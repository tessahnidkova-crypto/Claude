# -*- coding: utf-8 -*-
import os, sys, json
sp = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, sp)
from icons_hw import HW_ICONS

fonts = open(os.path.join(sp,"fonts_embed.css"), encoding='utf-8').read()
reuse = json.load(open(os.path.join(sp,"reuse_icons.json"), encoding='utf-8'))

CSS = '''
@page{size:A4 landscape;margin:0}
:root{--ink:#16323B;--sea:#0F8B8D;--stamp:#E4572E;--sun:#F2B028;--ok:#2E8B57;
 --line:#B9D2CE;--soft:#F2F8F6;--grey:#7A939B}
*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact}
html,body{margin:0;background:#fff;color:var(--ink);font-family:'Nunito',sans-serif}
.page{position:relative;width:297mm;height:210mm;padding:11mm 14mm 10mm;overflow:hidden;background:#fff;
 display:flex;flex-direction:column}
.airmail{position:absolute;top:0;left:0;right:0;height:4mm;
 background:repeating-linear-gradient(-45deg,var(--stamp) 0 6mm,#fff 6mm 12mm,var(--sea) 12mm 18mm,#fff 18mm 24mm)}
.foot{position:absolute;bottom:5mm;left:14mm;right:14mm;display:flex;justify-content:space-between;
 font-size:8pt;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--grey)}
.ph{flex:0 0 auto;display:flex;align-items:flex-end;justify-content:space-between;gap:8mm;
 border-bottom:1.2mm solid var(--ink);padding-bottom:2.5mm;margin-bottom:4mm}
.ph .grp{display:flex;align-items:center;gap:5mm}
.ph .no{font-family:'Fredoka',sans-serif;font-weight:600;font-size:15pt;color:#fff;background:var(--stamp);
 width:11mm;height:11mm;border-radius:50%;display:flex;align-items:center;justify-content:center;flex:0 0 auto}
.ph h2{font-family:'Fredoka',sans-serif;font-weight:600;font-size:27pt;margin:0;line-height:1}
.ph .task{font-size:11pt;font-weight:700;color:var(--sea);text-align:right;max-width:120mm}
h3{font-family:'Fredoka',sans-serif;font-weight:600;font-size:16pt;margin:0 0 2.5mm;color:var(--sea);
 display:flex;align-items:center;gap:2.5mm}
h3 .num{background:var(--sun);color:var(--ink);width:8mm;height:8mm;border-radius:50%;
 display:inline-flex;align-items:center;justify-content:center;font-size:11pt;font-weight:700;
 font-family:'Nunito',sans-serif;flex:0 0 auto}
h3 svg{width:9mm;height:9mm}
/* slovíčka */
.words{flex:0 0 auto;display:grid;grid-template-columns:repeat(6,1fr);gap:4mm;margin-bottom:4mm}
.wc{border:.6mm solid var(--line);border-radius:2mm;padding:3mm 2.5mm;display:flex;flex-direction:column;
 align-items:center;text-align:center;gap:1.2mm;background:#fff}
.wc svg{width:18mm;height:18mm}
.wc .en{font-family:'Fredoka',sans-serif;font-weight:600;font-size:14pt;line-height:1.05}
.wc .ph2{font-family:'DejaVu Sans Mono',monospace;font-size:8.5pt;color:var(--sea)}
.wc .cz{font-weight:800;font-size:12.5pt;color:var(--ink);border-top:.4mm dashed var(--line);
 padding-top:1.2mm;margin-top:.4mm;width:100%}
.wc .ex{font-size:7.5pt;color:var(--grey);font-style:italic;line-height:1.25;margin-top:.5mm}
/* spodek */
.bottom{flex:1;min-height:0;display:grid;grid-template-columns:1.15fr .85fr;gap:10mm;margin-bottom:13mm}
.bottom>div{display:flex;flex-direction:column;min-height:0}
.sent{flex:1;display:flex;flex-direction:column;justify-content:space-between}
.starter{font-family:'Fredoka',sans-serif;font-weight:600;font-size:16pt;margin-bottom:1mm}
.wl{border-bottom:.6mm solid var(--line);height:11mm}
.draw{flex:1;min-height:0;border:.8mm dashed var(--line);border-radius:2mm;display:flex;
 align-items:flex-end;justify-content:center;padding:4mm;text-align:center;position:relative}
.draw span{font-size:10pt;color:var(--grey);font-weight:700;letter-spacing:.06em;
 text-transform:uppercase;line-height:1.4}
.draw .deco{position:absolute;top:5mm;left:50%;transform:translateX(-50%);opacity:.18}
.draw .deco svg{width:34mm;height:34mm}
.bye{position:absolute;left:14mm;right:14mm;bottom:11mm;font-family:'Fredoka',sans-serif;
 font-weight:600;font-size:17pt;color:var(--stamp);text-align:center}
'''

WORDS = [
 ("i-seaside","seaside","SÍ-sajd","u moře","at the seaside"),
 ("i-inside","inside","in-SAJD","uvnitř","inside the house"),
 ("i-outside","outside","aut-SAJD","venku","outside in the garden"),
 ("i-but","but","bat","ale","I can swim <b>but</b> I can't ski."),
 ("i-need","need","níd","potřebovat","I <b>need</b> a ball."),
 ("i-bit","a little bit","e litl bit","trochu","I can cook <b>a little bit</b>."),
]
ST = ["I can …","I can't …","My best friend can …"]

def sprite():
    p=['<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>']
    for k,v in list(HW_ICONS.items())+list(reuse.items()):
        p.append('<symbol id="%s" viewBox="0 0 100 100">%s</symbol>'%(k,v))
    p.append('</defs></svg>'); return "".join(p)

cards="".join(
 '<div class="wc"><svg><use href="#%s"/></svg><span class="en">%s</span>'
 '<span class="ph2">[%s]</span><span class="cz">%s</span><span class="ex">%s</span></div>'%w
 for w in WORDS)
sts="".join('<div><div class="starter">%s</div><div class="wl"></div></div>'%s for s in ST)

HTML = f'''<meta charset="utf-8">
<title>Homework — What can you do?</title>
<style>
{fonts}
{CSS}
</style>
{sprite()}
<div class="page"><div class="airmail"></div>
 <div class="ph"><div class="grp"><span class="no">7</span><h2>Homework</h2></div>
  <span class="task">Learn the words. Write three sentences. Draw a picture. See you next week!</span></div>

 <h3><span class="num">1</span>Learn these words <span style="font-size:10pt;color:#7A939B;font-weight:700">
  &mdash; čti nahlas podle výslovnosti v závorce</span></h3>
 <div class="words">{cards}</div>

 <div class="bottom">
  <div><h3><span class="num">2</span>Write 3 sentences <svg><use href="#i-draw"/></svg></h3>
   <div class="sent">{sts}</div></div>
  <div><h3><span class="num">3</span>Draw &amp; label</h3>
   <div class="draw"><span class="deco"><svg><use href="#i-star"/></svg></span>
    <span>Draw yourself doing something<br>write one sentence with CAN</span></div></div>
 </div>

 <div class="bye">Great job today! See you next week!</div>
 <div class="foot"><span>English &middot; 15 September</span><span>Homework</span><span>Rozárka</span></div>
</div>'''

out=os.path.join(sp,"ukol.html")
open(out,"w",encoding='utf-8').write(HTML)
assert "</style>" in open(out,encoding='utf-8').read(), "CHYBÍ </style>!"
print("ukol.html hotov | </style> ok")
