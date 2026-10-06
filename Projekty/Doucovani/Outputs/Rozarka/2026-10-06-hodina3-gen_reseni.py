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
.top h1{font-family:'Fredoka',sans-serif;font-weight:600;font-size:20pt;margin:0;line-height:1}
.top p{margin:1mm 0 0;font-size:9pt;color:var(--grey);font-weight:700;letter-spacing:.1em;text-transform:uppercase}
.body{flex:1;min-height:0;display:flex;flex-direction:column;justify-content:space-between}
.ex{border:.4mm solid var(--line);border-radius:1.5mm;overflow:hidden;background:#fff}
.ex .hd{background:var(--ink);color:#fff;display:flex;align-items:center;gap:3mm;padding:1.8mm 3mm}
.ex .hd .n{background:var(--stamp);width:7mm;height:7mm;border-radius:50%;flex:0 0 auto;
 display:flex;align-items:center;justify-content:center;font-size:9.5pt;font-weight:800}
.ex .hd h2{font-family:'Fredoka',sans-serif;font-weight:600;font-size:12.5pt;margin:0;flex:1;line-height:1.1}
.ex .hd em{font-style:normal;font-size:8.5pt;color:#9FC4C5;font-weight:700;letter-spacing:.08em}
.row{display:flex;gap:3mm;padding:1.6mm 3mm;border-bottom:.3mm solid var(--line);align-items:baseline}
.row:last-child{border-bottom:none}
.tag{flex:0 0 auto;width:24mm;font-size:7.5pt;font-weight:800;letter-spacing:.08em;text-transform:uppercase;
 padding-top:.4mm}
.row .txt{flex:1;font-size:9.5pt;line-height:1.5}
.r-uci .tag{color:var(--sea)} .r-uci{background:#F2F8F6}
.r-rekni .tag{color:var(--sun)} .r-rekni{background:#FFF8EC}
.r-rekni .txt{font-weight:700;font-style:italic;color:var(--ink)}
.r-res .tag{color:var(--ok)} .r-res .txt b{color:var(--ok)}
.r-poz .tag{color:var(--stamp)} .r-poz{background:#FDF2EE} .r-poz .txt b{color:var(--stamp)}
.mistakes{border:.4mm solid var(--line);border-left:1.8mm solid var(--stamp);border-radius:1mm;
 padding:2.5mm 3.5mm;background:var(--soft)}
.mistakes h3{font-family:'Fredoka',sans-serif;font-weight:600;font-size:12pt;margin:0 0 1.5mm;color:var(--stamp)}
.mistakes table{width:100%;border-collapse:collapse}
.mistakes td{padding:1.1mm 2mm;font-size:9pt;vertical-align:top;border-bottom:.3mm solid var(--line)}
.mistakes tr:last-child td{border-bottom:none}
.mistakes .bad{color:var(--stamp);font-weight:800;width:32%}
.mistakes .good{color:var(--ok);font-weight:800;width:26%}
.mistakes .why{color:var(--grey);font-weight:600}
'''

# (číslo strany listu, název, minuty, co se učí, řekni jí, řešení, pozor)
EX = [
("2","Hello again! + CAN","3 min",
 "Rozmluvit ji po třítýdenní pauze a ověřit, že CAN nevypadlo z hlavy.",
 "„Nejdřív si trochu popovídáme a zopakujeme, co už umíš.“",
 "<b>Yes, I can.</b> / <b>No, I can't.</b> &mdash; víc dnes nechtěj. Dole jedna věta <i>I can … but I can't …</i>",
 "Tady <b>neopravuj</b>. Po pauze je cílem rozmluvit ji, ne přesnost. Chyby si jen zapiš."),

("3","Verb BE","5 min",
 "Tvary slovesa <i>být</i> a jejich krátké tvary. Jádro celého unitu 2 &mdash; všechno ostatní na tom stojí.",
 "„Be je anglické JSEM, JSI, JE. V češtině ho můžeš vynechat, v angličtině nikdy &mdash; věta bez něj není věta.“",
 "I <b>'m</b> &middot; he / she / it <b>'s</b> &middot; we / you / they <b>'re</b><br>"
 "I<b>'m not</b> &middot; he <b>isn't</b> &middot; we <b>aren't</b><br>"
 "1 She<b>'s</b> from <b>Italy</b>. &nbsp; 2 I<b>'m</b> from <b>Spain</b>. &nbsp; 3 We<b>'re</b> from <b>Japan</b>. "
 "&nbsp; 4 He<b>'s</b> from <b>Hungary</b>. &nbsp; 5 They<b>'re</b> from <b>the Czech Republic</b>.",
 "Nejčastější chyba celé hodiny: <b>I from Brno</b> místo <i>I'm from Brno</i>. Není to překlep, je to čeština."),

("4","Words for the test","3 min",
 "Dvacet slov, která budou v testu &mdash; osm zemí a dvanáct slov o rodině.",
 "„Tohle jsou slova do testu. Přečteme si je nahlas a ty si označíš ta, co neznáš.“",
 "Tahle strana <b>se nevyplňuje</b>, jen se čte. Jsou to přesně ta slova, co pak jedete na čas na straně 5.",
 "U tří zemí se musí říct <b>the</b>: the USA, the Czech Republic, the UK. Výslovnost: "
 "<b>Hungary [HAN-ge-ry]</b> &middot; <b>aunt [ánt]</b> &middot; <b>uncle [ANKL]</b> &middot; <b>cousin [KAZN]</b>."),

("5","Word race","3 min",
 "Rychlé vybavení slov. Zároveň zjistíš, která slovíčka do testu ještě chybí.",
 "„Ukážu slovo, ty řekneš anglicky. Máš minutu. Co nevíš, přeskočíme.“",
 "<b>1.</b> Britain &middot; the USA &middot; France &middot; Italy &middot; Spain<br>"
 "<b>2.</b> Japan &middot; the Czech Republic &middot; Greece &middot; mother &middot; father<br>"
 "<b>3.</b> sister &middot; brother &middot; grandmother &middot; grandfather &middot; parents<br>"
 "<b>4.</b> children &middot; aunt &middot; uncle &middot; cousin &middot; daughter",
 "Během kola <b>neopravuj a nekomentuj</b> &mdash; běží čas. Po třetím kole si zapiš, co neuměla."),

("6","my / your / his / her","4 min",
 "Přivlastňovací zájmena. Druhá polovina toho, co test zkouší.",
 "„Před podstatným jménem nestojí ‚on‘ nebo ‚ona‘, ale ‚jeho‘, ‚její‘. Ne he name, ale HIS name.“",
 "I&rarr;<b>my</b> &middot; you&rarr;<b>your</b> &middot; he&rarr;<b>his</b> &middot; she&rarr;<b>her</b> &middot; "
 "it&rarr;<b>its</b> &middot; we&rarr;<b>our</b> &middot; they&rarr;<b>their</b><br>"
 "1 <b>His</b> &middot; 2 <b>Their</b> &middot; 3 <b>Its</b> &middot; 4 <b>Her</b> &middot; 5 <b>Our</b> &middot; 6 <b>your</b>",
 "Rozhoduje <b>majitel</b>, ne ta věc: <i>his sister</i> (kluk má sestru). Ptej se u každé věty "
 "<b>„Boy or girl?“</b> &mdash; a pozor na <b>its</b> (bez apostrofu) vs. <b>it's</b> (= it is)."),

("7","Questions and short answers","5 min",
 "Otázka se slovesem <i>be</i> a krátká odpověď. V Progress checku je to bodované cvičení.",
 "„U be se otázka dělá jen prohozením: You are → Are you? Nic se nepřidává, žádné DO.“",
 "Are you…? &rarr; <b>Yes, I am. / No, I'm not.</b> &nbsp;|&nbsp; Is your mum…? &rarr; <b>Yes, she is. / No, she isn't.</b><br>"
 "Are your friends…? &rarr; <b>Yes, they are. / No, they aren't.</b> &nbsp;|&nbsp; Is your dog…? &rarr; <b>Yes, it is. / No, it isn't.</b><br>"
 "Am I…? &rarr; <b>Yes, you are. / No, you aren't.</b> &nbsp;|&nbsp; Are we…? &rarr; <b>Yes, we are. / No, we aren't.</b>",
 "V <u>kladné</u> krátké odpovědi nikdy krátký tvar: <b>Yes, he is</b>, ne <i>Yes, he's</i>. "
 "V záporu krátký tvar být může. A nejtěžší je <i>Am I…?</i> &rarr; <b>Yes, you are</b> &mdash; ta výměna I/you."),

("8","Wh- questions","3 min",
 "Šest tázacích slov. Víc jich v testu nebude.",
 "„What je co, Where kde, Who kdo, When kdy, How old kolik let, Whose čí.“",
 "What's your name? &rarr; <b>My name's Rozárka.</b> &nbsp;|&nbsp; Where are you from? &rarr; <b>I'm from the Czech Republic.</b><br>"
 "How old are you? &rarr; <b>I'm eleven.</b> &nbsp;|&nbsp; When is your birthday? &rarr; <b>It's on 5th May.</b><br>"
 "Who is your teacher? &rarr; <b>Mrs Nováková.</b> &nbsp;|&nbsp; Whose dog is it? &rarr; <b>It's my sister's.</b>",
 "Chyták: <b>Who</b> [hú] = kdo, <b>Whose</b> [húz] = čí. Zní skoro stejně. "
 "A po tázacím slově jde <i>be</i> hned: <b>Where are you from?</b>, ne <i>Where you are from?</i>"),

("9","Possessive 's a dny v týdnu","4 min",
 "Přivlastňovací <b>'s</b> a sedm dní. Obojí je v Revision i v Self-assessmentu, takže to v testu bude.",
 "„Koncovka ’s se lepí na toho, komu to patří: Melina propiska = Mel’s pen.“",
 "This is <b>Mel's</b> pen. &middot; <b>Joe's</b> watch. &middot; <b>Jack and Maya's</b> dog. &middot; "
 "<b>Lin's</b> book. &middot; <b>Granddad and Grandma's</b> house.<br>"
 "Monday [MAN-dej] &middot; Tuesday [TJÚZ-dej] &middot; Wednesday [WENZ-dej] &middot; Thursday [THÉRZ-dej] &middot; "
 "Friday [FRAJ-dej] &middot; Saturday [SE-tr-dej] &middot; Sunday [SAN-dej]",
 "U dvou jmen jde <b>'s</b> jen na to poslední: <i>Jack and Maya's dog</i>. "
 "<b>Wednesday</b> se čte <b>[WENZ-dej]</b> &mdash; první <i>d</i> se nevyslovuje. Vyslovte to třikrát."),

("10","Homework","2 min",
 "Odejít s jasným zadáním. Slovíčka jsou rodinná &mdash; ta v testu budou.",
 "„Nauč se šest slovíček, napiš tři věty do sešitu a nakresli rodinu.“",
 "I'm from <b>Brno</b>. &middot; My mother's name is <b>…</b> &middot; My friends aren't <b>…</b><br>"
 "Slovíčka: mother &middot; father &middot; parents &middot; children &middot; cousin &middot; Whose?",
 "Nech ji úkol <b>zopakovat vlastními slovy</b> &mdash; tím ověříš, že rozumí, co má dělat."),

("11","Check list","1 min",
 "Sebehodnocení. Řekne ti přesně, co do testu zbývá.",
 "„Vybarvi hvězdu u všeho, co umíš. Buď upřímná &mdash; co nevybarvíš, na to se příště podíváme.“",
 "Řešení nemá &mdash; vyplňuje ho ona o sobě.",
 "<b>Vyfoť si tu stranu po hodině.</b> Prázdné hvězdy jsou plán na příští hodinu. "
 "Když vybarví všechny bez rozmyslu, zeptej se na jednu konkrétní: <i>„Say a negative sentence.“</i>"),

("12","Mini test","bonus",
 "Dvanáct úkolů ve stylu Progress checku. Ukáže jí, že to umí &mdash; a tobě, co dolaďit.",
 "„Zkus to sama, jako ve škole. Nebudu ti pomáhat a nebude to na známku.“",
 "1 <b>'m</b> &middot; 2 <b>isn't</b> &middot; 3 <b>Are</b> &middot; 4 <b>His</b> &middot; 5 <b>are</b> &middot; 6 <b>How</b><br>"
 "7 <b>are</b> &middot; 8 <b>isn't</b> &middot; 9 <b>Her</b> &middot; 10 <b>When</b> &middot; 11 <b>Mel's</b> &middot; 12 <b>Tuesday</b>",
 "Když zbyde pět minut, udělejte ho spolu; jinak ho zadej na doma. "
 "<b>Neopravuj ho na známku</b> &mdash; je to nácvik, ne zkouška."),
]

MIST = [("I <u>from</u> Brno.","I<b>'m</b> from Brno.","Vynechané sloveso &mdash; česká chyba. Nejčastější ze všech."),
 ("Yes, he<u>'s</u>.","Yes, he <b>is</b>.","V kladné krátké odpovědi nikdy krátký tvar."),
 ("<u>Do</u> you are…?","<b>Are</b> you…?","U <i>be</i> se jen prohodí pořadí, žádné DO."),
 ("<u>He</u> name is Joe.","<b>His</b> name is Joe.","Před podstatným jménem přivlastňovací zájmeno."),
 ("This is <u>Mel pen</u>.","This is <b>Mel's</b> pen.","Zapomenuté 's.")]

def block(n, title, mins, uci, rekni, res, poz):
    h = ('<div class="ex"><div class="hd"><span class="n">%s</span><h2>%s</h2><em>%s</em></div>'%(n,title,mins))
    h+= '<div class="row r-uci"><span class="tag">Co se učí</span><span class="txt">%s</span></div>'%uci
    h+= '<div class="row r-rekni"><span class="tag">Řekni jí</span><span class="txt">%s</span></div>'%rekni
    h+= '<div class="row r-res"><span class="tag">Řešení</span><span class="txt">%s</span></div>'%res
    if poz:
        h+= '<div class="row r-poz"><span class="tag">Pozor</span><span class="txt">%s</span></div>'%poz
    return h + '</div>'

mt='<div class="mistakes"><h3>Pět chyb, které uslyšíš &mdash; a co na ně říct</h3><table>'
for bad,good,why in MIST:
    mt+='<tr><td class="bad">%s</td><td class="good">%s</td><td class="why">%s</td></tr>'%(bad,good,why)
mt+='</table></div>'

PAGES = [(EX[0:4], "Řešení a vysvětlení", "Hodina 3 &middot; Unit 2 &middot; strany 2&ndash;5 listu", ""),
         (EX[4:8], "Řešení &mdash; pokračování", "Strany 6&ndash;9 listu", ""),
         (EX[8:],  "Řešení &mdash; závěr hodiny", "Strany 10&ndash;12 listu", mt)]

H=['<meta charset="utf-8">','<title>Řešení a vysvětlení — hodina 3</title>','<style>',fonts,CSS,'</style>']
for i,(blocks,title,sub,extra) in enumerate(PAGES,1):
    body="".join(block(*b) for b in blocks)
    H.append('<div class="page"><div class="airmail"></div>'
             '<div class="top"><h1>%s</h1><p>%s</p></div>'
             '<div class="body">%s%s</div>'
             '<div class="foot"><span>Řešení &middot; hodina 3 &middot; Unit 2</span>'
             '<span>Co se učí &middot; co říct &middot; klíč</span><span>%d / %d</span></div></div>'
             %(title,sub,body,extra,i,len(PAGES)))

out=os.path.join(sp,"reseni2.html")
open(out,"w",encoding='utf-8').write("\n".join(H))
assert "</style>" in open(out,encoding='utf-8').read(), "CHYBÍ </style>!"
print("reseni2.html hotovo, stran:", len(PAGES), "| cvičení:", len(EX), "| </style> ok")
