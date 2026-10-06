# -*- coding: utf-8 -*-
# Data pro RESENI hodiny 3. Jedno cviceni = jedna strana.
# klic: (cislo, nazev, strana v listu, minuty, co_se_uci, rekni_jí(list vet), reseni_html, pozor_html)

def tab(head, rows, w=None):
    cols = "".join('<col style="width:%s">'%x for x in w) if w else ""
    t = '<table class="kt">%s<tr>'%cols + "".join('<th>%s</th>'%h for h in head) + '</tr>'
    for r in rows:
        t += '<tr>' + "".join('<td>%s</td>'%c for c in r) + '</tr>'
    return t + '</table>'

def ol(items, start=1):
    return '<ol class="kl" start="%d">'%start + "".join('<li>%s</li>'%i for i in items) + '</ol>'

def note(s):
    return '<div class="kn">%s</div>'%s

A = '<b class="a">%s</b>'   # doplnena odpoved (zelene)

EX = []

# ---------- 1 Hello again ----------
EX.append((
 "1", "Hello again!", 2, "3 min",
 "Rozmluvit ji po třech týdnech pauzy. Zopakovat <b>can / can't</b> z minulé hodiny "
 "a krátkou odpověď <i>Yes, I can. / No, I can't.</i>",
 ["„Nejdřív si popovídáme. Odpovídej mi <b>celou větou</b>, ne jedním slovem.“",
  "„Teď vpravo — zakroužkuj YES nebo NO a pak to <b>řekni nahlas</b>: Yes, I can. / No, I can't.“"],
 "<div class='kh'>Levý sloupec — mluvení</div>" +
 tab(["Otázka","Jak odpoví","Výslovnost"],
     [("How are you today?", A%"I'm fine, thank you."+" / I'm OK. / I'm tired.", "[ajm fajn, SENK jú]"),
      ("What day is it today?", A%"It's Tuesday."+" (6. 10. 2026 = úterý)", "[ics TJÚZ-dej]"),
      ("What's the weather like?", A%"It's sunny / cloudy / rainy / cold.", "[ics SA-ny / KLAU-dy]")],
     ["30%","40%","30%"]) +
 "<div class='kh'>Pravý sloupec — CAN</div>" +
 tab(["Otázka","Kladně","Záporně"],
     [("Can you swim?", A%"Yes, I can.", A%"No, I can't."),
      ("Can you cook?", A%"Yes, I can.", A%"No, I can't."),
      ("Can you ride a bike?", A%"Yes, I can.", A%"No, I can't."),
      ("Can you play the piano?", A%"Yes, I can.", A%"No, I can't.")],
     ["40%","30%","30%"]) +
 note("Poslední řádek je volný: <b>I can ……… but I can't ……… </b> — doplní dvě svoje slovesa, "
      "např. <i>I can swim but I can't ski.</i> [aj ken swim bat aj kánt skí]"),
 "Po <b>can</b> jde sloveso <b>bez to</b>: <i>I can swim</i>, ne <s>I can to swim</s>.<br>"
 "V odpovědi se <b>neopakuje</b> sloveso: <i>Yes, I can.</i>, ne <s>Yes, I can swim.</s><br>"
 "<b>can't</b> se čte [kánt] — dlouze, jinak to zní jako <i>can</i>."
))

