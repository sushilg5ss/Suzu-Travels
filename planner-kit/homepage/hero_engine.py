#!/usr/bin/env python3
"""Homepage booking-engine hero (Phase 2, 15 Oct 2026).
apply:  python3 homepage/hero_engine.py before.html after.html
Replaces the hero FILM inside #nz-hero with:
  - a light photo slideshow background (.tpx-bg, crossfade + slow zoom, lazy after load)
  - <section id="tp-engine"> MakeMyTrip-style search card (Holiday planner · Yatra & Mata darshan · Cabs · Hotels)
  - an on-page overlay that opens /plan-your-trip/?embed=1&... in an iframe (no page change for the visitor)
Keeps: #nz-hero, pill row (weather chip lands there), H1, accent, desc, the 3 CTA links, checks, ridges.
Removes: film wrap + nz-film-boot, grain, pause button, "Watch our India film" button, nz-cal, nz-cap, nz-rail,
         and the two suzu-film2 poster preloads in <head>.
Nature JS hero(): guard changed to return when there is no video (it only drove the film).
"""
import json, os, re, sys, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'data'))
from places import PLACES
TPL = json.load(open(os.path.join(HERE, '..', 'data', 'templates.json'), encoding='utf-8'))
RATES = json.load(open(os.path.join(HERE, '..', 'data', 'rates.json'), encoding='utf-8'))
U = 'https://suzutravels.com/wp-content/uploads/'
SLIDES = [  # [desktop, phone, caption, template id]
    [U + '2026/04/Shimla-Manali-Tour-1024x466.webp', U + '2026/10/family-snowball-fight-falling-snow-768x512.webp', 'Shimla – Manali, Himachal', 'shimla-manali'],
    [U + '2026/05/Kashmir-1024x576.webp', U + '2026/05/Kashmir-1024x576.webp', 'Srinagar, Kashmir', 'kashmir-classic'],
    [U + '2026/10/family-snowball-fight-falling-snow-1536x1024.webp', U + '2026/04/Spiti_-768x512.webp', 'Snow days in Himachal', 'manali-honeymoon'],
    [U + '2026/04/Spiti_-1024x683.webp', U + '2026/04/Spiti_-768x512.webp', 'Key Monastery, Spiti', 'spiti-circuit'],
    [U + '2026/04/gangotri-temple-1024x683.webp', U + '2026/04/gangotri-temple-768x512.webp', 'Gangotri Dham, Char Dham', 'char-dham'],
    [U + '2026/10/kanchenjunga-sunrise-sikkim-1536x1024.webp', U + '2026/10/kanchenjunga-sunrise-sikkim-768x512.webp', 'Himalayan sunrise', 'nau-devi'],
]
FROM = [p['id'] for p in PLACES if p['kind'] == 'hub'] + ['srinagar', 'leh', 'haridwar', 'shimla', 'manali', 'dharamshala', 'kullu']
DATA = {
    't': [[t['id'], t['name'], t['cat'], sum(s[1] for s in t['stops']) + 1, t['start']] for t in TPL],
    'p': [[p['id'], p['name'], p['hi'], p['kind'], p['region']] for p in PLACES],
    'f': FROM,
    'v': [[v['id'], v['name'].split(' (')[0], v['seats']] for v in RATES['cab']['vehicles']],
    's': [[s[2], s[3]] for s in SLIDES[1:]], 'si': [[s[0], s[1]] for s in SLIDES[1:]],
}

