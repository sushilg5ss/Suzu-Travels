#!/usr/bin/env python3
"""Generator for dharamshala-skyway.html — Page Builder (night) 19 Nov 2026.
Source: Research Lead brief 18 Nov (Project doc claude/adventure-research/briefs/dharamshala-skyway.md)
+ Visual Studio (night) media @b9a4e31 (Project doc claude/adventure-visual-studio/2026-11-19-night-dharamshala-skyway.md).
Model: gen_jakhu-ropeway-shimla.py. Run: python3 gen_dharamshala-skyway.py > dharamshala-skyway.html
"""
from urllib.parse import quote

SLUG = "dharamshala-skyway"
CDN = "https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@b9a4e31ce9367db800bc2a0105456bfeb2f348a4/adventure-kit/media/dharamshala-skyway/"
UP = "https://suzutravels.com/wp-content/uploads/"

def wa(what, tag=SLUG):
    t = f"Hi Suzu Travels, I want a quote for {what}. Travel date: ___ , people: ___ (page: {tag})"
    return "https://wa.me/917087488961?text=" + quote(t, safe="")

WA_MAIN = wa("the Dharamshala Skyway to McLeodganj")
QUOTE_FORM = "/himachal-tour-packages-quote/?activity=" + quote("Dharamshala Skyway", safe="")

def card(img, w, h, alt, badge, title, meta, text, what, explore=None, credit=None):
    ex = f'<a class="x" href="{explore}">Explore →</a>' if explore else ""
    cr = f'<p class="sza-credit">{credit}</p>' if credit else ""
    return f'''<article class="sza-card"><div class="img"><img src="{img}" alt="{alt}" loading="lazy" width="{w}" height="{h}"><span class="sza-badge">{badge}</span></div><div class="body"><h3>{title}</h3><div class="meta"><b>{meta}</b></div><p class="meta">{text}</p>{cr}<div class="go"><a class="q" href="{wa(what)}" target="_blank" rel="noopener">Get Quote →</a>{ex}</div></div></article>'''

CSS = """<style>.sza-dsk .sza-hero-in>*{max-width:620px}@media(min-width:901px){.sza-dsk .sza-hero-in>*{max-width:min(560px,44vw)}}.sza-dsk .sza-chips{max-width:700px}.sza-dsk .sza-media ul{padding-left:20px;list-style:disc;margin:0}.sza-dsk .sza-media ul li{margin:0 0 8px}.sza-dsk .sza-media img{height:auto;aspect-ratio:4/3;object-fit:cover}.sza-dsk .sza-media video{height:auto;aspect-ratio:16/9}.sza-dsk #spots .sza-grid{grid-template-columns:repeat(auto-fit,minmax(min(260px,100%),1fr))}.sza-dsk #spots .sza-card .img img{aspect-ratio:3/2;object-fit:cover}.sza-dsk .sza-checks{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}.sza-dsk .sza-choose{margin-top:32px}.sza-dsk #spots .sza-card:first-child .img img{object-position:50% 70%}.sza-dsk .sza-credit{font-size:12px;opacity:.75;margin:4px 0 0}@media(min-width:1000px){.sza-dsk #experience .sza-steps{grid-template-columns:repeat(3,1fr)}}@media(max-width:820px){.sza-dsk .sza-hero video{object-position:22% 50%}.sza-dsk .sza-hero:after{background:linear-gradient(180deg,rgba(11,31,51,.45) 0%,rgba(11,31,51,.68) 45%,rgba(11,31,51,.95) 100%)}}</style>"""

