# -*- coding: utf-8 -*-
"""The /cabs/ hub page (page ID 10080)."""
import json
from build import *
from cabs_data import TIERS, PRICED, PLACES, PICKUPS

HUB = dict(slug="cabs", title="Cab & Taxi Booking — Delhi, Chandigarh & Himachal",
    seo_title="Himachal & North India Cab Booking | One-Way Taxi Fares",
    seo_desc="Book cabs from Delhi, Chandigarh, Pathankot & Jammu to Shimla, Manali, Dharamshala, Kashmir & Uttarakhand. Sedan to Tempo Traveller, one-way fares.",
    focus="himachal cab service",
    kicker="Suzu Cabs · North India",
    tag="Cabs and taxis for the hills, from a Himachal-based team",
    sub="One-way drops, round trips and full tours from Delhi, Chandigarh, Pathankot and Jammu to Shimla, Manali, Dharamshala, Kashmir and Uttarakhand — hatchback to 45-seat coach, in the fleet tier you choose.",
    wa="Hi Suzu Travels, I need a cab. From: ___ , to: ___ , date: ___ , people: ___")

FAQS = [
 ("How do I book a cab with Suzu Travels?", "Send the pickup, drop, date and number of people on WhatsApp (+91 70874 88961) or use the form on this page. You get one clear quote with the car and total fare, confirm with a small advance on our payment page, and receive the driver's details the day before."),
 ("Do you offer one-way taxis to Shimla and Manali?", "Yes. One-way drops are our most booked service — for example Delhi to Shimla from about ₹5,199 and Chandigarh to Manali from about ₹4,199 in a sedan. The fare already covers the car's empty return."),
 ("What is included in your cab fare?", "One-way fares include the AC car, fuel, driver and driver allowance. Tolls, parking and state entry tax or permits are extra at actuals and are shown in your quote before you pay."),
 ("What are your per-km rates for round trips?", "Round trips and tours are billed per kilometre with a 250 km daily minimum: about ₹11/km hatchback, ₹12 sedan, ₹14 Ertiga, ₹16 Kia Carens, ₹19 Innova Crysta, ₹26 Tempo Traveller and ₹36 Force Urbania, plus driver allowance per night."),
 ("Can your cab do sightseeing in Manali, Solang and Rohtang?", "Sightseeing around Manali (Solang, Atal Tunnel, Rohtang) is done in Manali-registered local taxis as per union practice. We book the local taxi for you at union rates on the same chat."),
 ("Which pickup points do you cover?", "All of Delhi NCR (including IGI Airport and the main stations), Chandigarh–Mohali–Panchkula and IXC airport, Ambala, Kalka, Pathankot, Jammu, Katra, Dehradun, Haridwar, Amritsar, and airports at Bhuntar (Kullu) and Gaggal (Kangra)."),
 ("Is Suzu Travels a registered company?", "Suzu Travels is a registered travel agent with HP Tourism (Reg. No. DTO-MND-11-243/2022) and GST registered. You can see both certificates on our certificates page."),
 ("What is the difference between Prime, Standard and Saver cabs?", "They are the same car class with a different fleet age. Prime cars are 2023 or newer (under 3 years old) and cost about 15% more than Standard; Standard cars are 3–5 years old and carry the fares shown on our route pages; Saver cars are 5–10 years old, well maintained, and about 8% cheaper. Every car is AC with a driver who knows the hills."),
 ("Do you have buses and Tempo Travellers for large groups?", "Yes. Besides 12- and 17-seater Tempo Travellers and the Force Urbania, we arrange 26-seater mini coaches and 35- and 45-seater AC coaches for weddings, corporate outings and yatras from Delhi, Chandigarh and Himachal. Coaches are quoted per trip on WhatsApp."),
 ("Can I see the road route before I book?", "Yes — use the route planner at the top of this page. Type any pickup and drop in North India and it draws the real road route on a map, plays the drive, and shows the distance, time and fares for every car."),
 ("Do you drive at night in the hills?", "For safety we plan hill sections in daylight. Leave early and we'll tell you the best start time for your route."),
]

TIER_COPY = {
    "prime": "Latest-generation cars with the newest safety kit and the quietest cabins - for guests who want the best car on the road.",
    "standard": "The cars we book most: serviced on schedule, clean, and the fares shown on every route page.",
    "saver": "Older but well-kept cars from our transporter network at a lower fare - the same driver standard, a few more kilometres on the clock.",
}

