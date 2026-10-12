#!/usr/bin/env python3
# Generates adventure-kit/pages/rafting-in-shimla-tattapani.html (Page Builder night, 13 Oct 2026)
import urllib.parse, pathlib
SLUG = "rafting-in-shimla-tattapani"
HERE = pathlib.Path(__file__).resolve().parent
CDN = "https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@a8111b6681cd97a2c8e424dcf41ca63e747ebb20/adventure-kit/media/rafting-in-shimla-tattapani/"
UP = "https://suzutravels.com/wp-content/uploads/2026/10/"
QUOTE = "/himachal-tour-packages-quote/?activity=" + urllib.parse.quote("Rafting at Tattapani")

def wa(activity, place="Tattapani near Shimla", tag=SLUG):
    t = f"Hi Suzu Travels, I want a quote for {activity}{' at ' + place if place else ''}. Travel date: ___ , people: ___ (page: {tag})"
    return "https://wa.me/917087488961?text=" + urllib.parse.quote(t, safe="")

def walink(activity, label, cls="sza-btn gold", place="Tattapani near Shimla"):
    return f'<a class="{cls}" href="{wa(activity, place)}" target="_blank" rel="noopener">{label}</a>'

MAIN = wa("river rafting")

def card(src, w, h, alt, badge, title, meta, text, act, place="Tattapani near Shimla", extra=""):
    return (f'<article class="sza-card"><div class="img"><img src="{src}" alt="{alt}" loading="lazy" width="{w}" height="{h}"><span class="sza-badge">{badge}</span></div>'
            f'<div class="body"><h3>{title}</h3><div class="meta">{meta}</div><p class="meta">{text}</p>'
            f'<div class="go">{extra}<a class="q" href="{wa(act, place)}" target="_blank" rel="noopener">Get Quote →</a></div></div></article>')

cards = "".join([
    card(f"{UP}raft-dropping-into-white-rapid-guide-standing-768x512.webp", 768, 512,
         "Guide standing at the back of a yellow raft as the crew in red helmets drops into a white rapid",
         "Rafting", "Satluj rafting", "<b>Tattapani</b> · since 2002",
         "A guided raft trip on the Satluj with a registered local operator — about 20 rafts run here. We confirm the river is running for your date.",
         "river rafting"),
    card(f"{UP}jet-ski-on-hill-lake-at-sunset-768x512.webp", 768, 512,
         "Jet ski cutting a white wake across a calm lake below green hills",
         "Still water", "Kol Dam lake water sports", "<b>Kol Dam reservoir</b>",
         "Jet ski, speed boat, bumper boat, banana ride, e-foil and water ski on the lake that formed in 2015.",
         "Kol Dam lake water sports"),
    card(f"{UP}steam-rising-over-hot-spring-pool-768x432.webp", 768, 432,
         "Steam rising over a warm natural pool on a cool morning",
         "Relax after", "Tattapani hot springs", "<b>Sulphur-rich springs</b>",
         "Soak after rafting. Tattapani's hot spring was inaugurated by President Rajendra Prasad in 1952.",
         "rafting with a hot springs visit"),
    card(f"{UP}cars-on-pine-forest-mountain-road-768x512.webp", 768, 512,
         "Cars driving along a winding mountain road through pine forest",
         "Day plan", "Shimla day trip", "<b>About 55 km each way</b>",
         "Leave Shimla in the morning, raft, ride and soak, and be back by evening in our cab.",
         "a Shimla day trip to Tattapani with rafting", place=None),
    card(f"{UP}wide-himalayan-river-valley-768x982.webp", 768, 982,
         "Wide river winding through a deep green Himalayan valley under a blue sky with white clouds",
         "Manali side", "Kullu rafting instead", "<b>Beas river</b> · Pirdi · Babeli · Raisan",
         "On a Manali trip? Raft the Beas in Kullu valley instead.",
         "river rafting", place="Kullu Manali",
         extra='<a class="x" href="/adventure/river-rafting-in-kullu-manali/">Kullu rafting →</a>'),
])

