# -*- coding: utf-8 -*-
import os, sys
sp = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, sp)
import tahak1_data as T1, tahak2_data as T2

fonts = open(os.path.join(sp,"fonts","embed.css"), encoding='utf-8').read()
base  = open(os.path.join(sp,"tahak_base.css"), encoding='utf-8').read()

EXTRA = '''
.cantab td{padding:1.8mm 2mm}
.cantab .who{font-weight:800;font-size:10pt;width:30%}
.cantab .pos{font-family:'Fredoka',sans-serif;font-weight:600;font-size:11pt;color:#2E7D4F;width:24%}
.cantab .neg{font-family:'Fredoka',sans-serif;font-weight:600;font-size:11pt;color:#E4572E;width:24%}
.cantab .ph2{font-family:'DejaVu Sans Mono',monospace;font-size:7.5pt;color:#0F8B8D}
.err td{padding:1.8mm 2mm}
.err .bad{font-weight:800;font-size:10pt;color:#E4572E;width:27%}
.err .bad u{text-decoration:none;background:#FBE3DB;padding:0 1mm;border-radius:1mm}
.err .good{font-weight:800;font-size:10pt;color:#2E7D4F;width:24%}
.err .why{font-size:8.5pt;color:#6E868D;font-weight:600;line-height:1.4}
.err .why b{color:#16323B}
.big{background:#16323B;color:#fff;border-radius:2mm;padding:4mm 5mm;margin-bottom:5mm;text-align:center}
.big .l1{font-family:'Fredoka',sans-serif;font-weight:600;font-size:16pt;line-height:1.25}
.big .l2{font-size:9.5pt;color:#9FC4C5;font-weight:700;margin-top:2mm;letter-spacing:.06em}
.klic{display:grid;grid-template-columns:repeat(3,1fr);gap:2mm 6mm;margin-bottom:5mm}
.klic div{font-size:9.5pt;font-weight:700;border-bottom:.3mm solid #C9DCD8;padding:1mm 0}
.klic div span{color:#6E868D;font-weight:600}
'''

def rows(items, cls=""):
    o=['<table class="%s">'%cls]
    for en,ph,cz in items:
        o.append('<tr><td class="en">%s</td><td class="ph">[%s]</td><td class="cz">%s</td></tr>'%(en,ph,cz))
    o.append('</table>'); return "\n".join(o)

TOT=7
def foot(n,lbl):
    return ('<div class="foot"><span>Tahák &middot; Rozárka &middot; hodina 2 &middot; 15. 9.</span>'
            '<span>%s</span><span>%d / %d</span></div>'%(lbl,n,TOT))
def page(title,sub,body,n,lbl):
    return ('<div class="page"><div class="airmail"></div>'
            '<div class="top"><h1>%s</h1><p>%s</p></div><div class="body">%s</div>%s</div>'
            %(title,sub,body,foot(n,lbl)))

S={t:(t,c,i) for t,c,i in T1.HODINA}
def sec(title):
    t,c,i=S[title]; return '<h2 class="%s">%s</h2>'%(c,t)+rows(i)

H=['<meta charset="utf-8">','<title>Tahák — hodina 2</title>','<style>',fonts,base,EXTRA,'</style>']

# 1
b='''<div class="note"><h3>Dneska se učí jedna jediná věc</h3>
<p><b>CAN = umět.</b> A po <b>can</b> se <u>nikdy</u> nepřidává koncové <b>-s</b> — ani u <i>my mum</i>, ani u <i>she</i>. To je přesně naopak než minule u <i>likes</i>. Celé pravidlo máš na straně 5.</p>
<p><b>Nemusíš mluvit anglicky celou hodinu.</b> Když nevíš, jak se něco řekne, řekni to česky — nikdy nehádej.</p>
<p><b>Výslovnost v závorkách je berlička, ne přesný přepis.</b> VELKÁ PÍSMENA = přízvuk.</p></div>'''
b+=sec("Na začátku")+sec("Pokyny během hodiny")
H.append(page("Tahák &mdash; hodina 2","Co jí říkat &middot; s výslovností",b,1,"Fráze"))

# 2
b=sec("Pochvala — používej hodně")+sec("Když to není správně — nikdy neříkej „No!“")
b+=sec("Když neví nebo nerozumí")
H.append(page("Pochvala, opravy, nejistota","Jak reagovat, ať ji to baví dál",b,2,"Fráze"))

# 3
b=sec("Na konci")
b+='<h2 class="ink">Když se to zvrtne</h2><table class="em">'
for w,a in T1.NOUZOVKY: b+='<tr><td class="w">%s</td><td class="a">%s</td></tr>'%(w,a)
b+='</table>'
b+='''<div class="note"><h3>Jak vést hru na straně 6</h3>
<p><b>Rozárka si tajně zakroužkuje jednu činnost.</b> Ty se ptáš <i>„Can you ski?“</i> a hádáš, kterou. Za každou otázku si odškrtne jedno kolečko — máš jich deset.</p>
<p>Ona odpovídá jen <b>„Yes, I can.“</b> nebo <b>„No, I can't.“</b> Když odpoví česky, zopakuj otázku a ukaž jí odpovědi v rámečku vedle mřížky.</p>
<p><b>Pak si role vyměňte</b> — to je ta důležitější polovina, protože tam musí otázky <i>tvořit</i>, ne jen odpovídat.</p></div>'''
H.append(page("Konec, nouzovky, hra","Jak zakončit &middot; co dělat, když &middot; pravidla hry",b,3,"Fráze"))

