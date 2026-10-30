#!/usr/bin/env python3
"""Suzu Cab Kit page builder.
  python3 build.py            -> builds out/<slug>.html (readable) and out/<slug>.min.html (ONE line, ready for WordPress)
Media URLs come from media.json ({"hero": {...}, "<slug>": {"route": {...}}}); missing media -> poster-less fallback.
Refuses to build if copy fares disagree with the fare engine, or if a placeholder is left.
"""
import json, re, html, pathlib, sys, urllib.parse
from cabs_data import *
from pages_content import PAGES
from vehicles_svg import svg as vsvg

ROOT = pathlib.Path(__file__).parent
OUT = ROOT / "out"; OUT.mkdir(exist_ok=True)
MEDIA = json.loads((ROOT / "media.json").read_text()) if (ROOT / "media.json").exists() else {}
LIVE = set(json.loads((ROOT / "live.json").read_text())) if (ROOT / "live.json").exists() else set()
KIT_CSS = (ROOT / "kit.css").read_text()

def min_css(css):
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r"\s+", " ", css)
    css = re.sub(r"\s*([{}:;,>])\s*", r"\1", css)
    return css.replace(";}", "}").strip()

def min_html(h):
    h = re.sub(r"<!--.*?-->", "", h, flags=re.S)
    h = re.sub(r">\s+<", "><", h)
    h = re.sub(r"\s+", " ", h)
    return h.strip()

def wa(text):
    return WA_BASE + urllib.parse.quote(text)

def esc(s):
    return html.escape(s, quote=True)

def page_url(slug):
    return f"/cabs/{slug}/"

def is_live(slug):
    return slug in LIVE

def pinr(n):
    """Price span the tier switch re-paints (n = Standard-tier amount)."""
    return f'<span data-inr="{int(n)}">{inr(n)}</span>'

def pkm(rate):
    return f'<span data-km="{int(rate)}">₹{int(rate)}/km</span>'

def tier_switch(note=True):
    b = "".join(f'<button type="button" data-tier="{t["id"]}"{" class=on" if t["id"]=="standard" else ""} aria-pressed="{"true" if t["id"]=="standard" else "false"}"><span class="n">{t["name"]}</span><span class="s">{t["sub"]}</span><span class="b">{t["badge"]}</span></button>' for t in TIERS)
    n = '<p class="szc-tier-note">Same route, same driver standard - you pick how new the car should be. Prices on this page update with your choice.</p>' if note else ""
    return f'<div class="szc-tier" role="group" aria-label="Choose fleet">{b}</div>{n}'

PHOTOS = MEDIA.get("photos", {})

def video_tag(m, cls="", eager=False):
    if not m:
        return ""
    pre = "auto" if eager else "metadata"
    mob = f'<source src="{m["mobile"]}" type="video/mp4" media="(max-width: 640px)">' if m.get("mobile") else ""
    return (f'<video class="{cls}" autoplay muted loop playsinline preload="{pre}" poster="{m["poster"]}" width="{m.get("w",1600)}" height="{m.get("h",900)}">'
            f'{mob}<source src="{m["webm"]}" type="video/webm"><source src="{m["mp4"]}" type="video/mp4"></video>')

# ---------------------------------------------------------------- blocks
def hero(p, chips):
    trust = (f'<div class="szc-trust"><span><a href="/certificates/">{REG}</a></span><span>GST registered</span>'
             f'<span>{RATING}</span><span>24×7 WhatsApp {PHONE_TXT}</span></div>')
    chip_html = "".join(f"<li>{c}</li>" for c in chips)
    film = MEDIA.get("film") or MEDIA.get(p["slug"], {}).get("hero") or MEDIA.get("hero")   # 17 Oct 2026: one cinematic real-footage film on every cab page (Sushil: the drawn car loop looked cheap)
    return (f'<section class="szc-hero">{video_tag(film, eager=True)}<div class="szc-hero-in">'
            f'<span class="szc-kicker">{p["kicker"]}</span><p class="szc-hero-tag">{p["tag"]}</p>'
            f'<p class="szc-hero-sub">{p["sub"]}</p><ul class="szc-chips">{chip_html}</ul>'
            f'<div class="szc-btns"><a class="szc-btn gold" href="{wa(p["wa"] + " (page: " + p["slug"] + ")")}" target="_blank" rel="noopener">Get fare on WhatsApp</a>'
            f'<a class="szc-btn ghost" href="#fares">See all fares</a></div>{trust}</div></section>')

def nav(items):
    links = "".join(f'<a href="#{a}">{b}</a>' for a, b in items)
    return f'<nav class="szc-nav" aria-label="On this page"><div class="szc-nav-in">{links}<a class="cta" href="#quote">Get quote</a></div></nav>'

def facts(fs):
    return '<div class="szc-facts">' + "".join(f'<div class="szc-fact"><div class="k">{k}</div><div class="v">{v}</div></div>' for k, v in fs) + "</div>"

