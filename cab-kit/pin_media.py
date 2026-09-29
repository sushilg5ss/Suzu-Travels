#!/usr/bin/env python3
"""Pin a page's freshly committed media in media.json.
   python3 pin_media.py <slug> <full-commit-sha>
Adds/updates media.json[<slug>]["hero"|"route"] for every file present in media/<slug>/."""
import json, sys, pathlib
KIT = pathlib.Path(__file__).resolve().parent
slug, sha = sys.argv[1], sys.argv[2]
assert len(sha) == 40, "pass the FULL 40-char commit SHA"
base = f"https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@{sha}/cab-kit/media/{slug}/"
m = json.loads((KIT / "media.json").read_text())
d = KIT / "media" / slug
entry = m.get(slug, {})
for kind, w, h in (("hero", 1600, 900), ("route", 1280, 720)):
    if (d / f"{kind}.mp4").exists():
        entry[kind] = {"mp4": base + f"{kind}.mp4", "webm": base + f"{kind}.webm",
                       "poster": base + f"{kind}-poster.webp", "w": w, "h": h}
m[slug] = entry
(KIT / "media.json").write_text(json.dumps(m, indent=1, ensure_ascii=False) + "\n")
print(json.dumps(entry, indent=1))
