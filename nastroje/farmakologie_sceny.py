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

S("O13", "Absorpce, Batemanova funkce, biologická dostupnost, AUC",
  "PŘETAHOVANÁ NA VRCHOLU KOPCE — Cmax je REMÍZA mezi vstřebáváním a eliminací.", "hory",
  [("⚖️", "Vyrovnané váhy", True, "Cmax není konec vstřebávání — je to okamžik, kdy se rychlost vstupu vyrovná rychlosti eliminace. Vstřebávání pokračuje i po něm, jen ho eliminace převáží."),
   ("📈", "Křivka přes kopec", False, "BATEMANOVA FUNKCE popisuje průběh koncentrace po jednorázovém perorálním podání: vzestupná fáze (převažuje absorpce), vrchol, sestupná fáze (převažuje eliminace)."),
   ("🧮", "Počítadlo plochy", False, "AUC — plocha pod křivkou = celková expozice organismu; podle ní se srovnává originál s generikem (bioekvivalence)."),
   ("🚪", "Vrátnice s výběrčím", False, "Biologická dostupnost F = podíl dávky, který se dostane NEZMĚNĚNÝ do systémového oběhu; snižuje ji neúplné vstřebání a first-pass metabolismus."),
   ("⏱️", "Stopky", False, "tmax vypovídá o RYCHLOSTI vstřebávání, Cmax a AUC o jeho ROZSAHU."),
   ("🥛", "Sklenice mléka", True, "Vstřebání ovlivní léková forma, rozpustnost, pH, jídlo, motilita a prokrvení; antacida, železo a vápník váží tetracykliny a chinolony."),
   ("📋", "Dvě shodné křivky", False, "Generikum musí mít shodné AUC i Cmax v předepsaném rozmezí — proto se u něj nezkoumá znovu účinnost.")],
  "Vyšší Cmax při stejném AUC znamená rychlejší, ale krátkodobější účinek — proto retardovaná forma snižuje Cmax, aniž by měnila celkovou expozici.")

S("O14", "Distribuce, distribuční objem, redistribuce, vazba na bílkoviny, bariéry",
  "SKLAD S VELKOU NÁDOBOU — Vd je ZDÁNLIVÝ objem, ne skutečný. Velké číslo znamená: lék není v krvi, sedí ve tkáních.", "laborator",
  [("🫙", "Obří nádoba", False, "Vd = dávka ÷ plazmatická koncentrace. Je to počítaná veličina, ne anatomický prostor — může mnohonásobně převýšit objem těla."),
   ("🛋️", "Gauč ve skladu", True, "Vysoké Vd = lék uložený ve tkáních (tuk, sval), v krvi ho je málo — proto ho HEMODIALÝZA NEODSTRANÍ (digoxin, antidepresiva)."),
   ("🔗", "Řetěz k albuminu", True, "Účinná je jen VOLNÁ frakce. Albumin váže kyselé látky (warfarin, fenytoin), OROSOMUKOID (kyselý α1-glykoprotein) zásadité. Při hypoalbuminemii stoupá volná frakce a s ní účinek i toxicita."),
   ("🧠", "Brána do mozku", False, "Hematoencefalická bariéra — těsné spoje a P-glykoprotein; propustí jen lipofilní a nenabité látky."),
   ("🤰", "Placenta", True, "Placentární bariéra je propustnější, než se čeká — proto se u gravidity vždy ptáme, co projde k plodu."),
   ("💤", "Usínající pacient", False, "REDISTRIBUCE: thiopental uspí rychle (jde do mozku) a probudí rychle (přesune se do svalu a tuku) — konec účinku dělá PŘESUN, ne eliminace."),
   ("⚔️", "Vytěsnění z vazby", False, "Sulfonamidy vytěsní warfarin z albuminu; samo o sobě bývá klinicky přechodné — nebezpečné je, když se přidá i útlum metabolismu.")],
  "Hydrofilní látky mají nízké Vd (zůstávají v krvi a extracelulárně), lipofilní vysoké — proto se u obézního pacienta liší dávkování podle typu léčiva.")

