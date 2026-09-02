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

S("O19", "Inhibice a indukce enzymů léčivy, klinický význam",
  "INHIBICE je rychlá a hladina VYSKOČÍ. INDUKCE je pomalá a hladina SPADNE — musí se nasyntetizovat nový enzym.",
  [("🛑", "INHIBICE: během hodin ↑ hladina → toxicita"),
   ("🏭", "INDUKCE: za dny až týdny ↓ hladina → selhání léčby"),
   ("🍊", "Grapefruit, azoly, makrolidy = inhibitory"),
   ("🔥", "Rifampicin, karbamazepin, fenytoin, třezalka = induktory")],
  [("Stopka", "Inhibitor obsadí enzym hned — hladina druhého léčiva stoupá během hodin až dnů a hrozí toxicita."),
   ("Továrna", "Induktor spouští tvorbu nového enzymu — trvá dny až týdny, než se plně projeví, a stejně dlouho odeznívá. Hladina druhého léčiva klesne a léčba selže."),
   ("Inhibitory", "Grapefruitová šťáva, azolová antimykotika (flukonazol, itrakonazol), makrolidy (erythromycin, klarithromycin — nikoli azithromycin), ciprofloxacin, verapamil, amiodaron, ritonavir."),
   ("Induktory", "Rifampicin, karbamazepin, fenytoin, fenobarbital, třezalka tečkovaná; chronicky alkohol a kouření (CYP1A2)."),
   ("Co to udělá", "Rifampicin sníží účinnost hormonální kontracepce, warfarinu a antiretrovirotik. Klarithromycin se statinem zvýší riziko rabdomyolýzy.")],
  "U proléčiva je to obráceně: inhibitor CYP2D6 (fluoxetin, paroxetin) sníží účinek kodeinu a klopidogrelu, protože zabrání jejich AKTIVACI.")

S("O20", "Vylučování léčiv renální a extrarenální",
  "Ledvina dělá tři věci: FILTRUJE, SEKRETUJE a část zase VSTŘEBÁ ZPĚT. Vyloučí se jen to, co je vodorozpustné.",
  [("🫧", "Glomerulární filtrace: jen VOLNÁ frakce"),
   ("➡️", "Tubulární sekrece: aktivní, saturovatelná"),
   ("↩️", "Zpětná resorpce: lipofilní látky se vracejí"),
   ("💨", "Extrarenálně: žluč, plíce, mléko, sliny, pot")],
  [("Filtr", "Glomerulem projde jen volná (nenavázaná) frakce; látka vázaná na albumin se nefiltruje."),
   ("Šipka ven", "Tubulární sekrece je aktivní transport se společnými přenašeči — proto probenecid zpomaluje vylučování penicilinu (soupeří o týž přenašeč)."),
   ("Šipka zpět", "Lipofilní a nenabité látky se z tubulu vstřebávají zpět. Změnou pH moči se to dá ovlivnit: alkalizace bikarbonátem urychlí vyloučení kyselých látek (salicyláty, barbituráty)."),
   ("Pára", "Extrarenální cesty: žluč a stolice (a enterohepatální oběh), plíce (inhalační anestetika, ethanol — odtud dechová zkouška), mateřské mléko, sliny, pot."),
   ("Renální insuficience", "Dávky léčiv vylučovaných ledvinami se snižují podle clearance kreatininu — aminoglykosidy, digoxin, metformin, lithium, mnohá antibiotika.")],
  "Vyloučit se dá jen látka vodorozpustná — proto předchází biotransformace. Lipofilní látka by se v tubulu jen stále dokola vstřebávala zpět.")

