# -*- coding: utf-8 -*-
import os, sys
sp = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, sp)
fonts = open(os.path.join(sp,"fonts_embed.css"), encoding='utf-8').read()

CSS = '''
@page{size:A4 portrait;margin:0}
:root{--ink:#16323B;--sea:#0F8B8D;--stamp:#E4572E;--sun:#C98A0E;--ok:#2E7D4F;
 --line:#C9DCD8;--soft:#F4F9F8;--grey:#6E868D}
*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact}
html,body{margin:0;background:#fff;color:var(--ink);font-family:'Nunito',sans-serif}
.page{position:relative;width:210mm;height:297mm;padding:11mm 13mm 13mm;overflow:hidden;
 display:flex;flex-direction:column;background:#fff}
.airmail{position:absolute;top:0;left:0;right:0;height:3mm;
 background:repeating-linear-gradient(-45deg,var(--stamp) 0 5mm,#fff 5mm 10mm,var(--sea) 10mm 15mm,#fff 15mm 20mm)}
.foot{position:absolute;bottom:5mm;left:13mm;right:13mm;display:flex;justify-content:space-between;
 font-size:7.5pt;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--grey)}
.top{flex:0 0 auto;border-bottom:1mm solid var(--ink);padding-bottom:2.5mm;margin-bottom:4mm}
.top h1{font-family:'Fredoka',sans-serif;font-weight:600;font-size:21pt;margin:0;line-height:1}
.top p{margin:1mm 0 0;font-size:9pt;color:var(--grey);font-weight:700;letter-spacing:.1em;text-transform:uppercase}
.body{flex:1;min-height:0;display:flex;flex-direction:column;gap:3mm}
.ex{border:.4mm solid var(--line);border-left:1.8mm solid var(--sea);border-radius:1mm;
 padding:2.5mm 3.5mm;background:#fff}
.ex h2{font-family:'Fredoka',sans-serif;font-weight:600;font-size:12pt;margin:0 0 1.5mm;
 display:flex;align-items:center;gap:2.5mm;line-height:1.1}
.ex h2 .n{background:var(--sea);color:#fff;width:7mm;height:7mm;border-radius:50%;flex:0 0 auto;
 display:flex;align-items:center;justify-content:center;font-size:9pt;font-family:'Nunito',sans-serif;font-weight:800}
.ex h2 em{font-style:normal;font-size:8.5pt;color:var(--grey);font-weight:600;letter-spacing:.06em;
 text-transform:uppercase;margin-left:auto}
.ex p{margin:0;font-size:9.5pt;line-height:1.55;color:var(--ink)}
.ex p + p{margin-top:1.2mm}
.ex b{color:var(--ok)}
.ex .cz{color:var(--grey);font-weight:600}
.ex.warn{border-left-color:var(--stamp)}
.ex.warn h2 .n{background:var(--stamp)}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:1mm 6mm}
.tabline{font-family:'Fredoka',sans-serif;font-weight:600;font-size:10.5pt;color:var(--ok)}
.mistakes{border:.4mm solid var(--line);border-left:1.8mm solid var(--stamp);border-radius:1mm;
 padding:3mm 3.5mm;background:var(--soft);margin-top:auto}
.mistakes h3{font-family:'Fredoka',sans-serif;font-weight:600;font-size:12pt;margin:0 0 2mm;color:var(--stamp)}
.mistakes table{width:100%;border-collapse:collapse}
.mistakes td{padding:1.2mm 2mm;font-size:9.5pt;vertical-align:top;border-bottom:.3mm solid var(--line)}
.mistakes tr:last-child td{border-bottom:none}
.mistakes .bad{color:var(--stamp);font-weight:800;width:34%}
.mistakes .good{color:var(--ok);font-weight:800;width:28%}
.mistakes .why{color:var(--grey);font-weight:600}
'''

def ex(n, title, mins, body, warn=False):
    return ('<div class="ex%s"><h2><span class="n">%s</span>%s<em>%s</em></h2>%s</div>'
            %(" warn" if warn else "", n, title, mins, body))

