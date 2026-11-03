#!/usr/bin/env python3
"""Check every link, video and poster URL on built pages (the QA "Links" step).

    python3 tools/linkcheck.py <slug> [<slug> ...]      # pages from out/<slug>.min.html
    python3 tools/linkcheck.py --all                    # every page in live.json
    python3 tools/linkcheck.py --all --budget 400       # stop cleanly after 400 s (default 480)
    python3 tools/linkcheck.py --all --fresh            # ignore the 7-day cache, check every URL again

- suzutravels.com URLs are fetched 1.2 s apart (Hostinger bot protection), jsDelivr media 0.2 s, other sites 0.3 s.
- If Hostinger answers with its 403 "Checking your browser" page, that is the bot challenge for THIS IP, not a broken
  link: the script stops checking suzutravels.com URLs, says so, and exits 3. Re-run later in the run.
- Other sites that refuse bots (403/429/503) are listed as "blocked to bots" (confirm with WebFetch), not as failures.
- An external URL that will not connect at all (curl 000, usually an SSL chain this container does not trust — several
  *.gov.in sites — or a timeout) is listed as "UNREACHABLE FROM THIS AGENT", not a failure: it is our network, not a
  broken link. Check it with WebFetch/WebSearch before ever removing a source because of this line (v0.2.5, 3 Nov 2026).
- Time budget (v0.2.5, 3 Nov 2026): a full --all run is ~334 URLs and can outlast a scheduled agent's patience, so the
  script stops after `--budget` seconds (default 480), prints what it managed, and exits 4 ("incomplete, re-run").
  URLs that answered 200/206 are remembered in `research/.linkcheck-cache.json` for 7 days and skipped on the next run,
  so two or three runs cover everything without re-fetching what was fine yesterday. `--fresh` ignores the cache.
Exit codes: 0 all OK · 1 real failures · 3 bot challenge (nothing else failed) · 4 budget reached, nothing failed.
"""
import html, json, pathlib, re, subprocess, sys, tempfile, time
from urllib.parse import urljoin

KIT = pathlib.Path(__file__).resolve().parents[1]
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
CHALLENGE = "Checking your browser"
CACHE = KIT / "research" / ".linkcheck-cache.json"
CACHE_DAYS = 7


def urls_of(slug):
    h = (KIT / "out" / f"{slug}.min.html").read_text(encoding="utf-8")
    for _, u in re.findall(r'\b(href|src|data-src|poster)="([^"]+)"', h):
        u = html.unescape(u)
        if u.startswith(("#", "mailto:", "tel:", "data:")) or "wa.me/" in u:
            continue
        yield urljoin("https://suzutravels.com/", u)


def get(u, ranged=True):
    with tempfile.NamedTemporaryFile() as f:
        r = subprocess.run(["curl", "-s", "-L", "--max-redirs", "3", "-m", "40", "-A", UA] + (["-r", "0-0"] if ranged else []) + ["-o", f.name,
                            "-w", "%{http_code} %{url_effective}", u], capture_output=True, text=True)
        body = pathlib.Path(f.name).read_text(encoding="utf-8", errors="replace")[:4000]
    code, _, final = r.stdout.strip().partition(" ")
    return code or "000", final, body


def load_cache(fresh):
    if fresh or not CACHE.exists():
        return {}
    try:
        c = json.loads(CACHE.read_text())
    except Exception:
        return {}
    cut = time.time() - CACHE_DAYS * 86400
    return {u: t for u, t in c.items() if t > cut}


def main():
    args = sys.argv[1:]
    if not args:
        raise SystemExit(__doc__)
    budget = 480.0
    if "--budget" in args:
        i = args.index("--budget")
        budget = float(args[i + 1])
        del args[i:i + 2]
    fresh = "--fresh" in args
    if fresh:
        args.remove("--fresh")
    started = time.time()
    cache = load_cache(fresh)
    if args == ["--all"]:  # every kit-built page in live.json; hand-built pages (11411/11412/11413) have no out/ file
        live = json.loads((KIT / "live.json").read_text())
        slugs = [s for s, v in live.items() if not v.get("hand_built")]
        skipped = [s for s in live if s not in slugs]
        if skipped:
            print(f"skipping hand-built (no out/ build): {', '.join(skipped)}")
    else:
        slugs = args
    pages = {}
    for s in slugs:
        for u in urls_of(s):
            pages.setdefault(u, set()).add(s)
    site = sorted(u for u in pages if "suzutravels.com" in u)
    media = sorted(u for u in pages if "cdn.jsdelivr.net" in u)
    ext = sorted(u for u in pages if u not in site and u not in media)
    cached = sum(1 for u in pages if u in cache)
    print(f"{len(slugs)} page(s) · {len(pages)} unique URLs: {len(site)} site, {len(media)} media, {len(ext)} external"
          + (f" · {cached} still OK from the last {CACHE_DAYS} days (skipped; --fresh to recheck)" if cached else ""),
          flush=True)
    fails, blocked, redirects, challenged = [], [], [], False
    unreachable = []
    unchecked = 0
    for group, gap in ((media, 0.2), (site, 1.2), (ext, 0.3)):
        for u in group:
            if group is site and challenged:
                unchecked += 1
                continue
            if u in cache:
                continue
            if time.time() - started > budget:
                unchecked += 1
                continue
            code, final, body = get(u)
            if group is ext and code == "000":  # connection reset/timeout: some servers drop ranged requests; retry once plain
                time.sleep(3)
                code, final, body = get(u, ranged=False)
            if group is site and CHALLENGE in body:
                challenged = True
                print(f"BOT CHALLENGE at {u}: Hostinger is challenging this IP. Stopped checking site URLs; re-run later.")
                break
            if code in ("200", "206"):
                cache[u] = time.time()
                if group is site and final.split("#")[0].rstrip("/") != u.split("#")[0].rstrip("/"):
                    redirects.append((u, final))
            elif group is ext and code in ("403", "429", "503", "999"):
                blocked.append((code, u))
            elif group is ext and code == "000":
                unreachable.append(u)
            else:
                fails.append((code, u, sorted(pages[u])))
            time.sleep(gap)
    for u, f in redirects:
        print(f"REDIRECT  {u} -> {f}  (link straight to the final URL)")
    for c, u in blocked:
        print(f"BLOCKED TO BOTS ({c})  {u}  — confirm with WebFetch; not a failure")
    for u in unreachable:
        print(f"UNREACHABLE FROM THIS AGENT  {u}  — TLS/connection, not a broken link; confirm with WebFetch")
    for c, u, s in fails:
        print(f"FAIL {c}  {u}  on {', '.join(s)}")
    try:
        CACHE.write_text(json.dumps(cache, indent=0, sort_keys=True))
    except Exception as e:
        print(f"(cache not written: {e})")
    print(f"RESULT: {len(fails)} failures, {len(redirects)} redirects, {len(blocked)} blocked-to-bots, {len(unreachable)} unreachable-from-this-agent"
          + (f", {unchecked} not checked this run (budget {budget:.0f}s / bot challenge) — re-run to finish" if unchecked else "")
          + (", BOT CHALLENGE (site URLs incomplete)" if challenged else ""))
    raise SystemExit(1 if fails else 3 if challenged else 4 if unchecked else 0)


if __name__ == "__main__":
    main()
