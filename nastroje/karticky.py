#!/usr/bin/env python3
"""Rozseká studijní markdown na malé tištěné kartičky (výchozí 55 × 45 mm).

Text se NEKRÁTÍ — delší otázka se rozloží na víc navazujících kartiček
(v hlavičce je „3/7"). Sazbu do pevných rámečků dělá až prohlížeč: JavaScript
přidává slovo po slovu (binárním půlením) a jakmile by karta přetekla, založí
další. Proto se nic neuřízne.

Tabulky se převádějí na řádky „**první buňka** — druhá · třetí" — třísloupcová
tabulka je na 5 cm široké kartičce nečitelná, ale slova zůstávají všechna.

Použití:
    python3 nastroje/karticky.py vstup.md vystup.pdf [pt] [šířka_mm] [výška_mm]
"""

import html
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from md2gdoc import inline as _inline  # noqa: E402
from md2pdf import najdi_chromium  # noqa: E402


def inline(s: str) -> str:
    return _inline(s).replace('font-size:10pt', 'font-size:inherit').replace('\\*', '*')


def rozbor(md: str):
    """Markdown → seznam otázek [{'id':..., 'nazev':..., 'bloky':[html, ...]}]."""
    otazky, akt = [], None
    lines = md.split("\n")
    i = 0
    while i < len(lines):
        ln = lines[i].rstrip()
        if ln.startswith("## "):
            hlava = ln[3:].strip()
            cislo, _, nazev = hlava.partition("·")
            akt = {"id": cislo.strip(), "nazev": nazev.strip(), "bloky": []}
            akt["bloky"].append(
                f'<p class="nz1"><b>{inline(cislo.strip())} · {inline(nazev.strip())}</b></p>')
            otazky.append(akt)
            i += 1
            continue
        if akt is None or ln.startswith("# ") or ln.startswith("---") or not ln.strip():
            i += 1
            continue
        # tabulka
        if ln.startswith("|"):
            radky = []
            while i < len(lines) and lines[i].startswith("|"):
                radky.append(lines[i])
                i += 1
            bunky = [[c.strip() for c in r.strip().strip("|").split("|")] for r in radky]
            bunky = [b for b in bunky if not all(set(c) <= set("-: ") for c in b)]
            if len(bunky) > 1:
                hlava_t = " · ".join(inline(x) for x in bunky[0] if x.strip())
                if hlava_t:
                    akt["bloky"].append(f'<p class="th">{hlava_t}</p>')
            for b in bunky[1:] if len(bunky) > 1 else bunky:
                b = [x for x in b if x not in ("", "—")]
                if not b:
                    continue
                prvni = inline(b[0])
                zbytek = " · ".join(inline(x) for x in b[1:])
                akt["bloky"].append(f'<p class="t"><b>{prvni}</b>{" — " + zbytek if zbytek else ""}</p>')
            continue
        # odrážka
        m = re.match(r"^(\s*)[-*] +(.*)$", ln)
        if m:
            hloubka = len(m.group(1)) // 2
            text = m.group(2)
            i += 1
            while i < len(lines) and lines[i].startswith("  ") and not re.match(r"^\s*[-*] ", lines[i]) and lines[i].strip():
                text += " " + lines[i].strip()
                i += 1
            akt["bloky"].append(f'<p class="b{min(hloubka,1)}">{inline(text)}</p>')
            continue
        akt["bloky"].append(f'<p>{inline(ln.strip())}</p>')
        i += 1
    return otazky


