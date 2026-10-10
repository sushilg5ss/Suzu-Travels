#!/usr/bin/env python3
"""Homepage 10 Oct 2026 — lighter phone film (Ashish: mobile fully-loaded 26 s).
Usage: python3 enh-2026-10-10a.py live.html after.html
- Phones (max-aspect-ratio 4/5) now get suzu-film2-9x16-540.mp4 (540x960, 3.06 MB) instead of the 720p 6.8 MB file; desktop unchanged (720p).
- Film autoplay is skipped (poster + play button, existing "lite" mode) when the connection reports Save-Data, 2g/3g, or downlink < 1.5 Mbps.
- On phones the film sources attach 1.5 s after load (desktop 0.3 s) so the LCP poster and fonts are never competing with video bytes.
Also applies the night release enh-2026-10-09n.py (Recently viewed strip) separately.
"""
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
assert '9x16-540' not in s, 'already applied'
def once(n): assert s.count(n) == 1, (n[:70], s.count(n)); return s.index(n)
a = "lite=!!c.saveData||/^(slow-2g|2g|3g)$/.test(c.effectiveType||'')||matchMedia('(prefers-reduced-motion: reduce)').matches;"; once(a)
s = s.replace(a, "lite=!!c.saveData||/^(slow-2g|2g|3g)$/.test(c.effectiveType||'')||(c.downlink&&c.downlink<1.5)||matchMedia('(prefers-reduced-motion: reduce)').matches,f=k==='9x16'?'suzu-film2-9x16-540.mp4?v=1':'suzu-film2-'+k+'.mp4?v=1';")
a = "v.setAttribute('data-cur','suzu-film2-'+k+'.mp4?v=1');"; once(a)
s = s.replace(a, "v.setAttribute('data-cur',f);")
a = "v.innerHTML='<source src=\"suzu-film2-'+k+'.mp4?v=1\" type=\"video/mp4\"><source src=\"suzu-film2-'+k+'.webm?v=1\" type=\"video/webm\">';"; once(a)
s = s.replace(a, "v.innerHTML='<source src=\"'+f+'\" type=\"video/mp4\"><source src=\"suzu-film2-'+k+'.webm?v=1\" type=\"video/webm\">';")
a = "if(document.readyState==='complete')go();else{addEventListener('load',function(){setTimeout(go,300)});setTimeout(go,4000)}"; once(a)
s = s.replace(a, "var dl=k==='9x16'?1500:300;if(document.readyState==='complete')setTimeout(go,dl);else{addEventListener('load',function(){setTimeout(go,dl)});setTimeout(go,4000+dl)}")

# the hero's pick() attached <source>s itself during parse (webm first) and the boot loader attached mp4 again after load -> both files downloaded.
# Now: pick() only runs at parse in lite mode; the boot loader is the single attach (mp4 first). pick() still handles orientation change / unlock.
a="pick(); if(portrait.addEventListener)portrait.addEventListener('change',pick);"; once(a)
s=s.replace(a,"if(lite)pick(); if(portrait.addEventListener)portrait.addEventListener('change',pick);")
a="V.innerHTML='<source src=\"'+f.webm+'\" type=\"video/webm\"><source src=\"'+f.src+'\" type=\"video/mp4\">';V.load();"; once(a)
s=s.replace(a,"V.innerHTML='<source src=\"'+f.src+'\" type=\"video/mp4\"><source src=\"'+f.webm+'\" type=\"video/webm\">';V.load();")
# nz-data: phone cut -> 540p file (must equal the boot loader's data-cur so pick() does not reload)
a='"p": {"src": "suzu-film2-9x16.mp4?v=1"'; once(a)
s=s.replace(a,'"p": {"src": "suzu-film2-9x16-540.mp4?v=1"')
open(dst, 'w', encoding='utf-8').write(s); print('ok', len(s.encode()))
