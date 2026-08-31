#!/usr/bin/env python3
"""Text kapesních kartiček — ODPOVĚĎ na každou ze 136 zkouškových otázek.

Každý záznam je `K(číslo, název, text)`. Text je **souvislá odpověď**, ne výčet
útržků: co to je → jak to funguje → dělení a zástupci → k čemu → nežádoucí účinky
a kontraindikace. Cíl: kartu si přečteš a otázku umíš.

Rozsah: zhruba **1150–1350 znaků** na kartu — tolik se na 66 × 71 mm vejde
a zároveň to kartu zaplní.
**Tučně** se zvýrazňují názvy skupin, zástupci a to, na čem odpověď stojí.
"""

KARTY = []


def K(cislo, nadpis, text):
    KARTY.append((cislo, nadpis, " ".join(text.split())))


# ═══════════════════════════════ OBECNÁ FARMAKOLOGIE

K("O1", "Farmakologie, původ a zdroje léčiv, názvy, lékopis", """
**Farmakologie** je věda o léčivech a jejich působení na organismus. Dělí se na
**farmakokinetiku** (co dělá tělo s lékem — absorpce, distribuce, metabolismus,
exkrece) a **farmakodynamiku** (co dělá lék s tělem — mechanismus a účinek).
Navazuje farmakoterapie, toxikologie a farmakovigilance.
**Léčivá látka** je nositel účinku; s pomocnými látkami tvoří **lékovou formu**
a výsledkem je **léčivý přípravek**.
**Zdroje:** rostliny (alkaloidy — morfin, atropin; glykosidy — digoxin),
živočichové (heparin, inzulin), mikroorganismy (peniciliny), minerály, dnes
především **chemická syntéza** a **biotechnologie** (rekombinantní bílkoviny,
monoklonální protilátky).
**Názvy** jsou tři: chemický (vzorec), **generický** (nechráněný — ibuprofen;
tímhle se mluví odborně) a firemní (chráněný — Brufen).
**Lékopis** je závazný soubor požadavků na jakost léčiv a jejich zkoušení; český
vychází z evropského. Látka v něm uvedená je **oficinální**, přípravek
připravený v lékárně je **magistraliter**, hromadně vyráběný je **HVLP**.
""")

K("O2", "Legislativa, doplňky stravy, zdravotnické prostředky, regulační orgány", """
Základním předpisem je **zákon o léčivech 378/2007 Sb.** [ověřit dle skript].
Kategorii určuje **mechanismus účinku, ne složení**.
**Léčivý přípravek** působí farmakologicky, imunologicky nebo metabolicky. Musí
před registrací **prokázat účinnost, bezpečnost a jakost**; registruje **SÚKL**
národně nebo **EMA** centralizovaně. Smí deklarovat léčbu nemoci a podléhá
povinnému hlášení nežádoucích účinků (farmakovigilance).
**Doplněk stravy** je právně **potravina**: účinnost dokládat nemusí, stačí
ohlášení, dozor má SZPI a **nesmí tvrdit, že léčí**. Pacient ten rozdíl nevidí,
proto se na doplňky ptáme cíleně — mají reálné interakce.
**Zdravotnický prostředek** působí **fyzikálně** (výplň, implantát, obvaz),
posuzuje se shoda a riziková třída.
**Výdej:** vázaný na předpis, s omezením (odbornost), volně prodejný (OTC);
omamné a psychotropní látky na **recept s modrým pruhem**.
""")

K("O3", "Předepisování léčivých přípravků", """
**Recept je právní dokument** s odpovědností dvou lidí: lékaře za to, co
předepsal, a lékárníka za to, co vydal. Standardem je **eRecept** — lékař ho
vystaví do centrálního úložiště a pacient dostane identifikátor; listinný recept
zůstává pro výpadky systému.
**Náležitosti:** identifikace pacienta (jméno, číslo pojištěnce) · léčivo —
název, síla, léková forma a množství · **dávkování a způsob podání** (signatura,
D.S.) · identifikace lékaře a pracoviště s podpisem a razítkem · datum
vystavení.
**Platnost** běžného receptu je zpravidla 14 dní, u antibiotik kratší
[ověřit dle skript]. **Opakovací recept** uvádí počet opakování.
**Modrý pruh** je vyhrazen omamným a psychotropním látkám a má přísnější
evidenci.
**Magistraliter** předpis má stavbu Rp. — složení — M.f. (misce fiat) — D.S.
Před předepsáním patří anamnéza: alergie, gravidita, funkce jater a ledvin,
ostatní léky.
""")

K("O4", "Preklinické a klinické hodnocení léčiv", """
Vývoj léčiva jde po stupních a každý odpovídá na jinou otázku.
**Preklinika** probíhá in vitro a na zvířatech: farmakodynamika, kinetika,
**toxicita (ED50, TD50, LD50)**, mutagenita, teratogenita, karcinogenita.
**Klinické hodnocení** má čtyři fáze. **I.** desítky **zdravých** dobrovolníků —
bezpečnost, snášenlivost a chování látky v těle. **II.** stovky **nemocných** —
zabírá to a v jaké dávce. **III.** tisíce nemocných — **srovnání s dosavadní
léčbou nebo placebem**; na jejím základě se registruje. **IV.** po uvedení na
trh — sledování v běžné populaci.
**Zásady studie:** randomizace, zaslepení (jednoduché, dvojité, trojité),
kontrolní skupina, předem daný cíl, informovaný souhlas a souhlas etické komise.
**Proč se vzácné nežádoucí účinky objeví až ve fázi IV:** účinek, který postihne
jednoho z deseti tisíc, nemá ve studii o tisících pacientů šanci vyjít najevo.
Generikum účinnost neprokazuje znovu — dokládá **bioekvivalenci**.
""")

K("O5", "Způsoby aplikace léčiv, výhody a nevýhody", """
Cesta podání se volí podle toho, kde má lék působit, jak rychle a co pacient
zvládne. Hlavní rozdíl není v rychlosti, ale v tom, **zda lék projde játry**.
**Enterální:** **perorálně** — pohodlné, levné, bezpečné, ale pomalejší,
kolísavé a zatížené **first-pass efektem**; **sublingválně** — vstřebání rovnou
do systémového oběhu, **obchází játra**, proto nitroglycerin; **rektálně** —
funguje při zvracení a u dětí, játra obchází jen částečně.
**Parenterální:** **i.v.** — okamžitý účinek a **100% biologická dostupnost**,
ale podané se nedá vzít zpět; **i.m.** rychlé; **s.c.** pomalejší (inzulin,
hepariny); dále intratekálně, intraartikulárně, intraoseálně. Vyžadují
sterilitu a personál.
**Ostatní:** inhalačně, na kůži a sliznice, transdermální náplast (nejpomalejší,
účinek dny).
**Pozor:** „místní" podání neznamená „bez celkového účinku" — oční, nosní i
inhalační formy se vstřebávají.
""")

K("O6", "Lékové formy — perorální a orální", """
**Perorální** forma se polyká a působí až po vstřebání ze střeva;
**orální** zůstává v ústech (*per os* = skrz ústa, *oralis* = ústní).
**Perorální formy:** tablety, potahované tablety, tobolky, granuláty, sirupy,
suspenze, kapky. **Enterosolventní obal** projde žaludkem a rozpadne se až ve
střevě (chrání látku před kyselinou nebo žaludek před látkou).
**Retardované formy** (SR, ZOK) uvolňují látku postupně a umožní dávkování 1×
denně. **Ani jednu z nich nelze drtit** — drcením se uvolní celá dávka najednou
nebo se látka zničí.
**Orální formy:** pastilky, žvýkací tablety, ústní vody, gely. **Sublingválně a
bukálně** se látka vstřebá rovnou do krve a **obejde first-pass efekt** —
nitroglycerin, buprenorfin.
**Pomocné látky** (plniva, pojiva, kluzné látky, rozvolňovadla, barviva,
sladidla) nejsou neutrální: laktóza vadí při intoleranci, **cukr v sirupech** je
při dlouhodobé léčbě rizikem pro chrup.
""")

K("O7", "Lékové formy — parenterální a dermatologika", """
**Parenterální** znamená mimo trávicí trakt. Přípravek obchází přirozené
bariéry, proto musí být **sterilní, apyrogenní, izotonický, izohydrický a bez
mechanických nečistot**.
**Formy:** injekce (roztok, suspenze, emulze), infuze, implantáty a depotní
přípravky. **Suspenze se nikdy nepodává i.v.** — hrozí embolizace.
**Rychlost účinku sleduje prokrvení:** i.v. okamžitě a se 100% dostupností,
i.m. rychle, s.c. pomaleji, depotní formy a náplasti nejpomaleji, ale působí
dny až měsíce.
**Výhody:** jistá dostupnost, přesné dávkování, použitelné u zvracení a
bezvědomí. **Nevýhody:** bolestivost, riziko infekce a embolie, nutný personál
a **nevratnost podání**.
**Dermatologika:** mast (tučný základ, největší průnik, na suchou kůži), krém
(voda i tuk), gel (vodný, chladí), pasta, zásyp, roztok, náplast. Průnik zvyšuje
okluze. **Lokální kortikoidy** dlouhodobě způsobí atrofii kůže a strie, na
obličej patří jen slabé a krátce.
""")

K("O8", "Lékové formy — oční, ušní, nosní, rektalia, vaginalia, inhalanda", """
Společné pravidlo: **místní podání neznamená jen místní účinek** — všechny tyto
formy se vstřebávají a mohou působit celkově.
**Oční** (kapky, masti, gely) musí být sterilní a izotonické, po otevření mají
omezenou dobu použitelnosti. **Timolol z kapek** vyvolá bradykardii a
bronchospazmus; vstřebání sníží stisknutí vnitřního koutku po nakapání.
**Nosní:** dekongescencia (xylometazolin) jen **5–7 dní**, jinak vzniká
*rhinitis medicamentosa*; nosní cestou se podává i desmopresin či sumatriptan
k celkovému účinku.
**Ušní** kapky se nesmí podat při perforaci bubínku.
**Inhalanda:** aerosolový dávkovač, práškový inhalátor, nebulizace. Rozhoduje
**technika inhalace**; nástavec zlepší depozici a sníží nežádoucí účinky
(inhalační kortikoid jinak vyvolá orální kandidózu a chrapot).
**Rektalia** obcházejí játra jen z dolní části konečníku; hodí se u zvracení a
u dětí. **Vaginalia** slouží hlavně k místní léčbě.
""")

K("O9", "Komunikace, adherence, compliance, placebo a nocebo", """
**Compliance** je míra, do jaké pacient dodržuje pokyny (pasivní pojetí);
**adherence** je dodržování dohodnutého plánu, na kterém se pacient podílel;
**perzistence** je, jak dlouho u léčby vydrží; **konkordance** je společné
rozhodnutí lékaře a pacienta. Dnes se preferuje adherence, protože zdůrazňuje
spoluodpovědnost.
**Nejčastější příčina selhání léčby není špatný lék, ale nebraný lék.**
Adherenci snižuje: nemoc, která nebolí (hypertenze, osteoporóza), složitý režim
a mnoho tablet, nežádoucí účinky a obavy z nich, cena, nepochopení a nedůvěra.
Zlepší ji fixní kombinace, dávkování 1× denně, srozumitelné vysvětlení a
kontrola.
**Placebo:** očekávání zlepšení vede k **měřitelnému** zlepšení; má
neurobiologický podklad (endogenní opioidy, dopamin), není to „vymyšlený" efekt
a zesiluje účinek každého skutečného léku.
**Nocebo:** očekávání škody vyvolá potíže — vzniká z příbalového letáku i z
neopatrné věty a stojí za častým vysazením statinů a antidepresiv. Formulace
lékaře je proto účinná látka s vlastní dávkou.
""")

