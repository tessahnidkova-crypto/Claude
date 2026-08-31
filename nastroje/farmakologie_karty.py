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

K("65", "Farmakoterapie migrény", """
Migréna je **neurovaskulární onemocnění** s aktivací trigeminovaskulárního
systému a vyplavením **CGRP**; léčba se dělí na akutní a profylaktickou.
**Akutní léčba** má být zahájena co nejdříve. Podává se **NSA nebo paracetamol**
spolu s **metoklopramidem nebo domperidonem** — ty nepůsobí jen proti nevolnosti,
ale hlavně rozhýbou při záchvatu zastavený žaludek, takže se analgetikum vůbec
vstřebá.
**Triptany** (sumatriptan, eletriptan, zolmitriptan) jsou agonisté **5-HT1B/1D**:
stahují rozšířené mozkové cévy a tlumí uvolňování CGRP. Jsou kontraindikované u
ischemické choroby srdeční a nekontrolované hypertenze a nesmějí se kombinovat s
ergotaminem, který je pro riziko ergotismu obsoletní.
**Bolest hlavy z nadužívání léků** vzniká při užívání analgetik více než 10–15
dní v měsíci; řešením je vysazení, nikoli přidání dalšího léku.
**Profylaxe** se zahajuje při čtyřech a více záchvatech měsíčně: betablokátory
(metoprolol, propranolol), topiramát, valproát, amitriptylin, flunarizin,
kandesartan; u těžkých forem **monoklonální protilátky proti CGRP** a u chronické
migrény botulotoxin. Účinek se hodnotí až po 2–3 měsících.
""")

K("66", "Léčiva s pozitivně inotropním účinkem, digoxin", """
**Pozitivně inotropní** léčiva zvyšují sílu stahu srdce a všechna nakonec zvýší
nabídku vápníku v kardiomyocytu.
**Skupiny:** srdeční glykosidy (digoxin, digitoxin), sympatomimetika
(**dobutamin**), inhibitory fosfodiesterázy 3 (milrinon — „inodilatátor") a
senzitizér vápníku **levosimendan**.
**Digoxin blokuje Na⁺/K⁺-ATPázu:** uvnitř buňky přibude sodík, výměník Na⁺/Ca²⁺
přestane vyvážet vápník, jehož koncentrace stoupne a stah zesílí. Druhým účinkem
je **vagotonické zpomalení vedení v AV uzlu**.
**Indikace:** fibrilace síní s rychlou komorovou odpovědí a srdeční selhání se
systolickou dysfunkcí; **zlepší příznaky, ale neprodlouží život**. Vylučuje se
ledvinami (digitoxin játry), proto opatrně u seniorů.
**Toxicita:** úzké terapeutické okno, hladiny se měří. **Hypokalemie toxicitu
zvyšuje**, protože draslík a digoxin soutěží o stejné vazebné místo — a
hypokalemii způsobují diuretika, která pacient obvykle užívá. Projevy: nauzea a
zvracení, **žluté vidění (xantopsie)**, zmatenost a **arytmie** (bigeminie, AV
blokáda). Léčbou jsou **protilátky proti digoxinu (Fab)** a úprava kalia.
""")

K("67", "Antiarytmika", """
**Vaughanova–Williamsova klasifikace** řadí antiarytmika podle blokovaného
kanálu.
**I. třída — blokátory sodíkových kanálů:** IA chinidin, prokainamid, ajmalin
(prodlužují akční potenciál); **IB lidokain** a mexiletin (zkracují, používají se
u komorových arytmií při infarktu); **IC propafenon a flekainid**, které silně
zpomalují vedení a jsou kontraindikované u strukturálního postižení srdce —
studie CAST ukázala, že po infarktu sice potlačí extrasystoly, ale **zvýší
úmrtnost**.
**II. třída — betablokátory:** jediná skupina, která prokazatelně snižuje
úmrtnost.
**III. třída — blokátory draslíkových kanálů: amiodaron**, sotalol, dronedaron;
prodlužují QT a hrozí *torsades de pointes*. Amiodaron je nejúčinnější, ale
nejtoxičtější: obsahuje jód (tyreopatie), způsobuje plicní fibrózu, usazeniny v
rohovce, fotosenzitivitu a hepatotoxicitu, a poločas má týdny až měsíce.
**IV. třída — blokátory kalciových kanálů:** verapamil a diltiazem; nesmějí se
kombinovat s betablokátorem.
**Mimo klasifikaci:** **adenosin** (poločas několik sekund, ukončí paroxysmální
supraventrikulární tachykardii), digoxin, **magnezium** u torsades, atropin,
ivabradin. Každé antiarytmikum může arytmii také vyvolat.
""")

K("68", "ACE inhibitory a antagonisté angiotensinu", """
**Systém renin-angiotensin-aldosteron:** renin štěpí angiotensinogen na
angiotensin I, **ACE** jej mění na **angiotensin II**, který přes receptor
**AT1** stahuje cévy, uvolňuje aldosteron, podporuje remodelaci myokardu, žízeň
a výdej ADH.
**ACE je zároveň kináza II**, která odbourává **bradykinin**. Proto se při
podávání ACE inhibitorů bradykinin hromadí a vzniká **suchý dráždivý kašel** a
vzácně **angioedém**. **Sartany** blokují až receptor AT1, bradykinin
neovlivňují, a proto kašel nezpůsobují.
**Zástupci:** ramipril, perindopril, enalapril, kaptopril (**-pril**); losartan,
valsartan, telmisartan, kandesartan (**-sartan**).
**Indikace:** hypertenze, srdeční selhání, stav po infarktu myokardu a
**diabetická či proteinurická nefropatie**. **Renoprotekce** spočívá v uvolnění
odvodné tepénky glomerulu, čímž klesne nitroglomerulární tlak; mírný vzestup
kreatininu na začátku léčby je proto očekávaný.
**Nežádoucí účinky a kontraindikace:** hyperkalemie, hypotenze po první dávce,
zhoršení funkce ledvin, **absolutní kontraindikace v graviditě** a při
oboustranné stenóze renálních tepen. ACE inhibitor a sartan se nekombinují.
Kombinace **ARNI** (sakubitril + valsartan) je dnešním standardem u srdečního
selhání.
""")