# 4
b='<div class="cols">'
for num,name,items in T2.STRANY:
    b+='<div class="pg"><h3><span>%s</span>%s</h3>%s</div>'%(num,name,rows(items))
b+='</div>'
H.append(page("Stranu po straně","Co říct u které aktivity v pracovním listu",b,4,"Podle stran listu"))

# 5 — gramatika CAN
b='''<div class="big"><div class="l1">CAN se nikdy nemění. Nikdy.</div>
<div class="l2">I CAN &middot; SHE CAN &middot; MY MUM CAN &middot; THEY CAN</div></div>'''
b+='<h2 class="sea">Celá tabulka &mdash; tohle je všechno, co v ní je</h2><table class="cantab">'
for who,pos,neg,ph in T2.CAN_TAB:
    b+=('<tr><td class="who">%s</td><td class="pos">%s</td><td class="neg">%s</td>'
        '<td class="ph2">[%s]</td></tr>'%(who,pos,neg,ph))
b+='</table>'
b+='''<p style="font-size:9.5pt;color:#6E868D;font-weight:600;margin:-2mm 0 5mm;line-height:1.45">
<b style="color:#16323B">Otázka:</b> <b style="color:#0F8B8D">Can you swim?</b> [ken jú swim] &rarr;
odpověď <b style="color:#2E7D4F">Yes, I can.</b> [jes, aj ken] / <b style="color:#E4572E">No, I can't.</b> [nou, aj kánt]
&nbsp;&mdash;&nbsp; <b style="color:#16323B">can't</b> se britsky čte <b>[kánt]</b> s dlouhým á.</p>'''
b+='<h2 class="stamp">Pět chyb, které udělá &mdash; a co na ně říct</h2><table class="err">'
for bad,good,why in T2.CAN_CHYBY:
    b+='<tr><td class="bad">%s</td><td class="good">%s</td><td class="why">%s</td></tr>'%(bad,good,why)
b+='</table>'
H.append(page("Gramatika: CAN","Jádro hodiny &middot; tabulka &middot; časté chyby",b,5,"Gramatika"))

# 6 — slovíčka + zásoba
b='<h2 class="sea">Dvanáct činností ze strany 3 &mdash; jak je předříkat</h2><table class="vc">'
for en,ph,cz,tip in T2.SLOVICKA:
    b+='<tr><td class="en">%s</td><td class="ph">[%s]</td><td class="cz">%s</td><td class="tip">%s</td></tr>'%(en,ph,cz,tip)
b+='</table>'
b+='''<div class="note"><h3>Jedna past, kterou u nás plete skoro každý</h3>
<p><b>U hudebních nástrojů je THE, u sportů není.</b></p>
<p><b style="color:#2E7D4F">play THE piano</b>, play THE guitar &nbsp;&nbsp;|&nbsp;&nbsp;
<b style="color:#2E7D4F">play football</b>, play tennis, play chess &mdash; <u>bez</u> the.</p></div>'''
for h,txt in T2.ZASOBA:
    b+='<div class="zas"><h4>%s</h4><p>%s</p></div>'%(h,txt)
H.append(page("Slovíčka a zásoba","Výslovnost &middot; past s THE &middot; co dělat, když zbyde čas",b,6,"Reference"))

# 7 — řešení
b='<h2 class="ok">Kontrola úkolu z minula &mdash; klíč</h2><div class="klic">'
for en,cz in T2.HW_KLIC:
    b+='<div>%s <span>= %s</span></div>'%(en,cz)
b+='</div>'
b+='<h2 class="ok">Strana 4 &mdash; jak mají vypadat její tři věty</h2>'+rows(T2.RES_STR4)
b+='<h2 class="ok">Strana 5 &mdash; co má říct o tobě</h2>'+rows(T2.RES_STR5)
b+='''<p style="font-size:9.5pt;color:#6E868D;font-weight:600;margin:-2mm 0 5mm;line-height:1.45">
Tady hlídej to <b style="color:#16323B">-s</b>: <b style="color:#E4572E">My teacher cans cook</b> je chyba.
Kdyby ho přidala, ukaž jí rámeček dole na straně 5 listu.</p>'''
b+='<h2 class="ok">Domácí úkol &mdash; vzorové věty</h2>'+rows(T2.RES_HW)
H.append(page("Řešení a vzorové odpovědi","Klíč k úkolu &middot; jak mají znít věty",b,7,"Řešení"))

out=os.path.join(sp,"tahak2.html")
open(out,"w",encoding='utf-8').write("\n".join(H))
assert "</style>" in open(out,encoding='utf-8').read(), "CHYBÍ </style>!"
print("tahak2.html hotov, stran:", TOT, "| </style> ok")
