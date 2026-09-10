# -*- coding: utf-8 -*-
import sys, os
sp = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, sp)
import tahak_data as T

css = open(os.path.join(sp,"fonts","embed.css"), encoding='utf-8').read()

HEAD = '<meta charset="utf-8">\n<title>Tahák pro učitele</title>\n<style>\n'+css+'''
@page{size:A4 portrait;margin:0}
:root{--ink:#16323B;--sea:#0F8B8D;--stamp:#E4572E;--sun:#C98A0E;--ok:#2E7D4F;
 --line:#C9DCD8;--soft:#F4F9F8;--grey:#6E868D}
*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact}
html,body{margin:0;background:#fff;color:var(--ink);font-family:'Nunito',sans-serif}
.page{position:relative;width:210mm;height:297mm;padding:13mm 14mm 15mm;overflow:hidden;
 break-after:page;display:flex;flex-direction:column}
.page:last-child{break-after:auto}
.airmail{position:absolute;top:0;left:0;right:0;height:3mm;
 background:repeating-linear-gradient(-45deg,var(--stamp) 0 5mm,#fff 5mm 10mm,var(--sea) 10mm 15mm,#fff 15mm 20mm)}
.foot{position:absolute;bottom:6mm;left:14mm;right:14mm;display:flex;justify-content:space-between;
 font-size:7.5pt;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--grey)}
.top{flex:0 0 auto;border-bottom:1mm solid var(--ink);padding-bottom:2.5mm;margin-bottom:5mm}
.top h1{font-family:'Fredoka',sans-serif;font-weight:600;font-size:22pt;margin:0;line-height:1}
.top p{margin:1mm 0 0;font-size:9pt;color:var(--grey);font-weight:700;letter-spacing:.1em;text-transform:uppercase}
.body{flex:1;min-height:0}
h2{font-family:'Fredoka',sans-serif;font-weight:600;font-size:13pt;margin:0 0 1.5mm;
 padding-left:3mm;border-left:1.6mm solid var(--sea);line-height:1.15}
h2.ink{border-color:var(--ink)} h2.ok{border-color:var(--ok);color:var(--ok)}
h2.stamp{border-color:var(--stamp);color:var(--stamp)} h2.sun{border-color:var(--sun);color:var(--sun)}
h2.sea{border-color:var(--sea);color:var(--sea)}
table{width:100%;border-collapse:collapse;margin-bottom:4.5mm}
td{padding:1.5mm 2mm;vertical-align:top;border-bottom:.3mm solid var(--line)}
tr:nth-child(odd) td{background:var(--soft)}
.en{font-weight:800;font-size:10.5pt;width:38%}
.ph{font-family:'DejaVu Sans Mono',monospace;font-size:8.5pt;color:var(--sea);width:27%;padding-top:2mm}
.cz{font-size:9.5pt;color:var(--grey);font-weight:600}
.note{background:var(--soft);border:.4mm solid var(--line);border-left:1.6mm solid var(--stamp);
 border-radius:1mm;padding:3.5mm 4mm;margin-bottom:5mm}
.note h3{font-family:'Fredoka',sans-serif;font-weight:600;font-size:12pt;margin:0 0 2mm;color:var(--stamp)}
.note p{margin:0 0 1.5mm;font-size:10pt;line-height:1.45}
.note p:last-child{margin-bottom:0}
.note b{color:var(--ink)}
.cols{column-count:2;column-gap:8mm}
.pg{margin-bottom:4mm;break-inside:avoid;-webkit-column-break-inside:avoid}
.pg h3{font-family:'Fredoka',sans-serif;font-weight:600;font-size:11.5pt;margin:0 0 1.5mm;color:var(--ink)}
.pg h3 span{display:inline-block;background:var(--stamp);color:#fff;width:6mm;height:6mm;border-radius:50%;
 text-align:center;line-height:6mm;font-size:9pt;margin-right:1.5mm}
.pg table{margin-bottom:0}
.pg td{padding:1.1mm 1.5mm}
.pg .en{width:42%;font-size:9pt}
.pg .ph{width:30%;font-size:7.5pt;padding-top:1.6mm}
.pg .cz{font-size:8pt}
.vc .en{width:24%} .vc .ph{width:20%} .vc .cz{width:20%}
.vc .tip{font-size:8.5pt;color:var(--stamp);font-weight:700}
.snd td{padding:2mm}
.snd .s{font-family:'Fredoka',sans-serif;font-weight:600;font-size:16pt;color:var(--sea);width:9%}
.snd .ex{font-family:'DejaVu Sans Mono',monospace;font-size:8pt;color:var(--ink);width:26%}
.snd .d{font-size:9pt;line-height:1.4}
.snd .d i{display:block;color:var(--stamp);font-weight:700;font-style:normal;margin-top:1mm;font-size:8.5pt}
.em td{padding:1.3mm 2mm}
.em .w{width:38%;font-weight:800;font-size:9pt}
.em .a{font-size:9pt;color:var(--grey);font-weight:600;line-height:1.38}
.abc{display:grid;grid-template-columns:repeat(7,1fr);gap:2mm;margin-bottom:4mm}
.abc div{border:.4mm solid var(--line);border-radius:1mm;padding:1.5mm 1mm;text-align:center;background:var(--soft)}
.abc b{font-family:'Fredoka',sans-serif;font-weight:600;font-size:14pt;display:block;line-height:1}
.abc span{font-family:'DejaVu Sans Mono',monospace;font-size:7.5pt;color:var(--sea);display:block;margin-top:.8mm}
/* --- řešení --- */
.qa{margin-bottom:3.5mm;break-inside:avoid;-webkit-column-break-inside:avoid}
.qa .qq{font-family:'Fredoka',sans-serif;font-weight:600;font-size:10.5pt;color:var(--ink);
 border-bottom:.5mm solid var(--sea);padding-bottom:.8mm;margin-bottom:1mm}
.qa table{margin:0}
.qa td{padding:1mm 1.5mm}
.qa .en{width:46%;font-size:9pt}
.qa .ph{width:28%;font-size:7.5pt;padding-top:1.5mm}
.qa .cz{font-size:8pt}
.odd .zad{font-family:'DejaVu Sans Mono',monospace;font-size:8.5pt;width:36%;line-height:1.5}
.odd .zad b{color:var(--stamp);font-family:'Nunito',sans-serif;font-weight:800;font-size:9.5pt}
.odd .ans{font-weight:800;font-size:9.5pt;width:32%}
.odd .ans span{display:block;font-family:'DejaVu Sans Mono',monospace;font-weight:400;
 font-size:7.5pt;color:var(--sea);margin-top:.6mm}
.odd .cz{font-size:8.5pt}
.chal .n{font-family:'Fredoka',sans-serif;font-weight:600;font-size:11pt;color:#fff;width:7mm;
 text-align:center;background:var(--sea)!important;padding:1mm}
.chal .u{font-weight:800;font-size:9pt;width:31%}
.chal .r{font-size:9pt;color:var(--ink);font-weight:700;width:32%}
.chal .p{font-size:8pt;color:var(--grey);font-weight:600;line-height:1.35}
.zas{margin-bottom:2.5mm}
.zas h4{font-family:'Fredoka',sans-serif;font-weight:600;font-size:10.5pt;margin:0 0 .8mm;color:var(--sea)}
.zas p{margin:0;font-size:9pt;line-height:1.55;color:var(--ink)}
.zas p b{color:var(--stamp)}
</style>
'''

