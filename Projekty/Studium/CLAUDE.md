# Studium — zubní lékařství, LF UK Plzeň

Druhá vrstva pravidel. **Doplňuje** master `CLAUDE.md` v kořeni, nepřebíjí ho. Přečti to na začátku každé práce na škole.

---

## Kontext

- Obor: **Zubní lékařství**, Lékařská fakulta Univerzity Karlovy v Plzni
- Fáze: **preklinika (1.–2. ročník)** — velké objemy faktografie, hodně memorování, latina, základ pro klinické ročníky
- Aktuální ročník a zapsané předměty: viz `KB.md`

---

## ⚠️ Faktická přesnost — platí tu nejtvrději

Master pravidlo z kořenového `CLAUDE.md` tady platí bez výjimky. Zopakuju to nejdůležitější:

- **Nevymýšlej.** „Nevím" je vždycky správná odpověď.
- **Materiály od Tessy mají přednost před tvou pamětí.** Zkouší ji konkrétní katedra podle konkrétních skript. Rozpor pojmenuj nahlas, nepřepisuj potichu.
- **Latina, čísla, klasifikace = nejvyšší laťka.** Když si nejsi 100% jistá → `[⚠️ ověřit]`.
- **Žádná klinická doporučení pro reálné pacienty.** Modelový případ u zkoušky ano, živý člověk ne.

---

## Struktura

```
Projekty/Studium/
├── CLAUDE.md          ← jsi tady
├── KB.md              ← ročník, předměty, termíny, jak která katedra zkouší
├── LOG.md             ← rozhodnutí, výsledky, co u zkoušek fungovalo
├── Inputs/            ← skripta, PDF, fotky tabule, zadání (syrové, nezpracované)
├── Process/           ← rozpracované — plány, checkpointy, discovery
├── Outputs/           ← hotové — taháky, souhrny, dokumenty
├── Feedback/          ← jak to dopadlo — výsledky, co se ptali, co nesedělo
└── Predmety/
    └── <Predmet>/
        ├── okruhy.md          ← oficiální seznam okruhů + stav (▢ / ◩ / ☑)
        ├── vypisky-<tema>.md  ← zpracovaná látka ze zdroje
        ├── slaba-mista.md     ← co nešlo při zkoušení (motor opakování)
        ├── plan-<datum>.md    ← plán učení na konkrétní termín
        └── Inputs/            ← materiály jen k tomuhle předmětu
```

**Nová složka předmětu:** vytvoř ji sama, když je poprvé potřeba — neptej se. Použij název podle sylabu, bez diakritiky a mezer (`Histologie-a-embryologie`).

---

## Pracovní postup

| Situace | Skill |
|---|---|
| Mám skripta / přednášku / fotky a chci učební materiál | `/vypisky` |
| Chci se vyzkoušet | `/zkousej-me` |
| Blíží se termín, potřebuju rozvrh | `/plan-uceni` |
| Dlouhá práce, hrozí ztráta kontextu | `/checkpoint` |
| Konec práce, něco se zjistilo | `/session-close` |

**Nabízej `/zkousej-me` proaktivně** hned po dokončení výpisků — jednou větou, ne přemlouváním. Čerstvě zpracovaná látka je nejlepší moment na první aktivní vybavení.

---

## Sledování okruhů

Každý předmět má `okruhy.md` — seznam oficiálních zkouškových okruhů se stavem:

```
# Okruhy — <Předmět>
Zdroj: <odkud seznam je> · Zkouška: <RRRR-MM-DD> · Forma: <ústní/písemná>

| # | Okruh | Stav | Výpisky | Zkoušeno | Pozn. |
|---|---|---|---|---|---|
| 1 | <název> | ☑ | vypisky-x.md | 2× ✅ | |
| 2 | <název> | ◩ | vypisky-y.md | 1× ⚠️ | chybí detail Z |
| 3 | <název> | ▢ | — | — | |
```

**Stavy:** `▢` neviděno · `◩` rozpracováno · `☑` umím (= prošlo 2× ✅ ve `/zkousej-me`, ne „přečetla jsem to")

⚠️ **Okruh se nesmí označit `☑` na základě přečtení.** Jen na základě dvou úspěšných aktivních vybavení. Tohle je celý smysl toho sloupce — jinak je to seznam přání, ne stav znalostí.

**Stav aktualizuj sama** po každém `/vypisky` a `/zkousej-me`, bez ptaní.

---

## Předměty preklinické části *(odhad — nech Tessu opravit podle sylabu)*

Tenhle seznam jsem **odhadl**, ne ověřil proti sylabu LF UK Plzeň. Až Tessa řekne, jak se předměty jmenují doopravdy, přepiš to tady a v `KB.md`.

- Anatomie
- Histologie a embryologie
- Biologie
- Lékařská biofyzika
- Biochemie
- Fyziologie
- Preklinické zubní lékařství
- Latinská terminologie
- První pomoc

---

## Po každé zkoušce — POVINNĚ

Tohle je nejcennější data, která ekosystém sbírá. Po každé zkoušce (ať dopadla jakkoli) zapiš do `LOG.md` a do `Feedback/`:

- **Na co se skutečně ptali** — konkrétní otázky, ne témata
- **Co zkoušející chtěl slyšet** a čemu naopak nevěnoval čas
- **Co z přípravy fungovalo a co byla ztráta času**
- **Kde byla díra**, kterou příprava neodhalila

Po třech zkouškách z toho bude vidět vzorec a plány učení se podle něj dají stavět mnohem přesněji. Nabídni tenhle zápis sama, hned jak se o výsledku dozvíš.
