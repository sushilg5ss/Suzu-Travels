#!/usr/bin/env python3
# Generates adventure-kit/pages/paragliding-in-khajjiar-dalhousie.html (Page Builder night, 16 Oct 2026)
import urllib.parse, pathlib
SLUG = "paragliding-in-khajjiar-dalhousie"
HERE = pathlib.Path(__file__).resolve().parent
CDN = "https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@cfa8a67ff7cc773130b61a2db4d104757b5f2788/adventure-kit/media/paragliding-in-khajjiar-dalhousie/"
UP = "https://suzutravels.com/wp-content/uploads/2026/10/"
QUOTE = "/himachal-tour-packages-quote/?activity=" + urllib.parse.quote("Paragliding")

def wa(what="paragliding in Khajjiar near Dalhousie", tag=SLUG):
    t = f"Hi Suzu Travels, I want a quote for {what}. Travel date: ___ , people: ___ (page: {tag})"
    return "https://wa.me/917087488961?text=" + urllib.parse.quote(t, safe="")

def walink(label, what="paragliding in Khajjiar near Dalhousie", cls="sza-btn gold"):
    return f'<a class="{cls}" href="{wa(what)}" target="_blank" rel="noopener">{label}</a>'

MAIN = wa()

def card(src, w, h, alt, badge, title, meta, text, what, extra=""):
    return (f'<article class="sza-card"><div class="img"><img src="{src}" alt="{alt}" loading="lazy" width="{w}" height="{h}"><span class="sza-badge">{badge}</span></div>'
            f'<div class="body"><h3>{title}</h3><div class="meta">{meta}</div><p class="meta">{text}</p>'
            f'<div class="go">{extra}<a class="q" href="{wa(what)}" target="_blank" rel="noopener">Get Quote →</a></div></div></article>')

cards = "".join([
    card(f"{UP}tandem-paragliding-pilot-and-passenger-in-flight-768x569.webp", 768, 569,
         "Tandem paragliding selfie: passenger in front and pilot behind, both in helmets, flying high above forested hills",
         "Classic pick", "Khajjiar tandem flight", "<b>Licensed tandem pilot</b>",
         "A scenic flight over the meadow and the deodar forest around it. No licence or experience needed.",
         "a tandem paragliding flight in Khajjiar"),
    card(f"{UP}wide-meadow-edged-by-pine-forest-big-clouds-768x512.webp", 768, 512,
         "Wide open grassy meadow edged by a dark pine forest, a rocky mountain top and big white clouds in a blue sky",
         "Notified spots", "Dadota ↔ Lahara", "<b>Marked launch sites</b>",
         "The district has marked launch sites for flights from Dadota to Lahara and back; your pilot picks one by the day's wind.",
         "a Khajjiar paragliding flight (Dadota or Lahara launch)"),
    card(f"{UP}tandem-pilot-passenger-ready-hilltop-above-town-768x576.webp", 768, 576,
         "Tandem paragliding pilot and passenger in helmets and harnesses standing on a grassy hilltop take-off, looking over a green valley and town",
         "Easy add-on", "Dalhousie day trip + flight", "<b>Dalhousie → Khajjiar, about an hour</b>",
         "Leave Dalhousie early, fly in the calm morning air, be back for lunch.",
         "a Dalhousie day trip with a Khajjiar paragliding flight",
         extra='<a class="x" href="/dalhousie/">Dalhousie guide →</a>'),
    card(f"{UP}paraglider-yellow-wing-green-valley-cloudy-768x1152.webp", 768, 1152,
         "Paraglider with a yellow wing flying over a forested green valley and a town below on a cloudy day",
         "Package pairing", "Dharamshala–Dalhousie circuit", "<b>Kangra + Chamba in one trip</b>",
         "Add a Khajjiar morning to a Dharamshala–Dalhousie tour. Want a longer flight? Compare Bir Billing.",
         "a Dharamshala–Dalhousie trip with a Khajjiar paragliding flight",
         extra='<a class="x" href="/adventure/paragliding-in-bir-billing/">Bir Billing →</a>'),
])

