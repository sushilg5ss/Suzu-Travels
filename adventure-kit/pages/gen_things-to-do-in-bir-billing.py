#!/usr/bin/env python3
"""Generator for /adventure/things-to-do-in-bir-billing/ — Page Builder (night) 24 Oct 2026 IST.
Source: Research Lead brief 23 Oct 2026 (morning) + Visual Studio media @df23190 (reel section @ec90371).
Writes things-to-do-in-bir-billing.html next to this file; then: python3 ../build.py things-to-do-in-bir-billing.html > things-to-do-in-bir-billing.min.html
"""
import pathlib, urllib.parse

SLUG = "things-to-do-in-bir-billing"
SHA = "df231905233c4f3bf5c1fc70ed2158d22bc1d298"
CDN = f"https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@{SHA}/adventure-kit/media/{SLUG}/"
UP = "https://suzutravels.com/wp-content/uploads/2026/"
QUOTE = "/himachal-tour-packages-quote/?activity=" + urllib.parse.quote("Bir Billing activities")


def wa(what, tag=""):
    msg = (f"Hi Suzu Travels, I want a quote for {what}. Travel date: ___ , people: ___ "
           f"(page: {SLUG}{tag})")
    return "https://wa.me/917087488961?text=" + urllib.parse.quote(msg, safe="")


def a_wa(what, label, cls="", tag=""):
    c = f' class="{cls}"' if cls else ""
    return f'<a{c} href="{wa(what, tag)}" target="_blank" rel="noopener">{label}</a>'


MAIN = "a Bir Billing trip (activities, stay and cab)"

cards = [
    ("10/paraglider-orange-wing-green-mountain-valley-768x512.webp", 768, 512,
     "Paraglider with an orange wing flying over a green mountain valley",
     "Main draw", "Tandem paragliding", "Billing ~2,400 m → Bir ~1,400 m",
     "Jeep 14 km up to Billing, 15–30 minutes in the air, land in Bir's Chowgan fields. 12 years+ and 30 kg+.",
     "tandem paragliding in Bir Billing", "/adventure/paragliding-in-bir-billing/"),
    ("10/bungee-jumper-leap-platform-green-gorge-768x512.webp", 768, 512,
     "Bungee jumper leaping from a platform over a green forested gorge",
     "Only verified jump", "Bungee jump", "Near Slabak, close to the landing area",
     "Himachal's verified bungee site, set up in 2018 — fly in the morning, jump later the same day.",
     "a bungee jump at Bir", "/adventure/bungee-jumping-in-himachal/"),
    ("04/dalai-lama-temple-mcleod-ganj-dharamshala-tour-768x512.webp", 768, 512,
     "Prayer flags over a Tibetan monastery roof",
     "Culture", "Tibetan colony &amp; monasteries", "Chokling Monastery · Sherab Ling (Bhattu)",
     "Chokling Monastery's big stupa sits in the colony; Palpung Sherab Ling is about 7 km away. Colony cafés after the flight.",
     "a Bir trip with the Tibetan colony and monasteries", None),
    ("10/dome-tents-hilltop-meadow-sunrise-768x498.webp", 768, 498,
     "Dome tents on a grassy hilltop meadow at sunrise with blue mountain ridges behind",
     "Overnight", "Billing–Rajgundha trek &amp; camp", "About 4–5 hours from the take-off",
     "Walk on from Billing to Rajgundha meadow for a night under the Dhauladhar — guided, arranged on request.",
     "the Billing–Rajgundha trek with a camp night", "/adventure/camping-in-himachal/"),
    ("10/terraced-tea-garden-green-hills-768x1151.webp", 768, 1151,
     "Rows of tea bushes on terraced slopes below a forested green hill",
     "Easy half-day", "Waterfall &amp; village walks", "Gunehar · Bangoru",
     "Gunehar waterfall (about 100 ft) is a short walk from Bir; Bangoru falls is reached from the colony.",
     "waterfall and village walks in Bir", None),
    ("10/mountain-bikers-dirt-road-green-hills-768x1152.webp", 768, 1152,
     "Three riders cycling mountain bikes along a dirt road between green trees",
     "Slow day", "Cycling, tea &amp; Baijnath", "Village roads · tea gardens",
     "Ride village roads and the Chowgan tea gardens by bike; stop at Baijnath's Shiva temple on the drive in.",
     "cycling and a tea-garden day in Bir", None),
]

