#!/usr/bin/env python3
"""Kapesní kartičky — jedna otázka na jednu malou kartu, k vytištění a rozstříhání.

    python3 nastroje/gen_tahaky.py

Formát: **12 karet na stránku A4** (3 sloupce × 4 řady), karta zhruba 66 × 71 mm —
velikost hrací karty. 136 otázek = 12 listů. Tiskni jednostranně a rozstříhej
po čárkovaných linkách.

Obsah kartičky je **automaticky zhuštěný** z `farmakologie_sketch.py` a vysázený
**odborným registrem**: jen fakta — definice a mechanismus, dělení se zástupci,
indikace, nežádoucí účinky, kontraindikace a interakce. **Vynechává se zubní přesah,
mnemotechnika a jakýkoli komentář k učení**; zvýrazňovací piktogramy se odstraňují.
Když se opraví sketchnota, přegenerují se i kartičky.
"""
import html
import re
import subprocess
import sys
from pathlib import Path

KOREN = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(KOREN / "nastroje"))
import farmakologie_sketch as fs  # noqa: E402

CIL = KOREN / "Projekty/Studium/Predmety/Farmakologie/minimum"
CHROMIUM = ["/opt/pw-browsers/chromium", "/usr/bin/chromium", "/usr/bin/chromium-browser"]

SLOUPCU, RADU = 3, 4
NA_STRANU = SLOUPCU * RADU
MAX_BODU = 11
VYSKA_KARTY_RADKU = 22   # kolik řádků se na kartu vejde (odhad pro rozpočet)
ZNAKU_NA_RADEK = 55      # užší karta → dřív se zalomí; odtud plynou i limity zkracování


# Karta má být odborný text, ne studijní poznámka: pryč jde zubní přesah,
# komentáře k učení a piktogramy.
DENTALNI = re.compile(
    r"(zubař|zubní ordinac|zubním lékařství|zubaře|extrakc|sanace chrupu|sanaci chrupu|"
    r"protéz|kazivost|alveolitid|ústní hygien|parodontitid|gingivostomatitid|epulis|"
    r"dutiny ústní|chrupu)", re.I)
META = re.compile(
    r"(u zkoušky|zkoušející|zkoušková|chytají|naučit se|odvodíš|se ptají|vděčn|"
    r"nejdůležitější věta|k naučení|nezaměňovat|nepleť)", re.I)
PIKTOGRAMY = re.compile(r"[⚠️🔑🦷⭐⬆⬇]|️")


def _odborne(s: str) -> str:
    """Odstraní piktogramy a uvozovací značky, ať text zní jako odborný zápis."""
    s = PIKTOGRAMY.sub("", s)
    s = re.sub(r"^\s*[-–—:·→]\s*", "", s)
    s = re.sub(r"\(\s+", "(", s)
    s = re.sub(r"\[\s+", "[", s)
    s = re.sub(r"\s+([)\]])", r"\1", s)
    return " ".join(s.split())


def _vhodne(s: str) -> bool:
    return not DENTALNI.search(s) and not META.search(s)


def _zkrat(s: str, limit: int) -> str:
    """Zkrátí text na limit znaků — přednostně na konci věty nebo úseku."""
    s = " ".join(s.split())
    if len(s) <= limit:
        return s
    rez = s[:limit]
    for delic in ("; ", " — ", ", ", " "):
        i = rez.rfind(delic)
        if i > limit * 0.55:
            return rez[:i].rstrip(" ,;—") + "…"
    return rez.rstrip() + "…"


def _duraz(s: str) -> str:
    """Termíny psané VERZÁLKAMI se vysází tučně — na kartě nesou hlavní váhu."""
    s = html.escape(s)
    s = re.sub(r"\b([A-ZÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ]{3,}(?:[ -][A-ZÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ]{2,})*)\b",
               r"<b>\1</b>", s)
    return s


def _radku(text: str, na_radek: float) -> float:
    return max(1, -(-len(text) // int(na_radek)))


def karta(cislo, nadpis, kw) -> str:
    tok = kw.get("tok") or []
    retez = " → ".join(_zkrat(_odborne(t), 34) for t, _ in tok[:4])

    # ⚠️ Kolik řádků na kartě ještě zbývá na odrážky. Bez tohohle rozpočtu se
    # u hustých otázek poslední řádky uřízly (karta má overflow:hidden).
    zbyva = VYSKA_KARTY_RADKU
    zbyva -= 2.4 if len(nadpis) > 30 else 1.7
    if retez:
        zbyva -= _radku(retez, ZNAKU_NA_RADEK + 8) + 0.4

    body, videno, radku = [], set(), 0.0

    def pridej(b):
        nonlocal radku
        if not _vhodne(b):
            return
        t = _zkrat(_odborne(b), 100)
        if not t or t in videno or len(body) >= MAX_BODU:
            return
        odhad = _radku(t, ZNAKU_NA_RADEK)
        if radku + odhad > zbyva:
            return
        videno.add(t)
        body.append(t)
        radku += odhad

    # nejdřív rizikové položky (nežádoucí účinky, kontraindikace, interakce),
    # pak zbytek dělení a zástupců
    for _, polozky, _ in kw.get("karty") or []:
        for b in polozky:
            if "⚠️" in b:
                pridej(b)
    for _, polozky, _ in kw.get("karty") or []:
        for b in polozky:
            pridej(b)

    casti = [f'<div class="h"><span class="n">{html.escape(str(cislo))}</span>'
             f'<span class="t">{html.escape(nadpis)}</span></div>']
    if retez:
        casti.append(f'<div class="r">{_duraz(retez)}</div>')
    if body:
        casti.append("<ul>" + "".join(f"<li>{_duraz(b)}</li>" for b in body) + "</ul>")
    return '<div class="k">' + "".join(casti) + "</div>"


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
     padding-bottom: 0.8mm; margin-bottom: 1.2mm; }
.n { font-size: 9.6pt; font-weight: 700; color: #1B6B5F; }
.t { font-size: 7.4pt; font-weight: 700; line-height: 1.1; }
.r { font-size: 6pt; line-height: 1.2; color: #1B6B5F; font-weight: 600;
     border-left: 2pt solid #1B6B5F; padding-left: 1.4mm; margin-bottom: 1.2mm; }
ul { margin: 0 0 1mm; padding-left: 2.8mm; }
li { font-size: 6pt; line-height: 1.24; margin-bottom: 0.5mm; }
b { font-weight: 700; }
"""


def main() -> None:
    poradi = sorted(fs.DATA, key=lambda z: (0 if str(z[0]).startswith("O") else 1,
                                            int(str(z[0]).lstrip("O"))))
    karty = [karta(c, n, kw) for c, n, kw in poradi]
    listy = ["<div class='list'>" + "".join(karty[i:i + NA_STRANU]) + "</div>"
             for i in range(0, len(karty), NA_STRANU)]
    doc = (f"<html><head><meta charset='utf-8'><title>Taháčky — farmakologie</title>"
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


if __name__ == "__main__":
    main()