K("O10", "Přechod látek biologickými membránami", """
Membrána je **tuková stěna**, proto přes ni prostou difuzí projde jen látka
**lipofilní a nenabitá**; nabitá (ionizovaná) forma neprojde.
**Mechanismy přestupu:** **prostá difuze** — po koncentračním spádu, bez energie
a bez přenašeče; **facilitovaná difuze** — přenašečem, po spádu, saturovatelná;
**aktivní transport** — proti spádu, spotřebuje ATP (např. **P-glykoprotein**,
který léky aktivně vypuzuje z buňky); dále filtrace póry a pinocytóza.
**Co rozhoduje:** rozpustnost v tucích, velikost molekuly, koncentrační spád a
**ionizace**, tedy poměr pKa látky k pH prostředí.
**Iontová past:** látka projde membránou v nenabité formě, na druhé straně se
při jiném pH ionizuje a **zpět už neprojde — hromadí se**. Vysvětluje, proč
lokální anestetikum nezabírá v kyselém zánětlivém prostředí, proč alkalizace
moči urychlí vyloučení salicylátů a proč laktulóza uvězní amoniak ve střevě.
**Bariéry:** hematoencefalická (těsné spoje + P-glykoprotein), placentární
(propustnější, než se čeká), krev–varle, krev–sítnice. Zánět bariéru zpropustní.
""")

K("O11", "Základní farmakokinetické parametry a procesy", """
Farmakokinetika popisuje osud léčiva v těle zkratkou **ADME**: **absorpce**
(vstup do krve), **distribuce** (rozvod do tkání), **metabolismus** (přeměna,
hlavně v játrech) a **exkrece** (vyloučení, hlavně ledvinami). Metabolismus a
exkrece se dohromady označují jako **eliminace**. Děje probíhají současně, ne po
sobě.
**Parametry:** **F — biologická dostupnost** (podíl dávky, který se dostal
nezměněný do systémového oběhu; i.v. = 100 %); **Vd — distribuční objem**
(zdánlivý, poměr dávky a plazmatické koncentrace); **CL — clearance** (objem
krve očištěný za čas); **t½ — biologický poločas**; **AUC** (plocha pod křivkou
= celková expozice); **Cmax a tmax**.
**Vztahy:** poločas závisí na clearance **i** na distribučním objemu — velký Vd
poločas prodlouží, i když clearance je dobrá. **Ustálený stav (steady state)
nastane za 4–5 poločasů** a stejně dlouho trvá, než je lék po vysazení prakticky
pryč; zrychlit ho lze jen nasycovací dávkou.
Farmakokinetika = co tělo dělá s lékem; farmakodynamika = co lék dělá s tělem.
""")

K("O12", "Procesy nultého a prvního řádu, saturační kinetika", """
Rozdíl je v tom, co se za jednotku času eliminuje.
**Kinetika prvního řádu** platí pro naprostou většinu léčiv: odbourává se
konstantní **podíl** (například polovina za hodinu), protože enzymy mají
kapacitní rezervu. Pokles je exponenciální, má smysl mluvit o **poločasu** a
dávkování je předvídatelné.
**Kinetika nultého řádu** nastává, když je enzym **nasycený**: odbourává se
konstantní **množství** za čas bez ohledu na koncentraci. Pokles je lineární a
**poločas ztrácí smysl**. Chová se tak **ethanol** (řádově 0,1–0,15 ‰ za
hodinu), **fenytoin**, salicyláty ve vysoké dávce a částečně theofylin.
**Saturační (Michaelisova–Mentenové) kinetika** je přechod mezi oběma: dokud je
enzym volný, jde o první řád; po jeho zahlcení o nultý.
**Klinický důsledek:** u fenytoinu stačí malé zvýšení dávky a hladina vyskočí do
toxického pásma (nystagmus, ataxie, zmatenost), proto se u něj **měří hladiny**.
Stejně tak nelze u ethanolu počítat „za dva poločasy bude polovina".
""")

K("O13", "Absorpce, Batemanova funkce, biologická dostupnost, AUC", """
**Absorpce** je přestup léčiva z místa podání do systémového oběhu. Ovlivňuje ji
léková forma (roztok se vstřebá rychleji než tableta), jídlo, pH a motilita
žaludku, prokrvení a **chelatace** (mléko, antacida a železo znemožní vstřebání
tetracyklinů a chinolonů).
**Batemanova funkce** popisuje průběh plazmatické koncentrace po jednorázovém
perorálním podání jako výsledek dvou současných dějů — vstřebávání a eliminace.
**Vrchol křivky (Cmax) není konec vstřebávání**, ale okamžik, kdy se rychlost
vstřebávání a eliminace vyrovnají; **tmax** je čas do vrcholu a závisí hlavně na
rychlosti vstřebávání.
**Biologická dostupnost F** je podíl dávky, který se dostal do oběhu nezměněný.
Z definice je **i.v. = 100 %**; perorálně ji snižuje rozklad v žaludku, špatné
vstřebání a hlavně **first-pass efekt**. Počítá se z poměru AUC po perorálním a
nitrožilním podání.
**AUC** vyjadřuje celkovou expozici organismu. Na AUC a Cmax stojí posuzování
**bioekvivalence generik** — nemusí jít o identickou tabletu, ale o srovnatelnou
expozici.
""")

K("O14", "Distribuce, distribuční objem, redistribuce, vazba na bílkoviny, bariéry", """
**Distribuce** je rozvod léčiva z krve do tkání. Závisí na prokrvení orgánu,
lipofilitě látky, bariérách a **vazbě na plazmatické bílkoviny**.
**Vazba na bílkoviny:** kyselá léčiva se vážou na **albumin** (warfarin, NSA,
fenytoin), zásaditá na **orosomukoid**. **Vázaná frakce je neúčinná** — je to
sklad; **působí, metabolizuje se a vylučuje jen frakce volná**. Při nízkém
albuminu (senior, cirhóza, nefrotický syndrom, popáleniny) volné frakce přibude
a při „normální" dávce hrozí předávkování. Vytěsněním z vazby se vysvětlují
interakce (NSA × warfarin).
**Distribuční objem Vd** je zdánlivá veličina — poměr dávky k plazmatické
koncentraci, ne skutečný objem. Malý Vd znamená, že lék zůstává v krvi (heparin);
**velký Vd** znamená uložení ve tkáních (digoxin) a dialýzou se takový lék
nedostane ven.
**Redistribuce:** léčivo nejdřív zasytí dobře prokrvený mozek a pak se přelije do
svalů a tuku. Tím končí účinek **thiopentalu** — ne odbouráním. Po opakovaných
dávkách se tkáně nasytí a probouzení trvá hodiny.
""")

K("O15", "Eliminace, poločas, fáze α a β, eliminační konstanta, clearance", """
**Eliminace** = metabolismus + exkrece. Po nitrožilním podání má křivka poklesu
dvě fáze. **Fáze α (distribuční)** je rychlý pokles daný tím, že se léčivo
**přestěhovalo do tkání**, nikoli odbouralo — právě jí končí účinek thiopentalu.
**Fáze β (eliminační)** je pomalejší pokles, při kterém se léčivo skutečně
metabolizuje a vylučuje; z ní se počítá poločas.
**Biologický poločas t½** je doba, za kterou klesne koncentrace na polovinu. Za
**4–5 poločasů** je léčivo prakticky vyloučeno a stejně dlouho trvá dosažení
ustáleného stavu. Poločas závisí na clearance i na distribučním objemu:
**t½ = 0,693 × Vd / CL**.
**Clearance** je objem krve zcela očištěný od látky za jednotku času; celková se
skládá z jaterní, renální a ostatní. **Eliminační konstanta ke = CL / Vd.**
**Poločas prodlužuje** selhání jater a ledvin, vysoký věk, nízký srdeční výdej,
inhibice enzymů a velký distribuční objem. U léčiv s úzkým terapeutickým oknem
se proto sledují plazmatické hladiny.
""")

K("O16", "Dávkovací režim, kumulace, kumulační index", """
Cílem dávkovacího režimu je udržet koncentraci v terapeutickém rozmezí.
**Nasycovací dávka** naplní distribuční prostor naráz a řídí se **distribučním
objemem**; používá se tam, kde nelze čekat 4–5 poločasů (digoxin, amiodaron,
některá antibiotika). **Udržovací dávka** nahrazuje jen to, co se eliminovalo, a
řídí se **clearance**.
**Ustálený stav** nastane vždy za 4–5 poločasů bez ohledu na velikost udržovací
dávky — ta určuje jen výši hladiny.
**Kumulace** nastane, když se léčivo podává rychleji, než stačí eliminace;
**kumulační index** udává, kolikanásobně hladina vzroste proti jedné dávce.
Riziko roste při selhání ledvin a jater a je nebezpečné u léčiv s úzkým oknem
(digoxin, lithium, aminoglykosidy).
**Dávkovací interval** se odvozuje od poločasu; kratší interval znamená menší
kolísání, ale horší spolupráci pacienta — řeší to retardované formy.
**Terapeutické monitorování (TDM)** se dělá u léčiv s úzkým oknem a nejasným
vztahem dávky a účinku: digoxin, lithium, theofylin, fenytoin, vankomycin,
aminoglykosidy. Odebírá se v přesně daném čase, obvykle údolní hladina.
""")

K("O17", "Biotransformace léčiv, fáze, příklady", """
**Biotransformace** mění lipofilní látku na hydrofilní, aby ji bylo možné
vyloučit. Probíhá hlavně v **játrech** (hladké endoplazmatické retikulum), dále
ve střevní stěně, plicích, ledvinách a plazmě (esterázy).
**Fáze I — funkcionalizace:** oxidace, redukce, hydrolýza, převážně systémem
**cytochromu P450** (nejvýznamnější **CYP3A4**, dále 2D6, 2C9, 2C19, 1A2).
Zavede nebo odhalí reaktivní skupinu. Produkt může být **účinnější nebo
toxičtější** než výchozí látka.
**Fáze II — konjugace:** glukuronidace, sulfatace, acetylace, methylace,
konjugace s glutathionem. Připojí velkou polární skupinu, produkt je zpravidla
neúčinný a snadno vyloučitelný.
**Proléčiva** se podávají neúčinná a aktivuje je až metabolismus: kodein na
morfin (CYP2D6), klopidogrel (CYP2C19), enalapril, cyklofosfamid, levodopa,
aciklovir. U pomalého metabolizátora proléčivo nezabere.
**Příklad obojího:** paracetamol se z 90 % konjuguje, ale asi 10 % jde přes
CYP2E1 na toxický **NAPQI**, který zneškodní glutathion. Při předávkování se
konjugace nasytí, glutathion se vyčerpá a vzniká jaterní nekróza; antidotem je
**N-acetylcystein**.
""")