def rows(items, cls=""):
    o=['<table class="%s">'%cls]
    for en,ph,cz in items:
        o.append('<tr><td class="en">%s</td><td class="ph">[%s]</td><td class="cz">%s</td></tr>'%(en,ph,cz))
    o.append('</table>'); return "\n".join(o)

TOT = 8
def foot(n,lbl):
    return ('<div class="foot"><span>Tahák &middot; Rozárka &middot; 10. 9.</span>'
            '<span>%s</span><span>%d / %d</span></div>'%(lbl,n,TOT))
def page(title,sub,body,n,lbl):
    return ('<div class="page"><div class="airmail"></div>'
            '<div class="top"><h1>%s</h1><p>%s</p></div><div class="body">%s</div>%s</div>'
            %(title,sub,body,foot(n,lbl)))

S={t:(t,c,i) for t,c,i in T.HODINA}
def sec(title):
    t,c,i=S[title]; return '<h2 class="%s">%s</h2>'%(c,t)+rows(i)

H=[HEAD]

# 1
b='''<div class="note"><h3>Přečti si tohle první</h3>
<p><b>Nemusíš mluvit anglicky celou hodinu.</b> U páté třídy je úplně normální, že učitel vysvětluje česky a anglicky říká pokyny, pochvaly a učivo. Radši míň angličtiny správně než hodně špatně.</p>
<p><b>Když nevíš, jak se něco řekne, řekni to česky.</b> Nikdy nehádej — Rozárka se naučí i tvoji chybu a u zkoušení ji zopakuje.</p>
<p><b>Výslovnost v hranatých závorkách je berlička, ne přesný přepis.</b> Čeština nemá anglické <i>th</i>, <i>w</i> ani nepřízvučné samohlásky — přiblížíš se, netrefíš přesně. To úplně stačí. VELKÁ PÍSMENA = přízvuk.</p></div>'''
b+=sec("Na začátku")+sec("Pokyny během hodiny")
H.append(page("Tahák pro učitele","Co jí říkat &middot; s výslovností",b,1,"Fráze na hodinu"))

