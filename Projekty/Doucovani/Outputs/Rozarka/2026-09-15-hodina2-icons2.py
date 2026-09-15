# -*- coding: utf-8 -*-
# Nové ikony pro hodinu 2 — činnosti. viewBox 0 0 100 100, stejný styl jako hodina 1.
INK="#16323B"; SEA="#0F8B8D"; STAMP="#E4572E"; SUN="#F2B028"; WHITE="#FFFFFF"

NEW = {
"i-run": f'''
  <circle cx="60" cy="18" r="10" fill="{INK}"/>
  <path d="M56 30 L44 52 L56 60 L52 84" fill="none" stroke="{INK}" stroke-width="8"
        stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M44 52 L24 60" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>
  <path d="M52 38 L74 44" fill="none" stroke="{STAMP}" stroke-width="8" stroke-linecap="round"/>
  <path d="M56 60 L78 74" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>
  <path d="M10 30 h16 M8 48 h14" stroke="{SEA}" stroke-width="5" stroke-linecap="round"/>''',

"i-sing": f'''
  <rect x="38" y="10" width="24" height="40" rx="12" fill="{STAMP}" stroke="{INK}" stroke-width="4"/>
  <path d="M26 44 a24 24 0 0 0 48 0" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  <line x1="50" y1="68" x2="50" y2="86" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  <line x1="36" y1="88" x2="64" y2="88" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  <g fill="{SEA}"><circle cx="82" cy="30" r="7"/><rect x="86" y="8" width="4" height="24"/>
   <path d="M86 8 h10 v6 h-10 z"/></g>''',

"i-dance": f'''
  <circle cx="44" cy="18" r="10" fill="{INK}"/>
  <path d="M44 28 L42 56" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>
  <path d="M42 38 L20 24 M42 38 L66 18" fill="none" stroke="{STAMP}" stroke-width="8" stroke-linecap="round"/>
  <path d="M42 56 L26 84 M42 56 L62 78" fill="none" stroke="{INK}" stroke-width="8"
        stroke-linecap="round" stroke-linejoin="round"/>
  <g fill="{SEA}"><circle cx="78" cy="58" r="7"/><rect x="82" y="36" width="4" height="24"/>
   <path d="M82 36 h10 v6 h-10 z"/></g>''',

"i-cook": f'''
  <path d="M18 44 h64 v22 a12 12 0 0 1 -12 12 h-40 a12 12 0 0 1 -12 -12 z" fill="{SEA}" stroke="{INK}" stroke-width="4"/>
  <line x1="10" y1="42" x2="90" y2="42" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
  <rect x="45" y="28" width="10" height="8" rx="3" fill="{INK}"/>
  <g stroke="{STAMP}" stroke-width="5" stroke-linecap="round" fill="none">
   <path d="M34 22 q6 -7 0 -14"/><path d="M50 18 q6 -7 0 -14"/><path d="M66 22 q6 -7 0 -14"/></g>''',

"i-draw": f'''
  <path d="M18 82 L24 62 L64 22 L80 38 L40 78 Z" fill="{SUN}" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>
  <path d="M64 22 L80 38" stroke="{INK}" stroke-width="4"/>
  <path d="M18 82 L24 62 L40 78 Z" fill="{INK}"/>
  <path d="M56 30 L72 46" stroke="{INK}" stroke-width="3.5"/>
  <path d="M12 92 q14 -10 28 0 t28 0" fill="none" stroke="{SEA}" stroke-width="5" stroke-linecap="round"/>''',

"i-football": f'''
  <circle cx="50" cy="50" r="34" fill="{WHITE}" stroke="{INK}" stroke-width="5"/>
  <path d="M50 30 L66 42 L60 62 L40 62 L34 42 Z" fill="{INK}"/>
  <g stroke="{INK}" stroke-width="4.5" stroke-linecap="round">
   <line x1="50" y1="30" x2="50" y2="17"/><line x1="66" y1="42" x2="78" y2="34"/>
   <line x1="60" y1="62" x2="68" y2="78"/><line x1="40" y1="62" x2="32" y2="78"/>
   <line x1="34" y1="42" x2="22" y2="34"/></g>''',

"i-tennis": f'''
  <ellipse cx="40" cy="34" rx="22" ry="26" fill="{WHITE}" stroke="{INK}" stroke-width="5"/>
  <g stroke="{SEA}" stroke-width="3">
   <line x1="26" y1="18" x2="26" y2="52"/><line x1="40" y1="10" x2="40" y2="58"/>
   <line x1="54" y1="18" x2="54" y2="52"/>
   <line x1="20" y1="26" x2="60" y2="26"/><line x1="18" y1="36" x2="62" y2="36"/>
   <line x1="22" y1="46" x2="58" y2="46"/></g>
  <line x1="48" y1="56" x2="66" y2="84" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>
  <circle cx="80" cy="60" r="11" fill="{SUN}" stroke="{INK}" stroke-width="4"/>''',

"i-piano": f'''
  <rect x="10" y="30" width="80" height="44" rx="3" fill="{WHITE}" stroke="{INK}" stroke-width="4.5"/>
  <g stroke="{INK}" stroke-width="3">
   <line x1="26" y1="32" x2="26" y2="72"/><line x1="42" y1="32" x2="42" y2="72"/>
   <line x1="58" y1="32" x2="58" y2="72"/><line x1="74" y1="32" x2="74" y2="72"/></g>
  <g fill="{INK}">
   <rect x="20" y="32" width="11" height="24" rx="1.5"/><rect x="37" y="32" width="11" height="24" rx="1.5"/>
   <rect x="68" y="32" width="11" height="24" rx="1.5"/></g>
  <rect x="10" y="74" width="80" height="8" rx="3" fill="{STAMP}" stroke="{INK}" stroke-width="4"/>''',

"i-ski": f'''
  <g stroke="{STAMP}" stroke-width="7" stroke-linecap="round" fill="none">
   <path d="M14 82 L62 34 q6 -6 12 -2"/>
   <path d="M30 88 L78 40 q6 -6 12 -2"/></g>
  <g stroke="{INK}" stroke-width="5" stroke-linecap="round">
   <line x1="34" y1="20" x2="26" y2="70"/><line x1="52" y1="16" x2="46" y2="60"/></g>
  <g stroke="{SEA}" stroke-width="4" stroke-linecap="round">
   <line x1="20" y1="62" x2="32" y2="66"/><line x1="38" y1="54" x2="50" y2="58"/></g>''',

"i-skate": f'''
  <path d="M28 18 h16 v34 l22 8 v14 H28 Z" fill="{SEA}" stroke="{INK}" stroke-width="4.5" stroke-linejoin="round"/>
  <g stroke="{INK}" stroke-width="3.5"><line x1="32" y1="30" x2="40" y2="30"/>
   <line x1="32" y1="40" x2="40" y2="40"/></g>
  <path d="M18 82 h64" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  <path d="M18 82 q-6 0 -6 -6 M82 82 q6 0 6 -6" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
  <g stroke="{STAMP}" stroke-width="4" stroke-linecap="round">
   <line x1="34" y1="74" x2="34" y2="82"/><line x1="58" y1="74" x2="58" y2="82"/></g>''',
}