S("O15", "Eliminace, poločas, fáze α a β, eliminační konstanta, clearance",
  "VODÁRNA SE DVĚMA SPÁDY — nejdřív strmý (rozvod), pak pozvolný (skutečná eliminace).", "krajina",
  [("½", "Cedule s polovinou", False, "Biologický poločas t½ — doba, za kterou klesne koncentrace na polovinu. U kinetiky prvního řádu je konstantní a nezávisí na dávce."),
   ("🅰️", "Strmý spád α", False, "FÁZE α — po i.v. podání klesá koncentrace nejprve strmě, protože se látka rozvádí do tkání (distribuce)."),
   ("🅱️", "Pozvolný spád β", False, "FÁZE β — pozvolný pokles odpovídá skutečné eliminaci; poločas se počítá právě z ní."),
   ("🚰", "Kohoutek clearance", False, "CL = objem plazmy zcela očištěný za jednotku času; CL = CLren + CLhep. Vztah: t½ = 0,693 × Vd ÷ CL."),
   ("4️⃣", "Čtyři zářezy", True, "Za 4–5 poločasů se dosáhne ustáleného stavu — a stejně dlouho trvá vymizení po vysazení."),
   ("📐", "Konstanta kel", False, "Eliminační konstanta kel — podíl látky odstraněný za jednotku času; t½ = 0,693 ÷ kel."),
   ("🫘", "Ledvina a játra", True, "Poločas roste, když klesne clearance (jaterní nebo renální selhání) NEBO když stoupne Vd — proto nestačí sledovat jen ledviny.")],
  "Krátký poločas neznamená krátký účinek: ireverzibilní inhibitory (aspirin na COX-1, omeprazol na protonovou pumpu) působí, dokud se neobnoví enzym.")

S("O16", "Dávkovací režim, kumulace, kumulační index",
  "SUD, DO KTERÉHO PŘITÉKÁ RYCHLEJI, NEŽ ODTÉKÁ — tak vzniká kumulace.", "krajina",
  [("🛢️", "Plnící se sud", True, "KUMULACE nastane, je-li dávkovací interval kratší než doba potřebná k eliminaci; hladina se ustálí po 4–5 poločasech."),
   ("🚀", "Startovací raketa", False, "NASYCOVACÍ dávka = Vd × cílová koncentrace. Podává se, když je poločas dlouhý a nelze čekat 4–5 poločasů na účinek."),
   ("🔄", "Doplňovací konev", False, "UDRŽOVACÍ dávka = CL × cílová koncentrace × interval. Nahrazuje to, co se za interval vyloučí."),
   ("📊", "Plochá vlnovka", False, "Krátký interval a malé dávky = plochá, stabilní hladina. Dlouhý interval a velké dávky = větší kolísání mezi vrcholem a údolím."),
   ("⚠️", "Přetékající okraj", True, "Kolísání je nebezpečné u léčiv s úzkým terapeutickým oknem — proto se u nich volí kratší interval."),
   ("📈", "Kumulační index", False, "Poměr koncentrace v ustáleném stavu k té po první dávce; udává, kolikrát se hladina nahromadí."),
   ("🫘", "Zúžený odtok", True, "Při renální insuficienci se krátí UDRŽOVACÍ dávka (závisí na clearance), ale nasycovací zůstává stejná (závisí na Vd).")],
  "Nasycovací dávka se řídí distribučním objemem, udržovací clearance — proto se u renálního selhání mění jen jedna z nich.")

