#!/usr/bin/env python3
"""Homepage perf release 3 — 9 Oct 2026 (GTmetrix tgNSr2R1: perf 61, LCP 1.1 s, TBT 829 ms).
Usage: python3 enh-2026-10-09e.py live.html after.html
Trace of the live page: the single biggest long task (~200 ms) is the nature script evaluating synchronously inside HTML parsing —
JSON.parse + explorer wiring + 63 compare pills + reveal measurements + forced layouts — all before the page is interactive.
Change: the hero part stays immediate (film, calligraphy, rail); everything else runs after the load event in two separate tasks:
  task 1 = reveal observer + trip explorer + trip sheet (deep links included); task 2 = guest stories + compare + explore-sync.
No behaviour change except that explorer/sheet handlers attach ~0.3–1 s later than before.
"""
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
assert 'function nzRest(' not in s, 'already applied'
a = s.index('<script id="suzu-nature-2026-10-js">'); b = s.index('</script>', a)
js = s[a:b]
m1 = '/* ================= REVEAL ================= */'; m2 = '/* ================= GUEST STORIES ================= */'
assert js.count(m1) == 1 and js.count(m2) == 1
tail = '})();\n'   # closes the outer IIFE
assert js.endswith(tail), repr(js[-40:])
body = js[:-len(tail)]
i1 = body.index(m1); i2 = body.index(m2)
new = (body[:i1] + 'function nzRest(){\n' + body[i1:i2] + 'setTimeout(function(){\n' + body[i2:] + '\n},0);\n}\n'
       "(function(){var done=false;function go(){if(done)return;done=true;setTimeout(nzRest,0)}if(document.readyState==='complete')go();else addEventListener('load',go);setTimeout(go,6000)})();\n" + tail)
s = s[:a] + new + s[b:]

# reveal observers: never force layout (getBoundingClientRect inside content-visibility sections lays them out) — observe only
a="$$('.nz-xp,.nz-vid,.nz-head').forEach(function(el,k){var r=el.getBoundingClientRect();if(r.top<innerHeight)return;el.classList.add('nz-rv');el.style.transitionDelay=((k%4)*70)+'ms';io.observe(el)});"
assert s.count(a)==1; s=s.replace(a,"$$('.nz-xp,.nz-vid,.nz-head').forEach(function(el,k){el.classList.add('nz-rv');el.style.transitionDelay=((k%4)*70)+'ms';io.observe(el)});")
a="""  targets.forEach(function (el) {
    var r = el.getBoundingClientRect();
    if (r.top < window.innerHeight) return;   // already on screen: never hide it
    el.classList.add('sz-reveal'); io.observe(el);
  });"""
assert s.count(a)==1, s.count(a); s=s.replace(a,"""  targets.forEach(function (el) {
    el.classList.add('sz-reveal'); io.observe(el);   // perf3: no forced layout; the observer fires immediately for on-screen elements
  });""")

# hidden panels should not be laid out: nav mega-menus (shown on hover / mobile-open) and the planner popup (shown with .active)
i=s.index("/* ---------- perf2-2026-10-09: skip rendering of off-screen sections ---------- */"); j=s.index('</style>',i)
s=s[:j]+"\n/* ---------- perf3-2026-10-09: hidden panels skip layout ---------- */\n@media (hover:hover){.nav-dropdown-wrapper:not(:hover):not(:focus-within):not(.mobile-open) .dropdown-menu{content-visibility:hidden}}.hero-search-wrapper:not(.active){content-visibility:hidden}\n"+s[j:]
# WhatsApp widget: creating an AudioContext for the "pop" sound costs ~130 ms on the main thread at 5 s; browsers block it before a gesture anyway
a="            var playSound = true;"; assert s.count(a)==1; s=s.replace(a,"            var playSound = false; // perf3: no auto 'pop' sound (AudioContext cost ~130 ms; blocked before user gesture anyway)")
open(dst, 'w', encoding='utf-8').write(s); print('ok', len(s.encode()))
