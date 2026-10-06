# -*- coding: utf-8 -*-
import os, sys, json
sp = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, sp)
from flags import FLAGS

fonts = open(os.path.join(sp,"fonts_embed.css"), encoding='utf-8').read()
base  = open(os.path.join(sp,"base.css"), encoding='utf-8').read()
reuse = json.load(open(os.path.join(sp,"reuse_icons.json"), encoding='utf-8'))

EXTRA = '''
.two{flex:1;min-height:0;display:grid;grid-template-columns:1fr 1fr;gap:10mm}
.two>section{display:flex;flex-direction:column;min-height:0}
.sub{font-family:'Fredoka',sans-serif;font-weight:600;font-size:16pt;margin:0 0 3mm;color:var(--sea);
 border-bottom:.8mm solid var(--line);padding-bottom:1.5mm}
.qlist{flex:1;display:flex;flex-direction:column;justify-content:space-between}
.qrow .t{font-family:'Fredoka',sans-serif;font-weight:600;font-size:17pt;line-height:1.15}
.qrow .h{font-size:10.5pt;font-style:italic;color:var(--sea);margin:1mm 0 0 2mm}
.vrow{display:flex;align-items:flex-end;gap:4mm}
.vrow b{font-family:'Fredoka',sans-serif;font-weight:600;font-size:16pt}
.vrow .l{flex:1;border-bottom:.6mm dashed var(--line);height:10mm}
.callout{border:.8mm solid var(--sea);border-radius:2mm;padding:3mm 4mm;background:var(--paper-warm);
 font-family:'Fredoka',sans-serif;font-weight:600;font-size:13pt;text-align:center;line-height:1.3}
.yn{display:flex;gap:3mm}
.yn span{font-family:'Fredoka',sans-serif;font-weight:600;font-size:12pt;border:.7mm solid var(--line);
 border-radius:50%;width:14mm;height:8.5mm;display:flex;align-items:center;justify-content:center}
.yn .y{color:#2E8B57;border-color:#2E8B57} .yn .n{color:var(--stamp);border-color:var(--stamp)}
.ivr{display:flex;align-items:center;gap:4mm;border-bottom:.6mm dashed var(--line);padding-bottom:2mm}
.ivr .q{font-family:'Fredoka',sans-serif;font-weight:600;font-size:16pt;flex:1}
/* --- český pokyn pod zadáním --- */
.taskwrap{display:flex;flex-direction:column;align-items:flex-end;gap:1.2mm;max-width:138mm}
.czhint{font-size:11.5pt;font-weight:800;color:var(--ink);background:#FFF4DE;
 border:.7mm solid var(--sun);border-radius:1.5mm;padding:2mm 3.5mm;text-align:right;line-height:1.3}
.cz2{font-size:11pt;font-weight:700;color:var(--ink);background:#FFF4DE;border-left:1.6mm solid var(--sun);
 border-radius:1mm;padding:1.8mm 3mm;margin:0 0 3mm;line-height:1.35}
.cz2 b{color:var(--stamp)}
/* --- slovni zasoba --- */
.voctab{flex:1;min-height:0;display:grid;grid-template-columns:1fr 1fr;gap:6mm}
.voctab>div{display:flex;flex-direction:column;min-height:0}
.voctab h3{font-family:'Fredoka',sans-serif;font-weight:600;font-size:15pt;margin:0 0 2.5mm;color:var(--sea);
 border-bottom:.8mm solid var(--line);padding-bottom:1.5mm}
.voctab table{width:100%;border-collapse:collapse;flex:1}
.voctab td{padding:1.3mm 2mm;border-bottom:.4mm solid var(--line);vertical-align:middle}
.voctab tr:nth-child(odd) td{background:var(--paper-warm)}
.voctab .ven{font-family:'Fredoka',sans-serif;font-weight:600;font-size:13pt;width:38%}
.voctab .vph{font-family:'DejaVu Sans Mono',monospace;font-size:9pt;color:var(--sea);width:30%}
.voctab .vcz{font-size:12pt;font-weight:700;color:var(--ink)}
/* --- gramatické tabulky --- */
.gtab{width:100%;border-collapse:collapse;margin-bottom:4mm}
.gtab th{background:var(--ink);color:#fff;font-family:'Fredoka',sans-serif;font-weight:600;font-size:12pt;
 padding:2mm 3mm;text-align:left;letter-spacing:.06em}
.gtab td{border:.5mm solid var(--line);padding:2.5mm 3mm;font-family:'Fredoka',sans-serif;
 font-weight:600;font-size:15pt;background:#fff}
.gtab td.who{background:var(--paper-warm);width:30%}
.gtab td.gap{background:#FAFDFC}
.gtab td.gap::after{content:"";display:block;border-bottom:.6mm dashed var(--line);height:6mm}
/* --- věty s vlajkou --- */
.fsent{flex:1;min-height:0;display:flex;flex-direction:column;justify-content:space-between}
.fs{display:flex;align-items:center;gap:4mm;border-bottom:.6mm dashed var(--line);padding-bottom:2.5mm}
.fs .n{font-family:'Fredoka',sans-serif;font-weight:600;font-size:14pt;color:var(--stamp);width:6mm;flex:0 0 auto}
.fs .t{font-family:'Fredoka',sans-serif;font-weight:600;font-size:16pt;flex:1;line-height:1.2}
.fs .t u{text-decoration:none;border-bottom:.6mm dashed var(--line);padding:0 9mm}
.fs svg{width:21mm;height:21mm;flex:0 0 auto}
/* --- word race --- */
.race{flex:1;min-height:0;display:grid;grid-template-columns:repeat(5,1fr);grid-template-rows:repeat(4,1fr);gap:4mm}
.rcell{border:.6mm solid var(--line);border-radius:2mm;display:flex;align-items:center;justify-content:center;
 padding:2mm;text-align:center;font-family:'Fredoka',sans-serif;font-weight:600;font-size:15pt;line-height:1.1}
.score{flex:0 0 auto;display:flex;gap:5mm;margin-top:5mm}
.sbox{flex:1;border:.8mm solid var(--line);border-radius:2mm;padding:2.5mm 3mm;text-align:center;
 display:flex;flex-direction:column;gap:1.5mm}
.sbox .h{font-size:9.5pt;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#7A939B}
.sbox .l{border-bottom:.6mm solid var(--line);height:11mm}
.sbox.rec{border-color:var(--sun);background:var(--paper-warm)}
.sbox.rec .h{color:#C98A0E}
/* --- spojovačka --- */
.match{flex:1;min-height:0;display:grid;grid-template-columns:1fr 1fr;gap:4mm 14mm;align-content:space-between}
.mq,.ma{border:.6mm solid var(--line);border-radius:2mm;padding:2.5mm 3mm;display:flex;align-items:center;
 font-family:'Fredoka',sans-serif;font-weight:600;font-size:14.5pt;line-height:1.15}
.mq{border-left:1.6mm solid var(--sea)} .ma{border-left:1.6mm solid var(--sun);background:var(--paper-warm)}
/* --- mini test --- */
.mt{flex:1;min-height:0;display:grid;grid-template-columns:1fr 1fr;gap:3mm 12mm;align-content:space-between}
.mti{display:flex;align-items:center;gap:3mm;border-bottom:.6mm dashed var(--line);padding-bottom:2mm}
.mti .n{font-family:'Fredoka',sans-serif;font-weight:600;font-size:12pt;color:#fff;background:var(--sea);
 width:9mm;height:9mm;border-radius:50%;display:flex;align-items:center;justify-content:center;flex:0 0 auto}
.mti .t{font-family:'Fredoka',sans-serif;font-weight:600;font-size:14.5pt;flex:1;line-height:1.15}
.mti .t u{text-decoration:none;border-bottom:.6mm solid var(--line);padding:0 8mm}
/* --- check list --- */
.check{flex:1;min-height:0;display:flex;flex-direction:column}
.clist{flex:1;min-height:0;display:grid;grid-template-columns:1fr 1fr;grid-auto-rows:auto;
 align-content:space-between;gap:3mm 12mm}
.ci{display:flex;align-items:center;gap:4mm;border-bottom:.6mm dashed var(--line);padding-bottom:2.5mm}
.ci svg{width:15mm;height:15mm;flex:0 0 auto}
.ci .t b{font-family:'Fredoka',sans-serif;font-weight:600;font-size:15pt;display:block;line-height:1.15}
.ci .t i{font-size:10.5pt;color:#7A939B;font-style:italic;font-weight:600;display:block;margin-top:.8mm}
/* --- possessive 's + days --- */
.poss{flex:1;display:flex;flex-direction:column;justify-content:space-between}
.pr{display:flex;align-items:center;gap:4mm;border-bottom:.6mm dashed var(--line);padding-bottom:2.5mm}
.pr .cue{font-family:'Fredoka',sans-serif;font-weight:600;font-size:14pt;color:var(--stamp);
 width:52mm;flex:0 0 auto}
.pr .l{flex:1;border-bottom:.6mm solid var(--line);height:10mm}
.days{flex:1;display:flex;flex-direction:column;justify-content:space-between}
.day{display:flex;align-items:flex-end;gap:3mm}
.day b{font-family:'Fredoka',sans-serif;font-weight:600;font-size:17pt;width:8mm;flex:0 0 auto}
.day .l{flex:1;border-bottom:.6mm solid var(--line);height:10mm}
/* --- homework --- */
.hwtop{flex:1;min-height:0;display:grid;grid-template-columns:1.05fr 1fr .9fr;gap:9mm}
.hwtop>div{display:flex;flex-direction:column}
.hwtop h3{font-family:'Fredoka',sans-serif;font-weight:600;font-size:18pt;margin:0 0 3.5mm;color:var(--sea)}
.hwtop h3 .num{background:var(--sun);color:var(--ink);width:8mm;height:8mm;border-radius:50%;
 display:inline-flex;align-items:center;justify-content:center;font-size:11pt;font-weight:700;
 margin-right:2mm;font-family:'Nunito',sans-serif}
.vocab2{flex:1;display:flex;flex-direction:column;justify-content:space-between}
.vocab2 .r{display:flex;align-items:flex-end;gap:3mm}
.vocab2 .w{width:40mm}
.vocab2 .w b{font-family:'Fredoka',sans-serif;font-weight:600;font-size:14pt;display:block;line-height:1.05}
.vocab2 .w span{font-family:'DejaVu Sans Mono',monospace;font-size:8pt;color:var(--sea);display:block}
.vocab2 .l{flex:1;border-bottom:.6mm dashed var(--line);height:9mm}
.draw2{flex:1;min-height:0;border:.8mm dashed var(--line);border-radius:2mm;display:flex;
 align-items:flex-end;justify-content:center;padding:3mm;text-align:center}
.draw2 span{font-size:9.5pt;color:#7A939B;font-weight:700;letter-spacing:.06em;text-transform:uppercase;line-height:1.4}
'''

