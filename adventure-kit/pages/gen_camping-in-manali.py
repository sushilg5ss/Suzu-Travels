#!/usr/bin/env python3
# Generates adventure-kit/pages/camping-in-manali.html (Page Builder night, 25 Oct 2026 IST)
import urllib.parse, pathlib
SLUG = "camping-in-manali"
HERE = pathlib.Path(__file__).resolve().parent
CDN = "https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@e3f42f977ef7cd563c71c8caf9feded5a5cbc537/adventure-kit/media/camping-in-manali/"
UP = "https://suzutravels.com/wp-content/uploads/2026/10/"
QUOTE = "/himachal-tour-packages-quote/?activity=" + urllib.parse.quote("Camping in Manali")
WHAT = "camping in Manali"

def wa(what=WHAT, tag=SLUG):
    t = f"Hi Suzu Travels, I want a quote for {what}. Travel date: ___ , people: ___ (page: {tag})"
    return "https://wa.me/917087488961?text=" + urllib.parse.quote(t, safe="")

def walink(label, what=WHAT, cls="sza-btn gold"):
    return f'<a class="{cls}" href="{wa(what)}" target="_blank" rel="noopener">{label}</a>'

MAIN = wa()

def card(src, w, h, alt, badge, title, meta, text, what, page=None):
    explore = f'<a class="x" href="{page}">Explore →</a>' if page else ""
    return (f'<article class="sza-card"><div class="img"><img src="{src}" alt="{alt}" loading="lazy" width="{w}" height="{h}"><span class="sza-badge">{badge}</span></div>'
            f'<div class="body"><h3>{title}</h3><div class="meta">{meta}</div><p class="meta">{text}</p>'
            f'<div class="go"><a class="q" href="{wa(what)}" target="_blank" rel="noopener">Get Quote →</a>{explore}</div></div></article>')

cards = "".join([
    card(f"{UP}dome-tents-hilltop-meadow-sunrise-768x498.webp", 768, 498,
         "Dome tents on a grassy hilltop meadow at sunrise with layered blue mountain ridges behind",
         "Meadow camps", "Solang Valley", "<b>~13 km from Manali · Mar–Jun, mid-Sep–Nov</b>",
         "Meadow camps near the Solang ropeway, paragliding slopes and the snow point — the busiest camping area around Manali.",
         "camping in Solang Valley, Manali", "/adventure/solang-valley-activities/"),
    card(f"{UP}lit-tents-snow-mountain-night-768x512.webp", 768, 512,
         "Two lit tents pitched on deep snow below a snow-covered mountain with pine trees, at night",
         "Snow side", "Kothi–Gulaba road", "<b>Pine and gorge camps on the Rohtang road</b>",
         "Quieter than town, higher up the valley — this side gets the first snow of the season.",
         "camping on the Kothi–Gulaba road, Manali"),
    card(f"{UP}tent-door-view-mountain-river-pine-forest-768x1186.webp", 768, 1186,
         "View from an open tent door over a fast mountain river and pine-covered slopes",
         "By the Beas", "Naggar road / left bank", "<b>Riverside &amp; orchard camps</b>",
         "Camps between Manali and Naggar, set back from the river; pair a camp night with rafting near Pirdi (not 15 Jul–15 Sep).",
         "riverside camping on the Naggar road, Manali", "/adventure/river-rafting-in-kullu-manali/"),
    card(f"{UP}lit-tents-meadow-campsite-dusk-768x512.webp", 768, 512,
         "Lit dome tents on a grassy campsite at dusk below a dark hill",
         "Orchard night", "Sethan &amp; orchard camps", "<b>Above town, among apple orchards</b>",
         "Camps in the orchards above Manali; in winter the Sethan side is where the igloo stays are.",
         "an orchard camp near Sethan, Manali", "/adventure/igloo-stay-manali/"),
    card(f"{UP}trek-tents-meadow-stream-valley-768x1024.webp", 768, 1024,
         "Row of orange trek tents on a green meadow beside a stream in a steep mountain valley",
         "On the trail", "Trek camps (Hampta side)", "<b>Tents each night of the trek</b>",
         "Trek tents on the Hampta Pass route and other trails, run by the trek operator with forest permission.",
         "a trek camp on the Hampta Pass route", "/adventure/hampta-pass-trek/"),
    card(f"{UP}camping-tents-starry-night-sky-768x702.webp", 768, 702,
         "Row of small camping tents below a forested hill under a starry night sky",
         "Dec–Feb", "Winter instead?", "<b>Heated tent, igloo or a warm room</b>",
         "When tents are too cold, sleep in a heated tent where a camp stays open, an igloo stay, or a warm room plus a Solang snow day.",
         "a winter camp or igloo stay in Manali", "/adventure/snow-activities-manali/"),
])

