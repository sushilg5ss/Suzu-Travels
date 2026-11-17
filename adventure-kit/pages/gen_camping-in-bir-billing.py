#!/usr/bin/env python3
# Generates adventure-kit/pages/camping-in-bir-billing.html (Page Builder night, 18 Nov 2026 IST)
import urllib.parse, pathlib
SLUG = "camping-in-bir-billing"
HERE = pathlib.Path(__file__).resolve().parent
CDN = "https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@60c8596551cfb2bd2b7c6db02c962e7f87dc985c/adventure-kit/media/camping-in-bir-billing/"
U10 = "https://suzutravels.com/wp-content/uploads/2026/10/"
U11 = "https://suzutravels.com/wp-content/uploads/2026/11/"
QUOTE = "/himachal-tour-packages-quote/?activity=" + urllib.parse.quote("Camping in Bir Billing")
WHAT = "camping in Bir Billing"

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
    card(f"{U10}dome-tents-hilltop-meadow-sunrise-768x498.webp", 768, 498,
         "Red, blue and orange dome tents on a grassy hilltop meadow at sunrise, with layered blue mountain ridges behind",
         "Year-round", "Bir village field camps", "<b>~1,450–1,500 m · Bir, Gharnala, Chowgan side</b>",
         "Tents and huts in the fields around Bir village; walk to the paragliding landing site, the Tibetan colony and the monasteries. The camp zone that works in every season except the monsoon.",
         "a Bir village field camp, Bir Billing"),
    card(f"{U11}suzu-bir-weather-fig-1-768x576.webp", 768, 576,
         "The upper paragliding take-off at Billing",
         "Oct–Nov · Mar–Jun", "Billing ridge camps", "<b>~2,400 m · 14 km up the road from Bir</b>",
         "Sunset and stars at the take-off ridge. Colder and simpler than the village; in December–February snow and ice make it a day trip, not a camp night.",
         "a Billing ridge camp, Bir Billing"),
    card(f"{U11}canvas-trek-tents-green-meadow-misty-mountains-768x512.webp", 768, 512,
         "Row of canvas trek tents on a green meadow below misty forested mountains with snow patches, a trekker walking in front",
         "Trekkers", "Rajgundha valley", "<b>~2,700 m · 12–14 km walk from Billing</b>",
         "A walk-in camp or homestay night in the valley behind Billing, with a local guide and check-post registration. Snow closes most access December–March.",
         "a Rajgundha camp and trek from Billing", "/adventure/rajgundha-valley-trek/"),
    card(f"{U11}suzu-bir-weather-g-5-768x576.webp", 768, 576,
         "Paragliders over Bir Billing",
         "Fly + camp", "Fly + camp weekend", "<b>Camp night in Bir + tandem flight from Billing</b>",
         "Camp in the village, drive up to Billing next morning for a tandem flight (season and weather permitting). The flight is usually a separate add-on — we quote both together.",
         "a camp night in Bir with a tandem paragliding flight from Billing", "/adventure/paragliding-in-bir-billing/"),
])

steps_exp = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Tell us your plan", "Dates, group and tent type — standard tent, safari tent or dome."),
    ("We pick the zone", "Bir village, Billing ridge or Rajgundha for your month, booked with a registered local camp."),
    ("Reach Bir", "By cab from Delhi (~520 km, overnight) or Chandigarh (~260 km), or fly to Kangra–Gaggal (~70 km)."),
    ("Evening at camp", "Village or monastery walk, a bonfire where the camp allows it, dinner."),
    ("Next morning", "Drive up to Billing for a tandem flight (season and weather permitting) or start the Rajgundha walk."),
    ("Onward", "Palampur, Barot, Dharamshala or Manali with the same cab."),
])

booking = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Tell us", "WhatsApp or the quote form — dates, group size, tent type and where you start from."),
    ("We check your date", "Season, snow on the Billing road, flying days and a registered camp for that night."),
    ("You get one quote", "Camp night, flight if you want one, hotel nights and cab in one plan."),
    ("Confirm and go", "We send the camp location, check-in time and what to pack."),
])

