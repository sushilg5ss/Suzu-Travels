const {chromium,devices}=require('playwright');const fs=require('fs');
(async()=>{
 const h=fs.readFileSync('/home/claude/hp/after.html','utf8').replace('<head>','<head><base href="https://suzutravels.com/">');
 fs.writeFileSync('/home/claude/hp/after-local.html',h);
 const b=await chromium.launch({args:['--autoplay-policy=no-user-gesture-required']});
 const R={};
 for (const [name,ctx] of [['desktop',{viewport:{width:1440,height:900}}],['mobile',devices['Pixel 7']]]){
  const c=await b.newContext(ctx); const p=await c.newPage();
  const errs=[],posts=[];
  p.on('pageerror',e=>errs.push(String(e).slice(0,200))); p.on('console',m=>{if(m.type()==='error'&&!/CORS|ERR_FAILED|suzu-(reviews|weather|blog)/.test(m.text()))errs.push(m.text().slice(0,200))});
  p.on('request',r=>{if(r.method()==='POST')posts.push(r.url().slice(0,100))});
  await p.route('**/wp-admin/admin-ajax.php',r=>r.fulfill({status:200,body:'{}'}));
  await p.goto('file:///home/claude/hp/after-local.html',{waitUntil:'load',timeout:90000});
  await p.waitForTimeout(3000);
  const r={};
  const clk=async sel=>{await p.evaluate(()=>{const h=document.getElementById('hero-search');if(h)h.classList.remove('active')});await p.evaluate(s=>{const e=document.querySelector(s);e.scrollIntoView({block:'center'});e.click()},sel);};
  // hero raf gating: count frames while hero visible vs scrolled away
  r.rafHeroVisible=await p.evaluate(()=>new Promise(res=>{let n=0;const o=requestAnimationFrame;let c=0;const t0=performance.now();(function f(){c++;if(performance.now()-t0<600)requestAnimationFrame(f);else res(c)})()}));
  await p.locator('#nz-toolkit').scrollIntoViewIfNeeded(); await p.waitForTimeout(800);
  r.tabs=await p.$$eval('#nz-toolkit .nz-tk-tab',e=>e.length);
  r.costBig=await p.$eval('#nz-tk-big',e=>e.textContent);
  r.costTotalVisible=await p.$eval('#nz-tk-co',e=>e.offsetHeight>100);
  await p.screenshot({path:`/home/claude/hp/tk-${name}-cost.png`});
  // change travellers + tier + month
  await clk('#nz-tk-cf .nz-tk-step button[data-d="1"]'); await clk('#nz-tk-tier button[data-t="2"]');
  await p.selectOption('#nz-tk-m',{index:6}); await p.waitForTimeout(700);
  r.costAfter=await p.$eval('#nz-tk-co',e=>({big:e.querySelector('.big').textContent,n:e.querySelector('.k').textContent,wa:e.querySelector('a[href*="wa.me"]').href.length}));
  // view itinerary deep link opens trip sheet
  await clk('#nz-tk-co a[href^="#trip-"]'); await p.waitForTimeout(900);
  r.sheetOpen=await p.evaluate(()=>!document.getElementById('nz-sheet').hidden&&document.documentElement.classList.contains('nz-open'));
  await p.keyboard.press('Escape'); await p.waitForTimeout(500);
  // distance
  await clk('#nz-tk-t-dist'); await p.waitForTimeout(500);
  r.dist=await p.$eval('#nz-tk-km',e=>e.textContent.replace(/\s+/g,' ').trim());
  r.distLink=await p.$eval('#nz-tk-do a.nz-btn-gold',e=>e.href);
  await clk('#nz-tk-dq button:nth-child(5)'); await p.waitForTimeout(300);
  r.distKaza=await p.$eval('#nz-tk-km',e=>e.textContent.replace(/\s+/g,' ').trim());
  await p.selectOption('#nz-tk-to','Agra'); await p.waitForTimeout(300);
  r.distUnknown=await p.$eval('#nz-tk-dn',e=>e.textContent.slice(0,60));
  await p.screenshot({path:`/home/claude/hp/tk-${name}-dist.png`});
  // packing
  await clk('#nz-tk-t-pack'); await p.waitForTimeout(500);
  r.packItems=await p.$$eval('#nz-tk-pkl input',e=>e.length);
  await p.evaluate(()=>{const i=document.querySelectorAll('#nz-tk-pkl input');i[0].click();i[1].click()});
  r.packProg=await p.$eval('#nz-tk-pc',e=>e.textContent);
  await clk('#nz-tk-pkk button[data-k="altitude"]'); await p.waitForTimeout(300);
  r.packAlt=await p.$$eval('#nz-tk-pkl input',e=>e.length);
  r.packWa=await p.$eval('#nz-tk-pwa',e=>e.href.length);
  await p.screenshot({path:`/home/claude/hp/tk-${name}-pack.png`});
  // help
  await clk('#nz-tk-t-help'); await p.waitForTimeout(500);
  r.helpCards=await p.$$eval('#nz-tk-p-help .nz-tk-hc',e=>e.length);
  r.helpExt=await p.$$eval('#nz-tk-p-help a[target=_blank]',e=>e.map(a=>a.href));
  await p.screenshot({path:`/home/claude/hp/tk-${name}-help.png`});
  // fest
  await clk('#nz-tk-t-fest'); await p.waitForTimeout(500);
  r.fest=await p.$$eval('#nz-tk-fl .nz-tk-fe',e=>e.slice(0,4).map(a=>a.querySelector('h4').textContent+' | '+a.querySelector('.in').textContent));
  r.festCount=await p.$$eval('#nz-tk-fl .nz-tk-fe',e=>e.length);
  await p.screenshot({path:`/home/claude/hp/tk-${name}-fest.png`});
  // keyboard: arrow on tabs
  await p.focus('#nz-tk-t-fest'); await p.keyboard.press('ArrowRight'); await p.waitForTimeout(200);
  r.kbTab=await p.$eval('.nz-tk-tab[aria-selected=true]',e=>e.id);
  // overflow + raf when hero off-screen
  r.hscroll=await p.evaluate(()=>document.documentElement.scrollWidth-document.documentElement.clientWidth);
  r.rafOffscreen=await p.evaluate(()=>new Promise(res=>{let c=0;const t0=performance.now();(function f(){c++;if(performance.now()-t0<600)requestAnimationFrame(f);else res(c)})()}));
  r.heroRafFlag=await p.evaluate(()=>{const v=document.querySelector('video.nz-film');return v?{paused:v.paused,t:+v.currentTime.toFixed(1)}:null});
  // szx sections visible + styled
  r.szx=await p.evaluate(()=>['plan-trip','when-to-go','how-it-works'].map(id=>{const e=document.getElementById(id);const cs=getComputedStyle(e);return id+':'+e.offsetHeight+'px/'+cs.backgroundColor}));
  // hash deep link to tab
  await p.goto('file:///home/claude/hp/after-local.html#toolkit-pack',{waitUntil:'load'}); await p.waitForTimeout(2500);
  r.hashTab=await p.$eval('.nz-tk-tab[aria-selected=true]',e=>e.id);
  r.errors=[...new Set(errs)]; r.posts=posts;
  R[name]=r; await c.close();
 }
 console.log(JSON.stringify(R,null,1)); await b.close();
})();