K("O18", "Úloha jater v eliminaci léčiv, first-pass efekt", """
Játra jsou hlavním orgánem biotransformace a zároveň branou, kterou musí projít
všechno, co se vstřebá ze střeva.
**First-pass efekt** je ztráta léčiva při prvním průchodu střevní stěnou a játry
ještě před vstupem do systémového oběhu. Výrazně snižuje biologickou dostupnost —
u nitroglycerinu, morfinu, propranololu, lidokainu, verapamilu nebo testosteronu
až na jednotky procent. **Obcházejí ho** cesty sublingvální, i.v., i.m., s.c. a
transdermální; rektální jen částečně (dolní část konečníku ano, horní ne).
**Jaterní clearance:** u léčiv s vysokou extrakcí ji určuje **průtok játry** —
proto při srdečním selhání nebo šoku jejich hladina stoupá. U léčiv s nízkou
extrakcí rozhoduje **enzymová kapacita a volná frakce** — proto je mění indukce,
inhibice a nízký albumin.
**Pacient s jaterním postižením:** klesá metabolická kapacita (kumulace), klesá
albumin (vyšší volná frakce), portosystémové zkraty obcházejí first-pass a
prudce zvyšují hladinu, klesá tvorba koagulačních faktorů (krvácivost).
Paracetamol se podává v redukované dávce, nesteroidním antirevmatikům se
vyhýbáme.
""")

K("O19", "Inhibice a indukce enzymů léčivy, klinický význam", """
Nejvýznamnější lékové interakce probíhají na **cytochromu P450**.
**Inhibice** je brzda a nastupuje prakticky **ihned**: enzym přestane pracovat,
hladina druhého léčiva **stoupne** a hrozí **předávkování**. Silné inhibitory:
**makrolidy** (erythromycin, klarithromycin — ne azithromycin), **azolová
antimykotika**, **ritonavir**, amiodaron, verapamil a **grapefruit**.
**Indukce** je plyn s pomalým rozjezdem: enzymu se musí vytvořit více, takže
efekt naskakuje **dny až týdny**. Hladina druhého léčiva **klesne** a hrozí
**selhání léčby**. Silné induktory: **rifampicin**, karbamazepin, fenytoin,
fenobarbital, **třezalka tečkovaná**, chronicky alkohol (CYP2E1) a **kouření**
(CYP1A2).
**Nebezpečný je i konec indukce** — enzymy se odbourávají týdny, takže po
vysazení induktoru hladina druhého léku vyskočí. Když kuřák přestane kouřit,
stoupne mu theofylin, olanzapin i klozapin.
**Typické dvojice:** rifampicin či třezalka × hormonální antikoncepce (selhání),
klarithromycin × statin (rabdomyolýza), azol × warfarin (krvácení).
**U proléčiva působí inhibitor obráceně** — zabrání vzniku účinné látky
(omeprazol × klopidogrel).
""")

K("O20", "Vylučování léčiv renální a extrarenální", """
Hlavní cestou je **ledvina** a uplatňují se v ní tři děje.
**Glomerulární filtrace** propustí jen **volnou frakci** a řídí se glomerulární
filtrací. **Tubulární sekrece** je aktivní děj s přenašeči pro kyseliny a
zásady; přenašeče se dají obsadit (probenecid zpomalí vylučování penicilinu).
**Tubulární resorpce** vrací látku zpět, ale jen v **nenabité** formě.
Toho se využívá: **alkalizace moči** udrží kyselé léčivo v ionizované podobě,
takže se nevstřebá zpět a rychleji odejde — u otravy salicyláty a barbituráty
(iontová past).
**Extrarenální cesty:** **žlučí a stolicí** — část léčiva se ve střevě
dekonjuguje a vstřebá zpět (**enterohepatální oběh**), což prodlužuje účinek;
**plícemi** (inhalační anestetika, ethanol); **mlékem** — mírně kyselé mléko
zachytí zásaditá léčiva; dále slinami, potem a vlasy (toxikologický průkaz).
**Při renální insuficienci** se léčiva vylučovaná ledvinami kumulují — dávka se
redukuje nebo prodlouží interval podle odhadu glomerulární filtrace. Týká se
digoxinu, aminoglykosidů, lithia, metforminu a přímých antikoagulancií.
""")

K("O21", "Účinek léčiv obecně, způsob účinku na molekulární úrovni", """
Léčivo může působit **specificky** nebo **nespecificky**.
**Specifický účinek** je vázán na konkrétní cílovou strukturu a stačí k němu
malé dávky. Cíle jsou čtyři: **receptor** (agonista, antagonista, parciální
agonista), **enzym** (statiny na HMG-CoA reduktázu, ACE inhibitory, NSA na
cyklooxygenázu), **iontový kanál** (lokální anestetika na sodíkový kanál,
blokátory kalciových kanálů) a **přenašeč či pumpa** (SSRI, glifloziny,
omeprazol na H+/K+-ATPázu).
**Nespecifický účinek** je fyzikálně-chemický, bez cílové struktury, a potřebuje
velké dávky: antacida (neutralizace), osmotická laxativa a diuretika, aktivní
uhlí (adsorpce), dezinficiencia, chelátory.
**Podle výsledku léčby** se rozlišuje léčba **kauzální** (odstraní příčinu —
antibiotikum, antidotum), **symptomatická** (uleví od projevu — analgetikum),
**substituční** (nahradí chybějící — inzulin, levothyroxin) a **profylaktická**.
**Afinita** je pevnost vazby, **vnitřní aktivita** schopnost vyvolat odpověď,
**selektivita** přesnost zásahu. Selektivita není absolutní a s rostoucí dávkou
mizí.
""")

K("O22", "Specifický účinek, cílové struktury, receptorová teorie, typy receptorů", """
**Receptor** je makromolekula, která rozpozná ligand a převede vazbu na buněčnou
odpověď. Rychlost odpovědi určuje typ receptoru.
**Ionotropní** receptor je sám iontovým kanálem a reaguje v **milisekundách** —
nikotinový, GABA-A, NMDA. **Metabotropní** receptor spřažený s **G-proteinem**
reaguje v sekundách — muskarinový, adrenergní, opioidní, histaminový.
**Receptor s enzymovou aktivitou** (inzulinový, receptory růstových faktorů)
reaguje v minutách. **Nitrobuněčný** receptor mění **přepis genů**, a proto
působí až za **hodiny** — kortikoidy, hormony štítné žlázy, pohlavní hormony.
Z toho plyne, proč adrenalin anafylaxi zvrátí během minuty, zatímco kortikoid ne.
**Typy ligandů:** agonista (plná odpověď), **parciální agonista** (má strop —
buprenorfin, aripiprazol), antagonista (blokuje bez vlastní odpovědi), inverzní
agonista.
**Kompetitivní** antagonista soutěží o stejné místo a **lze ho překonat vyšší
dávkou agonisty** (naloxon × morfin); **nekompetitivní** nebo ireverzibilní
překonat nelze (aspirin na cyklooxygenázu).
**Regulace:** nadbytek podnětu vede k **down-regulaci** (tolerance), blokáda k
**up-regulaci** — proto se betablokátory nevysazují náhle.
""")

K("O23", "Dávka a účinek, terapeutický index, terapeutické okno, riziko, NNT", """
Vztah dávky a účinku popisuje sigmoidní křivka. **ED50** je dávka účinná u
poloviny jedinců, **TD50** toxická a **LD50** letální.
**Terapeutický index = TD50 / ED50** — čím vyšší, tím bezpečnější léčivo.
**Terapeutické okno** je rozmezí mezi minimální účinnou a toxickou koncentrací.
**Účinnost** (efficacy) je maximální dosažitelný účinek, **potence** velikost
dávky, která je k němu potřeba — vysoká potence neznamená vysokou účinnost.
**Léčiva s úzkým oknem**, u nichž se **měří plazmatické hladiny**: digoxin,
lithium, warfarin, theofylin, fenytoin, aminoglykosidy, vankomycin, cytostatika,
imunosupresiva.
**Hodnocení přínosu:** **NNT** je počet pacientů, které je třeba léčit, aby měl
jeden prospěch (čím nižší, tím lépe), **NNH** počet, než jeden utrpí škodu (čím
vyšší, tím lépe). Absolutní snížení rizika je informativnější než relativní,
které vždy zní působivěji.
Poměr přínosu a rizika se posuzuje vždy podle závažnosti nemoci — u banální
choroby se toleruje minimální riziko, v onkologii velké.
""")

K("O24", "Vlivy působící na kinetiku a dynamiku léčiv", """
Stejná dávka nevyvolá u dvou lidí stejný účinek, a je to předvídatelné.
**Věk:** novorozenec má vyšší pH žaludku, 75 % vody, málo albuminu, **nezralou
glukuronidaci** a nezralou hematoencefalickou bariéru; dávkuje se podle povrchu
těla. Senior má méně vody a více tuku, horší funkci ledvin a vyšší citlivost
CNS.
**Orgánové funkce a nemoci:** jaterní postižení snižuje metabolismus a albumin,
renální insuficience vede ke kumulaci, srdeční selhání zhoršuje prokrvení střeva
i jater; roli hraje i štítná žláza, horečka, dehydratace a obezita.
**Genetika:** polymorfismy **CYP2D6 a CYP2C19** dělí populaci na pomalé,
normální a ultrarychlé metabolizátory; dále acetylátorský status, deficit
**TPMT**, **G6PD** a atypická pseudocholinesteráza.
**Vnější vlivy:** ostatní léčiva (indukce, inhibice, kompetice), strava
(**grapefruit**, mléko, vitamin K, tyramin), **kouření** a alkohol, denní doba.
**Pohlaví a gravidita** mění složení těla i metabolismus.
Standardní dávka je proto jen výchozí bod, který se u seniora, dítěte a při
orgánovém postižení upravuje.
""")

K("O25", "Lékové interakce", """
Interakce je změna účinku jednoho léčiva přítomností druhého. Dělí se na dva
zcela odlišné typy.
**Farmakokinetické** mění **hladinu** druhého léčiva. Ve vstřebávání: antacida,
mléko a železo chelatují tetracykliny a chinolony; prokinetika a laxativa mění
rychlost pasáže. V distribuci: vytěsnění z vazby na albumin (NSA × warfarin). V
metabolismu: **indukce a inhibice CYP** — klinicky nejvýznamnější skupina. Ve
vylučování: soutěž o tubulární sekreci (probenecid × penicilin).
**Farmakodynamické** nechávají hladinu beze změny a mění **účinek**: sčítání
(alkohol + benzodiazepin + opioid → útlum dechu), rušení (naloxon × morfin,
vitamin K × warfarin), nepřímé působení (NSA zvyšují tlak a ruší efekt
antihypertenziv) a sčítání rizik (prodloužení QT u makrolidu s antipsychotikem).
**Typy výsledku:** aditivní 1+1=2, synergie 1+1=5, **potenciace 0+1=5** (látka
sama neúčinná zesílí druhou), antagonismus — princip antidot.
**Nejdůležitější:** „triple whammy" (NSA + ACE inhibitor + diuretikum → selhání
ledvin), ibuprofen ruší antiagregační účinek aspirinu, rifampicin a třezalka ruší
antikoncepci, makrolid + statin → rabdomyolýza, IMAO + tyramin → hypertenzní
krize.
""")

