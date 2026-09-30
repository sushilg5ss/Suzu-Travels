#!/usr/bin/env python3
"""Search Wikimedia Commons for freely-licensed photos and download them with attribution.

usage: commons.py OUT_DIR "query 1" "query 2" ... [--n 6] [--min-width 1400]
Writes OUT_DIR/<slug>.jpg and appends to OUT_DIR/credits.json
Only keeps licenses that allow commercial reuse (CC0, PD, CC BY, CC BY-SA).
"""
import json, os, re, sys, time, urllib.error, urllib.parse, urllib.request

UA = {"User-Agent": "SuzuTravelsBharatDarshan/1.0 (https://suzutravels.com; info@suzutravels.com)"}
API = "https://commons.wikimedia.org/w/api.php"
OK_LIC = re.compile(r"^(cc0|pd|public domain|cc by(-sa)? ?[0-9.]*|cc-by(-sa)?-[0-9.]+)", re.I)


def get(url, tries=5):
    """curl with backoff — Wikimedia rate-limits urllib hard; curl + a descriptive UA works."""
    import subprocess
    for t in range(tries):
        r = subprocess.run(["curl", "-s", "-L", "-A", UA["User-Agent"], "-w", "\n%{http_code}", url],
                           capture_output=True)
        body, _, code = r.stdout.rpartition(b"\n")
        if code == b"200":
            return body
        if code in (b"429", b"503") and t < tries - 1:
            time.sleep(12 * (t + 1)); continue
        raise RuntimeError(f"HTTP {code.decode()} for {url}")


def search(q, n, min_w):
    params = {
        "action": "query", "format": "json", "generator": "search",
        "gsrsearch": f"filetype:bitmap {q}", "gsrnamespace": 6, "gsrlimit": 30,
        "prop": "imageinfo", "iiprop": "url|size|extmetadata|mime", "iiurlwidth": 3840,
    }
    d = json.loads(get(API + "?" + urllib.parse.urlencode(params)))
    pages = sorted(d.get("query", {}).get("pages", {}).values(), key=lambda p: p.get("index", 99))
    out = []
    for p in pages:
        ii = (p.get("imageinfo") or [{}])[0]
        if ii.get("mime") not in ("image/jpeg", "image/png", "image/webp"):
            continue
        if ii.get("width", 0) < min_w:
            continue
        md = ii.get("extmetadata", {})
        lic = md.get("LicenseShortName", {}).get("value", "")
        if not OK_LIC.match(lic.strip()):
            continue
        artist = re.sub("<[^>]+>", "", md.get("Artist", {}).get("value", "")).strip()
        out.append({
            "title": p["title"], "url": ii.get("thumburl") or ii["url"], "page": ii.get("descriptionurl"),
            "w": ii["width"], "h": ii["height"], "license": lic, "artist": artist[:120],
        })
        if len(out) >= n:
            break
    return out


def main():
    args = sys.argv[1:]
    n, min_w = 6, 1400
    if "--n" in args:
        i = args.index("--n"); n = int(args[i + 1]); del args[i:i + 2]
    if "--min-width" in args:
        i = args.index("--min-width"); min_w = int(args[i + 1]); del args[i:i + 2]
    out_dir, queries = args[0], args[1:]
    os.makedirs(out_dir, exist_ok=True)
    cred_path = os.path.join(out_dir, "credits.json")
    credits = json.load(open(cred_path)) if os.path.exists(cred_path) else []
    seen = {c["title"] for c in credits}
    for q in queries:
        try:
            found = search(q, n, min_w)
        except Exception as e:  # rate-limited search: skip this query, keep the rest
            print("search failed", q, e); time.sleep(20); continue
        for k, it in enumerate(found):
            if it["title"] in seen:
                continue
            slug = re.sub(r"[^a-z0-9]+", "-", q.lower()).strip("-") + f"-{k+1}"
            ext = ".png" if it["url"].lower().endswith(".png") else ".jpg"
            path = os.path.join(out_dir, slug + ext)
            time.sleep(4)
            try:
                data = get(it["url"]); open(path, "wb").write(data)
            except Exception as e:
                print("skip", it["title"], e); continue
            it["file"] = os.path.basename(path); it["query"] = q
            credits.append(it); seen.add(it["title"])
            json.dump(credits, open(cred_path, "w"), ensure_ascii=False, indent=1)  # incremental: survives a timeout
            print(f"{it['file']:40s} {it['w']}x{it['h']} {it['license']:12s} {it['title'][:70]}")
    json.dump(credits, open(cred_path, "w"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
