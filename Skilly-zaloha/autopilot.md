---
name: autopilot
description: THE DEFAULT mode for building non-trivial executable code that must actually work (apps/scripts/endpoints) — fire it yourself, no permission needed, whenever Josef asks to build/change runnable code beyond a one-line fix, OR explicitly hands off with "dej mi to na autopilota", "postav to sám, neptej se", "autopilot", "jeden zátah bez ptaní", "nastav to a jeď", "goal-and-go", "/autopilot". Runs ONE non-skippable intake batch (Claude proposes runnable acceptance + decision defaults, Josef confirms/redirects in a single message), locks the spec to a file, then drives the Plan→Build→Judge loop to PASS with no further questions. Stops ONLY for irreversible/outbound actions (deploy, e-mail, spend, delete, publish, config → gated queue) and for a hard contradiction in the spec that no default resolves. Vague/exploratory goal with no runnable criteria → ask first (one batch), then autopilot. NOT for text/reports (use loop_agent.md), NOT for validating an idea before building (use /roast), NOT for extracting a spec via long dialogue (use /grill-me), NOT for a trivial one-line fix (edit directly).
argument-hint: "[cíl + akceptační kritéria, nebo nech prázdné a doptám se v jednom zátahu]"
---

# Autopilot — jeden cíl, jeden zátah otázek, pak to dojedu sám

## Co to dělá (a co slibuje)

Josef dá **cíl**. Já se **jednou** doptám na to nezbytné, on odpoví, a od té chvíle **nejedu se ptát** — stavím a ověřuju spustitelný kód přes Plan→Build→Judge, dokud to reálně neprojde. Zastavím se jen ve dvou případech (viz níže). Výstup: funkční kód + report.

> Promise: **právě jeden round otázek na začátku.** Když se ptám podruhé, buď je to nevratná akce, nebo tvrdý rozpor v zadání — nic jiného mě zastavit nesmí.

Tohle je [[Skilly/agent_loop_pbj|PBJ]] s pořádným vstupním interview vepředu a state filem, aby loop věděl, kdy je „hotovo", a nemusel se doptávat v půlce.

## Proč se jinak ptám v půlce (a proč tohle funguje)

Doptávání v půlce = „hotovo" není definované. Autopilot to řeší tím, že na startu zamkne **tři věci**:

1. **Cíl** — co má kód dělat (dává Josef).
2. **Akceptační kritéria** — *spustitelné* „hotovo" (Judge je musí umět reálně otestovat). Bez nich loop nekonverguje.
3. **Defaulty pro rozcestí** — co udělám, když narazím na volbu, místo abych se ptal.

Zamčeno na startu → zbytek dojedu bez tebe.

## FÁZE 1 — Intake (JEDEN round, pak už žádné otázky)

Cíl: nasbírat vše potřebné v **jednom** dávkovém kole. Ne otázka po otázce (to je /grill-me) — **jedna dávka, pak jedeš**.

Postup:

