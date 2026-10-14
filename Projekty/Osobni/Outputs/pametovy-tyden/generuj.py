#!/usr/bin/env python3
"""Generátor „Týden pro paměť" pro babičku a dědu.

Zdroj obsahu = tenhle soubor. Úprava: změň texty v DNY, spusť
  python3 generuj.py && node render.js
→ vznikne tyden-1.html a tyden-1.pdf.
"""
import html
from pathlib import Path

OUT = Path(__file__).parent

# ---------------------------------------------------------------- obsah
DNY = [
    dict(
        den="Pondělí", tema="Na statku", ikona="🐓",
        ranni="Jaké je dnes datum? A co jste včera měli k večeři?",
        vzpominky=[
            "Jak se jmenovala vaše první kráva nebo kůň? Proč zrovna tak?",
            "Co všechno se na statku muselo udělat v říjnu, než přišla zima?",
            "Jak u vás probíhala zabijačka? Kdo měl co na starosti?",
        ],
        kviz=[
            ("Jak dlouho nosí kráva tele?", ["asi 6 měsíců", "asi 9 měsíců", "asi 12 měsíců"]),
            ("Jak se jmenuje mládě kozy?", ["jehně", "kůzle", "hříbě"]),
            ("Za kolik dní se z vajíčka vylíhne kuře?", ["14", "21", "30"]),
            ("Čím se dříve ručně mlátilo obilí?", ["srpem", "cepem", "hráběmi"]),
            ("Jak se říká samci kachny?", ["kačer", "houser", "kohout"]),
        ],
        hadanka=dict(typ="tajenka", nazev="Tajenka",
            navod="První písmena shora dolů dají tajenku – místo, kam se sváželo seno a obilí.",
            radky=[
                ("Usušená tráva pro dobytek na zimu", "SENO"),
                ("Mládě krávy", "TELE"),
                ("Obilí, které nejraději žerou koně", "OVES"),
                ("Co se dělá s kravou ráno a večer", "DOJIT"),
                ("Zvíře, které dává vlnu", "OVCE"),
                ("Kde se seče tráva", "LOUKA"),
                ("Keř s chlupatými kyselými kuličkami", "ANGREŠT"),
            ]),
        clanek=dict(nadpis="Proč kohout kokrhá ještě za tmy?", odstavce=[
            "Kohout se ozve dřív, než vyjde slunce. Dlouho se myslelo, že ho probudí první světlo. Japonští vědci z univerzity v Nagoji to v roce 2013 vyzkoušeli.",
            "Kohouty zavřeli do místnosti, kde bylo pořád stejné tlumené světlo. A kohouti přesto kokrhali každý den zhruba ve stejnou dobu, kdy by venku začínalo svítat. Mají totiž v těle vlastní „hodiny“, které běží přibližně 24 hodin.",
            "Vědci zjistili ještě jednu věc: v hejnu se jako první ozývá vždycky kohout nejvyšší v pořadí – ten nejsilnější. Ostatní počkají, až začne on. Kdo by si taky troufl kokrhat dřív než pán dvora?",
        ]),
        otazky=["Ve které zemi vědci pokus dělali?", "Který kohout v hejnu začíná kokrhat jako první?"],
    ),
    dict(
        den="Úterý", tema="V lese a na honu", ikona="🦌",
        ranni="Vzpomenete si na tajenku ze včerejška? Co jste včera dělali odpoledne?",
        vzpominky=[
            "Dědo, na který hon nejraději vzpomínáš? Kdo tam s tebou byl?",
            "Jakého jsi měl psa? Jak se jmenoval a co všechno uměl?",
            "Jaké nejvzácnější zvíře jsi kdy v lese viděl?",
        ],
        kviz_uvod="Myslivecká mluva. Dědo, dnes jsi zkoušející ty – babička odpovídá, ty kontroluješ a vysvětluješ!",
        kviz=[
            ("Jak myslivci říkají krvi zvěře?", ["šťáva", "barva", "stopa"]),
            ("Jak myslivci říkají očím zvěře?", ["světla", "kukadla", "lampy"]),
            ("Jak se jmenuje samec divokého prasete?", ["beran", "kňour", "jelen"]),
            ("Jak se jmenuje samice jelena?", ["laň", "srna", "muflonka"]),
            ("Kdo je patronem myslivců?", ["svatý Václav", "svatý Hubert", "svatý Martin"]),
        ],
        hadanka=dict(typ="nepatri", nazev="Co nepatří do řady?",
            navod="V každém řádku jedno slovo nepatří k ostatním. Škrtněte ho a řekněte proč.",
            radky=[
                "srnec · jelen · daněk · zajíc",
                "liška · jezevec · kuna · bažant",
                "dub · buk · smrk · javor",
                "sova · datel · káně · netopýr",
            ],
            presmycky=["KAŠIL", "NELEJ", "VASO", "CENRS"],
            presmycky_navod="Přesmyčky – přeházená písmena dají zvíře z lesa:"),
        clanek=dict(nadpis="Svatý Hubert – proč je patronem myslivců", odstavce=[
            "Podle staré legendy byl Hubert šlechtic, který žil asi před 1300 lety v Ardenách, na území dnešní Belgie. Lov miloval nade všechno – prý vyrazil do lesa i na Velký pátek, kdy se lovit nemělo. V lese před ním stanul jelen a mezi jeho parožím zářil kříž. Hubert uslyšel hlas, který ho vyzval, aby změnil svůj život.",
            "Od té doby lovil s úctou, stal se knězem a nakonec biskupem. Zemřel kolem roku 727. Z legendy vzešlo pravidlo, které myslivci dodržují dodnes: zvěř šetřit, nestřílet zbytečně a ulovenému kusu vzdát poslední čest – třeba zelenou větvičkou, „posledním hryzem“.",
            "Svátek svatého Huberta je 3. listopadu. Kolem tohoto dne se po celé republice konají hubertské mše, hony a hubertovské jízdy na koních.",
        ]),
        otazky=["Co uviděl Hubert mezi parožím jelena?", "Kdy má svatý Hubert svátek?"],
    ),
    dict(
        den="Středa", tema="Za hranice: Itálie", ikona="🇮🇹",
        ranni="Jaký den byl předevčírem? Co jste včera měli k obědu?",
        vzpominky=[
            "Babičko, kam ses v životě podívala nejdál?",
            "Které cizí jídlo vám nejvíc chutnalo – nebo které byste rádi ochutnali?",
            "Kdybyste zítra mohli odjet kamkoli na světě, kam by to bylo a proč?",
        ],
        kviz=[
            ("Jaké je hlavní město Itálie?", ["Milán", "Řím", "Neapol"]),
            ("Ve kterém městě stojí šikmá věž?", ["v Pise", "ve Florencii", "v Benátkách"]),
            ("Která sopka zasypala starověké město Pompeje?", ["Etna", "Vesuv", "Stromboli"]),
            ("Jaká řeka teče Římem?", ["Pád", "Tibera", "Arno"]),
            ("Jak se italsky řekne „děkuji“?", ["gracias", "grazie", "merci"]),
        ],
        hadanka=dict(typ="spojovacka", nazev="Spojte čarou",
            navod="Spojte každou zemi s tím, čím je známá.",
            leve=["Francie", "Nizozemsko", "Egypt", "Řecko", "Švýcarsko", "Anglie"],
            prave=["pyramidy", "Big Ben", "Eiffelova věž", "Alpy a sýr s dírami", "Akropolis", "větrné mlýny a tulipány"]),
        clanek=dict(nadpis="Benátky – město, které stojí na dřevě", odstavce=[
            "Benátky jsou postavené na více než stovce malých ostrovů v laguně u Jaderského moře. Místo ulic mají kanály, místo aut lodě – a nejslavnější z nich jsou černé gondoly.",
            "Jak se dá postavit kamenný palác na bahně? Benátčané před staletími zatloukali do dna laguny miliony dřevěných kůlů, hlavně z dubu a modřínu. Na ně položili dřevěné desky a teprve na ně kámen. Dřevo, které je celé pod vodou a v bahně, se nedostane ke vzduchu – a proto nehnije. Domy na něm stojí celá staletí.",
            "Na podzim a v zimě přichází „acqua alta“ – vysoká voda, kdy moře zaplaví i náměstí svatého Marka a lidé chodí po dřevěných lávkách. Od roku 2020 město chrání obří pohyblivé hráze jménem MOSE, které se při velké vodě zvednou ze dna moře.",
        ]),
        otazky=["Z jakého dřeva jsou kůly pod Benátkami?", "Proč dřevo pod vodou nehnije?"],
    ),
    dict(
        den="Čtvrtek", tema="Kus naší historie", ikona="📜",
        ranni="Na čem stojí Benátky? A co jste dělali včera večer?",
        vzpominky=[
            "Dědo, co ti o válce vyprávěli tvoji rodiče nebo prarodiče?",
            "Kde jste byli a co jste dělali v srpnu 1968?",
            "Jak se u vás na vesnici změnil život, když vzniklo JZD?",
        ],
        kviz=[
            ("Kdy vzniklo Československo?", ["28. října 1918", "1. ledna 1920", "9. května 1945"]),
            ("Kdo byl prvním československým prezidentem?", ["Edvard Beneš", "T. G. Masaryk", "Ludvík Svoboda"]),
            ("Které město osvobodila v květnu 1945 americká armáda?", ["Plzeň", "Brno", "Olomouc"]),
            ("Jak se jmenovali parašutisté, kteří v roce 1942 provedli atentát na Heydricha?", ["Gabčík a Kubiš", "Mašín a Morávek", "Švec a Šrámek"]),
            ("Ve kterém roce skončila druhá světová válka v Evropě?", ["1944", "1945", "1946"]),
        ],
        hadanka=dict(typ="poradi", nazev="Seřaďte podle času",
            navod="Očíslujte události od nejstarší (1) po nejnovější (6).",
            radky=["Atentát na Heydricha", "Vznik Československa", "Sametová revoluce",
                   "Mnichovská dohoda", "Konec druhé světové války", "Příjezd vojsk Varšavské smlouvy"]),
        clanek=dict(nadpis="Josef František – Čech, který bránil Londýn", odstavce=[
            "V létě 1940 stála Británie proti Hitlerovi sama. Německá letadla útočila na anglická letiště a města a o všem se rozhodovalo ve vzduchu. Tomu se říká Bitva o Británii.",
            "Mezi piloty, kteří Británii bránili, byli i Čechoslováci, kteří utekli z okupované vlasti. Nejslavnější z nich byl Josef František, rodák z Otaslavic u Prostějova. Létal s polskou 303. perutí – s Poláky už předtím bojoval v Polsku i ve Francii. Během září 1940 sestřelil 17 nepřátelských letadel a patřil k nejúspěšnějším pilotům celé bitvy.",
            "Domů se už nevrátil. Zahynul 8. října 1940 při letecké nehodě, den po svých 26. narozeninách. V Británii, v Polsku i u nás na něj dodnes vzpomínají jako na hrdinu.",
        ]),
        otazky=["S jakou perutí Josef František létal?", "Kolik nepřátelských letadel sestřelil?"],
    ),
    dict(
        den="Pátek", tema="Zahrada a kuchyně", ikona="🥧",
        ranni="Kdo byl Josef František? A s kým jste včera mluvili?",
        vzpominky=[
            "Babičko, který recept po mamince umíš dodnes zpaměti? Napiš ho sem.",
            "Co jste nejraději zavařovali nebo sušili na zimu?",
            "Kdo u vás doma pekl nejlepší chleba nebo koláče?",
        ],
        kviz_uvod="Doplňte pranostiky a přísloví.",
        doplnovacka=[
            "Medard kápě, ________ dní kape.",
            "Na svatého ________ přijíždí na bílém koni.",
            "Únor bílý, ________ sílí.",
            "Na Hromnice o ________ více.",
            "Pankrác, Servác, Bonifác – říká se jim ________ muži.",
            "Bez práce nejsou ________.",
        ],
        hadanka=dict(typ="seznam", nazev="Nákupní seznam – paměťová hra",
            navod="Přečtěte si pomalu seznam. Pak ho zakryjte papírem a napište, co si pamatujete. Pomůže představit si, že z toho pečete koláče.",
            polozky=["mouka", "vejce", "máslo", "droždí", "cukr", "mléko", "švestky", "mák", "sůl", "tvaroh"]),
        clanek=dict(nadpis="Jak brambory přišly do Čech", odstavce=[
            "Brambory u nás nebyly odjakživa. Pocházejí z Jižní Ameriky, z hor zvaných Andy, kde je místní obyvatelé pěstovali tisíce let. Do Evropy je přivezli Španělé v 16. století. Zpočátku je lidé pěstovali spíš pro hezké květy a jíst se je báli – zelené bobule i nať jsou totiž jedovaté.",
            "Své české jméno dostaly podle sousedního Braniborska – brambory jsou vlastně „braniborky“. Opravdu se u nás rozšířily až po velkém hladomoru v letech 1770–1772, kdy lidé poznali, že brambory rodinu uživí, i když se obilí neurodí.",
            "Pak už to šlo rychle – knedlíky, bramboráky, škubánky, kaše… Dnes si českou kuchyni bez brambor neumíme představit.",
        ]),
        otazky=["Odkud brambory původně pocházejí?", "Podle kterého kraje dostaly brambory své české jméno?"],
    ),
    dict(
        den="Sobota", tema="Na cestách po světě", ikona="🧭",
        ranni="Odkud pocházejí brambory? Co jste včera měli k obědu?",
        vzpominky=[
            "Pamatujete si na pohlednici, kterou jste dostali z ciziny? Odkud byla a kdo ji poslal?",
            "Babičko, jaké cizí slovo nebo větu znáš? Nauč ji dědu.",
            "Dědo, kde jsi byl v životě nejdál od domova?",
        ],
        kviz=[
            ("Ve které zemi žijí ve volné přírodě klokani?", ["v Keni", "v Austrálii", "v Brazílii"]),
            ("Která hora je nejvyšší na světě?", ["Mont Blanc", "Mount Everest", "Kilimandžáro"]),
            ("Do kterého moře se vlévá Dunaj?", ["do Černého", "do Severního", "do Středozemního"]),
            ("Ve kterém městě stojí Socha svobody?", ["v Londýně", "v Paříži", "v New Yorku"]),
            ("Jaké je hlavní město Norska?", ["Oslo", "Stockholm", "Kodaň"]),
        ],
        hadanka=dict(typ="tajenka", nazev="Tajenka",
            navod="Vyluštěte slova. První písmena shora dolů dají tajenku – zemi, o které je dnešní článek.",
            radky=[
                ("Řeka, která teče Egyptem", "NIL"),
                ("Velká slaná voda mezi světadíly", "OCEÁN"),
                ("Naši jižní sousedé s hlavním městem Vídní", "RAKOUSKO"),
                ("Největší horká poušť na světě", "SAHARA"),
                ("Zvíře, které nosí mládě ve vaku", "KLOKAN"),
                ("Kus země, ze všech stran obklopený vodou", "OSTROV"),
            ]),
        clanek=dict(nadpis="Norsko – země půlnočního slunce", odstavce=[
            "Norsko je dlouhá země na severu Evropy. Jeho pobřeží je rozbrázděné fjordy – úzkými, hlubokými zálivy se strmými skalami, které sahají daleko do vnitrozemí. Vyhloubily je obří ledovce v dobách ledových. Nejdelší, Sognefjord, měří přes 200 kilometrů.",
            "Na severu Norska, za polárním kruhem, slunce v létě celé týdny nezapadá – i o půlnoci je světlo. V zimě je to naopak a slunce se dlouho neukáže vůbec. Zato je za tmy vidět polární záře – zelené pruhy světla, které se vlní po obloze.",
            "Podél pobřeží jezdí už od roku 1893 lodě Hurtigruten. Dřív vozily poštu a zásoby do vesnic, kam nevedla silnice. Dnes s nimi cestují i turisté.",
        ]),
        otazky=["Co vytvořilo norské fjordy?", "Co je vidět na obloze v norské zimě?"],
    ),
    dict(
        den="Neděle", tema="Rodina a velký týdenní kvíz", ikona="💛",
        ranni="Co jste dělali včera? A co vás tento týden nejvíc pobavilo?",
        vzpominky=[
            "Jak jste se vy dva poznali? Kdo koho první oslovil?",
            "Jak vypadala vaše svatba? Co se jedlo, kdo hrál k tanci?",
        ],
        vzkaz="Vzkaz pro vnoučata: co jste se v životě naučili a v žádné knížce to nestojí?",
        kviz_uvod="Velký týdenní kvíz – bez nahlížení dozadu! Kolik si toho pamatujete?",
        doplnovacka=[
            "Proč kohout kokrhá ještě za tmy? ____________________",
            "Co uviděl svatý Hubert mezi parožím jelena? ____________",
            "Na čem stojí Benátky? ____________________",
            "S jakou perutí létal Josef František? ______________",
            "Podle čeho mají brambory své jméno? ______________",
            "Kdy v severním Norsku nezapadá slunce? ____________",
        ],
        hadanka=dict(typ="pocty", nazev="Počty z dvora",
            radky=[
                "Na dvoře je 8 slepic a 3 kachny. Kolik mají dohromady nohou?",
                "Babička nasbírala 24 vajec a dává je do plat po deseti. Kolik plat naplní celých a kolik vajec zbude?",
                "Děda vyrazil na hon v 7:30 a vrátil se ve 13:15. Jak dlouho byl pryč?",
                "Kilo švestek stojí 40 Kč. Kolik zaplatíte za tři a půl kila?",
            ]),
        clanek=dict(nadpis="Emil a Dana – narození ve stejný den", odstavce=[
            "Emil a Dana Zátopkovi se narodili ve stejný den – 19. září 1922. On v Kopřivnici, ona ve Fryštátě u Karviné. Potkali se až jako dospělí sportovci a zůstali spolu celý život.",
            "Na olympiádě v Helsinkách v roce 1952 Emil vyhrál běh na 5 a 10 kilometrů a nakonec i maraton – který běžel vůbec poprvé v životě. Tři zlaté medaile na jedněch hrách! A Dana? Ta vyhrála hod oštěpem – ve stejný den, kdy Emil vyhrál pětku.",
            "Emil zemřel v roce 2000, Dana se dožila 97 let. Celý život táhli za jeden provaz – a když se jednomu nedařilo, druhý ho podržel.",
        ]),
        otazky=["Co měli Emil a Dana společného už od narození?", "Kolik zlatých medailí získal Emil v Helsinkách?"],
    ),
]