season = [
    ("Oct–Nov", "Best — clear skies, flying on", "Best; cold nights at Billing"),
    ("Dec–Feb", "Open, chilly — near freezing at night", "Snow at Billing; Rajgundha mostly snowed in — not advised"),
    ("Mar–Jun", "Good; May–Jun busiest", "Good; Rajgundha opens from March–April"),
    ("Jul–mid-Sep", "Wet; flying banned 15 Jul–15 Sep", "Landslide risk — not advised"),
    ("Late Sep", "Flying resumes; camps reopen", "Good"),
]
season_html = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in season)

faqs = [
    ("Where can you camp in Bir Billing?", "In three zones: the fields around Bir village (Bir, Gharnala and Chowgan side), near the Billing take-off ridge, and in <a href=\"/adventure/rajgundha-valley-trek/\">Rajgundha valley</a> behind Billing."),
    ("Can you camp at Billing in December?", "Billing gets snow and sub-zero nights from December to February, and the road can ice over. We suggest a Bir village camp and a day trip up to Billing when the road is open."),
    ("How far is Billing from Bir?", "14 km by road, or a steep footpath of about 7 km."),
    ("Is paragliding included in camping packages?", "Not always — the tandem flight is usually a separate add-on. We quote the camp and the <a href=\"/adventure/paragliding-in-bir-billing/\">paragliding flight</a> together so you know exactly what is included."),
    ("When is paragliding closed in Bir Billing?", "Every year from 15 July to 15 September (the monsoon ban), and on bad-weather days."),
    ("How cold is Bir camping in winter?", "Days are mild, but nights drop to around freezing at Bir and below zero at Billing. Carry thermals and a warm sleeping bag."),
    ("Can we trek and camp at Rajgundha?", "Yes, in March–June and September–November. It is a 12–14 km walk from Billing, and you register at the Rajgundha check post before you go."),
    ("How much does camping in Bir Billing cost?", "Get Quote — the rate depends on the camp zone, tent type, meals, month, group size and any flight or cab you add. Send your dates on WhatsApp and we reply with today's rate within minutes."),
]
faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)

more = [
    ("/adventure/paragliding-in-bir-billing/", "🪂", "Paragliding in Bir Billing", "Tandem flights from Billing"),
    ("/adventure/things-to-do-in-bir-billing/", "🏞️", "Things to do in Bir Billing", "Monasteries, cafés, walks"),
    ("/adventure/rajgundha-valley-trek/", "🥾", "Rajgundha valley trek", "Walk in from Billing"),
    ("/adventure/camping-in-himachal/", "⛺", "Camping in Himachal", "Camp areas across the state"),
    ("/adventure/winter-treks-in-himachal/", "❄️", "Winter treks in Himachal", "What is open in snow"),
    ("/adventure/triund-trek/", "🏔️", "Triund trek", "Dharamshala's ridge camp"),
]
more_html = "".join(f'<a class="sza-cat" href="{h}"><span class="ic">{i}</span><span class="n">{n}</span><span class="c">{c}</span></a>' for h, i, n, c in more)

reel = (HERE.parent / "media" / SLUG / "reel-section.html").read_text(encoding="utf-8").strip()