K("69", "Diuretika", """
Diuretika se dělí podle **místa účinku v nefronu**, z něhož plyne jejich síla i
minerálové poruchy.
**Proximální tubulus:** **acetazolamid** (inhibitor karboanhydrázy) u glaukomu a
výškové nemoci, způsobuje metabolickou acidózu; osmotický **mannitol** u
mozkového edému.
**Vzestupné raménko Henleovy kličky: furosemid** blokuje kotransportér NKCC2. Je
**nejsilnější**, protože klička vstřebává největší podíl sodíku, a **účinkuje i
při selhání ledvin**. **Vyplavuje vápník**, způsobuje hypokalemii,
hypomagnezemii a je ototoxický; nitrožilně působí nejprve žilní dilatací, což se
využívá u plicního edému.
**Distální tubulus: thiazidy** (hydrochlorothiazid, indapamid, chlortalidon)
blokují kotransportér NCC. **Vápník naopak šetří.** Nefungují při těžkém selhání
ledvin a mají metabolické nežádoucí účinky — hyperurikemii (dna), hyperglykemii,
hyperlipidemii a hyponatremii.
**Sběrací kanálek — kalium šetřící:** antagonisté aldosteronu **spironolakton**
(zlepšuje přežití u srdečního selhání, ale způsobuje gynekomastii) a eplerenon;
blokátory sodíkového kanálu amilorid a triamteren.
Všechna kromě poslední skupiny **ztrácejí draslík**, což zvyšuje toxicitu
digoxinu.
""")

K("70", "Blokátory kalciových kanálů", """
Blokují **kalciové kanály typu L** v hladké svalovině cév a v myokardu; podle
převažujícího cíle se dělí na dvě skupiny.
**Dihydropyridiny** (amlodipin, nifedipin, nitrendipin, lerkanidipin, felodipin —
koncovka **-dipin**) působí především na **cévy**. Vyvolají vazodilataci a
snížení tlaku; nežádoucí jsou **otoky kotníků** (nejde o retenci tekutin, ale o
nerovnováhu mezi dilatovanou tepénkou a nedilatovanou žilkou, proto na ně
diuretikum nezabere), návaly, bolest hlavy, reflexní tachykardie a **hyperplazie
gingivy**.
**Verapamil** (fenylalkylamin) a **diltiazem** (**benzothiazepin**) působí
především na **srdce**: zpomalují frekvenci, snižují kontraktilitu a zpomalují
vedení v AV uzlu; verapamil navíc způsobuje zácpu. **Nesmějí se kombinovat s
betablokátory** (riziko AV blokády) a jsou **kontraindikované u srdečního
selhání**.
**Indikace:** hypertenze (zejména dihydropyridiny, vhodné u seniorů), angina
pectoris včetně vazospastické, a u verapamilu i diltiazemu supraventrikulární
arytmie a fibrilace síní — zejména tam, kde nelze podat betablokátor.
**Grapefruit** inhibuje CYP3A4 a zvyšuje jejich hladinu.
""")

K("71", "Nitrity a nitráty", """
**Nitráty jsou donory oxidu dusnatého (NO)**. NO aktivuje guanylátcyklázu,
zvýší cGMP a uvolní hladkou svalovinu — **především v žilním řečišti**. Krev se
zadrží v žilách, klesne **předtížení**, srdce se méně plní a **potřebuje méně
kyslíku**; teprve druhotně se rozšíří věnčité tepny a odezní spazmus.
**Zástupci a formy:** **nitroglycerin** sublingválně nebo ve spreji (**nesmí se
polykat**, zničil by ho first-pass efekt), isosorbid dinitrát a mononitrát
(mononitrát first-pass nemá), molsidomin a nitroglycerin nitrožilně u akutních
stavů.
**Tolerance** je hlavním praktickým problémem: při nepřetržité expozici účinek
během několika dní vymizí, a proto se dodržuje **nitrátový interval 8–12 hodin**
denně, obvykle přes noc (u nočních obtíží naopak přes den).
**Nežádoucí účinky:** bolest hlavy (během dnů odezní), návaly, hypotenze a
reflexní tachykardie.
**Absolutní kontraindikací jsou inhibitory fosfodiesterázy 5** (sildenafil,
tadalafil) — obě skupiny zvyšují cGMP, účinek se sečte a nastane nezvratný pokles
tlaku. Na jejich užívání je nutné se aktivně ptát.
Nitráty jsou léčbou symptomatickou, prognózu nezlepšují.
""")

K("72", "Farmakoterapie srdečního selhání", """
U srdečního selhání je zásadní odlišit léčbu, která **prodlužuje život**, od
léčby, která pouze **ulevuje od příznaků**.
**Čtyři pilíře** u selhání se sníženou ejekční frakcí: **ACE inhibitor nebo
sartan** (dnes nejlépe **ARNI** — sakubitril s valsartanem), **betablokátor**
(pouze bisoprolol, metoprolol ZOK, karvedilol a nebivolol), **antagonista
aldosteronu** (spironolakton, eplerenon) a **gliflozin** (dapagliflozin,
empagliflozin), který působí i u nediabetika.
**Symptomatická léčba:** diuretika (furosemid), digoxin a ivabradin. Zlepší
příznaky a sníží hospitalizace, ale prognózu nemění.
**Proč se tlumí srdce, které nestačí:** chronická aktivace sympatiku a systému
RAAS je zpočátku kompenzací, ale dlouhodobě vede k remodelaci a poškození
myokardu. Léčba tuto nadměrnou podporu odstraňuje — proto se betablokátor nasazuje
až u stabilizovaného pacienta v nízké dávce a titruje se týdny, přičemž stav se
může přechodně zhoršit.
**Kontraindikované jsou** nesteroidní antirevmatika (retence sodíku, zhoršení
funkce ledvin), verapamil a diltiazem (negativně inotropní) a glitazony (retence
tekutin).
""")

K("73", "Farmakoterapie ischemické choroby srdeční", """
Ischemická choroba srdeční vzniká **nepoměrem mezi nabídkou a spotřebou kyslíku
v myokardu**. Léčba se dělí na chronickou a akutní.
**U chronické formy zlepšují prognózu** antiagregancia (kyselina
acetylsalicylová), **statin** ve vysoké dávce (nejen kvůli cholesterolu, ale pro
**stabilizaci plátu**, protože infarkt způsobí prasklý plát), **ACE inhibitor** a
**betablokátor**.
**Pouze od příznaků ulevují** nitráty, **ivabradin** (blokuje kanál If v
sinusovém uzlu, zpomalí tep bez vlivu na kontraktilitu a tlak), trimetazidin,
ranolazin a blokátory kalciových kanálů, které jsou volbou u vazospastické
anginy. Betablokátor uleví tím, že zpomalí tep, prodlouží diastolu a zlepší
plnění věnčitých tepen, k němuž dochází právě v diastole.
**Akutní koronární syndrom:** rozhoduje čas a otevření tepny perkutánní koronární
intervencí. Farmakoterapie ji doprovází: kyselina acetylsalicylová s inhibitorem
P2Y12 (tikagrelor, prasugrel), antikoagulancium, morfin, kyslík při desaturaci,
nitrát, betablokátor a statin. Trombolýza se podá jen tam, kde katetrizace není
dostupná.
**Duální antiagregace po zavedení stentu** trvá obvykle 12 měsíců a nesmí se
svévolně vysadit — hrozí trombóza stentu.
""")