RESENI = {
    "Pondělí": ["Kvíz: 1b (asi 9 měsíců) · 2b (kůzle) · 3b (21 dní) · 4b (cepem) · 5a (kačer)",
                "Tajenka: SENO, TELE, OVES, DOJIT, OVCE, LOUKA, ANGREŠT → <b>STODOLA</b>",
                "Článek: v Japonsku · ten nejvyšší v pořadí (nejsilnější)"],
    "Úterý": ["Kvíz: 1b (barva) · 2a (světla) · 3b (kňour) · 4a (laň) · 5b (sv. Hubert)",
              "Nepatří: zajíc (nemá paroží) · bažant (je pták) · smrk (jehličnan) · netopýr (savec, ne pták)",
              "Přesmyčky: LIŠKA, JELEN, SOVA, SRNEC",
              "Článek: kříž · 3. listopadu"],
    "Středa": ["Kvíz: 1b (Řím) · 2a (Pisa) · 3b (Vesuv) · 4b (Tibera) · 5b (grazie)",
               "Spojovačka: Francie – Eiffelova věž · Nizozemsko – mlýny a tulipány · Egypt – pyramidy · Řecko – Akropolis · Švýcarsko – Alpy a sýr · Anglie – Big Ben",
               "Článek: dub a modřín · nedostane se k němu vzduch"],
    "Čtvrtek": ["Kvíz: 1a (28. 10. 1918) · 2b (Masaryk) · 3a (Plzeň) · 4a (Gabčík a Kubiš) · 5b (1945)",
                "Pořadí: 1 Vznik ČSR (1918) · 2 Mnichov (1938) · 3 Atentát (1942) · 4 Konec války (1945) · 5 Srpen 1968 · 6 Sametová revoluce (1989)",
                "Článek: s polskou 303. perutí · 17"],
    "Pátek": ["Pranostiky: čtyřicet · Martina · pole · hodinu · ledoví · koláče",
              "Článek: z Jižní Ameriky (z And) · podle Braniborska"],
    "Sobota": ["Kvíz: 1b (Austrálie) · 2b (Everest) · 3a (Černé) · 4c (New York) · 5a (Oslo)",
               "Tajenka: NIL, OCEÁN, RAKOUSKO, SAHARA, KLOKAN, OSTROV → <b>NORSKO</b>",
               "Článek: ledovce · polární záře"],
    "Neděle": ["Týdenní kvíz: má vnitřní „hodiny“ · kříž · na dřevěných kůlech · s polskou 303. perutí · podle Braniborska · v létě",
               "Počty: 22 nohou · 2 plata a 4 vejce zbudou · 5 hodin 45 minut · 140 Kč",
               "Článek: narodili se ve stejný den · tři"],
}