CSS = r"""<style id="tp-engine-css">
/* Suzu booking-engine hero (Trip Planner agent lane) */
.tpx-bg{position:absolute;inset:0;z-index:-3;overflow:hidden;background:#123d26}
.tpx-bg img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;transition:opacity 1.4s ease;transform:scale(1.02);will-change:opacity,transform}
.tpx-bg img.on{opacity:1;animation:tpxZoom 14s ease-out forwards}
@keyframes tpxZoom{from{transform:scale(1.02)}to{transform:scale(1.09)}}
.tpx-snow{position:absolute;inset:0;z-index:-2;pointer-events:none;opacity:.55;background-image:radial-gradient(2px 2px at 20% 30%,#fff 50%,transparent 51%),radial-gradient(1.6px 1.6px at 70% 10%,#fff 50%,transparent 51%),radial-gradient(2.2px 2.2px at 40% 70%,#fff 50%,transparent 51%),radial-gradient(1.4px 1.4px at 85% 55%,#fff 50%,transparent 51%),radial-gradient(1.8px 1.8px at 10% 85%,#fff 50%,transparent 51%);background-size:340px 340px;animation:tpxSnow 26s linear infinite}
@keyframes tpxSnow{from{background-position:0 0,0 0,0 0,0 0,0 0}to{background-position:40px 340px,-30px 340px,20px 340px,-50px 340px,30px 340px}}
.nz-hero.tpx{justify-content:flex-end}
.nz-hero.tpx .nz-desc,.nz-hero.tpx .nz-checks{display:none}
.nz-hero.tpx .nz-hero-in{padding-block:clamp(26px,5vw,60px) 14px}
#tp-engine{position:relative;z-index:2;margin:6px 0 clamp(70px,9vw,120px);color:#10261a;font-family:var(--nz-body,'Plus Jakarta Sans',system-ui,sans-serif)}
#tp-engine *{box-sizing:border-box}
.tpe-card{background:#fff;border-radius:22px;box-shadow:0 30px 60px -28px rgba(0,0,0,.55),0 0 0 1px rgba(16,61,38,.06);max-width:1180px}
.tpe-tabs{display:flex;gap:4px;padding:8px 8px 0;overflow-x:auto;scrollbar-width:none}
.tpe-tabs::-webkit-scrollbar{display:none}
.tpe-tabs button{flex:0 0 auto;display:flex;align-items:center;gap:8px;border:0;background:none;padding:11px 15px 13px;border-radius:14px 14px 0 0;font-weight:800;font-size:14px;line-height:1;font-family:inherit;color:#5b6b62;border-bottom:3px solid transparent;min-height:46px;cursor:pointer}
.tpe-tabs button svg{width:21px;height:21px}
.tpe-tabs button[aria-selected=true]{color:#123d26;border-bottom-color:#1f7a45;background:linear-gradient(180deg,#e9f5ee,#fff)}
.tpe-pane{border-top:1px solid #d9e6dd;padding:14px}
.tpe-row{display:grid;grid-template-columns:1fr 1.5fr .95fr 1fr auto;gap:10px;align-items:stretch}
.tpe-row.cab{grid-template-columns:1.2fr 1.2fr .9fr 1fr auto}
.tpe-row.hot{grid-template-columns:1.4fr 1fr .8fr .8fr 1.1fr auto}
.tpe-f{position:relative;display:flex;flex-direction:column;justify-content:center;border:1.5px solid #d9e6dd;border-radius:14px;padding:7px 12px;min-height:62px;background:#fbfdfb;min-width:0}
.tpe-f:focus-within{border-color:#1f7a45;background:#fff}
.tpe-f label{font-size:11px;font-weight:800;letter-spacing:.07em;text-transform:uppercase;color:#5b6b62}
.tpe-f input,.tpe-f select{border:0;background:none;padding:2px 0;font-weight:800;font-size:16.5px;line-height:1.3;font-family:inherit;color:#123d26;width:100%;min-height:30px;outline:none;-webkit-appearance:none;appearance:none;min-width:0}
.tpe-f select{cursor:pointer;padding-right:14px;background-image:linear-gradient(45deg,transparent 50%,#5b6b62 50%),linear-gradient(135deg,#5b6b62 50%,transparent 50%);background-position:calc(100% - 8px) 55%,calc(100% - 3px) 55%;background-size:5px 5px;background-repeat:no-repeat}
.tpe-f small{font-size:11.5px;color:#5b6b62;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.tpe-go{border:0;border-radius:14px;padding:0 24px;min-height:62px;background:linear-gradient(135deg,#e2a93b,#c9962b);color:#2b1d02;font-weight:900;font-size:17px;line-height:1;font-family:inherit;box-shadow:0 12px 24px -12px rgba(201,150,43,.9);white-space:nowrap;cursor:pointer}
.tpe-go:hover{filter:brightness(1.05)}
.tpe-quick{display:flex;flex-wrap:wrap;gap:7px;margin-top:11px;align-items:center}
.tpe-quick b{font-size:12.5px;color:#5b6b62}
.tpe-chip{display:inline-flex;align-items:center;gap:6px;border:1.5px solid #d9e6dd;background:#fff;border-radius:999px;padding:5px 12px;font-weight:700;font-size:13px;line-height:1.2;font-family:inherit;color:#123d26;min-height:36px;cursor:pointer}
.tpe-chip:hover{border-color:#1f7a45;background:#e9f5ee}
.tpe-yatra{display:flex;flex-wrap:wrap;gap:8px}
.tpe-yatra .tpe-chip{min-height:44px;padding:8px 14px}
.tpe-dd{position:absolute;left:-2px;right:-2px;top:calc(100% + 6px);z-index:50;background:#fff;border-radius:16px;box-shadow:0 24px 50px -20px rgba(0,0,0,.45),0 0 0 1px rgba(16,61,38,.08);max-height:330px;overflow:auto;padding:6px}
.tpe-dd[hidden]{display:none}
.tpe-dd button{display:flex;width:100%;align-items:center;gap:10px;border:0;background:none;text-align:left;padding:8px 10px;border-radius:10px;min-height:44px;cursor:pointer;font-family:inherit;font-size:inherit;color:#10261a}
.tpe-dd button:hover,.tpe-dd button.on{background:#e9f5ee}
.tpe-dd b{display:block;font-size:14px;color:#123d26}
.tpe-dd small{display:block;font-size:12px;color:#5b6b62}
.tpe-dd .hd{font-size:10.5px;font-weight:800;letter-spacing:.08em;color:#5b6b62;text-transform:uppercase;padding:8px 10px 3px}
.tpe-note{display:flex;flex-wrap:wrap;gap:6px 14px;margin-top:10px;font-size:12px;color:#5b6b62;font-weight:600}
.tpe-note span::before{content:"✓ ";color:#1f7a45;font-weight:900}
.tpx-cap{position:absolute;right:clamp(12px,3vw,40px);top:clamp(80px,12vh,130px);z-index:2;display:inline-flex;align-items:center;gap:8px;border:0;border-radius:999px;background:rgba(14,42,27,.55);color:#fff;padding:7px 14px;font:700 13px/1.2 var(--nz-body,system-ui);cursor:pointer;transition:opacity .5s}
.tpx-cap:hover{background:rgba(14,42,27,.75)}
.tpx-cap u{text-decoration:none;color:#ffd86b}
#tp-ov{position:fixed;inset:0;z-index:2147483600;background:#f6faf7;display:flex;flex-direction:column}
#tp-ov[hidden]{display:none}
#tp-ov iframe{flex:1;width:100%;border:0;background:#f6faf7}
#tp-ov .ld{position:absolute;inset:0;display:grid;place-items:center;font:700 15px var(--nz-body,system-ui);color:#123d26;pointer-events:none}
#tp-ov .ld[hidden]{display:none}
#tp-ov .ld i{width:42px;height:42px;border-radius:50%;border:4px solid #d9e6dd;border-top-color:#1f7a45;animation:tpxSpin .8s linear infinite;display:block;margin:0 auto 10px}
@keyframes tpxSpin{to{transform:rotate(360deg)}}
html.tp-ov-open,html.tp-ov-open body{overflow:hidden!important}
@media(max-width:1000px){.tpe-row,.tpe-row.cab,.tpe-row.hot{grid-template-columns:1fr 1fr}.tpe-row .w2,.tpe-go{grid-column:1/-1}}
@media(max-width:640px){
 #tp-engine{margin-bottom:64px}
 .tpe-pane{padding:12px}
 .tpe-row{gap:8px}
 .tpe-f{min-height:56px;padding:6px 10px}
 .tpe-f input,.tpe-f select{font-size:15.5px}
 .tpe-go{min-height:54px}
 .tpe-tabs button{padding:10px 11px 12px;font-size:13px}
 .tpx-cap{top:auto;bottom:10px;right:10px;font-size:12px;padding:6px 11px}
 .tpe-note{display:none}
}
@media(prefers-reduced-motion:reduce){.tpx-bg img.on{animation:none}.tpx-snow{display:none}}
</style>"""

