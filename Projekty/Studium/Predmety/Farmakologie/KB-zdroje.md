# Zdroje k farmakologii — co je čím a čemu věřit

Aktualizováno 2026-08-08

## Pořadí důvěryhodnosti

| # | Zdroj | Soubor | Role |
|---|---|---|---|
| **1** | **Podrobná Obecka 2024/2025 („AK")** | `Inputs/obecka-podrobna-cast1.pdf` | **autorita** — nejnovější, nejpodrobnější, odpovídá oficiálním okruhům. Při rozporu platí tenhle. |
| 2 | Oficiální seznam otázek | `Inputs/seznam-otazek-VL.docx` | závazné znění otázek |
| 3 | Podmínky předmětu | `Inputs/podminky-predmetu-Farmakologie-II.pdf` | forma a pravidla zkoušky |
| 4 | Vypracované otázky (Obecka, Specka 1, 2) | `Inputs/obecka-vypracovane…`, `specka-1…`, `specka-2…` | **kostra** — struktura odpovědí, ale ⚠️ obsahuje chyby |
| 5 | Obecné znalosti | — | jen když nic výše téma nepokrývá, vždy značit `[+]` |

## Podrobná Obecka — dvě části, různě čitelné

| Část | Soubor | Stran | Pokrývá | Čtení |
|---|---|---|---|---|
| 1 | ⚠️ `obecka-podrobna-cast1.pdf` | 100 | **O1–O16** | **nepoužívat** — rozbité kódování |
| 1 | ✅ **`obecka-podrobna-cast1-CITELNA.pdf`** | 100 | **O1–O16** | ✅ **text jde extrahovat přímo** |
| 2 | `obecka-podrobna-cast2.pdf` | 72 | **O17–O34** | ✅ **text jde extrahovat přímo** |
| S2/1 | ⚠️ `specka2-podrobna-cast1.pdf` | 91 | **otázky 89–131** | **nepoužívat** — rozbité kódování |
| S2/1 | ✅ **`specka2-podrobna-cast1-CITELNA.pdf`** | 91 | **otázky 89–131** | ✅ **opraveno 2026-08-10, čte se jako text** |
| S2/2 | ⚠️ `specka2-podrobna-cast2.pdf` | 21 | **otázky 132–136** | **nepoužívat** — rozbité kódování |
| S2/2 | ✅ **`specka2-podrobna-cast2-CITELNA.pdf`** | 21 | **otázky 132–136** | ✅ **opraveno 2026-08-10, čte se jako text** |

⚠️ **`O35` Biologická léčba není ani v jedné části.** Zůstává pokrytá jen mým `vypisky-O35-biologicka-lecba.md` z obecných znalostí.

**Mapa části 2:** O17 s.1 · O18 s.4 · O19 s.7 · O20 s.10 · O21 s.15 · O22 s.20 · O23 s.32 · O24 s.37 · O25 s.40 · O26 s.45 · O27 s.49 · O28 s.51 · O29 s.54 · O30 s.58 · O31 s.61 · O32 s.63 · O33 s.69 · O34 s.71

*(Část 2 hlásí při otevírání `MuPDF error: cannot find object in xref` — je to neškodné, text se načte správně. Stačí potlačit stderr.)*

## ✅ Část 1 — rozbité kódování je OPRAVENÉ (2026-08-10)

**Původní `cast1.pdf` vracelo při extrakci nesmysly** (`%,G'H<D:3*7L` místo `Zdravotnický`). Nešlo o sken ani o šifru: **12 vložených fontů mělo prázdnou tabulku ToUnicode**, takže se místo znaků vypisovala čísla glyfů.

**Opraveno skriptem `nastroje/oprav_pdf_fonty.py`** — přečte skutečné přiřazení z tabulky `cmap` vloženého fontu a dopíše správnou ToUnicode zpět do PDF. Výsledek: **`Inputs/obecka-podrobna-cast1-CITELNA.pdf`**, plně čitelný jako text.

```bash
python3 nastroje/oprav_pdf_fonty.py vstup.pdf vystup.pdf
```

⚠️ **Vždy používej `-CITELNA` verzi.** Původní soubor je ponechaný jako záloha, ale číst se z něj nedá.
⚠️ Renderování stránek do obrázku už **není potřeba** — bylo to jen obcházení téhle chyby.

**Mapa části 1 — kompletní, ověřená podle nadpisů:**

| Otázka | Strany | | Otázka | Strany |
|---|---|---|---|---|
| **O1** | 1–6 | | **O9** | 53–55 |
| **O2** | 7–12 | | **O10** | 56–59 |
| **O3** | 13–18 | | **O11** | 60–67 |
| **O4** | 19–24 | | **O12** | 68–70 |
| **O5** | 25–31 | | **O13** | 71–76 |
| **O6** | 32–38 | | **O14** | 77–85 |
| **O7** | 39–47 | | **O15** | 86–93 |
| **O8** | 48–52 | | **O16** | 94–100 |

*(Dřívější poznámka „část 1 pokrývá zhruba O1–O13, zbytek Tessa pošle" byla omyl — část 1 pokrývá O1–O16 celé.)*

## Zjištěné chyby ve vypracovaných otázkách

| Kde | Ve zdroji | Správně |
|---|---|---|
| O1 | oficiální, obsolentní | **oficinální, obsoletní** — ⚠️ **stejný překlep má i podrobná Obecka**, tedy zdroj katedry; u zkoušky mluv správně, ale zkoušejícího neopravuj |
| O1 | farmakoviligance, fototerapie, Karetonoidy, Aprotonin, Cefataxim, Adalizumab | farmakovigilance, **fytoterapie**, karotenoidy, aprotinin, cefotaxim, adalimumab |
| O1 × O33 | dělitel u *dosis pro infantibus*: **1,73** (část 1) × **1,7** (část 2) | **1,73 m²** — průměrná plocha těla dospělého |
| O12 | „nepřekročiténé maximum" | **nepřekročitelné** |
| O19 | text o neindukovatelných enzymech je pod nadpisem „benzpyrenový typ indukce" | benzpyrenový typ indukuje **CYP1A1/1A2** |
| O20 | Aportův syndrom | **Alportův syndrom** |
| O22 | tabulka jaderných receptorů má **ligandy posunuté o řádek** (GR–steroidní hormony, MR–kortizol, AR–aldosteron…) | GR–kortizol, MR–aldosteron, AR–testosteron, PR–progesteron, ER–estradiol |
| O22 | „adrenogenní receptor" | **androgenní receptor (AR)** |
| O14–O16 | propanolol, warfatin, fentoyn, tobutamid, prokaindamid, acetsalycilová, sulfondamidy, beriéry | propranolol, warfarin, fenytoin, tolbutamid, prokainamid, acetylsalicylová, sulfonamidy, bariéry |
| S1-52 | tetracykliny = „inhibice syntézy buněčné stěny" | **inhibice proteosyntézy (30S)** |

## Chybějící obsah ve vypracovaných otázkách

| Otázka | Co chybí | Stav |
|---|---|---|
| O1 | původ a zdroje léčiv | doplněno `[+]`, **v podrobné Obecce je — ověřit** |
| O5 | způsoby aplikace (má tam jiné téma) | doplněno `[+]`, **ověřit proti podrobné** |
| O9 | adherence, komunikace, placebo, nocebo | ✅ **přepsáno podle podrobné Obecky** |
| O12 | saturační kinetika (nadpis bez textu) | doplněno `[+]`, **ověřit** |
| O14 | redistribuce | doplněno `[+]`, **ověřit** |
| O35 | celá otázka (biologická léčba) | `vypisky-O35`, **ověřit** |
| S1-53 | celá otázka (makrolidy) | `vypisky-S1-53`, ověřit až dorazí Specka |

## Opravená chyba v mém výkladu

**O9 — compliance vs. adherence.** Napsal jsem, že compliance, adherence a konkordance jsou tři různé úrovně. **Podrobná Obecka říká, že compliance a adherence jsou pojmy rovnocenné**, adherence jen víc zdůrazňuje podíl zodpovědnosti pacienta; konkordanci vůbec nezmiňuje. Přepsáno podle materiálu. *(2026-08-08)*
