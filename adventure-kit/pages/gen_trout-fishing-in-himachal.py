#!/usr/bin/env python3
"""Generator for /adventure/trout-fishing-in-himachal/ — Page Builder (night) 23 Oct 2026 IST.
Source: Research Lead brief 22 Oct 2026 (morning) + Visual Studio media @90a4f01 (night 23 Oct).
Writes trout-fishing-in-himachal.html next to this file; then: python3 ../build.py trout-fishing-in-himachal.html > trout-fishing-in-himachal.min.html
"""
import pathlib, urllib.parse

SLUG = "trout-fishing-in-himachal"
SHA = "90a4f01c2c27f2f5046c919ee9c2d942adc3971e"
CDN = f"https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@{SHA}/adventure-kit/media/{SLUG}/"
UP = "https://suzutravels.com/wp-content/uploads/2026/10/"
QUOTE = "/himachal-tour-packages-quote/?activity=" + urllib.parse.quote("Trout fishing")


def wa(what, tag=""):
    msg = (f"Hi Suzu Travels, I want a quote for {what}. Travel date: ___ , people: ___ "
           f"(page: {SLUG}{tag})")
    return "https://wa.me/917087488961?text=" + urllib.parse.quote(msg, safe="")


def a_wa(what, label, cls="", tag=""):
    c = f' class="{cls}"' if cls else ""
    return f'<a{c} href="{wa(what, tag)}" target="_blank" rel="noopener">{label}</a>'


MAIN = "trout fishing in Himachal (licence, guide, stay, cab)"

cards = [
    ("trout-fishing-himachal-boulder-stream-768x578.webp", 768, 578,
     "Clear mountain stream rushing over boulders below forested slopes with a footbridge",
     "Homestay valley", "Tirthan River (Kullu)", "Largi–Nagni, about 20 km of listed trout water",
     "Local guides and riverside homestays around Gushaini and Jibhi; pairs with a Jibhi–Tirthan holiday.",
     "trout fishing on the Tirthan River, Kullu", None),
    ("trout-fishing-himachal-angler-casting-768x510.webp", 768, 510,
     "Angler in waders casting a fly rod in a fast blue-green river",
     "Easy from Manali", "Beas, Katrain–Manali", "About 18 km of listed trout water",
     "The easiest beat to reach from a Manali hotel — a morning on the water, the rest of the day free.",
     "trout fishing on the Beas between Katrain and Manali", None),
    ("trout-fishing-himachal-brown-trout-release-768x768.webp", 768, 768,
     "Angler's hand releasing a spotted brown trout back into the water",
     "Quiet valley", "Barot (Uhl and Lambadug), Mandi", "Uhl ~10 km · Lambadug ~6 km",
     "A government trout farm sits at Barot, and 15,000 brown trout fingerlings were released into the Lambadug in March 2025.",
     "trout fishing at Barot (Uhl and Lambadug)", None),
    ("trout-fishing-himachal-boulder-stream-768x578.webp", 768, 578,
     "Clear mountain stream rushing over boulders below forested slopes with a footbridge",
     "Off-beat", "Sainj River (Kullu)", "Largi–Ropa, about 22 km",
     "The longest listed stretch, with fewer anglers — a good second day after the Tirthan.",
     "trout fishing on the Sainj River, Kullu", None),
    ("trout-fishing-himachal-wooden-hill-house-768x1023.webp", 768, 1023,
     "Traditional wooden hill house with a slate roof below Himalayan mountains",
     "Shimla side", "Pabbar at Rohru (Shimla district)", "Trout stream of the apple belt",
     "Fits a Shimla trip: drive out to Rohru for the river, stay a night and come back by the apple orchards.",
     "trout fishing on the Pabbar at Rohru", None),
    ("wide-calm-lake-hills-dusk-768x432.webp", 768, 432,
     "Wide, calm lake reflecting a pink and gold dusk sky, with a low line of hills on the far shore",
     "Winter option", "Mahseer and general waters", "Lower Beas, Pong and Gobind Sagar backwaters",
     "When trout rivers close (Nov–Feb), general waters stay open except 16 Jun–15 Aug — close to our Bilaspur base.",
     "mahseer / general-water angling (Pong, Gobind Sagar, lower Beas)", "/adventure/gobind-sagar-water-sports/"),
]

