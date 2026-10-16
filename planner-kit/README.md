# Suzu Trip Planner — "Plan Your Trip" booking engine (planner-kit)

Owner: Sushil Kumar, Suzu Travels (suzutravels.com). Started 15 Oct 2026 with Claude.
Branch `planner` of `sushilg5ss/Suzu-Travels`, folder `planner-kit/`. This README is the spec; `agents/developer.md` is the daily agent's standing instructions.

## 1. Why (Sushil's idea, 15 Oct 2026)
After looking at MakeMyTrip, Sushil found the big hero video on the homepage "only for view" — it gives the visitor nothing to do. He wants a real booking engine instead:
- Guests **and travel agents** pick places (tours, cities, cabs, hotels, pilgrim / Mata tours) and **create and customise their own itinerary** — "Plan your trip / Create your itinerary".
- They **see it visually** while building: road map with the car route, day-by-day plan (HyperFrames-style motion).
- **Estimated prices**, kept on the **higher side of market** — real price, availability and discounts come from the Suzu team.
- **Download / share** the itinerary through a link. **Suzu does not store itineraries** — the plan lives inside the link.
- **Lead capture**: name + WhatsApp number before download / share / best price. The customer gets a custom itinerary, Suzu gets the lead, the team confirms dates and offers discounts.
- Not a one-day job: a dedicated developer agent improves it every day.

## 2. What exists (v0.1, 15 Oct 2026)
Two static files (since v0.5, 16 Oct 2026): `dist/plan-your-trip/index.html` (≈240 KB raw, ≈81 KB gzip; CSS + JS + places/rates/templates/km-matrix inline) and `dist/plan-your-trip/roads-geo.json` (≈460 KB road geometry, fetched after first paint — deploy BOTH together), to live at **https://suzutravels.com/plan-your-trip/** as `public_html/plan-your-trip/index.html` (static file → LiteSpeed serves it without PHP; WordPress has no page on that slug — 404 checked 15 Oct).

Booking-engine tabs (MakeMyTrip-style card on a light mountain hero):
1. **Holiday planner** — Starting from · Going to (search over places + ready ideas) · Start date · Travellers → *Plan my trip*.
2. **Yatra & Mata darshan** — ready pilgrim circuits (Himachal Shakti Peeth / Nau Devi, Vaishno Devi, Char Dham, Do Dham, Golden Temple…).
3. **Cabs** — from/to/one-way or round trip/car → instant fare estimate → book (lead) / WhatsApp.
4. **Hotels** — destination/check-in/nights/rooms/class → estimate → "Get hotel options" (lead) / "Make it a trip".

Workspace after *Plan my trip* (3 columns desktop, stacked + sticky price bar on phones):
- **Builder**: pickup/drop, ordered stops with nights (0 N = visit on the way, e.g. Jwala Ji darshan), ↑ move, × remove, add place (search) + "Near <last stop>" suggestions with km, *Best order* (nearest-neighbour + 2-opt), dates, adults/children/infants/rooms, hotel class (Standard/Deluxe/Super Deluxe/Luxury), meals (MAP/CP), car (auto by group size; SUV forced for Spiti/Lahaul/Ladakh/Chitkul), add-ons (price on request), **Travel agent box** (agency name/phone/email/markup %).
- **Route map**: animated SVG sketch built from real road geometry (OSRM/OpenStreetMap), numbered pins, "▶ Play my trip" drives a car along each day's road and highlights the day; "Real map" lazy-loads Leaflet 1.9.4 (cdnjs) + CARTO Voyager tiles.
- **Day-by-day plan**: km + realistic hill drive time (OSRM × 1.3 in hills), night stay, sights scheduled per day, "also possible", long-drive and season warnings (Chandratal/Kunzum/Manali–Leh Jun–Oct, Char Dham May–Oct).
- **Price card**: per adult + range + total, breakdown (private car incl. driver/tolls/parking, hotels, service & GST 5%), CTAs: *Get best price & availability* (lead), *Download itinerary (PDF)* (lead → print-to-PDF document), *Share link* (lead → link + WhatsApp/copy/native share), *Chat on WhatsApp*.
- **Agent mode**: price card shows Suzu B2B estimate and client price (+markup); PDF is branded with the agency (footer "Ground arrangements by Suzu Travels (DMC)"); *Client link* opens in client view: agency branding + client price only, no net, no mode switch, "Book with <agency>" WhatsApp button.

Leads (only when the page runs on suzutravels.com): POST `/wp-admin/admin-ajax.php`, `action=suzu_submit_landing_form`, fields `name, contact, email, destination, travel_date, message`; `destination` starts `TRIP PLANNER 🗺️ ` (`B2B AGENT 🧳 TRIP PLANNER 🗺️ ` in agent mode); message = full day plan + estimate + share link. Fires Google Ads lead `AW-17212172485/SPBwCPbf_9saEMXRs49A` and GA4 `generate_lead`. Honeypot field `website`. Same session never asked twice (sessionStorage `suzuTpLead`).

