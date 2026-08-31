#!/usr/bin/env python3
"""Vysvětlující schéma ke KAŽDÉ ze 136 zkouškových otázek z farmakologie.

Spuštění:
    python3 nastroje/farmakologie_obrazky.py           # vyrobí .md i .pdf

Každý záznam je `N(číslo, "Nadpis otázky", schéma)`. Schéma se skládá ze šablon
v `nastroje/schemata.py` — díky tomu vypadají všechna stejně a dají se hromadně
přegenerovat, když se něco opraví. Obrázek má nést JEDNU myšlenku otázky, ne
její obsah; text je ve `VYCUC-FINAL.md`.
"""
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from schemata import cil, retez, smycka, srovnani, stupnice, vetev  # noqa: E402

O = []


def N(cislo, nadpis, svg):
    O.append((cislo, nadpis, svg))


# ═══════════════════════════════════════════ OBECNÁ FARMAKOLOGIE  O1–O35

N("O1", "Farmakologie, původ a zdroje léčiv, názvy, lékopis", retez(
    [("ÚČINNÁ LÁTKA co působí", "zvyrazni"),
     ("+ POMOCNÉ LÁTKY plnivo, barvivo, konzervans", "normal"),
     ("= LÉKOVÁ FORMA tableta, mast, injekce", "normal"),
     ("= LÉČIVÝ PŘÍPRAVEK to, co koupíš v lékárně", "zvyrazni")],
    titulek="Od molekuly k tomu, co drží pacient v ruce",
    pozn="Tři názvy téže věci: chemický (dlouhý vzorec) · GENERICKÝ (ibuprofen) · "
         "firemní (Brufen). U zkoušky mluv generickým."))

N("O2", "Legislativa, doplňky stravy, zdravotnické prostředky, regulační orgány", srovnani(
    "LÉČIVÝ PŘÍPRAVEK",
    ["Musí prokázat ÚČINNOST a bezpečnost", "Registruje SÚKL / EMA",
     "Smí tvrdit, že léčí nemoc", "Hlásí se nežádoucí účinky"],
    "DOPLNĚK STRAVY",
    ["Účinnost prokazovat NEMUSÍ", "Jen ohlášení na SZPI — potravina",
     "Nesmí tvrdit, že léčí", "⚠️ Pacient v tom rozdíl nevidí"],
    titulek="Proč je „na to mám bylinky z lékárny\" jiná kategorie než lék",
    pozn="Zdravotnický prostředek působí FYZIKÁLNĚ (výplň, implantát, obvaz), "
         "lék FARMAKOLOGICKY."))

N("O3", "Předepisování léčivých přípravků", retez(
    [("LÉKAŘ vystaví eRecept", "zvyrazni"), ("CENTRÁLNÍ ÚLOŽIŠTĚ identifikátor", "normal"),
     ("LÉKÁRNA vydá a odepíše", "normal"), ("PACIENT", "zvyrazni")],
    titulek="Cesta receptu a co na něm musí být",
    pozn="Náležitosti: pacient · léčivo, síla, forma, množství · dávkování · lékař a "
         "razítko · datum. ⚠️ Opiáty na recept s modrým pruhem."))

N("O4", "Preklinické a klinické hodnocení léčiv", stupnice(
    [("PREKLINIKA", "zkumavka a zvíře — toxicita, kinetika, mechanismus", "tichy"),
     ("FÁZE I · desítky ZDRAVÝCH dobrovolníků", "ptá se: JE TO BEZPEČNÉ a jak se to chová?", "normal"),
     ("FÁZE II · stovky NEMOCNÝCH", "ptá se: ZABÍRÁ TO a v jaké dávce?", "normal"),
     ("FÁZE III · tisíce nemocných, srovnání", "ptá se: JE TO LEPŠÍ než dosavadní léčba?", "zvyrazni"),
     ("FÁZE IV · po registraci, celá populace", "⚠️ tady se najdou VZÁCNÉ nežádoucí účinky", "pozor")],
    titulek="Proč se vzácný nežádoucí účinek najde až po uvedení na trh",
    sipka_popis="čas a počet lidí",
    pozn="Fáze III má tisíce pacientů — účinek, který se stane jednomu z deseti tisíc, "
         "v ní nemá šanci vyjít najevo."))

