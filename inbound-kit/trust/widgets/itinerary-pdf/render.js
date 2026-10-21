// node render.js  -> PDF from gt-6-day.html (Chromium print, A4)
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://' + __dirname + '/gt-6-day.html');
  await p.pdf({ path: __dirname + '/golden-triangle-6-day-itinerary-suzu-travels.pdf', format: 'A4', printBackground: true, preferCSSPageSize: true });
  await b.close();
})();
