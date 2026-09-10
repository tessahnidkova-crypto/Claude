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

# ---------- ŘEŠENÍ ----------
# otázka -> [(vzorová odpověď, výslovnost, česky)]
RES_HELLO = [
 ("How are you today?", [
   ("I'm fine, thank you.", "ajm fajn, thenk jú", "Mám se dobře, děkuju."),
   ("I'm tired.", "ajm tajrd", "Jsem unavená."),
   ("I'm happy today.", "ajm hepy tudej", "Dneska jsem šťastná.")]),
 ("What's the weather like today?", [
   ("It's sunny.", "its sany", "Je slunečno."),
   ("It's raining.", "its rejning", "Prší."),
   ("It's cold and cloudy.", "its kould end klaudy", "Je zima a zataženo.")]),
 ("Where were you in the summer?", [
   ("I was at home.", "aj woz et houm", "Byla jsem doma."),
   ("I was at my grandma's.", "aj woz et máj GREND-máz", "Byla jsem u babičky."),
   ("I was in Italy.", "aj woz in ITEL-y", "Byla jsem v Itálii.")]),
 ("Did you go swimming?", [
   ("Yes, I did.", "jes, aj did", "Ano, byla."),
   ("No, I didn't.", "nou, aj DIDNT", "Ne, nebyla."),
   ("Yes, in the sea!", "jes, in ď sí", "Ano, v moři!")]),
 ("What did you eat every day?", [
   ("I ate ice cream.", "aj ejt ajs krím", "Jedla jsem zmrzlinu."),
   ("I ate a lot of fruit.", "aj ejt e lot ov frút", "Jedla jsem hodně ovoce.")]),
 ("What was the best day? Why?", [
   ("The best day was Saturday.", "ď best dej woz SETR-dej", "Nejlepší byla sobota."),
   ("Because it was fun.", "bikoz it woz fan", "Protože to byla zábava."),
   ("Because I was with my friends.", "bikoz aj woz wid máj frendz", "Protože jsem byla s kamarády.")]),
]

RES_SENT_VETY = [
 ("I like swimming.", "aj lajk SWI-ming", "Ráda plavu."),
 ("I don't like football.", "aj dount lajk FUT-ból", "Nemám ráda fotbal."),
 ("My mum likes ice cream.", "máj mam lajks ajs krím", "Máma má ráda zmrzlinu."),
 ("My mum doesn't like dogs.", "máj mam DAZNT lajk dogz", "Máma nemá ráda psy."),
 ("My dog likes the seaside.", "máj dog lajks ď SÍ-sajd", "Můj pes má rád moře."),
 ("My teacher doesn't like cats.", "máj tíčr daznt lajk kets", "Moje učitelka nemá ráda kočky."),
]

RES_ODD = [
 ("beach · sea · mountains · ICE CREAM", "ice cream",
  "Because it isn't a place.", "bikoz it IZNT e plejs", "Protože to není místo."),
 ("swim · run · TENT · ride", "tent",
  "Because a tent is a thing.", "bikoz e tent iz e thing", "Protože stan je věc."),
 ("PLANE · cat · dog · horse", "plane",
  "Because it isn't an animal.", "bikoz it iznt en ENIML", "Protože to není zvíře."),
 ("hot · sunny · cold · BIKE", "bike",
  "Because it isn't weather.", "bikoz it iznt WEDR", "Protože to není počasí."),
 ("Monday · Tuesday · JULY · Friday", "July",
  "Because it isn't a day.", "bikoz it iznt e dej", "Protože to není den."),
 ("suitcase · bag · backpack · SWIM", "swim",
  "Because it isn't a bag.", "bikoz it iznt e beg", "Protože to není taška."),
]

