#!/usr/bin/env python3
"""treks-near-dalhousie — Page Builder (night) 14 Nov 2026.
Built from the Research Lead brief (13 Nov 2026) + Visual Studio night media @1ce786e (hero, explainer, reel).
Unverified list respected: Ganji Pahari = "short hike" (no length/height), no Bakrota number, no fee/timings,
no camping promise. Generic Pexels photos carry neutral alt and are never captioned as Ganji Pahari.
CC BY-SA photos (Dainkund, Kalatop, Khajjiar) credited. No prices, no operator names. Quote-form links carry ?activity=.
Run: python3 pages/gen_treks-near-dalhousie.py && python3 build.py pages/treks-near-dalhousie.html > pages/treks-near-dalhousie.min.html
"""
from urllib.parse import quote
import pathlib

SLUG = "treks-near-dalhousie"
U = "https://suzutravels.com/wp-content/uploads/"
CDN = ("https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@1ce786ee8347b6d851b00e1298c008359c9d5ad8"
       f"/adventure-kit/media/{SLUG}/")


def wa(activity, place="Dalhousie"):
    t = (f"Hi Suzu Travels, I want a quote for {activity} in {place}. "
         f"Travel date: ___ , people: ___ (page: {SLUG})")
    return "https://wa.me/917087488961?text=" + quote(t, safe="")


WA = wa("a trek")
QF = "/himachal-tour-packages-quote/?activity=" + quote("Treks near Dalhousie", safe="")
A = 'target="_blank" rel="noopener"'
CC = '<a href="https://creativecommons.org/licenses/by-sa/4.0" rel="nofollow noopener" target="_blank">CC BY-SA 4.0</a>'

cards = [
    ("Ganji Pahari", "Easy · half day", "2026/11/grassy-clearing-conifers-snow-peaks-768x1152.webp",
     "Open grassy clearing ringed by tall conifer trees with snow-capped peaks behind", "50% 60%",
     "About 5 km from Dalhousie bus stand · trail from Panchpula",
     "&ldquo;Ganji&rdquo; means bald: a tree-less hilltop with open views above the pine and oak forest. A short hike — no shops on top.",
     wa("the Ganji Pahari hike"), ""),
    ("Dainkund Peak", "Snow peak", "2026/11/suzu-dalhousie-ka-mausam-g-5-768x364.webp",
     "Snow on Dainkund Peak, the highest point near Dalhousie", "50% 50%",
     "Highest point near Dalhousie · Lakkar Mandi road",
     "A short, steep walk up from the Lakkar Mandi side road to the ridge and the Pholani Devi temple.",
     wa("the Dainkund Peak trek"),
     '<a class="x" href="/adventure/dainkund-peak-trek/">Dainkund guide →</a>'),
    ("Kalatop forest walk", "Family walk", "2026/11/suzu-dalhousie-ka-mausam-g-6-768x432.webp",
     "Kalatop–Khajjiar wildlife sanctuary in winter", "50% 50%",
     "3 km forest road from the Lakkar Mandi barrier",
     "A level walk inside the Kalatop Wildlife Sanctuary to the forest rest house — the gentlest hike here.",
     wa("the Kalatop forest walk"),
     '<a class="x" href="/adventure/kalatop-khajjiar-sanctuary-trek/">Kalatop guide →</a>'),
    ("Dalhousie → Kalatop → Khajjiar", "Full day", "2026/11/suzu-dalhousie-ka-mausam-g-3-768x576.webp",
     "Khajjiar meadow ringed by deodar forest near Dalhousie", "50% 55%",
     "Full Dalhousie–Kalatop trail about 14 km",
     "A full-day forest trail with a local guide, finishing on the Khajjiar meadow; the cab meets you there.",
     wa("the Dalhousie–Kalatop–Khajjiar trail"),
     '<a class="x" href="/adventure/paragliding-in-khajjiar-dalhousie/">Khajjiar paragliding →</a>'),
    ("Panchpula &amp; Bakrota walks", "Easy stroll", "2026/11/family-walk-pine-forest-path-768x432.webp",
     "Parent and child walking on a dirt path through a hillside pine forest on a sunny day", "50% 50%",
     "Gentle town walks",
     "Panchpula's streams and the Bakrota hill loop — good for a rainy or no-snow day, and for kids and seniors.",
     wa("Panchpula and Bakrota walks"), ""),
]

