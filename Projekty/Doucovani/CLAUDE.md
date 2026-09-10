# Doučování — kontext projektu

Tessa doučuje. Tenhle projekt drží přípravy na hodiny, materiály a zpětnou vazbu.

## Studenti

| Student | Předmět | Ročník | Formát | Frekvence |
|---|---|---|---|---|
| **Rozárka** | angličtina | 5. třída ZŠ | online, Google Meet, sdílená obrazovka | 1× týdně, 30 minut |

## ⚠️ Tessina angličtina

**Tessa není v angličtině pokročilá.** Neví spolehlivě, jak co říct a jak to vyslovit. Z toho plyne:

- **Ke každé hodině patří tahák pro učitele** s frázemi, které bude potřebovat, a **s výslovností** — zjednodušený český přepis v hranatých závorkách, VELKÁ PÍSMENA = přízvuk.
- **Nikdy jí nedávej anglickou frázi bez výslovnosti.** Bez ní ji buď nepoužije, nebo ji vysloví špatně a Rozárka se to tak naučí.
- **Nepředpokládej, že si frázi domyslí.** Co má říct, musí být napsané doslova — včetně pochval, oprav a přechodů mezi aktivitami.
- **Piš jí i to, co dělat, když neví.** Legitimní odpověď je „řekni to česky" — u páté třídy je to normální a lepší než hádat.
- **Přepis výslovnosti označuj jako přibližný.** Čeština nemá *th*, *w* ani nepřízvučné samohlásky. Neslibuj přesnost, kterou český přepis nemůže mít.

## Jak vypadá hodina s Rozárkou

- **30 minut, online.** Tessa sdílí obrazovku a promítá jí soubor — příprava proto musí být **vizuální a klikací**, ne text ke čtení.
- **Úroveň:** průměr páté třídy (≈ A1). Zvládne jednoduché věty, přítomný čas, základní slovní zásobu (rodina, škola, jídlo, zvířata). Minulý čas jen jako naučené fráze.
- **Formát přípravy: PDF pro GoodNotes.** Tessa ho otevře v GoodNotes a sdílí okno — Rozárka do něj **píše perem**. Každá aktivita proto musí mít linku, rámeček nebo něco k zakroužkování.
- **Vyrábí se z HTML přes headless Chromium** (postup: `nastroje/html-na-pdf.md`). Zdrojové HTML i PDF commitni do `Outputs/Rozarka/`.
- **Formát: A4 na šířku, velké písmo** (otázky ≥ 20 pt) — čte se to přes videohovor na malé obrazovce.
- **Struktura 30 minut:** 6 bloků po 3–6 minutách. Vždy začít rozmluvením, skončit úkolem a rozloučením. Uprostřed musí být aspoň jedna hra.
- **Motivace:** hvězdičkové počítadlo na stránce. Sbírá hvězdy za splněné úkoly.

## Pravidla pro přípravy

- **Ne prezentace, ale nástroj.** Každý blok má na obrazovce něco, na co se dá kliknout — karta, tlačítko, generátor.
- **V listu není ani slovo pro učitele.** Žádné „Rozárka odpoví…", žádné české pokyny pro Tessu, žádné odpovědi. Rozárka to celé vidí. Instrukce v listu jsou anglicky a **oslovují ji** („Circle one word from each box").
- **Scénář a klíč jsou vždy samostatný markdown**, který se nesdílí.
- **Anglická slovíčka a fráze kontroluj.** Chybné slovíčko se dítě naučí jako správné. Když si nejsi jistá vazbou, ověř nebo ji nepoužij.
- **Časovač je pomůcka, ne diktát.** Když blok baví, ať běží; obětuj vždycky prostřední aktivitu, ne závěr.

## ⚠️ Gotchas — z reálných chyb

- **⚠️ Generátor vět musí projít VŠECHNY kombinace, ne jen ukázkovou.** Když stavíš cvičení ze sloupců („vyber si z každého boxu"), projdi součin všech voleb a ověř, že každá věta dává smysl. *(2026-09-10: strana 4 měla `can` a `have got` v jednom boxu s podstatnými jmény ve druhém → vznikaly nesmysly „I can football", „I have got swimming". Opraveno na `like / don't like` + 3. osoba, kde funguje každá kombinace.)*
- **⚠️ Řešení patří k listu od začátku, ne až na vyžádání.** Tessa potřebuje vědět nejen co říct, ale i co je správná odpověď — u každého cvičení. Vyrob klíč rovnou.
- **⚠️ Při generování HTML skriptem zkontroluj, že vznikl uzavřený `</style>`.** Bez něj se celý dokument vykreslí jako CSS a PDF vyjde prázdné — a to na náhledu vypadá jako „bílá stránka", ne jako chyba. *(2026-09-10)*

## Kam co

- `Outputs/Rozarka/` — hotové hodiny:
  - `…nazev.pdf` — pracovní list, tohle se promítá
  - `…nazev-ZDROJ.html` — z toho se PDF vyrábí
  - `…TAHAK-pro-ucitele.pdf` — fráze s výslovností pro Tessu, **nesdílet**
  - `…scenar-pro-ucitele.md` — časování a klíč k odpovědím, **nesdílet**
- `Process/` — rozpracované nápady, banky aktivit
- `Feedback/Rozarka/` — jak hodina dopadla, co nefungovalo, co umí a co ne
- `Inputs/` — co dodá rodič nebo škola (učebnice, zadání od učitelky)
- `nastroje/` — technické postupy (výroba PDF)
- `LOG.md` — jedna řádka na hodinu