# ---------- 2 Verb BE ----------
EX.append((
 "2", "Verb BE — tabulka + věty s vlajkami", 3, "5 min",
 "Úplný systém slovesa <b>být</b>: dlouhý tvar, krátký tvar, zápor. "
 "Tohle je jádro celého testu — bez toho neudělá skoro žádné cvičení.",
 ["„Do prázdného sloupce doplň <b>krátký tvar</b>. am se zkracuje na ’m, is na ’s, are na ’re.“",
  "„Teď věty. Podívej se na vlajku, doplň sloveso <b>a</b> zemi. Nahlas celou větu.“"],
 "<div class='kh'>Tabulka 1 — kladně</div>" +
 tab(["who","long form","short form"],
     [("I","am",A%"I'm"),("He / She / It","is",A%"he's / she's / it's"),
      ("We / You / They","are",A%"we're / you're / they're")], ["34%","26%","40%"]) +
 "<div class='kh'>Tabulka 2 — záporně</div>" +
 tab(["who","negative long","negative short"],
     [("I","am not",A%"I'm not"),("He / She / It","is not",A%"he isn't / she isn't / it isn't"),
      ("We / You / They","are not",A%"we aren't / you aren't / they aren't")], ["34%","26%","40%"]) +
 "<div class='kh'>Věty s vlajkami &mdash; celé znění</div>" +
 tab(["#","Celá věta","Výslovnost","Vlajka"],
     [("1","This is Rosa. "+A%"She's"+" from "+A%"Italy"+".","[ši-z from I-te-ly]","Itálie"),
      ("2",A%"I'm"+" from "+A%"Spain"+".","[ajm from spejn]","Španělsko"),
      ("3",A%"We're"+" from "+A%"Japan"+".","[wír from dže-PEN]","Japonsko"),
      ("4","This is Hans. "+A%"He's"+" from "+A%"Hungary"+".","[hí-z from HAN-ge-ry]","Maďarsko"),
      ("5",A%"They're"+" from "+A%"the Czech Republic"+".","[dej-r from ď ček ri-PAB-lik]","Česko")],
     ["5%","43%","34%","18%"]),
 "U <b>I'm not</b> existuje jen jeden krátký tvar — <s>I amn't</s> neexistuje.<br>"
 "Zápor jde zkrátit dvěma způsoby: <i>she's not</i> i <i>she isn't</i>. Obojí je správně, "
 "v Projectu se učí <b>isn't / aren't</b> — ber to jako první volbu.<br>"
 "Země se píšou <b>velkým písmenem</b>: Italy, Spain. U <i>the USA</i> a <i>the Czech Republic</i> musí být <b>the</b>."
))

# ---------- 3 Words ----------
EX.append((
 "3", "Words for the test — slovíčka", 4, "3 min",
 "Projet nahlas obě sady slovíček, které v testu budou: <b>8 zemí</b> a <b>12 slov o rodině</b>. "
 "Výslovnost v závorce je zjednodušená — čti ji přesně tak, jak je napsaná.",
 ["„Přečti mi každé slovo nahlas. V závorce je, jak se to čte. VELKÁ písmena = tam je přízvuk.“",
  "„Které tři jsou nejtěžší? Ty si zakroužkuj, ty zopakujeme na konci hodiny.“"],
 "<div class='kh'>Na co si dát pozor ve výslovnosti</div>" +
 tab(["Slovo","Správně","Častá chyba"],
     [("the USA","[ď jú-es-EJ] — přízvuk na konci","[JÚ-es-ej]"),
      ("Japan","[dže-PEN] — přízvuk na druhé slabice","[DŽA-pan]"),
      ("Italy","[I-te-ly] — přízvuk na začátku","[i-TÁ-ly]"),
      ("aunt","[ánt] — jedna slabika, dlouhé á","[ent]"),
      ("uncle","[ANKL] — bez samohlásky na konci","[AN-kle]"),
      ("daughter","[DÓ-tr] — <b>gh</b> se nečte","[DAUG-tr]"),
      ("children","[ČIL-drn]","[CHIL-dren]")], ["22%","42%","36%"]) +
 note("Pozor na dvojice, které si plete: <b>grandmother</b> = babička × <b>mother</b> = matka; "
      "<b>parents</b> = rodiče (vždy množné) × <b>parent</b> = jeden rodič."),
 "Tahle strana <b>nemá řešení</b> — je to referenční tabulka, nic se nedoplňuje. "
 "Je tam proto, aby měla slovíčka na jednom místě, až se bude učit sama.<br>"
 "<b>cousin</b> [KAZN] je v angličtině <b>jedno slovo</b> pro bratrance i sestřenici — rod se nerozlišuje."
))