ICON = {
 'plan': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M9 4 3 6v14l6-2 6 2 6-2V4l-6 2-6-2z"/><path d="M9 4v14M15 6v14"/></svg>',
 'yatra': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 2l3 5H9l3-5zM6 21V11l6-4 6 4v10M4 21h16M10 21v-5h4v5"/></svg>',
 'cab': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M5 16V11l2-5h10l2 5v5M3 16h18v3H3zM7 19v2M17 19v2M5 11h14"/></svg>',
 'hotel': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M3 21V5h11v16M14 9h7v12M7 9h3M7 13h3M7 17h3M17 13h1M17 17h1M2 21h20"/></svg>',
}

SECTION = """<section id="tp-engine" aria-label="Plan your trip — create your own itinerary">
<div class="tpe-card">
<div class="tpe-tabs" role="tablist" aria-label="What do you want to plan">
<button type="button" role="tab" id="tpe-t-plan" aria-controls="tpe-plan" aria-selected="true">""" + ICON['plan'] + """Plan your trip</button>
<button type="button" role="tab" id="tpe-t-yatra" aria-controls="tpe-yatra" aria-selected="false" tabindex="-1">""" + ICON['yatra'] + """Yatra &amp; Mata darshan</button>
<button type="button" role="tab" id="tpe-t-cab" aria-controls="tpe-cab" aria-selected="false" tabindex="-1">""" + ICON['cab'] + """Cabs</button>
<button type="button" role="tab" id="tpe-t-hotel" aria-controls="tpe-hotel" aria-selected="false" tabindex="-1">""" + ICON['hotel'] + """Hotels</button>
</div>
<div class="tpe-pane" id="tpe-plan" role="tabpanel" aria-labelledby="tpe-t-plan">
<div class="tpe-row">
<div class="tpe-f"><label for="tpe-from">Starting from</label><select id="tpe-from"></select><small>Pickup city</small></div>
<div class="tpe-f w2"><label for="tpe-to">Going to</label><input id="tpe-to" type="text" autocomplete="off" placeholder="Manali, Mata darshan, Char Dham…" role="combobox" aria-expanded="false" aria-controls="tpe-dd" aria-autocomplete="list"><small id="tpe-to-s">Place or ready trip idea</small><div class="tpe-dd" id="tpe-dd" role="listbox" hidden></div></div>
<div class="tpe-f"><label for="tpe-date">Start date</label><input id="tpe-date" type="date"><small id="tpe-date-s">&nbsp;</small></div>
<div class="tpe-f"><label for="tpe-pax">Travellers</label><select id="tpe-pax"></select><small>Rooms &amp; car next</small></div>
<button type="button" class="tpe-go" id="tpe-go">Plan my trip</button>
</div>
<div class="tpe-quick" id="tpe-quick"><b>Popular:</b></div>
<div class="tpe-note"><span>Day-by-day plan &amp; road map</span><span>Instant price estimate</span><span>Free PDF download</span><span>For travellers &amp; travel agents</span></div>
</div>
<div class="tpe-pane" id="tpe-yatra" role="tabpanel" aria-labelledby="tpe-t-yatra" hidden><div class="tpe-yatra" id="tpe-yatra-list"></div></div>
<div class="tpe-pane" id="tpe-cab" role="tabpanel" aria-labelledby="tpe-t-cab" hidden>
<div class="tpe-row cab">
<div class="tpe-f"><label for="tpe-cf">From</label><select id="tpe-cf"></select></div>
<div class="tpe-f"><label for="tpe-ct">To</label><select id="tpe-ct"></select></div>
<div class="tpe-f"><label for="tpe-ctype">Trip</label><select id="tpe-ctype"><option value="one">One way drop</option><option value="round">Round trip</option></select></div>
<div class="tpe-f"><label for="tpe-cv">Car</label><select id="tpe-cv"></select></div>
<button type="button" class="tpe-go" id="tpe-cgo">Get fare</button>
</div></div>
<div class="tpe-pane" id="tpe-hotel" role="tabpanel" aria-labelledby="tpe-t-hotel" hidden>
<div class="tpe-row hot">
<div class="tpe-f"><label for="tpe-hp">Destination</label><select id="tpe-hp"></select></div>
<div class="tpe-f"><label for="tpe-hin">Check-in</label><input id="tpe-hin" type="date"></div>
<div class="tpe-f"><label for="tpe-hn">Nights</label><select id="tpe-hn"></select></div>
<div class="tpe-f"><label for="tpe-hr">Rooms</label><select id="tpe-hr"></select></div>
<div class="tpe-f"><label for="tpe-ht">Hotel class</label><select id="tpe-ht"><option value="standard">Standard</option><option value="deluxe" selected>Deluxe (3★)</option><option value="super">Super Deluxe</option><option value="luxury">Luxury</option></select></div>
<button type="button" class="tpe-go" id="tpe-hgo">Check price</button>
</div></div>
</div>
</section>"""

