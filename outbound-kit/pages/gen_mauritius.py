#!/usr/bin/env python3
"""Mauritius page — .hx design system; same template as gen_switzerland.py / gen_georgia.py.
Run from outbound-kit/:  python3 pages/gen_mauritius.py <PAGE_ID>  -> pages/mauritius-tour-packages.html (one line)
Facts: Passport and Immigration Office (PIO) Mauritius checked 25 Oct 2026 — "Visa Requirement Country-wise" list
(Visa-Requirement-Country-2025.pdf, linked from the Visa Requirements page): India = "No visa required."; Travel
Requirements page (passport valid beyond stay, return ticket, funds, confirmed hotel booking); Health and Entry
Regulations (All-in-One Travel Form + Health Declaration Form before boarding). No prices. 6-day itinerary = 3 columns.
"""
import json, html, sys, os
sys.path.insert(0, os.getcwd())
import gen_hub as G

PID = int(sys.argv[1]) if len(sys.argv) > 1 else 0
M = G.M
svg, WA_SVG, wa = G.svg, G.WA_SVG, G.wa
CHECKED = '25 October 2026'
SRC_PIO = 'https://passport.govmu.org/passport/?page_id=605'
SRC_PIO_LIST = 'https://passport.govmu.org/passport/wp-content/uploads/2021/03/Visa-Requirement-Country-2025.pdf'
SRC_PIO_REQ = 'https://passport.govmu.org/passport/?page_id=587'
SRC_PIO_HEALTH = 'https://passport.govmu.org/passport/?p=1494'

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
.hx .hx-itin{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin-top:18px}
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
body.page-id-PID .page-header:before{content:"Holidays abroad \00B7  Mauritius";display:inline-block;font:800 12px/1 "Plus Jakarta Sans",sans-serif;letter-spacing:.18em;text-transform:uppercase;color:#1a1606;background:#E2C158;padding:8px 13px;border-radius:999px;margin-bottom:16px}
body.page-id-PID .page-header .entry-title{color:#fff!important;font-family:"Sora","Plus Jakarta Sans",sans-serif!important;font-size:clamp(34px,4.2vw,58px)!important;line-height:1.06!important;letter-spacing:-.035em!important;margin:0!important;font-weight:800!important;max-width:15ch;text-shadow:0 2px 24px rgba(0,0,0,.35)}
@media(max-width:1100px){.hx .hx-cards{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-itin{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-visa{grid-template-columns:1fr}.hx .hx-inc,.hx .hx-steps{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:700px){body.page-id-PID .page-header{left:14px;right:14px;padding:26px 18px 0}body.page-id-PID .page-header:before{font-size:10.5px;padding:7px 11px;margin-bottom:12px}body.page-id-PID .page-header .entry-title{font-size:33px!important}.hx .hx-facts{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-pg{grid-template-columns:repeat(2,minmax(0,1fr));grid-auto-rows:150px}.hx .hx-pg figure:first-child{grid-column:span 2;grid-row:span 1}.hx .hx-pg figure:nth-child(4){grid-row:span 1}.hx .hx-pg figure:nth-child(8){display:none}.hx .hx-cards,.hx .hx-itin,.hx .hx-inc,.hx .hx-steps{grid-template-columns:1fr}.hx .hx-mini{grid-template-columns:repeat(2,minmax(0,1fr))}}
.hx .hx-pg p,.hx .hx-cards>p,.hx .hx-itin>p,.hx .hx-inc>p,.hx .hx-facts>p{display:none}
""".replace('PID', str(PID))
CSS = ' '.join(l.strip() for l in (base + EXTRA).strip().splitlines() if l.strip() and not l.strip().startswith('/*'))
HERO = ['mauritius-1', 'mauritius-2', 'mauritius-5', 'mauritius-3', 'mauritius-6', 'mauritius-10']
GAL = ['mauritius-10', 'mauritius-4', 'mauritius-7', 'mauritius-3', 'mauritius-8', 'mauritius-2', 'mauritius-5', 'mauritius-6']
FINAL = 'mauritius-9'
CC = 'Mauritius'

FAQ = [
    ("Do Indians need a visa for Mauritius?", "According to the Passport and Immigration Office of Mauritius, Indian passport holders do not need a visa to visit Mauritius. You still have to meet the entry conditions: a passport valid beyond your stay, a return ticket, enough funds for the trip and a confirmed hotel booking. The length of stay is granted by the immigration officer on arrival, and entry is always the decision of the Mauritius authorities. We checked these rules on 25 October 2026 and re-check them before every booking."),
    ("How many days are enough for Mauritius?", "Five to six nights covers a north and south sightseeing tour, a day on Île aux Cerfs and time to enjoy the beach. With seven to eight nights you can split your stay between two hotels — for example the east coast and the south-west near Le Morne — and add water activities or a day at a nature park without rushing."),
    ("Which is the best time to visit Mauritius from India?", "Mauritius can be visited all year. May to November is the cooler, drier winter — pleasant for sightseeing, and the windy season that kitesurfers come to Le Morne for. December to April is the hot, humid summer with most of the rain, and tropical cyclones are possible, mainly from January to March. April–May and September–November are good all-round months; we check weather and holiday dates against your plan."),
    ("Is Mauritius good for a honeymoon?", "Yes — it is one of the most popular honeymoon destinations for Indian couples: calm lagoons, beach resorts with private-feeling spaces, sunset catamaran trips and easy sightseeing. We keep hotel changes few, choose the coast that suits your dates and add special touches when you tell us the occasion."),
    ("Is vegetarian and Indian food easy to find in Mauritius?", "Yes. Most Mauritians are of Indian origin, Hindi and Bhojpuri are widely understood, and Indian food, vegetarian dishes and temples are part of everyday life. We note vegetarian and Jain needs with your hotels and suggest restaurants on every tour day."),
    ("Which part of Mauritius should we stay in?", "The north (Grand Baie, Trou aux Biches) is lively, with restaurants and shops close by. The east (Belle Mare, Trou d'Eau Douce) has long beaches and is closest to Île aux Cerfs. The south-west (Le Morne, Flic en Flac) has the sunsets, Le Morne Brabant and easy access to Chamarel. We match the area to your trip style and can split the stay between two coasts."),
    ("Why are there no prices on this page?", "Mauritius costs depend heavily on your dates, the hotel and its meal plan, the room or villa type, the tours you add and the airfare from your city. Instead of a teaser price that changes when you ask, we send a costed, day-by-day quote for your dates — usually within 24 hours."),
]

JS = ("(function(){var f=document.getElementById('hxPlan');if(!f){return;}f.addEventListener('submit',function(e){e.preventDefault();"
      "var d=f.querySelector('[name=d]').value,s=f.querySelector('[name=s]').value,m=f.querySelector('[name=m]').value,a=f.querySelector('[name=a]').value,k=f.querySelector('[name=k]').value,c=f.querySelector('[name=c]').value;"
      "var t='Hi Suzu Travels, please send me a costed Mauritius itinerary.\\nTrip: '+d+'\\nTrip type: '+s+'\\nTravel month: '+m+'\\nAdults: '+a+'\\nChildren: '+k;"
      "if(c){t=t+'\\nDeparting from: '+c;}"
      "window.open('https:'+String.fromCharCode(47,47)+'wa.me/917087488961?text='+encodeURIComponent(t),'_blank','noopener');});})();")

REL = [('dubai-tour-packages', 'Dubai', 'suzu-abroad-dubai', 'Burj Khalifa, desert, Abu Dhabi'), ('maldives-tour-packages', 'Maldives', 'suzu-card-maldives', 'Overwater villas'),
       ('bali-tour-packages', 'Bali', 'suzu-card-bali', 'Ubud, villas, temples'), ('sri-lanka-tour-packages', 'Sri Lanka', 'suzu-card-sri-lanka', 'Beaches & tea country'),
       ('thailand-tour-packages', 'Thailand', 'suzu-card-thailand', 'Bangkok, Phuket, Krabi'), ('turkey-tour-packages', 'Turkey', 'suzu-abroad-turkey', 'Istanbul, Cappadocia, Pamukkale'),
       ('georgia-tour-packages', 'Georgia', 'suzu-abroad-georgia', 'Tbilisi, Kazbegi, Gudauri'), ('azerbaijan-tour-packages', 'Azerbaijan', 'suzu-abroad-azerbaijan', 'Baku, Gabala, Shahdag'),
       ('japan-tour-packages', 'Japan', 'suzu-abroad-japan', 'Tokyo, Fuji, Kyoto, Osaka'), ('europe-tour-packages', 'Europe', 'suzu-abroad-europe', 'Paris, Swiss Alps, Italy'),
       ('switzerland-tour-packages', 'Switzerland', 'suzu-abroad-switzerland', 'Lucerne, Jungfrau, Zermatt'),
       ('uk-tour-packages', 'United Kingdom', 'suzu-abroad-uk', 'London, Stonehenge, Scotland'),
       ('nepal-tour-packages', 'Nepal', 'suzu-card-nepal', 'No visa for Indians'), ('bhutan-tour-packages', 'Bhutan', 'suzu-card-bhutan', 'Paro, Thimphu, Punakha'),
       ('singapore-tour-packages', 'Singapore', 'suzu-card-singapore', 'City, Sentosa, Universal'), ('malaysia-tour-packages', 'Malaysia', 'suzu-card-malaysia', 'KL, Langkawi, Genting'),
       ('vietnam-tour-packages', 'Vietnam', 'suzu-card-vietnam', 'Hanoi, Ha Long, Hoi An')]

def build():
    W = "Hi Suzu Travels, I'm planning a Mauritius trip. Please share a quote."
    h = [f'<div class="suzu-intl hx hx-country"><style>{CSS}</style>']
    slides = ''.join(f'<div class="hx-slide"><img src="{U(s)}" alt="{A(s)}" width="1600" height="1000" {"fetchpriority=\"high\" loading=\"eager\"" if i == 0 else "loading=\"lazy\""} decoding="async"><span class="hx-cap">{C(s)}</span></div>' for i, s in enumerate(HERO))
    h.append('<section class="hx-hero" aria-label="Mauritius tour packages from India"><div class="hx-slides">' + slides + '</div><div class="hx-copy">'
             '<p class="hx-lede">Turquoise lagoons, Le Morne Brabant rising above the sea, waterfalls in green hills and a warm island where Indian food, temples and Hindi are part of everyday life — Mauritius is a favourite of Indian honeymooners and families. We plan it to your dates, budget and pace, with the right coast, hotel and tours, and clear entry guidance from the start.</p>'
             '<div class="hx-badges">'
             f'<span class="hx-badge">{svg("globe")}Beaches, lagoons &amp; island tours</span><span class="hx-badge">{svg("food")}Vegetarian meals planned</span>'
             f'<span class="hx-badge">{svg("team")}Honeymoon, family &amp; groups</span><span class="hx-badge">{svg("doc")}Official entry rules, checked</span></div>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Get a Mauritius Quote {svg("arrow")}</a>'
             f'<a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div></div>'
             '<form class="hx-plan" id="hxPlan" aria-label="Get a costed Mauritius itinerary on WhatsApp"><h3>Plan my Mauritius trip</h3>'
             '<p>Tell us the basics — we reply on WhatsApp with a costed, day-by-day plan, usually within 24 hours.</p><div class="hx-f">'
             '<label class="hx-full">Trip<select name="d"><option selected>Mauritius beach + sightseeing</option><option>Mauritius honeymoon</option><option>Mauritius family holiday</option><option>Two hotels, two coasts</option><option>Mauritius + Dubai stopover</option><option>Not sure yet</option></select></label>'
             '<label>Trip type<select name="s"><option>Honeymoon / couple</option><option>Family</option><option>Friends</option><option>Seniors</option><option>Group</option><option>Corporate / MICE</option></select></label>'
             f'<label>Travel month<select name="m">{G.months()}</select></label>'
             '<label>Adults<select name="a"><option>1</option><option selected>2</option><option>3</option><option>4</option><option>5</option><option>6</option><option>7–10</option><option>11–20</option><option>20+</option></select></label>'
             '<label>Children<select name="k"><option>0</option><option>1</option><option>2</option><option>3</option><option>4+</option></select></label>'
             '<label class="hx-full">Departing from<input name="c" type="text" placeholder="e.g. Delhi, Mumbai, Chandigarh" autocomplete="address-level2"></label></div>'
             f'<button class="hx-btn" type="submit">{WA_SVG}Get my Mauritius plan on WhatsApp</button><small>Opens WhatsApp with your details filled in. We do not store anything on this page.</small></form></section>')
    h.append('<div class="hx-trust">'
             f'<div>{svg("clock")}<span><b>Quote in ~24 hours</b><span>Costed, day by day</span></span></div>'
             f'<div>{svg("doc")}<span><b>Honest entry guidance</b><span>Official rules, checked</span></span></div>'
             f'<div>{svg("shield")}<span><b>HP Tourism registered</b><span>Reg. DTO-MND-11-243/2022</span></span></div>'
             f'<div>{svg("chat")}<span><b>One team, start to finish</b><span>On WhatsApp while you travel</span></span></div></div>')
    h.append('<nav class="hx-toc" aria-label="On this page"><a href="#why-mauritius">Why Mauritius</a><a href="#mauritius-in-photos">Photos</a><a href="#how-to-choose">Choose your trip</a><a href="#sample-itinerary">Sample itinerary</a><a href="#when-to-go">When to go</a><a href="#visa-and-entry">Visa &amp; entry</a><a href="#whats-included">What\'s included</a><a href="#mauritius-faq">FAQ</a></nav>')
    facts = [('Getting there', 'Fly into Sir Seewoosagur Ramgoolam International Airport — we compare routes from your city'), ('Time difference', 'India is 1 hr 30 min ahead of Mauritius'), ('Currency', 'Mauritian rupee (MUR)'),
             ('Best season', 'April to June and September to November; open all year'), ('Typical trip', '5 to 8 nights, one or two hotels'), ('Visa', 'Not required for Indian passport holders, as per PIO Mauritius — entry conditions apply')]
    h.append('<section id="why-mauritius" class="hx-sec"><span class="hx-eye">Mauritius</span><h2>Why Mauritius works so well for Indian travellers</h2>'
             '<p class="hx-sub">Mauritius is a volcanic island in the Indian Ocean ringed by coral reefs and calm lagoons. In a week you can see Le Morne Brabant, a UNESCO World Heritage Site, the coloured earth and waterfall at Chamarel, the sacred lake of Grand Bassin, Port Louis and the Aapravasi Ghat, the immigration depot where indentured workers from India arrived, and spend a day on Île aux Cerfs — and still have time for the beach. Most Mauritians are of Indian origin, so vegetarian food, temples and Hindi are easy to find, and Indian passport holders do not need a visa.</p>'
             '<div class="hx-facts">' + ''.join(f'<div class="hx-fact"><b>{a}</b><span>{b}</span></div>' for a, b in facts) + '</div></section>')
    h.append('<section id="mauritius-in-photos" class="hx-sec"><span class="hx-eye">Real places</span><h2>Mauritius in photos</h2>'
             '<p class="hx-sub">Le Morne Brabant from the air, a palm-lined beach from above, the Albion lighthouse, a waterfall in the hills, Port Louis, the lagoon at Le Morne, Belle Mare on the east coast and a lagoon-side resort at Trou d\'Eau Douce. Photos by Unsplash photographers, credited below.</p><div class="hx-pg">'
             + ''.join(f'<figure><img src="{U(k)}" alt="{A(k)}" width="800" height="600" loading="lazy" decoding="async"><figcaption>{C(k)}</figcaption></figure>' for k in GAL) + '</div></section>')
    cards = [('Couples', 'Honeymoon', 'A beach resort on a calm lagoon, a sunset catamaran, a south-island tour and slow days by the sea. One hotel or two, few transfers, special touches for the occasion.'),
             ('Families &amp; seniors', 'Easy family holiday', 'A family-friendly resort, private transfers, sightseeing at an easy pace, a glass-bottom boat or nature park day for children, and vegetarian meals arranged.'),
             ('Culture', 'Island tours &amp; heritage', 'Grand Bassin, Port Louis and the Aapravasi Ghat, Pamplemousses botanical garden, Chamarel and the Black River Gorges viewpoints — with a driver-guide.'),
             ('Sea &amp; adventure', 'Water days', 'Île aux Cerfs by boat, snorkelling, parasailing or an undersea walk, and dolphin-watching trips off the west coast, chosen to suit your group and the season.')]
    stays = [('North — Grand Baie', 'Lively and convenient, with restaurants, shops and boat trips to the northern islets close by. Good for friends and first-timers.'),
             ('East — Belle Mare', 'Long white beaches and calm lagoons, closest to Île aux Cerfs. Popular with honeymooners and resort lovers.'),
             ('South-west — Le Morne', 'Le Morne Brabant, sunsets over the sea and easy access to Chamarel and the Black River Gorges. Also the kitesurfing coast.'),
             ('West — Flic en Flac', 'A long public beach with sunset views and good value hotels, near Tamarin for dolphin trips and Casela nature park.')]
    h.append('<section id="how-to-choose" class="hx-sec"><span class="hx-eye">How to choose</span><h2>Choose the Mauritius trip that fits you</h2>'
             '<p class="hx-sub">Start from the kind of trip you want — we fine-tune the coast, hotel, meal plan and tours to your group.</p><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><span class="hx-tag">{t}</span><h3>{n}</h3><p>{d}</p></div>' for t, n, d in cards) + '</div>'
             '<h3 style="margin-top:30px">Where to stay — the coast shapes your trip</h3><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><h3>{n}</h3><p>{d}</p></div>' for n, d in stays) + '</div></section>')
    days = [('Day 1', 'Arrive in Mauritius', 'Airport pickup and private transfer to your hotel. The rest of the day on the beach to recover from the flight.'),
            ('Day 2', 'North tour &amp; Port Louis', 'Port Louis with the Caudan Waterfront and the Aapravasi Ghat, Pamplemousses botanical garden and an evening in Grand Baie.'),
            ('Day 3', 'South tour &amp; Chamarel', 'Trou aux Cerfs crater, Grand Bassin, the Black River Gorges viewpoint, the Chamarel waterfall and the Seven Coloured Earth.'),
            ('Day 4', 'Île aux Cerfs', 'A boat day to Île aux Cerfs off the east coast — white sand, calm water and optional water sports.'),
            ('Day 5', 'Free day or sea activity', 'Beach time, or add a catamaran cruise, snorkelling, an undersea walk or a dolphin-watching trip from the west coast.'),
            ('Day 6', 'Fly home', 'Breakfast, last swim if time allows, and a private transfer to the airport.')]
    h.append('<section id="sample-itinerary" class="hx-sec"><span class="hx-eye">Sample plan</span><h2>A sample 6-day Mauritius itinerary</h2>'
             '<p class="hx-sub">The classic first trip: two sightseeing days, an island day and time to relax. We rebuild it around you — add nights, split the stay between two coasts, or add a Dubai stopover on the way.</p><div class="hx-itin">'
             + ''.join(f'<div class="hx-day"><i>{a}</i><b>{b}</b><p>{c}</p></div>' for a, b, c in days) + '</div></section>')
    seasons = [('Apr – Jun', '<span class="hx-ok">Best</span>', 'Warm, drier, cooling down', 'Pleasant beach weather after the summer rains. Late May and June are busy with Indian school holidays, so book hotels early.'),
               ('Jul – Aug', '<span class="hx-mid">Good, cooler</span>', 'Mild winter, windy', 'The coolest months, comfortable for sightseeing. Breezier on the south and east coasts — the season kitesurfers come to Le Morne for.'),
               ('Sep – Nov', '<span class="hx-ok">Best</span>', 'Dry, warming up', 'Sunny, dry and warming — one of the best all-round periods, and popular with honeymooners.'),
               ('Dec – Mar', '<span class="hx-mid">Hot &amp; humid</span>', 'Summer, most rain', 'Hot, humid and the wettest time; tropical cyclones are possible, mainly from January to March. Christmas and New Year are peak dates — book early.')]
    h.append('<section id="when-to-go" class="hx-sec"><span class="hx-eye">Best season</span><h2>When to go to Mauritius</h2>'
             '<p class="hx-sub">Mauritius is a year-round destination. We check the weather, holiday dates and hotel availability against your plan before we quote.</p>'
             '<div class="hx-tw"><table class="hx-t"><thead><tr><th>Months</th><th>Verdict</th><th>Weather</th><th>What it means for your trip</th></tr></thead><tbody>'
             + ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in seasons) + '</tbody></table></div></section>')
    h.append('<section id="visa-and-entry" class="hx-sec"><span class="hx-eye">Visa &amp; entry</span><h2>Mauritius entry rules for Indian passport holders</h2>'
             '<div class="hx-visa"><div class="hx-vbox"><h3>What the official rules say</h3><ul>'
             '<li>The <b>Passport and Immigration Office of Mauritius</b> lists India as <b>&ldquo;No visa required&rdquo;</b> in its country-wise visa requirements. You do not apply for a visa before travel for a holiday.</li>'
             '<li>Every visitor must <b>hold a passport valid beyond the intended stay</b>, a <b>valid return ticket</b>, be eligible to re-enter their home country, have <b>adequate funds</b> for the stay and a <b>confirmed hotel booking</b> (or sponsorship for accommodation). Visitors may not work without a permit.</li>'
             '<li>The <b>length of stay is granted by the immigration officer on arrival</b>. For tourists, the Passport and Immigration Office says a maximum of six months in a calendar year may be granted, case by case.</li>'
             '<li>Under the Quarantine (Health Declaration Form) Regulations 2026, <b>all passengers must complete the All-in-One Travel Form and the Health Declaration Form before boarding</b> a flight to Mauritius. Health-related entry restrictions can change at short notice, so we re-check them before you fly.</li>'
             '<li>Carry printed or phone copies of your hotel confirmation, return ticket and travel insurance for the immigration desk.</li></ul>'
             f'<p class="hx-checked">Checked {CHECKED} · sources: <a href="{SRC_PIO}" target="_blank" rel="noopener nofollow">PIO Mauritius — Visa requirements</a> · <a href="{SRC_PIO_LIST}" target="_blank" rel="noopener nofollow">PIO Mauritius — Visa requirement country-wise (PDF)</a> · <a href="{SRC_PIO_REQ}" target="_blank" rel="noopener nofollow">PIO Mauritius — Travel requirements</a> · <a href="{SRC_PIO_HEALTH}" target="_blank" rel="noopener nofollow">PIO Mauritius — Health and entry regulations</a></p></div>'
             '<div class="hx-vnote"><p><b>Please note:</b> entry at the border is always the decision of the Mauritius immigration authorities. We guide you through the documents honestly, but we never promise an outcome we do not control.</p>'
             '<p>If you plan a stopover on the way — for example in Dubai — that country has its own visa rules, which we check separately for your passport and route.</p></div></div></section>')
    inc = [('doc', 'Entry guidance', 'A clear document checklist, hotel confirmations and a return ticket that match your trip, and help with the All-in-One Travel Form before you fly.'), ('pin', 'Hotels on the right coast', 'Named hotels or resorts in the north, east or south-west, with the room type and meal plan you choose.'),
           ('team', 'Private transfers', 'Airport pickup and drop, and an air-conditioned car with a driver-guide for the sightseeing days.'), ('globe', 'Island tours', 'North and south island tours, Île aux Cerfs by boat, and add-ons such as a catamaran cruise, undersea walk or dolphin trip.'),
           ('food', 'Meal plan', 'Breakfast, half board or all-inclusive as you prefer; vegetarian and Jain needs noted with hotels, plus Indian restaurant suggestions.'), ('award', 'Flights optional', 'Land-only, or a full package with international flights from your nearest Indian airport.')]
    h.append('<section id="whats-included" class="hx-sec"><span class="hx-eye">Your package</span><h2>What a Suzu Mauritius package includes</h2><div class="hx-inc">'
             + ''.join(f'<div>{svg(i)}<span><b>{t}</b><span>{d}</span></span></div>' for i, t, d in inc) + '</div></section>')
    steps = [('chat', 'Tell us the basics', 'Dates, travellers and the kind of trip you want. A WhatsApp message is enough.'),
             ('doc', 'Get a costed itinerary', 'A day-by-day plan with named hotels and a clear per-person price, usually within 24 hours.'),
             ('sliders', 'Adjust until it fits', 'Change the hotel, the coast, the meal plan or the tours. We re-quote as needed.'),
             ('lock', 'Confirm with a token', 'Lock your rate with a small token amount; the balance is paid later, as agreed in writing.')]
    h.append('<section id="how-booking-works" class="hx-sec"><span class="hx-eye">Simple process</span><h2>How booking works</h2><div class="hx-steps">'
             + ''.join(f'<div class="hx-step"><div class="hx-n">{svg(i)}</div><b>{t}</b><p>{d}</p></div>' for i, t, d in steps) + '</div></section>')
    h.append('<section id="mauritius-faq" class="hx-sec"><span class="hx-eye">FAQ</span><h2>Common questions about a Mauritius tour</h2><div class="hx-faqs">'
             + ''.join(f'<details class="hx-faq"{" open" if k == 0 else ""}><summary>{html.escape(q)}</summary><div class="hx-ans"><p>{html.escape(a)}</p></div></details>' for k, (q, a) in enumerate(FAQ)) + '</div></section>')
    h.append('<section id="more-destinations" class="hx-sec"><span class="hx-eye">Explore more</span><h2>Explore more destinations</h2>'
             '<p class="hx-sub">Every trip is planned the same way — your dates, your budget, one team from quote to return. <a href="https://suzutravels.com/international-tour-packages/">See all international holidays →</a></p><div class="hx-mini">'
             + ''.join(f'<a class="hx-mc" href="https://suzutravels.com/{p}/"><img src="https://suzutravels.com/wp-content/uploads/2026/10/{img}.webp" alt="{html.escape(n)} holiday — Suzu Travels" width="640" height="360" loading="lazy" decoding="async"><span><b>{html.escape(n)}</b><em>{html.escape(e)}</em></span></a>' for p, n, img, e in REL) + '</div></section>')
    h.append(f'<div class="hx-final"><img src="{U(FINAL)}" alt="{A(FINAL)}" width="1600" height="900" loading="lazy" decoding="async">'
             '<h2>Plan your Mauritius trip</h2><p>Send us your dates and group size. We will come back with a costed, day-by-day Mauritius itinerary you can compare — no obligation.</p>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Request a Mauritius Quote {svg("arrow")}</a><a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div>'
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
    open('pages/mauritius-tour-packages.html', 'w').write(o)
    print('pages/mauritius-tour-packages.html', len(o))
