const {ctx,go}=require('./lib');
const U=['/packages/','/packages/himachal-tour-package-shimla-manali/','/packages/kashmir-package-6-nights-7-days/','/tours/himachal-amritsar-package-from-chandigarh/','/destination/kashmir-tour-packages/','/blogs/','/shimla-in-december/','/contact-us/','/cabs/','/adventure/'];
(async()=>{const tag=process.argv[2]; const nobust=process.argv[3]==='nobust';
for (const mob of [false,true]){const {b,c}=await ctx(mob);const p=await c.newPage(); let errs=[]; p.on('console',m=>{if(m.type()==='error')errs.push(m.text().slice(0,80))});
 for (const u of U){ errs=[];
  const st=await go(p,'https://suzutravels.com'+u+(nobust?'':'?da='+Math.random())); await p.waitForTimeout(3000);
  const r=await p.evaluate(()=>{const vis=s=>{const e=document.querySelector(s);if(!e)return 0;const r=e.getBoundingClientRect();return r.width>0&&r.height>0?1:0};
   const tel=[...document.querySelectorAll('footer a[href^="tel:"], .main-footer a[href^="tel:"]')].length;
   const faqItem=document.querySelector('#faq .faq-item'); 
   return {ov:document.documentElement.scrollWidth-innerWidth, hdr:vis('.site-header'), cta:vis('#szcta')||vis('a[href*="wa.me"]'), footTel:tel, faqBg:faqItem?getComputedStyle(faqItem).backgroundColor:'-', da15: [...document.querySelectorAll('style')].some(s=>s.textContent.includes('DA-2026-10-15'))?1:0};});
  console.log(mob?'M':'D',st,u,JSON.stringify(r),'errs:'+errs.length);
  await p.screenshot({path:`shots/${tag}-${u.replace(/\//g,'_')}-${mob?'m':'d'}.png`});
 }
 await b.close();}})();
