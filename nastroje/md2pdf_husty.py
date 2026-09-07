#!/usr/bin/env python3
"""Hustší sazba PDF — stejný převodník jako `md2pdf.py`, jen menší písmo a užší
řádkování, aby se dlouhý studijní materiál vešel do zadaného počtu stran.

Použití:
    python3 nastroje/md2pdf_husty.py vstup.md vystup.pdf "Titulek" [velikost_pt]

⚠️ Používej jen tam, kde je limit stran zadaný zvenčí (např. „max 80 stran").
Default `md2pdf.py` je čitelnější a zůstává preferovaný.
"""

import html
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from md2gdoc import convert  # noqa: E402
from md2pdf import najdi_chromium, uprav_velke_tabulky  # noqa: E402


def styl(pt: float) -> str:
    return f"""
@page {{ size: A4; margin: 10mm 10mm 12mm 10mm; }}
body {{ font-family: Calibri, Carlito, Arial, sans-serif; font-size: {pt}pt;
       line-height: 1.26; margin: 0;
       -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
h1 {{ font-size: {pt + 3.5}pt; margin: 0.5em 0 0.3em; break-after: avoid; }}
h2 {{ font-size: {pt + 1.6}pt; margin: 0.6em 0 0.25em; break-after: avoid; }}
h3 {{ font-size: {pt + 0.8}pt; margin: 0.4em 0 0.2em; break-after: avoid; }}
h1, h2, h3 {{ break-inside: avoid; }}
p {{ margin: 0.25em 0; }}
ul, ol {{ margin: 0.25em 0 0.25em 1.1em; padding-left: 0.6em; }}
li {{ margin: 0.12em 0; }}
table {{ break-inside: avoid; font-size: {pt - 0.6}pt; width: 100%; border-collapse: collapse; margin: 0.3em 0; }}
th, td {{ padding: 2px 4px; }}
tr, td, th {{ break-inside: avoid; }}
hr {{ margin: 0.4em 0; border: 0; border-top: 1px solid #ccc; }}
blockquote, ul, ol, li, p {{ break-inside: avoid; orphans: 2; widows: 2; }}
code {{ font-family: Consolas, "DejaVu Sans Mono", monospace; }}
img {{ max-width: 100%; }}
"""


def md_na_pdf(vstup: Path, vystup: Path, titulek: str, pt: float) -> Path:
    telo = uprav_velke_tabulky(convert(vstup.read_text(encoding="utf-8")))
    stranka = ("<html><head><meta charset='utf-8'>"
               f"<title>{html.escape(titulek)}</title>"
               f"<style>{styl(pt)}</style></head><body>{telo}</body></html>")
    docasne = vystup.with_suffix(".tisk.html")
    docasne.write_text(stranka, encoding="utf-8")
    try:
        subprocess.run(
            [najdi_chromium(), "--headless", "--disable-gpu", "--no-sandbox",
             "--no-pdf-header-footer", f"--print-to-pdf={vystup}",
             docasne.resolve().as_uri()],
            check=True, capture_output=True, timeout=300)
    finally:
        docasne.unlink(missing_ok=True)
    return vystup


if __name__ == "__main__":
    a = sys.argv[1:]
    vstup = Path(a[0])
    vystup = Path(a[1]) if len(a) > 1 else vstup.with_suffix(".pdf")
    titulek = a[2] if len(a) > 2 else vstup.stem
    pt = float(a[3]) if len(a) > 3 else 9.6
    pdf = md_na_pdf(vstup, vystup, titulek, pt)
    print(f"{pdf} · {pdf.stat().st_size // 1024} kB")
