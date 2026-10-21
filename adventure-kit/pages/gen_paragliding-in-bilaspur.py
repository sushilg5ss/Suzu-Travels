#!/usr/bin/env python3
# Generates adventure-kit/pages/paragliding-in-bilaspur.html (Page Builder night, 15 Oct 2026)
import urllib.parse, pathlib
SLUG = "paragliding-in-bilaspur"
HERE = pathlib.Path(__file__).resolve().parent
CDN = "https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@42b05458773c70452c027435a817a971c15c1a2d/adventure-kit/media/paragliding-in-bilaspur/"
UP = "https://suzutravels.com/wp-content/uploads/2026/10/"
ND = "https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@6822fc9d05cc90f0b590fc45b676143b22bc6988/pilgrim-kit/media/naina-devi/hero-poster.webp"
QUOTE = "/himachal-tour-packages-quote/?activity=" + urllib.parse.quote("Paragliding")

def wa(what="tandem paragliding in Bilaspur (Bandla Dhar)", tag=SLUG):
    t = f"Hi Suzu Travels, I want a quote for {what}. Travel date: ___ , people: ___ (page: {tag})"
    return "https://wa.me/917087488961?text=" + urllib.parse.quote(t, safe="")

def walink(label, what="tandem paragliding in Bilaspur (Bandla Dhar)", cls="sza-btn gold"):
    return f'<a class="{cls}" href="{wa(what)}" target="_blank" rel="noopener">{label}</a>'

MAIN = wa()

def card(src, w, h, alt, badge, title, meta, text, what, extra="", cls=""):
    return (f'<article class="sza-card{cls}"><div class="img"><img src="{src}" alt="{alt}" loading="lazy" width="{w}" height="{h}"><span class="sza-badge">{badge}</span></div>'
            f'<div class="body"><h3>{title}</h3><div class="meta">{meta}</div><p class="meta">{text}</p>'
            f'<div class="go">{extra}<a class="q" href="{wa(what)}" target="_blank" rel="noopener">Get Quote →</a></div></div></article>')

cards = "".join([
    card(f"{UP}tandem-paraglider-over-lake-hazy-mountains-768x1152.webp", 768, 1152,
         "Tandem paraglider with an orange wing flying high above a long lake between hazy blue mountains",
         "Classic pick", "Bandla tandem joyride", "<b>Bandla Dhar → Luhnu</b> · tandem",
         "A tandem flight from the ridge above Bilaspur town down to the Luhnu ground on the Gobind Sagar shore.",
         "a Bandla tandem joyride in Bilaspur"),
    card(f"{UP}tandem-paragliding-pilot-and-passenger-in-flight-768x569.webp", 768, 569,
         "Tandem paragliding selfie: passenger in front and pilot behind, both in helmets, flying high above forested hills",
         "Add-on", "Tandem + flight video", "<b>Same flight, on camera</b>",
         "Ask for a helmet or hand-camera clip of your flight when you book.",
         "a Bandla tandem flight with video"),
    card(f"{UP}speed-boat-white-wake-lake-from-above-768x1227.webp", 768, 1227,
         "Speed boat seen from above cutting a long white wake across dark blue water",
         "Same day", "Fly + Gobind Sagar water sports", "<b>After you land by the lake</b>",
         "Speed boat, water scooter or a lake cruise, run by the district society — season permitting.",
         "a Bandla flight plus Gobind Sagar water sports"),
    card(ND, 1600, 900,
         "Illustration of the Shri Naina Devi Ji temple on a Shivalik hilltop at dusk",
         "Pilgrim combo", "Naina Devi + Bandla day", "<b>Same district</b>",
         "Morning darshan at Naina Devi, afternoon flight at Bandla, night in Bilaspur.",
         "Naina Devi darshan plus a Bandla flight",
         extra='<a class="x" href="/pilgrimage-tours/naina-devi/">Naina Devi →</a>', cls=" nd"),
    card(f"{UP}tandem-pilot-passenger-ready-hilltop-above-town-768x576.webp", 768, 576,
         "Tandem paragliding pilot and passenger in helmets and harnesses standing on a grassy hilltop take-off, looking over a green valley and town",
         "Road trip", "Halt on the Manali road", "<b>Chandigarh → Bilaspur → Manali</b>",
         "Break the long drive at Bilaspur, fly next morning, then carry on to Manali.",
         "a Chandigarh to Manali road trip with a Bandla flight",
         extra='<a class="x" href="/cabs/chandigarh-to-manali-taxi/">Chandigarh–Manali cab →</a>'),
])