K("O26", "Farmakogenetika, genetický polymorfismus", """
**Farmakogenetika** zkoumá, jak dědičné odchylky mění odpověď na léčivo. Nejvíce
se uplatní u enzymů biotransformace.
**Polymorfismus CYP2D6** rozděluje populaci na **pomalé, normální a ultrarychlé
metabolizátory**. U běžného léčiva znamená pomalý metabolizátor kumulaci a
toxicitu. **U proléčiva je to přesně naopak:** kodein se musí přes CYP2D6
přeměnit na morfin, takže pomalý metabolizátor nemá analgezii, zatímco
ultrarychlý si vyrobí morfinu příliš — u dětí byla popsána úmrtí. Stejně tak
**klopidogrel** aktivuje CYP2C19.
**Další významné enzymy:** CYP2C9 (warfarin, fenytoin), N-acetyltransferáza
(izoniazid — rychlí a pomalí acetylátoři, u pomalých vyšší riziko neuropatie a
hepatotoxicity).
**Neenzymové odchylky:** **TPMT** (nízká aktivita → těžká myelosuprese po
azathioprinu), **plazmatická cholinesteráza** (prodloužená apnoe po
sukcinylcholinu), **deficit G6PD** (hemolýza po primachinu, sulfonamidech,
nitrofurantoinu), ryanodinový receptor (maligní hypertermie).
**HLA a závažné reakce:** HLA-B*5701 a abakavir (testuje se před nasazením),
HLA-B*1502 a karbamazepin, HLA-B*5801 a alopurinol.
""")

K("O27", "Tolerance, tachyfylaxe, rezistence", """
Rozhodující otázka je, **kdo se změnil** — organismus, nebo patogen.
**Tolerance** je slábnutí odpovědi organismu při opakovaném podávání; vzniká dny
až týdny. Mechanismy: **down-regulace receptorů**, desenzibilizace, indukce
metabolických enzymů a protiregulační pochody. Existuje **zkřížená tolerance**
mezi látkami stejné skupiny (alkohol a benzodiazepiny). U opioidů se toleruje
analgezie, euforie i útlum dechu, ale **nikdy mióza a zácpa**.
**Tachyfylaxe** je prudký pokles účinku během hodin, typicky vyčerpáním zásob:
nepřímá sympatomimetika (prázdné vezikuly s noradrenalinem), nitráty (proto
denní nitrátový interval), nosní dekongescencia.
**Rezistence** znamená změnu **mikroorganismu nebo nádorové buňky**, ne
pacienta: tvorba **betalaktamáz**, změna cílové struktury (MRSA má pozměněný
PBP2a), **efluxní pumpy** a snížená propustnost stěny. Roste s používáním
antibiotik, proto antibiotická stewardship.
**Příbuzné pojmy:** závislost psychická (craving) a fyzická (odvykací stav),
senzibilizace jako opak tolerance a **rebound fenomén** po vysazení
(betablokátory, nitráty, benzodiazepiny, inhibitory protonové pumpy).
""")

K("O28", "Vliv průvodních onemocnění, polypragmazie", """
**Nemoc mění kinetiku i dynamiku.** Jaterní postižení snižuje metabolickou
kapacitu a albumin, renální insuficience vede ke kumulaci léčiv vylučovaných
ledvinami, srdeční selhání zhoršuje prokrvení střeva a jater, hypotyreóza
zpomaluje metabolismus, dehydratace a sepse mění distribuci.
**Polypragmazie** je současné užívání pěti a více léčiv. Počet možných interakcí
roste **geometricky**, takže u osmi léků je z hlavy neuhlídá nikdo. Přináší vyšší
riziko nežádoucích účinků, pádů a hospitalizací a **zhoršuje adherenci** —
pacient přestane brát i to důležité.
**Preskripční kaskáda** je situace, kdy se nežádoucí účinek považuje za novou
nemoc a nasadí se na něj další lék: blokátor kalciových kanálů → otoky kotníků →
diuretikum (které nepomůže); NSA → vzestup tlaku → antihypertenzivum;
metoklopramid → parkinsonismus → antiparkinsonikum. **Každý nový příznak u
polymorbidního pacienta je do prokázání opaku nežádoucí účinek.**
**Řešením** je pravidelná revize medikace, kritéria **STOPP** (co vysadit) a
**START** (co chybí), Beersova kritéria pro seniory a fixní kombinace.
""")

K("O29", "Nežádoucí účinky léčiv", """
**Nežádoucí účinek** je nechtěná reakce na léčivo v běžné dávce. Základní dělení
je na typ A a typ B.
**Typ A („augmented")** vyplývá z farmakologického mechanismu, je **závislý na
dávce a předvídatelný**, častý a obvykle méně závažný — krvácení po warfarinu,
sucho v ústech po atropinu, hypoglykemie po inzulinu. **Řeší se snížením dávky.**
**Typ B („bizarre")** s mechanismem nesouvisí, je **nezávislý na dávce a
nepředvídatelný**, vzácný, ale často závažný — alergie, agranulocytóza,
aplastická anemie, maligní hypertermie. **Řeší se okamžitým vysazením a lék se
už nikdy nepodá.**
**Rozšířené dělení:** C — chronické při dlouhodobém podávání (osteoporóza po
kortikoidech), D — opožděné (karcinogenita, teratogenita), E — po vysazení
(rebound), F — selhání léčby (interakce s induktorem).
**Farmakovigilance** je sledování bezpečnosti po registraci. **Hlášení podezření
na nežádoucí účinek SÚKL je povinností zdravotníka**, zejména u účinků
závažných, neočekávaných a u nově registrovaných léčiv. Signál vede k
přehodnocení, změně informací o přípravku nebo stažení z trhu.
""")

K("O30", "Léková alergie, idiosynkrazie", """
Ne každá reakce na léčivo je alergie.
**Alergie** je imunitně zprostředkovaná reakce. Vyžaduje **předchozí
senzibilizaci**, takže při prvním podání nevznikne, a **nezávisí na dávce** —
stačí stopové množství. Podle Coombse a Gella: **I. typ** IgE (anafylaxe,
kopřivka, bronchospazmus), **II.** cytotoxický (hemolýza, trombocytopenie),
**III.** imunokomplexový (sérová nemoc, vaskulitida), **IV.** pozdní buněčný
(kontaktní ekzém, lékové exantémy, Stevensův–Johnsonův syndrom).
**Idiosynkrazie** není imunitní: jde o geneticky danou odchylku enzymu nebo
receptoru, a proto se může projevit **hned při prvním podání** — hemolýza při
deficitu G6PD, prodloužená apnoe po sukcinylcholinu, maligní hypertermie.
**Anafylaxe** se rozvíjí během minut: kožní projevy, otok, bronchospazmus a
pokles tlaku. Lékem první volby je **adrenalin 0,5 mg i.m. do stehna**;
antihistaminikum a kortikoid jsou jen doplněk a působí pozdě.
**Anafylaktoidní reakce** vypadá stejně, ale probíhá **bez IgE** přímým
uvolněním histaminu — kontrastní látky, vankomycin, opioidy, NSA. Ampicilinový
exantém u infekční mononukleózy alergie není.
""")

K("O31", "Karcinogenní a mutagenní účinky", """
**Mutagen** poškozuje DNA, **karcinogen** vyvolává nádor a **teratogen**
poškozuje vývoj plodu. Mezi zásahem a nádorem uplynou roky, proto se
karcinogenita v klinické studii nikdy neprojeví a hodnotí se nepřímo.
**Karcinogeny genotoxické** poškozují DNA přímo; u nich **se nepředpokládá
bezpečná prahová dávka**. **Negenotoxické** působí nepřímo (hormonální
stimulace, chronický zánět, imunosuprese) a práh mají.
**Testování:** **Amesův test** ověří mutagenitu na bakteriích *Salmonella* a
slouží jako rychlý screening; dále testy chromozomových aberací a mikrojader na
buněčných kulturách a dvouleté studie na hlodavcích. Epidemiologické studie
hodnotí člověka.
**Klasifikace IARC:** skupina 1 prokázaný karcinogen pro člověka, 2A
pravděpodobný, 2B možný, 3 neklasifikovatelný. Vyjadřuje **sílu důkazu, ne
velikost rizika**.
**V medicíně:** alkylační cytostatika (sekundární leukemie), imunosupresiva
(lymfomy a kožní nádory), estrogeny bez gestagenu (karcinom endometria),
ionizující záření. Ochrana spočívá v odůvodněné indikaci a nejnižší účinné dávce.
""")

K("O32", "Léčiva v těhotenství, teratogenní účinek, léčiva v době kojení", """
Riziko závisí na době expozice.
**1.–2. týden** platí pravidlo „vše, nebo nic" — buď dojde k potratu, nebo se
nic nestane. **3.–8. týden je organogeneze a největší riziko strukturálních
vad.** Od 9. týdne do porodu vznikají spíše funkční poruchy a poruchy růstu;
kolem porodu hrozí útlum novorozence nebo odvykací stav. Nejrizikovější je doba,
kdy žena o těhotenství ještě neví.
**Klasické teratogeny:** isotretinoin a vysoké dávky vitaminu A, thalidomid,
**valproát** (defekty neurální trubice, nižší IQ), **warfarin**, **ACE
inhibitory a sartany**, methotrexát, tetracykliny, lithium (Ebsteinova anomálie)
a alkohol (fetální alkoholový syndrom).
**Bezpečnější volby:** bolest — **paracetamol** (NSA ne ve 3. trimestru, hrozí
uzávěr ductus arteriosus); infekce — peniciliny, cefalosporiny, makrolidy; tlak
— **methyldopa**, labetalol, nifedipin; antikoagulace — **nízkomolekulární
heparin**, který neprochází placentou.
**Kojení:** do mléka přejde téměř každé léčivo, jde o množství. Mléko je mírně
kyselé, takže se v něm hromadí zásaditá léčiva (iontová past). Podává se ihned
po kojení, volí se krátký poločas; nevhodná jsou cytostatika, radiofarmaka,
lithium a amiodaron.
""")

K("O33", "Farmakoterapie v dětství", """
**Dítě není malý dospělý** — má kvalitativně jinou kinetiku, ne jen menší
hmotnost. Novorozencem se rozumí dítě do 28. dne.
**Absorpce:** vyšší pH žaludku (kyselá léčiva se hůř vstřebávají), pomalá pasáž,
tenká a dobře prokrvená kůže — lokální přípravky se vstřebávají výrazně více.
**Distribuce:** až **75 % vody** a málo tuku (hydrofilní léčiva mají větší
distribuční objem), **nízký albumin** a nezralá hematoencefalická bariéra.
**Metabolismus:** oxidace (fáze I) částečně funguje, ale **glukuronidace (fáze
II) dozrává až kolem 2 let**. **Exkrece:** glomerulární filtrace dozrává v
polovině druhého roku.
**Tři typické nežádoucí účinky:** **Reyeův syndrom** (aspirin u dítěte s virózou
→ jaterní encefalopatie), **gray baby syndrom** (chloramfenikol při nezralé
glukuronidaci), **tetracykliny** ukládající se do kostí a zubů. **Jádrový
ikterus** vzniká součtem tří nezralostí — sulfonamid vytěsní bilirubin z
albuminu, glukuronidace nestačí a bariéra propouští.
**Dávkuje se podle povrchu těla**, protože metabolická aktivita sleduje spíš
povrch než hmotnost. Bolest a horečka: paracetamol nebo ibuprofen, nikdy aspirin.
Mnoho léčiv se u dětí podává off-label.
""")

