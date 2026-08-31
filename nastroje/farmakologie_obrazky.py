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


# ═══════════════════════════════════════════ SPECKA I  36–88

N("36", "Cholinergní přenos vzruchu", retez(
    [("cholin + acetyl-CoA", "normal"), ("ACETYLCHOLIN ve vezikule", "zvyrazni"),
     ("EXOCYTÓZA do štěrbiny", "normal"),
     ("⚠️ ROZŠTĚPÍ HO ENZYM acetylcholinesteráza", "pozor")],
    ["cholinacetyl- transferáza", "⚠️ botulotoxin blokuje", "receptory M1–M5, Nm, Nn"],
    titulek="Acetylcholin se ve štěrbině ROZŠTĚPÍ — noradrenalin se vychytá zpět",
    pozn="Proto na acetylcholin fungují inhibitory esterázy a na noradrenalin blokátory "
         "reuptake. ⚠️ M2 = srdce (jediný tlumivý) · M3 = žlázy a hladký sval · Nm = ploténka."))

N("37", "Přímá cholinomimetika", cil(
    "PŘÍMÉ CHOLINOMIMETIKUM sedne na receptor místo acetylcholinu",
    [("SLINY a SLZY ⚠️ pilokarpin na xerostomii", "zvyrazni"),
     ("MIÓZA — léčba glaukomu", "zvyrazni"),
     ("BRADYKARDIE", "normal"),
     ("⚠️ BRONCHOSPAZMUS — KI u astmatu", "pozor"),
     ("⚠️ SEKRECE KYSELINY — KI u vředu", "pozor"),
     ("PERISTALTIKA a měchýř — betanechol", "normal")],
    titulek="Zapneš celý parasympatikus najednou — žádané i nežádoucí",
    pozn="🔑 SLUDGE: Salivace, Lakrimace, Urinace, Defekace, GIT křeče, Emeze."))

N("38", "Nepřímá cholinomimetika", srovnani(
    "NEOSTIGMIN — KVARTÉRNÍ",
    ["Nabitý → ⚠️ NEPROJDE do mozku", "Myasthenia gravis, dekurarizace",
     "⚠️ Podává se s ATROPINEM", "aby nezpůsobil bradykardii"],
    "FYZOSTIGMIN — TERCIÁRNÍ",
    ["⚠️ PROJDE do mozku", "→ antidotum centrálního",
     "anticholinergního syndromu", "(durman, atropin, TCA)"],
    titulek="Jedno písmeno rozhoduje, jestli lék projde do mozku",
    pozn="⚠️ Otrava organofosfáty: atropin (na M receptory) + PRALIDOXIM (reaktivátor enzymu) "
         "— ten musí přijít dřív, než enzym „zestárne\".", b_kind="zvyrazni"))

N("39", "Parasympatolytika", cil(
    "ATROPIN blokáda M receptorů = obrácený parasympatikus",
    [("„slepý jako netopýr\" mydriáza, cykloplegie", "normal"),
     ("⚠️ „suchý jako kost\" XEROSTOMIE → KAZ", "pozor"),
     ("„červený jako řepa\"", "normal"),
     ("„horký jako pec\" nepotí se, nemá jak chladit", "pozor"),
     ("„šílený jako kloboučník\" delirium", "pozor"),
     ("tachykardie, zácpa, retence moči", "normal")],
    titulek="Pět přirovnání, ze kterých poznáš otravu atropinem",
    pozn="⚠️ Zubařsky: xerostomii nedělá jen atropin — stejně suší tricyklická antidepresiva, "
         "antipsychotika, antihistaminika a léky na hyperaktivní měchýř. A ty pacient bere roky."))

N("40", "Adrenergní přenos vzruchu", retez(
    [("TYROSIN", "normal"), ("DOPA ⚠️ krok určující rychlost", "pozor"),
     ("DOPAMIN", "normal"), ("NORADRENALIN ⚠️ v nadledvině → ADRENALIN", "zvyrazni")],
    ["tyrosin- hydroxyláza", "dekarboxyláza", "dopamin-β- hydroxyláza"],
    titulek="Syntéza katecholaminů a kde vzniká adrenalin",
    pozn="⚠️ Zánik NENÍ enzymem ve štěrbině, ale REUPTAKE zpět do neuronu (kokain a "
         "tricyklika ho blokují); teprve pak MAO uvnitř a COMT vně. Adrenalin vzniká jen "
         "v dřeni nadledvin — jen tam je enzym PNMT."))

N("41", "Neselektivní sympatomimetika", cil(
    "ADRENALIN u ANAFYLAXE ⚠️ i.m. do stehna",
    [("α1 — stáhne cévy → zvedne TLAK", "zvyrazni"),
     ("β1 — podpoří SRDCE", "zvyrazni"),
     ("β2 — rozšíří PRŮDUŠKY", "zvyrazni"),
     ("β2 — zastaví výdej mediátorů ze žírných buněk", "zvyrazni"),
     ("⚠️ antihistaminikum tohle NEUMÍ", "pozor"),
     ("⚠️ kortikoid působí až za hodiny", "pozor")],
    titulek="Proč je adrenalin u anafylaxe nenahraditelný",
    pozn="DOPAMIN má tři chování podle dávky: nízká → D1 ledviny · střední → β1 srdce · "
         "vysoká → α1 stah cév."))

N("42", "Sympatomimetika alfa", srovnani(
    "α1 — na periferii",
    ["Fenylefrin, midodrin, xylometazolin", "Stah cév → ⚠️ ZVYŠUJE TLAK",
     "Dekongesce nosu, mydriáza bez cykloplegie", "⚠️ Nosní kapky max 7 dní"],
    "α2 — CENTRÁLNĚ, PŘED synapsí",
    ["Klonidin, methyldopa, brimonidin", "Sedne si na BRZDU výdeje sympatiku",
     "→ ⚠️ SNIŽUJE TLAK", "⚠️ Methyldopa = volba v graviditě"],
    titulek="Paradox: obě jsou „alfa\", ale s tlakem dělají opak",
    pozn="⚠️ Rhinitis medicamentosa: po odeznění kapek sliznice oteče ještě víc, pacient "
         "kápne znovu a je v kruhu.", b_kind="zvyrazni"))

N("43", "Sympatomimetika beta", srovnani(
    "CO CHCEME — β2 v průduškách",
    ["SABA salbutamol, fenoterol — úlevově", "LABA formoterol, salmeterol",
     "⚠️ LABA NIKDY samotná bez kortikoidu", "Tokolytika: hexoprenalin"],
    "CO PŘIJDE S TÍM — β2 jinde",
    ["⚠️ TREMOR (β2 na kosterním svalu)", "⚠️ TACHYKARDIE (přelití na β1)",
     "⚠️ HYPOKALEMIE (β2 žene K⁺ do buňky)", "→ využito u akutní hyperkalemie"],
    titulek="Tři nežádoucí účinky β2-mimetik plynou z jediného receptoru",
    a_kind="zvyrazni"))

N("44", "Nepřímá sympatomimetika", retez(
    [("efedrin, amfetamin, ⚠️ TYRAMIN", "normal"),
     ("vytlačí NORADRENALIN z vezikul", "zvyrazni"),
     ("silná sympatická odpověď", "normal"),
     ("⚠️ vezikuly jsou prázdné → TACHYFYLAXE", "pozor")],
    titulek="Potřebují mít z čeho brát — proto jim rychle dojde dech",
    pozn="⚠️ Sýrový efekt: tyramin z uzrálých sýrů normálně zničí střevní MAO. U pacienta "
         "na neselektivním inhibitoru MAO projde, vytlačí noradrenalin → HYPERTENZNÍ KRIZE. "
         "Kokain naopak blokuje reuptake."))

N("45", "Sympatolytika alfa", retez(
    [("FEOCHROMOCYTOM", "normal"), ("⚠️ NEJDŘÍV α-BLOKÁDA fentolamin, fenoxybenzamin", "zvyrazni"),
     ("teprve POTOM betablokátor", "zvyrazni"), ("bezpečná operace", "normal")],
    titulek="Pořadí, které se ptají skoro vždycky",
    pozn="⚠️ Obráceně: zablokuješ β2 vazodilataci, zůstane čistý α1 stah → hypertenzní krize. "
         "⚠️ Tamsulosin je selektivní na α1A v prostatě → nesnižuje tlak, ale způsobuje "
         "„floppy iris\" při operaci šedého zákalu."))

N("46", "Sympatolytika beta (betablokátory)", srovnani(
    "β1 — SRDCE = žádaný účinek",
    ["Nižší tep a slabší stah", "Méně reninu → nižší tlak",
     "ICHS, hypertenze, arytmie", "⚠️ Srdeční selhání — jen 4 z nich, pomalu titrovat"],
    "β2 — PLÍCE a jinde = nežádoucí",
    ["⚠️ BRONCHOSPAZMUS — KI u astmatu", "⚠️ Maskuje hypoglykemii (pocení zůstane)",
     "Studené končetiny, únava", "⚠️ Nikdy nevysazovat náhle — rebound"],
    titulek="Selektivita je celý rozdíl mezi účinkem a nežádoucím účinkem",
    pozn="Neselektivní: propranolol, sotalol, ⚠️ timolol (i v očních kapkách!). "
         "β1-selektivní: metoprolol, bisoprolol, atenolol. S vazodilatací: karvedilol, nebivolol."))

