---
name: plan-uceni
description: Plán učení na zkoušku — použij, když Tessa řekne "naplánuj mi učení", "kdy se mám co učit", "mám zkoušku za X dní", "rozvrhni mi to", "stíhám to?", "nevím, kde začít", "zbývá mi týden", nebo napíše "/plan-uceni". Počítá pozpátku od termínu, rozdělí okruhy do dnů, zabuduje opakování v rozestupech a řekne UPŘÍMNĚ, jestli se to dá stihnout. Taky se používá pro průběžnou revizi rozjetého plánu. NENÍ to zkoušení (/zkousej-me) ani výroba materiálů (/vypisky).
argument-hint: "[předmět + termín zkoušky]"
---

# Plán učení — pozpátku od termínu, s opakováním

## Princip

Plán, který jen rozseká látku na dny, nefunguje — látka nastudovaná první den je do zkoušky zapomenutá. Každé téma proto dostane **první průchod + naplánovaná opakování v rostoucích rozestupech** (+1 den, +3 dny, +7 dní). Opakování je součást plánu, ne něco, co se udělá „když zbyde čas". Zbyde vždycky málo.

Druhý princip: **plán, který nesedí do reálného dne, je horší než žádný**, protože se rozpadne třetí den a vezme s sebou motivaci. Radši méně témat pořádně než všechna na oko.

---

## Setup — jedna dávka otázek, pak už jedeš

Zjisti dnešní datum (`date +%F`) a **v jedné zprávě** se zeptej na to, co si nemůžeš odvodit z vaultu:

1. **Termín zkoušky** (a jestli je opravný termín, kdy)
2. **Kolik hodin denně reálně** — ne kolik by chtěla, kolik se opravdu stane. Zeptej se na pracovní dny a víkend zvlášť.
3. **Co už je hotové** — které okruhy má nastudované, co má výpisky, co ještě neviděla
4. **Forma zkoušky** — ústní / písemná / test / praktická. Mění to úplně způsob přípravy.

Zdroje ve vaultu prohledej **napřed**, ať se neptáš na to, co už tam je:
- `Projekty/Studium/Predmety/<Predmet>/okruhy.md` — seznam okruhů
- `Projekty/Studium/Predmety/<Predmet>/slaba-mista.md` — kde jsou díry
- `Projekty/Studium/Predmety/<Predmet>/vypisky-*.md` — co je zpracované
- `Projekty/Studium/LOG.md` — jak dopadly minulé zkoušky

---

## KROK 1 — Reality check PŘED plánem (nepřeskakovat)

Spočítej: **počet okruhů × odhad hodin na okruh** vs. **dostupné hodiny do termínu**.

Pak řekni výsledek **upřímně a jako první věc**, ne schovaný na konci:

- **Vejde se to** → *„Máš 14 dní a 40 okruhů, 3 h denně. Vejde se to s rezervou 2 dny."*
- **Je to těsné** → *„Vejde se to, ale bez jediného výpadku. Když vypadneš dva dny, plán padá — tady je, co se v tom případě vyhodí jako první."*
- **Nevejde** → **řekni to rovnou a navrhni triáž.** *„40 okruhů za 6 dní při 3 h denně nejde — to je 45 minut na okruh včetně opakování. Buď posuneme termín, nebo jdeme na triáž: tyhle okruhy pořádně, tyhle jen kostru, tyhle vědomě obětujeme."*

**Nikdy nevyrob optimistický plán, o kterém víš, že nesedí.** Falešný plán je horší než pravda, protože ji připraví o možnost rozhodnout se jinak (posunout termín, obětovat okruh vědomě). Tohle je přesně ta situace, kde se nepřitakává.

---

## KROK 2 — Triáž okruhů (když se nevejde, nebo je to těsné)

Rozděl okruhy do tří kategorií a **řekni, podle čeho jsi to rozdělila**:

| Priorita | Co tam patří |
|---|---|
| **A — pořádně** | Velké nosné okruhy · to, co je v `slaba-mista.md` · co podle `LOG.md` katedra zkouší často · co je základ pro další předměty |
| **B — kostra** | Umět zarámovat a říct hlavní body, bez detailů |
| **C — vědomě obětované** | Vzácné, okrajové, nízká váha. **Pojmenuj je nahlas** — obětovat vědomě je strategie, obětovat nevědomě je nehoda. |

Když nemáš data o tom, na co se katedra ptá, **řekni to** a triážuj podle rozsahu a návaznosti, ne podle dojmu.

---

## KROK 3 — Rozvrh pozpátku od termínu

- **Poslední den před zkouškou = jen opakování a tahák.** Žádná nová látka. Nikdy.
- **Předposlední den = průchod slabými místy**, ne celou látkou.
- Zbytek dní zpět: nová látka **dopoledne v plánu** (ve výkonnějším čase), opakování starší látky navrch.
- **Každé téma dostane 3 dotyky:** první průchod → +1 den → +3 dny → +7 dní (co se vejde do zbývajícího času).
- **Zabuduj jeden volný den** jako polštář na výpadek. Když ho nepotřebuje, je to opakování navíc. Bez polštáře plán nepřežije první nemoc nebo praktikum navíc.
- **Nepřeplňuj dny na 100 %.** Plánuj na ~80 % dostupného času.
- Denní blok = **max 90 minut na jedno téma**, pak přestávka nebo změna předmětu.

---

## KROK 4 — Ulož jako odškrtávací seznam

`Projekty/Studium/Predmety/<Predmet>/plan-<RRRR-MM-DD-zkousky>.md`

Formát, který se dá odškrtávat na mobilu:

```
# Plán učení — <Předmět> — zkouška <RRRR-MM-DD>
Vytvořeno: <datum> · Zbývá dní: <N> · Hodin denně: <N> · Forma: <ústní/písemná>

## Verdikt
<vejde se / těsné / nevejde — jednou větou, upřímně>

## Triáž
- **A (pořádně):** <okruhy>
- **B (kostra):** <okruhy>
- **C (obětováno):** <okruhy>

## Rozvrh
### <Den, RRRR-MM-DD> — <N h>
- [ ] NOVÉ: okruh <X> — <téma> (<N> min)
- [ ] OPAKOVÁNÍ +1: okruh <Y>
- [ ] OPAKOVÁNÍ +3: okruh <Z>

### <Den, RRRR-MM-DD> — VOLNÝ POLŠTÁŘ
- [ ] rezerva na skluz, nebo opakování navíc

### <den před zkouškou>
- [ ] Jen tahák + slabá místa. Žádná nová látka.

## Když nastane skluz
<co se vyhodí jako první, konkrétně — rozhodnuté dopředu, ne v panice>
```

---

## KROK 5 — Commit a push, bez ptaní

```
git add -A && git commit -m "plán učení: <předmět> — zkouška <datum>" && git push -u origin <branch>
```

Plán musí být na mobilu, jinak se podle něj nedá jet.

---

## Revize rozjetého plánu

Když Tessa přijde s tím, že je ve skluzu (a přijde — plány kloužou vždycky):

1. **Žádné výčitky, žádné „to se dalo čekat".** Přepočítej.
2. Zjisti reálný stav: co je opravdu hotové, ne co mělo být.
3. **Přepiš plán od dneška**, neposouvej původní. Původní nech v souboru pod čarou jako historii.
4. Když skluz překročil polštář → **znovu triáž**, něco musí ven. Řekni co a proč.
5. Zapiš do `Projekty/Studium/LOG.md` jednu větu, **proč** skluz nastal — po třetí zkoušce z toho bude vidět vzorec (přeceňuje hodiny? podceňuje okruhy? vypadává na praktikách?), a ten se dá zaplánovat dopředu.

---

## Kdy NE

- „Kolik toho ještě mám?" → odpověz přímo z `okruhy.md`, žádný plán.
- Chce se vyzkoušet → `/zkousej-me`.
- Chce zpracovat materiál → `/vypisky`.