K("O34", "Farmakoterapie ve stáří, polypragmazie", """
Ve stáří se mění složení těla, orgánové funkce i citlivost tkání.
**Distribuce se mění dvěma protichůdnými směry:** **ubývá vody**, takže
hydrofilní léčivo se má kam méně rozředit a jeho **koncentrace hned stoupne**
(digoxin, lithium, aminoglykosidy — problém po první dávce); **přibývá tuku**,
takže lipofilní léčivo má větší distribuční objem a **delší poločas**
(benzodiazepiny — problém až po týdnu kumulace).
**Eliminace:** klesá jaterní průtok i enzymová kapacita, klesá glomerulární
filtrace. **Normální kreatinin neznamená normální ledviny** — senior ho při
úbytku svalové hmoty méně tvoří a zároveň hůře vylučuje, takže se obě změny
vyruší; funkce se odhaduje výpočtem.
**Dynamika:** vyšší citlivost centrálního nervového systému a chybějící
adaptační rezerva (ortostáza, pády, zmatenost).
**Zásady:** „start low, go slow", pravidelná revize medikace, kritéria **STOPP**
(co vysadit) a **START** (co chybí — podléčení je stejný problém jako
předávkování), **Beersova kritéria**. Nejrizikovější skupiny jsou
benzodiazepiny, anticholinergika a nesteroidní antirevmatika.
""")

K("O35", "Biologická léčba: rozdělení, názvosloví, biosimilars, přínosy a rizika", """
**Biologické léčivo** je látka vyráběná živým organismem, zpravidla velká
bílkovina z rekombinantní DNA technologie. Všechny jeho vlastnosti plynou z toho,
že jde o bílkovinu: v trávicím traktu by se strávila, proto se podává **jen
parenterálně**; imunitní systém ji rozpozná, proto hrozí **imunogenita** s tvorbou
protilátek a ztrátou účinku; a protože ji tvoří živá buňka, **nelze vyrobit
identickou kopii**.
**Skupiny a koncovky:** **-mab** monoklonální protilátka (adalimumab, rituximab,
trastuzumab), **-cept** fúzní receptor (etanercept), **-kin** interleukiny,
**-stim** růstové faktory (filgrastim), **-poetin**; dále rekombinantní hormony
a enzymy. Koncovka **-tinib** označuje malé molekuly, které biologiky **nejsou**.
**Názvosloví protilátek** kopíruje původ: **-o-** myší, **-xi-** chimérická,
**-zu-** humanizovaná, **-u-** plně humánní — čím lidštější, tím méně imunogenní.
**Biosimilar** není generikum: liší se glykosylací a musí se vejít do pásma
kolísání originálu, což vyžaduje srovnávací studie.
**Rizika:** infekce (před anti-TNF **screening tuberkulózy**, protože TNF-α drží
granulom pohromadě), reakce na infuzi, imunogenita, vysoká cena; **žádné živé
vakcíny**.
""")


# ═══════════════════════════════ SPECIÁLNÍ FARMAKOLOGIE I

K("36", "Cholinergní přenos vzruchu", """
**Acetylcholin** vzniká z cholinu a acetyl-CoA působením cholinacetyltransferázy,
ukládá se do vezikul a po depolarizaci a vstupu vápníku se uvolní exocytózou
(**botulotoxin** ji blokuje štěpením SNARE proteinů). Ve štěrbině je **rozštěpen
acetylcholinesterázou** na cholin a acetát; cholin se vychytá zpět
(hemicholinium tento krok blokuje).
**Klíčový rozdíl proti adrenergnímu přenosu:** acetylcholin se rozkládá enzymem
přímo ve štěrbině, kdežto noradrenalin se vychytává zpět do neuronu. Proto na
cholinergní přenos působí inhibitory esterázy a na adrenergní blokátory reuptake.
**Receptory jsou dvojí. Muskarinové** (metabotropní, přes G-protein, odpověď v
sekundách): **M1** v CNS, gangliích a parietálních buňkách žaludku, **M2** v
srdci — jediný tlumivý, přes Gi, **M3** v hladké svalovině a **žlázách**, M4 a M5
v CNS. **Nikotinové** (ionotropní, samy jsou kanálem, odpověď v milisekundách):
**Nm** na nervosvalové ploténce, **Nn** v gangliích a dřeni nadledvin.
Acetylcholin je přenašečem všech pregangliových vláken, postgangliových vláken
parasympatiku, ploténky a — jako výjimka — sympatických vláken k **potním
žlázám**.
""")

K("37", "Přímá cholinomimetika", """
**Přímá cholinomimetika** se sama vážou na cholinergní receptory a napodobují
acetylcholin.
**Estery cholinu:** acetylcholin (v praxi nepoužitelný, esteráza jej zničí během
vteřin), **karbachol** (odolný vůči esteráze, i nikotinový účinek),
**betanechol** (selektivní pro M3, prakticky bez vlivu na srdce), methacholin
(diagnostika bronchiální hyperreaktivity).
**Přírodní alkaloidy:** **pilokarpin**, muskarin, arekolin.
**Účinky odpovídají aktivaci celého parasympatiku:** mióza, akomodace na blízko a
pokles nitroočního tlaku; slinění, slzení, pocení a bronchiální sekrece;
bradykardie a zpomalení AV vedení; bronchokonstrikce; zvýšená peristaltika a
sekrece v trávicím traktu; vyprázdnění močového měchýře.
**Indikace:** glaukom a **xerostomie** u Sjögrenova syndromu a po ozáření
(pilokarpin), pooperační atonie střeva a měchýře (betanechol).
**Nežádoucí účinky** shrnuje zkratka **SLUDGE** — salivace, lakrimace, urinace,
defekace, gastrointestinální křeče, emeze — plus mióza a bronchospazmus.
**Kontraindikace:** astma a CHOPN, vředová choroba, bradykardie a AV blokáda,
obstrukce střeva či močových cest.
""")

K("38", "Nepřímá cholinomimetika", """
**Nepřímá cholinomimetika** se na receptor nevážou — **inhibují
acetylcholinesterázu**, takže acetylcholin zůstává ve štěrbině déle a působí
silněji.
**Reverzibilní krátkodobé:** **edrofonium** (diagnostika myasthenie).
**Reverzibilní střednědobé:** **neostigmin** a pyridostigmin — kvartérní, nabité,
**neprocházejí do mozku**; **fyzostigmin** — terciární, **do mozku prochází**, a
proto je antidotem centrálního anticholinergního syndromu.
**Centrálně působící:** donepezil, rivastigmin, galantamin u Alzheimerovy nemoci.
**Ireverzibilní:** organofosfáty (insekticidy, sarin) a karbamáty.
**Indikace:** myasthenia gravis, **dekurarizace** po nedepolarizujících
myorelaxanciích, atonie střeva a měchýře, glaukom.
**Neostigmin se podává s atropinem** — zvýší acetylcholin všude, ale atropin
odstřihne nežádoucí muskarinové účinky (bradykardii) a ploténku (Nm) ponechá.
**Otrava organofosfáty:** SLUDGE, mióza jako špendlíková hlavička, bronchorea,
fascikulace, slabost a křeče; smrt nastává zahlcením dýchacích cest. **Léčba:
atropin plus pralidoxim** jako reaktivátor enzymu, který musí být podán dřív, než
vazba „zestárne".
""")

K("39", "Parasympatolytika", """
**Parasympatolytika** jsou kompetitivní antagonisté **muskarinových** receptorů;
acetylcholin se uvolní, ale nemá si kam sednout. Prototypem je **atropin** z
rulíku zlomocného.
**Zástupci:** atropin, skopolamin, homatropin; **kvartérní** deriváty, které
zůstávají v místě podání — **ipratropium a tiotropium** inhalačně,
butylskopolamin jako spazmolytikum; **uroselektivní** oxybutynin, tolterodin,
solifenacin; oční tropikamid a cyklopentolát.
**Účinky jsou obrazem vypnutého parasympatiku:** mydriáza, cykloplegie a vzestup
nitroočního tlaku; **sucho v ústech**, snížené pocení a sekrece; tachykardie;
bronchodilatace; útlum peristaltiky a zácpa; retence moči.
**Indikace:** bradykardie a premedikace, **CHOPN a astma** (inhalační formy),
spazmy trávicího a močového ústrojí, hyperaktivní měchýř, kinetóza (skopolamin),
oftalmologie a **antidotum otravy organofosfáty**.
**Otrava** se popisuje pěti přirovnáními: slepý jako netopýr, suchý jako kost,
červený jako řepa, horký jako pec (nepotí se) a šílený jako kloboučník
(delirium). **Antidotem je fyzostigmin.**
**Kontraindikace:** glaukom s úzkým úhlem, hyperplazie prostaty s retencí, ileus.
""")

K("40", "Adrenergní přenos vzruchu", """
**Syntéza:** tyrosin → **DOPA** (tyrosinhydroxyláza je krokem určujícím
rychlost) → dopamin → uvnitř vezikuly **noradrenalin**; jen v dřeni nadledvin
navíc enzym **PNMT** tvoří **adrenalin**, proto je adrenalin hormon, ne
přenašeč.
**Zánik účinku není enzymatický ve štěrbině, ale zpětným vychytáním
(reuptake, uptake-1) do neuronu** — tento krok blokuje kokain a tricyklická
antidepresiva. Teprve poté látku odbourává **MAO** uvnitř neuronu a **COMT**
extraneuronálně.
**Receptory:** **α1** — stah cév, mydriáza, sfinktery, hladká svalovina prostaty
(Gq); **α2** — presynaptická brzda výdeje, centrálně snižuje tonus sympatiku
(Gi); **β1** — srdeční frekvence a kontraktilita, výdej reninu; **β2** —
bronchodilatace, dilatace cév v kosterním svalu, relaxace dělohy, tremor a
hypokalemie; **β3** — lipolýza a relaxace detruzoru.
**Místa zásahu léčiv:** syntéza (methyldopa jako falešný přenašeč), skladování a
výdej (rezerpin, nepřímá sympatomimetika), reuptake (kokain, tricyklika, SNRI),
odbourání (inhibitory MAO a COMT) a receptor (sympatomimetika a sympatolytika).
""")

K("41", "Neselektivní sympatomimetika", """
**Neselektivní sympatomimetika** aktivují více typů adrenergních receptorů
zároveň a liší se tím, který převáží.
**Adrenalin** působí na α i β. **Noradrenalin** na α1 a β1, prakticky **bez β2**,
proto zvyšuje tlak a vyvolává reflexní bradykardii; používá se jako vazopresor v
šoku. **Isoprenalin** je čistý β1 a β2 agonista. **Dopamin** má **dávkově závislý
účinek**: nízká dávka působí na D1 (dilatace ledvinných cév), střední na β1
(inotropní podpora), vysoká na α1 (vazokonstrikce).
**Adrenalin je lékem volby u anafylaxe**, protože jako jediný pokryje všechny
složky reakce najednou: α1 stáhne cévy a zvedne tlak, β1 podpoří srdce, β2 rozšíří
průdušky a zároveň zastaví vyplavování mediátorů ze žírných buněk. Podává se
**0,5 mg i.m. do stehna** (roztok 1 : 1000). Dále se užívá při resuscitaci a jako
**vazokonstrikční přísada k lokálním anestetikům** — prodlouží účinek a sníží
systémovou toxicitu.
**Nežádoucí účinky:** tachykardie, arytmie, hypertenze, tremor, úzkost.
**Adrenalinová reverze** znamená, že po α-blokádě vyvolá adrenalin místo vzestupu
tlaku pokles, protože zbudou jen β2 účinky.
""")

