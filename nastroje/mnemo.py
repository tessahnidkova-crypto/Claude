#!/usr/bin/env python3
"""Mnemotechnická scéna — obrázek, který si zapamatuješ MÍSTO seznamu faktů.

Rozdíl proti `sketch.py`: sketchnote je **přehled celé otázky** (mechanismus,
dělení, zástupci, nežádoucí účinky). Tady jde o něco jiného — o **paměťový hák**.
Stránka je krátký **obrázkový příběh o 3–4 obrazech**, který je schválně
konkrétní, přehnaný a absurdní, protože přesně takové věci si mozek pamatuje.
Pod ním je **rozklíčování**: co který obraz znamená.

⚠️ Mnemotechnika nikdy nesmí zakódovat nepravdu — chybný hák se naučí stejně
pevně jako správný a u zkoušky vypadne jako omyl. Proto se každý obraz páruje
s faktem doslova a rozklíčování se píše odborně.

Náhodnost je seedovaná číslem otázky, takže přegenerování dá tentýž obrázek.
"""
from sketch import (ACCENT, BLUE, CRIT, HIGH_B, HIGH_G, HIGH_R, HIGH_Y, INK, W,
                    hachure, platno, podklad, rough_rect, seed, sipka, text,
                    vyska_textu, wrap, zvyraznovac)

OKRAJ = 26
BARVY = {
    "zelena": (ACCENT, HIGH_G),
    "cervena": (CRIT, HIGH_R),
    "modra": (BLUE, HIGH_B),
    "zluta": ("#8A6A18", HIGH_Y),
}
PORADI = ["zelena", "modra", "zluta", "cervena"]


def _hlavicka(cislo, nadpis, y):
    """Číslo otázky + název, podtržené linkou."""
    s = text(OKRAJ, y + 30, [str(cislo)], fs=34, barva=ACCENT, tucne=True)
    odsaz = OKRAJ + 26 + 20 * len(str(cislo))
    radky = wrap(nadpis, W - odsaz - OKRAJ, 21)
    s += text(odsaz, y + 26, radky, fs=21, tucne=True)
    h = max(44, 26 + len(radky) * 21 * 1.32)
    s += rough_rect(OKRAJ, y + h, W - 2 * OKRAJ, 0.1, ACCENT, sw=2.4, r=0, jitter=1.6)
    return s, h + 16


def _hak(hak, y):
    """Věta, kterou si má člověk vybavit jako první — velká, přes zvýrazňovač."""
    radky = wrap(hak, W - 2 * OKRAJ - 44, 20)
    h = len(radky) * 20 * 1.32 + 30
    s = podklad(OKRAJ, y, W - 2 * OKRAJ, h, HIGH_Y, opacita=0.45)
    s += rough_rect(OKRAJ, y, W - 2 * OKRAJ, h, "#8A6A18", sw=2.1)
    for n, r in enumerate(radky):
        s += zvyraznovac(OKRAJ + 20, y + 16 + n * 20 * 1.32, min(len(r) * 10.6, W - 2 * OKRAJ - 40), 21)
    s += text(OKRAJ + 22, y + 26, radky, fs=20, tucne=True, barva="#4A3A08")
    return s, h + 20


def _panely(panely, y):
    """Obrázkový příběh — 3 až 4 rámečky vedle sebe, mezi nimi šipka."""
    n = len(panely)
    mezera = 26
    sirka = (W - 2 * OKRAJ - (n - 1) * mezera) / n
    popisky = [wrap(p[1], sirka - 40, 15.6) for p in panely]
    h = 132 + max(len(r) for r in popisky) * 14.6 * 1.32 + 20

    s = ""
    for i, (glyf, _) in enumerate(panely):
        x = OKRAJ + i * (sirka + mezera)
        barva, vypln = BARVY[PORADI[i % len(PORADI)]]
        s += podklad(x, y, sirka, h, vypln, opacita=0.4)
        s += rough_rect(x, y, sirka, h, barva, sw=2.2)
        s += text(x + sirka / 2, y + 100, [glyf], fs=82, anchor="middle")
        s += text(x + sirka / 2, y + 150, popisky[i], fs=14.6, anchor="middle",
                  tucne=True, barva=barva)
        if i < n - 1:
            s += sipka(x + sirka + 4, y + h / 2, x + sirka + mezera - 4, y + h / 2,
                       INK, 2.0)
    return s, h + 22


def _rozklic(rozklic, y):
    """Co který obraz doopravdy znamená — tady se mnemotechnika převádí na fakt."""
    lev = 250
    s = text(OKRAJ, y + 14, ["ROZKLÍČOVÁNÍ"], fs=13.5, tucne=True, barva=ACCENT)
    s += hachure(OKRAJ + 132, y + 4, W - 2 * OKRAJ - 132, 12, ACCENT, rozestup=7,
                 opacita=0.22)
    yy = y + 34
    for obraz, fakt in rozklic:
        rl = wrap(obraz, lev - 16, 15.4)
        rp = wrap(fakt, W - 2 * OKRAJ - lev - 10, 15.4)
        vys = max(len(rl), len(rp)) * 15.4 * 1.32
        s += text(OKRAJ + 4, yy + 12, rl, fs=15.4, tucne=True, barva=BLUE)
        s += text(OKRAJ + lev, yy + 12, rp, fs=15.4)
        yy += vys + 11
    return s, yy - y + 6


def _past(past, y):
    """Na co se u téhle otázky nejčastěji naletí."""
    radky = wrap(past, W - 2 * OKRAJ - 40, 14.6)
    h = len(radky) * 14.6 * 1.32 + 26
    s = podklad(OKRAJ, y, W - 2 * OKRAJ, h, HIGH_R, opacita=0.42)
    s += rough_rect(OKRAJ, y, W - 2 * OKRAJ, h, CRIT, sw=2.0)
    s += text(OKRAJ + 14, y + 22, ["⚠️"], fs=15)
    s += text(OKRAJ + 40, y + 22, radky, fs=14.6, barva="#5E1F14")
    return s, h + 12


def scena(cislo, nadpis, hak, panely, rozklic, past=None):
    """Jedna stránka = jedna otázka jako zapamatovatelný obraz.

    hak     — věta, která se má vybavit první
    panely  — 3–4 dvojice (glyf, popisek): obrázkový příběh
    rozklic — dvojice (co vidíš, co to znamená)
    past    — nejčastější omyl u téhle otázky
    """
    seed(int(str(cislo).lstrip("O")) * 13 + 5)
    y = 18
    casti = []
    for kus, vys in (_hlavicka(cislo, nadpis, y),):
        casti.append(kus)
        y += vys
    for f, a in ((_hak, hak), (_panely, panely), (_rozklic, rozklic)):
        kus, vys = f(a, y)
        casti.append(kus)
        y += vys
    if past:
        kus, vys = _past(past, y)
        casti.append(kus)
        y += vys
    return platno("".join(casti), y + 14)
