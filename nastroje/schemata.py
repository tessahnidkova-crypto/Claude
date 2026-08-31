#!/usr/bin/env python3
"""Generátor vysvětlujících schémat (SVG) pro studijní materiály.

Proč vlastní generátor a ne ručně kreslené SVG: schémat je přes sto a musí
vypadat stejně. Tady se popíše, CO má obrázek říct, a rozvržení dopočítá kód.

Šablony:
    retez(...)     řetěz kroků se šipkami (metabolická dráha, kaskáda)
    vetev(...)     jeden zdroj → několik větví (rozdělení skupiny léků)
    srovnani(...)  dva sloupce proti sobě (A × B, agonista × antagonista)
    cil(...)       ústřední objekt a šipky, které do něj míří (cíle léků v buňce)
    stupnice(...)  patra pod sebou (nefron, generace, stupňovitá léčba)
    smycka(...)    kruh se zpětnou vazbou (osa, regulace)

Barvy sedí s `md2gdoc.py`, aby obrázek nevypadal jako cizí těleso v textu.
"""

W = 900                      # šířka plátna; v PDF se roztáhne na šířku sazby
ACCENT = "#1B6B5F"
CRIT = "#9C3628"
WARN = "#B8752A"
MUTED = "#556964"
LINE = "#C6D5D0"
BG = "#F4F7F5"
BGW = "#FBEEE9"              # podklad pro „pozor" uzly
BGA = "#E7F0ED"              # podklad pro zvýrazněné uzly

FS = 13.5                    # základní velikost písma v uzlu
FSS = 12                     # popisky šipek
CH = 0.545                   # odhad šířky znaku vůči velikosti písma


def _wrap(text: str, sirka: float, fs: float = FS) -> list[str]:
    """Zalomí text na řádky, které se vejdou do dané šířky."""
    max_znaku = max(6, int(sirka / (fs * CH)))
    radky, akt = [], ""
    for slovo in text.split():
        zkouska = (akt + " " + slovo).strip()
        if len(zkouska) <= max_znaku:
            akt = zkouska
        else:
            if akt:
                radky.append(akt)
            akt = slovo
    if akt:
        radky.append(akt)
    return radky


def _esc(s: str) -> str:
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def _text(x, y, radky, fs=FS, barva="#1A2421", anchor="middle", tucne_prvni=False,
          halo=False):
    """halo=True obtáhne text bílou linkou, aby byl čitelný i přes čáru šipky."""
    kusy = []
    obtah = ' stroke="#FFFFFF" stroke-width="3.4" paint-order="stroke"' if halo else ""
    for n, r in enumerate(radky):
        w = "600" if (tucne_prvni and n == 0) else "400"
        kusy.append(f'<text x="{x:.0f}" y="{y + n * (fs * 1.25):.0f}" font-size="{fs}" '
                    f'font-weight="{w}" fill="{barva}" text-anchor="{anchor}"{obtah}>'
                    f'{_esc(r)}</text>')
    return "".join(kusy)


def _box(x, y, w, h, text, kind="normal"):
    """Zaoblený rámeček s vycentrovaným textem. kind: normal | zvyrazni | pozor | tichy"""
    fill, stroke, tb = "#FFFFFF", LINE, "#1A2421"
    if kind == "zvyrazni":
        fill, stroke = BGA, ACCENT
    elif kind == "pozor":
        fill, stroke, tb = BGW, CRIT, "#5B1E16"
    elif kind == "tichy":
        fill, stroke, tb = BG, LINE, MUTED
    radky = _wrap(text, w - 16)
    celkem = len(radky) * FS * 1.25
    ty = y + h / 2 - celkem / 2 + FS * 0.92
    return (f'<rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" rx="7" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="1.6"/>'
            + _text(x + w / 2, ty, radky, barva=tb, tucne_prvni=True))


def _sipka(x1, y1, x2, y2, popis="", barva=ACCENT, nad=True):
    s = (f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" '
         f'stroke="{barva}" stroke-width="2" marker-end="url(#hrot)"/>')
    if popis:
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        radky = _wrap(popis, max(110, abs(x2 - x1) + 70), FSS)
        oy = -9 - (len(radky) - 1) * FSS * 1.2 if nad else 20
        s += _text(mx, my + oy, radky, fs=FSS, barva=barva, halo=True)
    return s


def _plat(vnitrek, h, titulek=""):
    hlava = ""
    if titulek:
        hlava = _text(W / 2, 22, _wrap(titulek, W - 40, 14.5), fs=14.5,
                      barva=ACCENT, tucne_prvni=True)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h:.0f}" '
            f'width="100%" style="max-width:100%;height:auto;display:block;margin:10px 0" '
            f'font-family="Calibri, Carlito, Arial, sans-serif">'
            f'<defs><marker id="hrot" markerWidth="9" markerHeight="9" refX="8" refY="3" '
            f'orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="{ACCENT}"/></marker></defs>'
            f'<rect x="0" y="0" width="{W}" height="{h:.0f}" rx="8" fill="#FFFFFF" '
            f'stroke="{LINE}" stroke-width="1.4"/>{hlava}{vnitrek}</svg>')


