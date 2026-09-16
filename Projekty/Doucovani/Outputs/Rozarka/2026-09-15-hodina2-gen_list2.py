# -*- coding: utf-8 -*-
import os, sys, json
sp = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, sp)
from icons2 import NEW

fonts = open(os.path.join(sp,"fonts_embed.css"), encoding='utf-8').read()
base  = open(os.path.join(sp,"base.css"), encoding='utf-8').read()
reuse = json.load(open(os.path.join(sp,"reuse_icons.json"), encoding='utf-8'))

EXTRA = '''
/* --- hodina 2 --- */
.two{flex:1;min-height:0;display:grid;grid-template-columns:1fr 1fr;gap:10mm}
.two>section{display:flex;flex-direction:column;min-height:0}
.sub{font-family:'Fredoka',sans-serif;font-weight:600;font-size:17pt;margin:0 0 3mm;color:var(--sea);
 border-bottom:.8mm solid var(--line);padding-bottom:1.5mm}
.qlist{flex:1;display:flex;flex-direction:column;justify-content:space-between}
.qrow .t{font-family:'Fredoka',sans-serif;font-weight:600;font-size:18pt;line-height:1.15}
.qrow .h{font-size:11pt;font-style:italic;color:var(--sea);margin:1mm 0 0 2mm}
.vrow{display:flex;align-items:flex-end;gap:4mm}
.vrow b{font-family:'Fredoka',sans-serif;font-weight:600;font-size:17pt;width:52mm}
.vrow .l{flex:1;border-bottom:.6mm dashed var(--line);height:11mm}
.callout{border:.8mm solid var(--sea);border-radius:2mm;padding:3mm 4mm;background:var(--paper-warm);
 font-family:'Fredoka',sans-serif;font-weight:600;font-size:14pt;text-align:center;line-height:1.3}
.cans{flex:1;min-height:0;display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:repeat(2,1fr);gap:5mm}
.canc{border:.6mm solid var(--line);border-radius:2mm;padding:3mm;display:flex;flex-direction:column;
 align-items:center;justify-content:center;gap:2mm}
.canc svg{width:19mm;height:19mm}
.canc .w{font-family:'Fredoka',sans-serif;font-weight:600;font-size:14pt;text-align:center;line-height:1.1}
.yn{display:flex;gap:4mm;margin-top:1mm}
.yn span{font-family:'Fredoka',sans-serif;font-weight:600;font-size:13pt;border:.7mm solid var(--line);
 border-radius:50%;width:15mm;height:9mm;display:flex;align-items:center;justify-content:center}
.yn .y{color:#2E8B57;border-color:#2E8B57}
.yn .n{color:var(--stamp);border-color:var(--stamp)}
.iv{flex:1;display:flex;flex-direction:column;justify-content:space-between}
.ivr{display:flex;align-items:center;gap:5mm;border-bottom:.6mm dashed var(--line);padding-bottom:2mm}
.ivr .q{font-family:'Fredoka',sans-serif;font-weight:600;font-size:17pt;flex:1}
.ivr .yn{margin:0}
.rule{display:flex;gap:6mm;justify-content:center;align-items:center;background:var(--paper-warm);
 border:.8mm solid var(--line);border-radius:2mm;padding:3mm 4mm;margin-top:4mm}
.rule div{font-family:'Fredoka',sans-serif;font-weight:600;font-size:15pt}
.rule .ok{color:#2E8B57} .rule .bad{color:var(--stamp);text-decoration:line-through}
.sgrid{flex:1;min-height:0;display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:repeat(3,1fr);gap:4mm}
.scell{border:.6mm solid var(--line);border-radius:2mm;display:flex;flex-direction:column;
 align-items:center;justify-content:center;gap:1mm;padding:2mm}
.scell svg{width:15mm;height:15mm}
.scell span{font-family:'Fredoka',sans-serif;font-weight:600;font-size:11.5pt;text-align:center;line-height:1.1}
.side{display:flex;flex-direction:column;gap:4mm;justify-content:center}
.dots{display:flex;flex-wrap:wrap;gap:3mm}
.dots i{width:9mm;height:9mm;border:.7mm solid var(--line);border-radius:50%;display:block}
.lbl{font-size:9.5pt;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#7A939B}
/* --- word race --- */
.race{flex:1;min-height:0;display:grid;grid-template-columns:repeat(5,1fr);grid-template-rows:repeat(4,1fr);gap:4mm}
.rcell{border:.6mm solid var(--line);border-radius:2mm;display:flex;align-items:center;justify-content:center;padding:2mm}
.rcell svg{width:23mm;height:23mm}
.score{flex:0 0 auto;display:flex;gap:5mm;margin-top:5mm;align-items:stretch}
.sbox{flex:1;border:.8mm solid var(--line);border-radius:2mm;padding:2.5mm 3mm;text-align:center;
 display:flex;flex-direction:column;gap:1.5mm}
.sbox .h{font-size:9.5pt;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#7A939B}
.sbox .l{border-bottom:.6mm solid var(--line);height:12mm}
.sbox.rec{border-color:var(--sun);background:var(--paper-warm)}
.sbox.rec .h{color:#C98A0E}
/* --- bonus --- */
.ttt{display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(3,1fr);gap:2.5mm;flex:1;min-height:0}
.ttt div{border:.7mm solid var(--line);border-radius:1.5mm;display:flex;align-items:center;justify-content:center;
 font-family:'Fredoka',sans-serif;font-weight:600;font-size:14pt;text-align:center;line-height:1.1;padding:2mm}
.tttwrap{display:flex;flex-direction:column;min-height:0;flex:1;gap:2.5mm}
.tttwrap .cap{font-size:9.5pt;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#7A939B;text-align:center}
.quick{flex:1;display:flex;flex-direction:column;justify-content:space-between}
.qk{display:flex;align-items:center;gap:3.5mm;border-bottom:.6mm dashed var(--line);padding-bottom:2mm}
.qk .n{font-family:'Fredoka',sans-serif;font-weight:600;font-size:13pt;color:#fff;background:var(--sea);
 width:10mm;height:10mm;border-radius:50%;display:flex;align-items:center;justify-content:center;flex:0 0 auto}
.qk .t{font-family:'Fredoka',sans-serif;font-weight:600;font-size:14.5pt;line-height:1.15;flex:1}
.qk svg{width:10mm;height:10mm;flex:0 0 auto}
/* --- homework: slovíčka s výslovností --- */
.hwtop{flex:1;min-height:0;display:grid;grid-template-columns:1.05fr 1fr .9fr;gap:9mm}
.hwtop h3{font-family:'Fredoka',sans-serif;font-weight:600;font-size:18pt;margin:0 0 3.5mm;color:var(--sea)}
.hwtop h3 .num{background:var(--sun);color:var(--ink);width:8mm;height:8mm;border-radius:50%;
 display:inline-flex;align-items:center;justify-content:center;font-size:11pt;font-weight:700;margin-right:2mm;
 font-family:'Nunito',sans-serif}
.hwtop>div{display:flex;flex-direction:column}
.vocab2{flex:1;display:flex;flex-direction:column;justify-content:space-between;gap:1mm}
.vocab2 .r{display:flex;align-items:flex-end;gap:3mm}
.vocab2 .w{width:37mm}
.vocab2 .w b{font-family:'Fredoka',sans-serif;font-weight:600;font-size:15pt;display:block;line-height:1.05}
.vocab2 .w span{font-family:'DejaVu Sans Mono',monospace;font-size:8.5pt;color:var(--sea);display:block;margin-top:.5mm}
.vocab2 .w i{font-size:8.5pt;color:#7A939B;font-style:italic;display:block;margin-top:.5mm;line-height:1.25}
.vocab2 .l{flex:1;border-bottom:.6mm dashed var(--line);height:8mm}
.draw2{flex:1;min-height:0;border:.8mm dashed var(--line);border-radius:2mm;display:flex;
 align-items:flex-end;justify-content:center;padding:3mm;text-align:center}
.draw2 span{font-size:9.5pt;color:var(--grey,#7A939B);font-weight:700;letter-spacing:.06em;
 text-transform:uppercase;line-height:1.4}
/* --- check list --- */
.check{flex:1;min-height:0;display:flex;flex-direction:column}
.check .hd{display:flex;align-items:baseline;gap:4mm;margin-bottom:2mm}
.check .hd h3{font-family:'Fredoka',sans-serif;font-weight:600;font-size:17pt;margin:0;color:var(--ink);display:none}
.check .hd span{font-size:10pt;color:var(--sea);font-weight:700}
.clist{flex:1;min-height:0;display:grid;grid-template-columns:1fr 1fr;grid-auto-rows:auto;
 align-content:space-between;gap:3mm 12mm}
.ci{display:flex;align-items:center;gap:4mm;border-bottom:.6mm dashed var(--line);padding-bottom:2.5mm}
.ci svg{width:15mm;height:15mm;flex:0 0 auto}
.ci .t{flex:1}
.ci .t b{font-family:'Fredoka',sans-serif;font-weight:600;font-size:16pt;display:block;line-height:1.15}
.ci .t i{font-size:11pt;color:#7A939B;font-style:italic;font-weight:600;display:block;margin-top:.8mm}
'''

