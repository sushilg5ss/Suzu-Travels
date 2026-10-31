import urllib.parse as U, pathlib
CDN="https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@61742fd28a6632b9d4e777392a1cda8e02d8b69e/adventure-kit/media/chanshal-pass/"
UP="https://suzutravels.com/wp-content/uploads/2026/10/"
def wa(what):
    return "https://wa.me/917087488961?text="+U.quote(f"Hi Suzu Travels, I want a quote for {what}. Travel date: ___ , people: ___ (page: chanshal-pass)",safe="")
Q="/himachal-tour-packages-quote/?activity=Chanshal%20Pass"
MAIN=wa("a Chanshal Pass trip (Rohru, Shimla)")
def card(img,w,h,alt,badge,title,meta,txt,what):
    return f'<article class="sza-card"><div class="img"><img src="{UP}{img}" alt="{alt}" loading="lazy" width="{w}" height="{h}"><span class="sza-badge">{badge}</span></div><div class="body"><h3>{title}</h3><div class="meta"><b>{meta}</b></div><p class="meta">{txt}</p><div class="go"><a class="q" href="{wa(what)}" target="_blank" rel="noopener">Get Quote →</a></div></div></article>'
cards="".join([
 card("green-meadow-below-snow-peaks-768x432.webp",768,432,"Open green meadow and conifer forest below rocky snow-capped peaks under a deep blue sky","The pass","Chanshal top","About 3,750 m","Wide high meadows with snow patches often lasting into June, and views over the Pabbar valley side. Nothing to stay or eat at the top.","a Chanshal Pass day trip to the top"),
 card("aerial-hairpin-bends-forest-mountain-road-768x432.webp",768,432,"Aerial view of a mountain road looping through hairpin bends across a forested green slope","Last stop","Larot","Last village before the climb","The final village below the pass, with basic homestays. Above it the road gets rough, rocky and steep.","a Chanshal Pass trip with a stay at Larot"),
 card("cars-on-pine-forest-mountain-road-768x512.webp",768,512,"Cars on a narrow mountain road through a pine forest","Base","Rohru &amp; the Pabbar valley","Base town with the most hotels","Rohru on the Pabbar river is where most trips stay the night before an early start for the pass. Last fuel stop too.","a Chanshal Pass trip with hotel nights in Rohru"),
 card("car-winding-road-green-mountain-valley-768x512.webp",768,512,"A white car on a winding road with tight bends through a steep green mountain valley","En route","Hatkoti temple","On the Kharapathar–Hatkoti road","The Hatkoti temple sits on the way down to Rohru when you take the Kharapathar road from Shimla — a good stop on day 1.","a Shimla to Chanshal Pass trip via Hatkoti"),
 card("4x4-on-gravel-mountain-road-768x512.webp",768,512,"A dark 4x4 driving up a gravel mountain road between dry hills, a small village on the slope behind","Explorers","Dodra Kwar","Remote valley beyond the pass","Dodra and Kwar lie on the far side of Chanshal. The road beyond the pass is seasonal and often not motorable — we check before you plan it.","a Chanshal Pass and Dodra Kwar trip"),
 card("grassy-slope-below-rocky-himalayan-ridge-768x1058.webp",768,1058,"Grassy high-altitude slope below a steep rocky mountain ridge and white clouds in Himachal Pradesh","Trekkers","Chanshal trek","Larot → pass → Kwar on foot","A multi-day trek with camps over the pass to Kwar, best in May–June and mid-September–October. Guide and camps arranged on request.","the Chanshal Pass trek (Larot to Kwar)"),
])
reel=pathlib.Path('/root/ak/adventure-kit/media/chanshal-pass/reel-section.html').read_text().strip()
html=f'''<!-- chanshal-pass — built by Page Builder (night) 1 Nov 2026 from the Research Lead brief 31 Oct + Visual Studio media @61742fd (reel-section @a7f0303). Kit v1.8. No prices, no operator names; unverified items (forest permit, hairpin count, exact Larot→top km, Dodra Kwar road dates, bus service) kept off the page. Photos generic, neutral alt. -->
<style>.sza-chs .sza-hero-in>*{{max-width:620px}}.sza-chs .sza-chips{{max-width:700px}}.sza-chs #experience .sza-steps{{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}.sza-chs .sza-media ul{{padding-left:20px;list-style:disc;margin:0}}.sza-chs .sza-media ul li{{margin:0 0 8px}}.sza-chs .sza-media img{{height:auto;aspect-ratio:4/3;object-fit:cover}}.sza-chs .sza-media video{{height:auto;aspect-ratio:16/9}}.sza-chs #spots .sza-grid{{grid-template-columns:repeat(auto-fit,minmax(min(340px,100%),1fr))}}.sza-chs #spots .sza-card .img img{{aspect-ratio:3/2;object-fit:cover}}.sza-chs .sza-checks{{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}@media(max-width:820px){{.sza-chs .sza-hero video{{object-position:20% 50%}}.sza-chs .sza-hero:after{{background:linear-gradient(180deg,rgba(11,31,51,.35) 0%,rgba(11,31,51,.6) 40%,rgba(11,31,51,.94) 100%)}}}}</style>
<div class="sza sza-chs">
<section class="sza-hero">
<video autoplay muted loop playsinline preload="metadata" poster="{UP}chanshal-pass-hero-poster.webp" aria-label="A car on a winding green valley road, hairpin bends from above, a meadow below snow peaks and a high grassy ridge, with a gold road line from Rohru up to Chanshal Pass at about 3,750 m"><source src="{CDN}hero.webm" type="video/webm"><source src="{CDN}hero.mp4" type="video/mp4"></video>
<div class="sza-hero-in">
<span class="sza-kicker">Shimla district · Land &amp; Rides</span>
<p class="sza-hero-tag">Shimla's highest road pass, above the Pabbar valley.</p>
<p class="sza-hero-sub">From Rohru via Chirgaon and Larot to 3,750 m meadows — we plan the SUV, the stay and the snow-day backup.</p>
<ul class="sza-chips"><li><b>Height</b> ~3,750 m</li><li><b>From Shimla</b> ~160 km</li><li><b>Open</b> May–Nov</li><li><b>Stay</b> Rohru / Larot</li><li><b>Car</b> SUV advised</li><li><b>Price</b> Get Quote</li></ul>
<div class="sza-btns"><a class="sza-btn gold" href="{MAIN}" target="_blank" rel="noopener">Get Quote on WhatsApp</a><a class="sza-btn ghost" href="{Q}">Plan my trip</a></div>
<div class="sza-trust"><span><a href="https://suzutravels.com/certificates/">HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022</a></span><span>Cab + hotel + backup plan</span><span>Reply within minutes</span></div>
</div>
</section>
<nav class="sza-nav" aria-label="On this page"><div class="sza-nav-in"><a href="#overview">Overview</a><a href="#spots">Stops</a><a href="#experience">The drive</a><a href="#season">Best time</a><a href="#safety">Safety</a><a href="#booking">How booking works</a><a href="#packages">Packages</a><a href="#faq">FAQ</a><a class="cta" href="{MAIN}" target="_blank" rel="noopener">Get Quote</a></div></nav>
<section class="sza-sec" id="overview">
<span class="sza-kicker">Quick answer</span>
<h2>Chanshal Pass, at a glance</h2>
<p class="sza-answer">Chanshal Pass (about 3,750 m) is the high road from Rohru to the Dodra Kwar valley in Shimla district, about 160 km from Shimla via Hatkoti and Rohru. It is open to traffic roughly May to November and snowbound the rest of the year. The last stretch above Larot is rough, so a high-clearance SUV and an early start are best.</p>
<div class="sza-facts">
<div class="sza-fact"><div class="k">Height</div><div class="v">About 3,750 m (the Shimla district site gives 3,755 m)</div></div>
<div class="sza-fact"><div class="k">Route</div><div class="v">Shimla → Theog → Kharapathar / Hatkoti → Rohru → Chirgaon → Larot → pass (~160 km; ~175 km via Narkanda)</div></div>
<div class="sza-fact"><div class="k">Drive time</div><div class="v">About 7–9 hours from Shimla; Rohru to the pass is about 48 km</div></div>
<div class="sza-fact"><div class="k">Open</div><div class="v">Roughly May to November; snow closes the top the rest of the year</div></div>
<div class="sza-fact"><div class="k">Stay</div><div class="v">Rohru (most hotels) or basic homestays at Larot; nothing at the top</div></div>
<div class="sza-fact"><div class="k">Price</div><div class="v">Get Quote</div></div>
</div>
</section>
<section class="sza-sec alt" id="spots">
<span class="sza-kicker">Stops on the way</span>
<h2>From Rohru to the top, and beyond</h2>
<p class="sza-lead">The places that shape a Chanshal trip. Photos show Himalayan roads and meadows in general.</p>
<div class="sza-grid">{cards}</div>
</section>
<section class="sza-sec" id="experience">
<span class="sza-kicker">How the trip runs</span>
<h2>Your Chanshal Pass trip, step by step</h2>
<ol class="sza-steps">
<li><h3>Send your dates</h3><p>WhatsApp your dates and group; we check the road status for that week.</p></li>
<li><h3>Day 1: to Rohru</h3><p>Shimla or Chandigarh to Rohru by the Kharapathar–Hatkoti road (or via Narkanda). Night in Rohru.</p></li>
<li><h3>Day 2: up to the pass</h3><p>An early start: Rohru → Chirgaon → Larot → Chanshal top, then back to Rohru by evening.</p></li>
<li><h3>Add-ons</h3><p>Hatkoti temple, a day by the Pabbar river, or a night in Narkanda or Shimla on the way back.</p></li>
<li><h3>Trekkers</h3><p>The Larot → Kwar trek over the pass, arranged with registered local operators on request.</p></li>
<li><h3>Snow or a slide?</h3><p>If the top is shut on the day, we switch to a backup plan — Narkanda, Hatkoti or the Pabbar riverside.</p></li>
</ol>
<div class="sza-media">
<video autoplay muted loop playsinline preload="none" poster="{CDN}explainer-poster.webp" width="1600" height="900" aria-label="Route map, not to scale: Shimla to Theog, Hatkoti and Rohru along the valley road, then Chirgaon, Larot and Chanshal Pass, about 160 km and 7 to 9 hours; SUV advised, nothing to stay at the top; open May to November, snow December to April"><source src="{CDN}explainer.webm" type="video/webm"><source src="{CDN}explainer.mp4" type="video/mp4"></video>
<div><h3>Shimla to Chanshal in one picture</h3><ul><li><b>Valley road</b> → Shimla → Theog → Hatkoti → Rohru.</li><li><b>The climb</b> → Rohru → Chirgaon → Larot → the pass, about 48 km.</li><li><b>Total</b> → about 160 km, 7–9 hours from Shimla.</li><li><b>Open</b> → May to November; snow from December to April.</li></ul></div>
</div>
</section>
<section class="sza-sec alt" id="season">
<span class="sza-kicker">When to go</span>
<h2>Best time to visit Chanshal Pass</h2>
<div class="sza-scroll"><table class="sza-tbl"><thead><tr><th>Months</th><th>Road</th><th>What to expect</th></tr></thead><tbody>
<tr><td>May – June</td><td>Open</td><td>Snow walls and patches near the top; the busiest weeks</td></tr>
<tr><td>July – mid-September</td><td>Open, risky</td><td>Monsoon slides on the Larot stretch; check alerts</td></tr>
<tr><td>Mid-September – October</td><td>Open</td><td>Clear skies and the best photos</td></tr>
<tr><td>November</td><td>Closure risk</td><td>The first snow can shut the top</td></tr>
<tr><td>December – April</td><td>Closed at the top</td><td>Snowbound; Rohru and Larot side only</td></tr>
</tbody></table></div>
<p style="margin-top:14px">Travelling in early May or November? Send your dates — we check whether the top is open that week before we book.</p>
</section>
<div class="sza-band" id="safety"><div class="sza-band-in">
<span class="sza-kicker">Safety</span>
<h2>What we check before we book your trip</h2>
<p class="sza-lead">Suzu Travels is an <a href="https://suzutravels.com/certificates/" style="color:#f3d98f;text-decoration:underline">HP Tourism registered travel agent (Reg. No. DTO-MND-11-243/2022)</a>. We plan the drive around these checks:</p>
<ul class="sza-checks">
<li><b>The road above Larot</b>Rough, rocky and steep: a high-clearance SUV and an experienced hill driver. Fuel up in Rohru.</li>
<li><b>No network</b>Phone signal ends around Larot. Tell your hotel your plan and when you expect to be back.</li>
<li><b>Altitude</b>About 3,750 m on a day trip — go slow, carry warm layers and start down by early afternoon.</li>
<li><b>Monsoon and snow</b>We follow HP SDMA and district alerts, and turn back on fresh snow or a slide.</li>
<li><b>Daylight</b>An early start from Rohru so you are off the high stretch well before dark.</li>
</ul>
</div></div>
<section class="sza-sec" id="booking">
<span class="sza-kicker">How booking works</span>
<h2>Get a quote in minutes</h2>
<ol class="sza-steps">
<li><h3>Tell us your dates</h3><p>WhatsApp or the quote form — dates, group size and where you start from.</p></li>
<li><h3>We check your date</h3><p>Road status for that week, the right vehicle and your stay in Rohru or Larot.</p></li>
<li><h3>You get one quote</h3><p>SUV, hotel nights and any trek add-on in one plan.</p></li>
<li><h3>Confirm and go</h3><p>We send the start time, what to carry and the latest road update before you travel.</p></li>
</ol>
<div class="sza-media">
<img src="{UP}aerial-hairpin-bends-forest-mountain-road-1024x576.webp" alt="Aerial view of a mountain road looping through hairpin bends across a forested green slope" loading="lazy" width="1024" height="576">
<div><h3>What your quote depends on</h3><ul><li>Vehicle — SUV / 4x4 for the pass, or a sedan to Rohru only</li><li>Start city (Shimla, Chandigarh or Delhi) and number of days</li><li>Season and the road status that week</li><li>Hotel nights in Rohru, Shimla or Narkanda</li><li>Trek add-on (guide, camps) on request</li></ul></div>
</div>
</section>
{reel}
<section class="sza-quote"><div><span class="sza-kicker">Ready for the drive?</span><h2>Get your Chanshal Pass quote</h2><p>Tell us your dates and group size. We reply with one plan — SUV, stay and a snow-day backup — for your dates within minutes.</p></div><div class="sza-btns"><a class="sza-btn gold" href="{MAIN}" target="_blank" rel="noopener">Get Quote on WhatsApp</a><a class="sza-btn ghost" href="{Q}">Plan full trip</a></div></section>
<section class="sza-sec" id="packages">
<span class="sza-kicker">Make it a trip</span>
<h2>Chanshal + Shimla and Narkanda</h2>
<p>The plan that works best: <b>Shimla → Narkanda → Rohru → Chanshal, 4 nights / 5 days by SUV</b>. Trekking <a href="/adventure/buran-ghati-trek/">Buran Ghati</a>? It also starts via Rohru, so Chanshal fits your night there. See our <a href="/destination/shimla-tour-packages/">Shimla tour packages</a>, <a href="/adventure/adventure-activities-in-shimla/">adventure in Shimla</a>, <a href="/adventure/snow-and-skiing-in-narkanda/">snow and skiing in Narkanda</a> and <a href="/adventure/trout-fishing-in-himachal/">trout fishing in Himachal</a>, or book a <a href="/cabs/shimla-taxi-service/">Shimla taxi</a> or a <a href="/cabs/chandigarh-to-shimla-taxi/">Chandigarh to Shimla taxi</a>. Going on to Kinnaur? Read our <a href="/sangla-valley-and-chitkul-kinnaur-trip-guide/">Sangla and Chitkul guide</a>.</p>
<div class="sza-btns" style="margin-top:18px"><a class="sza-btn gold" href="{wa("a Shimla, Narkanda, Rohru and Chanshal Pass trip (4N/5D by SUV)")}" target="_blank" rel="noopener">Shimla + Chanshal — Get Quote</a><a class="sza-btn line" href="{Q}">Plan my trip</a></div>
</section>
<section class="sza-sec sza-faq" id="faq">
<span class="sza-kicker">FAQ</span>
<h2>Chanshal Pass — questions</h2>
<details><summary>How high is Chanshal Pass?</summary><p>About 3,750 m; the Shimla district site gives 3,755 m. Chanshal Peak above it (about 4,520 m) is the highest peak of Shimla district.</p></details>
<details><summary>How far is Chanshal Pass from Shimla?</summary><p>About 160 km via Kharapathar and Hatkoti, or about 175 km via Narkanda — both through Rohru. Plan 7–9 hours.</p></details>
<details><summary>When is Chanshal Pass open?</summary><p>Roughly May to November. Snow closes the top for the rest of the year; the Rohru and Larot side stays reachable.</p></details>
<details><summary>Can a normal car go to Chanshal Pass?</summary><p>Up to Rohru and Chirgaon, yes. The stretch above Larot is rough and steep, so a high-clearance SUV is the safer choice.</p></details>
<details><summary>Where do I stay for Chanshal Pass?</summary><p>Rohru has the most hotels and is the usual base. Larot has basic homestays. There is no stay at the top.</p></details>
<details><summary>Can I go to Dodra Kwar by road?</summary><p>Do not plan on it. The road beyond the pass is seasonal and often not motorable; we check the status before you go.</p></details>
<details><summary>Is there a Chanshal trek?</summary><p>Yes — a multi-day trek from Larot over the pass to Kwar, best in May–June and mid-September–October. We arrange it with registered local operators on request.</p></details>
<details><summary>What does a Chanshal Pass trip cost?</summary><p>It depends on the vehicle, your start city, the number of nights and the season. Send your dates on WhatsApp and we share today's rate in minutes — Get Quote.</p></details>
</section>
<section class="sza-sec alt" id="more">
<span class="sza-kicker">More adventures</span>
<h2>Explore more in Himachal</h2>
<div class="sza-cats">
<a class="sza-cat" href="/adventure/adventure-activities-in-shimla/"><span class="ic">🏔️</span><span class="n">Adventure in Shimla</span><span class="c">Treks, paragliding, rafting</span></a>
<a class="sza-cat" href="/adventure/snow-and-skiing-in-narkanda/"><span class="ic">⛷️</span><span class="n">Narkanda snow</span><span class="c">Skiing and snow days</span></a>
<a class="sza-cat" href="/adventure/buran-ghati-trek/"><span class="ic">⛰️</span><span class="n">Buran Ghati Trek</span><span class="c">Starts via Rohru</span></a>
<a class="sza-cat" href="/adventure/churdhar-trek/"><span class="ic">🌲</span><span class="n">Churdhar Trek</span><span class="c">Cedar forest to 3,647 m</span></a>
<a class="sza-cat" href="/adventure/trout-fishing-in-himachal/"><span class="ic">🎣</span><span class="n">Trout fishing</span><span class="c">Himachal's trout rivers</span></a>
<a class="sza-cat" href="/adventure/"><span class="ic">🧭</span><span class="n">All adventures</span><span class="c">Air · Water · Snow · Land</span></a>
</div>
</section>
</div>
'''
pathlib.Path('/root/ak/adventure-kit/pages/chanshal-pass.html').write_text(html)