K("74", "Antihypertenziva", """
Léčba hypertenze stojí na **pěti základních třídách**: ACE inhibitory a sartany,
blokátory kalciových kanálů (dihydropyridiny), **thiazidová diuretika**,
betablokátory a u rezistentní hypertenze **spironolakton**. Doplňují je centrálně
působící α2 agonisté (methyldopa, klonidin), α1-blokátory, přímé vazodilatátory
(hydralazin, minoxidil) a urapidil.
**Zásadou je kombinovat nízké dávky několika léčiv** raději než vyhnat jedno do
maxima — účinek se sečte, nežádoucí účinky ne. Fixní kombinace v jedné tabletě
zlepšuje adherenci, protože hypertenze nebolí.
**Volba podle pacienta:** diabetik nebo proteinurie → ACE inhibitor či sartan; po
infarktu → betablokátor s ACE inhibitorem; srdeční selhání → čtyři pilíře;
starší pacient s izolovanou systolickou hypertenzí → blokátor kalciových kanálů
nebo thiazid. **U dny se nepodává thiazid, u astmatu betablokátor.**
**V graviditě** jsou povolené **methyldopa, labetalol a nifedipin**, zatímco ACE
inhibitory a sartany jsou absolutně kontraindikované.
**Hypertenzní krize** se nesmí srážet příliš rychle. U rezistentní hypertenze se
nejdřív vyloučí nespolupráce a sekundární příčina — nejčastěji **primární
hyperaldosteronismus**, dále onemocnění ledvin či léky (NSA, kortikoidy,
antikoncepce).
""")

K("75", "Farmakoterapie aterosklerózy, hyperlipidemie", """
**Statiny** (atorvastatin, rosuvastatin, simvastatin) inhibují **HMG-CoA
reduktázu**, klíčový enzym tvorby cholesterolu v játrech. Játra na to reagují
zvýšením počtu **LDL receptorů**, kterými vytáhnou cholesterol z krve. Kromě toho
mají pleiotropní účinek — tlumí zánět ve stěně cévy a **stabilizují
aterosklerotický plát**, což je klinicky podstatnější než samotné číslo v odběru.
**Nežádoucí účinky:** svalové obtíže od myalgie po vzácnou **rabdomyolýzu**
(bolest svalů, tmavá moč, vysoká kreatinkináza), zvýšení jaterních testů a mírné
zvýšení rizika diabetu. **Riziko myopatie stoupá s inhibitory CYP3A4** —
makrolidy (klarithromycin), azolová antimykotika, verapamil, cyklosporin,
grapefruit — a při kombinaci s fibrátem.
**Další hypolipidemika:** **ezetimib** blokuje střevní vstřebávání cholesterolu
(přenašeč NPC1L1); **inhibitory PCSK9** (evolokumab, alirokumab) jsou injekční
protilátky s velmi silným účinkem pro rodinnou hypercholesterolemii a
netolerující pacienty; **fibráty** (fenofibrát) přes PPAR-α snižují především
triacylglyceroly; dále pryskyřice, kyselina nikotinová a omega-3 mastné kyseliny.
Cílová hodnota LDL se řídí celkovým kardiovaskulárním rizikem.
""")

K("76", "Parenterální antikoagulancia", """
**Heparin sám o sobě neúčinkuje** — asi tisíckrát zesílí přirozený inhibitor
**antitrombin III**. Proto při vrozeném deficitu antitrombinu nefunguje.
**Nefrakcionovaný heparin** má dlouhý řetězec, inhibuje **faktor IIa i Xa**,
monitoruje se pomocí **aPTT**, má krátký poločas a **antidotem je protamin
sulfát**; hodí se při těžkém selhání ledvin a tam, kde je třeba účinek rychle
ukončit.
**Nízkomolekulární hepariny** (enoxaparin, nadroparin) působí především na
**faktor Xa**, podávají se podkožně jednou až dvakrát denně, rutinní monitorace
není nutná (jen anti-Xa aktivita) a protamin je zruší jen částečně.
**Fondaparinux** je syntetický pentasacharid inhibující výhradně faktor Xa a
**nevyvolává HIT**.
**Heparinem indukovaná trombocytopenie (HIT)** je paradoxní komplikace:
protilátky proti komplexu heparinu s destičkovým faktorem 4 destičky nejen
ubírají, ale i **aktivují**, takže pacient má málo destiček a přitom trombózy.
Heparin se okamžitě vysadí a nahradí argatrobanem, bivalirudinem nebo
fondaparinuxem; **destičky se nepodávají**.
Hepariny **neprocházejí placentou**, a jsou proto antikoagulanciem volby v
graviditě.
""")

K("77", "Perorální antikoagulancia", """
**Warfarin** je antagonista vitaminu K: blokuje γ-karboxylaci koagulačních
faktorů **II, VII, IX a X**, ale i přirozených inhibitorů **proteinu C a S**.
Protože protein C má nejkratší poločas, je pacient v prvních dnech přechodně
**protrombogenní** — proto se léčba **překrývá heparinem**, dokud INR nedosáhne
cíle. Účinek nastupuje za 3–5 dní, monitoruje se **INR** (obvykle 2–3),
antidotem je **vitamin K**, plazma nebo koncentrát protrombinového komplexu.
Warfarin je **teratogenní**.
**Interakce** jsou rozsáhlé: vitamin K v listové zelenině (zásadou je jíst jí
stále stejně), antibiotika ničící střevní bakterie produkující vitamin K,
amiodaron a azolová antimykotika zvyšují INR, rifampicin, karbamazepin a
třezalka je snižují; NSA zvyšují riziko krvácení i beze změny INR.
**Přímá perorální antikoagulancia (DOAC):** **dabigatran** je přímý inhibitor
trombinu s antidotem **idarucizumabem**; **rivaroxaban, apixaban a edoxaban**
inhibují faktor Xa a antidotem je andexanet alfa. Výhodou je fixní dávka bez
monitorace, méně interakcí a nižší riziko krvácení do mozku; **nesmějí se použít
u mechanické chlopně a u těžké renální insuficience**.
""")