steps_exp = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Send your date", "Date, group size and ages on WhatsApp — we check rafting and water sports are running that day and book a registered local operator."),
    ("Drive to Tattapani", "Our cab picks you up in Shimla and drives about 55 km down to Tattapani."),
    ("Register &amp; gear up", "Register at the counter; the guide fits your life jacket and helmet and gives the safety talk."),
    ("Raft the Satluj", "Paddle the stretch with your guide; a rescue raft or kayak stays on the water."),
    ("Lake ride &amp; hot springs", "Change into dry clothes, try a lake ride if you want, then a soak at the hot springs."),
    ("Lunch &amp; head back", "Lunch, then the drive back to Shimla — or carry on towards Mandi and Manali."),
])

booking = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Tell us your date", "WhatsApp or the quote form — date, where you stay in Shimla, people and ages."),
    ("We check the river", "Water level, rain-day stops and which lake rides are running."),
    ("You get one quote", "Rafting, lake rides, cab and hotel in one plan."),
    ("Confirm and go", "We send the pickup time and a what-to-carry list before you travel."),
])

faqs = [
    ("Where is river rafting in Shimla?", "At Tattapani on the Satluj, about 55 km from Shimla, in the Karsog area of Mandi district. Shimla town itself has no river rafting."),
    ("Is rafting still on at Tattapani after Kol Dam?", "Yes. The Kol Dam reservoir (2015) turned part of the river into a lake, but rafting that started in 2002 still runs, with about 20 rafts (Dec 2024)."),
    ("What water sports are there at Tattapani?", "On the Kol Dam lake: jet ski, speed boat, bumper boat, banana ride, e-foil and water ski, plus ATV rides on the shore."),
    ("How far is Tattapani from Shimla?", "About 55 km, so rafting, a lake ride and the hot springs fit into one day."),
    ("Are the hot springs still there?", "Yes, Tattapani is known for its sulphur-rich hot springs; the original spring was inaugurated by President Rajendra Prasad in 1952."),
    ("Is it safe for beginners?", "Trips are guided; life jacket and helmet are compulsory and every rafting trip needs a rescue raft or kayak under HP rules."),
    ("When is the best time?", "October to June; monsoon months often see rain-day stops. We confirm the river is running before you go."),
    ("What does rafting at Tattapani cost?", f'It depends on the stretch, group, lake rides and cab from Shimla. Send your plan on <a href="{MAIN}" target="_blank" rel="noopener">WhatsApp</a> for today\'s rate — Price: Get Quote.'),
]
faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)

more = [
    ("/adventure/river-rafting-in-kullu-manali/", "🛶", "River rafting in Kullu Manali", "Beas · Pirdi · Babeli · Raisan"),
    ("/adventure/kufri-adventure-activities/", "🎢", "Kufri adventure activities", "Near Shimla"),
    ("/adventure/snow-kingdom-kufri/", "❄️", "Snow Kingdom Kufri", "Real snow, any month"),
    ("/adventure/ice-skating-shimla/", "⛸️", "Ice skating in Shimla", "Winter rink"),
    ("/adventure/paragliding-in-himachal/", "🪂", "Paragliding in Himachal", "Every site compared"),
    ("/adventure/", "🧭", "All adventures", "Air · Water · Snow · Land"),
]
more_html = "".join(f'<a class="sza-cat" href="{h}"><span class="ic">{i}</span><span class="n">{n}</span><span class="c">{c}</span></a>' for h, i, n, c in more)

reel = (HERE.parent / "media" / SLUG / "reel-section.html").read_text(encoding="utf-8").strip()

