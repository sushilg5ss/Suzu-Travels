#!/usr/bin/env python3
# Generates adventure-kit/pages/shali-tibba-trek.html (Page Builder night, 25 Nov 2026 IST)
import urllib.parse, pathlib
SLUG = "shali-tibba-trek"
HERE = pathlib.Path(__file__).resolve().parent
CDN = "https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@e39aa9d4c176814df1caab1c782f992ca40310f5/adventure-kit/media/shali-tibba-trek/"
U11 = "https://suzutravels.com/wp-content/uploads/2026/11/"
QUOTE = "/himachal-tour-packages-quote/?activity=" + urllib.parse.quote("Shali Tibba trek")
WHAT = "the Shali Tibba trek near Shimla with cab"

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
    card(f"{U11}suzu-naldehra-mashobra-g-6-768x1155.webp", 768, 1155,
         "Mixed forest on the slopes around Mashobra, Shimla district",
         "Start", "Khatnol village trailhead", "<b>Last road point · beyond Mashobra</b>",
         "The road ends at Khatnol. Park in the village: the short dirt extension beyond has room for only a few cars.",
         "the Shali Tibba trek from Khatnol with cab"),
    card(f"{U11}suzu-naldehra-mashobra-g-3-768x576.webp", 768, 576,
         "Tall deodar trees in a forest near Mashobra",
         "Forest walk", "The 1936 zigzag trail", "<b>~7 km one way · deodar and pine</b>",
         "A zigzag path built in 1936 by the Raja of Faridkot climbs through deodar and pine forest to the top.",
         "the Shali Tibba trek with a local guide"),
    card(f"{U11}shali-mata-temple-shali-tibba-768x571.webp", 768, 571,
         "The Shali Mata (Bhima Kali) temple on top of Shali Tibba",
         "Summit", "Bhima Kali / Shali Mata temple", "<b>About 2,870 m · busy in Navratri</b>",
         "The hilltop temple of Bhima Kali (Shali Mata) sits just above the trail end. Devotees come especially during Navratri.",
         "the Shali Tibba summit trek"),
    card(f"{U11}kinnaur-kullu-himalaya-from-shali-tibba-768x576.webp", 768, 576,
         "Snow ranges of Kinnaur and Kullu seen from the Shali Mata temple",
         "Views", "360° Himalayan panorama", "<b>Kinnaur Kailash to Churdhar</b>",
         "On a clear day the view takes in Kinnaur Kailash, Shrikhand, Deo Tibba, the Kullu ranges and Churdhar.",
         "the Shali Tibba trek for the views"),
    card(f"{U11}suzu-janjehli-shikari-devi-g-2-768x511.webp", 768, 511,
         "Hikers on a snowy slope in a Himalayan fir forest",
         "Seasonal · with guide", "Winter snow day", "<b>Dec–Feb · guide and microspikes</b>",
         "The peak gets heavy snow in winter: a real snow hike close to Shimla. Go only with a local guide and traction.",
         "a winter Shali Tibba snow trek with a local guide"),
    card(f"{U11}shimla-ridges-from-shali-tibba-768x432.webp", 768, 432,
         "Ridges towards Shimla, Kasauli and Churdhar seen from the Shali Mata temple",
         "Package idea", "Shimla + Mashobra stay", "<b>Add Kufri or Narkanda snow</b>",
         "Pair the trek with a night in Mashobra or Shimla, and a Kufri or Narkanda snow day.",
         "a Shimla or Mashobra stay with the Shali Tibba trek, hotel and cab"),
])

steps_exp = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Send your date", "On WhatsApp, with your group size. We plan an early cab from Shimla, Mashobra or Chandigarh, and your stay."),
    ("Drive to Khatnol", "About 2–2.5 hours from Shimla via Dhalli, Mashobra and Baldeyan. Start walking by about 9 am."),
    ("Climb the zigzag trail", "About 7 km and 3–5 hours up through the forest. A local guide is recommended, and essential in snow."),
    ("Bhima Kali temple", "Take in the 360° view and eat your packed lunch: nothing is sold at the top."),
    ("Walk down", "About 2 hours back to Khatnol, well before dusk."),
    ("Onward", "The cab drops you in Shimla or Mashobra, or goes on towards Kufri, Narkanda or Chandigarh."),
])