def fare_table_route(r, slug):
    rows = []
    for v in PRICED:
        ow = oneway(v["id"], r["km"], r["f"])
        q = wa(f"Hi Suzu Travels, quote for {r['a']} to {r['b']} in {v['name']}. Date: ___ , people: ___ (page: {slug})")
        rows.append(f'<tr><td><b>{v["name"]}</b><br><small>{v["model"]}</small></td><td>{v["seats"]}</td><td class="num">{pinr(ow)}</td>'
                    f'<td class="num">{pkm(v["hire"])}</td><td><a class="szc-btn sm line" href="{q}" target="_blank" rel="noopener">Quote</a></td></tr>')
    return (tier_switch() + '<div class="szc-scroll"><table class="szc-tbl"><thead><tr><th>Car</th><th>Seats</th><th>One-way from (<span data-tiername>Standard</span>)</th><th>Round trip</th><th></th></tr></thead><tbody>'
            + "".join(rows) + "</tbody></table></div>")

def includes():
    return '<ul class="szc-note" style="padding-left:18px;margin-top:14px">' + "".join(f"<li>{x}</li>" for x in COMMON_INCLUDES) + "</ul>"

def calculator(dests, slug, default_vehicle="sedan"):
    veh = [dict(id=v["id"], n=v["name"], ow=v["ow"], h=v["hire"], m=v["min"], nt=v["night"]) for v in PRICED]
    data = json.dumps(dict(v=veh, d=dests, s=slug), ensure_ascii=False, separators=(",", ":"))
    dopts = "".join(f'<option value="{i}">{esc(d["l"])}</option>' for i, d in enumerate(dests))
    vopts = "".join(f'<option value="{v["id"]}"{" selected" if v["id"]==default_vehicle else ""}>{v["name"]} ({v["seats"]} seats)</option>' for v in PRICED)
    d0 = dests[0]; amt0 = oneway(default_vehicle, d0["km"], d0["f"])
    return (f'<div class="szc-calc" id="szc-calc" data-cfg=\'{esc(data)}\'>'
            f'<div class="szc-calc-f"><div class="full"><label for="szc-cd">Route</label><select id="szc-cd">{dopts}</select></div>'
            f'<div class="full"><label>Trip type</label><div class="szc-seg" role="group"><button type="button" class="on" data-m="one">One-way drop</button><button type="button" data-m="round">Round trip / tour</button></div></div>'
            f'<div><label for="szc-cv">Car</label><select id="szc-cv">{vopts}</select></div>'
            f'<div><label for="szc-cn">Days (round trip)</label><input id="szc-cn" type="number" min="1" max="20" value="3" disabled></div>'
            f'<div class="full"><label>Fleet</label>{tier_switch(note=False)}</div></div>'
            f'<div class="szc-calc-o" aria-live="polite"><span class="lbl">Estimated fare</span><div class="amt" id="szc-ca">{inr(amt0)}</div><p class="brk" id="szc-cb">One-way drop · {d0["km"]} km · fuel, driver and driver allowance included</p>'
            f'<ul><li>Tolls, parking & state entry fee extra at actuals</li><li>Final price confirmed on WhatsApp before you pay</li></ul>'
            f'<a class="szc-btn gold" id="szc-cw" href="{wa("Hi Suzu Travels")}" target="_blank" rel="noopener">Lock this fare on WhatsApp</a></div></div>')

def route_planner(p, r):
    """Compact live planner for a route page (17 Oct 2026, ENHANCEMENTS #3): fixed From/To, real road route on the map,
    drive animation auto-plays when scrolled into view, per-tier fares for every car, WhatsApp lock-in. Same #szc-plan ids as the hub,
    so kit.js runs unchanged; data-auto makes it run on scroll instead of waiting for the button."""
    if r["a"] not in PLACES or r["b"] not in PLACES:
        return ""
    pv = [dict(id=v["id"], n=v["name"], ow=v["ow"], h=v["hire"], m=v["min"], nt=v["night"], seats=v["seats"], quote=bool(v.get("quote"))) for v in FLEET]
    cfg = dict(p={k: [round(PLACES[k][0], 3), round(PLACES[k][1], 3)] for k in (r["a"], r["b"])},
               r=[dict(a=r["a"], b=r["b"], km=r["km"], f=r["f"], t=r["t"], u="")], v=pv, s=p["slug"],
               js="https://cdn.jsdelivr.net/npm/maplibre-gl@5.24.0/dist/maplibre-gl.js", css="https://cdn.jsdelivr.net/npm/maplibre-gl@5.24.0/dist/maplibre-gl.css")
    vopts = "".join(f'<option value="{v["id"]}"{" selected" if v["id"]=="sedan" else ""}>{v["name"]} · {v["seats"]} seats</option>' for v in FLEET)
    return (f'<section class="szc-sec" id="live"><span class="szc-kicker">Live road map</span><h2>Watch the {r["a"]} to {r["b"]} drive - with the fare</h2>'
            f'<p class="szc-lead">The real {r["km"]} km road from OpenStreetMap, drawn live as the car drives it. Pick a car and trip type - the fare for every fleet tier updates below, then lock it on WhatsApp.</p>'
            f'<form class="szc-plan c" id="szc-plan" data-plan=\'{esc(json.dumps(cfg, ensure_ascii=False, separators=(",", ":")))}\' data-auto="1" onsubmit="return false">'
            f'<div class="szc-pform c"><div class="szc-proute"><input id="szc-fa" type="hidden" value="{esc(r["a"])}"><input id="szc-fb" type="hidden" value="{esc(r["b"])}"><span class="szc-pa">{r["a"]}</span><i>→</i><span class="szc-pb">{r["b"]}</span>'
            f'<button type="button" class="szc-pswap" id="szc-pswap" aria-label="Reverse direction">⇄ Reverse</button></div>'
            f'<div><label for="szc-pv">Car</label><select id="szc-pv">{vopts}</select></div>'
            f'<div><label for="szc-pm">Trip</label><select id="szc-pm"><option value="one">One-way drop</option><option value="round">Round trip</option></select></div>'
            f'<div><label for="szc-pd">Date</label><input id="szc-pd" type="date"></div>'
            f'<div><label for="szc-pn">People</label><input id="szc-pn" type="number" min="1" max="45" value="2"></div>'
            f'<div class="szc-pgo"><button class="szc-btn gold" type="submit">Show route &amp; fare</button></div><p class="szc-pstat" id="szc-pstat"></p></div>'
            f'<div class="szc-mapwrap"><div class="szc-map" id="szc-map" aria-label="Road map of {esc(r["a"])} to {esc(r["b"])}"></div><div class="szc-mapidle"><b>{r["a"]} → {r["b"]} on the map</b><span>Scroll here and the drive plays on real roads - hills, tunnels and all.</span></div></div>'
            f'<div class="szc-pout" id="szc-pout"><div class="szc-pempty"><b>Fares for this road:</b> the map loads the real route and shows one-way or round-trip fares for Prime, Standard and Saver fleets - lock the price on WhatsApp in one tap.</div></div>'
            f'</form><p class="szc-note">Map data © OpenStreetMap contributors · road routing by OSRM · map tiles by OpenFreeMap. Distances and times are road estimates for planning; your WhatsApp quote is the final price.</p></section>')

