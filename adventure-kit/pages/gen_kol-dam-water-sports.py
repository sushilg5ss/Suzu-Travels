#!/usr/bin/env python3
"""kol-dam-water-sports — Page Builder (night) 12 Nov 2026.
Built from the Research Lead brief (11 Nov 2026) + Visual Studio night media @949ba11 (hero, explainer, reel).
Unverified list respected: no operating hours, no road distances to Aehan, no age/weight limits,
no monsoon ban date for Mandi/Bilaspur, no promise of entry to the dam (NTPC area).
All photos are generic (Pexels) with neutral alt text — never captioned as Kol Dam / Aehan / Tattapani.
No prices, no operator names. Quote-form links carry ?activity= (night override).
Run: python3 pages/gen_kol-dam-water-sports.py && python3 build.py pages/kol-dam-water-sports.html > pages/kol-dam-water-sports.min.html
"""
from urllib.parse import quote
import pathlib

SLUG = "kol-dam-water-sports"
U = "https://suzutravels.com/wp-content/uploads/"
CDN = ("https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@949ba113892bf0dd243971a8d8ecd2fd874353c2"
       f"/adventure-kit/media/{SLUG}/")


def wa(activity, place="Kol Dam"):
    t = (f"Hi Suzu Travels, I want a quote for {activity} in {place}. "
         f"Travel date: ___ , people: ___ (page: {SLUG})")
    return "https://wa.me/917087488961?text=" + quote(t, safe="")


WA = wa("water sports")
QF = "/himachal-tour-packages-quote/?activity=" + quote("Kol Dam water sports", safe="")
A = 'target="_blank" rel="noopener"'

cards = [
    ("Aehan launch point (Mandi)", "New 2026", "2026/10/jet-ski-on-hill-lake-at-sunset-768x512.webp",
     "Jet ski cutting a wake across a calm lake between forested hills", "50% 50%",
     "Opened 24 Oct 2026",
     "The new government water-sports base on the Kol Dam reservoir and the start of the ~35 km stretch to Tattapani.",
     wa("water sports", "Aehan, Kol Dam"), ""),
    ("Tattapani lake rides", "Shimla day trip", "2026/10/speed-boat-white-wake-lake-from-above-768x1227.webp",
     "Speed boat seen from above cutting a long white wake across dark blue water", "50% 50%",
     "About 55 km from Shimla",
     "Jet ski, speedboat, bumper and banana rides, plus e-foil and water skiing, on the lake that formed behind the dam.",
     wa("lake rides", "Tattapani"), ""),
    ("Mini cruise", "Family pick", "2026/11/passenger-cruise-boat-on-lake-768x512.webp",
     "Covered passenger boat with tourists cruising on a calm lake below hills", "50% 50%",
     "20-seat boat",
     "The calm option on the Aehan–Tattapani stretch — good for families and elders who don't want speed.",
     wa("the mini cruise"), ""),
    ("Banana &amp; bumper rides", "Group fun", "2026/11/banana-boat-ride-towed-by-speedboat-768x576.webp",
     "Speedboat towing a banana boat with riders in life jackets across open water, seen from above", "50% 50%",
     "Towed by a speedboat",
     "Ride together on an inflatable behind a boat — life jackets on for everyone, every round.",
     wa("banana and bumper rides"), ""),
    ("Hot springs + Satluj rafting", "Combo", "2026/10/steam-rising-over-hot-spring-pool.webp",
     "Steam rising over a hot spring pool edged with rocks", "50% 50%",
     "Tattapani in one day",
     "Lake rides in the morning, then the sulphur springs and river rafting below the dam.",
     wa("lake rides with rafting and hot springs", "Tattapani"),
     '<a class="x" href="/adventure/rafting-in-shimla-tattapani/">Tattapani rafting →</a>'),
    ("Kol Dam from the Bilaspur side", "Home turf", "2026/10/wide-calm-lake-hills-dusk-768x432.webp",
     "Wide, calm lake reflecting a pink and gold dusk sky, with a low line of hills", "50% 50%",
     "163 m dam, ~40 km lake",
     "See the lake from public roads and pair it with Gobind Sagar and Naina Devi. The dam itself is an NTPC area — entry is not open to visitors.",
     wa("Kol Dam with Gobind Sagar and Naina Devi", "Bilaspur"),
     '<a class="x" href="/adventure/gobind-sagar-water-sports/">Gobind Sagar →</a>'),
]

