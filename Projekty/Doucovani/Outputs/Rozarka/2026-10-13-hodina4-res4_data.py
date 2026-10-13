# -*- coding: utf-8 -*-
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
A = '<b class="a">%s</b>'

EX = []

# ---------- 1 Hello again ----------
EX.append((
 "1", "Hello again! + am / is / are", 2, "3 min",
 "Rozmluvit ji a <b>zkontrolovat, jestli jí zůstalo sloveso být</b> z minulé hodiny. "
 "Bez něj dnešní <i>have got</i> nepostavíš &mdash; obojí se plete.",
 ["„Nejdřív si popovídáme. Odpovídej mi <b>celou větou</b>.“",
  "„Jak dopadl ten test? Nemusíš říkat známku, jen jestli to bylo lehké nebo těžké.“",
  "„Teď vpravo rychlovka &mdash; doplň <b>am, is</b> nebo <b>are</b>. Nahlas.“"],
 "<div class='kh'>Vlevo &mdash; mluvení</div>" +
 tab(["Otázka","Jak odpoví","Výslovnost"],
     [("How are you today?", A%"I'm fine, thank you."+" / I'm OK.","[ajm fajn, SENK jú]"),
      ("What day is it today?", A%"It's Tuesday."+" (13. 10. 2026 = úterý)","[ics TJÚZ-dej]"),
      ("How was the test?", A%"It was easy / OK / difficult.","[it woz Í-zy / DI-fi-kalt]")],
     ["30%","40%","30%"]) +
 "<div class='kh'>Vpravo &mdash; am / is / are</div>" +
 ol(["I " + A%"am" + " (" + A%"'m" + ") from the Czech Republic.",
     "My mum " + A%"is" + " a teacher.",
     "My friends " + A%"are" + " at school.",
     A%"Are" + " you eleven?"]) +
 note("Když u <b>How was the test?</b> neví, co říct, nabídni jí tři slova: "
      "<i>easy</i> [Í-zy] lehký &middot; <i>OK</i> [ou-KEJ] &middot; <i>difficult</i> [DI-fi-kalt] těžký."),
 "Věta 4 je otázka &mdash; sloveso jde <b>dopředu</b>: <i>Are you&hellip;?</i>, ne <s>You are&hellip;?</s><br>"
 "Kdyby <b>vynechala sloveso</b> („I from Brno“), je to nejčastější chyba z minula &mdash; zopakuj "
 "rámeček dole na listu a jeď dál, nezdržuj se tím déle než minutu.<br>"
 "<b>Tohle cvičení není dnešní látka</b> &mdash; je to jen zahřátí. Když jí jde, zkrať ho a získej čas."
))

# ---------- 2 cousin ----------
EX.append((
 "2", "Who is a cousin? &mdash; rodokmen", 3, "4 min",
 "<b>cousin</b> je slovo, které jí dělá problém.</b> Tři důvody: píše se jinak, než se čte; "
 "je to jedno slovo pro kluka i holku; a hlavně <b>neví, co to v příbuzenstvu znamená</b>. "
 "Rodokmen to řeší obrázkem, ne definicí.",
 ["„Podívej se na ten obrázek. Nahoře babička a děda. Ti mají dvě dcery &mdash; tvoji mámu a tvoji tetu.“",
  "„A teď to důležité: dítě tvojí tety je tvůj <b>cousin</b>. Česky bratranec nebo sestřenice.“",
  "„V angličtině je to <b>jedno slovo</b> pro kluka i pro holku. Nerozlišuje se.“",
  "„Čte se to <b>[KA-zn]</b>. Píše se ou, ale čte se A. Řekni to třikrát.“"],
 "<div class='kh'>Řešení vět</div>" +
 ol(["My mum's sister is my " + A%"aunt" + ". &nbsp;<span class='ph'>[ánt]</span>",
     "My aunt's son is my " + A%"cousin" + ". &nbsp;<span class='ph'>[KA-zn]</span>",
     "My dad's brother is my " + A%"uncle" + ". &nbsp;<span class='ph'>[ANKL]</span>",
     "Grandma and Granddad are my " + A%"grandparents" + ". &nbsp;<span class='ph'>[GREN-pe-rnts]</span>"]) +
 "<div class='kh'>Co je na rodokmenu</div>" +
 tab(["Patro","Kdo","Česky"],
     [("1.","Grandma + Granddad","babička a dědeček"),
      ("2.","my mum &middot; my aunt","máma a teta &mdash; <b>sestry</b>"),
      ("3.","ME &middot; my COUSIN","já a můj bratranec / moje sestřenice")],
     ["12%","44%","44%"]) +
 note("Když řekne, že žádného bratrance nemá, je to v pořádku &mdash; ať pak mluví o kamarádovi: "
      "<i>My friend has got a cousin.</i> Důležité je, aby chápala <b>vztah</b>, ne aby měla vlastního."),
 "Nejčastější chyby u <b>cousin</b>:<br>"
 "&bull; čte to <s>[KOU-sin]</s> nebo <s>[KAU-zin]</s> podle psané podoby &rarr; správně <b>[KA-zn]</b>;<br>"
 "&bull; hledá zvlášť slovo pro sestřenici &rarr; <b>žádné není</b>, cousin je obojí;<br>"
 "&bull; plete si <b>aunt</b> (teta) a <b>uncle</b> (strýc). Pomůcka: <i>a</i>unt = <i>a</i> jako „ona“, uncle má <i>u</i> jako „ujo“.<br>"
 "<b>grandparents</b> je vždy v množném čísle &mdash; jsou dva."
))