def route_media(slug, stops, heading, lead):
    m = MEDIA.get(slug, {}).get("route")
    items = []
    for i, (n, t) in enumerate(stops):
        cls = ' class="end"' if i == len(stops) - 1 else ""
        items.append(f"<li{cls}><b>{n}</b><span>{t}</span></li>")
    left = f'<div class="szc-media">{video_tag(m)}</div>' if m else ""
    return (f'<section class="szc-sec" id="route"><span class="szc-kicker">Route plan</span><h2>{heading}</h2><p class="szc-lead">{lead}</p>'
            f'<div class="szc-split">{left}<ol class="szc-stops">{"".join(items)}</ol></div></section>')

def photo_tag(v, uid):
    ph = PHOTOS.get(v["id"])
    if ph:
        return f'<img src="{ph["src"]}" alt="{esc(v["photo_alt"])}" width="{ph.get("w",1280)}" height="{ph.get("h",853)}" loading="lazy" decoding="async">'
    fb = {"hycross": "crysta", "fortuner": "crysta", "tempo17": "tempo", "minibus": "urbania", "bus35": "urbania", "bus45": "urbania"}
    sid = fb.get(v["id"], v["id"])
    if MEDIA.get("svg_base"):
        return f'<img src="{MEDIA["svg_base"]}/{sid}.svg" alt="{esc(v["photo_alt"])}" width="320" height="140" loading="lazy" decoding="async" style="object-fit:contain;padding:16px">'
    return vsvg(sid, uid=uid)

def credits_block():
    items = []
    for v in FLEET:
        ph = PHOTOS.get(v["id"])
        if ph and ph.get("credit"):
            items.append(f'<li>{v["name"]} - {ph["credit"]}, <a href="{ph["lic_url"]}" rel="license noopener" target="_blank">{ph["lic"]}</a>, via <a href="{ph["page"]}" rel="noopener" target="_blank">Wikimedia Commons</a>{" (cropped)" if ph.get("cropped") else ""}</li>')
    film = MEDIA.get("film", {})
    if film.get("credit"):
        items.append(f'<li>Hero film - {film["credit"]}</li>')
    if not items:
        return ""
    return ('<details class="szc-credits"><summary>Photo credits (the cars shown are representative of each class, not the exact vehicle you will get)</summary><ul>'
            + "".join(items) + "</ul></details>")

