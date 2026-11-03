#!/usr/bin/env python3
# Generates adventure-kit/pages/pong-dam-bird-watching-water-sports.html (Page Builder night, 4 Nov 2026 IST)
import urllib.parse, pathlib
SLUG = "pong-dam-bird-watching-water-sports"
HERE = pathlib.Path(__file__).resolve().parent
CDN = "https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@9a95df58a2dbe92a3453740c46ec39a4ec1c5f3f/adventure-kit/media/pong-dam-bird-watching-water-sports/"
UP10 = "https://suzutravels.com/wp-content/uploads/2026/10/"
UP11 = "https://suzutravels.com/wp-content/uploads/2026/11/"
QUOTE = "/himachal-tour-packages-quote/?activity=" + urllib.parse.quote("Water sports")
WHAT = "a Pong Dam Lake trip (bird-watching / boating) in Kangra"

def wa(what=WHAT, tag=SLUG):
    t = f"Hi Suzu Travels, I want a quote for {what}. Travel date: ___ , people: ___ (page: {tag})"
    return "https://wa.me/917087488961?text=" + urllib.parse.quote(t, safe="")

def walink(label, what=WHAT, cls="sza-btn gold"):
    return f'<a class="{cls}" href="{wa(what)}" target="_blank" rel="noopener">{label}</a>'

MAIN = wa()

def card(src, w, h, alt, badge, title, meta, text, what, page=None):
    explore = f'<a class="x" href="{page}">Explore →</a>' if page else ""
    return (f'<article class="sza-card"><div class="img"><img src="{src}" alt="{alt}" loading="lazy" width="{w}" height="{h}"><span class="sza-badge">{badge}</span></div>'
            f'<div class="body"><h3>{title}</h3><div class="meta">{meta}</div><p class="meta">{text}</p>'
            f'<div class="go"><a class="q" href="{wa(what)}" target="_blank" rel="noopener">Get Quote →</a>{explore}</div></div></article>')

cards = "".join([
    card(f"{UP11}huge-flock-of-geese-in-flight-over-wetland-768x483.webp", 768, 483,
         "A huge flock of geese in flight over a flat wetland",
         "Winter pick", "Nagrota Surian bird-watching", "<b>Sanctuary shore · Nov–Feb</b>",
         "The lake's best-known bird-watching base; go at sunrise, when the flocks are on the water. The state is developing guided bird-watching here (Jan 2026).",
         "bird-watching at Nagrota Surian, Pong Dam Lake"),
    card(f"{UP10}two-kayakers-lake-hazy-hills-768x510.webp", 768, 510,
         "Two kayakers on a still lake below layers of hazy hills",
         "Classic pick", "Khatiyar water-sports centre", "<b>Boating · kayaking · canoeing · sailing · rowing</b>",
         "The state's regional water-sports centre on the lake. Rancer island is about 20 minutes away by boat.",
         "boating or kayaking at the Khatiyar water-sports centre, Pong Dam"),
    card(f"{UP10}old-stone-shrine-reflected-in-water-768x988.webp", 768, 988,
         "Old stone shrine on a grassy bank, reflected in still water",
         "Photo spot", "Bathu ki Ladi temples", "<b>Show when the water drops</b>",
         "Stone temples that stay under the lake about eight months a year and appear as the level falls, usually from about March to June.",
         "a Pong Dam trip to see the Bathu ki Ladi temples"),
    card(f"{UP11}birdwatcher-with-binoculars-by-winter-lake-683x1024.webp", 683, 1024,
         "A man watching birds through binoculars beside a lake in winter",
         "For learners", "ABVIMAS Pong Dam centre", "<b>Multi-day water-sports courses</b>",
         "The state mountaineering and allied sports institute has run a water-sports centre at Pong since 1980 — for people who want a proper course, not a ride.",
         "a water-sports course at Pong Dam"),
    card(f"{UP10}boat-ride-orange-life-jackets-lake-768x768.webp", 768, 768,
         "Small boat with riders in orange life jackets on a green lake beside a wooded shore",
         "Local tip", "Fatehpur / Dhameta side", "<b>Quieter western arm</b>",
         "Quieter access points with a district boating point at Fatehpur. What runs varies by season and water level — we check before you go.",
         "boating on the Fatehpur / Dhameta side of Pong Dam"),
])

