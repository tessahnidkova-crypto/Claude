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

## O33 · Farmakoterapie v dětství

**O čem to je:** klíčová věta celé otázky — **dítě není malý dospělý**. Novorozenec má jinou absorpci, distribuci, metabolismus i eliminaci, a mění se to z týdne na týden.

**Novorozenec** = 0.–28. den, farmakoterapeuticky **extrémně nehomogenní** skupina (týdenní dítě funguje jinak než 27denní).

- **Absorpce:** perorálně těžko předvídatelná — **vyšší (méně kyselé) pH žaludku**, pomalé vyprazdňování, málo žlučových kyselin a pankreatických šťáv, pomalá peristaltika. **I.m.** špatné u nemocného dítěte (centralizace oběhu). **Rektálně** se vstřebává dobře, ale nespolehlivě (odchod stolice). **Endotracheálně** se podává adrenalin při resuscitaci a surfaktant. **Transdermálně nevhodné** — tenká kůže nezralého novorozence propustí významné množství látky do oběhu.
- **Distribuce:** **voda tvoří 75 % hmotnosti** (dospělý ~60 %) → **větší distribuční objem hydrofilních léčiv** (potřebují relativně vyšší dávku) a **menší pro lipofilní** (málo tuku); nízký albumin i kyselý glykoprotein → **vysoká volná frakce** → snadná toxicita.
- **Metabolismus:** reakce **fáze I** má donošený novorozenec na **50–70 % kapacity dospělého**; **fáze II (konjugace) dozrává až kolem 2 let** — nízká UDP-glukuronyltransferáza nutí tělo použít náhradní cesty a vznikají jiné metabolity.
- **Exkrece:** **glomerulární filtrace dosáhne hodnot dospělého až v polovině 2. roku**; nedonošení mají navíc velmi nízkou tubulární funkci.
- **Praktické:** léková forma musí být přijatelná chuťově (sirupy, korigované suspenze), i.m. injekce se aplikuje do **m. quadriceps femoris**, dávky podle lékopisu (*dosis pro infantibus*), přepočet na **hmotnost nebo povrch těla**.

| Syndrom | Léčivo | Projevy |
|---|---|---|
| **Reyeův syndrom** | **kyselina acetylsalicylová** (typicky při virové infekci) | jaterní encefalopatie, zvracení, delirium, křeče, nitrolební hypertenze — **může být smrtelný** |
| **Gray baby syndrom** | **chloramfenikol** (nezralá konjugace → kumulace) | šedá kůže, hypotenze, hypoperfuze, kolaps, šok |
| poškození zubů a kostí | **tetracykliny** | ukládají se do rostoucí kosti a skloviny |

🔑 **Tři jména, tři syndromy: aspirin → Reye · chloramfenikol → gray baby · tetracyklin → zuby a kosti.**

❓ *Proč je chloramfenikol nebezpečný u nedonošenců?* → Nezralá glukuronidace v játrech → kumulace → gray baby syndrom.

---

## O34 · Farmakoterapie ve stáří, polypragmazie

**O čem to je:** zrcadlo O33 — u seniora se ADME zase zpomaluje, ale z involuce orgánů, ne z nezralosti. K tomu se přidává polypragmazie.

**Senior = nad 65 let.** Typická je **zvýšená vnímavost k benzodiazepinům**, horší compliance a přidružené nemoci vedoucí k polypragmazii.

- **Absorpce:** vzestup žaludečního pH (hypo- až achlorhydrie), menší vstřebávací plocha střeva, horší prokrvení splanchniku, nižší motilita.
- **Distribuce:** **klesá tělesná voda** → menší distribuční objem → **vyšší koncentrace hydrofilních léčiv** (digoxin, ASA) · **stoupá tuk** → větší objem a **delší poločas lipofilních** (benzodiazepiny, metoprolol) · **hypoalbuminemie** → vyšší volná frakce (warfarin, NSA, perorální antidiabetika).
- **Metabolismus a dynamika:** klesá kapacita jater (fáze I i II) a mění se citlivost receptorů → vyšší vnímavost k **benzodiazepinům, morfinu, warfarinu, ACE inhibitorům**.
- **Exkrece:** klesá renální průtok i GF — **po 75. roce až o 50 %**, a to **bez vzestupu sérového kreatininu**.

⚠️ **Klasická past: normální kreatinin u seniora neznamená normální ledviny** — malá svalová hmota tvoří málo kreatininu, takže hodnota "vypadá dobře" i při poloviční filtraci. Dávkuj podle vypočtené GFR/clearance kreatininu, ne podle kreatininu samotného.

- **Zásady:** ptát se, jestli je lék vůbec nutný · hledat bezpečnější alternativu · **vyhýbat se polypragmazii** · volit zvládnutelnou lékovou formu a pacienta poučit · pravidelně revidovat medikaci a aktivně pátrat po nežádoucích účincích.
- **Nástroje:** **Beersova kritéria** = seznam léčiv potenciálně nevhodných u seniorů · **STOPP** = najde nevhodný nebo zbytečný lék · **START** = upozorní na **chybějící** potřebnou léčbu.

🔑 **START hledá, co chybí; STOPP hledá, co přebývá. Beers je obecný seznam nevhodných léčiv.**

❓ *Proč mají senioři delší poločas benzodiazepinů?* → Vyšší podíl tělesného tuku → větší distribuční objem lipofilních látek.

---

## O35 · Biologická léčba: rozdělení, názvosloví, biosimilars, přínosy a rizika

⚠️ **Tuhle otázku tvoje vypracované materiály nemají** — text je z obecných znalostí `[doplněno]`, ne ze skript. Kdyby se lišila přednáška, platí přednáška.

**O čem to je:** biologika jsou léky vyrobené **živým organismem** (ne chemickou syntézou) — velké bílkoviny jako protilátky, hormony či enzymy. Kvůli velikosti se chovají úplně jinak než klasické malé molekuly.

| | Malá molekula | Biologikum |
|---|---|---|
| Velikost | stovky Da | tisíce až ~150 000 Da |
| Výroba | chemická syntéza | **živé buňky** (rekombinantní DNA, hybridomy) |
| Podání | často perorálně | **prakticky vždy parenterálně** (bílkovina by se v GIT strávila) |
| Imunogenita | nízká | **významná** |
| Kopie po patentu | generikum = identické | **biosimilar = vysoce podobný, ne identický** |

- **Rozdělení podle typu (poznáš podle koncovky):** **-mab** monoklonální protilátky (infliximab, rituximab, trastuzumab) · **-cept** fúzní proteiny (etanercept) · rekombinantní **hormony** (inzulin, somatropin) · **-áza** enzymy (altepláza) · **cytokiny** (interferon alfa) · **-stim** růstové faktory (filgrastim) · **-poetin** erytropoetiny · **ATMP** (genová terapie, CAR-T).
- **Názvosloví protilátek** podle míry „polidštění": **-o-** myší (nejvíc imunogenní) → **-xi-** chimérická (ritu**xi**mab) → **-zu-** humanizovaná (trastu**zu**mab) → **-u-** plně humánní (adali**mu**mab, nejméně imunogenní).
- **Biosimilar** — u biologika nelze vyrobit chemicky identickou kopii (roste v živých buňkách), proto se registruje jako přípravek **vysoce podobný** referenčnímu, bez klinicky významných rozdílů v kvalitě, účinnosti a bezpečnosti. Vyžaduje **srovnávací studie včetně imunogenity**, ne jen průkaz bioekvivalence jako u generika.
- **Přínosy:** vysoká cílová specificita, účinnost tam, kde konvenční léčba selhává (revmatoidní artritida, IBD, psoriáza, roztroušená skleróza, onkologie), často ovlivní **průběh nemoci**, ne jen příznaky; dlouhý poločas → řidší dávkování.
- **Rizika:** **imunogenita** (protilátky proti léčivu → ztráta účinku) · **infekce a reaktivace latentní TBC a hepatitidy B** · infuzní reakce až anafylaxe · **syndrom z uvolnění cytokinů** (CAR-T, bispecifické protilátky) · imunitně podmíněné NÚ u checkpoint inhibitorů (kolitida, hepatitida, tyreoiditida) · cena a chladový řetězec.
- **Před zahájením vždy:** screening latentní TBC (IGRA/Mantoux + RTG), hepatitidy B a C, HIV; vyloučit aktivní infekci. **Živé vakcíny jsou během biologické léčby kontraindikované.**

