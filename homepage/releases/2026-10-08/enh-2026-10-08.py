#!/usr/bin/env python3
"""Homepage Enhancement Agent, 8 Oct 2026 (nz layer only).
Usage: python3 enh-2026-10-08.py live.html after.html
1. Compare up to 3 trips side by side (card toggle -> floating tray -> table in #nz-sheet).
2. Static "Explore more" internal-link cluster #nz-explore after #tour-packages
   (60 sitemap URLs, all 200 + self-canonical + indexable on 8 Oct), synced to the region tabs.
"""
import sys, html as H
G=[
("himachal","Himachal","हिमाचल","var(--nz-emerald)",[
 ("/himachal-tour-packages/","All Himachal tour packages"),
 ("/himachal-tour-package-from-delhi/","Himachal tour from Delhi"),
 ("/himachal-tour-package-from-chandigarh/","Himachal tour from Chandigarh"),
 ("/himachal-tour-package-5-nights-6-days/","5 nights / 6 days plan"),
 ("/himachal-tour-package-for-family/","Himachal for families"),
 ("/shimla-vs-manali/","Shimla vs Manali: which one?"),
 ("/best-month-to-visit-himachal/","Best month to visit Himachal"),
 ("/rohtang-pass-permit-himachal-road-status/","Rohtang permit & road status")]),
("adventure","Snow & adventure","रोमांच","var(--nz-glacier)",[
 ("/adventure/","All adventure activities"),
 ("/adventure/paragliding-in-bir-billing/","Paragliding in Bir Billing"),
 ("/adventure/solang-valley-activities/","Solang Valley activities"),
 ("/adventure/snow-kingdom-kufri/","Snow Kingdom, Kufri"),
 ("/adventure/atal-tunnel-sissu-snow-trip/","Atal Tunnel & Sissu snow trip"),
 ("/adventure/skiing-in-himachal/","Skiing in Himachal"),
 ("/adventure/igloo-stay-manali/","Igloo stay in Manali"),
 ("/adventure/snow-suit-and-boots-on-rent-manali/","Snow suit & boots on rent")]),
("mountains","Mountains & treks","पर्वत","var(--nz-indigo)",[
 ("/mountains-of-india/","Mountains of India"),
 ("/mountains-of-india/trekking-peaks/","Trekking peaks for beginners"),
 ("/mountains-of-india/imf-permit-fees/","IMF permit fees"),
 ("/mountains-of-india/mountaineering-courses/","Mountaineering courses"),
 ("/mountains-of-india/stok-kangri/","Stok Kangri"),
 ("/mountains-of-india/friendship-peak/","Friendship Peak"),
 ("/mountains-of-india/hanuman-tibba/","Hanuman Tibba"),
 ("/mountains-of-india/deo-tibba/","Deo Tibba")]),
("kashmir","Kashmir & Ladakh","कश्मीर","var(--nz-lagoon)",[
 ("/destination/kashmir-tour-packages/","Kashmir tour packages"),
 ("/best-kashmir-tour-package/","How to pick a Kashmir package"),
 ("/kashmir-tour-package-6-days-itinerary/","Kashmir 6-day itinerary"),
 ("/destination/leh-ladakh-tour-packages/","Leh Ladakh tour packages"),
 ("/leh-ladakh-road-trip-2026/","Leh Ladakh road trip 2026"),
 ("/leh-to-pangong-lake/","Leh to Pangong Lake"),
 ("/best-mountain-pass-ladakh/","Best mountain passes in Ladakh")]),
("spiritual","Pilgrimage & Uttarakhand","तीर्थ","var(--nz-saffron)",[
 ("/pilgrimage-tours/","Pilgrimage tours"),
 ("/pilgrimage-tours/shakti-peeth-himachal/","Shakti Peeth of Himachal"),
 ("/pilgrimage-tours/12-jyotirlinga/","12 Jyotirlinga yatra"),
 ("/destination/chardham-tour-packages/","Char Dham packages"),
 ("/char-dham-closing-dates-2026/","Char Dham closing dates 2026"),
 ("/char-dham-yatra-for-nri/","Char Dham for NRIs"),
 ("/uttarakhand/","Uttarakhand tours")]),
("beach","Goa, Kerala & Rajasthan","समुद्र","var(--nz-sand)",[
 ("/goa-tour-packages/","Goa tour packages"),
 ("/kerala-tour-packages/","Kerala tour packages"),
 ("/kerala-trip-plan-2026-budget-itinerary/","Kerala budget itinerary 2026"),
 ("/rajasthan-tour-packages/","Rajasthan tour packages"),
 ("/rajasthan-heritage-tour-packages-price-the-complete-2026-cost-guide/","Rajasthan trip cost guide"),
 ("/golden-triangle-tour/","Golden Triangle tour"),
 ("/honeymoon-trip/","Honeymoon trips")]),
("cabs","Cabs & road trips","टैक्सी","var(--nz-leaf)",[
 ("/cabs/","All cab services"),
 ("/cabs/delhi-to-manali-taxi/","Delhi to Manali taxi"),
 ("/cabs/delhi-to-shimla-taxi/","Delhi to Shimla taxi"),
 ("/cabs/chandigarh-to-manali-taxi/","Chandigarh to Manali taxi"),
 ("/cabs/shimla-to-manali-taxi/","Shimla to Manali taxi"),
 ("/cabs/jammu-to-srinagar-taxi/","Jammu to Srinagar taxi"),
 ("/cabs/tempo-traveller-hire-delhi/","Tempo Traveller from Delhi"),
 ("/cabs/innova-crysta-on-rent/","Innova Crysta on rent")]),
("dmc","For travel agents (DMC)","B2B","var(--nz-rose)",[
 ("/best-dmc-for-himachal-pradesh/","Himachal DMC"),
 ("/spiti-dmc/","Spiti DMC"),
 ("/kashmir-dmc/","Kashmir DMC"),
 ("/ladakh-dmc/","Ladakh DMC"),
 ("/uttarakhand-dmc/","Uttarakhand DMC"),
 ("/goa-dmc-travel-agents/","Goa DMC"),
 ("/kerala-dmc-travel-agents/","Kerala DMC")]),
]