steps_exp = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Tell us your plan", "Dates, group (kids? seniors?) and the night you want — meadow, river, orchard or snow."),
    ("We check your week", "Which areas are open that week: weather, snow, river level and current orders."),
    ("We book a registered camp", "With a registered local operator, then add your hotel nights and cab."),
    ("Arrive by afternoon", "Check-in, tea, a short walk or an activity — rafting, paragliding or a Solang outing."),
    ("Evening at camp", "Bonfire where the camp is allowed one, dinner, sleeping bag or heater for the season."),
    ("Morning and onward", "Breakfast, check-out and the cab on to Solang, the Atal Tunnel or your next stop."),
])

booking = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Tell us", "WhatsApp or the quote form — dates, group size, the area you like and where you start from."),
    ("We check your date", "Season, snow, river level and a registered camp for that night."),
    ("You get one quote", "Camp night, hotel nights, cab and any activity in one plan."),
    ("Confirm and go", "We send the camp location, check-in time and what to pack."),
])

season = [
    ("Mar–Jun", "Open — best", "Pleasant days, cool nights; May–Jun is busiest, book early"),
    ("Jul–mid-Sep", "Limited", "Monsoon: stay off riverbanks, landslide risk; rafting and paragliding closed 15 Jul–15 Sep"),
    ("mid-Sep–Nov", "Open — best", "Clear skies; cold nights from November"),
    ("Dec–Feb", "Mostly closed", "Snow; heated tents or an igloo stay only; beyond Solang the road can be 4x4-only after snowfall"),
]
season_html = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in season)

faqs = [
    ("Where can I camp in Manali?", "The main areas are Solang Valley, the Kothi–Gulaba road towards Rohtang, the Naggar road along the Beas, the orchard camps above town around Sethan, and trek camps on the <a href=\"/adventure/hampta-pass-trek/\">Hampta Pass</a> side."),
    ("What is the best time for camping in Manali?", "March to June and mid-September to November. Winter nights go below zero and many camps close."),
    ("Can I camp in Manali in winter?", "Only in heated tents or an <a href=\"/adventure/igloo-stay-manali/\">igloo stay</a>, and only where a camp stays open after snow. Most families take a heated room plus a <a href=\"/adventure/snow-activities-manali/\">Solang snow day</a> instead."),
    ("Is riverside camping in Manali safe?", "Outside the monsoon, at a registered camp set back from the river, yes. Kullu banned camps close to riverbeds after the July 2022 flash floods, so we never book a tent on the riverbed."),
    ("Is camping in Solang Valley allowed?", "Yes, at registered camps near the valley. Beyond Solang, police may allow only 4x4 vehicles after snowfall."),
    ("Do I need a permit to camp near Manali?", "Not at a registered camp. Camping in forest areas or on trek routes needs Forest Department permission, which the trek operator arranges."),
    ("Can we combine camping with rafting or paragliding?", "Yes — <a href=\"/adventure/river-rafting-in-kullu-manali/\">rafting</a> near Pirdi or <a href=\"/adventure/paragliding-in-manali/\">paragliding</a> at Solang or Dobhi, except from 15 July to 15 September, when both are closed."),
    ("How much does camping in Manali cost?", "Get Quote — the rate depends on the area, tent type, meals, month and transport. Send your dates on WhatsApp and we reply with today's rate within minutes."),
]
faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)

more = [
    ("/adventure/camping-in-himachal/", "⛺", "Camping in Himachal", "Six camping areas"),
    ("/adventure/camping-in-kasol/", "🏕️", "Camping in Kasol", "Riverside camps, Parvati valley"),
    ("/adventure/adventure-activities-in-manali/", "🏔️", "Manali adventures", "What runs in your month"),
    ("/adventure/paragliding-in-manali/", "🪂", "Paragliding in Manali", "Solang and Dobhi flights"),
    ("/adventure/atal-tunnel-sissu-snow-trip/", "❄️", "Atal Tunnel &amp; Sissu", "Snow day from Manali"),
    ("/adventure/bike-rent-in-manali/", "🏍️", "Bike rent in Manali", "Ride to your camp"),
]
more_html = "".join(f'<a class="sza-cat" href="{h}"><span class="ic">{i}</span><span class="n">{n}</span><span class="c">{c}</span></a>' for h, i, n, c in more)