ACTIONS = [
 ("i-swim","swim"), ("i-bike","ride a bike"), ("i-run","run"), ("i-sing","sing"),
 ("i-dance","dance"), ("i-cook","cook"), ("i-draw","draw"), ("i-football","play football"),
 ("i-tennis","play tennis"), ("i-piano","play the piano"), ("i-ski","ski"), ("i-skate","skate"),
]
NAME = dict(ACTIONS)
CAN8 = ["i-swim","i-cook","i-ski","i-sing","i-draw","i-bike","i-piano","i-dance"]
# 20 obrázků na čas: 12 dnešních + 8 z hodiny 1
RACE = [i for i,_ in ACTIONS] + ["i-beach","i-sea","i-icecream","i-mountains",
                                 "i-sun","i-tent","i-suitcase","i-plane"]
TTT1 = ["swim","cook","ski","sing","draw","dance","ride a bike","play the piano","run"]
TTT2 = ["play tennis","skate","play football","draw","swim","sing","ski","cook","dance"]
QUICK = ["Say 5 things you can do.","Spell your name out loud.","Count from 1 to 20.",
         "Ask me 3 questions with CAN.","Say a sentence about your mum with CAN.",
         "Name 3 things you can see in your room."]

PLAN = [("1","Hello again!","3 min"),("2","Action words","5 min"),("3","Word race","4 min"),
        ("4","I can / I can't","5 min"),("5","Can you…?","5 min"),("6","Secret action","5 min"),
        ("7","Homework","3 min")]
