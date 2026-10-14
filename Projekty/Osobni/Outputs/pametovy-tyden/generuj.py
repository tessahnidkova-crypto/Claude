#!/usr/bin/env python3
"""Generátor „Týden pro paměť" pro babičku a dědu.

Zdroj obsahu = tenhle soubor. Úprava: změň texty v DNY, spusť
  python3 generuj.py && node render.js
→ vznikne tyden-1.html a tyden-1.pdf.
"""
import html
from pathlib import Path

OUT = Path(__file__).parent

# ---------------------------------------------------------------- obsah
from obsah_tyden1 import DNY, RESENI  # obsah týdne; další týden = nový soubor obsah_tydenN.py

# ---------------------------------------------------------------- HTML
e = html.escape


def lines(n, cls="line"):
    return "".join(f'<div class="{cls}"></div>' for _ in range(n))


def tajenka(h):
    maxlen = max(len(w) for _, w in h["radky"])
    rows = []
    for clue, word in h["radky"]:
        cells = "".join(
            f'<td class="box{" key" if i == 0 else ""}"></td>' for i in range(len(word)))
        pad = "".join('<td class="nobox"></td>' for _ in range(maxlen - len(word)))
        rows.append(f'<tr><td class="clue">{e(clue)} <span class="cnt">({len(word)})</span></td>{cells}{pad}</tr>')
    return f'<table class="taj">{"".join(rows)}</table>'


def hadanka(h):
    t = h["typ"]
    out = [f'<h3>✎ {e(h["nazev"])}</h3>']
    if h.get("navod"):
        out.append(f'<p class="navod">{e(h["navod"])}</p>')
    if t == "tajenka":
        out.append(tajenka(h))
        out.append('<p class="taj-out">Tajenka: <span class="fill"></span></p>')
    elif t == "nepatri":
        out.append('<ol class="rada">' + "".join(f"<li>{e(r)}</li>" for r in h["radky"]) + "</ol>")
        out.append(f'<p class="navod">{e(h["presmycky_navod"])}</p>')
        out.append('<div class="presm">' + "".join(
            f'<div><b>{e(p)}</b> → <span class="fill short"></span></div>' for p in h["presmycky"]) + "</div>")
    elif t == "spojovacka":
        rows = "".join(
            f'<tr><td class="l">{e(a)} <span class="dot">●</span></td><td class="gap"></td>'
            f'<td class="r"><span class="dot">●</span> {e(b)}</td></tr>'
            for a, b in zip(h["leve"], h["prave"]))
        out.append(f'<table class="spoj">{rows}</table>')
    elif t == "poradi":
        out.append('<div class="poradi">' + "".join(
            f'<div><span class="numbox"></span> {e(r)}</div>' for r in h["radky"]) + "</div>")
    elif t == "seznam":
        out.append('<div class="seznam">' + " · ".join(e(p) for p in h["polozky"]) + "</div>")
        out.append('<p class="navod">Co si pamatujete (bez koukání!):</p>' + lines(3))
    elif t == "az":
        out.append('<table class="az">' + "".join(
            f'<tr><td class="hexc"><span class="hex">{e(p)}</span></td><td>{e(c)}</td><td class="azfill"><span class="fill short"></span></td></tr>'
            for p, c in h["radky"]) + "</table>")
    elif t == "pocty":
        out.append('<ol class="pocty">' + "".join(
            f'<li>{e(r)}<div class="ans">Výsledek: <span class="fill short"></span></div></li>' for r in h["radky"]) + "</ol>")
    return "".join(out)


def kviz(d):
    out = ['<h3>? Kvíz</h3>']
    if d.get("kviz_uvod"):
        out.append(f'<p class="navod">{e(d["kviz_uvod"])}</p>')
    if d.get("kviz"):
        items = []
        for q, opts in d["kviz"]:
            o = "".join(f'<span class="opt"><span class="circ">{c}</span> {e(x)}</span>'
                        for c, x in zip("abc", opts))
            items.append(f'<li><div class="q">{e(q)}</div><div class="opts">{o}</div></li>')
        out.append('<ol class="kviz">' + "".join(items) + "</ol>")
    if d.get("doplnovacka"):
        if d.get("doplnovacka_uvod"):
            out.append(f'<p class="navod" style="margin-top:2mm"><b>{e(d["doplnovacka_uvod"])}</b></p>')
        cls = "dopl two" if d.get("doplnovacka_uvod") else "dopl"
        out.append(f'<ol class="{cls}">' + "".join(f"<li>{e(x)}</li>" for x in d["doplnovacka"]) + "</ol>")
    return "".join(out)


