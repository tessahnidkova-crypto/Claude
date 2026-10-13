# -*- coding: utf-8 -*-
import os, sys, json
sp = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, sp)
from flags import FLAGS
from icons_fam import FAM_ICONS
from icons4 import ICONS4

fonts = open(os.path.join(sp,"fonts_embed.css"), encoding='utf-8').read()
base  = open(os.path.join(sp,"base.css"), encoding='utf-8').read()
old   = json.load(open(os.path.join(sp,"icons_all.json"), encoding='utf-8'))
ICONS = {}; ICONS.update(old); ICONS.update(FLAGS); ICONS.update(FAM_ICONS); ICONS.update(ICONS4)

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
/* český pokyn */
.taskwrap{display:flex;flex-direction:column;align-items:flex-end;gap:1.2mm;max-width:138mm}
.czhint{font-size:11.5pt;font-weight:800;color:var(--ink);background:#FFF4DE;
 border:.7mm solid var(--sun);border-radius:1.5mm;padding:2mm 3.5mm;text-align:right;line-height:1.3}
.cz2{font-size:11pt;font-weight:700;color:var(--ink);background:#FFF4DE;border-left:1.6mm solid var(--sun);
 border-radius:1mm;padding:1.8mm 3mm;margin:0 0 3mm;line-height:1.35}
.cz2 b{color:var(--stamp)}
/* slovní zásoba */
.voctab{flex:1;min-height:0;display:grid;grid-template-columns:1fr 1fr;gap:6mm}
.voctab>div{display:flex;flex-direction:column;min-height:0}
.voctab h3{font-family:'Fredoka',sans-serif;font-weight:600;font-size:15pt;margin:0 0 2.5mm;color:var(--sea);
 border-bottom:.8mm solid var(--line);padding-bottom:1.5mm}
.voctab table{width:100%;border-collapse:collapse;flex:1}
.voctab td{padding:1.3mm 2mm;border-bottom:.4mm solid var(--line);vertical-align:middle}
.voctab tr:nth-child(odd) td{background:var(--paper-warm)}
.voctab .ven{font-family:'Fredoka',sans-serif;font-weight:600;font-size:13pt;width:36%}
.voctab .vph{font-family:'DejaVu Sans Mono',monospace;font-size:9pt;color:var(--sea);width:30%}
.voctab .vcz{font-size:12pt;font-weight:700;color:var(--ink)}
/* gramatické tabulky */
.gtab{width:100%;border-collapse:collapse;margin-bottom:4mm}
.gtab th{background:var(--ink);color:#fff;font-family:'Fredoka',sans-serif;font-weight:600;font-size:12pt;
 padding:2mm 3mm;text-align:left;letter-spacing:.06em}
