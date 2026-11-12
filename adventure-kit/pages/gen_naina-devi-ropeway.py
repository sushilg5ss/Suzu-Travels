#!/usr/bin/env python3
"""naina-devi-ropeway — Page Builder (night) 13 Nov 2026 IST.
Built from the Research Lead brief (12 Nov 2026) + Visual Studio night media @7820ac8 (hero, explainer, reel).
Unverified list respected: no cable length, vertical rise, ride minutes, cabin count or year opened;
no lower-station name; no promise of a lift or extended Navratri ropeway hours; operator never named.
Gondola photos are generic (never captioned as Naina Devi); Naina Devi photos are Wikimedia Commons, credited.
No prices. Quote-form links carry ?activity= (night override).
Run: python3 pages/gen_naina-devi-ropeway.py && python3 build.py pages/naina-devi-ropeway.html > pages/naina-devi-ropeway.min.html
"""
from urllib.parse import quote
import pathlib

SLUG = "naina-devi-ropeway"
U = "https://suzutravels.com/wp-content/uploads/"
CDN = ("https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@7820ac81ff1817c5089417b9555d6b27459114bf"
       f"/adventure-kit/media/{SLUG}/")


def wa(activity, place="Naina Devi"):
    t = (f"Hi Suzu Travels, I want a quote for {activity} in {place}. "
         f"Travel date: ___ , people: ___ (page: {SLUG})")
    return "https://wa.me/917087488961?text=" + quote(t, safe="")


WA = wa("the ropeway with darshan (cab + stay)")
QF = "/himachal-tour-packages-quote/?activity=" + quote("Naina Devi ropeway", safe="")
A = 'target="_blank" rel="noopener"'

cards = [
    ("Naina Devi cable car", "Easiest way up", "2026/10/ropeway-gondolas-over-forest-hills-768x512.webp",
     "Gondola cabins on a cable gliding over forested green hills (illustrative photo)", "50% 50%",
     "Base station → hilltop temple",
     "Ride up from the base of the hill to the temple and look out over Gobind Sagar on the way.",
     wa("the ropeway with darshan"), ""),
    ("Old footpath", "Free, steep", "2026/11/suzu-naina-devi-g-5-768x576.webp",
     "Houses of Naina Devi town on the ridge with the plains in the distance", "50% 50%",
     "About 1.25 km of steps and slope",
     "The traditional walk up from the bazaar. Fine for fit walkers; hard work for elders in the heat.",
     wa("darshan with the walk up"), ""),
    ("By car closer to the temple", "Check on the day", "2026/11/suzu-naina-devi-fig-2-768x1024.webp",
     "Shri Naina Devi Ji temple on its hilltop in Bilaspur district", "50% 35%",
     "Paid parking, limited space",
     "Visitors report that cars can go up close to the back of the temple. Our driver checks what is allowed that day.",
     wa("darshan by car"), ""),
    ("Navratri &amp; mela days", "Go early", "2026/11/suzu-naina-devi-g-3-768x511.webp",
     "White shikhara of the Shri Naina Devi temple with red flags", "50% 40%",
     "Temple open 2 am – midnight",
     "The busiest days of the year: queues at the ropeway and at the gate. Reach before sunrise or pick a weekday.",
     wa("Navratri darshan with the ropeway"), ""),
    ("Anandpur Sahib – Naina Devi line", "Not running", "2026/11/suzu-naina-devi-g-8-768x576.webp",
     "Gobind Sagar reservoir near Naina Devi framed by hills", "50% 50%",
     "Proposed since 2012, not built",
     "A Punjab–Himachal ropeway from Anandpur Sahib has been talked about for years, but you still go by road — about 20 km.",
     wa("a cab from Anandpur Sahib with the ropeway"),
     ""),
    ("Gobind Sagar &amp; Bandla add-on", "Day trip", "2026/11/suzu-naina-devi-g-4-768x432.webp",
     "Gobind Sagar lake seen from the Shri Naina Devi temple area", "50% 50%",
     "Same district, same day",
     "After darshan, add boating on Gobind Sagar or a tandem flight at Bandla near Bilaspur.",
     wa("Naina Devi with Gobind Sagar or Bandla", "Bilaspur"),
     '<a class="x" href="/adventure/gobind-sagar-water-sports/">Gobind Sagar →</a>'),
]

