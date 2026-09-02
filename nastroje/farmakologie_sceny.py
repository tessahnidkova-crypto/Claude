#!/usr/bin/env python3
"""Paměťové scény ke všem 136 zkouškovým otázkám z farmakologie.

Každý zápis `S(...)` = jedna strana atlasu `SCENY.pdf`:
  misto     — věta, která scénu pojmenuje a spojí s tématem
  prostredi — kde se to odehrává (krajina, poust, more, pokoj, laborator, noc, les, hory)
  prvky     — (glyf, název, kritické, fakt); poloha se dopočítá automaticky
  past      — nejčastější omyl u téhle otázky

⚠️ **Mnemotechnika nesmí zakódovat nepravdu.** Symbol smí být přehnaný, ale
**legenda se píše odborně a doslova** — chybný hák se naučí stejně pevně jako
správný a u zkoušky vypadne jako omyl.

Přegeneruje se příkazem `python3 nastroje/gen_sceny.py`.
"""
from scenka import scenka

O = []


def S(cislo, nadpis, misto, prostredi, prvky, past=None):
    O.append((cislo, nadpis, scenka(cislo, nadpis, misto, prostredi, prvky, past)))


# ───────────────────────────────── OBECNÁ FARMAKOLOGIE ─────────────────────────

S("O1", "Farmakologie, původ a zdroje léčiv, názvy, lékopis",
  "LÉKÁRNICKÁ ZAHRADA — odsud pocházejí léky a odsud vedou dvě cesty: tam (kinetika) a zpátky (dynamika).", "krajina",
  [("🧭", "Kompas", False, "FARMAKOKINETIKA — co dělá tělo s lékem: absorpce, distribuce, metabolismus, exkrece (ADME)."),
   ("💥", "Výbuch", False, "FARMAKODYNAMIKA — co dělá lék s tělem: mechanismus účinku a vztah dávky a odpovědi."),
   ("🌿", "Bylina", False, "Zdroje rostlinné (morfin, atropin, digoxin), živočišné (heparin, inzulin), mikrobiální (peniciliny), chemická syntéza a biotechnologie (monoklonální protilátky)."),
   ("🏷️", "Tři visačky", False, "Názvy: chemický (vzorec) · generický = mezinárodní nechráněný (ibuprofen) · firemní chráněný (Brufen®)."),
   ("📕", "Červená kniha", False, "LÉKOPIS — závazný soubor požadavků na jakost léčiv; Český vychází z Evropského."),
   ("⚗️", "Lékárnický kotlík", False, "Magistraliter se připravuje v lékárně podle receptu; HVLP se vyrábí hromadně."),
   ("💊", "Hotová tableta", False, "Léčivá LÁTKA je nositel účinku, léčivý PŘÍPRAVEK je hotová forma, kterou pacient dostane.")],
  "Farmakologie zastřešuje i farmakoterapii, toxikologii a farmakovigilanci — není to jen nauka o účincích léků.")

S("O2", "Legislativa, doplňky stravy, zdravotnické prostředky, regulační orgány",
  "TRŽNICE SE TŘEMI PULTY — u každého platí jiná pravidla, a rozhoduje MECHANISMUS, ne složení.", "pokoj",
  [("⚖️", "Váhy na prvním pultu", False, "LÉČIVÝ PŘÍPRAVEK působí farmakologicky, imunologicky nebo metabolicky; musí prokázat účinnost, bezpečnost a jakost."),
   ("🥤", "Kelímek na druhém pultu", True, "DOPLNĚK STRAVY je právně potravina — účinnost dokládat nemusí, stačí ohlášení, a nesmí tvrdit, že léčí. Dozor má SZPI."),
   ("🩹", "Náplast na třetím pultu", False, "ZDRAVOTNICKÝ PROSTŘEDEK působí FYZIKÁLNĚ (výplň, implantát, obvaz) — posuzuje se shoda a riziková třída."),
   ("🏛️", "Úřední budova", False, "SÚKL registruje léčiva, stanovuje ceny a úhrady, dozoruje lékárny, povoluje klinická hodnocení a vede farmakovigilanci."),
   ("🇪🇺", "Vlajka nad tržnicí", False, "EMA vede centralizovanou registraci platnou pro celou EU."),
   ("🟦", "Modrý pruh na krabičce", True, "Omamné a psychotropní látky se předepisují na recept s modrým pruhem a mají přísnější evidenci."),
   ("🤝", "Podání ruky", False, "Klinické hodnocení musí kromě SÚKL schválit i etická komise.")],
  "Pacient rozdíl mezi lékem a doplňkem nevidí — na doplňky se proto ptej cíleně: třezalka, ginkgo a česnek mají reálné interakce.")

