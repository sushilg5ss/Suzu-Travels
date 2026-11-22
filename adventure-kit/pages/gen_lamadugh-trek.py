#!/usr/bin/env python3
# Generates adventure-kit/pages/lamadugh-trek.html (Page Builder night, 23 Nov 2026 IST)
import urllib.parse, pathlib
SLUG = "lamadugh-trek"
HERE = pathlib.Path(__file__).resolve().parent
CDN = "https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@2355aad29c4405299061ed824281080cbf353c4e/adventure-kit/media/lamadugh-trek/"
U10 = "https://suzutravels.com/wp-content/uploads/2026/10/"
U11 = "https://suzutravels.com/wp-content/uploads/2026/11/"
QUOTE = "/himachal-tour-packages-quote/?activity=" + urllib.parse.quote("Lamadugh trek")
WHAT = "the Lamadugh trek in Manali"

def wa(what=WHAT, tag=SLUG):
    t = f"Hi Suzu Travels, I want a quote for {what}. Travel date: ___ , people: ___ (page: {tag})"
    return "https://wa.me/917087488961?text=" + urllib.parse.quote(t, safe="")

def walink(label, what=WHAT, cls="sza-btn gold"):
    return f'<a class="{cls}" href="{wa(what)}" target="_blank" rel="noopener">{label}</a>'

MAIN = wa()

def card(src, w, h, alt, badge, title, meta, text, what, page=None, plabel="Explore →"):
    explore = f'<a class="x" href="{page}">{plabel}</a>' if page else ""
    return (f'<article class="sza-card"><div class="img"><img src="{src}" alt="{alt}" loading="lazy" width="{w}" height="{h}"><span class="sza-badge">{badge}</span></div>'
            f'<div class="body"><h3>{title}</h3><div class="meta">{meta}</div><p class="meta">{text}</p>'
            f'<div class="go"><a class="q" href="{wa(what)}" target="_blank" rel="noopener">Get Quote →</a>{explore}</div></div></article>')

cards = "".join([
    card(f"{U11}group-trekkers-forest-path-768x512.webp", 768, 512,
         "A group of hikers with backpacks walking up a rocky path through tall pine forest",
         "Most booked", "Lamadugh day hike", "<b>Old Manali → meadow → back · one full day</b>",
         "Up through deodar and pine forest, packed lunch on the meadow, and down to Manali by evening with a local guide.",
         "a Lamadugh day hike from Old Manali"),
    card(f"{U11}canvas-trek-tents-green-meadow-misty-mountains-768x512.webp", 768, 512,
         "Canvas trek tents on a green meadow below forested slopes and misty mountains",
         "Summer pick", "Lamadugh overnight camp", "<b>Night on the meadow · Apr–Nov only</b>",
         "Climb in the afternoon, a night in tents on the meadow and sunrise over the valley, then walk down next morning.",
         "a Lamadugh overnight camp (1 night)"),
    card(f"{U10}snow-laden-conifer-forest-winter-768x499.webp", 768, 499,
         "Conifer trees heavy with fresh snow in a winter forest",
         "Dec–Feb", "Winter snow hike (part way)", "<b>As far as the snow allows · guide only</b>",
         "In winter the upper trail is under snow. We go on clear days only and turn back by early afternoon, wherever we are.",
         "a winter snow hike on the Lamadugh trail"),
    card(f"{U10}trekkers-meadow-snow-peak-himalaya-768x1024.webp", 768, 1024,
         "Three trekkers with backpacks walking across a green meadow towards a snow-capped Himalayan peak",
         "Family pick", "Lamadugh + Jogini combo", "<b>Two easy Manali hikes on two days</b>",
         "Lamadugh one day, the shorter Jogini Waterfall walk from Vashisht the next — both from the same Manali hotel.",
         "Lamadugh and Jogini Waterfall hikes on one Manali trip", "/adventure/jogini-waterfall-trek/", "Jogini guide →"),
])

steps_exp = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Night before", "We check the weather and snow on the trail and register your group on the Kullu trekking portal."),
    ("8–9 am: meet your guide", "At your Old Manali or Manali hotel. Fill 2 litres of water each — there is none on the trail."),
    ("The climb", "Steady, often steep forest trail through deodar, pine and oak above Dhungri, with short rests."),
    ("Around 12–1 pm: the meadow", "Lunch on the open Lamadugh meadow with views across the upper Beas valley to the snow peaks."),
    ("Start down by 2 pm", "The descent is quicker but slippery — take it slowly, especially on wet or icy sections."),
    ("5–6 pm: back in Manali", "Cab back to your hotel if you stay outside Old Manali, or on to the rest of your trip."),
])