src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
assert 'id="nz-explore"' not in s and 'nz-cmp' not in s, 'already applied'

def once(hay, needle):
    assert hay.count(needle) == 1, (needle[:60], hay.count(needle))
    return hay.index(needle)

# ---------- 1. CSS (appended inside the nature style block) ----------
CSS = r"""
/* ---------- 2026-10-08: compare trips + explore-more links ---------- */
.nz-cmp-t{position:relative;align-self:flex-start;display:inline-flex;align-items:center;gap:6px;border:1.5px solid var(--nz-line);background:#fff;color:var(--nz-forest);border-radius:999px;padding:6px 12px;font:700 .78rem var(--nz-body);cursor:pointer;transition:background .18s ease,border-color .18s ease}
.nz-cmp-t::after{content:"";position:absolute;inset:-10px -4px}
.nz-cmp-t svg{width:15px;height:15px;flex:none}
.nz-cmp-t:hover{border-color:var(--nz-emerald)}
.nz-cmp-t[aria-pressed="true"]{background:var(--nz-forest);border-color:var(--nz-forest);color:#fff}
.nz-cmpbar{position:fixed;z-index:99997;left:50%;bottom:calc(96px + env(safe-area-inset-bottom,0px));width:min(560px,calc(100% - 24px));display:flex;align-items:center;gap:10px;padding:8px 8px 8px 12px;background:#fff;border:1.5px solid var(--nz-line);border-radius:20px;box-shadow:var(--nz-shadow-lg);transform:translate(-50%,0);transition:transform .25s ease,opacity .25s ease}
.nz-cmpbar.off{transform:translate(-50%,140%);opacity:0;pointer-events:none}
html.nz-open .nz-cmpbar{display:none}
html.nz-cmp-on .nz-toast{bottom:calc(176px + env(safe-area-inset-bottom,0px))}
.nz-cmpbar .th{display:flex;flex:none}
.nz-cmpbar .th img{width:36px;height:36px;border-radius:10px;object-fit:cover;border:2px solid #fff;margin-left:-8px;box-shadow:0 1px 4px rgba(0,0,0,.15)}
.nz-cmpbar .th img:first-child{margin-left:0}
.nz-cmpbar .tx{flex:1;min-width:0;font-size:.8rem;line-height:1.25;color:var(--nz-muted)}
.nz-cmpbar .tx b{display:block;color:var(--nz-ink);font-size:.9rem}
.nz-cmpbar .nz-btn{padding:12px 16px;min-height:44px}
.nz-cmpbar .nz-btn[disabled]{opacity:.55;cursor:not-allowed;transform:none}
.nz-cmpbar .x{width:44px;height:44px;flex:none;border:0;background:var(--nz-mint);border-radius:50%;display:grid;place-items:center;cursor:pointer;color:var(--nz-forest)}
.nz-cmpbar .x svg{width:16px;height:16px}
.nz-cmpw{overflow-x:auto;margin:0 -22px;padding:0 22px 4px;-webkit-overflow-scrolling:touch}
.nz-cmptb{width:100%;min-width:460px;border-collapse:separate;border-spacing:0;font-size:.86rem;table-layout:fixed}
.nz-cmptb th,.nz-cmptb td{text-align:left;vertical-align:top;padding:10px 8px;border-bottom:1px solid var(--nz-line)}
.nz-cmptb tbody th{width:96px;font-size:.72rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--nz-muted)}
.nz-cmptb thead th{border-bottom:0;padding-top:4px}
.nz-cmptb thead img{width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:12px;margin-bottom:8px}
.nz-cmptb thead b{display:block;font:700 .9rem/1.25 var(--nz-display);color:var(--nz-ink)}
.nz-cmptb .pr{font:800 1.08rem var(--nz-display);color:var(--nz-ink)}
.nz-cmptb .tag{display:inline-block;margin-top:4px;font-size:.7rem;font-weight:700;background:var(--nz-mint);color:var(--nz-forest);border-radius:6px;padding:2px 7px}
.nz-cmptb ul{margin:0;padding:0;list-style:none;display:grid;gap:4px}
.nz-cmptb li{display:flex;gap:5px;font-size:.8rem}
.nz-cmptb li svg{width:14px;height:14px;flex:none;margin-top:2px;color:var(--nz-emerald)}
.nz-cmptb .rm{margin-top:6px;border:0;background:none;color:var(--nz-muted);font:600 .76rem var(--nz-body);text-decoration:underline;cursor:pointer;padding:8px 0;min-height:44px}
.nz-cmptb .nz-btn{padding:10px 14px;font-size:.82rem;min-height:44px;width:100%}
.nz-cmptb a.pg{display:inline-block;margin-top:8px;font-size:.8rem;font-weight:600;color:var(--nz-emerald);padding:6px 0}
.nz-explore{background:linear-gradient(180deg,var(--nz-snow),var(--nz-mint));padding:clamp(48px,7vw,84px) 0;content-visibility:auto;contain-intrinsic-size:auto 900px}
.nz-explore .nz-head{margin-bottom:22px}
.nz-explore .nz-head p{color:var(--nz-muted);max-width:640px;margin-top:8px}
.nz-xg{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:14px}
.nz-xc{--c:var(--nz-emerald);background:#fff;border:1.5px solid var(--nz-line);border-radius:var(--nz-r);padding:16px 14px 10px;box-shadow:var(--nz-shadow);position:relative;overflow:hidden;transition:border-color .2s ease,box-shadow .2s ease,transform .2s ease}
.nz-xc::before{content:"";position:absolute;left:0;right:0;top:0;height:4px;background:var(--c)}
.nz-xc.on{border-color:var(--c);box-shadow:0 0 0 3px color-mix(in srgb,var(--c) 22%,transparent),var(--nz-shadow);transform:translateY(-2px)}
.nz-xc h3{font-size:1.02rem;display:flex;align-items:baseline;justify-content:space-between;gap:8px;margin:0 0 6px}
.nz-xc h3 span{font:600 .8rem var(--nz-deva);color:color-mix(in srgb,var(--c) 72%,#000)}
.nz-xc ul{list-style:none;margin:0;padding:0}
.nz-xc li+li{border-top:1px dashed var(--nz-line)}
.nz-xc a{display:flex;align-items:center;justify-content:space-between;gap:8px;min-height:44px;padding:6px 2px;text-decoration:none;font-size:.9rem;font-weight:600;color:var(--nz-ink)}
.nz-xc a::after{content:"→";color:color-mix(in srgb,var(--c) 72%,#000);transition:transform .18s ease}
.nz-xc a:hover{color:var(--nz-forest)}
.nz-xc a:hover::after{transform:translateX(3px)}
@media (max-width:640px){
  .nz-xg{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;scrollbar-width:none;margin:0 calc(-1*clamp(16px,4vw,40px));padding:4px clamp(16px,4vw,40px) 10px}
  .nz-xg::-webkit-scrollbar{display:none}
  .nz-xc{flex:0 0 84%;scroll-snap-align:start}
  .nz-cmpbar .tx span{display:none}
  .nz-cmptb{min-width:400px;font-size:.82rem}
  .nz-cmptb tbody th{width:74px;font-size:.66rem;letter-spacing:.03em;padding-left:2px}
}
@media (max-width:768px){ /* legacy html{zoom:.9}: keep tap targets >=44px after zoom */
  .nz-xc a,.nz-cmpbar .nz-btn,.nz-cmptb .rm,.nz-cmptb .nz-btn{min-height:49px}
  .nz-cmpbar .x{width:49px;height:49px}
  .nz-cmp-t{padding:8px 13px}
  .nz-cmp-t::after{inset:-11px -4px}
}
"""
i = once(s, '<style id="suzu-nature-2026-10">')
j = s.index('</style>', i)
s = s[:j] + CSS + s[j:]

