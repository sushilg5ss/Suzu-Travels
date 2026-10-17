#!/usr/bin/env python3
"""Wrap out/<slug>.min.html in the real site theme for screenshots (no WordPress needed).

    python3 tools/preview.py <slug> ["H1 title"]      -> /tmp/pk-prev/<slug>.html   (then: node tools/shots.js /tmp/pk-prev/<slug>.html <slug>)

Uses the live hub https://suzutravels.com/india-tours/ as the theme shell (cached in /tmp/pk-prev/shell.html; delete it
to refresh), swaps the hub's own content for the page, sets the H1 (default: "title" from src/pages/<slug>.json) and removes
the theme's scripts, so WP Rocket's delay-JS cannot swallow clicks in the preview. Theme CSS still loads from the live site.
"""
import json, pathlib, re, sys, urllib.request

KIT = pathlib.Path(__file__).resolve().parents[1]
D = pathlib.Path("/tmp/pk-prev")


def shell():
    f = D / "shell.html"
    if not f.exists():
        D.mkdir(parents=True, exist_ok=True)
        for u in ("https://suzutravels.com/india-tours/", "https://suzutravels.com/mountains-of-india/"):  # 2nd = shell before the hub existed
            try:
                req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 (SuzuPilgrimQA)"})
                f.write_text(urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace"), encoding="utf-8")
                break
            except Exception:
                continue
    return f.read_text(encoding="utf-8")


def main():
    slug = sys.argv[1]
    spec = KIT / "src" / "pages" / f"{slug}.json"
    mf = KIT / "src" / "meta.json"  # optional (pilgrim-kit legacy)
    meta = json.loads(mf.read_text(encoding="utf-8")) if mf.exists() else {}
    title = sys.argv[2] if len(sys.argv) > 2 else (json.loads(spec.read_text(encoding="utf-8"))["title"] if spec.exists() else meta.get(slug, {}).get("title", slug))
    h = shell()
    i = h.find('<div class="szi">')
    if i < 0:
        i = h.find('<div class="szm">')
    start = h.rfind("<style>", 0, i)                      # the kit CSS that opens the hub's content
    k = h.find("IntersectionObserver", i)                  # the kit JS that closes it
    end = h.find("</script>", k) + len("</script>")
    if min(i, start, k) < 0:  # hand-built hub (11411, Sep 2026): swap the whole entry-content body instead (Page Builder, 17 Oct 2026)
        ec = h.find('<div class="entry-content"')
        m_ = h.rfind("</main>")
        if ec < 0 or m_ < 0:
            raise SystemExit("could not find the kit block or the entry-content in the hub shell — delete /tmp/pk-prev/shell.html and retry")
        start = h.find(">", ec) + 1
        end = h.rfind("</div>", 0, h.rfind("</div>", 0, m_))
    page = (KIT / "out" / f"{slug}.min.html").read_text(encoding="utf-8")
    out = h[:start] + "@@PAGE@@" + h[end:]
    out = re.sub(r"<script\b(?![^>]*application/ld\+json)[^>]*>.*?</script>", "", out, flags=re.S)  # theme scripts out
    out = re.sub(r'(<h1 class="entry-title"[^>]*>)(.*?)(</h1>)', lambda m: m.group(1) + title.replace("&", "&amp;") + m.group(3), out, count=1, flags=re.S)
    out = out.replace("@@PAGE@@", page)
    D.mkdir(parents=True, exist_ok=True)
    (D / f"{slug}.html").write_text(out, encoding="utf-8")
    print(D / f"{slug}.html")


if __name__ == "__main__":
    main()
