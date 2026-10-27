import json, sys, os, time, math, urllib.request
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))  # usage: python3 tools/patch_roads.py <new place id> (adds one place to roads.json without refetching all)
sys.path.insert(0, 'data'); sys.path.insert(0, 'tools')
from places import PLACES
NEW = sys.argv[1]
R = json.load(open('data/roads.json'))
ids = [p['id'] for p in PLACES]
assert NEW not in R['ids'] and [i for i in ids if i != NEW] == R['ids']
ni = ids.index(NEW)
B = 'https://router.project-osrm.org'
def get(u):
    with urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'SuzuTripPlanner/0.1 (info@suzutravels.com)'}), timeout=90) as r: return json.loads(r.read())
coords = ';'.join('%.5f,%.5f' % (p['lon'], p['lat']) for p in PLACES)
a = get(B + '/table/v1/driving/' + coords + '?sources=%d&annotations=distance,duration' % ni); time.sleep(1)
b = get(B + '/table/v1/driving/' + coords + '?destinations=%d&annotations=distance,duration' % ni)
print('snap m', round(a['sources'][0]['distance']))
rowk = [round((x or 0) / 1000) for x in a['distances'][0]]; rowm = [round((x or 0) / 60) for x in a['durations'][0]]
colk = [round((r[0] or 0) / 1000) for r in b['distances']]; colm = [round((r[0] or 0) / 60) for r in b['durations']]
for M, row, col in ((R['km'], rowk, colk), (R['min'], rowm, colm)):
    for i, r in enumerate(M): r.insert(ni, col[i if i < ni else i + 1])
    M.insert(ni, row)
km = R['km']; n = len(ids)
import importlib.util
spec = importlib.util.spec_from_file_location('fr_helpers', 'tools/fetch_roads.py')
src = open('tools/fetch_roads.py').read()
helpers = src[src.index('def dp'):src.index('ids = [p')]
exec(helpers)
order = sorted((km[ni][j], j) for j in range(n) if j != ni)
js = set(j for _, j in order[:9])
for d, j in order:
    if PLACES[j]['kind'] == 'hub' and d <= 700: js.add(j)
for j in sorted(js):
    i1, i2 = sorted((ni, j)); p, q = PLACES[i1], PLACES[i2]
    r = get(B + '/route/v1/driving/%.5f,%.5f;%.5f,%.5f?overview=full&geometries=geojson' % (p['lon'], p['lat'], q['lon'], q['lat'])); time.sleep(0.4)
    pts = [(c[1], c[0]) for c in r['routes'][0]['geometry']['coordinates']]
    R['geo'][ids[i1] + '|' + ids[i2]] = enc(dp(pts, 0.004 if km[i1][i2] > 150 else 0.002))
    print('geo', ids[i1], ids[i2], km[i1][i2], 'km')
R['ids'] = ids
json.dump(R, open('data/roads.json', 'w'), separators=(',', ':'))
print('ok', {x: (km[ni][ids.index(x)], R['min'][ni][ids.index(x)]) for x in ['sonamarg', 'srinagar', 'jammu', 'pahalgam']})