SABLONA = """<!doctype html><html><head><meta charset="utf-8"><title>Kartičky</title>
<style>
@page {{ size: A4; margin: {mtop}mm {mside}mm; }}
* {{ box-sizing: border-box; }}
body {{ margin: 0; font-family: Calibri, Carlito, Arial, sans-serif; }}
#mriz {{ display: flex; flex-wrap: wrap; width: {gw}mm; }}
.karta {{ width: {w}mm; height: {h}mm; border: 0.25pt solid #9aa; padding: 1.4mm 1.6mm;
          overflow: hidden; break-inside: avoid; }}
.hl {{ font-size: {hpt}pt; font-weight: 700; color: #123; border-bottom: 0.25pt solid #bcc;
       height: {hlh}mm; margin-bottom: 0.5mm; display: flex; justify-content: space-between;
       gap: 1.5mm; line-height: 1.05; overflow: hidden; }}
.hl .nz {{ flex: 1; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
.hl .cis {{ white-space: nowrap; color: #667; font-weight: 600; }}
.telo {{ font-size: {pt}pt; line-height: 1.16; height: calc(100% - {hh}mm); overflow: hidden; }}
.telo p {{ margin: 0 0 0.5mm 0; }}
.telo p.b0 {{ padding-left: 1.5mm; text-indent: -1.5mm; }}
.telo p.b0::before {{ content: "▪ "; color: #789; }}
.telo p.b1 {{ padding-left: 3.2mm; text-indent: -1.5mm; }}
.telo p.b1::before {{ content: "– "; color: #789; }}
.telo p.t {{ padding-left: 1.5mm; border-left: 0.5pt solid #cdd; }}
.telo p.th {{ color: #567; font-style: italic; margin-top: 0.6mm; }}
.telo p.nz1 {{ color: #123; margin-bottom: 0.8mm; }}
b {{ font-weight: 700; }}
code {{ font-family: inherit; }}
#zdroj {{ display: none; }}
</style></head><body>
<div id="mriz"></div>
<div id="zdroj">{data}</div>
<script>
const KARTY = {json};
const mriz = document.getElementById('mriz');

function slovaUzlu(node, pole) {{
  if (node.nodeType === 3) {{
    const casti = node.nodeValue.split(/(\\s+)/).filter(s => s.length);
    for (const c of casti) if (c.trim()) pole.push(c);
  }} else for (const ch of node.childNodes) slovaUzlu(ch, pole);
}}

function stavba(src, limit, stav) {{
  // vrátí klon `src` obsahující jen slova s indexem < limit (stav.i počítá slova)
  if (src.nodeType === 3) {{
    const casti = src.nodeValue.split(/(\\s+)/).filter(s => s.length);
    let out = '';
    for (const c of casti) {{
      if (!c.trim()) {{ out += c; continue; }}
      if (stav.i >= limit) return out ? document.createTextNode(out) : null;
      out += c; stav.i++;
    }}
    return document.createTextNode(out);
  }}
  const kl = src.cloneNode(false);
  for (const ch of src.childNodes) {{
    const d = stavba(ch, limit, stav);
    if (d) kl.appendChild(d);
    if (stav.i >= limit) break;
  }}
  return kl.childNodes.length ? kl : null;
}}

function novaKarta(id, nazev) {{
  const k = document.createElement('div'); k.className = 'karta';
  const hl = document.createElement('div'); hl.className = 'hl';
  hl.innerHTML = '<span class="nz"></span><span class="cis"></span>';
  const t = document.createElement('div'); t.className = 'telo';
  k.appendChild(hl); k.appendChild(t); mriz.appendChild(k);
  k.dataset.id = id; k.dataset.nazev = nazev;
  return k;
}}

let vyrobene = [];
for (const q of KARTY) {{
  let karta = novaKarta(q.id, q.nazev), telo = karta.querySelector('.telo');
  let skupina = [karta];
  for (const bl of q.bloky) {{
    const tmp = document.createElement('div'); tmp.innerHTML = bl;
    let src = tmp.firstElementChild;
    while (src) {{
      const slova = []; slovaUzlu(src, slova);
      const celkem = slova.length;
      // zkus celý blok
      telo.appendChild(stavba(src, celkem, {{i:0}}));
      if (telo.scrollHeight <= telo.clientHeight) {{ src = null; break; }}
      telo.lastChild.remove();
      // binárně najdi, kolik slov se vejde
      let lo = 0, hi = celkem;
      while (lo < hi) {{
        const mid = Math.ceil((lo + hi) / 2);
        const zk = stavba(src, mid, {{i:0}});
        telo.appendChild(zk);
        if (telo.scrollHeight <= telo.clientHeight) lo = mid; else hi = mid - 1;
        zk.remove();
      }}
      if (lo > 0) telo.appendChild(stavba(src, lo, {{i:0}}));
      if (lo >= celkem) {{ src = null; break; }}
      // zbytek na novou kartu
      const zbytek = document.createElement('div');
      const cely = stavba(src, celkem, {{i:0}});
      zbytek.appendChild(cely);
      // odeber prvních `lo` slov z klonu
      const vse = []; slovaUzlu(cely, vse);
      let odebrat = lo;
      (function orez(node) {{
        if (odebrat <= 0) return;
        if (node.nodeType === 3) {{
          const casti = node.nodeValue.split(/(\\s+)/).filter(s => s.length);
          let out = '';
          for (const c of casti) {{
            if (!c.trim()) {{ if (odebrat <= 0) out += c; continue; }}
            if (odebrat > 0) {{ odebrat--; continue; }}
            out += c;
          }}
          node.nodeValue = out;
          return;
        }}
        for (const ch of Array.from(node.childNodes)) orez(ch);
      }})(cely);
      karta = novaKarta(q.id, q.nazev); telo = karta.querySelector('.telo'); skupina.push(karta);
      src = cely;
      if (lo === 0 && celkem > 0) {{ /* pojistka proti zacyklení */ }}
    }}
  }}
  skupina.forEach((k, idx) => {{
    // na první kartě je celý název hned pod hlavičkou, tak ho tam neopakujeme
    const nz = k.dataset.nazev.length > 40 ? k.dataset.nazev.slice(0, 39) + '…' : k.dataset.nazev;
    k.querySelector('.nz').textContent = idx === 0 ? k.dataset.id : k.dataset.id + ' · ' + nz;
    k.querySelector('.cis').textContent = skupina.length > 1 ? (idx + 1) + '/' + skupina.length : '';
  }});
  vyrobene.push(skupina.length);
}}
document.title = 'Kartičky — ' + mriz.children.length + ' karet';
</script></body></html>"""


