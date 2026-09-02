#!/usr/bin/env python3
"""Sestaví z `farmakologie_sceny.py` atlas paměťových scén (.md → .pdf).

    python3 nastroje/gen_sceny.py

Jedna otázka = jedno místo = jedna strana. Výstup:
Projekty/Studium/Predmety/Farmakologie/minimum/SCENY.{md,pdf}
"""
import re
import subprocess
import sys
from pathlib import Path

KOREN = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(KOREN / "nastroje"))
import farmakologie_sceny as fs  # noqa: E402

CIL = KOREN / "Projekty/Studium/Predmety/Farmakologie/minimum"
ZLOM = '<div style="break-after:page"></div>'


def _poradi(zaznam):
    cislo = str(zaznam[0])
    return (0 if cislo.startswith("O") else 1, int(cislo.lstrip("O")))


def main() -> None:
    casti = [f"{svg}\n{ZLOM}\n" for _, _, svg in sorted(fs.O, key=_poradi)]
    md_cesta = CIL / "SCENY.md"
    md_cesta.write_text("\n".join(casti), encoding="utf-8")
    pdf = CIL / "SCENY.pdf"
    subprocess.run([sys.executable, str(KOREN / "nastroje/md2pdf.py"),
                    str(md_cesta), str(pdf)], check=True)

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

    ocekavane = {f"O{i}" for i in range(1, 36)} | {str(i) for i in range(36, 137)}
    chybi = sorted(ocekavane - {c for c, _, _ in fs.O},
                   key=lambda c: (0 if c.startswith("O") else 1, int(c.lstrip("O"))))
    print(f"{pdf.name} · {len(fs.O)} otázek · {d.page_count} stran · {len(toc)} záložek")
    if chybi:
        print("  ⚠️ chybí:", chybi)


if __name__ == "__main__":
    main()
