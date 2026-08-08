# Název skillu: Loop Agent
# Kdy použít: Kdykoliv tě Josef požádá o komplexní úkol kde záleží na kvalitě výstupu — report, strategie, analýza, obsah, kód, plán. Aktivuje se slovem "loop", "/loop" nebo "použij loop mode".

---

## Princip

Místo jednoho výstupu pracuješ v cyklu dokud výsledek neprojde přísným gatem. Přepínáš mezi dvěma rolemi:

- **MAKER** — produkuje výstup, rychle, bez autocenzury
- **CHECKER** — hodnotí výstup jako skeptický kritik, hledá slabiny, ne chyby v gramatice

Tato separace je klíčová. Model který práci udělal je příliš shovívavý sám na sebe. CHECKER musí být záměrně přísný.

---

## Postup — každá iterace

### KROK 1 — SETUP (pouze v první iteraci)
Před zahájením loopu vyžádej od Josefa (nebo odvoď z kontextu):

```
TASK:        [co přesně má být výsledkem]
CRITERIA:    [3–5 měřitelných podmínek úspěchu — konkrétní, ne vágní]
MAX LOOPS:   [výchozí: 5, nebo dle složitosti]
```

Pokud Josef nedodá kritéria, navrhni je sám a **rovnou rozjeď loop** (jedna věta oznámení, ne blokující „potvrzuješ?"). Loop je drahý (~4× tokeny) → heads-up ať může zabrzdit, ale nečekej na „ano". Per centrální pravidlo pro skilly v CLAUDE.md.

### KROK 2 — PLAN
Jednou větou: co je nejslabší bod aktuálního výstupu a co v tomto kole opravíš. Pokud jde o první kolo: co je tvůj přístup.

### KROK 3 — DO (MAKER role)
Proveď práci. Produkuj celý výstup nebo aktualizovanou verzi. Bez autocenzury, bez "omlouvám se za nedokonalost".

### KROK 4 — VERIFY (CHECKER role)
Přepni na roli přísného kritika. Ohodnoť každé kritérium na škále 1–10:

```
VERIFY — kolo [N]:
├─ [Kritérium 1]: X/10 — [co konkrétně je slabé]
├─ [Kritérium 2]: X/10 — [co konkrétně je slabé]
├─ [Kritérium 3]: X/10 — [co konkrétně je slabé]
└─ NEJSLABŠÍ BOD: [kritérium s nejnižším skóre]
```

Buď brutálně upřímný. 7/10 není úspěch.

**Kritérium na vkus → skóruj proti rubrice, ne proti dojmu.** Když kritérium není měřitelné faktem („je to dobrý design", „zní to jako Josef", „dobré API"), nedávej CHECKERovi prózu — dej mu existující rubriku a nech ho skórovat proti jejím bodům:
- design / frontend → `Skilly/taste-score/`
- text psaný za Josefa → `voice-principles.md`
- web (strojová čitelnost) → `Skilly/agent-ready-web/`

U výstupů, kde je vkus hlavní kritérium, spusť CHECKERa jako **samostatné verifier agenty** (Workflow/Agent) — každý s jednou rubrikou, jednou čočkou. Vlastní práci si model odpouští; cizí agent s rubrikou ne.

### KROK 5 — DECIDE

```
→ FINAL     pokud VŠECHNA kritéria ≥ 8/10
→ ITERATING pokud jakékoliv kritérium < 8/10
→ STOP      pokud dosažen MAX LOOPS limit
```

Při **ITERATING**: začni znovu od KROK 2, opravuj výhradně nejslabší bod z VERIFY.

Při **FINAL**: prezentuj výsledek čistě bez loop metadat. Shrň co se změnilo oproti prvnímu pokusu.

Při **STOP** (limit): reportuj stav — co prošlo, co ne, a co by bylo třeba pro FINAL.

---

## Pravidla

- **Neptat se na otázky během loopu.** Pokud ti něco chybí, udělej sensible assumption, poznamenej ji a pokračuj.
- **Vždy opravovat nejslabší bod.** Ne ten, který se ti líbí opravovat. Ten s nejnižším skóre.
- **Nikdy nevolat FINAL pokud jakékoliv kritérium < 8.** Ani kdyby se to blížilo.
- **Kritéria jsou neměnná.** Nelze je v průběhu loopu změkčit.
- **Krátký výstup je lepší než dlouhý, který nesplňuje kritéria.**

---

## Formát výstupu v každém kole

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LOOP [N/MAX]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PLAN: [jedna věta — co opravuješ a proč]

[VÝSTUP — celý aktualizovaný dokument/text/analýza]

VERIFY:
├─ [kritérium 1]: X/10 — [poznámka]
├─ [kritérium 2]: X/10 — [poznámka]
└─ [kritérium 3]: X/10 — [poznámka]

→ ITERATING / FINAL / STOP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Příklady použití

**Bankability Report:**
```
TASK: Finální Bankability Report pro klienta XY
CRITERIA:
- Executive summary srozumitelná člověku bez fin. vzdělání: ≥8
- Každý ukazatel má konkrétní doporučení (ne obecné rady): ≥8  
- Risk sekce pojmenovává 3 konkrétní stop-faktory pro banku: ≥8
MAX LOOPS: 4
```

**Strategie / plán:**
```
TASK: Go-to-market strategie pro <produkt> na Q3
CRITERIA:
- Každý kanál má konkrétní čísla (budget, objem, timeline): ≥8
- Rizika jsou pojmenovaná a mají mitigation: ≥8
- Akční kroky lze začít tento týden bez dalšího plánování: ≥8
MAX LOOPS: 5
```

**Obsah / email:**
```
TASK: Cold email sekvence pro bankability (3 emaily)
CRITERIA:
- Každý email má jasné CTA a jeden hlavní bod: ≥8
- Tón odpovídá stylu Josefa (přímý, bez fluffu): ≥8
- Otevírací věta každého emailu hákuje bez clickbaitu: ≥8
MAX LOOPS: 3
```

---

## Poznámka k nákladům

Každá iterace spotřebuje přibližně stejně tokenů jako nový prompt. Pro 4 iterace počítej 4× náklady. Používej loop pouze tehdy, kdy kvalita výsledku stojí za to — ne pro jednoduché dotazy.

<!-- AUTO-LINKS:START -->
## 🔗 Souvislosti
- [[CLAUDE|CLAUDE (master)]]
<!-- AUTO-LINKS:END -->
