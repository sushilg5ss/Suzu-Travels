#!/usr/bin/env python3
"""Printable itinerary PDF for every `kind: itinerary` kit page (Reviewer, 21 Oct 2026 — Trust FIX NEEDED 'itinerary-pdf in the kit').

    python3 tools/itinerary_pdf.py <slug|all>     -> pdf/<slug>/<slug>-itinerary-suzu-travels.pdf (+ .html source)
    then: commit + push, `python3 tools/itinerary_pdf.py --pin <slug|all> <sha>` -> pdf.json, and gen_pages.py prints the
    download card right after the page's `days` section (only for slugs pinned in pdf.json).

Content comes ONLY from src/pages/<slug>.json (the same text that is live): title, days, the `included` section cards, the
price rows (on request / from US$ in data/prices.json) — plus the fixed booking line, registration line, address and contacts.
Same design as trust/widgets/itinerary-pdf (Trust lane, 11412). Rendered with Chromium print (Playwright, A4).
"""
import html, json, pathlib, re, sys

KIT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(KIT))
import gen_pages as G  # noqa: E402

PINS = KIT / "pdf.json"
BOOKING = ("20% deposit locks your dates and price; full refund if cancelled within 48 hours of paying; "
           "balance before the trip; pay by card via Razorpay (international cards accepted) or PayPal.")
ADDRESS = "NH 103, Kulahru, Tehsil Ghumarwin, Bilaspur, Himachal Pradesh, India"
ALLOWED = set(G.PRICES.get("allowed", []))


def txt(s):
    s = re.sub(r"<[^>]+>", "", str(s))
    return html.escape(html.unescape(s), quote=False)


def pdf_name(slug):
    return f"{slug}{'' if 'itinerary' in slug else '-itinerary'}-suzu-travels.pdf"


def page(slug):
    c = json.loads((KIT / "src" / "pages" / f"{slug}.json").read_text(encoding="utf-8"))
    if c.get("kind") != "itinerary":
        return None
    dsec = next((s for s in c["sections"] if s.get("kind") == "days"), None)
    if not dsec:
        return None
    return c, dsec


def pdf_html(slug):
    c, dsec = page(slug)
    days = "".join(f'<div class="d"><div class="n">DAY {txt(d)}</div><div><h3>{txt(t)}</h3><p>{txt(x)}</p></div></div>'
                   for d, t, x in dsec["days"])
    inc = next((s for s in c["sections"] if s.get("id") == "included"), None)
    incl = "".join(f"<li><b>{txt(a)}.</b> {txt(b)}</li>" for a, b in (inc or {}).get("items", []))
    rows = (c.get("prices") or {}).get("rows", [])
    pr = "".join(f"<tr><td>{txt(a)}</td><td><b>{txt(b)}</b></td><td>{txt(x)}</td></tr>" for a, b, x in rows)
    title = c.get("trip", {}).get("name") or c["title"]
    url = f"https://suzutravels.com{c['path']}"
    h = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{txt(title)} · Suzu Travels</title>
