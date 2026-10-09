#!/usr/bin/env python3
"""Homepage perf release 4 — 9 Oct 2026 (GTmetrix FunpIQH3: TBT 800 ms even with video removed on a test page).
Local experiment: blocking web fonts cut long-task blocking from 246 ms to 30 ms — every font file that arrives after first
layout forces a full relayout (~80-110 ms each on a 5,500-node page). Two fixes:
1. Google Fonts (Sora, Plus Jakarta Sans, Tiro Devanagari Hindi are variable fonts: one woff2 per family) are preloaded, so they are
   available at first layout — no later swap/relayout.
2. Phosphor icons: the unpkg loader pulled 6 icon sets (6 CSS + 3 fonts); the page uses only regular/fill/bold, all inside hidden
   menus or below the fold. Now only those 3 CSS files load, on first pointer/touch/scroll/key (fallback 8 s after load).
"""
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
assert 'nz-ph-loader' not in s, 'already applied'
def once(n): assert s.count(n) == 1, (n[:70], s.count(n)); return s.index(n)
a = '<script defer src="https://unpkg.com/@phosphor-icons/web"></script>'; once(a)
s = s.replace(a, '<script id="nz-ph-loader">(function(){var d=false;function go(){if(d)return;d=true;["regular","fill","bold"].forEach(function(v){var l=document.createElement("link");l.rel="stylesheet";l.href="https://cdn.jsdelivr.net/npm/@phosphor-icons/web@2.1.2/src/"+v+"/style.css";document.head.appendChild(l)})}["pointermove","pointerdown","touchstart","keydown","scroll"].forEach(function(e){addEventListener(e,go,{once:true,passive:true})});addEventListener("load",function(){setTimeout(go,8000)})})();</script>')
PRE = ''.join('<link rel="preload" as="font" type="font/woff2" crossorigin href="%s">' % u for u in [
 'https://fonts.gstatic.com/s/sora/v17/xMQbuFFYT72XzQUpDg.woff2',
 'https://fonts.gstatic.com/s/plusjakartasans/v12/LDIoaomQNQcsA88c7O9yZ4KMCoOg4Ko20yw.woff2',
 'https://fonts.gstatic.com/s/tirodevanagarihindi/v7/55xyezN7P8T4e0_CfIJrwdodg9HoYw0i-M9vTuMPTG0.woff2',
 'https://fonts.gstatic.com/s/tirodevanagarihindi/v7/55xyezN7P8T4e0_CfIJrwdodg9HoYw0i-M9vT-MP.woff2'])
i = once('</head>')
s = s[:i] + '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>' + PRE + s[i:]
open(dst, 'w', encoding='utf-8').write(s); print('ok', len(s.encode()))
