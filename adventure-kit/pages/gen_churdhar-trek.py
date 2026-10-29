#!/usr/bin/env python3
# Generates adventure-kit/pages/churdhar-trek.html (Page Builder night, 30 Oct 2026)
import urllib.parse, pathlib
SLUG = "churdhar-trek"
HERE = pathlib.Path(__file__).resolve().parent
CDN = "https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@fd941ab71967cbc01be6046b19c67433ca96941c/adventure-kit/media/churdhar-trek/"
UP = "https://suzutravels.com/wp-content/uploads/2026/10/"
QUOTE = "/himachal-tour-packages-quote/?activity=" + urllib.parse.quote("Churdhar trek")
WHAT = "the Churdhar trek (Sirmaur)"

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
    card(f"{UP}misty-forest-trail-tall-conifers-768x1152.webp", 768, 1152,
         "Narrow dirt trail running between tall conifer trees in a misty forest",
         "Classic route", "Nohradhar route", "<b>About 14–18 km one way · usually 2 days</b>",
         "The classic forest climb from the Sirmaur side (via Solan and Rajgarh). Night near the temple, summit at dawn.",
         "the Churdhar trek by the Nohradhar route"),
    card(f"{UP}hikers-footbridge-forest-trail-himalaya-768x1152.webp", 768, 1152,
         "Two hikers crossing a wooden footbridge over a rushing stream on a forest trail in the Himalaya",
         "Shortest walk", "Sarain (Chaupal) route", "<b>About 7–10 km one way</b>",
         "The shorter climb from the Shimla side, via Theog and Chaupal. Good for a tight weekend; fit walkers do it in a long day.",
         "the Churdhar trek by the Sarain (Chaupal) route"),
    card(f"{UP}stone-hut-pine-forest-himachal-768x1365.webp", 768, 1365,
         "Walker resting beside a stone hut among tall pine trees in a misty Himachal forest",
         "Temple", "Shirgul Maharaj temple", "<b>Just below the summit</b>",
         "The shrine of Shirgul Maharaj, revered across Sirmaur and Chaupal. Its doors close for winter and reopen on Baisakhi in April.",
         "the Churdhar trek to the Shirgul Maharaj temple"),
    card(f"{UP}rocky-summit-cairn-flags-above-clouds-768x1024.webp", 768, 1024,
         "Stone cairn with saffron flags on a rocky mountain top above a sea of white cloud under a blue sky",
         "Sunrise", "Summit &amp; sunrise", "<b>3,647 m (11,965 ft)</b>",
         "A pre-dawn walk from the temple to the rocky top. On clear days you look over the Shivaliks to the snow line of the Great Himalaya.",
         "the Churdhar trek with a sunrise summit"),
    card(f"{UP}snow-capped-himalayan-peaks-clouds-forested-ridges-768x512.webp", 768, 512,
         "Snow-capped Himalayan peaks breaking through white clouds above dark forested ridges",
         "Wildlife", "Churdhar Sanctuary", "<b>About 56 km², notified 1985</b>",
         "The whole trail runs through the sanctuary: deodar and oak forest, home to musk deer, black bear, leopard and langur.",
         "the Churdhar trek through the Churdhar Sanctuary"),
])

steps_exp = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Send your dates", "WhatsApp your dates, group and where you start — Chandigarh or Solan suits Nohradhar, Shimla suits Sarain."),
    ("We check the status", "We confirm the trek and temple are open for your dates and arrange a guide with a registered local operator."),
    ("Drive to the trailhead", "Our cab takes you to Nohradhar or Sarain early in the morning."),
    ("Day 1: up through the forest", "A long, steady climb through deodar and oak forest to the temple area, where you stay the night (camp or temple-area stay on request)."),
    ("Day 2: summit at sunrise", "A pre-dawn walk to the 3,647 m top for sunrise, then down to the trailhead by afternoon."),
    ("Back, or one more night", "Cab back home, or add a night in Shimla, Chail or Narkanda."),
])

booking = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Tell us your dates", "WhatsApp or the quote form — dates, group size, which side you come from."),
    ("We check your date", "Season, the winter closure, and a guide with a registered local operator."),
    ("You get one quote", "Guide, trek stay, hotel nights and the cab in one plan."),
    ("Confirm and go", "We send the reporting time, what to carry and the latest trail status before you travel."),
])

