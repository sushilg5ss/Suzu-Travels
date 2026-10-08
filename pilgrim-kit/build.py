#!/usr/bin/env python3
"""Suzu Pilgrim Kit builder.

    python3 build.py <slug|all> [--force]     reads out/<slug>.html  ->  writes out/<slug>.min.html

Inlines kit.css (minified) at the top and kit.js (minified) where the page has <script>/*KITJS*/</script>, strips comments and
collapses the page to ONE line (WordPress wpautop cannot break it). REFUSES to build when:
  * a placeholder is left ({{...}}, TODO, ___ outside WhatsApp text, lorem)
  * a rupee price appears (₹ / Rs 123 / INR 123) — pilgrimage pages never print Suzu prices (packages link to their own pages)
  * a partner/vendor name or network claim appears (see BANNED), or a link to a competitor operator (COMPETITORS)
  * a known wrong "fact" appears (FACT_TRAPS — see README "Facts to avoid")
  * a link points to a /pilgrimage-tours/ URL that is not in live.json (no links to unbuilt pages)
  * the page has no HyperFrames video
  * (pages from src/pages/*.json) the SEO title is over 60 characters or the description over 155, or the focus keyword is missing
--force skips the refusal (only for local previews — never publish a forced build).
"""
import json, pathlib, re, sys

KIT = pathlib.Path(__file__).resolve().parent
BANNED = [r"our vendor network", r"partner (?:company|companies|vendor|operator)s?", r"verified vendors", r"authori[sz]ed vendors",
          r"Everest summiteers? on our team", r"our own (?:guides|sherpas|team of climbers)", r"\bin-house guides\b"]
COMPETITORS = ["veenaworld", "thomascook", "sotc.in", "makemytrip", "yatra.com", "trivenicabs", "tourtravelworld", "triptotemples", "thrillophilia",
               "tripoto", "indianholiday", "irctctourism.com", "discoverwithdheeraj", "wanderon", "holidify", "ujjaindarshan", "bhaktibharat", "ttrikon"]
