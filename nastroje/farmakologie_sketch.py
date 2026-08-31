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


# ═════════════════════════════════════ SPECKA I

S("36", "Cholinergní přenos vzruchu",
  jadro="Acetylcholin se ve štěrbině ROZŠTĚPÍ ENZYMEM — noradrenalin se vychytá zpět. "
        "Z toho plyne, proč na každý z nich fungují jiné léky.",
  tok=[("cholin + acetyl-CoA", "bila"), ("ACETYLCHOLIN ve vezikule", "zelena"),
       ("EXOCYTÓZA do štěrbiny", "bila"), ("⚠️ ROZŠTĚPÍ HO ACETYLCHOLINESTERÁZA", "cervena")],
  tok_popisky=["cholinacetyltransferáza", "⚠️ botulotoxin blokuje", "receptory M a N"],
  karty=[
      ("CESTA MOLEKULY A KDE ZASAHUJÍ LÉKY", [
          "Syntéza z cholinu a acetyl-CoA (cholinacetyltransferáza)",
          "Uložení do vezikul (⚠️ vezamikol blokuje plnění)",
          "Uvolnění exocytózou po vstupu Ca²⁺ (⚠️ botulotoxin štěpí SNARE)",
          "Zánik acetylcholinesterázou (⚠️ nepřímá cholinomimetika ji blokují)",
          "Zpětné vychytání cholinu (⚠️ hemicholinium blokuje)"], "zelena"),
      ("MUSKARINOVÉ RECEPTORY", [
          "Metabotropní, přes G-protein → účinek v sekundách",
          "M1 — CNS, ganglia, parietální buňky žaludku",
          "⚠️ M2 — SRDCE, jediný tlumivý (přes Gi) → bradykardie",
          "⚠️ M3 — hladká svalovina a ŽLÁZY → sekrece, mióza, bronchokonstrikce",
          "M4, M5 — CNS"], "modra"),
      ("NIKOTINOVÉ RECEPTORY", [
          "⚠️ Ionotropní — samy jsou iontový kanál → účinek v milisekundách",
          "Nm — nervosvalová ploténka (myorelaxancia)",
          "Nn — vegetativní ganglia a dřeň nadledvin",
          "⚠️ Atropin je NEblokuje — proto nezruší svalovou obrnu"], "bila"),
      ("KDE SE ACETYLCHOLIN UPLATŇUJE", [
          "Všechna pregangliová vlákna (sympatiku i parasympatiku)",
          "Postgangliová parasympatická vlákna",
          "⚠️ Výjimka: postgangliová sympatická vlákna k POTNÍM žlázám",
          "Nervosvalová ploténka a CNS"], "zluta"),
  ],
  mnemo="M2 srdce · M3 žlázy a hladký sval · Nm ploténka · Nn ganglia.",
  zubar="Sliny řídí M3 — proto pilokarpin (cholinomimetikum) léčí xerostomii a "
        "anticholinergika ji naopak způsobují.",
  past="Potní žlázy jsou sympatické, ale cholinergní — proto betablokátor "
       "maskuje třes a bušení srdce při hypoglykemii, ale POCENÍ zůstane.")

S("37", "Přímá cholinomimetika",
  jadro="Sednou si přímo na muskarinový receptor místo acetylcholinu — a zapnou "
        "celý parasympatikus najednou.",
  karty=[
      ("ESTERY CHOLINU", [
          "Acetylcholin — ⚠️ v praxi nepoužitelný, esteráza ho zničí za vteřiny",
          "Karbachol — odolný vůči esteráze, i nikotinový účinek",
          "Betanechol — ⚠️ selektivní na M3, skoro nepůsobí na srdce",
          "Methacholin — diagnostika bronchiální hyperreaktivity"], "zelena"),
      ("PŘÍRODNÍ ALKALOIDY", [
          "⚠️ PILOKARPIN — glaukom, ⚠️ XEROSTOMIE u Sjögrena a po ozáření",
          "Muskarin — z hub (vláknice, strmělky), toxikologicky",
          "Arekolin — betelový ořech",
          "Cevimelin (kde je registrován) — také na suchost úst"], "zelena"),
      ("ÚČINKY — celý parasympatikus", [
          "Oko: mióza, akomodace na blízko, ⚠️ pokles nitroočního tlaku",
          "Žlázy: slinění, slzení, pocení, bronchiální sekrece",
          "Srdce: bradykardie, zpomalení AV vedení",
          "⚠️ Průdušky: bronchokonstrikce · GIT: peristaltika a sekrece",
          "Měchýř: vyprázdnění"], "modra"),
      ("⚠️ NEŽÁDOUCÍ ÚČINKY A KONTRAINDIKACE", [
          "🔑 SLUDGE: Salivace, Lakrimace, Urinace, Defekace, GIT křeče, Emeze",
          "⚠️ KI: ASTMA a CHOPN (bronchospazmus)",
          "⚠️ KI: vředová choroba (sekrece kyseliny)",
          "⚠️ KI: bradykardie, AV blok, obstrukce střeva a močových cest"], "cervena"),
  ],
  mnemo="SLUDGE — všechno teče. Plus mióza a stažené průdušky.",
  zubar="⚠️ PILOKARPIN je zubařsky nejdůležitější: rozjede slinné žlázy přes M3 "
        "u Sjögrenova syndromu a po radioterapii hlavy a krku. Zmírní tím riziko "
        "kořenového kazu a kandidózy.",
  past="Acetylcholin sám se jako lék nepodává — cholinesteráza ho zničí dřív, "
       "než by mohl působit.")

S("38", "Nepřímá cholinomimetika",
  jadro="Nesedají na receptor vůbec — blokují acetylcholinesterázu, takže acetylcholin "
        "ve štěrbině zůstane déle.",
  tok=[("REVERZIBILNÍ krátké: edrofonium", "bila"),
       ("střední: NEOSTIGMIN, FYZOSTIGMIN", "zelena"),
       ("centrální: donepezil, rivastigmin", "modra"),
       ("⚠️ IREVERZIBILNÍ organofosfáty", "cervena")],
  karty=[
      ("⚠️ KVARTÉRNÍ × TERCIÁRNÍ", [
          "⚠️ NEOSTIGMIN, pyridostigmin — kvartérní, nabité → do mozku NEprojdou",
          "⚠️ FYZOSTIGMIN — terciární → do mozku projde",
          "🔑 FYZostigmin projde, NEOstigmin ne",
          "→ fyzostigmin je antidotum centrálního anticholinergního syndromu"], "zelena"),
      ("INDIKACE", [
          "Myasthenia gravis — pyridostigmin; ⚠️ edrofonium k diagnostice",
          "⚠️ Dekurarizace po nedepolarizujících myorelaxanciích",
          "Atonie střeva a měchýře",
          "Glaukom · Alzheimerova nemoc (donepezil, rivastigmin, galantamin)"], "modra"),
      ("⚠️ OTRAVA ORGANOFOSFÁTY", [
          "Insekticidy, bojové látky (sarin), karbamáty",
          "Obraz: ⚠️ SLUDGE + mióza „jako špendlíková hlavička\" + bronchorea",
          "+ fascikulace, slabost, křeče; ⚠️ smrt zahlcením dýchacích cest",
          "⚠️ Léčba: ATROPIN (na M) + PRALIDOXIM (reaktivátor enzymu)",
          "⚠️ Pralidoxim musí přijít dřív, než enzym „zestárne\" (aging)"], "cervena"),
      ("NEŽÁDOUCÍ ÚČINKY", [
          "Bradykardie, hypersalivace, průjem, křeče v břiše",
          "⚠️ Cholinergní krize — vypadá jako zhoršení myasthenie, ale je z předávkování",
          "⚠️ Neostigmin se podává s ATROPINEM — ten odstřihne účinky na srdce",
          "a ploténku (Nm) nechá být"], "bila"),
  ],
  mnemo="Blokuješ enzym → acetylcholinu je všude víc. Atropin pak vypne jen ten nežádoucí.",
  zubar="Pacient s Alzheimerovou nemocí na donepezilu má ⚠️ hypersalivaci — a hlavně "
        "postupně přestává zvládat ústní hygienu. Ošetření plánuj co nejdřív.",
  past="Atropin nezruší svalovou slabost při otravě organofosfáty — ploténka je "
       "nikotinová, atropin blokuje jen muskarinové receptory.")

S("39", "Parasympatolytika",
  jadro="Kompetitivní antagonisté na muskarinových receptorech — acetylcholin se "
        "vyrobí i uvolní, ale nemá si kam sednout.",
  karty=[
      ("ZÁSTUPCI", [
          "ATROPIN (rulík zlomocný), skopolamin, homatropin",
          "⚠️ Kvartérní — zůstanou tam, kam je dáš: ipratropium, tiotropium (inhalačně),",
          "butylskopolamin (spazmolytikum)",
          "Uroselektivní: oxybutynin, tolterodin, solifenacin",
          "Oční: tropikamid, cyklopentolát · Pirenzepin (M1, obsoletní)"], "zelena"),
      ("ÚČINKY = obrácený parasympatikus", [
          "Oko: mydriáza, cykloplegie, ⚠️ vzestup nitroočního tlaku",
          "⚠️ Žlázy: SUCHO V ÚSTECH, méně potu, sekretů",
          "Srdce: tachykardie · Průdušky: rozšíření",
          "GIT: útlum peristaltiky, zácpa · Měchýř: retence moči"], "modra"),
      ("INDIKACE", [
          "Bradykardie a premedikace (atropin)",
          "⚠️ CHOPN a astma (ipratropium, tiotropium)",
          "Spazmy GIT a močových cest, hyperaktivní měchýř",
          "Kinetóza (skopolamin), oftalmologie",
          "⚠️ Antidotum otravy organofosfáty"], "bila"),
      ("⚠️ OTRAVA — pět přirovnání", [
          "„Slepý jako netopýr\" — mydriáza a cykloplegie",
          "„Suchý jako kost\" · „Červený jako řepa\"",
          "„Horký jako pec\" — nepotí se, nemá jak snížit teplotu",
          "„Šílený jako kloboučník\" — delirium",
          "⚠️ Antidotum FYZOSTIGMIN. KI: glaukom s úzkým úhlem, hyperplazie prostaty"], "cervena"),
  ],
  mnemo="Slepý, suchý, červený, horký, šílený.",
  zubar="⚠️ XEROSTOMIE → mnohočetný kaz, kandidóza, nesnášenlivost protézy. A netýká se "
        "jen atropinu: stejně suší ⚠️ tricyklická antidepresiva, antipsychotika, "
        "antihistaminika I. generace a léky na hyperaktivní měchýř — a ty pacient bere roky.",
  past="Ipratropium inhalačně nedělá sucho v ústech ani tachykardii, protože je "
       "kvartérní — nevstřebá se a nedostane se do mozku.")

S("40", "Adrenergní přenos vzruchu",
  jadro="Noradrenalin se ve štěrbině NErozkládá — on se VYCHYTÁ ZPĚT. "
        "Proto na něj fungují úplně jiné léky než na acetylcholin.",
  tok=[("TYROSIN", "bila"), ("DOPA ⚠️ krok určující rychlost", "cervena"),
       ("DOPAMIN", "bila"), ("NORADRENALIN ⚠️ v nadledvině → ADRENALIN", "zelena")],
  tok_popisky=["tyrosinhydroxyláza", "dekarboxyláza", "dopamin-β-hydroxyláza"],
  karty=[
      ("SYNTÉZA A ZÁNIK", [
          "Tyrosin → DOPA (⚠️ tyrosinhydroxyláza = limitující krok) → dopamin",
          "V vezikule → noradrenalin; ⚠️ jen v dřeni nadledvin PNMT → ADRENALIN",
          "⚠️ Zánik hlavně REUPTAKE (uptake-1) — kokain a tricyklika blokují",
          "Teprve pak MAO (uvnitř neuronu) a COMT (extraneuronálně)"], "zelena"),
      ("RECEPTORY — co dělají", [
          "α1 — stah cév, mydriáza, sfinktery, prostata (Gq)",
          "⚠️ α2 — PRESYNAPTICKÁ BRZDA výdeje; centrálně snižuje tlak (Gi)",
          "β1 — srdce: frekvence a síla, výdej reninu",
          "⚠️ β2 — bronchodilatace, dilatace cév ve svalu, děloha, tremor, hypokalemie",
          "β3 — lipolýza, relaxace měchýře"], "modra"),
      ("KDE LÉKY ZASAHUJÍ", [
          "Syntéza: methyldopa (falešný přenašeč), α-methyltyrosin",
          "Skladování a výdej: rezerpin, nepřímá sympatomimetika",
          "⚠️ Reuptake: kokain, tricyklika, SNRI",
          "Odbourání: inhibitory MAO a COMT",
          "Receptor: sympatomimetika a sympatolytika"], "bila"),
      ("ROZDÍL PROTI ACETYLCHOLINU", [
          "ACh — rozštěpí ho enzym přímo ve štěrbině",
          "NA — vychytá se zpět do neuronu a znovu použije",
          "⚠️ Proto u ACh fungují inhibitory esterázy",
          "a u NA blokátory zpětného vychytávání"], "zluta"),
  ],
  mnemo="Jedno srdce = β1. Dvě plíce = β2.",
  zubar="⚠️ Adrenalin v lokálním anestetiku působí přes α1 (vazokonstrikce) — proto "
        "prodlouží účinek a sníží krvácení. U pacienta na tricyklikách nebo po kokainu "
        "se jeho účinek zesílí, protože je blokovaný reuptake.",
  past="α2-agonista snižuje tlak, i když α znamená stah cév — protože působí "
       "CENTRÁLNĚ a PŘEDSYNAPTICKY, tedy na brzdu.")

S("41", "Neselektivní sympatomimetika",
  jadro="Adrenalin je jediný lék, který v anafylaxi zabírá na všechny složky reakce "
        "zároveň — a proto ho nic nenahradí.",
  karty=[
      ("ZÁSTUPCI", [
          "ADRENALIN — α i β; anafylaxe, resuscitace, přísada k anestetiku",
          "NORADRENALIN — α1 a β1, ⚠️ skoro žádné β2; vazopresor v šoku",
          "ISOPRENALIN — β1 + β2, dnes okrajově",
          "DOPAMIN — ⚠️ dávkově závislé chování"], "zelena"),
      ("⚠️ DOPAMIN — tři chování podle dávky", [
          "Nízká dávka → D1: rozšíření ledvinných cév",
          "Střední → β1: silnější a rychlejší stah srdce",
          "Vysoká → α1: stah cév, vzestup tlaku",
          "⚠️ Jeden lék, tři různé klinické efekty"], "modra"),
      ("⚠️ PROČ ADRENALIN U ANAFYLAXE", [
          "α1 — stáhne cévy a zvedne tlak",
          "β1 — podpoří srdce",
          "β2 — rozšíří průdušky",
          "β2 — zastaví vyplavování mediátorů ze žírných buněk",
          "⚠️ Dávka 0,5 mg i.m. do stehna (roztok 1 : 1000)"], "cervena"),
      ("NEŽÁDOUCÍ ÚČINKY A PASTI", [
          "Tachykardie, arytmie, hypertenze, tremor, úzkost",
          "⚠️ Noradrenalin → reflexní bradykardie (baroreflex, chybí β2)",
          "⚠️ Adrenalinová reverze: po α-blokádě zvedne adrenalin místo tlaku POKLES",
          "⚠️ Extravazace noradrenalinu → nekróza; antidotum fentolamin lokálně"], "bila"),
  ],
  mnemo="Anafylaxe: adrenalin řeší tlak, srdce, průdušky i mediátory najednou.",
  zubar="⚠️ Adrenalin v anestetiku: prodlouží účinek, sníží toxicitu a krvácení v poli. "
        "⚠️ Nepodávat do akrálních částí (prst, ucho, nos) — ischemie. U kompenzovaného "
        "kardiaka je běžné množství bezpečné, u nekontrolované hypertenze a hypertyreózy opatrně.",
  past="Antihistaminikum ani kortikoid anafylaxi nezvládnou — nepůsobí na tlak "
       "a nastupují příliš pozdě.")

S("42", "Sympatomimetika alfa",
  jadro="α1 zvyšuje tlak, centrálně působící α2 ho snižuje. Ten paradox je jádro otázky.",
  karty=[
      ("α1 AGONISTÉ — periferní", [
          "Fenylefrin — dekongesce, ⚠️ mydriáza BEZ cykloplegie, hypotenze",
          "Midodrin — ortostatická hypotenze",
          "Nafazolin, xylometazolin, oxymetazolin — nosní kapky",
          "⚠️ Účinek: stah cév → vzestup tlaku, reflexní bradykardie"], "zelena"),
      ("⚠️ α2 AGONISTÉ — centrální", [
          "Klonidin, methyldopa, guanfacin",
          "Brimonidin (glaukom) · tizanidin (spasticita) · dexmedetomidin (sedace)",
          "⚠️ Sednou na PRESYNAPTICKOU BRZDU v CNS → utlumí výdej sympatiku",
          "→ ⚠️ SNIŽUJÍ tlak, i když jsou to „alfa\" agonisté"], "modra"),
      ("INDIKACE", [
          "Hypotenze a šok (fenylefrin, midodrin)",
          "Rýma a otok nosní sliznice",
          "⚠️ METHYLDOPA — antihypertenzivum volby v graviditě",
          "Glaukom, spasticita, sedace na JIP, odvykací stavy"], "bila"),
      ("⚠️ NEŽÁDOUCÍ ÚČINKY", [
          "⚠️ RHINITIS MEDICAMENTOSA — nosní kapky max 5–7 dní",
          "(po odeznění sliznice oteče ještě víc → začarovaný kruh)",
          "Klonidin: ⚠️ sucho v ústech, sedace, ⚠️ REBOUND hypertenze po vysazení",
          "Methyldopa: útlum, hemolytická anemie, pozitivní Coombsův test"], "cervena"),
  ],
  mnemo="α1 na periferii tlačí tlak nahoru. α2 v mozku ho tlačí dolů.",
  zubar="Xylometazolin a fenylefrin patří mezi léky, které pacient v anamnéze neuvede. "
        "⚠️ Klonidin dělá výraznou xerostomii.",
  past="Fenylefrin rozšíří zornici, ale nezruší akomodaci — na cykloplegii je potřeba "
       "anticholinergikum (tropikamid, atropin).")

