# -*- coding: utf-8 -*-
import os, sys
sp = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, sp)
import metodika_data as M

fonts = open(os.path.join(sp,"fonts_embed.css"), encoding='utf-8').read()

CSS = '''
@page{size:A4 portrait;margin:0}
:root{--ink:#16323B;--sea:#0F8B8D;--stamp:#E4572E;--sun:#C98A0E;--ok:#2E7D4F;
 --line:#C9DCD8;--soft:#F4F9F8;--grey:#6E868D;--warm:#FDF6EC}
*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact}
html,body{margin:0;background:#fff;color:var(--ink);font-family:'Nunito',sans-serif}
.page{position:relative;width:210mm;height:297mm;padding:12mm 14mm 14mm;overflow:hidden;
 break-after:page;display:flex;flex-direction:column}
.page:last-child{break-after:auto}
.airmail{position:absolute;top:0;left:0;right:0;height:3mm;
 background:repeating-linear-gradient(-45deg,var(--stamp) 0 5mm,#fff 5mm 10mm,var(--sea) 10mm 15mm,#fff 15mm 20mm)}
.foot{position:absolute;bottom:5mm;left:14mm;right:14mm;display:flex;justify-content:space-between;
 font-size:7.5pt;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--grey)}
.top{flex:0 0 auto;display:flex;align-items:center;gap:5mm;border-bottom:1mm solid var(--ink);
 padding-bottom:3mm;margin-bottom:4mm}
.pgno{flex:0 0 auto;width:15mm;height:15mm;border-radius:2mm;background:var(--stamp);color:#fff;
 display:flex;flex-direction:column;align-items:center;justify-content:center;line-height:1}
.pgno b{font-family:'Fredoka',sans-serif;font-weight:600;font-size:16pt}
.pgno span{font-size:6.5pt;letter-spacing:.1em;text-transform:uppercase;margin-top:.5mm}
.top h1{font-family:'Fredoka',sans-serif;font-weight:600;font-size:21pt;margin:0;line-height:1.05;flex:1}
.top .min{font-family:'Fredoka',sans-serif;font-weight:600;font-size:12pt;color:var(--sea);flex:0 0 auto}
.goal{background:var(--ink);color:#fff;border-radius:2mm;padding:2.4mm 3.5mm;margin-bottom:3mm;
 font-family:'Fredoka',sans-serif;font-weight:500;font-size:11.5pt;line-height:1.28}
.goal b{color:#F2B028}
h2{font-family:'Fredoka',sans-serif;font-weight:600;font-size:12pt;margin:0 0 1.5mm;
 padding-left:3mm;border-left:1.6mm solid var(--sea);line-height:1.15;display:flex;
 align-items:baseline;gap:3mm}
h2 i{font-style:normal;font-size:8pt;font-weight:400;color:var(--grey);letter-spacing:.08em;text-transform:uppercase}
h2.plus{border-color:var(--sun);color:var(--sun)}
h2.gram{border-color:var(--stamp);color:var(--stamp)}
h2.key{border-color:var(--ok);color:var(--ok)}
table{width:100%;border-collapse:collapse;margin-bottom:3mm}
td{padding:1.1mm 2mm;vertical-align:top;border-bottom:.3mm solid var(--line)}
tr:nth-child(odd) td{background:var(--soft)}
.en{font-weight:800;font-size:10.5pt;width:38%}
.ph{font-family:'DejaVu Sans Mono',monospace;font-size:8.5pt;color:var(--sea);width:26%;padding-top:2mm}
.cz{font-size:9.5pt;color:var(--grey);font-weight:600}
table.plus tr:nth-child(odd) td{background:var(--warm)}
table.plus .ph{color:var(--sun)}
.gbox{border:.4mm solid var(--line);border-left:1.6mm solid var(--stamp);border-radius:1mm;
 padding:3mm 3.5mm;margin-bottom:3mm;background:#fff}
.gbox h3{font-family:'Fredoka',sans-serif;font-weight:600;font-size:11pt;margin:0 0 1.2mm;color:var(--ink)}
.gbox p{margin:0;font-size:9.5pt;line-height:1.5;color:var(--grey)}
.gbox p b{color:var(--ink)}
.gbox p i{color:var(--stamp);font-style:italic}
.kbox{border:.4mm solid var(--line);border-left:1.6mm solid var(--ok);border-radius:1mm;
 padding:2mm 3mm;margin-bottom:3mm;background:var(--soft)}
.kbox h3{font-family:'Fredoka',sans-serif;font-weight:600;font-size:10pt;margin:0 0 1mm;color:var(--ok)}
.kbox p{margin:0;font-size:9pt;line-height:1.45;color:var(--ink);font-weight:600}
.ends{margin-top:auto;display:grid;grid-template-columns:1fr 1fr;gap:4mm}
.ends div{border:.4mm dashed var(--line);border-radius:1mm;padding:2mm 2.5mm;background:#fff}
.ends .h{font-size:8pt;font-weight:700;letter-spacing:.1em;text-transform:uppercase;margin-bottom:1mm}
.ends .easy .h{color:var(--sea)} .ends .hard .h{color:var(--stamp)}
.ends p{margin:0;font-size:8.5pt;line-height:1.35;color:var(--ink);font-weight:600}
h2.step{border-color:#7A5AA8;color:#7A5AA8}
.steps{counter-reset:st;margin:0 0 3mm}
.steps .s{display:flex;gap:2.5mm;align-items:flex-start;padding:1.1mm 0;border-bottom:.3mm solid var(--line)}
.steps .s:last-child{border-bottom:none}
.steps .n{flex:0 0 auto;width:6.5mm;height:6.5mm;border-radius:50%;background:#7A5AA8;color:#fff;
 font-family:'Fredoka',sans-serif;font-weight:600;font-size:8.5pt;display:flex;align-items:center;
 justify-content:center;margin-top:.3mm}
.steps .x{font-size:9pt;line-height:1.4;color:var(--ink);font-weight:600}
.steps .x b{color:var(--stamp)}
.steps .x i{color:var(--sea);font-style:italic;font-weight:700}
/* dialog */
h2.dlg{border-color:#7A5AA8;color:#7A5AA8}
table.dlgt td{padding:1mm 2mm}
table.dlgt tr:nth-child(odd) td{background:#fff}
.dlgt .who{width:9%;font-family:'Fredoka',sans-serif;font-weight:600;font-size:9.5pt;
 letter-spacing:.06em;padding-top:2mm}
.dlgt .t-ty .who{color:var(--sea)} .dlgt .t-ona .who{color:var(--stamp)}
.dlgt .t-ty td{background:#EFF7F6 !important} .dlgt .t-ona td{background:#FDF3EC !important}
.dlgt .en{width:36%;font-size:11pt}
.dlgt .ph{width:25%;font-size:8.5pt;padding-top:2mm}
.dlgt .cz{font-size:9pt}
table.wrong td{padding:1.3mm 2mm}
.wrong .bad{width:27%;font-weight:800;font-size:10pt;color:var(--stamp)}
.wrong .bad u{text-decoration:none;background:#FBE3DB;padding:0 1mm;border-radius:1mm}
.wrong .good{width:22%;font-weight:800;font-size:10pt;color:var(--ok)}
.wrong .why{font-size:9pt;color:var(--grey);font-weight:600;line-height:1.4}
.wrong .why b{color:var(--ink)}
/* úvodní strana */
.hero{background:var(--ink);color:#fff;border-radius:2mm;padding:6mm;margin-bottom:5mm;text-align:center}
.hero .l1{font-family:'Fredoka',sans-serif;font-weight:600;font-size:22pt;line-height:1.15}
.hero .l2{font-size:10pt;color:#9FC4C5;font-weight:700;margin-top:2.5mm;letter-spacing:.06em;line-height:1.5}
.ctab td{padding:2mm}
.ctab .who{font-weight:800;font-size:10pt;width:26%}
.ctab .pos{font-family:'Fredoka',sans-serif;font-weight:600;font-size:11pt;color:var(--ok);width:22%}
.ctab .neg{font-family:'Fredoka',sans-serif;font-weight:600;font-size:11pt;color:var(--stamp);width:22%}
.ctab .p2{font-family:'DejaVu Sans Mono',monospace;font-size:7.5pt;color:var(--sea)}
.err td{padding:1.8mm 2mm}
.err .bad{font-weight:800;font-size:9.5pt;color:var(--stamp);width:28%}
.err .bad u{text-decoration:none;background:#FBE3DB;padding:0 1mm;border-radius:1mm}
.err .good{font-weight:800;font-size:9.5pt;color:var(--ok);width:24%}
.err .why{font-size:8.5pt;color:var(--grey);font-weight:600;line-height:1.4}
.err .why b{color:var(--ink)}
'''

