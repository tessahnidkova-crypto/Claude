# -*- coding: utf-8 -*-
# Hodina 2 — specifická data. Obecné fráze se recyklují z tahak1_data.

STRANY = [
 ("1","Titulka",[
  ("Write your name here.","rajt jor nejm hír","Napiš sem svoje jméno."),
  ("Today: what can you do?","tudej: wot ken jú dú","Dneska: co všechno umíš?")]),
 ("2","Hello again! + úkol",[
  ("How are you today?","hau ár jú tudej","Jak se dneska máš?"),
  ("Show me your homework.","šou mí jor HOUM-vérk","Ukaž mi domácí úkol."),
  ("Do you remember these words?","dú jú ri-MEMBR dýz vérdz","Pamatuješ si tahle slovíčka?"),
  ("Read me one sentence.","ríd mí wan SENTNS","Přečti mi jednu větu.")]),
 ("3","Action words",[
  ("What is he doing?","wot iz hí DÚ-ing","Co dělá? (u obrázku)"),
  ("Repeat after me.","ri-PÍT áftr mí","Opakuj po mně."),
  ("Now write it in Czech.","nau rajt it in ček","Teď to napiš česky.")]),
 ("4","Word race (na čas)",[
  ("No words — just pictures!","nou vérdz — džast PIK-črz","Žádná slova — jenom obrázky!"),
  ("Ready? Go!","redy? gou","Připravená? Teď!"),
  ("Time's up!","tajmz ap","Čas vypršel!"),
  ("How many?","hau MENY","Kolik jsi jich dala?"),
  ("Can you beat it?","ken jú bít it","Zvládneš to překonat?")]),
 ("5","I can / I can't",[
  ("Can you swim? Circle it.","ken jú swim? SÉRKL it","Umíš plavat? Zakroužkuj."),
  ("True for you!","trú for jú","Podle pravdy!"),
  ("Now write three sentences.","nau rajt thrí SENTN-siz","Teď napiš tři věty.")]),
 ("6","Can you…? (ptá se TEBE)",[
  ("Now you ask ME!","nau jú ásk mí","Teď se ptáš ty mě!"),
  ("Yes, I can. / No, I can't.","jes aj ken / nou aj kánt","Ano, umím. / Ne, neumím."),
  ("A little bit.","e litl bit","Trochu."),
  ("Now tell me about me!","nau tel mí e-BAUT mí","Teď mi řekni něco o mně!")]),
 ("7","Secret action (hra)",[
  ("Circle one — don't tell me!","sérkl wan — dount tel mí","Jednu zakroužkuj — neříkej mi to!"),
  ("Can you ride a bike?","ken jú rajd e bajk","Umíš jezdit na kole?"),
  ("I know! You can cook!","aj nou! jú ken kuk","Já vím! Ty umíš vařit!"),
  ("My turn! / Your turn!","máj térn / jor térn","Já jsem na řadě! / Ty jsi na řadě!")]),
 ("8","Homework",[
  ("Learn these six words.","lérn dýz siks vérdz","Nauč se těchhle šest slovíček."),
  ("Draw yourself.","dró jor-SELF","Nakresli sama sebe."),
  ("Can you tell me the homework?","ken jú tel mí ď HOUM-vérk","Můžeš mi říct, co máš za úkol?")]),
 ("9","Bonus (když zbyde čas)",[
  ("Choose a square.","čúz e skwér","Vyber si políčko."),
  ("Say a sentence with CAN.","sej e SENTNS wid ken","Řekni větu se slovem CAN."),
  ("It's yours!","ic jorz","Je tvoje!"),
  ("Three in a row — you win!","thrí in e rou — jú win","Tři v řadě — vyhrálas!")]),
]

# 20 obrázků na straně 4 listu, po řadách zleva doprava
RACE_KLIC = [
 ["swim","ride a bike","run","sing","dance"],
 ["cook","draw","play football","play tennis","play the piano"],
 ["ski","skate","beach","sea","ice cream"],
 ["mountains","sun","tent","suitcase","plane"],
]

