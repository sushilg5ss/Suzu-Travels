#!/usr/bin/env python3
# Generates adventure-kit/pages/serolsar-lake-trek.html (Page Builder night, 29 Oct 2026)
import urllib.parse, pathlib
SLUG = "serolsar-lake-trek"
HERE = pathlib.Path(__file__).resolve().parent
CDN = "https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@f38ae1b777667b20baea2ede54aa7003e15de49c/adventure-kit/media/serolsar-lake-trek/"
UP = "https://suzutravels.com/wp-content/uploads/2026/10/"
QUOTE = "/himachal-tour-packages-quote/?activity=" + urllib.parse.quote("Serolsar Lake trek")
WHAT = "the Serolsar Lake trek from Jalori Pass (Jibhi, Kullu)"

def wa(what=WHAT, tag=SLUG):
    t = f"Hi Suzu Travels, I want a quote for {what}. Travel date: ___ , people: ___ (page: {tag})"
    return "https://wa.me/917087488961?text=" + urllib.parse.quote(t, safe="")

def walink(label, what=WHAT, cls="sza-btn gold"):
    return f'<a class="{cls}" href="{wa(what)}" target="_blank" rel="noopener">{label}</a>'

MAIN = wa()

def card(src, w, h, alt, badge, title, meta, text, what):
    return (f'<article class="sza-card"><div class="img"><img src="{src}" alt="{alt}" loading="lazy" width="{w}" height="{h}"><span class="sza-badge">{badge}</span></div>'
            f'<div class="body"><h3>{title}</h3><div class="meta">{meta}</div><p class="meta">{text}</p>'
            f'<div class="go"><a class="q" href="{wa(what)}" target="_blank" rel="noopener">Get Quote →</a></div></div></article>')

cards = "".join([
    card(f"{UP}misty-forest-trail-tall-conifers-768x1152.webp", 768, 1152,
         "Narrow dirt trail running between tall conifer trees in a misty forest",
         "Classic pick", "Serolsar Lake day hike", "<b>About 5 km each way from Jalori Pass</b>",
         "Jalori Pass → forest trail → the lake and back in one day, from a Jibhi or Tirthan stay.",
         "the Serolsar Lake day hike from Jalori Pass with a Jibhi stay"),
    card(f"{UP}snow-peaks-above-pine-forest-768x576.webp", 768, 576,
         "Snow-capped mountain range under a deep blue sky with snowy slopes and dark pine trees in front",
         "On the way", "360° viewpoint", "<b>About 2 km above Jalori</b>",
         "The highest point of the walk, after one short steep climb. Wide views over the ridges of Seraj and the Tirthan side.",
         "the Serolsar Lake trek with the 360-degree viewpoint at Jalori Pass"),
    card(f"{UP}mountain-lake-ringed-by-pine-trees-768x512.webp", 768, 512,
         "Calm blue mountain lake ringed by pine forest with rocky peaks behind under a blue sky",
         "Sacred site", "Lake &amp; Budhi Nagin temple", "<b>Lake about 3,100 m</b>",
         "A small shrine stands on the shore and devotees offer ghee. The water is fenced and not to be touched; the temple closes in heavy snow.",
         "the Serolsar Lake trek to the Budhi Nagin temple"),
    card(f"{UP}himalayan-forest-valley-view-768x1365.webp", 768, 1365,
         "Forested Himalayan valley with mountain peaks",
         "Add-on", "Raghupur Fort walk", "<b>Separate trail from Jalori Pass</b>",
         "On the other side of the pass: open meadows and the ruins of an old fort. Add it on the same day or the next.",
         "the Raghupur Fort walk at Jalori Pass with the Serolsar Lake trek"),
    card(f"{UP}snow-laden-conifer-forest-winter-768x499.webp", 768, 499,
         "Snow-laden conifer trees after fresh snowfall under a pale winter sky",
         "Dec–Feb, conditions apply", "Winter snow walk", "<b>Only when the Jalori road is open</b>",
         "Snow and ice on the trail. With a local guide and microspikes, and a 4x4 cab; we check the road that morning.",
         "a winter snow walk to Serolsar Lake from Jalori Pass"),
])

