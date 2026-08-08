---
name: automatizace-governance
description: Pravidla pro stavbu, nasazení a rušení automatizací v Josefově ekosystému — EAD filtr (Eliminate → Automate → Delegate) před stavbou, volba běhového prostředí (GitHub Actions vs. lokální launchd vs. cloud routine), **audit doručení** (jak zajistit, aby job hlásil selhání a nespadl potichu), **pravidlo sweepu** (najdeš jednu instanci chyby → prověř celou třídu), Kill Switch na mrtvé automatizace a kvartální re-audit oprávnění. Přečti PŘED tím, než postavíš jakýkoli skript, cron, workflow, launchd job nebo scheduled task, a taky když nějaká automatizace opakovaně padá, potřebuje pořád záplaty, tváří se že běží ale nedodává výstup, nebo se ptáš, jestli ji nezabít. NENÍ to o tom, jak psát kód — je to o tom, jestli a kde má daná automatizace vůbec existovat.
---

# Automatizace — governance

## 1. EAD filtr — než postavíš cokoli
Prožeň proces tímto filtrem **v tomto pořadí**. Brzdí automatizační reflex: nejdřív se ptej, pak stav.

1. **Eliminate** — „Co se stane, když to prostě přestaneme dělat?" Duplicity, reporty, co nikdo nečte, kroky bez hodnoty → zabij. **Neautomatizuj odpad.**
2. **Automate** — co přežije, automatizuj, ale málokdy na 100 %. Reálný cíl ~**60 % plně auto / 30 % AI-assisted (draft + Josefova kontrola = safe-fail) / 10 % ruční**. Kdo slibuje 100 % automatizaci čehokoli smysluplného, něco ti prodává.
3. **Delegate** — co je moc složité, proměnlivé nebo závislé na lidském úsudku, předej **člověku**, ne AI.

