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
    s = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", s)
    return s


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
            body = " ".join(x for x in buf if x)
            color = CRIT if "⚠️" in body else ACCENT
            out.append(f'<p style="border-left:3px solid {color};padding-left:12px;'
                       f'margin:10px 0">{inline(body)}</p>')
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