N("O5", "Způsoby aplikace léčiv, výhody a nevýhody", srovnani(
    "PERORÁLNĚ (ústy)",
    ["Pohodlné, levné, bezpečné", "⚠️ Prochází JÁTRY = first-pass",
     "Pomalejší a méně předvídatelné", "Nejde použít u zvracení a bezvědomí"],
    "PARENTERÁLNĚ (i.v., i.m., s.c.)",
    ["⚠️ i.v. = 100% dostupnost, okamžitě", "Obchází játra i žaludek",
     "Nutná sterilita a personál", "⚠️ Podané se nedá vzít zpět"],
    titulek="Hlavní rozdíl není rychlost, ale jestli lék projde játry",
    pozn="Sublingválně, rektálně a transdermálně first-pass také obcházejí — proto "
         "nitroglycerin pod jazyk a ne polknout."))

N("O6", "Lékové formy — perorální a orální", srovnani(
    "PERORÁLNÍ = k POLKNUTÍ",
    ["Tablety, tobolky, sirupy", "Účinek až po vstřebání ve střevě",
     "⚠️ Enterosolventní obal chrání před žaludkem", "Retardované uvolňují postupně"],
    "ORÁLNÍ = ÚČINEK V ÚSTECH",
    ["Pastilky, ústní vody, gely", "⚠️ Sublingválně se vstřebá rovnou do krve",
     "Obchází játra (nitroglycerin)", "Zubařsky nejbližší skupina"],
    titulek="Dvě slova, která znějí stejně a znamenají opak",
    pozn="⚠️ Retardovanou ani enterosolventní tabletu nikdy nedrtit — zničí se "
         "mechanismus a uvolní se celá dávka najednou.", b_kind="zvyrazni"))

N("O7", "Lékové formy — parenterální a dermatologika", stupnice(
    [("i.v. — nitrožilně", "účinek OKAMŽITĚ, 100 % dávky v krvi", "zvyrazni"),
     ("i.m. — do svalu", "rychle, dobře prokrvený sval", "normal"),
     ("s.c. — pod kůži", "pomaleji, hodí se pro inzulin a hepariny", "normal"),
     ("depotní / transdermální náplast", "⚠️ nejpomalejší, ale drží dny", "tichy")],
    titulek="Rychlost účinku sleduje prokrvení místa vpichu",
    sipka_popis="čím níž, tím pomaleji",
    pozn="Masti (tučné, na suchou kůži) · krémy (voda i tuk) · gely (vodné, chladí) — "
         "čím tučnější základ, tím hlubší průnik."))

N("O8", "Lékové formy — oční, ušní, nosní, rektalia, vaginalia, inhalanda", cil(
    "MÍSTNÍ PODÁNÍ ⚠️ „místní\" neznamená „bez celkového účinku\"",
    [("OČNÍ kapky — timolol z kapek sráží tep a dusí astmatika", "pozor"),
     ("NOSNÍ kapky — ⚠️ max 7 dní, jinak rhinitis medicamentosa", "pozor"),
     ("INHALANDA — kortikoid → ⚠️ kandidóza v ústech", "pozor"),
     ("REKTÁLNĚ — částečně obchází játra, funguje i při zvracení", "normal"),
     ("VAGINÁLNĚ — místní léčba infekcí", "normal"),
     ("UŠNÍ — ⚠️ ne při perforaci bubínku", "normal")],
    titulek="Každá „místní\" forma se dokáže vstřebat do celého těla",
    pozn="Po nakapání do oka stiskni vnitřní koutek — sníží to vstřebání přes slzný "
         "kanálek do nosu."))

N("O9", "Komunikace, adherence, compliance, placebo a nocebo", srovnani(
    "PLACEBO",
    ["Očekávání ZLEPŠENÍ → stav se zlepší", "Měřitelný, ne „vymyšlený\" efekt",
     "Zesiluje účinek každého skutečného léku", "Vzhled a jistota lékaře na tom mají podíl"],
    "NOCEBO",
    ["Očekávání ŠKODY → potíže se objeví", "⚠️ Vzniká i z příbalového letáku",
     "Časté vysazení statinů a antidepresiv", "Vytvoří ho i špatně řečená věta"],
    titulek="Tvoje slova jsou účinná látka s dávkou",
    pozn="Adherence = jestli pacient léčbu dodržuje. ⚠️ Nejčastější příčina „selhání "
         "léčby\" není špatný lék, ale nebrané tablety.", a_kind="zvyrazni"))