TOT=10

def sprite():
    p=['<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>']
    for k,v in list(reuse.items())+list(NEW.items()):
        p.append('<symbol id="%s" viewBox="0 0 100 100">%s</symbol>'%(k,v))
    p.append('</defs></svg>'); return "".join(p)

def foot(n,lbl):
    return ('<div class="foot"><span>English &middot; 15 September</span>'
            '<span>%s</span><span>%d / %d</span></div>'%(lbl,n,TOT))
def head(no,title,task):
    return ('<div class="ph"><div class="grp"><span class="no">%s</span><h2>%s</h2></div>'
            '<span class="task">%s</span></div>'%(no,title,task))

H=['<meta charset="utf-8">','<title>What can you do?</title>','<style>',fonts,base,EXTRA,'</style>',sprite()]

# 1 cover
stars="".join('<svg><use href="#i-star"/></svg>' for _ in range(10))
plan="".join('<div><span class="n">%s</span><div class="t">%s</div><span class="m">%s</span></div>'%p for p in PLAN)
H.append(f'''<div class="page"><div class="airmail"></div><div class="cover">
<div><p class="kicker">English &middot; Lesson 2 &middot; 15 September</p>
<h1>What <span>can</span><br>you do?</h1>
<div class="namebox"><b>My name is</b><span class="l"></span></div>
<div class="starrow"><span class="lbl">My stars today</span>{stars}</div></div>
<div class="plan">{plan}</div></div>{foot(1,"Lesson 2")}</div>''')

# 2 warm-up + homework
Q=[("How are you today?","I'm …"),("What's the weather like today?","It's …"),
   ("What day is it today?","It's Monday / Tuesday …")]
