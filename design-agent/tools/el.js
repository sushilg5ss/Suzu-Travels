const {open,go}=require('./lib');
(async()=>{const {b,d,m}=await open(); const [url,sel,tag]=process.argv.slice(2);
for(const [vn,ctx] of [['d',d],['m',m]]){ const {p}=await go(ctx,url);
 const e=await p.$(sel); if(!e){console.log('nosel');continue;} await e.scrollIntoViewIfNeeded(); await p.waitForTimeout(600);
 await e.screenshot({path:`${tag}-${vn}.png`});
 if(vn==='d') console.log(await p.evaluate(s=>document.querySelector(s).outerHTML.slice(0,2500),sel));
 await p.close();}
await b.close();})();
