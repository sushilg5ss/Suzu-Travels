/* Suzu Cab Kit - compare 2-3 cars side by side (ENHANCEMENTS #11, 1 Nov 2026). Hub only, lazy-loaded from jsDelivr on the
   first "Compare" tick (kit_hub.js exposes window.szcK). Same ES5 rules as kit.js: no ampersand, no line comments.
   Fares = the viewer formula (engine one-way for FL.ref x tier, hire x tier). Every path ends in WhatsApp or #enquiry. Nothing stored. */
(function(){
var K=window.szcK;
if(!K){return;}
if(window.szcCmp){return;}
var T=K.T,FL=K.FL,FB=K.FB,M=K.M;
var css='.szc .szc-cmpbar{position:fixed;left:50%;bottom:14px;transform:translateX(-50%);z-index:9990;display:flex;align-items:center;gap:10px;flex-wrap:wrap;justify-content:center;background:#122615;color:#fff;border:1px solid rgba(212,175,55,.55);border-radius:18px;padding:10px 12px;box-shadow:0 18px 44px rgba(0,0,0,.35);max-width:calc(100vw - 24px);box-sizing:border-box;font-family:"Plus Jakarta Sans",Inter,system-ui,sans-serif}'+
'.szc .szc-cmpbar[hidden]{display:none}'+
'.szc .szc-cmpch{display:flex;gap:6px;flex-wrap:wrap;justify-content:center}'+
'.szc .szc-cmpc{display:inline-flex;align-items:center;gap:6px;background:rgba(255,255,255,.1);border-radius:999px;padding:4px 6px 4px 4px;font-size:13px;font-weight:700;color:#fff}'+
'.szc .szc-cmpc img{width:34px;height:23px;border-radius:999px;object-fit:cover;display:block}'+
'.szc .szc-cmpc button{background:none;border:0;color:#f1d98a;font-size:16px;line-height:1;cursor:pointer;padding:0 2px}'+
'.szc .szc-cmphint{font-size:12px;color:#cfe0d2}'+
'.szc .szc-cmpbar .szc-btn{padding:9px 16px;font-size:14px;width:auto}'+
'.szc .szc-cmpbar .szc-btn[disabled]{opacity:.5;cursor:default;transform:none}'+
'.szc .szc-cmpx{background:none;border:0;color:#cfe0d2;font-weight:700;font-size:13px;cursor:pointer;text-decoration:underline}'+
'.szc .szc-cmpb.on{background:#122615;color:#fff!important;border-color:#122615}'+
'.szc-modal .szc-cmpm{grid-column:1/-1;padding:24px 22px 20px}'+
'.szc-modal .szc-cmpm h3{font-size:24px;margin:2px 0 4px;color:#122615;font-weight:800;padding-right:44px}'+
'.szc-modal .szc-cmpsub{color:#56675b;font-size:14px;margin:0 0 12px}'+
'.szc-modal .szc-cmpt{display:flex;gap:6px;flex-wrap:wrap;margin:0 0 12px}'+
'.szc-modal .szc-cmpt button{border:1.5px solid #122615;background:#fff;color:#122615;border-radius:999px;padding:6px 12px;font-weight:700;font-size:13px;cursor:pointer;font-family:inherit}'+
'.szc-modal .szc-cmpt button.on{background:#122615;color:#fff}'+
'.szc-modal .szc-cmpw{overflow-x:auto;-webkit-overflow-scrolling:touch}'+
'.szc-modal .szc-cmptb{width:100%;border-collapse:collapse;font-size:14px;table-layout:fixed;min-width:300px}'+
'.szc-modal .szc-cmptb th,.szc-modal .szc-cmptb td{padding:8px 6px;border-bottom:1px solid #e2e6df;vertical-align:top;text-align:left;word-wrap:break-word}'+
'.szc-modal .szc-cmptb tbody th{font-size:11px;letter-spacing:.05em;text-transform:uppercase;color:#56675b;font-weight:800;width:24%}'+
'.szc-modal .szc-cmptb thead td{font-weight:800;color:#122615;font-size:14px}'+
'.szc-modal .szc-cmptb thead img{width:100%;aspect-ratio:3/2;object-fit:cover;border-radius:10px;display:block;margin-bottom:6px;background:#eef1ec}'+
'.szc-modal .szc-cmptb .num{font-weight:800;color:#122615;white-space:nowrap}'+
'.szc-modal .szc-cmpbest{display:inline-block;background:#d4af37;color:#122615;font-size:10px;font-weight:800;border-radius:999px;padding:2px 7px;margin-top:3px;letter-spacing:.04em;text-transform:uppercase}'+
'.szc-modal .szc-cmptb a.szc-btn{padding:8px 10px;font-size:13px;width:100%;box-sizing:border-box}'+
'.szc-modal .szc-cmpm .szc-btns{margin-top:14px}'+
'.szc-modal .szc-cmpnote{font-size:12px;color:#56675b;margin:10px 0 0}'+
'@media (max-width:600px){.szc-modal .szc-cmpm{padding:20px 12px 16px}.szc-modal .szc-cmptb{font-size:13px}.szc-modal .szc-cmptb tbody th{width:26%;font-size:10px}.szc .szc-cmpc span{max-width:96px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}}';
var st=document.createElement('style');st.textContent=css;document.head.appendChild(st);
var bar=document.createElement('div');bar.className='szc-cmpbar';bar.hidden=true;bar.setAttribute('role','region');bar.setAttribute('aria-label','Compare cars');
K.g.appendChild(bar);
function esc(s){return String(s).replace(/[<>"]/g,'');}
function fare(v,k){
 if(v.quote){return null;}
 var r=FL.ref;var base=Math.max(v.min,K.r99(r.km*v.ow*r.f));
 return {ow:T[k]===1?base:K.r99(base*T[k]),km:Math.round(v.hire*T[k])};
}
function tname(k){return K.TN[k].split(' (')[0];}
function sync(){
 K.qa('.szc-cmpb',K.g).forEach(function(b){var on=K.C.indexOf(b.getAttribute('data-cmp')) > -1;b.classList.toggle('on',on);b.setAttribute('aria-pressed',on?'true':'false');b.textContent=on?'✓ Comparing':'+ Compare';});
}
function paint(){
 var C=K.C;sync();
 if(!C.length){bar.hidden=true;return;}
 bar.hidden=false;
 var ch=C.map(function(id){var v=FB[id];return '<span class="szc-cmpc">'+(v.photo?'<img src="'+v.photo.replace(/\.webp$/,'-800.webp')+'" alt="" width="34" height="23" loading="lazy">':'')+'<span>'+esc(v.name)+'</span><button type="button" data-cmprm="'+id+'" aria-label="Remove '+esc(v.name)+'">×</button></span>';}).join('');
 bar.innerHTML='<div class="szc-cmpch">'+ch+'</div>'+(C.length < 2?'<span class="szc-cmphint">Tick one more car to compare (max 3)</span>':'')+'<button type="button" class="szc-btn gold szc-cmpgo"'+(C.length < 2?' disabled':'')+'>Compare '+C.length+' cars</button><button type="button" class="szc-cmpx">Clear</button>';
}
function photo(v){return v.photo?v.photo.replace(/\.webp$/,'-800.webp'):'';}
function open(){
 var C=K.C;if(C.length < 2){return;}if(!M){return;}
 var k=K.tier(),r=FL.ref;
 var vs=C.map(function(id){return FB[id];});
 var fs=vs.map(function(v){return fare(v,k);});
 var low=null,room=0;
 fs.forEach(function(f){if(f){if(low===null){low=f.ow;}if(f.ow < low){low=f.ow;}}});
 vs.forEach(function(v){if(v.seats > room){room=v.seats;}});
 var head='<tr><th></th>'+vs.map(function(v){var p=photo(v);return '<td>'+(p?'<img src="'+p+'" alt="'+esc(v.alt)+'" width="800" height="533" loading="lazy">':'')+esc(v.name)+'</td>';}).join('')+'</tr>';
 function row(lbl,cells){return '<tr><th scope="row">'+lbl+'</th>'+cells.map(function(c){return '<td>'+c+'</td>';}).join('')+'</tr>';}
 var rows='';
 rows+=row('Model',vs.map(function(v){return esc(v.model);}));
 rows+=row('Seats',vs.map(function(v){return '<span class="num">'+v.seats+'</span>'+(v.seats===room?(vs.length > 1?'<br><span class="szc-cmpbest">Most room</span>':''):'');}));
 rows+=row('Bags',vs.map(function(v){return esc(v.bags);}));
 rows+=row('AC / fuel',vs.map(function(v){return 'AC · '+esc(v.fuel);}));
 rows+=row('Best for',vs.map(function(v){return esc(v.best);}));
 rows+=row(esc(r.l)+' one-way',fs.map(function(f){if(!f){return '<b>On quote</b>';}return 'from <span class="num">'+K.inr(f.ow)+'</span>'+(f.ow===low?'<br><span class="szc-cmpbest">Lowest</span>':'');}));
 rows+=row('Round trip / tour',fs.map(function(f){return f?'<span class="num">₹'+f.km+'/km</span><br><small>min 250 km/day</small>':'<b>On quote</b>';}));
 rows+=row('Driver night',vs.map(function(v){return v.quote?'Included in quote':'₹'+v.night+'/night';}));
 rows+=row('Quote',vs.map(function(v){return '<a class="szc-btn wa" target="_blank" rel="noopener" href="'+K.wa('Hi Suzu Travels, I would like a '+v.name+' ('+K.TN[k]+') for '+FL.ctx+'. Date: ___ , people: ___ (page: cabs compare)')+'">WhatsApp</a>'+(v.page?'<br><a href="'+v.page+'" style="font-size:13px;font-weight:700;color:#2e7d32">Rates page</a>':'');}));
 var tb='<div class="szc-cmpt" role="group" aria-label="Fleet">'+Object.keys(T).map(function(t){return '<button type="button" data-cmpt="'+t+'" class="'+(t===k?'on':'')+'" aria-pressed="'+(t===k?'true':'false')+'">'+tname(t)+'</button>';}).join('')+'</div>';
 var names=vs.map(function(v){return v.name;}).join(' vs ');
 var all=K.wa('Hi Suzu Travels, I am comparing '+names+' ('+K.TN[k]+') for '+FL.ctx+'. Please send the best all-in quote. Date: ___ , people: ___ (page: cabs compare)');
 M.querySelector('.szc-mbody').innerHTML='<div class="szc-cmpm"><h3 id="szc-mt">Compare cars</h3><p class="szc-cmpsub">'+esc(names)+' · '+K.TN[k]+'</p>'+tb+'<div class="szc-cmpw"><table class="szc-cmptb"><thead>'+head+'</thead><tbody>'+rows+'</tbody></table></div><p class="szc-cmpnote">Starting prices for off-season weekdays, '+esc(r.l)+' as the example route. Tolls, parking and state entry tax extra at actuals. Photos are representative of the class - the exact car can differ.</p><div class="szc-btns"><a class="szc-btn wa" target="_blank" rel="noopener" href="'+all+'">Get one quote for all on WhatsApp</a><a class="szc-btn line szc-cmpcb" href="#enquiry">Request a call back</a></div></div>';
 M.hidden=false;document.body.style.overflow='hidden';
 var cl=M.querySelector('.szc-mclose');if(cl){cl.focus();}
}
K.g.addEventListener('click',function(e){
 var t=e.target;if(!t){return;}
 if(t.closest){
  var rm=t.closest('[data-cmprm]');
  if(rm){K.tog(rm.getAttribute('data-cmprm'));return;}
  if(t.closest('.szc-cmpgo')){open();return;}
  if(t.closest('.szc-cmpx')){K.C.length=0;paint();return;}
 }
});
if(M){M.addEventListener('click',function(e){
 var t=e.target;if(!t){return;}if(!t.closest){return;}
 var b=t.closest('[data-cmpt]');
 if(b){K.st(b.getAttribute('data-cmpt'));open();return;}
 if(t.closest('.szc-cmpcb')){M.hidden=true;document.body.style.overflow='';}
});}
window.szcCmp=paint;
paint();
})();