# ---------------------------------------------------------------- HTML
e = html.escape


def lines(n, cls="line"):
    return "".join(f'<div class="{cls}"></div>' for _ in range(n))


def tajenka(h):
    maxlen = max(len(w) for _, w in h["radky"])
    rows = []
    for clue, word in h["radky"]:
        cells = "".join(
            f'<td class="box{" key" if i == 0 else ""}"></td>' for i in range(len(word)))
        pad = "".join('<td class="nobox"></td>' for _ in range(maxlen - len(word)))
        rows.append(f'<tr><td class="clue">{e(clue)} <span class="cnt">({len(word)})</span></td>{cells}{pad}</tr>')
    return f'<table class="taj">{"".join(rows)}</table>'


def hadanka(h):
    t = h["typ"]
    out = [f'<h3>✎ {e(h["nazev"])}</h3>']
    if h.get("navod"):
        out.append(f'<p class="navod">{e(h["navod"])}</p>')
    if t == "tajenka":
        out.append(tajenka(h))
        out.append('<p class="taj-out">Tajenka: <span class="fill"></span></p>')
    elif t == "nepatri":
        out.append('<ol class="rada">' + "".join(f"<li>{e(r)}</li>" for r in h["radky"]) + "</ol>")
        out.append(f'<p class="navod">{e(h["presmycky_navod"])}</p>')
        out.append('<div class="presm">' + "".join(
            f'<div><b>{e(p)}</b> → <span class="fill short"></span></div>' for p in h["presmycky"]) + "</div>")
    elif t == "spojovacka":
        rows = "".join(
            f'<tr><td class="l">{e(a)} <span class="dot">●</span></td><td class="gap"></td>'
            f'<td class="r"><span class="dot">●</span> {e(b)}</td></tr>'
            for a, b in zip(h["leve"], h["prave"]))
        out.append(f'<table class="spoj">{rows}</table>')
    elif t == "poradi":
        out.append('<div class="poradi">' + "".join(
            f'<div><span class="numbox"></span> {e(r)}</div>' for r in h["radky"]) + "</div>")
    elif t == "seznam":
        out.append('<div class="seznam">' + " · ".join(e(p) for p in h["polozky"]) + "</div>")
        out.append('<p class="navod">Co si pamatujete (bez koukání!):</p>' + lines(3))
    elif t == "pocty":
        out.append('<ol class="pocty">' + "".join(
            f'<li>{e(r)}<div class="ans">Výsledek: <span class="fill short"></span></div></li>' for r in h["radky"]) + "</ol>")
    return "".join(out)


