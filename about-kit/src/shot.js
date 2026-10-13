// usage: node shot.js <file-or-url> <out.png> [width] [height] [fullPage 0/1] [waitms]
const { chromium } = require('/opt/npm-tools/node_modules/playwright');
(async()=>{
 const [,,src,out,w='1440',h='900',full='1',wait='800']=process.argv;
 const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'}).catch(()=>chromium.launch());
 const p=await b.newPage({viewport:{width:+w,height:+h},deviceScaleFactor:1});
 const url=/^https?:/.test(src)?src:'file://'+require('path').resolve(src);
 await p.goto(url,{waitUntil:'load',timeout:90000});
 await p.waitForTimeout(+wait);
 const info=await p.evaluate(()=>({sw:document.documentElement.scrollWidth,cw:document.documentElement.clientWidth,h1:document.querySelectorAll('h1').length,H:document.documentElement.scrollHeight}));
 console.log(JSON.stringify(info));
 await p.screenshot({path:out,fullPage:full==='1'});
 await b.close();
})();