P1 = [
 ex("2","Hello again! + CAN","3 min",
   "<p><b>Yes, I can.</b> / <b>No, I can't.</b> &mdash; víc dnes nechtěj.</p>"
   "<p class='cz'>Dole: <i>I can … but I can't …</i></p>"),
 ex("3","Verb BE","5 min",
   "<p class='tabline'>I <b>'m</b> &middot; he / she / it <b>'s</b> &middot; we / you / they <b>'re</b></p>"
   "<p class='tabline'>I<b>'m not</b> &middot; he <b>isn't</b> &middot; we <b>aren't</b></p>"
   "<p>1 She<b>'s</b> from <b>Italy</b>. &nbsp; 2 I<b>'m</b> from <b>Spain</b>. &nbsp; 3 We<b>'re</b> from <b>Japan</b>.</p>"
   "<p>4 He<b>'s</b> from <b>Hungary</b>. &nbsp; 5 They<b>'re</b> from <b>the Czech Republic</b>.</p>"),
 ex("4","Words for the test","3 min",
   "<p>Tahle strana nemá řešení &mdash; je to <b>přehled k přečtení</b>. "
   "Nech ji každé slovo přečíst nahlas podle výslovnosti v závorce.</p>"
   "<p class='cz'>Jsou to přesně ta slova, která pak jedete na čas na straně 5.</p>"),
 ex("5","Word race","3 min",
   "<p><b>1.</b> Britain &middot; the USA &middot; France &middot; Italy &middot; Spain<br>"
   "<b>2.</b> Japan &middot; the Czech Republic &middot; Greece &middot; mother &middot; father<br>"
   "<b>3.</b> sister &middot; brother &middot; grandmother &middot; grandfather &middot; parents<br>"
   "<b>4.</b> children &middot; aunt &middot; uncle &middot; cousin &middot; daughter</p>"
   "<p class='cz'>Výslovnost: Hungary [HAN-ge-ry] &middot; aunt [ánt] &middot; uncle [ANKL] &middot; "
   "cousin [KAZN] &middot; daughter [DÓ-tr] &middot; Greece [grís]</p>"),
 ex("6","my / your / his / her","4 min",
   "<p class='tabline'>I&rarr;my &middot; you&rarr;your &middot; he&rarr;his &middot; she&rarr;her &middot; "
   "it&rarr;its &middot; we&rarr;our &middot; they&rarr;their</p>"
   "<div class='grid2'><p>1 <b>His</b> name's Joe.</p><p>4 <b>Her</b> dog is Mut.</p>"
   "<p>2 <b>Their</b> names are Mary and Jack.</p><p>5 <b>Our</b> teacher is Mr Brown.</p>"
   "<p>3 <b>Its</b> name's Buddy.</p><p>6 What's <b>your</b> name?</p></div>"),
]

