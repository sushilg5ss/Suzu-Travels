#!/usr/bin/env python3
"""Homepage performance release — 9 Oct 2026 (after Ashish's GTmetrix report: 5.2 s, perf 56, TBT 992 ms).
Usage: python3 enh-2026-10-09c.py live.html after.html   (also writes suzu-nz-trips.json next to after.html)
1. Trip-sheet data (itineraries, highlights, inclusions, exclusions, blurbs — ~160 KB of the 240 KB nz-data) moved to
   /suzu-nz-trips.json, fetched on idle after load (or on first hover of the explorer). Sheet/compare wait for it.
2. Hero rail + region-tab thumbnails 768px → 300px (they render at ~90 px): about −0.8 MB on first paint.
3. Phosphor icon loader (unpkg, 6 CSS + 3 fonts, was a blocking <script> in <head>) → defer.
4. Google Ads gtag.js loads on first interaction or 3 s after load (the gtag() stub queues earlier events → no lost conversions).
5. Hero film sources attached after the load event (poster = LCP paints first; film no longer competes with LCP/fonts);
   poster preloaded with fetchpriority=high.
6. Mobile (≤900 px): no backdrop-filter blur on hero pills/dots/buttons/chips, no animated film grain (biggest paint cost).
Deliberate legacy edits (parity will flag): the phosphor <script> gains `defer`; the gtag loader tag is replaced by a delayed loader.
"""
import sys, re, json, os
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
assert 'suzu-nz-trips.json' not in s, 'already applied'
def once(n): assert s.count(n) == 1, (n[:60], s.count(n)); return s.index(n)

# 1. lazy trip data
m = re.search(r'(<script[^>]*id="nz-data"[^>]*>)(.*?)(</script>)', s, re.S)
D = json.loads(m.group(2)); HEAVY = ['itin', 'hl', 'inc', 'exc', 'blurb']
X = {}
for t in D['trips']:
    X[t['slug']] = {k: t.pop(k) for k in HEAVY if k in t}