# ---------- 3 slovicka ----------
EX.append((
 "3", "Words for today &mdash; slovíčka", 4, "3 min",
 "Dvě sady: <b>rodina</b> (opakování + Hungary, které minule chybělo) a <b>věci</b> (nové, "
 "potřebuje je na dnešní <i>have got</i>). Tahle strana se <b>nevyplňuje</b>, jen čte nahlas.",
 ["„Přečti mi každé slovo nahlas. V závorce je, jak se to čte. VELKÁ písmena = tam je přízvuk.“",
  "„Které tři jsou nejtěžší? Zakroužkuj si je, vrátíme se k nim na konci.“"],
 "<div class='kh'>Na co si dát pozor ve výslovnosti</div>" +
 tab(["Slovo","Správně","Častá chyba"],
     [("cousin","[KA-zn] &mdash; ou se čte jako A","[KOU-sin]"),
      ("aunt","[ánt] &mdash; jedna slabika, dlouhé á","[ent]"),
      ("uncle","[ANKL] &mdash; na konci není samohláska","[AN-kle]"),
      ("daughter","[DÓ-tr] &mdash; <b>gh</b> se vůbec nečte","[DAUG-tr]"),
      ("Hungary","[HAN-ge-ry] &mdash; přízvuk na začátku","[hun-GA-ry]"),
      ("a mobile","[e MOU-bajl] &mdash; přízvuk na druhé slabice","[MO-bil]"),
      ("a watch","[e woč] &mdash; krátké, jedna slabika","[watch]"),
      ("an umbrella","[en am-BRE-la] &mdash; přízvuk uprostřed","[UM-bre-la]")],
     ["20%","46%","34%"]) +
 note("<b>a</b> vs. <b>an</b>: před samohláskou je <b>an</b> &mdash; proto <i>an umbrella</i>, "
      "ale <i>a dog</i>. Je to jen kvůli výslovnosti, aby se to nedrhlo."),
 "Tahle strana <b>nemá řešení</b> &mdash; nic se nedoplňuje, je to referenční tabulka, "
 "ze které se bude učit doma.<br>"
 "Nenech ji číst potichu. <b>Musí to zaznít nahlas</b>, jinak si zafixuje čtení podle psané podoby "
 "&mdash; a přesně to je problém u <i>cousin</i>."
))