card_html = "".join(
    f'<article class="sza-card"><div class="img"><img src="{U}{img}" alt="{alt}" style="object-position:{pos}" loading="lazy" width="768" height="512"><span class="sza-badge">{badge}</span></div>'
    f'<div class="body"><h3>{name}</h3><div class="meta"><b>{meta}</b></div><p class="meta">{txt}</p>'
    f'<div class="go">{extra}<a class="q" href="{link}" {A}>Get Quote →</a></div></div></article>'
    for name, badge, img, alt, pos, meta, txt, link, extra in cards)

faqs = [
    ("Is there a ropeway to Naina Devi temple?",
     "Yes. A cable car runs from the base of the hill to the hilltop temple in Bilaspur district. The old footpath, about 1.25 km and steep, is the other way up."),
    ("What are the Naina Devi ropeway timings?",
     "Listings show about 8:15 am to 7 pm from April to October and about 8:15 am to 6 pm the rest of the year. It stops in bad weather, so timings can change on the day — we check before you travel."),
    ("What is the Naina Devi ropeway ticket price?",
     f'Fares are set by the operator and change. <a href="{WA}" {A}>Send your date on WhatsApp</a> and we share today\'s fare with your cab and stay quote within minutes.'),
    ("Does the ropeway run during Navratri?",
     "Navratri is the busiest time of the year. The temple opens from 2 am to midnight and queues build at the ropeway and the gate. Go early in the morning or choose a weekday outside the festival."),
    ("Is there a ropeway from Anandpur Sahib to Naina Devi?",
     "No. A Punjab–Himachal ropeway has been proposed since 2012, with MoUs in 2012 and 2018 and failed bids in 2020–21, but it has not been built. You travel by road, about 20 km from Anandpur Sahib."),
    ("How far is Naina Devi from Chandigarh and Anandpur Sahib?",
     "About 108 km by road from Chandigarh and about 20 km from Anandpur Sahib railway station. From Bilaspur town it is roughly 60–85 km depending on the route."),
    ("Can elders visit Naina Devi without climbing?",
     f'Yes. Take the cable car up; ramps help at the temple. Avoid Navratri peak hours. For darshan timings and the temple story see our <a href="/pilgrimage-tours/naina-devi/">Naina Devi temple guide</a>.'),
    ("Can I book the Naina Devi ropeway online?",
     "Tickets are bought at the counter. We plan your timing and cab so you reach the base station before the queues build."),
]
faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)

reel = pathlib.Path(__file__).resolve().parents[1].joinpath("media", SLUG, "reel-section.html").read_text(encoding="utf-8").strip()

