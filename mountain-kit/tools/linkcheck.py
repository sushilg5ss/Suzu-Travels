#!/usr/bin/env python3
"""Check every link, video and poster URL on built pages (the QA "Links" step).

    python3 tools/linkcheck.py <slug> [<slug> ...]      # pages from out/<slug>.min.html
    python3 tools/linkcheck.py --all                    # every page in live.json

- suzutravels.com URLs are fetched 1.2 s apart (Hostinger bot protection), jsDelivr media 0.2 s, other sites 0.3 s.
- If Hostinger answers with its 403 "Checking your browser" page, that is the bot challenge for THIS IP, not a broken
  link: the script stops checking suzutravels.com URLs, says so, and exits 3. Re-run later in the run.
- Other sites that refuse bots (403/429/503) are listed as "blocked to bots" (confirm with WebFetch), not as failures.
Exit codes: 0 all OK · 1 real failures · 3 bot challenge (nothing else failed).
"""
import html, json, pathlib, re, subprocess, sys, tempfile, time
from urllib.parse import urljoin

KIT = pathlib.Path(__file__).resolve().parents[1]
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
CHALLENGE = "Checking your browser"


def urls_of(slug):
    h = (KIT / "out" / f"{slug}.min.html").read_text(encoding="utf-8")
    for _, u in re.findall(r'\b(href|src|data-src|poster)="([^"]+)"', h):
        u = html.unescape(u)
        if u.startswith(("#", "mailto:", "tel:", "data:")) or "wa.me/" in u:
            continue
        yield urljoin("https://suzutravels.com/", u)


def get(u):
    with tempfile.NamedTemporaryFile() as f:
        r = subprocess.run(["curl", "-s", "-L", "--max-redirs", "3", "-m", "40", "-A", UA, "-r", "0-0", "-o", f.name,
                            "-w", "%{http_code} %{url_effective}", u], capture_output=True, text=True)
        body = pathlib.Path(f.name).read_text(encoding="utf-8", errors="replace")[:4000]
    code, _, final = r.stdout.strip().partition(" ")
    return code or "000", final, body


def main():
    args = sys.argv[1:]
    if not args:
        raise SystemExit(__doc__)
    slugs = list(json.loads((KIT / "live.json").read_text())) if args == ["--all"] else args
    pages = {}
    for s in slugs:
        for u in urls_of(s):
            pages.setdefault(u, set()).add(s)
    site = sorted(u for u in pages if "suzutravels.com" in u)
    media = sorted(u for u in pages if "cdn.jsdelivr.net" in u)
    ext = sorted(u for u in pages if u not in site and u not in media)
    print(f"{len(slugs)} page(s) · {len(pages)} unique URLs: {len(site)} site, {len(media)} media, {len(ext)} external")
    fails, blocked, redirects, challenged = [], [], [], False
    for group, gap in ((media, 0.2), (site, 1.2), (ext, 0.3)):
        for u in group:
            if group is site and challenged:
                break
            code, final, body = get(u)
            if group is site and CHALLENGE in body:
                challenged = True
                print(f"BOT CHALLENGE at {u}: Hostinger is challenging this IP. Stopped checking site URLs; re-run later.")
                break
            if code in ("200", "206"):
                if group is site and final.split("#")[0].rstrip("/") != u.split("#")[0].rstrip("/"):
                    redirects.append((u, final))
            elif group is ext and code in ("403", "429", "503", "999"):
                blocked.append((code, u))
            else:
                fails.append((code, u, sorted(pages[u])))
            time.sleep(gap)
    for u, f in redirects:
        print(f"REDIRECT  {u} -> {f}  (link straight to the final URL)")
    for c, u in blocked:
        print(f"BLOCKED TO BOTS ({c})  {u}  — confirm with WebFetch; not a failure")
    for c, u, s in fails:
        print(f"FAIL {c}  {u}  on {', '.join(s)}")
    print(f"RESULT: {len(fails)} failures, {len(redirects)} redirects, {len(blocked)} blocked-to-bots"
          + (", BOT CHALLENGE (site URLs incomplete)" if challenged else ""))
    raise SystemExit(1 if fails else 3 if challenged else 0)


if __name__ == "__main__":
    main()
