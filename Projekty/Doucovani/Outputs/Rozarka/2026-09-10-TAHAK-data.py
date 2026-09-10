# -*- coding: utf-8 -*-
# EN, výslovnost (zjednodušený český přepis), česky
HODINA = [
 ("Na začátku", "sea", [
  ("Hi Rozárka! How are you?", "haj … hau ár jú", "Ahoj! Jak se máš?"),
  ("Can you hear me?", "ken jú hír mí", "Slyšíš mě?"),
  ("Can you see my screen?", "ken jú sí máj skrín", "Vidíš moji obrazovku?"),
  ("Let's start!", "lets stárt", "Začínáme!"),
  ("Write your name here.", "rajt jor nejm hír", "Napiš sem svoje jméno."),
 ]),
 ("Pokyny během hodiny", "ink", [
  ("Look at page three.", "luk et pejdž thrí", "Podívej se na stranu 3."),
  ("Read it out loud.", "ríd it aut laud", "Přečti to nahlas."),
  ("Say it in English.", "sej it in ingliš", "Řekni to anglicky."),
  ("Say it in Czech.", "sej it in ček", "Řekni to česky."),
  ("Write it here.", "rajt it hír", "Napiš to sem."),
  ("Circle the word.", "sérkl ď vérd", "Zakroužkuj to slovo."),
  ("Repeat after me.", "ripít áftr mí", "Opakuj po mně."),
  ("One more time.", "wan mór tajm", "Ještě jednou."),
  ("Full sentence, please.", "ful sentns plíz", "Celou větou, prosím."),
  ("Take your time.", "tejk jor tajm", "Nespěchej."),
  ("Next one.", "nekst wan", "Další."),
  ("Let's move on.", "lets múv on", "Jdeme dál."),
 ]),
 ("Pochvala — používej hodně", "ok", [
  ("Well done!", "wel dan", "Výborně!"),
  ("Very good!", "very gud", "Moc dobře!"),
  ("Excellent!", "ekselent", "Skvělé!"),
  ("That's right!", "dets rajt", "Správně!"),
  ("Good job!", "gud džob", "Dobrá práce!"),
  ("Perfect!", "pérfekt", "Perfektní!"),
  ("You're getting better!", "jor geting betr", "Zlepšuješ se!"),
 ]),
 ("Když to není správně — nikdy neříkej „No!“", "stamp", [
  ("Almost!", "ólmoust", "Skoro!"),
  ("Good try!", "gud traj", "Dobrý pokus!"),
  ("Close!", "klous", "Blízko!"),
  ("Not quite — try again.", "not kwajt — traj egejn", "Ne tak úplně — zkus to znovu."),
  ("Listen: …", "lisn", "Poslouchej: … (a řekni to správně)"),
  ("Let's do it together.", "lets dú it tugedr", "Uděláme to spolu."),
 ]),
 ("Když neví nebo nerozumí", "sun", [
  ("Do you understand?", "dú jú andrstend", "Rozumíš?"),
  ("Do you know this word?", "dú jú nou dis vérd", "Znáš tohle slovo?"),
  ("It means „…“", "it mínz", "Znamená to „…“"),
  ("Think about it.", "think ebaut it", "Přemýšlej."),
  ("I'll help you.", "ajl help jú", "Pomůžu ti."),
  ("Don't worry.", "dount wory", "Neboj."),
  ("Sorry, can you repeat?", "sory, ken jú ripít", "Promiň, můžeš to zopakovat? (když nerozumíš TY)"),
 ]),
 ("Na konci", "sea", [
  ("That's all for today.", "dets ól for tudej", "To je pro dnešek všechno."),
  ("Your homework is on page seven.", "jor houmvérk iz on pejdž sevn", "Domácí úkol je na straně 7."),
  ("You got five stars today!", "jú got fajv stárz tudej", "Dneska máš pět hvězd!"),
  ("Great job today!", "grejt džob tudej", "Dneska to bylo super!"),
  ("See you next week!", "sí jú nekst wík", "Uvidíme se příští týden!"),
  ("Bye bye!", "baj baj", "Ahoj!"),
 ]),
]

