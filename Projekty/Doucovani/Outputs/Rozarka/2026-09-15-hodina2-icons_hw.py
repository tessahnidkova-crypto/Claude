# -*- coding: utf-8 -*-
INK="#16323B"; SEA="#0F8B8D"; STAMP="#E4572E"; SUN="#F2B028"; OK="#2E8B57"; W="#FFFFFF"

HW_ICONS = {
"i-seaside": f'''
  <circle cx="74" cy="24" r="13" fill="{SUN}"/>
  <g stroke="{SUN}" stroke-width="5" stroke-linecap="round">
    <line x1="74" y1="2" x2="74" y2="8"/><line x1="94" y1="24" x2="99" y2="24"/>
    <line x1="89" y1="9" x2="93" y2="5"/><line x1="59" y1="9" x2="55" y2="5"/></g>
  <path d="M6 58 q40 -22 88 0 v10 H6 Z" fill="{SUN}" opacity="0.45"/>
  <g stroke="{SEA}" stroke-width="7" stroke-linecap="round" fill="none">
    <path d="M6 70 q11 -12 22 0 t22 0 t22 0 t22 0"/>
    <path d="M6 88 q11 -12 22 0 t22 0 t22 0 t22 0"/></g>''',

"i-inside": f'''
  <path d="M50 12 L88 44 v44 H12 V44 Z" fill="{W}" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>
  <circle cx="50" cy="62" r="11" fill="{SEA}"/>
  <path d="M50 12 L88 44 v44 H12 V44 Z" fill="none" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>
  <g stroke="{STAMP}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round">
    <line x1="4" y1="62" x2="26" y2="62"/><path d="M19 55 L26 62 L19 69"/></g>''',

"i-outside": f'''
  <path d="M44 20 L74 46 v42 H14 V46 Z" fill="{W}" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>
  <rect x="34" y="64" width="20" height="24" fill="{SEA}"/>
  <path d="M44 20 L74 46 v42 H14 V46 Z" fill="none" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>
  <circle cx="90" cy="44" r="9" fill="{OK}"/>
  <line x1="90" y1="53" x2="90" y2="88" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
  <g stroke="{STAMP}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round">
    <line x1="60" y1="34" x2="82" y2="34"/><path d="M75 27 L82 34 L75 41"/></g>''',

"i-but": f'''
  <path d="M8 52 L24 70 L54 28" fill="none" stroke="{OK}" stroke-width="10"
        stroke-linecap="round" stroke-linejoin="round"/>
  <line x1="62" y1="16" x2="62" y2="84" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
  <g stroke="{STAMP}" stroke-width="10" stroke-linecap="round">
    <line x1="76" y1="34" x2="96" y2="64"/><line x1="96" y1="34" x2="76" y2="64"/></g>''',

"i-need": f'''
  <path d="M26 88 V52 a7 7 0 0 1 14 0 v-8 a7 7 0 0 1 14 0 v4 a7 7 0 0 1 14 0 v6 a7 7 0 0 1 13 3 v15
           a18 18 0 0 1 -18 18 Z"
        fill="{W}" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>
  <circle cx="26" cy="24" r="4" fill="{STAMP}"/>
  <line x1="26" y1="4" x2="26" y2="16" stroke="{STAMP}" stroke-width="7" stroke-linecap="round"/>''',

"i-bit": f'''
  <rect x="8" y="38" width="24" height="26" rx="3" fill="{SEA}" stroke="{INK}" stroke-width="4"/>
  <rect x="38" y="38" width="24" height="26" rx="3" fill="{W}" stroke="{INK}" stroke-width="4"/>
  <rect x="68" y="38" width="24" height="26" rx="3" fill="{W}" stroke="{INK}" stroke-width="4"/>
  <line x1="8" y1="78" x2="32" y2="78" stroke="{STAMP}" stroke-width="5" stroke-linecap="round"/>''',
}
