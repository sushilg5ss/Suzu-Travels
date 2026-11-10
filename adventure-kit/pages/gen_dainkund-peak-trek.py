#!/usr/bin/env python3
"""dainkund-peak-trek — Page Builder (night) 11 Nov 2026.
Built from the Research Lead brief (9 Nov 2026) + Visual Studio night media @81f251c (hero, explainer, reel).
Unverified list respected: distances/walk as ranges only; no visiting hours; "drive as far as allowed, then walk";
no Mount Kailash claim; no entry/parking fee; general IAF photography line only.
Generic Pexels photos carry neutral alt. CC BY-SA photos (WP 19358, 19359, 19356) credited.
No prices, no operator names. Quote-form links carry ?activity= (night override).
Run: python3 pages/gen_dainkund-peak-trek.py && python3 build.py pages/dainkund-peak-trek.html > pages/dainkund-peak-trek.min.html
"""
from urllib.parse import quote
import pathlib

SLUG = "dainkund-peak-trek"
U = "https://suzutravels.com/wp-content/uploads/"
CDN = ("https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@81f251ce108ce3913558c5f06ffb61bdcac36fb2"
       f"/adventure-kit/media/{SLUG}/")


def wa(activity, place="Dalhousie"):
    t = (f"Hi Suzu Travels, I want a quote for {activity} in {place}. "
         f"Travel date: ___ , people: ___ (page: {SLUG})")
    return "https://wa.me/917087488961?text=" + quote(t, safe="")


WA = wa("the Dainkund Peak trek")
QF = "/himachal-tour-packages-quote/?activity=" + quote("Dainkund Peak trek", safe="")
A = 'target="_blank" rel="noopener"'
CC = '<a href="https://creativecommons.org/licenses/by-sa/4.0" rel="nofollow noopener" target="_blank">CC BY-SA 4.0</a>'

cards = [
    ("Dainkund ridge &amp; Pholani Devi temple", "Main walk", "2026/11/suzu-dalhousie-ka-mausam-g-5-768x364.webp",
     "Snow on Dainkund Peak, the highest point near Dalhousie", "50% 50%",
     "About 2,755 m · 360° view",
     "The top: a small temple with a trident and wide views of the Pir Panjal, the Dhauladhar and the Ravi valley.",
     wa("the Dainkund Peak trek"), ""),
    ("Lakkar Mandi", "Base", "2026/11/dainkund-peak-trek-stone-steps-forest-768x1024.webp",
     "Old stone steps climbing through a misty pine forest on a hillside", "50% 55%",
     "Forest hamlet on the Dalhousie–Khajjiar road",
     "The turn-off for both Dainkund and the Kalatop barrier. Drive as far as allowed, then walk the paved path.",
     wa("the Dainkund Peak trek via Lakkar Mandi"), ""),
    ("Snow day on the Dainkund road", "Winter", "2026/11/dainkund-peak-trek-snowy-conifer-path-768x960.webp",
     "Snow-covered path between snowy conifer trees on a winter morning", "50% 60%",
     "Snow usually December to February",
     "After fresh snow the BRO clears the road because of the Air Force station, so walkers often find snow here first.",
     wa("a Dainkund snow morning"), ""),
    ("Kalatop forest", "Add-on", "2026/11/suzu-dalhousie-ka-mausam-g-6-768x432.webp",
     "Kalatop–Khajjiar wildlife sanctuary in winter", "50% 50%",
     "Deodar sanctuary on the same road",
     "About 3 km in from the Lakkar Mandi barrier — pairs with Dainkund in one day.",
     wa("Dainkund Peak with the Kalatop forest walk"),
     '<a class="x" href="/adventure/kalatop-khajjiar-sanctuary-trek/">Kalatop walk →</a>'),
    ("Khajjiar meadow", "Add-on", "2026/11/suzu-dalhousie-ka-mausam-g-3-768x576.webp",
     "Khajjiar meadow ringed by deodar forest near Dalhousie", "50% 55%",
     "About 30 min further on the same road",
     "Meadow walks and tandem paragliding — Dainkund, Kalatop and Khajjiar fit in one long day.",
     wa("Dainkund Peak with Khajjiar"),
     '<a class="x" href="/adventure/paragliding-in-khajjiar-dalhousie/">Khajjiar paragliding →</a>'),
]