N("47", "Myorelaxancia", srovnani(
    "SUKCINYLCHOLIN — depolarizující",
    ["Nejdřív fascikulace, pak ochabnutí", "⚠️ NEMÁ ANTIDOTUM",
     "⚠️ Hyperkalemie, maligní hypertermie", "⚠️ Atypická pseudocholinesteráza → apnoe"],
    "ROKURONIUM ap. — nedepolarizující",
    ["Kompetitivní blokáda ploténky", "⚠️ Antidotum NEOSTIGMIN + atropin",
     "⚠️ U rokuronia SUGAMMADEX (obalí ho)", "Atrakurium: ⚠️ Hofmannova eliminace"],
    titulek="Proč u jednoho antidotum je a u druhého ne",
    pozn="⚠️ U depolarizujícího bloku není problém nedostatek acetylcholinu, ale jeho "
         "nadbytek — neostigmin by blok prohloubil. Dantrolen působí přímo na sval "
         "(sarkoplazmatické retikulum) — maligní hypertermie.", b_kind="zvyrazni"))

N("48", "Lokální anestetika", retez(
    [("ANESTETIKUM = slabá zásada nenabité", "zvyrazni"), ("projde membránou", "normal"),
     ("uvnitř se nabije", "normal"), ("zavře Na⁺ kanál ZEVNITŘ", "zvyrazni")],
    titulek="Musí projít dovnitř, aby zavřelo kanál zevnitř",
    pozn="⚠️ ZÁNĚT = kyselé pH → skoro všechno je nabité UŽ VENKU → dovnitř se nedostane → "
         "V ZANÍCENÉM ZUBU ANESTEZIE NEZABERE. Estery (prokain) → alergie na PABA. "
         "Amidy (lidokain, ⚠️ ARTIKAIN) → játra. ⚠️ Bupivakain je kardiotoxický, "
         "prilokain dělá methemoglobinemii. Antidotum toxicity: LIPIDOVÁ EMULZE."))

N("49", "Celková anestetika — inhalační", srovnani(
    "MAC = jak je SILNÉ",
    ["Minimální alveolární koncentrace", "⚠️ NÍZKÁ MAC = SILNÉ anestetikum",
     "⚠️ Oxid dusný má MAC > 100 %", "→ sám nikdy neuspí"],
    "ROZPUSTNOST V KRVI = jak RYCHLE",
    ["Koeficient krev/plyn", "⚠️ NÍZKÁ rozpustnost = RYCHLÝ nástup",
     "co se nerozpustí v krvi, nasytí mozek", "Desfluran nejrychlejší, sevofluran standard"],
    titulek="Dvě veličiny, které spolu vůbec nesouvisí",
    pozn="⚠️ Oxid dusný: výborná analgezie → sedace u dětí a úzkostných pacientů v zubní "
         "ordinaci; rizika difuzní hypoxie a inaktivace vitaminu B12. "
         "⚠️ Maligní hypertermie po halogenovaných → dantrolen.", b_kind="zvyrazni"))

N("50", "Celková anestetika — intravenózní", cil(
    "ČÍM UVEDU PACIENTA DO ANESTEZIE?",
    [("PROPOFOL rychlý, antiemetický ⚠️ sráží tlak, bez analgezie", "normal"),
     ("THIOPENTAL ⚠️ krátkost je REDISTRIBUCÍ, ne metabolismem → kumuluje", "pozor"),
     ("KETAMIN ⚠️ jako jediný ZVYŠUJE tlak a nechá dýchat → šok, terén", "zvyrazni"),
     ("ETOMIDÁT kardiálně nejstabilnější ⚠️ tlumí kůru nadledvin", "normal"),
     ("MIDAZOLAM anxiolýza + amnézie", "normal"),
     ("⚠️ Všechna kromě ketaminu jdou přes GABA-A; ketamin blokuje NMDA", "pozor")],
    titulek="Každé má jednu přednost a jednu nevýhodu — podle toho se vybírá pacient"))

N("51", "Hypnotika", srovnani(
    "BENZODIAZEPIN",
    ["Zvyšuje FREKVENCI otevírání kanálu", "⚠️ Bez vlastní GABA neudělá NIC",
     "→ ⚠️ MÁ STROP účinku", "Samo o sobě jen výjimečně zabije"],
    "BARBITURÁT",
    ["Prodlužuje DOBU otevření", "⚠️ Ve vyšší dávce otevře kanál I BEZ GABA",
     "→ ⚠️ NEMÁ STROP, nemá antidotum", "Proto se přestal používat na spaní"],
    titulek="Proč barbiturát zabíjí a benzodiazepin (skoro) ne",
    pozn="Z-hypnotika (zolpidem) míří na podjednotku α1 → uspí bez myorelaxace; "
         "⚠️ parasomnie — noční jedení a chození s amnézií.", a_kind="zvyrazni"))

N("52", "Benzodiazepiny", cil(
    "BENZODIAZEPIN pozitivní modulátor GABA-A",
    [("ANXIOLÝZA", "zvyrazni"), ("SEDACE a HYPNÓZA", "zvyrazni"),
     ("ANTIKONVULZE — status epilepticus", "zvyrazni"),
     ("MYORELAXACE", "zvyrazni"),
     ("⚠️ ANTEROGRÁDNÍ AMNÉZIE (proto midazolam před výkonem)", "normal"),
     ("⚠️ Tolerance, závislost, rebound", "pozor")],
    titulek="Pět účinků najednou — a nedají se od sebe oddělit",
    pozn="⚠️ LOT — lorazepam, oxazepam, temazepam — se jen konjugují (bez fáze I) → bezpečné "
         "u jater a u seniorů. Antidotum FLUMAZENIL, ⚠️ opatrně: u závislého vyvolá křeče."))

N("53", "Antiepileptika", vetev(
    "JAK ZTIŠIT NADMĚRNÝ VÝBOJ NEURONŮ",
    [("zavřít Na⁺ kanály", "fenytoin · karbamazepin · lamotrigin · valproát", "normal"),
     ("zavřít T-Ca²⁺ kanály", "⚠️ ETHOSUXIMID — jen absence", "normal"),
     ("zesílit GABA", "benzodiazepiny · barbituráty · vigabatrin", "normal"),
     ("tlumit glutamát / SV2A", "topiramát · perampanel · levetiracetam", "normal")],
    titulek="Čtyři mechanismy — z nich si zástupce odvodíš",
    pozn="⚠️ FENYTOIN: HYPERPLAZIE GINGIVY (stejně jako cyklosporin a nifedipin) + nelineární "
         "kinetika. ⚠️ VALPROÁT je nejsilnější teratogen. ⚠️ KARBAMAZEPIN: autoindukce, "
         "hyponatremie, HLA-B*1502 → Stevensův–Johnsonův syndrom."))

N("54", "Antiparkinsonika", retez(
    [("LEVODOPA polknutá", "zvyrazni"),
     ("⚠️ na PERIFERII se hned mění na dopamin → nauzea, hypotenze", "pozor"),
     ("+ KARBIDOPA / BENSERAZID ⚠️ ty do mozku NEPROJDOU", "zvyrazni"),
     ("do mozku dorazí víc levodopy → dopamin TAM, kde chybí", "normal")],
    titulek="Proč se levodopa nikdy nedává samotná",
    pozn="⚠️ Dopamin sám hematoencefalickou bariéru neprojde, levodopa ano. "
         "⚠️ Parkinsonikovi se NESMÍ dát metoklopramid ani klasické antipsychotikum — "
         "blokují D2; bezpečný je domperidon."))

N("55", "Neuroleptika (antipsychotika)", vetev(
    "BLOKÁDA RECEPTORŮ D2 lék neumí rozlišit dráhy",
    [("MEZOLIMBICKÁ", "⭐ ÚČINEK — halucinace a bludy ustoupí", "zvyrazni"),
     ("MEZOKORTIKÁLNÍ", "⚠️ ZHORŠÍ negativní příznaky a kognici", "pozor"),
     ("NIGROSTRIATÁLNÍ", "⚠️ EXTRAPYRAMIDOVÉ nežádoucí účinky", "pozor"),
     ("TUBEROINFUNDIBULÁRNÍ", "⚠️ HYPERPROLAKTINEMIE — dopamin je brzda prolaktinu", "pozor")],
    titulek="Jedna blokáda je léčba, tři jsou nežádoucí účinky",
    pozn="🔑 V pořadí, jak přicházejí: hodiny → dystonie · dny → akatizie · týdny → "
         "parkinsonismus · ⚠️ měsíce až roky → TARDIVNÍ DYSKINEZE (často nevratná, "
         "v orofaciální oblasti). ⚠️ Klozapin = nejúčinnější u rezistence, ale agranulocytóza."))

