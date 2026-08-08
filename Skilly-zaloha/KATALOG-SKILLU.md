# Katalog skillů — 53 kusů z ostrého provozu

**Pro vašeho Clauda:** tohle je úplný seznam skillů, které v tom ekosystému běží. Projdi ho proti tomu, co uživatel reálně dělá, a **doporuč 5–8 skillů k zavedení v prvním kole** — ne víc. Ke každému napiš, proč zrovna ten. Skilly ve sloupci `BALÍK` jsou přiložené jako soubory; ostatní se musí napsat (šablonu dá `skill-creator`, viz README).

**Pro člověka:** nečti to celé. Skoč na tabulku *Jádro* — to je 80 % hodnoty. Zbytek nech na Claudovi.

## Legenda sloupce „Verdikt"

| Značka | Znamená |
|---|---|
| 🟢 **BALÍK** | Přiložený soubor, zkopíruj a funguje. Obecný, nezávislý na byznysu. |
| 🔵 **OBECNÝ** | Funguje kdekoli, ale soubor v balíku není — vyžádejte si ho, nebo si ho nechte napsat. |
| 🟡 **VZOR** | Nápad je přenositelný, obsah ne. Přeberte strukturu, naplňte svými fakty. |
| 🔴 **NA MÍRU** | Vázané na konkrétní firmu/nástroj/klienta. Nekopírovat — jen jako ukázka, jak takový skill vypadá. |

---

## 1. Jádro — postupy, jak vzít práci (začněte tady)

