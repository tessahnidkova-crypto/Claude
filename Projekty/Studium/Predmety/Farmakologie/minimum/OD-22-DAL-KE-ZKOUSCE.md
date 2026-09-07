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
