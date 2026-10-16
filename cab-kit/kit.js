(function(){
var P='917087488961';
var AMP='\x26';
function r99(x){return Math.ceil(x/100)*100-1;}
function inr(n){return '₹'+Math.round(n).toLocaleString('en-IN');}
function wa(t){return 'https://wa.me/'+P+'?text='+encodeURIComponent(t);}
function $(i){return document.getElementById(i);}
function qa(s,el){return Array.prototype.slice.call((el||document).querySelectorAll(s));}
var root=document.querySelector('.szc');
var TIERS={prime:1.15,standard:1,saver:0.92};
var TNAME={prime:'Prime (2023+ cars)',standard:'Standard (3-5 yr cars)',saver:'Saver (5-10 yr cars)'};
var tier='standard';
try{var st=localStorage.getItem('szcTier');if(st){if(TIERS[st]){tier=st;}}}catch(e){}
function tmul(){return TIERS[tier]||1;}
function priced(base){var m=tmul();return m===1?base:r99(base*m);}
function paintPrices(){
 qa('[data-inr]').forEach(function(el){el.textContent=inr(priced(+el.getAttribute('data-inr')));});
 qa('[data-km]').forEach(function(el){el.textContent='₹'+Math.round(+el.getAttribute('data-km')*tmul())+'/km';});
 qa('[data-tiername]').forEach(function(el){el.textContent=TNAME[tier].split(' (')[0];});
 qa('.szc-tier button').forEach(function(b){b.classList.toggle('on',b.getAttribute('data-tier')===tier);b.setAttribute('aria-pressed',b.getAttribute('data-tier')===tier?'true':'false');});
 if(root){root.setAttribute('data-tier',tier);}
}
function setTier(t){if(!TIERS[t]){return;}tier=t;try{localStorage.setItem('szcTier',t);}catch(e){}paintPrices();if(window.szcCalc){window.szcCalc();}if(window.szcPlanRefresh){window.szcPlanRefresh();}}
qa('.szc-tier button').forEach(function(b){b.addEventListener('click',function(){setTier(b.getAttribute('data-tier'));});});
paintPrices();

/* ---------- fare calculator ---------- */
var c=$('szc-calc');
if(c){
 var cfg=JSON.parse(c.getAttribute('data-cfg'));
 var mode='one';
 var V={};cfg.v.forEach(function(v){V[v.id]=v;});
 var segs=qa('.szc-seg button',c);
 function calc(){
  var d=cfg.d[+$('szc-cd').value]||cfg.d[0];var v=V[$('szc-cv').value];
  var days=Math.max(1,Math.min(20,parseInt($('szc-cn').value,10)||1));
  var amt,brk,label;
  if(mode==='one'){amt=Math.max(v.m,r99(d.km*v.ow*d.f));brk='One-way drop · '+d.km+' km · fuel, driver and driver allowance included';label='one-way';}
  else{var km=Math.max(2*d.km,250*days);var nights=Math.max(0,days-1);amt=r99(km*v.h)+nights*v.nt;brk='Round trip · about '+km+' km × ₹'+v.h+'/km'+(nights?' + '+nights+' night'+(nights>1?'s':'')+' driver allowance':'');label='round trip, '+days+' day'+(days>1?'s':'');}
  amt=priced(amt);
  $('szc-ca').textContent=inr(amt);$('szc-cb').textContent=brk+' · '+TNAME[tier];
  $('szc-cw').href=wa('Hi Suzu Travels, I want to book '+d.l+' ('+label+') in '+v.n+', '+TNAME[tier]+'. Estimate on your site: '+inr(amt)+'. Date: ___ , people: ___ (page: '+cfg.s+')');
 }
 window.szcCalc=calc;
 segs.forEach(function(b){b.addEventListener('click',function(){segs.forEach(function(x){x.classList.remove('on');});b.classList.add('on');mode=b.getAttribute('data-m');$('szc-cn').disabled=(mode==='one');calc();});});
 ['szc-cd','szc-cv','szc-cn'].forEach(function(i){$(i).addEventListener('change',calc);$(i).addEventListener('input',calc);});
 calc();
}

/* ---------- quote form ---------- */
var f=$('szc-qf');
if(f){
 try{var t=new Date();t.setDate(t.getDate()+1);$('szc-qt').min=new Date().toISOString().slice(0,10);if(!$('szc-qt').value){$('szc-qt').value=t.toISOString().slice(0,10);}}catch(e){}
 var send=function(){
  var m='Hi Suzu Travels, I need a cab.\nPickup: '+($('szc-qp').value||'___')+'\nDrop: '+($('szc-qd').value||'___')+'\nDate: '+($('szc-qt').value||'___')+'\nPeople: '+($('szc-qx').value||'___')+'\nCar: '+$('szc-qv').value+'\nFleet: '+TNAME[tier]+'\nTrip: '+$('szc-qr').value+'\n(page: '+f.getAttribute('data-slug')+')';
  window.open(wa(m),'_blank');
 };
 f.addEventListener('submit',function(e){e.preventDefault();send();});
}

/* ---------- fleet gallery: filters + 3D tilt + viewer ---------- */
var g=$('szc-fleet');
if(g){
 var FL=JSON.parse(g.getAttribute('data-fleet'));
 var FB={};FL.v.forEach(function(v){FB[v.id]=v;});
 var cards=qa('.szc-veh',g);
 var ftype='all',fseat='all';
 function applyF(){
  var n=0;
  cards.forEach(function(cd){
   var ok=true;
   if(ftype!=='all'){if(cd.getAttribute('data-type')!==ftype){ok=false;}}
   if(fseat!=='all'){var s=+cd.getAttribute('data-seats');var lo=+fseat.split('-')[0],hi=+fseat.split('-')[1];if(s<lo||s>hi){ok=false;}}
   cd.hidden=!ok;if(ok){n++;}
  });
  var cnt=$('szc-fcount');if(cnt){cnt.textContent=n+' of '+cards.length+' vehicles';}
  qa('[data-ft]',g).forEach(function(b){b.classList.toggle('on',b.getAttribute('data-ft')===ftype);});
  qa('[data-fs]',g).forEach(function(b){b.classList.toggle('on',b.getAttribute('data-fs')===fseat);});
 }
 qa('[data-ft]',g).forEach(function(b){b.addEventListener('click',function(){ftype=b.getAttribute('data-ft');applyF();});});
 qa('[data-fs]',g).forEach(function(b){b.addEventListener('click',function(){fseat=b.getAttribute('data-fs');applyF();});});
 applyF();
 var fine=window.matchMedia?window.matchMedia('(hover:hover) and (pointer:fine)').matches:false;
 if(fine){
  cards.forEach(function(cd){
   var ph=cd.querySelector('.szc-ph');if(!ph){return;}
   cd.addEventListener('mousemove',function(e){var r=cd.getBoundingClientRect();var x=(e.clientX-r.left)/r.width-0.5,y=(e.clientY-r.top)/r.height-0.5;ph.style.transform='perspective(900px) rotateY('+(x*14)+'deg) rotateX('+(-y*10)+'deg) scale(1.04)';});
   cd.addEventListener('mouseleave',function(){ph.style.transform='';});
  });
 }
 var M=$('szc-modal');
 function fares(v){
  if(v.quote){return '<p class="szc-mq">Priced per trip - tell us the dates and we send the all-in quote on WhatsApp.</p>';}
  var r=FL.ref;var base=Math.max(v.min,r99(r.km*v.ow*r.f));
  var rows=Object.keys(TIERS).map(function(k){var a=TIERS[k]===1?base:r99(base*TIERS[k]);return '<tr class="'+(k===tier?'on':'')+'"><td><b>'+TNAME[k].split(' (')[0]+'</b><br><small>'+TNAME[k].split(' (')[1].replace(')','')+'</small></td><td class="num">'+inr(a)+'</td><td class="num">₹'+Math.round(v.hire*TIERS[k])+'/km</td></tr>';}).join('');
  return '<p class="szc-mref">'+r.l+' one-way · '+r.km+' km</p><table class="szc-mt"><thead><tr><th>Fleet</th><th>One-way from</th><th>Round trip</th></tr></thead><tbody>'+rows+'</tbody></table>';
 }
 function openV(id){
  var v=FB[id];if(!v||!M){return;}
  var img=v.photo?'<img src="'+v.photo+'" alt="'+v.alt+'" width="1280" height="853" decoding="async">':'';
  var specs=['<b>'+v.seats+'</b> seats','<b>'+v.bags+'</b>','AC · '+v.fuel,v.model];
  M.querySelector('.szc-mbody').innerHTML='<div class="szc-mimg">'+img+'</div><div class="szc-minfo"><span class="szc-tag">'+v.model+'</span><h3 id="szc-mt">'+v.name+'</h3><ul class="szc-mspecs">'+specs.map(function(s){return '<li>'+s+'</li>';}).join('')+'</ul><p class="szc-mbest">Best for: '+v.best+'</p>'+fares(v)+'<div class="szc-btns"><a class="szc-btn wa" target="_blank" rel="noopener" href="'+wa('Hi Suzu Travels, I would like a '+v.name+' ('+TNAME[tier]+') for '+FL.ctx+'. Date: ___ , people: ___ (page: '+FL.s+')')+'">WhatsApp quote</a>'+(v.page?'<a class="szc-btn line" href="'+v.page+'">Rates page</a>':'')+'</div>'+(v.credit?'<p class="szc-mcredit">Photo: '+v.credit+'</p>':'')+'</div>';
  M.hidden=false;document.body.style.overflow='hidden';M.querySelector('.szc-mclose').focus();
 }
 function closeV(){if(M){M.hidden=true;document.body.style.overflow='';}}
 qa('[data-view]',g).forEach(function(b){b.addEventListener('click',function(e){e.preventDefault();openV(b.getAttribute('data-view'));});});
 if(M){M.addEventListener('click',function(e){if(e.target===M||e.target.classList.contains('szc-mclose')){closeV();}});document.addEventListener('keydown',function(e){if(e.key==='Escape'){closeV();}});}
}

/* ---------- route planner (hub): geocode + OSRM + MapLibre animation ---------- */
var pl=$('szc-plan');
if(pl){
 var PC=JSON.parse(pl.getAttribute('data-plan'));
 var PV={};PC.v.forEach(function(v){PV[v.id]=v;});
 var map=null,mapReady=false,anim=null,last=null,carEl=null,carMk=null;
 var out=$('szc-pout'),mapBox=$('szc-map');
 function status(t,err){var s=$('szc-pstat');if(s){s.textContent=t;s.className='szc-pstat'+(err?' err':'');}}
 function norm(s){return (s||'').trim().toLowerCase().replace(/\s+/g,' ');}
 function known(name){var n=norm(name);var k=Object.keys(PC.p);for(var i=0;i<k.length;i++){if(norm(k[i])===n){return {name:k[i],lat:PC.p[k[i]][0],lon:PC.p[k[i]][1]};}}for(var j=0;j<k.length;j++){if(norm(k[j]).indexOf(n)===0){if(n.length>=3){return {name:k[j],lat:PC.p[k[j]][0],lon:PC.p[k[j]][1]};}}}return null;}
 function geocode(name){
  var k=known(name);if(k){return Promise.resolve(k);}
  var u='https://photon.komoot.io/api/?q='+encodeURIComponent(name+', India')+AMP+'limit=5'+AMP+'lang=en'+AMP+'bbox=68,6,98,37';
  return fetch(u).then(function(r){return r.json();}).then(function(d){
   var fs=(d.features||[]).filter(function(x){var p=x.properties||{};return p.country==='India'||p.countrycode==='IN';});
   if(!fs.length){throw new Error('Place not found: '+name);}
   var p=fs[0];var pr=p.properties||{};
   return {name:(pr.name||name)+(pr.state?', '+pr.state:''),lat:p.geometry.coordinates[1],lon:p.geometry.coordinates[0]};
  });
 }
 function hav(a,b){var R=6371,dl=(b.lat-a.lat)*Math.PI/180,dn=(b.lon-a.lon)*Math.PI/180;var x=Math.sin(dl/2)*Math.sin(dl/2)+Math.cos(a.lat*Math.PI/180)*Math.cos(b.lat*Math.PI/180)*Math.sin(dn/2)*Math.sin(dn/2);return 2*R*Math.asin(Math.sqrt(x));}
 function dec6(str){var idx=0,lat=0,lng=0,coords=[];while(idx<str.length){var b,shift=0,res=0;do{b=str.charCodeAt(idx++)-63;res|=(b%32)<<shift;shift+=5;}while(b>=32);lat+=((res%2)?~(res>>1):(res>>1));shift=0;res=0;do{b=str.charCodeAt(idx++)-63;res|=(b%32)<<shift;shift+=5;}while(b>=32);lng+=((res%2)?~(res>>1):(res>>1));coords.push([lng/1e6,lat/1e6]);}return coords;}
 function route(a,b){
  var q='/route/v1/driving/'+a.lon+','+a.lat+';'+b.lon+','+b.lat+'?overview=full'+AMP+'geometries=polyline6'+AMP+'steps=false';
  var hosts=['https://routing.openstreetmap.de/routed-car','https://router.project-osrm.org'];
  function tryHost(i){
   if(i>=hosts.length){return Promise.reject(new Error('no routing'));}
   return fetch(hosts[i]+q).then(function(r){return r.json();}).then(function(d){if(d.code!=='Ok'){throw new Error(d.code);}var r=d.routes[0];return {km:r.distance/1000,hrs:r.duration/3600,coords:dec6(r.geometry)};}).catch(function(){return tryHost(i+1);});
  }
  return tryHost(0);
 }
 function matchRoute(a,b){var na=norm(a.name.split(',')[0]),nb=norm(b.name.split(',')[0]);for(var i=0;i<PC.r.length;i++){var r=PC.r[i];if((norm(r.a)===na?norm(r.b)===nb:false)||(norm(r.a)===nb?norm(r.b)===na:false)){return r;}}return null;}
 function factorFor(km,hrs,b){
  if(b.lat>32.5){if(b.lon<76.2){return 1.7;}}
  if(b.lat>33){if(b.lon>76.5){return 1.6;}}
  var v=hrs>0?km/hrs:50;
  return v>=58?0.85:(v>=44?1.0:(v>=34?1.1:1.3));
 }
 function fmtH(h,fct){var k=fct>=1.3?1.55:(fct>=1.1?1.4:(fct>=1?1.25:1.12));var lo=h*k,hi=h*k*1.18;function f(x){var q=Math.round(x*4)/4,w=Math.floor(q),m=Math.round((q-w)*60);return m===0?w+' h':w+' h '+m+' m';}var a=f(lo),b=f(hi);return a===b?a:a+' – '+b;}
 function loadMap(cb){
  if(window.maplibregl){cb();return;}
  var l=document.createElement('link');l.rel='stylesheet';l.href=PC.css;document.head.appendChild(l);
  var s=document.createElement('script');s.src=PC.js;s.async=true;s.onload=cb;s.onerror=function(){status('Map could not load - fares and WhatsApp still work.',true);};document.head.appendChild(s);
 }
 function ensureMap(cb){
  loadMap(function(){
   if(map){if(mapReady){cb();}else{map.once('load',cb);}return;}
   map=new maplibregl.Map({container:'szc-map',style:'https://tiles.openfreemap.org/styles/liberty',center:[77.2,30.9],zoom:6,pitch:0,attributionControl:{compact:true},cooperativeGestures:true,maxBounds:[[66,16],[92,38]]});
   map.addControl(new maplibregl.NavigationControl({showCompass:false}),'top-right');
   map.on('load',function(){
    try{map.getStyle().layers.forEach(function(L){if(L['source-layer']==='boundary'){map.setLayoutProperty(L.id,'visibility','none');}});}catch(e){}
    map.addSource('rt',{type:'geojson',data:{type:'FeatureCollection',features:[]}});
    map.addSource('pg',{type:'geojson',data:{type:'FeatureCollection',features:[]}});
    map.addLayer({id:'rt-casing',type:'line',source:'rt',paint:{'line-color':'#122615','line-width':9,'line-opacity':0.18},layout:{'line-cap':'round','line-join':'round'}});
    map.addLayer({id:'rt-line',type:'line',source:'rt',paint:{'line-color':'#9aa89d','line-width':4,'line-dasharray':[1,2]},layout:{'line-cap':'round','line-join':'round'}});
    map.addLayer({id:'pg-glow',type:'line',source:'pg',paint:{'line-color':'#d4af37','line-width':12,'line-opacity':0.25,'line-blur':6},layout:{'line-cap':'round','line-join':'round'}});
    map.addLayer({id:'pg-line',type:'line',source:'pg',paint:{'line-color':'#2e7d32','line-width':5},layout:{'line-cap':'round','line-join':'round'}});
    mapReady=true;cb();
   });
  });
 }
 function pin(txt,cls){var d=document.createElement('div');d.className='szc-pin '+cls;d.innerHTML='<span>'+txt+'</span>';return d;}
 var mks=[];
 function draw(res,a,b){
  mks.forEach(function(m){m.remove();});mks=[];
  var line={type:'Feature',geometry:{type:'LineString',coordinates:res.coords}};
  map.getSource('rt').setData(line);map.getSource('pg').setData({type:'FeatureCollection',features:[]});
  var bb=res.coords.reduce(function(o,c){return [Math.min(o[0],c[0]),Math.min(o[1],c[1]),Math.max(o[2],c[0]),Math.max(o[3],c[1])];},[999,999,-999,-999]);
  var mob=window.innerWidth<700;
  map.fitBounds([[bb[0],bb[1]],[bb[2],bb[3]]],{padding:mob?{top:60,bottom:60,left:40,right:40}:{top:80,bottom:80,left:90,right:90},pitch:mob?30:45,bearing:0,duration:1200,maxZoom:11});
  mks.push(new maplibregl.Marker({element:pin(a.name.split(',')[0],'a'),anchor:'bottom'}).setLngLat(res.coords[0]).addTo(map));
  mks.push(new maplibregl.Marker({element:pin(b.name.split(',')[0],'b'),anchor:'bottom'}).setLngLat(res.coords[res.coords.length-1]).addTo(map));
  if(!carEl){carEl=document.createElement('div');carEl.className='szc-car';carEl.innerHTML='<svg viewBox="0 0 48 48" width="34" height="34" aria-hidden="true"><circle cx="24" cy="24" r="22" fill="#122615"/><path d="M12 28l3-8c.4-1 1.3-1.6 2.3-1.6h13.4c1 0 1.9.6 2.3 1.6l3 8v7a1.5 1.5 0 0 1-1.5 1.5h-2A1.5 1.5 0 0 1 31 35v-2H17v2a1.5 1.5 0 0 1-1.5 1.5h-2A1.5 1.5 0 0 1 12 35z" fill="#d4af37"/><circle cx="17" cy="29" r="2" fill="#122615"/><circle cx="31" cy="29" r="2" fill="#122615"/><path d="M16.5 20.5h15l1.6 4.5H14.9z" fill="#122615" opacity=".55"/></svg>';}
  if(carMk){carMk.remove();}
  carMk=new maplibregl.Marker({element:carEl,rotationAlignment:'map'}).setLngLat(res.coords[0]).addTo(map);
  play(res);
 }
 function play(res){
  if(anim){cancelAnimationFrame(anim);}
  var cs=res.coords,cum=[0],tot=0;
  for(var i=1;i<cs.length;i++){tot+=hav({lat:cs[i-1][1],lon:cs[i-1][0]},{lat:cs[i][1],lon:cs[i][0]});cum.push(tot);}
  var dur=Math.max(5000,Math.min(11000,tot*18)),t0=null;
  function step(ts){
   if(t0===null){t0=ts;}
   var p=Math.min(1,(ts-t0)/dur);p=p<0.5?2*p*p:-1+(4-2*p)*p;
   var d=p*tot,j=1;while(j<cs.length-1){if(cum[j]>=d){break;}j++;}
   var seg=cum[j]-cum[j-1],f=seg>0?(d-cum[j-1])/seg:0;
   var pt=[cs[j-1][0]+(cs[j][0]-cs[j-1][0])*f,cs[j-1][1]+(cs[j][1]-cs[j-1][1])*f];
   var prog=cs.slice(0,j);prog.push(pt);
   map.getSource('pg').setData({type:'Feature',geometry:{type:'LineString',coordinates:prog}});
   carMk.setLngLat(pt);
   var ang=Math.atan2(cs[j][0]-cs[j-1][0],cs[j][1]-cs[j-1][1])*180/Math.PI;carMk.setRotation(ang);
   if(p<1){anim=requestAnimationFrame(step);}else{anim=null;}
  }
  anim=requestAnimationFrame(step);
 }
 function render(res,a,b){
  var kr=matchRoute(a,b);
  var km=kr?kr.km:Math.round(res.km),fct=kr?kr.f:factorFor(res.km,res.hrs,b);
  var tm=kr?(kr.t||fmtH(res.hrs,fct)):fmtH(res.hrs,fct);
  var vid=$('szc-pv').value,v=PV[vid];
  var trip=$('szc-pm').value,date=$('szc-pd').value||'___',ppl=$('szc-pn').value||'___';
  var isRound=trip==='round';
  function amtFor(vv,k){
   if(vv.quote){return null;}
   var base;
   if(isRound){var kmr=Math.max(2*km,250),base2=r99(kmr*vv.h);base=base2;}
   else{base=Math.max(vv.m,r99(km*vv.ow*fct));}
   return TIERS[k]===1?base:r99(base*TIERS[k]);
  }
  var tiersHtml=Object.keys(TIERS).map(function(k){var a2=amtFor(v,k);return '<button type="button" class="szc-ptier'+(k===tier?' on':'')+'" data-tier="'+k+'"><span class="n">'+TNAME[k].split(' (')[0]+'</span><span class="s">'+TNAME[k].split(' (')[1].replace(')','')+'</span><span class="a">'+(a2===null?'On quote':inr(a2))+'</span></button>';}).join('');
  var all=PC.v.filter(function(x){return !x.quote;}).map(function(x){var a3=amtFor(x,tier);return '<li'+(x.id===vid?' class="on"':'')+'><span>'+x.n+' <small>'+x.seats+' seats</small></span><b>'+inr(a3)+'</b></li>';}).join('');
  var est=amtFor(v,tier);
  var msg='Hi Suzu Travels, I planned a route on your site.\nFrom: '+a.name+'\nTo: '+b.name+'\nDistance: ~'+km+' km ('+(isRound?'round trip':'one-way')+')\nCar: '+v.n+' - '+TNAME[tier]+'\nEstimate shown: '+(est===null?'on quote':inr(est))+'\nDate: '+date+'\nPeople: '+ppl+'\n(page: cabs planner)';
  var pageLink=kr?(kr.u?'<a class="szc-btn line" href="'+kr.u+'">Full '+kr.a+' → '+kr.b+' route page</a>':''):'';
  out.innerHTML='<div class="szc-pres"><div class="szc-pfacts"><div><span class="k">Distance</span><span class="v">'+km+' km</span></div><div><span class="k">Drive time</span><span class="v">'+tm+'</span></div><div><span class="k">Car</span><span class="v">'+v.n+'</span></div><div><span class="k">Trip</span><span class="v">'+(isRound?'Round trip':'One-way drop')+'</span></div></div>'
   +'<p class="szc-plbl">Choose your fleet - same route, three price points</p><div class="szc-ptiers">'+tiersHtml+'</div>'
   +'<details class="szc-pall"><summary>Compare all cars at '+TNAME[tier].split(' (')[0]+' rates</summary><ul>'+all+'</ul></details>'
   +'<p class="szc-pnote">Fuel, driver and driver allowance included. Tolls, parking and state entry tax extra at actuals. Indicative '+(isRound?'2-day round trip (250 km/day minimum)':'off-season fare')+' - your WhatsApp quote is the final price.</p>'
   +'<div class="szc-btns"><a class="szc-btn gold" target="_blank" rel="noopener" href="'+wa(msg)+'">Lock this fare on WhatsApp</a><a class="szc-btn line" href="#enquiry">Request a call back</a>'+pageLink+'<button type="button" class="szc-btn line" id="szc-replay">Replay route</button></div></div>';
  qa('.szc-ptier',out).forEach(function(b){b.addEventListener('click',function(){setTier(b.getAttribute('data-tier'));});});
  var rp=$('szc-replay');if(rp){rp.addEventListener('click',function(){if(last){play(last.res);}});}
 }
 window.szcPlanRefresh=function(){if(last){render(last.res,last.a,last.b);}};
 function run(){
  var A=$('szc-fa').value,B=$('szc-fb').value;
  if(!A||!B){status('Type a pickup and a drop city.',true);return;}
  if(norm(A)===norm(B)){status('Pickup and drop are the same place.',true);return;}
  status('Finding the road route…');pl.classList.add('busy');
  try{pl.scrollIntoView({behavior:'smooth',block:'start'});}catch(e){}
  Promise.all([geocode(A),geocode(B)]).then(function(ab){
   var a=ab[0],b=ab[1];
   return route(a,b).catch(function(){var km=hav(a,b)*1.3;return {km:km,hrs:km/42,coords:[[a.lon,a.lat],[b.lon,b.lat]],fallback:true};}).then(function(res){
    last={res:res,a:a,b:b};
    render(res,a,b);
    status(res.fallback?'Live road map unavailable right now - showing straight-line estimate.':a.name.split(',')[0]+' → '+b.name.split(',')[0]+' by road',res.fallback);
    pl.classList.remove('busy');pl.classList.add('has');
    ensureMap(function(){draw(res,a,b);});
   });
  }).catch(function(e){pl.classList.remove('busy');status((e.message||'Could not find that place')+' - try a nearby town or send it on WhatsApp.',true);});
 }
 pl.addEventListener('submit',function(e){e.preventDefault();run();});
 ['szc-pv','szc-pm'].forEach(function(i){var el=$(i);if(el){el.addEventListener('change',function(){if(last){render(last.res,last.a,last.b);}});}});
 var fd=$('szc-find');
 if(fd){fd.addEventListener('submit',function(e){e.preventDefault();$('szc-fa').value=$('szc-ha').value;$('szc-fb').value=$('szc-hb').value;if($('szc-hd').value){$('szc-pd').value=$('szc-hd').value;}run();});}
 qa('[data-plan-route]').forEach(function(el){el.addEventListener('click',function(e){e.preventDefault();var r=el.getAttribute('data-plan-route').split('>');$('szc-fa').value=r[0];$('szc-fb').value=r[1];run();});});
 try{var io=new IntersectionObserver(function(en){en.forEach(function(x){if(x.isIntersecting){io.disconnect();ensureMap(function(){});}});},{rootMargin:'400px'});io.observe(mapBox);}catch(e){}
}
})();
