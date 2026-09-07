# FARMAKOLOGIE — zbytek ke zkoušce (od otázky 23 do 136)

**Pro koho to je:** jsi u otázky 22, zítra zkouška. Tenhle soubor obsahuje **všech zbývajících 114 otázek** (O23–O35 obecná, 36–88 speciální I, 89–136 speciální II) zkrácených tak, aby se daly projet za jeden den — ale **ne osekaných na hesla**. U každé otázky najdeš:

- **O čem to je** — jedna věta lidsky, ať víš, o co v otázce jde, než se pustíš do detailů
- **Mechanismus** — proč to funguje (ne co si zapamatovat, ale co odvodit)
- **Zástupci** — konkrétní léky, které musí zaznít
- **Indikace / Kontraindikace / NÚ** — klinický rámec, na který se ptají jako druhé
- 🔑 věta k zapamatování · ⚠️ past, na kterou se chytají · ❓ na co se doptají

**Nic tu není potřeba dohledávat jinde** — zkratky a odborné pojmy jsou vysvětlené na místě, kde se poprvé objeví.

**Jak to projet za den:** čti otázku, pak zavři oči a zkus ji **nahlas** vysvětlit vlastními slovy (kdo to nedokáže vysvětlit, ten to neumí). Na druhé kolo večer čti jen 🔑, ⚠️ a ❓.

---

# ČÁST 1 — OBECNÁ FARMAKOLOGIE (dokončení, O23–O35)

## O23 · Dávka a účinek, terapeutický index, terapeutické rozmezí (okno), terapeutické riziko

**O čem to je:** čím vyšší dávka, tím silnější účinek — ale jen do určité míry. Otázka je o tom, jak se ten vztah **měří čísly** a jak se z něj pozná, **jestli je lék bezpečný**.

- **Křivka koncentrace–účinek (CRC)** — měří se síla účinku při rostoucí koncentraci (typicky in vitro na izolovaném orgánu). Tři věci, které z ní čteš:
  - **EC50** = koncentrace vyvolávající **polovinu maximálního účinku**; posouvá křivku po ose x a odráží hlavně **afinitu** (jak pevně se léčivo váže na receptor),
  - **Emax** = maximální dosažitelný účinek; odráží **vnitřní aktivitu** (plný agonista má Emax nejvyšší, parciální nižší),
  - **sklon střední části** — **strmý sklon = nebezpečný lék** (malá změna dávky = velká změna účinku → snadné předávkování), pozvolný sklon se dávkuje bezpečněji.
- **Kvantální (statistická) závislost** — nesleduje se síla účinku, ale **kolik jedinců** z populace zareaguje (vše nebo nic). Odráží **individuální vnímavost**: citlivější člověk zareaguje na nižší dávku. Rozložení má tvar **Gaussovy křivky**, kumulativně vyjde **sigmoidální (esovitá) křivka** s inflexí u ED50.
- **Tři hraniční dávky:** **ED50** = účinek u 50 % jedinců · **TD50** = toxický účinek u 50 % · **LD50** = usmrtí 50 % (jen preklinika, na zvířatech).
- **Terapeutický index TI = TD50 / ED50** — kolikrát je toxická dávka vyšší než účinná:

| TI | Význam |
|---|---|
| **≥ 10** | léčivo relativně **bezpečné** |
| **≥ 2,5** | použitelné **jen s monitorováním hladin (TDM)** — digoxin, lithium, warfarin, aminoglykosidy |
| **≤ 2** | vývoj se **zastavuje**, příliš nebezpečné |

- **Terapeutické okno (šíře) = TD50 − ED50** — pásmo koncentrací, kde lék už léčí, ale ještě netraví. Udržet koncentraci uvnitř okna je smysl **farmakokineticky řízené individualizace terapie (TDM)**. *Názorně na jednom léku: anxiolytikum v nízké dávce zbaví úzkosti, ve vyšší uspí, ve velmi vysoké utlumí dýchání.*
- **Dávkování:** **nasycovací dávka** urychlí dosažení okna (u léčiv s dlouhým poločasem), **udržovací dávka** pak nechá koncentraci kolísat uvnitř okna.
- **NNT (number needed to treat)** — kolik pacientů musíš léčit, aby se u jednoho projevil sledovaný efekt; výhoda proti TI je, že zohlední i závažnost nemoci (u smrtelné nemoci akceptuješ horší poměr).
- **Doplnění k receptorům:** **plný/parciální agonista** posouvá receptor do aktivní konformace (R\*) a zvedá účinek nad bazální úroveň · **inverzní agonista** stabilizuje neaktivní formu (R) a účinek **sníží pod** bazální úroveň · **neutrální antagonista** se váže na obě formy stejně, sám nic nedělá, jen blokuje ostatní.

