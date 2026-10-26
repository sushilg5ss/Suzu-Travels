#!/usr/bin/env python3
# Generates adventure-kit/pages/dome-stay-in-manali.html (Page Builder night, 27 Oct 2026 IST)
import urllib.parse, pathlib
SLUG = "dome-stay-in-manali"
HERE = pathlib.Path(__file__).resolve().parent
CDN = "https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@fe885e2e8163b03422f8bf9318e4d52494a0cf9c/adventure-kit/media/dome-stay-in-manali/"
UP = "https://suzutravels.com/wp-content/uploads/"
QUOTE = "/himachal-tour-packages-quote/?activity=" + urllib.parse.quote("Dome Stay in Manali")
WHAT = "a dome stay in Manali"

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
    card(f"{UP}2026/10/geodesic-glamping-dome-wooden-deck-forest-768x509.webp", 768, 509,
         "White geodesic glamping dome on a raised wooden deck among trees on a forested hillside in evening light",
         "Year-round", "Classic heated dome", "<b>Insulated dome · heaters · attached bath</b>",
         "An insulated geodesic dome with room heaters, electric blankets and its own bathroom — it runs in every season.",
         "a classic heated dome stay in Manali"),
    card(f"{UP}2026/10/geodesic-glamping-domes-wooden-walkway-600x900.webp", 600, 900,
         "Two white geodesic glamping domes on a wooded slope, reached by a wooden walkway and steps under the trees",
         "Couples", "View dome", "<b>Big window towards the valley</b>",
         "Some domes have a large window or a glass panel facing the valley. Not every dome is see-through — we confirm what your room has.",
         "a view dome stay in Manali for a couple"),
    card(f"{UP}2026/10/snowman-lit-snow-igloo-night-768x512.webp", 768, 512,
         "Snowman standing in front of a snow igloo glowing with warm light from inside at night",
         "Snow season", "Dome night + igloo visit", "<b>When snow allows, mid-Dec/Jan–Feb</b>",
         "Sleep warm in a dome and visit, or spend a night in, a snow igloo once there is enough settled snow.",
         "a dome night with an igloo visit in Manali", "/adventure/igloo-stay-manali/"),
    card(f"{UP}2026/09/suv-snowy-mountain-road-768x411.webp", 768, 411,
         "White SUV driving on a snowy road through pine forest during snowfall",
         "Adventure", "Dome + snow day", "<b>Snow play, Solang or Sissu by cab</b>",
         "Morning snow play near the domes, or a cab day to Solang or the Atal Tunnel and Sissu — snow suit and boots arranged on request.",
         "a dome stay plus a snow day in Manali", "/adventure/snow-activities-manali/"),
    card(f"{UP}2026/10/camping-tents-starry-night-sky-768x702.webp", 768, 702,
         "Row of small camping tents below a forested hill under a starry night sky with the Milky Way",
         "Budget", "Camp instead", "<b>Tents lower down the valley</b>",
         "Dome or Swiss tents in Manali's riverside and forest camps — lower, easier to reach, best outside deep winter.",
         "camping in Manali instead of a dome", "/adventure/camping-in-manali/"),
])

steps_exp = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Send your dates", "Dates, group and ages on WhatsApp — we check snow, the Hamta road and the property's age rules before we quote."),
    ("Cab to Manali", "From Delhi, Chandigarh or Manali town; after fresh snow we switch to a 4x4 with a local driver."),
    ("Permit at Prini", "The vehicle's Hamta road permit is checked at the Prini barrier, then the car climbs the switchbacks."),
    ("Walk to your dome", "A short walk from the road — at some properties a steep path downhill."),
    ("Warm evening", "Heater on, dinner (most places run a fixed menu) and stargazing on clear nights."),
    ("Next morning", "Snow play near the domes, or Solang / Atal Tunnel–Sissu, then your hotel or the drive onward."),
])

