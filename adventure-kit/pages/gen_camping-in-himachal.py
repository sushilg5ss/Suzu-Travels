#!/usr/bin/env python3
# Generates adventure-kit/pages/camping-in-himachal.html (Page Builder night, 20 Oct 2026 IST)
import urllib.parse, pathlib
SLUG = "camping-in-himachal"
HERE = pathlib.Path(__file__).resolve().parent
CDN = "https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@6e3daab6d4d5aa1f3017af2b079773026e45be34/adventure-kit/media/camping-in-himachal/"
UP = "https://suzutravels.com/wp-content/uploads/2026/10/"
QUOTE = "/himachal-tour-packages-quote/?activity=" + urllib.parse.quote("Camping in Himachal")
WHAT = "camping in Himachal"

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
    card(f"{UP}tent-door-view-mountain-river-pine-forest-768x1186.webp", 768, 1186,
         "View from an open tent door over a fast mountain river and pine-covered slopes",
         "By the river", "Kasol, Parvati valley", "<b>Riverside camps · most of the year</b>",
         "Tents near the Parbati river below pine slopes; our Kasol guide covers the camp areas month by month.",
         "camping in Kasol", "/adventure/camping-in-kasol/"),
    card(f"{UP}lit-canvas-tent-pine-forest-night-768x512.webp", 768, 512,
         "A glowing canvas bell tent among tall pine trees under a starry night sky",
         "Quiet", "Jibhi–Tirthan (Banjar)", "<b>Forest &amp; stream camps</b>",
         "Forest camps in the valley that leads into the Great Himalayan National Park (UNESCO, 2014).",
         "camping in Jibhi and the Tirthan valley"),
    card(f"{UP}paraglider-over-green-fields-blue-sky-768x1156.webp", 768, 1156,
         "Paraglider with a yellow wing gliding down over green fields under a blue sky",
         "Pair with flying", "Bir (Kangra)", "<b>Camp + tandem flight</b>",
         "Camps near the paragliding landing area — pair a tent night with a tandem flight from Billing.",
         "camping in Bir with a paragliding flight", "/adventure/paragliding-in-bir-billing/"),
    card(f"{UP}lit-tents-snow-mountain-night-768x512.webp", 768, 512,
         "Two lit tents pitched on deep snow below a snow-covered mountain with pine trees, at night",
         "Snow side trip", "Manali–Solang", "<b>Camps Mar–Nov · snow day Dec–Feb</b>",
         "Camps on the edge of town and towards Solang; in winter sleep warm and add a snow day at Solang.",
         "camping in Manali", "/adventure/solang-valley-activities/"),
    card(f"{UP}dome-tents-hilltop-meadow-sunrise-768x498.webp", 768, 498,
         "Dome tents on a grassy hilltop meadow at sunrise with layered blue mountain ridges behind",
         "Easiest weekend", "Shimla–Kasauli hills", "<b>Closest to Chandigarh &amp; Delhi</b>",
         "Weekend forest and hilltop camps a short drive from Chandigarh — the easiest first camp.",
         "camping near Shimla or Kasauli"),
    card(f"{UP}chandratal-lake-reflection-lahaul-768x432.webp", 768, 432,
         "Chandratal Lake in Lahaul mirroring bare brown mountain slopes under a clear blue sky",
         "High &amp; seasonal", "Chandratal (Lahaul)", "<b>~4,250 m · Jun to early Oct</b>",
         "A Ramsar lake reached by road only from late May or June to early October; camps sit away from the lake.",
         "camping at Chandratal"),
])

trek = [
    ("/adventure/triund-trek/", "⛰️", "Triund Trek", "One night on the ridge"),
    ("/adventure/prashar-lake-trek/", "🏞️", "Prashar Lake Trek", "Snow camp in winter"),
    ("/adventure/kareri-lake-trek/", "💧", "Kareri Lake Trek", "Riverside camp halfway"),
    ("/adventure/hampta-pass-trek/", "🥾", "Hampta Pass Trek", "4–5 days, tents each night"),
]
trek_html = "".join(f'<a class="sza-cat" href="{h}"><span class="ic">{i}</span><span class="n">{n}</span><span class="c">{c}</span></a>' for h, i, n, c in trek)