S("O3", "Předepisování léčivých přípravků",
  "ORDINACE SE DVĚMA PODPISY — lékař ručí za to, co předepsal, lékárník za to, co vydal.", "pokoj",
  [("✍️", "Dva podpisy pod receptem", False, "Recept je právní dokument se sdílenou odpovědností — proto musí být čitelný a úplný."),
   ("💻", "Obrazovka s eReceptem", False, "eRecept je standard: lékař ho vystaví do centrálního úložiště, pacient dostane identifikátor. Listinný recept zůstává pro výpadky."),
   ("🪪", "Průkazka pacienta", False, "Náležitosti: pacient (jméno, číslo pojištěnce) · léčivo (název, síla, forma, množství) · dávkování a způsob podání (D.S.) · lékař a pracoviště s podpisem a razítkem · datum."),
   ("🟦", "Modrý pruh", True, "Vyhrazen omamným a psychotropním látkám; přísnější evidence."),
   ("⚗️", "Třecí miska", False, "Magistraliter předpis má stavbu Rp. (recipe) — složení — M.f. (misce fiat) — D.S. (da signa)."),
   ("📅", "Kalendář na zdi", False, "Platnost běžného receptu je zpravidla 14 dní, u antibiotik kratší [⚠️ ověřit dle skript]. Opakovací recept uvádí počet opakování."),
   ("🔁", "Výměna krabiček", False, "Generická substituce — lékárník smí vydat jiný přípravek se stejnou účinnou látkou, silou a formou, pokud to lékař nezakázal a pacient souhlasí.")],
  "Před předepsáním patří anamnéza: alergie, gravidita a kojení, funkce jater a ledvin a všechny ostatní léky včetně volně prodejných.")

S("O4", "Preklinické a klinické hodnocení léčiv",
  "ŽEBŘÍK O ČTYŘECH PŘÍČKÁCH — dole myš, nahoře celý svět. Každá příčka odpovídá na jinou otázku.", "laborator",
  [("🐁", "Myš na spodní příčce", False, "PREKLINIKA in vitro a na zvířeti: farmakokinetika, farmakodynamika, toxicita (ED50, TD50, LD50), mutagenita, teratogenita, karcinogenita."),
   ("💪", "Zdravý dobrovolník", False, "FÁZE I — desítky ZDRAVÝCH: bezpečnost a snášenlivost; zahajuje se mikrodávkami s pomalou eskalací."),
   ("🧪", "Stovka zkumavek", False, "FÁZE II — stovky nemocných: hledá se účinná dávka."),
   ("👥", "Zástup lidí", False, "FÁZE III — tisíce nemocných: srovnání s dosavadní léčbou nebo placebem; na jejím základě se registruje."),
   ("🌍", "Zeměkoule nahoře", True, "FÁZE IV — po uvedení na trh, běžná populace. Teprve tady se odhalí VZÁCNÉ nežádoucí účinky, protože ve studii na tisících neměly šanci vyjít najevo."),
   ("🎲", "Kostka randomizace", False, "Zásady studie: randomizace, zaslepení (jednoduché, dvojité, trojité), kontrolní skupina, předem daný cíl, souhlas etické komise."),
   ("📋", "Kopírák", False, "Generikum účinnost neprokazuje znovu — dokládá BIOEKVIVALENCI, tedy shodný průběh hladin s originálem.")],
  "Preklinika sama nestačí: zvíře nemá stejný metabolismus ani receptory. Od objevu k registraci uplyne zpravidla 10–15 let.")

S("O5", "Způsoby aplikace léčiv, výhody a nevýhody",
  "KŘIŽOVATKA PŘED JÁTRY — hlavní otázka není „jak rychle“, ale „PROJDE TO JÁTRY?“.", "krajina",
  [("🚪", "Vrátnice u cesty", True, "PERORÁLNĚ: látka projde střevní stěnou a játry dřív, než se dostane do oběhu (first-pass). Proto se stejný lék podává ústy v mnohonásobně vyšší dávce než do žíly."),
   ("👅", "Odbočka pod jazykem", False, "SUBLINGVÁLNĚ a bukálně — vstřebání rovnou do systémového oběhu, obchází játra; proto nitroglycerin pod jazyk."),
   ("💉", "Stříkačka na cestě", True, "I.V.: okamžitý účinek a biologická dostupnost 100 % — ale podané se nedá vzít zpět."),
   ("💪", "Sval u cesty", False, "I.M. rychlé, S.C. pomalejší (inzulin, hepariny); dále intratekálně, intraartikulárně, intraoseálně. Vyžadují sterilitu a personál."),
   ("🩹", "Náplast na plotě", False, "TRANSDERMÁLNĚ — nejpomalejší nástup, ale stálá hladina po dny; po sejmutí účinek doznívá z kožního depa."),
   ("🍑", "Zadní vrátka", False, "REKTÁLNĚ — funguje při zvracení a u dětí, játra obchází jen zčásti (dolní část konečníku), vstřebávání je kolísavé."),
   ("👁️", "Oko nad krajinou", True, "„Místní“ podání neznamená „bez celkového účinku“ — timolol z očních kapek vyvolá bradykardii a bronchospasmus.")],
  "Biologická dostupnost F je podíl dávky, který se dostane nezměněný do oběhu; i.v. má z definice F = 100 %.")

