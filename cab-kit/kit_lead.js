/* 12 Nov 2026 (ENHANCEMENTS #22) enquiry-source counter - every cab page, own small script (kit script stays byte-identical).
   On a WhatsApp / call-back / phone click inside the kit it sends ONE GA4 event szc_lead {src, kind, page} if the site's gtag is there.
   No name, phone, message text or anything typed is ever sent. Rules: ES5, no ampersand, no slash-slash comments, no '<'. Kept short on purpose (hub size budget).
   src: hero, calc, helper, fleet, viewer, compare, form, route-card, fares, faq, planner / chips / route-map / shared (how the planner result was started), else the section id.
   kind: whatsapp, callback, call.  page: last path segment (cabs = hub). */
(function(){
var d=document,L='planner',S={'szc-calc':'calc','szc-help':'helper','szc-fleet':'fleet','szc-qf':'form',routes:'route-card',more:'route-card',fares:'fares',faq:'faq','szc-pout':0,'szc-plan':0,live:0};
if(location.search.indexOf('from=')>-1){L='shared';}
function G(s,k){var g=window.gtag,p=location.pathname.split('/').filter(String);if(typeof g=='function'){try{g('event','szc_lead',{src:s,kind:k,page:p.pop()||'home'});}catch(e){}}}
function W(a){
 var m=a.closest('.szc-modal'),n=a;
 if(m){return m.querySelector('[class^=szc-cmp]')?'compare':'viewer';}
 if(a.closest('.szc-hero')){return 'hero';}
 while(n){if(n.id in S){return S[n.id]||L;}n=n.parentElement;}
 m=a.closest('section[id]');
 return m?m.id:'page';
}
d.addEventListener('click',function(e){
 var t=e.target,a,h,k;
 if(!t.closest){return;}
 if(t.closest('.szc-pchips button')){L='chips';return;}
 if(t.closest('[data-plan-route],.szc-route-card a[href="#planner"]')){L='route-map';return;}
 if(t.closest('#szc-plan [type=submit],#szc-padd')){L='planner';}
 a=t.closest('.szc a,.szc-modal a');
 if(a){h=a.getAttribute('href')||'';k=h.indexOf('wa.me/')>-1?'whatsapp':h.indexOf('#enquiry')?h.indexOf('tel:')?0:'call':'callback';if(k){G(W(a),k);}}
},true);
d.addEventListener('submit',function(e){if(e.target.id=='szc-qf'){G('form','whatsapp');}},true);
})();
