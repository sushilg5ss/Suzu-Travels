const { chromium } = require('/opt/npm-tools/node_modules/playwright');
(async()=>{
 const [,,src,out,w='1440',wait='2500']=process.argv;
 const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
 const p=await b.newPage({viewport:{width:+w,height:900}});
 const url=/^https?:/.test(src)?src:'file://'+require('path').resolve(src);
 await p.goto(url,{waitUntil:'load',timeout:90000});
 const H=await p.evaluate(()=>document.documentElement.scrollHeight);
 await p.setViewportSize({width:+w,height:H});
 await p.waitForTimeout(+wait);
 const info=await p.evaluate(()=>({sw:document.documentElement.scrollWidth,cw:document.documentElement.clientWidth,h1:document.querySelectorAll('h1').length,H:document.documentElement.scrollHeight,over:[...document.querySelectorAll('.szab *')].filter(e=>{const r=e.getBoundingClientRect();return r.right>document.documentElement.clientWidth+1&&getComputedStyle(e).position!=='fixed'&&!e.closest('.ab-track,.ab-rv,.ab-nav')}).slice(0,8).map(e=>e.className&&e.className.baseVal!==undefined?e.className.baseVal:e.className)}));
 console.log(JSON.stringify(info));
 await p.screenshot({path:out,fullPage:false});
 await b.close();
})();
