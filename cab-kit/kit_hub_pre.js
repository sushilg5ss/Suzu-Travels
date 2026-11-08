/* kit_hub_pre.js - hub only, a small separate script placed right BEFORE the minified kit script (build.py finish), so the
   kit script stays byte-identical (terser re-mangles every name on any kit change = a 40 KB republish).
   Same rules as kit.js: ES5, no ampersand character, no double-slash comments, HTML only in single-quoted strings.
   1) Hub size trim (ENHANCEMENTS #16, 8 Nov 2026): hub.py leaves out r.u when it is the usual /cabs/<a>-to-<b>-taxi/ page -
      put it back into data-plan before the kit parses it (same rule: lower case, spaces to '-').
   2) Call-back time slot (ENHANCEMENTS #16, 8 Nov 2026): Morning / Afternoon / Evening buttons in the hub quote form; the pick
      rides in the WhatsApp page tag, e.g. '(page: cabs - call back: Evening, 4-9 pm)' - kit.js send() reads data-slug at send
      time. Nothing is stored. The site-wide #enquiry popup belongs to another lane and is left as it is. */
(function(){
var d=document,P=d.getElementById('szc-plan'),F=d.getElementById('szc-qf');
if(P){try{var c=JSON.parse(P.getAttribute('data-plan'));c.r.forEach(function(r){if(!('u' in r)){r.u='/cabs/'+(r.a+'-to-'+r.b).toLowerCase().split(' ').join('-')+'-taxi/';}});P.setAttribute('data-plan',JSON.stringify(c));}catch(e){}}
if(F){
var G=F.getAttribute('data-slug'),D=d.createElement('div');
D.className='full szc-slot';
D.innerHTML='<label>Best time to call you back</label><div role="group" aria-label="Call-back time">'+['Morning|9 am–12 pm','Afternoon|12–4 pm','Evening|4–9 pm'].map(function(x){x=x.split('|');return '<button type="button" aria-pressed="false" data-s="'+x[0]+', '+x[1]+'">'+x[0]+'<small>'+x[1]+'</small></button>';}).join('')+'</div>';
F.insertBefore(D,F.querySelector('.szc-btns'));
var B=D.querySelectorAll('button');
for(var i=0;i < B.length;i++){B[i].addEventListener('click',function(){var b=this,on=b.getAttribute('aria-pressed')!=='true';for(var j=0;j < B.length;j++){B[j].setAttribute('aria-pressed','false');}if(on){b.setAttribute('aria-pressed','true');}F.setAttribute('data-slug',on?G+' - call back: '+b.getAttribute('data-s'):G);});}
}
})();
