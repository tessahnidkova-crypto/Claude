# -*- coding: utf-8 -*-
import os, sys
sp = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, sp)
from res3_data import EX, MIST, TIME

fonts = open(os.path.join(sp,"fonts_embed.css"), encoding='utf-8').read()

CSS = '''
@page{size:A4 landscape;margin:0}
:root{--ink:#16323B;--sea:#0F8B8D;--stamp:#E4572E;--sun:#C98A0E;--ok:#2E7D4F;
 --line:#C9DCD8;--soft:#F4F9F8;--warm:#FFF8EC;--grey:#6E868D}
*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact}
html,body{margin:0;background:#fff;color:var(--ink);font-family:'Nunito',sans-serif}
.page{position:relative;width:297mm;height:210mm;padding:9mm 11mm 10mm;overflow:hidden;
 display:flex;flex-direction:column;background:#fff;break-after:page}
.page:last-child{break-after:auto}
.airmail{position:absolute;top:0;left:0;right:0;height:2.6mm;
 background:repeating-linear-gradient(-45deg,var(--stamp) 0 5mm,#fff 5mm 10mm,var(--sea) 10mm 15mm,#fff 15mm 20mm)}

/* ---- hlavicka strany ---- */
.ph{display:flex;align-items:center;gap:4mm;border-bottom:1mm solid var(--ink);
 padding-bottom:2.5mm;margin-bottom:4mm;flex:0 0 auto}
.ph .no{font-family:'Fredoka',sans-serif;font-weight:600;font-size:16pt;color:#fff;background:var(--sea);
 min-width:12mm;height:12mm;border-radius:2.5mm;display:flex;align-items:center;justify-content:center;
 flex:0 0 auto;padding:0 2mm}
.ph h2{font-family:'Fredoka',sans-serif;font-weight:600;font-size:20pt;margin:0;flex:1;line-height:1.05}
.ph .meta{display:flex;gap:3mm;flex:0 0 auto}
.ph .chip{font-size:9.5pt;font-weight:800;letter-spacing:.05em;border:.7mm solid var(--line);
 border-radius:1.5mm;padding:1.6mm 3mm;color:var(--grey);white-space:nowrap}
.ph .chip b{color:var(--ink);display:block;font-size:11pt;letter-spacing:0}

/* ---- dva sloupce ---- */
.body{flex:1;min-height:0;display:grid;grid-template-columns:82mm 1fr;gap:7mm}
.left{display:flex;flex-direction:column;gap:3.5mm;min-height:0}
.right{min-height:0;display:flex;flex-direction:column;gap:0}

/* ---- karty vlevo ---- */
.card{border-radius:2mm;padding:3mm 3.5mm;line-height:1.4}
.card .lbl{font-size:8.5pt;font-weight:800;letter-spacing:.14em;text-transform:uppercase;
 display:block;margin-bottom:1.5mm}
.c-uci{background:var(--soft);border-left:1.6mm solid var(--sea)}
.c-uci .lbl{color:var(--sea)}
.c-uci .tx{font-size:11pt}
.c-rekni{background:var(--warm);border-left:1.6mm solid var(--sun)}
.c-rekni .lbl{color:var(--sun)}
.c-rekni p{margin:0 0 2mm;font-size:11.5pt;font-weight:700;font-style:italic;line-height:1.35}
.c-rekni p:last-child{margin-bottom:0}
.c-poz{background:#FFF1EC;border-left:1.6mm solid var(--stamp);margin-top:auto}
.c-poz .lbl{color:var(--stamp)}
.c-poz .tx{font-size:10.5pt;line-height:1.45}
.card s{color:var(--stamp);text-decoration-thickness:.5mm}

/* ---- reseni vpravo ---- */
.reslbl{font-size:8.5pt;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--ok);
 border-bottom:.7mm solid var(--ok);padding-bottom:1.2mm;margin-bottom:3mm;flex:0 0 auto}
.resbody{flex:1;min-height:0;overflow:hidden}
.kh{font-family:'Fredoka',sans-serif;font-weight:600;font-size:12.5pt;color:var(--sea);
 margin:0 0 2mm;letter-spacing:.01em}
.kh:not(:first-child){margin-top:3.5mm}
table.kt{width:100%;border-collapse:collapse;table-layout:fixed}
table.kt th{background:var(--ink);color:#fff;font-size:9pt;font-weight:800;letter-spacing:.08em;
 text-transform:uppercase;padding:1.6mm 2.5mm;text-align:left}
table.kt td{border:.4mm solid var(--line);padding:1.8mm 2.5mm;font-size:11pt;line-height:1.3;
 vertical-align:middle;word-wrap:break-word}
table.kt tr:nth-child(even) td{background:var(--soft)}
b.q{color:var(--stamp);font-family:'Fredoka',sans-serif;font-weight:600;margin-right:1.5mm}
b.a{color:var(--ok);font-family:'Fredoka',sans-serif;font-weight:600;font-size:12pt}
.ph2,.ph{}
span.ph{font-family:'DejaVu Sans Mono',monospace;font-size:8.5pt;color:var(--sea);font-weight:400}
ol.kl{margin:0;padding-left:7mm}
ol.kl li{font-size:12pt;line-height:1.5;margin-bottom:1.6mm;font-family:'Fredoka',sans-serif;font-weight:600}
ol.kl li::marker{color:var(--stamp);font-weight:700}
.kn{background:var(--warm);border:.5mm solid var(--line);border-radius:1.5mm;padding:2.2mm 3mm;
 font-size:10.5pt;line-height:1.4;margin-top:3mm}
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:4mm;align-items:start}

/* ---- zhusteni pro nabite strany ---- */
.t1 table.kt td{padding:1.3mm 2.2mm;font-size:10.5pt;line-height:1.25}
.t1 table.kt th{padding:1.2mm 2.2mm;font-size:8.5pt}
.t1 b.a{font-size:11.5pt}
.t1 .kh{font-size:11.5pt;margin-bottom:1.5mm}
.t1 .kh:not(:first-child){margin-top:2.5mm}
.t1 ol.kl li{font-size:11pt;margin-bottom:1.2mm;line-height:1.4}
.t1 .kn{padding:1.8mm 2.5mm;font-size:10pt;margin-top:2mm}
.t2 table.kt td{padding:1.0mm 2mm;font-size:10pt;line-height:1.2}
.t2 table.kt th{padding:1.0mm 2mm;font-size:8pt}
.t2 b.a{font-size:11pt}
.t2 span.ph{font-size:8pt}
.t2 .kh{font-size:11pt;margin-bottom:1.2mm}
.t2 .kh:not(:first-child){margin-top:2mm}
.t2 ol.kl li{font-size:10.5pt;margin-bottom:1mm;line-height:1.35}
.t2 .kn{padding:1.5mm 2.5mm;font-size:9.5pt;margin-top:1.5mm}

/* ---- paticka ---- */
.foot{flex:0 0 auto;display:flex;justify-content:space-between;align-items:center;
 border-top:.5mm solid var(--line);padding-top:2mm;margin-top:3.5mm;
 font-size:8.5pt;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--grey)}

/* ---- titulka ---- */
.cover{flex:1;display:grid;grid-template-columns:1.15fr 1fr;gap:9mm;min-height:0}
.cover h1{font-family:'Fredoka',sans-serif;font-weight:600;font-size:42pt;line-height:.98;margin:0 0 4mm}
.cover h1 span{color:var(--stamp)}
.kicker{font-size:10pt;font-weight:800;letter-spacing:.2em;text-transform:uppercase;color:var(--sea);margin:0 0 3mm}
.lead{font-size:12pt;line-height:1.5;margin:0 0 5mm}
.legend{display:flex;flex-direction:column;gap:2.5mm}
.lg{display:flex;gap:3mm;align-items:flex-start;font-size:10.5pt;line-height:1.35}
.lg .k{font-size:8.5pt;font-weight:800;letter-spacing:.1em;text-transform:uppercase;
 padding:1.2mm 2.5mm;border-radius:1.2mm;white-space:nowrap;flex:0 0 36mm;text-align:center}
.k1{background:var(--soft);color:var(--sea)} .k2{background:var(--warm);color:var(--sun)}
.k3{background:#EAF6EF;color:var(--ok)} .k4{background:#FFF1EC;color:var(--stamp)}
.tt{width:100%;border-collapse:collapse}
.tt th{background:var(--ink);color:#fff;font-size:9pt;font-weight:800;letter-spacing:.08em;
 text-transform:uppercase;padding:1.8mm 2.5mm;text-align:left}
.tt td{border-bottom:.4mm solid var(--line);padding:2mm 2.5mm;font-size:11pt}
.tt td.t{font-family:'DejaVu Sans Mono',monospace;font-size:10pt;color:var(--sea);width:14mm}
.tt td.n{font-family:'Fredoka',sans-serif;font-weight:600;color:var(--stamp);width:9mm;text-align:center}
.tt td.m{text-align:right;width:16mm;color:var(--grey);font-weight:700;font-size:10pt}
.tt tr:nth-child(even) td{background:var(--soft)}

/* ---- chyby ---- */
.mist{width:100%;border-collapse:collapse;flex:1}
.mist th{background:var(--ink);color:#fff;font-size:9.5pt;font-weight:800;letter-spacing:.08em;
 text-transform:uppercase;padding:2mm 3mm;text-align:left}
.mist td{border:.4mm solid var(--line);padding:2.4mm 3mm;font-size:12pt;vertical-align:middle}
.mist tr:nth-child(even) td{background:var(--soft)}
.mist .bad{color:var(--stamp);text-decoration:line-through;font-family:'Fredoka',sans-serif;
 font-weight:600;width:27%}
.mist .good{color:var(--ok);font-family:'Fredoka',sans-serif;font-weight:600;width:27%}
.mist .why{font-size:10.5pt;line-height:1.35}
'''

