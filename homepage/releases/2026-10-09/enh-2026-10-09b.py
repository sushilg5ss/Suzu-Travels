#!/usr/bin/env python3
"""Homepage hero film v2 — 9 Oct 2026 (nz layer). Usage: python3 enh-2026-10-09b.py live.html after.html
- 11-scene "Bharat Darshan" film (was 8): Himachal (snow play) · Spiti · Kasol · Kashmir (Suzu guests, Pahalgam) ·
  Ladakh (Suzu biker, Pangong) · Sikkim · Uttarakhand · Rajasthan · Goa · Kerala · Andaman. 66 s loop, 6 s per scene.
- New film files suzu-film2-{16x9,9x16}.{mp4,webm,jpg} (old suzu-film-* files stay on the server for rollback).
- nz-data: 3 new slides + Devanagari calligraphy paths (स्पीति, कसोल, सिक्किम shaped with HarfBuzz from Tiro Devanagari Hindi).
- Rail: 3 new destination dots; Himachal dot thumbnail now the snow-play photo (was the Spiti poster).
"""
import sys, re, json, html as H
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
assert 'suzu-film2-' not in s, 'already applied'
CAL = json.load(open('/home/claude/hp/deva_paths_v2.json', encoding='utf-8'))
U = 'https://suzutravels.com/wp-content/uploads/'
NEW = {
 'spiti':  dict(key='spiti', name='Spiti', hi='स्पीति', line='Key Monastery, Chandratal and the winter white desert', chip='6 trips · from ₹22,499', url='https://suzutravels.com/destination/spiti-valley-tour-packages/', thumb=U+'2026/04/Spiti_-768x512.webp'),
 'kasol':  dict(key='kasol', name='Kasol', hi='कसोल', line='Parvati river, pine forests and Kheerganga trails', chip='Custom trips', url='https://suzutravels.com/kasol-trip-plan/', thumb=U+'2026/10/parvati-valley-kasol-768x513.webp'),
 'sikkim': dict(key='sikkim', name='Sikkim', hi='सिक्किम', line='Kanchenjunga sunrises, Gangtok and Gurudongmar', chip='Plan with us', url='https://suzutravels.com/india-trip-planner/', thumb=U+'2026/10/kanchenjunga-sunrise-sikkim-768x512.webp'),
}
ORDER = ['himachal','spiti','kasol','kashmir','ladakh','sikkim','uttarakhand','rajasthan','goa','kerala','andaman']

# ---- nz-data
m = re.search(r'(<script[^>]*id="nz-data"[^>]*>)(.*?)(</script>)', s, re.S)
D = json.loads(m.group(2))
old = {x['key']: x for x in D['slides']}
D['slides'] = [old[k] if k in old else {kk: v for kk, v in NEW[k].items() if kk != 'thumb'} for k in ORDER]
for k in NEW: D['cal'][k] = CAL[k]
for cut in ('l', 'p'):
    for kk in D['film'][cut]: D['film'][cut][kk] = D['film'][cut][kk].replace('suzu-film-', 'suzu-film2-')
s = s[:m.start(2)] + json.dumps(D, ensure_ascii=False) + s[m.end(2):]

# ---- rail dots
def dot(k, cur='false'):
    x = NEW[k]
    return ('<button class="nz-dot" type="button" aria-label="Go to %s" aria-current="%s"><img src="%s" alt="" loading="lazy"><span>%s</span><span class="d" lang="hi">%s</span><i class="bar"></i></button>' % (H.escape(x['name']), cur, x['thumb'], H.escape(x['name']), x['hi']))
def after_dot(name):
    i = s.index('aria-label="Go to %s"' % name); j = s.index('</button>', i) + len('</button>'); return j
j = after_dot('Himachal'); s = s[:j] + dot('spiti') + dot('kasol') + s[j:]
j = after_dot('Ladakh');   s = s[:j] + dot('sikkim') + s[j:]
# Himachal dot thumbnail → snow play (the Spiti poster now belongs to the Spiti dot)
i = s.index('aria-label="Go to Himachal"'); j = s.index('>', s.index('<img', i))
seg = s[i:j]; assert 'Spiti_-768x512.webp' in seg
s = s[:i] + seg.replace(U+'2026/04/Spiti_-768x512.webp', U+'2026/10/family-snowball-fight-falling-snow-768x512.webp') + s[j:]

# ---- film file names everywhere (poster <picture>, boot script, sources)
n = s.count('suzu-film-'); s = s.replace('suzu-film-', 'suzu-film2-')

# ---- mp4 first (H.264 files are the smaller encode of this film); webm stays as fallback
a='<source src="suzu-film2-\'+k+\'.webm?v=1" type="video/webm"><source src="suzu-film2-\'+k+\'.mp4?v=1" type="video/mp4">'
b='<source src="suzu-film2-\'+k+\'.mp4?v=1" type="video/mp4"><source src="suzu-film2-\'+k+\'.webm?v=1" type="video/webm">'
assert s.count(a)==1; s=s.replace(a,b)
open(dst, 'w', encoding='utf-8').write(s)
print('ok slides', len(D['slides']), 'cal', len(D['cal']), 'film refs renamed', n, 'dots', s.count('class="nz-dot"'))
