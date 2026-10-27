#!/usr/bin/env python3
# Generates adventure-kit/pages/zipline-in-manali.html (Page Builder night, 21 Oct 2026 IST)
import urllib.parse, pathlib
SLUG = "zipline-in-manali"
HERE = pathlib.Path(__file__).resolve().parent
CDN = "https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@cea61e32d770f3325e2cd139b1ae4f2a565ea8d2/adventure-kit/media/zipline-in-manali/"
UP9 = "https://suzutravels.com/wp-content/uploads/2026/09/"
UP = "https://suzutravels.com/wp-content/uploads/2026/10/"
QUOTE = "/himachal-tour-packages-quote/?activity=" + urllib.parse.quote("Zipline")
WHAT = "a zipline in Manali"

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
    card(f"{UP}himalayan-forest-valley-view-768x1365.webp", 768, 1365,
         "Forested Himalayan valley with mountain peaks",
         "Classic pick", "Solang Valley zipline", "<b>~13 km from Manali · year-round, weather permitting</b>",
         "Ride above the Solang meadow, then the ropeway or a tandem flight the same morning.",
         "a zipline at Solang Valley, Manali", "/adventure/solang-valley-activities/"),
    card(f"{UP}two-riders-ziplines-over-water-768x512.webp", 768, 512,
         "Two people in helmets and harnesses riding parallel ziplines over a wide lake with green islands",
         "Ask us first", "Beas-valley ziplines &amp; river crossing", "<b>Several lines near Manali</b>",
         "Only some of these lines are registered — we check the operator and the site approval before we book.",
         "a zipline or river crossing in the Beas valley near Manali"),
    card(f"{UP}paraglider-snow-peaks-solang-valley-768x960.webp", 768, 960,
         "Paraglider with a yellow wing high above pine forest and snow-capped peaks at Solang Valley, Manali",
         "Combo", "Solang adventure day", "<b>Zipline + paragliding + ropeway</b>",
         "All three in one half-day at Solang, with your cab from the hotel and back.",
         "a Solang adventure half-day with zipline, paragliding and ropeway", "/adventure/paragliding-in-manali/"),
    card(f"{UP9}zipline-rider-over-forest-768x512.webp", 768, 512,
         "A smiling woman in a helmet and harness riding a zipline high above green forest",
         "Shimla side", "Kufri (Shimla)", "<b>Inside the Kufri adventure park</b>",
         "A zipline next to go-karts and horse rides — easy to add to a Shimla–Kufri day.",
         "a zipline at Kufri near Shimla", "/adventure/kufri-adventure-activities/"),
    card(f"{UP}snow-peaks-above-pine-forest-768x576.webp", 768, 576,
         "Snow-capped mountain range under a deep blue sky with snowy slopes and dark pine trees in front",
         "Not open yet", "Naddi, Dharamshala (coming)", "<b>Planned by the state on PPP</b>",
         "A ~4.3 km zipline from the Gallu Devi area over Naddi is planned — not open yet. For Dharamshala today, fly tandem instead.",
         "adventure activities in Dharamshala", "/adventure/paragliding-in-dharamshala/"),
])

steps_exp = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Send your dates", "Your Manali dates and group on WhatsApp — tell us the ages of any kids."),
    ("We pick a registered site", "One that fits your day plan; a Solang morning is the usual choice."),
    ("Cab to the site", "Staff weigh you and give a short safety briefing before anyone clips in."),
    ("Gear on, clips checked", "Helmet, full-body harness and gloves go on; the staff check every clip."),
    ("You ride", "Then the next activity — ropeway, a tandem flight, snow play — or back to the hotel."),
    ("Rain or wind?", "The operator pauses the line; we move it to another slot in your trip."),
])

booking = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Tell us", "WhatsApp or the quote form — dates, group size, kids' ages and your hotel area."),
    ("We check your date", "Weather, season and a registered operator with an approved site for that day."),
    ("You get one quote", "Zipline, any add-on activity, hotel nights and cab in one plan."),
    ("Confirm and go", "We send the meeting time, the site and what to wear."),
])