reel = (HERE.parent / "media" / SLUG / "reel-section.html").read_text(encoding="utf-8").strip()
reel = reel.replace('href="/adventure/camping-in-himachal/"', 'href="/adventure/camping-in-himachal/"')

page = f'''<!-- camping-in-manali — built by Page Builder (night) 25 Oct 2026 IST from the Research Lead brief 24 Oct + Visual Studio media @e3f42f9. Kit v1.8. No prices, no operator or camp names. Unverified items left off: "25 m from streams", whether the 2022 riverbed order is re-issued yearly, exact km for Kothi/Gulaba/Sethan, which camps stay open in winter, forest fees. Generic photos carry neutral alt text. -->
<style>.sza-cim .sza-hero-in>*{{max-width:620px}}.sza-cim .sza-chips{{max-width:700px}}.sza-cim .sza-media ul{{padding-left:20px;list-style:disc;margin:0}}.sza-cim .sza-media ul li{{margin:0 0 8px}}.sza-cim .sza-media img{{height:auto;aspect-ratio:4/3;object-fit:cover}}.sza-cim .sza-media video{{height:auto;aspect-ratio:16/9}}.sza-cim #spots .sza-grid{{grid-template-columns:repeat(auto-fit,minmax(min(340px,100%),1fr))}}.sza-cim #spots .sza-card .img img{{aspect-ratio:3/2;object-fit:cover}}.sza-cim .sza-checks{{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}.sza-cim .sza-choose{{margin-top:32px}}@media(max-width:820px){{.sza-cim .sza-hero video{{object-position:30% 50%}}.sza-cim .sza-hero:after{{background:linear-gradient(180deg,rgba(11,31,51,.35) 0%,rgba(11,31,51,.6) 40%,rgba(11,31,51,.94) 100%)}}}}</style>
<div class="sza sza-cim">
<section class="sza-hero">
<video autoplay muted loop playsinline preload="metadata" poster="{UP}camping-in-manali-hero-poster.webp" aria-label="Tents under a starry sky, a tent-door view over a river, dome tents on a meadow and lit tents on snow, with a schematic of five camping areas around Manali: Solang, Kothi–Gulaba, Sethan, Hampta and the Naggar road; best March to June and mid-September to November, registered camps only"><source src="{CDN}hero.webm" type="video/webm"><source src="{CDN}hero.mp4" type="video/mp4"></video>
<div class="sza-hero-in">
<span class="sza-kicker">Treks &amp; Camps · Manali</span>
<p class="sza-hero-tag">Pick your Manali camp night — meadow, river or orchard</p>
<p class="sza-hero-sub">Five camping areas, what is open in your month and the rules that matter — we add the camp to your hotel + cab plan.</p>
<ul class="sza-chips"><li><b>5</b> camp areas</li><li><b>Registered</b> camps only</li><li><b>Best</b> Mar–Jun, mid-Sep–Nov</li><li><b>Winter</b> heated tent / igloo</li><li><b>Monsoon</b> off the riverbank</li><li><b>Price</b> Get Quote</li></ul>
<div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan my trip</a></div>
<div class="sza-trust"><span><a href="https://suzutravels.com/certificates/">HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022</a></span><span>Camp + hotel + cab</span><span>Reply within minutes</span></div>
</div>
</section>
<nav class="sza-nav" aria-label="On this page"><div class="sza-nav-in"><a href="#overview">Overview</a><a href="#spots">Camp areas</a><a href="#experience">How it works</a><a href="#season">By month</a><a href="#safety">Rules &amp; safety</a><a href="#booking">How booking works</a><a href="#packages">Packages</a><a href="#faq">FAQ</a><a class="cta" href="{MAIN}" target="_blank" rel="noopener">Get Quote</a></div></nav>

<section class="sza-sec" id="overview">
<span class="sza-kicker">Quick answer</span>
<h2>Camping in Manali, at a glance</h2>
<p class="sza-answer">Camping in Manali means a night in a fixed tent camp at Solang, on the Kothi–Gulaba road, along the Naggar road or in the orchards above town. Camps run best from March to June and mid-September to November. In winter most tent camps close or switch to heated tents, and riverbank camps are risky in the monsoon. Book only registered camps.</p>
<div class="sza-facts"><div class="sza-fact"><div class="k">Areas</div><div class="v">Solang Valley, Kothi–Gulaba (Rohtang road), Naggar road, Sethan &amp; orchard camps, trek camps (Hampta side)</div></div><div class="sza-fact"><div class="k">Best months</div><div class="v">Mar–Jun and mid-Sep–Nov</div></div><div class="sza-fact"><div class="k">Winter (Dec–Feb)</div><div class="v">Heated tents or an igloo stay only; many camps shut</div></div><div class="sza-fact"><div class="k">Monsoon (Jul–mid-Sep)</div><div class="v">Avoid riverbank camps — Kullu banned camps near riverbeds after the July 2022 floods</div></div><div class="sza-fact"><div class="k">Rules</div><div class="v">Registered camps only; forest-area camps need Forest Department permission</div></div><div class="sza-fact"><div class="k">Price</div><div class="v">Get Quote</div></div></div>
</section>

<section class="sza-sec alt" id="spots">
<span class="sza-kicker">Where to camp</span>
<h2>Five camping areas around Manali</h2>
<p class="sza-lead">Pick by month and mood: a meadow near the Solang slopes, pine forest on the Rohtang road, a camp by the Beas, an orchard night above town or tents on a trek.</p>
<div class="sza-grid">{cards}</div>
<div class="sza-media sza-choose" id="camp-month"><video autoplay muted loop playsinline preload="none" poster="{UP}camping-in-manali-explainer-poster.webp" width="1600" height="900" aria-label="Which Manali camp for your month: month pills switch Naggar riverside, Sethan orchards, Solang meadows and Kothi–Gulaba between open, caution and closed; monsoon no camps near the riverbed, registered camps only, price Get Quote"><source src="{CDN}explainer.webm" type="video/webm"><source src="{CDN}explainer.mp4" type="video/mp4"></video><div><h3>Which Manali camp for your month?</h3><ul><li><b>Mar–Jun</b> → all areas open; May–Jun is busiest.</li><li><b>Jul–mid-Sep</b> → stay off the riverbank; rafting and paragliding stop.</li><li><b>mid-Sep–Nov</b> → clear skies, the best overall.</li><li><b>Dec–Feb</b> → heated tents or an igloo stay; most tent camps shut.</li></ul></div></div>
</section>

<section class="sza-sec" id="experience">
<span class="sza-kicker">How it works</span>
<h2>How a Manali camp night works with Suzu</h2>
<ol class="sza-steps">{steps_exp}</ol>
<div class="sza-media"><img src="{UP}friends-campfire-hillside-sunset-768x1152.webp" alt="Group of friends in warm jackets sitting around a campfire on a hillside at sunset" loading="lazy" width="768" height="1152"><div><h3>What a camp night looks like</h3><p>Dome or Swiss tents with bedding, dinner and breakfast, and a bonfire where the camp is allowed one. Add a day at <a href="/adventure/solang-valley-activities/">Solang Valley</a>, a <a href="/adventure/paragliding-in-manali/">paragliding flight</a> or a ride through the <a href="/adventure/atal-tunnel-sissu-snow-trip/">Atal Tunnel to Sissu</a>.</p><p>Carry a warm layer even in May, a torch and shoes with grip. Take all your waste back with you.</p></div></div>
</section>

<section class="sza-sec alt" id="season">
<span class="sza-kicker">When to go</span>
<h2>Camping in Manali by month</h2>
<div class="sza-scroll"><table class="sza-tbl"><thead><tr><th>Months</th><th>Camping</th><th>Notes</th></tr></thead><tbody>{season_html}</tbody></table></div>
<p style="margin-top:14px">Planning New Year in Manali? Tent camps are mostly shut — book an <a href="/adventure/igloo-stay-manali/">igloo stay</a> or a warm hotel early and add a snow day. Read <a href="/manali-in-november/">Manali in November</a> and <a href="/snowfall-in-manali/">snowfall in Manali</a>.</p>
</section>

<div class="sza-band" id="safety"><div class="sza-band-in">
<span class="sza-kicker">Rules &amp; safety</span>
<h2>What we check before we book your camp</h2>
<p class="sza-lead">Suzu Travels is an <a href="https://suzutravels.com/certificates/" style="color:#f3d98f;text-decoration:underline">HP Tourism registered travel agent (Reg. No. DTO-MND-11-243/2022)</a>. We arrange camps with registered local operators and plan around these checks:</p>
<ul class="sza-checks"><li><b>Registered camps only</b>A November 2024 inspection in Kullu found 45 tourism units — camps, homestays and hotels — running without registration. We book only registered camps.</li><li><b>Forest &amp; trek camps</b>Camps in forest areas and on trek routes need Forest Department permission; Kullu has acted against illegal tents in the Hampta, Bhrigu and Beas Kund forests.</li><li><b>No tents on riverbeds</b>In July 2022 Kullu's ADM banned camps close to riverbeds under the Disaster Management Act after camps were washed away.</li><li><b>Monsoon closures</b>Kullu stops rafting, river crossing, paragliding and bungee from 15 July to 15 September (2026 order) — we plan camp activities around it.</li><li><b>Winter nights</b>Sub-zero nights: insulated bedding or a heater, and never a charcoal or gas heater inside a closed tent.</li><li><b>Bonfires &amp; litter</b>Bonfire only where the camp is allowed to light one; carry out all your waste.</li></ul>
</div></div>

<section class="sza-sec" id="booking">
<span class="sza-kicker">How booking works</span>
<h2>Get a quote in minutes</h2>
<ol class="sza-steps">{booking}</ol>
<div class="sza-media"><img src="{UP}lit-tents-meadow-campsite-dusk-768x512.webp" alt="Lit dome tents on a grassy campsite at dusk below a dark hill" loading="lazy" width="768" height="512"><div><h3>What your quote depends on</h3><ul><li>Area and tent type — standard, deluxe, heated tent or igloo</li><li>Month, and weekend or holiday dates</li><li>Meals included, number of nights, group size and kids</li><li>Activities added — rafting, paragliding, a Solang day or a trek camp</li><li>Cab from Delhi or Chandigarh and local transfers (4x4 in snow)</li><li>Hotel nights before or after the camp</li></ul><p>We send today's rate on WhatsApp within minutes.</p></div></div>
</section>

{reel}

<section class="sza-quote"><div><span class="sza-kicker">Ready for a night under the stars?</span><h2>Get your Manali camping quote</h2><p>Tell us your dates, group size and the kind of night you want. We reply with one plan — camp, hotel and cab — within minutes.</p></div><div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan full trip</a></div></section>

<section class="sza-sec" id="packages">
<span class="sza-kicker">Make it a trip</span>
<h2>Add a camp night to your Manali trip</h2>
<p>Most guests add one camp night to a Manali holiday: see our <a href="/destination/manali/">Manali tour packages</a> or the <a href="/shimla-manali-tour-package-by-car/">Shimla Manali tour package by car</a>, then tell us which night you want under canvas. Need only a cab? Book a <a href="/cabs/delhi-to-manali-taxi/">Delhi to Manali taxi</a> or a <a href="/cabs/chandigarh-to-manali-taxi/">Chandigarh to Manali taxi</a>. For riverside camps in the Parvati valley see <a href="/adventure/camping-in-kasol/">camping in Kasol</a>, and for every area in the state, <a href="/adventure/camping-in-himachal/">camping in Himachal</a>.</p>
<div class="sza-btns" style="margin-top:18px">{walink("Manali trip + camp night — Get Quote", what="a Manali trip with one camp night, hotel and cab")}{walink("Camp + rafting or paragliding — Get Quote", what="a Manali camp night with rafting or paragliding", cls="sza-btn line")}</div>
</section>

<section class="sza-sec sza-faq" id="faq">
<span class="sza-kicker">FAQ</span>
<h2>Camping in Manali — questions</h2>
{faq_html}
</section>

<section class="sza-sec alt" id="more">
<span class="sza-kicker">More adventures</span>
<h2>Explore more around Manali</h2>
<div class="sza-cats">{more_html}</div>
</section>
</div>
'''
out = HERE / f"{SLUG}.html"
out.write_text(page, encoding="utf-8")
print(len(page))
