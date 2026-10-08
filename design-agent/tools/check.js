const {open,go}=require('./lib'); const fs=require('fs');
const tag=process.argv[2]; const bust=process.argv[3]!=='nobust'; const urls=process.argv.slice(4);
(async()=>{const {b,d,m}=await open(); fs.mkdirSync(tag,{recursive:true}); const out=[];
for(const url of urls) for(const [vn,ctx] of [['d',d],['m',m]]){
 let r; try{ const {p,errs,getStatus}=await go(ctx,url,bust);
  r=await p.evaluate(()=>{const vis=s=>[...document.querySelectorAll(s)].some(e=>{const b=e.getBoundingClientRect();const c=getComputedStyle(e);return b.width>0&&b.height>0&&c.visibility!=='hidden'&&c.display!=='none'&&c.opacity!=='0'});
   return {sw:document.documentElement.scrollWidth, iw:innerWidth, nav: vis('.site-header'), wa: vis('a[href*="wa.me"],a[href*="whatsapp"]'), call: vis('a[href^="tel:"]'),
     footerPhone: (document.querySelector('footer')?.textContent||'').replace(/\s/g,'').includes('7087488961'),
     da: !!document.getElementById('wp-custom-css') && document.getElementById('wp-custom-css').textContent.includes('DA-2026-10-09'), h:document.documentElement.scrollHeight}});
  r.status=getStatus(); r.errs=errs.filter(e=>!/Failed to load resource/.test(e)).slice(0,4);
  const name=url.replace('https://suzutravels.com/','').replace(/\/$/,'').replace(/\//g,'_')||'root';
  await p.screenshot({path:`${tag}/${name}-${vn}.png`,fullPage:false});
  await p.close(); } catch(e){ r={err:e.message.slice(0,120)} }
 r.url=url; r.v=vn; r.ok= r.sw<=r.iw; out.push(r); console.log(JSON.stringify(r)); }
fs.writeFileSync(`${tag}/results.json`,JSON.stringify(out,null,1)); await b.close();})();
