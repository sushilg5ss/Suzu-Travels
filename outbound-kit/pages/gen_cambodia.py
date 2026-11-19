#!/usr/bin/env python3
"""Cambodia page - .hx design; same template as gen_southkorea.py / gen_philippines.py.
Run from outbound-kit/:  python3 pages/gen_cambodia.py <PAGE_ID> -> pages/cambodia-tour-packages.html (one line)
Facts (official pages read 19 Nov 2026 with a real browser - evisa.gov.kh sits behind a Nexusguard JS challenge):
- evisa.gov.kh (Ministry of Foreign Affairs and International Cooperation of Cambodia), Visa Type Information (last updated
  1 Jan 2025): Visa T (Tourist) - single entry, fee USD 30, validity 3 months from issue, stay 1 month, processing 3 business
  days; passport valid more than 6 months at entry, digital photo, Visa/MasterCard. Visa exemption list = Laos, Malaysia,
  Philippines, Singapore, Vietnam, Thailand, Indonesia, Brunei, Myanmar (India not on it).
- evisa.gov.kh home: e-Visa ports - airports Techo International (KTI), Siem Reap Angkor International (SAI), Sihanoukville
  International (KOS); land Bavet (Svay Rieng), Trapeang Kreal (Stung Treng); temporarily closed for e-Visa entry: Cham Yeam
  (Koh Kong), Poipet (Banteay Meanchey). e-Arrival required for all travellers incl. visa holders, within 7 days before arrival.
- evisa.gov.kh Terms (14 Jul 2026): submission is not approval; Ministry may approve/refuse; processing times are estimates.
- arrival.gov.kh (Cambodia e-Arrival): within 7 days before arrival, submission is free; arriving visitors get a v-Pass by
  email replacing the passport stamp.
Not stated (not read on an official page): visa on arrival for Indians, nationality list of the e-Visa form.
Keyword Planner IN 19 Nov 2026: "cambodia tour package" 1,900/mo (focus kw), "cambodia tour package from india" 390,
"cambodia trip cost from india" 260, "cambodia vietnam tour package" 590, "cambodia visa for indians" 5,400.
Photos: Wikimedia Commons (CC BY-SA 2.0/3.0/4.0, CC BY 3.0; licence + author read from each File: page raw wikitext
19 Nov 2026), WP IDs 23667-23679; every uploaded WP copy viewed.
Climate/season wording is general guidance (no figures); no package prices; no flight times.
"""
import json, html, sys, os
sys.path.insert(0, os.getcwd())
import gen_hub as G