S("43", "Sympatomimetika beta",
  jadro="Tři nežádoucí účinky β2-mimetik — tremor, tachykardie a hypokalemie — "
        "plynou z jednoho jediného receptoru.",
  karty=[
      ("β2 — základ léčby astmatu", [
          "SABA (krátkodobá, úlevová): salbutamol, fenoterol, terbutalin",
          "LABA (dlouhodobá): formoterol, salmeterol, indakaterol",
          "⚠️ LABA NIKDY samostatně u astmatu — zvyšuje úmrtnost; vždy s kortikoidem",
          "⚠️ Formoterol nastupuje rychle → smí i úlevově (režim MART), salmeterol ne"], "zelena"),
      ("β1 a β3", [
          "β1: DOBUTAMIN — inotropikum u akutního srdečního selhání a šoku",
          "β3: MIRABEGRON — hyperaktivní měchýř (relaxace detruzoru)",
          "⚠️ Alternativa k anticholinergikům, nedělá xerostomii"], "modra"),
      ("DALŠÍ INDIKACE β2", [
          "⚠️ Tokolýza — hexoprenalin, oddálení předčasného porodu",
          "⚠️ Akutní hyperkalemie — salbutamol v nebulizaci naveze draslík do buněk",
          "CHOPN (s LAMA)"], "bila"),
      ("⚠️ TŘI NEŽÁDOUCÍ ÚČINKY", [
          "⚠️ TREMOR — β2 na kosterním svalu",
          "⚠️ TACHYKARDIE — přelití účinku na β1",
          "⚠️ HYPOKALEMIE — β2 žene draslík do buněk",
          "Dále: neklid, bolest hlavy, ⚠️ tolerance při nadužívání"], "cervena"),
  ],
  mnemo="Tremor + tachykardie + hypokalemie = podpis každého β2-mimetika.",
  zubar="⚠️ Astmatik má mít inhalátor v ordinaci u sebe. Salbutamol před výkonem "
        "zesílí bušení srdce po anestetiku s adrenalinem — pacienta na to upozorni.",
  past="Rostoucí spotřeba úlevového inhalátoru je varovný signál špatně kontrolovaného "
       "astmatu — řešením je kortikoid, ne víc salbutamolu.")

S("44", "Nepřímá sympatomimetika",
  jadro="Na receptor samy nesedají — buď vytlačí noradrenalin z vezikul, nebo zablokují "
        "jeho vychytávání. Proto potřebují mít z čeho brát.",
  tok=[("efedrin, amfetamin, ⚠️ TYRAMIN", "bila"),
       ("vytlačí NORADRENALIN z vezikul", "zelena"),
       ("silná sympatická odpověď", "bila"),
       ("⚠️ vezikuly prázdné → TACHYFYLAXE", "cervena")],
  karty=[
      ("VYPLAVUJÍCÍ", [
          "Efedrin, pseudoefedrin (smíšený mechanismus)",
          "Amfetamin, metamfetamin (pervitin)",
          "⚠️ Tyramin — v uzrálých sýrech, víně, uzeninách",
          "⚠️ Tachyfylaxe — po opakovaných dávkách účinek rychle slábne"], "zelena"),
      ("BLOKUJÍCÍ REUPTAKE", [
          "⚠️ KOKAIN — noradrenalin zůstane ve štěrbině",
          "→ vazokonstrikce, hypertenze, ⚠️ infarkt a CMP u mladých",
          "⚠️ Nekróza nosní přepážky při šňupání",
          "Tricyklická antidepresiva, SNRI, modafinil"], "cervena"),
      ("⚠️ SÝROVÝ EFEKT", [
          "Tyramin ve střevě normálně zničí MAO",
          "⚠️ U pacienta na neselektivním IMAO projde do oběhu",
          "→ vytlačí noradrenalin → HYPERTENZNÍ KRIZE",
          "⚠️ Moklobemid (reverzibilní RIMA) tenhle problém nemá"], "cervena"),
      ("POUŽITÍ A RIZIKA", [
          "Efedrin — hypotenze v anestezii; pseudoefedrin — dekongesce",
          "⚠️ Pseudoefedrin je prekurzor pervitinu → výdej je omezený",
          "Metylfenidát u ADHD, modafinil u narkolepsie",
          "⚠️ Zneužívání: euforie, nespavost, psychóza, hypertermie"], "bila"),
  ],
  mnemo="Vyplavují ze skladu — a sklad dojde. To je tachyfylaxe.",
  zubar="⚠️ Pacientovi pod vlivem pervitinu nebo kokainu se NEDÁVÁ anestetikum "
        "s adrenalinem — účinky se sečtou (hypertenzní krize, arytmie). Výkon odlož.",
  past="Tachyfylaxe je znak nepřímých sympatomimetik. Přímá sympatomimetika ji nedělají, "
       "protože nepotřebují zásoby noradrenalinu.")

S("45", "Sympatolytika alfa",
  jadro="U feochromocytomu se vždy blokuje nejdřív alfa a teprve potom beta — "
        "obrácené pořadí vyvolá hypertenzní krizi.",
  tok=[("FEOCHROMOCYTOM", "bila"), ("⚠️ NEJDŘÍV α-BLOKÁDA", "zelena"),
       ("teprve POTOM betablokátor", "zelena"), ("bezpečná operace", "modra")],
  karty=[
      ("NESELEKTIVNÍ α-BLOKÁTORY", [
          "Fentolamin — reverzibilní, krátce působící",
          "Fenoxybenzamin — ⚠️ ireverzibilní, dlouhý účinek",
          "⚠️ Příprava k operaci feochromocytomu",
          "⚠️ Fentolamin lokálně při extravazaci noradrenalinu"], "zelena"),
      ("α1-SELEKTIVNÍ", [
          "Prazosin, doxazosin, terazosin — hypertenze, hlavně s hyperplazií prostaty",
          "⚠️ Uroselektivní α1A: TAMSULOSIN, silodosin",
          "→ nesnižují tlak, míří na prostatu a hrdlo měchýře",
          "Yohimbin — α2 antagonista, okrajově"], "modra"),
      ("⚠️ NEŽÁDOUCÍ ÚČINKY", [
          "⚠️ FIRST-DOSE EFEKT — první dávka může způsobit kolaps",
          "(malá dávka na noc vleže)",
          "Ortostatická hypotenze, závratě, reflexní tachykardie",
          "Retrográdní ejakulace, ucpaný nos",
          "⚠️ FLOPPY IRIS SYNDROME při operaci šedého zákalu (tamsulosin)"], "cervena"),
      ("PROČ POŘADÍ", [
          "Betablokátor podaný první zablokuje β2 vazodilataci",
          "⚠️ Zůstane čistý α1 stah → prudký vzestup tlaku",
          "Proto: α-blokáda → objemová náhrada → teprve pak betablokátor"], "zluta"),
  ],
  mnemo="Nejdřív alfa, potom beta. Obráceně je to hypertenzní krize.",
  zubar="⚠️ Pacient na α-blokátoru má sklon k ortostatické hypotenzi — po delším "
        "ošetření vleže ho nechej chvíli sedět, než vstane.",
  past="Tamsulosin je nutné hlásit oftalmologovi před operací katarakty, i když ho "
       "pacient už nebere — duhovka zůstává ochablá.")

S("46", "Sympatolytika beta (betablokátory)",
  jadro="Selektivita je celý rozdíl mezi žádaným účinkem (β1 na srdci) a nežádoucím "
        "(β2 v průduškách a jinde).",
  karty=[
      ("DĚLENÍ", [
          "Neselektivní: propranolol (lipofilní, do CNS), sotalol (+ třída III),",
          "⚠️ timolol (i v očních kapkách!), karvedilol (+ α1)",
          "β1-selektivní: metoprolol, bisoprolol, atenolol, betaxolol, nebivolol (+ NO)",
          "S vnitřní aktivitou (ISA): pindolol"], "zelena"),
      ("INDIKACE", [
          "ICHS, hypertenze, tachyarytmie a fibrilace síní",
          "⚠️ Srdeční selhání — jen bisoprolol, metoprolol ZOK, karvedilol, nebivolol;",
          "⚠️ nasazovat nízko a titrovat týdny",
          "Tyreotoxikóza, esenciální tremor, profylaxe migrény, glaukom, portální hypertenze"], "modra"),
      ("⚠️ NEŽÁDOUCÍ ÚČINKY", [
          "⚠️ Bronchospazmus — KI u astmatu (i z očních kapek)",
          "Bradykardie, AV blokáda, únava, studené končetiny",
          "⚠️ Maskují hypoglykemii (⚠️ pocení zůstane — je cholinergní)",
          "Poruchy spánku a noční můry (lipofilní), erektilní dysfunkce"], "cervena"),
      ("⚠️ VYSAZOVÁNÍ", [
          "Během léčby proběhne UP-REGULACE receptorů",
          "⚠️ Náhlé vysazení → rebound tachykardie, hypertenze, až infarkt",
          "→ vysazovat vždy postupně",
          "⚠️ Nekombinovat s verapamilem nebo diltiazemem (AV blok)"], "cervena"),
  ],
  mnemo="β1 = žádaný účinek. β2 = nežádoucí. Selektivita mizí s dávkou.",
  zubar="⚠️ Pacient na neselektivním betablokátoru: adrenalin v anestetiku může "
        "vyvolat vzestup tlaku s reflexní bradykardií (nezůstane β2 vazodilatace). "
        "Používej nejnižší účinné množství a aspiruj.",
  past="U srdečního selhání se stav na začátku léčby může přechodně zhoršit — "
       "účinek je v ochraně myokardu před chronickým sympatikem, ne v okamžité úlevě.")

S("47", "Myorelaxancia",
  jadro="Periferní působí na ploténce a používají se v anestezii, centrální působí "
        "v míše a používají se na spasticitu.",
  karty=[
      ("DEPOLARIZUJÍCÍ — sukcinylcholin", [
          "Nejdřív fascikulace, pak ochabnutí; velmi rychlý nástup a krátký účinek",
          "⚠️ NEMÁ ANTIDOTUM — neostigmin by blok prohloubil",
          "⚠️ HYPERKALEMIE (u popálenin a poranění míchy smrtelná)",
          "⚠️ MALIGNÍ HYPERTERMIE (zvl. s halogenovanými) → DANTROLEN",
          "⚠️ Atypická pseudocholinesteráza → apnoe na hodiny"], "cervena"),
      ("NEDEPOLARIZUJÍCÍ — kompetitivní", [
          "Rokuronium, vekuronium, pankuronium, atrakurium, cisatrakurium",
          "⚠️ Antidotum NEOSTIGMIN + atropin",
          "⚠️ U rokuronia SUGAMMADEX — molekulární klec, která ho obalí",
          "⚠️ Atrakurium: HOFMANNOVA ELIMINACE — rozpadá se samo při tělesné teplotě",
          "→ lék volby při selhání jater a ledvin"], "zelena"),
      ("CENTRÁLNÍ MYORELAXANCIA", [
          "Baklofen — agonista GABA-B, spasticita u roztroušené sklerózy",
          "Tizanidin — α2 agonista v míše",
          "Tolperison, guaifenesin, benzodiazepiny (diazepam)",
          "⚠️ Nežádoucí: sedace, slabost, závratě"], "modra"),
      ("DANTROLEN — zvláštní případ", [
          "Působí PŘÍMO na sval, ne na nerv",
          "⚠️ Blokuje ryanodinový receptor → brání výdeji Ca²⁺ ze sarkoplazmatického retikula",
          "⚠️ Antidotum maligní hypertermie a maligního neuroleptického syndromu",
          "Také u těžké spasticity"], "bila"),
  ],
  mnemo="Depolarizující nemá antidotum. Nedepolarizující ano — neostigmin nebo sugammadex.",
  zubar="Myorelaxancia potkáš u celkové anestezie. ⚠️ Rodinná anamnéza „po narkóze "
        "problémy\" může znamenat maligní hypertermii nebo atypickou cholinesterázu — "
        "ptej se na ni před výkonem v celkové anestezii.",
  past="U depolarizujícího bloku je problém nadbytek, ne nedostatek acetylcholinu — "
       "proto neostigmin nepomůže, ale uškodí.")

S("48", "Lokální anestetika",
  jadro="Musí projít membránou v nenabité formě, aby mohla zavřít sodíkový kanál "
        "zevnitř. V zaníceném zubu se tam nedostanou.",
  tok=[("slabá ZÁSADA nenabitá forma", "zelena"), ("projde membránou", "bila"),
       ("uvnitř se nabije", "bila"), ("zavře Na⁺ kanál ZEVNITŘ", "zelena")],
  karty=[
      ("ESTERY × AMIDY", [
          "ESTERY: prokain, tetrakain, benzokain — štěpí plazmatická cholinesteráza",
          "⚠️ metabolit PABA → alergie",
          "AMIDY: lidokain, mepivakain, ⚠️ ARTIKAIN, bupivakain, prilokain, trimekain",
          "→ metabolizují se v játrech, alergie výjimečná",
          "🔑 Amid má v názvu dvě „i\" — lIdokaIn"], "zelena"),
      ("⚠️ IONTOVÁ PAST V ZANÍCENÉM ZUBU", [
          "Zánět = kyselé pH → anestetikum je nabité UŽ VENKU",
          "⚠️ Nabitá forma neprojde membránou → anestezie nezabere",
          "Řešení: svodná anestezie mimo zánět, větší objem, intraligamentární technika",
          "⚠️ Ne bezhlavě vyšší dávka — roste jen toxicita"], "cervena"),
      ("VAZOKONSTRIKTOR", [
          "Adrenalin (obvykle 1 : 100 000 nebo 1 : 200 000)",
          "⚠️ Prodlouží účinek, sníží systémovou toxicitu, sníží krvácení v poli",
          "⚠️ NE do akrálních částí (prst, ucho, nos)",
          "Opatrně: nekontrolovaná hypertenze, hypertyreóza, kokain, tricyklika"], "modra"),
      ("⚠️ SYSTÉMOVÁ TOXICITA", [
          "Nejdřív CNS: brnění kolem úst, kovová chuť, tinnitus, neklid → křeče → útlum",
          "Pak kardiovaskulární kolaps",
          "⚠️ BUPIVAKAIN je nejvíc kardiotoxický — srdce může selhat před varováním z CNS",
          "⚠️ PRILOKAIN → methemoglobinemie",
          "⚠️ Antidotum: LIPIDOVÁ EMULZE i.v. + zajištění dýchání + benzodiazepin na křeče"], "cervena"),
  ],
  mnemo="Nenabité dovnitř, tam se nabije a zavře kanál. Kyselé pH to celé zastaví.",
  zubar="⚠️ ARTIKAIN je v zubním lékařství nejpoužívanější: je to amid, ale nese "
        "navíc esterovou skupinu → plazmatické esterázy ho rychle rozštěpí → krátký "
        "poločas a nízká systémová toxicita. ⚠️ Vždy aspiruj, ať nepodáš do cévy.",
  past="Alergie na lokální anestetikum je vzácná a týká se hlavně esterů. Většina "
       "„alergických reakcí\" je ve skutečnosti reakce na adrenalin nebo vazovagální synkopa.")

S("49", "Celková anestetika — inhalační",
  jadro="MAC říká, jak je anestetikum silné. Rozpustnost v krvi říká, jak rychle "
        "nastupuje. A ty dvě veličiny spolu nesouvisí.",
  karty=[
      ("DVĚ NEZÁVISLÉ VELIČINY", [
          "MAC — koncentrace, při které 50 % pacientů nereaguje na kožní řez",
          "⚠️ NÍZKÁ MAC = SILNÉ anestetikum",
          "Rozpustnost v krvi (koeficient krev/plyn)",
          "⚠️ NÍZKÁ rozpustnost = RYCHLÝ nástup i probuzení"], "zelena"),
      ("ZÁSTUPCI", [
          "⚠️ HALOTAN — obsoletní: hepatotoxicita, senzibilizace srdce ke katecholaminům",
          "Isofluran — levný, dráždivý",
          "⚠️ SEVOFLURAN — dnes standard, sladký a nedráždivý → úvod maskou u dětí",
          "Desfluran — nejrychlejší, ale dráždí dýchací cesty"], "modra"),
      ("⚠️ OXID DUSNÝ (rajský plyn)", [
          "⚠️ MAC přes 100 % → sám nikdy neuspí",
          "⚠️ Výborný ANALGETICKÝ účinek",
          "⚠️ V zubním lékařství sedace a analgezie u úzkostných pacientů a dětí",
          "⚠️ Rizika: difuzní hypoxie při ukončení (podat 100% kyslík),",
          "inaktivace vitaminu B12, expanze uzavřených dutin"], "zelena"),
      ("⚠️ MALIGNÍ HYPERTERMIE", [
          "Geneticky podmíněná porucha ryanodinového receptoru",
          "Spouštěče: halogenovaná anestetika a sukcinylcholin",
          "Obraz: rigidita, prudký vzestup teploty, acidóza, rabdomyolýza",
          "⚠️ Léčba: DANTROLEN, chlazení, ukončení expozice"], "cervena"),
  ],
  mnemo="Nízká MAC = silné. Nízká rozpustnost v krvi = rychlé.",
  zubar="⚠️ Oxid dusný je v zubní ordinaci nejběžnější inhalační sedace — u dětí a "
        "fobických pacientů. Vyžaduje odsávání a ventilaci (chronická expozice personálu).",
  past="Oxid dusný sám o sobě není anestetikum — je to analgetikum a sedativum. "
       "Jeho MAC nad 100 % znamená, že by k uspání bylo potřeba víc než 100 % plynu.")

S("50", "Celková anestetika — intravenózní",
  jadro="Každé má jednu přednost a jednu nevýhodu — a podle nich se vybírá pacient, "
        "ne naopak.",
  karty=[
      ("PROPOFOL a THIOPENTAL", [
          "PROPOFOL — rychlý, čisté probuzení, ⚠️ antiemetický",
          "⚠️ Sráží tlak, nemá analgezii, propofolový infuzní syndrom",
          "THIOPENTAL — ultrarychlý, chrání mozek",
          "⚠️ Krátkost účinku je REDISTRIBUCÍ, ne metabolismem → ⚠️ KUMULUJE"], "zelena"),
      ("KETAMIN", [
          "⚠️ Blokuje NMDA receptor (ostatní jdou přes GABA-A)",
          "⚠️ Jako jediný ZACHOVÁVÁ dýchání a ZVYŠUJE tlak",
          "⚠️ Silná analgezie → šok, terén, popáleniny",
          "⚠️ Halucinace při probuzení (emergence reaction) → podat s benzodiazepinem",
          "⚠️ Hypersalivace"], "modra"),
      ("ETOMIDÁT a MIDAZOLAM", [
          "ETOMIDÁT — ⚠️ kardiálně nejstabilnější, vhodný u nestabilního pacienta",
          "⚠️ Tlumí kůru nadledvin, myoklonie",
          "MIDAZOLAM — anxiolýza, ⚠️ anterográdní amnézie, pomalejší nástup",
          "⚠️ Antidotum flumazenil"], "bila"),
      ("PRAKTICKÉ ZÁSADY", [
          "Úvod do anestezie = nitrožilně, vedení = inhalačně nebo TIVA",
          "⚠️ K bolestivému výkonu je vždy potřeba i analgetikum (opioid)",
          "Doplňková analgezie: fentanyl, sufentanil, remifentanil",
          "⚠️ Sledování dýchání a oběhu je nutné u všech"], "zluta"),
  ],
  mnemo="Propofol sráží tlak, ketamin ho zvedá. Etomidát ho nechá být.",
  zubar="⚠️ Krátká nitrožilní sedace midazolamem je v zubní praxi běžná u fobických "
        "pacientů — vyžaduje monitoraci, kyslík a flumazenil po ruce.",
  past="Thiopental je „krátce působící\" jen po jedné dávce. Po opakovaných se tkáně "
       "nasytí a probuzení trvá hodiny.")

