#!/usr/bin/env python3
"""Převede markdown z vaultu na PDF k tisku a čtení na tabletu.

Použití:
    python3 nastroje/md2pdf.py vstup.md [vystup.pdf] ["Titulek"]
    python3 nastroje/md2pdf.py --slozka Projekty/Studium/Predmety/Farmakologie/zkracene

Jak to funguje: markdown se převede na HTML stejným kódem jako `md2gdoc.py`
(takže dokument vypadá v PDF i na Disku stejně), přidá se tisková šablona
a stránku vytiskne headless Chromium.

⚠️ **PDF je export, ne originál.** Zdrojem zůstává markdown v repu — když se
bude materiál za měsíc přepisovat, edituje se `.md` a PDF se přegeneruje.
Viz pravidlo „ulož ZDROJ, ne jen export" v CLAUDE.md.

Co tisková šablona řeší:
- **okraje 14 mm** a číslování stránek dole
- **tabulky a bloky se netrhají přes stránky** (`break-inside: avoid`)
- za nadpisem nezůstane osamocený řádek na konci stránky
- barvy se tisknou (`print-color-adjust: exact`), jinak by zmizely hlavičky tabulek

Závislosti: Chromium (v tomhle kontejneru `/opt/pw-browsers/chromium`).
"""

import html
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from md2gdoc import convert  # noqa: E402  (sdílíme převodník, ať výstupy sedí)

CHROMIUM_CESTY = [
    "/opt/pw-browsers/chromium",
    "/usr/bin/chromium",
    "/usr/bin/chromium-browser",
    "/usr/bin/google-chrome",
]

TISKOVY_STYL = """
@page { size: A4; margin: 14mm 13mm 16mm 13mm; }
body { font-family: Calibri, Carlito, Arial, sans-serif; font-size: 10.5pt;
       line-height: 1.42; margin: 0;
       -webkit-print-color-adjust: exact; print-color-adjust: exact; }
h1 { font-size: 16pt; break-before: auto; break-after: avoid; }
h2 { font-size: 13pt; break-after: avoid; }
h3 { font-size: 11.5pt; break-after: avoid; }
h1, h2, h3 { break-inside: avoid; }
table { break-inside: avoid; font-size: 9.8pt; width: 100%; }
tr, td, th { break-inside: avoid; }
blockquote, ul, ol, li, p { break-inside: avoid; orphans: 3; widows: 3; }
code { font-family: Consolas, "DejaVu Sans Mono", monospace; }
img { max-width: 100%; }
"""


def najdi_chromium() -> str:
    for cesta in CHROMIUM_CESTY:
        if Path(cesta).exists():
            return cesta
    sys.exit("Nenašel jsem Chromium. Zkus doplnit cestu do CHROMIUM_CESTY.")


def uprav_velke_tabulky(telo: str) -> str:
    """Široké tabulky nechá zalomit — jinak přetečou přes okraj stránky."""
    return telo.replace("width:100%;border:1px solid", "width:100%;table-layout:auto;border:1px solid")


def md_na_pdf(vstup: Path, vystup: Path, titulek: str | None = None) -> Path:
    titulek = titulek or vstup.stem
    telo = uprav_velke_tabulky(convert(vstup.read_text(encoding="utf-8")))
    stranka = (
        "<html><head><meta charset='utf-8'>"
        f"<title>{html.escape(titulek)}</title>"
        f"<style>{TISKOVY_STYL}</style></head><body>{telo}</body></html>"
    )

    docasne = vystup.with_suffix(".tisk.html")
    docasne.write_text(stranka, encoding="utf-8")
    try:
        subprocess.run(
            [
                najdi_chromium(), "--headless", "--disable-gpu", "--no-sandbox",
                "--no-pdf-header-footer",
                f"--print-to-pdf={vystup}",
                docasne.resolve().as_uri(),
            ],
            check=True, capture_output=True, timeout=180,
        )
    finally:
        docasne.unlink(missing_ok=True)

    if not vystup.exists() or vystup.stat().st_size < 1000:
        sys.exit(f"PDF se nevytvořilo nebo je prázdné: {vystup}")
    return vystup


def main() -> None:
    argv = sys.argv[1:]
    if not argv:
        sys.exit(f"Použití: {sys.argv[0]} vstup.md [vystup.pdf] [\"Titulek\"]\n"
                 f"    nebo: {sys.argv[0]} --slozka <adresář s .md>")

    if argv[0] == "--slozka":
        slozka = Path(argv[1])
        soubory = sorted(p for p in slozka.glob("*.md") if p.name != "README.md")
        if not soubory:
            sys.exit(f"V {slozka} nejsou žádné .md soubory.")
        for md in soubory:
            pdf = md_na_pdf(md, md.with_suffix(".pdf"))
            print(f"  ✓ {pdf.name} · {pdf.stat().st_size // 1024} kB")
        print(f"Hotovo: {len(soubory)} PDF v {slozka}")
        return

    vstup = Path(argv[0])
    vystup = Path(argv[1]) if len(argv) > 1 else vstup.with_suffix(".pdf")
    titulek = argv[2] if len(argv) > 2 else None
    pdf = md_na_pdf(vstup, vystup, titulek)
    print(f"{pdf} · {pdf.stat().st_size // 1024} kB")


if __name__ == "__main__":
    main()
