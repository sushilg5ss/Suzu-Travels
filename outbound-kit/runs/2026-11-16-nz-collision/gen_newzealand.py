#!/usr/bin/env python3
"""New Zealand page — .hx design; same template as gen_russia.py (10-day itinerary grid = 5 columns, like gen_europe.py).
Run from outbound-kit/:  python3 pages/gen_newzealand.py <PAGE_ID> -> pages/new-zealand-tour-packages.html (one line)
Facts (official Immigration New Zealand pages read 16 Nov 2026):
- visit/.../visa-waiver-countries-and-territories/: India is NOT on the visa waiver list (NZeTA only for waiver passports).
- visas/visitor-visa/: stay up to 6 or 9 months; processing 80% within 2 weeks; busiest Sep-Mar, apply early; do not book
  non-refundable travel until approved; multiple-entry = up to 6 months in each 12-month period, INZ decides single/multiple;
  requirements: good health, good character, genuine intentions, enough money or acceptable sponsor, show you can leave;
  stays <6 months normally no chest X-ray, <12 months normally no medical certificate; partner + dependent children can be
  included; Group Visitor Visa for groups visiting 1 month or less. (Fee and money amounts deliberately not shown.)
- visit/what-you-need-to-visit-new-zealand/: on arrival apply for entry permission + answer biosecurity and customs questions.
Keyword Planner IN 16 Nov 2026: "new zealand tour package" 4,400/mo (focus kw), "new zealand trip cost from india" 1,300,
"new zealand package" 880, "new zealand trip" 880, "new zealand tour package from india" 590, "new zealand visa for indians" 8,100.
Photos: 11 Wikimedia Commons (CC BY 2.5/3.0, CC BY-SA 3.0/4.0; licence read from each file page's wikitext 16 Nov 2026),
WP IDs 22685-22695, + 2 Unsplash photos already on the Australia page (16295 Queenstown, 16303 Milford Sound).
Climate/season wording is general guidance (no figures); no prices.
"""
import json, html, sys, os
sys.path.insert(0, os.getcwd())
import gen_hub as G