S("O21", "Účinek léčiv obecně, způsob účinku na molekulární úrovni",
  "Většina léčiv se váže na CÍLOVOU STRUKTURU — receptor, enzym, kanál nebo přenašeč. Nespecifický účinek žádnou cílovou strukturu nepotřebuje.",
  [("🎯", "SPECIFICKÝ: vazba na cílovou strukturu"),
   ("🧂", "NESPECIFICKÝ: fyzikálně-chemický (antacida, osmotika)"),
   ("🔓", "AGONISTA aktivuje · ANTAGONISTA blokuje"),
   ("⚗️", "Enzymy, kanály, přenašeče, nukleové kyseliny")],
  [("Terč", "Specifický účinek — vazba na receptor, enzym, iontový kanál, přenašeč nebo nukleovou kyselinu; je strukturně závislý a nasytitelný."),
   ("Sůl", "Nespecifický účinek — fyzikálně-chemický, bez cílové struktury: antacida neutralizují kyselinu, osmotická projímadla táhnou vodu, aktivní uhlí adsorbuje, celková anestetika mění vlastnosti membrány."),
   ("Klíč", "Agonista se váže a receptor aktivuje (má afinitu i vnitřní aktivitu). Antagonista se váže, ale neaktivuje (má jen afinitu) — brání navázání agonisty."),
   ("Cílové struktury", "Enzymy (statiny na HMG-CoA-reduktázu, ACE inhibitory), iontové kanály (lokální anestetika na sodíkové, blokátory kalciových kanálů), přenašeče (SSRI na serotoninový transportér, IPP na H+/K+-ATPázu), nukleové kyseliny (cytostatika, chinolony).")],
  "Účinek léčiva je vždy jen zesílení nebo zeslabení děje, který v těle už existuje — lék nevytváří novou funkci.")

S("O22", "Specifický účinek, cílové struktury, receptorová teorie, typy receptorů",
  "AFINITA = jak pevně se to naváže. VNITŘNÍ AKTIVITA = jestli to po navázání něco udělá. Antagonista má afinitu, ale nulovou aktivitu.",
  [("🧲", "AFINITA: síla vazby"),
   ("⚡", "VNITŘNÍ AKTIVITA: co to po navázání spustí"),
   ("🚪", "Ionotropní (ms) · metabotropní G-protein (s)"),
   ("🧬", "Nitrobuněčné receptory: hodiny až dny")],
  [("Magnet", "Afinita — jak pevně se ligand váže; určuje potřebnou koncentraci."),
   ("Blesk", "Vnitřní aktivita — co se po navázání stane. Plný agonista 1, parciální agonista mezi 0 a 1 (buprenorfin), antagonista 0, inverzní agonista pod 0 (utlumí i bazální aktivitu — H1-antihistaminika)."),
   ("Dveře", "Ionotropní receptory jsou samy iontovým kanálem — účinek za milisekundy (nikotinový acetylcholinový, GABA-A, NMDA). Metabotropní jdou přes G-protein a druhého posla — sekundy (muskarinové, adrenergní, opioidní)."),
   ("DNA", "Nitrobuněčné (jaderné) receptory mění přepis genů — účinek za hodiny až dny (kortikosteroidy, hormony štítné žlázy, pohlavní hormony). Odsud jejich pomalý nástup."),
   ("Antagonismus", "Kompetitivní — překonatelný vyšší dávkou agonisty, posouvá křivku doprava. Nekompetitivní — nepřekonatelný, snižuje maximum.")],
  "Down-regulace (úbytek receptorů při trvalé stimulaci) vysvětluje toleranci; up-regulace při dlouhé blokádě vysvětluje rebound fenomén po náhlém vysazení β-blokátoru.")

