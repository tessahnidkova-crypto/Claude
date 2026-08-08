# Název skillu: Agent Loop — Plan / Build / Judge
# Kdy použít: Kdykoliv Josef chce postavit funkční kód nebo appku a záleží na tom, aby to reálně fungovalo (ne jen "vypadalo hotově"). Aktivuje se slovy "agent loop", "PBJ loop", "postav to loopem", "/agent_loop_pbj".

---

## Princip

Tři oddělení agenti běží v cyklu, dokud appka reálně neprojde testem. Každý má **čerstvý kontext** — to je celé tajemství.

- **PLANNER** — rozloží úkol na konkrétní kroky a akceptační kritéria
- **BUILDER** — napíše/upraví kód podle plánu
- **JUDGE (adversariální)** — appku **spustí a aktivně se ji snaží zlomit**, vrátí PASS/FAIL + co konkrétně je špatně

Proč oddělení agenti, ne jeden model přepínající role: model, který kód napsal, je sám na sebe shovívavý ("vždyť to skoro funguje"). JUDGE kód neviděl vznikat → soudí ho jako cizí. To je rozdíl mezi [loop_agent.md](loop_agent.md) (jeden kontext, MAKER/CHECKER, vhodné pro text) a tímhle (kód/appky).

> Vítězové nemají nejchytřejší model. Mají nejlepší loop.

---

## Setup (první iterace)

Vyžádej od Josefa nebo odvoď z kontextu:

```
TASK:        [co přesně má appka dělat — jedna věta]
ACCEPTANCE:  [ověřitelné podmínky — škáluj dle velikosti: ~3–5 malý fix, ~12–20+ appka/více komponent; contract fáze je ještě zpřísní]
STACK:       [jazyk/framework, pokud není jasný z projektu]
MAX LOOPS:   [výchozí 5]
```

Pokud chybí ACCEPTANCE, navrhni je a potvrď před spuštěním. Kritéria musí být **spustitelná**, ne vágní:
- ❌ "appka je uživatelsky přívětivá"
- ✅ "po `npm run dev` se na localhost:3000 načte stránka bez chyby v konzoli"
- ✅ "endpoint POST /api/order vrátí 200 a uloží řádek do DB"

**Nejlepší forma kritéria je kód, ne věta.** Když existuje (nebo jde rychle napsat) testovací soubor, shell skript s `exit 1`, nebo HTML mockup cílového stavu, předej Judgeovi **jeho cestu** a kritérium zněj „`npm test -- acceptance` projde beze zbytku". Judge pak verifikuje běh, ne interpretaci. Vkusová kritéria (design, tón, API) → přilož rubriku (`Skilly/taste-score/`, `voice-principles.md`), ne adjektiva.

---

## Jak to spustit — nástroj Workflow

Tento skill běží přes harness nástroj **Workflow** (deterministická orchestrace agentů). Použij níže uvedený skript jako šablonu — uprav `TASK`, `ACCEPTANCE` a `MAX_LOOPS`, zbytek nech.

Loop logika: PLAN → BUILD → JUDGE, a dokud JUDGE vrací `pass: false` a nedosáhli jsme `MAX_LOOPS`, jdi znovu do BUILD s feedbackem od JUDGE (PLANNER se přepočítá jen když JUDGE řekne, že problém je v plánu, ne v provedení).

