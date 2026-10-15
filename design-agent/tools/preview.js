const {ctx,go}=require('./lib');const fs=require('fs');
(async()=>{const tag=process.argv[2]; const inject=process.argv[3]==='inject'; const css=fs.readFileSync('new.css','utf8');
for (const mob of [false,true]){const {b,c}=await ctx(mob);const p=await c.newPage();
 for (const u of process.argv.slice(4)){
  await go(p,u+'?da='+Math.random()); await p.waitForTimeout(2500);
  if(inject) await p.addStyleTag({content:css});
  const s=await p.$('#faq'); if(!s){console.log('nofaq',u);continue;}
  await p.evaluate(()=>{const s=document.querySelector('#faq');s.style.opacity=1;s.classList.add('visible');});
  // click FAQ tab in pkg-nav and measure landing
  const land=await p.evaluate(async()=>{const a=document.querySelector('.pkg-nav a[href="#faq"]'); if(!a) return 'no tab'; a.click(); await new Promise(r=>setTimeout(r,1500));
    const t=document.querySelector('#faq .section-title').getBoundingClientRect().top; const hd=document.querySelector('.site-header'); const nav=document.querySelector('.pkg-nav');
    return {titleTop:Math.round(t), headerBottom:hd?Math.round(hd.getBoundingClientRect().bottom):null, navBottom:nav?Math.round(nav.getBoundingClientRect().bottom):null};});
  await p.evaluate(()=>{const q=document.querySelector('#faq .faq-q'); q.click();});
  await p.waitForTimeout(600);
  const m=await p.evaluate(()=>{const a=document.querySelector('#faq .faq-item.open .faq-a');const pp=a&&a.querySelector('p');const c=getComputedStyle;
   return {open:!!a, aH:a&&Math.round(a.getBoundingClientRect().height), pCol:pp&&c(pp).color, pW:pp&&Math.round(pp.getBoundingClientRect().width), qH:Math.round(document.querySelector('#faq .faq-q').getBoundingClientRect().height), overflow:document.documentElement.scrollWidth-innerWidth};});
  console.log(mob?'M':'D',u.split('/').filter(Boolean).pop(),JSON.stringify(land),JSON.stringify(m));
  await s.scrollIntoViewIfNeeded(); await p.waitForTimeout(500);
  await s.screenshot({path:`shots/${tag}-${u.split('/').filter(Boolean).pop()}-${mob?'m':'d'}.png`});
 }
 await b.close();}})();
