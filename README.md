# Tessin Claude vault

Jedno místo pro všechno, co s Claudem děláš — studium zubního lékařství i osobní věci. Postaveno 2026-08-08 podle AIOS Starter Kitu, upraveno na studium.

---

## Jak funguje sync mezi tabletem a mobilem

**Mechanismus:** vault = tenhle GitHub repozitář. Když otevřeš Clauda nad tímhle repem na jakémkoli zařízení, dostane stejné soubory a stejná pravidla. Tablet a mobil se nesynchronizují spolu — oba se synchronizují s GitHubem.

```
   tablet ──┐                    ┌── mobil
            ├──► GitHub repo ◄───┤
            │   (zdroj pravdy)   │
```

**Z toho plynou tři věci, které si musíš zapamatovat:**

1. **Co není pushnuté, na druhém zařízení neexistuje.** Claude má v pravidlech, že má commitovat a pushovat sám po každé hotové věci. Když si nejsi jistá, prostě napiš *„pushni to"*.
2. **Historie chatu se nesynchronizuje. Soubory ano.** Konverzace z tabletu na mobilu neuvidíš. Proto všechno důležité končí v souboru — to je celý smysl `/checkpoint` a `/session-close`.
3. **Než začneš na druhém zařízení, řekni Claudovi „načti si, kde jsme skončily".** Přečte si poslední checkpoint nebo handoff a naváže.

**Co ještě musíš udělat ty (já to za tebe udělat nemůžu):** na mobilu otevři Clauda a připoj tenhle repozitář (`tessahnidkova-crypto/Claude`) stejně, jako je připojený tady na tabletu. Pak už je to automatické.

---

## Co tu je

```
/
├── CLAUDE.md          ← mistr pravidel. Claude to čte automaticky vždy.
├── MEMORY.md          ← trvalé fakty (kdo jsi, ročník, termíny)
├── ARCHIVE.md         ← co zastaralo, ale nemažeme
├── README.md          ← jsi tady
├── .claude/skills/    ← 6 aktivních skillů
└── Projekty/
    ├── Studium/       ← škola: předměty, okruhy, výpisky, zkoušky
    ├── Osobni/        ← úkoly, termíny, plánování času
    ├── Finance/       ← rozpočet, úřady, formuláře
    ├── Psani/         ← e-maily, žádosti, dopisy
    └── Zdravi/        ← trénink, režim, koníčky
```

Každý projekt má stejnou kostru: `CLAUDE.md` (kontext) · `KB.md` (detaily) · `LOG.md` (rozhodnutí) · `Inputs/` `Process/` `Outputs/` `Feedback/`.

---

## Skilly — co umí

**Nemusíš je psát.** Claude popisy všech skillů vidí automaticky a sám pozná, kdy který použít. Lomítko je jen zkratka, když chceš přinutit konkrétní postup.

| Skill | Co dělá | Řekni prostě |
|---|---|---|
| `/zkousej-me` | Zkouší tě otázku po otázce, nenapoví předem, zapisuje, co ti nešlo | *„zkoušej mě z anatomie"* |
| `/vypisky` | Ze skript / přednášky / fotek udělá učební materiál s citacemi stránek | *„zpracuj mi tuhle kapitolu"* |
| `/plan-uceni` | Rozvrhne učení pozpátku od termínu, s opakováním | *„mám zkoušku za 3 týdny"* |
| `/checkpoint` | Zmrazí rozdělanou práci do souboru, ať se neztratí | *„ulož, kde jsme"* |
| `/session-close` | Uzávěrka — zapíše, co se rozhodlo a naučilo, a pushne to | *„zavři session"* |
| `/orchestrace` | Router — poradí, jakým postupem práci vzít | *(použije se sám)* |

Neaktivní skilly z kitu leží v `Skilly-zaloha/` — nejsou načtené, ale dají se kdykoli zapnout. Viz `Skilly-zaloha/README.md`.

⚠️ **Nový nebo změněný skill se načte až v NOVÉ session.** V rozjeté konverzaci ho neuvidíš.

---

## Jak s tím reálně pracovat

**Studium — celý cyklus:**

1. Nafoť nebo nahraj skripta → *„zpracuj mi tohle"* → vzniknou výpisky s citacemi
2. *„zkoušej mě z toho"* → aktivní vybavování, slabá místa se zapíšou do souboru
3. Za pár dní: *„zkoušej mě jen ze slabin"* → opakuje se přesně to, co nešlo
4. Před zkouškou: *„mám zkoušku 15. ledna, naplánuj mi to"*
5. Po zkoušce: *„zapiš, na co se ptali"* → příští plán bude přesnější

**Jedna session = jeden job.** Nemíchej výpisky z anatomie + plánování týdne + e-mail do jedné nekonečné konverzace. Slije se to a kvalita klesne. Radši novou konverzaci.

---

## Tři pravidla, na kterých to celé stojí

**1. Systém se učí z chyb.** *Použij → klopýtne → oprav pravidlo hned → už se to nestane.* Klíčové je **hned** a **do souboru**. Oprava řečená v chatu zmizí; oprava zapsaná do `CLAUDE.md` nebo do skillu platí navždy a je i na druhém zařízení. Když ti Claude něco udělá špatně, neopravuj to jen pro tuhle jednu odpověď — řekni *„zapiš si to jako pravidlo"*.

**2. Práce cestuje jako soubory, ne jako historie chatu.** Kontext se plní, session končí, chat mizí, kontejner se smaže. Cokoli má přežít do zítřka, musí být commitnuté.

**3. Fakta se nevymýšlejí.** U studia medicíny je halucinace přímá škoda — naučíš se ji jako pravdu. Claude má v pravidlech označovat původ každého faktu (`[s. 42]` ze zdroje · `[+]` doplněno · `[⚠️ ověřit]` nejistota) a přiznat „nevím". **Když u odborného tvrzení značka chybí, zeptej se, odkud to je.**

---

## Poctivé varování

- **Prvních pár týdnů to bude působit jako režie navíc.** Návratnost přijde, až se poprvé stane, že Claude sám nezopakuje chybu z minulého měsíce, nebo že se před zkouškou vytáhne seznam přesně těch věcí, které ti dvakrát nešly.
- **`CLAUDE.md` má tendenci tloustnout.** Každé pravidlo stojí kontext v každé session. Jednou za čas ho projdi a smaž, co se neosvědčilo.
- **Sekci „Gotchas" nedopisuj dopředu.** Má růst z reálných škod, ne z fantazie o rizicích.
- **Nezaváděj další skilly hromadně.** Šest je už teď na horní hranici. Další přidej, až tenhle přestane stačit.
- **Ověřuj odborný obsah.** Ani nejlepší pravidla halucinace nevypnou úplně. U čísel, latiny a klasifikací kontroluj proti skriptům.

---

## Co ještě chybí

- [ ] Doplnit ročník, předměty a termíny do `MEMORY.md` a `Projekty/Studium/KB.md`
- [ ] Opravit seznam předmětů v `Projekty/Studium/CLAUDE.md` podle skutečného sylabu
- [ ] Připojit repozitář na mobilu
- [ ] Vyrobit `Projekty/Psani/voice-principles.md` z ~20 reálných odeslaných zpráv
