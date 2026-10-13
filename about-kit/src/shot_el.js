const { chromium } = require('/opt/npm-tools/node_modules/playwright');
(async()=>{
 const [,,src,out,w,h,sel]=process.argv;
 const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
 const p=await b.newPage({viewport:{width:+w,height:+h}});
 await p.goto('file://'+require('path').resolve(src),{waitUntil:'load'});
 if(sel){await p.evaluate(s=>{const e=document.querySelector(s);window.scrollTo(0,e.getBoundingClientRect().top+scrollY-130)},sel);}
 await p.waitForTimeout(2500);
 await p.screenshot({path:out});
 await b.close();
})();