S("O23", "Dávka a účinek, terapeutický index, terapeutické okno, riziko, NNT",
  "Terapeutické okno je pruh mezi „ještě to nefunguje“ a „už to škodí“. U digoxinu, warfarinu a lithia je ten pruh úzký jako vlas.",
  [("🪟", "TERAPEUTICKÉ OKNO: účinné, ale ne toxické"),
   ("📏", "TI = TD50 ÷ ED50 — čím vyšší, tím bezpečnější"),
   ("🩺", "Úzké okno → MONITOROVAT HLADINY"),
   ("🔢", "NNT: kolik pacientů léčit, aby prospěl jednomu")],
  [("Okno", "Terapeutické okno — rozmezí koncentrací mezi minimální účinnou a toxickou."),
   ("Pravítko", "Terapeutický index TI = TD50 ÷ ED50 (u zvířat LD50 ÷ ED50). ED50 = dávka účinná u poloviny, TD50 = toxická u poloviny, LD50 = smrtelná pro polovinu."),
   ("Fonendoskop", "Úzký terapeutický index mají digoxin, warfarin, theofylin, lithium, fenytoin, aminoglykosidy, cyklosporin — u nich se měří plazmatické hladiny."),
   ("Číslice", "NNT (number needed to treat) — kolik pacientů je třeba léčit, aby se u jednoho zabránilo příhodě; nízké NNT = účinná léčba. Obdobně NNH pro poškození."),
   ("Křivka", "Vztah dávky a účinku je sigmoidní (v logaritmickém měřítku). Účinnost (efficacy) = jak vysokého maxima lék dosáhne; potence = jak malá dávka k tomu stačí.")],
  "Potentnější lék není lepší lék — znamená jen nižší potřebnou dávku. Rozhoduje maximální dosažitelný účinek a bezpečnost, ne velikost tablety.")

S("O24", "Vlivy působící na kinetiku a dynamiku léčiv",
  "Stejná dávka, jiný člověk, jiný účinek. Rozhodují játra, ledviny, věk, geny, další léky a jídlo.",
  [("👶", "VĚK: novorozenec i senior mají jinou kinetiku"),
   ("🫘", "ORGÁNY: játra a ledviny určují eliminaci"),
   ("🧬", "GENY: rychlý a pomalý metabolizátor"),
   ("🍽️", "JÍDLO, kouření, alkohol, další léky")],
  [("Dítě", "Novorozenec má nezralou glukuronidaci a vyšší podíl vody; senior má nižší glomerulární filtraci, nižší albumin, méně svaloviny a více tuku (lipofilní léčiva se hromadí)."),
   ("Ledvina", "Jaterní selhání snižuje metabolismus a tvorbu albuminu; renální insuficience zpomaluje vylučování. U obojího se dávky snižují."),
   ("DNA", "Polymorfismus CYP2D6, CYP2C9, CYP2C19, NAT2, TPMT rozhoduje, zda je člověk pomalý, či ultrarychlý metabolizátor."),
   ("Talíř", "Jídlo mění vstřebávání (mléko a antacida váží tetracykliny), grapefruit inhibuje CYP3A4, kouření indukuje CYP1A2 (theofylin, klozapin, olanzapin), alkohol akutně inhibuje a chronicky indukuje."),
   ("Dynamika", "Mění se i citlivost cílové struktury: u seniorů vyšší citlivost na benzodiazepiny a opioidy, při hypokalemii vyšší toxicita digoxinu.")],
  "Gravidita mění obojí: roste objem distribuce a glomerulární filtrace, klesá albumin — a přibývá otázka, co projde placentou.")

