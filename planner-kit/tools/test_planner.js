// Headless test: node tools/test_planner.js <url> <outdir>
const { chromium, devices } = require('playwright');
(async () => {
  const url = process.argv[2], out = process.argv[3] || '/tmp/tp';
  require('fs').mkdirSync(out, { recursive: true });
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const res = {};
  for (const [name, opts] of [['desktop', { viewport: { width: 1440, height: 900 } }], ['phone', devices['Pixel 7']]]) {
    const ctx = await browser.newContext(opts); const page = await ctx.newPage();
    const errs = []; page.on('pageerror', e => errs.push(String(e))); page.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
    await page.route('**/admin-ajax.php', r => r.fulfill({ status: 200, body: '{}' }));
    await page.addInitScript(() => { navigator.sendBeacon = () => true; window.print = () => { window.__printed = (window.__printed || 0) + 1; }; });
    await page.goto(url, { waitUntil: 'load' });
    await page.screenshot({ path: `${out}/${name}-1-hero.png` });
    const r = {};
    // template via chip
    await page.click('#q-quick [data-tpl="shimla-manali"]');
    await page.waitForTimeout(1800);
    r.days = await page.$$eval('.tl-day', x => x.length);
    r.price = await page.textContent('#price .big');
    r.title = await page.textContent('#m-title');
    await page.screenshot({ path: `${out}/${name}-2-plan.png`, fullPage: false });
    await page.screenshot({ path: `${out}/${name}-2b-full.png`, fullPage: true });
    // add stop via suggestion
    await page.click('#b-sugg [data-add]');
    await page.waitForTimeout(400);
    r.stopsAfterAdd = await page.$$eval('#b-stops li[data-i]', x => x.length);
    // optimise + tier
    await page.click('#b-opt'); await page.click('#b-tiers [data-t="luxury"]'); await page.waitForTimeout(300);
    r.luxPrice = await page.textContent('#price .big');
    // play
    await page.click('#m-play'); await page.waitForTimeout(2500);
    await page.screenshot({ path: `${out}/${name}-3-play.png` });
    await page.click('#m-play');
    // mata template
    await page.evaluate(() => SuzuTripPlanner.load('nau-devi')); await page.waitForTimeout(1200);
    r.mata = { days: await page.$$eval('.tl-day', x => x.length), price: await page.textContent('#price .big'), warns: await page.$$eval('.warn', x => x.map(y => y.textContent)) };
    await page.screenshot({ path: `${out}/${name}-4-mata.png` });
    // spiti in Dec -> season warning
    await page.evaluate(() => { SuzuTripPlanner.load('spiti-circuit'); }); await page.waitForTimeout(800);
    r.spiti = { sub: await page.textContent('#m-sub'), warns: await page.$$eval('.warn', x => x.map(y => y.textContent)) };
    // lead + pdf
    await page.click('#price [data-act="pdf"]'); await page.waitForTimeout(300);
    await page.fill('#ld-name', 'TEST Claude'); await page.fill('#ld-ph', '9876543210'); await page.click('#ld-go'); await page.waitForTimeout(600);
    r.printed = await page.evaluate(() => window.__printed || 0);
    r.lead = await page.evaluate(() => window.__tpLastLead && window.__tpLastLead.destination);
    // share link round-trip
    await page.click('#price [data-act="share"]'); await page.waitForTimeout(400);
    const link = await page.inputValue('#sh-url'); r.linkLen = link.length;
    await page.screenshot({ path: `${out}/${name}-5-share.png` });
    const p2 = await ctx.newPage(); await p2.goto(link, { waitUntil: 'load' }); await p2.waitForTimeout(1200);
    r.roundTrip = await p2.textContent('#m-title');
    // agent mode client link
    await p2.click('.tp-mode [data-mode="agent"]'); await p2.waitForTimeout(300);
    await p2.fill('#ag-name', 'Shubh Yatra Holidays'); await p2.fill('#ag-phone', '9812345678'); await p2.fill('#ag-mk', '20'); await p2.waitForTimeout(500);
    r.agentBox = await p2.textContent('#price .agent');
    await page.click('#mod .x');
    // cab tab
    await page.click('#tab-cab'); await page.selectOption('#c-from', 'delhi'); await page.selectOption('#c-to', 'shimla'); await page.click('#c-go');
    r.cab = await page.textContent('#c-res .v');
    await page.click('#tab-hotel'); await page.click('#h-go'); r.hotel = await page.textContent('#h-res .v');
    r.overflow = await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth + 1);
    r.errors = errs;
    res[name] = r; await ctx.close();
  }
  console.log(JSON.stringify(res, null, 1));
  await browser.close();
})();