⚠️ Léčiva s koncovkou **-tinib** (imatinib, erlotinib) jsou **malé molekuly, ne biologika** — „cílená léčba" a „biologická léčba" nejsou synonyma.

❓ *Co je nutné vyšetřit před anti-TNF terapií?* → Latentní TBC a hepatitidu B (riziko reaktivace).

---

# ČÁST 2 — SPECIÁLNÍ FARMAKOLOGIE I (36–88)

## 36 · Cholinergní přenos vzruchu

**O čem to je:** vegetativní nervový systém řídí to, na co nemyslíš (tep, trávení, pocení) — dvě větve fungují jako plyn a brzda. Tahle otázka je o „brzdě" (parasympatiku) a o přenašeči **acetylcholinu**.

**Cesta signálu je vždy stejná:** mozkový kmen nebo mícha → **pregangliové vlákno** → ganglion (přepojení) → **postgangliové vlákno** → orgán. Přenašeč se skladuje ve vezikulách a uvolňuje exocytózou.

| | Sympatikus | Parasympatikus |
|---|---|---|
| Původ vláken | **thorakolumbální** (hrudní + bederní mícha) | **kraniosakrální** (mozkový kmen + křížová mícha) |
| Kdy | zátěž, strach, zima, hypoglykemie | klid, trávení, tvorba zásob (anabolismus) |
| Efekt | ↑ tlak, mobilizace energie — *fight or flight* | trávení, vylučování — *rest and digest* |
| Uspořádání | **difuzní** (jedno vlákno zasáhne víc orgánů) | **cílené** (jeden orgán) |

**Kde se přenáší acetylcholinem** (pozor, není to jen parasympatikus):
- **nervosvalová ploténka** (kosterní sval),
- **pregangliová vlákna OBOU větví** — v gangliu se vždy přepojuje přes ACh, i u sympatiku,
- **postgangliová vlákna sympatiku k potním žlázám** — záměrná výjimka z pravidla „sympatikus = noradrenalin", oblíbený chyták,
- **dřeň nadledvin** (ACh tam spouští výlev adrenalinu),
- **celý postgangliový parasympatikus**.

**Dva typy receptorů:**
- **Nikotinové (N)** — samy jsou **iontový kanál**: navázání ACh kanál otevře, dovnitř jde Na⁺/K⁺ → **rychlá** depolarizace. Umístění: ganglia a nervosvalová ploténka.
- **Muskarinové (M)** — **receptory spřažené s G-proteinem**, přes druhé posly (IP₃, DAG, cAMP) → **pomalejší, ale komplexnější** odpověď:

| Receptor | Kde | Efekt |
|---|---|---|
| **M1** | CNS, žlázy | kognice, ↑ sekrece žaludeční šťávy a slin |
| **M2** | **srdce** | ↓ frekvence SA uzlu (negativně chronotropně), ↓ síla stahu, ↓ vedení AV uzlem |
| **M3** | hladké svaly, exokrinní žlázy, endotel | ↑ sekrece a motilita GIT, uvolnění svěračů, **mióza**, **bronchokonstrikce**, vazodilatace (přes NO z endotelu) |
| **M4, M5** | CNS | modulace pohybu a dopaminového systému |

🔑 **N = rychlý iontový kanál (ganglia, ploténka) · M = pomalý G-protein (orgány parasympatiku). V gangliu je vždy acetylcholin — teprve za ním se sympatikus přepne na noradrenalin.**

❓ *Kde má sympatikus výjimečně acetylcholin?* → Na postgangliových vláknech k **potním žlázám**.

---

## 37 · Přímá cholinomimetika

**O čem to je:** léky, které **napodobují acetylcholin** tím, že se přímo navážou na jeho receptor → efekt „zapnutý parasympatikus navíc".

- **Mechanismus:** agonisté **M i N** receptorů; převažuje stimulace **M → parasympatomimetický efekt**. Některé dráždí i **gangliové N** (aktivují obě větve VNS a výlev adrenalinu z nadledvin) nebo N na ploténce a v CNS.
- ⚠️ **Samotný acetylcholin se jako lék nepoužívá** — v synapsi ho okamžitě rozloží **acetylcholinesteráza (AChE)** na cholin a acetát, účinek by trval vteřiny. Používají se proto **syntetické estery cholinu** (odolné vůči AChE) a **přírodní alkaloidy**.
- **Účinky (a tím i nežádoucí účinky celé skupiny):** **mióza** a pokles nitroočního tlaku, **bradykardie**, **vazodilatace a hypotenze** (přes NO), **bronchokonstrikce**, ↑ motilita GIT a povolení svěračů, ↑ sliny, slzy, pot, stah močového měchýře; centrálně zlepšení kognice a nálady.

| Léčivo | Podstatné |
|---|---|
| **Karbachol** | odolný vůči AChE → dlouhý účinek; **glaukom** |
| **Betanechol** | atonie střev, **retence moči** |
| **Cevimelin** | selektivní **M3** → ↑ sliny a slzy |
| **Pilokarpin** | alkaloid; **mióza, glaukom**, ↑ salivace |
| **Arekolin** | M i N, centrálně stimulační; složka **betelu** — červené sliny, **ničí sklovinu, černý chrup** |

- **Indikace:** glaukom, pooperační atonie střev a retence moči, **xerostomie** (suchost v ústech u Sjögrenova syndromu — cevimelin, pilokarpin).
- **Kontraindikace:** **astma a CHOPN** (bronchokonstrikce), bradykardie a AV blokáda, vředová choroba (↑ kyselina), obstrukce střev a močových cest.
- **Muskarin a otrava houbami:** muskarin je z mochomůrky, ale nejvíc ho mají houby rodu **vláknice**. Během minut: zvracení, průjem, slinění, slzení, pocení, **mióza, bronchospasmus, bradykardie**. **Antidotum = atropin** (blokuje M receptory, na které muskarin útočí); při křečích diazepam.
- **Nikotin:** působí na N v obou gangliích, v CNS i na ploténce → tachykardie, ↑ tlak, ↑ motilita GIT, ↑ sliny/pot/bronchiální sekrece, výlev adrenalinu a ADH, zvracení. Nízká dávka centrálně: euforie, pozornost; vysoká: **křeče, zvracení, zástava dechu**. Receptory umí i **desenzibilizovat** → nepředvídatelný efekt a **fyzická i psychická závislost**. Z cigarety se vstřebá ~**1,5 mg**, smrtelná dávka **~40 mg**. Odvykání: psychoterapie, náhradní nikotin, antidepresivum.

🔑 **Nežádoucí účinky cholinomimetik jednou větou: sliny, pot, slzy, mióza, průjem, časté močení, dušnost z bronchospasmu, hypotenze, bradykardie.**

❓ *Které léky z téhle otázky použiješ jako zubařka?* → **Pilokarpin a cevimelin na xerostomii**; betel (arekolin) je učebnicová příčina zničené skloviny.

---

## 38 · Nepřímá cholinomimetika

**O čem to je:** místo napodobování acetylcholinu se jednoduše **zablokuje enzym, který ho odbourává** — vlastní ACh se pak v synapsi hromadí a účinkuje déle a silněji.

- **Mechanismus:** **inhibitory cholinesterázy**. Dva enzymy: **AChE** (acetylcholinesteráza, vázaná na membránu synapse) a **butyrylcholinesteráza** = pseudocholinesteráza (plazma, tkáně). Efekt je jako u M agonistů, **navíc posílí kontrakci kosterního svalu** (hromadění ACh na ploténce).
- **Reverzibilní inhibitory** (účinek pomine sám) — karbamáty a příbuzné látky. Kdo má **terciární dusík, prochází hematoencefalickou bariérou** a působí i v CNS (ve vysoké dávce křeče, pak útlum CNS a dechu); **kvartérní dusík do mozku neprojde**.