def planner():
    pv = [dict(id=v["id"], n=v["name"], ow=v["ow"], h=v["hire"], m=v["min"], nt=v["night"], seats=v["seats"], quote=bool(v.get("quote"))) for v in FLEET]
    pr = [dict(a=r["a"], b=r["b"], km=r["km"], f=r["f"], t=r["t"], u=(page_url(r["slug"]) if r["slug"] and is_live(r["slug"]) else "")) for r in ROUTES]
    pp = dict(PLACES, **PICKUPS)
    cfg = dict(p={k: [round(v[0], 3), round(v[1], 3)] for k, v in pp.items()}, r=pr, v=pv, s="cabs",
               js="https://cdn.jsdelivr.net/npm/maplibre-gl@5.24.0/dist/maplibre-gl.js", css="https://cdn.jsdelivr.net/npm/maplibre-gl@5.24.0/dist/maplibre-gl.css")
    vopts = "".join(f'<option value="{v["id"]}"{" selected" if v["id"]=="sedan" else ""}>{v["name"]} · {v["seats"]} seats</option>' for v in FLEET)
    # datalist HTML = route cities + pickup presets only (hub size budget); kit_hub.js appends the other PLACES on load
    ends = sorted(set([r["a"] for r in ROUTES] + [r["b"] for r in ROUTES]))
    dl = "".join(f"<option value=\"{esc(k)}\">" for k in ends + sorted(PICKUPS))
    return (f'<section class="szc-sec" id="planner"><span class="szc-kicker">Live route planner</span><h2>See your road trip on the map - with the fare</h2>'
            f'<p class="szc-lead">Type any two places in North India. We draw the real road route, play the drive, and show one-way or round-trip fares for every car and fleet tier.</p>'
            f'<form class="szc-plan" id="szc-plan" data-plan=\'{esc(json.dumps(cfg, ensure_ascii=False, separators=(",", ":")))}\' onsubmit="return false">'
            f'<div class="szc-pform"><div><label for="szc-fa">From</label><input id="szc-fa" type="text" list="szc-places" value="Delhi" placeholder="City, airport or station" autocomplete="off"></div>'
            f'<div><label for="szc-fb">To</label><input id="szc-fb" type="text" list="szc-places" value="Manali" placeholder="Anywhere in North India" autocomplete="off"></div>'
            f'<div><label for="szc-pv">Car</label><select id="szc-pv">{vopts}</select></div>'
            f'<div><label for="szc-pm">Trip</label><select id="szc-pm"><option value="one">One-way drop</option><option value="round">Round trip</option></select></div>'
            f'<div><label for="szc-pd">Date</label><input id="szc-pd" type="date"></div>'
            f'<div><label for="szc-pn">People</label><input id="szc-pn" type="number" min="1" max="45" value="2"></div>'
            f'<div class="szc-pgo"><button class="szc-btn gold" type="submit">Show route &amp; fare</button></div>'
            f'<div class="szc-pvia" id="szc-pvias"><div class="szc-pvlist" id="szc-pvlist"></div><button type="button" class="szc-padd" id="szc-padd">+ Add a stop on the way</button>'
            f'<span class="szc-phint">Himachal circuit? Add up to 3 stops (Kasol, Shimla, Dharamshala …) for total km, days and fare.</span>'
            f'<div class="szc-vdays"><label for="szc-pdy">Trip days</label><input id="szc-pdy" type="number" min="1" max="20" placeholder="auto"></div></div>'
            f'<p class="szc-pstat" id="szc-pstat"></p></div>'
            f'<div class="szc-mapwrap"><div class="szc-map" id="szc-map" aria-label="Road map of your route"></div><div class="szc-mapidle"><b>Your route appears here</b><span>Real roads, live distance and a drive-through animation - hills, tunnels and all.</span></div></div>'
            f'<div class="szc-pout" id="szc-pout"><div class="szc-pempty"><b>How it works:</b> pick From and To and press <b>Show route &amp; fare</b>. You get the distance, the driving time and the fare for Prime, Standard and Saver fleets - then lock the price on WhatsApp in one tap.</div></div>'
            f'</form><datalist id="szc-places">{dl}</datalist>'
            f'<p class="szc-note">Map data © OpenStreetMap contributors · road routing by OSRM · map tiles by OpenFreeMap. Distances and times are road estimates for planning; your WhatsApp quote is the final price.</p></section>')

