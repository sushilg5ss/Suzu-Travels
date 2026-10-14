const { chromium, devices } = require('playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const out = process.argv[2] || '/tmp/hp'; fs.mkdirSync(out, { recursive: true });
  const ROOT = process.argv[3] || ''; // '' = local site folder, else live base url
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const res = {};
  for (const [name, opts] of [['desktop', { viewport: { width: 1440, height: 900 } }], ['phone', devices['Pixel 7']]]) {
    const ctx = await browser.newContext(opts);
    const errs = [];
    await ctx.route('**/admin-ajax.php*', r => r.fulfill({ status: 200, body: '{}' }));
    if (!ROOT) await ctx.route('http://local.test/**', async r => {
      const u = new URL(r.request().url()); let p = u.pathname;
      if (p === '/' ) return r.fulfill({ status: 200, contentType: 'text/html', body: fs.readFileSync('site/index.html') });
      if (p.startsWith('/plan-your-trip/')) return r.fulfill({ status: 200, contentType: 'text/html', body: fs.readFileSync('site/plan-your-trip/index.html') });
      try { const resp = await r.fetch({ url: 'https://suzutravels.com' + p + u.search }); return r.fulfill({ response: resp }); } catch (e) { return r.abort(); }
    });
    await ctx.addInitScript(() => { navigator.sendBeacon = () => true; window.print = () => { window.__printed = 1; }; });
    const page = await ctx.newPage();
    page.on('pageerror', e => errs.push('home: ' + e));
    const base = ROOT || 'http://local.test';
    await page.goto(base + '/', { waitUntil: 'load', timeout: 90000 });
    await page.waitForTimeout(1500);
    const r = {};
    r.h1 = await page.$$eval('h1', x => x.length);
    r.video = await page.$$eval('#nz-hero video', x => x.length);
    r.engineTop = await page.$eval('#tp-engine', e => Math.round(e.getBoundingClientRect().top));
    r.goBtnBottom = await page.$eval('#tpe-go', e => Math.round(e.getBoundingClientRect().bottom));
    r.vh = await page.evaluate(() => innerHeight);
    r.overflow = await page.evaluate(() => document.documentElement.scrollWidth > innerWidth + 1);
    await page.screenshot({ path: `${out}/${name}-1-hero.png` });
    // popular chip
    await page.click('#tpe-quick [data-tpl="shimla-manali"]');
    await page.waitForSelector('#tp-ov:not([hidden])');
    const fr = page.frameLocator('#tp-ov iframe');
    await fr.locator('.tl-day').first().waitFor({ timeout: 30000 });
    await page.waitForTimeout(1500);
    r.ovDays = await fr.locator('.tl-day').count();
    r.ovPrice = await fr.locator('#price .big').textContent();
    await page.screenshot({ path: `${out}/${name}-2-overlay.png` });
    // pdf through lead inside iframe
    await fr.locator('#price [data-act="pdf"]').dispatchEvent('click');
    await fr.locator('#ld-name').fill('TEST'); await fr.locator('#ld-ph').fill('9876543210'); await fr.locator('#ld-go').dispatchEvent('click');
    await page.waitForTimeout(500);
    r.shareBase = await page.frames().find(f => f.url().includes('plan-your-trip')).evaluate(() => (window.__tpLastLead || {}).message || '').then(m => (m.match(/Link: (\S+)/) || [])[1] || '');
    // close
    await page.screenshot({ path: `${out}/${name}-2b-beforeclose.png` });
    r.closeBox = await fr.locator('.tp-close').boundingBox();
    await fr.locator('.tp-close').click({ timeout: 5000 }).catch(async e => { r.closeErr = String(e).slice(0, 80); await fr.locator('.tp-close').dispatchEvent('click'); });
    await page.waitForTimeout(400);
    r.closed = await page.$eval('#tp-ov', e => e.hidden);
    // search place
    await page.fill('#tpe-to', 'chintp'); await page.waitForTimeout(200);
    await page.keyboard.press('Enter');
    await fr.locator('#m-title').waitFor(); await page.waitForTimeout(1500);
    r.placeTitle = await fr.locator('#m-title').textContent();
    await page.keyboard.press('Escape'); await page.waitForTimeout(300);
    r.closedEsc = await page.$eval('#tp-ov', e => e.hidden);
    // cab tab
    await page.click('#tpe-t-cab'); await page.selectOption('#tpe-cf', 'delhi'); await page.selectOption('#tpe-ct', 'shimla'); await page.click('#tpe-cgo');
    await page.waitForTimeout(2500);
    r.cab = await fr.locator('#c-res .v').textContent().catch(() => 'none');
    await page.screenshot({ path: `${out}/${name}-3-cab.png` });
    await page.evaluate(() => history.back()); await page.waitForTimeout(600);
    r.closedBack = await page.$eval('#tp-ov', e => e.hidden);
    // Book now popup still works
    await page.click('#nz-hero a[href="#hero-search"]'); await page.waitForTimeout(600);
    r.bookPopup = await page.$eval('#hero-search', e => e.classList.contains('active') || getComputedStyle(e).display !== 'none').catch(() => 'n/a');
    r.assistant = await page.$$eval('.sa-launch', x => x.length);
    r.slides = await page.$$eval('.tpx-bg img', x => x.length);
    r.errors = errs;
    res[name] = r; await ctx.close();
  }
  console.log(JSON.stringify(res, null, 1)); await browser.close();
})();
