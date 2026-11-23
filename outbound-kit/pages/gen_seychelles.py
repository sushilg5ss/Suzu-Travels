#!/usr/bin/env python3
"""Seychelles page - .hx design; same template as gen_norway.py.
Built + published 23 Nov 2026 (photos WP 24741-24754, 13 used + 24743 spare).
Run from outbound-kit/:  python3 pages/gen_seychelles.py <PAGE_ID> -> pages/seychelles-tour-packages.html (one line)
Facts (official pages read 23 Nov 2026 with curl):
- ics.gov.sc/visa-and-travel/visiting-seychelles: "a visa is not required to enter Seychelles by other passport holders";
  passport valid for the period of the intended stay until arrival back home; Visitor's Permit issued on arrival for
  holiday, business, visiting friends/family to travellers who: are not prohibited immigrants, do not hold a residence
  permit, hold a valid return/onward ticket, have confirmed accommodation, have sufficient funds (minimum US$150 or
  equivalent per day). Complete immigration forms on seychelles.govtas.com. Give correct accommodation address.
- ics.gov.sc/permits/visitors-permit: permit initially up to three months, free of charge; extensions up to 3 months each
  to max 12 months, SCR 5,000 per extension (not quoted on the page); all visitors must hold a valid Electronic Travel
  Authorisation before departing their country of origin (Seychelles e-Border app or seychelles.govtas.com).
Not stated (not read officially): the Travel Authorisation fee (govtas site is a JS app) -> page says "any fee is shown there".
Keyword Planner IN 23 Nov 2026: "seychelles tour package" 1,900/mo (focus kw), "seychelles package" 2,400,
"seychelles trip cost from india" 390, "seychelles tour package from india" 170.
Photos: Wikimedia Commons (CC BY-SA 4.0 NorbertNagel / Radoslaw Botev; Tobi 87 GFDL|cc-by-sa-all used as CC BY-SA 3.0).
Season wording is general guidance; no package prices; no flight times.
"""
import json, html, sys, os
sys.path.insert(0, os.getcwd())
import gen_hub as G