# ---------- 4 Word race ----------
EX.append((
 "4", "Word race — rychlovka", 5, "3 min",
 "Automatizace. Zná je, ale pomalu — v testu nebude čas přemýšlet. "
 "Tři kola po minutě, skóre se zapisuje, snaží se překonat sama sebe.",
 ["„Teď hra. Já ukazuju česky, ty říkáš anglicky. Máš minutu. Kolik jich stihneš?“",
  "„Kolik jsi měla? Zapíšeme. Druhé kolo — zkus být rychlejší.“"],
 "<div class='kh'>Klíč — 20 slov v pořadí, jak jsou v mřížce</div>" +
 '<div class="two-col">' +
 tab(["Česky","Anglicky","Výslovnost"],
     [("Británie","Britain","[BRI-tn]"),("Spojené státy","the USA","[ď jú-es-EJ]"),
      ("Francie","France","[fráns]"),("Itálie","Italy","[I-te-ly]"),
      ("Španělsko","Spain","[spejn]"),("Japonsko","Japan","[dže-PEN]"),
      ("Česká republika","the Czech Republic","[ď ček ri-PAB-lik]"),("Řecko","Greece","[grís]"),
      ("matka","mother","[MA-dr]"),("otec","father","[FÁ-dr]")], ["30%","32%","38%"]) +
 tab(["Česky","Anglicky","Výslovnost"],
     [("sestra","sister","[SIS-tr]"),("bratr","brother","[BRA-dr]"),
      ("babička","grandmother","[GREN-ma-dr]"),("dědeček","grandfather","[GREN-fá-dr]"),
      ("rodiče","parents","[PE-rnts]"),("děti","children","[ČIL-drn]"),
      ("teta","aunt","[ánt]"),("strýc","uncle","[ANKL]"),
      ("bratranec","cousin","[KAZN]"),("dcera","daughter","[DÓ-tr]")], ["30%","32%","38%"]) +
 '</div>' +
 note("Skóre zapisuj do boxů dole na listu. <b>Nehádej se o výslovnost během kola</b> — "
      "běží čas, opravíš až po kole."),
 "Uznávej i <i>Britain</i> místo <i>the UK</i> a naopak — obojí je správně.<br>"
 "Když zasekne, <b>neříkej odpověď</b> — řekni první hlásku („B…“) a jdi dál. "
 "Vrať se k tomu až v dalším kole.<br>"
 "Cíl není 20 z 20. Cíl je, aby třetí kolo bylo lepší než první."
))

# ---------- 5 pronouns ----------
EX.append((
 "5", "my / your / his / her — přivlastňovací zájmena", 6, "4 min",
 "Přivlastňovací zájmena a hlavně rozdíl <b>its</b> (jeho) × <b>it's</b> (ono je). "
 "V Progress checku na tohle bývá chyták.",
 ["„Vedle každého zájmena doplň přivlastňovací tvar. I → my. Pokračuj.“",
  "„Teď věty. Do každé doplň <b>jedno slovo</b> z té tabulky vlevo.“"],
 "<div class='kh'>Tabulka</div>" +
 '<div class="two-col">' +
 tab(["pronoun","possessive","význam"],
     [("I",A%"my","[maj] můj"),("you",A%"your","[jór] tvůj"),
      ("he",A%"his","[hiz] jeho"),("she",A%"her","[hr] její")], ["26%","30%","44%"]) +
 tab(["pronoun","possessive","význam"],
     [("it",A%"its","[ics] jeho (věc, zvíře)"),("we",A%"our","[aur] náš"),
      ("they",A%"their","[dér] jejich"),("&nbsp;","&nbsp;","&nbsp;")], ["26%","30%","44%"]) +
 '</div>' +
 "<div class='kh'>Věty — celé znění</div>" +
 ol(["This is my brother. " + A%"His" + " name's Joe.",
     "These are my parents. " + A%"Their" + " names are Mary and Jack.",
     "I've got a dog. " + A%"Its" + " name's Buddy.",
     "This is Millie. " + A%"Her" + " dog is Mut.",
     "We're in Class 7. " + A%"Our" + " teacher is Mr Brown.",
     "What's " + A%"your" + " name? I'm Rozárka."]),
 "Věta 3 je ta past: <b>Its</b> name — <b>bez apostrofu</b>. "
 "S apostrofem <i>it's</i> znamená <i>it is</i>. Pomůcka: dosaď „ono je“ — "
 "„<s>ono je</s> jméno je Buddy“ nedává smysl, tedy <b>its</b>.<br>"
 "<b>his</b> × <b>her</b> se řídí tím, <b>komu to patří</b>, ne tím, co se vlastní: "
 "<i>Millie — <b>her</b> dog</i> (i když pes je kluk).<br>"
 "Věta 2: <i>names</i> je v množném čísle, protože rodiče jsou dva."
))

