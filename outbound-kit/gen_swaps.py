#!/usr/bin/env python3
"""Build find/replace pairs that swap the green route-map videos/posters for real photos
on the 9 outbound country pages and the 3 inbound pages. Output: swaps.json
[{id, find, replace, expected}]"""
import json, re, sys
from slides import slideshow

M = json.load(open('photos/wp_map.json'))
U = 'https://suzutravels.com/wp-content/uploads/'

def med(slug):
    return M[slug].get('med') or M[slug]['url']

COUNTRY = {  # page id, html file, slug in suzu-intl, photo keys
    'nepal': (11355, 'c-nepal.html', 'nepal'),
    'bhutan': (11362, 'c-bhutan.html', 'bhutan'),
    'srilanka': (11364, 'c-sri-lanka.html', 'sri-lanka'),
    'maldives': (11366, 'c-maldives.html', 'maldives'),
    'thailand': (11368, 'c-thailand.html', 'thailand'),
    'singapore': (11370, 'c-singapore.html', 'singapore'),
    'malaysia': (11372, 'c-malaysia.html', 'malaysia'),
    'vietnam': (11374, 'c-vietnam.html', 'vietnam'),
    'bali': (11376, 'c-bali.html', 'bali'),
}
NEPAL_GUEST = [(U + '2026/10/patan-durbar-square-temples.webp', 'Patan Durbar Square temples, Lalitpur, on a Suzu Travels Nepal tour', 'Patan Durbar Square · our guests'),
               (U + '2026/10/nepal-pagoda-group-tour.webp', 'Suzu Travels group at a pagoda temple in Nepal', 'Our group in Nepal')]

def video_div(t):
    m = re.search(r'<div class="sx-media"><video.*?</video></div>', t, re.S)
    return m.group(0) if m else None

swaps = []
for key, (pid, f, isl) in COUNTRY.items():
    t = open(f).read()
    v = video_div(t)
    items = [(M[f'{key}-1']['url'], M[f'{key}-1']['alt'], M[f'{key}-1']['cap']),
             (M[f'{key}-2']['url'], M[f'{key}-2']['alt'], M[f'{key}-2']['cap'])]
    if key == 'nepal':
        items += NEPAL_GUEST
    if v:
        swaps.append({'id': pid, 'find': v, 'replace': slideshow(items, M[f'{key}-1']['cap']), 'expected': 1})
    # explore-grid posters on this page -> real photos (all 8 others)
    for k2, (_, _, isl2) in COUNTRY.items():
        poster = f'{U}suzu-intl/suzu-intl-{isl2}-poster.webp'
        n = t.count(poster) - (1 if (v and poster in v) else 0)
        if n > 0:
            swaps.append({'id': pid, 'find': poster, 'replace': med(f'{k2}-1'), 'expected': n})

INBOUND = {
    11411: ('india.html', [('india-hero', None), ('india-jaipur', None), ('kashmir', None), ('india-himalaya', None), ('goldentemple', None)]),
    11412: ('golden-triangle-tour.html', [('india-hero', None), ('india-jaipur', None), ('humayun', None), ('amer', None)]),
    11413: ('char-dham-yatra-for-nri.html', [('chardham', None), ('rishikesh', None), ('india-himalaya', None)]),
}
POSTER_SWAP = {'golden-triangle': U + '2026/09/taj-mahal-agra-golden-triangle-tour.webp',
               'char-dham': U + '2026/05/Char-Dham-Yatra-scaled.webp',
               'india-tours': U + '2026/09/guests/golden-triangle-tour-guests-taj-mahal-agra.webp'}
for pid, (f, keys) in INBOUND.items():
    t = open(f).read()
    v = video_div(t)
    items = [(M[k]['url'], M[k]['alt'], M[k]['cap']) for k, _ in keys if k in M]
    if v:
        swaps.append({'id': pid, 'find': v, 'replace': slideshow(items, items[0][2]), 'expected': 1})
    for slug, rep in POSTER_SWAP.items():
        poster = f'{U}suzu-intl/suzu-intl-{slug}-poster.webp'
        n = t.count(poster) - (1 if (v and poster in v) else 0)
        if n > 0:
            swaps.append({'id': pid, 'find': poster, 'replace': rep, 'expected': n})

json.dump(swaps, open('swaps.json', 'w'), indent=1, ensure_ascii=False)
for s in swaps:
    print(s['id'], s['expected'], s['find'][:70], '->', s['replace'][:60])
