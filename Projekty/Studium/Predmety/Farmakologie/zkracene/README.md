# Zkrácené otázky — obecná farmakologie

**Všech 35 otázek hotových** · Stav k 2026-08-08

## Soubory

| Soubor | Otázky | Zdroj |
|---|---|---|
| `obecna-O1-O5.md` | O1–O5 | vypracované; **O5 přepsána z podrobné Obecky** |
| `obecna-O6-O12.md` | O6–O12 | vypracované; **O9 přepsána z podrobné Obecky** |
| `obecna-O13-O16.md` | O13–O16 | vypracované; **O14 redistribuce ověřena** |
| `obecna-O17-O20.md` | O17–O20 | ⚠️ vypracované, **neověřeno** |
| `obecna-O21-O24.md` | O21–O24 | ⚠️ vypracované, **neověřeno** |
| `obecna-O25-O28.md` | O25–O28 | ✅ **podrobná Obecka** |
| `obecna-O29-O32.md` | O29–O32 | ✅ **podrobná Obecka** |
| `obecna-O33-O34.md` | O33–O34 | ✅ **podrobná Obecka** |
| `../vypisky-O35-biologicka-lecba.md` | O35 | ⚠️ **obecné znalosti** — v žádném materiálu není |

## Co ještě ověřit

**Priorita 1 — `O17`–`O24`.** Psané z vypracovaných otázek, které obsahují chyby.
Podrobná Obecka je má v části 2 na stranách 1–39. Postup:

```python
import pymupdf
d = pymupdf.open('../Inputs/obecka-podrobna-cast2.pdf')
print(''.join(d[i].get_text() for i in range(0, 39)))   # O17-O24
```

**Priorita 2 — `O1`–`O4`, `O6`–`O8`, `O10`–`O13`, `O15`–`O16`.**
Podrobná Obecka část 1, ⚠️ **jen jako obrázek** (rozbité kódování fontu).

**Priorita 3 — `O35`.** Sehnat oficiální zpracování, moje verze je z obecných znalostí.

## Jak je používat

Každá otázka začíná **Kostrou odpovědi** — jednou řádkou, co říct v jakém pořadí.
To je to, co u ústní části prodává pochopení. Zbytek jsou tabulky a odrážky.

Značky: `[+]` doplněno mimo materiály · `[⚠️ ověřit]` nejistota