cards = "".join([
    card(UP+"2026/10/ropeway-red-cabin-pine-slope-683x1024.webp", 683, 1024,
         "Red cable car cabin on a ropeway crossing a steep pine forest slope", "Saves the hill drive",
         "Skyway one-way up", "~5 min · 1.8 km · cab meets you on top",
         "Stay in lower Dharamshala, ride up to McLeodganj in the morning, and your cab meets you at the top for the rest of the day.",
         "a one-way Dharamshala Skyway ride with a cab in McLeodganj"),
    card(UP+"2026/11/suzu-dharamshala-ghumne-ki-jagah-g-3-768x576.webp", 768, 576,
         "Tibetan temple on the main road of McLeodganj", "Day visitors",
         "Return ride", "Up and back the same day",
         "Ride up, walk to the Dalai Lama Temple and the McLeodganj market, then ride back down. Return tickets are sold at the counter.",
         "a return Dharamshala Skyway ride and McLeodganj sightseeing",
         credit="Photo: Adam Jones, CC BY-SA 2.0, Wikimedia Commons"),
    card(UP+"2026/11/suzu-dharamshala-snowfall-g-7-768x373.webp", 768, 373,
         "Walkers on the Triund ridge below snowy peaks", "Trekkers",
         "Skyway + Triund", "Early ride · trail from Galu Devi or Dharamkot",
         "Ride up early, then cab or walk to Galu Devi or Dharamkot for the Triund trail — saves the slow hill road on trek morning.",
         "the Dharamshala Skyway with the Triund trek", explore="/adventure/triund-trek/",
         credit="Photo: Aliya Tour Packages, CC BY-SA 4.0, Wikimedia Commons"),
    card(UP+"2026/10/paragliding-in-dharamshala-hero-poster-768x432.webp", 768, 432,
         "Green Dharamshala valley with a gold flight line from the Indrunag take-off down to the town", "Combo",
         "Skyway + paragliding", "McLeodganj morning · flight in the afternoon",
         "McLeodganj in the morning by Skyway, then a tandem flight from Indrunag in the afternoon (season and weather permitting).",
         "the Dharamshala Skyway with paragliding at Indrunag", explore="/adventure/paragliding-in-dharamshala/"),
])

def li(h, p): return f"<li><h3>{h}</h3><p>{p}</p></li>"

faqs = [
 ("How long is the Dharamshala Skyway?", "1.8 km, about five minutes, from Kotwali Bazaar in lower Dharamshala to Temple Road in McLeodganj, near the Dalai Lama Temple."),
 ("Is the Dharamshala ropeway open now?", "It was suspended after a landslide in August 2025 and riders report trips through 2026, but it pauses for weather and maintenance. We confirm the status for your date before you travel."),
 ("What are the Dharamshala ropeway timings?", "Daytime, roughly 9:30–10 am to 6–7 pm. Hours change with season and weather, so we check on the day."),
 ("Where is the lower station?", "Near Kotwali Bazaar on the bypass side of lower Dharamshala; a lift serves it. The upper station is on Temple Road, McLeodganj."),
 ("Can I buy a return ticket?", "Yes — one-way and return tickets are sold at the counter."),
 ("Is it the longest ropeway in Himachal?", "Yes. The Kangra district website lists it as the longest ropeway in Himachal Pradesh, with 18 gondolas on 10 towers."),
 ("When did the Dharamshala Skyway open?", "It was inaugurated on 19 January 2022."),
 ("How much does the Dharamshala Skyway cost?", "Get Quote — the fare depends on one-way or return, adults and children, and the date. WhatsApp your dates and we send one quote for hotel, cab and the day plan with the Skyway within minutes."),
]
faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)

def tile(href, ic, n, c): return f'<a class="sza-cat" href="{href}"><span class="ic">{ic}</span><span class="n">{n}</span><span class="c">{c}</span></a>'