# 2
b=sec("Pochvala — používej hodně")+sec("Když to není správně — nikdy neříkej „No!“")
b+='''<div class="note"><h3>Jak opravovat, aby ji to neodradilo</h3>
<p><b>Neříkej „to je špatně“.</b> Zopakuj to správně jako běžnou reakci — dítě si opravu vezme samo.</p>
<p>Ona: <i>„I go to sea.“</i> &nbsp;&rarr;&nbsp; Ty: <b>„Ah, you went to the seaside! Nice.“</b> [á, jú went tu ď SÍ-sajd! najs]</p>
<p>Ona: <i>„My mum like ice cream.“</i> &nbsp;&rarr;&nbsp; Ty: <b>„Yes, your mum likeS ice cream.“</b> — zdůrazni to <b>-s</b> hlasem.</p></div>'''
H.append(page("Pochvala a opravy","Jak reagovat, ať ji to baví dál",b,2,"Fráze na hodinu"))

# 3
b=sec("Když neví nebo nerozumí")+sec("Na konci")
b+='<h2 class="ink">Když se to zvrtne</h2><table class="em">'
for w,a in T.NOUZOVKY: b+='<tr><td class="w">%s</td><td class="a">%s</td></tr>'%(w,a)
b+='</table>'
H.append(page("Nejistota, konec, nouzovky","Když neví &middot; jak zakončit &middot; co dělat, když",b,3,"Fráze na hodinu"))

# 4
b='<div class="cols">'
for num,name,items in T.STRANY:
    b+='<div class="pg"><h3><span>%s</span>%s</h3>%s</div>'%(num,name,rows(items))
b+='</div>'
H.append(page("Stranu po straně","Co říct u které aktivity v pracovním listu",b,4,"Podle stran listu"))

# 5
b='<h2 class="sea">Slovíčka ze strany 3 &mdash; jak je předříkat</h2><table class="vc">'
for en,ph,cz,tip in T.SLOVICKA:
    b+='<tr><td class="en">%s</td><td class="ph">[%s]</td><td class="cz">%s</td><td class="tip">%s</td></tr>'%(en,ph,cz,tip)
b+='</table><h2 class="stamp">Tři hlásky, které Čechy prozradí</h2><table class="snd">'
for s,ex,desc,tip in T.ZVUKY:
    b+='<tr><td class="s">%s</td><td class="ex">%s</td><td class="d">%s<i>%s</i></td></tr>'%(s,ex,desc,tip)