S("O6", "Lékové formy — perorální a orální",
  "CUKRÁRNA S CEDULÍ NEDRTIT — co se polyká, jde dál do střeva; co se cucá, zůstává v ústech.", "pokoj",
  [("💊", "Tableta na pultu", False, "PERORÁLNÍ formy se polykají a působí až po vstřebání: tablety, potahované tablety, tobolky, granuláty, sirupy, suspenze, kapky."),
   ("🍬", "Pastilka ve sklenici", False, "ORÁLNÍ formy zůstávají v ústech: pastilky, žvýkací tablety, ústní vody, gely (per os = skrz ústa, oralis = ústní)."),
   ("🛡️", "Štít na tabletě", False, "ENTEROSOLVENTNÍ obal projde žaludkem a rozpadne se až ve střevě — chrání látku před kyselinou nebo žaludek před látkou."),
   ("⛔", "Cedule NEDRTIT", True, "Retardované formy (SR, ZOK) uvolňují látku postupně — rozdrcením se uvolní celá denní dávka najednou nebo se látka zničí. Totéž platí pro enterosolventní obal."),
   ("👅", "Jazyk pod pultem", False, "Sublingválně a bukálně se látka vstřebá rovnou do krve a obejde first-pass — nitroglycerin, buprenorfin."),
   ("🥛", "Konvička s laktózou", True, "Pomocné látky nejsou neutrální: laktóza vadí při intoleranci, barviva mohou vyvolat alergii, cukr v sirupech je při dlouhodobé léčbě rizikový."),
   ("⏳", "Rozpouštějící se kostka", False, "Rozpad a rozpuštění předchází vstřebání — u málo rozpustných léčiv je rychlost rozpouštění krokem určujícím nástup účinku.")],
  "Šumivé a orodispergovatelné tablety nástup urychlují, protože přeskakují fázi rozpadu tuhé lékové formy.")

S("O7", "Lékové formy — parenterální a dermatologika",
  "STERILNÍ SÁL A VEDLE NĚJ MASTIČKÁŘSKÝ PULT — co obchází bariéry, musí být čisté.", "laborator",
  [("🧼", "Mýdlo a rouška", False, "Parenterální přípravek obchází kůži i sliznici, proto musí být STERILNÍ, APYROGENNÍ, IZOTONICKÝ, IZOHYDRICKÝ a bez mechanických nečistot."),
   ("🩸", "Krevní řečiště", False, "Rychlost účinku sleduje prokrvení: i.v. okamžitě a se 100% dostupností · i.m. rychle · s.c. pomaleji · depotní formy a náplasti nejpomaleji, ale působí dny až měsíce."),
   ("🚫", "Přeškrtnutá kalná lahvička", True, "SUSPENZE A EMULZE SE NIKDY NEPODÁVAJÍ I.V. — hrozí embolizace."),
   ("⚖️", "Váhy výhod a nevýhod", False, "Výhody: jistá dostupnost, přesné dávkování, použitelné u zvracení a bezvědomí. Nevýhody: bolestivost, riziko infekce a embolie, nutný personál a NEVRATNOST podání."),
   ("🧴", "Řada kelímků", False, "Dermatologika: mast (tučný základ, největší průnik, na suchou kůži), krém (voda i tuk), gel (vodný, chladí), pasta, zásyp, roztok, náplast. Průnik zvyšuje okluze."),
   ("⚠️", "Ztenčená kůže", True, "Lokální kortikoidy dlouhodobě způsobí atrofii kůže a strie — na obličej a do záhybů jen slabé přípravky a krátce, protože se tam vstřebávají nejvíc."),
   ("🩹", "Náplast na paži", False, "Transdermální náplast obchází játra a udrží stálou hladinu po dny (fentanyl, nikotin, estrogeny).")],
  "Depotní a implantabilní formy působí týdny až měsíce — výhodou je adherence, nevýhodou to, že se při nežádoucí reakci nedají odstranit.")

