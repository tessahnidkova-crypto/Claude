#!/usr/bin/env python3
"""Kapesní kartičky — jedna otázka na jednu malou kartu, k vytištění a rozstříhání.

    python3 nastroje/gen_tahaky.py

Formát: **12 karet na stránku A4** (3 sloupce × 4 řady), karta zhruba 66 × 71 mm —
velikost hrací karty. 136 otázek = 12 listů. Tiskni jednostranně a rozstříhej
po čárkovaných linkách.

Struktura karty:
    ZAČÁTEK   dvě věty, kterými se otázka otevře — bere se z `VYCUC-FINAL.md`
    KOSTRA    osnova odpovědi jako šipkový řetěz — rovněž z `VYCUC-FINAL.md`
    ZÁKLAD    fakta z `farmakologie_sketch.py`: mechanismus, dělení se zástupci,
              indikace, nežádoucí účinky, kontraindikace, interakce

Registr je odborný: **vynechává se zubní přesah, mnemotechnika a komentáře k učení**
a odstraňují se zvýrazňovací piktogramy. Text se nikdy neutíná uprostřed myšlenky —
položka, která by po zkrácení nedávala smysl, se raději vynechá a nastoupí další.
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
VYSKA_KARTY_RADKU = 22.5   # kolik řádků se na kartu vejde (odhad pro rozpočet)
ZNAKU_NA_RADEK = 55        # užší karta → dřív se zalomí

# „zub(ař|ní…)" zachytí zubaře i zubní lékařství, ale ne fakta typu „zbarvení zubů"
DENTALNI = re.compile(
    r"(zub(?:ař|n[ií])|extrakc|sanace chrupu|sanaci chrupu|protéz|kazivost|alveolitid|"
    r"ústní hygien|parodontitid|gingivostomatitid|epulis|dutiny ústní|chrupu)", re.I)
META = re.compile(
    r"(u zkoušky|zkoušející|zkoušková|chytají|naučit se|odvodíš|odvodím|se ptají|vděčn|"
    r"nejdůležitější věta|k naučení|nepleť|celá otázka|celé otázk|"
    r"tak s ním začnu|to je věta, kterou|pointa|chci ukázat|to je celý důvod|"
    r"proč se to změnilo|klíč k celé otázce|vypracovan|abych to vysvětlil|hned to zdůrazním|ve zdroji|zdroj (má|uvádí)|s ním začnu|začnu jím|to podstatné, čím začnu)", re.I)
PIKTOGRAMY = re.compile(r"[⚠️🔑🦷⭐⬆⬇]|️")
# Otázka 114 má začátek psaný přes zubařský přesah, takže ho filtr odstraní celý —
# tady je odborná náhrada.
NAHRADNI_ZACATEK = {
    "114": "Imunosupresiva se dělí podle místa zásahu do imunitní odpovědi: kortikoidy, "
           "kalcineurinové inhibitory, inhibitory mTOR, antiproliferativní látky a "
           "biologika. Společným rizikem celé skupiny jsou infekce včetně oportunních "
           "a vyšší výskyt nádorů.",
}
UVOD = re.compile(r"^(Odpověď otevřu[^:]*:|Chci [^:]*:|Začnu [^:]*:|Řeknu [^:]*:|"
                  r"Nejdřív [^:]*:)\s*")


def _odborne(s: str) -> str:
    """Odstraní piktogramy, markdown a uvozovky, ať text zní jako odborný zápis."""
    s = PIKTOGRAMY.sub("", s)
    s = s.replace("**", "").replace("*", "")   # kurzíva z markdownu
    s = s.replace("\u201e", "").replace("\u201c", "").replace('"', "")
    s = re.sub(r"^\s*[-–—:·→]\s*", "", s)
    s = re.sub(r"\(\s+", "(", s)
    s = re.sub(r"\[\s+", "[", s)
    s = re.sub(r"\s+([)\]])", r"\1", s)
    return " ".join(s.split())


def _vhodne(s: str) -> bool:
    return not DENTALNI.search(s) and not META.search(s)


def _cely(s: str, limit: int) -> str:
    """Text, který dává smysl: vejde se celý, nebo se uřízne na hranici úseku.

    Když by řez padl doprostřed myšlenky, vrací prázdno — položka se pak vynechá.
    """
    s = " ".join(s.split())
    if len(s) <= limit:
        return s
    rez = s[:limit]
    for delic in ("; ", " — ", ", "):
        i = rez.rfind(delic)
        if i > limit * 0.62:
            return rez[:i].rstrip(" ,;—")
    return ""


def _vety(s: str, limit: int) -> str:
    """Zkrátí na celé věty — pro dvouvětý začátek odpovědi."""
    s = " ".join(s.split())
    if len(s) <= limit:
        return s
    kus = ""
    for veta in re.split(r"(?<=[.!?]) ", s):
        if len(kus) + len(veta) + 1 > limit:
            break
        kus = (kus + " " + veta).strip()
    return kus


def nacti_vycuc() -> dict:
    """Ze `VYCUC-FINAL.md` vytáhne pro každou otázku začátek odpovědi a kostru."""
    text = (CIL / "VYCUC-FINAL.md").read_text(encoding="utf-8")
    out = {}
    for blok in re.split(r"(?m)^## ", text)[1:]:
        hlavicka = blok.split("\n", 1)[0]
        m = re.match(r"(O?\d{1,3})\s*·", hlavicka)
        if not m:
            continue
        z = re.search(r"▶ \*\*ZAČNI:\*\*\s*(.+)", blok)
        k = re.search(r"(?m)^\*\*KOSTRA:\*\*\s*(.+)", blok)
        zacatek = ""
        if z:
            cisty = UVOD.sub("", _odborne(z.group(1)))
            vety = [v for v in re.split(r"(?<=[.!?]) ", cisty) if _vhodne(v)]
            zacatek = " ".join(vety)
            if zacatek:
                zacatek = zacatek[0].upper() + zacatek[1:]
        zacatek = zacatek or NAHRADNI_ZACATEK.get(m.group(1), "")
        kostra = ""
        if k:
            useky = [u.strip() for u in _odborne(k.group(1)).split("→")]
            kostra = " → ".join(u for u in useky if u and _vhodne(u))
        out[m.group(1)] = (zacatek, kostra)
    return out


def _duraz(s: str) -> str:
    """Termíny psané VERZÁLKAMI se vysází tučně — na kartě nesou hlavní váhu."""
    s = html.escape(s)
    return re.sub(r"\b([A-ZÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ]{3,}(?:[ -][A-ZÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ]{2,})*)\b",
                  r"<b>\1</b>", s)


def _radku(text: str, na_radek: float) -> float:
    return max(1, -(-len(text) // int(na_radek)))


def _dve_vety(zacatek: str, kw: dict) -> str:
    """Dvě věty na úvod. Když filtr jednu odstranil, doplní se z jádra otázky."""
    vety = [v for v in re.split(r"(?<=[.!?]) ", zacatek) if v]
    if len(vety) < 2:
        # 1) jádro otázky, 2) první faktická odrážka — ať má úvod vždy dvě věty
        zdroje = [_odborne(kw.get("jadro", ""))]
        zdroje += [_odborne(b) for _, polozky, _ in (kw.get("karty") or [])
                   for b in polozky]
        for zdroj in zdroje:
            veta = re.split(r"(?<=[.!?]) ", zdroj)[0] if zdroj else ""
            if veta and _vhodne(veta) and veta not in vety and len(veta) > 25:
                vety.append(veta if veta.endswith((".", "!", "?")) else veta + ".")
                break
    return " ".join(vety[:3])


def karta(cislo, nadpis, kw, vycuc) -> str:
    zacatek, kostra = vycuc.get(str(cislo), ("", ""))
    zacatek = _vety(_dve_vety(zacatek, kw), 250)
    kostra = _cely(kostra, 170) or _cely(kostra, 120)

    zbyva = VYSKA_KARTY_RADKU
    zbyva -= 2.4 if len(nadpis) > 30 else 1.7
    if zacatek:
        zbyva -= _radku(zacatek, ZNAKU_NA_RADEK - 3) + 0.8
    if kostra:
        zbyva -= _radku(kostra, ZNAKU_NA_RADEK + 8) + 0.4

    body, videno, radku = [], set(), 0.0

    def pridej(b):
        nonlocal radku
        if not _vhodne(b):
            return
        t = _cely(_odborne(b), 100)
        if not t or t in videno:
            return
        odhad = _radku(t, ZNAKU_NA_RADEK)
        if radku + odhad > zbyva:
            return
        videno.add(t)
        body.append(t)
        radku += odhad

    # nejdřív rizikové položky (nežádoucí účinky, kontraindikace, interakce),
    # pak zbytek dělení a zástupců — dokud se karta nezaplní
    for _, polozky, _ in kw.get("karty") or []:
        for b in polozky:
            if "⚠️" in b:
                pridej(b)
    for _, polozky, _ in kw.get("karty") or []:
        for b in polozky:
            pridej(b)

    casti = [f'<div class="h"><span class="n">{html.escape(str(cislo))}</span>'
             f'<span class="t">{html.escape(nadpis)}</span></div>']
    if zacatek:
        casti.append(f'<div class="z">{_duraz(zacatek)}</div>')
    if kostra:
        casti.append(f'<div class="r">{_duraz(kostra)}</div>')
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
     padding-bottom: 0.8mm; margin-bottom: 1.1mm; }
.n { font-size: 9.6pt; font-weight: 700; color: #1B6B5F; }
.t { font-size: 7.4pt; font-weight: 700; line-height: 1.1; }
.z { font-size: 6.1pt; line-height: 1.26; background: #EAF1EE; padding: 1mm 1.4mm;
     border-radius: 1mm; margin-bottom: 1.1mm; }
.r { font-size: 5.9pt; line-height: 1.2; color: #1B6B5F; font-weight: 600;
     border-left: 2pt solid #1B6B5F; padding-left: 1.4mm; margin-bottom: 1.1mm; }
ul { margin: 0; padding-left: 2.8mm; }
li { font-size: 6pt; line-height: 1.24; margin-bottom: 0.45mm; }
b { font-weight: 700; }
"""


def main() -> None:
    vycuc = nacti_vycuc()
    poradi = sorted(fs.DATA, key=lambda z: (0 if str(z[0]).startswith("O") else 1,
                                            int(str(z[0]).lstrip("O"))))
    karty = [karta(c, n, kw, vycuc) for c, n, kw in poradi]
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
    bez_zacatku = [c for c, _, kw in poradi
                   if not _dve_vety(vycuc.get(str(c), ("", ""))[0], kw)]
    print(f"{pdf.name} · {len(karty)} karet · {len(listy)} listů "
          f"· bez začátku: {bez_zacatku or 'žádná'}")


if __name__ == "__main__":
    main()