S("51", "Hypnotika",
  jadro="Vývojová řada barbituráty → benzodiazepiny → Z-hypnotika hnala jediná věc: "
        "snaha o širší bezpečnostní okno.",
  karty=[
      ("⚠️ ROZDÍL, KTERÝ ROZHODUJE", [
          "GABA-A receptor je chloridový kanál — chlorid dovnitř = buňka se ztiší",
          "⚠️ BENZODIAZEPIN zvyšuje FREKVENCI otevírání → bez GABA neudělá nic → MÁ STROP",
          "⚠️ BARBITURÁT prodlužuje DOBU otevření a ve vyšší dávce otevře kanál",
          "I BEZ GABA → ⚠️ NEMÁ STROP → proto zabíjí"], "cervena"),
      ("BARBITURÁTY", [
          "Fenobarbital, thiopental",
          "⚠️ Velmi úzké terapeutické okno, ⚠️ nemají antidotum",
          "⚠️ Silná indukce jaterních enzymů",
          "Dnes už ne jako hypnotika; zůstaly u epilepsie a v anestezii"], "cervena"),
      ("Z-HYPNOTIKA", [
          "Zolpidem, zopiklon, zaleplon",
          "⚠️ Váží se hlavně na podjednotku α1 → hypnotický účinek bez myorelaxace",
          "Kratší poločas, menší ranní kocovina",
          "⚠️ PARASOMNIE — noční jedení, chození, řízení s amnézií"], "modra"),
      ("OSTATNÍ A ZÁSADY", [
          "Melatonin a agonisté melatoninu — posun vnitřních hodin, jet lag",
          "Antihistaminika I. generace (promethazin), trazodon, mirtazapin",
          "⚠️ Hypnotikum jen krátkodobě a jako doplněk — základ je spánková hygiena a KBT",
          "⚠️ U seniora benzodiazepin = pády a zlomeniny krčku"], "bila"),
  ],
  mnemo="Benzodiazepin má strop. Barbiturát ne — a proto zabíjí.",
  zubar="Pacient na hypnotikách bývá po ranním ošetření utlumený a hůř spolupracuje; "
        "⚠️ nesmí po výkonu řídit.",
  past="Benzodiazepin sám o sobě zabije jen výjimečně. Smrtelný je v kombinaci "
       "s alkoholem nebo opioidem — ty strop nemají.")

S("52", "Benzodiazepiny",
  jadro="Pozitivní alosterické modulátory GABA-A: samy receptor nespustí, jen zesílí "
        "to, co udělá vlastní GABA. Proto mají strop.",
  karty=[
      ("PĚT ÚČINKŮ NAJEDNOU", [
          "Anxiolýza",
          "Sedace a hypnóza",
          "Antikonvulze — ⚠️ lék volby u status epilepticus",
          "Myorelaxace (centrální)",
          "⚠️ Anterográdní amnézie — proto midazolam před výkonem"], "zelena"),
      ("DĚLENÍ PODLE POLOČASU", [
          "Krátce: midazolam, triazolam — premedikace, výkony",
          "Středně: alprazolam, oxazepam, lorazepam — úzkost, panika",
          "Dlouze: diazepam, klonazepam, chlordiazepoxid — epilepsie, odvykací stav",
          "⚠️ LOT (lorazepam, oxazepam, temazepam) — jen glukuronidace, bez fáze I",
          "→ bezpečné u jaterního postižení a u seniorů"], "modra"),
      ("⚠️ TOLERANCE A ZÁVISLOST", [
          "Tolerance k sedaci vzniká rychle, k anxiolýze pomaleji",
          "⚠️ Fyzická závislost — odvykací stav připomíná alkoholový",
          "⚠️ Rebound úzkost a nespavost po vysazení",
          "→ vysazovat pomalu, po týdnech; předepisovat krátkodobě"], "cervena"),
      ("ANTIDOTUM A KOMBINACE", [
          "⚠️ FLUMAZENIL — kompetitivní antagonista",
          "⚠️ Opatrně: u dlouhodobě závislého nebo u smíšené otravy s TCA vyvolá KŘEČE",
          "⚠️ Smrtelná kombinace: benzodiazepin + alkohol nebo opioid",
          "⚠️ U seniorů: pády, zmatenost, zhoršení kognice"], "cervena"),
  ],
  mnemo="Anxiolýza, sedace, antikonvulze, myorelaxace, amnézie. Pět v jednom.",
  zubar="⚠️ Midazolam je základ sedace v zubní ordinaci — anxiolýza + amnézie znamená, "
        "že si pacient výkon nepamatuje. Nutná monitorace a doprovod domů.",
  past="Flumazenil není rutinní lék — u pacienta závislého na benzodiazepinech "
       "může vyvolat křeče, které se pak těžko tlumí.")

S("53", "Antiepileptika",
  jadro="Je jednodušší naučit se čtyři mechanismy než seznam léků — zástupce si z nich odvodíš.",
  karty=[
      ("ČTYŘI MECHANISMY", [
          "Blokáda Na⁺ kanálů — fenytoin, karbamazepin, lamotrigin, valproát",
          "⚠️ Blokáda T-Ca²⁺ kanálů — ETHOSUXIMID (jen absence)",
          "Zesílení GABA — benzodiazepiny, barbituráty, vigabatrin, tiagabin",
          "Tlumení glutamátu — topiramát, perampanel",
          "Vazba na SV2A — levetiracetam (vlastní kategorie)"], "zelena"),
      ("⚠️ FENYTOIN", [
          "⚠️ HYPERPLAZIE GINGIVY — stejně jako cyklosporin a nifedipin",
          "⚠️ Nelineární (saturační) kinetika — malé zvýšení dávky → skok hladiny",
          "Toxicita: nystagmus, ataxie, zmatenost",
          "Hirsutismus, hrubnutí rysů, ⚠️ silná indukce CYP"], "cervena"),
      ("⚠️ VALPROÁT a KARBAMAZEPIN", [
          "VALPROÁT: ⚠️ NEJSILNĚJŠÍ TERATOGEN — defekty neurální trubice, nižší IQ",
          "⚠️ Hepatotoxicita, hyperamonemie, přírůstek hmotnosti, tremor",
          "KARBAMAZEPIN: ⚠️ autoindukce (po 2 týdnech si srazí hladinu)",
          "⚠️ Hyponatremie, ⚠️ HLA-B*1502 → Stevensův–Johnsonův syndrom",
          "LAMOTRIGIN: ⚠️ rash a SJS při rychlé titraci"], "cervena"),
      ("PRAKTICKÉ ZÁSADY", [
          "⚠️ Status epilepticus: benzodiazepin i.v. → fenytoin nebo levetiracetam → anestezie",
          "⚠️ Nikdy nevysazovat náhle — hrozí status epilepticus",
          "⚠️ Karbamazepin a fenytoin zhoršují absence a myoklonie",
          "U generalizované epilepsie spíš valproát nebo levetiracetam"], "modra"),
  ],
  mnemo="Na kanál · T-Ca kanál · GABA nahoru · glutamát dolů. Čtyři cesty ke ztišení.",
  zubar="⚠️ FENYTOINOVÁ HYPERPLAZIE GINGIVY — objeví se u velké části pacientů a "
        "závisí na ústní hygieně; při dokonalé hygieně se výrazně zmenší. Chirurgické "
        "odstranění má smysl až po zlepšení hygieny, jinak recidivuje.",
  past="Antiepileptika jsou silné induktory CYP — sníží účinnost hormonální "
       "antikoncepce, warfarinu i některých antibiotik.")

S("54", "Antiparkinsonika",
  jadro="Dopamin sám neprojde do mozku, levodopa ano. Celá léčba je o tom, jak dostat "
        "dopamin tam, kde chybí.",
  tok=[("LEVODOPA polknutá", "zelena"),
       ("⚠️ na periferii se hned mění na dopamin", "cervena"),
       ("+ KARBIDOPA / BENSERAZID", "zelena"), ("do mozku dorazí víc", "modra")],
  tok_popisky=["", "nauzea, hypotenze", "⚠️ ty do mozku neprojdou"],
  karty=[
      ("LEVODOPA", [
          "Prekurzor dopaminu, projde bariérou přenašečem pro aminokyseliny",
          "⚠️ Vždy s inhibitorem periferní dekarboxylázy (karbidopa, benserazid)",
          "⚠️ Nezapíjet bílkovinným jídlem — soutěží o stejný přenašeč",
          "⚠️ Po letech: „wearing off\", „on–off\", dyskineze"], "zelena"),
      ("DALŠÍ SKUPINY", [
          "Agonisté D2: pramipexol, ropinirol, rotigotin",
          "⚠️ Poruchy kontroly impulzů — hazard, nakupování, hypersexualita",
          "Inhibitory MAO-B: selegilin, rasagilin",
          "Inhibitory COMT: entakapon, ⚠️ tolkapon (hepatotoxicita)",
          "Amantadin (NMDA) · anticholinergika: biperiden"], "modra"),
      ("ANTICHOLINERGIKA", [
          "Působí hlavně na TŘES",
          "⚠️ U seniorů zhoršují kognici",
          "⚠️ Xerostomie, zácpa, retence moči",
          "Dnes okrajová role"], "bila"),
      ("⚠️ CO PARKINSONIKOVI NEDÁVAT", [
          "⚠️ METOKLOPRAMID — blokuje D2, stav prudce zhorší",
          "⚠️ Klasická antipsychotika (haloperidol)",
          "→ ⚠️ Bezpečná alternativa proti nevolnosti: DOMPERIDON (neprojde do mozku)",
          "⚠️ Lékový parkinsonismus na levodopu nereaguje — řeší se vysazením"], "cervena"),
  ],
  mnemo="Levodopa dovnitř, karbidopa hlídá periferii.",
  zubar="⚠️ Parkinsonik má ztuhlé svaly, třes a hypersalivaci (ne z nadprodukce, ale "
        "z poruchy polykání) — ošetření plánuj krátké, v době nejlepšího účinku léků. "
        "⚠️ Nikdy metoklopramid.",
  past="U mladých pacientů se levodopa spíš šetří a začíná se agonistou — protože "
       "dyskineze po letech léčby jsou největší problém.")

S("55", "Neuroleptika (antipsychotika)",
  jadro="Dopamin má v mozku čtyři dráhy a lék je neumí rozlišit. Proto je jedna "
        "blokáda léčba a tři jsou nežádoucí účinky.",
  tok=[("MEZOLIMBICKÁ ⭐ účinek", "zelena"), ("MEZOKORTIKÁLNÍ ⚠️ horší negativní příznaky", "cervena"),
       ("NIGROSTRIATÁLNÍ ⚠️ extrapyramidové NÚ", "cervena"),
       ("TUBEROINFUNDIBULÁRNÍ ⚠️ prolaktin", "cervena")],
  karty=[
      ("KLASICKÁ × ATYPICKÁ", [
          "Vysokopotentní: haloperidol, flufenazin — ⚠️ hodně extrapyramidových NÚ",
          "Nízkopotentní: chlorpromazin, levomepromazin — ⚠️ sedace, anticholinergní, hypotenze",
          "Atypická (blokují i 5-HT2A): risperidon (⚠️ nejvíc prolaktin),",
          "olanzapin a kvetiapin (⚠️ metabolický syndrom), aripiprazol (parciální agonista)"], "zelena"),
      ("⚠️ EXTRAPYRAMIDOVÉ NÚ V ČASE", [
          "Hodiny → ⚠️ AKUTNÍ DYSTONIE (křeč krku, okulogyrická krize) → biperiden",
          "Dny → AKATIZIE (neschopnost vydržet v klidu)",
          "Týdny → PARKINSONISMUS",
          "⚠️ Měsíce až roky → TARDIVNÍ DYSKINEZE — často NEVRATNÁ"], "cervena"),
      ("⚠️ ZÁVAŽNÉ KOMPLIKACE", [
          "⚠️ MALIGNÍ NEUROLEPTICKÝ SYNDROM: rigidita, horečka, porucha vědomí,",
          "vysoká CK → vysadit lék, DANTROLEN, bromokriptin",
          "⚠️ KLOZAPIN — nejúčinnější u rezistentní schizofrenie, ale AGRANULOCYTÓZA",
          "→ povinné pravidelné krevní obrazy; prakticky nedělá extrapyramidové NÚ",
          "⚠️ Prodloužení QT, metabolický syndrom, hyperprolaktinemie"], "cervena"),
      ("NA CO NEZABEROU", [
          "⚠️ Na negativní příznaky (apatie, oploštělá emotivita, stažení)",
          "Mezokortikální blokádou je mohou i zhoršit",
          "Atypická jsou v tomhle o něco lepší",
          "Indikace i mimo schizofrenii: mánie, agitovanost, těžká deprese (přídavně)"], "bila"),
  ],
  mnemo="Čtyři dráhy: jedna léčí, tři škodí.",
  zubar="⚠️ Xerostomie → kaz a kandidóza. ⚠️ Tardivní dyskineze v orofaciální oblasti "
        "(mlaskání, žvýkací pohyby) → potíže s protézou a ošetřením. ⚠️ Prodloužené QT — "
        "pozor na kombinaci s makrolidy a některými antimykotiky.",
  past="Rozlišení maligního neuroleptického a serotoninového syndromu: neuroleptický "
       "má RIGIDITU a vzniká pomalu, serotoninový má HYPERreflexii a myoklonus a vzniká rychle.")

S("56", "Antidepresiva — tricyklická, inhibitory MAO",
  jadro="Obě skupiny fungují — ale jsou druhou volbou, protože tricyklika jsou "
        "kardiotoxická a inhibitory MAO mají nebezpečné interakce s jídlem.",
  karty=[
      ("TCA — jeden žádaný účinek", [
          "Amitriptylin, nortriptylin, imipramin, klomipramin, dosulepin",
          "⭐ Blokáda reuptake noradrenalinu a serotoninu = léčebný účinek",
          "Dnes hlavně: ⚠️ neuropatická bolest, profylaxe migrény, noční pomočování",
          "(v nižších dávkách, než jaké se používaly na depresi)"], "zelena"),
      ("⚠️ TCA — čtyři nežádoucí blokády", [
          "⚠️ M receptory → XEROSTOMIE, zácpa, retence moči, rozmazané vidění",
          "⚠️ H1 → sedace, přírůstek hmotnosti",
          "⚠️ α1 → ortostatická hypotenze, pády",
          "⚠️ Na⁺ kanály v srdci → ARYTMIE = příčina smrti při předávkování",
          "⚠️ Antidotum arytmie: hydrogenuhličitan sodný"], "cervena"),
      ("INHIBITORY MAO", [
          "Neselektivní ireverzibilní: tranylcypromin, fenelzin",
          "⚠️ SÝROVÁ REAKCE s tyraminem → hypertenzní krize",
          "⚠️ Riziko trvá až 2 týdny po vysazení (enzym se musí vytvořit znovu)",
          "MOKLOBEMID (RIMA) — reverzibilní inhibitor MAO-A, tyramin ho vytlačí → bezpečný",
          "Selegilin, rasagilin — MAO-B, u Parkinsonovy nemoci"], "modra"),
      ("⚠️ SEROTONINOVÝ SYNDROM", [
          "Kombinace IMAO + SSRI, tramadol, triptan, linezolid",
          "Obraz: horečka, ⚠️ myoklonus a HYPERreflexie, neklid, průjem, pocení",
          "⚠️ Odlišení od maligního neuroleptického syndromu: ten má RIGIDITU",
          "Léčba: vysadit, benzodiazepiny, chlazení"], "cervena"),
  ],
  mnemo="Tricyklikum blokuje čtyři věci navíc — a každá z nich má svůj nežádoucí účinek.",
  zubar="⚠️ Výrazná xerostomie → mnohočetný kaz. ⚠️ A pozor s adrenalinem v anestetiku: "
        "tricyklika blokují jeho zpětné vychytávání a účinek zesílí — používej "
        "nejnižší účinné množství a aspiruj.",
  past="Zásoba tricyklik na dva týdny může být smrtelná dávka — u pacienta se "
       "suicidálními myšlenkami je to zásadní argument proti.")

S("57", "Antidepresiva — SSRI, SNRI, atypická",
  jadro="SSRI nejsou účinnější než tricyklika — jsou jen bezpečnější při předávkování "
        "a snesitelnější. To je celý důvod, proč se to změnilo.",
  tok=[("nasazení SSRI", "zelena"), ("1.–2. týden ⚠️ vrátí se ENERGIE", "cervena"),
       ("2.–4. týden zlepší se NÁLADA", "bila"), ("plný účinek", "zelena")],
  karty=[
      ("SSRI", [
          "Fluoxetin — ⚠️ dlouhý poločas, silný inhibitor CYP2D6",
          "Sertralin — nejmenší interakce",
          "Escitalopram, citalopram — ⚠️ prodlužují QT",
          "Paroxetin — ⚠️ anticholinergní, nejhorší discontinuation syndrom"], "zelena"),
      ("⚠️ NEŽÁDOUCÍ ÚČINKY", [
          "Nauzea na začátku, ⚠️ sexuální dysfunkce (přetrvává)",
          "Nespavost nebo naopak útlum",
          "⚠️ Hyponatremie (SIADH) u seniorů",
          "⚠️ KRVÁCENÍ — vyprázdnění serotoninu z trombocytů",
          "⚠️ Discontinuation syndrom — závratě, „elektrické šoky\", úzkost"], "cervena"),
      ("SNRI A ATYPICKÁ", [
          "Venlafaxin — ⚠️ ve vyšších dávkách zvyšuje tlak",
          "Duloxetin — i diabetická neuropatie a stresová inkontinence",
          "⚠️ MIRTAZAPIN — sedace + chuť k jídlu (výhoda u nespavého a hubnoucího)",
          "⚠️ BUPROPION — bez sexuálních NÚ, pomáhá přestat kouřit, ⚠️ snižuje práh křečí",
          "Trazodon (na spánek), agomelatin, vortioxetin"], "modra"),
      ("⚠️ PAST LATENCE", [
          "Účinek nastupuje za 2–4 týdny",
          "⚠️ Psychomotorický útlum se upraví DŘÍV než nálada",
          "→ pacient dostane energii, ale ještě má depresivní myšlenky",
          "⚠️ Na začátku léčby proto STOUPÁ riziko sebevraždy",
          "Léčit nejméně 6 měsíců po odeznění příznaků"], "cervena"),
  ],
  mnemo="Energie se vrátí dřív než nálada. To je ta nebezpečná chvíle.",
  zubar="⚠️ SSRI vyprázdní serotonin z destiček → horší agregace → DELŠÍ KRVÁCENÍ "
        "PO EXTRAKCI, zvlášť v kombinaci s NSA. ⚠️ Lék se kvůli tomu nevysazuje — "
        "počítej s tím a ošetři lůžko (šití, tranexamová kyselina).",
  past="Kombinace SSRI s tramadolem nebo triptanem může vyvolat serotoninový syndrom — "
       "u analgezie po výkonu to má praktický dopad.")