N("56", "Antidepresiva — tricyklická, inhibitory MAO", cil(
    "TRICYKLICKÉ ANTIDEPRESIVUM „špinavý\" lék",
    [("blok reuptake NA a 5-HT ⭐ tohle je žádaný účinek", "zvyrazni"),
     ("⚠️ blok M → XEROSTOMIE → KAZ, zácpa, retence", "pozor"),
     ("⚠️ blok H1 → sedace, přírůstek hmotnosti", "pozor"),
     ("⚠️ blok α1 → ortostáza, pády", "pozor"),
     ("⚠️ blok Na⁺ v srdci → ARYTMIE = příčina smrti", "pozor"),
     ("⚠️ zásoba na 14 dní může být smrtelná dávka", "pozor")],
    titulek="Jeden žádaný účinek a čtyři nežádoucí ze čtyř dalších receptorů",
    pozn="⚠️ IMAO: sýrová reakce s tyraminem; s SSRI serotoninový syndrom. "
         "Rozlišení: serotoninový má HYPERreflexii a myoklonus, neuroleptický RIGIDITU."))

N("57", "Antidepresiva — SSRI, SNRI, atypická", retez(
    [("nasazení SSRI", "zvyrazni"), ("1.–2. týden: ⚠️ vrátí se ENERGIE", "pozor"),
     ("2.–4. týden: zlepší se NÁLADA", "normal"), ("plný účinek", "zvyrazni")],
    titulek="Past latence — hybnost se upraví dřív než nálada",
    pozn="⚠️ Proto na začátku léčby STOUPÁ riziko sebevraždy: pacient už má sílu jednat, "
         "ale ještě má depresivní myšlenky. ⚠️ Zubařsky: SSRI vyprázdní serotonin "
         "z trombocytů → DELŠÍ KRVÁCENÍ PO EXTRAKCI, zvlášť s NSA."))

N("58", "Anxiolytika, stabilizátory nálady", cil(
    "LITHIUM ⚠️ terapeutické rozmezí 0,6–1,2 mmol/l",
    [("⚠️ Vylučuje se VÝHRADNĚ LEDVINAMI", "pozor"),
     ("⚠️ NSA zvednou hladinu", "pozor"),
     ("⚠️ ACE inhibitory a sartany zvednou hladinu", "pozor"),
     ("⚠️ Thiazidy a dehydratace zvednou hladinu", "pozor"),
     ("NÚ: třes, polyurie, hypotyreóza", "normal"),
     ("⚠️ Teratogen — Ebsteinova anomálie", "pozor")],
    titulek="Nejužší terapeutické okno v psychiatrii",
    pozn="Při nedostatku sodíku si ledvina lithium plete se sodíkem a šetří ho. "
         "Anxiolytika: BZD jen krátkodobě, dlouhodobě SSRI; buspiron nenávykový, ale pomalý."))

N("59", "Farmakoterapie Alzheimerovy choroby, nootropika", srovnani(
    "INHIBITORY AChE",
    ["Donepezil, rivastigmin, galantamin", "Lehké až středně těžké stadium",
     "⚠️ NÚ = SLUDGE nasvětlejší formě:", "hypersalivace, průjem, bradykardie"],
    "⚠️ CO NEDÁVAT",
    ["⚠️ Anticholinergika (oxybutynin!)", "— ruší si tím vlastní léčbu",
     "⚠️ Benzodiazepiny a klasická antipsychotika", "zhorší kognici a zvyšují úmrtnost"],
    titulek="Léčba je přesný opak anticholinergik — a proto se nesmí kombinovat",
    pozn="Memantin (NMDA) u těžších stadií. ⚠️ Nic z toho nemoc nezastaví. "
         "Nootropika (piracetam, ginkgo) mají slabou až žádnou evidenci.", a_kind="zvyrazni"))

N("60", "Opium a jeho alkaloidy", srovnani(
    "CO SE TOLERUJE",
    ["Analgezie", "Euforie", "⚠️ Útlum dechu", "Nauzea"],
    "⚠️ CO SE NETOLERUJE NIKDY",
    ["⚠️ MIÓZA — proto je diagnostická", "⚠️ ZÁCPA — proto se laxativum",
     "nasazuje SOUČASNĚ s opioidem", "a nikdy až potom"],
    titulek="Co při dlouhodobém podávání povolí a co ne",
    pozn="⚠️ Příčina smrti = útlum dechového centra (klesne citlivost k CO₂). Antidotum "
         "NALOXON má ⚠️ kratší poločas než morfin → musí se opakovat. Papaverin a noskapin "
         "(isochinolinové) analgezii ani závislost nedělají.", a_kind="normal"))

N("61", "Deriváty a náhražky morfinu", stupnice(
    [("SILNÉ — plní agonisté μ", "fentanyl (100× morfin), sufentanil, oxykodon, metadon", "zvyrazni"),
     ("PARCIÁLNÍ — buprenorfin", "⚠️ má strop dechového útlumu, ale naloxon ho těžko vytlačí", "normal"),
     ("SLABÉ — kodein, tramadol", "⚠️ tramadol: + reuptake 5-HT/NA → serotoninový sy, křeče", "normal"),
     ("ANTAGONISTÉ", "naloxon i.v. · naltrexon p.o. · ⚠️ methylnaltrexon jen na zácpu", "pozor")],
    titulek="Řazení podle síly a podle chování na receptoru",
    sipka_popis="klesající síla",
    pozn="⚠️ Petidin → metabolit norpetidin dráždí CNS (křeče), smrtelná interakce s IMAO. "
         "⚠️ Metadon prodlužuje QT. ⚠️ Fentanyl i.v. rychle → rigidita hrudní stěny."))

N("62", "Eikosanoidy", vetev(
    "KYSELINA ARACHIDONOVÁ ⚠️ o patro výš ji blokují KORTIKOIDY (fosfolipáza A₂)",
    [("COX — ⚠️ tady blokují NSA", "prostaglandiny · prostacyklin · tromboxan", "normal"),
     ("LOX — ⚠️ NSA sem NESAHAJÍ", "LEUKOTRIENY — stah průdušek, hlen", "pozor")],
    titulek="Dvě větve — a proč kortikoid funguje šířeji než NSA",
    pozn="⚠️ Zavřeš COX → kyselina se PŘELIJE do větve leukotrienů → ASPIRINEM INDUKOVANÉ "
         "ASTMA (Samterova trias: astma + nosní polypy + intolerance aspirinu). "
         "COX-1 = žaludeční hlen, tromboxan, ledviny. COX-2 = zánět."))

N("63", "Analgetika-antipyretika", retez(
    [("PARACETAMOL", "zvyrazni"), ("90 % konjugace → neškodné", "normal"),
     ("10 % CYP2E1 → ⚠️ NAPQI", "pozor"),
     ("GLUTATHION ⚠️ dokud vydrží", "zvyrazni")],
    titulek="Celá otrava paracetamolem v jednom řádku",
    pozn="⚠️ Alkoholik má obojí proti sobě: indukovaný CYP2E1 (víc NAPQI) A vyčerpaný "
         "glutathion. ⚠️ Příznaky přijdou až za 1–3 dny — rozhoduje HLADINA V ČASE, ne stav "
         "pacienta. Antidotum N-ACETYLCYSTEIN. ⚠️ Po extrakci je ibuprofen účinnější než "
         "paracetamol; nejlepší je jejich kombinace."))

N("64", "Nesteroidní antiflogistika", cil(
    "BLOKÁDA COX-1 tam, kde ji tělo POTŘEBUJE",
    [("ŽALUDEK — ⚠️ vřed a krvácení (prevence PPI)", "pozor"),
     ("LEDVINA — ⚠️ zruší vazodilataci přívodné tepénky", "pozor"),
     ("DESTIČKY — ⚠️ méně tromboxanu → krvácivost", "pozor"),
     ("⚠️ Aspirin acetyluje IREVERZIBILNĚ → účinek 7–10 dní", "zvyrazni"),
     ("⚠️ Reyeův syndrom u dětí s virózou", "pozor"),
     ("⚠️ Koxiby šetří žaludek, ale zvyšují KV riziko", "pozor")],
    titulek="Skoro všechny nežádoucí účinky plynou z blokády COX-1",
    pozn="⚠️ „Triple whammy\": NSA + ACE inhibitor + diuretikum = akutní selhání ledvin. "
         "⚠️ Ibuprofen ruší antiagregační účinek aspirinu — obsadí COX-1 dřív."))

N("65", "Farmakoterapie migrény", srovnani(
    "AKUTNĚ — hned na začátku záchvatu",
    ["NSA nebo paracetamol", "⚠️ + METOKLOPRAMID — nejen proti nevolnosti,",
     "ale aby se analgetikum vůbec vstřebalo", "TRIPTANY (5-HT1B/1D) ⚠️ KI u ICHS"],
    "PROFYLAXE — při 4+ záchvatech měsíčně",
    ["Betablokátory, topiramát, amitriptylin", "Kandesartan, flunarizin, valproát",
     "⚠️ Protilátky proti CGRP", "⚠️ Hodnotí se až po 2–3 měsících"],
    titulek="Dvě zcela oddělené léčby, které se nesmí zaměnit",
    pozn="⚠️ Analgetika víc než 10–15 dní v měsíci → bolest hlavy Z NADUŽÍVÁNÍ LÉKŮ. "
         "Řešením je vysazení, ne přidání. ⚠️ Migréna s aurou = KI kombinované antikoncepce.",
    b_kind="zvyrazni"))