card_html = "".join(
    f'<article class="sza-card"><div class="img"><img src="{U}{img}" alt="{alt}" style="object-position:{pos}" loading="lazy"><span class="sza-badge">{badge}</span></div>'
    f'<div class="body"><h3>{name}</h3><div class="meta"><b>{meta}</b></div><p class="meta">{txt}</p>'
    f'<div class="go">{extra}<a class="q" href="{link}" {A}>Get Quote →</a></div></div></article>'
    for name, badge, img, alt, pos, meta, txt, link, extra in cards)

faqs = [
    ("How high is Dainkund Peak?",
     "About 2,755 m (9,039 ft). It is the highest point near Dalhousie, in Chamba district."),
    ("How far is Dainkund from Dalhousie?",
     "It is reached by road via Lakkar Mandi. Published figures range from about 8 to 17 km depending on where in town you start, so allow 30–45 minutes' drive."),
    ("How long is the Dainkund trek?",
     "From where vehicles are stopped, roughly 2–3 km on a paved path; most people take 45–90 minutes up. Longer versions start lower, at Lakkar Mandi."),
    ("Does Dainkund get snow?",
     "Yes. It is one of the first places around Dalhousie to get snow, usually December to February. The BRO clears the road because of the Air Force station, but it can stay closed for hours after fresh snow."),
    ("What is the Pholani Devi temple?",
     "A small temple on the top of the ridge with a trident and no idol."),
    ("Why is Dainkund called the singing hill?",
     "Wind through the deodar and oak trees makes a whistling sound, so locals call it the singing hill."),
    ("Is Dainkund OK for children and elders?",
     "Yes with care. The height is modest but the first stretch of the path is steep — go slow, carry water and start early. We can arrange a porter on request."),
    ("Can I combine Dainkund with Khajjiar?",
     "Yes. Dainkund, Kalatop and Khajjiar are on the same road; one long day covers all three."),
    ("What does the Dainkund trip cost?",
     f'We don\'t post fixed prices — it depends on your hotel, cab and dates. <a href="{WA}" {A}>Tap Get Quote</a> and we send today\'s rate on WhatsApp within minutes.'),
]
faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)

REEL_WA = ("https://wa.me/917087488961?text=Hi%20Suzu%20Travels%2C%20I%20want%20a%20quote%20for%20the%20Dainkund%20Peak%20trek%20in%20Dalhousie%20%28hotel%20%2B%20cab%29."
           "%20Travel%20date%3A%20___%20%2C%20people%3A%20___%20%28page%3A%20dainkund-peak-trek%20reel%29")
reel = (f'<section class="sza-sec" id="reel"><div style="display:flex;flex-wrap:wrap;align-items:center;gap:32px"><div style="flex:0 0 auto;width:min(300px,100%);margin:0 auto">'
        f'<video poster="{CDN}reel-web-poster.webp" autoplay muted loop playsinline preload="metadata" width="300" height="533" style="display:block;width:100%;height:auto;aspect-ratio:9/16;border-radius:18px;background:#0b1f33;box-shadow:0 12px 32px rgba(11,31,51,.25)" aria-label="15-second reel: snowy conifers, stone steps in a misty forest, a snowy ridge near Dalhousie and the Khajjiar meadow; Dainkund Peak about 2,755 m, 2–3 km up a paved path, snow usually December to February, Kalatop and Khajjiar on the same road">'
        f'<source src="{CDN}reel-web.webm" type="video/webm"><source src="{CDN}reel-web.mp4" type="video/mp4"></video></div>'
        f'<div style="flex:1 1 320px;min-width:0"><span class="sza-kicker">Watch in 15 seconds</span><h2>Dainkund Peak, Dalhousie\'s highest point</h2><p>The short walk to the ridge, the winter snow and the Kalatop–Khajjiar road: we plan your Dalhousie stay and cab in one quote.</p>'
        f'<div class="sza-btns"><a class="sza-btn gold" href="{REEL_WA}" {A}>Get Quote on WhatsApp</a><a class="sza-btn" href="/adventure/kalatop-khajjiar-sanctuary-trek/" style="background:#fff;color:#0b1f33;border:2px solid #0b1f33">Add the Kalatop forest walk</a></div></div></div></section>')

