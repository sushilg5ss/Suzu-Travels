#!/usr/bin/env python3
# Generates adventure-kit/pages/bahadurpur-fort-trek.html (Page Builder night, 24 Nov 2026 IST)
import urllib.parse, pathlib
SLUG = "bahadurpur-fort-trek"
HERE = pathlib.Path(__file__).resolve().parent
CDN = "https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@085601219939bd31e1aeb80eea9cf9b9ca54640a/adventure-kit/media/bahadurpur-fort-trek/"
U11 = "https://suzutravels.com/wp-content/uploads/2026/11/"
QUOTE = "/himachal-tour-packages-quote/?activity=" + urllib.parse.quote("Bahadurpur Fort trek")
WHAT = "a Bilaspur trip with the Bahadurpur Fort forest walk"

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
    card(f"{U11}bahadurpur-fort-trek-hero-poster.webp", 1600, 900,
         "Graphic: misty conifer forest beside an altitude line from Namhol up an 11 km hill road to the Forest Rest House at 1,872 m and the fort ruins at about 1,980 m",
         "Must see", "Bahadurpur Fort ruins", "<b>Hilltop · about 1,980 m</b>",
         "Stone ruins of the fort Raja Keshab Sen built in 1620, on top of the district's highest hill.",
         "a Bahadurpur Fort day trip from Bilaspur"),
    card(f"{U11}suzu-chakrata-weather-g-3-768x437.webp", 768, 437,
         "Mist among tall deodar trees in a hill forest",
         "Nature walk", "Deodar &amp; ban-oak forest", "<b>Bilaspur's only reserve forest</b>",
         "Deodar, ban oak and chil pine on the hill: a cool, quiet walk when the valley below is hot.",
         "a forest walk at Bahadurpur"),
    card(f"{U11}sunrise-over-layered-hill-ridges-768x512.webp", 768, 512,
         "Sun rising over layers of misty hill ridges",
         "Views", "Viewpoint over the forts", "<b>Clearest Oct–Nov</b>",
         "Look out towards Naina Devi hill, the old forts of Ratanpur, Fatehpur and Swarghat, and the plains towards Ropar.",
         "a Bahadurpur Fort viewpoint trip"),
    card(f"{U11}misty-conifer-forest-footpath-768x1152.webp", 768, 1152,
         "Earth footpath climbing through misty conifer forest with green undergrowth",
         "Ask first", "Bara Dev temple walk", "<b>About 5 km from the Forest Rest House</b>",
         "An old bridle path to the Bara Dev temple at Bari Dhar. A longer walk: we add a local guide.",
         "the Bara Dev temple walk from Bahadurpur with a local guide"),
    card(f"{U11}bahadurpur-fort-trek-explainer-poster.webp", 1600, 900,
         "Schematic map: Bilaspur town to Namhol, then an 11 km hill road to the Forest Rest House at 1,872 m and the fort ruins at about 1,980 m",
         "Stay", "Forest Rest House night", "<b>HP Forest Dept · 1,872 m</b>",
         "The Bahadurpur Forest Rest House (built 2007-08) is booked through HP Eco-tourism. We plan the cab around it, or a Bilaspur hotel.",
         "a night near Bahadurpur Fort with cab"),
    card(f"{U11}light-snow-on-forest-trees-768x1152.webp", 768, 1152,
         "Light fresh snow on the branches of forest trees in winter",
         "Seasonal", "Winter snow day", "<b>Dec–Feb · some days only</b>",
         "The hill gets light snow some winter days, the closest snow to Bilaspur town. We check the road first.",
         "a winter snow day at Bahadurpur (road permitting)"),
])

steps_exp = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Send your date", "On WhatsApp. Our team in Ghumarwin, Bilaspur plans the cab and the timing, and the Forest Rest House night if you want one."),
    ("Drive to Namhol", "From Bilaspur town, Ghumarwin or Kiratpur. Bahadurpur is about 40 km from Bilaspur town."),
    ("Up the hill road", "A metalled road climbs 11 km from Namhol to the Bahadurpur Forest Rest House at 1,872 m."),
    ("Forest walk to the top", "Through deodar and ban oak to the fort ruins at about 1,980 m. Your driver or a local guide shows the path."),
    ("Take in the views", "Naina Devi hill, the old Kahlur forts and, on clear days, the plains. Optional: the Bara Dev temple path."),
    ("Back before dark", "Drive down in daylight, or add Gobind Sagar, Bandla or Naina Devi on the same trip."),
])

