# -*- coding: utf-8 -*-
INK="#16323B"; SEA="#0F8B8D"; STAMP="#E4572E"; SUN="#F2B028"; W="#FFFFFF"

def _w(cx,cy,r,fill):   # postava se sukní
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{INK}" stroke-width="4"/>'
            f'<path d="M{cx-r-6} {cy+r+30} L{cx} {cy+r+2} L{cx+r+6} {cy+r+30} Z" '
            f'fill="{fill}" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>')
def _m(cx,cy,r,fill):   # postava s rameny
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{INK}" stroke-width="4"/>'
            f'<path d="M{cx-r-4} {cy+r+30} v-16 a{r+4} {r+4} 0 0 1 {2*r+8} 0 v16 Z" '
            f'fill="{fill}" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>')

FAM_ICONS = {
"i-mother": _w(50,32,16,STAMP),
"i-father": _m(50,32,16,SEA),
"i-parents": _w(30,34,13,STAMP) + _m(70,34,13,SEA),
"i-children": _m(30,40,11,SUN) + _w(70,40,11,SEA),
"i-cousin": (f'<line x1="50" y1="14" x2="50" y2="30" stroke="{INK}" stroke-width="4"/>'
   f'<line x1="24" y1="30" x2="76" y2="30" stroke="{INK}" stroke-width="4"/>'
   f'<line x1="24" y1="30" x2="24" y2="40" stroke="{INK}" stroke-width="4"/>'
   f'<line x1="76" y1="30" x2="76" y2="40" stroke="{INK}" stroke-width="4"/>'
   + _m(24,50,10,SEA) + _w(76,50,10,SUN)),
"i-whose": (f'<path d="M26 72 h48 a6 6 0 0 0 6 -6 v-22 a6 6 0 0 0 -6 -6 h-48 a6 6 0 0 0 -6 6 v22 '
   f'a6 6 0 0 0 6 6 Z" fill="{SEA}" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>'
   f'<path d="M40 38 v-6 a10 10 0 0 1 20 0 v6" fill="none" stroke="{INK}" stroke-width="4"/>'
   f'<text x="50" y="66" font-family="sans-serif" font-size="30" font-weight="bold" '
   f'fill="{W}" text-anchor="middle">?</text>'),
}
