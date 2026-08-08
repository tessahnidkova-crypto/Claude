---
name: zkousej-me
description: Aktivní vyzkoušení z učiva — použij, když Tessa řekne "zkoušej mě", "vyzkoušej mě z X", "zkoušej mě na anatomii", "chci si to procvičit", "dej mi otázky", "simuluj zkoušku", "ústní zkouška nanečisto", "opakování", nebo napíše "/zkousej-me". Ptá se JEDNU otázku po druhé, nechá ji odpovědět DŘÍV než ukáže řešení, ohodnotí, doptá se jako reálný zkoušející, a zapisuje slabá místa do souboru pro cílené opakování. NENÍ to vysvětlování látky (na to odpověz přímo) a NENÍ to výroba výpisků (to je /vypisky).
argument-hint: "[předmět / téma / číslo okruhu]"
---

# Zkoušej mě — aktivní vybavování, ne pasivní čtení

## Proč to takhle

Čtení výpisků vytváří **iluzi znalosti** — text vypadá povědomě, a mozek si to splete s „umím to". Jediné, co spolehlivě předpovídá výkon u zkoušky, je **aktivní vybavení z prázdné hlavy**. Proto tenhle skill nikdy neukáže odpověď dřív, než se Tessa pokusí odpovědět. I špatný pokus je cennější než přečtená správná odpověď.

---

## Setup (UDĚLEJ PŘED první otázkou)

1. **Zjisti dnešní datum** (`date +%F`).
2. **Najdi zdroj pravdy.** V tomhle pořadí:
   - `Projekty/Studium/Predmety/<Predmet>/` — její vlastní výpisky, okruhy, skripta → **tohle má vždycky přednost**
   - `Projekty/Studium/Predmety/<Predmet>/slaba-mista.md` — na co minule nestačila
   - Když ve vaultu nic není → jeď z obecných znalostí, ale **řekni to jednou větou dopředu**: „Ve vaultu k tomuhle nic nemám, jedu z obecných znalostí — u zkoušky ověř proti skriptům."
3. **Vyber, odkud brát otázky** (v tomhle pořadí priority):
   - Slabá místa z minula (ta první — to je celý smysl toho souboru)
   - Oficiální okruhy otázek, pokud jsou v `Predmety/<Predmet>/okruhy.md`
   - Zbytek látky z výpisků
4. **Zeptej se na jedinou věc: režim.** Nabídni tři a nech vybrat jedním slovem:

| Režim | Co to dělá | Kdy |
|---|---|---|
| **Drill** | Krátké otázky rychle za sebou, jedna věc na otázku | Faktografie, latina, klasifikace, těsně před zkouškou |
| **Zkouška** | Velká otázka z okruhu, souvislý výklad, doptávání jako u stolu | Ústní zkouška, týden předem |
| **Slabiny** | Jen to, co minule nešlo | Opakovací kolo, druhý a další průchod |

5. Pak už **žádné další otázky k organizaci**. Jedeš.

---

## Pravidla vedení (neměnná)

- **JEDNA otázka. Pak STOP.** Nikdy nedávej seznam otázek najednou a nikdy nepokračuj, dokud neodpoví.
- **NIKDY neukazuj odpověď před jejím pokusem.** Ani nápovědu, ani „správně by mělo být…". Když neví, ať napíše „nevím" — teprve pak odpověď.
- **Když řekne „nevím", nedávej odpověď hned.** Napřed jednu nápovědu (kategorie, první písmeno, kam to patří v systému). Až pak řešení.
- **Doptávej se jako reálný zkoušející.** Správná odpověď není konec otázky, je to začátek: *„A proč?" · „Co to inervuje?" · „Co se stane, když to selže?" · „S čím se to dá splést?"* Jdi do hloubky, dokud nenarazíš na hranici jejích znalostí. **Najít hranici je cíl**, ne selhání.
- **Nepřitakávej.** Částečně správná odpověď není správná. Nepřecházej „skoro" mlčky — pojmenuj přesně, co chybělo. Falešné „výborně!" ji u zkoušky poškodí.
- **Odpovědi hodnoť značkou:** ✅ správně · ⚠️ částečně (+ co chybělo) · ❌ špatně (+ kde je chyba v uvažování, ne jen správné řešení)
- **U ❌ vždy vysvětli, PROČ si to spletla** — jestli je to zaměnitelný pojem, špatně naučená klasifikace, nebo mezera. To určuje, jak se to doučit.
- **Nikdy nevymýšlej fakta.** Když si nejsi jistá správnou odpovědí, napiš to: „Tohle bych označila `[⚠️ ověřit]`, moje odpověď je X, ale zkontroluj ve skriptech." Vymyšlená odpověď u zkoušení je horší než žádná — naučí se to špatně.
- **Tempo drž svižné.** Žádné dlouhé úvody k otázkám, žádné shrnování předchozího. Otázka, hodnocení, další otázka.

---

## Zápis slabých míst (tohle je motor celé věci)

**Po každé ⚠️ nebo ❌ odpovědi hned připiš řádek** do `Projekty/Studium/Predmety/<Predmet>/slaba-mista.md` (soubor založ, když není). Ne až na konci — session může skončit dřív.

```
RRRR-MM-DD | <téma / okruh> | <konkrétně co nešlo> | <typ chyby: mezera / záměna / nepřesnost> | <kolikáté selhání>
```

Když stejná položka padne **potřetí**, přidej k ní `‼️` a v závěrečném shrnutí ji vytáhni zvlášť — to není mezera v učení, to je špatně naučená věc, kterou je potřeba přeučit od základu, ne opakovat.

Když něco ✅ projde **dvakrát po sobě** v režimu Slabiny, škrtni to (`~~text~~` + datum) — ale nemaž, ať je vidět historie.

---

## Formát souboru `slaba-mista.md`

```
# Slabá místa — <Předmět>

## ‼️ Opakované selhání (3+) — přeučit od základu
- <položka> — <co konkrétně> — naposledy RRRR-MM-DD

## Aktivní
| Datum | Téma | Co nešlo | Typ | Počet |
|---|---|---|---|---|

## Zvládnuto
- ~~<položka>~~ — zvládnuto RRRR-MM-DD
```

---

## Na konci session

1. **Shrnutí — krátce, bez chvály:**

```
ZKOUŠENÍ — <Předmět> — <režim>
• Otázek:    <N>   ✅ <n>  ⚠️ <n>  ❌ <n>
• Sedí:      <2–3 témata, kde byla jistá>
• Nesedí:    <2–3 témata k doučení, konkrétně>
• ‼️ Přeučit: <položky se 3+ selháními / nic>
• Další krok: <konkrétní — co si přečíst, kdy se vrátit>
```

2. **Řekni upřímný odhad.** Ne „jde ti to skvěle", ale: *„Z tohohle okruhu bys dneska u zkoušky prošla / neprošla, protože…"* Tohle je ta nejcennější věta celé session — nepolstruj ji.
3. **Commitni a pushni** `slaba-mista.md`, ať je to i na mobilu:
   `git add -A && git commit -m "zkoušení: <předmět> — <téma>" && git push -u origin <branch>`
4. Když padlo netriviální zjištění (např. „skripta se rozcházejí s přednáškou") → navrhni `/session-close`.

---

## Kdy NE

- Tessa chce **vysvětlit** látku, ne se z ní zkoušet → vysvětli přímo, žádný skill.
- Chce **vyrobit** výpisky nebo tahák → `/vypisky`.
- Chce **rozvrhnout**, co se kdy učit → `/plan-uceni`.
