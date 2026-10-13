#!/usr/bin/env python3
# Generates adventure-kit/pages/bungee-jumping-in-himachal.html (Page Builder night, 14 Oct 2026)
import urllib.parse, pathlib
SLUG = "bungee-jumping-in-himachal"
HERE = pathlib.Path(__file__).resolve().parent
CDN = "https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@a357aaa9c29439952d64e6cd9f8f2ac262725d17/adventure-kit/media/bungee-jumping-in-himachal/"
UP = "https://suzutravels.com/wp-content/uploads/2026/10/"
QUOTE = "/himachal-tour-packages-quote/?activity=" + urllib.parse.quote("Bungee jumping")

def wa(what="bungee jumping at Bir", tag=SLUG):
    t = f"Hi Suzu Travels, I want {what}. Dates: ___ , people: ___ (page: {tag})"
    return "https://wa.me/917087488961?text=" + urllib.parse.quote(t, safe="")

def walink(label, what="bungee jumping at Bir", cls="sza-btn gold"):
    return f'<a class="{cls}" href="{wa(what)}" target="_blank" rel="noopener">{label}</a>'

MAIN = wa()

def card(src, w, h, alt, badge, title, meta, text, what, extra=""):
    return (f'<article class="sza-card"><div class="img"><img src="{src}" alt="{alt}" loading="lazy" width="{w}" height="{h}"><span class="sza-badge">{badge}</span></div>'
            f'<div class="body"><h3>{title}</h3><div class="meta">{meta}</div><p class="meta">{text}</p>'
            f'<div class="go">{extra}<a class="q" href="{wa(what)}" target="_blank" rel="noopener">Get Quote →</a></div></div></article>')

cards = "".join([
    card(f"{UP}bungee-jumper-leap-platform-green-gorge-768x512.webp", 768, 512,
         "Bungee jumper in a harness diving head-first off a platform above a green forested gorge",
         "Verified", "Bir bungee site", "<b>Near Slabak, Bir (Kangra)</b> · set up in 2018",
         "About 50 m by operator listing, day slots roughly 10 am–5 pm. We confirm the height, slot and limits for your date.",
         "bungee jumping at Bir"),
    card(f"{UP}bungee-jumper-rebound-green-forest-768x512.webp", 768, 512,
         "Bungee jumper hanging from the cord on the rebound above a green wooded hillside",
         "Honest answer", "Bungee in Manali?", "<b>No operating site today</b>",
         "A 182 m site near Marhi was announced in 2019 but never opened. From Manali, plan the jump at Bir on your way to Dharamshala.",
         "bungee jumping at Bir on a Manali trip",
         extra='<a class="x" href="/adventure/adventure-activities-in-manali/">Manali activities →</a>'),
    card(f"{UP}paraglider-over-green-fields-blue-sky-768x1156.webp", 768, 1156,
         "Paraglider with a yellow wing gliding over green fields under a blue sky",
         "Combo", "Bir in one day", "<b>Bungee + tandem paragliding</b>",
         "Both are at Bir: jump, fly a tandem flight and see the Tibetan colony in one day.",
         "bungee jumping and tandem paragliding at Bir",
         extra='<a class="x" href="/adventure/paragliding-in-bir-billing/">Bir paragliding →</a>'),
    card(f"{UP}dharamshala-river-valley-dhauladhar-snow-peaks-768x576.webp", 768, 576,
         "Dharamshala: a green wooded valley with houses and the snow-capped Dhauladhar range",
         "Day trip", "From Dharamshala", "<b>Short drive to Bir</b>",
         "Staying in Dharamshala or McLeodganj? Bir is an easy day trip in our cab.",
         "a day trip from Dharamshala to Bir for bungee jumping",
         extra='<a class="x" href="/adventure/paragliding-in-dharamshala/">Dharamshala flights →</a>'),
])

steps_exp = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Send your date", "Date and group size on WhatsApp or the quote form."),
    ("We confirm the slot", "We check the slot, the limits and today's rate with a registered local operator."),
    ("Weigh-in &amp; check", "At the site the operator weighs every jumper and checks age and health."),
    ("Briefing &amp; harness", "Safety briefing, then the harness and ankle or body gear are fitted."),
    ("The jump", "The jump, the rebound and the lower-down; the recovery crew brings you back up."),
    ("Carry on", "Video handed over if included, then paragliding or your drive onwards."),
])

booking = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Tell us your date", "WhatsApp or the quote form — date, people, ages and where you are coming from."),
    ("We check your date", "Slot, limits and weather with a registered local operator."),
    ("You get one quote", "Bungee, paragliding if you want it, cab and hotel in one plan."),
    ("Confirm and go", "We send the reporting time and what to wear before you travel."),
])