K("78", "Fibrinolytika, trombolytika, hemostatika", """
**Trombolytika** aktivují plazminogen na **plazmin**, který rozpouští fibrin.
Patří sem rekombinantní **alteplasa** a tenektaplasa a starší **streptokináza**,
kterou nelze podat opakovaně, protože jako bakteriální bílkovina vyvolá tvorbu
protilátek.
**Indikace:** infarkt myokardu s elevacemi ST tam, kde není dostupná katetrizace,
masivní plicní embolie a **ischemická cévní mozková příhoda do 4,5 hodiny**.
**Kontraindikace:** aktivní krvácení, krvácení do mozku v anamnéze, nedávná
operace nebo úraz, nekontrolovaná hypertenze, disekce aorty.
**Hemostatika** působí opačně. **Vitamin K** ruší účinek warfarinu. **Kyselina
tranexamová** je antifibrinolytikum — blokuje vazbu plazminogenu na fibrin a
používá se u silného krvácení a menoragie; je kontraindikovaná při aktivní
trombóze. **Desmopresin** vyplaví z endotelu **von Willebrandův faktor a faktor
VIII**, a uplatní se proto u mírné hemofilie A a von Willebrandovy choroby.
Dále etamsylát, koncentráty koagulačních faktorů a rekombinantní faktor VIIa.
**Místně** se používá oxidovaná celulóza, kolagenová houbička a fibrinové lepidlo.
**Hemofilie A je vrozený, X-vázaný deficit faktoru VIII.**
""")

K("79", "Antiagregancia", """
**V tepně** vzniká sraženina převážně z **destiček**, proto se používají
antiagregancia; **v žíle** převažuje fibrin a nasazují se antikoagulancia. Toto
rozlišení určuje indikace.
**Kyselina acetylsalicylová** v dávce 75–100 mg **ireverzibilně acetyluje COX-1**
v trombocytu. Ten nemá jádro a enzym si neobnoví, takže účinek trvá celý život
destičky, tedy 7–10 dní. Nízká dávka zasáhne destičkovou COX-1 už při průchodu
játry, zatímco vyšší dávka by potlačila i ochranný prostacyklin v endotelu.
**Inhibitory receptoru P2Y12 pro ADP:** **klopidogrel** je proléčivo aktivované
CYP2C19 — pomalí metabolizátoři z něj nemají užitek a omeprazol jeho účinek
snižuje; **prasugrel a tikagrelor** jsou účinnější, tikagrelor navíc reverzibilní
a není proléčivem.
**Inhibitory GPIIb/IIIa** (abciximab, eptifibatid) blokují poslední společný krok
agregace, podávají se jen nitrožilně v katetrizační laboratoři.
**Dipyridamol** se kombinuje s aspirinem po cévní mozkové příhodě, **cilostazol**
se používá u ischemické choroby dolních končetin.
Hlavním nežádoucím účinkem je krvácení, u aspirinu navíc gastropatie.
""")

K("80", "Inzulin, jeho analoga a glukagon", """
Cílem inzulinoterapie je napodobit fyziologii — stálou **bazální** hladinu a
vzestup k jídlu (**bolus**).
**Rychlá analoga** (lispro, aspart, glulisin) nastupují asi za 15 minut a
podávají se těsně před jídlem. **Krátce působící humánní inzulin** vyžaduje
odstup asi 30 minut. **Střednědobý NPH** slouží k překlenutí, **dlouhá analoga**
(glargin, detemir, degludek) nemají výrazný vrchol a kryjí bazální potřebu;
existují i premixované směsi.
**Hlavním nebezpečím je hypoglykemie:** pocení, třes, bušení srdce, hlad, poté
zmatenost, bezvědomí a křeče. **Betablokátor maskuje třes a palpitace**
zprostředkované sympatikem, ale **pocení zůstane**, protože je cholinergní, a
bývá jediným varováním. Léčbou je cukr ústy, při bezvědomí glukóza nitrožilně
nebo **glukagon** i.m. či nosním sprejem.
**Glukagon** je zároveň **antidotem předávkování betablokátory**, protože zvyšuje
cAMP v myokardu jinou cestou než přes β receptor.
Dalšími nežádoucími účinky jsou přírůstek hmotnosti a **lipodystrofie**, které
předchází střídání míst vpichu. Rozlišuje se Somogyiho fenomén (ranní
hyperglykemie po noční hypoglykemii) a dawn fenomén.
""")

K("81", "Perorální antidiabetika", """
U diabetu 2. typu stojí problém na **inzulinové rezistenci** a postupném
selhávání beta-buněk. Léčiva se dnes nevybírají jen podle glykemie, ale i podle
ochrany srdce a ledvin.
**Metformin** je lékem první volby: snižuje jaterní glukoneogenezi a zvyšuje
citlivost k inzulinu. **Sám hypoglykemii nevyvolá**, protože nenutí slinivku
vylučovat inzulin. Vysazuje se před podáním jodové kontrastní látky a při
akutním stavu pro riziko **laktátové acidózy**; dlouhodobě může vést k deficitu
vitaminu B12.
**Sulfonylurea** (glimepirid, gliklazid) uzavírá KATP kanál a vyplaví inzulin
**bez ohledu na glykemii**, proto jako jediná z tablet způsobuje těžkou a
protrahovanou **hypoglykemii** a přírůstek hmotnosti; podobně glinidy.
**Gliptiny** (sitagliptin) jsou metabolicky neutrální. **Agonisté GLP-1**
(liraglutid, semaglutid) vedou k hubnutí a chrání srdce, podávají se injekčně a
zpomalují vyprazdňování žaludku. **Glifloziny** (dapagliflozin, empagliflozin)
blokují SGLT2, chrání srdce i ledviny, ale způsobují glykosurii s rizikem
mykotických infekcí a **euglykemické ketoacidózy**.
Dále pioglitazon (retence tekutin, srdeční selhání) a akarbóza.
""")

K("82", "Principy antibiotické terapie", """
Antibiotická léčba stojí na **selektivní toxicitě** — zasáhne strukturu, kterou
má bakterie a člověk ne.
**Cíle v bakteriální buňce:** **buněčná stěna** z peptidoglykanu (betalaktamy,
glykopeptidy), **cytoplazmatická membrána** (polymyxiny, daptomycin),
**ribozom 70S** — podjednotka 30S (aminoglykosidy, tetracykliny) a 50S
(makrolidy, linkosamidy, amfenikoly), **nukleové kyseliny** (chinolony blokují
topoizomerázu, rifampicin RNA-polymerázu, metronidazol poškozuje DNA anaerobů) a
**syntéza kyseliny listové** (sulfonamidy s trimethoprimem).
**Pojmy:** baktericidní × bakteriostatické, úzké × široké spektrum, empirická ×
cílená léčba, **MIC**. Podle způsobu zabíjení se dávkuje: **koncentračně závislá**
antibiotika (aminoglykosidy, chinolony) se podávají ve vysoké dávce jednou
denně, **časově závislá** (betalaktamy) častěji, protože rozhoduje doba nad MIC.
**Mechanismy rezistence:** produkce **betalaktamáz**, změna cílové struktury
(MRSA má pozměněný PBP2a), **efluxní pumpy** a snížená propustnost stěny.
Rezistence roste s používáním, proto se antibiotika nenasazují na virózy a
neslouží jako náhrada chirurgického ošetření ložiska.
""")

