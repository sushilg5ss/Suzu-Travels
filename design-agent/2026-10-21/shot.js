const { chromium } = require('/opt/npm-tools/node_modules/playwright');
const [,, tag, urlsFile, cb] = process.argv;
const urls = require('fs').readFileSync(urlsFile,'utf8').trim().split('\n');
const UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36';
(async()=>{
 const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'}).catch(()=>chromium.launch());
 const out=[];
 for (const [w,h,mob] of [[1440,900,false],[390,844,true]]) {
  const ctx=await b.newContext({viewport:{width:w,height:h},userAgent:mob?UA.replace('Windows NT 10.0; Win64; x64','Linux; Android 14; Pixel 8')+' Mobile':UA,isMobile:mob,hasTouch:mob,deviceScaleFactor:1});
  let first=true; for (const u of urls) {
   const p=await ctx.newPage(); const errs=[];
   p.on('console',m=>{if(m.type()==='error')errs.push(m.text().slice(0,120))});
   const url = cb==='nocb'? u : u+(u.includes('?')?'&':'?')+'da='+Math.random().toString(36).slice(2,8);
   let st=0; try{const r=await p.goto(url,{waitUntil:'domcontentloaded',timeout:60000}); st=r.status(); await p.waitForTimeout(first?9000:3000); first=false; await p.waitForLoadState('load');}catch(e){st='ERR '+e.message.slice(0,60)}
   let m={};
   try{ m=await p.evaluate(()=>{const v=s=>{const e=document.querySelector(s);if(!e)return null;const r=e.getBoundingClientRect();const cs=getComputedStyle(e);return cs.display!=='none'&&cs.visibility!=='hidden'&&r.width>0&&r.height>0};
     return {sw:document.documentElement.scrollWidth,iw:innerWidth,H:document.documentElement.scrollHeight,
       hdr:v('header')||v('#masthead')||v('.site-header'), cta:v('#szcta'), tel:[...document.querySelectorAll('a[href^="tel:"]')].map(a=>a.getAttribute('href')).filter((x,i,a)=>a.indexOf(x)===i).slice(0,4),
       wa:!!document.querySelector('a[href*="wa.me"],a[href*="whatsapp"]'), da21:[...document.styleSheets].some(s=>{try{return [...s.cssRules].some(r=>r.cssText.includes('p:first-child'))}catch(e){return false}}) || document.documentElement.outerHTML.includes('DA-2026-10-21')}});}catch(e){}
   const slug=u.replace(/https?:\/\/[^/]+/,'').replace(/[^a-z0-9]+/gi,'_').replace(/^_|_$/g,'')||'root';
   await p.screenshot({path:`${tag}_${w}_${slug}.png`,fullPage:false}).catch(()=>{});
   out.push({w,u,st,...m,errs:errs.length});
   await p.close();
  }
  await ctx.close();
 }
 await b.close();
 require('fs').writeFileSync(`${tag}.json`,JSON.stringify(out,null,1));
 for(const o of out) console.log(o.w,o.st,o.sw>o.iw?'OVERFLOW '+o.sw:'ok',o.H,'hdr',o.hdr,'cta',o.cta,'wa',o.wa,o.tel&&o.tel.join(','),'err',o.errs,'da21',o.da21,o.u);
})();