card_html = "".join(
    f'<article class="sza-card"><div class="img"><img src="{U}{img}" alt="{alt}" style="object-position:{pos}" loading="lazy"><span class="sza-badge">{badge}</span></div>'
    f'<div class="body"><h3>{name}</h3><div class="meta"><b>{meta}</b></div><p class="meta">{txt}</p>'
    f'<div class="go">{extra}<a class="q" href="{link}" {A}>Get Quote →</a></div></div></article>'
    for name, badge, img, alt, pos, meta, txt, link, extra in cards)

faqs = [
    ("Is Kol Dam open for tourists?",
     "Yes, the reservoir is. Water sports on the Aehan–Tattapani stretch were opened by the Chief Minister on 24 Oct 2026, and Tattapani's lake rides have run since the lake formed in 2015. Rides run subject to weather and the operator's schedule."),
    ("What water sports are there at Kol Dam?",
     "Speedboat, jet ski, banana boat, bumper ride and a 20-seat mini cruise. Tattapani also offers e-foil and water skiing."),
    ("Where is Kol Dam?",
     "On the Sutlej between Mandi and Bilaspur districts. The boating stretch runs about 35 km from Aehan in Mandi district to Tattapani."),
    ("How far is Tattapani from Shimla?",
     "About 55 km, so the lake rides work as a day trip from Shimla."),
    ("Who built Kol Dam and how big is it?",
     "NTPC. It produces 800 MW from four 200 MW units, with a 163 m rock-and-gravel fill dam and a reservoir about 40 km long."),
    ("Are life jackets compulsory?",
     "Yes. A May 2026 Bilaspur district order makes life jackets compulsory for everyone and allows only certified operators."),
    ("Can we combine Kol Dam with Gobind Sagar and Naina Devi?",
     f'Yes. Suzu is based in Bilaspur district; we plan Kol Dam, <a href="/adventure/gobind-sagar-water-sports/">Gobind Sagar Lake</a> and <a href="/pilgrimage-tours/naina-devi/">Naina Devi</a> as one 2-day trip with cab and hotel.'),
    ("What is the price of a Kol Dam boat ride?",
     f'It depends on the ride, your group and the day. <a href="{WA}" {A}>Send your date on WhatsApp</a> and we share today\'s rate within minutes.'),
]
faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)

reel = pathlib.Path(__file__).resolve().parents[1].joinpath("media", SLUG, "reel-section.html").read_text(encoding="utf-8").strip()