PID = int(sys.argv[1]) if len(sys.argv) > 1 else 0
M = dict(G.M)
PREVIEW = False
svg, WA_SVG, wa = G.svg, G.WA_SVG, G.wa
CHECKED = '23 November 2026'
SRC_EMB = 'https://www.ics.gov.sc/visa-and-travel/visiting-seychelles'
SRC_VISA = 'https://www.ics.gov.sc/permits/visitors-permit'
SRC_ENTRY = 'https://seychelles.govtas.com/en'

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
body.page-id-PID .page-header:before{content:"Holidays abroad \00B7  Seychelles";display:inline-block;font:800 12px/1 "Plus Jakarta Sans",sans-serif;letter-spacing:.18em;text-transform:uppercase;color:#1a1606;background:#E2C158;padding:8px 13px;border-radius:999px;margin-bottom:16px}
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
HERO = ['seychelles-1', 'seychelles-2', 'seychelles-3', 'seychelles-4', 'seychelles-5', 'seychelles-6']
GAL = ['seychelles-7', 'seychelles-8', 'seychelles-9', 'seychelles-10', 'seychelles-11', 'seychelles-12', 'seychelles-13']
FINAL = 'seychelles-12'  # sunset at Port Glaud (also in the gallery)

FAQ = [
    ("Do Indians need a visa for Seychelles?", "No visa is needed. Seychelles' Immigration and Civil Status department says a visa is not required to enter Seychelles, and that a Visitor's Permit is issued on arrival to travellers coming for a holiday, business or to visit friends or family who meet its criteria (checked 23 November 2026). Admission is always the decision of the Seychelles immigration officers at the border."),
    ("What is the Seychelles Travel Authorisation?", "The Immigration and Civil Status department says all visitors must hold a valid Electronic Travel Authorisation before departing from their country of origin. You apply on the official Seychelles Electronic Border System website (seychelles.govtas.com) or its Seychelles e-Border app. Any fee is shown on the official site when you apply; we help you fill it in correctly with your hotel addresses."),
    ("What documents do I need to enter Seychelles?", "The official criteria for a Visitor's Permit are: a passport valid for the period of your stay until you are back in India, a valid return or onward ticket, confirmed accommodation, and sufficient funds for the stay — the immigration page mentions a minimum of US$150 or equivalent per day. You must not be a prohibited immigrant. We give you a clear itinerary and hotel confirmations to carry."),
    ("How long can I stay in Seychelles as a tourist?", "The Visitor's Permit is first granted for up to three months and is free of charge for that period, according to the Immigration and Civil Status department. Extensions are possible for further periods of up to three months each, to a maximum of twelve months, for a fee — each is decided by Seychelles immigration."),
    ("Which is the best time to visit Seychelles?", "Seychelles is warm all year. The calmer months between the two trade-wind seasons, roughly April to May and October to November, are often the most comfortable for beaches, boat trips and snorkelling. December to March is usually more humid with more rain showers; June to September is drier but breezier, with rougher seas on some coasts. We pick beaches and boat days to suit your month."),
    ("How many days are enough for Seychelles?", "Six to seven nights works well for Mahé, Praslin and La Digue: two or three nights on Mahé, then Praslin and La Digue by ferry. For a honeymoon at a slower pace, eight to nine nights with one resort stay is a good plan. Shorter trips of four to five nights can cover Mahé with a day trip to Praslin and La Digue."),
    ("Is Seychelles good for a honeymoon or a family trip?", "Yes. Couples come for quiet beaches, granite-boulder coves, sunsets and boat days around the islands. Families do well with calm-water beaches, the giant tortoises of Curieuse and easy cycling on La Digue. We choose hotels for your group, plan vegetarian meals in advance, and note that Victoria on Mahé has a Hindu temple, the Arul Mihu Navashakti Vinayagar Temple."),
    ("Why are there no prices on this page?", "A Seychelles trip cost depends on your dates, the islands you choose, hotel or resort category, ferries or inter-island flights and the airfare from your city. Instead of a teaser price that changes when you ask, we send a costed, day-by-day quote for your dates — usually within 24 hours."),
]

JS = ("(function(){var f=document.getElementById('hxPlan');if(!f){return;}f.addEventListener('submit',function(e){e.preventDefault();"
      "var d=f.querySelector('[name=d]').value,s=f.querySelector('[name=s]').value,m=f.querySelector('[name=m]').value,a=f.querySelector('[name=a]').value,k=f.querySelector('[name=k]').value,c=f.querySelector('[name=c]').value;"
      "var t='Hi Suzu Travels, please send me a costed Seychelles itinerary.\\nTrip: '+d+'\\nTrip type: '+s+'\\nTravel month: '+m+'\\nAdults: '+a+'\\nChildren: '+k;"
      "if(c){t=t+'\\nDeparting from: '+c;}"
      "window.open('https:'+String.fromCharCode(47,47)+'wa.me/917087488961?text='+encodeURIComponent(t),'_blank','noopener');});})();")

REL = [('mauritius-tour-packages', 'Mauritius', 'suzu-abroad-mauritius', 'Lagoons, Le Morne, island tours'), ('maldives-tour-packages', 'Maldives', 'suzu-card-maldives', 'Overwater villas'),
       ('sri-lanka-tour-packages', 'Sri Lanka', 'suzu-card-sri-lanka', 'Beaches & tea country'), ('bali-tour-packages', 'Bali', 'suzu-card-bali', 'Ubud, villas, temples'),
       ('philippines-tour-packages', 'Philippines', 'PH', 'Palawan, Boracay, Bohol'), ('thailand-tour-packages', 'Thailand', 'suzu-card-thailand', 'Bangkok, Phuket, Krabi'),
       ('dubai-tour-packages', 'Dubai', 'suzu-abroad-dubai', 'Burj Khalifa, desert, Abu Dhabi'), ('egypt-tour-packages', 'Egypt', 'suzu-abroad-egypt', 'Cairo, Nile cruise, Luxor'),
       ('turkey-tour-packages', 'Turkey', 'suzu-abroad-turkey', 'Istanbul, Cappadocia, Pamukkale'), ('europe-tour-packages', 'Europe', 'suzu-abroad-europe', 'Paris, Swiss Alps, Italy'),
       ('switzerland-tour-packages', 'Switzerland', 'suzu-abroad-switzerland', 'Lucerne, Jungfrau, Zermatt'), ('uk-tour-packages', 'UK', 'suzu-abroad-uk', 'London, Cotswolds, Scotland'),
       ('iceland-tour-packages', 'Iceland', 'IS', 'Golden Circle, glaciers, northern lights'), ('norway-tour-packages', 'Norway', 'NO', 'Fjords, Flåm Railway, Bergen'),
       ('russia-tour-packages', 'Russia', 'RU', 'Moscow, Saint Petersburg'),
       ('new-zealand-tour-packages', 'New Zealand', 'NZ', 'Queenstown, Milford, Mount Cook'), ('australia-tour-packages', 'Australia & NZ', 'suzu-abroad-australia', 'Sydney, Melbourne, Queenstown'),
       ('japan-tour-packages', 'Japan', 'suzu-abroad-japan', 'Tokyo, Fuji, Kyoto, Osaka'), ('south-korea-tour-packages', 'South Korea', 'KR', 'Seoul, Busan, Jeju'),
       ('china-tour-packages', 'China', 'CN', 'Great Wall, Xi’an, Shanghai'), ('hong-kong-tour-packages', 'Hong Kong & Macau', 'HK', 'Harbour, Peak, Disneyland, Macau'),
       ('georgia-tour-packages', 'Georgia', 'suzu-abroad-georgia', 'Tbilisi, Kazbegi, Gudauri'),
       ('azerbaijan-tour-packages', 'Azerbaijan', 'suzu-abroad-azerbaijan', 'Baku, Gabala, Shahdag'), ('armenia-tour-packages', 'Armenia', 'suzu-abroad-armenia', 'Yerevan, Garni, Sevan'),
       ('uzbekistan-tour-packages', 'Uzbekistan', 'suzu-abroad-uzbekistan', 'Samarkand, Bukhara, Khiva'), ('kazakhstan-tour-packages', 'Kazakhstan', 'suzu-abroad-kazakhstan', 'Almaty, lakes, Kyrgyzstan'),
       ('vietnam-tour-packages', 'Vietnam', 'suzu-card-vietnam', 'Hanoi, Ha Long, Hoi An'), ('cambodia-tour-packages', 'Cambodia', 'KH', 'Angkor Wat, Siem Reap, Phnom Penh'),
       ('malaysia-tour-packages', 'Malaysia', 'suzu-card-malaysia', 'KL, Langkawi, Genting'),
       ('singapore-tour-packages', 'Singapore', 'suzu-card-singapore', 'City, Sentosa, Universal'),
       ('nepal-tour-packages', 'Nepal', 'suzu-card-nepal', 'No visa for Indians'), ('bhutan-tour-packages', 'Bhutan', 'suzu-card-bhutan', 'Paro, Thimphu, Punakha')]
SPECIAL_IMG = {'IS': 'https://suzutravels.com/wp-content/uploads/2026/11/iceland-jokulsarlon-glacier-lagoon-768x509.webp',
               'NO': 'https://suzutravels.com/wp-content/uploads/2026/11/norway-geirangerfjord-from-ornesvingen-768x431.webp',
               'HK': 'https://suzutravels.com/wp-content/uploads/2026/11/hong-kong-victoria-harbour-night-from-the-peak-768x363.webp',
               'CN': 'https://suzutravels.com/wp-content/uploads/2026/11/china-great-wall-mutianyu-768x575.webp',
               'RU': 'https://suzutravels.com/wp-content/uploads/2026/11/russia-moscow-saint-basils-cathedral-red-square-768x512.webp',
               'NZ': 'https://suzutravels.com/wp-content/uploads/2026/11/new-zealand-milford-sound-mitre-peak-768x481.webp',
               'PH': 'https://suzutravels.com/wp-content/uploads/2026/11/philippines-el-nido-big-lagoon-palawan-768x512.webp',
               'KR': 'https://suzutravels.com/wp-content/uploads/2026/11/south-korea-seoul-gyeongbokgung-geunjeongjeon-768x432.webp',
               'KH': 'https://suzutravels.com/wp-content/uploads/2026/11/cambodia-angkor-wat-reflection-pond-768x499.webp'}

def build():
    W = "Hi Suzu Travels, I'm planning a Seychelles trip. Please share a quote."
    h = [f'<div class="suzu-intl hx hx-country"><style>{CSS}</style>']
    slides = ''.join(f'<div class="hx-slide"><img src="{U(s)}" alt="{A(s)}" width="1600" height="1000" {"fetchpriority=\"high\" loading=\"eager\"" if i == 0 else "loading=\"lazy\""} decoding="async"><span class="hx-cap">{C(s)}</span></div>' for i, s in enumerate(HERO))
    h.append('<section class="hx-hero" aria-label="Seychelles tour packages from India"><div class="hx-slides">' + slides + '</div><div class="hx-copy">'
             '<p class="hx-lede">Walk between the granite boulders of Anse Source d&rsquo;Argent on La Digue, swim at Anse Lazio on Praslin, meet the giant tortoises of Curieuse and end the day with a sunset on Mahé. We plan Seychelles to your dates, budget and pace, with hotels, ferries and island tours lined up, vegetarian meals noted in advance and honest guidance on the entry rules.</p>'
             '<div class="hx-badges">'
             f'<span class="hx-badge">{svg("globe")}Mahé, Praslin &amp; La Digue</span><span class="hx-badge">{svg("doc")}No visa — entry steps explained</span>'
             f'<span class="hx-badge">{svg("team")}Honeymoons, families &amp; groups</span><span class="hx-badge">{svg("food")}Vegetarian meals planned</span></div>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Get a Seychelles Quote {svg("arrow")}</a>'
             f'<a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div></div>'
             '<form class="hx-plan" id="hxPlan" aria-label="Get a costed Seychelles itinerary on WhatsApp"><h3>Plan my Seychelles trip</h3>'
             '<p>Tell us the basics — we reply on WhatsApp with a costed, day-by-day plan, usually within 24 hours.</p><div class="hx-f">'
             '<label class="hx-full">Trip<select name="d"><option selected>Mahé, Praslin &amp; La Digue</option><option>Honeymoon: beach resort + island hopping</option><option>Mahé only (short trip)</option><option>Seychelles + Mauritius</option><option>Seychelles + Dubai stopover</option><option>Not sure yet</option></select></label>'
             '<label>Trip type<select name="s"><option>Honeymoon / couple</option><option>Family</option><option>Friends</option><option>Seniors</option><option>Group</option><option>Corporate / MICE</option></select></label>'
             f'<label>Travel month<select name="m">{G.months()}</select></label>'
             '<label>Adults<select name="a"><option>1</option><option selected>2</option><option>3</option><option>4</option><option>5</option><option>6</option><option>7–10</option><option>11–20</option><option>20+</option></select></label>'
             '<label>Children<select name="k"><option>0</option><option>1</option><option>2</option><option>3</option><option>4+</option></select></label>'
             '<label class="hx-full">Departing from<input name="c" type="text" placeholder="e.g. Delhi, Mumbai, Chandigarh" autocomplete="address-level2"></label></div>'
             f'<button class="hx-btn" type="submit">{WA_SVG}Get my Seychelles plan on WhatsApp</button><small>Opens WhatsApp with your details filled in. We do not store anything on this page.</small></form></section>')
    h.append('<div class="hx-trust">'
             f'<div>{svg("clock")}<span><b>Quote in ~24 hours</b><span>Costed, day by day</span></span></div>'
             f'<div>{svg("doc")}<span><b>Honest entry guidance</b><span>Official Seychelles sources, checked</span></span></div>'
             f'<div>{svg("shield")}<span><b>HP Tourism registered</b><span>Reg. DTO-MND-11-243/2022</span></span></div>'
             f'<div>{svg("chat")}<span><b>One team, start to finish</b><span>Reachable while you travel</span></span></div></div>')
    h.append('<nav class="hx-toc" aria-label="On this page"><a href="#why-seychelles">Why Seychelles</a><a href="#seychelles-in-photos">Photos</a><a href="#how-to-choose">Choose your trip</a><a href="#sample-itinerary">Sample itinerary</a><a href="#when-to-go">When to go</a><a href="#visa-and-entry">Entry rules</a><a href="#whats-included">What\'s included</a><a href="#seychelles-faq">FAQ</a></nav>')
    facts = [('Getting there', 'Fly into Seychelles International Airport on Mahé — we compare routes and connections from your city'), ('Time difference', 'India is 1 hour 30 minutes ahead of Seychelles'), ('Currency', 'Seychelles rupee (SCR)'),
             ('Best season', 'April–May and October–November are often the calmest; warm all year'), ('Typical trip', '6 to 7 nights across Mahé, Praslin and La Digue'), ('Entry', 'No visa for Indians — Visitor&rsquo;s Permit on arrival; Travel Authorisation before you fly')]
    h.append('<section id="why-seychelles" class="hx-sec"><span class="hx-eye">Seychelles</span><h2>Why Seychelles is worth it for Indian travellers</h2>'
             '<p class="hx-sub">Seychelles is a group of islands in the Indian Ocean, known for white-sand coves between smooth granite boulders, clear turquoise water and green hills. Most trips combine three islands: Mahé, with the capital Victoria and the international airport; Praslin, with Anse Lazio and the Vallée de Mai nature reserve; and La Digue, a small island best explored by bicycle. There is no visa to apply for in advance — you complete an online Travel Authorisation before you fly — which makes it an easy choice for a honeymoon or a short beach holiday.</p>'
             '<div class="hx-facts">' + ''.join(f'<div class="hx-fact"><b>{a}</b><span>{b}</span></div>' for a, b in facts) + '</div></section>')
    h.append('<section id="seychelles-in-photos" class="hx-sec"><span class="hx-eye">Real places</span><h2>Seychelles in photos</h2>'
             '<p class="hx-sub">Granite boulders on the shore of Anse Source d&rsquo;Argent, the Navashakti Vinayagar Temple in Victoria, the rocky coast of Curieuse Island, the Clock Tower in Victoria, a leaning palm at Anse Takamaka, sunset at Port Glaud and sunrise at Anse Royale. Real photos by Wikimedia Commons photographers, credited below.</p><div class="hx-pg">'
             + ''.join(f'<figure><img src="{U(k) if j == 0 else M[k]["med"]}" alt="{A(k)}" width="800" height="600" loading="lazy" decoding="async"><figcaption>{C(k)}</figcaption></figure>' for j, k in enumerate(GAL)) + '</div></section>')
    cards = [('First-timers', 'Three islands in one trip', 'Mahé, Praslin and La Digue — Victoria, Anse Lazio, the Vallée de Mai and Anse Source d&rsquo;Argent, linked by ferry.'),
             ('Couples', 'Beach honeymoon', 'A quiet beach hotel or resort, sunset evenings, a boat day around the islands and an unhurried pace with one or two island moves.'),
             ('Families', 'Easy island holiday', 'Calm-water beaches, giant tortoises on Curieuse, cycling on La Digue and short, simple transfers between hotels.'),
             ('Combine', 'Seychelles &amp; more', 'Pair Seychelles with Mauritius or a Dubai stopover — we plan the order and flight connections around your dates.')]
    stays = [('Mahé — Beau Vallon &amp; the west coast', 'Beach hotels close to restaurants, with easy access to Victoria and the ferry jetty.'),
             ('Mahé — the south', 'Quieter coves such as Anse Intendance and Anse Takamaka, and resort stays for a slower honeymoon.'),
             ('Praslin', 'Hotels near Anse Lazio or Côte d&rsquo;Or, close to the Vallée de Mai and boat trips to Curieuse.'),
             ('La Digue', 'Small guesthouses and hotels a short bicycle ride from Anse Source d&rsquo;Argent and Grand Anse.')]
    h.append('<section id="how-to-choose" class="hx-sec"><span class="hx-eye">How to choose</span><h2>Choose the Seychelles trip that fits you</h2>'
             '<p class="hx-sub">Start from the kind of trip you want — we fine-tune the islands, hotels, ferries and tours to your group and season.</p><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><span class="hx-tag">{t}</span><h3>{n}</h3><p>{d}</p></div>' for t, n, d in cards) + '</div>'
             '<h3 style="margin-top:30px">Where to stay</h3><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><h3>{n}</h3><p>{d}</p></div>' for n, d in stays) + '</div></section>')
    days = [('Day 1', 'Arrive on Mahé', 'Transfer from the airport to your beach hotel. Easy evening on the beach.'),
            ('Day 2', 'Mahé island tour', 'Victoria&rsquo;s market and Clock Tower, the Navashakti Vinayagar Temple, a mountain viewpoint and the beaches of the south coast.'),
            ('Day 3', 'Ferry to Praslin', 'Ferry to Praslin, then the Vallée de Mai nature reserve with its coco de mer palms; afternoon at Anse Lazio.'),
            ('Day 4', 'Curieuse &amp; island boat trip', 'Boat day to Curieuse Island for the giant tortoises, with snorkelling stops when the sea allows.'),
            ('Day 5', 'La Digue by bicycle', 'Short ferry to La Digue, cycle to Anse Source d&rsquo;Argent and see Grand Anse; overnight on La Digue or return to Praslin.'),
            ('Day 6', 'Back to Mahé', 'Ferry back to Mahé and a free afternoon — a beach, a sunset at Port Glaud or a little shopping in Victoria.'),
            ('Day 7', 'Fly home', 'Transfer to the airport for your flight home — or add a Dubai stopover on the way.')]
    h.append('<section id="sample-itinerary" class="hx-sec"><span class="hx-eye">Sample plan</span><h2>A sample 7-day Seychelles itinerary</h2>'
             '<p class="hx-sub">The classic three-island trip. We rebuild it around you — slow it down with a resort stay for a honeymoon, keep it to Mahé for a short break, or add Mauritius.</p><div class="hx-itin">'
             + ''.join(f'<div class="hx-day"><i>{a}</i><b>{b}</b><p>{c}</p></div>' for a, b, c in days) + '</div></section>')
    seasons = [('Apr – May', '<span class="hx-ok">Best</span>', 'Warm, often calm', 'A calm period between the trade-wind seasons, often good for beaches, boat days and snorkelling.'),
               ('Jun – Sep', '<span class="hx-ok">Good</span>', 'Drier, breezier', 'Less humid with more wind; seas can be rougher on some coasts, so we choose sheltered beaches and plan boat days with care.'),
               ('Oct – Nov', '<span class="hx-ok">Best</span>', 'Warm, often calm', 'Another calm period between the seasons — a popular time for honeymoons and island hopping.'),
               ('Dec – Mar', '<span class="hx-mid">Humid</span>', 'Hot, more showers', 'Warmer and more humid, with more rain showers that often pass quickly; the Christmas and New Year weeks are busy, so book early.')]
    h.append('<section id="when-to-go" class="hx-sec"><span class="hx-eye">Best season</span><h2>When to go to Seychelles</h2>'
             '<p class="hx-sub">Seychelles is warm all year, so there is no bad month — only different winds and sea conditions. This is general guidance; we check the season, sea conditions and flight prices against your plan before we quote.</p>'
             '<div class="hx-tw"><table class="hx-t"><thead><tr><th>Months</th><th>Verdict</th><th>Weather</th><th>What it means for your trip</th></tr></thead><tbody>'
             + ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in seasons) + '</tbody></table></div></section>')
    h.append('<section id="visa-and-entry" class="hx-sec"><span class="hx-eye">Visa &amp; entry</span><h2>Seychelles entry rules for Indian passport holders</h2>'
             '<div class="hx-visa"><div class="hx-vbox"><h3>What the official sources say</h3><ul>'
             f'<li><b>No visa is needed in advance.</b> Seychelles&rsquo; <a href="{SRC_EMB}" target="_blank" rel="noopener nofollow">Immigration and Civil Status department</a> says a visa is not required to enter Seychelles. A Visitor&rsquo;s Permit is issued on arrival to travellers coming for a holiday, business or to visit friends or family who meet the criteria below.</li>'
             f'<li><b>Travel Authorisation before you fly:</b> according to the <a href="{SRC_VISA}" target="_blank" rel="noopener nofollow">Visitor&rsquo;s Permit page</a>, all visitors must hold a valid Electronic Travel Authorisation before departing from their country of origin — applied for on the official <a href="{SRC_ENTRY}" target="_blank" rel="noopener nofollow">Seychelles Electronic Border System</a> or its Seychelles e-Border app. Any fee is shown there when you apply.</li>'
             '<li><b>Criteria for the Visitor&rsquo;s Permit:</b> a valid return or onward ticket, confirmed accommodation and sufficient funds for the stay (the immigration page mentions a minimum of US$150 or equivalent per day), and you must not be a prohibited immigrant.</li>'
             '<li><b>Passport:</b> valid for the period of your intended stay until you are back in your country of origin or residence.</li>'
             '<li><b>Length of stay:</b> the Visitor&rsquo;s Permit is first granted for up to three months, free of charge; extensions of up to three months at a time, to a maximum of twelve months, carry a fee. Give your correct accommodation address and tell immigration if it changes.</li></ul>'
             f'<p class="hx-checked">Checked {CHECKED} · sources: <a href="{SRC_EMB}" target="_blank" rel="noopener nofollow">Visiting Seychelles — Immigration and Civil Status</a> · <a href="{SRC_VISA}" target="_blank" rel="noopener nofollow">Visitor&rsquo;s Permit — Immigration and Civil Status</a> · <a href="{SRC_ENTRY}" target="_blank" rel="noopener nofollow">Seychelles Electronic Border System (official)</a></p></div>'
             '<div class="hx-vnote"><p><b>Please note:</b> whether you are admitted, and for how long, is always the decision of the Seychelles immigration authorities at the border. We help you prepare clear, consistent documents — itinerary, hotel bookings and return tickets — but we never promise an outcome we do not control.</p>'
             '<p>Entry rules and fees can change. We re-check the official sources when you book, and remind you to complete the Travel Authorisation before your flight.</p></div></div></section>')
    inc = [('doc', 'Entry paperwork help', 'A day-by-day itinerary, hotel confirmations and help with the Seychelles Travel Authorisation form.'), ('pin', 'Hotels', 'Named beach hotels or resorts on Mahé, Praslin and La Digue, chosen for your budget and season.'),
           ('team', 'Ferries &amp; transfers', 'Inter-island ferries or short flights, airport and jetty transfers, and bicycles on La Digue.'), ('globe', 'Tours', 'Mahé island tour, the Vallée de Mai, a Curieuse boat day and snorkelling, as you choose.'),
           ('food', 'Meal plan', 'Breakfast or half board at most hotels; vegetarian and Jain needs noted in advance.'), ('award', 'Flights optional', 'Land-only, or a full package with international flights from your nearest Indian airport.')]
    h.append('<section id="whats-included" class="hx-sec"><span class="hx-eye">Your package</span><h2>What a Suzu Seychelles package includes</h2><div class="hx-inc">'
             + ''.join(f'<div>{svg(i)}<span><b>{t}</b><span>{d}</span></span></div>' for i, t, d in inc) + '</div></section>')
    steps = [('chat', 'Tell us the basics', 'Dates, travellers and the kind of trip you want. A WhatsApp message is enough.'),
             ('doc', 'Get a costed itinerary', 'A day-by-day plan with named hotels and a clear per-person price, usually within 24 hours.'),
             ('sliders', 'Adjust until it fits', 'Change the islands, hotels, tours or add Mauritius. We re-quote as needed.'),
             ('lock', 'Confirm with a token', 'Lock your plan with a small token amount; the balance is paid later, as agreed in writing.')]
    h.append('<section id="how-booking-works" class="hx-sec"><span class="hx-eye">Simple process</span><h2>How booking works</h2><div class="hx-steps">'
             + ''.join(f'<div class="hx-step"><div class="hx-n">{svg(i)}</div><b>{t}</b><p>{d}</p></div>' for i, t, d in steps) + '</div></section>')
    h.append('<section id="seychelles-faq" class="hx-sec"><span class="hx-eye">FAQ</span><h2>Common questions about a Seychelles tour</h2><div class="hx-faqs">'
             + ''.join(f'<details class="hx-faq"{" open" if k == 0 else ""}><summary>{html.escape(q)}</summary><div class="hx-ans"><p>{html.escape(a)}</p></div></details>' for k, (q, a) in enumerate(FAQ)) + '</div></section>')
    def _img(img): return SPECIAL_IMG[img] if img in SPECIAL_IMG else f'https://suzutravels.com/wp-content/uploads/2026/10/{img}.webp'
    h.append('<section id="more-destinations" class="hx-sec"><span class="hx-eye">Explore more</span><h2>Explore more destinations</h2>'
             '<p class="hx-sub">Every trip is planned the same way — your dates, your budget, one team from quote to return. <a href="https://suzutravels.com/international-tour-packages/">See all international holidays →</a></p><div class="hx-mini">'
             + ''.join(f'<a class="hx-mc" href="https://suzutravels.com/{p}/"><img src="{_img(img)}" alt="{html.escape(n)} holiday — Suzu Travels" width="640" height="360" loading="lazy" decoding="async"><span><b>{html.escape(n)}</b><em>{html.escape(e)}</em></span></a>' for p, n, img, e in REL) + '</div></section>')
    h.append(f'<div class="hx-final"><img src="{U(FINAL)}" alt="{A(FINAL)}" width="1600" height="900" loading="lazy" decoding="async">'
             '<h2>Plan your Seychelles trip</h2><p>Send us your dates and group size. We will come back with a costed, day-by-day Seychelles itinerary you can compare, no obligation.</p>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Request a Seychelles Quote {svg("arrow")}</a><a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div>'
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
    open('pages/seychelles-tour-packages.html', 'w').write(o)
    print('pages/seychelles-tour-packages.html', len(o), len(o.encode()))
