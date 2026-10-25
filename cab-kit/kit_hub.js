/* kit_hub.js - hub-only planner extension: multi-stop trips (ENHANCEMENTS #4, 25 Oct 2026).
   build.py inserts this INSIDE the planner block of kit.js (after the IntersectionObserver line) for the hub only,
   so it can reuse geocode/route/draw/render and re-point run/render. Child pages keep plain kit.js.
   Same rules as kit.js: ES5, no ampersand character, no double-slash comments, HTML only in single-quoted strings. */
var vbox=$('szc-pvias'),vadd=$('szc-padd');
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
 relabel();
}}