booking = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Tell us", "WhatsApp or the quote form: date, group size and your pickup point."),
    ("We check your date", "Snow and the road beyond Mashobra, rain, fire season and the best start time."),
    ("You get one quote", "Cab, an optional local guide and your stay: one plan, one rate."),
    ("Confirm and go", "We send the pickup time and what to carry."),
])

season = [
    ("Mar – Jun", "Clear trails, deodar forest and warm days", "Best overall; carry extra water. Apr–Jun is forest-fire season"),
    ("Jul – Sep", "Green and misty; the trail gets slippery", "Clear days only; views often hidden by cloud"),
    ("Oct – Nov", "The sharpest Himalayan views", "Best for photos"),
    ("Dec – Feb", "Snow on the trail and at the top, often deep after storms", "Guide + microspikes; check the Khatnol road after snowfall; turn back in fresh snow"),
]
season_html = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in season)

faqs = [
    ("Where is Shali Tibba?", "It is a peak beyond Mashobra in Shimla district. The road ends at Khatnol village, and the trek starts there."),
    ("How far is Shali Tibba from Shimla?", "Khatnol is roughly 35–48 km from Shimla by road via Dhalli, Mashobra and Baldeyan, about 2–2.5 hours. Sources differ on the exact distance."),
    ("How long is the Shali Tibba trek?", "About 7 km one way from Khatnol. Most hikers take 3–5 hours up and about 2 hours down; that is a planning figure, not a promise."),
    ("How high is Shali Tibba?", "About 2,870 m. The HP trekking portal lists 2,865 m."),
    ("Which temple is at the top?", "The Bhima Kali (Shali Mata) temple. Devotees visit especially during Navratri."),
    ("Is there water or food on the way?", "No. Carry 2–3 litres of water per person and a packed lunch."),
    ("Does it snow at Shali Tibba?", "Yes, the peak gets heavy snow in winter. Trek then only with a local guide and traction, and check the road after snowfall. More snow ideas in our <a href=\"/adventure/winter-treks-in-himachal/\">winter treks guide</a>."),
    ("Can I stay overnight at the top?", "There is no hotel. A basic pilgrim serai near the temple is for emergencies, by permission of the temple caretaker. A same-day trek is the usual plan."),
    ("How much does a Shali Tibba trip cost?", "Get Quote. The rate depends on your pickup point and cab type, a day trip or a night stay, a local guide and group size. WhatsApp your date and we reply with today's rate within minutes."),
]
faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)

more = [
    ("/adventure/karol-tibba-trek/", "⛰️", "Karol Tibba trek", "Solan's highest hill"),
    ("/adventure/churdhar-trek/", "🏔️", "Churdhar trek", "The big trek south of Shimla"),
    ("/adventure/snow-and-skiing-in-narkanda/", "⛷️", "Narkanda snow &amp; skiing", "Snow beyond Shimla"),
    ("/adventure/kufri-adventure-activities/", "❄️", "Kufri activities", "Snow and parks near Shimla"),
    ("/adventure/adventure-activities-in-shimla/", "🧗", "Adventure in Shimla", "Everything around Shimla"),
    ("/adventure/trekking-in-himachal/", "🥾", "Trekking in Himachal", "Every trek in the state"),
]
more_html = "".join(f'<a class="sza-cat" href="{h}"><span class="ic">{i}</span><span class="n">{n}</span><span class="c">{c}</span></a>' for h, i, n, c in more)

reel = (HERE.parent / "media" / SLUG / "reel-section.html").read_text(encoding="utf-8").strip()