def main():
    a = sys.argv[1:]
    vstup, vystup = Path(a[0]), Path(a[1])
    pt = float(a[2]) if len(a) > 2 else 6.0
    w = float(a[3]) if len(a) > 3 else 55.0
    h = float(a[4]) if len(a) > 4 else 45.0
    import json as _json

    otazky = rozbor(vstup.read_text(encoding="utf-8"))
    sloupcu = int(194 // w)
    radku = int(281 // h)
    gw = sloupcu * w
    mside = round((210 - gw) / 2, 2)
    mtop = round((297 - radku * h) / 2, 2)
    stranka = SABLONA.format(
        json=_json.dumps(otazky, ensure_ascii=False), data="", w=w, h=h, gw=gw,
        mside=mside, mtop=mtop, pt=pt, hpt=round(pt * 1.0, 2),
        hlh=round(pt * 0.42, 2), hh=round(pt * 0.42 + 0.9, 2),
    )
    docasne = vystup.with_suffix(".karty.html")
    docasne.write_text(stranka, encoding="utf-8")
    subprocess.run(
        [najdi_chromium(), "--headless", "--disable-gpu", "--no-sandbox",
         "--no-pdf-header-footer", "--virtual-time-budget=600000",
         f"--print-to-pdf={vystup}", docasne.resolve().as_uri()],
        check=True, capture_output=True, timeout=900)
    print(f"{vystup} · {vystup.stat().st_size // 1024} kB · mřížka {sloupcu}×{radku} = {sloupcu*radku} karet/list")


if __name__ == "__main__":
    main()