Share link: `#t=<base64url(JSON)>` — `{v:1,s,e,d,a,c,i,r,t,m,k,p:[[id,nights]],x,tp,g?,cv?}`. Nothing stored server-side. **Keep v:1 links working forever** (people save them); add `v:2` decoding if the format changes.

## 3. Pricing engine (data/rates.json) — "higher side" by design
- **Car**: per-km rates and driver allowance identical to the live /cabs/ fare engine (`cab-kit/cabs_data.py` on branch `cabs`): sedan 12, Ertiga 14, Innova Crysta 19, Tempo 26, Urbania 36 ₹/km; ₹400/night (₹500 Tempo/Urbania). Billable km = max(actual drive + sightseeing km, 250 km × days; 150 km/day on Kashmir/Ladakh union days). Kashmir ×1.25 / Ladakh ×1.35 local-union factor. Tolls + parking ₹1.5/km.
- **Hotels**: per room-night, double, MAP, off-peak, by place class: metro 3,200 · Rajasthan city/heritage 3,600 · popular hill 3,800 · hill town 3,200 · remote/camps 3,600 · pilgrim town 2,400 · pilgrim city (Katra/Haridwar) 4,000 · Kashmir 4,400 · Ladakh 3,900 (rate audit 16 Oct 2026, `research/rates-sources.md`). Tier ×0.7 / 1.0 / 1.45 / 2.6 (remote capped ×1.8). Extra adult 35 %, child bed 25 %, CP ×0.88. **Peak ×1.25** on Suzu's own windows: 15 Mar–30 Jun, all October, 20 Dec–5 Jan.
- **Service** 10 % + **GST 5 %**; display range = total → total × 1.12; per adult = total ÷ (adults + ½ children).
- Calibration 16 Oct 2026 (after rate audit): same trip → ₹23,300/adult; Vaishno Devi template ₹9,300; Kashmir classic ₹22,300.
- Calibration 15 Oct 2026: Shimla–Manali 5N from Chandigarh, 2 adults, deluxe, Nov → ₹22,200/adult (sedan ₹21.3k + hotels ₹17k). The homepage "from ₹12,499" is a 4–6 person off-season rate; the planner estimate drops toward it as the group grows. **Never show a figure lower than the market; never call an estimate a quote.**
- Activities are never priced (Suzu rule: "Get Quote" / "price on request").

## 4. Data
- `data/places.py` — 87 places (hubs, Himachal, Mata temples, Kashmir, Ladakh, Uttarakhand/Kumaon, Rajasthan, Agra–Mathura, Punjab) with Hindi names, class, open months, sights (name, extra km, note), tips.
- `data/roads.json` — OSRM road km + minutes for every pair, plus simplified road geometry (Google polyline) for 531 legs; missing pairs are drawn by chaining stored legs (Dijkstra) in the browser. Rebuild: `EXTRA_LEGS="a-b,..." python3 tools/fetch_roads.py` (OSRM demo server, polite; cache `data/.osrm_cache.json` is git-ignored).
- `data/templates.json` — 31 ready ideas (cat himachal / mata / pilgrim / honeymoon / kashmir / ladakh / uttarakhand / rajasthan) with links to the live package pages.

## 5. Build · test · deploy
```
python3 build.py                                   # -> dist/plan-your-trip/index.html (+ size, sha256)
(cd dist && python3 -m http.server 8765 &)
npm i playwright@1.49.1 --no-save
node tools/test_planner.js http://localhost:8765/plan-your-trip/ /tmp/tp   # desktop 1440 + Pixel 7, JSON report + screenshots
```
The test stubs `sendBeacon`, admin-ajax and `print` — it never sends a real lead. Pass = 0 page errors (the local favicon 404 is fine), no horizontal overflow, share link round-trips, PDF + lead fire, prices sane.
Deploy = Hostinger File Browser API from Sushil's Chrome (see `agents/developer.md` §Deploy). Rolling backup: `public_html/plan-your-trip/index-previous.html`.

## 6. Hard business rules
- Phone/WhatsApp **+91 70874 88961** only; info@suzutravels.com; "HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022" (never "registered DMC").
- Booking terms exactly: small token advance locks the rate; balance before the trip; advance non-refundable; one date change within 6 months; Razorpay / bank / UPI.
- No invented ratings, reviews, "seats left", fake discounts or strike-through prices. Estimates are labelled estimates.
- Never name partner companies, vendors or transporters. No social posting.
- Light nature theme (never dark), `--nz-*` colours, Plus Jakarta Sans + Tiro Devanagari Hindi, transform/opacity animation only, `prefers-reduced-motion` respected, tap targets ≥ 44 px.

## 7. Roadmap — see BACKLOG.md