S("58", "Anxiolytika, stabilizátory nálady",
  jadro="Úzkostná porucha se dlouhodobě neléčí benzodiazepiny, ale antidepresivy. "
        "A u bipolární poruchy je hlavní téma lithium a jeho úzké okno.",
  karty=[
      ("ANXIOLYTIKA", [
          "⚠️ Benzodiazepiny — jen krátkodobě, na překlenutí prvních týdnů",
          "⭐ SSRI a SNRI — dlouhodobá léčba první volby",
          "Buspiron — ⚠️ nenávykový, bez sedace, ale nastupuje týdny",
          "Hydroxyzin, pregabalin",
          "⚠️ Betablokátory — jen na tělesné projevy (třes, palpitace) u trémy"], "zelena"),
      ("⚠️ LITHIUM — nejužší okno v psychiatrii", [
          "⚠️ Terapeutické rozmezí 0,6–1,2 mmol/l → nutné měřit hladiny",
          "⚠️ Vylučuje se VÝHRADNĚ ledvinami, nemetabolizuje se",
          "⚠️ Hladinu zvednou: NSA, ACE inhibitory a sartany, thiazidy, dehydratace",
          "(při nedostatku sodíku si ho ledvina plete se sodíkem a šetří)"], "cervena"),
      ("⚠️ LITHIUM — NÚ a otrava", [
          "Třes, polyurie a žízeň (⚠️ nefrogenní diabetes insipidus)",
          "⚠️ Hypotyreóza, přírůstek hmotnosti, akné",
          "⚠️ TERATOGEN — Ebsteinova anomálie",
          "Otrava: zvracení, ataxie, zmatenost, křeče → hemodialýza"], "cervena"),
      ("DALŠÍ STABILIZÁTORY", [
          "Valproát, karbamazepin",
          "⚠️ LAMOTRIGIN — jediný s převahou účinku na DEPRESIVNÍ pól",
          "Atypická antipsychotika (kvetiapin, olanzapin, aripiprazol)",
          "⚠️ Antidepresivum u bipolární poruchy jen se stabilizátorem — jinak přepne do mánie"], "modra"),
  ],
  mnemo="Lithium jde ledvinami. Cokoli, co zhorší ledviny, zvedne jeho hladinu.",
  zubar="⚠️ NSA po extrakci u pacienta na lithiu je reálné riziko intoxikace — "
        "volit paracetamol. Lithium také způsobuje xerostomii a kovovou chuť.",
  past="Benzodiazepin na dlouhodobou úzkost je chyba: tolerance, závislost, "
       "rebound úzkost a zhoršení kognice.")

S("59", "Farmakoterapie Alzheimerovy choroby, nootropika",
  jadro="Žádný z těch léků nemoc nezastaví. Zpomalí zhoršování a zlepší denní fungování.",
  karty=[
      ("INHIBITORY ACETYLCHOLINESTERÁZY", [
          "Lehké až středně těžké stadium",
          "Donepezil (1× denně), rivastigmin (⚠️ i náplast), galantamin",
          "⚠️ Základ: nejdřív zanikají cholinergní neurony v nucleus basalis Meynerti",
          "⚠️ NÚ = SLUDGE v mírnější podobě: nevolnost, průjem, hypersalivace, bradykardie"], "zelena"),
      ("MEMANTIN", [
          "Antagonista NMDA receptoru (glutamátová hypotéza)",
          "Středně těžké až těžké stadium",
          "Lze kombinovat s inhibitorem AChE",
          "Lépe snášený, méně GIT potíží"], "modra"),
      ("⚠️ CO NEDÁVAT", [
          "⚠️ Anticholinergika (oxybutynin, antihistaminika I. generace, tricyklika)",
          "→ ruší si tím vlastní léčbu a zhorší kognici",
          "⚠️ Benzodiazepiny — zmatenost a pády",
          "⚠️ Klasická antipsychotika — zvyšují úmrtnost u demence"], "cervena"),
      ("NOVÁ LÉČBA A NOOTROPIKA", [
          "Protilátky proti amyloidu (lekanemab, donanemab) — ⚠️ [⚠️ ověřit dle skript]",
          "⚠️ Riziko mozkových otoků a mikrokrvácení",
          "Nootropika: piracetam, ginkgo, vinpocetin",
          "⚠️ Evidence slabá až žádná — u prokázané Alzheimerovy nemoci nejsou léčbou"], "bila"),
  ],
  mnemo="Cholinergní systém dole → doplň acetylcholin. Glutamát nahoře → zablokuj NMDA.",
  zubar="⚠️ Dementní pacient postupně přestává zvládat ústní hygienu → prudký nárůst "
        "kazu a parodontitidy. Ošetření a sanaci plánuj co nejdřív, dokud spolupracuje. "
        "⚠️ Inhibitory AChE způsobují hypersalivaci.",
  past="Klasická chyba: geriatr předepíše dementnímu pacientovi oxybutynin na měchýř — "
       "a tím zruší účinek donepezilu.")

S("60", "Opium a jeho alkaloidy",
  jadro="Opium má dvě chemické skupiny alkaloidů — a jen jedna z nich tlumí bolest "
        "a je návyková.",
  tok=[("FENANTHRENOVÉ morfin, kodein, thebain", "zelena"),
       ("⚠️ analgezie + závislost", "cervena"),
       ("ISOCHINOLINOVÉ papaverin, noskapin", "modra"),
       ("⚠️ BEZ analgezie a závislosti", "bila")],
  karty=[
      ("PŮVOD A SLOŽENÍ", [
          "Opium = zaschlá šťáva z nezralých makovic máku setého (Papaver somniferum)",
          "Fenanthrenové alkaloidy: morfin, kodein, thebain",
          "Isochinolinové: papaverin (spazmolytikum), noskapin (antitusikum)",
          "⚠️ Isochinolinové netlumí bolest a nejsou návykové"], "zelena"),
      ("MECHANISMUS", [
          "Receptory μ, κ, δ — spřažené s Gi",
          "↓ cAMP, otevření K⁺ kanálů, uzavření Ca²⁺ kanálů",
          "→ ⚠️ buňka se hyperpolarizuje a nevyšle vzruch",
          "Působí pre- i postsynapticky, míšně i v mozku"], "modra"),
      ("ÚČINKY", [
          "Analgezie, euforie, sedace, antitusický účinek",
          "⚠️ Útlum dechového centra — snížení citlivosti k CO₂ = příčina smrti",
          "⚠️ Mióza · ⚠️ zácpa · nauzea · uvolnění histaminu (svědění, hypotenze)",
          "⚠️ Stah Oddiho svěrače → u biliární koliky nikdy bez spazmolytika"], "cervena"),
      ("⚠️ TOLERANCE A OTRAVA", [
          "🔑 Toleruje se: analgezie, euforie, útlum dechu, nauzea",
          "⚠️ NETOLERUJE SE: MIÓZA a ZÁCPA",
          "→ špendlíková zornice je diagnostická i u letitého uživatele",
          "⚠️ Trias otravy: kóma + útlum dechu + mióza",
          "⚠️ Antidotum NALOXON — kratší poločas než morfin, nutné opakovat"], "cervena"),
  ],
  mnemo="Mióza a zácpa se netolerují nikdy. Proto zornice prozradí uživatele.",
  zubar="Opioidy v zubní praxi jen výjimečně — bolest po výkonu je zánětlivá a lépe "
        "na ni zabere ibuprofen s paracetamolem.",
  past="Kodein je proléčivo aktivované CYP2D6 na morfin — u ultrarychlých metabolizátorů "
       "hrozí předávkování (popsána úmrtí dětí), u pomalých nezabere vůbec.")

S("61", "Deriváty a náhražky morfinu",
  jadro="Řadím je podle síly a podle chování na receptoru — z toho plyne, k čemu se "
        "hodí a čím jsou nebezpečné.",
  karty=[
      ("SILNÉ — plní agonisté μ", [
          "⚠️ FENTANYL — 100× morfin, náplast; ⚠️ rigidita hrudní stěny při rychlém i.v.",
          "Sufentanil · ⚠️ REMIFENTANIL (rozkládají esterázy, kontextově necitlivý poločas)",
          "Oxykodon, hydromorfon",
          "⚠️ METADON — dlouhý poločas → substituce; ⚠️ prodlužuje QT",
          "⚠️ PETIDIN — metabolit norpetidin dráždí CNS (křeče); ⚠️ smrtelná interakce s IMAO"], "zelena"),
      ("SLABÉ", [
          "Kodein, dihydrokodein",
          "⚠️ TRAMADOL — duální: slabý μ agonista + blokáda reuptake NA a 5-HT",
          "⚠️ Serotoninový syndrom s SSRI; ⚠️ snižuje práh křečí",
          "Vhodný u neuropatické bolesti"], "modra"),
      ("PARCIÁLNÍ A SMÍŠENÉ", [
          "⚠️ BUPRENORFIN — parciální agonista: má strop dechového útlumu,",
          "⚠️ ale drží se receptoru tak pevně, že ho naloxon těžko vytlačí",
          "Nalbufin, pentazocin — smíšení agonisté-antagonisté",
          "⚠️ U pacienta na plném agonistovi mohou vyvolat odvykací stav"], "bila"),
      ("ANTAGONISTÉ A ZÁSADY", [
          "NALOXON i.v. — akutní otrava; ⚠️ kratší poločas → opakovat",
          "NALTREXON p.o. — prevence relapsu u závislostí",
          "⚠️ METHYLNALTREXON — neprojde do mozku → jen na opioidovou zácpu",
          "⚠️ Žebříček WHO: neopioid → slabý opioid → silný opioid",
          "⚠️ U chronické bolesti dávkovat podle hodin, ne podle potřeby"], "zluta"),
  ],
  mnemo="Plný agonista nemá strop. Parciální ho má, ale hůř se ruší.",
  zubar="⚠️ Pacient na substituci metadonem nebo buprenorfinem má vysokou toleranci — "
        "jeho substituční dávka analgezii NEZAJIŠŤUJE. Po výkonu potřebuje běžnou, "
        "často i vyšší analgezii, ne odepření léčby.",
  past="Tramadol není „bezpečný opioid\" — jeho serotoninová složka znamená riziko "
       "serotoninového syndromu a snížený práh křečí.")

S("62", "Eikosanoidy",
  jadro="Kortikoid blokuje o patro výš než NSA — proto vypne obě větve najednou. "
        "A proto NSA mohou vyvolat astma.",
  tok=[("FOSFOLIPIDY MEMBRÁNY", "bila"),
       ("⚠️ fosfolipáza A₂ — tady blokují KORTIKOIDY", "cervena"),
       ("KYSELINA ARACHIDONOVÁ", "zelena"),
       ("COX ⚠️ NSA · LOX ⚠️ NSA sem nesahají", "cervena")],
  karty=[
      ("DVĚ VĚTVE", [
          "COX → prostaglandiny, prostacyklin (PGI₂), tromboxan (TXA₂)",
          "LOX → leukotrieny (bronchokonstrikce, hlen, chemotaxe)",
          "⚠️ NSA blokují jen COX → kyselina se PŘELIJE do větve leukotrienů",
          "→ ⚠️ ASPIRINEM INDUKOVANÉ ASTMA",
          "⚠️ Samterova trias: astma + nosní polypy + intolerance aspirinu"], "cervena"),
      ("COX-1 × COX-2", [
          "COX-1 konstitutivní: ochranný hlen žaludku, tromboxan v destičkách,",
          "průtok ledvinou",
          "COX-2 indukovatelná: zánět, bolest, horečka",
          "⚠️ Ale COX-2 je i normálně v endotelu (PGI₂) a v ledvině",
          "→ proto koxiby zvyšují kardiovaskulární riziko"], "zelena"),
      ("PROTIPÓL TXA₂ × PGI₂", [
          "TXA₂ z destiček — sráží krev a stahuje cévu",
          "PGI₂ z endotelu — brání srážení a cévu rozšiřuje",
          "⚠️ Rovnováha mezi nimi drží krev tekutou",
          "Aspirin ji posouvá ve prospěch PGI₂ (destička si COX neobnoví)"], "modra"),
      ("LÉČEBNĚ POUŽÍVANÁ ANALOGA", [
          "⚠️ MISOPROSTOL (PGE1) — prevence vředu z NSA; ⚠️ vyvolává děložní stahy",
          "Alprostadil (PGE1) — udrží otevřený ductus arteriosus",
          "Latanoprost — glaukom · epoprostenol, iloprost — plicní hypertenze",
          "Dinoproston — indukce porodu",
          "Antileukotrieny: MONTELUKAST (astma, hlavně u dětí a námahové)"], "bila"),
  ],
  mnemo="Kortikoid vypne obě větve. NSA jen jednu — a druhá se tím přeplní.",
  zubar="Zánětlivá bolest po extrakci je z prostaglandinů — proto ibuprofen zabírá "
        "lépe než paracetamol. ⚠️ U pacienta se Samterovou triádou volit paracetamol.",
  past="Prostaglandiny nejsou jen „zánětové látky\" — chrání žaludeční sliznici a "
       "udržují průtok ledvinou. Odtud pochází většina nežádoucích účinků NSA.")

S("63", "Analgetika-antipyretika",
  jadro="Na rozdíl od NSA nemají významný protizánětlivý účinek. Hlavním tématem "
        "paracetamolu je jaterní toxicita.",
  tok=[("PARACETAMOL", "zelena"), ("90 % konjugace → neškodné", "bila"),
       ("10 % CYP2E1 → ⚠️ NAPQI", "cervena"), ("GLUTATHION ho zneškodní", "zelena")],
  karty=[
      ("PARACETAMOL", [
          "Působí centrálně; ⚠️ nedráždí žaludek, neovlivňuje srážení",
          "⚠️ Bezpečný v graviditě, u dětí, u astmatu a vředové choroby",
          "⚠️ Maximálně 4 g/den, u rizikových méně",
          "⚠️ Nemá protizánětlivý účinek"], "zelena"),
      ("⚠️ OTRAVA PARACETAMOLEM", [
          "Nasytí se konjugace → víc NAPQI → ⚠️ vyčerpá se glutathion → nekróza jater",
          "⚠️ Alkoholik: indukovaný CYP2E1 A vyčerpaný glutathion — obojí táhne stejným směrem",
          "⚠️ Příznaky přijdou AŽ ZA 1–3 DNY — první dva dny může být pacient bez potíží",
          "⚠️ Rozhoduje HLADINA V ČASE (nomogram), ne stav pacienta",
          "⚠️ Antidotum N-ACETYLCYSTEIN, nejúčinnější do 8 hodin"], "cervena"),
      ("METAMIZOL a další", [
          "⚠️ Metamizol — silná analgezie + SPAZMOLYTICKÝ účinek (koliky)",
          "⚠️ Riziko agranulocytózy; ⚠️ prudký pokles tlaku při rychlém i.v. podání",
          "Kyselina acetylsalicylová v analgetické dávce",
          "Kombinace s kofeinem (zvyšuje účinnost)"], "modra"),
      ("KDY CO", [
          "⚠️ Paracetamol lepší: vřed, astma s intolerancí NSA, antikoagulace,",
          "gravidita, malé dítě, renální insuficience",
          "⚠️ Po extrakci je ibuprofen ÚČINNĚJŠÍ než paracetamol",
          "⭐ Nejúčinnější neopioidní schéma: IBUPROFEN + PARACETAMOL"], "zluta"),
  ],
  mnemo="Paracetamol netlumí zánět. Proto po extrakci sám nestačí.",
  zubar="⚠️ Kombinace ibuprofen + paracetamol po extrakci předčí i slabé opioidy. "
        "Působí dvěma různými mechanismy a nesčítají se jim nežádoucí účinky.",
  past="U otravy paracetamolem se nečeká na příznaky — když přijdou, játra se už "
       "rozpadají a antidotum má menší účinek.")

S("64", "Nesteroidní antiflogistika",
  jadro="Skoro všechny nežádoucí účinky NSA plynou z toho, že blokují COX-1 tam, "
        "kde ji tělo potřebuje.",
  karty=[
      ("DĚLENÍ PODLE SELEKTIVITY", [
          "Neselektivní: ibuprofen, diklofenak, ⚠️ naproxen (nejnižší KV riziko),",
          "indometacin, ketoprofen, piroxikam, ⚠️ kyselina acetylsalicylová",
          "Preferenční COX-2: nimesulid, meloxikam",
          "⚠️ Koxiby: celekoxib, etorikoxib — méně GIT potíží, ⚠️ vyšší KV riziko",
          "(rofekoxib byl proto stažen)"], "zelena"),
      ("⚠️ ASPIRIN JE JINÝ", [
          "⚠️ Jako jediný acetyluje COX IREVERZIBILNĚ",
          "⚠️ Destička nemá jádro a enzym si nevyrobí",
          "→ antiagregační účinek trvá 7–10 dní = celý život destičky",
          "→ proto stačí 100 mg denně"], "modra"),
      ("⚠️ NEŽÁDOUCÍ ÚČINKY PODLE ORGÁNU", [
          "⚠️ Žaludek — vřed a krvácení (vzniká i po i.v. podání!) → prevence PPI",
          "⚠️ Ledvina — zruší prostaglandinovou vazodilataci přívodné tepénky",
          "→ u dehydratovaného a seniora akutní selhání; analgetická nefropatie",
          "Hypertenze, otoky, kardiovaskulární riziko",
          "⚠️ Reyeův syndrom u dětí · ⚠️ aspirinem indukované astma"], "cervena"),
      ("⚠️ INTERAKCE", [
          "⚠️ „TRIPLE WHAMMY\": NSA + ACE inhibitor/sartan + diuretikum → selhání ledvin",
          "⚠️ IBUPROFEN RUŠÍ antiagregační účinek aspirinu (obsadí COX-1 dřív)",
          "→ aspirin podat 2 hodiny před ibuprofenem",
          "⚠️ NSA + warfarin → krvácení · NSA + lithium → intoxikace"], "cervena"),
  ],
  mnemo="COX-1 chrání žaludek, ledvinu a sráží krev. Zablokuješ ji — a máš tři nežádoucí účinky.",
  zubar="⚠️ Ibuprofen je po extrakci lék volby, ⚠️ ale u antikoagulovaného pacienta, "
        "u vředové choroby a u renální insuficience volit paracetamol. "
        "⚠️ Nikdy NSA u hemofilika.",
  past="Vřed z NSA nevzniká místním drážděním, ale systémovou blokádou COX-1 — "
       "proto se objeví i po nitrožilním podání a čípek před ním neochrání.")