K("42", "Sympatomimetika alfa", """
Skupina se dělí podle receptoru a působí **protichůdně**.
**α1 agonisté** působí periferně: **fenylefrin** (dekongesce nosní sliznice,
mydriáza bez cykloplegie, léčba hypotenze), **midodrin** u ortostatické
hypotenze, **nafazolin, xylometazolin a oxymetazolin** jako nosní kapky. Stahují
cévy, zvyšují tlak a vyvolávají reflexní bradykardii. **Nosní dekongescencia se
smějí podávat nejvýše 5–7 dní**, jinak vzniká *rhinitis medicamentosa* — sliznice
po odeznění účinku oteče ještě víc a pacient se dostane do bludného kruhu.
**α2 agonisté** působí **centrálně a presynapticky**: sednou si na brzdu výdeje
noradrenalinu, a proto **snižují krevní tlak**, přestože jde o „alfa" agonisty.
Patří sem **klonidin** (nežádoucí je sucho v ústech, sedace a **rebound
hypertenze** po náhlém vysazení), **methyldopa** jako antihypertenzivum volby v
graviditě, **brimonidin** u glaukomu, **tizanidin** u spasticity a
**dexmedetomidin** k sedaci.
Rozdíl mezi periferním α1 a centrálním α2 účinkem je nejčastěji zkoušeným bodem
celé skupiny.
""")

K("43", "Sympatomimetika beta", """
**β2 agonisté** jsou základem úlevové léčby astmatu. **SABA** (krátkodobé):
salbutamol, fenoterol, terbutalin — nástup do minut, podávají se podle potřeby.
**LABA** (dlouhodobé): formoterol, salmeterol, indakaterol. **LABA se u astmatu
nikdy nepodává samostatně** — bez inhalačního kortikoidu zvyšuje úmrtnost, proto
existují fixní kombinace. Formoterol nastupuje rychle, a proto může sloužit i
úlevově; salmeterol nikoli.
**Další využití β2:** **tokolýza** (hexoprenalin oddálí předčasný porod) a
**akutní hyperkalemie**, protože β2 stimulace přesouvá draslík do buněk.
**β1 agonista dobutamin** je inotropikum u akutního srdečního selhání a
kardiogenního šoku. **β3 agonista mirabegron** relaxuje detruzor u hyperaktivního
měchýře a nemá anticholinergní nežádoucí účinky.
**Tři typické nežádoucí účinky β2 mimetik** plynou z jediného receptoru:
**tremor** (β2 na kosterním svalu), **tachykardie** (přelití účinku na β1) a
**hypokalemie**. Dále neklid, bolest hlavy a při nadužívání tolerance.
**Rostoucí spotřeba úlevového inhalátoru** je známkou nedostatečně kontrolovaného
astmatu.
""")

K("44", "Nepřímá sympatomimetika", """
**Nepřímá sympatomimetika** se na receptor nevážou. Buď **vytlačují noradrenalin
z vezikul**, nebo **blokují jeho zpětné vychytávání**; výsledkem je zvýšená
koncentrace přenašeče ve štěrbině.
**Vyplavující:** efedrin a pseudoefedrin (smíšený mechanismus), amfetamin,
metamfetamin a **tyramin**. Protože potřebují zásoby, vzniká při opakovaném
podání **tachyfylaxe** — prudký pokles účinku během hodin z vyprázdněných
vezikul. To přímá sympatomimetika nedělají.
**Blokující reuptake:** **kokain**, tricyklická antidepresiva, modafinil. Kokain
vyvolává vazokonstrikci s rizikem infarktu a cévní mozkové příhody i u mladých a
při šňupání nekrózu nosní přepážky.
**Sýrový (tyraminový) efekt:** tyramin z uzrálých sýrů, vína a uzenin ve střevě
běžně odbourá monoaminooxidáza. U pacienta na **neselektivním inhibitoru MAO**
projde do oběhu, vytlačí noradrenalin a vyvolá **hypertenzní krizi**. Moklobemid
jako reverzibilní inhibitor toto riziko nemá.
**Použití:** efedrin u hypotenze v anestezii, pseudoefedrin jako dekongescens,
metylfenidát u ADHD, modafinil u narkolepsie.
""")

K("45", "Sympatolytika alfa", """
**Alfa-blokátory** ruší vazokonstrikci zprostředkovanou α1 receptory.
**Neselektivní:** **fentolamin** (reverzibilní, krátce působící) a
**fenoxybenzamin** (ireverzibilní). Používají se k přípravě pacienta s
**feochromocytomem** k operaci; fentolamin se aplikuje také lokálně při
extravazaci noradrenalinu, aby nevznikla nekróza.
**Zásadní pravidlo:** u feochromocytomu se blokuje **nejprve alfa, teprve potom
beta**. Opačné pořadí zablokuje β2 vazodilataci, zůstane nekrytý α1 stah a vzniká
hypertenzní krize.
**α1-selektivní:** prazosin, doxazosin, terazosin — hypertenze, zvláště současně
s hyperplazií prostaty. **Uroselektivní α1A** tamsulosin a silodosin míří na
prostatu a hrdlo měchýře, a proto tlak prakticky nesnižují.
**Nežádoucí účinky:** ortostatická hypotenze a **„first-dose efekt"** (první
dávka může vyvolat kolaps, proto se podává malá dávka na noc vleže), reflexní
tachykardie, retrográdní ejakulace, ucpaný nos a **floppy iris syndrom**
komplikující operaci šedého zákalu u pacientů na tamsulosinu.
""")

K("46", "Sympatolytika beta (betablokátory)", """
**Betablokátory** jsou kompetitivní antagonisté β receptorů. Klinicky rozhoduje
**selektivita** — žádoucí účinky plynou z blokády β1, nežádoucí z blokády β2.
**Dělení:** **neselektivní** — propranolol (lipofilní, proniká do CNS), sotalol
(navíc III. třída antiarytmik), **timolol** (i v očních kapkách), karvedilol
(navíc α1 blokáda); **β1-selektivní** — metoprolol, bisoprolol, atenolol,
betaxolol, nebivolol (navíc uvolňuje NO); **s vnitřní aktivitou** — pindolol.
**Mechanismus:** snížení srdečního výdeje a frekvence, snížení výdeje reninu a
centrální útlum sympatiku.
**Indikace:** ischemická choroba srdeční, hypertenze, tachyarytmie, **srdeční
selhání** (jen bisoprolol, metoprolol ZOK, karvedilol a nebivolol, nasazovat
nízko a titrovat týdny), tyreotoxikóza, esenciální tremor, profylaxe migrény,
glaukom, portální hypertenze.
**Nežádoucí účinky:** bronchospazmus (kontraindikace u astmatu i z očních kapek),
bradykardie a AV blokáda, únava, studené končetiny, **maskování hypoglykemie**
(pocení zůstane, je cholinergní).
**Nikdy nevysazovat náhle** — receptory jsou up-regulované a hrozí rebound
tachykardie až infarkt.
""")

K("47", "Myorelaxancia", """
**Periferní myorelaxancia** působí na nervosvalové ploténce a používají se v
anestezii.
**Depolarizující — sukcinylcholin:** trvale depolarizuje ploténku, nejprve
vyvolá fascikulace, pak ochabnutí. Má velmi rychlý nástup a krátké trvání.
**Nemá antidotum** — neostigmin by blok prohloubil, protože problémem je nadbytek,
nikoli nedostatek acetylcholinu. Rizika: **hyperkalemie** (u popálenin a poranění
míchy smrtelná), **maligní hypertermie** (zvláště s halogenovanými anestetiky) a
**atypická pseudocholinesteráza** s apnoí trvající hodiny.
**Nedepolarizující (kompetitivní):** rokuronium, vekuronium, pankuronium,
atrakurium a cisatrakurium. **Antidotem je neostigmin s atropinem**, u rokuronia
**sugammadex**, který lék fyzicky obalí. **Atrakurium se rozpadá Hofmannovou
eliminací** nezávisle na játrech a ledvinách, proto je vhodné při jejich selhání.
**Centrální myorelaxancia** tlumí polysynaptické reflexy: **baklofen** (agonista
GABA-B), tizanidin, tolperison a benzodiazepiny; používají se u spasticity.
**Dantrolen** působí přímo na sval — blokuje výdej vápníku ze sarkoplazmatického
retikula a je antidotem maligní hypertermie.
""")

K("48", "Lokální anestetika", """
**Lokální anestetika** jsou slabé zásady, které **blokují napěťově řízené
sodíkové kanály zevnitř buňky**, a tím zastaví vedení vzruchu. Aby se dovnitř
dostala, musí být v **nenabité formě**.
**Estery** (prokain, tetrakain, benzokain) štěpí plazmatická cholinesteráza;
jejich metabolit PABA vyvolává alergie. **Amidy** (lidokain, mepivakain,
**artikain**, bupivakain, prilokain, trimekain) se metabolizují v játrech a
alergie jsou u nich výjimečné. Artikain nese navíc esterovou skupinu, a proto má
krátký poločas a nízkou systémovou toxicitu.
**V zánětu je kyselé pH**, anestetikum je proto ionizované už mimo buňku,
neprojde membránou a účinek je slabý — řešením je svodná anestezie mimo zánět,
nikoli zvyšování dávky.
**Vazokonstriktor** (adrenalin) prodlouží účinek, sníží krvácení i systémovou
toxicitu; nepodává se do akrálních částí.
**Systémová toxicita** začíná v CNS: brnění kolem úst, kovová chuť, tinnitus,
neklid a křeče, teprve pak nastupuje kardiovaskulární kolaps. **Bupivakain je
nejvíce kardiotoxický**, prilokain vyvolává methemoglobinemii. **Antidotem je
lipidová emulze** spolu se zajištěním dýchání.
""")

K("49", "Celková anestetika — inhalační", """
Účinek inhalačních anestetik popisují **dvě nezávislé veličiny**. **MAC**
(minimální alveolární koncentrace, při níž polovina pacientů nereaguje na kožní
řez) vyjadřuje **sílu** — čím nižší MAC, tím silnější anestetikum.
**Rozpustnost v krvi** (koeficient krev/plyn) určuje **rychlost** nástupu a
probuzení — čím nižší rozpustnost, tím rychlejší nástup.
**Halotan** je obsoletní pro hepatotoxicitu a senzibilizaci myokardu ke
katecholaminům. **Isofluran** je levný, ale dráždivý. **Sevofluran** je dnes
standardem — sladký a nedráždivý, vhodný k úvodu maskou u dětí. **Desfluran** je
nejrychlejší, ale dráždí dýchací cesty.
**Oxid dusný** má MAC nad 100 %, takže **sám nikdy neuspí**, zato má výborný
**analgetický** účinek a používá se k sedaci a analgezii u úzkostných pacientů a
dětí. Rizika: difuzní hypoxie při ukončení (podává se 100% kyslík), inaktivace
vitaminu B12 a expanze uzavřených dutin.
**Maligní hypertermie** je geneticky podmíněná porucha ryanodinového receptoru;
spouštějí ji halogenovaná anestetika a sukcinylcholin. Projeví se rigiditou,
prudkým vzestupem teploty, acidózou a rabdomyolýzou. Léčbou je **dantrolen**.
""")