PLAN = [("1","Hello again","3 min"),("2","Verb BE","5 min"),("3","Words","3 min"),
        ("4","Word race","3 min"),("5","my / his / her","4 min"),("6","Questions","5 min"),
        ("7","Wh- questions","3 min"),("8","'s + days","4 min")]
TOT = 12

CAN_Q = ["Can you swim?","Can you cook?","Can you ride a bike?","Can you play the piano?"]
BE_POS = [("I","am","I'm"),("He / She / It","is","he's"),("We / You / They","are","we're")]
BE_NEG = [("I","am not","I'm not"),("He / She / It","is not","he isn't"),("We / You / They","are not","we aren't")]
FSENT = [("This is Rosa. She","from","f-it"),
         ("I","from","f-es"),
         ("We","from","f-jp"),
         ("This is Hans. He","from","f-hu"),
         ("They","from","f-cz")]
RACE = ["Británie","Spojené státy","Francie","Itálie","Španělsko",
        "Japonsko","Česká republika","Řecko","matka","otec",
        "sestra","bratr","babička","dědeček","rodiče",
        "děti","teta","strýc","bratranec","dcera"]
PRON = [("I","my"),("you","your"),("he","his"),("she","her"),("it","its"),("we","our"),("they","their")]
PSENT = ["This is my brother. <u></u> name's Joe.",
         "These are my parents. <u></u> names are Mary and Jack.",
         "I've got a dog. <u></u> name's Buddy.",
         "This is Millie. <u></u> dog is Mut.",
         "We're in Class 7. <u></u> teacher is Mr Brown.",
         "What's <u></u> name? I'm Rozárka."]
