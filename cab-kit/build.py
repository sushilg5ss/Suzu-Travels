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

def video_tag(m, cls="", eager=False):
    if not m:
        return ""
    pre = "auto" if eager else "metadata"
    return (f'<video class="{cls}" autoplay muted loop playsinline preload="{pre}" poster="{m["poster"]}" width="{m.get("w",1600)}" height="{m.get("h",900)}">'
            f'<source src="{m["webm"]}" type="video/webm"><source src="{m["mp4"]}" type="video/mp4"></video>')

# ---------------------------------------------------------------- blocks
def hero(p, chips):
    trust = (f'<div class="szc-trust"><span><a href="/certificates/">{REG}</a></span><span>GST registered</span>'
             f'<span>{RATING}</span><span>24×7 WhatsApp {PHONE_TXT}</span></div>')
    chip_html = "".join(f"<li>{c}</li>" for c in chips)
    return (f'<section class="szc-hero">{video_tag(MEDIA.get(p["slug"], {}).get("hero") or MEDIA.get("hero"), eager=True)}<div class="szc-hero-in">'
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
    for v in FLEET:
        ow = oneway(v["id"], r["km"], r["f"])
        q = wa(f"Hi Suzu Travels, quote for {r['a']} to {r['b']} in {v['name']}. Date: ___ , people: ___ (page: {slug})")
        rows.append(f'<tr><td><b>{v["name"]}</b><br><small>{v["model"]}</small></td><td>{v["seats"]}</td><td class="num">{inr(ow)}</td>'
                    f'<td class="num">₹{v["hire"]}/km</td><td><a class="szc-btn sm line" href="{q}" target="_blank" rel="noopener">Quote</a></td></tr>')
    return ('<div class="szc-scroll"><table class="szc-tbl"><thead><tr><th>Car</th><th>Seats</th><th>One-way from</th><th>Round trip</th><th></th></tr></thead><tbody>'
            + "".join(rows) + "</tbody></table></div>")

def includes():
    return '<ul class="szc-note" style="padding-left:18px;margin-top:14px">' + "".join(f"<li>{x}</li>" for x in COMMON_INCLUDES) + "</ul>"

def calculator(dests, slug, default_vehicle="sedan"):
    veh = [dict(id=v["id"], n=v["name"], ow=v["ow"], h=v["hire"], m=v["min"], nt=v["night"]) for v in FLEET]
    data = json.dumps(dict(v=veh, d=dests, s=slug), ensure_ascii=False, separators=(",", ":"))
    dopts = "".join(f'<option value="{i}">{esc(d["l"])}</option>' for i, d in enumerate(dests))
    vopts = "".join(f'<option value="{v["id"]}"{" selected" if v["id"]==default_vehicle else ""}>{v["name"]} ({v["seats"]} seats)</option>' for v in FLEET)
    d0 = dests[0]; amt0 = oneway(default_vehicle, d0["km"], d0["f"])
    return (f'<div class="szc-calc" id="szc-calc" data-cfg=\'{esc(data)}\'>'
            f'<div class="szc-calc-f"><div class="full"><label for="szc-cd">Route</label><select id="szc-cd">{dopts}</select></div>'
            f'<div class="full"><label>Trip type</label><div class="szc-seg" role="group"><button type="button" class="on" data-m="one">One-way drop</button><button type="button" data-m="round">Round trip / tour</button></div></div>'
            f'<div><label for="szc-cv">Car</label><select id="szc-cv">{vopts}</select></div>'
            f'<div><label for="szc-cn">Days (round trip)</label><input id="szc-cn" type="number" min="1" max="20" value="3" disabled></div></div>'
            f'<div class="szc-calc-o" aria-live="polite"><span class="lbl">Estimated fare</span><div class="amt" id="szc-ca">{inr(amt0)}</div><p class="brk" id="szc-cb">One-way drop · {d0["km"]} km · fuel, driver and driver allowance included</p>'
            f'<ul><li>Tolls, parking & state entry fee extra at actuals</li><li>Final price confirmed on WhatsApp before you pay</li></ul>'
            f'<a class="szc-btn gold" id="szc-cw" href="{wa("Hi Suzu Travels")}" target="_blank" rel="noopener">Lock this fare on WhatsApp</a></div></div>')

def route_media(slug, stops, heading, lead):
    m = MEDIA.get(slug, {}).get("route")
    items = []
    for i, (n, t) in enumerate(stops):
        cls = ' class="end"' if i == len(stops) - 1 else ""
        items.append(f"<li{cls}><b>{n}</b><span>{t}</span></li>")
    left = f'<div class="szc-media">{video_tag(m)}</div>' if m else ""
    return (f'<section class="szc-sec" id="route"><span class="szc-kicker">Route plan</span><h2>{heading}</h2><p class="szc-lead">{lead}</p>'
            f'<div class="szc-split">{left}<ol class="szc-stops">{"".join(items)}</ol></div></section>')

def vehicle_cards(slug, ctx_label):
    cards = []
    for v in FLEET:
        q = wa(f"Hi Suzu Travels, I'd like a {v['name']} for {ctx_label}. Date: ___ , people: ___ (page: {slug})")
        more = f'<a class="szc-btn sm line" href="{page_url(v["page"])}">Details</a>' if v["page"] and v["page"] != slug and is_live(v["page"]) else ""
        img = f'<img src="{MEDIA.get("svg_base","")}/{v["id"]}.svg" alt="{v["name"]} ({v["model"]}) illustration" width="320" height="140" loading="lazy" decoding="async">' if MEDIA.get("svg_base") else vsvg(v["id"], uid=slug[:6] + v["id"])
        cards.append(f'<article class="szc-card szc-veh">{img}<div class="szc-card-b"><span class="szc-tag">{v["model"]}</span><h3>{v["name"]}</h3>'
                     f'<div class="meta"><span>{v["seats"]} seats</span><span>{v["bags"]}</span><span>AC · {v["fuel"]}</span></div><p>Best for: {v["best"]}</p>'
                     f'<div class="acts"><a class="szc-btn sm wa" href="{q}" target="_blank" rel="noopener">WhatsApp quote</a>{more}</div></div></article>')
    return '<div class="szc-grid">' + "".join(cards) + "</div>"

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
    rid = f' id="rt-{r["a"].lower()}-{r["b"].lower()}"'.replace(" ", "-")
    return (f'<article class="szc-card szc-route-card"{rid}><div class="rc-top"><div class="from">{r["a"]}</div><div class="to">→ {r["b"]}</div>'
            f'<div class="line"><span>{r["km"]} km</span><i></i><span>{r["t"]}</span></div></div>'
            f'<div class="szc-card-b"><div class="price">Sedan from <b>{inr(sedan)}</b> · Innova Crysta from {inr(crysta)}</div><div class="acts">{acts}</div></div></article>')

def related(rel):
    return '<div class="szc-links">' + "".join(f'<a href="{u}"><span>{l}{("<small>" + s + "</small>") if s else ""}</span></a>' for u, l, s in rel) + "</div>"

JS = (ROOT / "kit.js").read_text()

def wrap(body, p, faqs, area):
    return f'<div class="szc" data-szc="{p["slug"]}">{body}{jsonld(p, faqs, area)}<script>{JS}</script></div>'

# ---------------------------------------------------------------- pages
def build_route(p):
    r = ROUTE_BY_SLUG[p["route"]]
    sed = oneway("sedan", r["km"], r["f"])
    if inr(sed) not in p["seo_title"]:
        sys.exit(f"FARE MISMATCH in {p['slug']}: seo_title vs engine {inr(sed)}")
    chips = [f'<b>{r["km"]} km</b> · {r["t"]}', f'Sedan from <b>{inr(sed)}</b>', f'Innova from <b>{inr(oneway("crysta", r["km"], r["f"]))}</b>', "Hatchback → Tempo Traveller", "One-way or round trip"]
    dests = [dict(l=f'{r["a"]} → {r["b"]}', km=r["km"], f=r["f"]), dict(l=f'{r["b"]} → {r["a"]}', km=r["km"], f=r["f"])]
    body = hero(p, chips) + nav([("overview", "Overview"), ("fares", "Fares"), ("route", "Route"), ("cars", "Cars"), ("tips", "Tips"), ("faq", "FAQ")])
    body += (f'<section class="szc-sec" id="overview"><span class="szc-kicker">At a glance</span><h2>{p["title"]}: distance, time and fare</h2>'
             f'<div class="szc-answer">{p["answer"]}</div>{facts(p["facts"])}</section>')
    body += (f'<section class="szc-sec alt" id="fares"><span class="szc-kicker">Fares 2026</span><h2>{r["a"]} to {r["b"]} taxi fare</h2>'
             f'<p class="szc-lead">Indicative starting prices for off-season weekdays. Same fare for the return direction ({r["b"]} to {r["a"]}).</p>'
             f'{fare_table_route(r, p["slug"])}{includes()}<h3 style="margin-top:34px">Fare calculator</h3>{calculator(dests, p["slug"])}</section>')
    body += route_media(p["slug"], p["stops"], f'{r["a"]} to {r["b"]} by road, stop by stop', f'The route our drivers take, with the stops worth making.')
    body += f'<section class="szc-sec alt" id="cars"><span class="szc-kicker">Our fleet</span><h2>Choose your car for {r["b"]}</h2>{vehicle_cards(p["slug"], r["a"] + " to " + r["b"])}</section>'
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
        rows.append(f'<tr><td><b>{name}</b></td><td>{km} km</td><td class="num">{inr(oneway("sedan", km, f))}</td><td class="num">{inr(oneway("ertiga", km, f))}</td><td class="num">{inr(oneway("crysta", km, f))}</td></tr>')
    return ('<div class="szc-scroll"><table class="szc-tbl"><thead><tr><th>One-way drop</th><th>Distance</th><th>Sedan</th><th>Ertiga</th><th>Innova Crysta</th></tr></thead><tbody>'
            + "".join(rows) + "</tbody></table></div>")

def build_city(p):
    town = p["map"]["hub"]
    outs = p["outstation"]
    chips = [f"Local sightseeing", f"Outstation drops", f'To Chandigarh from <b>{inr(oneway("sedan", outs[0][2], outs[0][3]))}</b>', "Hatchback → Tempo Traveller", "24×7 WhatsApp"]
    dests = [dict(l=f"{a} → {b}", km=km, f=f) for a, b, km, f in outs]
    body = hero(p, chips) + nav([("overview", "Overview"), ("fares", "Rates"), ("route", "Trips"), ("cars", "Cars"), ("tips", "Tips"), ("faq", "FAQ")])
    body += (f'<section class="szc-sec" id="overview"><span class="szc-kicker">At a glance</span><h2>{p["title"]}: rates and trips</h2>'
             f'<div class="szc-answer">{p["answer"]}</div>{facts(p["facts"])}</section>')
    body += (f'<section class="szc-sec alt" id="fares"><span class="szc-kicker">Rates 2026</span><h2>{town} local taxi rates</h2>{local_table(p["local_rates"])}'
             f'<h3 style="margin-top:34px">Outstation taxi from {town}</h3>{outstation_table(outs, p["slug"])}{includes()}'
             f'<h3 style="margin-top:34px">Fare calculator</h3>{calculator(dests, p["slug"])}</section>')
    body += route_media(p["slug"], p["stops"], f"Popular taxi trips from {town}", f"Where our {town} cabs go most, and what each trip is known for.")
    body += f'<section class="szc-sec alt" id="cars"><span class="szc-kicker">Our fleet</span><h2>Cars available in {town}</h2>{vehicle_cards(p["slug"], town)}</section>'
    body += f'<section class="szc-sec" id="tips"><span class="szc-kicker">Know before you go</span><h2>Good to know about taxis in {town}</h2>{tips(p["tips"])}</section>'
    body += f'<section class="szc-sec alt" id="booking"><span class="szc-kicker">How booking works</span><h2>Booked in four simple steps</h2>{steps()}</section>'
    body += quote_block(p, town, "")
    body += f'<section class="szc-sec" id="more"><span class="szc-kicker">More cab routes</span><h2>Popular routes to and from the hills</h2>{more_routes(p["slug"])}<h3 style="margin-top:30px">Plan the rest of the trip</h3>{related(p["related"])}</section>'
    body += faq_block(p["faqs"])
    return wrap(body, p, p["faqs"], [town, "Himachal Pradesh"])

def build_vehicle(p):
    v = FLEET_BY_ID[p["vehicle"]]
    vs = [v] + ([FLEET_BY_ID["urbania"]] if v["id"] == "tempo" else [FLEET_BY_ID["ertiga"]])
    chips = [f'From <b>₹{v["hire"]}/km</b>', "250 km / day minimum", f'{v["seats"]} seats · {v["bags"]}', "Driver included", "Delhi · Chandigarh pickup"]
    top = [r for r in ROUTES if r["a"] in ("Delhi", "Chandigarh", "Pathankot", "Jammu")][:12]
    dests = [dict(l=f'{r["a"]} → {r["b"]}', km=r["km"], f=r["f"]) for r in top]
    rate_rows = "".join(f'<tr><td><b>{x["name"]}</b><br><small>{x["model"]}</small></td><td>{x["seats"]}</td><td class="num">₹{x["hire"]}/km</td><td>250 km/day</td><td class="num">₹{x["night"]}/night</td></tr>' for x in vs)
    rate_tbl = f'<div class="szc-scroll"><table class="szc-tbl"><thead><tr><th>Vehicle</th><th>Seats</th><th>Round trip rate</th><th>Minimum</th><th>Driver allowance</th></tr></thead><tbody>{rate_rows}</tbody></table></div>'
    ow_rows = "".join(
        f'<tr><td><b>{("<a href=" + chr(34) + page_url(r["slug"]) + chr(34) + ">" + r["a"] + " → " + r["b"] + "</a>") if r["slug"] and is_live(r["slug"]) else r["a"] + " → " + r["b"]}</b></td><td>{r["km"]} km</td>'
        + "".join(f'<td class="num">{inr(oneway(x["id"], r["km"], r["f"]))}</td>' for x in vs) + "</tr>" for r in top)
    ow_tbl = (f'<div class="szc-scroll"><table class="szc-tbl"><thead><tr><th>One-way drop</th><th>Distance</th>' + "".join(f"<th>{x['name']}</th>" for x in vs)
              + f"</tr></thead><tbody>{ow_rows}</tbody></table></div>")
    body = hero(p, chips) + nav([("overview", "Overview"), ("fares", "Rates"), ("route", "Trips"), ("cars", "Fleet"), ("tips", "Tips"), ("faq", "FAQ")])
    body += (f'<section class="szc-sec" id="overview"><span class="szc-kicker">At a glance</span><h2>{p["title"]}: rates and what you get</h2>'
             f'<div class="szc-answer">{p["answer"]}</div>{facts(p["facts"])}</section>')
    body += (f'<section class="szc-sec alt" id="fares"><span class="szc-kicker">Rates 2026</span><h2>{v["name"]} rent per km and per day</h2>{rate_tbl}'
             f'<h3 style="margin-top:34px">One-way drops from Delhi, Chandigarh, Pathankot & Jammu</h3>{ow_tbl}{includes()}'
             f'<h3 style="margin-top:34px">Fare calculator</h3>{calculator(dests, p["slug"], default_vehicle=v["id"])}</section>')
    body += route_media(p["slug"], p["stops"], f"Where groups take our {v['name']}", "The trips this vehicle does most, from Delhi NCR and Chandigarh.")
    body += f'<section class="szc-sec alt" id="cars"><span class="szc-kicker">Our fleet</span><h2>Compare every car we run</h2>{vehicle_cards(p["slug"], "my trip")}</section>'
    body += f'<section class="szc-sec" id="tips"><span class="szc-kicker">Know before you go</span><h2>Good to know before you book</h2>{tips(p["tips"])}</section>'
    body += f'<section class="szc-sec alt" id="booking"><span class="szc-kicker">How booking works</span><h2>Booked in four simple steps</h2>{steps()}</section>'
    body += quote_block(p, "Delhi", "")
    body += f'<section class="szc-sec" id="more"><span class="szc-kicker">Cab routes</span><h2>Popular routes for this vehicle</h2>{more_routes(p["slug"])}<h3 style="margin-top:30px">Plan the rest of the trip</h3>{related(p["related"])}</section>'
    body += faq_block(p["faqs"])
    return wrap(body, p, p["faqs"], ["Delhi", "Chandigarh", "Himachal Pradesh", "Uttarakhand"])

def finish(slug, h):
    h = re.sub(r"&(?![a-zA-Z]+;|#\d+;)", "&amp;", h.split("<script>")[0]) + ("<script>" + "<script>".join(h.split("<script>")[1:]) if "<script>" in h else "")
    problems = re.findall(r"\{\{.*?\}\}|TODO|XXX", h)
    if problems:
        sys.exit(f"BUILD REFUSED {slug}: {problems}")
    (OUT / f"{slug}.html").write_text(h, encoding="utf-8")
    m = f"<style>{min_css(KIT_CSS)}</style>" + min_html(h)
    if "&&" in m.split("<script>", 1)[-1]:
        sys.exit(f"BUILD REFUSED {slug}: '&&' in script would be mangled by WordPress convert_chars")
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
        print("cabs", finish("cabs", hub.build()))