K("50", "Celková anestetika — intravenózní", """
Nitrožilní anestetika slouží především k **úvodu do anestezie**, protože působí
během jednoho oběhu krve. Většina působí přes **receptor GABA-A**, výjimkou je
ketamin.
**Propofol** má rychlý nástup, čisté probuzení a **antiemetický** účinek, ale
sráží tlak, nemá analgetickou složku a při dlouhé infuzi hrozí propofolový
infuzní syndrom.
**Thiopental** je ultrakrátce působící barbiturát; jeho krátkost je dána
**redistribucí do tuku a svalů, nikoli metabolismem**, proto se po opakovaných
dávkách **kumuluje** a probouzení trvá hodiny.
**Ketamin** blokuje **NMDA** receptor. Jako jediný **zachovává dýchání a zvyšuje
krevní tlak** a má silný analgetický účinek, proto se hodí u šokového pacienta, v
terénu a u popálenin. Vyvolává halucinace při probouzení (podává se s
benzodiazepinem) a hypersalivaci.
**Etomidát** je kardiálně nejstabilnější, ale tlumí kůru nadledvin a vyvolává
myoklonie. **Midazolam** přináší anxiolýzu a anterográdní amnézii, nastupuje
pomaleji a jeho antidotem je flumazenil.
K bolestivému výkonu je vždy nutné přidat **opioid**.
""")

K("51", "Hypnotika", """
Hypnotika navozují spánek. Vývojová řada barbituráty → benzodiazepiny →
Z-hypnotika byla hnána snahou o **širší bezpečnostní okno**.
**Receptor GABA-A je chloridový kanál.** **Benzodiazepin** zvyšuje **frekvenci**
jeho otevírání, ale bez vlastní GABA neudělá nic — má proto **strop účinku**.
**Barbiturát** prodlužuje **dobu** otevření a ve vyšší dávce otevře kanál i bez
GABA, takže **strop nemá** a může zabít.
**Barbituráty** (fenobarbital, thiopental) mají velmi úzké terapeutické okno,
silně indukují jaterní enzymy a **nemají antidotum**; jako hypnotika se
nepoužívají.
**Z-hypnotika** (zolpidem, zopiklon, zaleplon) se vážou převážně na podjednotku
α1, takže navozují spánek téměř bez myorelaxace a antikonvulzivního účinku, mají
krátký poločas a menší ranní útlum. Rizikem jsou **parasomnie** — noční jedení,
chození či řízení s amnézií.
**Další možnosti:** melatonin a jeho agonisté posouvají vnitřní hodiny,
antihistaminika I. generace, trazodon a mirtazapin.
**Hypnotikum se podává krátkodobě a jako doplněk** — základem je spánková hygiena
a kognitivně-behaviorální terapie. U seniorů znamenají benzodiazepiny pády.
""")

K("52", "Benzodiazepiny", """
**Benzodiazepiny** jsou pozitivní alosterické modulátory receptoru **GABA-A**:
samy kanál neotevřou, jen zesílí účinek vlastní GABA, a proto mají strop.
**Pět účinků najednou:** anxiolýza, sedace a hypnóza, **antikonvulzivní** účinek
(lék volby u status epilepticus), centrální myorelaxace a **anterográdní
amnézie** — proto se midazolam podává před výkony.
**Dělení podle poločasu:** krátkodobé (midazolam, triazolam) k premedikaci;
středně dlouhé (alprazolam, oxazepam, lorazepam) u úzkosti a paniky; dlouhodobé
(diazepam, klonazepam) u epilepsie, spasticity a odvykacího stavu. **Lorazepam,
oxazepam a temazepam** se pouze konjugují bez fáze I, a jsou proto bezpečné u
jaterního postižení a u seniorů.
**Tolerance a závislost** vznikají poměrně rychle; po vysazení hrozí rebound
úzkost, nespavost a u dlouhodobých uživatelů i křeče, proto se vysazuje pomalu.
**Antidotem je flumazenil**, ale u závislého pacienta nebo u smíšené otravy s
tricyklickými antidepresivy může vyvolat křeče.
Samotný benzodiazepin usmrtí výjimečně; **smrtelná je kombinace s alkoholem nebo
opioidem**, které strop nemají.
""")

K("53", "Antiepileptika", """
Epileptický záchvat je **nadměrný synchronní výboj neuronů**. Antiepileptika ho
tlumí čtyřmi mechanismy, z nichž se dají odvodit zástupci.
**Blokáda sodíkových kanálů:** fenytoin, karbamazepin, lamotrigin, valproát.
**Blokáda T-kalciových kanálů: ethosuximid** — jen u absencí. **Zesílení GABA:**
benzodiazepiny, barbituráty, vigabatrin, tiagabin. **Tlumení glutamátu:**
topiramát, perampanel. Zvláštní postavení má **levetiracetam** (vazba na
vezikulární protein SV2A).
**Fenytoin** má **nelineární (saturační) kinetiku** — malé zvýšení dávky vede ke
skoku hladiny a k nystagmu, ataxii a zmatenosti; způsobuje **hyperplazii
gingivy**, hirsutismus a silně indukuje CYP.
**Valproát** je nejsilnějším teratogenem mezi antiepileptiky (defekty neurální
trubice, snížené IQ), dále hepatotoxicita, hyperamonemie, tremor a přírůstek
hmotnosti. **Karbamazepin** má autoindukci, vyvolává hyponatremii a u nositelů
HLA-B*1502 Stevensův–Johnsonův syndrom. **Lamotrigin** vyžaduje pomalou titraci
kvůli riziku exantému.
**Status epilepticus:** benzodiazepin i.v. → fenytoin nebo levetiracetam →
celková anestezie. **Nikdy nevysazovat náhle.**
""")

K("54", "Antiparkinsonika", """
Parkinsonova nemoc je **zánik dopaminergních neuronů nigrostriatální dráhy**.
Dopamin sám neprojde hematoencefalickou bariérou, jeho prekurzor **levodopa**
ano.
**Levodopa se vždy podává s inhibitorem periferní dekarboxylázy** (karbidopa,
benserazid), který do mozku neprochází; zabrání přeměně na periferii, sníží
nauzeu a hypotenzi a zvýší podíl látky, který dorazí do mozku. Nemá se zapíjet
bílkovinným jídlem, protože aminokyseliny soutěží o stejný přenašeč. Po letech
léčby se objevují dyskineze a kolísání účinku („wearing off", fenomén
„on–off").
**Agonisté D2** (pramipexol, ropinirol, rotigotin) se používají zejména u
mladších pacientů; mohou vyvolat **poruchy kontroly impulzů** — hráčství,
nakupování, hypersexualitu. **Inhibitory MAO-B** (selegilin, rasagilin) a
**COMT** (entakapon, tolkapon s hepatotoxicitou) prodlužují účinek levodopy.
**Amantadin** působí přes NMDA, **anticholinergika** (biperiden) hlavně na třes,
ale u seniorů zhoršují kognici.
**Parkinsonikovi se nesmí podat metoklopramid ani klasické antipsychotikum**;
bezpečnou alternativou proti nevolnosti je **domperidon**.
""")

K("55", "Neuroleptika (antipsychotika)", """
Antipsychotika blokují **dopaminové receptory D2**. Dopamin má v mozku čtyři
dráhy a lék je nerozliší — proto je jedna blokáda léčbou a tři nežádoucím
účinkem.
**Mezolimbická** dráha: blokáda tlumí halucinace a bludy (žádaný účinek).
**Mezokortikální:** blokáda zhoršuje negativní příznaky a kognici.
**Nigrostriatální:** blokáda vyvolá **extrapyramidové** příznaky.
**Tuberoinfundibulární:** dopamin je brzdou prolaktinu, takže blokáda způsobí
**hyperprolaktinemii** (galaktorea, amenorea, gynekomastie).
**Klasická:** vysokopotentní haloperidol a flufenazin (více extrapyramidových
účinků), nízkopotentní chlorpromazin a levomepromazin (sedace, anticholinergní
účinky, hypotenze). **Atypická** blokují navíc 5-HT2A, a proto mají méně
extrapyramidových účinků: risperidon (nejvíce zvyšuje prolaktin), olanzapin a
kvetiapin (metabolický syndrom), aripiprazol (parciální agonista).
**Extrapyramidové účinky v čase:** hodiny — akutní **dystonie** (léčí se
biperidenem), dny — akatizie, týdny — parkinsonismus, měsíce až roky —
**tardivní dyskineze**, často nevratná.
**Maligní neuroleptický syndrom** (rigidita, horečka, porucha vědomí, vysoká CK)
se léčí vysazením a dantrolenem. **Klozapin** je nejúčinnější u rezistentní
schizofrenie, ale hrozí **agranulocytóza**.
""")

K("56", "Antidepresiva — tricyklická, inhibitory MAO", """
Obě skupiny účinkují, ale jsou druhou volbou pro svou nebezpečnost.
**Tricyklická antidepresiva** (amitriptylin, nortriptylin, imipramin,
klomipramin, dosulepin) blokují zpětné vychytávání **noradrenalinu i
serotoninu** — to je žádoucí účinek. Zároveň blokují další tři receptory, odkud
plynou nežádoucí účinky: **muskarinové** (sucho v ústech, zácpa, retence moči,
rozmazané vidění), **H1** (sedace, přírůstek hmotnosti) a **α1** (ortostatická
hypotenze, pády). Blokádou sodíkových kanálů v myokardu vyvolávají při
předávkování **arytmie**, které jsou příčinou smrti; antidotem je
hydrogenuhličitan sodný. Mají **úzké terapeutické okno**, takže zásoba na dva
týdny může být smrtelnou dávkou. Dnes se používají hlavně u neuropatické bolesti
a v profylaxi migrény.
**Inhibitory MAO:** neselektivní ireverzibilní (tranylcypromin, fenelzin)
způsobují **tyraminovou („sýrovou") reakci** s hypertenzní krizí, a to až dva
týdny po vysazení. **Moklobemid** je reverzibilní inhibitor MAO-A, tyramin ho z
enzymu vytlačí, a je proto bezpečný.
**Serotoninový syndrom** (horečka, myoklonus, hyperreflexie, průjem) hrozí při
kombinaci s SSRI, tramadolem nebo triptany; na rozdíl od maligního
neuroleptického syndromu má hyperreflexii, nikoli rigiditu.
""")

K("57", "Antidepresiva — SSRI, SNRI, atypická", """
**SSRI** jsou dnes léky první volby u deprese a úzkostných poruch — ne proto, že
by byly účinnější než tricyklika, ale proto, že jsou **bezpečné při
předávkování** a lépe snášené. Blokují zpětné vychytávání serotoninu.
**Zástupci:** **fluoxetin** (dlouhý poločas, silný inhibitor CYP2D6),
**sertralin** (nejméně interakcí), **escitalopram a citalopram** (prodlužují QT),
**paroxetin** (anticholinergní, nejobtížnější vysazování).
**Nežádoucí účinky:** nauzea na začátku, **sexuální dysfunkce** (přetrvává),
nespavost nebo útlum, **hyponatremie (SIADH)** u seniorů, **zvýšená krvácivost**
z vyprázdnění serotoninu z trombocytů a **discontinuation syndrom** po náhlém
vysazení.
**Latence účinku je 2–4 týdny** a skrývá past: psychomotorický útlum se upraví
dříve než nálada, takže **na začátku léčby stoupá riziko sebevraždy**. První
epizoda se léčí nejméně 6 měsíců po odeznění příznaků.
**SNRI:** venlafaxin (ve vyšších dávkách zvyšuje tlak), duloxetin (i u
diabetické neuropatie).
**Atypická podle profilu:** **mirtazapin** (sedace a chuť k jídlu — výhodné u
nespavého a hubnoucího pacienta), **bupropion** (bez sexuálních nežádoucích
účinků, pomáhá při odvykání kouření, snižuje práh křečí), trazodon, agomelatin,
vortioxetin.
""")