b+='</table><h2 class="sun">Abeceda &mdash; na úkol „Spell BEACH out loud“</h2><div class="abc">'
for l,p in T.ABECEDA: b+='<div><b>%s</b><span>%s</span></div>'%(l,p)
b+='''</div><p style="font-size:9pt;color:#6E868D;font-weight:600;margin:0;line-height:1.45">
<b style="color:#16323B">BEACH se hláskuje</b> [bí &middot; í &middot; ej &middot; sí &middot; ejč].
&nbsp;<b style="color:#16323B">Z</b> se v britské angličtině (tu se u nás učí) říká <b style="color:#0F8B8D">[zed]</b>, v americké [zí] &mdash; uč ji [zed].</p>'''
H.append(page("Slovíčka, zvuky, abeceda","Výslovnost &middot; tři zrádné hlásky &middot; hláskování",b,5,"Reference"))

# 6 — řešení str. 2 a 4
b='<h2 class="ok">Strana 2 &mdash; Hello again! &nbsp;<span style="font-size:9pt;color:#6E868D">Vzorové odpovědi, když se zasekne</span></h2><div class="cols">'
for q,ans in T.RES_HELLO:
    b+='<div class="qa"><div class="qq">%s</div>%s</div>'%(q,rows(ans))
b+='</div>'
b+='''<h2 class="ok">Strana 4 &mdash; Sentence machine</h2>
<div class="note" style="border-left-color:#2E7D4F"><h3 style="color:#2E7D4F">Jediné pravidlo, které se tu učí</h3>
<p><b>I</b> &rarr; <b>like</b> / <b>don't like</b> &nbsp;&nbsp;|&nbsp;&nbsp; <b>My mum, My best friend, My dog, My teacher</b> &rarr; <b>likes</b> / <b>doesn't like</b></p>
<p>Čili: u všeho, co se dá nahradit <i>he / she / it</i>, přibude <b>-s</b>. A pozor — po <b>doesn't</b> už se <b>-s</b> nepíše: <i>doesn't likeS</i> je chyba.</p></div>'''
b+=rows(T.RES_SENT_VETY)
H.append(page("Řešení &mdash; strany 2 a 4","Vzorové odpovědi &middot; pravidlo třetí osoby",b,6,"Řešení"))

# 7 — řešení str. 5 a 7
b='<h2 class="ok">Strana 5 &mdash; Odd one out</h2><table class="odd">'
for zad,key,en,ph,cz in T.RES_ODD:
    zz=zad
    for w in zad.split(" · "):
        if w.isupper(): zz=zz.replace(w,"<b>%s</b>"%w.lower())
    b+='<tr><td class="zad">%s</td><td class="ans">%s<span>[%s]</span></td><td class="cz">%s</td></tr>'%(zz,en,ph,cz)
b+='</table>'
b+='<p style="font-size:9pt;color:#6E868D;font-weight:600;margin:-2mm 0 5mm;line-height:1.45">Tučně je slovo, které tam nepatří. Nech ji zkusit odpověď <b style="color:#16323B">dřív</b>, než jí poradíš — a stačí, když zdůvodnění řekne jednoduše.</p>'
b+='<h2 class="ok">Strana 7 &mdash; Homework: jak mají věty vypadat</h2>'
for st,ans in T.RES_HW:
    b+='<div class="qa"><div class="qq">%s</div>%s</div>'%(st,rows(ans))
H.append(page("Řešení &mdash; strany 5 a 7","Klíč k Odd one out &middot; vzorové věty do úkolu",b,7,"Řešení"))

# 8 — řešení str. 6 + zásoba slov
b='<h2 class="ok">Strana 6 &mdash; Star challenge: co má zaznít</h2><table class="chal">'
for n,u,r,p in T.RES_CHALLENGE:
    b+='<tr><td class="n">%s</td><td class="u">%s</td><td class="r">%s</td><td class="p">%s</td></tr>'%(n,u,r,p)
b+='</table><h2 class="sea">Zásoba slov, kterou u těch úkolů potřebuješ</h2>'
for h,txt in T.ZASOBA:
    b+='<div class="zas"><h4>%s</h4><p>%s</p></div>'%(h,txt)
H.append(page("Řešení &mdash; strana 6","Star challenge &middot; zásoba slov k úkolům",b,8,"Řešení"))

open(os.path.join(sp,"tahak.html"),"w",encoding='utf-8').write("\n".join(H))
print("tahák: 8 stran")