N("66", "Léčiva s pozitivně inotropním účinkem, digoxin", retez(
    [("DIGOXIN zablokuje Na⁺/K⁺-ATPázu", "zvyrazni"),
     ("sodíku uvnitř PŘIBUDE", "normal"),
     ("výměník Na⁺/Ca²⁺ přestane vyvážet vápník", "normal"),
     ("⚠️ VÍC VÁPNÍKU → SILNĚJŠÍ STAH", "zvyrazni")],
    titulek="Proč blokáda sodíkové pumpy posílí stah srdce",
    pozn="⚠️ HYPOKALEMIE ZVYŠUJE TOXICITU — draslík a digoxin soutěží o stejné místo na "
         "pumpě. A hypokalemii dělají diuretika, která má srdeční pacient skoro vždy. "
         "Otrava: nauzea · ⚠️ ŽLUTÉ VIDĚNÍ · arytmie. Antidotum: protilátky (Fab)."))

N("67", "Antiarytmika", stupnice(
    [("I. — blokátory Na⁺ kanálů", "IA chinidin · IB LIDOKAIN (komorové) · ⚠️ IC propafenon", "normal"),
     ("II. — BETABLOKÁTORY", "⚠️ jediná třída, která prokazatelně snižuje úmrtnost", "zvyrazni"),
     ("III. — blokátory K⁺ kanálů", "AMIODARON, sotalol · ⚠️ prodlužují QT → torsades", "pozor"),
     ("IV. — blokátory Ca²⁺ kanálů", "verapamil, diltiazem", "normal"),
     ("MIMO KLASIFIKACI", "⚠️ ADENOSIN (poločas vteřiny) · digoxin · magnezium · ivabradin", "normal")],
    titulek="Vaughanova–Williamsova klasifikace podle blokovaného kanálu",
    sipka_popis="I. až IV. třída",
    pozn="⚠️ KAŽDÉ ANTIARYTMIKUM MŮŽE ARYTMII TAKÉ VYVOLAT (studie CAST: třída IC po "
         "infarktu zvýšila úmrtnost). ⚠️ Amiodaron obsahuje jód → tyreopatie, plicní "
         "fibróza, usazeniny v rohovce, poločas v týdnech."))

N("68", "ACE inhibitory a antagonisté angiotensinu", vetev(
    "ACE = enzym se dvěma úkoly",
    [("tvoří ANGIOTENSIN II", "stah cév, aldosteron, remodelace → ⚠️ tohle chceme zastavit", "normal"),
     ("⚠️ rozkládá BRADYKININ", "ACE inhibitor to zastaví taky → ⚠️ SUCHÝ KAŠEL, ANGIOEDÉM", "pozor"),
     ("SARTAN blokuje až receptor AT1", "⚠️ bradykinin neovlivní → BEZ KAŠLE", "zvyrazni")],
    titulek="Proč po ACE inhibitoru kašel je a po sartanu ne",
    pozn="⚠️ Renoprotekce: uvolní se ODVODNÁ tepénka → klesne tlak v glomerulu → přestane "
         "se ničit. Mírný vzestup kreatininu na začátku je proto žádaný, ne selhání. "
         "⚠️ KI: gravidita, oboustranná stenóza renálních tepen, hyperkalemie."))

N("69", "Diuretika", stupnice(
    [("PROXIMÁLNÍ TUBULUS", "acetazolamid (⚠️ acidóza, glaukom) · mannitol (mozkový edém)", "tichy"),
     ("HENLEOVA KLIČKA — vzestupné raménko", "⚠️ FUROSEMID — NEJSILNĚJŠÍ, ⚠️ ZTRÁCÍ VÁPNÍK, ototoxicita", "zvyrazni"),
     ("DISTÁLNÍ TUBULUS", "THIAZIDY — ⚠️ ŠETŘÍ VÁPNÍK, ⚠️ hyperurikemie a hyperglykemie", "normal"),
     ("SBĚRACÍ KANÁLEK", "⚠️ KALIUM ŠETŘÍCÍ: spironolakton, eplerenon, amilorid", "normal")],
    titulek="Nefron shora dolů — místo účinku určuje sílu i minerálovou poruchu",
    sipka_popis="průtok nefronem",
    pozn="🔑 Furosemid vápník VYPLAVÍ, thiazid ho ZADRŽÍ. ⚠️ Všechna kromě posledního patra "
         "ztrácejí draslík — odtud konflikt s digoxinem."))

N("70", "Blokátory kalciových kanálů", srovnani(
    "DIHYDROPYRIDINY (-dipin)",
    ["Amlodipin, nifedipin, lerkanidipin", "⚠️ Míří hlavně na CÉVY → snižují tlak",
     "NÚ: otoky kotníků, návaly, reflexní tep", "⚠️ HYPERPLAZIE GINGIVY"],
    "VERAPAMIL a DILTIAZEM",
    ["⚠️ Míří hlavně na SRDCE", "Bradykardie, slabší stah, zácpa",
     "⚠️ NEKOMBINOVAT s betablokátorem → AV blok", "⚠️ KI u srdečního selhání"],
    titulek="Dvě skupiny, dva různé cíle — a z toho plyne, co se nesmí kombinovat",
    pozn="⚠️ VE ZDROJI JSOU DVĚ CHYBY: diltiazem je BENZOTHIAZEPIN (ne benzodiazepin) "
         "a verapamil se použije při kontraindikaci β-ANTAGONISTŮ (ne β-agonistů). "
         "⚠️ Otoky kotníků nejsou z retence — diuretikum na ně nepomůže.", a_kind="normal"))

N("71", "Nitrity a nitráty", retez(
    [("NITRÁT uvolní NO", "zvyrazni"), ("↑ cGMP → uvolnění hladkého svalu", "normal"),
     ("⚠️ hlavně ŽILY — krev se „zaparkuje\"", "zvyrazni"),
     ("↓ předtížení → srdce potřebuje MÍŇ KYSLÍKU", "normal")],
    titulek="Nerozšiřují hlavně věnčité tepny — rozšiřují ŽÍLY",
    pozn="⚠️ TOLERANCE: nutný denní nitrátový interval 8–12 hodin. ⚠️ ABSOLUTNÍ KI: "
         "sildenafil a spol. — obojí zvyšuje cGMP, sečte se to a tlak spadne nezvratně. "
         "Nitroglycerin se ⚠️ nepolyká (first-pass), dává se pod jazyk vsedě."))

N("72", "Farmakoterapie srdečního selhání", srovnani(
    "⭐ PRODLUŽUJÍ ŽIVOT — čtyři pilíře",
    ["ACE inhibitor / sartan → nejlépe ARNI", "BETABLOKÁTOR (jen 4 z nich, pomalu titrovat)",
     "Antagonista aldosteronu (spironolakton)", "GLIFLOZIN — ⚠️ i u nediabetika"],
    "JEN ULEVÍ — prognózu nemění",
    ["Diuretika (furosemid)", "Digoxin", "Ivabradin (snižuje hospitalizace)",
     "⚠️ NEDÁVAT: NSA, verapamil, glitazony"],
    titulek="Nejdůležitější rozlišení celé kardiologie",
    pozn="⚠️ Proč tlumíme srdce, které nestačí? Protože chronická aktivace sympatiku a RAAS "
         "myokard přestavuje a ničí. Proto se betablokátor nasazuje pomalu a stav se "
         "může na začátku přechodně zhoršit.", b_kind="normal"))

N("73", "Farmakoterapie ischemické choroby srdeční", srovnani(
    "⭐ ZLEPŠUJÍ PROGNÓZU",
    ["Antiagregancia", "Statin", "ACE inhibitor", "Betablokátor"],
    "JEN ULEVÍ OD ANGÍNY",
    ["Nitráty", "Ivabradin", "Trimetazidin, ranolazin", "Blokátory kalciových kanálů"],
    titulek="U chronické ICHS rozlišuj prognostickou a úlevovou léčbu",
    pozn="⚠️ Betablokátor uleví tím, že zpomalí tep → prodlouží diastolu → věnčité tepny se "
         "plní právě v diastole. ⚠️ Duální antiagregace po stentu obvykle 12 měsíců — "
         "plánovanou extrakci v té době raději odložit, léky nevysazovat.", b_kind="normal"))

N("74", "Antihypertenziva", cil(
    "JAKÝ LÉK PODLE PACIENTA?",
    [("diabetik / proteinurie → ACE inhibitor, sartan", "zvyrazni"),
     ("po infarktu → betablokátor + ACE inhibitor", "zvyrazni"),
     ("senior, izolovaná systolická → blokátor Ca, thiazid", "normal"),
     ("⚠️ dna → NE thiazid", "pozor"),
     ("⚠️ astma → NE betablokátor", "pozor"),
     ("⚠️ GRAVIDITA → methyldopa, labetalol, nifedipin — NE ACEI a sartany", "pozor")],
    titulek="Hypertenze se neléčí podle čísla, ale podle toho, kdo ji má",
    pozn="⚠️ Raději kombinovat nízké dávky několika léků v jedné tabletě než jeden vyhnat "
         "do maxima — účinek se sečte a nežádoucí účinky ne."))