S("O17", "Biotransformace léčiv, fáze, příklady",
  "DÍLNA VE DVOU KROCÍCH — nejdřív KLADIVO rozbije, pak ŠTÍTKOVAČ přilepí velkou vodorozpustnou visačku.", "laborator",
  [("🔨", "Kladivo I. fáze", False, "I. FÁZE — oxidace (hlavně cytochromy P450, nejvíc CYP3A4), redukce, hydrolýza. Vzniká reaktivnější metabolit s odhalenou funkční skupinou."),
   ("🏷️", "Štítkovač II. fáze", False, "II. FÁZE — konjugace: glukuronidace, sulfatace, acetylace, methylace, vazba na glutathion. Produkt je velký, polární a snadno vyloučitelný."),
   ("💧", "Kapka vody", False, "Smyslem je změnit lipofilní látku na hydrofilní — jinak by se v ledvinách stále zpětně vstřebávala."),
   ("⚡", "Jiskra aktivace", True, "PROLÉČIVO se aktivuje až metabolismem: kodein → morfin (CYP2D6), enalapril → enalaprilát, cyklofosfamid, klopidogrel."),
   ("☠️", "Toxický metabolit", True, "Metabolismus může vytvořit i jed: paracetamol → NAPQI, methanol → kyselina mravenčí („letální syntéza“)."),
   ("👶", "Novorozenec", True, "Nezralá glukuronidace u novorozence — odtud gray baby syndrom po chloramfenikolu."),
   ("🏭", "Jiná pracoviště", False, "Kromě jater i střevní stěna, plíce, ledviny a plazma (esterázy). U starších klesá hlavně I. fáze, II. zůstává poměrně zachovaná.")],
  "Metabolit není vždy neúčinný — může být účinnější než původní látka, stejně toxický, nebo teprve toxický. Proto se sleduje osud metabolitu, ne jen léčiva.")

S("O18", "Úloha jater v eliminaci léčiv, first-pass efekt",
  "MĚSTSKÁ BRÁNA S CELNICÍ — všechno ze střeva projde nejdřív játry a zaplatí clo.", "pokoj",
  [("🚪", "Celnice u brány", True, "Vše vstřebané ze střeva projde portální žílou JÁTRY dřív, než se dostane do systémového oběhu — first-pass efekt."),
   ("📉", "Zmenšená zásilka", False, "Silný first-pass mají nitroglycerin, propranolol, morfin, verapamil, lidokain — proto se nitroglycerin podává sublingválně a lidokain se ústy nepodává vůbec."),
   ("🔁", "Kruhová cesta", False, "ENTEROHEPATÁLNÍ OBĚH: látka se vyloučí žlučí, ve střevě se uvolní a znovu vstřebá — prodlužuje účinek (kontraceptiva; proto mohou antibiotika jejich účinnost snížit)."),
   ("🫀", "Pumpa u brány", True, "U léčiv s VYSOKOU jaterní extrakcí limituje eliminaci PRŮTOK játry — při srdečním selhání a šoku hladiny stoupají."),
   ("⚗️", "Enzymová dílna", False, "U NÍZKÉ extrakce rozhoduje enzymatická kapacita a vazba na bílkoviny, nikoli průtok."),
   ("🩹", "Objízdná trasa", False, "Játra obcházejí sublingvální, bukální, transdermální a parenterální podání; rektální jen zčásti."),
   ("🧪", "Nízký albumin", True, "Při jaterním selhání klesá metabolismus i tvorba albuminu, roste volná frakce a zkratový oběh obchází játra — dávky se snižují.")],
  "Perorální dávka bývá mnohonásobně vyšší než nitrožilní právě kvůli first-pass efektu — záměna cest podání proto může znamenat předávkování.")