S("O25", "Lékové interakce",
  "Interakce jsou dvojího druhu: FARMAKOKINETICKÉ (lék A změní hladinu léku B) a FARMAKODYNAMICKÉ (oba táhnou za týž provaz).",
  [("🧪", "KINETICKÉ: vstřebávání, vazba, metabolismus, vylučování"),
   ("🤼", "DYNAMICKÉ: sčítání nebo rušení účinku"),
   ("🍇", "Grapefruit inhibuje CYP3A4"),
   ("🌼", "Třezalka indukuje CYP3A4 a P-glykoprotein")],
  [("Zkumavka", "Farmakokinetické: vstřebávání (antacida a železo váží tetracykliny a chinolony), vazba na bílkoviny (vytěsnění warfarinu), metabolismus (inhibice a indukce CYP450), vylučování (probenecid a penicilin)."),
   ("Přetahovaná", "Farmakodynamické: synergie (alkohol + benzodiazepiny = útlum dechu; ACE inhibitor + kalium šetřící diuretikum = hyperkalemie) nebo antagonismus (β-blokátor ruší účinek β2-agonisty u astmatu)."),
   ("Grapefruit", "Inhibuje střevní CYP3A4 → prudce zvýší hladinu statinů, blokátorů kalciových kanálů a imunosupresiv."),
   ("Třezalka", "Silný induktor CYP3A4 a P-glykoproteinu → sníží účinnost kontracepce, warfarinu, cyklosporinu, digoxinu a antiretrovirotik."),
   ("Nejrizikovější dvojice", "Warfarin s čímkoli · statin s makrolidem nebo azolem · NSA s antikoagulanciem · látky prodlužující QT navzájem · serotonergní léčiva navzájem.")],
  "Nejvíc interakcí nevzniká z léků na předpis, ale z toho, co pacient nehlásí: volně prodejná NSA, doplňky stravy a bylinky.")

S("O26", "Farmakogenetika, genetický polymorfismus",
  "Stejná dávka může být u jednoho neúčinná a u druhého toxická — rozhoduje, jestli je POMALÝ, nebo ULTRARYCHLÝ metabolizátor.",
  [("🐢", "POMALÝ metabolizátor: hladina stoupá → toxicita"),
   ("🐇", "ULTRARYCHLÝ: hladina klesá → léčba nefunguje"),
   ("💊", "U PROLÉČIVA je to naopak"),
   ("🧾", "Testuje se: HLA-B*5701, TPMT, G6PD")],
  [("Želva", "Pomalý metabolizátor odbourává léčivo pomalu — hladina stoupá a hrozí toxicita (CYP2D6 a antidepresiva, CYP2C9 a warfarin)."),
   ("Zajíc", "Ultrarychlý metabolizátor odbourá léčivo dřív, než stačí zabrat — léčba selhává."),
   ("Proléčivo", "U proléčiva se to obrací: ultrarychlý metabolizátor CYP2D6 vytvoří z kodeinu nebezpečně mnoho morfinu, pomalý metabolizátor nemá z kodeinu ani z klopidogrelu žádný účinek."),
   ("Testy", "HLA-B*5701 před abakavirem (hypersenzitivita), HLA-B*5801 před allopurinolem, TPMT před azathioprinem a 6-merkaptopurinem (myelosuprese), G6PD před primachinem a sulfonamidy (hemolýza), NAT2 a rychlost acetylace izoniazidu.")],
  "Farmakogenetika vysvětluje i idiosynkrazii — geneticky podmíněnou neobvyklou reakci, například maligní hypertermii po sukcinylcholinu a halotanu.")

S("O27", "Tolerance, tachyfylaxe, rezistence",
  "TOLERANCE se buduje dny až týdny. TACHYFYLAXE je bleskurychlá — přijde během minut a novou dávkou ji nepřekonáš.",
  [("📉", "TOLERANCE: postupně slábne účinek"),
   ("⚡", "TACHYFYLAXE: rychlé vyčerpání, během minut"),
   ("🦠", "REZISTENCE: netýká se člověka, ale mikroba"),
   ("🔀", "ZKŘÍŽENÁ tolerance mezi látkami stejného mechanismu")],
  [("Klesající křivka", "Tolerance — na týž účinek je třeba stále vyšší dávka. Farmakodynamická (down-regulace receptorů) nebo farmakokinetická (indukce vlastního metabolismu, např. barbituráty)."),
   ("Blesk", "Tachyfylaxe — velmi rychlý pokles účinku při opakovaném podání v krátkém sledu, typicky vyčerpáním zásoby mediátoru (efedrin) nebo obsazením receptorů; zvýšení dávky nepomůže. Vzniká i u nitrátů, proto se ponechává noční interval bez náplasti."),
   ("Bakterie", "Rezistence je vlastnost mikroorganismu, ne pacienta — primární (přirozená) nebo získaná (mutace, přenos plazmidu). Nepleť si ji s tolerancí."),
   ("Křížení", "Zkřížená tolerance existuje mezi látkami se stejným mechanismem — alkohol, benzodiazepiny a barbituráty; morfin a ostatní opioidy.")],
  "Tolerance na různé účinky téže látky se vyvíjí různě rychle: u opioidů rychle na euforii a útlum dechu, ale prakticky vůbec na zácpu a miózu.")