N("75", "Farmakoterapie aterosklerózy, hyperlipidemie", retez(
    [("STATIN blokuje HMG-CoA reduktázu", "zvyrazni"),
     ("játra vyrobí míň cholesterolu", "normal"),
     ("nahustí si LDL RECEPTORY", "normal"),
     ("vytáhnou LDL z krve + ⚠️ STABILIZUJE PLÁT", "zvyrazni")],
    titulek="Statin nesnižuje jen číslo — stabilizuje plát, který by praskl",
    pozn="⚠️ Myopatie až rabdomyolýza: bolest svalů + tmavá moč + vysoká kreatinkináza. "
         "⚠️ Riziko roste s makrolidy, azoly, verapamilem, fibráty a grapefruitem "
         "(inhibitory CYP3A4). Ezetimib blokuje vstřebávání, inhibitory PCSK9 jsou "
         "injekční protilátky, fibráty míří na triacylglyceroly."))

N("76", "Parenterální antikoagulancia", vetev(
    "HEPARIN sám neúčinkuje — ⚠️ 1000× zesílí ANTITROMBIN III",
    [("NEFRAKCIONOVANÝ dlouhý řetězec", "⚠️ IIa i Xa · aPTT · ⚠️ antidotum PROTAMIN", "normal"),
     ("NÍZKOMOLEKULÁRNÍ enoxaparin", "⚠️ hlavně Xa · s.c. · bez rutinní monitorace", "zvyrazni"),
     ("FONDAPARINUX pentasacharid", "⚠️ výhradně Xa · ⚠️ NEDĚLÁ HIT", "normal")],
    titulek="Čím kratší řetězec, tím výhradněji míří na faktor Xa",
    pozn="⚠️ HIT: protilátky proti komplexu heparinu a PF4 destičky ubírají A ZÁROVEŇ "
         "AKTIVUJÍ → málo destiček a přitom TROMBÓZY. ⚠️ Nikdy nepodávat destičky — "
         "vysadit heparin a nasadit jiné antikoagulans. ⚠️ Hepariny NEPROCHÁZEJÍ "
         "PLACENTOU → volba v graviditě."))

N("77", "Perorální antikoagulancia", retez(
    [("WARFARIN nasazen", "zvyrazni"),
     ("⚠️ nejdřív klesne PROTEIN C — má nejkratší poločas", "pozor"),
     ("⚠️ pacient je přechodně PROTROMBOGENNÍ", "pozor"),
     ("⚠️ proto se PŘEKRÝVÁ HEPARINEM, dokud INR nedosáhne cíle", "zvyrazni")],
    titulek="Proč warfarin první dny paradoxně zvyšuje srážlivost",
    pozn="Blokuje γ-karboxylaci faktorů 🔑 II, VII, IX, X („1972\") — ale i proteinů C a S. "
         "⚠️ Zubařsky: PŘED BĚŽNOU EXTRAKCÍ SE NEVYSAZUJE, pokud je INR v rozmezí — "
         "řeší se místní hemostázou. DOAC: -xaban blokuje Xa, dabigatran trombin; "
         "⚠️ nesmí u mechanické chlopně."))

N("78", "Fibrinolytika, trombolytika, hemostatika", srovnani(
    "TROMBOLÝZA — rozpustit sraženinu",
    ["Alteplasa, tenektaplasa, streptokináza", "Aktivují plazminogen → plazmin → fibrin",
     "STEMI bez katetrizace, plicní embolie", "⚠️ CMP jen do 4,5 hodiny"],
    "HEMOSTÁZA — zastavit krvácení",
    ["Vitamin K · ⚠️ kyselina TRANEXAMOVÁ", "⚠️ DESMOPRESIN (vyplaví vWF a f. VIII)",
     "⚠️ Místně: oxidovaná celulóza,", "kolagenová houbička, fibrinové lepidlo, šití"],
    titulek="Dvě protilehlé poloviny jedné otázky",
    pozn="⚠️ Ve zdroji je chyba: hemofilie A je VROZENÝ dědičný defekt faktoru VIII vázaný "
         "na X, ne „získaná geneticky\". Extrakce u hemofilika se domlouvá předem "
         "s hematologem a ⚠️ nikdy NSA na bolest.", b_kind="zvyrazni"))

N("79", "Antiagregancia", srovnani(
    "TEPNA — rychlý proud",
    ["Sraženina hlavně z DESTIČEK", "→ ⚠️ ANTIAGREGANCIA",
     "Aspirin · klopidogrel, tikagrelor", "Inhibitory GPIIb/IIIa v katetrizaci"],
    "ŽÍLA — pomalý proud",
    ["Sraženina hlavně z FIBRINU", "→ ⚠️ ANTIKOAGULANCIA",
     "Warfarin, DOAC, hepariny", "Jiná indikace, jiné léky"],
    titulek="Proč se na tepnu a na žílu dávají úplně jiné léky",
    pozn="⚠️ Aspirin acetyluje COX-1 IREVERZIBILNĚ; destička nemá jádro → účinek trvá "
         "7–10 dní. ⚠️ Klopidogrel je proléčivo (CYP2C19 — omeprazol ho oslabí). "
         "⚠️ Zubařsky: aspirin se před extrakcí NEVYSAZUJE.", a_kind="zvyrazni", b_kind="normal"))

N("80", "Inzulin, jeho analoga a glukagon", stupnice(
    [("RYCHLÁ ANALOGA lispro, aspart", "nástup ~15 min → k jídlu (bolus)", "zvyrazni"),
     ("KRÁTKÝ HUMÁNNÍ regular", "⚠️ nástup ~30 min → píchat s předstihem", "normal"),
     ("STŘEDNÍ NPH", "překlenovací", "normal"),
     ("DLOUHÁ ANALOGA glargin, degludek", "⚠️ bez vrcholu → bazál", "zvyrazni")],
    titulek="Režim bazál-bolus napodobuje fyziologii",
    sipka_popis="delší účinek",
    pozn="⚠️ Hlavní nebezpečí = HYPOGLYKEMIE. ⚠️ Betablokátor maskuje třes a bušení srdce, "
         "POCENÍ ZŮSTANE (cholinergní) a bývá jediným varováním. Glukagon i.m. u bezvědomí "
         "— ⚠️ a zároveň antidotum předávkování betablokátory."))

N("81", "Perorální antidiabetika", srovnani(
    "⚠️ DĚLAJÍ HYPOGLYKEMII",
    ["Sulfonylurea (glimepirid, gliklazid)", "— uzavře KATP kanál a vyplaví inzulin",
     "bez ohledu na glykemii", "Glinidy · (a samozřejmě inzulin)"],
    "NEDĚLAJÍ HYPOGLYKEMII",
    ["⭐ METFORMIN — lék první volby", "Gliptiny · GLP-1 agonisté (hubnutí)",
     "⚠️ GLIFLOZINY — ochrana srdce a ledvin", "Akarbóza, pioglitazon"],
    titulek="Nejpraktičtější rozdělení antidiabetik",
    pozn="⚠️ Metformin: vysadit před jodovou kontrastní látkou a při akutním stavu — "
         "laktátová acidóza. ⚠️ Glifloziny: glykosurie → mykotické infekce a euglykemická "
         "ketoacidóza.", a_kind="pozor", b_kind="zvyrazni"))

N("82", "Principy antibiotické terapie", cil(
    "BAKTERIÁLNÍ BUŇKA jeden obrázek na otázky 82–88",
    [("BUNĚČNÁ STĚNA ⚠️ člověk ji NEMÁ betalaktamy, glykopeptidy", "zvyrazni"),
     ("MEMBRÁNA polymyxiny, daptomycin", "normal"),
     ("RIBOZOM 30S aminoglykosidy, TETRACYKLINY", "zvyrazni"),
     ("RIBOZOM 50S makrolidy, KLINDAMYCIN, amfenikoly", "zvyrazni"),
     ("DNA chinolony → ⚠️ TOPOIZOMERÁZA · rifampicin · metronidazol", "normal"),
     ("KYSELINA LISTOVÁ sulfonamid + trimethoprim", "normal")],
    titulek="Selektivní toxicita: zasáhnout to, co bakterie má a člověk ne",
    pozn="⚠️ Koncentračně závislé (aminoglykosidy, chinolony) → velká dávka 1× denně. "
         "Časově závislé (betalaktamy) → rozdělit do více dávek. Rezistence: betalaktamázy, "
         "změna cíle, efluxní pumpy, nižší propustnost."))

N("83", "Peniciliny, inhibitory betalaktamáz", vetev(
    "PENICILINY blokáda stavby buněčné stěny ⚠️ jen na DĚLÍCÍ SE bakterie",
    [("PŘIROZENÉ", "⚠️ PENICILIN V — lék volby u odontogenních infekcí", "zvyrazni"),
     ("PROTISTAFYLOKOKOVÉ", "oxacilin — odolný vůči stafylokokové betalaktamáze", "normal"),
     ("AMINOPENICILINY", "amoxicilin ⚠️ + kyselina klavulanová", "normal"),
     ("UREIDOPENICILINY", "piperacilin + tazobaktam → Pseudomonas", "normal")],
    titulek="Řada od nejužšího po nejširší spektrum",
    pozn="⚠️ Inhibitor betalaktamázy sám skoro neúčinkuje — obětuje se enzymu. "
         "⚠️ Ampicilinový exantém u infekční mononukleózy NENÍ alergie. "
         "⚠️ Člověk buněčnou stěnu nemá → hlavním rizikem je alergie, ne toxicita."))