steps_exp = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Tell us your plan", "Dates, start point (Dharamshala, McLeod Ganj, Kangra, Pathankot, Amritsar, Chandigarh) and what you want: birds, boating or both."),
    ("We check the week", "What is running at the water-sports centre, boat availability, and the lake level for Bathu ki Ladi."),
    ("Sunrise: birds", "Reach Nagrota Surian early and watch the flocks along the shore, Nov–Feb."),
    ("Late morning: on the water", "A boat ride or a kayak / canoe session at Khatiyar, life jackets on."),
    ("Afternoon", "Bathu ki Ladi if the water is low, or Rancer island; back to Dharamshala or on to your next stop."),
    ("One quote", "Hotel + cab in the same plan; add <a href=\"/adventure/paragliding-in-bir-billing/\">Bir</a>, <a href=\"/adventure/triund-trek/\">Triund</a> or <a href=\"/adventure/paragliding-in-dharamshala/\">Dharamshala paragliding</a> on other days."),
])

booking = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Tell us", "WhatsApp or the quote form — date, group size, kids' ages and where you start."),
    ("We check your date", "Bird season, lake level, weather, the monsoon rule and a registered local operator."),
    ("You get one quote", "Lake day, hotel nights and cab in one plan."),
    ("Confirm and go", "We send the meeting point, timing and what to carry."),
])

season = [
    ("Nov – Feb", "Migratory birds peak; cool, clear days, foggy mornings", "Bird-watching, photography"),
    ("Mar – Jun", "Birds leave by March; lake level drops and Bathu ki Ladi temples appear; warm to hot", "Bathu ki Ladi, boating"),
    ("Jul – mid Sep", "Monsoon; Kangra water-sports ban 15 Jul – 15 Sep; the lake fills", "Avoid water activities"),
    ("Mid Sep – Oct", "Calm water; the first birds arrive in late October", "Boating, water sports"),
]
season_html = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in season)

faqs = [
    ("When is the best time to see birds at Pong Dam?", "November to February, with the peak in December and January. Most migratory birds leave by March."),
    ("How many birds come to Pong Dam?", "The forest department counted 92,885 migratory birds by December 2024, and earlier seasons have topped one lakh. More than 420 bird species have been recorded at the lake."),
    ("Is boating allowed at Pong Dam?", "Yes. The state water-sports centre at Khatiyar offers boating, kayaking, canoeing, sailing and rowing. We confirm what is running on your date before you go."),
    ("When can you see the Bathu ki Ladi temples?", "When the lake level drops, usually from about March to June. For the rest of the year the temples are under water."),
    ("Is Pong Dam a Ramsar site?", "Yes. Pong Dam Lake was declared a Ramsar wetland in 2002, the first in Himachal Pradesh, and it is also a wildlife sanctuary."),
    ("How far is Pong Dam from Dharamshala?", "About 55–65 km by road, roughly 1.5–2 hours. Kangra (Gaggal) airport is about 76 km away."),
    ("Are water sports open in the monsoon?", "No. Water sports in Kangra stop for the monsoon from 15 July to 15 September."),
    ("Is Pong Dam the same as Maharana Pratap Sagar?", "Yes. Maharana Pratap Sagar is the official name of the reservoir behind the Pong dam on the Beas, built in 1975."),
]
faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)