S("O28", "Vliv průvodních onemocnění, polypragmazie",
  "Každý další lék zvyšuje riziko interakce geometricky. A předepsat lék na nežádoucí účinek jiného léku je začátek KASKÁDY.",
  [("🫘", "Ledviny a játra: snížit dávku"),
   ("🫀", "Srdeční selhání: méně průtoku, hůř se eliminuje"),
   ("♾️", "Preskripční KASKÁDA: lék na nežádoucí účinek léku"),
   ("🧹", "DEPRESKRIPCE: pravidelná revize medikace")],
  [("Ledvina", "Renální insuficience — snížit dávku léčiv vylučovaných ledvinami (aminoglykosidy, digoxin, metformin, lithium). Jaterní selhání — nižší metabolismus, nižší albumin, zkratový oběh."),
   ("Srdce", "Srdeční selhání snižuje průtok játry i ledvinami; u léčiv s vysokou jaterní extrakcí hladina stoupá."),
   ("Kaskáda", "Preskripční kaskáda: metoklopramid vyvolá parkinsonské projevy → nasadí se antiparkinsonikum. Blokátor kalciových kanálů vyvolá otoky → nasadí se diuretikum. Vždy se nejdřív ptej, jestli nový příznak není nežádoucí účinek."),
   ("Koště", "Depreskripce — plánované vysazení léků, které už nepřinášejí užitek; u polymorbidních je stejně důležitá jako nasazení."),
   ("Polypragmazie", "Zpravidla 5 a více léčiv současně; roste riziko interakcí, pádů, hospitalizací a klesá adherence.")],
  "Kontraindikace bývají dané právě přidruženou chorobou: β-blokátor u astmatu, NSA u renální insuficience a vředové choroby, metformin při riziku laktátové acidózy.")

S("O29", "Nežádoucí účinky léčiv",
  "Typ A je ZESÍLENÝ ÚČINEK — dá se předvídat, závisí na dávce, je častý. Typ B je BIZARNÍ — nepředvídatelný, na dávce nezávisí, ale zabíjí.",
  [("📈", "TYP A (Augmented): závisí na dávce, předvídatelný"),
   ("🎲", "TYP B (Bizarre): nezávisí na dávce, nepředvídatelný"),
   ("⏱️", "C chronický · D pozdní · E po vysazení"),
   ("📮", "HLÁŠENÍ SÚKL — farmakovigilance")],
  [("Vzestup", "Typ A — vyplývá z farmakologického účinku, závisí na dávce, je častý a málokdy smrtelný; řeší se snížením dávky. Krvácení po warfarinu, hypoglykemie po inzulinu, bradykardie po β-blokátoru."),
   ("Kostka", "Typ B — nesouvisí s dávkou ani s mechanismem, nedá se předvídat; je vzácný, ale často závažný. Alergie, aplastická anemie po chloramfenikolu, maligní hypertermie, Stevensův–Johnsonův syndrom."),
   ("Hodiny", "Typ C — chronický, při dlouhém podávání (osteoporóza po kortikoidech). Typ D — pozdní (teratogenita, kancerogenita). Typ E — po náhlém vysazení (rebound hypertenze, adrenální insuficience)."),
   ("Schránka", "Podezření na nežádoucí účinek se hlásí SÚKL; u nově registrovaných léčiv (černý trojúhelník) se hlásí i podezření běžná. Právě tak se odhalí to, co ve fázi III nevyšlo najevo.")],
  "Typ A se řeší úpravou dávky. Typ B znamená lék vysadit a už nikdy nepodat — a poznamenat do dokumentace.")