steps_exp = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Send your dates", "WhatsApp us your dates and group. We check the Jalori road status for those days."),
    ("Stay in Jibhi or Tirthan", "A cottage or homestay by the river — we book it together with your cab."),
    ("Drive up to Jalori Pass", "Morning drive Jibhi → Jalori Pass, about 12 km on a steep hill road."),
    ("Walk to the lake", "With a local guide: the 360° viewpoint, then the forest trail to the lake and the Budhi Nagin temple — about 3–3.5 hours up."),
    ("Lunch and turn back", "Carry your own tiffin and water (no shops on the trail). Turn back by early afternoon — about 3 hours down."),
    ("Back to Jibhi", "Down to Jalori and on to your stay. Next day: Raghupur Fort, Jibhi waterfall or a trout-fishing day in Tirthan."),
])

booking = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Tell us your dates", "WhatsApp or the quote form — dates, group size, where you start from."),
    ("We check your date", "Season, the Jalori road, and a local guide with a registered local operator."),
    ("You get one quote", "Guide, Jibhi or Tirthan stay and the cab in one plan."),
    ("Confirm and go", "We send the reporting time, what to carry and the road update before you travel."),
])

faqs = [
    ("How long is the Serolsar Lake trek?", "About 5 km one way from Jalori Pass, so about 10 km return. Most people take 3–3.5 hours up and about 3 hours back."),
    ("Is the Serolsar Lake trek easy?", "Yes. It is an easy forest walk with gentle ups and downs and one short steep climb to the 360-degree viewpoint. Good shoes help."),
    ("How high is Serolsar Lake?", "About 3,100 m (10,170 ft). Jalori Pass, where the walk starts, is about 3,120 m."),
    ("Can I do the Serolsar Lake trek in winter?", "Only when the Jalori road is open. From December to February the trail has snow and ice and the highway over Jalori (NH-305) can close after heavy snow, so go with a guide and check that morning."),
    ("Do I need a permit for Serolsar Lake?", "No permit is needed for the walk. Please do not touch the lake water — it is sacred and fenced."),
    ("Can I camp at Serolsar Lake?", 'Camping is not allowed around the lake. Stay in <a href="/jibhi/">Jibhi</a> or <a href="/tirthan-valley/">Tirthan</a> and do it as a day trek.'),
    ("How far is Jalori Pass from Jibhi?", "About 12 km by a steep hill road, roughly 45 minutes to an hour in good conditions."),
    ("What does the Serolsar trek cost?", "It depends on the guide, the cab, nights in Jibhi and the season. Send your dates on WhatsApp and we share today's rate in minutes — Get Quote."),
]
faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)

more = [
    ("/adventure/prashar-lake-trek/", "⛰️", "Prashar Lake Trek", "Another easy lake trek, near Mandi"),
    ("/adventure/trout-fishing-in-himachal/", "🎣", "Trout fishing", "A day on the Tirthan river"),
    ("/adventure/camping-in-himachal/", "⛺", "Camping in Himachal", "Riverside and forest camps"),
    ("/adventure/kheerganga-trek/", "🥾", "Kheerganga Trek", "Hot springs in the Parvati valley"),
    ("/adventure/river-rafting-in-kullu-manali/", "🚣", "Rafting in Kullu", "On the Beas, on your way"),
    ("/adventure/", "🧭", "All adventures", "Air · Water · Snow · Land"),
]
more_html = "".join(f'<a class="sza-cat" href="{h}"><span class="ic">{i}</span><span class="n">{n}</span><span class="c">{c}</span></a>' for h, i, n, c in more)

reel = (HERE.parent / "media" / SLUG / "reel-section.html").read_text(encoding="utf-8").strip()

