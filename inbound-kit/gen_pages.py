#!/usr/bin/env python3
"""Suzu Inbound Kit — page generator for the "India for international travellers" section of suzutravels.com.

    python3 gen_pages.py <slug|all>        reads src/pages/<slug>.json  ->  writes out/<slug>.html   (then: python3 build.py <slug>)

One generic schema for four page kinds — guide (practical/how-to), itinerary (a sample trip), product (a bookable service,
e.g. private car + driver), hub (a landing page listing children). Every section is data-driven from the JSON, so the
Page Builder never writes raw HTML by hand. Scoped to `.szi` (kit.css). Hero video from media/<slug>/ pinned on jsDelivr
(media.json); set PK_LOCAL_MEDIA=1 for a local preview.

Hard rules enforced here (build.py enforces more):
  * prices: ONLY the "from US$…" values listed in data/prices.json (the live /india-tours/ rates) — any other US$ number refuses
  * every page carries: answer-first block, FAQ (≥5), sources (≥3), verified date, trust strip with the HP Tourism reg. no.,
    WhatsApp + email CTA, the booking line (DEPOSIT, printed ONCE, in the CTA section — price boxes only point to it) and the
    privacy line (PRIVACY: enquiry answered by the Suzu team only, data not shared, link to /privacy-policy/) — Reviewer rules 16 Oct 2026
  * links to /india-tours/<slug>/ only when that slug is in live.json
"""
import html, json, os, pathlib, re, sys, urllib.parse

KIT = pathlib.Path(__file__).resolve().parent
LIVE = json.loads((KIT / "live.json").read_text(encoding="utf-8")) if (KIT / "live.json").exists() else {}
MEDIA = json.loads((KIT / "media.json").read_text(encoding="utf-8")) if (KIT / "media.json").exists() else {}
PDFS = json.loads((KIT / "pdf.json").read_text(encoding="utf-8")) if (KIT / "pdf.json").exists() else {}  # itinerary PDFs (tools/itinerary_pdf.py)
PRICES = json.loads((KIT / "data" / "prices.json").read_text(encoding="utf-8")) if (KIT / "data" / "prices.json").exists() else {}
REPO = "sushilg5ss/suzu-travels"
WA = "https://wa.me/917087488961?text="
PHONE = "+91 70874 88961"
EMAIL = "info@suzutravels.com"
REG = "HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022"
HUB = "/india-tours/"
DEPOSIT = "A 20% deposit locks your dates and price. Full refund if you cancel within 48 hours of paying. Pay by card (Razorpay, international cards accepted) or PayPal; the balance is due before the trip."
PRIVACY = ('Your message goes only to the Suzu Travels team in Himachal and is used only to answer your enquiry — we do not sell or share it. '
           '<a href="/privacy-policy/">Privacy policy</a>.')
VERIFIED = "16 Oct 2026"
LOCAL_MEDIA = bool(os.environ.get("PK_LOCAL_MEDIA"))


def e(s):
    return html.escape(str(s), quote=True).replace(" - ", " – ")


def wa(text):
    return WA + urllib.parse.quote(text)


def iso_date(verified):
    """'16 Oct 2026' -> '2026-10-16' for schema.org dates (falls back to the text as given)."""
    try:
        import datetime
        return datetime.datetime.strptime(verified.strip(), "%d %b %Y").date().isoformat()
    except Exception:
        return verified


def ext(url, text):
    return f'<a href="{e(url)}" target="_blank" rel="noopener">{text}</a>'


def media_url(slug, fname):
    if LOCAL_MEDIA:
        return (KIT / "media" / slug / fname).as_uri()
    sha = MEDIA.get(slug)
    if not sha:
        raise SystemExit(f"media.json has no commit pinned for '{slug}' — run make_media.sh, push, then pin_media.py")
    return f"https://cdn.jsdelivr.net/gh/{REPO}@{sha}/inbound-kit/media/{slug}/{fname}"


def hero_video(slug, comp, alt):
    u = lambda f: media_url(slug, f)
    return (f'<video autoplay muted loop playsinline preload="metadata" poster="{u(comp + "-poster.webp")}" aria-label="{e(alt)}">'
            f'<source media="(max-width: 640px)" src="{u(comp + "-m.mp4")}" type="video/mp4">'
            f'<source src="{u(comp + ".mp4")}" type="video/mp4"></video>')