card_html = ""
for img, w, h, alt, badge, name, meta, txt, what, x in cards:
    xl = f'<a class="x" href="{x}">Explore →</a>' if x else ""
    card_html += (f'<article class="sza-card"><div class="img"><img src="{UP}{img}" alt="{alt}" loading="lazy" '
                  f'width="{w}" height="{h}"><span class="sza-badge">{badge}</span></div><div class="body"><h3>{name}</h3>'
                  f'<div class="meta"><b>{meta}</b></div><p class="meta">{txt}</p><div class="go">'
                  f'{a_wa(what, "Get Quote →", "q")}{xl}</div></div></article>')

faqs = [
    ("What can you do in Bir Billing besides paragliding?",
     "Bungee near Slabak, the Tibetan colony monasteries (Chokling, and Sherab Ling at Bhattu), Gunehar waterfall and village walks, cycling through tea gardens and the Billing–Rajgundha trek."),
    ("How many days are enough for Bir Billing?",
     "Two days covers a flight, the monasteries and one more activity. Add a third for the Rajgundha trek, or as a buffer if weather grounds the flight."),
    ("What is the best time to visit Bir Billing?",
     "Mid-September to November and March to June. Paragliding is closed every year from 15 July to 15 September."),
    ("Is Bir Billing worth visiting in winter?",
     "Yes for monasteries, walks and flights on clear days, but mornings are cold and snow can close the Billing road — keep a spare day."),
    ("Can we do bungee and paragliding on the same day?",
     "Yes, both are at Bir. Fly in the morning and jump later, subject to weather and slots."),
    ("What is the minimum age for paragliding at Bir?",
     "HP rules allow no passengers under 12 years or under 30 kg. See <a href=\"/adventure/paragliding-in-bir-billing/\">paragliding in Bir Billing</a> for the full rules."),
    ("How far is Bir from Dharamshala and Palampur?",
     "About 70 km from Dharamshala and about 35 km from Palampur. The nearest airport is Kangra (Gaggal), and the toy-train halt at Ahju is about 3 km away."),
    ("How much does a Bir Billing trip cost?",
     "Get Quote. It depends on activities, nights, stay and cab — send your dates on WhatsApp for today's rate."),
]
faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)

reel = pathlib.Path(__file__).resolve().parent.parent.joinpath("media", SLUG, "reel-section.html").read_text(encoding="utf-8").strip()

