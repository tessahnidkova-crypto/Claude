#!/usr/bin/env python3
"""Sketchnote ke KAŽDÉ ze 136 zkouškových otázek z farmakologie — celá otázka
na jednu kreslenou stranu.

Struktura jednoho záznamu:
    jadro   — jedna věta pod zvýrazňovačem: o čem otázka JE
    tok     — vodorovný pás mechanismu (3–5 kroků)
    karty   — dlaždice: dělení, zástupci, indikace, nežádoucí účinky, pasti
    mnemo   — čím si to udržíš v hlavě
    zubar   — zubařský přesah (katedra zkouší zubaře)
    past    — na čem se u téhle otázky nejčastěji chytají

Klíče barev: zelena (jádro věci) · cervena (past, NÚ) · modra (klinika) ·
zluta (mnemotechnika) · bila (neutrální výčet).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sketch import sketchnote  # noqa: E402

O = []


def S(cislo, nadpis, **kw):
    O.append((cislo, nadpis, sketchnote(cislo, nadpis, **kw)))


# ═════════════════════════════════════ OBECNÁ FARMAKOLOGIE

S("O1", "Farmakologie, původ a zdroje léčiv, názvy, lékopis",
  jadro="Farmakologie zkoumá vzájemné působení léčiva a organismu — a dělí se na to, "
        "co tělo dělá s lékem (kinetika) a co lék dělá s tělem (dynamika).",
  tok=[("ÚČINNÁ LÁTKA", "zelena"), ("+ POMOCNÉ LÁTKY", "bila"),
       ("= LÉKOVÁ FORMA", "bila"), ("= LÉČIVÝ PŘÍPRAVEK", "zelena")],
  tok_popisky=["plnivo, barvivo, konzervans", "tableta, mast, injekce", "to, co je v lékárně"],
  karty=[
      ("OBORY FARMAKOLOGIE", [
          "Farmakokinetika — co tělo dělá s lékem (ADME)",
          "Farmakodynamika — co lék dělá s tělem (mechanismus, účinek)",
          "Farmakoterapie — použití léčiv v léčbě",
          "Toxikologie · farmakovigilance · farmakoekonomika · farmakogenetika"], "zelena"),
      ("ZDROJE LÉČIV", [
          "Rostliny — alkaloidy (morfin, atropin), glykosidy (digoxin)",
          "Živočichové — heparin, inzulin, hormony",
          "Mikroorganismy — antibiotika (penicilin z Penicillium)",
          "Minerály — soli, stopové prvky",
          "Syntéza a polosyntéza — dnes většina léčiv",
          "Biotechnologie — rekombinantní bílkoviny a protilátky"], "bila"),
      ("TŘI NÁZVY TÉŽE LÁTKY", [
          "Chemický — přesný vzorec, v praxi se nepoužívá",
          "GENERICKÝ (nechráněný) — ibuprofen; ⚠️ u zkoušky mluv tímhle",
          "Firemní (chráněný) — Brufen, Ibalgin"], "zluta"),
      ("LÉKOPIS (Pharmacopoea)", [
          "Závazný soubor požadavků na jakost léčiv a jejich zkoušení",
          "Český lékopis vychází z Evropského lékopisu",
          "OFICINÁLNÍ = uvedené v lékopisu · MAGISTRALITER = připravené v lékárně",
          "HVLP = hromadně vyráběný léčivý přípravek"], "modra"),
  ],
  mnemo="Kinetika = KAM lék jde. Dynamika = CO tam dělá.",
  zubar="V zubní ordinaci se běžně setkáš s magistraliter přípravky (roztoky, pasty) "
        "i s HVLP — rozdíl je v tom, kdo ručí za jakost.",
  past="Ve zdroji jsou dva překlepy: „oficiální\" má být OFICINÁLNÍ (z lékopisu) "
       "a „obsolentní\" má být OBSOLETNÍ (zastaralý). U zkoušky to zazní jako neznalost.")

S("O2", "Legislativa, doplňky stravy, zdravotnické prostředky, regulační orgány",
  jadro="Rozdíl mezi lékem a doplňkem stravy není v tom, co je uvnitř, ale v tom, "
        "co musel výrobce prokázat, než to směl prodávat.",
  karty=[
      ("LÉČIVÝ PŘÍPRAVEK", [
          "Musí prokázat ÚČINNOST, bezpečnost a jakost",
          "Registruje SÚKL (národně) nebo EMA (evropsky)",
          "Smí tvrdit, že léčí nebo předchází nemoci",
          "Povinné hlášení nežádoucích účinků (farmakovigilance)"], "zelena"),
      ("DOPLNĚK STRAVY", [
          "Je to POTRAVINA, ne lék",
          "⚠️ Účinnost prokazovat NEMUSÍ",
          "Jen ohlášení; dozor SZPI",
          "⚠️ Nesmí tvrdit, že léčí — a pacient v tom rozdíl nevidí"], "cervena"),
      ("ZDRAVOTNICKÝ PROSTŘEDEK", [
          "Působí FYZIKÁLNĚ, ne farmakologicky",
          "Výplň, implantát, obvaz, kanyla, protéza",
          "Posuzuje se shoda (CE), rizikové třídy I–III"], "modra"),
      ("KDO NA CO DOHLÍŽÍ", [
          "SÚKL — registrace, dozor nad léčivy, ceny a úhrady",
          "EMA — centralizovaná registrace v EU",
          "MZ ČR — legislativa · SZPI — potraviny a doplňky",
          "⚠️ Zákon o léčivech č. 378/2007 Sb. [⚠️ ověřit číslo dle skript]"], "bila"),
      ("ZPŮSOBY VÝDEJE", [
          "Vázán na lékařský předpis (Rp.)",
          "S omezením — jen určitá odbornost",
          "Volně prodejné (OTC)",
          "⚠️ Recept s modrým pruhem — opiáty a psychotropní látky"], "zluta"),
  ],
  mnemo="Lék musí DOKÁZAT, že funguje. Doplněk stravy jen nesmí LHÁT, že léčí.",
  zubar="Pacienti běžně berou doplňky (ginkgo, česnek, třezalka) a v anamnéze je "
        "neuvedou — ptej se na ně cíleně, mají skutečné interakce a zvyšují krvácivost.",
  past="„Přírodní\" a „bez předpisu\" neznamená „bez rizika\" ani „bez interakcí\".")

S("O3", "Předepisování léčivých přípravků",
  jadro="Recept je právní dokument — a jeho náležitosti nejsou formalita, "
        "ale to, co lékárníka chrání před záměnou.",
  tok=[("LÉKAŘ vystaví eRecept", "zelena"), ("CENTRÁLNÍ ÚLOŽIŠTĚ", "bila"),
       ("LÉKÁRNA vydá a odepíše", "bila"), ("PACIENT", "zelena")],
  tok_popisky=["identifikátor SMS / e-mail", "kontrola interakcí", ""],
  karty=[
      ("CO MUSÍ BÝT NA RECEPTU", [
          "Identifikace pacienta (jméno, číslo pojištěnce)",
          "Léčivo — název, síla, léková forma, množství",
          "Dávkování a způsob podání (D.S. — signatura)",
          "Identifikace lékaře a zdravotnického zařízení, podpis a razítko",
          "Datum vystavení"], "zelena"),
      ("DRUHY RECEPTŮ", [
          "eRecept — dnes standard, s identifikátorem",
          "Listinný — jen ve výjimkách (výpadek systému)",
          "⚠️ S modrým pruhem — omamné a psychotropní látky",
          "Opakovací recept (repetatur) — s uvedeným počtem opakování"], "modra"),
      ("PLATNOST", [
          "Běžný recept obvykle 14 dní od vystavení",
          "Recept od pohotovosti kratší dobu",
          "Antibiotika — kratší platnost",
          "⚠️ [⚠️ ověřit přesné lhůty podle vašich skript]"], "bila"),
      ("MAGISTRALITER", [
          "Individuálně připravený přípravek v lékárně",
          "Předpis: Rp. — složení — M.f. (misce fiat) — D.S.",
          "V zubním lékařství stále živé (výplachy, pasty, roztoky)"], "zluta"),
  ],
  mnemo="Rp. (recipe = vezmi) — D.S. (da signa = vydej a označ).",
  zubar="Zubní lékař předepisuje hlavně analgetika, antibiotika a lokální antiseptika. "
        "⚠️ Před předpisem vždy anamnéza: alergie, warfarin, těhotenství, ledviny.",
  past="Předepsat antibiotikum bez ošetření zdroje infekce problém nevyřeší — "
       "u abscesu je rozhodující drenáž, ne recept.")

S("O4", "Preklinické a klinické hodnocení léčiv",
  jadro="Cesta od molekuly k léku trvá roky a jde po stupních, protože každý stupeň "
        "odpovídá na jinou otázku — a vzácné riziko se pozná až na konci.",
  tok=[("PREKLINIKA zkumavka a zvíře", "bila"), ("FÁZE I zdraví dobrovolníci", "bila"),
       ("FÁZE II nemocní, dávka", "bila"), ("FÁZE III tisíce, srovnání", "zelena"),
       ("FÁZE IV po registraci", "cervena")],
  karty=[
      ("NA CO SE KTERÁ FÁZE PTÁ", [
          "Preklinika — toxicita, kinetika, mechanismus, teratogenita",
          "I. desítky ZDRAVÝCH — je to bezpečné a jak se to v těle chová?",
          "II. stovky NEMOCNÝCH — zabírá to a v jaké dávce?",
          "III. tisíce nemocných — je to LEPŠÍ než dosavadní léčba?",
          "IV. celá populace — ⚠️ co se objeví, až to bere milion lidí"], "zelena"),
      ("ZÁSADY KLINICKÉ STUDIE", [
          "Randomizace — náhodné rozdělení do skupin",
          "Zaslepení: jednoduché · dvojité · trojité",
          "Kontrolní skupina: placebo nebo dosavadní léčba",
          "Předem daný primární cíl (endpoint)",
          "⚠️ Informovaný souhlas a etická komise"], "modra"),
      ("PROČ SE VZÁCNÝ NÚ NAJDE POZDĚ", [
          "Fáze III má tisíce pacientů",
          "Účinek jednoho z deseti tisíc v ní nemá šanci vyjít najevo",
          "⚠️ Proto farmakovigilance a hlášení podezření na NÚ",
          "Příklady stažení: rofekoxib, sibutramin, thalidomid"], "cervena"),
      ("POJMY", [
          "GLP · GCP — správná laboratorní a klinická praxe",
          "Účinnost (efficacy) ve studii × účinnost (effectiveness) v praxi",
          "Non-inferiorita × superiorita",
          "Generikum — prokazuje se BIOEKVIVALENCE, ne účinnost znovu"], "bila"),
  ],
  mnemo="I. bezpečnost · II. dávka · III. srovnání · IV. vzácné nežádoucí účinky.",
  zubar="Hlášení nežádoucích účinků SÚKL je povinnost i zubního lékaře — typicky "
        "alergie na anestetikum nebo antibiotikum.",
  past="Registrace neznamená, že je lék dokonale prozkoumaný. Znamená jen, "
       "že přínos v době registrace převážil známá rizika.")

S("O5", "Způsoby aplikace léčiv, výhody a nevýhody",
  jadro="Hlavní rozdíl mezi cestami podání není rychlost, ale to, "
        "jestli lék projde játry, než se dostane do oběhu.",
  tok=[("polknutá dávka 100 %", "zelena"), ("střevní stěna", "bila"),
       ("⚠️ JÁTRA first-pass", "cervena"), ("do těla dorazí zlomek", "bila")],
  tok_popisky=["", "portální žíla", ""],
  karty=[
      ("ENTERÁLNÍ (přes trávicí trakt)", [
          "Perorálně — pohodlné, levné, bezpečné; ⚠️ first-pass, pomalejší",
          "Sublingválně — ⚠️ obchází játra, rychlé (nitroglycerin)",
          "Rektálně — částečně obchází játra, funguje i při zvracení"], "zelena"),
      ("PARENTERÁLNÍ (mimo trávicí trakt)", [
          "i.v. — ⚠️ 100% dostupnost, okamžitě, ⚠️ nedá se vzít zpět",
          "i.m. — rychle, dobře prokrvený sval",
          "s.c. — pomalejší (inzulin, hepariny)",
          "Intratekálně, intraartikulárně, intraoseálně"], "modra"),
      ("MÍSTNÍ A OSTATNÍ", [
          "Na kůži a sliznice, inhalačně, do oka, do nosu",
          "Transdermální náplast — nejpomalejší, ale drží dny",
          "⚠️ „Místní\" neznamená „bez celkového účinku\""], "bila"),
      ("CO ROZHODUJE O VOLBĚ", [
          "Stav pacienta (bezvědomí, zvracení)",
          "Potřebná rychlost účinku",
          "Vlastnosti látky (rozpad v žaludku, first-pass)",
          "Cíl: má působit místně, nebo celkově?"], "zluta"),
  ],
  mnemo="First-pass obchází: pod jazyk, do žíly, do svalu, na kůži, do konečníku.",
  zubar="Lokální anestetikum je klasické místní podání — ale ⚠️ vstřebá se a při "
        "překročení dávky má systémovou toxicitu (CNS a srdce).",
  past="i.v. podání je nejrychlejší, ale i nejméně odpustí chybu — podané se "
       "nedá odvolat, na rozdíl od polknuté tablety.")

S("O6", "Lékové formy — perorální a orální",
  jadro="Perorální = k polknutí, orální = účinek přímo v ústech. "
        "Znějí stejně a znamenají skoro opak.",
  karty=[
      ("PERORÁLNÍ — polknout", [
          "Tablety, potahované tablety, tobolky",
          "Sirupy, suspenze, kapky, prášky",
          "⚠️ Enterosolventní obal — projde žaludkem, rozpadne se ve střevě",
          "⚠️ Retardované (SR, ZOK) — uvolňují postupně, 1× denně"], "zelena"),
      ("ORÁLNÍ — účinek v ústech", [
          "Pastilky, žvýkací tablety, ústní vody, gely",
          "⚠️ Sublingválně a bukálně — vstřebá se rovnou do krve",
          "→ obchází játra (nitroglycerin, buprenorfin)",
          "Zubařsky nejbližší skupina lékových forem"], "modra"),
      ("PROČ SE NĚKTERÉ TABLETY NESMÍ DRTIT", [
          "Retardovaná — drcením se uvolní celá denní dávka najednou",
          "Enterosolventní — obsah poleptá žaludek nebo se zničí kyselinou",
          "⚠️ U pacienta s poruchou polykání se hledá jiná forma, nedrtí se"], "cervena"),
      ("POMOCNÉ LÁTKY", [
          "Plniva, pojiva, kluzné látky, rozvolňovadla",
          "Barviva, sladidla, konzervanty",
          "⚠️ Laktóza — problém u intolerance",
          "⚠️ Cukr v sirupech — u dětí a chronické léčby riziko kazu"], "bila"),
  ],
  mnemo="PER os = skrz ústa dál. OR = v ústech a zůstává tam.",
  zubar="⚠️ Sirupy a rozpustné tablety obsahují cukr — u dětí na dlouhodobé léčbě "
        "(antiepileptika, antibiotika) je to reálná příčina kazu. Doporuč vypláchnout "
        "ústa a čistit zuby po dávce.",
  past="Sublingvální forma se NEPOLYKÁ — polknutím ztratí smysl, protože ji zničí "
       "first-pass efekt.")

S("O7", "Lékové formy — parenterální a dermatologika",
  jadro="Rychlost účinku parenterální formy sleduje prokrvení místa, kam se podá.",
  tok=[("i.v. okamžitě", "zelena"), ("i.m. rychle", "bila"),
       ("s.c. pomaleji", "bila"), ("náplast dny", "modra")],
  karty=[
      ("PARENTERÁLNÍ FORMY", [
          "Injekce — roztok, suspenze, emulze; ⚠️ suspenze NIKDY i.v.",
          "Infuze — velkoobjemové, isotonické",
          "Implantáty a depotní injekce — týdny až měsíce",
          "⚠️ Musí být sterilní, apyrogenní, bez částic"], "zelena"),
      ("VÝHODY A NEVÝHODY", [
          "+ Obchází játra i žaludek, přesné dávkování, jistá dostupnost",
          "+ Použitelné u bezvědomí a zvracení",
          "⚠️ − Bolestivé, riziko infekce a embolie",
          "⚠️ − Podané se nedá vzít zpět"], "cervena"),
      ("DERMATOLOGIKA — základy", [
          "Mast — tučný základ, na suchou kůži, největší průnik",
          "Krém — voda i tuk, univerzální",
          "Gel — vodný, chladí, na ochlupené oblasti",
          "Pasta, zásyp, roztok, náplast"], "modra"),
      ("PRŮNIK KŮŽÍ", [
          "Rozhoduje tučnost základu a stav kůže",
          "Okluze (krytí) průnik výrazně zvyšuje",
          "⚠️ Na obličej a k dětem jen slabé kortikoidy a krátce",
          "⚠️ Dlouhodobé lokální kortikoidy → atrofie kůže a strie"], "bila"),
  ],
  mnemo="Čím tučnější základ, tím hlouběji to jde.",
  zubar="Kortikoidová mast na ústní sliznici se drží špatně — používají se "
        "adhezivní pasty (orabase); ⚠️ u herpetické léze se kortikoid nedává vůbec.",
  past="Suspenzi nikdy nitrožilně — částice by způsobily embolizaci.")

S("O8", "Lékové formy — oční, ušní, nosní, rektalia, vaginalia, inhalanda",
  jadro="Každá „místní\" forma se dokáže vstřebat do celého těla — a právě odtud "
        "pocházejí nejčastěji přehlédnuté nežádoucí účinky.",
  karty=[
      ("OČNÍ", [
          "Kapky, masti, gely — ⚠️ musí být sterilní a isotonické",
          "⚠️ Timolol z kapek → bradykardie a bronchospazmus",
          "Stisknutí vnitřního koutku po nakapání sníží vstřebání",
          "⚠️ Po otevření obvykle 4 týdny použitelnosti"], "cervena"),
      ("NOSNÍ a UŠNÍ", [
          "⚠️ Dekongescenční kapky max 5–7 dní → rhinitis medicamentosa",
          "Nosní forma se využívá i k celkovému účinku (desmopresin, sumatriptan)",
          "⚠️ Ušní kapky ne při perforaci bubínku"], "cervena"),
      ("INHALANDA", [
          "Aerosolový dávkovač (MDI), práškový inhalátor (DPI), nebulizace",
          "⚠️ Rozhoduje technika inhalace — chybná = lék do úst, ne do plic",
          "⚠️ Nástavec (spacer) zlepší depozici a sníží NÚ",
          "⚠️ Inhalační kortikoid → orální kandidóza a chrapot"], "modra"),
      ("REKTALIA a VAGINALIA", [
          "Čípky, rektální roztoky, masti",
          "⚠️ Dolní část konečníku obchází játra, horní ne",
          "Vhodné u zvracení, u dětí, u bezvědomí",
          "Vaginálně: globule, krémy, tablety — hlavně místní léčba"], "bila"),
  ],
  mnemo="„Místní\" znamená KAM to dáváš, ne KDE to působí.",
  zubar="⚠️ Po každé inhalaci kortikoidu vypláchnout ústa — jinak kandidóza. "
        "U pacienta s protézou je riziko vyšší, protéza se musí dezinfikovat.",
  past="Oční kapky pacient v anamnéze neuvede, protože je nepovažuje za lék. "
       "Ptej se na ně cíleně — hlavně na timolol.")

S("O9", "Komunikace, adherence, compliance, placebo a nocebo",
  jadro="Nejčastější příčina „selhání léčby\" není špatný lék, ale nebrané tablety.",
  karty=[
      ("POJMY", [
          "Compliance — pacient dělá, co bylo nařízeno (pasivní)",
          "Adherence — pacient dodržuje dohodnutý plán (partnerství)",
          "Perzistence — jak dlouho u léčby vydrží",
          "Konkordance — společné rozhodnutí lékaře a pacienta"], "zelena"),
      ("PROČ PACIENTI NEBEROU LÉKY", [
          "Nemoc nebolí (hypertenze, osteoporóza)",
          "Příliš mnoho tablet a složitý režim",
          "Nežádoucí účinky, obavy z nich",
          "Cena, nedůvěra, nepochopení",
          "⚠️ Zlepší: fixní kombinace, 1× denně, jasné vysvětlení"], "bila"),
      ("PLACEBO", [
          "Očekávání zlepšení → měřitelné zlepšení",
          "⚠️ Není to „vymyšlený\" efekt — má neurobiologický podklad",
          "Zesiluje účinek každého skutečného léku",
          "Podíl mají i vzhled léku a jistota lékaře"], "modra"),
      ("NOCEBO", [
          "Očekávání škody → potíže se skutečně objeví",
          "⚠️ Vzniká i z příbalového letáku a z neopatrné věty",
          "Časté vysazení statinů a antidepresiv „kvůli NÚ\"",
          "⚠️ „Bude to bolet\" bolest zesílí"], "cervena"),
  ],
  mnemo="Tvoje slova jsou účinná látka. Mají dávku i nežádoucí účinky.",
  zubar="Nocebo je v zubní ordinaci každodenní — formulace před vpichem měřitelně "
        "mění vnímanou bolest. „Teď to znecitlivíme\" funguje lépe než „píchnu vám injekci\".",
  past="Než přidáš druhý lék pro „nedostatečný účinek\", ověř, jestli pacient bere ten první.")

S("O11", "Základní farmakokinetické parametry a procesy",
  jadro="Farmakokinetika = co tělo dělá s lékem. Čtyři děje, které se dějí současně, ne po sobě.",
  tok=[("A absorpce", "zelena"), ("D distribuce", "zelena"),
       ("M metabolismus", "zelena"), ("E exkrece", "zelena")],
  karty=[
      ("ČTYŘI DĚJE", [
          "Absorpce — vstup do krve; měří ji biologická dostupnost F",
          "Distribuce — rozvod do tkání; měří ji distribuční objem Vd",
          "Metabolismus — přeměna, hlavně játra, fáze I a II",
          "Exkrece — vyloučení, hlavně ledviny; ⚠️ M + E = ELIMINACE"], "zelena"),
      ("KLÍČOVÉ PARAMETRY", [
          "F — biologická dostupnost (i.v. = 100 %)",
          "Vd — zdánlivý distribuční objem",
          "CL — clearance: objem krve očištěný za čas",
          "t½ — biologický poločas",
          "AUC — plocha pod křivkou = celková expozice",
          "Cmax a tmax — vrchol a čas vrcholu"], "bila"),
      ("JAK SPOLU SOUVISÍ", [
          "t½ závisí na Vd A na clearance zároveň",
          "Velký Vd → dlouhý poločas, i když clearance je dobrá",
          "⚠️ Ustálený stav (steady state) přijde za 4–5 poločasů",
          "⚠️ Po vysazení je lék prakticky pryč také za 4–5 poločasů"], "modra"),
      ("KINETIKA × DYNAMIKA", [
          "Kinetika — kam lék jde a jak dlouho tam je",
          "Dynamika — co v cíli udělá (receptor, enzym, kanál)",
          "⚠️ Nezaměňovat — bývá to úvodní otázka"], "zluta"),
  ],
  mnemo="ADME. A eliminace = M + E dohromady.",
  zubar="Poločas rozhoduje o dávkovacím intervalu analgetika po extrakci — "
        "ibuprofen po 6–8 h, paracetamol po 6 h, ne „podle potřeby\" nárazově.",
  past="Ustálený stav nezrychlíš vyšší dávkou — jen nasycovací dávkou. "
       "Vyšší udržovací dávka jen zvedne hladinu, ale stejně za 4–5 poločasů.")

S("O12", "Procesy nultého a prvního řádu, saturační kinetika",
  jadro="Většina léků se odbourává v konstantním PODÍLU. Pár jich má nasycený enzym "
        "a odbourává se konstantní MNOŽSTVÍ — a ty jsou nebezpečné.",
  karty=[
      ("PRVNÍ ŘÁD — většina léčiv", [
          "Odbourá se stále stejný PODÍL za čas (např. polovina za hodinu)",
          "Enzym má rezervu a stíhá",
          "⚠️ Má smysl mluvit o poločasu",
          "Křivka poklesu je exponenciála"], "zelena"),
      ("NULTÝ ŘÁD — nasycený enzym", [
          "Odbourá se stále stejné MNOŽSTVÍ za čas",
          "⚠️ ETANOL, FENYTOIN, aspirin ve vysoké dávce, theofylin",
          "⚠️ Poločas ztrácí smysl",
          "Křivka poklesu je přímka"], "cervena"),
      ("SATURAČNÍ KINETIKA", [
          "Přechod mezi oběma řády (Michaelisova–Mentenové)",
          "Dokud je enzym volný → první řád",
          "Jakmile se zahltí → nultý řád",
          "⚠️ Právě v tom přechodu je lék nejnebezpečnější"], "modra"),
      ("PROČ TO ROZHODUJE V PRAXI", [
          "⚠️ U fenytoinu stačí malé zvýšení dávky a hladina vyskočí do toxického pásma",
          "Příznaky: nystagmus, ataxie, zmatenost",
          "⚠️ Proto se u něj měří hladiny",
          "Etanol: odbourá se zhruba 0,1–0,15 ‰ za hodinu bez ohledu na to, kolik vypiješ"], "bila"),
  ],
  mnemo="První řád = PODÍL. Nultý řád = MNOŽSTVÍ. Nasycený enzym víc nestihne.",
  zubar="Pacient po alkoholu má nepředvídatelnou reakci na sedativa a lokální "
        "anestetika — plánovaný výkon odlož.",
  past="U léku s nultým řádem nemá smysl počítat „za dva poločasy bude polovina\" — "
       "poločas se s dávkou mění.")

S("O13", "Absorpce, Batemanova funkce, biologická dostupnost, AUC",
  jadro="Vrchol křivky není konec vstřebávání — je to remíza mezi vstřebáváním a eliminací.",
  tok=[("vstřebávání převažuje", "zelena"), ("VRCHOL Cmax rovnováha", "cervena"),
       ("eliminace převažuje", "bila")],
  karty=[
      ("BATEMANOVA KŘIVKA", [
          "Popisuje průběh hladiny po jednorázovém perorálním podání",
          "Výsledek dvou dějů najednou: vstřebávání a eliminace",
          "⚠️ V Cmax se oba vyrovnají — vstřebávání ještě běží dál",
          "tmax — čas do vrcholu; závisí hlavně na rychlosti vstřebávání"], "zelena"),
      ("BIOLOGICKÁ DOSTUPNOST F", [
          "Podíl dávky, který se dostal do systémového oběhu nezměněný",
          "⚠️ i.v. = 100 % z definice",
          "Snižuje ji: rozklad v žaludku, špatné vstřebání, ⚠️ first-pass",
          "Počítá se z poměru AUC (p.o. / i.v.)"], "modra"),
      ("AUC — plocha pod křivkou", [
          "Celková expozice organismu léku",
          "Základ posuzování bioekvivalence generik",
          "⚠️ Generikum musí mít srovnatelnou AUC i Cmax, ne stejnou tabletu"], "bila"),
      ("CO OVLIVŇUJE VSTŘEBÁVÁNÍ", [
          "Léková forma (roztok rychleji než tableta)",
          "Jídlo — zpomalí, někdy i zvýší (tučné jídlo u lipofilních)",
          "pH žaludku, rychlost vyprazdňování, motilita",
          "⚠️ Chelatace: mléko, antacida, železo × tetracykliny a chinolony"], "cervena"),
  ],
  mnemo="Cmax = remíza. Ne konec vstřebávání.",
  zubar="Analgetikum po extrakci má smysl podat ještě před odezněním anestezie — "
        "než začne bolest, aby vrcholu hladiny dosáhlo včas.",
  past="Bioekvivalence neznamená identický přípravek — znamená, že se AUC a Cmax "
       "vejdou do povoleného pásma.")

S("O10", "Přechod látek biologickými membránami",
  jadro="Léčivo projde membránou jen v NENABITÉ formě — a z toho jediného pravidla "
        "plyne pět různých klinických situací.",
  tok=[("NENABITÉ tukorozpustné", "zelena"), ("projde membránou", "bila"),
       ("uvnitř jiné pH → NABIJE SE", "cervena"), ("zpět neprojde → HROMADÍ SE", "cervena")],
  tok_popisky=["prostá difuze", "", "IONTOVÁ PAST"],
  karty=[
      ("ZPŮSOBY PŘESTUPU", [
          "Prostá difuze — po spádu, bez energie; jen nenabité a lipofilní",
          "Facilitovaná difuze — přenašečem, po spádu, ⚠️ saturovatelná",
          "Aktivní transport — proti spádu, ⚠️ stojí ATP (P-glykoprotein)",
          "Filtrace póry, pinocytóza"], "zelena"),
      ("CO ROZHODUJE", [
          "Rozpustnost v tucích — čím lipofilnější, tím snáz",
          "Velikost molekuly",
          "⚠️ Ionizace: pKa látky proti pH prostředí",
          "Koncentrační spád"], "bila"),
      ("IONTOVÁ PAST — pět situací", [
          "⚠️ Anestezie nezabírá v zaníceném zubu (kyselé pH)",
          "Alkalizace moči u otravy aspirinem",
          "Laktulóza u jaterní encefalopatie (uvězní NH₄⁺)",
          "Léčiva u plodu a v mateřském mléce",
          "Nikotin z kyselého cigaretového kouře"], "cervena"),
      ("BARIÉRY", [
          "Hematoencefalická — těsné spoje + ⚠️ P-glykoprotein léky vyhazuje ven",
          "Placentární — ⚠️ propustnější, než se čeká",
          "Krev–varle, krev–sítnice",
          "⚠️ Zánět bariéru zpropustní (proto ATB u meningitidy fungují)"], "modra"),
  ],
  mnemo="Nenabité projde, nabité uvízne. Kyselý lék se hromadí v zásaditém prostředí a naopak.",
  zubar="V zaníceném zubu je kyselé pH → anestetikum je nabité už venku → do nervu se "
        "nedostane. Řešení: svodná anestezie mimo zánět nebo intraligamentární technika, "
        "ne bezhlavě vyšší dávka.",
  past="P-glykoprotein je důvod, proč některá lipofilní léčiva do mozku nepůsobí — "
       "aktivně je to vyhazuje zpět.")

S("O14", "Distribuce, distribuční objem, redistribuce, vazba na bílkoviny, bariéry",
  jadro="Působí, metabolizuje se a vylučuje jen VOLNÁ frakce léku. Vázaná část je sklad.",
  karty=[
      ("VAZBA NA BÍLKOVINY", [
          "Kyselé léky → ALBUMIN (warfarin, NSA, fenytoin)",
          "Zásadité léky → OROSOMUKOID (α1-kyselý glykoprotein)",
          "⚠️ Vázaná frakce NEPŮSOBÍ a nefiltruje se",
          "⚠️ Nízký albumin (senior, cirhóza, nefrotický sy, popáleniny)",
          "→ volné frakce přibude → účinek i toxicita při „normální\" dávce"], "cervena"),
      ("DISTRIBUČNÍ OBJEM Vd", [
          "Zdánlivý objem — poměr dávky a koncentrace v plazmě",
          "Není to skutečný objem těla",
          "Malý Vd → lék zůstává v krvi (heparin)",
          "⚠️ Velký Vd → schovaný ve tkáních; dialýza ho nedostane ven (digoxin)"], "zelena"),
      ("REDISTRIBUCE", [
          "Lék se nejdřív dostane do dobře prokrvených orgánů (mozek)",
          "Pak se přelije do svalů a tuku",
          "⚠️ THIOPENTAL: krátký účinek je REDISTRIBUCÍ, ne odbouráním",
          "⚠️ Po opakovaných dávkách se tkáně nasytí → probuzení trvá hodiny"], "modra"),
      ("BARIÉRY A ZVLÁŠTNÍ PROSTORY", [
          "Hematoencefalická, placentární, krev–varle, krev–sítnice",
          "Mateřské mléko (mírně kyselé → zásadité léky se v něm hromadí)",
          "Tuková tkáň jako depo (thiopental, THC, amiodaron)"], "bila"),
  ],
  mnemo="Volná frakce působí. Vázaná čeká ve skladu.",
  zubar="⚠️ NSA a warfarin soutěží o albumin — u antikoagulovaného pacienta to po "
        "extrakci znamená vyšší riziko krvácení. Volit paracetamol.",
  past="Ve zdroji je překlep „oxomukoid\" — správně je OROSOMUKOID.")

S("O15", "Eliminace, poločas, fáze α a β, eliminační konstanta, clearance",
  jadro="Pokles hladiny má dvě fáze — a jen ta druhá znamená, že lék z těla skutečně mizí.",
  tok=[("podání", "zelena"), ("FÁZE α distribuce do tkání", "cervena"),
       ("FÁZE β skutečná eliminace", "zelena")],
  tok_popisky=["rychlý pokles", "pomalý pokles"],
  karty=[
      ("DVĚ FÁZE POKLESU", [
          "α — distribuční: lék se jen PŘESTĚHOVAL do tkání, neodbourává se",
          "⚠️ Tím končí účinek thiopentalu",
          "β — eliminační: teď se lék skutečně metabolizuje a vylučuje",
          "⚠️ Biologický poločas se počítá z fáze β"], "zelena"),
      ("POLOČAS t½", [
          "Doba, za kterou klesne hladina na polovinu",
          "⚠️ Za 4–5 poločasů je lék prakticky pryč (a stejně dlouho trvá ustálený stav)",
          "Závisí na Vd A na clearance zároveň",
          "Delší poločas → delší interval mezi dávkami"], "modra"),
      ("CLEARANCE", [
          "Objem krve zcela očištěný od léku za jednotku času",
          "Celková CL = jaterní + renální + ostatní",
          "⚠️ Klesá při selhání jater a ledvin → nutná redukce dávky",
          "Eliminační konstanta ke = CL / Vd"], "bila"),
      ("CO POLOČAS PRODLUŽUJE", [
          "Selhání ledvin nebo jater",
          "Vysoký věk, nízký srdeční výdej",
          "Interakce s inhibitorem enzymů",
          "⚠️ Velký distribuční objem (lék se schovává ve tkáních)"], "cervena"),
  ],
  mnemo="α = přestěhování. β = odchod. Čtyři až pět poločasů oběma směry.",
  zubar="Poločas ti řekne, jak dlouho ještě působí lék, který pacient bral ráno — "
        "u sedativ a opioidů je to důležité před výkonem.",
  past="Rychlý pokles hladiny neznamená, že je lék pryč — u thiopentalu je to jen "
       "přesun do tuku a svalů, ze kterých se pak vrací.")

S("O16", "Dávkovací režim, kumulace, kumulační index",
  jadro="Tělo je vana: kohoutek je dávkování, odtok je eliminace. Ustálený stav je "
        "chvíle, kdy přitéká stejně, jako odtéká.",
  tok=[("NASYCOVACÍ DÁVKA naplní vanu naráz", "zelena"),
       ("UDRŽOVACÍ DÁVKA dorovnává, co odteče", "zelena"),
       ("USTÁLENÝ STAV za 4–5 poločasů", "modra")],
  karty=[
      ("NASYCOVACÍ × UDRŽOVACÍ DÁVKA", [
          "Nasycovací — řídí ji DISTRIBUČNÍ OBJEM (Vd)",
          "Udržovací — řídí ji CLEARANCE",
          "⚠️ Nasycovací se dává tam, kde se nedá čekat 4–5 poločasů",
          "Příklady: digoxin, amiodaron, některá antibiotika"], "zelena"),
      ("KUMULACE", [
          "Nastane, když se podává rychleji, než tělo stíhá eliminovat",
          "Kumulační index — o kolik hladina vzroste proti jedné dávce",
          "⚠️ Roste při selhání ledvin a jater",
          "⚠️ Nebezpečná u léků s úzkým oknem (digoxin, lithium, aminoglykosidy)"], "cervena"),
      ("DÁVKOVACÍ INTERVAL", [
          "Obvykle se odvozuje od poločasu",
          "Kratší interval → menší kolísání hladiny, horší spolupráce pacienta",
          "Retardovaná forma umožní podávat 1× denně",
          "⚠️ Časově závislá ATB potřebují častěji, koncentračně závislá naopak 1× denně"], "bila"),
      ("TERAPEUTICKÉ MONITOROVÁNÍ (TDM)", [
          "Měří se hladina léku v krvi",
          "⚠️ Jen u léků s úzkým oknem a nejasným vztahem dávky a účinku",
          "Digoxin, lithium, theofylin, fenytoin, vankomycin, aminoglykosidy",
          "Odběr v přesně daném čase (údolní hladina před další dávkou)"], "modra"),
  ],
  mnemo="Nasycovací naplní vanu, udržovací ji drží plnou. Rovnováha za 4–5 poločasů.",
  zubar="U antibiotické profylaxe endokarditidy se dává jedna vysoká dávka krátce "
        "před výkonem — cílem je vysoká hladina v době bakteriemie, ne ustálený stav.",
  past="Ustálený stav přijde vždy za 4–5 poločasů, ať dáváš jakkoli velkou udržovací "
       "dávku. Zrychlí ho jen dávka nasycovací.")

S("O17", "Biotransformace léčiv, fáze, příklady",
  jadro="Cílem přeměny je udělat z lipofilní látky hydrofilní, aby ji šlo vyloučit — "
        "jenže občas přitom vznikne něco jedovatějšího, než byl původní lék.",
  tok=[("PARACETAMOL", "zelena"), ("90 % konjugace → neškodné", "bila"),
       ("10 % CYP2E1 → ⚠️ NAPQI", "cervena"), ("GLUTATHION ho zneškodní", "zelena")],
  karty=[
      ("FÁZE I — funkcionalizace", [
          "Oxidace, redukce, hydrolýza — hlavně systém CYP450",
          "Přidá nebo odhalí reaktivní skupinu (−OH, −NH₂, −SH)",
          "⚠️ Produkt může být účinnější nebo toxičtější než výchozí látka",
          "Hlavní izoformy: CYP3A4 (nejvíc léčiv), CYP2D6, CYP2C9, CYP2C19, CYP1A2"], "zelena"),
      ("FÁZE II — konjugace", [
          "Glukuronidace, sulfatace, acetylace, methylace, konjugace s glutathionem",
          "Přilepí velkou polární skupinu → látka se stane vylučitelnou",
          "⚠️ Produkt je zpravidla neúčinný (výjimka: morfin-6-glukuronid)",
          "⚠️ U novorozence glukuronidace nefunguje → gray baby, jádrový ikterus"], "modra"),
      ("PROLÉČIVA (prodrugs)", [
          "Podává se neúčinná forma, tělo ji aktivuje",
          "⚠️ Kodein → morfin (CYP2D6) · klopidogrel (CYP2C19)",
          "Enalapril → enalaprilát · cyklofosfamid · levodopa · aciklovir",
          "⚠️ U pomalého metabolizátora proléčivo nezabere"], "bila"),
      ("KDE SE TO DĚJE", [
          "Hlavně JÁTRA (hladké endoplazmatické retikulum)",
          "Také střevní stěna, plíce, ledviny, plazma (esterázy)",
          "⚠️ Otrava paracetamolem: nasycení konjugace → víc NAPQI → vyčerpaný",
          "glutathion → nekróza jater; antidotum N-ACETYLCYSTEIN"], "cervena"),
  ],
  mnemo="Fáze I odhalí háček, fáze II na něj pověsí závaží. Pak to jde ven.",
  zubar="⚠️ Alkoholik má indukovaný CYP2E1 A vyčerpaný glutathion — paracetamol u něj "
        "může poškodit játra i v běžné dávce. Po extrakci volit nižší dávku a spíš ibuprofen.",
  past="Metabolit není automaticky neškodný. NAPQI, norpetidin a acetaldehyd jsou "
       "toxičtější než výchozí látka.")

S("O18", "Úloha jater v eliminaci léčiv, first-pass efekt",
  jadro="Všechno, co polkneš, jde nejdřív přes játra — a část z toho se do těla vůbec nedostane.",
  tok=[("100 % polknuté dávky", "zelena"), ("střevní stěna", "bila"),
       ("⚠️ JÁTRA portální oběh", "cervena"), ("do těla dorazí třeba 10 %", "bila")],
  karty=[
      ("FIRST-PASS EFEKT", [
          "Ztráta léku při prvním průchodu střevem a játry",
          "Snižuje biologickou dostupnost, někdy až na jednotky procent",
          "⚠️ Vysoký first-pass: nitroglycerin, morfin, propranolol, testosteron,",
          "lidokain, verapamil, isosorbid dinitrát"], "cervena"),
      ("JAK SE OBCHÁZÍ", [
          "Sublingválně a bukálně",
          "Nitrožilně, nitrosvalově, podkožně",
          "Transdermálně (náplast)",
          "⚠️ Rektálně jen částečně — dolní část konečníku ano, horní ne"], "zelena"),
      ("JATERNÍ CLEARANCE", [
          "Léky s vysokou extrakcí — clearance závisí na PRŮTOKU játry",
          "→ srdeční selhání a šok jejich hladinu zvednou",
          "Léky s nízkou extrakcí — závisí na ENZYMOVÉ kapacitě a volné frakci",
          "→ mění je indukce, inhibice a nízký albumin"], "modra"),
      ("PACIENT S POSTIŽENÝMI JÁTRY", [
          "Nižší metabolická kapacita → kumulace",
          "Nízký albumin → vyšší volná frakce",
          "Portosystémové zkraty → obejde se first-pass → prudký vzestup hladiny",
          "⚠️ Snížená tvorba koagulačních faktorů → krvácivost"], "bila"),
  ],
  mnemo="Co jde ústy, jde přes játra. Co jde pod jazyk, do žíly nebo na kůži, ne.",
  zubar="⚠️ Pacient s jaterní cirhózou: paracetamol v redukované dávce, NSA raději "
        "vůbec (krvácivost + ledviny), pozor na lokální anestetika amidového typu.",
  past="Nitroglycerin se nesmí polknout — first-pass ho zničí. Proto pod jazyk.")

S("O19", "Inhibice a indukce enzymů léčivy, klinický význam",
  jadro="Inhibitor je brzda a působí hned. Induktor je plyn a rozjíždí se dny — "
        "a stejně pomalu se pak zastavuje.",
  karty=[
      ("INHIBICE — hladina STOUPNE", [
          "Enzym přestane pracovat prakticky ihned",
          "⚠️ Makrolidy (erythromycin, klarithromycin — ne azithromycin)",
          "⚠️ Azolová antimykotika, ⚠️ GRAPEFRUIT, ritonavir, amiodaron, verapamil",
          "⚠️ Důsledek: PŘEDÁVKOVÁNÍ druhým lékem"], "cervena"),
      ("INDUKCE — hladina KLESNE", [
          "Enzymu se musí narobit → nástup dny až týdny",
          "⚠️ RIFAMPICIN, karbamazepin, fenytoin, fenobarbital",
          "⚠️ TŘEZALKA, ⚠️ KOUŘENÍ (CYP1A2), alkohol chronicky (CYP2E1)",
          "⚠️ Důsledek: SELHÁNÍ LÉČBY (antikoncepce, warfarin, imunosupresiva)"], "cervena"),
      ("NEBEZPEČNÝ KONEC INDUKCE", [
          "Po vysazení induktoru se enzymy ještě týdny odbourávají",
          "⚠️ Hladina druhého léku pak vyskočí nahoru",
          "⚠️ Kuřák, který přestane kouřit: stoupne theofylin, olanzapin, klozapin"], "modra"),
      ("KLINICKY NEJDŮLEŽITĚJŠÍ DVOJICE", [
          "Rifampicin × hormonální antikoncepce → selhání",
          "Klarithromycin × statin → rabdomyolýza",
          "Azol × warfarin → krvácení",
          "Třezalka × cyklosporin → rejekce štěpu",
          "⚠️ Proléčivo + inhibitor = žádný účinek (klopidogrel + omeprazol)"], "bila"),
  ],
  mnemo="Inhibitor brzdí HNED. Induktor rozjíždí POMALU — a doznívá taky pomalu.",
  zubar="⚠️ Než předepíšeš makrolid nebo azolové antimykotikum, zkontroluj, co pacient "
        "bere. Klarithromycin u pacienta na statinu nebo warfarinu je reálné riziko; "
        "azithromycin je v tomhle bezpečnější.",
  past="U proléčiva funguje inhibitor OPAČNĚ — nezvýší hladinu účinné látky, "
       "ale zabrání jejímu vzniku.")

S("O20", "Vylučování léčiv renální a extrarenální",
  jadro="Ledvina lék filtruje, aktivně vylučuje — a část si ho bere zpátky. "
        "Ten třetí děj se dá lékařsky využít.",
  tok=[("GLOMERULÁRNÍ FILTRACE jen VOLNÁ frakce", "zelena"),
       ("TUBULÁRNÍ SEKRECE aktivní, i vázané léky", "zelena"),
       ("⚠️ TUBULÁRNÍ RESORPCE nenabité se vrací zpět", "cervena"), ("MOČ", "bila")],
  karty=[
      ("TŘI DĚJE V LEDVINĚ", [
          "Filtrace — jen volná frakce, podle glomerulární filtrace",
          "Sekrece — aktivní přenašeče pro kyseliny a zásady; ⚠️ soutěž (probenecid × penicilin)",
          "Resorpce — pasivní, zpět se vstřebá jen NENABITÁ forma"], "zelena"),
      ("VYUŽITÍ: ALKALIZACE MOČI", [
          "Zásaditá moč udrží kyselý lék v nabité formě",
          "→ nevstřebá se zpět → rychleji odejde",
          "⚠️ Otrava aspirinem, barbituráty",
          "Iontová past — stejný princip jako u anestezie v zaníceném zubu"], "modra"),
      ("EXTRARENÁLNÍ CESTY", [
          "Žlučí a stolicí — ⚠️ ENTEROHEPATÁLNÍ OBĚH prodlužuje účinek",
          "Plícemi — inhalační anestetika, etanol (dechová zkouška)",
          "Mlékem — ⚠️ zásadité léky se v mírně kyselém mléce hromadí",
          "Slinami, potem, vlasy (toxikologický průkaz)"], "bila"),
      ("PACIENT SE SELHÁNÍM LEDVIN", [
          "⚠️ Kumulace léků vylučovaných ledvinami",
          "Redukce dávky nebo prodloužení intervalu podle glomerulární filtrace",
          "⚠️ Digoxin, aminoglykosidy, lithium, metformin, DOAC",
          "⚠️ U seniora klame kreatinin — počítá se odhad filtrace"], "cervena"),
  ],
  mnemo="Filtruje se volné. Vylučuje se aktivně. Vrací se nenabité.",
  zubar="⚠️ U pacienta s renální insuficiencí opatrně s NSA (zhorší funkci) a "
        "s antibiotiky vylučovanými ledvinami — dávka se upravuje.",
  past="Enterohepatální oběh je důvod, proč některé léky působí déle, než odpovídá "
       "jejich poločasu — a proč je průjem nebo antibiotikum může „vypnout\".")

S("O21", "Účinek léčiv obecně, způsob účinku na molekulární úrovni",
  jadro="Léčivo buď sedí na konkrétní cílové struktuře, nebo působí prostou fyzikální "
        "chemií — a to druhé potřebuje mnohem větší dávky.",
  karty=[
      ("SPECIFICKÝ ÚČINEK", [
          "Přes konkrétní cílovou strukturu",
          "RECEPTOR — agonista, antagonista, parciální agonista",
          "ENZYM — inhibitor (statiny, ACE inhibitory, NSA)",
          "IONTOVÝ KANÁL — blokátory Na⁺, Ca²⁺, K⁺",
          "PŘENAŠEČ — SSRI, glifloziny, omeprazol (pumpa)",
          "⚠️ Působí v malých dávkách"], "zelena"),
      ("NESPECIFICKÝ ÚČINEK", [
          "Fyzikálně-chemický, bez cílové struktury",
          "Antacida (neutralizace), osmotická laxativa a diuretika",
          "Adsorbencia (aktivní uhlí), dezinficiencia, chelátory",
          "⚠️ Potřebuje velké dávky"], "bila"),
      ("PODLE VÝSLEDKU LÉČBY", [
          "Kauzální — odstraní příčinu (antibiotikum, antidotum)",
          "Symptomatická — uleví od projevu (analgetikum, antipyretikum)",
          "Substituční — nahradí, co chybí (inzulin, levothyroxin, vitaminy)",
          "Profylaktická — předchází (vakcína, antikoagulancium)"], "modra"),
      ("DALŠÍ POJMY", [
          "Selektivita — jak přesně lék trefí jen zamýšlený cíl",
          "Afinita — jak pevně se váže · vnitřní aktivita — co po navázání spustí",
          "⚠️ Selektivita není absolutní a s dávkou mizí",
          "(β1-selektivní betablokátor ve vysoké dávce blokuje i β2)"], "zluta"),
  ],
  mnemo="Specifický = klíč do zámku. Nespecifický = kladivo.",
  zubar="Fluorid působí obojím způsobem: chemicky mění hydroxyapatit na fluoroapatit "
        "a zároveň tlumí metabolismus bakterií v plaku.",
  past="Selektivita platí jen v terapeutickém rozmezí. Ve vysoké dávce ji ztratí "
       "prakticky každý lék.")

S("O22", "Specifický účinek, cílové struktury, receptorová teorie, typy receptorů",
  jadro="Typ receptoru určuje, za jak dlouho lék zabere — od milisekund po hodiny.",
  tok=[("IONOTROPNÍ milisekundy", "zelena"), ("G-PROTEIN sekundy", "bila"),
       ("ENZYMOVÝ minuty", "bila"), ("NITROBUNĚČNÝ hodiny", "cervena")],
  karty=[
      ("ČTYŘI TYPY RECEPTORŮ", [
          "Ionotropní — sám je iontový kanál: nikotinový, GABA-A, NMDA",
          "Spřažený s G-proteinem — muskarinový, adrenergní, opioidní, histaminový",
          "S vlastní enzymovou aktivitou — inzulinový, receptory růstových faktorů",
          "⚠️ Nitrobuněčný — mění PŘEPIS GENŮ: kortikoidy, hormony štítnice, pohlavní hormony"], "zelena"),
      ("TYPY LIGANDŮ", [
          "Agonista — váže se a spustí plný účinek",
          "Parciální agonista — spustí jen část; ⚠️ má strop (buprenorfin, aripiprazol)",
          "Antagonista — váže se a nespustí nic, brání agonistovi",
          "⚠️ Inverzní agonista — sníží i klidovou aktivitu receptoru"], "modra"),
      ("KOMPETITIVNÍ × NEKOMPETITIVNÍ", [
          "Kompetitivní antagonista — soutěží o stejné místo",
          "⚠️ Dá se překonat vyšší dávkou agonisty (naloxon × morfin)",
          "Nekompetitivní — váže se jinam nebo nevratně",
          "⚠️ Vyšší dávkou agonisty se překonat NEDÁ (aspirin na COX)"], "cervena"),
      ("REGULACE POČTU RECEPTORŮ", [
          "Down-regulace — při nadbytku podnětu receptorů ubývá → tolerance",
          "⚠️ Up-regulace — při blokádě jich přibývá",
          "→ proto se betablokátor NIKDY nevysazuje náhle (rebound)",
          "Desenzibilizace — receptor přestane odpovídat i beze změny počtu"], "bila"),
  ],
  mnemo="Kanál = milisekundy. Gen = hodiny. Proto adrenalin zachrání anafylaxi a kortikoid ne.",
  zubar="Lokální anestetikum blokuje sodíkový kanál zevnitř — proto se musí nejdřív "
        "dostat přes membránu v nenabité formě.",
  past="Kortikoid má nástup hodiny, protože musí projít jádrem. U anafylaxe je proto "
       "vždy první adrenalin.")

S("O23", "Dávka a účinek, terapeutický index, terapeutické okno, riziko, NNT",
  jadro="Jediná vlastnost rozhoduje, jestli se lék monitoruje: šířka terapeutického okna.",
  karty=[
      ("KŘIVKA DÁVKA–ÚČINEK", [
          "ED₅₀ — dávka účinná u poloviny · TD₅₀ toxická · LD₅₀ letální",
          "Terapeutický index = TD₅₀ / ED₅₀ — čím vyšší, tím bezpečnější",
          "Účinnost (efficacy) — jak velký účinek lék umí vůbec vyvolat",
          "Potence — jak malá dávka k tomu stačí"], "zelena"),
      ("⚠️ ÚZKÉ TERAPEUTICKÉ OKNO", [
          "DIGOXIN · LITHIUM · WARFARIN · THEOFYLIN",
          "FENYTOIN · AMINOGLYKOSIDY · CYTOSTATIKA · vankomycin",
          "⚠️ Účinná a toxická dávka skoro splývají",
          "⚠️ Proto se u nich MĚŘÍ HLADINY"], "cervena"),
      ("HODNOCENÍ PŘÍNOSU", [
          "NNT — kolik pacientů léčit, aby jeden měl prospěch (nižší = lepší)",
          "NNH — kolik léčit, než jeden utrpí škodu (vyšší = lepší)",
          "Absolutní × relativní snížení rizika",
          "⚠️ Relativní číslo zní vždy působivěji — proto se v reklamě používá"], "modra"),
      ("POMĚR PŘÍNOS / RIZIKO", [
          "Vždy se posuzuje v kontextu konkrétního pacienta a nemoci",
          "U banální nemoci se toleruje jen minimální riziko",
          "U onkologické léčby se toleruje riziko velké",
          "⚠️ Bezpečný lék neexistuje, existuje jen přijatelné riziko"], "bila"),
  ],
  mnemo="Digoxin, lithium, warfarin, theofylin, fenytoin — u těch se měří hladiny.",
  zubar="Analgetika mají široké okno — kromě paracetamolu, kde je hranice denní dávky "
        "(4 g) a překročení znamená jaterní selhání.",
  past="Vysoká potence neznamená vysoká účinnost. Potence je jen o velikosti dávky.")

S("O24", "Vlivy působící na kinetiku a dynamiku léčiv",
  jadro="Stejná dávka stejného léku má u dvou lidí různý účinek — a je to předvídatelné.",
  karty=[
      ("VĚK", [
          "Novorozenec — ⚠️ nezralá glukuronidace, 75 % vody, málo albuminu",
          "Dítě — dávkuje se na povrch těla, ne na hmotnost",
          "Senior — ⚠️ méně vody a víc tuku, horší ledviny, polypragmazie",
          "⚠️ U seniora klame kreatinin"], "zelena"),
      ("ORGÁNOVÉ FUNKCE A NEMOCI", [
          "Játra — nižší metabolismus, nízký albumin, zkraty",
          "Ledviny — kumulace vylučovaných léčiv",
          "Srdeční selhání — horší prokrvení střeva a jater",
          "Štítná žláza, horečka, dehydratace, obezita"], "modra"),
      ("GENETIKA A POHLAVÍ", [
          "⚠️ Pomalý × rychlý × ultrarychlý metabolizátor (CYP2D6, CYP2C19)",
          "Acetylátorský status (izoniazid)",
          "Ženy: jiné složení těla, hormonální cyklus, gravidita",
          "Etnické rozdíly (HLA-B*1502, HLA-B*5801)"], "bila"),
      ("VNĚJŠÍ VLIVY", [
          "⚠️ Jiné léky — indukce, inhibice, kompetice",
          "⚠️ Strava — grapefruit, mléko, vitamin K, tyramin",
          "Kouření (CYP1A2), alkohol (CYP2E1)",
          "Denní doba (chronofarmakologie), tělesná zátěž"], "cervena"),
  ],
  mnemo="Věk · orgány · geny · ostatní léky · jídlo. Pět důvodů, proč dávka není univerzální.",
  zubar="Před předpisem analgetika nebo antibiotika se ptej na: věk, ledviny a játra, "
        "těhotenství, alergie a ostatní léky. Pět otázek, které zabrání většině chyb.",
  past="„Standardní dávka\" je jen výchozí bod. U seniora, dítěte a nemocných jater "
       "nebo ledvin se musí upravit.")

S("O25", "Lékové interakce",
  jadro="Dva léky si mohou vjet do vlasů dvěma zcela různými cestami: buď si mění "
        "hladinu, nebo si mění účinek.",
  karty=[
      ("FARMAKOKINETICKÉ — mění HLADINU", [
          "Vstřebávání: ⚠️ antacida a mléko chelatují tetracykliny a chinolony",
          "Vazba na bílkoviny: vytěsnění z albuminu (NSA × warfarin)",
          "⚠️ Metabolismus: indukce a inhibice CYP",
          "Vylučování: soutěž o tubulární sekreci (probenecid × penicilin)"], "zelena"),
      ("FARMAKODYNAMICKÉ — mění ÚČINEK", [
          "Sčítání: alkohol + benzodiazepin + opioid → útlum dechu",
          "Rušení: naloxon × morfin, vitamin K × warfarin",
          "Nepřímé: NSA zvyšují tlak a ruší efekt antihypertenziv",
          "⚠️ Prodloužení QT: makrolid + antipsychotikum + ondansetron"], "modra"),
      ("TYPY VÝSLEDKU", [
          "Aditivní 1 + 1 = 2",
          "Synergie 1 + 1 = 5",
          "⚠️ Potenciace 0 + 1 = 5 (látka sama neúčinná zesílí druhou)",
          "Antagonismus — základ všech antidot"], "zluta"),
      ("⚠️ INTERAKCE, KTERÉ MUSÍŠ ZNÁT", [
          "„Triple whammy\": NSA + ACE inhibitor + diuretikum → selhání ledvin",
          "Ibuprofen ruší antiagregační účinek aspirinu",
          "Rifampicin a třezalka ruší hormonální antikoncepci",
          "Makrolid + statin → rabdomyolýza",
          "IMAO + tyramin → hypertenzní krize · IMAO + SSRI → serotoninový syndrom"], "cervena"),
  ],
  mnemo="Kinetická mění KOLIK. Dynamická mění CO to udělá.",
  zubar="Nejčastější interakce v zubní ordinaci: ⚠️ NSA × warfarin (krvácení), "
        "makrolid a azol × statin, adrenalin v anestetiku × tricyklika a kokain.",
  past="Interakce se počítají geometricky. U pacienta s osmi léky je nikdo neuhlídá "
       "z hlavy — proto existují kontrolní programy.")

S("O26", "Farmakogenetika, genetický polymorfismus",
  jadro="Stejná dávka: jeden pacient nemá žádný účinek, druhý je otrávený. "
        "Často za to může jediný enzym.",
  tok=[("POMALÝ metabolizátor lék se hromadí", "cervena"),
       ("NORMÁLNÍ očekávaný účinek", "zelena"),
       ("ULTRARYCHLÝ lék zmizí dřív, než zabere", "cervena")],
  karty=[
      ("⚠️ POZOR — U PROLÉČIVA JE TO OBRÁCENĚ", [
          "Kodein je proléčivo, aktivuje ho CYP2D6 na morfin",
          "⚠️ Ultrarychlý metabolizátor udělá morfinu příliš — popsána úmrtí dětí",
          "⚠️ Pomalý metabolizátor nemá analgetický účinek žádný",
          "Totéž klopidogrel (CYP2C19) — pomalý metabolizátor není chráněný"], "cervena"),
      ("KLÍČOVÉ ENZYMY", [
          "CYP2D6 — kodein, tramadol, tricyklika, betablokátory, antipsychotika",
          "CYP2C19 — klopidogrel, omeprazol, diazepam",
          "CYP2C9 — warfarin, fenytoin, NSA",
          "N-acetyltransferáza — izoniazid (rychlí × pomalí acetylátoři)"], "zelena"),
      ("NEENZYMOVÉ POLYMORFISMY", [
          "⚠️ TPMT — azathioprin; nízká aktivita → těžká myelosuprese",
          "⚠️ Plazmatická cholinesteráza — sukcinylcholin → apnoe na hodiny",
          "⚠️ Deficit G6PD — hemolýza po primachinu, sulfonamidech, nitrofurantoinu",
          "Ryanodinový receptor — maligní hypertermie"], "modra"),
      ("HLA A ZÁVAŽNÉ REAKCE", [
          "⚠️ HLA-B*5701 — abakavir: testuje se PŘED nasazením",
          "⚠️ HLA-B*1502 — karbamazepin a Stevensův–Johnsonův syndrom (asijská populace)",
          "⚠️ HLA-B*5801 — alopurinol a hypersenzitivní syndrom",
          "Idiosynkrazie — reakce nezávislá na dávce, geneticky podmíněná"], "bila"),
  ],
  mnemo="U běžného léku pomalý metabolizátor = předávkování. U PROLÉČIVA přesně naopak.",
  zubar="⚠️ Kodein v analgetické kombinaci: u části pacientů nezabere vůbec a u části "
        "je nebezpečný. Ibuprofen + paracetamol je předvídatelnější volba.",
  past="Rodinná anamnéza „po narkóze se dlouho nemohl probrat\" je varování před "
       "atypickou pseudocholinesterázou nebo maligní hypertermií.")

S("O27", "Tolerance, tachyfylaxe, rezistence",
  jadro="Otupí se pacient, nebo se změnil patogen? To je celý rozdíl mezi tolerancí a rezistencí.",
  karty=[
      ("TOLERANCE", [
          "Slábne odpověď ORGANISMU, vzniká dny až týdny",
          "Mechanismy: down-regulace receptorů, indukce enzymů, protiregulace",
          "⚠️ Zkřížená tolerance — mezi látkami stejné skupiny",
          "⚠️ Netoleruje se: mióza a zácpa u opioidů"], "zelena"),
      ("TACHYFYLAXE", [
          "Prudký pokles účinku během hodin",
          "⚠️ Nepřímá sympatomimetika — vyčerpané zásoby noradrenalinu",
          "Nitráty — proto nitrátový interval 8–12 h denně",
          "Nosní dekongescencia — proto max 7 dní"], "cervena"),
      ("REZISTENCE", [
          "Změnil se PATOGEN nebo nádorová buňka, ne pacient",
          "⚠️ Betalaktamázy · změna cílové struktury (MRSA, PBP2a)",
          "⚠️ Efluxní pumpy · snížená propustnost stěny",
          "Roste s používáním antibiotik — proto antibiotická stewardship"], "modra"),
      ("PŘÍBUZNÉ POJMY", [
          "Závislost — psychická (craving) a fyzická (odvykací stav)",
          "Senzibilizace — opak tolerance, odpověď se zesiluje",
          "⚠️ Rebound fenomén — po vysazení návrat příznaků silněji",
          "(betablokátory, nitráty, benzodiazepiny, PPI, kortikoidy)"], "bila"),
  ],
  mnemo="Tolerance = dny. Tachyfylaxe = hodiny. Rezistence = jiný organismus.",
  zubar="⚠️ Rezistence orální flóry je důvod, proč se antibiotikum nedává „pro jistotu\". "
        "U abscesu rozhoduje drenáž, ne recept.",
  past="Up-regulace receptorů při chronické blokádě je důvod, proč se betablokátor "
       "nikdy nevysazuje náhle.")

S("O28", "Vliv průvodních onemocnění, polypragmazie",
  jadro="Každý přidaný lék není jen „+1\" — počet možných interakcí roste geometricky.",
  tok=[("nový příznak", "bila"), ("je to nežádoucí účinek?", "cervena"),
       ("⚠️ nasadí se DALŠÍ lék", "cervena"), ("PRESKRIPČNÍ KASKÁDA", "cervena")],
  karty=[
      ("POLYPRAGMAZIE", [
          "Obvykle 5 a více léků současně",
          "⚠️ Interakce rostou geometricky — u osmi léků je z hlavy neuhlídáš",
          "Horší adherence — pacient přestane brát i to důležité",
          "Vyšší riziko pádů, hospitalizací a nežádoucích účinků"], "cervena"),
      ("⚠️ PRESKRIPČNÍ KASKÁDA — příklady", [
          "Blokátor Ca → otoky kotníků → nasadí se diuretikum (a nepomůže)",
          "NSA → zvýšený tlak → nasadí se antihypertenzivum",
          "Metoklopramid → parkinsonismus → nasadí se antiparkinsonikum",
          "⚠️ Vždy nejdřív zvaž: není nový příznak nežádoucím účinkem?"], "cervena"),
      ("NEMOC MĚNÍ KINETIKU", [
          "Játra — nižší metabolismus, nízký albumin",
          "Ledviny — kumulace, nutná úprava dávky",
          "Srdeční selhání — horší prokrvení střeva a jater",
          "Štítná žláza, sepse, dehydratace, popáleniny"], "modra"),
      ("JAK SE TO ŘEŠÍ", [
          "Pravidelná revize medikace (deprescribing)",
          "⚠️ STOPP — co vysadit · ⚠️ START — co CHYBÍ a má se nasadit",
          "Beersova kritéria — léky nevhodné u seniorů",
          "Fixní kombinace a dávkování 1× denně"], "bila"),
  ],
  mnemo="Nový příznak u pacienta s mnoha léky = do prokázání opaku nežádoucí účinek.",
  zubar="Seznam léků pacienta je pro zubaře zdroj informací o jeho nemocech — "
        "bisfosfonáty, antikoagulancia, imunosupresiva a antiepileptika mění postup ošetření.",
  past="Podléčení je stejný problém jako předávkování — proto existuje i kritérium "
       "START, ne jen STOPP.")

S("O29", "Nežádoucí účinky léčiv",
  jadro="Typ A vyplývá z mechanismu a řeší se snížením dávky. Typ B s ním nesouvisí "
        "a řeší se jen okamžitým vysazením.",
  karty=[
      ("TYP A — „Augmented\"", [
          "Vyplývá z farmakologického mechanismu léku",
          "⚠️ ZÁVISLÝ NA DÁVCE, předvídatelný",
          "Častý, obvykle méně závažný",
          "Krvácení po warfarinu, sucho v ústech po atropinu, hypoglykemie po inzulinu",
          "→ řeší se SNÍŽENÍM DÁVKY"], "zelena"),
      ("TYP B — „Bizarre\"", [
          "S mechanismem nesouvisí",
          "⚠️ NEZÁVISLÝ NA DÁVCE, nepředvídatelný",
          "Vzácný, ale často závažný",
          "Alergie, agranulocytóza, aplastická anemie, maligní hypertermie",
          "→ ⚠️ řeší se VYSAZENÍM a lék se už nikdy nepodá"], "cervena"),
      ("DALŠÍ TYPY (rozšířené dělení)", [
          "C — chronické, při dlouhodobém podávání (osteoporóza po kortikoidech)",
          "D — delayed, opožděné (karcinogenita, teratogenita)",
          "E — end of use, po vysazení (rebound)",
          "F — failure, selhání léčby (interakce s induktorem)"], "modra"),
      ("FARMAKOVIGILANCE", [
          "Sledování bezpečnosti léčiv po registraci",
          "⚠️ Hlášení podezření na NÚ na SÚKL — povinnost zdravotníka",
          "Hlásí se hlavně: závažné, neočekávané a u nových léčiv (▼)",
          "Signál → přehodnocení → změna SPC nebo stažení z trhu"], "bila"),
  ],
  mnemo="A jako Augmented — zesílený účinek. B jako Bizarre — s lékem to nesouvisí.",
  zubar="Nejčastější NÚ v zubní ordinaci: alergie na anestetikum nebo antibiotikum, "
        "xerostomie z chronické medikace, hyperplazie gingivy, osteonekróza čelisti.",
  past="Typ B nelze předvídat z dávky ani z mechanismu — proto se u něj lék "
       "kontraindikuje natrvalo, ne jen sníží.")

S("O30", "Léková alergie, idiosynkrazie",
  jadro="Ne každá „reakce na lék\" je alergie. Alergie potřebuje imunitu a předchozí "
        "setkání — idiosynkrazie ani jedno.",
  karty=[
      ("ALERGIE", [
          "Zapojený IMUNITNÍ systém",
          "⚠️ Nutná předchozí SENZIBILIZACE — při prvním podání nevznikne",
          "⚠️ Nezávisí na dávce — stačí stopové množství",
          "Coombs: I. IgE (anafylaxe) · II. cytotoxická · III. imunokomplexová · IV. pozdní"], "cervena"),
      ("IDIOSYNKRAZIE", [
          "Imunita v tom NENÍ",
          "Geneticky daná odchylka enzymu nebo receptoru",
          "⚠️ Může se objevit hned při prvním podání",
          "Hemolýza při deficitu G6PD, maligní hypertermie, apnoe po sukcinylcholinu"], "modra"),
      ("⚠️ ANAFYLAXE", [
          "Kožní projevy + dýchací obtíže + pokles tlaku, během minut",
          "⭐ ADRENALIN 0,5 mg i.m. do stehna — první a nenahraditelný",
          "⚠️ Antihistaminikum a kortikoid jsou jen doplněk a působí pozdě",
          "Poloha vleže s nohama nahoru, kyslík, tekutiny, volání pomoci"], "cervena"),
      ("ANAFYLAKTOIDNÍ REAKCE", [
          "Vypadá stejně, ale ⚠️ NEZPROSTŘEDKOVANÁ IgE",
          "Přímé uvolnění histaminu ze žírných buněk",
          "⚠️ Může přijít i při prvním podání",
          "Kontrastní látky, vankomycin („red man\"), morfin, NSA"], "bila"),
  ],
  mnemo="Alergie potřebuje druhé setkání. Idiosynkrazie stačí první.",
  zubar="⚠️ Ordinace musí mít adrenalin a nacvičený postup. Skutečná alergie na "
        "penicilin je vzácnější, než ji pacienti uvádějí — ⚠️ ale u anamnézy anafylaxe "
        "se betalaktamům vyhýbáme úplně (alternativa klindamycin).",
  past="Ampicilinový exantém u infekční mononukleózy NENÍ alergie — pacient "
       "smí penicilin v budoucnu dostat.")

S("O31", "Karcinogenní a mutagenní účinky",
  jadro="Mezi poškozením DNA a nádorem uplynou roky — proto se karcinogenita "
        "v klinické studii nikdy neprojeví.",
  tok=[("MUTAGEN poškodí DNA", "cervena"), ("mutace v klíčovém genu", "bila"),
       ("ztráta kontroly dělení", "bila"), ("⚠️ NÁDOR — po LETECH", "cervena")],
  karty=[
      ("POJMY", [
          "Mutagen — poškozuje DNA",
          "Karcinogen — vyvolává nádor (genotoxický × negenotoxický)",
          "Teratogen — poškozuje vývoj plodu",
          "⚠️ U genotoxických karcinogenů se nepředpokládá bezpečná prahová dávka"], "cervena"),
      ("JAK SE TESTUJE", [
          "⚠️ AMESŮV TEST — mutagenita na bakteriích (Salmonella), rychlý screening",
          "Testy na buněčných kulturách (chromozomové aberace, mikrojádra)",
          "Dlouhodobé studie na hlodavcích (2 roky)",
          "Epidemiologické studie u lidí"], "zelena"),
      ("KLASIFIKACE IARC", [
          "Skupina 1 — prokázaný karcinogen pro člověka",
          "2A — pravděpodobný · 2B — možný",
          "3 — nelze klasifikovat",
          "⚠️ Klasifikace vyjadřuje SÍLU DŮKAZU, ne velikost rizika"], "modra"),
      ("PŘÍKLADY V MEDICÍNĚ", [
          "⚠️ Cytostatika (alkylační) — riziko sekundárních nádorů",
          "⚠️ Imunosupresiva — lymfomy a kožní nádory",
          "Estrogeny bez gestagenu — karcinom endometria",
          "⚠️ Ionizující záření, tabák, alkohol, arzen, azbest"], "bila"),
  ],
  mnemo="Amesův test = bakterie místo let čekání.",
  zubar="⚠️ V ordinaci: ionizující záření (clonění, nejnižší dávka, ALARA) a rizikoví "
        "pacienti po transplantaci a na imunosupresi — vyšší riziko nádorů rtu a dutiny ústní.",
  past="Zařazení do skupiny 1 IARC znamená jistotu, že látka karcinogenní JE — "
       "ne že je nebezpečnější než látka ve skupině 2A.")

S("O32", "Léčiva v těhotenství, teratogenní účinek, léčiva v době kojení",
  jadro="Nejrizikovější doba je právě ta, kdy žena o těhotenství ještě neví.",
  tok=[("1.–2. týden „vše nebo nic\"", "bila"),
       ("⚠️ 3.–8. TÝDEN ORGANOGENEZE", "cervena"),
       ("9. týden–porod růst a zrání", "modra")],
  karty=[
      ("TŘI OBDOBÍ", [
          "1.–2. týden — buď potrat, nebo se nic nestane („vše nebo nic\")",
          "⚠️ 3.–8. týden — organogeneze: NEJVĚTŠÍ riziko strukturálních vad",
          "Od 9. týdne — funkční poruchy, poruchy růstu a zrání orgánů",
          "⚠️ Kolem porodu — útlum novorozence, odvykací stav"], "cervena"),
      ("⚠️ KLASICKÉ TERATOGENY", [
          "Isotretinoin (vitamin A) · thalidomid",
          "VALPROÁT — defekty neurální trubice, nižší IQ",
          "WARFARIN · ACE inhibitory a sartany",
          "Methotrexát · tetracykliny · lithium (Ebsteinova anomálie)",
          "⚠️ Alkohol — fetální alkoholový syndrom"], "cervena"),
      ("CO JE V GRAVIDITĚ BEZPEČNĚJŠÍ", [
          "Bolest: PARACETAMOL (⚠️ NSA ne ve 3. trimestru — uzávěr ductus arteriosus)",
          "Infekce: peniciliny, cefalosporiny, makrolidy",
          "Tlak: methyldopa, labetalol, nifedipin",
          "Antikoagulace: ⚠️ nízkomolekulární heparin (neprochází placentou)"], "zelena"),
      ("KOJENÍ", [
          "Do mléka přejde skoro každý lék, otázka je v jakém množství",
          "⚠️ Mléko je mírně kyselé → zásadité léky se v něm hromadí (iontová past)",
          "Vhodné: podat hned PO kojení, zvolit lék s krátkým poločasem",
          "⚠️ Nevhodné: cytostatika, radiofarmaka, lithium, amiodaron"], "bila"),
  ],
  mnemo="3.–8. týden = orgány se staví. Tam se dělají vady.",
  zubar="Plánované zákroky nejlépe ve 2. trimestru. ⚠️ Anestetikum s adrenalinem je "
        "v běžném množství přijatelné, ⚠️ tetracykliny nikdy, po výkonu paracetamol. "
        "⚠️ Rentgen jen při jasné indikaci a se stíněním.",
  past="Neléčená nemoc matky je pro plod často větší riziko než dobře zvolený lék — "
       "vysadit všechno není bezpečné řešení.")

S("O33", "Farmakoterapie v dětství",
  jadro="Dítě není malý dospělý — má kvalitativně jinou kinetiku, ne jen menší dávku.",
  tok=[("A vyšší pH žaludku", "bila"), ("D 75 % vody, málo albuminu", "bila"),
       ("⚠️ M fáze I ano, fáze II NE", "cervena"), ("E filtrace dozraje ve 2. roce", "bila")],
  karty=[
      ("ZMĚNY PODLE ADME", [
          "Absorpce — vyšší pH žaludku, pomalá pasáž, tenká kůže (větší vstřebání)",
          "Distribuce — 75 % vody, málo tuku, ⚠️ málo albuminu, nezralá HEB",
          "⚠️ Metabolismus — fáze I částečně, GLUKURONIDACE až kolem 2 let",
          "Exkrece — glomerulární filtrace dozrává v polovině 2. roku"], "zelena"),
      ("⚠️ TŘI SPECIFICKÉ NEŽÁDOUCÍ ÚČINKY", [
          "⚠️ REYEŮV SYNDROM — aspirin + dítě + viróza → jaterní encefalopatie",
          "⚠️ GRAY BABY — chloramfenikol, nezralá glukuronidace",
          "⚠️ TETRACYKLINY — barví zuby a ukládají se do kostí (do 8 let ne)",
          "⚠️ Jádrový ikterus — sulfonamid vytěsní bilirubin z albuminu"], "cervena"),
      ("DÁVKOVÁNÍ", [
          "⚠️ Podle POVRCHU TĚLA (m²), ne jen podle hmotnosti",
          "Metabolická aktivita sleduje spíš povrch než váhu",
          "Dítě má na svou hmotnost obrovský povrch",
          "Formy: sirupy, kapky, čípky; ⚠️ tablety malé děti nepolknou"], "modra"),
      ("PRAKTICKY", [
          "Bolest a horečka: paracetamol, ibuprofen (⚠️ ne aspirin)",
          "Mnoho léků není u dětí registrováno → podávání „off-label\"",
          "⚠️ Sladké sirupy při dlouhodobé léčbě → kaz",
          "Rodič musí dostat jasnou dávku v ml, ne „lžičku\""], "bila"),
  ],
  mnemo="První fáze funguje, druhá ne. A dávka na povrch, ne na váhu.",
  zubar="⚠️ Dlouhodobě podávané sirupy (antiepileptika, antibiotika) obsahují cukr → "
        "mnohočetný kaz. ⚠️ Tetracykliny do 8 let nikdy. ⚠️ Fluoridy dávkovat opatrně — "
        "nadbytek v době vývoje zubu působí fluorózu.",
  past="Jádrový ikterus vzniká ze součtu tří nezralostí: málo albuminu + nezralá "
       "glukuronidace + nevyvinutá hematoencefalická bariéra.")

S("O34", "Farmakoterapie ve stáří, polypragmazie",
  jadro="Distribuce se ve stáří mění dvěma protichůdnými směry najednou — "
        "a to je nejzajímavější věc celé otázky.",
  karty=[
      ("⚠️ UBÝVÁ VODY", [
          "Hydrofilní lék se má kam méně rozředit",
          "→ KONCENTRACE hned stoupne",
          "Digoxin, aspirin, lithium, aminoglykosidy",
          "⚠️ Problém už po první dávce"], "cervena"),
      ("⚠️ PŘIBÝVÁ TUKU", [
          "Lipofilní lék má kam se schovat",
          "→ větší Vd → DELŠÍ POLOČAS",
          "Benzodiazepiny, amiodaron",
          "⚠️ Problém až za týden — kumulace"], "cervena"),
      ("ELIMINACE A DYNAMIKA", [
          "Játra — menší objem a průtok, nižší first-pass",
          "Ledviny — klesá filtrace; ⚠️ NORMÁLNÍ KREATININ NEZNAMENÁ NORMÁLNÍ LEDVINY",
          "(senior ho méně vyrábí i vylučuje — změny se vyruší)",
          "⚠️ Vyšší citlivost CNS, chybí adaptační rezerva"], "zelena"),
      ("JAK PŘEDEPISOVAT", [
          "„Start low, go slow\" — začni nízko, stoupej pomalu",
          "⚠️ Beersova kritéria — léky nevhodné u seniorů",
          "⚠️ STOPP (co vysadit) / START (co chybí)",
          "⚠️ Rizikové: benzodiazepiny (pády), anticholinergika (kognice), NSA"], "modra"),
  ],
  mnemo="Hydrofilní se KONCENTRUJÍ hned. Lipofilní se HROMADÍ pomalu.",
  zubar="⚠️ Senior má často xerostomii z medikace → kořenový kaz, potíže s protézou, "
        "kandidóza. Zkontroluj seznam léků — anticholinergika, antidepresiva, diuretika.",
  past="Podléčení je u seniorů stejně častá chyba jako předávkování — proto existuje "
       "kritérium START, ne jen STOPP.")

S("O35", "Biologická léčba: rozdělení, názvosloví, biosimilars, přínosy a rizika",
  jadro="Biologikum je bílkovina vyrobená živým organismem — a všechny jeho vlastnosti "
        "plynou právě z toho.",
  tok=[("-O- MYŠÍ", "cervena"), ("-XI- CHIMÉRICKÁ", "bila"),
       ("-ZU- HUMANIZOVANÁ", "bila"), ("-U- PLNĚ HUMÁNNÍ", "zelena")],
  tok_popisky=["", "", "čím lidštější, tím méně imunogenní"],
  karty=[
      ("CO Z TOHO, ŽE JE TO BÍLKOVINA", [
          "⚠️ Ve střevě by se strávila → jen PARENTERÁLNĚ",
          "⚠️ Imunitní systém ji vidí → IMUNOGENITA, protilátky, ztráta účinku",
          "⚠️ Vyrábí ji živá buňka → nedá se udělat identická kopie → BIOSIMILAR",
          "Náročné skladování (chladový řetězec)"], "zelena"),
      ("SKUPINY A KONCOVKY", [
          "-mab — monoklonální protilátka (adalimumab, rituximab)",
          "-cept — fúzní receptor (etanercept, abatacept)",
          "-kin — interleukiny · -stim — růstové faktory (filgrastim) · -poetin",
          "Rekombinantní hormony a enzymy (inzulin, somatropin)",
          "⚠️ -tinib NENÍ biologikum — je to malá molekula (cílená ≠ biologická léčba)"], "modra"),
      ("BIOSIMILARS", [
          "⚠️ Není to generikum — molekula nemůže být identická",
          "Liší se glykosylací; ⚠️ i dvě šarže originálu se od sebe liší",
          "Musí se vejít do pásma, ve kterém kolísá originál",
          "Vyžaduje srovnávací studie, ne jen bioekvivalenci"], "bila"),
      ("PŘÍNOSY A RIZIKA", [
          "+ Vysoká cílenost a účinnost tam, kde klasická léčba selhala",
          "⚠️ − INFEKCE — screening TBC a hepatitid před anti-TNF",
          "⚠️ − Žádné živé vakcíny během léčby",
          "⚠️ − Reakce na infuzi, imunogenita, nádory, vysoká cena"], "cervena"),
  ],
  mnemo="Koncovka říká původ: o–xi–zu–u, od myši k člověku.",
  zubar="⚠️ Pacient na anti-TNF nebo jiné biologické léčbě je imunosuprimovaný: "
        "vyšší riziko infekcí, horší hojení, nutná konzultace před rozsáhlým výkonem.",
  past="TNF-α drží pohromadě granulom — jeho zablokování rozpustí granulom a "
       "latentní tuberkulóza propukne. Proto povinný screening.")