SLOVICKA = [
 ("swim","swim","plavat","Znáš z minula."),
 ("ride a bike","rajd e bajk","jezdit na kole",""),
 ("run","ran","běhat",""),
 ("sing","sing","zpívat","Ne „sink“ — na konci je nosové NG."),
 ("dance","dáns","tancovat","Britsky dlouhé Á, ne „dens“."),
 ("cook","kuk","vařit",""),
 ("draw","dró","kreslit","Ne „drav“ — W se nevyslovuje."),
 ("play football","plej FUT-ból","hrát fotbal",""),
 ("play tennis","plej TE-nis","hrát tenis",""),
 ("play the piano","plej ď pi-E-nou","hrát na klavír","⚠️ THE jen u nástrojů, ne u sportů."),
 ("ski","skí","lyžovat","Dlouhé Í."),
 ("skate","skejt","bruslit",""),
]

# (nadpis, řádky) — gramatika CAN
CAN_TAB = [
 ("I","can swim","can't swim","aj ken swim / aj kánt swim"),
 ("You","can swim","can't swim","jú ken swim"),
 ("My mum / She","can swim","can't swim","máj mam ken swim"),
 ("My dog / It","can swim","can't swim","máj dog ken swim"),
 ("My friends / They","can swim","can't swim","máj frendz ken swim"),
]

CAN_CHYBY = [
 ("My mum <u>cans</u> swim.", "My mum can swim.",
  "Po <b>can</b> se nikdy nepřidává -s. Tohle je ta past — minule se <b>-s</b> přidávat MUSELO (<i>My mum likeS</i>), teď se NESMÍ."),
 ("I can <u>to</u> swim.", "I can swim.",
  "Po <b>can</b> jde holé sloveso, žádné <i>to</i>."),
 ("I can <u>swimming</u>.", "I can swim.",
  "Po <b>can</b> jde základní tvar, ne -ing."),
 ("I <u>no can</u> swim.", "I can't swim.",
  "Zápor se dělá slovem <b>can't</b>, ne přidáním <i>no</i>."),
 ("Yes, I can <u>swim</u>.", "Yes, I can.",
  "V krátké odpovědi se sloveso neopakuje. (Není to chyba, jen to zní nepřirozeně.)"),
]

CAN_VETY = [
 ("I can draw.","aj ken dró","Umím kreslit."),
 ("I can't ski.","aj kánt skí","Neumím lyžovat."),
 ("My mum can cook.","máj mam ken kuk","Máma umí vařit."),
 ("My dog can swim.","máj dog ken swim","Můj pes umí plavat."),
 ("Can you play the piano?","ken jú plej ď pi-E-nou","Umíš hrát na klavír?"),
 ("No, I can't. A little bit.","nou, aj kánt. e litl bit","Ne, neumím. Trochu."),
]

HW_KLIC = [
 ("suitcase","kufr"),("tent","stan"),("mountains","hory"),
 ("castle","hrad"),("plane","letadlo"),("seaside","u moře"),
]

RES_STR4 = [
 ("I can draw.","aj ken dró","Umím kreslit."),
 ("I can't play the piano.","aj kánt plej ď pi-E-nou","Neumím hrát na klavír."),
 ("My mum can cook.","máj mam ken kuk","Máma umí vařit."),
]
RES_STR5 = [
 ("My teacher can cook.","máj tíčr ken kuk","Moje učitelka umí vařit."),
 ("My teacher can't ski.","máj tíčr kánt skí","Moje učitelka neumí lyžovat."),
]
RES_HW = [
 ("I can ride a bike.","aj ken rajd e bajk","Umím jezdit na kole."),
 ("I can't skate.","aj kánt skejt","Neumím bruslit."),
 ("My best friend can sing.","máj best frend ken sing","Můj kamarád umí zpívat."),
]

ZASOBA = [
 ("Další činnosti, kdyby chtěla víc",
  "read [ríd] číst &middot; write [rajt] psát &middot; jump [džamp] skákat &middot; "
  "climb [klajm] šplhat (<b>B se nevyslovuje</b>) &middot; play chess [plej čes] hrát šachy &middot; "
  "ride a horse [rajd e hors] jezdit na koni &middot; speak English [spík INGLIŠ] mluvit anglicky"),
 ("Jak pochválit odpověď u hry",
  "You got it! [jú got it] Uhodla jsi! &middot; That was quick! [det woz kwik] To bylo rychlé! &middot; "
  "One more! [wan mór] Ještě jednu!"),
 ("Kdyby zbyl čas po straně 3 listu",
  "Vrať se na stranu 3 listu a ptej se <b>„Can you …?“</b> na každý obrázek. Dvanáct obrázků = dvanáct otázek, "
  "a procvičí se přesně to, co se dneska učí."),
]