more = [
    ("/adventure/gobind-sagar-water-sports/", "🚤", "Gobind Sagar water sports", "Bhakra lake, Bilaspur"),
    ("/adventure/trout-fishing-in-himachal/", "🎣", "Trout fishing", "Rivers and lakes of Himachal"),
    ("/adventure/paragliding-in-bir-billing/", "🪂", "Paragliding in Bir Billing", "Kangra's famous flying site"),
    ("/adventure/paragliding-in-dharamshala/", "🪂", "Paragliding in Dharamshala", "Near McLeod Ganj"),
    ("/adventure/triund-trek/", "🥾", "Triund trek", "Above McLeod Ganj"),
    ("/adventure/", "🧭", "All adventures", "Air · Water · Snow · Land"),
]
more_html = "".join(f'<a class="sza-cat" href="{h}"><span class="ic">{i}</span><span class="n">{n}</span><span class="c">{c}</span></a>' for h, i, n, c in more)

reel = (HERE.parent / "media" / SLUG / "reel-section.html").read_text(encoding="utf-8").strip()

page = f'''<!-- pong-dam-bird-watching-water-sports — built by Page Builder (night) 4 Nov 2026 IST from the Research Lead brief 3 Nov + Visual Studio media @9a95df5 (reel-section @529111a). Kit v1.8. No prices, no operator names. Left off (unverified): jet skis / cruises / shikaras / floating decks, water-skiing, 2025-26 bird count, ABVIMAS exact location, fees, Chandigarh distance. Generic photos carry neutral alt text (never "Pong"). -->
<style>.sza-pdw .sza-hero-in>*{{max-width:620px}}.sza-pdw .sza-chips{{max-width:700px}}.sza-pdw .sza-media ul{{padding-left:20px;list-style:disc;margin:0}}.sza-pdw .sza-media ul li{{margin:0 0 8px}}.sza-pdw .sza-media img{{height:auto;aspect-ratio:3/2;object-fit:cover}}.sza-pdw .sza-media video{{height:auto;aspect-ratio:16/9}}.sza-pdw #spots .sza-grid{{grid-template-columns:repeat(auto-fit,minmax(min(300px,100%),1fr))}}.sza-pdw #spots .sza-card .img img{{aspect-ratio:3/2;object-fit:cover}}.sza-pdw .sza-checks{{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}@media(max-width:820px){{.sza-pdw .sza-hero video{{object-position:30% 50%}}.sza-pdw .sza-hero:after{{background:linear-gradient(180deg,rgba(11,31,51,.35) 0%,rgba(11,31,51,.6) 40%,rgba(11,31,51,.94) 100%)}}}}</style>
<div class="sza sza-pdw">
<section class="sza-hero">
<video autoplay muted loop playsinline preload="metadata" poster="{UP11}pong-dam-bird-watching-water-sports-hero-poster.webp" aria-label="A calm lake at dusk, a huge flock of geese, a small boat on still water and an old stone shrine at the water's edge, with a gold flight path of geese and the facts: migratory birds November to February, boating and kayaking, temples show March to June"><source src="{CDN}hero.webm" type="video/webm"><source src="{CDN}hero.mp4" type="video/mp4"></video>
<div class="sza-hero-in">
<span class="sza-kicker">Maharana Pratap Sagar · Kangra</span>
<p class="sza-hero-tag">Himachal's biggest bird lake — geese in winter, kayaks by day</p>
<p class="sza-hero-sub">Bird-watching at Nagrota Surian, boating and water sports at Khatiyar, and the half-sunk temples of Bathu ki Ladi.</p>
<ul class="sza-chips"><li><b>Ramsar</b> wetland</li><li><b>420+</b> bird species</li><li><b>Birds</b> Nov–Feb</li><li><b>~1.5 h</b> from Dharamshala</li><li><b>Water-sports</b> centre</li><li><b>Price</b> Get Quote</li></ul>
<div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan my trip</a></div>
<div class="sza-trust"><span><a href="https://suzutravels.com/certificates/">HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022</a></span><span>Lake day + hotel + cab</span><span>Reply within minutes</span></div>
</div>
</section>
<nav class="sza-nav" aria-label="On this page"><div class="sza-nav-in"><a href="#overview">Overview</a><a href="#spots">Where to go</a><a href="#experience">Your lake day</a><a href="#season">By month</a><a href="#safety">Rules &amp; safety</a><a href="#booking">How booking works</a><a href="#packages">Packages</a><a href="#faq">FAQ</a><a class="cta" href="{MAIN}" target="_blank" rel="noopener">Get Quote</a></div></nav>

<section class="sza-sec" id="overview">
<span class="sza-kicker">Quick answer</span>
<h2>Pong Dam Lake, at a glance</h2>
<p class="sza-answer">Pong Dam Lake (Maharana Pratap Sagar) is the large Beas reservoir in Kangra district, protected as a wildlife sanctuary and Himachal's first Ramsar wetland. Between November and February tens of thousands of migratory birds, led by bar-headed geese, winter here; the count by December 2024 alone passed 92,000. A state water-sports centre runs boating and paddle sports, and the Bathu ki Ladi temples rise from the water in spring and early summer.</p>
<div class="sza-facts"><div class="sza-fact"><div class="k">What</div><div class="v">Beas reservoir behind the Pong dam (built 1975); wildlife sanctuary; Ramsar site since 2002</div></div><div class="sza-fact"><div class="k">Birds</div><div class="v">420+ species recorded; peak Nov–Feb (bar-headed geese, ruddy shelduck, pintail, coots, cormorants)</div></div><div class="sza-fact"><div class="k">Bird spot</div><div class="v">Nagrota Surian, on the sanctuary shore</div></div><div class="sza-fact"><div class="k">On the water</div><div class="v">Boating, kayaking, canoeing, sailing and rowing at the Khatiyar water-sports centre; ABVIMAS courses at its Pong centre</div></div><div class="sza-fact"><div class="k">Getting there</div><div class="v">~55–65 km from Dharamshala; ~76 km from Kangra (Gaggal) airport</div></div><div class="sza-fact"><div class="k">Price</div><div class="v">Get Quote</div></div></div>
</section>

<section class="sza-sec alt" id="spots">
<span class="sza-kicker">Where to go</span>
<h2>Bird spots, boating points and the sunken temples</h2>
<p class="sza-lead">Birds at Nagrota Surian, boats at Khatiyar, temples at Bathu ki Ladi when the water is low. We check what is running for your date.</p>
<div class="sza-grid">{cards}</div>
</section>

<section class="sza-sec" id="experience">
<span class="sza-kicker">Your lake day</span>
<h2>How a Pong Dam day works</h2>
<ol class="sza-steps">{steps_exp}</ol>
<div class="sza-media"><video autoplay muted loop playsinline preload="none" poster="{UP11}pong-dam-bird-watching-water-sports-explainer-poster.webp" width="1600" height="900" aria-label="Motion graphic: one lake, three seasons. A 12-month strip shows birds from November to February, temples showing from March to June and no water sports from 15 July to 15 September; then a schematic from Dharamshala to Nagrota Surian for bird-watching and to Khatiyar for the water-sports centre, about 1.5 to 2 hours, life jacket on the water, price on quote"><source src="{CDN}explainer.webm" type="video/webm"><source src="{CDN}explainer.mp4" type="video/mp4"></video><div><h3>One lake, three seasons</h3><ul><li><b>Nov–Feb</b> → the birds are in.</li><li><b>Mar–Jun</b> → the water drops and the temples show.</li><li><b>15 Jul – 15 Sep</b> → no water sports in Kangra.</li><li><b>Birds or boats?</b> Nagrota Surian for birds, Khatiyar for the water.</li></ul><p>We check the week before we book.</p></div></div>
</section>

<section class="sza-sec alt" id="season">
<span class="sza-kicker">When to go</span>
<h2>Pong Dam by month</h2>
<div class="sza-scroll"><table class="sza-tbl"><thead><tr><th>Months</th><th>What's happening</th><th>Best for</th></tr></thead><tbody>{season_html}</tbody></table></div>
<p style="margin-top:14px">Bird-season weekends fill fastest. December and January mornings can be foggy — the drive is slower and boating may start late.</p>
</section>

<div class="sza-band" id="safety"><div class="sza-band-in">
<span class="sza-kicker">Rules &amp; safety</span>
<h2>What we check before we book your lake day</h2>
<p class="sza-lead">Suzu Travels is an <a href="https://suzutravels.com/certificates/" style="color:#f3d98f;text-decoration:underline">HP Tourism registered travel agent (Reg. No. DTO-MND-11-243/2022)</a>. We arrange water activities with registered local operators and check these first:</p>
<ul class="sza-checks"><li><b>Registered operators, life jackets on</b>Water activities only at the state centre or with registered operators, life jackets on at all times (HP water-sports rules).</li><li><b>Monsoon ban</b>Kangra stops water sports from 15 Jul to 15 Sep — nothing on the water in that window.</li><li><b>It is a sanctuary</b>Keep your distance from the flocks: no chasing birds by boat, no feeding, no loud music. Follow the forest staff.</li><li><b>Winter fog</b>Dec–Jan mornings can be foggy: slower drives, and boating may start late.</li><li><b>Bathu ki Ladi ground</b>The approach can be muddy and slippery, and the water returns with the monsoon — do not walk out on wet ground.</li><li><b>Sun and water</b>Shade is limited on the shore — carry sun protection and drinking water.</li></ul>
</div></div>

<section class="sza-sec" id="booking">
<span class="sza-kicker">How booking works</span>
<h2>Get a quote in minutes</h2>
<ol class="sza-steps">{booking}</ol>
<div class="sza-media"><img src="{UP10}wide-calm-lake-hills-dusk-768x432.webp" alt="Wide, calm lake reflecting a pink and gold dusk sky, with a low line of hills on the far shore" loading="lazy" width="768" height="432"><div><h3>What your quote depends on</h3><ul><li>Start city, and a day trip or a night near the lake</li><li>Season — bird-season weekends fill fastest</li><li>Which water activity and how long (or a multi-day course)</li><li>Group size and car type</li><li>Add-ons: guided bird-watching, binocular / camera help, Dharamshala, Bir or Triund days</li></ul><p>We send today's rate on WhatsApp within minutes.</p></div></div>
</section>

{reel}

<section class="sza-quote"><div><span class="sza-kicker">Birds or boats?</span><h2>Get your Pong Dam quote</h2><p>Tell us your date and who is coming. We reply with one plan — lake day, hotel and cab — within minutes.</p></div><div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan full trip</a></div></section>

<section class="sza-sec" id="packages">
<span class="sza-kicker">Make it a trip</span>
<h2>A Dharamshala + Pong Dam plan</h2>
<p>The easy way to do it: a <b>Dharamshala–McLeod Ganj 3N/4D trip with one Pong Dam day</b>, or a circuit <b>Amritsar / Pathankot → Pong Dam → Dharamshala → Bir</b>, with hotel and cab in one quote. In Dharamshala add the <a href="/adventure/triund-trek/">Triund trek</a> or the <a href="/adventure/kareri-lake-trek/">Kareri Lake trek</a>; in Bir, a <a href="/adventure/paragliding-in-bir-billing/">tandem paragliding flight</a>. Anglers: Pong is also in our <a href="/adventure/trout-fishing-in-himachal/">fishing guide</a>. Another big lake: <a href="/adventure/gobind-sagar-water-sports/">Gobind Sagar water sports</a> in Bilaspur.</p>
<div class="sza-btns" style="margin-top:18px">{walink("Dharamshala + Pong day — Get Quote", what="a Dharamshala–McLeod Ganj 3N/4D trip with a Pong Dam day (hotel + cab)")}{walink("Amritsar → Pong → Dharamshala → Bir — Get Quote", what="an Amritsar / Pathankot → Pong Dam → Dharamshala → Bir circuit (hotel + cab)", cls="sza-btn line")}</div>
</section>

<section class="sza-sec sza-faq" id="faq">
<span class="sza-kicker">FAQ</span>
<h2>Pong Dam Lake — questions</h2>
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