S("65", "Farmakoterapie migrény",
  jadro="Migréna není obyčejná bolest hlavy — je to neurovaskulární onemocnění "
        "s aktivací trigeminovaskulárního systému a vyplavením CGRP.",
  karty=[
      ("AKUTNÍ LÉČBA", [
          "⚠️ Co nejdřív, hned na začátku záchvatu",
          "NSA nebo paracetamol",
          "⚠️ + METOKLOPRAMID nebo domperidon — nejen proti nevolnosti:",
          "při migréně se zastaví vyprazdňování žaludku a analgetikum se nevstřebá"], "zelena"),
      ("TRIPTANY", [
          "Sumatriptan, eletriptan, zolmitriptan",
          "⚠️ Agonisté 5-HT1B/1D → stáhnou rozšířené cévy a zastaví výdej CGRP",
          "⚠️ KI: ischemická choroba srdeční, nekontrolovaná hypertenze",
          "⚠️ Nekombinovat s ergotaminem (obojí vazokonstrikce)",
          "⚠️ Ergotamin je obsoletní — riziko ergotismu"], "modra"),
      ("⚠️ BOLEST Z NADUŽÍVÁNÍ LÉKŮ", [
          "Analgetika víc než 10–15 dní v měsíci",
          "⚠️ Bolest je pak způsobená samotnou léčbou",
          "⚠️ Řešením je VYSAZENÍ, ne přidání dalšího analgetika",
          "Typické u kombinovaných přípravků s kofeinem a kodeinem"], "cervena"),
      ("PROFYLAXE — při 4+ záchvatech měsíčně", [
          "Betablokátory (metoprolol, propranolol) — ⚠️ řeší i hypertenzi",
          "Topiramát (⚠️ snižuje hmotnost), valproát (⚠️ ne u žen ve fertilním věku)",
          "Amitriptylin (⚠️ vhodný u depresivního pacienta), flunarizin, kandesartan",
          "⚠️ Protilátky proti CGRP (erenumab, fremanezumab) u těžkých forem",
          "⚠️ Botulotoxin u chronické migrény · hodnotí se až po 2–3 měsících"], "bila"),
  ],
  mnemo="Nejdřív rozhýbat žaludek, pak analgetikum. Jinak se ani nevstřebá.",
  zubar="⚠️ Migréna se často plete s bolestí z čelistního kloubu nebo s dentální "
        "bolestí — a naopak. ⚠️ Migréna s aurou je kontraindikací kombinované antikoncepce.",
  past="Profylaxe se nehodnotí po týdnu. Účinek se posuzuje až po 2–3 měsících "
       "pravidelného užívání.")

S("66", "Léčiva s pozitivně inotropním účinkem, digoxin",
  jadro="Blokádou sodíkové pumpy přibude uvnitř buňky vápník — a srdce se stáhne silněji.",
  tok=[("DIGOXIN blokuje Na⁺/K⁺-ATPázu", "zelena"), ("sodíku uvnitř PŘIBUDE", "bila"),
       ("výměník Na⁺/Ca²⁺ nevyváží vápník", "bila"), ("⚠️ VÍC Ca²⁺ → SILNĚJŠÍ STAH", "zelena")],
  karty=[
      ("ČTYŘI SKUPINY INOTROPIK", [
          "Srdeční glykosidy — digoxin, digitoxin",
          "Sympatomimetika — dobutamin (β1), dopamin",
          "Inhibitory fosfodiesterázy 3 — milrinon („inodilatátor\")",
          "⚠️ Levosimendan — senzitizér: zvýší citlivost myofilament k vápníku"], "zelena"),
      ("DIGOXIN — dva účinky", [
          "⭐ Pozitivně inotropní (přes vápník)",
          "⭐ ⚠️ Vagotonický — zpomalí vedení v AV uzlu",
          "Indikace: ⚠️ fibrilace síní s rychlou odpovědí, srdeční selhání",
          "⚠️ Zlepší příznaky, ale NEPRODLOUŽÍ život",
          "⚠️ Vylučuje se ledvinami (digitoxin játry)"], "modra"),
      ("⚠️ TOXICITA", [
          "⚠️ Velmi úzké terapeutické okno → měří se hladiny",
          "⚠️ HYPOKALEMIE ZVYŠUJE TOXICITU — draslík a digoxin soutěží o stejné místo",
          "⚠️ A hypokalemii dělají diuretika, která pacient skoro vždy má",
          "Obraz: nevolnost, zvracení, ⚠️ ŽLUTÉ VIDĚNÍ (xantopsie), zmatenost,",
          "⚠️ arytmie (bigeminie, AV blokáda)"], "cervena"),
      ("LÉČBA OTRAVY A ZÁSADY", [
          "⚠️ Protilátky proti digoxinu (Fab fragmenty)",
          "Úprava kalia a magnezia",
          "⚠️ Opatrně u seniorů — klesá funkce ledvin",
          "⚠️ Inotropika se nepodávají chronicky — poháněné srdce se rychleji vyčerpá"], "bila"),
  ],
  mnemo="Málo draslíku = víc digoxinu na pumpě = otrava.",
  zubar="⚠️ Pacient na digoxinu: opatrně s adrenalinem v anestetiku (arytmie) "
        "a ⚠️ NSA mohou zhoršit funkci ledvin a tím zvýšit hladinu digoxinu.",
  past="Digoxin zlepší, jak se pacient cítí, ale ne to, jak dlouho bude žít — "
       "prognózu mění jen čtyři pilíře léčby srdečního selhání.")

S("67", "Antiarytmika",
  jadro="Vaughanova–Williamsova klasifikace řadí antiarytmika podle kanálu, který "
        "blokují. A platí věta: každé antiarytmikum může arytmii také vyvolat.",
  karty=[
      ("I. — BLOKÁTORY Na⁺ KANÁLŮ", [
          "IA chinidin, prokainamid, ajmalin — prodlužují akční potenciál",
          "IB ⚠️ LIDOKAIN, mexiletin — zkracují; ⚠️ komorové arytmie u infarktu",
          "⚠️ IC propafenon, flekainid — silně zpomalují vedení",
          "⚠️ KI u strukturálního postižení srdce (studie CAST: po infarktu",
          "potlačily extrasystoly, ale ZVÝŠILY úmrtnost)"], "cervena"),
      ("II. a IV. TŘÍDA", [
          "⭐ II. BETABLOKÁTORY — ⚠️ jediná třída, která prokazatelně snižuje úmrtnost",
          "IV. blokátory Ca²⁺ — verapamil, diltiazem",
          "⚠️ Nekombinovat II. a IV. (AV blokáda)",
          "Indikace: kontrola frekvence u fibrilace síní, supraventrikulární arytmie"], "zelena"),
      ("III. — BLOKÁTORY K⁺ KANÁLŮ", [
          "⚠️ AMIODARON — nejúčinnější, ale nejtoxičtější",
          "⚠️ Obsahuje jód → tyreopatie (hypo- i hyper-), plicní fibróza,",
          "usazeniny v rohovce, fotosenzitivita a modrošedé zbarvení kůže, hepatotoxicita",
          "⚠️ Poločas týdny až měsíce (ukládá se v tucích)",
          "Sotalol (+ betablokáda), dronedaron; ⚠️ prodlužují QT → torsades"], "cervena"),
      ("MIMO KLASIFIKACI", [
          "⚠️ ADENOSIN — poločas vteřiny, rychlý bolus, na pár vteřin zastaví srdce",
          "→ ukončí paroxysmální supraventrikulární tachykardii (pacienta varovat)",
          "Digoxin, magnezium (⚠️ lék volby u torsades), atropin, ivabradin",
          "⚠️ Torsades de pointes = polymorfní KT při dlouhém QT"], "modra"),
  ],
  mnemo="I. sodík · II. beta · III. draslík · IV. vápník. A všechna jsou proarytmická.",
  zubar="⚠️ Amiodaron a sotalol prodlužují QT — nekombinovat s makrolidy, azolovými "
        "antimykotiky ani s ondansetronem. Před předpisem zkontroluj medikaci.",
  past="Potlačení extrasystol není cíl léčby. Studie CAST ukázala, že se tím dá "
       "úmrtnost zvýšit, ne snížit.")

S("68", "ACE inhibitory a antagonisté angiotensinu",
  jadro="ACE má dva úkoly: tvoří angiotensin II a rozkládá bradykinin. Z toho druhého "
        "plyne suchý kašel — a proto ho sartany nedělají.",
  tok=[("angiotensinogen", "bila"), ("angiotensin I", "bila"),
       ("⚠️ ACE = i kinináza II", "cervena"), ("angiotensin II → receptor AT1", "zelena")],
  karty=[
      ("SYSTÉM RAAS", [
          "Renin z ledviny → angiotensinogen → angiotensin I",
          "ACE → angiotensin II → receptor AT1",
          "Účinky AT1: stah cév, aldosteron, remodelace myokardu, žízeň, ADH",
          "⚠️ ACE je zároveň KININÁZA II — rozkládá bradykinin"], "zelena"),
      ("ROZDÍL ACEI × SARTAN", [
          "⚠️ ACE inhibitor zastaví i rozklad bradykininu → hromadí se",
          "→ ⚠️ SUCHÝ DRÁŽDIVÝ KAŠEL a vzácně ANGIOEDÉM",
          "⚠️ Sartan blokuje až receptor AT1 → bradykinin neovlivní → BEZ KAŠLE",
          "Zástupci: ramipril, perindopril, enalapril (-pril)",
          "losartan, valsartan, telmisartan, kandesartan (-sartan)"], "modra"),
      ("INDIKACE a ⚠️ RENOPROTEKCE", [
          "Hypertenze, srdeční selhání, stav po infarktu",
          "⚠️ Diabetická a proteinurická nefropatie",
          "⚠️ Uvolní ODVODNOU tepénku → klesne tlak v glomerulu → přestane se ničit",
          "⚠️ Mírný vzestup kreatininu na začátku je proto ŽÁDANÝ, ne selhání",
          "ARNI (sakubitril/valsartan) — dnešní standard u srdečního selhání"], "zelena"),
      ("⚠️ NÚ A KONTRAINDIKACE", [
          "⚠️ Hyperkalemie, hypotenze po první dávce",
          "⚠️ ANGIOEDÉM — otok jazyka a hrtanu, i po letech léčby",
          "⚠️ KI: GRAVIDITA (absolutně), oboustranná stenóza renálních tepen",
          "⚠️ Nekombinovat ACEI + sartan",
          "⚠️ Nejrizikovější kombinace: ACEI + spironolakton + NSA"], "cervena"),
  ],
  mnemo="Bradykinin dělá kašel. Sartan na něj nesahá.",
  zubar="⚠️ ANGIOEDÉM po ACE inhibitoru je v zubní ordinaci diferenciální diagnóza "
        "otoku obličeje a jazyka — může přijít i po letech užívání a nesouvisí s alergií. "
        "⚠️ Suchý kašel je také častý.",
  past="U stenózy renálních tepen si ledvina drží filtraci právě stahem odvodné "
       "tepénky — když ho zrušíš, filtrace se zhroutí.")

S("69", "Diuretika",
  jadro="Místo účinku v nefronu určuje sílu diuretika i to, jakou minerálovou "
        "poruchu udělá.",
  tok=[("PROXIMÁLNÍ acetazolamid, mannitol", "bila"),
       ("HENLEOVA KLIČKA ⚠️ FUROSEMID", "zelena"),
       ("DISTÁLNÍ thiazidy", "bila"), ("SBĚRACÍ KANÁLEK kalium šetřící", "modra")],
  karty=[
      ("KLIČKOVÁ — furosemid", [
          "Blokáda kotransportéru NKCC2 ve vzestupném raménku",
          "⚠️ NEJSILNĚJŠÍ — klička vstřebává nejvíc sodíku",
          "⚠️ Funguje i při selhání ledvin",
          "⚠️ ZTRÁCÍ VÁPNÍK · ⚠️ ototoxicita · hypokalemie, hypomagnezemie",
          "⚠️ i.v. působí žilní dilatací dřív, než přijde diuréza (plicní edém)"], "zelena"),
      ("THIAZIDY", [
          "Hydrochlorothiazid, indapamid, chlortalidon — blokáda NCC v distálním tubulu",
          "⚠️ ŠETŘÍ VÁPNÍK (opak furosemidu) → vhodné u kalciových kamenů",
          "⚠️ Nefungují při těžkém selhání ledvin",
          "⚠️ Metabolické NÚ: hyperurikemie (dna), hyperglykemie, hyperlipidemie,",
          "⚠️ hyponatremie (nejčastěji u seniorek)"], "modra"),
      ("KALIUM ŠETŘÍCÍ", [
          "Antagonisté aldosteronu: ⚠️ SPIRONOLAKTON, eplerenon",
          "Blokátory Na⁺ kanálu: amilorid, triamteren",
          "⚠️ Spironolakton zlepšuje přežití u srdečního selhání",
          "⚠️ NÚ spironolaktonu: gynekomastie, poruchy cyklu (eplerenon je čistší)",
          "⚠️ Riziko hyperkalemie, zvlášť s ACE inhibitorem"], "bila"),
      ("OSTATNÍ A ZÁSADY", [
          "Acetazolamid (karboanhydráza) — glaukom, ⚠️ výšková nemoc (vyvolá acidózu",
          "→ zrychlí dýchání a urychlí aklimatizaci); ⚠️ metabolická acidóza",
          "Mannitol (osmotické) — ⚠️ mozkový edém, glaukom",
          "⚠️ Všechna kromě kalium šetřících ztrácejí draslík → konflikt s digoxinem"], "cervena"),
  ],
  mnemo="Furosemid vápník VYPLAVÍ, thiazid ho ZADRŽÍ.",
  zubar="⚠️ Pacient na diureticích má často xerostomii a je náchylnější k ortostatické "
        "hypotenzi — po delším ošetření vleže ho nechej chvíli sedět.",
  past="Thiazid u pacienta s dnou je chyba — zvýší kyselinu močovou a vyvolá záchvat.")

S("70", "Blokátory kalciových kanálů",
  jadro="Dihydropyridiny míří na cévy, verapamil a diltiazem na srdce. Z toho plyne "
        "všechno — indikace i to, co se nesmí kombinovat.",
  karty=[
      ("DIHYDROPYRIDINY (-dipin)", [
          "Amlodipin, nifedipin, nitrendipin, lerkanidipin, felodipin",
          "⚠️ Hlavně CÉVY → vazodilatace → snížení tlaku",
          "NÚ: ⚠️ otoky kotníků, návaly, bolest hlavy, reflexní tachykardie",
          "⚠️ HYPERPLAZIE GINGIVY (hlavně nifedipin)"], "zelena"),
      ("VERAPAMIL a DILTIAZEM", [
          "⚠️ VERAPAMIL (fenylalkylamin) — hlavně SRDCE: bradykardie,",
          "negativně inotropní, ⚠️ zácpa",
          "⚠️ DILTIAZEM je BENZOTHIAZEPIN — někde mezi oběma skupinami",
          "⚠️ NEKOMBINOVAT s betablokátorem → AV blokáda",
          "⚠️ KI u srdečního selhání (negativně inotropní)"], "cervena"),
      ("INDIKACE", [
          "Hypertenze (hlavně dihydropyridiny, vhodné u seniorů)",
          "Angina pectoris, ⚠️ vazospastická (Prinzmetalova) angina",
          "⚠️ Verapamil a diltiazem: fibrilace síní a supraventrikulární tachykardie",
          "⚠️ Verapamil tam, kde je kontraindikovaný betablokátor (astma)",
          "Nimodipin — prevence vazospazmu po subarachnoidálním krvácení"], "modra"),
      ("⚠️ CHYBY VE ZDROJI A INTERAKCE", [
          "⚠️ Zdroj uvádí diltiazem jako „benzodiazepin\" — správně BENZOTHIAZEPIN",
          "⚠️ Zdroj uvádí verapamil při KI „β-agonistů\" — správně β-ANTAGONISTŮ",
          "⚠️ GRAPEFRUIT inhibuje CYP3A4 → hladina stoupne → hypotenze",
          "⚠️ Otoky kotníků nejsou z retence — diuretikum na ně nepomůže,",
          "pomůže přidání ACE inhibitoru"], "cervena"),
  ],
  mnemo="Dipiny na cévy, verapamil na srdce.",
  zubar="⚠️ HYPERPLAZIE GINGIVY — třetí lék vedle fenytoinu a cyklosporinu. "
        "Rozsah závisí na ústní hygieně; při dokonalé hygieně se výrazně zmenší. "
        "Chirurgie má smysl až po zlepšení hygieny, jinak recidivuje.",
  past="Verapamil s betablokátorem je nebezpečná kombinace — oba zpomalují vedení "
       "v AV uzlu a mohou vyvolat blokádu.")