P = "sza-kol"
html = f'''<!-- {SLUG} — built by Page Builder (night) 12 Nov 2026 from the Research Lead brief + Visual Studio night media @949ba11. Kit v2.0. -->
<style>@media(max-width:900px){{.{P} .sza-hero video{{object-position:30% 50%}}.{P} .sza-hero:after{{background:linear-gradient(180deg,rgba(11,31,51,.5) 0%,rgba(11,31,51,.7) 45%,rgba(11,31,51,.95) 100%)}}}}.{P} .sza-hero-in>*{{max-width:640px}}@media(min-width:901px){{.{P} .sza-hero-in>*{{max-width:min(560px,44vw)}}}}.{P} .sza-chips{{max-width:720px}}.{P} #spots .sza-grid{{grid-template-columns:repeat(auto-fit,minmax(220px,1fr))}}@media(min-width:1000px){{.{P} #experience .sza-steps,.{P} #spots .sza-grid{{grid-template-columns:repeat(3,1fr)}}}}.{P} #spots .sza-card .img img{{aspect-ratio:3/2;object-fit:cover}}.{P} .sza-media ul{{padding-left:20px;list-style:disc;margin:0}}.{P} .sza-media ul li{{margin:0 0 8px}}.{P} .sza-checks{{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}.{P} .go .x{{margin-right:14px}}.{P} .sza-credit{{font-size:12px;color:#5b6b7a;margin:14px 0 0}}</style>
<div class="sza {P}">
<section class="sza-hero">
<video autoplay muted loop playsinline preload="metadata" poster="{U}2026/11/{SLUG}-hero-poster.webp" aria-label="A calm lake at dusk, a jet ski, a banana ride towed by a boat and a passenger boat, with a gold wake line from Aehan to Tattapani on the Kol Dam reservoir"><source src="{CDN}hero.webm" type="video/webm"><source src="{CDN}hero.mp4" type="video/mp4"></video>
<div class="sza-hero-in">
<span class="sza-kicker">Water · Mandi–Bilaspur · our home stretch of the Sutlej</span>
<p class="sza-hero-tag">Jet skis and a mini cruise on Himachal's newest lake</p>
<p class="sza-hero-sub">The 800 MW Kol Dam turned the Sutlej into a 40 km lake. Boats now run from Aehan to Tattapani — we add the ride to your cab, hotel and Shimla or Bilaspur trip.</p>
<ul class="sza-chips"><li><b>Reservoir</b> ~40 km</li><li><b>Stretch</b> Aehan–Tattapani ~35 km</li><li><b>Opened</b> 24 Oct 2026</li><li><b>Life jacket</b> Compulsory</li><li><b>Tattapani</b> 55 km from Shimla</li><li><b>Price</b> Get Quote</li></ul>
<div class="sza-btns"><a class="sza-btn gold" href="{WA}" {A}>Get Quote on WhatsApp</a><a class="sza-btn ghost" href="{QF}">Add to my Himachal trip</a></div>
<div class="sza-trust"><span><a href="https://suzutravels.com/certificates/">HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022</a></span><span>Ride + cab + hotel in one quote</span><span>Reply within minutes</span></div>
</div>
</section>
<nav class="sza-nav" aria-label="On this page"><div class="sza-nav-in"><a href="#overview">Overview</a><a href="#spots">Rides &amp; spots</a><a href="#experience">Your day</a><a href="#season">Season</a><a href="#safety">Safety</a><a href="#booking">How booking works</a><a href="#packages">Packages</a><a href="#faq">FAQ</a><a class="cta" href="{WA}" {A}>Get Quote</a></div></nav>

<section class="sza-sec" id="overview">
<span class="sza-kicker">Quick answer</span>
<h2>Kol Dam water sports at a glance</h2>
<p class="sza-answer">Kol Dam is NTPC's 800 MW dam on the Sutlej between Mandi and Bilaspur districts. Its 163 m rock-and-gravel dam created a reservoir about 40 km long. Since 24 Oct 2026, speedboats, jet skis, banana and bumper rides and a 20-seat mini cruise run along the Aehan–Tattapani stretch. Tattapani's lake rides started after the reservoir filled in 2015.</p>
<div class="sza-facts"><div class="sza-fact"><div class="k">Dam</div><div class="v">NTPC, 800 MW (4 × 200 MW), 163 m rock-and-gravel fill dam on the Sutlej</div></div><div class="sza-fact"><div class="k">Reservoir</div><div class="v">About 40 km, touching Mandi, Bilaspur, Solan and Shimla districts</div></div><div class="sza-fact"><div class="k">Water sports</div><div class="v">Aehan (Mandi) launch point, ~35 km stretch to Tattapani; opened 24 Oct 2026</div></div><div class="sza-fact"><div class="k">Rides</div><div class="v">Speedboat, jet ski, banana, bumper, 20-seat mini cruise; e-foil and water ski at Tattapani</div></div><div class="sza-fact"><div class="k">Safety</div><div class="v">Life jacket for every person; certified operators only (Bilaspur DDMA order, May 2026)</div></div><div class="sza-fact"><div class="k">Price</div><div class="v">Get Quote</div></div></div>
</section>

<section class="sza-sec alt" id="spots">
<span class="sza-kicker">Rides &amp; spots</span>
<h2>Where and what to ride on the Kol Dam lake</h2>
<p class="sza-lead">Two jetties, five kinds of ride and Tattapani's springs and rapids next door. Tell us your start city and we pick the jetty that runs on your date.</p>
<div class="sza-grid">{card_html}</div>
<p class="sza-credit">Photos are illustrative (Pexels licence) — not taken at Kol Dam.</p>
</section>

<section class="sza-sec" id="experience">
<span class="sza-kicker">Your day</span>
<h2>How a Kol Dam day works</h2>
<ol class="sza-steps"><li><h3>Share your plan</h3><p>Date, group size and where you start — Shimla, Bilaspur, Mandi or Chandigarh — on WhatsApp.</p></li><li><h3>We check the jetty</h3><p>Which jetty runs that day (Aehan or Tattapani) and today's rate; one quote with cab + hotel.</p></li><li><h3>Briefing first</h3><p>Drive to the jetty; safety briefing and life jackets before every ride.</p></li><li><h3>Ride</h3><p>Speedboat, jet ski, banana or bumper ride, or the mini cruise.</p></li><li><h3>Lunch by the lake</h3><p>Then Tattapani hot springs or rafting if you have time.</p></li><li><h3>Back or stay</h3><p>Drive back to Shimla or Bilaspur, or stay the night near Tattapani or Bilaspur.</p></li></ol>
<div class="sza-media"><video autoplay muted loop playsinline preload="none" poster="{U}2026/11/{SLUG}-explainer-poster.webp" width="1600" height="900" aria-label="How the Kol Dam lake works (schematic, not to scale): the Sutlej, the 800 MW dam, a reservoir about 40 km long, and the ~35 km Aehan–Tattapani boating stretch opened 24 Oct 2026; rides: jet ski, speedboat, banana, bumper, mini cruise; life jacket for everyone; price: Get Quote"><source src="{CDN}explainer.webm" type="video/webm"><source src="{CDN}explainer.mp4" type="video/mp4"></video><div><h3>How the Kol Dam lake works</h3><ul><li><b>Dam</b> → NTPC, 800 MW, 163 m high, on the Sutlej.</li><li><b>Lake</b> → about 40 km long, across four districts.</li><li><b>Boating</b> → ~35 km from Aehan to Tattapani.</li><li><b>Rides</b> → jet ski, speedboat, banana, bumper, 20-seat mini cruise.</li></ul><p style="margin-top:8px;font-size:14px">Rides run subject to weather and the operator's schedule — we confirm on your date.</p></div></div>
</section>

<section class="sza-sec alt" id="season">
<span class="sza-kicker">When to go</span>
<h2>Best time for Kol Dam water sports</h2>
<div class="sza-scroll"><table class="sza-tbl"><thead><tr><th>Months</th><th>Lake conditions</th><th>Our advice</th></tr></thead><tbody><tr><td>Mar – Jun</td><td>Warm, calm mornings; the busiest months</td><td>Best window — go early in the day</td></tr><tr><td>Jul – Sep</td><td>Monsoon inflow and rain; the district can suspend rides</td><td>Check before you book — we confirm on your date</td></tr><tr><td>Oct – Nov</td><td>Clear skies, pleasant days; Aehan opened late Oct 2026</td><td>Very good</td></tr><tr><td>Dec – Feb</td><td>Cool but no snow at lake level; shorter days</td><td>Fine for the mini cruise and boat rides; dress warm for the jet ski</td></tr></tbody></table></div>
</section>

<div class="sza-band" id="safety"><div class="sza-band-in">
<span class="sza-kicker">Safety &amp; district rules</span>
<h2>What we check before your ride</h2>
<p class="sza-lead">Suzu Travels is an HP Tourism registered travel agent (Reg. No. DTO-MND-11-243/2022). We arrange rides with registered local operators and plan around these checks:</p>
<ul class="sza-checks"><li><b>Life jacket for everyone</b>Every person, every ride — compulsory under the Bilaspur DDMA order (May 2026, Disaster Management Act 2005)</li><li><b>Certified operators only</b>Trained, certified pilots and boat operators; boats carry life buoys, ropes and first aid, with passenger capacity displayed</li><li><b>Briefing first</b>A safety briefing before every trip; high-risk zones are closed to all activity</li><li><b>Weather call</b>Rides stop in bad weather or high inflow — we re-plan the day, no pressure to ride</li><li><b>Kids and elders</b>We suggest the mini cruise or a speedboat; the operator decides age and weight limits on the day</li><li><b>Dam area</b>The dam is an NTPC area — enjoy the lake from the jetties and public roads</li></ul>
</div></div>

<section class="sza-sec" id="booking">
<span class="sza-kicker">How booking works</span>
<h2>Get a quote in minutes</h2>
<ol class="sza-steps"><li><h3>Tell us</h3><p>WhatsApp or the quote form — dates, people and start city.</p></li><li><h3>We check your date</h3><p>Which jetty runs, the weather and today's rate.</p></li><li><h3>You get one quote</h3><p>Ride, cab and hotel together, with any add-ons.</p></li><li><h3>Confirm and go</h3><p>We send the plan and stay in touch on WhatsApp.</p></li></ol>
<p class="sza-lead">Your quote depends on which ride (jet ski, speedboat, banana or bumper ride, mini cruise) and how many rounds, your group size and weekday vs weekend, which jetty runs that day and your start city, add-ons such as Tattapani rafting, the hot springs, Naina Devi or Gobind Sagar, and the cab type and hotel nights (Shimla, Bilaspur or Tattapani). We confirm today's rate on WhatsApp within minutes.</p>
</section>

{reel}

<section class="sza-quote"><div><span class="sza-kicker">Kol Dam lake rides</span><h2>Get your Kol Dam quote</h2><p>Tell us your date, group size and start city. We reply with today's rate — ride, cab and hotel included.</p></div><div class="sza-btns"><a class="sza-btn gold" href="{WA}" {A}>Get Quote on WhatsApp</a><a class="sza-btn ghost" href="{QF}">Plan full trip</a></div></section>

<section class="sza-sec" id="packages">
<span class="sza-kicker">Make it a trip</span>
<h2>Pair Kol Dam with Shimla or Bilaspur</h2>
<p><b>Shimla + Tattapani day:</b> lake rides, the hot springs and <a href="/adventure/rafting-in-shimla-tattapani/">rafting and lake rides at Tattapani</a> in one day. Coming from the plains? Book the <a href="/cabs/chandigarh-to-shimla-taxi/">Chandigarh to Shimla taxi</a> and read about the <a href="/adventure/hot-springs-in-himachal/">hot springs in Himachal</a>.</p>
<p><b>Bilaspur 2-day (our home district):</b> Kol Dam, <a href="/adventure/gobind-sagar-water-sports/">Gobind Sagar water sports</a>, <a href="/pilgrimage-tours/naina-devi/">Naina Devi</a> and <a href="/adventure/paragliding-in-bilaspur/">paragliding at Bandla</a>. On the Mandi side, add the <a href="/adventure/kamrunag-trek/">Kamrunag trek</a>. Check <a href="/bilaspur-weather/">Bilaspur weather</a>, <a href="/mandi-weather/">Mandi weather</a> or <a href="/karsog-weather/">Karsog weather</a>, or <a href="{QF}">ask for a custom plan</a>.</p>
</section>

<section class="sza-sec sza-faq" id="faq">
<span class="sza-kicker">FAQ</span>
<h2>Kol Dam water sports — questions</h2>
{faq_html}
</section>

<section class="sza-sec alt" id="more">
<span class="sza-kicker">More adventures</span>
<h2>Explore more in Himachal</h2>
<div class="sza-cats"><a class="sza-cat" href="/adventure/gobind-sagar-water-sports/"><span class="ic">🚤</span><span class="n">Gobind Sagar water sports</span><span class="c">Bilaspur</span></a><a class="sza-cat" href="/adventure/rafting-in-shimla-tattapani/"><span class="ic">🛶</span><span class="n">Rafting at Tattapani</span><span class="c">Shimla</span></a><a class="sza-cat" href="/adventure/paragliding-in-bilaspur/"><span class="ic">🪂</span><span class="n">Paragliding in Bilaspur</span><span class="c">Bandla</span></a><a class="sza-cat" href="/adventure/pong-dam-bird-watching-water-sports/"><span class="ic">🦆</span><span class="n">Pong Dam</span><span class="c">Kangra</span></a><a class="sza-cat" href="/adventure/hot-springs-in-himachal/"><span class="ic">♨️</span><span class="n">Hot springs</span><span class="c">Tattapani · Manikaran</span></a><a class="sza-cat" href="/adventure/"><span class="ic">🧭</span><span class="n">All adventures</span><span class="c">Air · Water · Snow · Land</span></a></div>
</section>
</div>'''

pathlib.Path(__file__).with_name(f"{SLUG}.html").write_text(html, encoding="utf-8")
print("ok", len(html))
