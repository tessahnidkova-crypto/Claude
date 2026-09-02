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

S("O26", "Farmakogenetika, genetický polymorfismus",
  "ZÁVOD ŽELVY A ZAJÍCE — stejná dávka, ale jeden ji odbourává pomalu a druhý bleskem.", "les",
  [("🐢", "Želva", True, "POMALÝ metabolizátor odbourává léčivo pomalu — hladina stoupá a hrozí TOXICITA (CYP2D6 a antidepresiva, CYP2C9 a warfarin)."),
   ("🐇", "Zajíc", True, "ULTRARYCHLÝ metabolizátor odbourá léčivo dřív, než stačí zabrat — LÉČBA SELHÁVÁ."),
   ("🔀", "Obrácená cedule", True, "U PROLÉČIVA je to naopak: ultrarychlý CYP2D6 vytvoří z kodeinu nebezpečně mnoho morfinu, pomalý nemá z kodeinu ani z klopidogrelu žádný účinek."),
   ("🧾", "Laboratorní výsledek", False, "Testuje se HLA-B*5701 před abakavirem, HLA-B*5801 před allopurinolem, TPMT před azathioprinem a 6-merkaptopurinem, G6PD před primachinem a sulfonamidy."),
   ("🩸", "Prasklý erytrocyt", True, "Deficit G6PD vede k HEMOLÝZE po primachinu, sulfonamidech a nitrofurantoinu."),
   ("🔥", "Horečka na sále", True, "MALIGNÍ HYPERTERMIE po sukcinylcholinu a halogenovaných anesteticích — geneticky podmíněná idiosynkrazie; antidotem dantrolen."),
   ("💊", "Izoniazid", False, "NAT2 určuje rychlost acetylace izoniazidu — pomalí acetylátoři mají vyšší riziko neuropatie.")],
  "Farmakogenetika vysvětluje idiosynkrazii — neobvyklou reakci, která nesouvisí s dávkou ani s mechanismem účinku a není imunitně podmíněná.")

S("O27", "Tolerance, tachyfylaxe, rezistence",
  "TŘI RŮZNÉ DĚJE, KTERÉ SE PLETOU — pomalé slábnutí, bleskové vyčerpání a obrana bakterie.", "krajina",
  [("📉", "Pomalu klesající křivka", False, "TOLERANCE — na týž účinek je třeba stále vyšší dávka; buduje se dny až týdny. Farmakodynamická (down-regulace receptorů) nebo farmakokinetická (indukce vlastního metabolismu — barbituráty)."),
   ("⚡", "Vybitá baterie", True, "TACHYFYLAXE — velmi rychlý pokles účinku při opakovaném podání v krátkém sledu, typicky vyčerpáním zásoby mediátoru (efedrin). ZVÝŠENÍ DÁVKY NEPOMŮŽE."),
   ("🩹", "Náplast sundaná na noc", False, "Tachyfylaxe vzniká i u nitrátů — proto se ponechává noční interval bez nitrátu."),
   ("🦠", "Bakterie za štítem", True, "REZISTENCE je vlastnost MIKROORGANISMU, ne pacienta — primární (přirozená) nebo získaná (mutace, přenos plazmidu). Nepleť si ji s tolerancí."),
   ("🔀", "Zkřížené šipky", False, "ZKŘÍŽENÁ TOLERANCE existuje mezi látkami se stejným mechanismem — alkohol, benzodiazepiny a barbituráty; morfin a ostatní opioidy."),
   ("💤", "Spící pacient", False, "U opioidů roste tolerance rychle na euforii a útlum dechu."),
   ("🚽", "Zácpa, která zůstává", True, "Na zácpu a miózu po opioidech tolerance prakticky nevzniká — proto se laxativum podává po celou dobu léčby.")],
  "Tolerance na různé účinky téže látky se vyvíjí různě rychle — proto pacient s tolerancí na útlum dechu může být stále ohrožen zácpou a miózou.")

S("O28", "Vliv průvodních onemocnění, polypragmazie",
  "LÉKÁRNIČKA, KTERÁ SE SAMA PLNÍ — každý nový lék léčí nežádoucí účinek předchozího.", "pokoj",
  [("♾️", "Nekonečná smyčka", True, "PRESKRIPČNÍ KASKÁDA: metoklopramid vyvolá parkinsonské projevy → nasadí se antiparkinsonikum. Blokátor kalciových kanálů vyvolá otoky → nasadí se diuretikum."),
   ("🫘", "Zúžená ledvina", False, "Renální insuficience — snížit dávku léčiv vylučovaných ledvinami (aminoglykosidy, digoxin, metformin, lithium)."),
   ("🫀", "Slabé srdce", False, "Srdeční selhání snižuje průtok játry i ledvinami; u léčiv s vysokou jaterní extrakcí hladina stoupá."),
   ("5️⃣", "Pět krabiček", True, "POLYPRAGMAZIE — zpravidla 5 a více léčiv současně; roste riziko interakcí, pádů, hospitalizací a klesá adherence."),
   ("🧹", "Koště", False, "DEPRESKRIPCE — plánované vysazení léků, které už nepřinášejí užitek; u polymorbidních stejně důležitá jako nasazení."),
   ("🫁", "Astmatik s β-blokátorem", True, "Kontraindikace bývají dané přidruženou chorobou: β-blokátor u astmatu, NSA u renální insuficience a vředové choroby, metformin při riziku laktátové acidózy."),
   ("❓", "Otazník nad novým příznakem", True, "Nový příznak je nežádoucí účinek léku, dokud se neprokáže opak — teprve pak se hledá nová diagnóza.")],
  "Polypragmazie není jen počet léků, ale i jejich vzájemná zbytečnost — cílem je nejmenší počet léčiv, který splní léčebný záměr.")