def foot(n, tot, lbl):
    return ('<div class="foot"><span>Řešení &middot; Hodina 3 &middot; 6. října</span>'
            '<span>%s</span><span>%d / %d</span></div>'%(lbl,n,tot))

P = []
import json
_tf = os.path.join(sp,"res3_tight.json")
_T = json.load(open(_tf)) if os.path.exists(_tf) else {}

TIGHT = {int(k):v for k,v in _T.items()}   # strana -> t1/t2, z res3_tight.json

def page(inner):
    cls = TIGHT.get(len(P)+1, "")
    P.append('<div class="page %s"><div class="airmail"></div>%s</div>'%(cls,inner))

# ---------- titulka ----------
tt = '<table class="tt"><tr><th>čas</th><th>#</th><th>co děláme</th><th>min</th></tr>'
for t,n,c,m in TIME:
    tt += '<tr><td class="t">%s</td><td class="n">%s</td><td>%s</td><td class="m">%s</td></tr>'%(t,n,c,m)
tt += '</table>'

cover = f'''<div class="cover">
<div>
 <p class="kicker">Jen pro tebe &middot; nepromítat</p>
 <h1>Řešení a<br><span>vysvětlení</span></h1>
 <p class="lead">Ke každému cvičení jedna strana: co se tím učí, co jí máš říct,
 <b>celé vypsané řešení</b> a na co si dát pozor. Strany jdou ve stejném pořadí
 jako list, který jí promítáš.</p>
 <div class="legend">
  <div class="lg"><span class="k k1">Co se učí</span><span>proč tam to cvičení je &mdash; abys věděla, co máš z Rozárky dostat</span></div>
  <div class="lg"><span class="k k2">Řekni jí</span><span>věty k přečtení nahlas, slovo od slova</span></div>
  <div class="lg"><span class="k k3">Řešení</span><span>všechny odpovědi vypsané celé, <b>zeleně</b></span></div>
  <div class="lg"><span class="k k4">Pozor</span><span>chyby, které udělá, a jak je opravit</span></div>
 </div>
</div>
<div style="display:flex;flex-direction:column;min-height:0">
 <div class="kh" style="margin-top:0">Časovka na 30 minut</div>
 {tt}
 <div class="kn"><b>Cvičení 1&ndash;8 zaberou přesně 30 minut &mdash; mini test se tam už nevejde.</b>
 Něco musí ven. Doporučení: vynech <b>cvičení 4 (Word race)</b> a zadej ho domů; ušetříš 3 minuty.
 Zbylé 2 minuty vem z cvičení 3 (slovíčka) &mdash; stačí přečíst jen jeden sloupec.
 <b>Mini test nech vždycky</b>, ten jediný ti řekne, jestli je na test připravená.</div>
</div>
</div>'''
page(cover + foot(1, 1, "Přehled"))