def lazy_video(slug, comp, alt):
    u = lambda f: media_url(slug, f)
    return (f'<video data-lazy muted loop playsinline preload="none" poster="{u(comp + "-poster.webp")}" aria-label="{e(alt)}">'
            f'<source data-src="{u(comp + ".mp4")}" type="video/mp4"></video>')


def nav(items, cta_href):
    a = "".join(f'<a href="#{i}">{t}</a>' for i, t in items)
    return f'<nav class="szi-nav" aria-label="On this page"><div class="szi-nav-in">{a}<a class="cta" href="{cta_href}" target="_blank" rel="noopener">Talk to a local expert</a></div></nav>'


def faq(items):
    return '<div class="szi-faq">' + "".join(f"<details><summary>{e(q)}</summary><p>{a}</p></details>" for q, a in items) + "</div>"


def faq_ld(items):
    strip = lambda s: re.sub(r"<[^>]+>", "", s)
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": html.unescape(strip(a))}} for q, a in items]}


def ld(*objs):
    g = {"@context": "https://schema.org", "@graph": list(objs)}
    return '<script type="application/ld+json">' + json.dumps(g, ensure_ascii=False).replace("</", "<\\/") + "</script>"


def trust(verified=None):
    return (f'<div class="szi-trust"><span><a href="/certificates/">{REG}</a></span><span>Facts checked {e(verified or VERIFIED)}</span>'
            f'<span>Sources listed below</span><span>Local office in Himachal, India · since 2019</span></div>')


def sources(items):
    return '<ol class="szi-src">' + "".join(f"<li>{ext(u, e(t))}</li>" for t, u in items) + "</ol>"


def tile(v):
    return f'<a class="szi-link" href="{v["path"]}"><span class="n">{e(v["label"])}</span><span class="c">{e(v.get("blurb", ""))}</span></a>'


def price_ok(text):
    """Only the approved 'from US$…' figures may appear."""
    allowed = {str(v) for v in PRICES.get("allowed", [])}
    for m in re.finditer(r"US\$\s?([0-9][0-9,]*)", text):
        if m.group(1).replace(",", "") not in allowed:
            raise SystemExit(f"price US${m.group(1)} is not in data/prices.json allowed list — use an approved 'from' rate or 'on request'")


def steps(items):
    return '<ol class="szi-steps">' + "".join(f"<li><b>{e(a)}</b><span>{b}</span></li>" for a, b in items) + "</ol>"


def cards(items):
    return '<div class="szi-cards">' + "".join(f'<div class="szi-card"><h3>{e(a)}</h3><p>{b}</p></div>' for a, b in items) + "</div>"


def table(rows, head=None):
    th = ("<thead><tr>" + "".join(f"<th>{e(h)}</th>" for h in head) + "</tr></thead>") if head else ""
    tb = "<tbody>" + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody>"
    return f'<div class="szi-scroll"><table class="szi-tbl">{th}{tb}</table></div>'


def days(items):
    # markup matches kit.css .szi-route (.d day label, .t title, p text) — fixed 18 Oct 2026 (first `days` page: kerala-tour)
    return '<ol class="szi-route">' + "".join(f'<li><div class="d">DAY {e(d)}</div><div class="t">{e(t)}</div><p>{x}</p></li>' for d, t, x in items) + "</ol>"


def stats(items):
    return '<div class="szi-stats">' + "".join(f'<div class="szi-stat"><b>{e(a)}</b><span>{e(b)}</span></div>' for a, b in items) + "</div>"


def section(s, slug):
    k = s.get("kind", "prose")
    body = f'<span class="k">{e(s.get("kicker", ""))}</span>' if s.get("kicker") else ""
    body += f'<h2>{e(s["h2"])}</h2>'
    if s.get("lead"):
        body += f'<p class="lead">{s["lead"]}</p>'
    if s.get("video"):  # explainer composition name inside media/<slug>/
        body += f'<div class="szi-media">{lazy_video(slug, s["video"], s["h2"])}<div><p>{s.get("video_caption", "")}</p></div></div>'
    if k == "prose":
        body += "".join(f"<p>{p}</p>" for p in s.get("paras", []))
    elif k == "steps":
        body += steps(s["items"])
    elif k == "cards":
        body += cards(s["items"])
    elif k == "table":
        body += table(s["rows"], s.get("head"))
    elif k == "days":
        body += days(s["days"])
    elif k == "stats":
        body += stats(s["items"])
    elif k == "callout":
        body += f'<div class="szi-call"><p>{s["text"]}</p></div>'
    else:
        raise SystemExit(f"unknown section kind {k}")
    if s.get("after"):
        body += "".join(f"<p>{p}</p>" for p in s["after"])
    if s.get("note"):
        body += f'<p class="szi-note">{s["note"]}</p>'
    cls = "szi-sec" + (f' {s["style"]}' if s.get("style") else "")
    return f'<section class="{cls}" id="{e(s["id"])}">{body}</section>'