```javascript
export const meta = {
  name: 'agent-loop-pbj',
  description: 'Plan→Build→Judge loop: staví kód a cykluje, dokud Judge appku reálně neodklikne',
  phases: [
    { title: 'Contract' },
    { title: 'Plan' },
    { title: 'Build' },
    { title: 'Judge' },
  ],
}

// ── Naplň pro konkrétní úkol ──────────────────────────────
const TASK = args?.task ?? 'POPIS ÚKOLU ZDE'
const ACCEPTANCE = args?.acceptance ?? [
  'kritérium 1 — spustitelné',
  'kritérium 2 — spustitelné',
]
const MAX_LOOPS = args?.maxLoops ?? 5
const CONTRACT = args?.contract ?? true   // adversariální dohoda kritérií před stavbou; =false pro triviální úkol
// ──────────────────────────────────────────────────────────

const CONTRACT_SCHEMA = {
  type: 'object',
  properties: {
    criteria:  { type: 'array', items: { type: 'string' } }, // finální, spustitelná
    added:     { type: 'array', items: { type: 'string' } }, // co kritik přidal + proč
    task_size: { type: 'string', enum: ['small', 'medium', 'large'] },
    notes:     { type: 'string' },
  },
  required: ['criteria', 'task_size'],
}

const VERDICT = {
  type: 'object',
  properties: {
    pass: { type: 'boolean' },
    failing: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          criterion: { type: 'string' },
          evidence: { type: 'string' },   // co Judge reálně viděl (výstup, chyba)
          fix_hint: { type: 'string' },   // konkrétní směr opravy
        },
        required: ['criterion', 'evidence', 'fix_hint'],
      },
    },
    plan_is_wrong: { type: 'boolean' },   // true = problém není v kódu, ale v plánu
    summary: { type: 'string' },
  },
  required: ['pass', 'failing', 'plan_is_wrong', 'summary'],
}

// ── Kontrakt: adversariální kritik zpřísní/rozšíří kritéria PŘED stavbou (Karpathy §III) ──
let acceptance = ACCEPTANCE
if (CONTRACT) {
  phase('Contract')
  const contract = await agent(
    `Jsi JUDGE v roli KONTRAKTORA — adversariální. Než se začne stavět, dohodni SMLOUVU: ` +
    `seznam SPUSTITELNÝCH kritérií, proti kterým appku po stavbě nemilosrdně prohnneš.\n` +
    `Dostal jsi NÁVRH kritérií. Předpokládej, že je DĚRAVÝ: najdi, co chybí, co je vágní/neměřitelné, ` +
    `a jaké edge cases nikdo nepokryl (prázdný vstup, chybný vstup, mobil, chyba souboru/sítě, dvojí spuštění, prázdný stav).\n` +
    `Vágní přepiš na měřitelná, neotestovatelná zahoď.\n` +
    `ŠKÁLUJ POČET PODLE VELIKOSTI ÚKOLU — nenafukuj ani nepodstřel:\n` +
    `  • malý fix / 1 soubor → ~3–5 kritérií\n` +
    `  • appka / více komponent / endpoint+DB → ~12–20+ kritérií (edge cases + chybové cesty)\n` +
    `Zadavatel navrhl ${ACCEPTANCE.length}. Urči správnou velikost z úkolu; ` +
    `málo kritérií = Judge jen orazítkuje (rubber-stamp).\n\n` +
    `ÚKOL: ${TASK}\nNÁVRH KRITÉRIÍ:\n- ${ACCEPTANCE.join('\n- ')}\n\n` +
    `Vrať finální seznam (criteria), co jsi přidal a proč (added) a task_size. ` +
    `JEDNO kolo kritiky — žádná nekonečná debata.`,
    { label: 'contract', phase: 'Contract', schema: CONTRACT_SCHEMA }
  )
  acceptance = contract.criteria?.length ? contract.criteria : ACCEPTANCE
  log(`📋 Kontrakt: ${ACCEPTANCE.length} → ${acceptance.length} kritérií (velikost: ${contract.task_size})`)
}

phase('Plan')
let plan = await agent(
  `Jsi PLANNER. Rozlož tento úkol na konkrétní implementační kroky.\n` +
  `ÚKOL: ${TASK}\n` +
  `AKCEPTAČNÍ KRITÉRIA (musí být splněna):\n- ${acceptance.join('\n- ')}\n\n` +
  `Vrať číslovaný plán souborů a změn. Žádný kód, jen plán. Buď konkrétní: které soubory, jaké funkce, jak se to spustí a otestuje.`,
  { label: 'planner', phase: 'Plan' }
)

let lastFeedback = null

for (let i = 1; i <= MAX_LOOPS; i++) {
  log(`Kolo ${i}/${MAX_LOOPS}`)

  phase('Build')
  await agent(
    `Jsi BUILDER. Naimplementuj kód přesně podle plánu. Edituj reálné soubory v repu.\n\n` +
    `PLÁN:\n${plan}\n\n` +
    (lastFeedback
      ? `JUDGE v minulém kole našel tyto problémy — oprav VÝHRADNĚ je:\n${lastFeedback}\n\n`
      : '') +
    `Po dokončení stručně shrň, co jsi změnil a jak se to spouští.`,
    { label: `builder-k${i}`, phase: 'Build', isolation: 'worktree' }
  )

  phase('Judge')
  const verdict = await agent(
    `Jsi JUDGE — adversariální. Kód jsi neviděl vznikat, posuzuj ho jako cizí a nepřátelský.\n` +
    `VÝCHOZÍ PŘEDPOKLAD: appka je ROZBITÁ. Tvůj úkol NENÍ potvrdit, že funguje — je DOKÁZAT, kde selhává.\n` +
    `Appku REÁLNĚ SPUSŤ (nehádej z kódu) a každé kritérium aktivně zkus ZLOMIT: ` +
    `edge case, prázdný/špatný vstup, mobil, dvojí spuštění, chybějící soubor.\n` +
    `PASS uděl jen tomu, co sis reálným během zasloužil. Když VÁHÁŠ, je to FAIL. Žádné „skoro funguje".\n\n` +
    `ÚKOL: ${TASK}\n` +
    `KRITÉRIA:\n- ${acceptance.join('\n- ')}\n\n` +
    `Pro každé selhávající kritérium uveď evidence (co jsi spustil a co to reálně udělalo) a fix_hint. ` +
    `pass=true jen když jsi VŠECHNA kritéria reálně prohnal a žádné nezlomil. plan_is_wrong=true jen když je chyba v zadání/plánu, ne v provedení.`,
    { label: `judge-k${i}`, phase: 'Judge', schema: VERDICT }
  )

  if (verdict.pass) {
    log(`✅ PASS v kole ${i}: ${verdict.summary}`)
    return { status: 'PASS', loops: i, summary: verdict.summary, plan, acceptance }
  }

  lastFeedback = verdict.failing
    .map(f => `- ${f.criterion}\n  viděno: ${f.evidence}\n  oprava: ${f.fix_hint}`)
    .join('\n')

  // Problém v plánu → přeplánuj, jinak jen rebuild s feedbackem.
  if (verdict.plan_is_wrong) {
    phase('Plan')
    plan = await agent(
      `Jsi PLANNER. Původní plán měl vadu. Přepracuj ho.\n` +
      `ÚKOL: ${TASK}\nKRITÉRIA:\n- ${acceptance.join('\n- ')}\n\n` +
      `Co JUDGE označil za špatně v plánu:\n${verdict.summary}\n\nVrať opravený plán.`,
      { label: `planner-k${i}`, phase: 'Plan' }
    )
  }
}