booking = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Tell us", "WhatsApp or the quote form — dates, group size, ages and where you start from."),
    ("We check your date", "Snow, road and permit for that week, and a registered stay that accepts your group."),
    ("You get one quote", "Dome night, hotel nights, cab (4x4 if needed) and a snow day in one plan."),
    ("Confirm and go", "We send the permit details, pick-up time and what to pack."),
])

season = [
    ("Oct–Nov", "Cold, clear nights; early snow possible on the high slopes", "Stargazing, quiet dates"),
    ("Dec", "Snow possible, often late Dec; Christmas–New Year is peak — book early", "Snow + festive"),
    ("Jan–Feb", "Most settled snow; the road can shut after fresh snow until it is cleared", "Snow stay, igloo combo"),
    ("Mar", "Snow fades, slush on the road", "Shoulder dates"),
    ("Apr–Jun", "Green valley, cool nights", "Families with older kids, workations"),
    ("Jul–Sep", "Monsoon; landslide risk on hill roads", "Only with flexible dates"),
]
season_html = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in season)

faqs = [
    ("Where are dome stays in Manali?", "Most are on the Hamta road above Prini, around Sethan village, 12–15 km from Mall Road at about 2,600–2,700 m. It is the same road that leads to the <a href=\"/adventure/hampta-pass-trek/\">Hampta Pass trek</a>."),
    ("Are the domes heated in winter?", "Yes — insulated domes with room heaters and electric blankets, and an attached bathroom. Ask about backup power, because snow can cut electricity and heaters stop when the power goes."),
    ("Dome or igloo — what is the difference?", "A dome is a heated tent that runs all year. An <a href=\"/adventure/igloo-stay-manali/\">igloo</a> is built from snow and exists only when snow allows, usually mid-December or January to February. Many guests sleep in a dome and visit an igloo."),
    ("Can a car reach the domes in snow?", "After fresh snow only 4x4 vehicles go up the Hamta road, and the road can close until it is cleared. We send a 4x4 with a local driver and time the drive."),
    ("Do I need a permit?", "Yes. Vehicles going up the Hamta road need a one-day permit from the official portal (rohtangpermits.hp.gov.in), checked at the Prini barrier; there is a daily vehicle quota. Carry the printout, ID and PUC — we arrange it for your cab."),
    ("Are children allowed?", "It depends on the property — some do not host children under 13, and the path down can be steep. Tell us the ages and we shortlist only places that accept them."),
    ("Will I see snow?", "Snow is most likely from late December to February, but never guaranteed. If there is none near the domes, we plan a day to <a href=\"/adventure/atal-tunnel-sissu-snow-trip/\">Atal Tunnel–Sissu</a> or <a href=\"/adventure/solang-valley-activities/\">Solang</a>."),
    ("How much does a dome stay in Manali cost?", "Get Quote — the rate depends on dates, dome type, nights, meals, group and cab. Send your dates on WhatsApp and we share today's rate within minutes."),
]
faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)

more = [
    ("/adventure/igloo-stay-manali/", "🧊", "Igloo stay in Manali", "Snow-built, Dec–Feb"),
    ("/adventure/camping-in-manali/", "⛺", "Camping in Manali", "Five camp areas"),
    ("/adventure/snow-activities-manali/", "❄️", "Snow activities", "Solang, Gulaba, sledging"),
    ("/adventure/atal-tunnel-sissu-snow-trip/", "🏔️", "Atal Tunnel &amp; Sissu", "Snow day from Manali"),
    ("/adventure/snow-suit-and-boots-on-rent-manali/", "🧥", "Snow suit &amp; boots", "Rent for your snow day"),
    ("/adventure/adventure-activities-in-manali/", "🧭", "Manali adventures", "What runs in your month"),
]
more_html = "".join(f'<a class="sza-cat" href="{h}"><span class="ic">{i}</span><span class="n">{n}</span><span class="c">{c}</span></a>' for h, i, n, c in more)

reel = (HERE.parent / "media" / SLUG / "reel-section.html").read_text(encoding="utf-8").strip()