# ---------- 4 word race ----------
EX.append((
 "4", "Word race &mdash; rychlovka", 5, "3 min",
 "Automatizace. Osmnáct slov z dneška + dvě ze třetí hodiny (Itálie, Španělsko) jako opakování. "
 "Tři kola po minutě, zapisuje se skóre.",
 ["„Teď hra. Já ukazuju česky, ty říkáš anglicky. Máš minutu. Kolik stihneš?“",
  "„Kolik jsi měla? Zapíšeme. Druhé kolo &mdash; zkus být rychlejší.“"],
 "<div class='kh'>Klíč &mdash; 20 slov v pořadí, jak jsou v mřížce</div>" +
 '<div class="two-col">' +
 tab(["Česky","Anglicky","Výslovnost"],
     [("bratranec","cousin","[KA-zn]"),("teta","aunt","[ánt]"),
      ("strýc","uncle","[ANKL]"),("syn","son","[san]"),
      ("dcera","daughter","[DÓ-tr]"),("prarodiče","grandparents","[GREN-pe-rnts]"),
      ("bratr","brother","[BRA-dr]"),("sestra","sister","[SIS-tr]"),
      ("Maďarsko","Hungary","[HAN-ge-ry]"),("Itálie","Italy","[I-te-ly]")],
     ["30%","32%","38%"]) +
 tab(["Česky","Anglicky","Výslovnost"],
     [("pes","a dog","[e dog]"),("kočka","a cat","[e ket]"),
      ("mobil","a mobile","[e MOU-bajl]"),("hodinky","a watch","[e woč]"),
      ("kniha","a book","[e buk]"),("deštník","an umbrella","[en am-BRE-la]"),
      ("dům","a house","[e haus]"),("kolo","a bike","[e bajk]"),
      ("domácí mazlíček","a pet","[e pet]"),("Španělsko","Spain","[spejn]")],
     ["30%","32%","38%"]) +
 '</div>' +
 note("Poslední dvě v každém sloupci (<b>Itálie</b>, <b>Španělsko</b>) jsou <b>z třetí hodiny</b> "
      "&mdash; schválně, ať se neztratí. U věcí uznej i samotné slovo bez <i>a</i>."),
 "<b>Nehádej se o výslovnost během kola</b> &mdash; běží čas. Opravuj až mezi koly.<br>"
 "Když zasekne, <b>neříkej odpověď</b>: nápověda je první hláska („B&hellip;“) a jedeš dál.<br>"
 "Cíl není 20 z 20. Cíl je, aby třetí kolo bylo lepší než první. To si zapiš do feedbacku."
))

# ---------- 5 have got ----------
EX.append((
 "5", "HAVE GOT &mdash; hlavní gramatika dne", 6, "5 min",
 "Vyjádření <b>vlastnictví</b>. Dvě věci: (1) tvar se mění jen u <b>he / she / it</b> &rarr; <i>has</i>; "
 "(2) <b>’s může být „is“ i „has“</b> &mdash; to je past, která navazuje přímo na minulou hodinu.",
 ["„Anglicky se neřekne jen <i>mám</i>. Říká se <b>have got</b> &mdash; doslova „mám dostáno“. Ber to jako jedno slovo.“",
  "„U <b>he, she, it</b> se have mění na <b>has</b>. Jinde ne.“",
  "„Teď ten červený rámeček. Minule jsme měly <i>He’s from Italy</i> &mdash; tam ’s znamenalo <b>is</b>. "
  "Dneska <i>He’s got a cat</i> &mdash; tady ’s znamená <b>has</b>. Pozná se to podle toho, jestli za tím je <b>got</b>.“"],
 "<div class='kh'>Tabulka 1 &mdash; kladně</div>" +
 tab(["who","dlouhý tvar","krátký tvar"],
     [("I / you / we / they","have got",A%"'ve got"),
      ("he / she / it","has got",A%"'s got")], ["36%","28%","36%"]) +
 "<div class='kh'>Tabulka 2 &mdash; záporně</div>" +
 tab(["who","zápor dlouhý","zápor krátký"],
     [("I / you / we / they","have not got",A%"haven't got"),
      ("he / she / it","has not got",A%"hasn't got")], ["36%","28%","36%"]) +
 "<div class='kh'>Cvičení dole &mdash; have, has, haven't nebo hasn't?</div>" +
 ol(["I " + A%"have" + " (" + A%"'ve" + ") got two brothers.",
     "He " + A%"has" + " (" + A%"'s" + ") got a new bike.",
     "We " + A%"haven't" + " got a cat. <span class='ph'>(NOT &rarr; zápor)</span>",
     "My sister " + A%"hasn't" + " got a mobile. <span class='ph'>(NOT &rarr; zápor, a je to „ona“)</span>"]),
 "Věta 4 má <b>dvě pasti najednou</b>: je to zápor <b>a</b> třetí osoba &rarr; <b>hasn't</b>. "
 "Když řekne <i>haven't</i>, zeptej se: „kdo to je? sestra &mdash; to je she, a co patří k she?“<br>"
 "Výslovnost: <i>haven't</i> [HE-vnt] &middot; <i>hasn't</i> [HE-znt]. Rozdíl je jen <b>v</b> × <b>z</b>, "
 "a Rozárka ho neuslyší &mdash; řekni jí ho pomalu zvlášť.<br>"
 "<b>Neopravuj</b>, když řekne <i>I have a dog</i> místo <i>I've got a dog</i>. "
 "Gramaticky je to taky správně, jen se to v Projectu učí jinak. Řekni: „jde to, ale ve škole chtějí <b>have got</b>.“"
))

