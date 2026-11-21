#!/usr/bin/env python3
# Generates adventure-kit/pages/thatharana-trek.html (Page Builder night, 22 Nov 2026 IST)
import urllib.parse, pathlib
SLUG = "thatharana-trek"
HERE = pathlib.Path(__file__).resolve().parent
CDN = "https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@3b9a425e6625d7178b38b981795baf4453f6aa7a/adventure-kit/media/thatharana-trek/"
U10 = "https://suzutravels.com/wp-content/uploads/2026/10/"
U11 = "https://suzutravels.com/wp-content/uploads/2026/11/"
QUOTE = "/himachal-tour-packages-quote/?activity=" + urllib.parse.quote("Thatharana trek")
WHAT = "the Thatharana trek near Dharamshala"

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
    card(f"{U10}hikers-on-forest-trail-trek-768x1150.webp", 768, 1150,
         "Hikers with backpacks walking up a forest trail between tall trees",
         "Fit walkers", "Thatharana day hike", "<b>Khadota → Top → Khadota · 6–8 hrs return</b>",
         "Up and back in one long day. Start from Khadota by 8–9 am so you are off the upper trail well before dark.",
         "a Thatharana day hike from Khadota"),
    card(f"{U10}dome-tents-hilltop-meadow-sunrise-768x498.webp", 768, 498,
         "Red, blue and orange dome tents on a grassy hilltop meadow at sunrise, with layered blue mountain ridges behind",
         "Classic pick", "Thatharana camp (1N/2D)", "<b>Climb after lunch · night on the meadow · down by ~1 pm</b>",
         "Walk up in the afternoon, sunset and a night on the meadow, sunrise over the Kangra valley, then down to Khadota by lunch.",
         "a Thatharana camp trek (1 night / 2 days)"),
    card(f"{U10}dhauladhar-range-sunset-dharamshala-768x1020.webp", 768, 1020,
         "Snow-capped Dhauladhar range catching the last sunlight above dark forested ridges, seen from the Dharamshala side",
         "Two ridges", "Triund + Thatharana", "<b>Two Dhauladhar treks from one Dharamshala hotel</b>",
         "Triund is easier and busier; Thatharana is quieter and steeper. Do one each day, or one this trip and one the next.",
         "Triund and Thatharana treks on one Dharamshala trip", "/adventure/triund-trek/", "Triund guide →"),
    card(f"{U10}trekkers-meadow-snow-peak-himalaya-768x1024.webp", 768, 1024,
         "Three trekkers with backpacks walking across a green meadow towards a snow-capped Himalayan peak",
         "Summer only", "Kundli Pass (expert)", "<b>Beyond Thatharana · well above 3,000 m</b>",
         "Thatharana is the base for Kundli Pass, an expert crossing for fit, experienced trekkers with a guide. Summer windows only; Kangra's winter orders apply above 3,000 m.",
         "a Kundli Pass trek via Thatharana"),
])

steps_exp = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Tell us your plan", "WhatsApp your dates, group size and fitness. We check the Kangra district order and the weather for that date."),
    ("Cab to Khadota", "From your Dharamshala or McLeodganj hotel to Khaniyara and up to the Khadota road-head."),
    ("Register at the check post", "Show original ID at the Khadota check post and meet your local trek lead."),
    ("The climb", "3–5 hours up through oak and rhododendron forest. Packed lunch on the way; carry 2 litres of water each."),
    ("Night on the meadow", "Tent, bedding, dinner and breakfast are arranged on request — or turn back the same day."),
    ("Down and onward", "Walk down to Khadota by lunch; the cab takes you back to your hotel or on to your next Himachal stop."),
])

booking = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Tell us", "WhatsApp or the quote form — dates, group size, day hike or camp, and where you start from."),
    ("We check your date", "The Kangra order in force, weather and whether the upper trail is clear."),
    ("You get one quote", "Trek lead, camp, hotel nights and cab in one plan."),
    ("Confirm and go", "We send the meeting point at Khadota, start time and a packing list."),
])

season = [
    ("Mar – Jun", "Dry trail; rhododendrons in Mar–Apr; warm days", "Best"),
    ("Jul – Aug", "Monsoon: slippery forest, low cloud, landslide risk", "Avoid"),
    ("Sep – Nov", "Clear post-monsoon views; cold nights from November", "Best"),
    ("Dec – Feb", "Snow on the upper trail. The Top is below 3,000 m, but any IMD alert or district order can stop treks", "Clear-weather days only, with a local lead"),
]
season_html = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in season)

