#!/bin/bash
# render.sh <svg> <png> <w> <h>   — vyrenderuje SVG do PNG bez skalovani
SVG="$1"; PNG="$2"; W="$3"; H="$4"
TMP="$(dirname "$PNG")/_wrap_$(basename "$PNG" .png).html"
cat > "$TMP" << HTML
<!doctype html><meta charset="utf-8">
<style>html,body{margin:0;padding:0;background:#fff}img{display:block}</style>
<img src="file://$(cd "$(dirname "$SVG")" && pwd)/$(basename "$SVG")" width="$W" height="$H">
HTML
/opt/pw-browsers/chromium-1194/chrome-linux/chrome --headless --disable-gpu --no-sandbox \
  --hide-scrollbars --force-device-scale-factor=1 --window-size="$W,$H" \
  --screenshot="$PNG" "file://$TMP" 2>/dev/null
echo "$PNG"