S("O19", "Inhibice a indukce enzymů léčivy, klinický význam",
  "TOVÁRNA A ZÁVORA — závora spadne hned, ale novou halu se stavěl týden.", "laborator",
  [("🛑", "Spadlá závora", True, "INHIBICE je RYCHLÁ (hodiny až dny): hladina druhého léčiva stoupá a hrozí TOXICITA."),
   ("🏭", "Rostoucí továrna", True, "INDUKCE je POMALÁ (dny až týdny, protože se musí nasyntetizovat nový enzym) a stejně dlouho odeznívá: hladina klesá a LÉČBA SELŽE."),
   ("🍇", "Grapefruit", False, "Inhibitory: grapefruitová šťáva, azolová antimykotika, makrolidy (erythromycin, klarithromycin — nikoli azithromycin), ciprofloxacin, verapamil, amiodaron, ritonavir."),
   ("🔥", "Oheň pod kotlem", False, "Induktory: rifampicin, karbamazepin, fenytoin, fenobarbital, třezalka tečkovaná; chronicky alkohol a kouření (CYP1A2)."),
   ("💊", "Selhávající antikoncepce", True, "Rifampicin sníží účinnost hormonální kontracepce, warfarinu a antiretrovirotik."),
   ("💪", "Bolavý sval", True, "Klarithromycin se statinem zvýší riziko rabdomyolýzy."),
   ("🔀", "Obrácená šipka", True, "U PROLÉČIVA je to obráceně: inhibitor CYP2D6 (fluoxetin, paroxetin) SNÍŽÍ účinek kodeinu a klopidogrelu, protože zabrání jejich aktivaci.")],
  "Interakce nemizí okamžitě po vysazení induktoru — enzym se odbourává týdny, takže hladina druhého léčiva pak může naopak vyskočit.")

S("O20", "Vylučování léčiv renální a extrarenální",
  "ČISTIČKA SE TŘEMI KROKY — filtruje, dopouští a část zase nasává zpátky.", "more",
  [("🫧", "Filtrační síto", False, "GLOMERULÁRNÍ FILTRACE — projde jen VOLNÁ (nenavázaná) frakce; látka vázaná na albumin se nefiltruje."),
   ("➡️", "Boční přítok", False, "TUBULÁRNÍ SEKRECE je aktivní transport se společnými přenašeči — proto probenecid zpomaluje vylučování penicilinu (soupeří o týž přenašeč)."),
   ("↩️", "Zpětné nasávání", True, "ZPĚTNÁ RESORPCE: lipofilní a nenabité látky se z tubulu vstřebávají zpět. Alkalizace moči bikarbonátem urychlí vyloučení kyselých látek (salicyláty, barbituráty)."),
   ("💨", "Výdech", False, "Extrarenálně: plícemi (inhalační anestetika, ethanol — odtud dechová zkouška)."),
   ("🟡", "Žlučovod", False, "Žlučí a stolicí, s možností enterohepatálního oběhu."),
   ("🍼", "Mateřské mléko", True, "Do mléka přechází nejspíš látka lipofilní, málo vázaná na bílkoviny a zásaditá — proto se u kojící ptáme na každý lék."),
   ("🫘", "Zúžená ledvina", True, "Dávky léčiv vylučovaných ledvinami se snižují podle clearance kreatininu — aminoglykosidy, digoxin, metformin, lithium, mnohá antibiotika.")],
  "Vyloučit se dá jen látka vodorozpustná — proto biotransformace předchází exkreci; lipofilní látka by se v tubulu jen stále vstřebávala zpět.")

S("O21", "Účinek léčiv obecně, způsob účinku na molekulární úrovni",
  "STŘELNICE A VEDLE NÍ HROMADA SOLI — buď se trefíš do terče, nebo prostě zabereš místo.", "krajina",
  [("🎯", "Terč", False, "SPECIFICKÝ účinek — vazba na cílovou strukturu: receptor, enzym, iontový kanál, přenašeč nebo nukleovou kyselinu. Je strukturně závislý a nasytitelný."),
   ("🧂", "Hromada soli", False, "NESPECIFICKÝ účinek — fyzikálně-chemický, bez cílové struktury: antacida neutralizují kyselinu, osmotická projímadla táhnou vodu, aktivní uhlí adsorbuje."),
   ("🔓", "Klíč otvírá zámek", False, "AGONISTA se váže a receptor AKTIVUJE (má afinitu i vnitřní aktivitu)."),
   ("🔒", "Klíč v zámku bez otočení", False, "ANTAGONISTA se váže, ale neaktivuje (má jen afinitu) — brání navázání agonisty."),
   ("⚗️", "Enzym pod lupou", False, "Enzymy jako cíl: statiny na HMG-CoA-reduktázu, ACE inhibitory, inhibitory protonové pumpy."),
   ("🚪", "Iontový kanál", False, "Kanály a přenašeče: lokální anestetika na sodíkové kanály, blokátory kalciových kanálů, SSRI na serotoninový transportér."),
   ("🧬", "Šroubovice DNA", False, "Nukleové kyseliny jako cíl: cytostatika, chinolony (topoizomeráza), rifampicin (RNA-polymeráza).")],
  "Lék nevytváří novou funkci — jen zesiluje nebo zeslabuje děj, který v těle už probíhá. Proto nemá smysl čekat účinek tam, kde cílová struktura chybí.")