🔑 **Čím vyšší terapeutický index, tím větší rezerva mezi dávkou, která léčí, a dávkou, která škodí.**

⚠️ Opakované podávání může odpověď zesílit i zeslabit (tolerance/senzitizace, viz O27); u psychotropních látek hrozí abúzus a **léková závislost**.

❓ *Co dělá inverzní agonista jinak než antagonista?* → Antagonista jen blokuje (bazální aktivitu nemění), inverzní agonista ji aktivně **sníží pod klidovou úroveň**.

---

## O24 · Vlivy působící na kinetiku a dynamiku léčiv

**O čem to je:** checklist všeho, co může změnit, jak lék zabere u konkrétního pacienta — proč stejná tableta u dvou lidí nedělá totéž.

- **Léková forma, cesta podání, velikost dávky** — určují rychlost a rozsah vstřebání (viz O5–O8).
- **Pohlaví** — ženy bývají **citlivější**, mají víc nežádoucích účinků; navíc menstruační cyklus, gravidita a laktace mění hormonální hladiny a tím i odpověď.
- **Věk** — **novorozenci a nedonošení**: nedovyvinutá **hematoencefalická bariéra** (léky snáz do CNS → větší riziko neurotoxicity), nezralé jaterní enzymy a nižší clearance. **Senioři**: snížená eliminace (ledviny i játra) → nižší dávky.
- **Tělesná hmotnost a povrch těla** — základ přepočtu dávky (u dětí a cytostatik zásadně podle povrchu, m²).
- **Psychika, prostředí, teplota, cirkadiánní rytmy** — mění vnímavost i farmakokinetiku (chronofarmakologie).
- **Interakce s jinými léčivy a s potravou** (viz O25).
- **Poruchy hemodynamiky** — snížený průtok krve v místě vstřebávání (GIT, sval) → **zpomalené a nespolehlivé vstřebání**. Proto se v šoku a urgentních stavech podává **i.v.** — nezávisle na prokrvení periferie.
- **Onemocnění ledvin** — ovlivní celé ADME, ne jen exkreci. Glomerulární filtrace se odhaduje ze **sérového kreatininu + věk, hmotnost, pohlaví**; podle výsledku se **upraví dávka nebo vymění lék**.
- **Onemocnění jater** — klesá jaterní clearance, ale hlavně: u léčiv s **vysokou jaterní extrakcí stoupá biologická dostupnost**, protože nemocná játra je při prvním průchodu nezachytí (viz O18).

🔑 **Děti a senioři = snížená/odlišná eliminace → nižší dávky. Jaterní selhání paradoxně ZVYŠUJE dostupnost léčiv s vysokým first-pass efektem.**

❓ *Co se stane s biologickou dostupností léčiva s vysokým first-pass efektem u cirhózy?* → **Stoupne** — méně se ho "ztratí" cestou přes játra, hrozí předávkování.

---

## O25 · Lékové interakce

**O čem to je:** jak jedna látka změní účinek druhé — dělí se podle **významu** (chtěná/nechtěná) a podle **místa**, kde se to stane.

**Interakce** = změna síly nebo trvání účinku léčiva vlivem jiné látky (jiný lék, volně prodejný přípravek, alkohol, potrava). Klinicky se projeví buď jako nežádoucí reakce (typ A–E, viz O29), nebo jako **selhání léčby = typ F (failure)**.

**Podle významu:**
- **Žádoucí** — **synergismus** (zesílení, např. kombinace cytostatik nebo antibiotik), nebo **antagonismus** (oslabení — podání antidota při otravě).
- **Nežádoucí** — vedou k toxicitě nebo k selhání léčby.

**Podle mechanismu:**
- **Farmaceutické (inkompatibility)** — chemická reakce **ještě před vstřebáním** (v infuzní lahvi nebo v žaludku). Typicky **tetracykliny + Ca²⁺/Mg²⁺/Al³⁺ z mléka a antacid** → nevstřebatelný chelátový komplex → antibiotikum nezabere.
- **Farmakokinetické** — na úrovni ADME, nejčastěji **biotransformace**:
  - **inhibice enzymu** (dvě léčiva soutěží o stejný CYP) → hladina druhého léku stoupá → toxicita,
  - **indukce enzymu** → hladina klesá → selhání léčby; typicky **benzopyreny z cigaretového kouře indukují CYP450**, dále rifampicin, karbamazepin, třezalka.
  - Významné jsou i interakce v **renální exkreci** (soutěž o tubulární sekreci, změna pH moči → jiná reabsorpce).