JS = r"""<script id="tpe-data" type="application/json">__DATA__</script>
<script id="tp-engine-js">
/* Suzu booking-engine hero v1 — opens /plan-your-trip/ inside an on-page overlay */
(function(){'use strict';
var D=document,W=window,E=D.getElementById('tp-engine');if(!E)return;
var X;try{X=JSON.parse(D.getElementById('tpe-data').textContent)}catch(e){return}
function $(s,r){return (r||D).querySelector(s)}function $$(s,r){return [].slice.call((r||D).querySelectorAll(s))}
function esc(x){return String(x==null?'':x).replace(/[&<>"']/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
function pad(n){return(n<10?'0':'')+n}function iso(d){return d.getFullYear()+'-'+pad(d.getMonth()+1)+'-'+pad(d.getDate())}
var P={};X.p.forEach(function(p){P[p[0]]={id:p[0],n:p[1],hi:p[2],k:p[3],r:p[4]}});
var REG={himachal:'Himachal',pilgrim:'Mata darshan',kashmir:'Kashmir',ladakh:'Ladakh',uttarakhand:'Uttarakhand',hub:'City',punjab:'Punjab'};
var KEYS={mata:'mata devi shakti peeth darshan naina chintpurni jwala kangra chamunda vaishno navratri माता देवी',pilgrim:'yatra char dham kedarnath badrinath gangotri pilgrimage golden temple तीर्थ धाम',honeymoon:'honeymoon couple हनीमून',kashmir:'kashmir srinagar gulmarg pahalgam',ladakh:'ladakh leh pangong nubra',himachal:'himachal shimla manali spiti kinnaur dharamshala हिमाचल',uttarakhand:'uttarakhand rishikesh mussoorie nainital corbett'};
function ev(n,p){try{if(typeof gtag==='function')gtag('event',n,p||{})}catch(e){}}
var today=new Date();today.setHours(0,0,0,0);var d21=new Date(today.getTime()+21*864e5);
function opts(sel,ids,val){sel.innerHTML=ids.map(function(id){return '<option value="'+id+'"'+(id===val?' selected':'')+'>'+esc(P[id].n)+'</option>'}).join('')}
function groupOpts(sel,val,filter){var g={},order=['City','Himachal','Mata darshan','Kashmir','Ladakh','Uttarakhand','Punjab'];X.p.forEach(function(p){if(filter&&!filter(P[p[0]]))return;var k=p[3]==='hub'?'City':(REG[p[4]]||'Other');(g[k]=g[k]||[]).push(p[0])});
 sel.innerHTML=order.filter(function(k){return g[k]}).map(function(k){return '<optgroup label="'+k+'">'+g[k].map(function(id){return '<option value="'+id+'"'+(id===val?' selected':'')+'>'+esc(P[id].n)+'</option>'}).join('')+'</optgroup>'}).join('')}
/* fields */
opts($('#tpe-from'),X.f,'chandigarh');
$('#tpe-date').value=iso(d21);$('#tpe-date').min=iso(today);$('#tpe-hin').value=iso(d21);$('#tpe-hin').min=iso(today);
var WD=['Sun','Mon','Tue','Wed','Thu','Fri','Sat'];function dlab(){var v=$('#tpe-date').value.split('-');$('#tpe-date-s').textContent=v.length===3?WD[new Date(+v[0],+v[1]-1,+v[2]).getDay()]:''}dlab();$('#tpe-date').addEventListener('change',dlab);
$('#tpe-pax').innerHTML=[1,2,3,4,5,6,7,8,10,12,15,20].map(function(n){return '<option value="'+n+'"'+(n===2?' selected':'')+'>'+n+' Adult'+(n>1?'s':'')+'</option>'}).join('');
groupOpts($('#tpe-cf'),'delhi');groupOpts($('#tpe-ct'),'manali');
$('#tpe-cv').innerHTML=X.v.map(function(v){return '<option value="'+v[0]+'">'+esc(v[1])+' · '+v[2]+' seats</option>'}).join('');
groupOpts($('#tpe-hp'),'manali',function(p){return p.k!=='hub'||p.id==='amritsar'||p.id==='chandigarh'||p.id==='delhi'});
$('#tpe-hn').innerHTML=[1,2,3,4,5,6,7].map(function(n){return '<option value="'+n+'"'+(n===2?' selected':'')+'>'+n+' night'+(n>1?'s':'')+'</option>'}).join('');
$('#tpe-hr').innerHTML=[1,2,3,4,5,6,8,10].map(function(n){return '<option value="'+n+'">'+n+' room'+(n>1?'s':'')+'</option>'}).join('');
/* tabs */
var tabs=$$('.tpe-tabs [role=tab]',E);
function sel(t){tabs.forEach(function(x){var on=x===t;x.setAttribute('aria-selected',on);x.tabIndex=on?0:-1;$('#'+x.getAttribute('aria-controls')).hidden=!on});ev('trip_planner',{step:'home_tab',tab:t.id})}
tabs.forEach(function(t,i){t.addEventListener('click',function(){sel(t)});t.addEventListener('keydown',function(e){if(e.key==='ArrowRight'||e.key==='ArrowLeft'){var n=tabs[(i+(e.key==='ArrowRight'?1:tabs.length-1))%tabs.length];sel(n);n.focus()}})});
/* ideas */
var CAT={himachal:'🏔',mata:'🛕',pilgrim:'🙏',honeymoon:'💑',kashmir:'🌷',ladakh:'🏍',uttarakhand:'🌊'};
var POP=['shimla-manali','nau-devi','char-dham','kashmir-classic','spiti-circuit','vaishno-devi','dharamshala-dalhousie','ladakh-fly'];
var TP={};X.t.forEach(function(t){TP[t[0]]=t});
$('#tpe-quick').insertAdjacentHTML('beforeend',POP.filter(function(id){return TP[id]}).map(function(id){var t=TP[id];return '<button type="button" class="tpe-chip" data-tpl="'+id+'">'+(CAT[t[2]]||'')+' '+esc(t[1].replace(' (summer)','').replace(' (fly-in)',''))+'</button>'}).join(''));
$('#tpe-yatra-list').innerHTML=X.t.filter(function(t){return t[2]==='mata'||t[2]==='pilgrim'}).map(function(t){return '<button type="button" class="tpe-chip" data-tpl="'+t[0]+'">'+(CAT[t[2]]||'')+' '+esc(t[1])+' <small style="color:#5b6b62;font-weight:600">· '+t[3]+' days</small></button>'}).join('');
/* search */
var inp=$('#tpe-to'),box=$('#tpe-dd'),items=[],act=-1,chosen=null;
function search(q){q=q.trim().toLowerCase();var r=[];
 X.t.forEach(function(t){var hay=(t[1]+' '+(KEYS[t[2]]||'')).toLowerCase();var sc=!q?1:(t[1].toLowerCase().indexOf(q)>-1?3:hay.indexOf(q)>-1?2:0);if(sc)r.push({k:'t',t:t,sc:sc+.5})});
 X.p.forEach(function(p){if(!q&&p[3]==='hub')return;var n=p[1].toLowerCase(),hay=(n+' '+p[2]+' '+(REG[p[4]]||'')).toLowerCase();var sc=!q?.5:(n.indexOf(q)===0?4:n.indexOf(q)>-1||p[2].indexOf(q)>-1?3:hay.indexOf(q)>-1?1:0);if(sc)r.push({k:'p',p:p,sc:sc})});
 r.sort(function(a,b){return b.sc-a.sc});return r.slice(0,q?10:9)}
function render(){items=search(inp.value);act=-1;if(!items.length){box.innerHTML='<div class="hd">No match — try another place</div>';box.hidden=false;return}
 var h='',lk='';items.forEach(function(it,i){if(it.k!==lk){h+='<div class="hd">'+(it.k==='t'?'Ready trip ideas':'Places')+'</div>';lk=it.k}
  if(it.k==='t')h+='<button type="button" role="option" data-i="'+i+'"><span style="font-size:18px">'+(CAT[it.t[2]]||'🗺️')+'</span><span><b>'+esc(it.t[1])+'</b><small>'+it.t[3]+' days · from '+esc(P[it.t[4]].n)+'</small></span></button>';
  else h+='<button type="button" role="option" data-i="'+i+'"><span style="font-size:18px">'+(it.p[3]==='temple'?'🛕':it.p[3]==='hub'?'🏙️':'⛰️')+'</span><span><b>'+esc(it.p[1])+' <span style="font-weight:400;color:#5b6b62">'+esc(it.p[2])+'</span></b><small>'+esc(REG[it.p[4]]||'')+'</small></span></button>'});
 box.innerHTML=h;box.hidden=false;inp.setAttribute('aria-expanded','true')}
function pick(it){chosen=it;box.hidden=true;inp.setAttribute('aria-expanded','false');inp.value=it.k==='t'?it.t[1]:it.p[1];$('#tpe-to-s').textContent=it.k==='t'?'Ready idea · fully editable':(REG[it.p[4]]||'');plan()}
inp.addEventListener('focus',render);inp.addEventListener('input',function(){chosen=null;render()});
inp.addEventListener('keydown',function(e){var bs=$$('button[data-i]',box);if(e.key==='ArrowDown'||e.key==='ArrowUp'){e.preventDefault();act=Math.max(0,Math.min(bs.length-1,act+(e.key==='ArrowDown'?1:-1)));bs.forEach(function(b,i){b.classList.toggle('on',i===act)})}else if(e.key==='Enter'){e.preventDefault();var it=items[act>=0?act:0];if(it)pick(it)}else if(e.key==='Escape'){box.hidden=true}});
box.addEventListener('click',function(e){var b=e.target.closest('button[data-i]');if(b)pick(items[+b.dataset.i])});
D.addEventListener('click',function(e){if(!box.contains(e.target)&&e.target!==inp){box.hidden=true;inp.setAttribute('aria-expanded','false')}});
/* open planner */
function base(){return {embed:1,from:$('#tpe-from').value,date:$('#tpe-date').value,ad:$('#tpe-pax').value}}
function plan(){var q=base(),it=chosen;if(!it&&inp.value.trim()){it=search(inp.value)[0]}if(!it){q.tpl='shimla-manali'}else if(it.k==='t'){q.tpl=it.t[0]}else{q.place=it.p[0]}open(q)}
$('#tpe-go').addEventListener('click',plan);
E.addEventListener('click',function(e){var b=e.target.closest('[data-tpl]');if(b){var q=base();q.tpl=b.dataset.tpl;open(q)}});
$('#tpe-cgo').addEventListener('click',function(){open({embed:1,tab:'cab',cf:$('#tpe-cf').value,ct:$('#tpe-ct').value,ctype:$('#tpe-ctype').value,cv:$('#tpe-cv').value})});
$('#tpe-hgo').addEventListener('click',function(){open({embed:1,tab:'hotel',hp:$('#tpe-hp').value,hin:$('#tpe-hin').value,hn:$('#tpe-hn').value,hr:$('#tpe-hr').value,ht:$('#tpe-ht').value})});
var ov=null,ifr=null,lastFocus=null,ld=null;
function open(q){var qs=Object.keys(q).map(function(k){return k+'='+encodeURIComponent(q[k])}).join('&');lastFocus=D.activeElement;
 if(!ov){ov=D.createElement('div');ov.id='tp-ov';ov.setAttribute('role','dialog');ov.setAttribute('aria-modal','true');ov.setAttribute('aria-label','Trip planner');ov.innerHTML='<div class="ld"><div><i></i>Building your trip…</div></div>';ld=ov.firstChild;ifr=D.createElement('iframe');ifr.title='Suzu trip planner';ifr.setAttribute('allow','clipboard-write; web-share');ifr.addEventListener('load',function(){ld.hidden=true;try{ifr.contentWindow.focus()}catch(e){}});ifr.src='/plan-your-trip/?'+qs;ov.appendChild(ifr);D.body.appendChild(ov)}
 else{try{ifr.contentWindow.location.replace('/plan-your-trip/?'+qs)}catch(e){ifr.src='/plan-your-trip/?'+qs}}
 ld.hidden=false;ov.hidden=false;D.documentElement.classList.add('tp-ov-open','nz-open');
 try{history.pushState({tpov:1},'',location.pathname+location.search+'#plan-trip-now')}catch(e){}
 ev('trip_planner',{step:'home_open',q:q.tpl||q.place||q.tab||''})}
function close(back){if(!ov||ov.hidden)return;ov.hidden=true;D.documentElement.classList.remove('tp-ov-open','nz-open');if(back&&history.state&&history.state.tpov){try{history.back()}catch(e){}}if(lastFocus&&lastFocus.focus)lastFocus.focus()}
W.addEventListener('message',function(e){if(e.origin===location.origin&&e.data&&e.data.type==='tp-close')close(true)});
W.addEventListener('popstate',function(){if(ov&&!ov.hidden)close(false)});
D.addEventListener('keydown',function(e){if(e.key==='Escape'&&ov&&!ov.hidden)close(true)});
var pf=false;E.addEventListener('pointerenter',pre,{once:true});E.addEventListener('focusin',pre,{once:true});
function pre(){if(pf)return;pf=true;var l=D.createElement('link');l.rel='prefetch';l.href='/plan-your-trip/';D.head.appendChild(l)}
W.SuzuEngine={open:open,close:function(){close(true)}};
/* background slideshow — light: loads extra photos only after the page has loaded, never on Save-Data / reduced motion */
var bg=$('.tpx-bg'),cap=$('.tpx-cap');if(!bg)return;
var c=navigator.connection||{},lite=!!c.saveData||/^(slow-2g|2g|3g)$/.test(c.effectiveType||'')||matchMedia('(prefers-reduced-motion: reduce)').matches;
var phone=matchMedia('(max-width:700px)').matches,slides=[{el:$('img',bg),cap:cap?cap.getAttribute('data-cap'):'',tpl:cap?cap.getAttribute('data-tpl'):''}],idx=0,timer=0,vis=true;
if(cap)cap.addEventListener('click',function(){var q=base();q.tpl=slides[idx].tpl||'shimla-manali';open(q)});
function setCap(s){if(!cap)return;cap.style.opacity=0;setTimeout(function(){cap.innerHTML='📍 '+esc(s.cap)+' · <u>Plan this trip →</u>';cap.style.opacity=1},400)}
function next(){if(!vis||D.hidden)return;var a=slides[idx];idx=(idx+1)%slides.length;var b=slides[idx];if(!b.el.complete){idx=(idx-1+slides.length)%slides.length;return}a.el.classList.remove('on');void b.el.offsetWidth;b.el.classList.add('on');setCap(b)}
function build(){X.si.forEach(function(u,i){var im=D.createElement('img');im.alt='';im.decoding='async';im.loading='lazy';im.src=phone?u[1]:u[0];bg.appendChild(im);slides.push({el:im,cap:X.s[i][0],tpl:X.s[i][1]})});timer=setInterval(next,7000)}
if(!lite){var go=function(){setTimeout(build,2500)};if(D.readyState==='complete')go();else W.addEventListener('load',go)}
if('IntersectionObserver' in W)new IntersectionObserver(function(es){vis=es[0].isIntersecting}).observe(bg);
})();
</script>"""


