# -*- coding: utf-8 -*-
# Vlajky jako SVG, viewBox 0 0 100 100; samotná vlajka je rect 6,20 -> 94,80 (poměr ~3:2)
INK="#16323B"
def _frame(): return f'<rect x="6" y="20" width="88" height="60" fill="none" stroke="{INK}" stroke-width="3"/>'

FLAGS = {
"f-cz": f'''<rect x="6" y="20" width="88" height="30" fill="#FFFFFF"/>
  <rect x="6" y="50" width="88" height="30" fill="#D7141A"/>
  <path d="M6 20 L50 50 L6 80 Z" fill="#11457E"/>{_frame()}''',

"f-uk": f'''<rect x="6" y="20" width="88" height="60" fill="#012169"/>
  <path d="M6 20 L94 80 M94 20 L6 80" stroke="#FFFFFF" stroke-width="12"/>
  <path d="M6 20 L94 80 M94 20 L6 80" stroke="#C8102E" stroke-width="6"/>
  <path d="M50 20 V80 M6 50 H94" stroke="#FFFFFF" stroke-width="20"/>
  <path d="M50 20 V80 M6 50 H94" stroke="#C8102E" stroke-width="11"/>{_frame()}''',

"f-usa": f'''<rect x="6" y="20" width="88" height="60" fill="#FFFFFF"/>
  <g fill="#B22234">
   <rect x="6" y="20" width="88" height="8.6"/><rect x="6" y="37.1" width="88" height="8.6"/>
   <rect x="6" y="54.3" width="88" height="8.6"/><rect x="6" y="71.4" width="88" height="8.6"/></g>
  <rect x="6" y="20" width="40" height="34" fill="#3C3B6E"/>
  <g fill="#FFFFFF"><circle cx="14" cy="27" r="2"/><circle cx="26" cy="27" r="2"/><circle cx="38" cy="27" r="2"/>
   <circle cx="20" cy="36" r="2"/><circle cx="32" cy="36" r="2"/>
   <circle cx="14" cy="45" r="2"/><circle cx="26" cy="45" r="2"/><circle cx="38" cy="45" r="2"/></g>{_frame()}''',

"f-it": f'''<rect x="6" y="20" width="29.3" height="60" fill="#008C45"/>
  <rect x="35.3" y="20" width="29.3" height="60" fill="#FFFFFF"/>
  <rect x="64.6" y="20" width="29.4" height="60" fill="#CD212A"/>{_frame()}''',

"f-es": f'''<rect x="6" y="20" width="88" height="15" fill="#AA151B"/>
  <rect x="6" y="35" width="88" height="30" fill="#F1BF00"/>
  <rect x="6" y="65" width="88" height="15" fill="#AA151B"/>{_frame()}''',

"f-jp": f'''<rect x="6" y="20" width="88" height="60" fill="#FFFFFF"/>
  <circle cx="50" cy="50" r="18" fill="#BC002D"/>{_frame()}''',

"f-hu": f'''<rect x="6" y="20" width="88" height="20" fill="#CD2A3E"/>
  <rect x="6" y="40" width="88" height="20" fill="#FFFFFF"/>
  <rect x="6" y="60" width="88" height="20" fill="#436F4D"/>{_frame()}''',
}