html = f'''<!-- {SLUG} — built by Page Builder (night) 24 Oct 2026 IST from the Research Lead brief 23 Oct (morning) + Visual Studio media @df23190. Kit v1.8. No prices, no operator names. Kept off (unverified): Rajgundha permits/camping rules, hang-gliding/parasailing, events, exact Baijnath/Sherab Ling distances ('about'), course details, 'best site in the world' claims. Generic photos carry neutral alt text (never Bir/Chokling). -->
<style>.sza-bir .sza-hero-in>*{{max-width:620px}}.sza-bir .sza-chips{{max-width:700px}}.sza-bir .sza-media ul{{padding-left:20px;list-style:disc;margin:0}}.sza-bir .sza-media ul li{{margin:0 0 8px}}.sza-bir .sza-media img{{height:auto;aspect-ratio:3/2;object-fit:cover}}.sza-bir .sza-media video{{height:auto;aspect-ratio:16/9}}.sza-bir #spots .sza-grid{{grid-template-columns:repeat(auto-fit,minmax(min(300px,100%),1fr))}}.sza-bir #spots .sza-card .img img{{aspect-ratio:3/2;object-fit:cover}}.sza-bir .sza-checks{{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}.sza-bir .sza-choose{{margin-top:32px}}@media(max-width:820px){{.sza-bir .sza-hero video{{object-position:70% 50%}}.sza-bir .sza-hero:after{{background:linear-gradient(180deg,rgba(11,31,51,.35) 0%,rgba(11,31,51,.6) 40%,rgba(11,31,51,.94) 100%)}}}}</style>
<div class="sza sza-bir">
<section class="sza-hero">
<video autoplay muted loop playsinline preload="metadata" poster="{UP}10/things-to-do-in-bir-billing-hero-poster.webp" aria-label="A paraglider beside green slopes, a bungee jumper over a forested gorge, prayer flags over a monastery roof and tents on a meadow at sunrise, with a gold glide line from Billing at about 2,400 m down to Bir at about 1,400 m: fly, jump, trek and stay"><source src="{CDN}hero.webm" type="video/webm"><source src="{CDN}hero.mp4" type="video/mp4"></video>
<div class="sza-hero-in">
<span class="sza-kicker">Place guide · Bir, Kangra</span>
<p class="sza-hero-tag">Fly, jump, trek and slow down in one valley</p>
<p class="sza-hero-sub">Tandem flights from Billing, Himachal's verified bungee, monasteries and a camp night — planned with your hotel and cab in one quote.</p>
<ul class="sza-chips"><li><b>Take-off</b> Billing ~2,400 m</li><li><b>Land</b> Bir ~1,400 m</li><li><b>Best</b> Mid-Sep–Nov · Mar–Jun</li><li><b>Flying closed</b> 15 Jul–15 Sep</li><li><b>2–3 days</b> ideal</li><li><b>Price</b> Get Quote</li></ul>
<div class="sza-btns">{a_wa(MAIN, "Get Quote on WhatsApp", "sza-btn gold")}<a class="sza-btn ghost" href="{QUOTE}">Plan my trip</a></div>
<div class="sza-trust"><span><a href="https://suzutravels.com/certificates/">HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022</a></span><span>Activities + stay + cab</span><span>Reply within minutes</span></div>
</div>
</section>
<nav class="sza-nav" aria-label="On this page"><div class="sza-nav-in"><a href="#overview">Overview</a><a href="#spots">Things to do</a><a href="#experience">2-day plan</a><a href="#season">By month</a><a href="#safety">Safety</a><a href="#booking">How booking works</a><a href="#packages">Trips</a><a href="#faq">FAQ</a>{a_wa(MAIN, "Get Quote", "cta")}</div></nav>

<section class="sza-sec" id="overview">
<span class="sza-kicker">Quick answer</span>
<h2>Things to do in Bir Billing, at a glance</h2>
<p class="sza-answer">Bir Billing in Kangra is best known for tandem paragliding from Billing (about 2,400 m) down to Bir (about 1,400 m), but one trip can also hold Himachal's only verified bungee jump, the Tibetan colony monasteries, waterfall walks, mountain biking and the Billing–Rajgundha trek with a camp night. Fly mid-September to November or March to June; flying stops 15 July–15 September.</p>
<div class="sza-facts"><div class="sza-fact"><div class="k">Where</div><div class="v">Bir, Baijnath tehsil, Kangra — about 35 km from Palampur, about 70 km from Dharamshala; Billing is 14 km above Bir by a narrow hill road</div></div><div class="sza-fact"><div class="k">Main draw</div><div class="v">Tandem paragliding Billing → Bir with registered pilots; 12 years+ and 30 kg+ (HP Aero Sports Rules)</div></div><div class="sza-fact"><div class="k">Also here</div><div class="v">Bungee near Slabak, monasteries (Chokling, Sherab Ling), Gunehar waterfall walk, cycling, Billing–Rajgundha trek</div></div><div class="sza-fact"><div class="k">Best months</div><div class="v">Mid-Sep–Nov and Mar–Jun; Dec–Feb open but cold, Billing can get snow</div></div><div class="sza-fact"><div class="k">Closed</div><div class="v">Paragliding 15 Jul–15 Sep every monsoon (district order)</div></div><div class="sza-fact"><div class="k">Price</div><div class="v">Get Quote</div></div></div>
</section>

<section class="sza-sec alt" id="spots">
<span class="sza-kicker">What to do</span>
<h2>Six things to do in Bir Billing</h2>
<p class="sza-lead">One valley, two levels: Billing on top for the take-off and the Rajgundha trail, Bir below for the landing, monasteries, bungee and walks.</p>
<div class="sza-grid">{card_html}</div>
</section>

<section class="sza-sec" id="experience">
<span class="sza-kicker">Your 2-day plan</span>
<h2>How a Bir Billing trip works</h2>
<ol class="sza-steps"><li><h3>Send your dates</h3><p>Date and group on WhatsApp; we check the flying forecast and send today's rate for the whole trip.</p></li><li><h3>Arrive</h3><p>By cab from Delhi, Chandigarh, Dharamshala or a Manali route; check in at Bir, Palampur or a camp.</p></li><li><h3>Day 1: fly</h3><p>Jeep up to Billing and fly the tandem while the air is calm; afternoon monasteries and colony cafés.</p></li><li><h3>Day 2: jump or walk</h3><p>Bungee near Slabak, Gunehar waterfall or cycling through tea gardens — also your buffer morning if day 1 was grounded.</p></li><li><h3>Add-on night</h3><p>Walk Billing → Rajgundha with a guide and camp, or move on to Dharamshala / McLeodganj.</p></li><li><h3>Carry on</h3><p>Drive back, or continue your Himachal tour with the same cab.</p></li></ol>
<div class="sza-media"><video autoplay muted loop playsinline preload="none" poster="{UP}10/bir-billing-one-valley-two-levels-explainer.webp" width="1600" height="900" aria-label="13-second motion graphic: One valley, two levels. Billing at about 2,400 m has the take-off and the Rajgundha trail head, with snow possible December to February; a 14 km hill road runs down to Bir at about 1,400 m with the landing fields, monasteries, bungee, a waterfall walk and tea gardens. Your 2 Bir days: day 1 fly in the calm morning, then monasteries and colony cafés; day 2 bungee, walk or cycle, which is also your buffer morning. No flying 15 July to 15 September."><source src="{CDN}explainer.webm" type="video/webm"><source src="{CDN}explainer.mp4" type="video/mp4"></video><div><h3>One valley, two levels</h3><ul><li><b>Billing ~2,400 m</b> → take-off and the Rajgundha trail head; snow possible Dec–Feb.</li><li><b>14 km hill road</b> → the jeep ride up for your flight.</li><li><b>Bir ~1,400 m</b> → landing fields, monasteries, bungee, waterfall walk, tea gardens.</li><li><b>Weather decides</b> the flying day — keep a spare morning.</li></ul><p>We check the forecast and the Billing road for your dates before we book.</p></div></div>
</section>

<section class="sza-sec alt" id="season">
<span class="sza-kicker">When to go</span>
<h2>Bir Billing by month</h2>
<div class="sza-scroll"><table class="sza-tbl"><thead><tr><th>Months</th><th>Flying</th><th>On the ground</th><th>What to expect</th></tr></thead><tbody><tr><td>Mid-Sep – Nov</td><td>Best</td><td>All open</td><td>Clear post-monsoon air and the busiest window — the 2026 season began on 20 Sep with about 200 flights a day. Rain days still ground flights, so keep a spare morning.</td></tr><tr><td>Dec – Feb</td><td>Open, weather permitting</td><td>Walks, monasteries, bungee</td><td>Cold mornings and short days; the Billing road and take-off can get snow (6 inches on 6 Oct 2025 suspended flying).</td></tr><tr><td>Mar – Jun</td><td>Very good</td><td>Best for the Rajgundha trek</td><td>Strong thermals, longer flights possible, busy weekends; cloud builds after midday by June.</td></tr><tr><td>15 Jul – 15 Sep</td><td>Closed</td><td>Walks only; landslide and leech risk</td><td>Monsoon ban on paragliding; treks not advised.</td></tr></tbody></table></div>
</section>

<div class="sza-band" id="safety"><div class="sza-band-in">
<span class="sza-kicker">Safety</span>
<h2>The rules we check before we book</h2>
<p class="sza-lead">Suzu Travels is an <a href="https://suzutravels.com/certificates/" style="color:#f3d98f;text-decoration:underline">HP Tourism registered travel agent (Reg. No. DTO-MND-11-243/2022)</a>. We arrange each activity with registered local operators and check these first:</p>
<ul class="sza-checks"><li><b>Registered pilots only</b>Pilots registered with HP Tourism at the notified Billing site, insured; no passengers under 12 years or 30 kg, no stunts with passengers (HP Aero Sports Rules 2022, amended 2025).</li><li><b>District committee rules</b>Kangra's Aero Sports Regulatory Committee sets timings, a daily flight limit per pilot and no flying in bad weather; long cross-country flights only in groups with GPS trackers.</li><li><b>Weather call is final</b>Bad weather can ground flights even in peak weeks (it did on 21 Oct 2026) — always plan a buffer morning.</li><li><b>Monsoon</b>No flying 15 Jul–15 Sep; avoid the Billing road and treks in heavy rain.</li><li><b>Snow</b>The Billing road shuts to vehicles after snowfall — in winter we confirm the road on the morning.</li><li><b>Bungee and treks</b>We confirm bungee age and weight limits for your date — tell us about back, heart or pregnancy issues. Rajgundha walks go with a local guide; carry warm layers, Billing is about 1,000 m higher than Bir.</li></ul>
</div></div>

<section class="sza-sec" id="booking">
<span class="sza-kicker">How booking works</span>
<h2>Get a quote in minutes</h2>
<ol class="sza-steps"><li><h3>Tell us</h3><p>WhatsApp or the quote form — dates, group, activities and where you start.</p></li><li><h3>We check your date</h3><p>Flying forecast, the Billing road, bungee slots and a guide for the trek.</p></li><li><h3>You get one quote</h3><p>Activities, stay and cab in one plan.</p></li><li><h3>Confirm and go</h3><p>We send pickup times, meeting points and what to carry.</p></li></ol>
<div class="sza-media"><img src="{UP}10/dome-tents-hilltop-meadow-sunrise-768x498.webp" alt="Dome tents on a grassy hilltop meadow at sunrise with blue mountain ridges behind" loading="lazy" width="768" height="498"><div><h3>What your quote depends on</h3><ul><li>Which activities: flight length, bungee, guided Rajgundha trek and camp, cycle hire</li><li>Flight video or photos and pickup to the take-off</li><li>Your dates (weekends, the Oct–Nov peak, New Year) and number of people</li><li>Stay: Bir guesthouse, Palampur hotel or a camp, and number of nights</li><li>Cab from your city (Delhi, Chandigarh, Pathankot, Dharamshala, Manali)</li><li>Add-ons: Dharamshala–McLeodganj or Palampur days in the same plan</li></ul><p>Today's rate on WhatsApp within minutes.</p></div></div>
</section>

{reel}

<section class="sza-quote"><div><span class="sza-kicker">Ready for Bir?</span><h2>Get your Bir Billing quote</h2><p>Tell us your dates and what you want to do. We reply with one plan — activities, stay and cab — within minutes.</p></div><div class="sza-btns">{a_wa(MAIN, "Get Quote on WhatsApp", "sza-btn gold")}<a class="sza-btn ghost" href="{QUOTE}">Plan full trip</a></div></section>

<section class="sza-sec" id="packages">
<span class="sza-kicker">Make it a trip</span>
<h2>Bir Billing trips that fit a Himachal holiday</h2>
<p>Three easy ways to do it, with hotel and cab in one quote: <b>a Bir weekend</b> (2 nights: a flight plus bungee or the monasteries); <b>Dharamshala–McLeodganj + Bir</b> (4–5 nights — see our <a href="/dharamshala-tour-package-from-delhi/">Dharamshala tour package from Delhi</a> and <a href="/destination/dharamshala-tour-packages/">Dharamshala tour packages</a>, add <a href="/adventure/paragliding-in-dharamshala/">paragliding in Dharamshala</a>, the <a href="/adventure/triund-trek/">Triund trek</a> or the <a href="/adventure/kareri-lake-trek/">Kareri Lake trek</a>); or <b>a Manali → Bir → Dharamshala circuit</b> with our <a href="/adventure/adventure-activities-in-manali/">Manali adventure activities</a>. Anglers can add a day at Barot — see <a href="/adventure/trout-fishing-in-himachal/">trout fishing in Himachal</a>. Getting there: <a href="/cabs/pathankot-to-dharamshala-taxi/">Pathankot to Dharamshala taxi</a>, <a href="/cabs/dharamshala-taxi-service/">Dharamshala taxi service</a> or any route on <a href="/cabs/">Suzu cabs</a>.</p>
<div class="sza-btns" style="margin-top:18px">{a_wa("a 2-night Bir weekend (paragliding, bungee or monasteries, stay and cab)", "Bir weekend — Get Quote", "sza-btn gold")}{a_wa("a Dharamshala-McLeodganj + Bir Billing trip (4-5 nights, hotel and cab)", "Dharamshala + Bir — Get Quote", "sza-btn line")}</div>
</section>

<section class="sza-sec sza-faq" id="faq">
<span class="sza-kicker">FAQ</span>
<h2>Bir Billing — questions</h2>
{faq_html}
</section>

<section class="sza-sec alt" id="more">
<span class="sza-kicker">More adventures</span>
<h2>Explore more in Himachal</h2>
<div class="sza-cats"><a class="sza-cat" href="/adventure/paragliding-in-bir-billing/"><span class="ic">🪂</span><span class="n">Paragliding in Bir Billing</span><span class="c">Tandem flights from Billing</span></a><a class="sza-cat" href="/adventure/bungee-jumping-in-himachal/"><span class="ic">🪢</span><span class="n">Bungee jumping</span><span class="c">Himachal's verified jump</span></a><a class="sza-cat" href="/adventure/camping-in-himachal/"><span class="ic">⛺</span><span class="n">Camping in Himachal</span><span class="c">Where to camp this month</span></a><a class="sza-cat" href="/adventure/paragliding-in-himachal/"><span class="ic">🌄</span><span class="n">Paragliding in Himachal</span><span class="c">Every flying site</span></a><a class="sza-cat" href="/adventure/triund-trek/"><span class="ic">🥾</span><span class="n">Triund trek</span><span class="c">Above McLeodganj</span></a><a class="sza-cat" href="/adventure/"><span class="ic">🧭</span><span class="n">All adventures</span><span class="c">Air · Water · Snow · Land</span></a></div>
</section>
</div>
'''
out = pathlib.Path(__file__).with_name(f"{SLUG}.html")
out.write_text(html, encoding="utf-8")
print(out)
