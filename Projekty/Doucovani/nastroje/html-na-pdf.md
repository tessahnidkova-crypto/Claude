# Jak z HTML udělat PDF (v Claude session)

Chromium je v kontejneru předinstalovaný, weasyprint ani wkhtmltopdf tam nejsou.

```bash
/opt/pw-browsers/chromium-1194/chrome-linux/chrome \
  --headless --no-sandbox --disable-gpu --no-pdf-header-footer \
  --print-to-pdf=vystup.pdf "file:///cesta/k/souboru.html"
```

- V CSS použij `@page{size:A4 landscape;margin:0}` a `.page{width:297mm;height:210mm;break-after:page}`.
- Poslední stránce dej `break-after:auto`, jinak vznikne prázdná stránka navíc.
- **Emoji font v kontejneru NENÍ** — emoji se vykreslí jako prázdné čtverečky. Kresli ikony jako inline SVG.
- Fonty z Google Fonts stáhni a vlož jako base64 data URI (`@font-face … src:url(data:font/woff2;base64,…)`), ať PDF nezávisí na síti.
- Barvy na pozadí se do PDF dostanou jen s `print-color-adjust:exact`.
- Náhled ke kontrole: `--screenshot` na kopii HTML se `zoom:.36` a `display:inline-flex` na `.page`.
  ⚠️ `display:inline-block` v náhledovém override přebije `display:flex` a rozbije layout — pak náhled lže.
