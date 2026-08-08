# Záloha — skilly z kitu, které NEJSOU zavedené

Tyhle soubory **nejsou aktivní**. Claude je nenačítá — leží tady jen jako materiál na později. Aktivní skilly žijí v `.claude/skills/`.

Proč nejsou zavedené: kit sám varuje, že víc než 3 skilly naráz znamená, že neposoudíš, co pomohlo. A většina těchhle je stavěná na programování a byznys, ne na studium.

## Co tu leží

| Soubor | Co dělá | Kdy by se mohl hodit |
|---|---|---|
| `grill-me.md` | Vyzpovídá tě otázku po otázce a zapisuje odpovědi do souboru | Když budeš plánovat něco většího (výběr stáže, diplomka, velké rozhodnutí) a potřebuješ to dostat z hlavy |
| `loop_agent.md` | Maker/Checker cyklus na texty — píše a sám si to kritizuje, dokud to neprojde | Motivační dopis, žádost o stáž, cokoli důležitého, co jde ven. Stojí ~4× tokenů. |
| `roast.md` | Rada 5 person nápad rozstřelí, pak verdikt GO / RESHAPE / KILL | Než do něčeho půjdou peníze nebo hodně času |
| `autopilot.md` | Režim pro stavbu netriviálního kódu bez doptávání | Jen kdyby ses pustila do programování |
| `agent_loop_pbj.md` | Engine Plan/Build/Judge pod autopilotem | Totéž |
| `automatizace-governance.md` | Pravidla, kdy vůbec stavět automatizaci | Až budeš chtít něco spouštět automaticky (např. denní připomínku) |
| `KATALOG-SKILLU.md` | Původní katalog všech 53 skillů z kitu | Inspirace, co dalšího jde postavit |
| `PUVODNI-CLAUDE-sablona.md` | Původní neupravená šablona pravidel z kitu | Referenční originál — kdyby ses chtěla podívat, co jsem oproti němu změnil |

## Jak některý z nich zavést

1. Vytvoř složku: `.claude/skills/<nazev>/`
2. Zkopíruj tam soubor jako `SKILL.md`
3. **Přepiš „Josef" na „Tessa"** a cesty (`Brain/Projects/` → `Projekty/`, `Vault/Skilly/` → `.claude/skills/`)
4. Commit + push
5. ⚠️ **Načte se až v nové session** — v běžící ho neuvidíš

Nebo prostě řekni Claudovi: *„zaveď mi loop_agent ze zálohy"* a udělá to za tebe.
