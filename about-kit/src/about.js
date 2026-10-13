(function(){
var R=document.getElementById('szab');if(!R||R.getAttribute('data-js'))return;R.setAttribute('data-js','1');
var io=('IntersectionObserver' in window);
// live Google rating (same feed as the homepage)
try{fetch('/suzu-reviews.json',{cache:'no-cache'}).then(function(r){return r.ok?r.json():null}).then(function(d){if(!d||!d.rating_text)return;
R.querySelectorAll('[data-ab-rating]').forEach(function(e){e.textContent=d.rating_text});
R.querySelectorAll('[data-ab-count]').forEach(function(e){e.textContent='Google rating · '+d.count+' reviews'});
R.querySelectorAll('[data-ab-count2]').forEach(function(e){e.textContent=d.count})}).catch(function(){})}catch(e){}
// crew film: play only while on screen
var v=document.getElementById('abCrewFilm');
if(v&&io){var vo=new IntersectionObserver(function(es){es.forEach(function(x){if(x.isIntersecting&&x.intersectionRatio>.45){v.preload='auto';var p=v.play();if(p&&p.catch)p.catch(function(){})}else if(!v.paused){v.pause()}})},{threshold:[0,.45,.8]});vo.observe(v)}
// count-up of hero numbers
function cu(el){var t=el.textContent.replace(/,/g,'');var n=parseFloat(t);if(isNaN(n)||t.indexOf('.')>-1)return;var s=performance.now(),d=1400;function f(now){var k=Math.min(1,(now-s)/d),e=1-Math.pow(1-k,3),c=Math.round(n*e);el.textContent=c.toLocaleString('en-IN');if(k<1)requestAnimationFrame(f)}requestAnimationFrame(f)}
var nums=R.querySelectorAll('.ab-st b span:not([data-ab-rating])');
if(io){var co=new IntersectionObserver(function(es){es.forEach(function(x){if(x.isIntersecting){cu(x.target);co.unobserve(x.target)}})},{threshold:.6});nums.forEach(function(n){co.observe(n)})}
// chapter nav: highlight the section on screen
var links=R.querySelectorAll('.ab-nav a[href^="#"]'),map={};links.forEach(function(a){map[a.getAttribute('href').slice(1)]=a});
if(io){var so=new IntersectionObserver(function(es){es.forEach(function(x){if(x.isIntersecting){links.forEach(function(a){a.classList.remove('on')});var a=map[x.target.id];if(a){a.classList.add('on');var w=a.parentNode;try{w.scrollTo({left:a.offsetLeft-w.clientWidth/2+a.offsetWidth/2,behavior:'smooth'})}catch(e){}}}})},{rootMargin:'-45% 0px -50% 0px'});Object.keys(map).forEach(function(id){var s=document.getElementById(id);if(s)so.observe(s)})}
// map: hover a city row to light it on the map
R.querySelectorAll('.ab-bars2 li').forEach(function(li){var c=li.getAttribute('data-c'),g=R.querySelector('.ab-map .ct[data-c="'+c+'"]');if(!g)return;
li.addEventListener('mouseenter',function(){li.classList.add('on');g.style.transform='scale(1.25)';g.style.transformOrigin='center';g.style.transformBox='fill-box'});
li.addEventListener('mouseleave',function(){li.classList.remove('on');g.style.transform=''})});
var tr=R.querySelector('.ab-track');if(tr)tr.setAttribute('tabindex','0');
})();
