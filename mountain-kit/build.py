#!/usr/bin/env python3
"""Suzu Mountain Kit builder.

    python3 build.py <slug|all>     reads out/<slug>.html  ->  writes out/<slug>.min.html

Inlines kit.css (minified) at the top and kit.js (minified) where the page has <script>/*KITJS*/</script>, strips comments and
collapses the page to ONE line (WordPress wpautop cannot break it). REFUSES to build when:
  * a placeholder is left ({{...}}, TODO, ___ outside WhatsApp text, lorem)
  * a rupee price appears (₹ / Rs 123 / INR 123) — Suzu never prints its own prices on mountain pages
  * a partner/vendor name or network claim appears (see BANNED)
  * a link points to a /mountains-of-india/ URL that is not in live.json (no links to unbuilt pages)
"""
import json, pathlib, re, sys

KIT = pathlib.Path(__file__).resolve().parent
BANNED = [r"our vendor network", r"partner (?:company|companies|vendor)", r"verified vendors", r"authori[sz]ed vendors", r"Everest summiteers? on our team"]


def min_css(css):
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r"\s+", " ", css)
    css = re.sub(r"\s*([{}:;,>])\s*", r"\1", css)
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


def check(slug, body):
    problems = []
    visible = re.sub(r'href="https://wa\.me/[^"]*"', "", body)  # WhatsApp prefill text may contain ___
    for pat, why in [(r"\{\{.*?\}\}", "placeholder"), (r"\bTODO\b|\blorem\b", "placeholder"), (r"___", "placeholder"),
                     (r"₹|\bRs\.?\s?\d|\bINR\s?\d", "rupee price")]:
        for m in re.finditer(pat, visible, flags=re.I):
            problems.append(f"{why}: {m.group(0)}")
    for pat in BANNED:
        for m in re.finditer(pat, body, flags=re.I):
            problems.append(f"banned claim: {m.group(0)}")
    live = json.loads((KIT / "live.json").read_text()) if (KIT / "live.json").exists() else {}
    allowed = {v["path"] for v in live.values()} | {"/mountains-of-india/", "/mountains-of-india/highest-peaks-in-india/", "/adventure/himalayan-peak-expeditions/"}
    for m in re.finditer(r'href="(/mountains-of-india/[^"#?]*)', body):
        if m.group(1) not in allowed:
            problems.append(f"link to a page that is not live: {m.group(1)}")
    return problems


def build(slug):
    src = (KIT / "out" / f"{slug}.html").read_text(encoding="utf-8")
    body = min_html(src)
    probs = check(slug, body)
    if probs and "--force" not in sys.argv:
        sys.stderr.write(f"BUILD REFUSED ({slug}):\n  " + "\n  ".join(sorted(set(probs))) + "\n")
        sys.exit(1)
    css = min_css((KIT / "kit.css").read_text(encoding="utf-8"))
    js = min_js((KIT / "kit.js").read_text(encoding="utf-8"))
    body = body.replace("<script>/*KITJS*/</script>", f"<script>{js}</script>")
    outp = KIT / "out" / f"{slug}.min.html"
    outp.write_text(f"<style>{css}</style>{body}", encoding="utf-8")
    print(f"{outp.name}: {outp.stat().st_size:,} bytes")


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    slugs = [p.stem for p in (KIT / "out").glob("*.html") if not p.stem.endswith(".min")] if which == "all" else [which]
    for s in slugs:
        build(s)
