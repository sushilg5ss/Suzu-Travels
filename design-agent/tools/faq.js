const {ctx,go}=require('./lib');
(async()=>{const tag=process.argv[2];
for (const mob of [false,true]){const {b,c}=await ctx(mob);const p=await c.newPage();
 for (const u of process.argv.slice(3)){
  await go(p,u+'?da='+Math.random()); await p.waitForTimeout(2500);
  const info=await p.evaluate(()=>{const s=document.querySelector('#faq')||document.querySelector('.faq');
   if(!s) return {none:true};
   s.classList.add('visible','active','in-view'); s.style.opacity=1;
   const q=s.querySelector('.faq-q'), a=s.querySelector('.faq-a'), it=s.querySelector('.faq-item');
   const cs=e=>{if(!e)return null;const c=getComputedStyle(e);return {font:c.fontFamily.slice(0,40),fs:c.fontSize,fw:c.fontWeight,col:c.color,bg:c.backgroundColor,pad:c.padding,bd:c.border,br:c.borderRadius,mh:c.maxHeight,h:e.getBoundingClientRect().height,w:e.getBoundingClientRect().width,cur:c.cursor,shadow:c.boxShadow}};
   return {n:s.querySelectorAll('.faq-item').length,sec:cs(s),item:cs(it),q:cs(q),a:cs(a),arrow:cs(s.querySelector('.arrow')),title:cs(s.querySelector('.section-title')),cls:s.className,onclick:q&&q.getAttribute('onclick'),tabindex:q&&q.getAttribute('tabindex'),role:q&&q.getAttribute('role')};});
  console.log(mob?'M':'D',u,JSON.stringify(info));
  const s=await p.$('#faq'); if(s){await s.scrollIntoViewIfNeeded(); await p.waitForTimeout(800);
   const name=u.split('/').filter(Boolean).pop(); await s.screenshot({path:`shots/${tag}-faq-${name}-${mob?'m':'d'}.png`});
   // click first q and screenshot
   const q=await p.$('#faq .faq-q'); if(q){await q.click(); await p.waitForTimeout(700); const cls=await p.evaluate(()=>{const i=document.querySelector('#faq .faq-item');return i.className+' | a.h='+i.querySelector('.faq-a').getBoundingClientRect().height}); console.log(' after click:',cls); await s.screenshot({path:`shots/${tag}-faqopen-${name}-${mob?'m':'d'}.png`}); await q.click(); await p.waitForTimeout(500);}
  }
 }
 await b.close();}})();
