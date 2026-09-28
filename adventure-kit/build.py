#!/usr/bin/env python3
"""Suzu Adventure Kit builder.
Usage: python3 build.py page.html > page.min.html
Inlines kit.css (minified) as a <style> at the top of the page body and minifies the HTML to ONE line,
so WordPress's wpautop cannot inject <p>/<br> into the layout. Strips HTML comments.
Fails loudly if any placeholder (ALL_CAPS_URL / CARD_IMG_ / {{...}}) or a rupee price is left in.
"""
import re, sys, pathlib

KIT = pathlib.Path(__file__).with_name("kit.css")

def min_css(css: str) -> str:
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r"\s+", " ", css)
    css = re.sub(r"\s*([{}:;,>])\s*", r"\1", css)
    return css.replace(";}", "}").strip()

def min_html(html: str) -> str:
    html = re.sub(r"<!--.*?-->", "", html, flags=re.S)
    html = re.sub(r">\s+<", "><", html)
    html = re.sub(r"\s+", " ", html)
    return html.strip()

def main():
    src = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
    body = min_html(src)
    problems = []
    for pat, why in [(r"\b[A-Z][A-Z0-9_]*_(URL|IMG_\d|IMG_OR_VIDEO)\b", "placeholder left"),
                     (r"CARD_IMG_\d", "placeholder left"), (r"\{\{.*?\}\}", "placeholder left"),
                     (r"(₹|Rs\.?\s?\d|INR\s?\d)", "price shown — pages must not show prices")]:
        for m in re.finditer(pat, body):
            problems.append(f"{why}: {m.group(0)}")
    if problems and "--allow-placeholders" not in sys.argv:
        sys.stderr.write("BUILD REFUSED:\n" + "\n".join(sorted(set(problems))) + "\n")
        sys.exit(1)
    css = min_css(KIT.read_text(encoding="utf-8"))
    sys.stdout.write(f"<style>{css}</style>{body}")

if __name__ == "__main__":
    main()