html = f"""<!-- dharamshala-skyway — built by Page Builder (night) 19 Nov 2026 from the Research Lead brief 18 Nov + Visual Studio (night) media @b9a4e31. Kit v1.8. No prices, no operator names. Unverified items left off: this week's running status (page says we confirm for your date), exact hours, return-ticket validity, wheelchair access at the top. Generic photos carry neutral alt text; CC photos carry a credit line. -->
{CSS}
<div class="sza sza-dsk">
<section class="sza-hero">
<video autoplay muted loop playsinline preload="metadata" poster="{UP}2026/11/dharamshala-skyway-hero-poster.webp" aria-label="A red cable car cabin over a pine forest, the Dharamshala valley under the snowy Dhauladhar, prayer flags over a monastery roof and the Dhauladhar at golden hour, with a gold cable line from Dharamshala up to McLeodganj and a counter to 1.8 km">
<source src="{CDN}hero.webm" type="video/webm">
<source src="{CDN}hero.mp4" type="video/mp4">
</video>
<div class="sza-hero-in">
<span class="sza-kicker">Ropeways · Dharamshala → McLeodganj</span>
<p class="sza-hero-tag">Lower Dharamshala to the Dalai Lama Temple in five minutes</p>
<p class="sza-hero-sub">Himachal's longest ropeway skips the 9 km hill road. We check that week's running status and fit it into your Triund, cab and hotel plan.</p>
<ul class="sza-chips"><li><b>Cable</b> 1.8 km</li><li><b>Ride</b> ~5 min</li><li><b>Gondolas</b> 18</li><li><b>Towers</b> 10</li><li><b>Opened</b> Jan 2022</li><li><b>Price</b> Get Quote</li></ul>
<div class="sza-btns"><a class="sza-btn gold" href="{WA_MAIN}" target="_blank" rel="noopener">Get Quote on WhatsApp</a><a class="sza-btn ghost" href="{QUOTE_FORM}">Plan my Dharamshala trip</a></div>
<div class="sza-trust"><span><a href="https://suzutravels.com/certificates/">HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022</a></span><span>Skyway + hotel + cab</span><span>Reply within minutes</span></div>
</div>
</section>
<nav class="sza-nav" aria-label="On this page"><div class="sza-nav-in"><a href="#overview">Overview</a><a href="#spots">Ways to ride</a><a href="#experience">How it works</a><a href="#season">By month</a><a href="#safety">Safety</a><a href="#booking">How booking works</a><a href="#packages">Make it a trip</a><a href="#faq">FAQ</a><a class="cta" href="{WA_MAIN}" target="_blank" rel="noopener">Get Quote</a></div></nav>

<section class="sza-sec" id="overview">
<span class="sza-kicker">Quick answer</span>
<h2>Dharamshala Skyway, at a glance</h2>
<p class="sza-answer">The Dharamshala Skyway is a 1.8 km gondola from Kotwali Bazaar in lower Dharamshala to Temple Road in McLeodganj, near the Dalai Lama Temple. The ride takes about five minutes and replaces a 9 km hill drive. Opened in January 2022, it is Himachal's longest ropeway. It was suspended after a landslide in August 2025 and has run again since, but it stops in bad weather.</p>
<div class="sza-facts">
<div class="sza-fact"><div class="k">Route</div><div class="v">Lower station near Kotwali Bazaar, Dharamshala → upper station on Temple Road, McLeodganj</div></div>
<div class="sza-fact"><div class="k">Ride</div><div class="v">1.8 km in about 5 min; 18 gondolas on 10 towers</div></div>
<div class="sza-fact"><div class="k">Opened</div><div class="v">19 January 2022 — the longest ropeway in Himachal</div></div>
<div class="sza-fact"><div class="k">Hours</div><div class="v">Daytime, roughly 9:30–10 am to 6–7 pm — we confirm on your date</div></div>
<div class="sza-fact"><div class="k">Status</div><div class="v">Suspended 21 Aug 2025 after a landslide; riders report trips through 2026. It can pause for weather or maintenance — we check before you go</div></div>
<div class="sza-fact"><div class="k">Price</div><div class="v">Get Quote</div></div>
</div>
</section>

<section class="sza-sec alt" id="spots">
<span class="sza-kicker">Ways to ride</span>
<h2>Four ways to use the Skyway on your trip</h2>
<p class="sza-lead">One-way up saves the most time; a return ride suits day visitors. Trekkers and flyers can fold it into a Triund or paragliding day.</p>
<div class="sza-grid">{cards}</div>
<div class="sza-media sza-choose" id="skyway-or-road">
<video autoplay muted loop playsinline preload="none" poster="{UP}2026/11/dharamshala-skyway-or-hill-road-explainer-poster.webp" width="1600" height="900" aria-label="Skyway or the hill road: a gold cable on 10 towers from Kotwali Bazaar in lower Dharamshala to Temple Road, McLeodganj; Skyway about 5 minutes over 1.8 km with 18 gondolas; cab about 9 km on the winding hill road as backup; July to September monsoon pauses possible">
<source src="{CDN}explainer.webm" type="video/webm">
<source src="{CDN}explainer.mp4" type="video/mp4">
</video>
<div>
<h3>Skyway or the hill road?</h3>
<ul>
<li><b>Skyway</b> → ~5 min, 1.8 km over the pines; a lift serves the lower station.</li>
<li><b>Cab</b> → ~9 km winding hill road; our backup if the Skyway pauses.</li>
<li><b>Status</b> → we check weather and notices for your date first.</li>
<li><b>Jul–Sep</b> → heavy Kangra monsoon; pauses are possible.</li>
</ul>
</div>
</div>
</section>

<section class="sza-sec" id="experience">
<span class="sza-kicker">How it works</span>
<h2>Your Skyway ride with Suzu</h2>
<ol class="sza-steps">
{li("Tell us your plan", "Dharamshala dates and where you stay — lower Dharamshala, McLeodganj or Dharamkot.")}
{li("We check the status", "Skyway running status for that week: weather, district or maintenance notices.")}
{li("Drop at the lower station", "Your cab drops you near Kotwali Bazaar early in the day.")}
{li("Ticket and lift", "Buy a one-way or return ticket at the counter; a lift serves the lower station.")}
{li("Ride up to Temple Road", "About 5 minutes up — the Dalai Lama Temple (Tsuglagkhang) and McLeodganj market are a short walk.")}
{li("On with the day", "Your cab meets you on top, or ride back down; then Triund, Bhagsu or Naddi as planned.")}
</ol>
<div class="sza-media">
<img src="{UP}2026/10/dharamshala-river-valley-dhauladhar-snow-peaks-768x576.webp" alt="Dharamshala valley with a rocky stream, wooded hills and houses below the snow-capped Dhauladhar range" loading="lazy" width="768" height="576">
<div>
<h3>From Kotwali Bazaar to McLeodganj</h3>
<p>The lower station sits near Kotwali Bazaar on the bypass side of lower Dharamshala. The gondola climbs over the pine slopes with the Dhauladhar ahead, and the upper station opens onto Temple Road, McLeodganj. See what else to cover in town on our <a href="/dharamshala-tourist-places/">Dharamshala tourist places</a> guide and the <a href="/dharamshala-itinerary/">Dharamshala itinerary</a>.</p>
<p>For every other cable car in the state, see <a href="/adventure/ropeways-in-himachal/">ropeways in Himachal</a>.</p>
</div>
</div>
</section>

<section class="sza-sec alt" id="season">
<span class="sza-kicker">When to go</span>
<h2>Dharamshala Skyway by month</h2>
<div class="sza-scroll"><table class="sza-tbl"><thead><tr><th>Months</th><th>Skyway</th><th>What to expect</th></tr></thead><tbody>
<tr><td>Oct–Nov</td><td>Runs (check maintenance pauses)</td><td>Clear Dhauladhar views; short queues</td></tr>
<tr><td>Dec–Feb</td><td>Runs, weather allowing</td><td>Cold, clear mornings; snow on the Dhauladhar; storms can halt it</td></tr>
<tr><td>Mar–Jun</td><td>Runs</td><td>May–June busiest — go before 11 am</td></tr>
<tr><td>Jul–Sep</td><td>Weather-dependent</td><td>Heavy Kangra monsoon; landslide suspensions possible (as in Aug 2025)</td></tr>
</tbody></table></div>
<div class="sza-media" style="margin-top:32px">
<img src="{UP}2026/11/suzu-dharamshala-snowfall-g-5-768x509.webp" alt="Snow on rooftops and trees in McLeod Ganj" loading="lazy" width="768" height="509">
<div>
<h3>Going in winter?</h3>
<p>December–February brings snow to the Dhauladhar and, some years, to McLeodganj itself. Plan the ride for a clear morning — storms can halt it — and keep the road as backup. Pair it with a winter <a href="/adventure/triund-trek/">Triund trek</a> or a trip on to <a href="/adventure/things-to-do-in-bir-billing/">Bir Billing</a>.</p>
<p class="sza-credit">Photo: Derek Blackadder, CC BY-SA 2.0, Wikimedia Commons</p>
</div>
</div>
</section>

<div class="sza-band" id="safety"><div class="sza-band-in">
<span class="sza-kicker">Safety</span>
<h2>What we check before your ride</h2>
<p class="sza-lead">Suzu Travels is an <a href="https://suzutravels.com/certificates/" style="color:#f3d98f;text-decoration:underline">HP Tourism registered travel agent (Reg. No. DTO-MND-11-243/2022)</a>. We plan the Skyway into your Dharamshala day around these checks:</p>
<ul class="sza-checks">
<li><b>District orders</b>The Kangra district disaster management authority can suspend the ropeway at once — as on 21 August 2025, when a landslide came within about 10 feet of pillar 6. We re-check status on the morning of your ride.</li>
<li><b>Weather stops</b>Rides stop in storms, high wind or heavy rain — we keep the road drive as the backup for the same slot.</li>
<li><b>Capacity &amp; kids</b>Follow cabin capacity and staff instructions; children ride with an adult.</li>
<li><b>Monsoon</b>From mid-July to September expect pauses; we plan McLeodganj by road on those days.</li>
<li><b>Access</b>A lift serves the lower station — tell us about wheelchair users or elders and we confirm access at the top before planning.</li>
</ul>
</div></div>

<section class="sza-sec" id="booking">
<span class="sza-kicker">How booking works</span>
<h2>Get a quote in minutes</h2>
<ol class="sza-steps">
{li("Tell us", "WhatsApp or the quote form — Dharamshala dates, group size and where you start from.")}
{li("We check your date", "Skyway running status, weather and the road to McLeodganj.")}
{li("You get one quote", "Skyway day, McLeodganj sightseeing, Triund or paragliding add-ons, hotel nights and cab in one plan.")}
{li("Confirm and go", "We send the day plan, pick-up time and what to carry.")}
</ol>
<div class="sza-media">
<img src="{UP}2026/10/dhauladhar-snow-peaks-from-dharamshala-golden-light-768x576.webp" alt="Snow-capped Dhauladhar peaks lit gold above misty forested hills, seen from Dharamshala" loading="lazy" width="768" height="576">
<div>
<h3>What your quote depends on</h3>
<ul>
<li>One-way or return ride; number of adults and children</li>
<li>Date — weekends, Christmas–New Year, Dalai Lama teaching days and May–June are peak</li>
<li>Where the cab meets you (top or bottom) and the day plan — Triund, Bhagsu, Naddi, Kangra fort</li>
<li>Cab route — Chandigarh or Delhi to Dharamshala, Pathankot, or Kangra (Gaggal) airport pick-up</li>
<li>Hotel nights in Dharamshala, McLeodganj or Dharamkot and meal plan</li>
<li>Add-ons — Triund trek, paragliding at Indrunag, a Bir Billing day</li>
</ul>
<p>We send today's fare on WhatsApp within minutes.</p>
</div>
</div>
</section>

<section class="sza-sec" id="reel"><div style="display:flex;flex-wrap:wrap;align-items:center;gap:32px"><div style="flex:0 0 auto;width:min(300px,100%);margin:0 auto"><video poster="{UP}2026/11/dharamshala-skyway-reel-poster.webp" autoplay muted loop playsinline preload="metadata" width="300" height="533" style="display:block;width:100%;height:auto;aspect-ratio:9/16;border-radius:18px;background:#0b1f33;box-shadow:0 12px 32px rgba(11,31,51,.25)" aria-label="17-second reel: a cable car cabin over a pine forest, the Dharamshala valley under the snowy Dhauladhar, prayer flags over a monastery roof and the Dhauladhar peaks at golden hour; skip the 9 km hill road, board at Kotwali Bazaar, about 5 minutes and 1.8 km up to Temple Road, McLeodganj; it pauses in storms, so we check the status first"><source src="{CDN}reel-web.webm" type="video/webm"><source src="{CDN}reel-web.mp4" type="video/mp4"></video></div><div style="flex:1 1 320px;min-width:0"><span class="sza-kicker">Watch in 15 seconds</span><h2>Lower Dharamshala to McLeodganj in about five minutes</h2><p>Tell us your Dharamshala dates: we check that week's Skyway status, plan the ride for the morning and send one quote for the Skyway day, cab and hotel.</p><div class="sza-btns"><a class="sza-btn gold" href="https://wa.me/917087488961?text=Hi%20Suzu%20Travels%2C%20I%20want%20a%20quote%20for%20a%20Dharamshala%20trip%20with%20the%20Skyway%20to%20McLeodganj%20%28skyway%20%2B%20cab%20%2B%20hotel%29.%20Travel%20date%3A%20___%20%2C%20people%3A%20___%20%28page%3A%20dharamshala-skyway%20reel%29" target="_blank" rel="noopener">Get Quote on WhatsApp</a><a class="sza-btn" href="/adventure/triund-trek/" style="background:#fff;color:#0b1f33;border:2px solid #0b1f33">Add the Triund trek</a></div></div></div></section>

<section class="sza-quote"><div><span class="sza-kicker">Planning Dharamshala?</span><h2>Get your Skyway + Dharamshala quote</h2><p>Tell us your dates and group. We reply with one plan — Skyway day, McLeodganj, Triund, hotel and cab — within minutes.</p></div><div class="sza-btns"><a class="sza-btn gold" href="{WA_MAIN}" target="_blank" rel="noopener">Get Quote on WhatsApp</a><a class="sza-btn ghost" href="{QUOTE_FORM}">Plan full trip</a></div></section>

<section class="sza-sec" id="packages">
<span class="sza-kicker">Make it a trip</span>
<h2>Add the Skyway to your Dharamshala trip</h2>
<p>Most guests ride the Skyway on a 3-night Dharamshala–McLeodganj trip (Skyway + <a href="/adventure/triund-trek/">Triund</a>), a 4-night Dharamshala + Bir trip with <a href="/adventure/paragliding-in-bir-billing/">paragliding in Bir Billing</a>, or a 6-night Dalhousie–Dharamshala loop. See our <a href="/destination/dharamshala-tour-packages/">Dharamshala tour packages</a> and the <a href="/mcleodganj-tour-package/">McLeodganj tour package</a>. Coming by road? Book a <a href="/cabs/delhi-to-dharamshala-taxi/">Delhi to Dharamshala taxi</a>, a <a href="/cabs/chandigarh-to-dharamshala-taxi/">Chandigarh to Dharamshala taxi</a> or a <a href="/cabs/dharamshala-taxi-service/">Dharamshala taxi</a> for local sightseeing. Trekkers can also look at <a href="/adventure/kareri-lake-trek/">Kareri Lake</a> and <a href="/adventure/indrahar-pass-trek/">Indrahar Pass</a>.</p>
<div class="sza-btns" style="margin-top:18px"><a class="sza-btn gold" href="{wa('a 3-night Dharamshala–McLeodganj trip with the Skyway and Triund, hotel and cab')}" target="_blank" rel="noopener">Dharamshala 3N + Skyway — Get Quote</a><a class="sza-btn line" href="{wa('a 4-night Dharamshala and Bir trip with the Skyway, hotel and cab')}" target="_blank" rel="noopener">Dharamshala + Bir 4N — Get Quote</a></div>
</section>

<section class="sza-sec sza-faq" id="faq"><span class="sza-kicker">FAQ</span><h2>Dharamshala Skyway — questions</h2>{faq_html}</section>

<section class="sza-sec alt" id="more"><span class="sza-kicker">More adventures</span><h2>More around Dharamshala</h2><div class="sza-cats">
{tile("/adventure/ropeways-in-himachal/", "🚡", "Ropeways in Himachal", "Every cable car in the state")}
{tile("/adventure/triund-trek/", "🥾", "Triund trek", "The classic ridge above McLeodganj")}
{tile("/adventure/paragliding-in-dharamshala/", "🪂", "Paragliding in Dharamshala", "Tandem flights from Indrunag")}
{tile("/adventure/kareri-lake-trek/", "🏞️", "Kareri Lake trek", "Glacial lake in the Dhauladhar")}
{tile("/adventure/indrahar-pass-trek/", "⛰️", "Indrahar Pass trek", "Over the Dhauladhar")}
{tile("/adventure/things-to-do-in-bir-billing/", "🧭", "Things to do in Bir Billing", "Day trip from Dharamshala")}
</div></section>
</div>
"""
print(html)