steps_exp = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Send your plan", "Dates, group size and the area you like on WhatsApp — or just say “suggest one”."),
    ("We check the month", "Monsoon orders, snow and road status (Chandratal road, Atal Tunnel) for your exact dates."),
    ("We arrange a registered camp", "With a registered local operator — tent type, meals, bonfire where the camp allows it."),
    ("Hotel + cab added", "Your hotel nights and the cab from Delhi, Chandigarh or the airport in the same plan."),
    ("Camp day", "Drive in by afternoon, evening at the camp, a morning walk or an activity add-on."),
    ("Add-ons on request", "Paragliding at Bir, rafting near Kullu (Sep–Jun), the Triund or Kareri trek, a snow day at Solang."),
])

booking = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Tell us", "WhatsApp or the quote form — dates, group size, area and where you start from."),
    ("We check your date", "Season, monsoon orders, road status and a registered camp for that night."),
    ("You get one quote", "Camp night, hotel nights, cab and any activity in one plan."),
    ("Confirm and go", "We send the camp location, check-in time and what to pack."),
])

season = [
    ("Kasol / Parvati", "Open", "Avoid riverside — check orders", "Open", "Open, cold nights"),
    ("Jibhi–Tirthan", "Open", "Avoid stream banks", "Open", "Cold; some camps shut (ask)"),
    ("Bir", "Open", "Rain; flying stopped 15 Jul–15 Sep", "Open — best (flying season)", "Open, cold nights"),
    ("Manali–Solang", "Open", "Avoid riverside", "Open", "Snow; heated stays better (igloo/hotel)"),
    ("Shimla–Kasauli", "Open", "Open, rain", "Open", "Cold; snow spells"),
    ("Chandratal", "Closed until the road opens (late May)", "Open, rain/landslides on the way", "Open to early Oct", "Closed, lake frozen"),
]
season_html = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in season)

faqs = [
    ("Where can I go camping in Himachal?", "The main camp areas are Kasol in the Parvati valley, Jibhi–Tirthan, Bir, Manali–Solang, the hills near Shimla and Kasauli, and Chandratal in Lahaul in summer."),
    ("Is camping legal in Himachal Pradesh?", "Yes, at registered camps. Kullu officials shut 45 tourism units running without proper papers in Kasol in November 2024, so check the camp is registered — we book only those."),
    ("Can I camp by the river in monsoon?", "Avoid it. In July 2022 Kullu banned camps near rivers under the Disaster Management Act, and water sports stop 15 Jul–15 Sep every year. We check the current orders for your dates."),
    ("Can I camp at Chandratal?", "Only from late May or June to early October, when the road is open, and only at camps away from the lake — camping at the lake shore is not allowed. We check the current permit for your date."),
    ("Can I camp at Kheerganga?", "No — camping at the top is banned, so <a href=\"/adventure/kheerganga-trek/\">Kheerganga</a> is a day trek; stay in Kasol."),
    ("Which Himachal camp is best in winter?", "Lower camps such as Kasol, Bir and the Shimla side stay open with cold nights; for snow, add a day at Solang and sleep in a heated hotel or an <a href=\"/adventure/igloo-stay-manali/\">igloo stay</a>."),
    ("Which camp is closest to Delhi and Chandigarh?", "The forest and hilltop camps around Shimla and Kasauli — an easy weekend by road."),
    ("How much does camping in Himachal cost?", "It depends on the area, tent type, weekday or weekend, meals, group size and your cab. Send your dates on WhatsApp for today's rate within minutes — Price: Get Quote."),
]
faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)

more = [
    ("/adventure/camping-in-kasol/", "⛺", "Camping in Kasol", "Riverside camps, Parvati valley"),
    ("/adventure/kheerganga-trek/", "♨️", "Kheerganga Trek", "Hot spring day trek"),
    ("/adventure/paragliding-in-bir-billing/", "🪂", "Paragliding in Bir", "World-class tandem flights"),
    ("/adventure/adventure-activities-in-manali/", "🏔️", "Manali adventures", "What runs in your month"),
    ("/adventure/atal-tunnel-sissu-snow-trip/", "❄️", "Atal Tunnel &amp; Sissu", "Snow day from Manali"),
    ("/adventure/", "🧭", "All adventures", "Air · Water · Snow · Land"),
]
more_html = "".join(f'<a class="sza-cat" href="{h}"><span class="ic">{i}</span><span class="n">{n}</span><span class="c">{c}</span></a>' for h, i, n, c in more)

