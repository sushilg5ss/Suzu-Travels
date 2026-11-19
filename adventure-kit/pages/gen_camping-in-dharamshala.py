#!/usr/bin/env python3
# Generates adventure-kit/pages/camping-in-dharamshala.html (Page Builder night, 20 Nov 2026 IST)
import urllib.parse, pathlib
SLUG = "camping-in-dharamshala"
HERE = pathlib.Path(__file__).resolve().parent
CDN = "https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@5426375addbcbc4f4cb4caa0982e65c0fac43cbf/adventure-kit/media/camping-in-dharamshala/"
U10 = "https://suzutravels.com/wp-content/uploads/2026/10/"
U11 = "https://suzutravels.com/wp-content/uploads/2026/11/"
QUOTE = "/himachal-tour-packages-quote/?activity=" + urllib.parse.quote("Camping in Dharamshala")
WHAT = "camping in Dharamshala"

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
    card(f"{U10}lit-canvas-tent-pine-forest-night-768x512.webp", 768, 512,
         "A glowing canvas bell tent among tall pine trees under a starry night sky",
         "Easy, drive-in", "Dharamkot &amp; Gallu Devi", "<b>Forest-edge camps · 2–4 km above McLeodganj</b>",
         "Drive-in camps on the forest edge with cafés close by. Gallu Devi is also where the Triund walk starts, so it suits a camp night before or after the trek.",
         "a drive-in camp at Dharamkot or Gallu Devi, Dharamshala"),
    card(f"{U10}lit-tents-meadow-campsite-dusk-768x512.webp", 768, 512,
         "Lit dome tents on a grassy campsite at dusk below a dark hill and a deep blue sky",
         "Families", "Naddi", "<b>Hillside camps · near the Naddi viewpoint</b>",
         "Hillside camps close to the Naddi viewpoint, with sunset on the Dhauladhar wall. No trekking needed — the easiest choice for families.",
         "a drive-in camp at Naddi, Dharamshala"),
    card(f"{U10}camping-tents-starry-night-sky-768x702.webp", 768, 702,
         "Row of small camping tents below a forested hill under a starry night sky with the Milky Way",
         "Most asked", "Triund ridge", "<b>About 2,850 m · ~9 km walk from McLeodganj</b>",
         "One night in the regulated tent area on the ridge after a 4–5 hour walk up. Daily numbers and tents are capped, and you register with ID at the Gallu check post.",
         "a Triund ridge camp night from McLeodganj", "/adventure/triund-trek/"),
    card(f"{U10}trek-tents-meadow-stream-valley-768x1024.webp", 768, 1024,
         "Row of orange trek tents on a green meadow beside a stream in a steep mountain valley under a blue cloudy sky",
         "Quieter", "Kareri Lake trail", "<b>River camp · lake at 2,934 m</b>",
         "Drive about 25 km to Kareri village, walk up along the stream to a riverside camp, and reach the lake the next morning. Fewer people than Triund.",
         "a Kareri Lake trek with a river camp", "/adventure/kareri-lake-trek/"),
    card(f"{U10}trekkers-meadow-snow-peak-himalaya-768x1024.webp", 768, 1024,
         "Three trekkers with backpacks walking across a green meadow towards a snow-capped Himalayan peak",
         "Expert", "Indrahar / Laka Got", "<b>Alpine camps past Triund · Indrahar Pass 4,342 m</b>",
         "High camps beyond Triund for fit, experienced trekkers — guided and in summer only. Not a camp night for beginners.",
         "an Indrahar Pass trek with alpine camps", "/adventure/indrahar-pass-trek/"),
])

steps_exp = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Tell us your plan", "Dates, group, ages, and whether you want a drive-in camp or a trek camp."),
    ("We check what is open", "Season, weather and the current Kangra district order (registration, winter limits) for your dates."),
    ("One quote", "Camp night(s), a guide if you trek, cab and your Dharamshala or McLeodganj hotel nights."),
    ("Reach the camp", "The cab drops you at the camp, near Gallu Devi for Triund, or at Kareri village for the lake."),
    ("Trek camps: register", "Show original ID at the check post; plastic and alcohol may be checked; carry your waste back down."),
    ("Evening and sunrise", "Camp evening, sunrise over the Kangra valley, then down — and on to Bir, Palampur or Dalhousie if you like."),
])

booking = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Tell us", "WhatsApp or the quote form — dates, group size, camp type and where you start from."),
    ("We check your date", "Which camps are open, the Kangra order for trek camps, and the weather."),
    ("You get one quote", "Camp, guide, hotel nights and cab in one plan."),
    ("Confirm and go", "We send the meeting point, check-in time and what to pack."),
])