YNQ = ["Are you from the Czech Republic?","Is your mum a teacher?","Are your friends at school?",
       "Is your dog friendly?","Am I your teacher?","Are we on the computer?"]
WHQ = ["What's your name?","Where are you from?","How old are you?",
       "When is your birthday?","Who is your teacher?","Whose dog is it?"]
WHA = ["My name's Rozárka.","I'm from the Czech Republic.","I'm eleven.",
       "It's on 5th May.","Mrs Nováková.","It's my sister's."]
MT = ["I <u></u> from Brno.","She <u></u> from Spain. (NOT)","<u></u> you twelve?",
      "This is my brother. <u></u> name's Tom.","Where <u></u> you from?","<u></u> old are you?",
      "We <u></u> in the garden.","Is Paul your friend? No, he <u></u>.",
      "This is Millie. <u></u> dog is Mut.","<u></u> is your birthday?",
      "This is Mel. It's <u></u> pen. (Mel + 's)","After Monday it's <u></u>."]
HW_W = [("mother","MA-dr","matka"),("father","FÁ-dr","otec"),("parents","PE-rnts","rodiče"),
        ("children","ČIL-drn","děti"),("cousin","KA-zn","bratranec / sestřenice"),
        ("Whose?","húz","Čí?")]
CHECK = [("I can use am / is / are.","Umím použít am, is, are."),
         ("I can make short forms: I'm, he's, we're.","Umím krátké tvary."),
         ("I can make negatives: isn't, aren't.","Umím zápor."),
         ("I can ask: Are you…? Is he…?","Umím se zeptat."),
         ("I can answer: Yes, he is. / No, he isn't.","Umím krátce odpovědět."),
         ("I can use my, his, her, its, our, their.","Umím přivlastňovací zájmena."),
         ("I can ask Wh- questions: What? Where? How old?","Umím otázky s What, Where, How old."),
         ("I know 8 countries and 10 family words.","Znám země a slovíčka o rodině."),
         ("I can use 's: This is Mel's pen.","Umím přivlastňovací 's."),
         ("I know all seven days of the week.","Znám všech sedm dní v týdnu.")]

