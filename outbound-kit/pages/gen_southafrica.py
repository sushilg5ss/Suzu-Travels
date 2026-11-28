#!/usr/bin/env python3
"""South Africa page - .hx design; same template as gen_tanzania.py.
Built 28 Nov 2026 (photos WP 26024-26037; 13 used, 26024 Cape Town panorama from Lion's Head spare - 1920x519, too thin).
Run from outbound-kit/:  python3 pages/gen_southafrica.py <PAGE_ID> -> pages/south-africa-tour-packages.html (one line)
Facts (official South African government sources, read 28 Nov 2026 with curl + headless Chromium):
- dha.gov.za Exempt Countries table: India is exempt only for diplomatic, official and service passports (90 days);
  the Ordinary column is empty -> ordinary Indian passports need a visa.
- dha.gov.za Types of Visas: visitor's visas are for stays of 90 days or less; "Visas are not issued at South African ports
  of entry" and airlines must insist on visas before boarding.
- eta.dha.gov.za/faq (Electronic Travel Authorisation, DHA): visa-required travellers are issued a Port of Entry Visa
  (Section 10(a)); outcome typically within 24 hours; validity typically up to 6 months, multiple entries, each stay up to
  90 days; length of stay decided at the port of entry; currently at OR Tambo, Cape Town, Lanseria and King Shaka airports;
  passport valid >= 7 months from travel date and >= 30 days after visa expiry, machine-readable (ICAO); fees non-refundable;
  approved ETA does not guarantee entry; documents at the port of entry (passport, ETA approval, return ticket,
  accommodation proof, funds, yellow-fever certificate if applicable); minors need an ETA but minors' applications come
  "in a future phase"; if refused, apply through a South African mission or the eVisa system where available.
- sanews.gov.za 12-13 Aug 2026: ETA officially launched 12 Aug 2026 at OR Tambo; pilot began during the G20 Presidency for
  China, India, Indonesia and Mexico; approved travellers receive the ETA within 24 hours.
- dirco.gov.za/newdelhi (South African High Commission, visas section): all applications go to the VFS application centre;
  the High Commission does not accept visa applications directly (ordinary passports).
Keyword Planner IN 28 Nov 2026: "south africa tour package" 390/mo (focus kw), "south africa trip packages" 1,000,
"south africa tours" 1,000, "south africa tour package from india" 260, "south africa trip cost from india" 260,
"south africa visa for indians" 4,400 (Apr peak 6,600), "cape town tour package" 90.
Photos: Wikimedia Commons CC BY-SA 4.0 (Dietmar Rabich / XRay 2024 series, Diego Delso 2018 series).
Season wording is general guidance; no prices; no flight times; no visa fee amount (not stated on the pages read).
"""
import json, html, sys, os
sys.path.insert(0, os.getcwd())
import gen_hub as G