def pdf_card(slug, c):
    """Download card after the `days` section of an itinerary page whose PDF is pinned in pdf.json (Reviewer 21 Oct 2026)."""
    sha = PDFS.get(slug)
    if not sha:
        return ""
    fname = f"{slug}{'' if 'itinerary' in slug else '-itinerary'}-suzu-travels.pdf"
    url = f"https://cdn.jsdelivr.net/gh/{REPO}@{sha}/inbound-kit/pdf/{slug}/{fname}"
    n = len(next(s for s in c["sections"] if s.get("kind") == "days")["days"])
    text = f"Hello Suzu Travels, I downloaded the {n}-day itinerary ({c['label']}). Country: ___ , travel dates: ___ , travellers: ___"
    return (f'<section class="szi-sec" id="itinerary-pdf"><div class="szi-call"><p><b>Take this plan with you: {n}-day itinerary (PDF).</b> '
            'Day by day, what is included and what is not, prices and how booking works — 2 pages. No email or sign-up needed; '
            'print it or share it with whoever you travel with.</p>'
            f'<div class="szi-btns"><a class="szi-btn gold" href="{e(url)}" download target="_blank" rel="noopener">Download PDF</a>'
            f'<a class="szi-btn line" href="{wa(text)}" target="_blank" rel="noopener">Ask about this plan</a></div></div></section>')


def price_box(p):
    rows = [[e(a), f"<b>{e(b)}</b>", c] for a, b, c in p["rows"]]
    return (f'<section class="szi-sec alt" id="prices"><span class="k">Prices</span><h2>{e(p["h2"])}</h2>'
            + (f'<p class="lead">{p["lead"]}</p>' if p.get("lead") else "") + table(rows, ["Option", "From", "What it covers"])
            + f'<p class="szi-note">{p.get("note", "Prices are per person in US dollars, indicative for the season shown, and confirmed on your quote. Taxes included; international flights excluded.")}</p>'
            + '<p class="szi-note">Booking terms (20% deposit, 48-hour refund window) are stated once, under <a href="#plan">Plan it with a local</a>.</p></section>')


def cta(c, slug):
    text = c.get("wa", f"Hello Suzu Travels, I'm planning a trip to India. Page: {slug}. Dates: ___ , travellers: ___ , country: ___")
    second = c.get("second", ["/himachal-tour-packages-quote/", "Send a quote request"])
    return (f'<section class="szi-sec" id="plan"><div class="szi-quote"><div><span class="k">Plan it with a local</span><h2>{e(c["h2"])}</h2><p>{c["text"]}</p>'
            f'<p class="szi-note">We usually reply within 2 hours, 9 am–9 pm IST (UTC+5:30). Email {EMAIL} if you don\'t use WhatsApp.</p></div>'
            f'<div class="szi-btns"><a class="szi-btn gold" href="{wa(text)}" target="_blank" rel="noopener">WhatsApp {PHONE}</a>'
            f'<a class="szi-btn ghost" href="{second[0]}">{e(second[1])}</a></div></div>'
            f'<p class="szi-note"><b>Booking:</b> {DEPOSIT}</p>'
            f'<p class="szi-note">{PRIVACY}</p></section>')


def page(body):
    return f'<div class="szi">{body}</div><script>/*KITJS*/</script>'