season = [
    ("Mar–Jun", "Clear days, peak crowds (searches peak May–Jun)", "Go early morning"),
    ("Jul–mid-Sep", "Monsoon: rain days stop lines; Kullu's 15 Jul–15 Sep ban covers paragliding, rafting and water sports", "Check that year's order before booking"),
    ("Mid-Sep–Nov", "Clear, cool, quieter", "Best months"),
    ("Dec–Feb", "Snow and cold at Solang; lines run on dry, calm days only", "Combine with snow play"),
]
season_html = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in season)

faqs = [
    ("Where can I do a zipline in Manali?", "At Solang Valley and a few adventure spots along the Beas near Manali. We book only sites run by operators registered with HP Tourism."),
    ("Is ziplining in Manali safe?", "It is when the site is approved and the operator is registered: HP rules require yearly site inspection by a Technical Committee, proper safety gear and rescue within 30 minutes. A 2025 accident happened at a line with no approvals — so ask first."),
    ("How do I know a zipline is registered?", "Ask the operator for the HP Tourism Department registration certificate. When you book through us, we check it before your date."),
    ("What is the price of a zipline in Manali?", "It depends on the site, number of rides, group and date. Send your dates on WhatsApp and we share today's rate within minutes — Get Quote."),
    ("Can kids do the zipline?", "Many sites take children, but age and weight limits are set by the operator on the spot. Tell us the ages when you ask for a quote."),
    ("Does the zipline run in winter or rain?", "Lines stop in rain, storm or strong wind. In winter they run on calm, dry days, so keep the zipline flexible in your plan."),
    ("Is there a zipline in Dharamshala or Shimla?", "Kufri near Shimla has one in its <a href=\"/adventure/kufri-adventure-activities/\">adventure park</a>. A long zipline over Naddi in Dharamshala is planned by the state but not open yet."),
    ("Can I combine it with paragliding?", "Yes — Solang mornings often fit a zipline, a <a href=\"/adventure/paragliding-in-manali/\">tandem flight</a> and the ropeway. We plan it with your hotel and cab."),
]
faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)

more = [
    ("/adventure/solang-valley-activities/", "🏔️", "Solang Valley", "Ropeway, flights, snow"),
    ("/adventure/paragliding-in-manali/", "🪂", "Paragliding in Manali", "Tandem flights at Solang"),
    ("/adventure/adventure-activities-in-manali/", "🧭", "Manali adventures", "What runs in your month"),
    ("/adventure/river-rafting-in-kullu-manali/", "🚣", "River rafting", "Beas, Kullu–Manali"),
    ("/adventure/bungee-jumping-in-himachal/", "🪢", "Bungee jumping", "Where you can really jump"),
    ("/adventure/", "🗺️", "All adventures", "Air · Water · Snow · Land"),
]
more_html = "".join(f'<a class="sza-cat" href="{h}"><span class="ic">{i}</span><span class="n">{n}</span><span class="c">{c}</span></a>' for h, i, n, c in more)

reel = (HERE.parent / "media" / SLUG / "reel-section.html").read_text(encoding="utf-8").strip()