- **Farmakodynamické** — až na cíli (receptor, dráha za ním):
  - **kyselina acetylsalicylová** (nízká dávka antiagregační, vysoká antikoagulační) **zesiluje účinek warfarinu** → krvácení,
  - **vitamin K** účinek warfarinu naopak **ruší** (je jeho antidotum),
  - **grapefruitová šťáva** — flavonoidy a polyfenoly **inhibují CYP3A4** ve stěně střeva → prudce stoupne hladina statinů, BKK, imunosupresiv.

🔑 **Farmaceutická = ještě před vstřebáním (chemie v lahvičce/žaludku) · farmakokinetická = cestou tělem (ADME) · farmakodynamická = až na receptoru.**

❓ *Co znamená interakce typu F?* → **Failure — selhání léčby**, ne klasický nežádoucí účinek.

---

## O26 · Farmakogenetika, genetický polymorfismus

**O čem to je:** stejná dávka u dvou lidí zabere jinak, protože každý má jinak rychlé enzymy. Klinicky jedna z nejdůležitějších otázek — chtějí konkrétní příklady.

- **Mutace** = dědičná změna struktury DNA; u jednoho genu je se životem slučitelná jen **genová (bodová)** mutace — substituce, delece nebo inzerce nukleotidu.
  - **zárodečná** (ve vajíčku/spermii) — **dědí se**, testuje se z DNA leukocytů venózní krve,
  - **somatická** — vzniká během života, **nedědí se**; když zasáhne dráhy růstu a dělení, je **základem nádoru** — testuje se přímo z nádorové tkáně, protože rozhoduje o volbě cílené léčby.
- **Genetický polymorfismus** = jeden gen je v populaci zastoupen nejméně **dvěma fenotypy s frekvencí ≥ 1 %**. Nejlépe popsaný u izoenzymů **cytochromu P450**.

| Fenotyp | Podstata | Důsledek |
|---|---|---|
| **PM — pomalý metabolizátor** | homozygot pro alelu s nulovou/nízkou aktivitou | vysoká hladina, **zesílený a prodloužený účinek**; u **proléčiva naopak účinek chybí** (nevznikne aktivní metabolit) |
| **IM — intermediární** | heterozygot, jedna defektní alela | mezistupeň |
| **EM — extenzivní (rychlý)** | většina populace, normální gen | běžná eliminace |
| **UM — ultrarychlý** | duplikace/amplifikace genu | velmi rychlá eliminace → **subterapeutická hladina a selhání léčby**; u proléčiva naopak předávkování |

- **Zjišťuje se** genotypizací (PCR z krve) nebo fenotypizací (podá se testovací substrát a změří poměr metabolitu v moči/krvi).
- **SNPs (jednonukleotidové polymorfismy)** jsou velmi časté — mohou vést ke ztrátě syntézy proteinu, k syntéze abnormálního proteinu nebo ke změně rychlosti syntézy; s jedním z nich souvisí i **faktor V Leiden** (dědičná trombofilie, sklon ke srážení).

**Klinické příklady, které chtějí slyšet:**
- **CYP2D6** — tvoří jen ~2 % všech CYP, ale metabolizuje **20–30 % běžných léčiv**:
  - **PM** → kumulace: **kardiotoxicita tricyklických antidepresiv**, arytmie po antiarytmicích, těžká **bradykardie** při β-blokátorech, a hlavně **kodein netlumí bolest** (nevznikne z něj morfin),
  - **UM** → naopak **kumulace morfinu** z kodeinu — popsané otravy kojenců, jejichž matky kodein užívaly (rychle ho přemění na morfin, ten přejde do mléka).
- **CYP2C9** — ~30 % všech CYP, metabolizuje ~10 % léčiv (NSA, antiepileptika, antikoagulancia):
  - **S-warfarin** u variant \*2 a \*3 → nedostatečné odbourání účinnější formy → **předávkování a krvácení**,
  - **omeprazol** — PM sám o sobě neohrožen (široké terapeutické okno), ale soutěží o enzym a **sníží aktivaci klopidogrelu** → riziko trombózy,
  - **izoniazid** — pomalých metabolizátorů je až **60 % kavkazské populace** → vysoká hladina → **hepatotoxicita a periferní neuropatie** (proto se přidává pyridoxin, vit. B6),
  - **azathioprin** — PM → nadměrná imunosuprese a **útlum kostní dřeně**.

