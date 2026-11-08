#!/usr/bin/env python3
"""Commons photo picker: python3 commons.py <tag> "query1" "query2" ...
Writes /tmp/claude-0/dh/cs-<tag>.jpg (numbered contact sheet) and /tmp/claude-0/dh/cs-<tag>.json
(list of {n,title,lic,artist,w,h,thumb}). Only CC BY / CC BY-SA / CC0 / PD, landscape-ish, >=1200 px."""
import io, json, re, sys, time, urllib.parse, urllib.request
from PIL import Image, ImageDraw, ImageFont

UA = "SuzuTravelsPhotoPicker/1.0 (https://suzutravels.com)"
API = "https://commons.wikimedia.org/w/api.php"


def get(url, tries=5):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=40) as r:
                return r.read()
        except Exception as e:  # noqa
            print("  wait", e, flush=True)
            if i < tries - 1:
                time.sleep(8 * (i + 1)); continue
            return None


def strip(h):
    return re.sub(r"<[^>]+>", "", h or "").strip()


def ok_lic(l):
    l = (l or "").lower()
    if "nc" in l.split("-") or "-nc" in l or "-nd" in l or "noncommercial" in l or "no deriv" in l:
        return False
    return l.startswith("cc by") or l.startswith("cc-by") or l.startswith("cc0") or "public domain" in l or l == "pd"


def search(q, n=30):
    p = dict(action="query", format="json", generator="search", gsrsearch=q + " filetype:bitmap", gsrnamespace=6,
             gsrlimit=n, prop="imageinfo", iiprop="url|size|extmetadata", iiurlwidth=360)
    raw = get(API + "?" + urllib.parse.urlencode(p))
    if not raw:
        return []
    j = json.loads(raw)
    out = []
    for pg in (j.get("query", {}).get("pages") or {}).values():
        ii = (pg.get("imageinfo") or [{}])[0]
        m = ii.get("extmetadata", {})
        lic = m.get("LicenseShortName", {}).get("value", "")
        w, h = ii.get("width", 0), ii.get("height", 0)
        if not ok_lic(lic) or w < 1200 or h < 700:
            continue
        out.append(dict(title=pg["title"], lic=lic, artist=strip(m.get("Artist", {}).get("value", ""))[:80], w=w, h=h,
                        thumb=ii.get("thumburl"), desc=strip(m.get("ImageDescription", {}).get("value", ""))[:140]))
    return out


def main():
    tag, qs = sys.argv[1], sys.argv[2:]
    seen, items = set(), []
    for q in qs:
        for it in search(q):
            if it["title"] not in seen:
                seen.add(it["title"]); items.append(it)
        time.sleep(1)
    items = items[:40]
    W, H, cols = 360, 240, 5
    rows = (len(items) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * W, rows * (H + 30)), "white")
    d = ImageDraw.Draw(sheet)
    for k, it in enumerate(items):
        it["n"] = k
        try:
            im = Image.open(io.BytesIO(get(it["thumb"]) or b"")).convert("RGB")
            im.thumbnail((W, H))
            x, y = (k % cols) * W, (k // cols) * (H + 30)
            sheet.paste(im, (x, y))
            d.rectangle([x, y, x + 34, y + 22], fill="black")
            d.text((x + 4, y + 4), str(k), fill="yellow")
            d.text((x + 2, y + H + 4), (it["title"][5:50] + " | " + it["lic"])[:58], fill="black")
        except Exception as e:  # noqa
            print("thumb fail", k, e)
        time.sleep(0.3)
    sheet.save(f"/tmp/claude-0/dh/cs-{tag}.jpg", quality=80)
    json.dump(items, open(f"/tmp/claude-0/dh/cs-{tag}.json", "w"), ensure_ascii=False, indent=0)
    for it in items:
        print(it["n"], it["title"], "|", it["lic"], "|", it["artist"][:40], f'{it["w"]}x{it["h"]}')


if __name__ == "__main__":
    main()
