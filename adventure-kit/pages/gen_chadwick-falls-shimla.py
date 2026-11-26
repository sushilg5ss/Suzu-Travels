#!/usr/bin/env python3
# Generates adventure-kit/pages/chadwick-falls-shimla.html (Page Builder night, 27 Nov 2026 IST)
import urllib.parse, pathlib
SLUG = "chadwick-falls-shimla"
HERE = pathlib.Path(__file__).resolve().parent
CDN = "https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@e4cb72de1b834fc88c8a4b196a519aba17f3a8e5/adventure-kit/media/chadwick-falls-shimla/"
U11 = "https://suzutravels.com/wp-content/uploads/2026/11/"
U10 = "https://suzutravels.com/wp-content/uploads/2026/10/"
QUOTE = "/himachal-tour-packages-quote/?activity=" + urllib.parse.quote("Chadwick Falls walk")
WHAT = "a Shimla trip with a Chadwick Falls half-day, cab and stay"

def wa(what=WHAT, tag=SLUG):
    t = f"Hi Suzu Travels, I want a quote for {what}. Travel date: ___ , people: ___ (page: {tag})"
    return "https://wa.me/917087488961?text=" + urllib.parse.quote(t, safe="")

def walink(label, what=WHAT, cls="sza-btn gold"):
    return f'<a class="{cls}" href="{wa(what)}" target="_blank" rel="noopener">{label}</a>'

MAIN = wa()

def card(src, w, h, alt, badge, title, meta, text, what, page=None, plabel="Explore →"):
    explore = f'<a class="x" href="{page}">{plabel}</a>' if page else ""
    return (f'<article class="sza-card"><div class="img"><img src="{src}" alt="{alt}" loading="lazy" width="{w}" height="{h}"><span class="sza-badge">{badge}</span></div>'
            f'<div class="body"><h3>{title}</h3><div class="meta">{meta}</div><p class="meta">{text}</p>'
            f'<div class="go"><a class="q" href="{wa(what)}" target="_blank" rel="noopener">Get Quote →</a>{explore}</div></div></article>')

def noimg_card(icon, badge, title, meta, text, what, page=None, plabel="Explore →"):
    explore = f'<a class="x" href="{page}">{plabel}</a>' if page else ""
    return (f'<article class="sza-card"><div class="img sza-noimg"><span class="ic" aria-hidden="true">{icon}</span><span class="sza-badge">{badge}</span></div>'
            f'<div class="body"><h3>{title}</h3><div class="meta">{meta}</div><p class="meta">{text}</p>'
            f'<div class="go"><a class="q" href="{wa(what)}" target="_blank" rel="noopener">Get Quote →</a>{explore}</div></div></article>')

cards = "".join([
    card(f"{U11}waterfall-rock-ledge-forest-pool-768x576.webp", 768, 576,
         "Waterfall dropping over a rock ledge into a forest pool (representative photo)",
         "Easiest", "Chadwick Falls from the road-head", "<b>About 10 min on foot · forest path</b>",
         "Vehicles get close to the entry point below Summer Hill. From there a short walk through thick forest leads down to the falls.",
         "a Chadwick Falls half-day from my Shimla hotel with cab"),
    card(f"{U11}forest-trail-pine-slope-hills-768x512.webp", 768, 512,
         "Footpath through a pine forest on a hill slope (representative photo)",
         "Walkers", "Summer Hill to the falls on foot", "<b>Longer walk · village side</b>",
         "Walk from Summer Hill through the Hyun (Huen) village side instead of driving to the road-head. Longer, quieter and greener.",
         "a Summer Hill walk to Chadwick Falls with cab"),
    card(f"{U10}shimla-hills-hillside-town-sunrise-768x432.webp", 768, 432,
         "Shimla hillside houses at sunrise",
         "Combine it", "Potter Hill loop (4.7 km)", "<b>Official HP trekking route · easy</b>",
         "The listed Potter Hill loop starts at the Summer Hill police post and passes above Chadwick Falls. Add it for a fuller morning.",
         "a Summer Hill morning with Chadwick Falls and the Potter Hill loop", page="/adventure/treks-near-shimla/", plabel="Treks near Shimla →"),
    noimg_card("🌲", "Picnic", "The Glen forest", "<b>Old deodar forest · quiet walk</b>",
               "A shaded forest below the Ridge side of Shimla, popular for an easy picnic walk. Pair it with town sightseeing.",
               "a Shimla sightseeing day with Chadwick Falls and the Glen", page="/shimla-tourist-places/", plabel="Shimla places →"),
    card(f"{U11}suzu-shimla-snowfall-g-4-768x576.webp", 768, 576,
         "Snow-covered deodar trees above Christ Church, Shimla",
         "Winter", "Shimla winter plan", "<b>Dec–Feb · falls run thin</b>",
         "In winter the falls carry little water. Keep the forest walk short and spend the day on Kufri snow or the Shimla ice rink.",
         "a Shimla winter trip with Kufri snow and ice skating", page="/adventure/ice-skating-shimla/", plabel="Ice skating →"),
])