TOT = 1 + len(EX) + 1

# ---------- cviceni ----------
for i,(no,title,lstr,mins,uci,rekni,res,poz) in enumerate(EX, start=2):
    rek = "".join('<p>%s</p>'%r for r in rekni)
    left = ('<div class="card c-uci"><span class="lbl">Co se učí</span>'
            '<div class="tx">%s</div></div>'%uci)
    left += ('<div class="card c-rekni"><span class="lbl">Řekni jí</span>%s</div>'%rek)
    if poz:
        left += ('<div class="card c-poz"><span class="lbl">Pozor &mdash; tady chybuje</span>'
                 '<div class="tx">%s</div></div>'%poz)
    head = ('<div class="ph"><span class="no">%s</span><h2>%s</h2><div class="meta">'
            '<span class="chip">na listu<b>strana %d</b></span>'
            '<span class="chip">čas<b>%s</b></span></div></div>'%(no,title,lstr,mins))
    body = ('<div class="body"><div class="left">%s</div>'
            '<div class="right"><div class="reslbl">Řešení</div>'
            '<div class="resbody">%s</div></div></div>'%(left,res))
    page(head + body + foot(i, TOT, "Cvičení %s"%no.replace("&#9733;","★")))

# ---------- caste chyby ----------
mt = '<table class="mist"><tr><th>Řekne / napíše</th><th>Správně je</th><th>Proč</th></tr>'
for bad,good,why in MIST:
    mt += '<tr><td class="bad">%s</td><td class="good">%s</td><td class="why">%s</td></tr>'%(bad,good,why)
mt += '</table>'
head = ('<div class="ph"><span class="no">!</span><h2>Deset chyb, které uslyšíš</h2>'
        '<div class="meta"><span class="chip">platí<b>celou hodinu</b></span></div></div>')
page(head + mt +
     '<div class="kn" style="margin-top:3mm">Když chybu udělá, <b>neopravuj ji slovem</b> &mdash; '
     'jen zopakuj větu správně a nech ji to říct po tobě. Oprava, kterou si řekne sama, drží; '
     'oprava, kterou slyší, ne.</div>' +
     foot(TOT, TOT, "Časté chyby"))

H = ['<meta charset="utf-8">','<title>Hodina 3 — řešení a vysvětlení</title>',
     '<style>', fonts, CSS, '</style>'] + P
out = os.path.join(sp,"res3.html")
open(out,"w",encoding='utf-8').write("\n".join(H))
txt = open(out,encoding='utf-8').read()
assert "</style>" in txt, "CHYBÍ </style>!"
print("res3.html hotov | stran:", TOT, "| </style> ok")