page = f'''<!-- camping-in-bir-billing — built by Page Builder (night) 18 Nov 2026 IST from the Research Lead brief 17 Nov (Project doc claude/adventure-research/briefs/camping-in-bir-billing.md) + Visual Studio night media @60c8596. Kit v2.0. No prices, no operator or camp names. Brief badge "Most booked" replaced by "Fly + camp" (kit badge rule). Unverified items left off: which Billing ridge camps run Dec–Feb, any Kangra camping-permit rule for Billing forest land. Generic photos carry neutral alt text. -->
<style>.sza-cbb .sza-hero-in>*{{max-width:620px}}@media(min-width:901px){{.sza-cbb .sza-hero-in>*{{max-width:min(560px,44vw)}}}}.sza-cbb .sza-chips{{max-width:700px}}.sza-cbb .sza-media ul{{padding-left:20px;list-style:disc;margin:0}}.sza-cbb .sza-media ul li{{margin:0 0 8px}}.sza-cbb .sza-media img{{height:auto;aspect-ratio:4/3;object-fit:cover}}.sza-cbb .sza-media video{{height:auto;aspect-ratio:16/9}}.sza-cbb #spots .sza-grid{{grid-template-columns:repeat(auto-fit,minmax(min(300px,100%),1fr))}}.sza-cbb #spots .sza-card .img img{{aspect-ratio:3/2;object-fit:cover}}.sza-cbb .sza-checks{{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}.sza-cbb .sza-choose{{margin-top:32px}}@media(min-width:1000px){{.sza-cbb #experience .sza-steps{{grid-template-columns:repeat(3,1fr)}}}}@media(max-width:820px){{.sza-cbb .sza-hero video{{object-position:20% 50%}}.sza-cbb .sza-hero:after{{background:linear-gradient(180deg,rgba(11,31,51,.45) 0%,rgba(11,31,51,.68) 45%,rgba(11,31,51,.95) 100%)}}}}</style>
<div class="sza sza-cbb">
<section class="sza-hero">
<video autoplay muted loop playsinline preload="metadata" poster="{U11}camping-in-bir-billing-hero-poster.webp" aria-label="Lit tents at dusk, a bonfire under pines, the Billing paragliding take-off and tents under the stars, with a gold line from Bir to Billing to Rajgundha and an altitude counter from about 1,450 to 2,700 metres; best October to November and March to June"><source src="{CDN}hero.webm" type="video/webm"><source src="{CDN}hero.mp4" type="video/mp4"></video>
<div class="sza-hero-in">
<span class="sza-kicker">Treks &amp; Camps · Bir Billing, Kangra</span>
<p class="sza-hero-tag">A tent under the Dhauladhars, a flight the next morning</p>
<p class="sza-hero-sub">Three camp zones — Bir village fields, the Billing take-off ridge and Rajgundha — and which one works in your month. We add the camp to your hotel + cab plan.</p>
<ul class="sza-chips"><li><b>Bir</b> ~1,450–1,500 m</li><li><b>Billing</b> ~2,400 m</li><li><b>Rajgundha</b> ~2,700 m</li><li><b>Best</b> Oct–Nov &amp; Mar–Jun</li><li><b>Winter</b> stay low at Bir</li><li><b>Price</b> Get Quote</li></ul>
<div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan my trip</a></div>
<div class="sza-trust"><span><a href="https://suzutravels.com/certificates/">HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022</a></span><span>Camp + hotel + cab</span><span>Reply within minutes</span></div>
</div>
</section>
<nav class="sza-nav" aria-label="On this page"><div class="sza-nav-in"><a href="#overview">Overview</a><a href="#spots">Camp zones</a><a href="#experience">How it works</a><a href="#season">By month</a><a href="#safety">Rules &amp; safety</a><a href="#booking">How booking works</a><a href="#packages">Make it a trip</a><a href="#faq">FAQ</a><a class="cta" href="{MAIN}" target="_blank" rel="noopener">Get Quote</a></div></nav>

<section class="sza-sec" id="overview">
<span class="sza-kicker">Quick answer</span>
<h2>Camping in Bir Billing, at a glance</h2>
<p class="sza-answer">Camping in Bir Billing means one of three zones: farm-field camps around Bir village (about 1,450–1,500 m, open most of the year), ridge camps near the Billing take-off (about 2,400 m, 14 km up the road) and Rajgundha valley (about 2,700 m, a 12–14 km walk). October–November and March–June are best; in December–February stay low at Bir — Billing gets snow and sub-zero nights.</p>
<div class="sza-facts"><div class="sza-fact"><div class="k">Bir village camps</div><div class="v">~1,450–1,500 m, near the landing site and the Tibetan colony</div></div><div class="sza-fact"><div class="k">Billing ridge</div><div class="v">~2,400 m take-off, 14 km by road from Bir (or a steep ~7 km footpath)</div></div><div class="sza-fact"><div class="k">Rajgundha</div><div class="v">~2,700 m, 12–14 km / 5–6 h walk from Billing; snow closes most access Dec–Mar</div></div><div class="sza-fact"><div class="k">Best months</div><div class="v">Oct–Nov (clear skies, flying) and Mar–Jun; flying ban 15 Jul–15 Sep</div></div><div class="sza-fact"><div class="k">Winter (Dec–Feb)</div><div class="v">Nights below zero up high; the ridge road can ice over in Jan–Feb</div></div><div class="sza-fact"><div class="k">Price</div><div class="v">Get Quote</div></div></div>
</section>

<section class="sza-sec alt" id="spots">
<span class="sza-kicker">Where to camp</span>
<h2>Three camp zones, plus the fly + camp weekend</h2>
<p class="sza-lead">Pick by month: the village fields work almost all year, the ridge and Rajgundha only when there is no snow and no monsoon.</p>
<div class="sza-grid">{cards}</div>
<div class="sza-media sza-choose" id="camp-month"><video autoplay muted loop playsinline preload="none" poster="{U11}camping-in-bir-billing-which-camp-explainer-poster.webp" width="1600" height="900" aria-label="Which camp for your month: Bir about 1,450 to 1,500 m, 14 km road to Billing about 2,400 m, 12 to 14 km walk to Rajgundha about 2,700 m, with month chips for each zone — green good, blue snow or freezing nights December to February, grey monsoon with no flying 15 July to 15 September"><source src="{CDN}explainer.webm" type="video/webm"><source src="{CDN}explainer.mp4" type="video/mp4"></video><div><h3>Which camp for your month?</h3><ul><li><b>Oct–Nov</b> → every zone is good; the clearest skies and flying days.</li><li><b>Dec–Feb</b> → stay at a Bir village camp; Billing gets snow, Rajgundha is snowed in.</li><li><b>Mar–Jun</b> → all zones; Rajgundha opens from March–April, May–Jun is busiest.</li><li><b>Jul–mid-Sep</b> → wet; no flying, and skip the ridge and Rajgundha.</li></ul></div></div>
</section>

<section class="sza-sec" id="experience">
<span class="sza-kicker">How it works</span>
<h2>How a Bir Billing camp night works with Suzu</h2>
<ol class="sza-steps">{steps_exp}</ol>
<div class="sza-media"><img src="{U10}bonfire-pine-forest-night-768x1152.webp" alt="Small group sitting around a bright bonfire under pine trees at night" loading="lazy" width="768" height="1152"><div><h3>What a camp night looks like</h3><p>A standard tent, safari tent or dome with bedding, dinner and breakfast, and a bonfire where the camp is allowed one. Spend the evening on a village or monastery walk — see <a href="/adventure/things-to-do-in-bir-billing/">things to do in Bir Billing</a> — and fly next morning from Billing with a <a href="/adventure/paragliding-in-bir-billing/">tandem paragliding flight</a>.</p><p>Carry a warm layer even in May, a torch and shoes with grip. Take all your waste back with you.</p></div></div>
</section>

<section class="sza-sec alt" id="season">
<span class="sza-kicker">When to go</span>
<h2>Camping in Bir Billing by month</h2>
<div class="sza-scroll"><table class="sza-tbl"><thead><tr><th>Months</th><th>Bir village camps</th><th>Billing / Rajgundha</th></tr></thead><tbody>{season_html}</tbody></table></div>
<p style="margin-top:14px">Going in December? Read <a href="/himachal-in-december/">Himachal in December</a> and our <a href="/adventure/winter-treks-in-himachal/">winter treks guide</a> — and plan a Bir village camp rather than a ridge night. For the whole area, see <a href="/bir-billing-ghumne-ki-jagah/">Bir Billing ghumne ki jagah</a>.</p>
</section>

<div class="sza-band" id="safety"><div class="sza-band-in">
<span class="sza-kicker">Rules &amp; safety</span>
<h2>What we check before we book your camp</h2>
<p class="sza-lead">Suzu Travels is an <a href="https://suzutravels.com/certificates/" style="color:#f3d98f;text-decoration:underline">HP Tourism registered travel agent (Reg. No. DTO-MND-11-243/2022)</a>. We arrange camps with registered local operators and plan around these checks:</p>
<ul class="sza-checks"><li><b>Registered camps only</b>We book registered or designated camps — no wild camping on forest land without permission, and no open fires outside the camp's fire pit.</li><li><b>Rajgundha check post</b>Rajgundha is one of Kangra's 10 trek check posts (set up in November 2025): register before you walk, and go with a local guide.</li><li><b>Winter road</b>No sedan up the Billing road on ice — 4x4 or walk, and only when the road is open. Sleeping bags rated below zero.</li><li><b>Paragliding add-on</b>Registered pilots at the notified Bir Billing site only; no passengers under 12 years or 30 kg (HP Aero Sports Rules 2022, amended 2025).</li><li><b>Monsoon closures</b>No flying from 15 July to 15 September; skip ridge and Rajgundha nights in the monsoon (landslides, flash streams).</li><li><b>Bonfires &amp; litter</b>Bonfire only where the camp is allowed to light one; carry out all your waste.</li></ul>
</div></div>

<section class="sza-sec" id="booking">
<span class="sza-kicker">How booking works</span>
<h2>Get a quote in minutes</h2>
<ol class="sza-steps">{booking}</ol>
<div class="sza-media"><img src="{U10}lit-tents-snow-mountain-night-768x512.webp" alt="Two lit red and green tents pitched on deep snow below a snow-covered mountain with pine trees, at night" loading="lazy" width="768" height="512"><div><h3>What your quote depends on</h3><ul><li>Camp zone — Bir village, Billing ridge or Rajgundha</li><li>Tent type — standard, safari tent, dome or hut</li><li>Meals included and a bonfire</li><li>Weekend or weekday, and festival dates (Christmas–New Year, long weekends)</li><li>Group size and number of tents</li><li>Paragliding add-on and flight video</li><li>Cab from Delhi, Chandigarh or Kangra airport; nights in Palampur or Dharamshala</li></ul><p>We send today's rate on WhatsApp within minutes.</p></div></div>
</section>

{reel}

<section class="sza-quote"><div><span class="sza-kicker">Ready for a night under the Dhauladhars?</span><h2>Get your Bir Billing camping quote</h2><p>Tell us your dates, group size and the kind of night you want. We reply with one plan — camp, flight, hotel and cab — within minutes.</p></div><div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan full trip</a></div></section>

<section class="sza-sec" id="packages">
<span class="sza-kicker">Make it a trip</span>
<h2>Add a Bir camp night to your Himachal trip</h2>
<p>Most guests pair a Bir camp night with Dharamshala and McLeodganj (and a day on the <a href="/adventure/triund-trek/">Triund trek</a>), with Barot, or on the way to Manali — where you can add <a href="/adventure/camping-in-manali/">camping in Manali</a> too. Coming from Delhi? Book a <a href="/cabs/delhi-to-dharamshala-taxi/">Delhi to Dharamshala taxi</a> and we route it via Bir. For every camp area in the state, see <a href="/adventure/camping-in-himachal/">camping in Himachal</a>.</p>
<div class="sza-btns" style="margin-top:18px">{walink("Bir camp + Dharamshala weekend — Get Quote", what="a Bir Billing camp night with Dharamshala and McLeodganj, hotel and cab")}{walink("Camp + paragliding — Get Quote", what="a Bir Billing camp night with a tandem paragliding flight", cls="sza-btn line")}</div>
</section>

<section class="sza-sec sza-faq" id="faq">
<span class="sza-kicker">FAQ</span>
<h2>Camping in Bir Billing — questions</h2>
{faq_html}
</section>

<section class="sza-sec alt" id="more">
<span class="sza-kicker">More adventures</span>
<h2>Explore more around Bir and Kangra</h2>
<div class="sza-cats">{more_html}</div>
</section>
</div>
'''
out = HERE / f"{SLUG}.html"
out.write_text(page, encoding="utf-8")
print(len(page))
