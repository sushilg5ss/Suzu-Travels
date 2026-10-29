#!/usr/bin/env python3
# Generates adventure-kit/pages/kheerganga-trek.html (Page Builder night, 19 Oct 2026 IST)
import urllib.parse, pathlib
SLUG = "kheerganga-trek"
HERE = pathlib.Path(__file__).resolve().parent
CDN = "https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@cc279ccd9b7e298a582443a61c14a0a3d8e1d945/adventure-kit/media/kheerganga-trek/"
UP = "https://suzutravels.com/wp-content/uploads/2026/10/"
QUOTE = "/himachal-tour-packages-quote/?activity=" + urllib.parse.quote("Kheerganga trek")
WHAT = "the Kheerganga trek in the Parvati valley"

def wa(what=WHAT, tag=SLUG):
    t = f"Hi Suzu Travels, I want a quote for {what}. Travel date: ___ , people: ___ (page: {tag})"
    return "https://wa.me/917087488961?text=" + urllib.parse.quote(t, safe="")

def walink(label, what=WHAT, cls="sza-btn gold"):
    return f'<a class="{cls}" href="{wa(what)}" target="_blank" rel="noopener">{label}</a>'

MAIN = wa()

def card(src, w, h, alt, badge, title, meta, text, what):
    return (f'<article class="sza-card"><div class="img"><img src="{src}" alt="{alt}" loading="lazy" width="{w}" height="{h}"><span class="sza-badge">{badge}</span></div>'
            f'<div class="body"><h3>{title}</h3><div class="meta">{meta}</div><p class="meta">{text}</p>'
            f'<div class="go"><a class="q" href="{wa(what)}" target="_blank" rel="noopener">Get Quote →</a></div></div></article>')

cards = "".join([
    card(f"{UP}hikers-footbridge-forest-trail-himalaya-768x1152.webp", 768, 1152,
         "Two hikers crossing a wooden footbridge over a rushing stream on a forest trail in the Himalaya",
         "Classic pick", "Via Nakthan &amp; Rudranag", "<b>~12 km one way</b>",
         "The standard trail: Nakthan village, the Rudranag waterfall and small dhabas on the way up.",
         "the Kheerganga trek via Nakthan and Rudranag"),
    card(f"{UP}mountain-cascade-autumn-forest-himalaya-768x1365.webp", 768, 1365,
         "A mountain stream cascading over rocks through an autumn forest in the Himalaya",
         "Quieter trail", "Via Kalga", "<b>~14 km, guide advised</b>",
         "A quieter forest trail through Kalga village; slightly longer, so we add a registered guide.",
         "the Kheerganga trek via Kalga with a guide"),
    card(f"{UP}stone-hut-pine-forest-himachal-768x1365.webp", 768, 1365,
         "A stone hut in a misty pine forest in the Himachal hills",
         "Best for families", "Sleep in Tosh or Kalga, trek next morning", "<b>Reach the top by 10 am</b>",
         "Stay the night near the trailhead so an early start gets you to the top on time.",
         "a night in Tosh or Kalga and the Kheerganga trek next morning"),
])

steps_exp = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Night before", "Stay in Kasol, Tosh, Kalga or Barshaini — we book it together with your cab."),
    ("Early start, 5–6 am", "Start from the Barshaini road-head and register at the forest checkpoint with a photo ID."),
    ("Climb 4–6 hours", "Up through Nakthan and Rudranag (or via Kalga), through forest and past waterfalls."),
    ("At the top by 10 am", "The hot spring, the Shiva shrine and the meadow views at about 2,960 m."),
    ("Down well before 2 pm", "About 3–4 hours back to Barshaini — the 2 pm turn-around is the rule."),
    ("Onward", "Cab back to Kasol or Manali, or on to the next stop of your package."),
])

booking = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Tell us your dates", "WhatsApp or the quote form — dates, group size, ages and where you start from."),
    ("We check your date", "Season and road to Barshaini, your stay near the trailhead and a registered guide if you want one."),
    ("You get one quote", "Trek, stay before/after and the cab for the whole trip in one plan."),
    ("Confirm and go", "We send the pickup time, the start time for your trek day and what to pack."),
])

