// Screenshot a preview file or a live URL at desktop (1440 wide) and phone (390 wide), as a series of JPEG slices the Read
// tool can look at:   node tools/shots.js <file.html|https://url> <name>   -> /tmp/mk-shots/<name>-{d,m}-<n>.jpg
// Prints one JSON line per viewport: overflow (scrollWidth vs innerWidth), H1 count, page height, videos (readyState,
// lazy-loaded?, source file) and page errors (the site's known 'moment/setSettings/feather' errors are filtered out).
const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const [target, name] = process.argv.slice(2);
  const url = /^https?:/.test(target) ? target : 'file://' + target;
  const dir = '/tmp/mk-shots'; fs.mkdirSync(dir, { recursive: true });
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  for (const [tag, w, h] of [['d', 1440, 1400], ['m', 390, 1200]]) {
    const p = await b.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 1 });
    const errs = []; p.on('pageerror', e => errs.push(e.message));
    await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 });
    try { await p.waitForLoadState('load', { timeout: 30000 }); } catch (e) { errs.push('load event timeout (continuing)'); }
    await p.mouse.move(200, 300); await p.mouse.wheel(0, 300);           // wakes WP Rocket delayed JS on live pages
    const H = await p.evaluate(() => document.documentElement.scrollHeight);
    for (let y = 0; y < H; y += 800) { await p.evaluate(v => window.scrollTo(0, v), y); await p.waitForTimeout(80); }
    await p.waitForTimeout(1200);
    const info = await p.evaluate(() => ({
      overflow: document.documentElement.scrollWidth > innerWidth, scrollWidth: document.documentElement.scrollWidth, innerWidth,
      h1: document.querySelectorAll('h1').length, height: document.documentElement.scrollHeight,
      videos: [...document.querySelectorAll('.szm video')].map(v => ({ lazy: v.hasAttribute('data-lazy'), loaded: v.getAttribute('data-done') || !v.hasAttribute('data-lazy'), rs: v.readyState, src: (v.currentSrc || '').split('/').slice(-2).join('/') })),
    }));
    const slices = [];
    for (let y = 0, n = 0; y < info.height && n < 30; y += h, n++) {
      await p.evaluate(v => window.scrollTo(0, v), y); await p.waitForTimeout(250);
      const f = `${dir}/${name}-${tag}-${n}.jpg`;
      await p.screenshot({ path: f, type: 'jpeg', quality: 68 });
      slices.push(f);
    }
    console.log(JSON.stringify({ viewport: tag, ...info, errors: errs.filter(e => !/moment|setSettings|feather/.test(e)), slices }));
    await p.close();
  }
  await b.close();
})();
