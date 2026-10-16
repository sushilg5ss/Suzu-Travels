const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const c=await b.newContext({viewport:{width:390,height:844},isMobile:true});const p=await c.newPage();
await p.goto('https://suzutravels.com/blogs/',{waitUntil:'domcontentloaded'}).catch(()=>{});await p.waitForTimeout(7000);
for(const u of ['/contact/','/about-us/']){await p.goto('https://suzutravels.com'+u+'?da='+Date.now(),{waitUntil:'load'});await p.waitForTimeout(2000);
const r=await p.evaluate(()=>[...document.querySelectorAll('.main-footer .footer-contact > *')].map(e=>{const b=e.getBoundingClientRect();const cs=getComputedStyle(e);return e.tagName+' h'+Math.round(b.height)+' op'+cs.opacity+' vis'+cs.visibility+' '+(e.textContent||'').trim().slice(0,30)}));console.log(u,r);
await p.evaluate(()=>{document.querySelector('.footer-contact').scrollIntoView({block:'center'})});await p.waitForTimeout(800);await p.screenshot({path:'addr'+u.replace(/\W/g,'')+'.png'});}
await b.close();})();