faqs = [
    ("Is bungee jumping available in Manali?", "We have not found a verified, operating bungee site in Manali. A 182 m site near Marhi was announced in 2019 but never opened. Himachal's verified jump is at Bir."),
    ("Where is bungee jumping in Himachal?", "Near Bir in Kangra district, in the Slabak / Gunaid area — a site set up in 2018."),
    ("How high is the Bir bungee jump?", "Operator listings give about 50 m. We confirm the exact height and setup on booking."),
    ("What are the age and weight limits?", "The operator sets them; published figures vary (about 12/13–55 years, 40–100/110 kg). We confirm for your date before you travel."),
    ("How long does it take?", "About 30 minutes on site including the safety briefing (operator listing)."),
    ("Can I do bungee and paragliding on the same day?", 'Yes, both are at Bir; plan the jump and the <a href="/adventure/paragliding-in-bir-billing/">tandem flight</a> as one Bir day.'),
    ("What is the price of bungee jumping in Himachal?", f'It depends on group size, date, video and transport. Send your date on <a href="{MAIN}" target="_blank" rel="noopener">WhatsApp</a> and we share today\'s rate within minutes — Price: Get Quote.'),
    ("Is it safe?", "Jump only with a registered operator at the established site, meet the limits and follow the jump master. We arrange it only with registered local operators."),
]
faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)

more = [
    ("/adventure/paragliding-in-bir-billing/", "🪂", "Paragliding in Bir Billing", "Same-day combo"),
    ("/adventure/paragliding-in-dharamshala/", "🏔️", "Paragliding in Dharamshala", "Indrunag"),
    ("/adventure/paragliding-in-himachal/", "🧭", "Paragliding in Himachal", "Every site compared"),
    ("/adventure/adventure-activities-in-manali/", "🗓️", "Adventure activities in Manali", "What's open each month"),
    ("/adventure/river-rafting-in-kullu-manali/", "🛶", "River rafting in Kullu Manali", "Beas river"),
    ("/adventure/", "⛰️", "All adventures", "Air · Water · Snow · Land"),
]
more_html = "".join(f'<a class="sza-cat" href="{h}"><span class="ic">{i}</span><span class="n">{n}</span><span class="c">{c}</span></a>' for h, i, n, c in more)

reel = (HERE.parent / "media" / SLUG / "reel-section.html").read_text(encoding="utf-8").strip()

