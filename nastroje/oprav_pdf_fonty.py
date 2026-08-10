#!/usr/bin/env python3
"""Oprava rozbitého kódování textu v PDF (nečitelná extrakce textu).

PROBLÉM, KTERÝ TOHLE ŘEŠÍ
-------------------------
Některá PDF (typicky export z Wordu přes Microsoft Print to PDF) mají u
vložených fontů **neúplnou nebo prázdnou tabulku ToUnicode**. Extrakce textu
pak vrací nesmysly typu ``%,G'H<D:3*7L FG<BDA-,-7`` místo ``Zdravotnický
prostředek``. Text se nedá číst, hledat ani kopírovat — jen vytisknout.

Nejde o šifru ani o skenovaný obrázek. Znaky, které vidíš, jsou **čísla glyfů**
(GID) vypsaná jako písmena. Skutečné přiřazení „glyf → znak" je pořád uložené
v tabulce ``cmap`` vloženého fontu — jen ho PDF nepoužívá.

CO SKRIPT DĚLÁ
--------------
1. Najde všechny fonty typu ``Type0`` s vloženým souborem ``FontFile2``.
2. Z jejich ``cmap`` sestaví převod GID → Unicode.
3. Z toho vygeneruje **správnou tabulku ToUnicode** a zapíše ji zpět do PDF.
4. Uloží opravenou kopii. Originál zůstává nedotčený.

Vzhled ani obsah dokumentu se nemění — mění se jen to, co se z něj dá přečíst.

POUŽITÍ
-------
    python3 nastroje/oprav_pdf_fonty.py vstup.pdf vystup.pdf

Závislosti: ``pip install pymupdf fonttools``

KDY TO NEPOMŮŽE
---------------
- PDF je **sken** (stránka je obrázek) → potřebuje OCR, ne tenhle skript.
- Vložený font nemá tabulku ``cmap`` (plně podmnožinový font bez znakových
  jmen) → skript to ohlásí a font přeskočí.

⚠️ Po opravě si **vždy zkontroluj pár stránek proti originálu.** Skript hlásí,
kolik fontů opravil; když je to 0, text zůstal stejně nečitelný.

Historie: napsáno 2026-08-10 pro `Inputs/obecka-podrobna-cast1.pdf`
(podrobná Obecka 2024/2025), kde 12 fontů mělo prázdnou ToUnicode a kvůli tomu
se 100 stran otázek O1–O16 nedalo číst jinak než jako obrázek.
"""

import io
import re
import sys

import pymupdf
from fontTools.ttLib import TTFont

CMAP_HLAVICKA = (
    "/CIDInit /ProcSet findresource begin\n"
    "12 dict begin\n"
    "begincmap\n"
    "/CIDSystemInfo <</Registry (Adobe) /Ordering (UCS) /Supplement 0>> def\n"
    "/CMapName /Adobe-Identity-UCS def\n"
    "/CMapType 2 def\n"
    "1 begincodespacerange\n<0000><FFFF>\nendcodespacerange\n"
)
CMAP_PATICKA = "endcmap\nCMapName currentdict /CMap defineresource pop\nend\nend\n"


def _glyf_na_unicode(font_bytes):
    """Z vloženého TrueType fontu sestaví převod GID → Unicode."""
    font = TTFont(io.BytesIO(font_bytes))
    poradi = {jmeno: i for i, jmeno in enumerate(font.getGlyphOrder())}
    prevod = {}
    for tabulka in font["cmap"].tables:
        # (3,1) = Windows Unicode BMP, (3,10) = Windows Unicode plný rozsah
        if tabulka.platformID == 3 and tabulka.platEncID in (1, 10):
            for uni, jmeno in tabulka.cmap.items():
                if jmeno in poradi:
                    prevod.setdefault(poradi[jmeno], uni)
    return prevod


def _sestav_tounicode(prevod):
    radky = [f"<{gid:04X}> <{uni:04X}>" for gid, uni in sorted(prevod.items())]
    # bfchar smí mít nejvýš 100 položek v jednom bloku
    bloky = [radky[i:i + 100] for i in range(0, len(radky), 100)]
    telo = "".join(
        f"{len(blok)} beginbfchar\n" + "\n".join(blok) + "\nendbfchar\n"
        for blok in bloky
    )
    return CMAP_HLAVICKA + telo + CMAP_PATICKA


def oprav(vstup, vystup):
    dok = pymupdf.open(vstup)
    opraveno, preskoceno = 0, []

    for xref in range(1, dok.xref_length()):
        try:
            obj = dok.xref_object(xref, compressed=True)
        except Exception:
            continue
        if "/Subtype/Type0" not in obj:
            continue

        m_tu = re.search(r"/ToUnicode (\d+) 0 R", obj)
        m_df = re.search(r"/DescendantFonts\[(\d+) 0 R", obj)
        if not (m_tu and m_df):
            continue

        potomek = dok.xref_object(int(m_df.group(1)), compressed=True)
        m_fd = re.search(r"/FontDescriptor (\d+) 0 R", potomek)
        if not m_fd:
            continue
        popis = dok.xref_object(int(m_fd.group(1)), compressed=True)
        m_ff = re.search(r"/FontFile2 (\d+) 0 R", popis)
        if not m_ff:
            continue

        jmeno = re.search(r"/BaseFont/(\S+?)[/ >]", obj)
        jmeno = jmeno.group(1) if jmeno else f"xref {xref}"

        try:
            prevod = _glyf_na_unicode(dok.xref_stream(int(m_ff.group(1))))
        except Exception as chyba:
            preskoceno.append(f"{jmeno}: {chyba}")
            continue

        if not prevod:
            preskoceno.append(f"{jmeno}: font nemá použitelnou cmap")
            continue

        dok.update_stream(int(m_tu.group(1)), _sestav_tounicode(prevod).encode("latin-1"))
        opraveno += 1

    dok.save(vystup)
    print(f"Opraveno fontů: {opraveno}")
    for radek in preskoceno:
        print(f"  přeskočeno — {radek}")
    if opraveno == 0:
        print("⚠️ Neopraven žádný font. Text bude nejspíš pořád nečitelný —")
        print("   zkontroluj, jestli PDF není sken (pak je potřeba OCR).")
    else:
        print(f"Uloženo: {vystup}")
        print("⚠️ Zkontroluj pár stránek proti originálu, než výstup použiješ.")
    return opraveno


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(f"Použití: {sys.argv[0]} vstup.pdf vystup.pdf")
    oprav(sys.argv[1], sys.argv[2])