card_html = ""
for img, w, h, alt, badge, name, meta, txt, what, x in cards:
    xl = f'<a class="x" href="{x}">Explore →</a>' if x else ""
    card_html += (f'<article class="sza-card"><div class="img"><img src="{UP}{img}" alt="{alt}" loading="lazy" '
                  f'width="{w}" height="{h}"><span class="sza-badge">{badge}</span></div><div class="body"><h3>{name}</h3>'
                  f'<div class="meta"><b>{meta}</b></div><p class="meta">{txt}</p><div class="go">'
                  f'{a_wa(what, "Get Quote →", "q")}{xl}</div></div></article>')

faqs = [
    ("When is trout fishing season in Himachal?",
     "1 March to 31 October. Trout fishing in rivers is banned from 1 November to the last day of February for breeding; trout farms are not covered by the ban."),
    ("Do I need a fishing licence?",
     "Yes. The Fisheries Department issues the licence stream by stream, and you carry it with photo ID on the bank. We arrange it with your trip."),
    ("Can I fish in winter?",
     "Not for trout in rivers. General waters such as Pong and Gobind Sagar (mahseer and other fish) stay open, except from 16 June to 15 August."),
    ("What bait is allowed?",
     "Only artificial lures — spoons and flies — on trout waters. Nets, explosives, poison, spears and guns are banned."),
    ("Can I keep what I catch?",
     "A daily bag limit and a minimum size apply, and undersized trout must go back. Many anglers release every fish."),
    ("Which river is best for a first-timer?",
     "The Beas between Katrain and Manali is the easiest to reach; the Tirthan has local guides and riverside homestays."),
    ("Can children fish?",
     "Yes, with an adult and a guide, on calm water, wearing a life jacket."),
    ("Can you combine angling with a holiday?",
     "Yes — Jibhi–Tirthan, Manali, Bir–Barot or Bilaspur trips with hotel and cab in one quote. See the <a href=\"/jibhi-and-tirthan-valley-itinerary/\">Jibhi and Tirthan valley itinerary</a>."),
]
faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)

reel = pathlib.Path(__file__).resolve().parent.parent.joinpath("media", SLUG, "reel-section.html").read_text(encoding="utf-8").strip()

