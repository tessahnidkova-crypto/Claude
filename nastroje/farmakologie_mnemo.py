#!/usr/bin/env python3
"""Mnemotechnické obrazy ke všem 136 zkouškovým otázkám z farmakologie.

Každý zápis `S(...)` = jedna strana atlasu `MNEMO.pdf`:
  hak     — věta, která se má vybavit jako první
  panely  — 3–4 dvojice (glyf, popisek): obrázkový příběh zleva doprava
  rozklic — dvojice (co vidíš, co to doopravdy znamená) → převod obrazu na fakt
  past    — nejčastější omyl u téhle otázky

⚠️ **Mnemotechnika nesmí zakódovat nepravdu.** Chybný hák se naučí stejně
pevně jako správný a u zkoušky vypadne jako omyl. Proto je pravidlo: obraz smí
být přehnaný a absurdní, ale **rozklíčování se píše odborně a doslova**.

Přegeneruje se příkazem `python3 nastroje/gen_mnemo.py`.
"""
from mnemo import scena

O = []


def S(cislo, nadpis, hak, panely, rozklic, past=None):
    O.append((cislo, nadpis, scena(cislo, nadpis, hak, panely, rozklic, past)))


# ───────────────────────────────── OBECNÁ FARMAKOLOGIE ─────────────────────────

S("O1", "Farmakologie, původ a zdroje léčiv, názvy, lékopis",
  "Kinetika = KAM lék jde. Dynamika = CO tam dělá. Jedna cesta tam, druhá zpátky.",
  [("🧭", "KINETIKA: co dělá tělo s lékem"),
   ("💥", "DYNAMIKA: co dělá lék s tělem"),
   ("🌿", "Zdroje: rostlina, zvíře, mikrob, syntéza, biotechnologie"),
   ("📕", "LÉKOPIS: závazný předpis jakosti")],
  [("Kompas", "Farmakokinetika — absorpce, distribuce, metabolismus, exkrece (ADME)."),
   ("Výbuch", "Farmakodynamika — mechanismus účinku, vztah dávky a odpovědi."),
   ("Bylina a bakterie", "Zdroje: rostliny (morfin, atropin, digoxin), živočichové (heparin, inzulin), mikroorganismy (peniciliny), chemická syntéza, biotechnologie (monoklonální protilátky)."),
   ("Tři jména", "Chemický (vzorec) · generický = mezinárodní nechráněný (ibuprofen) · firemní chráněný (Brufen®)."),
   ("Červená kniha", "Lékopis — závazný soubor požadavků na jakost léčiv; Český vychází z Evropského.")],
  "Léčivá látka je nositel účinku; léčivý přípravek je hotová forma, kterou pacient dostane. Magistraliter se připravuje v lékárně, HVLP se vyrábí hromadně.")

S("O2", "Legislativa, doplňky stravy, zdravotnické prostředky, regulační orgány",
  "Lék musí DOKÁZAT, že funguje. Doplněk stravy jen nesmí LHÁT, že léčí. O kategorii rozhoduje mechanismus, ne složení.",
  [("⚖️", "LÉK: prokáže účinnost, bezpečnost, jakost"),
   ("🥤", "DOPLNĚK: právně potravina, stačí ohlášení"),
   ("🩹", "PROSTŘEDEK: působí FYZIKÁLNĚ"),
   ("🏛️", "SÚKL · EMA · SZPI")],
  [("Váhy", "Léčivý přípravek působí farmakologicky, imunologicky nebo metabolicky; registruje SÚKL národně nebo EMA centralizovaně."),
   ("Kelímek", "Doplněk stravy je potravina — účinnost dokládat nemusí, nesmí tvrdit, že léčí; dozor má SZPI."),
   ("Náplast", "Zdravotnický prostředek působí fyzikálně (výplň, implantát, obvaz) — posuzuje se shoda a riziková třída."),
   ("Budova", "SÚKL registruje, stanovuje ceny a úhrady, dozoruje lékárny a vede farmakovigilanci; klinické hodnocení schvaluje i etická komise.")],
  "Pacient rozdíl mezi lékem a doplňkem nevidí — na doplňky se proto ptej cíleně: mají reálné interakce (třezalka, ginkgo, česnek).")

