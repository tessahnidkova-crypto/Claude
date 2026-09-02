#!/usr/bin/env python3
"""Vzorek tří paměťových scén — na odsouhlasení stylu, než se udělá všech 136."""
import sys, pathlib
KOREN = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(KOREN / "nastroje"))
from scenka import scenka

O = []
def S(*a, **k): O.append(scenka(*a, **k))

S("87", "Tetracykliny, amfenikoly",
  "MLÉKÁRNA, KDE SE BARVÍ ZUBY — všechno, co tam je, na sebe váže vápník.",
  "krajina",
  [("🥛", 0.12, 0.68, 74, "Konev mléka", False,
    "Chelatace s Ca²⁺, Mg²⁺, Al³⁺ a Fe — nezapíjet mlékem, neužívat s antacidy, železem a vápníkem."),
   ("🦷", 0.34, 0.72, 88, "Obarvený zub", True,
    "Ukládá se do mineralizující tkáně; šedohnědé zbarvení je UVNITŘ skloviny a dentinu — bělením ani leštěním se neodstraní."),
   ("👶", 0.53, 0.70, 70, "Dítě u plotu", True,
    "Kontraindikace do 8 let věku, v graviditě a při kojení — hypoplazie skloviny a zbarvení zubů."),
   ("☀️", 0.80, 0.20, 58, "Pálící slunce", False,
    "Fotosenzitivita — pacienta je nutné varovat před sluněním."),
   ("🎯", 0.70, 0.66, 62, "Terč s číslem 30", False,
    "Blokáda 30S podjednotky ribozomu = PROTEOSYNTÉZA, nikoli buněčná stěna. Bakteriostatické."),
   ("🕷️", 0.88, 0.74, 54, "Klíště a pavouk", False,
    "Široké spektrum včetně atypických: chlamydie, mykoplazmata, borrelie, rickettsie. Doxycyklin je hlavní zástupce."),
   ("👼", 0.22, 0.28, 56, "Šedé miminko na obloze", True,
    "Amfenikoly — chloramfenikol blokuje 50S. Gray baby syndrom u novorozence a aplastická anemie (typ B).")],
  "Ve zdroji katedry je u tetracyklinů uvedena inhibice buněčné stěny — to je chyba. Stěnu blokují betalaktamy a glykopeptidy.")

S("39", "Parasympatolytika",
  "VYPRAHLÁ POUŠŤ — atropin vysušil krajinu i člověka: sucho, horko, rudá kůže, rozšířené zorničky.",
  "poust",
  [("🏜️", 0.13, 0.70, 76, "Vyschlá půda", False,
    "Blokáda muskarinových receptorů — sucho v ústech, vyschlé sliznice, zástava pocení („suchý jako kost“)."),
   ("🌡️", 0.30, 0.66, 62, "Rozpálený teploměr", True,
    "Bez pocení stoupá teplota — hypertermie, u dětí nebezpečná („horký jako pec“). Kůže je suchá a zarudlá."),
   ("👁️", 0.47, 0.28, 66, "Obrovské oko na obloze", True,
    "Mydriáza a paralýza akomodace. ⚠️ Kontraindikací je glaukom s uzavřeným úhlem — rozšířená duhovka uzavře komorový úhel."),
   ("💓", 0.47, 0.68, 60, "Splašené srdce", False,
    "Blokáda M2 v srdci → tachykardie. Atropin se proto podává u bradykardie."),
   ("🚽", 0.64, 0.70, 58, "Zamčený záchod", False,
    "Retence moči (pozor u hyperplazie prostaty) a zácpa až paralytický ileus."),
   ("🎩", 0.80, 0.64, 66, "Šílený kloboučník", True,
    "Centrální anticholinergní syndrom — neklid, zmatenost, delirium. Antidotem je FYSOSTIGMIN (terciární amin, projde do CNS)."),
   ("🫁", 0.90, 0.30, 52, "Rozepnuté plíce", False,
    "Ipratropium a tiotropium inhalačně u CHOPN a astmatu — bronchodilatace bez systémových účinků.")],
  "Butylskopolamin je KVARTÉRNÍ amin — neprojde do CNS, takže neseduje ani nevyvolá delirium. Atropin a skopolamin (terciární) ano.")

S("77", "Perorální antikoagulancia",
  "ZELINÁŘSTVÍ S PAVOUČÍ SÍTÍ — čím víc zeleniny v košíku, tím hůř warfarin funguje.",
  "pokoj",
  [("🥬", 0.12, 0.66, 76, "Bedna se zelím", False,
    "Warfarin je antagonista vitaminu K — listová zelenina a brokolice jeho účinek SNIŽUJÍ. Účinek se sleduje pomocí INR."),
   ("🕸️", 0.31, 0.30, 70, "Pavučina nad pultem", False,
    "Blokuje vitamin K-epoxidreduktázu → chybí faktory II, VII, IX a X."),
   ("⏳", 0.30, 0.70, 58, "Přesýpací hodiny", True,
    "Nástup trvá 3–5 dní. Nejkratší poločas mají proteiny C a S — proto na začátku hrozí PARADOXNÍ trombóza a kožní nekróza; překrývá se heparinem."),
   ("💊", 0.50, 0.68, 60, "Lahvička antibiotik", True,
    "Antibiotika likvidují střevní bakterie tvořící vitamin K → INR stoupá. Totéž amiodaron, metronidazol, azoly, NSA a alkohol."),
   ("🤰", 0.66, 0.66, 62, "Těhotná zákaznice", True,
    "⚠️ Warfarin je v graviditě teratogenní — tam patří nízkomolekulární heparin."),
   ("💉", 0.83, 0.66, 58, "Injekce vitaminu K", False,
    "Antidotum warfarinu: vitamin K, při závažném krvácení koncentrát protrombinového komplexu."),
   ("🎯", 0.88, 0.28, 54, "Terč Xa a IIa", False,
    "DOAC: dabigatran (přímý inhibitor trombinu, antidotum idarucizumab) a xabany — rivaroxaban, apixaban, edoxaban (inhibitory Xa, antidotum andexanet alfa). Fixní dávka, bez monitorace.")],
  "U mechanické chlopenní náhrady a u antifosfolipidového syndromu zůstává warfarin jedinou možností — DOAC tam selhávají.")

md = "\n<div style=\"break-after:page\"></div>\n".join(O)
open(KOREN / 'Projekty/Studium/Predmety/Farmakologie/minimum/SCENY-VZOREK.md','w').write(md)
print('ok')