card_html = "".join(
    f'<article class="sza-card"><div class="img"><img src="{U}{img}" alt="{alt}" style="object-position:{pos}" loading="lazy"><span class="sza-badge">{badge}</span></div>'
    f'<div class="body"><h3>{name}</h3><div class="meta"><b>{meta}</b></div><p class="meta">{txt}</p>'
    f'<div class="go">{extra}<a class="q" href="{link}" {A}>Get Quote →</a></div></div></article>'
    for name, badge, img, alt, pos, meta, txt, link, extra in cards)

faqs = [
    ("Which are the best treks near Dalhousie?",
     "Ganji Pahari, Dainkund Peak, the Kalatop forest walk and the Dalhousie–Kalatop–Khajjiar trail. All are day hikes from a Dalhousie hotel."),
    ("Where is Ganji Pahari?",
     "About 5 km from Dalhousie bus stand on the Pathankot road. The walk starts from Panchpula."),
    ("Why is it called Ganji Pahari?",
     "&ldquo;Ganji&rdquo; means bald: the hilltop has no trees, unlike the pine and oak forest around it."),
    ("How long is the Ganji Pahari trek?",
     "It is a short hike of a few hours return from Panchpula; give it half a day with the drive. Sources give different trail lengths, so we confirm the route locally."),
    ("Does Ganji Pahari get snow?",
     "Yes, usually in winter (December to February). Paths can be icy, so wear shoes with grip."),
    ("Is a guide needed for Ganji Pahari?",
     "Not required for the short trail, but useful for families and in snow. For the longer Kalatop–Khajjiar trail we recommend a local guide."),
    ("What is the easiest walk near Dalhousie?",
     "The 3 km level forest road from Lakkar Mandi to Kalatop, or the Panchpula and Bakrota town walks."),
    ("Can we combine treks with Khajjiar?",
     "Yes. Kalatop and Dainkund sit on the Dalhousie–Khajjiar road, so one cab day covers a hike and the Khajjiar meadow."),
    ("Can we camp on Ganji Pahari?",
     f'We plan these as day hikes with a Dalhousie or Khajjiar hotel stay. If you want a night under canvas, see our <a href="/adventure/camping-in-himachal/">camping in Himachal</a> options.'),
    ("What do treks near Dalhousie cost?",
     f'We don\'t post fixed prices — it depends on your hotel, cab, guide and dates. <a href="{WA}" {A}>Tap Get Quote</a> and we send today\'s rate on WhatsApp within minutes.'),
]
faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)

reel = pathlib.Path(__file__).resolve().parent.parent.joinpath("media", SLUG, "reel-section.html").read_text(encoding="utf-8").strip()