CAN_TAB = [("I","can swim","can't swim","aj ken swim / aj kánt swim"),
 ("You","can swim","can't swim","jú ken swim"),
 ("She / My mum","can swim","can't swim","ší ken swim"),
 ("It / My dog","can swim","can't swim","it ken swim"),
 ("They / My friends","can swim","can't swim","dej ken swim")]

CAN_ERR = [
 ("My mum <u>cans</u> swim.","My mum can swim.",
  "Can nikdy nedostane <b>-s</b>. Minule se přidávat muselo (<i>likeS</i>), teď se nesmí."),
 ("I can <u>to</u> swim.","I can swim.","Po can jde holé sloveso, žádné <i>to</i>."),
 ("I can <u>swimming</u>.","I can swim.","Po can jde základní tvar, ne <i>-ing</i>."),
 ("<u>Do</u> you can swim?","Can you swim?","U can se DO nepoužívá. Jen se prohodí pořadí."),
 ("I <u>no can</u> swim.","I can't swim.","Zápor dělá <b>can't</b>, ne přidané <i>no</i>."),
]

TOT = len(M.CVICENI) * 2 + 1

def rows(items, cls=""):
    o=['<table class="%s">'%cls]
    for en,ph,cz in items:
        o.append('<tr><td class="en">%s</td><td class="ph">[%s]</td><td class="cz">%s</td></tr>'%(en,ph,cz))
    o.append('</table>'); return "\n".join(o)