N("84", "Cefalosporiny, karbapenemy, monobaktamy", stupnice(
    [("I. generace — cefazolin, cefalexin", "grampozitivní · chirurgická profylaxe", "normal"),
     ("II. — cefuroxim", "+ Haemophilus, respirační infekce", "normal"),
     ("III. — ceftriaxon, ceftazidim", "⚠️ gramnegativní · PROSTUP DO CNS → meningitidy", "zvyrazni"),
     ("IV.–V. — cefepim, ceftarolin", "⚠️ ceftarolin jako jediný i na MRSA", "normal"),
     ("KARBAPENEMY — meropenem", "⚠️ nejširší spektrum → REZERVA, dál už není kam ustoupit", "pozor")],
    titulek="Čím vyšší generace, tím míň G+ a víc G−",
    sipka_popis="generace",
    pozn="⚠️ ŽÁDNÝ cefalosporin nepůsobí na ENTEROKOKY ani na ATYPICKÉ patogeny. "
         "⚠️ Aztreonam (monobaktam) je natolik odlišný, že ho lze podat i při alergii "
         "na penicilin."))

N("85", "Aminoglykosidy, chinolony", srovnani(
    "AMINOGLYKOSIDY",
    ["⚠️ 30S ribozom, ale BAKTERICIDNÍ (výjimka)", "⚠️ Nevstřebají se ústy → jen injekčně",
     "⚠️ NEFROTOXICITA (vratná)", "⚠️ OTOTOXICITA — často TRVALÁ"],
    "CHINOLONY",
    ["⚠️ TOPOIZOMERÁZA II (gyráza) a IV", "⚠️ Ruptura Achillovy šlachy",
     "⚠️ KI u dětí a v graviditě (chrupavky)", "⚠️ Chelatace s Ca, Mg, Fe → ne s mlékem"],
    titulek="Dvě baktericidní, koncentračně závislé skupiny — každá s vlastní toxicitou",
    pozn="⚠️ VE ZDROJI JE CHYBA: chinolony neblokují DNA-polymerázu, ale TOPOIZOMERÁZU "
         "(DNA-gyrázu). ⚠️ Aminoglykosidy se dávkují 1× denně — vysoký vrchol zabíjí líp "
         "a dlouhá pauza chrání ledvinu.", a_kind="pozor"))

N("86", "Linkosamidy, glykopeptidy, polymyxiny", cil(
    "KLINDAMYCIN zubařsky nejdůležitější z téhle trojice",
    [("⚠️ Výborný průnik do KOSTI", "zvyrazni"),
     ("⚠️ Účinný na ANAEROBY", "zvyrazni"),
     ("→ odontogenní absces, osteomyelitida čelisti", "zvyrazni"),
     ("→ ⚠️ alternativa při alergii na penicilin", "zvyrazni"),
     ("⚠️ RIZIKO: pseudomembranózní kolitida (C. difficile)", "pozor"),
     ("léčí se ⚠️ vankomycinem PERORÁLNĚ nebo fidaxomicinem", "normal")],
    titulek="Proč právě klindamycin u infekcí čelisti",
    pozn="Vankomycin: ⚠️ jen G+, lék volby u MRSA; ⚠️ perorálně se nevstřebá — proto se tak "
         "podává právě na klostridiovou kolitidu. ⚠️ „Red man syndrome\" při rychlé infuzi "
         "není alergie. Kolistin = rezerva na multirezistentní G−, nefrotoxický."))

N("87", "Tetracykliny, amfenikoly", retez(
    [("TETRACYKLIN se váže na VÁPNÍK", "zvyrazni"),
     ("ukládá se do rostoucí kosti a ZUBU", "normal"),
     ("⚠️ ŠEDOHNĚDÉ ZBARVENÍ UVNITŘ skloviny a dentinu", "pozor"),
     ("⚠️ NEDÁ SE VYBĚLIT — barvivo není na povrchu", "pozor")],
    titulek="Nejznámější zubařský nežádoucí účinek v celé farmakologii",
    pozn="⚠️ VE ZDROJI JE CHYBA: tetracykliny NEBLOKUJÍ buněčnou stěnu, ale RIBOZOM (30S). "
         "⚠️ KI do 8 let a v graviditě. ⚠️ Nezapíjet mlékem (chelatace). Amfenikoly: "
         "⚠️ aplastická anemie nezávislá na dávce a gray baby syndrom."))

N("88", "Makrolidy", srovnani(
    "ERYTHROMYCIN a KLARITHROMYCIN",
    ["⚠️ SILNÉ INHIBITORY CYP3A4", "→ ⚠️ statin (rabdomyolýza), warfarin,",
     "cyklosporin, karbamazepin", "⚠️ Erythromycin dráždí žaludek (motilin)"],
    "AZITHROMYCIN",
    ["🔑 CYP3A4 prakticky neinhibuje", "→ volba u polymorbidního pacienta",
     "⚠️ Velmi dlouhý tkáňový poločas", "→ třídenní kúra působí ještě dny"],
    titulek="Největší úskalí makrolidů nejsou nežádoucí účinky, ale interakce",
    pozn="⚠️ 50S ribozom, bakteriostatické, pokrývají atypické patogeny a jsou alternativou "
         "při alergii na penicilin. ⚠️ Prodlužují QT.", a_kind="pozor", b_kind="zvyrazni"))


# ═══════════════════════════════════════════ SPECKA II  89–136

N("89", "Chemoterapeutika močových a střevních infekcí", retez(
    [("PABA", "normal"), ("dihydrofolát ⚠️ tady blokuje SULFONAMID", "pozor"),
     ("tetrahydrofolát ⚠️ tady blokuje TRIMETHOPRIM", "pozor"),
     ("DNA bakterie se nepostaví", "zvyrazni")],
    titulek="Sekvenční blokáda — dva zámky za sebou na jedné dráze",
    pozn="⚠️ Selektivita: člověk kyselinu listovou NEVYRÁBÍ, přijímá ji hotovou ze stravy. "
         "⚠️ Nitrofurantoin se koncentruje v moči, ale ne ve tkáni → jen dolní močové cesty. "
         "⚠️ Sulfonamid vytěsní bilirubin → jádrový ikterus novorozence."))

N("90", "Antiparazitika", cil(
    "METRONIDAZOL ⚠️ aktivuje se jen tam, kde NENÍ kyslík",
    [("Amébóza, giardióza, trichomoniáza", "normal"),
     ("⚠️ A NAVÍC ANAEROBNÍ BAKTERIE", "zvyrazni"),
     ("⚠️ Nekrotizující ulcerózní gingivitida", "zvyrazni"),
     ("⚠️ + amoxicilin u agresivní parodontitidy", "zvyrazni"),
     ("⚠️ DISULFIRAMOVÁ REAKCE S ALKOHOLEM", "pozor"),
     ("⚠️ Kovová chuť v ústech, tmavá moč", "pozor")],
    titulek="Nejužitečnější antiparazitikum pro zubaře",
    pozn="Antimalarika: artemisininové kombinace jsou dnes volbou; ⚠️ primachin na spící "
         "hypnozoity — ⚠️ hemolýza při deficitu G6PD. Antihelmintika: albendazol, mebendazol "
         "(blok mikrotubulů), praziquantel."))

N("91", "Antituberkulotika a antileprotika", stupnice(
    [("H — IZONIAZID", "⚠️ hepatotoxicita · ⚠️ NEUROPATIE → prevence PYRIDOXINEM (B6)", "normal"),
     ("R — RIFAMPICIN", "⚠️ SILNÝ INDUKTOR CYP → selže antikoncepce · ⚠️ ORANŽOVÁ moč a slzy", "pozor"),
     ("Z — PYRAZINAMID", "⚠️ hyperurikemie (dna), hepatotoxicita", "normal"),
     ("E — ETHAMBUTOL", "⚠️ RETROBULBÁRNÍ NEURITIDA → porucha barvocitu a ostrosti", "normal")],
    titulek="Režim 2 HRZE + 4 HR — a typická toxicita každého písmene",
    sipka_popis="čtyři léky první linie",
    pozn="⚠️ NIKDY monoterapie a NIKDY krátce — mykobakterie se pomalu dělí, sedí "
         "v makrofázích a rychle si vytvoří rezistenci. Pacient se cítí dobře po pár "
         "týdnech, ale léčba trvá 6 měsíců → kontrolované podávání."))

N("92", "Antimykotika", vetev(
    "HOUBA je EUKARYOTICKÁ buňka jako naše ⚠️ selektivita je proto těžká",
    [("MEMBRÁNA — ERGOSTEROL (člověk má cholesterol)", "polyeny (nystatin, amfotericin) · AZOLY", "zvyrazni"),
     ("STĚNA — β-GLUKAN (člověk ji nemá vůbec)", "ECHINOKANDINY → ⚠️ nejlépe snášené", "zvyrazni"),
     ("skvalenepoxidáza", "terbinafin → onychomykóza", "normal")],
    titulek="Dva cíle, na kterých stojí celá skupina",
    pozn="⚠️ Zubařsky: orální kandidóza → nystatin suspenze nebo mikonazolový gel, flukonazol "
         "systémově. ⚠️ Vždy hledat příčinu (inhalační kortikoid bez výplachu, protéza — "
         "musí se dezinfikovat, xerostomie, diabetes). ⚠️ I lokální mikonazol v ústech "
         "zvýší účinek warfarinu."))

