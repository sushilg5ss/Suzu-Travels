#!/usr/bin/env python3
"""trekking-in-manali — Page Builder (night) 15 Nov 2026.
Built from the Research Lead brief (14 Nov 2026) + Visual Studio night media @89996c9 (hero, explainer, reel).
Every trek number comes from the live Suzu trek page it links to. Unverified list respected: Lamadugh card says
only "forest day hike to a high meadow above Manali" (no height/length/start); no Jobdi Nullah fee/timings; no
Hampta opening date; trekking.hp.gov.in described as the Kullu registration portal only. Generic photos carry
neutral alt and are never captioned as a named spot. No prices, no operator names. Quote-form links carry ?activity=.
Run: python3 pages/gen_trekking-in-manali.py && python3 build.py pages/trekking-in-manali.html > pages/trekking-in-manali.min.html
"""
from urllib.parse import quote
import pathlib

SLUG = "trekking-in-manali"
U = "https://suzutravels.com/wp-content/uploads/"
CDN = ("https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@89996c91ddbd71cf95983d66e0fbd554a847a20c"
       f"/adventure-kit/media/{SLUG}/")


def wa(activity, place="Manali"):
    t = (f"Hi Suzu Travels, I want a quote for {activity} in {place}. "
         f"Travel date: ___ , people: ___ (page: {SLUG})")
    return "https://wa.me/917087488961?text=" + quote(t, safe="")


WA = wa("a trek")
QF = "/himachal-tour-packages-quote/?activity=" + quote("Trekking in Manali", safe="")
A = 'target="_blank" rel="noopener"'

# name, badge, img, alt, meta, text, wa link, guide link
cards = [
    ("Jogini Waterfall", "Half day · all year", "2026/11/waterfall-rock-ledge-forest-pool-1024x769.webp",
     "A waterfall pouring over a wide rock ledge into a green pool, with forested slopes around",
     "Vashisht · 3–4 km walk · ~150 ft fall",
     "Village trail past orchards from Vashisht temple to the Jogini Mata shrine at the base of the fall. Easy; slippery in snow and rain.",
     wa("the Jogini Waterfall trek"), "/adventure/jogini-waterfall-trek/"),
    ("Lamadugh meadow", "Day hike", "2026/11/trekkers-misty-pine-forest-trail-768x512.webp",
     "Two walkers on a dirt trail through misty pine forest on a green hillside",
     "Forest day hike above Manali",
     "A forest day hike to a high meadow above Manali town. Ask us for the route, timing and snow status for your date.",
     wa("the Lamadugh day hike"), ""),
    ("Sethan Valley", "Winter snow walk", "2026/11/snowy-mountain-hamlet-deep-snow-blue-sky-768x355.webp",
     "A small mountain hamlet half buried in deep snow under a clear blue sky",
     "~2,700 m · Hamta road, 12–15 km above Manali",
     "A quiet Buddhist village for snow walks; snow is most reliable in January–February, igloo stays from about mid-January to March.",
     wa("Sethan snow walks"), "/adventure/sethan-valley-manali/"),
    ("Beas Kund", "Best first trek", "2026/10/turquoise-glacial-lake-boulders-snow-768x1024.webp",
     "Small turquoise glacial lake ringed by boulders below snow-streaked peaks",
     "Dhundi near Solang · ~3,890 m · 2–3 days",
     "About 15–16 km to the source of the Beas below snow peaks. May to October.",
     wa("the Beas Kund trek"), "/adventure/beas-kund-trek/"),
    ("Patalsu Peak", "Peak views", "2026/11/trekker-snowy-summit-ridge-snow-range-768x512.webp",
     "Trekker with a red backpack standing on a snowy rocky ridge looking out over a range of snow peaks",
     "Solang · about 4,200 m · 3–4 days",
     "Solang to the Shagadugh clearing, a camp near the tree line, then the summit — a beginner-friendly peak.",
     wa("the Patalsu Peak trek"), "/adventure/patalsu-peak-trek/"),
    ("Bhrigu Lake", "Alpine lake", "2026/10/hiker-rock-above-cloud-valley-768x509.webp",
     "Hiker sitting on a rock outcrop above a valley filled with low white cloud",
     "Gulaba · ~4,235 m · 3–4 days",
     "About 24 km return through high meadows to a glacial lake. June to mid-October.",
     wa("the Bhrigu Lake trek"), "/adventure/bhrigu-lake-trek/"),
    ("Chandrakhani Pass", "Meadow camps", "2026/11/canvas-trek-tents-green-meadow-misty-mountains-768x512.webp",
     "Row of canvas trek tents on a green meadow below misty forested mountains with snow patches",
     "Rumsu near Naggar · 3,660 m · 4–5 days",
     "Deodar forest and meadow camps to a ridge-top pass above Malana; Malana village rules apply. May to October.",
     wa("the Chandrakhani Pass trek"), "/adventure/chandrakhani-pass-trek/"),
    ("Hampta Pass", "Classic crossing", "2026/10/trekkers-snowfield-high-pass-768x576.webp",
     "Small group of trekkers in red jackets and gaiters walking across a snowfield below rocky peaks",
     "Jobra → Chhatru · ~4,270 m · 4–5 days",
     "About 26 km from green Kullu into dry Lahaul, with a Chandratal add-on. Mid/late June to about September.",
     wa("the Hampta Pass trek"), "/adventure/hampta-pass-trek/"),
]

