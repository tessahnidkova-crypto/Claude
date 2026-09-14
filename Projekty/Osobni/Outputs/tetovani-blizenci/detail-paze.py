#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Detail doporucene varianty pro pazi + nahled na pazi."""
import sys, math
sys.path.insert(0, "/home/user/Claude/Projekty/Osobni/Outputs/tetovani-blizenci")
from generator import *
from paze import v2, kytice, stem

W, H = 1560, 1240
P = [f'<rect width="{W}" height="{H}" fill="#fbfaf8"/>']
P.append(f'<text x="{W/2}" y="54" text-anchor="middle" font-family="Georgia,serif" '
         f'font-size="31" fill="#111" letter-spacing="3">VARIANTA 2 &#8212; na paži</text>')

# ---------- levá půlka: návrh ve velkém ----------
CXa, TOP, SZ = 430, 130, 450
P.append(v2(CXa, TOP, SZ))

def note(x, y, txt, ax, ay, anchor="start"):
    return (f'<line x1="{x + (-9 if anchor=="end" else 9)}" y1="{y-5}" x2="{ax}" y2="{ay}" '
            f'stroke="#c6bfb1" stroke-width="0.9" stroke-dasharray="2 3"/>'
            f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Georgia,serif" '
            f'font-size="17.5" fill="#6f6a61">{txt}</text>')

m = make_mapper(CXa, TOP + SZ*0.5, SZ)
pp = m("Pollux")
P.append(note(96, 196, "Castor &amp; Pollux &#8212; dvojčata", pp[0]-14, pp[1]-6, "start"))
P.append(note(150, 812, "K &#8212; Kačka", CXa-98, TOP+SZ+38, "start"))
P.append(note(760, 700, "O &#8212; Ondra", CXa+118, TOP+SZ+92, "end"))
P.append(note(790, 1060, "jeden kořen &#8212; jedna rodina", CXa+14, TOP+SZ+352, "end"))

# ---------- pravá půlka: náhled na paži ----------
AX, AY = 1190, 640          # stred paze
AW, AH = 380, 1080
P.append('<defs>'
         '<linearGradient id="arm" x1="0" y1="0" x2="1" y2="0">'
         '<stop offset="0%"   stop-color="#cfa98e"/>'
         '<stop offset="22%"  stop-color="#eed4bf"/>'
         '<stop offset="48%"  stop-color="#f3e0d0"/>'
         '<stop offset="80%"  stop-color="#e2c0a6"/>'
         '<stop offset="100%" stop-color="#c9a087"/>'
         '</linearGradient>'
         '<linearGradient id="armtop" x1="0" y1="0" x2="0" y2="1">'
         '<stop offset="0%"   stop-color="#b8917a" stop-opacity="0.45"/>'
         '<stop offset="12%"  stop-color="#b8917a" stop-opacity="0"/>'
         '<stop offset="88%"  stop-color="#b8917a" stop-opacity="0"/>'
         '<stop offset="100%" stop-color="#b8917a" stop-opacity="0.45"/>'
         '</linearGradient></defs>')
P.append(f'<rect x="{AX-AW/2}" y="{AY-AH/2}" width="{AW}" height="{AH}" rx="112" fill="url(#arm)"/>')
P.append(f'<rect x="{AX-AW/2}" y="{AY-AH/2}" width="{AW}" height="{AH}" rx="112" fill="url(#armtop)"/>')

INK = "#2a2320"
ink = v2(AX + 6, AY - 400, 300).replace('#111', INK)
P.append(f'<g opacity="0.90" transform="rotate(2 {AX} {AY})">{ink}</g>')
P.append(f'<text x="{AX}" y="{AY+AH/2+46}" text-anchor="middle" font-family="Georgia,serif" '
         f'font-size="17" fill="#8b8b8b" font-style="italic">'
         f'orientační náhled &#183; skutečná výška cca 14&#8211;17 cm, šířka 6&#8211;7 cm</text>')

svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
       f'viewBox="0 0 {W} {H}">' + "\n".join(P) + '</svg>')
open("/home/user/Claude/Projekty/Osobni/Outputs/tetovani-blizenci/detail-paze.svg","w").write(svg)
print("ok")
