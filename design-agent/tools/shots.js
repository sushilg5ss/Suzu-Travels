const {open,go}=require('./lib');
(async()=>{const {b,d,m}=await open(); const url=process.argv[2]; const tag=process.argv[3];
for(const [vn,ctx] of [['d',d],['m',m]]){ const {p}=await go(ctx,url);
 const info=await p.evaluate(()=>{const sw=document.querySelector('.series-widget'); const rp=document.querySelector('.reading-progress-pill');
  return {series: sw&&sw.innerText.slice(0,500), seriesHTML: sw&&sw.outerHTML.slice(0,700), rp: rp&&rp.outerHTML.slice(0,400), rpStyle: rp&&(()=>{const c=getComputedStyle(rp);return c.position+' '+c.display+' '+c.top+' '+c.bottom+' '+c.left+' '+c.right})()}});
 if(vn==='d') console.log(JSON.stringify(info,null,1));
 for (const y of [0,900,2200,4000]){ await p.evaluate(y=>scrollTo(0,y),y); await p.waitForTimeout(700); await p.screenshot({path:`${tag}-${vn}-${y}.png`}); }
 await p.close();}
await b.close();})();