🔑 **PM u CYP2D6 → kodein nezabere (chybí aktivace na morfin). PM u CYP2C9 → warfarin se hromadí (krvácení).**

⚠️ U **proléčiv** je logika obrácená: pomalý metabolizátor má **méně** účinku, ne víc. Tohle je nejčastější chyták.

❓ *Jaký je rozdíl mezi zárodečnou a somatickou mutací?* → Zárodečná se dědí na potomky, somatická vzniká během života, nedědí se, ale může založit nádor.

---

## O27 · Tolerance, tachyfylaxe, rezistence

**O čem to je:** organismus (nebo bakterie či nádor) si na lék "zvykne" a přestane reagovat — typy se liší hlavně **rychlostí** a **mechanismem**.

- **Tachyfylaxe** — **rychlé (minuty)** vymizení účinku při opakovaném podání v krátkých intervalech, obnova je také rychlá. Příklad: **nepřímá sympatomimetika (efedrin)** vytěsňují noradrenalin ze zásobních váčků — jak zásoba dochází, účinek mizí.
- **Tolerance (návyk)** — **pomalý (dny až týdny)** pokles účinku při dlouhodobém podávání; nemusí postihnout všechny účinky látky stejně.
  - na **terapeutický** účinek je nežádoucí (nutno zvýšit dávku nebo vyměnit lék) — typicky **benzodiazepiny**, kde jde ruku v ruce se závislostí,
  - na **nežádoucí** účinek je vítaná — při léčbě astmatu **β2-agonisty** postupně mizí tremor, ale bronchodilatace zůstává.
- **Rezistence** — pokles účinku **antimikrobiálních a protinádorových** látek; není to vlastnost pacienta, ale mikroba/nádoru. U cytostatik je zásadní **sekundární (získaná) rezistence** — buňka si vypěstuje pumpu, která cytostatikum vyhání ven (P-glykoprotein).
- **Desenzitizace** — reakce na trvalou přítomnost agonisty, stejná koncentrace vyvolá menší účinek:
  - **hodiny až dny**: **down-regulace** — klesá počet receptorů, případně klesne afinita,
  - **minuty**: **internalizace** — komplex agonista–receptor se vtáhne endocytózou a odpojí od G-proteinu; po poklesu agonisty se receptor vrátí funkční zpět do membrány.
- **Senzitizace** — opak; po dlouhodobém **nedostatku ligandu** nebo **blokádě antagonistou** stoupá počet receptorů (**up-regulace**). Klinicky nejdůležitější: **dlouhodobá léčba β-blokátory** → up-regulace β-receptorů → při **náhlém vysazení rebound fenomén (syndrom z vysazení)** — tachykardie, vzestup tlaku, anginózní bolesti, riziko infarktu. Proto se β-blokátory vysazují **postupně**.
- **Kumulace účinku** — **humorální**: další dávka přijde dřív, než se předchozí eliminuje → roste koncentrace (závisí na dávkovacím intervalu a t½) · **funkční**: koncentrace stejná, ale roste citlivost tkáně.

🔑 **Tachyfylaxe = minuty · tolerance = dny až týdny · rezistence = vlastnost mikroba nebo nádoru, ne pacienta.**

❓ *Proč se nesmí náhle vysadit β-blokátor?* → Receptory jsou up-regulované; bez blokády přijde rebound tachykardie a hypertenze.

---

## O28 · Vliv průvodních onemocnění na účinek léčiv, polypragmazie

**O čem to je:** pacient málokdy má jen jednu nemoc — přidružené choroby mění, jak tělo lék zpracuje (kinetika) i jak na něj zareaguje (dynamika).

**Změny farmakokinetiky:**
- **Absorpce** — celiakie a Crohnova nemoc snižují vstřebávání; **gastroparéza u diabetu** zpomalí nástup účinku; antacida a inhibitory protonové pumpy sníží dostupnost ketokonazolu a digoxinu.
- **Distribuce** — **hypoalbuminemie** (jaterní a ledvinná onemocnění) → méně vazebných míst → **stoupá volná (účinná) frakce** warfarinu a fenytoinu → toxicita; při srdečním selhání horší prokrvení periferie omezí distribuci.
- **Metabolismus** — jaterní onemocnění sníží odbourávání léčiv závislých na CYP450 (**opioidy, benzodiazepiny**) → u cirhózy hrozí kumulace a útlum dechu.
- **Eliminace** — chronické onemocnění ledvin sníží clearance renálně vylučovaných léčiv (**aminoglykosidy, metformin, digoxin**) → dávka se upravuje **podle GFR**.