S("71", "Nitrity a nitráty",
  jadro="Nitráty nerozšiřují hlavně věnčité tepny — rozšiřují ŽÍLY a tím sníží "
        "nároky srdce na kyslík.",
  tok=[("NITRÁT uvolní NO", "zelena"), ("guanylátcykláza → ↑ cGMP", "bila"),
       ("⚠️ dilatace hlavně ŽIL", "zelena"), ("↓ preload → míň kyslíku", "modra")],
  karty=[
      ("MECHANISMUS", [
          "Donory oxidu dusnatého (NO)",
          "NO → guanylátcykláza → cGMP → uvolnění hladké svaloviny",
          "⚠️ Hlavně žilní řečiště → krev se „zaparkuje\" → ↓ předtížení",
          "⚠️ Sekundárně: dilatace věnčitých tepen a spazmolýza"], "zelena"),
      ("ZÁSTUPCI A FORMY", [
          "⚠️ Nitroglycerin sublingválně nebo sprej — ⚠️ NEPOLYKAT (first-pass)",
          "Isosorbid dinitrát a mononitrát (mononitrát first-pass nemá)",
          "Molsidomin",
          "Nitroglycerin i.v. u akutních stavů (plicní edém, akutní koronární syndrom)"], "modra"),
      ("⚠️ TOLERANCE", [
          "Při nepřetržité expozici účinek během dnů vymizí",
          "⚠️ Nutný denní NITRÁTOVÝ INTERVAL 8–12 hodin bez léku",
          "Obvykle přes noc; u nočních záchvatů se interval posune na den",
          "Náplast se na noc sundává"], "cervena"),
      ("⚠️ NÚ A ABSOLUTNÍ KONTRAINDIKACE", [
          "Bolest hlavy (ustoupí za pár dní), návaly, hypotenze, reflexní tachykardie",
          "⚠️ ABSOLUTNÍ KI: inhibitory fosfodiesterázy 5 (sildenafil, tadalafil)",
          "→ obojí zvyšuje cGMP, sečte se to a tlak spadne nezvratně",
          "⚠️ Na tohle je nutné se aktivně ptát",
          "⚠️ Nitráty jsou čistě symptomatické — prognózu nezlepšují"], "cervena"),
  ],
  mnemo="Žíly, ne tepny. Preload dolů, spotřeba kyslíku dolů.",
  zubar="⚠️ Pacient s anginou pectoris má mít svůj nitroglycerinový sprej v ordinaci "
        "u sebe. Při záchvatu: nechat SEDĚT (ne stoupnout — hrozí kolaps), dávka pod jazyk, "
        "po 5 minutách lze opakovat; ⚠️ nezabere-li do 15 minut, podezření na infarkt.",
  past="Pacienti nitroglycerin často polykají — tím ho zničí first-pass efekt "
       "a lék nezabere.")

S("72", "Farmakoterapie srdečního selhání",
  jadro="Rozlišuj léky, které pacientovi uleví, od léků, které mu prodlouží život. "
        "Nejsou to tytéž léky.",
  karty=[
      ("⭐ ČTYŘI PILÍŘE (prodlužují život)", [
          "1) ACE inhibitor / sartan → dnes nejlépe ARNI (sakubitril + valsartan)",
          "2) ⚠️ BETABLOKÁTOR — jen bisoprolol, metoprolol ZOK, karvedilol, nebivolol",
          "3) Antagonista aldosteronu — spironolakton, eplerenon",
          "4) ⚠️ GLIFLOZIN — dapagliflozin, empagliflozin (⚠️ i u nediabetika)"], "zelena"),
      ("JEN ÚLEVA (prognózu nemění)", [
          "Diuretika — furosemid; ⚠️ i.v. působí nejdřív žilní dilatací",
          "Digoxin — ⚠️ u fibrilace síní s rychlou odpovědí",
          "Ivabradin — snižuje hospitalizace, blokuje kanál If",
          "⚠️ Nitráty, hydralazin (u vybraných pacientů)"], "modra"),
      ("⚠️ PROČ TLUMÍME SRDCE, KTERÉ NESTAČÍ", [
          "Chronická aktivace sympatiku a RAAS je zpočátku záchrana,",
          "⚠️ ale dlouhodobě myokard přestavuje a ničí (remodelace)",
          "→ léčba odstraňuje tu NADMĚRNOU PODPORU",
          "⚠️ Proto se betablokátor nasazuje nízko a titruje týdny",
          "a stav se může na začátku přechodně zhoršit"], "cervena"),
      ("⚠️ CO NEDÁVAT", [
          "⚠️ NSA — retence sodíku, zhoršení funkce ledvin",
          "⚠️ Verapamil a diltiazem — negativně inotropní",
          "⚠️ Glitazony (pioglitazon) — retence tekutin",
          "⚠️ Antiarytmika třídy IC"], "cervena"),
  ],
  mnemo="Čtyři pilíře prodlužují život. Diuretikum a digoxin jen ulevují.",
  zubar="⚠️ Pacient se srdečním selháním: krátká sezení, poloha vpolosedě (vleže se "
        "hůř dýchá), ⚠️ NSA po výkonu nedávat — volit paracetamol.",
  past="Gliflozin u srdečního selhání funguje i u pacienta bez diabetu — jeho přínos "
       "nesouvisí s glykemií. [⚠️ ověřit rozsah, který chtějí vaše skripta.]")

S("73", "Farmakoterapie ischemické choroby srdeční",
  jadro="Ischemie = nepoměr mezi nabídkou a spotřebou kyslíku v myokardu. "
        "U chronické formy rozlišuj prognostickou a úlevovou léčbu.",
  karty=[
      ("⭐ ZLEPŠUJÍ PROGNÓZU", [
          "Antiagregancia — aspirin, případně klopidogrel",
          "Statin ve vysoké dávce — ⚠️ i při normálním cholesterolu (stabilizace plátu)",
          "ACE inhibitor",
          "Betablokátor"], "zelena"),
      ("JEN ULEVÍ OD ANGÍNY", [
          "Nitráty (⚠️ s nitrátovým intervalem)",
          "Ivabradin — ⚠️ zpomalí tep bez vlivu na stažlivost a tlak",
          "Trimetazidin, ranolazin — metabolická léčba",
          "Blokátory kalciových kanálů (⚠️ volba u vazospastické anginy)"], "modra"),
      ("⚠️ AKUTNÍ KORONÁRNÍ SYNDROM", [
          "⚠️ Rozhoduje ČAS a otevření tepny (perkutánní koronární intervence)",
          "Farmakoterapie ji doprovází: aspirin + inhibitor P2Y12 (tikagrelor, prasugrel)",
          "+ antikoagulancium + morfin + kyslík při desaturaci",
          "+ nitrát + betablokátor + statin ve vysoké dávce",
          "⚠️ Trombolýza jen tam, kde není dostupná katetrizace"], "cervena"),
      ("⚠️ DUÁLNÍ ANTIAGREGACE", [
          "Po zavedení stentu obvykle 12 měsíců",
          "⚠️ Předčasné vysazení = trombóza stentu = infarkt",
          "⚠️ Plánovanou extrakci v téhle době raději odložit",
          "⚠️ Nikdy nevysazovat svévolně — vždy s kardiologem"], "cervena"),
  ],
  mnemo="Betablokátor zpomalí tep → prodlouží diastolu → věnčité tepny se plní právě v diastole.",
  zubar="⚠️ Pacient po infarktu: elektivní výkony odložit alespoň o 6 měsíců (⚠️ ověřit "
        "dle doporučení), krátká sezení, stres minimalizovat, ⚠️ nitroglycerin po ruce, "
        "⚠️ duální antiagregaci nevysazovat.",
  past="Statin se nedává „na cholesterol\", ale na stabilizaci plátu — proto se "
       "podává i pacientům s normální hodnotou.")

S("74", "Antihypertenziva",
  jadro="Hypertenze se neléčí podle čísla, ale podle toho, kdo ji má — a raději "
        "kombinací nízkých dávek než jedním lékem v maximu.",
  karty=[
      ("PĚT ZÁKLADNÍCH TŘÍD", [
          "ACE inhibitory a sartany",
          "Blokátory kalciových kanálů (dihydropyridiny)",
          "Thiazidová diuretika",
          "Betablokátory (⚠️ dnes hlavně při další indikaci)",
          "⚠️ Spironolakton u rezistentní hypertenze"], "zelena"),
      ("⚠️ VOLBA PODLE PACIENTA", [
          "Diabetik nebo proteinurie → ACE inhibitor / sartan",
          "Po infarktu → betablokátor + ACE inhibitor",
          "Srdeční selhání → čtyři pilíře",
          "Senior, izolovaná systolická hypertenze → blokátor Ca nebo thiazid",
          "⚠️ Dna → NE thiazid · ⚠️ Astma → NE betablokátor"], "modra"),
      ("DALŠÍ SKUPINY", [
          "Centrální α2 agonisté: methyldopa, klonidin (⚠️ rebound po vysazení)",
          "α1-blokátory: doxazosin (⚠️ vhodné s hyperplazií prostaty)",
          "Přímé vazodilatátory: hydralazin, minoxidil",
          "Urapidil (i.v. v akutních stavech)"], "bila"),
      ("⚠️ GRAVIDITA A KRIZE", [
          "⚠️ GRAVIDITA: methyldopa, labetalol, nifedipin (akutně urapidil)",
          "⚠️ ABSOLUTNĚ KONTRAINDIKOVÁNY: ACE inhibitory a sartany",
          "⚠️ Hypertenzní krize se nesmí srážet příliš rychle — ischemie mozku a ledvin",
          "Rezistentní hypertenze: nejdřív vyloučit nespolupráci a sekundární příčinu",
          "⚠️ Nejčastější sekundární příčina: primární hyperaldosteronismus"], "cervena"),
  ],
  mnemo="Fixní kombinace v jedné tabletě — hypertenze nebolí a čím víc tablet, tím víc vynechaných.",
  zubar="⚠️ Před výkonem změř tlak. Nekontrolovaná hypertenze je důvod odložit elektivní "
        "výkon. ⚠️ NSA po výkonu zvyšují tlak a ruší účinek antihypertenziv.",
  past="Léky samy mohou hypertenzi způsobit: ⚠️ NSA, kortikoidy, hormonální "
       "antikoncepce, sympatomimetika v nosních kapkách.")

S("75", "Farmakoterapie aterosklerózy, hyperlipidemie",
  jadro="Statin nesnižuje jen číslo v odběru — stabilizuje plát, který by jinak praskl. "
        "A infarkt způsobí prasklý plát, ne hodnota cholesterolu.",
  tok=[("STATIN blokuje HMG-CoA reduktázu", "zelena"), ("játra vyrobí míň cholesterolu", "bila"),
       ("nahustí si LDL receptory", "bila"), ("vytáhnou LDL z krve", "zelena")],
  karty=[
      ("STATINY", [
          "Atorvastatin, rosuvastatin, simvastatin, fluvastatin",
          "⚠️ NÚ: svalové potíže — od myalgie po ⚠️ RABDOMYOLÝZU",
          "(příznak: bolest svalů + tmavá moč + vysoká kreatinkináza)",
          "Zvýšení jaterních testů, mírné zvýšení rizika diabetu",
          "⚠️ Pleiotropní efekt — protizánětlivý, stabilizace plátu"], "zelena"),
      ("⚠️ INTERAKCE STATINŮ", [
          "⚠️ Riziko myopatie roste s inhibitory CYP3A4:",
          "⚠️ makrolidy (klarithromycin), azolová antimykotika, verapamil,",
          "cyklosporin, ⚠️ GRAPEFRUIT",
          "⚠️ Kombinace s fibrátem (zvl. gemfibrozilem)",
          "→ u pacienta na statinu volit azithromycin, ne klarithromycin"], "cervena"),
      ("DALŠÍ HYPOLIPIDEMIKA", [
          "Ezetimib — blokuje vstřebávání cholesterolu (přenašeč NPC1L1)",
          "⚠️ Inhibitory PCSK9 (evolokumab, alirokumab) — injekční protilátky,",
          "velmi silný efekt, rodinná hypercholesterolemie",
          "Fibráty (fenofibrát) — ⚠️ hlavně na triacylglyceroly",
          "Pryskyřice (cholestyramin), kyselina nikotinová, omega-3"], "modra"),
      ("PRAKTICKY", [
          "⚠️ Cíl LDL se posouvá podle rizika — po infarktu velmi nízko",
          "Statiny s krátkým poločasem večer, atorvastatin a rosuvastatin kdykoli",
          "⚠️ Fibrát u výrazně zvýšených triacylglycerolů (riziko pankreatitidy)",
          "Základem zůstává strava, pohyb a nekouření"], "bila"),
  ],
  mnemo="Statin stabilizuje plát. Číslo v odběru je jen ukazatel.",
  zubar="⚠️ Než předepíšeš makrolid nebo azolové antimykotikum pacientovi na statinu, "
        "zvaž azithromycin — klarithromycin může vyvolat rabdomyolýzu.",
  past="Bolest svalů u pacienta na statinu se nemá bagatelizovat — může jít o "
       "začínající rabdomyolýzu s rizikem selhání ledvin.")

S("76", "Parenterální antikoagulancia",
  jadro="Heparin sám nedělá nic — funguje jen díky tomu, že tisíckrát zesílí "
        "přirozený antitrombin III.",
  tok=[("ANTITROMBIN III přirozená, ale pomalá brzda", "bila"),
       ("+ HEPARIN", "zelena"), ("⚠️ zrychlí ji asi 1000×", "zelena"),
       ("inhibice IIa a Xa", "modra")],
  karty=[
      ("TŘI TYPY", [
          "NEFRAKCIONOVANÝ — dlouhý řetězec, ⚠️ inhibuje IIa i Xa",
          "⚠️ monitorace aPTT, ⚠️ antidotum PROTAMIN SULFÁT, krátký poločas",
          "NÍZKOMOLEKULÁRNÍ (enoxaparin, nadroparin) — ⚠️ hlavně Xa,",
          "s.c. 1–2× denně, bez rutinní monitorace (jen anti-Xa aktivita)",
          "FONDAPARINUX — syntetický pentasacharid, ⚠️ výhradně Xa, ⚠️ nedělá HIT"], "zelena"),
      ("⚠️ HIT — heparinem indukovaná trombocytopenie", [
          "Protilátky proti komplexu heparinu a destičkového faktoru 4",
          "⚠️ Destičky se nejen ubírají, ale ZÁROVEŇ AKTIVUJÍ",
          "→ ⚠️ pacient má málo destiček A PŘITOM TROMBÓZY",
          "⚠️ Léčba: okamžitě vysadit heparin, nasadit argatroban/bivalirudin/fondaparinux",
          "⚠️ NIKDY nepodávat destičky"], "cervena"),
      ("INDIKACE", [
          "Prevence a léčba žilní trombózy a plicní embolie",
          "Akutní koronární syndrom, katetrizace, dialýza",
          "⚠️ GRAVIDITA — hepariny NEPROCHÁZEJÍ PLACENTOU → antikoagulancium volby",
          "Přímé inhibitory trombinu: bivalirudin, argatroban"], "modra"),
      ("PRAKTICKÉ POZNÁMKY", [
          "⚠️ Protamin zruší nefrakcionovaný heparin úplně, nízkomolekulární jen částečně",
          "⚠️ Heparin nefunguje u vrozeného deficitu antitrombinu — nemá co zesílit",
          "⚠️ Nefrakcionovaný raději u těžkého selhání ledvin a před operací",
          "NÚ: krvácení, ⚠️ osteoporóza při dlouhodobém podávání, hyperkalemie"], "bila"),
  ],
  mnemo="Heparin je zesilovač antitrombinu. Bez něj neumí nic.",
  zubar="Pacient na nízkomolekulárním heparinu je „přemostěný\" před operací — "
        "⚠️ termín extrakce se domlouvá s ošetřujícím lékařem, obvykle s vynecháním "
        "ranní dávky v den výkonu. [⚠️ ověřit dle doporučení.]",
  past="HIT je paradox: méně destiček, a přesto trombózy. Podání destiček by stav zhoršilo.")

S("77", "Perorální antikoagulancia",
  jadro="Warfarin blokuje i přirozené brzdy srážení — a proto první dny paradoxně "
        "zvyšuje srážlivost.",
  tok=[("WARFARIN nasazen", "zelena"), ("⚠️ nejdřív klesne PROTEIN C", "cervena"),
       ("⚠️ pacient je přechodně protrombogenní", "cervena"),
       ("⚠️ proto PŘEKRYTÍ HEPARINEM", "zelena")],
  karty=[
      ("WARFARIN", [
          "Antagonista vitaminu K → blokuje γ-karboxylaci faktorů 🔑 II, VII, IX, X („1972\")",
          "⚠️ Ale i přirozených brzd — proteinu C a S",
          "⚠️ Nástup 3–5 dní, monitorace INR (obvykle 2–3)",
          "⚠️ Antidotum: vitamin K, plazma, koncentrát protrombinového komplexu",
          "⚠️ TERATOGEN — v graviditě nízkomolekulární heparin"], "zelena"),
      ("⚠️ INTERAKCE WARFARINU", [
          "Vitamin K v listové zelenině — ⚠️ zásada není nejíst ji, ale jíst ji POŘÁD STEJNĚ",
          "⚠️ Antibiotika — zlikvidují střevní bakterie, které vitamin K vyrábějí",
          "Amiodaron, azolová antimykotika, metronidazol → zvýší INR",
          "⚠️ Rifampicin, karbamazepin, třezalka → sníží INR",
          "⚠️ NSA a aspirin → krvácení i bez změny INR"], "cervena"),
      ("DOAC", [
          "⚠️ Dabigatran — přímý inhibitor trombinu; antidotum IDARUCIZUMAB",
          "🔑 -xaban blokuje Xa: rivaroxaban, apixaban, edoxaban",
          "antidotum andexanet alfa",
          "+ fixní dávka, bez odběrů, méně interakcí, méně krvácení do mozku",
          "⚠️ − Nesmí u MECHANICKÉ CHLOPNĚ a u těžké renální insuficience"], "modra"),
      ("⚠️ ZUBAŘSKÝ POSTUP", [
          "⚠️ Před běžnou extrakcí se warfarin NEVYSAZUJE, je-li INR v rozmezí",
          "(zhruba do 3–3,5) — riziko trombózy je větší než riziko krvácení",
          "⚠️ Řeší se místně: šití, oxidovaná celulóza, kolagenová houbička,",
          "výplach kyselinou tranexamovou, skus na tampon",
          "⚠️ [⚠️ ověřit přesnou hranici INR podle vašich skript]"], "cervena"),
  ],
  mnemo="1972 = faktory II, VII, IX, X. Protein C padá první.",
  zubar="⚠️ Nejčastější praktická otázka: warfarin ani DOAC se před běžnou extrakcí "
        "svévolně nevysazují. Ověř INR v den výkonu, výkon plánuj dopoledne a ošetři "
        "lůžko místní hemostázou.",
  past="Kumarinová nekróza kůže je vzácná komplikace prvních dní léčby — právě "
       "z předčasného poklesu proteinu C.")

