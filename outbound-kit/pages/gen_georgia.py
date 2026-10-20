#!/usr/bin/env python3
"""Georgia country page (.hx design system; same template as gen_dubai.py / gen_turkey.py).
Run from outbound-kit/:  python3 pages/gen_georgia.py <PAGE_ID>  -> pages/georgia-tour-packages.html (one line)
Facts: visa/entry checked 20 Oct 2026 against official Georgian sources (e-Visa portal evisa.gov.ge, MFA Georgia
Government Ordinance No 256 list, Georgian National Tourism Administration georgia.travel). No prices.
"""
import json, html, sys, os
sys.path.insert(0, os.getcwd())
import gen_hub as G

PID = int(sys.argv[1]) if len(sys.argv) > 1 else 0
M = G.M
svg, WA_SVG, wa = G.svg, G.WA_SVG, G.wa
CHECKED = '20 October 2026'
SRC_EV = 'https://www.evisa.gov.ge/geovisa/countries/index.html'
SRC_ORD = 'https://gc-pfiles.mfa.gov.ge/DocFiles//2023/12/14/LegalAct/37/9be1574b-1684-4cfd-89d0-d57c572df9fc.pdf'
SRC_GNTA = 'https://georgia.travel/coming-to-georgia/georgia-travel-visa-application'

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
body.page-id-PID .page-header:before{content:"Holidays abroad \00B7  Georgia";display:inline-block;font:800 12px/1 "Plus Jakarta Sans",sans-serif;letter-spacing:.18em;text-transform:uppercase;color:#1a1606;background:#E2C158;padding:8px 13px;border-radius:999px;margin-bottom:16px}
body.page-id-PID .page-header .entry-title{color:#fff!important;font-family:"Sora","Plus Jakarta Sans",sans-serif!important;font-size:clamp(34px,4.2vw,58px)!important;line-height:1.06!important;letter-spacing:-.035em!important;margin:0!important;font-weight:800!important;max-width:15ch;text-shadow:0 2px 24px rgba(0,0,0,.35)}
@media(max-width:1100px){.hx .hx-cards{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-itin{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-visa{grid-template-columns:1fr}.hx .hx-inc,.hx .hx-steps{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:700px){body.page-id-PID .page-header{left:14px;right:14px;padding:26px 18px 0}body.page-id-PID .page-header:before{font-size:10.5px;padding:7px 11px;margin-bottom:12px}body.page-id-PID .page-header .entry-title{font-size:33px!important}.hx .hx-facts{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-pg{grid-template-columns:repeat(2,minmax(0,1fr));grid-auto-rows:150px}.hx .hx-pg figure:first-child{grid-column:span 2;grid-row:span 1}.hx .hx-pg figure:nth-child(4){grid-row:span 1}.hx .hx-pg figure:nth-child(8){display:none}.hx .hx-cards,.hx .hx-itin,.hx .hx-inc,.hx .hx-steps{grid-template-columns:1fr}.hx .hx-mini{grid-template-columns:repeat(2,minmax(0,1fr))}}
.hx .hx-pg p,.hx .hx-cards>p,.hx .hx-itin>p,.hx .hx-inc>p,.hx .hx-facts>p{display:none}
""".replace('PID', str(PID))
EXTRA += "@media(min-width:1101px){.hx .hx-itin{grid-template-columns:repeat(3,minmax(0,1fr))}}"
CSS = ' '.join(l.strip() for l in (base + EXTRA).strip().splitlines() if l.strip() and not l.strip().startswith('/*'))
HERO = ['georgia-1', 'georgia-2', 'georgia-3', 'georgia-4', 'georgia-5', 'georgia-6']
GAL = ['georgia-6', 'georgia-7', 'georgia-9', 'georgia-8', 'georgia-2', 'georgia-10', 'georgia-4', 'georgia-5']
CC = 'Georgia'

FAQ = [
    ("Do Indians need a visa for Georgia?", "Yes, Indian ordinary passport holders need a visa for Georgia. India is on the list of countries that can apply for a Georgian e-Visa on the official portal evisa.gov.ge. If you hold a valid visa or residence permit of a country on Georgia's official list — such as the USA, the UK, Canada, Australia, Japan, EU member states, the UAE, Saudi Arabia, Qatar, Oman, Kuwait or Bahrain — you may enter without a Georgian visa for up to 90 days in any 180-day period, as long as that visa or permit is valid on the day you enter. Entry is always the decision of the Georgian authorities."),
    ("How many days are enough for Georgia?", "Five to six nights covers Tbilisi, the mountain drive to Kazbegi (with Mtskheta, Ananuri and Gudauri on the way) and a day in the Kakheti wine region. With seven or eight nights you can add Batumi on the Black Sea coast or slow the pace down."),
    ("When is the best time to visit Georgia from India?", "May to June and September to October suit most Indian travellers: pleasant days in Tbilisi and green, open mountain roads. July and August are warm in Tbilisi and pleasant in the mountains. December to March brings snow — Gudauri is a ski resort — but mountain roads can close for a while after heavy snowfall."),
    ("Can we see snow in Georgia?", "Yes. In winter the Gudauri and Kazbegi area is usually snow-covered, and Gudauri has ski slopes and chairlifts. The high mountain road can close temporarily after heavy snow, so we keep a flexible day in winter plans and check road conditions before the drive."),
    ("Is vegetarian food easy to find in Georgia?", "Yes. Georgian food has many vegetarian dishes — cheese-filled khachapuri breads, bean stew (lobio), vegetable and walnut pkhali, aubergine rolls and fresh salads — and Tbilisi has Indian restaurants. Jain meals need advance notice, which we arrange with hotels where possible."),
    ("Why are there no prices on this page?", "Georgia costs depend on your dates, hotel category, the vehicle you need and the airfare from India. Instead of a teaser price that changes when you ask, we send a costed, day-by-day quote for your dates — usually within 24 hours."),
]

JS = ("(function(){var f=document.getElementById('hxPlan');if(!f){return;}f.addEventListener('submit',function(e){e.preventDefault();"
      "var d=f.querySelector('[name=d]').value,s=f.querySelector('[name=s]').value,m=f.querySelector('[name=m]').value,a=f.querySelector('[name=a]').value,k=f.querySelector('[name=k]').value,c=f.querySelector('[name=c]').value;"
      "var t='Hi Suzu Travels, please send me a costed Georgia itinerary.\\nTrip: '+d+'\\nTrip type: '+s+'\\nTravel month: '+m+'\\nAdults: '+a+'\\nChildren: '+k;"
      "if(c){t=t+'\\nDeparting from: '+c;}"
      "window.open('https:'+String.fromCharCode(47,47)+'wa.me/917087488961?text='+encodeURIComponent(t),'_blank','noopener');});})();")

REL = [('dubai-tour-packages', 'Dubai', 'suzu-abroad-dubai', 'Burj Khalifa, desert, Abu Dhabi'), ('turkey-tour-packages', 'Turkey', 'suzu-abroad-turkey', 'Istanbul, Cappadocia, Pamukkale'),
       ('nepal-tour-packages', 'Nepal', 'suzu-card-nepal', 'No visa for Indians'), ('bhutan-tour-packages', 'Bhutan', 'suzu-card-bhutan', 'Paro, Thimphu, Punakha'),
       ('sri-lanka-tour-packages', 'Sri Lanka', 'suzu-card-sri-lanka', 'Beaches & tea country'), ('maldives-tour-packages', 'Maldives', 'suzu-card-maldives', 'Overwater villas'),
       ('thailand-tour-packages', 'Thailand', 'suzu-card-thailand', 'Bangkok, Phuket, Krabi'), ('singapore-tour-packages', 'Singapore', 'suzu-card-singapore', 'City, Sentosa, Universal'),
       ('malaysia-tour-packages', 'Malaysia', 'suzu-card-malaysia', 'KL, Langkawi, Genting'), ('vietnam-tour-packages', 'Vietnam', 'suzu-card-vietnam', 'Hanoi, Ha Long, Hoi An'),
       ('bali-tour-packages', 'Bali', 'suzu-card-bali', 'Ubud, villas, temples')]

def build():
    W = "Hi Suzu Travels, I'm planning a Georgia trip. Please share a quote."
    h = [f'<div class="suzu-intl hx hx-country"><style>{CSS}</style>']
    slides = ''.join(f'<div class="hx-slide"><img src="{U(s)}" alt="{A(s)}" width="1600" height="1000" {"fetchpriority=\"high\" loading=\"eager\"" if i == 0 else "loading=\"lazy\""} decoding="async"><span class="hx-cap">{C(s)}</span></div>' for i, s in enumerate(HERO))
    h.append('<section class="hx-hero" aria-label="Georgia tour packages from India"><div class="hx-slides">' + slides + '</div><div class="hx-copy">'
             '<p class="hx-lede">The Gergeti Trinity Church high above Kazbegi, the old town and fortress walls of Tbilisi, the monasteries of Mtskheta, Ananuri fortress on the mountain road and snow at Gudauri in winter — Georgia is a compact, scenic holiday abroad for Indian travellers. We plan it to your dates, your budget and your pace.</p>'
             '<div class="hx-badges">'
             f'<span class="hx-badge">{svg("globe")}Tbilisi, Kazbegi &amp; more</span><span class="hx-badge">{svg("food")}Vegetarian meals arranged</span>'
             f'<span class="hx-badge">{svg("team")}Families, couples &amp; groups</span><span class="hx-badge">{svg("doc")}Honest visa guidance</span></div>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Get a Georgia Quote {svg("arrow")}</a>'
             f'<a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div></div>'
             '<form class="hx-plan" id="hxPlan" aria-label="Get a costed Georgia itinerary on WhatsApp"><h3>Plan my Georgia trip</h3>'
             '<p>Tell us the basics — we reply on WhatsApp with a costed, day-by-day plan, usually within 24 hours.</p><div class="hx-f">'
             '<label class="hx-full">Trip<select name="d"><option>Tbilisi only</option><option selected>Tbilisi + Kazbegi (Gudauri, Ananuri)</option><option>Tbilisi + Kazbegi + Kakheti wine region</option><option>Georgia with Batumi (Black Sea)</option><option>Snow trip — Gudauri in winter</option><option>Georgia combined with another country</option></select></label>'
             '<label>Trip type<select name="s"><option>Family</option><option>Honeymoon / couple</option><option>Friends</option><option>Group</option><option>Corporate / MICE</option></select></label>'
             f'<label>Travel month<select name="m">{G.months()}</select></label>'
             '<label>Adults<select name="a"><option>1</option><option selected>2</option><option>3</option><option>4</option><option>5</option><option>6</option><option>7–10</option><option>11–20</option><option>20+</option></select></label>'
             '<label>Children<select name="k"><option>0</option><option>1</option><option>2</option><option>3</option><option>4+</option></select></label>'
             '<label class="hx-full">Departing from<input name="c" type="text" placeholder="e.g. Delhi, Mumbai, Chandigarh" autocomplete="address-level2"></label></div>'
             f'<button class="hx-btn" type="submit">{WA_SVG}Get my Georgia plan on WhatsApp</button><small>Opens WhatsApp with your details filled in. We do not store anything on this page.</small></form></section>')
    h.append('<div class="hx-trust">'
             f'<div>{svg("clock")}<span><b>Quote in ~24 hours</b><span>Costed, day by day</span></span></div>'
             f'<div>{svg("doc")}<span><b>Honest visa guidance</b><span>Official rules, checked</span></span></div>'
             f'<div>{svg("shield")}<span><b>HP Tourism registered</b><span>Reg. DTO-MND-11-243/2022</span></span></div>'
             f'<div>{svg("chat")}<span><b>One team, start to finish</b><span>On WhatsApp while you travel</span></span></div></div>')
    h.append('<nav class="hx-toc" aria-label="On this page"><a href="#why-georgia">Why Georgia</a><a href="#georgia-in-photos">Photos</a><a href="#how-to-choose">Choose your trip</a><a href="#sample-itinerary">Sample itinerary</a><a href="#when-to-go">When to go</a><a href="#visa-and-entry">Visa &amp; entry</a><a href="#whats-included">What\'s included</a><a href="#georgia-faq">FAQ</a></nav>')
    facts = [('Getting there', 'Flights to Tbilisi — we compare options from your city'), ('Time difference', 'Georgia is 1 hr 30 min behind IST'), ('Currency', 'Georgian Lari (GEL)'),
             ('Best season', 'May to June, September to October; Dec to Mar for snow'), ('Typical trip', '5 to 7 nights'), ('Language', 'Georgian; English in hotels and tourist areas')]
    h.append('<section id="why-georgia" class="hx-sec"><span class="hx-eye">Georgia (Sakartvelo)</span><h2>Why Georgia works so well for Indian travellers</h2>'
             '<p class="hx-sub">Georgia is small, so a short holiday covers a lot: Tbilisi\'s old town, sulphur-bath quarter and riverside parks, the ancient churches of Mtskheta, the mountain road past Ananuri and Gudauri to Kazbegi and the Caucasus peaks, and the vineyards and hill town of Sighnaghi in Kakheti. Distances are short, the scenery changes every hour, and the food has plenty of vegetarian choices.</p>'
             '<div class="hx-facts">' + ''.join(f'<div class="hx-fact"><b>{a}</b><span>{b}</span></div>' for a, b in facts) + '</div></section>')
    h.append('<section id="georgia-in-photos" class="hx-sec"><span class="hx-eye">Real places</span><h2>Georgia in photos</h2>'
             '<p class="hx-sub">Tbilisi, Mtskheta, Ananuri, Gudauri and Kazbegi — the places on a classic Suzu Georgia itinerary. Photos by Unsplash photographers, credited below.</p><div class="hx-pg">'
             + ''.join(f'<figure><img src="{U(k)}" alt="{A(k)}" width="800" height="600" loading="lazy" decoding="async"><figcaption>{C(k)}</figcaption></figure>' for k in GAL) + '</div></section>')
    cards = [('Couples', 'Honeymoon', 'A boutique stay in old Tbilisi, a mountain-view room in Kazbegi and a slow day among the vineyards of Kakheti. Add Batumi on the Black Sea if you have more time.'),
             ('First trip to Georgia', 'Classic circuit', 'Tbilisi, Mtskheta, Ananuri, Gudauri and Kazbegi, with a Kakheti day trip, in 5–7 nights. The trip most first-time visitors from India choose.'),
             ('Families', 'Family holiday', 'Two hotel bases, a private vehicle with driver, short drives and rest built into the day. In winter, a snow day at Gudauri is a favourite with children.'),
             ('Groups', 'Groups &amp; corporate', 'Coaches with guides, group check-ins, conference venues and team dinners. Tell us the group size and we quote accordingly, including B2B for travel agents.')]
    stays = [('Old Tbilisi', 'Stay near the old town, Narikala fortress and the sulphur-bath quarter — everything on foot. The easiest base for a first visit.'),
             ('Rustaveli &amp; Vera, Tbilisi', 'Central, with wide avenues, museums, cafés and easy taxis. Good for families who prefer larger city hotels.'),
             ('Kazbegi (Stepantsminda) or Gudauri', 'Mountain hotels with views of the Caucasus. Kazbegi for the Gergeti church in summer, Gudauri for snow and ski slopes in winter.'),
             ('Sighnaghi or Batumi', 'Sighnaghi is a small hill town in the Kakheti wine region; Batumi is a Black Sea city for a few beach and promenade days in summer.')]
    h.append('<section id="how-to-choose" class="hx-sec"><span class="hx-eye">How to choose</span><h2>Choose the Georgia trip that fits you</h2>'
             '<p class="hx-sub">Start from the kind of trip you want — we fine-tune the days, hotels and pace to your group.</p><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><span class="hx-tag">{t}</span><h3>{n}</h3><p>{d}</p></div>' for t, n, d in cards) + '</div>'
             '<h3 style="margin-top:30px">Where to stay — it shapes your whole trip</h3><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><h3>{n}</h3><p>{d}</p></div>' for n, d in stays) + '</div></section>')
    days = [('Day 1', 'Arrive in Tbilisi', 'Airport pickup and hotel check-in. An easy evening walk in the old town and dinner near your hotel.'),
            ('Day 2', 'Old Tbilisi', 'Narikala fortress (by cable car from Rike Park), the sulphur-bath quarter, Metekhi, the Peace Bridge and the old-town lanes with a local guide.'),
            ('Day 3', 'Mtskheta to Kazbegi', 'Jvari Monastery and the old capital Mtskheta, then the mountain road past Ananuri fortress and Gudauri to Kazbegi for the night.'),
            ('Day 4', 'Gergeti &amp; the Caucasus', 'Up to the Gergeti Trinity Church by 4x4 or on foot for the mountain views, then back to Tbilisi via the Gudauri viewpoint.'),
            ('Day 5', 'Kakheti day trip', 'The hill town of Sighnaghi, Bodbe and a family-run vineyard visit (grape juice and churchkhela for non-drinkers), back to Tbilisi.'),
            ('Day 6', 'Fly home', 'A last coffee or shopping stop, then the transfer to Tbilisi airport for your flight home.')]
    h.append('<section id="sample-itinerary" class="hx-sec"><span class="hx-eye">Sample plan</span><h2>A sample 6-day Tbilisi, Kazbegi &amp; Kakheti itinerary</h2>'
             '<p class="hx-sub">The classic first trip to Georgia. We rebuild it around you — a snow day at Gudauri in winter, Batumi for a longer summer trip, fewer hotel changes for families.</p><div class="hx-itin">'
             + ''.join(f'<div class="hx-day"><i>{a}</i><b>{b}</b><p>{c}</p></div>' for a, b, c in days) + '</div></section>')
    seasons = [('Apr – Jun', '<span class="hx-ok">Best</span>', 'Spring, mild to warm', 'Green valleys and comfortable sightseeing. In April there can still be snow on the high mountain road. May and June are ideal for Kazbegi.'),
               ('Jul – Aug', '<span class="hx-mid">Good</span>', 'Warm in Tbilisi, cool in the mountains', 'Busy summer season. A good time to add Batumi on the Black Sea; plan city walks for mornings and evenings.'),
               ('Sep – Oct', '<span class="hx-ok">Best</span>', 'Warm days, cool evenings', 'Pleasant weather and the grape harvest season in Kakheti. Pack a jacket for Kazbegi.'),
               ('Nov – Mar', '<span class="hx-mid">Snow season</span>', 'Cold, snow in the mountains', 'Snow at Gudauri and Kazbegi and ski slopes in Gudauri. The mountain road can close for a while after heavy snow, so we keep a flexible day.')]
    h.append('<section id="when-to-go" class="hx-sec"><span class="hx-eye">Best season</span><h2>When to go to Georgia</h2>'
             '<p class="hx-sub">Late spring and early autumn suit most Indian travellers; winter is for those who want snow. We check road and weather conditions against your dates.</p>'
             '<div class="hx-tw"><table class="hx-t"><thead><tr><th>Months</th><th>Verdict</th><th>Weather</th><th>What it means for your trip</th></tr></thead><tbody>'
             + ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in seasons) + '</tbody></table></div></section>')
    h.append('<section id="visa-and-entry" class="hx-sec"><span class="hx-eye">Visa &amp; entry</span><h2>Visa and entry for Indian passport holders</h2>'
             '<div class="hx-visa"><div class="hx-vbox"><h3>What the official rules say</h3><ul>'
             '<li>Indian <b>ordinary passport holders need a visa</b> to enter Georgia. (Only Indian diplomatic and official/service passport holders are exempt.)</li>'
             '<li><b>e-Visa:</b> India is on the list of countries whose citizens can apply on the <b>official Georgian e-Visa portal, evisa.gov.ge</b>. Tourists are asked for a photo, a copy of the passport, proof of accommodation, a return ticket, travel insurance and proof of funds.</li>'
             '<li><b>Visa-free with another visa or residence permit:</b> if you hold a valid visa or residence permit of a country on Georgia\'s official list — including the USA, the UK, Canada, Australia, Japan, EU member states, Switzerland, Norway, the UAE, Saudi Arabia, Qatar, Oman, Kuwait and Bahrain — you may enter and stay without a Georgian visa for <b>90 days in any 180-day period</b>. The visa or permit must be valid on the day you enter Georgia.</li>'
             '<li>Georgia\'s National Tourism Administration says a decision on a visa is made within 5 to 30 calendar days depending on the category — so apply well before your travel date.</li></ul>'
             f'<p class="hx-checked">Checked {CHECKED} · sources: <a href="{SRC_EV}" target="_blank" rel="noopener nofollow">Georgia e-Visa portal — eligible countries</a> · <a href="{SRC_ORD}" target="_blank" rel="noopener nofollow">Government of Georgia Ordinance No 256 (list of countries whose visa/residence permit allows visa-free entry), Ministry of Foreign Affairs of Georgia</a> · <a href="{SRC_GNTA}" target="_blank" rel="noopener nofollow">Georgian National Tourism Administration — visa information</a></p></div>'
             '<div class="hx-vnote"><p><b>Please note:</b> visa approval and entry at the border are always the decision of the Georgian authorities. We guide you through the documents and timelines honestly, but we never promise an outcome we do not control.</p>'
             '<p>Apply only on the official portal, and keep printed copies of your hotel bookings, return ticket and insurance with you when you travel.</p></div></div></section>')
    inc = [('doc', 'Visa guidance', 'Document checklist and e-Visa support — or confirmation that your existing visa or permit qualifies.'), ('pin', 'Hotels in the right area', 'Named hotels — old Tbilisi, and a mountain-view stay in Kazbegi or Gudauri.'),
           ('team', 'Private vehicle &amp; driver', 'Airport pickup and drop, and a private car, van or coach with driver for the mountain and wine-region days.'), ('globe', 'Guided sightseeing', 'Local guides for Tbilisi and Mtskheta; 4x4 to Gergeti where the road needs it.'),
           ('food', 'Meal plan', 'Breakfast as standard; vegetarian and Jain meals arranged on request where hotels can.'), ('award', 'Flights optional', 'Land-only, or a full package with international flights from your nearest Indian airport.')]
    h.append('<section id="whats-included" class="hx-sec"><span class="hx-eye">Your package</span><h2>What a Suzu Georgia package includes</h2><div class="hx-inc">'
             + ''.join(f'<div>{svg(i)}<span><b>{t}</b><span>{d}</span></span></div>' for i, t, d in inc) + '</div></section>')
    steps = [('chat', 'Tell us the basics', 'Dates, travellers and the kind of Georgia trip you want. A WhatsApp message is enough.'),
             ('doc', 'Get a costed itinerary', 'A day-by-day plan with named hotels and a clear per-person price, usually within 24 hours.'),
             ('sliders', 'Adjust until it fits', 'Add Batumi, a snow day or a wine-region night, upgrade a hotel, change the pace. We re-quote as needed.'),
             ('lock', 'Confirm with a token', 'Lock your rate with a small token amount; the balance is paid later, as agreed in writing.')]
    h.append('<section id="how-booking-works" class="hx-sec"><span class="hx-eye">Simple process</span><h2>How booking works</h2><div class="hx-steps">'
             + ''.join(f'<div class="hx-step"><div class="hx-n">{svg(i)}</div><b>{t}</b><p>{d}</p></div>' for i, t, d in steps) + '</div></section>')
    h.append('<section id="georgia-faq" class="hx-sec"><span class="hx-eye">FAQ</span><h2>Common questions about Georgia</h2><div class="hx-faqs">'
             + ''.join(f'<details class="hx-faq"{" open" if k == 0 else ""}><summary>{html.escape(q)}</summary><div class="hx-ans"><p>{html.escape(a)}</p></div></details>' for k, (q, a) in enumerate(FAQ)) + '</div></section>')
    h.append('<section id="more-destinations" class="hx-sec"><span class="hx-eye">Explore more</span><h2>Explore more destinations</h2>'
             '<p class="hx-sub">Every trip is planned the same way — your dates, your budget, one team from quote to return. <a href="https://suzutravels.com/international-tour-packages/">See all international holidays →</a></p><div class="hx-mini">'
             + ''.join(f'<a class="hx-mc" href="https://suzutravels.com/{p}/"><img src="https://suzutravels.com/wp-content/uploads/2026/10/{img}.webp" alt="{html.escape(n)} holiday — Suzu Travels" width="640" height="360" loading="lazy" decoding="async"><span><b>{html.escape(n)}</b><em>{html.escape(e)}</em></span></a>' for p, n, img, e in REL) + '</div></section>')
    h.append(f'<div class="hx-final"><img src="{U("georgia-6")}" alt="{A("georgia-6")}" width="1600" height="900" loading="lazy" decoding="async">'
             '<h2>Plan your Georgia trip</h2><p>Send us your dates and group size. We will come back with a costed, day-by-day Georgia itinerary you can compare — no obligation.</p>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Request a Georgia Quote {svg("arrow")}</a><a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div>'
             '<p class="hx-contact">Or call <strong>+91 70874 88961</strong> · <a href="mailto:info@suzutravels.com">info@suzutravels.com</a></p></div>')
    seen = []
    for k in HERO + GAL:
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
    open('pages/georgia-tour-packages.html', 'w').write(o)
    print('pages/georgia-tour-packages.html', len(o))