card_html = "".join(
    f'<article class="sza-card"><div class="img"><img src="{U}{img}" alt="{alt}" loading="lazy"><span class="sza-badge">{badge}</span></div>'
    f'<div class="body"><h3>{name}</h3><div class="meta"><b>{meta}</b></div><p class="meta">{txt}</p>'
    f'<div class="go">{(f"<a class=x href={chr(34)}{guide}{chr(34)}>Trek guide →</a>" if guide else "")}<a class="q" href="{link}" {A}>Get Quote →</a></div></div></article>'
    for name, badge, img, alt, meta, txt, link, guide in cards)

pick = [
    ("1 day", "Jogini Waterfall (½ day) · Lamadugh meadow · Sethan snow walk", True),
    ("2–3 days", "Beas Kund", False),
    ("3–4 days", "Bhrigu Lake · Patalsu Peak", False),
    ("4–5 days", "Chandrakhani Pass · Hampta Pass", False),
]
pick_html = "".join(
    f'<div class="sza-fact"><div class="k">{d}</div><div class="v">{t}{"<br><span class=wn>Winter now: Jogini + Sethan</span>" if w else ""}</div></div>'
    for d, t, w in pick)

faqs = [
    ("Which is the best one-day trek in Manali?",
     'Jogini Waterfall: a 3–4 km walk from Vashisht to a fall of about 150 ft, easy and open most of the year. See the <a href="/adventure/jogini-waterfall-trek/">Jogini Waterfall trek guide</a>.'),
    ("Which Manali treks are open in winter?",
     'Jogini Waterfall and the Sethan snow walks on the Hamta road. Beas Kund, Bhrigu Lake, Patalsu, Chandrakhani and Hampta are summer treks.'),
    ("Which Manali trek is best for beginners?",
     'Beas Kund: about 15–16 km over 2–3 days from Dhundi near Solang, May to October. Patalsu Peak is a beginner-friendly summit too.'),
    ("Do I need a permit for Hampta Pass?",
     'Trekkers register at the Jobdi Nullah check post, and the Lahaul-Spiti side needs prior registration with the DDMA-authorised officer and check-out on return. We do this for you.'),
    ("Do I need to register to trek in Kullu?",
     'Kullu district runs trek registration on the HP Trekking Management System portal (trekking.hp.gov.in). We register your group with the trek.'),
    ("Bhrigu Lake or Beas Kund?",
     'Beas Kund is shorter (2–3 days to about 3,890 m); Bhrigu Lake is higher (about 4,235 m) and takes 3–4 days from Gulaba.'),
    ("How much does a Manali trek cost?",
     f'It depends on the trek, days, group, month and add-ons. <a href="{WA}" {A}>Send your dates on WhatsApp</a> and get today\'s rate within minutes.'),
    ("Can you add hotel and cab?",
     'Yes — Manali hotel nights plus the cab to the start point and back, in one quote.'),
]
faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)