booking = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Tell us", "WhatsApp or the quote form — dates, group size, day hike or camp, and where you are staying."),
    ("We check your date", "Weather, snow on the upper trail and any Kullu district advisory."),
    ("You get one quote", "Guide, camp if you want it, hotel nights and cab in one plan."),
    ("Confirm and go", "We send the meeting point, start time and a packing list."),
])

season = [
    ("Dec – Feb", "Snow on the upper half of the trail", "Guide only, clear days only; you may turn back short of the meadow"),
    ("Mar – Apr", "Snow patches early, clearing by April", "Cold mornings, good views"),
    ("May – Jun", "Open", "Best weather and busiest; camping possible"),
    ("Jul – Aug", "Wet, slippery, leeches", "Not advised during heavy-rain alerts"),
    ("Sep – Nov", "Open and dry", "Clear skies; cold nights from late October"),
]
season_html = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in season)

faqs = [
    ("How long is the Lamadugh trek?", "About 6 km one way on the usual route from Old Manali. Most people take 4–6 hours up and 2–3 hours down, so plan a full day. Some operators count other routes and quote longer round-trip distances."),
    ("How high is Lamadugh?", "The meadow is at about 3,000 m (around 9,900 ft); the HP trekking portal lists 3,018 m. You climb roughly 950 m from Manali town."),
    ("Where does the Lamadugh trek start?", "From Old Manali or from the Dhungri / Hadimba forest above Manali. Both trails meet in the forest below the meadow; your guide picks the one that suits your hotel."),
    ("Can I do the Lamadugh trek in winter?", "From about December to February the upper trail is under snow. Go only with a local guide on a clear day and be ready to turn back. For a sure snow day, pick <a href=\"/adventure/sethan-valley-manali/\">Sethan</a> or <a href=\"/adventure/snow-activities-manali/\">snow activities in Manali</a>."),
    ("Is there water on the trail?", "No. Carry at least 2 litres each from Manali; there are no shops or taps on the way."),
    ("Do I need a permit for Lamadugh?", "There is no separate permit, but trekkers in Kullu district are asked to register on the HP trekking portal before they start. We do it for our guests."),
    ("Is Lamadugh good for beginners?", "Yes, if you are fit enough for a steep 5–6 hour climb. Young children and anyone with knee trouble should choose the shorter <a href=\"/adventure/jogini-waterfall-trek/\">Jogini Waterfall trek</a>."),
    ("Can we camp at Lamadugh?", "Yes, from about April to November, with a guide and tents arranged on request. There is no camping in the snow season. See also <a href=\"/adventure/camping-in-manali/\">camping in Manali</a>."),
    ("How much does the Lamadugh trek cost?", "Get Quote — the rate depends on day hike or camp, group size, private guide, winter gear, pick-up point, dates, and the hotel and cab you add. WhatsApp your dates and we reply with today's rate within minutes."),
]
faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)

more = [
    ("/adventure/trekking-in-manali/", "🥾", "Trekking in Manali", "All Manali treks"),
    ("/adventure/jogini-waterfall-trek/", "💧", "Jogini Waterfall trek", "Short walk from Vashisht"),
    ("/adventure/patalsu-peak-trek/", "⛰️", "Patalsu Peak trek", "Day summit near Solang"),
    ("/adventure/sethan-valley-manali/", "❄️", "Sethan valley", "Sure winter snow"),
    ("/adventure/camping-in-manali/", "⛺", "Camping in Manali", "Riverside and meadow camps"),
    ("/adventure/paragliding-in-manali/", "🪂", "Paragliding in Manali", "Tandem flights at Solang"),
]
more_html = "".join(f'<a class="sza-cat" href="{h}"><span class="ic">{i}</span><span class="n">{n}</span><span class="c">{c}</span></a>' for h, i, n, c in more)

reel = (HERE.parent / "media" / SLUG / "reel-section.html").read_text(encoding="utf-8").strip()

