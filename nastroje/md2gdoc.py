#!/usr/bin/env python3
"""Převede markdown z vaultu na HTML, které Disk umí přijmout jako Google dokument.

Použití:  python3 nastroje/md2gdoc.py vstup.md vystup.html "Titulek"

Proč HTML a ne .docx: nahrání .docx s konverzí Disk odmítá chybou
„Invalid conversion requested". HTML se převede na nativní Google dokument
i s tabulkami. Viz pravidlo „Výstupy vždy jako Google dokument" v CLAUDE.md.
"""
import html
import re
import sys

ACCENT = "#1B6B5F"
CRIT = "#9C3628"
MUTED = "#6E837E"
LINE = "#D9E2DE"


def inline(s: str) -> str:
    s = html.escape(s)
    s = re.sub(r"`([^`]+)`", r'<code style="background:#F0F4F2;padding:1px 4px;'
                            r'border-radius:2px;font-size:10pt">\1</code>', s)
    # ***tučná kurzíva*** musí jít první, jinak ji sežere pravidlo pro **tučné**
    s = re.sub(r"\*\*\*(.+?)\*\*\*", r"<b><i>\1</i></b>", s)
    # **tučné** smí obsahovat *kurzívu* uvnitř — proto lookahead a rekurze do skupiny
    s = re.sub(r"\*\*(.+?)\*\*(?!\*)", lambda m: f"<b>{_kurziva(m.group(1))}</b>", s)
    s = _kurziva(s)
    return s


def _kurziva(s: str) -> str:
    return re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", s)


def convert(md: str) -> str:
    out, i = [], 0
    lines = md.split("\n")
    while i < len(lines):
        ln = lines[i]

        # tabulka
        if ln.strip().startswith("|") and i + 1 < len(lines) and re.match(
                r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1]):
            head = [c.strip() for c in ln.strip().strip("|").split("|")]
            i += 2
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            t = ['<table style="border-collapse:collapse;width:100%;border:1px solid '
                 + LINE + ';margin:10px 0">']
            t.append("<tr>" + "".join(
                f'<td style="background:{ACCENT};color:#fff;border:1px solid {LINE};'
                f'padding:5px 8px"><b>{inline(c)}</b></td>' for c in head) + "</tr>")
            for n, r in enumerate(rows):
                bg = "#F4F7F5" if n % 2 else "#ffffff"
                t.append("<tr>" + "".join(
                    f'<td style="background:{bg};border:1px solid {LINE};'
                    f'padding:5px 8px">{inline(c)}</td>' for c in r) + "</tr>")
            t.append("</table>")
            out.append("".join(t))
            continue

        # citace / zvýrazněný blok
        if ln.strip().startswith(">"):
            buf = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip().lstrip(">").strip())
                i += 1
            color = CRIT if "⚠️" in " ".join(buf) else ACCENT

            # uvnitř citace se často používá nadpis (`> ### Titulek`) a odrážky —
            # bez tohohle by se vypsaly i s ### a - jako holý text
            casti, odstavec, seznam = [], [], []

            def zavri():
                if seznam:
                    casti.append("<ul style='margin:4px 0'>"
                                 + "".join(f"<li>{inline(x)}</li>" for x in seznam)
                                 + "</ul>")
                    seznam.clear()
                if odstavec:
                    casti.append(f"<div style='margin:4px 0'>{inline(' '.join(odstavec))}</div>")
                    odstavec.clear()

            for radek in buf:
                nadpis = re.match(r"^(#{1,4})\s+(.*)$", radek)
                if nadpis:
                    zavri()
                    velikost = {1: "13pt", 2: "12.5pt", 3: "12pt", 4: "11pt"}[len(nadpis.group(1))]
                    casti.append(f"<div style='font-size:{velikost};color:{color};"
                                 f"font-weight:bold;margin:4px 0'>{inline(nadpis.group(2))}</div>")
                elif re.match(r"^[-*]\s+", radek):
                    if odstavec:
                        zavri()
                    seznam.append(re.sub(r"^[-*]\s+", "", radek))
                elif radek:
                    if seznam:
                        zavri()
                    odstavec.append(radek)
                else:
                    zavri()
            zavri()

            out.append(f'<div style="border-left:3px solid {color};padding-left:12px;'
                       f'margin:10px 0">{"".join(casti)}</div>')
            continue

        # seznam
        if re.match(r"^\s*[-*] ", ln):
            items = []
            while i < len(lines) and re.match(r"^\s*[-*] ", lines[i]):
                items.append(inline(re.sub(r"^\s*[-*] ", "", lines[i])))
                i += 1
            out.append("<ul>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>")
            continue

        if re.match(r"^\s*\d+\. ", ln):
            items = []
            while i < len(lines) and re.match(r"^\s*\d+\. ", lines[i]):
                items.append(inline(re.sub(r"^\s*\d+\. ", "", lines[i])))
                i += 1
            out.append("<ol>" + "".join(f"<li>{x}</li>" for x in items) + "</ol>")
            continue

        if ln.strip() == "---":
            out.append(f'<hr style="border:0;border-top:1px solid {LINE};margin:18px 0">')
        elif ln.startswith("### "):
            out.append(f'<h3 style="font-size:12pt;margin:14px 0 4px">{inline(ln[4:])}</h3>')
        elif ln.startswith("## "):
            out.append(f'<h2 style="font-size:14pt;color:{ACCENT};margin:18px 0 6px">'
                       f"{inline(ln[3:])}</h2>")
        elif ln.startswith("# "):
            out.append(f'<h1 style="font-size:18pt;color:{ACCENT};margin:24px 0 8px;'
                       f'border-bottom:1px solid {LINE};padding-bottom:4px">'
                       f"{inline(ln[2:])}</h1>")
        elif ln.strip():
            out.append(f"<p>{inline(ln)}</p>")
        i += 1
    return "".join(out)


def main() -> None:
    src, dst = sys.argv[1], sys.argv[2]
    title = sys.argv[3] if len(sys.argv) > 3 else "Dokument"
    body = convert(open(src, encoding="utf-8").read())
    doc = (f"<html><head><meta charset='utf-8'><title>{html.escape(title)}</title></head>"
           f"<body style=\"font-family:Calibri,Arial,sans-serif;font-size:11pt;"
           f"line-height:1.45\">{body}</body></html>")
    open(dst, "w", encoding="utf-8").write(doc)
    print(f"{dst} · {len(doc)} B")


if __name__ == "__main__":
    main()
