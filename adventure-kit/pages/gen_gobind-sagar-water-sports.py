#!/usr/bin/env python3
# Generates adventure-kit/pages/gobind-sagar-water-sports.html (Page Builder night, 22 Oct 2026 IST)
import urllib.parse, pathlib
SLUG = "gobind-sagar-water-sports"
HERE = pathlib.Path(__file__).resolve().parent
CDN = "https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@11e39fce3c679fd7decbe9f7b5abfe36ab7dcfa9/adventure-kit/media/gobind-sagar-water-sports/"
UP = "https://suzutravels.com/wp-content/uploads/2026/10/"
QUOTE = "/himachal-tour-packages-quote/?activity=" + urllib.parse.quote("Water sports")
WHAT = "boating / water sports at Gobind Sagar Lake, Bilaspur"

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
    card(f"{UP}jet-ski-on-hill-lake-at-sunset-768x512.webp", 768, 512,
         "Jet ski cutting a white wake across a wide hill lake at sunset, pine trees in front",
         "Main boating point", "Mandi Bharari jetty", "<b>Boat rides · jet skis · water scooters</b>",
         "Where the state launched jet skis, shikaras and a cruise-style boat on 29 Oct 2024. What runs on your date is confirmed locally.",
         "a boat ride or jet ski at Mandi Bharari, Gobind Sagar Lake"),
    card(f"{UP}two-kayakers-lake-hazy-hills-768x510.webp", 768, 510,
         "Two kayakers on a still lake below layers of hazy hills",
         "Sports base", "Luhnu ground, Bilaspur town", "<b>Lake shore below Bandla</b>",
         "The lake's sports base: an NCC sailing expedition started here on 9 Sep 2026 and a 30-day youth water-sports camp ran in Oct 2026.",
         "water sports at Luhnu, Bilaspur town"),
    card(f"{UP}tandem-paraglider-over-lake-hazy-mountains-768x1152.webp", 768, 1152,
         "Tandem paraglider with an orange wing flying over a lake between hazy mountains",
         "Same-day combo", "Fly Bandla + boat the lake", "<b>Flight lands at Luhnu, by the water</b>",
         "A morning tandem flight from Bandla Dhar, then a boat or jet-ski ride the same day, weather permitting.",
         "a Bandla tandem flight plus a boat ride on Gobind Sagar the same day", "/adventure/paragliding-in-bilaspur/"),
    card(f"{UP}old-stone-shrine-reflected-in-water-768x988.webp", 768, 988,
         "Old stone shrine on a grassy bank, reflected in still water",
         "Low-water months", "Sunken temples of old Bilaspur", "<b>Show when the water falls</b>",
         "Old Bilaspur went under the lake in the late 1950s; the Ranganath and Khanmukeshwar shrines surface as the level drops.",
         "a Gobind Sagar visit to see the sunken temples of old Bilaspur"),
    card(f"{UP}speed-boat-white-wake-lake-from-above-768x1227.webp", 768, 1227,
         "Speed boat seen from above, leaving a long white wake on dark blue water",
         "Ask first", "Kol Dam reservoir", "<b>Upstream on the Sutlej</b>",
         "Water sports were launched here on 11 Apr 2025, but what runs varies — we check before you plan around it.",
         "water sports at Kol Dam, Bilaspur"),
    card(f"{UP}kayak-silhouette-lake-moonrise-768x432.webp", 768, 432,
         "Kayaker silhouetted on a mirror-still lake as a full moon rises over blue hills",
         "Coming, not open", "Andarauli cruise (Una side)", "<b>Overnight cruise + water-sports project</b>",
         "Not running yet: its third tender drew one bidder on 14 Oct 2026 and is being re-invited. Ride at Mandi Bharari instead.",
         "boating on Gobind Sagar (Andarauli side, Una)"),
])

steps_exp = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Send your date", "Date and group on WhatsApp — we check the water level, weather and what is running that week."),
    ("Cab pick-up", "From Chandigarh, Shimla, Naina Devi, your Bilaspur hotel or Ghumarwin."),
    ("Optional: fly first", "A morning <a href=\"/adventure/paragliding-in-bilaspur/\">Bandla tandem flight</a>, landing at Luhnu by the lake."),
    ("At the jetty", "Life jacket on, safety briefing, then the boat, jet-ski or water-scooter ride."),
    ("Low-water months", "Walk or drive to the sunken-temple shore with your driver's guidance."),
    ("Lunch, then on", "To <a href=\"/pilgrimage-tours/naina-devi/\">Naina Devi</a>, on up the four-lane to Manali, or back to your hotel."),
])