# ---------- 6 questions ----------
EX.append((
 "6", "Questions and short answers", 7, "5 min",
 "Otázka se tvoří <b>prohozením</b> (You are → Are you?) a krátká odpověď "
 "se musí říct <b>celá</b>. Tohle v testu bývá za nejvíc bodů.",
 ["„Zakroužkuj YES nebo NO podle toho, jak to je u tebe.“",
  "„A teď to <b>řekni celé</b>. Ne jenom yes — Yes, I am.“"],
 "<div class='kh'>Krátké odpovědi ke každé otázce</div>" +
 tab(["#","Otázka","Yes-odpověď","No-odpověď"],
     [("1","Are you from the Czech Republic?",A%"Yes, I am.",A%"No, I'm not."),
      ("2","Is your mum a teacher?",A%"Yes, she is.",A%"No, she isn't."),
      ("3","Are your friends at school?",A%"Yes, they are.",A%"No, they aren't."),
      ("4","Is your dog friendly?",A%"Yes, it is.",A%"No, it isn't."),
      ("5","Am I your teacher?",A%"Yes, you are.",A%"No, you aren't."),
      ("6","Are we on the computer?",A%"Yes, we are.",A%"No, we aren't.")],
     ["5%","39%","28%","28%"]) +
 note("Výslovnost: <i>Yes, I am.</i> [jes aj em] · <i>No, she isn't.</i> [nou ší IZ-nt] · "
      "<i>No, they aren't.</i> [nou dej ÁRNT]"),
 "<b>Kladná</b> krátká odpověď se <b>nezkracuje</b>: <i>Yes, he is.</i> — nikdy <s>Yes, he's.</s> "
 "To je na listu schválně přeškrtnuté. Záporná se zkrátit <b>musí</b>: <i>No, he isn't.</i><br>"
 "Otázka 5 je chyták: ptám se <b>já</b> (Am I…?), takže odpovídá <b>you are</b>, ne <s>I am</s>.<br>"
 "Otázka 4 — pes je pro ni asi „he“, ale v Projectu se u zvířete učí <b>it</b>. Uznej obojí, "
 "ale ukaž, že v testu je bezpečnější <b>it</b>."
))

# ---------- 7 wh ----------
EX.append((
 "7", "Wh- questions — spojovačka", 8, "3 min",
 "Rozlišit tázací slova: <b>What / Where / How old / When / Who / Whose</b>. "
 "Odpovědi vpravo jsou schválně v jiném pořadí, aby musela přemýšlet, ne jen táhnout čáry rovně.",
 ["„Spoj čarou otázku s odpovědí. Pozor, nejsou ve stejném pořadí.“",
  "„Hotovo? Teď dole odpověz <b>sama za sebe</b> — tvoje jméno, tvůj věk, tvoje narozeniny.“"],
 "<div class='kh'>Správné dvojice &mdash; a kde ta odpověď na listu leží</div>" +
 tab(["Otázka (vlevo)","Správná odpověď","Je vpravo v řádku","Tázací slovo"],
     [("1 &nbsp;What's your name?", A%"My name's Rozárka."+"<br><span class='ph'>[maj nejms ro-ZÁR-ka]</span>", "3.", "What = Co / Jaký"),
      ("2 &nbsp;Where are you from?", A%"I'm from the Czech Republic."+"<br><span class='ph'>[ajm from ď ček ri-PAB-lik]</span>", "5.", "Where = Odkud"),
      ("3 &nbsp;How old are you?", A%"I'm eleven."+"<br><span class='ph'>[ajm i-LE-vn]</span>", "1.", "How old = Jak starý"),
      ("4 &nbsp;When is your birthday?", A%"It's on 5th May."+"<br><span class='ph'>[ics on fifs mej]</span>", "6.", "When = Kdy"),
      ("5 &nbsp;Who is your teacher?", A%"Mrs Nováková."+"<br><span class='ph'>[MI-siz no-VÁ-ko-vá]</span>", "4.", "Who = Kdo"),
      ("6 &nbsp;Whose dog is it?", A%"It's my sister's."+"<br><span class='ph'>[ics maj SIS-trz]</span>", "2.", "Whose = Čí")],
     ["27%","35%","13%","25%"]) +
 note("Dole na listu jsou tři boxy, kam píše odpověď <b>o sobě</b>: jméno, věk, narozeniny. "
      "Ty si nech přečíst nahlas — jsou to věty, které u zkoušení řekne jako první."),
 "Nejčastější záměna: <b>Who</b> (kdo) × <b>Whose</b> (čí) — zní skoro stejně: "
 "[hú] × [húz]. Pozná to jen podle toho <b>z</b> na konci.<br>"
 "<i>How old are you?</i> &rarr; <b>I'm eleven.</b>, ne <s>I have eleven years.</s> — "
 "v angličtině se věk <b>je</b>, nemá.<br>"
 "Datum má předložku <b>on</b>: <i>It's <b>on</b> 5th May.</i><br>"
 "Poslední odpověď <i>It's my sister's.</i> má <b>'s</b> navíc — přivlastnění. To navazuje na cvičení 8."
))