N("O10", "Přechod látek biologickými membránami", retez(
    [("NENABITÁ forma tuková, projde membránou", "zvyrazni"),
     ("PROJDE do buňky", "normal"),
     ("uvnitř jiné pH → NABIJE SE", "pozor"),
     ("⚠️ nabité neprojde zpět → HROMADÍ SE", "pozor")],
    ["prostá difuze", "", "IONTOVÁ PAST"],
    titulek="Iontová past — nejvýnosnější obrázek celé obecné farmakologie",
    pozn="Vysvětlí pětkrát: anestezie nezabírá v zaníceném zubu · alkalizace moči u otravy "
         "aspirinem · laktulóza u encefalopatie · léky v mléce a u plodu · nikotin z kouře."))

N("O11", "Základní farmakokinetické parametry a procesy", retez(
    [("A — ABSORPCE vstřebání", "normal"), ("D — DISTRIBUCE rozvod po těle", "normal"),
     ("M — METABOLISMUS přeměna, hlavně v játrech", "normal"),
     ("E — EXKRECE vyloučení, hlavně ledvinami", "normal")],
    titulek="ADME — co tělo dělá s lékem",
    pozn="⚠️ Farmakokinetika = co tělo dělá s lékem. Farmakodynamika = co lék dělá s tělem. "
         "Nepleť si to, ptají se na to jako na první otázku."))

N("O12", "Procesy nultého a prvního řádu, saturační kinetika", srovnani(
    "PRVNÍ ŘÁD (většina léků)",
    ["Odbourá se stále stejný PODÍL", "Např. polovina za hodinu",
     "Enzym má rezervu, stíhá", "⚠️ Má poločas — dá se počítat"],
    "NULTÝ ŘÁD (etanol, fenytoin, aspirin ve vysoké dávce)",
    ["Odbourá se stále stejné MNOŽSTVÍ", "Enzym je NASYCENÝ, víc nestíhá",
     "⚠️ Malé zvýšení dávky → skok hladiny", "⚠️ Poločas nemá smysl"],
    titulek="Proč u fenytoinu stačí přidat kousek a pacient je otrávený",
    pozn="Saturační kinetika = přechod mezi nimi. Dokud je enzym volný, jede první řád; "
         "jakmile se zahltí, přepne na nultý."))

N("O13", "Absorpce, Batemanova funkce, biologická dostupnost, AUC", srovnani(
    "VRCHOL KŘIVKY (Cmax, tmax)",
    ["⚠️ NENÍ konec vstřebávání", "Je to REMÍZA: kolik se vstřebá,",
     "tolik se právě odbourává", "Potom už převáží eliminace"],
    "AUC — plocha pod křivkou",
    ["Kolik léku se CELKEM dostalo do krve", "Základ biologické dostupnosti (F)",
     "⚠️ i.v. = F 100 %, p.o. je vždy méně", "Podle AUC se posuzují generika"],
    titulek="Batemanova křivka — co znamená její vrchol",
    pozn="Biologická dostupnost je podíl dávky, který se dostal do krve nezměněný. "
         "First-pass ji sráží nejvíc.", b_kind="zvyrazni"))

N("O14", "Distribuce, distribuční objem, vazba na bílkoviny, bariéry", srovnani(
    "VÁZANÁ frakce",
    ["Sedí na albuminu (kyselé léky)", "nebo na orosomukoidu (zásadité)",
     "⚠️ NEÚČINNÁ — je to sklad", "Nefiltruje se ani nepůsobí"],
    "VOLNÁ frakce",
    ["⚠️ JEN TA PŮSOBÍ", "Jen ta se metabolizuje a vylučuje",
     "⚠️ Málo albuminu (senior, cirhóza, nefrotický sy)", "→ volné frakce přibude → předávkování"],
    titulek="Proč pacient s nízkým albuminem dostane při normální dávce toxický účinek",
    pozn="Distribuční objem není skutečný objem — je to poměr dávky a koncentrace v krvi. "
         "Velký Vd = lék je schovaný ve tkáních, dialýza ho nedostane ven.", a_kind="tichy"))