log(`⛔ STOP — vyčerpán limit ${MAX_LOOPS} kol`)
return { status: 'STOP', loops: MAX_LOOPS, lastFeedback, acceptance }
```

Skript volej přes Workflow s `args: { task, acceptance, maxLoops }`, ať nemusíš editovat tělo.

---

## Pravidla

- **Kontrakt před stavbou (adversariální).** Než se začne stavět, JUDGE-kritik jednou zpřísní a rozšíří kritéria (najde vágní/chybějící/edge cases) — teprve dohodnutý seznam (`acceptance`) se staví a soudí. Počet škáluj dle velikosti: ~3–5 malý fix, ~12–20+ appka. Vypni `args.contract=false` pro triviální úkol.
- **JUDGE je adversariální, ne jen skeptický.** Výchozí předpoklad: appka je rozbitá; úkol = dokázat, kde selhává, ne potvrdit funkčnost. Při pochybnosti FAIL. (Stejný adversariální default jako `/taste-score` — proti přitakávání, Karpathy §II.)
- **JUDGE musí appku reálně spustit**, ne číst kód. PASS bez spuštění je zakázaný.
- **BUILDER opravuje jen to, co JUDGE označil.** Žádné "při té příležitosti jsem ještě...".
- **Kritéria jsou neměnná.** V průběhu loopu se nezměkčují.
- **PLANNER se přepočítá jen při `plan_is_wrong`.** Jinak je drahé a zbytečné plánovat znovu.
- **BUILDER běží ve worktree** (`isolation: 'worktree'`) — izolovaná kopie repa, aby paralelní/opakované buildy nekolidovaly. Po PASS změny review a merge ručně.
- Při STOP (limit) reportuj: co prošlo, co ne, poslední feedback od JUDGE.

---

## Kdy NEpoužít

- Text, report, strategie → použij [loop_agent.md](loop_agent.md) (MAKER/CHECKER, levnější).
- Rychlý fix / jednoduchá změna → udělej přímo, loop je overkill.
- Brainstorming, lookup → loop nedává smysl.

---

## Náklady

3 agenti × N kol (+1 contract běh na startu, když `CONTRACT`). Pro 5 kol počítej zhruba 15 agentích běhů + spouštění appky. Drahé — pouštěj jen když na funkčnosti reálně záleží. Nastav `MAX_LOOPS` střízlivě (3 pro malé, 5 pro střední úkoly).

<!-- AUTO-LINKS:START -->
## 🔗 Souvislosti
- [[CLAUDE|CLAUDE (master)]]
<!-- AUTO-LINKS:END -->
