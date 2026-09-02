#!/usr/bin/env python3
"""Paměťová SCÉNA v duchu Sketchy — jedna velká ilustrace na otázku.

Princip: otázka se nepřevádí na seznam, ale na **jedno místo**. Scéna má svůj
děj a v ní jsou rozmístěné **symboly**; každý symbol znamená jeden fakt.
Člověk si zapamatuje obraz a pak se po něm „prochází“ a odečítá z něj látku.

Rozdíl proti `mnemo.py`: tam byly čtyři oddělené rámečky vedle sebe, což je
pořád jen seznam s obrázky. Tady je **jeden souvislý prostor** — objekty mají
polohu, velikost (popředí × pozadí) a vztah k sobě, protože právě prostorové
uspořádání je to, co paměť drží.

⚠️ Symbol smí být přehnaný, ale legenda se píše odborně a doslova — chybná
mnemotechnika se naučí stejně pevně jako správná.

Náhodnost je seedovaná číslem otázky, takže přegenerování dá tentýž obrázek.
"""
from sketch import (ACCENT, BLUE, CRIT, HIGH_R, HIGH_Y, INK, PAPER, W, _esc,
                    platno, podklad, rough_line, rough_rect, seed, text, wrap)

OKRAJ = 26
SIRKA = W - 2 * OKRAJ
VYSKA_SCENY = 470

# Prostředí = „kde se to odehrává“. Samo o sobě je prvním paměťovým vodítkem,
# proto se volí tak, aby ho šlo s tématem spojit (ledviny → vodárna apod.).
PROSTREDI = {
    "krajina":  ("#DCEBF5", "#D8E8C8", 0.60, "#9CBF7A"),
    "poust":    ("#F6E7C8", "#EFD9A4", 0.58, "#D9BC72"),
    "more":     ("#D5EAF2", "#A9D3E4", 0.55, "#7FB9CE"),
    "pokoj":    ("#F2EDE2", "#E3D8C6", 0.66, "#C9B99E"),
    "laborator": ("#E6EEF0", "#D3DEE1", 0.64, "#B4C4C8"),
    "noc":      ("#2E3D50", "#3E4F63", 0.62, "#5A6E85"),
    "les":      ("#DFEAD8", "#C6DCB4", 0.58, "#8FB472"),
    "hory":     ("#E4EDF4", "#DEE6EA", 0.56, "#AFC0CB"),
}


def _kulisy(prostredi, yh, cara):
    """Pár nakreslených kulis, aby prostředí bylo poznat na první pohled."""
    s = ""
    if prostredi in ("krajina", "les", "hory", "poust"):
        # chalupa vlevo vzadu
        bx, by = OKRAJ + SIRKA * 0.06, yh - 6
        s += rough_rect(bx, by - 74, 96, 74, cara, sw=2.0, jitter=2.2)
        s += rough_line(bx - 10, by - 74, bx + 48, by - 116, cara, w=2.0, jitter=2.4)
        s += rough_line(bx + 48, by - 116, bx + 106, by - 74, cara, w=2.0, jitter=2.4)
        # plot vpravo
        for i in range(7):
            px = OKRAJ + SIRKA * 0.70 + i * 26
            s += rough_line(px, yh + 6, px, yh - 42, cara, w=1.7, tahy=1, jitter=1.8)
        s += rough_line(OKRAJ + SIRKA * 0.70, yh - 28,
                        OKRAJ + SIRKA * 0.70 + 6 * 26, yh - 28, cara, w=1.7, jitter=2.0)
    elif prostredi in ("pokoj", "laborator"):
        # pracovní stůl přes celou šířku a police vzadu
        s += rough_line(OKRAJ + 20, yh + 40, OKRAJ + SIRKA - 20, yh + 40,
                        cara, w=2.6, jitter=2.2)
        for px in (OKRAJ + 70, OKRAJ + SIRKA - 70):
            s += rough_line(px, yh + 40, px, VYSKA_SCENY - 20, cara, w=2.2, jitter=2.0)
        for i in range(2):
            s += rough_line(OKRAJ + SIRKA * 0.60, yh - 40 - i * 46,
                            OKRAJ + SIRKA * 0.94, yh - 40 - i * 46, cara, w=2.0, jitter=2.2)
        s += rough_rect(OKRAJ + SIRKA * 0.08, yh - 150, 120, 96, cara, sw=2.0, jitter=2.2)
    elif prostredi == "more":
        for i in range(4):
            yv = yh + 22 + i * 30
            s += rough_line(OKRAJ + 30, yv, OKRAJ + SIRKA - 30, yv, cara,
                            w=1.6, tahy=1, jitter=5.0)
    # vzdálené kopce
    for i in range(3):
        x = OKRAJ + SIRKA * (0.16 + 0.33 * i)
        s += rough_line(x - 80, yh, x, yh - 40 - 14 * i, cara, w=1.6, tahy=1, jitter=3.0)
        s += rough_line(x, yh - 40 - 14 * i, x + 88, yh, cara, w=1.6, tahy=1, jitter=3.0)
    return s


def _pozadi(prostredi):
    """Obloha, země a horizont — aby scéna byla místo, ne mřížka."""
    horni, dolni, hor, cara = PROSTREDI.get(prostredi, PROSTREDI["krajina"])
    yh = VYSKA_SCENY * hor
    s = (f'<rect x="{OKRAJ}" y="0" width="{SIRKA}" height="{yh:.0f}" fill="{horni}"/>'
         f'<rect x="{OKRAJ}" y="{yh:.0f}" width="{SIRKA}" '
         f'height="{VYSKA_SCENY - yh:.0f}" fill="{dolni}"/>')
    s += _kulisy(prostredi, yh, cara)
    s += rough_line(OKRAJ, yh, OKRAJ + SIRKA, yh, cara, w=2.2, tahy=2, jitter=2.6)
    return s


