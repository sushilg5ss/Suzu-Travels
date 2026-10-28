#!/usr/bin/env python3
# Generates adventure-kit/pages/bhrigu-lake-trek.html (Page Builder night, 28 Oct 2026)
import urllib.parse, pathlib
SLUG = "bhrigu-lake-trek"
HERE = pathlib.Path(__file__).resolve().parent
CDN = "https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@cbe9b44a4a87ee851ec6d19a3ae387ea3f9da3cc/adventure-kit/media/bhrigu-lake-trek/"
UP = "https://suzutravels.com/wp-content/uploads/2026/10/"
QUOTE = "/himachal-tour-packages-quote/?activity=" + urllib.parse.quote("Bhrigu Lake trek")
WHAT = "the Bhrigu Lake trek from Gulaba, Manali"

def wa(what=WHAT, tag=SLUG):
    t = f"Hi Suzu Travels, I want a quote for {what}. Travel date: ___ , people: ___ (page: {tag})"
    return "https://wa.me/917087488961?text=" + urllib.parse.quote(t, safe="")

def walink(label, what=WHAT, cls="sza-btn gold"):
    return f'<a class="{cls}" href="{wa(what)}" target="_blank" rel="noopener">{label}</a>'

MAIN = wa()

def card(src, w, h, alt, badge, title, meta, text, what, extra=""):
    return (f'<article class="sza-card"><div class="img"><img src="{src}" alt="{alt}" loading="lazy" width="{w}" height="{h}"><span class="sza-badge">{badge}</span></div>'
            f'<div class="body"><h3>{title}</h3><div class="meta">{meta}</div><p class="meta">{text}</p>'
            f'<div class="go">{extra}<a class="q" href="{wa(what)}" target="_blank" rel="noopener">Get Quote →</a></div></div></article>')

cards = "".join([
    card(f"{UP}trek-tents-meadow-stream-valley-768x1024.webp", 768, 1024,
         "Row of orange trek tents on a green meadow beside a stream in a steep mountain valley",
         "Classic pick", "Classic 3 days, Gulaba – Gulaba", "<b>Rola Kholi camp → lake → back</b>",
         "Walk to the Rola Kholi camp (about 3,820 m) on day 1, climb to the lake and back on day 2, walk out the same way on day 3.",
         "the classic 3-day Bhrigu Lake trek from Gulaba, Manali"),
    card(f"{UP}trek-tents-grassy-mountain-bowl-768x1024.webp", 768, 1024,
         "Trek camp tents pitched on a green grassy slope below high mountains and clouds",
         "Best views", "Loop, Gulaba – Vashisht", "<b>Down via Pandu Ropa meadows</b>",
         "Cross from the lake to the Pandu Ropa meadows and walk down to Vashisht and its hot springs, near Manali.",
         "the Bhrigu Lake loop trek from Gulaba to Vashisht, Manali"),
    card(f"{UP}hiker-rock-above-cloud-valley-768x509.webp", 768, 509,
         "Hiker sitting on a rock outcrop above a valley filled with low white cloud",
         "First trek", "4 days with a Manali rest day", "<b>One extra night for altitude</b>",
         "Spend a night in Manali before you climb — the trek gains about 1,300 m in two days.",
         "a 4-day Bhrigu Lake trek with a Manali rest day"),
])

steps_exp = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Day 0 — arrive in Manali", "Rest at your hotel in Manali (about 2,050 m), meet the trek team for a kit check and briefing."),
    ("Day 1 — Gulaba to Rola Kholi", "Cab up the Rohtang road to Gulaba (about 3,000 m), then about 7–8 km (4–5 hours) through the Jonker Thach meadows to the Rola Kholi camp (about 3,820 m)."),
    ("Day 2 — up to the lake", "A steep climb of about 2 hours to the first ridge, then on to Bhrigu Lake (about 4,235–4,300 m) and back to camp, or across to Pandu Ropa — about 12–14 km, 7–8 hours."),
    ("Day 3 — back to Manali", "Walk down to Gulaba, or about 8 km down to Vashisht on the loop; your cab drives you to your hotel."),
    ("Start early, finish before dark", "Leave camp early and be back before dark. Never walk down alone or after sunset on this route."),
    ("Hotel and cab included", "We add your Manali hotel nights and the cab to Gulaba and back in the same quote."),
])