K("83", "Peniciliny, inhibitory betalaktamáz", """
**Peniciliny** jsou betalaktamová antibiotika, která blokují transpeptidázu
(protein vázající penicilin) a tím **syntézu buněčné stěny**. Jsou **baktericidní
a působí jen na dělící se bakterie**. Protože člověk buněčnou stěnu nemá, jsou
velmi bezpečné a hlavním rizikem je alergie, nikoli toxicita.
**Přirozené:** penicilin G (i.v., i.m.), **penicilin V** perorálně (podává se
nalačno) a depotní benzathin-penicilin. **Protistafylokokové:** oxacilin, odolný
vůči stafylokokové betalaktamáze. **Aminopeniciliny:** ampicilin a **amoxicilin**
se širším spektrem včetně některých gramnegativních bakterií.
**Ureidopeniciliny:** piperacilin s účinkem na *Pseudomonas*.
**Inhibitory betalaktamáz** (kyselina klavulanová, sulbaktam, tazobaktam) samy
prakticky neúčinkují — obětují se enzymu a rozšíří spektrum na producenty
betalaktamáz.
**Nežádoucí účinky:** alergie (skutečná IgE reakce je vzácnější, než pacienti
uvádějí; při anafylaxi v anamnéze se betalaktamům vyhýbáme a volíme klindamycin
nebo makrolid), průjem a infekce *Clostridioides difficile*, ve vysokých dávkách
křeče. **Ampicilinový exantém u infekční mononukleózy není alergie.**
""")

K("84", "Cefalosporiny, karbapenemy, monobaktamy", """
Všechny tři skupiny jsou **betalaktamy** se stejným mechanismem jako peniciliny.
**Cefalosporiny** se dělí do generací a platí pravidlo: **čím vyšší generace, tím
méně grampozitivních a více gramnegativních bakterií**. I. generace (cefazolin,
cefalexin) se používá k chirurgické profylaxi; II. (cefuroxim) pokrývá i
*Haemophilus*; III. (**ceftriaxon**, cefotaxim) proniká do centrálního nervového
systému, a hodí se proto u meningitid, ceftazidim navíc na *Pseudomonas*; IV.
(cefepim) je široká, nemocniční; V. (ceftarolin) jako jediná působí i na **MRSA**.
**Žádný cefalosporin nepůsobí na enterokoky ani na atypické patogeny.**
**Karbapenemy** (meropenem, imipenem s cilastatinem, ertapenem) mají nejširší
spektrum, a proto se drží v **rezervě** pro těžké a multirezistentní infekce.
Imipenem se musí kombinovat s cilastatinem, aby jej nerozložil ledvinný enzym, a
snižuje práh pro křeče; ertapenem nepůsobí na *Pseudomonas*.
**Monobaktam aztreonam** působí jen na gramnegativní bakterie, ale je natolik
strukturálně odlišný, že jej lze podat i při alergii na penicilin.
Nežádoucí účinky jsou společné: alergie, průjem a **klostridiová kolitida**.
""")

K("85", "Aminoglykosidy, chinolony", """
Obě skupiny jsou **baktericidní a koncentračně závislé**, proto se dávkují ve
vysoké dávce jednou denně.
**Aminoglykosidy** (gentamicin, amikacin, tobramycin, streptomycin) blokují
**30S podjednotku ribozomu**, ale na rozdíl od ostatních inhibitorů proteosyntézy
jsou **baktericidní**. Nevstřebávají se ze střeva, podávají se jen parenterálně a
nepůsobí na anaeroby, protože jejich vstup do buňky vyžaduje kyslík. Se
**betalaktamy působí synergicky**. Toxicita je typická: **nefrotoxicita**
(obvykle vratná) a **ototoxicita** postihující sluch i rovnováhu, která bývá
**trvalá** — proto se sledují plazmatické hladiny. Dávkování jednou denně navíc
chrání ledvinu.
**Chinolony** (ciprofloxacin, ofloxacin, levofloxacin, moxifloxacin) inhibují
**topoizomerázu II, tedy DNA-gyrázu, a topoizomerázu IV**. Mají široké spektrum
a dobrou tkáňovou penetraci. Nežádoucí účinky: **zánět a ruptura šlach** (typicky
Achillovy, zvláště u seniorů a při současné kortikoterapii), **kontraindikace u
dětí a v graviditě** pro poškození chrupavek, prodloužení QT, fotosenzitivita,
neuropsychické projevy a průjem po *C. difficile*. **Chelatují se s vápníkem,
hořčíkem a železem** — nesmějí se zapíjet mlékem ani brát s antacidy.
""")

K("86", "Linkosamidy, glykopeptidy, polymyxiny", """
**Klindamycin** (linkosamid) blokuje **50S podjednotku ribozomu** a je
bakteriostatický. Působí na grampozitivní koky a především na **anaeroby** a má
**vynikající průnik do kosti**, proto se používá u abscesů, osteomyelitidy a jako
alternativa při alergii na penicilin. Hlavním rizikem je **pseudomembranózní
kolitida vyvolaná *Clostridioides difficile***, která se projeví vodnatými
průjmy během léčby i po ní a léčí se **perorálním vankomycinem** nebo
fidaxomicinem; léky tlumící střevní motilitu jsou kontraindikované.
**Glykopeptidy** (vankomycin, teikoplanin) blokují syntézu buněčné stěny na
**jiném místě než betalaktamy**, takže je betalaktamázy neovlivní. Působí pouze
na **grampozitivní** bakterie a jsou lékem volby u **MRSA**. Perorálně se
nevstřebávají — právě proto se tak podávají u klostridiové kolitidy. Při rychlé
infuzi vzniká **„red man syndrome"**, histaminová reakce, která není alergií;
dále hrozí nefrotoxicita a ototoxicita.
**Polymyxiny** (kolistin) narušují cytoplazmatickou membránu jako detergent,
slouží jako rezerva na multirezistentní gramnegativní bakterie a jsou výrazně
nefrotoxické a neurotoxické.
""")