P = "sza-dkd"
html = f'''<!-- {SLUG} — built by Page Builder (night) 11 Nov 2026 from the Research Lead brief + Visual Studio night media @81f251c. Kit v2.0. -->
<style>@media(max-width:900px){{.{P} .sza-hero video{{object-position:20% 50%}}.{P} .sza-hero:after{{background:linear-gradient(180deg,rgba(11,31,51,.5) 0%,rgba(11,31,51,.7) 45%,rgba(11,31,51,.95) 100%)}}}}.{P} .sza-hero-in>*{{max-width:640px}}@media(min-width:901px){{.{P} .sza-hero-in>*{{max-width:min(560px,44vw)}}}}.{P} .sza-chips{{max-width:720px}}.{P} #spots .sza-grid{{grid-template-columns:repeat(auto-fit,minmax(200px,1fr))}}@media(min-width:1000px){{.{P} #experience .sza-steps{{grid-template-columns:repeat(3,1fr)}}}}.{P} #spots .sza-card .img img{{aspect-ratio:3/2;object-fit:cover}}.{P} .sza-media ul{{padding-left:20px;list-style:disc;margin:0}}.{P} .sza-media ul li{{margin:0 0 8px}}.{P} .sza-checks{{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}.{P} .go .x{{margin-right:14px}}.{P} .sza-credit{{font-size:12px;color:#5b6b7a;margin:14px 0 0}}.{P} .sza-credit a{{color:inherit}}</style>
<div class="sza {P}">
<section class="sza-hero">
<video autoplay muted loop playsinline preload="metadata" poster="{U}2026/11/{SLUG}-hero-poster.webp" aria-label="Snowy conifer path, misty stone steps, the snowy Dainkund ridge and the ranges seen from Dalhousie, with a gold route from Dalhousie past Lakkar Mandi to the ridge at 2,755 m"><source src="{CDN}hero.webm" type="video/webm"><source src="{CDN}hero.mp4" type="video/mp4"></video>
<div class="sza-hero-in">
<span class="sza-kicker">Dalhousie · Chamba · 2,755 m</span>
<p class="sza-hero-tag">The highest point around Dalhousie — a short climb above the clouds</p>
<p class="sza-hero-sub">Drive past Lakkar Mandi, walk up to the Pholani Devi temple and see the Pir Panjal and the Ravi valley in one sweep. In winter it is Dalhousie's surest snow.</p>
<ul class="sza-chips"><li><b>Height</b> 2,755 m</li><li><b>Trip</b> Half day</li><li><b>Walk</b> 2–3 km, easy–moderate</li><li><b>Snow</b> Dec–Feb</li><li><b>Top</b> Pholani Devi temple</li><li><b>Price</b> Get Quote</li></ul>
<div class="sza-btns"><a class="sza-btn gold" href="{WA}" {A}>Get Quote on WhatsApp</a><a class="sza-btn ghost" href="{QF}">Add to my Himachal trip</a></div>
<div class="sza-trust"><span><a href="https://suzutravels.com/certificates/">HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022</a></span><span>Hotel + cab in one quote</span><span>Reply within minutes</span></div>
</div>
</section>
<nav class="sza-nav" aria-label="On this page"><div class="sza-nav-in"><a href="#overview">Overview</a><a href="#spots">Spots</a><a href="#experience">Your morning</a><a href="#season">Season</a><a href="#safety">Safety</a><a href="#booking">How booking works</a><a href="#packages">Packages</a><a href="#faq">FAQ</a><a class="cta" href="{WA}" {A}>Get Quote</a></div></nav>

<section class="sza-sec" id="overview">
<span class="sza-kicker">Quick answer</span>
<h2>Dainkund Peak at a glance</h2>
<p class="sza-answer">Dainkund Peak (about 2,755 m) is the highest point near Dalhousie in Chamba district. A road climbs from Dalhousie past Lakkar Mandi towards the Indian Air Force station; you drive as far as allowed, then a paved path of roughly 2–3 km climbs to the Pholani Devi temple on the ridge. Most visitors do it as a half day, often with Kalatop or Khajjiar. Snow usually lies December to February.</p>
<div class="sza-facts"><div class="sza-fact"><div class="k">Height</div><div class="v">About 2,755 m (9,039 ft), Chamba district</div></div><div class="sza-fact"><div class="k">Start</div><div class="v">Road beyond Lakkar Mandi — 30–45 min drive from Dalhousie</div></div><div class="sza-fact"><div class="k">Walk</div><div class="v">About 2–3 km on a paved path, first stretch steep; 45–90 min up</div></div><div class="sza-fact"><div class="k">Best views</div><div class="v">Clear days October–February; snow December–February</div></div><div class="sza-fact"><div class="k">At the top</div><div class="v">Pholani Devi temple (a trident, no idol) and the 'singing hill' wind</div></div><div class="sza-fact"><div class="k">Price</div><div class="v">Get Quote</div></div></div>
</section>

<section class="sza-sec alt" id="spots">
<span class="sza-kicker">Spots &amp; options</span>
<h2>Dainkund and the Lakkar Mandi road</h2>
<p class="sza-lead">The walk is short; the day is what you add to it. Kalatop and Khajjiar sit on the same road, so one cab covers all three.</p>
<div class="sza-grid">{card_html}</div>
<p class="sza-credit">Photos: Dainkund Peak in snow — Abhyuday Bhandari, {CC}; Kalatop–Khajjiar sanctuary — Vishrutpanday, {CC}; Khajjiar — Bittudubeyji, {CC} (Wikimedia Commons). Forest-path photos are illustrative.</p>
</section>

<section class="sza-sec" id="experience">
<span class="sza-kicker">Your morning</span>
<h2>How a Dainkund half day works</h2>
<ol class="sza-steps"><li><h3>Share your dates</h3><p>We plan hotel + cab and check the road after any snowfall.</p></li><li><h3>Early start</h3><p>Leave Dalhousie before 8 am for clear views; drive past Lakkar Mandi.</p></li><li><h3>Drive as far as allowed</h3><p>Park where vehicles are stopped below the Air Force area, then walk up the paved path.</p></li><li><h3>Temple and ridge</h3><p>Pholani Devi temple and the ridge viewpoints; 30–45 min at the top.</p></li><li><h3>Walk down, carry on</h3><p>Continue to Kalatop or Khajjiar, or head back to Dalhousie.</p></li><li><h3>In snow</h3><p>Snow boots or microspikes arranged on request; the cab goes only as far as the cleared road.</p></li></ol>
<div class="sza-media"><video autoplay muted loop playsinline preload="none" poster="{U}2026/11/{SLUG}-explainer-poster.webp" width="1600" height="900" aria-label="Your Dainkund morning: drive from Dalhousie to where vehicles stop, about 2–3 km on a paved path to the ridge and temple at about 2,755 m; Kalatop and Khajjiar on the same road; snow usually December to February; price: Get Quote"><source src="{CDN}explainer.webm" type="video/webm"><source src="{CDN}explainer.mp4" type="video/mp4"></video><div><h3>Your Dainkund morning</h3><ul><li><b>Drive</b> → Dalhousie past Lakkar Mandi to where vehicles stop.</li><li><b>Walk</b> → about 2–3 km on a paved path, 45–90 min up.</li><li><b>Top</b> → ridge and Pholani Devi temple at about 2,755 m.</li><li><b>Same road</b> → Kalatop forest and Khajjiar meadow.</li></ul><p style="margin-top:8px;font-size:14px">Snow usually December to February — keep a buffer day.</p></div></div>
</section>

<section class="sza-sec alt" id="season">
<span class="sza-kicker">When to go</span>
<h2>Best time for Dainkund Peak</h2>
<div class="sza-scroll"><table class="sza-tbl"><thead><tr><th>Months</th><th>What you get</th><th>Note</th></tr></thead><tbody><tr><td>Dec – Feb</td><td>Snow on the ridge and road</td><td>Road can close for hours after snowfall; the BRO clears it — keep a buffer day</td></tr><tr><td>Mar – Jun</td><td>Pleasant, rhododendrons, busy weekends</td><td>June can still bring a freak snow spell (the Dalhousie–Lakkarmandi–Khajjiar road was hit on 22 Jun 2026)</td></tr><tr><td>Jul – Sep</td><td>Monsoon cloud, slippery steps</td><td>Views often hidden; landslide risk on Chamba roads</td></tr><tr><td>Oct – Nov</td><td>Clearest skies, cold mornings</td><td>Best for photos</td></tr></tbody></table></div>
</section>

<div class="sza-band" id="safety"><div class="sza-band-in">
<span class="sza-kicker">Safety &amp; area rules</span>
<h2>What we check before your Dainkund walk</h2>
<p class="sza-lead">Suzu Travels is an HP Tourism registered travel agent (Reg. No. DTO-MND-11-243/2022). We plan your morning around these checks:</p>
<ul class="sza-checks"><li><b>Air Force area</b>The top sits next to an Indian Air Force station — follow the signboards, stay on the public path and never photograph the installation</li><li><b>No drones</b>Dalhousie and Chamba are not free-fly areas; no drone without the required permissions (DigitalSky rules)</li><li><b>After snowfall</b>Go up only once the road is reported cleared, and wear grip footwear — the first stretch is steep</li><li><b>Start early</b>It gets dark and very cold by 5 pm in winter; there is no food or toilet on the path</li><li><b>Elders and kids</b>The height is modest but the climb is steep — go slow; a porter can be arranged on request</li><li><b>No camping</b>The ridge is forest and defence land — no camping or fires</li></ul>
</div></div>

<section class="sza-sec" id="booking">
<span class="sza-kicker">How booking works</span>
<h2>Get a quote in minutes</h2>
<ol class="sza-steps"><li><h3>Tell us</h3><p>WhatsApp or the quote form — dates, people and pickup city.</p></li><li><h3>We check your date</h3><p>Snow, road status and the best day for Dainkund in your plan.</p></li><li><h3>You get one quote</h3><p>Dalhousie hotel and cab together, with any add-ons.</p></li><li><h3>Confirm and go</h3><p>We send the plan and stay in touch on WhatsApp.</p></li></ol>
<p class="sza-lead">Your quote depends on the number of nights in Dalhousie and the hotel category, the cab type and whether you add Kalatop, Khajjiar or Chamba the same day, the season (snow weeks and Christmas–New Year cost more), your pickup point (Pathankot, Chakki Bank railway station, Gaggal airport, Chandigarh or Delhi), add-ons such as a local guide, snow boots or a porter, and group size.</p>
</section>

{reel}

<section class="sza-quote"><div><span class="sza-kicker">Dalhousie snow &amp; views</span><h2>Get your Dainkund quote</h2><p>Tell us your dates, group size and pickup city. We reply with today's rate — hotel and cab included.</p></div><div class="sza-btns"><a class="sza-btn gold" href="{WA}" {A}>Get Quote on WhatsApp</a><a class="sza-btn ghost" href="{QF}">Plan full trip</a></div></section>

<section class="sza-sec" id="packages">
<span class="sza-kicker">Make it a trip</span>
<h2>Pair Dainkund with Khajjiar and Kalatop</h2>
<p><b>Dalhousie + Khajjiar (2N):</b> add a Dainkund morning to our <a href="/dalhousie-tour-package/">Dalhousie tour package</a>, or go further with the <a href="/dharamshala-dalhousie-tour-package/">Dharamshala–Dalhousie tour package</a>. Coming by train? Book the <a href="/cabs/pathankot-to-dalhousie-taxi/">Pathankot to Dalhousie taxi</a>. Plan the day with our <a href="/dalhousie-khajjiar-trip-guide/">Dalhousie–Khajjiar trip guide</a> and the list of <a href="/dalhousie-tourist-places/">Dalhousie tourist places</a>.</p>
<p><b>Chasing snow?</b> Check <a href="/weather/dalhousie/">Dalhousie weather</a>, our <a href="/dalhousie-snowfall/">Dalhousie snowfall guide</a> and the <a href="/snow-tracker/">snow tracker</a>, or read <a href="/himachal-in-december/">Himachal in December</a>. Want a real Dhauladhar trek next? Try the <a href="/adventure/kareri-lake-trek/">Kareri Lake trek</a>, or <a href="{QF}">ask for a custom plan</a>.</p>
</section>

<section class="sza-sec sza-faq" id="faq">
<span class="sza-kicker">FAQ</span>
<h2>Dainkund Peak — questions</h2>
{faq_html}
</section>

<section class="sza-sec alt" id="more">
<span class="sza-kicker">More adventures</span>
<h2>Explore more in Himachal</h2>
<div class="sza-cats"><a class="sza-cat" href="/adventure/kalatop-khajjiar-sanctuary-trek/"><span class="ic">🌲</span><span class="n">Kalatop forest walk</span><span class="c">Dalhousie</span></a><a class="sza-cat" href="/adventure/paragliding-in-khajjiar-dalhousie/"><span class="ic">🪂</span><span class="n">Paragliding in Khajjiar</span><span class="c">Dalhousie</span></a><a class="sza-cat" href="/adventure/kareri-lake-trek/"><span class="ic">🏞️</span><span class="n">Kareri Lake trek</span><span class="c">Dhauladhar</span></a><a class="sza-cat" href="/adventure/snow-activities-manali/"><span class="ic">❄️</span><span class="n">Snow activities</span><span class="c">Manali</span></a><a class="sza-cat" href="/adventure/kamrunag-trek/"><span class="ic">🛕</span><span class="n">Kamrunag temple trek</span><span class="c">Mandi</span></a><a class="sza-cat" href="/adventure/"><span class="ic">🧭</span><span class="n">All adventures</span><span class="c">Air · Water · Snow · Land</span></a></div>
</section>
</div>'''

pathlib.Path(__file__).with_name(f"{SLUG}.html").write_text(html, encoding="utf-8")
print("ok", len(html))