page = f'''<!-- shali-tibba-trek — built by Page Builder (night) 25 Nov 2026 IST from the Research Lead brief 24 Nov (Project doc claude/adventure-research/briefs/shali-tibba-trek.md) + Visual Studio media @e39aa9d. Kit v2.0. No prices, no operator names. Not stated (unverified): exact road km, registration rules, temple hours, serai state. Real Shali photos: 25297-25300 (Commons CC0); others generic with neutral alt. -->
<style>.sza-stt .sza-hero-in>*{{max-width:620px}}@media(min-width:901px){{.sza-stt .sza-hero-in>*{{max-width:min(560px,44vw)}}}}.sza-stt .sza-chips{{max-width:700px}}.sza-stt .sza-media ul{{padding-left:20px;list-style:disc;margin:0}}.sza-stt .sza-media ul li{{margin:0 0 8px}}.sza-stt .sza-media img{{height:auto;aspect-ratio:4/3;object-fit:cover}}.sza-stt .sza-media video{{height:auto;aspect-ratio:16/9}}.sza-stt #spots .sza-grid{{grid-template-columns:repeat(auto-fit,minmax(min(340px,100%),1fr))}}.sza-stt .sza-checks{{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}.sza-stt .sza-choose{{margin-top:32px}}.sza-stt .sza-credit{{font-size:13px;opacity:.75;margin-top:18px}}@media(min-width:1000px){{.sza-stt #experience .sza-steps{{grid-template-columns:repeat(3,1fr)}}}}@media(max-width:820px){{.sza-stt .sza-hero video{{object-position:30% 50%}}.sza-stt .sza-hero:after{{background:linear-gradient(180deg,rgba(11,31,51,.45) 0%,rgba(11,31,51,.68) 45%,rgba(11,31,51,.95) 100%)}}}}</style>
<div class="sza sza-stt">
<section class="sza-hero">
<video autoplay muted loop playsinline preload="metadata" poster="{U11}shali-tibba-trek-hero-poster.webp" aria-label="Deodar forest, the Shali Mata temple on the summit and snow ranges seen from it, with a gold zigzag trail from Khatnol village to the Bhima Kali temple at about 2,870 m"><source src="{CDN}hero.webm" type="video/webm"><source src="{CDN}hero.mp4" type="video/mp4"></video>
<div class="sza-hero-in">
<span class="sza-kicker">Shimla district · Khatnol · summit day hike</span>
<p class="sza-hero-tag">The highest viewpoint near Shimla, crowned by Bhima Kali</p>
<p class="sza-hero-sub">A 7 km forest climb from Khatnol village to a hilltop temple with views from Kinnaur Kailash to Churdhar. Suzu plans the early cab from Shimla and the stay.</p>
<ul class="sza-chips"><li><b>~2,870 m</b> summit</li><li><b>Start</b> Khatnol village</li><li><b>~7 km</b> one way</li><li><b>Bhima Kali</b> temple</li><li><b>Snow</b> in winter</li><li><b>Price</b> Get Quote</li></ul>
<div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan my trip</a></div>
<div class="sza-trust"><span><a href="https://suzutravels.com/certificates/">HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022</a></span><span>Himachal-based since 2019</span><span>Reply within minutes</span></div>
</div>
</section>
<nav class="sza-nav" aria-label="On this page"><div class="sza-nav-in"><a href="#overview">Overview</a><a href="#spots">Route &amp; stops</a><a href="#experience">How the day works</a><a href="#season">By month</a><a href="#safety">Safety</a><a href="#booking">How booking works</a><a href="#packages">Make it a trip</a><a href="#faq">FAQ</a><a class="cta" href="{MAIN}" target="_blank" rel="noopener">Get Quote</a></div></nav>

<section class="sza-sec" id="overview">
<span class="sza-kicker">Quick answer</span>
<h2>Shali Tibba trek, at a glance</h2>
<p class="sza-answer">Shali Tibba is a ~2,870 m peak beyond Mashobra, the highest viewpoint near Shimla. The road ends at Khatnol village, roughly 35–48 km from Shimla via Dhalli, Mashobra and Baldeyan. From there a 7 km forest trail, built in 1936, zigzags up to the Bhima Kali (Shali Mata) temple. Allow 3–5 hours up. Carry all your water, and expect snow in winter.</p>
<div class="sza-facts"><div class="sza-fact"><div class="k">Where</div><div class="v">Shali peak above Khatnol village, Shimla district; by road via Dhalli → Mashobra → Baldeyan → Khatnol</div></div><div class="sza-fact"><div class="k">Height</div><div class="v">About 2,870 m (HP trekking portal: 2,865 m)</div></div><div class="sza-fact"><div class="k">Trek</div><div class="v">About 7 km one way from Khatnol; 3–5 hours up, ~2 hours down; easy to moderate</div></div><div class="sza-fact"><div class="k">At the top</div><div class="v">The Bhima Kali (Shali Mata) temple, a basic pilgrim serai and a 360° Himalayan view</div></div><div class="sza-fact"><div class="k">Season</div><div class="v">Mar–Dec for clear trails; Dec–Feb snow, go only with a guide and traction</div></div><div class="sza-fact"><div class="k">Price</div><div class="v">Get Quote</div></div></div>
<div class="sza-media" style="margin-top:28px"><img src="{U11}shali-mata-temple-shali-tibba-768x571.webp" alt="The Shali Mata (Bhima Kali) temple on top of Shali Tibba" loading="lazy" width="768" height="571"><div><h3>Is Shali Tibba for you?</h3><ul><li><b>Want the best full-day trek near Shimla</b> → this is the highest viewpoint around, with a real summit.</li><li><b>First trek</b> → yes in Mar–Nov, if you are fit for 3–5 hours of steady climbing.</li><li><b>Want snow</b> → Dec–Feb, with a local guide and microspikes; also see <a href="/adventure/snow-and-skiing-in-narkanda/">Narkanda</a> and <a href="/adventure/kufri-adventure-activities/">Kufri</a>.</li><li><b>Pilgrim</b> → the Bhima Kali temple is busiest in Navratri.</li></ul><p>More around Shimla: <a href="/things-to-do-in-shimla/">things to do in Shimla</a>, <a href="/shimla-tourist-places/">Shimla tourist places</a> and <a href="/hatu-peak-narkanda/">Hatu Peak</a>.</p></div></div>
</section>

<section class="sza-sec alt" id="spots">
<span class="sza-kicker">Route &amp; stops</span>
<h2>From Khatnol to the Bhima Kali temple</h2>
<p class="sza-lead">Park at Khatnol, climb the 1936 zigzag trail through the forest, and finish at the hilltop temple with a 360° view.</p>
<div class="sza-grid">{cards}</div>
<div class="sza-media sza-choose" id="route"><video autoplay muted loop playsinline preload="none" poster="{U11}shali-tibba-trek-explainer-poster.webp" width="1600" height="900" aria-label="Schematic map: Shimla to Dhalli, Mashobra, Baldeyan and Khatnol, roughly 35 to 48 km and 2 to 2.5 hours by cab, then a 7 km zigzag trail to the temple at about 2,870 m; a 360 degree compass ring; month strip; no water on the trail, carry 3 litres"><source src="{CDN}explainer.webm" type="video/webm"><source src="{CDN}explainer.mp4" type="video/mp4"></video><div><h3>Shimla → Khatnol → Shali Tibba</h3><ul><li><b>Shimla</b> → roughly 35–48 km, ~2–2.5 hours by cab.</li><li><b>Dhalli, Mashobra, Baldeyan</b> → the road route.</li><li><b>Khatnol</b> → the trailhead and parking.</li><li><b>Zigzag forest trail</b> → about 7 km, 3–5 hours up.</li><li><b>Bhima Kali temple</b> → the summit, about 2,870 m.</li></ul><p>Schematic, not to scale.</p></div></div>
</section>

<section class="sza-sec" id="experience">
<span class="sza-kicker">How the day works</span>
<h2>A Shali Tibba day with Suzu, step by step</h2>
<ol class="sza-steps">{steps_exp}</ol>
<div class="sza-media"><img src="{U11}suzu-naldehra-mashobra-g-3-768x576.webp" alt="Tall deodar trees in a forest near Mashobra" loading="lazy" width="768" height="576"><div><h3>What to carry</h3><ul><li>2–3 litres of water per person: no water on the trail or at the top</li><li>A packed lunch and snacks</li><li>Shoes with good grip and a warm layer</li><li>In winter: microspikes, gloves and a proper jacket</li><li>A rain shell in the monsoon</li></ul><p>Polythene is banned in Himachal: take all your waste back down.</p></div></div>
</section>

<section class="sza-sec alt" id="season">
<span class="sza-kicker">When to go</span>
<h2>Shali Tibba by month</h2>
<div class="sza-scroll"><table class="sza-tbl"><thead><tr><th>Months</th><th>What you get</th><th>Note</th></tr></thead><tbody>{season_html}</tbody></table></div>
<div class="sza-media" style="margin-top:28px"><img src="{U11}dhauladhar-from-shali-tibba-768x432.webp" alt="The Dhauladhar range seen from the Shali Mata temple" loading="lazy" width="768" height="432"><div><h3>Winter on Shali Tibba</h3><p>Dec–Feb brings real snow to the trail and the top, often deep after a storm, so the path is hard to follow. Go only with a local guide and microspikes, skip it during and right after a storm, and check the road beyond Mashobra after snowfall.</p><p>More snow ideas: <a href="/adventure/winter-treks-in-himachal/">winter treks in Himachal</a> and all <a href="/adventure/trekking-in-himachal/">trekking in Himachal</a>.</p></div></div>
</section>

<div class="sza-band" id="safety"><div class="sza-band-in">
<span class="sza-kicker">Safety</span>
<h2>What we check before your Shali Tibba trek</h2>
<p class="sza-lead">Suzu Travels is an <a href="https://suzutravels.com/certificates/" style="color:#f3d98f;text-decoration:underline">HP Tourism registered travel agent (Reg. No. DTO-MND-11-243/2022)</a>. We arrange local guides with registered local operators and plan around these checks:</p>
<ul class="sza-checks"><li><b>Carry your water</b>There is no water on the trail or at the top. Carry 2–3 litres per person and a packed lunch.</li><li><b>Never alone, down before dusk</b>Dense forest with no houses, and wildlife lives here. Trek in a group and be back at Khatnol before dark.</li><li><b>Snow needs a guide</b>In winter the trail is snow-covered and hard to follow. Local guide and microspikes only; skip it in or right after a storm.</li><li><b>Lightning</b>The open hilltop attracts lightning. Come down if clouds build up in the afternoon.</li><li><b>Monsoon and fire season</b>Jul–Sep the path is slippery; Apr–Jun is fire season. Check local news and never light a fire.</li><li><b>Leave no trace</b>Polythene is banned; don't litter, and don't feed or approach wild animals.</li></ul>
</div></div>

<section class="sza-sec" id="booking">
<span class="sza-kicker">How booking works</span>
<h2>Get a quote in minutes</h2>
<ol class="sza-steps">{booking}</ol>
<div class="sza-media"><img src="{U11}shimla-ridges-from-shali-tibba-768x432.webp" alt="Ridges towards Shimla, Kasauli and Churdhar seen from the Shali Mata temple" loading="lazy" width="768" height="432"><div><h3>What your quote depends on</h3><ul><li>Pickup point (Shimla, Mashobra, Kufri, Chandigarh) and cab type</li><li>A day trip, or a night in Mashobra or Shimla before the trek</li><li>A local guide (recommended; essential in snow) and winter traction gear, arranged on request</li><li>Season and the road beyond Mashobra after snowfall</li><li>Group size</li><li>Add-ons: Kufri or Narkanda snow day, Jakhu ropeway, ice skating in Shimla, Hatu Peak</li></ul><p>We send today's rate on WhatsApp within minutes.</p></div></div>
</section>

{reel}

<section class="sza-quote"><div><span class="sza-kicker">Ready for Shimla's highest view?</span><h2>Get your Shali Tibba quote</h2><p>Tell us your date and group size. We reply with one plan (cab, guide and stay) within minutes.</p></div><div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan full trip</a></div></section>

<section class="sza-sec" id="packages">
<span class="sza-kicker">Make it a trip</span>
<h2>Add Shali Tibba to a Shimla winter weekend</h2>
<p>A good plan is two nights in Shimla or Mashobra: the Shali Tibba trek one day and a <a href="/adventure/kufri-adventure-activities/">Kufri</a> or <a href="/adventure/snow-and-skiing-in-narkanda/">Narkanda snow day</a> the next. Add the <a href="/adventure/jakhu-ropeway-shimla/">Jakhu ropeway</a> or <a href="/adventure/ice-skating-shimla/">ice skating in Shimla</a>. Coming from the plains? See the drive <a href="/chandigarh-to-shimla/">Chandigarh to Shimla</a>.</p>
<div class="sza-btns" style="margin-top:18px">{walink("2N Shimla winter weekend — Get Quote", what="a 2-night Shimla winter trip with the Shali Tibba trek, a snow day, hotel and cab")}{walink("Day trek from Shimla — Get Quote", what="a Shali Tibba day trek from Shimla with cab", cls="sza-btn line")}</div>
<p class="sza-credit">Temple and summit photos: 502hsuya via Wikimedia Commons (CC0). Snowy forest photo: Kai Chongloi, <a href="https://creativecommons.org/licenses/by-sa/4.0">CC BY-SA 4.0</a> (Wikimedia Commons).</p>
</section>

<section class="sza-sec sza-faq" id="faq">
<span class="sza-kicker">FAQ</span>
<h2>Shali Tibba trek — questions</h2>
{faq_html}
</section>

<section class="sza-sec alt" id="more">
<span class="sza-kicker">More adventures</span>
<h2>Explore more near Shimla</h2>
<div class="sza-cats">{more_html}</div>
</section>
</div>
'''
out = HERE / f"{SLUG}.html"
out.write_text(page, encoding="utf-8")
print(len(page))