N("93", "Antivirotika", retez(
    [("ACIKLOVIR neaktivní proléčivo", "zvyrazni"),
     ("⚠️ VIROVÁ THYMIDINKINÁZA ho fosforyluje ⚠️ ten enzym má JEN infikovaná buňka", "pozor"),
     ("buněčné kinázy dokončí na trifosfát", "normal"),
     ("zablokuje virovou DNA-polymerázu", "zvyrazni")],
    titulek="Nejelegantnější selektivní toxicita ve virologii",
    pozn="⚠️ Ve zdravé buňce zůstane aciklovir neaktivní a neškodný. ⚠️ Zubařsky: primární "
         "herpetická gingivostomatitida a herpes labialis — začít CO NEJDŘÍV, ideálně "
         "v prodromu; ⚠️ na herpetickou lézi nikdy kortikoid. Chřipka: oseltamivir do 48 h."))

N("94", "Antiretrovirotika", stupnice(
    [("VSTUP DO BUŇKY", "maravirok, enfuvirtid", "normal"),
     ("PŘEPIS RNA → DNA", "NRTI (tenofovir, ⚠️ abakavir — testuje se HLA-B*5701) · NNRTI", "normal"),
     ("VLOŽENÍ DO NAŠÍ DNA", "⚠️ INHIBITORY INTEGRÁZY — dolutegravir, dnešní základ", "zvyrazni"),
     ("DOZRÁVÁNÍ ČÁSTICE", "inhibitory proteázy + ⚠️ ritonavir jako „booster\"", "normal")],
    titulek="Životní cyklus viru a kde se do něj zasahuje",
    sipka_popis="cyklus HIV",
    pozn="⚠️ Vždy kombinace 3 léků ze 2 tříd — virus mutuje tak rychle, že proti jednomu "
         "léku vytvoří rezistenci během týdnů. ⚠️ U = U: nedetekovatelná nálož = nepřenosný. "
         "⚠️ PEP po poranění do 72 hodin, ideálně dřív."))

N("95", "Antitusika, mukolytika, expektorancia", srovnani(
    "ANTITUSIKUM — na SUCHÝ kašel",
    ["Butamirát (nenávykový), kodein,", "dextrometorfan",
     "Potlačí reflex", "⚠️ Ne u produktivního kašle"],
    "MUKOLYTIKUM — na PRODUKTIVNÍ kašel",
    ["N-acetylcystein (⚠️ štěpí disulfidy)", "Ambroxol, erdostein, ⚠️ dornáza alfa",
     "Zředí hlen, aby šel vykašlat", "⚠️ Ne u potlačeného kašle"],
    titulek="⚠️ Tyhle dvě skupiny se navzájem vylučují",
    pozn="Rozředíš hlen a zároveň potlačíš kašel → pacient ho nemá jak dostat ven a zůstane "
         "v průduškách. ⚠️ N-acetylcystein je zároveň antidotum otravy paracetamolem. "
         "⚠️ Dlouhý suchý kašel: pomysli na ACE inhibitor.", a_kind="normal"))

N("96", "Antiastmatika", srovnani(
    "ÚLEVOVÁ — podle potřeby",
    ["SABA salbutamol, SAMA ipratropium", "Systémový kortikoid u exacerbace",
     "⚠️ Rostoucí spotřeba = varovný signál", "Řeší příznak, ne zánět"],
    "⭐ KONTROLUJÍCÍ — denně",
    ["⭐ INHALAČNÍ KORTIKOID = základ", "LABA — ⚠️ NIKDY samotná bez kortikoidu",
     "LAMA, montelukast, teofylin", "Biologika u těžkého astmatu"],
    titulek="Základem astmatu není bronchodilatátor, ale protizánětlivá léčba",
    pozn="⚠️ Zubařsky: inhalační kortikoid → ORÁLNÍ KANDIDÓZA a chrapot → vyplachovat ústa "
         "a používat nástavec. ⚠️ Astmatik má mít inhalátor v ordinaci u sebe. "
         "⚠️ NSA jsou u Samterovy triády kontraindikovaná → paracetamol.",
    a_kind="normal", b_kind="zvyrazni"))

N("97", "Antihistaminika", srovnani(
    "I. GENERACE",
    ["⚠️ PROCHÁZÍ do mozku → SEDACE", "⚠️ Anticholinergní → XEROSTOMIE, zácpa",
     "Bisulepin, prometazin, hydroxyzin", "Využití: kinetóza, svědění, spaní"],
    "II. GENERACE",
    ["⚠️ NEPROCHÁZÍ do mozku", "Bez sedace, bez sucha v ústech",
     "Cetirizin, loratadin, bilastin", "⭐ Běžná léčba alergie"],
    titulek="Celá otázka stojí na jediné vlastnosti — projde lék do mozku?",
    pozn="⚠️ NEJDŮLEŽITĚJŠÍ VAROVÁNÍ: ANTIHISTAMINIKUM NESTAČÍ NA ANAFYLAXI. Tam je lékem "
         "první volby ADRENALIN i.m. ⚠️ H2 blokátory (famotidin) nepatří k alergii, "
         "ale k vředové chorobě.", a_kind="pozor", b_kind="zvyrazni"))

N("98", "Laxativa, antidiaroika", retez(
    [("LAKTULÓZA se ve střevě rozloží na kyseliny", "zvyrazni"),
     ("obsah střeva se OKYSELÍ", "normal"),
     ("NH₃ (projde) + H⁺ → ⚠️ NH₄⁺ (nabitý, NEPROJDE)", "pozor"),
     ("amoniak uvězněný ve střevě odejde stolicí", "zvyrazni")],
    titulek="Iontová past podruhé — proto laktulóza léčí jaterní encefalopatii",
    pozn="Laxativa: objemová · osmotická · stimulační (⚠️ ne dlouhodobě) · změkčující · "
         "⚠️ methylnaltrexon u opioidové zácpy. ⚠️ Loperamid je KONTRAINDIKOVANÝ "
         "u horečnaté a krvavé dysenterie a u C. difficile — zadržel by toxiny."))

N("99", "Farmakoterapie vředové choroby a GERD", retez(
    [("PPI je PROLÉČIVO", "zvyrazni"),
     ("⚠️ aktivuje se až v KYSELÉM prostředí u pumpy", "pozor"),
     ("⚠️ blokuje H⁺/K⁺-ATPázu IREVERZIBILNĚ", "zvyrazni"),
     ("⚠️ proto se bere 30 MIN PŘED JÍDLEM — pumpa musí být aktivní", "pozor")],
    titulek="Proč se PPI nesmí brát až po jídle",
    pozn="⚠️ Dlouhodobě: hypomagnezemie, deficit B12 a železa, zlomeniny, C. difficile; "
         "⚠️ omeprazol oslabuje klopidogrel → u kardiaka pantoprazol. ⚠️ Zubařsky: reflux "
         "→ EROZE SKLOVINY na patrových plochách horních zubů; ⚠️ po epizodě refluxu "
         "hned nečistit zuby, jen vypláchnout."))

N("100", "Prokinetika, antiemetika, emetika", cil(
    "ZVRACENÍ podle příčiny se vybírá RECEPTOR",
    [("CHEMOTERAPIE → 5-HT3 ondansetron (+ dexamethason, aprepitant)", "zvyrazni"),
     ("KINETÓZA → M a H1 skopolamin, prometazin", "zvyrazni"),
     ("GASTROSTÁZA, MIGRÉNA → D2 metoklopramid", "zvyrazni"),
     ("⚠️ PARKINSONIK → domperidon (neprojde do mozku)", "pozor"),
     ("⚠️ Metoklopramid: akutní DYSTONIE, max 5 dní", "pozor"),
     ("⚠️ Emetika (ipekakuanha) se dnes NEPOUŽÍVAJÍ", "pozor")],
    titulek="Antiemetikum se vybírá podle toho, který receptor zvracení spouští",
    pozn="⚠️ Po chemoterapii se ze zraněné střevní sliznice vyplaví SEROTONIN → proto právě "
         "blokáda 5-HT3. U migrény metoklopramid rozhýbe žaludek, aby se analgetikum vstřebalo."))

N("101", "Farmakoterapie nespecifických střevních zánětů", srovnani(
    "NAVOZENÍ REMISE",
    ["Kortikoidy (⚠️ budesonid — vysoký first-pass)", "Aminosalicyláty (hlavně u kolitidy)",
     "⚠️ Kortikoid JEN sem", "Rychlý nástup"],
    "UDRŽENÍ REMISE",
    ["Azathioprin (⚠️ testovat TPMT), methotrexát", "⚠️ Biologika: anti-TNF, vedolizumab",
     "⚠️ KORTIKOID SEM NIKDY", "— osteoporóza, diabetes, infekce"],
    titulek="Dvě fáze léčby, které se nesmí zaměnit",
    pozn="⚠️ Před anti-TNF povinný SCREENING TUBERKULÓZY: TNF-α drží pohromadě granulom; "
         "zablokuješ ho → granulom se rozpadne a latentní tuberkulóza propukne. "
         "⚠️ Aftózní léze v ústech mohou být projevem Crohnovy choroby.",
    a_kind="normal", b_kind="zvyrazni"))

