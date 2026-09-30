#!/usr/bin/env python3
"""Suzu Mountain Kit builder.

    python3 build.py <slug|all> [--force]     reads out/<slug>.html  ->  writes out/<slug>.min.html

Inlines kit.css (minified) at the top and kit.js (minified) where the page has <script>/*KITJS*/</script>, strips comments and
collapses the page to ONE line (WordPress wpautop cannot break it). REFUSES to build when:
  * a placeholder is left ({{...}}, TODO, ___ outside WhatsApp text, lorem)
  * a rupee price appears (₹ / Rs 123 / INR 123) — Suzu never prints its own prices on mountain pages
  * a partner/vendor name or network claim appears (see BANNED), or a link to a competitor operator (COMPETITORS)
  * a known wrong "fact" appears (FACT_TRAPS — see README "Facts to avoid")
  * a link points to a /mountains-of-india/ URL that is not in live.json (no links to unbuilt pages)
  * the page has no HyperFrames video
  * (pages from src/pages/*.json) the SEO title is over 60 characters or the description over 155, or the focus keyword is missing
--force skips the refusal (only for local previews — never publish a forced build).
"""
import json, pathlib, re, sys

KIT = pathlib.Path(__file__).resolve().parent
BANNED = [r"our vendor network", r"partner (?:company|companies|vendor|operator)s?", r"verified vendors", r"authori[sz]ed vendors",
          r"Everest summiteers? on our team", r"our own (?:guides|sherpas|team of climbers)", r"\bin-house guides\b"]
COMPETITORS = ["bikatadventures", "trekthehimalayas", "indiahikes", "whitemagicadventure", "shikhar.com", "brozaadventures", "aquaterra",
               "himalayadestination", "wanderon", "discoverwithdheeraj", "jtreks", "thrillophilia", "tripoto"]
FACT_TRAPS = [
    (r"Kamet[^.<]{0,80}\bfirst\b[^.<]{0,40}7,?000", "Kamet was NOT the first 7,000 m summit (Trisul, 1907, was)"),
    (r"Stok Kangri[^.<?]{0,60}\b(?:is|now|has) (?:re-?)?open(?:ed)?\b", "Stok Kangri is closed since 2020 — never call it open"),
    (r"Sonam Gyatso[^.<]{0,60}first Indian", "the first Indians on Everest were Avtar Singh Cheema and Nawang Gombu (20 May 1965)"),
    (r"climb(?:ed|ing)? Kangchenjunga from (?:Sikkim|India)(?! is| has| was)", "Kangchenjunga cannot be climbed from India (banned since 2001)"),
    (r"national (?:refundable )?garbage deposit", "there is no national IMF garbage deposit"),
]


def min_css(css):
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    keep = []  # protect quoted strings (content:"Grade: ") from the whitespace squeeze

    def stash(m):
        keep.append(m.group(0))
        return f"\x00{len(keep) - 1}\x00"
    css = re.sub(r'"[^"]*"|\'[^\']*\'', stash, css)
    css = re.sub(r"\s+", " ", css)
    css = re.sub(r"\s*([{}:;,>])\s*", r"\1", css)
    css = re.sub(r"\x00(\d+)\x00", lambda m: keep[int(m.group(1))], css)
    return css.replace(";}", "}").strip()


def min_js(js):
    js = re.sub(r"/\*.*?\*/", "", js, flags=re.S)
    out = []
    for line in js.splitlines():
        line = line.strip()
        if line.startswith("//") or not line:
            continue
        out.append(line)
    return " ".join(out)


def min_html(h):
    h = re.sub(r"<!--.*?-->", "", h, flags=re.S)
    h = re.sub(r">\s+<", "><", h)
    h = re.sub(r"\s+", " ", h)
    return h.strip()


def live_paths():
    live = json.loads((KIT / "live.json").read_text()) if (KIT / "live.json").exists() else {}
    return {v["path"] for v in live.values()} | {"/mountains-of-india/", "/mountains-of-india/highest-peaks-in-india/", "/adventure/himalayan-peak-expeditions/"}


def check(slug, body, allowed=None):
    problems = []
    visible = re.sub(r'href="https://wa\.me/[^"]*"', "", body)  # WhatsApp prefill text may contain ___
    for pat, why in [(r"\{\{.*?\}\}", "placeholder"), (r"\bTODO\b|\blorem\b", "placeholder"), (r"___", "placeholder"),
                     (r"₹|\bRs\.?\s?\d|\bINR\s?\d", "rupee price")]:
        for m in re.finditer(pat, visible, flags=re.I):
            problems.append(f"{why}: {m.group(0)}")
    for pat in BANNED:
        for m in re.finditer(pat, body, flags=re.I):
            problems.append(f"banned claim: {m.group(0)}")
    for dom in COMPETITORS:
        if dom in body.lower():
            problems.append(f"competitor link/mention: {dom} (cite official or neutral sources instead)")
    for pat, why in FACT_TRAPS:
        for m in re.finditer(pat, body, flags=re.I):
            problems.append(f"fact trap: '{m.group(0)[:80]}' — {why}")
    allowed = allowed if allowed is not None else live_paths()
    for m in re.finditer(r'href="(/mountains-of-india/[^"#?]*)', body):
        if m.group(1) not in allowed:
            problems.append(f"link to a page that is not live: {m.group(1)}")
    if "file://" in body:
        problems.append("local media URLs (file://) — this build was made with MK_LOCAL_MEDIA=1 for preview; rebuild without it")
    if "<video" not in body:
        problems.append("no HyperFrames video on the page (render media first: make_media.sh, push, pin_media.py)")
    spec = KIT / "src" / "pages" / f"{slug}.json"
    if spec.exists():
        c = json.loads(spec.read_text(encoding="utf-8"))
        if len(c.get("seo_title", "")) > 60 or not c.get("seo_title"):
            problems.append(f"seo_title missing or over 60 chars ({len(c.get('seo_title', ''))})")
        if len(c.get("seo_desc", "")) > 155 or len(c.get("seo_desc", "")) < 110:
            problems.append(f"seo_desc must be 110-155 chars ({len(c.get('seo_desc', ''))})")
        if not c.get("focus"):
            problems.append("focus keyword missing")
        if len(c.get("sources", [])) < 3:
            problems.append("fewer than 3 sources listed")
        if len(c.get("faqs", [])) < 5:
            problems.append("fewer than 5 FAQs")
    return problems


def assemble(body_html):
    """Page HTML (out/<slug>.html contents) -> the one-line WordPress content string."""
    body = min_html(body_html)
    css = min_css((KIT / "kit.css").read_text(encoding="utf-8"))
    js = min_js((KIT / "kit.js").read_text(encoding="utf-8"))
    body = body.replace("<script>/*KITJS*/</script>", f"<script>{js}</script>")
    return f"<style>{css}</style>{body}"


def build(slug, force=False):
    src = (KIT / "out" / f"{slug}.html").read_text(encoding="utf-8")
    probs = check(slug, min_html(src))
    if probs and not force:
        sys.stderr.write(f"BUILD REFUSED ({slug}):\n  " + "\n  ".join(sorted(set(probs))) + "\n")
        sys.exit(1)
    outp = KIT / "out" / f"{slug}.min.html"
    outp.write_text(assemble(src), encoding="utf-8")
    print(f"{outp.name}: {outp.stat().st_size:,} bytes")


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    slugs = [p.stem for p in (KIT / "out").glob("*.html") if not p.stem.endswith(".min")] if which == "all" else [which]
    for s in slugs:
        build(s, "--force" in sys.argv)