def vehicle_cards(slug, ctx_label, ref=None):
    """Fleet gallery: type/seat filters, photo cards with 3D tilt, 'View car' opens the viewer (per-tier fares for the page's reference route)."""
    ref = ref or dict(l="Delhi → Shimla", km=345, f=1.0)
    cards = []
    for v in FLEET:
        q = wa(f"Hi Suzu Travels, I'd like a {v['name']} for {ctx_label}. Date: ___ , people: ___ (page: {slug})")
        more = f'<a class="szc-btn sm line" href="{page_url(v["page"])}">Details</a>' if v["page"] and v["page"] != slug and is_live(v["page"]) else ""
        if v.get("quote"):
            rate = '<div class="rate"><span><b>On quote</b>per trip, all-in</span><span>Luggage hold · AC</span></div>'
        else:
            ow0 = oneway(v["id"], ref["km"], ref["f"])
            rate = f'<div class="rate"><span><b>{pkm(v["hire"])}</b>round trip</span><span><b>{pinr(ow0)}</b>{esc(ref["l"])} one-way</span></div>'
        cards.append(f'<article class="szc-card szc-veh" data-type="{v["type"]}" data-seats="{v["seats"]}"><div class="szc-ph">{photo_tag(v, slug[:6] + v["id"])}'
                     f'<span class="szc-seats">{v["seats"]} seats</span><button type="button" class="szc-view" data-view="{v["id"]}">View car</button></div>'
                     f'<div class="szc-card-b"><span class="szc-tag">{v["model"]}</span><h3>{v["name"]}</h3>'
                     f'<div class="meta"><span>{v["seats"]} seats</span><span>{v["bags"]}</span><span>AC · {v["fuel"]}</span></div><p>Best for: {v["best"]}</p>{rate}'
                     f'<div class="acts"><a class="szc-btn sm wa" href="{q}" target="_blank" rel="noopener">WhatsApp quote</a>{more}</div></div></article>')
    fl = dict(s=slug, ctx=ctx_label, ref=ref, v=[dict(id=v["id"], name=v["name"], model=v["model"], seats=v["seats"], bags=v["bags"], fuel=v["fuel"], best=v["best"],
             ow=v["ow"], hire=v["hire"], min=v["min"], night=v["night"], quote=bool(v.get("quote")), page=(page_url(v["page"]) if v["page"] and is_live(v["page"]) else ""),
             photo=(PHOTOS.get(v["id"], {}).get("src", "")), alt=v["photo_alt"], credit=(PHOTOS.get(v["id"], {}).get("credit", ""))) for v in FLEET])
    types = '<span class="lbl">Type</span><button type="button" class="szc-chip on" data-ft="all">All</button>' + "".join(f'<button type="button" class="szc-chip" data-ft="{k}">{l}</button>' for k, l in VTYPES)
    seats = '<span class="lbl">Seats</span><button type="button" class="szc-chip on" data-fs="all">Any</button><button type="button" class="szc-chip" data-fs="1-4">Up to 4</button><button type="button" class="szc-chip" data-fs="5-7">5–7</button><button type="button" class="szc-chip" data-fs="8-17">8–17</button><button type="button" class="szc-chip" data-fs="18-99">18+</button><span class="szc-fcount" id="szc-fcount"></span>'
    return (f'<div id="szc-fleet" data-fleet=\'{esc(json.dumps(fl, ensure_ascii=False, separators=(",", ":")))}\'>{tier_switch()}'
            f'<div class="szc-filters">{types}</div><div class="szc-filters" style="margin-top:8px">{seats}</div>'
            f'<div class="szc-grid">{"".join(cards)}</div>{credits_block()}</div>')

def modal_block():
    return ('<div class="szc-modal" id="szc-modal" hidden role="dialog" aria-modal="true" aria-labelledby="szc-mt"><div class="szc-mbox">'
            '<button type="button" class="szc-mclose" aria-label="Close">×</button><div class="szc-mbody"></div></div></div>')

def tips(ts):
    return '<div class="szc-tips">' + "".join(f'<div class="szc-tip"><h3>{h}</h3><p>{t}</p></div>' for h, t in ts) + "</div>"

def steps():
    return '<div class="szc-steps">' + "".join(f'<div class="szc-step"><h3>{h}</h3><p>{t}</p></div>' for h, t in BOOKING_STEPS) + "</div>"

def quote_block(p, pick="", drop=""):
    vopts = "".join(f'<option>{v["name"]}</option>' for v in FLEET)
    return (f'<section class="szc-quote" id="quote"><div><span class="szc-kicker" style="color:#f1d98a">Book in 2 minutes</span><h2>Get your fixed fare now</h2>'
            f'<p>Tell us the trip and a Suzu travel desk member replies on WhatsApp with the car, driver and one all-in price. No booking fee, no spam.</p>'
            f'<p style="margin:0"><a class="szc-btn ghost sm" href="#enquiry">Prefer a call back? Request one</a></p></div>'
            f'<form class="szc-form" id="szc-qf" data-slug="{p["slug"]}" onsubmit="return false">'
            f'<div><label for="szc-qp">Pickup</label><input id="szc-qp" type="text" value="{esc(pick)}" placeholder="City, airport or station"></div>'
            f'<div><label for="szc-qd">Drop</label><input id="szc-qd" type="text" value="{esc(drop)}" placeholder="Where to?"></div>'
            f'<div><label for="szc-qt">Date</label><input id="szc-qt" type="date"></div>'
            f'<div><label for="szc-qx">People</label><input id="szc-qx" type="number" min="1" max="40" value="2"></div>'
            f'<div><label for="szc-qv">Car</label><select id="szc-qv">{vopts}</select></div>'
            f'<div><label for="szc-qr">Trip</label><select id="szc-qr"><option>One-way drop</option><option>Round trip / tour</option><option>Local sightseeing</option></select></div>'
            f'<div class="szc-btns"><button type="submit" class="szc-btn wa" id="szc-qs">Send on WhatsApp</button><a class="szc-btn ghost" href="tel:+{PHONE}">Call {PHONE_TXT}</a></div>'
            f'<small>We reply within minutes, 7 am – 11 pm. Your number is never shared.</small></form></section>')

def faq_block(faqs):
    items = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)
    return f'<section class="szc-sec" id="faq"><span class="szc-kicker">FAQ</span><h2>Questions travellers ask</h2><div class="szc-faq">{items}</div></section>'

def plain(s):
    s = re.sub(r"<[^>]+>", "", s)
    return html.unescape(s).replace("&", "and")