N("O15", "Eliminace, poločas, fáze α a β, clearance", srovnani(
    "FÁZE α — DISTRIBUČNÍ",
    ["Rychlý pokles hladiny", "⚠️ lék se jen PŘESTĚHOVAL do tkání",
     "Nic se ještě neodbouralo", "Tím končí účinek thiopentalu"],
    "FÁZE β — ELIMINAČNÍ",
    ["Pomalý pokles", "Teď se lék skutečně odbourává a vylučuje",
     "⚠️ Z ní se počítá biologický poločas", "Po 4–5 poločasech je lék pryč"],
    titulek="Dvě fáze poklesu — a jen ta druhá znamená, že lék mizí z těla",
    pozn="Clearance = objem krve očištěný za jednotku času. Poločas závisí na clearance "
         "A na distribučním objemu zároveň.", a_kind="pozor", b_kind="zvyrazni"))

N("O16", "Dávkovací režim, kumulace, kumulační index", retez(
    [("VANA = tělo", "tichy"), ("KOHOUTEK = dávkování", "zvyrazni"),
     ("ODTOK = eliminace", "normal"), ("USTÁLENÝ STAV: přitéká = odtéká", "zvyrazni")],
    ["napouštím", "vypouštím", "za 4–5 poločasů"],
    titulek="Nasycovací × udržovací dávka na jednom obrázku",
    pozn="NASYCOVACÍ dávka naplní vanu naráz (řídí ji distribuční objem). UDRŽOVACÍ jen "
         "dorovnává, co odteče (řídí ji clearance). ⚠️ Ustálený stav přijde vždy až za 4–5 poločasů."))

N("O17", "Biotransformace léčiv, fáze, příklady", vetev(
    "PARACETAMOL v terapeutické dávce",
    [("90 % — fáze II, konjugace", "neškodné metabolity → moč", "normal"),
     ("10 % — fáze I, CYP2E1", "⚠️ NAPQI — jedovatý", "pozor"),
     ("GLUTATHION ho zneškodní", "⚠️ dokud zásoba vydrží", "zvyrazni")],
    titulek="Fáze I × fáze II na jednom léku — a celá otrava paracetamolem",
    pozn="Předávkování, alkohol nebo hladovění → hlavní cesta se nasytí, NAPQI přibývá, "
         "glutathion dojde → nekróza jater. Antidotum N-ACETYLCYSTEIN dodá stavební kámen glutathionu."))

N("O18", "Úloha jater v eliminaci léčiv, first-pass efekt", retez(
    [("100 % polknuté dávky", "zvyrazni"), ("STŘEVNÍ STĚNA první ztráta", "normal"),
     ("JÁTRA přes portální žílu ⚠️ hlavní ztráta", "pozor"),
     ("do těla dorazí třeba jen 10 %", "normal")],
    ["", "portální oběh", "FIRST-PASS"],
    titulek="First-pass efekt — proč se stejná látka dávkuje ústy jinak než do žíly",
    pozn="Obcházejí ho: sublingválně, i.v., i.m., transdermálně a částečně rektálně. "
         "Proto se nitroglycerin dává pod jazyk a testosteron injekčně."))

N("O19", "Inhibice a indukce enzymů léčivy, klinický význam", srovnani(
    "INHIBITOR — brzda",
    ["Makrolidy, azoly, ⚠️ grapefruit, ritonavir", "Enzym přestane pracovat HNED",
     "→ hladina druhého léku STOUPNE", "⚠️ hrozí PŘEDÁVKOVÁNÍ"],
    "INDUKTOR — plyn",
    ["Rifampicin, karbamazepin, fenytoin, ⚠️ třezalka, kouření",
     "Enzymu se musí NAROBIT — trvá dny", "→ hladina druhého léku KLESNE",
     "⚠️ hrozí SELHÁNÍ LÉČBY (antikoncepce!)"],
    titulek="Dva směry jedné interakce a jejich různá rychlost",
    pozn="⚠️ Nebezpečí indukce nekončí vysazením induktoru — enzymy se ještě týdny "
         "odbourávají a hladina druhého léku pak vyskočí nahoru.", a_kind="pozor", b_kind="pozor"))

N("O20", "Vylučování léčiv renální a extrarenální", retez(
    [("GLOMERULÁRNÍ FILTRACE ⚠️ jen VOLNÁ frakce", "zvyrazni"),
     ("TUBULÁRNÍ SEKRECE aktivní, i vázané léky", "normal"),
     ("TUBULÁRNÍ RESORPCE ⚠️ nenabité se vrací zpět", "pozor"),
     ("MOČ", "normal")],
    titulek="Tři děje v ledvině — a proč alkalizace moči urychlí vyloučení aspirinu",
    pozn="Zásaditá moč udrží kyselý lék v nabité formě → nevstřebá se zpět → odejde. "
         "Extrarenálně: žlučí (⚠️ enterohepatální oběh), plícemi, mlékem, slinami, potem."))