page = f'''<!-- lamadugh-trek — built by Page Builder (night) 23 Nov 2026 IST from the Research Lead brief 20 Nov (Project doc claude/adventure-research/briefs/lamadugh-trek.md) + Visual Studio night media @2355aad. Kit v2.0. No prices, no operator names. Hedged: one-way distance (about 6 km), winter reachability, sanctuary status (not stated). All photos are generic: neutral alt text, never captioned as Lamadugh. -->
<style>.sza-lmd .sza-hero-in>*{{max-width:620px}}@media(min-width:901px){{.sza-lmd .sza-hero-in>*{{max-width:min(560px,44vw)}}}}.sza-lmd .sza-chips{{max-width:700px}}.sza-lmd .sza-media ul{{padding-left:20px;list-style:disc;margin:0}}.sza-lmd .sza-media ul li{{margin:0 0 8px}}.sza-lmd .sza-media img{{height:auto;aspect-ratio:4/3;object-fit:cover}}.sza-lmd .sza-media video{{height:auto;aspect-ratio:16/9}}.sza-lmd #spots .sza-grid{{grid-template-columns:repeat(auto-fit,minmax(min(260px,100%),1fr))}}.sza-lmd #spots .sza-card .img img{{aspect-ratio:3/2;object-fit:cover}}.sza-lmd .sza-checks{{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}.sza-lmd .sza-choose{{margin-top:32px}}@media(min-width:1000px){{.sza-lmd #experience .sza-steps{{grid-template-columns:repeat(3,1fr)}}}}@media(max-width:820px){{.sza-lmd .sza-hero video{{object-position:20% 50%}}.sza-lmd .sza-hero:after{{background:linear-gradient(180deg,rgba(11,31,51,.45) 0%,rgba(11,31,51,.68) 45%,rgba(11,31,51,.95) 100%)}}}}</style>
<div class="sza sza-lmd">
<section class="sza-hero">
<video autoplay muted loop playsinline preload="metadata" poster="{U11}lamadugh-trek-hero-poster.webp" aria-label="Hikers on a forest path, a misty pine-forest trail, a hiker resting on a meadow below snow peaks and a snow-laden conifer forest, with a gold altitude line from Old Manali at about 2,050 m to the Lamadugh meadow at about 3,000 m"><source src="{CDN}hero.webm" type="video/webm"><source src="{CDN}hero.mp4" type="video/mp4"></video>
<div class="sza-hero-in">
<span class="sza-kicker">Treks &amp; Camps · Manali · Day hike</span>
<p class="sza-hero-tag">Forest climb to a high meadow above Manali</p>
<p class="sza-hero-sub">A full-day deodar-forest hike from Old Manali to the Lamadugh meadow, with a local guide, your hotel and cab in one quote.</p>
<ul class="sza-chips"><li><b>Meadow</b> ~3,000 m</li><li><b>Start</b> Old Manali</li><li><b>1 day</b> (5–8 hrs)</li><li><b>Easy–moderate</b></li><li><b>No water</b> on trail</li><li><b>Price</b> Get Quote</li></ul>
<div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan my trip</a></div>
<div class="sza-trust"><span><a href="https://suzutravels.com/certificates/">HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022</a></span><span>Guide + hotel + cab</span><span>Reply within minutes</span></div>
</div>
</section>
<nav class="sza-nav" aria-label="On this page"><div class="sza-nav-in"><a href="#overview">Overview</a><a href="#spots">Ways to do it</a><a href="#experience">How the day works</a><a href="#season">By month</a><a href="#safety">Rules &amp; safety</a><a href="#booking">How booking works</a><a href="#packages">Make it a trip</a><a href="#faq">FAQ</a><a class="cta" href="{MAIN}" target="_blank" rel="noopener">Get Quote</a></div></nav>

<section class="sza-sec" id="overview">
<span class="sza-kicker">Quick answer</span>
<h2>Lamadugh trek, at a glance</h2>
<p class="sza-answer">Lamadugh is a high meadow at about 3,000 m (9,900 ft) above Manali, reached on a steep forest trail from Old Manali in 4–6 hours up and 2–3 hours down. It is an easy-to-moderate day hike with views of the upper Beas valley and the snow peaks around it. Carry all your water, register on the Kullu trekking portal and start by 9 am.</p>
<div class="sza-facts"><div class="sza-fact"><div class="k">Where</div><div class="v">Above Old Manali and Dhungri, Kullu district — forest trail to an open meadow</div></div><div class="sza-fact"><div class="k">Height</div><div class="v">Meadow about 3,000 m (HP trekking portal: 3,018 m); about 950 m of climbing from Manali</div></div><div class="sza-fact"><div class="k">Distance &amp; time</div><div class="v">About 6 km one way; 4–6 hours up, 2–3 hours down</div></div><div class="sza-fact"><div class="k">Best time</div><div class="v">Apr–Jun and Sep–Nov; Dec–Feb snow on the upper trail — guide and clear day only</div></div><div class="sza-fact"><div class="k">Rules</div><div class="v">Register on the Kullu trekking portal; no plastic, no fires; back before dark</div></div><div class="sza-fact"><div class="k">Price</div><div class="v">Get Quote</div></div></div>
<div class="sza-media" style="margin-top:28px"><img src="{U11}trekker-resting-meadow-pine-forest-snow-peaks-768x512.webp" alt="A hiker in a red cap resting on a grassy slope with pine forest and snow-capped peaks behind" loading="lazy" width="768" height="512"><div><h3>Is Lamadugh for you?</h3><ul><li><b>One free day in Manali</b> → the classic day hike, back by evening.</li><li><b>Fit beginner</b> → yes, with a local guide; it is steep in places.</li><li><b>Small children or bad knees</b> → choose <a href="/adventure/jogini-waterfall-trek/">Jogini Waterfall</a> instead.</li><li><b>Want a night under the stars</b> → the meadow camp, April to November.</li></ul><p>Getting there: <a href="/cabs/delhi-to-manali-taxi/">Delhi to Manali taxi</a> or <a href="/cabs/chandigarh-to-manali-taxi/">Chandigarh to Manali taxi</a>. Check the <a href="/weather/manali/">Manali weather</a> before you pack, and see our <a href="/manali-itinerary/">Manali itinerary</a> for the rest of your days.</p></div></div>
</section>

<section class="sza-sec alt" id="spots">
<span class="sza-kicker">Ways to do it</span>
<h2>Four ways to do the Lamadugh trek</h2>
<p class="sza-lead">A day hike, a summer meadow camp, a winter snow walk, or two easy Manali hikes on one trip.</p>
<div class="sza-grid">{cards}</div>
<div class="sza-media sza-choose" id="route"><video autoplay muted loop playsinline preload="none" poster="{U11}lamadugh-trek-explainer-poster.webp" width="1600" height="900" aria-label="Day profile: 9 am start at Old Manali about 2,050 m, through deodar, pine and oak forest, around 1 pm at the meadow about 3,000 m, start down by 2 pm, back in Manali by 5 to 6 pm, with a no-water reminder and a month bar showing snow from December to February"><source src="{CDN}explainer.webm" type="video/webm"><source src="{CDN}explainer.mp4" type="video/mp4"></video><div><h3>Up to ~3,000 m and back</h3><ul><li><b>9 am · Old Manali</b> → about 2,050 m.</li><li><b>Deodar, pine &amp; oak forest</b> → steady climb, short rests.</li><li><b>~1 pm · Lamadugh meadow</b> → about 3,000 m; lunch with mountain views.</li><li><b>By 2 pm</b> → start down.</li><li><b>5–6 pm</b> → back in Manali.</li></ul><p>No water on the trail: carry 2 litres each. Times and heights are approximate.</p></div></div>
</section>

<section class="sza-sec" id="experience">
<span class="sza-kicker">How the day works</span>
<h2>A Lamadugh hike with Suzu, hour by hour</h2>
<ol class="sza-steps">{steps_exp}</ol>
<div class="sza-media"><img src="{U11}trekkers-misty-pine-forest-trail-768x512.webp" alt="Two hikers on a muddy trail through misty pine forest on a green hillside" loading="lazy" width="768" height="512"><div><h3>What to carry</h3><ul><li>2 litres of water each and a packed lunch</li><li>Shoes with good grip; microspikes in winter (arranged on request)</li><li>Warm layers and a rain shell, even in May</li><li>Sun cap, sunscreen and a small first-aid kit</li></ul><p>Polythene is banned in Himachal — take all your waste back down. Add a <a href="/adventure/paragliding-in-manali/">paragliding flight</a> or a <a href="/adventure/snow-activities-manali/">snow day</a> to the same trip.</p></div></div>
</section>

<section class="sza-sec alt" id="season">
<span class="sza-kicker">When to go</span>
<h2>Lamadugh trek by month</h2>
<div class="sza-scroll"><table class="sza-tbl"><thead><tr><th>Months</th><th>Trail</th><th>What to expect</th></tr></thead><tbody>{season_html}</tbody></table></div>
<div class="sza-media" style="margin-top:28px"><img src="{U10}snow-laden-conifer-forest-winter-768x499.webp" alt="Conifer trees heavy with fresh snow in a winter forest" loading="lazy" width="768" height="499"><div><h3>Going in winter?</h3><p>From about December to February the upper part of the trail is under snow. We go only on clear days with a local guide, start early and turn round by early afternoon — even if that is short of the meadow. After heavy snowfall the upper trail is not attempted.</p><p>Read our <a href="/adventure/winter-treks-in-himachal/">winter treks guide</a>, or see <a href="/manali-in-april/">Manali in April</a> for the spring thaw. For every trek in the state, see <a href="/adventure/trekking-in-himachal/">trekking in Himachal</a>.</p></div></div>
</section>

<div class="sza-band" id="safety"><div class="sza-band-in">
<span class="sza-kicker">Rules &amp; safety</span>
<h2>What we check before we book your hike</h2>
<p class="sza-lead">Suzu Travels is an <a href="https://suzutravels.com/certificates/" style="color:#f3d98f;text-decoration:underline">HP Tourism registered travel agent (Reg. No. DTO-MND-11-243/2022)</a>. We arrange the hike with registered local operators and plan around these checks:</p>
<ul class="sza-checks"><li><b>Register before you start</b>Kullu district asks every trekker to register on the HP trekking portal (trekking.hp.gov.in). We register our guests.</li><li><b>Weather and snow advisories</b>We follow Kullu district snow and weather advisories; after heavy snowfall the upper trail is not attempted.</li><li><b>Timing</b>Start by 9 am and turn round by 2 pm. No descents in the dark.</li><li><b>Water</b>There are no water points on the trail — 2 litres per person minimum.</li><li><b>Gear</b>Shoes with grip, warm layers; microspikes in winter, arranged on request.</li><li><b>Leave no trace</b>Polythene is banned in Himachal. No fires; carry all waste down.</li></ul>
</div></div>

<section class="sza-sec" id="booking">
<span class="sza-kicker">How booking works</span>
<h2>Get a quote in minutes</h2>
<ol class="sza-steps">{booking}</ol>
<div class="sza-media"><img src="{U11}group-trekkers-forest-path-768x512.webp" alt="A group of hikers with backpacks walking up a rocky path through tall pine forest" loading="lazy" width="768" height="512"><div><h3>What your quote depends on</h3><ul><li>Day hike or an overnight camp</li><li>Group size and whether you want a private guide</li><li>Winter extras: microspikes, snow boots, warm gear (arranged on request)</li><li>Pick-up point — Old Manali or a hotel further out</li><li>Season and dates</li><li>Hotel nights, cab and other Manali activities in the same trip</li></ul><p>We send today's rate on WhatsApp within minutes.</p></div></div>
</section>

{reel}

<section class="sza-quote"><div><span class="sza-kicker">Ready for a day above Manali?</span><h2>Get your Lamadugh trek quote</h2><p>Tell us your dates, group size and whether you want a day hike or a camp night. We reply with one plan — guide, hotel and cab — within minutes.</p></div><div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan full trip</a></div></section>

<section class="sza-sec" id="packages">
<span class="sza-kicker">Make it a trip</span>
<h2>Add Lamadugh to your Manali trip</h2>
<p>A good plan is Manali for 3 nights: one hike day (Lamadugh or <a href="/adventure/jogini-waterfall-trek/">Jogini</a>), one snow day at <a href="/adventure/sethan-valley-manali/">Sethan</a> or Solang, and one easy day in town — with the cab for the whole trip. Fit and want more? Try the <a href="/adventure/patalsu-peak-trek/">Patalsu Peak trek</a> or browse all <a href="/adventure/trekking-in-manali/">treks in Manali</a>.</p>
<div class="sza-btns" style="margin-top:18px">{walink("Manali 3 nights + Lamadugh hike — Get Quote", what="a 3-night Manali trip with the Lamadugh hike, a snow day, hotel and cab")}{walink("Lamadugh + Jogini — Get Quote", what="a Manali trip with the Lamadugh and Jogini Waterfall hikes", cls="sza-btn line")}</div>
</section>

<section class="sza-sec sza-faq" id="faq">
<span class="sza-kicker">FAQ</span>
<h2>Lamadugh trek — questions</h2>
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
