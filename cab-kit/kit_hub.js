/* kit_hub.js - hub-only planner extension: multi-stop trips (ENHANCEMENTS #4, 25 Oct 2026).
   build.py inserts this INSIDE the planner block of kit.js (after the IntersectionObserver line) for the hub only,
   so it can reuse geocode/route/draw/render and re-point run/render. Child pages keep plain kit.js.
   Same rules as kit.js: ES5, no ampersand character, no double-slash comments, HTML only in single-quoted strings. */
/* Pickup presets + full place list (ENHANCEMENTS #6, 27 Oct 2026): the HTML datalist carries route cities + pickup points only; the other PLACES are appended here. */
var dlp=$('szc-places');
if(dlp){var dlHave={};qa('option',dlp).forEach(function(o){dlHave[o.value]=1;});Object.keys(PC.p).sort().forEach(function(k){if(!dlHave[k]){var o=document.createElement('option');o.value=k;dlp.appendChild(o);}});}
var vbox=$('szc-pvias'),vadd=$('szc-padd'),hubAddVia=null;
if(vbox){if(vadd){
 var MAXV=3,run1=run,render1=render;
 var vlist=$('szc-pvlist');
 function vIns(){return qa('input.szc-vin',vlist);}
 function vVals(){return vIns().map(function(i){return i.value.trim();}).filter(function(x){return x.length>0;});}
 function relabel(){
  vIns().forEach(function(inp,i){inp.setAttribute('aria-label','Stop '+(i+1));inp.parentNode.querySelector('.szc-vn').textContent=(i+1)+'';});
  vadd.hidden=vIns().length>=MAXV;
  vbox.classList.toggle('on',vIns().length>0);
 }
 function addVia(val){
  if(vIns().length>=MAXV){return null;}
  var row=document.createElement('div');row.className='szc-vrow';
  row.innerHTML='<span class="szc-vn"></span><input class="szc-vin" type="text" list="szc-places" placeholder="Stop on the way, e.g. Kasol" autocomplete="off"><button type="button" class="szc-vx" aria-label="Remove this stop">×</button>';
  vlist.appendChild(row);
  var inp=row.querySelector('input');if(val){inp.value=val;}
  row.querySelector('.szc-vx').addEventListener('click',function(){vlist.removeChild(row);relabel();if(last){run(true);}});
  relabel();return inp;
 }
 function clearVias(){vlist.innerHTML='';relabel();}
 vadd.addEventListener('click',function(){var i=addVia('');if(i){i.focus();}});
 var dy=$('szc-pdy');
 function syncMode(){pl.classList.toggle('round',$('szc-pm').value==='round');}
 $('szc-pm').addEventListener('change',syncMode);syncMode();
 var dyV='';
 function dyChg(){if(dy.value===dyV){return;}dyV=dy.value;if(last){if(last.pts){render(last.res,last.a,last.b);}}}
 if(dy){dy.addEventListener('input',dyChg);dy.addEventListener('change',dyChg);}
 document.addEventListener('click',function(e){var t=e.target;if(t.closest){if(t.closest('[data-plan-route]')){clearVias();}}},true);
 document.addEventListener('submit',function(e){if(e.target.id==='szc-find'){clearVias();}},true);
 function hk(f){return f>=1.3?1.55:(f>=1.1?1.4:(f>=1?1.25:1.12));}
 function hm(x){var q=Math.round(x*4)/4,w=Math.floor(q),m=Math.round((q-w)*60);return m===0?w+' h':w+' h '+m+' m';}
 function routeMulti(pts){
  var q='/route/v1/driving/'+pts.map(function(p){return p.lon+','+p.lat;}).join(';')+'?overview=full'+AMP+'geometries=polyline6'+AMP+'steps=false';
  var hosts=['https://routing.openstreetmap.de/routed-car','https://router.project-osrm.org'];
  function tryHost(i){
   if(i>=hosts.length){return Promise.reject(new Error('no routing'));}
   return fetch(hosts[i]+q).then(function(r){return r.json();}).then(function(d){
    if(d.code!=='Ok'){throw new Error(d.code);}
    var r=d.routes[0];
    return {km:r.distance/1000,hrs:r.duration/3600,coords:dec6(r.geometry),legs:r.legs.map(function(L){return {km:L.distance/1000,hrs:L.duration/3600};})};
   }).catch(function(){return tryHost(i+1);});
  }
  return tryHost(0);
 }
 function straight(pts){
  var legs=[],cs=[],tot=0;
  for(var i=0;i<pts.length;i++){cs.push([pts[i].lon,pts[i].lat]);if(i>0){var k=hav(pts[i-1],pts[i])*1.3;legs.push({km:k,hrs:k/42});tot+=k;}}
  return {km:tot,hrs:tot/42,coords:cs,legs:legs,fallback:true};
 }
 function back(b,a){var kr=matchRoute(b,a);if(kr){return Promise.resolve({km:kr.km});}return route(b,a).catch(function(){return {km:hav(b,a)*1.3};});}
 run=function(auto){
  var vs=vVals();
  pl.classList.toggle('multi',vs.length>0);
  if(!vs.length){return run1(auto);}
  var A=$('szc-fa').value,B=$('szc-fb').value;
  if(!A||!B){status('Type a pickup and a drop city.',true);return;}
  var names=[A].concat(vs,[B]);
  for(var i=1;i<names.length;i++){if(norm(names[i])===norm(names[i-1])){status('Two stops in a row are the same place - remove one.',true);return;}}
  status('Finding the road route via '+vs.join(', ')+'…');pl.classList.add('busy');
  if(!auto){try{pl.scrollIntoView({behavior:'smooth',block:'start'});}catch(e){}}
  Promise.all(names.map(geocode)).then(function(pts){
   var a=pts[0],b=pts[pts.length-1];
   return Promise.all([routeMulti(pts).catch(function(){return straight(pts);}),back(b,a)]).then(function(rr){
    var res=rr[0];res.back=rr[1];
    last={res:res,a:a,b:b,pts:pts};
    render(res,a,b);
    status(res.fallback?'Live road map unavailable right now - showing straight-line estimate.':pts.map(function(p){return p.name.split(',')[0];}).join(' → ')+' by road',res.fallback);
    pl.classList.remove('busy');pl.classList.add('has');
    ensureMap(function(){
     draw(res,a,b);
     for(var j=1;j<pts.length-1;j++){mks.push(new maplibregl.Marker({element:pin(j+'. '+pts[j].name.split(',')[0],'v'),anchor:'bottom'}).setLngLat([pts[j].lon,pts[j].lat]).addTo(map));}
    });
   });
  }).catch(function(e){pl.classList.remove('busy');status((e.message||'Could not find that place')+' - try a nearby town or send it on WhatsApp.',true);});
 };
 render=function(res,a,b){
  if(!last){return render1(res,a,b);}
  if(!last.pts){return render1(res,a,b);}
  var pts=last.pts,legs=[],km=0,lo=0,hi=0;
  for(var i=0;i<pts.length-1;i++){
   var kr=matchRoute(pts[i],pts[i+1]),L=res.legs[i]||{km:0,hrs:0};
   var lk=kr?kr.km:Math.round(L.km),lf=kr?kr.f:factorFor(L.km,L.hrs,pts[i+1]);
   var lt=kr?(kr.t||fmtH(L.hrs,lf)):fmtH(L.hrs,lf);
   legs.push({a:pts[i].name.split(',')[0],b:pts[i+1].name.split(',')[0],km:lk,f:lf,t:lt});
   var nums=kr?(String(kr.t||'').indexOf('hr')>0?String(kr.t).match(/\d+(\.\d+)?/g):null):null;
   if(nums){lo+=+nums[0];hi+=+(nums[1]||nums[0]);}else{lo+=L.hrs*hk(lf);hi+=L.hrs*hk(lf)*1.18;}
   km+=lk;
  }
  var tm=hm(lo)+' – '+hm(hi)+' driving';
  var vid=$('szc-pv').value,v=PV[vid];
  var isRound=$('szc-pm').value==='round';
  var bk=Math.round(res.back?res.back.km:0);
  var kmr=km+bk;
  var need=Math.max(1,Math.ceil((isRound?kmr:km)/250));
  var ud=dy?(parseInt(dy.value,10)||0):0;
  var days=isRound?Math.max(need,Math.min(20,ud)):need;
  var date=$('szc-pd').value||'___',ppl=$('szc-pn').value||'___';
  function amtFor(vv,k){
   if(vv.quote){return null;}
   var base;
   if(isRound){base=r99(Math.max(kmr,250*days)*vv.h)+(days-1)*vv.nt;}
   else{var s=0;legs.forEach(function(l){s+=l.km*vv.ow*l.f;});base=Math.max(vv.m,r99(s));}
   return TIERS[k]===1?base:r99(base*TIERS[k]);
  }
  var path=legs.map(function(l){return l.a;}).concat([legs[legs.length-1].b]);
  var tiersHtml=Object.keys(TIERS).map(function(k){var a2=amtFor(v,k);return '<button type="button" class="szc-ptier'+(k===tier?' on':'')+'" data-tier="'+k+'"><span class="n">'+TNAME[k].split(' (')[0]+'</span><span class="s">'+TNAME[k].split(' (')[1].replace(')','')+'</span><span class="a">'+(a2===null?'On quote':inr(a2))+'</span></button>';}).join('');
  var all=PC.v.filter(function(x){return !x.quote;}).map(function(x){return '<li'+(x.id===vid?' class="on"':'')+'><span>'+x.n+' <small>'+x.seats+' seats</small></span><b>'+inr(amtFor(x,tier))+'</b></li>';}).join('');
  var legHtml=legs.map(function(l,i){return '<li><span class="i">'+(i+1)+'</span><span class="r">'+l.a+' → '+l.b+'</span><span class="d">'+l.km+' km · '+l.t+'</span></li>';}).join('')+(isRound?'<li class="bk"><span class="i">↩</span><span class="r">'+path[path.length-1]+' → '+path[0]+' (return)</span><span class="d">'+bk+' km</span></li>':'');
  var est=amtFor(v,tier);
  var msg='Hi Suzu Travels, I planned a multi-stop trip on your site.\nRoute: '+path.join(' → ')+(isRound?' → '+path[0]+' (round trip)':' (one-way)')+'\nDistance: ~'+(isRound?kmr:km)+' km\nDays: '+days+'\nCar: '+v.n+' - '+TNAME[tier]+'\nEstimate shown: '+(est===null?'on quote':inr(est))+'\nDate: '+date+'\nPeople: '+ppl+'\n(page: '+(PC.s||'cabs')+' planner multi-stop)';
  var note=isRound?'Round trip back to '+path[0]+': '+days+' day'+(days>1?'s':'')+' at the 250 km/day minimum, driver allowance for '+(days-1)+' night'+(days-1===1?'':'s')+' included.':'One-way drop with stops on the way, priced leg by leg. Staying overnight at a stop? Switch to Round trip or tell us the nights on WhatsApp - it becomes a tour fare.';
  out.innerHTML='<div class="szc-pres"><div class="szc-pfacts"><div><span class="k">Total distance</span><span class="v">'+(isRound?kmr:km)+' km</span></div><div><span class="k">Drive time</span><span class="v">'+tm+'</span></div><div><span class="k">Days needed</span><span class="v">'+days+' day'+(days>1?'s':'')+'</span></div><div><span class="k">Stops</span><span class="v">'+(pts.length-2)+' on the way</span></div></div>'
   +'<ol class="szc-plegs">'+legHtml+'</ol>'
   +'<p class="szc-plbl">Choose your fleet - same trip, three price points</p><div class="szc-ptiers">'+tiersHtml+'</div>'
   +'<details class="szc-pall"><summary>Compare all cars at '+TNAME[tier].split(' (')[0]+' rates</summary><ul>'+all+'</ul></details>'
   +'<p class="szc-pnote">'+note+' Fuel and driver included. Tolls, parking and state entry tax extra at actuals. Indicative - your WhatsApp quote is the final price.</p>'
   +'<div class="szc-btns"><a class="szc-btn gold" target="_blank" rel="noopener" href="'+wa(msg)+'">Lock this trip on WhatsApp</a><a class="szc-btn line" href="#enquiry">Request a call back</a><button type="button" class="szc-btn line" id="szc-replay">Replay route</button></div></div>';
  qa('.szc-ptier',out).forEach(function(b2){b2.addEventListener('click',function(){setTier(b2.getAttribute('data-tier'));});});
  var rp=$('szc-replay');if(rp){rp.addEventListener('click',function(){if(last){play(last.res);}});}
 };
 hubAddVia=addVia;
 relabel();
}}