N("102", "Spasmolytika", srovnani(
    "NEUROTROPNÍ (anticholinergní)",
    ["Butylskopolamin, atropin", "Přeruší nervový signál ke svalu",
     "⚠️ Butylskopolamin je kvartérní → do mozku ne", "⚠️ KI: glaukom, retence, ileus"],
    "MYOTROPNÍ (přímo na sval)",
    ["Drotaverin, papaverin, mebeverin", "Inhibice fosfodiesterázy → ↑ cAMP",
     "⚠️ Bez anticholinergních nežádoucích účinků", "Vhodné i u glaukomu"],
    titulek="Dvě cesty k témuž svalu — a rozdílné kontraindikace",
    pozn="U kolik se spazmolytikum kombinuje s analgetikem (metamizol). ⚠️ Morfin sám "
         "stahuje Oddiho svěrač → u biliární koliky nikdy bez spazmolytika. "
         "⚠️ Na zubní bolest spazmolytika nepatří — nejde o hladký sval.",
    a_kind="normal", b_kind="zvyrazni"))

N("103", "Hepatoprotektiva, cholagoga", srovnani(
    "⭐ MÁ DOLOŽENÝ ÚČINEK",
    ["Kyselina ursodeoxycholová (UDCA)", "N-acetylcystein u paracetamolu",
     "Laktulóza + rifaximin u encefalopatie", "Ornithin-aspartát"],
    "SLABÁ EVIDENCE",
    ["Silymarin (ostropestřec)", "Esenciální fosfolipidy", "Ademetionin",
     "⚠️ Nenahradí odstranění příčiny"],
    titulek="U většiny „hepatoprotektiv\" je důkaz slabý — a je fér to říct nahlas",
    pozn="⚠️ Nejúčinnější „hepatoprotektivum\" u alkoholika je ABSTINENCE. ⚠️ U cirhózy: "
         "nízký albumin → vyšší volná frakce léků; paracetamol v redukované dávce, "
         "NSA raději vůbec.", b_kind="tichy"))

N("104", "Farmaka v očním lékařství", srovnani(
    "MÉNĚ TVORBY nitrooční tekutiny",
    ["Betablokátory — ⚠️ TIMOLOL", "Inhibitory karboanhydrázy (dorzolamid)",
     "α2 agonisté (brimonidin)", ""],
    "LEPŠÍ ODTOK",
    ["⭐ Analoga prostaglandinů — LATANOPROST", "⚠️ ztmavnutí duhovky, delší řasy",
     "Pilokarpin (mióza otevře úhel)", "Nejúčinnější, 1× denně"],
    titulek="Glaukom: buď zmenším tvorbu, nebo zlepším odtok",
    pozn="⚠️ OČNÍ KAPKY SE VSTŘEBÁVAJÍ — timolol z kapek vyvolá u astmatika bronchospazmus "
         "a u kardiaka bradykardii; pacient je v anamnéze neuvede. ⚠️ Kortikoid do oka: "
         "KI u herpetické keratitidy, dlouhodobě katarakta a glaukom. ⚠️ Anticholinergikum "
         "může vyvolat akutní glaukom s úzkým úhlem.", a_kind="normal", b_kind="zvyrazni"))

N("105", "Drogová (léková) závislost", smycka(
    ["DROGA vyplaví DOPAMIN v nucleus accumbens",
     "mozek si to označí: „opakuj to\"",
     "opakování → ⚠️ DOWN-REGULACE receptorů = TOLERANCE",
     "bez látky je systém pod normálem ⚠️ ODVYKACÍ STAV a CRAVING"],
    titulek="Kruh závislosti — všechny návykové látky končí ve stejném místě",
    brzda="a proto se droga vezme znovu"))

N("106", "Ethylalkohol, methylalkohol", srovnani(
    "ETANOL",
    ["ADH → acetaldehyd → acetát", "⚠️ Kinetika NULTÉHO ŘÁDU",
     "⚠️ Disulfiram blokuje 2. krok", "⚠️ Tlumivá látka — „rozjaření\" je odbrždění"],
    "METANOL",
    ["⚠️ Sám je málo toxický", "⚠️ ADH → formaldehyd → KYSELINA MRAVENČÍ",
     "→ těžká acidóza a ⚠️ SLEPOTA", "⚠️ Antidotum: ETANOL nebo FOMEPIZOL"],
    titulek="Proč se otrava metanolem léčí alkoholem",
    pozn="Etanol má k alkoholdehydrogenáze mnohem vyšší afinitu → obsadí ji a metanol se "
         "vyloučí nezměněný. ⚠️ Delirium tremens: benzodiazepiny + ⚠️ THIAMIN PŘED GLUKÓZOU "
         "(jinak hrozí Wernickeova encefalopatie).", a_kind="normal"))

N("107", "Konopí, kanabinoidy", srovnani(
    "THC",
    ["⚠️ Psychoaktivní — parciální agonista CB1", "Euforie, změněné vnímání času",
     "⚠️ Zhoršení paměti a pozornosti", "⚠️ Riziko psychózy u disponovaných"],
    "CBD",
    ["⚠️ NEpsychoaktivní", "⚠️ Kanabidiol u vzácných dětských epilepsií",
     "(Dravetové, Lennoxův–Gastautův sy)", "Jiný mechanismus než THC"],
    titulek="Dvě látky z jedné rostliny, které se pletou dohromady",
    pozn="⚠️ Zubařsky: XEROSTOMIE → kaz · gingivitida · kouřením leukoplakie · "
         "⚠️ u intoxikovaného pacienta neprovádět plánovaný výkon (tachykardie, úzkost). "
         "Léčebně: nauzea po chemoterapii, spasticita u roztroušené sklerózy.",
    a_kind="pozor", b_kind="normal"))

N("108", "Halucinogeny (psychomimetika)", srovnani(
    "SEROTONINERGNÍ — LSD, psilocybin",
    ["⚠️ Agonisté 5-HT2A", "Halucinace při ZACHOVANÉ orientaci",
     "⚠️ Pacient se POTÍ, ví, kde je", "Léčba: klid + benzodiazepin"],
    "⚠️ ANTICHOLINERGNÍ — durman, rulík",
    ["Delirium a zmatenost", "⚠️ SUCHÁ, HORKÁ, ČERVENÁ kůže",
     "⚠️ Pacient je DEZORIENTOVANÝ", "⚠️ Antidotum FYZOSTIGMIN"],
    titulek="Jak od sebe odlišit dvě intoxikace, které obě „vidí věci\"",
    pozn="Disociativní (fencyklidin, ketamin) blokují NMDA. ⚠️ MDMA: hypertermie, "
         "hyponatremie, serotoninový syndrom a ⚠️ výrazný BRUXISMUS a trismus — "
         "pro zubaře typický nález.", a_kind="normal"))

N("109", "Stimulancia", cil(
    "STIMULANCIA víc dopaminu a noradrenalinu ve štěrbině",
    [("Euforie, bdělost, ztráta chuti k jídlu", "normal"),
     ("⚠️ INFARKT a CMP u mladých (kokain)", "pozor"),
     ("⚠️ Toxická PSYCHÓZA k nerozeznání od schizofrenie", "pozor"),
     ("⚠️ HYPERTERMIE jako příčina smrti", "pozor"),
     ("⚠️ „METH MOUTH\" a BRUXISMUS", "pozor"),
     ("⚠️ NIKDY adrenalin v anestetiku u intoxikovaného", "pozor")],
    titulek="Jeden mechanismus, ze kterého plyne účinek i všechny komplikace",
    pozn="Léčebně: methylfenidát u ADHD (⚠️ paradoxně zklidní — posílí kontrolní funkce "
         "čelního laloku), modafinil u narkolepsie. ⚠️ Kokain do nosu → nekróza přepážky "
         "a patra. Kofein blokuje adenosin — jen maskuje únavu."))

N("110", "Nikotin", srovnani(
    "CIGARETOVÝ kouř — KYSELÝ",
    ["Nikotin je NABITÝ", "⚠️ Ústy se nevstřebá",
     "→ ⚠️ musí se INHALOVAT do plic", "→ mozek za 7 s → ⚠️ silný návyk"],
    "DÝMKOVÝ a DOUTNÍKOVÝ — ZÁSADITÝ",
    ["Nikotin je nenabitý", "⚠️ Vstřebá se rovnou v ÚSTECH",
     "→ nemusí se inhalovat", "Iontová past potřetí"],
    titulek="Proč se cigareta musí šluknout a doutník ne",
    pozn="⚠️ ZUBAŘSKY: karcinom dutiny ústní · ⚠️ PARODONTITIDA A NAVÍC MASKOVANÁ (nikotin "
         "stahuje cévy → dáseň méně krvácí) · zhoršené hojení, suchá alveolitida, selhání "
         "implantátů. ⚠️ Kouření indukuje CYP1A2 → po přestání stoupne hladina theofylinu, "
         "olanzapinu, klozapinu. Odvykání: ⚠️ vareniklin je nejúčinnější.",
    a_kind="pozor", b_kind="normal"))