qs="".join('<div class="qrow"><div class="t">%s</div><div class="h">%s</div><div class="wl short"></div></div>'%q for q in Q)
HW=["suitcase","tent","mountains","castle","plane","seaside"]
vs="".join('<div class="vrow"><b>%s</b><span class="l"></span></div>'%w for w in HW)
H.append(f'''<div class="page"><div class="airmail"></div>
{head("1","Hello again!","Answer in a full sentence. Then show me your homework!")}
<div class="two">
 <section><div class="sub">Talk to me</div><div class="qlist">{qs}</div></section>
 <section><div class="sub">Homework check &mdash; write it in Czech</div>
  <div class="qlist">{vs}
  <div class="callout">Now read me <b>one sentence</b> from your notebook!</div></div></section>
</div>{foot(2,"Warm-up")}</div>''')

# 3 action words
cards="".join('<div class="wcard"><svg><use href="#%s"/></svg><span class="en">%s</span><span class="l"></span></div>'%a
              for a in ACTIONS)
H.append(f'''<div class="page"><div class="airmail"></div>
{head("2","Action words","Say it in English. Then write it in Czech on the line.")}
<div class="wgrid">{cards}</div>{foot(3,"Vocabulary")}</div>''')

# 4 WORD RACE
rc="".join('<div class="rcell"><svg><use href="#%s"/></svg></div>'%i for i in RACE)
H.append(f'''<div class="page"><div class="airmail"></div>
{head("3","Word race","No words &mdash; just pictures! Say them all in English. Ready? GO!")}
<div class="race">{rc}</div>
<div class="score">
 <div class="sbox"><span class="h">Round 1 &middot; 60 seconds</span><span class="l"></span></div>
 <div class="sbox"><span class="h">Round 2 &middot; 60 seconds</span><span class="l"></span></div>
 <div class="sbox"><span class="h">Round 3 &middot; 60 seconds</span><span class="l"></span></div>
 <div class="sbox rec"><span class="h">&#9733; My best score</span><span class="l"></span></div>
</div>{foot(4,"Speed game")}</div>''')

# 5 I can / I can't
cc="".join('<div class="canc"><svg><use href="#%s"/></svg><span class="w">%s</span>'
           '<div class="yn"><span class="y">can</span><span class="n">can\'t</span></div></div>'%(i,NAME[i])
           for i in CAN8)
H.append(f'''<div class="page"><div class="airmail"></div>
{head("4","I can / I can't","Circle <b>can</b> or <b>can't</b> for you. Then write three sentences.")}
<div class="cans">{cc}</div>
<div class="iv" style="flex:0 0 auto;margin-top:5mm;gap:2mm">
 <div class="vrow"><b>I can</b><span class="l"></span></div>
 <div class="vrow"><b>I can't</b><span class="l"></span></div>
 <div class="vrow"><b>My mum can</b><span class="l"></span></div>
</div>{foot(5,"Grammar")}</div>''')

# 6 interview
IVQ=["Can you cook?","Can you ski?","Can you play the piano?","Can you dance?","Can you draw?"]
iv="".join('<div class="ivr"><span class="q">%s</span>'
           '<div class="yn"><span class="y">YES</span><span class="n">NO</span></div></div>'%q for q in IVQ)
H.append(f'''<div class="page"><div class="airmail"></div>
{head("5","Can you…?","Ask your teacher. Circle her answer. Then tell me about her.")}
<div class="iv">{iv}
 <div class="vrow"><b>My teacher can</b><span class="l"></span></div>
 <div class="vrow"><b>My teacher can't</b><span class="l"></span></div>
</div>
<div class="rule"><div class="ok">My teacher <u>can</u> swim.</div><div class="bad">My teacher cans swim.</div></div>
{foot(6,"Speaking")}</div>''')