S("O8", "Lékové formy — oční, ušní, nosní, rektalia, vaginalia, inhalanda",
  "ORDINACE SE VŠEMI OTVORY TĚLA — a nade všemi visí cedule: MÍSTNÍ NENÍ JEN MÍSTNÍ.", "pokoj",
  [("👁️", "Oční kapky", True, "Musí být sterilní a izotonické, po otevření omezená použitelnost. TIMOLOL z kapek vyvolá bradykardii a bronchospasmus; vstřebání sníží stisknutí vnitřního koutku po nakapání."),
   ("👃", "Nosní sprej", True, "Dekongescencia (xylometazolin) jen 5–7 DNÍ, jinak vzniká rhinitis medicamentosa. Nosní cestou se podává i desmopresin a sumatriptan k celkovému účinku."),
   ("👂", "Ušní kapátko", True, "Ušní kapky se nesmí podat při perforaci bubínku."),
   ("🫁", "Inhalátor s nástavcem", False, "Aerosolový dávkovač, práškový inhalátor, nebulizace. Rozhoduje TECHNIKA inhalace; nástavec zlepší depozici a sníží orofaryngeální kandidózu a chrapot po inhalačním kortikoidu."),
   ("🍑", "Čípek", False, "Rektalia obcházejí játra jen z dolní části konečníku, vstřebávání je kolísavé; hodí se u zvracení, u dětí a v bezvědomí (diazepam u křečí)."),
   ("🌸", "Vaginální globule", False, "Slouží hlavně k místní léčbě (antimykotika, estrogeny), ale i odsud se látka částečně vstřebává."),
   ("📢", "Cedule nade vším", True, "Společné pravidlo: všechny tyto formy se vstřebávají a mohou působit celkově.")],
  "Nosní a bukální sliznice jsou dobře prokrvené a first-pass obcházejí — vstřebání odsud může být rychlejší než ze střeva.")

S("O9", "Komunikace, adherence, compliance, placebo a nocebo",
  "ČEKÁRNA, KDE SLOVA MAJÍ DÁVKU — co lékař řekne, má nástup, účinek i nežádoucí účinky.", "pokoj",
  [("👂", "Naslouchající ucho", False, "COMPLIANCE — míra, do jaké pacient dodržuje pokyny; pasivní pojetí."),
   ("🤝", "Podání ruky", False, "ADHERENCE — pacient se na plánu podílel; KONKORDANCE je společné rozhodnutí lékaře a pacienta. Dnes se preferuje adherence, protože zdůrazňuje spoluodpovědnost."),
   ("✨", "Jiskra nad hlavou", False, "PLACEBO — očekávané zlepšení; má neurobiologický podklad (endogenní opioidy, dopamin), není „vymyšlené“ a zesiluje účinek každého skutečného léku."),
   ("🌩️", "Mrak s bleskem", True, "NOCEBO — očekávaná škoda; nepříznivé věty a příbalový leták vyvolají potíž. Odsud časté vysazení statinů a antidepresiv."),
   ("💊", "Hromada krabiček", True, "Nejčastější příčina selhání léčby není špatný lék, ale NEBRANÝ lék: složitý režim, mnoho tablet, nežádoucí účinky a obavy z nich, cena, nepochopení, nedůvěra."),
   ("1️⃣", "Jedna tableta denně", False, "Zlepší to fixní kombinace (méně tablet), dávkování 1× denně, srozumitelné vysvětlení a kontrola."),
   ("🗣️", "Mluvící lékař", False, "Formulace lékaře je sama o sobě účinná látka s vlastní dávkou — proto se způsob sdělení plánuje stejně jako dávka.")],
  "Placebo se neomezuje na placebo tablety — každý účinný lék nese i placebovou složku, a ta se sčítá s jeho farmakologickým účinkem.")

