#!/usr/bin/env python3
"""Homepage perf release 2 — 9 Oct 2026 late (GTmetrix bGiCauOz after release 1: LCP 1.5 s OK, TBT still 906 ms).
Usage: python3 enh-2026-10-09d.py live.html after.html
CPU profile of the live page: ~3 s of style/layout/paint ("program") on a 5,500-node DOM, of which #tour-packages alone is 2,550 nodes;
plus gtag.js 316 ms, live-reviews.js render 170 ms, the toolkit's odometer animation 35 ms, all inside the TBT window.
1. content-visibility:auto on every below-the-fold section (sizes from measured heights) → style/layout/paint skipped until near the viewport.
2. Google Ads gtag.js: first interaction only (fallback 10 s after load). gtag() stub queues earlier events.
3. live-reviews.js (legacy plugin, renders the review widgets): loads 2 s after the load event instead of defer.
4. Toolkit cost odometer: no animation on first paint (only when the user changes an input).
"""
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
assert 'perf2-2026-10-09' not in s, 'already applied'
def once(n): assert s.count(n) == 1, (n[:70], s.count(n)); return s.index(n)

# 1. content-visibility
i = once("/* ---------- 2026-10-09 perf: mobile paint diet ---------- */"); j = s.index('</style>', i)
CSS = ("\n/* ---------- perf2-2026-10-09: skip rendering of off-screen sections ---------- */\n"
       "#tour-packages{content-visibility:auto;contain-intrinsic-size:auto 2200px}"
       "#himachal-weather{content-visibility:auto;contain-intrinsic-size:auto 800px}"
       "section.nz-exp{content-visibility:auto;contain-intrinsic-size:auto 1000px}"
       "section.top-destinations,section.bento-destinations,section.section-newsletter{content-visibility:auto;contain-intrinsic-size:auto 750px}"
       "#when-to-go,#how-it-works,section.section-experience,section.section-image-features,.trustindex-reviews-wrapper{content-visibility:auto;contain-intrinsic-size:auto 900px}"
       "section.section-blog{content-visibility:auto;contain-intrinsic-size:auto 1400px}"
       "footer.main-footer{content-visibility:auto;contain-intrinsic-size:auto 700px}"
       "@media (max-width:900px){#tour-packages{contain-intrinsic-size:auto 3600px}section.section-blog{contain-intrinsic-size:auto 2400px}}\n")
s = s[:j] + CSS + s[j:]

# 2. gtag: interaction only, 10 s fallback
a = 'addEventListener("load",function(){setTimeout(go,3000)});setTimeout(go,8000)})();</script>'; once(a)
s = s.replace(a, 'addEventListener("load",function(){setTimeout(go,10000)})})();</script>')

# 3. live-reviews after load
a = '<script src="/wp-content/plugins/suzu-live-reviews/assets/live-reviews.js?v=1.0.0" defer></script>'; once(a)
s = s.replace(a, '<script id="nz-lr-loader">addEventListener("load",function(){setTimeout(function(){var x=document.createElement("script");x.src="/wp-content/plugins/suzu-live-reviews/assets/live-reviews.js?v=1.0.0";document.body.appendChild(x)},2000)})</script>')

# 4. toolkit odometer
a = "anim($('#nz-tk-big'),last||tot*0.9,tot);last=tot}"; once(a)
s = s.replace(a, "if(last)anim($('#nz-tk-big'),last,tot);else{var _b=$('#nz-tk-big');if(_b)_b.textContent=inr(tot)}last=tot}")

open(dst, 'w', encoding='utf-8').write(s); print('ok', len(s.encode()))
