# Předměty

Jedna složka na předmět. **Vytvoří se sama, když je poprvé potřeba** — Claude ji založí bez ptaní, stačí říct „chci si zpracovat histologii".

Název složky bez diakritiky a mezer, podle sylabu: `Histologie-a-embryologie`, `Anatomie`, `Biochemie`.

## Co v každé složce žije

| Soubor | K čemu | Kdo ho píše |
|---|---|---|
| `okruhy.md` | Oficiální seznam zkouškových okruhů + stav znalosti | Ty nahraješ seznam, Claude udržuje stav |
| `vypisky-<tema>.md` | Zpracovaná látka ze zdroje, s citacemi stránek | `/vypisky` |
| `slaba-mista.md` | Co nešlo při zkoušení — motor cíleného opakování | `/zkousej-me` |
| `plan-<datum>.md` | Plán učení na konkrétní termín | `/plan-uceni` |
| `Inputs/` | Skripta, PDF, fotky tabule k tomuhle předmětu | Ty |

## Stavy okruhů

`▢` neviděno · `◩` rozpracováno · `☑` **umím**

⚠️ `☑` se nedává za přečtení. Jen za **dvě úspěšná aktivní vybavení** ve `/zkousej-me`. Jinak je z toho seznam přání místo stavu znalostí — a to je přesně ta chyba, kvůli které se u zkoušky zjistí, že „přečetla jsem to" znamenalo „neumím to".

## Šablona `okruhy.md`

```
# Okruhy — <Předmět>
Zdroj: <odkud seznam je> · Zkouška: <RRRR-MM-DD> · Forma: <ústní/písemná/test>

| # | Okruh | Stav | Výpisky | Zkoušeno | Pozn. |
|---|---|---|---|---|---|
| 1 | | ▢ | — | — | |
```