S("O22", "Specifický účinek, cílové struktury, receptorová teorie, typy receptorů",
  "ZÁMEČNICTVÍ SE TŘEMI RYCHLOSTMI — milisekundy, sekundy, hodiny.", "pokoj",
  [("🧲", "Magnet", False, "AFINITA — jak pevně se ligand váže; určuje potřebnou koncentraci."),
   ("⚡", "Blesk", False, "VNITŘNÍ AKTIVITA — co se po navázání stane. Plný agonista 1, parciální mezi 0 a 1 (buprenorfin), antagonista 0, inverzní agonista pod 0 (H1-antihistaminika)."),
   ("🚪", "Rychlé dveře", False, "IONOTROPNÍ receptory jsou samy iontovým kanálem — účinek za MILISEKUNDY: nikotinový acetylcholinový, GABA-A, NMDA."),
   ("📞", "Telefon s ústřednou", False, "METABOTROPNÍ receptory jdou přes G-protein a druhého posla — účinek za SEKUNDY: muskarinové, adrenergní, opioidní."),
   ("🧬", "Jádro buňky", False, "NITROBUNĚČNÉ (jaderné) receptory mění přepis genů — účinek za HODINY až DNY: kortikosteroidy, hormony štítné žlázy, pohlavní hormony."),
   ("⚔️", "Přetlačovaná o zámek", False, "KOMPETITIVNÍ antagonismus je překonatelný vyšší dávkou agonisty (posun křivky doprava); NEKOMPETITIVNÍ nepřekonatelný (snižuje maximum)."),
   ("📉", "Ubývající zámky", True, "DOWN-REGULACE při trvalé stimulaci vysvětluje toleranci; UP-REGULACE při dlouhé blokádě vysvětluje rebound po náhlém vysazení β-blokátoru.")],
  "Pomalý nástup kortikoidů není vlastnost lékové formy, ale mechanismu — musí proběhnout přepis genů a syntéza bílkovin.")

S("O23", "Dávka a účinek, terapeutický index, terapeutické okno, riziko, NNT",
  "ÚZKÉ OKNO NAD PROPASTÍ — pod ním „nefunguje“, nad ním „škodí“.", "hory",
  [("🪟", "Úzké okno", False, "TERAPEUTICKÉ OKNO — rozmezí koncentrací mezi minimální účinnou a toxickou."),
   ("📏", "Pravítko", False, "TERAPEUTICKÝ INDEX TI = TD50 ÷ ED50 (u zvířat LD50 ÷ ED50). ED50 = dávka účinná u poloviny, TD50 = toxická u poloviny, LD50 = smrtelná pro polovinu."),
   ("🩺", "Fonendoskop a odběr", True, "Úzký index mají digoxin, warfarin, theofylin, lithium, fenytoin, aminoglykosidy, cyklosporin — u nich se MĚŘÍ plazmatické hladiny."),
   ("🔢", "Číslice NNT", False, "NNT — kolik pacientů je třeba léčit, aby se u jednoho zabránilo příhodě; nízké NNT = účinná léčba. Obdobně NNH pro poškození."),
   ("📈", "Esovitá křivka", False, "Vztah dávky a účinku je sigmoidní (v logaritmickém měřítku)."),
   ("💪", "Silák", False, "ÚČINNOST (efficacy) = jak vysokého maxima lék dosáhne."),
   ("🐜", "Malá tableta", True, "POTENCE = jak malá dávka k tomu stačí. Potentnější lék NENÍ lepší lék — rozhoduje maximální účinek a bezpečnost.")],
  "Riziko se vždy váží proti prospěchu: u onkologické léčby se přijímá terapeutický index, který by u léku na rýmu byl nepřijatelný.")