N("O21", "Účinek léčiv obecně, způsob účinku na molekulární úrovni", srovnani(
    "SPECIFICKÝ účinek",
    ["Přes konkrétní cílovou strukturu", "Receptor, enzym, kanál, přenašeč",
     "Působí v malých dávkách", "Většina léčiv"],
    "NESPECIFICKÝ účinek",
    ["Fyzikálně-chemický, bez receptoru", "Antacida, projímadla, dezinficiencia,",
     "aktivní uhlí, osmotická diuretika", "Potřebuje velké dávky"],
    titulek="Dva způsoby, jak léčivo vůbec může působit", b_kind="tichy",
    pozn="Podle výsledku: kauzální (odstraní příčinu — antibiotikum) × symptomatická "
         "(uleví — analgetikum) × substituční (nahradí, co chybí — inzulin)."))

N("O22", "Specifický účinek, receptorová teorie, typy receptorů", stupnice(
    [("IONOTROPNÍ = sám je kanál", "nikotinový, GABA-A, NMDA · ⚠️ MILISEKUNDY", "zvyrazni"),
     ("SPŘAŽENÝ S G-PROTEINEM", "muskarinový, adrenergní, opioidní · sekundy", "normal"),
     ("S VLASTNÍ ENZYMOVOU AKTIVITOU", "inzulinový receptor · minuty", "normal"),
     ("NITROBUNĚČNÝ — mění přepis genů", "kortikoidy, hormony štítnice · ⚠️ HODINY", "pozor")],
    titulek="Typ receptoru určuje, za jak dlouho lék zabere",
    sipka_popis="čím níž, tím pomaleji",
    pozn="Proto adrenalin u anafylaxe zabere za minutu a kortikoid až za hodiny — a proto "
         "kortikoid anafylaxi sám nezachrání."))

N("O23", "Dávka a účinek, terapeutický index, terapeutické okno, NNT", srovnani(
    "ŠIROKÉ okno",
    ["Penicilin, většina běžných léků", "Mezi účinnou a toxickou dávkou je prostor",
     "Hladiny se neměří", "Bezpečné i při chybě v dávce"],
    "⚠️ ÚZKÉ okno",
    ["Digoxin, lithium, warfarin, theofylin,", "fenytoin, aminoglykosidy, cytostatika",
     "⚠️ účinná a toxická dávka skoro splývají", "⚠️ MĚŘÍ SE HLADINY"],
    titulek="Terapeutické okno — jediné, co určuje, jestli se lék monitoruje",
    pozn="NNT = kolik pacientů musíš léčit, aby jeden měl prospěch. Čím nižší, tím lepší lék."))

N("O24", "Vlivy působící na kinetiku a dynamiku léčiv", cil(
    "STEJNÁ DÁVKA ≠ STEJNÝ ÚČINEK",
    [("VĚK — novorozenec i senior mají jinou kinetiku", "normal"),
     ("JÁTRA a LEDVINY — hlavní orgány eliminace", "pozor"),
     ("GENETIKA — pomalý × rychlý metabolizátor", "normal"),
     ("JINÉ LÉKY — indukce a inhibice", "pozor"),
     ("STRAVA — grapefruit, mléko, vitamin K", "normal"),
     ("HMOTNOST a složení těla — voda × tuk", "normal")],
    titulek="Proč se dávka nedá určit jen podle diagnózy"))

N("O25", "Lékové interakce", srovnani(
    "FARMAKOKINETICKÉ",
    ["Mění HLADINU druhého léku", "Vstřebání (antacida × tetracykliny)",
     "Vytěsnění z bílkoviny", "⚠️ Indukce a inhibice enzymů"],
    "FARMAKODYNAMICKÉ",
    ["Hladina je stejná, mění se ÚČINEK", "Sčítání (alkohol + benzodiazepin)",
     "Rušení (naloxon × morfin)", "⚠️ „Triple whammy\" na ledviny"],
    titulek="Dvě zcela různé cesty, jak si dva léky vjedou do vlasů",
    pozn="Aditivní 1+1=2 · synergie 1+1=5 · potenciace 0+1=5 (látka sama neúčinná zesílí "
         "druhou) · antagonismus = princip všech antidot."))