steps_exp = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Send your date", "Dates, group size, ages and weights on WhatsApp or the quote form — we confirm the day's flying and the rate."),
    ("Reach Khajjiar early", "Calm morning air is best. Our cab drives you up from Dalhousie, about an hour."),
    ("Weigh-in &amp; briefing", "Weight check and a short safety briefing; the pilot checks the wind and picks the launch site."),
    ("Harness up, take off", "Helmet and harness on, a short run on the grass with the pilot behind you."),
    ("The flight", "Over the meadow and the forest around it — the day's air decides how long you stay up."),
    ("Land at the marked site", "Touch down at the marked landing point; collect your video if you booked it."),
])

booking = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Tell us your date", "WhatsApp or the quote form — date, people, ages, weights and where you start from."),
    ("We check the day", "Flying, weather and limits with a registered local operator."),
    ("You get one quote", "Flight, video if you want it, cab and hotel in Dalhousie or Dharamshala in one plan."),
    ("Confirm and go", "We send the reporting time and what to wear before you travel."),
])

faqs = [
    ("Is there paragliding in Dalhousie?", "The flying near Dalhousie happens at Khajjiar, about 24 km away. We did not find a separate notified site in Dalhousie town (checked Oct 2026)."),
    ("Where do you take off in Khajjiar?", "The district has marked launch sites for flights from Dadota to Lahara and from Lahara to Dadota; your pilot picks one by the wind."),
    ("Is Khajjiar paragliding open now?", "Yes. It restarted on 16 September 2026 after the monsoon ban; we re-check the week of your trip."),
    ("When is paragliding closed in Khajjiar?", "Every monsoon. In 2026 the Chamba tourism office stopped flying until 15 September."),
    ("Who can fly?", "Under Himachal's aero sports rules passengers must be at least 12 years old and 30 kg, and fly tandem with a licensed pilot."),
    ("How high is Khajjiar?", "The meadow sits at about 1,920 m (6,300 ft)."),
    ("Are the pilots licensed?", "Tandem pilots at Khajjiar hold licences that ABVIMAS, Manali renews after inspecting their equipment. Ask your pilot to show the licence."),
    ("What does paragliding in Khajjiar cost?", f'Rates change with season, flight and video. Ask on <a href="{MAIN}" target="_blank" rel="noopener">WhatsApp</a> and we send today\'s rate in minutes — Price: Get Quote.'),
]
faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)

more = [
    ("/adventure/paragliding-in-himachal/", "🧭", "Paragliding in Himachal", "Every site compared"),
    ("/adventure/paragliding-in-dharamshala/", "🪂", "Paragliding in Dharamshala", "Indrunag above McLeodganj"),
    ("/adventure/paragliding-in-bir-billing/", "🏔️", "Paragliding in Bir Billing", "The big Kangra site"),
    ("/adventure/triund-trek/", "🥾", "Triund Trek", "Day hike above McLeodganj"),
    ("/adventure/", "⛰️", "All adventures", "Air · Water · Snow · Land"),
]
more_html = "".join(f'<a class="sza-cat" href="{h}"><span class="ic">{i}</span><span class="n">{n}</span><span class="c">{c}</span></a>' for h, i, n, c in more)

reel = (HERE.parent / "media" / SLUG / "reel-section.html").read_text(encoding="utf-8").strip()