P2 = [
 ex("7","Questions and short answers","5 min",
   "<div class='grid2'>"
   "<p>Are you…? &rarr; <b>Yes, I am. / No, I'm not.</b></p>"
   "<p>Is your mum…? &rarr; <b>Yes, she is. / No, she isn't.</b></p>"
   "<p>Are your friends…? &rarr; <b>Yes, they are. / No, they aren't.</b></p>"
   "<p>Is your dog…? &rarr; <b>Yes, it is. / No, it isn't.</b></p>"
   "<p>Am I…? &rarr; <b>Yes, you are. / No, you aren't.</b></p>"
   "<p>Are we…? &rarr; <b>Yes, we are. / No, we aren't.</b></p></div>"),
 ex("8","Wh- questions","3 min",
   "<p>What's your name? &rarr; <b>My name's Rozárka.</b> &nbsp;|&nbsp; "
   "Where are you from? &rarr; <b>I'm from the Czech Republic.</b></p>"
   "<p>How old are you? &rarr; <b>I'm eleven.</b> &nbsp;|&nbsp; "
   "When is your birthday? &rarr; <b>It's on 5th May.</b></p>"
   "<p>Who is your teacher? &rarr; <b>Mrs Nováková.</b> &nbsp;|&nbsp; "
   "Whose dog is it? &rarr; <b>It's my sister's.</b></p>"),
 ex("9","Possessive 's a dny","4 min",
   "<p>This is <b>Mel's</b> pen. &middot; <b>Joe's</b> watch. &middot; <b>Jack and Maya's</b> dog. &middot; "
   "<b>Lin's</b> book. &middot; <b>Granddad and Grandma's</b> house.</p>"
   "<p class='cz'>Monday [MAN-dej] &middot; Tuesday [TJÚZ-dej] &middot; <b style='color:#E4572E'>Wednesday [WENZ-dej]</b> &middot; "
   "Thursday [THÉRZ-dej] &middot; Friday [FRAJ-dej] &middot; Saturday [SE-tr-dej] &middot; Sunday [SAN-dej]</p>"),
 ex("10","Homework","2 min",
   "<p>I'm from <b>Brno</b>. &middot; My mother's name is <b>…</b> &middot; My friends aren't <b>…</b></p>"
   "<p class='cz'>Slovíčka: mother &middot; father &middot; parents &middot; children &middot; cousin &middot; Whose?</p>"),
 ex("12","Mini test","bonus",
   "<div class='grid2'>"
   "<p>1 <b>'m</b> &nbsp; 2 <b>isn't</b> &nbsp; 3 <b>Are</b> &nbsp; 4 <b>His</b></p>"
   "<p>5 <b>are</b> &nbsp; 6 <b>How</b> &nbsp; 7 <b>are</b> &nbsp; 8 <b>isn't</b></p>"
   "<p>9 <b>Her</b> &nbsp; 10 <b>When</b></p>"
   "<p>11 <b>Mel's</b> &nbsp; 12 <b>Tuesday</b></p></div>"),
]

MIST = [("I <u>from</u> Brno.","I<b>'m</b> from Brno.","Vynechané sloveso &mdash; česká chyba. Nejčastější ze všech."),
 ("Yes, he<u>'s</u>.","Yes, he <b>is</b>.","V kladné krátké odpovědi nikdy krátký tvar."),
 ("<u>Do</u> you are…?","<b>Are</b> you…?","U <i>be</i> se jen prohodí pořadí, žádné DO."),
 ("<u>He</u> name is Joe.","<b>His</b> name is Joe.","Před podstatným jménem přivlastňovací zájmeno."),
 ("This is <u>Mel pen</u>.","This is <b>Mel's</b> pen.","Zapomenuté 's.")]

mt='<div class="mistakes"><h3>Pět chyb, které uslyšíš &mdash; a co na ně říct</h3><table>'
for bad,good,why in MIST:
    mt+='<tr><td class="bad">%s</td><td class="good">%s</td><td class="why">%s</td></tr>'%(bad,good,why)
mt+='</table></div>'

def page(n, title, sub, blocks, extra=""):
    return ('<div class="page"><div class="airmail"></div>'
            '<div class="top"><h1>%s</h1><p>%s</p></div>'
            '<div class="body">%s</div>%s'
            '<div class="foot"><span>Řešení &middot; hodina 3 &middot; Unit 2</span>'
            '<span>Klíč ke všem cvičením</span><span>%d / 2</span></div></div>'
            %(title, sub, "".join(blocks), extra, n))

HTML = ('<meta charset="utf-8">\n<title>Řešení — hodina 3</title>\n<style>\n'
        + fonts + CSS + '\n</style>\n'
        + page(1,"Řešení všech cvičení","Hodina 3 &middot; Unit 2 &middot; strany 2&ndash;6 listu", P1)
        + page(2,"Řešení &mdash; pokračování","Strany 7&ndash;12 listu", P2, mt))

out=os.path.join(sp,"reseni.html")
open(out,"w",encoding='utf-8').write(HTML)
assert "</style>" in open(out,encoding='utf-8').read(), "CHYBÍ </style>!"
print("reseni.html hotovo | </style> ok")