def build():
    p = HUB
    chips = ["<b>20+</b> popular routes", "Sedan from <b>₹12/km</b>", f"<b>{len(FLEET)}</b> vehicle classes, hatchback → 45-seat coach", "Prime · Standard · Saver fleets", "Live route map", "24×7 WhatsApp"]
    finder = (f'<form class="szc-finder" id="szc-find">'
              f'<div><label for="szc-ha">From</label><input id="szc-ha" type="text" list="szc-places" value="Delhi" placeholder="City, airport or station" autocomplete="off"></div>'
              f'<div><label for="szc-hb">To</label><input id="szc-hb" type="text" list="szc-places" value="Manali" placeholder="Anywhere in North India" autocomplete="off"></div>'
              f'<div><label for="szc-hd">Travel date</label><input id="szc-hd" type="date"></div>'
              f'<button class="szc-btn gold" type="submit">Show route &amp; fare</button></form>')
    body = hero(p, chips) + finder
    body += nav([("planner", "Route map"), ("routes", "Routes"), ("fares", "Fares"), ("fleet", "Fleet"), ("local", "Local taxis"), ("pickup", "Pickup points"), ("why", "Why Suzu"), ("faq", "FAQ")])
    body += planner()
    # routes
    body += (f'<section class="szc-sec" id="routes"><span class="szc-kicker">Popular routes</span><h2>Taxi routes and one-way fares</h2>'
             f'<p class="szc-lead">Starting fares for a sedan and an Innova Crysta, one-way. Every route runs both directions at the same price.</p>{more_routes("cabs")}</section>')
    # fares
    rows = "".join(f'<tr><td><b>{v["name"]}</b><br><small>{v["model"]}</small></td><td>{v["seats"]}</td><td>{v["bags"]}</td><td class="num">{pkm(v["hire"])}</td><td class="num">{pinr(v["min"])}</td><td class="num">₹{v["night"]}</td></tr>' for v in PRICED)
    rows += "".join(f'<tr><td><b>{v["name"]}</b><br><small>{v["model"]}</small></td><td>{v["seats"]}</td><td>{v["bags"]}</td><td class="num">On quote</td><td class="num">On quote</td><td class="num">₹{v["night"]}</td></tr>' for v in FLEET if v.get("quote"))
    tiers_exp = "".join(f'<div class="szc-tip"><h3>{t["name"]} <small style="font-weight:600;color:#56675b">· {t["badge"].lower()}</small></h3><p>{t["sub"]}. {TIER_COPY[t["id"]]}</p></div>' for t in TIERS)
    tbl = (f'<div class="szc-tips" style="margin-top:10px">{tiers_exp}</div>{tier_switch()}'
           f'<div class="szc-scroll"><table class="szc-tbl"><thead><tr><th>Vehicle</th><th>Seats</th><th>Luggage</th><th>Round trip rate (<span data-tiername>Standard</span>)</th><th>Minimum one-way fare</th><th>Driver / night</th></tr></thead><tbody>{rows}</tbody></table></div>')
    dests = [dict(l=f'{r["a"]} → {r["b"]}', km=r["km"], f=r["f"]) for r in ROUTES]
    body += (f'<section class="szc-sec alt" id="fares"><span class="szc-kicker">Fare chart 2026</span><h2>Cab rates per km</h2>'
             f'<p class="szc-lead">Round trips and tours are billed per kilometre (minimum 250 km a day). One-way drops have fixed route fares — use the calculator.</p>{tbl}{includes()}'
             f'<h3 style="margin-top:34px">Fare calculator</h3>{calculator(dests, "cabs")}</section>')
    # fleet
    body += f'<section class="szc-sec" id="fleet"><span class="szc-kicker">Our fleet</span><h2>Pick the right car</h2><p class="szc-lead">Every car is AC, comes with a driver who knows hill roads, and is sized honestly for people and bags.</p>{vehicle_cards("cabs", "my trip", dict(l="Delhi → Shimla", km=345, f=1.0))}</section>'
    # local taxis
    local = [("manali-taxi-service", "Manali taxi service", "Solang, Atal Tunnel–Sissu, Rohtang at union rates; drops to Chandigarh, Delhi, Leh."),
             ("shimla-taxi-service", "Shimla taxi service", "Kufri, Chail, Naldehra, Narkanda day trips; Kalka & airport transfers."),
             ("chandigarh-taxi-service", "Chandigarh taxi service", "IXC airport & Tricity pickups; drops to Shimla, Kasauli, Manali, Amritsar, Delhi."),
             ("chandigarh-airport-taxi", "Chandigarh airport taxi", "IXC arrivals pickup with flight tracking; drops to Shimla, Kasauli, Manali, Dharamshala, Amritsar & Delhi."),
             ("dehradun-taxi-service", "Dehradun taxi service", "Jolly Grant airport pickups, Mussoorie & Dhanaulti day trips; drops to Rishikesh, Haridwar, Delhi."),
             ("srinagar-taxi-service", "Srinagar taxi service", "Airport pickups, Gulmarg, Pahalgam & Sonamarg day trips; drops to Jammu."),
             ("jammu-taxi-service", "Jammu taxi service", "Airport & Jammu Tawi pickups, Vaishno Devi drops at Katra, Patnitop & Shiv Khori; drops to Srinagar, Amritsar & Delhi."),
             ("haridwar-taxi-service", "Haridwar taxi service", "Station & ghat pickups, Rishikesh and Neelkanth trips; drops to Delhi, Sonprayag & Badrinath."),
             ("rishikesh-taxi-service", "Rishikesh taxi service", "Jolly Grant airport, station & rafting-camp pickups, Neelkanth trips; drops to Chopta, Sonprayag, Badrinath & Delhi."),
             ("outstation-cab-delhi", "Outstation cab from Delhi", "One-way drops and round trips from all of Delhi NCR to the hills, Haridwar, Amritsar, Agra and Jaipur."),
             ("amritsar-taxi-service", "Amritsar taxi service", "Airport & Golden Temple pickups, Wagah border trips; drops to Dharamshala, Dalhousie, Jammu, Katra & Delhi."),
             ("nainital-taxi-service", "Nainital taxi service", "Kathgodam & Pantnagar pickups, lake tour, Kainchi Dham; drops to Mukteshwar, Almora, Ranikhet, Corbett & Delhi."),
             ("tempo-traveller-hire-delhi", "Tempo Traveller hire in Delhi", "12–17 seats for hill trips, Char Dham and weddings."),
             ("tempo-traveller-chandigarh", "Tempo Traveller in Chandigarh", "12-seater, 17-seater & Urbania from the Tricity and IXC to Shimla, Manali, Dharamshala, Amritsar & Rishikesh."),
             ("innova-crysta-on-rent", "Innova Crysta on rent", "With driver, from ₹19/km for tours; one-way hill drops.")]
    lc = "".join(f'<article class="szc-card"><div class="szc-card-b"><span class="szc-tag">Service</span><h3>{t}</h3><p>{d}</p><div class="acts">'
                 + (f'<a class="szc-btn sm em" href="{page_url(s)}">Rates & details</a>' if is_live(s) else "")
                 + f'<a class="szc-btn sm wa" href="{wa("Hi Suzu Travels, I need " + t + ". Date: ___ , people: ___ (page: cabs)")}" target="_blank" rel="noopener">WhatsApp</a></div></div></article>' for s, t, d in local)
    lc += (f'<article class="szc-card"><div class="szc-card-b"><span class="szc-tag">Service</span><h3>Dharamshala & Kangra taxis</h3><p>McLeodganj, Bir, Palampur and Gaggal airport transfers.</p>'
           f'<div class="acts">' + (f'<a class="szc-btn sm em" href="{page_url("dharamshala-taxi-service")}">Rates & details</a>' if is_live("dharamshala-taxi-service") else "") + f'<a class="szc-btn sm wa" href="{wa("Hi Suzu Travels, I need a taxi in Dharamshala. Date: ___ (page: cabs)")}" target="_blank" rel="noopener">WhatsApp</a></div></div></article>'
           f'<article class="szc-card"><div class="szc-card-b"><span class="szc-tag">Service</span><h3>Char Dham yatra taxi</h3><p>From Delhi, Haridwar or Dehradun with drivers who know the yatra routes.</p>'
           f'<div class="acts">' + (f'<a class="szc-btn sm em" href="{page_url("char-dham-yatra-taxi")}">Rates & details</a>' if is_live("char-dham-yatra-taxi") else "") + f'<a class="szc-btn sm line" href="/packages/ultimate-char-dham-yatra/">Char Dham package</a><a class="szc-btn sm wa" href="{wa("Hi Suzu Travels, I need a Char Dham taxi. Dates: ___ , people: ___ (page: cabs)")}" target="_blank" rel="noopener">WhatsApp</a></div></div></article>')
    body += f'<section class="szc-sec alt" id="local"><span class="szc-kicker">Local & special taxis</span><h2>Local taxis and group vehicles</h2><div class="szc-grid">{lc}</div></section>'
    # pickup points
    pts = ["Delhi NCR · IGI Airport T1/T3", "New Delhi · Nizamuddin · Anand Vihar stations", "Gurugram · Noida · Ghaziabad", "Chandigarh · Mohali · Panchkula", "Chandigarh Airport (IXC)",
           "Ambala Cantt", "Kalka station", "Pathankot · Chakki Bank", "Jammu Tawi · Katra", "Dehradun · Jolly Grant", "Haridwar · Rishikesh", "Amritsar", "Bhuntar (Kullu) airport", "Gaggal (Kangra) airport", "Shimla · Manali · Dharamshala"]
    body += (f'<section class="szc-sec" id="pickup"><span class="szc-kicker">Where we pick up</span><h2>Airports, stations and cities we cover</h2>'
             f'<p class="szc-lead">Most hill trips start at one of these points. Tell us yours — if it is on the way, there is no extra charge.</p><ul class="szc-pts">' + "".join(f"<li>{x}</li>" for x in pts) + "</ul></section>")
    # why
    why = [("<b>Registered and accountable</b> — HP Tourism registered travel agent (DTO-MND-11-243/2022) and GST registered.",),
           ("<b>A Himachal team</b> — our office is on NH 103 in Bilaspur district; we plan hill drives every day.",),
           ("<b>One clear price</b> — the quote lists what's included and what's paid at actuals, before you pay.",),
           ("<b>Right car for the road</b> — we'll tell you honestly when a sedan is enough and when you need an Innova.",),
           ("<b>Daylight hill driving</b> — start times planned so hill sections are driven before dark.",),
           ("<b>Trip + stay in one chat</b> — add hotels, sightseeing or activities to the same booking if you want.",)]
    body += (f'<section class="szc-sec" id="why"><div class="szc-band"><span class="szc-kicker">Why book with Suzu</span><h2>A local travel company, not a call centre</h2>'
             f'<ul class="szc-checks">' + "".join(f"<li>{w[0]}</li>" for w in why) + '</ul>'
             f'<p style="margin:22px 0 0"><a class="szc-btn gold" href="/certificates/">See our certificates</a></p></div></section>')
    # tips
    from pages_content import HP_ENTRY, NIGHT, WINTER, MONSOON
    body += f'<section class="szc-sec alt" id="tips"><span class="szc-kicker">Road guide</span><h2>Driving to the hills: what to know</h2>{tips([HP_ENTRY, NIGHT, WINTER, MONSOON, ("Local union taxis", "In Manali and Kashmir, local sightseeing is done in locally registered taxis as per union practice. We book them for you at local rates."), ("Snow & permits", "Rohtang needs an online permit and is closed on Tuesdays; Atal Tunnel needs none. We handle permits with your booking.")])}</section>'
    body += f'<section class="szc-sec" id="booking"><span class="szc-kicker">How booking works</span><h2>Booked in four simple steps</h2>{steps()}</section>'
    body += quote_block(p, "", "")
    rel = [("/himachal-tour-packages/", "Himachal tour packages", "Hotel + cab"), ("/destination/kashmir-tour-packages/", "Kashmir tour packages", ""),
           ("/destination/chardham-tour-packages/", "Char Dham packages", ""), ("/adventure/", "Himachal adventure activities", ""),
           ("/himachal-entry-tax-permits-2026/", "Himachal entry tax & permits 2026", ""), ("/payment-booking/", "Payment & booking", "")]
    body += f'<section class="szc-sec" id="plan"><span class="szc-kicker">Plan the rest</span><h2>Hotels, packages and permits</h2>{related(rel)}</section>'
    body += faq_block(FAQS)
    return wrap(body, p, FAQS, ["Delhi", "Chandigarh", "Himachal Pradesh", "Punjab", "Uttarakhand", "Jammu and Kashmir"], js=HUB_JS)