booking = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
    ("Tell us", "WhatsApp or the quote form — date, group size, kids' ages and where you start."),
    ("We check your date", "Water level, weather, district advisories and a registered local operator."),
    ("You get one quote", "Lake ride, any Bandla flight, hotel nights and cab in one plan."),
    ("Confirm and go", "We send the jetty, the meeting time and what to carry."),
])

season = [
    ("Aug – Sep", "Rising to full", "Search peak; monsoon alerts and dam releases (Kol Dam releases in Aug 2026 came with river warnings) — boats only when the district allows"),
    ("Oct – Jan", "High", "Best boating; cool, clear days. Naina Devi is busy in Navratri weeks"),
    ("Feb – Jun", "Falling to lowest", "Sunken temples surface; boating depends on the level and the jetty; hot from May"),
    ("Jul", "Monsoon", "Check the day's district (DDMA) advisory before you go"),
]
season_html = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in season)

faqs = [
    ("Where is Gobind Sagar Lake?", "It is the reservoir behind the Bhakra Dam on the Sutlej, in Bilaspur and Una districts of Himachal. Bilaspur town sits on its shore, about 85 km from Shimla and 135 km from Chandigarh."),
    ("What water sports can I do at Gobind Sagar?", "The state launched boat rides, jet skis, water scooters, shikaras and a cruise-style boat at Mandi Bharari on 29 Oct 2024. What runs on a given day depends on the water level and the operator — we confirm it for your date."),
    ("When is the best time for boating?", "August to January, when the lake is high. October to January also has the most comfortable weather."),
    ("When can I see the sunken temples?", "When the water recedes, from winter into early summer. The temples of old Bilaspur, drowned in the late 1950s, include the Ranganath and Khanmukeshwar shrines."),
    ("Is a life jacket compulsory?", "Yes. Since the DC Bilaspur order of 2 May 2026, nobody may take part in any water activity on Gobind Sagar or Kol Dam without a standard life jacket."),
    ("Is there a cruise on Gobind Sagar?", "A cruise-style motorboat was launched in 2024. The larger overnight-cruise project at Andarauli (Una side) is not running; its tender is being re-invited after 14 Oct 2026."),
    ("Can I fly at Bandla and go boating the same day?", "Yes. <a href=\"/adventure/paragliding-in-bilaspur/\">Bandla tandem flights</a> land at Luhnu on the lake shore, so a morning flight and a ride fit in one day, weather permitting."),
    ("Are there water sports at Kol Dam too?", "Water sports were launched at Kol Dam on 11 Apr 2025 and the May 2026 safety order covers it, but operations vary. Ask us before you plan around it."),
]
faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)

more = [
    ("/adventure/paragliding-in-bilaspur/", "🪂", "Paragliding in Bilaspur", "Bandla Dhar, above the lake"),
    ("/adventure/rafting-in-shimla-tattapani/", "🚣", "Rafting at Tattapani", "Sutlej, near Shimla"),
    ("/adventure/river-rafting-in-kullu-manali/", "🌊", "River rafting", "Beas, Kullu–Manali"),
    ("/adventure/camping-in-himachal/", "⛺", "Camping in Himachal", "Where to camp this month"),
    ("/adventure/paragliding-in-himachal/", "🗺️", "Paragliding sites", "Which site for your trip"),
    ("/adventure/", "🧭", "All adventures", "Air · Water · Snow · Land"),
]
more_html = "".join(f'<a class="sza-cat" href="{h}"><span class="ic">{i}</span><span class="n">{n}</span><span class="c">{c}</span></a>' for h, i, n, c in more)

reel = (HERE.parent / "media" / SLUG / "reel-section.html").read_text(encoding="utf-8").strip()

