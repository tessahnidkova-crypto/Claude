#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ctyri koncepty navrhu tetovani na jeden list."""
import sys, math
sys.path.insert(0, "/home/user/Claude/Projekty/Osobni/Outputs/tetovani-blizenci")
from generator import *

W, H = 1700, 1700
CX = [425, 1275, 425, 1275]
CYs = [520, 520, 1310, 1310]
SIZE = 520
LW = 1.0

def head(i, title, sub):
    x = CX[i]; y = CYs[i] - 320
    return (f'<text x="{x}" y="{y}" text-anchor="middle" font-family="Georgia,serif" '
            f'font-size="28" fill="#111" letter-spacing="2">{title}</text>'
            f'<text x="{x}" y="{y+31}" text-anchor="middle" font-family="Georgia,serif" '
            f'font-size="16.5" fill="#8b8b8b" font-style="italic">{sub}</text>')

def foot(i, txt):
    return (f'<text x="{CX[i]}" y="{CYs[i]+330}" text-anchor="middle" font-family="Georgia,serif" '
            f'font-size="16" fill="#8b8b8b">{txt}</text>')

def stem(p_from, p_to, bow=18, w=1.0):
    """jemny prohnuty stonek"""
    mx, my = (p_from[0]+p_to[0])/2, (p_from[1]+p_to[1])/2
    return (f'<path d="M {p_from[0]:.1f} {p_from[1]:.1f} Q {mx+bow:.1f} {my:.1f} '
            f'{p_to[0]:.1f} {p_to[1]:.1f}" fill="none" stroke="#111" stroke-width="{w}" '
            f'stroke-linecap="round"/>')

P = [f'<rect width="{W}" height="{H}" fill="#fbfaf8"/>']
P.append(f'<text x="{W/2}" y="62" text-anchor="middle" font-family="Georgia,serif" '
         f'font-size="33" fill="#111" letter-spacing="4">BLÍŽENCI &#8212; máma &amp; dcera</text>')
P.append(f'<text x="{W/2}" y="92" text-anchor="middle" font-family="Georgia,serif" '
         f'font-size="16" fill="#9a9a9a" font-style="italic">Castor a Pollux &#183; dvě postavy, které se drží &#183; K a O ukryté v linii</text>')
P.append(f'<line x1="{W/2}" y1="130" x2="{W/2}" y2="{H-40}" stroke="#e6e2da" stroke-width="1"/>')
P.append(f'<line x1="60" y1="{(CYs[0]+CYs[2])/2}" x2="{W-60}" y2="{(CYs[0]+CYs[2])/2}" stroke="#e6e2da" stroke-width="1"/>')

# ---------- A: POUTO ----------
m = make_mapper(CX[0], CYs[0], SIZE)
P.append(head(0, "A &#183; POUTO", "K nahoře, O dole"))
P.append(constellation(m, w=LW))
P.append(morse_on_arc(m("Castor"), m("Pollux"), bulge=0.16, letters=("K",), w=LW+0.2, up=True,  fit=0.86)[0])
P.append(morse_on_arc(m("Alhena"), m("Propus"), bulge=0.10, letters=("O",), w=LW+0.2, up=False, fit=0.78)[0])
P.append(foot(0, "děti drží obě postavy &#8212; nad hlavami i pod nohama"))

# ---------- B: DVĚ KVĚTINY ----------
m = make_mapper(CX[1], CYs[1], SIZE)
P.append(head(1, "B &#183; DVĚ KVĚTINY", "jeden stonek, dvě děti"))
P.append(constellation(m, w=LW))
bx, by = CX[1]+6, CYs[1]+250
fork = (CX[1], CYs[1]+48)
P.append(stem((bx, by), fork, bow=20, w=1.05))
# vetev 1 -> rozvity kvet (Kacka)
k_tip = (fork[0]-52, fork[1]-104)
P.append(stem(fork, k_tip, bow=-20, w=0.95))
P.append(petal_flower(k_tip[0], k_tip[1]-10, 19, rot=-90, petals=5))
# vetev 2 -> poupe (Ondra)
o_tip = (fork[0]+44, fork[1]-66)
P.append(stem(fork, o_tip, bow=16, w=0.95))
P.append(bud(o_tip[0], o_tip[1]-2, 15, angle=-58))
P.append(leaf(bx-4, by-78, 34, 206))
P.append(leaf(bx+2, by-134, 28, -18))
P.append(foot(1, "rozvitý květ = Kačka, poupě = Ondra"))

# ---------- C: DVĚ HVĚZDY ----------
m = make_mapper(CX[2], CYs[2], SIZE)
P.append(head(2, "C &#183; DVĚ HVĚZDY", "nejtišší varianta"))
P.append(constellation(m, w=LW, highlight=("Mebsuta", "Wasat")))
a, b = m("Mebsuta"), m("Wasat")
mx, my = (a[0]+b[0])/2, (a[1]+b[1])/2
P.append(f'<path d="M {a[0]:.1f} {a[1]:.1f} Q {mx:.1f} {my+40:.1f} {b[0]:.1f} {b[1]:.1f}" '
         f'fill="none" stroke="#111" stroke-width="0.8" stroke-dasharray="1.3 4.0" '
         f'stroke-linecap="round"/>')
P.append(foot(2, "dvě zářící hvězdy uvnitř obou postav"))

# ---------- D: KOMBINACE ----------
m = make_mapper(CX[3], CYs[3], SIZE)
P.append(head(3, "D &#183; KOMBINACE", "doporučeno"))
P.append(constellation(m, w=LW, highlight=("Mebsuta", "Wasat")))
P.append(morse_on_arc(m("Castor"), m("Pollux"), bulge=0.16, letters=("K",), w=LW+0.2, up=True,  fit=0.86)[0])
P.append(morse_on_arc(m("Alhena"), m("Propus"), bulge=0.10, letters=("O",), w=LW+0.2, up=False, fit=0.78)[0])
bx, by = CX[3]+4, CYs[3]+232
tip = (CX[3]-26, CYs[3]+96)
P.append(stem((bx, by), tip, bow=16, w=0.95))
P.append(petal_flower(tip[0], tip[1]-9, 15, rot=-90, petals=5))
P.append(leaf(bx-4, by-58, 27, 204))
P.append(foot(3, "morseovka + dvě hvězdy + jedna větvička"))

svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
       f'viewBox="0 0 {W} {H}">' + "\n".join(P) + '</svg>')
open("/home/user/Claude/Projekty/Osobni/Outputs/tetovani-blizenci/varianty.svg","w").write(svg)
print("ok", len(svg))