booking = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Tell us your dates", "WhatsApp or the quote form — dates, group size, ages, fitness and where you start from."),
    ("We check your date", "Trail, snow and road conditions for your month, and a guide and camp with a registered local operator."),
    ("You get one quote", "Trek, Manali hotel nights and the cab to Gulaba and back in one plan."),
    ("Confirm and go", "We send the kit list, reporting time and what to expect before you travel."),
])

faqs = [
    ("How long is the Bhrigu Lake trek?", "About 24 km out and back from Gulaba over 3–4 days. The loop down to Vashisht is about 27–30 km."),
    ("What is the height of Bhrigu Lake?", "About 4,235–4,300 m, roughly 14,000 ft. Wikipedia gives 4,235 m; most trek guides say about 4,300 m."),
    ("Where does the Bhrigu Lake trek start?", "At Gulaba, about 22–26 km from Manali on the Rohtang road. Some treks end at Vashisht, near Manali."),
    ("What is the best time for the Bhrigu Lake trek?", "September to mid-October for clear skies; June for snow. From November the trail is under snow and regular treks stop."),
    ("Do I need a Rohtang permit for the trek?", 'Not for the trek itself — the <a href="/rohtang-pass-permit-himachal-road-status/">Rohtang permit</a> is for vehicles going beyond the Gulaba barrier. A cab drop at Gulaba is enough.'),
    ("Is the Bhrigu Lake trek good for beginners?", "Yes, for fit beginners. It is non-technical but climbs about 1,300 m in two days, so rest a day in Manali first."),
    ("Does Bhrigu Lake freeze?", "It can stay partly frozen into June, and nights at the lake drop below freezing from late September."),
    ("Can I camp at Bhrigu Lake?", "Treks camp lower, at Rola Kholi or Pandu Ropa. Camping at the lake itself is not advised."),
]
faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)

more = [
    ("/adventure/hampta-pass-trek/", "🥾", "Hampta Pass Trek", "Kullu to Lahaul crossover"),
    ("/adventure/beas-kund-trek/", "🏞️", "Beas Kund Trek", "Source of the Beas, Solang"),
    ("/adventure/camping-in-manali/", "⛺", "Camping in Manali", "Riverside and forest camps"),
    ("/adventure/paragliding-in-manali/", "🪂", "Paragliding in Manali", "Fly before your trek"),
    ("/adventure/snow-activities-manali/", "❄️", "Snow in Manali", "For winter months"),
    ("/adventure/", "⛰️", "All adventures", "Air · Water · Snow · Land"),
]
more_html = "".join(f'<a class="sza-cat" href="{h}"><span class="ic">{i}</span><span class="n">{n}</span><span class="c">{c}</span></a>' for h, i, n, c in more)

reel = (HERE.parent / "media" / SLUG / "reel-section.html").read_text(encoding="utf-8").strip()

