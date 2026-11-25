// usage: node test.js <html file or "live"> <outdir>
const { chromium, devices } = require('playwright');
const fs = require('fs');
(async () => {
  const file = process.argv[2], out = process.argv[3] || '.';
  fs.mkdirSync(out, { recursive: true });
  const body = file === 'live' ? null : fs.readFileSync(file);
  const browser = await chromium.launch({ args: ['--autoplay-policy=no-user-gesture-required'] });
  const res = {};
  for (const [name, opts] of [['desktop', { viewport: { width: 1440, height: 900 } }], ['mobile', { ...devices['Pixel 7'] }]]) {
    const ctx = await browser.newContext({ ...opts, serviceWorkers: 'block' });
    await ctx.addInitScript(() => {
      window.__beacons = 0;
      navigator.sendBeacon = function () { window.__beacons++; return true; };
    });
    let posted = 0, feed = [];
    await ctx.route('**/wp-admin/admin-ajax.php**', r => { posted++; r.fulfill({ status: 200, contentType: 'application/json', body: '{"success":true}' }); });
    if (body) await ctx.route(u => { const x = new URL(u); return x.hostname === 'suzutravels.com' && x.pathname === '/' ; },
      r => r.request().resourceType() === 'document' ? r.fulfill({ status: 200, contentType: 'text/html; charset=utf-8', body }) : r.continue());
    const page = await ctx.newPage();
    const errors = [];
    page.on('pageerror', e => errors.push(String(e).slice(0, 200)));
    page.on('request', q => { if (q.url().includes('suzu-weather')) feed.push(q.url().replace('https://suzutravels.com', '').slice(0, 60)); });
    await page.goto('https://suzutravels.com/?t=' + Date.now(), { waitUntil: 'domcontentloaded', timeout: 90000 });
    await page.waitForTimeout(6000);
    const r = {};
    r.h1 = await page.locator('h1').count();
    r.tp = await page.evaluate(() => { const e = document.getElementById('tp-engine'); if (!e) return null; const b = e.getBoundingClientRect(); return { top: Math.round(b.top), vis: b.height > 0 && b.top < innerHeight }; });
    await page.screenshot({ path: `${out}/${name}-hero.png` });
    // Plan my trip
    try {
      await page.locator('#tpe-go').click({ timeout: 5000 }); await page.waitForTimeout(2000);
      r.plan = await page.evaluate(() => { const f = [...document.querySelectorAll('iframe')].map(i => i.src).filter(s => s.includes('plan-your-trip')); return f[0] ? f[0].replace('https://suzutravels.com', '').slice(0, 50) : location.href.includes('plan-your-trip') ? 'nav' : null; });
      await page.keyboard.press('Escape'); await page.waitForTimeout(500);
      if (!page.url().includes('suzutravels.com/?')) await page.goBack();
    } catch (e) { r.plan = 'ERR ' + String(e).slice(0, 100); }
    // close any overlay: reload (count weather-feed requests from this fresh load)
    feed = [];
    await page.goto('https://suzutravels.com/?t=' + Date.now(), { waitUntil: 'domcontentloaded' }); await page.waitForTimeout(3000);
    // Book Now
    try {
      await page.locator('a:has-text("Book Now")').first().click({ timeout: 5000 }); await page.waitForTimeout(1500);
      r.book = await page.evaluate(() => { const h = document.getElementById('hero-search'); const b = h && h.getBoundingClientRect(); const pop = [...document.querySelectorAll('[id*="szp"],[class*="popup"],[class*="modal"]')].some(e => { const s = getComputedStyle(e), q = e.getBoundingClientRect(); return s.display !== 'none' && s.visibility !== 'hidden' && q.width > 200 && q.height > 150 && q.top < innerHeight && q.bottom > 0; }); return { heroInView: b ? b.top < innerHeight && b.bottom > 0 : null, popup: pop }; });
      await page.screenshot({ path: `${out}/${name}-booknow.png` });
      await page.keyboard.press('Escape'); await page.waitForTimeout(400);
    } catch (e) { r.book = 'ERR ' + String(e).slice(0, 100); }
    // scroll the whole page to trigger lazy weather blocks
    await page.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 600) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 120)); } });
    await page.waitForTimeout(2500);
    r.snowPill = await page.evaluate(() => { const e = document.querySelector('.nz-xp-live'); return e ? (e.hidden ? 'hidden' : e.textContent.slice(0, 70)) : null; });
    r.wxMarquee = await page.evaluate(() => { const s = document.getElementById('himachal-weather'); return s ? { off: s.classList.contains('nzw-off'), items: s.querySelectorAll('#nzw-track > *').length } : null; });
    r.hkwx = await page.evaluate(() => { const e = document.querySelector('#nz-hk [class*="wx"]'); return e ? e.textContent.replace(/\s+/g, ' ').trim().slice(0, 80) : null; });
    r.rwx = await page.evaluate(() => { const e = document.getElementById('nz-rwx'); return e ? (e.hidden ? 'hidden' : e.textContent.replace(/\s+/g, ' ').trim().slice(0, 80)) : null; });
    r.feedRequests = feed.slice();
    // explorer: Kashmir filter + open first card (fresh page so no overlay)
    await page.goto('https://suzutravels.com/?t=' + Date.now(), { waitUntil: 'domcontentloaded' }); await page.waitForTimeout(3000);
    try {
      await page.locator('#tour-packages').scrollIntoViewIfNeeded(); await page.waitForTimeout(800);
      await page.locator('#tour-packages .nz-reg[data-r="kashmir"]').first().click(); await page.waitForTimeout(800);
      r.kashmir = await page.evaluate(() => [...document.querySelectorAll('#nz-grid [data-open]')].filter(c => c.offsetParent).length);
      await page.screenshot({ path: `${out}/${name}-explorer.png` });
      await page.locator('#nz-grid button[data-open]:visible').first().click({ timeout: 8000 }); await page.waitForTimeout(2500);
      r.sheet = await page.evaluate(() => { const s = document.getElementById('nz-sheet'); if (!s) return null; const w = s.querySelector('.nz-wxr'); return { title: (s.querySelector('h2,h3') || {}).textContent, wa: s.querySelectorAll('a[href*="wa.me"],a[href*="whatsapp"]').length, routeWx: w ? w.textContent.replace(/\s+/g, ' ').slice(0, 90) : null }; });
      await page.screenshot({ path: `${out}/${name}-sheet.png` });
    } catch (e) { r.sheet = 'ERR ' + String(e).slice(0, 120); }
    r.newLinks = await page.evaluate(() => ['adventure/treks-near-shimla/', 'kenya-tour-packages/', 'mehrangarh-fort/', 'cabs/dalhousie-taxi-service/'].map(p => document.querySelectorAll('a[href="https://suzutravels.com/' + p + '"]').length));
    r.overflow = await page.evaluate(() => document.documentElement.scrollWidth - innerWidth);
    r.posted = posted; r.beacons = await page.evaluate(() => window.__beacons);
    r.errors = [...new Set(errors)];
    res[name] = r;
    await ctx.close();
  }
  console.log(JSON.stringify(res, null, 1));
  await browser.close();
})();