1. **Zjisti dnešní datum** (`date +%F`) a **detekuj projekt/stack** z kontextu (Routing Map v CLAUDE.md; jazyk/framework z repa). Nehádej naslepo — když je repo jasné, přečti ho.
2. **Navrhni akceptační kritéria SÁM** (spustitelná; **škáluj dle velikosti**: ~3–5 malý fix, ~12–20+ appka/více komponent) z cíle. Nenech to na Josefovi — je to moje práce. Kritéria musí být ověřitelná, ne vágní:
   - ❌ „appka je user-friendly"
   - ✅ „po `npm run dev` se na localhost:3000 načte stránka bez chyby v konzoli"
   - ✅ „`POST /api/order` vrátí 200 a uloží řádek do DB"

   **⭐ Acceptance jako kód, ne jako odrážky.** Kdykoli to jde, nepiš kritéria jako markdown seznam — napiš je jako **spustitelný artefakt**, který Judge jen pustí:
   - testovací soubor (`tests/acceptance.spec.ts`, `test_acceptance.py`) nebo shell skript s `exit 1` při selhání,
   - u webu **HTML mockup** cílového stavu místo popisu designu (mockup v kódu je přesnější zadání než próza nebo screenshot),
   - u portu/napojení **odkaz na existující funkci nebo endpoint**, který se má chovat stejně.

   Ulož ho vedle spec souboru a v `ACCEPTANCE` na něj odkaž (`ACCEPTANCE: viz ./acceptance.spec.ts + níže vypsané body`). Judge pak verifikuje **běh**, ne prózu — a kritéria nejde vyložit dvěma způsoby. Markdown odrážky nech jen na to, co se spustit nedá (např. „diff neobsahuje zakomentovaný kód").
   Když je kritériem **vkus** (design, tón, API), přilož rubriku: `Skilly/taste-score/`, `voice-principles.md`, `Skilly/agent-ready-web/`.
3. **Navrhni decision-defaulty** pro pravděpodobná rozcestí (např. „chybí data → dopočítej a označ", „styl → drž stávající konvenci repa", „nová dependency → ano, ale zapiš kterou").
4. **Předlož VŠECHNO k odsouhlasení v jedné zprávě** — cíl (jak jsem ho pochopil) + kritéria + defaulty + detekovaný stack + `MAX_LOOPS` (default 5) + připomenutí dvou stop-gate. Použij `AskUserQuestion` pro strukturované volby, kde dávají smysl; jinak jeden krátký blok „tohle beru jako zadání — edituj, nebo řekni *jeď*".
5. **Josef odpoví jednou** (edituje/potvrdí). Tím intake KONČÍ.

Když je cíl vágní a nejde z něj kritéria odvodit, doptej se — ale pořád **v jedné dávce** (klidně přes `AskUserQuestion`, více otázek naráz), ne v sérii.

## FÁZE 2 — Lock: zapiš spec do souboru (zdroj pravdy)

Před spuštěním loopu ulož zamčené zadání na disk (per Context discipline — práce cestuje jako soubory, ne jako historie chatu):

- **Kam:** mapuje-li cíl na projekt → `Brain/Projects/<Projekt>/Process/{YYYY-MM-DD}-autopilot-{slug}.md`; jinak `Brain/Brainstorms/{YYYY-MM-DD}-autopilot-{slug}.md`.
- **Co do souboru:**
  ```
  # Autopilot spec — {slug} ({YYYY-MM-DD})
  CÍL:            <jedna věta>
  ACCEPTANCE:     <3–5 spustitelných kritérií>
  STACK/REPO:     <jazyk/framework + cesta>
  DEFAULTY:       <rozhodovací pravidla pro forky>
  STOP-GATES:     nevratné akce (deploy/e-mail/spend/delete/publish/config) + tvrdý rozpor v zadání
  MAX_LOOPS:      <default 5>
  GATED QUEUE:    <sem loop píše nevratné akce čekající na tvůj souhlas>
  LOG:            <sem loop píše rozhodnutí u forků + verdikt každého kola>
  ```
- **Řekni jednou větou, kam jsi uložil.** Tenhle soubor je zdroj pravdy; kritéria se v průběhu **nezměkčují** (contract fáze je smí jen zpřísnit/rozšířit, nikdy zeslabit — finální seznam se zapíše zpět do LOG, viz FÁZE 4).

## FÁZE 3 — Autonomní běh (Plan→Build→Judge)

Spusť [[Skilly/agent_loop_pbj|PBJ]] přes nástroj **Workflow** s `args: { task, acceptance, maxLoops }` ze spec souboru. Loop: **CONTRACT** → PLAN → BUILD (ve worktree) → JUDGE, dokud Judge vrací `pass:false` a nedošel `MAX_LOOPS`. Pravidla PBJ platí beze změny (Judge appku REÁLNĚ spustí; Builder opravuje jen co Judge označil; kritéria se nezměkčují; Planner se přepočítá jen při `plan_is_wrong`).

Dvě věci navíc oproti holému intake:
- **Contract fáze (adversariální).** Před stavbou Judge-kritik jednou zpřísní/rozšíří moje kritéria (najde vágní/chybějící/edge cases). Běží až tady, uvnitř loopu — intake s Josefem zůstává jedno kolo, slib „už se neptám" platí.
- **Judge staví na „appka je rozbitá".** Nepotvrzuje funkčnost, dokazuje selhání; při pochybnosti FAIL (proti přitakávání).

**Během běhu se NEPTÁM.** Forky řeším sám podle DEFAULTŮ ze specu a zapíšu rozhodnutí do LOG v souboru. Jen dva důvody smí loop zastavit a vyžádat si tě:

### STOP-GATE A — nevratná / odchozí akce
Deploy, odeslání e-mailu/zprávy, útrata, mazání dat, publikace, změna účtu/konfigurace, cokoliv co opouští stroj/vault. **Loop to NEUDĚLÁ sám** (safe-fail L2). Místo toho:
- akci připraví jako **draft / dry-run / připravený příkaz**,
- zapíše ji do **GATED QUEUE** ve spec souboru,
- pokračuje ve všem ostatním, co jde bez ní.
Na konci ti gated akce předložím k jednomu odkliknutí. (Loop staví + ověřuje v worktree — to je celé vratné; nevratné je až to, co jde ven.)

### STOP-GATE B — tvrdý rozpor v zadání
Když narazím na rozpor/nejednoznačnost, kterou **žádný default neřeší** (dvě kritéria si odporují; cíl jde proti realitě repa; Judge X kol po sobě padá na tomtéž bez pokroku → zadání je nejspíš vadné, ne provedení). Pak:
- zastavím, **položím jednu cílenou otázku** (co přesně je v rozporu + moje navrhované řešení),
- po odpovědi upravím spec soubor a **jedu dál** bez dalšího ptaní.

Anti-thrash: stejné kritérium padá 3 kola po sobě bez pokroku → zastav a eskaluj (Gate B). Nemlať hlavou do zdi do vyčerpání `MAX_LOOPS`.

## FÁZE 4 — Report (konec)

Když Judge dá PASS (nebo dojde `MAX_LOOPS`):
- **Status:** PASS / STOP + kolik kol.
- **Finální kontrakt:** zapiš contract-rozšířená kritéria (`acceptance` z návratu workflow) do `LOG` ve spec souboru — ať zámek kritérií sedí s tím, co Judge reálně vymáhal (ne jen s původním návrhem z intake).
- **Co prošlo / co ne** (poslední feedback od Judge, když STOP).
- **Kde je kód** (worktree/branch) + jak to spustit.
- **GATED QUEUE:** nevratné akce čekající na tvůj souhlas, každou s přesným příkazem/draftem k odkliknutí. E-mailové drafty → povinný řádek `✉️ PŘED ODESLÁNÍM PŘEPNI ODESÍLATELE NA: <alias>` (viz CLAUDE.md).
- Nabídni `/session-close`, pokud práce pokračuje nebo padlo netriviální rozhodnutí.

## Kdy NEpoužít

- **Text / report / strategie / e-mail** → [[Skilly/loop_agent|loop_agent]] (Maker/Checker), ne tohle.
- **Validace nápadu před stavbou** → [[Skilly/roast/SKILL|roast]].
- **Vytáhnout spec z hlavy dlouhým rozhovorem** → [[Skilly/grill-me/SKILL|grill-me]] (otázka po otázce). Autopilot je opak: jedna dávka, pak ticho.
- **Triviální fix / jednoduchá změna** → udělej přímo, loop je overkill.

## Náklady

3 agenti × N kol (PBJ). Pro 5 kol ~15 agentích běhů + spouštění appky. Drahé — heads-up jednou větou, pak jeď (per centrální pravidlo pro skilly). `MAX_LOOPS` střízlivě: 3 malé, 5 střední.

<!-- AUTO-LINKS:START -->
## 🔗 Souvislosti
- [[CLAUDE|CLAUDE (master)]]
<!-- AUTO-LINKS:END -->