K("58", "Anxiolytika, stabilizátory nálady", """
**Anxiolytika:** benzodiazepiny se hodí jen krátkodobě k překlenutí prvních
týdnů, protože vedou k toleranci a závislosti. **Dlouhodobou léčbou úzkostných
poruch jsou SSRI a SNRI.** **Buspiron** (parciální agonista 5-HT1A) je
nenávykový a nesedativní, ale nastupuje týdny, takže na akutní paniku nestačí.
Dále hydroxyzin, pregabalin a betablokátory, které potlačí jen tělesné projevy
(třes, palpitace).
**Stabilizátory nálady:** **lithium** má nejužší terapeutické okno v psychiatrii,
**0,6–1,2 mmol/l**, a proto se měří hladiny. Vylučuje se **výhradně ledvinami** a
nemetabolizuje se; hladinu zvyšují **nesteroidní antirevmatika, ACE inhibitory a
sartany, thiazidy a dehydratace**, protože ledvina si lithium při nedostatku
sodíku plete se sodíkem a šetří ho. Nežádoucí účinky: třes, polyurie a žízeň
(nefrogenní diabetes insipidus), **hypotyreóza**, přírůstek hmotnosti, akné;
je **teratogenní** (Ebsteinova anomálie). Otrava se projeví zvracením, ataxií,
zmateností a křečemi a léčí se hemodialýzou.
Dále se používají valproát, karbamazepin, **lamotrigin** (jediný s převahou
účinku na depresivní pól) a atypická antipsychotika. **Antidepresivum se u
bipolární poruchy podává jen se stabilizátorem**, jinak hrozí přesmyk do mánie.
""")

K("59", "Farmakoterapie Alzheimerovy choroby, nootropika", """
Alzheimerova nemoc je neurodegenerativní onemocnění s amyloidovými plaky a tau
patologií; nejdříve zanikají **cholinergní neurony v nucleus basalis Meynerti**,
odkud vychází cholinergní hypotéza. **Žádný z dostupných léků nemoc nezastaví**
— zpomalí zhoršování a zlepší denní fungování.
**Inhibitory acetylcholinesterázy** se používají v lehkém až středně těžkém
stadiu: **donepezil** (1× denně), **rivastigmin** (blokuje i
butyrylcholinesterázu, existuje jako náplast s lepší snášenlivostí) a
**galantamin**. Jejich nežádoucí účinky odpovídají mírnému SLUDGE — nevolnost,
průjem, hypersalivace, bradykardie, živé sny.
**Memantin** je antagonista **NMDA** receptoru (glutamátová hypotéza) pro středně
těžké až těžké stadium; lze jej kombinovat s inhibitorem cholinesterázy.
**Čemu se vyhnout:** anticholinergika (například oxybutynin — ruší účinek
inhibitoru cholinesterázy), benzodiazepiny a klasická antipsychotika, která u
demence zvyšují úmrtnost.
**Nová léčba:** monoklonální protilátky proti amyloidu (lekanemab, donanemab) s
rizikem mozkových otoků a mikrokrvácení [ověřit dle skript].
**Nootropika** (piracetam, ginkgo, vinpocetin) mají slabou až žádnou evidenci a
u prokázané demence léčbou nejsou.
""")

K("60", "Opium a jeho alkaloidy", """
**Opium** je zaschlá šťáva z nezralých makovic máku setého (*Papaver
somniferum*) a obsahuje dvě chemické skupiny alkaloidů.
**Fenanthrenové** — morfin, kodein, thebain — tlumí bolest a jsou návykové.
**Isochinolinové** — papaverin (spazmolytikum) a noskapin (antitusikum) —
analgetický účinek ani závislost nemají.
**Mechanismus:** receptory **μ, κ, δ** jsou spřaženy s Gi; snižují cAMP, otevírají
draslíkové a uzavírají vápníkové kanály, takže neuron hyperpolarizují a nevyšle
vzruch. Působí presynapticky i postsynapticky, míšně i supraspinálně.
**Účinky:** analgezie, euforie, sedace, antitusický účinek, **útlum dechového
centra** (snížení citlivosti k CO₂ — příčina smrti při předávkování), **mióza**,
**zácpa**, nauzea, uvolnění histaminu (svědění, hypotenze) a stah Oddiho svěrače.
**Tolerance** vzniká k analgezii, euforii, útlumu dechu i nauzee, ale **nikdy k
mióze a zácpě** — proto je špendlíková zornice diagnostická i u letitého
uživatele a k opioidu se rovnou nasazuje laxativum.
**Otrava:** kóma, útlum dechu a mióza. **Antidotem je naloxon**, který má kratší
poločas než morfin, a proto se musí opakovat.
**Kodein** je proléčivo aktivované CYP2D6 na morfin.
""")

K("61", "Deriváty a náhražky morfinu", """
Opioidy se dělí podle **síly** a podle **chování na receptoru**.
**Silné, plné agonisty μ:** **fentanyl** (asi stokrát účinnější než morfin,
náplasti; při rychlém i.v. podání rigidita hrudní stěny), sufentanil,
**remifentanil** (rozkládají ho esterázy, má kontextově necitlivý poločas),
oxykodon, hydromorfon, **metadon** (velmi dlouhý poločas, používá se k substituci,
prodlužuje QT) a **petidin**, jehož metabolit norpetidin dráždí CNS a vyvolává
křeče; s inhibitory MAO je kombinace smrtelná.
**Slabé:** kodein, dihydrokodein a **tramadol**, který kromě slabého působení na
μ receptor blokuje zpětné vychytávání noradrenalinu a serotoninu — odtud riziko
**serotoninového syndromu** a snížení prahu pro křeče.
**Parciální a smíšené:** **buprenorfin** má strop dechového útlumu, ale váže se
tak pevně, že jej naloxon obtížně vytlačí; nalbufin a pentazocin mohou u pacienta
na plném agonistovi vyvolat odvykací stav.
**Antagonisté:** naloxon i.v. u akutní otravy, naltrexon perorálně v prevenci
relapsu a **methylnaltrexon**, který neprochází do mozku a používá se na
opioidovou zácpu.
Podle **žebříčku WHO** se postupuje od neopioidního analgetika přes slabý opioid
k silnému; u chronické bolesti se dávkuje podle hodin, ne podle potřeby.
""")

K("62", "Eikosanoidy", """
**Eikosanoidy** jsou místní působky odvozené od **kyseliny arachidonové**, která
se uvolňuje z membránových fosfolipidů působením **fosfolipázy A₂**.
Kyselina arachidonová se dál metabolizuje dvěma větvemi. **Cyklooxygenázová
(COX)** větev tvoří prostaglandiny, **prostacyklin (PGI₂)** a **tromboxan
(TXA₂)**; **lipoxygenázová (LOX)** větev tvoří **leukotrieny**, které stahují
průdušky, zvyšují tvorbu hlenu a působí chemotakticky.
**Kortikoidy blokují fosfolipázu A₂**, tedy o patro výše, a vypnou proto **obě**
větve. **Nesteroidní antirevmatika blokují jen COX**, takže se kyselina
arachidonová „přelije" do lipoxygenázové větve — odtud **aspirinem indukované
astma** a Samterova trias (astma, nosní polypy, intolerance aspirinu).
**COX-1** je konstitutivní: ochranný hlen žaludku, tromboxan v trombocytech,
průtok ledvinou. **COX-2** je indukovatelná zánětem, ale nachází se i v endotelu
a ledvině, proto koxiby zvyšují kardiovaskulární riziko.
**Tromboxan a prostacyklin jsou protipóly** — TXA₂ z destiček sráží a stahuje
cévu, PGI₂ z endotelu působí opačně.
**Léčebně:** misoprostol, alprostadil, latanoprost, epoprostenol, dinoproston a
antileukotrien montelukast.
""")

K("63", "Analgetika-antipyretika", """
Analgetika-antipyretika tlumí bolest a horečku, ale **nemají významný
protizánětlivý účinek**.
**Paracetamol** působí převážně centrálně. Nedráždí žaludeční sliznici,
neovlivňuje srážení krve a je bezpečný v graviditě, u dětí, u astmatu a u vředové
choroby. Maximální denní dávka je **4 g**, u rizikových pacientů méně.
**Otrava paracetamolem:** za běžných okolností se 90 % konjuguje a asi 10 %
přechází přes CYP2E1 na toxický **NAPQI**, který zneškodní glutathion. Při
předávkování se konjugace nasytí, glutathion se vyčerpá a vzniká **jaterní
nekróza**. Alkoholik je ohrožen i běžnou dávkou, protože má indukovaný CYP2E1 a
nízké zásoby glutathionu. **Příznaky se objeví až za 1–3 dny**, proto se
rozhoduje podle hladiny v čase, nikoli podle stavu pacienta; **antidotem je
N-acetylcystein**, nejúčinnější do 8 hodin.
**Metamizol** má silný analgetický a **spazmolytický** účinek, hodí se u kolik;
rizikem je **agranulocytóza** a prudký pokles tlaku při rychlém nitrožilním
podání.
Dále se používá kyselina acetylsalicylová v analgetické dávce a kombinace s
kofeinem, který účinek zesiluje.
""")

K("64", "Nesteroidní antiflogistika", """
**Nesteroidní antirevmatika (NSA)** inhibují cyklooxygenázu a mají čtyři účinky:
protizánětlivý, analgetický, antipyretický a antiagregační.
**Neselektivní:** ibuprofen, diklofenak, **naproxen** (nejnižší kardiovaskulární
riziko), indometacin, ketoprofen, piroxikam a kyselina acetylsalicylová.
**Preferenční COX-2:** nimesulid, meloxikam. **Koxiby** (celekoxib, etorikoxib)
šetří žaludek, ale zvyšují kardiovaskulární riziko — rofekoxib byl proto stažen.
**Kyselina acetylsalicylová** jako jediná **ireverzibilně acetyluje COX**;
trombocyt nemá jádro a enzym si neobnoví, takže antiagregační účinek trvá 7–10
dní a stačí dávka 100 mg denně.
**Nežádoucí účinky plynou z blokády COX-1:** vřed a krvácení (vznikají i po
nitrožilním podání, prevencí je inhibitor protonové pumpy); v ledvině zrušení
prostaglandinové vazodilatace přívodné tepénky s rizikem akutního selhání u
dehydratovaného a seniora a analgetická nefropatie; retence sodíku, hypertenze;
**Reyeův syndrom** u dětí a **aspirinem indukované astma**.
**Interakce:** trojkombinace NSA + ACE inhibitor + diuretikum ohrožuje ledviny a
**ibuprofen ruší antiagregační účinek aspirinu**.
""")
