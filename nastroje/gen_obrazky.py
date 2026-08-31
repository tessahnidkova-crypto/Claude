#!/usr/bin/env python3
"""Sestaví z `farmakologie_obrazky.py` obrázkový atlas (.md → .pdf).

    python3 nastroje/gen_obrazky.py

Výstup: Projekty/Studium/Predmety/Farmakologie/minimum/OBRAZKY-VSE.{md,pdf}
Zdrojem je Python skript, ne ručně psaný markdown — když se schéma opraví,
přegeneruje se celý atlas jednou.
"""
import subprocess
import sys
from pathlib import Path

KOREN = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(KOREN / "nastroje"))
import farmakologie_obrazky as fo  # noqa: E402

CIL = KOREN / "Projekty/Studium/Predmety/Farmakologie/minimum"

UVOD = """# OBRÁZKY — jedno schéma ke každé otázce

**Ke každé ze 136 zkouškových otázek jeden obrázek, který nese její hlavní myšlenku.**
Není to náhrada textu — je to to, co si máš vybavit, když se u zkoušky zasekneš.
Text ke stejným otázkám je ve `VYCUC-FINAL`.

> **Jak to číst:** ⚠️ **červený rámeček = past nebo nežádoucí účinek** ·
> **zelený rámeček = jádro věci** · **červená věta pod obrázkem = co si z něj odnést.**

---
"""


def main() -> None:
    casti = [UVOD]
    for cislo, nadpis, svg in fo.O:
        casti.append(f"## {cislo} · {nadpis}\n\n{svg}\n\n---\n")
    md = "\n".join(casti)
    md_cesta = CIL / "OBRAZKY-VSE.md"
    md_cesta.write_text(md, encoding="utf-8")
    print(f"{md_cesta.name} · {len(fo.O)} schémat")
    subprocess.run([sys.executable, str(KOREN / "nastroje/md2pdf.py"),
                    str(md_cesta), str(CIL / "OBRAZKY-VSE.pdf")], check=True)


if __name__ == "__main__":
    main()