S("O29", "Nežádoucí účinky léčiv",
  "DVĚ ŠUPLÍKY: „ČEKANÝ“ A „BIZARNÍ“ — v prvním se dávka snižuje, ve druhém se lék už nikdy nepodá.", "pokoj",
  [("📈", "Šuplík A", False, "TYP A (Augmented) — zesílený farmakologický účinek: závisí na dávce, je předvídatelný a častý. Krvácení po warfarinu, hypoglykemie po inzulinu, bradykardie po β-blokátoru. Řeší se snížením dávky."),
   ("🎲", "Šuplík B s kostkou", True, "TYP B (Bizarre) — nesouvisí s dávkou ani s mechanismem, nedá se předvídat; vzácný, ale často závažný. Alergie, aplastická anemie po chloramfenikolu, maligní hypertermie, Stevensův–Johnsonův syndrom."),
   ("⏱️", "Hodiny", False, "TYP C — chronický, při dlouhém podávání (osteoporóza po kortikoidech)."),
   ("🕰️", "Staré hodiny", False, "TYP D — pozdní: teratogenita, kancerogenita."),
   ("🚪", "Bouchnuté dveře", True, "TYP E — po náhlém vysazení: rebound hypertenze, adrenální insuficience, rebound nespavost."),
   ("📮", "Schránka hlášení", False, "Podezření se hlásí SÚKL; u nově registrovaných léčiv (černý trojúhelník) i podezření běžná — právě tak se odhalí to, co ve fázi III nevyšlo najevo."),
   ("📝", "Zápis do dokumentace", True, "Typ B znamená lék vysadit, už nikdy nepodat a poznamenat do dokumentace.")],
  "Rozdělení A/B rozhoduje o postupu: typ A se řeší dávkou, typ B vysazením — proto je nutné je odlišit dřív, než se sáhne po úpravě dávkování.")

S("O30", "Léková alergie, idiosynkrazie",
  "DVĚ SETKÁNÍ — první je tiché, druhé bouřlivé. Bez prvního nikdy nepřijde druhé.", "pokoj",
  [("1️⃣", "Tiché první setkání", True, "SENZIBILIZACE probíhá BEZ příznaků — proto reakce nikdy nepřijde při úplně prvním podání."),
   ("2️⃣", "Bouřlivé druhé setkání", True, "TYP I (IgE, časný) — kopřivka, angioedém, bronchospasmus, ANAFYLAXE během minut."),
   ("💉", "Adrenalinové pero", True, "U anafylaxe je lékem první volby ADRENALIN INTRAMUSKULÁRNĚ do stehna; antihistaminika a kortikosteroidy jsou jen doplňkové a působí příliš pomalu."),
   ("🩸", "Typ II a III", False, "Typ II cytotoxický, typ III imunokomplexový (sérová nemoc)."),
   ("🖐️", "Ekzém na ruce", False, "Typ IV pozdní buněčný — kontaktní ekzém, makulopapulózní exantém za dny."),
   ("🧬", "Idiosynkrazie", True, "Geneticky podmíněná neobvyklá reakce BEZ účasti imunity — hemolýza při deficitu G6PD, maligní hypertermie po sukcinylcholinu, prodloužená apnoe při atypické pseudocholinesteráze."),
   ("🍄", "Ampicilin u mononukleózy", True, "Exantém po ampicilinu u infekční mononukleózy NENÍ alergie — a nesmí se tak zapsat.")],
  "Nauzea po antibiotiku není alergie, ale nesnášenlivost — přesto se často zapíše jako alergie a pacient pak zbytečně přijde o celou lékovou skupinu.")

S("O31", "Karcinogenní a mutagenní účinky",
  "DLOUHÝ STÍN — mutagen poškodí DNA dnes, nádor vyroste za dvacet let.", "noc",
  [("🧬", "Zlomená šroubovice", False, "MUTAGENITA — poškození genetické informace: genové mutace, chromozomové aberace, změny počtu chromozomů. V zárodečných buňkách se přenáší na potomstvo."),
   ("🦀", "Nádor", False, "KARCINOGENEZE má fáze INICIACE (nevratné poškození DNA), PROMOCE (podpora množení poškozeného klonu) a PROGRESE."),
   ("⏳", "Dlouhé přesýpací hodiny", True, "Latence je roky až desetiletí — proto se karcinogenita odhalí až po letech užívání a žádná registrační studie ji nezachytí."),
   ("🧪", "Amesův test", False, "Testuje se předklinicky: Amesův test (mutagenita na bakteriích), testy chromozomových aberací, dlouhodobé studie na hlodavcích."),
   ("💊", "Cytostatikum", True, "Alkylační látky vyvolávají sekundární leukemie — lék na nádor zvyšuje riziko nádoru druhého."),
   ("🛡️", "Imunosuprese", True, "Imunosupresiva zvyšují výskyt lymfomů a kožních nádorů."),
   ("🚬", "Cigareta", False, "Genotoxické karcinogeny nemají bezpečnou dávku; negenotoxické (hormonální, imunosupresivní) působí nepřímo — estrogeny bez gestagenu a karcinom endometria.")],
  "To, že lék léčí nádor a zároveň zvyšuje riziko jiného, není rozpor — je to poměr rizika a prospěchu, který se váží u každého pacienta zvlášť.")