**Změny farmakodynamiky:**
- **snížená citlivost receptorů** — inzulinová rezistence u diabetika,
- **kompenzační mechanismy** — u srdečního selhání je sympatikus trvale aktivovaný, což mění odpověď na β-blokátory,
- **poruchy homeostázy** — **hypokalemie zásadně zvyšuje toxicitu digoxinu** (draslík soutěží s digoxinem o Na⁺/K⁺-ATPázu).

**Polypragmazie** = současné užívání více léčiv (typicky u polymorbidních seniorů). Rizika:
- **farmakokinetická interakce** — ketokonazol (inhibitor CYP3A4) zvýší hladinu statinu → rabdomyolýza,
- **farmakodynamická interakce** — warfarin + NSA → krvácení,
- **orgánová toxicita** — **ACE inhibitor + NSA** (obojí zhoršuje průtok ledvinou) → akutní poškození ledvin,
- **antagonismus a selhání léčby** — β-agonista proti β-blokátoru,
- **non-adherence** — složitý režim = chyby v užívání.
- **Prevence:** pravidelná revize medikace a rušení zbytečných léků, dávkování podle jaterních/renálních funkcí, software na interakce, edukace pacienta.

🔑 **Dvě dvojice, které chtějí slyšet: hypoalbuminemie → volná frakce warfarinu/fenytoinu ↑. Hypokalemie → toxicita digoxinu ↑.**

❓ *Proč je nebezpečná kombinace ACE inhibitoru a NSA?* → Obě zhoršují prokrvení a filtraci v ledvině → akutní renální selhání.

---

## O29 · Nežádoucí účinky léčiv

**O čem to je:** dvě části — jak funguje **systém hlášení a dohledu** (farmakovigilance) a jaké jsou **typy nežádoucích účinků (A–E)**. Klasifikace A–E je jádro otázky.

**Farmakovigilance** ("léková bdělost") — systematický dozor nad bezpečností už registrovaných léčiv: sledování v praxi, hodnocení poměru přínos/riziko, regulační opatření, informování zdravotníků. **Národním centrem v ČR je SÚKL.**
- **Zdroje:** spontánní hlášení lékařů i pacientů, klinická hodnocení, epidemiologické studie, firmy, literatura.
- **Kdo hlásí:** povinnost mají zdravotníci, držitelé registrace a zadavatelé studií — **hlásit ale může i sám pacient** (formulář SÚKL).
- **Náležitosti hlášení:** údaje o pacientovi a oznamovateli, popis reakce, název přípravku a léčivé látky, dávka a cesta podání.
- **Cesta hlášení:** unikátní světové číslo → databáze ČR / WHO / EudraVigilance → **farmakovigilanční signál** (hypotéza o souvislosti) → vyhodnocení → opatření: změna SPC/PIL, omezení indikace, změna dávkování nebo výdeje, až **stažení z trhu**.

**Pojmy, které se pletou:**

| Pojem | Definice |
|---|---|
| **nežádoucí účinek** | nepříznivá, nezamýšlená reakce na **běžnou dávku** |
| **nežádoucí příhoda** | jakýkoli neobvyklý nález u účastníka studie — **nemusí souviset** s léčbou |
| **závažný NÚ** | smrt, ohrožení života, hospitalizace, trvalé poškození nebo vrozená vada |
| **neočekávaný NÚ** | povahou či závažností **neodpovídá SPC** |

**Typy nežádoucích účinků A–E:**
- **A — Augmented (zesílený):** **až 95 % všech NÚ**, nízká mortalita, **předvídatelné** (odvoditelné z farmakologického účinku), **závislé na dávce**, typicky na začátku léčby. Příklady: **warfarin → krvácení, α1-blokátor → hypotenze, inzulin → hypoglykemie, β-blokátor → bronchospasmus u astmatika**. Řešení: **snížit dávku** (ne nutně vysadit), případně antidotum.
- **B — Bizarre (bizarní):** **vzácné (0,01–0,1 %), ale s vysokou mortalitou**, **nezávislé na dávce**, nepředvídatelné, typicky v prvních týdnech. Dva podtypy: **idiosynkrazie** (geneticky podmíněná odchylka, nedá se odvodit z mechanismu) a **léková alergie** (imunitně zprostředkovaná, vyžaduje předchozí expozici). Většina léčiv je příliš malá molekula na to, aby sama imunizovala — musí se navázat na bílkovinu jako **hapten** (penicilin na albumin) nebo vzniknout reaktivní metabolit (**prohapten** — sulfametoxazol). Řešení: **vysadit** (úprava dávky nepomůže).
- **C — Continuous:** až po **dlouhodobém** podávání (např. osteoporóza po kortikoidech).
- **D — Delayed:** projeví se **se zpožděním**, i po vysazení — teratogenita, kancerogenita.
- **E — End of use:** **po vysazení** — rebound fenomén (viz O27).