page = f'''<!-- gobind-sagar-water-sports — built by Page Builder (night) 22 Oct 2026 IST from the Research Lead brief 21 Oct (morning) + Visual Studio media @11e39fc (reel-section @5dcedb1). Kit v1.8. No prices, no operator names. Unverified items left off: which rides run today at each jetty, timings, operators, whether the shikara/cruise boat still runs in 2026, exact temple months, water-level figures, Bhakra photography rule, reservoir size, fish/birds. Generic photos carry neutral alt text (never "Gobind Sagar"). -->
<style>.sza-gsw .sza-hero-in>*{{max-width:620px}}.sza-gsw .sza-chips{{max-width:700px}}.sza-gsw .sza-media ul{{padding-left:20px;list-style:disc;margin:0}}.sza-gsw .sza-media ul li{{margin:0 0 8px}}.sza-gsw .sza-media img{{height:auto;aspect-ratio:3/2;object-fit:cover}}.sza-gsw .sza-media video{{height:auto;aspect-ratio:16/9}}.sza-gsw #spots .sza-grid{{grid-template-columns:repeat(auto-fit,minmax(min(300px,100%),1fr))}}.sza-gsw #spots .sza-card .img img{{aspect-ratio:3/2;object-fit:cover}}.sza-gsw .sza-checks{{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}.sza-gsw .sza-choose{{margin-top:32px}}@media(max-width:820px){{.sza-gsw .sza-hero video{{object-position:30% 50%}}.sza-gsw .sza-hero:after{{background:linear-gradient(180deg,rgba(11,31,51,.35) 0%,rgba(11,31,51,.6) 40%,rgba(11,31,51,.94) 100%)}}}}</style>
<div class="sza sza-gsw">
<section class="sza-hero">
<video autoplay muted loop playsinline preload="metadata" poster="{UP}gobind-sagar-lake-rides-hero-poster.webp" aria-label="A calm lake at dusk, a jet ski on the water and riders in orange life jackets on a boat, with a lake cross-section whose gold water line falls from high water (August to January) to low water when old temples show, and rises again"><source src="{CDN}hero.webm" type="video/webm"><source src="{CDN}hero.mp4" type="video/mp4"></video>
<div class="sza-hero-in">
<span class="sza-kicker">Water · Bilaspur · our home district</span>
<p class="sza-hero-tag">Boat rides, jet skis and sunken temples on the Bhakra lake</p>
<p class="sza-hero-sub">Jetties at Mandi Bharari and Luhnu near Bilaspur town — we add the ride to your cab, hotel, Naina Devi and Bandla plan.</p>
<ul class="sza-chips"><li><b>Bilaspur</b> district</li><li><b>~85 km</b> from Shimla · ~135 km from Chandigarh</li><li><b>Life jacket</b> compulsory</li><li><b>Best water</b> Aug–Jan</li><li><b>Temples show</b> when water falls</li><li><b>Price</b> Get Quote</li></ul>
<div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan my trip</a></div>
<div class="sza-trust"><span><a href="https://suzutravels.com/certificates/">HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022</a></span><span>Lake ride + hotel + cab</span><span>Reply within minutes</span></div>
</div>
</section>
<nav class="sza-nav" aria-label="On this page"><div class="sza-nav-in"><a href="#overview">Overview</a><a href="#spots">Where to ride</a><a href="#experience">Your lake day</a><a href="#season">By month</a><a href="#safety">Rules &amp; safety</a><a href="#booking">How booking works</a><a href="#packages">Packages</a><a href="#faq">FAQ</a><a class="cta" href="{MAIN}" target="_blank" rel="noopener">Get Quote</a></div></nav>

<section class="sza-sec" id="overview">
<span class="sza-kicker">Quick answer</span>
<h2>Gobind Sagar Lake, at a glance</h2>
<p class="sza-answer">Gobind Sagar is the reservoir behind the Bhakra Dam on the Sutlej, spread along Bilaspur and Una districts. Boat rides, jet skis and water scooters run from the Mandi Bharari side, launched by the state on 29 Oct 2024, and Luhnu ground by Bilaspur town is the lake's sports base. Water is highest Aug–Jan; when it falls, the sunken temples of old Bilaspur appear. A life jacket is compulsory.</p>
<div class="sza-facts"><div class="sza-fact"><div class="k">Where</div><div class="v">Bhakra reservoir at Bilaspur town and Mandi Bharari, Bilaspur district; the lake runs on into Una district</div></div><div class="sza-fact"><div class="k">Getting there</div><div class="v">~85 km from Shimla, ~135 km from Chandigarh; nearest broad-gauge station Kiratpur Sahib (~65 km)</div></div><div class="sza-fact"><div class="k">What runs</div><div class="v">Boat rides, jet skis, water scooters (shikara and a cruise-style boat launched 2024) — confirmed locally for your date</div></div><div class="sza-fact"><div class="k">Best water</div><div class="v">Aug–Jan (high); temples show as the level drops, winter to early summer</div></div><div class="sza-fact"><div class="k">Rules</div><div class="v">Life jacket for every rider, capacity shown, certified crew (DC Bilaspur order, 2 May 2026)</div></div><div class="sza-fact"><div class="k">Price</div><div class="v">Get Quote</div></div></div>
</section>

<section class="sza-sec alt" id="spots">
<span class="sza-kicker">Where to ride</span>
<h2>Boating points and things to see on the lake</h2>
<p class="sza-lead">Mandi Bharari is the main boating point and Luhnu the sports base. Kol Dam varies, and the Andarauli cruise is not open yet.</p>
<div class="sza-grid">{cards}</div>
<div class="sza-media sza-choose" id="lake-level"><video autoplay muted loop playsinline preload="none" poster="{UP}gobind-sagar-fly-bandla-then-boat-explainer.webp" width="1600" height="900" aria-label="Motion graphic: Gobind Sagar water level by month, high from August to January for boat rides and jet skis, low from February to June when old temples show; then a gold paragliding line from the Bandla Dhar take-off to the Luhnu landing and water-sports base, and a boat heading to the Mandi Bharari boating jetty; 28 temples went under, life jacket for every rider, price on quote"><source src="{CDN}explainer.webm" type="video/webm"><source src="{CDN}explainer.mp4" type="video/mp4"></video><div><h3>The lake that rises and falls</h3><ul><li><b>High water, Aug–Jan</b> → boat rides and jet skis.</li><li><b>Low water, Feb–Jun</b> → the old temples show.</li><li><b>Fly Bandla</b> → land at Luhnu, right on the shore.</li><li><b>Ride</b> → the main jetty is at Mandi Bharari.</li></ul><p>We check the level and what runs before we book.</p></div></div>
<figure id="bandla-flight" style="margin:32px auto 0;max-width:880px"><video poster="https://suzutravels.com/wp-content/uploads/2026/10/your-bandla-flight-paragliding-explainer.webp" autoplay muted loop playsinline preload="none" width="1600" height="900" style="display:block;width:100%;height:auto;aspect-ratio:16/9;border-radius:18px;background:#0b1f33;box-shadow:0 12px 32px rgba(11,31,51,.2)" aria-label="Motion graphic: Your Bandla flight. Side profile with the take-off on Bandla Dhar, a gold flight line over Bilaspur town to the Luhnu landing by Gobind Sagar; month bar with the flying season, fair-weather months and the monsoon closure; 12+ years and 30 kg+, tandem with a registered pilot, price on quote"><source src="https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@42b05458773c70452c027435a817a971c15c1a2d/adventure-kit/media/paragliding-in-bilaspur/explainer.webm" type="video/webm"><source src="https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@42b05458773c70452c027435a817a971c15c1a2d/adventure-kit/media/paragliding-in-bilaspur/explainer.mp4" type="video/mp4"></video><figcaption style="margin-top:12px;font-size:15px;line-height:1.5;color:#5b6975;text-align:center"><b style="color:#0b1f33">See the lake from the air first:</b> a tandem flight from Bandla Dhar over Bilaspur town lands at the Luhnu ground on the Gobind Sagar shore, with a registered pilot (12+ years, 30 kg+). <a href="/adventure/paragliding-in-bilaspur/" style="color:#0b1f33;font-weight:700">See the Bandla paragliding guide →</a></figcaption></figure>
</section>

<section class="sza-sec" id="experience">
<span class="sza-kicker">Your lake day</span>
<h2>How a Gobind Sagar day works</h2>
<ol class="sza-steps">{steps_exp}</ol>
<div class="sza-media"><img src="{UP}boat-ride-orange-life-jackets-lake-768x768.webp" alt="Small boat with riders in orange life jackets on a green lake beside a wooded shore" loading="lazy" width="768" height="768"><div><h3>What to wear and carry</h3><p>Light clothes, a cap and sunscreen (it is hot from May), shoes you can get wet, and a dry bag for phones. Everyone wears a life jacket — sizes for kids are part of the rules.</p><p>Many guests pair the lake with <a href="/pilgrimage-tours/naina-devi/">Naina Devi</a> darshan above the reservoir, or with the <a href="/pilgrimage-tours/nau-devi-yatra/">Nau Devi yatra</a> and <a href="/pilgrimage-tours/chintpurni/">Chintpurni</a>.</p></div></div>
</section>

<section class="sza-sec alt" id="season">
<span class="sza-kicker">When to go</span>
<h2>Gobind Sagar by month</h2>
<div class="sza-scroll"><table class="sza-tbl"><thead><tr><th>Months</th><th>Water</th><th>What to expect</th></tr></thead><tbody>{season_html}</tbody></table></div>
<p style="margin-top:14px">Weekends, Navratri and holiday weeks are busiest — a weekday gives you a shorter wait at the jetty.</p>
</section>

<div class="sza-band" id="safety"><div class="sza-band-in">
<span class="sza-kicker">Rules &amp; safety</span>
<h2>The Bilaspur lake rules we check before we book</h2>
<p class="sza-lead">Suzu Travels is an <a href="https://suzutravels.com/certificates/" style="color:#f3d98f;text-decoration:underline">HP Tourism registered travel agent (Reg. No. DTO-MND-11-243/2022)</a>. We arrange lake rides with registered local operators and check these first:</p>
<ul class="sza-checks"><li><b>Life jacket for every person</b>The DC Bilaspur / DDMA order of 2 May 2026 for Gobind Sagar and Kol Dam bars entry to any water activity without a standard life jacket.</li><li><b>Gear and capacity</b>Lifebuoys, ropes and first aid on every boat; seating capacity painted on each boat, no overloading; engines matched to seats.</li><li><b>Trained crew</b>Boat drivers, instructors and lifeguards must hold swimming, rescue and first-aid certificates, and give a safety briefing before every trip.</li><li><b>Marked danger zones</b>High-risk zones carry boards and are closed to activities; breaking the order brings penalties under the Disaster Management Act, 2005.</li><li><b>Registered operators</b>Water sports come under the HP Water Sports and Allied Activities Rules, 2021. In Sep 2024 the High Court stopped one Kol Dam operator whose power-boat driver lacked the required certificate — we use only registered local operators.</li><li><b>Kids</b>Life jackets come in kids' sizes under the order; keep small children seated and nobody swims off the boats.</li></ul>
</div></div>

<section class="sza-sec" id="booking">
<span class="sza-kicker">How booking works</span>
<h2>Get a quote in minutes</h2>
<ol class="sza-steps">{booking}</ol>
<div class="sza-media"><img src="{UP}wide-calm-lake-hills-dusk-768x432.webp" alt="Wide, calm lake reflecting a pink and gold dusk sky, with a low line of hills on the far shore" loading="lazy" width="768" height="432"><div><h3>What your quote depends on</h3><ul><li>Which ride — boat, jet ski, water scooter — and how many riders</li><li>Date: weekends, Navratri and holiday weeks are busier</li><li>Adding a Bandla tandem flight (and video)</li><li>Cab type, pick-up point and onward drive (Manali four-lane)</li><li>Hotel nights in Bilaspur or near Naina Devi, and meal plan</li><li>Adding Kol Dam or Naina Devi darshan</li></ul><p>We send today's rate on WhatsApp within minutes.</p></div></div>
</section>

{reel}

<section class="sza-quote"><div><span class="sza-kicker">Ready for the lake?</span><h2>Get your Gobind Sagar quote</h2><p>Tell us your date and who is riding. We reply with one plan — lake ride, hotel and cab — within minutes.</p></div><div class="sza-btns">{walink("Get Quote on WhatsApp")}<a class="sza-btn ghost" href="{QUOTE}">Plan full trip</a></div></section>

<section class="sza-sec" id="packages">
<span class="sza-kicker">Make it a trip</span>
<h2>A Naina Devi + Bilaspur lake weekend</h2>
<p>The easy way to do it: from Chandigarh, <b>Naina Devi darshan → Bandla flight → Gobind Sagar ride → a night in Bilaspur</b>, with hotel and cab in one quote. Or make the lake a stop on the Chandigarh–Manali drive — book a <a href="/cabs/chandigarh-to-manali-taxi/">Chandigarh to Manali taxi</a> or see <a href="/cabs/">all our cabs</a>. Coming from Shimla? See <a href="/destination/shimla-tour-packages/">Shimla tour packages</a>, or go downstream on the Sutlej for <a href="/adventure/rafting-in-shimla-tattapani/">rafting at Tattapani</a>. For a night out by the water, see <a href="/adventure/camping-in-himachal/">camping in Himachal</a>.</p>
<div class="sza-btns" style="margin-top:18px">{walink("Naina Devi + lake weekend — Get Quote", what="a Naina Devi + Bilaspur lake weekend from Chandigarh (darshan, Bandla flight, Gobind Sagar ride, hotel and cab)")}{walink("Lake stop on the Manali drive — Get Quote", what="a Gobind Sagar lake stop on a Chandigarh to Manali cab trip", cls="sza-btn line")}</div>
</section>

<section class="sza-sec sza-faq" id="faq">
<span class="sza-kicker">FAQ</span>
<h2>Gobind Sagar Lake — questions</h2>
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