credits = ('Photos: Naina Devi town on the ridge — <a href="https://commons.wikimedia.org/wiki/File:Naina_devi_Himachal_Pradesh.jpg" target="_blank" rel="noopener">Sahilxr</a>, '
           '<a href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank" rel="noopener license">CC BY-SA 4.0</a> · '
           'Hilltop temple — <a href="https://commons.wikimedia.org/wiki/File:Shri_Naina_Devi_Ji_Temple_situated_on_a_hilltop_in_the_Bilaspur_Distt.,Jan2013.jpg" target="_blank" rel="noopener">Invictus27</a>, '
           '<a href="https://creativecommons.org/licenses/by-sa/3.0/" target="_blank" rel="noopener license">CC BY-SA 3.0</a> · '
           'Temple shikhara — <a href="https://commons.wikimedia.org/wiki/File:Naina_Devi,_Himachal_Pardesh_(17).jpg" target="_blank" rel="noopener">Gurlal Maan</a>, '
           '<a href="https://creativecommons.org/licenses/by-sa/3.0/" target="_blank" rel="noopener license">CC BY-SA 3.0</a> · '
           'Gobind Sagar from the temple area — <a href="https://commons.wikimedia.org/wiki/File:Gobind_Sagar.jpg" target="_blank" rel="noopener">Harmalhotra</a>, '
           '<a href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank" rel="noopener license">CC BY-SA 4.0</a> · '
           'Gobind Sagar reservoir — <a href="https://commons.wikimedia.org/wiki/File:Gobind_Sagar_Lake_Ambuj.jpg" target="_blank" rel="noopener">Ambuj Mishra</a>, '
           '<a href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank" rel="noopener license">CC BY-SA 4.0</a> · '
           'Videos also use Naina Devi town by <a href="https://commons.wikimedia.org/wiki/File:Naina_Devi_town,_Bilaspur_district_2015-09-25_Devyansh4.jpg" target="_blank" rel="noopener">Devyansh.sharma09</a>, '
           '<a href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank" rel="noopener license">CC BY-SA 4.0</a> (all Wikimedia Commons). '
           'Gondola photos are illustrative stock images, not the Naina Devi ropeway.')

