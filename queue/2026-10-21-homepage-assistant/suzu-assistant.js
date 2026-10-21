/*! Suzu Assistant v1.1 — 20 Oct 2026 (v1 13 Oct) — suzutravels.com
 * Floating "Hi, I'm Suzu" trip helper: speak or type a trip -> 3 matching packages -> name + WhatsApp -> lead.
 * Rule-based (no paid AI yet). Speech-to-text = the browser's own service. Leads go to the same WordPress
 * handler as the homepage planner (action suzu_submit_landing_form) with source tag "Suzu Assistant".
 * Owner lane: this file only. index.html carries just the loader <script id="nz-sa-loader">.
 */
(function () {
  'use strict';
  if (window.__suzuSA) return; window.__suzuSA = 1;
  var D = document, W = window, VER = '1.1';
  var WA = '917087488961', PHONE = '+91 70874 88961';
  var SR = W.SpeechRecognition || W.webkitSpeechRecognition;

  /* ---------- data from the homepage (optional) ---------- */
  var TRIPS = [];
  try { var nz = D.getElementById('nz-data'); if (nz) TRIPS = (JSON.parse(nz.textContent).trips || []); } catch (e) {}

  /* ---------- language ---------- */
  var lang = 'hi';
  try { var L0 = localStorage.getItem('suzuSaLang'); if (L0 === 'en' || L0 === 'hi') lang = L0; else if (!/^hi|^mr|^pa/i.test(navigator.language || '')) lang = 'en'; } catch (e) {}
  function T(hi, en) { return lang === 'hi' ? hi : en; }

  /* ---------- styles ---------- */
  var css = `
#sz-sa,#sz-sa *{box-sizing:border-box}
#sz-sa{--e:var(--nz-emerald,#1f7a45);--f:var(--nz-forest,#123d26);--g:var(--nz-gold,#c9962b);--m:var(--nz-mint,#e9f5ee);--l:var(--nz-line,#d9e6dd);--ink:#10261a;--mut:#5b6b62;font:15px/1.45 var(--nz-body,'Plus Jakarta Sans',system-ui,sans-serif);color:var(--ink)}
#sz-sa .dv{font-family:var(--nz-deva,'Tiro Devanagari Hindi',serif)}
.sa-launch{position:fixed;left:18px;bottom:calc(78px + env(safe-area-inset-bottom,0px));z-index:99990;display:flex;align-items:center;gap:10px;padding:6px 18px 6px 6px;min-height:60px;border:0;border-radius:999px;background:linear-gradient(135deg,#fff 0%,#f3faf6 100%);color:var(--f);box-shadow:0 12px 30px -10px rgba(16,61,38,.45),0 0 0 1.5px rgba(31,122,69,.18);cursor:pointer;transition:transform .25s ease,opacity .25s ease;font:inherit;text-align:left}
.sa-launch:hover{transform:translateY(-2px)}
.sa-launch:focus-visible,.sa-panel button:focus-visible,.sa-panel a:focus-visible,.sa-panel input:focus-visible{outline:3px solid var(--g);outline-offset:2px}
.sa-av{position:relative;flex:0 0 auto;width:48px;height:48px;border-radius:50%;display:block}
.sa-av svg{width:100%;height:100%;display:block;border-radius:50%}
.sa-dot{position:absolute;right:-1px;bottom:-1px;width:18px;height:18px;border-radius:50%;background:var(--g);border:2px solid #fff;display:grid;place-items:center}
.sa-dot svg{width:10px;height:10px}
.sa-ring{position:absolute;inset:-4px;border-radius:50%;border:2px solid rgba(31,122,69,.45);animation:saPulse 2.4s ease-out infinite}
@keyframes saPulse{0%{opacity:.9;transform:scale(.92)}100%{opacity:0;transform:scale(1.35)}}
.sa-lt{display:grid;line-height:1.15}.sa-lt b{font-size:15px;font-weight:800;letter-spacing:-.01em}.sa-lt small{font-size:12.5px;color:var(--mut);font-weight:600}
.sa-launch.mini{padding-right:6px}.sa-launch.mini .sa-lt{display:none}
.sa-launch.hide{opacity:0;pointer-events:none;transform:translateY(20px)}
.sa-bub{position:fixed;left:18px;bottom:calc(150px + env(safe-area-inset-bottom,0px));z-index:99990;max-width:290px;padding:14px 38px 14px 16px;border-radius:18px 18px 18px 6px;background:#fff;box-shadow:0 18px 40px -14px rgba(16,61,38,.45),0 0 0 1px var(--l);font-size:14.5px;cursor:pointer;opacity:0;transform:translateY(10px) scale(.96);transform-origin:left bottom;transition:opacity .3s ease,transform .3s ease;pointer-events:none}
.sa-bub.on{opacity:1;transform:none;pointer-events:auto}
.sa-bub b{display:block;font-size:15.5px;margin-bottom:2px}
.sa-bub .x{position:absolute;top:4px;right:4px;width:36px;height:36px;border:0;background:none;color:var(--mut);font-size:20px;cursor:pointer;border-radius:50%}
.sa-panel{position:fixed;left:18px;bottom:calc(78px + env(safe-area-inset-bottom,0px));z-index:2147483000;width:392px;height:min(640px,calc(100vh - 150px));display:flex;flex-direction:column;background:#fbfdfb;border-radius:24px;box-shadow:0 30px 70px -20px rgba(10,40,25,.55),0 0 0 1px var(--l);overflow:hidden;opacity:0;transform:translateY(16px) scale(.98);transform-origin:left bottom;transition:opacity .25s ease,transform .25s ease;pointer-events:none}
.sa-panel.on{opacity:1;transform:none;pointer-events:auto}
.sa-hd{display:flex;align-items:center;gap:10px;padding:12px 10px 12px 14px;background:linear-gradient(120deg,var(--f) 0%,var(--e) 100%);color:#fff}
.sa-hd .sa-av{width:42px;height:42px}
.sa-ht{flex:1;min-width:0;line-height:1.2}.sa-ht b{display:block;font-size:16px}.sa-ht small{font-size:12.5px;opacity:.9}
.sa-ht small i{display:inline-block;width:8px;height:8px;border-radius:50%;background:#6ee7a0;margin-right:5px;vertical-align:1px;font-style:normal}
.sa-lg{display:flex;padding:3px;background:rgba(255,255,255,.16);border-radius:999px}
.sa-lg button{min-width:44px;min-height:40px;padding:0 10px;border:0;border-radius:999px;background:transparent;color:#fff;font:700 13px/1 var(--nz-body,system-ui);cursor:pointer}
.sa-lg button[aria-pressed=true]{background:#fff;color:var(--f)}
.sa-x{width:44px;height:44px;border:0;border-radius:50%;background:transparent;color:#fff;font-size:24px;cursor:pointer}
.sa-log{flex:1;overflow-y:auto;padding:16px 14px 8px;display:flex;flex-direction:column;gap:10px;overscroll-behavior:contain;scroll-behavior:smooth}
.sa-log>*{flex-shrink:0}
.sa-m{max-width:88%;padding:10px 13px;border-radius:16px;font-size:14.5px;animation:saIn .25s ease both;word-wrap:break-word}
@keyframes saIn{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}
.sa-m.b{align-self:flex-start;background:#fff;border:1px solid var(--l);border-bottom-left-radius:6px}
.sa-m.u{align-self:flex-end;background:var(--e);color:#fff;border-bottom-right-radius:6px}
.sa-m a{color:var(--e);font-weight:700}
.sa-m.u a{color:#fff}
.sa-tags{display:flex;flex-wrap:wrap;gap:6px;margin-top:6px}.sa-tags span{padding:2px 10px;border-radius:999px;background:var(--m);color:var(--f);font-weight:700;font-size:12.5px}
.sa-typing{align-self:flex-start;display:flex;gap:4px;padding:12px 14px;background:#fff;border:1px solid var(--l);border-radius:16px}
.sa-typing i{width:7px;height:7px;border-radius:50%;background:#9bb5a6;animation:saDot 1s infinite}
.sa-typing i:nth-child(2){animation-delay:.15s}.sa-typing i:nth-child(3){animation-delay:.3s}
@keyframes saDot{0%,60%,100%{opacity:.35;transform:none}30%{opacity:1;transform:translateY(-3px)}}
.sa-chips{display:flex;flex-wrap:wrap;gap:7px;align-self:flex-start;max-width:100%}
.sa-chips button,.sa-chips a{min-height:40px;padding:0 14px;border:1.5px solid var(--l);border-radius:999px;background:#fff;color:var(--f);font:700 13.5px/1 var(--nz-body,system-ui);cursor:pointer;display:inline-flex;align-items:center;gap:6px;text-decoration:none}
.sa-chips button:hover,.sa-chips a:hover{border-color:var(--e);background:var(--m)}
.sa-chips .p{background:var(--e);border-color:var(--e);color:#fff}
.sa-chips .wa{background:#1fa855;border-color:#1fa855;color:#fff}
.sa-cards{display:flex;gap:10px;overflow-x:auto;padding:2px 2px 6px;align-self:stretch;scroll-snap-type:x mandatory}
.sa-card{flex:0 0 230px;scroll-snap-align:start;background:#fff;border:1px solid var(--l);border-radius:16px;overflow:hidden;display:flex;flex-direction:column}
.sa-card img{width:100%;height:110px;object-fit:cover;display:block;background:var(--m)}
.sa-card .cb{padding:10px 12px 12px;display:flex;flex-direction:column;gap:4px;flex:1}
.sa-card b{font-size:14px;line-height:1.25}
.sa-card .mt{font-size:12.5px;color:var(--mut)}
.sa-card .pr{font-weight:800;color:var(--f);font-size:14px}.sa-card .pr small{font-weight:600;color:var(--mut)}
.sa-card .ab{margin-top:auto;display:flex;gap:6px;padding-top:6px}
.sa-card .ab button{flex:1;min-height:40px;border-radius:12px;border:1.5px solid var(--e);background:#fff;color:var(--e);font:700 13px/1 var(--nz-body,system-ui);cursor:pointer}
.sa-card .ab button.p{background:var(--e);color:#fff}
.sa-form{align-self:stretch;background:#fff;border:1px solid var(--l);border-radius:16px;padding:12px;display:grid;gap:8px}
.sa-form label{font-size:12.5px;font-weight:700;color:var(--mut)}
.sa-form input{width:100%;min-height:46px;padding:0 12px;border:1.5px solid var(--l);border-radius:12px;font:inherit;background:#fbfdfb}
.sa-form input:focus{border-color:var(--e);outline:none}
.sa-form .er{color:#b42318;font-size:13px}
.sa-form button{min-height:48px;border:0;border-radius:12px;background:var(--e);color:#fff;font:800 15px/1 var(--nz-body,system-ui);cursor:pointer}
.sa-form small{color:var(--mut);font-size:12px}
.sa-in{display:flex;align-items:center;gap:8px;padding:10px 10px 12px;border-top:1px solid var(--l);background:#fff}
.sa-in input{flex:1;min-width:0;min-height:48px;padding:0 14px;border:1.5px solid var(--l);border-radius:999px;font:inherit;background:#fbfdfb}
.sa-in input:focus{border-color:var(--e);outline:none}
.sa-mic,.sa-send{flex:0 0 auto;width:48px;height:48px;border:0;border-radius:50%;display:grid;place-items:center;cursor:pointer;position:relative}
.sa-mic{background:var(--m);color:var(--f)}
.sa-mic[aria-pressed=true]{background:#d9475b;color:#fff}
.sa-mic[aria-pressed=true]::after{content:"";position:absolute;inset:-5px;border-radius:50%;border:2px solid #d9475b;animation:saPulse 1.2s ease-out infinite}
.sa-send{background:var(--e);color:#fff}
.sa-mic svg,.sa-send svg{width:22px;height:22px}
.sa-ft{padding:0 14px 10px;background:#fff;font-size:11px;color:var(--mut);text-align:center}
.nz-open .sa-launch,.nz-open .sa-bub{display:none!important}
@media (max-width:768px){
 .sa-launch{left:12px;bottom:calc(86px + env(safe-area-inset-bottom,0px));padding-right:16px;min-height:56px}
 .sa-av{width:44px;height:44px}
 .sa-lt b{font-size:14px}.sa-lt small{font-size:12px}
 .sa-bub{left:12px;bottom:calc(152px + env(safe-area-inset-bottom,0px));max-width:calc(100vw - 110px)}
 .sa-panel{left:0;right:0;bottom:0;width:auto;height:min(88vh,calc(100dvh - 40px));border-radius:22px 22px 0 0}
 .sa-in{padding-bottom:calc(12px + env(safe-area-inset-bottom,0px))}
 /* site sets html{zoom:.9} on phones: 49 css px = 44 px on screen */
 #sz-sa .sa-chips button,#sz-sa .sa-chips a,#sz-sa .sa-card .ab button,#sz-sa .sa-lg button,#sz-sa .sa-form button{min-height:49px}
 #sz-sa .sa-x{width:49px;height:49px}
}
@media (prefers-reduced-motion:reduce){.sa-ring,.sa-mic[aria-pressed=true]::after{animation:none;display:none}.sa-m{animation:none}.sa-launch,.sa-panel,.sa-bub{transition:none}}
`;

  var AV = '<svg viewBox="0 0 64 64" aria-hidden="true"><defs><linearGradient id="saG" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2a9d63"/><stop offset="1" stop-color="#0f5a3a"/></linearGradient></defs><rect width="64" height="64" fill="url(#saG)"/><circle cx="45" cy="19" r="7" fill="#f3c969"/><path d="M-2 52 L20 26 L30 37 L40 24 L66 52 Z" fill="#cfe9dc"/><path d="M20 26 L14 33 L18 32 L21 35 L24 30 Z M40 24 L35 30 L39 29 L42 32 L45 29 Z" fill="#fff"/><path d="M-2 56 Q16 46 32 52 T66 50 V66 H-2Z" fill="#165c3a"/><circle cx="25" cy="46" r="1.6" fill="#10261a"/><circle cx="35" cy="46" r="1.6" fill="#10261a"/><path d="M26.5 50 Q30 53 33.5 50" stroke="#10261a" stroke-width="1.6" fill="none" stroke-linecap="round"/></svg>';
  var ICO = {
    mic: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/></svg>',
    send: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h13M13 6l6 6-6 6"/></svg>',
    spark: '<svg viewBox="0 0 24 24" fill="#fff" aria-hidden="true"><path d="M12 2l2.2 6.3L20 10l-5.8 1.7L12 18l-2.2-6.3L4 10l5.8-1.7z"/></svg>'
  };

  /* ---------- helpers ---------- */
  function el(tag, cls, html) { var e = D.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; }
  function esc(x) { return String(x == null ? '' : x).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function inr(n) { return '₹' + Number(n).toLocaleString('en-IN'); }
  function srcTag() { try { return localStorage.getItem('szl_src') || 'DR'; } catch (e) { return 'DR'; } }
  function ev(name, p) { try { if (typeof gtag === 'function') gtag('event', name, p || {}); } catch (e) {} }

  /* ---------- understanding (Hindi + English + Hinglish) ---------- */
  var MON = [['january', 'jan', 'जनवरी'], ['february', 'feb', 'फरवरी', 'फ़रवरी'], ['march', 'mar', 'मार्च'], ['april', 'apr', 'अप्रैल', 'अप्रेल'], ['may', 'मई'], ['june', 'jun', 'जून'], ['july', 'jul', 'जुलाई'], ['august', 'aug', 'अगस्त'], ['september', 'sept', 'sep', 'सितंबर', 'सितम्बर'], ['october', 'oct', 'अक्टूबर', 'अक्तूबर'], ['november', 'nov', 'नवंबर', 'नवम्बर'], ['december', 'dec', 'दिसंबर', 'दिसम्बर']];
  var MN = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
  var MNH = ['जनवरी', 'फ़रवरी', 'मार्च', 'अप्रैल', 'मई', 'जून', 'जुलाई', 'अगस्त', 'सितंबर', 'अक्टूबर', 'नवंबर', 'दिसंबर'];
  var NUM = { 'एक': 1, 'दो': 2, 'तीन': 3, 'चार': 4, 'पांच': 5, 'पाँच': 5, 'छह': 6, 'छः': 6, 'छे': 6, 'सात': 7, 'आठ': 8, 'नौ': 9, 'दस': 10, 'बारह': 12, 'पंद्रह': 15, 'बीस': 20, 'पच्चीस': 25, 'तीस': 30, 'चालीस': 40, 'पचास': 50,
    'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'twelve': 12, 'fifteen': 15, 'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50,
    'teen': 3, 'char': 4, 'paanch': 5, 'panch': 5, 'chhe': 6, 'saat': 7, 'aath': 8, 'das': 10, 'bees': 20, 'pachees': 25, 'tees': 30, 'chalis': 40 };
  var WHO = [['couple', /honeymoon|हनीमून|couple|कपल|wife|पत्नी|husband|पति|romantic|रोमांटिक/],
    ['family', /family|फैमिली|परिवार|parivar|bachch|बच्च|kids|children|parents|माता|मम्मी|पापा/],
    ['pilgrimage', /pilgrim|तीर्थ|mandir|मंदिर|temple|darshan|दर्शन|devi|देवी|dham|धाम|yatra|यात्रा|शक्तिपीठ|shakti|jyotirling|ज्योतिर्लिंग/],
    ['snow', /snow|बर्फ|\bbarf|snowfall|बर्फबारी|\bice\b/],
    ['friends', /friend|दोस्त|dost|adventure|एडवेंचर|trek|ट्रेक|rafting|राफ्टिंग|paragliding|पैराग्लाइडिंग|bike|बाइक|camping|कैंपिंग/],
    ['beach', /beach|बीच|समुद्र|\bsea\b|heritage|हेरिटेज|\bforts?\b|किला/]];
  var THEME = { couple: ['couple', 'honeymoon'], family: ['family'], pilgrimage: ['pilgrimage'], snow: ['snow'], friends: ['adventure', 'biking', 'offbeat'], beach: ['beach', 'heritage'] };
  var WHOL = { couple: ['कपल / हनीमून', 'Couple / honeymoon'], family: ['फैमिली', 'Family'], pilgrimage: ['तीर्थ यात्रा', 'Pilgrimage'], snow: ['बर्फ़ / स्नो', 'Snow'], friends: ['दोस्त / एडवेंचर', 'Friends / adventure'], beach: ['बीच / हेरिटेज', 'Beach & heritage'] };
  /* places -> region (+ word to match in trip title/route) */
  var PLACES = [
    [/himachal|हिमाचल/, 'himachal', ''], [/manali|मनाली|solang|सोलंग|rohtang|रोहतांग|\batal\b|sissu/, 'himachal', 'manali'], [/shimla|शिमला|kufri|कुफरी|kasauli|कसौली|\bchail\b|narkanda/, 'himachal', 'shimla'],
    [/dharamshala|धर्मशाला|mcleod|मैक्लोड/, 'himachal', 'dharamshala'], [/dalhousie|डलहौजी|डलहौज़ी|khajjiar|खज्जियार/, 'himachal', 'dalhousie'], [/spiti|स्पीति|kaza|काज़ा|chandratal/, 'himachal', 'spiti'],
    [/kinnaur|किन्नौर|sangla|सांगला|chitkul|छितकुल/, 'himachal', 'kinnaur'], [/kasol|कसोल|kullu|कुल्लू|\bbir\b|बीर|jibhi|tirthan/, 'himachal', 'manali'], [/amritsar|अमृतसर/, 'himachal', 'amritsar'],
    [/kashmir|कश्मीर|srinagar|श्रीनगर|gulmarg|गुलमर्ग|pahalgam|पहलगाम|sonmarg/, 'kashmir', ''], [/vaishno|वैष्णो/, 'kashmir', 'vaishno'], [/amarnath|अमरनाथ/, 'kashmir', 'amarnath'],
    [/ladakh|लद्दाख|\bleh\b|लेह|pangong|पैंगोंग|nubra/, 'ladakh', ''],
    [/uttarakhand|उत्तराखंड|nainital|नैनीताल|mussoorie|मसूरी|rishikesh|ऋषिकेश|haridwar|हरिद्वार|corbett|कॉर्बेट|bhimtal/, 'uttarakhand', ''], [/char ?dham|चारधाम|चार धाम|kedarnath|केदारनाथ|badrinath|बद्रीनाथ|do ?dham/, 'uttarakhand', 'dham'],
    [/rajasthan|राजस्थान|jaipur|जयपुर|udaipur|उदयपुर|jodhpur|जोधपुर|jaisalmer|जैसलमेर|mount abu|माउंट आबू/, 'rajasthan', ''],
    [/\bgoa\b|गोवा/, 'goa', ''], [/kerala|केरल|munnar|मुन्नार|alleppey|अलेप्पी|guruvayoor/, 'kerala', ''],
    [/varanasi|वाराणसी|kashi|काशी|banaras|बनारस|ayodhya|अयोध्या/, 'spiritual', 'varanasi']];
  var RNAME = { himachal: ['हिमाचल', 'Himachal'], kashmir: ['कश्मीर', 'Kashmir'], ladakh: ['लद्दाख', 'Ladakh'], uttarakhand: ['उत्तराखंड', 'Uttarakhand'], rajasthan: ['राजस्थान', 'Rajasthan'], goa: ['गोवा', 'Goa'], kerala: ['केरल', 'Kerala'], spiritual: ['तीर्थ (वाराणसी)', 'Spiritual India'] };

  function norm(t) { return ' ' + String(t || '').toLowerCase().replace(/[,.?!।]/g, ' ').replace(/[०-९]/g, function (d) { return '०१२३४५६७८९'.indexOf(d); }).replace(/\s+/g, ' ') + ' '; }
  function numIn(str) { var m = str.match(/(\d+(?:\.\d+)?)/); if (m) return parseFloat(m[1]); var best = 0; Object.keys(NUM).forEach(function (w) { if (str.indexOf(' ' + w + ' ') > -1 && w.length > (best ? best.l : 0)) best = { l: w.length, v: NUM[w] }; }); return best ? best.v : 0; }
  function parse(raw) {
    var t = norm(raw).replace(/ (may i|may be|maybe|i may|you may|we may|it may) /g, ' '), r = {};
    var nowM = new Date().getMonth() + 1;
    if (/next month|अगले महीने|agle mahine/.test(t)) r.month = nowM % 12 + 1;
    else if (/this month|इस महीने|is mahine/.test(t)) r.month = nowM;
    else MON.forEach(function (ws, i) { ws.forEach(function (w) { if (t.indexOf(' ' + w + ' ') > -1 || t.indexOf(' ' + w + 'में') > -1) r.month = i + 1; }); });
    if (/diwali|दिवाली|दीवाली/.test(t) && !r.month) r.month = 11;
    if (/new year|नए साल|नया साल|christmas|क्रिसमस/.test(t) && !r.month) r.month = 12;
    var b = 0, m;
    if ((m = t.match(/(?:₹|rs\.? |rupees? )?\s?(\d[\d ]*\d|\d)\s?(?:k\b|हज़ार|हजार|hazar|hazaar|thousand)/))) b = parseFloat(m[1].replace(/ /g, '')) * 1000;
    else if ((m = t.match(/(\d[\d,]{3,})\s?(?:₹|rs|rupees?|रुपये|रुपए)?/))) b = parseFloat(m[1].replace(/,/g, ''));
    else if ((m = t.match(/(\S+(?: \S+)?) (?:हज़ार|हजार|hazar|thousand)/))) { var n = numIn(' ' + m[1] + ' '); if (n) b = n * 1000; }
    if (/लाख|lakh/.test(t)) { var lm = t.match(/(\d+(?:\.\d+)?)\s?(?:लाख|lakh)/); b = (lm ? parseFloat(lm[1]) : 1) * 100000; }
    if (b >= 3000) r.bud = b;
    var d = 0, dm = t.match(/(\d+)\s?(?:-|to|से)?\s?(?:\d+\s?)?(day|days|din|दिन|night|nights|raat|रात|रातें)/);
    if (dm) { d = parseInt(dm[1], 10); if (/night|raat|रात/.test(dm[2])) d += 1; }
    else { var wm = t.match(/(\S+) (?:day|days|din|दिन|night|nights|रात)/); if (wm) { d = numIn(' ' + wm[1] + ' '); if (d && /night|रात/.test(t)) d += 1; } }
    if (!d && /weekend|वीकेंड/.test(t)) d = 3;
    if (!d && /(?:one|एक|ek|1) (?:week|हफ्ते|हफ़्ते|हफ्ता|hafte)|a week/.test(t)) d = 7;
    if (!d && /(?:two|दो|2) (?:weeks|हफ्ते|हफ़्ते)/.test(t)) d = 14;
    if (d && d < 40) r.days = d;
    for (var i = 0; i < WHO.length; i++) if (WHO[i][1].test(t)) { r.who = WHO[i][0]; break; }
    for (var j = 0; j < PLACES.length; j++) if (PLACES[j][0].test(t)) { r.region = PLACES[j][1]; if (PLACES[j][2]) r.place = PLACES[j][2]; break; }
    var pm = t.match(/(\d+)\s?(?:log|लोग|people|persons|adults|pax|members|सदस्य)/); if (pm) r.pax = parseInt(pm[1], 10);
    return r;
  }
  function intent(raw) {
    var t = norm(raw);
    if (/\b(hi|hello|hey|namaste|namaskar)\b|नमस्ते|नमस्कार|हेलो|हाय/.test(t) && t.length < 22) return 'hello';
    if (/human|real person|live agent|talk to (?:an? )?(?:agent|person)|insaan|इंसान|call me|call back|callback|कॉल|फ़ोन|फोन|phone|\bbaat\b|बात|\btalk|contact|संपर्क|your number|mobile number/.test(t)) return 'human';
    if (/payment|pay |advance|एडवांस|token|refund|रिफंड|cancel|कैंसल|रद्द|razorpay|upi|भुगतान|booking process|बुकिंग कैसे/.test(t)) return 'pay';
    if (/registered|registration|रजिस्टर्ड|trust|भरोसा|genuine|real company|fraud|certificate|license|लाइसेंस/.test(t)) return 'trust';
    if (/\bcabs?\b|taxi|टैक्सी|कैब|गाड़ी|gaadi|car rent|car hire|innova|इनोवा|tempo|टेम्पो|one ?way|\bdrop\b|pickup|pick up|airport transfer/.test(t) && !/package|पैकेज|\btour\b|honeymoon|हनीमून|\d+ ?(?:days?|din|दिन|nights?)/.test(t)) return 'cab';
    if (/price|cost|\brate\b|kitne|kitna|कितने|कितना|\bdaam\b|दाम|kharcha|खर्च|budget kya|कीमत|keemat/.test(t)) return 'price';
    if (/weather|मौसम|mausam|temperature|तापमान|road status|road open|रास्ता खुला/.test(t)) return 'weather';
    if (/snow ?fall|बर्फबारी|snow kab|बर्फ कब|snow radar|is there snow|snow abhi/.test(t)) return 'snownow';
    if (/thank|धन्यवाद|शुक्रिया|shukriya|ok bye|bye/.test(t)) return 'thanks';
    return '';
  }

  /* ---------- cab routes: live /cabs/ pages (page-sitemap.xml, verified 200 on 20 Oct 2026) ---------- */
  var CITY = [['delhi', /delhi|दिल्ली|dilli/], ['chandigarh', /chandigarh|चंडीगढ़|चण्डीगढ़|चंडीगढ/], ['shimla', /shimla|शिमला/], ['manali', /manali|मनाली/], ['amritsar', /amritsar|अमृतसर/], ['jammu', /jammu|जम्मू/], ['srinagar', /srinagar|श्रीनगर/], ['pathankot', /pathankot|पठानकोट/], ['dharamshala', /dharamshala|dharamsala|धर्मशाला/], ['nainital', /nainital|नैनीताल/], ['dehradun', /dehradun|देहरादून/], ['mussoorie', /mussoorie|मसूरी/], ['rishikesh', /rishikesh|ऋषिकेश/], ['haridwar', /haridwar|हरिद्वार/], ['kalka', /kalka|कालका/]];
  var CNAME = { delhi: ['दिल्ली', 'Delhi'], chandigarh: ['चंडीगढ़', 'Chandigarh'], shimla: ['शिमला', 'Shimla'], manali: ['मनाली', 'Manali'], amritsar: ['अमृतसर', 'Amritsar'], jammu: ['जम्मू', 'Jammu'], srinagar: ['श्रीनगर', 'Srinagar'], pathankot: ['पठानकोट', 'Pathankot'], dharamshala: ['धर्मशाला', 'Dharamshala'], nainital: ['नैनीताल', 'Nainital'], dehradun: ['देहरादून', 'Dehradun'], mussoorie: ['मसूरी', 'Mussoorie'], rishikesh: ['ऋषिकेश', 'Rishikesh'], haridwar: ['हरिद्वार', 'Haridwar'], kalka: ['कालका', 'Kalka'] };
  var CABR = ' jammu-srinagar pathankot-dharamshala delhi-amritsar shimla-manali delhi-manali delhi-jammu delhi-nainital dehradun-mussoorie delhi-mussoorie delhi-rishikesh delhi-haridwar chandigarh-manali delhi-chandigarh delhi-shimla delhi-dehradun kalka-shimla chandigarh-shimla ';
  var CABC = ' jammu rishikesh amritsar haridwar manali nainital srinagar dharamshala dehradun chandigarh shimla ';
  function cabMatch(raw) {
    var t = norm(raw), hits = [];
    CITY.forEach(function (c) { var m = c[1].exec(t); if (m) hits.push([m.index, c[0]]); });
    hits.sort(function (a, b) { return a[0] - b[0]; });
    var cs = hits.map(function (h) { return h[1]; }), from = cs[0], to = cs[1], r = { from: from || '', to: to || '' };
    /* "manali from delhi" / "दिल्ली से मनाली" both work: if the 2nd city is preceded by from/से-less wording, keep reading order */
    if (from && to && /\b(?:from|se)\b|से/.test(t)) { var fi = t.search(/\bfrom\b/); if (fi > -1 && hits[1][0] > fi && hits[0][0] < fi) { r.from = to; r.to = from; from = r.from; to = r.to; } }
    if (/tempo|टेम्पो|traveller|12 ?seater|17 ?seater/.test(t) && (from === 'chandigarh' || to === 'chandigarh')) r.url = '/cabs/tempo-traveller-chandigarh/';
    else if (/tempo|टेम्पो|traveller/.test(t)) r.url = '/cabs/tempo-traveller-hire-delhi/';
    else if (/airport|एयरपोर्ट/.test(t) && cs.indexOf('chandigarh') > -1) r.url = '/cabs/chandigarh-airport-taxi/';
    else if (from && to && CABR.indexOf(' ' + from + '-' + to + ' ') > -1) r.url = '/cabs/' + from + '-to-' + to + '-taxi/';
    else if (/innova|इनोवा|crysta/.test(t)) r.url = '/cabs/innova-crysta-on-rent/';
    else if (from === 'delhi' && !to) r.url = '/cabs/outstation-cab-delhi/';
    else if (from && CABC.indexOf(' ' + from + ' ') > -1) r.url = '/cabs/' + from + '-taxi-service/';
    else if (to && CABC.indexOf(' ' + to + ' ') > -1) r.url = '/cabs/' + to + '-taxi-service/';
    else if (from === 'delhi') r.url = '/cabs/outstation-cab-delhi/';
    else r.url = '/cabs/';
    return r;
  }

  /* ---------- trip matching ---------- */
  function score(tp, s) {
    var sc = 0;
    if (s.region) sc += tp.region === s.region ? 6 : -6;
    if (s.place) { var hay = (tp.title + ' ' + (tp.route || []).join(' ') + ' ' + tp.slug).toLowerCase(); if (hay.indexOf(s.place) > -1) sc += 4; }
    if (s.who) { var th = THEME[s.who] || []; if (th.some(function (x) { return (tp.themes || []).indexOf(x) > -1; })) sc += 3; }
    if (s.month && tp.months) sc += tp.months.indexOf(s.month) > -1 ? 2 : -3;
    if (s.days) sc -= Math.abs((tp.days || 0) - s.days) * 0.6;
    if (s.bud) { if (tp.price) sc += tp.price <= s.bud ? 2 : -3; else sc -= 0.5; }
    if (tp.price) sc += 0.3;
    return sc;
  }
  function best(s) { return TRIPS.map(function (tp) { return [score(tp, s), tp]; }).sort(function (a, b) { return b[0] - a[0]; }).slice(0, 3).map(function (x) { return x[1]; }); }

  /* ---------- state ---------- */
  var S = {}, shown = [], said = [], asked = {}, leadSent = false, engaged = false, autoHi = false, prev = [], cabReq = '';
  var root, log, input, micBtn, panel, launch, bub;

  /* ---------- UI build ---------- */
  function build() {
    var st = el('style'); st.id = 'sz-sa-css'; st.textContent = css; D.head.appendChild(st);
    root = el('div'); root.id = 'sz-sa'; D.body.appendChild(root);
    launch = el('button', 'sa-launch', '<span class="sa-av"><span class="sa-ring"></span>' + AV + '<span class="sa-dot">' + ICO.spark + '</span></span><span class="sa-lt"><b>' + T('नमस्ते, मैं Suzu हूँ', "Hi, I'm Suzu") + '</b><small>' + T('🎙 बोलकर trip ढूँढें', '🎙 Speak or chat your trip') + '</small></span>');
    launch.type = 'button'; launch.setAttribute('aria-haspopup', 'dialog'); launch.setAttribute('aria-label', T('Suzu से बात करें: बोलकर या लिखकर trip ढूँढें', 'Talk to Suzu: find a trip by voice or chat'));
    root.appendChild(launch);
    bub = el('div', 'sa-bub', '<b>' + T('नमस्ते! 👋 मैं Suzu हूँ', "Hi there! 👋 I'm Suzu") + '</b>' + T('बोलकर बताइए कहाँ घूमना है — मैं 30 सेकंड में 3 सही trips दिखा दूँगी।', 'Tell me where you want to go — I’ll show 3 trips that fit in 30 seconds.') + '<button class="x" type="button" aria-label="Close">×</button>');
    bub.setAttribute('role', 'status'); root.appendChild(bub);
    panel = el('div', 'sa-panel');
    panel.setAttribute('role', 'dialog'); panel.setAttribute('aria-label', 'Suzu trip assistant'); panel.setAttribute('aria-modal', 'false'); panel.hidden = true;
    panel.innerHTML = '<div class="sa-hd"><span class="sa-av">' + AV + '</span><div class="sa-ht"><b>Suzu · ' + T('ट्रिप असिस्टेंट', 'Trip assistant') + '</b><small><i></i>' + T('तुरंत जवाब', 'Replies instantly') + '</small></div>' +
      '<div class="sa-lg" role="group" aria-label="Language"><button type="button" data-l="hi" class="dv">हिं</button><button type="button" data-l="en">EN</button></div><button class="sa-x" type="button" aria-label="Close">×</button></div>' +
      '<div class="sa-log" aria-live="polite"></div>' +
      '<form class="sa-in" autocomplete="off"><input type="text" enterkeyhint="send" aria-label="Message" maxlength="300"><button type="button" class="sa-mic" aria-pressed="false" aria-label="Speak">' + ICO.mic + '</button><button type="submit" class="sa-send" aria-label="Send">' + ICO.send + '</button></form>' +
      '<div class="sa-ft">' + T('बोलने पर आपका ब्राउज़र आवाज़ को text में बदलता है · Suzu ऑडियो नहीं रखता', 'Your browser turns speech into text · Suzu never stores audio') + '</div>';
    root.appendChild(panel);
    log = panel.querySelector('.sa-log'); input = panel.querySelector('.sa-in input'); micBtn = panel.querySelector('.sa-mic');
    if (!SR) micBtn.hidden = true;
    setLangButtons(); input.placeholder = T('जैसे: दिसंबर में मनाली, 5 दिन, फैमिली', 'e.g. Manali in December, 5 days, family');

    launch.addEventListener('click', function () { open(); });
    bub.addEventListener('click', function (e) { if (e.target.closest('.x')) { hideBub(); try { sessionStorage.setItem('suzuSaBub', '1'); } catch (x) {} return; } open(); });
    panel.querySelector('.sa-x').addEventListener('click', close);
    panel.querySelector('.sa-lg').addEventListener('click', function (e) { var b = e.target.closest('[data-l]'); if (!b || b.dataset.l === lang) return; lang = b.dataset.l; try { localStorage.setItem('suzuSaLang', lang); } catch (x) {} setLangButtons(); input.placeholder = T('जैसे: दिसंबर में मनाली, 5 दिन, फैमिली', 'e.g. Manali in December, 5 days, family'); bot(T('ठीक है, अब मैं हिंदी में बात करूँगी।', 'Sure — I’ll reply in English now.')); });
    panel.querySelector('.sa-in').addEventListener('submit', function (e) { e.preventDefault(); var v = input.value.trim(); if (!v) return; input.value = ''; handle(v); });
    micBtn.addEventListener('click', function () { recBusy ? stopRec() : startRec(); });
    D.addEventListener('keydown', function (e) { if (e.key === 'Escape' && panel.classList.contains('on')) close(); });
    log.addEventListener('click', onLogClick);

    /* the legacy "Plan Your Trip" popup auto-opens ~7 s after scrolling; don't let it cover an active chat */
    var pop = D.getElementById('hero-search'), lastQuoteClick = 0;
    D.addEventListener('click', function (e) { if (e.target.closest && e.target.closest('a[href="#hero-search"],a.btn-call,a.td-book-btn')) lastQuoteClick = Date.now(); }, true);
    if (pop && 'MutationObserver' in W) new MutationObserver(function () {
      if (pop.classList.contains('active')) { hideBub(); if (panel.classList.contains('on') && engaged && Date.now() - lastQuoteClick > 800) pop.classList.remove('active'); }
    }).observe(pop, { attributes: true, attributeFilter: ['class'] });
    /* hide the launcher while the compare tray is up (same corner on phones) */
    var cmp = D.querySelector('.nz-cmpbar');
    if (cmp && 'MutationObserver' in W) { var chk = function () { launch.classList.toggle('hide', !cmp.classList.contains('off') && getComputedStyle(cmp).display !== 'none'); }; new MutationObserver(chk).observe(cmp, { attributes: true, attributeFilter: ['class', 'style'] }); }

    if (W.matchMedia('(max-width:768px)').matches) W.addEventListener('scroll', function () { launch.classList.toggle('mini', W.scrollY > 900); }, { passive: true });
    var seen = false; try { seen = sessionStorage.getItem('suzuSaBub') === '1'; } catch (e) {}
    if (!seen) setTimeout(function () { if (!panel.classList.contains('on') && !(pop && pop.classList.contains('active'))) { bub.classList.add('on'); try { sessionStorage.setItem('suzuSaBub', '1'); } catch (e) {} setTimeout(hideBub, 14000); } }, 4500);
  }
  function setLangButtons() { [].forEach.call(panel.querySelectorAll('.sa-lg [data-l]'), function (b) { b.setAttribute('aria-pressed', b.dataset.l === lang ? 'true' : 'false'); }); }
  function hideBub() { bub.classList.remove('on'); }

  var started = false;
  function open() {
    hideBub(); panel.hidden = false; launch.classList.add('hide');
    requestAnimationFrame(function () { panel.classList.add('on'); });
    if (!started) { started = true; greet(); }
    setTimeout(function () { if (W.matchMedia('(min-width:769px)').matches) input.focus(); }, 260);
    ev('suzu_assistant', { step: 'open' });
  }
  function close() { panel.classList.remove('on'); launch.classList.remove('hide'); stopRec(); setTimeout(function () { if (!panel.classList.contains('on')) panel.hidden = true; }, 260); launch.focus(); }

  /* ---------- messages ---------- */
  function scroll() { log.scrollTop = log.scrollHeight; }
  function add(node) { log.appendChild(node); scroll(); return node; }
  function me(text) { var m = el('div', 'sa-m u'); m.textContent = text; add(m); }
  var q = Promise.resolve();
  function bot(html, extra) {
    q = q.then(function () {
      return new Promise(function (res) {
        var ty = add(el('div', 'sa-typing', '<i></i><i></i><i></i>'));
        setTimeout(function () { ty.remove(); add(el('div', 'sa-m b', html)); if (extra) extra(); res(); }, Math.min(900, 280 + html.length * 4));
      });
    });
    return q;
  }
  function chips(list) {
    q = q.then(function () {
      var c = el('div', 'sa-chips');
      list.forEach(function (x) {
        var b;
        if (x.href) { b = el('a', x.cls || '', x.t); b.href = x.href; if (/^https?:/.test(x.href)) { b.target = '_blank'; b.rel = 'noopener'; } }
        else { b = el('button', x.cls || '', x.t); b.type = 'button'; b.dataset.say = x.say || ''; if (x.act) b.dataset.act = x.act; }
        c.appendChild(b);
      });
      add(c);
    });
  }

  function greet() {
    bot(T('<b>नमस्ते! मैं Suzu हूँ</b> — Suzu Travels की ट्रिप असिस्टेंट। 🙏<br>बताइए कहाँ घूमना है, कब और कितने दिन — <b>बोलकर 🎙 या लिखकर</b>।', '<b>Hi, I’m Suzu</b> — Suzu Travels’ trip assistant. 🙏<br>Tell me where, when and for how many days — <b>speak 🎙 or type</b>.'));
    bot(T('जैसे: <i>“दिसंबर में मनाली, 5 दिन, फैमिली, 25 हज़ार तक”</i>', 'For example: <i>“Kashmir in May, 6 days, couple, under 30k”</i>'));
    chips([
      { t: '🏔 ' + T('हिमाचल', 'Himachal'), say: T('हिमाचल ट्रिप', 'Himachal trip') },
      { t: '❄️ ' + T('स्नो ट्रिप', 'Snow trip'), say: T('बर्फ वाली ट्रिप', 'snow trip') },
      { t: '💑 ' + T('हनीमून', 'Honeymoon'), say: 'honeymoon' },
      { t: '🛕 ' + T('तीर्थ यात्रा', 'Pilgrimage'), say: T('तीर्थ यात्रा', 'pilgrimage yatra') },
      { t: '🚕 ' + T('सिर्फ़ टैक्सी', 'Cab only'), say: 'taxi' },
      { t: '📞 ' + T('टीम से बात', 'Talk to team'), say: T('टीम से बात करनी है', 'talk to a person') }
    ]);
  }

  function onLogClick(e) {
    var b = e.target.closest('button'); if (!b) return;
    if (b.dataset.trip) { var slug = b.dataset.trip; ev('suzu_assistant', { step: 'view_trip', slug: slug }); close(); setTimeout(function () { if (location.hash === '#trip-' + slug) location.hash = ''; location.hash = 'trip-' + slug; }, 280); return; }
    if (b.dataset.pick) { pickTrip(b.dataset.pick); return; }
    if (b.dataset.act === 'lead') { leadForm(); return; }
    if (b.dataset.act === 'more') { moreTrips(); return; }
    if (b.dataset.say) { handle(b.dataset.say, b.textContent.replace(/^[^\wऀ-ॿ]+/, '')); }
  }

  /* ---------- dialogue ---------- */
  function summaryTags() {
    var t = [];
    if (S.region) t.push(RNAME[S.region] ? T(RNAME[S.region][0], RNAME[S.region][1]) : S.region);
    if (S.who) t.push(T(WHOL[S.who][0], WHOL[S.who][1]));
    if (S.month) t.push(T(MNH[S.month - 1], MN[S.month - 1]));
    if (S.days) t.push(S.days + ' ' + T('दिन', 'days'));
    if (S.bud) t.push(T('बजट ', 'Budget ') + inr(S.bud) + T(' तक', ''));
    if (S.pax) t.push(S.pax + ' ' + T('लोग', 'people'));
    return t;
  }
  function handle(text, shownAs) {
    engaged = true; me(shownAs || text); said.push(text); if (said.length > 14) said.shift();
    if (/[ऀ-ॿ]/.test(text) && lang !== 'hi') { /* typed Hindi: answer in Hindi */ lang = 'hi'; autoHi = true; setLangButtons(); input.placeholder = T('जैसे: दिसंबर में मनाली, 5 दिन, फैमिली', 'e.g. Manali in December, 5 days, family'); }
    else if (autoHi && !/[ऀ-ॿ]/.test(text) && /\b(?:i|we|want|need|the|is|are|for|with|please|my|our|how|what|which|under|trip to)\b/i.test(text) && !/\b(?:hai|hain|karein|karna|kaise|chahiye|mein|kitne|kitna|kya|nahi|jana|batao|dikhao|wala|wali)\b/i.test(text)) { lang = 'en'; autoHi = false; setLangButtons(); input.placeholder = T('जैसे: दिसंबर में मनाली, 5 दिन, फैमिली', 'e.g. Manali in December, 5 days, family'); }
    var it = intent(text);
    if (it === 'cab') { ev('suzu_assistant', { step: 'message', intent: 'cab' }); cab(cabMatch(text)); return; }
    var p = parse(text), got = 0;
    /* a new destination starts a fresh trip: drop the old place, theme, days and budget (keep month, people, family/couple) */
    if (p.region && S.region && p.region !== S.region) {
      if (summaryTags().length) prev.push(summaryTags().join(', '));
      delete S.place; delete S.days; delete S.bud; if (S.who && S.who !== 'family' && S.who !== 'couple') delete S.who;
      asked.days = asked.who = 0;
    }
    if (p.region && !p.place && p.region === S.region && S.place) delete S.place;
    Object.keys(p).forEach(function (k) { S[k] = p[k]; got++; });
    ev('suzu_assistant', { step: 'message', intent: it || (got ? 'trip' : 'unknown') });
    if (it === 'hello' && !got) { bot(T('नमस्ते! 😊 बताइए कहाँ जाने का प्लान है?', 'Hello! 😊 Where would you like to go?')); return; }
    if (it === 'thanks' && !got) { bot(T('आपका धन्यवाद! 🙏 कभी भी पूछिए — या सीधे WhatsApp कीजिए ' + PHONE + '.', 'Thank you! 🙏 Ask me anytime — or WhatsApp us on ' + PHONE + '.')); return; }
    if (it === 'human') { human(); return; }
    if (it === 'pay') { pay(); return; }
    if (it === 'trust') { trust(); return; }
    if (it === 'price' && !got && !shown.length) { bot(T('हमारी trips पर जो <b>“शुरुआत ₹”</b> लिखा है वो published starting price है; पक्का rate तारीख़, होटल और गाड़ी से तय होता है। बताइए कहाँ और कितने दिन — मैं trips और उनके rate दिखाती हूँ।', 'The <b>“from ₹”</b> on our trips is the published starting price; the final rate depends on dates, hotel and vehicle. Tell me where and for how many days and I’ll show trips with their prices.')); chips([{ t: '🏔 ' + T('हिमाचल', 'Himachal'), say: 'Himachal' }, { t: T('कश्मीर', 'Kashmir'), say: 'Kashmir' }, { t: T('गोवा', 'Goa'), say: 'Goa' }, { t: T('Rate WhatsApp पर', 'Rate on WhatsApp'), act: 'lead', cls: 'p' }]); return; }
    if (it === 'price' && !got) { leadAsk(); return; }
    if (it === 'weather') { jump('himachal-weather', T('Himachal का live मौसम (Shimla, Manali, Lahaul, Dharamshala, Dalhousie) यहीं homepage पर है — मैं वहाँ ले चलती हूँ।', 'Live Himachal weather (Shimla, Manali, Lahaul, Dharamshala, Dalhousie) is right here on the page — taking you there.')); return; }
    if (it === 'snownow') { jump('nz-snow', T('अगले 7 दिन में कहाँ बर्फ़ गिर सकती है — हमारा <b>Snow Radar</b> देखिए, वहाँ WhatsApp snow alert भी ले सकते हैं।', 'See where fresh snow is forecast in the next 7 days on our <b>Snow Radar</b> — you can also get a WhatsApp snow alert there.')); return; }
    if (!got) { unknown(); return; }
    priceQ = it === 'price';
    tripReply();
  }
  var priceQ = false;
  function tripReply() {
    var tags = summaryTags();
    bot(T('समझ गई 👍', 'Got it 👍') + '<div class="sa-tags">' + tags.map(function (x) { return '<span>' + esc(x) + '</span>'; }).join('') + '</div>');
    if (!TRIPS.length) { leadAsk(); return; }
    var list = best(S).filter(function (tp) { return !S.region || tp.region === S.region; });
    if (!list.length) list = best(S);
    var same = shown.length && list.map(function (x) { return x.slug; }).join() === shown.slice(0, list.length).map(function (x) { return x.slug; }).join();
    shown = list;
    var extra = '';
    if (S.month && list[0] && list[0].months && list[0].months.indexOf(S.month) < 0) extra = T(' (इस महीने के लिए हमारी टीम सही रूट बताएगी)', ' (our team will suggest the right route for that month)');
    if (priceQ) extra += T(' — “शुरुआत ₹” published starting price है, पक्का rate तारीख़ और होटल से', ' — “from ₹” is the published starting price; the final rate depends on dates and hotel');
    if (same) bot(T('ऊपर वाली trips अब भी आपके लिए सबसे सही हैं।', 'The trips above still fit you best.'));
    else bot(T('आपके लिए ये ' + list.length + ' trips सबसे सही लगती हैं' + extra + ':', 'These ' + list.length + ' trips fit you best' + extra + ':'), function () { add(cards(list)); });
    /* ask the single most useful missing detail, once */
    priceQ = false;
    if (!S.month && !asked.month) { asked.month = 1; bot(T('कब जाने का सोच रहे हैं?', 'When are you planning to go?')); var nm = new Date().getMonth(); var ms = []; for (var i = 0; i < 4; i++) { var k = (nm + i) % 12; ms.push({ t: T(MNH[k], MN[k]), say: MN[k] }); } chips(ms); return; }
    if (!S.days && !asked.days) { asked.days = 1; bot(T('कितने दिन का ट्रिप?', 'How many days?')); chips([{ t: '3–4 ' + T('दिन', 'days'), say: '4 days' }, { t: '5–6 ' + T('दिन', 'days'), say: '6 days' }, { t: '7–9 ' + T('दिन', 'days'), say: '8 days' }, { t: '10+ ' + T('दिन', 'days'), say: '11 days' }]); return; }
    if (!S.who && !asked.who) { asked.who = 1; bot(T('कौन-कौन जा रहा है?', 'Who is travelling?')); chips([{ t: T('फैमिली', 'Family'), say: 'family' }, { t: T('कपल', 'Couple'), say: 'couple' }, { t: T('दोस्त', 'Friends'), say: 'friends' }, { t: T('तीर्थ यात्रा', 'Pilgrimage'), say: 'yatra' }]); return; }
    leadAsk();
  }
  function cards(list) {
    var wrap = el('div', 'sa-cards');
    list.forEach(function (tp) {
      var price = tp.price ? '<span class="pr">' + T('शुरुआत ', 'from ') + inr(tp.price) + ' <small>/' + T('व्यक्ति', 'person') + '</small></span>' : '<span class="pr"><small>' + T('रेट WhatsApp पर, मिनटों में', 'Price on request') + '</small></span>';
      var c = el('div', 'sa-card', '<img src="' + esc(tp.img) + '" alt="' + esc(tp.alt || tp.title) + '" loading="lazy" decoding="async" width="230" height="110"><div class="cb"><b>' + esc(tp.title) + '</b><span class="mt">' + tp.days + 'D/' + tp.nights + 'N · ' + esc(tp.start ? T('से ', 'from ') + tp.start : (tp.regionName || '')) + '</span>' + price +
        '<div class="ab"><button type="button" data-trip="' + esc(tp.slug) + '">' + T('देखें', 'View') + '</button><button type="button" class="p" data-pick="' + esc(tp.slug) + '">' + T('यही चाहिए', 'I like this') + '</button></div></div>');
      wrap.appendChild(c);
    });
    return wrap;
  }
  function moreTrips() {
    var have = shown.map(function (t) { return t.slug; });
    var list = TRIPS.map(function (tp) { return [score(tp, S), tp]; }).sort(function (a, b) { return b[0] - a[0]; }).map(function (x) { return x[1]; }).filter(function (tp) { return have.indexOf(tp.slug) < 0; }).slice(0, 3);
    shown = shown.concat(list);
    bot(T('ये 3 और विकल्प:', '3 more options:'), function () { add(cards(list)); });
    leadAsk(true);
  }
  var picked = '';
  function pickTrip(slug) {
    var tp = TRIPS.filter(function (x) { return x.slug === slug; })[0]; if (!tp) return;
    picked = tp.title; engaged = true; me(T('मुझे ये पसंद है: ', 'I like: ') + tp.title);
    ev('suzu_assistant', { step: 'pick', slug: slug });
    bot(T('बढ़िया चुनाव! 👌 <b>' + esc(tp.title) + '</b> — आपकी तारीख़ पर होटल, कैब और आज का best rate हमारी टीम WhatsApp पर भेज देगी।', 'Great choice! 👌 <b>' + esc(tp.title) + '</b> — our team will WhatsApp you hotels, cab and today’s best rate for your dates.'));
    leadForm();
  }
  function leadAsk(soft) {
    if (leadSent) { bot(T('आपकी details हमारी टीम के पास हैं — वो जल्द WhatsApp करेंगे। 🙏 ये नई पसंद भी सीधे भेज दीजिए:', 'Our team already has your details — they’ll WhatsApp you shortly. 🙏 Send this new idea to them too:')); chips([{ t: T('WhatsApp पर भेजें', 'Send on WhatsApp'), href: waLink(), cls: 'wa' }]); return; }
    bot(T('क्या मैं आपकी <b>पूरी itinerary और आज का best rate</b> WhatsApp पर भिजवा दूँ? (फ्री, कोई बाध्यता नहीं)', 'Shall I get our team to send you the <b>full itinerary and today’s best rate</b> on WhatsApp? (free, no obligation)'));
    chips([{ t: '✅ ' + T('हाँ, भेजिए', 'Yes, send it'), act: 'lead', cls: 'p' }].concat(soft ? [] : [{ t: T('और विकल्प दिखाएँ', 'Show more options'), act: 'more' }]).concat([{ t: T('WhatsApp पर अभी बात', 'Chat on WhatsApp now'), href: waLink(), cls: 'wa' }]));
  }
  function waText() {
    var t = T('नमस्ते Suzu Travels, मुझे ट्रिप प्लान करनी है। ', 'Hi Suzu Travels, I want to plan a trip. ') + summaryTags().join(', ') + (cabReq ? ' | Cab: ' + cabReq.split(' (')[0] : '');
    if (picked) t += ' | ' + picked; else if (shown[0]) t += ' | ' + shown.slice(0, 3).map(function (x) { return x.title; }).join(' / ');
    return t + ' (Suzu Assistant)';
  }
  function waLink() { return 'https://wa.me/' + WA + '?text=' + encodeURIComponent(waText()); }
  function leadForm() {
    if (leadSent) { leadAsk(); return; }
    q = q.then(function () {
      var f = el('form', 'sa-form');
      f.innerHTML = '<label for="sa-nm">' + T('आपका नाम', 'Your name') + '</label><input id="sa-nm" autocomplete="name" maxlength="60">' +
        '<label for="sa-ph">' + T('WhatsApp नंबर', 'WhatsApp number') + '</label><input id="sa-ph" type="tel" inputmode="tel" autocomplete="tel" maxlength="16" placeholder="98xxxxxxxx">' +
        '<p class="er" hidden></p><button type="submit">' + T('Itinerary + best rate भेजें', 'Send me the itinerary + best rate') + '</button><small>' + T('हम सिर्फ़ इसी ट्रिप के लिए संपर्क करेंगे।', 'We only contact you about this trip.') + '</small>';
      f.addEventListener('submit', function (e) {
        e.preventDefault();
        var nm = f.querySelector('#sa-nm').value.trim(), ph = f.querySelector('#sa-ph').value.replace(/\D/g, ''), er = f.querySelector('.er');
        if (ph.length === 12 && ph.indexOf('91') === 0) ph = ph.slice(2);
        if (ph.length === 11 && ph[0] === '0') ph = ph.slice(1);
        if (!/^[6-9]\d{9}$/.test(ph)) { er.textContent = T('कृपया सही 10 अंकों का WhatsApp नंबर लिखें।', 'Please enter a valid 10-digit WhatsApp number.'); er.hidden = false; return; }
        er.hidden = true; f.querySelector('button').disabled = true;
        var ref = sendLead(nm, ph);
        f.remove(); me((nm ? nm + ' · ' : '') + ph);
        bot(T('धन्यवाद' + (nm ? ' ' + esc(nm.split(' ')[0]) : '') + '! 🙏 आपकी request मिल गई (Ref <b>' + ref + '</b>). हमारी टीम जल्द ही WhatsApp पर itinerary और rate भेजेगी।', 'Thank you' + (nm ? ' ' + esc(nm.split(' ')[0]) : '') + '! 🙏 Request received (Ref <b>' + ref + '</b>). Our team will WhatsApp you the itinerary and rate shortly.'));
        chips([{ t: T('अभी WhatsApp पर बात करें', 'Chat on WhatsApp now'), href: waLink(), cls: 'wa' }, { t: '📞 ' + T('कॉल करें', 'Call us'), href: 'tel:+' + WA }]);
      });
      add(f);
      setTimeout(function () { var i = f.querySelector('#sa-nm'); if (i && W.matchMedia('(min-width:769px)').matches) i.focus(); }, 50);
    });
  }
  function sendLead(name, phone) {
    var ref = 'SZ-' + String(Date.now()).slice(-6), src = srcTag();
    var dest = summaryTags().slice(0, 2).join(' / ') || (cabReq ? 'Cab ' + cabReq.split(' (')[0] : T('ट्रिप', 'Trip'));
    var lines = ['Suzu Assistant (homepage chat) v' + VER];
    if (S.region) lines.push('Region: ' + S.region + (S.place ? ' (' + S.place + ')' : ''));
    if (S.who) lines.push('Trip type: ' + S.who);
    if (S.month) lines.push('Month: ' + MN[S.month - 1]);
    if (S.days) lines.push('Days: ' + S.days);
    if (S.bud) lines.push('Budget per person: ' + inr(S.bud));
    if (S.pax) lines.push('People: ' + S.pax);
    if (cabReq) lines.push('Cab route asked: ' + cabReq);
    if (prev.length) lines.push('Earlier in chat: ' + prev.join(' || ').slice(0, 300));
    if (picked) lines.push('Liked: ' + picked);
    if (shown.length) lines.push('Shown: ' + shown.map(function (x) { return x.title; }).join(' | '));
    lines.push('Chat: ' + said.join(' | ').slice(0, 900));
    lines.push('Language: ' + lang);
    lines.push('Source: ' + src + ' | Page: ' + location.pathname + ' (Suzu Assistant) | Ref: ' + ref);
    try {
      var fd = new FormData();
      fd.append('action', 'suzu_submit_landing_form'); fd.append('name', name || 'Suzu chat'); fd.append('contact', phone); fd.append('email', '');
      fd.append('destination', 'SUZU ASSISTANT 🤖 ' + dest + '  •  Source: ' + src + '  •  Ref: ' + ref);
      fd.append('travel_date', S.month ? MN[S.month - 1] : ''); fd.append('message', lines.join('\n'));
      if (!(navigator.sendBeacon && navigator.sendBeacon('/wp-admin/admin-ajax.php', fd))) fetch('/wp-admin/admin-ajax.php', { method: 'POST', body: fd, keepalive: true }).catch(function () {});
      if (typeof gtag === 'function') gtag('event', 'conversion', { 'send_to': 'AW-17212172485/SPBwCPbf_9saEMXRs49A' });
    } catch (e) {}
    leadSent = true; ev('suzu_assistant', { step: 'lead' });
    return ref;
  }

  function human() {
    bot(T('ज़रूर! 🙂 हमारी टीम से सीधे बात कीजिए — या नंबर दीजिए, हम आपको कॉल / WhatsApp करेंगे।', 'Of course! 🙂 Talk to our team directly — or leave your number and we’ll call / WhatsApp you.'));
    chips([{ t: 'WhatsApp', href: waLink(), cls: 'wa' }, { t: '📞 ' + PHONE, href: 'tel:+' + WA }, { t: T('मुझे कॉल करें', 'Call me back'), act: 'lead', cls: 'p' }]);
  }
  function pay() {
    bot(T('<b>बुकिंग कैसे होती है:</b><br>• एक छोटा token advance देकर आपका rate lock हो जाता है<br>• बाकी रकम ट्रिप से पहले<br>• advance non-refundable है, पर 6 महीने में एक बार तारीख़ बदल सकते हैं<br>• Online payment Razorpay से, या bank / UPI — <a href="/payment/">Payment page</a>',
      '<b>How booking works:</b><br>• a small token advance locks your rate<br>• the balance is paid before the trip<br>• the advance is non-refundable, but you can change the date once within 6 months<br>• pay online via Razorpay, or bank / UPI — <a href="/payment/">Payment page</a>'));
    chips([{ t: T('ट्रिप ढूँढें', 'Find a trip'), say: T('ट्रिप दिखाओ', 'show trips') }, { t: T('टीम से बात', 'Talk to team'), say: 'talk to team' }]);
  }
  function trust() {
    bot(T('Suzu Travels एक <b>HP Tourism registered travel agent</b> है · Reg. No. DTO-MND-11-243/2022 — <a href="/certificates/">certificate देखें</a>. 2019 से हिमाचल और पूरे भारत की trips।', 'Suzu Travels is an <b>HP Tourism registered travel agent</b> · Reg. No. DTO-MND-11-243/2022 — <a href="/certificates/">see the certificate</a>. Planning trips in Himachal and across India since 2019.'));
  }
  function cab(m) {
    m = m || {};
    if (m.from || m.url !== '/cabs/') {
      var nm = function (c) { return CNAME[c] ? T(CNAME[c][0], CNAME[c][1]) : c; };
      var route = (/tempo/.test(m.url) ? 'Tempo Traveller ' : '') + (m.from && m.to ? nm(m.from) + ' → ' + nm(m.to) : (m.from ? nm(m.from) : ''));
      cabReq = (m.from && m.to ? m.from + ' to ' + m.to : m.from) + ' (' + m.url + ')';
      bot('🚕 ' + (route ? '<b>' + esc(route) + '</b> ' : '') + T('टैक्सी — गाड़ियाँ, रूट और fare की पूरी जानकारी यहाँ: <a href="' + m.url + '">' + T('यह पेज देखें', 'see this page') + '</a>. तारीख़ और गाड़ी (Sedan / SUV / Innova / Tempo) बताइए — या नंबर दीजिए, हमारी टीम आज का fare WhatsApp कर देगी।', 'taxi — cars, route and fares are here: <a href="' + m.url + '">see this page</a>. Tell me your date and car (sedan / SUV / Innova / Tempo) — or leave your number and our team will WhatsApp today’s fare.'));
      chips([{ t: T('Fare भिजवाएँ', 'Send me a fare'), act: 'lead', cls: 'p' }, { t: T('Cab पेज खोलें', 'Open cab page'), href: m.url }, { t: 'WhatsApp', href: waLink(), cls: 'wa' }]);
      return;
    }
    bot(T('🚕 हम पूरे North India में one-way और round-trip टैक्सी देते हैं (Delhi, Chandigarh → Shimla, Manali, Dharamshala, Char Dham…). Route और fare यहाँ: <a href="/cabs/">Cabs & taxi</a>. अपना route बताइए — या नंबर दीजिए, हम fare भेज देंगे।', '🚕 We run one-way and round-trip taxis across North India (Delhi, Chandigarh → Shimla, Manali, Dharamshala, Char Dham…). Routes & fares: <a href="/cabs/">Cabs & taxi</a>. Tell me your route — or leave your number for a fare.'));
    chips([{ t: T('Fare भिजवाएँ', 'Send me a fare'), act: 'lead', cls: 'p' }, { t: 'WhatsApp', href: waLink(), cls: 'wa' }]);
  }
  function jump(id, html) {
    bot(html, function () { setTimeout(function () { var t = D.getElementById(id); if (t) { close(); t.scrollIntoView({ behavior: 'smooth', block: 'start' }); } }, 900); });
  }
  function unknown() {
    bot(T('माफ़ कीजिए, ये मैं ठीक से समझ नहीं पाई। 🙏 जगह, महीना, दिन या बजट बताइए — या हमारी टीम से सीधे बात कीजिए।', 'Sorry, I didn’t quite get that. 🙏 Tell me a place, month, days or budget — or talk to our team directly.'));
    chips([{ t: '🏔 ' + T('हिमाचल', 'Himachal'), say: 'Himachal' }, { t: T('कश्मीर', 'Kashmir'), say: 'Kashmir' }, { t: T('गोवा', 'Goa'), say: 'Goa' }, { t: T('चार धाम', 'Char Dham'), say: 'char dham' }, { t: '📞 ' + T('टीम से बात', 'Talk to team'), say: 'talk to team' }]);
  }

  /* ---------- voice ---------- */
  var rec = null, recBusy = false;
  function stopRec() { recBusy = false; if (micBtn) micBtn.setAttribute('aria-pressed', 'false'); if (input) input.placeholder = T('जैसे: दिसंबर में मनाली, 5 दिन, फैमिली', 'e.g. Manali in December, 5 days, family'); try { rec && rec.stop(); } catch (e) {} }
  function startRec() {
    if (!SR) return;
    try { rec = new SR(); } catch (e) { return; }
    rec.lang = lang === 'hi' ? 'hi-IN' : 'en-IN'; rec.interimResults = true; rec.maxAlternatives = 1; rec.continuous = false;
    var fin = '';
    rec.onresult = function (e) { var txt = ''; for (var i = e.resultIndex; i < e.results.length; i++) { txt += e.results[i][0].transcript; if (e.results[i].isFinal) fin += e.results[i][0].transcript; } input.value = txt; };
    rec.onerror = function (e) { stopRec(); if (e && (e.error === 'not-allowed' || e.error === 'service-not-allowed')) bot(T('माइक की अनुमति नहीं मिली — ब्राउज़र के address bar में माइक allow करें, या लिखकर बताइए।', 'Microphone is blocked — allow it in the address bar, or just type.')); else if (e && e.error === 'no-speech') bot(T('कुछ सुनाई नहीं दिया — माइक दबाकर फिर बोलिए।', 'Didn’t hear anything — tap the mic and speak again.')); };
    rec.onend = function () { var was = recBusy; stopRec(); var v = (fin || input.value).trim(); if (was && v) { input.value = ''; handle(v); } };
    try { rec.start(); recBusy = true; micBtn.setAttribute('aria-pressed', 'true'); input.value = ''; input.placeholder = T('सुन रही हूँ… बोलिए', 'Listening… speak now'); } catch (e) { stopRec(); }
  }

  /* test hooks */
  W.SuzuAssistant = { open: open, close: close, say: handle, parse: parse, best: best, intent: intent, cab: cabMatch, version: VER };

  if (D.readyState === 'loading') D.addEventListener('DOMContentLoaded', build); else build();
})();