# ---------- 6 I've got ----------
EX.append((
 "6", "I've got / I haven't got", 7, "4 min",
 "Použití v praxi a <b>o sobě</b> &mdash; co je pravda, to si zapamatuje. "
 "Osm obrázků se jen zakroužkuje a řekne nahlas, <b>psát se budou jen tři</b>. "
 "Víc se do čtyř minut nevejde.",
 ["„U každého obrázku zakroužkuj fajfku nebo křížek &mdash; podle toho, jestli to máš.“",
  "„A hned to řekni celou větou: <b>I've got a dog.</b> nebo <b>I haven't got a dog.</b>“",
  "„Teď vyber tři a napiš je vpravo.“"],
 "<div class='kh'>Osm obrázků &mdash; věta ke každému</div>" +
 '<div class="two-col">' +
 tab(["Obrázek","Kladně","Záporně"],
     [("a dog",A%"I've got a dog.",A%"I haven't got a dog."),
      ("a cat",A%"I've got a cat.",A%"I haven't got a cat."),
      ("a mobile",A%"I've got a mobile.",A%"I haven't got a mobile."),
      ("a watch",A%"I've got a watch.",A%"I haven't got a watch.")], ["26%","37%","37%"]) +
 tab(["Obrázek","Kladně","Záporně"],
     [("a book",A%"I've got a book.",A%"I haven't got a book."),
      ("an umbrella",A%"I've got an umbrella.",A%"I haven't got an umbrella."),
      ("a house",A%"I've got a house.",A%"I haven't got a house."),
      ("a bike",A%"I've got a bike.",A%"I haven't got a bike.")], ["26%","37%","37%"]) +
 '</div>' +
 note("Po každé větě se jí zeptej <b>Really?</b> [RY-ly] a nech ji říct něco navíc &mdash; "
      "jméno psa, barvu kola. Tím se z vyplňovačky stane konverzace."),
 "<b>an</b> umbrella &mdash; jediné slovo na stránce, kde je <i>an</i>. Skoro jistě napíše <i>a umbrella</i>.<br>"
 "Pozor na pořadí v záporu: <i>I haven't got</i>, ne <s>I don't have got</s> a ne <s>I haven't a dog</s>.<br>"
 "Když chce říct víc než jeden kus (<i>I've got two dogs</i>), nech ji &mdash; je to správně "
 "a množné číslo se teprve bude učit."
))