steps_exp = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Send your Shimla dates", "On WhatsApp or the quote form, with your group size and hotel area."),
    ("We plan the half-day", "Cab from your hotel towards Summer Hill and the road-head, timed so you are back before dusk."),
    ("Walk to the falls", "About 10 minutes through the forest from the entry point. Add the Potter Hill loop for a longer walk."),
    ("Rest by the water", "Photos from safe ground, a snack, and stay off the wet rocks at the pool."),
    ("Walk back up", "Back to the cab, then via Summer Hill and Boileauganj to town."),
    ("Rest of the day", "The Mall, the Ridge or Jakhu, or onward to Kufri."),
])

booking = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Tell us", "WhatsApp or the quote form: date, group size and where you stay in Shimla."),
    ("We check your day", "Weather and road status, season crowds and the right start time."),
    ("You get one quote", "Cab, stay and the rest of your Shimla days: one plan, one rate."),
    ("Confirm and go", "We send the pickup time and what to carry."),
])

season = [
    ("Jul – Sep (monsoon)", "Full flow", "Wet, slippery path, leeches possible, landslip delays on roads. Go in the morning with good shoes; skip it in heavy rain."),
    ("Oct – Nov", "Still flowing, clear skies", "Dry path and clear views. The best balance overall."),
    ("Dec – Feb", "Thin, low water", "Cold and frosty; snow after a Shimla snowfall. Go only for the forest walk."),
    ("Mar – Jun", "Low before the rains", "Dry and warm, busy Shimla summer. A pleasant forest walk; pair it with Potter Hill."),
]
season_html = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in season)

faqs = [
    ("How far is Chadwick Falls from Shimla?", "Roughly 5–7 km from central Shimla, below Summer Hill. Sources give about 5 km from Shimla railway station and about 7 km from the city centre."),
    ("How long is the walk to Chadwick Falls?", "Vehicles get close to the entry point, and the walk from there is short: about 10 minutes through thick forest. Walking all the way from Summer Hill takes longer."),
    ("When does Chadwick Falls have water?", "Best after the monsoon, July to October. It carries little water in the dry summer and in winter."),
    ("How high is Chadwick Falls?", "It is often quoted as about 86 m high. The 1,586 m figure many sites give is the altitude above sea level, not the height of the fall."),
    ("Is Chadwick Falls safe?", "It is an easy route on the HP trekking portal, but rocks near the water are slippery and leopards are reported in the area after dark. Go in daylight, ideally in a group, and stay off wet rocks."),
    ("Is there an entry fee or fixed timing?", "We found no official fee or timing notice. Go in daylight and check locally on the day."),
    ("Can I combine it with Potter Hill?", "Yes. The official 4.7 km Potter Hill loop starts at the Summer Hill police post and passes above Chadwick Falls. See <a href=\"/adventure/treks-near-shimla/\">treks near Shimla</a>."),
    ("Is it worth visiting in December?", "Only as a forest walk, because the falls run thin in winter. In December most visitors pair Shimla with <a href=\"/adventure/kufri-adventure-activities/\">Kufri</a> or <a href=\"/adventure/snow-and-skiing-in-narkanda/\">Narkanda snow</a> and the <a href=\"/adventure/ice-skating-shimla/\">Shimla ice rink</a>."),
]
faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)

more = [
    ("/adventure/treks-near-shimla/", "🥾", "Treks near Shimla", "Day hikes around Shimla"),
    ("/adventure/shali-tibba-trek/", "🏔️", "Shali Tibba trek", "Shimla's highest viewpoint"),
    ("/adventure/karol-tibba-trek/", "⛰️", "Karol Tibba trek", "Solan's highest hill"),
    ("/adventure/jakhu-ropeway-shimla/", "🚡", "Jakhu ropeway", "Ride up to Jakhu"),
    ("/adventure/kufri-adventure-activities/", "❄️", "Kufri adventure", "Snow and parks near Shimla"),
    ("/adventure/adventure-activities-in-shimla/", "🧗", "Adventure in Shimla", "Everything around Shimla"),
]
more_html = "".join(f'<a class="sza-cat" href="{h}"><span class="ic">{i}</span><span class="n">{n}</span><span class="c">{c}</span></a>' for h, i, n, c in more)