S("O32", "Léčiva v těhotenství, teratogenní účinek, léčiva v době kojení",
  "KALENDÁŘ TĚHOTENSTVÍ — nejnebezpečnější je 3.–8. TÝDEN, kdy žena často ještě neví, že je těhotná.", "pokoj",
  [("🥚", "Vajíčko", False, "0.–2. TÝDEN — pravidlo „všechno, nebo nic“: buď zárodek zanikne, nebo se poškození plně opraví."),
   ("⚠️", "Červené pole na kalendáři", True, "3.–8. TÝDEN — ORGANOGENEZE, období největšího rizika strukturních vad."),
   ("💊", "Seznam teratogenů", True, "Isotretinoin a retinoidy, thalidomid, warfarin, valproát, karbamazepin, fenytoin, metotrexát, mykofenolát, ACE inhibitory a sartany, tetracykliny, živé vakcíny, inhibitory 5-α-reduktázy."),
   ("📈", "Rostoucí plod", False, "Od 9. týdne vznikají FUNKČNÍ poruchy a poruchy růstu: ACE inhibitory poškozují ledviny plodu, NSA předčasně uzavírají ductus arteriosus, tetracykliny barví zuby."),
   ("🍼", "Kojení", False, "Do mléka přechází nejspíš látka lipofilní, málo vázaná na bílkoviny a zásaditá. Podává se ihned PO kojení. Kontraindikovány jsou cytostatika, radiofarmaka, lithium, amiodaron."),
   ("⚖️", "Váhy rizika", True, "Neléčená nemoc matky (epilepsie, astma, těžká deprese, infekce) ohrožuje plod často víc než lék — neléčí se „nulovým rizikem“, ale poměrem rizika a prospěchu."),
   ("🥬", "Kyselina listová", False, "Podává se preventivně už před početím jako prevence rozštěpů neurální trubice; u žen na antiepilepticích ve vyšší dávce.")],
  "Bezpečnost v graviditě se nedá odvodit z toho, že je lék volně prodejný — NSA jsou ve třetím trimestru kontraindikované, přestože je má doma každý.")

S("O33", "Farmakoterapie v dětství",
  "DĚTSKÁ ORDINACE S VÁHAMI — dítě není zmenšený dospělý, dávkuje se na KILOGRAM.", "pokoj",
  [("⚖️", "Váhy", False, "Dávkuje se na kilogram tělesné hmotnosti, u cytostatik na plochu povrchu těla — nikdy „zlomkem dávky dospělého“ od oka."),
   ("🍼", "Kojenec", True, "Novorozenec má nezralou glukuronidaci (gray baby syndrom po chloramfenikolu), vyšší podíl tělesné vody, nižší vazbu na bílkoviny a nezralou glomerulární filtraci."),
   ("🦷", "Obarvený zub", True, "Tetracykliny do 8 let — zbarvení zubů a hypoplazie skloviny."),
   ("🦵", "Poškozená chrupavka", True, "Chinolony u dětí poškozují chrupavku."),
   ("😴", "Kodein", True, "Kodein a tramadol — útlum dechu u ultrarychlých metabolizátorů CYP2D6; u dětí kontraindikované."),
   ("🧠", "Reyeův syndrom", True, "Kyselina acetylsalicylová u dítěte s horečnatým virovým onemocněním — Reyeův syndrom. Antipyretiky volby jsou paracetamol a ibuprofen."),
   ("🧃", "Sirup a čípek", False, "Formy: perorální roztoky, sirupy, kapky, čípky; při dlouhodobé léčbě pozor na obsah cukru a etanolu.")],
  "Řada léčiv nemá u dětí registraci a podává se off-label podle odborných doporučení — klinické studie na dětech jsou vzácné.")

S("O34", "Farmakoterapie ve stáří, polypragmazie",
  "POMALÁ CESTA — START LOW, GO SLOW. A každý nový příznak je podezřelý z toho, že ho způsobil lék.", "krajina",
  [("🐢", "Želva na cestě", False, "Start low, go slow — nižší úvodní dávka a pomalá titrace s kontrolou účinku i nežádoucích účinků."),
   ("🫘", "Ledvina", True, "Glomerulární filtrace klesá s věkem i při NORMÁLNÍM sérovém kreatininu, protože ubývá svalové hmoty — počítá se clearance, ne jen kreatinin."),
   ("🧠", "Citlivý mozek", True, "Vyšší citlivost na benzodiazepiny, opioidy, anticholinergika a antipsychotika — riziko pádů, zmatenosti a deliria."),
   ("🧈", "Tuková zásoba", False, "Ubývá svalu a přibývá tuku, takže lipofilní léčiva se hromadí a mají delší poločas."),
   ("📋", "Seznam Beers", False, "Beersova kritéria a STOPP/START vyjmenovávají u seniorů nevhodná léčiva (dlouhodobě působící benzodiazepiny, anticholinergika, NSA) i ta, která chybějí."),
   ("🏜️", "Anticholinergní zátěž", True, "Sčítá se z mnoha léků najednou (antihistaminika I. generace, tricyklika, spasmolytika, některá antipsychotika) — zmatenost, retence moči, zácpa, pády."),
   ("❓", "Otazník", True, "Nový příznak u seniora je nežádoucí účinek léku, dokud se neprokáže opak — jinak vzniká preskripční kaskáda.")],
  "Depreskripce je u seniora stejně důležitá jako nasazení nového léku — a často přinese větší užitek.")

