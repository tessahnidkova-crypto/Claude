// HTML → PDF přes Chromium. Použití: node render.js
const { chromium } = require('/opt/node-tools/node_modules/playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + path.join(__dirname, 'tyden-1.html'));
  await p.pdf({ path: path.join(__dirname, 'tyden-1.pdf'), format: 'A4', preferCSSPageSize: true, printBackground: true });
  await b.close();
})();