def sprite():
    p=['<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>']
    for k,v in list(reuse.items())+list(FLAGS.items()):
        p.append('<symbol id="%s" viewBox="0 0 100 100">%s</symbol>'%(k,v))
    p.append('</defs></svg>'); return "".join(p)

def foot(n,lbl):
    return ('<div class="foot"><span>English &middot; Unit 2 &middot; 6 October</span>'
            '<span>%s</span><span>%d / %d</span></div>'%(lbl,n,TOT))
def head(no,title,task,cz=""):
    czrow = '<div class="czhint">%s</div>'%cz if cz else ""
    return ('<div class="ph"><div class="grp"><span class="no">%s</span><h2>%s</h2></div>'
            '<div class="taskwrap"><span class="task">%s</span>%s</div></div>'%(no,title,task,czrow))

H=['<meta charset="utf-8">','<title>Unit 2 — test practice</title>','<style>',fonts,base,EXTRA,'</style>',sprite()]

# 1 cover
stars="".join('<svg><use href="#i-star"/></svg>' for _ in range(10))
plan="".join('<div><span class="n">%s</span><div class="t">%s</div><span class="m">%s</span></div>'%p for p in PLAN)
H.append(f'''<div class="page"><div class="airmail"></div><div class="cover">
<div><p class="kicker">English &middot; Lesson 3 &middot; 6 October &middot; Project 1, Unit 2</p>
<h1>Ready for<br>the <span>test!</span></h1>
<div class="namebox"><b>My name is</b><span class="l"></span></div>
<div class="starrow"><span class="lbl">My stars today</span>{stars}</div></div>
<div class="plan">{plan}</div></div>{foot(1,"Lesson 3")}</div>''')

# 2 warm-up + CAN
Q=[("How are you today?","I'm …"),("What day is it today?","It's Monday / Tuesday …"),
   ("What's the weather like?","It's …")]
qs="".join('<div class="qrow"><div class="t">%s</div><div class="h">%s</div><div class="wl short"></div></div>'%q for q in Q)
cans="".join('<div class="ivr"><span class="q">%s</span>'
             '<div class="yn"><span class="y">YES</span><span class="n">NO</span></div></div>'%q for q in CAN_Q)
H.append(f'''<div class="page"><div class="airmail"></div>
{head("1","Hello again!","We haven't seen each other for a while. Let's warm up!",
      "Vlevo odpovídej celou větou. Vpravo zakroužkuj YES/NO a odpověz: Yes, I can. / No, I can't.")}
<div class="two">
 <section><div class="sub">Talk to me</div><div class="cz2">Zeptej se jí na tyhle tři věci. Odpovídá <b>celou větou</b>, ne jedním slovem.</div><div class="qlist">{qs}</div></section>
 <section><div class="sub">Do you still remember CAN?</div><div class="cz2">Zakroužkuje YES nebo NO a řekne <b>Yes, I can.</b> / <b>No, I can't.</b></div>
  <div class="qlist">{cans}
   <div class="vrow"><b>I can</b><span class="l"></span><b>but I can't</b><span class="l"></span></div>
  </div></section>
</div>{foot(2,"Warm-up")}</div>''')