page = f'''<!-- bungee-jumping-in-himachal — built by Page Builder (night) 14 Oct 2026 from the Research Lead (night) brief + Visual Studio (night) media @a357aaa (reel-section @b98aa49). Kit v1.5. No prices, no operator names; height/limits shown as operator-listed and confirmed on booking; monsoon status for bungee left as "we confirm"; no claim the site is government-notified. Photos generic, neutral alt (not labelled as Bir). Quote-form links carry ?activity=Bungee%20jumping. -->
<style>.sza-bgj .sza-hero-in>*{{max-width:620px}}.sza-bgj .sza-chips{{max-width:700px}}.sza-bgj #experience .sza-steps{{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}.sza-bgj .sza-media ul{{padding-left:20px;list-style:disc;margin:0}}.sza-bgj .sza-media ul li{{margin:0 0 8px}}.sza-bgj .sza-media img{{aspect-ratio:4/3;object-fit:cover}}.sza-bgj .sza-media video{{height:auto;aspect-ratio:16/9}}.sza-bgj #spots .sza-grid{{grid-template-columns:repeat(auto-fit,minmax(230px,1fr))}}.sza-bgj #spots .sza-card .img img{{aspect-ratio:3/2;object-fit:cover}}.sza-bgj .sza-checks{{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}.sza-bgj .sza-choose{{margin-top:32px}}.sza-bgj .go .x{{margin-right:14px}}@media(max-width:820px){{.sza-bgj .sza-hero video{{object-position:30% 50%}}.sza-bgj .sza-hero:after{{background:linear-gradient(180deg,rgba(11,31,51,.35) 0%,rgba(11,31,51,.6) 40%,rgba(11,31,51,.94) 100%)}}}}</style>
<div class="sza sza-bgj">
<section class="sza-hero">
<video autoplay muted loop playsinline preload="metadata" poster="{UP}bungee-jumping-in-himachal-hero-poster.webp" aria-label="A bungee jumper diving off a platform over a green gorge, free fall and rebound on the cord, with a gold cord line that drops and settles and the words Bungee, Jump at Bir, about 50 m jump, operator-listed"><source src="{CDN}hero.webm" type="video/webm"><source src="{CDN}hero.mp4" type="video/mp4"></video>
<div class="sza-hero-in">
<span class="sza-kicker">Air · Bir, Kangra</span>
<p class="sza-hero-tag">Himachal's one real bungee jump — and how to fit it in</p>
<p class="sza-hero-sub">Bir, the paragliding capital, also has the state's verified bungee site. We add it to your Manali or Dharamshala trip with hotel + cab.</p>
<ul class="sza-chips"><li><b>Jump</b> ~50 m (operator-listed)</li><li><b>Where</b> Near Bir, Kangra</li><li><b>Slots</b> 10 am–5 pm (operator)</li><li><b>Includes</b> Harness + briefing + video option</li><li><b>Price</b> Get Quote</li></ul>
<div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Add to my trip</a></div>
<div class="sza-trust"><span><a href="https://suzutravels.com/certificates/">HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022</a></span><span>Cab + hotel + activities</span><span>Reply within minutes</span></div>
</div>
</section>
<nav class="sza-nav" aria-label="On this page"><div class="sza-nav-in"><a href="#overview">Overview</a><a href="#spots">Where to jump</a><a href="#experience">Your jump</a><a href="#season">Season</a><a href="#safety">Safety</a><a href="#booking">How booking works</a><a href="#packages">Packages</a><a href="#faq">FAQ</a><a class="cta" href="{MAIN}" target="_blank" rel="noopener">Get Quote</a></div></nav>

<section class="sza-sec" id="overview">
<span class="sza-kicker">Quick answer</span>
<h2>Bungee jumping in Himachal at a glance</h2>
<p class="sza-answer">Himachal's verified bungee jump is near Bir in Kangra district, run from a site set up in 2018 near Slabak village; operator listings give the jump as about 50 m. There is no operating bungee site in Manali today — a 182 m Marhi project announced in 2019 never opened. We arrange the Bir jump with a registered local operator and add it to your trip. Price: Get Quote.</p>
<div class="sza-facts"><div class="sza-fact"><div class="k">Where</div><div class="v">Near Bir (Slabak / Gunaid area, Kangra), close to the Bir paragliding landing area</div></div><div class="sza-fact"><div class="k">Jump</div><div class="v">About 50 m (operator listing) — confirmed on booking</div></div><div class="sza-fact"><div class="k">Time on site</div><div class="v">About 30 min including the briefing (operator listing)</div></div><div class="sza-fact"><div class="k">Who can jump</div><div class="v">Age and weight limits set by the operator — we confirm them for your date</div></div><div class="sza-fact"><div class="k">Pair with</div><div class="v">Tandem paragliding at Bir, monasteries, Dharamshala / McLeodganj</div></div><div class="sza-fact"><div class="k">Price</div><div class="v">Get Quote</div></div></div>
</section>

<section class="sza-sec alt" id="spots">
<span class="sza-kicker">Where to jump</span>
<h2>Where you can bungee jump in Himachal</h2>
<p class="sza-lead">One verified site, three easy ways to fit it into your trip. Photos show bungee jumping in general, not the Bir site itself.</p>
<div class="sza-grid">{cards}</div>
<div class="sza-media sza-choose" id="where"><video autoplay muted loop playsinline preload="none" poster="{UP}bungee-where-can-i-jump-explainer-poster.webp" width="1600" height="900" aria-label="Where can I actually jump? Schematic map: Manali, no verified bungee site today; Bir in Kangra, verified jump of about 50 m, operator-listed and confirmed on booking; Dharamshala, a short drive to Bir; add a Bir night on the Manali route; Get Quote"><source src="{CDN}explainer.webm" type="video/webm"><source src="{CDN}explainer.mp4" type="video/mp4"></video><div><h3>Where can I actually jump?</h3><ul><li><b>Manali</b> → no verified bungee site today.</li><li><b>Bir, Kangra</b> → the verified jump, about 50 m (operator-listed).</li><li><b>Dharamshala</b> → a short drive to Bir.</li><li><b>Manali → Dharamshala trip</b> → add a Bir night on the route.</li></ul></div></div>
</section>

<section class="sza-sec" id="experience">
<span class="sza-kicker">What happens</span>
<h2>Your bungee jump at Bir, step by step</h2>
<ol class="sza-steps">{steps_exp}</ol>
<div class="sza-media"><img src="{UP}bungee-jumper-upside-down-blue-sky-768x577.webp" alt="Bungee jumper hanging upside down from the cord with ankle straps against a pale blue sky" loading="lazy" width="768" height="577"><div><h3>First jump? That's normal</h3><p>Most jumpers are first-timers. The jump master fits your gear, explains the count and the position, and the crew lowers you down after the rebound.</p><p>Wear comfortable clothes and closed shoes, empty your pockets and tie long hair back. Tell us the ages and weights in your group when you book.</p></div></div>
</section>

<section class="sza-sec alt" id="season">
<span class="sza-kicker">When to go</span>
<h2>Best time for bungee jumping at Bir</h2>
<div class="sza-scroll"><table class="sza-tbl"><thead><tr><th>Months</th><th>Bungee at Bir</th><th>Note</th></tr></thead><tbody><tr><td>Oct – Nov</td><td>Open (best)</td><td>Dry and clear; peak paragliding season too</td></tr><tr><td>Dec – Feb</td><td>Usually open</td><td>Cold mornings; we confirm daily</td></tr><tr><td>Mar – Jun</td><td>Open</td><td>Busy in May–June</td></tr><tr><td>Jul – mid Sep</td><td>Check</td><td>Monsoon; Kangra's 15 Jul–15 Sep adventure ban covers paragliding and rafting — we confirm whether jumps run before you plan</td></tr></tbody></table></div>
</section>

<div class="sza-band" id="safety"><div class="sza-band-in">
<span class="sza-kicker">Safety first</span>
<h2>What we check before we book your jump</h2>
<p class="sza-lead">Suzu Travels is an <a href="https://suzutravels.com/certificates/" style="color:#f3d98f;text-decoration:underline">HP Tourism registered travel agent (Reg. No. DTO-MND-11-243/2022)</a>. We arrange bungee only with registered local operators and plan around these checks:</p>
<ul class="sza-checks"><li><b>Established site only</b>Jump only with a registered operator at an established site; we never book roadside or 'new' jumps.</li><li><b>Weigh-in on the day</b>The operator weighs every jumper; you must meet the age and weight limits on the day.</li><li><b>Health first</b>Do not jump with heart conditions, high blood pressure, epilepsy, recent surgery, a back or neck injury, or during pregnancy (standard bungee exclusions — the operator has the final word).</li><li><b>Clear head</b>No alcohol before the jump; follow every instruction from the jump master.</li><li><b>Weather buffer</b>Weather or wind can pause jumps; we keep a buffer in your plan.</li></ul>
</div></div>

<section class="sza-sec" id="booking">
<span class="sza-kicker">How booking works</span>
<h2>Get a quote in minutes</h2>
<ol class="sza-steps">{booking}</ol>
<div class="sza-media"><img src="{UP}bungee-jumper-free-fall-pine-forest-768x512.webp" alt="Bungee jumper in a blue body harness falling with arms spread, a red cord trailing above, against a pine forest" loading="lazy" width="768" height="512"><div><h3>What your quote depends on</h3><ul><li>Number of jumpers and the date (weekends and holidays are busiest)</li><li>Video / photo add-on</li><li>Combo with tandem paragliding at Bir</li><li>Transport: from Bir town, Dharamshala, Palampur or a Manali route</li><li>Hotel nights in Bir or Dharamshala and the rest of your package — today's rate on WhatsApp within minutes</li></ul></div></div>
</section>

{reel}

<section class="sza-quote"><div><span class="sza-kicker">Ready to jump?</span><h2>Get your Bir bungee quote</h2><p>Tell us your travel date and group size. We reply with today's rate for your date within minutes — and can add your stay and cab.</p></div><div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan full trip</a></div></section>

<section class="sza-sec" id="packages">
<span class="sza-kicker">Make it a trip</span>
<h2>Fit the jump into a Manali – Bir – Dharamshala circuit</h2>
<div class="sza-media"><img src="{UP}dharamshala-river-valley-dhauladhar-snow-peaks-768x576.webp" alt="Dharamshala: a green wooded valley with houses and the snow-capped Dhauladhar range under a blue sky" loading="lazy" width="768" height="576"><div><p>Bir sits between Manali and Dharamshala, so the jump fits naturally into a circuit: Manali, a night at Bir for bungee and a tandem flight, then Dharamshala and McLeodganj. Staying only in Dharamshala? Make Bir a day trip.</p><p>Need only a cab? Book a <a href="/cabs/dharamshala-taxi-service/">Dharamshala taxi</a> or a <a href="/cabs/manali-taxi-service/">Manali taxi</a>, or see our <a href="/himachal-tour-packages/">Himachal tour packages</a>.</p></div></div>
<div class="sza-btns" style="margin-top:18px">{walink("Manali → Bir → Dharamshala — Get Quote", what="a Manali, Bir and Dharamshala trip with bungee jumping at Bir")}{walink("Dharamshala + Bir day trip — Get Quote", what="a Dharamshala stay with a Bir day trip for bungee jumping", cls="sza-btn line")}</div>
</section>

<section class="sza-sec sza-faq" id="faq">
<span class="sza-kicker">FAQ</span>
<h2>Bungee jumping in Himachal — questions</h2>
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