def den_html(i, d):
    vz = "".join(f'<li><div class="q">{e(q)}</div>{lines(2)}</li>' for q in d["vzpominky"])
    vzkaz = ""
    if d.get("vzkaz"):
        vzkaz = f'<div class="vzkaz"><div class="q"><b>{e(d["vzkaz"])}</b></div>{lines(4)}</div>'
    clanek = "".join(f"<p>{e(p)}</p>" for p in d["clanek"]["odstavce"])
    otazky = "".join(f'<li><div class="q">{e(q)}</div>{lines(1)}</li>' for q in d["otazky"])
    return f'''
<section class="page">
  <header class="dayhead"><span class="num">Den {i}</span><span class="dname">{e(d["den"])}</span>
    <span class="tema">{d["ikona"]} {e(d["tema"])}</span></header>
  <div class="ranni"><b>Ranní rozcvička:</b> {e(d["ranni"])}{lines(1)}</div>
  <h3>❦ Povídání a vzpomínky</h3>
  <p class="navod">Povídejte si spolu a pár slov zapište.</p>
  <ol class="vzp">{vz}</ol>
  {vzkaz}
  {kviz(d)}
</section>
<section class="page">
  <div class="hadanka">{hadanka(d["hadanka"])}</div>
  <article class="clanek"><h3>☕ Čtení ke kávě: {e(d["clanek"]["nadpis"])}</h3>{clanek}</article>
  <div class="potclanku"><b>Zakryjte článek a zkuste si vzpomenout:</b><ol>{otazky}</ol></div>
  <div class="denik"><h3>☾ Večer: co jsme dnes dělali</h3>
    <div class="dr"><span>Dopoledne:</span><div class="line"></div></div>
    <div class="dr"><span>Odpoledne:</span><div class="line"></div></div>
    <div class="dr"><span>Dnes nás potěšilo:</span><div class="line"></div></div>
  </div>
</section>'''


