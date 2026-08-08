---
name: vypisky
description: Výroba studijních materiálů ze zdroje — použij, když Tessa dá skripta, přednášku, PDF, fotky tabule, kapitolu z učebnice nebo poznámky a chce z toho výpisky, shrnutí, tahák, přehled, tabulku nebo kartičky; taky když řekne "zpracuj mi tohle", "udělej z toho výpisky", "shrň mi tu kapitolu", "vytáhni z toho podstatné", nebo napíše "/vypisky". Pracuje VÝHRADNĚ ze zdroje, cituje stránky, odděluje doplněné obecné znalosti a označuje nejisté. NENÍ to zkoušení (to je /zkousej-me) ani plánování učení (/plan-uceni).
argument-hint: "[soubor / téma / předmět]"
---

# Výpisky — ze zdroje do učitelného tvaru

## Tvrdé pravidlo, které přebíjí všechno ostatní

**Zdroj má vždycky přednost před tvou pamětí.** Tessu zkouší konkrétní katedra podle konkrétních skript. Když se tvoje obecné znalosti rozcházejí se zdrojem:

1. Napiš verzi **ze zdroje** jako hlavní.
2. Rozpor zmiň zvlášť: *„Skripta uvádějí X, obecně se uvádí Y — u zkoušky jeď podle skript."*
3. **Nikdy to nepřepiš potichu na svou verzi.**

**Nikdy nedoplňuj fakta, která ve zdroji nejsou, bez označení.** Každé tvrzení musí mít původ:

| Značka | Znamená |
|---|---|
| `[s. 42]` | Ze zdroje, tahle stránka |
| `[+]` | Doplněno z obecných znalostí, ve zdroji to není |
| `[⚠️ ověřit]` | Nejsem si jistá, Tessa musí zkontrolovat |

U **čísel, dávek, klasifikací a latinských názvů** je laťka nejvyšší — tam, kde si nejsi 100% jistá, dej `[⚠️ ověřit]`. Tyhle věci Tessa sama nepozná jako chybné a naučí se je špatně.

---

## Postup

### KROK 1 — Zorientuj se ve zdroji

- Zjisti dnešní datum (`date +%F`).
- Přečti zdroj **celý**, ne jen začátek. ⚠️ Utnutý výstup není důkaz, že tam nic dalšího není — u PDF si ověř počet stran, u dlouhého textu počet znaků.
- **Spočítej strukturu** (kolik kapitol / podkapitol / oddílů) a to číslo si zapamatuj. Na konci ověříš, že jsi žádnou nevynechala. Tichý výpadek celé podkapitoly je nejčastější způsob, jak z výpisků vypadne přesně to, na co se u zkoušky ptají.
- Když je zdroj fotka nebo scan a něco je nečitelné → **řekni to a označ `[nečitelné]`**, nedomýšlej.

### KROK 2 — Zeptej se na JEDINOU věc: na co to je

Formu určuje účel, ne téma. Zeptej se jednou větou a nabídni:

| Účel | Výstup |
|---|---|
| **Naučit se to nazpaměť** | Hierarchické výpisky + tabulky pojmů + mnemotechniky |
| **Zopakovat den před zkouškou** | Tahák — jedna strana, jen kostry, klasifikace, čísla |
| **Pochopit to** | Souvislý výklad s analogiemi + na konci přesná odborná formulace |
| **Zkoušet se z toho** | Sada otázek a odpovědí pro `/zkousej-me` |

Když neodpoví nebo je to zřejmé ze zadání, default = **naučit se nazpaměť**.

### KROK 3 — Napiš výpisky

**Struktura, ne próza.** Souvislý text je nejhorší forma pro učení faktografie.

- **Hierarchie** — nadpisy podle struktury zdroje, ať se v tom dá orientovat i za měsíc
- **Tabulka vždy, když se srovnávají 3+ položky** — klasifikace, typy, rozdíly, diferenciální přehledy
- **Latinské názvy** v samostatné tabulce: `latinsky | česky | co to je / kde to je`
- **Čísla a hodnoty** vypíchni tučně — u zkoušky se ptají přesně na ně
- **„Snadno se plete s…"** — samostatná sekce. Zaměnitelné dvojice jsou nejčastější zdroj chyb u zkoušek a ze zdrojů se nedají vyčíst.
- **Mnemotechniky** navrhni jen tam, kde reálně pomůžou (pořadí, výčty, klasifikace). Nevyrábět do počtu — špatná mnemotechnika je horší než žádná.
- **Zkratky rozepiš** při prvním výskytu.
- **Nezjednodušuj do neškodnosti.** Tohle není shrnutí pro laika. Když je látka složitá, výpisky musí být složité — jen přehledně uspořádané. Detail, na který se u zkoušky ptají, se **nesmí** vyhodit kvůli stručnosti.

### KROK 4 — Ověř invariant (POVINNÉ)

Než výpisky odevzdáš:
- Prošla jsi **všechny** kapitoly/oddíly, které jsi napočítala v KROKU 1? Vyjmenuj je a odškrtni.
- Když některá chybí → dopiš ji. Když ji vynecháváš záměrně (opravdu nepodstatná) → **řekni to nahlas**, ať to Tessa může přebít.
- Projdi výpisky očima na neoznačená tvrzení — má každý fakt značku původu?

### KROK 5 — Ulož

`Projekty/Studium/Predmety/<Predmet>/vypisky-<tema>.md`

- Zdroj patří do `Projekty/Studium/Predmety/<Predmet>/Inputs/` (nebo `Projekty/Studium/Inputs/`), ať jde později dohledat, odkud to je.
- Tahák a hotové výstupy → `Projekty/Studium/Outputs/` **jako markdown**, ne jen jako PDF. (Ulož zdroj, ne jen export — za měsíc to budeš přepisovat.)
- Do hlavičky souboru vždy: `Zdroj: <co to bylo> · Zpracováno: <datum> · Pokrývá: <rozsah>`

### KROK 6 — Commit a push, bez ptaní

```
git add -A && git commit -m "výpisky: <předmět> — <téma>" && git push -u origin <branch>
```

### KROK 7 — Nabídni navázání

Jednou větou, ne seznamem: *„Chceš se z toho rovnou vyzkoušet? → /zkousej-me"*

---

## Šablona výpisků

```
# <Téma> — <Předmět>
Zdroj: <co> · Zpracováno: <RRRR-MM-DD> · Pokrývá: <kapitoly / strany>

## Kostra v deseti řádcích
<to nejdůležitější — tohle si přečteš, když máš 5 minut>

## <Kapitola 1>
### <Podkapitola>
- <fakt> `[s. X]`
- <fakt doplněný> `[+]`

## Klíčové pojmy
| Pojem | Latinsky | Význam | Zdroj |
|---|---|---|---|

## Klasifikace a přehledy
<tabulky>

## Čísla, která se musí umět
| Co | Hodnota | Zdroj |
|---|---|---|

## ⚠️ Snadno se plete s…
| Tohle | vs. | Tamto | Rozdíl |
|---|---|---|---|

## Mnemotechniky
- <jen ty, co reálně pomůžou>

## ⚠️ K ověření
- <co je označené [⚠️ ověřit] a proč>

## Rozpory se zdrojem
- <kde se skripta rozcházejí s obecně uváděným — nebo „žádné">
```

---

## Kdy NE

- Rychlý dotaz „co je X" → odpověz přímo.
- Vyzkoušení z už hotových výpisků → `/zkousej-me`.
- Rozvržení, co se kdy učit → `/plan-uceni`.