K("87", "Tetracykliny, amfenikoly", """
**Tetracykliny** (doxycyklin, minocyklin, tetracyklin) jsou širokospektrá
**bakteriostatická** antibiotika, která blokují **30S podjednotku ribozomu** —
nikoli buněčnou stěnu. Spektrum zahrnuje i **atypické patogeny**: chlamydie,
mykoplazmata, borrelie a rickettsie, proto je doxycyklin lékem volby u lymeské
boreliózy. Doxycyklin má lepší vstřebávání, delší poločas a lze jej podat i při
renální insuficienci.
**Nežádoucí účinky:** vážou se na **vápník** a ukládají do rostoucí kosti a zubu,
kde způsobí **nevratné šedohnědé zbarvení a hypoplazii skloviny** — proto jsou
kontraindikované **do 8 let věku, v graviditě a při kojení**. Dále **chelatace**
s vápníkem, hořčíkem a železem (nezapíjet mlékem, neužívat s antacidy),
fotosenzitivita a ezofagitida, které předchází zapití velkým množstvím vody.
Rezistence je dnes rozsáhlá.
**Amfenikoly — chloramfenikol** blokuje **50S podjednotku**. Systémově se
prakticky nepoužívá pro **aplastickou anemii**, která je idiosynkratická a
nezávislá na dávce, a pro **gray baby syndrom** u novorozence s nezralou
glukuronidací. Zůstal v očních kapkách a mastech.
""")

K("88", "Makrolidy", """
**Makrolidy** blokují **50S podjednotku ribozomu** a jsou bakteriostatické.
Pokrývají **atypické patogeny** — mykoplazmata, chlamydie, legionelu, původce
černého kašle — a jsou **alternativou při alergii na penicilin**.
**Zástupci:** erythromycin (nejstarší, špatně snášený), **klarithromycin**,
**azithromycin** a spiramycin.
**Nejvýznamnějším problémem jsou lékové interakce.** Erythromycin a
klarithromycin jsou **silné inhibitory CYP3A4**, a proto zvyšují hladiny statinů
(riziko rabdomyolýzy), warfarinu (krvácení), cyklosporinu, karbamazepinu a
některých blokátorů kalciových kanálů. **Azithromycin CYP3A4 prakticky
neinhibuje**, a je tedy volbou u polymorbidního pacienta. Azithromycin má navíc
velmi dlouhý tkáňový poločas — třídenní kúra působí ještě řadu dní po poslední
dávce.
**Další nežádoucí účinky:** **prodloužení QT**, zvláště v kombinaci s dalšími
léčivy se stejným efektem (antipsychotika, chinolony, ondansetron), a
gastrointestinální nesnášenlivost. Erythromycin dráždí žaludek přes
**motilinový receptor** — této vlastnosti se využívá, když se podává jako
prokinetikum u gastroparézy.
""")

K("89", "Chemoterapeutika močových a střevních infekcí", """
Jde o léčiva, která se **koncentrují v místě infekce** — v moči nebo ve střevním
lumen — a systémově působí málo, což omezuje nežádoucí účinky.
**Močové cesty: nitrofurantoin** se aktivuje bakteriálními nitroreduktázami na
radikály poškozující DNA; má **baktericidní účinek jen v moči**, proto se hodí
na nekomplikovanou cystitidu, ale **nikdy na pyelonefritidu** (netvoří tkáňové
hladiny). Kontraindikován je při **renální insuficienci** (nedostane se do moči)
a v posledním trimestru gravidity; dlouhodobě hrozí plicní fibróza a
polyneuropatie. **Fosfomycin** blokuje ranou fázi syntézy peptidoglykanu a
podává se jako **jednorázová dávka 3 g**. Používají se dále
**kotrimoxazol** a **chinolony** (u komplikovaných infekcí).
**Střevní infekce: rifaximin** je nevstřebatelný derivát rifamycinu — působí
v lumen, užívá se u cestovatelského průjmu a v prevenci **jaterní encefalopatie**
(snižuje střevní produkci amoniaku). **Nifuroxazid** je střevní nitrofuran.
**Vankomycin perorálně** se nevstřebává a je léčbou **klostridiové kolitidy**,
stejně jako **fidaxomicin**. **Metronidazol** pokrývá anaeroby a améby.
""")

K("90", "Antiparazitika", """
**Antiparazitika** se dělí podle cílového parazita na antiprotozoika,
antihelmintika a ektoparazitika; většina zasahuje **struktury, které savčí
buňka nemá** — mikrotubuly červa, jeho neuromuskulární přenos nebo
anaerobní metabolismus prvoka.
**Antiprotozoika: metronidazol** (a tinidazol) se aktivuje v anaerobním
prostředí na radikály štěpící DNA — účinkuje na **trichomonádu, lamblie,
améby** a anaerobní bakterie; má **disulfiramový efekt s alkoholem** a kovovou
pachuť. **Antimalarika:** chlorochin, **artemisininové kombinace (ACT)** jako
lék volby u falciparové malárie, atovakvon/proguanil a doxycyklin v profylaxi,
**primachin** na jaterní hypnozoity (kontraindikace při **deficitu G6PD** —
hemolýza). Toxoplazmóza: pyrimethamin se sulfadiazinem a kyselinou listovou.
**Antihelmintika: albendazol a mebendazol** vážou **β-tubulin** červa a blokují
příjem glukózy — široké spektrum hlístic. **Praziquantel** zvyšuje propustnost
membrány pro vápník (motolice, tasemnice). **Ivermektin** otevírá
glutamátem řízené chloridové kanály.
**Ektoparazitika:** permethrin a ivermektin na svrab a veš.
""")

K("91", "Antituberkulotika a antileprotika", """
**Tuberkulóza se nikdy neléčí jedním lékem** — mykobakterie se dělí pomalu,
tvoří dormantní populace a rychle vytvoří rezistenci; proto vždy
**kombinace nejméně čtyř léčiv** a dlouhé podávání pod přímým dohledem (DOT).
**Standardní režim: 2 měsíce HRZE + 4 měsíce HR.**
**Izoniazid (H)** blokuje syntézu **kyseliny mykolové**; nežádoucí je
**periferní neuropatie** (prevence **pyridoxinem, vitamin B6**) a
hepatotoxicita. **Rifampicin (R)** inhibuje bakteriální **RNA-polymerázu**;
je **silným induktorem CYP450** — snižuje účinek kontraceptiv, warfarinu,
antiretrovirotik — a **barví moč, slzy a pot oranžově** (varovat pacienta,
barví kontaktní čočky). **Pyrazinamid (Z)** působí v kyselém prostředí
makrofágu, zvyšuje kyselinu močovou a je hepatotoxický. **Etambutol (E)**
blokuje arabinosyltransferázu a způsobuje **retrobulbární neuritidu** —
porucha barvocitu a ostrosti, nutná oční kontrola.
**Rezervní:** streptomycin, fluorochinolony, bedachilin, linezolid.
**Lepra:** dapson + rifampicin + klofazimin, léčba trvá roky.
""")