PID = int(sys.argv[1]) if len(sys.argv) > 1 else 0
M = dict(G.M)
PREVIEW = False
svg, WA_SVG, wa = G.svg, G.WA_SVG, G.wa
CHECKED = '28 November 2026'
SRC_EXEMPT = 'https://www.dha.gov.za/index.php/immigration-services/exempt-countries'
SRC_TYPES = 'https://www.dha.gov.za/index.php/immigration-services/types-of-visas'
SRC_ETA = 'https://eta.dha.gov.za/faq'
SRC_NEWS = 'https://www.sanews.gov.za/south-africa/eta-system-quantum-leap-forward-immigration-system'
SRC_HC = 'https://dirco.gov.za/newdelhi/elementor-1431/'

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
body.page-id-PID .page-header:before{content:"Holidays abroad \00B7  South Africa";display:inline-block;font:800 12px/1 "Plus Jakarta Sans",sans-serif;letter-spacing:.18em;text-transform:uppercase;color:#1a1606;background:#E2C158;padding:8px 13px;border-radius:999px;margin-bottom:16px}
body.page-id-PID .page-header .entry-title{color:#fff!important;font-family:"Sora","Plus Jakarta Sans",sans-serif!important;font-size:clamp(34px,4.2vw,58px)!important;line-height:1.06!important;letter-spacing:-.035em!important;margin:0!important;font-weight:800!important;max-width:15ch;text-shadow:0 2px 24px rgba(0,0,0,.35)}
@media(max-width:1100px){.hx .hx-cards{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-itin{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-visa{grid-template-columns:1fr}.hx .hx-inc,.hx .hx-steps{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:700px){body.page-id-PID .page-header{left:14px;right:14px;padding:26px 18px 0}body.page-id-PID .page-header:before{font-size:10.5px;padding:7px 11px;margin-bottom:12px}body.page-id-PID .page-header .entry-title{font-size:33px!important}.hx .hx-facts{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-pg{grid-template-columns:repeat(2,minmax(0,1fr));grid-auto-rows:150px}.hx .hx-pg figure:first-child{grid-column:span 2;grid-row:span 1}.hx .hx-pg figure:nth-child(4){grid-row:span 1}.hx .hx-pg figure:nth-child(8){display:none}.hx .hx-cards,.hx .hx-itin,.hx .hx-inc,.hx .hx-steps{grid-template-columns:1fr}.hx .hx-mini{grid-template-columns:repeat(2,minmax(0,1fr))}}
.hx .hx-pg p,.hx .hx-cards>p,.hx .hx-itin>p,.hx .hx-inc>p,.hx .hx-facts>p{display:none}
""".replace('PID', str(PID))
CSS = ' '.join(l.strip() for l in (base + EXTRA).strip().splitlines() if l.strip() and not l.strip().startswith('/*'))
# 14 Nov 2026: 7-photo gallery — first photo spans 2 columns, one row (2 rows of 4 on desktop, 1+3x2 on phones)
CSS = CSS + ' .hx .hx-pg{grid-auto-rows:230px} .hx .hx-pg figure:first-child{grid-row:span 1} .hx .hx-pg figure:nth-child(4){grid-row:span 1}'
CSS = CSS + ' @media(max-width:700px){.hx .hx-pg{grid-auto-rows:150px} .hx .hx-pg figure:nth-child(8){display:block}}'
# Hostinger WAF (31 Oct 2026) returns 503 for writes containing '@media(' — use the equivalent '@media screen and ('
CSS = CSS.replace('@media(', '@media screen and (')
HERO = ['south-africa-1', 'south-africa-2', 'south-africa-3', 'south-africa-4', 'south-africa-5', 'south-africa-6']
GAL = ['south-africa-7', 'south-africa-8', 'south-africa-9', 'south-africa-10', 'south-africa-11', 'south-africa-12', 'south-africa-13']
FINAL = 'south-africa-7'  # Camps Bay from Table Mountain (also first in the gallery)

FAQ = [
    ("Do Indians need a visa for South Africa?", "Yes. On the Department of Home Affairs list of visa-exempt countries, India is exempt only for diplomatic, official and service passports — ordinary Indian passports need a visa for a holiday (checked 28 November 2026). Home Affairs also states that visas are not issued at South African ports of entry, so you must have your approval before you fly. The decision is always made by the South African authorities."),
    ("What is the South African ETA?", "The Electronic Travel Authorisation (ETA) is the online system of the Department of Home Affairs at eta.dha.gov.za, officially launched on 12 August 2026. It started with travellers from China, India, Indonesia and Mexico. For Indian passport holders it issues a port of entry visa before you travel. The official FAQ says most applications get an outcome within 24 hours, the ETA is typically valid for up to six months with multiple entries, and each stay is limited to up to 90 days (checked 28 November 2026)."),
    ("Which airports accept the South African ETA?", "The official ETA FAQ lists OR Tambo International (Johannesburg), Cape Town International, King Shaka International (Durban) and Lanseria International, with more ports of entry to follow. We plan your flights so you land at one of the listed airports, and we re-check the list when you book."),
    ("Can children travel on the South African ETA?", "The official ETA FAQ says minors also need an ETA, but applications for minors will be introduced in a future phase. For families with children we check the current route for each child when you book — the ETA FAQ names a South African mission or the eVisa system as the other channels, and the South African High Commission in New Delhi takes visa applications through the VFS Global application centres."),
    ("What documents are needed for South Africa?", "The ETA FAQ asks for a machine-readable passport valid for at least seven months from your travel date, and lists what you may be asked to show at the airport: your passport, the ETA approval, a return or onward ticket, proof of accommodation, proof of sufficient funds and a yellow fever certificate if you travel from a yellow fever risk country. We give you a day-by-day itinerary and hotel confirmations so your papers are clear and consistent."),
    ("When is the best time to visit South Africa?", "It depends on what you want to see. Cape Town and the Garden Route are at their warmest and driest from about November to March. The Kruger area is best for game drives in the dry winter, roughly May to September, when the bush is thinner. For one trip that combines Cape Town and a safari, the in-between months — about March to May and September to November — work well."),
    ("How many days are enough for South Africa?", "Seven to ten nights covers Cape Town, the Cape Peninsula and a Kruger safari. Add three or four nights to drive the Garden Route between Cape Town and Port Elizabeth (Gqeberha), or a few days in the Winelands."),
    ("Why are there no prices on this page?", "A South Africa trip cost depends on your dates, the season, the hotels and safari lodge, private or shared game drives, self-drive or chauffeur-driven travel, internal flights between Cape Town and the Kruger area, and the airfare from your city. Instead of a teaser price that changes when you ask, we send a costed, day-by-day quote for your dates — usually within 24 hours."),
]

JS = ("(function(){var f=document.getElementById('hxPlan');if(!f){return;}f.addEventListener('submit',function(e){e.preventDefault();"
      "var d=f.querySelector('[name=d]').value,s=f.querySelector('[name=s]').value,m=f.querySelector('[name=m]').value,a=f.querySelector('[name=a]').value,k=f.querySelector('[name=k]').value,c=f.querySelector('[name=c]').value;"
      "var t='Hi Suzu Travels, please send me a costed South Africa itinerary.\\nTrip: '+d+'\\nTrip type: '+s+'\\nTravel month: '+m+'\\nAdults: '+a+'\\nChildren: '+k;"
      "if(c){t=t+'\\nDeparting from: '+c;}"
      "window.open('https:'+String.fromCharCode(47,47)+'wa.me/917087488961?text='+encodeURIComponent(t),'_blank','noopener');});})();")

REL = [('tanzania-tour-packages', 'Tanzania', 'TZ', 'Serengeti, Ngorongoro, Zanzibar'), ('kenya-tour-packages', 'Kenya', 'KE', 'Masai Mara, Amboseli, lakes'), ('seychelles-tour-packages', 'Seychelles', 'SC', 'Mahé, Praslin, La Digue'), ('mauritius-tour-packages', 'Mauritius', 'suzu-abroad-mauritius', 'Lagoons, Le Morne, island tours'),
       ('egypt-tour-packages', 'Egypt', 'suzu-abroad-egypt', 'Cairo, Nile cruise, Luxor'), ('dubai-tour-packages', 'Dubai', 'suzu-abroad-dubai', 'Burj Khalifa, desert, Abu Dhabi'),
       ('oman-tour-packages', 'Oman', 'OM', 'Muscat, wadis, desert, Nizwa'), ('turkey-tour-packages', 'Turkey', 'suzu-abroad-turkey', 'Istanbul, Cappadocia, Pamukkale'),
       ('georgia-tour-packages', 'Georgia', 'suzu-abroad-georgia', 'Tbilisi, Kazbegi, Gudauri'), ('azerbaijan-tour-packages', 'Azerbaijan', 'suzu-abroad-azerbaijan', 'Baku, Gabala, Shahdag'),
       ('armenia-tour-packages', 'Armenia', 'suzu-abroad-armenia', 'Yerevan, Garni, Sevan'), ('uzbekistan-tour-packages', 'Uzbekistan', 'suzu-abroad-uzbekistan', 'Samarkand, Bukhara, Khiva'),
       ('kazakhstan-tour-packages', 'Kazakhstan', 'suzu-abroad-kazakhstan', 'Almaty, lakes, Kyrgyzstan'), ('maldives-tour-packages', 'Maldives', 'suzu-card-maldives', 'Overwater villas'),
       ('sri-lanka-tour-packages', 'Sri Lanka', 'suzu-card-sri-lanka', 'Beaches & tea country'), ('thailand-tour-packages', 'Thailand', 'suzu-card-thailand', 'Bangkok, Phuket, Krabi'),
       ('bali-tour-packages', 'Bali', 'suzu-card-bali', 'Ubud, villas, temples'), ('philippines-tour-packages', 'Philippines', 'PH', 'Palawan, Boracay, Bohol'),
       ('vietnam-tour-packages', 'Vietnam', 'suzu-card-vietnam', 'Hanoi, Ha Long, Hoi An'), ('cambodia-tour-packages', 'Cambodia', 'KH', 'Angkor Wat, Siem Reap, Phnom Penh'),
       ('malaysia-tour-packages', 'Malaysia', 'suzu-card-malaysia', 'KL, Langkawi, Genting'), ('singapore-tour-packages', 'Singapore', 'suzu-card-singapore', 'City, Sentosa, Universal'),
       ('europe-tour-packages', 'Europe', 'suzu-abroad-europe', 'Paris, Swiss Alps, Italy'), ('switzerland-tour-packages', 'Switzerland', 'suzu-abroad-switzerland', 'Lucerne, Jungfrau, Zermatt'),
       ('uk-tour-packages', 'UK', 'suzu-abroad-uk', 'London, Cotswolds, Scotland'), ('iceland-tour-packages', 'Iceland', 'IS', 'Golden Circle, glaciers, northern lights'),
       ('norway-tour-packages', 'Norway', 'NO', 'Fjords, Flåm Railway, Bergen'), ('russia-tour-packages', 'Russia', 'RU', 'Moscow, Saint Petersburg'),
       ('japan-tour-packages', 'Japan', 'suzu-abroad-japan', 'Tokyo, Fuji, Kyoto, Osaka'), ('south-korea-tour-packages', 'South Korea', 'KR', 'Seoul, Busan, Jeju'),
       ('china-tour-packages', 'China', 'CN', 'Great Wall, Xi’an, Shanghai'), ('hong-kong-tour-packages', 'Hong Kong & Macau', 'HK', 'Harbour, Peak, Disneyland, Macau'),
       ('new-zealand-tour-packages', 'New Zealand', 'NZ', 'Queenstown, Milford, Mount Cook'), ('australia-tour-packages', 'Australia & NZ', 'suzu-abroad-australia', 'Sydney, Melbourne, Queenstown'),
       ('nepal-tour-packages', 'Nepal', 'suzu-card-nepal', 'No visa for Indians'), ('bhutan-tour-packages', 'Bhutan', 'suzu-card-bhutan', 'Paro, Thimphu, Punakha')]
SPECIAL_IMG = {'IS': 'https://suzutravels.com/wp-content/uploads/2026/11/iceland-jokulsarlon-glacier-lagoon-768x509.webp',
               'NO': 'https://suzutravels.com/wp-content/uploads/2026/11/norway-geirangerfjord-from-ornesvingen-768x431.webp',
               'HK': 'https://suzutravels.com/wp-content/uploads/2026/11/hong-kong-victoria-harbour-night-from-the-peak-768x363.webp',
               'CN': 'https://suzutravels.com/wp-content/uploads/2026/11/china-great-wall-mutianyu-768x575.webp',
               'RU': 'https://suzutravels.com/wp-content/uploads/2026/11/russia-moscow-saint-basils-cathedral-red-square-768x512.webp',
               'NZ': 'https://suzutravels.com/wp-content/uploads/2026/11/new-zealand-milford-sound-mitre-peak-768x481.webp',
               'PH': 'https://suzutravels.com/wp-content/uploads/2026/11/philippines-el-nido-big-lagoon-palawan-768x512.webp',
               'KR': 'https://suzutravels.com/wp-content/uploads/2026/11/south-korea-seoul-gyeongbokgung-geunjeongjeon-768x432.webp',
               'KH': 'https://suzutravels.com/wp-content/uploads/2026/11/cambodia-angkor-wat-reflection-pond-768x499.webp',
               'SC': M['seychelles-1']['med'], 'OM': M['oman']['med'], 'TZ': M['tanzania']['med'],
               'KE': 'https://suzutravels.com/wp-content/uploads/2026/11/kenya-masai-mara-giraffes-768x511.webp'}


def build():
    W = "Hi Suzu Travels, I'm planning a South Africa holiday. Please share a quote."
    h = [f'<div class="suzu-intl hx hx-country"><style>{CSS}</style>']
    slides = ''.join(f'<div class="hx-slide"><img src="{U(s)}" alt="{A(s)}" width="1600" height="1000" {"fetchpriority=\"high\" loading=\"eager\"" if i == 0 else "loading=\"lazy\""} decoding="async"><span class="hx-cap">{C(s)}</span></div>' for i, s in enumerate(HERO))
    h.append('<section class="hx-hero" aria-label="South Africa tour packages from India"><div class="hx-slides">' + slides + '</div><div class="hx-copy">'
             '<p class="hx-lede">Ride the cable car up Table Mountain, drive the cliffs of Chapman’s Peak to the Cape of Good Hope, watch African penguins on Boulders Beach, walk the colourful lanes of Bo-Kaap and then go looking for lions and elephants on game drives around Kruger National Park. We plan your South Africa trip to your dates, budget and pace, with hotels and a safari lodge, private transfers or a self-drive car, vegetarian meals noted in advance and honest guidance on the new ETA visa.</p>'
             '<div class="hx-badges">'
             f'<span class="hx-badge">{svg("globe")}Cape Town, Kruger &amp; Garden Route</span><span class="hx-badge">{svg("doc")}ETA visa steps explained</span>'
             f'<span class="hx-badge">{svg("team")}Families, couples &amp; groups</span><span class="hx-badge">{svg("food")}Vegetarian meals planned</span></div>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Get a South Africa Quote {svg("arrow")}</a>'
             f'<a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div></div>'
             '<form class="hx-plan" id="hxPlan" aria-label="Get a costed South Africa itinerary on WhatsApp"><h3>Plan my South Africa trip</h3>'
             '<p>Tell us the basics — we reply on WhatsApp with a costed, day-by-day plan, usually within 24 hours.</p><div class="hx-f">'
             '<label class="hx-full">Trip<select name="d"><option selected>Cape Town + Kruger safari</option><option>Cape Town only</option><option>Cape Town + Garden Route</option><option>Cape Town, Garden Route + safari</option><option>South Africa + Mauritius or Seychelles</option><option>Not sure yet</option></select></label>'
             '<label>Trip type<select name="s"><option>Family</option><option>Honeymoon / couple</option><option>Friends</option><option>Seniors</option><option>Group</option><option>Corporate / MICE</option></select></label>'
             f'<label>Travel month<select name="m">{G.months()}</select></label>'
             '<label>Adults<select name="a"><option>1</option><option selected>2</option><option>3</option><option>4</option><option>5</option><option>6</option><option>7–10</option><option>11–20</option><option>20+</option></select></label>'
             '<label>Children<select name="k"><option>0</option><option>1</option><option>2</option><option>3</option><option>4+</option></select></label>'
             '<label class="hx-full">Departing from<input name="c" type="text" placeholder="e.g. Delhi, Mumbai, Chandigarh" autocomplete="address-level2"></label></div>'
             f'<button class="hx-btn" type="submit">{WA_SVG}Get my South Africa plan on WhatsApp</button><small>Opens WhatsApp with your details filled in. We do not store anything on this page.</small></form></section>')
    h.append('<div class="hx-trust">'
             f'<div>{svg("clock")}<span><b>Quote in ~24 hours</b><span>Costed, day by day</span></span></div>'
             f'<div>{svg("doc")}<span><b>Honest visa guidance</b><span>Official Home Affairs pages, checked</span></span></div>'
             f'<div>{svg("shield")}<span><b>HP Tourism registered</b><span>Reg. DTO-MND-11-243/2022</span></span></div>'
             f'<div>{svg("chat")}<span><b>One team, start to finish</b><span>Reachable while you travel</span></span></div></div>')
    h.append('<nav class="hx-toc" aria-label="On this page"><a href="#why-south-africa">Why South Africa</a><a href="#south-africa-in-photos">Photos</a><a href="#how-to-choose">Choose your trip</a><a href="#sample-itinerary">Sample itinerary</a><a href="#when-to-go">When to go</a><a href="#visa-and-entry">Visa</a><a href="#whats-included">What\'s included</a><a href="#south-africa-faq">FAQ</a></nav>')
    facts = [('Getting there', 'Fly into Johannesburg (OR Tambo) or Cape Town — we compare routes and connections from your city'), ('Time difference', 'India is 3 hours 30 minutes ahead of South Africa'), ('Currency', 'South African rand (ZAR)'),
             ('Best season', 'Mar–May and Sep–Nov for Cape Town plus a safari; Nov–Mar is Cape Town’s summer, May–Sep the dry season around Kruger'), ('Typical trip', '7 to 10 nights; add 3 to 4 nights for the Garden Route'), ('Entry', 'Visa for Indian passports — online ETA or a visa via VFS Global; no visa on arrival')]
    h.append('<section id="why-south-africa" class="hx-sec"><span class="hx-eye">South Africa</span><h2>Why South Africa is worth it for Indian travellers</h2>'
             '<p class="hx-sub">South Africa packs two very different holidays into one trip. Cape Town sits between Table Mountain and the ocean, with mountain drives, beaches, the penguins of Boulders Beach and the Winelands an hour away. In the north-east, Kruger National Park and the private reserves beside it are home to lions, elephants, leopards, rhinos and buffalo, and the Panorama Route looks down into the Blyde River Canyon. The Garden Route along the south coast adds lagoons, forests and the cliffs of Tsitsikamma — and there is a large Indian community, so vegetarian food is easy to find.</p>'
             '<div class="hx-facts">' + ''.join(f'<div class="hx-fact"><b>{a}</b><span>{b}</span></div>' for a, b in facts) + '</div></section>')
    h.append('<section id="south-africa-in-photos" class="hx-sec"><span class="hx-eye">Real places</span><h2>South Africa in photos</h2>'
             '<p class="hx-sub">Camps Bay seen from Table Mountain, a lion resting in Kruger National Park, the Blyde River Canyon, a giraffe in a private reserve near Kruger, the rocky shore at the Cape of Good Hope, the top of Table Mountain and the coast of Tsitsikamma. Real photos by Wikimedia Commons photographers, credited below.</p><div class="hx-pg">'
             + ''.join(f'<figure><img src="{U(k) if j == 0 else M[k]["med"]}" alt="{A(k)}" width="800" height="600" loading="lazy" decoding="async"><figcaption>{C(k)}</figcaption></figure>' for j, k in enumerate(GAL)) + '</div></section>')
    cards = [('First-timers', 'Cape Town + Kruger', 'Four nights in Cape Town for Table Mountain and the Cape Peninsula, then a short flight to the Kruger area for game drives and the Panorama Route.'),
             ('Families', 'Easy-paced &amp; fun', 'Penguins at Boulders Beach, the V&amp;A Waterfront, a malaria-free private reserve option near Cape Town or the Eastern Cape, and hotels with family rooms.'),
             ('Couples', 'Winelands &amp; a lodge', 'Cape Town sunsets, a night or two in the Winelands around Stellenbosch or Franschhoek, and a private safari lodge with game drives in an open vehicle.'),
             ('Road trip', 'The Garden Route', 'Drive east from Cape Town past Mossel Bay to Knysna, Plettenberg Bay and Tsitsikamma — self-drive or with a chauffeur, three to five nights.')]
    stays = [('Cape Town', 'Hotels at the V&amp;A Waterfront, in the city centre, or by the sea at Camps Bay and Sea Point — four nights is a good base.'),
             ('Winelands', 'Guest houses and estate hotels around Stellenbosch and Franschhoek, about an hour from Cape Town.'),
             ('Kruger area', 'Lodges inside Kruger National Park, or in the private reserves on its western edge where game drives are in open vehicles.'),
             ('Garden Route', 'Lagoon-side hotels in Knysna, beach stays in Plettenberg Bay, and lodges near the Tsitsikamma forest.')]
    h.append('<section id="how-to-choose" class="hx-sec"><span class="hx-eye">How to choose</span><h2>Choose the South Africa trip that fits you</h2>'
             '<p class="hx-sub">Start from the kind of trip you want — we fine-tune the route, hotels, safari lodge and pace to your group and season.</p><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><span class="hx-tag">{t}</span><h3>{n}</h3><p>{d}</p></div>' for t, n, d in cards) + '</div>'
             '<h3 style="margin-top:30px">Where to stay</h3><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><h3>{n}</h3><p>{d}</p></div>' for n, d in stays) + '</div></section>')
    days = [('Day 1', 'Arrive in Cape Town', 'Airport pick-up and transfer to your hotel. An easy evening at the V&amp;A Waterfront with Table Mountain behind the harbour.'),
            ('Day 2', 'Table Mountain &amp; city', 'Cable car up Table Mountain (weather permitting), the colourful houses of Bo-Kaap and the Company’s Garden; sunset at Signal Hill.'),
            ('Day 3', 'Cape Peninsula', 'Chapman’s Peak Drive, the Cape of Good Hope and Cape Point, and the African penguin colony at Boulders Beach in Simon’s Town.'),
            ('Day 4', 'Winelands or free day', 'A day in Stellenbosch and Franschhoek, or a trip along the coast to Hermanus in the whale season — or a free day in Cape Town.'),
            ('Day 5', 'Fly to the Kruger area', 'Short flight from Cape Town towards Kruger and transfer to your safari lodge, with an afternoon game drive.'),
            ('Day 6', 'Game drives', 'Morning and afternoon game drives looking for lions, elephants, leopards, rhinos and buffalo with your ranger.'),
            ('Day 7', 'Panorama Route', 'The Blyde River Canyon, Bourke’s Luck Potholes and the Three Rondavels viewpoints along the Panorama Route.'),
            ('Day 8', 'Fly home', 'Transfer to the airport for your flight home via Johannesburg — or add the Garden Route or a beach stay before you leave.')]
    h.append('<section id="sample-itinerary" class="hx-sec"><span class="hx-eye">Sample plan</span><h2>A sample 8-day Cape Town &amp; Kruger itinerary</h2>'
             '<p class="hx-sub">The classic first trip to South Africa — the Cape, then a safari. We rebuild it around you: add the Garden Route, stay in a private reserve, swap the flight for a self-drive, or add a few beach days in Mauritius or the Seychelles.</p><div class="hx-itin">'
             + ''.join(f'<div class="hx-day"><i>{a}</i><b>{b}</b><p>{c}</p></div>' for a, b, c in days) + '</div></section>')
    seasons = [('Dec – Feb', '<span class="hx-ok">Cape best</span>', 'Summer — warm and dry in Cape Town', 'Long beach days and clear views from Table Mountain; the Kruger area is hot and green, with afternoon storms. Busy around Christmas — book early.'),
               ('Mar – May', '<span class="hx-ok">Good for both</span>', 'Autumn — mild, settled weather', 'Pleasant in Cape Town and on the Garden Route, and the bush around Kruger starts to dry out. A good time to combine the Cape with a safari.'),
               ('Jun – Aug', '<span class="hx-mid">Safari best</span>', 'Winter — cool, rain in the Cape', 'The dry season brings the best game viewing around Kruger, with cold early mornings. Cape Town gets its rain; the whale season on the south coast usually starts around July.'),
               ('Sep – Nov', '<span class="hx-ok">Good for both</span>', 'Spring — warming up', 'Kruger is still dry in September and October, and Cape Town warms up with longer days. Often good for whale watching around Hermanus.')]
    h.append('<section id="when-to-go" class="hx-sec"><span class="hx-eye">Best season</span><h2>When to go to South Africa</h2>'
             '<p class="hx-sub">South Africa is in the southern hemisphere, so its summer is our winter. Cape Town has dry summers and wet winters, while the Kruger area gets its rain in summer and is dry in winter. This is general guidance; we check the season, lodge availability and flight prices against your plan before we quote.</p>'
             '<div class="hx-tw"><table class="hx-t"><thead><tr><th>Months</th><th>Verdict</th><th>Weather</th><th>What it means for your trip</th></tr></thead><tbody>'
             + ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in seasons) + '</tbody></table></div></section>')
    h.append('<section id="visa-and-entry" class="hx-sec"><span class="hx-eye">Visa &amp; entry</span><h2>South Africa visa for Indian passport holders</h2>'
             '<div class="hx-visa"><div class="hx-vbox"><h3>What the official sources say</h3><ul>'
             f'<li><b>A visa is needed.</b> On the Department of Home Affairs <a href="{SRC_EXEMPT}" target="_blank" rel="noopener nofollow">list of visa-exempt countries</a>, India is exempt only for diplomatic, official and service passports — ordinary Indian passports need a visa. Home Affairs also says <a href="{SRC_TYPES}" target="_blank" rel="noopener nofollow">visas are not issued at South African ports of entry</a>, so there is no visa on arrival.</li>'
             f'<li><b>The new ETA:</b> South Africa’s <a href="{SRC_ETA}" target="_blank" rel="noopener nofollow">Electronic Travel Authorisation</a> (eta.dha.gov.za) was <a href="{SRC_NEWS}" target="_blank" rel="noopener nofollow">officially launched on 12 August 2026</a>, starting with China, India, Indonesia and Mexico. You apply online from home; for visa-required travellers it issues a port of entry visa. Most applications get an outcome within 24 hours.</li>'
             '<li><b>Validity and stay:</b> the ETA is typically valid for up to six months with multiple entries, and each stay is limited to up to 90 days. The immigration officer decides your length of stay on arrival.</li>'
             '<li><b>Airports:</b> the ETA is currently used at OR Tambo (Johannesburg), Cape Town, King Shaka (Durban) and Lanseria airports. Fees are non-refundable, whatever the outcome.</li>'
             '<li><b>Passport and documents:</b> a machine-readable passport valid for at least seven months from your travel date. At the airport you may be asked for the ETA approval, a return ticket, proof of accommodation, proof of funds and a yellow fever certificate if you come from a yellow fever risk country.</li>'
             f'<li><b>Children and the VFS route:</b> minors also need an ETA, but ETA applications for minors will open in a future phase. If the ETA is not approved, you can apply through a South African mission or the eVisa system; the <a href="{SRC_HC}" target="_blank" rel="noopener nofollow">South African High Commission in New Delhi</a> takes visa applications through the VFS Global centres.</li></ul>'
             f'<p class="hx-checked">Checked {CHECKED} · sources: <a href="{SRC_EXEMPT}" target="_blank" rel="noopener nofollow">Exempt countries — Home Affairs</a> · <a href="{SRC_TYPES}" target="_blank" rel="noopener nofollow">Types of visas — Home Affairs</a> · <a href="{SRC_ETA}" target="_blank" rel="noopener nofollow">ETA FAQ — Home Affairs</a> · <a href="{SRC_NEWS}" target="_blank" rel="noopener nofollow">ETA launch — SAnews</a> · <a href="{SRC_HC}" target="_blank" rel="noopener nofollow">Visas — South African High Commission, New Delhi</a></p></div>'
             '<div class="hx-vnote"><p><b>Please note:</b> visa approval, and entry at the border, are always the decision of the South African authorities — the official ETA FAQ says an approved ETA does not guarantee entry, and final admission is decided by the immigration officer. We help you prepare clear, consistent documents — itinerary, hotel and lodge bookings and return tickets — but we never promise an outcome we do not control.</p>'
             '<p>The ETA is new and is still being rolled out, so rules, fees and airports can change. We re-check the official pages when you book. Please ask your doctor about vaccinations and malaria precautions for the Kruger area, and check the current health rules for your return to India, before you travel.</p></div></div></section>')
    inc = [('doc', 'Visa paperwork help', 'A day-by-day itinerary, hotel and lodge confirmations, and help with the ETA or the VFS visa application for each traveller.'), ('pin', 'Hotels &amp; safari lodge', 'Named hotels in Cape Town, the Winelands and on the Garden Route, and a safari lodge in or beside Kruger, chosen for your budget.'),
           ('team', 'Transfers &amp; guides', 'Airport transfers, a private driver-guide or a self-drive car with a planned route, and a ranger for your game drives.'), ('globe', 'Sightseeing &amp; drives', 'Table Mountain cable car, Cape Peninsula day, game drives and park fees — itemised in your quote; extras like whale cruises as options.'),
           ('food', 'Meal plan', 'Breakfast at hotels and usually all meals at the safari lodge; vegetarian and Jain needs noted in advance at every stay.'), ('award', 'Flights optional', 'Land-only, or a full package with international flights from your nearest Indian airport and the flight between Cape Town and Kruger.')]
    h.append('<section id="whats-included" class="hx-sec"><span class="hx-eye">Your package</span><h2>What a Suzu South Africa package includes</h2><div class="hx-inc">'
             + ''.join(f'<div>{svg(i)}<span><b>{t}</b><span>{d}</span></span></div>' for i, t, d in inc) + '</div></section>')
    steps = [('chat', 'Tell us the basics', 'Dates, travellers and the kind of trip you want. A WhatsApp message is enough.'),
             ('doc', 'Get a costed itinerary', 'A day-by-day plan with named hotels and a clear per-person price, usually within 24 hours.'),
             ('sliders', 'Adjust until it fits', 'Change the hotels, the safari lodge or the route, add the Garden Route or a beach stay. We re-quote as needed.'),
             ('lock', 'Confirm with a token', 'Lock your plan with a small token amount; the balance is paid later, as agreed in writing.')]
    h.append('<section id="how-booking-works" class="hx-sec"><span class="hx-eye">Simple process</span><h2>How booking works</h2><div class="hx-steps">'
             + ''.join(f'<div class="hx-step"><div class="hx-n">{svg(i)}</div><b>{t}</b><p>{d}</p></div>' for i, t, d in steps) + '</div></section>')
    h.append('<section id="south-africa-faq" class="hx-sec"><span class="hx-eye">FAQ</span><h2>Common questions about a South Africa holiday</h2><div class="hx-faqs">'
             + ''.join(f'<details class="hx-faq"{" open" if k == 0 else ""}><summary>{html.escape(q)}</summary><div class="hx-ans"><p>{html.escape(a)}</p></div></details>' for k, (q, a) in enumerate(FAQ)) + '</div></section>')
    def _img(img): return SPECIAL_IMG[img] if img in SPECIAL_IMG else f'https://suzutravels.com/wp-content/uploads/2026/10/{img}.webp'
    h.append('<section id="more-destinations" class="hx-sec"><span class="hx-eye">Explore more</span><h2>Explore more destinations</h2>'
             '<p class="hx-sub">Every trip is planned the same way — your dates, your budget, one team from quote to return. <a href="https://suzutravels.com/international-tour-packages/">See all international holidays →</a></p><div class="hx-mini">'
             + ''.join(f'<a class="hx-mc" href="https://suzutravels.com/{p}/"><img src="{_img(img)}" alt="{html.escape(n)} holiday — Suzu Travels" width="640" height="360" loading="lazy" decoding="async"><span><b>{html.escape(n)}</b><em>{html.escape(e)}</em></span></a>' for p, n, img, e in REL) + '</div></section>')
    h.append(f'<div class="hx-final"><img src="{U(FINAL)}" alt="{A(FINAL)}" width="1600" height="900" loading="lazy" decoding="async">'
             '<h2>Plan your South Africa holiday</h2><p>Send us your dates and group size. We will come back with a costed, day-by-day South Africa itinerary you can compare, no obligation.</p>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Request a South Africa Quote {svg("arrow")}</a><a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div>'
             '<p class="hx-contact">Or call <strong>+91 70874 88961</strong> · <a href="mailto:info@suzutravels.com">info@suzutravels.com</a></p></div>')
    seen = []
    for k in HERO + GAL + [FINAL]:
        v = M[k]
        if (v['credit'], v['license'], v['src']) not in seen:
            seen.append((v['credit'], v['license'], v['src']))
    h.append('<details class="hx-credits"><summary>Photo credits</summary><p>' + ' · '.join(f'<a href="{html.escape(s, quote=True)}" rel="nofollow noopener" target="_blank">{html.escape(c)}</a> ({html.escape(l)})' for c, l, s in seen) + '</p></details>')
    ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}
    h.append('<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + '</script><script>' + JS + '</script></div>')
    out = ''.join(h)
    assert '\n' not in out.replace('\\n', '')
    js = out[out.rfind('<script>'):]
    assert '&' not in js and '//' not in js
    return out

if __name__ == '__main__':
    o = build()
    open('pages/south-africa-tour-packages.html', 'w').write(o)
    print('pages/south-africa-tour-packages.html', len(o), len(o.encode()))