S("O35", "Biologická léčba: rozdělení, názvosloví, biosimilars",
  "TABULE S KONCOVKAMI — konec názvu prozradí, co to je.", "laborator",
  [("🔤", "Koncovka -mab", False, "MONOKLONÁLNÍ PROTILÁTKA. Předposlední slabika říká původ: -xi- chimérická (infliximab), -zu- humanizovaná (trastuzumab), -u- plně lidská (adalimumab)."),
   ("🪝", "Koncovka -cept", False, "FÚZNÍ BÍLKOVINA, solubilní receptor, který na sebe naváže cytokin: etanercept váže TNF-α, dále abatacept, aflibercept."),
   ("🧩", "Koncovka -nib", False, "MALÁ MOLEKULA, inhibitor kinázy — na rozdíl od protilátek se podává PERORÁLNĚ (imatinib, tofacitinib, ibrutinib)."),
   ("💉", "Injekce, ne tableta", True, "Protilátky jsou bílkoviny — v trávicím traktu by se strávily, proto se podávají parenterálně a vyžadují chladový řetězec."),
   ("♻️", "Podobná, ne stejná kopie", False, "BIOSIMILAR — u bílkoviny nelze vyrobit přesnou kopii jako u generika; dokládá se srovnatelná kvalita, účinnost a bezpečnost, ne pouhá bioekvivalence."),
   ("🦠", "Latentní tuberkulóza", True, "Před anti-TNF-α je nutné vyloučit latentní tuberkulózu a hepatitidu B — hrozí reaktivace."),
   ("🛡️", "Protilátky proti léku", True, "Imunogenicita — tvorba neutralizujících protilátek proti léku, které ho časem přestanou nechat účinkovat. Dále infuzní a hypersenzitivní reakce.")],
  "Inhibitory kontrolních bodů (nivolumab, pembrolizumab) působí opačně než imunosupresiva — uvolňují brzdu imunity, a proto jejich nežádoucí účinky vypadají jako autoimunitní choroby.")

# ────────────────────────────── SPECIÁLNÍ FARMAKOLOGIE I ───────────────────────

S("36", "Cholinergní přenos vzruchu",
  "DVOJE DVEŘE ACETYLCHOLINU — nikotinové (bleskové, kanál) a muskarinové (pomalé, přes G-protein).", "les",
  [("🚬", "Rychlé dveře N", False, "NIKOTINOVÉ receptory jsou ionotropní — samy iontovým kanálem, účinek za milisekundy. Nn v gangliích a dřeni nadledvin, Nm na nervosvalové ploténce."),
   ("🍄", "Pomalé dveře M", False, "MUSKARINOVÉ receptory jsou metabotropní, přes G-protein. M1 v CNS a gangliích, M2 v srdci (zpomalí ho), M3 v hladkém svalu a žlázách (kontrakce, sekrece)."),
   ("✂️", "Nůžky esterázy", False, "Acetylcholin vzniká z cholinu a acetyl-CoA (cholinacetyltransferáza) a po uvolnění ho okamžitě štěpí ACETYLCHOLINESTERÁZA — proto je jeho účinek velmi krátký."),
   ("💧", "Tekoucí voda", False, "Účinky parasympatiku: slinění, slzení, pocení, mióza a akomodace na blízko."),
   ("🐢", "Zpomalené srdce", False, "Bradykardie přes M2."),
   ("🫁", "Stažené bronchy", True, "Bronchokonstrikce a zvýšená sekrece hlenu — proto jsou cholinomimetika u astmatu kontraindikovaná."),
   ("🚽", "Vyprázdnění", False, "Zvýšená peristaltika a vyprázdnění močového měchýře.")],
  "Sympatikus i parasympatikus mají v gangliích tentýž nikotinový receptor — proto ganglioplegika ovlivňují obojí a mají tolik nežádoucích účinků.")

S("37", "Přímá cholinomimetika",
  "PROMOKLÁ KRAJINA — všechno teče a všechno se stahuje. SLUDGE.", "more",
  [("💧", "Déšť SLUDGE", False, "Salivation, Lacrimation, Urination, Diarrhea, GI motility, Emesis — typický muskarinový obraz."),
   ("👁️", "Zúžená zornice", False, "PILOKARPIN stahuje musculus sphincter pupillae (mióza) a ciliární sval, čímž otevře komorový úhel — u glaukomu s uzavřeným úhlem a u xerostomie po ozáření."),
   ("🚽", "Plný měchýř", False, "BETHANECHOL — karbamátový ester odolný vůči acetylcholinesteráze; stimuluje močový měchýř a střevo u pooperační atonie."),
   ("💊", "Lahvička atropinu", True, "ANTIDOTEM předávkování je ATROPIN."),
   ("🫁", "Stažené bronchy", True, "Kontraindikace: astma a CHOPN (bronchokonstrikce), vředová choroba, bradykardie a poruchy vedení, obstrukce močových cest a střeva."),
   ("👀", "Karbachol", False, "Karbachol se používá v oftalmologii; methacholin jen k bronchoprovokačnímu testu."),
   ("🍄", "Muchomůrka", True, "Muskarin z muchomůrky červené a strmělek působí týž obraz — otrava se léčí atropinem.")],
  "Přímá cholinomimetika působí i bez vlastního acetylcholinu, protože sedají rovnou na receptor — na rozdíl od nepřímých, která potřebují zachovanou produkci mediátoru.")