faqs = [
    ("Is Kheerganga open in 2026?", "Yes, as a day trek. Since July 2024 the Forest Department has banned camping and night stays at the top; you must reach by 10 am and leave by 2 pm."),
    ("Can I camp at Kheerganga?", "No. Overnight stays are allowed lower down in Nakthan, Barshaini, Kalga or Tosh. Kasol has riverside camps."),
    ("How long is the Kheerganga trek?", "About 12–13 km one way from Barshaini, roughly 24–26 km return; most walkers take 4–6 hours up and 3–4 hours down."),
    ("How do I reach the start?", "Drive or take a bus to Kasol (about 30 km from Bhuntar airport), then about 15–20 km more to the Barshaini road-head."),
    ("What is the best time?", "April to June and mid-September to October. Trekking is permitted from April to October; skip the monsoon months."),
    ("Is there a hot spring?", "Yes, the Parvati Kund hot spring at the top (about 2,960 m), next to a Shiva shrine. It is a sacred site — follow the posted rules."),
    ("Is it good for beginners?", "It is long but not technical. Start early, carry water and rain gear, and keep the 2 pm turn-around."),
    ("How much does the Kheerganga trek cost?", "It depends on your stay, cab, group size and month. Send your dates on WhatsApp for today's rate within minutes — Price: Get Quote."),
]
faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)

more = [
    ("/adventure/camping-in-kasol/", "⛺", "Camping in Kasol", "Riverside camps, Parvati valley"),
    ("/adventure/river-rafting-in-kullu-manali/", "🚣", "Rafting in Kullu", "Pirdi &amp; Raisan rafting points"),
    ("/adventure/triund-trek/", "⛰️", "Triund Trek", "Day hike above McLeodganj"),
    ("/adventure/hampta-pass-trek/", "🥾", "Hampta Pass Trek", "Manali to Lahaul in 4–5 days"),
    ("/adventure/prashar-lake-trek/", "🏞️", "Prashar Lake Trek", "Easy trek near Mandi"),
    ("/adventure/", "🧭", "All adventures", "Air · Water · Snow · Land"),
]
more_html = "".join(f'<a class="sza-cat" href="{h}"><span class="ic">{i}</span><span class="n">{n}</span><span class="c">{c}</span></a>' for h, i, n, c in more)

reel = (HERE.parent / "media" / SLUG / "reel-section.html").read_text(encoding="utf-8").strip()