S("O30", "Léková alergie, idiosynkrazie",
  "Alergie POTŘEBUJE PŘEDCHOZÍ SETKÁNÍ — první podání senzibilizuje, druhé spustí reakci. Nesnášenlivost není alergie.",
  [("1️⃣", "1. kontakt: senzibilizace, bez příznaků"),
   ("2️⃣", "2. kontakt: reakce — IgE, do minut"),
   ("💉", "ANAFYLAXE → ADRENALIN i.m., ne antihistaminikum"),
   ("🧬", "IDIOSYNKRAZIE: geneticky podmíněná, ne imunitní")],
  [("První setkání", "Senzibilizace probíhá bez příznaků; proto reakce nikdy nepřijde při úplně prvním podání."),
   ("Druhé setkání", "Typ I (IgE, časný) — kopřivka, angioedém, bronchospasmus, anafylaxe během minut. Typ II cytotoxický, typ III imunokomplexový (sérová nemoc), typ IV pozdní buněčný (kontaktní ekzém, makulopapulózní exantém za dny)."),
   ("Adrenalin", "U anafylaxe je lékem první volby adrenalin intramuskulárně do stehna; antihistaminika a kortikosteroidy jsou pouze doplňkové a působí příliš pomalu."),
   ("Idiosynkrazie", "Geneticky podmíněná neobvyklá reakce bez účasti imunity — hemolýza při deficitu G6PD, maligní hypertermie po sukcinylcholinu, prodloužená apnoe při atypické pseudocholinesteráze."),
   ("Zkřížená alergie", "Mezi peniciliny a cefalosporiny existuje, ale je nižší, než se dřív uvádělo; anafylaxe na penicilin v anamnéze je však kontraindikací celé skupiny.")],
  "Nauzea po antibiotiku není alergie, ale nesnášenlivost — přesto se často zapíše jako alergie a pacient pak zbytečně přijde o celou lékovou skupinu.")

S("O31", "Karcinogenní a mutagenní účinky",
  "Mutagen poškodí DNA. Karcinogen z toho udělá nádor. A projeví se to za roky až desetiletí — proto to žádná studie nezachytí včas.",
  [("🧬", "MUTAGEN: poškození DNA (genové, chromozomové)"),
   ("🦀", "KARCINOGEN: iniciace → promoce → progrese"),
   ("⏳", "Latence roky až desetiletí"),
   ("🧪", "Testy: Amesův test, testy in vitro a na zvířeti")],
  [("DNA", "Mutagenita — poškození genetické informace: genové mutace, chromozomové aberace, změny počtu chromozomů. Postihuje-li zárodečné buňky, přenáší se na potomstvo."),
   ("Nádor", "Karcinogeneze má fáze iniciace (nevratné poškození DNA), promoce (podpora množení poškozeného klonu) a progrese. Genotoxické karcinogeny nemají bezpečnou dávku, negenotoxické (hormonální, imunosupresivní) působí nepřímo."),
   ("Přesýpací hodiny", "Dlouhá latence je důvod, proč se karcinogenita odhalí až po letech užívání — a proč se testuje předklinicky."),
   ("Zkumavka", "Amesův test (mutagenita na bakteriích), testy chromozomových aberací, dlouhodobé studie na hlodavcích."),
   ("Příklady", "Cytostatika (alkylační látky — sekundární leukemie), imunosupresiva (lymfomy a kožní nádory), estrogeny bez gestagenu (karcinom endometria), tabákový kouř.")],
  "Cytostatika léčí nádor a zároveň zvyšují riziko nádoru druhého — to není rozpor, ale poměr rizika a prospěchu, který se u každého pacienta váží zvlášť.")

