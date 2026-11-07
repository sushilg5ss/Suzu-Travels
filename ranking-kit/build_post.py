#!/usr/bin/env python3
"""python3 build_post.py spec_shimla  -> out/<slug>.html (one line) + /tmp/pk-prev/b-<slug>.html (preview in a live post shell)"""
import importlib, json, os, re, sys, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import blogkit as K

mod = importlib.import_module(sys.argv[1])
S = mod.SPEC
if S.get("photo_pick"):
    pool = {p["id"]: p for sl in S["photo_pick"]["slugs"] for p in K.wp_items(sl)}
    S["photos"] = [dict(pool[i], role=r) for i, r in S["photo_pick"]["ids"]]
else:
    S["photos"] = K.wp_items(S.get("photo_slug", S["slug"]))
h = K.render(S)
for bad in ["24/7", "24x7", "24×7", "most trusted", "best DMC", "verified driver", "vetted driver", "No.1", "guaranteed", "Most asked", "Most booked"]:
    assert bad.lower() not in re.sub(r"<[^>]+>", " ", h).lower(), bad
os.makedirs("out", exist_ok=True)
open(f"out/{S['slug']}.html", "w").write(h)
json.dump({k: S[k] for k in ("slug", "title", "seo_title", "seo_desc", "focus")} | {"hero_id": next((p["id"] for p in S["photos"] if p["role"] == "hero"), None)},
          open(f"out/{S['slug']}.json", "w"), ensure_ascii=False)
shell_f = "/tmp/pk-prev/post-shell.html"
if not os.path.exists(shell_f):
    sh = urllib.request.urlopen(urllib.request.Request("https://suzutravels.com/kufri-snowfall/", headers={"User-Agent": "Mozilla/5.0"}), timeout=60).read().decode()
    sh = re.sub(r'<script(?![^>]*application/ld\+json)[^>]*>.*?</script>', '', sh, flags=re.S)
    sh = re.sub(r'\ssrc="data:image/svg\+xml[^"]*"', '', sh).replace('data-lazy-src=', 'src=').replace('data-lazy-srcset=', 'srcset=')
    sh = sh.replace('<head>', '<head><base href="https://suzutravels.com/kufri-snowfall/">', 1)
    open(shell_f, "w").write(sh)
sh = open(shell_f).read()
i = sh.find('class="article-body'); i = sh.find('>', i) + 1
depth, k = 1, i
for m in re.finditer(r'<(/?)div\b', sh[i:]):
    depth += -1 if m.group(1) else 1
    if depth == 0:
        k = i + m.start(); break
j = k
prev = sh[:i] + h.replace("fetch('/suzu-snow.php')", "fetch('https://suzutravels.com/suzu-snow.php')") + sh[j:]
prev = re.sub(r'<h1[^>]*>.*?</h1>', f'<h1 class="entry-title">{S["title"]}</h1>', prev, count=1, flags=re.S)
open(f"/tmp/pk-prev/b-{S['slug']}.html", "w").write(prev)
print(S["slug"], len(h), "bytes;", {r: sum(1 for p in S["photos"] if p["role"] == r) for r in ("hero", "fig", "g")})