Nic nezůstává „jak to bylo": každý proces se zabije, zautomatizuje, nebo předá.
(Zdroj: Nate Herk „3 Ms of AI"; převzato 2026-07-04.)

## 2. Kde to má běžet

| Prostředí | Kdy |
|---|---|
| **GitHub Actions** ⭐ default | Cokoli běží na plán (cron/denně/týdně) a jde spustit ve stateless cloud runneru — operuje nad repem vaultu, veřejnými daty nebo přes API s tokenem. Always-on, zdarma, bez LLM tokenů. Mac spí = zmeškané běhy, proto ne launchd. |
| **lokální launchd** | Job potřebuje lokální stroj/síť/credentials, kam runner nedosáhne — imapsync, remote-control, lokální DB/soubory. **U každého zdůvodni v `LOG.md`, proč je lokální.** |
| **cloud routine** (`schedule`) | Job vyžaduje **LLM/Claude úsudek při každém běhu**. Na mechanické skripty je to overkill (tokeny) → ber Actions. |

**Actions nasazuj end-to-end sám:** napiš `.github/workflows/*.yml`, commitni, pushni, ověř běh přes Actions API. Josef nic ručně neklikán.
⚠️ Předpoklad: git token v keychainu má `workflow` scope (fine-grained PAT na repo vaultu s Contents + Workflows + Actions R/W). Bez něj GitHub push workflow souboru odmítne → fallback na ruční paste v UI.

**Fázování (per safe-fail L0–L4):** novou automatizaci najeď ručně → pod dohledem → samostatně. Nikdy rovnou na L4.

## ⚠️ 3. Audit doručení — automatizace musí hlásit SELHÁNÍ, ne úspěch
Nejnebezpečnější automatizace není ta, co spadne. Je to ta, co **spadne potichu** a tváří se, že běží.

Každá automatizace, kterou postavíš nebo reviduješ, musí splnit tři body:
1. **Nepolykej chyby.** `prikaz >/dev/null 2>&1 && echo "OK"` je zakázaný vzor — při selhání se nezaloguje **nic** a log vypadá stejně jako když nic neběželo. Vždy zachyť stderr a zaloguj ho: `if VYSTUP="$(prikaz 2>&1)"; then … else echo "❌ CHYBA: $VYSTUP"; fi`.
2. **Stav ven jednou čitelnou větou.** Vedle logu drž soubor/notifikaci ve tvaru `OK — poslední úspěch <čas>` / `NEZALOHOVANO od <čas> — <důvod>`. Log čte člověk jen když už tuší problém; stavovou větu uvidí i když netuší.
3. **Ověř předpoklady, na kterých job stojí**, a při jejich porušení **zastav nahlas** místo tichého pokračování v polovičním režimu (např. „běžím jen na branchi `main`", „token má scope X", „vstupní soubor existuje").

**Ptej se „jak bych poznal, že to NEfunguje?"** Když odpověď je „všiml bych si, že chybí výstup", automatizace není hotová.

**Hotová detekce hlídá STÁŘÍ, ne přítomnost.** Kontrolovat „je v logu záznam?" nestačí — když se job nespustí vůbec, nikdo nic nenapíše a chybějící záznam vypadá jako klid. Kontroluj „není poslední úspěch starší než X?". Implementace: `Projects/Automatizace/health-check.sh` (běží na SessionStart, hlásí stáří posledního pushe, větev vaultu a exit kódy launchd jobů).

**⚠️ Skript, který hlídá systém, musí být VE vaultu.** Neverzovaná kopie na každém stroji znamená, že oprava se nešíří — a vzniká `.md` návod „udělej sed ručně na druhém stroji", což je práce, která neměla existovat. Kanonická kopie do `Projects/Automatizace/`, na stroji symlink. ⚠️ Když skript synchronizuje repo, ve kterém sám leží, **musí se na startu zkopírovat do /tmp a pokračovat z kopie** — jinak si ho `git pull` přepíše pod rukama a shell dočte zbytek z nové verze. Obalení do funkce **NESTAČÍ** (ověřeno testem 2026-07-28).

(Proč: 2026-07-28 se ukázalo, že `brain-sync.sh` **15 dní tiše nepushoval** — vault zůstal na staré branchi, `git push origin main` pushoval zamrzlý lokální ref, GitHub to odmítal jako non-fast-forward a chyba padala do `/dev/null`. 53 commitů existovalo v jediné kopii na jednom disku. Job přitom běžel každé 3 minuty a log vypadal zdravě. → `Projects/Automatizace/LOG.md`.)

## ⚠️ 4. Sweep — jednu instanci najdeš, celou třídu prověř
Když najdeš chybu, **zeptej se, jaká je to třída, a projdi všechny její instance** — ne jen tu, která tě kopla. Jedna nalezená instance je vzorek, ne případ.

Postup: (1) pojmenuj třídu jednou větou („automatizace, co polyká chybu a tváří se, že běží"), (2) napiš si mechanický dotaz, který ji najde (`grep`, `launchctl list`, výpis jobů/workflow), (3) projeď **všechny** kandidáty a výsledek vypiš i s těmi zdravými, (4) až pak opravuj. Sweep bez výpisu zdravých nedokazuje nic.

(Proč: 2026-07-13 jsem díru „audit doručení" našel na ads-checku, zapsal do LOGu a šel dál. Sweep, který trval dvě minuty, jsem neudělal — a odhalil by tehdy, že `brain-sync` nepushuje a `claude-remote-control` padá na 401. Stálo to 15 dní bez zálohy vaultu. Sweep 2026-07-28 našel ze 4 launchd jobů **3 rozbité**: brain-sync tiše nepushoval, remote-control v retry loopu na vypršelém přihlášení, imapsync-status vůbec nenaložený. → `Projects/Automatizace/LOG.md`.)

## 5. Kill Switch — údržba > přínos = pryč
- **Monitoruj, co běží.** Automatizace (launchd job, Action, skill, workflow), která soustavně potřebuje záplaty, chrlí nekvalitní výstup, nebo stojí víc údržby/tokenů než ušetří → **rozeber a smaž.** Umět zbourat je stejně důležité jako umět spustit.
- **Sunk cost je past:** „strávil jsem tím 3 dny" není důvod držet něco, co nefunguje.
- **Sám navrhni revizi**, když automatizací přibývá nebo jedna opakovaně padá. Kandidáty na smazání zapiš do `LOG.md`.
- **Smazání až na potvrzení** (safe-fail): nejdřív archiv/vypnutí, teprve pak delete.

## 6. Kvartální re-audit oprávnění
Projdi scopes napojených tokenů a účtů. **Write přidaný „jen jednou" se sám nereviduje** — to je scope creep a platí se za něj až při incidentu. Detaily per-nástroj: `Brain/connector-governance.md`.
(Zdroj: loop-engineering článek, „security tax"; 2026-07-13.)

## 7. Harness audit při novém modelu
Spouštěč = nový major model. Projdi `CLAUDE.md` + skilly a **smaž scaffolding, který model nově zvládá nativně** — motivační priming, „mysli nahlas", ruční dekompozici, kroky, které dřív model bez instrukce nedělal. Harness, který jen roste, je harness, který jsi přestal číst.

⚠️ **Auditu se NEPODROBUJÍ:** safe-fail, úrovně autonomie, zákaz greedy regexu, grounding LLM promptů, negativní závěr až po prohledání, projektové zákazy. Chrání před nevratnou chybou, ne před slabým modelem.

Návrh auditu dělej sám; skutečné mazání až na potvrzení. Běhy: 2026-07-12 (Opus 4.8) · 2026-07-28 (Opus 5).
(Zdroj: Karpathy „LOOPS.md" Princip VIII+IX; Anthropic článek o context engineeringu.)

## 🔗 Souvisí
- [[connector-governance|connector-governance]]
- [[Skilly/orchestrace/SKILL|orchestrace]]
- [[Projects/Automatizace/LOG|Automatizace › LOG]]

<!-- AUTO-LINKS:START -->
## 🔗 Souvislosti
- [[CLAUDE|CLAUDE (master)]]
<!-- AUTO-LINKS:END -->