steps_exp = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Send your date", "Date, group size and weights on WhatsApp — we confirm the day's flying with a registered local operator."),
    ("Up to Bandla Dhar", "Our cab drives you up from Bilaspur town or your hotel."),
    ("Check &amp; briefing", "Weight check, harness and helmet fitting, short safety briefing from the pilot."),
    ("Take-off run", "A short run down the grassy take-off slope with the pilot behind you."),
    ("The glide", "Over Bilaspur town and the lake — the pilot handles every turn."),
    ("Land by the lake", "Touch down at Luhnu by Gobind Sagar; your cab waits there. Add a boat ride or drive on."),
])

booking = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Tell us your date", "WhatsApp or the quote form — date, people, ages, weights and where you are coming from."),
    ("We check the day", "Flying, weather and limits with a registered local operator."),
    ("You get one quote", "Flight, video if you want it, cab, hotel and Naina Devi or lake add-ons in one plan."),
    ("Confirm and go", "We send the reporting time and what to wear before you travel."),
])

faqs = [
    ("Where is paragliding in Bilaspur?", "At Bandla Dhar, the hill right above Bilaspur town. You land on the Luhnu ground beside Gobind Sagar lake."),
    ("Is Bandla a real paragliding site?", "Yes. The Bilaspur district administration names Bandla top as the take-off with Luhnu as the landing, and the site hosted an international paragliding championship with 70+ pilots in March 2025."),
    ("When can I fly at Bandla?", "Outside the monsoon. The district flagged off the 2025-26 season on 28–29 Sep 2025; we confirm the day's flying before you travel."),
    ("Who can fly tandem?", "Anyone 12 years or older and at least 30 kg, under the HP Aero Sports Rules. No licence is needed for a tandem flight."),
    ("What does paragliding in Bilaspur cost?", f'The rate depends on flight type, video and your date. Send your plan on <a href="{MAIN}" target="_blank" rel="noopener">WhatsApp</a> and we share today\'s rate within minutes — Price: Get Quote.'),
    ("Can I combine it with Naina Devi?", 'Yes. <a href="/pilgrimage-tours/naina-devi/">Naina Devi</a> is in the same district; many guests do darshan in the morning and fly in the afternoon.'),
    ("What else is there at Gobind Sagar?", "The district runs speed boat, water scooter, banana and cruise rides on the lake in season."),
    ("Bandla or Bir Billing?", 'Bir is the big, high Kangra site; Bandla is closer to Chandigarh and the Manali highway and lands by a lake. See our <a href="/adventure/paragliding-in-himachal/">paragliding in Himachal comparison</a>.'),
]
faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)

more = [
    ("/adventure/paragliding-in-himachal/", "🧭", "Paragliding in Himachal", "Every site compared"),
    ("/adventure/paragliding-in-bir-billing/", "🪂", "Paragliding in Bir Billing", "The big Kangra site"),
    ("/adventure/paragliding-in-manali/", "🏔️", "Paragliding in Manali", "Solang &amp; Dobhi"),
    ("/pilgrimage-tours/nau-devi-yatra/", "🛕", "Nau Devi Yatra", "Naina Devi &amp; more"),
    ("/pilgrimage-tours/shakti-peeth-himachal/", "🙏", "Shakti Peeths of Himachal", "Temple circuit"),
    ("/adventure/", "⛰️", "All adventures", "Air · Water · Snow · Land"),
]
more_html = "".join(f'<a class="sza-cat" href="{h}"><span class="ic">{i}</span><span class="n">{n}</span><span class="c">{c}</span></a>' for h, i, n, c in more)

reel = (HERE.parent / "media" / SLUG / "reel-section.html").read_text(encoding="utf-8").strip()