page = f'''<!-- kheerganga-trek — built by Page Builder (night) 19 Oct 2026 IST from the Research Lead brief 17 Oct + Visual Studio media @cc279cc (reel-section @3a913dc). Kit v1.8. No prices, no operator names. Unverified items left off: checkpoint fee amount, 320/day cap in 2026, separate pools, exact Kasol–Barshaini km. No Kheerganga/hot-spring photo exists — generic photos with neutral alt. -->
<style>.sza-kgt .sza-hero-in>*{{max-width:620px}}.sza-kgt .sza-chips{{max-width:700px}}.sza-kgt .sza-media ul{{padding-left:20px;list-style:disc;margin:0}}.sza-kgt .sza-media ul li{{margin:0 0 8px}}.sza-kgt .sza-media img{{height:auto;aspect-ratio:4/3;object-fit:cover}}.sza-kgt .sza-media video{{height:auto;aspect-ratio:16/9}}.sza-kgt #spots .sza-grid{{grid-template-columns:repeat(auto-fit,minmax(240px,1fr))}}.sza-kgt #spots .sza-card .img img{{aspect-ratio:3/2;object-fit:cover}}.sza-kgt .sza-checks{{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}.sza-kgt .sza-choose{{margin-top:32px}}@media(max-width:820px){{.sza-kgt .sza-hero video{{object-position:30% 50%}}.sza-kgt .sza-hero:after{{background:linear-gradient(180deg,rgba(11,31,51,.35) 0%,rgba(11,31,51,.6) 40%,rgba(11,31,51,.94) 100%)}}}}</style>
<div class="sza sza-kgt">
<section class="sza-hero">
<video autoplay muted loop playsinline preload="metadata" poster="{UP}kheerganga-trek-hero-poster.webp" aria-label="The green Parvati valley, a forest footbridge, a mountain cascade and trekkers below a snow peak, with a gold trail line from the Barshaini road-head to the top: about 12 to 13 km, top at about 2,960 m, day trek only, leave by 2 pm"><source src="{CDN}hero.webm" type="video/webm"><source src="{CDN}hero.mp4" type="video/mp4"></video>
<div class="sza-hero-in">
<span class="sza-kicker">Treks &amp; Camps · Parvati Valley, Kullu</span>
<p class="sza-hero-tag">A forest climb to a hot spring meadow — done in a day</p>
<p class="sza-hero-sub">12–13 km up from Barshaini to Kheerganga (about 2,960 m). Camping at the top is banned, so we plan your night in Kasol, Tosh or Kalga, plus the cab.</p>
<ul class="sza-chips"><li><b>One way</b> ~12–13 km</li><li><b>Top</b> ~2,960 m</li><li><b>Day trek</b> only</li><li><b>Top by</b> 10 am · leave by 2 pm</li><li><b>Season</b> Apr–Jun &amp; Sep–Oct</li><li><b>Price</b> Get Quote</li></ul>
<div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan my trip</a></div>
<div class="sza-trust"><span><a href="https://suzutravels.com/certificates/">HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022</a></span><span>Trek + stay + cab</span><span>Reply within minutes</span></div>
</div>
</section>
<nav class="sza-nav" aria-label="On this page"><div class="sza-nav-in"><a href="#overview">Overview</a><a href="#spots">Routes</a><a href="#experience">Your day</a><a href="#season">Best time</a><a href="#safety">Rules &amp; safety</a><a href="#booking">How booking works</a><a href="#packages">Packages</a><a href="#faq">FAQ</a><a class="cta" href="{MAIN}" target="_blank" rel="noopener">Get Quote</a></div></nav>

<section class="sza-sec" id="overview">
<span class="sza-kicker">Quick answer</span>
<h2>Kheerganga trek, at a glance</h2>
<p class="sza-answer">Kheerganga is a 12–13 km trek from Barshaini, the road-end above Kasol, to a meadow and hot spring at about 2,960 m. Since July 2024 the Forest Department allows no camping at the top: walkers must reach by 10 am and leave by 2 pm. Most people take 4–6 hours up and 3–4 down, and sleep in Kasol, Tosh, Kalga or Nakthan.</p>
<div class="sza-facts"><div class="sza-fact"><div class="k">Start</div><div class="v">Barshaini road-head, about 15–20 km beyond Kasol</div></div><div class="sza-fact"><div class="k">Distance</div><div class="v">~12–13 km one way (~24–26 km return)</div></div><div class="sza-fact"><div class="k">Top</div><div class="v">~2,960 m — Parvati Kund hot spring and a Shiva shrine</div></div><div class="sza-fact"><div class="k">Rule</div><div class="v">Day trek only — no night stay or camping at the top (Forest Dept, July 2024)</div></div><div class="sza-fact"><div class="k">Season</div><div class="v">Trekking April–October; best Apr–Jun and mid-Sep–Oct</div></div><div class="sza-fact"><div class="k">Price</div><div class="v">Get Quote</div></div></div>
</section>

<section class="sza-sec alt" id="spots">
<span class="sza-kicker">Your options</span>
<h2>Ways to do the Kheerganga trek</h2>
<p class="sza-lead">Two trails go up from Barshaini; where you sleep the night before decides how easy the day is.</p>
<div class="sza-grid">{cards}</div>
<div class="sza-media sza-choose" id="kheerganga-day"><video autoplay muted loop playsinline preload="none" poster="{UP}your-kheerganga-day-explainer.webp" width="1600" height="900" aria-label="Your Kheerganga day: time and altitude line from Barshaini at about 2,000 m early morning, past Nakthan and Rudranag at about 2,700 m, to the top by 10 am at about 2,960 m, a red 2 pm turn-around marker and 3 to 4 hours down; no camping at the top, sleep in Kasol, Tosh or Kalga"><source src="{CDN}explainer.webm" type="video/webm"><source src="{CDN}explainer.mp4" type="video/mp4"></video><div><h3>Your Kheerganga day</h3><ul><li><b>5–6 am</b> → leave Barshaini (~2,000 m), register at the checkpoint.</li><li><b>By 10 am</b> → at the top (~2,960 m): hot spring and meadow.</li><li><b>2 pm</b> → latest time to start down; guards record walkers.</li><li><b>Evening</b> → back at Barshaini, night in Kasol, Tosh or Kalga.</li></ul></div></div>
</section>

<section class="sza-sec" id="experience">
<span class="sza-kicker">Your day</span>
<h2>How your Kheerganga day works</h2>
<ol class="sza-steps">{steps_exp}</ol>
<div class="sza-media"><img src="{UP}tosh-village-houses-valley-768x347.webp" alt="Hillside houses of Tosh village in the Parvati valley" loading="lazy" width="768" height="347"><div><h3>Where you sleep</h3><p>No one may stay at the top any more, so the night before and after is in the valley: riverside camps in <a href="/adventure/camping-in-kasol/">Kasol</a>, or guesthouses in Tosh, Kalga, Barshaini or Nakthan, closer to the trail.</p><p>Carry water, snacks, a warm layer, a rain shell and shoes with grip. Pack your litter back down.</p></div></div>
</section>

<section class="sza-sec alt" id="season">
<span class="sza-kicker">When to go</span>
<h2>Best time for the Kheerganga trek</h2>
<div class="sza-scroll"><table class="sza-tbl"><thead><tr><th>Months</th><th>Trail</th><th>Our advice</th></tr></thead><tbody><tr><td>Apr–Jun</td><td>Open; green, busy in May–Jun</td><td>Best window; book your stay early</td></tr><tr><td>Jul–Aug</td><td>Monsoon: slippery trail, landslide risk on the road</td><td>Avoid; check the road before you go</td></tr><tr><td>Sep–Oct</td><td>Open, clear skies, cold nights</td><td>Great; October is the last month</td></tr><tr><td>Nov–Mar</td><td>Snow and ice; outside the April–October trekking season</td><td>Not offered — do a Kasol stay instead</td></tr></tbody></table></div>
<p style="margin-top:14px">Out of season? Searches for Kheerganga peak in May–June; plan now for spring, or take a winter <a href="/adventure/camping-in-kasol/">Kasol camp stay</a> instead.</p>
</section>

<div class="sza-band" id="safety"><div class="sza-band-in">
<span class="sza-kicker">Rules &amp; safety</span>
<h2>What we check before we book your trek</h2>
<p class="sza-lead">Suzu Travels is an <a href="https://suzutravels.com/certificates/" style="color:#f3d98f;text-decoration:underline">HP Tourism registered travel agent (Reg. No. DTO-MND-11-243/2022)</a>. We arrange the trek with registered local operators and plan around these checks:</p>
<ul class="sza-checks"><li><b>Day-only rule</b>No camping or night stay at the top (Forest Department order, July 2024). Never book anyone who offers you a tent at Kheerganga.</li><li><b>10 am / 2 pm</b>Reach the top by 10 am and leave by 2 pm — a barrier and guards at Icy Point record walkers.</li><li><b>Register at Barshaini</b>Carry a photo ID for the forest checkpoint; a small fee is charged locally.</li><li><b>Registered guides</b>Trekking guides must be registered under the HP adventure activity rules; we arrange one with a registered local operator.</li><li><b>River water</b>The Parbati and its side streams rise fast after rain and dam water release — never step into the river.</li><li><b>Sacred hot spring</b>Follow the posted bathing rules at Parvati Kund; no soap, no litter.</li></ul>
</div></div>

<section class="sza-sec" id="booking">
<span class="sza-kicker">How booking works</span>
<h2>Get a quote in minutes</h2>
<ol class="sza-steps">{booking}</ol>
<figure id="booking-explainer" style="margin:28px auto 28px;max-width:880px"><video poster="https://suzutravels.com/wp-content/uploads/2026/09/how-booking-works-adventure-explainer.webp" autoplay muted loop playsinline preload="none" width="1600" height="900" style="display:block;width:100%;height:auto;aspect-ratio:16/9;border-radius:18px;background:#0b1f33;box-shadow:0 12px 32px rgba(11,31,51,.2)" aria-label="10-second motion graphic: how booking works in 4 steps. Tell us the activity, place, date and group size; we check your date, season, weather rules and a registered local operator; you get one quote, activity alone or with hotel, cab and sightseeing; confirm with a small advance and our team looks after the day"><source src="https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@1d39d275782e44fb56b01370aa2524e4786607f3/adventure-kit/media/adventure-hub/booking-explainer.webm" type="video/webm"><source src="https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@1d39d275782e44fb56b01370aa2524e4786607f3/adventure-kit/media/adventure-hub/booking-explainer.mp4" type="video/mp4"></video><figcaption style="margin-top:10px;font-size:15px;line-height:1.5;color:#5b6975;text-align:center">Four steps from your WhatsApp message to your Kheerganga trek. Send your dates and get today’s rate within minutes.</figcaption></figure>
<div class="sza-media"><img src="{UP}parvati-valley-kasol-768x513.webp" alt="Sun breaking over the green Parvati Valley and river near Kasol, Himachal" loading="lazy" width="768" height="513"><div><h3>What your quote depends on</h3><ul><li>Route (Nakthan or Kalga) and whether you want a guide or porter</li><li>Where you sleep before and after — Kasol, Tosh, Kalga or Barshaini — and the room type</li><li>Group size and ages</li><li>Cab from Bhuntar airport, Manali, Chandigarh or Delhi; one-way or round trip</li><li>Month (May–Jun and long weekends are busiest); add-ons like a Kasol camp night or rafting — today's rate on WhatsApp within minutes</li></ul></div></div>
</section>

{reel}

<section class="sza-quote"><div><span class="sza-kicker">Ready for the trail?</span><h2>Get your Kheerganga quote</h2><p>Tell us your dates and group size. We reply with one plan — trek day, stay in Kasol, Tosh or Kalga and the cab — within minutes.</p></div><div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan full trip</a></div></section>

<section class="sza-sec" id="packages">
<span class="sza-kicker">Make it a trip</span>
<h2>Kasol + Kheerganga + Manali</h2>
<p>The easy way to fit it in: <b>Kasol 2 nights (a riverside camp + the Kheerganga day) → Manali 2 nights</b>, with the cab from Delhi or Chandigarh. Read our <a href="/kasol-trip-plan/">Kasol trip plan</a>, add <a href="/adventure/river-rafting-in-kullu-manali/">river rafting in Kullu</a> on the way, or see <a href="/adventure/adventure-activities-in-manali/">adventure activities in Manali</a> and <a href="/adventure/bike-rent-in-manali/">bike rent in Manali</a>. Need only a cab? Book a <a href="/cabs/delhi-to-manali-taxi/">Delhi to Manali taxi</a>, a <a href="/cabs/chandigarh-to-manali-taxi/">Chandigarh to Manali taxi</a> or a <a href="/cabs/manali-taxi-service/">Manali taxi</a>.</p>
<div class="sza-btns" style="margin-top:18px">{walink("Kasol + Kheerganga + Manali — Get Quote", what="a Kasol (2 nights, camp + Kheerganga day) and Manali (2 nights) trip with cab")}{walink("Kheerganga + Kasol stay — Get Quote", what="the Kheerganga trek with a stay in Kasol", cls="sza-btn line")}</div>
</section>

<section class="sza-sec sza-faq" id="faq">
<span class="sza-kicker">FAQ</span>
<h2>Kheerganga trek — questions</h2>
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
