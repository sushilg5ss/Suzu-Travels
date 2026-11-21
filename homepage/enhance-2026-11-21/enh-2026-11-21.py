#!/usr/bin/env python3
"""Homepage Enhancement 2026-11-21 night.
1) Trip sheet: "Weather on this route" row under "When to go" — up to 5 places on the trip's route,
   each chip = live temperature now (+ snow flag from the 5-day forecast) from /suzu-weather-feed.json
   (MET Norway, same feed as the weather widget), linking to the place's weather page + its Hindi page.
   Feed is fetched only when a sheet opens (never on page load), skipped on Save-Data; temps hidden if feed > 30 h old.
2) Fix: the 74 links in #nz-wxa (20 Nov) had no trailing slash -> each was a 301 hop. Now point straight at the 200 URL.
3) 10 links to pages published 20 Nov: airports, Kangra toy train, 3 Dharamshala institutes (Routes fold); German guides + Malaysia (overseas fold).
Usage: python3 enh-2026-11-21.py IN.html OUT.html  (asserts not already applied)"""
import sys, re, json, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wxmap import M
src = open(sys.argv[1], encoding='utf-8').read()
s = src
assert 'nz-wxr' not in s, 'already applied'
U = 'https://suzutravels.com/'

# ---------- 2) trailing slash on the 74 nz-wxa links ----------
a = s.find('<details class="nz-wxa" id="nz-wxa">'); assert a > 0
b = s.find('</details>', a); blk = s[a:b]
fixed, n = re.subn(r'href="https://suzutravels\.com/([a-z-]+-weather)"', r'href="https://suzutravels.com/\1/"', blk)
assert n == 74, n
s = s[:a] + fixed + s[b:]

# ---------- 1) weather row in the trip sheet ----------
jsmap = json.dumps(M, ensure_ascii=False, separators=(',', ':'))
JS = r'''/* 2026-11-21: live weather on this trip's route (feed /suzu-weather-feed.json = MET Norway, same as the weather widget; fetched only when a sheet opens) */
var WXR=__MAP__,WXF=null,WXB=null;
function wxPlaces(t){var out=[],seen={};(t.route||[]).concat(t.top?[t.top[0]]:[]).forEach(function(n){var v=WXR[String(n).toLowerCase().trim()];if(v&&!seen[v[2]]&&out.length<5){seen[v[2]]=1;out.push(v)}});return out}
function wxRow(t){try{var ps=wxPlaces(t);if(!ps.length)return '';var W='https://suzutravels.com/';
  return '<div class="nz-wxr"><p class="nz-wxr-h"><b>Weather on this route</b><span class="nz-wxr-u"></span></p><ul>'+ps.map(function(v){
    return '<li data-wx="'+v[1]+'"><a class="nz-wxr-a" href="'+W+v[2]+'"><span>'+v[0]+'</span><em></em></a>'+(v[3]?'<a class="nz-wxr-hi" href="'+W+v[3]+'" lang="hi" aria-label="'+v[0]+' weather in Hindi">हिंदी</a>':'')+'</li>'}).join('')+'</ul></div>'}catch(e){return ''}}
function wxPaint(d){var box=$('#nz-sc .nz-wxr');if(!box||!d)return;var up=Date.parse(d.updated);if(!up||Date.now()-up>36e5*30)return;
  if(!WXB){WXB={};(d.places||[]).concat(d.more||[]).forEach(function(p){if(p&&p.id)WXB[p.id]=p})}
  var f=false;try{f=localStorage.getItem('nzw-unit')==='f'}catch(_){}
  $$('li[data-wx]',box).forEach(function(li){var p=WXB[li.getAttribute('data-wx')];if(!p||!p.now||typeof p.now.t!=='number')return;
    var c=p.now.t,tx=f?Math.round(c*9/5+32)+'°F':Math.round(c)+'°C',sn=(p.days||[]).some(function(x){return x&&x.snow});
    li.querySelector('em').textContent=tx+(sn?' · ❄ snow':'');
    li.querySelector('.nz-wxr-a').setAttribute('aria-label',li.querySelector('span').textContent+': '+tx+' now'+(sn?', snow in the 5-day forecast':'')+'. Full forecast')});
  var u=$('.nz-wxr-u',box);if(u)try{u.textContent='Now · updated '+new Date(up).toLocaleTimeString('en-IN',{hour:'2-digit',minute:'2-digit',hour12:false,timeZone:'Asia/Kolkata'})+' IST · MET Norway'}catch(_){}}
function wxFill(){try{if(!$('#nz-sc .nz-wxr'))return;var c=navigator.connection;if(c&&c.saveData)return;
  if(!WXF)WXF=fetch('/suzu-weather-feed.json').then(function(r){if(!r.ok)throw new Error(r.status);return r.json()});
  WXF.then(wxPaint).catch(function(){WXF=null})}catch(e){}}
'''.replace('__MAP__', jsmap)
k = 'function head(t){'; assert s.count(k) == 1
s = s.replace(k, JS + k)
k = "+monthStrip(t);\n}"; assert s.count(k) == 1
s = s.replace(k, "+monthStrip(t)+wxRow(t);\n}")
k = "panel('plan');foot();"; assert s.count(k) == 1
s = s.replace(k, "panel('plan');foot();wxFill();")