S("O3", "Předepisování léčivých přípravků",
  "Recept je PRÁVNÍ dokument dvou lidí: lékař ručí za to, co předepsal, lékárník za to, co vydal.",
  [("💻", "eRecept: identifikátor do centrálního úložiště"),
   ("✍️", "Rp. — složení — M.f. — D.S."),
   ("🟦", "MODRÝ PRUH: omamné a psychotropní"),
   ("🔁", "Opakovací recept: uvádí počet opakování")],
  [("Dva podpisy", "Odpovědnost je sdílená — proto musí být recept čitelný a úplný."),
   ("Náležitosti", "Pacient (jméno, číslo pojištěnce) · léčivo (název, síla, forma, množství) · dávkování a způsob podání (D.S. = da signa) · lékař a pracoviště s podpisem a razítkem · datum."),
   ("Modrý pruh", "Vyhrazen omamným a psychotropním látkám, má přísnější evidenci."),
   ("Rp. = recipe", "„Vezmi“; M.f. = misce fiat („smíchej, ať vznikne“); D.S. = „vydej a označ“ — stavba magistraliter předpisu.")],
  "Platnost běžného receptu je zpravidla 14 dní, u antibiotik kratší [ověřit dle skript]. Před předepsáním patří anamnéza: alergie, gravidita, funkce jater a ledvin, ostatní léky.")

S("O4", "Preklinické a klinické hodnocení léčiv",
  "I. je to bezpečné? II. jaká dávka? III. je to lepší než dosavadní léčba? IV. co vzácného se objeví, až to bere milion lidí?",
  [("🐁", "PREKLINIKA: in vitro a na zvířeti"),
   ("💪", "I. desítky ZDRAVÝCH — bezpečnost"),
   ("🧪", "II. stovky nemocných — dávka · III. tisíce — srovnání"),
   ("🌍", "IV. běžná populace — vzácné nežádoucí účinky")],
  [("Myš", "Preklinika: farmakokinetika, farmakodynamika, toxicita (ED50, TD50, LD50), mutagenita, teratogenita, karcinogenita."),
   ("Fáze I", "Desítky zdravých dobrovolníků — snášenlivost a chování látky v těle; zahajuje se mikrodávkami s pomalou eskalací."),
   ("Fáze II a III", "II. stovky nemocných — hledá se účinná dávka. III. tisíce — srovnání s dosavadní léčbou nebo placebem; na jejím základě se registruje."),
   ("Fáze IV", "Po uvedení na trh — sledování v běžné populaci; teprve tady se odhalí vzácné nežádoucí účinky, protože ve studii na tisících pacientů neměly šanci vyjít najevo."),
   ("Zásady studie", "Randomizace, zaslepení (jednoduché, dvojité, trojité), kontrolní skupina, předem daný cíl, souhlas etické komise.")],
  "Generikum účinnost neprokazuje znovu — dokládá bioekvivalenci, tedy shodný průběh hladin s originálem.")