json.dump(X, open(os.path.join(os.path.dirname(os.path.abspath(dst)), 'suzu-nz-trips.json'), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
s = s[:m.start(2)] + json.dumps(D, ensure_ascii=False) + s[m.end(2):]
a = "var D=JSON.parse(document.getElementById('nz-data').textContent);\n"
once(a)
s = s.replace(a, a + "var NZX=null,NZXP=null;function nzLoadX(){if(NZX)return Promise.resolve(NZX);if(NZXP)return NZXP;NZXP=fetch('/suzu-nz-trips.json?v=1',{credentials:'omit'}).then(function(r){if(!r.ok)throw 0;return r.json()}).then(function(j){D.trips.forEach(function(t){var x=j[t.slug];if(x)for(var k in x)t[k]=x[k]});NZX=j;return j}).catch(function(e){NZXP=null;throw e});return NZXP}\n"
 "window.addEventListener('load',function(){setTimeout(function(){nzLoadX().catch(function(){})},2500)});var _tp=document.getElementById('tour-packages');if(_tp){['pointerover','touchstart','focusin'].forEach(function(ev){_tp.addEventListener(ev,function(){nzLoadX().catch(function(){})},{once:true,passive:true})})}\n")
a = "function openTrip(slug){var t=BY[slug];if(!t)return;cur=t;"
once(a)
s = s.replace(a, "function openTrip(slug){var t=BY[slug];if(!t)return;if(!NZX){nzLoadX().then(function(){openTrip(slug)},function(){location.href=t.url});return}cur=t;")
i = once('function openCompare('); j = s.index('{', i) + 1
s = s[:j] + "if(!NZX){var _a=arguments,_f=openCompare;nzLoadX().then(function(){_f.apply(null,_a)},function(){});return}" + s[j:]

# 2. small thumbnails in the hero rail and region tabs
def small(u):
    mm = re.search(r'-768x(\d+)\.webp$', u)
    if not mm: return u
    hgt = int(mm.group(1)); nh = round(300 * hgt / 768)
    return u[:mm.start()] + '-300x%d.webp' % nh
cnt = 0
def rep(mo):
    global cnt; u = mo.group(2); nu = small(u); cnt += (nu != u); return mo.group(1) + nu + '"'
s = re.sub(r'(<button class="nz-(?:dot|reg)"[^>]*><img src=")([^"]+)"', rep, s)

# 3. phosphor defer
a = '<script src="https://unpkg.com/@phosphor-icons/web"></script>'; once(a)
s = s.replace(a, '<script defer src="https://unpkg.com/@phosphor-icons/web"></script>')

# 4. delayed gtag loader
a = '<script async src="https://www.googletagmanager.com/gtag/js?id=AW-17212172485"></script>'; once(a)
s = s.replace(a, '<script id="nz-gtag-loader">(function(){var d=false;function go(){if(d)return;d=true;var x=document.createElement("script");x.async=true;x.src="https://www.googletagmanager.com/gtag/js?id=AW-17212172485";document.head.appendChild(x)}'
                 '["pointerdown","touchstart","keydown","scroll"].forEach(function(e){addEventListener(e,go,{once:true,passive:true})});'
                 'addEventListener("load",function(){setTimeout(go,3000)});setTimeout(go,8000)})();</script>')

# 5. film after load + poster preload
a = "v.innerHTML='<source src=\"suzu-film2-'+k+'.mp4?v=1\" type=\"video/mp4\"><source src=\"suzu-film2-'+k+'.webm?v=1\" type=\"video/webm\">';}catch(e){}})();"
once(a)
s = s.replace(a, "var go=function(){if(v.getAttribute('data-src-on'))return;v.setAttribute('data-src-on','1');v.innerHTML='<source src=\"suzu-film2-'+k+'.mp4?v=1\" type=\"video/mp4\"><source src=\"suzu-film2-'+k+'.webm?v=1\" type=\"video/webm\">';v.load();var p=v.play();if(p&&p.catch)p.catch(function(){})};"
                 "if(document.readyState==='complete')go();else{addEventListener('load',function(){setTimeout(go,300)});setTimeout(go,4000)}}catch(e){}})();")
a = '<video class="nz-film" autoplay muted loop playsinline preload="auto" aria-hidden="true">'; once(a)
s = s.replace(a, '<video class="nz-film" autoplay muted loop playsinline preload="metadata" aria-hidden="true">')
k = once('</head>')
s = s[:k] + '<link rel="preload" as="image" href="suzu-film2-16x9.jpg?v=1" media="(min-aspect-ratio: 4/5)" fetchpriority="high"><link rel="preload" as="image" href="suzu-film2-9x16.jpg?v=1" media="(max-aspect-ratio: 4/5)" fetchpriority="high"><link rel="preconnect" href="https://unpkg.com" crossorigin><link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>\n' + s[k:]

# 6. mobile paint diet (nature CSS block)
i = once('/* ---------- 2026-10-09: traveller\'s toolkit ---------- */'); j = s.index('</style>', i)
s = s[:j] + "\n/* ---------- 2026-10-09 perf: mobile paint diet ---------- */\n@media (max-width:900px){.nz-pill,.nz-dot,.nz-btn-ghost,.nz-filmbtn,.nz-bar,.nz-dur,.nzw-chip,.nzw-alt{backdrop-filter:none!important;-webkit-backdrop-filter:none!important}.nz-pill,.nz-btn-ghost,.nz-filmbtn{background:rgba(14,42,27,.55)!important}.nz-dot{background:rgba(14,42,27,.5)!important}.nz-grain{display:none!important}}\n" + s[j:]

open(dst, 'w', encoding='utf-8').write(s)
print('ok thumbs', cnt, 'trips.json', len(X), 'size', len(s.encode()))