def content_page(slug):
    c = json.loads((KIT / "src" / "pages" / f"{slug}.json").read_text(encoding="utf-8"))
    m = c.get("media", slug)
    navi = [("overview", "Overview")] + [(s["id"], s.get("nav", s["h2"])) for s in c["sections"]] + ([("prices", "Prices")] if c.get("prices") else []) + [("faq", "FAQ"), ("plan", "Plan")]
    watxt = c.get("cta", {}).get("wa", f"Hello Suzu Travels, I'm planning a trip to India ({c['title']}). Dates: ___ , travellers: ___ , country: ___")
    hero = (f'<section class="szi-hero">{hero_video(m, "hero", c.get("hero_alt", c["title"]))}<div class="szi-hero-in"><span class="k">{e(c["kicker"])}</span>'
            f'<p class="szi-tag">{e(c["tag"])}</p><p class="szi-sub">{c["sub"]}</p>'
            + ('<ul class="szi-chips">' + "".join(f"<li><b>{e(a)}</b> {e(b)}</li>" for a, b in c.get("chips", [])) + "</ul>" if c.get("chips") else "")
            + f'<div class="szi-btns"><a class="szi-btn gold" href="#overview">{e(c.get("cta1", "Read the guide"))}</a><a class="szi-btn ghost" href="{wa(watxt)}" target="_blank" rel="noopener">Ask a local on WhatsApp</a></div>{trust(c.get("verified"))}</div></section>')
    over = (f'<section class="szi-sec" id="overview"><div class="szi-answer"><span class="k">In short</span><h2>{e(c["q"])}</h2><p>{c["answer"]}</p></div>'
            + (stats(c["facts"]) if c.get("facts") else "") + "</section>")
    secs = [section(s, m) + (pdf_card(slug, c) if s.get("kind") == "days" and c.get("kind") == "itinerary" else "") for s in c["sections"]]
    pb = price_box(c["prices"]) if c.get("prices") else ""
    fq = f'<section class="szi-sec alt" id="faq"><span class="k">FAQ</span><h2>{e(c.get("faq_h2", "Questions travellers ask"))}</h2>{faq(c["faqs"])}</section>'
    links = "".join(tile(LIVE[s]) for s in c.get("links", []) if s in LIVE) + f'<a class="szi-link" href="{HUB}"><span class="n">All India tours for international travellers</span><span class="c">Golden Triangle, Himalayas, Kashmir, Char Dham &amp; private driver trips</span></a>'
    more = (f'<section class="szi-sec" id="more"><h2>Keep exploring</h2><div class="szi-links">{links}</div><h3 class="szi-gh">Sources</h3>{sources([(a, b) for a, b in c["sources"]])}'
            f'<p class="szi-note">Written by the Suzu Travels team in Himachal Pradesh, India. Facts checked {e(c.get("verified", VERIFIED))}. Prices, visa rules and road conditions change — we re-check this page regularly; ask us before you book.</p></section>')
    body = hero + nav(navi, wa(watxt)) + over + "".join(secs) + pb + fq + cta(c["cta"], slug) + more
    graph = [{"@type": "Article", "headline": c["title"], "inLanguage": "en", "dateModified": c.get("modified", iso_date(c.get("verified", VERIFIED))),
              "author": {"@type": "Organization", "name": "Suzu Travels"}, "publisher": {"@type": "TravelAgency", "name": "Suzu Travels", "url": "https://suzutravels.com/", "telephone": "+91-7087488961", "address": {"@type": "PostalAddress", "addressLocality": "Bilaspur", "addressRegion": "Himachal Pradesh", "addressCountry": "IN"}}}]
    if c.get("trip"):
        t = c["trip"]
        graph.append({"@type": "TouristTrip", "name": t["name"], "description": t.get("desc", ""), "touristType": t.get("type", ["International travellers"]),
                      "itinerary": {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n} for i, n in enumerate(t.get("stops", []))]},
                      "provider": {"@type": "TravelAgency", "name": "Suzu Travels", "telephone": "+91-7087488961"}})
    if c.get("service"):
        s = c["service"]
        graph.append({"@type": "Service", "name": s["name"], "serviceType": s.get("type", "Private car with driver"), "areaServed": s.get("area", "North India"),
                      "provider": {"@type": "TravelAgency", "name": "Suzu Travels", "telephone": "+91-7087488961"}})
    graph.append(faq_ld(c["faqs"]))
    out = page(body + ld(*graph))
    price_ok(out)
    if len(c["faqs"]) < 5 or len(c["sources"]) < 3:
        raise SystemExit("every inbound page needs ≥5 FAQs and ≥3 sources")
    for s in c.get("links", []):
        if s not in LIVE:
            raise SystemExit(f"link to '{s}' refused: not in live.json")
    return out


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    slugs = [p.stem for p in (KIT / "src" / "pages").glob("*.json") if not p.stem.startswith("_")] if which == "all" else [which]
    (KIT / "out").mkdir(exist_ok=True)
    for s in slugs:
        (KIT / "out" / f"{s}.html").write_text(content_page(s), encoding="utf-8")
        print(f"out/{s}.html")