S("O5", "Způsoby aplikace léčiv, výhody a nevýhody",
  "Hlavní otázka není „jak rychle“, ale „PROJDE TO JÁTRY?“. First-pass obchází: pod jazyk, do žíly, do svalu, na kůži.",
  [("🚪", "PERORÁLNĚ: projde játry, first-pass"),
   ("👅", "SUBLINGVÁLNĚ: obchází játra — nitroglycerin"),
   ("💉", "I.V.: okamžitě, F = 100 %, nevratné"),
   ("🩹", "TRANSDERMÁLNĚ: nejpomalejší, účinek dny")],
  [("Dveře do jater", "Perorální podání = vrátnice: látka projde střevní stěnou a játry dřív, než se dostane do oběhu. Proto se stejný lék podává ústy v mnohem vyšší dávce než do žíly."),
   ("Jazyk", "Sublingválně a bukálně se látka vstřebá rovnou do systémového oběhu — obchází first-pass; proto nitroglycerin pod jazyk."),
   ("Stříkačka", "I.v. má z definice biologickou dostupnost 100 % a okamžitý účinek — ale podané se nedá vzít zpět. I.m. rychlé, s.c. pomalejší (inzulin, hepariny)."),
   ("Náplast", "Nejpomalejší nástup, ale stálá hladina po dny; po sejmutí účinek doznívá z kožního depa.")],
  "„Místní“ podání neznamená „bez celkového účinku“ — oční, nosní i inhalační formy se vstřebávají. Timolol z očních kapek vyvolá bradykardii a bronchospasmus.")

S("O6", "Lékové formy — perorální a orální",
  "PER os = skrz ústa dál do střeva. ORÁLNÍ = zůstává v ústech. A obojí, co má obal nebo je retardované, se NESMÍ DRTIT.",
  [("💊", "Perorální: polkne se, působí po vstřebání"),
   ("🍬", "Orální: pastilka zůstává v ústech"),
   ("🛡️", "Enterosolventní obal projde žaludkem"),
   ("⛔", "Retardované formy NEDRTIT")],
  [("Skrz ústa dál", "Perorální formy: tablety, potahované tablety, tobolky, granuláty, sirupy, suspenze, kapky."),
   ("Zůstává v ústech", "Orální formy: pastilky, žvýkací tablety, ústní vody, gely. Sublingválně a bukálně se látka vstřebá do krve a obejde first-pass."),
   ("Štít", "Enterosolventní obal se rozpadne až ve střevě — chrání látku před kyselinou, nebo žaludek před látkou."),
   ("Zákaz drcení", "Retardované formy (SR, ZOK) uvolňují látku postupně; rozdrcením se uvolní celá denní dávka najednou nebo se látka zničí."),
   ("Pomocné látky", "Nejsou neutrální: laktóza vadí při intoleranci, barviva mohou vyvolat alergii, cukr v sirupech je při dlouhodobé léčbě rizikový.")],
  "Rozpad a rozpuštění předchází vstřebání — u málo rozpustných léčiv je rychlost rozpouštění krokem, který určuje rychlost nástupu účinku.")

S("O7", "Lékové formy — parenterální a dermatologika",
  "Parenterální forma obchází všechny přirozené bariéry — proto musí být sterilní. A co je jednou v žíle, nevrátíš.",
  [("🧼", "Sterilní, apyrogenní, izotonický, izohydrický"),
   ("🩸", "Rychlost sleduje PROKRVENÍ"),
   ("🚫", "Suspenze NIKDY i.v. — embolizace"),
   ("🧴", "Mast → krém → gel: čím tučnější, tím hlouběji")],
  [("Mýdlo", "Přípravek obchází kůži i sliznici, proto musí být sterilní, apyrogenní (bez pyrogenů), izotonický, izohydrický a bez mechanických nečistot."),
   ("Krev", "I.v. okamžitě a se 100% dostupností · i.m. rychle · s.c. pomaleji · depotní formy a náplasti nejpomaleji, ale působí dny až měsíce."),
   ("Zákaz", "Suspenze a emulze se nepodávají i.v. — hrozí embolizace."),
   ("Tuba", "Mast (tučný základ, největší průnik, na suchou kůži) · krém (voda i tuk) · gel (vodný, chladí) · pasta · zásyp · roztok · náplast. Průnik zvyšuje okluze."),
   ("Výhody a nevýhody", "Jistá dostupnost, přesné dávkování, použitelné u zvracení a bezvědomí — proti tomu bolestivost, riziko infekce a embolie, nutný personál a nevratnost podání.")],
  "Lokální kortikoidy dlouhodobě způsobí atrofii kůže a strie — na obličej a do záhybů patří jen slabé přípravky a krátce, protože se tam vstřebávají nejvíc.")