S("O24", "Vlivy působící na kinetiku a dynamiku léčiv",
  "STEJNÁ DÁVKA, SEDM RŮZNÝCH LIDÍ — a u každého jiný výsledek.", "pokoj",
  [("👶", "Novorozenec", True, "Nezralá glukuronidace, vyšší podíl tělesné vody, nižší vazba na bílkoviny a nezralá glomerulární filtrace."),
   ("👵", "Seniorka", True, "Nižší glomerulární filtrace, nižší albumin, méně svaloviny a více tuku (lipofilní léčiva se hromadí), vyšší citlivost CNS."),
   ("🫘", "Ledvina a játra", False, "Jaterní selhání snižuje metabolismus a tvorbu albuminu; renální insuficience zpomaluje vylučování. U obojího se dávky snižují."),
   ("🧬", "Šroubovice", False, "Polymorfismus CYP2D6, CYP2C9, CYP2C19, NAT2, TPMT rozhoduje, zda je člověk pomalý, nebo ultrarychlý metabolizátor."),
   ("🍽️", "Talíř s jídlem", False, "Jídlo mění vstřebávání (mléko a antacida váží tetracykliny), grapefruit inhibuje CYP3A4, kouření indukuje CYP1A2 (theofylin, klozapin, olanzapin)."),
   ("🤰", "Těhotná", False, "Roste objem distribuce a glomerulární filtrace, klesá albumin — a přibývá otázka, co projde placentou."),
   ("⚡", "Změněná citlivost", True, "Mění se i DYNAMIKA: u seniorů vyšší citlivost na benzodiazepiny a opioidy, při hypokalemii vyšší toxicita digoxinu.")],
  "Kinetika i dynamika se mění současně — proto nestačí přepočítat dávku podle hmotnosti, ale je nutné počítat i s jinou odpovědí cílové struktury.")

S("O25", "Lékové interakce",
  "PŘETAHOVANÁ NA DVOU LANECH — na jednom se pere o hladinu, na druhém o účinek.", "krajina",
  [("🧪", "Lano kinetické", False, "FARMAKOKINETICKÉ interakce: vstřebávání (antacida a železo váží tetracykliny a chinolony), vazba na bílkoviny, metabolismus (inhibice a indukce CYP450), vylučování (probenecid a penicilin)."),
   ("🤼", "Lano dynamické", False, "FARMAKODYNAMICKÉ interakce: synergie (alkohol + benzodiazepiny = útlum dechu; ACE inhibitor + kalium šetřící diuretikum = hyperkalemie) nebo antagonismus (β-blokátor ruší β2-agonistu u astmatu)."),
   ("🍇", "Grapefruit", True, "Inhibuje střevní CYP3A4 → prudce zvýší hladinu statinů, blokátorů kalciových kanálů a imunosupresiv."),
   ("🌼", "Třezalka", True, "Silný induktor CYP3A4 a P-glykoproteinu → sníží účinnost kontracepce, warfarinu, cyklosporinu, digoxinu a antiretrovirotik."),
   ("💊", "Warfarin uprostřed", True, "Nejrizikovější dvojice: warfarin s čímkoli · statin s makrolidem nebo azolem · NSA s antikoagulanciem."),
   ("💓", "Prodloužené QT", True, "Látky prodlužující QT se sčítají: antiarytmika III. třídy, makrolidy, chinolony, antipsychotika, ondansetron."),
   ("🛒", "Nákupní taška", True, "Nejvíc interakcí nevzniká z léků na předpis, ale z toho, co pacient nehlásí: volně prodejná NSA, doplňky stravy a bylinky.")],
  "Serotonergní léčiva se také sčítají — SSRI, IMAO, tramadol, triptany a linezolid mohou spolu vyvolat serotoninový syndrom.")