.gtab td{border:.5mm solid var(--line);padding:2.5mm 3mm;font-family:'Fredoka',sans-serif;
 font-weight:600;font-size:15pt;background:#fff}
.gtab td.who{background:var(--paper-warm);width:34%}
.gtab td.gap{background:#FAFDFC}
.gtab td.gap::after{content:"";display:block;border-bottom:.6mm dashed var(--line);height:6mm}
/* zhustena strana */
.tight .gtab td{padding:1.6mm 3mm;font-size:13.5pt}
.tight .gtab th{padding:1.4mm 3mm;font-size:11pt}
.tight .gtab{margin-bottom:2.5mm}
.tight .gtab td.gap::after{height:5mm}
.tight .cz2{padding:1.4mm 3mm;margin-bottom:2mm;font-size:10.5pt}
.tight .fs{padding-bottom:1.8mm}
.tight .fs .t{font-size:15pt}
/* věty s ikonou */
.fsent{flex:1;min-height:0;display:flex;flex-direction:column;justify-content:space-between}
.fs{display:flex;align-items:center;gap:4mm;border-bottom:.6mm dashed var(--line);padding-bottom:2.5mm}
.fs .n{font-family:'Fredoka',sans-serif;font-weight:600;font-size:14pt;color:var(--stamp);width:6mm;flex:0 0 auto}
.fs .t{font-family:'Fredoka',sans-serif;font-weight:600;font-size:16pt;flex:1;line-height:1.2}
.fs .t u{text-decoration:none;border-bottom:.6mm dashed var(--line);padding:0 9mm}
.fs svg{width:19mm;height:19mm;flex:0 0 auto}
/* word race */
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
/* mini test */
.mt{flex:1;min-height:0;display:grid;grid-template-columns:1fr 1fr;gap:3mm 12mm;align-content:space-between}
.mti{display:flex;align-items:center;gap:3mm;border-bottom:.6mm dashed var(--line);padding-bottom:2mm}
.mti .n{font-family:'Fredoka',sans-serif;font-weight:600;font-size:12pt;color:#fff;background:var(--sea);
 width:9mm;height:9mm;border-radius:50%;display:flex;align-items:center;justify-content:center;flex:0 0 auto}
.mti .t{font-family:'Fredoka',sans-serif;font-weight:600;font-size:14.5pt;flex:1;line-height:1.15}
.mti .t u{text-decoration:none;border-bottom:.6mm solid var(--line);padding:0 8mm}
/* check list */
.check{flex:1;min-height:0;display:flex;flex-direction:column}
.clist{flex:1;min-height:0;display:grid;grid-template-columns:1fr 1fr;grid-auto-rows:auto;
 align-content:space-between;gap:3mm 12mm}
.ci{display:flex;align-items:center;gap:4mm;border-bottom:.6mm dashed var(--line);padding-bottom:2.5mm}
.ci svg{width:15mm;height:15mm;flex:0 0 auto}
.ci .t b{font-family:'Fredoka',sans-serif;font-weight:600;font-size:15pt;display:block;line-height:1.15}
.ci .t i{font-size:10.5pt;color:#7A939B;font-style:italic;font-weight:600;display:block;margin-top:.8mm}
/* rodokmen */
.treewrap{flex:1;min-height:0;display:flex;flex-direction:column}
.treewrap svg.big{width:100%;flex:1;min-height:0}
/* have got — obrázkové karty */
.cards{flex:1;min-height:0;display:grid;grid-template-columns:repeat(4,1fr);gap:4mm}
.card4{border:.6mm solid var(--line);border-radius:2mm;display:flex;flex-direction:column;
 align-items:center;justify-content:center;gap:1.5mm;padding:3mm 2mm;text-align:center}
.card4 svg{width:24mm;height:24mm}
.card4 b{font-family:'Fredoka',sans-serif;font-weight:600;font-size:14pt;line-height:1.05}
.card4 .tick2{display:flex;gap:3mm;margin-top:1mm}
.card4 .tick2 svg{width:11mm;height:11mm}
/* interview */
.ivw{flex:1;min-height:0;display:flex;flex-direction:column;justify-content:space-between}
.ivq{display:flex;align-items:center;gap:4mm;border-bottom:.6mm dashed var(--line);padding-bottom:2.5mm}
.ivq svg{width:15mm;height:15mm;flex:0 0 auto}
.ivq .q{font-family:'Fredoka',sans-serif;font-weight:600;font-size:15.5pt;flex:1;line-height:1.15}
.ivq .tick{display:flex;gap:2.5mm;flex:0 0 auto}
.ivq .tick svg{width:11mm;height:11mm}
/* psaní o sobě */
.wrt{flex:1;display:flex;flex-direction:column;justify-content:space-around}
.wrt>div{margin-bottom:2mm}
.wrt .st{font-family:'Fredoka',sans-serif;font-weight:600;font-size:16pt;margin-bottom:1.5mm}
.wrt .l{border-bottom:.6mm solid var(--line);height:11mm;margin-bottom:2mm}
/* homework */
.hwtop{flex:1;min-height:0;display:grid;grid-template-columns:1.05fr 1fr .9fr;gap:9mm}
.hwtop>div{display:flex;flex-direction:column}
.hwtop h3{font-family:'Fredoka',sans-serif;font-weight:600;font-size:18pt;margin:0 0 3.5mm;color:var(--sea)}
.hwtop h3 .num{background:var(--sun);color:var(--ink);width:8mm;height:8mm;border-radius:50%;
 display:inline-flex;align-items:center;justify-content:center;font-size:11pt;font-weight:700;
 margin-right:2mm;font-family:'Nunito',sans-serif}
.vocab2{flex:1;display:flex;flex-direction:column;justify-content:space-between}
.vocab2 .r{display:flex;align-items:flex-end;gap:3mm}
.vocab2 .w{width:44mm}
.vocab2 .w b{font-family:'Fredoka',sans-serif;font-weight:600;font-size:14pt;display:block;line-height:1.05}
.vocab2 .w span{font-family:'DejaVu Sans Mono',monospace;font-size:8pt;color:var(--sea);display:block}
.vocab2 .l{flex:1;border-bottom:.6mm dashed var(--line);height:9mm}
.draw2{flex:1;min-height:0;border:.8mm dashed var(--line);border-radius:2mm;display:flex;
 align-items:flex-end;justify-content:center;padding:3mm;text-align:center}
.draw2 span{font-size:9.5pt;color:#7A939B;font-weight:700;letter-spacing:.06em;text-transform:uppercase;line-height:1.4}
'''

TOT = 12
PLAN = [("1","Hello again","3 min"),("2","My cousin","4 min"),("3","Words","3 min"),
        ("4","Word race","3 min"),("5","HAVE GOT","5 min"),("6","Sentences","4 min"),
        ("7","Have you got…?","5 min"),("8","About me","3 min")]

def sprite():
    p=['<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>']
    for k,v in ICONS.items():
        p.append('<symbol id="%s" viewBox="0 0 100 100">%s</symbol>'%(k,v))
    p.append('</defs></svg>'); return "".join(p)

def foot(n,lbl):
    return ('<div class="foot"><span>English &middot; Lesson 4 &middot; 13 October</span>'
            '<span>%s</span><span>%d / %d</span></div>'%(lbl,n,TOT))
def head(no,title,task,cz=""):
    czrow = '<div class="czhint">%s</div>'%cz if cz else ""
    return ('<div class="ph"><div class="grp"><span class="no">%s</span><h2>%s</h2></div>'
            '<div class="taskwrap"><span class="task">%s</span>%s</div></div>'%(no,title,task,czrow))

H=['<meta charset="utf-8">','<title>Lesson 4 — Have you got a pet?</title>','<style>',
   fonts, base, EXTRA,'</style>', sprite()]

# ======================= 1 — titulka =======================
stars="".join('<svg><use href="#i-star"/></svg>' for _ in range(10))
plan="".join('<div><span class="n">%s</span><div class="t">%s</div><span class="m">%s</span></div>'%p for p in PLAN)
H.append(f'''<div class="page"><div class="airmail"></div><div class="cover">
<div><p class="kicker">English &middot; Lesson 4 &middot; 13 October</p>
<h1>Have you got<br>a <span>pet?</span></h1>
<div class="namebox"><b>My name is</b><span class="l"></span></div>
<div class="starrow"><span class="lbl">My stars today</span>{stars}</div></div>
<div class="plan">{plan}</div></div>{foot(1,"Lesson 4")}</div>''')

# ======================= 2 — rozmluvení =======================
Q=[("How are you today?","I'm …"),("What day is it today?","It's Tuesday."),
   ("How was the test?","It was easy / OK / difficult.")]
qs="".join('<div class="qrow"><div class="t">%s</div><div class="h">%s</div><div class="wl short"></div></div>'%q for q in Q)
BE=["I <u></u> from the Czech Republic.","My mum <u></u> a teacher.",
    "My friends <u></u> at school.","<u></u> you eleven?"]
bs="".join('<div class="fs"><span class="n">%d</span><span class="t">%s</span></div>'%(i,s)
           for i,s in enumerate(BE,1))
H.append(f'''<div class="page"><div class="airmail"></div>
{head("1","Hello again!","Let's warm up. Then a quick check: am, is or are?",
      "Vlevo odpovídej celou větou. Vpravo doplň am / is / are.")}
<div class="two">
 <section><div class="sub">Talk to me</div>
  <div class="cz2">Zeptej se jí na tři věci. Odpovídá <b>celou větou</b>. U testu se neptej na známku, jen jaké to bylo.</div>
  <div class="qlist">{qs}</div></section>
 <section><div class="sub">Quick check: am / is / are</div>
  <div class="cz2">Rychlé opakování z minula. Doplní <b>jedno slovo</b>, nahlas.</div>
  <div class="fsent">{bs}
   <div class="callout" style="font-size:12pt">I <b>am</b> &nbsp;&middot;&nbsp; he / she / it <b>is</b> &nbsp;&middot;&nbsp; we / you / they <b>are</b></div>
  </div></section>
</div>{foot(2,"Warm-up")}</div>''')

# ======================= 3 — rodokmen / COUSIN =======================
TREE = '''<svg class="big" viewBox="0 0 560 300" preserveAspectRatio="xMidYMid meet">
<style>
 .bx{fill:#fff;stroke:#16323B;stroke-width:3}
 .bxs{fill:#F2F8F6;stroke:#0F8B8D;stroke-width:3}
 .bxh{fill:#FFF6F3;stroke:#E4572E;stroke-width:5}
 .en{font-family:Fredoka,sans-serif;font-weight:600;font-size:20px;fill:#16323B;text-anchor:middle}
 .cz{font-family:Nunito,sans-serif;font-weight:700;font-size:13px;fill:#7A939B;text-anchor:middle}
 .enh{font-family:Fredoka,sans-serif;font-weight:600;font-size:22px;fill:#E4572E;text-anchor:middle}
 .czh{font-family:Nunito,sans-serif;font-weight:800;font-size:13px;fill:#E4572E;text-anchor:middle}
 .ln{stroke:#16323B;stroke-width:3;fill:none}
</style>
<rect class="bx" x="168" y="6" width="224" height="52" rx="9"/>
<text class="en" x="280" y="29">Grandma + Granddad</text>
<text class="cz" x="280" y="47">babička a dědeček</text>
<path class="ln" d="M280 58 V82 M110 82 H450 M110 82 V116 M450 82 V116"/>
<rect class="bxs" x="35" y="116" width="150" height="52" rx="9"/>
<text class="en" x="110" y="139">my mum</text>
<text class="cz" x="110" y="157">moje máma</text>
<rect class="bxs" x="375" y="116" width="150" height="52" rx="9"/>
<text class="en" x="450" y="139">my aunt</text>
<text class="cz" x="450" y="157">moje teta</text>
<path class="ln" d="M185 142 H375" stroke-dasharray="7 6"/>
<rect x="245" y="130" width="70" height="22" rx="5" fill="#fff"/>
<text class="cz" x="280" y="146">sestry</text>
<path class="ln" d="M110 168 V218 M450 168 V218"/>
<rect class="bx" x="35" y="218" width="150" height="52" rx="9"/>
<text class="en" x="110" y="241">ME</text>
<text class="cz" x="110" y="259">já</text>
<rect class="bxh" x="368" y="212" width="164" height="64" rx="9"/>
<text class="enh" x="450" y="235">my COUSIN</text>
<text class="czh" x="450" y="253">můj bratranec /</text>
<text class="czh" x="450" y="268">moje sestřenice</text>
<path class="ln" d="M185 244 H360" stroke="#E4572E" stroke-dasharray="7 6"/>
<polygon points="368,244 356,238 356,250" fill="#E4572E"/>
<rect x="226" y="232" width="92" height="22" rx="5" fill="#fff"/>
<text class="cz" x="272" y="248" fill="#E4572E">dítě tvojí tety</text>
</svg>'''
FAMQ = ["My mum's sister is my <u></u>.","My aunt's son is my <u></u>.",
        "My dad's brother is my <u></u>.","Grandma and Granddad are my <u></u>."]
fq="".join('<div class="fs"><span class="n">%d</span><span class="t">%s</span></div>'%(i,s)
           for i,s in enumerate(FAMQ,1))
H.append(f'''<div class="page"><div class="airmail"></div>
{head("2","Who is a cousin?","Look at the family tree. Then finish the sentences.",
      "Podívej se na rodokmen a doplň věty. Všechno, co potřebuješ, je na obrázku.")}
<div class="two" style="grid-template-columns:1.15fr .85fr">
 <section><div class="sub">Family tree</div>
  <div class="cz2">Sestra tvojí mámy = <b>my aunt</b>. Její dítě = <b>my cousin</b> &mdash; jedno slovo pro kluka i holku.</div>
  <div class="treewrap">{TREE}</div></section>
 <section><div class="sub">Finish the sentences</div>
  <div class="cz2">Jedno slovo na každou linku. Pozor na psaní: <b>cousin</b> se čte [KA-zn], ne „kousin“.</div>
  <div class="fsent">{fq}
   <div class="callout" style="border-color:var(--stamp);color:var(--stamp);font-size:15pt">
    c<span style="border-bottom:1.2mm solid var(--stamp)">ou</span>sin &nbsp;=&nbsp; [ KA - zn ]</div>
  </div></section>
</div>{foot(3,"Family")}</div>''')

# ======================= 4 — slovní zásoba =======================
FAMILY=[("cousin","KA-zn","bratranec / sestřenice"),("aunt","ánt","teta"),
 ("uncle","ANKL","strýc"),("son","san","syn"),("daughter","DÓ-tr","dcera"),
 ("grandparents","GREN-pe-rnts","prarodiče"),("brother","BRA-dr","bratr"),
 ("sister","SIS-tr","sestra"),("Hungary","HAN-ge-ry","Maďarsko")]
THINGS=[("a pet","e pet","domácí mazlíček"),("a dog","e dog","pes"),("a cat","e ket","kočka"),
 ("a mobile","e MOU-bajl","mobil"),("a watch","e woč","hodinky"),("a book","e buk","kniha"),
 ("an umbrella","en am-BRE-la","deštník"),("a house","e haus","dům"),("a bike","e bajk","kolo")]
def vtab(rows):
    t="<table>"
    for en,ph,cz in rows:
        t+='<tr><td class="ven">%s</td><td class="vph">[%s]</td><td class="vcz">%s</td></tr>'%(en,ph,cz)
    return t+"</table>"
H.append(f'''<div class="page"><div class="airmail"></div>
{head("3","Words for today","Read them out loud. The pronunciation is in brackets.",
      "Přečti každé slovo nahlas. V hranaté závorce je výslovnost.")}
<div class="voctab">
 <div><h3>Family &mdash; rodina</h3><div class="cz2">Opakování z minula + <b>Hungary</b>, které minule chybělo.</div>{vtab(FAMILY)}</div>
 <div><h3>Things &mdash; věci</h3><div class="cz2">Nová slova. Před každým je <b>a</b> / <b>an</b> &mdash; „jeden, jedna“.</div>{vtab(THINGS)}</div>
</div>{foot(4,"Vocabulary")}</div>''')

# ======================= 5 — word race =======================
RACE = ["bratranec","teta","strýc","syn","dcera",
        "prarodiče","bratr","sestra","Maďarsko","Itálie",
        "pes","kočka","mobil","hodinky","kniha",
        "deštník","dům","kolo","domácí mazlíček","Španělsko"]
rc="".join('<div class="rcell">%s</div>'%w for w in RACE)
H.append(f'''<div class="page"><div class="airmail"></div>
{head("4","Word race","Say every word in English. Ready? GO!",
      "Česky je napsané, ty říkáš anglicky. Minuta na kolo, tři kola.")}
<div class="cz2">Ukazuj po řadách, ona říká <b>anglicky</b>. U věcí stačí slovo bez <i>a</i>. Minuta, pak zapiš skóre. Tři kola.</div>
<div class="race">{rc}</div>
<div class="score">
 <div class="sbox"><span class="h">Round 1 &middot; 60 s</span><span class="l"></span></div>
 <div class="sbox"><span class="h">Round 2 &middot; 60 s</span><span class="l"></span></div>
 <div class="sbox"><span class="h">Round 3 &middot; 60 s</span><span class="l"></span></div>
 <div class="sbox rec"><span class="h">&#9733; My best score</span><span class="l"></span></div>
</div>{foot(5,"Speed game")}</div>''')

# ======================= 6 — HAVE GOT tabulka =======================
HG_POS=[("I / you / we / they","have got"),("he / she / it","has got")]
HG_NEG=[("I / you / we / they","haven't got"),("he / she / it","hasn't got")]
HG_EX=["I <u></u> got two brothers.","He <u></u> got a new bike.",
       "We <u></u> got a cat. (NOT)","My sister <u></u> got a mobile. (NOT)"]
def gtab(rows, h2, h3):
    t='<table class="gtab"><tr><th>who</th><th>%s</th><th>%s</th></tr>'%(h2,h3)
    for who,lon in rows:
        t+='<tr><td class="who">%s</td><td>%s</td><td class="gap"></td></tr>'%(who,lon)
    return t+'</table>'
hgs="".join('<div class="fs"><span class="n">%d</span><span class="t">%s</span></div>'%(i,t)
            for i,t in enumerate(HG_EX,1))
H.append(f'''<div class="page"><div class="airmail"></div>
{head("5","HAVE GOT &mdash; mít","Fill in the short forms. Then read the warning box!",
      "Do prázdného sloupce doplň krátký tvar. Pak si přečti červený rámeček — to je nejdůležitější.")}
<div class="two tight" style="grid-template-columns:1.1fr .9fr">
 <section>
  <div class="cz2">Krátký tvar: <b>have got &rarr; ’ve got</b>, <b>has got &rarr; ’s got</b>. Zápor se nezkracuje dál.</div>
  {gtab(HG_POS,"dlouhý tvar","krátký tvar")}{gtab(HG_NEG,"zápor dlouhý","zápor krátký")}
  <div class="sub" style="font-size:14pt;margin-top:1mm">Now you &mdash; have, has, haven't or hasn't?</div>
  <div class="cz2">Doplní <b>jedno slovo</b>. U vět s <b>(NOT)</b> musí být zápor.</div>
  <div class="fsent">{hgs}</div>
 </section>
 <section class="side" style="justify-content:center;gap:5mm">
  <div class="callout" style="font-size:12.5pt;line-height:1.5">
   <b style="color:#0F8B8D">I've got</b> a dog. = Mám psa.<br>
   <span style="font-size:10pt;color:#7A939B">[ajv got e dog]</span></div>
  <div class="callout" style="border-color:var(--stamp);font-size:12pt;line-height:1.5">
   <b style="color:#E4572E">POZOR!</b><br>
   <b>He’s</b> from Italy. = He <b>is</b><br>
   <b>He’s</b> got a cat. = He <b>has</b><br>
   <span style="font-size:10pt;color:#7A939B">Stejné ’s, dvě různá slovesa.<br>Pozná se podle toho, jestli za ním je <b>got</b>.</span></div>
 </section>
</div>{foot(6,"Grammar")}</div>''')

# ======================= 7 — věty podle obrázků =======================
CARDS=[("i-dog","a dog"),("i-cat","a cat"),("i-mobile","a mobile"),("i-watch","a watch"),
       ("i-book","a book"),("i-umbrella","an umbrella"),("i-house","a house"),("i-bike","a bike")]
cds="".join('<div class="card4"><svg><use href="#%s"/></svg><b>%s</b>'
            '<span class="tick2"><svg><use href="#i-yes"/></svg><svg><use href="#i-no"/></svg></span></div>'%(i,n)
            for i,n in CARDS)
H.append(f'''<div class="page"><div class="airmail"></div>
{head("6","I've got / I haven't got","Circle &#10003; or &#10007;. Say the sentence. Then write THREE of them.",
      "U každého obrázku zakroužkuj fajfku nebo křížek a řekni větu nahlas. Tři z nich pak napiš.")}
<div class="two" style="grid-template-columns:1.45fr .55fr">
 <section><div class="cz2">Zakroužkuje podle <b>pravdy o sobě</b> a hned řekne celou větu:
  <b>I've got a dog.</b> / <b>I haven't got a dog.</b> Po každé se zeptej <i>Really?</i> [RY-ly].</div>
  <div class="cards">{cds}</div></section>
 <section><div class="sub">Write three</div>
  <div class="cz2">Jen <b>tři</b> věty &mdash; ty zbylé stačí říct nahlas.</div>
  <div class="wrt">
   <div><div class="st" style="font-size:13pt;color:#7A939B">1</div><div class="l"></div></div>
   <div><div class="st" style="font-size:13pt;color:#7A939B">2</div><div class="l"></div></div>
   <div><div class="st" style="font-size:13pt;color:#7A939B">3</div><div class="l"></div></div>
  </div></section>
</div>
{foot(7,"Speaking + writing")}</div>''')

# ======================= 8 — Have you got…? =======================
IVQ=[("i-dog","Have you got a dog?"),("i-sibling","Have you got a brother or a sister?"),
     ("i-mobile","Have you got a mobile?"),("i-book","Have you got a favourite book?"),
     ("i-cat","Has your friend got a cat?"),("i-house","Has your family got a big house?")]
iv="".join('<div class="ivq"><svg><use href="#%s"/></svg><span class="q">%s</span>'
           '<span class="tick"><svg><use href="#i-yes"/></svg><svg><use href="#i-no"/></svg></span></div>'%q
           for q in IVQ)
H.append(f'''<div class="page"><div class="airmail"></div>
{head("7","Have you got &hellip;?","Circle &#10003; or &#10007;. Then say the WHOLE short answer out loud.",
      "Zakroužkuj fajfku nebo křížek. Pak řekni CELOU krátkou odpověď nahlas.")}
<div class="two" style="grid-template-columns:1.3fr .7fr">
 <section><div class="cz2">Zakroužkuje a pak <b>řekne celou odpověď</b>. Poslední dvě otázky jsou o někom jiném &mdash; tam se mění <b>has</b>.</div>
  <div class="ivw">{iv}</div></section>
 <section class="side" style="justify-content:center;gap:4mm">
  <div class="callout" style="border-color:#2E8B57;color:#2E8B57;font-size:12.5pt;line-height:1.5">
   Yes, I <b>have</b>.<br>No, I <b>haven't</b>.<br>
   <span style="font-size:9.5pt;color:#7A939B">[jes aj hev] &middot; [nou aj HE-vnt]</span></div>
  <div class="callout" style="border-color:#2E8B57;color:#2E8B57;font-size:12.5pt;line-height:1.5">
   Yes, he <b>has</b>.<br>No, she <b>hasn't</b>.<br>
   <span style="font-size:9.5pt;color:#7A939B">[jes hí hez] &middot; [nou ší HE-znt]</span></div>
  <div class="callout" style="border-color:var(--stamp);color:var(--stamp);text-decoration:line-through;font-size:12pt">
   Yes, I've. &nbsp; Yes, he's.</div>
 </section>
</div>{foot(8,"Speaking")}</div>''')

# ======================= 9 — About me =======================
ST=["I've got …","I haven't got …","My cousin's name is …","My best friend has got …"]
sts="".join('<div><div class="st">%s</div><div class="l"></div></div>'%s for s in ST)
H.append(f'''<div class="page"><div class="airmail"></div>
{head("8","About me","Finish the four sentences. Write the truth!",
      "Dokonči čtyři věty. Piš pravdu o sobě, ne opsanou větu.")}
<div class="two" style="grid-template-columns:1.25fr .75fr">
 <section><div class="cz2">Čtyři věty <b>o sobě</b>. Poslední je o kamarádovi &mdash; tam musí být <b>has got</b>, ne <i>have got</i>.</div>
  <div class="wrt">{sts}</div></section>
 <section class="side" style="justify-content:center;gap:5mm">
  <div class="callout" style="font-size:12pt;line-height:1.5">
   <b>I</b> / you / we / they &rarr; <b style="color:#0F8B8D">have got</b><br>
   <b>he</b> / <b>she</b> / it &rarr; <b style="color:#E4572E">has got</b></div>
  <div class="callout" style="font-size:11.5pt;line-height:1.45;border-color:var(--sun)">
   Můj kamarád = <b>he</b> nebo <b>she</b><br>&rarr; proto <b style="color:#E4572E">has got</b></div>
 </section>
</div>{foot(9,"Writing")}</div>''')

# ======================= 10 — domácí úkol =======================
HW_W=[("a pet","e pet","domácí mazlíček"),("a mobile","e MOU-bajl","mobil"),
      ("an umbrella","en am-BRE-la","deštník"),("a watch","e woč","hodinky"),
      ("cousin","KA-zn","bratranec / sestřenice"),("Hungary","HAN-ge-ry","Maďarsko")]
voc="".join('<div class="r"><span class="w"><b>%s</b><span>[%s]</span></span><span class="l"></span></div>'%(e,p)
            for e,p,c in HW_W)
ST2=["I've got …","My mum has got …","I haven't got …"]
sts2="".join('<div class="starter">%s</div><div class="wl short"></div>'%s for s in ST2)
H.append(f'''<div class="page"><div class="airmail"></div>
{head("9","Homework","See you next week!",
      "Domácí úkol: nauč se slovíčka, napiš tři věty, nakresli svůj pokoj.")}
<div class="hwtop">
 <div><h3><span class="num">1</span>Learn these words</h3><div class="vocab2">{voc}</div></div>
 <div><h3><span class="num">2</span>Write 3 sentences</h3>{sts2}</div>
 <div><h3><span class="num">3</span>Draw &amp; label</h3>
  <div class="draw2"><span>Draw your room &middot; write one sentence<br>with I'VE GOT</span></div></div>
</div>{foot(10,"Homework")}</div>''')

# ======================= 11 — check list =======================
CHECK=[("I can use have got / has got.","Umím have got a has got."),
       ("I know when it's HAS and when it's HAVE.","Vím, kdy je has a kdy have."),
       ("I can make negatives: haven't got, hasn't got.","Umím zápor."),
       ("I can ask: Have you got…? Has he got…?","Umím se zeptat."),
       ("I can answer: Yes, I have. / No, I haven't.","Umím krátce odpovědět."),
       ("I know what a COUSIN is.","Vím, co je cousin, a umím to vyslovit."),
       ("I know aunt, uncle, son, daughter, grandparents.","Znám slova o rodině."),
       ("I know 9 things: pet, dog, cat, mobile…","Znám devět věcí."),
       ("I know: He's from Italy ≠ He's got a cat.","Rozeznám ’s = is od ’s = has."),
       ("I can still use am / is / are.","Pořád umím sloveso být.")]
chk="".join('<div class="ci"><svg><use href="#i-star"/></svg>'
            '<span class="t"><b>%s</b><i>%s</i></span></div>'%c for c in CHECK)
H.append(f'''<div class="page"><div class="airmail"></div>
{head("10","What I can do now","Colour a star for every YES! Be honest — it shows us what to practise.",
      "Vybarvi hvězdu u všeho, co umíš. Co nevybarvíš, na to se příště podíváme.")}
<div class="cz2">U všeho, co umí, vybarví hvězdu. <b>Ať je upřímná</b> &mdash; nevybarvené si vezmeme příště.</div>
<div class="check"><div class="clist">{chk}</div></div>{foot(11,"Check")}</div>''')

# ======================= 12 — mini test =======================
MT=["I <u></u> got a dog.","She <u></u> got a cat.","<u></u> you got a mobile?",
    "Has he got a bike? Yes, he <u></u>.","I <u></u> got a horse. (NOT)",
    "My mum <u></u> got a watch. (NOT)","My aunt's son is my <u></u>.",
    "Grandma and Granddad are my <u></u>.","Hans is from <u></u>. (Maďarsko)",
    "He's <u></u> a cat. (má)","<u></u> your friend got a dog?","Have you got a sister? No, I <u></u>."]
mt="".join('<div class="mti"><span class="n">%d</span><span class="t">%s</span></div>'%(i,t)
           for i,t in enumerate(MT,1))
H.append(f'''<div class="page"><div class="airmail"></div>
{head("&#9733;","Mini test","Twelve questions. No help — try it alone!",
      "Dvanáct úkolů. Zkus to sama, bez nápovědy.")}
<div class="cz2">Doplní jedno slovo na každou linku. <b>Sama, bez nápovědy</b> &mdash; ať víme, jak na tom je.</div>
<div class="mt">{mt}</div>
<div class="bye" style="margin-top:4mm">Great job today! See you next week!</div>
{foot(12,"Mini test")}</div>''')

out=os.path.join(sp,"list4.html")
open(out,"w",encoding='utf-8').write("\n".join(H))
txt=open(out,encoding='utf-8').read()
assert "</style>" in txt, "CHYBÍ </style>!"
assert txt.count('class="page"')==TOT, "stran je %d, ceka se %d"%(txt.count('class="page"'),TOT)
print("list4.html hotov | stran:",TOT,"| </style> ok")