S("O8", "Lékové formy — oční, ušní, nosní, rektalia, vaginalia, inhalanda",
  "„Místní“ znamená KAM to dáváš, ne KDE to působí. Kapka do oka umí zpomalit srdce.",
  [("👁️", "Oční: sterilní, izotonické — timolol dělá bradykardii"),
   ("👃", "Nosní: dekongescencia jen 5–7 dní"),
   ("🫁", "Inhalanda: rozhoduje TECHNIKA, nástavec"),
   ("🍑", "Rektalia: first-pass obchází jen zčásti")],
  [("Oko", "Kapky, masti a gely musí být sterilní a izotonické. Timolol z kapek vyvolá bradykardii a bronchospasmus; vstřebání sníží stisknutí vnitřního koutku po nakapání."),
   ("Nos", "Xylometazolin jen 5–7 dní, jinak vzniká rhinitis medicamentosa. Nosní cestou se podává i desmopresin a sumatriptan k celkovému účinku."),
   ("Plíce", "Aerosolový dávkovač, práškový inhalátor, nebulizace. Nástavec zlepší depozici a sníží nežádoucí účinky — bez něj inhalační kortikoid vyvolá orofaryngeální kandidózu a chrapot."),
   ("Konečník", "Rektalia obcházejí játra jen z dolní části konečníku, vstřebávání je kolísavé; hodí se u zvracení, u dětí a v bezvědomí (diazepam u křečí)."),
   ("Ucho a pochva", "Ušní kapky se nesmí podat při perforaci bubínku. Vaginalia slouží hlavně k místní léčbě, ale i odsud se látka částečně vstřebává.")],
  "Vstřebání ze sliznice může být rychlejší než ze střeva — nosní a bukální sliznice jsou dobře prokrvené a first-pass obcházejí.")

S("O9", "Komunikace, adherence, compliance, placebo a nocebo",
  "Tvoje slova jsou účinná látka. Mají dávku, nástup i nežádoucí účinky — a špatně podaná informace udělá z léku nefunkční lék.",
  [("👂", "COMPLIANCE: pacient dodržuje pokyny"),
   ("🤝", "ADHERENCE: dodrží plán, na kterém se podílel"),
   ("✨", "PLACEBO: očekávání zlepšení — má neurobiologický podklad"),
   ("🌩️", "NOCEBO: očekávání škody vytvoří potíž")],
  [("Ucho", "Compliance — míra, do jaké pacient dodržuje pokyny; pasivní pojetí."),
   ("Podání ruky", "Adherence — pacient se na plánu podílel; konkordance je společné rozhodnutí lékaře a pacienta. Dnes se preferuje adherence, protože zdůrazňuje spoluodpovědnost."),
   ("Jiskra", "Placebo — očekávané zlepšení; má neurobiologický podklad (endogenní opioidy, dopamin), není „vymyšlené“ a zesiluje účinek každého skutečného léku."),
   ("Blesk", "Nocebo — očekávaná škoda; nepříznivé věty a příbalový leták vyvolají potíž. Odsud časté vysazení statinů a antidepresiv."),
   ("Proč léčba selhává", "Nejčastěji ne špatný lék, ale nebraný lék: hypertenze, osteoporóza, složitý režim, mnoho tablet, nežádoucí účinky a obavy z nich, cena, nepochopení a nedůvěra.")],
  "Zlepší to fixní kombinace (méně tablet), dávkování 1× denně, srozumitelné vysvětlení a kontrola. Formulace lékaře je proto sama o sobě účinná látka s vlastní dávkou.")