faqs = [
    ("How high is Churdhar?", "Churdhar peak is 3,647 m (11,965 ft), the highest point in Sirmaur district and the highest peak of the outer Himalaya."),
    ("How long is the Churdhar trek?", "From Nohradhar it is about 14–18 km one way and usually takes 2 days. From Sarain on the Chaupal side it is about 7–10 km one way."),
    ("Which route is best, Nohradhar or Sarain?", "Nohradhar is the classic forest route if you come from Chandigarh, Solan or Rajgarh. Sarain is shorter and better if you come from Shimla."),
    ("Is Churdhar open in December?", "No. The district administration usually bans the trek from about 1 December until the temple reopens on Baisakhi in April. We confirm the order in force for your dates."),
    ("What is the best time for the Churdhar trek?", "May–June and September–November. Avoid the July–August monsoon, when the trail has fog, mud, leeches and slides."),
    ("Is there an entry fee for Churdhar?", "Yes. The sanctuary collects trek, temple and camping fees at the Nohradhar, Sarain and Pulbahal entry points. We include them in your quote."),
    ("Can beginners do the Churdhar trek?", "Yes, if you are fit. It is a long, steady climb of over 1,500 m, not a technical one, with a rocky last stretch. Take 3 days if you are new to the hills."),
    ("What does the Churdhar trek cost?", "It depends on the route, the number of days, the guide, the stay and your cab. Send your dates on WhatsApp and we share today's rate in minutes — Get Quote."),
]
faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)

more = [
    ("/adventure/adventure-activities-in-shimla/", "🏔️", "Adventure in Shimla", "Treks, paragliding, rafting"),
    ("/adventure/prashar-lake-trek/", "⛰️", "Prashar Lake Trek", "An easy lake trek near Mandi"),
    ("/adventure/serolsar-lake-trek/", "🌲", "Serolsar Lake Trek", "Forest walk from Jalori Pass"),
    ("/adventure/camping-in-himachal/", "⛺", "Camping in Himachal", "Riverside and forest camps"),
    ("/mountains-of-india/himachal-pradesh/", "🗻", "Peaks of Himachal", "The state's mountains, by height"),
    ("/adventure/", "🧭", "All adventures", "Air · Water · Snow · Land"),
]
more_html = "".join(f'<a class="sza-cat" href="{h}"><span class="ic">{i}</span><span class="n">{n}</span><span class="c">{c}</span></a>' for h, i, n, c in more)

reel = (HERE.parent / "media" / SLUG / "reel-section.html").read_text(encoding="utf-8").strip()

