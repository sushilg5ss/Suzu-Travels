const { chromium } = require('playwright');
const UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36';
const UAM='Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Mobile Safari/537.36';
async function open(){ const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--disable-blink-features=AutomationControlled']});
 const d=await b.newContext({userAgent:UA,viewport:{width:1440,height:900}});
 const m=await b.newContext({userAgent:UAM,viewport:{width:390,height:844},isMobile:true,hasTouch:true,deviceScaleFactor:1});
 return {b,d,m};}
async function go(ctx,url,bust=true){ const p=await ctx.newPage(); const errs=[];
 p.on('console',m=>{if(m.type()==='error')errs.push(m.text().slice(0,160))}); p.on('pageerror',e=>errs.push('PE '+e.message.slice(0,160)));
 let status=0; p.on('response',r=>{ if(r.request().isNavigationRequest() && r.frame()===p.mainFrame()) status=r.status();});
 const u=bust? url+(url.includes('?')?'&':'?')+'da='+Date.now()+Math.random().toString(36).slice(2,6):url;
 await p.goto(u,{waitUntil:'domcontentloaded',timeout:90000});
 for(let i=0;i<30;i++){ let t='Checking your browser'; try{t=await p.title();}catch(e){} if(!/Checking your browser/.test(t)) break; await p.waitForTimeout(1000);}
 try{await p.waitForLoadState('load',{timeout:30000});}catch(e){}
 await p.waitForTimeout(2000);
 return {p,errs,getStatus:()=>status};}
module.exports={open,go};