faqs = [
    ("Where does the Thatharana trek start?", "At Khadota (also spelt Kharota) village, about 2 km above Khaniyara, which is about 8 km from Dharamshala. Some operators count from Khaniyara market, which adds 1–2 hours of walking."),
    ("How long is the Thatharana trek?", "About 5–7 km one way from Khadota: 3–5 hours up and 2–3 hours down. Operators who start at Khaniyara quote 12–18 km for the round trip."),
    ("What is the height of Thatharana Top?", "Roughly 2,500–2,750 m (about 8,200–9,000 ft); sources differ and operators usually say about 8,500 ft. It is lower than the Triund ridge but feels steeper."),
    ("Is Thatharana harder than Triund?", "Slightly, yes — shorter, but steeper all the way and less clearly marked. Fit beginners manage it with a local trek lead."),
    ("Do I need a permit for Thatharana?", "There is no separate permit, but you must register with original ID at the Khadota check post, one of Kangra's notified trek entry points. Fees, if any, are paid locally."),
    ("Can I camp at Thatharana Top?", "Yes. One-night camps on the meadow, with tents, dinner and breakfast, are arranged through a registered local operator — not wild camping. See also <a href=\"/adventure/camping-in-dharamshala/\">camping in Dharamshala</a>."),
    ("Is the Thatharana trek open in winter?", "The Top is below Kangra's 3,000 m winter limit, so it can open on clear days, but snow on the upper trail or an IMD alert can stop it. We confirm the order in force for your date before we quote — see our <a href=\"/adventure/winter-treks-in-himachal/\">winter treks guide</a>."),
    ("Thatharana or Triund — which should I do?", "Triund is easier, busier and has capped tents; Thatharana is quieter, with wide Kangra-valley views. Many guests do both on one Dharamshala trip — see the <a href=\"/adventure/triund-trek/\">Triund trek guide</a>."),
    ("How much does the Thatharana trek cost?", "Get Quote — the rate depends on day hike or camp, group size, dates, tents and meals, trek lead, and the cab and hotel you add. WhatsApp your dates and we reply with today's rate within minutes."),
]
faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)

more = [
    ("/adventure/triund-trek/", "🏔️", "Triund trek", "The classic ridge above McLeodganj"),
    ("/adventure/kareri-lake-trek/", "🏞️", "Kareri Lake trek", "Lake at 2,934 m"),
    ("/adventure/indrahar-pass-trek/", "⛰️", "Indrahar Pass trek", "Expert crossing, summer"),
    ("/adventure/camping-in-dharamshala/", "⛺", "Camping in Dharamshala", "Forest and ridge camps"),
    ("/adventure/paragliding-in-dharamshala/", "🪂", "Paragliding in Dharamshala", "Tandem flights at Indrunag"),
    ("/adventure/dharamshala-skyway/", "🚡", "Dharamshala Skyway", "Ropeway to McLeodganj"),
]
more_html = "".join(f'<a class="sza-cat" href="{h}"><span class="ic">{i}</span><span class="n">{n}</span><span class="c">{c}</span></a>' for h, i, n, c in more)

reel = (HERE.parent / "media" / SLUG / "reel-section.html").read_text(encoding="utf-8").strip()

