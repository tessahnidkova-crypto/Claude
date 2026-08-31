#!/usr/bin/env python3
"""Sketchnote — ručně kreslený přehled CELÉ zkouškové otázky na jednu stranu.

Rozdíl proti `schemata.py`: tam jeden obrázek = jedna myšlenka. Tady jedna
stránka = celá otázka (mechanismus + dělení + zástupci + nežádoucí účinky +
pasti + zubařský přesah + mnemotechnika).

Vzhled: rámečky a šipky se kreslí **rozechvělým tahem** (jitterované cesty
kreslené nadvakrát, jako když člověk obtáhne čáru tužkou), zvýraznění se dělá
**šrafováním** a **zvýrazňovačem**. Ručně psané písmo v kontejneru není
(fonty se nedají stáhnout), takže se sází bezpatkovým — čitelnost má přednost.

Náhodnost je **seedovaná číslem otázky**, takže přegenerování dá tentýž obrázek.
"""

W = 900
H_MAX = 1310                 # využitelná výška A4 při okrajích z md2pdf

INK = "#23303A"              # tužka
PAPER = "#FFFDF7"            # papír
ACCENT = "#1B6B5F"
CRIT = "#9C3628"
BLUE = "#28556E"
HIGH_Y = "#FDE9A8"           # zvýrazňovač žlutý
HIGH_R = "#F7CFC4"           # růžový
HIGH_B = "#CFE3EC"           # modrý
HIGH_G = "#CDE6DC"           # zelený

CH = 0.545


class _Rnd:
    """Malý deterministický generátor — ať je obrázek po přegenerování stejný."""

    def __init__(self, seed: int):
        self.s = (seed * 2654435761) % 4294967291 or 12345

    def next(self) -> float:
        self.s = (1103515245 * self.s + 12345) % 2147483648
        return self.s / 2147483648

    def sym(self, a: float) -> float:
        return (self.next() * 2 - 1) * a


_R = _Rnd(1)


def seed(n: int) -> None:
    global _R
    _R = _Rnd(n + 7)


def _esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def wrap(text: str, sirka: float, fs: float) -> list[str]:
    maxz = max(4, int(sirka / (fs * CH)))
    radky, akt = [], ""
    for slovo in text.split():
        z = (akt + " " + slovo).strip()
        if len(z) <= maxz:
            akt = z
        else:
            if akt:
                radky.append(akt)
            akt = slovo
    if akt:
        radky.append(akt)
    return radky


def vyska_textu(text: str, sirka: float, fs: float) -> float:
    return len(wrap(text, sirka, fs)) * fs * 1.32


# ------------------------------------------------------------------ kreslení

def rough_line(x1, y1, x2, y2, barva=INK, w=1.9, tahy=2, jitter=3.0):
    """Čára kreslená nadvakrát s mírným prohnutím — vypadá jako tažená rukou."""
    out = []
    for _ in range(tahy):
        mx = (x1 + x2) / 2 + _R.sym(jitter * 2)
        my = (y1 + y2) / 2 + _R.sym(jitter * 2)
        out.append(
            f'<path d="M{x1 + _R.sym(jitter):.1f},{y1 + _R.sym(jitter):.1f} '
            f'Q{mx:.1f},{my:.1f} {x2 + _R.sym(jitter):.1f},{y2 + _R.sym(jitter):.1f}" '
            f'fill="none" stroke="{barva}" stroke-width="{w}" stroke-linecap="round" '
            f'opacity="0.75"/>')
    return "".join(out)


def rough_rect(x, y, w, h, barva=INK, sw=1.9, r=6, jitter=3.4, tahy=2):
    """Obdélník se zaoblenými rohy, obtažený rozechvělým tahem."""
    out = []
    for _ in range(tahy):
        j = lambda a=jitter: _R.sym(a)  # noqa: E731
        d = (f"M{x + r + j():.1f},{y + j():.1f} "
             f"L{x + w - r + j():.1f},{y + j():.1f} "
             f"Q{x + w + j():.1f},{y + j():.1f} {x + w + j():.1f},{y + r + j():.1f} "
             f"L{x + w + j():.1f},{y + h - r + j():.1f} "
             f"Q{x + w + j():.1f},{y + h + j():.1f} {x + w - r + j():.1f},{y + h + j():.1f} "
             f"L{x + r + j():.1f},{y + h + j():.1f} "
             f"Q{x + j():.1f},{y + h + j():.1f} {x + j():.1f},{y + h - r + j():.1f} "
             f"L{x + j():.1f},{y + r + j():.1f} "
             f"Q{x + j():.1f},{y + j():.1f} {x + r + j():.1f},{y + j():.1f}")
        out.append(f'<path d="{d}" fill="none" stroke="{barva}" stroke-width="{sw}" '
                   f'stroke-linecap="round" stroke-linejoin="round" opacity="0.8"/>')
    return "".join(out)


