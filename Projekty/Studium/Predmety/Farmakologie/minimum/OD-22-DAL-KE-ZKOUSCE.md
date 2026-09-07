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

## 53 · Antiepileptika

**O čem to je:** léky proti záchvatům, kdy neurony vystřelí naráz a nekontrolovaně. Jádro otázky = **tři mechanismy** + konkrétní léky s typickými nežádoucími účinky.

- **Epileptický záchvat** = přechodný projev abnormální, nadměrné neuronální aktivity (ložiskové nebo generalizované). **Epilepsie** = ① ≥ 2 nevyprovokované záchvaty s odstupem > 24 h, nebo ② jeden záchvat s vysokým rizikem dalšího, nebo ③ diagnóza epileptického syndromu. Postihuje **0,5–1 % populace**.
- **Klasifikace ve dvou krocích:** typ **záchvatu** (fokální / generalizovaný / neznámý začátek) → typ **epilepsie**. Příčiny: genetická, strukturální (nádor, úraz, CMP), imunitní, zánětlivá, metabolická, neznámá. Diagnostika EEG, MR, PET.

**Tři mechanismy účinku (řekni je v tomhle pořadí):**
- ① **Snížení excitability a výdeje přenašečů** — blokáda **Na⁺ kanálů** (fenytoin, karbamazepin, lamotrigin), blokáda **Ca²⁺ kanálů** (etosuximid, gabapentin, pregabalin), vazba na **synaptický vezikulární protein** (levetiracetam).
- ② **Posílení tlumivého GABA systému** — alosterická aktivace GABA_A (**benzodiazepiny, barbituráty**) nebo blokáda odbourávání GABA (**valproát, vigabatrin**).
- ③ **Potlačení excitační glutamátové transmise** — ↓ výdej glutamátu (gabapentin), blokáda glutamátových receptorů (**topiramát**).

🔑 **Status epilepticus: záchvat trvající > 5 minut bez návratu vědomí → lék volby diazepam (i.v./rektálně) nebo midazolam bukálně. Trvá-li i po adekvátní dávce > 30 minut → rozvinutý status: i.v. fenytoin, valproát nebo levetiracetam; při selhání navozené kóma s monitorací EEG.**

- **Zásady léčby:** začíná se **monoterapií** v nízké dávce a titruje se; kombinace až při selhání (víc NÚ a interakcí). Kontrola dynamická (počet záchvatů, EEG, jaterní testy, krevní obraz) i kinetická (**TDM** — účinek koreluje s hladinou lépe než s dávkou). ⚠️ **Vysazovat jen postupně — náhlé vysazení vyvolá status epilepticus.**
- **Nežádoucí účinky:** **typ A (na dávce)** — ospalost, zpomalení, poruchy paměti, **ataxie**, dvojité vidění, třes, změny hmotnosti, **hyperplazie dásní**, polyneuropatie, megaloblastická anemie (porucha metabolismu kyseliny listové), osteoporóza · **typ B** — alergie, **poškození jater, útlum krvetvorby** (vyžadují okamžité vysazení) · **typ C** — **teratogenita, defekty neurální trubice**. ⚠️ **Intoxikace nemá antidotum**, léčí se symptomaticky.
- ⚠️ **Hyperplazie dásní u pacienta na fenytoinu je učebnicový zubařský nález** — na tohle se tě u zkoušky ze zubního lékařství ptát budou.

| Klasické antiepileptikum | Mechanismus, indikace, NÚ |
|---|---|
| **Fenobarbital** (a **primidon**, který se na něj mění) | alostericky GABA_A, prodlouží otevření Cl⁻ kanálu; generalizované tonicko-klonické záchvaty. NÚ: sedace, poruchy paměti, deprese, **silná indukce jaterních enzymů** |
| **Fenytoin** | prodlužuje inaktivaci **Na⁺ kanálů**; fokální i generalizované záchvaty, i.v. u status epilepticus. ⚠️ **Kinetika 0. řádu** — nad určitou dávkou koncentrace prudce vyskočí (saturační kinetika, viz O12). NÚ: **nystagmus, diplopie, ataxie, hyperplazie dásní, hirsutismus, zhrubnutí rysů**, hepatotoxicita, indukce CYP |
| **Karbamazepin** | prodlužuje inaktivaci Na⁺ kanálů; **fokální záchvaty**, **neuralgie trigeminu** (!), antimanický efekt. NÚ: závratě, hyponatremie (SIADH), hepatotoxicita, **útlum krvetvorby**, kožní reakce; **indukuje enzymy** |
| **Valproát** | blokuje odbourávání GABA + Na⁺ kanály → **širokospektrý** (fokální i generalizované, absence). NÚ: **přírůstek hmotnosti, hepatotoxicita, trombocytopenie, hyperamonemická encefalopatie**, syndrom polycystických ovarií. ⚠️ **Nejsilnější teratogen mezi antiepileptiky — u žen ve fertilním věku se nepoužívá** |
| **Etosuximid** | blokáda T-typu Ca²⁺ kanálů v thalamu — **lék volby u absencí** |

| Nové antiepileptikum | Podstatné |
|---|---|
| **Lamotrigin** | Na⁺ kanály + ↓ glutamát; **první volba u fokálních i generalizovaných záchvatů, vhodný v graviditě**. ⚠️ NÚ: **kožní vyrážka až Stevensův-Johnsonův syndrom / toxická epidermální nekrolýza** → nasazuje se velmi pomalou titrací |
| **Levetiracetam** | vazba na vezikulární protein SV2A; **první volba**, minimum interakcí (nemetabolizuje se v játrech). NÚ: podrážděnost, deprese, vzácně cytopenie |
| **Gabapentin, pregabalin** | blokáda Ca²⁺ kanálů; epilepsie a hlavně **neuropatická bolest**, pregabalin i **generalizovaná úzkostná porucha**. NÚ: závratě, otoky, přírůstek hmotnosti; vylučují se ledvinami beze změny |
| **Benzodiazepiny** (klonazepam, klobazam, diazepam, midazolam) | akutní léčba záchvatu a status epilepticus; **ne na dlouhodobou léčbu** (tolerance) |

- **Nová antiepileptika mají kinetickou výhodu:** minimální vazba na bílkoviny, nemetabolizují se přes CYP → **málo lékových interakcí**.
- **Gravidita:** ⚠️ **léčbu NEVYSAZOVAT** (záchvat ohrožuje plod víc než lék) — přejít na **monoterapii, ideálně lamotrigin nebo levetiracetam**, valproátu se vyhnout, přidat **kyselinu listovou**. Kojení není kontraindikací.

❓ *Jaký nález na dásních spojíš s antiepileptikem?* → **Hyperplazie dásní u fenytoinu** (a zhoršuje ji špatná ústní hygiena).

---

## 54 · Antiparkinsonika

**O čem to je:** ubývají dopaminové neurony, chybí „brzda" pohybu a převládne cholinergní „plyn" — proto třes a ztuhlost. Léky buď dopamin doplní, nebo utlumí přebývající cholinergní stranu.

- **Patofyziologie (uměj vysvětlit plynule):** zaniká dopaminergní dráha ze **substantia nigra do striata**. Zpočátku zbylé neurony kompenzují, takže nemoc je němá. Jak dopaminu ubývá, klesá jeho **tlumivý vliv na striatum**, kde jsou excitační **cholinergní** neurony → **relativní převaha cholinergního systému** → třes a rigidita. ⚠️ **Klinicky se nemoc projeví, až když ve striatu chybí 80 % dopaminu.**
- **Příznaky:** klidový třes, svalová rigidita, **bradykineze** (zpomalení pohybu), posturální nestabilita a porucha chůze; k tomu deprese, poruchy spánku, zácpa, později demence. Podobný obraz umí vyvolat i **antipsychotika** (blokádou D2 ve striatu — polékový parkinsonský syndrom).
- ⚠️ **Léčba je pouze symptomatická — postup nemoci nezastaví.** Cílem je obnovit rovnováhu mezi chybějícím dopaminem a převažujícím acetylcholinem.

🔑 **L-DOPA + karbidopa — nejelegantnější myšlenka otázky.** Dopamin sám **neprojde hematoencefalickou bariérou**, proto se podává jeho prekurzor **levodopa (L-DOPA)**, který projde. Jenže L-DOPA se z 95 % dekarboxyluje na dopamin **už ve střevě a v periferii** — do mozku nedojde a v těle způsobí nauzeu, zvracení a ortostatickou hypotenzi. **Karbidopa (nebo benserazid) je inhibitor dekarboxylázy, který sám do mozku neprojde** → zablokuje přeměnu jen v periferii, takže se L-DOPA dostane až do mozku a teprve tam se změní na dopamin.

- **L-DOPA** je **nejúčinnější** lék (odpověď u ~80 %), ale ⚠️ **po ~2–5 letech vzniká „wearing-off"** (zkracující se doba účinku), **dyskineze** závislé na dávce, fenomén **on-off** a psychiatrické NÚ (zmatenost, halucinace). Proto se u mladších pacientů začíná spíš agonisty.

