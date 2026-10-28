// node render2.js <in.html> <out.pdf>  (Chromium print, A4)
const { chromium } = require('playwright');
(async () => { const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://' + __dirname + '/' + process.argv[2]);
  await p.pdf({ path: __dirname + '/' + process.argv[3], format: 'A4', printBackground: true, preferCSSPageSize: true }); await b.close(); })();
