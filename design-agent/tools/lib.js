const { chromium } = require('playwright');
const UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36';
const UAM='Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
async function ctx(mobile){
 const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',proxy:{server:process.env.HTTPS_PROXY},args:['--disable-blink-features=AutomationControlled']});
 const c=await b.newContext({ignoreHTTPSErrors:true,userAgent:mobile?UAM:UA,viewport:mobile?{width:390,height:844}:{width:1440,height:900},isMobile:!!mobile,hasTouch:!!mobile,deviceScaleFactor:1});
 return {b,c};
}
async function go(p,u){
 for(let i=0;i<4;i++){
  const r=await p.goto(u,{waitUntil:'domcontentloaded',timeout:60000}).catch(e=>null);
  let st=r?r.status():0;
  if(st===403 || (await p.title().catch(()=>''))===''){ await p.waitForTimeout(9000); await p.waitForLoadState('domcontentloaded').catch(()=>{});
    const t=await p.title().catch(()=>''); if(t && !/Checking/.test(await p.innerText('body').catch(()=>'Checking'))) return 200; continue;}
  return st;
 }
 return 403;
}
module.exports={ctx,go};