def jsonld(p, faqs, area):
    faq = {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": plain(q), "acceptedAnswer": {"@type": "Answer", "text": plain(a)}} for q, a in faqs]}
    svc = {"@context": "https://schema.org", "@type": "TaxiService", "name": plain(p["title"]) + " by Suzu Travels",
           "url": "https://suzutravels.com" + (page_url(p["slug"]) if p["slug"] != "cabs" else "/cabs/"),
           "areaServed": area, "provider": {"@type": "TravelAgency", "name": "Suzu Travels", "url": "https://suzutravels.com/",
           "telephone": "+91-7087488961", "address": {"@type": "PostalAddress", "streetAddress": "NH 103, Road Side, Kulahru, Tehsil Ghumarwin",
           "addressLocality": "Bilaspur", "addressRegion": "Himachal Pradesh", "addressCountry": "IN"}}}
    return ('<script type="application/ld+json">' + json.dumps(faq, ensure_ascii=False) + "</script>"
            '<script type="application/ld+json">' + json.dumps(svc, ensure_ascii=False) + "</script>")

def more_routes(current):
    cards = []
    for r in ROUTES:
        if r["slug"] == current:
            continue
        cards.append(route_card(r, current))
    return '<div class="szc-grid">' + "".join(cards[:8 if current != "cabs" else 99]) + "</div>"

def route_card(r, page_slug):
    sedan = oneway("sedan", r["km"], r["f"])
    crysta = oneway("crysta", r["km"], r["f"])
    live = r["slug"] and is_live(r["slug"])
    q = wa(f"Hi Suzu Travels, I need a {r['a']} to {r['b']} taxi. Date: ___ , people: ___ (page: {page_slug})")
    acts = (f'<a class="szc-btn sm em" href="{page_url(r["slug"])}">Route & fares</a>' if live else "") + \
           f'<a class="szc-btn sm wa" href="{q}" target="_blank" rel="noopener">WhatsApp quote</a>'
    rid = ' id="rt-' + (r["a"].lower() + "-" + r["b"].lower()).replace(" ", "-") + '"'
    if page_slug == "cabs":
        acts += f'<a class="szc-btn sm line" href="#planner" data-plan-route="{esc(r["a"] + ">" + r["b"])}">Map</a>'
    return (f'<article class="szc-card szc-route-card"{rid}><div class="rc-top"><div class="from">{r["a"]}</div><div class="to">→ {r["b"]}</div>'
            f'<div class="line"><span>{r["km"]} km</span><i></i><span>{r["t"]}</span></div></div>'
            f'<div class="szc-card-b"><div class="price">Sedan from <b>{pinr(sedan)}</b> · Innova Crysta from {pinr(crysta)}</div><div class="acts">{acts}</div></div></article>')

def related(rel):
    return '<div class="szc-links">' + "".join(f'<a href="{u}"><span>{l}{("<small>" + s + "</small>") if s else ""}</span></a>' for u, l, s in rel) + "</div>"

def js_safe(src):
    """WordPress runs wpautop/lazy-load filters over the rendered page, so any literal '<p', '<div', '<img'... inside
    the inline script gets <p>/<br />/fetchpriority injected and the script breaks. Replace every '<' inside
    single-quoted JS string literals with the escape \x3c (identical at runtime)."""
    out, i, n, instr = [], 0, len(src), False
    while i < n:
        c = src[i]
        if instr:
            if c == "\\":
                out.append(src[i:i + 2]); i += 2; continue
            if c == "'":
                instr = False
            elif c == "<":
                out.append("\\x3c"); i += 1; continue
        elif c == "'":
            instr = True
        out.append(c); i += 1
    return "".join(out)

JS = js_safe((ROOT / "kit.js").read_text())
# Hub-only planner extension (multi-stop, 25 Oct 2026): kit_hub.js is inserted INSIDE the planner block of kit.js right after
# the IntersectionObserver line, so it can reuse the planner's functions; kit_hub.css is appended to the hub's <style>.
# Child pages keep plain kit.js/kit.css (no republish needed). Fold both into kit.js/kit.css at the next global kit change.
_HUB_ANCHOR = "io.observe(mapBox);}catch(e){}\n"
assert JS.count(_HUB_ANCHOR) == 1, "kit_hub.js anchor not found in kit.js"
HUB_JS = JS.replace(_HUB_ANCHOR, _HUB_ANCHOR + js_safe(re.sub(r"/\*.*?\*/", "", (ROOT / "kit_hub.js").read_text(), flags=re.S)))
HUB_CSS = (ROOT / "kit_hub.css").read_text()
HUB_JS = HUB_JS.replace("__SEATMAP_BASE__", MEDIA.get("seatmaps", {}).get("base", ""))
# 30 Oct 2026 hub size budget: hub-only JS tighten - drop /* */ section comments and the indentation/line-join space after
# a line ending in ; { } or , (line boundaries are never inside a string literal in the kit's ES5 code). Children unchanged.
def _tight(js):
    js = re.sub(r"/\*.*?\*/", "", js, flags=re.S)
    out = ""
    for ln in js.split("\n"):
        ln = ln.strip()
        if not ln:
            continue
        out += ln if (not out or out[-1] in ";{},") else "\n" + ln
    return out
# HUB_JS = _tight(HUB_JS)  # not applied yet: rewrites the whole script (61 diff ops) — use at the next full hub rewrite

def wrap(body, p, faqs, area, js=None):
    return f'<div class="szc" data-szc="{p["slug"]}" data-tier="standard">{body}{modal_block()}{jsonld(p, faqs, area)}<script>{js or JS}</script></div>'

# ---------------------------------------------------------------- pages
def build_route(p):
    r = ROUTE_BY_SLUG[p["route"]]
    sed = oneway("sedan", r["km"], r["f"])
    if inr(sed) not in p["seo_title"]:
        sys.exit(f"FARE MISMATCH in {p['slug']}: seo_title vs engine {inr(sed)}")
    chips = [f'<b>{r["km"]} km</b> · {r["t"]}', f'Sedan from <b>{inr(sed)}</b>', f'Innova from <b>{inr(oneway("crysta", r["km"], r["f"]))}</b>', "Hatchback → Tempo Traveller", "One-way or round trip"]
    dests = [dict(l=f'{r["a"]} → {r["b"]}', km=r["km"], f=r["f"]), dict(l=f'{r["b"]} → {r["a"]}', km=r["km"], f=r["f"])]
    body = hero(p, chips) + nav([("overview", "Overview"), ("fares", "Fares"), ("live", "Live map"), ("route", "Route"), ("cars", "Cars"), ("tips", "Tips"), ("faq", "FAQ")])
    body += (f'<section class="szc-sec" id="overview"><span class="szc-kicker">At a glance</span><h2>{p["title"]}: distance, time and fare</h2>'
             f'<div class="szc-answer">{p["answer"]}</div>{facts(p["facts"])}</section>')
    body += (f'<section class="szc-sec alt" id="fares"><span class="szc-kicker">Fares 2026</span><h2>{r["a"]} to {r["b"]} taxi fare</h2>'
             f'<p class="szc-lead">Indicative starting prices for off-season weekdays. Same fare for the return direction ({r["b"]} to {r["a"]}).</p>'
             f'{fare_table_route(r, p["slug"])}{includes()}<h3 style="margin-top:34px">Fare calculator</h3>{calculator(dests, p["slug"])}</section>')
    body += route_planner(p, r)
    body += route_media(p["slug"], p["stops"], f'{r["a"]} to {r["b"]} by road, stop by stop', f'The route our drivers take, with the stops worth making.')
    body += f'<section class="szc-sec alt" id="cars"><span class="szc-kicker">Our fleet</span><h2>Choose your car for {r["b"]}</h2>{vehicle_cards(p["slug"], r["a"] + " to " + r["b"], dests[0])}</section>'
    body += f'<section class="szc-sec" id="tips"><span class="szc-kicker">Know before you go</span><h2>Road tips for {r["a"]} to {r["b"]}</h2>{tips(p["tips"])}</section>'
    body += f'<section class="szc-sec alt" id="booking"><span class="szc-kicker">How booking works</span><h2>Booked in four simple steps</h2>{steps()}</section>'
    body += quote_block(p, r["a"], r["b"])
    body += f'<section class="szc-sec" id="more"><span class="szc-kicker">More cab routes</span><h2>Other popular taxi routes</h2>{more_routes(p["slug"])}<h3 style="margin-top:30px">Plan the rest of the trip</h3>{related(p["related"])}</section>'
    body += faq_block(p["faqs"])
    return wrap(body, p, p["faqs"], [r["a"], r["b"]])

def local_table(lr):
    head = "".join(f"<th>{h}</th>" for h in lr["head"])
    rows = "".join("<tr>" + "".join((f"<td><b>{c}</b></td>" if i == 0 else f'<td class="num">{c}</td>') for i, c in enumerate(row)) + "</tr>" for row in lr["rows"])
    return f'<div class="szc-scroll"><table class="szc-tbl"><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div><p class="szc-note">{lr["note"]}</p>'

def outstation_table(outs, slug):
    rows = []
    for a, b, km, f in outs:
        link = next((r["slug"] for r in ROUTES if r["slug"] and is_live(r["slug"]) and {r["a"], r["b"]} == {a, b}), None)
        name = f'<a href="{page_url(link)}">{a} → {b}</a>' if link else f"{a} → {b}"
        rows.append(f'<tr><td><b>{name}</b></td><td>{km} km</td><td class="num">{pinr(oneway("sedan", km, f))}</td><td class="num">{pinr(oneway("ertiga", km, f))}</td><td class="num">{pinr(oneway("crysta", km, f))}</td></tr>')
    return ('<div class="szc-scroll"><table class="szc-tbl"><thead><tr><th>One-way drop</th><th>Distance</th><th>Sedan</th><th>Ertiga</th><th>Innova Crysta</th></tr></thead><tbody>'
            + "".join(rows) + "</tbody></table></div>")

def build_city(p):
    town = p.get("town") or p["map"]["hub"]   # 26 Oct 2026: city/tour pages may use a path map (e.g. char-dham-yatra-taxi) and set town
    outs = p["outstation"]
    chips = p.get("chips") or [f"Local sightseeing", f"Outstation drops", f'To {outs[0][1]} from <b>{inr(oneway("sedan", outs[0][2], outs[0][3]))}</b>', "Hatchback → Tempo Traveller", "24×7 WhatsApp"]
    dests = [dict(l=f"{a} → {b}", km=km, f=f) for a, b, km, f in outs]
    body = hero(p, chips) + nav([("overview", "Overview"), ("fares", "Rates"), ("route", "Trips"), ("cars", "Cars"), ("tips", "Tips"), ("faq", "FAQ")])
    body += (f'<section class="szc-sec" id="overview"><span class="szc-kicker">At a glance</span><h2>{p["title"]}: rates and trips</h2>'
             f'<div class="szc-answer">{p["answer"]}</div>{facts(p["facts"])}</section>')
    body += (f'<section class="szc-sec alt" id="fares"><span class="szc-kicker">Rates 2026</span><h2>{p.get("rates_h") or town + " local taxi rates"}</h2>{local_table(p["local_rates"])}'
             f'<h3 style="margin-top:34px">{p.get("out_h") or "Outstation taxi from " + town}</h3>{outstation_table(outs, p["slug"])}{includes()}'
             f'<h3 style="margin-top:34px">Fare calculator</h3>{calculator(dests, p["slug"])}</section>')
    body += route_media(p["slug"], p["stops"], p.get("route_h") or f"Popular taxi trips from {town}", p.get("route_lead") or f"Where our {town} cabs go most, and what each trip is known for.")
    body += f'<section class="szc-sec alt" id="cars"><span class="szc-kicker">Our fleet</span><h2>Cars available {p.get("in_town") or "in " + town}</h2>{vehicle_cards(p["slug"], town, dests[0])}</section>'
    body += f'<section class="szc-sec" id="tips"><span class="szc-kicker">Know before you go</span><h2>Good to know about taxis {p.get("in_town") or "in " + town}</h2>{tips(p["tips"])}</section>'
    body += f'<section class="szc-sec alt" id="booking"><span class="szc-kicker">How booking works</span><h2>Booked in four simple steps</h2>{steps()}</section>'
    body += quote_block(p, town, "")
    body += f'<section class="szc-sec" id="more"><span class="szc-kicker">More cab routes</span><h2>Popular routes to and from the hills</h2>{more_routes(p["slug"])}<h3 style="margin-top:30px">Plan the rest of the trip</h3>{related(p["related"])}</section>'
    body += faq_block(p["faqs"])
    return wrap(body, p, p["faqs"], p.get("area") or [town, "Himachal Pradesh"])

def build_vehicle(p):
    v = FLEET_BY_ID[p["vehicle"]]
    if p.get("title_fare") and inr(oneway(*p["title_fare"])) not in p["seo_title"]:
        sys.exit(f"FARE MISMATCH in {p['slug']}: seo_title vs engine {inr(oneway(*p['title_fare']))}")
    # optional per-page overrides (18 Oct 2026, city-based vehicle pages e.g. tempo-traveller-chandigarh): vs, ow_routes, ow_h, chips, pick, trips_lead, area
    vs = [FLEET_BY_ID[x] for x in p["vs"]] if p.get("vs") else [v] + ([FLEET_BY_ID["urbania"]] if v["id"] == "tempo" else [FLEET_BY_ID["ertiga"]])
    chips = p.get("chips") or [f'From <b>₹{v["hire"]}/km</b>', "250 km / day minimum", f'{v["seats"]} seats · {v["bags"]}', "Driver included", "Delhi · Chandigarh pickup"]
    if p.get("ow_routes"):
        top = [dict(slug=next((r["slug"] for r in ROUTES if r["slug"] and {r["a"], r["b"]} == {a, b}), None), a=a, b=b, km=km, f=f) for a, b, km, f in p["ow_routes"]]
    else:
        top = [r for r in ROUTES if r["a"] in ("Delhi", "Chandigarh", "Pathankot", "Jammu")][:12]
    dests = [dict(l=f'{r["a"]} → {r["b"]}', km=r["km"], f=r["f"]) for r in top]
    rate_rows = "".join(f'<tr><td><b>{x["name"]}</b><br><small>{x["model"]}</small></td><td>{x["seats"]}</td><td class="num">{pkm(x["hire"])}</td><td>250 km/day</td><td class="num">₹{x["night"]}/night</td></tr>' for x in vs)
    rate_tbl = f'<div class="szc-scroll"><table class="szc-tbl"><thead><tr><th>Vehicle</th><th>Seats</th><th>Round trip rate</th><th>Minimum</th><th>Driver allowance</th></tr></thead><tbody>{rate_rows}</tbody></table></div>'
    ow_rows = "".join(
        f'<tr><td><b>{("<a href=" + chr(34) + page_url(r["slug"]) + chr(34) + ">" + r["a"] + " → " + r["b"] + "</a>") if r["slug"] and is_live(r["slug"]) else r["a"] + " → " + r["b"]}</b></td><td>{r["km"]} km</td>'
        + "".join(f'<td class="num">{pinr(oneway(x["id"], r["km"], r["f"]))}</td>' for x in vs) + "</tr>" for r in top)
    ow_tbl = (f'<div class="szc-scroll"><table class="szc-tbl"><thead><tr><th>One-way drop</th><th>Distance</th>' + "".join(f"<th>{x['name']}</th>" for x in vs)
              + f"</tr></thead><tbody>{ow_rows}</tbody></table></div>")
    body = hero(p, chips) + nav([("overview", "Overview"), ("fares", "Rates"), ("route", "Trips"), ("cars", "Fleet"), ("tips", "Tips"), ("faq", "FAQ")])
    body += (f'<section class="szc-sec" id="overview"><span class="szc-kicker">At a glance</span><h2>{p["title"]}: rates and what you get</h2>'
             f'<div class="szc-answer">{p["answer"]}</div>{facts(p["facts"])}</section>')
    body += (f'<section class="szc-sec alt" id="fares"><span class="szc-kicker">Rates 2026</span><h2>{v["name"]} rent per km and per day</h2>{rate_tbl}'
             f'<h3 style="margin-top:34px">{p.get("ow_h") or "One-way drops from Delhi, Chandigarh, Pathankot & Jammu"}</h3>{ow_tbl}{includes()}'
             f'<h3 style="margin-top:34px">Fare calculator</h3>{calculator(dests, p["slug"], default_vehicle=v["id"])}</section>')
    body += route_media(p["slug"], p["stops"], f"Where groups take our {v['name']}", p.get("trips_lead") or "The trips this vehicle does most, from Delhi NCR and Chandigarh.")
    body += f'<section class="szc-sec alt" id="cars"><span class="szc-kicker">Our fleet</span><h2>Compare every car we run</h2>{vehicle_cards(p["slug"], "my trip", dests[0])}</section>'
    body += f'<section class="szc-sec" id="tips"><span class="szc-kicker">Know before you go</span><h2>Good to know before you book</h2>{tips(p["tips"])}</section>'
    body += f'<section class="szc-sec alt" id="booking"><span class="szc-kicker">How booking works</span><h2>Booked in four simple steps</h2>{steps()}</section>'
    body += quote_block(p, p.get("pick") or "Delhi", "")
    body += f'<section class="szc-sec" id="more"><span class="szc-kicker">Cab routes</span><h2>Popular routes for this vehicle</h2>{more_routes(p["slug"])}<h3 style="margin-top:30px">Plan the rest of the trip</h3>{related(p["related"])}</section>'
    body += faq_block(p["faqs"])
    return wrap(body, p, p["faqs"], p.get("area") or ["Delhi", "Chandigarh", "Himachal Pradesh", "Uttarakhand"])

def _css_rules(css):
    """Split minified CSS into (selector, body, is_at_rule) at top level."""
    i, out = 0, []
    while i < len(css):
        j = css.find("{", i)
        if j < 0:
            break
        sel = css[i:j]
        if sel.startswith("@"):
            depth, k = 1, j + 1
            while depth:
                depth += {"{": 1, "}": -1}.get(css[k], 0)
                k += 1
            out.append((sel, css[j + 1:k - 1], True)); i = k
        else:
            k = css.find("}", j); out.append((sel, css[j + 1:k], False)); i = k + 1
    return out

def prune_css(css, used):
    """30 Oct 2026 (hub size budget, hub only): drop rules whose every selector needs a .szc-* class that appears nowhere
    in the page markup or script (route/city-page-only components such as .szc-stops, .szc-answer). Substring test = conservative."""
    def dead(sel):
        for s in sel.split(","):
            cls = re.findall(r"\.(szc-[\w-]+)", s)
            if not cls or all(c in used for c in cls):
                return False
        return True
    out = ""
    for sel, body, at in _css_rules(css):
        if at:
            inner = "".join(f"{s2}{{{b2}}}" for s2, b2, _ in _css_rules(body) if not dead(s2))
            if inner or not sel.startswith("@media"):
                out += f"{sel}{{{inner if sel.startswith('@media') else body}}}"
        elif not dead(sel):
            out += f"{sel}{{{body}}}"
    return out

def finish(slug, h, css_extra=""):
    h = re.sub(r"&(?![a-zA-Z]+;|#\d+;)", "&amp;", h.split("<script>")[0]) + ("<script>" + "<script>".join(h.split("<script>")[1:]) if "<script>" in h else "")
    problems = re.findall(r"\{\{.*?\}\}|TODO|XXX", h)
    if problems:
        sys.exit(f"BUILD REFUSED {slug}: {problems}")
    (OUT / f"{slug}.html").write_text(h, encoding="utf-8")
    m = f"<style>{min_css(KIT_CSS + css_extra)}</style>" + min_html(h)
    if "&&" in m.split("<script>", 1)[-1]:
        sys.exit(f"BUILD REFUSED {slug}: '&&' in script would be mangled by WordPress convert_chars")
    if re.search(r'="[^"<]*>[^"<]*"', m.split("<script>", 1)[0]):
        sys.exit(f"BUILD REFUSED {slug}: literal '>' inside an attribute value (wptexturize breaks the closing quote) — use &gt;")
    if slug == "cabs":  # 28 Oct 2026 hub size budget: '"' needs no escaping inside the single-quoted data-cfg/fleet/plan JSON (saves ~11 KB)
        m = re.sub(r"data-(cfg|fleet|plan)='[^']*'", lambda x: x.group(0).replace("&quot;", '"'), m)
    if slug == "cabs":
        st = m.split("<style>", 1)[1].split("</style>", 1)[0]
        m = m.replace(f"<style>{st}</style>", f"<style>{prune_css(st, m.replace(st, ''))}</style>", 1)
    kitjs = m.rsplit("<script>", 1)[-1].split("</script>")[0]
    if re.search(r"<(/|p\b|div\b|table\b|img\b|ul\b|ol\b|li\b|span\b|br\b|svg\b|button\b|details\b|summary\b|small\b|b\b|a\b|h[1-6]\b|t[rdh]\b|thead\b|tbody\b|circle\b|path\b)", kitjs):
        sys.exit(f"BUILD REFUSED {slug}: HTML tag inside kit script (wpautop would inject <p>) — use \\x3c")
    (OUT / f"{slug}.min.html").write_text(m, encoding="utf-8")
    return len(m)

if __name__ == "__main__":
    import hub
    only = sys.argv[1:]
    for p in PAGES:
        if only and p["slug"] not in only:
            continue
        h = {"route": build_route, "city": build_city, "vehicle": build_vehicle}[p["kind"]](p)
        print(p["slug"], finish(p["slug"], h))
    if not only or "cabs" in only:
        print("cabs", finish("cabs", hub.build(), HUB_CSS))