# ---------- 2. Explore-more section after #tour-packages ----------
i = once(s, '<section class="nz nz-app" id="tour-packages"')
j = s.index('</section>', i) + len('</section>')
assert '<section' not in s[i + 10:j], 'nested section in #tour-packages'
cards = []
for key, name, hi, col, items in G:
    lis = ''.join('<li><a href="https://suzutravels.com%s">%s</a></li>' % (u, H.escape(t)) for u, t in items)
    lang = '' if hi in ('B2B',) else ' lang="hi"'
    cards.append('<div class="nz-xc" data-g="%s" style="--c:%s"><h3>%s <span%s>%s</span></h3><ul>%s</ul></div>' % (key, col, H.escape(name), lang, hi, lis))
SEC = ('\n<section class="nz nz-explore" id="nz-explore" aria-labelledby="nz-x-h"><div class="nz-wrap">'
       '<div class="nz-head"><div class="st"><span class="nz-eyebrow">Explore more</span>'
       '<h2 id="nz-x-h">Guides, activities and cabs, <span>by region</span></h2></div>'
       '<p>Package hubs, how-to guides, adventure activities, mountain pages and point-to-point cabs from our team. Pick a region above and its links light up here.</p></div>'
       '<div class="nz-xg" role="navigation" aria-label="Explore more by region">' + ''.join(cards) + '</div></div></section>')