reel = (HERE.parent / "media" / SLUG / "reel-section.html").read_text(encoding="utf-8").strip()

page = f'''<!-- camping-in-himachal — built by Page Builder (night) 20 Oct 2026 IST from the Research Lead brief 19 Oct + Visual Studio media @6e3daab (reel-section @f51438b). Kit v1.8. No prices, no operator or camp names. Unverified items left off: 2026 Chandratal e-permit, exact camp distance from the lake, any 2026 riverside order, forest entry fee, Sissu camping. Generic photos carry neutral alt text; the Chandratal photo is the real lake. -->
<style>.sza-cih .sza-hero-in>*{{max-width:620px}}.sza-cih .sza-chips{{max-width:700px}}.sza-cih .sza-media ul{{padding-left:20px;list-style:disc;margin:0}}.sza-cih .sza-media ul li{{margin:0 0 8px}}.sza-cih .sza-media img{{height:auto;aspect-ratio:4/3;object-fit:cover}}.sza-cih .sza-media video{{height:auto;aspect-ratio:16/9}}.sza-cih #spots .sza-grid{{grid-template-columns:repeat(auto-fit,minmax(min(340px,100%),1fr))}}.sza-cih #spots .sza-card .img img{{aspect-ratio:3/2;object-fit:cover}}.sza-cih .sza-checks{{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}.sza-cih .sza-choose{{margin-top:32px}}.sza-cih .sza-treks{{margin-top:36px}}.sza-cih .sza-treks .sza-cats{{grid-template-columns:repeat(auto-fit,minmax(200px,1fr))}}@media(max-width:820px){{.sza-cih .sza-hero video{{object-position:30% 50%}}.sza-cih .sza-hero:after{{background:linear-gradient(180deg,rgba(11,31,51,.35) 0%,rgba(11,31,51,.6) 40%,rgba(11,31,51,.94) 100%)}}}}</style>
<div class="sza sza-cih">
<section class="sza-hero">
<video autoplay muted loop playsinline preload="metadata" poster="{UP}camping-in-himachal-hero-poster.webp" aria-label="Lit tents at dusk, a lit tent in a pine forest at night, dome tents on a hilltop at sunrise and Chandratal lake, with gold pins for six camping areas: Bir, Manali, Kasol, Jibhi, Shimla and Chandratal; registered camps only, Chandratal from June to early October"><source src="{CDN}hero.webm" type="video/webm"><source src="{CDN}hero.mp4" type="video/mp4"></video>
<div class="sza-hero-in">
<span class="sza-kicker">Treks &amp; Camps · Himachal Pradesh</span>
<p class="sza-hero-tag">Riverside, forest or high lake — pick your camp night</p>
<p class="sza-hero-sub">Six camping areas, what is open in your month, and the rules that matter — we add the camp to your hotel + cab plan.</p>
<ul class="sza-chips"><li><b>6</b> camping areas</li><li><b>Registered</b> camps only</li><li><b>Monsoon</b> no riverside camps</li><li><b>Chandratal</b> Jun–early Oct</li><li><b>Trek camps</b> 4 routes</li><li><b>Price</b> Get Quote</li></ul>
<div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan my trip</a></div>
<div class="sza-trust"><span><a href="https://suzutravels.com/certificates/">HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022</a></span><span>Camp + hotel + cab</span><span>Reply within minutes</span></div>
</div>
</section>
<nav class="sza-nav" aria-label="On this page"><div class="sza-nav-in"><a href="#overview">Overview</a><a href="#spots">Camp areas</a><a href="#experience">How it works</a><a href="#season">By month</a><a href="#safety">Rules &amp; safety</a><a href="#booking">How booking works</a><a href="#packages">Packages</a><a href="#faq">FAQ</a><a class="cta" href="{MAIN}" target="_blank" rel="noopener">Get Quote</a></div></nav>

<section class="sza-sec" id="overview">
<span class="sza-kicker">Quick answer</span>
<h2>Camping in Himachal, at a glance</h2>
<p class="sza-answer">Camping in Himachal means a night in a fixed tent camp near a river, forest or lake, or a tent on a trek. Kasol, Jibhi–Tirthan, Bir, Manali–Solang and the hills near Shimla and Kasauli run camps most of the year; Chandratal only from June to early October. Book only registered camps, and avoid riverbanks in monsoon, when Kullu has banned riverside camping before.</p>
<div class="sza-facts"><div class="sza-fact"><div class="k">Main areas</div><div class="v">Kasol (Parvati), Jibhi–Tirthan, Bir, Manali–Solang, Shimla–Kasauli, Chandratal</div></div><div class="sza-fact"><div class="k">Best months</div><div class="v">Mar–Jun and Sep–Nov; Dec–Feb only at lower camps (Kasol, Bir, Shimla side)</div></div><div class="sza-fact"><div class="k">Monsoon</div><div class="v">Jul–mid-Sep: avoid riverside camps — Kullu banned them under the DM Act in 2022</div></div><div class="sza-fact"><div class="k">Rules</div><div class="v">Registered camps only; a Nov 2024 drive shut 45 unregistered units in Kasol</div></div><div class="sza-fact"><div class="k">Trek camps</div><div class="v">Triund, Prashar, Kareri, Hampta — no camping at Kheerganga top</div></div><div class="sza-fact"><div class="k">Price</div><div class="v">Get Quote</div></div></div>
</section>

<section class="sza-sec alt" id="spots">
<span class="sza-kicker">Where to camp</span>
<h2>Six camping areas in Himachal</h2>
<p class="sza-lead">Pick by month and mood: riverside, pine forest, a camp under the paragliders, a snow-side stay or a high-altitude lake.</p>
<div class="sza-grid">{cards}</div>
<div class="sza-media sza-choose" id="camp-month"><video autoplay muted loop playsinline preload="none" poster="{UP}camping-in-himachal-explainer-poster.webp" width="1600" height="900" aria-label="Where can you camp this month: month pills Mar to Jun, Jul to mid-Sep, mid-Sep to Nov and Dec to Feb switch six area cards (Kasol, Jibhi–Tirthan, Bir, Manali–Solang, Shimla–Kasauli, Chandratal) between open, caution and closed; never camp on a riverbed, registered camps only"><source src="{CDN}explainer.webm" type="video/webm"><source src="{CDN}explainer.mp4" type="video/mp4"></video><div><h3>Where can you camp this month?</h3><ul><li><b>Mar–Jun</b> → all lower areas open; Chandratal opens with the road.</li><li><b>Jul–mid-Sep</b> → stay off riverbanks; Bir flying stops.</li><li><b>mid-Sep–Nov</b> → best overall; Chandratal till early Oct.</li><li><b>Dec–Feb</b> → Kasol, Bir, Shimla side; Chandratal closed.</li></ul></div></div>
<div class="sza-treks"><h3>Camp on a trek</h3><p>Want a tent on the trail instead? These treks include a camp night. One honest note: <a href="/adventure/kheerganga-trek/">Kheerganga</a> is day-trek only now — the night is in Kasol.</p><div class="sza-cats">{trek_html}</div></div>
</section>

<section class="sza-sec" id="experience">
<span class="sza-kicker">How it works</span>
<h2>How a camp night works with Suzu</h2>
<ol class="sza-steps">{steps_exp}</ol>
<div class="sza-media"><img src="{UP}lit-tents-meadow-campsite-dusk-768x512.webp" alt="Lit dome tents on a grassy campsite at dusk below a dark hill" loading="lazy" width="768" height="512"><div><h3>What a camp night looks like</h3><p>Dome or Swiss tents with bedding, dinner and breakfast, and a bonfire where the camp allows it. Riverside camps are in <a href="/adventure/camping-in-kasol/">Kasol</a>; forest camps in Jibhi–Tirthan — see our <a href="/jibhi-and-tirthan-valley-itinerary/">Jibhi and Tirthan itinerary</a>.</p><p>Carry a warm layer even in May, a torch and shoes with grip. Take all your waste back with you.</p></div></div>
</section>

<section class="sza-sec alt" id="season">
<span class="sza-kicker">When to go</span>
<h2>Camping in Himachal by month and area</h2>
<div class="sza-scroll"><table class="sza-tbl"><thead><tr><th>Area</th><th>Mar–Jun</th><th>Jul–mid-Sep</th><th>mid-Sep–Nov</th><th>Dec–Feb</th></tr></thead><tbody>{season_html}</tbody></table></div>
<p style="margin-top:14px">Planning New Year? The lower camps (Kasol, Bir, Shimla side) stay open with cold nights — book early for 31 December.</p>
</section>

<div class="sza-band" id="safety"><div class="sza-band-in">
<span class="sza-kicker">Rules &amp; safety</span>
<h2>What we check before we book your camp</h2>
<p class="sza-lead">Suzu Travels is an <a href="https://suzutravels.com/certificates/" style="color:#f3d98f;text-decoration:underline">HP Tourism registered travel agent (Reg. No. DTO-MND-11-243/2022)</a>. We arrange camps with registered local operators and plan around these checks:</p>
<ul class="sza-checks"><li><b>Registered camps only</b>A November 2024 joint inspection shut 45 tourism units running without proper papers in Kasol, camps included. We only book registered camps.</li><li><b>Monsoon riverside rule</b>On 6 July 2022 Kullu banned camps near rivers under the Disaster Management Act. Never camp on a riverbed or island — hydro projects release water without warning.</li><li><b>Forest rules</b>Kullu's 2022 forest order bans fixed camps on routes like Hampta and wants tents at least 25 m from rivers and water bodies — we use operator camps, not wild pitches.</li><li><b>Chandratal</b>No camping at the lake shore — it is a Ramsar wetland, and the lake is frozen in winter. We check the current permit for your date.</li><li><b>Kangra treks in winter</b>A November 2024 order needed SP Kangra permission for Triund and Kareri and stopped trekking above 3,000 m — expect a fresh order each winter.</li><li><b>Kheerganga &amp; bonfires</b>No camping at Kheerganga top — do it as a day trek. Bonfire only where the camp allows it; carry out all waste.</li></ul>
</div></div>

<section class="sza-sec" id="booking">
<span class="sza-kicker">How booking works</span>
<h2>Get a quote in minutes</h2>
<ol class="sza-steps">{booking}</ol>
<div class="sza-media"><img src="{UP}friends-campfire-hillside-sunset-768x1152.webp" alt="Group of friends in warm jackets sitting around a campfire on a hillside at sunset" loading="lazy" width="768" height="1152"><div><h3>What your quote depends on</h3><ul><li>Area and camp type — dome tent, Swiss tent, glamping or trek tent</li><li>Weekday or weekend; New Year and long weekends</li><li>Group size and tents needed (sharing)</li><li>Meals (dinner + breakfast or all meals) and bonfire</li><li>Add-on activity — paragliding, rafting, a trek or a snow day</li><li>Hotel nights before or after and the hotel category; cab from Delhi, Chandigarh or the airport, or self-drive</li></ul><p>We send today's rate on WhatsApp within minutes.</p></div></div>
</section>

{reel}

<section class="sza-quote"><div><span class="sza-kicker">Ready for a night under the stars?</span><h2>Get your Himachal camping quote</h2><p>Tell us your dates, group size and the area you like. We reply with one plan — camp night, hotel and cab — within minutes.</p></div><div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan full trip</a></div></section>

<section class="sza-sec" id="packages">
<span class="sza-kicker">Make it a trip</span>
<h2>Camp + fly, or Parvati + Jibhi</h2>
<p>Two easy ways to fit a camp in: <b>Camp + fly</b> — 3 nights at Bir (one camp night + hotel) with a tandem flight; or <b>Parvati + Jibhi</b> — 4 nights with a riverside camp near Kasol and a forest camp in Jibhi, with the cab from Delhi. Read our <a href="/kasol-trip-plan/">Kasol trip plan</a>, see <a href="/destination/shimla-tour-packages/">Shimla tour packages</a>, <a href="/destination/dharamshala-tour-packages/">Dharamshala tour packages</a> or <a href="/spiti-valley-tour-packages/">Spiti valley tour packages</a> (for Chandratal). Need only a cab? Book a <a href="/cabs/delhi-to-manali-taxi/">Delhi to Manali taxi</a>, a <a href="/cabs/chandigarh-to-manali-taxi/">Chandigarh to Manali taxi</a> or a <a href="/cabs/shimla-taxi-service/">Shimla taxi</a>.</p>
<div class="sza-btns" style="margin-top:18px">{walink("Camp + fly at Bir — Get Quote", what="a 3-night Bir trip with one camp night and a tandem paragliding flight")}{walink("Parvati + Jibhi camps — Get Quote", what="a 4-night Kasol riverside camp and Jibhi forest camp trip with cab from Delhi", cls="sza-btn line")}</div>
</section>

<section class="sza-sec sza-faq" id="faq">
<span class="sza-kicker">FAQ</span>
<h2>Camping in Himachal — questions</h2>
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
