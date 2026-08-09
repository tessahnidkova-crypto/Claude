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

## ⚠️ Podrobná Obecka má rozbité kódování fontu

Extrakce textu vrací nesmysly (`H*3:7G^8.*3H<`). **Musí se číst jako obrázek** — vyrenderovat stránku přes pymupdf a přečíst. Text z ní nikdy nekopíruj přímo.

```python
import pymupdf
d = pymupdf.open('Inputs/obecka-podrobna-cast1.pdf')
d[52].get_pixmap(matrix=pymupdf.Matrix(2.0, 2.0)).save('p53.png')
```

Část 1 má **100 stran** a pokrývá zhruba otázky **O1–O13**. Zbytek Tessa pošle.

**Mapa nalezených nadpisů:** O6 s.32 · O7 s.39 · O8 s.48 · O9 s.53 · O11 s.60 · O12 s.68 · O13 s.71

## Zjištěné chyby ve vypracovaných otázkách

| Kde | Ve zdroji | Správně |
|---|---|---|
| O1 | oficiální, obsolentní | **oficinální, obsoletní** |
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