PID = int(sys.argv[1]) if len(sys.argv) > 1 else 0
M = G.M
svg, WA_SVG, wa = G.svg, G.WA_SVG, G.wa

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
.hx .hx-itin{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:12px;margin-top:18px}
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
body.page-id-PID .page-header:before{content:"Holidays abroad \00B7  New Zealand";display:inline-block;font:800 12px/1 "Plus Jakarta Sans",sans-serif;letter-spacing:.18em;text-transform:uppercase;color:#1a1606;background:#E2C158;padding:8px 13px;border-radius:999px;margin-bottom:16px}
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
# long title ("New Zealand Tour Packages from India") = 3 lines on phones — extra hero top padding, as on gen_hongkong.py
CSS = CSS + (' @media screen and (max-width:700px){body.page-id-PID .hx .hx-hero{padding-top:262px}}').replace('PID', str(PID))
CHECKED = '16 November 2026'
SRC_VV = 'https://www.immigration.govt.nz/visas/visitor-visa/'
SRC_WAIVER = 'https://www.immigration.govt.nz/visit/what-you-need-to-visit-new-zealand/visa-waiver-countries-and-territories/'
SRC_NEED = 'https://www.immigration.govt.nz/visit/what-you-need-to-visit-new-zealand/'

HERO = ['newzealand-1', 'newzealand-2', 'newzealand-3', 'newzealand-4', 'newzealand-5', 'newzealand-6']
GAL = ['newzealand-7', 'newzealand-8', 'newzealand-13', 'newzealand-9', 'newzealand-10', 'newzealand-11', 'newzealand-12']
FINAL = 'newzealand-2'  # reuses hero slide 2 (Queenstown on Lake Wakatipu)

FAQ = [
    ("Do Indians need a visa for New Zealand?", "Yes. When we checked Immigration New Zealand's website on 16 November 2026, India was not on New Zealand's visa waiver list, so Indian passport holders apply online for a New Zealand Visitor Visa before they travel. Whether a visa is granted, and on what terms, is always the decision of Immigration New Zealand."),
    ("Can Indian passport holders use the NZeTA instead of a visa?", "No. The NZeTA (New Zealand Electronic Travel Authority) is for passport holders of the countries on New Zealand's visa waiver list, and India is not on that list. Indian travellers need a Visitor Visa. If you also hold another passport, we check which rule applies to that passport."),
    ("How long does a New Zealand visitor visa take?", "Immigration New Zealand shows a processing time of 80% of Visitor Visa applications within 2 weeks, and says processing is busiest between September and March, so it asks travellers to apply early with complete information. It also recommends not booking non-refundable travel until the visa is approved — we plan your bookings around that."),
    ("How many days are enough for New Zealand?", "Ten days is a good first trip covering both islands: Auckland and Rotorua in the North Island, then Queenstown, Milford Sound, Wanaka, Mount Cook and Lake Tekapo in the South Island. With 7 to 8 days, focus on the South Island; with 12 to 14 days, add Waitomo, Hobbiton, the West Coast glaciers or a Bay of Islands stay."),
    ("Which is the best time to visit New Zealand from India?", "December to April — New Zealand's summer and early autumn — brings the longest, warmest days and the easiest driving, and fits Indian winter and spring holidays. September to November is spring, with fresh green landscapes. June to August is winter: the ski season around Queenstown and Wanaka, with snow on the mountains and some mountain roads that can close in bad weather."),
    ("Can I combine New Zealand with Australia?", "Yes, many Indian travellers combine the two. They are separate countries with separate visas, so you apply for an Australian visa and a New Zealand Visitor Visa. We plan the order of cities and the flight across the Tasman Sea so the trip flows — see our Australia page for the Australian side."),
    ("Is vegetarian and Indian food available in New Zealand?", "Yes. Auckland, Queenstown, Christchurch and Rotorua have Indian restaurants and many cafés with vegetarian food; in small towns we plan meals in advance. We note vegetarian and Jain needs with your hotels and suggest places on your route."),
    ("Why are there no prices on this page?", "New Zealand costs depend on your dates, the flights from your city, hotel or apartment category, self-drive or chauffeur-driven travel, domestic flights, cruises and activities. Instead of a teaser price that changes when you ask, we send a costed, day-by-day quote for your dates — usually within 24 hours."),
]

JS = ("(function(){var f=document.getElementById('hxPlan');if(!f){return;}f.addEventListener('submit',function(e){e.preventDefault();"
      "var d=f.querySelector('[name=d]').value,s=f.querySelector('[name=s]').value,m=f.querySelector('[name=m]').value,a=f.querySelector('[name=a]').value,k=f.querySelector('[name=k]').value,c=f.querySelector('[name=c]').value;"
      "var t='Hi Suzu Travels, please send me a costed New Zealand itinerary.\\nTrip: '+d+'\\nTrip type: '+s+'\\nTravel month: '+m+'\\nAdults: '+a+'\\nChildren: '+k;"
      "if(c){t=t+'\\nDeparting from: '+c;}"
      "window.open('https:'+String.fromCharCode(47,47)+'wa.me/917087488961?text='+encodeURIComponent(t),'_blank','noopener');});})();")

REL = [('australia-tour-packages', 'Australia', 'suzu-abroad-australia', 'Sydney, Melbourne, Gold Coast'), ('japan-tour-packages', 'Japan', 'suzu-abroad-japan', 'Tokyo, Fuji, Kyoto, Osaka'),
       ('europe-tour-packages', 'Europe', 'suzu-abroad-europe', 'Paris, Swiss Alps, Italy'), ('switzerland-tour-packages', 'Switzerland', 'suzu-abroad-switzerland', 'Lucerne, Jungfrau, Zermatt'),
       ('uk-tour-packages', 'UK', 'suzu-abroad-uk', 'London, Cotswolds, Scotland'), ('russia-tour-packages', 'Russia', 'RU', 'Moscow, St Petersburg, Kazan'),
       ('turkey-tour-packages', 'Turkey', 'suzu-abroad-turkey', 'Istanbul, Cappadocia, Pamukkale'), ('georgia-tour-packages', 'Georgia', 'suzu-abroad-georgia', 'Tbilisi, Kazbegi, Gudauri'),
       ('azerbaijan-tour-packages', 'Azerbaijan', 'suzu-abroad-azerbaijan', 'Baku, Gabala, Shahdag'), ('armenia-tour-packages', 'Armenia', 'suzu-abroad-armenia', 'Yerevan, Garni, Sevan'),
       ('uzbekistan-tour-packages', 'Uzbekistan', 'suzu-abroad-uzbekistan', 'Samarkand, Bukhara, Khiva'), ('kazakhstan-tour-packages', 'Kazakhstan', 'suzu-abroad-kazakhstan', 'Almaty, lakes, Kyrgyzstan'),
       ('china-tour-packages', 'China', 'CN', 'Great Wall, Xi’an, Shanghai'), ('hong-kong-tour-packages', 'Hong Kong & Macau', 'HK', 'Harbour, Peak, Disneyland, Macau'),
       ('dubai-tour-packages', 'Dubai', 'suzu-abroad-dubai', 'Burj Khalifa, desert, Abu Dhabi'), ('egypt-tour-packages', 'Egypt', 'suzu-abroad-egypt', 'Cairo, Nile cruise, Luxor'),
       ('singapore-tour-packages', 'Singapore', 'suzu-card-singapore', 'City, Sentosa, Universal'), ('thailand-tour-packages', 'Thailand', 'suzu-card-thailand', 'Bangkok, Phuket, Krabi'),
       ('malaysia-tour-packages', 'Malaysia', 'suzu-card-malaysia', 'KL, Langkawi, Genting'), ('vietnam-tour-packages', 'Vietnam', 'suzu-card-vietnam', 'Hanoi, Ha Long, Hoi An'),
       ('bali-tour-packages', 'Bali', 'suzu-card-bali', 'Ubud, villas, temples'), ('maldives-tour-packages', 'Maldives', 'suzu-card-maldives', 'Overwater villas'),
       ('mauritius-tour-packages', 'Mauritius', 'suzu-abroad-mauritius', 'Lagoons, Le Morne, island tours'), ('sri-lanka-tour-packages', 'Sri Lanka', 'suzu-card-sri-lanka', 'Beaches & tea country'),
       ('nepal-tour-packages', 'Nepal', 'suzu-card-nepal', 'No visa for Indians'), ('bhutan-tour-packages', 'Bhutan', 'suzu-card-bhutan', 'Paro, Thimphu, Punakha')]
SPECIAL_IMG = {'HK': 'https://suzutravels.com/wp-content/uploads/2026/11/hong-kong-victoria-harbour-night-from-the-peak-768x363.webp',
               'CN': 'https://suzutravels.com/wp-content/uploads/2026/11/china-great-wall-mutianyu-768x575.webp',
               'RU': 'https://suzutravels.com/wp-content/uploads/2026/11/russia-moscow-saint-basils-cathedral-red-square-768x512.webp'}

def build():
    W = "Hi Suzu Travels, I'm planning a New Zealand trip. Please share a quote."
    h = [f'<div class="suzu-intl hx hx-country"><style>{CSS}</style>']
    slides = ''.join(f'<div class="hx-slide"><img src="{U(s)}" alt="{A(s)}" width="1600" height="1000" {"fetchpriority=\"high\" loading=\"eager\"" if i == 0 else "loading=\"lazy\""} decoding="async"><span class="hx-cap">{C(s)}</span></div>' for i, s in enumerate(HERO))
    h.append('<section class="hx-hero" aria-label="New Zealand tour packages from India"><div class="hx-slides">' + slides + '</div><div class="hx-copy">'
             '<p class="hx-lede">Cruise between the cliffs of Milford Sound, ride the gondola above Queenstown, walk the Hooker Valley towards Aoraki / Mount Cook, watch the turquoise of Lake Tekapo and feel the steam of Rotorua&rsquo;s geothermal parks. We plan New Zealand to your dates, budget and pace — honeymoon, family road trip or snow holiday — with comfortable stays, vegetarian meals noted in advance and honest guidance on the New Zealand Visitor Visa.</p>'
             '<div class="hx-badges">'
             f'<span class="hx-badge">{svg("globe")}North &amp; South Island</span><span class="hx-badge">{svg("doc")}Visitor Visa guidance</span>'
             f'<span class="hx-badge">{svg("team")}Honeymoons, families &amp; groups</span><span class="hx-badge">{svg("food")}Vegetarian meals planned</span></div>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Get a New Zealand Quote {svg("arrow")}</a>'
             f'<a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div></div>'
             '<form class="hx-plan" id="hxPlan" aria-label="Get a costed New Zealand itinerary on WhatsApp"><h3>Plan my New Zealand trip</h3>'
             '<p>Tell us the basics — we reply on WhatsApp with a costed, day-by-day plan, usually within 24 hours.</p><div class="hx-f">'
             '<label class="hx-full">Trip<select name="d"><option selected>North + South Island (classic)</option><option>South Island only (Queenstown, Milford, Mount Cook)</option><option>Honeymoon in New Zealand</option><option>Self-drive road trip</option><option>Winter / ski in Queenstown</option><option>New Zealand + Australia</option><option>Not sure yet</option></select></label>'
             '<label>Trip type<select name="s"><option>Family</option><option>Honeymoon / couple</option><option>Friends</option><option>Seniors</option><option>Group</option><option>Corporate / MICE</option></select></label>'
             f'<label>Travel month<select name="m">{G.months()}</select></label>'
             '<label>Adults<select name="a"><option>1</option><option selected>2</option><option>3</option><option>4</option><option>5</option><option>6</option><option>7–10</option><option>11–20</option><option>20+</option></select></label>'
             '<label>Children<select name="k"><option>0</option><option>1</option><option>2</option><option>3</option><option>4+</option></select></label>'
             '<label class="hx-full">Departing from<input name="c" type="text" placeholder="e.g. Delhi, Mumbai, Chandigarh" autocomplete="address-level2"></label></div>'
             f'<button class="hx-btn" type="submit">{WA_SVG}Get my New Zealand plan on WhatsApp</button><small>Opens WhatsApp with your details filled in. We do not store anything on this page.</small></form></section>')
    h.append('<div class="hx-trust">'
             f'<div>{svg("clock")}<span><b>Quote in ~24 hours</b><span>Costed, day by day</span></span></div>'
             f'<div>{svg("doc")}<span><b>Honest visa guidance</b><span>Official Immigration NZ rules, checked</span></span></div>'
             f'<div>{svg("shield")}<span><b>HP Tourism registered</b><span>Reg. DTO-MND-11-243/2022</span></span></div>'
             f'<div>{svg("chat")}<span><b>One team, start to finish</b><span>Reachable while you travel</span></span></div></div>')
    h.append('<nav class="hx-toc" aria-label="On this page"><a href="#why-new-zealand">Why New Zealand</a><a href="#new-zealand-in-photos">Photos</a><a href="#how-to-choose">Choose your trip</a><a href="#sample-itinerary">Sample itinerary</a><a href="#when-to-go">When to go</a><a href="#visa-and-entry">Visa</a><a href="#whats-included">What\'s included</a><a href="#new-zealand-faq">FAQ</a></nav>')
    facts = [('Getting there', 'Fly into Auckland, Queenstown or Christchurch; we compare connecting flights from your city'), ('Time difference', 'New Zealand is 6 hours 30 minutes ahead of India (7 hours 30 minutes during NZ summer time)'), ('Currency', 'New Zealand dollar (NZD); cards are widely accepted'),
             ('Best season', 'December to April; June to August for snow and skiing'), ('Typical trip', '8 to 12 nights; 14 to 16 with Australia'), ('Entry', 'Visitor Visa applied online before travel')]
    h.append('<section id="why-new-zealand" class="hx-sec"><span class="hx-eye">New Zealand</span><h2>Why New Zealand is worth the long flight from India</h2>'
             '<p class="hx-sub">Two islands, one easy trip: the North Island with Auckland, the geysers and Māori culture of Rotorua and the volcanoes of Tongariro, and the South Island with Queenstown, the fjords of Milford Sound, the lakes of Wanaka, Tekapo and Pukaki, and Aoraki / Mount Cook. Short domestic flights and scenic drives link them. Indian passport holders apply online for a Visitor Visa — we walk you through the official steps.</p>'
             '<div class="hx-facts">' + ''.join(f'<div class="hx-fact"><b>{a}</b><span>{b}</span></div>' for a, b in facts) + '</div></section>')
    h.append('<section id="new-zealand-in-photos" class="hx-sec"><span class="hx-eye">Real places</span><h2>New Zealand in photos</h2>'
             '<p class="hx-sub">Auckland from Mount Eden, Ngauruhoe and Ruapehu in Tongariro National Park, Milford Sound, Lake Tekapo, Lake Wanaka at sunrise, Lake Pukaki and the view from the Remarkables above Queenstown. Real photos by Wikimedia Commons and Unsplash photographers, credited below.</p><div class="hx-pg">'
             + ''.join(f'<figure><img src="{U(k)}" alt="{A(k)}" width="800" height="600" loading="lazy" decoding="async"><figcaption>{C(k)}</figcaption></figure>' for k in GAL) + '</div></section>')
    cards = [('First-timers', 'North &amp; South Island', 'The classic first trip: Auckland and Rotorua, then Queenstown, Milford Sound, Wanaka, Mount Cook and Lake Tekapo.'),
             ('Honeymoon', 'Lakes, fjords &amp; stars', 'Lake-view stays in Queenstown and Wanaka, a Milford Sound cruise, a scenic flight if you like, and a night under the dark skies of Lake Tekapo.'),
             ('Families', 'New Zealand with children', 'Easy driving days, gondolas and luge rides, geothermal parks, farm and wildlife visits, and family apartments with kitchens.'),
             ('Winter', 'Snow in Queenstown', 'June to August is ski season around Queenstown and Wanaka — lessons for beginners, snow play for children and cosy lakeside evenings.')]
    stays = [('Auckland — city centre &amp; waterfront', 'Walk to the Sky Tower, the Viaduct Harbour and the ferries; easy for an arrival night after a long flight.'),
             ('Rotorua — near the lake', 'Close to the geothermal parks, Māori cultural evenings and restaurants, with lake views from many hotels.'),
             ('Queenstown — town centre or lakefront', 'Walk to the gondola, the lake cruises and restaurants; the base for Milford Sound and the ski fields.'),
             ('Lake Tekapo &amp; Mount Cook', 'Small lakeside or alpine lodges for stargazing at Tekapo and the Hooker Valley walk at Mount Cook.')]
    h.append('<section id="how-to-choose" class="hx-sec"><span class="hx-eye">How to choose</span><h2>Choose the New Zealand trip that fits you</h2>'
             '<p class="hx-sub">Start from the kind of trip you want — we fine-tune the islands, stays, flights, car or chauffeur and activities to your group.</p><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><span class="hx-tag">{t}</span><h3>{n}</h3><p>{d}</p></div>' for t, n, d in cards) + '</div>'
             '<h3 style="margin-top:30px">Where to stay</h3><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><h3>{n}</h3><p>{d}</p></div>' for n, d in stays) + '</div></section>')
    days = [('Day 1', 'Arrive in Auckland', 'Airport transfer to your hotel. An easy evening on the waterfront or up the Sky Tower.'),
            ('Day 2', 'Auckland to Rotorua', 'Drive south through farmland, with an optional stop at Hobbiton (Matamata) or the Waitomo glowworm caves.'),
            ('Day 3', 'Rotorua', 'Geothermal parks such as Wai-O-Tapu with its Champagne Pool, then a Māori cultural evening.'),
            ('Day 4', 'Fly to Queenstown', 'Short flight to Queenstown. Skyline Gondola and an evening by Lake Wakatipu.'),
            ('Day 5', 'Queenstown', 'Lake cruise, Arrowtown or a day of adventure — jet boat, luge or bungy, as you choose.'),
            ('Day 6', 'Milford Sound', 'Full-day trip through Fiordland to Milford Sound for a cruise beneath the cliffs and waterfalls.'),
            ('Day 7', 'Wanaka', 'Drive over the Crown Range to Wanaka for the lake, the lakeside walks and a relaxed evening.'),
            ('Day 8', 'Mount Cook', 'Drive past Lake Pukaki to Aoraki / Mount Cook National Park and walk the Hooker Valley track.'),
            ('Day 9', 'Lake Tekapo to Christchurch', 'Morning at Lake Tekapo and the Church of the Good Shepherd, then on to Christchurch.'),
            ('Day 10', 'Fly home', 'Free morning in Christchurch, then transfer to the airport for your flight home.')]
    h.append('<section id="sample-itinerary" class="hx-sec"><span class="hx-eye">Sample plan</span><h2>A sample 10-day New Zealand itinerary</h2>'
             '<p class="hx-sub">The classic first trip across both islands. We rebuild it around you — South Island only, a self-drive version, more nights in Queenstown, the West Coast glaciers, or Australia before or after.</p><div class="hx-itin">'
             + ''.join(f'<div class="hx-day"><i>{a}</i><b>{b}</b><p>{c}</p></div>' for a, b, c in days) + '</div></section>')
    seasons = [('Dec – Feb', '<span class="hx-ok">Best</span>', 'Summer, long days', 'The main season: warm, long days for lakes, cruises and walks; book early for school holidays and New Year.'),
               ('Mar – Apr', '<span class="hx-ok">Best</span>', 'Autumn, mild', 'Settled weather, autumn colours around Queenstown, Arrowtown and Wanaka, and fewer crowds than midsummer.'),
               ('Sep – Nov', '<span class="hx-mid">Good</span>', 'Spring, changeable', 'Green landscapes, lambs and flowers; weather changes quickly, so we keep some flexibility in the plan.'),
               ('Jun – Aug', '<span class="hx-mid">Snow</span>', 'Winter, cold', 'Ski season around Queenstown and Wanaka; short days, and some mountain roads can close in bad weather.'),
               ('May', '<span class="hx-mid">Quiet</span>', 'Cool', 'Quiet and good value between autumn and the ski season; cooler days and early darkness.')]
    h.append('<section id="when-to-go" class="hx-sec"><span class="hx-eye">Best season</span><h2>When to go to New Zealand</h2>'
             '<p class="hx-sub">New Zealand&rsquo;s seasons are the opposite of India&rsquo;s: summer runs from December to February and winter from June to August. We check the season, school holidays and flight prices against your plan before we quote.</p>'
             '<div class="hx-tw"><table class="hx-t"><thead><tr><th>Months</th><th>Verdict</th><th>Weather</th><th>What it means for your trip</th></tr></thead><tbody>'
             + ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in seasons) + '</tbody></table></div></section>')
    h.append('<section id="visa-and-entry" class="hx-sec"><span class="hx-eye">Visa &amp; entry</span><h2>New Zealand visitor visa for Indian passport holders</h2>'
             '<div class="hx-visa"><div class="hx-vbox"><h3>What the official rules say</h3><ul>'
             '<li><b>A visa is needed.</b> India is not on New Zealand&rsquo;s visa waiver list, so Indian passport holders apply for a <b>Visitor Visa</b> before travel. The NZeTA (electronic travel authority) is only for passports from visa waiver countries.</li>'
             f'<li><b>Apply online with Immigration New Zealand</b> on its official website: <a href="{SRC_VV}" target="_blank" rel="noopener nofollow">immigration.govt.nz</a>. Immigration New Zealand shows a processing time of <b>80% of applications within 2 weeks</b>, says it is busiest between <b>September and March</b>, and recommends <b>not booking non-refundable travel</b> until the visa is approved.</li>'
             '<li><b>What you must show:</b> genuine plans for a visit and to leave at the end of it, enough money for your stay (or an acceptable sponsor), and good health and character. A holiday visit does not normally need a chest X-ray or medical certificate.</li>'
             '<li><b>Length of stay:</b> Immigration New Zealand decides whether to issue a multiple-entry or a single-entry visa; a multiple-entry Visitor Visa allows stays of up to 6 months in each 12-month period. Partners and dependent children can be included in the same application.</li>'
             '<li><b>Groups and arrival:</b> tour groups visiting for 1 month or less may be able to apply for a Group Visitor Visa. On arrival you apply for entry permission and answer biosecurity and customs questions.</li></ul>'
             f'<p class="hx-checked">Checked {CHECKED} · sources: <a href="{SRC_VV}" target="_blank" rel="noopener nofollow">Immigration New Zealand — Visitor Visa</a> · <a href="{SRC_WAIVER}" target="_blank" rel="noopener nofollow">visa waiver countries and territories</a> · <a href="{SRC_NEED}" target="_blank" rel="noopener nofollow">what you need to visit New Zealand</a></p></div>'
             '<div class="hx-vnote"><p><b>Please note:</b> whether a visa is granted, and on what terms, is always the decision of Immigration New Zealand, and admission at the border is decided on arrival. We help you prepare a complete application, but we never promise an outcome we do not control.</p>'
             '<p>We give you a day-by-day itinerary and hotel details for your application, a checklist of the documents to gather, and we confirm non-refundable bookings only once your visa is approved. Combining with Australia? That is a separate Australian visa — we plan both timelines together.</p></div></div></section>')
    inc = [('doc', 'Visa help', 'A day-by-day itinerary, hotel details and a document checklist for your Visitor Visa application.'), ('pin', 'Stays', 'Named hotels, lodges or apartments in Auckland, Rotorua, Queenstown, Wanaka, Mount Cook or Tekapo and Christchurch.'),
           ('team', 'Transfers &amp; driving', 'Airport transfers, domestic flights, and a self-drive car or a private chauffeur-driven vehicle, as you prefer.'), ('globe', 'Cruises &amp; activities', 'Milford Sound cruise, Skyline Gondola, geothermal park and Māori cultural evening tickets, plus optional adventures.'),
           ('food', 'Meal plan', 'Breakfast at most stays; vegetarian and Jain needs noted in advance, with Indian restaurant suggestions.'), ('award', 'Flights optional', 'Land-only, or a full package with international flights from your nearest Indian airport.')]
    h.append('<section id="whats-included" class="hx-sec"><span class="hx-eye">Your package</span><h2>What a Suzu New Zealand package includes</h2><div class="hx-inc">'
             + ''.join(f'<div>{svg(i)}<span><b>{t}</b><span>{d}</span></span></div>' for i, t, d in inc) + '</div></section>')
    steps = [('chat', 'Tell us the basics', 'Dates, travellers and the kind of trip you want. A WhatsApp message is enough.'),
             ('doc', 'Get a costed itinerary', 'A day-by-day plan with named stays and a clear per-person price, usually within 24 hours.'),
             ('sliders', 'Adjust until it fits', 'Change the islands, stays, car or add-ons. We re-quote as needed.'),
             ('lock', 'Confirm with a token', 'Lock your plan with a small token amount; the balance is paid later, as agreed in writing.')]
    h.append('<section id="how-booking-works" class="hx-sec"><span class="hx-eye">Simple process</span><h2>How booking works</h2><div class="hx-steps">'
             + ''.join(f'<div class="hx-step"><div class="hx-n">{svg(i)}</div><b>{t}</b><p>{d}</p></div>' for i, t, d in steps) + '</div></section>')
    h.append('<section id="new-zealand-faq" class="hx-sec"><span class="hx-eye">FAQ</span><h2>Common questions about a New Zealand tour</h2><div class="hx-faqs">'
             + ''.join(f'<details class="hx-faq"{" open" if k == 0 else ""}><summary>{html.escape(q)}</summary><div class="hx-ans"><p>{html.escape(a)}</p></div></details>' for k, (q, a) in enumerate(FAQ)) + '</div></section>')
    def _img(img): return SPECIAL_IMG[img] if img in SPECIAL_IMG else f'https://suzutravels.com/wp-content/uploads/2026/10/{img}.webp'
    h.append('<section id="more-destinations" class="hx-sec"><span class="hx-eye">Explore more</span><h2>Explore more destinations</h2>'
             '<p class="hx-sub">Every trip is planned the same way — your dates, your budget, one team from quote to return. <a href="https://suzutravels.com/international-tour-packages/">See all international holidays →</a></p><div class="hx-mini">'
             + ''.join(f'<a class="hx-mc" href="https://suzutravels.com/{p}/"><img src="{_img(img)}" alt="{html.escape(n)} holiday — Suzu Travels" width="640" height="360" loading="lazy" decoding="async"><span><b>{html.escape(n)}</b><em>{html.escape(e)}</em></span></a>' for p, n, img, e in REL) + '</div></section>')
    h.append(f'<div class="hx-final"><img src="{U(FINAL)}" alt="{A(FINAL)}" width="1600" height="900" loading="lazy" decoding="async">'
             '<h2>Plan your New Zealand trip</h2><p>Send us your dates and group size. We will come back with a costed, day-by-day New Zealand itinerary you can compare, no obligation.</p>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Request a New Zealand Quote {svg("arrow")}</a><a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div>'
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
    open('pages/new-zealand-tour-packages.html', 'w').write(o)
    print('pages/new-zealand-tour-packages.html', len(o), len(o.encode()))