| Léčivo | Zvláštnost |
|---|---|
| **Neostigmin** | kvartérní — **neprochází do CNS**; atonie střev, retence moči, dekurarizace |
| **Pyridostigmin, distigmin** | dlouhodobá léčba **myasthenia gravis** |
| **Edrofonium** | velmi krátký účinek → **diagnostika myasthenia gravis** |
| **Fyzostigmin** | terciární — **jediný vstupuje do CNS**; otrava atropinem/cholinolytiky, glaukom |
| **Rivastigmin, donepezil, galantamin** | **Alzheimerova choroba** (viz otázka 59) |

- **Indikace:** **myasthenia gravis** (autoimunitní protilátky proti N receptorům ploténky → padající víčko, dvojité vidění, poruchy polykání, únavnost svalů, v těžkém případě dechové selhání), pooperační atonie střev a retence moči, glaukom, **otrava parasympatolytiky (atropinem)**, Alzheimerova choroba.
- **Kontraindikace a NÚ:** stejné jako u přímých cholinomimetik — astma, bradykardie, vřed, obstrukce; při předávkování **cholinergní krize** (slinění, křeče, slabost dýchacích svalů).
- **Ireverzibilní inhibitory — organofosfáty:** fosforylují AChE a vyřadí ji **natrvalo**. Po několika hodinách komplex „**zestárne**" (chemická přeměna) a **reaktivace už není možná** — proto se s léčbou musí spěchat. Patří sem insekticidy (paraoxon), **bojové látky sarin a soman** (vstřebávají se i kůží) a echotiofát (glaukom).

🔑 **Léčba otravy organofosfáty ve třech krocích: ① atropin i.v. (blokuje M receptory) ② reaktivátory cholinesterázy — pralidoxim/obidoxim, ale jen dokud komplex „nezestárl" ③ diazepam na křeče.**

❓ *Jak se potvrdí myasthenia gravis farmakologicky?* → Podá se **edrofonium** — krátkodobé zlepšení svalové síly diagnózu podporuje.

---

## 39 · Parasympatolytika

**O čem to je:** přesný opak otázky 37 — **blokáda M receptorů** = „vypnutý parasympatikus": sucho v ústech, tachykardie, mydriáza.

- **Mechanismus:** **přímá** parasympatolytika = kompetitivní antagonisté **muskarinových** receptorů (**N receptory neovlivňují** → nemají vliv na ganglia ani na ploténku). **Nepřímá** brání tvorbě nebo uvolnění ACh.
- **Zástupci — přírodní alkaloidy:** **atropin, hyoscyamin, skopolamin** z rulíku zlomocného, blínu černého a durmanu.

🔑 **Citlivost tkání k atropinu (přesně v tomhle pořadí se ptají):** ① **nejcitlivější — slinné, bronchiální a potní žlázy** (proto je sucho v ústech první příznak) → ② hladké svaly a srdce → ③ **nejméně citlivé — parietální buňky žaludku** tvořící kyselinu.