🔑 **Typ A = časté, předvídatelné, závislé na dávce → řeší se snížením dávky. Typ B = vzácné, nepředvídatelné, nezávislé na dávce → řeší se vysazením.**

❓ *Co je hapten?* → Malá molekula léčiva, která sama imunitní odpověď nevyvolá; musí se kovalentně navázat na velkou bílkovinu, a teprve pak je imunogenní.

---

## O30 · Léková alergie a idiosynkrazie

**O čem to je:** prohloubení typu B z O29. **Alergie** potřebuje imunitní systém a **předchozí kontakt**; **idiosynkrazie** je vrozená odchylka enzymu a předchozí kontakt nepotřebuje.

**Vznik alergie:** léčivo je malá molekula → imunogenní se stane až jako **hapten** (kovalentní vazba na nosičovou bílkovinu — penicilin na albumin), jako **prohapten** (reaktivní metabolit — sulfametoxazol), nebo přímou interakcí s receptory imunitního systému. Riziko zvyšuje **parenterální a kožní podání** (perorální je nejfyziologičtější a nejméně rizikové) a pomocné látky či nečistoty v přípravku.

**Čtyři typy podle Gell–Coombse:**

| Typ | Mechanismus | Nástup | Projev a příklady |
|---|---|---|---|
| **I — IgE** | senzibilizace → tvorba IgE; při reexpozici **degranulace mastocytů** (histamin, leukotrieny, PG) | **sekundy až minuty** | vyrážka, svědění, sekrece nosu/očí, otok, **anafylaktický šok**; peniciliny, cefalosporiny, chinolony, makrolidy, salicyláty, lokální anestetika |
| **II — cytotoxický** | léčivo na povrchu buňky + IgG/IgM → komplement a NK buňky → **destrukce buňky** | hodiny–dny | hemolytická anemie (cefalosporiny, chinidin, methyldopa, NSA), **trombocytopenie po heparinu** (až 5 %) |
| **III — imunokomplexový** | IgG + antigen → imunokomplexy uložené v tkáních | **1–3 týdny** | vaskulitida, horečka, artritida, glomerulonefritida; chimerické protilátky, amoxicilin, kotrimoxazol, NSA |
| **IV — pozdní, buněčný** | antigen prezentován **T-lymfocytům** → cytokiny | **2–8 dní** | kontaktní dermatitida, makulopapulózní exantém; aminoglykosidy |

- ⚠️ **Anafylaktický šok** — nejtěžší forma typu I: svědění, erytém, otok, tíseň na hrudi, bronchospasmus, **hypotenze**, arytmie. **75 % případů způsobují peniciliny.** Rizikové faktory: vyšší dávka, astma/atopie, vyšší věk.
- **Léčba alergie:** **adrenalin** (lék volby u anafylaxe — vazokonstrikce zvedne tlak, bronchodilatace, brzdí uvolňování mediátorů), **antihistaminika** (kompetitivní blokáda H1, snižují propustnost kapilár), **kortikoidy** (imunosuprese, brzdí tvorbu IgE — nastupují pomalu, proto až po adrenalinu).
- **Pseudoalergická reakce** — vypadá jako typ I, ale **není imunitní** (IgE nestoupá): jde o **přímé vytěsnění histaminu** z mastocytů. Stejně častá a rychlá jako typ I. Příklady: **NSA, vankomycin ("red man syndrome"), opioidy, radiokontrastní látky**.
- **Idiosynkrazie** — **nevyžaduje předchozí senzibilizaci**, jde o geneticky podmíněnou odchylku metabolismu. Příklady: **atypická (pseudo)cholinesteráza** odbourává sukcinylcholin abnormálně pomalu → **prodloužená apnoe a ochrnutí po myorelaxans**; **deficit glukózo-6-fosfátdehydrogenázy** → hemolýza po chinidinu, sulfonamidech, primachinu.
- **Léky stažené z trhu pro NÚ** (typická doplňující otázka): **thalidomid** (hypnotikum proti těhotenské nevolnosti — silný teratogen, fokomelie), **rimonabant** (anorektikum, inverzní agonista kanabinoidních receptorů — psychiatrické NÚ), **sibutramin** (anorektikum — kardiovaskulární rizika), **tetrazepam** (myorelaxans — těžké kožní reakce).