page = f'''<!-- churdhar-trek — built by Page Builder (night) 30 Oct 2026 from the Research Lead brief 29 Oct + Visual Studio media @fd941ab (reel-section @26716c6). Kit v1.8. No prices, no operator names; distances as ranges; winter closure "usually from about 1 December", no fixed order date; fees mentioned without amounts; Pulbahal named only as an entry point. Photos generic, neutral alt. -->
<style>.sza-chd .sza-hero-in>*{{max-width:620px}}.sza-chd .sza-chips{{max-width:700px}}.sza-chd #experience .sza-steps{{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}.sza-chd .sza-media ul{{padding-left:20px;list-style:disc;margin:0}}.sza-chd .sza-media ul li{{margin:0 0 8px}}.sza-chd .sza-media img{{height:auto;aspect-ratio:4/3;object-fit:cover}}.sza-chd .sza-media video{{height:auto;aspect-ratio:16/9}}.sza-chd #spots .sza-grid{{grid-template-columns:repeat(auto-fit,minmax(220px,1fr))}}.sza-chd #spots .sza-card .img img{{aspect-ratio:3/2;object-fit:cover}}.sza-chd .sza-checks{{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}@media(max-width:820px){{.sza-chd .sza-hero video{{object-position:20% 50%}}.sza-chd .sza-hero:after{{background:linear-gradient(180deg,rgba(11,31,51,.35) 0%,rgba(11,31,51,.6) 40%,rgba(11,31,51,.94) 100%)}}}}</style>
<div class="sza sza-chd">
<section class="sza-hero">
<video autoplay muted loop playsinline preload="metadata" poster="{UP}churdhar-trek-hero-poster.webp" aria-label="Misty conifer forest trail, a stone hut in pine forest, a cairn with flags above the clouds and a hiker above a cloud valley, with a gold altitude profile from Nohradhar past the temple to the 3,647 m summit and down the Sarain side"><source src="{CDN}hero.webm" type="video/webm"><source src="{CDN}hero.mp4" type="video/mp4"></video>
<div class="sza-hero-in">
<span class="sza-kicker">Highest peak of the outer Himalaya · Sirmaur</span>
<p class="sza-hero-tag">Cedar forest to a 3,647 m summit shrine.</p>
<p class="sza-hero-sub">A 2-day guided trek from Nohradhar or Sarain; we add your hotel and cab from Chandigarh, Shimla or Delhi.</p>
<ul class="sza-chips"><li><b>Peak</b> 3,647 m</li><li><b>Days</b> 1–2 (3 easy)</li><li><b>Nohradhar</b> ~14–18 km one way</li><li><b>Sarain</b> ~7–10 km</li><li><b>Open</b> ~Apr–Nov</li><li><b>Price</b> Get Quote</li></ul>
<div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan my trip</a></div>
<div class="sza-trust"><span><a href="https://suzutravels.com/certificates/">HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022</a></span><span>Guide + stay + cab</span><span>Reply within minutes</span></div>
</div>
</section>
<nav class="sza-nav" aria-label="On this page"><div class="sza-nav-in"><a href="#overview">Overview</a><a href="#spots">Routes</a><a href="#experience">How the trek runs</a><a href="#season">Best time</a><a href="#safety">Safety</a><a href="#booking">How booking works</a><a href="#packages">Packages</a><a href="#faq">FAQ</a><a class="cta" href="{MAIN}" target="_blank" rel="noopener">Get Quote</a></div></nav>

<section class="sza-sec" id="overview">
<span class="sza-kicker">Quick answer</span>
<h2>Churdhar trek, at a glance</h2>
<p class="sza-answer">Churdhar (3,647 m) is the highest peak of the outer Himalaya and the home of Shirgul Maharaj, in Sirmaur's Churdhar Sanctuary. You trek from Nohradhar (about 14–18 km one way, 2 days) or the shorter Sarain–Chaupal side (about 7–10 km). It is open roughly from Baisakhi in April to late November; the trek is usually banned from about 1 December.</p>
<div class="sza-facts"><div class="sza-fact"><div class="k">Height</div><div class="v">3,647 m (11,965 ft) — the highest point in Sirmaur and in the outer Himalaya</div></div><div class="sza-fact"><div class="k">Routes</div><div class="v">Nohradhar (Sirmaur, via Solan and Rajgarh) · Sarain (Chaupal, via Theog) · Pulbahal (third entry point)</div></div><div class="sza-fact"><div class="k">Days &amp; distance</div><div class="v">Nohradhar about 14–18 km one way, usually 2 days; Sarain about 7–10 km, a long day for fit walkers</div></div><div class="sza-fact"><div class="k">Difficulty</div><div class="v">Easy–moderate: a long, steady climb of over 1,500 m; the last stretch is rocky</div></div><div class="sza-fact"><div class="k">Best months</div><div class="v">May–June and September–November; closed from about 1 December to Baisakhi (April)</div></div><div class="sza-fact"><div class="k">Price</div><div class="v">Get Quote</div></div></div>
</section>

<section class="sza-sec alt" id="spots">
<span class="sza-kicker">Routes &amp; highlights</span>
<h2>Two ways up Churdhar, and what you see</h2>
<p class="sza-lead">Pick the route that suits where you start from. Photos show Himalayan forests and peaks in general.</p>
<div class="sza-grid">{cards}</div>
</section>

<section class="sza-sec" id="experience">
<span class="sza-kicker">How the trek runs</span>
<h2>Your Churdhar trek, step by step</h2>
<ol class="sza-steps">{steps_exp}</ol>
<div class="sza-media"><video autoplay muted loop playsinline preload="none" poster="{CDN}explainer-poster.webp" width="1600" height="900" aria-label="Schematic, not to scale: Chandigarh to Solan, Rajgarh and Nohradhar for the long route of about 14 to 18 km, and Shimla to Theog, Chaupal and Sarain for the short route of about 7 to 10 km, both meeting at the 3,647 m peak; a month strip shows the trek closed from about 1 December to Baisakhi"><source src="{CDN}explainer.webm" type="video/webm"><source src="{CDN}explainer.mp4" type="video/mp4"></video><div><h3>Two ways up to 3,647 m</h3><ul><li><b>Long route</b> → Chandigarh → Solan → Rajgarh → Nohradhar, then about 14–18 km on foot.</li><li><b>Short route</b> → Shimla → Theog → Chaupal → Sarain, then about 7–10 km on foot.</li><li><b>Both</b> meet near the Shirgul Maharaj temple, just below the top.</li><li><b>Closed</b> from about 1 December until Baisakhi in April.</li></ul></div></div>
</section>

<section class="sza-sec alt" id="season">
<span class="sza-kicker">When to go</span>
<h2>Best time for the Churdhar trek</h2>
<div class="sza-scroll"><table class="sza-tbl"><thead><tr><th>Months</th><th>Trail</th><th>Good for</th></tr></thead><tbody><tr><td>Mid-April (Baisakhi)</td><td>Temple reopens; snow patches near the top</td><td>First treks of the year</td></tr><tr><td>May – June</td><td>Clear, mild, busiest weekends</td><td>Classic season</td></tr><tr><td>July – August</td><td>Monsoon: fog, mud, leeches, slides</td><td>Avoid, or only with a guide</td></tr><tr><td>September – November</td><td>Clear views, cold nights, quieter</td><td>Best views</td></tr><tr><td>December – Baisakhi</td><td>Snow; trek banned by the district administration</td><td>Closed</td></tr></tbody></table></div>
<p style="margin-top:14px">Planning for late November or April? Send your dates — we check the closure order and the temple dates for that year before we book.</p>
</section>

<div class="sza-band" id="safety"><div class="sza-band-in">
<span class="sza-kicker">Safety</span>
<h2>What we check before we book your trek</h2>
<p class="sza-lead">Suzu Travels is an <a href="https://suzutravels.com/certificates/" style="color:#f3d98f;text-decoration:underline">HP Tourism registered travel agent (Reg. No. DTO-MND-11-243/2022)</a>. We arrange the guide with registered local operators and plan around these checks:</p>
<ul class="sza-checks"><li><b>Winter ban</b>The Sirmaur administration usually closes the trek from about 1 December until Baisakhi, and walking it then can bring legal action. We confirm the order for your dates.</li><li><b>Sanctuary fees</b>Trek, temple and camping fees are collected at Nohradhar, Sarain and Pulbahal. We include them in your quote.</li><li><b>Fog in the forest</b>People do get lost in fog. Stay on the main trail, go with a guide, and start down by early afternoon.</li><li><b>Weather near the top</b>It turns fast even in May — carry a warm layer, a rain shell and a torch.</li><li><b>Patchy signal</b>Phone signal is weak in the forest; do not rely on GPS alone.</li><li><b>Temple customs</b>No alcohol on the trek, and follow the footwear rules at the shrine.</li></ul>
</div></div>

<section class="sza-sec" id="booking">
<span class="sza-kicker">How booking works</span>
<h2>Get a quote in minutes</h2>
<ol class="sza-steps">{booking}</ol>
<div class="sza-media"><img src="{UP}hiker-rock-above-cloud-valley.webp" alt="Hiker sitting on a rock outcrop above a valley filled with low white cloud, forested ridges behind" loading="lazy" width="1920" height="1272"><div><h3>What your quote depends on</h3><ul><li>Route — Nohradhar or Sarain — and 1, 2 or 3 days</li><li>Group size; guide only, or guide + camp</li><li>Stay on the trek, and hotel nights before or after in Solan, Shimla or Chail</li><li>Cab from Chandigarh, Shimla or Delhi and back</li><li>Month — shoulder season or May–June weekends; gear on request</li></ul></div></div>
</section>

{reel}

<section class="sza-quote"><div><span class="sza-kicker">Ready for the summit?</span><h2>Get your Churdhar trek quote</h2><p>Tell us your dates and group size. We reply with one plan — guide, stay and the cab — for your dates within minutes.</p></div><div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan full trip</a></div></section>

<section class="sza-sec" id="packages">
<span class="sza-kicker">Make it a trip</span>
<h2>Churdhar + Shimla, Chail or Narkanda</h2>
<p>Two plans work well: <b>Chandigarh → Churdhar by Nohradhar (2 days) + 2 nights in Shimla or Chail</b>, or <b>Shimla + Churdhar by Sarain (3 nights)</b>. See our <a href="/destination/shimla-tour-packages/">Shimla tour packages</a>, book a <a href="/cabs/chandigarh-to-shimla-taxi/">Chandigarh to Shimla taxi</a>, a <a href="/cabs/delhi-to-shimla-taxi/">Delhi to Shimla taxi</a> or a <a href="/cabs/shimla-taxi-service/">Shimla taxi</a> for the trailhead, or add more from our <a href="/adventure/adventure-activities-in-shimla/">adventure activities in Shimla</a>. Curious about the state's other summits? See the <a href="/mountains-of-india/himachal-pradesh/">mountains of Himachal Pradesh</a>.</p>
<div class="sza-btns" style="margin-top:18px">{walink("Chandigarh + Churdhar — Get Quote", what="a Chandigarh to Churdhar (Nohradhar) 2-day trek with 2 nights in Shimla or Chail")}{walink("Shimla + Churdhar — Get Quote", what="a Shimla trip with the Churdhar trek via Sarain (3 nights)", cls="sza-btn line")}</div>
</section>

<section class="sza-sec sza-faq" id="faq">
<span class="sza-kicker">FAQ</span>
<h2>Churdhar trek — questions</h2>
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