S("38", "Nepřímá cholinomimetika",
  "PŘESTŘIŽENÉ NŮŽKY — acetylcholin se nerozkládá, tak se ho v synapsi hromadí čím dál víc.", "laborator",
  [("✂️", "Zlomené nůžky", False, "Inhibice ACETYLCHOLINESTERÁZY zvyšuje koncentraci acetylcholinu v synapsi — účinek je nepřímý a závisí na vlastní produkci mediátoru."),
   ("💪", "Slabý sval", False, "NEOSTIGMIN a pyridostigmin jsou KVARTÉRNÍ aminy — do CNS nepronikají; u myasthenia gravis, k dekurarizaci po nedepolarizujících myorelaxanciích a u pooperační atonie."),
   ("🧠", "Mozek", False, "DONEPEZIL, rivastigmin a galantamin jsou terciární aminy — do CNS pronikají, u Alzheimerovy choroby. Fysostigmin je antidotem anticholinergního deliria."),
   ("☠️", "Postřikovač", True, "ORGANOFOSFÁTY (insekticidy, bojové látky) vážou enzym NEVRATNĚ — cholinergní krize: mióza, bronchorea, bronchospasmus, bradykardie, křeče, obrna dýchacích svalů."),
   ("💉", "Atropin", True, "Antidotum I: ATROPIN — blokuje muskarinové účinky."),
   ("🔑", "Pralidoxim", True, "Antidotum II: PRALIDOXIM — reaktivuje enzym, dokud nedojde ke „stárnutí“ vazby."),
   ("🔬", "Edrofonium", False, "Edrofonium má velmi krátký účinek (dříve diagnostický test u myasthenia gravis).")],
  "Atropin sám organofosfátovou otravu nevyřeší — neúčinkuje na nikotinové receptory, a tedy ani na obrnu dýchacích svalů. Proto se přidává pralidoxim.")

S("39", "Parasympatolytika",
  "VYPRAHLÁ POUŠŤ — suchý jako kost, rudý jako řepa, horký jako pec, slepý jako netopýr, šílený jako kloboučník.", "poust",
  [("🏜️", "Vyschlá půda", False, "Blokáda muskarinových receptorů — sucho v ústech, vyschlé sliznice, zástava pocení."),
   ("🌡️", "Rozpálený teploměr", True, "Bez pocení stoupá teplota — hypertermie, u dětí nebezpečná. Kůže je suchá a zarudlá."),
   ("👁️", "Obří oko", True, "Mydriáza a paralýza akomodace (cykloplegie). Kontraindikací je GLAUKOM S UZAVŘENÝM ÚHLEM — rozšířená duhovka uzavře komorový úhel."),
   ("💓", "Splašené srdce", False, "Blokáda M2 → tachykardie. Atropin se proto podává u bradykardie a v premedikaci."),
   ("🚽", "Zamčený záchod", True, "Retence moči (pozor u hyperplazie prostaty) a zácpa až paralytický ileus."),
   ("🎩", "Šílený kloboučník", True, "Centrální anticholinergní syndrom — neklid, zmatenost, delirium. Antidotem FYSOSTIGMIN (terciární amin, projde do CNS)."),
   ("🫁", "Rozepnuté plíce", False, "Ipratropium a tiotropium inhalačně u CHOPN a astmatu. Dále butylskopolamin (spasmolytikum), tropikamid (oční vyšetření), biperiden, oxybutynin a solifenacin.")],
  "Butylskopolamin je KVARTÉRNÍ amin — neprojde do CNS, takže neseduje ani nevyvolá delirium. Atropin a skopolamin (terciární) ano.")

S("40", "Adrenergní přenos vzruchu",
  "RECYKLAČNÍ DVŮR — noradrenalin se nerozkládá jako acetylcholin, ale z 80 % se VRACÍ ZPĚT do nervu.", "krajina",
  [("🔄", "Recyklační kruh", True, "Účinek končí především ZPĚTNÝM VYCHYTÁVÁNÍM (uptake-1) do nervového zakončení; teprve pak látku odbourává MAO a COMT. Kokain, tricyklika a SNRI tento transportér blokují."),
   ("🧬", "Výrobní linka", False, "Tyrosin → DOPA (tyrosinhydroxyláza, krok určující rychlost) → dopamin → noradrenalin; v dřeni nadledvin dále na adrenalin."),
   ("🩸", "Stažená céva", False, "α1 — vazokonstrikce, mydriáza, kontrakce svěrače měchýře a prostaty."),
   ("🛑", "Brzda na nervu", False, "α2 — PRESYNAPTICKY tlumí další výlev noradrenalinu; proto klonidin snižuje tlak centrálně."),
   ("❤️", "Zrychlené srdce", False, "β1 — zvýšená frekvence, vodivost a kontraktilita; v ledvině výlev reninu."),
   ("🫁", "Rozšířené bronchy", False, "β2 — bronchodilatace, vazodilatace ve svalech, relaxace dělohy, tremor, hypokalemie."),
   ("🧈", "Tuková buňka", False, "β3 — lipolýza a relaxace detruzoru (mirabegron).")],
  "Adrenalin má afinitu ke všem receptorům, noradrenalin převážně k α a β1 — proto noradrenalin zvyšuje tlak vazokonstrikcí, kdežto adrenalin navíc rozšiřuje bronchy.")