P = "sza-ndr"
html = f'''<!-- {SLUG} — built by Page Builder (night) 13 Nov 2026 from the Research Lead brief + Visual Studio night media @7820ac8. Kit v2.0. -->
<style>@media(max-width:900px){{.{P} .sza-hero video{{object-position:30% 50%}}.{P} .sza-hero:after{{background:linear-gradient(180deg,rgba(11,31,51,.5) 0%,rgba(11,31,51,.7) 45%,rgba(11,31,51,.95) 100%)}}}}.{P} .sza-hero-in>*{{max-width:640px}}@media(min-width:901px){{.{P} .sza-hero-in>*{{max-width:min(560px,44vw)}}}}.{P} .sza-chips{{max-width:720px}}.{P} #spots .sza-grid{{grid-template-columns:repeat(auto-fit,minmax(220px,1fr))}}@media(min-width:1000px){{.{P} #experience .sza-steps,.{P} #spots .sza-grid{{grid-template-columns:repeat(3,1fr)}}}}.{P} #spots .sza-card .img img{{aspect-ratio:3/2;object-fit:cover;width:100%;height:auto}}.{P} .sza-media ul{{padding-left:20px;list-style:disc;margin:0}}.{P} .sza-media ul li{{margin:0 0 8px}}.{P} .sza-checks{{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}.{P} .go .x{{margin-right:14px}}.{P} .sza-credit{{font-size:12px;color:#5b6b7a;margin:14px 0 0;line-height:1.6}}.{P} .sza-credit a{{color:inherit}}</style>
<div class="sza {P}">
<section class="sza-hero">
<video autoplay muted loop playsinline preload="metadata" poster="{U}2026/11/{SLUG}-hero-poster.webp" aria-label="Naina Devi town on its ridge, a gondola cabin on a cable, Gobind Sagar below and the white temple shikhara with red flags, with a gold cable line rising to the hilltop temple"><source src="{CDN}hero.webm" type="video/webm"><source src="{CDN}hero.mp4" type="video/mp4"></video>
<div class="sza-hero-in">
<span class="sza-kicker">Pilgrim ropeway · Bilaspur, Himachal (our home district)</span>
<p class="sza-hero-tag">Ride up to Maa Naina Devi, skip the steep climb</p>
<p class="sza-hero-sub">The cable car from the base to the hilltop temple above Gobind Sagar — hours, crowds, the walking path and a cab plan from Chandigarh or Anandpur Sahib.</p>
<ul class="sza-chips"><li><b>Route</b> Base → hilltop temple</li><li><b>Hilltop</b> ~1,200 m</li><li><b>Chandigarh</b> ~108 km</li><li><b>Anandpur Sahib</b> ~20 km</li><li><b>Navratri</b> Longest queues</li><li><b>Price</b> Get Quote</li></ul>
<div class="sza-btns"><a class="sza-btn gold" href="{WA}" {A}>Get Quote on WhatsApp</a><a class="sza-btn ghost" href="{QF}">Add to my Himachal trip</a></div>
<div class="sza-trust"><span><a href="https://suzutravels.com/certificates/">HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022</a></span><span>Ropeway + cab + stay in one quote</span><span>Reply within minutes</span></div>
</div>
</section>
<nav class="sza-nav" aria-label="On this page"><div class="sza-nav-in"><a href="#overview">Overview</a><a href="#spots">Ways up</a><a href="#experience">Your day</a><a href="#season">Season</a><a href="#safety">Safety</a><a href="#booking">How booking works</a><a href="#packages">Trips</a><a href="#faq">FAQ</a><a class="cta" href="{WA}" {A}>Get Quote</a></div></nav>

<section class="sza-sec" id="overview">
<span class="sza-kicker">Quick answer</span>
<h2>Naina Devi ropeway at a glance</h2>
<p class="sza-answer">Yes — a cable car runs from the base of the hill up to the hilltop temple of Shri Naina Devi Ji, so elders and children can skip the steep 1.25 km footpath. It runs through the day all year, with longer hours in summer, and stops in strong wind or storms. Navratri brings the longest queues. Tell us your date and we time the ride into your cab plan.</p>
<div class="sza-facts"><div class="sza-fact"><div class="k">Where</div><div class="v">Shri Naina Devi Ji, Bilaspur district, on a Shivalik hilltop above Gobind Sagar (~1,200 m)</div></div><div class="sza-fact"><div class="k">Route</div><div class="v">Base station on the Nangal road side → upper station near the temple</div></div><div class="sza-fact"><div class="k">Ropeway hours</div><div class="v">About 8:15 am – 7 pm (Apr – Oct), about 8:15 am – 6 pm (Nov – Mar); weather permitting — we confirm on your date</div></div><div class="sza-fact"><div class="k">Temple darshan</div><div class="v">4 am – 10 pm; 2 am – midnight in Navratri (temple trust)</div></div><div class="sza-fact"><div class="k">Walking option</div><div class="v">Old footpath ~1.25 km, steep; the bus stand is ~2 km below the shrine</div></div><div class="sza-fact"><div class="k">Price</div><div class="v">Get Quote</div></div></div>
</section>

<section class="sza-sec alt" id="spots">
<span class="sza-kicker">Ways up &amp; add-ons</span>
<h2>How to reach the Naina Devi temple on the hilltop</h2>
<p class="sza-lead">The cable car is the easy way; the footpath is the old way. Tell us who is travelling and we plan the right one for your group and date.</p>
<div class="sza-grid">{card_html}</div>
<p class="sza-credit">{credits}</p>
</section>

<section class="sza-sec" id="experience">
<span class="sza-kicker">Your day</span>
<h2>How a ropeway darshan day works</h2>
<ol class="sza-steps"><li><h3>Share your plan</h3><p>Date, group size and pick-up city on WhatsApp.</p></li><li><h3>We check the week</h3><p>That the ropeway is running — weather, festival crowds, maintenance.</p></li><li><h3>Early drop</h3><p>Cab from Chandigarh, Anandpur Sahib, Kiratpur, Bilaspur or Ghumarwin to the lower station, early.</p></li><li><h3>Ride up</h3><p>Ticket at the counter, ride up, darshan at the temple.</p></li><li><h3>Ride or walk down</h3><p>Come down by cable car or the footpath; your driver waits at the base.</p></li><li><h3>Carry on</h3><p>Anandpur Sahib, Gobind Sagar, Bandla or the Shakti Peeth circuit to Chintpurni.</p></li></ol>
<div class="sza-media"><video autoplay muted loop playsinline preload="none" poster="{U}2026/11/{SLUG}-explainer-poster.webp" width="1600" height="900" aria-label="Schematic, not to scale: bus stand about 2 km below, the lower station, the cable car, the upper station and the temple at about 1,200 m, with the 1.25 km footpath dotted; then road distances: Chandigarh about 108 km, Anandpur Sahib 20 km, Bilaspur 60 to 85 km, Ghumarwin 64 km; price: Get Quote"><source src="{CDN}explainer.webm" type="video/webm"><source src="{CDN}explainer.mp4" type="video/mp4"></video><div><h3>Base to temple, and how far you drive</h3><ul><li><b>Bus stand</b> → about 2 km below the shrine.</li><li><b>Cable car</b> → lower station to the upper station by the temple.</li><li><b>Footpath</b> → about 1.25 km, steep.</li><li><b>By road</b> → Chandigarh ~108 km · Anandpur Sahib ~20 km · Bilaspur 60–85 km · Ghumarwin 64 km.</li></ul><p style="margin-top:8px;font-size:14px">Schematic, not to scale. Ropeway runs subject to weather — we confirm on your date.</p></div></div>
</section>

<section class="sza-sec alt" id="season">
<span class="sza-kicker">When to go</span>
<h2>Best time to ride the Naina Devi ropeway</h2>
<div class="sza-scroll"><table class="sza-tbl"><thead><tr><th>Months</th><th>What to expect</th><th>Our tip</th></tr></thead><tbody><tr><td>Apr – Jun</td><td>Longest ropeway hours, hot afternoons, busy weekends</td><td>Ride before 10 am</td></tr><tr><td>Jul – Aug</td><td>Monsoon showers; Shravan Ashtami mela crowds</td><td>Rain or wind can stop the ropeway — keep the day flexible</td></tr><tr><td>Sep – Oct</td><td>Pleasant weather; Sharad Navratri is very crowded</td><td>Weekday or pre-dawn darshan</td></tr><tr><td>Nov – Feb</td><td>Shorter hours (till about 6 pm), cool clear days, lighter crowds</td><td>Best for elders</td></tr><tr><td>Mar – early Apr</td><td>Chaitra Navratri (2027 from 7 Apr) — heavy crowds</td><td>Book cab and stay early</td></tr></tbody></table></div>
</section>

<div class="sza-band" id="safety"><div class="sza-band-in">
<span class="sza-kicker">Safety &amp; crowd tips</span>
<h2>What we check before your ride</h2>
<p class="sza-lead">Suzu Travels is an HP Tourism registered travel agent (Reg. No. DTO-MND-11-243/2022), based in Bilaspur district. We plan the ropeway into your trip around these checks:</p>
<ul class="sza-checks"><li><b>Weather stops</b>Ropeways in Himachal stop in high wind, storms or landslide alerts — ride early and follow staff and district advisories</li><li><b>Festival crowds</b>In Navratri keep children and elders close and carry small bags only; the district runs a command centre for crowd and traffic</li><li><b>Elders and wheelchairs</b>Ramps are in place at the temple; tell us mobility needs and we plan the timing around them</li><li><b>In the cabin</b>Stay seated, don't rock the cabin, follow the attendant's instructions</li><li><b>Temple rules</b>Follow dress and photo rules — no photos inside the sanctum; carry water</li><li><b>Plan B</b>If the ropeway is stopped, we suggest the footpath or the road up and re-plan the day</li></ul>
</div></div>

<section class="sza-sec" id="booking">
<span class="sza-kicker">How booking works</span>
<h2>Get a quote in minutes</h2>
<ol class="sza-steps"><li><h3>Tell us</h3><p>WhatsApp or the quote form — dates, people and pick-up city.</p></li><li><h3>We check your date</h3><p>Ropeway status, festival crowds and today's fare.</p></li><li><h3>You get one quote</h3><p>Cab, stay and ropeway plan together, with any add-ons.</p></li><li><h3>Confirm and go</h3><p>We send the plan and stay in touch on WhatsApp.</p></li></ol>
<p class="sza-lead">Your quote depends on the date (Navratri, Shravan mela, weekend or weekday), the number of riders (adults, children, elders) and one-way or return ride, your pick-up city and cab type (Chandigarh, Anandpur Sahib station, Delhi or Shimla), a night stay (temple-trust rooms, HP rest house, guest houses or Anandpur Sahib hotels) and add-ons such as Bandla paragliding, Gobind Sagar or Kol Dam water sports or the Shakti Peeth circuit. We send today's fare on WhatsApp within minutes.</p>
</section>

{reel}

<section class="sza-quote"><div><span class="sza-kicker">Naina Devi ropeway</span><h2>Get your Naina Devi quote</h2><p>Tell us your date, group size and pick-up city. We reply with a cab + stay plan that times the ropeway before the queues.</p></div><div class="sza-btns"><a class="sza-btn gold" href="{WA}" {A}>Get Quote on WhatsApp</a><a class="sza-btn ghost" href="{QF}">Plan full trip</a></div></section>

<section class="sza-sec" id="packages">
<span class="sza-kicker">Make it a trip</span>
<h2>Pair the ropeway with darshan and our home district</h2>
<p><b>Day trip from Chandigarh:</b> early cab, ropeway, darshan and back by evening. Flying in? Start with a <a href="/cabs/chandigarh-airport-taxi/">Chandigarh airport taxi</a>. For darshan timings, the legend and the temple story, read our <a href="/pilgrimage-tours/naina-devi/">Naina Devi temple timings</a> guide.</p>
<p><b>Shakti Peeth yatra:</b> Naina Devi with <a href="/pilgrimage-tours/chintpurni/">Chintpurni</a>, <a href="/pilgrimage-tours/jwala-ji/">Jwala Ji</a> and <a href="/pilgrimage-tours/baba-balak-nath/">Baba Balak Nath</a> — see all <a href="/pilgrimage-tours/">pilgrimage tours</a>.</p>
<p><b>Bilaspur 2-day:</b> add <a href="/adventure/gobind-sagar-water-sports/">Gobind Sagar water sports</a>, <a href="/adventure/kol-dam-water-sports/">Kol Dam lake rides</a> or <a href="/adventure/paragliding-in-bilaspur/">paragliding at Bandla</a>. Other cable cars in the state are on our <a href="/adventure/ropeways-in-himachal/">ropeways in Himachal</a> page. Check <a href="/bilaspur-weather/">Bilaspur weather</a> before you go, or <a href="{QF}">ask for a custom plan</a>.</p>
</section>

<section class="sza-sec sza-faq" id="faq">
<span class="sza-kicker">FAQ</span>
<h2>Naina Devi ropeway — questions</h2>
{faq_html}
</section>

<section class="sza-sec alt" id="more">
<span class="sza-kicker">More adventures</span>
<h2>Explore more in Himachal</h2>
<div class="sza-cats"><a class="sza-cat" href="/adventure/ropeways-in-himachal/"><span class="ic">🚡</span><span class="n">Ropeways in Himachal</span><span class="c">All cable cars</span></a><a class="sza-cat" href="/adventure/gobind-sagar-water-sports/"><span class="ic">🚤</span><span class="n">Gobind Sagar water sports</span><span class="c">Bilaspur</span></a><a class="sza-cat" href="/adventure/paragliding-in-bilaspur/"><span class="ic">🪂</span><span class="n">Paragliding in Bilaspur</span><span class="c">Bandla</span></a><a class="sza-cat" href="/adventure/kol-dam-water-sports/"><span class="ic">🌊</span><span class="n">Kol Dam water sports</span><span class="c">Mandi–Bilaspur</span></a><a class="sza-cat" href="/adventure/kamrunag-trek/"><span class="ic">🛕</span><span class="n">Kamrunag trek</span><span class="c">Mandi</span></a><a class="sza-cat" href="/adventure/"><span class="ic">🧭</span><span class="n">All adventures</span><span class="c">Air · Water · Snow · Land</span></a></div>
</section>
</div>'''

pathlib.Path(__file__).with_name(f"{SLUG}.html").write_text(html, encoding="utf-8")
print("ok", len(html))
