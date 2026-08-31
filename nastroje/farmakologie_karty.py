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
