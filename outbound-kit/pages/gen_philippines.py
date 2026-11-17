#!/usr/bin/env python3
"""Philippines page — .hx design; same template as gen_russia.py / gen_china.py.
Run from outbound-kit/:  python3 pages/gen_philippines.py <PAGE_ID> -> pages/philippines-tour-packages.html (one line)
Facts (official pages read 17 Nov 2026):
- DFA Philippines advisory "Visa-free privileges for Indian nationals entering the Philippines" (Manila, 07 June 2025; also on the
  Philippine Embassy New Delhi site): from 08 June 2025 Indian nationals may enter without a visa for a non-extendible,
  non-convertible 14 days for tourism - passport valid 6+ months beyond the stay, confirmed hotel booking, proof of financial
  capacity, return/onward ticket; holders of valid US, Japan, Australia, Canada, Schengen, Singapore or UK visas/residence
  permits: 30 days, non-extendible (passport 6+ months + return/onward ticket); any Philippine port of entry; no derogatory
  record with the Bureau of Immigration; transit / long stays / non-tourism need a visa; eligible Indians may also use the
  official e-Visa site evisa.gov.ph (e-Visas not extendable/convertible).
- Embassy New Delhi visa page: no legal right to a visa; a visa does not guarantee entry - immigration decides at the port of entry.
- etravel.gov.ph: eTravel is free; register only within 72 hours before arrival/departure; present the eTravel QR code at boarding.
Keyword Planner IN 17 Nov 2026: "philippines tour package" 3,600/mo (focus kw); next candidates "south korea tour package" 2,900,
"cambodia tour package" 1,900 ("cambodia visa for indians" 5,400).
Photos: Wikimedia Commons (CC BY / CC BY-SA; licence + author read from each File: page raw wikitext 17 Nov 2026), WP IDs 23154-23166,
all used; every uploaded WP copy viewed.
Climate/season wording is general guidance (no figures); no prices; no flight times.
"""
import json, html, sys, os
sys.path.insert(0, os.getcwd())
import gen_hub as G