S("O10", "Přechod látek biologickými membránami",
  "Membrána je TUKOVÁ STĚNA. Projde jen látka lipofilní a NENABITÁ. Nabitá forma zůstane stát přede dveřmi.",
  [("🧈", "Membrána = tuková dvojvrstva"),
   ("🚶", "Prostá difuze: po spádu, zdarma"),
   ("🔋", "Aktivní transport: proti spádu, za ATP"),
   ("🪤", "IONTOVÁ PAST: nabitá forma se nevrátí")],
  [("Máslo", "Přes membránu projde jen látka lipofilní a nenabitá; nabitá (ionizovaná) forma neprojde."),
   ("Chodec", "Prostá difuze — po koncentračním spádu, bez energie a bez přenašeče; hlavní mechanismus u většiny léčiv."),
   ("Baterie", "Aktivní transport — proti spádu, spotřebuje ATP, saturovatelný (např. P-glykoprotein, který léčiva aktivně vypuzuje z buňky). Facilitovaná difuze jde přenašečem, ale po spádu a bez energie."),
   ("Past", "Látka projde membránou v nenabité formě, na druhé straně se při jiném pH nabije a zpět už neprojde — tak se hromadí (a proto se alkalizací moči urychlí vyloučení salicylátů)."),
   ("Bariéry", "Hematoencefalická (těsné spoje + P-glykoprotein), placentární (propustnější, než se čeká), krev–varle, krev–sítnice. Zánět bariéru zpropustní — proto penicilin proniká do CNS jen při meningitidě.")],
  "Proto lokální anestetikum nezabírá v kyselém zánětlivém prostředí: převáží nabitá forma, která přes membránu neprojde k sodíkovému kanálu.")

S("O11", "Základní farmakokinetické parametry a procesy",
  "ADME. A eliminace není totéž co exkrece — eliminace = metabolismus PLUS vylučování.",
  [("🅰️", "A — absorpce (vstup do krve)"),
   ("🅳", "D — distribuce (rozvod do tkání)"),
   ("🅼", "M — metabolismus (přeměna, hlavně játra)"),
   ("🅴", "E — exkrece (vyloučení, hlavně ledviny)")],
  [("ADME", "Čtyři děje osudu léčiva v těle; probíhají současně, ne po sobě."),
   ("Eliminace", "Metabolismus + exkrece dohromady — proto se „eliminace“ a „vylučování“ nesmí zaměňovat."),
   ("F", "Biologická dostupnost — podíl dávky, který se dostane nezměněný do systémového oběhu; i.v. = 100 %."),
   ("Vd", "Distribuční objem — zdánlivý, poměr dávky k plazmatické koncentraci. Vysoké Vd znamená, že látka sedí ve tkáních, ne v krvi (proto ji dialýza neodstraní)."),
   ("CL a t½", "Clearance — objem krve očištěný za čas. Biologický poločas — doba poklesu koncentrace na polovinu; ustálený stav nastane za 4–5 poločasů a stejně dlouho trvá vymizení.")],
  "Farmakokinetika = co tělo dělá s lékem. Farmakodynamika = co lék dělá s tělem. AUC (plocha pod křivkou) je celková expozice, Cmax vrchol a tmax doba do vrcholu.")