reel = pathlib.Path(__file__).resolve().parent.parent.joinpath("media", SLUG, "reel-section.html").read_text(encoding="utf-8").strip()

P = "sza-tim"
html = f'''<!-- {SLUG} — built by Page Builder (night) 15 Nov 2026 from the Research Lead brief + Visual Studio night media @89996c9. Kit v2.0. -->
<style>@media(max-width:900px){{.{P} .sza-hero video{{object-position:20% 50%}}.{P} .sza-hero:after{{background:linear-gradient(180deg,rgba(11,31,51,.5) 0%,rgba(11,31,51,.7) 45%,rgba(11,31,51,.95) 100%)}}}}.{P} .sza-hero-in>*{{max-width:640px}}@media(min-width:901px){{.{P} .sza-hero-in>*{{max-width:min(560px,44vw)}}}}.{P} .sza-chips{{max-width:720px}}.{P} #spots .sza-grid{{grid-template-columns:repeat(auto-fit,minmax(230px,1fr))}}@media(min-width:1000px){{.{P} #experience .sza-steps{{grid-template-columns:repeat(3,1fr)}}}}.{P} #spots .sza-card .img img{{aspect-ratio:3/2;object-fit:cover}}.{P} .sza-media ul{{padding-left:20px;list-style:disc;margin:0}}.{P} .sza-media ul li{{margin:0 0 8px}}.{P} .sza-checks{{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}.{P} .go .x{{margin-right:14px}}.{P} .sza-pick{{margin-top:18px}}.{P} .wn{{display:inline-block;margin-top:6px;font-size:13px;font-weight:700;color:#0b1f33;background:#f6e7c4;border-radius:999px;padding:2px 10px}}.{P} .sza-credit{{font-size:12px;color:#5b6b7a;margin:14px 0 0}}</style>
<div class="sza {P}">
<section class="sza-hero">
<video autoplay muted loop playsinline preload="metadata" poster="{U}2026/11/{SLUG}-hero-poster.webp" aria-label="A waterfall in forest, a lake below snow peaks, trekkers on a snowfield and a snowy hamlet, with a gold trail map from Manali to six treks and a day counter from half a day to 5 days"><source src="{CDN}hero.webm" type="video/webm"><source src="{CDN}hero.mp4" type="video/mp4"></video>
<div class="sza-hero-in">
<span class="sza-kicker">Treks &amp; Camps · Manali, Kullu</span>
<p class="sza-hero-tag">From a waterfall walk to a 4,270 m pass, all from Manali</p>
<p class="sza-hero-sub">Day hikes, lake treks and crossings into Lahaul — registered local team, hotel and cab planned by Suzu.</p>
<ul class="sza-chips"><li><b>Treks</b> 8 from Manali</li><li><b>Time</b> Half-day to 5 days</li><li><b>Highest</b> ~4,270 m (Hampta)</li><li><b>Winter</b> Jogini + Sethan</li><li><b>Passes</b> Mid-Jun–Sep</li><li><b>Price</b> Get Quote</li></ul>
<div class="sza-btns"><a class="sza-btn gold" href="{WA}" {A}>Get Quote on WhatsApp</a><a class="sza-btn ghost" href="{QF}">Add to my Himachal trip</a></div>
<div class="sza-trust"><span><a href="https://suzutravels.com/certificates/">HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022</a></span><span>Hotel + cab in one quote</span><span>Reply within minutes</span></div>
</div>
</section>
<nav class="sza-nav" aria-label="On this page"><div class="sza-nav-in"><a href="#overview">Overview</a><a href="#spots">Treks</a><a href="#experience">How it works</a><a href="#season">Season</a><a href="#safety">Rules</a><a href="#booking">How booking works</a><a href="#packages">Packages</a><a href="#faq">FAQ</a><a class="cta" href="{WA}" {A}>Get Quote</a></div></nav>

<section class="sza-sec" id="overview">
<span class="sza-kicker">Quick answer</span>
<h2>Trekking in Manali at a glance</h2>
<p class="sza-answer">Manali is a base for eight good treks. Jogini Waterfall from Vashisht is a half-day walk; Beas Kund, Bhrigu Lake and Patalsu take 2–4 days; Chandrakhani Pass and Hampta Pass (about 4,270 m, 4–5 days) are the classic crossings. Summer treks run roughly May to October. In winter, Jogini and the Sethan snow walks stay open.</p>
<div class="sza-facts"><div class="sza-fact"><div class="k">Treks from Manali</div><div class="v">8 — 2 day hikes, a winter snow walk, 3 lake and peak treks, 2 passes</div></div><div class="sza-fact"><div class="k">Start points</div><div class="v">Vashisht, Solang/Dhundi, Gulaba, Sethan, Rumsu (Naggar), Jobra (Hampta)</div></div><div class="sza-fact"><div class="k">Highest</div><div class="v">Hampta Pass about 4,270 m; Bhrigu Lake about 4,235 m</div></div><div class="sza-fact"><div class="k">Season</div><div class="v">May–Oct for lakes and passes; Jogini all year</div></div><div class="sza-fact"><div class="k">Registration</div><div class="v">Kullu trekking portal; Jobdi Nullah check post for Hampta; Lahaul-Spiti DDMA on the Chhatru side</div></div><div class="sza-fact"><div class="k">Price</div><div class="v">Get Quote</div></div></div>
<h3 style="margin-top:28px">Pick your trek by days</h3>
<div class="sza-facts sza-pick">{pick_html}</div>
</section>

<section class="sza-sec alt" id="spots">
<span class="sza-kicker">Treks &amp; options</span>
<h2>Eight treks from a Manali base</h2>
<p class="sza-lead">Short to long: two day walks, a winter snow village, three lake and peak treks and the two classic passes. Each card links to its full trek guide.</p>
<div class="sza-grid">{card_html}</div>
<p class="sza-credit">Photos are illustrative (Pexels), not the named spots themselves. Also from Manali: <a href="/adventure/himalayan-peak-expeditions/">Friendship Peak and other guided climbs</a>; nearby in Parvati valley: <a href="/adventure/treks-near-kasol/">treks near Kasol</a> and the <a href="/adventure/kheerganga-trek/">Kheerganga trek</a> (a day trek now — no camping at the top).</p>
</section>

<section class="sza-sec" id="experience">
<span class="sza-kicker">How it works</span>
<h2>How a Manali trek works with Suzu</h2>
<ol class="sza-steps"><li><h3>Send your pick</h3><p>WhatsApp your dates, group and trek — or ask us to suggest one for your days.</p></li><li><h3>Season and snow check</h3><p>We confirm the route is open and the snow conditions for those dates.</p></li><li><h3>Registration + team</h3><p>We register the group (Kullu portal / Jobdi Nullah check post; Lahaul-Spiti DDMA for Hampta's Chhatru side) and arrange a registered local trek team.</p></li><li><h3>Night in Manali</h3><p>Hotel the night before; cab to Vashisht, Solang, Gulaba, Jobra or Rumsu.</p></li><li><h3>Trek days</h3><p>Pick-up at the end point — Chhatru for Hampta, the Malana side for Chandrakhani.</p></li><li><h3>Back to Manali</h3><p>A night in Manali after the trek — all in one quote.</p></li></ol>
<div class="sza-media"><video autoplay muted loop playsinline preload="none" poster="{U}2026/11/{SLUG}-explainer-poster.webp" width="1600" height="900" aria-label="Bars to scale for seven Manali treks from Jogini at about 2,300 m to Hampta Pass at about 4,270 m, Winter now on Jogini and Sethan, a month strip of the season and Price: Get Quote"><source src="{CDN}explainer.webm" type="video/webm"><source src="{CDN}explainer.mp4" type="video/mp4"></video><div><h3>How high, and when</h3><ul><li><b>Low</b> → Jogini and Sethan, open in winter.</li><li><b>Mid</b> → Beas Kund ~3,890 m, from May.</li><li><b>High</b> → Patalsu ~4,200 m, Bhrigu ~4,235 m, Hampta ~4,270 m.</li><li><b>Passes</b> → Chandrakhani from May; Hampta mid/late June to about September.</li></ul><p style="margin-top:8px;font-size:14px">Heights are from our individual trek guides.</p></div></div>
</section>

<section class="sza-sec alt" id="season">
<span class="sza-kicker">When to go</span>
<h2>Best time for trekking in Manali</h2>
<div class="sza-scroll"><table class="sza-tbl"><thead><tr><th>Months</th><th>Day hikes (Jogini, Lamadugh, Sethan)</th><th>Lake &amp; peak treks (Beas Kund, Bhrigu, Patalsu)</th><th>Passes (Chandrakhani, Hampta)</th></tr></thead><tbody><tr><td>Dec – Feb</td><td>Jogini open; Sethan snow walks and igloo nights</td><td>Closed by snow</td><td>Closed; Lahaul side under a winter trekking ban</td></tr><tr><td>Mar – Apr</td><td>Good, snow patches</td><td>Snow; not advised</td><td>Closed</td></tr><tr><td>May – Jun</td><td>Good</td><td>Season opens (Beas Kund May; Bhrigu June)</td><td>Chandrakhani opens; Hampta from mid/late June</td></tr><tr><td>Jul – Aug</td><td>Rain, slippery</td><td>Open but wet</td><td>Hampta best (Lahaul side drier)</td></tr><tr><td>Sep – Oct</td><td>Best</td><td>Best till mid-October</td><td>Best; Hampta till about September</td></tr></tbody></table></div>
</section>

<div class="sza-band" id="safety"><div class="sza-band-in">
<span class="sza-kicker">Safety &amp; area rules</span>
<h2>Rules we follow on every Manali trek</h2>
<p class="sza-lead">Suzu Travels is an HP Tourism registered travel agent (Reg. No. DTO-MND-11-243/2022). Before your trek we check:</p>
<ul class="sza-checks"><li><b>Kullu trek registration</b>Kullu district registers treks on the HP Trekking Management System (trekking.hp.gov.in); we register your group</li><li><b>Hampta check post</b>The forest and tourism check post at Jobdi Nullah records trekkers so there is a record in an emergency</li><li><b>Lahaul-Spiti side</b>Hampta comes down into Lahaul-Spiti: prior registration with the DDMA-authorised officer and check-out on return; winter trekking is banned there</li><li><b>Altitude limit</b>The state advisory on tracks above 15,000 ft does not cover these eight treks; Friendship Peak is higher — see guided climbs</li><li><b>Sethan road</b>Vehicles need the online Hamta road permit; after fresh snow only 4x4s with chains get through</li><li><b>Team and weather</b>Registered local trek team, no solo pass crossings, weather checked at Solang or Gulaba before going up</li></ul>
</div></div>

<section class="sza-sec" id="booking">
<span class="sza-kicker">How booking works</span>
<h2>Get a quote in minutes</h2>
<ol class="sza-steps"><li><h3>Tell us</h3><p>WhatsApp or the quote form — trek, dates, people and pickup city.</p></li><li><h3>We check your date</h3><p>Season, snow and the right trek for your group.</p></li><li><h3>You get one quote</h3><p>Trek team, Manali hotel and cab together.</p></li><li><h3>Confirm and go</h3><p>We send the plan and stay in touch on WhatsApp.</p></li></ol>
<p class="sza-lead">Your quote depends on which trek and how many days, group size (private or small group), the month (snow gear, mules or porters), tents and meals on the trail, registration or check-post entry where it applies, hotel nights in Manali and the cab to the start and from the end point, and add-ons such as gear or snow-suit rental or a porter for your personal bag.</p>
</section>

{reel}

<section class="sza-quote"><div><span class="sza-kicker">Manali treks</span><h2>Get your Manali trek quote</h2><p>Tell us the trek, your dates and group size. We reply with today's rate — trek team, hotel and cab included.</p></div><div class="sza-btns"><a class="sza-btn gold" href="{WA}" {A}>Get Quote on WhatsApp</a><a class="sza-btn ghost" href="{QF}">Plan full trip</a></div></section>

<section class="sza-sec" id="packages">
<span class="sza-kicker">Make it a trip</span>
<h2>Pair your trek with a Manali holiday</h2>
<p><b>Manali 3 nights + one trek + cab:</b> add a trek to the <a href="/packages/himachal-tour-package-shimla-manali/">Shimla–Manali tour package</a> or the <a href="/packages/kullu-manali-honeymoon-tour-package/">Kullu–Manali honeymoon package</a>, or browse <a href="/packages/">all packages</a>. Getting there: <a href="/cabs/delhi-to-manali-taxi/">Delhi to Manali taxi</a>, <a href="/cabs/chandigarh-to-manali-taxi/">Chandigarh to Manali taxi</a> and <a href="/cabs/manali-taxi-service/">Manali taxi service</a> for trailheads. Doing Hampta? Add the <a href="/adventure/chandratal-lake-trek-and-camps/">Chandratal lake camps</a>.</p>
<p><b>Plan the rest:</b> our <a href="/manali/">Manali travel guide</a>, the <a href="/old-manali-guide/">Old Manali guide</a> and <a href="/weather/manali/">Manali weather</a>. More in Manali: <a href="/adventure/adventure-activities-in-manali/">adventure activities in Manali</a>, <a href="/adventure/camping-in-manali/">camping in Manali</a>, <a href="/adventure/snow-activities-manali/">snow activities</a> and <a href="/adventure/solang-valley-activities/">Solang Valley</a>. All regions: <a href="/adventure/trekking-in-himachal/">trekking in Himachal</a>, or <a href="{QF}">ask for a custom plan</a>.</p>
</section>

<section class="sza-sec sza-faq" id="faq">
<span class="sza-kicker">FAQ</span>
<h2>Trekking in Manali — questions</h2>
{faq_html}
</section>

<section class="sza-sec alt" id="more">
<span class="sza-kicker">More adventures</span>
<h2>Explore more in Himachal</h2>
<div class="sza-cats"><a class="sza-cat" href="/adventure/trekking-in-himachal/"><span class="ic">🥾</span><span class="n">Trekking in Himachal</span><span class="c">All regions</span></a><a class="sza-cat" href="/adventure/hampta-pass-trek/"><span class="ic">🏔️</span><span class="n">Hampta Pass trek</span><span class="c">Manali → Lahaul</span></a><a class="sza-cat" href="/adventure/camping-in-manali/"><span class="ic">⛺</span><span class="n">Camping in Manali</span><span class="c">Manali</span></a><a class="sza-cat" href="/adventure/igloo-stay-manali/"><span class="ic">❄️</span><span class="n">Igloo stay</span><span class="c">Sethan, Manali</span></a><a class="sza-cat" href="/adventure/paragliding-in-manali/"><span class="ic">🪂</span><span class="n">Paragliding in Manali</span><span class="c">Solang</span></a><a class="sza-cat" href="/adventure/"><span class="ic">🧭</span><span class="n">All adventures</span><span class="c">Air · Water · Snow · Land</span></a></div>
</section>
</div>'''

pathlib.Path(__file__).with_name(f"{SLUG}.html").write_text(html, encoding="utf-8")
print("ok", len(html))
