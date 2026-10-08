const {open,go}=require('./lib'); const fs=require('fs'); const css=fs.readFileSync('new-block.css','utf8');
(async()=>{const {b,d,m}=await open(); const [url,tag]=process.argv.slice(2);
for(const [vn,ctx] of [['d',d],['m',m]]){ const {p}=await go(ctx,url); await p.addStyleTag({content:css}); await p.waitForTimeout(500);
 const H=await p.evaluate(()=>document.documentElement.scrollHeight);
 for(const f of [0.08,0.45]){ await p.evaluate(y=>scrollTo(0,y),Math.round(H*f)); await p.waitForTimeout(600); await p.screenshot({path:`${tag}-${vn}-${f}.png`}); }
 const e=await p.$('.popular-destinations-section'); if(e){await e.scrollIntoViewIfNeeded(); await p.waitForTimeout(400); await e.screenshot({path:`${tag}-${vn}-pop.png`});}
 console.log(vn, await p.evaluate(()=>({sw:document.documentElement.scrollWidth,iw:innerWidth, bar:getComputedStyle(document.body,'::before').transform})));
 await p.close();}
await b.close();})();