S("41", "Neselektivní sympatomimetika",
  "ZÁCHRANÁŘSKÝ VŮZ — jediný lék, který u anafylaxe umí obojí najednou: otevřít bronchy a stáhnout cévy.", "krajina",
  [("💉", "Pero do stehna", True, "U ANAFYLAXE je ADRENALIN lékem první volby — intramuskulárně do stehna (m. vastus lateralis); nástup je rychlejší a bezpečnější než subkutánně."),
   ("🫁", "Otevřené bronchy", False, "β2 rozšíří bronchy."),
   ("🩸", "Ustupující otok", False, "α1 stáhne cévy a ustoupí otok sliznice a angioedém — obojí zároveň, což žádný jiný lék neumí."),
   ("❤️", "Srdeční zástava", False, "β1 zvyšuje kontraktilitu a frekvenci; adrenalin se podává při srdeční zástavě a v šoku."),
   ("⚠️", "Arytmie", True, "Vysoké dávky působí arytmie a hypertenzi."),
   ("💊", "S lokálním anestetikem", False, "Přídavek adrenalinu způsobí vazokonstrikci — zpomalí vstřebávání, prodlouží účinek a sníží krvácení a systémovou toxicitu."),
   ("🥞", "Glukagon v záloze", True, "U pacienta na β-blokátoru může být adrenalin méně účinný — pak se podává glukagon, který srdce stimuluje mimo β-receptor.")],
  "Izoprenalin je neselektivní β-agonista (β1 i β2) — dnes okrajově u bradykardie a AV blokády; dopamin a dobutamin patří k inotropní podpoře.")

S("42", "Sympatomimetika alfa",
  "STAŽENÉ POTRUBÍ — α1 stahuje cévy. Ale α2 v mozku dělá pravý opak: tlak SNIŽUJE.", "pokoj",
  [("🩸", "Stažená trubka", False, "α1-agonisté (fenylefrin, noradrenalin, midodrin) stahují cévy, zvyšují periferní odpor a krevní tlak — v šoku, při hypotenzi a k lokální vazokonstrikci."),
   ("👃", "Nosní kapky", True, "Xylometazolin, oxymetazolin, nafazolin — jen 5–7 DNÍ, jinak vzniká rhinitis medicamentosa s odrazovým otokem a závislostí na kapkách."),
   ("🧠", "Brzda v mozku", True, "α2-agonisté (klonidin, methyldopa, brimonidin, dexmedetomidin) působí na PRESYNAPTICKÝ receptor v CNS — tlumí výlev noradrenalinu, a proto tlak SNIŽUJÍ."),
   ("💓", "Zpomalené srdce", False, "Prudký vzestup tlaku vyvolá baroreflexem BRADYKARDII — proto po fenylefrinu srdce zpomalí, ačkoli jde o sympatomimetikum."),
   ("🤰", "Methyldopa", False, "Methyldopa je lékem volby u hypertenze v graviditě."),
   ("👁️", "Brimonidin", False, "Brimonidin se používá lokálně u glaukomu."),
   ("⚠️", "Náhlé vysazení", True, "Náhlé vysazení klonidinu vyvolá REBOUND HYPERTENZI s tachykardií a pocením — vysazuje se postupně.")],
  "Že agonista snižuje tlak, není chyba — rozhoduje, na kterém receptoru a na které straně synapse působí.")

S("43", "Sympatomimetika beta",
  "TŘESOUCÍ SE RUCE NAD INHALÁTOREM — β2 otevře bronchy a vždycky přidá stejnou trojici: třes, tachykardii, hypokalemii.", "krajina",
  [("🫁", "Otevřené bronchy", False, "β2-agonisté relaxují hladký sval bronchu. SABA (salbutamol, fenoterol, terbutalin) působí během minut — úlevová léčba."),
   ("📈", "Prázdné krabičky", True, "Vysoká spotřeba SABA znamená špatně kontrolované astma."),
   ("⏳", "Dlouhý účinek", True, "LABA (formoterol, salmeterol, indakaterol) působí 12–24 hodin. NIKDY samostatně u astmatu — monoterapie zvyšuje mortalitu; vždy s inhalačním kortikoidem."),
   ("🤲", "Třesoucí se ruce", False, "Tremor (β2 v kosterním svalu)."),
   ("💓", "Bušící srdce", False, "Tachykardie — částečná stimulace β1 a reflexně."),
   ("🍌", "Klesající draslík", True, "Hypokalemie — draslík se přesouvá do buňky; pozor při současné léčbě diuretiky a digoxinem."),
   ("🤰", "Tokolýza", False, "β2-agonisté relaxují dělohu — hexoprenalin k tokolýze při hrozícím předčasném porodu. β1-agonista dobutamin slouží k inotropní podpoře.")],
  "β2-agonista neléčí zánět, jen uvolní sval — proto astma nikdy nestojí na něm samotném, ale na inhalačním kortikoidu.")

S("44", "Nepřímá sympatomimetika",
  "VYPLAVENÝ SKLAD — nesedají na receptor, jen vysypou zásoby. A sklad se dá vyprázdnit.", "pokoj",
  [("🪣", "Převrácený kbelík", False, "Efedrin, pseudoefedrin, amfetamin a metamfetamin obracejí chod transportéru a VYPLAVUJÍ noradrenalin z nervového zakončení."),
   ("🚫", "Zabedněný vchod", False, "Kokain, tricyklická antidepresiva a SNRI BLOKUJÍ zpětné vychytávání — mediátor zůstává v synapsi déle."),
   ("⚡", "Prázdný sklad", True, "TACHYFYLAXE — opakované podání vyčerpá zásobu mediátoru, účinek rychle slábne a zvýšení dávky NEPOMŮŽE."),
   ("🧀", "Zrající sýr", True, "S inhibitory MAO hrozí HYPERTENZNÍ KRIZE — „sýrový efekt“ po potravinách bohatých na tyramin (zrající sýry, uzeniny, červené víno)."),
   ("👃", "Dekongescens", False, "Efedrin a pseudoefedrin jako dekongescencia a při hypotenzi."),
   ("🧒", "ADHD", False, "Amfetaminové deriváty terapeuticky u ADHD a narkolepsie, jinak zneužívané."),
   ("🍽️", "Tyramin z potravy", True, "Tyramin je nepřímé sympatomimetikum z potravy — normálně ho MAO ve střevě zlikviduje; při léčbě IMAO se dostane do oběhu.")],
  "Nepřímé sympatomimetikum nezabere tam, kde jsou zásoby mediátoru vyčerpané — proto se v šoku dává přednost přímým agonistům.")