S("O12", "Procesy nultého a prvního řádu, saturační kinetika",
  "První řád = ubývá stále stejný PODÍL. Nultý řád = ubývá stále stejné MNOŽSTVÍ. Nasycený enzym víc nestihne, i kdyby chtěl.",
  [("📉", "1. řád: konstantní PODÍL za čas — exponenciála"),
   ("⏳", "0. řád: konstantní MNOŽSTVÍ za čas — přímka"),
   ("🍺", "Ethanol: 0,1–0,15 ‰ za hodinu, vždy stejně"),
   ("⚠️", "Saturace: malé zvýšení dávky → prudký vzestup hladiny")],
  [("Klesající křivka", "Kinetika prvního řádu — odbourává se konstantní podíl (polovina za poločas); platí pro naprostou většinu léčiv, protože enzymy mají kapacitní rezervu."),
   ("Přesýpací hodiny", "Kinetika nultého řádu — enzym je nasycený, odbourává konstantní množství za čas bez ohledu na koncentraci. Pokles je lineární a poločas ztrácí smysl."),
   ("Pivo", "Ethanol se odbourává řádově 0,1–0,15 ‰ za hodinu — rychlost nelze urychlit ničím. Proto nelze počítat „za dva poločasy bude polovina“."),
   ("Michaelisova–Mentenové kinetika", "Přechod mezi obojím: při nízké koncentraci první řád, po nasycení enzymu nultý. Chová se tak fenytoin, salicyláty a theofylin."),
   ("Klinický důsledek", "U saturačního léčiva stačí malé zvýšení dávky a hladina vyskočí do toxického pásma — nystagmus, ataxie, zmatenost u fenytoinu. Proto se měří hladiny.")],
  "Ustálený stav (steady state) nastane za 4–5 poločasů a stejně dlouho trvá, než lék vymizí — proto se u dlouhého poločasu podává nasycovací dávka.")

S("O13", "Absorpce, Batemanova funkce, biologická dostupnost, AUC",
  "Cmax není konec vstřebávání — je to REMÍZA: okamžik, kdy se rychlost vstřebávání vyrovná rychlosti eliminace.",
  [("⚖️", "Cmax = rychlost vstupu se rovná rychlosti eliminace"),
   ("📈", "Batemanova křivka: vzestup, vrchol, pokles"),
   ("🧮", "AUC = celková expozice organismu"),
   ("🔀", "F = podíl dávky, který dorazil nezměněný")],
  [("Váhy", "Ve vrcholu (Cmax) se vstřebávání a eliminace vyrovnají — vstřebávání pokračuje i po něm, jen ho eliminace převáží."),
   ("Křivka", "Batemanova funkce popisuje průběh koncentrace po jednorázovém perorálním podání: vzestupná fáze (převažuje absorpce), vrchol, sestupná fáze (převažuje eliminace)."),
   ("Kalkulačka", "AUC = plocha pod křivkou = celková expozice; podle ní se srovnává originál s generikem (bioekvivalence)."),
   ("Biologická dostupnost", "F = podíl podané dávky, který se dostane nezměněný do systémového oběhu. Snižuje ji neúplné vstřebání a first-pass metabolismus."),
   ("Co ovlivní vstřebání", "Léková forma, rozpustnost, pH, jídlo, motilita, prokrvení, současně podaná léčiva (antacida, železo, vápník váží tetracykliny a chinolony).")],
  "tmax vypovídá o rychlosti vstřebávání, Cmax a AUC o rozsahu. Generikum musí mít shodné AUC i Cmax v předepsaném rozmezí — proto se u něj nezkoumá znovu účinnost.")