/* Share / save the plan (ENHANCEMENTS #5, 26 Oct 2026): a link with from, to, via, car, trip, days, tier, date and ppl query values plus #planner
   re-runs the planner on load. Nothing is stored; the link lives only in the visitor's own share sheet or clipboard. */
var shRe=/^\d{4}-\d{2}-\d{2}$/;
function shClean(x){return String(x||'').replace(/[<>"]/g,'').trim().slice(0,60);}
function shLink(){
 var q=[],dy2=$('szc-pdy');
 function add(k,v){if(v){q.push(k+'='+encodeURIComponent(v));}}
 add('from',shClean($('szc-fa').value));
 var vs=qa('input.szc-vin').map(function(i){return shClean(i.value);}).filter(function(x){return x.length>0;});
 if(vs.length){add('via',vs.join('|'));}
 add('to',shClean($('szc-fb').value));
 add('car',$('szc-pv').value);
 add('trip',$('szc-pm').value);
 if(dy2){if($('szc-pm').value==='round'){add('days',dy2.value);}}
 add('tier',tier);
 add('date',$('szc-pd').value);
 add('ppl',$('szc-pn').value);
 return location.origin+location.pathname+'?'+q.join(AMP)+'#planner';
}
function shText(){
 var f=out.querySelector('.szc-pfacts'),km='';
 if(f){var v1=f.querySelector('.v');if(v1){km=v1.textContent;}}
 var on=out.querySelector('.szc-ptier.on .a'),amt=on?on.textContent:'';
 var vs=qa('input.szc-vin').map(function(i){return shClean(i.value);}).filter(function(x){return x.length>0;});
 var path=[shClean($('szc-fa').value)].concat(vs,[shClean($('szc-fb').value)]).join(' → ');
 return 'Our road trip plan: '+path+(km?', '+km:'')+(amt?', '+PV[$('szc-pv').value].n+' '+amt+' ('+TNAME[tier].split(' (')[0]+')':'')+' - see the route on the map:';
}
function shDone(b,t){var o=b.textContent;b.textContent=t;b.classList.add('ok');setTimeout(function(){b.textContent=o;b.classList.remove('ok');},2200);}
function shCopy(b,url){
 function fb(){window.prompt('Copy this link',url);}
 if(navigator.clipboard){if(navigator.clipboard.writeText){navigator.clipboard.writeText(url).then(function(){shDone(b,'Link copied ✓');},fb);return;}}
 fb();
}
function shAdd(){
 var row=out.querySelector('.szc-btns');if(!row){return;}
 if(row.querySelector('.szc-pshare')){return;}
 var b=document.createElement('button');b.type='button';b.className='szc-btn line szc-pshare';b.textContent='Share this plan';
 b.setAttribute('aria-label','Share or copy a link to this route plan');
 b.addEventListener('click',function(){
  var url=shLink();
  if(navigator.share){navigator.share({title:'Road trip plan - Suzu Travels',text:shText(),url:url}).catch(function(){});return;}
  shCopy(b,url);
 });
 row.appendChild(b);
}
var render2=render;
render=function(res,a,b){render2(res,a,b);shAdd();};
/* Hill-season note (ENHANCEMENTS #7, 28 Oct 2026): month + places of the plan -> honest season/permit notes from the kit's road tips. Data only, no live road status. */
var SNS=[
 [32.75,36,75.75,80,'111110000111','Ladakh roads are seasonal','Snow shuts the Manali–Leh highway in winter; it usually runs from late May or June to mid-October, and Zojila (Srinagar–Leh) from about mid-April. Off season, fly to Leh; we book the Leh taxi.',1],
 [32.75,36,75.75,80,'000001111000','Altitude comes first','Most of the drive is above 4,000 m. Halt a night in Manali or Kargil, carry cash and warm layers, and keep a spare day before your flight out of Leh.',0],
 [31.8,32.5,77.6,79,'111111000111','Spiti via Kunzum','Snow shuts Kunzum Pass (Manali–Kaza) from about mid-October until it reopens in summer. We check the road report before we quote.',1],
 [32.4,32.75,76.75,77.6,'111000000001','Lahaul in snow','After fresh snow the road beyond the Atal Tunnel can close for a day or two. We confirm the day before.',1],
 [32.15,32.4,77,77.35,'111111111111','Rohtang permit','Rohtang needs an online permit, is closed on Tuesdays and is usually open about May to November. Local sightseeing runs in Manali union taxis; we book them.',0],
 [30.55,31.1,78.15,79.6,'000011111000','Yatra rules','Every pilgrim must register, and yatra hill roads are closed to cars from 8 pm to 5 am, so days start at 5–6 am.',0],
 [30.55,31.1,78.15,79.6,'111100000111','Char Dham winter closing','The dhams close for winter in November, after Diwali, and reopen on Akshaya Tritiya in late April or May.',1],
 [33.2,35,73.5,75.75,'110000000001','Kashmir in snow','Heavy snow can close the Jammu–Srinagar highway for a day or more. Drivers carry chains; we check the advisory the evening before.',1]
];
var SNG=[
 ['110000000001','Snow months','From mid-December to February hill roads can close for a day or two after fresh snow. Drivers carry chains; we confirm the day before.',1],
 ['000000110000','Monsoon caution','Mid-July to August brings landslides on hill highways. We watch advisories and shift your start time or route at no extra charge.',0],
 ['111111111111','No night driving in the hills','Our drivers do not run hill sections late at night. Leave early and reach before dark.',2]
];
function snHill(p){
 var X=[74.5,75.8,77,78.1,79.5,81],Y=[32.9,32.4,30.95,30.2,29.33,28.8];
 if(p.lon<73.5){return false;}if(p.lon>81.5){return false;}
 var x=Math.max(74.5,Math.min(81,p.lon)),i=1;
 while(i<5){if(x<=X[i]){break;}i++;}
 return p.lat>Y[i-1]+(Y[i]-Y[i-1])*(x-X[i-1])/(X[i]-X[i-1]);
}
function snAdd(){
 if(!last){return;}
 var at=out.querySelector('.szc-pnote');if(!at){return;}
 var P=last.pts||[last.a,last.b],dv=$('szc-pd').value||'',m=parseInt(dv.slice(5,7),10),own=m>0;
 if(!own){m=new Date().getMonth()+1;}
 var N=[],snow=0,hill=P.some(snHill);
 SNS.forEach(function(r){
  if(r[4].charAt(m-1)==='1'){if(P.some(function(p){return p.lat>=r[0]?(p.lat<=r[1]?(p.lon>=r[2]?p.lon<=r[3]:false):false):false;})){N.push(r.slice(5));if(r[7]){snow=1;}}}
 });
 if(hill){SNG.forEach(function(g){if(g[0].charAt(m-1)==='1'){if(g[3]===1){if(!snow){N.push(g.slice(1));}}else{if(g[3]===2){if(!N.length){N.push(g.slice(1));}}else{N.push(g.slice(1));}}}});}
 if(!N.length){return;}
 var mn=new Date(2026,m-1,1).toLocaleString('en-IN',{month:'long'});
 var rt=P.map(function(p){return p.name.split(',')[0];}).join(' → ');
 var msg='Hi Suzu Travels, how are the roads for '+rt+' in '+mn+(own?' ('+dv+')':'')+'?\n(page: cabs planner season)';
 var d=document.createElement('div');d.className='szc-psea';d.setAttribute('role','note');
 d.innerHTML='<span class="szc-psh">Season check · '+mn+(own?'':' (this month)')+'</span>'+N.slice(0,2).map(function(n){return '<p class="szc-psn"><b>'+n[0]+'.</b> '+n[1]+'</p>';}).join('')+'<a class="szc-psa" target="_blank" rel="noopener" href="'+wa(msg)+'">Ask us about the road on WhatsApp →</a>';
 at.parentNode.insertBefore(d,at);
}
var render3=render;
render=function(res,a,b){render3(res,a,b);snAdd();};
var pdEl=$('szc-pd');if(pdEl){pdEl.addEventListener('change',function(){if(last){render(last.res,last.a,last.b);}});}
(function(){
 var s=location.search;if(!s){return;}if(s.length<2){return;}
 var Q={};
 s.slice(1).split(AMP).forEach(function(kv){var i=kv.indexOf('=');if(i>0){try{Q[kv.slice(0,i)]=decodeURIComponent(kv.slice(i+1).replace(/\+/g,' '));}catch(e){}}});
 var A=shClean(Q.from),B=shClean(Q.to);
 if(!A){return;}if(!B){return;}
 $('szc-fa').value=A;$('szc-fb').value=B;
 if(PV[Q.car]){$('szc-pv').value=Q.car;}
 if(Q.trip==='round'){$('szc-pm').value='round';}else{if(Q.trip==='one'){$('szc-pm').value='one';}}
 try{$('szc-pm').dispatchEvent(new Event('change'));}catch(e){}
 var d2=parseInt(Q.days,10),dy3=$('szc-pdy');if(dy3){if(d2>0){if(d2<21){dy3.value=d2+'';}}}
 if(shRe.test(Q.date||'')){$('szc-pd').value=Q.date;}
 var n2=parseInt(Q.ppl,10);if(n2>0){if(n2<46){$('szc-pn').value=n2+'';}}
 if(Q.via){if(hubAddVia){Q.via.split('|').slice(0,3).forEach(function(v){v=shClean(v);if(v){hubAddVia(v);}});}}
 PC.s='cabs shared';
 if(TIERS[Q.tier]){if(Q.tier!==tier){setTier(Q.tier);}}
 run();
})();
/* Which car do I need? (ENHANCEMENTS #8, 29 Oct 2026): people + big bags + road + priority (+ seniors/kids) -> class + tier.
   Uses the fleet gallery data (FL/FB from the fleet block). Fares = same engine as the viewer. Ends in WhatsApp '(page: cabs car helper)'. */
var hb=$('szc-help'),ho=$('szc-hout');
if(hb){if(ho){if(FB){
 var HL={saver:['hatch','sedan','ertiga','crysta','tempo','tempo17','minibus','bus35','bus45'],standard:['sedan','carens','crysta','tempo','tempo17','minibus','bus35','bus45'],prime:['hycross','urbania','minibus','bus45']};
 var HH={saver:['crysta','tempo','tempo17'],standard:['crysta','tempo','tempo17'],prime:['fortuner','crysta','tempo17']};
 var RDN={plain:'plains / city roads',hill:'hill roads',high:'high passes'};
 function hcap(v){var n=parseInt(v.bags,10);return isNaN(n)?99:n;}
 function hnum(id,lo,hi,dv){var n=parseInt($(id).value,10);if(isNaN(n)){n=dv;}if(n < lo){n=lo;}if(n > hi){n=hi;}return n;}
 function hfare(v,k){if(v.quote){return null;}var r=FL.ref;var base=Math.max(v.min,r99(r.km*v.ow*r.f));return {ow:TIERS[k]===1?base:r99(base*TIERS[k]),km:Math.round(v.hire*TIERS[k])};}
 function hpick(n,bg,rd,k,sn){
  var L=(rd==='high'?HH[k]:HL[k]).slice();
  L=L.filter(function(id){
   if(rd!=='plain'){if(id==='hatch'){return false;}}
   if(sn){if(id==='hatch'){return false;}if(id==='ertiga'){return false;}if(id==='carens'){return false;}if(id==='sedan'){if(n > 3){return false;}}}
   return true;
  });
  var fit=L.filter(function(id){var v=FB[id];return v.seats >= n ? hcap(v) >= bg : false;});
  if(fit.length){return fit;}
  if(rd==='high'){return [];}
  return FL.v.filter(function(v){return v.seats >= n ? hcap(v) >= bg : false;}).map(function(v){return v.id;});
 }
 function hcard(v,k,main){
  var f=hfare(v,k);
  var price=f?'\x3cdiv class="szc-hpr">\x3cspan>\x3cb>'+inr(f.ow)+'\x3c/b>'+FL.ref.l+' one-way\x3c/span>\x3cspan>\x3cb>₹'+f.km+'/km\x3c/b>round trip\x3c/span>\x3c/div>':'\x3cdiv class="szc-hpr">\x3cspan>\x3cb>On quote\x3c/b>per trip, all-in\x3c/span>\x3c/div>';
  var img=v.photo?'\x3cimg src="'+v.photo+'" alt="'+v.alt+'" width="1280" height="853" loading="lazy" decoding="async">':'';
  return '\x3cdiv class="szc-hcar'+(main?' main':'')+'">\x3cdiv class="szc-himg">'+img+'\x3c/div>\x3cdiv class="szc-hinfo">\x3cspan class="szc-tag">'+(main?'Our pick':'Also fits')+' · '+TNAME[k].split(' (')[0]+' fleet\x3c/span>\x3ch4>'+v.name+'\x3c/h4>\x3cp class="szc-hfit">'+v.seats+' seats · '+v.bags+' · AC · '+v.fuel+'\x3c/p>'+price+'\x3cbutton type="button" class="szc-hlink" data-hview="'+v.id+'">View photos and specs\x3c/button>\x3c/div>\x3c/div>';
 }
 var hLast='';
 function hpaint(){
  var n=hnum('szc-hp',1,45,4),bg=hnum('szc-hg',0,40,2),rd=$('szc-hr').value,k=$('szc-hy').value,sn=$('szc-hs').checked;
  if(!TIERS[k]){k='standard';}
  var hk=[n,bg,rd,k,sn,tier].join('|');if(hk===hLast){return;}hLast=hk;
  var ids=hpick(n,bg,rd,k,sn);
  var who=n+(n===1?' person':' people')+', '+bg+(bg===1?' big bag':' big bags')+', '+RDN[rd]+(sn?', seniors/kids':'');
  if(!ids.length){
   ho.innerHTML='\x3cdiv class="szc-hnone">\x3cb>No single vehicle fits '+who+'.\x3c/b> We split the group into two cars or a Tempo Traveller plus a car - tell us the plan and we send one all-in quote.\x3c/div>\x3cdiv class="szc-btns">\x3ca class="szc-btn wa" target="_blank" rel="noopener" href="'+wa('Hi Suzu Travels, which cars do we need? We are '+who+'. Date: ___ , route: ___ (page: cabs car helper)')+'">Ask on WhatsApp\x3c/a>\x3ca class="szc-btn line" href="#enquiry">Request a call back\x3c/a>\x3c/div>';
   return;
  }
  var v=FB[ids[0]],alt=ids.length > 1 ? FB[ids[1]] : null;
  var why=['Fits '+who+': '+v.seats+' seats, '+v.bags+'.','Best for: '+v.best+'.',TNAME[k]+' - '+(k==='prime'?'newest cars, about 15% above Standard.':(k==='saver'?'older, well-kept cars, about 8% below Standard.':'the fares shown on our route pages.'))];
  if(rd==='high'){why.push('For high passes we suggest only our diesel SUVs and Tempo Travellers.');}
  var msg='Hi Suzu Travels, which car fits us? We are '+who+'. Your helper suggests '+v.name+', '+TNAME[k].split(' (')[0]+' fleet. Date: ___ , route: ___ (page: cabs car helper)';
  ho.innerHTML='\x3cdiv class="szc-hres">'+hcard(v,k,true)+(alt?hcard(alt,k,false):'')+'\x3c/div>\x3cul class="szc-hwhy">'+why.map(function(t){return '\x3cli>'+t+'\x3c/li>';}).join('')+'\x3c/ul>\x3cdiv class="szc-btns">\x3ca class="szc-btn wa" target="_blank" rel="noopener" href="'+wa(msg)+'">Get this car quoted on WhatsApp\x3c/a>\x3cbutton type="button" class="szc-btn line" data-hplan="'+v.id+'">Price my route in the planner\x3c/button>'+(k!==tier?'\x3cbutton type="button" class="szc-btn line" data-htier="'+k+'">Show all prices in '+TNAME[k].split(' (')[0]+'\x3c/button>':'')+'\x3c/div>\x3cp class="szc-hnote">Cars shown are representative of each class. Final car and fare are confirmed on the WhatsApp quote.\x3c/p>';
  qa('[data-hview]',ho).forEach(function(b){b.addEventListener('click',function(){var t=g.querySelector('[data-view="'+b.getAttribute('data-hview')+'"]');if(t){t.click();}});});
  qa('[data-hplan]',ho).forEach(function(b){b.addEventListener('click',function(){var s=$('szc-pv');if(s){s.value=b.getAttribute('data-hplan');}var pn=$('szc-pn');if(pn){pn.value=n+'';}var ps=$('planner');if(ps){ps.scrollIntoView({behavior:'smooth'});}var fb=$('szc-fb');if(fb){setTimeout(function(){try{fb.focus({preventScroll:true});}catch(e){}},600);}});});
  qa('[data-htier]',ho).forEach(function(b){b.addEventListener('click',function(){setTier(b.getAttribute('data-htier'));hpaint();});});
 }
 if(TIERS[tier]){$('szc-hy').value=tier;}
 ['szc-hp','szc-hg','szc-hr','szc-hy','szc-hs'].forEach(function(id){var el=$(id);el.addEventListener('input',hpaint);el.addEventListener('change',hpaint);});
 hpaint();
}}
/* Seat + luggage layout in the car viewer (ENHANCEMENTS #9, 30 Oct 2026): original SVGs from seatmap_svg.py on jsDelivr; added after kit.js fills the viewer. */
var SMB='__SEATMAP_BASE__';
var SMX=M?M.querySelector('.szc-mbody'):null;
if(SMX){
 new MutationObserver(function(){
  var t=SMX.querySelector('#szc-mt');if(!t){return;}
  if(SMX.querySelector('.szc-seat')){return;}
  var v=null;Object.keys(FB).forEach(function(k){if(FB[k].name===t.textContent){v=FB[k];}});
  if(!v){return;}
  var f=document.createElement('figure');f.className='szc-seat';
  f.innerHTML='\x3cimg src="'+SMB+v.id+'.svg" alt="Top view seat and luggage layout of a '+v.name+'" decoding="async">\x3cfigcaption>Seats and bags: '+v.seats+' passengers + driver, '+v.bags+'. Typical layout for the class - the exact car can differ.\x3c/figcaption>';
  var b=SMX.querySelector('.szc-mbest');if(b){b.parentNode.insertBefore(f,b.nextSibling);}
 }).observe(SMX,{childList:true});
}
}
