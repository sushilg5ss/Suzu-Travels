const { chromium } = require('playwright');
const tag = process.argv[2] || 'before';
const bust = process.argv[3] !== 'nobust';
const urls = (process.argv[4] || '/packages/,/packages/himachal-tour-package-shimla-manali/,/tours/himachal-amritsar-package-from-chandigarh/,/destination/kashmir-tour-packages/,/blogs/,/shimla-in-december/,/contact/,/about-us/,/cabs/,/adventure/').split(',');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const out = [];
  for (const vp of [{w:390,h:844,n:'m'},{w:1440,h:900,n:'d'}]) {
    const ctx = await b.newContext({ viewport:{width:vp.w,height:vp.h}, isMobile: vp.n==='m', userAgent: vp.n==='m' ? 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1' : undefined });
    const p = await ctx.newPage();
    await p.goto('https://suzutravels.com/blogs/', {waitUntil:'domcontentloaded'}).catch(()=>{}); await p.waitForTimeout(7000);
    for (const u of urls) {
      const errs = []; p.removeAllListeners('console'); p.on('console', m => { if (m.type()==='error') errs.push(m.text().slice(0,120)); });
      const url = 'https://suzutravels.com' + u + (bust ? '?da=' + Math.random().toString(36).slice(2,8) : '');
      let st = 0; try { const r = await p.goto(url, {waitUntil:'load', timeout:60000}); st = r.status(); } catch(e) { st = 'ERR'; }
      await p.waitForTimeout(2500);
      const m = await p.evaluate(() => {
        const vis = s => { const e = document.querySelector(s); if (!e) return false; const r = e.getBoundingClientRect(); const cs = getComputedStyle(e); return r.width>0 && r.height>0 && cs.visibility!=='hidden' && cs.display!=='none'; };
        const f = document.querySelector('.main-footer');
        const fr = f ? f.getBoundingClientRect() : null;
        const links = f ? [...f.querySelectorAll('.footer-links a')].map(a=>Math.round(a.getBoundingClientRect().height)) : [];
        const soc = f ? [...f.querySelectorAll('.fb-center a')].map(a=>Math.round(a.getBoundingClientRect().width)) : [];
        return { ow: document.documentElement.scrollWidth - innerWidth, header: vis('header, .site-header'), cta: vis('#szcta'), footPhone: !!document.querySelector('a[href*="7087488961"]'), footerH: fr ? Math.round(fr.height) : null, linkH: links.length? Math.min(...links)+'-'+Math.max(...links):null, soc: soc.join('/'), inSzc: f ? !!f.closest('.szc') : null, szcCount: document.querySelectorAll('.szc').length };
      });
      await p.screenshot({ path: `${tag}-${vp.n}-${u.replace(/\W+/g,'_')}.png`, fullPage: false });
      if (u === '/contact/') { await p.evaluate(()=>{const f=document.querySelector('.main-footer'); f && f.scrollIntoView();}); await p.waitForTimeout(500); const f = await p.$('.main-footer'); if (f) await f.screenshot({ path: `${tag}-${vp.n}-contact-footer.png` }); }
      out.push({vp:vp.n, u, st, ...m, errs: errs.length});
    }
    await ctx.close();
  }
  await b.close();
  console.table(out);
})();
