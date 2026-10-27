#!/usr/bin/env python3
"""Data-only homepage re-sync (idempotent): replace ONLY <script id="tpe-data"> in the LIVE homepage with the
current planner data (places, templates). sync_engine.py is the one-time code patcher (already applied 16 Oct
2026; it no longer matches the live file). Usage: python3 sync_data.py <live_index.html> <out.html>
Then: python3 parity.py live out (PARITY PASS) and node ../tools/test_home.js."""
import json, os, re, sys, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hero_engine as HE
h = open(sys.argv[1], encoding='utf-8').read()
assert 'id="tp-engine"' in h, 'tp-engine missing'
data = json.dumps(HE.DATA, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
pat = r'(<script id="tpe-data" type="application/json">)(.*?)(</script>)'
m = re.findall(pat, h, re.S); assert len(m) == 1, len(m)
h = re.sub(pat, lambda _: m[0][0] + data + m[0][2], h, flags=re.S)
open(sys.argv[2], 'w', encoding='utf-8').write(h)
b = h.encode('utf-8'); print(sys.argv[2], len(b), hashlib.sha256(b).hexdigest())
