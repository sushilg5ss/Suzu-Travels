#!/usr/bin/env python3
"""South Korea page - .hx design; same template as gen_philippines.py / gen_russia.py.
Run from outbound-kit/:  python3 pages/gen_southkorea.py <PAGE_ID> -> pages/south-korea-tour-packages.html (one line)
Facts (official pages read 18 Nov 2026):
- Consulate General of the Republic of Korea in Chennai (MOFA), "Korean Visa Application Guide" (For Indian Applicants,
  posted 2025-11-10): "Indian nationals must apply for Korean Visa and obtain it through the Visa Portal (www.visa.go.kr) &
  Visa Application Center (KVAC-VFS)" - fill/print the e-Form on the Visa Portal, submit at the Visa Application Center,
  check status on the Visa Portal.
- k-eta.go.kr (official): K-ETA is for nationals who can enter Korea without a visa; apply only on www.k-eta.go.kr or the
  K-ETA app; beware look-alike agency/phishing sites -> not a substitute for a visa for Indian passports.
- e-arrivalcard.go.kr (Ministry of Justice): Korea Electronic Arrival Card, online with no fee, can be filed from 3 days
  before arrival.
Document lists, fees, processing times and visa validity were NOT read on an official page -> not stated on the page.
Keyword Planner IN 18 Nov 2026: "south korea tour package" 2,900/mo (focus kw), "korea tour package" 1,000,
"south korea trip cost from india" 720, "korea tour package from india" 170, "south korea visa for indians" 9,900.
Photos: Wikimedia Commons (CC BY / CC BY-SA / Korea.net CC BY-SA 2.0 / PD US Army; licence + author read from each File: page
raw wikitext 18 Nov 2026), WP IDs 23437-23451; every uploaded WP copy viewed. Unused: 23442 (Seoul at night - too dark),
23448 (Jinhae cherry blossoms - low resolution, people on the track).
Climate/season wording is general guidance (no figures); no prices; no flight times.
"""
import json, html, sys, os
sys.path.insert(0, os.getcwd())
import gen_hub as G

