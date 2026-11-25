#!/usr/bin/env python3
# Generates adventure-kit/pages/gilbert-trail-kasauli.html (Page Builder night, 26 Nov 2026 IST)
import urllib.parse, pathlib
SLUG = "gilbert-trail-kasauli"
HERE = pathlib.Path(__file__).resolve().parent
CDN = "https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@b5fc816f097e80e561122df66dd4ae50b2bbf436/adventure-kit/media/gilbert-trail-kasauli/"
U11 = "https://suzutravels.com/wp-content/uploads/2026/11/"
QUOTE = "/himachal-tour-packages-quote/?activity=" + urllib.parse.quote("Gilbert Trail walk")
WHAT = "a Kasauli trip with the Gilbert Trail walk, cab and stay"

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

cards = "".join([
    card(f"{U11}suzu-kasauli-weather-g-4-768x432.webp", 768, 432,
         "Footpath on a pine-covered slope in Kasauli",
         "Easy · 1–3 h", "Gilbert Trail walk", "<b>~1.5 km · pine and oak · valley views</b>",
         "A quiet cliffside path through pine and oak on Kasauli's wooded slopes. Most guides start it near the Kasauli Club.",
         "the Gilbert Trail walk in Kasauli with cab"),
    card(f"{U11}suzu-kasauli-weather-g-1-768x513.webp", 768, 513,
         "Lower Himalayan ridges seen from Kasauli in morning haze",
         "Nature", "Bird-watching mornings", "<b>Go at dawn · carry binoculars</b>",
         "Travel guides single out the trail for bird-watchers. Early mornings are the quietest and best for birds.",
         "an early-morning Gilbert Trail bird walk in Kasauli"),
    card(f"{U11}suzu-kasauli-weather-fig-1-768x576.webp", 768, 576,
         "Light over a sea of clouds seen from Kasauli",
         "Evening", "Sunset Point", "<b>The usual end of the walk</b>",
         "Many walkers finish towards Sunset Point. Time the walk for the evening view, and be off the path before dark.",
         "the Gilbert Trail and Sunset Point in Kasauli"),
    ("<article class=\"sza-card\"><div class=\"img sza-noimg\"><span class=\"ic\" aria-hidden=\"true\">🛕</span><span class=\"sza-badge\">Nearby · rules apply</span></div>"
     "<div class=\"body\"><h3>Monkey Point (Manki Point)</h3><div class=\"meta\"><b>Inside the Air Force Station</b></div>"
     "<p class=\"meta\">A Hanuman temple at Kasauli's highest point. ID is checked; phones, cameras and bags are not allowed inside. Open roughly 9 am to 4–5 pm.</p>"
     f"<div class=\"go\"><a class=\"q\" href=\"{wa('a Kasauli day with the Gilbert Trail and Monkey Point')}\" target=\"_blank\" rel=\"noopener\">Get Quote →</a></div></div></article>"),
    card(f"{U11}suzu-kasauli-weather-g-6-768x576.webp", 768, 576,
         "Lower Mall road in Kasauli",
         "Heritage walk", "Christ Church &amp; the Mall", "<b>1853 church · car-free Mall walks</b>",
         "Round off the day with Christ Church (built 1853) and a slow walk on Kasauli's Mall Road.",
         "a Kasauli heritage day with the Gilbert Trail", page="/kasauli-tourist-places/", plabel="Kasauli places →"),
    card(f"{U11}suzu-kasauli-weather-g-2-768x542.webp", 768, 542,
         "Kasauli town at golden hour",
         "Package idea", "Kasauli weekend stay", "<b>Add Dagshai, Barog or Karol Tibba</b>",
         "Stay a night or two: the trail at dawn, Sunset Point in the evening, and Dagshai or Barog the next day.",
         "a 2-night Kasauli weekend with the Gilbert Trail, hotel and cab", page="/kasauli-tour-package/", plabel="Kasauli package →"),
])

steps_exp = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Send your date", "On WhatsApp, with your group size. We plan the cab from Chandigarh, Panchkula or Delhi, and a Kasauli stay if you want one."),
    ("Reach Kasauli", "About 60 km from Chandigarh via Parwanoo and Dharampur. The walk begins about 2 km from the bus stand area."),
    ("Walk the trail early", "Go slowly, with binoculars. The path is easy but runs along a cliff edge in places."),
    ("Sunset Point", "Many walkers finish towards Sunset Point. Monkey Point the same day only with ID and without phones or bags."),
    ("Lunch and the Mall", "Christ Church and a walk on the car-free Mall."),
    ("Onward", "Drive back, or go on to Dagshai, Barog or Shimla."),
])

