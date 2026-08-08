---
name: grill-me
description: Use when Josef wants to extract what's in his head into a durable, organized file via a relentless one-question-at-a-time interview — "vygriluj mě", "vytáhni mi to z hlavy", "proveď mě tím rozhodnutím", "stress-test tenhle plán/design", "discovery session", "grill me", "sepiš to ze mě", or says "/grill-me". Walks the decision tree branch by branch and CHECKPOINTS every answer to a markdown file in the vault so nothing is lost as context fills. NOT for validating an idea (use /roast), NOT for producing a polished deliverable (use loop_agent), NOT for a quick adversarial brainstorm (use inline "Destrukce nápadů").
argument-hint: "[téma / plán / rozhodnutí k prokádrování]"
---

# Grill Me — vytáhnu ti to z hlavy do souboru

## Co to dělá

Neúnavně tě vyzpovídám o každém aspektu tématu, dokud nedojdeme ke sdílenému pochopení. Procházím strom rozhodnutí větev po větvi a řeším závislosti jednu po druhé. **Skutečný cíl: dostat to, co máš v hlavě, ven — do trvalého, uspořádaného souboru**, aby se nic neztratilo, jak se plní kontext.

## Capture soubor JE celý smysl (non-negotiable)

Dlouhý rozhovor zaplní kontext. Když si odpovědi držím jen „v hlavě", dřív nebo později něco přeházím, slepím nebo ztratím. Proto **checkpointuju na disk po každé jednotlivé odpovědi**. Zdroj pravdy je soubor, ne můj kontext. Nikdy nečekám, až mě požádáš o uložení.

> Tohle je tvoje pravidlo *„práce cestuje jako soubory, ne jako historie chatu"* (Context discipline) aplikované na brainstorm. Když se kontext ztratí kdykoli během session, soubor už drží všechno řečené.

## Setup (UDĚLEJ PŘED první otázkou)

1. **Zjisti dnešní datum** (`date +%F`), pokud ho neznáš.
2. **Urči, kam soubor patří** — respektuj strukturu vaultu, nedělej guláš:
   - Téma mapuje na známý projekt (Routing Map v CLAUDE.md — Blynkr, FSE, Bankability, Investice, Ink_ognito, Automatizace)? → `Brain/Projects/<Projekt>/Process/{YYYY-MM-DD}-{topic-slug}-discovery.md`
   - Nemapuje na žádný projekt? → `Brain/Brainstorms/{YYYY-MM-DD}-{topic-slug}.md` (složku vytvoř, pokud není).
   - Discovery notes = **Process** artefakt. Když z toho později vznikne hotový výstup (plán, spec, mapa), *ten* se přesune do `Outputs/` nebo do `Projects/`; syrový záznam zůstává tady.
3. **Vytvoř soubor hned** s hlavičkou: titul, datum, cíl session, prázdná sekce „Open flags".
4. **Řekni jednou větou, kam ukládáš.** Pak polož Q1.

## Checkpoint rule (neměnné)

Po KAŽDÉ tvé odpovědi, PŘED položením další otázky:
- Připoj strukturovaný záznam do souboru: téma otázky, klíčová fakta a rozhodnutí z odpovědi (tvými slovy tam, kde na formulaci záleží), a flagy (co nešlo zodpovědět + kdo to zodpoví).
- Aktualizuj/oprav dřívější záznamy, pokud je pozdější odpověď změnila.
- Teprve pak polož další otázku.

Nikdy nebatchuj víc odpovědí do jednoho zápisu. Checkpoint = jedna odpověď = jeden zápis.

## Metoda rozhovoru

- **Jedna otázka po druhé.** U každé dej svůj **doporučený návrh odpovědi** (nejlepší odhad z kontextu), ať můžeš jen potvrdit, opravit, nebo přesměrovat. Snižuje to friction — nezačínáš od prázdna.
- **Závislosti řeš v pořadí:** nejdřív ustanov nadřazené rozhodnutí, pak ta, co na něm visí.
- **Když jde odpověď najít, nehas se ptát — najdi ji.** Máš vault, Gmail/DB/Drive konektory a kód. Když ti dám dokument (Google Doc, soubor), přečti ho a vytáhni jen to, co je *nové* — neptej se na to, co už tam je.
- **Když neumíš odpovědět** → zapiš to jako flag se správným ownerem a jdi dál. Nezasekni se.
- **Nepřitakávej (tvrdé pravidlo Josefa).** Když odpověď odporuje dřívější odpovědi nebo deklarovanému cíli, nebo stojí na chatrném předpokladu — **řekni to v tu chvíli**, ne že to potichu zapíšeš. Krátce: „tohle si bije s X, jak to spolu drží?" Grill = tlak, ne stenograf.
- Pokračuj, dokud neřekneš dost, nebo dokud neprojdu všechny větve. U konce dej **backstop na úplnost**: „na co jsme se ještě nedotkli?"

## Struktura capture souboru

```
# {Téma}: Discovery / Brainstorm
Datum: {datum} · Cíl: {jedna věta}

## Shrnutí / klíčová rozhodnutí
(běžící syntéza, aktualizuje se průběžně)

## Q&A log
### Q1 — {téma}
- Ptáno: {otázka}
- Zachyceno: {fakta, rozhodnutí, tvými slovy kde na tom záleží}
- Flagy: {otevřená věc -> owner}
...

## Open flags (čeká na vstup)
- {věc} -> {kdo zodpoví}
```

## Na konci

- Přečti si celý soubor znovu — najdi rozpory a mezery, srovnej je.
- Dej krátký recap: co je zachyceno, co je pořád flagged, a **navržený další krok** — často je to jiný nástroj:
  - Chceš ten plán/nápad teď *rozstřelit*? → **/roast**
  - Chceš z toho *vyrobit* hotový výstup (report, strategie, spec)? → **loop_agent**
  - Je to spustitelný kód, co musí fungovat? → **agent_loop_pbj**
- Discovery doc zůstává v `Process/` jako vstup pro ten další job (práce cestuje jako soubory).
- Když skončila netriviální práce nebo padlo rozhodnutí k navázání → navrhni **/session-close**.

## Kdy NE

- Rychlý dotaz, lookup, triviální úprava → přímo, žádný grill.
- *Validace* nápadu (má cenu to stavět?) → **/roast**.
- Rychlý adverzariální brainstorm bez souboru → inline **„Destrukce nápadů"**.
- *Produkce* kvalitního textu z už jasného zadání → **loop_agent**.

<!-- AUTO-LINKS:START -->
## 🔗 Souvislosti
- [[CLAUDE|CLAUDE (master)]]
<!-- AUTO-LINKS:END -->