# 3 BE
def gtab(rows, head2, head3):
    t='<table class="gtab"><tr><th>who</th><th>%s</th><th>%s</th></tr>'%(head2,head3)
    for who,lon,sho in rows:
        t+='<tr><td class="who">%s</td><td>%s</td><td class="gap"></td></tr>'%(who,lon)
    return t+'</table>'
fs="".join('<div class="fs"><span class="n">%d</span><span class="t">%s <u></u> %s <u></u></span>'
           '<svg><use href="#%s"/></svg></div>'%(i,a,b,f) for i,(a,b,f) in enumerate(FSENT,1))
H.append(f'''<div class="page"><div class="airmail"></div>
{head("2","Verb BE","Fill in the table. Then complete the sentences &mdash; and say the country!",
      "Do tabulky doplň krátké tvary. Pak doplň věty a řekni, odkud kdo je.")}
<div class="two" style="grid-template-columns:1fr 1.15fr">
 <section><div class="cz2">Do prázdného sloupce doplní <b>krátký tvar</b>: am &rarr; ’m, is &rarr; ’s, are &rarr; ’re.</div>{gtab(BE_POS,"long form","short form")}{gtab(BE_NEG,"negative long","negative short")}</section>
 <section><div class="cz2">Doplní sloveso <b>a</b> zemi podle vlajky: <i>She’s from Italy.</i></div><div class="fsent">{fs}</div></section>
</div>{foot(3,"Grammar")}</div>''')


# 4 slovni zasoba
COUNTRIES=[("Britain","BRI-tn","Británie"),("the USA","ď jú-es-EJ","Spojené státy"),
 ("France","fráns","Francie"),("Italy","I-te-ly","Itálie"),("Spain","spejn","Španělsko"),
 ("Japan","dže-PEN","Japonsko"),("the Czech Republic","ď ček ri-PAB-lik","Česká republika"),
 ("Greece","grís","Řecko")]
FAMILY=[("mother","MA-dr","matka"),("father","FÁ-dr","otec"),("sister","SIS-tr","sestra"),
 ("brother","BRA-dr","bratr"),("grandmother","GREN-ma-dr","babička"),
 ("grandfather","GREN-fá-dr","dědeček"),("parents","PE-rnts","rodiče"),
 ("children","ČIL-drn","děti"),("aunt","ánt","teta"),("uncle","ANKL","strýc"),
 ("cousin","KAZN","bratranec / sestřenice"),("daughter","DÓ-tr","dcera")]
def vtab(rows):
    t="<table>"
    for en,ph,cz in rows:
        t+='<tr><td class="ven">%s</td><td class="vph">[%s]</td><td class="vcz">%s</td></tr>'%(en,ph,cz)
    return t+"</table>"
H.append(f'''<div class="page"><div class="airmail"></div>
{head("3","Words for the test","Read them out loud. The pronunciation is in brackets.",
      "Přečti každé slovo nahlas. V hranaté závorce je výslovnost.")}
<div class="voctab">
 <div><h3>Countries</h3><div class="cz2">Osm zemí. Čte nahlas podle závorky.</div>{vtab(COUNTRIES)}</div>
 <div><h3>Family</h3><div class="cz2">Dvanáct slov o rodině. Taky nahlas.</div>{vtab(FAMILY)}</div>
</div>{foot(4,"Vocabulary")}</div>''')

# 5 word race
rc="".join('<div class="rcell">%s</div>'%w for w in RACE)
H.append(f'''<div class="page"><div class="airmail"></div>
{head("4","Word race","Say every word in English. Ready? GO!",
      "Česky je napsané, ty říkáš anglicky. Minuta na kolo, tři kola.")}
<div class="cz2">Ukazuj po řadách, ona říká <b>anglicky</b>. Minuta, pak zapiš skóre dole. Tři kola.</div><div class="race">{rc}</div>
<div class="score">
 <div class="sbox"><span class="h">Round 1 &middot; 60 s</span><span class="l"></span></div>
 <div class="sbox"><span class="h">Round 2 &middot; 60 s</span><span class="l"></span></div>
 <div class="sbox"><span class="h">Round 3 &middot; 60 s</span><span class="l"></span></div>
 <div class="sbox rec"><span class="h">&#9733; My best score</span><span class="l"></span></div>
</div>{foot(5,"Speed game")}</div>''')