S("O32", "Léčiva v těhotenství, teratogenní účinek, léčiva v době kojení",
  "Nejzranitelnější je ORGANOGENEZE (3.–8. týden) — a to je doba, kdy žena často ještě neví, že je těhotná.",
  [("🥚", "0.–2. týden: „všechno, nebo nic“"),
   ("⚠️", "3.–8. týden: ORGANOGENEZE — malformace"),
   ("📈", "Od 9. týdne: růst a funkce, ne tvar"),
   ("🍼", "Kojení: podat hned PO kojení, ne před")],
  [("Vajíčko", "Do 2. týdne platí pravidlo „všechno, nebo nic“ — buď zárodek zanikne, nebo se poškození plně opraví."),
   ("Varování", "3.–8. týden je organogeneze a období největšího rizika strukturních vad. Klasické teratogeny: isotretinoin a ostatní retinoidy, thalidomid, warfarin, valproát, karbamazepin, fenytoin, metotrexát, mykofenolát, ACE inhibitory a sartany, tetracykliny, živé vakcíny, inhibitory 5-α-reduktázy."),
   ("Růst", "Po organogenezi vznikají funkční poruchy a poruchy růstu — ACE inhibitory poškozují ledviny plodu, NSA předčasně uzavírají ductus arteriosus, tetracykliny barví zuby."),
   ("Kojení", "Do mléka přechází nejspíš látka lipofilní, málo vázaná na bílkoviny a zásaditá. Podává se ihned po kojení, aby do dalšího přiložení hladina klesla. Kontraindikovány jsou cytostatika, radiofarmaka, lithium, amiodaron."),
   ("Rozhodování", "Neléčená nemoc matky (epilepsie, astma, těžká deprese, infekce) ohrožuje plod často víc než lék — proto se neléčí „nulovým rizikem“, ale poměrem rizika a prospěchu.")],
  "Kyselina listová se podává preventivně už před početím jako prevence rozštěpů neurální trubice — u žen na antiepilepticích ve vyšší dávce.")

S("O33", "Farmakoterapie v dětství",
  "Dítě není zmenšený dospělý. Dávkuje se na KILOGRAM nebo na povrch těla — a některé léky nesmí dostat vůbec.",
  [("⚖️", "Dávka na kg hmotnosti nebo na m² povrchu"),
   ("🍼", "Novorozenec: nezralá glukuronidace, více vody"),
   ("🚫", "Zakázáno: tetracykliny, chinolony, kodein, ASA"),
   ("🧃", "Formy: sirupy, kapky, čípky — ne velké tablety")],
  [("Váhy", "Dávkuje se na kilogram tělesné hmotnosti, u cytostatik na plochu povrchu těla; nikdy se nepřepočítává „zlomkem dávky dospělého“ od oka."),
   ("Kojenec", "Novorozenec má nezralé jaterní enzymy (glukuronidaci — odtud gray baby syndrom po chloramfenikolu), vyšší podíl tělesné vody (vyšší Vd pro hydrofilní léčiva), nižší vazbu na bílkoviny a nezralou glomerulární filtraci."),
   ("Zákaz", "Tetracykliny do 8 let (zbarvení zubů a hypoplazie skloviny) · chinolony (poškození chrupavky) · kodein a tramadol (útlum dechu u ultrarychlých metabolizátorů) · kyselina acetylsalicylová u virózy (Reyeův syndrom) · metoklopramid (dystonie)."),
   ("Sirup", "Perorální roztoky, sirupy, kapky, čípky; při dlouhodobé léčbě pozor na obsah cukru a etanolu v přípravku."),
   ("Off-label", "Řada léčiv nemá u dětí registraci — podávají se off-label na základě odborných doporučení, protože klinické studie na dětech jsou vzácné.")],
  "Paracetamol a ibuprofen jsou základní antipyretika dětského věku; kyselina acetylsalicylová se u dětí s horečnatým virovým onemocněním nepodává pro riziko Reyeova syndromu.")

