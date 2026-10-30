#!/usr/bin/env python3
# Generates adventure-kit/pages/buran-ghati-trek.html (Page Builder morning, 30 Oct 2026)
import urllib.parse, pathlib
SLUG = "buran-ghati-trek"
HERE = pathlib.Path(__file__).resolve().parent
CDN = "https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@050e0aa3ec38c7dd47a12ac4030e68d8d845e0cd/adventure-kit/media/buran-ghati-trek/"
UP = "https://suzutravels.com/wp-content/uploads/"
QUOTE = "/himachal-tour-packages-quote/?activity=" + urllib.parse.quote("Buran Ghati trek")
WHAT = "the Buran Ghati trek (Janglik to Barua)"

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
    card(f"{UP}2026/10/trekkers-roped-gear-snow-ridge-line-768x512.webp", 768, 512,
         "Line of trekkers with backpacks, harnesses and ice axes walking up a snow-covered ridge under a cloudy sky",
         "Classic pick", "Classic 7-day crossover", "<b>Janglik → Barua · about 37–44 km</b>",
         "Janglik, Dayara meadow, Litham, Chandranahan lake, Dhunda, the pass and down the snow slope to Barua in the Sangla valley.",
         "the classic 7-day Buran Ghati crossover (Janglik to Barua)"),
    card(f"{UP}2026/10/dome-tents-hilltop-meadow-sunrise-768x498.webp", 768, 498,
         "Red, blue and orange dome tents on a grassy hilltop meadow at sunrise, with layered blue mountain ridges behind",
         "Safer pick", "8 days with a buffer", "<b>Same route + 1 spare day</b>",
         "One extra day at Dhunda so the group can wait out fresh snow or bad weather before the pass.",
         "the 8-day Buran Ghati trek with a buffer day"),
    card(f"{UP}2026/10/trek-camp-tents-meadow-close-768x1024.webp", 768, 1024,
         "Grey and pink trek tents on a mountain meadow with a sunlit ridge behind",
         "Easier", "Dayara + Chandranahan only", "<b>Out and back · no pass</b>",
         "A shorter trek to the Dayara meadow and the Chandranahan lake and back to Janglik, without the roped snow descent.",
         "a shorter Dayara meadow and Chandranahan lake trek from Janglik (no pass)"),
    card(f"{UP}2026/10/turquoise-glacial-lake-boulders-snow-768x1024.webp", 768, 1024,
         "Small turquoise glacial lake ringed by boulders below snow-streaked peaks",
         "Day 4", "Chandranahan lake", "<b>About 4,000 m · source of the Pabbar</b>",
         "The acclimatisation-day walk from Litham to the high glacial lake that feeds the Pabbar river, then back to camp.",
         "the Buran Ghati trek with the Chandranahan lake day"),
    card(f"{UP}2024/12/kalpa-himachal-pradesh-v0-ftkl4glp20sd1-1-768x512.webp", 768, 512,
         "Kalpa village in Kinnaur, Himachal Pradesh, below the Kinner Kailash range",
         "Make it a package", "Crossover + Kinnaur stay", "<b>Finish at Barua, then hotel nights</b>",
         "Walk out at Barua and stay on in Sangla, Chitkul or Kalpa before the drive back to Shimla.",
         "the Buran Ghati trek plus hotel nights in Sangla, Chitkul or Kalpa"),
])

steps_exp = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Send your dates", "WhatsApp your dates, group size and past treks — we check the snow and the forest-permit paperwork."),
    ("Day 1: drive to Janglik", "Cab Shimla → Rohru → Chirgaon → Janglik, about 150–160 km and a full day; the last stretch is rough and slow."),
    ("Days 2–3: Dayara and Litham", "Up through forest to the wide Dayara meadow, then on to the Litham camp."),
    ("Day 4: Chandranahan lake", "Acclimatisation walk to the glacial lake that feeds the Pabbar river, and back to camp."),
    ("Days 5–6: Dhunda and the pass", "Climb to Dhunda, then the long pass day (9–10 hours) over about 4,575 m and down the roped snow slope to the river camp."),
    ("Day 7: Barua and the cab", "Down to Barua in the Sangla valley; our cab takes you to Sangla or back to Shimla via Karcham and Rampur."),
])