🔑 **Alergie potřebuje předchozí kontakt (imunitní paměť), idiosynkrazie ne (genetická odchylka enzymu). To je hlavní rozlišovací znak.**

❓ *Lék první volby u anafylaktického šoku?* → **Adrenalin**, ne antihistaminikum.

---

## O31 · Karcinogenní a mutagenní účinky

**O čem to je:** léčiva mohou poškodit DNA (**mutagenita**) a vyvolat nádor (**karcinogenita**) — proto se každé nové léčivo v preklinice povinně testuje na mutagenitu.

- **Mutagenita** = schopnost látky vyvolat mutaci (změnu genotypu). Mutace může vést k nádoru, nebo naopak k apoptóze poškozené buňky. **Pravděpodobnost roste s frekvencí buněčného dělení** (proto jsou zasažené hlavně rychle se dělící tkáně).
- **Amesův test** (test mutagenity in vitro) — použije se kmen *Salmonella typhimurium*, který kvůli mutaci **neumí syntetizovat histidin**. Naočkuje se do prostředí **bez histidinu** spolu s testovanou látkou: pokud látka vyvolá **zpětnou mutaci** a bakterie začne růst (umí si histidin vyrobit), je látka **mutagenní**.
- **Karcinogeny** se dělí na:
  - **genotoxické** — přímo poškozují DNA,
  - **epigenetické** — samy DNA nepoškodí, ale zvýší pravděpodobnost poškození: **promotory** (cigaretový kouř), **kokarcinogeny** (aromatické uhlovodíky), **hormony**.
- **Hlavní skupiny chemických karcinogenů:** polycyklické aromatické uhlovodíky (benzpyren, fenantren — cigaretový kouř, výfuky), aromatické aminy (barviva), nitrosloučeniny, **alkylační látky** (přenášejí alkyl na DNA — patří sem i některá **cytostatika**), aflatoxin (plíseň), kovy a azbest.

| IARC skupina | Význam | Příklady |
|---|---|---|
| **1** | prokázaný lidský karcinogen | azbest, benzen, etanol, **cyklosporin** |
| **2A** | pravděpodobný | **cisplatina**, chloramfenikol, anabolické steroidy |
| **2B** | možný | bleomycin, digoxin, fenobarbital, sulfasalazin |
| **3** | nehodnotitelný (málo důkazů) | aciklovir, ampicilin, disulfiram, káva |

🔑 **I běžně používaný lék může být prokázaný karcinogen — cyklosporin je ve skupině 1 stejně jako azbest. Cytostatika (alkylační látky) jsou zároveň lék i karcinogen.**

❓ *Jak funguje Amesův test?* → Sleduje, zda látka vyvolá zpětnou mutaci u salmonely neschopné tvořit histidin — růst kolonií = látka je mutagenní.

---

## O32 · Léčiva v těhotenství (teratogenní účinek) a léčiva v době kojení

**O čem to je:** v graviditě se mění farmakokinetika matky a navíc je tu placenta — přes ni se lék dostane k plodu a může způsobit **vrozenou vadu**. Klinicky jedna z nejdůležitějších otázek celé obecné farmakologie.

**Změny farmakokinetiky v graviditě:**
- **absorpce** — nauzea a zvracení v I. trimestru, **vyšší (méně kyselé) pH žaludku**, zpomalená motilita vlivem progesteronu; inhalačně se vstřebává **rychleji** (větší dechový objem), i.m. **pomaleji** (horší žilní odtok z dolní poloviny těla),
- **distribuce** — distribuční objem **+ až 50 %** (plazma a celková voda +7 l), vyšší srdeční výdej a průtok ledvinami; **hypoalbuminemie** (steroidy obsadí vazebná místa) → **roste volná frakce léčiv**,
- **eliminace** — v játrech stoupá aktivita CYP450 a glukuronyltransferázy (ale CYP1A2 a CYP2C19 klesají); **renální průtok +25–50 %, GF +50 %** → renálně vylučovaná léčiva se eliminují rychleji (mohou potřebovat vyšší dávku).

