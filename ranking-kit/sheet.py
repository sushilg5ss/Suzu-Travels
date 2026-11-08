#!/usr/bin/env python3
"""python3 sheet.py <tag>  — reads /tmp/claude-0/dh/cs-<tag>.json, writes numbered contact sheet cs-<tag>.jpg"""
import io, json, sys, time, urllib.request
from PIL import Image, ImageDraw
tag = sys.argv[1]
items = [x for x in json.load(open(f"/tmp/claude-0/dh/cs-{tag}.json")) if "title" in x]
W, H, cols = 360, 240, 5
rows = (len(items) + cols - 1) // cols
sheet = Image.new("RGB", (cols * W, rows * (H + 30)), "white"); d = ImageDraw.Draw(sheet)
for k, it in enumerate(items):
    it["n"] = k
    x, y = (k % cols) * W, (k // cols) * (H + 30)
    for i in range(3):
        try:
            req = urllib.request.Request(it["thumb"], headers={"User-Agent": "SuzuTravelsPhotoPicker/1.0 (https://suzutravels.com)"})
            im = Image.open(io.BytesIO(urllib.request.urlopen(req, timeout=30).read())).convert("RGB"); im.thumbnail((W, H)); sheet.paste(im, (x, y)); break
        except Exception as e:
            time.sleep(3 * (i + 1))
    d.rectangle([x, y, x + 34, y + 22], fill="black"); d.text((x + 4, y + 4), str(k), fill="yellow")
    d.text((x + 2, y + H + 4), (it["title"][5:48] + " | " + it["lic"])[:58], fill="black")
    print(k, it["title"], "|", it["lic"], "|", it["artist"][:40], f'{it["w"]}x{it["h"]}')
sheet.save(f"/tmp/claude-0/dh/cs-{tag}.jpg", quality=80)
json.dump(items, open(f"/tmp/claude-0/dh/cs-{tag}.json", "w"), ensure_ascii=False)