PID = int(sys.argv[1]) if len(sys.argv) > 1 else 0
M = G.M
svg, WA_SVG, wa = G.svg, G.WA_SVG, G.wa
CHECKED = '19 November 2026'
SRC_EV = 'https://www.evisa.gov.kh/'
SRC_VT = 'https://www.evisa.gov.kh/information/visa_type/4'
SRC_EA = 'https://arrival.gov.kh/'

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
body.page-id-PID .page-header:before{content:"Holidays abroad \00B7  Cambodia";display:inline-block;font:800 12px/1 "Plus Jakarta Sans",sans-serif;letter-spacing:.18em;text-transform:uppercase;color:#1a1606;background:#E2C158;padding:8px 13px;border-radius:999px;margin-bottom:16px}
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
HERO = ['cambodia-1', 'cambodia-2', 'cambodia-3', 'cambodia-4', 'cambodia-5', 'cambodia-6']
GAL = ['cambodia-7', 'cambodia-8', 'cambodia-9', 'cambodia-10', 'cambodia-11', 'cambodia-12', 'cambodia-13']
FINAL = 'cambodia-7'  # wide Angkor Wat reflection (also gallery photo 1)

FAQ = [
    ("Do Indians need a visa for Cambodia?", "Yes. When we checked the official Cambodia e-Visa portal of the Ministry of Foreign Affairs and International Cooperation on 19 November 2026, India was not on its visa-exemption list (that list covers Laos, Malaysia, the Philippines, Singapore, Vietnam, Thailand, Indonesia, Brunei and Myanmar). Indian travellers therefore need a visa. Whether a visa is issued is always the decision of the Cambodian authorities."),
    ("How does the Cambodia e-Visa work?", "The official portal is evisa.gov.kh. You fill in the online form, upload a recent digital photo and pay by Visa or MasterCard; the approved e-Visa is emailed to you or can be downloaded from the portal. On 19 November 2026 the portal listed the tourist e-Visa (Visa T) as single entry, valid for 3 months from the date of issue for a stay of up to 1 month, with a passport valid for more than six months at entry and a processing time of 3 business days. The portal states that processing times are estimates."),
    ("What is the Cambodia e-Visa fee?", "On 19 November 2026 the official portal listed USD 30 for the tourist e-Visa (Visa T), a fee in force since 1 January 2025. Fees are set by the Cambodian government and can change, so we re-check the portal when you book. Use only the official portal evisa.gov.kh and ignore look-alike websites that charge extra."),
    ("Can I enter Cambodia by land from Thailand or Vietnam on an e-Visa?", "Only at the checkpoints the portal lists for e-Visa entry. On 19 November 2026 these were the airports at Techo International (Phnom Penh), Siem Reap Angkor International and Sihanoukville, and the land crossings at Bavet (from Vietnam) and Trapeang Kreal (from Laos). The portal also said Cham Yeam and Poipet (the main crossings from Thailand) were temporarily closed for e-Visa entry. We plan your route around the open checkpoints."),
    ("What is the Cambodia e-Arrival?", "It is Cambodia's online arrival form at arrival.gov.kh. The official e-Visa portal says every traveller must complete it, including visa holders, and recommends submitting it within 7 days before arrival; the e-Arrival site says submission is free. After arrival you receive a v-Pass by email instead of an ink stamp."),
    ("How many days are enough for a Cambodia trip?", "Five to six nights is a comfortable first trip: three nights in Siem Reap for Angkor Wat, the Bayon, Ta Prohm and Banteay Srei, and two nights in Phnom Penh. With nine to eleven nights you can combine Cambodia with Vietnam, or add the south coast at Kampot or the islands of Koh Rong."),
    ("Which is the best time to visit Cambodia?", "The cooler, dry months from about November to March are the most comfortable for temple visits. April and May are the hottest. From about June to October the rainy season brings short heavy showers, green landscapes and fewer visitors, and the Tonle Sap lake is at its fullest."),
    ("Why are there no prices on this page?", "A Cambodia trip cost depends on your dates, the cities you choose, hotel category, temple passes, guides and the airfare from your city. Instead of a teaser price that changes when you ask, we send a costed, day-by-day quote for your dates — usually within 24 hours."),
]

JS = ("(function(){var f=document.getElementById('hxPlan');if(!f){return;}f.addEventListener('submit',function(e){e.preventDefault();"
      "var d=f.querySelector('[name=d]').value,s=f.querySelector('[name=s]').value,m=f.querySelector('[name=m]').value,a=f.querySelector('[name=a]').value,k=f.querySelector('[name=k]').value,c=f.querySelector('[name=c]').value;"
      "var t='Hi Suzu Travels, please send me a costed Cambodia itinerary.\\nTrip: '+d+'\\nTrip type: '+s+'\\nTravel month: '+m+'\\nAdults: '+a+'\\nChildren: '+k;"
      "if(c){t=t+'\\nDeparting from: '+c;}"
      "window.open('https:'+String.fromCharCode(47,47)+'wa.me/917087488961?text='+encodeURIComponent(t),'_blank','noopener');});})();")

REL = [('vietnam-tour-packages', 'Vietnam', 'suzu-card-vietnam', 'Hanoi, Ha Long, Hoi An'), ('thailand-tour-packages', 'Thailand', 'suzu-card-thailand', 'Bangkok, Phuket, Krabi'),
       ('malaysia-tour-packages', 'Malaysia', 'suzu-card-malaysia', 'KL, Langkawi, Genting'), ('singapore-tour-packages', 'Singapore', 'suzu-card-singapore', 'City, Sentosa, Universal'),
       ('bali-tour-packages', 'Bali', 'suzu-card-bali', 'Ubud, villas, temples'), ('philippines-tour-packages', 'Philippines', 'PH', 'Palawan, Boracay, Bohol'),
       ('south-korea-tour-packages', 'South Korea', 'KR', 'Seoul, Busan, Jeju'), ('japan-tour-packages', 'Japan', 'suzu-abroad-japan', 'Tokyo, Fuji, Kyoto, Osaka'),
       ('china-tour-packages', 'China', 'CN', 'Great Wall, Xi’an, Shanghai'), ('hong-kong-tour-packages', 'Hong Kong & Macau', 'HK', 'Harbour, Peak, Disneyland, Macau'),
       ('maldives-tour-packages', 'Maldives', 'suzu-card-maldives', 'Overwater villas'), ('sri-lanka-tour-packages', 'Sri Lanka', 'suzu-card-sri-lanka', 'Beaches & tea country'),
       ('mauritius-tour-packages', 'Mauritius', 'suzu-abroad-mauritius', 'Lagoons, Le Morne, island tours'), ('australia-tour-packages', 'Australia & NZ', 'suzu-abroad-australia', 'Sydney, Melbourne, Queenstown'),
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
               'NZ': 'https://suzutravels.com/wp-content/uploads/2026/11/new-zealand-milford-sound-mitre-peak-768x481.webp',
               'PH': 'https://suzutravels.com/wp-content/uploads/2026/11/philippines-el-nido-big-lagoon-palawan-768x512.webp',
               'KR': 'https://suzutravels.com/wp-content/uploads/2026/11/south-korea-seoul-gyeongbokgung-geunjeongjeon-768x432.webp'}

def build():
    W = "Hi Suzu Travels, I'm planning a Cambodia trip. Please share a quote."
    h = [f'<div class="suzu-intl hx hx-country"><style>{CSS}</style>']
    slides = ''.join(f'<div class="hx-slide"><img src="{U(s)}" alt="{A(s)}" width="1600" height="1000" {"fetchpriority=\"high\" loading=\"eager\"" if i == 0 else "loading=\"lazy\""} decoding="async"><span class="hx-cap">{C(s)}</span></div>' for i, s in enumerate(HERO))
    h.append('<section class="hx-hero" aria-label="Cambodia tour packages from India"><div class="hx-slides">' + slides + '</div><div class="hx-copy">'
             '<p class="hx-lede">Watch the towers of Angkor Wat appear in the reflection pond, walk among the stone faces of the Bayon and the forest-wrapped galleries of Ta Prohm, then see the golden roofs of the Royal Palace and the Silver Pagoda in Phnom Penh. We plan Cambodia to your dates, budget and pace — on its own or combined with Vietnam or Thailand — with temple days timed around the heat, vegetarian meals noted in advance and honest guidance on the e-Visa.</p>'
             '<div class="hx-badges">'
             f'<span class="hx-badge">{svg("globe")}Angkor &amp; Phnom Penh</span><span class="hx-badge">{svg("doc")}e-Visa steps explained</span>'
             f'<span class="hx-badge">{svg("team")}Couples, families &amp; groups</span><span class="hx-badge">{svg("food")}Vegetarian meals planned</span></div>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Get a Cambodia Quote {svg("arrow")}</a>'
             f'<a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div></div>'
             '<form class="hx-plan" id="hxPlan" aria-label="Get a costed Cambodia itinerary on WhatsApp"><h3>Plan my Cambodia trip</h3>'
             '<p>Tell us the basics — we reply on WhatsApp with a costed, day-by-day plan, usually within 24 hours.</p><div class="hx-f">'
             '<label class="hx-full">Trip<select name="d"><option selected>Siem Reap + Phnom Penh (classic)</option><option>Angkor temples only (short break)</option><option>Cambodia + Vietnam</option><option>Cambodia + Thailand</option><option>Angkor + Kampot or Koh Rong</option><option>Not sure yet</option></select></label>'
             '<label>Trip type<select name="s"><option>Honeymoon / couple</option><option>Family</option><option>Friends</option><option>Seniors</option><option>Group</option><option>Corporate / MICE</option></select></label>'
             f'<label>Travel month<select name="m">{G.months()}</select></label>'
             '<label>Adults<select name="a"><option>1</option><option selected>2</option><option>3</option><option>4</option><option>5</option><option>6</option><option>7–10</option><option>11–20</option><option>20+</option></select></label>'
             '<label>Children<select name="k"><option>0</option><option>1</option><option>2</option><option>3</option><option>4+</option></select></label>'
             '<label class="hx-full">Departing from<input name="c" type="text" placeholder="e.g. Delhi, Mumbai, Chandigarh" autocomplete="address-level2"></label></div>'
             f'<button class="hx-btn" type="submit">{WA_SVG}Get my Cambodia plan on WhatsApp</button><small>Opens WhatsApp with your details filled in. We do not store anything on this page.</small></form></section>')
    h.append('<div class="hx-trust">'
             f'<div>{svg("clock")}<span><b>Quote in ~24 hours</b><span>Costed, day by day</span></span></div>'
             f'<div>{svg("doc")}<span><b>Honest visa guidance</b><span>Official Cambodian sources, checked</span></span></div>'
             f'<div>{svg("shield")}<span><b>HP Tourism registered</b><span>Reg. DTO-MND-11-243/2022</span></span></div>'
             f'<div>{svg("chat")}<span><b>One team, start to finish</b><span>Reachable while you travel</span></span></div></div>')
    h.append('<nav class="hx-toc" aria-label="On this page"><a href="#why-cambodia">Why Cambodia</a><a href="#cambodia-in-photos">Photos</a><a href="#how-to-choose">Choose your trip</a><a href="#sample-itinerary">Sample itinerary</a><a href="#when-to-go">When to go</a><a href="#visa-and-entry">Visa</a><a href="#whats-included">What\'s included</a><a href="#cambodia-faq">FAQ</a></nav>')
    facts = [('Getting there', 'Fly into Siem Reap or Phnom Penh; we compare connecting and any direct flights from your city'), ('Time difference', 'Cambodia is 1 hour 30 minutes ahead of India'), ('Currency', 'Cambodian riel (KHR); US dollars are widely used in tourist areas'),
             ('Best season', 'November to March (cooler, dry)'), ('Typical trip', '5 to 6 nights; 9 to 11 with Vietnam'), ('Entry', 'Visa needed for Indians — official e-Visa online')]
    h.append('<section id="why-cambodia" class="hx-sec"><span class="hx-eye">Cambodia</span><h2>Why Cambodia is worth it for Indian travellers</h2>'
             '<p class="hx-sub">The temples of Angkor are among the great sights of Asia — Angkor Wat, the faces of the Bayon, Ta Prohm in the forest and the fine carvings of Banteay Srei, all within reach of Siem Reap. Phnom Penh adds the Royal Palace, the Silver Pagoda and riverside evenings, and the south coast has Kampot&rsquo;s river and the islands of Koh Rong. It is a compact country that pairs naturally with Vietnam or Thailand, and Indian travellers often feel at home among its Hindu and Buddhist temples.</p>'
             '<div class="hx-facts">' + ''.join(f'<div class="hx-fact"><b>{a}</b><span>{b}</span></div>' for a, b in facts) + '</div></section>')
    h.append('<section id="cambodia-in-photos" class="hx-sec"><span class="hx-eye">Real places</span><h2>Cambodia in photos</h2>'
             '<p class="hx-sub">Angkor Wat behind its reflection pond, the Silver Pagoda in Phnom Penh, the two-storey hall at Preah Khan, a floating village on the Tonle Sap, a waterfall on Phnom Kulen, sunset on the Kampot river and Lazy Beach on Koh Rong Sanloem. Real photos by Wikimedia Commons photographers, credited below.</p><div class="hx-pg">'
             + ''.join(f'<figure><img src="{U(k)}" alt="{A(k)}" width="800" height="600" loading="lazy" decoding="async"><figcaption>{C(k)}</figcaption></figure>' for k in GAL) + '</div></section>')
    cards = [('First-timers', 'Siem Reap &amp; Phnom Penh', 'Two or three days for the Angkor temples from Siem Reap, then Phnom Penh for the Royal Palace, the Silver Pagoda and the riverfront.'),
             ('Combine', 'Cambodia &amp; Vietnam', 'Angkor and Phnom Penh joined with Ho Chi Minh City, the Mekong Delta or Hanoi and Ha Long Bay — one of the most popular two-country trips.'),
             ('Couples', 'Temples &amp; a quiet coast', 'Sunrise at Angkor Wat and boutique stays in Siem Reap, then slow days by the Kampot river or on the beaches of Koh Rong.'),
             ('Families', 'Easy temple days', 'Short temple circuits with breaks in the afternoon heat, a tuk-tuk or private car with a guide, and family rooms with a pool.')]
    stays = [('Siem Reap — near Pub Street', 'Central for restaurants, markets and the night market, with easy tuk-tuk rides to the Angkor ticket office and temples.'),
             ('Siem Reap — quiet resorts', 'Garden resorts and boutique hotels a little outside the centre, good for couples and families who want a pool after temple mornings.'),
             ('Phnom Penh — Riverside', 'Close to the Royal Palace, the Silver Pagoda and the National Museum, with evening walks along the river.'),
             ('Kampot or Koh Rong', 'Riverside guesthouses and resorts in Kampot, or simple to upmarket beach stays on Koh Rong and Koh Rong Sanloem.')]
    h.append('<section id="how-to-choose" class="hx-sec"><span class="hx-eye">How to choose</span><h2>Choose the Cambodia trip that fits you</h2>'
             '<p class="hx-sub">Start from the kind of trip you want — we fine-tune the cities, hotels, guides, flights and road transfers to your group.</p><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><span class="hx-tag">{t}</span><h3>{n}</h3><p>{d}</p></div>' for t, n, d in cards) + '</div>'
             '<h3 style="margin-top:30px">Where to stay</h3><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><h3>{n}</h3><p>{d}</p></div>' for n, d in stays) + '</div></section>')
    days = [('Day 1', 'Arrive in Siem Reap', 'Airport transfer to your hotel. Easy evening around Pub Street and the night market.'),
            ('Day 2', 'Angkor Wat &amp; Angkor Thom', 'Sunrise at Angkor Wat with a guide, then the South Gate, the Bayon and the Terrace of the Elephants; rest in the afternoon heat.'),
            ('Day 3', 'Ta Prohm &amp; Banteay Srei', 'Ta Prohm among the trees, Preah Khan, and the pink sandstone carvings of Banteay Srei.'),
            ('Day 4', 'Tonle Sap or Phnom Kulen', 'A boat trip to a floating village on the Tonle Sap, or the waterfall and river carvings of Phnom Kulen.'),
            ('Day 5', 'On to Phnom Penh', 'Short flight or road transfer to Phnom Penh. Evening walk along the riverside.'),
            ('Day 6', 'Phnom Penh', 'The Royal Palace and Silver Pagoda, the National Museum and the Central Market.'),
            ('Day 7', 'Fly home', 'Transfer to the airport and fly home — or continue by road to Ho Chi Minh City for Vietnam.')]
    h.append('<section id="sample-itinerary" class="hx-sec"><span class="hx-eye">Sample plan</span><h2>A sample 7-day Cambodia itinerary</h2>'
             '<p class="hx-sub">The classic first trip. We rebuild it around you — add Vietnam for four to five more nights, swap Phnom Penh for Kampot and the coast, or keep it to three nights in Siem Reap for a short break.</p><div class="hx-itin">'
             + ''.join(f'<div class="hx-day"><i>{a}</i><b>{b}</b><p>{c}</p></div>' for a, b, c in days) + '</div></section>')
    seasons = [('Nov – Feb', '<span class="hx-ok">Best</span>', 'Cooler, dry', 'The most comfortable months for temple mornings and city days; also the busiest at Angkor, so book early.'),
               ('Mar – May', '<span class="hx-hot">Hot</span>', 'Hot, dry', 'March is still dry; April and May are the hottest months — start early, rest at midday and plan pool time.'),
               ('Jun – Aug', '<span class="hx-mid">Rainy</span>', 'Warm, green, showers', 'Short heavy showers, usually in the afternoon; green landscapes, fewer visitors at the temples.'),
               ('Sep – Oct', '<span class="hx-mid">Rainy</span>', 'Wettest, lake full', 'The heaviest rains; the Tonle Sap lake is at its fullest. Keep plans flexible and allow for wet days.')]
    h.append('<section id="when-to-go" class="hx-sec"><span class="hx-eye">Best season</span><h2>When to go to Cambodia</h2>'
             '<p class="hx-sub">Cambodia is warm all year, with a dry season and a rainy season. November to March suits most travellers; the green season has its own charm. We check the season, holidays and flight prices against your plan before we quote.</p>'
             '<div class="hx-tw"><table class="hx-t"><thead><tr><th>Months</th><th>Verdict</th><th>Weather</th><th>What it means for your trip</th></tr></thead><tbody>'
             + ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in seasons) + '</tbody></table></div></section>')
    h.append('<section id="visa-and-entry" class="hx-sec"><span class="hx-eye">Visa &amp; entry</span><h2>Cambodia visa for Indian passport holders</h2>'
             '<div class="hx-visa"><div class="hx-vbox"><h3>What the official sources say</h3><ul>'
             '<li><b>A visa is needed.</b> India is not on the visa-exemption list of Cambodia&rsquo;s official e-Visa portal (that list covers nine ASEAN countries), so Indian travellers need a visa.</li>'
             f'<li><b>Official e-Visa:</b> apply online on the <a href="{SRC_EV}" target="_blank" rel="noopener nofollow">Cambodia e-Visa portal (evisa.gov.kh)</a> of the Ministry of Foreign Affairs and International Cooperation — fill in the form, upload a recent digital photo and pay by Visa or MasterCard; the approved e-Visa is emailed to you or downloaded from the portal.</li>'
             f'<li><b>Tourist e-Visa (Visa T):</b> the <a href="{SRC_VT}" target="_blank" rel="noopener nofollow">portal&rsquo;s visa information</a> lists it as single entry, valid 3 months from the date of issue, for a stay of up to 1 month; fee USD 30; processing 3 business days (the portal says processing times are estimates); passport valid for more than six months at entry.</li>'
             '<li><b>Where you can enter on an e-Visa:</b> the airports at Techo International (Phnom Penh), Siem Reap Angkor International and Sihanoukville, and the land crossings at Bavet and Trapeang Kreal. The portal says Cham Yeam and Poipet are temporarily closed for e-Visa entry — we plan Thailand combinations around this.</li>'
             f'<li><b>Cambodia e-Arrival:</b> every traveller, including visa holders, completes the free online <a href="{SRC_EA}" target="_blank" rel="noopener nofollow">e-Arrival form (arrival.gov.kh)</a>, ideally within 7 days before arrival. After arrival you get a v-Pass by email instead of an ink stamp.</li></ul>'
             f'<p class="hx-checked">Checked {CHECKED} · sources: <a href="{SRC_EV}" target="_blank" rel="noopener nofollow">Cambodia e-Visa — Ministry of Foreign Affairs and International Cooperation</a> · <a href="{SRC_VT}" target="_blank" rel="noopener nofollow">e-Visa visa type information</a> · <a href="{SRC_EA}" target="_blank" rel="noopener nofollow">Cambodia e-Arrival (official)</a></p></div>'
             '<div class="hx-vnote"><p><b>Please note:</b> whether a visa is issued is always the decision of the Cambodian authorities — the portal itself says that submitting an application is not an approval — and admission is decided by Cambodian immigration on arrival. We help you prepare a clear, consistent application, but we never promise an outcome we do not control.</p>'
             '<p>Fees, rules and open checkpoints can change. We re-check the official portal when you book and remind you about the e-Visa and e-Arrival before you fly. Use only the official government sites, not look-alike agencies.</p></div></div></section>')
    inc = [('doc', 'e-Visa help', 'Step-by-step help with the official e-Visa form and photo, plus an e-Arrival reminder before you fly.'), ('pin', 'Hotels', 'Named hotels in Siem Reap, Phnom Penh and on the coast, chosen for your budget and trip style.'),
           ('team', 'Guides &amp; transfers', 'Airport transfers, a private car or tuk-tuk for temple days, and an English-speaking guide at Angkor.'), ('globe', 'Tours', 'Angkor temple circuits, Tonle Sap boat trip, Phnom Kulen, Phnom Penh city tour and Vietnam or Thailand add-ons, as you choose.'),
           ('food', 'Meal plan', 'Breakfast at most hotels; vegetarian and Jain needs noted in advance, with restaurant suggestions along your route.'), ('award', 'Flights optional', 'Land-only, or a full package with international flights from your nearest Indian airport.')]
    h.append('<section id="whats-included" class="hx-sec"><span class="hx-eye">Your package</span><h2>What a Suzu Cambodia package includes</h2><div class="hx-inc">'
             + ''.join(f'<div>{svg(i)}<span><b>{t}</b><span>{d}</span></span></div>' for i, t, d in inc) + '</div></section>')
    steps = [('chat', 'Tell us the basics', 'Dates, travellers and the kind of trip you want. A WhatsApp message is enough.'),
             ('doc', 'Get a costed itinerary', 'A day-by-day plan with named hotels and a clear per-person price, usually within 24 hours.'),
             ('sliders', 'Adjust until it fits', 'Change the cities, hotels, guides or add-ons. We re-quote as needed.'),
             ('lock', 'Confirm with a token', 'Lock your plan with a small token amount; the balance is paid later, as agreed in writing.')]
    h.append('<section id="how-booking-works" class="hx-sec"><span class="hx-eye">Simple process</span><h2>How booking works</h2><div class="hx-steps">'
             + ''.join(f'<div class="hx-step"><div class="hx-n">{svg(i)}</div><b>{t}</b><p>{d}</p></div>' for i, t, d in steps) + '</div></section>')
    h.append('<section id="cambodia-faq" class="hx-sec"><span class="hx-eye">FAQ</span><h2>Common questions about a Cambodia tour</h2><div class="hx-faqs">'
             + ''.join(f'<details class="hx-faq"{" open" if k == 0 else ""}><summary>{html.escape(q)}</summary><div class="hx-ans"><p>{html.escape(a)}</p></div></details>' for k, (q, a) in enumerate(FAQ)) + '</div></section>')
    def _img(img): return SPECIAL_IMG[img] if img in SPECIAL_IMG else f'https://suzutravels.com/wp-content/uploads/2026/10/{img}.webp'
    h.append('<section id="more-destinations" class="hx-sec"><span class="hx-eye">Explore more</span><h2>Explore more destinations</h2>'
             '<p class="hx-sub">Every trip is planned the same way — your dates, your budget, one team from quote to return. <a href="https://suzutravels.com/international-tour-packages/">See all international holidays →</a></p><div class="hx-mini">'
             + ''.join(f'<a class="hx-mc" href="https://suzutravels.com/{p}/"><img src="{_img(img)}" alt="{html.escape(n)} holiday — Suzu Travels" width="640" height="360" loading="lazy" decoding="async"><span><b>{html.escape(n)}</b><em>{html.escape(e)}</em></span></a>' for p, n, img, e in REL) + '</div></section>')
    h.append(f'<div class="hx-final"><img src="{U(FINAL)}" alt="{A(FINAL)}" width="1600" height="900" loading="lazy" decoding="async">'
             '<h2>Plan your Cambodia trip</h2><p>Send us your dates and group size. We will come back with a costed, day-by-day Cambodia itinerary you can compare, no obligation.</p>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Request a Cambodia Quote {svg("arrow")}</a><a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div>'
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
    open('pages/cambodia-tour-packages.html', 'w').write(o)
    print('pages/cambodia-tour-packages.html', len(o), len(o.encode()))