PID = int(sys.argv[1]) if len(sys.argv) > 1 else 0
M = G.M
svg, WA_SVG, wa = G.svg, G.WA_SVG, G.wa
CHECKED = '17 November 2026'
SRC_DFA = 'https://dfa.gov.ph/dfa-news/statements-and-advisoriesupdate/36660-visa-free-privileges-for-indian-nationals-entering-the-philippines'
SRC_ND = 'https://newdelhipe.dfa.gov.ph/index.php/newsroom/embassy-news/1144-visa-free-privileges-for-indian-nationals-entering-the-philippines'
SRC_ET = 'https://etravel.gov.ph/'
SRC_EV = 'https://evisa.gov.ph/'

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
body.page-id-PID .page-header:before{content:"Holidays abroad \00B7  Philippines";display:inline-block;font:800 12px/1 "Plus Jakarta Sans",sans-serif;letter-spacing:.18em;text-transform:uppercase;color:#1a1606;background:#E2C158;padding:8px 13px;border-radius:999px;margin-bottom:16px}
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
HERO = ['philippines-1', 'philippines-2', 'philippines-3', 'philippines-4', 'philippines-5', 'philippines-6']
GAL = ['philippines-7', 'philippines-8', 'philippines-9', 'philippines-10', 'philippines-11', 'philippines-12', 'philippines-13']
FINAL = 'philippines-3'  # reuses hero slide 3 (Kayangan Lake, Coron)

FAQ = [
    ("Do Indians need a visa for the Philippines?", "Not for a short holiday, if you meet the conditions. When we checked the official advisory of the Philippine Department of Foreign Affairs on 17 November 2026, Indian nationals could enter the Philippines without a visa for up to 14 days for tourism, with a passport valid for at least six months beyond the stay, a confirmed hotel booking, proof of financial capacity and a return or onward ticket. The 14 days cannot be extended or converted. Whether you are admitted is always the decision of the Philippine immigration authorities at the port of entry."),
    ("Can Indians stay 30 days in the Philippines without a visa?", "Yes, according to the same DFA advisory, if you hold a valid and current visa or residence permit of the United States, Japan, Australia, Canada, the Schengen area, Singapore or the United Kingdom. You can then enter without a Philippine visa for up to 30 days for tourism (not extendable), with a passport valid for at least six months beyond the stay and a return or onward ticket. For longer stays or other purposes you need a Philippine visa; eligible travellers can apply on the official e-Visa site, evisa.gov.ph."),
    ("What is eTravel and do I need it?", "eTravel is the Philippine government's free online travel declaration. The official eTravel site says you can register only within 72 hours before your arrival, and you are asked to show your eTravel QR code when boarding your flight. Use only the official site etravel.gov.ph — it is free, so ignore websites that charge for it. We remind you when your 72-hour window opens."),
    ("How many days are enough for a Philippines trip?", "Seven or eight days is a comfortable first trip: a day or two in Manila, two or three days in Bohol for the Chocolate Hills, the tarsiers and the Loboc River, and three days on a beach island such as Boracay. With 10 to 12 days you can add Palawan — El Nido or Coron. Remember that the visa-free stay for most Indian travellers is 14 days."),
    ("Which is better for a first trip — Boracay, Palawan or Bohol?", "Boracay is the easiest beach holiday, with its long White Beach, sunsets and plenty of hotels and restaurants. Palawan (El Nido and Coron) is for island-hopping between limestone cliffs and lagoons, and suits travellers happy with boat days. Bohol mixes countryside sights — the Chocolate Hills, tarsiers and river cruise — with Panglao's beaches. Many couples and families combine two of them; we suggest the mix that fits your dates and flights."),
    ("Which is the best time to visit the Philippines?", "The dry season, from about December to May, is the most popular time: December to February is the most pleasant, and March to May is hotter and good for beaches. From about June to November it is the rainy season, and typhoons can disrupt boats and domestic flights, especially in the second half of the year. Trips are still possible then — we build in buffer days and choose islands and dates carefully."),
    ("Is vegetarian and Indian food available in the Philippines?", "Yes, in Manila and in tourist areas such as Boracay, Cebu and El Nido you will find Indian restaurants and vegetarian options; on remote islands and boat tours it takes more planning. We note vegetarian and Jain needs with hotels and island-hopping operators in advance."),
    ("Why are there no prices on this page?", "A Philippines trip cost depends on your dates, the islands you choose, the domestic flights and boat transfers between them, hotel category, tours and the airfare from your city. Instead of a teaser price that changes when you ask, we send a costed, day-by-day quote for your dates — usually within 24 hours."),
]

JS = ("(function(){var f=document.getElementById('hxPlan');if(!f){return;}f.addEventListener('submit',function(e){e.preventDefault();"
      "var d=f.querySelector('[name=d]').value,s=f.querySelector('[name=s]').value,m=f.querySelector('[name=m]').value,a=f.querySelector('[name=a]').value,k=f.querySelector('[name=k]').value,c=f.querySelector('[name=c]').value;"
      "var t='Hi Suzu Travels, please send me a costed Philippines itinerary.\\nTrip: '+d+'\\nTrip type: '+s+'\\nTravel month: '+m+'\\nAdults: '+a+'\\nChildren: '+k;"
      "if(c){t=t+'\\nDeparting from: '+c;}"
      "window.open('https:'+String.fromCharCode(47,47)+'wa.me/917087488961?text='+encodeURIComponent(t),'_blank','noopener');});})();")

REL = [('thailand-tour-packages', 'Thailand', 'suzu-card-thailand', 'Bangkok, Phuket, Krabi'), ('bali-tour-packages', 'Bali', 'suzu-card-bali', 'Ubud, villas, temples'),
       ('vietnam-tour-packages', 'Vietnam', 'suzu-card-vietnam', 'Hanoi, Ha Long, Hoi An'), ('malaysia-tour-packages', 'Malaysia', 'suzu-card-malaysia', 'KL, Langkawi, Genting'),
       ('singapore-tour-packages', 'Singapore', 'suzu-card-singapore', 'City, Sentosa, Universal'), ('maldives-tour-packages', 'Maldives', 'suzu-card-maldives', 'Overwater villas'),
       ('mauritius-tour-packages', 'Mauritius', 'suzu-abroad-mauritius', 'Lagoons, Le Morne, island tours'), ('sri-lanka-tour-packages', 'Sri Lanka', 'suzu-card-sri-lanka', 'Beaches & tea country'),
       ('hong-kong-tour-packages', 'Hong Kong & Macau', 'HK', 'Harbour, Peak, Disneyland, Macau'), ('japan-tour-packages', 'Japan', 'suzu-abroad-japan', 'Tokyo, Fuji, Kyoto, Osaka'),
       ('china-tour-packages', 'China', 'CN', 'Great Wall, Xi’an, Shanghai'), ('australia-tour-packages', 'Australia & NZ', 'suzu-abroad-australia', 'Sydney, Melbourne, Queenstown'),
       ('new-zealand-tour-packages', 'New Zealand', 'NZ', 'Queenstown, Milford, Mount Cook'), ('dubai-tour-packages', 'Dubai', 'suzu-abroad-dubai', 'Burj Khalifa, desert, Abu Dhabi'),
       ('turkey-tour-packages', 'Turkey', 'suzu-abroad-turkey', 'Istanbul, Cappadocia, Pamukkale'), ('egypt-tour-packages', 'Egypt', 'suzu-abroad-egypt', 'Cairo, Nile cruise, Luxor'),
       ('europe-tour-packages', 'Europe', 'suzu-abroad-europe', 'Paris, Swiss Alps, Italy'), ('switzerland-tour-packages', 'Switzerland', 'suzu-abroad-switzerland', 'Lucerne, Jungfrau, Zermatt'),
       ('uk-tour-packages', 'UK', 'suzu-abroad-uk', 'London, Cotswolds, Scotland'), ('russia-tour-packages', 'Russia', 'RU', 'Moscow, Saint Petersburg'),
       ('georgia-tour-packages', 'Georgia', 'suzu-abroad-georgia', 'Tbilisi, Kazbegi, Gudauri'), ('azerbaijan-tour-packages', 'Azerbaijan', 'suzu-abroad-azerbaijan', 'Baku, Gabala, Shahdag'),
       ('armenia-tour-packages', 'Armenia', 'suzu-abroad-armenia', 'Yerevan, Garni, Sevan'), ('uzbekistan-tour-packages', 'Uzbekistan', 'suzu-abroad-uzbekistan', 'Samarkand, Bukhara, Khiva'),
       ('kazakhstan-tour-packages', 'Kazakhstan', 'suzu-abroad-kazakhstan', 'Almaty, lakes, Kyrgyzstan'), ('nepal-tour-packages', 'Nepal', 'suzu-card-nepal', 'No visa for Indians'),
       ('bhutan-tour-packages', 'Bhutan', 'suzu-card-bhutan', 'Paro, Thimphu, Punakha')]
SPECIAL_IMG = {'HK': 'https://suzutravels.com/wp-content/uploads/2026/11/hong-kong-victoria-harbour-night-from-the-peak-768x363.webp',
               'CN': 'https://suzutravels.com/wp-content/uploads/2026/11/china-great-wall-mutianyu-768x575.webp',
               'RU': 'https://suzutravels.com/wp-content/uploads/2026/11/russia-moscow-saint-basils-cathedral-red-square-768x512.webp',
               'NZ': 'https://suzutravels.com/wp-content/uploads/2026/11/new-zealand-milford-sound-mitre-peak-768x481.webp'}

def build():
    W = "Hi Suzu Travels, I'm planning a Philippines trip. Please share a quote."
    h = [f'<div class="suzu-intl hx hx-country"><style>{CSS}</style>']
    slides = ''.join(f'<div class="hx-slide"><img src="{U(s)}" alt="{A(s)}" width="1600" height="1000" {"fetchpriority=\"high\" loading=\"eager\"" if i == 0 else "loading=\"lazy\""} decoding="async"><span class="hx-cap">{C(s)}</span></div>' for i, s in enumerate(HERO))
    h.append('<section class="hx-hero" aria-label="Philippines tour packages from India"><div class="hx-slides">' + slides + '</div><div class="hx-copy">'
             '<p class="hx-lede">Swim in the turquoise lagoons of El Nido, watch the sun set over Boracay&rsquo;s White Beach, see the Chocolate Hills and the tiny tarsiers of Bohol, and walk the old Spanish walls of Intramuros in Manila. We plan the Philippines to your dates, budget and pace — island by island, with domestic flights and boat transfers that actually connect, vegetarian meals noted in advance and honest guidance on the visa-free entry rules for Indians.</p>'
             '<div class="hx-badges">'
             f'<span class="hx-badge">{svg("globe")}Palawan, Boracay &amp; Bohol</span><span class="hx-badge">{svg("doc")}Visa-free entry rules explained</span>'
             f'<span class="hx-badge">{svg("team")}Honeymoons, families &amp; groups</span><span class="hx-badge">{svg("food")}Vegetarian meals planned</span></div>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Get a Philippines Quote {svg("arrow")}</a>'
             f'<a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div></div>'
             '<form class="hx-plan" id="hxPlan" aria-label="Get a costed Philippines itinerary on WhatsApp"><h3>Plan my Philippines trip</h3>'
             '<p>Tell us the basics — we reply on WhatsApp with a costed, day-by-day plan, usually within 24 hours.</p><div class="hx-f">'
             '<label class="hx-full">Trip<select name="d"><option selected>Manila + Bohol + Boracay (classic)</option><option>Palawan — El Nido and/or Coron</option><option>Boracay beach holiday</option><option>Cebu + Bohol</option><option>Classic + Palawan (10–12 days)</option><option>Not sure yet</option></select></label>'
             '<label>Trip type<select name="s"><option>Honeymoon / couple</option><option>Family</option><option>Friends</option><option>Seniors</option><option>Group</option><option>Corporate / MICE</option></select></label>'
             f'<label>Travel month<select name="m">{G.months()}</select></label>'
             '<label>Adults<select name="a"><option>1</option><option selected>2</option><option>3</option><option>4</option><option>5</option><option>6</option><option>7–10</option><option>11–20</option><option>20+</option></select></label>'
             '<label>Children<select name="k"><option>0</option><option>1</option><option>2</option><option>3</option><option>4+</option></select></label>'
             '<label class="hx-full">Departing from<input name="c" type="text" placeholder="e.g. Delhi, Mumbai, Chandigarh" autocomplete="address-level2"></label></div>'
             f'<button class="hx-btn" type="submit">{WA_SVG}Get my Philippines plan on WhatsApp</button><small>Opens WhatsApp with your details filled in. We do not store anything on this page.</small></form></section>')
    h.append('<div class="hx-trust">'
             f'<div>{svg("clock")}<span><b>Quote in ~24 hours</b><span>Costed, day by day</span></span></div>'
             f'<div>{svg("doc")}<span><b>Honest entry guidance</b><span>Official DFA rules, checked</span></span></div>'
             f'<div>{svg("shield")}<span><b>HP Tourism registered</b><span>Reg. DTO-MND-11-243/2022</span></span></div>'
             f'<div>{svg("chat")}<span><b>One team, start to finish</b><span>Reachable while you travel</span></span></div></div>')
    h.append('<nav class="hx-toc" aria-label="On this page"><a href="#why-philippines">Why the Philippines</a><a href="#philippines-in-photos">Photos</a><a href="#how-to-choose">Choose your islands</a><a href="#sample-itinerary">Sample itinerary</a><a href="#when-to-go">When to go</a><a href="#visa-and-entry">Visa</a><a href="#whats-included">What\'s included</a><a href="#philippines-faq">FAQ</a></nav>')
    facts = [('Getting there', 'Fly into Manila; we compare direct and connecting flights from your city'), ('Time difference', 'The Philippines is 2 hours 30 minutes ahead of India'), ('Currency', 'Philippine peso (PHP); cards in cities and resorts, cash for islands and boats'),
             ('Best season', 'December to May (dry season)'), ('Typical trip', '6 to 8 nights; 10 to 12 with Palawan'), ('Entry', 'Visa-free for Indians up to 14 days for tourism — conditions apply')]
    h.append('<section id="why-philippines" class="hx-sec"><span class="hx-eye">Philippines</span><h2>Why the Philippines is worth it for Indian travellers</h2>'
             '<p class="hx-sub">More than 7,000 islands, and the best of them are made for an easy island-hopping holiday: the limestone lagoons of El Nido and Coron in Palawan, the long White Beach of Boracay, and Bohol with its Chocolate Hills, tarsiers and river cruises. English is widely spoken, Manila adds Spanish-era history in Intramuros, and since June 2025 eligible Indian tourists can enter without a visa for up to 14 days.</p>'
             '<div class="hx-facts">' + ''.join(f'<div class="hx-fact"><b>{a}</b><span>{b}</span></div>' for a, b in facts) + '</div></section>')
    h.append('<section id="philippines-in-photos" class="hx-sec"><span class="hx-eye">Real places</span><h2>The Philippines in photos</h2>'
             '<p class="hx-sub">An island lagoon in Bacuit Bay at El Nido, a Philippine tarsier in Bohol, San Agustin Church in Intramuros, the entrance of the Puerto Princesa Underground River, the Loboc River in Bohol, Kawasan Falls in Cebu and Taal Volcano seen from Tagaytay. Real photos by Wikimedia Commons photographers, credited below.</p><div class="hx-pg">'
             + ''.join(f'<figure><img src="{U(k)}" alt="{A(k)}" width="800" height="600" loading="lazy" decoding="async"><figcaption>{C(k)}</figcaption></figure>' for k in GAL) + '</div></section>')
    cards = [('First-timers', 'Manila, Bohol &amp; Boracay', 'The classic first trip: Intramuros in Manila, the Chocolate Hills and tarsiers of Bohol, then beach days on Boracay&rsquo;s White Beach.'),
             ('Honeymoon', 'Palawan islands', 'Island-hopping between the lagoons and limestone cliffs of El Nido and Coron, with quiet beach resorts and sunset boat trips.'),
             ('Families', 'Easy beaches', 'Boracay or Panglao (Bohol) for calm, shallow beaches, short transfers and family rooms, plus a gentle river cruise and the tarsiers.'),
             ('Active', 'Cebu &amp; waterfalls', 'Kawasan Falls and canyoneering in Cebu, snorkelling trips and the Underground River at Puerto Princesa for nature lovers.')]
    stays = [('Manila — Makati or Bonifacio Global City', 'Modern, walkable business districts with malls and restaurants; Intramuros and Manila Bay are a short drive away.'),
             ('Boracay — White Beach', 'Stay along White Beach for sunsets and restaurants within walking distance; quieter ends of the beach suit couples and families.'),
             ('Bohol — Panglao Island', 'Beach resorts on Panglao, with easy day trips to the Chocolate Hills, the tarsier sanctuary and the Loboc River.'),
             ('Palawan — El Nido town or a beach resort', 'El Nido town for the island-hopping boats; beach and island resorts for a quieter honeymoon. Coron town for Kayangan Lake trips.')]
    h.append('<section id="how-to-choose" class="hx-sec"><span class="hx-eye">How to choose</span><h2>Choose the Philippines trip that fits you</h2>'
             '<p class="hx-sub">Start from the kind of trip you want — we fine-tune the islands, hotels, domestic flights, boats and tours to your group.</p><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><span class="hx-tag">{t}</span><h3>{n}</h3><p>{d}</p></div>' for t, n, d in cards) + '</div>'
             '<h3 style="margin-top:30px">Where to stay</h3><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><h3>{n}</h3><p>{d}</p></div>' for n, d in stays) + '</div></section>')
    days = [('Day 1', 'Arrive in Manila', 'Airport transfer to your hotel. Easy evening at a mall or by Manila Bay for the sunset.'),
            ('Day 2', 'Intramuros &amp; old Manila', 'Fort Santiago and San Agustin Church in the walled city of Intramuros, then Rizal Park. Optional day trip to Tagaytay for the Taal Volcano view.'),
            ('Day 3', 'Fly to Bohol', 'Domestic flight to Bohol and transfer to a beach resort on Panglao. Afternoon on the beach.'),
            ('Day 4', 'Bohol countryside', 'The Chocolate Hills, the tarsiers at a sanctuary, and a lunch cruise on the Loboc River.'),
            ('Day 5', 'Panglao island day', 'An island-hopping and snorkelling trip, or a free day on the beach at Panglao.'),
            ('Day 6', 'Fly to Boracay', 'Flight and short boat transfer to Boracay. Sunset on White Beach.'),
            ('Day 7', 'Boracay', 'Island-hopping and snorkelling, or a slow day on White Beach. Optional sunset sailing on a paraw.'),
            ('Day 8', 'Fly home', 'Transfer back to the mainland airport and fly home via Manila.')]
    h.append('<section id="sample-itinerary" class="hx-sec"><span class="hx-eye">Sample plan</span><h2>A sample 8-day Philippines itinerary</h2>'
             '<p class="hx-sub">The classic first trip. We rebuild it around you — swap Bohol or Boracay for Palawan (El Nido or Coron), add Cebu, or keep it to one island for a relaxed honeymoon.</p><div class="hx-itin">'
             + ''.join(f'<div class="hx-day"><i>{a}</i><b>{b}</b><p>{c}</p></div>' for a, b, c in days) + '</div></section>')
    seasons = [('Dec – Feb', '<span class="hx-ok">Best</span>', 'Dry, most pleasant', 'The most popular time for beaches and island-hopping; Christmas and New Year are busy — book early.'),
               ('Mar – May', '<span class="hx-ok">Best</span>', 'Dry, hot', 'Calm seas and long beach days; it gets hot, especially in April and May. Indian summer holidays fall here.'),
               ('Jun – Aug', '<span class="hx-mid">Rainy</span>', 'Showers, humid', 'Rainy season begins; fewer visitors and good value, but some boat trips can be cancelled on rough days.'),
               ('Sep – Nov', '<span class="hx-mid">Typhoons</span>', 'Wet, stormy spells', 'Typhoons can disrupt boats and domestic flights; we keep buffer days and choose islands carefully.')]
    h.append('<section id="when-to-go" class="hx-sec"><span class="hx-eye">Best season</span><h2>When to go to the Philippines</h2>'
             '<p class="hx-sub">The Philippines is a dry-season destination: December to May is the most reliable time for beaches and boats. We check the season, holidays and flight prices against your plan before we quote.</p>'
             '<div class="hx-tw"><table class="hx-t"><thead><tr><th>Months</th><th>Verdict</th><th>Weather</th><th>What it means for your trip</th></tr></thead><tbody>'
             + ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in seasons) + '</tbody></table></div></section>')
    h.append('<section id="visa-and-entry" class="hx-sec"><span class="hx-eye">Visa &amp; entry</span><h2>Philippines entry rules for Indian passport holders</h2>'
             '<div class="hx-visa"><div class="hx-vbox"><h3>What the official rules say</h3><ul>'
             '<li><b>Visa-free for up to 14 days for tourism.</b> Since 8 June 2025, Indian nationals may enter the Philippines without a visa for a <b>non-extendible, non-convertible 14 days</b>. You need a passport valid for at least <b>six months beyond your stay</b>, a <b>confirmed hotel booking</b>, <b>proof of financial capacity</b> and a <b>return or onward ticket</b>.</li>'
             '<li><b>Up to 30 days with certain visas.</b> If you hold a valid and current visa or residence permit of the <b>United States, Japan, Australia, Canada, the Schengen area, Singapore or the United Kingdom</b>, you may enter without a Philippine visa for up to <b>30 days</b> for tourism (not extendable), with a passport valid six months beyond the stay and a return or onward ticket.</li>'
             '<li><b>Any port of entry.</b> Visa-free entry can be used at any Philippine port of entry. Travellers must not have any derogatory record with the Bureau of Immigration.</li>'
             f'<li><b>Longer stays, transit or other purposes</b> need a Philippine visa. Eligible Indian nationals can apply on the official e-Visa site <a href="{SRC_EV}" target="_blank" rel="noopener nofollow">evisa.gov.ph</a>.</li>'
             f'<li><b>eTravel declaration:</b> register free on the official site <a href="{SRC_ET}" target="_blank" rel="noopener nofollow">etravel.gov.ph</a> within 72 hours before arrival, and show the eTravel QR code when boarding.</li></ul>'
             f'<p class="hx-checked">Checked {CHECKED} · sources: <a href="{SRC_DFA}" target="_blank" rel="noopener nofollow">DFA Philippines — visa-free privileges for Indian nationals</a> · <a href="{SRC_ND}" target="_blank" rel="noopener nofollow">Philippine Embassy, New Delhi</a> · <a href="{SRC_ET}" target="_blank" rel="noopener nofollow">eTravel (official)</a></p></div>'
             '<div class="hx-vnote"><p><b>Please note:</b> admission is always the decision of the Philippine immigration authorities at the port of entry, and any visa is the decision of the Philippine government. We help you carry the right documents, but we never promise an outcome we do not control.</p>'
             '<p>We give you the hotel confirmations, return ticket and day-by-day itinerary in one set, keep your trip within the visa-free days, and remind you to complete eTravel in time. If you want to stay longer than your visa-free period, we guide you to the right visa before you book.</p></div></div></section>')
    inc = [('doc', 'Entry paperwork', 'Hotel confirmations, return ticket and itinerary ready for the airline and immigration, plus an eTravel reminder.'), ('pin', 'Hotels', 'Named hotels and beach resorts on each island, chosen for your budget and trip style.'),
           ('team', 'Flights &amp; boats', 'Domestic flights between the islands, boat transfers and airport pick-ups that connect.'), ('globe', 'Tours', 'Island-hopping, the Bohol countryside tour, the Underground River and city tours, as you choose.'),
           ('food', 'Meal plan', 'Breakfast at most hotels; vegetarian and Jain needs noted in advance with hotels and boat operators.'), ('award', 'Flights optional', 'Land-only, or a full package with international flights from your nearest Indian airport.')]
    h.append('<section id="whats-included" class="hx-sec"><span class="hx-eye">Your package</span><h2>What a Suzu Philippines package includes</h2><div class="hx-inc">'
             + ''.join(f'<div>{svg(i)}<span><b>{t}</b><span>{d}</span></span></div>' for i, t, d in inc) + '</div></section>')
    steps = [('chat', 'Tell us the basics', 'Dates, travellers and the kind of trip you want. A WhatsApp message is enough.'),
             ('doc', 'Get a costed itinerary', 'A day-by-day plan with named hotels and a clear per-person price, usually within 24 hours.'),
             ('sliders', 'Adjust until it fits', 'Change the islands, hotels, flights or add-ons. We re-quote as needed.'),
             ('lock', 'Confirm with a token', 'Lock your plan with a small token amount; the balance is paid later, as agreed in writing.')]
    h.append('<section id="how-booking-works" class="hx-sec"><span class="hx-eye">Simple process</span><h2>How booking works</h2><div class="hx-steps">'
             + ''.join(f'<div class="hx-step"><div class="hx-n">{svg(i)}</div><b>{t}</b><p>{d}</p></div>' for i, t, d in steps) + '</div></section>')
    h.append('<section id="philippines-faq" class="hx-sec"><span class="hx-eye">FAQ</span><h2>Common questions about a Philippines tour</h2><div class="hx-faqs">'
             + ''.join(f'<details class="hx-faq"{" open" if k == 0 else ""}><summary>{html.escape(q)}</summary><div class="hx-ans"><p>{html.escape(a)}</p></div></details>' for k, (q, a) in enumerate(FAQ)) + '</div></section>')
    def _img(img): return SPECIAL_IMG[img] if img in SPECIAL_IMG else f'https://suzutravels.com/wp-content/uploads/2026/10/{img}.webp'
    h.append('<section id="more-destinations" class="hx-sec"><span class="hx-eye">Explore more</span><h2>Explore more destinations</h2>'
             '<p class="hx-sub">Every trip is planned the same way — your dates, your budget, one team from quote to return. <a href="https://suzutravels.com/international-tour-packages/">See all international holidays →</a></p><div class="hx-mini">'
             + ''.join(f'<a class="hx-mc" href="https://suzutravels.com/{p}/"><img src="{_img(img)}" alt="{html.escape(n)} holiday — Suzu Travels" width="640" height="360" loading="lazy" decoding="async"><span><b>{html.escape(n)}</b><em>{html.escape(e)}</em></span></a>' for p, n, img, e in REL) + '</div></section>')
    h.append(f'<div class="hx-final"><img src="{U(FINAL)}" alt="{A(FINAL)}" width="1600" height="900" loading="lazy" decoding="async">'
             '<h2>Plan your Philippines trip</h2><p>Send us your dates and group size. We will come back with a costed, day-by-day Philippines itinerary you can compare, no obligation.</p>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Request a Philippines Quote {svg("arrow")}</a><a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div>'
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
    open('pages/philippines-tour-packages.html', 'w').write(o)
    print('pages/philippines-tour-packages.html', len(o), len(o.encode()))