P = "sza-tnd"
html = f'''<!-- {SLUG} — built by Page Builder (night) 14 Nov 2026 from the Research Lead brief + Visual Studio night media @1ce786e. Kit v2.0. -->
<style>@media(max-width:900px){{.{P} .sza-hero video{{object-position:20% 50%}}.{P} .sza-hero:after{{background:linear-gradient(180deg,rgba(11,31,51,.5) 0%,rgba(11,31,51,.7) 45%,rgba(11,31,51,.95) 100%)}}}}.{P} .sza-hero-in>*{{max-width:640px}}@media(min-width:901px){{.{P} .sza-hero-in>*{{max-width:min(560px,44vw)}}}}.{P} .sza-chips{{max-width:720px}}.{P} #spots .sza-grid{{grid-template-columns:repeat(auto-fit,minmax(200px,1fr))}}@media(min-width:1000px){{.{P} #experience .sza-steps{{grid-template-columns:repeat(3,1fr)}}}}.{P} #spots .sza-card .img img{{aspect-ratio:3/2;object-fit:cover}}.{P} .sza-media ul{{padding-left:20px;list-style:disc;margin:0}}.{P} .sza-media ul li{{margin:0 0 8px}}.{P} .sza-checks{{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}.{P} .go .x{{margin-right:14px}}.{P} .sza-credit{{font-size:12px;color:#5b6b7a;margin:14px 0 0}}.{P} .sza-credit a{{color:inherit}}</style>
<div class="sza {P}">
<section class="sza-hero">
<video autoplay muted loop playsinline preload="metadata" poster="{U}2026/11/{SLUG}-hero-poster.webp" aria-label="A family on a pine forest path, snow peaks over conifers, the Kalatop forest in snow and the snowy Dainkund ridge, with a gold two-road map from Dalhousie to Ganji Pahari and to Dainkund and Kalatop"><source src="{CDN}hero.webm" type="video/webm"><source src="{CDN}hero.mp4" type="video/mp4"></video>
<div class="sza-hero-in">
<span class="sza-kicker">Treks &amp; Camps · Dalhousie</span>
<p class="sza-hero-tag">Easy pine-forest hikes and snowy hilltops around Dalhousie</p>
<p class="sza-hero-sub">Half-day and full-day walks from your Dalhousie hotel — we add the cab, the guide and Khajjiar.</p>
<ul class="sza-chips"><li><b>Hikes</b> 4 day hikes</li><li><b>Level</b> Easy to moderate</li><li><b>Time</b> Half or full day</li><li><b>Snow</b> Dec–Feb</li><li><b>Who</b> Family friendly</li><li><b>Price</b> Get Quote</li></ul>
<div class="sza-btns"><a class="sza-btn gold" href="{WA}" {A}>Get Quote on WhatsApp</a><a class="sza-btn ghost" href="{QF}">Add to my Himachal trip</a></div>
<div class="sza-trust"><span><a href="https://suzutravels.com/certificates/">HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022</a></span><span>Hotel + cab in one quote</span><span>Reply within minutes</span></div>
</div>
</section>
<nav class="sza-nav" aria-label="On this page"><div class="sza-nav-in"><a href="#overview">Overview</a><a href="#spots">Hikes</a><a href="#experience">Your day</a><a href="#season">Season</a><a href="#safety">Safety</a><a href="#booking">How booking works</a><a href="#packages">Packages</a><a href="#faq">FAQ</a><a class="cta" href="{WA}" {A}>Get Quote</a></div></nav>

<section class="sza-sec" id="overview">
<span class="sza-kicker">Quick answer</span>
<h2>Treks near Dalhousie at a glance</h2>
<p class="sza-answer">The best treks near Dalhousie are short day hikes: Ganji Pahari, a tree-less &ldquo;bald hill&rdquo; reached on foot from Panchpula; Dainkund Peak, the highest point near Dalhousie off the Lakkar Mandi road; the 3 km forest walk to Kalatop; and the longer Dalhousie–Kalatop–Khajjiar trail. Most are easy to moderate and turn snowy from December to February.</p>
<div class="sza-facts"><div class="sza-fact"><div class="k">Base</div><div class="v">Dalhousie town (Chamba district); hikes start 5–20 minutes' drive away</div></div><div class="sza-fact"><div class="k">Ganji Pahari</div><div class="v">About 5 km from Dalhousie bus stand on the Pathankot road; trail from Panchpula</div></div><div class="sza-fact"><div class="k">Kalatop</div><div class="v">3 km forest road from the Lakkar Mandi barrier; full Dalhousie–Kalatop trail about 14 km</div></div><div class="sza-fact"><div class="k">Dainkund Peak</div><div class="v">The highest point near Dalhousie, on the same Lakkar Mandi road as Kalatop</div></div><div class="sza-fact"><div class="k">Snow</div><div class="v">Usually December to February; roads can shut after heavy snow</div></div><div class="sza-fact"><div class="k">Price</div><div class="v">Get Quote</div></div></div>
</section>

<section class="sza-sec alt" id="spots">
<span class="sza-kicker">Hikes &amp; options</span>
<h2>Four day hikes, two roads</h2>
<p class="sza-lead">Ganji Pahari sits off the Pathankot road via Panchpula; Dainkund and Kalatop share the Lakkar Mandi road towards Khajjiar. Pick one, or pair two in a day.</p>
<div class="sza-grid">{card_html}</div>
<p class="sza-credit">Photos: Dainkund Peak in snow — Abhyuday Bhandari, {CC}; Kalatop–Khajjiar sanctuary — Vishrutpanday, {CC}; Khajjiar — Bittudubeyji, {CC} (Wikimedia Commons). Forest-path and hilltop photos are illustrative (Pexels), not Ganji Pahari itself.</p>
</section>

<section class="sza-sec" id="experience">
<span class="sza-kicker">Your day</span>
<h2>How a Dalhousie trek day works</h2>
<ol class="sza-steps"><li><h3>Share dates and group</h3><p>Kids or seniors? We pick the right hike and check snow and road status the day before.</p></li><li><h3>Pickup after breakfast</h3><p>Your cab collects you from your Dalhousie hotel.</p></li><li><h3>Drive to the trailhead</h3><p>Panchpula for Ganji Pahari, or Lakkar Mandi for Dainkund and Kalatop.</p></li><li><h3>Hike</h3><p>With a local guide where useful; carry water and snacks — no shops on top.</p></li><li><h3>Down before dark</h3><p>Start down at least 2 hours before dark; in winter finish by mid-afternoon.</p></li><li><h3>Back or on to Khajjiar</h3><p>Cab back to the hotel, or on to the Khajjiar meadow for the evening.</p></li></ol>
<div class="sza-media"><video autoplay muted loop playsinline preload="none" poster="{U}2026/11/{SLUG}-explainer-poster.webp" width="1600" height="900" aria-label="Four day hikes, two roads: Dalhousie to Panchpula and Ganji Pahari; Dalhousie to Lakkar Mandi for Dainkund and the 3 km Kalatop walk, on to Khajjiar; difficulty cards, snow usually December to February; price: Get Quote"><source src="{CDN}explainer.webm" type="video/webm"><source src="{CDN}explainer.mp4" type="video/mp4"></video><div><h3>Four hikes, two roads</h3><ul><li><b>Road 1</b> → Panchpula → Ganji Pahari, a short hike.</li><li><b>Road 2</b> → Lakkar Mandi → Dainkund Peak (short, steep) or Kalatop (3 km, level).</li><li><b>Full day</b> → Dalhousie–Kalatop–Khajjiar trail with a guide.</li><li><b>Snow</b> → usually December to February.</li></ul><p style="margin-top:8px;font-size:14px">Keep a buffer day in winter — roads can shut after heavy snow.</p></div></div>
</section>

<section class="sza-sec alt" id="season">
<span class="sza-kicker">When to go</span>
<h2>Best time for treks near Dalhousie</h2>
<div class="sza-scroll"><table class="sza-tbl"><thead><tr><th>Months</th><th>Conditions</th><th>Best for</th></tr></thead><tbody><tr><td>Dec – Feb</td><td>Snow on hilltops, cold; roads can close after snowfall</td><td>Snow walks (Ganji Pahari, Dainkund) — check the day before</td></tr><tr><td>Mar – Apr</td><td>Snow melting, clear days</td><td>All hikes</td></tr><tr><td>May – Jun</td><td>Warm, busy season</td><td>Kalatop–Khajjiar full-day trail, early starts</td></tr><tr><td>Jul – Sep</td><td>Monsoon rain, leeches, slippery paths</td><td>Short town walks only</td></tr><tr><td>Oct – Nov</td><td>Clear and dry, cool</td><td>Every hike — best views</td></tr></tbody></table></div>
</section>

<div class="sza-band" id="safety"><div class="sza-band-in">
<span class="sza-kicker">Safety &amp; area rules</span>
<h2>What we check before your Dalhousie hike</h2>
<p class="sza-lead">Suzu Travels is an HP Tourism registered travel agent (Reg. No. DTO-MND-11-243/2022). We plan your day around these checks:</p>
<ul class="sza-checks"><li><b>Kalatop is a wildlife sanctuary</b>Stay on the road or trail, don't feed animals and be out of the forest by dusk; rest-house stays need DFO Chamba permission</li><li><b>Winter grip</b>Snow and ice on the Dainkund and Ganji Pahari paths — wear grip shoes; we check road closures before you go</li><li><b>Carry water and food</b>No shops or water on Ganji Pahari top; start down 2 hours before dark</li><li><b>Kids and seniors</b>The Kalatop road and the town walks are the gentle options; Dainkund's last climb is steep</li><li><b>Follow forest signs</b>We found no blanket trekking registration rule for these short day hikes; follow forest-department signs and barrier rules</li><li><b>Dainkund Air Force area</b>Stay on the public path and never photograph the installation; no drones</li></ul>
</div></div>

<section class="sza-sec" id="booking">
<span class="sza-kicker">How booking works</span>
<h2>Get a quote in minutes</h2>
<ol class="sza-steps"><li><h3>Tell us</h3><p>WhatsApp or the quote form — dates, people and pickup city.</p></li><li><h3>We check your date</h3><p>Snow, road status and the right hike for your group.</p></li><li><h3>You get one quote</h3><p>Dalhousie or Khajjiar hotel, cab and guide together.</p></li><li><h3>Confirm and go</h3><p>We send the plan and stay in touch on WhatsApp.</p></li></ol>
<p class="sza-lead">Your quote depends on which hikes and how many days you spend in Dalhousie and Khajjiar, the cab type and route (Dalhousie to Panchpula, Lakkar Mandi or Khajjiar) and your pickup from Pathankot, Chandigarh or Delhi, a local guide for the longer trails, the hotel category and the season (Christmas–New Year is peak), and add-ons such as Khajjiar paragliding, a Kalatop rest-house request or snow gear on rent.</p>
</section>

{reel}

<section class="sza-quote"><div><span class="sza-kicker">Dalhousie hikes &amp; snow</span><h2>Get your Dalhousie trek quote</h2><p>Tell us your dates, group size and pickup city. We reply with today's rate — hotel, cab and guide included.</p></div><div class="sza-btns"><a class="sza-btn gold" href="{WA}" {A}>Get Quote on WhatsApp</a><a class="sza-btn ghost" href="{QF}">Plan full trip</a></div></section>

<section class="sza-sec" id="packages">
<span class="sza-kicker">Make it a trip</span>
<h2>Pair your hikes with Khajjiar</h2>
<p><b>2 nights Dalhousie + 1 night Khajjiar:</b> a Ganji Pahari morning and a Dainkund–Kalatop day fit into our <a href="/dalhousie-tour-package/">Dalhousie tour package</a>, or go further with the <a href="/dharamshala-dalhousie-tour-package/">Dharamshala–Dalhousie tour package</a>. Coming by train? Book the <a href="/cabs/pathankot-to-dalhousie-taxi/">Pathankot to Dalhousie taxi</a>. Plan the rest with our <a href="/dalhousie/">Dalhousie travel guide</a>, the <a href="/dalhousie-khajjiar-trip-guide/">Dalhousie–Khajjiar trip guide</a> and the list of <a href="/dalhousie-tourist-places/">Dalhousie tourist places</a>.</p>
<p><b>Chasing snow?</b> Check <a href="/weather/dalhousie/">Dalhousie weather</a>, <a href="/dalhousie-ka-mausam/">Dalhousie ka mausam</a>, our <a href="/dalhousie-snowfall/">Dalhousie snowfall guide</a> and <a href="/himachal-in-december/">Himachal in December</a>; rent <a href="/adventure/snow-suit-and-boots-on-rent-manali/">snow suits and boots</a>. Want a bigger trek next? Try the <a href="/adventure/kareri-lake-trek/">Kareri Lake trek</a> or the <a href="/adventure/triund-trek/">Triund trek</a>, or <a href="{QF}">ask for a custom plan</a>.</p>
</section>

<section class="sza-sec sza-faq" id="faq">
<span class="sza-kicker">FAQ</span>
<h2>Treks near Dalhousie — questions</h2>
{faq_html}
</section>

<section class="sza-sec alt" id="more">
<span class="sza-kicker">More adventures</span>
<h2>Explore more in Himachal</h2>
<div class="sza-cats"><a class="sza-cat" href="/adventure/dainkund-peak-trek/"><span class="ic">🏔️</span><span class="n">Dainkund Peak trek</span><span class="c">Dalhousie</span></a><a class="sza-cat" href="/adventure/kalatop-khajjiar-sanctuary-trek/"><span class="ic">🌲</span><span class="n">Kalatop forest walk</span><span class="c">Dalhousie</span></a><a class="sza-cat" href="/adventure/paragliding-in-khajjiar-dalhousie/"><span class="ic">🪂</span><span class="n">Paragliding in Khajjiar</span><span class="c">Dalhousie</span></a><a class="sza-cat" href="/adventure/kareri-lake-trek/"><span class="ic">🏞️</span><span class="n">Kareri Lake trek</span><span class="c">Dhauladhar</span></a><a class="sza-cat" href="/adventure/camping-in-himachal/"><span class="ic">⛺</span><span class="n">Camping in Himachal</span><span class="c">All regions</span></a><a class="sza-cat" href="/adventure/"><span class="ic">🧭</span><span class="n">All adventures</span><span class="c">Air · Water · Snow · Land</span></a></div>
</section>
</div>'''

pathlib.Path(__file__).with_name(f"{SLUG}.html").write_text(html, encoding="utf-8")
print("ok", len(html))