booking = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Tell us", "WhatsApp or the quote form: date, group size and your pickup city."),
    ("We check your date", "Weekend crowds, rain, winter fog and fire season, and the best start time."),
    ("You get one quote", "Cab, stay and the rest of your Kasauli day: one plan, one rate."),
    ("Confirm and go", "We send the pickup time and what to carry."),
])

season = [
    ("Mar – Jun", "Clear, mild walks; busiest weekends", "Go at dawn. Apr–Jun is forest-fire season (a fire hit the Gilbert Trail slopes in May 2026)"),
    ("Jul – Sep", "Green and misty", "Slippery path; skip it on rainy days"),
    ("Oct – Nov", "Clear views, fewer crowds", "Best balance of views and quiet"),
    ("Dec – Feb", "Cold, foggy mornings; occasional light snow", "Go late morning or midday; carry a jacket and a torch in fog"),
]
season_html = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in season)

faqs = [
    ("How long is the Gilbert Trail?", "About 1.5 km. Most people take one to three hours with stops for views and birds."),
    ("Where does the Gilbert Trail start?", "Most guides start it near the Kasauli Club, about 2 km from the bus stand, and walk it towards the Air Force Station area and Sunset Point. Sources differ slightly on the exact start and end."),
    ("Is there an entry fee for the Gilbert Trail?", "No entry fee is reported for the trail."),
    ("Is the Gilbert Trail difficult?", "No, it is an easy walk. Parts run along a cliff edge and get slippery in rain or fog, so wear shoes with grip and keep children close."),
    ("When is the best time to walk it?", "Early morning in Mar–Jun or Sep–Nov. Avoid monsoon rain and foggy winter mornings. More on winter in our <a href=\"/kasauli-snowfall/\">Kasauli snowfall guide</a>."),
    ("Can I visit Monkey Point the same day?", "Yes. It is inside the Air Force Station and open roughly 9 am to 4–5 pm. Carry ID and leave phones, cameras and bags behind."),
    ("How far is Kasauli from Chandigarh?", "About 60 km by road via Parwanoo and Dharampur. See our <a href=\"/cabs/chandigarh-to-kasauli-taxi/\">Chandigarh to Kasauli taxi</a> page."),
    ("How much does a Kasauli trip with the Gilbert Trail cost?", "Get Quote. The rate depends on your pickup city and cab type, a day trip or a night stay, add-ons, season and group size. WhatsApp your date and we reply with today's rate within minutes."),
]
faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)

more = [
    ("/adventure/karol-tibba-trek/", "⛰️", "Karol Tibba trek", "Solan's highest hill"),
    ("/adventure/camping-near-shimla-kasauli/", "⛺", "Camping near Kasauli", "Nights under the stars"),
    ("/adventure/treks-near-shimla/", "🥾", "Treks near Shimla", "Day hikes around Shimla"),
    ("/adventure/shali-tibba-trek/", "🏔️", "Shali Tibba trek", "Shimla's highest viewpoint"),
    ("/adventure/adventure-activities-in-shimla/", "🧗", "Adventure in Shimla", "Everything around Shimla"),
    ("/adventure/trekking-in-himachal/", "🗺️", "Trekking in Himachal", "Every trek in the state"),
]
more_html = "".join(f'<a class="sza-cat" href="{h}"><span class="ic">{i}</span><span class="n">{n}</span><span class="c">{c}</span></a>' for h, i, n, c in more)

reel = (HERE.parent / "media" / SLUG / "reel-section.html").read_text(encoding="utf-8").strip()