def foot(n,lbl):
    return ('<div class="foot"><span>Metodika &middot; hodina 2 &middot; What can you do?</span>'
            '<span>%s</span><span>%d / %d</span></div>'%(lbl,n,TOT))

H=['<meta charset="utf-8">','<title>Metodika k hodině 2</title>','<style>',fonts,CSS,'</style>']

# --- strana 1: gramatika CAN celkově ---
b='''<div class="hero"><div class="l1">CAN se nikdy nemění.</div>
<div class="l2">I CAN &middot; YOU CAN &middot; SHE CAN &middot; MY MUM CAN &middot; THEY CAN<br>
Nikdy -s. Nikdy to. Nikdy -ing. Nikdy DO v otázce.</div></div>'''
b+='<h2 class="gram">Celá tabulka <i>víc v ní není</i></h2><table class="ctab">'
for who,pos,neg,ph in CAN_TAB:
    b+='<tr><td class="who">%s</td><td class="pos">%s</td><td class="neg">%s</td><td class="p2">[%s]</td></tr>'%(who,pos,neg,ph)
b+='</table>'
b+='''<div class="gbox"><h3>Otázka a krátká odpověď</h3>
<p><b>Can you swim?</b> [ken jú swim] &rarr; <b>Yes, I can.</b> [jes, aj ken] / <b>No, I can't.</b> [nou, aj kánt]<br>
<b>can't</b> se britsky čte <b>[kánt]</b> s dlouhým á. Americké [kent] neuč &mdash; ve škole mají britskou angličtinu.</p></div>
<div class="gbox"><h3>Proč se to nemění &mdash; a proč to Rozárka splete</h3>
<p><b>Can je modální sloveso</b> a modální slovesa se nečasují. Minulou hodinu se učila pravý opak:
u <i>like</i> se ve třetí osobě <b>-s</b> přidávat MUSÍ. <b>Rozlišit tyhle dva případy je celý smysl dnešní hodiny</b> &mdash;
počítej s tím, že to splete, a neber to jako nepozornost.</p></div>
<div class="gbox"><h3>Jak jí to vysvětlit česky &mdash; jednou větou</h3>
<p><b>„Can je jako české UMÍM. Řekneš ‚umím plavat‘ &mdash; a to sloveso za tím zůstane holé.
Nic se k němu nelepí, ať mluvíš o sobě, nebo o mámě.“</b></p></div>'''
b+='<h2 class="gram">Pět chyb, které udělá &mdash; a co na ně říct</h2><table class="err">'
for bad,good,why in CAN_ERR:
    b+='<tr><td class="bad">%s</td><td class="good">%s</td><td class="why">%s</td></tr>'%(bad,good,why)
