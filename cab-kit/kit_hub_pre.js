/* kit_hub_pre.js - hub only, a small separate script placed right BEFORE the minified kit script (build.py finish), so the
   kit script stays byte-identical (terser re-mangles every name on any kit change = a 40 KB republish).
   Same rules as kit.js: ES5, no ampersand character, no double-slash comments, HTML only in single-quoted strings.
   1) Hub size trim (ENHANCEMENTS #16, 8 Nov 2026): hub.py leaves out r.u when it is the usual /cabs/<a>-to-<b>-taxi/ page -
      put it back into data-plan before the kit parses it (same rule: lower case, spaces to '-').
   2) Call-back time slot (ENHANCEMENTS #16, 8 Nov 2026): Morning / Afternoon / Evening buttons in the hub quote form; the pick
      rides in the WhatsApp page tag, e.g. '(page: cabs - call back: Evening, 4-9 pm)' - kit.js send() reads data-slug at send
      time. Nothing is stored. The site-wide #enquiry popup belongs to another lane and is left as it is.
   3) Hub size headroom (ENHANCEMENTS #20, 10 Nov 2026): build.py hub_trim() drops values the page already shows - put them back
      before the kit parses: data-fleet alt / model / best from the gallery card (img alt, .szc-tag, the p that starts 'Best for: ' - wpautop
      leaves an empty p before it on the live page; the
      browser decodes entities in both places, so the values come back identical), night 400 (the default); data-plan-route on route-card Map links (card From / To) and
      on the planner chips (chip text 'A - B' with the arrow). quote:false / page:'' need no restore (the kit only tests them).
   4) Hub size budget (ENHANCEMENTS #22, 12 Nov 2026): the calculator's data-cfg v / d are left out when they equal data-plan v
      (minus seats and on-quote buses) / data-plan r as {l:'A → B', km, f} - rebuilt here after the r.u restore, same keys and order. */
(function(){
var d=document,P=d.getElementById('szc-plan'),F=d.getElementById('szc-qf');
if(P){try{var c=JSON.parse(P.getAttribute('data-plan'));c.r.forEach(function(r){if(!('u' in r)){r.u='/cabs/'+(r.a+'-to-'+r.b).toLowerCase().split(' ').join('-')+'-taxi/';}});P.setAttribute('data-plan',JSON.stringify(c));var Q=d.querySelector('[data-cfg]'),o,g;if(Q){o=JSON.parse(Q.getAttribute('data-cfg'));if(!('v' in o)){g={v:c.v.filter(function(v){return !v.quote;}).map(function(v){var x={},k;for(k in v){if(k!=='seats'){x[k]=v[k];}}return x;}),d:c.r.map(function(r){return {l:r.a+' → '+r.b,km:r.km,f:r.f};})};for(var k in o){g[k]=o[k];}Q.setAttribute('data-cfg',JSON.stringify(g));}}}catch(e){}}
var T=function(e){return e?e.textContent:'';};
var W=d.getElementById('szc-fleet');
if(W){try{var L=JSON.parse(W.getAttribute('data-fleet'));(L.v||[]).forEach(function(v){var b=d.querySelector('.szc-veh [data-view="'+v.id+'"]'),a=b?b.closest('.szc-veh'):null,im,ps,pi;if(!('night' in v)){v.night=400;}if(a){im=a.querySelector('img');if(!('alt' in v)){v.alt=im?im.getAttribute('alt'):v.name;}if(!('model' in v)){v.model=T(a.querySelector('.szc-tag'));}if(!('best' in v)){v.best='';ps=a.querySelectorAll('.szc-card-b p');for(pi=0;pi < ps.length;pi++){if(T(ps[pi]).indexOf('Best for: ')===0){v.best=T(ps[pi]).slice(10);}}}}});W.setAttribute('data-fleet',JSON.stringify(L));}catch(e){}}
var M=d.querySelectorAll('.szc-route-card a[href="#planner"]:not([data-plan-route])'),k,q;
for(k=0;k < M.length;k++){q=M[k].closest('.szc-route-card');if(q){M[k].setAttribute('data-plan-route',T(q.querySelector('.from'))+'>'+T(q.querySelector('.to')).replace(/^→\s*/,''));}}
M=d.querySelectorAll('.szc-pchips button:not([data-plan-route])');
for(k=0;k < M.length;k++){q=T(M[k]).split(' → ');if(q.length===2){M[k].setAttribute('data-plan-route',q[0]+'>'+q[1]);}}
if(F){
var G=F.getAttribute('data-slug'),D=d.createElement('div');
D.className='full szc-slot';
D.innerHTML='<label>Best time to call you back</label><div role="group" aria-label="Call-back time">'+['Morning|9 am–12 pm','Afternoon|12–4 pm','Evening|4–9 pm'].map(function(x){x=x.split('|');return '<button type="button" aria-pressed="false" data-s="'+x[0]+', '+x[1]+'">'+x[0]+'<small>'+x[1]+'</small></button>';}).join('')+'</div>';
F.insertBefore(D,F.querySelector('.szc-btns'));
var B=D.querySelectorAll('button');
for(var i=0;i < B.length;i++){B[i].addEventListener('click',function(){var b=this,on=b.getAttribute('aria-pressed')!=='true';for(var j=0;j < B.length;j++){B[j].setAttribute('aria-pressed','false');}if(on){b.setAttribute('aria-pressed','true');}F.setAttribute('data-slug',on?G+' - call back: '+b.getAttribute('data-s'):G);});}
}
})();