# 7 secret action
cells="".join('<div class="scell"><svg><use href="#%s"/></svg><span>%s</span></div>'%a for a in ACTIONS)
dots="".join('<i></i>' for _ in range(10))
H.append(f'''<div class="page"><div class="airmail"></div>
{head("6","Secret action","Circle one &mdash; don't tell! Your teacher asks, you answer.")}
<div class="two" style="grid-template-columns:2.4fr 1fr">
 <section><div class="sgrid">{cells}</div></section>
 <section class="side">
  <div class="callout">You say:<br><b>Yes, I can.</b><br><b>No, I can't.</b></div>
  <div><div class="lbl">Questions used</div><div class="dots">{dots}</div></div>
  <div class="callout">Got it? <b>Now you ask!</b></div>
 </section>
</div>{foot(7,"Game")}</div>''')

# 8 homework + check list
# slovíčka, která jí 16. 9. nešla — s výslovností a příkladem
HW2=[("seaside","SÍ-sajd","at the seaside"),
     ("inside","in-SAJD","inside the house"),
     ("outside","aut-SAJD","outside in the garden"),
     ("but","bat","I can swim but I can't ski."),
     ("need","níd","I need a ball."),
     ("a little bit","e litl bit","I can cook a little bit.")]
CHECK=[("I can say 12 actions in English.","Umím říct dvanáct činností anglicky."),
       ("I can say what I CAN do.","I can swim."),
       ("I can say what I CAN'T do.","I can't ski."),
       ("I can ask: Can you …?","Umím se zeptat."),
       ("I can answer: Yes, I can. / No, I can't.","Umím krátce odpovědět."),
       ("I can say: My mum can … (no -s!)","Umím mluvit i o někom jiném."),
       ("I know: seaside, inside, outside, but, need.","Nová slovíčka z dneška.")]
voc="".join('<div class="r"><span class="w"><b>%s</b><span>[%s]</span><i>%s</i></span>'
            '<span class="l"></span></div>'%w for w in HW2)
ST=["I can …","I can't …","My best friend can …"]
sts="".join('<div class="starter">%s</div><div class="wl short"></div>'%s for s in ST)
chk="".join('<div class="ci"><svg><use href="#i-star"/></svg>'
            '<span class="t"><b>%s</b><i>%s</i></span></div>'%c for c in CHECK)
H.append(f'''<div class="page"><div class="airmail"></div>
{head("7","Homework","See you next week!")}
<div class="hwtop">
 <div><h3><span class="num">1</span>Learn these words</h3><div class="vocab2">{voc}</div></div>
 <div><h3><span class="num">2</span>Write 3 sentences</h3>{sts}</div>
 <div><h3><span class="num">3</span>Draw &amp; label</h3>
  <div class="draw2"><span>Draw yourself doing something<br>write one sentence with CAN</span></div></div>
</div>
{foot(8,"Homework")}</div>''')

# 9 check list
H.append(f'''<div class="page"><div class="airmail"></div>
{head("8","What I can do now","Colour a star for every YES! Be honest &mdash; it's for you.")}
<div class="check"><div class="clist">{chk}</div></div>
<div class="bye" style="margin-top:4mm">Great job today! See you next week!</div>
{foot(9,"Check")}</div>''')

# 10 bonus
t1="".join('<div>%s</div>'%w for w in TTT1)
t2="".join('<div>%s</div>'%w for w in TTT2)
qk="".join('<div class="qk"><span class="n">%d</span><span class="t">%s</span>'
           '<svg><use href="#i-star"/></svg></div>'%(i,q) for i,q in enumerate(QUICK,1))
H.append(f'''<div class="page"><div class="airmail"></div>
{head("&#9733;","If we have time!","Say a sentence with CAN to take a square. Three in a row wins!")}
<div class="two" style="grid-template-columns:1.5fr 1fr">
 <section style="gap:5mm">
   <div class="tttwrap"><span class="cap">Game 1</span><div class="ttt">{t1}</div></div>
   <div class="tttwrap"><span class="cap">Game 2</span><div class="ttt">{t2}</div></div>
 </section>
 <section><div class="sub">Quick challenges</div><div class="quick">{qk}</div></section>
</div>{foot(10,"Bonus")}</div>''')

out=os.path.join(sp,"list2.html")
open(out,"w",encoding='utf-8').write("\n".join(H))
assert "</style>" in open(out,encoding='utf-8').read(), "CHYBÍ </style>!"
print("list2.html hotov, stran:", TOT, "| </style> ok")
