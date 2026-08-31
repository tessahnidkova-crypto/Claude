# LOG — Studium

Append-only log rozhodnutí a oprav. **Nejnovější nahoře.** Jeden řádek na záznam:
`RRRR-MM-DD — co se rozhodlo/opravilo — proč`

Zapisuje se přes `/session-close`. Živý rozpracovaný stav sem NEPATŘÍ — ten je v `Process/checkpoint-*.md`.

## 2026

- 2026-08-08 — Farmakologie: rozsah zjištěn z oficiálního seznamu — 136 okruhů (35 obecná / 53 spec. I / 48 spec. II), zahrnuje i Farmakologii I
- 2026-08-08 — Farmakologie: z podmínek předmětu zjištěno, že test (50 ot., nutno 35) je na 1. termínu tvrdá brána — při neúspěchu propadá termín a je 4, bez ústní části
- 2026-08-08 — OPRAVA plánu: původní pravidlo „při skluzu škrtej šířku" je s testovou branou obráceně — šířka je nepodkročitelná, flexuje hloubka
- 2026-08-08 — Termín farmakologie potvrzen na 1. 9. 2026 (24 dní) → postaven plán učení ve 4 fázích
- 2026-08-08 — Rozhodnuto: nastoupit i na VL jako nástroj — složit farmakologii, patofyziologii a patologii, nechat uznat do 3. ročníku ZL, pak VL ukončit
- 2026-08-08 — Upřesněno: zkouška, kvůli které skončilo VL, byla patofyziologie (ne farmakologie) — určuje prioritu přípravy v zimě
- 2026-08-08 — Zpracován oficiální studijní plán ZL do `studijni-plan.md`, zdroj uložen do `Inputs/` — nahrazuje odhady tvrdými daty
- 2026-08-08 — Zjištěno: biofyzika je LETNÍ předmět a preklinika I nemá zkoušku → v 1. ročníku je jediná zkouška, a to v červnu 2027
- 2026-08-08 — Zjištěno: biofyzika Zk + preklinika I Z jsou prerekvizity Preklinického ZL II → lehký ročník, ale dva úzké krčky
- 2026-08-08 — Zjištěno: farmakologie je na ZL dvousemestrální předmět 3. ročníku → zářijové uznání musí potvrdit studijní oddělení
- 2026-08-08 — Zapsán studijní kontext: nástup do 1. ročníku ZL po ukončeném VL (2 hotové ročníky + psychologie ve 3.) — určuje, co se uznává a co zbývá splnit
- 2026-08-08 — Identifikován nejbližší termín: farmakologie, září 2026 — nejvyšší priorita, datum zatím chybí
- 2026-08-08 — Projekt založen při stavbě vaultu — viz kořenový README.md
2026-08-29 — Farmakologie: dodelan VYCUC-FINAL (89 str., vsech 136 otazek: zacatek odpovedi, kostra, sketch, doptavaci otazky). README aktualizovano jako primarni soubor na posledni dny.
2026-08-31 — Farmakologie: OBRAZKY-VSE (46 str., 136 kreslenych schemat, 1 na otazku). Novy nastroj nastroje/schemata.py + gen_obrazky.py; md2gdoc umi inline SVG.
2026-08-31 — Farmakologie: SKETCHNOTES (136 stran, 1 kreslena strana na otazku, cela otazka vcetne deleni, NU, pasti, zubarskeho presahu a mnemotechniky). Novy nastroj nastroje/sketch.py (rucne kresleny styl: jitterovane tahy, zvyraznovac) + gen_sketch.py.
2026-08-31 — Farmakologie: mluvena verze slouceena po castech — SPECKA1-mluvena.pdf (36-88, 69 str.) a SPECKA2-mluvena.pdf (89-136, 83 str.), obe se zalozkami.
2026-08-31 — Farmakologie: TAHACKY.pdf — kapesni karticky, 136 karet (95x68 mm), 8 na list A4, 17 listu. Obsah se automaticky zhustuje ze sketchnot (nastroje/gen_tahaky.py); S() ve farmakologie_sketch.py nove uklada i strukturovana data (DATA).
2026-08-31 — Farmakologie: TAHACKY zmenseny na 12 karet na A4 (66x71 mm, 12 listu). Do generatoru pridan rozpocet radku a min-height:0 v mrizce — bez toho radek rostl podle obsahu a text pretekal na dalsi stranu.
2026-08-31 — Farmakologie: TAHACKY prepsany do odborneho registru — bez zubniho presahu, mnemotechniky a piktogramu; jen fakta (az 11 bodu na kartu). Generator ma filtry DENTALNI/META a cisteni piktogramu.
2026-08-31 — Farmakologie: TAHACKY prepsany — kazda karta ma ZACATEK (dve vety z VYCUC-FINAL), KOSTRU a ZAKLAD, plni se az do kraje. Generator cte VYCUC-FINAL.md, filtruje zubni presah i z kostry a nikdy neutina text uprostred mysleny.
