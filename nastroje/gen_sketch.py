#!/usr/bin/env python3
"""Sestaví z `farmakologie_sketch.py` sketchnotový atlas (.md → .pdf).

    python3 nastroje/gen_sketch.py

Jedna otázka = jedna strana. Výstup:
Projekty/Studium/Predmety/Farmakologie/minimum/SKETCHNOTES.{md,pdf}
"""
import re
import subprocess
import sys
from pathlib import Path

KOREN = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(KOREN / "nastroje"))
import farmakologie_sketch as fs  # noqa: E402

CIL = KOREN / "Projekty/Studium/Predmety/Farmakologie/minimum"
ZLOM = '<div style="break-after:page"></div>'


def _poradi(zaznam):
    """Otázky se řadí podle čísla, ne podle pořadí zápisu v souboru."""
    cislo = str(zaznam[0])
    return (0 if cislo.startswith("O") else 1, int(cislo.lstrip("O")))


def main() -> None:
    casti = []
    for cislo, nadpis, svg in sorted(fs.O, key=_poradi):
        casti.append(f"{svg}\n{ZLOM}\n")
    md = "\n".join(casti)
    md_cesta = CIL / "SKETCHNOTES.md"
    md_cesta.write_text(md, encoding="utf-8")
    pdf = CIL / "SKETCHNOTES.pdf"
    subprocess.run([sys.executable, str(KOREN / "nastroje/md2pdf.py"),
                    str(md_cesta), str(pdf)], check=True)

    # záložky: jedna na otázku, ať se dá skočit rovnou na číslo
    import pymupdf
    d = pymupdf.open(pdf)
    toc, videno = [], set()
    for i in range(d.page_count):
        radky = d[i].get_text().splitlines()
        for n, r in enumerate(radky):
            r = r.strip()
            if re.fullmatch(r"O?\d{1,3}", r) and r not in videno:
                nazev = radky[n + 1].strip() if n + 1 < len(radky) else ""
                videno.add(r)
                toc.append([1, f"{r} · {nazev[:70]}", i + 1])
                break
    d.set_toc(toc)
    d.saveIncr()
    print(f"{pdf.name} · {len(fs.O)} otázek · {d.page_count} stran · {len(toc)} záložek")


if __name__ == "__main__":
    main()
