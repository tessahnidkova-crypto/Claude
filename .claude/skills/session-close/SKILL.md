---
name: session-close
description: Uzávěrka session — použij na konci větší práce nebo když Tessa řekne "zavři session", "session-close", "/session-close", "uzavři to", "handoff", "předej session", "shrň to". Operacionalizuje compounding loop — zachytí, co se rozhodlo a naučilo, aby se to příště nemuselo řešit znovu; zapíše to do souborů ve vaultu a pushne, aby to bylo i na druhém zařízení; a když práce pokračuje, napíše handoff pro plynulé navázání. NENÍ to rolling checkpoint uprostřed práce — to je /checkpoint.
---

# Session Close — uzávěrka session

## Princip

Konec práce není „hotovo" — je to okamžik, kdy se systém učí. Čtyři otázky, vždy stejné pořadí:

1. **Co jsme rozhodly nebo opravily?** → do `LOG.md`
2. **Co se opakovalo?** → kandidát na nový skill
3. **Změnil se nějaký trvalý fakt?** → do `MEMORY.md` / `KB.md`
4. **Bude práce pokračovat?** → handoff do `Process/`

Drž to rychlé (cíl: pár řádků). Žádný balast — jen to, co má hodnotu příště.

---

## Postup

### KROK 1 — Identifikuj projekt

Urči, kterého projektu se session týkala (per Routing Map v `CLAUDE.md`). Pokud žádného konkrétního, zapisuj globálně do `MEMORY.md`.

### KROK 2 — Zápis do LOG.md

Projdi session a vytáhni **netriviální rozhodnutí a opravy** (ne mechanické kroky). Pro každé jeden řádek:

```
RRRR-MM-DD — [co se rozhodlo/opravilo] — [proč, stručně]
```

Zapiš na začátek sekce roku v `Projekty/<Projekt>/LOG.md` (nejnovější nahoře). Drobné dotáhni sama; když si nejsi jistá relevancí, ukaž návrh řádků k odsouhlasení.

**U studia sem patří i tohle:** „u zkoušky z X se ptali hlavně na Y", „tenhle způsob učení nefungoval, tenhle ano", „skripta se rozcházejí s přednáškou v Z".

### KROK 3 — Detekce opakování → skill

Zeptej se sama sebe: **„Udělala jsem totéž už potřetí?"** (napříč sessions, ne jen dnes.)

- Ano → *„Tohle je skill čekající na vznik."* Navrhni konkrétní skill (název + co by dělal). Skill vytvoř až na potvrzení, do `.claude/skills/<name>/SKILL.md`, a připomeň, že **se načte až v nové session**.
- Ne → přeskoč.

### KROK 4 — Aktualizace paměti

Změnil se během session **trvalý fakt** (termín zkoušky, výsledek, status předmětu, kontakt, cíl)?

- Globální / štíhlý fakt → `MEMORY.md`
- Operační detail projektu → `Projekty/<P>/KB.md`
- Předpis chování („vždy / nikdy…") → master `CLAUDE.md` — **napřed se zeptej**, tenhle soubor se needituje bez svolení

`MEMORY.md` drž štíhlý — staré přesouvej do `ARCHIVE.md`.

### KROK 5 — Handoff (jen když práce bude pokračovat)

**Kdy:** rozdělaná práce bude pokračovat příště — nedokončené výpisky, rozepsaný plán, rozpracovaný text. **Čistě uzavřená session → přeskoč**, do shrnutí napiš „handoff: netřeba".

**Kam:** `Projekty/<Projekt>/Process/handoff-RRRR-MM-DD.md`

**Jak:** syntéza toho, co se dělo v TÉTO session — ne audit filesystému. Projdi **celou** konverzaci, ne jen poslední pár tahů. Použij přesně tuhle strukturu, sekci nikdy nevynechávej — když je prázdná, napiš „žádné":

```
# Handoff — <RRRR-MM-DD> — <jednořádkový titul>

## Kde to začalo
<2–3 věty: co Tessa chtěla, klíčové omezení, co se vyjasnilo>

## Rozhodnuto + co je hotové
- <rozhodnutí/změna> — <proč, a kde to žije (cesta od kořene repa)>

## Klíčové soubory pro příští session (číst v tomhle pořadí)
- `<cesta>` — <proč číst jako první>

## Stav teď
- Rozpracované: <co je rozdělané a kde> — nebo „žádné"

## Odloženo + otevřené otázky
- Odloženo: <položka> — <proč>
- Otevřené: <otázka na Tessu> — <kontext>

## Naval tady
<1–2 věty: nejpravděpodobnější další akce pro čerstvou session>
```

Terse a konkrétní: cesty, rozhodnutí, otázky. Žádné hodnocení „co šlo dobře".

### KROK 6 — Commit a push (POVINNÉ, neptej se)

```
git add -A && git commit -m "session-close: <téma>" && git push -u origin <branch>
```

⚠️ **Bez pushnutí je celá uzávěrka k ničemu.** Kontejner se smaže a na mobilu z toho nebude nic. Tohle je jediný krok, který se nesmí vynechat.

### KROK 7 — Shrnutí (1 blok)

```
UZÁVĚRKA SESSION — <Projekt>
• LOG:      [X záznamů zapsáno / 0]
• SKILL:    [návrh: <název> / nic]
• PAMĚŤ:    [co aktualizováno / nic]
• HANDOFF:  [Process/handoff-RRRR-MM-DD.md / netřeba]
• PUSH:     [commit <hash> pushnut / ⚠️ selhalo]
• DALŠÍ:    [1 navazující krok, pokud nějaký je]
```

---

## Pravidla

- **Nezapisuj balast.** Když session nepřinesla nic trvalého, řekni to rovnou („nic k zápisu") — neforsíruj záznamy pro formu.
- **Soubory > chat.** Cílem je, aby příští session nezačínala od nuly.
- **Handoff = syntéza, ne audit.** Popisuješ, co se dělo v TÉTO session. Ale projdi celou konverzaci — handoffy nejčastěji zapomenou věci ze středu session.
- **Handoff = stabilní struktura.** Sekci nikdy nevynechávej. Stabilita je celý smysl.
- **Úprava globálních pravidel = napřed se zeptej.** Projektové logy a fakty dotahuj sama.