page = f'''<!-- thatharana-trek — built by Page Builder (night) 22 Nov 2026 IST from the Research Lead brief 21 Nov (Project doc claude/adventure-research/briefs/thatharana-trek.md) + Visual Studio morning media @3b9a425. Kit v2.0. No prices, no operator names. Hedged: Top altitude (range), forest fee (if any), winter 2026-27 Kangra order, Kundli Pass height (not stated). Generic photos carry neutral alt text. -->
<style>.sza-tht .sza-hero-in>*{{max-width:620px}}@media(min-width:901px){{.sza-tht .sza-hero-in>*{{max-width:min(560px,44vw)}}}}.sza-tht .sza-chips{{max-width:700px}}.sza-tht .sza-media ul{{padding-left:20px;list-style:disc;margin:0}}.sza-tht .sza-media ul li{{margin:0 0 8px}}.sza-tht .sza-media img{{height:auto;aspect-ratio:4/3;object-fit:cover}}.sza-tht .sza-media video{{height:auto;aspect-ratio:16/9}}.sza-tht #spots .sza-grid{{grid-template-columns:repeat(auto-fit,minmax(min(260px,100%),1fr))}}.sza-tht #spots .sza-card .img img{{aspect-ratio:3/2;object-fit:cover}}.sza-tht .sza-checks{{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}.sza-tht .sza-choose{{margin-top:32px}}@media(min-width:1000px){{.sza-tht #experience .sza-steps{{grid-template-columns:repeat(3,1fr)}}}}@media(max-width:820px){{.sza-tht .sza-hero video{{object-position:20% 50%}}.sza-tht .sza-hero:after{{background:linear-gradient(180deg,rgba(11,31,51,.45) 0%,rgba(11,31,51,.68) 45%,rgba(11,31,51,.95) 100%)}}}}</style>
<div class="sza sza-tht">
<section class="sza-hero">
<video autoplay muted loop playsinline preload="metadata" poster="{U11}thatharana-trek-hero-poster.webp" aria-label="Dhauladhar snow peaks from Dharamshala, hikers on a forest trail, dome tents on a meadow at sunrise and lit tents at dusk, with a gold altitude line from Khaniyara past the Khadota check post to Thatharana Top at about 2,500 to 2,750 m"><source src="{CDN}hero.webm" type="video/webm"><source src="{CDN}hero.mp4" type="video/mp4"></video>
<div class="sza-hero-in">
<span class="sza-kicker">Treks &amp; Camps · Dharamshala, Kangra</span>
<p class="sza-hero-tag">The quieter Triund — a forest climb to a Dhauladhar meadow</p>
<p class="sza-hero-sub">Start at Khadota above Khaniyara, camp on Thatharana Top, walk down next morning. We plan it with a registered local operator and add your Dharamshala hotel and cab.</p>
<ul class="sza-chips"><li><b>Top</b> ~2,500–2,750 m</li><li><b>~5–7 km</b> one way</li><li><b>3–5 hrs</b> up</li><li><b>Register</b> at Khadota</li><li><b>Best</b> Mar–Jun &amp; Sep–Nov</li><li><b>Price</b> Get Quote</li></ul>
<div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan my trip</a></div>
<div class="sza-trust"><span><a href="https://suzutravels.com/certificates/">HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022</a></span><span>Trek + camp + hotel + cab</span><span>Reply within minutes</span></div>
</div>
</section>
<nav class="sza-nav" aria-label="On this page"><div class="sza-nav-in"><a href="#overview">Overview</a><a href="#spots">Ways to do it</a><a href="#experience">How it works</a><a href="#season">By month</a><a href="#safety">Rules &amp; safety</a><a href="#booking">How booking works</a><a href="#packages">Make it a trip</a><a href="#faq">FAQ</a><a class="cta" href="{MAIN}" target="_blank" rel="noopener">Get Quote</a></div></nav>

<section class="sza-sec" id="overview">
<span class="sza-kicker">Quick answer</span>
<h2>Thatharana trek, at a glance</h2>
<p class="sza-answer">Thatharana (Thatharna) Top is a meadow at about 2,500–2,750 m on the Dhauladhar slope above Dharamshala. The trail starts at Khadota (Kharota) village, about 2 km above Khaniyara, and climbs 5–7 km through forest in 3–5 hours. Most people camp one night and come down the next morning. Register at the Khadota check post; the best months are March–June and September–November.</p>
<div class="sza-facts"><div class="sza-fact"><div class="k">Height</div><div class="v">Thatharana Top about 2,500–2,750 m (sources differ)</div></div><div class="sza-fact"><div class="k">Start</div><div class="v">Khadota / Kharota village, ~2 km above Khaniyara (~8 km from Dharamshala)</div></div><div class="sza-fact"><div class="k">Distance &amp; time</div><div class="v">~5–7 km one way, 3–5 hours up; steeper and less marked than Triund</div></div><div class="sza-fact"><div class="k">Entry</div><div class="v">Register with original ID at the Khadota check post (Kangra district order)</div></div><div class="sza-fact"><div class="k">Best time</div><div class="v">Mar–Jun and Sep–Nov; Jul–Aug monsoon; Dec–Feb snow on the upper trail</div></div><div class="sza-fact"><div class="k">Price</div><div class="v">Get Quote</div></div></div>
<div class="sza-media" style="margin-top:28px"><img src="{U10}dhauladhar-snow-peaks-from-dharamshala-golden-light-768x576.webp" alt="Snow-covered Dhauladhar peaks in golden light above forested slopes, seen from Dharamshala, Himachal Pradesh" loading="lazy" width="768" height="576"><div><h3>Is Thatharana for you?</h3><ul><li><b>You liked the idea of Triund but not the crowds</b> → Thatharana is quieter.</li><li><b>Fit beginner</b> → yes, with a local trek lead; it is steep all the way.</li><li><b>Short on time</b> → do it as a long day hike from Khadota.</li><li><b>Want the night sky</b> → the 1-night meadow camp.</li></ul><p>Getting there: <a href="/cabs/delhi-to-dharamshala-taxi/">Delhi to Dharamshala taxi</a> or <a href="/cabs/pathankot-to-dharamshala-taxi/">Pathankot to Dharamshala taxi</a>. Check the <a href="/weather/dharamshala/">Dharamshala weather</a> before you pack, and see our <a href="/dharamshala-itinerary/">Dharamshala itinerary</a> for the rest of your days.</p></div></div>
</section>

<section class="sza-sec alt" id="spots">
<span class="sza-kicker">Ways to do it</span>
<h2>Four ways to do the Thatharana trek</h2>
<p class="sza-lead">A long day hike, the classic meadow camp, a two-ridge Dharamshala trip, or Kundli Pass for experts.</p>
<div class="sza-grid">{cards}</div>
<div class="sza-media sza-choose" id="route"><video autoplay muted loop playsinline preload="none" poster="{U11}thatharana-trek-explainer-poster.webp" width="1600" height="900" aria-label="Route profile: Khaniyara about 1,300 m, Khadota check post where you register with ID, oak and rhododendron forest, Thatharana Top about 2,500 to 2,750 m with one night in camp, and a dashed summer-only line to Kundli Pass, with a 12-month season strip"><source src="{CDN}explainer.webm" type="video/webm"><source src="{CDN}explainer.mp4" type="video/mp4"></video><div><h3>The route, step by step</h3><ul><li><b>Khaniyara</b> → about 1,300 m, ~8 km from Dharamshala.</li><li><b>Khadota check post</b> → register with original ID.</li><li><b>Oak &amp; rhododendron forest</b> → 3–5 hours up; carry 2 litres of water.</li><li><b>Thatharana Top</b> → about 2,500–2,750 m; camp one night.</li><li><b>Kundli Pass</b> → beyond, summer only, experts with a guide.</li></ul><p>Heights and distances are approximate.</p></div></div>
</section>

<section class="sza-sec" id="experience">
<span class="sza-kicker">How it works</span>
<h2>How a Thatharana trek works with Suzu</h2>
<ol class="sza-steps">{steps_exp}</ol>
<div class="sza-media"><img src="{U10}lit-tents-meadow-campsite-dusk-768x512.webp" alt="Lit dome tents on a grassy campsite at dusk below a dark hill and a deep blue sky" loading="lazy" width="768" height="512"><div><h3>What the camp night looks like</h3><p>A tent with bedding or a sleeping bag, dinner and breakfast, and sunrise over the Kangra valley. Add a <a href="/adventure/paragliding-in-dharamshala/">tandem paragliding flight</a> or the <a href="/adventure/dharamshala-skyway/">Dharamshala Skyway</a> to the same trip.</p><p>Carry a headlamp, a rain shell and warm layers even in May. Take all your waste back down.</p></div></div>
</section>

<section class="sza-sec alt" id="season">
<span class="sza-kicker">When to go</span>
<h2>Thatharana trek by month</h2>
<div class="sza-scroll"><table class="sza-tbl"><thead><tr><th>Months</th><th>Trail</th><th>Verdict</th></tr></thead><tbody>{season_html}</tbody></table></div>
<div class="sza-media" style="margin-top:28px"><img src="{U10}snow-laden-conifer-forest-winter-768x499.webp" alt="Conifer trees heavy with fresh snow in a winter forest" loading="lazy" width="768" height="499"><div><h3>Going in winter?</h3><p>Snow can lie on the upper trail from December to February. Thatharana Top is below the 3,000 m line used in past Kangra winter orders, but Kundli Pass beyond it is not, and any IMD alert can stop treks. We check the order in force for your date.</p><p>Read our <a href="/adventure/winter-treks-in-himachal/">winter treks guide</a>, and for every trek in the state see <a href="/adventure/trekking-in-himachal/">trekking in Himachal</a>.</p></div></div>
</section>

<div class="sza-band" id="safety"><div class="sza-band-in">
<span class="sza-kicker">Rules &amp; safety</span>
<h2>What we check before we book your trek</h2>
<p class="sza-lead">Suzu Travels is an <a href="https://suzutravels.com/certificates/" style="color:#f3d98f;text-decoration:underline">HP Tourism registered travel agent (Reg. No. DTO-MND-11-243/2022)</a>. We arrange the trek with registered local operators and plan around these checks:</p>
<ul class="sza-checks"><li><b>Registration at Khadota</b>Khadota village is one of the 10 trek entry check posts notified by Kangra district in November 2025. Trekking these routes without registering is barred under the Disaster Management Act.</li><li><b>The 3,000 m winter rule</b>Kangra orders in November 2024 and January 2026 banned trekking above 3,000 m in winter. Thatharana Top is below that line, Kundli Pass is not — we check the order in force for your date.</li><li><b>Groups and guides</b>Kangra has asked that all trekkers register and that guides take no more than 10 trekkers per group.</li><li><b>Trail</b>Parts of the forest trail are unmarked — go with a local lead, start before about 11 am and carry a headlamp.</li><li><b>Water and snow</b>Water sources on the way are few: carry 2 litres each. In Dec–Feb use microspikes or turn back if the top section is icy.</li><li><b>Network</b>Mobile signal is patchy above Khadota; share your plan with your hotel.</li></ul>
</div></div>

<section class="sza-sec" id="booking">
<span class="sza-kicker">How booking works</span>
<h2>Get a quote in minutes</h2>
<ol class="sza-steps">{booking}</ol>
<div class="sza-media"><img src="{U10}dhauladhar-range-sunset-dharamshala-768x1020.webp" alt="Snow-capped Dhauladhar range catching the last sunlight above dark forested ridges, seen from the Dharamshala side" loading="lazy" width="768" height="1020"><div><h3>What your quote depends on</h3><ul><li>Day hike or a 1-night camp</li><li>Group size and dates — weekends and May–June fill fast</li><li>Tent type, meals and sleeping bags</li><li>Local trek lead or porter</li><li>Cab from your hotel to Khadota and back (Dharamshala, McLeodganj, Bir or Pathankot pickup)</li><li>Hotel nights in Dharamshala and the rest of your Himachal trip</li></ul><p>We send today's rate on WhatsApp within minutes.</p></div></div>
</section>

{reel}

<section class="sza-quote"><div><span class="sza-kicker">Ready for a quieter Dhauladhar trek?</span><h2>Get your Thatharana trek quote</h2><p>Tell us your dates, group size and whether you want a day hike or a camp night. We reply with one plan — trek lead, camp, hotel and cab — within minutes.</p></div><div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan full trip</a></div></section>

<section class="sza-sec" id="packages">
<span class="sza-kicker">Make it a trip</span>
<h2>Add Thatharana to your Dharamshala trip</h2>
<p>Most guests add the Thatharana camp night to a <a href="/mcleodganj-tour-package/">McLeodganj tour package</a> or a <a href="/destination/dharamshala-tour-packages/">Dharamshala tour package</a>. Bir is about two hours away — add a <a href="/adventure/paragliding-in-bir-billing/">paragliding day in Bir Billing</a>. For more of the valley, see <a href="/kangra-tourist-places/">Kangra tourist places</a>.</p>
<div class="sza-btns" style="margin-top:18px">{walink("McLeodganj 3 nights + Thatharana camp — Get Quote", what="a McLeodganj–Dharamshala trip with a Thatharana camp night, hotel and cab")}{walink("Thatharana + Bir paragliding — Get Quote", what="a Dharamshala trip with the Thatharana trek and a Bir Billing paragliding day", cls="sza-btn line")}</div>
</section>

<section class="sza-sec sza-faq" id="faq">
<span class="sza-kicker">FAQ</span>
<h2>Thatharana trek — questions</h2>
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
