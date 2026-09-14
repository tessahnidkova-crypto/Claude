# Tetování Blíženci — máma & dcera

Návrh párového tetování. Souhvězdí Blíženců (Gemini) jako čárová kresba, do níž jsou
nenásilně zakomponované obě děti — **Kačka** a **Ondra**.

---

## Proč zrovna Blíženci takhle

Souhvězdí netvoří jedna postava, ale **dvě, které se drží** — Castor a Pollux,
v řecké mytologii dvojčata Kastór a Polydeukés. Pollux byl nesmrtelný, Castor ne;
Pollux se vzdal poloviny své nesmrtelnosti, aby nemuseli být rozdělení, a proto
jsou spolu na obloze. *[obecné znalosti — mytologie, běžně uváděná verze]*

Pro tetování mámy a dcery, které jsou obě Blíženci, to sedí dvakrát: je to jejich
znamení **a zároveň** dvě postavy stojící vedle sebe.

## Kde jsou v tom děti

| Prvek | Co znamená | Ve variantách |
|---|---|---|
| Oblouk nad hlavami | **K** v morseovce (`—·—`) = Kačka | A, D |
| Oblouk pod nohama | **O** v morseovce (`———`) = Ondra | A, D |
| Rozvitý květ / poupě | Kačka / Ondra | B |
| Dvě zářící hvězdy uvnitř obou postav | dvě děti | C, D |

**Proč morseovka:** tečky a čárky splynou s tečkovanou linií souhvězdí. Zvenku to
vypadá jen jako ozdobná křivka — jména tam čtou jen ony. Žádné písmeno, žádný nápis.

## Varianty

- **A · POUTO** — čisté souhvězdí, K nahoře, O dole. Nejvíc minimalistické.
- **B · DVĚ KVĚTINY** — jeden stonek se rozdvojuje: rozvitý květ (Kačka) a poupě (Ondra).
  Nejblíž k té inspiraci s pomněnkami.
- **C · DVĚ HVĚZDY** — děti jen jako dvě zvýrazněné hvězdy uvnitř obou postav. Nejtišší.
- **D · KOMBINACE** — morseovka + dvě hvězdy + jedna větvička. **Doporučeno** — má všechny
  tři vrstvy významu a pořád je vzdušné.

## Soubory

| Soubor | K čemu |
|---|---|
| `varianty.png` / `.svg` | přehled všech čtyř variant |
| `detail-D.png` / `.svg` | doporučená varianta ve velkém + vysvětlivky + náhled na kůži |
| `stencil-A/B/C/D.svg` | **pro tatéra** — čistá čerň na bílé, bez popisků, vektor |
| `stencil-D-zrcadlove.svg` | zrcadlová verze (viz níže) |
| `generator.py`, `varianty.py`, `stencil.py`, `render.sh` | zdroj, ze kterého se to dá přegenerovat |

SVG je vektor — dá se zvětšit na jakoukoli velikost bez ztráty kvality. Tatérovi posílej
**SVG, ne PNG**.

## Pro tatéra — praktické poznámky

- **Velikost:** návrh počítá s cca **9–12 cm na výšku**. Míň ne — morseovka i tečky by
  se po letech slily. Fine-line na lopatce drží dobře.
- **Tloušťka linky:** nejtenčí možná, kterou tatér umí udržet čitelnou po 5+ letech.
  Vzdálenosti mezi tečkami raději zvětšit než zmenšit.
- **Kritické místo:** tečka uprostřed morseovky K (`—·—`) musí zůstat viditelně menší
  než hvězdy a viditelně oddělená od čárek. Když splyne, přečte se to jako `—`, ne jako K.
- **Zrcadlová verze:** kdyby chtěly tetování na protilehlé straně, aby si vedle sebe
  "hleděly", je připravená v `stencil-D-zrcadlove.svg`. ⚠️ Zrcadlené souhvězdí už
  neodpovídá skutečné obloze — je to čistě estetické rozhodnutí.

## Co je potřeba ověřit / rozhodnout

- **Pozice hvězd** jsou podle RA/Dec (J2000) z mé paměti. Tvar souhvězdí sedí,
  ale `[⚠️ ověřit]` — kdyby chtěly astronomicky přesnou repliku, nechat zkontrolovat
  ve Stellariu (zdarma, stellarium-web.org).
- **Souhvězdí je natočené na výšku**, aby postavy "stály" — na skutečné obloze leží
  šikmo. Běžná tatérská stylizace; v `generator.py` jde vypnout (`rot=0`).
- **Spojnice mezi hvězdami** jsou stylizace, ne jediná správná verze — různé atlasy
  kreslí figuru Blíženců mírně jinak.
- **Kolik toho tam má být?** Čím míň prvků, tím líp to zestárne. Když váháš mezi
  D a C, ber C.

## Nápady na rozšíření, kdyby chtěly víc

- **Datum narození dětí** místo/vedle morseovky — jako počet teček v jedné spojnici.
- **Dvě různé květiny** podle měsíce narození každého dítěte.
- **Rozdělení na dvě:** máma má souhvězdí s K, dcera s O — dohromady dávají celek.
  Silné, ale každá pak má jen půlku; ptát se, jestli to chtějí.