season = [
    ("Mar–Jun", "Open; May–June busiest", "Open; book early for weekends — Triund tents are capped"),
    ("Jul–Aug (into Sep)", "Rain and leeches; some camps shut", "Slippery trail; Kangra monsoon registration order in force (8 Jul–15 Oct 2026) — usually best avoided"),
    ("Sep–Nov", "Open; clearest views", "Open — best season; cold nights from November"),
    ("Dec–Feb", "Cold; some camps stay open", "Snow up high. Past winter orders stopped or restricted trekking above 3,000 m — only if that winter's order allows, with a guide and snow gear"),
]
season_html = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in season)

faqs = [
    ("Can you camp at Triund?", "Yes, but only in the regulated tent area on the ridge, within a daily cap, after registering at the Gallu check post. We arrange it with a registered local operator — see our <a href=\"/adventure/triund-trek/\">Triund trek guide</a>."),
    ("Is camping allowed around Dharamshala in winter?", "Lower camps at Dharamkot and Naddi can run in winter. Triund and Kareri get snow, and Kangra issues winter orders that have restricted trekking above 3,000 m, so we check the order for your dates before we quote."),
    ("Where can we camp without trekking?", "At drive-in forest and hillside camps at Dharamkot, Gallu Devi and Naddi, about 2–4 km above McLeodganj."),
    ("What is included in a Dharamshala camp?", "Usually a tent with bedding or a sleeping bag, dinner and breakfast; trek camps add a guide. Bonfires only where the camp allows them."),
    ("Do we need to register for Triund or Kareri?", "Yes. Kangra made registration compulsory at 10 trek check posts, including Gallu temple, and you need original ID."),
    ("When is the best time to camp in Dharamshala?", "March to June and September to November. July–August brings heavy rain and leeches; December–February brings snow on the high camps."),
    ("Is it safe for families?", "Drive-in camps at Naddi or Dharamkot suit families. The Triund night needs a 4–5 hour uphill walk and suits fit teens and adults."),
    ("How much does camping in Dharamshala cost?", "Get Quote — the rate depends on the camp type, tent, nights, meals, guide, month, group size and the cab and hotel you add. WhatsApp your dates and we reply with today's rate within minutes."),
]
faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)

more = [
    ("/adventure/triund-trek/", "🏔️", "Triund trek", "The ridge camp above McLeodganj"),
    ("/adventure/kareri-lake-trek/", "🏞️", "Kareri Lake trek", "Lake at 2,934 m"),
    ("/adventure/paragliding-in-dharamshala/", "🪂", "Paragliding in Dharamshala", "Tandem flights at Indrunag"),
    ("/adventure/dharamshala-skyway/", "🚡", "Dharamshala Skyway", "Ropeway to McLeodganj"),
    ("/adventure/camping-in-bir-billing/", "⛺", "Camping in Bir Billing", "Village, ridge and Rajgundha"),
    ("/adventure/camping-in-himachal/", "🏕️", "Camping in Himachal", "Camp areas across the state"),
]
more_html = "".join(f'<a class="sza-cat" href="{h}"><span class="ic">{i}</span><span class="n">{n}</span><span class="c">{c}</span></a>' for h, i, n, c in more)

reel = (HERE.parent / "media" / SLUG / "reel-section.html").read_text(encoding="utf-8").strip()