# strana listu -> (co říct anglicky, výslovnost, česky / poznámka)
STRANY = [
 ("1", "Titulka", [
  ("Write your name here.", "rajt jor nejm hír", "Napiš sem svoje jméno."),
  ("These stars are yours!", "dýz stárz ár jorz", "Tyhle hvězdy jsou tvoje!"),
  ("Colour one star for every challenge.", "kalr wan stár for evry čelindž", "Za každý splněný úkol si vybarvíš jednu hvězdu."),
 ]),
 ("2", "Hello again!", [
  ("How are you today?", "hau ár jú tudej", "Jak se dneska máš?"),
  ("What's the weather like today?", "wots ď wedr lajk tudej", "Jaké je dnes počasí?"),
  ("Where were you in the summer?", "wér wér jú in ď samr", "Kde jsi byla v létě?"),
  ("Did you go swimming?", "did jú gou swiming", "Byla jsi plavat?"),
  ("What did you eat every day?", "wot did jú ít evry dej", "Co jsi jedla každý den?"),
  ("What was the best day? Why?", "wot woz ď best dej? waj", "Který den byl nejlepší? Proč?"),
 ]),
 ("3", "Holiday words", [
  ("What is this in English?", "wot iz dis in ingliš", "Co je to anglicky?"),
  ("Repeat after me.", "ripít áftr mí", "Opakuj po mně."),
  ("Now write it in Czech.", "nau rajt it in ček", "Teď to napiš česky."),
 ]),
 ("4", "Sentence machine", [
  ("Circle one word from each box.", "sérkl wan vérd from íč boks", "Zakroužkuj jedno slovo z každého rámečku."),
  ("Now write your sentence.", "nau rajt jor sentns", "Teď napiš svoji větu."),
  ("Read it out loud.", "ríd it aut laud", "Přečti to nahlas."),
  ("Is it true or false?", "iz it trú or fóls", "Je to pravda, nebo ne?"),
  ("Now say the true one.", "nau sej ď trú wan", "Teď řekni tu pravdivou. (když zakroužkuje FALSE)"),
 ]),
 ("5", "Odd one out", [
  ("Which word doesn't belong?", "wič vérd daznt bilong", "Které slovo tam nepatří?"),
  ("Why? Tell me in English.", "waj? tel mí in ingliš", "Proč? Řekni mi to anglicky."),
  ("Start with „Because it isn't…“", "bikoz it iznt", "Začni „Because it isn't…“ (Protože to není…)"),
 ]),
 ("6", "Star challenge", [
  ("Pick a number from one to ten.", "pik e nambr from wan tu ten", "Vyber si číslo od jedné do deseti."),
  ("Are you ready? Go!", "ár jú redy? gou", "Jsi připravená? Teď!"),
  ("You did it! Colour a star.", "jú did it! kalr e stár", "Dokázala jsi to! Vybarvi si hvězdu."),
 ]),
 ("7", "Homework", [
  ("This is your homework.", "dis iz jor houmvérk", "Tohle je tvůj domácí úkol."),
  ("Learn these six words.", "lérn dýz siks vérdz", "Nauč se těchhle šest slovíček."),
  ("Write three sentences in your notebook.", "rajt thrí sentnsiz in jor noutbuk", "Napiš tři věty do sešitu."),
  ("Can you tell me the homework?", "ken jú tel mí ď houmvérk", "Můžeš mi říct, co máš za úkol? (ověření)"),
 ]),
]

SLOVICKA = [
 ("beach", "bíč", "pláž", "Dlouhé Í! Krátké „bič“ je v angličtině sprosté slovo."),
 ("sea", "sí", "moře", ""),
 ("swim", "swim", "plavat", "W = rty do kolečka, ne české V."),
 ("ice cream", "ajs krím", "zmrzlina", ""),
 ("mountains", "MAUN-tnz", "hory", "Přízvuk na první slabice."),
 ("bike", "bajk", "kolo", ""),
 ("sun", "san", "slunce", ""),
 ("tent", "tent", "stan", ""),
 ("suitcase", "SÚT-kejs", "kufr", "Ne „sjút“ — čte se SÚT."),
 ("plane", "plejn", "letadlo", ""),
 ("castle", "KÁ-sl", "hrad", "T se NEVYSLOVUJE."),
 ("friend", "frend", "kamarád", ""),
 ("seaside", "SÍ-sajd", "u moře", "Je v domácím úkolu — vysvětli jí ho."),
]

ZVUKY = [
 ("th", "the, this, weather, together",
  "Jazyk mezi zuby, znělé — jako když šišláš na „d“. V taháku píšu ď/d.",
  "Když to nezvládneš, řekni „d“. Nikdy „z“ nebo „f“."),
 ("w", "swim, well, why, what",
  "Rty do malého kolečka, jako když foukáš. NENÍ to české V.",
  "Rozdíl slyší i děti — stojí za to si to nacvičit."),
 ("r", "very, right, friend, read",
  "Jazyk se nikde nedotýká, nedrnčí. Zní to skoro jako „ř“ bez chvění.",
  "České drnčivé R je největší poznávací znak českého přízvuku."),
]

NOUZOVKY = [
 ("Nevíš, jak se něco řekne", "Řekni to česky. Nikdy nehádej — naučila by se tvoji chybu jako správnou."),
 ("Nerozumíš, co řekla", "„Sorry, can you repeat?“ [sory, ken jú ripít] nebo prostě „Zopakuj to, prosím.“"),
 ("Mlčí a nic neříká", "Nabídni jí výběr: „Is it a beach or a castle?“ Vybrat je snazší než vymyslet."),
 ("Odpovídá jedním slovem", "„Full sentence, please.“ [ful sentns plíz] a ukaž jí nápovědu kurzívou v listu."),
 ("Řekne to špatně", "Neopravuj přímo. Zopakuj to správně jako běžnou reakci: ona „I go to sea“ → ty „Ah, you went to the seaside! Nice.“"),
 ("Vypadne internet / zvuk", "„Just a moment.“ [džast e moument] — Momentíček."),
 ("Je unavená a nedává to", "Přeskoč na stranu 6 (hra) a skonči tam. Lepší skončit v dobrém než dotáhnout plán."),
 ("Zbývá 5 minut a nejsi u konce", "Rovnou na stranu 7. Domácí úkol nikdy nevynechávej."),
]

ABECEDA = [("A","ej"),("B","bí"),("C","sí"),("D","dý"),("E","í"),("F","ef"),("G","dží"),
 ("H","ejč"),("I","aj"),("J","džej"),("K","kej"),("L","el"),("M","em"),("N","en"),
 ("O","ou"),("P","pí"),("Q","kjú"),("R","ár"),("S","es"),("T","tí"),("U","jú"),
 ("V","ví"),("W","dabl jú"),("X","eks"),("Y","waj"),("Z","zed")]