def _cislo(n, x, y, barva):
    """Číselný štítek u symbolu — spojuje obraz s legendou."""
    return (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="15" fill="{PAPER}" '
            f'stroke="{barva}" stroke-width="2.4"/>'
            f'<text x="{x:.1f}" y="{y + 6:.1f}" font-size="17" font-weight="700" '
            f'fill="{barva}" text-anchor="middle">{n}</text>')


def _scena(prvky, prostredi):
    """Symboly rozmístěné v prostoru; větší = blíž, tedy důležitější."""
    s = _pozadi(prostredi)
    for n, p in enumerate(prvky, 1):
        _, fx, fy, vel = p[0], p[1], p[2], p[3] * 1.34
        x = OKRAJ + SIRKA * fx
        y = VYSKA_SCENY * fy
        barva = CRIT if len(p) > 5 and p[5] else ACCENT
        # měkký stín pod objektem, ať „stojí“ na zemi a nelevituje
        s += (f'<ellipse cx="{x:.1f}" cy="{y + vel * 0.30:.1f}" rx="{vel * 0.38:.1f}" '
              f'ry="{vel * 0.10:.1f}" fill="{INK}" opacity="0.12"/>')
        s += text(x, y + vel * 0.34, [p[0]], fs=vel, anchor="middle")
        s += _cislo(n, x + vel * 0.40, y - vel * 0.34, barva)
    return s


def _legenda(prvky, y):
    """Očíslovaný klíč: symbol → co doopravdy znamená."""
    lev = 268
    s = text(OKRAJ, y + 14, ["CO JE VE SCÉNĚ"], fs=13.5, tucne=True, barva=ACCENT)
    yy = y + 36
    for n, p in enumerate(prvky, 1):
        nazev, fakt = p[4], p[6] if len(p) > 6 else ""
        barva = CRIT if len(p) > 5 and p[5] else BLUE
        rl = wrap(nazev, lev - 58, 15.4)
        rp = wrap(fakt, W - 2 * OKRAJ - lev - 10, 15.4)
        vys = max(len(rl), len(rp)) * 15.4 * 1.32
        s += _cislo(n, OKRAJ + 15, yy + 8, barva)
        s += text(OKRAJ + 38, yy + 13, rl, fs=15.4, tucne=True, barva=barva)
        s += text(OKRAJ + lev, yy + 13, rp, fs=15.4)
        yy += vys + 12
    return s, yy - y + 6


def _misto(misto, y):
    """Název místa — samotné prostředí je první paměťové vodítko."""
    radky = wrap(misto, SIRKA - 44, 19)
    h = len(radky) * 19 * 1.32 + 28
    s = podklad(OKRAJ, y, SIRKA, h, HIGH_Y, opacita=0.5)
    s += rough_rect(OKRAJ, y, SIRKA, h, "#8A6A18", sw=2.1)
    s += text(OKRAJ + 20, y + 25, radky, fs=19, tucne=True, barva="#4A3A08")
    return s, h + 18


def _past(past, y):
    radky = wrap(past, SIRKA - 40, 14.6)
    h = len(radky) * 14.6 * 1.32 + 26
    s = podklad(OKRAJ, y, SIRKA, h, HIGH_R, opacita=0.42)
    s += rough_rect(OKRAJ, y, SIRKA, h, CRIT, sw=2.0)
    s += text(OKRAJ + 14, y + 22, ["⚠️"], fs=15)
    s += text(OKRAJ + 40, y + 22, radky, fs=14.6, barva="#5E1F14")
    return s, h + 12


def scenka(cislo, nadpis, misto, prostredi, prvky, past=None):
    """Jedna otázka = jedno místo, po kterém se dá projít a odečíst látku.

    misto     — věta, která scénu pojmenuje a spojí s tématem
    prostredi — klíč z PROSTREDI (krajina, poust, more, pokoj, laborator, noc…)
    prvky     — n-tice (glyf, x, y, velikost, název, kriticke, fakt);
                x a y jsou zlomky 0–1 uvnitř scény, velikost je stupeň písma
    past      — nejčastější omyl u téhle otázky
    """
    seed(int(str(cislo).lstrip("O")) * 17 + 3)
    casti = []
    y = 18

    # hlavička
    casti.append(text(OKRAJ, y + 30, [str(cislo)], fs=34, barva=ACCENT, tucne=True))
    odsaz = OKRAJ + 26 + 20 * len(str(cislo))
    radky = wrap(nadpis, W - odsaz - OKRAJ, 21)
    casti.append(text(odsaz, y + 26, radky, fs=21, tucne=True))
    h = max(44, 26 + len(radky) * 21 * 1.32)
    casti.append(rough_rect(OKRAJ, y + h, SIRKA, 0.1, ACCENT, sw=2.4, r=0, jitter=1.6))
    y += h + 16

    kus, vys = _misto(misto, y)
    casti.append(kus)
    y += vys

    # scéna se kreslí do vlastní soustavy, proto posun přes <g transform>
    casti.append(f'<g transform="translate(0,{y:.1f})">{_scena(prvky, prostredi)}'
                 f'</g>')
    casti.append(rough_rect(OKRAJ, y, SIRKA, VYSKA_SCENY, INK, sw=2.4, r=8, jitter=2.4))
    y += VYSKA_SCENY + 20

    kus, vys = _legenda(prvky, y)
    casti.append(kus)
    y += vys

    if past:
        kus, vys = _past(past, y)
        casti.append(kus)
        y += vys

    return platno("".join(casti), y + 14)