<meta name="author" content="Suzu Travels"><style>
@page{{size:A4;margin:16mm 15mm 16mm}}*{{box-sizing:border-box}}
body{{font-family:Inter,'DejaVu Sans',sans-serif;color:#0E1B14;font-size:10.2pt;line-height:1.45;margin:0}}
.top{{background:#0E1B14;color:#F4EEDD;border-radius:10px;padding:16px 18px}}
.top small{{color:#E2C158;letter-spacing:.12em;font-weight:700;font-size:8pt}}.top h1{{margin:4px 0 2px;font-size:18pt;line-height:1.15;color:#fff}}
.top p{{margin:0;color:#DCD3BC;font-size:9.5pt}}h2{{font-size:12.5pt;margin:16px 0 8px;border-bottom:2px solid #E2C158;padding-bottom:4px}}
.d{{display:flex;gap:12px;padding:7px 0;border-bottom:1px solid #E8E1CC;page-break-inside:avoid}}.n{{flex:none;width:56px;font-weight:800;color:#B8860B;font-size:9pt;padding-top:2px}}
.d h3{{margin:0 0 2px;font-size:10.8pt}}.d p{{margin:0}}ul{{margin:0;padding-left:16px}}li{{margin:3px 0}}
table{{width:100%;border-collapse:collapse;font-size:9.2pt}}td{{border-bottom:1px solid #E8E1CC;padding:5px 6px;vertical-align:top}}
.box{{background:#F4EEDD;border-radius:8px;padding:10px 12px;margin-top:8px;page-break-inside:avoid}}
.foot{{margin-top:14px;font-size:8.8pt;color:#4b5249;border-top:1px solid #E8E1CC;padding-top:8px}}a{{color:#8a6508}}</style></head><body>
<div class="top"><small>SUZU TRAVELS · PRIVATE TOUR OF INDIA</small><h1>{txt(title)}</h1><p>{txt(c.get("blurb") or c["label"])} — a sample plan we build from; every night can move.</p></div>
<h2>Day by day</h2>{days}
{f"<h2>What is included — and what is not</h2><ul>{incl}</ul>" if incl else ""}
{f'<h2>Prices</h2><table>{pr}</table><div class="box">Prices are per person in US dollars, indicative, and confirmed on your quote. You receive a day-by-day plan with a US-dollar total and what it covers before you pay anything.</div>' if pr else ""}
<h2>How booking works</h2><p>{txt(BOOKING)}</p>
<div class="foot"><b>Suzu Travels</b> · {txt(G.REG)} (certificate: <a href="https://suzutravels.com/certificates/">suzutravels.com/certificates</a>) · Office: {ADDRESS}<br>
WhatsApp / phone <b>{G.PHONE}</b> · <a href="mailto:{G.EMAIL}">{G.EMAIL}</a> · Full page: <a href="{url}">{url.replace("https://", "")}</a> · Facts checked {txt(c.get("verified", G.VERIFIED))}.</div>
</body></html>'''
    for bad in ["24/7", "verified driver", "police", "cheapest", "best price", "₹", "guaranteed"]:
        assert bad not in h.lower(), (slug, bad)
    for n in re.findall(r"US\$\s?([\d,]+)", h):
        assert int(n.replace(",", "")) in ALLOWED, (slug, n)
    assert G.PHONE in h and BOOKING in html.unescape(h) and G.REG in html.unescape(h)
    return h


def render(slug):
    from playwright.sync_api import sync_playwright
    d = KIT / "pdf" / slug
    d.mkdir(parents=True, exist_ok=True)
    src = d / f"{slug}-itinerary.html"
    src.write_text(pdf_html(slug), encoding="utf-8")
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/opt/pw-browsers/chromium") if pathlib.Path("/opt/pw-browsers/chromium").exists() else p.chromium.launch()
        pg = b.new_page()
        pg.goto(src.as_uri())
        pg.pdf(path=str(d / pdf_name(slug)), format="A4", print_background=True, prefer_css_page_size=True)
        b.close()
    print(d / pdf_name(slug), round((d / pdf_name(slug)).stat().st_size / 1024), "KB")


def slugs(which):
    if which != "all":
        return [which]
    return [p.stem for p in sorted((KIT / "src" / "pages").glob("*.json")) if not p.stem.startswith("_") and page(p.stem)]


if __name__ == "__main__":
    if sys.argv[1] == "--pin":
        pins = json.loads(PINS.read_text()) if PINS.exists() else {}
        for s in slugs(sys.argv[2]):
            pins[s] = sys.argv[3]
        PINS.write_text(json.dumps(pins, indent=1, sort_keys=True) + "\n")
        print("pinned", sys.argv[2], sys.argv[3])
    else:
        for s in slugs(sys.argv[1]):
            render(s)
