---
name: checkpoint
description: Use MID-JOB (not at the end) to freeze the current state of unfinished work into a file so nothing is lost when context fills, before ending a session, or before a risky step — triggers like "checkpoint", "ulož kde jsme", "zmraz stav", "než to zapomeneš", "shrň progres", or "/checkpoint". Also fire PROACTIVELY (no asking) every ~10–15 substantive steps of a long job or before an irreversible action. Rolling: OVERWRITES one file with the live state (cíl / hotovo / rozhodnutí / další krok) and commits it. NOT the end-of-work uzávěrka — that is /session-close.
argument-hint: "[volitelně: čeho se checkpoint týká]"
---

# Checkpoint — zmrazím stav rozdělané práce do souboru

## Co to dělá a proč

Uprostřed dlouhého jobu se plní kontext. Když si stav držím jen „v hlavě", při přerušení ztratím původní **cíl**, už padlá **rozhodnutí** a to, **kde jsem skončila**. Checkpoint = jeden krátký soubor se **ŽIVÝM stavem**, který průběžně přepisuju.

⚠️ Tady to platí ještě víc než na desktopu: **kontejner je dočasný a session může skončit bez varování.** Checkpoint musí být nejen zapsaný, ale i **commitnutý a pushnutý** — jinak se na druhém zařízení neobjeví.

## Kam — JEDEN rolling soubor (přepisuju, ne append)

- Projekt podle Routing Map → `Projekty/<Projekt>/Process/checkpoint-<slug>.md`
- Konkrétní předmět → `Projekty/Studium/Predmety/<Predmet>/checkpoint.md`
- **Přepiš celý soubor** při každém checkpointu — je to *aktuální stav*, ne log.
- ⚠️ **NE do `LOG.md`.** `LOG.md` je trvalý append-only log rozhodnutí. Do něj se rozhodnutí propíšou až na konci přes `/session-close`.

## Kdy se spouští

- Tessa řekne „checkpoint" / „ulož kde jsme" / napíše `/checkpoint`.
- **Sama proaktivně, bez ptaní** (jen jednořádkové „📍 checkpoint uložen"): každých ~10–15 netriviálních kroků dlouhého jobu, **před nevratným krokem**, nebo než navrhneš ukončení session.

## Formát (< 200 slov, terse)

Přepiš soubor přesně touhle strukturou — sekci nevynechávej, prázdnou vyplň „—":

```
# Checkpoint — <Projekt/téma> — aktualizováno <RRRR-MM-DD HH:MM>

## Cíl (zadání)
<1–2 věty — to, co se nejsnáz ztratí>

## Hotovo
- <co je udělané>

## Klíčová rozhodnutí
- <rozhodnutí> — <proč, stručně>

## Stav teď
- Soubory: <dotčené cesty od kořene repa>
- Rozpracované: <co je rozdělané a kde — nebo „—">

## Další krok
<1 věta — nejpravděpodobnější další akce>

## Otevřené / blokery
- <otázka na Tessu / co chybí — nebo „—">
```

## Po zápisu VŽDY

```
git add -A && git commit -m "checkpoint: <téma>" && git push -u origin <branch>
```

Bez pushnutí checkpoint neplní svůj účel — na druhém zařízení neexistuje.

## Resume (nová session)

Přečti checkpoint soubor **jako první**. Pak: (1) potvrď jednou větou, kde jsme, (2) pojmenuj další krok, (3) **neopakuj hotovou práci**. Teprve pak pokračuj.

## Vztah k ostatním skillům

- **Uprostřed** práce = tenhle `/checkpoint` (rolling, lehký, opakovaný).
- **Na konci** = `/session-close` (povýší trvalá rozhodnutí do `LOG.md`, udělá handoff, aktualizuje paměť).
- Checkpoint session-close **nenahrazuje** — připravuje mu půdu.
