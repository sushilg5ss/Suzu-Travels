#!/usr/bin/env python3
"""Compare a LIVE page with the local build: visible text + key attributes (href/src/id/class/data-*) + JSON-LD parse.

    python3 tools/cmp_live.py <slug> [--url https://suzutravels.com/...]      (URL defaults to live.json path)

Prints TEXT DIFFS / ATTR DIFFS (expect 0 and 0) and the JSON-LD types found. Fetches with a cache-busting ?v= so WP Rocket's
cached copy is bypassed; run once more without it (--plain) to confirm the cache was purged too.
"""
import difflib, html, json, pathlib, random, re, sys, time, urllib.error, urllib.request
from html.parser import HTMLParser

KIT = pathlib.Path(__file__).resolve().parents[1]
KEEP = ("href", "src", "data-src", "poster", "id", "class", "data-band", "data-state", "data-status", "data-m", "data-fa")


class P(HTMLParser):
    def __init__(s):
        super().__init__()
        s.t, s.a, s.skip = [], [], 0

    def handle_starttag(s, tag, attrs):
        if tag in ("script", "style"):
            s.skip += 1
        for k, v in attrs:
            if k in KEEP and v:
                s.a.append(f"{tag}.{k}={v}")

    def handle_endtag(s, tag):
        if tag in ("script", "style"):
            s.skip -= 1

    def handle_data(s, d):
        if not s.skip and d.strip():
            s.t.append(d.strip())


def norm(x):
    x = html.unescape(x)
    for a, b in [("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), ("…", "..."), ("×", "x"), ("′", "'"), ("″", '"'), ("&#038;", "&")]:
        x = x.replace(a, b)
    return re.sub(r"\s+", " ", x)


def region(h):
    """From <div class="szm"> to the end of the page's own JSON-LD script (or the end of the document)."""
    i = h.find('<div class="szm">')
    if i < 0:
        raise SystemExit("no .szm block found on the live page")
    k = h.find("application/ld+json", i)
    return h[i:(h.find("</script>", k) + 9) if k > 0 else len(h)]


CHALLENGE = "Checking your browser"


def fetch(url, tries=4, wait=120):
    """GET a live page. Hostinger's bot protection answers a burst of requests from one IP with a 403
    "Checking your browser" page for some minutes. That is NOT a page fault and NOT drift: wait and retry,
    then exit with code 3 and a clear message (never re-upload a page because of it)."""
    for n in range(1, tries + 1):
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (SuzuMountainQA)"})
        try:
            body, code = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace"), 200
        except urllib.error.HTTPError as e:
            body, code = e.read().decode("utf-8", "replace"), e.code
        if CHALLENGE not in body and code == 200:
            return body
        if CHALLENGE not in body:
            raise SystemExit(f"HTTP {code} for {url}: a real error (not the bot challenge). Check the page in WordPress.")
        if n < tries:
            print(f"bot challenge (HTTP {code}) — waiting {wait} s, try {n + 1}/{tries}", file=sys.stderr)
            time.sleep(wait)
    print(f"BOT CHALLENGE: Hostinger is still challenging this IP for {url}. Not a page fault and not drift: "
          "do not re-upload. Re-run cmp_live later in the run; if it persists, log it and verify with wp_get_page.")
    raise SystemExit(3)


def main():
    slug = sys.argv[1]
    live = json.loads((KIT / "live.json").read_text())
    url = sys.argv[sys.argv.index("--url") + 1] if "--url" in sys.argv else "https://suzutravels.com" + live[slug]["path"]
    if "--plain" not in sys.argv:
        url += ("&" if "?" in url else "?") + f"v={random.randint(10**6, 10**7)}"
    lh = fetch(url)
    src = (KIT / "out" / f"{slug}.min.html").read_text(encoding="utf-8")
    ps, pl = P(), P()
    ps.feed(src[src.find('<div class="szm">'):])
    pl.feed(region(lh))
    ts, tl = [norm(x) for x in ps.t], [norm(x) for x in pl.t]
    d = [l for l in difflib.unified_diff(ts, tl, lineterm="", n=0) if not l.startswith(("---", "+++", "@@"))]
    print(url)
    print("TEXT DIFFS:", len(d))
    print("\n".join(d[:40]))
    aa, al = [norm(x) for x in ps.a], [norm(x) for x in pl.a]
    d2 = [l for l in difflib.unified_diff(aa, al, lineterm="", n=0) if not l.startswith(("---", "+++", "@@"))]
    print("ATTR DIFFS:", len(d2))
    print("\n".join(d2[:40]))
    print("H1 count:", len(re.findall(r"<h1[\s>]", lh)), "| robots:", (re.search(r'<meta name="robots" content="([^"]*)"', lh) or [None, "?"])[1],
          "| title:", (re.search(r"<title>(.*?)</title>", lh, re.S) or [None, "?"])[1].strip()[:90])
    for m in re.finditer(r'<script type="application/ld\+json"[^>]*>(.*?)</script>', region(lh), re.S):
        try:
            j = json.loads(m.group(1))
            print("page JSON-LD ok:", [g.get("@type") for g in j.get("@graph", [j])])
        except Exception as ex:
            print("JSON-LD PARSE ERROR:", ex)


if __name__ == "__main__":
    main()