page = f'''<!-- rafting-in-shimla-tattapani — built by Page Builder (night) 13 Oct 2026 from the Research Lead (night) brief + Visual Studio (night) media @a8111b6 (reel-section @b22f82b). Kit v1.5. No prices, no operator names, nothing from the brief's unverified list (no stretches/km, grades, times, ages, monsoon ban dates, spring fees). Photos generic, neutral alt. Quote-form links carry ?activity=Rafting%20at%20Tattapani. -->
<style>.sza-tpn .sza-hero-in>*{{max-width:620px}}.sza-tpn .sza-chips{{max-width:700px}}.sza-tpn #experience .sza-steps{{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}.sza-tpn .sza-media ul{{padding-left:20px;list-style:disc;margin:0}}.sza-tpn .sza-media ul li{{margin:0 0 8px}}.sza-tpn .sza-media img{{aspect-ratio:4/3;object-fit:cover}}.sza-tpn #spots .sza-grid{{grid-template-columns:repeat(auto-fit,minmax(220px,1fr))}}.sza-tpn #spots .sza-card .img img{{aspect-ratio:3/2;object-fit:cover}}.sza-tpn .sza-checks{{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}.sza-tpn .sza-choose{{margin-top:32px}}.sza-tpn .go .x{{margin-right:14px}}@media(max-width:820px){{.sza-tpn .sza-hero video{{object-position:25% 50%}}.sza-tpn .sza-hero:after{{background:linear-gradient(180deg,rgba(11,31,51,.35) 0%,rgba(11,31,51,.6) 40%,rgba(11,31,51,.94) 100%)}}}}</style>
<div class="sza sza-tpn">
<section class="sza-hero">
<video autoplay muted loop playsinline preload="metadata" poster="{UP}rafting-shimla-tattapani-hero-poster.webp" aria-label="A raft dropping into a white rapid, a raft crew paddling, a jet ski on a hill lake and steam over a hot pool, with the words Raft the Satluj, 55 km from Shimla"><source src="{CDN}hero.webm" type="video/webm"><source src="{CDN}hero.mp4" type="video/mp4"></video>
<div class="sza-hero-in">
<span class="sza-kicker">Water · Satluj river · Tattapani, near Shimla</span>
<p class="sza-hero-tag">Raft the Satluj, then soak in Tattapani's hot springs</p>
<p class="sza-hero-sub">A one-day adventure from Shimla — rafting with registered local operators, lake water sports and the hot springs, with our cab and hotel.</p>
<ul class="sza-chips"><li><b>River</b> Satluj</li><li><b>Distance</b> 55 km from Shimla</li><li><b>Rafting</b> since 2002</li><li><b>Lake</b> Kol Dam water sports</li><li><b>Gear</b> Life jacket + helmet</li><li><b>Price</b> Get Quote</li></ul>
<div class="sza-btns">{walink("river rafting", "Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Add to my Shimla trip</a></div>
<div class="sza-trust"><span><a href="https://suzutravels.com/certificates/">HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022</a></span><span>Cab + hotel + rafting</span><span>Reply within minutes</span></div>
</div>
</section>
<nav class="sza-nav" aria-label="On this page"><div class="sza-nav-in"><a href="#overview">Overview</a><a href="#spots">What to do</a><a href="#experience">Your day</a><a href="#season">Season</a><a href="#safety">Safety</a><a href="#booking">How booking works</a><a href="#packages">Packages</a><a href="#faq">FAQ</a><a class="cta" href="{MAIN}" target="_blank" rel="noopener">Get Quote</a></div></nav>

<section class="sza-sec" id="overview">
<span class="sza-kicker">Quick answer</span>
<h2>River rafting in Shimla at a glance</h2>
<p class="sza-answer">River rafting near Shimla happens at Tattapani, on the Satluj about 55 km from Shimla, in Mandi district's Karsog area. Rafting started here in 2002 and about 20 rafts now run. Since the Kol Dam reservoir formed in 2015, Tattapani also has a lake with jet skis and speed boats, and the old sulphur hot springs. It all fits in one day from Shimla.</p>
<div class="sza-facts"><div class="sza-fact"><div class="k">River</div><div class="v">Satluj, Tattapani (Karsog, Mandi district — on the Shimla–Mandi border)</div></div><div class="sza-fact"><div class="k">Distance</div><div class="v">About 55 km from Shimla</div></div><div class="sza-fact"><div class="k">Rafting</div><div class="v">Running since 2002, about 20 rafts (Dec 2024)</div></div><div class="sza-fact"><div class="k">Lake water sports</div><div class="v">Jet ski, speed boat, bumper boat, banana ride, e-foil, water ski on the Kol Dam reservoir</div></div><div class="sza-fact"><div class="k">Safety gear</div><div class="v">Life jacket and helmet compulsory; trained guide in every raft</div></div><div class="sza-fact"><div class="k">Price</div><div class="v">Get Quote</div></div></div>
</section>

<section class="sza-sec alt" id="spots">
<span class="sza-kicker">What to do</span>
<h2>Rafting, lake rides and hot springs at Tattapani</h2>
<p class="sza-lead">Since the Kol Dam reservoir filled in 2015, Tattapani is part river, part lake — so one trip gives you white water on the Satluj, still-water rides on the lake and a soak in the hot springs. Photos show the activities in general, not Tattapani itself.</p>
<div class="sza-grid">{cards}</div>
<div class="sza-media sza-choose" id="day-plan"><video autoplay muted loop playsinline preload="none" poster="{UP}one-day-from-shimla-tattapani-explainer.webp" width="1600" height="900" aria-label="One day from Shimla: a road from Shimla 55 km to Tattapani with a cab, three stops for Satluj rafting, Kol Dam lake rides and hot springs, back in Shimla by evening; rafting since 2002 with about 20 rafts; life jacket and helmet, registered operators, price on quote"><source src="{CDN}explainer.webm" type="video/webm"><source src="{CDN}explainer.mp4" type="video/mp4"></video><div><h3>One day from Shimla</h3><ul><li><b>Morning</b> → our cab drives you about 55 km from Shimla down to Tattapani.</li><li><b>Rafting</b> → a guided run on the Satluj with a registered local operator.</li><li><b>Lake rides</b> → add a jet ski, speed boat or banana ride on the Kol Dam lake if you like.</li><li><b>Hot springs</b> → a warm soak before lunch.</li><li><b>Evening</b> → back in Shimla, or on towards Mandi and Manali.</li></ul></div></div>
</section>

<section class="sza-sec" id="experience">
<span class="sza-kicker">What happens</span>
<h2>Your Tattapani rafting day, step by step</h2>
<ol class="sza-steps">{steps_exp}</ol>
<div class="sza-media"><img src="{UP}blue-raft-team-paddling-through-rapid-768x512.webp" alt="Three rafters in helmets and life jackets paddling a blue raft through a brown rapid, seen from above" loading="lazy" width="768" height="512"><div><h3>No experience needed</h3><p>Trips are guided for first-timers. The guide steers and calls the strokes; you paddle and hold on through the rapids.</p><p>Wear quick-dry clothes and shoes that strap on, and carry a full change of clothes and a towel — you will get wet. Tell us about any health issue and the ages in your group when you book.</p></div></div>
</section>

<section class="sza-sec alt" id="season">
<span class="sza-kicker">When to go</span>
<h2>Best time for rafting at Tattapani</h2>
<div class="sza-scroll"><table class="sza-tbl"><thead><tr><th>Months</th><th>Rafting / water sports</th><th>What it's like</th></tr></thead><tbody><tr><td>Oct – Nov</td><td>Open on most days</td><td>Clear, falling water; pleasant days</td></tr><tr><td>Dec – Feb</td><td>Open on fair days</td><td>Cold water and cold mornings; hot springs at their best; we confirm the day</td></tr><tr><td>Mar – Jun</td><td>Open, peak</td><td>Warm valley, busiest weekends; book ahead</td></tr><tr><td>Jul – Sep (monsoon)</td><td>Often suspended</td><td>High, muddy water and rain-day stops; plan only after we confirm</td></tr></tbody></table></div>
<div class="sza-media" style="margin-top:28px"><img src="{UP}wide-himalayan-river-valley-768x982.webp" alt="Wide river winding through a deep green Himalayan valley under a blue sky with white clouds" loading="lazy" width="768" height="982"><div><h3>Coming in winter?</h3><p>December to February is cold on the water but the best time for the hot springs. Pair the day with <a href="/adventure/ice-skating-shimla/">ice skating in Shimla</a> or <a href="/adventure/snow-kingdom-kufri/">Snow Kingdom Kufri</a>, and read <a href="/shimla-in-december/">Shimla in December</a>.</p><p>On any day, rafting and lake rides can stop for rain or high water — we confirm before you drive down.</p></div></div>
</section>

<div class="sza-band" id="safety"><div class="sza-band-in">
<span class="sza-kicker">Safety first</span>
<h2>HP rules that apply at Tattapani</h2>
<p class="sza-lead">Suzu Travels is an <a href="https://suzutravels.com/certificates/" style="color:#f3d98f;text-decoration:underline">HP Tourism registered travel agent (Reg. No. DTO-MND-11-243/2022)</a>. We arrange rafting and lake rides with registered local operators and plan around these rules:</p>
<ul class="sza-checks"><li><b>Registered operators only</b>Rafting is run by operators registered with HP Tourism under the HP Tourism Development &amp; Registration Act 2002 and the HP River Rafting Rules 2005.</li><li><b>Life jacket + helmet, rescue backup</b>Both are compulsory, and every rafting trip needs rescue cover — two rescue rafts, or a raft plus a kayak (Rule 11(b), HP River Rafting Rules 2005).</li><li><b>Certified boat drivers</b>Lake rides fall under the HP Water Sports and Allied Activities Rules 2021: motor-boat and jet-ski drivers need a power-boat handling certificate from the National Institute of Water Sports.</li><li><b>Certified crews, every time</b>The HP High Court (Sep 2024) stopped one Kol Dam reservoir operator for an uncertified boat driver — another reason we book only registered operators with certified crews.</li><li><b>Rain days &amp; high water</b>No rafting or lake rides on rain-day suspensions or high water.</li><li><b>Kids &amp; seniors</b>Tell us the ages in your group; the guide decides on the day.</li></ul>
</div></div>

<section class="sza-sec" id="booking">
<span class="sza-kicker">How booking works</span>
<h2>Get a quote in minutes</h2>
<ol class="sza-steps">{booking}</ol>
<div class="sza-media"><img src="{UP}safety-kayaker-in-whitewater-768x511.webp" alt="Kayaker in a red helmet and blue jacket paddling a yellow kayak through white water" loading="lazy" width="768" height="511"><div><h3>What your quote depends on</h3><ul><li>Rafting stretch and length on the day</li><li>Number of people and date (weekends and May–June are busiest)</li><li>Lake rides added (jet ski, speed boat, banana ride…)</li><li>Photo / video add-on</li><li>Cab from Shimla (or Chandigarh) and waiting time; hot-spring entry</li><li>Hotel nights in Shimla and other activities (Kufri, ice skating in winter) — today's rate on WhatsApp within minutes</li></ul></div></div>
</section>

{reel}

<section class="sza-quote"><div><span class="sza-kicker">Ready to raft?</span><h2>Get your Tattapani rafting quote</h2><p>Tell us your travel date and group size. We reply with today's rate for your date within minutes — and can add your stay and cab.</p></div><div class="sza-btns">{walink("river rafting", "Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan full trip</a></div></section>

<section class="sza-sec" id="packages">
<span class="sza-kicker">Make it a trip</span>
<h2>Pair Tattapani rafting with a Shimla trip</h2>
<div class="sza-media"><img src="{UP}cars-on-pine-forest-mountain-road-768x512.webp" alt="Cars driving along a winding mountain road through pine forest" loading="lazy" width="768" height="512"><div><p>Tattapani is an easy day out from a Shimla stay: raft in the morning, soak in the hot springs and be back for dinner. Driving on to Manali? Tattapani works as a rafting stop on the way via Mandi.</p><p>Need only a cab? Book a <a href="/cabs/shimla-taxi-service/">Shimla taxi</a>, a <a href="/cabs/delhi-to-shimla-taxi/">Delhi to Shimla taxi</a> or a <a href="/cabs/chandigarh-to-shimla-taxi/">Chandigarh to Shimla taxi</a>.</p></div></div>
<div class="sza-btns" style="margin-top:18px">{walink("a Shimla 2-night trip with a Tattapani rafting day", "Shimla 2N + Tattapani rafting — Get Quote", place=None)}{walink("a Shimla to Tattapani to Manali road trip with a rafting stop", "Shimla → Tattapani → Manali road trip — Get Quote", cls="sza-btn line", place=None)}</div>
</section>

<section class="sza-sec sza-faq" id="faq">
<span class="sza-kicker">FAQ</span>
<h2>Rafting at Tattapani near Shimla — questions</h2>
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
