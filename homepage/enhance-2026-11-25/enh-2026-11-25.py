#!/usr/bin/env python3
"""Homepage Enhancement 2026-11-25 night.
1) ONE shared weather-feed request. Five blocks used to fetch /suzu-weather-feed.json separately
   (nzw marquee on load + snow tile, Himachal-vs-Kashmir compare, region weather, trip-sheet route
   weather when scrolled/opened). New tiny <script id="nz-wxf-js"> defines window.nzWxFeed(): one
   memoised fetch (same ?h=<UTC hour> URL + cache:'default' as nzw, 20-min TTL so nzw's 30-min
   refresh still re-fetches, reset on error). All five callers now use it (nzw keeps its own fetch
   as fallback if the helper is missing, and its /suzu-weather.php fallback is unchanged).
2) +11 Explore links to pages published 24-25 Nov (all 200, index, self-canonical).
Usage: python3 enh-2026-11-25.py live.html after.html
"""
import sys, re

src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
assert 'nz-wxf-js' not in s, 'already applied'
W = 'https://suzutravels.com/'

def block(id_):
    a = s.find('<script id="%s">' % id_); assert a > 0, id_
    b = s.find('</script>', a); return a, b

# ---------- 1) shared weather feed ----------
HELPER = '''<script id="nz-wxf-js">
/* nz-wxf 2026-11-25: one shared fetch of /suzu-weather-feed.json for every weather block (nzw marquee, snow tile, H-vs-K compare, region weather, trip-sheet route weather). Same URL as nzw (?h=UTC hour, cache default); 20-min memo; cleared on error. */
(function(){var P=null,T=0;
window.nzWxFeed=function(){var n=Date.now();if(P&&n-T<12e5)return P;T=n;
 var h=new Date().toISOString().slice(0,13).replace(/\\D/g,'');
 P=fetch('/suzu-weather-feed.json?h='+h,{cache:'default'}).then(function(r){if(!r.ok)throw new Error(r.status);return r.json()});
 P.catch(function(){P=null});return P};
})();
</script>
'''
a, _ = block('nz-hk-wx-js')
s = s[:a] + HELPER + s[a:]

OLDX = "fetch('/suzu-weather-feed.json').then(function(x){if(!x.ok)throw new Error(x.status);return x.json()})"
OLDR = "fetch('/suzu-weather-feed.json').then(function(r){if(!r.ok)throw new Error(r.status);return r.json()})"
NEW = "window.nzWxFeed()"
done = 0
for id_, old in [('nz-hk-wx-js', OLDX), ('nz-rwx-js', OLDX), ('nz-xp-live-js', OLDX), ('suzu-nature-2026-10-js', OLDR)]:
    a, b = block(id_)
    seg = s[a:b]
    assert seg.count(old) == 1, (id_, seg.count(old))
    s = s[:a] + seg.replace(old, NEW) + s[b:]
    done += 1
# nzw widget: use the shared promise, keep its own fetch as fallback
OLDW = "fetch(FEED+'?h='+h,{cache:'default'}).then(function(r){if(!r.ok)throw r.status;return r.json()})"
NEWW = "(window.nzWxFeed?window.nzWxFeed():fetch(FEED+'?h='+h,{cache:'default'}).then(function(r){if(!r.ok)throw r.status;return r.json()}))"
a, b = block('nzw-js'); seg = s[a:b]
assert seg.count(OLDW) == 1
s = s[:a] + seg.replace(OLDW, NEWW) + s[b:]
done += 1
assert done == 5
assert s.count("fetch('/suzu-weather-feed.json')") == 0

# ---------- 2) Explore links ----------
ADD = [
    ('More activities', [('adventure/treks-near-shimla/', 'Treks near Shimla'),
                         ('adventure/shali-tibba-trek/', 'Shali Tibba trek, Shimla')]),
    ('More peaks, gear &amp; safety guides', [('mountains-of-india/nilkantha/', 'Neelkanth Peak, Badrinath')]),
    ('More Kashmir guides', [('trekking-vs-road-trips-in-ladakh-10-key-differences-every-traveller-should-know/', 'Ladakh: trek or road trip?')]),
    ('Temple, Jyotirlinga &amp; Char Dham guides', [('pilgrimage-tours/jagannath-puri/', 'Jagannath Puri Temple')]),
    ('India guides for overseas guests', [('india-tours/jaisalmer/', 'Jaisalmer travel guide')]),
    ('Kerala &amp; Rajasthan guides', [('mehrangarh-fort/', 'Mehrangarh Fort, Jodhpur'),
                                     ('jaigarh-fort/', 'Jaigarh Fort, Jaipur'),
                                     ('christmas-in-kerala/', 'Christmas in Kerala')]),
    ('More cab routes &amp; city taxis', [('cabs/dalhousie-taxi-service/', 'Dalhousie taxi service')]),
    ('More countries', [('kenya-tour-packages/', 'Kenya')]),
]
x0 = s.find('id="nz-explore"'); x1 = s.find('</section>', x0)
n = 0
for summ, items in ADD:
    m = re.compile(r'<summary>' + re.escape(summ) + r' <span>\((\d+)\)</span></summary>').search(s, x0, x1)
    assert m, summ
    cnt = int(m.group(1))
    e = s.find('</ul></details>', m.end()); assert 0 < e < x1
    lis = ''
    for path, txt in items:
        assert 'href="' + W + path + '"' not in s, path
        lis += '<li><a href="' + W + path + '">' + txt + '</a></li>'
        n += 1
    s = s[:e] + lis + s[e:]
    s = s[:m.start(1)] + str(cnt + len(items)) + s[m.end(1):]
    x1 = s.find('</section>', x0)
assert n == 11
open(dst, 'w', encoding='utf-8').write(s)
print('ok: 5 feed callers shared,', n, 'links')
