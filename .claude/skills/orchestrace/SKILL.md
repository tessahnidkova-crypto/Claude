---
name: orchestrace
description: Rozhodovací strom „jakým postupem tuhle práci vzít" — kdy zkousej-me, kdy vypisky, kdy plan-uceni, kdy checkpoint, a kdy prostě odpovědět přímo; plus pravidla toku práce mezi sessionami (context discipline) a kdy poslat subagenta. Přečti, když volba postupu není zřejmá, když plánuješ delší práci na víc sessionů, nebo když se chystáš nasypat do hlavní konverzace hromadu materiálu. NENÍ to engine — jen router.
---

# Orchestrace — jakým postupem vzít tuhle práci

## Rozhodovací strom (shora dolů, první shoda vyhrává)

| Situace | Postup | Cena |
|---|---|---|
| Rychlý dotaz, lookup, „co znamená X", drobná editace | **přímo**, žádný skill | 1× |
| „Vyzkoušej mě", „zkoušej mě z X", příprava na ústní zkoušku | **`/zkousej-me`** | nízká |
| Mám skripta / přednášku / PDF / fotky a chci z toho učební materiál | **`/vypisky`** | střední |
| Blíží se termín, potřebuju rozvrhnout učení | **`/plan-uceni`** | nízká |
| Dlouhá práce, hrozí ztráta kontextu, nebo před rizikovým krokem | **`/checkpoint`** | minimální |
| Konec práce, něco se rozhodlo nebo naučilo | **`/session-close`** | nízká |
| Text, na kterém záleží (žádost, motivační dopis, formální e-mail) | napiš draft → **sama si ho zkritizuj** jako skeptický čtenář → přepiš. Teprve pak ukaž. | ~2× |
| Velký rozsah — projít 20 souborů, audit vaultu, hledání napříč | **subagent** (Explore / general-purpose) | dle počtu |

## Jak drahý postup ohlásit

Drahý postup **oznam jednou větou a rovnou rozjeď** — nečekej na souhlas:
> „Beru to přes /vypisky, chvíli to potrvá — zabrzdi, pokud nechceš."

Heads-up ano, blokující „chceš?" ne. (Nevratné/odchozí akce jsou jiná kategorie — tam se vždy zastav, viz safe-fail v `CLAUDE.md`.)

## Intake kontrakt — než rozjedeš delší práci

Zamkni tři věci, jinak se budeš doptávat v půlce:

1. **Cíl** — jedna věta, co má být hotovo.
2. **Kritérium „hotovo"** — konkrétní, ověřitelné. U studia obvykle: *„umím odpovědět na všech 12 otázek z okruhu bez nahlédnutí"*, ne *„rozumím tomu"*.
3. **Decision-defaulty** — co uděláš na rozcestí místo ptaní.

Vše předlož **v jedné zprávě**. Tenhle jeden round **JE** to doptání. Po odkývnutí zamkni zadání do `Projekty/<P>/Process/{RRRR-MM-DD}-{slug}.md` a dál se neptej.

**Anti-thrash:** když se stejná věc nedaří třikrát po sobě, je nejspíš vadné zadání, ne provedení. Eskaluj jednou cílenou otázkou.

## Context discipline — jedna session, jeden čistý job

- **Jeden job pořádně, pak nová session.** Nemíchej „udělej mi výpisky z anatomie" + „naplánuj mi týden" + „napiš e-mail" do jedné nekonečné session — slije se to a kvalita klesá.
- **Práce cestuje jako soubory, ne jako historie chatu.** Výstup ulož do vaultu a **pushni**. Další job z něj čte. Nespoléhej na „pamatuju si to z konverzace" — na druhém zařízení si to nepamatuješ.
- **Ulož ZDROJ, ne jen export.** Tahák ulož jako markdown vedle PDF.
- **Delegační otázka:** „Chystám se nasypat do chatu hromadu věcí, které už nikdy nepřečtu?" → pošli subagenta. Chytrý šéf, levní dělníci.
- **Handoff:** když práce bude pokračovat příště, zapiš handoff přes `/session-close`.

## Kdy poslat subagenta a kdy ne

**ANO:** prohledat celý vault, projít mnoho souborů, mechanická hromadná editace, hledání „kde jsem to psala".

**NE:** cokoli, kde záleží na faktické správnosti odborného obsahu. Subagent vrací tvrzení, ne fakt — u studijních materiálů ověř každý nález proti zdroji, než ho zapíšeš. (Viz gotcha v `CLAUDE.md`.)