page = f'''<!-- dome-stay-in-manali — built by Page Builder (night) 27 Oct 2026 IST from the Research Lead brief 26 Oct + Visual Studio media @fe885e2 (reel @aa40fb9). Kit v1.8. No prices, no property names. Left off as unverified: permit time window (6 am–6 pm / 10 pm hotel exemption), number of dome properties, transparent roofs. Generic photos carry neutral alt text; no dome-interior photo (none honest found). -->
<style>.sza-dsm .sza-hero-in>*{{max-width:620px}}.sza-dsm .sza-chips{{max-width:700px}}.sza-dsm .sza-media ul{{padding-left:20px;list-style:disc;margin:0}}.sza-dsm .sza-media ul li{{margin:0 0 8px}}.sza-dsm .sza-media img{{height:auto;aspect-ratio:4/3;object-fit:cover}}.sza-dsm .sza-media video{{height:auto;aspect-ratio:16/9}}.sza-dsm #spots .sza-grid{{grid-template-columns:repeat(auto-fit,minmax(min(300px,100%),1fr))}}.sza-dsm #spots .sza-card .img img{{aspect-ratio:3/2;object-fit:cover}}.sza-dsm .sza-checks{{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}.sza-dsm .sza-choose{{margin-top:32px}}@media(max-width:820px){{.sza-dsm .sza-hero video{{object-position:30% 50%}}.sza-dsm .sza-hero:after{{background:linear-gradient(180deg,rgba(11,31,51,.35) 0%,rgba(11,31,51,.6) 40%,rgba(11,31,51,.94) 100%)}}}}</style>
<div class="sza sza-dsm">
<section class="sza-hero">
<video autoplay muted loop playsinline preload="metadata" poster="{UP}2026/10/dome-stay-in-manali-hero-poster.webp" aria-label="A geodesic dome glowing at blue hour, two domes on a wooden walkway, a lit snow igloo and a starry sky, with a gold road line from Mall Road to Prini and the dome stays, altitude rising from about 2,050 to 2,650 metres and falling snow"><source src="{CDN}hero.webm" type="video/webm"><source src="{CDN}hero.mp4" type="video/mp4"></video>
<div class="sza-hero-in">
<span class="sza-kicker">Snow · Stays · Hamta road above Prini, Manali</span>
<p class="sza-hero-tag">Sleep under a dome, wake up to snow</p>
<p class="sza-hero-sub">Heated geodesic domes 12–15 km above Manali — we check the road, permit and snow for your dates, then add cab and sightseeing.</p>
<ul class="sza-chips"><li><b>~2,600–2,700 m</b> altitude</li><li><b>12–15 km</b> from Mall Road</li><li><b>Heated</b> attached bath</li><li><b>Open</b> all year</li><li><b>Snow</b> late Dec–Feb</li><li><b>Price</b> Get Quote</li></ul>
<div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan my trip</a></div>
<div class="sza-trust"><span><a href="https://suzutravels.com/certificates/">HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022</a></span><span>Dome + hotel + cab</span><span>Reply within minutes</span></div>
</div>
</section>
<nav class="sza-nav" aria-label="On this page"><div class="sza-nav-in"><a href="#overview">Overview</a><a href="#spots">Dome options</a><a href="#experience">How it works</a><a href="#season">By month</a><a href="#safety">Safety</a><a href="#booking">How booking works</a><a href="#packages">Packages</a><a href="#faq">FAQ</a><a class="cta" href="{MAIN}" target="_blank" rel="noopener">Get Quote</a></div></nav>

<section class="sza-sec" id="overview">
<span class="sza-kicker">Quick answer</span>
<h2>Dome stays near Manali, at a glance</h2>
<p class="sza-answer">Most dome stays near Manali sit on the Hamta road above Prini, around Sethan village, 12–15 km from Mall Road at about 2,600–2,700 m. A dome is an insulated geodesic tent with heaters and an attached bathroom, so it runs all year — unlike an igloo, which needs settled snow. In snow the road is 4x4-only, and a Hamta road permit is checked at Prini.</p>
<div class="sza-facts"><div class="sza-fact"><div class="k">Where</div><div class="v">Hamta road, Prini → Sethan, Manali tehsil</div></div><div class="sza-fact"><div class="k">Altitude</div><div class="v">About 2,600–2,700 m (Manali town ~2,050 m)</div></div><div class="sza-fact"><div class="k">Drive</div><div class="v">12–15 km, 40–60 min; 1–2 h on snow or ice</div></div><div class="sza-fact"><div class="k">Season</div><div class="v">Domes all year; snow most likely late Dec–Feb</div></div><div class="sza-fact"><div class="k">Access</div><div class="v">One-day Hamta permit for vehicles, checked at the Prini barrier; 4x4 after fresh snow</div></div><div class="sza-fact"><div class="k">Price</div><div class="v">Get Quote</div></div></div>
</section>

<section class="sza-sec alt" id="spots">
<span class="sza-kicker">Choose your night</span>
<h2>Five ways to do a dome stay in Manali</h2>
<p class="sza-lead">A warm dome on its own, a room with a valley window, a dome night with an igloo visit, a dome plus a snow day — or a camp lower down if a dome is more than you need.</p>
<div class="sza-grid">{cards}</div>
<div class="sza-media sza-choose" id="road-to-dome"><video autoplay muted loop playsinline preload="none" poster="{UP}2026/10/dome-stay-in-manali-explainer-poster.webp" width="1600" height="900" aria-label="Your road to a dome: Mall Road to the Prini barrier where the permit QR is scanned, up the Hamta road switchbacks to the domes, 12 to 15 km and about 2,050 to 2,650 m; after fresh snow the car switches to a 4x4; dome all year, igloo December to February when snow allows"><source src="{CDN}explainer.webm" type="video/webm"><source src="{CDN}explainer.mp4" type="video/mp4"></video><div><h3>Your road to a dome</h3><ul><li><b>Mall Road → Prini</b> → the barrier where the vehicle permit is checked.</li><li><b>Hamta road switchbacks</b> → 12–15 km, up to about 2,650 m.</li><li><b>After fresh snow</b> → 4x4 only; the road can shut until cleared.</li><li><b>Dome</b> all year · <b>igloo</b> Dec–Feb, when snow allows.</li></ul></div></div>
</section>

<section class="sza-sec" id="experience">
<span class="sza-kicker">How it works</span>
<h2>How a dome night works with Suzu</h2>
<ol class="sza-steps">{steps_exp}</ol>
<div class="sza-media"><img src="{UP}2026/10/car-on-cleared-snowy-road-winter-768x411.webp" alt="A car driving carefully on a cleared snowy road through snow-covered pine trees during light snowfall" loading="lazy" width="768" height="411"><div><h3>Dome or igloo?</h3><p>Pick a dome if you want warmth, a private bathroom and any month of the year. Pick an <a href="/adventure/igloo-stay-manali/">igloo stay</a> if sleeping inside snow is the point — it runs only when snow allows. Many couples sleep in a dome and visit an igloo the same trip.</p><p>Add a snow day at <a href="/adventure/solang-valley-activities/">Solang Valley</a> or through the <a href="/adventure/atal-tunnel-sissu-snow-trip/">Atal Tunnel to Sissu</a>, with <a href="/adventure/snow-suit-and-boots-on-rent-manali/">snow suit and boots</a> on request.</p></div></div>
</section>

<section class="sza-sec alt" id="season">
<span class="sza-kicker">When to go</span>
<h2>Dome stays in Manali by month</h2>
<div class="sza-scroll"><table class="sza-tbl"><thead><tr><th>Months</th><th>Conditions</th><th>Best for</th></tr></thead><tbody>{season_html}</tbody></table></div>
<p style="margin-top:14px">Planning Christmas or New Year? Domes fill early for those dates — see <a href="/christmas-new-year-manali-packages/">Christmas &amp; New Year Manali packages</a>, <a href="/manali-in-december/">Manali in December</a> and <a href="/manali-in-january/">Manali in January</a>.</p>
</section>

<div class="sza-band" id="safety"><div class="sza-band-in">
<span class="sza-kicker">Safety</span>
<h2>What we check before we book your dome</h2>
<p class="sza-lead">Suzu Travels is an <a href="https://suzutravels.com/certificates/" style="color:#f3d98f;text-decoration:underline">HP Tourism registered travel agent (Reg. No. DTO-MND-11-243/2022)</a>. We arrange stays with registered local properties and plan around these checks:</p>
<ul class="sza-checks"><li><b>Registered stays only</b>We book only properties registered with HP Tourism as a hotel or homestay.</li><li><b>Safe heating</b>Electric heaters and blankets only — never a coal angithi or an unvented gas heater in a closed dome (carbon-monoxide risk). We ask about backup power, because snow brings power cuts.</li><li><b>Road after snow</b>After fresh snow only 4x4s go up the Hamta road: a local driver, chains, no two-wheelers on snow or ice, and SDM Manali orders on the day.</li><li><b>Permit papers</b>The printed one-day vehicle permit, ID and PUC; details must match the vehicle, and older vehicles may not be allowed.</li><li><b>Kids &amp; mobility</b>Some dome properties do not host children under 13, and steep paths do not suit elderly guests with mobility issues or pregnant guests — we confirm per property.</li><li><b>Altitude ~2,650 m</b>Drink water and skip alcohol on the first night; mild symptoms are common, worsening ones mean coming down.</li></ul>
</div></div>

<section class="sza-sec" id="booking">
<span class="sza-kicker">How booking works</span>
<h2>Get a quote in minutes</h2>
<ol class="sza-steps">{booking}</ol>
<div class="sza-media"><img src="{UP}2026/10/geodesic-glamping-dome-wooden-deck-forest-768x509.webp" alt="White geodesic glamping dome on a raised wooden deck among trees on a forested hillside in evening light" loading="lazy" width="768" height="509"><div><h3>What your quote depends on</h3><ul><li>Dates — Christmas–New Year and long weekends are peak</li><li>Dome type and number of nights</li><li>Meals (most places run a fixed menu)</li><li>Group size and ages</li><li>Cab type (4x4 in snow), pick-up city and the vehicle permit</li><li>Add-ons: igloo visit, snow suit and boots, Solang or Atal Tunnel–Sissu day, Manali hotel nights</li></ul><p>We send today's rate on WhatsApp within minutes.</p></div></div>
</section>

{reel}

<section class="sza-quote"><div><span class="sza-kicker">Ready for a warm night in the snow?</span><h2>Get your Manali dome stay quote</h2><p>Tell us your dates, group and ages. We reply with one plan — dome night, hotel and cab — within minutes.</p></div><div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan full trip</a></div></section>

<section class="sza-sec" id="packages">
<span class="sza-kicker">Make it a trip</span>
<h2>Add a dome night to your Manali trip</h2>
<p>A popular plan is two hotel nights in Manali, one dome night and a Solang or Sissu snow day: start from our <a href="/destination/manali/">Manali tour packages</a> or <a href="/destination/honeymoon-packages/">honeymoon packages</a> and tell us which night you want in a dome. Need only a cab? Book a <a href="/cabs/delhi-to-manali-taxi/">Delhi to Manali taxi</a> or the <a href="/cabs/manali-taxi-service/">Manali taxi service</a>. Prefer tents? See <a href="/adventure/camping-in-manali/">camping in Manali</a>.</p>
<div class="sza-btns" style="margin-top:18px">{walink("Manali trip + dome night — Get Quote", what="a Manali trip with one dome night, hotel and cab")}{walink("Honeymoon with a dome night — Get Quote", what="a Manali honeymoon with a dome night", cls="sza-btn line")}</div>
</section>

<section class="sza-sec sza-faq" id="faq">
<span class="sza-kicker">FAQ</span>
<h2>Dome stay in Manali — questions</h2>
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
