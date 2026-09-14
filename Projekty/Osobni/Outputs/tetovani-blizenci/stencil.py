#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ciste podklady pro tatera: cerna na bile, bez popisku, vektorove (SVG)."""
import sys
sys.path.insert(0, "/home/user/Claude/Projekty/Osobni/Outputs/tetovani-blizenci")
from generator import *

def stem(a, b, bow=18, w=1.0):
    mx, my = (a[0]+b[0])/2, (a[1]+b[1])/2
    return (f'<path d="M {a[0]:.1f} {a[1]:.1f} Q {mx+bow:.1f} {my:.1f} {b[0]:.1f} {b[1]:.1f}" '
            f'fill="none" stroke="#000" stroke-width="{w}" stroke-linecap="round"/>')

W, H = 760, 980
CX, CY, SZ = W/2, H/2, 760

def build(variant, flip=False):
    m = make_mapper(CX, CY, SZ, flip=flip)
    LW = 1.3
    hi = ("Mebsuta", "Wasat") if variant in ("C", "D") else ()
    P = [f'<rect width="{W}" height="{H}" fill="#fff"/>']
    P.append(constellation(m, w=LW, star_scale=1.3, highlight=hi))
    if variant in ("A", "D"):
        P.append(morse_on_arc(m("Castor"), m("Pollux"), bulge=0.16, letters=("K",),
                              w=LW+0.25, up=True,  fit=0.86)[0])
        P.append(morse_on_arc(m("Alhena"), m("Propus"), bulge=0.10, letters=("O",),
                              w=LW+0.25, up=False, fit=0.78)[0])
    if variant == "B":
        bx, by = CX+6, CY+336
        fork = (CX, CY+66)
        P.append(stem((bx, by), fork, bow=26, w=1.35))
        k_tip = (fork[0]-68, fork[1]-136)
        P.append(stem(fork, k_tip, bow=-26, w=1.2))
        P.append(petal_flower(k_tip[0], k_tip[1]-13, 23, rot=-90, petals=5, w=1.25, center_r=2.4))
        o_tip = (fork[0]+58, fork[1]-86)
        P.append(stem(fork, o_tip, bow=20, w=1.2))
        P.append(bud(o_tip[0], o_tip[1]-2, 21, angle=-58, w=1.15))
        P.append(leaf(bx-5, by-104, 45, 206, w=1.15))
        P.append(leaf(bx+3, by-178, 37, -18, w=1.15))
    if variant == "D":
        bx, by = CX+6, CY+318
        tip = (CX-36, CY+128)
        P.append(stem((bx, by), tip, bow=22, w=1.2))
        P.append(petal_flower(tip[0], tip[1]-11, 20, rot=-90, petals=5, w=1.1, center_r=2.0))
        P.append(leaf(bx-5, by-80, 38, 204, w=1.05))
    body = "\n".join(P).replace('#111', '#000')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
            f'viewBox="0 0 {W} {H}">' + body + '</svg>')

base = "/home/user/Claude/Projekty/Osobni/Outputs/tetovani-blizenci/"
for v in ("A", "B", "C", "D"):
    open(base + f"stencil-{v}.svg", "w").write(build(v))
open(base + "stencil-D-zrcadlove.svg", "w").write(build("D", flip=True))
print("hotovo: stencil-A/B/C/D + zrcadlova D")
