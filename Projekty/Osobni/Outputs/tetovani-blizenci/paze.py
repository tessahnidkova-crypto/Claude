#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Varianty pro PAZI: uzky vysoky format, skutecna pismena K a O + kvety."""
import sys, math
sys.path.insert(0, "/home/user/Claude/Projekty/Osobni/Outputs/tetovani-blizenci")
from generator import *

def stem(a, b, bow=18, w=1.0):
    mx, my = (a[0]+b[0])/2, (a[1]+b[1])/2
    return (f'<path d="M {a[0]:.1f} {a[1]:.1f} Q {mx+bow:.1f} {my:.1f} {b[0]:.1f} {b[1]:.1f}" '
            f'fill="none" stroke="#111" stroke-width="{w}" stroke-linecap="round"/>')

def scurve(a, b, c1, c2, w=1.0):
    return (f'<path d="M {a[0]:.1f} {a[1]:.1f} C {c1[0]:.1f} {c1[1]:.1f} {c2[0]:.1f} {c2[1]:.1f} '
            f'{b[0]:.1f} {b[1]:.1f}" fill="none" stroke="#111" stroke-width="{w}" '
            f'stroke-linecap="round"/>')

LW = 1.15

def kytice(cx, base_y, fork_y, k_off=(-62, -120), o_off=(56, -74),
           k_r=22, o_r=18, w=1.25):
    """dva stonky s kvety z jednoho korene; vraci (svg, pozice_K_kvetu, pozice_O_kvetu)"""
    base = (cx + 4, base_y); fork = (cx - 2, fork_y)
    P = [stem(base, fork, bow=20, w=w)]
    k_tip = (fork[0] + k_off[0], fork[1] + k_off[1])
    P.append(stem(fork, k_tip, bow=-22, w=w*0.88))
    P.append(petal_flower(k_tip[0], k_tip[1] - k_r*0.6, k_r, rot=-90, petals=5,
                          w=w*0.88, center_r=k_r*0.10))
    o_tip = (fork[0] + o_off[0], fork[1] + o_off[1])
    P.append(stem(fork, o_tip, bow=18, w=w*0.85))
    P.append(petal_flower(o_tip[0], o_tip[1] - o_r*0.6, o_r, rot=-70, petals=5,
                          w=w*0.85, center_r=o_r*0.10))
    P.append(leaf(base[0]-5, base[1]-(base_y-fork_y)*0.44, 40, 206, w=w*0.85))
    P.append(leaf(base[0]+3, base[1]-(base_y-fork_y)*0.78, 33, -20, w=w*0.85))
    return "\n".join(P), (k_tip[0], k_tip[1]-k_r*0.6), (o_tip[0], o_tip[1]-o_r*0.6)

# ---------------------------------------------------------------- 1
def v1(cx, top, sz=430):
    """MEZI NIMI: pismena ve volnem prostoru mezi obema postavami"""
    m = make_mapper(cx, top + sz*0.5, sz)
    P = [constellation(m, w=LW, star_scale=1.15)]
    # prazdny pruh mezi figurami: relativne ke stredu
    GH = 62
    P.append(glyph("K", cx - 74, top + sz*0.47, GH, w=1.3))
    P.append(glyph("O", cx - 19, top + sz*0.47, GH, w=1.3))
    k, _, _ = kytice(cx, top + sz + 350, top + sz + 168)
    P.append(k)
    return "\n".join(P)

# ---------------------------------------------------------------- 2
def v2(cx, top, sz=430):
    """KAZDY SVUJ KVET: pismeno patri ke kvetu"""
    m = make_mapper(cx, top + sz*0.5, sz)
    P = [constellation(m, w=LW, star_scale=1.15)]
    k, kp, op = kytice(cx, top + sz + 360, top + sz + 172,
                       k_off=(-66, -128), o_off=(62, -76), k_r=24, o_r=20)
    P.append(k)
    P.append(glyph("K", kp[0] - 74, kp[1] - 22, 50, w=1.45))
    P.append(glyph("O", op[0] + 24, op[1] - 20, 50, w=1.45))
    return "\n".join(P)

# ---------------------------------------------------------------- 3
def v3(cx, top, sz=330):
    """PISMENA JAKO ZAKLAD: souhvezdi - kytice - velka K a O pod sebou"""
    m = make_mapper(cx, top + sz*0.5, sz)
    P = [constellation(m, w=LW, star_scale=1.05)]
    k, _, _ = kytice(cx, top + sz + 218, top + sz + 128,
                     k_off=(-54, -84), o_off=(48, -52), k_r=19, o_r=16, w=1.2)
    P.append(k)
    GH = 148
    gy = top + sz + 248
    P.append(glyph("K", cx - 122, gy, GH, w=1.75))
    P.append(glyph("O", cx + 22, gy, GH, w=1.75))
    return "\n".join(P)

# ================= list =================
if __name__ == "__main__":
    PW, PH = 560, 1080
    W, H = PW*3, PH + 60
    CX = [PW*0.5, PW*1.5, PW*2.5]
    P = [f'<rect width="{W}" height="{H}" fill="#fbfaf8"/>']
    P.append(f'<text x="{W/2}" y="58" text-anchor="middle" font-family="Georgia,serif" '
             f'font-size="33" fill="#111" letter-spacing="4">BLÍŽENCI NA PAŽI &#8212; s písmeny a květy</text>')
    P.append(f'<text x="{W/2}" y="89" text-anchor="middle" font-family="Georgia,serif" '
             f'font-size="16.5" fill="#9a9a9a" font-style="italic">'
             f'úzký svislý formát &#183; K a O jako skutečná písmena</text>')
    titles = [("1 &#183; MEZI NIMI", "písmena uvnitř souhvězdí"),
              ("2 &#183; KAŽDÝ SVŮJ KVĚT", "písmeno patří ke svému květu"),
              ("3 &#183; PÍSMENA JAKO ZÁKLAD", "písmena jsou hlavní prvek")]
    for i, (t, s) in enumerate(titles):
        P.append(f'<text x="{CX[i]}" y="152" text-anchor="middle" font-family="Georgia,serif" '
                 f'font-size="25" fill="#111" letter-spacing="1.5">{t}</text>')
        P.append(f'<text x="{CX[i]}" y="181" text-anchor="middle" font-family="Georgia,serif" '
                 f'font-size="16" fill="#8b8b8b" font-style="italic">{s}</text>')
    for i in (1, 2):
        P.append(f'<line x1="{PW*i}" y1="115" x2="{PW*i}" y2="{H-30}" stroke="#e6e2da" stroke-width="1"/>')
    P.append(v1(CX[0], 232))
    P.append(v2(CX[1], 232))
    P.append(v3(CX[2], 232))
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
           f'viewBox="0 0 {W} {H}">' + "\n".join(P) + '</svg>')
    open("/home/user/Claude/Projekty/Osobni/Outputs/tetovani-blizenci/paze-varianty.svg","w").write(svg)
    print("ok", W, H)