html = f'''<!-- {SLUG} — built by Page Builder (night) 23 Oct 2026 IST from the Research Lead brief 22 Oct (morning) + Visual Studio media @90a4f01. Kit v1.8. No prices, no operator names. Kept off (unverified): licence fee and where to buy it, exact bag limit and minimum size numbers, whether the 15 Jul–15 Sep adventure ban covers angling, the 2026-27 ban notice, fishing inside GHNP / Tirthan sanctuary, catch-and-release-only beats, mahseer species names. Brief badge 'Most popular' replaced by 'Homestay valley' (kit badge rule). Generic photos carry neutral alt text (never Tirthan/Barot). -->
<style>.sza-trf .sza-hero-in>*{{max-width:620px}}.sza-trf .sza-chips{{max-width:700px}}.sza-trf .sza-media ul{{padding-left:20px;list-style:disc;margin:0}}.sza-trf .sza-media ul li{{margin:0 0 8px}}.sza-trf .sza-media img{{height:auto;aspect-ratio:3/2;object-fit:cover}}.sza-trf .sza-media video{{height:auto;aspect-ratio:16/9}}.sza-trf #spots .sza-grid{{grid-template-columns:repeat(auto-fit,minmax(min(300px,100%),1fr))}}.sza-trf #spots .sza-card .img img{{aspect-ratio:3/2;object-fit:cover}}.sza-trf .sza-checks{{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}.sza-trf .sza-choose{{margin-top:32px}}@media(max-width:820px){{.sza-trf .sza-hero video{{object-position:30% 50%}}.sza-trf .sza-hero:after{{background:linear-gradient(180deg,rgba(11,31,51,.35) 0%,rgba(11,31,51,.6) 40%,rgba(11,31,51,.94) 100%)}}}}</style>
<div class="sza sza-trf">
<section class="sza-hero">
<video autoplay muted loop playsinline preload="metadata" poster="{UP}trout-fishing-in-himachal-hero-poster.webp" aria-label="A clear boulder mountain stream, an angler casting a fly rod, a brown trout being released and a wooden hill house, with a gold fly line that casts and lands with ripples and a 12-month strip lighting March to October: trout season 1 March to 31 October, closed November to February for breeding"><source src="{CDN}hero.webm" type="video/webm"><source src="{CDN}hero.mp4" type="video/mp4"></video>
<div class="sza-hero-in">
<span class="sza-kicker">Angling · Himachal Pradesh</span>
<p class="sza-hero-tag">Cast a fly on Himachal's cold trout streams</p>
<p class="sza-hero-sub">Tirthan, Barot, Beas and Pabbar — licence, guide, stay and cab arranged with your trip.</p>
<ul class="sza-chips"><li><b>Season</b> 1 Mar–31 Oct</li><li><b>Closed</b> 1 Nov–end Feb</li><li><b>Licence</b> for each stream</li><li><b>Spoons &amp; flies</b> only</li><li><b>Brown &amp; rainbow</b> trout</li><li><b>Price</b> Get Quote</li></ul>
<div class="sza-btns">{a_wa(MAIN, "Get Quote on WhatsApp", "sza-btn gold")}<a class="sza-btn ghost" href="{QUOTE}">Plan my trip</a></div>
<div class="sza-trust"><span><a href="https://suzutravels.com/certificates/">HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022</a></span><span>Licence + guide + stay + cab</span><span>Reply within minutes</span></div>
</div>
</section>
<nav class="sza-nav" aria-label="On this page"><div class="sza-nav-in"><a href="#overview">Overview</a><a href="#spots">Rivers</a><a href="#experience">Your angling day</a><a href="#season">By month</a><a href="#safety">Rules &amp; safety</a><a href="#booking">How booking works</a><a href="#packages">Trips</a><a href="#faq">FAQ</a>{a_wa(MAIN, "Get Quote", "cta")}</div></nav>

<section class="sza-sec" id="overview">
<span class="sza-kicker">Quick answer</span>
<h2>Trout fishing in Himachal, at a glance</h2>
<p class="sza-answer">Trout fishing in Himachal is open from 1 March to 31 October on listed stretches of the Tirthan, Beas, Sainj, Uhl (Barot), Pabbar and Baspa. It closes from 1 November to the last day of February for breeding. You need a Fisheries Department licence for the stream you fish, and only spoons and flies are allowed. Send your dates — we arrange the licence, a local guide, stay and cab.</p>
<div class="sza-facts"><div class="sza-fact"><div class="k">Rivers</div><div class="v">Tirthan and Sainj (Kullu), Beas Katrain–Manali, Uhl and Lambadug at Barot (Mandi), Pabbar at Rohru, Baspa at Sangla</div></div><div class="sza-fact"><div class="k">Trout season</div><div class="v">1 Mar–31 Oct; closed 1 Nov–last day of Feb (natural rivers; trout farms excluded)</div></div><div class="sza-fact"><div class="k">Licence</div><div class="v">Fisheries Department, issued per stream; carry it with photo ID</div></div><div class="sza-fact"><div class="k">Tackle</div><div class="v">Artificial lures only (spoons, flies); daily bag limit and a minimum size — undersized fish go back</div></div><div class="sza-fact"><div class="k">Winter option</div><div class="v">Mahseer and other fish in general waters (Pong, Gobind Sagar, lower Beas) — closed only 16 Jun–15 Aug</div></div><div class="sza-fact"><div class="k">Price</div><div class="v">Get Quote</div></div></div>
</section>

<section class="sza-sec alt" id="spots">
<span class="sza-kicker">Where to fish</span>
<h2>Himachal's trout rivers, and a winter option</h2>
<p class="sza-lead">Five trout beats, each with its own licence, plus mahseer waters for the months the trout rivers are closed.</p>
<div class="sza-grid">{card_html}</div>
</section>

<section class="sza-sec" id="experience">
<span class="sza-kicker">Your angling day</span>
<h2>How a guided angling day works</h2>
<ol class="sza-steps"><li><h3>Send your dates</h3><p>River, dates and group on WhatsApp.</p></li><li><h3>We check the water</h3><p>That the stream is open and fishable that week.</p></li><li><h3>Licence</h3><p>Taken for that stream on your photo ID — carry it on the bank.</p></li><li><h3>Morning on the water</h3><p>With a local guide — spoon or fly, wading only where it is safe.</p></li><li><h3>Fish within the rules</h3><p>Stay inside the bag limit and release undersized fish (many guests release all).</p></li><li><h3>Back to your stay</h3><p>Add Jalori or GHNP walks, <a href="/adventure/paragliding-in-bir-billing/">Bir paragliding</a> (Barot side) or <a href="/adventure/gobind-sagar-water-sports/">Gobind Sagar</a>.</p></li></ol>
<div class="sza-media"><img src="{UP}trout-fishing-himachal-angler-casting-768x510.webp" alt="Angler in waders casting a fly rod in a fast blue-green river" loading="lazy" width="768" height="510"><div><h3>What to bring</h3><ul><li>Photo ID for the licence</li><li>Your own rod, reel, spoons and flies — or gear arranged on request</li><li>Grip or felt-soled boots and warm layers; snowmelt water is cold</li><li>Polarised glasses, a cap and a small dry bag</li></ul><p>Keep the bank clean: take back all line, hooks and plastic.</p></div></div>
</section>

<section class="sza-sec alt" id="season">
<span class="sza-kicker">When to go</span>
<h2>Trout fishing by month</h2>
<div class="sza-scroll"><table class="sza-tbl"><thead><tr><th>Months</th><th>Trout rivers</th><th>Mahseer / general waters</th><th>Notes</th></tr></thead><tbody><tr><td>Mar – Apr</td><td>Open</td><td>Open</td><td>Cold snowmelt water; a good start</td></tr><tr><td>May – Jun</td><td>Open</td><td>Open (closed from 16 Jun)</td><td>Peak searches; book early</td></tr><tr><td>Jul – Aug</td><td>Open on paper</td><td>Closed 16 Jun–15 Aug</td><td>Monsoon floods and muddy water; small streams only, check roads</td></tr><tr><td>Sep – Oct</td><td>Open (last day 31 Oct)</td><td>Open</td><td>Clear water, the best trout weeks</td></tr><tr><td>Nov – Feb</td><td>Closed (breeding ban; fines under the HP Fisheries Act 2020)</td><td>Open</td><td>Winter = mahseer at Pong or Gobind Sagar, or a trout-farm visit</td></tr></tbody></table></div>
<div class="sza-media sza-choose"><video autoplay muted loop playsinline preload="none" poster="{UP}trout-fishing-in-himachal-explainer-poster.webp" width="1600" height="900" aria-label="Motion graphic: can I fish in my month? Trout streams open March to October and closed November to February; general waters and mahseer closed 16 June to 15 August. Then where the trout water is: Sainj about 22 km, Tirthan about 20 km, Beas Katrain to Manali about 18 km, Uhl about 10 km, Lambadug about 6 km, plus Pabbar and Baspa; licence for each stream, spoons and flies only, price on quote"><source src="{CDN}explainer.webm" type="video/webm"><source src="{CDN}explainer.mp4" type="video/mp4"></video><div><h3>Can I fish in my month?</h3><ul><li><b>Mar–Oct</b> → trout rivers open.</li><li><b>Nov–Feb</b> → trout rivers closed for breeding.</li><li><b>16 Jun–15 Aug</b> → general (mahseer) waters closed.</li><li><b>Longest beats</b> → Sainj ~22 km, Tirthan ~20 km, Beas ~18 km.</li></ul><p>We check the water and the licence for your dates before we book.</p></div></div>
</section>

<div class="sza-band" id="safety"><div class="sza-band-in">
<span class="sza-kicker">Rules &amp; safety</span>
<h2>The angling rules we check before we book</h2>
<p class="sza-lead">Suzu Travels is an <a href="https://suzutravels.com/certificates/" style="color:#f3d98f;text-decoration:underline">HP Tourism registered travel agent (Reg. No. DTO-MND-11-243/2022)</a>. We arrange angling days with registered local guides and check these first:</p>
<ul class="sza-checks"><li><b>Season and licence</b>Fish only in season and with a valid licence for that stream; the department patrols rivers in the closed season.</li><li><b>Rod and line only</b>Spoons and flies on trout water. Nets, explosives, poison, spears and guns are banned under the HP Fisheries Rules.</li><li><b>Wading</b>Grip or felt boots, never alone, stay off wet boulders above deep pools; a life jacket near fast water and for children.</li><li><b>Hydro releases</b>Water can rise suddenly below dams and power houses — follow sirens and boards and leave the riverbed when the water colours.</li><li><b>Monsoon</b>Flash floods and landslides in Jul–Aug; we move you to a safer stream or another day.</li><li><b>Respect the river</b>Leave no line, hooks or plastic; some stretches near temples and cremation grounds are closed to fishing.</li></ul>
</div></div>

<section class="sza-sec" id="booking">
<span class="sza-kicker">How booking works</span>
<h2>Get a quote in minutes</h2>
<ol class="sza-steps"><li><h3>Tell us</h3><p>WhatsApp or the quote form — dates, river, group and where you start.</p></li><li><h3>We check your date</h3><p>Season, water and weather, the licence and a local guide.</p></li><li><h3>You get one quote</h3><p>Angling days, licence, guide, stay and cab in one plan.</p></li><li><h3>Confirm and go</h3><p>We send the meeting point, the licence details and what to carry.</p></li></ol>
<div class="sza-media"><img src="{UP}trout-fishing-himachal-wooden-hill-house-768x1023.webp" alt="Traditional wooden hill house with a slate roof below Himalayan mountains" loading="lazy" width="768" height="1023"><div><h3>What your quote depends on</h3><ul><li>River and number of fishing days</li><li>Licence days and whether you want a local guide</li><li>Own tackle, or gear arranged on request</li><li>Stay type (riverside homestay, cottage, hotel) and nights</li><li>Cab from Delhi, Chandigarh or Manali, and between valleys</li><li>Group size, and whether it is part of a longer Himachal package</li></ul><p>We send today's rate on WhatsApp within minutes.</p></div></div>
</section>

{reel}

<section class="sza-quote"><div><span class="sza-kicker">Ready to cast?</span><h2>Get your trout fishing quote</h2><p>Tell us your dates and river. We reply with one plan — licence, guide, stay and cab — within minutes.</p></div><div class="sza-btns">{a_wa(MAIN, "Get Quote on WhatsApp", "sza-btn gold")}<a class="sza-btn ghost" href="{QUOTE}">Plan full trip</a></div></section>

<section class="sza-sec" id="packages">
<span class="sza-kicker">Make it a trip</span>
<h2>Angling days that fit a Himachal holiday</h2>
<p>Three easy ways to do it, with hotel and cab in one quote: <b>Jibhi–Tirthan, 4 days with one angling day</b> (see our <a href="/jibhi-and-tirthan-valley-itinerary/">Jibhi and Tirthan valley itinerary</a>); <b>a Manali stay with a Beas morning</b>, plus <a href="/adventure/river-rafting-in-kullu-manali/">river rafting in Kullu–Manali</a> or the rest of our <a href="/adventure/adventure-activities-in-manali/">Manali adventure activities</a>; or <b>Bir + Barot</b>, with a <a href="/adventure/paragliding-in-bir-billing/">Bir Billing tandem flight</a>. Getting there: <a href="/cabs/delhi-to-manali-taxi/">Delhi to Manali taxi</a> or <a href="/cabs/delhi-to-kasol-taxi/">Delhi to Kasol taxi</a> (via Bhuntar and Aut, the turn for Tirthan). For nights by the river, see <a href="/adventure/camping-in-himachal/">camping in Himachal</a>.</p>
<div class="sza-btns" style="margin-top:18px">{a_wa("a Jibhi-Tirthan trip with one trout fishing day (licence, guide, stay, cab)", "Jibhi–Tirthan + angling — Get Quote", "sza-btn gold")}{a_wa("a Manali stay with a morning of trout fishing on the Beas", "Manali + Beas morning — Get Quote", "sza-btn line")}</div>
</section>

<section class="sza-sec sza-faq" id="faq">
<span class="sza-kicker">FAQ</span>
<h2>Trout fishing in Himachal — questions</h2>
{faq_html}
</section>

<section class="sza-sec alt" id="more">
<span class="sza-kicker">More adventures</span>
<h2>Explore more in Himachal</h2>
<div class="sza-cats"><a class="sza-cat" href="/adventure/gobind-sagar-water-sports/"><span class="ic">🚤</span><span class="n">Gobind Sagar Lake</span><span class="c">Boats and jet skis, Bilaspur</span></a><a class="sza-cat" href="/adventure/river-rafting-in-kullu-manali/"><span class="ic">🌊</span><span class="n">River rafting</span><span class="c">Beas, Kullu–Manali</span></a><a class="sza-cat" href="/adventure/rafting-in-shimla-tattapani/"><span class="ic">🚣</span><span class="n">Rafting at Tattapani</span><span class="c">Sutlej, near Shimla</span></a><a class="sza-cat" href="/adventure/camping-in-himachal/"><span class="ic">⛺</span><span class="n">Camping in Himachal</span><span class="c">Where to camp this month</span></a><a class="sza-cat" href="/adventure/paragliding-in-bir-billing/"><span class="ic">🪂</span><span class="n">Paragliding in Bir Billing</span><span class="c">Near Barot</span></a><a class="sza-cat" href="/adventure/"><span class="ic">🧭</span><span class="n">All adventures</span><span class="c">Air · Water · Snow · Land</span></a></div>
</section>
</div>
'''
out = pathlib.Path(__file__).with_name(f"{SLUG}.html")
out.write_text(html, encoding="utf-8")
print(out)