def kviz(d):
    out = ['<h3>? Kvíz</h3>']
    if d.get("kviz_uvod"):
        out.append(f'<p class="navod">{e(d["kviz_uvod"])}</p>')
    if d.get("kviz"):
        items = []
        for q, opts in d["kviz"]:
            o = "".join(f'<span class="opt"><span class="circ">{c}</span> {e(x)}</span>'
                        for c, x in zip("abc", opts))
            items.append(f'<li><div class="q">{e(q)}</div><div class="opts">{o}</div></li>')
        out.append('<ol class="kviz">' + "".join(items) + "</ol>")
    if d.get("doplnovacka"):
        out.append('<ol class="dopl">' + "".join(f"<li>{e(x)}</li>" for x in d["doplnovacka"]) + "</ol>")
    return "".join(out)


def den_html(i, d):
    vz = "".join(f'<li><div class="q">{e(q)}</div>{lines(2)}</li>' for q in d["vzpominky"])
    vzkaz = ""
    if d.get("vzkaz"):
        vzkaz = f'<div class="vzkaz"><div class="q"><b>{e(d["vzkaz"])}</b></div>{lines(4)}</div>'
    clanek = "".join(f"<p>{e(p)}</p>" for p in d["clanek"]["odstavce"])
    otazky = "".join(f'<li><div class="q">{e(q)}</div>{lines(1)}</li>' for q in d["otazky"])
    return f'''
<section class="page">
  <header class="dayhead"><span class="num">Den {i}</span><span class="dname">{e(d["den"])}</span>
    <span class="tema">{d["ikona"]} {e(d["tema"])}</span></header>
  <div class="ranni"><b>Ranní rozcvička:</b> {e(d["ranni"])}{lines(1)}</div>
  <h3>❦ Povídání a vzpomínky</h3>
  <p class="navod">Povídejte si spolu a pár slov zapište.</p>
  <ol class="vzp">{vz}</ol>
  {vzkaz}
  {kviz(d)}
</section>
<section class="page">
  <div class="hadanka">{hadanka(d["hadanka"])}</div>
  <article class="clanek"><h3>☕ Čtení ke kávě: {e(d["clanek"]["nadpis"])}</h3>{clanek}</article>
  <div class="potclanku"><b>Zakryjte článek a zkuste si vzpomenout:</b><ol>{otazky}</ol></div>
  <div class="denik"><h3>☾ Večer: co jsme dnes dělali</h3>
    <div class="dr"><span>Dopoledne:</span><div class="line"></div></div>
    <div class="dr"><span>Odpoledne:</span><div class="line"></div></div>
    <div class="dr"><span>Dnes nás potěšilo:</span><div class="line"></div></div>
  </div>
</section>'''


