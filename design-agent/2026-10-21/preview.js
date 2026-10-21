const { chromium } = require('/opt/npm-tools/node_modules/playwright');
const fs=require('fs'); const css=fs.readFileSync('DA-2026-10-21.css','utf8');
const UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36';
const SEL='body.page-template-default .page-content:has(> .entry-content > p:first-child):not(:has(.szc, .sza, .pl))';
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const urls=fs.readFileSync(process.argv[2],'utf8').trim().split('\n'); const shots=process.argv[3]==='shots';
for (const [w,h,mob] of [[1440,900,false],[390,844,true]]){
const ctx=await b.newContext({userAgent:UA,viewport:{width:w,height:h},isMobile:mob,hasTouch:mob}); const p=await ctx.newPage(); let first=true;
for(const u of urls){ try{
await p.goto('https://suzutravels.com'+u+'?da=p'+Date.now(),{waitUntil:'load',timeout:60000}); await p.waitForTimeout(first?9000:2000); first=false; await p.waitForLoadState('load');
const match=await p.evaluate(s=>!!document.querySelector(s),SEL);
const H0=await p.evaluate(()=>document.documentElement.scrollHeight);
await p.addStyleTag({content:css}); await p.waitForTimeout(600);
const m=await p.evaluate(()=>({sw:document.documentElement.scrollWidth,iw:innerWidth,H:document.documentElement.scrollHeight}));
const slug=u.replace(/[^a-z0-9]+/gi,'_');
if(shots&&match){ await p.screenshot({path:`prev_${w}${slug}top.png`}); const t=await p.$('.entry-content table'); if(t){await t.scrollIntoViewIfNeeded(); await p.evaluate(()=>scrollBy(0,-120)); await p.screenshot({path:`prev_${w}${slug}table.png`});}
 const c=await p.$('.entry-content > div[style*="border-radius"]'); if(c){await c.scrollIntoViewIfNeeded(); await p.evaluate(()=>scrollBy(0,-200)); await p.screenshot({path:`prev_${w}${slug}cta.png`});}}
console.log(w,u,'match',match,'H',H0,'->',m.H,m.sw>m.iw?'OVERFLOW':'ok');
}catch(e){console.log(w,u,'ERR',e.message.slice(0,80))}}
await ctx.close();}
await b.close();})();