page = f'''<!-- serolsar-lake-trek — built by Page Builder (night) 29 Oct 2026 from the Research Lead brief 28 Oct + Visual Studio media @f38ae1b (reel-section @1edd102). Kit v1.8. No prices, no operator names; heights/distances "about"; NH-305 winter closure as "can close", no fixed dates; Raghupur distance left off (unverified). Brief badge "Most booked" replaced by "Classic pick" (kit v1.7 rule). Photos generic, neutral alt. -->
<style>.sza-srl .sza-hero-in>*{{max-width:620px}}.sza-srl .sza-chips{{max-width:700px}}.sza-srl #experience .sza-steps{{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}.sza-srl .sza-media ul{{padding-left:20px;list-style:disc;margin:0}}.sza-srl .sza-media ul li{{margin:0 0 8px}}.sza-srl .sza-media img{{height:auto;aspect-ratio:4/3;object-fit:cover}}.sza-srl .sza-media video{{height:auto;aspect-ratio:16/9}}.sza-srl #spots .sza-grid{{grid-template-columns:repeat(auto-fit,minmax(220px,1fr))}}.sza-srl #spots .sza-card .img img{{aspect-ratio:3/2;object-fit:cover}}.sza-srl .sza-checks{{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}@media(max-width:820px){{.sza-srl .sza-hero video{{object-position:20% 50%}}.sza-srl .sza-hero:after{{background:linear-gradient(180deg,rgba(11,31,51,.35) 0%,rgba(11,31,51,.6) 40%,rgba(11,31,51,.94) 100%)}}}}</style>
<div class="sza sza-srl">
<section class="sza-hero">
<video autoplay muted loop playsinline preload="metadata" poster="{UP}serolsar-lake-trek-hero-poster.webp" aria-label="Misty conifer trail, a lake ringed by pines, a snow ridge and snowy conifers, with a gold trail from Jalori Pass via the 360-degree viewpoint to Serolsar Lake and a counter running to about 5 km one way"><source src="{CDN}hero.webm" type="video/webm"><source src="{CDN}hero.mp4" type="video/mp4"></video>
<div class="sza-hero-in">
<span class="sza-kicker">Easy forest trek · Jalori Pass, Kullu</span>
<p class="sza-hero-tag">Five kilometres of oak forest to a sacred lake.</p>
<p class="sza-hero-sub">Walk from Jalori Pass (about 3,120 m) to Serolsar Lake and the Budhi Nagin temple, with a Jibhi stay and cab arranged by us.</p>
<ul class="sza-chips"><li><b>Distance</b> ~5 km one way</li><li><b>Grade</b> Easy</li><li><b>Time</b> ~3 h up, ~3 h back</li><li><b>Lake</b> ~3,100 m</li><li><b>Season</b> Mar–Nov; snow Dec–Feb</li><li><b>Price</b> Get Quote</li></ul>
<div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan my trip</a></div>
<div class="sza-trust"><span><a href="https://suzutravels.com/certificates/">HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022</a></span><span>Guide + stay + cab</span><span>Reply within minutes</span></div>
</div>
</section>
<nav class="sza-nav" aria-label="On this page"><div class="sza-nav-in"><a href="#overview">Overview</a><a href="#spots">The walk</a><a href="#experience">How the day runs</a><a href="#season">Best time</a><a href="#safety">Safety</a><a href="#booking">How booking works</a><a href="#packages">Packages</a><a href="#faq">FAQ</a><a class="cta" href="{MAIN}" target="_blank" rel="noopener">Get Quote</a></div></nav>

<section class="sza-sec" id="overview">
<span class="sza-kicker">Quick answer</span>
<h2>Serolsar Lake trek, at a glance</h2>
<p class="sza-answer">Serolsar Lake is a small sacred lake about 5 km from Jalori Pass (about 3,120 m) in Kullu district, reached on an easy forest trail with a 360-degree viewpoint on the way. The walk takes about three hours each way and needs no permit. March to November is best; in winter snow and ice cover the trail and the Jalori road can close.</p>
<div class="sza-facts"><div class="sza-fact"><div class="k">Start</div><div class="v">Jalori Pass (~3,120 m), by the Mata Jalori temple; about 12 km above Jibhi</div></div><div class="sza-fact"><div class="k">Distance</div><div class="v">About 5 km one way — about 2 km to the 360° viewpoint, then about 3.3 km to the lake</div></div><div class="sza-fact"><div class="k">Time</div><div class="v">About 3–3.5 h up and 3 h back; same-day return from Jibhi</div></div><div class="sza-fact"><div class="k">Difficulty</div><div class="v">Easy, with one short steep climb to the viewpoint</div></div><div class="sza-fact"><div class="k">The lake</div><div class="v">About 3,100 m (10,170 ft), Budhi Nagin temple on the shore; water fenced, not to be touched</div></div><div class="sza-fact"><div class="k">Price</div><div class="v">Get Quote</div></div></div>
</section>

<section class="sza-sec alt" id="spots">
<span class="sza-kicker">The walk</span>
<h2>What you see on the Serolsar Lake trek</h2>
<p class="sza-lead">The stops on the trail and the extras you can add. Photos show Himalayan forests and lakes in general.</p>
<div class="sza-grid">{cards}</div>
</section>

<section class="sza-sec" id="experience">
<span class="sza-kicker">How the day runs</span>
<h2>Your Serolsar Lake day, step by step</h2>
<ol class="sza-steps">{steps_exp}</ol>
<div class="sza-media"><video autoplay muted loop playsinline preload="none" poster="{UP}serolsar-lake-trek-explainer-poster.webp" width="1600" height="900" aria-label="Route from Jibhi at about 1,600 m by cab about 12 km to Jalori Pass at about 3,120 m, then on foot about 2 km to the 360-degree viewpoint and on to Serolsar Lake at about 3,100 m with the Budhi Nagin temple; about 5 km one way, about 3 hours up and 3 hours back, no camping at the lake; best March to November, in December to February snow we check the road that morning; guide, Jibhi stay and cab; price on quote"><source src="{CDN}explainer.webm" type="video/webm"><source src="{CDN}explainer.mp4" type="video/mp4"></video><div><h3>Jibhi → Jalori → Serolsar</h3><ul><li><b>By cab</b> → Jibhi to Jalori Pass, about 12 km of steep hill road.</li><li><b>On foot</b> → about 2 km to the 360° viewpoint.</li><li><b>On foot</b> → about 3.3 km more to the lake and the Budhi Nagin temple.</li><li><b>Back</b> → the same way; leave the lake by early afternoon.</li></ul></div></div>
</section>

<section class="sza-sec alt" id="season">
<span class="sza-kicker">When to go</span>
<h2>Best time for the Serolsar Lake trek</h2>
<div class="sza-scroll"><table class="sza-tbl"><thead><tr><th>Months</th><th>Trail &amp; road</th><th>What to expect</th></tr></thead><tbody><tr><td>March – April</td><td>Opening, snow patches</td><td>Cold and clear, first flowers; the road reopens after snow clearance</td></tr><tr><td>May – June</td><td>Peak season</td><td>Green forest, busiest weekends</td></tr><tr><td>July – August</td><td>Monsoon</td><td>Rain, leeches, slippery trail; landslides on the hill roads</td></tr><tr><td>September – November</td><td>Best views</td><td>Dry, clear skies; cold mornings from late October</td></tr><tr><td>December – February</td><td>Snow</td><td>Trail iced; the highway over Jalori can close after heavy snow, and often reopens to 4x4 only at first</td></tr></tbody></table></div>
<p style="margin-top:14px">Going in winter? Send your dates — we check the Jalori road that morning and switch you to a Jibhi or Tirthan day if it is shut.</p>
</section>

<div class="sza-band" id="safety"><div class="sza-band-in">
<span class="sza-kicker">Safety</span>
<h2>What we check before we book your walk</h2>
<p class="sza-lead">Suzu Travels is an <a href="https://suzutravels.com/certificates/" style="color:#f3d98f;text-decoration:underline">HP Tourism registered travel agent (Reg. No. DTO-MND-11-243/2022)</a>. We arrange the guide with registered local operators and plan around these checks:</p>
<ul class="sza-checks"><li><b>Road status first</b>In winter we check the Jalori road the same morning; after snowfall the highway is often open to 4x4 only at first, or closed.</li><li><b>Local hill driver</b>No self-drive on the Jibhi–Jalori stretch in snow or ice — a local driver who knows the road.</li><li><b>Guide and spikes in winter</b>Winter walks only with a guide and microspikes; the trail has block ice and drop-offs in places.</li><li><b>Turn-back time</b>Leave the lake by about 3 pm to reach Jalori before dark. Carry 2 litres of water — there is no source until the temple.</li><li><b>Respect the lake</b>No touching the water, no camping by the lake, and carry all litter back.</li><li><b>Warm layers</b>Even in summer — the pass is above 3,000 m and the weather turns fast.</li></ul>
</div></div>

<section class="sza-sec" id="booking">
<span class="sza-kicker">How booking works</span>
<h2>Get a quote in minutes</h2>
<ol class="sza-steps">{booking}</ol>
<div class="sza-media"><img src="{UP}mountain-lake-ringed-by-pine-trees-1024x683.webp" alt="Calm blue mountain lake ringed by pine forest with rocky peaks behind under a blue sky" loading="lazy" width="1024" height="683"><div><h3>What your quote depends on</h3><ul><li>Guide for the walk and the number of walkers</li><li>Cab type (4x4 in snow months) and pickup point — Jibhi, Tirthan, Shimla, Manali or Chandigarh</li><li>Nights in Jibhi or Tirthan and the type of stay — cottage, homestay or treehouse</li><li>Add-ons: Raghupur Fort walk, Jibhi waterfall, a trout-fishing day in Tirthan, a GHNP walk</li><li>Season, and weekend or weekday — today's rate on WhatsApp within minutes</li></ul></div></div>
</section>

{reel}

<section class="sza-quote"><div><span class="sza-kicker">Ready for the forest?</span><h2>Get your Serolsar Lake trek quote</h2><p>Tell us your dates and group size. We reply with one plan — guide, Jibhi stay and the cab — for your dates within minutes.</p></div><div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan full trip</a></div></section>

<section class="sza-sec" id="packages">
<span class="sza-kicker">Make it a trip</span>
<h2>Jibhi + Tirthan + Serolsar Lake</h2>
<p>A good plan is <b>3–4 nights in Jibhi or Tirthan</b>: a cottage by the river, one day for the Serolsar walk, and one for a <a href="/adventure/trout-fishing-in-himachal/">trout-fishing day</a> or a Great Himalayan National Park walk. See our <a href="/jibhi-and-tirthan-valley-itinerary/">Jibhi and Tirthan Valley itinerary</a>, the guides to <a href="/jibhi/">Jibhi</a> and <a href="/tirthan-valley/">Tirthan Valley</a>, or travel <a href="/shimla-to-manali-for-foreigners/">Shimla to Manali via Jalori</a> with one Jibhi night on the way. Want another easy lake walk? Try the <a href="/adventure/prashar-lake-trek/">Prashar Lake trek</a> near Mandi.</p>
<div class="sza-btns" style="margin-top:18px">{walink("Jibhi + Serolsar trip — Get Quote", what="a Jibhi and Tirthan trip with the Serolsar Lake trek")}{walink("Shimla → Jalori → Manali — Get Quote", what="a Shimla to Manali trip via Jalori Pass with one Jibhi night", cls="sza-btn line")}</div>
</section>

<section class="sza-sec sza-faq" id="faq">
<span class="sza-kicker">FAQ</span>
<h2>Serolsar Lake trek — questions</h2>
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