S("45", "Sympatolytika alfa",
  "PRVNÍ VSTÁNÍ Z POSTELE — po první dávce se podlomí kolena. Proto se bere na noc.", "pokoj",
  [("📉", "Klesající tlak", False, "Blokáda α1 uvolní hladký sval cév — klesá periferní odpor a tlak. Doxazosin a terazosin se používají u hypertenze i u prostaty."),
   ("🛏️", "Postel", True, "FENOMÉN PRVNÍ DÁVKY — prudká ortostatická hypotenze a synkopa; proto se začíná nízkou dávkou na noc."),
   ("🚹", "Prostata", False, "TAMSULOSIN a silodosin jsou uroselektivní (α1A) — uvolní hladký sval prostaty a hrdla měchýře, tlak ovlivní málo."),
   ("💧", "Retrográdní ejakulace", False, "Typický nežádoucí účinek tamsulosinu."),
   ("👁️", "Plovoucí duhovka", True, "IFIS — intraoperative floppy iris syndrome; před operací katarakty je nutné oftalmologa upozornit na užívání tamsulosinu."),
   ("💥", "Feochromocytom", True, "Fenoxybenzamin a fentolamin jsou neselektivní α-blokátory u feochromocytomu — podávají se PŘED β-blokátorem."),
   ("🚫", "Zakázané pořadí", True, "U feochromocytomu se nikdy nezačíná β-blokátorem — nebrzděná α-stimulace by vyvolala hypertenzní krizi.")],
  "α-blokátory nejsou dnes lékem první volby u hypertenze — používají se spíš u rezistentní hypertenze nebo tam, kde je současně hyperplazie prostaty.")

S("46", "Sympatolytika beta (betablokátory)",
  "ZPOMALENÁ VESNICE — všechno tu jde pomaleji: srdce, dech i cukr. A odjet se nesmí náhle.", "krajina",
  [("💓", "Zpomalené srdce", False, "Blokáda β1 snižuje frekvenci, kontraktilitu, vodivost a spotřebu kyslíku myokardem; snižuje i výlev reninu."),
   ("🫁", "Sevřené plíce", True, "Neselektivní (propranolol, sotalol) blokují i β2 → bronchospasmus. Kardioselektivní (bisoprolol, metoprolol, atenolol, nebivolol) jsou bezpečnější, ve vysoké dávce selektivita mizí."),
   ("🍬", "Schovaný bonbon", True, "U diabetika maskují varovné příznaky hypoglykemie (tachykardii, třes) — pocení zůstává."),
   ("🛑", "Zákaz náhlého odjezdu", True, "NEVYSAZOVAT NÁHLE — up-regulace receptorů vede k rebound tachykardii, hypertenzi a může vyprovokovat anginu nebo infarkt."),
   ("👁️", "Kapka do oka", True, "Timolol v očních kapkách se vstřebá a může vyvolat bradykardii a bronchospasmus."),
   ("🚧", "Zaseknutá závora", True, "Kombinace s verapamilem nebo diltiazemem hrozí těžkou bradykardií a AV blokádou."),
   ("🦋", "Motýl štítné žlázy", False, "Indikace: hypertenze, ischemická choroba, arytmie, srdeční selhání (bisoprolol, karvedilol, metoprolol), tyreotoxikóza, tremor, migréna, glaukom.")],
  "Karvedilol a labetalol blokují i α1; sotalol má navíc antiarytmický účinek III. třídy; nebivolol uvolňuje oxid dusnatý.")

S("47", "Myorelaxancia",
  "DVĚ CESTY K OCHRNUTÍ — jedna sval nejdřív ROZKMITÁ a zvrátit se nedá, druhá ho jen odpojí a zvrátit jde.", "laborator",
  [("⚡", "Záškuby svalu", True, "SUKCINYLCHOLIN je DEPOLARIZUJÍCÍ — chová se jako acetylcholin, který se nerozkládá: nejprve receptor trvale aktivuje (fascikulace), pak nastane blokáda. Působí 5–10 minut."),
   ("🚫", "Nelze zvrátit", True, "Depolarizující blok NELZE zvrátit neostigminem — ten by ho prohloubil."),
   ("🔒", "Obsazený zámek", False, "NEDEPOLARIZUJÍCÍ (rokuronium, vekuronium, atrakurium, cisatrakurium) jsou kompetitivní antagonisté nikotinového receptoru — sval ochrne bez fascikulací."),
   ("💊", "Sugammadex", False, "Nedepolarizující blok lze zvrátit neostigminem, u rokuronia specificky SUGAMMADEXEM."),
   ("🔥", "Maligní hypertermie", True, "Vzácná geneticky podmíněná reakce na sukcinylcholin a inhalační anestetika: prudký vzestup teploty, rigidita, acidóza. Antidotem DANTROLEN."),
   ("🍌", "Hyperkalemie", True, "Sukcinylcholin uvolní draslík — nebezpečné u popálenin, polytraumat a neuromuskulárních chorob. Dále bolest svalů, vzestup nitroočního tlaku, prodloužená apnoe při atypické pseudocholinesteráze."),
   ("🧘", "Baklofen", False, "Centrální myorelaxancia: baklofen (agonista GABA-B), tizanidin, tolperison — na spasticitu, nikoli k anestezii.")],
  "Myorelaxans netlumí vědomí ani bolest — pacient musí být zároveň uspán a analgetizován, jinak je ochrnutý při vědomí.")