booking = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Tell us", "WhatsApp or the quote form: date, group size and your pickup point."),
    ("We check your date", "The weather and the hill road, especially after snow or heavy rain."),
    ("You get one quote", "Cab, an optional guide and your stay: one plan, one rate."),
    ("Confirm and go", "We send the pickup time and what to carry."),
])

season = [
    ("Dec – Feb", "Cold, clear days; light snow some days", "Closest snow to Bilaspur town; we check the road after snowfall"),
    ("Mar – Jun", "Pleasant forest walks, a cool escape from the Bilaspur heat", "Best for families"),
    ("Jul – Sep", "Green and misty; leeches on forest paths", "Go on clear days; landslide checks on the hill road"),
    ("Oct – Nov", "The clearest views over the forts and the plains", "Best for photos"),
]
season_html = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in season)

faqs = [
    ("Where is Bahadurpur Fort?", "On Bahadurpur hill near Tepra village in Bilaspur district, about 40 km from Bilaspur town. A metalled road climbs 11 km from Namhol to the Forest Rest House below the top."),
    ("How high is Bahadurpur Fort?", "About 1,980 m, the highest point in Bilaspur district. The Forest Rest House just below is listed at 1,872 m."),
    ("Who built Bahadurpur Fort?", "Raja Keshab Sen of Bilaspur (Kahlur) built it in 1620 AD. It is in ruins today."),
    ("Does it snow at Bahadurpur?", "Yes, the hill gets light snow some winter days, which is rare this close to Bilaspur town. We check the road after a snowfall before we send the cab. For sure snow, see our <a href=\"/adventure/winter-treks-in-himachal/\">winter treks guide</a>."),
    ("Is there a place to stay at Bahadurpur?", "The HP Forest Department's Bahadurpur Forest Rest House (built 2007-08) can be booked through HP Eco-tourism. We can also plan a hotel in Bilaspur or Ghumarwin."),
    ("How long is the walk to the fort?", "It is a forest walk from the road to the hilltop; your driver or a local guide shows the path. We don't publish a distance or time because no reliable source gives one."),
    ("Is there an entry fee?", "No entry fee is reported for the fort."),
    ("What can I combine it with?", "<a href=\"/adventure/paragliding-in-bilaspur/\">Bandla paragliding</a>, <a href=\"/adventure/gobind-sagar-water-sports/\">Gobind Sagar water sports</a>, <a href=\"/adventure/kol-dam-water-sports/\">Kol Dam</a> and the <a href=\"/adventure/naina-devi-ropeway/\">Naina Devi ropeway</a>, all in Bilaspur district."),
    ("How much does a Bahadurpur Fort trip cost?", "Get Quote. The rate depends on your pickup point and cab type, a day trip or a night stay, the season and road, a guide and group size. WhatsApp your date and we reply with today's rate within minutes."),
]
faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)

more = [
    ("/adventure/paragliding-in-bilaspur/", "🪂", "Bandla paragliding", "Bilaspur by air"),
    ("/adventure/gobind-sagar-water-sports/", "🚤", "Gobind Sagar water sports", "Lake day in Bilaspur"),
    ("/adventure/kol-dam-water-sports/", "🌊", "Kol Dam water sports", "On the Sutlej"),
    ("/adventure/naina-devi-ropeway/", "🚡", "Naina Devi ropeway", "Up to the temple"),
    ("/adventure/trekking-in-himachal/", "🥾", "Trekking in Himachal", "Every trek in the state"),
    ("/adventure/winter-treks-in-himachal/", "❄️", "Winter treks", "Snow-season picks"),
]
more_html = "".join(f'<a class="sza-cat" href="{h}"><span class="ic">{i}</span><span class="n">{n}</span><span class="c">{c}</span></a>' for h, i, n, c in more)

reel = (HERE.parent / "media" / SLUG / "reel-section.html").read_text(encoding="utf-8").strip()