CSS = """
@page { size: A4; margin: 14mm 15mm 14mm 15mm; }
* { box-sizing: border-box; }
body { font-family: 'DejaVu Serif', serif; font-size: 13.5pt; line-height: 1.38; color: #1c1c1c; margin: 0; }
h1, h2, h3, .dayhead { font-family: 'DejaVu Sans', sans-serif; }
.page { page-break-after: always; break-after: page; }
.page:last-child { page-break-after: auto; }
h3 { font-size: 15pt; color: #2d5a35; margin: 3.5mm 0 1.5mm; border-bottom: 1.5px solid #2d5a35; padding-bottom: 1mm; }
.navod { margin: 0 0 2mm; font-style: italic; color: #333; }
.line { border-bottom: 1px solid #8a8a8a; height: 8.6mm; }
.dayhead { display: flex; align-items: baseline; gap: 5mm; border-bottom: 3px solid #7a4a1e; padding-bottom: 2mm; }
.dayhead .num { background: #7a4a1e; color: #fff; padding: 1mm 3mm; border-radius: 2mm; font-size: 13pt; font-weight: bold; }
.dayhead .dname { font-size: 26pt; font-weight: bold; color: #7a4a1e; }
.dayhead .tema { font-size: 16pt; margin-left: auto; color: #333; }
.ranni { margin-top: 3mm; background: #f4efe6; border-left: 4px solid #7a4a1e; padding: 2mm 3mm 0; }
ol { margin: 0; padding-left: 8mm; }
.vzp li { margin-bottom: 1mm; }
.q { font-weight: bold; }
.kviz li { margin-bottom: 1.6mm; } .kviz .q { font-size: 13pt; }
.opts { display: flex; gap: 8mm; flex-wrap: wrap; margin-top: 0.5mm; }
.circ { display: inline-block; width: 7mm; height: 7mm; border: 1.5px solid #444; border-radius: 50%; text-align: center; line-height: 6.4mm; font-family: 'DejaVu Sans'; font-size: 11pt; }
.dopl li { margin-bottom: 3.2mm; } .dopl.two { columns: 2; column-gap: 8mm; font-size: 12.5pt; } .dopl.two li { margin-bottom: 1.5mm; }
.vzkaz { border: 2px dashed #7a4a1e; padding: 2mm 4mm; margin-top: 3mm; border-radius: 3mm; }
.taj { border-collapse: separate; border-spacing: 1mm; margin-left: -1.2mm; }
.taj .clue { padding-right: 3mm; width: 88mm; font-size: 12.5pt; }
.taj .cnt { color: #777; font-size: 11pt; }
.taj .box { width: 8mm; height: 8mm; border: 1.5px solid #444; }
.taj .box.key { background: #e9dcc5; border: 2.5px solid #7a4a1e; }
.taj .nobox { width: 8mm; }
.taj-out { margin-top: 2mm; font-weight: bold; }
.fill { display: inline-block; border-bottom: 1px solid #555; width: 70mm; height: 6mm; vertical-align: bottom; }
.fill.short { width: 45mm; }
.rada li { margin-bottom: 2mm; font-size: 14.5pt; letter-spacing: .3px; }
.presm { display: grid; grid-template-columns: 1fr 1fr; gap: 3mm 8mm; font-size: 14pt; }
.spoj { width: 100%; font-size: 14pt; border-collapse: collapse; }
.spoj td { padding: 2mm 0; }
.spoj .l { text-align: right; width: 35%; } .spoj .r { width: 45%; } .spoj .gap { width: 20%; }
.dot { color: #7a4a1e; }
.poradi div { margin-bottom: 1.6mm; font-size: 14pt; }
.numbox { display: inline-block; width: 9mm; height: 9mm; border: 1.5px solid #444; vertical-align: middle; margin-right: 3mm; }
.seznam { font-size: 17pt; font-weight: bold; text-align: center; border: 2px solid #2d5a35; border-radius: 3mm; padding: 3mm; line-height: 1.6; margin-bottom: 2mm; }
.az { border-collapse: collapse; width: 100%; } .az td { padding: 0.8mm 2mm; vertical-align: top; }
.az .azfill { width: 48mm; vertical-align: bottom; } .az td { font-size: 12.8pt; }
.az .hexc { width: 11mm; } .az .hex { display: inline-block; line-height: 9mm; width: 9mm; height: 9mm; text-align: center; font: bold 15pt 'DejaVu Sans'; color: #fff; background: #2d5a35; border-radius: 50%; vertical-align: middle; }
.pocty li { margin-bottom: 2.5mm; } .ans { margin-top: 1mm; }
.clanek p { font-size: 12.8pt; line-height: 1.33; margin: 0 0 1.5mm; text-align: justify; hyphens: auto; }
.potclanku { background: #eef3ec; padding: 2mm 4mm 1mm; border-radius: 2mm; margin-top: 2mm; }
.potclanku li { margin-bottom: 1mm; }
.denik .dr { display: flex; align-items: flex-end; gap: 3mm; } .denik .dr span { white-space: nowrap; font-weight: bold; }
.denik .dr .line { flex: 1; }
/* titulní strana */
.cover { text-align: center; padding-top: 30mm; }
.cover h1 { font-size: 40pt; color: #7a4a1e; margin: 0 0 4mm; }
.cover .sub { font-size: 19pt; color: #2d5a35; margin-bottom: 14mm; }
.cover .orn { font-size: 46pt; margin: 10mm 0; }
.cover .box { text-align: left; border: 2px solid #2d5a35; border-radius: 4mm; padding: 5mm 8mm; font-size: 14.5pt; margin: 0 6mm; }
.cover .box li { margin-bottom: 2mm; }
.cover .sign { margin-top: 12mm; font-size: 17pt; font-style: italic; }
.res h2 { font-size: 22pt; color: #7a4a1e; }
.res .d { margin-bottom: 3mm; font-size: 11.5pt; line-height: 1.3; }
.res .d b.h { font-family: 'DejaVu Sans'; color: #2d5a35; }
.res .d div { margin-left: 5mm; }
"""

COVER = """
<section class="page cover">
  <div class="orn">🌻</div>
  <h1>Týden pro paměť</h1>
  <div class="sub">pro babičku a dědu · týden č. 1</div>
  <div class="box">
    <b>Jak na to:</b>
    <ul>
      <li>Každý den jeden list. Nejlépe ráno ke kávě, v klidu a spolu.</li>
      <li>Nic se nehodnotí, nikdo nezkouší. Když něco nevíte, nevadí – přeskočte to, nebo se podívejte do řešení na konci.</li>
      <li>Nejdůležitější je <b>povídání</b>. Vy víte věci, které my mladší už nevíme – každá zapsaná vzpomínka je pro nás poklad.</li>
      <li>Večer zapište pár slov o tom, co jste ten den dělali. Druhý den ráno si to zkusíte vybavit.</li>
    </ul>
  </div>
  <div class="sign">S láskou, vaše vnučka</div>
</section>
"""


def build():
    body = COVER + "".join(den_html(i + 1, d) for i, d in enumerate(DNY))
    res = "".join(
        f'<div class="d"><b class="h">{d}</b>' + "".join(f"<div>{r}</div>" for r in rs) + "</div>"
        for d, rs in RESENI.items())
    body += f'<section class="page res"><h2>Řešení</h2>{res}</section>'
    doc = f'<!doctype html><html lang="cs"><head><meta charset="utf-8"><title>Týden pro paměť</title><style>{CSS}</style></head><body>{body}</body></html>'
    (OUT / "tyden-1.html").write_text(doc, encoding="utf-8")


if __name__ == "__main__":
    build()
