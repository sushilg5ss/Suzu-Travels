#!/usr/bin/env python3
# Generates adventure-kit/pages/hampta-pass-trek.html (Page Builder night, 17 Oct 2026)
import urllib.parse, pathlib
SLUG = "hampta-pass-trek"
HERE = pathlib.Path(__file__).resolve().parent
CDN = "https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@220d56f424bc1f602fd7a5e0b3b43352ae933618/adventure-kit/media/hampta-pass-trek/"
UP = "https://suzutravels.com/wp-content/uploads/2026/10/"
QUOTE = "/himachal-tour-packages-quote/?activity=" + urllib.parse.quote("Hampta Pass trek")

def wa(what="the Hampta Pass trek from Manali", tag=SLUG):
    t = f"Hi Suzu Travels, I want a quote for {what}. Travel date: ___ , people: ___ (page: {tag})"
    return "https://wa.me/917087488961?text=" + urllib.parse.quote(t, safe="")

def walink(label, what="the Hampta Pass trek from Manali", cls="sza-btn gold"):
    return f'<a class="{cls}" href="{wa(what)}" target="_blank" rel="noopener">{label}</a>'

MAIN = wa()

def card(src, w, h, alt, badge, title, meta, text, what, extra=""):
    return (f'<article class="sza-card"><div class="img"><img src="{src}" alt="{alt}" loading="lazy" width="{w}" height="{h}"><span class="sza-badge">{badge}</span></div>'
            f'<div class="body"><h3>{title}</h3><div class="meta">{meta}</div><p class="meta">{text}</p>'
            f'<div class="go">{extra}<a class="q" href="{wa(what)}" target="_blank" rel="noopener">Get Quote →</a></div></div></article>')

cards = "".join([
    card(f"{UP}trekkers-snowfield-high-pass-768x576.webp", 768, 576,
         "Small group of trekkers in red jackets and gaiters walking across a snowfield below rocky, snow-streaked peaks",
         "Classic pick", "Classic Hampta (4 days)", "<b>Jobra → Chhatru, ~26 km</b>",
         "Cross the pass on day 3, get picked up at Chhatru and drive back to Manali through the Atal Tunnel.",
         "the classic 4-day Hampta Pass trek"),
    card(f"{UP}high-valley-braided-river-glaciers-768x516.webp", 768, 516,
         "Wide high-altitude valley with a braided river winding between steep rock walls toward glaciated peaks",
         "With Chandratal", "Hampta + Chandratal (5 days)", "<b>Lake at about 4,250 m</b>",
         "Adds a rough drive from Chhatru to Chandratal lake — only when the road and weather allow.",
         "the 5-day Hampta Pass trek with Chandratal"),
    card(f"{UP}glacial-stream-green-valley-peaks-768x1024.webp", 768, 1024,
         "Fast glacial stream over boulders below pine-dotted green slopes and a rocky peak under blue sky",
         "Easy", "Jobra–Chika day walk", "<b>No pass crossing</b>",
         "An easy walk to the first riverside meadow and back — for families who won't cross the pass.",
         "a Jobra–Chika day walk from Manali"),
    card(f"{UP}snowman-lit-snow-igloo-night-768x512.webp", 768, 512,
         "Snowman standing in front of a snow igloo glowing with warm light from inside at night",
         "Winter", "Winter alternative: Sethan snow", "<b>Jan–Mar, about 2,700 m</b>",
         "Same valley while the pass is closed: snow play and igloo nights at Sethan.",
         "a winter Sethan snow trip with an igloo night",
         extra='<a class="x" href="/adventure/igloo-stay-manali/">Igloo stay →</a>'),
])

steps_exp = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Arrive in Manali a day early", "Sleep one night at about 2,000 m to acclimatise. Kit check and briefing with the trek team; carry ID copies and any medical form the operator asks for."),
    ("Day 1 — Jobra to Chika", "About an hour's drive to Jobra on the Prini–Sethan road, then a short walk to the riverside camp at Chika (about 3,050 m)."),
    ("Day 2 — Chika to Balu ka Ghera", "Walk up the valley to Balu ka Ghera (about 3,600 m), the last camp below the pass."),
    ("Day 3 — the pass day", "Early start, cross Hampta Pass (about 4,270 m), then a steep descent to Shea Goru (about 3,900 m). Plan 7–9 hours on your feet."),
    ("Day 4 — down to Chhatru", "Descend to Chhatru (about 3,350 m) on the Gramphu–Kaza road; your cab drives you back to Manali through the Atal Tunnel."),
    ("Day 5 — Chandratal (optional)", "If the road is open, drive on to Chandratal lake before heading back. Never guaranteed — it depends on the road and the weather."),
])

