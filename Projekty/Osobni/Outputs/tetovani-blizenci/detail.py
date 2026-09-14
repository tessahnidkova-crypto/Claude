#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Detail doporucene varianty D + vysvetlivky + nahled na kuzi."""
import sys, math
sys.path.insert(0, "/home/user/Claude/Projekty/Osobni/Outputs/tetovani-blizenci")
from generator import *

W, H = 1640, 1180
P = [f'<rect width="{W}" height="{H}" fill="#fbfaf8"/>']
P.append(f'<text x="{W/2}" y="56" text-anchor="middle" font-family="Georgia,serif" '
         f'font-size="31" fill="#111" letter-spacing="3">VARIANTA D &#8212; co kde je</text>')

# ===== levá půlka: velký návrh s anotacemi =====
CXa, CYa, SZ = 480, 640, 720
m = make_mapper(CXa, CYa, SZ)
LW = 1.25
P.append(constellation(m, w=LW, star_scale=1.25, highlight=("Mebsuta", "Wasat")))
P.append(morse_on_arc(m("Castor"), m("Pollux"), bulge=0.16, letters=("K",), w=LW+0.25, up=True,  fit=0.86)[0])
P.append(morse_on_arc(m("Alhena"), m("Propus"), bulge=0.10, letters=("O",), w=LW+0.25, up=False, fit=0.78)[0])
bx, by = CXa+6, CYa+318
tip = (CXa-36, CYa+128)
def stem(a, b, bow=18, w=1.0):
    mx, my = (a[0]+b[0])/2, (a[1]+b[1])/2
    return (f'<path d="M {a[0]:.1f} {a[1]:.1f} Q {mx+bow:.1f} {my:.1f} {b[0]:.1f} {b[1]:.1f}" '
            f'fill="none" stroke="#111" stroke-width="{w}" stroke-linecap="round"/>')
P.append(stem((bx, by), tip, bow=22, w=1.15))
P.append(petal_flower(tip[0], tip[1]-11, 19, rot=-90, petals=5, w=1.05, center_r=1.9))
P.append(leaf(bx-5, by-80, 36, 204, w=1.0))

# --- anotace ---
def note(x, y, txt, ax, ay, anchor="start"):
    """popisek + tenka vodici linka k mistu (ax,ay)"""
    return (f'<line x1="{x + (-8 if anchor=="end" else 8)}" y1="{y-5}" x2="{ax}" y2="{ay}" '
            f'stroke="#c0b9ab" stroke-width="0.9" stroke-dasharray="2 3"/>'
            f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Georgia,serif" '
            f'font-size="17" fill="#6f6a61">{txt}</text>')

cp = m("Castor"); pp = m("Pollux")
P.append(note(200, 232, "K &#8212; Kačka", (cp[0]+pp[0])/2 - 26, min(cp[1],pp[1]) - 44, "start"))
ap = m("Alhena"); hp = m("Propus")
P.append(note(200, 1062, "O &#8212; Ondra", (ap[0]+hp[0])/2 - 40, max(ap[1],hp[1]) + 30, "start"))
P.append(note(830, 352, "Castor &amp; Pollux &#8212; dvojčata", pp[0]+18, pp[1]-6, "end"))
P.append(note(830, 585, "dvě zářící hvězdy = děti", m("Wasat")[0]+14, m("Wasat")[1], "end"))
P.append(note(830, 880, "větvička &#8212; volitelná", tip[0]+22, tip[1], "end"))

# ===== pravá půlka: náhled na kůži =====
SKX, SKY = 1230, 620
P.append('<defs>'
         '<radialGradient id="skin" cx="42%" cy="30%" r="78%">'
         '<stop offset="0%" stop-color="#f2ddcd"/>'
         '<stop offset="55%" stop-color="#e8cdb8"/>'
         '<stop offset="100%" stop-color="#d9b99f"/>'
         '</radialGradient>'
         '<radialGradient id="shade" cx="50%" cy="50%" r="50%">'
         '<stop offset="60%" stop-color="#000" stop-opacity="0"/>'
         '<stop offset="100%" stop-color="#8a6a52" stop-opacity="0.30"/>'
         '</radialGradient></defs>')
P.append(f'<rect x="{SKX-330}" y="{SKY-420}" width="660" height="900" rx="70" fill="url(#skin)"/>')
P.append(f'<rect x="{SKX-330}" y="{SKY-420}" width="660" height="900" rx="70" fill="url(#shade)"/>')
# velmi jemny naznak lopatky (jen stin, zadne "svaly")
P.append(f'<ellipse cx="{SKX-60}" cy="{SKY-70}" rx="200" ry="250" fill="#c9a289" '
         f'fill-opacity="0.10" transform="rotate(-14 {SKX-60} {SKY-70})"/>')

INK = "#2a2320"
m2 = make_mapper(SKX + 28, SKY + 28, 430)
def ink_constellation(mm, w=0.95):
    out = []
    for a, b in LINES:
        p1, p2 = mm(a), mm(b)
        out.append(f'<line x1="{p1[0]:.2f}" y1="{p1[1]:.2f}" x2="{p2[0]:.2f}" y2="{p2[1]:.2f}" '
                   f'stroke="{INK}" stroke-width="{w}" stroke-linecap="round" '
                   f'stroke-dasharray="1.5 4.2" stroke-opacity="0.88"/>')
    for name, (ra, dec, mag) in STARS.items():
        x, y = mm(name); r = mag_radius(mag, 1.0)
        if name in ("Mebsuta", "Wasat"):
            out.append(sparkle(x, y, r*2.4).replace('fill="#111"', f'fill="{INK}" fill-opacity="0.9"'))
        else:
            out.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r*0.52:.2f}" fill="{INK}" fill-opacity="0.9"/>')
    return "\n".join(out)
g = [ink_constellation(m2)]
g.append(morse_on_arc(m2("Castor"), m2("Pollux"), bulge=0.16, letters=("K",), w=1.05, up=True,  fit=0.86)[0]
         .replace('#111', INK))
g.append(morse_on_arc(m2("Alhena"), m2("Propus"), bulge=0.10, letters=("O",), w=1.05, up=False, fit=0.78)[0]
         .replace('#111', INK))
bx2, by2 = SKX+32, SKY+218
tip2 = (SKX+8, SKY+108)
g.append(stem((bx2, by2), tip2, bow=14, w=0.95).replace('#111', INK))
g.append(petal_flower(tip2[0], tip2[1]-8, 13, rot=-90, petals=5, w=0.9).replace('#111', INK))
g.append(leaf(bx2-4, by2-52, 24, 204, w=0.85).replace('#111', INK))
P.append(f'<g opacity="0.92" transform="rotate(-7 {SKX} {SKY})">' + "\n".join(g) + '</g>')
P.append(f'<text x="{SKX}" y="{SKY+512}" text-anchor="middle" font-family="Georgia,serif" '
         f'font-size="17" fill="#8b8b8b" font-style="italic">orientační náhled na lopatce &#183; '
         f'skutečná velikost cca 9&#8211;12 cm na výšku</text>')

svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
       f'viewBox="0 0 {W} {H}">' + "\n".join(P) + '</svg>')
open("/home/user/Claude/Projekty/Osobni/Outputs/tetovani-blizenci/detail-D.svg","w").write(svg)
print("ok")