b+='</table>'
H.append('<div class="page"><div class="airmail"></div>'
 '<div class="top"><div class="pgno" style="background:var(--sea)"><b>G</b><span>gram</span></div>'
 '<h1>Gramatika CAN<br>na jedné straně</h1></div>'
 '<div class="body" style="flex:1;min-height:0">%s</div>%s</div>'%(b,foot(1,"Gramatika")))

# --- strany cvičení: A = co říkáš ty, B = co řekne ona ---
n = 2
for pg,name,mins,goal,rict,navic,gram,klic,easy,hard in M.CVICENI:
    dlg, chyby = M.DIALOGY[pg]

    # ---- strana A ----
    a='<div class="goal">%s</div>'%goal
    a+='<h2 class="step">Jak na to <i>krok za krokem</i></h2><div class="steps">'
    for si,stp in enumerate(M.POSTUP[pg], 1):
        a+='<div class="s"><span class="n">%d</span><span class="x">%s</span></div>'%(si,stp)
    a+='</div>'
    a+='<h2>Co říkáš <i>pokyny k tomuhle cvičení</i></h2>'+rows(rict)
    a+='<h2 class="plus">Co můžeš říct navíc <i>když chceš z ní dostat víc</i></h2>'+rows(navic,"plus")
    for h,t in klic:
        a+='<div class="kbox" style="margin-top:2mm"><h3>%s</h3><p>%s</p></div>'%(h,t)
    a+=('<div class="ends"><div class="easy"><div class="h">Když jí to nejde</div><p>%s</p></div>'
        '<div class="hard"><div class="h">Když jí to jde moc snadno</div><p>%s</p></div></div>'%(easy,hard))
    H.append('<div class="page"><div class="airmail"></div>'
     '<div class="top"><div class="pgno"><b>%s</b><span>list</span></div>'
     '<h1>%s</h1><span class="min">%s</span></div>'
     '<div class="body" style="flex:1;min-height:0;display:flex;flex-direction:column">%s</div>%s</div>'
     %(pg,name,mins,a,foot(n,"Co říkáš ty")))
    n+=1

    # ---- strana B ----
    b='<h2 class="dlg">Co řekne ona <i>modelový průběh</i></h2><table class="dlgt">'
    for who,en,ph,cz in dlg:
        cls = "t-ty" if who=="TY" else "t-ona"
        b+=('<tr class="%s"><td class="who">%s</td><td class="en">%s</td>'
            '<td class="ph">%s</td><td class="cz">%s</td></tr>'
            %(cls, who, en, ("[%s]"%ph) if ph else "", cz))
    b+='</table>'
    b+='<h2 class="gram">Co řekne špatně <i>a co s tím</i></h2><table class="wrong">'
    for bad,good,why in chyby:
        b+='<tr><td class="bad">%s</td><td class="good">%s</td><td class="why">%s</td></tr>'%(bad,good,why)
    b+='</table>'
    b+='<h2 class="gram">Gramatika za tím</h2>'
    for h,t in gram:
        b+='<div class="gbox"><h3>%s</h3><p>%s</p></div>'%(h,t)
    H.append('<div class="page"><div class="airmail"></div>'
     '<div class="top"><div class="pgno" style="background:var(--grey)"><b>%s</b><span>list</span></div>'
     '<h1>%s <span style="font-size:12pt;color:#6E868D">&mdash; co řekne ona</span></h1></div>'
     '<div class="body" style="flex:1;min-height:0;display:flex;flex-direction:column">%s</div>%s</div>'
     %(pg,name,b,foot(n,"Co řekne ona")))
    n+=1

out=os.path.join(sp,"metodika.html")
open(out,"w",encoding='utf-8').write("\n".join(H))
assert "</style>" in open(out,encoding='utf-8').read(), "CHYBÍ </style>!"
print("metodika.html hotova, stran:", TOT, "| </style> ok")