S("O34", "Farmakoterapie ve stáří, polypragmazie",
  "Ve stáří: „START LOW, GO SLOW“. Klesá filtrace, klesá albumin, přibývá tuku — a citlivost mozku na tlumivé léky roste.",
  [("🐢", "Začni nízkou dávkou, zvyšuj pomalu"),
   ("🫘", "Klesá glomerulární filtrace — i při normálním kreatininu"),
   ("🧠", "Vyšší citlivost na benzodiazepiny a opioidy"),
   ("📋", "Beersova kritéria, STOPP/START — nevhodná léčiva")],
  [("Želva", "Start low, go slow — nižší úvodní dávka a pomalá titrace; kontrola účinku i nežádoucích účinků."),
   ("Ledvina", "Glomerulární filtrace klesá s věkem i při normálním sérovém kreatininu, protože ubývá svalové hmoty — proto se počítá clearance, ne jen kreatinin."),
   ("Mozek", "Roste citlivost na benzodiazepiny, opioidy, anticholinergika a antipsychotika — riziko pádů, zmatenosti a deliria. Ubývá svalu a přibývá tuku, takže lipofilní léčiva se hromadí a mají delší poločas."),
   ("Seznam", "Beersova kritéria a STOPP/START vyjmenovávají léčiva u seniorů nevhodná (dlouhodobě působící benzodiazepiny, anticholinergika, NSA) a naopak ta, která chybějí."),
   ("Anticholinergní zátěž", "Sčítá se z mnoha léků najednou (antihistaminika I. generace, tricyklika, spasmolytika, některá antipsychotika) — výsledkem je zmatenost, retence moči, zácpa a pády.")],
  "Nový příznak u seniora je nežádoucí účinek léku, dokud se neprokáže opak — teprve pak se hledá nová diagnóza. Jinak vzniká preskripční kaskáda.")

S("O35", "Biologická léčba: rozdělení, názvosloví, biosimilars",
  "Konec názvu prozradí, co to je: -MAB je protilátka, -CEPT je vazebný receptor, -NIB je malá molekula inhibující kinázu.",
  [("🔤", "-mab = monoklonální protilátka"),
   ("🪝", "-cept = solubilní receptor (etanercept)"),
   ("🧩", "-nib = inhibitor kinázy (malá molekula)"),
   ("♻️", "BIOSIMILAR: podobný, nikdy ne identický")],
  [("Přípona -mab", "Monoklonální protilátka. Předposlední slabika říká původ: -xi- chimérická (infliximab), -zu- humanizovaná (trastuzumab), -u- plně lidská (adalimumab). Podávají se parenterálně — bílkovina by se v trávicím traktu strávila."),
   ("Přípona -cept", "Fúzní bílkovina, solubilní receptor, který na sebe naváže cytokin (etanercept váže TNF-α, abatacept, aflibercept)."),
   ("Přípona -nib", "Malá molekula, inhibitor kinázy — na rozdíl od protilátek se podává perorálně (imatinib, tofacitinib, ibrutinib)."),
   ("Biosimilar", "Biologicky podobný přípravek — u bílkoviny nelze vyrobit přesnou kopii jako u generika, proto se dokládá srovnatelná kvalita, účinnost a bezpečnost, ne pouhá bioekvivalence."),
   ("Rizika", "Infuzní a hypersenzitivní reakce, imunogenicita (tvorba protilátek proti léku), zvýšené riziko infekcí. ⚠️ Před anti-TNF-α je nutné vyloučit latentní tuberkulózu a hepatitidu B — hrozí reaktivace.")],
  "Biologika jsou bílkoviny — proto se nepodávají ústy, jsou drahá, vyžadují chladový řetězec a mohou vyvolat tvorbu neutralizujících protilátek, které je časem přestanou nechávat účinkovat.")