booking = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Tell us your dates", "WhatsApp or the quote form — dates, group size, ages and where you start from."),
    ("We check the season window", "Pass conditions, the year's orders and team availability with a registered local operator."),
    ("You get one quote", "Trek, Manali hotel nights before and after, and the cab to Jobra and back from Chhatru in one plan."),
    ("Confirm and go", "We send the kit list, reporting time and what to expect before you travel."),
])

faqs = [
    ("How high is Hampta Pass?", "About 4,270 m (around 14,000 ft). Published figures range from 4,200 to 4,300 m."),
    ("How long is the Hampta Pass trek?", "Roughly 26 km on foot from Jobra to Chhatru over 4 trekking days, or 5 days with the Chandratal drive."),
    ("What is the best time for the Hampta Pass trek?", "Mid-June to September. June still has snow on the pass, July–August is the monsoon with high streams, and September has the clearest views."),
    ("Can I do Hampta Pass in October or winter?", 'No. Snow closes the pass from about October to May. In winter we plan Sethan snow and <a href="/adventure/igloo-stay-manali/">igloo nights</a> in the same valley instead.'),
    ("Is Hampta Pass difficult for beginners?", "It is rated moderate. Fit beginners manage it with a guide, but the pass day is long (7–9 hours) with a steep descent and cold river crossings."),
    ("Do I need a permit for Hampta Pass?", 'Trekkers register at the forest/tourism check post on the Jobra side, and your operator arranges the forest permits. No Rohtang permit is needed to return through the Atal Tunnel — see <a href="/rohtang-pass-permit-himachal-road-status/">Rohtang permit vs Atal Tunnel</a>.'),
    ("Is there mobile network on the trek?", "No. Signal fades after Sethan and the camps have none until you are back on the road at Chhatru."),
    ("Can children do the Hampta trek?", "There is no government age rule; operators usually take fit children of about 9–10 years and up with a parent. Tell us the ages and we suggest the 4-day plan or the Jobra–Chika walk."),
]
faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)

more = [
    ("/adventure/triund-trek/", "🥾", "Triund Trek", "Easier day hike above McLeodganj"),
    ("/adventure/camping-in-kasol/", "⛺", "Camping in Kasol", "Riverside camps, Parvati valley"),
    ("/adventure/atal-tunnel-sissu-snow-trip/", "🚇", "Atal Tunnel &amp; Sissu", "Your exit road from Lahaul"),
    ("/adventure/adventure-activities-in-manali/", "🧭", "Adventure in Manali", "What's open in your month"),
    ("/adventure/himalayan-peak-expeditions/", "🏔️", "Peak expeditions", "The next step up"),
    ("/adventure/", "⛰️", "All adventures", "Air · Water · Snow · Land"),
]
more_html = "".join(f'<a class="sza-cat" href="{h}"><span class="ic">{i}</span><span class="n">{n}</span><span class="c">{c}</span></a>' for h, i, n, c in more)

reel = (HERE.parent / "media" / SLUG / "reel-section.html").read_text(encoding="utf-8").strip()