booking = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Tell us your dates", "WhatsApp or the quote form — dates, group size, start city and trek experience."),
    ("We check your date", "Snow on the pass, the season, the forest permit and a guided team with a registered local operator."),
    ("You get one quote", "Guided trek, camps, hotel nights and the cabs at both ends in one plan."),
    ("Confirm and go", "We send the reporting time, the kit list and the latest snow status before you travel."),
])

faqs = [
    ("How high is Buran Ghati?", "About 4,575 m (15,000 ft). Sources give 4,550–4,590 m for the pass."),
    ("How long is the Buran Ghati trek?", "About 37–44 km over 5–6 walking days, or 7–8 days in all including the drives at both ends."),
    ("Where does the trek start and end?", "It starts at Janglik village above Rohru, about 150–160 km from Shimla, and ends at Barua village in the Sangla valley, Kinnaur."),
    ("What is the best time for Buran Ghati?", "May–June, when the snow wall forms below the pass, and September–October after the monsoon. It is not run in the monsoon or in winter."),
    ("Is the Buran Ghati trek difficult?", "Moderate to difficult. The pass day is 9–10 hours with a steep roped snow descent, so it is not a first trek — prior multi-day trekking helps."),
    ("What is the snow wall?", "A steep snow slope just below the pass on the Kinnaur side. Guides fix a rope and you slide or rappel down it in a harness."),
    ("What is Chandranahan lake?", "A high glacial lake at about 4,000 m above Litham, the source of the Pabbar river, visited on the acclimatisation day."),
    ("Do I need a permit, and what does it cost?", "Yes, a forest permit, arranged through the operator with each trekker's ID and a medical certificate. The total depends on days, group, season and stays — send your dates and we share today's rate in minutes. Get Quote."),
]
faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)

more = [
    ("/adventure/hampta-pass-trek/", "🏔️", "Hampta Pass Trek", "Another crossover, Kullu to Lahaul"),
    ("/adventure/sar-pass-trek/", "❄️", "Sar Pass Trek", "Snow pass above Kasol"),
    ("/adventure/churdhar-trek/", "⛰️", "Churdhar Trek", "Summit shrine near Shimla"),
    ("/adventure/camping-in-himachal/", "⛺", "Camping in Himachal", "Riverside and forest camps"),
    ("/adventure/snow-and-skiing-in-narkanda/", "🎿", "Snow in Narkanda", "On the drive from Shimla"),
    ("/adventure/", "🧭", "All adventures", "Air · Water · Snow · Land"),
]
more_html = "".join(f'<a class="sza-cat" href="{h}"><span class="ic">{i}</span><span class="n">{n}</span><span class="c">{c}</span></a>' for h, i, n, c in more)

reel = (HERE.parent / "media" / SLUG / "reel-section.html").read_text(encoding="utf-8").strip()