# ---------------------------------------------------------------- šablony

def retez(kroky, sipky=None, titulek="", pozn="", vyska=86):
    """Řetěz kroků vedle sebe. kroky = [(text, kind), ...]; sipky = popisky mezi nimi."""
    n = len(kroky)
    sipky = sipky or [""] * (n - 1)
    mezera = 74
    w = (W - 60 - mezera * (n - 1)) / n
    y = 58 if titulek else 30
    vnitrek = ""
    for idx, (text, kind) in enumerate(kroky):
        x = 30 + idx * (w + mezera)
        vnitrek += _box(x, y, w, vyska, text, kind)
        if idx < n - 1:
            vnitrek += _sipka(x + w + 8, y + vyska / 2, x + w + mezera - 8,
                              y + vyska / 2, sipky[idx])
    h = y + vyska + 18
    if pozn:
        radky = _wrap(pozn, W - 60, FSS)
        vnitrek += _text(W / 2, h + 4, radky, fs=FSS, barva=CRIT)
        h += len(radky) * FSS * 1.25 + 10
    return _plat(vnitrek, h, titulek)


def vetev(zdroj, vetve, titulek="", pozn="", zdroj_kind="zvyrazni"):
    """Jeden zdroj vlevo → několik větví vpravo. vetve = [(popis_sipky, text, kind), ...]"""
    n = len(vetve)
    y0 = 56 if titulek else 26
    vh, mez = 74, 16
    celkem = n * vh + (n - 1) * mez
    zw, vw = 250, W - 250 - 200 - 60
    vnitrek = _box(30, y0 + celkem / 2 - 46, zw, 92, zdroj, zdroj_kind)
    sx, sy = 30 + zw, y0 + celkem / 2
    for idx, (popis, text, kind) in enumerate(vetve):
        by = y0 + idx * (vh + mez)
        bx = 30 + zw + 190
        vnitrek += _sipka(sx + 6, sy, bx - 8, by + vh / 2, popis)
        vnitrek += _box(bx, by, vw + 200 - 190, vh, text, kind)
    h = y0 + celkem + 18
    if pozn:
        radky = _wrap(pozn, W - 60, FSS)
        vnitrek += _text(W / 2, h + 4, radky, fs=FSS, barva=CRIT)
        h += len(radky) * FSS * 1.25 + 10
    return _plat(vnitrek, h, titulek)


def srovnani(a_nadpis, a_body, b_nadpis, b_body, titulek="", pozn="",
             a_kind="zvyrazni", b_kind="pozor"):
    """Dva panely proti sobě — klasické „tohle × tamto"."""
    y0 = 56 if titulek else 26
    pw = (W - 60 - 26) / 2
    radky_a, radky_b = [], []
    for b in a_body:
        radky_a += _wrap("• " + b, pw - 28, FSS)
    for b in b_body:
        radky_b += _wrap("• " + b, pw - 28, FSS)
    ph = 46 + max(len(radky_a), len(radky_b)) * FSS * 1.35 + 14
    vnitrek = ""
    for x, nadpis, radky, kind in ((30, a_nadpis, radky_a, a_kind),
                                   (30 + pw + 26, b_nadpis, radky_b, b_kind)):
        fill = BGA if kind == "zvyrazni" else (BGW if kind == "pozor" else BG)
        stroke = ACCENT if kind == "zvyrazni" else (CRIT if kind == "pozor" else LINE)
        vnitrek += (f'<rect x="{x:.0f}" y="{y0}" width="{pw:.0f}" height="{ph:.0f}" rx="7" '
                    f'fill="{fill}" stroke="{stroke}" stroke-width="1.6"/>')
        vnitrek += _text(x + pw / 2, y0 + 26, _wrap(nadpis, pw - 20, 13.5),
                         fs=13.5, barva=stroke, tucne_prvni=True)
        vnitrek += _text(x + 16, y0 + 52, radky, fs=FSS, anchor="start")
    h = y0 + ph + 18
    if pozn:
        r = _wrap(pozn, W - 60, FSS)
        vnitrek += _text(W / 2, h + 4, r, fs=FSS, barva=CRIT)
        h += len(r) * FSS * 1.25 + 10
    return _plat(vnitrek, h, titulek)