RES_CHALLENGE = [
 ("1", "Name 5 animals", "cat, dog, horse, fish, bird", "Zvířata máš dole na téhle straně."),
 ("2", "Spell BEACH out loud", "bí &middot; í &middot; ej &middot; sí &middot; ejč", "Abecedu máš na straně 5."),
 ("3", "Say a sentence with SWIM", "I can swim. / I like swimming.", "[aj ken swim] / [aj lajk SWI-ming]"),
 ("4", "Count from 20 down to 10", "twenty, nineteen, eighteen…", "Celá řada je dole na téhle straně."),
 ("5", "Name 3 things you can eat", "bread, cheese, an apple", "[bred] [číz] [en EPL]"),
 ("6", "Say the days of the week", "Monday … Sunday", "⚠️ Wednesday = [WENZ-dej], první D se nevyslovuje."),
 ("7", "Describe your room in 2 sentences", "My room is small. I have got a bed.", "[máj rúm iz smól] [aj hev got e bed]"),
 ("8", "Name 4 colours you can see now", "red, blue, green, white", "[red] [blú] [grín] [wajt]"),
 ("9", "Ask your teacher a question", "How are you? / Do you like ice cream?", "Nejtěžší úkol — schovej si ho na konec."),
 ("10", "Say 3 things you can do", "I can swim. I can sing. I can cook.", "[aj ken sing] [aj ken kuk]"),
]

RES_HW = [
 ("In the summer I …", [
   ("In the summer I swim in the sea.", "in ď samr aj swim in ď sí", "V létě plavu v moři."),
   ("In the summer I ride my bike.", "in ď samr aj rajd máj bajk", "V létě jezdím na kole.")]),
 ("I can …", [
   ("I can swim.", "aj ken swim", "Umím plavat."),
   ("I can ride a bike.", "aj ken rajd e bajk", "Umím jezdit na kole.")]),
 ("My best day was …", [
   ("My best day was at the beach.", "máj best dej woz et ď bíč", "Nejlepší den byl na pláži."),
   ("My best day was in the mountains.", "máj best dej woz in ď MAUN-tnz", "Nejlepší den byl na horách.")]),
]

ZASOBA = [
 ("Zvířata", "cat [ket] kočka &middot; dog [dog] pes &middot; horse [hors] kůň &middot; fish [fiš] ryba &middot; bird [bérd] pták &middot; cow [kau] kráva &middot; pig [pig] prase &middot; rabbit [REBIT] králík"),
 ("Jídlo", "bread [bred] chléb &middot; cheese [číz] sýr &middot; apple [EPL] jablko &middot; soup [súp] polévka &middot; chicken [ČIKN] kuře &middot; rice [rajs] rýže &middot; egg [eg] vejce"),
 ("Barvy", "red [red] &middot; blue [blú] &middot; green [grín] &middot; yellow [JELOU] &middot; black [blek] &middot; white [wajt] &middot; orange [ORINDŽ] &middot; pink [pink] &middot; brown [braun]"),
 ("Dny v týdnu", "Monday [MAN-dej] &middot; Tuesday [TJÚZ-dej] &middot; <b>Wednesday [WENZ-dej]</b> &middot; Thursday [THÉRZ-dej] &middot; Friday [FRAJ-dej] &middot; Saturday [SETR-dej] &middot; Sunday [SAN-dej]"),
 ("Čísla 20 → 10", "twenty [TWENTY] &middot; nineteen [najn-TÝN] &middot; eighteen [ej-TÝN] &middot; seventeen [sevn-TÝN] &middot; sixteen [siks-TÝN] &middot; fifteen [fif-TÝN] &middot; fourteen [fór-TÝN] &middot; thirteen [thér-TÝN] &middot; twelve [twelv] &middot; eleven [i-LEVN] &middot; ten [ten]"),
 ("Co umím (can)", "swim [swim] plavat &middot; sing [sing] zpívat &middot; cook [kuk] vařit &middot; dance [dáns] tancovat &middot; draw [dró] kreslit &middot; run [ran] běhat &middot; read [ríd] číst"),
]