| Skill | Co dělá | Verdikt |
|---|---|---|
| `orchestrace` | Rozhodovací strom „jakým postupem tuhle práci vzít" — kdy autopilot, kdy loop, kdy roast, kdy prostě odpovědět. Router, ne engine. **Zaveďte první.** | 🟢 BALÍK |
| `autopilot` | Default režim pro netriviální kód, co musí fungovat. Jedna dávka otázek → zamkne spec do souboru → jede Plan/Build/Judge do PASS bez dalšího ptaní. Zastaví jen u nevratné akce. | 🟢 BALÍK |
| `agent_loop_pbj` | Engine pod autopilotem: tři oddělení agenti (Plan / Build / Judge) s čerstvým kontextem v cyklu, dokud to reálně neprojde testem. | 🟢 BALÍK |
| `loop_agent` | Totéž pro **text** — Maker/Checker cyklus, dokud výstup neprojde gatem. Na reporty, strategie, e-mailové sekvence, pitche. ~4× tokeny. | 🟢 BALÍK |
| `session_close` | Uzávěrka session: co jsme rozhodli → `LOG.md`, co se opakovalo → kandidát na skill, co se změnilo → paměť, + handoff pro příští session. **Tohle je motor učení celého systému.** | 🟢 BALÍK |
| `checkpoint` | Uprostřed dlouhé práce zmrazí stav do souboru (přepisuje jeden soubor), aby se nic neztratilo při zaplnění kontextu nebo před rizikovým krokem. | 🟢 BALÍK |
| `roast` | Rada 5 person (Kontrarián, Expanzionista, Logik, Rešeršér, Zákazník) rozstřelí nápad, Soudce vrátí GO / RESHAPE / KILL + nejlevnější 48h test. Pouštět **před** utracením peněz. | 🟢 BALÍK |
| `grill-me` | Vytáhne z hlavy plán/spec/rozhodnutí — otázka po otázce, každá odpověď hned do souboru. | 🟢 BALÍK |
| `automatizace-governance` | EAD filtr (Eliminate → Automate → Delegate) **před** stavbou automatizace, volba běhového prostředí, audit doručení („hlásí job selhání, nebo padá potichu?"), Kill Switch na mrtvé automatizace. | 🟢 BALÍK |

---

## 2. Meta — skilly o samotném systému

Tahle rodina (`aios-*`) je **rozřezaná dokumentace vlastního ekosystému** na 15 kusů, aby se načítalo jen to relevantní. Koncept je zlatý a doporučuju ho převzít; **obsah si ale musíte napsat sami** — jsou to fakta o konkrétním systému, ne obecná pravda.

> Postup: první měsíc nic nepište. Až vám systém 3× klopýtne o totéž, teprve pak založte první z těchhle souborů.

| Skill | Odpovídá na otázku | Verdikt |
|---|---|---|
| `aios-architecture-contract` | Proč je to postavené takhle? Co se nesmí rozbít? | 🟡 VZOR |
| `aios-change-control` | Smím to nasadit/smazat/změnit? Kdo to schvaluje? Jaká úroveň autonomie? | 🟡 VZOR |
| `aios-external-boundary` | Smí tohle ven z vaultu? (e-mail, deploy, sdílení, PII, GDPR) | 🟡 VZOR |
| `aios-automation-registry` | Co všechno běží automaticky, kde, a jak ověřím, že to žije? | 🟡 VZOR |
| `aios-connectors-and-credentials` | Kde je který token, co smí, jak ověřím konektor. *(Cesty, nikdy hodnoty.)* | 🟡 VZOR |
| `aios-debugging-playbook` | Symptom → nejrychlejší cesta k příčině. Tabulka známých poruch. | 🟡 VZOR |
| `aios-failure-archaeology` | Řešili jsme tohle už? Proč se to nesmí? Kdo to zabil a proč? | 🟡 VZOR |
| `aios-diagnostics-and-tooling` | Jak to **změřit** místo hádání — katalog diagnostik + health skript. | 🟡 VZOR |
| `aios-validation-and-qa` | Kdy smím říct „funguje to". Evidence bar, golden testy. | 🟡 VZOR |
| `aios-analysis-toolkit` | Recepty na audit dat/čísel — „prove it, don't just install it". | 🔵 OBECNÝ |
| `aios-research-methodology` | Jak se z tušení stane přijatý fakt. Životní cyklus nápadu až po retirement. | 🔵 OBECNÝ |
| `aios-research-frontier` | Kam systém posunout dál, kde je největší páka. | 🟡 VZOR |
| `aios-run-and-operate` | Denní rituál: jak session začíná, routuje, předává práci. | 🟡 VZOR |
| `aios-docs-and-writing` | Kam který fakt patří + copy-paste šablony (LOG, handoff, SKILL.md). | 🟡 VZOR |
| `aios-build-and-env` | Runbook „postav prostředí na čistém stroji" + co z repa obnovit NELZE. | 🟡 VZOR |
| `aios_audit` *(recept)* | „Je systém postavený správně?" — read-only kontrola formy, ~1× týdně. | 🔵 OBECNÝ |
| `aios_level_up` *(recept)* | „Jaká byznys páka mi uniká?" — hledání dalšího kroku, ~1× týdně. | 🔵 OBECNÝ |
| `vault-lint` | Sémantické zdraví znalostní báze: kontradikce, zastaralá tvrzení, osamocené poznámky, díry v pokrytí. Flag-only, nikdy needituje. | 🔵 OBECNÝ |

---

## 3. Web, design, frontend

| Skill | Co dělá | Verdikt |
|---|---|---|
| `agent-ready-web` | Web čitelný pro AI agenty i lidi — schema.org JSON-LD šablony, `llms.txt`, GEO/AEO. Baseline u každé nové stránky. | 🔵 OBECNÝ |
| `design-taste-frontend` | „Anti-slop" stavba UI — odvodí design směr a postaví rozhraní, co nevypadá šablonovitě. *(Zdroj: Leon / taste-skill, MIT.)* | 🔵 OBECNÝ |
| `taste-score` | Číselná známka 0–1 pro hotový vzhled + jedna nejlevnější změna, co skóre zvedne nejvíc. Adversariální (musíš si body zasloužit). | 🔵 OBECNÝ |
| `motion-gallery` | Postaví živou galerii N × 3 variant animace k proklikání a výběru — protože pohyb se textem neprodá. | 🔵 OBECNÝ |
| `transitions-dev` | 21 hotových CSS mikro-interakcí (dropdown, modal, shake, skeleton…), každá s `prefers-reduced-motion`. *(Zdroj: Jakub Antalík, transitions.dev.)* | 🔵 OBECNÝ |
| `cinematic-web` | Celý pipeline na scrollytelling web s fotkou v pozadí a pinnovanými scénami. | 🔵 OBECNÝ |
| `webapp-testing` | Playwright toolkit — reálně proklikat appku, screenshoty, konzole. Tímhle Judge **dokazuje**, že to funguje. *(Zdroj: anthropics/skills.)* | 🔵 OBECNÝ |
| `web-perf-trace` | Změří runtime výkon (práce hlavního vlákna) přes headless Chrome + CDP, before→after, medián z víc běhů. | 🔵 OBECNÝ |
| `local-build-shot` | Spolehlivý screenshot webu přes headless Chrome — obchází to, že in-app browser vrací černé snímky. | 🔵 OBECNÝ |
| `netlify-deploy` | Bezpečný deploy (draft + restore) na konkrétní Netlify účet, s kontrolou, že se nepublikovaly interní zdroje. | 🔴 NA MÍRU |

---

## 4. Marketing a byznys

Pětice níže pochází z `marketingskills` (Corey Haines, MIT licence) — jsou obecné a stojí za převzetí en bloc. `product-marketing` čtou ostatní jako první.

| Skill | Co dělá | Verdikt |
|---|---|---|
| `product-marketing` | Založí základní marketingový kontext produktu (positioning, ICP, cílovka) — čtou ho všechny ostatní marketing skilly. **Zaveďte první z téhle pětice.** | 🔵 OBECNÝ |
| `copywriting` | Psaní a přepis marketingové copy, řízené vaším `voice-principles.md`. | 🔵 OBECNÝ |
| `cro` | Optimalizace konverzí — proč stránka neprodává. Ne vzhled, ne rychlost: přesvědčivost. | 🔵 OBECNÝ |
| `customer-research` | Sběr a syntéza zákaznického výzkumu — transkripty, VOC, review mining, persony, JTBD. | 🔵 OBECNÝ |
| `pricing` | Cenotvorba a packaging — tiery, value metric, Van Westendorp, willingness-to-pay. | 🔵 OBECNÝ |
| `seo-google` | Tvrdá SEO data zdarma z Google API (Core Web Vitals, Search Console, GA4). Žádné placené nástroje. | 🔵 OBECNÝ |
| `storm-research` | Multi-perspektivní rešerše s ověřenými citacemi: 5 expertních čoček → mapa rozporů → HTML briefing → adversariální peer review. Na témata, kde se střetávají názory. | 🔵 OBECNÝ |
| `monthly_seo_report` *(recept)* | Měsíční jednostránkový report jen s metrikami napojenými na peníze — ne vanity traffic. | 🟡 VZOR |
| `seo_competitor_audit` *(recept)* | Mapa projektu proti konkurenci → prioritizovaný akční plán jako spreadsheet. | 🟡 VZOR |
| `b2b_vyjednavac` *(recept)* | Postup pro zpracování obchodní schránky a psaní vyjednávacích odpovědí. | 🟡 VZOR |

---

## 5. Provozní, vázané na konkrétní firmu

Nekopírovat. Uvádím je proto, že **ukazují cílový stav**: nejvyšší hodnotu nemá obecný skill, ale ten, který zná váš konkrétní proces. Až budete třetí týden dělat totéž ručně, tady je vzor, jak z toho udělat skill.

| Skill | Co dělá | Verdikt |
|---|---|---|
| `follow-up-tracker` | Každé ráno projde štítek v Gmailu, najde vlákna přesně 7 dní bez odpovědi a připraví draft urgence. Nikdy neodesílá (L2). | 🟡 VZOR |
| `fse_lead_responder` *(recept)* | Na příchozí dotaz na ceník vyrobí draft odpovědi s připomínkou přiložit přílohy. | 🔴 NA MÍRU |
| `fse_tracking_drafts` *(recept)* | Po doplnění tracking čísel vyrobí drafty „dorazil vzorek, jak jste spokojeni?". | 🔴 NA MÍRU |
| `fse-print-doc` | Brandovaný PDF deliverable (deck, one-pager) přes Chrome-headless HTML→PDF, s render-verify smyčkou. | 🔴 NA MÍRU |
| `bankability_analyzer` *(recept)* | Z finančních výkazů klienta vygeneruje report bonity. | 🔴 NA MÍRU |
| `blynkr-ads-conversion-campaign` | Rozhodovacími branami řízená kampaň na vyřešení jedné konkrétní otázky v Google Ads. | 🔴 NA MÍRU |

---

## Doporučené pořadí zavádění

1. **Týden 1** — `CLAUDE.md` (šablona z balíku) + `orchestrace` + `session_close`. Nic víc. Tohle samo o sobě změní, jak s Claudem pracujete.
2. **Týden 2** — `autopilot` + `agent_loop_pbj` (pokud píšete kód) **nebo** `loop_agent` (pokud píšete texty). Ne obojí.
3. **Týden 3** — `checkpoint`, `roast`. A napište první vlastní skill z něčeho, co jste už třikrát dělali ručně.
4. **Měsíc 2+** — `automatizace-governance` až budete stavět první cron. Rodina `aios-*` až vás systém začne kousat.

**Nezavádějte víc než 3 skilly najednou.** Neposoudíte, co pomohlo.