page = f'''<!-- hampta-pass-trek — built by Page Builder (night) 17 Oct 2026 from the Research Lead brief 15 Oct + Visual Studio media @220d56f (reel-section @f70f79a). Kit v1.7. No prices, no operator names; altitudes "about"; check-post fee and 2026 monsoon order on Hamta left off (unverified). Photos neutral alt. Quote-form links carry ?activity=Hampta%20Pass%20trek. -->
<style>.sza-hpt .sza-hero-in>*{{max-width:620px}}.sza-hpt .sza-chips{{max-width:700px}}.sza-hpt #experience .sza-steps{{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}.sza-hpt .sza-media ul{{padding-left:20px;list-style:disc;margin:0}}.sza-hpt .sza-media ul li{{margin:0 0 8px}}.sza-hpt .sza-media img{{height:auto;aspect-ratio:4/3;object-fit:cover}}.sza-hpt .sza-media video{{height:auto;aspect-ratio:16/9}}.sza-hpt #spots .sza-grid{{grid-template-columns:repeat(auto-fit,minmax(220px,1fr))}}.sza-hpt #spots .sza-card .img img{{aspect-ratio:3/2;object-fit:cover}}.sza-hpt .sza-checks{{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}.sza-hpt .sza-choose{{margin-top:32px}}.sza-hpt .go .x{{margin-right:14px}}@media(max-width:820px){{.sza-hpt .sza-hero video{{object-position:30% 50%}}.sza-hpt .sza-hero:after{{background:linear-gradient(180deg,rgba(11,31,51,.35) 0%,rgba(11,31,51,.6) 40%,rgba(11,31,51,.94) 100%)}}}}</style>
<div class="sza sza-hpt">
<section class="sza-hero">
<video autoplay muted loop playsinline preload="metadata" poster="{UP}hampta-pass-trek-hero-poster.webp" aria-label="A glacial stream below green slopes, a tent camp in a meadow, trekkers on snow and a bare brown valley, with a gold altitude line from the Kullu side over Hampta Pass at about 4,270 m to the Lahaul side; about 26 km on foot in 4 to 5 days, open mid-June to September"><source src="{CDN}hero.webm" type="video/webm"><source src="{CDN}hero.mp4" type="video/mp4"></video>
<div class="sza-hero-in">
<span class="sza-kicker">Trek · Manali → Lahaul · ~4,270 m</span>
<p class="sza-hero-tag">Green Kullu one side, bare Lahaul the other</p>
<p class="sza-hero-sub">A 4–5 day crossing from Jobra to Chhatru over the Pir Panjal — we plan the trek, your Manali hotel and the cab at both ends.</p>
<ul class="sza-chips"><li><b>Pass</b> ~4,270 m</li><li><b>On foot</b> ~26 km</li><li><b>Trek days</b> 4–5</li><li><b>Open</b> Mid-Jun – Sep</li><li><b>Grade</b> Moderate</li><li><b>Price</b> Get Quote</li></ul>
<div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan my trek</a></div>
<div class="sza-trust"><span><a href="https://suzutravels.com/certificates/">HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022</a></span><span>Trek + hotel + cab</span><span>Reply within minutes</span></div>
</div>
</section>
<nav class="sza-nav" aria-label="On this page"><div class="sza-nav-in"><a href="#overview">Overview</a><a href="#spots">Options</a><a href="#experience">Day by day</a><a href="#season">Best time</a><a href="#safety">Safety</a><a href="#booking">How booking works</a><a href="#packages">Packages</a><a href="#faq">FAQ</a><a class="cta" href="{MAIN}" target="_blank" rel="noopener">Get Quote</a></div></nav>

<section class="sza-sec" id="overview">
<span class="sza-kicker">Quick answer</span>
<h2>Hampta Pass trek, at a glance</h2>
<p class="sza-answer">Hampta Pass (about 4,270 m) is a 4–5 day trek of roughly 26 km that crosses the Pir Panjal from the green Kullu side near Manali to the dry Lahaul side at Chhatru. It is open only from mid-June to September; snow closes it from October to May. Treks start at Jobra, about an hour's drive from Manali, and many groups add a Chandratal day.</p>
<div class="sza-facts"><div class="sza-fact"><div class="k">Highest point</div><div class="v">Hampta Pass, about 4,270 m (~14,000 ft; sources range 4,200–4,300 m)</div></div><div class="sza-fact"><div class="k">Route</div><div class="v">Jobra → Chika → Balu ka Ghera → pass → Shea Goru → Chhatru, about 26 km on foot</div></div><div class="sza-fact"><div class="k">Days</div><div class="v">4–5 trek days (+1 for Chandratal); plan about 7 days from Delhi or Chandigarh</div></div><div class="sza-fact"><div class="k">Season</div><div class="v">Mid-June to September; October–May closed by snow</div></div><div class="sza-fact"><div class="k">Grade</div><div class="v">Moderate — one long pass day (7–9 h) and cold river crossings</div></div><div class="sza-fact"><div class="k">Price</div><div class="v">Get Quote</div></div></div>
</section>

<section class="sza-sec alt" id="spots">
<span class="sza-kicker">Your options</span>
<h2>Ways to do Hampta Pass</h2>
<p class="sza-lead">Pick the version that fits your group. Photos show high Himalayan trails and camps in general.</p>
<div class="sza-grid">{cards}</div>
<div class="sza-media sza-choose" id="profile"><video autoplay muted loop playsinline preload="none" poster="{UP}hampta-pass-green-to-grey-explainer.webp" width="1600" height="900" aria-label="Green to grey in 4 days: altitude profile from Manali about 2,000 m by road to Jobra, then Chika about 3,050 m, Balu ka Ghera about 3,600 m, Hampta Pass about 4,270 m, Shea Goru about 3,900 m and Chhatru about 3,350 m, with a Chandratal branch road permitting; about 26 km over 4 days; open mid-June to September"><source src="{CDN}explainer.webm" type="video/webm"><source src="{CDN}explainer.mp4" type="video/mp4"></video><div><h3>Green to grey in 4 days</h3><ul><li><b>Kullu side</b> → forest, meadows and streams up to Balu ka Ghera.</li><li><b>Pass day</b> → about 4,270 m, then a steep drop to Shea Goru.</li><li><b>Lahaul side</b> → bare, brown, high-desert valley at Chhatru.</li><li><b>Chandratal</b> → a road add-on, only when the road is open.</li></ul></div></div>
</section>

<section class="sza-sec" id="experience">
<span class="sza-kicker">Day by day</span>
<h2>How your Hampta trek works</h2>
<ol class="sza-steps">{steps_exp}</ol>
<div class="sza-media"><img src="{UP}trek-tents-meadow-stream-valley-768x1024.webp" alt="Row of orange trek tents on a green meadow beside a stream in a steep mountain valley under a blue cloudy sky" loading="lazy" width="768" height="1024"><div><h3>Life at camp</h3><p>Nights are spent in tents at meadow camps beside the stream. The trek team sets up camp and cooks; you carry a day pack, or add a mule/porter for your backpack.</p><p>Pack a warm layer and rain shell even in summer, good trekking shoes with grip, and spare socks for the river crossings. There is no mobile signal after Sethan.</p></div></div>
</section>

<section class="sza-sec alt" id="season">
<span class="sza-kicker">When to go</span>
<h2>Best time for the Hampta Pass trek</h2>
<div class="sza-scroll"><table class="sza-tbl"><thead><tr><th>Months</th><th>Conditions</th><th>Our advice</th></tr></thead><tbody><tr><td>Mid-Jun – early Jul</td><td>Snow still on the pass, cold nights</td><td>Good for snow lovers; strong stream crossings start late June</td></tr><tr><td>Mid-Jul – Aug</td><td>Monsoon: flowers, rain, highest river levels, landslides on roads</td><td>Possible but riskiest; follow that year's monsoon orders and weather alerts</td></tr><tr><td>Sep</td><td>Clearest skies, colder nights, fewer streams</td><td>Best month for views</td></tr><tr><td>Oct – May</td><td>Pass under snow, route closed</td><td>Plan for next season; do Sethan snow or Solang instead</td></tr></tbody></table></div>
<p style="margin-top:14px">Planning for 2027? Searches and bookings climb from March. Snow already shut the Manali–Kaza road in mid-October 2026 — see our <a href="/leh-manali-and-manali-kaza-roads-shut-by-snow-15-oct-2026/">15 Oct 2026 road update</a>.</p>
</section>

<div class="sza-band" id="safety"><div class="sza-band-in">
<span class="sza-kicker">Safety first</span>
<h2>What we check before we book your trek</h2>
<p class="sza-lead">Suzu Travels is an <a href="https://suzutravels.com/certificates/" style="color:#f3d98f;text-decoration:underline">HP Tourism registered travel agent (Reg. No. DTO-MND-11-243/2022)</a>. We arrange the trek only with registered local operators and a guide, and plan around these checks:</p>
<ul class="sza-checks"><li><b>Registered team + check post</b>Trek only with a registered operator and guide, and register at the forest/tourism check post on the Jobra side. Lost or late groups on Hamta–Chhatru have needed police searches (31 trekkers traced by Lahaul-Spiti police in June 2025).</li><li><b>No signal after Sethan</b>Leave your full itinerary and Chhatru exit day with family; the trek team carries the communication device.</li><li><b>Altitude</b>One night in Manali first. The pass day climbs to about 4,270 m — watch for headache or nausea and descend if it gets worse.</li><li><b>River crossings</b>June–August streams run high: cross early in the morning, roped and in groups, as the guide says.</li><li><b>Weather orders</b>Himachal stops adventure activity when heavy rain is forecast (in 2021 trekking was covered too). In July–August we follow that year's Kullu/HP order.</li><li><b>Exit road</b>The Atal Tunnel road needs no Rohtang permit. The Chandratal road (Gramphu–Batal) can close with landslides, so the Chandratal day is never guaranteed.</li></ul>
</div></div>

<section class="sza-sec" id="booking">
<span class="sza-kicker">How booking works</span>
<h2>Get a quote in minutes</h2>
<ol class="sza-steps">{booking}</ol>
<div class="sza-media"><img src="{UP}barren-brown-mountain-valley-768x576.webp" alt="Dry, barren brown mountain valley with bare rock slopes under a blue sky with heavy clouds" loading="lazy" width="768" height="576"><div><h3>What your quote depends on</h3><ul><li>4-day classic or 5 days with Chandratal</li><li>Group size; private trek or a fixed group</li><li>Tent sharing (twin or single) and a mule/porter for your backpack</li><li>Month (June snow kit vs September)</li><li>Manali hotel nights, the cab to Jobra and back from Chhatru, and rental jacket/poles/shoes — today's rate on WhatsApp within minutes</li></ul></div></div>
</section>

{reel}

<section class="sza-quote"><div><span class="sza-kicker">Ready for the pass?</span><h2>Get your Hampta Pass quote</h2><p>Tell us your dates and group size. We reply with one plan — trek, Manali hotel and both cabs — for your dates within minutes.</p></div><div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan full trip</a></div></section>

<section class="sza-sec" id="packages">
<span class="sza-kicker">Make it a trip</span>
<h2>Manali + Hampta + Chandratal</h2>
<p>Most groups plan <b>6–7 days</b>: two hotel nights in Manali, the trek, the cab from Manali to Jobra and back from Chhatru. Read our <a href="/manali/">Manali guide</a>, see the <a href="/himachal-tour-package-from-delhi/">Himachal tour package from Delhi</a>, or check <a href="/adventure/adventure-activities-in-manali/">adventure activities in Manali</a> — a <a href="/adventure/paragliding-in-manali/">paragliding flight in Solang</a> fits before the trek in June or September. Going on to Spiti? See our <a href="/destination/spiti-valley-tour-packages/">Spiti valley tour packages</a>. Need only a cab to Manali? Book a <a href="/cabs/delhi-to-manali-taxi/">Delhi to Manali taxi</a> or a <a href="/cabs/chandigarh-to-manali-taxi/">Chandigarh to Manali taxi</a>.</p>
<div class="sza-btns" style="margin-top:18px">{walink("Manali + Hampta + Chandratal — Get Quote", what="a 6–7 day Manali + Hampta Pass + Chandratal trip")}{walink("Winter Sethan snow trip — Get Quote", what="a winter Sethan snow trip from Manali", cls="sza-btn line")}</div>
</section>

<section class="sza-sec sza-faq" id="faq">
<span class="sza-kicker">FAQ</span>
<h2>Hampta Pass trek — questions</h2>
{faq_html}
</section>

<section class="sza-sec alt" id="more">
<span class="sza-kicker">More adventures</span>
<h2>Explore more in Himachal</h2>
<div class="sza-cats">{more_html}</div>
</section>
</div>
'''
out = HERE / f"{SLUG}.html"
out.write_text(page, encoding="utf-8")
print(len(page))