N("O26", "Farmakogenetika, genetický polymorfismus", vetev(
    "STEJNÁ DÁVKA STEJNÉHO LÉKU",
    [("POMALÝ metabolizátor", "⚠️ lék se hromadí → toxicita", "pozor"),
     ("NORMÁLNÍ metabolizátor", "očekávaný účinek", "zvyrazni"),
     ("ULTRARYCHLÝ metabolizátor", "⚠️ lék zmizí dřív, než zabere", "pozor")],
    titulek="Proč jeden pacient nemá účinek a druhý je otrávený",
    pozn="Příklady: CYP2D6 a KODEIN (proléčivo — ultrarychlí udělají moc morfinu, u dětí "
         "popsána úmrtí) · CYP2C19 a klopidogrel · TPMT a azathioprin · plazmatická "
         "cholinesteráza a sukcinylcholin · HLA-B*5701 a abakavir."))

N("O27", "Tolerance, tachyfylaxe, rezistence", srovnani(
    "TOLERANCE / TACHYFYLAXE",
    ["Slábne odpověď ORGANISMU", "Tolerance = pomalu, po dnech a týdnech",
     "⚠️ Tachyfylaxe = během hodin", "Vyčerpané zásoby nebo down-regulace receptorů"],
    "REZISTENCE",
    ["Změnil se PATOGEN nebo NÁDOR", "Betalaktamázy, změněný cíl,",
     "efluxní pumpy, nižší propustnost", "⚠️ Roste používáním antibiotik"],
    titulek="Otupí se pacient, nebo bakterie? To je celý rozdíl",
    pozn="Down-regulace = receptorů ubývá při nadbytku podnětu. Up-regulace = přibývá při "
         "blokádě → proto se betablokátor nikdy nevysazuje náhle.", b_kind="pozor"))

N("O28", "Vliv průvodních onemocnění, polypragmazie", vetev(
    "POLYPRAGMAZIE 5 a více léků současně",
    [("interakce rostou GEOMETRICKY", "u 8 léků už je nikdo neuhlídá", "pozor"),
     ("PRESKRIPČNÍ KASKÁDA", "nežádoucí účinek se léčí dalším lékem", "pozor"),
     ("horší adherence", "pacient přestane brát i to důležité", "normal")],
    titulek="Proč každý přidaný lék není jen „+1\"",
    pozn="⚠️ Játra: nižší metabolismus a málo albuminu. Ledviny: kumulace. Srdeční selhání: "
         "horší prokrvení střeva i jater. Nemoc mění kinetiku stejně jako věk."))

N("O29", "Nežádoucí účinky léčiv", srovnani(
    "TYP A — „Augmented\"",
    ["Vyplývá z mechanismu léku", "⚠️ ZÁVISLÝ NA DÁVCE, předvídatelný",
     "Častý, obvykle méně závažný", "Krvácení po warfarinu, sucho po atropinu"],
    "TYP B — „Bizarre\"",
    ["S mechanismem nesouvisí", "⚠️ NEZÁVISLÝ NA DÁVCE, nepředvídatelný",
     "Vzácný, ale často závažný", "Alergie, agranulocytóza, maligní hypertermie"],
    titulek="Dva typy, které se řeší úplně jinak",
    pozn="Typ A se řeší snížením dávky. ⚠️ Typ B jen okamžitým vysazením a lék se nesmí "
         "podat znovu.", a_kind="normal"))

N("O30", "Léková alergie, idiosynkrazie", srovnani(
    "ALERGIE",
    ["Zapojený IMUNITNÍ systém", "⚠️ Nutná předchozí SENZIBILIZACE",
     "Při prvním podání nevznikne", "Vyrážka → anafylaxe; ⚠️ i malá dávka stačí"],
    "IDIOSYNKRAZIE",
    ["Imunita v tom NENÍ", "Geneticky daná odchylka enzymu",
     "⚠️ Může přijít hned napoprvé", "Hemolýza při deficitu G6PD"],
    titulek="Ne každá „reakce na lék\" je alergie",
    pozn="⚠️ Anafylaxe = adrenalin i.m., ne antihistaminikum. Anafylaktoidní reakce "
         "(kontrastní látka, vankomycin) vypadá stejně, ale imunitu nezapojuje."))