page = f'''<!-- camping-in-dharamshala — built by Page Builder (night) 20 Nov 2026 IST from the Research Lead brief 19 Nov (Project doc claude/adventure-research/briefs/camping-in-dharamshala.md) + Visual Studio night media @5426375. Kit v2.0. No prices, no operator or camp names. Unverified items left off: current Triund fee amounts and caps, winter 2026-27 Kangra order, Gallu cut-off times, riverside camps near town. Generic camp photos carry neutral alt text. -->
<style>.sza-cdh .sza-hero-in>*{{max-width:620px}}@media(min-width:901px){{.sza-cdh .sza-hero-in>*{{max-width:min(560px,44vw)}}}}.sza-cdh .sza-chips{{max-width:700px}}.sza-cdh .sza-media ul{{padding-left:20px;list-style:disc;margin:0}}.sza-cdh .sza-media ul li{{margin:0 0 8px}}.sza-cdh .sza-media img{{height:auto;aspect-ratio:4/3;object-fit:cover}}.sza-cdh .sza-media video{{height:auto;aspect-ratio:16/9}}.sza-cdh #spots .sza-grid{{grid-template-columns:repeat(auto-fit,minmax(min(300px,100%),1fr))}}.sza-cdh #spots .sza-card .img img{{aspect-ratio:3/2;object-fit:cover}}.sza-cdh .sza-checks{{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}.sza-cdh .sza-choose{{margin-top:32px}}@media(min-width:1000px){{.sza-cdh #experience .sza-steps{{grid-template-columns:repeat(3,1fr)}}}}@media(max-width:820px){{.sza-cdh .sza-hero video{{object-position:20% 50%}}.sza-cdh .sza-hero:after{{background:linear-gradient(180deg,rgba(11,31,51,.45) 0%,rgba(11,31,51,.68) 45%,rgba(11,31,51,.95) 100%)}}}}</style>
<div class="sza sza-cdh">
<section class="sza-hero">
<video autoplay muted loop playsinline preload="metadata" poster="{U11}camping-in-dharamshala-hero-poster.webp" aria-label="Lit tents at dusk, the Dhauladhar range at sunset, a lit tent in a pine forest and dome tents at sunrise, with a gold tent outline and lantern; forest camps above McLeodganj, Triund ridge about 2,850 m, Kareri Lake trail 2,934 m, best March to June and September to November"><source src="{CDN}hero.webm" type="video/webm"><source src="{CDN}hero.mp4" type="video/mp4"></video>
<div class="sza-hero-in">
<span class="sza-kicker">Treks &amp; Camps · Dharamshala, Kangra</span>
<p class="sza-hero-tag">Tents under the Dhauladhar — from forest edges to the Triund ridge</p>
<p class="sza-hero-sub">Drive-in forest camps above McLeodganj, a regulated night on Triund, or a riverside camp on the Kareri trek. We pick the camp that's open for your dates and add hotel and cab.</p>
<ul class="sza-chips"><li><b>Dharamkot · Naddi</b> 2–4 km above McLeodganj</li><li><b>Triund</b> ~2,850 m</li><li><b>Kareri Lake</b> 2,934 m</li><li><b>Register</b> at Gallu</li><li><b>Best</b> Mar–Jun &amp; Sep–Nov</li><li><b>Price</b> Get Quote</li></ul>
<div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan my trip</a></div>
<div class="sza-trust"><span><a href="https://suzutravels.com/certificates/">HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022</a></span><span>Camp + hotel + cab</span><span>Reply within minutes</span></div>
</div>
</section>
<nav class="sza-nav" aria-label="On this page"><div class="sza-nav-in"><a href="#overview">Overview</a><a href="#spots">Where to camp</a><a href="#experience">How it works</a><a href="#season">By month</a><a href="#safety">Rules &amp; safety</a><a href="#booking">How booking works</a><a href="#packages">Make it a trip</a><a href="#faq">FAQ</a><a class="cta" href="{MAIN}" target="_blank" rel="noopener">Get Quote</a></div></nav>

<section class="sza-sec" id="overview">
<span class="sza-kicker">Quick answer</span>
<h2>Camping in Dharamshala, at a glance</h2>
<p class="sza-answer">Camping around Dharamshala happens in three kinds of places. Drive-in forest and hillside camps sit at Dharamkot, Naddi and the Bhagsu side, a few kilometres above McLeodganj. Trek camps sit on the Triund ridge (about 2,850 m, regulated tents only) and halfway up the Kareri Lake trail. Best months are March–June and September–November; in winter the high camps depend on Kangra district orders.</p>
<div class="sza-facts"><div class="sza-fact"><div class="k">Camp types</div><div class="v">Drive-in forest/hillside camps · Triund ridge tents (regulated) · Kareri riverside trek camp · Indrahar alpine camps (guided, summer)</div></div><div class="sza-fact"><div class="k">Where</div><div class="v">Dharamkot and Naddi 2–4 km above McLeodganj; Triund ~9 km walk; Kareri village ~25 km by road</div></div><div class="sza-fact"><div class="k">Rules</div><div class="v">Register with ID at Gallu (one of 10 Kangra trek check posts); forest entry and tent fee at the post; Triund numbers capped</div></div><div class="sza-fact"><div class="k">Season</div><div class="v">Mar–Jun and Sep–Nov; Jul–Aug monsoon; Dec–Feb snow on the high camps</div></div><div class="sza-fact"><div class="k">Usually included</div><div class="v">Tent with bedding or sleeping bag, dinner and breakfast; guide for trek camps</div></div><div class="sza-fact"><div class="k">Price</div><div class="v">Get Quote</div></div></div>
<div class="sza-media" style="margin-top:28px"><img src="{U10}dhauladhar-range-sunset-dharamshala-768x1020.webp" alt="Snow-capped Dhauladhar range catching the last sunlight above dark forested ridges, seen from the Dharamshala side, Himachal Pradesh" loading="lazy" width="768" height="1020"><div><h3>Which camp suits you?</h3><ul><li><b>No trekking, families, a first camp</b> → Naddi or Dharamkot drive-in camps.</li><li><b>One big night out</b> → the Triund ridge, after a 4–5 hour walk.</li><li><b>Quieter, lake views</b> → the Kareri Lake trail with a river camp.</li><li><b>Fit and experienced</b> → Indrahar alpine camps, guided, summer only.</li></ul><p>Getting there: <a href="/cabs/delhi-to-dharamshala-taxi/">Delhi to Dharamshala taxi</a>, <a href="/cabs/chandigarh-to-dharamshala-taxi/">Chandigarh to Dharamshala taxi</a> or <a href="/cabs/pathankot-to-dharamshala-taxi/">Pathankot to Dharamshala taxi</a>. Check the <a href="/weather/dharamshala/">Dharamshala weather</a> before you pack.</p></div></div>
</section>

<section class="sza-sec alt" id="spots">
<span class="sza-kicker">Where to camp</span>
<h2>Five places to camp around Dharamshala and McLeodganj</h2>
<p class="sza-lead">Two drive-in camp areas and three trek camps. Pick by your group and your month.</p>
<div class="sza-grid">{cards}</div>
<div class="sza-media sza-choose" id="camp-map"><video autoplay muted loop playsinline preload="none" poster="{U11}camping-in-dharamshala-explainer-poster.webp" width="1600" height="900" aria-label="Schematic of where you can camp: McLeodganj, Dharamkot and Naddi drive-in camps 2 to 4 km above, Gallu Devi check post, Triund ridge about 2,850 m, Indrahar Pass 4,342 m guided in summer, and a side route to Kareri village, a river camp and Kareri Lake 2,934 m, with a month-by-month season strip"><source src="{CDN}explainer.webm" type="video/webm"><source src="{CDN}explainer.mp4" type="video/mp4"></video><div><h3>Where you can camp, by height</h3><ul><li><b>Dharamkot · Naddi</b> → drive-in, 2–4 km above McLeodganj.</li><li><b>Gallu Devi</b> → check post: register with original ID.</li><li><b>Triund ridge</b> → about 2,850 m, ~9 km, regulated tents.</li><li><b>Kareri Lake</b> → 2,934 m, ~25 km road to Kareri village, then the trail.</li></ul><p>Heights and distances are approximate. Kangra district orders decide when the trek camps are open.</p></div></div>
</section>

<section class="sza-sec" id="experience">
<span class="sza-kicker">How it works</span>
<h2>How a Dharamshala camp night works with Suzu</h2>
<ol class="sza-steps">{steps_exp}</ol>
<div class="sza-media"><img src="{U10}friends-campfire-hillside-sunset-768x1152.webp" alt="Group of friends in warm jackets sitting around a campfire on a hillside under a golden sunset sky" loading="lazy" width="768" height="1152"><div><h3>What a camp night looks like</h3><p>A tent with bedding or a sleeping bag, dinner and breakfast, and a bonfire only where the camp is allowed one. Add a <a href="/adventure/paragliding-in-dharamshala/">tandem paragliding flight</a> or a ride on the <a href="/adventure/dharamshala-skyway/">Dharamshala Skyway</a> to the same trip.</p><p>Carry a headlamp, a rain shell and warm layers even in May. Take all your waste back down.</p></div></div>
</section>

<section class="sza-sec alt" id="season">
<span class="sza-kicker">When to go</span>
<h2>Camping in Dharamshala by month</h2>
<div class="sza-scroll"><table class="sza-tbl"><thead><tr><th>Months</th><th>Drive-in camps (Dharamkot, Naddi)</th><th>Triund / Kareri trek camps</th></tr></thead><tbody>{season_html}</tbody></table></div>
<p style="margin-top:14px">Going in winter? Read our <a href="/adventure/winter-treks-in-himachal/">winter treks guide</a> and plan a drive-in camp unless the Kangra order allows the high camps. For every trek in the state, see <a href="/adventure/trekking-in-himachal/">trekking in Himachal</a>.</p>
</section>

<div class="sza-band" id="safety"><div class="sza-band-in">
<span class="sza-kicker">Rules &amp; safety</span>
<h2>What we check before we book your camp</h2>
<p class="sza-lead">Suzu Travels is an <a href="https://suzutravels.com/certificates/" style="color:#f3d98f;text-decoration:underline">HP Tourism registered travel agent (Reg. No. DTO-MND-11-243/2022)</a>. We arrange camps with registered local operators and plan around these checks:</p>
<ul class="sza-checks"><li><b>Registration</b>Kangra district orders under the Disaster Management Act made registration compulsory at 10 trek check posts, including Gallu temple. Trekking without it can invite legal action.</li><li><b>Winter orders</b>Past winter orders (November 2024 and 2025) needed permission for Triund and Kareri and stopped trekking above 3,000 m. Expect a fresh order each winter — we check it before quoting.</li><li><b>Triund is regulated</b>Limited trekkers per day and a capped number of tents, camping only in the marked area, through a registered local operator. No self-pitching.</li><li><b>Fire</b>A forest fire on the Triund route in January 2026 put the area on alert. No fires or smoking on trails; bonfires only where the camp allows them.</li><li><b>Turn back</b>Carry a headlamp, rain shell and warm layers; turn back if cloud builds or the last steep bends are icy.</li><li><b>Leave no trace</b>No alcohol on trails; carry back all waste — plastic may be checked at the post.</li></ul>
</div></div>

<section class="sza-sec" id="booking">
<span class="sza-kicker">How booking works</span>
<h2>Get a quote in minutes</h2>
<ol class="sza-steps">{booking}</ol>
<div class="sza-media"><img src="{U10}dome-tents-hilltop-meadow-sunrise-768x498.webp" alt="Red, blue and orange dome tents on a grassy hilltop meadow at sunrise, with layered blue mountain ridges behind" loading="lazy" width="768" height="498"><div><h3>What your quote depends on</h3><ul><li>Camp type — drive-in camp, Triund ridge night or Kareri river camp</li><li>Tent type — alpine, Swiss/dome, or glamping with attached bath</li><li>Nights, group size, weekday or weekend, and season (May–June and long weekends peak)</li><li>Meals, guide or porter for trek camps, forest entry and tent fees at the check post</li><li>Cab from Pathankot, Gaggal, Chandigarh or Delhi; drop near Gallu Devi or Kareri village</li><li>Hotel nights in Dharamshala or McLeodganj; add-ons like paragliding or the Skyway</li></ul><p>We send today's rate on WhatsApp within minutes.</p></div></div>
</section>

{reel}

<section class="sza-quote"><div><span class="sza-kicker">Ready for a night under the Dhauladhar?</span><h2>Get your Dharamshala camping quote</h2><p>Tell us your dates, group size and the kind of camp you want. We reply with one plan — camp, guide, hotel and cab — within minutes.</p></div><div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan full trip</a></div></section>

<section class="sza-sec" id="packages">
<span class="sza-kicker">Make it a trip</span>
<h2>Add a camp night to your Dharamshala trip</h2>
<p>Most guests add one camp night to a <a href="/mcleodganj-tour-package/">McLeodganj tour package</a> or a <a href="/destination/dharamshala-tour-packages/">Dharamshala tour package</a>, or pair it with Dalhousie on a <a href="/dharamshala-dalhousie-tour-package/">Dharamshala–Dalhousie trip</a>. Bir is two hours away — see <a href="/adventure/camping-in-bir-billing/">camping in Bir Billing</a> for a camping weekend that takes in both. For every camp area in the state, see <a href="/adventure/camping-in-himachal/">camping in Himachal</a>.</p>
<div class="sza-btns" style="margin-top:18px">{walink("Camp + McLeodganj 3 nights — Get Quote", what="a Dharamshala–McLeodganj trip with one camp night, hotel and cab")}{walink("Bir + Dharamshala camping weekend — Get Quote", what="a Bir and Dharamshala camping weekend", cls="sza-btn line")}</div>
</section>

<section class="sza-sec sza-faq" id="faq">
<span class="sza-kicker">FAQ</span>
<h2>Camping in Dharamshala — questions</h2>
{faq_html}
</section>

<section class="sza-sec alt" id="more">
<span class="sza-kicker">More adventures</span>
<h2>Explore more around Dharamshala and Kangra</h2>
<div class="sza-cats">{more_html}</div>
</section>
</div>
'''
out = HERE / f"{SLUG}.html"
out.write_text(page, encoding="utf-8")
print(len(page))
