#!/usr/bin/env python3
"""Pin the commit that contains a media folder (or the dataset) so pages load it from jsDelivr.
    python3 pin_media.py <media-slug|data> <full-commit-sha>
The commit must already be pushed to origin/pilgrimage. jsDelivr URLs are immutable per commit, so re-pin after every re-render."""
import json, pathlib, sys
KIT = pathlib.Path(__file__).resolve().parent
f = KIT / "media.json"
m = json.loads(f.read_text()) if f.exists() else {}
slug, sha = sys.argv[1], sys.argv[2]
assert len(sha) == 40, "use the full 40-character SHA"
m[slug] = sha
f.write_text(json.dumps(m, indent=1, sort_keys=True) + "\n")
print(f"pinned {slug} -> {sha}")