S("78", "Fibrinolytika, trombolytika, hemostatika",
  jadro="Dvě protilehlé poloviny jedné otázky: trombolytika sraženinu rozpouštějí, "
        "hemostatika krvácení zastavují.",
  karty=[
      ("TROMBOLYTIKA", [
          "Alteplasa, tenektaplasa (rekombinantní), streptokináza, urokináza",
          "Aktivují plazminogen → plazmin → rozpouští fibrin",
          "⚠️ Indikace: STEMI (kde není katetrizace), masivní plicní embolie,",
          "⚠️ ischemická cévní mozková příhoda DO 4,5 HODINY",
          "⚠️ Streptokináza se nesmí podat podruhé — protilátky (je to bakteriální bílkovina)"], "zelena"),
      ("⚠️ KONTRAINDIKACE TROMBOLÝZY", [
          "Aktivní krvácení, krvácení do mozku v anamnéze",
          "Nedávná operace, úraz nebo punkce velkých cév",
          "Nekontrolovaná hypertenze",
          "Disekce aorty, nádor CNS, těžká trombocytopenie"], "cervena"),
      ("HEMOSTATIKA", [
          "Vitamin K — u warfarinu",
          "⚠️ KYSELINA TRANEXAMOVÁ — antifibrinolytikum (blokuje vazbu plazminogenu)",
          "⚠️ DESMOPRESIN — vyplaví z endotelu vWF a faktor VIII",
          "→ mírná hemofilie A a von Willebrandova choroba",
          "Etamsylát, koncentráty faktorů, rekombinantní faktor VIIa"], "modra"),
      ("⚠️ MÍSTNÍ HEMOSTÁZA — zubařský arzenál", [
          "Oxidovaná celulóza, kolagenová houbička",
          "Fibrinové lepidlo, šití, skus na tampon",
          "⚠️ Výplach nebo obklad kyselinou tranexamovou",
          "⚠️ Chyba ve zdroji: hemofilie A je VROZENÝ dědičný defekt faktoru VIII",
          "vázaný na chromozom X, ne „získaná geneticky\""], "cervena"),
  ],
  mnemo="Plazmin rozpouští. Tranexamová kyselina mu v tom brání.",
  zubar="⚠️ Extrakce u hemofilika se domlouvá PŘEDEM s hematologem: substituce faktoru "
        "nebo desmopresin + kyselina tranexamová + pečlivá lokální hemostáza. "
        "⚠️ Nikdy NSA na bolest — volit paracetamol.",
  past="Kyselina tranexamová je kontraindikovaná u aktivní trombózy — zabránila by "
       "rozpouštění sraženiny tam, kde je to potřeba.")

S("79", "Antiagregancia",
  jadro="V tepně se sraženina tvoří hlavně z destiček, v žíle z fibrinu. Proto se "
        "na ně dávají úplně jiné léky.",
  tok=[("⚠️ TEPNA rychlý proud", "cervena"), ("sraženina z DESTIČEK", "bila"),
       ("→ ANTIAGREGANCIA", "zelena"), ("(žíla → antikoagulancia)", "modra")],
  karty=[
      ("KYSELINA ACETYLSALICYLOVÁ", [
          "75–100 mg denně",
          "⚠️ Ireverzibilně ACETYLUJE COX-1 v destičce",
          "⚠️ Destička nemá jádro → enzym si nevyrobí → účinek 7–10 dní",
          "⚠️ Nízká dávka zasáhne hlavně destičkovou COX-1 už při průchodu játry;",
          "vyšší dávka by potlačila i ochranný prostacyklin a efekt zhoršila"], "zelena"),
      ("INHIBITORY P2Y12", [
          "Blokáda receptoru pro ADP",
          "⚠️ KLOPIDOGREL — proléčivo aktivované CYP2C19",
          "→ pomalí metabolizátoři nemají užitek; ⚠️ omeprazol jeho účinek snižuje",
          "⚠️ Prasugrel a tikagrelor — silnější; tikagrelor je reverzibilní a není proléčivo"], "modra"),
      ("DALŠÍ", [
          "⚠️ Inhibitory GPIIb/IIIa (abciximab, eptifibatid) — nejsilnější,",
          "blokují poslední společný krok agregace; jen i.v. v katetrizační laboratoři",
          "Dipyridamol (s aspirinem po cévní mozkové příhodě)",
          "Cilostazol (ischemická choroba dolních končetin)"], "bila"),
      ("⚠️ ZUBAŘSKY", [
          "⚠️ Aspirin se PŘED EXTRAKCÍ NEVYSAZUJE",
          "→ krvácení je mírné a zvládne ho místní ošetření,",
          "vysazení naopak znamená riziko infarktu",
          "⚠️ Duální antiagregace po stentu: výkon domluvit s kardiologem,",
          "ale léky se svévolně nevysazují"], "cervena"),
  ],
  mnemo="Tepna = destičky. Žíla = fibrin.",
  zubar="⚠️ Po extrakci u pacienta na antiagregaci: šetrná technika, šití, oxidovaná "
        "celulóza, tranexamová kyselina, poučení a kontrola. ⚠️ Analgezie paracetamolem, "
        "ne NSA.",
  past="Ibuprofen ruší antiagregační účinek aspirinu — obsadí COX-1 dřív a aspirin "
       "nemá co acetylovat. Aspirin se podává 2 hodiny předem.")

S("80", "Inzulin, jeho analoga a glukagon",
  jadro="Cílem je napodobit fyziologii: stálou bazální hladinu a vzestup k jídlu. "
        "Tomu se říká režim bazál-bolus.",
  tok=[("RYCHLÁ ANALOGA ~15 min → k jídlu", "zelena"), ("KRÁTKÝ HUMÁNNÍ ~30 min", "bila"),
       ("STŘEDNÍ NPH", "bila"), ("DLOUHÁ ANALOGA bez vrcholu → bazál", "zelena")],
  karty=[
      ("TYPY INZULINŮ", [
          "Rychlá analoga: lispro, aspart, glulisin — k jídlu",
          "Krátký humánní (regular) — ⚠️ píchat s předstihem 30 min",
          "Střední: NPH",
          "⚠️ Dlouhá analoga: glargin, detemir, degludek — bez vrcholu, bazál",
          "Premixované směsi"], "zelena"),
      ("⚠️ HYPOGLYKEMIE", [
          "⚠️ Hlavní nebezpečí veškeré inzulinoterapie",
          "Příznaky: pocení, třes, bušení srdce, hlad → zmatenost → bezvědomí, křeče",
          "⚠️ Betablokátor maskuje třes a palpitace (sympatikus),",
          "⚠️ ale POCENÍ zůstane (cholinergní) a bývá jediným varováním",
          "Léčba: cukr ústy; při bezvědomí glukóza i.v. nebo glukagon i.m."], "cervena"),
      ("GLUKAGON", [
          "i.m., s.c. nebo nosním sprejem",
          "⚠️ Při hypoglykemii u pacienta v bezvědomí, kterému nelze nic dát ústy",
          "⚠️ Zajímavost, na kterou se ptají: glukagon je ANTIDOTUM PŘEDÁVKOVÁNÍ",
          "BETABLOKÁTORY — zvedne v srdci cAMP jinou cestou, mimo beta-receptor"], "modra"),
      ("PRAKTICKY", [
          "⚠️ Střídat místa vpichu — jinak LIPODYSTROFIE a nepředvídatelné vstřebávání",
          "Somogyiho fenomén (ranní hyperglykemie po noční hypoglykemii)",
          "× dawn fenomén (fyziologický ranní vzestup hormonů) — ⚠️ řeší se opačně",
          "NÚ: přírůstek hmotnosti, otoky na začátku léčby"], "bila"),
  ],
  mnemo="Bazál drží hladinu mezi jídly. Bolus pokrývá jídlo.",
  zubar="⚠️ Diabetika objednávej dopoledne, po jídle a po obvyklé dávce; nenechávej "
        "ho hladovět. Měj po ruce cukr. ⚠️ Diabetik se hůř hojí a má vyšší riziko "
        "parodontitidy a kandidózy.",
  past="Pocení je jediný příznak hypoglykemie, který betablokátor nezamaskuje — "
       "je zprostředkovaný cholinergně.")

S("81", "Perorální antidiabetika",
  jadro="Nejpraktičtější rozdělení: které dělají hypoglykemii a které ne. "
        "A dnes se navíc vybírá podle ochrany srdce a ledvin.",
  karty=[
      ("⭐ METFORMIN — lék první volby", [
          "Snižuje tvorbu glukózy v játrech, zvyšuje citlivost k inzulinu",
          "⚠️ SÁM HYPOGLYKEMII NEZPŮSOBUJE — nenutí slinivku vylučovat inzulin",
          "⚠️ Riziko laktátové acidózy → vysadit před jodovou kontrastní látkou",
          "a při akutním stavu (dehydratace, sepse, selhání ledvin)",
          "⚠️ Dlouhodobě: deficit vitaminu B12; NÚ: průjem, kovová chuť"], "zelena"),
      ("⚠️ DĚLAJÍ HYPOGLYKEMII", [
          "⚠️ SULFONYLUREA — glimepirid, gliklazid",
          "→ uzavře KATP kanál v beta-buňce → vyplaví inzulin BEZ OHLEDU na glykemii",
          "⚠️ Může způsobit těžkou a dlouhou hypoglykemii, zvlášť u seniora",
          "⚠️ Přírůstek hmotnosti",
          "Glinidy (repaglinid) — podobně, ale krátce"], "cervena"),
      ("MODERNÍ SKUPINY", [
          "Gliptiny (sitagliptin) — inhibitory DPP-4, neutrální, bez hypoglykemie",
          "⚠️ GLP-1 AGONISTÉ (liraglutid, semaglutid) — hubnutí + ochrana srdce,",
          "injekčně; ⚠️ zpomalují vyprazdňování žaludku",
          "⚠️ GLIFLOZINY (dapagliflozin, empagliflozin) — ochrana srdce a ledvin,",
          "⚠️ glykosurie → genitální mykózy, ⚠️ euglykemická ketoacidóza"], "modra"),
      ("OSTATNÍ", [
          "Glitazony (pioglitazon) — ⚠️ retence tekutin, srdeční selhání, zlomeniny",
          "Akarbóza — zpomalí štěpení cukrů ve střevě, nadýmání",
          "⚠️ Volba dnes: podle komorbidit, ne jen podle glykemie",
          "Základem zůstává režim, strava a pohyb"], "bila"),
  ],
  mnemo="Sulfonylurea vyplaví inzulin bez ohledu na cukr — proto jako jediná z tabletek dělá hypoglykemii.",
  zubar="⚠️ Glifloziny způsobují glykosurii → vyšší riziko mykotických infekcí, "
        "včetně ústní kandidózy u pacienta s protézou. ⚠️ Pacient na GLP-1 agonistovi "
        "má zpomalené vyprazdňování žaludku — důležité před sedací.",
  past="Metformin se nevysazuje „preventivně\" u každého výkonu — jen před podáním "
       "kontrastní látky a při akutním stavu.")

S("82", "Principy antibiotické terapie",
  jadro="Celá antibiotická léčba stojí na selektivní toxicitě: zasáhnout strukturu, "
        "kterou má bakterie a člověk ne.",
  karty=[
      ("CÍLE V BAKTERIÁLNÍ BUŇCE", [
          "⚠️ BUNĚČNÁ STĚNA (peptidoglykan) — člověk ji nemá:",
          "betalaktamy, glykopeptidy",
          "MEMBRÁNA — polymyxiny, daptomycin",
          "⚠️ RIBOZOM 70S (30S + 50S) — lidský je 80S:",
          "30S aminoglykosidy, tetracykliny · 50S makrolidy, klindamycin, amfenikoly",
          "NUKLEOVÉ KYSELINY — chinolony (⚠️ topoizomeráza), rifampicin, metronidazol",
          "KYSELINA LISTOVÁ — sulfonamidy + trimethoprim"], "zelena"),
      ("ZÁKLADNÍ POJMY", [
          "Baktericidní × bakteriostatické",
          "Úzké × široké spektrum · empirická × cílená léčba",
          "MIC — minimální inhibiční koncentrace",
          "⚠️ Koncentračně závislé (aminoglykosidy, chinolony) → velká dávka 1× denně",
          "⚠️ Časově závislé (betalaktamy) → častěji, rozhoduje čas nad MIC",
          "Postantibiotický efekt"], "modra"),
      ("⚠️ REZISTENCE", [
          "⚠️ Betalaktamázy (i širokospektré ESBL, karbapenemázy)",
          "⚠️ Změna cílové struktury — MRSA má pozměněný PBP2a",
          "⚠️ Efluxní pumpy · snížená propustnost stěny",
          "Roste s používáním → ⚠️ antibiotická stewardship",
          "⚠️ Antibiotikum na virózu nemá cíl — přinese jen NÚ a rezistenci"], "cervena"),
      ("⚠️ PROFYLAXE INFEKČNÍ ENDOKARDITIDY", [
          "Jen u rizikových pacientů: umělá chlopeň, prodělaná endokarditida,",
          "některé vrozené vady",
          "Jen u výkonů s poraněním dásně nebo sliznice",
          "⚠️ AMOXICILIN 2 g jednorázově zhruba hodinu před výkonem",
          "⚠️ Při alergii KLINDAMYCIN",
          "⚠️ [⚠️ ověřit dávky a indikace podle vašich skript — měnily se]"], "cervena"),
  ],
  mnemo="Stěna · ribozom 70S · DNA · kyselina listová. Čtyři místa, kde se člověk liší.",
  zubar="⚠️ U odontogenního abscesu antibiotikum NENAHRADÍ drenáž a ošetření zdroje. "
        "Samo o sobě problém nevyřeší. ⚠️ Profylaxe endokarditidy se dnes dává mnohem "
        "úžeji než dřív.",
  past="Klasické pravidlo „nekombinovat baktericidní s bakteriostatickým\" má "
       "výjimky — v praxi existují i výhodné kombinace.")

S("83", "Peniciliny, inhibitory betalaktamáz",
  jadro="Blokují stavbu buněčné stěny — a proto působí jen na bakterie, které se "
        "právě dělí. Člověk stěnu nemá, takže hlavním rizikem je alergie, ne toxicita.",
  karty=[
      ("SKUPINY", [
          "Přirozené: penicilin G (i.v., i.m.), ⚠️ PENICILIN V (p.o.), depotní benzathin",
          "Protistafylokokové: oxacilin — odolné vůči stafylokokové betalaktamáze",
          "Aminopeniciliny: ampicilin, ⚠️ AMOXICILIN (širší spektrum, i některé G−)",
          "Ureidopeniciliny: piperacilin — ⚠️ + Pseudomonas"], "zelena"),
      ("INHIBITORY BETALAKTAMÁZ", [
          "Kyselina klavulanová, sulbaktam, tazobaktam",
          "⚠️ Samy skoro neúčinkují — „obětují se\" enzymu",
          "Amoxicilin + klavulanát; piperacilin + tazobaktam",
          "⚠️ Rozšíří spektrum na producenty betalaktamáz"], "modra"),
      ("⚠️ ALERGIE", [
          "Skutečná IgE zprostředkovaná alergie je vzácnější, než ji pacienti uvádějí",
          "⚠️ Zkřížená reaktivita s cefalosporiny je nižší, než se dřív myslelo,",
          "⚠️ ale u anafylaxe v anamnéze se betalaktamům vyhýbáme úplně",
          "→ náhrada: klindamycin nebo makrolid",
          "⚠️ AMPICILINOVÝ EXANTÉM u infekční mononukleózy NENÍ alergie"], "cervena"),
      ("DALŠÍ NÚ A POZNÁMKY", [
          "Průjem, ⚠️ infekce Clostridioides difficile",
          "⚠️ Jarischova–Herxheimerova reakce u syfilis (rozpad bakterií, ne alergie)",
          "Ve vysokých dávkách neurotoxicita a křeče",
          "⚠️ Penicilin V se podává nalačno (jídlo zhoršuje vstřebání)"], "bila"),
  ],
  mnemo="Bakterie se musí dělit, aby ji penicilin zabil. Klidná bakterie stěnu nestaví.",
  zubar="⚠️ PENICILIN V je lék volby u odontogenních infekcí — ústní flóra na něj "
        "zůstala citlivá. ⚠️ Amoxicilin s klavulanátem u komplikovaných infekcí "
        "a při podezření na producenty betalaktamáz.",
  past="Většina „alergií na penicilin\" v anamnéze není alergie — ale u anafylaxe "
       "se riskovat nesmí a volí se klindamycin.")

S("84", "Cefalosporiny, karbapenemy, monobaktamy",
  jadro="U cefalosporinů platí jedno pravidlo: čím vyšší generace, tím míň "
        "grampozitivních a víc gramnegativních.",
  tok=[("I. cefazolin G+", "bila"), ("II. cefuroxim", "bila"),
       ("III. ceftriaxon G− + CNS", "zelena"), ("IV.–V. cefepim, ceftarolin", "modra")],
  karty=[
      ("GENERACE CEFALOSPORINŮ", [
          "I. cefazolin, cefalexin — ⚠️ chirurgická profylaxe",
          "II. cefuroxim — + Haemophilus, respirační infekce",
          "III. ceftriaxon, cefotaxim — ⚠️ prostup do CNS → meningitidy;",
          "ceftazidim — + Pseudomonas",
          "IV. cefepim — široké, nemocniční · V. ceftarolin — ⚠️ jako jediné i na MRSA"], "zelena"),
      ("⚠️ MEZERY VE SPEKTRU", [
          "⚠️ ŽÁDNÝ cefalosporin nepůsobí na ENTEROKOKY",
          "⚠️ ANI na ATYPICKÉ patogeny (mykoplazma, chlamydie, legionella)",
          "→ u atypické pneumonie je nutný makrolid nebo doxycyklin",
          "Na anaeroby působí jen omezeně"], "cervena"),
      ("KARBAPENEMY", [
          "Meropenem, imipenem/cilastatin, ertapenem",
          "⚠️ Nejširší spektrum ze všech antibiotik → ⚠️ REZERVA",
          "⚠️ Imipenem musí být s cilastatinem (jinak ho rozloží ledvinný enzym)",
          "⚠️ Imipenem snižuje práh pro křeče · ⚠️ ertapenem nepůsobí na Pseudomonas",
          "⚠️ Dál už není kam ustoupit — proto se šetří"], "cervena"),
      ("MONOBAKTAMY a NÚ", [
          "Aztreonam — ⚠️ jen gramnegativní",
          "⚠️ Strukturálně tak odlišný, že ho lze podat i při alergii na penicilin",
          "NÚ betalaktamů obecně: alergie, průjem, ⚠️ C. difficile",
          "Vzácně: neutropenie, zvýšení jaterních testů"], "bila"),
  ],
  mnemo="Nahoru generacemi = od G+ ke G−. Enterokoky a atypické nikdy.",
  zubar="⚠️ Cefalosporiny se u odontogenních infekcí běžně nevolí — penicilin V, "
        "amoxicilin (± klavulanát) a klindamycin pokrývají ústní flóru lépe.",
  past="Karbapenem není „lepší antibiotikum\" pro každý případ — je to poslední "
       "rezerva a jeho nadužívání vytváří rezistenci, na kterou už nemáme odpověď.")