# ---------- 7 Have you got? ----------
EX.append((
 "7", "Have you got &hellip;? &mdash; otázka a krátká odpověď", 8, "5 min",
 "Otázka se tvoří <b>prohozením</b> (You have got &rarr; Have you got?) a odpověď musí být <b>celá</b>. "
 "Poslední dvě otázky jsou o někom jiném &mdash; tam se mění na <b>Has</b>.",
 ["„Zakroužkuj fajfku nebo křížek podle toho, jak to máš.“",
  "„A teď to <b>řekni celé</b>. Ne jenom yes &mdash; <b>Yes, I have.</b>“",
  "„Poslední dvě otázky jsou o kamarádovi a o rodině. Všimni si: tam není <i>Have</i>, ale <b>Has</b>.“"],
 "<div class='kh'>Krátké odpovědi ke každé otázce</div>" +
 tab(["Otázka","Ano","Ne"],
     [("Have you got a dog?",A%"Yes, I have.",A%"No, I haven't."),
      ("Have you got a brother or a sister?",A%"Yes, I have.",A%"No, I haven't."),
      ("Have you got a mobile?",A%"Yes, I have.",A%"No, I haven't."),
      ("Have you got a favourite book?",A%"Yes, I have.",A%"No, I haven't."),
      ("Has your friend got a cat?",A%"Yes, he has."+" / "+A%"she has.",A%"No, he hasn't."+" / "+A%"she hasn't."),
      ("Has your family got a big house?",A%"Yes, it has.",A%"No, it hasn't.")],
     ["38%","31%","31%"]) +
 note("Výslovnost: <i>Yes, I have.</i> [jes aj hev] &middot; <i>No, I haven't.</i> [nou aj HE-vnt] &middot; "
      "<i>Yes, he has.</i> [jes hí hez] &middot; <i>No, she hasn't.</i> [nou ší HE-znt]"),
 "Krátká odpověď se <b>nezkracuje</b>: <i>Yes, I have.</i> &mdash; nikdy <s>Yes, I've.</s> "
 "Je to stejné pravidlo jako minule u <s>Yes, he's.</s> Na listu je to schválně přeškrtnuté.<br>"
 "Otázka 2 (<i>a brother or a sister</i>) je dlouhá &mdash; nech ji odpovědět a pak se doptej "
 "<b>Which one?</b> [vič wan] a <b>What's his / her name?</b><br>"
 "U otázky 6 je <i>your family</i> jeden celek &rarr; <b>it has</b>. Když řekne <i>they have</i>, "
 "je to pochopitelné; uznej, ale ukaž, že <i>family</i> se bere jako ono."
))

# ---------- 8 About me ----------
EX.append((
 "8", "About me &mdash; čtyři věty", 9, "3 min",
 "Samostatná produkce. První tři věty jsou o ní (<i>have got</i>), "
 "<b>čtvrtá je o kamarádovi</b> &mdash; a tam musí přepnout na <i>has got</i>. "
 "To je celý smysl tohohle cvičení.",
 ["„Čtyři věty o tobě. Piš pravdu, ne něco opsaného.“",
  "„Pozor na poslední &mdash; je o kamarádovi. Kamarád je <b>he</b> nebo <b>she</b>. A co k tomu patří?“"],
 "<div class='kh'>Vzorová řešení</div>" +
 ol(["I've got " + A%"a dog" + ". / " + A%"two brothers" + ". / " + A%"a new bike" + ".",
     "I haven't got " + A%"a cat" + ". / " + A%"a mobile" + ".",
     "My cousin's name is " + A%"Adam" + ". <span class='ph'>(jakékoli jméno)</span>",
     "My best friend " + A%"has got" + " a dog. <span class='ph'>(ne „have got“!)</span>"]) +
 "<div class='kh'>Na co se dívat při kontrole</div>" +
 tab(["Věta","Musí tam být","Proč"],
     [("1","have got / 've got","já = I"),
      ("2","haven't got","zápor, pořád já"),
      ("3","cousin's &mdash; s apostrofem","přivlastnění, z minulé hodiny"),
      ("4","<b>has got</b>","kamarád = he / she")],
     ["10%","40%","50%"]),
 "Věta 4 je ta, kvůli které tam cvičení je. <b>Skoro jistě napíše <i>have got</i></b> &mdash; "
 "je to první chyba, kterou u have got všichni dělají.<br>"
 "Neopravuj ji za ni. Zeptej se: <b>„Kamarád &mdash; to je he nebo she. A co patří k he?“</b> "
 "a nech ji opravit se samu. Oprava, kterou si řekne, drží; ta, kterou slyší, ne.<br>"
 "Věta 3 má <b>cousin's</b> s apostrofem &mdash; to je possessive ’s z minulé hodiny, "
 "ne have got. Pochval ji, když to trefí."
))