page = f'''<!-- zipline-in-manali — built by Page Builder (night) 21 Oct 2026 IST from the Research Lead brief 20 Oct (morning) + Visual Studio media @cea61e3 (reel-section @91dec3a). Kit v1.8. No prices, no operator names. Unverified items left off: line lengths/heights/speeds, "longest zipline" claims, official age/weight limits, whether the Kullu monsoon order names ziplines, list of registered 2026 sites, Naddi opening date, Kasauli. Brief badge "Most asked" replaced by "Classic pick" (kit v1.7 badge rule). Generic photos carry neutral alt text. -->
<style>.sza-zim .sza-hero-in>*{{max-width:620px}}.sza-zim .sza-chips{{max-width:700px}}.sza-zim .sza-media ul{{padding-left:20px;list-style:disc;margin:0}}.sza-zim .sza-media ul li{{margin:0 0 8px}}.sza-zim .sza-media img{{height:auto;aspect-ratio:3/2;object-fit:cover}}.sza-zim .sza-media video{{height:auto;aspect-ratio:16/9}}.sza-zim #spots .sza-grid{{grid-template-columns:repeat(auto-fit,minmax(min(300px,100%),1fr))}}.sza-zim #spots .sza-card .img img{{aspect-ratio:3/2;object-fit:cover}}.sza-zim .sza-checks{{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}.sza-zim .sza-choose{{margin-top:32px}}@media(max-width:820px){{.sza-zim .sza-hero video{{object-position:30% 50%}}.sza-zim .sza-hero:after{{background:linear-gradient(180deg,rgba(11,31,51,.35) 0%,rgba(11,31,51,.6) 40%,rgba(11,31,51,.94) 100%)}}}}</style>
<div class="sza sza-zim">
<section class="sza-hero">
<video autoplay muted loop playsinline preload="metadata" poster="{UP}zipline-in-manali-hero-poster.webp" aria-label="A rider on a zipline above green forest, locking carabiners on a harness, a man in a harness above the forest and snow peaks above pines, with a gold cable and a moving trolley counting four checks before you clip in: registered operator, site inspected this year, helmet and harness checked, weather calm"><source src="{CDN}hero.webm" type="video/webm"><source src="{CDN}hero.mp4" type="video/mp4"></video>
<div class="sza-hero-in">
<span class="sza-kicker">Air · Manali</span>
<p class="sza-hero-tag">Fly across the valley — on a registered line</p>
<p class="sza-hero-sub">Zipline rides at Solang and the Beas valley, fitted into your Manali day with hotel and cab. We book only with registered local operators.</p>
<ul class="sza-chips"><li><b>Solang</b> Valley</li><li><b>Registered</b> sites only</li><li><b>Helmet + harness</b> check</li><li><b>Pair with</b> paragliding</li><li><b>Price</b> Get Quote</li></ul>
<div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan my trip</a></div>
<div class="sza-trust"><span><a href="https://suzutravels.com/certificates/">HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022</a></span><span>Zipline + hotel + cab</span><span>Reply within minutes</span></div>
</div>
</section>
<nav class="sza-nav" aria-label="On this page"><div class="sza-nav-in"><a href="#overview">Overview</a><a href="#spots">Where to ride</a><a href="#experience">How it works</a><a href="#season">By month</a><a href="#safety">Rules &amp; safety</a><a href="#booking">How booking works</a><a href="#packages">Packages</a><a href="#faq">FAQ</a><a class="cta" href="{MAIN}" target="_blank" rel="noopener">Get Quote</a></div></nav>

<section class="sza-sec" id="overview">
<span class="sza-kicker">Quick answer</span>
<h2>Zipline in Manali, at a glance</h2>
<p class="sza-answer">You can ride a zipline in Manali at Solang Valley (about 13 km from town) and at a few Beas-valley adventure spots. In Himachal every zipline site must be approved and inspected each year by a state Technical Committee, and the operator must be registered with the Tourism Department. Ask for that registration before you ride — we book only registered local operators.</p>
<div class="sza-facts"><div class="sza-fact"><div class="k">Where</div><div class="v">Solang Valley + a few Beas-side spots near Manali; Kufri (Shimla) has one in its adventure park</div></div><div class="sza-fact"><div class="k">Rules</div><div class="v">HP Miscellaneous Adventure Activities Rules 2017 (amended 2021): yearly Technical Committee approval and inspection; rescue within 30 minutes</div></div><div class="sza-fact"><div class="k">Who registers</div><div class="v">HP Tourism Department — operator registration + participant insurance</div></div><div class="sza-fact"><div class="k">Weather</div><div class="v">Lines stop in rain, storm or strong wind — the operator's call on the day</div></div><div class="sza-fact"><div class="k">Pairs with</div><div class="v">Solang ropeway, paragliding, snow play in winter</div></div><div class="sza-fact"><div class="k">Price</div><div class="v">Get Quote</div></div></div>
</section>

<section class="sza-sec alt" id="spots">
<span class="sza-kicker">Where to ride</span>
<h2>Zipline options in and around Manali</h2>
<p class="sza-lead">Solang is the usual pick. Beas-valley lines vary — we check the paperwork first. Two more options sit elsewhere in Himachal.</p>
<div class="sza-grid">{cards}</div>
<div class="sza-media sza-choose" id="zipline-checks"><video autoplay muted loop playsinline preload="none" poster="{UP}zipline-before-you-clip-in-explainer-poster.webp" width="1600" height="900" aria-label="Before you clip in: a trolley runs a gold zipline cable through four checkpoints that tick gold — HP Tourism registration, yearly Technical Committee inspection, helmet and harness, calm weather — then: We check all four before we book, and Get Quote on WhatsApp"><source src="{CDN}explainer.webm" type="video/webm"><source src="{CDN}explainer.mp4" type="video/mp4"></video><div><h3>Before you clip in</h3><ul><li><b>Registered operator</b> — HP Tourism Department certificate.</li><li><b>Site inspected this year</b> — Technical Committee approval.</li><li><b>Helmet + harness</b> — checked by staff, every clip.</li><li><b>Weather calm</b> — no rain, storm or strong wind.</li></ul><p>We check all four before we book.</p></div></div>
</section>

<section class="sza-sec" id="experience">
<span class="sza-kicker">How it works</span>
<h2>Your zipline morning, step by step</h2>
<ol class="sza-steps">{steps_exp}</ol>
<div class="sza-media"><img src="{UP}zipline-rider-harness-above-forest-768x512.webp" alt="Smiling man in a full-body harness riding a zipline high above a dense green forest" loading="lazy" width="768" height="512"><div><h3>What to wear and carry</h3><p>Closed shoes with grip, clothes that fit under a harness and a warm layer — Solang mornings are cold even in May. Leave loose items with your driver.</p><p>Most guests do the zipline as part of a <a href="/adventure/solang-valley-activities/">Solang Valley</a> half-day. In winter add a <a href="/adventure/snow-activities-manali/">snow day</a> or the <a href="/adventure/atal-tunnel-sissu-snow-trip/">Atal Tunnel and Sissu</a>.</p></div></div>
</section>

<section class="sza-sec alt" id="season">
<span class="sza-kicker">When to go</span>
<h2>Zipline in Manali by month</h2>
<div class="sza-scroll"><table class="sza-tbl"><thead><tr><th>Months</th><th>What to expect</th><th>Plan</th></tr></thead><tbody>{season_html}</tbody></table></div>
<p style="margin-top:14px">Weekends and holidays are busiest — a weekday morning gives you a shorter wait.</p>
</section>

<div class="sza-band" id="safety"><div class="sza-band-in">
<span class="sza-kicker">Rules &amp; safety</span>
<h2>What we check before we book your zipline</h2>
<p class="sza-lead">Suzu Travels is an <a href="https://suzutravels.com/certificates/" style="color:#f3d98f;text-decoration:underline">HP Tourism registered travel agent (Reg. No. DTO-MND-11-243/2022)</a>. We arrange ziplines with registered local operators and check these first:</p>
<ul class="sza-checks"><li><b>Registered operator</b>The operator must be registered with the HP Tourism Department under the Miscellaneous Adventure Activities Rules 2017/2021 — ask to see the certificate.</li><li><b>Site inspected every year</b>Zipline and flying-fox sites need approval and a yearly inspection by the state Technical Committee, chaired by the Director of Tourism.</li><li><b>Safety gear and rescue</b>Helmet and harness to the specified standard (a life jacket on river crossings), and a rescue possible within 30 minutes.</li><li><b>Insurance</b>The rules require the operator to insure participants.</li><li><b>Why it matters</b>In June 2025 a 12-year-old girl fell about 30 ft from a zipline near Nehru Kund; the minister said that operator had neither Tourism registration nor technical approval (<a href="https://www.tribuneindia.com/news/himachal/manali-zipline-operators-to-face-action-sports-minister" target="_blank" rel="noopener" style="color:#f3d98f">The Tribune</a>).</li><li><b>Kids, weight, health</b>Limits are set by the operator on the spot — tell us ages and any health issue when you ask, and we confirm before you go.</li></ul>
</div></div>

<section class="sza-sec" id="booking">
<span class="sza-kicker">How booking works</span>
<h2>Get a quote in minutes</h2>
<ol class="sza-steps">{booking}</ol><figure id="booking-explainer" style="margin:28px auto 32px;max-width:880px"><video poster="https://suzutravels.com/wp-content/uploads/2026/09/how-booking-works-adventure-explainer.webp" autoplay muted loop playsinline preload="none" width="1600" height="900" style="display:block;width:100%;height:auto;aspect-ratio:16/9;border-radius:18px;background:#0b1f33;box-shadow:0 12px 32px rgba(11,31,51,.2)" aria-label="10-second motion graphic: how booking works in 4 steps. Tell us the activity, place, date and group size; we check your date, season, weather rules and a registered local operator; you get one quote, activity alone or with hotel, cab and sightseeing; confirm with a small advance and our team looks after the day"><source src="https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@1d39d275782e44fb56b01370aa2524e4786607f3/adventure-kit/media/adventure-hub/booking-explainer.webm" type="video/webm"><source src="https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@1d39d275782e44fb56b01370aa2524e4786607f3/adventure-kit/media/adventure-hub/booking-explainer.mp4" type="video/mp4"></video><figcaption style="margin-top:10px;font-size:15px;line-height:1.5;color:#5b6975;text-align:center">Four steps from your WhatsApp message to your zipline ride. Send your plan and get today’s rate within minutes.</figcaption></figure>
<div class="sza-media"><img src="{UP}instructor-checking-harness-clip-768x512.webp" alt="Instructor's hands checking the rope and carabiner on a person's orange safety harness before a climb" loading="lazy" width="768" height="512"><div><h3>What your quote depends on</h3><ul><li>Which site and how many rides</li><li>Zipline alone or a combo — paragliding, ropeway, snow play</li><li>Group size and kids</li><li>Travel date, weekend or holiday rush</li><li>Cab from your hotel and how long you stay</li><li>Photos / video add-on, arranged on request</li></ul><p>We send today's rate on WhatsApp within minutes.</p></div></div>
</section>

{reel}

<section class="sza-quote"><div><span class="sza-kicker">Ready to fly across the valley?</span><h2>Get your Manali zipline quote</h2><p>Tell us your dates and who is riding. We reply with one plan — zipline, hotel and cab — within minutes.</p></div><div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan full trip</a></div></section>

<section class="sza-sec" id="packages">
<span class="sza-kicker">Make it a trip</span>
<h2>A Manali trip with a Solang morning</h2>
<p>The easy way to fit it in: a <b>Manali 3N/4N</b> trip with one Solang morning — zipline, a tandem flight and the ropeway — with hotel and cab in one quote. Read our <a href="/manali/">Manali guide</a>, browse <a href="/packages/">all packages</a> or see <a href="/adventure/adventure-activities-in-manali/">what runs in Manali in your month</a>. Need only a cab? Book a <a href="/cabs/delhi-to-manali-taxi/">Delhi to Manali taxi</a> or a <a href="/cabs/chandigarh-to-manali-taxi/">Chandigarh to Manali taxi</a>. Going on to Shimla? See <a href="/destination/shimla-tour-packages/">Shimla tour packages</a>.</p>
<div class="sza-btns" style="margin-top:18px">{walink("Manali + Solang morning — Get Quote", what="a 3N/4N Manali trip with a Solang morning (zipline, paragliding, ropeway), hotel and cab")}{walink("Solang adventure half-day — Get Quote", what="a Solang adventure half-day with zipline, paragliding and ropeway", cls="sza-btn line")}</div>
</section>

<section class="sza-sec sza-faq" id="faq">
<span class="sza-kicker">FAQ</span>
<h2>Zipline in Manali — questions</h2>
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