CSS = """
@page { size: A4; margin: 14mm 15mm 14mm 15mm; }
* { box-sizing: border-box; }
body { font-family: 'DejaVu Serif', serif; font-size: 13.5pt; line-height: 1.38; color: #1c1c1c; margin: 0; }
h1, h2, h3, .dayhead { font-family: 'DejaVu Sans', sans-serif; }
.page { page-break-after: always; break-after: page; }
.page:last-child { page-break-after: auto; }
h3 { font-size: 15pt; color: #2d5a35; margin: 3.5mm 0 1.5mm; border-bottom: 1.5px solid #2d5a35; padding-bottom: 1mm; }
.navod { margin: 0 0 2mm; font-style: italic; color: #333; }
.line { border-bottom: 1px solid #8a8a8a; height: 8.6mm; }
.dayhead { display: flex; align-items: baseline; gap: 5mm; border-bottom: 3px solid #7a4a1e; padding-bottom: 2mm; }
.dayhead .num { background: #7a4a1e; color: #fff; padding: 1mm 3mm; border-radius: 2mm; font-size: 13pt; font-weight: bold; }
.dayhead .dname { font-size: 26pt; font-weight: bold; color: #7a4a1e; }
.dayhead .tema { font-size: 16pt; margin-left: auto; color: #333; }
.ranni { margin-top: 4mm; background: #f4efe6; border-left: 4px solid #7a4a1e; padding: 2mm 3mm 0; }
ol { margin: 0; padding-left: 8mm; }
.vzp li { margin-bottom: 2mm; }
.q { font-weight: bold; }
.kviz li { margin-bottom: 2.6mm; }
.opts { display: flex; gap: 8mm; flex-wrap: wrap; margin-top: 0.5mm; }
.circ { display: inline-block; width: 7mm; height: 7mm; border: 1.5px solid #444; border-radius: 50%; text-align: center; line-height: 6.4mm; font-family: 'DejaVu Sans'; font-size: 11pt; }
.dopl li { margin-bottom: 3.2mm; }
.vzkaz { border: 2px dashed #7a4a1e; padding: 2mm 4mm; margin-top: 3mm; border-radius: 3mm; }
.taj { border-collapse: separate; border-spacing: 1mm; margin-left: -1.2mm; }
.taj .clue { padding-right: 3mm; width: 88mm; font-size: 12.5pt; }
.taj .cnt { color: #777; font-size: 11pt; }
.taj .box { width: 9mm; height: 9mm; border: 1.5px solid #444; }
.taj .box.key { background: #e9dcc5; border: 2.5px solid #7a4a1e; }
.taj .nobox { width: 9mm; }
.taj-out { margin-top: 2mm; font-weight: bold; }
.fill { display: inline-block; border-bottom: 1px solid #555; width: 70mm; height: 6mm; vertical-align: bottom; }
.fill.short { width: 45mm; }
.rada li { margin-bottom: 2mm; font-size: 14.5pt; letter-spacing: .3px; }
.presm { display: grid; grid-template-columns: 1fr 1fr; gap: 3mm 8mm; font-size: 14pt; }
.spoj { width: 100%; font-size: 14pt; border-collapse: collapse; }
.spoj td { padding: 2mm 0; }
.spoj .l { text-align: right; width: 35%; } .spoj .r { width: 45%; } .spoj .gap { width: 20%; }
.dot { color: #7a4a1e; }
.poradi div { margin-bottom: 1.6mm; font-size: 14pt; }
.numbox { display: inline-block; width: 9mm; height: 9mm; border: 1.5px solid #444; vertical-align: middle; margin-right: 3mm; }
.seznam { font-size: 17pt; font-weight: bold; text-align: center; border: 2px solid #2d5a35; border-radius: 3mm; padding: 3mm; line-height: 1.6; margin-bottom: 2mm; }
.pocty li { margin-bottom: 2.5mm; } .ans { margin-top: 1mm; }
.clanek p { font-size: 12.8pt; line-height: 1.33; margin: 0 0 1.5mm; text-align: justify; hyphens: auto; }
.potclanku { background: #eef3ec; padding: 2mm 4mm 1mm; border-radius: 2mm; margin-top: 2mm; }
.potclanku li { margin-bottom: 1mm; }
.denik .dr { display: flex; align-items: flex-end; gap: 3mm; } .denik .dr span { white-space: nowrap; font-weight: bold; }
.denik .dr .line { flex: 1; }
/* titulní strana */
.cover { text-align: center; padding-top: 30mm; }
.cover h1 { font-size: 40pt; color: #7a4a1e; margin: 0 0 4mm; }
.cover .sub { font-size: 19pt; color: #2d5a35; margin-bottom: 14mm; }
.cover .orn { font-size: 46pt; margin: 10mm 0; }
.cover .box { text-align: left; border: 2px solid #2d5a35; border-radius: 4mm; padding: 5mm 8mm; font-size: 14.5pt; margin: 0 6mm; }
.cover .box li { margin-bottom: 2mm; }
.cover .sign { margin-top: 12mm; font-size: 17pt; font-style: italic; }
.res h2 { font-size: 22pt; color: #7a4a1e; }
.res .d { margin-bottom: 4mm; font-size: 12.5pt; }
.res .d b.h { font-family: 'DejaVu Sans'; color: #2d5a35; }
.res .d div { margin-left: 5mm; }
"""