**Placenta a plod:**
- **téměř všechna léčiva k plodu v nějaké míře pronikají**, hlavně **prostou difuzí** (nejlépe lipofilní, neionizované, s nízkou molekulovou hmotností), část i aktivním transportem (P-glykoprotein plod naopak chrání tím, že léčivo pumpuje zpět),
- **krev plodu má nižší pH** než mateřská → slabé zásady projdou placentou a v plodu se **ionizují a uvíznou (iontová past)** → hromadí se,
- eliminace u plodu je **nezralá** — spoléhá hlavně na zpětnou difuzi do matky.

**Období expozice rozhoduje o následku:**
- **blastogeneze (0.–14. den)** — pravidlo „**všechno, nebo nic**": buď zánik zárodku, nebo úplná náprava bez následků,
- **organogeneze (15.–90. den)** — **nejnebezpečnější, vznikají anatomické malformace**,
- **fetální období (90.–280. den)** — už ne malformace, ale **funkční poruchy** (mentální retardace, poruchy růstu).

**FDA kategorie rizika:** **A** bez rizika (levotyroxin, kyselina listová) · **B** bez rizika u zvířat (paracetamol, amoxicilin, metformin) · **C** teratogenní u zvířat, u lidí nejasné (teofylin, amlodipin) · **D** doložené riziko, ale při nenahraditelnosti se použije (sartany, ACE inhibitory) · **X** riziko jednoznačně převažuje — **warfarin, statiny, isotretinoin**.

| Teratogen | Následek u plodu |
|---|---|
| barbituráty, benzodiazepiny | závislost plodu, **fetální abstinenční syndrom** |
| ACE inhibitory / sartany | renální selhání plodu, **oligohydramnion** |
| kyselina acetylsalicylová | krvácení (matky i plodu) |
| NSA (III. trimestr) | **předčasný uzávěr Botallovy dučeje** (ductus arteriosus) |
| tetracykliny | porucha vývoje **skloviny a kostí**, žluté zbarvení zubů |
| **warfarin** | **fetální warfarinový syndrom** — nízká porodní hmotnost, sedlovitý nos, hypoplazie kostí, mentální retardace, hluchota; intrakraniální krvácení |
| **fenytoin** | **fetální hydantoinový syndrom** — rozštěpy obličeje, mikrocefalie, vady srdce a končetin, hypoplazie nehtů, nízko nasedající uši |

**Vhodné vs. nevhodné:** antibiotika — **peniciliny a cefalosporiny** ano, tetracykliny/chinolony/sulfonamidy ne · antitrombotika — **LMWH ano** (neprochází placentou), warfarin ne · antihypertenziva — **methyldopa** ano, ACE inhibitory a sartany ne · mukolytika — ambroxol, acetylcystein ano. *(⚠️ Zdroj katedry řadí mezi nevhodné i betablokátory — v praxi je labetalol/metoprolol v graviditě běžný, problematický je hlavně atenolol. U zkoušky jeď podle skript.)*

**Zásady léčby chronicky nemocné těhotné:** **neléčená nemoc bývá pro plod větší riziko než léčba** · plánovat graviditu v době nejlepší kompenzace · **monoterapie a nejnižší účinná dávka** · monitorovat hladiny (vyhnout se kolísání) · v citlivém období vývoje orgánu případně krátce vysadit (lithium a srdce plodu) · využít prenatální diagnostiku · u každé ženy ve fertilním věku počítat s možností gravidity.

**Kojení:**
- do mléka přechází většina léčiv **pasivní difuzí**; nejlépe **lipofilní, neionizovaná, málo vázaná na bílkoviny, s malou molekulou**,
- záleží i na dítěti — **jaterní metabolismus dozrává týdny** (u plodu funguje CYP3A7, po narození se mění na CYP3A4), takže novorozenec léčivo eliminuje pomalu,
- **tvorbu mléka snižují** estrogeny, gestageny a **bromokriptin** (agonista dopaminu → potlačí prolaktin); **zvyšují ji** dopaminoví antagonisté **metoklopramid a domperidon** a fenotiazinová neuroleptika,
- **praktické pravidlo:** lék užít **hned po kojení / 3–4 h před dalším kojením**, ideálně před nejdelším spánkem dítěte, aby hladina stihla klesnout; u krátkodobé nutné léčby zvážit dočasné přerušení kojení.

🔑 **Nejnebezpečnější období je organogeneze (15.–90. den) — přesně doba, kdy žena často ještě neví, že je těhotná.**

❓ *Proč se NSA nesmí ve III. trimestru?* → Předčasně uzavírají Botallovu dučej.

---
