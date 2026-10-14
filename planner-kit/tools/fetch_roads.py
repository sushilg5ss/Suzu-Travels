#!/usr/bin/env python3
"""Build data/roads.json: road km + drive minutes for every place pair (OSRM table) and simplified
road geometry for the legs a traveller can realistically drive in one day (k nearest + hub legs).
Re-run whenever data/places.py changes:  python3 tools/fetch_roads.py
OSRM demo server: be polite (1 request at a time, small sleeps). Output is cached in data/.osrm_cache.json.
"""
import json, os, sys, time, math, urllib.request
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'data'))
from places import PLACES

BASE = 'https://router.project-osrm.org'
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, '..', 'data', '.osrm_cache.json')
OUT = os.path.join(HERE, '..', 'data', 'roads.json')
cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}

def get(url):
    if url in cache: return cache[url]
    for i in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'SuzuTripPlanner/0.1 (info@suzutravels.com)'}), timeout=60) as r:
                d = json.loads(r.read().decode())
            cache[url] = d
            if len(cache) % 20 == 0: json.dump(cache, open(CACHE, 'w'))
            time.sleep(0.35)
            return d
        except Exception as e:
            print('retry', i, e, file=sys.stderr); time.sleep(2 + i * 3)
    raise SystemExit('OSRM failed: ' + url)

def dp(pts, tol):
    if len(pts) < 3: return pts
    a, b = pts[0], pts[-1]; dmax, idx = 0, 0
    for i in range(1, len(pts) - 1):
        p = pts[i]
        dx, dy = b[0] - a[0], b[1] - a[1]
        if dx == dy == 0: d = math.hypot(p[0] - a[0], p[1] - a[1])
        else:
            t = max(0, min(1, ((p[0] - a[0]) * dx + (p[1] - a[1]) * dy) / (dx * dx + dy * dy)))
            d = math.hypot(p[0] - (a[0] + t * dx), p[1] - (a[1] + t * dy))
        if d > dmax: dmax, idx = d, i
    if dmax > tol: return dp(pts[:idx + 1], tol)[:-1] + dp(pts[idx:], tol)
    return [a, b]

def enc(pts):  # Google polyline, precision 5, points as (lat, lon)
    out, plat, plon = [], 0, 0
    for lat, lon in pts:
        ilat, ilon = round(lat * 1e5), round(lon * 1e5)
        for v in (ilat - plat, ilon - plon):
            v = ~(v << 1) if v < 0 else (v << 1)
            while v >= 0x20: out.append(chr((0x20 | (v & 0x1f)) + 63)); v >>= 5
            out.append(chr(v + 63))
        plat, plon = ilat, ilon
    return ''.join(out)

ids = [p['id'] for p in PLACES]
coords = ';'.join('%.5f,%.5f' % (p['lon'], p['lat']) for p in PLACES)
t = get(BASE + '/table/v1/driving/' + coords + '?annotations=distance,duration')
km = [[round((x or 0) / 1000) for x in row] for row in t['distances']]
mins = [[round((x or 0) / 60) for x in row] for row in t['durations']]
snap = [round(w['distance']) for w in t['sources']]
for i, s in enumerate(snap):
    if s > 2000: print('WARN snapped far:', ids[i], s, 'm', file=sys.stderr)

# legs that get geometry
n = len(ids); pairs = set()
for i in range(n):
    order = sorted((km[i][j], j) for j in range(n) if j != i)
    for _, j in order[:9]: pairs.add(tuple(sorted((i, j))))
    if PLACES[i]['kind'] == 'hub':
        for d, j in order:
            if d <= 700: pairs.add(tuple(sorted((i, j))))
extra = os.environ.get('EXTRA_LEGS', '')  # "a-b,c-d"
for e in filter(None, extra.split(',')):
    a, b = e.split('-'); pairs.add(tuple(sorted((ids.index(a), ids.index(b)))))
pairs = sorted(pairs)
print('legs with geometry:', len(pairs), file=sys.stderr)
geo = {}
for k, (i, j) in enumerate(pairs):
    a, b = PLACES[i], PLACES[j]
    r = get(BASE + '/route/v1/driving/%.5f,%.5f;%.5f,%.5f?overview=full&geometries=geojson' % (a['lon'], a['lat'], b['lon'], b['lat']))
    pts = [(c[1], c[0]) for c in r['routes'][0]['geometry']['coordinates']]
    tol = 0.004 if km[i][j] > 150 else 0.002
    geo[ids[i] + '|' + ids[j]] = enc(dp(pts, tol))
    if k % 25 == 0: print(k, '/', len(pairs), file=sys.stderr)
json.dump(cache, open(CACHE, 'w'))
json.dump({'ids': ids, 'km': km, 'min': mins, 'geo': geo, 'src': 'OSRM (OpenStreetMap) ' + time.strftime('%Y-%m-%d')},
          open(OUT, 'w'), separators=(',', ':'))
print('wrote', OUT, os.path.getsize(OUT), 'bytes', file=sys.stderr)