def podklad(x, y, w, h, barva, opacita=0.55, r=10):
    """Měkká barevná plocha pod rámečkem — jako podmalování vodovkou."""
    return (f'<rect x="{x + 1:.1f}" y="{y + 1:.1f}" width="{w - 2:.1f}" '
            f'height="{h - 2:.1f}" rx="{r}" fill="{barva}" opacity="{opacita}"/>')


def hachure(x, y, w, h, barva=ACCENT, rozestup=9, opacita=0.30):
    """Šrafování šikmými tahy — sketchnote zvýraznění."""
    cary = []
    i = -h
    while i < w:
        x1, y1 = x + max(i, 0), y + max(-i, 0)
        delka = min(w - max(i, 0), h - max(-i, 0))
        x2, y2 = x1 + delka, y1 + delka
        cary.append(f'<path d="M{x1:.1f},{y1 + _R.sym(1):.1f} L{x2:.1f},{y2 + _R.sym(1):.1f}" '
                    f'stroke="{barva}" stroke-width="1.1" opacity="{opacita}"/>')
        i += rozestup
    return "".join(cary)


def zvyraznovac(x, y, w, h, barva=HIGH_Y):
    """Tah zvýrazňovačem — nepravidelné konce, jako když se přejede fixem."""
    return (f'<path d="M{x:.1f},{y + h / 2:.1f} L{x + w:.1f},{y + h / 2 + _R.sym(1.5):.1f}" '
            f'stroke="{barva}" stroke-width="{h:.1f}" stroke-linecap="round" '
            f'opacity="0.85"/>')


def sipka(x1, y1, x2, y2, barva=INK, w=1.7):
    """Šipka s ručně dokreslenou špičkou."""
    import math
    s = rough_line(x1, y1, x2, y2, barva, w, tahy=2, jitter=1.4)
    uh = math.atan2(y2 - y1, x2 - x1)
    for d in (2.6, -2.6):
        hx = x2 - 13 * math.cos(uh + d * 0.32)
        hy = y2 - 13 * math.sin(uh + d * 0.32)
        s += rough_line(x2, y2, hx, hy, barva, w, tahy=1, jitter=0.9)
    return s


def text(x, y, radky, fs=14, barva=INK, anchor="start", tucne=False, halo=False,
         kurziva=False):
    kusy = []
    ob = ' stroke="%s" stroke-width="3.2" paint-order="stroke"' % PAPER if halo else ""
    it = ' font-style="italic"' if kurziva else ""
    for n, r in enumerate(radky):
        kusy.append(f'<text x="{x:.1f}" y="{y + n * fs * 1.32:.1f}" font-size="{fs}" '
                    f'font-weight="{"700" if tucne else "400"}" fill="{barva}" '
                    f'text-anchor="{anchor}"{ob}{it}>{_esc(r)}</text>')
    return "".join(kusy)


def platno(vnitrek, h):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h:.0f}" '
            f'width="100%" style="max-width:100%;height:auto;display:block" '
            f'font-family="Liberation Sans, Carlito, Calibri, Arial, sans-serif">'
            f'<rect x="0" y="0" width="{W}" height="{h:.0f}" fill="{PAPER}"/>'
            f'{vnitrek}</svg>')


# ------------------------------------------------------------------ sketchnote

BARVY = {
    "zelena": (ACCENT, HIGH_G),
    "cervena": (CRIT, HIGH_R),
    "modra": (BLUE, HIGH_B),
    "zluta": ("#8A6A18", HIGH_Y),
    "bila": (INK, None),
}

OKRAJ = 26
SLOUPEC = (W - 2 * OKRAJ - 20) / 2


def _karta_vyska(karta):
    _, body, _ = karta
    h = 34
    for b in body:
        h += vyska_textu(b, SLOUPEC - 34, 14.6) + 3
    return h + 14


def _karta(x, y, karta):
    nadpis, body, klic = karta
    barva, vypln = BARVY.get(klic, BARVY["bila"])
    h = _karta_vyska(karta)
    out = ""
    if vypln:
        out += podklad(x, y, SLOUPEC, h, vypln, 0.42)
    out += rough_rect(x, y, SLOUPEC, h, barva, 2.0)
    out += text(x + 14, y + 23, wrap(nadpis, SLOUPEC - 24, 16.0), 16.0, barva, tucne=True)
    out += rough_line(x + 12, y + 30, x + 12 + min(SLOUPEC - 24, len(nadpis) * 8.2), y + 30,
                      barva, 1.2, tahy=1, jitter=1.0)
    ty = y + 48
    for b in body:
        radky = wrap(b, SLOUPEC - 34, 14.6)
        out += f'<circle cx="{x + 17:.1f}" cy="{ty - 4.5:.1f}" r="2.4" fill="{barva}" opacity="0.75"/>'
        out += text(x + 26, ty, radky, 14.6, INK)
        ty += len(radky) * 14.6 * 1.32 + 3
    return out, h


