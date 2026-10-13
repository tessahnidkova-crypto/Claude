# -*- coding: utf-8 -*-
INK="#16323B"; SEA="#0F8B8D"; STAMP="#E4572E"; SUN="#F2B028"; W="#FFFFFF"; GREY="#9CB3B8"
S=4  # stroke

def _fr(d,fill=W,st=INK,w=S):
    return f'<path d="{d}" fill="{fill}" stroke="{st}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round"/>'

ICONS4 = {
# --- pes ---
"i-dog": (f'<ellipse cx="46" cy="62" rx="26" ry="17" fill="{SUN}" stroke="{INK}" stroke-width="{S}"/>'
 f'<circle cx="74" cy="44" r="16" fill="{SUN}" stroke="{INK}" stroke-width="{S}"/>'
 + _fr("M64 32 l-4 -14 l13 7 Z", SUN)
 + _fr("M84 32 l4 -14 l-13 7 Z", SUN)
 + f'<circle cx="70" cy="42" r="2.6" fill="{INK}"/><circle cx="80" cy="42" r="2.6" fill="{INK}"/>'
 + f'<ellipse cx="75" cy="50" rx="4" ry="3" fill="{INK}"/>'
 + _fr("M22 62 q-12 -6 -10 -20", "none")
 + f'<line x1="34" y1="78" x2="34" y2="88" stroke="{INK}" stroke-width="{S}" stroke-linecap="round"/>'
 + f'<line x1="58" y1="78" x2="58" y2="88" stroke="{INK}" stroke-width="{S}" stroke-linecap="round"/>'),
# --- kocka ---
"i-cat": (f'<ellipse cx="46" cy="64" rx="24" ry="16" fill="{GREY}" stroke="{INK}" stroke-width="{S}"/>'
 f'<circle cx="72" cy="44" r="15" fill="{GREY}" stroke="{INK}" stroke-width="{S}"/>'
 + _fr("M61 34 l-2 -14 l12 6 Z", GREY) + _fr("M83 34 l2 -14 l-12 6 Z", GREY)
 + f'<circle cx="67" cy="43" r="2.4" fill="{INK}"/><circle cx="78" cy="43" r="2.4" fill="{INK}"/>'
 + f'<path d="M72.5 48 l-3 3 M72.5 48 l3 3" stroke="{INK}" stroke-width="3" fill="none" stroke-linecap="round"/>'
 + _fr("M22 62 q-14 -10 -6 -30", "none")
 + f'<line x1="36" y1="79" x2="36" y2="88" stroke="{INK}" stroke-width="{S}" stroke-linecap="round"/>'
 + f'<line x1="58" y1="79" x2="58" y2="88" stroke="{INK}" stroke-width="{S}" stroke-linecap="round"/>'),
# --- mobil ---
"i-mobile": (_fr("M34 10 h32 a7 7 0 0 1 7 7 v66 a7 7 0 0 1 -7 7 h-32 a7 7 0 0 1 -7 -7 v-66 a7 7 0 0 1 7 -7 Z", SEA)
 + _fr("M34 23 h32 v50 h-32 Z", W)
 + f'<circle cx="50" cy="80" r="4" fill="{W}" stroke="{INK}" stroke-width="2.5"/>'),
# --- hodinky ---
"i-watch": (_fr("M38 18 h24 l-3 16 h-18 Z", STAMP) + _fr("M38 82 h24 l-3 -16 h-18 Z", STAMP)
 + f'<circle cx="50" cy="50" r="22" fill="{W}" stroke="{INK}" stroke-width="{S}"/>'
 + f'<path d="M50 38 v12 h9" stroke="{INK}" stroke-width="{S}" fill="none" stroke-linecap="round"/>'),
# --- kniha ---
"i-book": (_fr("M14 22 q18 -8 36 0 v50 q-18 -8 -36 0 Z", SUN)
 + _fr("M86 22 q-18 -8 -36 0 v50 q18 -8 36 0 Z", W)
 + f'<line x1="50" y1="22" x2="50" y2="72" stroke="{INK}" stroke-width="{S}"/>'),
# --- destnik ---
"i-umbrella": (_fr("M8 50 a42 42 0 0 1 84 0 Z", STAMP)
 + f'<line x1="50" y1="50" x2="50" y2="80" stroke="{INK}" stroke-width="{S}" stroke-linecap="round"/>'
 + _fr("M50 80 a9 9 0 0 0 16 -5", "none")
 + f'<path d="M8 50 q14 -12 28 0 q14 -12 28 0 q14 -12 28 0" fill="none" stroke="{INK}" stroke-width="{S}" stroke-linejoin="round"/>'),
# --- dum ---
"i-house": (_fr("M50 12 L90 46 H10 Z", STAMP)
 + _fr("M20 46 h60 v40 h-60 Z", W)
 + _fr("M42 86 v-22 h16 v22 Z", SEA)
 + f'<rect x="26" y="54" width="12" height="12" fill="{SUN}" stroke="{INK}" stroke-width="3"/>'
 + f'<rect x="62" y="54" width="12" height="12" fill="{SUN}" stroke="{INK}" stroke-width="3"/>'),
# --- sourozenec (brother/sister spolecne) ---
"i-sibling": (f'<circle cx="34" cy="34" r="14" fill="{SEA}" stroke="{INK}" stroke-width="{S}"/>'
 + _fr("M16 82 v-16 a18 18 0 0 1 36 0 v16 Z", SEA)
 + f'<circle cx="70" cy="40" r="12" fill="{STAMP}" stroke="{INK}" stroke-width="{S}"/>'
 + _fr("M52 82 l18 -26 l18 26 Z", STAMP)),
# --- zaskrtnuto / ne (pro have / haven't) ---
"i-yes": (f'<circle cx="50" cy="50" r="38" fill="#EAF6EF" stroke="#2E7D4F" stroke-width="5"/>'
 + f'<path d="M32 52 l12 13 l25 -29" fill="none" stroke="#2E7D4F" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>'),
"i-no": (f'<circle cx="50" cy="50" r="38" fill="#FFF1EC" stroke="{STAMP}" stroke-width="5"/>'
 + f'<path d="M35 35 l30 30 M65 35 l-30 30" fill="none" stroke="{STAMP}" stroke-width="8" stroke-linecap="round"/>'),
# --- tuzka ---
"i-pencil": (_fr("M22 78 l6 -20 l38 -38 l14 14 l-38 38 Z", SUN)
 + _fr("M66 20 l8 -8 a7 7 0 0 1 10 0 l4 4 a7 7 0 0 1 0 10 l-8 8 Z", STAMP)
 + f'<path d="M22 78 l6 -20 l8 8 Z" fill="{INK}"/>'),
# --- rodokmen ---
"i-tree": (f'<line x1="50" y1="14" x2="50" y2="30" stroke="{INK}" stroke-width="5"/>'
 + f'<line x1="22" y1="30" x2="78" y2="30" stroke="{INK}" stroke-width="5"/>'
 + f'<line x1="22" y1="30" x2="22" y2="44" stroke="{INK}" stroke-width="5"/>'
 + f'<line x1="78" y1="30" x2="78" y2="44" stroke="{INK}" stroke-width="5"/>'
 + f'<circle cx="50" cy="14" r="8" fill="{STAMP}" stroke="{INK}" stroke-width="{S}"/>'
 + f'<circle cx="22" cy="54" r="10" fill="{SEA}" stroke="{INK}" stroke-width="{S}"/>'
 + f'<circle cx="78" cy="54" r="10" fill="{SUN}" stroke="{INK}" stroke-width="{S}"/>'),
}