page = f'''<!-- bhrigu-lake-trek — built by Page Builder (night) 28 Oct 2026 from the Research Lead brief 27 Oct + Visual Studio media @cbe9b44 (reel-section @9ed252f). Kit v1.8. No prices, no operator names; heights "about"; TMS link, campsite fees, winter road status and 2026 monsoon order left off (unverified). Photos generic, neutral alt. -->
<style>.sza-blt .sza-hero-in>*{{max-width:620px}}.sza-blt .sza-chips{{max-width:700px}}.sza-blt #experience .sza-steps{{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}.sza-blt .sza-media ul{{padding-left:20px;list-style:disc;margin:0}}.sza-blt .sza-media ul li{{margin:0 0 8px}}.sza-blt .sza-media img{{height:auto;aspect-ratio:4/3;object-fit:cover}}.sza-blt .sza-media video{{height:auto;aspect-ratio:16/9}}.sza-blt #spots .sza-grid{{grid-template-columns:repeat(auto-fit,minmax(240px,1fr))}}.sza-blt #spots .sza-card .img img{{aspect-ratio:3/2;object-fit:cover}}.sza-blt .sza-checks{{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}.sza-blt .sza-choose{{margin-top:32px}}.sza-blt .go .x{{margin-right:14px}}@media(max-width:820px){{.sza-blt .sza-hero video{{object-position:30% 50%}}.sza-blt .sza-hero:after{{background:linear-gradient(180deg,rgba(11,31,51,.35) 0%,rgba(11,31,51,.6) 40%,rgba(11,31,51,.94) 100%)}}}}</style>
<div class="sza sza-blt">
<section class="sza-hero">
<video autoplay muted loop playsinline preload="metadata" poster="{UP}bhrigu-lake-trek-hero-poster.webp" aria-label="A trekker on a ridge at sunrise, a hiker above a cloud-filled valley, lit tents on a meadow at dusk and a clear lake below snow-streaked peaks, with a gold trail from Gulaba past Rola Kholi camp to the lake, rising from about 3,000 m to about 4,235 m; about 24 km out and back in 3 to 4 days from Manali, season June to mid-October"><source src="{CDN}hero.webm" type="video/webm"><source src="{CDN}hero.mp4" type="video/mp4"></video>
<div class="sza-hero-in">
<span class="sza-kicker">Bhrigu Lake trek · Manali, Kullu</span>
<p class="sza-hero-tag">A high glacial lake above Manali in three days</p>
<p class="sza-hero-sub">Gulaba to the lake and back, with a guide, camps, cab and your Manali hotel in one quote.</p>
<ul class="sza-chips"><li><b>Lake</b> ~4,235–4,300 m</li><li><b>Start</b> Gulaba, ~22–26 km from Manali</li><li><b>Distance</b> ~24 km out and back</li><li><b>Days</b> 3–4</li><li><b>Season</b> June – mid-Oct</li><li><b>Price</b> Get Quote</li></ul>
<div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan my trek</a></div>
<div class="sza-trust"><span><a href="https://suzutravels.com/certificates/">HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022</a></span><span>Trek + hotel + cab</span><span>Reply within minutes</span></div>
</div>
</section>
<nav class="sza-nav" aria-label="On this page"><div class="sza-nav-in"><a href="#overview">Overview</a><a href="#spots">Options</a><a href="#experience">Day by day</a><a href="#season">Best time</a><a href="#safety">Safety</a><a href="#booking">How booking works</a><a href="#packages">Packages</a><a href="#faq">FAQ</a><a class="cta" href="{MAIN}" target="_blank" rel="noopener">Get Quote</a></div></nav>

<section class="sza-sec" id="overview">
<span class="sza-kicker">Quick answer</span>
<h2>Bhrigu Lake trek, at a glance</h2>
<p class="sza-answer">The Bhrigu Lake trek is a 3–4 day walk from Gulaba, about 22–26 km above Manali on the Rohtang road, to a small glacial lake at about 4,235–4,300 m. You camp at Rola Kholi, climb to the lake on day two and return to Gulaba or down to Vashisht. The season runs June to mid-October; in winter the trail is under deep snow.</p>
<div class="sza-facts"><div class="sza-fact"><div class="k">Lake height</div><div class="v">About 4,235–4,300 m (roughly 14,000 ft)</div></div><div class="sza-fact"><div class="k">Start</div><div class="v">Gulaba, about 3,000 m; return to Gulaba or loop down to Vashisht</div></div><div class="sza-fact"><div class="k">Distance</div><div class="v">About 24 km out and back; about 27–30 km on the Vashisht loop</div></div><div class="sza-fact"><div class="k">Days</div><div class="v">3–4 days Manali to Manali (a rest day in Manali first is wise)</div></div><div class="sza-fact"><div class="k">Season</div><div class="v">June – mid-October; June has snow and the lake may be partly frozen</div></div><div class="sza-fact"><div class="k">Price</div><div class="v">Get Quote</div></div></div>
</section>

<section class="sza-sec alt" id="spots">
<span class="sza-kicker">Your options</span>
<h2>Ways to do the Bhrigu Lake trek</h2>
<p class="sza-lead">Pick the plan that fits your group. Photos show Himalayan trails and camps in general.</p>
<div class="sza-grid">{cards}</div>
<div class="sza-media sza-choose" id="route"><video autoplay muted loop playsinline preload="none" poster="{UP}bhrigu-lake-trek-explainer-poster.webp" width="1600" height="900" aria-label="Your three Bhrigu days: cab from Manali to Gulaba at about 3,000 m, day 1 about 7 to 8 km to Rola Kholi camp at about 3,820 m, day 2 a steep climb of about 2 hours to Bhrigu Lake at about 4,235 m and back to camp, day 3 back down; season June to mid-October, July and August monsoon, November to May snow; guide, camp, hotel and cab, price on quote"><source src="{CDN}explainer.webm" type="video/webm"><source src="{CDN}explainer.mp4" type="video/mp4"></video><div><h3>Your three Bhrigu days</h3><ul><li><b>Manali → Gulaba</b> → cab up the Rohtang road to about 3,000 m.</li><li><b>Day 1</b> → about 7–8 km to Rola Kholi camp (about 3,820 m).</li><li><b>Day 2</b> → steep 2-hour wall, then the lake and back to camp.</li><li><b>Day 3</b> → down to Gulaba or Vashisht, cab to your hotel.</li></ul></div></div>
</section>

<section class="sza-sec" id="experience">
<span class="sza-kicker">Day by day</span>
<h2>How your Bhrigu Lake trek works</h2>
<ol class="sza-steps">{steps_exp}</ol>
<div class="sza-media"><img src="{UP}lit-tents-meadow-campsite-dusk-768x512.webp" alt="Lit dome tents on a grassy campsite at dusk below a dark hill and a deep blue sky" loading="lazy" width="768" height="512"><div><h3>Nights at the meadow camp</h3><p>You sleep in tents at Rola Kholi, a high meadow at about 3,820 m. The trek team sets up camp and cooks; you carry a day pack, or add a porter or mule for your backpack.</p><p>There is no mobile network beyond Gulaba. Carry 2 litres of water and refill at the streams before Rola Kholi, and pack a warm layer and a rain shell — nights are cold even in summer.</p></div></div>
</section>

<section class="sza-sec alt" id="season">
<span class="sza-kicker">When to go</span>
<h2>Best time for the Bhrigu Lake trek</h2>
<div class="sza-scroll"><table class="sza-tbl"><thead><tr><th>Months</th><th>Trail</th><th>Our advice</th></tr></thead><tbody><tr><td>Nov – May</td><td>Deep snow, camps closed</td><td>Closed for regular treks; plan for June</td></tr><tr><td>June</td><td>Snow above about 12,000 ft; the lake may be partly frozen</td><td>Good for snow views; microspikes on request</td></tr><tr><td>July – Aug</td><td>Monsoon rain, green meadows and flowers</td><td>Possible, but slippery; we watch road and weather alerts</td></tr><tr><td>Sept – mid-Oct</td><td>Clear skies; nights below freezing at the lake</td><td>Best for first-timers</td></tr></tbody></table></div>
<p style="margin-top:14px">Planning for 2027? The trail opens again in June. Until then, see <a href="/adventure/snow-activities-manali/">snow activities in Manali</a> for a winter trip to the same valley.</p>
</section>

<div class="sza-band" id="safety"><div class="sza-band-in">
<span class="sza-kicker">Safety first</span>
<h2>What we check before we book your trek</h2>
<p class="sza-lead">Suzu Travels is an <a href="https://suzutravels.com/certificates/" style="color:#f3d98f;text-decoration:underline">HP Tourism registered travel agent (Reg. No. DTO-MND-11-243/2022)</a>. We arrange the trek only with registered local operators and a guide, and plan around these checks:</p>
<ul class="sza-checks"><li><b>Registered guide only</b>Trekking guides and operators fall under Himachal's adventure tourism rules (registration and insurance), and Kullu district asks trekking groups to register as it directs.</li><li><b>Never alone, never after dark</b>Trek in a group with a guide, start early and be back at camp before dark. Tell us your planned return time.</li><li><b>Altitude</b>The trek climbs about 1,300 m in two days. Rest a day in Manali first and turn back on headache, vomiting or breathlessness.</li><li><b>Season end</b>Early snow after mid-October ends the season, so we do not book winter attempts.</li><li><b>No network</b>There is no mobile signal beyond Gulaba; your guide keeps the group together and knows the way down.</li><li><b>Weather alerts</b>In July–August we follow weather alerts and any district orders for your dates.</li></ul>
</div></div>

<section class="sza-sec" id="booking">
<span class="sza-kicker">How booking works</span>
<h2>Get a quote in minutes</h2>
<ol class="sza-steps">{booking}</ol>
<div class="sza-media"><img src="{UP}turquoise-glacial-lake-boulders-snow-768x1024.webp" alt="Small turquoise glacial lake ringed by boulders below snow-streaked peaks" loading="lazy" width="768" height="1024"><div><h3>What your quote depends on</h3><ul><li>Group size, and 3 or 4 days</li><li>Gulaba return or the Vashisht loop</li><li>Camps, meals, guide, and porter or mule load</li><li>Cab Manali – Gulaba both ways (and from Chandigarh or Delhi)</li><li>Manali hotel nights before and after</li><li>Gear arranged on request (jacket, poles, microspikes in June) — today's rate on WhatsApp within minutes</li></ul></div></div>
</section>

{reel}

<section class="sza-quote"><div><span class="sza-kicker">Ready for the lake?</span><h2>Get your Bhrigu Lake trek quote</h2><p>Tell us your dates and group size. We reply with one plan — trek, Manali hotel and the cab both ways — for your dates within minutes.</p></div><div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan full trip</a></div></section>

<section class="sza-sec" id="packages">
<span class="sza-kicker">Make it a trip</span>
<h2>Manali + Bhrigu Lake + Solang</h2>
<p>A good plan is <b>Delhi or Chandigarh → Manali 2 nights → the 3-day Bhrigu Lake trek → Manali 1 night</b>, with a Solang or Atal Tunnel day, or a <a href="/adventure/paragliding-in-manali/">paragliding flight</a> in September–October. Read our <a href="/manali/">Manali guide</a>, see the <a href="/himachal-tour-package-from-delhi/">Himachal tour package from Delhi</a>, or browse <a href="/adventure/adventure-activities-in-manali/">adventure activities in Manali</a>. Want another trek? Try the <a href="/adventure/beas-kund-trek/">Beas Kund trek</a> below <a href="/mountains-of-india/hanuman-tibba/">Hanuman Tibba</a>, or the <a href="/adventure/hampta-pass-trek/">Hampta Pass trek</a> from Kullu to Lahaul. Prefer a night out without the climb? See <a href="/adventure/camping-in-manali/">camping in Manali</a>.</p>
<div class="sza-btns" style="margin-top:18px">{walink("Manali + Bhrigu Lake trip — Get Quote", what="a Manali + Bhrigu Lake trek trip")}{walink("Winter Manali snow trip — Get Quote", what="a winter Manali snow trip", cls="sza-btn line")}</div>
</section>

<section class="sza-sec sza-faq" id="faq">
<span class="sza-kicker">FAQ</span>
<h2>Bhrigu Lake trek — questions</h2>
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
