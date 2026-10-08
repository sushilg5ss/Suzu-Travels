// Live check of a published page: hero video, overflow, H1, lazy videos, optional table filter test.
//   node tools/live_check.js <url> <out.png> <width> <height> [1 = also test the peak-table filter]
const { chromium } = require('playwright');
(async () => {
  const [url, out, w, h, table] = process.argv.slice(2);
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const p = await b.newPage({ viewport: { width: +w, height: +h } });
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  const t0 = Date.now();
  await p.goto(url, { waitUntil: 'load', timeout: 90000 });
  const loadMs = Date.now() - t0;
  await p.waitForTimeout(3000);
  // A late navigation (Hostinger JS challenge reloads the page ~3 s after load) destroys the context:
  // wait for the real page (waitForSelector survives navigations), then let it settle.
  try { await p.waitForSelector('.szp', { timeout: 45000 }); await p.waitForLoadState('load', { timeout: 30000 }); await p.waitForTimeout(2000); } catch (e) {}
  const title = await p.title().catch(() => '');
  if (/Checking your browser/i.test(title)) { console.log(JSON.stringify({ challenge: true, title })); await b.close(); process.exit(3); }
  const v1 = await p.evaluate(() => { const v = document.querySelector('.szp-hero video'); return v ? { rs: v.readyState, src: v.currentSrc.split('/').pop(), paused: v.paused } : null; });
  await p.mouse.move(300, 300); await p.mouse.wheel(0, 600); await p.waitForTimeout(3000);
  const info = await p.evaluate(() => ({ sw: document.documentElement.scrollWidth, iw: innerWidth, h1: document.querySelectorAll('h1').length, lazyDone: [...document.querySelectorAll('video[data-lazy]')].map(v => v.getAttribute('data-done')) }));
  let tbl = null;
  if (table === '1') {
    await p.click('.szp-filt button[data-k="state"][data-v="Gujarat"]');
    await p.waitForTimeout(500);
    tbl = await p.$eval('.szp-count', e => e.textContent);
  }
  await p.evaluate(() => window.scrollTo(0, 0)); await p.waitForTimeout(800);
  await p.screenshot({ path: out, fullPage: false });
  console.log(JSON.stringify({ loadMs, hero: v1, ...info, tbl, errs: errs.filter(e => !/moment|setSettings|feather/.test(e)) }));
  await b.close();
})();