reel = (HERE.parent / "media" / SLUG / "reel-section.html").read_text(encoding="utf-8").strip()

page = f'''<!-- chadwick-falls-shimla — built by Page Builder (night) 27 Nov 2026 IST from the Research Lead brief 26 Nov (Project doc claude/adventure-research/briefs/chadwick-falls-shimla.md) + Visual Studio media @e4cb72d. Kit v2.0. No prices, no operator names. Not stated as fact (unverified): fall height (only "often quoted as about 86 m"), entry fee/timings, winter freezing, exact Summer Hill route distance. Photos: representative library photos with neutral alt text (none shows Chadwick Falls). -->
<style>.sza-cfs .sza-hero-in>*{{max-width:620px}}@media(min-width:901px){{.sza-cfs .sza-hero-in>*{{max-width:min(560px,44vw)}}}}.sza-cfs .sza-chips{{max-width:700px}}.sza-cfs .sza-media ul{{padding-left:20px;list-style:disc;margin:0}}.sza-cfs .sza-media ul li{{margin:0 0 8px}}.sza-cfs .sza-media img{{height:auto;aspect-ratio:4/3;object-fit:cover}}.sza-cfs .sza-media video{{height:auto;aspect-ratio:16/9}}.sza-cfs #spots .sza-grid{{grid-template-columns:repeat(auto-fit,minmax(min(340px,100%),1fr))}}.sza-cfs .sza-noimg{{display:flex;align-items:center;justify-content:center;aspect-ratio:16/9;background:linear-gradient(135deg,#0b1f33,#1d3b5a)}}.sza-cfs .sza-noimg .ic{{font-size:64px}}.sza-cfs .sza-checks{{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}.sza-cfs .sza-choose{{margin-top:32px}}.sza-cfs .sza-rep{{font-size:13px;opacity:.75;margin-top:10px}}@media(min-width:1000px){{.sza-cfs #experience .sza-steps{{grid-template-columns:repeat(3,1fr)}}}}@media(max-width:820px){{.sza-cfs .sza-hero video{{object-position:30% 50%}}.sza-cfs .sza-hero:after{{background:linear-gradient(180deg,rgba(11,31,51,.45) 0%,rgba(11,31,51,.68) 45%,rgba(11,31,51,.95) 100%)}}}}</style>
<div class="sza sza-cfs">
<section class="sza-hero">
<video autoplay muted loop playsinline preload="metadata" poster="{U11}chadwick-falls-shimla-hero-poster.webp" aria-label="Representative photos of a forest waterfall, a pine trail, a hill road and Shimla hills at sunrise, with a gold path from the road-head to the falls and a counter to about 10 minutes on foot"><source src="{CDN}hero.webm" type="video/webm"><source src="{CDN}hero.mp4" type="video/mp4"></video>
<div class="sza-hero-in">
<span class="sza-kicker">Shimla · Summer Hill · short forest walk</span>
<p class="sza-hero-tag">A forest walk to the waterfall below Summer Hill, best after the rains</p>
<p class="sza-hero-sub">Drive towards Summer Hill, walk a short forest trail down to the falls, and be back before dusk. Suzu plans the cab, the timing and your Shimla stay.</p>
<ul class="sza-chips"><li><b>Easy</b> level</li><li><b>~1,586 m</b> altitude</li><li><b>~10 min</b> walk from the road-head</li><li><b>Jul–Oct</b> most water</li><li><b>Half-day</b> trip</li><li><b>Price</b> Get Quote</li></ul>
<div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan my trip</a></div>
<div class="sza-trust"><span><a href="https://suzutravels.com/certificates/">HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022</a></span><span>Himachal-based since 2019</span><span>Reply within minutes</span></div>
</div>
</section>
<nav class="sza-nav" aria-label="On this page"><div class="sza-nav-in"><a href="#overview">Overview</a><a href="#spots">Walks &amp; nearby</a><a href="#experience">How the day works</a><a href="#season">By month</a><a href="#safety">Safety</a><a href="#booking">How booking works</a><a href="#packages">Make it a trip</a><a href="#faq">FAQ</a><a class="cta" href="{MAIN}" target="_blank" rel="noopener">Get Quote</a></div></nav>

<section class="sza-sec" id="overview">
<span class="sza-kicker">Quick answer</span>
<h2>Chadwick Falls, Shimla, at a glance</h2>
<p class="sza-answer">Chadwick Falls is a forest waterfall below Summer Hill, about 5–7 km from central Shimla, at roughly 1,586 m. Vehicles get close to the entry point, and a short walk of about 10 minutes leads through thick forest to the falls. It is an easy route listed on the HP trekking portal. Go July to October for real water, and walk out well before sunset.</p>
<div class="sza-facts"><div class="sza-fact"><div class="k">Where</div><div class="v">Below Summer Hill, Shimla (HP University side)</div></div><div class="sza-fact"><div class="k">Altitude</div><div class="v">About 1,586 m; the fall is often quoted as about 86 m high</div></div><div class="sza-fact"><div class="k">Level</div><div class="v">Easy; a half-day trip</div></div><div class="sza-fact"><div class="k">Walk</div><div class="v">About 10 min from the road-head; longer from Summer Hill village</div></div><div class="sza-fact"><div class="k">Best time</div><div class="v">July–October; little water in dry summer and winter</div></div><div class="sza-fact"><div class="k">Price</div><div class="v">Get Quote</div></div></div>
<div class="sza-media" style="margin-top:28px"><img src="{U11}waterfall-rock-ledge-forest-pool-768x576.webp" alt="Waterfall dropping over a rock ledge into a forest pool (representative photo)" loading="lazy" width="768" height="576"><div><h3>Is Chadwick Falls for you?</h3><ul><li><b>Shimla visitors with half a day</b> → yes: short drive, short walk, real forest.</li><li><b>Families</b> → fine with steady footing; keep children off the wet rocks.</li><li><b>Visiting Dec–Jun</b> → expect a thin fall; go for the forest walk.</li><li><b>Want a real trek</b> → try the <a href="/adventure/shali-tibba-trek/">Shali Tibba trek</a> or <a href="/adventure/karol-tibba-trek/">Karol Tibba</a>.</li></ul><p>More in Shimla: <a href="/shimla-tourist-places/">Shimla tourist places</a> and <a href="/things-to-do-in-shimla/">things to do in Shimla</a>.</p><p class="sza-rep">Photos on this page are representative, not of Chadwick Falls itself.</p></div></div>
</section>

<section class="sza-sec alt" id="spots">
<span class="sza-kicker">Walks &amp; nearby</span>
<h2>Ways to see Chadwick Falls, and what to pair it with</h2>
<p class="sza-lead">The short road-head walk, the longer Summer Hill approach, the Potter Hill loop, and a winter plan for when the falls run thin.</p>
<div class="sza-grid">{cards}</div>
<div class="sza-media sza-choose" id="route"><video autoplay muted loop playsinline preload="none" poster="{U11}chadwick-falls-shimla-explainer-poster.webp" width="1600" height="900" aria-label="Schematic map: Mall and Ridge to Summer Hill by cab, about 5 to 7 km; road-head; about 10 minutes on foot to Chadwick Falls; an optional dotted Potter Hill loop of 4.7 km; a 12-month strip with most water from July to October"><source src="{CDN}explainer.webm" type="video/webm"><source src="{CDN}explainer.mp4" type="video/mp4"></video><div><h3>Mall / Ridge → Summer Hill → Chadwick Falls</h3><ul><li><b>Shimla town</b> → about 5–7 km by cab towards Summer Hill.</li><li><b>Road-head</b> → vehicles get close to the entry point.</li><li><b>Forest walk</b> → about 10 minutes down to the falls.</li><li><b>Optional</b> → the 4.7 km Potter Hill loop from the Summer Hill police post.</li><li><b>Back before dusk</b> → no night visits.</li></ul><p>Schematic, not to scale.</p></div></div>
</section>

<section class="sza-sec" id="experience">
<span class="sza-kicker">How the day works</span>
<h2>A Chadwick Falls half-day, step by step</h2>
<ol class="sza-steps">{steps_exp}</ol>
<div class="sza-media"><img src="{U11}hill-road-through-pine-forest-car-768x512.webp" alt="Car on a hill road through a pine forest (representative photo)" loading="lazy" width="768" height="512"><div><h3>What to carry</h3><ul><li>Shoes with good grip</li><li>Water and a light snack (there are no eateries near the falls)</li><li>A rain jacket in Jul–Sep, a warm layer in winter</li><li>A small bag to take your waste back</li></ul><p>Polythene is banned in Himachal: leave nothing behind.</p></div></div>
</section>

<section class="sza-sec alt" id="season">
<span class="sza-kicker">When to go</span>
<h2>Chadwick Falls by month</h2>
<div class="sza-scroll"><table class="sza-tbl"><thead><tr><th>Months</th><th>Water</th><th>Trail and verdict</th></tr></thead><tbody>{season_html}</tbody></table></div>
<div class="sza-media" style="margin-top:28px"><img src="{U11}tall-waterfall-green-gorge-691x1024.webp" alt="Tall waterfall in a green gorge after rain (representative photo)" loading="lazy" width="691" height="1024"><div><h3>Why July to October?</h3><p>The falls are fed by the rains. After the monsoon the flow is at its best, and by October the path dries out and the skies clear. In winter, pair Shimla with <a href="/adventure/kufri-adventure-activities/">Kufri</a>, <a href="/adventure/snow-and-skiing-in-narkanda/">Narkanda snow</a> or the <a href="/adventure/ice-skating-shimla/">Shimla ice rink</a>; see also <a href="/new-year-in-shimla/">New Year in Shimla</a>.</p></div></div>
</section>

<div class="sza-band" id="safety"><div class="sza-band-in">
<span class="sza-kicker">Safety</span>
<h2>What we check before your Chadwick Falls walk</h2>
<p class="sza-lead">Suzu Travels is an <a href="https://suzutravels.com/certificates/" style="color:#f3d98f;text-decoration:underline">HP Tourism registered travel agent (Reg. No. DTO-MND-11-243/2022)</a>. We plan your Shimla day around these checks:</p>
<ul class="sza-checks"><li><b>Daylight only</b>Walk out well before sunset. Leopards are reported in the area after dark; no night visits.</li><li><b>Wet rocks</b>Stay off slippery rocks at the pool and take no selfies at the water's edge.</li><li><b>Monsoon</b>Check road and landslide status on the day and skip it during heavy-rain alerts.</li><li><b>Wildlife and waste</b>Don't feed or approach animals, leave no food out, and carry your waste back.</li><li><b>Help nearby</b>Police at Boileauganj; health centres at Boileauganj and Summer Hill; IGMC Shimla for anything serious.</li><li><b>Kids and elders</b>The short walk is fine with steady footing. Carry water: there are no eateries at the falls.</li></ul>
</div></div>

<section class="sza-sec" id="booking">
<span class="sza-kicker">How booking works</span>
<h2>Get a quote in minutes</h2>
<ol class="sza-steps">{booking}</ol>
<div class="sza-media"><img src="{U11}forest-trail-pine-slope-hills-768x512.webp" alt="Footpath through a pine forest on a hill slope (representative photo)" loading="lazy" width="768" height="512"><div><h3>What your quote depends on</h3><ul><li>Cab type and pick-up point (Mall and Ridge hotels need a short walk to the vehicle point)</li><li>A half-day, or a full Summer Hill + Potter Hill + Shimla sightseeing day</li><li>A local guide on request</li><li>Season (summer and December rush) and group size</li><li>Hotel nights and Kufri or Narkanda add-ons</li></ul><p>We send today's rate on WhatsApp within minutes.</p></div></div>
</section>

{reel}

<section class="sza-quote"><div><span class="sza-kicker">Ready for Shimla?</span><h2>Get your Shimla quote</h2><p>Tell us your date and group size. We reply with one plan (cab, stay and your Chadwick Falls half-day) within minutes.</p></div><div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan full trip</a></div></section>

<section class="sza-sec" id="packages">
<span class="sza-kicker">Make it a trip</span>
<h2>Add Chadwick Falls to a Shimla trip</h2>
<p>A good plan is two or three nights in Shimla: a Summer Hill half-day with Chadwick Falls, the Mall and the Ridge, then Kufri or Narkanda. Or continue to Manali on a Shimla–Manali trip. See our <a href="/himachal-tour-packages/">Himachal tour packages</a>, the <a href="/mall-road-shimla/">Mall Road Shimla guide</a> and <a href="/shimla/">Shimla</a>.</p>
<div class="sza-btns" style="margin-top:18px">{walink("Shimla 2N/3N — Get Quote", what="a 2–3 night Shimla trip with a Chadwick Falls half-day, Kufri or Narkanda, hotel and cab")}{walink("Shimla–Manali — Get Quote", what="a Shimla–Manali trip with a Chadwick Falls half-day, hotels and cab", cls="sza-btn line")}</div>
</section>

<section class="sza-sec sza-faq" id="faq">
<span class="sza-kicker">FAQ</span>
<h2>Chadwick Falls, Shimla — questions</h2>
{faq_html}
</section>

<section class="sza-sec alt" id="more">
<span class="sza-kicker">More adventures</span>
<h2>Explore more around Shimla</h2>
<div class="sza-cats">{more_html}</div>
</section>
</div>
'''
out = HERE / f"{SLUG}.html"
out.write_text(page, encoding="utf-8")
print(len(page))