# ---------- 8 possessive + days ----------
EX.append((
 "8", "Possessive 's a dny v týdnu", 9, "4 min",
 "Dvě věci, které v Revision a Self-assessment v učebnici jsou, ale ve zbytku hodiny by vypadly: "
 "přivlastňovací <b>'s</b> u jmen a <b>sedm dní v týdnu</b>.",
 ["„Vlevo: komu to patří? Napiš <b>celou větu</b>. První je předepsaná jako vzor.“",
  "„Vpravo: doplň dny v týdnu. První písmeno máš napovězené.“"],
 "<div class='kh'>Vlevo — Whose is it?</div>" +
 ol(["Mel / pen &rarr; " + A%"This is Mel's pen." + " &nbsp;<span class='ph'>(vzor, už je napsaný)</span>",
     "Joe / watch &rarr; " + A%"This is Joe's watch.",
     "Jack and Maya / dog &rarr; " + A%"This is Jack and Maya's dog.",
     "Lin / book &rarr; " + A%"This is Lin's book.",
     "Granddad and Grandma / house &rarr; " + A%"This is Granddad and Grandma's house."]) +
 "<div class='kh'>Vpravo — Days of the week</div>" +
 tab(["","Anglicky","Výslovnost","Česky"],
     [("M",A%"Monday","[MAN-dej]","pondělí"),("T",A%"Tuesday","[TJÚZ-dej]","úterý"),
      ("W",A%"Wednesday","[WENZ-dej]","středa"),("T",A%"Thursday","[SÖRZ-dej]","čtvrtek"),
      ("F",A%"Friday","[FRAJ-dej]","pátek"),("S",A%"Saturday","[SE-tr-dej]","sobota"),
      ("S",A%"Sunday","[SAN-dej]","neděle")], ["6%","28%","36%","30%"]) +
 note("Dole dvě volné věty: <b>Today is</b> " + A%"Tuesday" + ". (6. 10. 2026) a "
      "<b>My birthday is on</b> ……… — doplní svoje."),
 "U dvou jmen jde <b>'s jen na to poslední</b>: <i>Jack and Maya<b>'s</b> dog</i>, "
 "ne <s>Jack's and Maya's</s>. Tohle v testu bývá.<br>"
 "Dny se píšou <b>velkým písmenem</b> — Monday, ne <s>monday</s>. Čeština to má malé, proto to plete.<br>"
 "<b>Wednesday</b> — píše se s <b>d</b>, které se <b>nečte</b>: [WENZ-dej]. Nejčastější pravopisná chyba.<br>"
 "Před dnem je předložka <b>on</b>: <i>on Monday</i>."
))