s = s[:j] + SEC + s[j:]

# ---------- 3. JS (inside the nature script, before its closing IIFE) ----------
JS = r"""
/* ================= 2026-10-08: COMPARE TRIPS (max 3) ================= */
var CMP=[],CMPI='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4" width="7" height="16" rx="2"/><rect x="14" y="4" width="7" height="16" rx="2"/></svg>';
function cimg(t){var im=$('#nz-grid .nz-card[data-slug="'+t.slug+'"] img');return im?(im.currentSrc||im.getAttribute('src')):t.img}
var bar=document.createElement('div');bar.className='nz nz-cmpbar off';bar.id='nz-cmpbar';bar.setAttribute('role','region');bar.setAttribute('aria-label','Compare trips');
bar.innerHTML='<div class="th"></div><div class="tx" aria-live="polite"></div><button class="nz-btn nz-btn-gold" type="button" id="nz-cmp-go">Compare</button><button class="x" type="button" aria-label="Clear comparison">'+SVG.x+'</button>';
document.body.appendChild(bar);
function paintCmp(){
  $$('.nz-cmp-t').forEach(function(b){var on=CMP.indexOf(b.dataset.slug)>-1;b.setAttribute('aria-pressed',on?'true':'false');b.lastChild.textContent=on?'Added':'Compare'});
  bar.classList.toggle('off',!CMP.length);document.documentElement.classList.toggle('nz-cmp-on',!!CMP.length);
  $('.th',bar).innerHTML=CMP.map(function(k){return '<img src="'+cimg(BY[k])+'" alt="" width="36" height="36" decoding="async">'}).join('');
  $('.tx',bar).innerHTML='<b>'+CMP.length+' of 3 selected</b><span>'+(CMP.length<2?'Add one more trip to compare':'Ready to compare')+'</span>';
  var g=$('#nz-cmp-go');g.disabled=CMP.length<2;g.textContent=CMP.length<2?'Compare':'Compare '+CMP.length;
}
function toggleCmp(slug){var k=CMP.indexOf(slug);if(k>-1)CMP.splice(k,1);else{if(CMP.length>=3){toast('You can compare up to 3 trips');return}CMP.push(slug);if(CMP.length===1)toast('Added. Pick 1 or 2 more to compare.')}paintCmp()}
$$('#nz-grid .nz-card').forEach(function(c){var b=$('.nz-body',c),f=$('.nz-facts',c),t=BY[c.dataset.slug];if(!b||!t)return;
  var btn=document.createElement('button');btn.type='button';btn.className='nz-cmp-t';btn.dataset.slug=t.slug;btn.setAttribute('aria-pressed','false');btn.setAttribute('aria-label','Compare '+t.title);
  btn.innerHTML=CMPI+'<span>Compare</span>';btn.addEventListener('click',function(){toggleCmp(t.slug)});
  if(f&&f.nextSibling)b.insertBefore(btn,f.nextSibling);else b.appendChild(btn)});
$('.x',bar).addEventListener('click',function(){CMP=[];paintCmp()});
$('#nz-cmp-go').addEventListener('click',function(){if(CMP.length>1)openCompare()});
function openCompare(){
  cur=null;lastFocus=document.activeElement;renderCompare();
  var sh=$('#nz-sheet'),sc=$('#nz-scrim');sh.hidden=false;sc.hidden=false;requestAnimationFrame(function(){sh.classList.add('on');sc.classList.add('on')});
  document.documentElement.style.overflow='hidden';document.documentElement.classList.add('nz-open');setTimeout(function(){var c=$('.nz-close',sh);if(c)c.focus()},60)}
function renderCompare(){
  var L=CMP.map(function(k){return BY[k]}),sc=$('#nz-sc'),se=season('');
  var priced=L.filter(function(t){return t.price}),lo=priced.length>1?Math.min.apply(null,priced.map(function(t){return t.price})):0;
  var sd=Math.min.apply(null,L.map(function(t){return t.days}));if(L.every(function(t){return t.days===sd}))sd=-1;
  function row(lbl,fn){return '<tr><th scope="row">'+lbl+'</th>'+L.map(function(t){return '<td>'+fn(t)+'</td>'}).join('')+'</tr>'}
  var h='<div class="nz-panel" style="display:grid;gap:14px;padding-top:22px">'+
   '<div style="display:flex;justify-content:space-between;align-items:center"><span class="nz-eyebrow">Compare trips</span><button class="nz-close" type="button" aria-label="Close" style="position:static">'+SVG.x+'</button></div>'+
   '<h2 id="nz-sh-title" style="font-size:1.45rem">'+L.length+' trips, side by side</h2>'+
   '<p class="nz-note">Prices are each package page’s published starting rate, per person on twin sharing. Today ('+se.label+') is '+(se.peak?'peak season, so expect the peak row':'off-season, so the “from” rate applies')+' until '+se.next+'.</p>'+
   '<div class="nz-cmpw"><table class="nz-cmptb"><thead><tr><td></td>'+L.map(function(t){return '<th scope="col"><img src="'+cimg(t)+'" alt="'+t.alt.replace(/"/g,'&quot;')+'" loading="lazy" decoding="async"><b>'+t.title+'</b><button class="rm" type="button" data-rm="'+t.slug+'">Remove</button></th>'}).join('')+'</tr></thead><tbody>'+
   row('Price from',function(t){return t.price?'<span class="pr">'+inr(t.price)+'</span>'+(lo&&t.price===lo?'<br><span class="tag">Lowest here</span>':''):'<b>Price on request</b><br><small style="color:var(--nz-muted)">Quoted in ~2 hrs</small>'})+
   row('Peak season',function(t){return t.price?inr(t.price*PEAK)+'<br><small style="color:var(--nz-muted)">15 Mar–30 Jun, Oct, 20 Dec–5 Jan</small>':'—'})+
   row('Hotels',function(t){return t.price?(t.tiers?'Deluxe '+inr(t.price)+'<br>Super Deluxe '+inr(t.price*1.18)+'<br>Luxury '+inr(t.price*1.35):'As per itinerary'):'Your choice, 3★ to 5★'})+
   row('Duration',function(t){return '<b>'+t.days+'D / '+t.nights+'N</b>'+(L.length>1&&t.days===sd?'<br><span class="tag">Shortest</span>':'')})+
   row('Starts',function(t){return t.start})+
   row('Region',function(t){return t.regionName})+
   row('Route',function(t){return t.route.length?t.route.join(' → '):'—'})+
   row('Highest point',function(t){return t.top?t.top[0]+'<br>'+t.top[1].toLocaleString('en-IN')+' m':'—'})+
   row('Best season',function(t){return t.season})+
   row('Included',function(t){return t.inc.length?'<ul>'+t.inc.slice(0,5).map(function(x){return '<li>'+SVG.check+'<span>'+x+'</span></li>'}).join('')+'</ul>':'<a href="'+t.url+'">See package page</a>'})+
   row('',function(t){return '<button class="nz-btn nz-btn-ink" type="button" data-cv="'+t.slug+'">View trip</button><a class="pg" href="'+t.url+'">Package page →</a>'})+
   '</tbody></table></div>'+
   '<p class="nz-note">Booking terms are the same for every trip: a small token advance locks the rate, the balance is paid before the trip, and one date change is allowed within 6 months. The advance is non-refundable.</p></div>';
  sc.innerHTML=h;sc.scrollTop=0;$('.nz-close',sc).onclick=closeTrip;
  $$('[data-rm]',sc).forEach(function(b){b.onclick=function(){toggleCmp(b.dataset.rm);if(CMP.length<2){closeTrip();return}renderCompare()}});
  $$('[data-cv]',sc).forEach(function(b){b.onclick=function(){var lf=lastFocus;openTrip(b.dataset.cv);lastFocus=lf}});
  var msg='Hi Suzu Travels, I am comparing these trips:\n'+L.map(function(t,k){return (k+1)+'. '+t.title+' ('+t.days+'D/'+t.nights+'N from '+t.start+')'+(t.price?' from '+inr(t.price)+' pp':'')}).join('\n')+'\nWhich one suits my dates best?';
  $('#nz-foot').innerHTML='<div class="p"><small>Comparing</small><strong>'+L.length+' trips</strong></div><a class="nz-btn nz-btn-wa" href="'+waLink(msg)+'" target="_blank" rel="noopener">'+SVG.wa+' Ask which suits me</a>';
}
paintCmp();

/* ================= 2026-10-08: EXPLORE-MORE sync with region tabs ================= */
(function(){var X=$('#nz-explore');if(!X)return;var MAP={himachal:'himachal',kashmir:'kashmir',ladakh:'kashmir',uttarakhand:'spiritual',spiritual:'spiritual',rajasthan:'beach',goa:'beach',kerala:'beach'};
  function sync(r){var g=MAP[r]||'';$$('.nz-xc',X).forEach(function(c){c.classList.toggle('on',c.dataset.g===g)});
    var c=g&&$('.nz-xc[data-g="'+g+'"]',X),rail=$('.nz-xg',X);if(c&&rail&&rail.scrollWidth>rail.clientWidth+4)rail.scrollTo({left:c.offsetLeft-rail.firstElementChild.offsetLeft,behavior:reduce?'auto':'smooth'})}
  $$('.nz-reg').forEach(function(b){b.addEventListener('click',function(){sync(b.dataset.r)})});})();
"""
i = once(s, '<script id="suzu-nature-2026-10-js">')
j = s.index('</script>', i)
k = s.rindex('})();', i, j)
s = s[:k] + JS + s[k:]

open(dst, 'w', encoding='utf-8').write(s)
print('ok', len(s.encode()))