S("O14", "Distribuce, distribuční objem, redistribuce, vazba na bílkoviny, bariéry",
  "Vd je ZDÁNLIVÝ objem — ne skutečný. Vysoké Vd znamená: „lék není v krvi, sedí ve tkáních“ — a dialýza ho nedostane ven.",
  [("🫙", "Vd = dávka ÷ plazmatická koncentrace"),
   ("🛋️", "Vysoké Vd → lék je ve tkáních, ne v krvi"),
   ("🔗", "Vázaná frakce je NEÚČINNÁ, jen volná působí"),
   ("🧠", "Bariéry: hematoencefalická, placentární")],
  [("Nádoba", "Distribuční objem je zdánlivý — je to počítaná veličina, ne anatomický prostor. Může mnohonásobně převýšit objem těla."),
   ("Gauč", "Vysoké Vd = lék je uložený ve tkáních (tuk, sval), v krvi ho je málo — proto ho hemodialýza neodstraní (digoxin, antidepresiva)."),
   ("Řetěz", "Účinná je jen volná frakce. Albumin váže kyselé látky (warfarin, fenytoin), orosomukoid (kyselý α1-glykoprotein) zásadité. Při hypoalbuminemii stoupá volná frakce a s ní účinek i toxicita."),
   ("Mozek", "Hematoencefalická bariéra — těsné spoje a P-glykoprotein; propustí jen lipofilní a nenabité látky. Placentární bariéra je propustnější, než se obvykle čeká."),
   ("Redistribuce", "Thiopental uspí rychle, protože se dostane do mozku, a probudí rychle, protože se přesune do svalu a tuku — konec účinku dělá přesun, ne eliminace.")],
  "Vytěsnění z vazby na bílkovinu je klasická interakce (sulfonamidy vytěsní warfarin), ale samo o sobě bývá klinicky přechodné — nebezpečné je, když se k němu přidá i útlum metabolismu.")

S("O15", "Eliminace, poločas, fáze α a β, eliminační konstanta, clearance",
  "Za 4–5 poločasů se hladina ustálí — a stejně dlouho trvá, než lék po vysazení zmizí. Poločas je hodiny, ne účinek.",
  [("½", "t½ — pokles koncentrace na polovinu"),
   ("🅰️", "Fáze α = distribuce · fáze β = vlastní eliminace"),
   ("🚰", "CL — objem krve očištěný za jednotku času"),
   ("4️⃣", "4–5 poločasů: ustálený stav i vymizení")],
  [("Polovina", "Biologický poločas — doba, za kterou klesne koncentrace na polovinu. U kinetiky prvního řádu je konstantní a nezávisí na dávce."),
   ("Dvě fáze", "Po i.v. podání klesá koncentrace nejprve strmě (fáze α — rozvod do tkání), pak pozvolna (fáze β — skutečná eliminace). Poločas se počítá z fáze β."),
   ("Kohoutek", "Clearance = objem plazmy zcela očištěný za jednotku času; sčítá se renální a jaterní (CL = CLren + CLhep). Vztah: t½ = 0,693 × Vd ÷ CL."),
   ("Čtyřka", "Za 4–5 poločasů se dosáhne ustáleného stavu při opakovaném podávání — a stejně dlouho trvá vymizení po vysazení."),
   ("Eliminační konstanta", "kel — podíl látky odstraněný za jednotku času; t½ = 0,693 ÷ kel.")],
  "Poločas roste, když klesne clearance (jaterní nebo renální selhání) NEBO když stoupne Vd — proto nestačí sledovat jen ledviny.")

S("O16", "Dávkovací režim, kumulace, kumulační index",
  "Když podáš další dávku dřív, než se vyloučí ta předchozí, lék se HROMADÍ. Nasycovací dávka řeší čekání, udržovací drží hladinu.",
  [("📚", "KUMULACE: interval kratší než eliminace"),
   ("🚀", "NASYCOVACÍ dávka — zkrátí čekání na účinek"),
   ("🔄", "UDRŽOVACÍ dávka — nahrazuje ztrátu"),
   ("📊", "Kratší interval = menší kolísání hladiny")],
  [("Hromada", "Kumulace nastane, je-li dávkovací interval kratší než doba potřebná k eliminaci; ustálí se po 4–5 poločasech."),
   ("Raketa", "Nasycovací dávka = Vd × cílová koncentrace. Podává se, když je poločas dlouhý a nelze čekat 4–5 poločasů na účinek."),
   ("Kolotoč", "Udržovací dávka = CL × cílová koncentrace × interval. Nahrazuje to, co se za interval vyloučí."),
   ("Graf", "Krátký interval a malé dávky = plochá, stabilní hladina. Dlouhý interval a velké dávky = větší kolísání mezi vrcholem a údolím — riziko u léčiv s úzkým terapeutickým oknem."),
   ("Kumulační index", "Poměr koncentrace v ustáleném stavu k té po první dávce; udává, kolikrát se hladina nahromadí.")],
  "Nasycovací dávka závisí na Vd, udržovací na clearance — proto se u renální insuficience krátí udržovací dávka, ale nasycovací zůstává stejná.")