def _banner(x, y, sirka, znak, obsah, barva, vypln):
    radky = wrap(obsah, sirka - 74, 14.6)
    h = max(38, len(radky) * 14.6 * 1.32 + 20)
    out = podklad(x, y, sirka, h, vypln, 0.55, r=8)
    out += rough_rect(x, y, sirka, h, barva, 1.9, r=6)
    out += text(x + 16, y + h / 2 + 6, [znak], 17, barva, tucne=True)
    out += text(x + 52, y + (h - len(radky) * 14.6 * 1.32) / 2 + 12, radky, 14.6, INK)
    return out, h


def sketchnote(cislo, nadpis, jadro="", tok=None, tok_popisky=None, karty=None,
               mnemo="", zubar="", past="", vyska=0):
    """Celá otázka na jednu stranu, kreslená rukou.

    tok    = [(text, klic), ...]  vodorovný pás mechanismu nahoře
    karty  = [(nadpis, [body], klic), ...]  dlaždice ve dvou sloupcích
    """
    seed(sum(ord(c) for c in str(cislo)) * 31 + len(nadpis))
    tok = tok or []
    tok_popisky = tok_popisky or []
    karty = karty or []
    o = ""

    # ---- hlavička: číslo v kroužku + název + podtržení
    o += rough_rect(OKRAJ, 20, 78, 46, ACCENT, 2.3, r=22, jitter=2.4)
    o += podklad(OKRAJ, 20, 78, 46, HIGH_G, 0.5, r=22)
    o += text(OKRAJ + 39, 52, [str(cislo)], 24, ACCENT, anchor="middle", tucne=True)
    nr = wrap(nadpis, W - OKRAJ * 2 - 104, 23)
    o += text(OKRAJ + 96, 46 - (len(nr) - 1) * 10, nr, 23, INK, tucne=True)
    y = 20 + max(46, len(nr) * 27) + 12
    o += rough_line(OKRAJ, y, W - OKRAJ, y, INK, 2.0, tahy=2, jitter=2.2)
    y += 16

    # ---- jádro otázky: jedna věta pod zvýrazňovačem
    if jadro:
        radky = wrap(jadro, W - 2 * OKRAJ - 30, 16.5)
        for n in range(len(radky)):
            sirka = min(len(radky[n]) * 16.5 * CH + 10, W - 2 * OKRAJ - 20)
            o += zvyraznovac(OKRAJ + 4, y + n * 22 - 6, sirka, 21, HIGH_Y)
        o += text(OKRAJ + 8, y + 5, radky, 16.5, INK, tucne=True)
        y += len(radky) * 22 + 18

    # ---- pás mechanismu
    if tok:
        n = len(tok)
        mez = 76
        bw = (W - 2 * OKRAJ - mez * (n - 1)) / n
        bh = 0
        for t, _ in tok:
            bh = max(bh, vyska_textu(t, bw - 20, 14.6) + 24)
        bh = max(bh, 56)
        popisky_pozdeji = []
        for i, (t, klic) in enumerate(tok):
            x = OKRAJ + i * (bw + mez)
            barva, vypln = BARVY.get(klic, BARVY["bila"])
            if vypln:
                o += podklad(x, y, bw, bh, vypln, 0.45, r=8)
            o += rough_rect(x, y, bw, bh, barva, 2.0, r=6)
            radky = wrap(t, bw - 20, 14.6)
            o += text(x + bw / 2, y + bh / 2 - len(radky) * 8.7 + 13, radky, 14.6,
                      INK, anchor="middle")
            if i < n - 1:
                o += sipka(x + bw + 6, y + bh / 2, x + bw + mez - 6, y + bh / 2, ACCENT)
                if i < len(tok_popisky) and tok_popisky[i]:
                    pr = wrap(tok_popisky[i], mez + 56, 12.2)
                    popisky_pozdeji.append(
                        text(x + bw + mez / 2, y - 6 - (len(pr) - 1) * 15, pr,
                             12.2, ACCENT, anchor="middle", halo=True))
        o += "".join(popisky_pozdeji)
        y += bh + 18

    # ---- dlaždice ve dvou sloupcích (kratší sloupec dostane další kartu)
    ly = ry = y
    for k in karty:
        if ly <= ry:
            blok, h = _karta(OKRAJ, ly, k)
            ly += h + 12
        else:
            blok, h = _karta(OKRAJ + SLOUPEC + 20, ry, k)
            ry += h + 12
        o += blok
    y = max(ly, ry) + 4

    # ---- pruhy dole
    for znak, obsah, barva, vypln in (("🔑", mnemo, "#8A6A18", HIGH_Y),
                                      ("🦷", zubar, BLUE, HIGH_B),
                                      ("⚠️", past, CRIT, HIGH_R)):
        if obsah:
            blok, h = _banner(OKRAJ, y, W - 2 * OKRAJ, znak, obsah, barva, vypln)
            o += blok
            y += h + 10

    return platno(o, max(vyska, y + 16))
