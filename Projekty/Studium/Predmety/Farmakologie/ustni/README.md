# Obecná farmakologie — verze na ústní zkoušku

**Všech 35 otázek · 1–1,5 strany na otázku · stav k 2026-08-10**

Tohle je **hlavní učební materiál**. Obsahuje to, co u ústní zkoušky skutečně řekneš,
aby bylo vidět pochopení — bez detailů, na kterých se vyhoří.

## ⚠️ Dvě vrstvy — nepleť si je

| Složka | K čemu | Rozsah |
|---|---|---|
| **`ustni/`** *(jsi tady)* | **ústní část** — co říct a v jakém pořadí | **1–1,5 strany** na otázku |
| `../zkracene/` | **test na počítači** — šířka a detail | 2,5 strany na otázku |

**Proč obojí:** test na počítači je **tvrdá podmínka prvního termínu** — pod 35/50 bodů
termín propadá, známka 4 a k ústní části se nejde. Na test potřebuješ šířku,
na ústní část hloubku a strukturu. Škrtat šířku by bylo riskantní.

**Postup, který dává smysl:** učit se z `ustni/`, a když si u něčeho nejsi jistá
nebo to potřebuješ do hloubky, sáhnout do `../zkracene/` na stejnou otázku.

## Rozsah po otázkách

| Soubor | Otázky | Nejdelší v souboru |
|---|---|---|
| `obecna-O1-O5.md` | O1–O5 | O2 · 1,5 |
| `obecna-O6-O12.md` | O6–O12 | O6, O7, O10 · 1,3 |
| `obecna-O13-O16.md` | O13–O16 | O14, O16 · 1,3 |
| `obecna-O17-O20.md` | O17–O20 | O17 · 1,5 |
| `obecna-O21-O24.md` | O21–O24 | O21, O22 · 1,5 |
| `obecna-O25-O28.md` | O25–O28 | O25 · 1,3 |
| `obecna-O29-O32.md` | O29–O32 | **O32 · 1,6** |
| `obecna-O33-O35.md` | O33–O35 | **O35 · 1,6** |

**Průměr 1,3 strany. Dvě otázky mírně přesahují na 1,6** — O32 (těhotenství *a* kojení jsou
fakticky dvě témata v jedné otázce) a O35 (biologická léčba). Dál už by se u nich
škrtal obsah, ne text.

## Jak jsou otázky stavěné

Každá začíná **kostrou odpovědi** — jedním řádkem, co říct a v jakém pořadí.
To je to, co u ústní části prodává pochopení; zbytek jsou tabulky a odrážky.

**⚠️** označuje past, chytačku nebo větu, kterou zkoušející chce slyšet.

## ⚠️ Jediná otázka bez opory v materiálech

**O35 Biologická léčba** není ani v podrobné Obecce, ani ve vypracovaných otázkách —
je z obecných znalostí. **Ověř si ji proti přednášce.**

## PDF

Ve složce `../pdf-ustni/` jsou tytéž soubory vytištěné, plus `USTNI-vse-v-jednom.pdf`
se záložkami. Přegenerování po úpravě markdownu:

```bash
python3 nastroje/md2pdf.py --slozka Projekty/Studium/Predmety/Farmakologie/ustni
```

⚠️ **Zdrojem je markdown, PDF je export.** Edituj `.md`, pak přegeneruj.