# 5 pronouns
pt='<table class="gtab"><tr><th>pronoun</th><th>possessive</th></tr>'
for a,b in PRON: pt+='<tr><td class="who">%s</td><td class="gap"></td></tr>'%a
pt+='</table>'
ps="".join('<div class="fs"><span class="n">%d</span><span class="t">%s</span></div>'%(i,s)
           for i,s in enumerate(PSENT,1))
H.append(f'''<div class="page"><div class="airmail"></div>
{head("5","my / your / his / her","Fill in the table. Then complete the sentences.",
      "Do tabulky doplň druhý sloupec. Pak do každé věty doplň chybějící zájmeno.")}
<div class="two" style="grid-template-columns:.75fr 1.25fr">
 <section><div class="cz2">Ke každému zájmenu doplní <b>přivlastňovací</b> tvar: I &rarr; my.</div>{pt}
  <div class="callout" style="font-size:12pt;line-height:1.45">
   This is my dog.<br><b style="color:#0F8B8D">Its</b> name is Mut.<br>
   <span style="font-size:10pt;color:#7A939B">but</span><br>
   <b style="color:#E4572E">It's</b> my dog. = It is</div></section>
 <section><div class="cz2">Do každé věty doplní <b>jedno slovo</b> z tabulky vlevo.</div><div class="fsent">{ps}</div></section>
</div>{foot(6,"Grammar")}</div>''')

# 6 questions
yn="".join('<div class="ivr"><span class="q">%s</span>'
           '<div class="yn"><span class="y">YES</span><span class="n">NO</span></div></div>'%q for q in YNQ)
H.append(f'''<div class="page"><div class="airmail"></div>
{head("6","Questions and short answers","Circle YES or NO. Then say the whole short answer out loud.",
      "Zakroužkuj YES nebo NO. Pak řekni CELOU odpověď: Yes, I am. / No, she isn't.")}
<div class="two" style="grid-template-columns:1.25fr .75fr">
 <section><div class="cz2">Zakroužkuje YES/NO a pak řekne <b>celou krátkou odpověď</b> nahlas.</div><div class="qlist">{yn}</div></section>
 <section class="side" style="justify-content:center;gap:5mm">
  <div class="callout" style="border-color:#2E8B57;color:#2E8B57">Yes, he <b>is</b>.<br>Yes, they <b>are</b>.</div>
  <div class="callout" style="border-color:var(--stamp);color:var(--stamp);text-decoration:line-through">
   Yes, he's. &nbsp; Yes, they're.</div>
  <div class="callout">No, he <b>isn't</b>.<br>No, they <b>aren't</b>.</div>
 </section>
</div>{foot(7,"Speaking")}</div>''')

# 7 wh-questions
# odpovědi schválně v jiném pořadí, jinak by nebylo co spojovat
SHUF=[2,5,0,4,1,3]
mm=""
for q,ai in zip(WHQ,SHUF):
    mm+='<div class="mq">%s</div><div class="ma">%s</div>'%(q,WHA[ai])
assert sorted(SHUF)==list(range(6)) and all(SHUF[i]!=i for i in range(6)), "každá odpověď musí být u jiné otázky"
H.append(f'''<div class="page"><div class="airmail"></div>
{head("7","Wh- questions","Draw a line: question &rarr; answer. Then answer about YOU.",
      "Spoj čarou otázku s odpovědí. Dole pak odpověz sama za sebe.")}
<div class="cz2">Spojí čarou otázku vlevo se správnou odpovědí vpravo. Odpovědi jsou <b>zpřeházené</b>.</div><div class="match">{mm}</div>
<div class="score" style="margin-top:4mm">
 <div class="sbox"><span class="h">What's your name?</span><span class="l"></span></div>
 <div class="sbox"><span class="h">How old are you?</span><span class="l"></span></div>
 <div class="sbox"><span class="h">When is your birthday?</span><span class="l"></span></div>
</div>{foot(8,"Speaking")}</div>''')


