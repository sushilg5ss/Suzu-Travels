#!/usr/bin/env python3
"""UK (London + Scotland) page — .hx design system; same template as gen_mauritius.py / gen_switzerland.py.
Run from outbound-kit/:  python3 pages/gen_uk.py <PAGE_ID>  -> pages/uk-tour-packages.html (one line)
Facts: GOV.UK checked 26 Oct 2026 — Check if you need a UK visa (India + tourism -> "You'll need a visa ... Apply for a
Standard Visitor visa"); Standard Visitor guide (usually up to 6 months, passport valid for whole stay, show you will
leave / can support yourself / pay return journey); Apply page (online, earliest 3 months before travel, appointment at a
visa application centre for fingerprints + photo, passport back same day, each family member own application, decision
usually within 3 weeks); Visa processing times outside the UK (Standard Visitor 3 weeks; do not book travel until decided).
No prices (visa fee deliberately not shown). 8-day itinerary = 4 columns.
"""
import json, html, sys, os
sys.path.insert(0, os.getcwd())
import gen_hub as G

PID = int(sys.argv[1]) if len(sys.argv) > 1 else 0
M = G.M
svg, WA_SVG, wa = G.svg, G.WA_SVG, G.wa
CHECKED = '26 October 2026'
SRC_CHECK = 'https://www.gov.uk/check-uk-visa'
SRC_SV = 'https://www.gov.uk/standard-visitor'
SRC_APPLY = 'https://www.gov.uk/standard-visitor/apply-standard-visitor-visa'
SRC_TIMES = 'https://www.gov.uk/guidance/visa-processing-times-applications-outside-the-uk'

def U(k): return M[k]['url']
def A(k): return html.escape(M[k]['alt'], quote=True)
def C(k): return html.escape(M[k]['cap'])

# hub CSS minus the hub's page-header block, then this page's header + extras
import re
_DROP = ('hx-intro', 'hx-region', 'hx-rhead', 'hx-rnote', 'hx-grid', 'hx-dc', 'hx-styles', 'hx-tabs', 'hx-r{', 'hx-r ', 'hx-pane', 'hx-sc', 'hx-gal', 'hx-why', 'hx-who', 'hxs', 'hx-p1')
def _prune(line):
    if line.startswith('@media(max-width'):
        head, body = line.split('{', 1)
        rules = re.findall(r'[^{}]+\{[^{}]*\}', body[:-1])
        keep = [r for r in rules if not any(t in r for t in _DROP) and 'page-id-' not in r]
        return head + '{' + ''.join(keep) + '}' if keep else ''
    return '' if any(t in line for t in _DROP) or 'page-id-' in line else line