S("O10", "Přechod látek biologickými membránami",
  "TUKOVÁ ZEĎ S JEDNOSMĚRNOU PASTÍ — projde jen ten, kdo je mastný a nenabitý.", "hory",
  [("🧈", "Máslová zeď", False, "Membrána je lipidová dvojvrstva — projde jen látka LIPOFILNÍ a NENABITÁ; ionizovaná forma neprojde."),
   ("🚶", "Chodec po svahu", False, "PROSTÁ DIFUZE — po koncentračním spádu, bez energie a bez přenašeče; hlavní mechanismus u většiny léčiv."),
   ("🔋", "Baterie u brány", False, "AKTIVNÍ TRANSPORT — proti spádu, spotřebuje ATP, je saturovatelný (P-glykoprotein léčiva aktivně vypuzuje z buňky). Facilitovaná difuze jde přenašečem, ale po spádu a bez energie."),
   ("🪤", "Past za zdí", True, "IONTOVÁ PAST: látka projde v nenabité formě, na druhé straně se při jiném pH nabije a zpět už neprojde — hromadí se. Proto alkalizace moči urychlí vyloučení salicylátů."),
   ("🧠", "Hlídaná brána do mozku", False, "Hematoencefalická bariéra — těsné spoje a P-glykoprotein. Zánět ji zpropustní: penicilin proniká do CNS jen při meningitidě."),
   ("🤰", "Placenta", True, "Placentární bariéra je PROPUSTNĚJŠÍ, než se obvykle čeká — většina léčiv jí projde."),
   ("💉", "Anestetikum v zánětu", True, "V kyselém zánětlivém prostředí převáží nabitá forma lokálního anestetika, která neprojde k sodíkovému kanálu — proto tam nezabírá.")],
  "Krev–varle a krev–sítnice jsou další bariéry; naopak zánět propustnost bariér obecně zvyšuje, což mění dávkování.")

S("O11", "Základní farmakokinetické parametry a procesy",
  "ČTYŘI STANICE JEDNÉ TRATĚ — A, D, M, E. Kdo si splete eliminaci s exkrecí, vystoupí na špatné.", "krajina",
  [("🅰️", "První stanice A", False, "ABSORPCE — vstup do krve; její rozsah vyjadřuje biologická dostupnost F (i.v. = 100 %)."),
   ("🅳", "Druhá stanice D", False, "DISTRIBUCE — rozvod do tkání; popisuje ji distribuční objem Vd (poměr dávky k plazmatické koncentraci)."),
   ("🅼", "Třetí stanice M", False, "METABOLISMUS — přeměna, hlavně v játrech; I. fáze (oxidace, redukce, hydrolýza) a II. fáze (konjugace)."),
   ("🅴", "Čtvrtá stanice E", False, "EXKRECE — vyloučení, hlavně ledvinami; dále žlučí, plícemi, mlékem."),
   ("➕", "Spojka M + E", True, "ELIMINACE = metabolismus PLUS exkrece. Není totéž co vylučování — to je jen její část."),
   ("🚰", "Vodárna", False, "CLEARANCE — objem krve zcela očištěný za jednotku času; sčítá se renální a jaterní."),
   ("½", "Půlená cedule", False, "Biologický poločas — doba poklesu na polovinu. Ustálený stav nastane za 4–5 poločasů a stejně dlouho trvá vymizení.")],
  "Vysoké Vd znamená, že látka sedí ve tkáních, ne v krvi — proto ji hemodialýza neodstraní (digoxin, antidepresiva).")

S("O12", "Procesy nultého a prvního řádu, saturační kinetika",
  "DVĚ PILY NA DŘEVO — jedna ubírá vždycky POLOVINU hromady, druhá vždycky STEJNÝCH PĚT POLEN.", "les",
  [("📉", "Klesající křivka", False, "KINETIKA PRVNÍHO ŘÁDU — odbourává se konstantní PODÍL za čas (polovina za poločas). Platí pro naprostou většinu léčiv, protože enzymy mají kapacitní rezervu."),
   ("⏳", "Přesýpací hodiny", False, "KINETIKA NULTÉHO ŘÁDU — enzym je nasycený, odbourává konstantní MNOŽSTVÍ za čas bez ohledu na koncentraci. Pokles je lineární a poločas ztrácí smysl."),
   ("🍺", "Korbel piva", True, "Ethanol se odbourává řádově 0,1–0,15 ‰ za hodinu, vždy stejně — proto NELZE počítat „za dva poločasy bude polovina“ a rychlost nejde urychlit."),
   ("🔀", "Výhybka", False, "Michaelisova–Mentenové (saturační) kinetika je přechod mezi obojím: při nízké koncentraci první řád, po nasycení enzymu nultý."),
   ("⚠️", "Přetékající hrnec", True, "U saturačního léčiva stačí malé zvýšení dávky a hladina vyskočí do toxického pásma — fenytoin (nystagmus, ataxie, zmatenost), salicyláty, theofylin. Proto se měří hladiny."),
   ("4️⃣", "Čtyři zářezy", False, "Ustálený stav nastane za 4–5 poločasů a stejně dlouho trvá vymizení po vysazení."),
   ("🚀", "Nasycovací dávka", False, "U dlouhého poločasu se čekání zkracuje nasycovací dávkou.")],
  "Poločas má smysl jen u kinetiky prvního řádu — u nultého řádu se mění s koncentrací, a proto se neuvádí.")