| Skupina | Léčiva a mechanismus |
|---|---|
| **Inhibitory COMT** | **entakapon, tolkapon** — brání periferní degradaci L-DOPA → prodlouží její účinek; jen jako **doplněk k L-DOPA**. NÚ: průjem, oranžová moč, tolkapon hepatotoxický |
| **Inhibitory MAO-B** | **selegilin, rasagilin** — chrání dopamin ve striatu před odbouráním; monoterapie v časné fázi nebo doplněk. ⚠️ Kombinace s SSRI/opioidy → riziko **serotoninového syndromu** |
| **Agonisté D2 receptorů** | **pramipexol, ropinirol, rotigotin** (náplast), **apomorfin** (podkožně při „off" stavech) — účinek 8–12 h, méně dyskinezí → **preferují se u mladších pacientů**. NÚ: ⚠️ **impulzivní chování (patologické hráčství, nakupování, hypersexualita)**, náhlé usnutí, halucinace, otoky |
| **Uvolňovače dopaminu** | **amantadin** — navíc **antagonista NMDA** → tlumí dyskineze po L-DOPA; méně účinný, ale dobře snášený, vzniká tolerance |
| **Anticholinergika** | **biperiden, procyklidin** — blokáda muskarinových receptorů ve striatu; hlavně na **třes** a u polékového parkinsonismu. ⚠️ **Nevhodné u seniorů** (zmatenost, poruchy paměti, retence moči, glaukom) |

❓ *Proč se levodopa nepodává samotná?* → Dekarboxyluje se na dopamin už v periferii — do mozku se nedostane a působí nauzeu a hypotenzi; karbidopa tuhle přeměnu mimo mozek zablokuje.

---

## 55 · Neuroleptika (antipsychotika)

**O čem to je:** léky na psychózu (halucinace = vjemy bez podnětu, bludy = nevyvratitelné mylné přesvědčení). Fungují blokádou **dopaminových receptorů** — a z toho plynou i skoro všechny jejich nežádoucí účinky.

- **Mechanismus:** antagonismus na **D2 receptorech**, u atypických navíc silná blokáda **5-HT2**. Antipsychotický efekt nastupuje **až po týdnech**, sedace hned.

🔑 **Čtyři dopaminergní dráhy — z nich plyne všechno:** **mezolimbická** → blokáda = **žádoucí antipsychotický efekt** · **nigrostriatální** → blokáda = **extrapyramidové příznaky** · **tuberoinfundibulární** → blokáda = **hyperprolaktinemie** (galaktorea, amenorea, gynekomastie, sexuální dysfunkce) · **area postrema (CTZ)** → blokáda = **antiemetický efekt**.

| Další blokovaný receptor | Nežádoucí účinek |
|---|---|
| **α1** | ortostatická hypotenze, závratě, ucpaný nos, sexuální dysfunkce |
| **muskarinový** | **sucho v ústech**, zácpa, retence moči, mydriáza, tachykardie, zhoršení paměti |
| **H1** | sedace, **přírůstek hmotnosti** |

- **Typická (1. generace)** — silná blokáda D2, hodně extrapyramidových účinků, působí hlavně na **pozitivní** příznaky:
  - **sedativní** — **chlorpromazin** (vůbec první antipsychotikum, původně antihistaminikum), levomepromazin,
  - **incizivní** — **haloperidol** (nejpoužívanější, levný, i.m. i i.v.), flufenazin (depotní i.m. à 4 týdny), perfenazin, droperidol.
- **Atypická (2. generace)** — vyšší poměr blokády 5-HT2 : D2 → **výrazně méně extrapyramidových příznaků** a působí i na **negativní příznaky** (apatie, oploštění emocí, sociální stažení, hypobulie):

| Skupina | Zástupci a zvláštnosti |
|---|---|
| **selektivní D2 antagonisté** | **sulpirid, amisulprid** (⚠️ nejvyšší **hyperprolaktinemie**), **tiaprid** (neklid a agrese u seniorů a dětí, odvykací stavy) |
| **SDA** (serotonin-dopaminoví antagonisté) | **risperidon, paliperidon** — akutní i udržovací léčba schizofrenie; ve vyšší dávce zase extrapyramidové NÚ |
| **MARTA** (multireceptoroví) | **klozapin, olanzapin, kvetiapin** — silná blokáda H1 → **sedace a nárůst hmotnosti, metabolický syndrom**; ⚠️ **klozapin: agranulocytóza (nutné pravidelné kontroly krevního obrazu), ale nejúčinnější u farmakorezistentní schizofrenie** |
| **parciální agonisté** | **aripiprazol** — „stabilizátor dopaminu": při nadbytku působí jako antagonista, při nedostatku jako agonista; málo sedace i prolaktinu |

- **Indikace:** schizofrenie a schizoafektivní porucha, manická epizoda, těžká agitovanost a agrese, psychotická deprese; mimo psychiatrii **antiemetikum** (haloperidol, tiaprid), součást neuroleptanalgezie, delirium.
- **Nežádoucí účinky — jádro doplňujících otázek:**
  - **extrapyramidové:** **akutní dystonie** (křeč svalů krku a očí, hodiny až dny — léčba **biperiden**) → **akatizie** (neklid, nemůže vydržet sedět) → **polékový parkinsonismus** (týdny) → ⚠️ **tardivní dyskineze** (po měsících až letech, mimovolní pohyby úst a jazyka, **často ireverzibilní**),
  - **metabolické:** přírůstek hmotnosti, diabetes, dyslipidemie (hlavně olanzapin, klozapin),
  - **kardiální:** **prodloužení QT intervalu** → riziko torsade de pointes,
  - **hematologické:** **agranulocytóza u klozapinu**,
  - ⚠️ **maligní neuroleptický syndrom** — vzácný, život ohrožující: **horečka, svalová rigidita, porucha vědomí, nestabilita oběhu, vysoká CK**. **Léčba: okamžitě vysadit neuroleptikum + dantrolen a bromokriptin, chlazení, hydratace.**
- **Kontraindikace:** kóma a útlum CNS, Parkinsonova nemoc (kromě kvetiapinu a klozapinu), prodloužené QT, u klozapinu porucha krvetvorby; opatrně u demence (↑ mortalita).

❓ *Jaký je rozdíl mezi typickými a atypickými antipsychotiky?* → Atypika blokují víc 5-HT2 než D2 → méně extrapyramidových NÚ a účinek i na **negativní** příznaky; platí za to metabolickými NÚ.

---

## 56 · Antidepresiva — tricyklická (TCA), inhibitory MAO

**O čem to je:** deprese souvisí s nedostatkem monoaminů (serotonin, noradrenalin, dopamin) v mozku. Tahle otázka pokrývá **dvě nejstarší skupiny** — účinné, ale rizikové.

- **Deprese — příznaky ve skupinách:** **psychické** (skleslá nálada, ztráta zájmu a energie, pocity viny, **sebevražedné myšlenky**) · **somatické** (nechutenství, poruchy spánku, zácpa, sexuální dysfunkce, **suchost sliznic**) · **behaviorální** (zpomalení, pláč, izolace) · **kognitivní** (nesoustředěnost, nerozhodnost) · **psychotické** (bludy, halucinace). Postižené struktury: prefrontální kůra, **hipokampus, amygdala**, limbický systém.
- **Monoaminová hypotéza:** klesá nabídka NA, serotoninu a dopaminu + dochází k **down-regulaci receptorů**. Všechna antidepresiva **zvyšují nabídku monoaminů** třemi cestami: ① blokáda **zpětného vychytávání** ② inhibice **odbourávacích enzymů** ③ přímé působení na receptory. ⚠️ **Účinek nastupuje až za 2–4 (až 6) týdnů** — hladina přenašeče stoupne hned, ale klinické zlepšení vyžaduje adaptaci receptorů. Tohle chtějí slyšet.

**Tricyklická antidepresiva (TCA)** — **imipramin, amitriptylin, klomipramin, nortriptylin, dosulepin**.
- **Mechanismus:** neselektivní blokáda zpětného vychytávání **noradrenalinu i serotoninu**.
- **NÚ si odvoď z blokovaných receptorů, neuč se je jako seznam:** **muskarinové** → sucho v ústech, zácpa, retence moči, poruchy akomodace, u seniorů **delirium** · **α1-adrenergní** → ortostatická hypotenze, závratě, reflexní tachykardie · **H1-histaminové** → sedace a **přírůstek hmotnosti**.
- ⚠️ **Hlavní bezpečnostní problém: kardiotoxicita** (blokáda Na⁺ kanálů → prodloužení QRS, arytmie) → **vysoká letalita při předávkování** (a předávkuje se právě suicidální pacient). Dále snižují práh pro křeče.
- **KI:** čerstvý infarkt a poruchy vedení, glaukom s úzkým úhlem, hyperplazie prostaty, současně IMAO; ⚠️ **s alkoholem hrozí útlum dechu**. Procházejí placentou i do mléka. Vysazovat **postupně** (jinak závratě, nauzea, třes).
- **Indikace:** těžká deprese, **neuropatická bolest a profylaxe migrény** (amitriptylin v nízké dávce), obsedantně-kompulzivní porucha (klomipramin), noční pomočování u dětí.

**Inhibitory MAO (IMAO)** — **MAO-A** (v neuronech a **střevní stěně**) odbourává serotonin, NA i tyramin; **MAO-B** (hlavně v mozku) hlavně dopamin.
- ⚠️ **Dvě interakce, kvůli kterým se prakticky nepoužívají:** ① **tyraminová („sýrová") hypertenzní krize** — zrající sýry, uzeniny, červené víno (viz otázka 44) ② **serotoninový syndrom** při kombinaci se SSRI, tramadolem, triptany.
- **Dnes se používá už jen moklobemid** — **reverzibilní selektivní inhibitor MAO-A** (RIMA), u kterého je riziko tyraminové reakce výrazně nižší; indikace deprese a **sociální fobie**. NÚ: nespavost, ortostatická hypotenze, závratě. Starší ireverzibilní (tranylcypromin, fenelzin) vyžadovaly přísnou dietu. ⚠️ **Před převodem z IMAO na jiné antidepresivum je nutná pauza (u ireverzibilních 2 týdny).**

🔑 **TCA = účinná, ale kardiotoxická a letální při předávkování · IMAO = nebezpečné interakce (sýr, serotoninergní léky).**

❓ *Proč antidepresivum nezabere hned?* → Hladina přenašeče stoupne během hodin, ale klinický efekt vyžaduje **adaptaci (down-regulaci) receptorů** — 2–4 týdny.

---

## 57 · Antidepresiva — SSRI, SNRI a atypická

**O čem to je:** novější generace, dnes **lék první volby** u deprese i úzkosti — cílenější mechanismus, méně nežádoucích účinků.

- **SSRI (selektivní inhibitory zpětného vychytávání serotoninu)** — **fluoxetin, sertralin, citalopram, escitalopram, paroxetin, fluvoxamin**.
  - **Mechanismus:** selektivní blokáda serotoninového transportéru (SERT) → víc serotoninu v synapsi.
  - **Indikace:** **deprese, generalizovaná úzkostná porucha, panická porucha, OCD, PTSD, sociální fobie, bulimie**, předčasná ejakulace.
  - **Proč se prosadily:** dobrá snášenlivost, **bezpečné při předávkování** (na rozdíl od TCA), nezvyšují výrazně hmotnost.
  - **NÚ:** nauzea a průjem (na začátku), **sexuální dysfunkce** (nejčastější důvod vysazení), nespavost nebo naopak sedace, **hyponatremie u seniorů (SIADH)**, ⚠️ **zvýšená krvácivost z horního GIT** — zvlášť v kombinaci s NSA nebo antikoagulancii (serotonin je potřeba k agregaci destiček); na začátku léčby **přechodné zvýšení úzkosti a suicidálního rizika u mladých**.
  - **Interakce:** blokují **CYP450** (hlavně fluoxetin a paroxetin — CYP2D6) → zvyšují hladiny jiných léků.
- ⚠️ **Dvě zkratky, které chtějí slyšet:**
  - **Syndrom z vysazení — FINISH:** **F**lu-like (jako chřipka) · **I**nsomnia · **N**ausea · **I**mbalance (nerovnováha, závratě) · **S**ensory disturbances (brnění, „elektrické šoky") · **H**yperarousal (neklid). Proto se vysazuje pomalu.
  - **Serotoninový syndrom** (při kombinaci serotoninergních léků): **horečka, pocení, tachykardie, třes, myoklonus, hyperreflexie, zmatenost** až kóma. Léčba: vysadit vše, chladit, benzodiazepiny, v těžkém případě cyproheptadin.
- **SNRI (serotonin a noradrenalin)** — **venlafaxin, duloxetin, milnacipran**: deprese, úzkostné poruchy, **chronická a neuropatická bolest** (duloxetin i u diabetické neuropatie a stresové inkontinence). NÚ jako SSRI + při vyšších dávkách **hypertenze** a pocení. Vysazovat postupně (venlafaxin má obzvlášť nepříjemný syndrom z vysazení).
- **Atypická antidepresiva:**

| Léčivo | Mechanismus a zvláštnost |
|---|---|
| **Bupropion** | inhibitor vychytávání **noradrenalinu a dopaminu**; **nezpůsobuje sexuální dysfunkce**, ⚠️ **používá se i k odvykání kouření**. NÚ: nespavost, neklid, **snižuje práh pro křeče** |
| **Mirtazapin** | antagonista **α2** a 5-HT2/5-HT3 → antidepresivní + **sedativní a anxiolytický**, rychlý nástup; vhodný u deprese s úzkostí a nespavostí. NÚ: **sedace a přírůstek hmotnosti** |
| **Trazodon** | blokáda 5-HT2 + slabá inhibice vychytávání; v nízké dávce **hypnotikum**. NÚ: sedace, ortostáza, vzácně priapismus |
| **Reboxetin, atomoxetin** | selektivní inhibitory vychytávání noradrenalinu; **atomoxetin se používá u ADHD** |

🔑 **SSRI = dnešní lék volby, bezpečné při předávkování; cenou jsou sexuální dysfunkce, hyponatremie a krvácivost.**

❓ *Proč jsou SSRI rizikové spolu s NSA?* → Blokádou vychytávání serotoninu ochudí destičky o serotonin → horší agregace → **krvácení do GIT**, které NSA ještě zesílí.

---

## 58 · Anxiolytika, stabilizátory nálady

**O čem to je:** dvě propojená témata — léky na **kolísání nálady** u bipolární poruchy (hlavně lithium) a léky proti **úzkosti**.

- **Bipolární porucha:** **typ I** (~1 % populace) — depresivní i **plně vyjádřené manické** epizody · **typ II** — depresivní a jen mírnější **hypomanické** epizody *(zdroj uvádí až 5 % populace)*. **Manická epizoda:** zvýšená aktivita, nadnesená nálada, přehnané sebevědomí, bludy o mimořádných schopnostech, podrážděnost až agrese. **Smíšená epizoda:** podrážděnost, úzkost, impulzivita, sebevražedné myšlenky.
- **Lithium** — základní stabilizátor nálady.
  - **Mechanismus není přesně znám** (ovlivňuje druhé posly — inositolový cyklus a GSK-3).
  - **Indikace:** akutní mánie a hlavně **dlouhodobá profylaxe** epizod; ⚠️ **jako jediný prokazatelně snižuje riziko sebevraždy**.
  - ⚠️ **Velmi úzké terapeutické okno → nutné TDM** (měření hladin). **NÚ:** třes rukou, **polyurie a žíznivost** (nefrogenní diabetes insipidus), GIT potíže, přírůstek hmotnosti, poruchy paměti, **hypotyreóza**, dlouhodobě poškození ledvin. **Intoxikace:** zvracení, průjem, hrubý třes, ataxie, zmatenost, křeče.
  - ⚠️ **Interakce, které jsou život ohrožující:** **thiazidová diuretika, ACE inhibitory a NSA zvyšují hladinu lithia** (ledvina ho zpětně vstřebává místo sodíku) → intoxikace. Stejně tak dehydratace a nízkosolná dieta. **KI:** těžká renální insuficience, gravidita (Ebsteinova anomálie srdce plodu).
  - **Alternativy a doplňky:** antiepileptika **valproát** (u mánie), **lamotrigin** (u bipolární deprese), **karbamazepin**; antipsychotika **olanzapin, kvetiapin, aripiprazol**.
- **Úzkostné poruchy** — nejčastější duševní poruchy vůbec. ⚠️ **Rozdíl, který chtějí slyšet: u úzkosti nedokáže člověk určit reálnou příčinu; u fobie si uvědomuje, že strach je nepřiměřený, ale přesto mu podléhá.**

| Porucha | Charakteristika |
|---|---|
| **panická porucha** | náhlý intenzivní záchvat úzkosti bez reálného nebezpečí (bušení srdce, dušnost, strach ze smrti) |
| **agorafobie** | strach z míst, odkud je obtížný únik nebo nedostupná pomoc |
| **sociální fobie** | strach ze situací, kde může být člověk hodnocen |
| **specifické fobie** | výšky, létání, pavouci |
| **generalizovaná úzkostná porucha** | trvalé napětí a negativní očekávání |
| **OCD** | vtíravé myšlenky (**obsese**) + nutkavé úkony (**kompulze**) — strach z nákazy a mytí rukou |
| **PTSD** | po traumatické události — znovuprožívání, vyhýbání se, hyperarousal |

- **Anxiolytika** (⚠️ **nemají antipsychotický efekt** — v tom se liší od neuroleptik):
  - **Benzodiazepiny** (alprazolam, klonazepam, oxazepam, diazepam) — **rychlý účinek**, proto se hodí na akutní úzkost a překlenutí prvních týdnů, než zaberou antidepresiva. ⚠️ **Jen krátkodobě** — tolerance, závislost, syndrom z vysazení; ⚠️ **s alkoholem útlum dechového centra**.
  - **SSRI a SNRI** — **léčba první volby všech úzkostných poruch** (kromě specifických fobií) díky lepšímu poměru přínos/riziko.
  - **Ostatní:** **hydroxyzin** (antihistaminikum, bez závislosti), **pregabalin** (generalizovaná úzkostná porucha), **buspiron** (parciální agonista 5-HT1A, nástup týdny), **β-blokátory** na somatické projevy trémy (třes, tachykardie).

🔑 **Lithium = úzké terapeutické okno, TDM, pozor na thiazidy/NSA/ACEI a dehydrataci. Snižuje suicidalitu.**

❓ *Proč thiazidové diuretikum ohrožuje pacienta na lithiu?* → Při ztrátě sodíku ho ledvina zadržuje a spolu s ním zpětně vstřebává i lithium → hladina stoupne do toxického pásma.

---

## 59 · Farmakoterapie Alzheimerovy choroby, nootropika

**O čem to je:** hromadí se škodlivá bílkovina a odumírají **cholinergní** neurony — léky proto šetří zbylý acetylcholin, nebo tlumí glutamátovou toxicitu.

- **Klinicky:** postupná porucha **paměti** (nejdřív krátkodobé), ztráta orientace, úbytek intelektových a sociálních dovedností, emoční nestabilita, agitovanost, deprese, poruchy cyklu spánek–bdění.
- **Patologie — dvě věci, které musíš říct:** ① **extracelulární plaky β-amyloidu** a intracelulární **neurofibrilární klubka z hyperfosforylovaného tau proteinu** `[doplněno]`, ubývají neurony v **hipokampu a bazálním předním mozku** ② **cholinergní deficit** v oblastech pro paměť — a **z tohohle bodu vychází celá léčba**.
- **Kognitiva — inhibitory cholinesteráz** (šetří zbylý acetylcholin):

| Léčivo | Podstatné |
|---|---|
| **Donepezil** | selektivní inhibitor AChE, 1× denně; lehká až středně těžká forma |
| **Rivastigmin** | blokuje **AChE i butyrylcholinesterázu**, selektivně v kůře a hipokampu; i **náplast** (méně GIT potíží) |
| **Galantamin** | inhibice AChE + alosterická modulace nikotinových receptorů |

- **NÚ kognitiv (jsou to cholinergní účinky):** nauzea, zvracení, průjem, **bradykardie a synkopy**, křeče, ↑ salivace, nespavost. **KI:** bradykardie a poruchy vedení, aktivní vřed, astma, obstrukce močových cest.
- **Memantin** — **nekompetitivní antagonista NMDA (glutamátových) receptorů**: brání excitotoxicitě z nadměrné stimulace glutamátem. **Indikace: středně těžká až těžká forma**; s inhibitory AChE má **aditivní efekt**. Dobře snášený, NÚ: závratě, bolest hlavy, zmatenost.
- ⚠️ **Léčba je symptomatická — zpomalí progresi, nezastaví ji.**
- **Nootropika** — **piracetam, vinpocetin**, vazoaktivní látky (pentoxifylin, cinnarizin, flunarizin): mají zvyšovat obrat kyslíku a glukózy v mozku, ⚠️ **ale jejich účinek nebyl prokázán kontrolovanou randomizovanou studií** — v praxi je nahradily inhibitory AChE.
- ⚠️ **Přínos vitaminu E a Ginkgo biloba se v kontrolovaných studiích neprokázal** — typická doplňující otázka.

🔑 **β-amyloid a tau = strukturální podstata · cholinergní deficit = to, co umíme léčit. Inhibitory AChE u lehké/střední formy, memantin u střední/těžké.**

❓ *Proč mají kognitiva GIT nežádoucí účinky a bradykardii?* → Zvyšují acetylcholin **všude**, nejen v mozku — tedy i parasympatické účinky na srdce a střevo.

---

## 60 · Opium a jeho alkaloidy

**O čem to je:** nejsilnější analgetika, jaká máme — z opia (zaschlé šťávy z nezralých makovic). Otázka = receptory, balík účinků a morfin jako referenční lék.

- **Bolest:** **nociceptivní** (poškození tkáně) · **neuropatická** (poškození nervu) · **fantomová** (podnět už neexistuje). ⚠️ **Farmakoterapie bolesti je vždy symptomatická.**
- **Mechanismus:** agonisté **opioidních receptorů spřažených s G-proteinem** → ↓ vstup Ca²⁺ presynapticky (méně přenašeče) a ↑ výstup K⁺ postsynapticky (hyperpolarizace) → přeruší se vedení bolesti v míše a mění se její vnímání v mozku.

| Receptor | Účinky |
|---|---|
| **μ (mí)** | **analgezie, útlum dechu, euforie, sedace, mióza, zácpa, fyzická závislost** |
| **δ (delta)** | analgezie hlavně na periferii |
| **κ (kappa)** | míšní analgezie, sedace, **dysforie** |

- **Podle vztahu k receptoru:** **plní agonisté** (morfin, kodein, fentanyl, sufentanil, metadon, pethidin) · **parciální / smíšení agonisté-antagonisté** (buprenorfin, nalbufin, pentazocin) · **antagonisté** (naloxon, naltrexon, nalmefen).
- **Sedm účinků, které odříkej:** ① **analgezie** (μ) ② **euforie a potlačení úzkosti** ③ **útlum dechu** — sníží citlivost dechového centra k CO₂ (**hlavní příčina smrti při předávkování**, ruší se naloxonem) ④ **antitusický** (nejvíc kodein) ⑤ **GIT a močové cesty** — **zácpa**, spazmus Oddiho svěrače a ↑ tlak ve žlučových cestách, retence moči, nauzea a zvracení ⑥ **mióza** („špendlíkové zorničky") ⑦ **uvolnění histaminu** — svědění, kopřivka v místě vpichu, hypotenze, bronchokonstrikce.
- ⚠️ **Tolerance vzniká na analgezii i na většinu NÚ — S VÝJIMKOU ZÁCPY A MIÓZY**, ty přetrvávají navždy. Klasická chytačka.
- **Indikace:** silná akutní bolest (trauma, pooperační, **infarkt**), **chronická nádorová bolest**, dušnost u terminálního srdečního selhání, kašel (kodein), průjem (loperamid periferně).
- **Kontraindikace a interakce:** útlum dechu a CHOPN, akutní břicho, ⚠️ **kombinace s tlumivými látkami (benzodiazepiny, alkohol, hypnotika) — sčítá se útlum dechu**; **tramadol/pethidin + SSRI či IMAO → serotoninový syndrom**.
- **Endogenní opioidy:** endorfiny, enkefaliny, dynorfiny — tělu vlastní ligandy stejných receptorů.
- **Morfin — referenční lék:** agonista μ a κ; i.v. u akutní bolesti, perorálně s postupným uvolňováním u chronické. **Kinetika:** silný **first-pass efekt**, metabolizuje se glukuronidací na **morfin-6-glukuronid, který je aktivní a má delší poločas** → ⚠️ **kumuluje se při renálním selhání**. Prochází placentou (útlum dechu novorozence). **Předepisuje se na recept s modrým pruhem (tabulka I).**
- **Intoxikace opioidy — trias:** **kóma + mióza + útlum dechu**; k tomu hypotenze, bradykardie. **Léčba: naloxon i.v.** + zajištění ventilace.
- **Heroin (diacetylmorfin)** — lipofilnější než morfin, rychle přes HEB → intenzivní „rush". Po podání naloxonu se okamžitě rozvine **abstinenční syndrom**: slzení, rýma, ⚠️ **mydriáza**, husí kůže, tachykardie, křeče v břiše, průjem, neklid.

🔑 **Intoxikace = zúžená zornice (mióza) · abstinence = rozšířená zornice (mydriáza).** Plete se to nejčastěji.

❓ *Na které dva účinky opioidů se tolerance nevyvíjí?* → **Zácpa a mióza.**

---

## 61 · Deriváty a náhražky morfinu

**O čem to je:** syntetičtí „příbuzní" morfinu — buď rychlejší/silnější, nebo s menším rizikem závislosti, nebo rovnou jako antidotum.

| Silné syntetické opioidy | Podstatné |
|---|---|
| **Fentanyl** | ~100× silnější než morfin; **náplast u chronické nádorové bolesti**, i.v. v anestezii, slizniční formy na **průlomovou bolest** |
| **Sufentanil** | nejsilnější, velmi rychlý nástup — anesteziologie |
| **Pethidin** | kratší účinek (4 h), rychlejší nástup. ⚠️ **Nevhodný pro dlouhodobou léčbu** — kumuluje se neurotoxický metabolit norpethidin (křeče) |
| **Metadon** | dlouhý poločas → **substituční léčba závislosti na opioidech** (potlačí abstinenční příznaky bez euforie). ⚠️ prodlužuje QT |
| **Oxykodon** | perorálně s postupným uvolňováním; vhodný i **při renální insuficienci** |

| Slabé opioidy | Podstatné |
|---|---|
| **Kodein** | **proléčivo** — ~10 % se mění na morfin přes **CYP2D6** (proto u pomalých metabolizátorů nezabere, viz O26); antitusikum, analgetikum v kombinacích |
| **Dihydrokodein** | asi 1/6 účinku morfinu, v kombinacích |
| **Tramadol** | atypický: slabý μ-agonista + **blokuje zpětné vychytávání NA a serotoninu**; ~6× slabší než morfin, ale **méně zácpy a útlumu dechu**. ⚠️ Riziko **serotoninového syndromu** a snížení prahu pro křeče |

- ⚠️ **Stropový efekt** (u slabých opioidů a parciálních agonistů): po dosažení určité dávky **se analgezie dál nezvyšuje, přibývají jen nežádoucí účinky** — proto se musí přejít na silný opioid, ne dál navyšovat.

| Antagonisté | Podstatné |
|---|---|
| **Naloxon** | kompetitivní antagonista všech opioidních receptorů; kvůli first-pass efektu **jen i.v./i.m./intranazálně**; **antidotum útlumu dechu při intoxikaci opioidy**. ⚠️ Krátký poločas — po odeznění se útlum může vrátit, pacient patří na monitoraci |
| **Naltrexon** | perorálně, dlouhodobě — **udržovací léčba závislosti na opioidech i alkoholu** |
| **Metylnaltrexon** | působí **jen na periferní μ receptory** (neprojde HEB) → zruší **zácpu, ale ne analgezii** |

⚠️ **Chyba ve zdroji:** tvůj materiál uvádí naloxon jako antidotum i u barbiturátů, benzodiazepinů a alkoholu — **to není pravda**. Naloxon ruší **jen opioidy**; u benzodiazepinů je antidotem **flumazenil**, u barbiturátů a alkoholu **antidotum neexistuje** (jen podpůrná léčba).

- **Parciální agonisté a smíšení agonisté-antagonisté** — vznikli ve snaze o analgezii bez závislosti; působí hlavně přes **κ** (míšní analgezie), na μ minimálně nebo antagonisticky → nižší riziko závislosti, ale **stropový efekt** a psychomimetické NÚ:
  - **Buprenorfin** — parciální agonista μ, antagonista κ; transdermálně nebo sublingválně (velký first-pass efekt); chronická bolest a substituční léčba závislosti. ⚠️ Vytěsní jiný opioid z receptoru → může vyvolat abstinenční příznaky.
  - **Nalbufin** — agonista κ, antagonista μ; minimální riziko závislosti, málo ovlivňuje GIT.
  - **Pentazocin** — agonista κ; ⚠️ **dysforie a halucinace** (přes κ, ne přes δ, jak uvádí zdroj), ↑ tlak v plicnici.

🔑 **Naloxon = akutní antidotum, jen injekčně · naltrexon = dlouhodobá léčba závislosti, perorálně.**

❓ *Proč se metylnaltrexon nedá použít jako antidotum?* → Neprojde přes hematoencefalickou bariéru — zruší jen periferní zácpu, ne útlum dechu.

---

## 62 · Eikosanoidy

**O čem to je:** lokální „tkáňové hormony" z kyseliny arachidonové, které řídí zánět, srážení, tonus cév a stahy dělohy. Aspirin, kortikoidy i antiastmatika zasahují právě sem.

🔑 **Kaskáda, kterou musíš odříkat jako první:** fosfolipidy membrány → **fosfolipáza A₂** → **kyselina arachidonová** → dvě větve: **cyklooxygenáza (COX)** → prostaglandiny, prostacyklin, tromboxany · **lipoxygenáza (LOX)** → **leukotrieny**. ⚠️ **Kortikoidy indukují lipokortin, který blokuje fosfolipázu A₂ → vypnou celou kaskádu na začátku** (obě větve). **NSA blokují jen COX** — leukotrienová větev jim zůstane (proto aspirinem indukované astma).

| Skupina | Účinky a léčiva |
|---|---|
| **PGE** | vazodilatace, bronchodilatace, ↓ tvorba žaludeční kyseliny a **ochrana sliznice**, stahy dělohy. **Alprostadil (PGE1)** — udržuje otevřenou **tepennou dučej** u novorozence s vrozenou srdeční vadou, vazodilatans. **Dinoproston (PGE2)** — gel na **zrání děložního hrdla před porodem**. **Misoprostol** — prevence vředů z NSA |
| **PGF** | konstrikce průdušek a plicních cév, stahy dělohy. **Dinoprost, karboprost** — indukce porodu, poporodní atonie dělohy. **Latanoprost, travoprost** — oční kapky u **glaukomu** (zlepší odtok nitrooční tekutiny) |
| **Prostacyklin (PGI₂)** | tvoří **cévní endotel** — **vazodilatace + brzdí agregaci destiček** (protipól tromboxanu). **Iloprost** u plicní hypertenze a ischemie končetin |
| **Tromboxan (TXA₂)** | tvoří **destičky** — **agregace destiček + vazokonstrikce**. ⚠️ **Kyselina acetylsalicylová ireverzibilně acetyluje COX-1 v destičce → antiagregační efekt na celou dobu jejího života (7–10 dní)** |
| **Leukotrieny** | mediátory zánětu a alergie — **bronchokonstrikce, otok, hlen**, chemotaxe. **Montelukast, zafirlukast** — antagonisté cysteinyl-leukotrienových receptorů (astma, alergická rýma) |

- **Prozánětlivé cytokiny** (IL-1, IL-6, **TNF-α**) — bílkovinné mediátory z makrofágů a T-lymfocytů: aktivují endotel, adhezivní molekuly, jsou **endogenní pyrogeny** a spouštějí bílkoviny akutní fáze.
- **Inhibitory cytokinů (biologická léčba):** anti-TNF-α **infliximab, adalimumab, etanercept, golimumab** (revmatoidní a psoriatická artritida, Crohnova choroba, psoriáza) · anti-IL-1 **anakinra, kanakinumab** (dna) · anti-IL-6 **tocilizumab**. ⚠️ Před nasazením **screening TBC a hepatitid** (viz O35).
- **Imunosupresiva a jejich tři cesty:** blokáda tvorby **IL-2** (cyklosporin, takrolimus, sirolimus) · blokáda exprese cytokinových genů (**kortikoidy**) · blokáda syntézy purinů/pyrimidinů (azathioprin, mykofenolát).

❓ *Jak se liší zásah kortikoidů a NSA do téhle kaskády?* → Kortikoidy blokují **fosfolipázu A₂** (vypnou obě větve), NSA jen **COX** — leukotrieny se tvoří dál.

---

## 63 · Analgetika-antipyretika

**O čem to je:** léky na **bolest a horečku bez protizánětlivého účinku** — hlavně paracetamol, který je běžně dostupný, ale při předávkování těžce poškodí játra.

- ⚠️ **Klíčový rozdíl proti NSA: analgetika-antipyretika NEMAJÍ protizánětlivý ani protidestičkový efekt** — jen analgetický a antipyretický.
- **Paracetamol**
  - **Mechanismus:** není zcela objasněn — nejspíš inhibice **cyklooxygenázy centrálně (v CNS a hypotalamu)**, kde je nízká koncentrace peroxidů; v periferní zanícené tkáni proto nefunguje.
  - **Indikace:** horečka, bolest hlavy, zubů, kloubů, chřipkové stavy. **Lék první volby u dětí, těhotných a seniorů** — nedráždí žaludek, nezvyšuje krvácivost, nehrozí Reyeův syndrom.
  - **Dávkování:** jednotlivá **~1 g**, maximálně **4 g/den** (u rizikových pacientů méně).
  - ⚠️ **Hepatotoxicita — jádro otázky:** malá část paracetamolu se přes **CYP2E1** mění na toxický metabolit **NAPQI**, který normálně zneškodní **glutathion**. Při předávkování (od ~10–15 g) glutathion dojde → NAPQI ničí hepatocyty → **jaterní nekróza a selhání**. **Alkohol indukuje CYP2E1 a vyčerpává glutathion** → chronický alkoholik se otráví i nižší dávkou. **Antidotum: N-acetylcystein** (prekurzor glutathionu) — čím dřív, tím lépe (ideálně do 8–10 h).
- **Pyrazolové deriváty — metamizol, propyfenazon**
  - **Účinek:** silná analgezie + **spasmolytický** efekt na hladký sval → **žlučová a ledvinná kolika**, spasmoanalgezie u instrumentálních vyšetření, silná akutní bolest; nedráždí žaludek jako NSA.
  - ⚠️ **NÚ: agranulocytóza** (vzácná, ale závažná), hypotenze při rychlém i.v. podání, anafylaktoidní reakce — **nepodávat astmatikům**; podezření na kancerogenitu a nefrotoxicitu.

🔑 **Paracetamol je v terapeutické dávce nejbezpečnější analgetikum, v předávkování jeden z nejnebezpečnějších léků vůbec. Antidotum: N-acetylcystein.**

❓ *Proč je kombinace paracetamolu s alkoholem nebezpečná?* → Alkohol indukuje CYP2E1 (víc toxického NAPQI) a zároveň vyčerpává glutathion, který ho má neutralizovat.

---

## 64 · Nesteroidní antiflogistika (NSA)

**O čem to je:** nejpoužívanější léky na bolest a zánět (ibuprofen, aspirin) — blokují **COX**, který má dvě varianty: „hodnou" COX-1 a „zánětlivou" COX-2. Většina nežádoucích účinků plyne z toho, že klasická NSA blokují obě.

| | **COX-1 (konstitutivní)** | **COX-2 (indukovatelná)** |
|---|---|---|
| Kde | trvale ve většině tkání | tvoří se **při zánětu**, indukují ji IL-1, IL-6, TNF-α |
| Funkce | **ochrana žaludeční sliznice** (PGE2), **průtok ledvinou**, **tromboxan v destičkách** | prostanoidy zánětu — vazodilatace, otok, **bolest**, horečka |
| Blokáda znamená | ⚠️ **vředy a krvácení do GIT, poškození ledvin, krvácivost** | **analgetický a protizánětlivý efekt — to, co chceme** |

- **Účinky NSA:** **analgetický, antipyretický, protizánětlivý**, u některých antiagregační a antiuratický. **Indikace:** mírná až středně silná bolest, **artritida, osteoartróza, dna**, poúrazové otoky, horečka, pooperační a zubní bolest.
- **Nežádoucí účinky (rostou s dávkou, délkou léčby a věkem):**
  - **GIT:** dyspepsie, **vředy, krvácení, perforace** — riziko násobí kombinace s kortikoidy, antikoagulancii nebo SSRI; prevence **inhibitorem protonové pumpy**,
  - **ledviny:** ↓ prostaglandiny udržující průtok → **retence sodíku a vody, hypertenze, akutní selhání**, dlouhodobě **analgetická nefropatie**; ⚠️ nebezpečná trojkombinace **NSA + ACEI/sartan + diuretikum**,
  - **kardiovaskulárně:** ↑ tlak, ↑ riziko infarktu a CMP (nejvíc u koxibů a diklofenaku),
  - **hypersenzitivita:** ⚠️ **aspirinem indukované astma** — zablokovaná COX přesměruje kaskádu do tvorby leukotrienů (viz otázka 62),
  - **krvácivost** (útlum tromboxanu).
- **Kontraindikace:** aktivní vřed a krvácení do GIT, těžká renální i jaterní insuficience, srdeční selhání, ⚠️ **III. trimestr gravidity** (předčasný uzávěr Botallovy dučeje, oligohydramnion), astma s přecitlivělostí na NSA.

| Skupina | Zástupci a zvláštnosti |
|---|---|
| **salicyláty** | **kyselina acetylsalicylová** — jako jediná blokuje COX **ireverzibilně**; v nízké dávce antiagregační, ve vysoké protizánětlivá. Kyselina salicylová lokálně **keratolyticky** |
| **deriváty kys. propionové** | **ibuprofen** — nejšetrnější k GIT; **naproxen** — dlouhý poločas, nejnižší kardiovaskulární riziko; ketoprofen, flurbiprofen |
| **deriváty kys. octové** | **diklofenak, indometacin** — silné, ale vyšší riziko GIT i KVS |
| **oxikamy** | piroxikam, **meloxikam** (částečně COX-2 preferenční), dlouhý poločas |
| **preferenční COX-2** | **nimesulid** — jen krátkodobě, ⚠️ hepatotoxicita |
| **koxiby (selektivní COX-2)** | **celekoxib, etorikoxib, parekoxib** — výrazně méně GIT komplikací, ⚠️ **ale stejné či vyšší kardiovaskulární riziko** a nemají antiagregační efekt |

⚠️ **Dvě věci, na které se ptají:** **Reyeův syndrom** — encefalopatie s jaterním selháním u **dítěte, kterému se při viróze podá kyselina acetylsalicylová**; úmrtnost až 40 % → **dětem se salicyláty nepodávají** (místo nich paracetamol nebo ibuprofen). **Salicylismus** — při vyšších dávkách **tinnitus, poruchy sluchu, závratě, nauzea, hyperventilace**.

🔑 **COX-1 chrání žaludek a ledviny, COX-2 dělá zánět. Aspirin jako jediné NSA blokuje enzym ireverzibilně — proto působí na destičku celých 7–10 dní.**

❓ *Proč mají koxiby méně vředů, ale kardiovaskulárně nejsou bezpečnější?* → Šetří COX-1 v žaludku, ale zároveň potlačí **prostacyklin** v endotelu, zatímco **tromboxan** v destičkách zůstává → posun k trombóze.

---

## 65 · Farmakoterapie migrény

**O čem to je:** záchvatovitá bolest hlavy se změnami průsvitu mozkových cév — léky buď cévy stáhnou zpět (akutní léčba), nebo záchvatům předcházejí (profylaxe).

- **Migréna** = opakovaná záchvatovitá bolest hlavy trvající hodiny až dny, často jednostranná, s nauzeou, zvracením, fotofobií a u části pacientů s **aurou**.
- **Tři mechanismy vzniku:** ① **vazomotorická složka** — dilatace nitrolebních i mimolebních tepen ② **spouštěcí zóna** v **serotoninergním systému** mozkového kmene ③ **aktivace trigeminovaskulárního systému** — z nemyelinizovaných vláken inervujících pleny se uvolní neuropeptidy (CGRP) → neurogenní zánět a bolest.
- **Tři stadia záchvatu:** ① vazokonstrikce (fáze aury) → ② **vazodilatace = bolest** → ③ otok a zvýšená propustnost cév.

| Akutní léčba | Podstatné |
|---|---|
| **Triptany** | **lék první volby**; **agonisté 5-HT1B/1D** → vazokonstrikce nitrolebních cév + útlum výdeje neuropeptidů z trigeminu. **Sumatriptan** (tablety, nosní sprej, s.c. u těžkého záchvatu), **zolmitriptan** (vyšší dostupnost). ⚠️ **Jen na akutní záchvat, ne na profylaxi.** NÚ: tlak na hrudi, mravenčení, únava, závratě. ⚠️ **KI: ischemická choroba srdeční, stav po infarktu, nekorigovaná hypertenze, kombinace s IMAO a námelovými alkaloidy** |
| **Námelové alkaloidy** | **ergotamin, dihydroergotamin** — parciální agonisté serotoninových a α-adrenergních receptorů → silná vazokonstrikce; špatná dostupnost → čípky, nosní sprej. NÚ: nauzea, křeče v břiše, průjem, **stahy dělohy** (KI gravidita), bolesti svalů, při nadužívání **ergotismus** (ischemie končetin) |
| **Analgetika a antiemetika** | u lehčích záchvatů **kyselina acetylsalicylová, ibuprofen, naproxen, paracetamol**; **metoklopramid nebo domperidon** — nejen proti zvracení, ale i proto, že obnoví vyprázdnění žaludku a zlepší vstřebání analgetika |

- **Profylaxe** (při ≥ 4 záchvatech měsíčně): **β-blokátory (metoprolol, propranolol)**, **blokátory kalciových kanálů (verapamil, flunarizin)**, **antiepileptika (valproát, topiramát)**, amitriptylin. Cíl: snížit frekvenci, délku a intenzitu záchvatů a umožnit nižší dávky akutních léků.
- ⚠️ **Nadužívání akutních léků (>10–15 dní v měsíci) vede k bolesti hlavy z nadužívání medikace** — pacient pak má bolesti častěji, ne méně často.

🔑 **Triptany = akutní záchvat (vazokonstrikce) · β-blokátory, BKK a valproát = profylaxe. Zaměnit to je klasická chyba.**

❓ *Proč jsou triptany kontraindikovány u ICHS?* → Stahují i věnčité tepny → mohou vyvolat ischemii myokardu.

---

## 66 · Léčiva s pozitivně inotropním účinkem, digoxin

**O čem to je:** kardiotonika posilují stah srdce; nejznámější je **digoxin** z náprstníku. Klíčový paradox: u **nemocného** srdce výdej zvýší, u **zdravého** sníží.

- **Srdeční glykosidy** = léčiva digitalisového typu (náprstník, konvalinka, čemeřice, oleandr). Struktura: **cukr** (vazba na myokard) + **aglykon** (steroidní jádro s laktonovým kruhem — nositel účinku).
- 🔑 **Mechanismus (odvoď, nešprtej):** blokáda **Na⁺/K⁺-ATPázy** → v buňce se hromadí Na⁺ → zpomalí se výměník Na⁺/Ca²⁺ → **v buňce zůstane víc Ca²⁺** → silnější vazba aktinu a myozinu = **pozitivně inotropní efekt**. Zároveň **aktivuje n. vagus** → **negativně chronotropní** (pomalejší tep) a **negativně dromotropní** efekt (zpomalené vedení AV uzlem — riziko AV blokády).
- ⚠️ **Protiklad, který chtějí slyšet:** u **selhávajícího** srdce digoxin **zvýší** minutový výdej a potlačí supraventrikulární arytmie; u **zdravého** srdce výdej naopak **sníží** (převáží vagový efekt a vazokonstrikce).
- **Digoxin:** dobře se vstřebává z GIT, **ze 2/3 se vylučuje nezměněný ledvinami** → ⚠️ **při renální insuficienci se kumuluje**. **Velmi úzké terapeutické okno → nutné TDM.** Kontroluje frekvenci hlavně **v klidu**, ne při zátěži — proto mají u fibrilace síní přednost β-blokátory.
- **Indikace:** **fibrilace síní s rychlou odpovědí komor** (kontrola frekvence), **chronické srdeční selhání se sníženou ejekční frakcí**, kde přetrvávají příznaky i při standardní léčbě.
- **Kontraindikace:** bradykardie a **AV blokáda**, hypokalemie i hyperkalemie, **hypertrofická kardiomyopatie a diastolická dysfunkce**, komorové tachyarytmie, WPW syndrom.
- ⚠️ **Co zvyšuje citlivost k digoxinu (= riziko intoxikace):** **hypokalemie** (draslík soutěží o stejné vazebné místo — proto **diuretika ztrácející draslík jsou nejrizikovější interakce**), **hyperkalcemie**, hypomagnezemie, ischemie a hypoxie myokardu, **hypotyreóza**, renální insuficience, věk.
- **Digitalisová intoxikace:** GIT (nauzea, zvracení, průjem, nechutenství), CNS (zmatenost, bolest hlavy, ⚠️ **poruchy barevného vidění — žluté vidění, xantopsie**), a hlavně **arytmie všeho druhu** (bigeminie, AV blok, komorová tachykardie). **Léčba:** vysadit, upravit kalium, atropin u bradykardie, **protilátky proti digoxinu (Fab fragmenty)** u těžké otravy.

| Ostatní pozitivně inotropní léčiva | Podstatné |
|---|---|
| **β1-sympatomimetika** — dobutamin, dopamin | akutní srdeční selhání a **kardiogenní šok**; jen krátkodobě — ⚠️ arytmie a **vyšší mortalita při dlouhodobém podání** |
| **Levosimendan** | **kalciový senzitizér** — zvyšuje citlivost troponinu C k vápníku (nezvyšuje spotřebu kyslíku); kardiogenní a septický šok |
| **Inhibitory fosfodiesterázy 3** — milrinon, amrinon | ↑ cAMP v myocytu; riziko arytmií a náhlé smrti |

❓ *Proč je hypokalemie u pacienta na digoxinu nebezpečná?* → Draslík soutěží s digoxinem o vazbu na Na⁺/K⁺-ATPázu; při jeho nedostatku se digoxin naváže víc → intoxikace i při „normální" dávce.

---

## 67 · Antiarytmika

**O čem to je:** léky na poruchy rytmu, rozdělené do **čtyř tříd podle Vaughana-Williamse** podle toho, jaký kanál či receptor blokují. Mechanismus, na který se ptají nejvíc, je **reentry**.

- **Tři vlastnosti nutné pro pravidelný rytmus:** **automaticita** (schopnost tvořit vzruchy — převodní systém), **dráždivost** (daná refrakterní fází) a **vodivost** — v **SA a AV uzlu je závislá na Ca²⁺ kanálech**, ve zbytku převodního systému a v komorách na **Na⁺ kanálech**. *(Z toho plyne, proč verapamil působí na uzly a lidokain na komory.)*
- 🔑 **Reentry:** vzruch narazí na ohnisko (ischemie) s **jednosměrnou blokádou**, obejde ho druhou drahou a vrátí se zpět už vodivou tkání → **obíhá dokola** a arytmii udržuje donekonečna. Další mechanismy: zvýšená automaticita a **spouštěné rytmy** (časná/opožděná následná depolarizace).
- ⚠️ **Každé antiarytmikum může arytmii i vyvolat (proarytmogenní efekt)** — proto individuální dávkování a monitorace.

| Třída | Mechanismus | Zástupci |
|---|---|---|
| **Ia** | blokáda Na⁺ kanálu, **prodlužuje** akční potenciál (blokuje i K⁺) | chinidin, disopyramid, prokainamid |
| **Ib** | blokáda Na⁺ kanálu, **zkracuje** akční potenciál | **lidokain**, mexiletin |
| **Ic** | blokáda Na⁺ kanálu, délku AP **nemění** | **propafenon, flekainid** |
| **II** | **β-blokátory** | metoprolol, bisoprolol, **esmolol** (i.v., ultrakrátký) |
| **III** | blokáda **K⁺ kanálů** → prodloužení repolarizace a QT | **amiodaron**, sotalol, dronedaron, vernakalant |
| **IV** | **blokátory kalciových kanálů** | **verapamil, diltiazem** |
| **nezařazená** | — | **adenosin**, digoxin, atropin, ionty Mg²⁺ |

- **Ia — chinidin:** fibrilace a flutter síní, komorové tachykardie. ⚠️ **Parasympatolytický efekt + prodloužení QT → torsade de pointes**; NÚ **cinchonismus** (tinnitus, poruchy sluchu a vidění, třes), GIT nesnášenlivost, interakce s **warfarinem** (krvácení). Dnes výjimečně.
- **Ib — lidokain:** chemicky amidové **lokální anestetikum**; **jen i.v.**, komorové extrasystoly a komorová tachykardie **v akutní fázi infarktu**. ⚠️ Při hypotenzi klesá průtok játry → kumulace → parestezie, zmatenost, křeče.
- **Ic — propafenon, flekainid:** lék volby u arytmií **bez strukturálního postižení srdce** (fibrilace síní, AV rekurentní tachykardie u **WPW syndromu**). ⚠️ **KI: ischemická choroba srdeční a stav po infarktu** — zvyšují tam mortalitu. Propafenon má navíc β-lytický efekt.
- **II — β-blokátory:** tlumí arytmogenní vliv katecholaminů, zpomalují SA uzel a prodlužují refrakteritu AV uzlu → **kontrola frekvence u fibrilace síní**, arytmie při stresu, hypertyreóze a námaze, **prevence náhlé smrti po infarktu**. KI: astma, těžká bradykardie, AV blok.
- **III — amiodaron:** ⚠️ **nejúčinnější antiarytmikum, ale nejtoxičtější.** Působí na všechny čtyři třídy zároveň, **extrémně dlouhý poločas (týdny)**, kumuluje se ve tkáních. **Indikace: supraventrikulární i komorové tachykardie, fibrilace síní, refrakterní komorová fibrilace při resuscitaci.** **NÚ — nejvděčnější část otázky:** ⚠️ **obsahuje jód → hypo- i hypertyreóza**, **plicní fibróza** (nejzávažnější), **hepatitida**, **šedomodré zbarvení kůže**, **depozita v rohovce**, fotosenzitivita, prodloužení QT. **Dronedaron** — obdoba bez jódu, slabší, KI u srdečního selhání. **Sotalol** — β-blokátor + třída III.
- **IV — verapamil, diltiazem:** ↓ automaticita SA uzlu, ↑ refrakterita AV uzlu → **supraventrikulární tachyarytmie a kontrola frekvence u fibrilace síní**; negativně inotropní. ⚠️ **KI: WPW syndrom, srdeční selhání, kombinace s i.v. β-blokátorem** (riziko asystolie).
- **Adenosin** — agonista A1 receptorů → otevře K⁺ kanály, hyperpolarizace, **krátkodobá blokáda AV uzlu**; podává se **rychlým i.v. bolusem**, účinek trvá sekundy; **lék volby u paroxysmální supraventrikulární tachykardie**. NÚ: krátký pocit dušnosti a tlaku na hrudi, flush.
- **Bradyarytmie:** nejčastěji polékové (digoxin, β-blokátory, verapamil). Řešení je **kardiostimulace**; **atropin a β-sympatomimetika** jen krátkodobě k překlenutí.

❓ *Co je reentry?* → Vzruch narazí na jednosměrnou blokádu, vrátí se oklikou zpět a obíhá dokola — tím arytmii udržuje.

---

## 68 · ACE inhibitory a antagonisté angiotenzinu

**O čem to je:** základní léky na hypertenzi a srdeční selhání — blokují systém **RAAS**. Jejich typický nežádoucí účinek (suchý kašel) vysvětluje celou otázku.

🔑 **Kaskáda RAAS, odříkej ji plynule:** **angiotenzinogen** (z jater) → **renin** (z juxtaglomerulárního aparátu ledvin, uvolňuje se při nízkém tlaku, nízkém Na⁺ a stimulaci β1) → **angiotenzin I** (sám neúčinný) → **ACE** (na endotelu, hlavně v plicích) → **angiotenzin II** = **silný vazokonstriktor**. ⚠️ **Stejný enzym ACE odbourává i bradykinin** — proto jeho blokáda znamená nadbytek bradykininu → **suchý dráždivý kašel a angioedém**.

- **Angiotenzin II dělá:** vazokonstrikci, ↑ výdej **noradrenalinu** ze sympatiku, ↑ **aldosteron** (zadržení Na⁺ a vody, ztráta K⁺), stah vas efferens s ↑ nitroglomerulárního tlaku, dlouhodobě **remodelaci srdce a cév**.
- **ACE inhibitory — kaptopril, enalapril, ramipril, perindopril, lisinopril** (koncovka **-pril**):
  - **Účinky:** ↓ tlak bez reflexní tachykardie (⚠️ **jediná vazodilatancia, která neaktivují sympatikus**), ↓ aldosteron, **regrese hypertrofie levé komory**, zpomalení remodelace po infarktu, ↑ citlivost na inzulin, ⚠️ **renoprotekce** — snižují únik bílkovin do moči (sníží tlak v glomerulu dilatací vas efferens).
  - **Indikace:** **hypertenze**, **chronické srdeční selhání se sníženou ejekční frakcí**, **stav po infarktu**, **diabetická a proteinurická nefropatie**.
  - **NÚ:** ⚠️ **suchý kašel (až 10–20 %)**, **angioedém** (vzácný, ale život ohrožující — otok jazyka a hrtanu), **hyperkalemie**, hypotenze po první dávce (u dehydratovaných a na diureticích), vzestup kreatininu, poruchy chuti (kaptopril).
  - **Kontraindikace:** ⚠️ **gravidita** (fetotoxicita, malformace, oligohydramnion), **oboustranná stenóza renálních tepen** (ledvina závisí na angiotenzinu II — hrozí akutní selhání), hyperkalemie, angioedém v anamnéze.
- **Sartany (blokátory AT1 receptoru) — losartan, valsartan, telmisartan, kandesartan** (koncovka **-sartan**):
  - **Mechanismus:** blokáda **receptoru AT1** — účinky angiotenzinu II se nedostanou k cíli, ⚠️ **ale bradykinin se odbourává normálně → nezpůsobují kašel**. To je jádro rozdílu.
  - **Indikace:** stejné jako ACEI; **nasazují se hlavně tam, kde pacient ACEI netoleruje** (kašel, angioedém).
  - **NÚ a KI:** hyperkalemie, hypotenze, **gravidita**, stenóza renálních tepen. ⚠️ **ACEI a sartan se nikdy nekombinují** (dvojitá blokáda RAAS = renální selhání a hyperkalemie bez přínosu).

❓ *Proč ACE inhibitory kašlou a sartany ne?* → ACEI blokují i odbourávání **bradykininu**, který dráždí dýchací cesty; sartany blokují jen receptor pro angiotenzin II.

---

## 69 · Diuretika

**O čem to je:** léky na odvodnění a na tlak — liší se **místem zásahu v nefronu**. Čím dřív v nefronu působí a čím větší podíl sodíku se tam vstřebává, tím jsou silnější.

| Skupina | Místo v nefronu | Mechanismus, zástupci, indikace |
|---|---|---|
| **Osmotická** | proximální tubulus + sestupné raménko | **manitol** — filtruje se, ale **nevstřebává se zpět** → strhává s sebou vodu. **Indikace: otok mozku, zvýšený nitrolební a nitrooční tlak, forsírovaná diuréza při intoxikaci.** ⚠️ KI: srdeční selhání (přechodně ↑ objem krve) |
| **Inhibitory karboanhydrázy** | proximální tubulus | **acetazolamid, dorzolamid, brinzolamid** — ↓ zpětné vstřebání HCO₃⁻ a Na⁺. Jako diuretika se dnes **nepoužívají**; indikace **glaukom** (↓ tvorba nitrooční tekutiny), horská nemoc, některé dětské epilepsie. NÚ: **metabolická acidóza**, hypokalemie |
| **Kličková** | vzestupné raménko Henleovy kličky | **furosemid** — blokáda **Na⁺/K⁺/2Cl⁻ kotransportéru**; ⚠️ **nejsilnější diuretika** (tady se vstřebává až 25 % sodíku) |
| **Thiazidová** | distální tubulus | **hydrochlorothiazid, chlorthalidon, indapamid** — blokáda **Na⁺/Cl⁻ kotransportéru** |
| **Kalium šetřící** | sběrný kanál | **amilorid** (blokáda ENaC kanálu), **spironolakton, eplerenon** (antagonisté **aldosteronu**) |
| **Aquaretika** | sběrný kanál | **tolvaptan** — blokáda vazopresinových V2 receptorů → vylučuje se **čistá voda**; indikace hyponatremie a SIADH |

- **Kličková diuretika (furosemid) — detaily, na které se ptají:**
  - **Extrarenální efekt:** rozšiřují **žíly** → ⚠️ **při plicním edému uleví dřív, než vůbec začne diuréza**.
  - **Kinetika:** i.v. účinek do 2–5 minut (trvá ~6 h), perorálně do hodiny (trvá ~8 h).
  - **Indikace:** **akutní plicní edém**, srdeční selhání s retencí tekutin, otoky při renálním a jaterním selhání (ascites), hyperkalemie, hyperkalcemie, ⚠️ **fungují i při nízké glomerulární filtraci** (na rozdíl od thiazidů).
  - **NÚ:** ⚠️ **hypokalemie** (arytmie, potencuje toxicitu digoxinu), hyponatremie, **hypokalcemie a hypomagnezemie**, dehydratace a hypotenze, hyperurikemie (dna), ⚠️ **ototoxicita** — zvlášť v kombinaci s **aminoglykosidy**.
- **Thiazidová diuretika:**
  - ⚠️ **Zvyšují zpětné vstřebávání vápníku** (opak kličkových) → proto se používají u **kalciové urolitiázy**; paradoxně pomáhají u **nefrogenního diabetu insipidus**.
  - Antihypertenzní efekt je zpočátku z poklesu objemu, **po ~2 týdnech z poklesu periferního odporu**.
  - **Indikace:** **hypertenze (základní lék)**, srdeční selhání, kalciové kameny.
  - **NÚ:** **hypokalemie a hyponatremie**, **hyperurikemie (dna)**, **hyperglykemie a inzulinová rezistence**, hyperlipidemie, **hyperkalcemie**, fotosenzitivita. ⚠️ **Nefungují při GFR < 30 ml/min.**
- **Kalium šetřící:** **spironolakton** — antagonista aldosteronu; indikace **srdeční selhání (snižuje mortalitu), jaterní cirhóza s ascitem, primární hyperaldosteronismus, rezistentní hypertenze**. NÚ: ⚠️ **hyperkalemie**, **gynekomastie a poruchy menstruace** (steroidní struktura — eplerenon je nemá). ⚠️ **Nekombinovat s ACEI/sartanem bez kontroly kalia.**

🔑 **Kličková = nejsilnější, ztrácejí vápník, fungují i při selhání ledvin · thiazidy = šetří vápník, na hypertenzi, nefungují při nízké GFR · kalium šetřící = jediné, která draslík zadržují.**

❓ *Proč furosemid pomůže u plicního edému dřív, než začne močit?* → Rozšíří žíly → klesne předtížení a tlak v plicním řečišti.

---

## 70 · Blokátory kalciových kanálů (BKK)

**O čem to je:** rozšiřují cévy blokádou vstupu vápníku do buňky — bez vápníku se sval nestáhne. **Tři podskupiny se zásadně liší** tím, jestli působí na cévy, nebo na srdce.

- **Mechanismus (odříkej celý řetězec):** depolarizace otevře **kalciový kanál L-typu** → Ca²⁺ vstoupí do buňky a spustí uvolnění dalšího Ca²⁺ ze sarkoplazmatického retikula → **Ca²⁺ + kalmodulin** aktivují kinázu lehkých řetězců myozinu → kontrakce. **BKK vstup Ca²⁺ zablokují → hladký sval se uvolní**, na srdci klesne kontraktilita a automaticita.

| Skupina | Kde působí | Zástupci a zvláštnosti |
|---|---|---|
| **Dihydropyridiny** (-dipin) | **selektivně cévy** | **amlodipin** (dlouhý účinek, 3. generace), felodipin, isradipin, **nifedipin** (1. generace — rychlý pokles tlaku → ⚠️ **reflexní tachykardie**, dnes jen retardovaně). **Minimální vliv na srdce** |
| **Fenylalkylaminy** | **hlavně myokard** | **verapamil** — ↓ kontraktilita, ↓ frekvence, ↑ refrakterita AV uzlu; volba u pacienta, který nesmí β-blokátor (astma). Typický NÚ **úporná zácpa** |
| **Benzothiazepiny** | **cévy i srdce** | **diltiazem** — mezi oběma skupinami; profylaxe anginy pectoris |

- **Indikace:** **hypertenze** (i v graviditě — nifedipin, amlodipin), **angina pectoris** včetně vazospastické (Prinzmetalovy), **supraventrikulární tachyarytmie a kontrola frekvence u fibrilace síní** (verapamil, diltiazem), Raynaudův fenomén, profylaxe migrény (flunarizin).
- **NÚ:** **otoky kolem kotníků** (dihydropyridiny — dilatace přívodných tepének), zrudnutí, bolest hlavy, reflexní tachykardie; u verapamilu/diltiazemu **bradykardie, AV blok, zácpa**, zhoršení srdečního selhání.
- **Kontraindikace a interakce:** ⚠️ **verapamil nebo diltiazem + β-blokátor (zvlášť i.v.) je kontraindikovaná kombinace** — sčítá se negativně chronotropní a dromotropní efekt → těžká bradykardie, AV blok, asystolie. Dále AV blok, systolické srdeční selhání, WPW syndrom. ⚠️ Metabolizují se přes **CYP3A4** — **grapefruitová šťáva a inhibitory CYP3A4 zvyšují jejich hladinu**.

🔑 **Dihydropyridiny = cévy · verapamil = srdce · diltiazem = obojí. Verapamil + β-blokátor = nikdy.**

❓ *Který BKK zvolíš u hypertenzního astmatika s tachyarytmií?* → **Verapamil** — kontroluje frekvenci a β-blokátor by astma zhoršil.

---

## 71 · Nitrity a nitráty

**O čem to je:** „dárci" oxidu dusnatého (NO) — látky, kterou si endotel vyrábí sám k rozšiřování cév. Nejdůležitější praktická věc je **smrtelná kombinace se sildenafilem**.

- 🔑 **Mechanismus — přesná kaskáda:** nitrát uvolní **NO** → aktivuje **guanylátcyklázu** → ↑ **cGMP** → aktivace **proteinkinázy G** → defosforylace myozinu a pokles Ca²⁺ → **relaxace hladkého svalu**. ⚠️ **cGMP odbourává fosfodiesteráza 5 (PDE5)** — proto její inhibitor efekt několikanásobně zesílí.
- **Hemodynamika:** převažuje **venodilatace** → ↓ návrat krve k srdci → **↓ předtížení a spotřeba kyslíku myokardem**; ve vyšší dávce i dilatace tepen a **věnčitých cév** (přerozdělení průtoku do ischemických oblastí). **Steal fenomén** = krev jde cestou nejmenšího odporu, tedy do zdravých cév, a ischemická oblast si pohorší.
- **Zástupci a podání:** **nitroglycerin** — ⚠️ **sublingválně (sprej, tableta) je lék první volby při záchvatu anginy pectoris**, nástup do 1–2 minut (obchází first-pass efekt, perorální dostupnost je jen ~30 %); **izosorbid-dinitrát a mononitrát** — profylaxe, perorálně; nitroglycerin i.v. u akutního koronárního syndromu a plicního edému; náplasti pro dlouhodobou profylaxi.
- **Indikace:** **akutní záchvat i profylaxe anginy pectoris**, akutní koronární syndrom, **akutní levostranné srdeční selhání a plicní edém**, hypertenzní krize.
- **NÚ:** **pulzující bolest hlavy** (dilatace mozkových cév — nejčastější), zrudnutí, **ortostatická hypotenze a reflexní tachykardie**, závratě.
- ⚠️ **Tolerance:** při nepřetržité expozici účinek během dní mizí → **nutný „nitrátový interval" 8–12 h denně bez léku** (náplast se na noc sundává).
- ⚠️ **Kontraindikace — nejčastější zkušební otázka:** **inhibitory PDE5 (sildenafil, tadalafil, vardenafil)** — oba mechanismy se sčítají (nitrát cGMP tvoří, sildenafil brání jeho odbourání) → **neztlumitelná vazodilatace a smrtelný pokles tlaku**. Dále: **hypotenze, hypovolemie, aortální stenóza, hypertrofická kardiomyopatie, infarkt pravé komory**, zvýšený nitrolební tlak.

❓ *Za jak dlouho po sildenafilu se nesmí podat nitrát?* → Podstatné je, že **kombinace je kontraindikovaná** (u sildenafilu se uvádí odstup ≥ 24 h, u tadalafilu ≥ 48 h) — jinak hrozí smrtelná hypotenze.

---

## 72 · Farmakoterapie srdečního selhání

**O čem to je:** srdce nestíhá pumpovat, tělo to kompenzuje sympatikem a RAAS — jenže **právě tahle kompenzace srdce dál ničí**. Proto léčba z velké části znamená kompenzaci zablokovat, ne pumpu posilovat.

- **Definice:** porucha srdeční funkce, při které srdce nepřečerpá tolik krve, kolik tkáně potřebují. Dělí se podle **ejekční frakce (EF)** — HFrEF (snížená, ≤ 40 %), HFmrEF (mírně snížená), HFpEF (zachovaná).
- 🔑 **Adaptační mechanismy, ze kterých plyne celá léčba:** nízký výdej → **aktivace sympatiku** (přes α vazokonstrikce = ↑ dotížení, přes β1 ↑ frekvence a spotřeba kyslíku + ↑ renin) → **aktivace RAAS** (angiotenzin II a aldosteron → retence sodíku a vody, fibróza a **remodelace myokardu**). Krátkodobě to pomůže, dlouhodobě srdce zabíjí.

| Cíl | Skupina | Zástupci a poznámka |
|---|---|---|
| **utlumit sympatikus** | **β-blokátory** | **bisoprolol, karvedilol, metoprolol ZOK, nebivolol** — ⚠️ **snižují mortalitu**; nasazovat **v malé dávce a pomalu titrovat**, nikdy při dekompenzaci |
| **utlumit RAAS** | **ACE inhibitory** (nebo **sartany** při kašli) | ramipril, perindopril, enalapril — **snižují mortalitu** |
| | **antagonisté aldosteronu** | **spironolakton, eplerenon** — snižují mortalitu; ⚠️ hlídat kalium |
| | (moderně **ARNI** — sakubitril/valsartan a **glifloziny**) `[doplněno]` | dnes standard u HFrEF |
| **odstranit městnání** | **diuretika** | **furosemid** (dušnost, otoky) — uleví od příznaků, ⚠️ **mortalitu nesnižují** |
| **posílit stah** | **pozitivně inotropní látky** | **digoxin** (fibrilace síní, přetrvávající příznaky), **dobutamin/dopamin, levosimendan** jen krátkodobě u akutního selhání a kardiogenního šoku |
| **zvládnout arytmie** | antiarytmika | **amiodaron** (ostatní třídy jsou u selhání rizikové), implantabilní defibrilátor |

- ⚠️ **Léky, které u srdečního selhání škodí:** **verapamil a diltiazem** (negativně inotropní), **NSA** (retence sodíku a vody, ↓ účinek diuretik a ACEI), glitazony, ⚠️ **β-blokátor nasazený při akutní dekompenzaci**.
- **Pravostranné selhání a plicní hypertenze:** **antagonisté endotelinu (bosentan)**, **inhibitory PDE5 (sildenafil)**, **prostacyklinová analoga (iloprost)**; při plicní embolii **antikoagulancia a trombolýza**; kyslík, diuretika.

🔑 **β-blokátory a inhibitory RAAS srdce neposilují — blokují kompenzaci, která ho ničí; proto jako jediné (spolu s antagonisty aldosteronu) snižují mortalitu. Diuretika uleví, ale život neprodlouží.**

❓ *Proč se β-blokátor u srdečního selhání nasazuje pomalu a v malé dávce?* → Na začátku sníží kontraktilitu a mohl by selhání akutně zhoršit; prospěch se projeví až po týdnech.

---

## 73 · Farmakoterapie ischemické choroby srdeční (ICHS)

**O čem to je:** myokard nedostává dost kyslíku, protože jsou zúžené věnčité tepny. Léčba se **liší podle formy** — stabilní vs. nestabilní.

- **ICHS** = nedostatečné okysličení myokardu, typicky aterosklerózou koronárních tepen. **Angina pectoris** = svíravá bolest za hrudní kostí, vystřeluje do krku, čelisti a levé paže. **Formy:** stabilní (námahová, ustupuje v klidu a po nitrátu), **Prinzmetalova/vazospastická** (klidová, ze spazmu), **nestabilní** a **akutní koronární syndrom**.
- **Princip léčby stabilní formy: snížit spotřebu kyslíku a zlepšit jeho dodávku.**

| Skupina | Jak pomáhá |
|---|---|
| **Nitráty** | venodilatace → ↓ předtížení a spotřeba kyslíku; sublingválně **lék volby na záchvat**, dlouhodobě profylakticky (s nitrátovým intervalem) |
| **β-blokátory** | ↓ frekvence a kontraktilita → ↓ spotřeba kyslíku, ⚠️ **prodloužená diastola zlepší plnění věnčitých tepen**; **základ dlouhodobé léčby**, snižují mortalitu po infarktu |
| **Blokátory kalciových kanálů** | vazodilatace koronárních tepen — ⚠️ **lék volby u Prinzmetalovy (vazospastické) anginy**; verapamil/diltiazem tam, kde nelze β-blokátor |
| **Ivabradin** `[doplněno]` | zpomaluje SA uzel bez vlivu na kontraktilitu — když β-blokátor nestačí nebo nelze |
| **Prognostická léčba (u všech!)** | **kyselina acetylsalicylová** (antiagregace), **statin**, **ACE inhibitor** |

- **Nestabilní angina a akutní koronární syndrom:** ⚠️ **těžiště je v protisrážlivé léčbě, ne v úlevě od bolesti** — **duální antiagregace (ASA + klopidogrel/tikagrelor)**, **antikoagulace (LMWH nebo heparin)**, β-blokátor, statin, nitrát; **morfin na bolest**; kyslík při hypoxii.
- **Infarkt myokardu:** **ruptura aterosklerotického plátu → nasedající trombus → uzávěr tepny**. ⚠️ **K nekróze celé tloušťky stěny dojde asi do 6 hodin** — proto se musí co nejdřív obnovit průtok: **primární PCI (katetrizace)**, případně **trombolýza**. Následně trvale ASA + P2Y12 inhibitor, β-blokátor, ACEI, statin.

🔑 **Stabilní AP = snižuj spotřebu kyslíku (nitráty, β-blokátory, BKK) + prognostická trojice ASA, statin, ACEI. Nestabilní AP a infarkt = rozpusť/odstraň trombus, čas je sval.**

❓ *Proč β-blokátor zlepší prokrvení srdce, i když cévy nerozšiřuje?* → Zpomalí tep → **prodlouží diastolu**, a věnčité tepny se plní právě v diastole.

---

## 74 · Antihypertenziva

**O čem to je:** u 95 % pacientů se příčina nezná — léčba proto **není kauzální**, ale brání poškození cév, srdce, mozku a ledvin.

- **Hypertenze** = opakovaně naměřený tlak **≥ 140/90 mm Hg**. **Primární (esenciální) v 95 %** — bez zjevné příčiny; **sekundární** — renální, renovaskulární, endokrinní (hyperaldosteronismus, feochromocytom), polékové.
- ⚠️ **Bludný kruh s aterosklerózou:** hypertenze poškodí endotel → chybí NO a prostacyklin, převáží vazokonstrikce → tlak dál stoupá; vysoký tlak navíc trhá aterosklerotické pláty.
- **Metabolický syndrom** = hypertenze + centrální obezita + porucha glukózové tolerance / diabetes 2. typu + dyslipidemie. **Základ léčby je nefarmakologický:** omezení soli a živočišných tuků, redukce hmotnosti, pohyb, nekouřit, omezit alkohol.
- **Tři mechanismy, kterými antihypertenziva fungují:** ① **vazodilatace** ② **↓ srdeční výdej** (frekvence a kontraktilita) ③ **odstranění sodíku a vody**.

| Skupina (první volba) | Podstatné | NÚ / KI |
|---|---|---|
| **ACE inhibitory / sartany** | ↓ angiotenzin II a aldosteron, **renoprotektivní** — volba u diabetika a nefropatie | kašel (ACEI), hyperkalemie, angioedém · ⚠️ **KI gravidita, stenóza renálních tepen** |
| **Blokátory kalciových kanálů** | vazodilatace; volba u seniorů a **v graviditě** (nifedipin) | otoky kotníků, návaly, zácpa (verapamil) · KI AV blok (verapamil) |
| **Thiazidová diuretika** | ↓ objem, po 2 týdnech ↓ periferní odpor | hypokalemie, hyperurikemie, hyperglykemie · KI dna |
| **β-blokátory** | ↓ výdej a renin; volba při **ICHS, po infarktu, u srdečního selhání a tachyarytmií** | únava, studené končetiny, bronchospasmus, maskování hypoglykemie · ⚠️ KI **astma, AV blok, bradykardie** |

- **Druhá a další volba:** **antagonisté aldosteronu (spironolakton)** — lék volby u **rezistentní hypertenze**; **α1-blokátory** (doxazosin, výhodné při hyperplazii prostaty); **centrálně působící α2-agonisté** — ⚠️ **methyldopa je volba v graviditě**, dále moxonidin, rilmenidin; přímá vazodilatancia (hydralazin, minoxidil).
- ⚠️ **Přes 70 % pacientů potřebuje kombinaci dvou a víc léků** — kombinují se skupiny s odlišným mechanismem (typicky ACEI/sartan + BKK + thiazid), a nikdy ACEI se sartanem.
- **Hypertenzní krize:** i.v. léčba (nitroglycerin, urapidil, labetalol) — tlak se snižuje **postupně**, prudký pokles hrozí mozkovou ischemií.

❓ *Které antihypertenzivum zvolíš u těhotné?* → **Methyldopa**, alternativně nifedipin nebo labetalol; **ACEI a sartany jsou kontraindikované**.

---

## 75 · Farmakoterapie aterosklerózy, hyperlipidemie

**O čem to je:** vysoký cholesterol nebolí, ale tiše ničí cévy — léčí se **preventivně**. Standardem jsou statiny.

- **Hyperlipidemie** = zvýšená koncentrace lipidů a lipoproteinů v krvi · **dyslipidemie** = porušený **poměr** mezi nimi (i při normálním celkovém množství). Následek: **ateroskleróza** (ICHS, CMP, ischemie končetin) a při vysokých triglyceridech **akutní pankreatitida**.

| Lipid | Cílová hranice |
|---|---|
| celkový cholesterol | **do 5,2 mmol/l** |
| **LDL** („zlý") | **do 3 mmol/l** (u vysoce rizikových výrazně méně) |
| **triacylglyceroly** | **do 1,7 mmol/l** |

- **Základ je nefarmakologický:** dieta s omezením živočišných tuků, redukce hmotnosti, pohyb, nekouřit, omezit alkohol.

| Skupina | Mechanismus, indikace, NÚ |
|---|---|
| **Statiny** (atorvastatin, rosuvastatin, simvastatin) | ⚠️ **lék první volby**: blokují **HMG-CoA reduktázu**, klíčový enzym syntézy cholesterolu v játrech → játra si **zvýší počet LDL receptorů** → z krve zmizí LDL. Snižují i triglyceridy a mají protizánětlivý („pleiotropní") efekt — **stabilizují plát**. **NÚ: myalgie, ↑ jaterní testy, vzácně rabdomyolýza** (riziko roste s fibráty a s inhibitory CYP3A4 — ⚠️ **grapefruit**). **KI: gravidita, aktivní jaterní onemocnění** |
| **Ezetimib** | blokuje **transportér cholesterolu v kartáčovém lemu střeva** → méně cholesterolu do jater → opět ↑ LDL receptory. Kombinace se statinem nebo při jeho nesnášenlivosti |
| **Inhibitory PCSK9** (alirokumab, evolokumab) | **monoklonální protilátky** — brání degradaci LDL receptorů → jater vychytají víc LDL; podkožní injekce à 2–4 týdny; **familiární hypercholesterolemie a velmi vysoké riziko**. NÚ: reakce v místě vpichu |
| **Fibráty** (fenofibrát) | agonisté **PPAR-α** → ↑ lipoproteinová lipáza → ⚠️ **hlavně snižují triglyceridy** a zvyšují HDL. Indikace: výrazná hypertriglyceridemie. NÚ: myopatie (⚠️ zvlášť se statinem), žlučové kameny |
| **Pryskyřice** (cholestyramin, kolesevelam) | vážou **žlučové kyseliny** ve střevě a přeruší jejich enterohepatální oběh → játra je tvoří z cholesterolu → ↑ LDL receptory. Nevstřebávají se. **NÚ: zácpa, nadýmání, ⚠️ vážou i vitaminy A, D, E, K a jiné léky** (podávat s odstupem) |

🔑 **Statiny = blokují výrobu cholesterolu · ezetimib = blokuje jeho vstřebávání · pryskyřice = přeruší jeho koloběh · fibráty = na triglyceridy. Všechny „nestatiny" nakonec fungují přes zvýšení počtu LDL receptorů v játrech.**

❓ *Proč je kombinace statinu s fibrátem riziková?* → Sčítá se **myotoxicita** → riziko rabdomyolýzy a selhání ledvin z myoglobinu.

---

## 76 · Parenterální antikoagulancia

**O čem to je:** injekční léky proti srážení — posilují **přirozenou brzdu srážení (antitrombin III)**, místo aby faktory blokovaly přímo.

- **Hemostáza ve třech fázích** (řekni na úvod O76 i O77): ① **cévní** — okamžitá vazokonstrikce, rovnováha mezi TXA₂ a serotoninem (stah) a PGI₂ z endotelu (dilatace) ② **destičková** — adheze a agregace destiček → **bílý trombus** ③ **koagulační** — tkáňový faktor spustí kaskádu → trombin → fibrin → **červený trombus** (fibrin + erytrocyty). Srážení drží v mezích **antitrombin III, protein C a S**; velikost trombu koriguje **fibrinolýza** (plazminogen → plazmin).
- **Dělení antitrombotik:** **antiagregancia → tepenný trombus** · **antikoagulancia → žilní trombus** · **trombolytika → rozpuštění už vzniklého trombu**.
- **Nefrakcionovaný heparin (UFH)**
  - **Mechanismus:** sám nic neblokuje — **naváže se na antitrombin III a zvýší jeho účinnost až 1000×**; komplex pak inaktivuje **trombin (IIa) a faktory Xa, IXa, XIIa**.
  - **Kinetika:** i.v. (nebo s.c.), **nástup okamžitý**, účinek 12–18 h, zůstává v cévním řečišti. ⚠️ **Neprochází placentou ani do mléka → antikoagulans volby v graviditě.**
  - ⚠️ **Nutná monitorace APTT** (norma 35–45 s, cíl **1,5–2,5násobek**).
  - **Indikace:** akutní tromboembolická nemoc, akutní koronární syndrom, **mimotělní oběh a hemodialýza**, nesrážlivá krev pro laboratoř.
  - **NÚ:** **krvácení** (⚠️ **antidotum protamin sulfát**), ⚠️ **heparinem indukovaná trombocytopenie (HIT)** — typ I benigní neimunitní, **typ II imunitní, paradoxně trombotický a nebezpečný**, dlouhodobě **osteoporóza**, hypoaldosteronismus s hyperkalemií.
  - **Rezistence:** vrozený **deficit antitrombinu III** (~1 % populace), vysoký faktor VIII.
- **Nízkomolekulární hepariny (LMWH) — enoxaparin, nadroparin, dalteparin, bemiparin**
  - Působí přes ATIII hlavně proti **faktoru Xa**; **s.c. 1–2× denně**, ⚠️ **předvídatelný účinek → nemusí se monitorovat** (jen u renální insuficience, obezity a v graviditě se měří **anti-Xa aktivita**); nižší riziko HIT a osteoporózy. Vylučují se **ledvinami** → ⚠️ pozor při renálním selhání. Antidotum protamin jen **částečně** účinný.
  - **Indikace:** profylaxe i léčba hluboké žilní trombózy a plicní embolie, akutní koronární syndrom, **antikoagulace v graviditě**.
- **Fondaparinux** — syntetický pentasacharid, přes ATIII inhibuje **výhradně faktor Xa**; s.c., **nevyvolává HIT**, antidotum nemá. *(Proč zrovna Xa: sbíhá se v něm vnitřní i zevní cesta — Xa dělá z protrombinu trombin.)*

🔑 **Heparin = okamžitý účinek, monitorace APTT, antidotum protamin. LMWH = předvídatelný, bez monitorace, s.c. Oba jsou bezpečné v graviditě, protože neprocházejí placentou.**

❓ *Co je HIT typu II a proč je nebezpečná?* → Imunitní reakce proti komplexu heparin-destičkový faktor 4 → destičky ubývají, ale zároveň se **aktivují** → **trombózy** i při nízkých destičkách; heparin se musí okamžitě vysadit.

---

## 77 · Perorální antikoagulancia

**O čem to je:** protisrážlivé léky ústy — buď **přímé (DOAC)**, nebo klasický **warfarin**, který působí oklikou přes vitamin K.

| DOAC | Mechanismus a antidotum |
|---|---|
| **Dabigatran** (gatran) | **přímý inhibitor trombinu**; ⚠️ **antidotum idarucizumab** (monoklonální protilátka) |
| **Rivaroxaban, apixaban, edoxaban** (xabany) | **přímé inhibitory faktoru Xa**; ⚠️ **antidotum andexanet alfa** (návnadová forma faktoru Xa bez aktivity) |

- **Výhody DOAC:** rychlý nástup, fixní dávka, **bez rutinní monitorace**, málo potravinových interakcí. **Indikace: prevence CMP u nevalvulární fibrilace síní, léčba a profylaxe hluboké žilní trombózy a plicní embolie, profylaxe po velkých ortopedických operacích.** ⚠️ **KI: mechanická chlopenní náhrada a těžká mitrální stenóza** (tam jen warfarin), těžká renální insuficience, gravidita.
- **Warfarin**
  - 🔑 **Mechanismus:** faktory **II, VII, IX, X a proteiny C a S** musí být **karboxylovány** (γ-glutamylkarboxylázou), a k tomu je potřeba **redukovaný vitamin K**. Warfarin blokuje **vitamin K-reduktázu**, která vitamin K regeneruje → do krve jdou jen **nefunkční prekurzory**, které neumí vázat vápník. ⚠️ **Proto účinkuje jen in vivo — ve zkumavce srážení neovlivní.**
  - ⚠️ **Proč se na začátku kombinuje s LMWH:** **protein C a S mají nejkratší poločas**, takže klesnou jako první — **první dny je pacient paradoxně v hyperkoagulačním stavu** (odtud i **kumarinová kožní nekróza**). Plný účinek nastupuje za 3–5 dní.
  - **Monitorace: protrombinový čas jako INR** (obvykle cíl 2–3). Kinetika: dobře se vstřebává, silně se váže na albumin, metabolizuje se **CYP2C9** (⚠️ polymorfismus, viz O26). ⚠️ **Prochází placentou a je teratogenní (fetální warfarinový syndrom)**, do mléka ale neprochází.
  - ⚠️ **Interakce — nejčastější zdroj problémů:** potraviny bohaté na **vitamin K** (listová zelenina) účinek **snižují**; **antibiotika** (vyhubí střevní flóru produkující vitamin K), **amiodaron, metronidazol, azolová antimykotika, ASA a NSA** účinek **zesilují** → krvácení; **rifampicin, karbamazepin, třezalka** ho **oslabují**.
  - **Antidotum: vitamin K** (fytomenadion), při život ohrožujícím krvácení **koncentrát protrombinového komplexu nebo čerstvě mražená plazma**.

| Antidotum | Proti čemu |
|---|---|
| **protamin sulfát** | heparin (LMWH jen částečně) |
| **vitamin K + protrombinový komplex** | warfarin |
| **idarucizumab** | dabigatran |
| **andexanet alfa** | xabany |

⚠️ **Pro tebe jako zubařku:** u pacienta na warfarinu se před extrakcí rozhoduje **podle aktuálního INR** (běžná extrakce se při terapeutickém INR obvykle nevysazuje, doplní se lokální hemostáza — oxycelulóza, tranexamová kyselina k výplachu), u DOAC podle **času od poslední dávky**. Konkrétní protokol je věc tvého pracoviště. `[obecné znalosti]`

❓ *Proč warfarin nefunguje ve zkumavce?* → Nezasahuje do kaskády přímo — blokuje **jaterní regeneraci vitaminu K**, tedy tvorbu faktorů; bez živého metabolismu nemá kde působit.

---

## 78 · Fibrinolytika, trombolytika, hemostatika

**O čem to je:** dva opačné cíle v jedné otázce — **rozpustit trombus, který už vznikl** (trombolytika) a **zastavit krvácení** (hemostatika, včetně těch, které budeš používat po extrakci).

- **Fibrinolytika (trombolytika)** — **mechanismus:** aktivují přeměnu **plazminogenu na plazmin**, a ten štěpí **fibrin** na degradační produkty → trombus se rozpustí.
  - **Zástupci: altepláza** (rekombinantní tkáňový aktivátor plazminogenu, rt-PA), **retepláza, tenektepláza** (rychlejší nástup, delší účinek, jednorázový bolus), historicky streptokináza a urokináza.
  - **Indikace:** ⚠️ **akutní ischemická cévní mozková příhoda (do 4,5 h)**, akutní infarkt myokardu tam, kde není dostupná katetrizace, **masivní plicní embolie**, uzávěr tepny končetiny, ucpaný centrální žilní katétr.
  - **NÚ a KI:** ⚠️ **krvácení, hlavně intrakraniální**; KI: čerstvé krvácení, stav po CMP, nedávná operace či úraz, těžká nekorigovaná hypertenze, aneuryzma, jaterní selhání.
- **Antifibrinolytika** — opak: brání přeměně plazminogenu na plazmin (**kyselina tranexamová**, kyselina aminokapronová) nebo blokují už vzniklý plazmin (aprotinin). **Indikace:** krvácení při hyperfibrinolýze, krvácení po trombolýze, silná menstruace, ⚠️ **výplach nebo tampon po stomatologickém výkonu u antikoagulovaného pacienta** (kyselina tranexamová).
- **Hemostatika pro místní účinek** — ⚠️ **tenhle odstavec je pro tvou praxi klíčový:**
  - **oxycelulóza** — v kontaktu s krví nabobtná, vytvoří mechanickou zátku a urychlí adhezi destiček; **standard po extrakci zubu**,
  - **kolagenová houbička** (i s gentamicinem), **fibrinové a trombinové lepidlo** (fibrinogen + trombin ± aprotinin) — vytvoří sraženinu přímo v ráně,
  - **adsorbenty** — rostlinné polysacharidy (škroby), v krvi zgelovatí a zkoncentrují krevní buňky a faktory,
  - **vazokonstrikční látky** — ⚠️ **felypresin** (analog vazopresinu) je vazokonstrikční přísada v **prilokainovém dentálním anestetiku**, alternativa adrenalinu u srdečního pacienta,
  - **etamsylát** — zlepšuje adhezi destiček a odolnost kapilár, i.v./i.m./perorálně u kapilárního krvácení.
- **Hemostatika pro systémový účinek:**
  - **koagulační faktory** — ⚠️ **hemofilie A = vrozený deficit faktoru VIII**, **hemofilie B = vrozený deficit faktoru IX** (Christmasův); projev: **krvácení do velkých kloubů a svalů**, otok, bolest, porucha hybnosti. Dnes rekombinantní faktory s prodlouženým poločasem (dřív plazma → vysoké riziko infekcí),
  - **fibrinogen**, **koncentrát protrombinového komplexu** (rychlá náprava účinku warfarinu),
  - **vitamin K** — nutný pro faktory II, VII, IX, X; ⚠️ **antagonista warfarinu**; podává se novorozencům jako prevence krvácivé nemoci, dále při malabsorpci tuků (ke vstřebání potřebuje žlučové kyseliny),
  - **antidota antikoagulancií** — protamin, idarucizumab, andexanet alfa.

⚠️ **Hemofilie je VROZENÁ (dědičná, X-vázaná) porucha** — některé studentské materiály ji chybně uvádějí jako získanou. Získaná porucha srážlivosti je např. ta po warfarinu nebo při jaterním selhání.

❓ *Jaká hemostatika použiješ po extrakci zubu?* → **Oxycelulóza nebo kolagenová houbička** do lůžka, komprese, u antikoagulovaného navíc **kyselina tranexamová** k výplachu.

---

## 79 · Antiagregancia

**O čem to je:** protidestičkové léky brání trombóze **v tepnách** (antikoagulancia řeší žíly). Nejznámější je aspirin v nízké dávce.

- **Arteriální trombóza** vzniká **rupturou aterosklerotického plátu** → destičkový (bílý) trombus → infarkt, CMP, ischemie končetiny. **Venózní tromboembolismus** vzniká ze stázy a hyperkoagulace → fibrinový (červený) trombus → hluboká žilní trombóza a plicní embolie.
- **Kyselina acetylsalicylová (ASA)**
  - 🔑 **Mechanismus — vysvětli jako rovnováhu:** destičky tvoří **TXA₂** (agregace + vazokonstrikce), endotel **PGI₂** (opak). ASA **ireverzibilně acetyluje COX-1**; ⚠️ **destička nemá jádro, novou COX-1 si nevyrobí → efekt trvá celou její životnost (~7–10 dní, klinicky ~5 dní)**, zatímco endotel si enzym obnoví. Proto **nízká dávka (75–100 mg) působí selektivně antiagregačně**.
  - **Indikace:** sekundární prevence po infarktu, CMP a stentu, ischemická choroba dolních končetin.
  - **NÚ a KI:** krvácení do GIT, vředy, aspirinem indukované astma; ⚠️ **před invazivním výkonem se u kardiaka obvykle NEVYSAZUJE** — riziko trombózy převáží nad krvácením z extrakce.
  - ⚠️ **Interakce: ibuprofen soutěží o stejné vazebné místo na COX-1 a ruší antiagregační efekt ASA** — proto se ASA bere alespoň 2 h před ibuprofenem.
- **Blokátory receptoru P2Y12 (ADP receptoru):**

| Léčivo | Podstatné |
|---|---|
| **Klopidogrel** | **proléčivo — aktivuje se přes CYP2C19**, ⚠️ u pomalých metabolizátorů a při současném omeprazolu nezabere; ireverzibilní, nástup hodiny |
| **Prasugrel** | také proléčivo, rychlejší a spolehlivější, ale vyšší riziko krvácení |
| **Tikagrelor, kangrelor** | **reverzibilní**, aktivují se přímo (bez jater), nástup v minutách |

- **Duální antiagregace (ASA + P2Y12 inhibitor)** — po akutním koronárním syndromu a implantaci stentu, obvykle **12 měsíců**; ⚠️ elektivní výkony se v téhle době odkládají.
- **Ostatní:** **inhibitory GP IIb/IIIa** (abciximab, eptifibatid) — i.v. při katetrizaci, nejsilnější antiagregace; **dipyridamol** (↑ cAMP), **epoprostenol** (PGI₂) při hemodialýze, když nelze heparin.

🔑 **Aspirin blokuje COX-1 nevratně → jedna dávka vyřadí destičku natrvalo. Klopidogrel je proléčivo — potřebuje CYP2C19, jinak nefunguje.**

❓ *Proč ruší ibuprofen účinek aspirinu?* → Obsadí stejné místo na COX-1 reverzibilně a **zabrání aspirinu, aby enzym trvale acetyloval**.

---

## 80 · Inzulin, jeho analoga a glukagon

**O čem to je:** dva hormony slinivky, které dělají přesný opak — **inzulin snižuje** glykemii, **glukagon zvyšuje**.

- **Inzulin:** tvoří ho **β-buňky** Langerhansových ostrůvků (20–40 IU/den); polypeptid ze dvou řetězců spojených disulfidickými můstky. ⚠️ **Při jeho vzniku se odštěpí C-peptid — jeho hladina ukazuje, kolik VLASTNÍHO inzulinu člověk tvoří** (podaný inzulin C-peptid neobsahuje).
- **Mechanismus:** naváže se na **inzulinový receptor** (tyrozinkináza) v játrech, svalu a tukové tkáni → přesun transportérů **GLUT4** do membrány → glukóza vstoupí do buňky; k tomu ↑ glykogeneze, lipogeneze a proteosyntéza, ↓ glukoneogeneze. **Nejsilnějším podnětem k sekreci je glukóza.** Protihráči: **glukagon, adrenalin, kortizol, růstový hormon**.
- ⚠️ **Inzulin přesouvá draslík do buněk — proto se glukóza s inzulinem i.v. používá v urgentní medicíně na léčbu hyperkalemie.** Oblíbená doplňující otázka.

| Typ | Charakteristika |
|---|---|
| **humánní (HM)** | rekombinantní technologií z *E. coli*; krátkodobý (regular) a střednědobý (NPH) |
| **analoga** | upravené pořadí aminokyselin → lepší profil: **ultrakrátká** (lispro, aspart, glulisin — k jídlu) a **dlouhodobá bazální** (glargin, detemir, degludek — bez vrcholu) |
| **premixované** | fixní směs krátkého a dlouhého — pro pacienty s horší spoluprací |

- **Režim:** ⚠️ **bazál-bolus** (dlouhodobý bazál + krátké bolusy k jídlu) = intenzifikovaný režim, standard u **diabetu 1. typu**; u **2. typu** se přidává při selhání PAD.
- **Kinetika:** ⚠️ **perorálně nelze** — je to bílkovina, proteázy v GIT ji rozloží; podává se **s.c.** (i.v. jen na JIP). Vstřebávání kolísá podle prokrvení a místa vpichu (**z břicha rychleji než ze stehna**). Exogenní inzulin se z > 60 % odbourá v ledvinách → ⚠️ **při renální insuficienci se dávka snižuje**.
- **NÚ:** ⚠️ **hypoglykemie** (pocení, třes, hlad, zmatenost → kóma), přírůstek hmotnosti, lipodystrofie a lokální reakce v místě vpichu, hypokalemie.
- **Interakce:** sulfonylurea a alkohol riziko hypoglykemie **zvyšují**; ⚠️ **β-blokátory maskují její varovné příznaky**; kortikoidy, hypertyreóza, stres a infekce potřebu inzulinu **zvyšují**.
- **Glukagon:** z **α-buněk**; při poklesu glykemie spustí v játrech **glykogenolýzu a glukoneogenezi**. **Indikace: těžká hypoglykemie — i.m. nebo s.c., zvládne ji podat i laik** (rodinný příslušník); poločas 5–6 min. NÚ: nauzea až u 30 %. **KI: feochromocytom.** ⚠️ **Nefunguje, když nejsou zásoby glykogenu** — u hladovění, jaterního selhání a **hypoglykemie z alkoholu**; po probrání musí pacient sníst sacharidy, jinak se hypoglykemie vrátí.

❓ *Proč glukagon nezabere u opilého pacienta v hypoglykemii?* → Alkohol blokuje glukoneogenezi a zásoby glykogenu jsou vyčerpané — glukagon nemá z čeho glukózu uvolnit; nutná je **glukóza i.v.**

---

## 81 · Perorální antidiabetika (PAD)

**O čem to je:** léčba diabetu 2. typu, kde tělo inzulin ještě tvoří — jen ho **nedokáže využít** (rezistence), nebo ho tvoří **stále míň**. **Metformin je lék první volby.**

- **Dva fenotypy 2. typu, z nichž plyne volba léku:** **inzulinová rezistence** → vysoká glykemie **nalačno** (sekrece zatím kompenzuje) · **selhávající sekrece** → vysoká glykemie **po jídle**.

| Skupina | Mechanismus, výhody, NÚ |
|---|---|
| **Metformin (biguanid)** | ⚠️ **lék první volby**: ↓ glukoneogenezi v játrech, ↑ citlivost tkání k inzulinu, zpomalí vstřebávání glukózy ve střevě. **Nezpůsobuje hypoglykemii, mírně snižuje hmotnost a LDL, prokazatelně snižuje mortalitu.** NÚ: **průjem a dyspepsie** (mírní retardovaná forma), dlouhodobě deficit **vitaminu B12** |
| **Deriváty sulfonylurey** (gliklazid, glimepirid) | zavírají K⁺ kanál na β-buňce → **stimulují sekreci inzulinu** (nutná zachovaná funkce slinivky). ⚠️ **Hypoglykemie a přírůstek hmotnosti** — sekreci zvýší i při už nízké glykemii |
| **Glitazony** (pioglitazon) | agonisté **PPAR-γ** → ↓ inzulinová rezistence; plný efekt až po měsících. NÚ: **retence tekutin, otoky, přírůstek hmotnosti, zlomeniny**. ⚠️ **KI: srdeční selhání**, jaterní selhání, karcinom močového měchýře |
| **Gliptiny** (inhibitory DPP-4 — sitagliptin, linagliptin) | brzdí odbourávání vlastního **GLP-1** (inkretin: ↑ inzulin, ↓ glukagon, ↓ chuť k jídlu). ⚠️ **Efekt je glukózo-dependentní → hypoglykemie prakticky nehrozí**; hmotnostně neutrální |
| **Glifloziny** (inhibitory SGLT-2 — dapagliflozin, empagliflozin) | blokují zpětné vstřebávání glukózy v proximálním tubulu → **glykosurie**; ↓ hmotnost a tlak, ⚠️ **snižují mortalitu u srdečního selhání a chrání ledviny**. NÚ: **genitální mykózy a uroinfekce**, dehydratace, ⚠️ **euglykemická ketoacidóza** |
| **agonisté GLP-1** (liraglutid, semaglutid) `[doplněno]` | injekční, ale patří sem logicky: silná redukce hmotnosti a kardiovaskulárního rizika |

⚠️ **Laktátová acidóza po metforminu — nejzávažnější věc otázky.** Vzniká prakticky jen při **nedodržení kontraindikací**: **renální insuficience** (metformin se vylučuje ledvinami), hypoxie, srdeční a jaterní selhání, alkohol, sepse, ⚠️ **podání jodové kontrastní látky** (metformin se před vyšetřením vysazuje). **Funkce ledvin se kontroluje minimálně 1× ročně; úmrtnost laktátové acidózy je kolem 50 %.**

🔑 **Metformin = první volba, bez hypoglykemie, pozor na ledviny. Sulfonylurea = hypoglykemie a přibírání. Gliptiny a glifloziny = hypoglykemie prakticky nehrozí, protože účinek závisí na aktuální glykemii.**

❓ *Proč se metformin vysazuje před CT s kontrastem?* → Kontrast může zhoršit funkci ledvin → metformin se kumuluje → **laktátová acidóza**.

---

## 82 · Principy antibiotické terapie

**O čem to je:** obecná pravidla, než se dostaneš ke konkrétním skupinám — jak se antibiotika dělí, čím se řídí dávkování a co si rozmyslet, než je předepíšeš.

- **Bakteriostatická** — reverzibilně zastaví růst a množení; ⚠️ **potřebují funkční imunitu pacienta**, efekt je vidět za 3–4 dny (tetracykliny, makrolidy, linkosamidy, sulfonamidy, chloramfenikol). **Baktericidní** — bakterii přímo usmrtí, nevratně a rychle; nutná u **endokarditidy, meningitidy, sepse a u imunokompromitovaných** (betalaktamy, aminoglykosidy, chinolony, glykopeptidy, metronidazol).
- 🔑 **Dělení podle farmakodynamiky (určuje dávkovací režim):** **na koncentraci závislá** (aminoglykosidy, chinolony, metronidazol) — rozhoduje **výška vrcholu**, dávkují se **ve vyšší dávce méně často** · **na čase závislá** (betalaktamy, makrolidy) — rozhoduje, **jak dlouho je koncentrace nad MIC**, dávkují se **častěji nebo v infuzi**.
- **Podle distribuce:** **hydrofilní** (betalaktamy, aminoglykosidy) — malý distribuční objem, do buněk se nedostanou, vylučují se **ledvinami** · **lipofilní** (makrolidy, chinolony, tetracykliny) — velký distribuční objem, **pronikají do buněk** (nitrobuněčné patogeny), metabolizují se v játrech.
- **MIC (minimální inhibiční koncentrace)** = nejnižší koncentrace, která zastaví růst daného mikroba — základ pro hodnocení citlivosti.
- **Pět otázek před nasazením ATB:** ① Je to vůbec bakteriální infekce? ② Odebral jsem materiál na kultivaci **před** podáním? ③ Který patogen je nejpravděpodobnější? ④ Které ATB je nejvhodnější (spektrum, průnik do místa infekce, rezistence, cena)? ⑤ Má tenhle pacient omezení (**alergie, gravidita, kojení, ledviny, interakce**)?
- **Rezistence:** **primární (přirozená)** — mikrob je necitlivý od začátku, bez předchozího kontaktu (streptokoky × aminoglykosidy) · **sekundární (získaná)** — vzniká mutací nebo přenosem genu na **plazmidu**, příčinou je nadužívání a nesprávné dávkování. **Mechanismy:** produkce **betalaktamáz**, změna cílové struktury, snížená propustnost stěny, **efluxní pumpy**.
- **Zásady:** správná indikace (⚠️ **ne na virózy**), cílená léčba podle kultivace, dostatečná dávka a délka léčby (**nedokončená kúra plodí rezistenci**), u ATB s úzkým oknem (aminoglykosidy, vankomycin) **monitorace hladin**.

❓ *Kdy je nutné baktericidní, ne bakteriostatické antibiotikum?* → U **endokarditidy, meningitidy, sepse a u pacientů s oslabenou imunitou** — bakteriostatikum se tam bez pomoci imunity neobejde.

---

## 83 · Peniciliny, inhibitory betalaktamáz

**O čem to je:** nejstarší a stále nejdůležitější skupina antibiotik. ⚠️ **Penicilin V je pro tebe jako zubařku lék první volby na infekce ústní dutiny.**

- **Mechanismus:** **β-laktamový kruh** blokuje **transpeptidázu (PBP — penicillin binding protein)** → nemůže vzniknout příčná vazba peptidoglykanu → **bakterie si nedostaví buněčnou stěnu a praskne**. ⚠️ **Baktericidní, ale jen na rostoucí a dělící se bakterie**, a **na čase závislé** (rozhoduje doba nad MIC → dávkovat často).
- **Kinetika:** vstřebání z GIT závisí na odolnosti vůči žaludeční kyselině a snižuje ho jídlo (podávat 1 h před nebo 2 h po jídle). Do buněk nepronikají; do CNS jen málo — ⚠️ **ale při zánětu mozkových blan koncentrace stoupá, proto fungují u meningitidy**. Vylučují se **ledvinami**.

| Skupina | Spektrum a indikace |
|---|---|
| **Penicilin G (benzylpenicilin)** | i.v./i.m.; **streptokoky, pneumokoky, meningokoky, treponema (syfilis), borrelie, klostridia, aktinomycety, listerie**. Lék volby: **meningokoková a pneumokoková meningitida a sepse, streptokoková endokarditida, syfilis, plynatá sněť, aktinomykóza**. Prokain-penicilin = depotní i.m. forma |
| **Penicilin V (fenoxymetylpenicilin)** | perorální — ⚠️ **odolný vůči žaludeční kyselině**; **lék první volby u streptokokové tonzilofaryngitidy a INFEKCÍ ÚSTNÍ DUTINY (stomatologie)**, erysipel, lehčí infekce dýchacích cest |
| **Antistafylokokové (oxacilin, kloxacilin)** | ⚠️ **odolné vůči stafylokokové betalaktamáze** → volba u infekcí *Staphylococcus aureus* (ne však MRSA) |
| **Aminopeniciliny (ampicilin i.v., amoxicilin p.o.)** | spektrum penicilinu **+ G− bakterie**: *E. coli*, *Proteus*, *Haemophilus*, salmonely, enterokoky, *Helicobacter*. Indikace: infekce dýchacích cest, otitida, sinusitida, močové infekce, eradikace *H. pylori* |
| **Ureidopeniciliny (piperacilin)** | + **pseudomonády** a další problémové G− kmeny; ⚠️ **s tazobaktamem má nejširší spektrum ze všech penicilinů** — nemocniční a těžké infekce |
| **Potencované (chráněné)** | **amoxicilin + kyselina klavulanová** (koamoxicilin), ampicilin + sulbaktam, piperacilin + tazobaktam |

- **Inhibitory betalaktamáz** (**kyselina klavulanová, sulbaktam, tazobaktam**) — ⚠️ **samy nejsou antibiotika**: obětují se jako „návnada" a **vyvážou bakteriální betalaktamázu**, čímž ochrání penicilin před rozštěpením. Rozšíří spektrum o kmeny produkující betalaktamázu (*S. aureus*, *H. influenzae*, *E. coli*, *Klebsiella*).
- **Nežádoucí účinky:** ⚠️ **alergie — nejčastější léková alergie vůbec** (od exantému po anafylaxi; **75 % anafylaktických šoků způsobují peniciliny**, viz O30), průjem a dysmikrobie (u koamoxicilinu nejčastěji), **pseudomembranózní kolitida**, u vysokých dávek křeče, ↓ vitaminu K.
- ⚠️ **Hoigného syndrom** — po (technicky chybném, příliš rychlém) i.m. podání depotní penicilinové suspenze do cévy: úzkost, dechová tíseň, kolaps, halucinace. **NENÍ to alergie**, ale mikroembolizace — proto se pacient po výkonu nevyřazuje z penicilinové léčby.

❓ *Co je penicilin volby na dentální infekci a proč?* → **Penicilin V** — je odolný vůči žaludeční kyselině (dá se podat ústy) a pokrývá orální streptokoky a anaeroby; u alergie na penicilin **klindamycin**.

---

## 84 · Cefalosporiny, karbapenemy, monobaktamy

**O čem to je:** „příbuzní" penicilinů v pěti generacích (s každou roste síla proti G− bakteriím) + karbapenemy jako **rezerva na multirezistentní kmeny**.

- **Mechanismus:** stejný jako u penicilinů — **betalaktamový kruh blokuje syntézu buněčné stěny**, baktericidní, na čase závislé. Proti penicilinům jsou **odolnější vůči betalaktamázám**; ⚠️ **zkřížená alergie s peniciliny asi u 5–10 %**. Vylučují se hlavně **ledvinami**.

| Generace | Spektrum a použití | Zástupci |
|---|---|---|
| **1.** | hlavně **G+ koky**, částečně *E. coli* a *Proteus*; ⚠️ **neprocházejí do likvoru → ne u meningitidy**; alternativa při alergii na PNC, **profylaxe v chirurgii** | cefazolin (i.v.), cefadroxil (p.o.) |
| **2.** | méně G+, víc **G−** (*Klebsiella*, *Proteus*, hemofily); infekce dýchacích a močových cest | cefuroxim |
| **3.** | silně **G−** a kmeny s betalaktamázou; ⚠️ **pronikají do CNS → meningitidy a sepse** (ale **ne na listerie**) | cefotaxim, **ceftriaxon**, **ceftazidim** (*Pseudomonas*) |
| **4.** | G+ i rezistentní G−; ⚠️ **volba u febrilní neutropenie** | cefepim |
| **5.** | pokrývá i **MRSA** | ceftarolin |

- **Karbapenemy** (**imipenem, meropenem, ertapenem**) — nejširší spektrum ze všech ATB, **stabilní vůči většině betalaktamáz**; jen **parenterálně**. **Indikace: těžké nemocniční a smíšené infekce, multirezistentní G− kmeny, febrilní neutropenie.** ⚠️ **Imipenem se v ledvinných tubulech rozkládá dehydropeptidázou → kombinuje se s cilastatinem**, který ji blokuje. **NÚ: dráždění CNS až křeče** (nejvíc imipenem), nauzea; **ertapenem nepokrývá pseudomonádu ani enterokoky**.
- **Monobaktamy — aztreonam:** jen **G− včetně pseudomonády**, i.v.; ⚠️ **nemá zkříženou alergii s peniciliny** → volba u těžce alergických; **lék volby u plicní infekce *P. aeruginosa* při cystické fibróze**.

❓ *Proč nelze cefalosporin 1. generace u meningitidy?* → Neprochází přes hematoencefalickou bariéru do likvoru.

---

## 85 · Aminoglykosidy, chinolony

**O čem to je:** dvě skupiny silných baktericidních ATB s výraznou toxicitou — aminoglykosidy ničí **sluch a ledviny**, chinolony jsou **zakázané u dětí a těhotných**.

- **Aminoglykosidy — gentamicin, tobramycin, amikacin** (lokálně neomycin)
  - **Mechanismus:** **ireverzibilní vazba na 30S ribozomální podjednotku** → chybné čtení mRNA a zástava proteosyntézy → **baktericidní**, ⚠️ **účinek závislý na koncentraci** → dávkují se **1× denně ve vysoké dávce** (lepší efekt a menší toxicita).
  - **Spektrum:** **G− tyčinky** (enterobakterie, pseudomonáda, *Acinetobacter*), stafylokoky; **amikacin i mykobakteria**. ⚠️ **Nefungují v anaerobním a kyselém prostředí (absces)** — vstup do bakterie je závislý na kyslíku; v kombinaci s betalaktamem působí **synergicky** (endokarditida).
  - **Kinetika:** ⚠️ **nevstřebávají se z GIT** → jen parenterálně; vylučují se **ledvinami** nezměněné; **úzké terapeutické okno → nutná monitorace hladin (TDM)**.
  - ⚠️ **NÚ — nejvděčnější část:** **ototoxicita** — poškození **VIII. hlavového nervu** (tinnitus, nedoslýchavost, závratě, poruchy rovnováhy), často **nevratná** · **nefrotoxicita** (poškození tubulů, obvykle vratná) · **nervosvalová blokáda až zástava dechu** (presynapticky snižují výdej ACh — ⚠️ pozor u myasthenia gravis a po myorelaxanciích). **KI:** renální insuficience, gravidita, myasthenia gravis; ⚠️ nekombinovat s **furosemidem** (ototoxicita) ani s vankomycinem (nefrotoxicita).
- **Chinolony a fluorochinolony**
  - **Mechanismus:** ⚠️ **blokáda bakteriálních topoizomeráz — DNA gyrázy (topoizomeráza II) u G−, topoizomerázy IV u G+** → nemůže probíhat replikace DNA; baktericidní, závislé na koncentraci. *(⚠️ Některé studentské materiály chybně píší „DNA polymeráza" — to je věcná chyba.)*
  - **Generace: 1.** kyselina nalidixová — jen močové infekce · **2. fluorochinolony** — **ciprofloxacin** (G−, **pseudomonáda**, močové a střevní infekce), ofloxacin, norfloxacin · **3.–4. „respirační"** — **levofloxacin, moxifloxacin** (pneumokoky, atypické patogeny, komunitní pneumonie).
  - **Kinetika:** výborná perorální dostupnost a průnik do tkání i do buněk. ⚠️ **Vápník, hořčík, železo a antacida jejich vstřebání blokují** (chelace) — podávat s odstupem.
  - ⚠️ **NÚ a KI:** **postižení chrupavek a šlach — tendinitida a ruptura Achillovy šlachy** (proto **KI u dětí do ukončení růstu a v graviditě**), fototoxicita, **prodloužení QT**, periferní neuropatie, zmatenost a křeče (snižují práh), **průjem po *C. difficile***, dysglykemie.

🔑 **Aminoglykosidy = 30S ribozom, ototoxicita (VIII. nerv) a nefrotoxicita, 1× denně. Chinolony = topoizomerázy, šlachy a chrupavky → ne dětem a těhotným.**

❓ *Proč aminoglykosid nezabere v abscesu?* → V kyselém anaerobním prostředí se nedostane do bakterie (jeho vstup je závislý na kyslíku).

---

## 86 · Linkosamidy, glykopeptidy, polymyxiny

**O čem to je:** tři „rezervní" skupiny. ⚠️ **Klindamycin je tvoje antibiotikum na zubní infekce** (proniká do kosti a pokrývá anaeroby).

- **Linkosamidy — klindamycin, linkomycin**
  - **Mechanismus:** vazba na **50S podjednotku ribozomu** → blokáda proteosyntézy; bakteriostatické až baktericidní.
  - **Spektrum:** **G+ koky (streptokoky, stafylokoky včetně části MRSA) a ANAEROBY**. ⚠️ **Výborně proniká do kosti a do abscesů.**
  - **Indikace:** ⚠️ **odontogenní infekce a osteomyelitida čelisti — hlavně při alergii na penicilin**, anaerobní infekce, abscesy, aspirační pneumonie, gynekologické záněty, toxoplazmóza.
  - ⚠️ **NÚ: nejvyšší riziko pseudomembranózní kolitidy (*Clostridioides difficile*)** ze všech ATB — průjem, horečka; léčba **vankomycinem p.o. nebo metronidazolem**.
- **Glykopeptidy — vankomycin, teikoplanin**
  - **Mechanismus:** vazba na **D-alanyl-D-alanin** prekurzoru peptidoglykanu → **zablokuje stavbu buněčné stěny** (jiné místo než betalaktamy); baktericidní, jen na **G+**.
  - **Indikace:** ⚠️ **MRSA**, *Enterococcus*, těžké infekce G+ při alergii na betalaktamy, **perorálně u pseudomembranózní kolitidy** (nevstřebává se → působí lokálně ve střevě).
  - **NÚ:** **nefrotoxicita a ototoxicita** (nutné TDM), flebitida; ⚠️ **red man syndrom** — zarudnutí horní poloviny těla při **příliš rychlé infuzi**, způsobené přímým uvolněním histaminu; **není to alergie**, stačí infuzi zpomalit.
  - **Rezistence: VRE** (vankomycin-rezistentní enterokoky) a **VRSA**.
- **Polymyxiny — kolistin:** **naruší cytoplazmatickou membránu** G− bakterií (působí jako detergent). ⚠️ **Rezervní ATB na multirezistentní nemocniční G− kmeny** (*Pseudomonas*, *Acinetobacter*, *Klebsiella*). **NÚ: nefrotoxicita a neurotoxicita.** **Bacitracin** — jen lokálně na G+ (Framykoin = bacitracin + neomycin).

❓ *Které ATB volíš u odontogenní infekce při alergii na penicilin?* → **Klindamycin** — pokrývá orální streptokoky a anaeroby a proniká do kosti; pozor na riziko klostridiové kolitidy.

---

## 87 · Tetracykliny, amfenikoly

**O čem to je:** ⚠️ **tetracykliny se vážou na vápník → poškozují vyvíjející se zuby a kosti** (přímo tvoje téma). Chloramfenikol je dnes rezerva kvůli aplastické anemii.

- **Tetracykliny — doxycyklin, tetracyklin, minocyklin, tigecyklin**
  - ⚠️ **Mechanismus: vazba na 30S podjednotku ribozomu → blokáda proteosyntézy, bakteriostatický efekt.** *(Tvůj zdroj u nich chybně uvádí inhibici buněčné stěny — to je věcná chyba, nezopakuj ji.)*
  - **Spektrum:** široké — G+ i G−, a hlavně **nitrobuněční a atypičtí patogeni: chlamydie, mykoplazmata, rickettsie, borrelie, *Yersinia*, aktinomycety**, akné.
  - **Indikace:** atypická pneumonie, **lymeská borelióza**, chlamydiové infekce, akné, rickettsiózy, malárie (profylaxe).
  - **Kinetika:** ⚠️ **chelatují dvojmocné ionty — mléko, antacida, železo a vápník výrazně snižují vstřebání** (podávat nalačno, s odstupem).
  - ⚠️ **NÚ a KI: ukládají se do mineralizujících se tkání → nevratné hnědožluté zbarvení zubů, hypoplazie skloviny, zpomalení růstu kostí → KONTRAINDIKOVÁNY do 12 let věku, v graviditě a při kojení**; dále **fototoxicita**, dráždění jícnu a GIT, hepatotoxicita ve vysokých dávkách.
- **Amfenikoly — chloramfenikol:** vazba na **50S ribozom**, bakteriostatický, velmi široké spektrum a výborný průnik i do CNS. ⚠️ **Dnes rezerva kvůli NÚ: nevratná aplastická anemie** (idiosynkratická, nezávislá na dávce), dřeňový útlum závislý na dávce a ⚠️ **gray baby syndrom** u novorozenců (nezralá glukuronidace, viz O33). Používá se hlavně **lokálně** (oční kapky), systémově u tyfu a mozkových abscesů, kde nic jiného nezbývá.

🔑 **Tetracykliny = 30S, vápník, zuby a kosti → nikdy dětem a těhotným. Chloramfenikol = 50S, aplastická anemie a gray baby syndrom.**

❓ *Proč se tetracyklin nesmí zapíjet mlékem?* → Vytvoří s vápníkem nevstřebatelný chelát → antibiotikum se nevstřebá (farmaceutická interakce, viz O25).

---

## 88 · Makrolidy `[doplněno — chybí v materiálu katedry]`

⚠️ **Tuhle otázku tvůj zdroj nemá** — text je ze standardní učebnice; kdybys měla materiál katedry, řiď se jím.

**O čem to je:** ATB na **atypické, nitrobuněčné patogeny** a **nejčastější náhrada penicilinu při alergii**.

- **Mechanismus:** vazba na **50S podjednotku (23S rRNA)** → blokáda translokace peptidového řetězce → **bakteriostatický** efekt (ve vysoké koncentraci baktericidní). Vazebné místo sdílejí s linkosamidy → **zkřížená rezistence (MLS-B fenotyp)**.
- **Zástupci:** **erythromycin, klarithromycin, roxithromycin** (14-členné) · **azithromycin** (azalid, 15-členný) · **spiramycin** (16-členný).
- **Spektrum:** G+ koky, moraxella, neisserie, **černý kašel, kampylobakter, *H. pylori***, a hlavně ⚠️ **atypické patogeny — mykoplazma, chlamydie, legionella**. **Nepůsobí na enterobakterie ani pseudomonádu.**
- **Kinetika:** výborný průnik **do buněk a tkání** (proto účinek na nitrobuněčné patogeny), do likvoru špatně; vylučují se **žlučí, ne ledvinami** (není nutná úprava při renální insuficienci). **Azithromycin** má velmi dlouhý poločas → **1× denně, kúra 3–5 dní**.
- **Indikace:** **komunitní a atypická pneumonie**, ⚠️ **respirační a streptokokové infekce při alergii na penicilin**, černý kašel, chlamydiové urogenitální infekce, **eradikace *H. pylori*** (klarithromycin), legionelóza, **spiramycin u toxoplazmózy v graviditě**.
- **NÚ:** GIT potíže (nejvíc erythromycin — je agonista motilinu, proto se off-label používá jako prokinetikum), ⚠️ **prodloužení QT → torsade de pointes**, hepatotoxicita, kovová chuť (klarithromycin).
- ⚠️ **Interakce — nejvděčnější část otázky: erythromycin a klarithromycin silně inhibují CYP3A4** → zvyšují hladinu **statinů (rabdomyolýza), warfarinu (krvácení), karbamazepinu, cyklosporinu, teofylinu, midazolamu**; makrolidy navíc zvyšují hladinu **digoxinu** (potlačí střevní bakterii, která ho inaktivuje). ⚠️ **Azithromycin CYP3A4 prakticky neinhibuje** → u pacienta na statinu nebo warfarinu volíš jeho.

❓ *Který makrolid zvolíš u pacienta na statinu a proč?* → **Azithromycin** — na rozdíl od klarithromycinu neblokuje CYP3A4, takže nehrozí rabdomyolýza.

---

# ČÁST 3 — SPECIÁLNÍ FARMAKOLOGIE II (89–136)

## 89 · Chemoterapeutika močových a střevních infekcí

**O čem to je:** léky, které působí **jen tam, kde mají** — buď se koncentrují v moči, nebo se ze střeva vůbec nevstřebají.

- **Nitrofurantoin** — ⚠️ **lék první volby u nekomplikované infekce močových cest**: poškozuje bakteriální DNA a enzymy. **Nerozšiřuje se systémově — terapeutické hladiny má jen v moči**, proto se hodí i k profylaxi a proto u *E. coli* skoro nevzniká rezistence. **NÚ:** GIT nesnášenlivost, dlouhodobě plicní fibróza a neuropatie. **KI: renální insuficience, gravidita v termínu, děti do 3 měsíců.**
- **Fosfomycin** — blokuje **první krok syntézy buněčné stěny**, baktericidní, širokospektrý (enterobakterie, stafylokoky, enterokoky); **jednorázová dávka u nekomplikované cystitidy**, dnes i u multirezistentních kmenů.
- **Ko-trimoxazol** (sulfamethoxazol + trimetoprim) — blokáda **folátové dráhy ve dvou krocích**; močové infekce, ⚠️ **pneumocystová pneumonie**. NÚ: alergie a **kožní reakce až Stevensův-Johnsonův syndrom**, útlum krvetvorby, hyperkalemie.
- **Pivmecilinam** — perorální betalaktam určený pro močové infekce.
- **Střevní:** **rifaximin** — ⚠️ **nevstřebává se z GIT, působí jen ve střevě**: bakteriální průjmy, cestovatelský průjem, **jaterní encefalopatie** (potlačí bakterie tvořící amoniak) · **nifuroxazid, cloroxin** — nespecifické průjmy · ⚠️ **fidaxomicin a vankomycin p.o. — infekce *Clostridioides difficile***.

🔑 **Nitrofurantoin působí jen v moči, rifaximin jen ve střevě — obojí proto, že se „nedostanou nikam jinam".**

❓ *Proč se rifaximin používá u jaterní encefalopatie?* → Nevstřebá se, ale ve střevě potlačí bakterie produkující **amoniak**, který mozek u jaterního selhání otravuje.

---

## 90 · Antiparazitika

**O čem to je:** léčba parazitů je těžší než léčba bakterií, protože ⚠️ **paraziti jsou eukaryota jako my** — co škodí jim, snadno škodí i našim buňkám.

- **Zásady:** léčí se **cíleně až po parazitologickém průkazu**; látky jsou často toxické; léčbu komplikuje **chronický průběh a různá vývojová stadia parazita**. V ČR je parazitóz málo → řada léků není registrována a musí se dovážet (viz pravidla pro neregistrované přípravky, O2).
- **Antihelmintika (červi):** **mebendazol, albendazol** (benzimidazoly — blokují tvorbu mikrotubulů a příjem glukózy; ⚠️ **v ČR registrovaný mebendazol na střevní hlísty — roupy, škrkavky**) · **pyrantel** (depolarizující blokáda ploténky červa → spastická obrna a vypuzení; roupi, škrkavky) · **praziquantel** (motolice a tasemnice) · **ivermektin** (filárie, svrab).
- **Antiprotozoika (prvoci):** **chlorochin, chinin, artemisinin** (malárie) · **pyrimethamin + sulfadiazin** (toxoplazmóza — blokáda folátové dráhy) · ⚠️ **metronidazol** (amébiáza, giardiáza, trichomoniáza — v anaerobním prostředí se aktivuje a poškodí DNA parazita; ⚠️ **s alkoholem disulfiramová reakce**) · **spiramycin** (toxoplazmóza v graviditě) · antimon a melarsoprol (leishmanióza, trypanosomiáza — těžké kovy, vysoce toxické).
- **NÚ obecně:** GIT potíže, hepatotoxicita, útlum krvetvorby, neurotoxicita; většina je **kontraindikována v graviditě** (hlavně v I. trimestru).

❓ *Proč je antiparazitární léčba toxičtější než antibakteriální?* → Parazit je **eukaryotická buňka podobná lidské** — je málo cílů, které má jen on a my ne.

---

## 91 · Antituberkulotika a antileprotika

**O čem to je:** TBC se léčí **vždy kombinací několika léků a dlouho** — jinak si mykobakterie okamžitě vypěstují rezistenci.

- ⚠️ **Zásady:** léčba je **dlouhodobá (6+ měsíců) a vždy kombinovaná** — úvodní fáze 4–5 léků, pokračovací 2–3. Důvod: zasáhnout **všechny růstové fáze** mykobakterií (rychle se množící, pomalu se množící, dormantní) a **předejít rezistenci**. Léčbu vede pneumolog, je **kontrolovaná a ze zákona povinná**.

| Léčivo | Podstatné a NÚ |
|---|---|
| **Izoniazid** | **proléčivo, které aktivuje sama mykobakterie** (kataláza); blokuje syntézu kyseliny mykolové ve stěně. ⚠️ **NÚ: hepatotoxicita a periferní neuropatie** — proto se přidává **pyridoxin (vit. B6)**; rychlost odbourání závisí na **acetylátorském fenotypu** (viz O26) |
| **Rifampicin** | blokuje bakteriální RNA-polymerázu; baktericidní, proniká i do kaveren a abscesů. ⚠️ **Silný induktor CYP450** → snižuje účinek **kontraceptiv, warfarinu, antiretrovirotik**; ⚠️ barví moč, slzy a pot **do oranžova** |
| **Pyrazinamid** | proléčivo, účinné v kyselém prostředí makrofágů. NÚ: **hepatotoxicita, hyperurikemie (dna)** |
| **Etambutol** | blokuje syntézu stěny, bakteriostatický. ⚠️ **NÚ: retrobulbární neuritida — porucha barvocitu a ostrosti vidění** (nutné oční kontroly) |
| **Streptomycin** | aminoglykosid i.m.; **oto- a nefrotoxický** |

🔑 **Rezistence ve čtyřech stupních:** monorezistentní (1 lék) · polyrezistentní (víc léků, **ale ne izoniazid + rifampicin zároveň**) · **MDR = rezistence na izoniazid I rifampicin současně** · **XDR = navíc na léky druhé řady** (fluorochinolony, injekční). **Hranicí mezi poly- a multirezistencí je právě dvojice izoniazid + rifampicin.**

- **Antileprotika:** *Mycobacterium leprae* — základ je **dapson (blokuje folátovou dráhu) + rifampicin**, u multibacilární formy navíc **klofazimin**. Dapson je **hematotoxický** (hemolýza, hlavně při deficitu G6PD).

❓ *Proč se k izoniazidu přidává vitamin B6?* → Izoniazid zvyšuje ztráty pyridoxinu → hrozí **periferní neuropatie**, pyridoxin jí předchází.

---

## 92 · Antimykotika

**O čem to je:** cílem je **ergosterol** — látka v membráně hub, kterou lidská buňka nemá (má cholesterol).

- **Proč mykóz přibývá:** širokospektrá antibiotika zlikvidují bakteriální konkurenci hub, a imunosupresiva, kortikoidy a cytostatika oslabí obranu.
- **Čtyři mechanismy:** ① **blokáda syntézy ergosterolu** (azoly, terbinafin) ② **přímá vazba na ergosterol → děravá membrána** (polyeny) ③ **blokáda syntézy β-glukanu buněčné stěny** (echinokandiny) ④ blokáda syntézy nukleových kyselin (flucytosin).

| Skupina | Zástupci, indikace, NÚ |
|---|---|
| **Polyeny** | **amfotericin B** — nejširší spektrum (kvasinky i plísně), i.v.; **mukormykóza, kryptokoková meningitida, těžké aspergilózy**. ⚠️ **NÚ: nefrotoxicita, horečka a třesavka při infuzi, hypokalemie** (lipozomální forma je šetrnější). **Nystatin** — jen lokálně, ⚠️ **pouze na kandidy** (orální soor) |
| **Azoly** | **flukonazol** (kandidózy, kryptokoková meningitida — proniká do CNS; ⚠️ **teratogenní**), **itrakonazol** (dermatofyta, profylaxe), ⚠️ **vorikonazol — lék volby u invazivní aspergilózy** (NÚ: poruchy vidění). ⚠️ **Všechny azoly silně inhibují CYP3A4** → hodně interakcí (statiny, warfarin, imunosupresiva); hepatotoxicita, prodloužení QT |
| **Echinokandiny** | **kaspofungin, anidulafungin, mikafungin** — i.v., ⚠️ **lék volby u invazivní kandidózy**; velmi dobře snášené. ⚠️ **Nepronikají do CNS** ani nepůsobí na kryptokoky |
| **Lokální** | klotrimazol, ekonazol, mikonazol (kůže, sliznice, vaginálně), **terbinafin** (dermatofyta, onychomykóza), amorolfin a cyklopirox v laku na nehty |

❓ *Proč amfotericin B poškozuje ledviny?* → Váže se i na **cholesterol** v lidských membránách (podobný ergosterolu) — hlavně v tubulech ledviny.

---

## 93 · Antivirotika

**O čem to je:** léčí se jen zlomek virových infekcí — většina se u zdravého člověka vyléčí sama.

- ⚠️ **Vždy léčíme: HIV, hepatitidu B a C.** **Podle klinického a imunitního stavu:** CMV, HSV-1 a 2, VZV, EBV, chřipka A, RSV, covid-19. Řada infekcí je u imunokompetentních **samoúzdravná**.
- **Antiherpetika:** **aciklovir** — proléčivo, které aktivuje až **virová thymidinkináza** (proto je selektivní pro infikované buňky), pak blokuje virovou DNA-polymerázu. ⚠️ **Perorální dostupnost jen 10–30 % → podává se jako valaciklovir (dostupnost ~70 %)** — učebnicový příklad proléčiva. **Indikace:** HSV-1 a 2, **VZV (pásový opar — čím dřív, tím lépe)**; ⚠️ **na CMV nefunguje — tam ganciklovir nebo foskarnet** (NÚ: útlum dřeně, nefrotoxicita). NÚ acikloviru: nefrotoxicita při rychlém i.v. podání (dostatečná hydratace!).
- **Chřipka — inhibitory neuraminidázy:** **oseltamivir** (p.o.) a **zanamivir** (inhalačně, ⚠️ **KI astma a CHOPN**). Neuraminidáza uvolňuje nové viriony z buňky — blokáda zkrátí příznaky, ⚠️ **jen když se podá do 48 h od začátku**.
- **Hepatitida C** (RNA virus) — bez léčby fibróza, cirhóza, hepatocelulární karcinom. ⚠️ **Přímo působící antivirotika (sofosbuvir + velpatasvir) vyléčí přes 97 % pacientů.**
- **Hepatitida B** (DNA virus, integruje se do genomu, ~10 % chronicita) — cílem je **trvale potlačit replikaci**, ne eradikace: **tenofovir**, entekavir, lamivudin, pegylovaný interferon α.
- **Ribavirin** — analog guanosinu; RSV, hemoragické horečky, dřív hepatitida C. ⚠️ **Teratogenní a mutagenní**, NÚ **hemolytická anemie**.
- **Očkování je nejúčinnější prevence:** povinné spalničky, příušnice, zarděnky, obrna, **hepatitida B**; doporučené klíšťová encefalitida, chřipka, **HPV**, hepatitida A, plané neštovice, covid-19.

❓ *Proč aciklovir nepoškozuje zdravé buňky?* → Aktivovat ho umí jen **virová thymidinkináza** — v neinfikované buňce zůstane neúčinný.

---

## 94 · Antiretrovirotika

**O čem to je:** léky proti HIV virus **nevyléčí** — jen zastaví jeho množení, proto se berou doživotně.

- **HIV** je **retrovirus**, který infikuje **CD4+ T-lymfocyty** a postupně je ničí → imunodeficit → oportunní infekce a nádory (AIDS).
- ⚠️ **Cíl léčby: potlačit replikaci viru na nedetekovatelnou hladinu — nikoli eradikace.** Virus přetrvává v latentních rezervoárech.
- **Mechanismy a skupiny:** **nukleosidové inhibitory reverzní transkriptázy (NRTI)** — tenofovir, emtricitabin, abakavir · **nenukleosidové (NNRTI)** — efavirenz · **inhibitory proteázy (-navir)** — brání sestavení funkčních virionů, ⚠️ **silné interakce přes CYP3A4** · **inhibitory integrázy (-tegravir)** — dolutegravir, dnes základ léčby · **inhibitory vstupu** — maravirok.
- ⚠️ **Léčí se vždy kombinací nejméně tří léků** (kombinovaná antiretrovirová terapie) — jinak virus rychle mutuje a stane se rezistentním.
- **NÚ:** lipodystrofie a metabolický syndrom (inhibitory proteázy), nefrotoxicita a úbytek kostní hmoty (tenofovir), hypersenzitivita na abakavir (HLA-B*5701), neuropsychické NÚ (efavirenz).
- **Zahájení léčby:** ⚠️ **zdroj uvádí pokles CD4 pod 350/mm³**; `[doplněno]` dnešní doporučení jsou **léčit každého HIV pozitivního bez ohledu na CD4** — u zkoušky uveď hodnotu ze skript a doplň, že současný trend je „treat all".

❓ *Proč se HIV léčí vždy kombinací tří léků?* → Při monoterapii virus **rychle zmutuje** a lék přestane fungovat; trojkombinace to znemožní.

---
## 95 · Antitusika, mukolytika, expektorancia

**O čem to je:** léčba kašle se řídí jeho typem — **suchý tlumíme, vlhký podporujeme**. Kombinovat obojí je chyba.

- **Kašel** vzniká drážděním tusigenních zón (dolní dýchací cesty, pohrudnice, bránice, osrdečník, jícen, zevní zvukovod). Dělení: **akutní < 3 týdny · subakutní 3–8 týdnů · chronický > 8 týdnů**; **neproduktivní (suchý) → antitusika** · **produktivní (vlhký) → mukolytika a expektorancia**.
- **Antitusika centrální:** **kodein** — tlumí centrum kašle v prodloužené míše přes **opioidní μ-receptory**; má i analgetický efekt, ⚠️ ve vysokých dávkách zácpa a útlum dechu, metabolizuje se na morfin přes **CYP2D6** (viz O26). **Dextrometorfan** — bez analgezie a bez závislosti, ⚠️ ve vysokých dávkách zneužíván (halucinace). **Butamirát** — nekodeinové, netlumí dechové centrum, **vhodné i pro malé děti**.
- **Antitusika periferní:** **dropropizin, levodropropizin** — tlumí dráždivost sliznice a C-vlákna; před bronchoskopií.
- **Mukolytika:** **N-acetylcystein** — rozštěpí disulfidické můstky v hlenu → hlen zřídne; ⚠️ **je zároveň prekurzorem glutathionu, tedy antidotum otravy paracetamolem** (viz otázka 63). **Bromhexin, ambroxol** — snižují viskozitu, podporují pohyb řasinek.
- **Expektorancia:** **guaifenesin** — zvyšuje sekreci bronchiálních žláz, hlen je řidší a lépe se vykašlává; má i mírný myorelaxační a anxiolytický efekt.
- ⚠️ **Kodein se nikdy nekombinuje s mukolytikem** — zvýšíš množství hlenu a zároveň zablokuješ jeho vykašlávání (riziko zahlenění a infekce).

❓ *Jaký lék je zároveň mukolytikum i antidotum paracetamolu?* → **N-acetylcystein.**

---

## 96 · Antiastmatika

**O čem to je:** ⚠️ **dvě naprosto odlišné role — úlevová léčba (rozšíří průdušky hned) a kontrolující léčba (tlumí zánět dlouhodobě).** Na tomhle rozdílu postav celou odpověď.

- **Astma** = chronický **neinfekční zánět** dýchacích cest s **reverzibilní** obstrukcí (bronchospasmus + hlen), často alergický. **CHOPN** = obstrukce **není plně reverzibilní**, postupuje, nejčastěji z kouření. ⚠️ **U astmatu je zánět přítomný i mezi záchvaty — proto se léčí i bez příznaků.**
- **Stupně astmatu:** intermitentní (≤ 1× týdně, spirometrie mezi záchvaty normální) · perzistující lehké (> 1× týdně, FEV1 > 80 %) · středně těžké (denně, 60–80 %) · těžké (trvalé příznaky, < 60 %).

**Úlevová (bronchodilatační) léčba:**
- **β2-agonisté** — přes ↑ cAMP uvolní hladký sval bronchů: **SABA (salbutamol, fenoterol, terbutalin)** na záchvat · **LABA (formoterol, salmeterol)** a **U-LABA (indakaterol, vilanterol)** dlouhodobě. ⚠️ **LABA nikdy samostatně, jen s inhalačním kortikoidem.** NÚ: **třes, tachykardie, hypokalemie**.
- **Anticholinergika** — blokáda M3: **SAMA ipratropium** · **LAMA tiotropium, glykopyronium** (hlavně **CHOPN**). NÚ: sucho v ústech, poruchy chuti, retence moči, ⚠️ zhoršení glaukomu.
- **Xantiny — teofylin, aminofylin:** neselektivní blokáda **fosfodiesteráz** (↑ cAMP) + antagonismus **adenosinových** receptorů. ⚠️ **Úzké terapeutické okno** — NÚ nauzea, tachyarytmie, křeče, reflux; dnes jen doplňková léčba.

**Kontrolující (protizánětlivá) léčba:**
- ⚠️ **Inhalační kortikosteroidy (budesonid, flutikazon, beklometazon) — základ léčby každého perzistujícího astmatu**: tlumí zánět a hyperreaktivitu, ale **akutní záchvat samy nezastaví** (nastupují hodiny). NÚ: ⚠️ **orofaryngeální kandidóza a chrapot → po inhalaci vyplachovat ústa** (tvoje zubařská rada), při vysokých dávkách systémové účinky. Systémové kortikoidy (prednison) u těžkých exacerbací a status asthmaticus.
- **Antileukotrieny — montelukast:** blokáda receptorů pro cysteinylové leukotrieny (viz otázka 62); perorálně, vhodný u alergického astmatu, u dětí a při aspirinovém astmatu.
- **Biologická léčba:** ⚠️ **omalizumab (anti-IgE)** u těžkého alergického astmatu, anti-IL5 (mepolizumab) u eozinofilního.
- **Roflumilast** (inhibitor PDE4) — udržovací léčba těžké CHOPN.
- **Stupňovitá strategie:** IKS-formoterol podle potřeby → denní nízká dávka IKS → IKS + LABA → přidat tiotropium či antileukotrien → vysoké dávky + biologikum, případně nízká dávka perorálního kortikoidu.

🔑 **Úlevová léčba otevře průdušky HNED, kontrolující tlumí zánět DLOUHODOBĚ. Pacient musí mít vždy u sebe úlevový inhalátor — kortikoid ho v záchvatu nezachrání.**

❓ *Co poradíš pacientovi na inhalačním kortikoidu?* → **Vypláchnout ústa po každé inhalaci** — prevence orofaryngeální kandidózy a chrapotu.

---

## 97 · Antihistaminika

**O čem to je:** blokují receptor pro **histamin**, který se uvolňuje při alergické reakci. Starší generace prochází do mozku a uspává.

- **Histamin** vzniká dekarboxylací **histidinu**, je uložen v granulích **mastocytů a bazofilů** (spolu s heparinem); uvolní se, když se na buňku naváže **IgE** (viz O30). **Receptory: H1** (Gq → IP₃/DAG → ↑ Ca²⁺; endotel, hladké svaly, nervová zakončení — vazodilatace, otok, svědění, bronchokonstrikce) · **H2** (Gs → ↑ cAMP; **sekrece žaludeční kyseliny**).
- ⚠️ **Věta, která odliší dobrou odpověď: antihistaminika H1 nejsou prostí antagonisté — jsou to inverzní agonisté** (stabilizují neaktivní formu receptoru a snižují jeho bazální aktivitu).
- **Indikace:** alergická rýma a konjunktivitida, **kopřivka a angioedém**, atopický ekzém, ⚠️ **doplňková léčba anafylaxe (lékem volby zůstává adrenalin)**, premedikace před rizikovými výkony, kinetózy a zvracení (I. generace).

| | **I. generace** | **II. generace** |
|---|---|---|
| Prostup do CNS | **ano → sedace** | minimální → **nesedativní** |
| Selektivita | **neselektivní** — blokují i muskarinové, serotoninové a α receptory | selektivní pro H1 |
| Zástupci | **prometazin, bisulepin, hydroxyzin, moxastin-teoklát** (Kinedryl) | **cetirizin, levocetirizin, loratadin, desloratadin, fexofenadin** |

- ⚠️ **NÚ I. generace:** sedace a zhoršená pozornost (⚠️ **řízení, kombinace s alkoholem**), **anticholinergní účinky** — sucho v ústech, **zahuštění hlenu**, retence moči, zácpa, poruchy akomodace; u dětí paradoxní neklid. **KI:** glaukom s úzkým úhlem, hyperplazie prostaty. II. generace: vzácně prodloužení QT.

❓ *Proč se antihistaminikum nesmí použít jako jediná léčba anafylaxe?* → Nastupuje pomalu a neřeší **hypotenzi ani bronchospasmus** — lékem volby je **adrenalin**.

---

## 98 · Laxativa, antidiaroika

**O čem to je:** dva opačné extrémy — u obou platí, že **lék není první volba** (u zácpy životospráva, u průjmu tekutiny).

- **Zácpa:** základ je **pohyb, tekutiny, vláknina**; laxativa jsou často volně prodejná a ⚠️ **nadužívaná** (mohou zhoršit motilitu a snížit vstřebávání jiných léků a vitaminů).

| Typ laxativa | Mechanismus a zástupci |
|---|---|
| **objemová** | **psyllium** — nasákne vodu, zvětší objem stolice → defekační reflex; ⚠️ **nutné zapíjet** |
| **osmotická** | **laktulóza** (nevstřebatelný disacharid, váže vodu a okyseluje střevo), **makrogol**; **glycerolové čípky** — účinek do 30 min |
| **salinická** | síran hořečnatý a sodný — zadrží vodu, dráždí sliznici; ⚠️ riziko iontového rozvratu |
| **změkčující** | tekutý parafín — dnes se nepoužívá (aspirace, blokuje vstřebání vitaminů A, D, E, K) |
| **stimulační** | bisakodyl, senna — dráždí plexy střevní stěny; ⚠️ **jen krátkodobě** |

- ⚠️ **Laktulóza má dvojí využití:** projímadlo **a léčba jaterní encefalopatie** — okyselí obsah střeva, amoniak se změní na nevstřebatelný NH₄⁺ a odejde stolicí.
- **Průjem** = řídká stolice víc než 3× denně. **Základ léčby je rehydratace** (perorální rehydratační roztok), dieta. Léky často průjem sami způsobují (ATB, NSA, cytostatika, laxativa, sorbitol).
- **Antidiaroika:** **adsorbencia** — aktivní uhlí (⚠️ upozornit na černou stolici), **diosmektit** — vážou toxiny a vodu · **střevní antiseptika** — nifuroxazid, **rifaximin** · **obstipancia** — **loperamid** (periferní μ-agonista → ↑ tonus svěračů, zpomalí pasáž; do CNS neproniká), difenoxylát.
- ⚠️ **Obstipancia se nesmí podat u infekčního průjmu (horečka, krev ve stolici) ani při podezření na něj** — zadržíš patogen a toxiny ve střevě (riziko toxického megakolon).

❓ *Proč se loperamid nedává u horečnatého průjmu s krví?* → Zpomalí pasáž, patogen a jeho toxiny zůstanou ve střevě déle → zhoršení a riziko toxického megakolon.

---

## 99 · Farmakoterapie vředové choroby gastroduodena a GERD

**O čem to je:** za většinou vředů dnes stojí ***Helicobacter pylori*** nebo **NSA** — proto se léčí kombinací antibiotik a léku tlumícího kyselinu.

- **Vřed** = slizniční defekt přesahující pod *muscularis mucosae*, vzniká tam, kde kyselina a pepsin převáží nad obranou sliznice (hlen, bikarbonát, prostaglandiny, prokrvení).
- **Příčiny:** ⚠️ ***H. pylori*** (G− bičíkatá tyčinka tvořící **ureázu**, díky které přežije v kyselém prostředí; **je klasifikován jako karcinogen** — riziko karcinomu žaludku a MALT lymfomu) a ⚠️ **NSA** (blokádou COX-1 vypnou ochranné prostaglandiny, viz otázka 64); dále stres u kriticky nemocných, kortikoidy, kouření, **Zollingerův-Ellisonův syndrom**. *(⚠️ Tvůj zdroj uvádí u H. pylori „asi 20 %" — to neodpovídá; u duodenálních vředů je H. pylori příčinou většiny případů. U zkoušky raději řekni „hlavní příčina" než konkrétní procento.)*
- 🔑 **Rozlišení, na které se ptají skoro vždy: žaludeční vřed bolí PO jídle · duodenální vřed bolí NALAČNO (v noci) a po jídle se uleví.** Komplikace: krvácení, perforace, penetrace, stenóza z jizvení, malignizace.
- **Inhibitory protonové pumpy (PPI) — omeprazol, pantoprazol, esomeprazol:** ⚠️ **ireverzibilně blokují H⁺/K⁺-ATPázu parietální buňky** — poslední společný krok tvorby kyseliny. Podávají se **nalačno, půl hodiny před jídlem** (aktivují se v kyselém prostředí a musí zastihnout aktivní pumpy). **Indikace:** vředová choroba, **GERD**, prevence vředů z NSA, Zollingerův-Ellisonův syndrom. **NÚ:** ⚠️ **horší vstřebávání vitaminu B12, hořčíku, vápníku a železa** (osteoporóza a zlomeniny), vyšší riziko střevních infekcí (*C. difficile*), nadýmání; ⚠️ **omeprazol blokuje CYP2C19 → snižuje účinek klopidogrelu** (volí se pantoprazol).
- **Další léčiva:** **antagonisté H2 receptorů** (famotidin) — slabší, na noční sekreci · **antacida** (hydroxid hlinitý a hořečnatý) — jen symptomatická úleva, ⚠️ **vážou jiné léky** (tetracykliny, chinolony) · **sukralfát** (ochranný film na vředu) · **misoprostol** (analog PGE1, prevence vředů z NSA, ⚠️ **KI v graviditě** — vyvolává děložní stahy).
- ⚠️ **Eradikace *H. pylori*: PPI + amoxicilin + klarithromycin po dobu 14 dní** (při alergii na penicilin metronidazol); při selhání čtyřkombinace s bismutem.

❓ *Proč se PPI podává nalačno?* → Musí zastihnout **aktivované protonové pumpy** stimulované jídlem; na plný žaludek účinkuje výrazně hůř.

---

## 100 · Prokinetika, antiemetika, emetika

**O čem to je:** prokinetika „rozhýbou" línou trávicí trubici, antiemetika tlumí zvracení — a to pochopíš přes **dvě centra**, která zvracení řídí.

- **Prokinetika** — zvyšují propulzivní peristaltiku a **tonus dolního jícnového svěrače**. ⚠️ **Účinek klesá směrem aborálně — nejsilnější je na jícnovém svěrači.** **Indikace: GERD, gastroparéza (diabetická), nauzea a zvracení, příprava k vyšetření.**
  - **Metoklopramid** — antagonista **D2** (+ 5-HT4); ⚠️ **prochází do CNS → sedace a extrapyramidové NÚ (akutní dystonie, hlavně u mladých)**, hyperprolaktinemie.
  - **Domperidon** — antagonista D2, ⚠️ **do CNS prakticky neproniká → bez extrapyramidových NÚ**, ale ⚠️ **prodlužuje QT**; podporuje i laktaci.
  - **Itoprid** (D2 antagonista + inhibitor AChE), **cisaprid** (5-HT4, stažen kvůli arytmiím).
  - **KI prokinetik:** mechanická obstrukce, perforace nebo krvácení do GIT.
- **Eubiotika:** **probiotika** = živé nepatogenní kmeny (laktobacily, bifidobakterie) — obnoví flóru po ATB, ↑ IgA a tvorbu vitaminů K a B12; **prebiotika** = substrát pro ně (inulin, oligofruktóza).
- 🔑 **Dvě centra zvracení:** ⓵ **centrum pro zvracení** v retikulární formaci prodloužené míchy — přijímá podněty z **vestibulárního ústrojí, n. vagus, GIT a vyšších center** ⓶ **chemorecepční spouštěcí zóna (area postrema)** — leží **mimo hematoencefalickou bariéru**, proto přímo „ochutnává" toxiny v krvi. Přenašeči: **dopamin, serotonin, histamin, acetylcholin** — proto je tolik skupin antiemetik.
- **Antiemetika podle mechanismu:** ⚠️ **setrony (ondansetron, granisetron) — antagonisté 5-HT3, nejúčinnější, hlavně u chemoterapie** (NÚ: bolest hlavy, zácpa, prodloužení QT) · **antagonisté D2** (metoklopramid, domperidon, haloperidol) · **antihistaminika I. generace a anticholinergika** (moxastin, skopolamin) — ⚠️ **volba u kinetóz** · **kortikoidy (dexametazon)** a **antagonisté NK1 (aprepitant)** u chemoterapie · **benzodiazepiny** u anticipačního zvracení. **Betahistin** — analog histaminu u **Ménièrovy choroby** (vertigo, tinnitus, nedoslýchavost).
- ⚠️ **Nejsilnější emetogen je cisplatina** — uvolní serotonin ze sliznice tenkého střeva, ten aktivuje vagus a obě centra.
- **Emetika:** **apomorfin** (agonista D2 v area postrema, s.c.), emetin — dnes se k vyvolání zvracení při otravách **prakticky nepoužívají** (riziko aspirace).

❓ *Proč metoklopramid působí v CNS a domperidon ne?* → Metoklopramid **prochází hematoencefalickou bariérou** (odtud extrapyramidové NÚ), domperidon prakticky ne.

---