base = '\n'.join(_prune(l) for l in G.CSS.splitlines())
EXTRA = r"""
.hx .hx-facts{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin:18px 0 0}
.hx .hx-fact{background:var(--cream);border:1px solid var(--line);border-radius:16px;padding:15px 16px;position:relative;overflow:hidden}
.hx .hx-fact:before{content:"";position:absolute;left:0;top:0;bottom:0;width:4px;background:var(--gold)}
.hx .hx-fact b{display:block;color:var(--mut);font-size:11.5px;text-transform:uppercase;letter-spacing:.1em;margin-bottom:3px;font-weight:800}
.hx .hx-fact span{color:var(--ink);font-size:15.5px;font-weight:700;line-height:1.35;display:block}
.hx .hx-pg{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));grid-auto-rows:210px;gap:12px;margin-top:18px}
.hx .hx-pg figure{position:relative;margin:0;border-radius:16px;overflow:hidden;background:#0b1510}
.hx .hx-pg figure:first-child{grid-column:span 2;grid-row:span 2}
.hx .hx-pg figure:nth-child(4){grid-row:span 2}
.hx .hx-pg img{width:100%;height:100%;object-fit:cover;display:block;margin:0;transition:transform .6s}
.hx .hx-pg figure:hover img{transform:scale(1.05)}
.hx .hx-pg figcaption{position:absolute;left:10px;bottom:10px;background:rgba(10,18,14,.7);color:#fff;font-size:12px;font-weight:700;padding:5px 10px;border-radius:999px}
.hx .hx-cards{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px;margin-top:18px}
.hx .hx-card{background:#fff;border:1px solid var(--line);border-radius:18px;padding:20px;box-shadow:0 4px 14px rgba(14,27,20,.04)}
.hx .hx-card h3{font-size:17.5px}
.hx .hx-card p{margin:0;color:var(--mut);font-size:14.5px;line-height:1.6}
.hx .hx-card .hx-tag{display:inline-block;margin:0 0 10px}
.hx .hx-itin{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px;margin-top:18px}
.hx .hx-day{background:var(--cream);border:1px solid var(--line);border-radius:18px;padding:18px 16px}
.hx .hx-day i{display:inline-block;font-style:normal;background:var(--ink);color:var(--gold);font-weight:800;font-size:12px;letter-spacing:.08em;text-transform:uppercase;padding:5px 10px;border-radius:999px;margin-bottom:10px}
.hx .hx-day b{display:block;color:var(--ink);font-size:16px;line-height:1.3;margin-bottom:6px}
.hx .hx-day p{margin:0;color:var(--mut);font-size:14px;line-height:1.55}
.hx .hx-tw{overflow-x:auto;margin-top:16px;border:1px solid var(--line);border-radius:18px}
.hx table.hx-t{width:100%;border-collapse:collapse;font-size:15px;min-width:560px;margin:0}
.hx table.hx-t th,.hx table.hx-t td{padding:13px 16px;text-align:left;border:0;border-bottom:1px solid var(--line);vertical-align:top}
.hx table.hx-t th{background:var(--ink);color:#fff;font-size:12.5px;letter-spacing:.08em;text-transform:uppercase}
.hx table.hx-t tr:last-child td{border-bottom:0}
.hx table.hx-t td:first-child{font-weight:800;color:var(--ink);white-space:nowrap}
.hx .hx-ok{color:#1B5E20;font-weight:800}.hx .hx-mid{color:#9A7B12;font-weight:800}.hx .hx-hot{color:#B3261E;font-weight:800}
.hx .hx-visa{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,.8fr);gap:18px;margin-top:16px}
.hx .hx-vbox{background:#fff;border:1px solid var(--line);border-radius:18px;padding:22px}
.hx .hx-vbox ul{margin:8px 0 0;padding-left:20px;color:var(--mut);font-size:15px}
.hx .hx-vbox li{margin:0 0 8px}
.hx .hx-vnote{background:#FFF8E6;border:1px solid #EBD9A3;border-radius:18px;padding:20px 22px;color:#5E4F18;font-size:15px}
.hx .hx-vnote p{margin:0 0 10px}
.hx .hx-checked{font-size:13px;color:var(--mut);margin-top:10px}
.hx .hx-checked a{color:var(--mut)}
.hx .hx-inc{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin-top:16px}
.hx .hx-inc div{display:flex;gap:12px;align-items:flex-start;background:var(--cream);border:1px solid var(--line);border-radius:16px;padding:16px}
.hx .hx-inc svg{width:22px;height:22px;flex:none;color:var(--g);margin-top:2px}
.hx .hx-inc b{display:block;color:var(--ink);font-size:15.5px}
.hx .hx-inc span{display:block;color:var(--mut);font-size:14px;line-height:1.5}
body.page-id-PID .page-content{position:relative;padding-top:22px!important}
body.page-id-PID .page-header{position:absolute;z-index:6;top:22px;left:24px;right:24px;margin:0!important;padding:58px 52px 0;background:none;pointer-events:none}
body.page-id-PID .page-header:before{content:"Holidays abroad \00B7  UK";display:inline-block;font:800 12px/1 "Plus Jakarta Sans",sans-serif;letter-spacing:.18em;text-transform:uppercase;color:#1a1606;background:#E2C158;padding:8px 13px;border-radius:999px;margin-bottom:16px}
body.page-id-PID .page-header .entry-title{color:#fff!important;font-family:"Sora","Plus Jakarta Sans",sans-serif!important;font-size:clamp(34px,4.2vw,58px)!important;line-height:1.06!important;letter-spacing:-.035em!important;margin:0!important;font-weight:800!important;max-width:15ch;text-shadow:0 2px 24px rgba(0,0,0,.35)}
@media(max-width:1100px){.hx .hx-cards{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-itin{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-visa{grid-template-columns:1fr}.hx .hx-inc,.hx .hx-steps{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:700px){body.page-id-PID .page-header{left:14px;right:14px;padding:26px 18px 0}body.page-id-PID .page-header:before{font-size:10.5px;padding:7px 11px;margin-bottom:12px}body.page-id-PID .page-header .entry-title{font-size:33px!important}.hx .hx-facts{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-pg{grid-template-columns:repeat(2,minmax(0,1fr));grid-auto-rows:150px}.hx .hx-pg figure:first-child{grid-column:span 2;grid-row:span 1}.hx .hx-pg figure:nth-child(4){grid-row:span 1}.hx .hx-pg figure:nth-child(8){display:none}.hx .hx-cards,.hx .hx-itin,.hx .hx-inc,.hx .hx-steps{grid-template-columns:1fr}.hx .hx-mini{grid-template-columns:repeat(2,minmax(0,1fr))}}
.hx .hx-pg p,.hx .hx-cards>p,.hx .hx-itin>p,.hx .hx-inc>p,.hx .hx-facts>p{display:none}
""".replace('PID', str(PID))
CSS = ' '.join(l.strip() for l in (base + EXTRA).strip().splitlines() if l.strip() and not l.strip().startswith('/*'))
HERO = ['uk', 'uk-1', 'uk-8', 'uk-10', 'uk-6', 'uk-9']
GAL = ['uk-10', 'uk-4', 'uk-5', 'uk-3', 'uk-7', 'uk-6', 'uk-8', 'uk-2']
FINAL = 'uk-9'
CC = 'UK'

