#!/usr/bin/env python3
"""Kapesní kartičky — na každé jedna otázka a její ODPOVĚĎ, k vytištění a rozstříhání.

    python3 nastroje/gen_tahaky.py

Formát: **12 karet na stránku A4** (3 sloupce × 4 řady), karta zhruba 66 × 71 mm.
136 otázek = 12 listů. Tiskni jednostranně, měřítko 100 %, rozstříhej po linkách.

⚠️ Text karet je **psaný ručně** v `nastroje/farmakologie_karty.py`, ne skládaný
z útržků. Každá karta odpovídá na otázku souvisle: co to je → jak to funguje →
dělení a zástupci → k čemu → nežádoucí účinky a kontraindikace. Cílem je, aby se
karta dala PŘEČÍST a člověk to věděl.
"""
import html
import re
import subprocess
import sys
from pathlib import Path

KOREN = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(KOREN / "nastroje"))
import farmakologie_karty as fk  # noqa: E402

CIL = KOREN / "Projekty/Studium/Predmety/Farmakologie/minimum"
CHROMIUM = ["/opt/pw-browsers/chromium", "/usr/bin/chromium", "/usr/bin/chromium-browser"]

SLOUPCU, RADU = 3, 4
NA_STRANU = SLOUPCU * RADU
LIMIT_ZNAKU = 1400         # kolik textu se na kartu vejde; přes to se hlásí varování


def sazba(text: str) -> str:
    """**Tučné** a nadpisy úseků; text se sází jako souvislý odstavcový blok."""
    t = html.escape(" ".join(text.split()))
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", t)
    t = t.replace(" · ", " &middot; ")
    return t


def karta(cislo: str, nadpis: str, text: str) -> str:
    return (f'<div class="k"><div class="h">'
            f'<span class="n">{html.escape(cislo)}</span>'
            f'<span class="t">{html.escape(nadpis)}</span></div>'
            f'<div class="o">{sazba(text)}</div></div>')


STYL = """
@page { size: A4; margin: 6mm; }
* { box-sizing: border-box; }
body { margin: 0; font-family: Calibri, Carlito, Arial, sans-serif;
       -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.list { display: grid; grid-template-columns: repeat(3, 1fr);
        grid-template-rows: repeat(4, 71.25mm);
        gap: 0; height: 285mm; page-break-after: always; }
.list:last-child { page-break-after: auto; }
.k { border: 1px dashed #B9C7C2; padding: 2mm 2.2mm; overflow: hidden;
     min-height: 0; min-width: 0; display: flex; flex-direction: column; }
.h { display: flex; align-items: baseline; gap: 1.4mm; border-bottom: 1.2pt solid #1B6B5F;
     padding-bottom: 0.7mm; margin-bottom: 1mm; }
.n { font-size: 9.4pt; font-weight: 700; color: #1B6B5F; }
.t { font-size: 7.2pt; font-weight: 700; line-height: 1.1; }
.o { font-size: 6.15pt; line-height: 1.31; text-align: justify;
     hyphens: auto; -webkit-hyphens: auto; }
.o b { font-weight: 700; }
"""


def main() -> None:
    poradi = sorted(fk.KARTY, key=lambda z: (0 if z[0].startswith("O") else 1,
                                             int(z[0].lstrip("O"))))
    dlouhe = [(c, len(t)) for c, _, t in poradi if len(t) > LIMIT_ZNAKU]
    kratke = [(c, len(t)) for c, _, t in poradi if len(t) < 950]
    karty = [karta(c, n, t) for c, n, t in poradi]
    listy = ["<div class='list'>" + "".join(karty[i:i + NA_STRANU]) + "</div>"
             for i in range(0, len(karty), NA_STRANU)]
    doc = (f"<html><head><meta charset='utf-8'><title>Kartičky — farmakologie</title>"
           f"<style>{STYL}</style></head><body>{''.join(listy)}</body></html>")
    htm = CIL / "TAHACKY.html"
    htm.write_text(doc, encoding="utf-8")

    chrom = next((c for c in CHROMIUM if Path(c).exists()), None)
    if not chrom:
        raise SystemExit("Chromium nenalezen")
    pdf = CIL / "TAHACKY.pdf"
    subprocess.run([chrom, "--headless", "--disable-gpu", "--no-sandbox",
                    "--no-pdf-header-footer", f"--print-to-pdf={pdf}", htm.as_uri()],
                   check=True, capture_output=True)
    print(f"{pdf.name} · {len(karty)} karet · {len(listy)} listů")
    if dlouhe:
        print("  ⚠️ přeteče:", dlouhe)
    if kratke:
        print("  ⚠️ zbytečně prázdné:", kratke)


if __name__ == "__main__":
    main()