FACT_TRAPS = [
    (r"Kedarnath[^.<]{0,60}(?:opened|opens|opening)[^.<]{0,30}19 April 2026", "Kedarnath opened on 22 Apr 2026 (Yamunotri/Gangotri opened 19 Apr)"),
    (r"Badrinath[^.<]{0,60}(?:opened|opening)[^.<]{0,20}24 April 2026", "Badrinath opened on 23 Apr 2026, not 24 Apr"),
    (r"Vaishno Devi[^.<]{0,60}\bone of the 51\b", "Vaishno Devi is NOT in the classical 51 Shakti Peeth lists"),
    (r"Sharad Navratri 2026[^.<]{0,40}22 Sep", "Sharad Navratri 2026 starts 11 Oct 2026"),
    (r"Mahashivratri 2027[^.<]{0,40}(?:2[0-9]|1[0-9]) (?:Feb|March)", "Mahashivratri 2027 is 6 March 2027"),
    (r"Amarnath[^.<]{0,80}helicopter[^.<]{0,40}(?:available|operat\w*|runs?) in 2026", "no Amarnath helicopter service ran in 2026 (no-fly zone)"),
    (r"Shrikhand[^.<]{0,60}2026[^.<]{0,40}(?:departures?|batch)", "Shrikhand Mahadev 2026 yatra was suspended on 29 Jun 2026"),
    (r"registered DMC", "never call Suzu a registered DMC: it is an HP Tourism registered travel agent"),
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
    return {v["path"] for v in live.values()}


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
    for m in re.finditer(r'href="(/pilgrimage-tours/[^"#?]*)', body):
        if m.group(1) not in allowed:
            problems.append(f"link to a page that is not live: {m.group(1)}")
    if "file://" in body:
        problems.append("local media URLs (file://) — this build was made with PK_LOCAL_MEDIA=1 for preview; rebuild without it")
    if "<video" not in body:
        problems.append("no HyperFrames video on the page (render media first: make_media.sh, push, pin_media.py)")
    spec = KIT / "src" / "pages" / f"{slug}.json"
    base_meta = json.loads((KIT / "src" / "meta.json").read_text(encoding="utf-8")) if (KIT / "src" / "meta.json").exists() else {}
    if spec.exists() or slug in base_meta:
        c = json.loads(spec.read_text(encoding="utf-8")) if spec.exists() else base_meta[slug]
        if len(c.get("seo_title", "")) > 60 or not c.get("seo_title"):
            problems.append(f"seo_title missing or over 60 chars ({len(c.get('seo_title', ''))})")
        if len(c.get("seo_desc", "")) > 155 or len(c.get("seo_desc", "")) < 110:
            problems.append(f"seo_desc must be 110-155 chars ({len(c.get('seo_desc', ''))})")
        if not c.get("focus"):
            problems.append("focus keyword missing")
        if spec.exists() and len(c.get("sources", [])) < 3:
            problems.append("fewer than 3 sources listed")
        if spec.exists() and len(c.get("faqs", [])) < 5:
            problems.append("fewer than 5 FAQs")
    return problems


BASE = ("pilgrimage-tours",)  # full kit CSS; every other page gets only the CSS rules it uses
KEEP_CLASSES = {"hl", "page-content", "page-header", "entry-title"}  # added by kit.js, or the theme's own wrappers


def css_rules(css):
    """Split minified CSS into top-level chunks: plain rules and whole @media blocks."""
    out, i, depth, start = [], 0, 0, 0
    while i < len(css):
        ch = css[i]
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                out.append(css[start:i + 1])
                start = i + 1
        i += 1
    return out


def prune_css(css, body):
    """Keep only rules whose every class name is used on the page (content pages only: smaller pages, same look)."""
    used = set(c for m in re.finditer(r'class="([^"]*)"', body) for c in m.group(1).split()) | KEEP_CLASSES

    def keep_rule(rule):
        sel = rule[:rule.find("{")]
        for part in sel.split(","):
            classes = re.findall(r"\.([A-Za-z0-9_-]+)", re.sub(r":has\([^)]*\)", "", part))
            if all(c in used for c in classes):
                return True
        return False
    out = []
    for r in css_rules(css):
        if r.startswith("@media"):
            inner = r[r.find("{") + 1:-1]
            kept = [x for x in css_rules(inner) if keep_rule(x)]
            if kept:
                out.append(r[:r.find("{") + 1] + "".join(kept) + "}")
        elif keep_rule(r):
            out.append(r)
    return "".join(out)


def assemble(body_html, slug=None):
    """Page HTML (out/<slug>.html contents) -> the one-line WordPress content string.
    Content pages get only the CSS rules they use; the three base pages keep the full kit CSS."""
    body = min_html(body_html)
    css = min_css((KIT / "kit.css").read_text(encoding="utf-8"))
    if slug and slug not in BASE:
        css = prune_css(css, body)
    media = json.loads((KIT / "media.json").read_text()) if (KIT / "media.json").exists() else {}
    if "FONTSHA" in css:
        if not media.get("fonts"):
            raise SystemExit("media.json has no 'fonts' commit pinned (python3 pin_media.py fonts <sha>)")
        css = css.replace("FONTSHA", media["fonts"])
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
    page_html = assemble(src, slug)
    import subprocess, tempfile
    for m in re.finditer(r"<script>(.*?)</script>", page_html, re.S):  # untyped = executable JS
        if re.search(r"<(?:div|p|h[1-6]|ul|ol|li|table|section)\b", m.group(1)) and not force:
            sys.exit("BUILD REFUSED: block-level HTML inside a <script> — WordPress wpautop will break it (README §8)")
        with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as t:
            t.write(m.group(1))
        r = subprocess.run(["node", "--check", t.name], capture_output=True, text=True)
        if r.returncode and not force:
            sys.exit("BUILD REFUSED: inline JS does not parse:\n" + r.stderr[:400])
    outp.write_text(page_html, encoding="utf-8")
    print(f"{outp.name}: {outp.stat().st_size:,} bytes")


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    slugs = [p.stem for p in (KIT / "out").glob("*.html") if not p.stem.endswith(".min")] if which == "all" else [which]
    for s in slugs:
        build(s, "--force" in sys.argv)