def snippet_parts():
    data = json.dumps(DATA, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    s0 = SLIDES[0]
    bg = ('<div class="tpx-bg" aria-hidden="true"><picture><source media="(max-width:700px)" srcset="%s">'
          '<img class="on" src="%s" alt="" fetchpriority="high" decoding="async" width="1024" height="466"></picture></div>'
          '<div class="tpx-snow" aria-hidden="true"></div>'
          '<button type="button" class="tpx-cap" data-cap="%s" data-tpl="%s">📍 %s · <u>Plan this trip →</u></button>') % (s0[1], s0[0], s0[2], s0[3], s0[2])
    preload = ('<link rel="preload" as="image" href="%s" media="(max-width:700px)" fetchpriority="high">'
               '<link rel="preload" as="image" href="%s" media="(min-width:701px)" fetchpriority="high">') % (s0[1], s0[0])
    return CSS, bg, SECTION, JS.replace('__DATA__', data), preload


def apply(src, dst):
    h = open(src, encoding='utf-8').read()
    CSSb, BG, SEC, JSb, PRE = snippet_parts()
    if 'id="tp-engine"' in h:
        raise SystemExit('tp-engine already present — edit in place instead')
    def cut(pattern, repl, flags=re.S, count=1):
        nonlocal h
        n = len(re.findall(pattern, h, flags))
        assert n == count, (pattern[:60], n)
        h = re.sub(pattern, lambda m: repl, h, flags=flags)
    # head: film poster preloads -> slide 1 preloads
    cut(r'<!--nz-perf--><link rel="preload" as="image" href="suzu-film2-9x16\.jpg\?v=1"[^>]*><link rel="preload" as="image" href="suzu-film2-16x9\.jpg\?v=1"[^>]*><!--/nz-perf-->', '<!--nz-perf-->' + PRE + '<!--/nz-perf-->')
    cut(r'<link rel="preload" as="image" href="suzu-film2-16x9\.jpg\?v=1" media="\(min-aspect-ratio: 4/5\)" fetchpriority="high"><link rel="preload" as="image" href="suzu-film2-9x16\.jpg\?v=1" media="\(max-aspect-ratio: 4/5\)" fetchpriority="high">', '')
    # hero
    cut(r'<section class="nz nz-hero" id="nz-hero"', CSSb + '\n<section class="nz nz-hero tpx" id="nz-hero"')
    cut(r'<div class="nz-film-wrap">.*?</div><script id="nz-film-boot">.*?</script>', BG)
    cut(r'\n<div class="nz-grain" aria-hidden="true"></div>', '')
    cut(r'\n<button class="nz-pause" type="button".*?</button>', '')
    cut(r'<button class="nz-filmbtn" id="nz-filmbtn" type="button">.*?</button>', '')
    cut(r'\n<svg class="nz-cal" role="img" aria-label="Himachal" viewBox="0 0 3100 1100"></svg>', '')
    cut(r'\n<div class="nz-cap" aria-live="polite"></div>', '')
    cut(r'\n<div class="nz-rail" role="group" aria-label="Destinations in the film">.*?</div></div>\n<svg class="nz-ridges"', '\n' + SEC + '</div>\n<svg class="nz-ridges"')
    # JS: insert after the hero section
    i = h.find('id="nz-hero"'); e = h.find('</section>', i) + len('</section>')
    h = h[:e] + '\n' + JSb + h[e:]
    # nature JS: hero() only drove the film
    cut(r"var H=\$\('#nz-hero'\); if\(!H\)return;", "var H=$('#nz-hero'); if(!H||!$('.nz-film',H))return; /* film replaced by #tp-engine (15 Oct 2026) */")
    assert h.count('<h1') == 1
    open(dst, 'w', encoding='utf-8').write(h)
    b = h.encode('utf-8')
    print(dst, len(b), hashlib.sha256(b).hexdigest()[:16])


if __name__ == '__main__':
    apply(sys.argv[1], sys.argv[2])