page = f'''<!-- paragliding-in-bilaspur — built by Page Builder (night) 15 Oct 2026 from the Research Lead brief (12 Oct) + Visual Studio (night) media @42b0545 (reel-section @76b10e8). Kit v1.5. No prices, no operator names; no altitudes, flight minutes or distances (unverified); 2026-27 season shown as "we confirm"; monsoon closure without exact dates. Photos generic, neutral alt (never labelled Bandla / Gobind Sagar). Naina Devi card uses the Pilgrim squad's own illustration. Quote-form links carry ?activity=Paragliding. -->
<style>.sza-bls .sza-hero-in>*{{max-width:620px}}.sza-bls .sza-chips{{max-width:700px}}.sza-bls #experience .sza-steps{{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}.sza-bls .sza-media ul{{padding-left:20px;list-style:disc;margin:0}}.sza-bls .sza-media ul li{{margin:0 0 8px}}.sza-bls .sza-media img{{height:auto;aspect-ratio:4/3;object-fit:cover}}.sza-bls .sza-media video{{height:auto;aspect-ratio:16/9}}.sza-bls #spots .sza-grid{{grid-template-columns:repeat(auto-fit,minmax(220px,1fr))}}.sza-bls #spots .sza-card .img img{{aspect-ratio:3/2;object-fit:cover}}.sza-bls #spots .sza-card.nd .img img{{object-position:20% 50%}}.sza-bls .sza-checks{{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}.sza-bls .sza-choose{{margin-top:32px}}.sza-bls .go .x{{margin-right:14px}}@media(max-width:820px){{.sza-bls .sza-hero video{{object-position:30% 50%}}.sza-bls .sza-hero:after{{background:linear-gradient(180deg,rgba(11,31,51,.35) 0%,rgba(11,31,51,.6) 40%,rgba(11,31,51,.94) 100%)}}}}</style>
<div class="sza sza-bls">
<section class="sza-hero">
<video autoplay muted loop playsinline preload="metadata" poster="{UP}paragliding-in-bilaspur-hero-poster.webp" aria-label="A paraglider over a forested ridge and wide blue water, a tandem pair ready on a hilltop above a town and a tandem flight over a long lake, with a gold flight line from the Bandla Dhar take-off over Bilaspur town to the Luhnu landing by Gobind Sagar"><source src="{CDN}hero.webm" type="video/webm"><source src="{CDN}hero.mp4" type="video/mp4"></video>
<div class="sza-hero-in">
<span class="sza-kicker">Air · Bilaspur · near our office</span>
<p class="sza-hero-tag">Take off above Bilaspur, land beside Gobind Sagar lake</p>
<p class="sza-hero-sub">Tandem flights from Bandla Dhar with a registered pilot — we add the flight to your hotel, cab and Naina Devi plan.</p>
<ul class="sza-chips"><li><b>Take-off</b> Bandla Dhar</li><li><b>Landing</b> Luhnu, Gobind Sagar</li><li><b>Tandem</b> Registered pilot</li><li><b>Age</b> 12+ · 30 kg+</li><li><b>Monsoon</b> Closed</li><li><b>Price</b> Get Quote</li></ul>
<div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Add to my trip</a></div>
<div class="sza-trust"><span><a href="https://suzutravels.com/certificates/">HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022</a></span><span>Cab + hotel + activities</span><span>Reply within minutes</span></div>
</div>
</section>
<nav class="sza-nav" aria-label="On this page"><div class="sza-nav-in"><a href="#overview">Overview</a><a href="#spots">Options</a><a href="#experience">Your flight</a><a href="#season">Season</a><a href="#safety">Safety</a><a href="#booking">How booking works</a><a href="#packages">Packages</a><a href="#faq">FAQ</a><a class="cta" href="{MAIN}" target="_blank" rel="noopener">Get Quote</a></div></nav>

<section class="sza-sec" id="overview">
<span class="sza-kicker">Quick answer</span>
<h2>Paragliding in Bilaspur at a glance</h2>
<p class="sza-answer">Paragliding in Bilaspur happens at Bandla Dhar, the ridge right above Bilaspur town. You fly tandem with a registered pilot and land on the Luhnu ground beside Gobind Sagar lake. The site hosted an international championship in March 2025 and flying restarted with the district on 28–29 Sep 2025. Flights stop in the monsoon; passengers must be 12+ and 30 kg+.</p>
<div class="sza-facts"><div class="sza-fact"><div class="k">Where</div><div class="v">Bandla Dhar (Bandla hill) above Bilaspur town, Bilaspur district</div></div><div class="sza-fact"><div class="k">Landing</div><div class="v">Luhnu ground on the bank of Gobind Sagar lake</div></div><div class="sza-fact"><div class="k">Type</div><div class="v">Tandem flight with a registered pilot (solo only for licensed pilots)</div></div><div class="sza-fact"><div class="k">Who can fly</div><div class="v">12 years+ and 30 kg+ (HP Aero Sports Rules)</div></div><div class="sza-fact"><div class="k">Season</div><div class="v">Autumn to spring; no flying in the monsoon</div></div><div class="sza-fact"><div class="k">Price</div><div class="v">Get Quote</div></div></div>
</section>

<section class="sza-sec alt" id="spots">
<span class="sza-kicker">Your options</span>
<h2>Ways to fly at Bandla</h2>
<p class="sza-lead">One site, five easy ways to fit it into your trip. Photos show paragliding and boating in general, not Bandla or Gobind Sagar themselves.</p>
<div class="sza-grid">{cards}</div>
<div class="sza-media sza-choose" id="flight"><video autoplay muted loop playsinline preload="none" poster="{UP}your-bandla-flight-paragliding-explainer.webp" width="1600" height="900" aria-label="Your Bandla flight: side profile with the take-off on Bandla Dhar, a gold flight line over Bilaspur town to the Luhnu landing by Gobind Sagar; month bar with the flying season, fair-weather months and the monsoon closure; 12+ years and 30 kg+, tandem with a registered pilot, price on quote"><source src="{CDN}explainer.webm" type="video/webm"><source src="{CDN}explainer.mp4" type="video/mp4"></video><div><h3>Your Bandla flight</h3><ul><li><b>Take off</b> → Bandla Dhar, the ridge above town.</li><li><b>Glide</b> → over Bilaspur town and the lake.</li><li><b>Land</b> → Luhnu ground by Gobind Sagar.</li><li><b>Monsoon</b> → closed; the district reopens the season.</li></ul></div></div>
</section>

<section class="sza-sec" id="experience">
<span class="sza-kicker">What happens</span>
<h2>Your Bandla flight, step by step</h2>
<ol class="sza-steps">{steps_exp}</ol>
<div class="sza-media"><img src="{UP}paraglider-wing-inflating-grassy-field-take-off-768x1152.webp" alt="Blue paraglider wing inflating above a pilot on a sunny grassy field, the moment before take-off" loading="lazy" width="768" height="1152"><div><h3>First flight? That's normal</h3><p>No licence or experience is needed for a tandem flight. The pilot clips you in, explains the run and does all the flying; you just run a few steps and sit back.</p><p>Wear closed shoes and a light jacket, tie long hair back and keep phones in a zipped pocket. Tell us the ages and weights in your group when you book.</p></div></div>
</section>

<section class="sza-sec alt" id="season">
<span class="sza-kicker">When to go</span>
<h2>Best time for paragliding in Bilaspur</h2>
<div class="sza-scroll"><table class="sza-tbl"><thead><tr><th>Months</th><th>Flying</th><th>What it's like</th></tr></thead><tbody><tr><td>Oct – Nov</td><td>Open (weather permitting)</td><td>Clear post-monsoon air, comfortable temperatures</td></tr><tr><td>Dec – Feb</td><td>Open on fair days</td><td>Mild valley winter; good when Manali and Bir are cold</td></tr><tr><td>Mar – Apr</td><td>Open</td><td>Spring season; Bandla hosted the March 2025 championship</td></tr><tr><td>May – Jun</td><td>Open, hot afternoons</td><td>Fly early; check the day's wind</td></tr><tr><td>Monsoon (Jul – Sep)</td><td>Closed</td><td>The district suspends adventure sports in the monsoon</td></tr></tbody></table></div>
</section>

<div class="sza-band" id="safety"><div class="sza-band-in">
<span class="sza-kicker">Safety first</span>
<h2>What we check before we book your flight</h2>
<p class="sza-lead">Suzu Travels is an <a href="https://suzutravels.com/certificates/" style="color:#f3d98f;text-decoration:underline">HP Tourism registered travel agent (Reg. No. DTO-MND-11-243/2022)</a>. We arrange flights only with registered local operators and plan around these checks:</p>
<ul class="sza-checks"><li><b>Registered pilot only</b>Pilot and operator registered with HP Tourism; tandem pilots hold a valid licence and logbook (HP Aero Sports Rules 2022, amended 2025).</li><li><b>Age and weight</b>Passengers under 12 years or under 30 kg are not allowed.</li><li><b>Notified site</b>Take off only from the notified Bandla site, never from a random ridge.</li><li><b>Gear on</b>Helmet, harness and reserve parachute are fitted before take-off — ask the pilot to show them.</li><li><b>Pilot's weather call</b>Strong wind or cloud means no flight that hour; we keep a buffer in your plan.</li><li><b>Monsoon closure</b>No flying during the monsoon suspension; the district reopens the season by order.</li></ul>
</div></div>

<section class="sza-sec" id="booking">
<span class="sza-kicker">How booking works</span>
<h2>Get a quote in minutes</h2>
<ol class="sza-steps">{booking}</ol>
<div class="sza-media"><img src="{UP}paraglider-forested-ridge-wide-blue-water-768x512.webp" alt="Paraglider with a green, yellow and red wing gliding past a forested ridge above wide blue water under a clear sky" loading="lazy" width="768" height="512"><div><h3>What your quote depends on</h3><ul><li>Joyride or a longer flight</li><li>Video add-on</li><li>Number of flyers and the date (weekends and holidays are busier)</li><li>Pickup point: Bilaspur town, your hotel, Naina Devi or Ghumarwin</li><li>Hotel nights, cab and a Gobind Sagar boat add-on — today's rate on WhatsApp within minutes</li></ul></div></div>
</section>

{reel}

<section class="sza-quote"><div><span class="sza-kicker">Ready to fly?</span><h2>Get your Bandla flight quote</h2><p>Tell us your travel date and group size. We reply with today's rate for your date within minutes — and can add your stay, cab and Naina Devi darshan.</p></div><div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan full trip</a></div></section>

<section class="sza-sec alt" id="lake-combo"><span class="sza-kicker">Same-day combo</span><h2>Fly Bandla, then get on the water</h2><div class="sza-media sza-choose" id="lake-ride"><video autoplay muted loop playsinline preload="none" poster="https://suzutravels.com/wp-content/uploads/2026/10/gobind-sagar-fly-bandla-then-boat-explainer.webp" width="1600" height="900" style="display:block;width:100%;height:auto;aspect-ratio:16/9" aria-label="Motion graphic: Gobind Sagar water level by month, high from August to January for boat rides and jet skis, low from February to June when old temples show; then a gold paragliding line from the Bandla Dhar take-off to the Luhnu landing and water-sports base, and a boat heading to the Mandi Bharari boating jetty; 28 temples went under, life jacket for every rider, price on quote"><source src="https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@11e39fce3c679fd7decbe9f7b5abfe36ab7dcfa9/adventure-kit/media/gobind-sagar-water-sports/explainer.webm" type="video/webm"><source src="https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@11e39fce3c679fd7decbe9f7b5abfe36ab7dcfa9/adventure-kit/media/gobind-sagar-water-sports/explainer.mp4" type="video/mp4"></video><div><h3>The lake below your flight</h3><ul><li><b>Land</b> → Luhnu ground, right on the Gobind Sagar shore.</li><li><b>Ride</b> → boat rides and jet skis; the main jetty is at Mandi Bharari.</li><li><b>Best water</b> → August to January, when the lake is high.</li><li><b>Safety</b> → a life jacket for every rider (DC Bilaspur order, 2026).</li></ul><div class="sza-btns"><a class="sza-btn gold" href="https://wa.me/917087488961?text=Hi%20Suzu%20Travels%2C%20I%20want%20a%20quote%20for%20a%20Bandla%20flight%20plus%20a%20Gobind%20Sagar%20boat%20ride.%20Travel%20date%3A%20___%20%2C%20people%3A%20___%20%28page%3A%20paragliding-in-bilaspur%20lake-combo%29" target="_blank" rel="noopener">Get Quote on WhatsApp</a></div></div></div></section>
<section class="sza-sec" id="packages">
<span class="sza-kicker">Make it a trip</span>
<h2>Naina Devi, the lake and the Manali road</h2>
<p>Bilaspur sits on the Chandigarh–Manali highway, so the flight fits two easy plans: <b>Naina Devi darshan + a Bandla flight with one night in Bilaspur</b>, or a <b>Chandigarh → Bilaspur (fly) → Manali road trip</b>. Need only a cab? Book a <a href="/cabs/chandigarh-taxi-service/">Chandigarh taxi</a> or a <a href="/cabs/chandigarh-to-manali-taxi/">Chandigarh to Manali taxi</a>, read our <a href="/himachal-road-trip-from-chandigarh-guide/">Himachal road trip from Chandigarh guide</a>, or see <a href="/himachal-tour-package-from-chandigarh/">Himachal tour packages from Chandigarh</a>.</p>
<div class="sza-btns" style="margin-top:18px">{walink("Naina Devi + Bandla flight, 1N Bilaspur — Get Quote", what="Naina Devi darshan plus a Bandla flight with 1 night in Bilaspur")}{walink("Chandigarh → Bilaspur → Manali — Get Quote", what="a Chandigarh, Bilaspur (Bandla flight) and Manali road trip", cls="sza-btn line")}</div>
</section>

<section class="sza-sec sza-faq" id="faq">
<span class="sza-kicker">FAQ</span>
<h2>Paragliding in Bilaspur — questions</h2>
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