def cil(stred, sipky, titulek="", pozn=""):
    """Ústřední objekt a popisky, které do něj míří. sipky = [(text, kind), ...] max 6."""
    y0 = 56 if titulek else 26
    n = len(sipky)
    lev = (n + 1) // 2
    prav = n - lev
    rh, mez = 62, 14
    hl = lev * rh + (lev - 1) * mez
    hp = prav * rh + (prav - 1) * mez if prav else 0
    telo = max(hl, hp, 120)
    cy = y0 + telo / 2
    bw = 226
    cx = W / 2
    vnitrek = (f'<rect x="{cx - 122:.0f}" y="{cy - 62:.0f}" width="244" height="124" rx="14" '
               f'fill="{BGA}" stroke="{ACCENT}" stroke-width="2"/>')
    radky = _wrap(stred, 214)
    vnitrek += _text(cx, cy - len(radky) * FS * 0.62 + FS * 0.9, radky,
                     barva=ACCENT, tucne_prvni=True)
    for idx, (text, kind) in enumerate(sipky):
        vlevo = idx < lev
        k = idx if vlevo else idx - lev
        pocet = lev if vlevo else prav
        blok = pocet * rh + (pocet - 1) * mez
        by = y0 + telo / 2 - blok / 2 + k * (rh + mez)
        bx = 26 if vlevo else W - 26 - bw
        vnitrek += _box(bx, by, bw, rh, text, kind)
        if vlevo:
            vnitrek += _sipka(bx + bw + 6, by + rh / 2, cx - 128, cy + (by + rh / 2 - cy) * 0.35)
        else:
            vnitrek += _sipka(bx - 6, by + rh / 2, cx + 128, cy + (by + rh / 2 - cy) * 0.35)
    h = y0 + telo + 18
    if pozn:
        r = _wrap(pozn, W - 60, FSS)
        vnitrek += _text(W / 2, h + 4, r, fs=FSS, barva=CRIT)
        h += len(r) * FSS * 1.25 + 10
    return _plat(vnitrek, h, titulek)


def stupnice(patra, titulek="", pozn="", sipka_popis=""):
    """Patra pod sebou se svislou šipkou vlevo. patra = [(nazev, popis, kind), ...]"""
    y0 = 56 if titulek else 26
    ph, mez = 66, 12
    lx, bw = 96, W - 96 - 56
    vnitrek = ""
    for idx, (nazev, popis, kind) in enumerate(patra):
        y = y0 + idx * (ph + mez)
        fill = BGA if kind == "zvyrazni" else (BGW if kind == "pozor" else "#FFFFFF")
        stroke = ACCENT if kind == "zvyrazni" else (CRIT if kind == "pozor" else LINE)
        nadpis_barva = MUTED if kind == "tichy" else (stroke if stroke != LINE else "#1A2421")
        vnitrek += (f'<rect x="{lx}" y="{y}" width="{bw}" height="{ph}" rx="7" '
                    f'fill="{fill}" stroke="{stroke}" stroke-width="1.6"/>')
        vnitrek += _text(lx + 14, y + 24, _wrap(nazev, bw - 28, 13.5), fs=13.5,
                         barva=nadpis_barva, anchor="start", tucne_prvni=True)
        vnitrek += _text(lx + 14, y + 45, _wrap(popis, bw - 28, FSS)[:2], fs=FSS,
                         anchor="start")
    celkem = len(patra) * (ph + mez) - mez
    vnitrek += _sipka(58, y0 + 6, 58, y0 + celkem - 4)
    if sipka_popis:
        vnitrek += (f'<text x="30" y="{y0 + celkem / 2:.0f}" font-size="{FSS}" fill="{MUTED}" '
                    f'transform="rotate(-90 30 {y0 + celkem / 2:.0f})" text-anchor="middle">'
                    f'{_esc(sipka_popis)}</text>')
    h = y0 + celkem + 18
    if pozn:
        r = _wrap(pozn, W - 60, FSS)
        vnitrek += _text(W / 2, h + 4, r, fs=FSS, barva=CRIT)
        h += len(r) * FSS * 1.25 + 10
    return _plat(vnitrek, h, titulek)


def smycka(uzly, titulek="", pozn="", brzda=""):
    """Kruhová regulace: uzly = [text, ...] (3–4), poslední se vrací k prvnímu."""
    y0 = 60 if titulek else 30
    n = len(uzly)
    bw, bh = 230, 74
    vys = 250
    cx, cy = W / 2, y0 + vys / 2
    rx, ry = 300, 88
    body = []
    import math
    for idx in range(n):
        uh = -math.pi / 2 + idx * 2 * math.pi / n
        body.append((cx + rx * math.cos(uh) - bw / 2, cy + ry * math.sin(uh) - bh / 2))
    vnitrek = ""
    for idx, (bx, by) in enumerate(body):
        vnitrek += _box(bx, by, bw, bh, uzly[idx], "zvyrazni" if idx == 0 else "normal")
    for idx in range(n):
        x1, y1 = body[idx][0] + bw / 2, body[idx][1] + bh / 2
        x2, y2 = body[(idx + 1) % n][0] + bw / 2, body[(idx + 1) % n][1] + bh / 2
        dx, dy = x2 - x1, y2 - y1
        d = max(1.0, (dx ** 2 + dy ** 2) ** 0.5)
        ox, oy = dx / d, dy / d
        posl = idx == n - 1
        vnitrek += _sipka(x1 + ox * 128, y1 + oy * 52, x2 - ox * 128, y2 - oy * 52,
                          brzda if posl and brzda else "",
                          barva=CRIT if posl and brzda else ACCENT)
    h = y0 + vys + 12
    if pozn:
        r = _wrap(pozn, W - 60, FSS)
        vnitrek += _text(W / 2, h + 4, r, fs=FSS, barva=CRIT)
        h += len(r) * FSS * 1.25 + 10
    return _plat(vnitrek, h, titulek)