S("48", "Lokální anestetika",
  "ZANESENÝ ZÁMEK V ZÁNĚTU — kanál se zavírá zevnitř, ale v kyselém prostředí se k němu lék nedostane.", "pokoj",
  [("🚪", "Sodíkový kanál", False, "Vážou se ZEVNITŘ na napěťově řízený sodíkový kanál a brání vzniku a šíření akčního potenciálu."),
   ("🔥", "Zanícená tkáň", True, "V kyselém prostředí zánětu převáží ionizovaná forma, která neprojde membránou k místu účinku — proto se v zaníceném terénu často nepodaří umrtvit."),
   ("💉", "S adrenalinem", True, "Vazokonstrikce prodlouží účinek, sníží krvácení a systémovou toxicitu. NEPODÁVAT do akrálních částí (prsty, nos, ucho) — riziko ischemie."),
   ("🧠", "Brnění kolem úst", True, "Systémová toxicita začíná v CNS: kovová chuť, brnění kolem úst, hučení, závrať, křeče — a TEPRVE PAK přijde kardiotoxicita."),
   ("💔", "Bupivakain", True, "Bupivakain je nejkardiotoxičtější; léčbou systémové toxicity je lipidová emulze."),
   ("🧪", "Estery a amidy", False, "ESTERY (prokain, benzokain, tetrakain) štěpí plazmatické esterázy, častější alergie (metabolit PABA). AMIDY (lidokain, mepivakain, artikain, bupivakain, prilokain) se metabolizují v játrech, alergie vzácná."),
   ("🔵", "Modrá krev", True, "Prilokain a benzokain mohou vyvolat methemoglobinemii — antidotem methylenová modř.")],
  "Nejdřív vypadne bolest a teplo, pak dotek a nakonec motorika — tenká nemyelinizovaná vlákna se blokují první. Lidokain je zároveň antiarytmikum třídy Ib.")

S("49", "Celková anestetika — inhalační",
  "MĚŘIDLO MAC — čím NIŽŠÍ číslo, tím SILNĚJŠÍ látka.", "laborator",
  [("📊", "Měřidlo MAC", False, "MAC — minimální alveolární koncentrace, při níž se 50 % pacientů nepohne po kožním řezu; je mírou potence. NÍZKÉ MAC = VYSOKÁ potence."),
   ("👵", "Klesající MAC", False, "MAC klesá s věkem, v graviditě a při současném podání opioidů."),
   ("💨", "Rychlá pára", False, "Rychlost nástupu určuje rozpustnost v krvi: čím nižší, tím rychlejší nástup i probuzení. Desfluran a sevofluran nastupují rychle, halothan pomalu."),
   ("🔥", "Maligní hypertermie", True, "Halogenovaná anestetika (sevofluran, desfluran, isofluran) mohou spolu se sukcinylcholinem vyvolat malignitní hypertermii — antidotem DANTROLEN."),
   ("🟡", "Halothan", True, "Halothan navíc hepatotoxicita — dnes se prakticky nepoužívá."),
   ("😀", "Rajský plyn", True, "Oxid dusný (N2O) má výbornou ANALGEZII, ale slabý anestetický účinek — jen jako doplněk. Inaktivuje vitamin B12 a difunduje do uzavřených dutin."),
   ("🧒", "Sevofluran u dětí", False, "Sevofluran je pro dobrou snášenlivost dýchacími cestami vhodný k úvodu do anestezie u dětí.")],
  "Inhalační anestetika snižují krevní tlak a tlumí dýchání — proto se vedou v kombinaci s dalšími složkami anestezie, ne samostatně ve vysoké dávce.")

S("50", "Celková anestetika — intravenózní",
  "ČTYŘI LÁHVE NA SÁLE — a jedna z nich se chová opačně než ostatní.", "laborator",
  [("🥛", "Bílá láhev propofolu", False, "PROPOFOL — nejužívanější, rychlý nástup i odeznění, antiemetický účinek. Nežádoucí: pokles krevního tlaku, útlum dechu, bolest při injekci; při dlouhé vysokodávkované infuzi propofolový infuzní syndrom."),
   ("🌀", "Ketamin", True, "KETAMIN je antagonista NMDA — disociativní anestezie se silnou analgezií. Na rozdíl od ostatních krevní tlak NEKLESÁ (stoupá) a dechová aktivita se zachovává — proto se hodí v šoku a v přednemocniční péči."),
   ("👻", "Halucinace při probouzení", True, "Ketamin působí halucinace a neklid při probouzení — tlumí je benzodiazepin. Esketamin se používá u farmakorezistentní deprese."),
   ("🫀", "Etomidát", False, "ETOMIDÁT je oběhově velmi stabilní — vhodný u kardiaka; tlumí ale syntézu kortizolu, proto se nepodává v infuzi."),
   ("💤", "Thiopental", True, "THIOPENTAL — účinek končí REDISTRIBUCÍ do svalu a tuku, nikoli eliminací; pacient se probudí rychle, ale látka v těle přetrvává a při opakovaném podání se kumuluje."),
   ("💉", "Opioid", False, "Anestezie se vede kombinací: hypnotikum + analgetikum (opioid) + myorelaxans."),
   ("⚖️", "Tři složky", False, "Jedna látka nezvládne všechny tři složky současně — proto se anestezie vždy skládá.")],
  "Ketamin je výjimkou z většiny pravidel o intravenózních anestetikách — proto se u něj vyplatí pamatovat si právě to, čím se liší.")