N("O31", "Karcinogenní a mutagenní účinky", retez(
    [("MUTAGEN poškodí DNA", "pozor"), ("mutace v klíčovém genu", "normal"),
     ("ztráta kontroly dělení", "normal"), ("⚠️ NÁDOR — po LETECH", "pozor")],
    titulek="Proč se karcinogenita neprojeví v klinické studii",
    pozn="⚠️ U karcinogenů se předpokládá, že bezpečná dávka neexistuje. Testuje se "
         "AMESOVÝM TESTEM (mutagenita na bakteriích) a dlouhodobě na zvířatech; klasifikuje IARC."))

N("O32", "Léčiva v těhotenství, teratogenní účinek, léčiva v době kojení", stupnice(
    [("1.–2. týden — „vše nebo nic\"", "buď potrat, nebo se nic nestane", "tichy"),
     ("⚠️ 3.–8. TÝDEN — ORGANOGENEZE", "⚠️ NEJVĚTŠÍ RIZIKO VROZENÝCH VAD", "pozor"),
     ("9. týden až porod — růst a zrání", "spíš funkční poruchy a poruchy růstu", "normal")],
    titulek="Kdy je plod nejzranitelnější",
    sipka_popis="průběh těhotenství",
    pozn="⚠️ Klasické teratogeny: isotretinoin, valproát, warfarin, ACE inhibitory a "
         "sartany, methotrexát, thalidomid, tetracykliny, lithium. ⚠️ Nejrizikovější doba "
         "je ta, kdy žena o těhotenství ještě neví."))

N("O33", "Farmakoterapie v dětství", srovnani(
    "FÁZE I (oxidace)",
    ["U novorozence ČÁSTEČNĚ funguje", "Dozrává během prvních měsíců", ""],
    "⚠️ FÁZE II (glukuronidace)",
    ["⚠️ U novorozence NEFUNGUJE", "Dozrává až kolem 2 let",
     "⚠️ CHLORAMFENIKOL → GRAY BABY", "⚠️ Sulfonamid → jádrový ikterus"],
    titulek="Dítě není malý dospělý — první fáze funguje, druhá ne",
    pozn="⚠️ Reyeův syndrom: aspirin + dítě + viróza → jaterní encefalopatie. "
         "⚠️ Tetracykliny barví zuby. Dávka se počítá na POVRCH těla, ne na hmotnost."))

N("O34", "Farmakoterapie ve stáří, polypragmazie", srovnani(
    "UBÝVÁ VODY",
    ["Hydrofilní lék se má kam MÉNĚ rozředit", "→ ⚠️ KONCENTRACE hned stoupne",
     "Digoxin, aspirin, lithium", "⚠️ Problém už po první dávce"],
    "PŘIBÝVÁ TUKU",
    ["Lipofilní lék má kam se schovat", "→ ⚠️ větší Vd → DELŠÍ POLOČAS",
     "Benzodiazepiny", "⚠️ Problém až za týden"],
    titulek="Distribuce se ve stáří mění dvěma protichůdnými směry najednou",
    pozn="⚠️ Normální kreatinin u seniora neznamená normální ledviny — vyrábí ho méně "
         "(úbytek svalů) A hůř ho vylučuje; ty změny se navzájem vyruší.",
    a_kind="pozor", b_kind="pozor"))

N("O35", "Biologická léčba: rozdělení, názvosloví, biosimilars", stupnice(
    [("-O-  MYŠÍ protilátka", "nejvíc cizí → ⚠️ nejvíc imunogenní", "pozor"),
     ("-XI-  CHIMÉRICKÁ", "infliximab, rituximab", "normal"),
     ("-ZU-  HUMANIZOVANÁ", "trastuzumab, omalizumab", "normal"),
     ("-U-  PLNĚ HUMÁNNÍ", "adalimumab, denosumab → nejméně imunogenní", "zvyrazni")],
    titulek="Názvosloví protilátek kopíruje historii oboru",
    sipka_popis="čím níž, tím lidštější",
    pozn="⚠️ Biosimilar není generikum — živá buňka nikdy nevyrobí dvě identické molekuly, "
         "liší se i dvě šarže originálu. ⚠️ Koncovka -tinib (imatinib) NENÍ biologikum, "
         "je to malá molekula."))
