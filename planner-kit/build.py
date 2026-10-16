#!/usr/bin/env python3
"""Build the Suzu Trip Planner into one static file: dist/plan-your-trip/index.html
   python3 build.py            -> dist/plan-your-trip/index.html (+ prints size and SHA-256)
The page is self-contained (CSS, JS and data inline) so it deploys as ONE file to
public_html/plan-your-trip/index.html on Hostinger (LiteSpeed serves it without PHP)."""
import json, os, sys, hashlib, re, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'data'))
from places import PLACES

def rd(p): return open(os.path.join(HERE, p), encoding='utf-8').read()
data = {
    'v': '0.4',
    'built': time.strftime('%Y-%m-%d'),
    'places': PLACES,
    'roads': json.loads(rd('data/roads.json')),
    'rates': json.loads(rd('data/rates.json')),
    'templates': json.loads(rd('data/templates.json')),
}
ids = {p['id'] for p in PLACES}
assert data['roads']['ids'] == [p['id'] for p in PLACES], 'roads.json is stale: run tools/fetch_roads.py'
for t in data['templates']:
    for s in t['stops']: assert s[0] in ids, (t['id'], s)
    assert t['start'] in ids and t['end'] in ids, t['id']
blob = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
src = rd('src/index.html')
# FAQPage JSON-LD generated from the visible FAQ (<details class="fq">) so schema and page never drift apart
faq = [{'@type': 'Question', 'name': re.sub('<[^>]+>', '', q).strip(), 'acceptedAnswer': {'@type': 'Answer', 'text': re.sub('<[^>]+>', '', a).strip()}}
       for q, a in re.findall(r'<details class="fq"><summary>(.*?)</summary><p>(.*?)</p></details>', src, re.S)]
assert len(faq) >= 5, 'FAQ not found in src/index.html'
src = src.replace('"@graph":[', '"@graph":[' + json.dumps({'@type': 'FAQPage', 'mainEntity': faq}, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/') + ',', 1)
html = src.replace('/*__CSS__*/', rd('src/planner.css')).replace('/*__JS__*/', rd('src/planner.js')).replace('/*__DATA__*/', blob)
out = os.path.join(HERE, 'dist', 'plan-your-trip')
os.makedirs(out, exist_ok=True)
fn = os.path.join(out, 'index.html')
open(fn, 'w', encoding='utf-8').write(html)
b = html.encode('utf-8')
print(fn, len(b), 'bytes, sha256', hashlib.sha256(b).hexdigest()[:16])