PID = int(sys.argv[1]) if len(sys.argv) > 1 else 0
M = G.M
svg, WA_SVG, wa = G.svg, G.WA_SVG, G.wa
CHECKED = '18 November 2026'
SRC_CG = 'https://ind-chennai.mofa.go.kr/in-chennai-en/brd/m_2785/view.do?seq=750165'
SRC_VP = 'https://www.visa.go.kr/'
SRC_KETA = 'https://www.k-eta.go.kr/'
SRC_EAC = 'https://www.e-arrivalcard.go.kr/'

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
body.page-id-PID .page-header:before{content:"Holidays abroad \00B7  South Korea";display:inline-block;font:800 12px/1 "Plus Jakarta Sans",sans-serif;letter-spacing:.18em;text-transform:uppercase;color:#1a1606;background:#E2C158;padding:8px 13px;border-radius:999px;margin-bottom:16px}
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
HERO = ['south-korea-1', 'south-korea-2', 'south-korea-3', 'south-korea-4', 'south-korea-5', 'south-korea-6']
GAL = ['south-korea-7', 'south-korea-8', 'south-korea-9', 'south-korea-10', 'south-korea-11', 'south-korea-12', 'south-korea-13']
FINAL = 'south-korea-2'  # reuses hero slide 2 (Seongsan Ilchulbong, Jeju)

FAQ = [
    ("Do Indians need a visa for South Korea?", "Yes. Indian passport holders need a Korean visa before they travel. When we checked on 18 November 2026, the Consulate General of the Republic of Korea in Chennai stated that Indian nationals must apply for a Korean visa and obtain it through the official Korea Visa Portal (visa.go.kr) and the Korea Visa Application Centre (KVAC). Whether a visa is issued is always the decision of the Korean authorities, and admission is decided by Korean immigration on arrival."),
    ("How do I apply for a South Korea tourist visa from India?", "According to the Korean consulate's visa guide for Indian applicants, you fill in and print the visa e-Form on the Korea Visa Portal, submit your application in person at a Korea Visa Application Centre (KVAC), and then track its status on the Visa Portal. The exact documents for your visa type are listed by the Visa Portal and the application centre. We prepare your hotel confirmations, flight itinerary and a day-by-day plan so that your trip papers are consistent."),
    ("Can Indians use K-ETA instead of a visa?", "No. The official K-ETA website says the electronic travel authorisation is for nationals who can enter Korea without a visa. Indian nationals need a visa, so K-ETA does not replace it. Apply only on official government sites, and ignore look-alike websites that charge extra fees."),
    ("What is the Korea e-Arrival Card?", "It is Korea's online arrival card, run by the Ministry of Justice on the official site e-arrivalcard.go.kr. The official site says it can be filed online with no fee, from three days before you arrive in Korea. We remind you about it before you fly and tell you whether your airline also hands out a paper card."),
    ("How many days are enough for a South Korea trip?", "Six to eight nights is a comfortable first trip: four nights in Seoul with a day trip to Nami Island, then the KTX train to Busan for two or three nights with an optional day in Gyeongju. With nine or ten nights you can add Jeju Island for its volcanic coast and Hallasan."),
    ("Which is the best time to visit South Korea?", "Spring (about March to May) and autumn (about September to November) are the most pleasant. Cherry blossoms usually appear in late March and early April, and the autumn colours peak around October and early November. Summer is hot and humid with a rainy spell, and winter is cold with snow — good for ski resorts and snowy scenery such as Nami Island."),
    ("Is vegetarian and Indian food available in South Korea?", "Yes, especially in Seoul and Busan, where you will find Indian restaurants and vegetarian or vegan places; many Korean dishes contain meat, fish sauce or seafood, so it takes some planning outside the big cities. We note vegetarian and Jain needs with hotels in advance and suggest restaurants along your route."),
    ("Why are there no prices on this page?", "A South Korea trip cost depends on your dates, the cities you choose, hotel category, KTX or domestic flights, tours and the airfare from your city. Instead of a teaser price that changes when you ask, we send a costed, day-by-day quote for your dates — usually within 24 hours."),
]

JS = ("(function(){var f=document.getElementById('hxPlan');if(!f){return;}f.addEventListener('submit',function(e){e.preventDefault();"
      "var d=f.querySelector('[name=d]').value,s=f.querySelector('[name=s]').value,m=f.querySelector('[name=m]').value,a=f.querySelector('[name=a]').value,k=f.querySelector('[name=k]').value,c=f.querySelector('[name=c]').value;"
      "var t='Hi Suzu Travels, please send me a costed South Korea itinerary.\\nTrip: '+d+'\\nTrip type: '+s+'\\nTravel month: '+m+'\\nAdults: '+a+'\\nChildren: '+k;"
      "if(c){t=t+'\\nDeparting from: '+c;}"
      "window.open('https:'+String.fromCharCode(47,47)+'wa.me/917087488961?text='+encodeURIComponent(t),'_blank','noopener');});})();")

REL = [('japan-tour-packages', 'Japan', 'suzu-abroad-japan', 'Tokyo, Fuji, Kyoto, Osaka'), ('china-tour-packages', 'China', 'CN', 'Great Wall, Xi’an, Shanghai'),
       ('hong-kong-tour-packages', 'Hong Kong & Macau', 'HK', 'Harbour, Peak, Disneyland, Macau'), ('philippines-tour-packages', 'Philippines', 'PH', 'Palawan, Boracay, Bohol'),
       ('thailand-tour-packages', 'Thailand', 'suzu-card-thailand', 'Bangkok, Phuket, Krabi'), ('vietnam-tour-packages', 'Vietnam', 'suzu-card-vietnam', 'Hanoi, Ha Long, Hoi An'),
       ('singapore-tour-packages', 'Singapore', 'suzu-card-singapore', 'City, Sentosa, Universal'), ('malaysia-tour-packages', 'Malaysia', 'suzu-card-malaysia', 'KL, Langkawi, Genting'),
       ('bali-tour-packages', 'Bali', 'suzu-card-bali', 'Ubud, villas, temples'), ('maldives-tour-packages', 'Maldives', 'suzu-card-maldives', 'Overwater villas'),
       ('mauritius-tour-packages', 'Mauritius', 'suzu-abroad-mauritius', 'Lagoons, Le Morne, island tours'), ('sri-lanka-tour-packages', 'Sri Lanka', 'suzu-card-sri-lanka', 'Beaches & tea country'),
       ('australia-tour-packages', 'Australia & NZ', 'suzu-abroad-australia', 'Sydney, Melbourne, Queenstown'), ('new-zealand-tour-packages', 'New Zealand', 'NZ', 'Queenstown, Milford, Mount Cook'),
       ('dubai-tour-packages', 'Dubai', 'suzu-abroad-dubai', 'Burj Khalifa, desert, Abu Dhabi'), ('turkey-tour-packages', 'Turkey', 'suzu-abroad-turkey', 'Istanbul, Cappadocia, Pamukkale'),
       ('egypt-tour-packages', 'Egypt', 'suzu-abroad-egypt', 'Cairo, Nile cruise, Luxor'), ('europe-tour-packages', 'Europe', 'suzu-abroad-europe', 'Paris, Swiss Alps, Italy'),
       ('switzerland-tour-packages', 'Switzerland', 'suzu-abroad-switzerland', 'Lucerne, Jungfrau, Zermatt'), ('uk-tour-packages', 'UK', 'suzu-abroad-uk', 'London, Cotswolds, Scotland'),
       ('russia-tour-packages', 'Russia', 'RU', 'Moscow, Saint Petersburg'), ('georgia-tour-packages', 'Georgia', 'suzu-abroad-georgia', 'Tbilisi, Kazbegi, Gudauri'),
       ('azerbaijan-tour-packages', 'Azerbaijan', 'suzu-abroad-azerbaijan', 'Baku, Gabala, Shahdag'), ('armenia-tour-packages', 'Armenia', 'suzu-abroad-armenia', 'Yerevan, Garni, Sevan'),
       ('uzbekistan-tour-packages', 'Uzbekistan', 'suzu-abroad-uzbekistan', 'Samarkand, Bukhara, Khiva'), ('kazakhstan-tour-packages', 'Kazakhstan', 'suzu-abroad-kazakhstan', 'Almaty, lakes, Kyrgyzstan'),
       ('nepal-tour-packages', 'Nepal', 'suzu-card-nepal', 'No visa for Indians'), ('bhutan-tour-packages', 'Bhutan', 'suzu-card-bhutan', 'Paro, Thimphu, Punakha')]
SPECIAL_IMG = {'HK': 'https://suzutravels.com/wp-content/uploads/2026/11/hong-kong-victoria-harbour-night-from-the-peak-768x363.webp',
               'CN': 'https://suzutravels.com/wp-content/uploads/2026/11/china-great-wall-mutianyu-768x575.webp',
               'RU': 'https://suzutravels.com/wp-content/uploads/2026/11/russia-moscow-saint-basils-cathedral-red-square-768x512.webp',
               'NZ': 'https://suzutravels.com/wp-content/uploads/2026/11/new-zealand-milford-sound-mitre-peak-768x481.webp',
               'PH': 'https://suzutravels.com/wp-content/uploads/2026/11/philippines-el-nido-big-lagoon-palawan-768x512.webp'}

def build():
    W = "Hi Suzu Travels, I'm planning a South Korea trip. Please share a quote."
    h = [f'<div class="suzu-intl hx hx-country"><style>{CSS}</style>']
    slides = ''.join(f'<div class="hx-slide"><img src="{U(s)}" alt="{A(s)}" width="1600" height="1000" {"fetchpriority=\"high\" loading=\"eager\"" if i == 0 else "loading=\"lazy\""} decoding="async"><span class="hx-cap">{C(s)}</span></div>' for i, s in enumerate(HERO))
    h.append('<section class="hx-hero" aria-label="South Korea tour packages from India"><div class="hx-slides">' + slides + '</div><div class="hx-copy">'
             '<p class="hx-lede">Walk through the royal palaces and hanok lanes of Seoul, take the fast KTX train to Busan&rsquo;s beaches and painted hillside village, see the temples of Gyeongju and climb the volcanic crater of Seongsan Ilchulbong on Jeju. We plan South Korea to your dates, budget and pace — cherry blossom or autumn colour, honeymoon or family — with vegetarian meals noted in advance and honest guidance on the visa Indians need.</p>'
             '<div class="hx-badges">'
             f'<span class="hx-badge">{svg("globe")}Seoul, Busan &amp; Jeju</span><span class="hx-badge">{svg("doc")}Visa steps explained</span>'
             f'<span class="hx-badge">{svg("team")}Honeymoons, families &amp; groups</span><span class="hx-badge">{svg("food")}Vegetarian meals planned</span></div>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Get a South Korea Quote {svg("arrow")}</a>'
             f'<a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div></div>'
             '<form class="hx-plan" id="hxPlan" aria-label="Get a costed South Korea itinerary on WhatsApp"><h3>Plan my South Korea trip</h3>'
             '<p>Tell us the basics — we reply on WhatsApp with a costed, day-by-day plan, usually within 24 hours.</p><div class="hx-f">'
             '<label class="hx-full">Trip<select name="d"><option selected>Seoul + Busan (classic)</option><option>Seoul + Nami Island (short break)</option><option>Seoul + Busan + Jeju (9–10 nights)</option><option>Cherry blossom trip (spring)</option><option>Autumn colours trip</option><option>Korea + Japan</option><option>Not sure yet</option></select></label>'
             '<label>Trip type<select name="s"><option>Honeymoon / couple</option><option>Family</option><option>Friends</option><option>Seniors</option><option>Group</option><option>Corporate / MICE</option></select></label>'
             f'<label>Travel month<select name="m">{G.months()}</select></label>'
             '<label>Adults<select name="a"><option>1</option><option selected>2</option><option>3</option><option>4</option><option>5</option><option>6</option><option>7–10</option><option>11–20</option><option>20+</option></select></label>'
             '<label>Children<select name="k"><option>0</option><option>1</option><option>2</option><option>3</option><option>4+</option></select></label>'
             '<label class="hx-full">Departing from<input name="c" type="text" placeholder="e.g. Delhi, Mumbai, Chandigarh" autocomplete="address-level2"></label></div>'
             f'<button class="hx-btn" type="submit">{WA_SVG}Get my South Korea plan on WhatsApp</button><small>Opens WhatsApp with your details filled in. We do not store anything on this page.</small></form></section>')
    h.append('<div class="hx-trust">'
             f'<div>{svg("clock")}<span><b>Quote in ~24 hours</b><span>Costed, day by day</span></span></div>'
             f'<div>{svg("doc")}<span><b>Honest visa guidance</b><span>Official Korean sources, checked</span></span></div>'
             f'<div>{svg("shield")}<span><b>HP Tourism registered</b><span>Reg. DTO-MND-11-243/2022</span></span></div>'
             f'<div>{svg("chat")}<span><b>One team, start to finish</b><span>Reachable while you travel</span></span></div></div>')
    h.append('<nav class="hx-toc" aria-label="On this page"><a href="#why-south-korea">Why South Korea</a><a href="#south-korea-in-photos">Photos</a><a href="#how-to-choose">Choose your trip</a><a href="#sample-itinerary">Sample itinerary</a><a href="#when-to-go">When to go</a><a href="#visa-and-entry">Visa</a><a href="#whats-included">What\'s included</a><a href="#south-korea-faq">FAQ</a></nav>')
    facts = [('Getting there', 'Fly into Incheon (Seoul); we compare direct and connecting flights from your city'), ('Time difference', 'South Korea is 3 hours 30 minutes ahead of India'), ('Currency', 'South Korean won (KRW); cards are widely accepted in cities'),
             ('Best season', 'March to May and September to November'), ('Typical trip', '6 to 8 nights; 9 to 10 with Jeju'), ('Entry', 'Visa needed for Indians — apply before you travel')]
    h.append('<section id="why-south-korea" class="hx-sec"><span class="hx-eye">South Korea</span><h2>Why South Korea is worth it for Indian travellers</h2>'
             '<p class="hx-sub">Seoul packs royal palaces, hanok lanes, street-food markets and a skyline view from Namsan into one easy, safe city with excellent metro and trains. The KTX high-speed train links it to Busan&rsquo;s beaches and Gyeongju&rsquo;s temples, and Jeju Island adds volcanic coast and Hallasan. Spring blossom and autumn colour make it a strong pick for honeymoons and family trips alike.</p>'
             '<div class="hx-facts">' + ''.join(f'<div class="hx-fact"><b>{a}</b><span>{b}</span></div>' for a, b in facts) + '</div></section>')
    h.append('<section id="south-korea-in-photos" class="hx-sec"><span class="hx-eye">Real places</span><h2>South Korea in photos</h2>'
             '<p class="hx-sub">A trail on Hallasan in Jeju, Haeundae Beach in Busan, a pavilion at Changdeokgung Palace, pancakes at Gwangjang Market, N Seoul Tower at sunset, Nami Island in snow and the Cheonggyecheon stream in central Seoul. Real photos by Wikimedia Commons photographers, credited below.</p><div class="hx-pg">'
             + ''.join(f'<figure><img src="{U(k)}" alt="{A(k)}" width="800" height="600" loading="lazy" decoding="async"><figcaption>{C(k)}</figcaption></figure>' for k in GAL) + '</div></section>')
    cards = [('First-timers', 'Seoul &amp; Busan', 'Palaces, Bukchon and Namsan in Seoul, a day at Nami Island, then the KTX to Busan for Haeundae Beach and Gamcheon Culture Village.'),
             ('Honeymoon', 'Seoul &amp; Jeju', 'City days in Seoul followed by Jeju&rsquo;s volcanic coast, Seongsan Ilchulbong at sunrise and quiet seaside hotels.'),
             ('Families', 'Theme parks &amp; easy days', 'Seoul&rsquo;s theme parks and aquariums, short transfers, family rooms and a gentle pace, with Nami Island or Busan&rsquo;s beach.'),
             ('Seasons', 'Blossom, colour &amp; snow', 'Cherry blossoms in spring, autumn colours in Seoraksan and the palaces, or snow and ski resorts in winter.')]
    stays = [('Seoul — Myeongdong or Jongno', 'Central for the palaces, Bukchon, Insadong and Namsan, with easy metro links and plenty of restaurants.'),
             ('Seoul — Hongdae or Gangnam', 'Hongdae for a lively, younger feel; Gangnam for modern hotels, shopping and the COEX area.'),
             ('Busan — Haeundae or Seomyeon', 'Haeundae for the beach and sea-view hotels; Seomyeon for a central base near the main metro lines.'),
             ('Jeju — Jeju City or Seogwipo', 'Jeju City near the airport and markets; Seogwipo on the south coast for waterfalls and resort hotels.')]
    h.append('<section id="how-to-choose" class="hx-sec"><span class="hx-eye">How to choose</span><h2>Choose the South Korea trip that fits you</h2>'
             '<p class="hx-sub">Start from the kind of trip you want — we fine-tune the cities, hotels, trains, flights and tours to your group.</p><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><span class="hx-tag">{t}</span><h3>{n}</h3><p>{d}</p></div>' for t, n, d in cards) + '</div>'
             '<h3 style="margin-top:30px">Where to stay</h3><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><h3>{n}</h3><p>{d}</p></div>' for n, d in stays) + '</div></section>')
    days = [('Day 1', 'Arrive in Seoul', 'Airport transfer from Incheon to your hotel. Easy evening in Myeongdong for street food and shopping.'),
            ('Day 2', 'Palaces &amp; hanok lanes', 'Gyeongbokgung Palace, Bukchon Hanok Village and Insadong, with an evening walk along the Cheonggyecheon stream.'),
            ('Day 3', 'Nami Island', 'A day trip to Nami Island and its tree-lined avenues; back in Seoul for dinner.'),
            ('Day 4', 'Seoul your way', 'N Seoul Tower on Namsan, Gwangjang Market and a theme park, or an optional guided DMZ tour.'),
            ('Day 5', 'KTX to Busan', 'High-speed train to Busan. Afternoon at Gamcheon Culture Village and sunset at Haeundae Beach.'),
            ('Day 6', 'Busan coast', 'Haeundae, the coastal walks and markets of Busan, at an easy pace.'),
            ('Day 7', 'Gyeongju day trip', 'Bulguksa Temple and the old royal capital of Gyeongju, then back to Busan.'),
            ('Day 8', 'Fly home', 'Transfer to the airport and fly home, direct or via Seoul.')]
    h.append('<section id="sample-itinerary" class="hx-sec"><span class="hx-eye">Sample plan</span><h2>A sample 8-day South Korea itinerary</h2>'
             '<p class="hx-sub">The classic first trip. We rebuild it around you — add Jeju for three nights, swap Gyeongju for Seoraksan in autumn, or keep it to Seoul and Nami Island for a short break.</p><div class="hx-itin">'
             + ''.join(f'<div class="hx-day"><i>{a}</i><b>{b}</b><p>{c}</p></div>' for a, b, c in days) + '</div></section>')
    seasons = [('Mar – May', '<span class="hx-ok">Best</span>', 'Spring, mild', 'Cherry blossoms usually in late March and early April; pleasant days for city walks and Jeju.'),
               ('Jun – Aug', '<span class="hx-mid">Hot</span>', 'Hot, humid, rainy spell', 'Summer heat and a rainy spell; good for Busan&rsquo;s beaches and indoor sights, with flexible plans.'),
               ('Sep – Nov', '<span class="hx-ok">Best</span>', 'Autumn, cool and clear', 'Autumn colours around October and early November in Seoraksan, the palaces and Nami Island.'),
               ('Dec – Feb', '<span class="hx-mid">Cold</span>', 'Cold, snow', 'Winter cold with snow — ski resorts, snowy Nami Island and winter festivals; pack warm clothes.')]
    h.append('<section id="when-to-go" class="hx-sec"><span class="hx-eye">Best season</span><h2>When to go to South Korea</h2>'
             '<p class="hx-sub">South Korea has four clear seasons. Spring and autumn are the most comfortable; winter suits snow lovers. We check the season, holidays and flight prices against your plan before we quote.</p>'
             '<div class="hx-tw"><table class="hx-t"><thead><tr><th>Months</th><th>Verdict</th><th>Weather</th><th>What it means for your trip</th></tr></thead><tbody>'
             + ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in seasons) + '</tbody></table></div></section>')
    h.append('<section id="visa-and-entry" class="hx-sec"><span class="hx-eye">Visa &amp; entry</span><h2>South Korea visa for Indian passport holders</h2>'
             '<div class="hx-visa"><div class="hx-vbox"><h3>What the official sources say</h3><ul>'
             '<li><b>A visa is needed before you travel.</b> The Korean consulate&rsquo;s visa guide for Indian applicants states that Indian nationals must apply for a Korean visa and obtain it through the official <b>Korea Visa Portal</b> and a <b>Korea Visa Application Centre (KVAC)</b>.</li>'
             f'<li><b>How it works:</b> fill in and print the visa e-Form on the <a href="{SRC_VP}" target="_blank" rel="noopener nofollow">Korea Visa Portal (visa.go.kr)</a>, submit it in person at a Korea Visa Application Centre, then check the status of your application on the Visa Portal.</li>'
             '<li><b>Documents:</b> the exact list for your visa type is shown by the Visa Portal and the application centre. We prepare matching hotel confirmations, a flight itinerary and a day-by-day plan for your file.</li>'
             f'<li><b>K-ETA is not a visa.</b> The official <a href="{SRC_KETA}" target="_blank" rel="noopener nofollow">K-ETA site</a> says K-ETA is for nationals who can enter Korea without a visa, so it does not replace a visa for Indian passports. Use only official sites and ignore look-alike agencies.</li>'
             f'<li><b>e-Arrival Card:</b> Korea&rsquo;s Ministry of Justice runs the official <a href="{SRC_EAC}" target="_blank" rel="noopener nofollow">e-Arrival Card site</a>; it can be filed online with no fee, from three days before arrival.</li></ul>'
             f'<p class="hx-checked">Checked {CHECKED} · sources: <a href="{SRC_CG}" target="_blank" rel="noopener nofollow">Consulate General of the Republic of Korea in Chennai — Korean Visa Application Guide</a> · <a href="{SRC_VP}" target="_blank" rel="noopener nofollow">Korea Visa Portal</a> · <a href="{SRC_KETA}" target="_blank" rel="noopener nofollow">K-ETA (official)</a> · <a href="{SRC_EAC}" target="_blank" rel="noopener nofollow">Korea e-Arrival Card (official)</a></p></div>'
             '<div class="hx-vnote"><p><b>Please note:</b> whether a visa is issued is always the decision of the Korean authorities, and admission is decided by Korean immigration on arrival. We help you prepare a clear, consistent file, but we never promise an outcome we do not control.</p>'
             '<p>Apply well before your travel dates. We give you the hotel confirmations, flight itinerary and day-by-day plan in one set, and we confirm your bookings only in the way that suits your visa timeline.</p></div></div></section>')
    inc = [('doc', 'Visa paperwork', 'Hotel confirmations, flight itinerary and a day-by-day plan ready for your visa file, plus an e-Arrival Card reminder.'), ('pin', 'Hotels', 'Named hotels in Seoul, Busan and Jeju, chosen for your budget and trip style.'),
           ('team', 'Trains &amp; transfers', 'Airport transfers, KTX train tickets and domestic flights to Jeju that connect.'), ('globe', 'Tours', 'Nami Island, palace and city tours, the DMZ, Gyeongju and Jeju sightseeing, as you choose.'),
           ('food', 'Meal plan', 'Breakfast at most hotels; vegetarian and Jain needs noted in advance, with restaurant suggestions.'), ('award', 'Flights optional', 'Land-only, or a full package with international flights from your nearest Indian airport.')]
    h.append('<section id="whats-included" class="hx-sec"><span class="hx-eye">Your package</span><h2>What a Suzu South Korea package includes</h2><div class="hx-inc">'
             + ''.join(f'<div>{svg(i)}<span><b>{t}</b><span>{d}</span></span></div>' for i, t, d in inc) + '</div></section>')
    steps = [('chat', 'Tell us the basics', 'Dates, travellers and the kind of trip you want. A WhatsApp message is enough.'),
             ('doc', 'Get a costed itinerary', 'A day-by-day plan with named hotels and a clear per-person price, usually within 24 hours.'),
             ('sliders', 'Adjust until it fits', 'Change the cities, hotels, trains or add-ons. We re-quote as needed.'),
             ('lock', 'Confirm with a token', 'Lock your plan with a small token amount; the balance is paid later, as agreed in writing.')]
    h.append('<section id="how-booking-works" class="hx-sec"><span class="hx-eye">Simple process</span><h2>How booking works</h2><div class="hx-steps">'
             + ''.join(f'<div class="hx-step"><div class="hx-n">{svg(i)}</div><b>{t}</b><p>{d}</p></div>' for i, t, d in steps) + '</div></section>')
    h.append('<section id="south-korea-faq" class="hx-sec"><span class="hx-eye">FAQ</span><h2>Common questions about a South Korea tour</h2><div class="hx-faqs">'
             + ''.join(f'<details class="hx-faq"{" open" if k == 0 else ""}><summary>{html.escape(q)}</summary><div class="hx-ans"><p>{html.escape(a)}</p></div></details>' for k, (q, a) in enumerate(FAQ)) + '</div></section>')
    def _img(img): return SPECIAL_IMG[img] if img in SPECIAL_IMG else f'https://suzutravels.com/wp-content/uploads/2026/10/{img}.webp'
    h.append('<section id="more-destinations" class="hx-sec"><span class="hx-eye">Explore more</span><h2>Explore more destinations</h2>'
             '<p class="hx-sub">Every trip is planned the same way — your dates, your budget, one team from quote to return. <a href="https://suzutravels.com/international-tour-packages/">See all international holidays →</a></p><div class="hx-mini">'
             + ''.join(f'<a class="hx-mc" href="https://suzutravels.com/{p}/"><img src="{_img(img)}" alt="{html.escape(n)} holiday — Suzu Travels" width="640" height="360" loading="lazy" decoding="async"><span><b>{html.escape(n)}</b><em>{html.escape(e)}</em></span></a>' for p, n, img, e in REL) + '</div></section>')
    h.append(f'<div class="hx-final"><img src="{U(FINAL)}" alt="{A(FINAL)}" width="1600" height="900" loading="lazy" decoding="async">'
             '<h2>Plan your South Korea trip</h2><p>Send us your dates and group size. We will come back with a costed, day-by-day South Korea itinerary you can compare, no obligation.</p>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Request a South Korea Quote {svg("arrow")}</a><a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div>'
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
    open('pages/south-korea-tour-packages.html', 'w').write(o)
    print('pages/south-korea-tour-packages.html', len(o), len(o.encode()))