FAQ = [
    ("Do Indians need a visa for the UK?", "Yes. GOV.UK says Indian nationals coming for tourism or to visit family and friends need a Standard Visitor visa before they travel. You apply online, then give your fingerprints and photo at a visa application centre. The decision is always made by UK Visas and Immigration — we help you prepare a complete, honest application but cannot promise an outcome. We checked these rules on 26 October 2026 and re-check them before every booking."),
    ("How early should we apply for the UK visa?", "GOV.UK says the earliest you can apply is 3 months before you travel, and you will usually get a decision within 3 weeks once you have applied online, proved your identity and provided your documents. It can take longer, for example in busy months or if more documents are needed. UK Visas and Immigration advises not to book travel until you have a decision, so we plan the itinerary first and confirm bookings after the visa."),
    ("How many days are enough for a UK trip?", "Five to six nights is enough for London with one or two day trips, such as Stonehenge and Bath or Oxford and the Cotswolds. With eight to ten nights you can add Edinburgh and a Scottish Highlands tour. Twelve nights or more lets you include the Isle of Skye, the Lake District or York at an easy pace."),
    ("Which is the best time to visit the UK from India?", "Late May to early September has the longest days and the mildest weather, but it is also the busiest and most expensive time, including Indian summer holidays. April–May and September–October are quieter and still pleasant. November to February is cold with short days, but London's Christmas lights and markets are a highlight. Rain is possible in any month, so we always plan indoor options."),
    ("Can we combine London with Scotland or Paris?", "Yes. London and Edinburgh are linked by direct trains, so London plus Scotland is the most popular combination. London and Paris are linked by the Eurostar train under the Channel — but France is a Schengen country, so you need a Schengen visa as well as the UK visa. We plan the visa order and dates with you."),
    ("Is Indian and vegetarian food easy to find in the UK?", "Yes. London and other UK cities have a very large Indian community and many Indian and vegetarian restaurants, and most cafés offer vegetarian options. We note vegetarian and Jain needs with your hotels and suggest restaurants on every tour day, including in Edinburgh and the Highlands."),
    ("Why are there no prices on this page?", "UK costs depend heavily on your dates, the hotel area in London, train and tour choices, attraction tickets and the airfare from your city. Instead of a teaser price that changes when you ask, we send a costed, day-by-day quote for your dates — usually within 24 hours."),
]

JS = ("(function(){var f=document.getElementById('hxPlan');if(!f){return;}f.addEventListener('submit',function(e){e.preventDefault();"
      "var d=f.querySelector('[name=d]').value,s=f.querySelector('[name=s]').value,m=f.querySelector('[name=m]').value,a=f.querySelector('[name=a]').value,k=f.querySelector('[name=k]').value,c=f.querySelector('[name=c]').value;"
      "var t='Hi Suzu Travels, please send me a costed UK itinerary.\\nTrip: '+d+'\\nTrip type: '+s+'\\nTravel month: '+m+'\\nAdults: '+a+'\\nChildren: '+k;"
      "if(c){t=t+'\\nDeparting from: '+c;}"
      "window.open('https:'+String.fromCharCode(47,47)+'wa.me/917087488961?text='+encodeURIComponent(t),'_blank','noopener');});})();")