page = f'''<!-- paragliding-in-khajjiar-dalhousie — built by Page Builder (night) 16 Oct 2026 from the Research Lead (night) brief 16 Oct + Visual Studio (night) media @cfa8a67 (reel-section @86b1cd4). Kit v1.6. No prices, no operator names; no flight minutes, take-off heights or operator counts (unverified). Photos generic, neutral alt (never labelled Khajjiar). Quote-form links carry ?activity=Paragliding. -->
<style>.sza-kjr .sza-hero-in>*{{max-width:620px}}.sza-kjr .sza-chips{{max-width:700px}}.sza-kjr #experience .sza-steps{{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}.sza-kjr .sza-media ul{{padding-left:20px;list-style:disc;margin:0}}.sza-kjr .sza-media ul li{{margin:0 0 8px}}.sza-kjr .sza-media img{{height:auto;aspect-ratio:4/3;object-fit:cover}}.sza-kjr .sza-media video{{height:auto;aspect-ratio:16/9}}.sza-kjr #spots .sza-grid{{grid-template-columns:repeat(auto-fit,minmax(220px,1fr))}}.sza-kjr #spots .sza-card .img img{{aspect-ratio:3/2;object-fit:cover}}.sza-kjr .sza-checks{{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}.sza-kjr .sza-choose{{margin-top:32px}}.sza-kjr .go .x{{margin-right:14px}}@media(max-width:820px){{.sza-kjr .sza-hero video{{object-position:30% 50%}}.sza-kjr .sza-hero:after{{background:linear-gradient(180deg,rgba(11,31,51,.35) 0%,rgba(11,31,51,.6) 40%,rgba(11,31,51,.94) 100%)}}}}</style>
<div class="sza sza-kjr">
<section class="sza-hero">
<video autoplay muted loop playsinline preload="metadata" poster="{UP}paragliding-in-khajjiar-hero-poster.webp" aria-label="A green meadow ringed by conifer forest, a tandem pair ready on a hilltop and a tandem flight, with a schematic gold flight line between the Dadota and Lahara launch sites on the Khajjiar meadow at about 1,920 m"><source src="{CDN}hero.webm" type="video/webm"><source src="{CDN}hero.mp4" type="video/mp4"></video>
<div class="sza-hero-in">
<span class="sza-kicker">Air · Chamba · Khajjiar meadow</span>
<p class="sza-hero-tag">Fly over India's “mini Switzerland” — the meadow near Dalhousie</p>
<p class="sza-hero-sub">Tandem flights by licensed pilots at Khajjiar's marked launch sites; we fit the flight into your Dalhousie trip.</p>
<ul class="sza-chips"><li><b>Meadow</b> ~1,920 m</li><li><b>From Dalhousie</b> 24 km</li><li><b>Open</b> Since 16 Sep 2026</li><li><b>Tandem</b> Licensed pilot</li><li><b>Age</b> 12+ · 30 kg+</li><li><b>Price</b> Get Quote</li></ul>
<div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Add to my trip</a></div>
<div class="sza-trust"><span><a href="https://suzutravels.com/certificates/">HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022</a></span><span>Cab + hotel + activities</span><span>Reply within minutes</span></div>
</div>
</section>
<nav class="sza-nav" aria-label="On this page"><div class="sza-nav-in"><a href="#overview">Overview</a><a href="#spots">Options</a><a href="#experience">Your flight</a><a href="#season">Season</a><a href="#safety">Safety</a><a href="#booking">How booking works</a><a href="#packages">Packages</a><a href="#faq">FAQ</a><a class="cta" href="{MAIN}" target="_blank" rel="noopener">Get Quote</a></div></nav>

<section class="sza-sec" id="overview">
<span class="sza-kicker">Quick answer</span>
<h2>Paragliding near Dalhousie, at a glance</h2>
<p class="sza-answer">Yes — you can paraglide near Dalhousie, but the flying happens at Khajjiar, a meadow at about 1,920 m roughly 24 km away. Licensed tandem pilots fly between marked launch sites at Dadota and Lahara. Flights stop every monsoon (in 2026 until 15 September) and restarted on 16 September 2026. Under Himachal's aero sports rules, passengers must be at least 12 years old and 30 kg.</p>
<div class="sza-facts"><div class="sza-fact"><div class="k">Where</div><div class="v">Khajjiar meadow, Chamba district, in the Kalatop–Khajjiar sanctuary area; ~24 km from Dalhousie</div></div><div class="sza-fact"><div class="k">Height</div><div class="v">Meadow at about 1,920 m (6,300 ft)</div></div><div class="sza-fact"><div class="k">Launch sites</div><div class="v">Dadota → Lahara and Lahara → Dadota, marked by the district</div></div><div class="sza-fact"><div class="k">Season</div><div class="v">Open again since 16 Sep 2026; closed every monsoon</div></div><div class="sza-fact"><div class="k">Who can fly</div><div class="v">12 years+ and 30 kg+, tandem with a licensed pilot only</div></div><div class="sza-fact"><div class="k">Price</div><div class="v">Get Quote</div></div></div>
</section>

<section class="sza-sec alt" id="spots">
<span class="sza-kicker">Your options</span>
<h2>Ways to fly at Khajjiar</h2>
<p class="sza-lead">One meadow, four easy ways to fit it into your trip. Photos show paragliding and meadows in general, not Khajjiar itself.</p>
<div class="sza-grid">{cards}</div>
<div class="sza-media sza-choose" id="morning"><video autoplay muted loop playsinline preload="none" poster="{UP}your-khajjiar-morning-paragliding-explainer.webp" width="1600" height="900" aria-label="Your Khajjiar morning: cab from Dalhousie about 24 km and 1 hour to the Khajjiar meadow at about 1,920 m, launch at Dadota or Lahara; month bar with flying months, weather days and the monsoon closure; open again since 16 September 2026; 12+ years and 30 kg+; price on quote"><source src="{CDN}explainer.webm" type="video/webm"><source src="{CDN}explainer.mp4" type="video/mp4"></video><div><h3>Your Khajjiar morning</h3><ul><li><b>Drive</b> → Dalhousie to Khajjiar, ≈24 km, about an hour.</li><li><b>Launch</b> → Dadota or Lahara, the pilot's call on the wind.</li><li><b>Fly</b> → over the meadow and the deodar forest.</li><li><b>Monsoon</b> → closed; open again since 16 Sep 2026.</li></ul></div></div>
</section>

<section class="sza-sec" id="experience">
<span class="sza-kicker">What happens</span>
<h2>Your Khajjiar flight, step by step</h2>
<ol class="sza-steps">{steps_exp}</ol>
<div class="sza-media"><img src="{UP}paraglider-wing-inflating-grassy-field-take-off-768x1152.webp" alt="Blue paraglider wing inflating above a pilot on a sunny grassy field, the moment before take-off" loading="lazy" width="768" height="1152"><div><h3>First flight? That's normal</h3><p>No licence or experience is needed for a tandem flight. The pilot clips you in, explains the run and does all the flying; you just run a few steps and sit back.</p><p>Khajjiar is cool even in summer: wear closed shoes and a warm layer, tie long hair back and keep phones in a zipped pocket. Tell us the ages and weights in your group when you book.</p></div></div>
</section>

<section class="sza-sec alt" id="season">
<span class="sza-kicker">When to go</span>
<h2>Best time for paragliding in Khajjiar</h2>
<div class="sza-scroll"><table class="sza-tbl"><thead><tr><th>Months</th><th>Flying?</th><th>What to expect</th></tr></thead><tbody><tr><td>Mid-Sep – Nov</td><td>Yes</td><td>Reopened 16 Sep 2026; clear post-monsoon air</td></tr><tr><td>Dec – Feb</td><td>Weather days</td><td>Snow and cold fronts can stop flights — we check the week before</td></tr><tr><td>Mar – Jun</td><td>Yes</td><td>Peak months (May–Jun); busiest at the meadow</td></tr><tr><td>Monsoon (to 15 Sep)</td><td>No</td><td>The district bans flying every monsoon; the 2026 ban ran to 15 Sep</td></tr></tbody></table></div>
</section>

<div class="sza-band" id="safety"><div class="sza-band-in">
<span class="sza-kicker">Safety first</span>
<h2>What we check before we book your flight</h2>
<p class="sza-lead">Suzu Travels is an <a href="https://suzutravels.com/certificates/" style="color:#f3d98f;text-decoration:underline">HP Tourism registered travel agent (Reg. No. DTO-MND-11-243/2022)</a>. We arrange flights only with registered local operators and plan around these checks:</p>
<ul class="sza-checks"><li><b>Licensed pilot only</b>Registered operators and licensed pilots only, from notified sites (HP Aero Sports Rules 2022, amended 2025).</li><li><b>Age and weight</b>Passengers under 12 years or under 30 kg are not allowed.</li><li><b>Licence and gear</b>ABVIMAS, Manali renews tandem pilot licences after inspecting equipment at Khajjiar — ask your pilot to show the licence.</li><li><b>Monsoon ban</b>The district stops flying every rainy season; anyone flying during the ban faces action.</li><li><b>Safety standards</b>On the 2026 restart the Chamba ADM asked pilots and tourists to follow the prescribed safety standards.</li><li><b>Pilot's weather call</b>Wind or rain means the pilot can cancel or shorten a flight on the spot; we keep a buffer in your plan.</li></ul>
</div></div>

<section class="sza-sec" id="booking">
<span class="sza-kicker">How booking works</span>
<h2>Get a quote in minutes</h2>
<ol class="sza-steps">{booking}</ol>
<div class="sza-media"><img src="{UP}green-meadow-ringed-by-conifer-forest-hills-768x512.webp" alt="Lush green meadow with tall grass ringed by dark conifer forest and misty green hills under a blue sky" loading="lazy" width="768" height="512"><div><h3>What your quote depends on</h3><ul><li>Flight type and how long the day's air allows</li><li>Season and day (weekends and May–Jun are busiest)</li><li>GoPro / video add-on</li><li>Group size</li><li>Pick-up from Dalhousie, Chamba or Dharamshala, and whether you add hotel + cab — today's rate on WhatsApp within minutes</li></ul></div></div>
</section>

{reel}

<section class="sza-quote"><div><span class="sza-kicker">Ready to fly?</span><h2>Get your Khajjiar flight quote</h2><p>Tell us your travel date and group size. We reply with today's rate for your date within minutes — and can add your stay and cab in Dalhousie or Dharamshala.</p></div><div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan full trip</a></div></section>

<section class="sza-sec" id="packages">
<span class="sza-kicker">Make it a trip</span>
<h2>Dalhousie, Khajjiar and Dharamshala</h2>
<p>Most guests fly on a <b>Dharamshala–Dalhousie trip with a Khajjiar morning</b>. See our <a href="/himachal-tour-package-5-nights-6-days/">Himachal 5 nights 6 days package</a> (Dharamshala–Dalhousie with Khajjiar), the <a href="/dharamshala-tour-package-from-delhi/">Dharamshala tour package from Delhi</a>, read the <a href="/dalhousie/">Dalhousie guide</a> or <a href="/dharamshala-vs-dalhousie/">Dharamshala vs Dalhousie</a>. Need only a cab? Book a <a href="/cabs/pathankot-to-dharamshala-taxi/">Pathankot to Dharamshala taxi</a> or a <a href="/cabs/dharamshala-taxi-service/">Dharamshala taxi</a>.</p>
<div class="sza-btns" style="margin-top:18px">{walink("Dharamshala–Dalhousie + Khajjiar flight — Get Quote", what="a Dharamshala–Dalhousie trip with a Khajjiar paragliding flight")}{walink("Dalhousie day trip + flight — Get Quote", what="a Dalhousie–Khajjiar day trip with a paragliding flight", cls="sza-btn line")}</div>
</section>

<section class="sza-sec sza-faq" id="faq">
<span class="sza-kicker">FAQ</span>
<h2>Paragliding in Khajjiar and Dalhousie — questions</h2>
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