# ---------- 9 homework ----------
EX.append((
 "9", "Domácí úkol", 10, "2 min",
 "Zadání úkolu. Tři části: slovíčka, tři věty, kresba pokoje.",
 ["„Doma tři věci: šest slovíček, tři věty a nakreslit svůj pokoj.“",
  "„U kresby napiš <b>jednu větu s I'VE GOT</b> &mdash; třeba <i>I've got a big bed.</i>“"],
 "<div class='kh'>1 &mdash; slovíčka k naučení</div>" +
 tab(["Anglicky","Výslovnost","Česky"],
     [("a pet","[e pet]","domácí mazlíček"),("a mobile","[e MOU-bajl]","mobil"),
      ("an umbrella","[en am-BRE-la]","deštník"),("a watch","[e woč]","hodinky"),
      ("cousin","[KA-zn]","bratranec / sestřenice"),("Hungary","[HAN-ge-ry]","Maďarsko")],
     ["30%","34%","36%"]) +
 "<div class='kh'>2 &mdash; tři věty, vzorové řešení</div>" +
 ol(["I've got " + A%"a bike" + ".",
     "My mum has got " + A%"a red car" + ". <span class='ph'>(máma = she &rarr; HAS got)</span>",
     "I haven't got " + A%"a cat" + "."]) +
 note("<b>3 &mdash; Draw &amp; label:</b> nakreslí svůj pokoj a napíše <b>jednu větu</b> s <i>I've got</i>. "
      "Např. " + A%"I've got a big bed and a desk."),
 "Druhá věta je schválně o <b>mámě</b> &mdash; aby musela použít <b>has got</b>. "
 "Když tam napíše <i>have got</i>, je to přesně ta chyba, kterou chceme chytit; projdeš to příští hodinu.<br>"
 "<b>cousin</b> a <b>Hungary</b> jsou v úkolu znovu schválně &mdash; obojí jí minule nešlo."
))

# ---------- 10 check list ----------
EX.append((
 "10", "What I can do now &mdash; sebehodnocení", 11, "2 min",
 "Ona sama označí, co umí. Není to na body &mdash; je to <b>tvoje mapa, co vzít příště</b>. "
 "Nevybarvená hvězda = téma na pátou hodinu.",
 ["„Vybarvi hvězdu u všeho, co fakt umíš. Buď upřímná &mdash; co nevybarvíš, na to se příště podíváme.“",
  "„Co bylo dneska nejtěžší?“"],
 "<div class='kh'>Deset bodů a kde se to procvičovalo</div>" +
 tab(["Umím&hellip;","Cvičení","Když nevybarví &rarr;"],
     [("have got / has got","5","projít znovu tabulku, 5 vět"),
      ("kdy HAS a kdy HAVE","5, 8","drill: řeknu zájmeno, ona doplní tvar"),
      ("zápor haven't / hasn't got","5, 6","5 vět: udělej z toho zápor"),
      ("otázky Have you got&hellip;?","7","prohazovací drill"),
      ("krátké odpovědi Yes, I have.","7","5× otázka&ndash;odpověď nahlas"),
      ("co je COUSIN","2, 3","rodokmen znovu, pak o kamarádech"),
      ("aunt, uncle, son, daughter, grandparents","2, 3, 4","Word race doma, 1 minuta denně"),
      ("devět věcí: pet, dog, cat, mobile&hellip;","3, 4, 6","kartičky nebo Word race"),
      ("He's from Italy &ne; He's got a cat","5","10 vět: is, nebo has?"),
      ("pořád umím am / is / are","1","vrátit se o hodinu zpět")],
     ["40%","14%","46%"]) +
 note("Výsledek si <b>zapiš</b> do <i>Feedback/Rozarka/2026-10-13-jak-to-dopadlo.md</i> &mdash; "
      "podle toho se staví pátá hodina."),
 "Když vybarví všechno, ptej se dál &mdash; děti vybarvují z ostychu. Ověř aspoň dvě položky otázkou navíc.<br>"
 "Nejdůležitější řádek je <b>„kdy HAS a kdy HAVE“</b>. Když tenhle nevybarví, "
 "příští hodina začíná tam a nikde jinde."
))