K("92", "Antimykotika", """
**Antimykotika** cílí na **ergosterol** — sterol houbové membrány, který
lidská buňka nemá (má cholesterol) — nebo na buněčnou stěnu z glukanu.
**Azoly** (flukonazol, itrakonazol, vorikonazol, posakonazol; lokálně
klotrimazol, mikonazol) inhibují **14-α-demetylázu**, tedy syntézu ergosterolu.
Jsou fungistatické a jejich hlavním rizikem jsou **interakce přes CYP450** —
inhibují CYP3A4, a tím zvyšují hladiny statinů, warfarinu, cyklosporinu.
**Polyeny — amfotericin B** se váže přímo na ergosterol a **děrují membránu**;
je fungicidní, vyhrazený pro těžké systémové mykózy, silně **nefrotoxický**
a působí horečku a třesavku při infuzi (lipozomální forma je snášena lépe).
**Nystatin** je polyen jen pro lokální a perorální (nevstřebatelné) použití —
kandidóza dutiny ústní a střeva.
**Echinokandiny** (kaspofungin, anidulafungin) blokují syntézu **β-glukanu**
buněčné stěny; jsou dobře snášené a jsou lékem volby u invazivní kandidózy.
**Terbinafin** inhibuje skvalenepoxidázu — onychomykózy a dermatofytózy.
**Flucytosin** se vestavuje do RNA, kombinuje se s amfotericinem.
""")

K("93", "Antivirotika", """
**Antivirotika** jsou převážně **virostatická** — potlačují replikaci, ale
nevymýtí latentní virus; proto herpetické infekce recidivují. Cílem bývá
**virová polymeráza**, protože ta se dostatečně liší od lidské.
**Herpetické viry: aciklovir** je proléčivo, které fosforyluje **virová
thymidinkináza** — proto se aktivuje jen v infikované buňce, což vysvětluje
jeho vysokou bezpečnost. Aktivní trifosfát pak blokuje virovou DNA-polymerázu
a působí jako **terminátor řetězce**. Valaciklovir má lepší biologickou
dostupnost. Riziko je **krystalurie a nefrotoxicita** při nedostatečné
hydrataci. Na **cytomegalovirus** slouží ganciklovir a valganciklovir
(myelosuprese), rezervně foskarnet a cidofovir (nefrotoxické).
**Chřipka: oseltamivir a zanamivir** blokují **neuraminidázu**, a brání tak
uvolnění nových virionů z buňky — účinné jen **do 48 hodin** od začátku
příznaků. **Hepatitida C:** přímo působící antivirotika (sofosbuvir,
ledipasvir, glekaprevir) dosahují vyléčení u naprosté většiny nemocných.
**Hepatitida B:** tenofovir, entekavir, peginterferon.
""")

K("94", "Antiretrovirotika", """
**Antiretrovirotika** potlačují replikaci HIV natolik, že virová nálož klesne
pod mez detekce; **infekci nevyléčí**, protože provirus přetrvává v paměťových
buňkách. Podávají se **vždy v kombinaci (cART)** — nejméně tři léčiva ze dvou
skupin — protože monoterapie během týdnů vybere rezistentní kmen.
**Skupiny podle kroku replikačního cyklu:**
**NRTI** — nukleosidové inhibitory reverzní transkriptázy (tenofovir,
emtricitabin, abakavir, lamivudin); terminují řetězec. Abakavir smí být podán
až po vyšetření **HLA-B*5701** kvůli hypersenzitivitě, starší NRTI působí
mitochondriální toxicitu a laktátovou acidózu.
**NNRTI** — nenukleosidové (efavirenz, rilpivirin, doravirin), vážou se
alostericky; interagují přes CYP450, efavirenz působí neuropsychicky.
**Inhibitory proteázy** (darunavir, atazanavir) blokují štěpení polyproteinu;
boostují se ritonavirem nebo kobicistatem (inhibitory CYP3A4), působí
**dyslipidemii a lipodystrofii**.
**Inhibitory integrázy** (dolutegravir, bictegravir) jsou dnes základem
první linie — rychlý pokles nálože, málo interakcí.
**Inhibitory vstupu:** maravirok (CCR5), enfuvirtid. **PrEP:** tenofovir
s emtricitabinem.
""")

K("95", "Antitusika, mukolytika, expektorancia", """
**Kašel je obranný reflex** — produktivní kašel se tlumit nemá, protože brání
odstranění sekretu; tlumí se jen **suchý dráždivý kašel**. Proto se
**antitusika zásadně nekombinují s mukolytiky** (hromadil by se hlen).
**Antitusika centrální — opioidní: kodein** a **dextromethorfan** tlumí
centrum kašle v prodloužené míše. Kodein je proléčivo metabolizované
**CYP2D6 na morfin**, působí zácpu, útlum dechu a je návykový; u dětí je
kontraindikován. Dextromethorfan není analgetický ani (v běžné dávce)
návykový, ve vysokých dávkách je disociativní. **Butamirát** je neopioidní
centrální antitusikum. **Periferní** antitusika snižují dráždivost receptorů
v dýchacích cestách.
**Mukolytika** mění vlastnosti hlenu. **N-acetylcystein** štěpí **disulfidové
můstky** mukoproteinů, čímž hlen zřeďuje; současně je **antidotem otravy
paracetamolem** (doplňuje glutathion). **Ambroxol** a bromhexin zvyšují
sekreci surfaktantu a tvorbu řidšího hlenu. **Erdostein**, **dornáza alfa**
(štěpí DNA v hnisavém sputu u cystické fibrózy).
**Expektorancia** (guaifenesin, silice, břečťan) zvyšují objem sekretu a
usnadňují vykašlání; základem zůstává **dostatečná hydratace**.
""")

K("96", "Antiastmatika", """
**Astma je chronický zánět dýchacích cest** s bronchiální hyperreaktivitou,
proto je jeho základem **protizánětlivá léčba, nikoli bronchodilatace**.
Léčiva se dělí na **úlevová** (podle potřeby) a **kontrolující** (denně).
**Úlevová: SABA — salbutamol, fenoterol** — β2-agonisté s rychlým nástupem,
relaxují hladký sval bronchu; nežádoucí je **tremor, tachykardie,
hypokalemie**. Vysoká spotřeba SABA je známkou špatně kontrolovaného astmatu.
Dále **ipratropium** (krátkodobé anticholinergikum).
**Kontrolující: inhalační kortikosteroidy (IKS)** — budesonid, flutikason,
beklometason — jsou **základem léčby**; potlačují zánět, jejich hlavním
lokálním nežádoucím účinkem je **orofaryngeální kandidóza a dysfonie**, čemuž
brání **výplach úst po inhalaci a použití nástavce**. **LABA** (formoterol,
salmeterol) se podávají **výhradně s IKS**, nikdy samostatně — monoterapie
LABA zvyšuje mortalitu. Dnešní standard je **fixní kombinace IKS + formoterol**
i jako úlevová léčba. Dále **LAMA** (tiotropium), **antileukotrieny**
(montelukast — pozor na neuropsychické reakce), **teofylin** (úzké
terapeutické okno) a **biologika** (omalizumab anti-IgE, mepolizumab anti-IL-5).
""")