page = f'''<!-- bahadurpur-fort-trek — built by Page Builder (night) 24 Nov 2026 IST from the Research Lead brief 23 Nov (Project doc claude/adventure-research/briefs/bahadurpur-fort-trek.md) + Visual Studio media @0856012. Kit v2.0. No prices, no operator names. Not stated (unverified): walk length/time from road to top, drive times. All photos are generic (neutral alt); fort/FRH cards use the kit's own graphics. -->
<style>.sza-bhf .sza-hero-in>*{{max-width:620px}}@media(min-width:901px){{.sza-bhf .sza-hero-in>*{{max-width:min(560px,44vw)}}}}.sza-bhf .sza-chips{{max-width:700px}}.sza-bhf .sza-media ul{{padding-left:20px;list-style:disc;margin:0}}.sza-bhf .sza-media ul li{{margin:0 0 8px}}.sza-bhf .sza-media img{{height:auto;aspect-ratio:4/3;object-fit:cover}}.sza-bhf .sza-media video{{height:auto;aspect-ratio:16/9}}.sza-bhf #spots .sza-grid{{grid-template-columns:repeat(auto-fit,minmax(min(340px,100%),1fr))}}.sza-bhf .sza-checks{{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}.sza-bhf .sza-choose{{margin-top:32px}}@media(min-width:1000px){{.sza-bhf #experience .sza-steps{{grid-template-columns:repeat(3,1fr)}}}}@media(max-width:820px){{.sza-bhf .sza-hero video{{object-position:30% 50%}}.sza-bhf .sza-hero:after{{background:linear-gradient(180deg,rgba(11,31,51,.45) 0%,rgba(11,31,51,.68) 45%,rgba(11,31,51,.95) 100%)}}}}</style>
<div class="sza sza-bhf">
<section class="sza-hero">
<video autoplay muted loop playsinline preload="metadata" poster="{U11}bahadurpur-fort-trek-hero-poster.webp" aria-label="Misty conifer forest with a gold altitude line from Namhol up an 11 km hill road to the Forest Rest House at 1,872 m and the Bahadurpur Fort ruins at about 1,980 m, the highest point of Bilaspur district, built 1620 AD"><source src="{CDN}hero.webm" type="video/webm"><source src="{CDN}hero.mp4" type="video/mp4"></video>
<div class="sza-hero-in">
<span class="sza-kicker">Bilaspur · Himachal · forest hill fort</span>
<p class="sza-hero-tag">Bilaspur's highest hill: deodar, oak and a 1620 fort ruin</p>
<p class="sza-hero-sub">A quiet forest walk near Tepra village, about 40 km from Bilaspur town. Our own team in Ghumarwin, Bilaspur plans the cab from Ghumarwin, Bilaspur or Kiratpur.</p>
<ul class="sza-chips"><li><b>~1,980 m</b> highest point of Bilaspur</li><li><b>Built</b> 1620 AD</li><li><b>Deodar</b>, ban oak, chil</li><li><b>Light snow</b> in winter</li><li><b>Forest Rest House</b></li><li><b>Price</b> Get Quote</li></ul>
<div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan my trip</a></div>
<div class="sza-trust"><span><a href="https://suzutravels.com/certificates/">HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022</a></span><span>Office in Ghumarwin, Bilaspur</span><span>Reply within minutes</span></div>
</div>
</section>
<nav class="sza-nav" aria-label="On this page"><div class="sza-nav-in"><a href="#overview">Overview</a><a href="#spots">What to see</a><a href="#experience">How the day works</a><a href="#season">By month</a><a href="#safety">Safety</a><a href="#booking">How booking works</a><a href="#packages">Make it a trip</a><a href="#faq">FAQ</a><a class="cta" href="{MAIN}" target="_blank" rel="noopener">Get Quote</a></div></nav>

<section class="sza-sec" id="overview">
<span class="sza-kicker">Quick answer</span>
<h2>Bahadurpur Fort, at a glance</h2>
<p class="sza-answer">Bahadurpur Fort sits on Bahadurpur hill near Tepra village, at about 1,980 m the highest point in Bilaspur district. Raja Keshab Sen built it in 1620; today it is a ruin in the district's only reserve forest of deodar, ban oak and chil. A metalled road runs 11 km up from Namhol to the Forest Rest House. The hill gets light snow in winter.</p>
<div class="sza-facts"><div class="sza-fact"><div class="k">Where</div><div class="v">Bahadurpur hill near Tepra village, Sadar tehsil, about 40 km from Bilaspur town</div></div><div class="sza-fact"><div class="k">Height</div><div class="v">About 1,980 m, the district's highest point; the Forest Rest House is listed at 1,872 m</div></div><div class="sza-fact"><div class="k">Road</div><div class="v">Metalled road, 11 km from Namhol up to the Bahadurpur Forest Rest House</div></div><div class="sza-fact"><div class="k">History</div><div class="v">Built by Raja Keshab Sen of Bilaspur (Kahlur) in 1620 AD; now ruins</div></div><div class="sza-fact"><div class="k">Season</div><div class="v">All year: light snow some winter days, cool summers when Bilaspur town is hot</div></div><div class="sza-fact"><div class="k">Price</div><div class="v">Get Quote</div></div></div>
<div class="sza-media" style="margin-top:28px"><img src="{U11}suzu-kasauli-weather-g-1-768x513.webp" alt="Layers of forested lower Himalayan ridges under a hazy sky" loading="lazy" width="768" height="513"><div><h3>Is Bahadurpur for you?</h3><ul><li><b>A quiet day out near Bilaspur</b> → a forest walk and a fort ruin, no crowds.</li><li><b>Families</b> → yes; the road goes most of the way up.</li><li><b>Want snow near the plains</b> → some winter days only; ask us first.</li><li><b>Already doing water sports or paragliding</b> → add it as a half day.</li></ul><p>More in the district: <a href="/bilaspur-ghumne-ki-jagah/">places to visit in Bilaspur</a>, <a href="/adventure/gobind-sagar-water-sports/">Gobind Sagar</a> and <a href="/adventure/paragliding-in-bilaspur/">Bandla paragliding</a>.</p></div></div>
</section>

<section class="sza-sec alt" id="spots">
<span class="sza-kicker">What to see</span>
<h2>Six things to do at Bahadurpur</h2>
<p class="sza-lead">The fort ruins and the forest walk, the views, a longer temple path, a night at the Forest Rest House, or a winter snow day.</p>
<div class="sza-grid">{cards}</div>
<div class="sza-media sza-choose" id="route"><video autoplay muted loop playsinline preload="none" poster="{U11}bahadurpur-fort-trek-explainer-poster.webp" width="1600" height="900" aria-label="Schematic map: Suzu's office in Ghumarwin, Bilaspur town, then Namhol and an 11 km hill road to the Forest Rest House at 1,872 m and the fort ruins at about 1,980 m; dotted links to Bandla, Gobind Sagar and Naina Devi; a month strip with Mar to Jun and Oct to Nov highlighted"><source src="{CDN}explainer.webm" type="video/webm"><source src="{CDN}explainer.mp4" type="video/mp4"></video><div><h3>Bilaspur → Namhol → Bahadurpur</h3><ul><li><b>Bilaspur town</b> → about 40 km to the fort.</li><li><b>Namhol</b> → the road-head town.</li><li><b>11 km hill road</b> → the Forest Rest House, 1,872 m.</li><li><b>Forest walk</b> → the fort ruins, about 1,980 m.</li><li><b>Same trip</b> → Bandla, Gobind Sagar or Naina Devi.</li></ul><p>Schematic, not to scale.</p></div></div>
</section>

<section class="sza-sec" id="experience">
<span class="sza-kicker">How the day works</span>
<h2>A Bahadurpur Fort day with Suzu, step by step</h2>
<ol class="sza-steps">{steps_exp}</ol>
<div class="sza-media"><img src="{U11}misty-conifer-forest-footpath-768x1152.webp" alt="Earth footpath climbing through misty conifer forest with green undergrowth" loading="lazy" width="768" height="1152"><div><h3>What to carry</h3><ul><li>Water and food: no facilities are reported at the top beyond the Forest Rest House</li><li>Shoes with good grip for the forest path</li><li>A warm layer; more in winter</li><li>A rain shell in the monsoon, and leech socks on wet days</li></ul><p>Polythene is banned in Himachal: take all your waste back down.</p></div></div>
</section>

<section class="sza-sec alt" id="season">
<span class="sza-kicker">When to go</span>
<h2>Bahadurpur Fort by month</h2>
<div class="sza-scroll"><table class="sza-tbl"><thead><tr><th>Months</th><th>What you get</th><th>Note</th></tr></thead><tbody>{season_html}</tbody></table></div>
<div class="sza-media" style="margin-top:28px"><img src="{U11}light-snow-on-forest-trees-768x1152.webp" alt="Light fresh snow on the branches of forest trees in winter" loading="lazy" width="768" height="1152"><div><h3>Hoping for snow?</h3><p>Bahadurpur gets light snow on some winter days, the closest snow to Bilaspur town. It is never certain, and the hill road can be icy just after a snowfall, so we check before we send the cab.</p><p>For surer snow, see our <a href="/adventure/winter-treks-in-himachal/">winter treks guide</a> or all <a href="/adventure/trekking-in-himachal/">trekking in Himachal</a>.</p></div></div>
</section>

<div class="sza-band" id="safety"><div class="sza-band-in">
<span class="sza-kicker">Safety</span>
<h2>What we check before your Bahadurpur trip</h2>
<p class="sza-lead">Suzu Travels is an <a href="https://suzutravels.com/certificates/" style="color:#f3d98f;text-decoration:underline">HP Tourism registered travel agent (Reg. No. DTO-MND-11-243/2022)</a>. We arrange guides with registered local operators and plan around these checks:</p>
<ul class="sza-checks"><li><b>Stay on the path</b>It is a forest, not a park: no trail map is published. Go with the driver or a local guide, and don't leave the path in fog.</li><li><b>Road after snow</b>The hill road can be icy after a snowfall. We send a hill-trained driver and advise against self-drive on snow.</li><li><b>Reserve forest rules</b>No fires and no litter. Camping only with Forest Department permission; we don't arrange camping here.</li><li><b>Carry your own</b>Water and food: no facilities are reported at the top beyond the Forest Rest House.</li><li><b>Loose stone walls</b>The ruins are unguarded. Keep children off the walls.</li><li><b>Monsoon</b>Jul–Sep brings mist and leeches. We go on clear days and check the hill road for slips.</li></ul>
</div></div>

<section class="sza-sec" id="booking">
<span class="sza-kicker">How booking works</span>
<h2>Get a quote in minutes</h2>
<ol class="sza-steps">{booking}</ol>
<div class="sza-media"><img src="{U11}sunrise-over-layered-hill-ridges-768x512.webp" alt="Sun rising over layers of misty hill ridges" loading="lazy" width="768" height="512"><div><h3>What your quote depends on</h3><ul><li>Pickup point (Ghumarwin, Bilaspur, Kiratpur/Anandpur, Chandigarh) and cab type</li><li>A day trip, or a night at the Forest Rest House or a Bilaspur hotel</li><li>The season and road condition after snowfall</li><li>A local guide for the forest walk or the Bara Dev temple path</li><li>Group size</li><li>Add-ons: Bandla paragliding, Gobind Sagar water sports, Naina Devi ropeway, Kol Dam</li></ul><p>We send today's rate on WhatsApp within minutes.</p></div></div>
</section>

{reel}

<section class="sza-quote"><div><span class="sza-kicker">Ready for Bilaspur's highest hill?</span><h2>Get your Bahadurpur Fort quote</h2><p>Tell us your date and group size. Our Bilaspur team replies with one plan (cab, guide and stay) within minutes.</p></div><div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan full trip</a></div></section>

<section class="sza-sec" id="packages">
<span class="sza-kicker">Make it a trip</span>
<h2>Add Bahadurpur to a Bilaspur weekend</h2>
<p>A good plan from Chandigarh is one night in Bilaspur: Bahadurpur Fort on one day, <a href="/adventure/gobind-sagar-water-sports/">Gobind Sagar water sports</a> and <a href="/adventure/paragliding-in-bilaspur/">Bandla paragliding</a> on the other. Or add it as a day on the Chandigarh–Manali route through Bilaspur, with the <a href="/adventure/naina-devi-ropeway/">Naina Devi ropeway</a> on the way.</p>
<div class="sza-btns" style="margin-top:18px">{walink("1N Bilaspur weekend — Get Quote", what="a 1-night Bilaspur weekend with Bahadurpur Fort, Gobind Sagar, Bandla, hotel and cab")}{walink("Add to a Manali trip — Get Quote", what="a Bahadurpur Fort day added to my Chandigarh–Manali trip", cls="sza-btn line")}</div>
</section>

<section class="sza-sec sza-faq" id="faq">
<span class="sza-kicker">FAQ</span>
<h2>Bahadurpur Fort — questions</h2>
{faq_html}
</section>

<section class="sza-sec alt" id="more">
<span class="sza-kicker">More adventures</span>
<h2>Explore more in Bilaspur</h2>
<div class="sza-cats">{more_html}</div>
</section>
</div>
'''
out = HERE / f"{SLUG}.html"
out.write_text(page, encoding="utf-8")
print(len(page))