# ---------- mini test ----------
EX.append((
 "&#9733;", "Mini test &mdash; 12 úkolů", 12, "5 min",
 "Kontrola, jestli dnešek sedl. Dělá to <b>sama a bez nápovědy</b> &mdash; jinak to nic nezměří.",
 ["„Teď sama. Nebudu ti radit. Dvanáct vět, do každé jedno slovo.“",
  "„Hotovo? Projdeme to spolu a spočítáme body.“"],
 "<div class='kh'>Řešení &mdash; 12 bodů</div>" +
 '<div class="two-col">' +
 tab(["Zadání","Správně"],
     [("<b class='q'>1</b> I ……… got a dog.",A%"have / 've"),
      ("<b class='q'>2</b> She ……… got a cat.",A%"has / 's"),
      ("<b class='q'>3</b> ……… you got a mobile?",A%"Have"),
      ("<b class='q'>4</b> Has he got a bike? Yes, he ……… .",A%"has"),
      ("<b class='q'>5</b> I ……… got a horse. (NOT)",A%"haven't"),
      ("<b class='q'>6</b> My mum ……… got a watch. (NOT)",A%"hasn't")], ["58%","42%"]) +
 tab(["Zadání","Správně"],
     [("<b class='q'>7</b> My aunt's son is my ……… .",A%"cousin"),
      ("<b class='q'>8</b> Grandma and Granddad are my ……… .",A%"grandparents"),
      ("<b class='q'>9</b> Hans is from ……… . (Maďarsko)",A%"Hungary"),
      ("<b class='q'>10</b> He's ……… a cat. (má)",A%"got"),
      ("<b class='q'>11</b> ……… your friend got a dog?",A%"Has"),
      ("<b class='q'>12</b> Have you got a sister? No, I ……… .",A%"haven't")], ["58%","42%"]) +
 '</div>' +
 "<div class='kh'>Hodnocení</div>" +
 tab(["Body","Co to znamená","Co s tím"],
     [("11&ndash;12","Have got sedí.","Příště můžeš jít dál."),
      ("8&ndash;10","Základ sedí, drhne třetí osoba.","Příští hodinu 10 minut na has got."),
      ("5&ndash;7","Tvar zná, ale nepoužívá jistě.","Celou příští hodinu na have got."),
      ("0&ndash;4","Nesedlo to.","Vrátit se na začátek a jet pomaleji.")],
     ["12%","44%","44%"]),
 "Body 1 a 2: uznej <b>oba tvary</b> &mdash; <i>have</i> i <i>'ve</i>, <i>has</i> i <i>'s</i>.<br>"
 "Bod 10 je chyták: <i>He's ……… a cat.</i> &mdash; doplní se <b>got</b>, protože ’s tady znamená <b>has</b>. "
 "Když napíše cokoli jiného, pravidlo z červeného rámečku jí nesedlo.<br>"
 "Body 5, 6, 12 jsou <b>zápory</b>. Bod 6 je navíc třetí osoba &rarr; <b>hasn't</b>, ne <i>haven't</i>.<br>"
 "Bod 9: <b>Hungary</b> s velkým H."
))

# ---------- caste chyby ----------
MIST = [
 ("I have got a dog, he have got a cat.", "he <b>has</b> got", "U he / she / it je vždycky HAS."),
 ("Yes, I've.", "Yes, I <b>have</b>.", "Kladná krátká odpověď se nezkracuje."),
 ("I don't have got a cat.", "I <b>haven't</b> got a cat.", "Zápor se dělá bez DO."),
 ("I haven't a dog.", "I haven't <b>got</b> a dog.", "GOT tam musí zůstat."),
 ("a umbrella", "<b>an</b> umbrella", "Před samohláskou je AN."),
 ("He's got from Italy.", "He's from Italy.", "’s = is. GOT tam nepatří."),
 ("My friend have got a bike.", "My friend <b>has</b> got", "Kamarád = he/she → has."),
 ("[KOU-sin]", "[<b>KA</b>-zn]", "Píše se ou, ale čte se A."),
 ("my cousin girl / sestřenice", "my <b>cousin</b>", "Jedno slovo pro kluka i holku."),
 ("Has you got a dog?", "<b>Have</b> you got a dog?", "You bere HAVE, ne HAS."),
]

TIME = [
 ("0:00", "1", "Hello again! + am / is / are", "3 min"),
 ("0:03", "2", "Who is a cousin? &mdash; rodokmen", "4 min"),
 ("0:07", "3", "Words for today (čtení nahlas)", "3 min"),
 ("0:10", "4", "Word race &mdash; 3 kola", "3 min"),
 ("0:13", "5", "<b>HAVE GOT</b> &mdash; tabulky + cvičení", "5 min"),
 ("0:18", "6", "I've got / I haven't got (obrázky)", "4 min"),
 ("0:22", "7", "Have you got&hellip;? + krátké odpovědi", "5 min"),
 ("0:27", "8", "About me &mdash; čtyři věty", "3 min"),
 ("0:30", "&#9733;", "Mini test &mdash; <i>když nezbude čas, zadej domů</i>", "5 min"),
]