# ---------- 9 homework ----------
EX.append((
 "9", "Domácí úkol", 10, "2 min",
 "Zadání úkolu. Je i jako samostatné jednostránkové PDF, které jí můžeš poslat.",
 ["„Doma tři věci: naučit šest slovíček, napsat tři věty, nakreslit rodinu.“",
  "„Ty věty si <b>vymysli sama</b> — mají být o tobě, ne opsané.“"],
 "<div class='kh'>1 — slovíčka k naučení</div>" +
 tab(["Anglicky","Výslovnost","Česky"],
     [("mother","[MA-dr]","matka"),("father","[FÁ-dr]","otec"),("parents","[PE-rnts]","rodiče"),
      ("children","[ČIL-drn]","děti"),("cousin","[KAZN]","bratranec / sestřenice"),
      ("Whose?","[húz]","Čí?")], ["30%","34%","36%"]) +
 "<div class='kh'>2 — tři věty, vzorové řešení</div>" +
 ol(["I'm from " + A%"Brno" + ". &nbsp;<span class='ph'>(jakékoli město)</span>",
     "My mum is " + A%"a nurse" + ". / " + A%"forty" + ". / " + A%"nice" + ".",
     "My best friend isn't " + A%"from Prague" + ". / " + A%"twelve" + "."]) +
 note("<b>3 — Draw &amp; label:</b> nakreslí rodinu a napíše <b>jednu větu</b> "
      "s <i>his</i>, <i>her</i> nebo <i>their</i>. Např. " + A%"This is my brother. His name is Tom."),
 "Třetí věta je <b>záporná</b> — musí tam zůstat <b>isn't</b>. "
 "Když napíše <i>My best friend is from Prague</i>, úkol nesplnila.<br>"
 "U druhé věty uznej cokoli, co dává smysl — povolání, věk i vlastnost."
))

# ---------- 10 check list ----------
EX.append((
 "10", "What I can do now — sebehodnocení", 11, "2 min",
 "Ona sama označí, co umí. <b>Tohle není cvičení na body</b> — je to tvoje mapa, "
 "co vzít příště. Nevybarvená hvězda = téma na příští hodinu.",
 ["„Vybarvi hvězdu u všeho, co fakt umíš. Buď upřímná — co nevybarvíš, na to se příště podíváme.“",
  "„Co bylo dneska nejtěžší?“"],
 "<div class='kh'>Deset bodů a kde se to procvičovalo</div>" +
 tab(["Umím…","Procvičeno ve cvičení","Když nevybarví →"],
     [("am / is / are","2","projít znovu tabulku BE"),
      ("krátké tvary I'm, he's, we're","2","diktovat 10 vět k zkrácení"),
      ("zápor isn't, aren't","2, mini test","5 vět: udělej z toho zápor"),
      ("otázky Are you…? Is he…?","6","prohazovací drill"),
      ("krátké odpovědi Yes, he is.","6","5× otázka–odpověď nahlas"),
      ("my, his, her, its, our, their","5","tabulka zájmen + 6 vět"),
      ("Wh- otázky","7","spojovačka znovu, pak sama tvoří"),
      ("8 zemí a 10 slov o rodině","3, 4","Word race doma, 1 minuta denně"),
      ("'s: This is Mel's pen.","8","5 nových jmen"),
      ("sedm dní v týdnu","8","říkat je každý den ráno")], ["34%","26%","40%"]) +
 note("Výsledek si <b>zapiš</b> do <i>Feedback/Rozarka/2026-10-06-jak-to-dopadlo.md</i> — "
      "podle toho se staví příští hodina."),
 "Když vybarví všechno, ptej se dál — děti vybarvují z ostychu. "
 "Ověř aspoň dvě položky otázkou navíc.<br>"
 "Když nevybarví skoro nic, <b>nelam to přes koleno</b>. Vyber jedno téma a to příště celou hodinu."
))