# 8 possessive 's + days of the week
CUES=[("Mel / pen","This is Mel's pen."),("Joe / watch",""),("Jack and Maya / dog",""),
      ("Lin / book",""),("Granddad and Grandma / house","")]
pr="".join('<div class="pr"><span class="cue">%s</span><span class="l"></span></div>'%c for c,_ in CUES)
dys="".join('<div class="day"><b>%s</b><span class="l"></span></div>'%d for d in ["M","T","W","T","F","S","S"])
H.append(f'''<div class="page"><div class="airmail"></div>
{head("8","Possessive 's and days","Whose is it? Write the sentence. Then write all seven days.",
      "Vlevo napiš celou větu: This is Mel's pen. Vpravo doplň dny v týdnu.")}
<div class="two">
 <section><div class="sub">Whose is it? &mdash; write sentences</div><div class="cz2">Z nápovědy vlevo napíše celou větu: <b>This is Mel's pen.</b></div>
  <div class="callout" style="margin-bottom:4mm;font-size:13pt">
   Mel <b style="color:#0F8B8D">+ 's</b> &rarr; This is <b style="color:#0F8B8D">Mel's</b> pen.</div>
  <div class="poss">{pr}</div></section>
 <section><div class="sub">Days of the week</div><div class="cz2">Doplní sedm dní v týdnu. První písmeno je napovězené.</div>
  <div class="days">{dys}
   <div class="vrow"><b>Today is</b><span class="l"></span></div>
   <div class="vrow"><b>My birthday is on</b><span class="l"></span></div>
  </div></section>
</div>{foot(9,"Grammar")}</div>''')

# 9 homework
voc="".join('<div class="r"><span class="w"><b>%s</b><span>[%s]</span></span><span class="l"></span></div>'%(e,p)
            for e,p,c in HW_W)
ST=["I'm from …","My mum is …","My best friend isn't …"]
sts="".join('<div class="starter">%s</div><div class="wl short"></div>'%s for s in ST)
H.append(f'''<div class="page"><div class="airmail"></div>
{head("9","Homework","See you next week &mdash; and good luck in the test!",
      "Domácí úkol: nauč se slovíčka, napiš tři věty, nakresli rodinu.")}
<div class="hwtop">
 <div><h3><span class="num">1</span>Learn these words</h3><div class="vocab2">{voc}</div></div>
 <div><h3><span class="num">2</span>Write 3 sentences</h3>{sts}</div>
 <div><h3><span class="num">3</span>Draw &amp; label</h3>
  <div class="draw2"><span>Draw your family &middot; write one sentence<br>with HIS, HER or THEIR</span></div></div>
</div>{foot(10,"Homework")}</div>''')

# 10 check list
chk="".join('<div class="ci"><svg><use href="#i-star"/></svg>'
            '<span class="t"><b>%s</b><i>%s</i></span></div>'%c for c in CHECK)
H.append(f'''<div class="page"><div class="airmail"></div>
{head("10","What I can do now","Colour a star for every YES! Be honest &mdash; it shows us what to practise.",
      "Vybarvi hvězdu u všeho, co umíš. Co nevybarvíš, na to se příště podíváme.")}
<div class="cz2">U všeho, co umí, vybarví hvězdu. <b>Ať je upřímná</b> &mdash; nevybarvené si vezmeme příště.</div><div class="check"><div class="clist">{chk}</div></div>
{foot(11,"Check")}</div>''')

# 11 mini test
mt="".join('<div class="mti"><span class="n">%d</span><span class="t">%s</span></div>'%(i,t)
           for i,t in enumerate(MT,1))
H.append(f'''<div class="page"><div class="airmail"></div>
{head("&#9733;","Mini test","Twelve questions, like in the Progress check. No help &mdash; try it alone!",
      "Dvanáct úkolů jako v testu ve škole. Zkus to sama, bez nápovědy.")}
<div class="cz2">Doplní jedno slovo na každou linku. <b>Sama, bez nápovědy</b> &mdash; ať víme, jak na tom je.</div><div class="mt">{mt}</div>
<div class="bye" style="margin-top:4mm">Good luck! You can do it!</div>
{foot(12,"Mini test")}</div>''')

out=os.path.join(sp,"list3.html")
open(out,"w",encoding='utf-8').write("\n".join(H))
assert "</style>" in open(out,encoding='utf-8').read(), "CHYBÍ </style>!"
print("list3.html hotov, stran:", TOT, "| </style> ok")