page = f'''<!-- buran-ghati-trek — built by Page Builder (morning) 30 Oct 2026 from the Research Lead brief 30 Oct + Visual Studio media @050e0aa (reel-section @69c645d). Kit v1.8. No prices, no operator names; heights/distances as ranges; no age limit (varies by operator); Chanshal/Dodra Kwar left off; badge "Most booked" → "Classic pick" (kit v1.7). Photos generic with neutral alt except Kalpa (real). -->
<style>.sza-bgt .sza-hero-in>*{{max-width:620px}}.sza-bgt .sza-chips{{max-width:700px}}.sza-bgt #experience .sza-steps{{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}.sza-bgt .sza-media ul{{padding-left:20px;list-style:disc;margin:0}}.sza-bgt .sza-media ul li{{margin:0 0 8px}}.sza-bgt .sza-media img{{height:auto;aspect-ratio:4/3;object-fit:cover}}.sza-bgt .sza-media video{{height:auto;aspect-ratio:16/9}}.sza-bgt #spots .sza-grid{{grid-template-columns:repeat(auto-fit,minmax(220px,1fr))}}.sza-bgt #spots .sza-card .img img{{aspect-ratio:3/2;object-fit:cover}}.sza-bgt .sza-facts{{grid-template-columns:repeat(auto-fit,minmax(280px,1fr))}}.sza-bgt .sza-checks{{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}.sza-bgt .sza-status{{display:inline-block;background:rgba(243,217,143,.16);border:1px solid rgba(243,217,143,.5);color:#f3d98f;border-radius:10px;padding:6px 12px;font-size:14px;margin:0 0 12px}}@media(min-width:821px){{.sza-bgt .sza-hero:after{{background:linear-gradient(90deg,rgba(11,31,51,.8) 0%,rgba(11,31,51,.5) 48%,rgba(11,31,51,.08) 72%),linear-gradient(180deg,rgba(11,31,51,.05) 0%,rgba(11,31,51,.55) 100%)}}}}@media(max-width:820px){{.sza-bgt .sza-hero video{{object-position:20% 50%}}.sza-bgt .sza-hero:after{{background:linear-gradient(180deg,rgba(11,31,51,.35) 0%,rgba(11,31,51,.6) 40%,rgba(11,31,51,.94) 100%)}}}}</style>
<div class="sza sza-bgt">
<section class="sza-hero">
<video autoplay muted loop playsinline preload="metadata" poster="{UP}2026/10/buran-ghati-trek-hero-poster.webp" aria-label="Meadow tents at sunrise, a glacial lake, trekkers on a snow ridge and Kalpa village in Kinnaur, with a gold altitude profile from Janglik past Dhunda over the pass of about 4,575 m down to Barua"><source src="{CDN}hero.webm" type="video/webm"><source src="{CDN}hero.mp4" type="video/mp4"></video>
<div class="sza-hero-in">
<span class="sza-kicker">Treks &amp; Camps · Rohru to Sangla</span>
<p class="sza-hero-tag">Cross from Shimla's apple valleys into Kinnaur on foot.</p>
<p class="sza-hero-sub">7–8 days from Janglik over Buran Ghati (about 4,575 m) and down to Barua near Sangla — cab, guided trek and Kinnaur stays in one quote.</p>
<p class="sza-status">Update 30 Oct 2026: the pass is under snow until late spring; next season May–June 2027.</p>
<ul class="sza-chips"><li><b>Pass</b> ~4,575 m</li><li><b>Distance</b> ~37–44 km</li><li><b>Days</b> 7–8</li><li><b>Season</b> May–Jun · Sep–Oct</li><li><b>Grade</b> Moderate–difficult</li><li><b>Price</b> Get Quote</li></ul>
<div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan my trip</a></div>
<div class="sza-trust"><span><a href="https://suzutravels.com/certificates/">HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022</a></span><span>Guided trek + stays + cab</span><span>Reply within minutes</span></div>
</div>
</section>
<nav class="sza-nav" aria-label="On this page"><div class="sza-nav-in"><a href="#overview">Overview</a><a href="#spots">Options</a><a href="#experience">Day by day</a><a href="#season">Best time</a><a href="#safety">Safety</a><a href="#booking">How booking works</a><a href="#packages">Packages</a><a href="#faq">FAQ</a><a class="cta" href="{MAIN}" target="_blank" rel="noopener">Get Quote</a></div></nav>

<section class="sza-sec" id="overview">
<span class="sza-kicker">Quick answer</span>
<h2>Buran Ghati trek, at a glance</h2>
<p class="sza-answer">Buran Ghati is a 7–8 day crossover trek from Janglik village above Rohru (Shimla district) over a pass of about 4,575 m to Barua in Kinnaur's Sangla valley. You camp at Dayara meadow, Litham and Dhunda, visit Chandranahan lake, then descend a steep snow slope on a fixed rope. It runs May–June and September–October.</p>
<div class="sza-facts"><div class="sza-fact"><div class="k">Start</div><div class="v">Janglik (about 2,800 m), about 150–160 km from Shimla via Rohru and Chirgaon — a full day's drive, rough after Chirgaon</div></div><div class="sza-fact"><div class="k">Highest point</div><div class="v">Buran Ghati, about 4,575 m (15,000 ft)</div></div><div class="sza-fact"><div class="k">Distance &amp; days</div><div class="v">About 37–44 km over 5–6 walking days; 7–8 days from Shimla</div></div><div class="sza-fact"><div class="k">Camps</div><div class="v">Dayara (~3,400 m) · Litham (~3,550 m) · Dhunda (~4,000 m) · river camp at Munirang (~3,350 m) · end at Barua (~2,400 m)</div></div><div class="sza-fact"><div class="k">Season</div><div class="v">May–June (snow wall) and September–October; not in the monsoon or winter</div></div><div class="sza-fact"><div class="k">Price</div><div class="v">Get Quote</div></div></div>
</section>

<section class="sza-sec alt" id="spots">
<span class="sza-kicker">Trek options</span>
<h2>Choose your Buran Ghati plan</h2>
<p class="sza-lead">Pick the length that suits your group and your trekking experience. Photos show Himalayan treks in general, plus Kalpa in Kinnaur.</p>
<div class="sza-grid">{cards}</div>
</section>

<section class="sza-sec" id="experience">
<span class="sza-kicker">Day by day</span>
<h2>Your Buran Ghati trek, step by step</h2>
<ol class="sza-steps">{steps_exp}</ol>
<div class="sza-media"><video autoplay muted loop playsinline preload="none" poster="{CDN}explainer-poster.webp" width="1600" height="900" aria-label="Schematic, not to scale: cab from Shimla to Rohru and Janglik, then on foot to Dayara, Litham with a day 4 spur to Chandranahan lake, Dhunda, Buran Ghati, Munirang and Barua, and a cab to Sangla, with a day counter from 1 to 7 and a height line rising to about 4,575 m"><source src="{CDN}explainer.webm" type="video/webm"><source src="{CDN}explainer.mp4" type="video/mp4"></video><div><h3>Shimla to Kinnaur, on foot</h3><ul><li><b>By cab</b> → Shimla → Rohru → Chirgaon → Janglik.</li><li><b>On foot</b> → Dayara → Litham (+ Chandranahan lake) → Dhunda → Buran Ghati → Munirang → Barua.</li><li><b>By cab</b> → Barua → Sangla, or back to Shimla via Karcham and Rampur.</li><li><b>Next season</b> May–June 2027.</li></ul></div></div>
</section>

<section class="sza-sec alt" id="season">
<span class="sza-kicker">When to go</span>
<h2>Best time for the Buran Ghati trek</h2>
<div class="sza-scroll"><table class="sza-tbl"><thead><tr><th>Months</th><th>Conditions</th><th>Our advice</th></tr></thead><tbody><tr><td>May – June</td><td>Snow on the pass; the snow wall forms on the Kinnaur side</td><td>Main season; roped descent</td></tr><tr><td>July – August</td><td>Monsoon</td><td>Not run</td></tr><tr><td>September – October</td><td>Less snow, clear skies, cold nights</td><td>Second window</td></tr><tr><td>November – April</td><td>Heavy snow</td><td>Closed</td></tr></tbody></table></div>
<p style="margin-top:14px">Planning for early May or late October? Send your dates — we check the snow on the pass with the operator before we book.</p>
</section>

<div class="sza-band" id="safety"><div class="sza-band-in">
<span class="sza-kicker">Safety</span>
<h2>What we check before we book your trek</h2>
<p class="sza-lead">Suzu Travels is an <a href="https://suzutravels.com/certificates/" style="color:#f3d98f;text-decoration:underline">HP Tourism registered travel agent (Reg. No. DTO-MND-11-243/2022)</a>. We arrange the trek with registered local operators and plan around these checks:</p>
<ul class="sza-checks"><li><b>Experience</b>Not a first trek. We ask about your past multi-day treks and fitness — operators usually ask for about a 5 km run in 25–30 minutes.</li><li><b>Forest permit</b>Arranged through the operator with each trekker's government ID and a medical certificate.</li><li><b>Guide, rope and harness</b>A trained guide fixes the rope for the snow descent; the team turns back if the snow is unsafe.</li><li><b>Altitude</b>The acclimatisation day at Litham and Chandranahan lake is never skipped.</li><li><b>Network and help</b>Mobile signal only up to around Janglik and Dayara; the nearest hospital and ATM are at Rohru.</li><li><b>Weather</b>No crossing in fresh snow or rain — which is why we suggest a buffer day.</li></ul>
</div></div>

<section class="sza-sec" id="booking">
<span class="sza-kicker">How booking works</span>
<h2>Get a quote in minutes</h2>
<ol class="sza-steps">{booking}</ol>
<div class="sza-media"><img src="{UP}2026/10/trekker-crampons-fixed-rope-snow-slope-768x1024.webp" alt="Trekker with a backpack and crampons walking up a steep snow slope beside a yellow fixed rope under a blue sky" loading="lazy" width="768" height="1024"><div><h3>What your quote depends on</h3><ul><li>Start city — Shimla, Chandigarh or Delhi — and the return drive from Barua</li><li>7 or 8 days (with a buffer day)</li><li>Group size; guide, porter or mule, tents and meals</li><li>Season — May–June is the peak</li><li>Hotel nights before and after in Shimla, Sangla, Chitkul or Kalpa</li></ul></div></div>
</section>

{reel}

<section class="sza-quote"><div><span class="sza-kicker">Ready to cross into Kinnaur?</span><h2>Get your Buran Ghati trek quote</h2><p>Tell us your dates, group size and trek experience. We reply with one plan — guided trek, stays and the cabs — within minutes.</p></div><div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan full trip</a></div></section>

<section class="sza-sec" id="packages">
<span class="sza-kicker">Make it a trip</span>
<h2>Shimla + Buran Ghati + Sangla and Kalpa</h2>
<p>The trek ends in the Sangla valley, so it pairs naturally with Kinnaur: <b>Shimla (1 night) → Buran Ghati trek (7 days) → Sangla or Chitkul (2 nights) → Kalpa → Shimla</b>. Read our <a href="/sangla-valley-and-chitkul-kinnaur-trip-guide/">Sangla and Chitkul trip guide</a> and <a href="/kalpa-in-winter/">Kalpa guide</a>, see our <a href="/destination/shimla-tour-packages/">Shimla tour packages</a>, or book a <a href="/cabs/delhi-to-shimla-taxi/">Delhi to Shimla taxi</a>, a <a href="/cabs/chandigarh-to-shimla-taxi/">Chandigarh to Shimla taxi</a> or a <a href="/cabs/shimla-taxi-service/">Shimla taxi</a> for the drive to Janglik.</p>
<div class="sza-btns" style="margin-top:18px">{walink("Shimla + Buran Ghati + Kinnaur — Get Quote", what="a Shimla + Buran Ghati trek + Sangla/Chitkul and Kalpa package")}{walink("Trek only — Get Quote", what="the Buran Ghati trek only, with cabs to Janglik and from Barua", cls="sza-btn line")}</div>
</section>

<section class="sza-sec sza-faq" id="faq">
<span class="sza-kicker">FAQ</span>
<h2>Buran Ghati trek — questions</h2>
{faq_html}
</section>

<section class="sza-sec alt" id="more">
<span class="sza-kicker">More adventures</span>
<h2>Explore more treks in Himachal</h2>
<div class="sza-cats">{more_html}</div>
</section>
</div>
'''
out = HERE / f"{SLUG}.html"
out.write_text(page, encoding="utf-8")
print(len(page))