# ---------- mini test ----------
EX.append((
 "&#9733;", "Mini test — 12 úkolů", 12, "5 min",
 "Simulace školního Progress checku. Dělá to <b>sama a bez nápovědy</b> — jinak to nic nezměří. "
 "Výsledek ti řekne, jestli je na test připravená.",
 ["„Teď sama. Nebudu ti radit. Dvanáct vět, do každé jedno slovo.“",
  "„Hotovo? Projdeme to spolu a spočítáme body.“"],
 "<div class='kh'>Řešení — 12 bodů</div>" +
 '<div class="two-col">' +
 tab(["Zadání","Správně"],
     [("<b class='q'>1</b> I ……… from Brno.",A%"am / 'm"),
      ("<b class='q'>2</b> She ……… from Spain. (NOT)",A%"isn't"),
      ("<b class='q'>3</b> ……… you twelve?",A%"Are"),
      ("<b class='q'>4</b> This is my brother. ……… name's Tom.",A%"His"),
      ("<b class='q'>5</b> Where ……… you from?",A%"are"),
      ("<b class='q'>6</b> ……… old are you?",A%"How")], ["57%","43%"]) +
 tab(["Zadání","Správně"],
     [("<b class='q'>7</b> We ……… in the garden.",A%"are / 're"),
      ("<b class='q'>8</b> Is Paul your friend? No, he ……… .",A%"isn't"),
      ("<b class='q'>9</b> This is Millie. ……… dog is Mut.",A%"Her"),
      ("<b class='q'>10</b> ……… is your birthday?",A%"When"),
      ("<b class='q'>11</b> This is Mel. It's ……… pen.",A%"Mel's"),
      ("<b class='q'>12</b> After Monday it's ……… .",A%"Tuesday")], ["57%","43%"]) +
 '</div>' +
 "<div class='kh'>Hodnocení</div>" +
 tab(["Body","Co to znamená","Co s tím"],
     [("11–12","Na test připravená.","Jen zopakovat slovíčka."),
      ("8–10","Základ sedí, drhnou detaily.","Projít chyby a zadat 5 podobných vět."),
      ("5–7","Gramatiku zná, ale nepoužívá jistě.","Příští hodinu celou na BE + zájmena."),
      ("0–4","Látku nemá.","Nestavět na tom dál — vrátit se na začátek Unit 2.")], ["12%","44%","44%"]),
 "Bod 1 a 7: uznej <b>oba tvary</b> — <i>am</i> i <i>'m</i>, <i>are</i> i <i>'re</i>.<br>"
 "Bod 2: musí být <b>zápor</b> (je tam NOT) — <i>isn't</i>, nebo <i>'s not</i>. "
 "Samotné <i>is</i> je chyba.<br>"
 "Bod 11: <b>Mel's</b> s apostrofem. <i>Mels</i> bez apostrofu neuznávej — v testu to nebude uznané taky.<br>"
 "Bod 12: pondělí → <b>Tuesday</b>, velké T."
))

# ---------- caste chyby (samostatna strana) ----------
MIST = [
 ("Yes, he's.", "Yes, he <b>is</b>.", "Kladná krátká odpověď se nikdy nezkracuje."),
 ("I have eleven years.", "I'<b>m</b> eleven.", "Věk se v angličtině <b>je</b>, nemá."),
 ("It's name is Buddy.", "<b>Its</b> name is Buddy.", "its = jeho (bez apostrofu) × it's = it is."),
 ("I can to swim.", "I can <b>swim</b>.", "Po can jde sloveso bez <i>to</i>."),
 ("She don't like it.", "She <b>doesn't</b> like it.", "U he/she/it je <b>doesn't</b>."),
 ("Jack's and Maya's dog", "Jack and Maya<b>'s</b> dog", "U dvou jmen jde 's jen na poslední."),
 ("on monday", "on <b>Monday</b>", "Dny se píšou velkým písmenem."),
 ("I am from Czech Republic.", "I'm from <b>the</b> Czech Republic.", "Před Czech Republic a USA musí být <b>the</b>."),
 ("Who dog is it?", "<b>Whose</b> dog is it?", "Who = kdo, Whose = čí."),
 ("He is'nt here.", "He is<b>n't</b> here.", "Apostrof je <b>před</b> t, ne za s."),
]

TIME = [
 ("0:00", "1", "Hello again! + CAN", "3 min"),
 ("0:03", "2", "Verb BE — tabulka + vlajky", "5 min"),
 ("0:08", "3", "Words for the test (čtení nahlas)", "3 min"),
 ("0:11", "4", "Word race — 3 kola", "3 min"),
 ("0:14", "5", "my / his / her", "4 min"),
 ("0:18", "6", "Questions + short answers", "5 min"),
 ("0:23", "7", "Wh- questions (spojovačka)", "3 min"),
 ("0:26", "8", "Possessive 's + dny v týdnu", "4 min"),
 ("0:30", "&#9733;", "Mini test — <i>když nezbude čas, zadej domů</i>", "5 min"),
]