K("97", "Antihistaminika", """
**Antihistaminika** blokují histaminové receptory. **H1-antihistaminika** jsou
inverzní agonisté H1 receptoru a tlumí projevy alergie: **svědění, kopřivku,
rýmu, kýchání a slzení**; na bronchokonstrikci u astmatu ani na anafylaxi
nestačí — **lékem první volby u anafylaxe je adrenalin**.
**I. generace** (bisulepin, prometazin, difenhydramin, hydroxyzin) prochází
**hematoencefalickou bariérou** a působí **sedaci** — nesmí se řídit ani pít
alkohol. Mají navíc **anticholinergní účinky**: sucho v ústech, retence moči,
rozmazané vidění, zácpa, u starších zmatenost; kontraindikací je
**glaukom s uzavřeným úhlem a hyperplazie prostaty**. Sedace a antiemetický
efekt se využívají cíleně (kinetóza, svědění v noci, premedikace).
**II. generace** (**cetirizin, loratadin, desloratadin, fexofenadin,
bilastin**) do CNS prakticky nepronikají — **nesedují a nemají anticholinergní
efekt**, proto jsou volbou pro denní léčbu. Starší preparáty této skupiny
(terfenadin, astemizol) byly staženy pro **prodloužení QT**.
**H2-antihistaminika** (famotidin) tlumí sekreci žaludeční kyseliny.
""")

K("98", "Laxativa, antidiaroika", """
**Laxativa** podporují vyprázdnění; podávají se až po vyloučení organické
příčiny a **nesmí se podat při podezření na střevní obstrukci nebo náhlou
příhodu břišní**. Základem zůstává vláknina, tekutiny a pohyb.
**Osmotická: laktulóza** (nevstřebatelný disacharid, který střevní bakterie
štěpí na kyseliny — táhne vodu a **snižuje vstřebávání amoniaku**, proto se
používá u **jaterní encefalopatie**), **makrogol** (polyethylenglykol, dnes
lék volby, váže vodu bez dráždění) a solná projímadla (síran hořečnatý).
**Kontaktní/stimulační: bisakodyl, senna, pikosíran** dráždí myenterický
plexus a zvyšují sekreci; při chronickém zneužívání hrozí **hypokalemie
a atonie tračníku**, proto se nehodí k trvalému užívání.
**Objemová** (psyllium, ispaghula) bobtnají — nutný dostatečný příjem tekutin.
**Změkčující/lubrikační:** dokusát, parafinový olej (zhoršuje vstřebávání
vitaminů rozpustných v tucích). **Periferní antagonisté opioidů**
(methylnaltrexon, naloxegol) na zácpu při opioidech.
**Antidiaroika: loperamid** je agonista periferních **µ-opioidních receptorů**,
který zpomaluje peristaltiku a do CNS neproniká; **nesmí se podat u dysenterie
a horečnatého průjmu** (riziko toxického megakolon). Dále adsorbencia
(diosmektit, aktivní uhlí), probiotika a **rehydratace**, která je zásadní.
""")

K("99", "Farmakoterapie vředové choroby a GERD", """
Vřed vzniká **nepoměrem mezi agresivními faktory** (kyselina, pepsin,
*Helicobacter pylori*, NSA) **a ochranou sliznice** (hlen, bikarbonáty,
prostaglandiny). Léčba proto tlumí kyselinu, eradikuje bakterii a odstraní
vyvolávající lék.
**Inhibitory protonové pumpy (IPP)** — omeprazol, pantoprazol, esomeprazol —
ireverzibilně blokují **H+/K+-ATPázu** parietální buňky, tedy poslední společný
krok sekrece; jsou nejúčinnější. Podávají se **nalačno, 30 minut před jídlem**,
protože aktivují se jen na sekretující pumpě. Dlouhodobě: hypomagnezemie,
deficit **vitaminu B12**, zvýšené riziko klostridiové kolitidy a zlomenin;
omeprazol inhibuje **CYP2C19** a snižuje účinek **klopidogrelu** (volí se
pantoprazol).
**H2-antihistaminika** (famotidin) tlumí sekreci slaběji, hodí se na noční
příznaky. **Antacida** (hydroxid hlinitý a hořečnatý) neutralizují kyselinu —
rychlá, ale krátká úleva; **vážou jiná léčiva**, proto s odstupem.
**Protektiva:** sukralfát tvoří film na spodině vředu, misoprostol
(analog prostaglandinu) chrání před NSA, ale je **kontraindikován v graviditě**.
**Eradikace H. pylori:** IPP + **amoxicilin + klarithromycin** (nebo metronidazol),
běžně jako **čtyřkombinace s bismutem**, 10–14 dní.
""")

K("100", "Prokinetika, antiemetika, emetika", """
**Prokinetika** urychlují vyprazdňování žaludku a zvyšují tonus dolního jícnového
svěrače. **Metoklopramid** je antagonista **D2 receptorů** (a v centru zároveň
antiemetikum); prochází do CNS, a proto působí **extrapyramidové projevy —
akutní dystonii, u dlouhodobého podání tardivní dyskinezi** — z čehož plyne
omezení dávky a délky podávání. **Itoprid** a **domperidon** do CNS pronikají
málo (domperidon však **prodlužuje QT**). **Erythromycin** působí přes
motilinový receptor u gastroparézy.
**Antiemetika se volí podle příčiny zvracení:**
**Setrony — ondansetron** blokují **5-HT3** receptory v area postrema a ve
střevě; jsou základem u **cytostatiky a ozářením vyvolaného zvracení** a po
operaci. Nežádoucí: zácpa, bolest hlavy, **prodloužení QT**.
**Antagonisté NK1** (aprepitant) proti pozdní fázi po chemoterapii.
**Kortikosteroidy** (dexametazon) v kombinaci. **Antihistaminika I. generace**
(prometazin) a **anticholinergika (skopolamin)** u **kinetózy**.
**Neuroleptika** (haloperidol, levomepromazin) u zvracení v paliativní péči.
**Kanabinoidy** rezervně.
**Emetika: ipekakuanha a apomorfin** (agonista D2 v area postrema) se dnes
při otravách **prakticky nepoužívají** — vyvolávat zvracení se nedoporučuje
pro riziko aspirace; volí se aktivní uhlí.
""")