COVER = """
<section class="page cover">
  <div class="orn">🌻</div>
  <h1>Týden pro paměť</h1>
  <div class="sub">pro babičku a dědu · týden č. 1</div>
  <div class="box">
    <b>Jak na to:</b>
    <ul>
      <li>Každý den jeden list. Nejlépe ráno ke kávě, v klidu a spolu.</li>
      <li>Nic se nehodnotí, nikdo nezkouší. Když něco nevíte, nevadí – přeskočte to, nebo se podívejte do řešení na konci.</li>
      <li>Nejdůležitější je <b>povídání</b>. Vy víte věci, které my mladší už nevíme – každá zapsaná vzpomínka je pro nás poklad.</li>
      <li>Večer zapište pár slov o tom, co jste ten den dělali. Druhý den ráno si to zkusíte vybavit.</li>
    </ul>
  </div>
  <div class="sign">S láskou, vaše vnučka</div>
</section>
"""


def build():
    body = COVER + "".join(den_html(i + 1, d) for i, d in enumerate(DNY))
    res = "".join(
        f'<div class="d"><b class="h">{d}</b>' + "".join(f"<div>{r}</div>" for r in rs) + "</div>"
        for d, rs in RESENI.items())
    body += f'<section class="page res"><h2>Řešení</h2>{res}</section>'
    doc = f'<!doctype html><html lang="cs"><head><meta charset="utf-8"><title>Týden pro paměť</title><style>{CSS}</style></head><body>{body}</body></html>'
    (OUT / "tyden-1.html").write_text(doc, encoding="utf-8")


if __name__ == "__main__":
    build()
