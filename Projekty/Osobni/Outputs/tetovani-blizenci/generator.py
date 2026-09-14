#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator navrhu tetovani: souhvezdi Blizencu (Gemini) se zakomponovanymi
iniciálami K (Kacka) a O (Ondra) v morseovce.

Pozice hvezd: RA/Dec (J2000), priblizne. Pro tattoo-uzitek je to vizualne verne;
pro astronomicky presnou repliku overit ve Stellariu.
"""
import math

# --- hvezdy Gemini: jmeno -> (RA v hodinach, Dec ve stupnich, magnituda) ---
STARS = {
    "Castor":  (7.576, 31.888, 1.58),   # alfa Gem
    "Pollux":  (7.755, 28.026, 1.16),   # beta Gem - nejjasnejsi
    "Alhena":  (6.629, 16.399, 1.90),   # gama Gem
    "Wasat":   (7.335, 21.982, 3.53),   # delta Gem
    "Mebsuta": (6.732, 25.131, 2.98),   # epsilon Gem
    "Mekbuda": (7.068, 20.570, 3.79),   # zeta Gem
    "Tejat":   (6.383, 22.514, 2.87),   # mu Gem
    "Propus":  (6.248, 22.507, 3.28),   # eta Gem
    "Kappa":   (7.741, 24.398, 3.57),
    "Lambda":  (7.302, 16.540, 3.58),
    "Theta":   (6.880, 33.961, 3.60),
    "Tau":     (7.186, 30.245, 4.41),
    "Iota":    (7.429, 27.798, 3.78),
    "Upsilon": (7.598, 26.896, 4.06),
    "Nu":      (6.483, 20.212, 4.15),
    "Xi":      (6.755, 12.896, 3.35),
}

# --- spojnice (stylizovana figura dvou postav) ---
LINES = [
    # leva postava (Castor)
    ("Castor", "Tau"), ("Tau", "Theta"),
    ("Tau", "Mebsuta"), ("Mebsuta", "Tejat"), ("Tejat", "Propus"),
    ("Mebsuta", "Nu"),
    # prava postava (Pollux)
    ("Pollux", "Upsilon"), ("Pollux", "Kappa"),
    ("Upsilon", "Wasat"), ("Wasat", "Mekbuda"), ("Mekbuda", "Alhena"),
    ("Wasat", "Lambda"), ("Lambda", "Xi"),
]
# spojnice hlav se kresli zvlast (nese morseovku)
BOND = ("Castor", "Pollux")

DEC0 = 24.0  # stred pro projekci

def project(ra_h, dec_deg):
    """RA/Dec -> rovinne souradnice (stupne). RA roste doleva (pohled z Zeme)."""
    x = -(ra_h * 15.0) * math.cos(math.radians(DEC0))
    y = -dec_deg
    return x, y

# spocitej bounding box a transformaci do plátna
_pts = [project(*STARS[n][:2]) for n in STARS]
_xs = [p[0] for p in _pts]; _ys = [p[1] for p in _pts]
X0, X1 = min(_xs), max(_xs)
Y0, Y1 = min(_ys), max(_ys)

# uhel, o ktery je treba otocit, aby postavy "stály" (osa Pollux -> Alhena svisle dolu)
def _upright_angle():
    ax, ay = project(*STARS["Pollux"][:2])
    bx, by = project(*STARS["Alhena"][:2])
    cur = math.degrees(math.atan2(by - ay, bx - ax))
    return 90.0 - cur          # rotace ve stupnich

ROT = _upright_angle()

def make_mapper(cx, cy, size, rot=None, flip=False):
    """
    Mapuje hvezdu do ramu o velikosti `size` se stredem cx,cy.
    rot=None -> natoci souhvezdi na vysku (tattoo stylizace)
    rot=0    -> ponecha skutecnou orientaci na obloze
    flip     -> zrcadlove (pro parove tetovani)
    """
    r = ROT if rot is None else rot
    a = math.radians(r)
    ca, sa = math.cos(a), math.sin(a)
    pts = []
    for n in STARS:
        x, y = project(*STARS[n][:2])
        if flip: x = -x
        pts.append((x*ca - y*sa, x*sa + y*ca))
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    x0, x1 = min(xs), max(xs); y0, y1 = min(ys), max(ys)
    s = size / max(x1-x0, y1-y0)
    mx = (x0+x1)/2.0; my = (y0+y1)/2.0
    def f(name):
        x, y = project(*STARS[name][:2])
        if flip: x = -x
        rx, ry = x*ca - y*sa, x*sa + y*ca
        return (cx + (rx - mx) * s, cy + (ry - my) * s)
    return f

def mag_radius(mag, base=1.0):
    """jasnejsi hvezda = vetsi bod"""
    r = (5.0 - mag) ** 1.35 * 0.62 + 1.25
    return max(1.35, r) * base

# ---------- kreslici primitiva ----------

def sparkle(x, y, r, w=0.9):
    """ctyrcipa hvezda (fine-line sparkle)"""
    a = r; b = r * 0.115
    d = (f"M {x:.2f} {y-a:.2f} Q {x+b:.2f} {y-b:.2f} {x+a:.2f} {y:.2f} "
         f"Q {x+b:.2f} {y+b:.2f} {x:.2f} {y+a:.2f} "
         f"Q {x-b:.2f} {y+b:.2f} {x-a:.2f} {y:.2f} "
         f"Q {x-b:.2f} {y-b:.2f} {x:.2f} {y-a:.2f} Z")
    return f'<path d="{d}" fill="#111" stroke="none"/>'

def dot(x, y, r, fill="#111"):
    return f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r:.2f}" fill="{fill}"/>'

def ring(x, y, r, w=0.9):
    return (f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r:.2f}" fill="#fff" '
            f'stroke="#111" stroke-width="{w}"/>')

def dotted(p1, p2, w=0.9, dash="1.6 4.4"):
    return (f'<line x1="{p1[0]:.2f}" y1="{p1[1]:.2f}" x2="{p2[0]:.2f}" y2="{p2[1]:.2f}" '
            f'stroke="#111" stroke-width="{w}" stroke-linecap="round" '
            f'stroke-dasharray="{dash}"/>')

def solid(p1, p2, w=0.9):
    return (f'<line x1="{p1[0]:.2f}" y1="{p1[1]:.2f}" x2="{p2[0]:.2f}" y2="{p2[1]:.2f}" '
            f'stroke="#111" stroke-width="{w}" stroke-linecap="round"/>')

# ---------- morseovka ----------
MORSE = {"K": "-.-", "O": "---"}

def quad_point(p0, p1, p2, t):
    x = (1-t)**2*p0[0] + 2*(1-t)*t*p1[0] + t*t*p2[0]
    y = (1-t)**2*p0[1] + 2*(1-t)*t*p1[1] + t*t*p2[1]
    return x, y

def quad_len(p0, p1, p2, n=400):
    L = 0.0; prev = quad_point(p0,p1,p2,0)
    tbl = [(0.0, 0.0)]
    for i in range(1, n+1):
        t = i/n; cur = quad_point(p0,p1,p2,t)
        L += math.hypot(cur[0]-prev[0], cur[1]-prev[1])
        tbl.append((L, t)); prev = cur
    return L, tbl

def t_at(tbl, s):
    """parametr t v dane delce s podel krivky"""
    lo, hi = 0, len(tbl)-1
    while lo < hi:
        mid = (lo+hi)//2
        if tbl[mid][0] < s: lo = mid+1
        else: hi = mid
    return tbl[lo][1]

def morse_on_arc(p0, p2, bulge=0.22, letters=("K", "O"), scale=1.0, w=0.95, up=True, fit=None):
    """
    Vykresli oblouk mezi dvema body, na nemz jsou tecky a carky morseovky.
    Vraci (svg, control_point).
    """
    mx, my = (p0[0]+p2[0])/2, (p0[1]+p2[1])/2
    dx, dy = p2[0]-p0[0], p2[1]-p0[1]
    L0 = math.hypot(dx, dy)
    # normala (nahoru nad spojnici)
    nx, ny = -dy/L0, dx/L0
    if (ny > 0) == up: nx, ny = -nx, -ny   # up=True -> vyboceni nahoru
    p1 = (mx + nx*L0*bulge*2, my + ny*L0*bulge*2)
    L, tbl = quad_len(p0, p1, p2)

    DASH = 13.0*scale; DOT = 1.55*scale
    GAP  = 7.0*scale                 # mezera mezi symboly v pismenu
    LGAP = 16.0*scale                # mezera mezi pismeny

    # celkova delka morse sekvence
    total = 0.0
    seq = []
    for li, ch in enumerate(letters):
        code = MORSE[ch]
        for si, sym in enumerate(code):
            seq.append(sym)
            total += DASH if sym == "-" else DOT*2
            if si < len(code)-1: total += GAP
        if li < len(letters)-1: total += LGAP

    if fit is not None and total > 0:
        # prepocitej meritko tak, aby morseovka vyplnila `fit` podil dráhy oblouku
        k = (L * fit) / total
        DASH *= k; DOT *= k; GAP *= k; LGAP *= k
        total *= k
    s = (L - total)/2.0
    out = []
    for li, ch in enumerate(letters):
        code = MORSE[ch]
        for si, sym in enumerate(code):
            if sym == "-":
                t_a = t_at(tbl, s); t_b = t_at(tbl, s+DASH)
                a = quad_point(p0,p1,p2,t_a); b = quad_point(p0,p1,p2,t_b)
                out.append(f'<path d="M {a[0]:.2f} {a[1]:.2f} Q '
                           f'{quad_point(p0,p1,p2,(t_a+t_b)/2)[0]:.2f} '
                           f'{quad_point(p0,p1,p2,(t_a+t_b)/2)[1]:.2f} '
                           f'{b[0]:.2f} {b[1]:.2f}" fill="none" stroke="#111" '
                           f'stroke-width="{w}" stroke-linecap="round"/>')
                s += DASH
            else:
                t_a = t_at(tbl, s+DOT)
                c = quad_point(p0,p1,p2,t_a)
                out.append(dot(c[0], c[1], max(1.3, w*1.55)))
                s += DOT*2
            if si < len(code)-1: s += GAP
        if li < len(letters)-1: s += LGAP
    return "\n".join(out), p1

# ---------- kvetina ----------

def petal_flower(cx, cy, r, rot=0.0, petals=5, w=0.85, center_r=1.5, fill="none"):
    """jemna peticetna kvetina (fine-line)"""
    out = []
    for i in range(petals):
        a = math.radians(rot + i*360.0/petals)
        px, py = cx + math.cos(a)*r*0.62, cy + math.sin(a)*r*0.62
        # okvetni listek jako elipsa natocena ven
        out.append(f'<ellipse cx="{px:.2f}" cy="{py:.2f}" rx="{r*0.44:.2f}" '
                   f'ry="{r*0.30:.2f}" fill="{fill}" stroke="#111" stroke-width="{w}" '
                   f'transform="rotate({math.degrees(a):.1f} {px:.2f} {py:.2f})"/>')
    out.append(dot(cx, cy, center_r))
    return "\n".join(out)

def bud(cx, cy, r, angle=-90, w=0.85):
    """poupe: kapkovite telo se spickou + dva kalisni listky u zakladny"""
    a = math.radians(angle)
    ux, uy = math.cos(a), math.sin(a)          # smer ke spicce
    px, py = -uy, ux                           # kolmice
    L = r * 2.3
    def pt(along, side):
        return (cx + ux*along + px*side, cy + uy*along + py*side)
    tip  = pt(L, 0)
    wmax = r * 0.86
    c1 = pt(L*0.12, wmax*0.95); c2 = pt(L*0.62, wmax*0.80)
    c3 = pt(L*0.62, -wmax*0.80); c4 = pt(L*0.12, -wmax*0.95)
    body = (f'<path d="M {cx:.2f} {cy:.2f} C {c1[0]:.2f} {c1[1]:.2f} {c2[0]:.2f} {c2[1]:.2f} '
            f'{tip[0]:.2f} {tip[1]:.2f} C {c3[0]:.2f} {c3[1]:.2f} {c4[0]:.2f} {c4[1]:.2f} '
            f'{cx:.2f} {cy:.2f} Z" fill="none" stroke="#111" stroke-width="{w}" '
            f'stroke-linejoin="round"/>')
    # naznak druheho listku uvnitr
    inner = (f'<path d="M {cx:.2f} {cy:.2f} C {pt(L*0.2, wmax*0.35)[0]:.2f} {pt(L*0.2, wmax*0.35)[1]:.2f} '
             f'{pt(L*0.6, wmax*0.28)[0]:.2f} {pt(L*0.6, wmax*0.28)[1]:.2f} '
             f'{tip[0]:.2f} {tip[1]:.2f}" fill="none" stroke="#111" stroke-width="{w*0.8}" '
             f'stroke-linecap="round"/>')
    # kalisni listky
    sep = []
    for sgn in (1, -1):
        s_end = pt(-L*0.06, sgn*wmax*1.25)
        ctrl  = pt(L*0.18, sgn*wmax*1.20)
        sep.append(f'<path d="M {cx:.2f} {cy:.2f} Q {ctrl[0]:.2f} {ctrl[1]:.2f} '
                   f'{s_end[0]:.2f} {s_end[1]:.2f}" fill="none" stroke="#111" '
                   f'stroke-width="{w*0.85}" stroke-linecap="round"/>')
    return "\n".join([body, inner] + sep)

def leaf(x, y, length, angle, w=0.8, curve=0.35):
    a = math.radians(angle)
    ex, ey = x + math.cos(a)*length, y + math.sin(a)*length
    nx, ny = -math.sin(a)*length*curve, math.cos(a)*length*curve
    mx, my = (x+ex)/2, (y+ey)/2
    return (f'<path d="M {x:.2f} {y:.2f} Q {mx+nx:.2f} {my+ny:.2f} {ex:.2f} {ey:.2f} '
            f'Q {mx-nx:.2f} {my-ny:.2f} {x:.2f} {y:.2f} Z" fill="none" '
            f'stroke="#111" stroke-width="{w}"/>')

# ---------- souhvezdi ----------

def constellation(m, w=0.9, dash="1.6 4.4", star_scale=1.0,
                  skip_bond=True, highlight=(), rings=()):
    out = []
    for a, b in LINES:
        out.append(dotted(m(a), m(b), w, dash))
    for name, (ra, dec, mag) in STARS.items():
        x, y = m(name)
        r = mag_radius(mag, star_scale)
        if name in highlight:
            out.append(sparkle(x, y, r*2.6, w))
        elif name in rings:
            out.append(ring(x, y, r*0.95, w))
        else:
            out.append(dot(x, y, r*0.52))
    return "\n".join(out)