REL = [('europe-tour-packages', 'Europe', 'suzu-abroad-europe', 'Paris, Swiss Alps, Italy'), ('switzerland-tour-packages', 'Switzerland', 'suzu-abroad-switzerland', 'Lucerne, Jungfrau, Zermatt'),
       ('dubai-tour-packages', 'Dubai', 'suzu-abroad-dubai', 'Burj Khalifa, desert, Abu Dhabi'), ('turkey-tour-packages', 'Turkey', 'suzu-abroad-turkey', 'Istanbul, Cappadocia, Pamukkale'),
       ('japan-tour-packages', 'Japan', 'suzu-abroad-japan', 'Tokyo, Fuji, Kyoto, Osaka'), ('mauritius-tour-packages', 'Mauritius', 'suzu-abroad-mauritius', 'Lagoons, Le Morne, island tours'), ('egypt-tour-packages', 'Egypt', 'suzu-abroad-egypt', 'Cairo, Nile cruise, Luxor'),
       ('georgia-tour-packages', 'Georgia', 'suzu-abroad-georgia', 'Tbilisi, Kazbegi, Gudauri'), ('azerbaijan-tour-packages', 'Azerbaijan', 'suzu-abroad-azerbaijan', 'Baku, Gabala, Shahdag'),
       ('maldives-tour-packages', 'Maldives', 'suzu-card-maldives', 'Overwater villas'), ('bali-tour-packages', 'Bali', 'suzu-card-bali', 'Ubud, villas, temples'),
       ('thailand-tour-packages', 'Thailand', 'suzu-card-thailand', 'Bangkok, Phuket, Krabi'), ('sri-lanka-tour-packages', 'Sri Lanka', 'suzu-card-sri-lanka', 'Beaches & tea country'),
       ('nepal-tour-packages', 'Nepal', 'suzu-card-nepal', 'No visa for Indians'), ('bhutan-tour-packages', 'Bhutan', 'suzu-card-bhutan', 'Paro, Thimphu, Punakha'),
       ('singapore-tour-packages', 'Singapore', 'suzu-card-singapore', 'City, Sentosa, Universal'), ('malaysia-tour-packages', 'Malaysia', 'suzu-card-malaysia', 'KL, Langkawi, Genting'),
       ('vietnam-tour-packages', 'Vietnam', 'suzu-card-vietnam', 'Hanoi, Ha Long, Hoi An')]