- **Indikace:** **mydriáza a cykloplegie** před vyšetřením očního pozadí (homatropin, tropikamid) · **premedikace před celkovou anestezií** (potlačí salivaci a bronchiální sekreci, chrání před vagovou bradykardií) · **bronchodilatancia u CHOPN — ipratropium, tiotropium** (inhalačně, kvartérní dusík → minimum systémových účinků) · **antidotum otravy inhibitory AChE a muskarinem** · **bradykardie a AV blokáda** (i.v. atropin) · **kinetóza a zvracení — skopolamin** (náplast) · **antiparkinsonika — biperiden, procyklidin** · **spasmolytika — butylskopolamin** (koliky GIT), **oxybutynin** (hyperaktivní měchýř).
- **Nežádoucí účinky (jsou to jen zesílené hlavní účinky):** sucho v ústech, poruchy akomodace a rozmazané vidění, **tachykardie**, zácpa, retence moči, **potlačení pocení → hypertermie** („atropinová horečka", u dětí i po malé dávce); centrálně neklid, zmatenost, halucinace (u seniorů delirium).
- ⚠️ **Kontraindikace: glaukom** (mydriáza zhorší odtok nitrooční tekutiny → akutní záchvat) a **hyperplazie prostaty** (retence moči); dále tachyarytmie a obstrukční stavy GIT.
- **Botulotoxin** (nepřímé cholinolytikum) — toxin *Clostridium botulinum* **zabrání splynutí vezikul s presynaptickou membránou**, takže se ACh vůbec neuvolní. Klinicky: blefarospazmus, hemifaciální spazmus, strabismus, anální fisura, **hypersalivace, hyperaktivní měchýř**, kosmeticky vrásky.

❓ *Proč je atropin kontraindikován u glaukomu?* → Rozšířená duhovka zablokuje odtok komorové tekutiny → prudký vzestup nitroočního tlaku.

---

## 40 · Adrenergní přenos vzruchu

**O čem to je:** zrcadlo otázky 36, ale pro **sympatikus** — přenašečem není acetylcholin, ale **noradrenalin**, a receptory se jmenují **α a β**.

- **Mechanismus:** postgangliová vlákna sympatiku uvolňují **noradrenalin (NA)**, který působí na **adrenergní receptory spřažené s G-proteinem** (pomalejší, ale komplexnější odpověď než iontový kanál). V CNS se část NA metyluje na **adrenalin**, dopaminergní neurony používají **dopamin**.

| Receptor | Kde | Co dělá |
|---|---|---|
| **α1** | hladká svalovina cév, svěrače, oko | **vazokonstrikce → ↑ tlak**, mydriáza, kontrakce svěrače měchýře, ejakulace, glykogenolýza |
| **α2** | **presynapticky**, trombocyty, β-buňky pankreatu | **brzda vlastního výdeje NA → ↓ tonus sympatiku a ↓ tlak**; agregace destiček; ↓ sekrece inzulinu |
| **β1** | **srdce**, ledviny | **↑ frekvence, ↑ síla stahu, ↑ vedení, ↑ spotřeba O₂**; ↑ uvolnění **reninu** |
| **β2** | průdušky, cévy svalů, děloha, játra | **bronchodilatace**, vazodilatace ve svalech, tokolýza (uvolnění dělohy), ↓ motilita GIT, glykogenolýza |
| **β3** | tuková tkáň, měchýř | lipolýza, relaxace stěny měchýře |

- **Jak se do toho dá zasáhnout léky:**
  - **Sympatomimetika** — **přímá** (agonisté receptorů, selektivní i ne) a **nepřímá**, která zvyšují množství NA ve štěrbině: ↑ jeho uvolnění, ↓ jeho odbourání (inhibitory MAO), nebo blokádou **zpětného vychytávání** (amfetamin, efedrin, pseudoefedrin, kokain).
  - **Sympatolytika** — **přímá** (α- a β-blokátory) a **nepřímá** (reserpin brání ukládání NA do vezikul, guanetidin brání jejich vyprázdnění — dnes prakticky mimo praxi).

🔑 **α1 a β1 = „zesil a stáhni" · α2 = brzda sympatiku samotného · β2 = „rozšiř" (průdušky, cévy svalů).**

❓ *Proč agonista α2 snižuje tlak, když ostatní α receptory tlak zvyšují?* → Je **presynaptický** — jeho aktivace tlumí uvolňování noradrenalinu, tedy celý sympatický výdej (princip klonidinu a methyldopy).

---

## 41 · Neselektivní sympatomimetika (katecholaminy)

**O čem to je:** skupina definovaná chemickou strukturou (adrenalin, noradrenalin a příbuzní), která působí na **víc typů receptorů najednou** — proto „neselektivní".

**Pět vlastností katecholaminu:** ① **-OH na 3. a 4. pozici** benzenového jádra (rozhoduje o délce účinku) ② nejúčinnější přímí agonisté α i β ③ rychle je odbourávají **COMT a MAO** ④ **perorálně neúčinné** (rozloží se dřív, než se vstřebají) ⑤ jsou polární → do CNS pronikají špatně, přesto mají centrální účinky (třes, úzkost). Vznikají z **fenylalaninu/tyrosinu**. **Adrenalin má nejvyšší afinitu k α, isoprenalin k β.**

- **Uptake (zpětné vychytávání):** **uptake 1** = zpět do presynaptického zakončení, kde NA rozloží **MAO** · **uptake 2** = difuze do okolních buněk, kde ho rozloží **COMT**.
- **Adrenalin** — hormon dřeně nadledvin: přes **β1** ↑ frekvence, síla stahu, srdeční výdej a spotřeba O₂, ↑ systolický tlak · přes **α** vazokonstrikce v kůži a na sliznicích · přes **β2** vazodilatace ve svalech, **bronchodilatace**, glykogenolýza · přes **α2** ↓ inzulin. **Poločas ~2,5 minuty** (MAO + COMT).
  - **Indikace: kardiopulmonální resuscitace, anafylaktický šok, těžké astma, vazokonstrikční přísada do lokálních anestetik** (prodlouží účinek a sníží krvácení).
  - **NÚ:** třes, úzkost, bolest hlavy, arytmie, hyperglykemie (diabetik potřebuje víc inzulinu).
  - ⚠️ **Interakce, které tě jako zubařku zajímají:** **inhalační anestetika zvyšují citlivost myokardu k adrenalinu** (arytmie) · s **neselektivními β-blokátory** hrozí hypertenzní krize (nezablokované α působí samo) · opatrně u **hypertyreózy** a **ischemické choroby srdeční**.
- **Noradrenalin** — stimuluje hlavně **α1 a β1**, **NEpůsobí na β2 → nemá bronchodilatační účinek**; zvyšuje periferní odpor a oba tlaky. **Indikace: septický šok a akutní hypotenze** (vazopresor volby).
- **Isoprenalin** — syntetický, čistý **β** agonista (β1 i β2): silně stimuluje srdce, **klesá diastolický a stoupá systolický tlak**; jen i.v. v akutní medicíně (bradykardie, AV blok).
- **Dobutamin** — **selektivní β1**, odvozený od dopaminu: ↑ kontraktilita a srdeční výdej, ↓ tlak v plicnici. **Indikace: kardiogenní šok, těžké srdeční selhání, stav po kardiochirurgii.**

🔑 **Dopamin — účinek závisí na dávce (klasická zkušební otázka):** **do 2 μg/kg/min → D receptory** (vazodilatace v ledvinách a splanchniku, ↑ diuréza, na srdce skoro nic) · **do 10 → β1** (↑ srdeční výdej) · **nad 10 → α** (vazokonstrikce, ↑ tlak) · **nad 20 → α převáží nad D a prokrvení ledvin naopak klesá**. Indikace: šok a těžká hypotenze.

❓ *Proč se katecholaminy nepodávají ústy?* → Rozloží je MAO a COMT ve stěně střeva a v játrech dřív, než se dostanou do oběhu.

---

## 42 · Sympatomimetika alfa

**O čem to je:** selektivní stimulace **jen α receptorů** — buď na zúžení cév (dekongestanty, hypotenze), nebo paradoxně na **snížení** tlaku (α2).

- **Selektivní α1-agonisté — mechanismus:** stah hladké svaloviny cév → ↑ periferní odpor a tlak, mydriáza, snížení překrvení sliznic.

| Léčivo | Podstatné |
|---|---|
| **Fenylefrin** | mydriatikum a dekongestant; **odolný vůči COMT → mnohem delší účinek** než katecholaminy; ↑ tlak. **KI v těhotenství** |
| **Midodrin** | **ortostatická hypotenze**, stresová inkontinence |
| **Nafazolin, xylometazolin, oxymetazolin, tetryzolin** | lokální dekongestanty do nosu a očí (alergická rýma, konjunktivitida) |

- ⚠️ **Nosní dekongestanty nepoužívat souvisle déle než ~7 dní** — vzniká **rhinitis medicamentosa** (rebound otok sliznice a návyk).
- **NÚ α1-agonistů:** hypertenze, **reflexní bradykardie**, bolest hlavy, retence moči; lokálně pálení a poškození sliznice. **KI:** hypertenze, ischemická choroba srdeční, tachyarytmie, glaukom s úzkým úhlem.
- **Selektivní α2-agonisté — paradox:** α2 sedí **presynapticky**, jeho aktivace je zpětnovazebná **brzda výdeje noradrenalinu** → klesá tonus sympatiku i tlak.
  - **klonidin** (u nás nedostupný), **moxonidin a rilmenidin** (centrálně působící antihypertenziva), **brimonidin** (oční kapky — ↓ tvorba nitrooční tekutiny → **glaukom**), **dexmedetomidin** (sedace na JIP).
  - **NÚ:** sedace, sucho v ústech, bradykardie, **rebound hypertenze při náhlém vysazení**.
- ⚠️ **L-methyldopa** — proléčivo, v CNS se mění na α-metylnoradrenalin, přes α2 sníží tonus sympatiku. **Antihypertenzivum volby u těhotných** — tohle chtějí slyšet.

❓ *Jaké antihypertenzivum se volí v graviditě?* → **Methyldopa** (centrální α2-agonista).

---

## 43 · Sympatomimetika beta

**O čem to je:** selektivní stimulace β receptorů — každý podtyp má jiné využití: **β1 srdce, β2 průdušky, β3 měchýř**.

- **Selektivní β1 — dobutamin:** derivát dopaminu bez vlivu na periferní D receptory; **pozitivně inotropní** (zesílí stah), ↑ srdeční výdej, ↓ tlak v plicnici. **Indikace: kardiogenní šok, těžké srdeční selhání, po kardiochirurgii.** Podává se **jen i.v.** (nástup do 2 min). NÚ: tachyarytmie, ↑ spotřeba kyslíku myokardem.
- **Selektivní β2 — mechanismus:** aktivace β2 → ↑ cAMP v hladkém svalu bronchů → **bronchodilatace**; navíc tokolytický efekt (uvolní dělohu — dnes se ale prakticky nepoužívá).

| Skupina | Charakteristika | Zástupci |
|---|---|---|
| **SABA** krátkodobá | nástup v minutách, účinek 4–6 h — **úlevová léčba astmatického záchvatu** | **salbutamol**, fenoterol, terbutalin, clenbuterol |
| **RABA** rychle nastupující | rychlý nástup | **formoterol** |
| **LABA** dlouhodobá | účinek ~12 h — **udržovací** léčba, vždy s inhalačním kortikoidem | **salmeterol**, formoterol, vilanterol |
| **uLABA** ultradlouhá | 24 h, hlavně **CHOPN** | indakaterol, olodaterol |

- ⚠️ **Formoterol je zároveň RABA i LABA** — proto se hodí do kombinace IKS + formoterol jako **úlevová i udržovací** léčba zároveň (viz otázka 96). ⚠️ **LABA se nikdy nepodává samostatně bez kortikoidu** — zvyšuje mortalitu na astma.
- **NÚ β2-agonistů:** **třes**, palpitace a tachyarytmie, **hypokalemie** (draslík se přesouvá do buněk), bolest hlavy, neklid, nespavost, hyperglykemie. **KI:** tachyarytmie, hypertrofická kardiomyopatie, neléčená hypertyreóza.
- **Selektivní β3 — mirabegron:** uvolní stěnu měchýře a zvětší jeho kapacitu → **hyperaktivní močový měchýř** (alternativa k anticholinergikům, nezpůsobuje sucho v ústech). NÚ: hypertenze, tachykardie.

🔑 **β1 = srdce · β2 = průdušky a cévy svalů · β3 = močový měchýř.**

❓ *Proč se LABA nesmí podávat v monoterapii?* → Uleví od příznaků, ale neléčí zánět — astma se pod ní zhoršuje a roste riziko úmrtí na těžký záchvat.

---

## 44 · Nepřímá sympatomimetika

**O čem to je:** nesedají na receptor, ale **zvyšují množství vlastního noradrenalinu** ve štěrbině.

**Tři mechanismy:** ① ↑ uvolňování přenašeče z vezikul ② ↓ jeho odbourávání (inhibice MAO) ③ **blokáda zpětného vychytávání (uptake 1)**.

| Léčivo | Podstatné |
|---|---|
| **Efedrin** | alkaloid chvojníku; působí **přímo i nepřímo**; ↑ tlak a srdeční činnost, centrálně stimuluje; dekongestant. ⚠️ **Prekurzor pro nelegální výrobu metamfetaminu** — proto omezený výdej |
| **Pseudoefedrin** | izomer efedrinu, méně centrálních účinků; dekongestant v přípravcích na nachlazení |
| **Amfetamin** | silně centrálně stimulační, dobře prochází HEB, **není odbouráván MAO**; jinde ve světě u ADHD, u nás droga |
| **Metylfenidát** | blokuje zpětné vychytávání NA a dopaminu → **léčba ADHD** |
| **Modafinil** | podobný mechanismus → **narkolepsie** |
| **Fentermin** | anorektikum — blokuje vychytávání NA, serotoninu i dopaminu → ↓ chuť k jídlu; NÚ hypertenze, nespavost, neklid, psychózy |

- **NÚ skupiny:** hypertenze, tachykardie a arytmie, nespavost, neklid, závislost, **tachyfylaxe** (vyčerpání zásob NA, viz O27). **KI:** hypertenze, ICHS, hypertyreóza, glaukom, současná léčba IMAO.

⚠️ **Tyraminová („sýrová") reakce — nejčastěji zkoušená interakce.** Tyramin vzniká kvašením bílkovinných potravin (**zrající sýry, červené víno, uzeniny**) a normálně ho rozloží MAO ve střevě a játrech. **Při léčbě inhibitory MAO se nerozloží, vstřebá se, vytěsní noradrenalin z vezikul → hypertenzní krize.**

❓ *Proč nesmí pacient na IMAO jíst zrající sýr?* → Nerozložený tyramin vytěsní noradrenalin → prudký vzestup tlaku až hypertenzní krize.

---

## 45 · Sympatolytika alfa

**O čem to je:** blokáda α receptorů — buď obou podtypů (diagnostika feochromocytomu), nebo selektivně α1 (dvě různé indikace: **tlak** a **prostata**).

- **Neselektivní α1+α2 — fenoxybenzamin (ireverzibilní), fentolamin (reverzibilní):** vazodilatace → ↓ periferní odpor a tlak. **Indikace: příprava k operaci a krátkodobá léčba feochromocytomu** (nádor chromafinních buněk dřeně nadledvin, nekontrolovaně vylučující katecholaminy). **NÚ: ortostatická hypotenze, výrazná reflexní tachykardie** (blokáda presynaptických α2 uvolní výdej NA na srdce), ucpaný nos.
- **Selektivní α1-blokátory — mechanismus:** blokáda α1 na cévách → vazodilatace; blokáda α1 v hrdle měchýře a prostatě → **uvolnění hladkého svalu a lepší odtok moči**.

| Léčiva | Indikace |
|---|---|
| **Prazosin, doxazosin, terazosin** | **hypertenze** — ale **ne lék první volby** (rezerva, nebo když je současně BHP) |
| **Tamsulosin, alfuzosin, silodosin** | **benigní hyperplazie prostaty** — uroselektivní (α1A), tlak ovlivňují méně |

- **NÚ:** **hypotenze po první dávce** (proto se začíná malou dávkou na noc), závratě, ortostáza, reflexní tachykardie, retrográdní ejakulace (tamsulosin), ucpaný nos. **KI:** ortostatická hypotenze, těžká aortální stenóza; opatrně před operací šedého zákalu (**floppy iris syndrom**).
- **α2-blokátor yohimbin** — dříve u erektilní dysfunkce, **dnes se nepoužívá**.

🔑 **Prazosinová skupina = tlak · tamsulosinová skupina = prostata. Obojí jsou α1-blokátory, liší se převažujícím místem účinku.**

❓ *Na co slouží fenoxybenzamin a fentolamin?* → Diagnostika a předoperační příprava u **feochromocytomu**.

---

## 46 · Sympatolytika beta (β-blokátory)

**O čem to je:** jedny z nejpoužívanějších léků na srdce a tlak — blokádou β receptorů srdce bije **pomaleji a slaběji** a hůř reaguje na stres a zátěž.

- **Mechanismus:** kompetitivní blokáda β receptorů. Tlak klesá dvěma cestami — **↓ minutový srdeční výdej** (β1 na srdci) a **↓ uvolňování reninu** v ledvinách (β1) → menší aktivace systému renin-angiotenzin. Při dlouhodobém podávání klesá i periferní odpor. Dále: **antiarytmický** efekt, **prodloužení diastoly** (lepší plnění věnčitých tepen → antiischemický efekt), snížení spotřeby kyslíku myokardem.
- ⚠️ **Účinky se projeví hlavně při zvýšené aktivitě sympatiku** (zátěž, stres) — v klidu je efekt menší.

| Generace | Charakteristika | Zástupci |
|---|---|---|
| **1.** | neselektivní (β1 i β2) | **propranolol**, pindolol, timolol (oční kapky) |
| **2.** | **β1-selektivní** („kardioselektivní") | **metoprolol, bisoprolol, atenolol, esmolol** (ultrakrátký, i.v.) |
| **3.** | neselektivní **s vazodilatací** (blokují i α1) | **karvedilol, labetalol** |
| **3.** | β1-selektivní s vazodilatací (přes NO) | **nebivolol**, betaxolol, celiprolol |

- **Farmakokinetika — proč záleží na rozpustnosti:** **lipofilní** (propranolol, metoprolol, karvedilol) mají výrazný **first-pass efekt** a **pronikají do CNS** (únava, noční můry, deprese) · **hydrofilní** (atenolol, sotalol) se vylučují **ledvinami v nezměněné podobě** → při renálním selhání se poločas prodlužuje a hrozí kumulace.
- **Indikace:** **hypertenze** · **angina pectoris** · **stav po infarktu** (snižují mortalitu a riziko reinfarktu) · **chronické srdeční selhání** (jen bisoprolol, karvedilol, metoprolol ZOK, nebivolol — a nasazují se **pomalou titrací od malé dávky**) · **supraventrikulární i komorové tachyarytmie** · **hypertyreóza a tyreotoxická krize** (tlumí příznaky ze sympatiku) · **glaukom** (timolol) · esenciální tremor, profylaxe migrény, trémafobie.
- **Nežádoucí účinky:** **bradykardie a AV blokáda**, zhoršení srdečního selhání při rychlé titraci, **bronchospasmus** (blokáda β2), studené končetiny a zhoršení klaudikací, únava, deprese, noční můry, ↓ HDL a ↑ triglyceridů, erektilní dysfunkce.
- ⚠️ **U diabetika: maskují varovné příznaky hypoglykemie** (třes, palpitace — zůstává jen pocení) a zpomalují zotavení z ní → nejsou lékem první volby u hypertenze u diabetika.
- **Kontraindikace:** **astma** (u CHOPN lze kardioselektivní opatrně), **sinusová bradykardie, AV blok II.–III. stupně**, dekompenzované srdeční selhání, těžká hypotenze, současné podání verapamilu/diltiazemu i.v. V graviditě nejsou teratogenní, ale mohou způsobit bradykardii a hypoglykemii plodu.

🔑 **Rebound fenomén: dlouhodobá blokáda up-reguluje β-receptory, náhlé vysazení proto vyvolá tachykardii, vzestup tlaku, anginózní bolest až infarkt — β-blokátory se vysazují VŽDY postupně.**

❓ *Proč nejsou β-blokátory první volbou u diabetika?* → Maskují hypoglykemii a zpomalují zotavení z ní.

---

## 47 · Myorelaxancia

**O čem to je:** léky na uvolnění svalu — buď mírné (bolestivý spazmus zad, **centrální**), nebo úplné ochrnutí k operaci (**periferní, nervosvalová blokáda**).

**Centrální myorelaxancia**
- **Mechanismus:** tlumí **polysynaptický reflexní oblouk** v míše a mozkovém kmeni, který udržuje patologicky zvýšené bolestivé napětí svalu → ↓ svalový tonus + analgetický efekt.
- **Zástupci:** **tolperison**, mefenoxalon, guaifenesin; **baklofen** (agonista GABA_B → otevření K⁺ kanálu, hyperpolarizace) a **benzodiazepiny/diazepam** (GABA_A), **tizanidin** (α2-agonista).
- **Indikace:** vertebrogenní bolestivý spazmus, myalgie po úraze, **spasticita** po CMP, u roztroušené sklerózy a míšních lézí (baklofen). **NÚ:** sedace, závratě, svalová slabost, sucho v ústech; u baklofenu ⚠️ **náhlé vysazení → křeče a halucinace**.

**Periferní myorelaxancia**
- **Presynapticky** (↓ výdej ACh): **botulotoxin**, **aminoglykosidová antibiotika** (tam je to nechtěný, potenciálně nebezpečný vedlejší účinek — pozor u pacienta s myasthenií).
- **Postsynapticky na N receptoru ploténky** — dvě protikladné strategie:

| | **Nedepolarizující** (kompetitivní) | **Depolarizující** |
|---|---|---|
| Vztah k ACh | **antagonisté** — obsadí receptor a brání depolarizaci | **agonista** — receptor aktivuje a drží **trvale depolarizovaný** |
| Zástupci | d-tubokurarin (historicky), **pankuronium, vekuronium, rokuronium, atrakurium** | **sukcinylcholin (suxamethonium)** |
| Nástup/trvání | minuty / desítky minut | **sekundy / ~5 minut** |
| **Antidotum** | **inhibitory AChE — neostigmin, edrofonium** (↑ ACh vytěsní blokátor); u rokuronia **sugammadex** | **antidotum neexistuje** — jen ventilace, dokud efekt neodezní |

- *(⚠️ Tvůj zdroj uvádí mezi zástupci „arkuronium" — správně **alkuronium**; dnes se stejně používají pankuronium, vekuronium, rokuronium, atrakurium.)*

🔑 **Pořadí ochrnutí (klasická otázka): ① oční svaly a víčka → ② žvýkací svaly → ③ svaly hlavy, krku a končetin → ④ mezižeberní a břišní svaly → ⑤ bránice (zástava dechu). Zotavení jde v opačném pořadí — bránice se obnoví jako první.**

⚠️ **Myorelaxans neovlivňuje vědomí ani vnímání bolesti** — pacient musí mít současně celkovou anestezii a **zajištěnou ventilaci**, jinak je při vědomí a ochrnutý.

- **Sukcinylcholin:** nejdřív **svalové záškuby (fascikulace)** na hrudníku a břiše, pak úplná paralýza; **ultrakrátký účinek**, protože ho rychle štěpí **pseudocholinesteráza**. ⚠️ Při **genetickém deficitu tohoto enzymu** (idiosynkrazie, viz O30) trvá apnoe hodiny. Další NÚ: **hyperkalemie** (riziko zástavy u popálenin a polytraumat), ↑ nitrooční tlak, svalové bolesti po výkonu.
- **Další NÚ skupiny:** uvolnění **histaminu** (hypotenze, bronchospasmus — hlavně u starších kurarimimetik), vliv na gangliové N receptory (nedepolarizující → bradykardie a hypotenze; sukcinylcholin → tachykardie a hypertenze).
- **Indikace:** doplněk celkové anestezie, **endotracheální intubace**, laryngoskopie a endoskopie, ochrana před úrazem při elektrokonvulzivní léčbě.

⚠️ **Maligní hypertermie** — vzácná, život ohrožující reakce na **sukcinylcholin a inhalační anestetika (halotan)**. Příčina: mutace **ryanodinového receptoru** → sarkoplazmatické retikulum nekontrolovaně vypouští Ca²⁺ a neumí ho vychytat zpět → trvalá kontrakce, prudce zrychlený metabolismus → **horečka, svalová rigidita, metabolická acidóza, hyperkalemie**. Bez léčby **umírá přes 60 %**. **Léčba: okamžitě dantrolen i.v.** (blokuje uvolňování Ca²⁺ z retikula) + chlazení a korekce acidózy. Dantrolen se používá i u **maligního neuroleptického syndromu**.

❓ *Jak se léčí maligní hypertermie?* → **Dantrolen i.v.**, okamžitě, ve stoupajících dávkách; současně chladit a korigovat acidózu.

---

## 48 · Lokální anestetika

**O čem to je:** znecitliví jen část těla **bez ztráty vědomí** — přesně to, co budeš denně používat při ošetření zubu.

- **Mechanismus:** reverzibilně blokují **napěťově řízené sodíkové kanály** zevnitř membrány → nevznikne akční potenciál → nervem se nešíří vzruch. Působí i na jiné vzrušivé tkáně (**srdce** — odtud kardiotoxicita a využití lidokainu jako antiarytmika).
- **Pořadí blokády vláken** (proč pacient cítí dotek, ale ne bolest): nejdřív **tenká vlákna** — vegetativní B (vazodilatace, teplo), pak **Aδ a C** (bolest, teplota), pak dotek a tlak, **nakonec silná Aα** (motorika). *(⚠️ Zdroj to má popsané zmateně jako „tenká myelinizovaná vlákna A a C" — **C vlákna jsou nemyelinizovaná**; platí, že tenčí vlákno se blokuje dřív a myelinizované dřív než nemyelinizované stejné tloušťky.)*
- **Chemicky jsou to slabé zásady** — v zaníceném (kyselém) prostředí se ionizují a hůř pronikají do nervu, **proto anestezie v zánětu často „nechytne"**.

| | **Estery** | **Amidy** |
|---|---|---|
| Zástupci | kokain, **prokain**, tetrakain, benzokain | **lidokain, trimekain (mezokain), bupivakain, levobupivakain, ropivakain, artikain, prilokain** |
| Odbourání | **plazmatická pseudocholinesteráza**, rychle | **v játrech přes CYP450**, pomaleji |
| Hlavní riziko | **alergie** (metabolit kyselina para-aminobenzoová) | **systémová toxicita** |

- **Vazokonstrikční přísada:** anestetika sama mírně **rozšiřují cévy** → rychle se odplaví. Přidaný **adrenalin** stáhne cévy → **prodlouží účinek, sníží krvácení v poli a sníží systémovou toxicitu** (látka se vstřebává pomaleji).
- ⚠️ **Lokální anestetikum se nikdy nepodává nitrožilně** — výjimkou je lidokain jako antiarytmikum při resuscitaci.

| Typ anestezie | Použití | Léčiva |
|---|---|---|
| **povrchová** | sliznice, rohovka, před vpichem | lidokain, tetrakain, benzokain |
| **infiltrační** | vstřik do tkáně v místě výkonu | většina |
| **svodná (blok)** | k nervu — paže, mezižeberní, **dentální nervy** | lidokain, artikain, mepivakain |
| **spinální / epidurální** | operace břicha a pánve, porod | lidokain, bupivakain |

- **Nežádoucí účinky — pro tebe nejdůležitější část.** ⚠️ **Aplikace v oblasti hlavy a krku má vyšší riziko** (bohaté prokrvení → rychlý vzestup hladiny, blízkost mozkových cév).
  - **CNS:** **nejdřív stimulace** (neklid, brnění kolem úst, kovová chuť, třes, **křeče**), **teprve pak útlum** až zástava dechu. Léčba: kyslík, **diazepam na křeče**, zajištění dýchání.
  - **Kardiovaskulárně:** ↓ dráždivost, vodivost i kontraktilita → bradykardie, hypotenze, zástava. ⚠️ **Nejvíc kardiotoxický je bupivakain.**
  - ⚠️ **Methemoglobinemie — způsobuje ji prilokain** (a benzokain); metabolit oxiduje hemoglobin → tkáně nedostanou kyslík, cyanóza nereagující na kyslík. **Léčba: methylenová (toluidinová) modř + kyslík.** Ve stomatologii klasická past.
  - **Alergie** — prakticky jen u **esterů**; od dermatitidy po anafylaxi (**lék volby adrenalin**).
  - **Z vazokonstrikční přísady:** ischemie a nekróza v akrálních oblastech, tachykardie, palpitace, hypertenze. ⚠️ **Opatrně u pacientů na IMAO a tricyklických antidepresivech** (zesílí účinek adrenalinu) a u neselektivních β-blokátorů.
- **Kontraindikace:** alergie na dané anestetikum, těžké poruchy vedení vzruchu, aplikace do infikované tkáně; adrenalinová přísada u nekompenzované hypertyreózy a těžké ICHS.

🔑 **Estery = alergie, rychlý rozklad v plazmě · amidy = systémová toxicita, odbourání v játrech. Bupivakain = nejvíc kardiotoxický, prilokain = methemoglobinemie.**

❓ *Proč anestezie často nezabere v zaníceném terénu?* → Kyselé pH ionizuje anestetikum (slabou zásadu) — v nabité formě neprojde membránou nervu.

---

## 49 · Celková anestetika — inhalační

**O čem to je:** úplné, ale **vratné vypnutí vědomí a vnímání bolesti** kvůli operaci; inhalační anestetika se vdechují jako plyn nebo páry (patří sem i „rajský plyn", který znáš ze stomatologie).

- **Mechanismus:** rozpouštějí se v lipidové části membrán neuronů a modulují iontové kanály (posilují **GABA_A**, tlumí NMDA) → útlum přenosu signálu. Účinnost roste s **rozpustností v tucích**.
- **Nejcitlivější struktury v pořadí:** retikulární formace → thalamická jádra a jejich spoje s kůrou (ztráta hodnocení bolesti) → mozková kůra → mícha. **Amnézie** po výkonu se přičítá útlumu hipokampu.

| Stadium | Co se děje |
|---|---|
| **1. analgezie** | pacient při vědomí, utlumený, mizí vnímání bolesti |
| **2. excitace (vagové)** | ztráta vědomí, neklid, nepravidelné dýchání — ⚠️ **dráždění n. vagus: bronchospasmus, zvracení, riziko zástavy srdce**; tímto stadiem se má projít co nejrychleji |
| **3. chirurgická tolerance** | pravidelné dýchání, mizí oční pohyby a rohovkový reflex, svalová relaxace — **tady se operuje** |
| **4. míšní paralýza** | útlum center dechu a oběhu, ochabnutí svěračů, kóma a smrt — **předávkování** |

**Dvě čísla, na která se ptají:**
- **Dělicí koeficient krev/plyn** — **nízký = rychlý nástup i rychlé probuzení** (látka se nehromadí v krvi a rychle sytí mozek); vysoký = pomalý nástup i odeznění.
- **MAC (minimální alveolární koncentrace)** = koncentrace, při které **50 % pacientů nereaguje pohybem na chirurgický řez** — míra účinnosti. **MAC klesá v kombinaci s N₂O**, v graviditě a ve stáří; roste u dětí a alkoholiků.

| Látka | Podstatné |
|---|---|
| **Halotan** | první halogenové; vazodilatace a hypotenze, ↓ srdeční výdej. ⚠️ **Maligní hypertermie a pohalotanová hepatitida** → **dnes se nepoužívá** |
| **Izofluran** | **dnes nejpoužívanější**; vazodilatace, riziko „**coronary steal**" — odklonění krve od ischemických oblastí myokardu |
| **Desfluran** | nejrychlejší nástup i odeznění, ale **dráždí dýchací cesty** (kašel, laryngospasmus) |
| **Sevofluran** | nedráždivý, příjemný — **úvod inhalací u dětí** |
| **N₂O (oxid dusný)** | rychlá indukce i odeznění; **v nízké koncentraci analgezie → základ inhalační sedace ve stomatologii**; nosný plyn snižující MAC ostatních. ⚠️ **Expozice nad 6 h inaktivuje vitamin B12 → útlum kostní dřeně**; nevhodný u anemie, chronická profesní expozice se pojí s vyšším rizikem potratů a vad plodu |
| **Xenon** | inertní, netoxický, nemetabolizuje se; **nejnižší rozpustnost v krvi → nejrychlejší nástup i probuzení**, neovlivňuje oběh (vhodný u kardiaků). Nevýhoda: cena |

- **Nežádoucí účinky:** útlum dechového centra a oběhu, vazodilatace a hypotenze, arytmie, pooperační nevolnost, hepatotoxicita (halotan), **maligní hypertermie** (viz otázka 47).
- **Interakce:** prohlubují a prodlužují blok nedepolarizujících myorelaxancií; s opioidy a benzodiazepiny se sčítá útlum dechu; **adrenalin při inhalační anestezii = riziko arytmií**.

| Antagonista | Co ruší |
|---|---|
| **Naloxon, naltrexon, nalmefen** | **opioidy** (útlum dechu a sedaci) |
| **Flumazenil** | benzodiazepiny |
| **Neostigmin, sugammadex** | nedepolarizující myorelaxancia |
| **Doxapram** | nespecifické dechové analeptikum (dráždí chemoreceptory) |
| **Dantrolen** | maligní hypertermie |

⚠️ **Naloxon je ANTAGONISTA opioidů** — starší studentské materiály ho někdy uvádějí jako agonistu, to je věcná chyba.

❓ *Co znamená MAC a co ji snižuje?* → Koncentrace, při níž 50 % pacientů nereaguje na řez; snižuje ji N₂O, gravidita, vyšší věk a opioidy.

---

## 50 · Celková anestetika — intravenózní

**O čem to je:** slouží hlavně k **rychlému a příjemnému úvodu** do anestezie (nástup ~1 minuta), případně ke krátkým výkonům.

- **Mechanismus:** většina posiluje **GABA_A** receptor (thiopental, propofol, etomidát, midazolam) → hluboký útlum CNS. **Ketamin je výjimka — blokuje NMDA receptory.**
- **Dělení:** **barbiturátová** (thiopental) a **nebarbiturátová** (propofol, etomidát, ketamin, midazolam).

| Léčivo | Podstatné |
|---|---|
| **Thiopental** | vysoce lipofilní → anestezie do 2 min, trvá 5–10 min. Probuzení je dáno **redistribucí do tuku**, ne eliminací → přetrvává ospalost („pobarbiturátová kocovina"), při opakovaných dávkách kumulace. **NÚ: útlum dechu, hypotenze.** Indikace: **úvod do anestezie** |
| **Propofol** | rychlý nástup i odeznění, minimum nevolnosti → **udržovací anestezie v infuzi a sedace na JIP**. NÚ: bolest při injekci, **hypotenze**, apnoe; ⚠️ dlouhodobě vysoké dávky → **propofolový infuzní syndrom** (metabolická acidóza, hyperkalemie, rhabdomyolýza, selhání oběhu) |
| **Etomidát** | oběhově nejšetrnější → **volba u nestabilního pacienta**. ⚠️ **Potlačuje syntézu kortikosteroidů** v nadledvinách (proto ne v infuzi, spojováno s vyšší mortalitou) |
| **Midazolam** | benzodiazepin — premedikace, sedace u endoskopie, anterográdní amnézie; antidotum **flumazenil** |
| **Ketamin** | ⚠️ **jediné anestetikum, které oběh STIMULUJE** (↑ tlak i tep), netlumí dýchání ani reflexy; navodí **disociovanou anestezii** (analgezie a amnézie při zachovaném vědomí). NÚ: **dysforie a halucinace** → kombinuje se s benzodiazepinem; ↑ nitrolební a nitrooční tlak, hypersalivace. Indikace: **výkony u dětí, medicína katastrof, popáleniny, šokový pacient** (dá se i.m.) |

- **Neuroleptanalgezie** — kombinace silného opioidu a neuroleptika, klasicky **fentanyl + droperidol**: sedace, analgezie a amnézie, ale ⚠️ **NE bezvědomí** — pacient je schopný spolupracovat (neurochirurgické výkony).
- ⚠️ **Nepleť si droperidol (neuroleptikum) s domperidonem (prokinetikum/antiemetikum)** — tuhle záměnu má i studentský zdroj.
- **Jak vypadá kombinovaná anestezie v praxi:** **premedikace** (atropin proti vagové bradykardii a salivaci + benzodiazepin) → **úvod** (thiopental nebo propofol) → **myorelaxace** (rokuronium/vekuronium) → **udržování** (inhalační anestetikum nebo propofol + opioid) → **antiemetikum** (ondansetron) → **pooperační analgezie** (opioidy, NSA).

🔑 **Thiopental = úvod · propofol = udržování · etomidát = nestabilní oběh · ketamin = výjimka, která oběh stimuluje.**

❓ *Proč se pacient po thiopentalu probudí za pár minut, i když se lék eliminuje hodiny?* → Kvůli **redistribuci** z mozku do svalů a tuku, ne kvůli odbourání.

---

## 51 · Hypnotika

**O čem to je:** léky na spaní — tři generace od nebezpečných barbiturátů přes benzodiazepiny k dnešní volbě, **Z-látkám**.

- **Insomnie** = usínání déle než 30 minut nebo přerušovaný spánek s časným probuzením; důsledkem je denní únava, poruchy pozornosti, chyby a nehody. **Akutní** < 3 měsíce (reakce na stres) · **chronická** ≥ 3 noci týdně po ≥ 3 měsíce · **primární** (bez organické příčiny) · **sekundární** (nemoc, léky, abúzus). ⚠️ Nespavost sama bývá **nežádoucím účinkem** psychostimulancií, antidepresiv, diuretik a β-blokátorů.
- **Mechanismus:** bdělost udržuje mozkový kmen přes histamin, dopamin, noradrenalin, serotonin a acetylcholin. Hypnotika buď **posílí to, co spánek navozuje** (GABA, melatonin, adenosin), nebo **utlumí to, co bdělost udržuje** (histamin, noradrenalin, ACh).
- **Zásady:** farmakoterapie hlavně u **akutní** insomnie (prevence přechodu do chronické), nejdřív **spánková hygiena a fytoterapie** (meduňka, heřmánek, chmel), pak nejnižší účinná dávka co nejkratší dobu; dlouhodobě hrozí tolerance, rebound nespavost a závislost.

**Barbituráty (1. generace)** — váží se na **vlastní vazebné místo GABA_A receptoru** a **přímo prodlužují otevření chloridového kanálu** (ve vysoké dávce ho otevřou i bez GABA — proto ta toxicita).
- Dělení: **krátkodobé** (thiopental, pentobarbital) · **střednědobé** (amobarbital) · **dlouhodobé** (**fenobarbital**, až 48 h).
- **NÚ:** útlum dechového centra, zmatenost, poruchy paměti, deprese; rychle vzniká **tolerance a závislost**, abstinenční příznaky (halucinace, arytmie, křeče); **potlačují REM spánek**. ⚠️ Jsou **silné induktory jaterních enzymů** → snižují účinek warfarinu, kontraceptiv a dalších léků. ⚠️ **Nemají antidotum** (na rozdíl od benzodiazepinů).
- Dnes už **ne jako hypnotika** — zůstávají jako antiepileptikum (fenobarbital) a anestetikum (thiopental).

**Benzodiazepiny (2. generace)** — viz otázka 52; na spaní se používají ty s krátkým poločasem, nevýhodou je zkrácení REM fáze a závislost.

**Z-látky (3. generace) — dnešní lék první volby.** Nebenzodiazepinoví **agonisté benzodiazepinového vazebného místa**, ale **selektivní pro podjednotku α1** → mají jen hypnotický efekt, **ne anxiolytický ani myorelaxační**; zkracují usínání, snižují počet probuzení a **nepotlačují REM spánek**; nižší riziko rebound fenoménu a interakcí.
- **Zolpidem** — potíže s **usínáním** (krátký poločas). **Zopiklon** — noční a časné probouzení; NÚ **ranní útlum** a ⚠️ **vylučuje se do slin → kovově hořká chuť v ústech** (zubařsky užitečný detail, pacienti si na to stěžují).
- **NÚ Z-látek:** bolest hlavy, ospalost, vzácně **parasomnie** (náměsíčnost, jídlo a řízení ve spánku), riziko pádů u seniorů. **KI:** myasthenia gravis, těžká respirační insuficience, spánková apnoe, těžké jaterní selhání.
- **Ostatní možnosti:** **melatonin** (u poruch rytmu a u seniorů), sedativní antidepresiva (trazodon, mirtazapin), antihistaminika 1. generace, nízké dávky sedativních antipsychotik.

🔑 **Barbituráty = toxické, bez antidota, potlačují REM, indukují enzymy. Z-látky = dnešní volba, REM nepotlačují.**

❓ *Na co si stěžuje pacient po zopiklonu?* → Na **kovovou hořkou chuť** v ústech (vylučuje se do slin) a ranní útlum.

---

## 52 · Benzodiazepiny

**O čem to je:** léky proti úzkosti a na spaní zároveň — od barbiturátů se liší mechanismem a hlavně tím, že **mají antidotum**.

- **Mechanismus (přesná formulace):** vážou se na **benzodiazepinové místo GABA_A receptoru, oddělené od místa pro GABA**, a **alostericky** (změnou tvaru receptoru) zvyšují **frekvenci otevírání chloridového kanálu** — ale **jen v přítomnosti GABA**. Proto mají mnohem širší terapeutické okno než barbituráty, které kanál otevřou i bez GABA.
- **Pět účinků:** **anxiolytický · sedativní · hypnotický · myorelaxační (centrálně) · antikonvulzivní.**

| Délka účinku | Poločas | Zástupci | Typické využití |
|---|---|---|---|
| **krátkodobé** | < 6 h | midazolam, cinolazepam, medazepam | **usínání**, premedikace |
| **střednědobé** | 6–24 h | **alprazolam**, bromazepam, oxazepam | úzkost, panická porucha |
| **dlouhodobé** | > 24 h | **diazepam, klonazepam** | úzkostné stavy, křeče, spasticita, odvykací stavy |

- ⚠️ **Z poločasu plyne indikace: krátký poločas → na spaní · dlouhý poločas → na úzkost.**
- **Indikace:** úzkostné a panické poruchy, nespavost, **epileptický status (diazepam, midazolam i.v.)**, febrilní křeče, alkoholový odvykací stav a delirium tremens, svalové spazmy, premedikace před výkonem.
- **Farmakokinetika:** perorální dostupnost blízká 100 %, silná vazba na bílkoviny, lipofilní → snadno přes HEB, metabolizace v játrech (**oxazepam a lorazepam se jen konjugují → bezpečnější u jaterního postižení a u seniorů**).
- **Nežádoucí účinky:** denní útlum a spavost, zhoršená pozornost a psychomotorika (⚠️ **řízení, zvlášť s alkoholem**), **anterográdní amnézie**, závratě a pády u seniorů, **zkrácení REM spánku**, paradoxní reakce (neklid, agrese) u dětí a seniorů; **tolerance, fyzická i psychická závislost** a **rebound nespavost/úzkost** po vysazení (proto se vysazují postupně).
- **Kontraindikace:** **myasthenia gravis**, těžká respirační insuficience a spánková apnoe, těžké jaterní selhání, akutní intoxikace alkoholem a tlumivými látkami, I. trimestr gravidity.
- **Antidotum: flumazenil** (kompetitivní antagonista) — pozor, má krátký poločas (riziko návratu útlumu) a u epileptiků může vyvolat křeče.

🔑 **Alostericky zvyšují frekvenci otevírání Cl⁻ kanálu, ale jen v přítomnosti GABA — proto jsou bezpečnější než barbituráty. Antidotum flumazenil.**

❓ *Proč mají benzodiazepiny širší terapeutické okno než barbituráty?* → Bez GABA nic neudělají; barbituráty kanál ve vysoké dávce otevřou samy → zástava dechu.

---