S("85", "Aminoglykosidy, chinolony",
  jadro="Obě skupiny jsou baktericidní a koncentračně závislé — a obě mají typickou "
        "orgánovou toxicitu, na kterou se ptají.",
  karty=[
      ("AMINOGLYKOSIDY", [
          "Gentamicin, amikacin, tobramycin, streptomycin",
          "⚠️ Blokují 30S ribozom, ale jsou BAKTERICIDNÍ — výjimka mezi inhibitory",
          "bílkovinné syntézy",
          "⚠️ Nevstřebávají se ze střeva → jen parenterálně",
          "⚠️ Nepůsobí na anaeroby (potřebují kyslíkem poháněný vstup do buňky)",
          "Synergie s betalaktamy — ty poruší stěnu a usnadní vstup"], "zelena"),
      ("⚠️ TOXICITA AMINOGLYKOSIDŮ", [
          "⚠️ NEFROTOXICITA — obvykle vratná",
          "⚠️ OTOTOXICITA — poškození sluchu a rovnováhy, často TRVALÉ",
          "→ proto se hlídají hladiny",
          "⚠️ Dávkování 1× denně: vysoký vrchol zabíjí líp a dlouhá pauza chrání ledvinu",
          "Neuromuskulární blokáda (opatrně s myorelaxancii)"], "cervena"),
      ("CHINOLONY", [
          "Ciprofloxacin, ofloxacin, levofloxacin, moxifloxacin",
          "⚠️ Blokují TOPOIZOMERÁZU II (DNA-GYRÁZU) a topoizomerázu IV",
          "⚠️ VE ZDROJI JE CHYBA: uvedena „DNA-polymeráza\" — to je špatně",
          "Široké spektrum, dobrá tkáňová penetrace, dobrá dostupnost p.o."], "cervena"),
      ("⚠️ NÚ CHINOLONŮ", [
          "⚠️ Zánět a RUPTURA ŠLACH (typicky Achillovy), zvl. u seniorů a s kortikoidy",
          "⚠️ KI u dětí a v graviditě — poškození chrupavek",
          "⚠️ Prodloužení QT, fotosenzitivita, neuropsychické projevy",
          "⚠️ CHELATACE s Ca, Mg, Fe → nezapíjet mlékem, nebrat s antacidy",
          "⚠️ Průjem po C. difficile"], "cervena"),
  ],
  mnemo="Aminoglykosid: ucho a ledvina. Chinolon: šlacha a chrupavka.",
  zubar="⚠️ Chinolony se v ústní oblasti volí spíš výjimečně — ústní flóra na ně "
        "není optimálně citlivá a rizika jsou významná.",
  past="Aminoglykosidy jsou baktericidní, i když blokují ribozom — to je výjimka "
       "z pravidla, že inhibitory proteosyntézy jsou bakteriostatické.")

S("86", "Linkosamidy, glykopeptidy, polymyxiny",
  jadro="Tři rezervní nebo úzce zaměřené skupiny. Pro zubní lékařství je z nich "
        "nejdůležitější klindamycin.",
  karty=[
      ("⭐ KLINDAMYCIN", [
          "⚠️ Blokuje 50S ribozom, bakteriostatický",
          "Grampozitivní koky a ⚠️ hlavně ANAEROBY",
          "⚠️ VÝBORNÝ PRŮNIK DO KOSTI",
          "→ ⚠️ odontogenní absces, osteomyelitida čelisti",
          "→ ⚠️ alternativa při alergii na penicilin (i profylaxe endokarditidy)"], "zelena"),
      ("⚠️ RIZIKO KLINDAMYCINU", [
          "⚠️ PSEUDOMEMBRANÓZNÍ KOLITIDA (Clostridioides difficile)",
          "→ historicky je s ní nejvíc spojován",
          "Obraz: vodnaté průjmy během léčby i po ní, křeče, horečka, leukocytóza",
          "⚠️ Léčba: vankomycin PERORÁLNĚ nebo fidaxomicin",
          "⚠️ Nepodávat léky tlumící střevní pohyb (loperamid)"], "cervena"),
      ("GLYKOPEPTIDY", [
          "Vankomycin, teikoplanin",
          "⚠️ Blokují stavbu stěny na JINÉM místě než betalaktamy → fungují i u betalaktamáz",
          "⚠️ Jen grampozitivní — ⚠️ lék volby u MRSA",
          "⚠️ Perorálně se nevstřebají → proto p.o. právě na klostridiovou kolitidu",
          "⚠️ „Red man syndrome\" při rychlé infuzi — histaminová reakce, NENÍ to alergie",
          "Nefro- a ototoxicita"], "modra"),
      ("POLYMYXINY", [
          "Kolistin, polymyxin B",
          "⚠️ Narušují cytoplazmatickou membránu jako detergent",
          "⚠️ Rezerva na multirezistentní gramnegativní bakterie",
          "⚠️ Výrazně nefrotoxické a neurotoxické"], "bila"),
  ],
  mnemo="Klindamycin do kosti a na anaeroby. A pozor na klostridium.",
  zubar="⚠️ Klindamycin je v zubním lékařství klíčové antibiotikum: absces v obličeji, "
        "osteomyelitida čelisti a náhrada při alergii na penicilin. ⚠️ Pacienta pouč, "
        "že při vodnatých průjmech má lék vysadit a ozvat se.",
  past="Vankomycin nepůsobí na gramnegativní bakterie — je to velká molekula a přes "
       "jejich zevní membránu se nedostane.")

S("87", "Tetracykliny, amfenikoly",
  jadro="Tetracykliny se vážou na vápník a ukládají se do rostoucí kosti a zubu — "
        "odtud nejznámější zubařský nežádoucí účinek celé farmakologie.",
  tok=[("TETRACYKLIN se váže na VÁPNÍK", "zelena"), ("ukládá se do zubu a kosti", "bila"),
       ("⚠️ ŠEDOHNĚDÉ ZBARVENÍ UVNITŘ", "cervena"), ("⚠️ NEDÁ SE VYBĚLIT", "cervena")],
  karty=[
      ("MECHANISMUS A SPEKTRUM", [
          "⚠️ Blokují 30S podjednotku RIBOZOMU, bakteriostatické",
          "⚠️ VE ZDROJI JE CHYBA: uvedena inhibice buněčné stěny — to je špatně",
          "(stěnu blokují betalaktamy a glykopeptidy)",
          "Široké spektrum, ⚠️ včetně atypických: chlamydie, mykoplazmata,",
          "borrelie (lymeská borelióza), rickettsie"], "cervena"),
      ("ZÁSTUPCI", [
          "⚠️ DOXYCYKLIN — dnes hlavní: lepší vstřebávání, delší poločas,",
          "méně ovlivněný jídlem, lze i při renální insuficienci",
          "Minocyklin, tetracyklin",
          "Tigecyklin (glycylcyklin) — rezervní, širokospektrý"], "zelena"),
      ("⚠️ NEŽÁDOUCÍ ÚČINKY", [
          "⚠️ Zbarvení zubů a hypoplazie skloviny — jen v době VÝVOJE zubu",
          "⚠️ KI do 8 let věku, v graviditě a při kojení",
          "⚠️ CHELATACE s Ca, Mg, Fe → nezapíjet mlékem, nebrat s antacidy",
          "⚠️ Fotosenzitivita · ezofagitida (zapít velkým množstvím vody, nelehat si)",
          "Rezistence je dnes rozsáhlá (i z veterinárního používání)"], "cervena"),
      ("AMFENIKOLY a PARODONTOLOGIE", [
          "Chloramfenikol — ⚠️ blokuje 50S ribozom",
          "⚠️ APLASTICKÁ ANEMIE — idiosynkratická, NEZÁVISLÁ NA DÁVCE, smrtelná",
          "⚠️ GRAY BABY SYNDROM u novorozence (nezralá glukuronidace)",
          "→ dnes systémově opuštěný, zůstal v očních kapkách a mastech",
          "⚠️ Nízkodávkovaný doxycyklin jako inhibitor kolagenáz v parodontologii",
          "[⚠️ ověřit, zda to vaše skripta uvádějí]"], "modra"),
  ],
  mnemo="Váže vápník → jde do zubu → barví zevnitř → vybělit nejde.",
  zubar="⚠️ Zbarvení je uvnitř skloviny a dentinu, ne na povrchu — proto ho nelze "
        "odstranit bělením ani leštěním. Řeší se jen protetickým krytím. "
        "⚠️ Dětem do 8 let se tetracykliny nedávají nikdy.",
  past="Aplastická anemie po chloramfenikolu je typ B — nezávisí na dávce a nedá se "
       "předvídat. Proto se lék systémově prakticky nepoužívá.")

S("88", "Makrolidy",
  jadro="Největší úskalí makrolidů nejsou nežádoucí účinky, ale lékové interakce — "
        "a azithromycin je v tom výjimka.",
  karty=[
      ("MECHANISMUS A SPEKTRUM", [
          "⚠️ Blokují 50S podjednotku ribozomu, bakteriostatické",
          "⚠️ Pokrývají ATYPICKÉ patogeny: mykoplazma, chlamydie, legionella, pertusse",
          "⚠️ Alternativa při alergii na penicilin",
          "Zástupci: erythromycin, klarithromycin, azithromycin, spiramycin"], "zelena"),
      ("⚠️ INTERAKCE — nejdůležitější část otázky", [
          "⚠️ ERYTHROMYCIN a KLARITHROMYCIN jsou SILNÉ INHIBITORY CYP3A4",
          "→ ⚠️ zvýší hladinu statinů (rabdomyolýza), warfarinu (krvácení),",
          "cyklosporinu, karbamazepinu, některých blokátorů Ca",
          "🔑 ⚠️ AZITHROMYCIN CYP3A4 prakticky NEINHIBUJE",
          "→ volba u polymorbidního pacienta"], "cervena"),
      ("AZITHROMYCIN — zvláštnost", [
          "⚠️ Velmi dlouhý tkáňový poločas",
          "Koncentruje se ve tkáních a v buňkách a uvolňuje se pomalu",
          "⚠️ Třídenní kúra působí ještě řadu dní po poslední tabletě",
          "Lepší snášenlivost než erythromycin"], "modra"),
      ("DALŠÍ NÚ", [
          "⚠️ Prodloužení QT — zvlášť s dalšími takovými léky",
          "(antipsychotika, chinolony, ondansetron, amiodaron)",
          "GIT nesnášenlivost — ⚠️ erythromycin dráždí přes MOTILINOVÝ receptor",
          "⚠️ A téhle vlastnosti se využívá: erythromycin jako prokinetikum u gastroparézy",
          "Vzácně hepatotoxicita, ototoxicita při vysokých dávkách"], "bila"),
  ],
  mnemo="Klarithromycin brzdí CYP. Azithromycin ne. To je celý rozdíl v praxi.",
  zubar="⚠️ Makrolid je alternativa při alergii na penicilin, ale u odontogenní infekce "
        "nebývá první volbou kvůli rezistenci — spíš klindamycin. ⚠️ Před předpisem "
        "klarithromycinu zkontroluj statin a warfarin.",
  past="Nežádoucí vlastnost erythromycinu (dráždění žaludku přes motilin) se využívá "
       "léčebně jako prokinetikum.")


# ═════════════════════════════════════ SPECKA II

S("89", "Chemoterapeutika močových a střevních infekcí",
  jadro="U močových infekcí stačí, když se lék dostane do MOČI — nemusí být dobrý "
        "v krvi. Proto se tu používají látky, které se jinde neuplatní.",
  tok=[("PABA", "bila"), ("dihydrofolát ⚠️ SULFONAMID", "cervena"),
       ("tetrahydrofolát ⚠️ TRIMETHOPRIM", "cervena"), ("DNA se nepostaví", "zelena")],
  karty=[
      ("KOTRIMOXAZOL — sekvenční blokáda", [
          "Sulfonamid je analog PABA → blokuje dihydropteroátsyntázu",
          "Trimethoprim → blokuje dihydrofolátreduktázu",
          "⚠️ Dva zámky za sebou na jedné dráze → účinek se násobí",
          "⚠️ Selektivita: člověk kyselinu listovou NEVYRÁBÍ, přijímá ji ze stravy",
          "Indikace: močové infekce, ⚠️ pneumocystová pneumonie (i profylakticky)"], "zelena"),
      ("⚠️ NÚ SULFONAMIDŮ", [
          "⚠️ Alergie a ⚠️ STEVENSŮV–JOHNSONŮV SYNDROM",
          "Krystalurie (dostatek tekutin), hyperkalemie, útlum krvetvorby",
          "⚠️ JÁDROVÝ IKTERUS u novorozence — sulfonamid vytěsní bilirubin z albuminu",
          "⚠️ Hemolýza při deficitu G6PD"], "cervena"),
      ("DALŠÍ UROANTISEPTIKA", [
          "⚠️ NITROFURANTOIN — koncentruje se v moči, ale ne ve tkáni",
          "→ ⚠️ jen dolní močové cesty, ne pyelonefritida",
          "⚠️ Dlouhodobě: plicní fibróza, neuropatie",
          "⚠️ FOSFOMYCIN — jednorázová dávka u nekomplikované cystitidy",
          "Chinolony (⚠️ dnes už ne první volba u nekomplikované cystitidy)"], "modra"),
      ("STŘEVNÍ", [
          "⚠️ RIFAXIMIN — nevstřebává se ze střeva; cestovatelské průjmy,",
          "jaterní encefalopatie",
          "Nifuroxazid",
          "⚠️ Clostridioides difficile: VANKOMYCIN PERORÁLNĚ nebo fidaxomicin,",
          "metronidazol u lehkých forem"], "bila"),
  ],
  mnemo="Dva zámky na jedné dráze — proto se sulfonamid a trimethoprim kombinují.",
  zubar="⚠️ Sulfonamidy patří mezi častější příčiny lékových exantémů a Stevensova–"
        "Johnsonova syndromu, který má výrazné slizniční projevy v dutině ústní.",
  past="Nitrofurantoin u pyelonefritidy nefunguje — v ledvinné tkáni nedosáhne "
       "účinné hladiny, i když je moč plná léku.")

S("90", "Antiparazitika",
  jadro="Tři skupiny podle parazita. Pro zubní lékařství je z nich nejdůležitější "
        "metronidazol, protože pokrývá i anaerobní bakterie.",
  karty=[
      ("ANTIMALARIKA", [
          "⚠️ Artemisininové kombinace (ACT) — dnešní lék volby u P. falciparum",
          "Chlorochin (⚠️ rozsáhlá rezistence), meflochin (⚠️ neuropsychické NÚ),",
          "atovakvon/proguanil",
          "⚠️ PRIMACHIN — likviduje spící formy (hypnozoity) v játrech u P. vivax a ovale",
          "⚠️ Při deficitu G6PD způsobí hemolýzu → enzym se předem testuje"], "zelena"),
      ("ANTIHELMINTIKA", [
          "⚠️ Albendazol, mebendazol — blokují tvorbu mikrotubulů",
          "(roupi, škrkavky); ⚠️ u roupů léčit celou rodinu a dávku opakovat za 2 týdny",
          "Pyrantel",
          "Praziquantel — tasemnice, motolice",
          "Ivermektin — strongyloidóza, svrab"], "modra"),
      ("⭐ METRONIDAZOL", [
          "⚠️ Aktivuje se jen v ANAEROBNÍM prostředí (proto na aeroby nepůsobí)",
          "Amébóza, giardióza, trichomoniáza",
          "⚠️ A NAVÍC ANAEROBNÍ BAKTERIE",
          "⚠️ DISULFIRAMOVÁ REAKCE S ALKOHOLEM",
          "⚠️ Kovová chuť v ústech, tmavá moč, při dlouhém podávání neuropatie"], "zelena"),
      ("⚠️ ZUBAŘSKÉ POUŽITÍ METRONIDAZOLU", [
          "⚠️ Nekrotizující ulcerózní gingivitida",
          "⚠️ V kombinaci s amoxicilinem u agresivní parodontitidy",
          "→ pokryje anaeroby, které amoxicilin nezvládne",
          "⚠️ Pacienta poučit o zákazu alkoholu během léčby a pár dní po ní"], "cervena"),
  ],
  mnemo="Metronidazol funguje jen tam, kde není kyslík.",
  zubar="⚠️ Kombinace amoxicilin + metronidazol je klasické schéma u agresivní "
        "parodontitidy. ⚠️ Kovová chuť a suchost úst jsou časté a pacienta překvapí.",
  past="Metronidazol s alkoholem = disulfiramová reakce (nevolnost, zvracení, návaly). "
       "Pacienta je nutné poučit, ne to považovat za samozřejmé.")

S("91", "Antituberkulotika a antileprotika",
  jadro="U tuberkulózy platí dvě neměnná pravidla: nikdy monoterapie a nikdy krátce.",
  tok=[("2 měsíce H R Z E", "zelena"), ("4 měsíce H R", "zelena"),
       ("⚠️ celkem 6 měsíců", "modra")],
  karty=[
      ("PROČ KOMBINACE A DLOUHO", [
          "Mykobakterie se pomalu dělí",
          "⚠️ Sedí uvnitř makrofágů a v kaseózních ložiscích",
          "⚠️ Rychle si vytvoří rezistenci proti jednomu léku",
          "⚠️ Pacient se cítí dobře po pár týdnech → kontrolované podávání (DOT)",
          "Nedodržení = multirezistentní tuberkulóza"], "zelena"),
      ("H — IZONIAZID a R — RIFAMPICIN", [
          "IZONIAZID: ⚠️ hepatotoxicita, ⚠️ PERIFERNÍ NEUROPATIE",
          "→ ⚠️ prevence PYRIDOXINEM (vitamin B6)",
          "⚠️ Acetylace: pomalí metabolizátoři mají vyšší riziko obojího",
          "RIFAMPICIN: ⚠️ SILNÝ INDUKTOR CYP → selže antikoncepce, warfarin,",
          "antiretrovirotika, kortikoidy",
          "⚠️ Oranžová moč, slzy a pot — barví kontaktní čočky"], "cervena"),
      ("Z — PYRAZINAMID a E — ETHAMBUTOL", [
          "PYRAZINAMID: ⚠️ hyperurikemie (dna), hepatotoxicita",
          "ETHAMBUTOL: ⚠️ RETROBULBÁRNÍ NEURITIDA",
          "→ porucha barvocitu a zrakové ostrosti; nutné oční kontroly",
          "Streptomycin — historicky první účinné antituberkulotikum"], "cervena"),
      ("ANTILEPROTIKA", [
          "Dapson, klofazimin, rifampicin",
          "⚠️ Také vždy v kombinaci a velmi dlouho (měsíce až roky)",
          "⚠️ Dapson: hemolýza (zvl. při deficitu G6PD), methemoglobinemie",
          "Klofazimin: zbarvení kůže"], "modra"),
  ],
  mnemo="HRZE: játra, indukce, dna, oči. Každé písmeno má svoji toxicitu.",
  zubar="⚠️ Pacientka na rifampicinu musí být poučena o náhradní antikoncepci. "
        "⚠️ Aktivní plicní tuberkulóza je důvod odložit elektivní ošetření a zajistit "
        "ochranu personálu.",
  past="Rifampicin je nejsilnější induktor v běžné praxi — sníží hladinu prakticky "
       "všeho, co pacient bere.")