def build():
    W = "Hi Suzu Travels, I'm planning a UK trip. Please share a quote."
    h = [f'<div class="suzu-intl hx hx-country"><style>{CSS}</style>']
    slides = ''.join(f'<div class="hx-slide"><img src="{U(s)}" alt="{A(s)}" width="1600" height="1000" {"fetchpriority=\"high\" loading=\"eager\"" if i == 0 else "loading=\"lazy\""} decoding="async"><span class="hx-cap">{C(s)}</span></div>' for i, s in enumerate(HERO))
    h.append('<section class="hx-hero" aria-label="UK and London tour packages from India"><div class="hx-slides">' + slides + '</div><div class="hx-copy">'
             '<p class="hx-lede">Big Ben and the Thames, Stonehenge and the honey-stone villages of the Cotswolds, Edinburgh Castle on its rock and the wild glens of the Scottish Highlands — a UK holiday packs history, royal London and some of Europe&rsquo;s most dramatic scenery into one trip. We plan it to your dates, budget and pace, with central hotels, the right trains and tours, and honest UK visa guidance from the start.</p>'
             '<div class="hx-badges">'
             f'<span class="hx-badge">{svg("globe")}London, England &amp; Scotland</span><span class="hx-badge">{svg("food")}Vegetarian meals planned</span>'
             f'<span class="hx-badge">{svg("team")}Families, couples &amp; groups</span><span class="hx-badge">{svg("doc")}Official visa rules, checked</span></div>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Get a UK Quote {svg("arrow")}</a>'
             f'<a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div></div>'
             '<form class="hx-plan" id="hxPlan" aria-label="Get a costed UK itinerary on WhatsApp"><h3>Plan my UK trip</h3>'
             '<p>Tell us the basics — we reply on WhatsApp with a costed, day-by-day plan, usually within 24 hours.</p><div class="hx-f">'
             '<label class="hx-full">Trip<select name="d"><option selected>London + Scotland</option><option>London highlights</option><option>London + Paris</option><option>England countryside + London</option><option>UK honeymoon</option><option>UK family holiday</option><option>Not sure yet</option></select></label>'
             '<label>Trip type<select name="s"><option>Family</option><option>Honeymoon / couple</option><option>Friends</option><option>Seniors</option><option>Group</option><option>Corporate / MICE</option></select></label>'
             f'<label>Travel month<select name="m">{G.months()}</select></label>'
             '<label>Adults<select name="a"><option>1</option><option selected>2</option><option>3</option><option>4</option><option>5</option><option>6</option><option>7–10</option><option>11–20</option><option>20+</option></select></label>'
             '<label>Children<select name="k"><option>0</option><option>1</option><option>2</option><option>3</option><option>4+</option></select></label>'
             '<label class="hx-full">Departing from<input name="c" type="text" placeholder="e.g. Delhi, Mumbai, Chandigarh" autocomplete="address-level2"></label></div>'
             f'<button class="hx-btn" type="submit">{WA_SVG}Get my UK plan on WhatsApp</button><small>Opens WhatsApp with your details filled in. We do not store anything on this page.</small></form></section>')
    h.append('<div class="hx-trust">'
             f'<div>{svg("clock")}<span><b>Quote in ~24 hours</b><span>Costed, day by day</span></span></div>'
             f'<div>{svg("doc")}<span><b>Honest visa guidance</b><span>Official GOV.UK rules, checked</span></span></div>'
             f'<div>{svg("shield")}<span><b>HP Tourism registered</b><span>Reg. DTO-MND-11-243/2022</span></span></div>'
             f'<div>{svg("chat")}<span><b>One team, start to finish</b><span>On WhatsApp while you travel</span></span></div></div>')
    h.append('<nav class="hx-toc" aria-label="On this page"><a href="#why-uk">Why the UK</a><a href="#uk-in-photos">Photos</a><a href="#how-to-choose">Choose your trip</a><a href="#sample-itinerary">Sample itinerary</a><a href="#when-to-go">When to go</a><a href="#visa-and-entry">Visa</a><a href="#whats-included">What\'s included</a><a href="#uk-faq">FAQ</a></nav>')
    facts = [('Getting there', 'Fly into London — Heathrow or Gatwick — or Edinburgh; we compare routes from your city'), ('Time difference', 'India is 5 hr 30 min ahead in winter (GMT) and 4 hr 30 min ahead in summer (BST)'), ('Currency', 'Pound sterling (GBP)'),
             ('Best season', 'Late May to early September; April–May and September–October are quieter'), ('Typical trip', '6 to 10 nights — London, England day trips, Scotland'), ('Visa', 'Standard Visitor visa needed for Indian nationals, as per GOV.UK — apply before you travel')]
    h.append('<section id="why-uk" class="hx-sec"><span class="hx-eye">United Kingdom</span><h2>Why the UK works so well for Indian travellers</h2>'
             '<p class="hx-sub">London alone can fill a week — Westminster and Big Ben, Buckingham Palace, the Tower of London and Tower Bridge, the London Eye, world-class museums and West End shows. Beyond it, easy day trips reach Stonehenge, the Georgian city of Bath, Oxford and the Cotswold villages, and fast trains take you north to Edinburgh and the Scottish Highlands. English is spoken everywhere, Indian and vegetarian food is easy to find, and many Indian families combine sightseeing with visiting relatives.</p>'
             '<div class="hx-facts">' + ''.join(f'<div class="hx-fact"><b>{a}</b><span>{b}</span></div>' for a, b in facts) + '</div></section>')
    h.append('<section id="uk-in-photos" class="hx-sec"><span class="hx-eye">Real places</span><h2>The UK in photos</h2>'
             '<p class="hx-sub">Eilean Donan Castle in the Highlands, Stonehenge, Bath on the River Avon, the London Eye, the Radcliffe Camera in Oxford, Bibury in the Cotswolds, Edinburgh Castle and Big Ben. Photos by Unsplash photographers, credited below.</p><div class="hx-pg">'
             + ''.join(f'<figure><img src="{U(k)}" alt="{A(k)}" width="800" height="600" loading="lazy" decoding="async"><figcaption>{C(k)}</figcaption></figure>' for k in GAL) + '</div></section>')
    cards = [('Families', 'London with children', 'The Natural History and Science Museums, the London Eye, a Thames cruise, the Changing of the Guard and a studio or theme-park day — at a pace that suits children, with central family rooms.'),
             ('Couples', 'Honeymoon &amp; romance', 'A London stay with a show and a river cruise, a night in a Cotswold village, then Edinburgh and the Highlands — few hotel changes and special touches for the occasion.'),
             ('Seniors', 'Easy UK holiday', 'Fewer hotel changes, a London base with comfortable day trips, private transfers and step-free choices where possible, and vegetarian meals arranged.'),
             ('Scenery', 'Scotland &amp; castles', 'Edinburgh&rsquo;s Old Town and castle, Glencoe, Loch Ness and Eilean Donan — add the Isle of Skye or the Lake District if you have more days.')]
    stays = [('Central London', 'Westminster, the South Bank or Covent Garden put Big Ben, the London Eye and the theatres within walking distance. Best for first-timers.'),
             ('Kensington &amp; Hyde Park', 'Quieter streets near the big museums and Hyde Park, with good Underground links. Popular with families.'),
             ('Edinburgh Old &amp; New Town', 'Stay below the castle near the Royal Mile, or in the elegant New Town by Princes Street — both close to the railway station.'),
             ('Scottish Highlands', 'A night near Inverness, Fort William or on the Isle of Skye turns a long day tour into a relaxed one, with lochs and glens on your doorstep.')]
    h.append('<section id="how-to-choose" class="hx-sec"><span class="hx-eye">How to choose</span><h2>Choose the UK trip that fits you</h2>'
             '<p class="hx-sub">Start from the kind of trip you want — we fine-tune the cities, hotels, trains and tours to your group.</p><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><span class="hx-tag">{t}</span><h3>{n}</h3><p>{d}</p></div>' for t, n, d in cards) + '</div>'
             '<h3 style="margin-top:30px">Where to stay — the area shapes your trip</h3><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><h3>{n}</h3><p>{d}</p></div>' for n, d in stays) + '</div></section>')
    days = [('Day 1', 'Arrive in London', 'Airport pickup and transfer to your central hotel. An easy evening walk along the Thames.'),
            ('Day 2', 'Westminster &amp; the Thames', 'Big Ben and the Houses of Parliament, Westminster Abbey, Buckingham Palace and the London Eye, with a Thames river cruise.'),
            ('Day 3', 'Tower &amp; museums', 'The Tower of London and Tower Bridge, then a museum of your choice and an evening in the West End or a show.'),
            ('Day 4', 'Stonehenge &amp; Bath', 'A day tour to the stone circle of Stonehenge and the Georgian city of Bath with its Roman Baths, back to London by evening.'),
            ('Day 5', 'Oxford &amp; the Cotswolds', 'The colleges and Radcliffe Camera in Oxford, then honey-stone villages such as Bibury in the Cotswolds.'),
            ('Day 6', 'Train to Edinburgh', 'A direct train from London to Edinburgh. Afternoon on the Royal Mile and Edinburgh Castle.'),
            ('Day 7', 'Scottish Highlands', 'A full-day Highlands tour through Glencoe to Loch Ness — or stay a night to add Eilean Donan and the Isle of Skye.'),
            ('Day 8', 'Fly home', 'Breakfast, a last walk in Edinburgh and a transfer to the airport for your flight home.')]
    h.append('<section id="sample-itinerary" class="hx-sec"><span class="hx-eye">Sample plan</span><h2>A sample 8-day London &amp; Scotland itinerary</h2>'
             '<p class="hx-sub">The classic first trip: three London days, two England day trips and Scotland. We rebuild it around you — more London time, an extra Highlands night, or Paris by Eurostar with a Schengen visa.</p><div class="hx-itin">'
             + ''.join(f'<div class="hx-day"><i>{a}</i><b>{b}</b><p>{c}</p></div>' for a, b, c in days) + '</div></section>')
    seasons = [('Mar – May', '<span class="hx-ok">Good</span>', 'Spring, cool to mild', 'Parks and gardens in bloom and fewer crowds than summer. Pack layers — mornings are cool and showers are common.'),
               ('Jun – Aug', '<span class="hx-ok">Best</span>', 'Summer, mildest, longest days', 'Long daylight for sightseeing and the best Highlands weather. Also the busiest and costliest season, with Indian summer holidays — book early.'),
               ('Sep – Oct', '<span class="hx-ok">Good</span>', 'Autumn, mild to cool', 'Quieter than summer, autumn colours in the countryside and still comfortable for touring. Days get shorter through October.'),
               ('Nov – Feb', '<span class="hx-mid">Cold, short days</span>', 'Winter', 'Cold, often grey and dark by late afternoon; Highlands roads can be affected by snow. London&rsquo;s Christmas lights and markets are the highlight — Christmas and New Year are peak dates.')]
    h.append('<section id="when-to-go" class="hx-sec"><span class="hx-eye">Best season</span><h2>When to go to the UK</h2>'
             '<p class="hx-sub">The UK can be visited all year, and rain is possible in any month. We check the season, school holidays and event dates against your plan before we quote.</p>'
             '<div class="hx-tw"><table class="hx-t"><thead><tr><th>Months</th><th>Verdict</th><th>Weather</th><th>What it means for your trip</th></tr></thead><tbody>'
             + ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in seasons) + '</tbody></table></div></section>')
    h.append('<section id="visa-and-entry" class="hx-sec"><span class="hx-eye">Visa &amp; entry</span><h2>UK visa for Indian passport holders</h2>'
             '<div class="hx-visa"><div class="hx-vbox"><h3>What the official rules say</h3><ul>'
             '<li>GOV.UK&rsquo;s visa checker says Indian nationals coming for <b>tourism or to visit family and friends need a visa</b> — the <b>Standard Visitor visa</b> — before they travel.</li>'
             '<li>You <b>apply online</b> and then <b>attend an appointment at a visa application centre</b>, where your fingerprints and photo are taken and you show your documents. You get your passport back on the same day.</li>'
             '<li><b>The earliest you can apply is 3 months before you travel.</b> Once you have applied, proved your identity and provided your documents, GOV.UK says you will <b>usually get a decision within 3 weeks</b>; it can take longer, for example if more evidence is needed.</li>'
             '<li>As a Standard Visitor you can <b>usually stay up to 6 months</b>. Your passport must be <b>valid for the whole stay</b>, and you must show that you will leave at the end of your visit, can support yourself during the trip and can pay for your return journey.</li>'
             '<li><b>Each family member needs their own application</b> and their own appointment. You may not work in the UK on a visitor visa.</li>'
             '<li>UK Visas and Immigration advises <b>not to book travel until you have a decision</b>. The UK is not in the Schengen area: a UK visa does not cover France or other Schengen countries, and a Schengen visa does not cover the UK.</li></ul>'
             f'<p class="hx-checked">Checked {CHECKED} · sources: <a href="{SRC_CHECK}" target="_blank" rel="noopener nofollow">GOV.UK — Check if you need a UK visa</a> · <a href="{SRC_SV}" target="_blank" rel="noopener nofollow">GOV.UK — Visit the UK as a Standard Visitor</a> · <a href="{SRC_APPLY}" target="_blank" rel="noopener nofollow">GOV.UK — Apply for a Standard Visitor visa</a> · <a href="{SRC_TIMES}" target="_blank" rel="noopener nofollow">GOV.UK — Visa processing times</a></p></div>'
             '<div class="hx-vnote"><p><b>Please note:</b> whether a visa is granted is always the decision of UK Visas and Immigration, and entry at the border is decided by UK Border Force. We help you prepare a complete, honest application, but we never promise an outcome we do not control.</p>'
             '<p>We share a document checklist that matches your itinerary, plan your trip so you can apply early, and confirm non-refundable bookings only after your visa decision.</p></div></div></section>')
    inc = [('doc', 'Visa guidance', 'A clear document checklist, a day-by-day itinerary and hotel details that match your application, and help planning your appointment dates.'), ('pin', 'Central hotels', 'Named hotels in central London, Edinburgh and the Highlands, with the room type you choose.'),
           ('team', 'Transfers &amp; trains', 'Airport transfers, London–Edinburgh train tickets and a private car or guided coach for day tours, as you prefer.'), ('globe', 'Sightseeing &amp; tickets', 'Day tours to Stonehenge and Bath, Oxford and the Cotswolds or the Highlands, and tickets for attractions such as the London Eye or the Tower of London.'),
           ('food', 'Meal plan', 'Breakfast at hotels; vegetarian and Jain needs noted, with Indian and vegetarian restaurant suggestions for every day.'), ('award', 'Flights optional', 'Land-only, or a full package with international flights from your nearest Indian airport.')]
    h.append('<section id="whats-included" class="hx-sec"><span class="hx-eye">Your package</span><h2>What a Suzu UK package includes</h2><div class="hx-inc">'
             + ''.join(f'<div>{svg(i)}<span><b>{t}</b><span>{d}</span></span></div>' for i, t, d in inc) + '</div></section>')
    steps = [('chat', 'Tell us the basics', 'Dates, travellers and the kind of trip you want. A WhatsApp message is enough.'),
             ('doc', 'Get a costed itinerary', 'A day-by-day plan with named hotels and a clear per-person price, usually within 24 hours.'),
             ('sliders', 'Adjust until it fits', 'Change the hotels, the cities, the trains or the tours. We re-quote as needed.'),
             ('lock', 'Confirm with a token', 'Lock your plan with a small token amount; the balance is paid later, as agreed in writing.')]
    h.append('<section id="how-booking-works" class="hx-sec"><span class="hx-eye">Simple process</span><h2>How booking works</h2><div class="hx-steps">'
             + ''.join(f'<div class="hx-step"><div class="hx-n">{svg(i)}</div><b>{t}</b><p>{d}</p></div>' for i, t, d in steps) + '</div></section>')
    h.append('<section id="uk-faq" class="hx-sec"><span class="hx-eye">FAQ</span><h2>Common questions about a UK tour</h2><div class="hx-faqs">'
             + ''.join(f'<details class="hx-faq"{" open" if k == 0 else ""}><summary>{html.escape(q)}</summary><div class="hx-ans"><p>{html.escape(a)}</p></div></details>' for k, (q, a) in enumerate(FAQ)) + '</div></section>')
    h.append('<section id="more-destinations" class="hx-sec"><span class="hx-eye">Explore more</span><h2>Explore more destinations</h2>'
             '<p class="hx-sub">Every trip is planned the same way — your dates, your budget, one team from quote to return. <a href="https://suzutravels.com/international-tour-packages/">See all international holidays →</a></p><div class="hx-mini">'
             + ''.join(f'<a class="hx-mc" href="https://suzutravels.com/{p}/"><img src="https://suzutravels.com/wp-content/uploads/2026/10/{img}.webp" alt="{html.escape(n)} holiday — Suzu Travels" width="640" height="360" loading="lazy" decoding="async"><span><b>{html.escape(n)}</b><em>{html.escape(e)}</em></span></a>' for p, n, img, e in REL) + '</div></section>')
    h.append(f'<div class="hx-final"><img src="{U(FINAL)}" alt="{A(FINAL)}" width="1600" height="900" loading="lazy" decoding="async">'
             '<h2>Plan your UK trip</h2><p>Send us your dates and group size. We will come back with a costed, day-by-day London and Scotland itinerary you can compare — no obligation.</p>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Request a UK Quote {svg("arrow")}</a><a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div>'
             '<p class="hx-contact">Or call <strong>+91 70874 88961</strong> · <a href="mailto:info@suzutravels.com">info@suzutravels.com</a></p></div>')
    seen = []
    for k in HERO + GAL + [FINAL]:
        v = M[k]
        if (v['credit'], v['src']) not in seen:
            seen.append((v['credit'], v['src']))
    h.append('<details class="hx-credits"><summary>Photo credits</summary><p>' + ' · '.join(f'<a href="{html.escape(s, quote=True)}" rel="nofollow noopener" target="_blank">{html.escape(c)}</a> (Unsplash License)' for c, s in seen) + '</p></details>')
    ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}
    h.append('<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + '</script><script>' + JS + '</script></div>')
    out = ''.join(h)
    assert '\n' not in out.replace('\\n', '')
    js = out[out.rfind('<script>'):]
    assert '&' not in js and '//' not in js
    return out

if __name__ == '__main__':
    o = build()
    open('pages/uk-tour-packages.html', 'w').write(o)
    print('pages/uk-tour-packages.html', len(o))