page = f'''<!-- gilbert-trail-kasauli — built by Page Builder (night) 26 Nov 2026 IST from the Research Lead brief 25 Nov (Project doc claude/adventure-research/briefs/gilbert-trail-kasauli.md) + Visual Studio media @b5fc816. Kit v2.0. No prices, no operator names. Not stated (unverified): altitude, exact start/end, trail hours, post-fire trail state. Photos: real Kasauli library photos (none shows the trail itself) with neutral alt text. -->
<style>.sza-gtk .sza-hero-in>*{{max-width:620px}}@media(min-width:901px){{.sza-gtk .sza-hero-in>*{{max-width:min(560px,44vw)}}}}.sza-gtk .sza-chips{{max-width:700px}}.sza-gtk .sza-media ul{{padding-left:20px;list-style:disc;margin:0}}.sza-gtk .sza-media ul li{{margin:0 0 8px}}.sza-gtk .sza-media img{{height:auto;aspect-ratio:4/3;object-fit:cover}}.sza-gtk .sza-media video{{height:auto;aspect-ratio:16/9}}.sza-gtk #spots .sza-grid{{grid-template-columns:repeat(auto-fit,minmax(min(340px,100%),1fr))}}.sza-gtk .sza-noimg{{display:flex;align-items:center;justify-content:center;aspect-ratio:16/9;background:linear-gradient(135deg,#0b1f33,#1d3b5a)}}.sza-gtk .sza-noimg .ic{{font-size:64px}}.sza-gtk .sza-checks{{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}.sza-gtk .sza-choose{{margin-top:32px}}@media(min-width:1000px){{.sza-gtk #experience .sza-steps{{grid-template-columns:repeat(3,1fr)}}}}@media(max-width:820px){{.sza-gtk .sza-hero video{{object-position:30% 50%}}.sza-gtk .sza-hero:after{{background:linear-gradient(180deg,rgba(11,31,51,.45) 0%,rgba(11,31,51,.68) 45%,rgba(11,31,51,.95) 100%)}}}}</style>
<div class="sza sza-gtk">
<section class="sza-hero">
<video autoplay muted loop playsinline preload="metadata" poster="{U11}gilbert-trail-kasauli-hero-poster.webp" aria-label="A footpath on a pine slope in Kasauli, layered hills, Kasauli at golden hour and a sunset over clouds, with a dotted gold path from near the Kasauli Club to Sunset Point and a counter to about 1.5 km"><source src="{CDN}hero.webm" type="video/webm"><source src="{CDN}hero.mp4" type="video/mp4"></video>
<div class="sza-hero-in">
<span class="sza-kicker">Solan district · Kasauli · easy nature walk</span>
<p class="sza-hero-tag">Kasauli's quiet cliffside trail of pines, birds and sunsets</p>
<p class="sza-hero-sub">An easy ~1.5 km walk on Kasauli's wooded slopes, close to Sunset Point and the Mall. Suzu plans the Chandigarh pickup, the stay and the rest of the Kasauli day.</p>
<ul class="sza-chips"><li><b>~1.5 km</b> walk</li><li><b>1–3 h</b> with stops</li><li><b>Easy</b> level</li><li><b>Birds</b> at dawn</li><li><b>~60 km</b> from Chandigarh</li><li><b>Price</b> Get Quote</li></ul>
<div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan my trip</a></div>
<div class="sza-trust"><span><a href="https://suzutravels.com/certificates/">HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022</a></span><span>Himachal-based since 2019</span><span>Reply within minutes</span></div>
</div>
</section>
<nav class="sza-nav" aria-label="On this page"><div class="sza-nav-in"><a href="#overview">Overview</a><a href="#spots">Trail &amp; nearby</a><a href="#experience">How the day works</a><a href="#season">By month</a><a href="#safety">Safety</a><a href="#booking">How booking works</a><a href="#packages">Make it a trip</a><a href="#faq">FAQ</a><a class="cta" href="{MAIN}" target="_blank" rel="noopener">Get Quote</a></div></nav>

<section class="sza-sec" id="overview">
<span class="sza-kicker">Quick answer</span>
<h2>Gilbert Trail, Kasauli, at a glance</h2>
<p class="sza-answer">The Gilbert Trail is an easy, roughly 1.5 km nature walk on the wooded cliffside of Kasauli in Solan district. Most guides start it near the Kasauli Club and take it towards the Air Force Station area and Sunset Point. Allow one to three hours with stops. Go early for birds and quiet, and avoid wet or foggy days.</p>
<div class="sza-facts"><div class="sza-fact"><div class="k">Where</div><div class="v">Kasauli, Solan district, Himachal Pradesh; about 2 km from the bus stand</div></div><div class="sza-fact"><div class="k">Length</div><div class="v">About 1.5 km</div></div><div class="sza-fact"><div class="k">Time</div><div class="v">1–3 hours including stops</div></div><div class="sza-fact"><div class="k">Level</div><div class="v">Easy; parts run along a cliff edge and get slippery</div></div><div class="sza-fact"><div class="k">Best time</div><div class="v">Early morning; Mar–Jun and Sep–Nov; avoid rain and fog</div></div><div class="sza-fact"><div class="k">Price</div><div class="v">Get Quote</div></div></div>
<div class="sza-media" style="margin-top:28px"><img src="{U11}suzu-kasauli-weather-g-4-768x432.webp" alt="Footpath on a pine-covered slope in Kasauli" loading="lazy" width="768" height="432"><div><h3>Is the Gilbert Trail for you?</h3><ul><li><b>Want an easy walk near Chandigarh</b> → yes: short, scenic and no climbing.</li><li><b>Families</b> → fine with children, holding hands at the cliff edge.</li><li><b>Bird-watchers</b> → go at dawn with binoculars.</li><li><b>Want a real trek</b> → try <a href="/adventure/karol-tibba-trek/">Karol Tibba near Solan</a> or the <a href="/adventure/shali-tibba-trek/">Shali Tibba trek</a> near Shimla.</li></ul><p>More in Kasauli: <a href="/kasauli-tourist-places/">Kasauli tourist places</a> and <a href="/kasauli-tour-package/">Kasauli tour package</a>.</p></div></div>
</section>

<section class="sza-sec alt" id="spots">
<span class="sza-kicker">Trail &amp; nearby</span>
<h2>The Gilbert Trail and what to pair it with</h2>
<p class="sza-lead">Walk the trail early, end towards Sunset Point, and round off the day with Monkey Point, Christ Church and the Mall.</p>
<div class="sza-grid">{cards}</div>
<div class="sza-media sza-choose" id="route"><video autoplay muted loop playsinline preload="none" poster="{U11}gilbert-trail-kasauli-explainer-poster.webp" width="1600" height="900" aria-label="Schematic map: Chandigarh to Parwanoo and Dharampur to the Kasauli bus stand, about 60 km by road; about 2 km to the Kasauli Club; the dotted Gilbert Trail of about 1.5 km to Sunset Point; side pins for Monkey Point inside the Air Force Station and for Christ Church and the Mall"><source src="{CDN}explainer.webm" type="video/webm"><source src="{CDN}explainer.mp4" type="video/mp4"></video><div><h3>Chandigarh → Kasauli → Gilbert Trail</h3><ul><li><b>Chandigarh</b> → about 60 km via Parwanoo and Dharampur.</li><li><b>Kasauli bus stand</b> → about 2 km on foot to the Kasauli Club area.</li><li><b>Gilbert Trail</b> → about 1.5 km, 1–3 hours with stops.</li><li><b>Sunset Point</b> → the usual end of the walk.</li><li><b>Monkey Point</b> → Air Force Station rules: ID, no phones.</li></ul><p>Schematic, not to scale.</p></div></div>
</section>

<section class="sza-sec" id="experience">
<span class="sza-kicker">How the day works</span>
<h2>A Kasauli day with the Gilbert Trail, step by step</h2>
<ol class="sza-steps">{steps_exp}</ol>
<div class="sza-media"><img src="{U11}suzu-kasauli-weather-g-1-768x513.webp" alt="Lower Himalayan ridges seen from Kasauli in morning haze" loading="lazy" width="768" height="513"><div><h3>What to carry</h3><ul><li>Shoes with good grip</li><li>Water and a light snack (carry no loose food: monkeys are common)</li><li>Binoculars for birds</li><li>A warm layer; in winter fog, a torch</li><li>ID if you plan to visit Monkey Point</li></ul><p>Polythene is banned in Himachal: take all your waste back with you.</p></div></div>
</section>

<section class="sza-sec alt" id="season">
<span class="sza-kicker">When to go</span>
<h2>Gilbert Trail by month</h2>
<div class="sza-scroll"><table class="sza-tbl"><thead><tr><th>Months</th><th>What you get</th><th>Note</th></tr></thead><tbody>{season_html}</tbody></table></div>
<div class="sza-media" style="margin-top:28px"><img src="{U11}suzu-kasauli-weather-g-2-768x542.webp" alt="Kasauli town at golden hour" loading="lazy" width="768" height="542"><div><h3>Winter in Kasauli</h3><p>Dec–Feb mornings are cold and often foggy, and Kasauli sometimes gets light snow. Walk late morning or midday, carry a jacket and a torch, and skip the cliff edge in thick fog. See <a href="/kasauli-snowfall/">Kasauli snowfall</a> and our <a href="/adventure/winter-treks-in-himachal/">winter treks guide</a>.</p></div></div>
</section>

<div class="sza-band" id="safety"><div class="sza-band-in">
<span class="sza-kicker">Safety</span>
<h2>What we check before your Gilbert Trail walk</h2>
<p class="sza-lead">Suzu Travels is an <a href="https://suzutravels.com/certificates/" style="color:#f3d98f;text-decoration:underline">HP Tourism registered travel agent (Reg. No. DTO-MND-11-243/2022)</a>. We plan your Kasauli day around these checks:</p>
<ul class="sza-checks"><li><b>Cliff edge</b>The path runs along a cliffside. Stay on the trail, keep children close and take no selfies at the edge.</li><li><b>Rain and fog</b>Wet days and winter fog make it slippery. Wear proper shoes, carry a torch in fog and skip it in rain.</li><li><b>Fire season</b>A forest fire burned the Gilbert Trail slopes on 26–27 May 2026. In Apr–Jun never smoke or light a fire, and turn back if you see smoke.</li><li><b>Monkeys</b>Monkeys are common in Kasauli. Carry no loose food and keep bags closed.</li><li><b>Air Force area</b>Follow the signboards. At Monkey Point, ID is checked and phones, cameras and bags are not allowed.</li><li><b>Leave no trace</b>Polythene is banned; don't litter, and don't feed wild animals.</li></ul>
</div></div>

<section class="sza-sec" id="booking">
<span class="sza-kicker">How booking works</span>
<h2>Get a quote in minutes</h2>
<ol class="sza-steps">{booking}</ol>
<div class="sza-media"><img src="{U11}suzu-kasauli-weather-fig-1-768x576.webp" alt="Light over a sea of clouds seen from Kasauli" loading="lazy" width="768" height="576"><div><h3>What your quote depends on</h3><ul><li>Pickup city (Chandigarh, Panchkula, Delhi) and cab type</li><li>A day trip, or a night or two in Kasauli</li><li>Add-ons: Dagshai, Barog, Chail, the <a href="/adventure/karol-tibba-trek/">Karol Tibba trek</a>, <a href="/adventure/camping-near-shimla-kasauli/">camping near Kasauli</a></li><li>Season, and weekend vs weekday</li><li>Group size</li></ul><p>We send today's rate on WhatsApp within minutes.</p></div></div>
</section>

{reel}

<section class="sza-quote"><div><span class="sza-kicker">Ready for a Kasauli walk?</span><h2>Get your Kasauli quote</h2><p>Tell us your date and group size. We reply with one plan (cab, stay and the Gilbert Trail day) within minutes.</p></div><div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan full trip</a></div></section>

<section class="sza-sec" id="packages">
<span class="sza-kicker">Make it a trip</span>
<h2>Add the Gilbert Trail to a Kasauli weekend</h2>
<p>A good plan is two nights in Kasauli: the Gilbert Trail at dawn and Sunset Point in the evening, then Monkey Point, Christ Church and a drive to Dagshai or Barog. Or continue to Shimla for a 3-night Kasauli–Shimla trip with the <a href="/adventure/shali-tibba-trek/">Shali Tibba trek</a>. Coming from Chandigarh? See the <a href="/cabs/chandigarh-to-kasauli-taxi/">Chandigarh to Kasauli taxi</a>.</p>
<div class="sza-btns" style="margin-top:18px">{walink("2N Kasauli weekend — Get Quote", what="a 2-night Kasauli weekend with the Gilbert Trail, Sunset Point, Monkey Point, Dagshai, hotel and cab")}{walink("Kasauli day trip — Get Quote", what="a Kasauli day trip from Chandigarh with the Gilbert Trail and cab", cls="sza-btn line")}</div>
</section>

<section class="sza-sec sza-faq" id="faq">
<span class="sza-kicker">FAQ</span>
<h2>Gilbert Trail, Kasauli — questions</h2>
{faq_html}
</section>

<section class="sza-sec alt" id="more">
<span class="sza-kicker">More adventures</span>
<h2>Explore more near Kasauli and Shimla</h2>
<div class="sza-cats">{more_html}</div>
</section>
</div>
'''
out = HERE / f"{SLUG}.html"
out.write_text(page, encoding="utf-8")
print(len(page))