CSS = '''<style id="nz-wxr-css">
/* nz-wxr 2026-11-21: trip sheet "Weather on this route" (live temp chips -> weather pages) */
.nz-wxr{padding:2px 22px 12px}
.nz-wxr-h{display:flex;flex-wrap:wrap;align-items:baseline;justify-content:space-between;gap:2px 12px;margin:0 0 8px;font-size:.76rem;color:var(--nz-muted)}
.nz-wxr-h b{font-size:.66rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase}
.nz-wxr ul{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:6px}
.nz-wxr li{display:flex;align-items:stretch;border:1.5px solid #BFDCF2;border-radius:999px;background:var(--nz-sky,#E3F1FB);overflow:hidden}
.nz-wxr a{display:inline-flex;align-items:center;gap:6px;min-height:44px;padding:0 12px;color:#0B3A63;font:700 .84rem/1.1 var(--nz-body);text-decoration:none}
.nz-wxr em{font-style:normal;font-weight:800;color:#1864AB;white-space:nowrap}
.nz-wxr em:empty{display:none}
.nz-wxr .nz-wxr-hi{border-left:1.5px solid #BFDCF2;background:#fff;padding:0 11px;font-weight:600;font-size:.8rem;color:#2D3F33}
.nz-wxr a:hover{background:#fff;color:#0B4F8A}
.nz-wxr .nz-wxr-hi:hover{background:var(--nz-sky,#E3F1FB)}
.nz-wxr a:focus-visible{outline:3px solid var(--nz-gold,#D4A017);outline-offset:-3px;border-radius:999px}
@media (max-width:768px){.nz-wxr a{min-height:49px}} /* legacy html{zoom:.9} -> 44px rendered */
</style>'''
a = s.find('<style id="suzu-nature-2026-10">'); assert a > 0
b = s.find('</style>', a) + 8
s = s[:b] + '\n' + CSS + s[b:]

# ---------- 3) links to 20 Nov pages ----------
def li(items): return ''.join('<li><a href="%s%s"%s>%s</a></li>' % (U, p, (' lang="%s"' % lg) if lg else '', t) for p, t, lg in items)
def add_fold(summary_name, items):
    global s
    m = re.search(r'<details class="nz-xm"[^>]*><summary>%s <span>\((\d+)\)</span></summary><ul>' % re.escape(summary_name), s)
    assert m, summary_name
    end = s.find('</ul></details>', m.end()); assert end > 0
    for p, _, _ in items: assert 'href="%s%s"' % (U, p) not in s, 'already linked: ' + p
    cnt = int(m.group(1)) + len(items)
    s = s[:end] + li(items) + s[end:]
    s = s[:m.start(1)] + str(cnt) + s[m.end(1):]
add_fold('Routes, towns &amp; where to stay', [
  ('shimla-airport/', 'Shimla Airport (Jubbarhatti)', ''), ('kangra-airport/', 'Kangra Airport (Gaggal)', ''),
  ('kangra-valley-railway/', 'Kangra Valley toy train', ''), ('norbulingka-institute/', 'Norbulingka Institute', ''),
  ('tushita-meditation-centre/', 'Tushita Meditation Centre', ''), ('library-of-tibetan-works-and-archives/', 'Library of Tibetan Works &amp; Archives', '')])
add_fold('India guides for overseas guests', [
  ('himachal-tour-from-malaysia/', 'Himachal trip from Malaysia', ''),
  ('himachal-pradesh-reise/', 'Himachal Pradesh Reise (Deutsch)', 'de'), ('manali-reisefuehrer/', 'Manali Reiseführer (Deutsch)', 'de'),
  ('dharamsala-reisefuehrer/', 'Dharamsala Reiseführer (Deutsch)', 'de')])

open(sys.argv[2], 'w', encoding='utf-8').write(s)
print('ok', len(src.encode()), '->', len(s.encode()))