S("O17", "Biotransformace léčiv, fáze, příklady",
  "Fáze I. látku ROZBIJE a odhalí funkční skupinu. Fáze II. na ni PŘILEPÍ velkou vodorozpustnou molekulu, aby šla ven.",
  [("🔨", "I. fáze: oxidace, redukce, hydrolýza (CYP450)"),
   ("🏷️", "II. fáze: konjugace — glukuronidace, sulfatace"),
   ("💧", "Cíl: z lipofilní látky udělat hydrofilní"),
   ("⚡", "Metabolit může být ÚČINNĚJŠÍ než původní látka")],
  [("Kladivo", "I. fáze — oxidace (hlavně cytochromy P450, nejvíc CYP3A4), redukce, hydrolýza. Vzniká reaktivnější metabolit s odhalenou funkční skupinou."),
   ("Štítek", "II. fáze — konjugace: glukuronidace, sulfatace, acetylace, methylace, vazba na glutathion. Produkt je velký, polární a snadno vyloučitelný."),
   ("Kapka", "Smyslem je změnit lipofilní látku na hydrofilní — jinak by se v ledvinách stále zpětně vstřebávala."),
   ("Blesk", "Proléčivo se aktivuje až metabolismem: kodein → morfin (CYP2D6), enalapril → enalaprilát, cyklofosfamid, klopidogrel. Metabolit může být i toxický: paracetamol → NAPQI."),
   ("Kde", "Především játra, ale i střevní stěna, plíce, ledviny a plazma (esterázy).")],
  "Novorozenec má nezralou glukuronidaci — odtud gray baby syndrom po chloramfenikolu. U starších klesá hlavně I. fáze, II. fáze zůstává poměrně zachovaná.")

S("O18", "Úloha jater v eliminaci léčiv, first-pass efekt",
  "Co se vstřebá ze střeva, jde NEJPRVE do jater — teprve zbytek doputuje do těla. Proto je perorální dávka mnohonásobně vyšší než nitrožilní.",
  [("🚪", "Střevo → portální žíla → JÁTRA → oběh"),
   ("📉", "First-pass sníží dostupnost, někdy pod 10 %"),
   ("🔁", "Enterohepatální oběh: žluč → střevo → zpět"),
   ("🫀", "Vysoká extrakce = závisí na PRŮTOKU játry")],
  [("Vrátnice", "Vše vstřebané ze střeva projde portální žílou játry dřív, než se dostane do systémového oběhu."),
   ("Pokles", "Silný first-pass mají nitroglycerin, propranolol, morfin, verapamil, lidokain — proto se nitroglycerin podává sublingválně a lidokain se ústy nepodává vůbec."),
   ("Kruh", "Enterohepatální oběh: látka se vyloučí žlučí, ve střevě se uvolní zpět a znovu vstřebá — prodlužuje účinek (kontraceptiva; proto antibiotika mohou jejich účinnost snížit)."),
   ("Srdce", "U léčiv s vysokou jaterní extrakcí limituje eliminaci průtok játry — při srdečním selhání a šoku hladiny stoupají. U nízké extrakce rozhoduje enzymatická kapacita a vazba na bílkoviny."),
   ("Jaterní selhání", "Klesá metabolismus i tvorba albuminu, roste volná frakce a zkratový oběh obchází játra — dávky se snižují.")],
  "Rektální podání obchází first-pass jen zčásti (dolní část konečníku), proto je vstřebávání kolísavé. Sublingválně a transdermálně se játra obejdou zcela.")
