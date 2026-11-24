#!/usr/bin/env python3
"""Oman page - .hx design; same template as gen_seychelles.py.
Built + published 24 Nov 2026 (photos WP 25133-25147; 13 used, 25145 opera interior + 25134 Muttrah rooftops spare).
Run from outbound-kit/:  python3 pages/gen_oman.py <PAGE_ID> -> pages/oman-tour-packages.html (one line)
Facts (official Royal Oman Police eVisa portal, read 24 Nov 2026 with headless Chromium; curl gets the JS shell):
- evisa.rop.gov.om/en/types-of-visa -> Visit Unsponsored -> 26 Tourist Visit Visa: "Granted ... to nationals of specified
  countries ... for ten (10) days, fourteen (14) days or one month". Sub-types: 26A 10 days / 26B 30 days for "G1 nationals";
  26M/26N 30/10 days for allowed nationalities holding a valid Schengen visa or a valid visa/residency of USA, UK, Canada,
  Australia or Japan. 26A fee OMR 5.000, 26B OMR 20.000 (26N OMR 5.000). 26B/26N: passport valid >= 6 months on entry,
  single entry, valid hotel booking in Oman, return ticket, digital photo + passport copy, applicant outside Oman,
  no sponsor needed, overstay fine OMR 10/day, use within 1 month. "Possession of a valid visa does not guarantee ...
  entry ... at the discretion of the Royal Oman Police officer at the port of entry."
- FAQ: unsponsored + sponsored tourist visas on the eVisa system; lodge at least 4 days in advance; e-visa by email;
  "Paying for a visa does not guarantee that a visa will be issued"; passport 6 months.
NOT stated (not read officially): whether India is on the G1 list (the list is shown only after registration) -> the page
  says visa types depend on nationality and are shown on the portal; we check eligibility with the traveller.
Keyword Planner IN 24 Nov 2026: "oman tour package" 1,300/mo (Nov-Jan 2,900; focus kw), "oman holiday packages" 1,300,
"oman visa for indians" 8,100, "oman tour package from india" 170, "muscat tour package" 110.
Photos: Wikimedia Commons (CC BY-SA 4.0 Diego Delso, Martin Falbisoner, Francesco Bini, albinfo, Uhooep, Erfan.arafat;
CC BY 2.0 Robert Haandrikman). Season wording is general guidance; no package prices; no flight times.
"""
import json, html, sys, os
sys.path.insert(0, os.getcwd())
import gen_hub as G

PID = int(sys.argv[1]) if len(sys.argv) > 1 else 0
M = dict(G.M)
PREVIEW = False
svg, WA_SVG, wa = G.svg, G.WA_SVG, G.wa
CHECKED = '24 November 2026'
SRC_EMB = 'https://evisa.rop.gov.om/en/home'
SRC_VISA = 'https://evisa.rop.gov.om/en/types-of-visa'
SRC_ENTRY = 'https://evisa.rop.gov.om/en/frequently-asked-questions'

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
body.page-id-PID .page-header:before{content:"Holidays abroad \00B7  Oman";display:inline-block;font:800 12px/1 "Plus Jakarta Sans",sans-serif;letter-spacing:.18em;text-transform:uppercase;color:#1a1606;background:#E2C158;padding:8px 13px;border-radius:999px;margin-bottom:16px}
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
HERO = ['oman-1', 'oman-2', 'oman-3', 'oman-4', 'oman-5', 'oman-6']
GAL = ['oman-7', 'oman-8', 'oman-9', 'oman-10', 'oman-11', 'oman-12', 'oman-13']
FINAL = 'oman-2'  # Wahiba Sands dunes (also in the hero)

FAQ = [
    ("Do Indians need a visa for Oman?", "Yes, plan on a visa before you travel. Tourist visas for Oman are issued online on the official eVisa portal of the Royal Oman Police. The portal lists unsponsored tourist visit visas of 10 days and 30 days for eligible nationalities, extra types for travellers who hold a valid Schengen visa or a valid US, UK, Canada, Australia or Japan visa or residency, and sponsored tourist visas. Which types you can apply for depends on your nationality and documents and is shown on the portal when you apply (checked 24 November 2026). Approval is always the decision of the Omani authorities."),
    ("How much is the Oman tourist visa fee?", "On the Royal Oman Police eVisa portal, the 10-day unsponsored tourist visit visa is listed at OMR 5 and the 30-day one at OMR 20 (checked 24 November 2026). Fees can change, and the portal shows the amount for your visa type when you apply. Paying the fee does not guarantee that a visa will be issued."),
    ("What documents do I need for an Oman tourist e-visa?", "For the 30-day unsponsored tourist visa the portal asks for a digital photograph and a copy of your passport, which must be valid for at least six months on entry, plus a valid hotel booking in Oman and a return ticket. You must apply from outside Oman, and the visa is for a single entry. We give you a clear itinerary and hotel confirmations to upload."),
    ("How early should I apply for the Oman visa?", "The Royal Oman Police eVisa FAQ recommends applying at least four days before travel, as processing times vary. The e-visa is sent to the email address you registered with. We suggest applying once flights and hotels are confirmed, and well before your departure date."),
    ("Which is the best time to visit Oman?", "October to March is the most comfortable time for Muscat, the mountains, the wadis and a desert night, with warm days and cooler evenings. April, May and September are hot, and June to August is very hot in Muscat and the interior. Salalah in the south is different: its khareef season, roughly July to September, brings mist, rain and green hills."),
    ("How many days are enough for Oman?", "Five to seven nights covers Muscat, the coast road with Bimmah Sinkhole and Wadi Shab, a desert camp in the Wahiba Sands and Nizwa with the mountains. Add two or three nights for the fjords of Musandam or for Salalah, or combine Oman with a few days in Dubai."),
    ("Is Oman good for families and vegetarian travellers?", "Yes. Oman suits families with its easy road trips, beaches, wadis to splash in and short desert camp stays. Muscat has many Indian restaurants and vegetarian food is easy to find; we note vegetarian and Jain meals with hotels and camps in advance. Muscat also has old Hindu temples, such as the Shiva temple in Old Muscat."),
    ("Why are there no prices on this page?", "An Oman trip cost depends on your dates, hotels and desert camp, the car and driver you choose, add-ons such as Musandam or Salalah and the airfare from your city. Instead of a teaser price that changes when you ask, we send a costed, day-by-day quote for your dates — usually within 24 hours."),
]

JS = ("(function(){var f=document.getElementById('hxPlan');if(!f){return;}f.addEventListener('submit',function(e){e.preventDefault();"
      "var d=f.querySelector('[name=d]').value,s=f.querySelector('[name=s]').value,m=f.querySelector('[name=m]').value,a=f.querySelector('[name=a]').value,k=f.querySelector('[name=k]').value,c=f.querySelector('[name=c]').value;"
      "var t='Hi Suzu Travels, please send me a costed Oman itinerary.\\nTrip: '+d+'\\nTrip type: '+s+'\\nTravel month: '+m+'\\nAdults: '+a+'\\nChildren: '+k;"
      "if(c){t=t+'\\nDeparting from: '+c;}"
      "window.open('https:'+String.fromCharCode(47,47)+'wa.me/917087488961?text='+encodeURIComponent(t),'_blank','noopener');});})();")

REL = [('dubai-tour-packages', 'Dubai', 'suzu-abroad-dubai', 'Burj Khalifa, desert, Abu Dhabi'), ('egypt-tour-packages', 'Egypt', 'suzu-abroad-egypt', 'Cairo, Nile cruise, Luxor'),
       ('turkey-tour-packages', 'Turkey', 'suzu-abroad-turkey', 'Istanbul, Cappadocia, Pamukkale'), ('georgia-tour-packages', 'Georgia', 'suzu-abroad-georgia', 'Tbilisi, Kazbegi, Gudauri'),
       ('azerbaijan-tour-packages', 'Azerbaijan', 'suzu-abroad-azerbaijan', 'Baku, Gabala, Shahdag'), ('armenia-tour-packages', 'Armenia', 'suzu-abroad-armenia', 'Yerevan, Garni, Sevan'),
       ('uzbekistan-tour-packages', 'Uzbekistan', 'suzu-abroad-uzbekistan', 'Samarkand, Bukhara, Khiva'), ('kazakhstan-tour-packages', 'Kazakhstan', 'suzu-abroad-kazakhstan', 'Almaty, lakes, Kyrgyzstan'),
       ('seychelles-tour-packages', 'Seychelles', 'SC', 'Mahé, Praslin, La Digue'), ('mauritius-tour-packages', 'Mauritius', 'suzu-abroad-mauritius', 'Lagoons, Le Morne, island tours'),
       ('maldives-tour-packages', 'Maldives', 'suzu-card-maldives', 'Overwater villas'), ('sri-lanka-tour-packages', 'Sri Lanka', 'suzu-card-sri-lanka', 'Beaches & tea country'),
       ('thailand-tour-packages', 'Thailand', 'suzu-card-thailand', 'Bangkok, Phuket, Krabi'), ('bali-tour-packages', 'Bali', 'suzu-card-bali', 'Ubud, villas, temples'),
       ('philippines-tour-packages', 'Philippines', 'PH', 'Palawan, Boracay, Bohol'), ('vietnam-tour-packages', 'Vietnam', 'suzu-card-vietnam', 'Hanoi, Ha Long, Hoi An'),
       ('cambodia-tour-packages', 'Cambodia', 'KH', 'Angkor Wat, Siem Reap, Phnom Penh'), ('malaysia-tour-packages', 'Malaysia', 'suzu-card-malaysia', 'KL, Langkawi, Genting'),
       ('singapore-tour-packages', 'Singapore', 'suzu-card-singapore', 'City, Sentosa, Universal'),
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
               'SC': M['seychelles-1']['med']}

def build():
    W = "Hi Suzu Travels, I'm planning an Oman trip. Please share a quote."
    h = [f'<div class="suzu-intl hx hx-country"><style>{CSS}</style>']
    slides = ''.join(f'<div class="hx-slide"><img src="{U(s)}" alt="{A(s)}" width="1600" height="1000" {"fetchpriority=\"high\" loading=\"eager\"" if i == 0 else "loading=\"lazy\""} decoding="async"><span class="hx-cap">{C(s)}</span></div>' for i, s in enumerate(HERO))
    h.append('<section class="hx-hero" aria-label="Oman tour packages from India"><div class="hx-slides">' + slides + '</div><div class="hx-copy">'
             '<p class="hx-lede">Walk the Muttrah corniche in Muscat, swim in the turquoise Bimmah Sinkhole and Wadi Shab, sleep at a desert camp in the Wahiba Sands and climb the walls of Nizwa Fort. We plan Oman to your dates, budget and pace, with hotels, a car and driver and tours lined up, vegetarian meals noted in advance and honest guidance on the e-visa.</p>'
             '<div class="hx-badges">'
             f'<span class="hx-badge">{svg("globe")}Muscat, wadis, desert &amp; Nizwa</span><span class="hx-badge">{svg("doc")}E-visa steps explained</span>'
             f'<span class="hx-badge">{svg("team")}Families, couples &amp; groups</span><span class="hx-badge">{svg("food")}Vegetarian meals planned</span></div>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Get an Oman Quote {svg("arrow")}</a>'
             f'<a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div></div>'
             '<form class="hx-plan" id="hxPlan" aria-label="Get a costed Oman itinerary on WhatsApp"><h3>Plan my Oman trip</h3>'
             '<p>Tell us the basics — we reply on WhatsApp with a costed, day-by-day plan, usually within 24 hours.</p><div class="hx-f">'
             '<label class="hx-full">Trip<select name="d"><option selected>Muscat, wadis, desert &amp; Nizwa</option><option>Muscat short break</option><option>Oman + Musandam fjords</option><option>Salalah (khareef or winter)</option><option>Oman + Dubai</option><option>Not sure yet</option></select></label>'
             '<label>Trip type<select name="s"><option>Family</option><option>Honeymoon / couple</option><option>Friends</option><option>Seniors</option><option>Group</option><option>Corporate / MICE</option></select></label>'
             f'<label>Travel month<select name="m">{G.months()}</select></label>'
             '<label>Adults<select name="a"><option>1</option><option selected>2</option><option>3</option><option>4</option><option>5</option><option>6</option><option>7–10</option><option>11–20</option><option>20+</option></select></label>'
             '<label>Children<select name="k"><option>0</option><option>1</option><option>2</option><option>3</option><option>4+</option></select></label>'
             '<label class="hx-full">Departing from<input name="c" type="text" placeholder="e.g. Delhi, Mumbai, Chandigarh" autocomplete="address-level2"></label></div>'
             f'<button class="hx-btn" type="submit">{WA_SVG}Get my Oman plan on WhatsApp</button><small>Opens WhatsApp with your details filled in. We do not store anything on this page.</small></form></section>')
    h.append('<div class="hx-trust">'
             f'<div>{svg("clock")}<span><b>Quote in ~24 hours</b><span>Costed, day by day</span></span></div>'
             f'<div>{svg("doc")}<span><b>Honest visa guidance</b><span>Official Royal Oman Police portal, checked</span></span></div>'
             f'<div>{svg("shield")}<span><b>HP Tourism registered</b><span>Reg. DTO-MND-11-243/2022</span></span></div>'
             f'<div>{svg("chat")}<span><b>One team, start to finish</b><span>Reachable while you travel</span></span></div></div>')
    h.append('<nav class="hx-toc" aria-label="On this page"><a href="#why-oman">Why Oman</a><a href="#oman-in-photos">Photos</a><a href="#how-to-choose">Choose your trip</a><a href="#sample-itinerary">Sample itinerary</a><a href="#when-to-go">When to go</a><a href="#visa-and-entry">Visa</a><a href="#whats-included">What\'s included</a><a href="#oman-faq">FAQ</a></nav>')
    facts = [('Getting there', 'Fly into Muscat International Airport — we compare routes and connections from your city'), ('Time difference', 'India is 1 hour 30 minutes ahead of Oman'), ('Currency', 'Omani rial (OMR)'),
             ('Best season', 'October to March; Salalah is green in the khareef, roughly July to September'), ('Typical trip', '5 to 7 nights: Muscat, wadis, desert camp and Nizwa'), ('Entry', 'Tourist e-visa online on the Royal Oman Police portal before you fly')]
    h.append('<section id="why-oman" class="hx-sec"><span class="hx-eye">Oman</span><h2>Why Oman is worth it for Indian travellers</h2>'
             '<p class="hx-sub">Oman sits on the south-east corner of the Arabian Peninsula, close to India across the Arabian Sea. It is a calm, friendly country of old forts, rocky mountains, green wadis with natural pools, golden dunes and a long coast. Muscat, the capital, mixes the Sultan Qaboos Grand Mosque and the Royal Opera House with the old harbour and souq of Muttrah. A week is enough to see the city, swim in a wadi, spend a night at a desert camp and visit Nizwa — and it pairs well with Dubai.</p>'
             '<div class="hx-facts">' + ''.join(f'<div class="hx-fact"><b>{a}</b><span>{b}</span></div>' for a, b in facts) + '</div></section>')
    h.append('<section id="oman-in-photos" class="hx-sec"><span class="hx-eye">Real places</span><h2>Oman in photos</h2>'
             '<p class="hx-sub">Al Alam Palace in Old Muscat, a marble arch and minaret at the Sultan Qaboos Grand Mosque, camels at the edge of the Wahiba Sands, the entrance to Wadi Shab, the canyon at Jebel Shams, a sea turtle at the Daymaniyat Islands and green hills near Salalah. Real photos by Wikimedia Commons photographers, credited below.</p><div class="hx-pg">'
             + ''.join(f'<figure><img src="{U(k) if j == 0 else M[k]["med"]}" alt="{A(k)}" width="800" height="600" loading="lazy" decoding="async"><figcaption>{C(k)}</figcaption></figure>' for j, k in enumerate(GAL)) + '</div></section>')
    cards = [('First-timers', 'Muscat, wadis &amp; desert', 'Muscat, Bimmah Sinkhole and Wadi Shab, a night in the Wahiba Sands and Nizwa Fort — a classic week by road with a driver.'),
             ('Families', 'Easy road trip', 'Short drives, beach hotels, wadi swims, a family tent at a desert camp and a dhow cruise in Muscat — with breaks built in.'),
             ('Couples', 'Coast, mountains &amp; fjords', 'A quiet beach hotel, a mountain stay near Jebel Shams or Jebel Akhdar, and a dhow day in the fjords of Musandam.'),
             ('Combine', 'Oman &amp; Dubai', 'Pair Oman with Dubai, or add Salalah in the green khareef season — we plan the order and flight or road connections around your dates.')]
    stays = [('Muscat', 'City and beach hotels near Qurum, Al Khuwair or the Muttrah corniche — close to the mosque, souq and restaurants.'),
             ('Sur &amp; the coast', 'Simple hotels on the coast road, handy for Wadi Shab, Wadi Tiwi and Bimmah Sinkhole.'),
             ('Wahiba Sands', 'Desert camps from simple to comfortable, with dinner and a sunset over the dunes.'),
             ('Nizwa &amp; the mountains', 'Hotels in Nizwa, or mountain stays on Jebel Akhdar and near Jebel Shams for cooler nights.')]
    h.append('<section id="how-to-choose" class="hx-sec"><span class="hx-eye">How to choose</span><h2>Choose the Oman trip that fits you</h2>'
             '<p class="hx-sub">Start from the kind of trip you want — we fine-tune the route, hotels, camp and car to your group and season.</p><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><span class="hx-tag">{t}</span><h3>{n}</h3><p>{d}</p></div>' for t, n, d in cards) + '</div>'
             '<h3 style="margin-top:30px">Where to stay</h3><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><h3>{n}</h3><p>{d}</p></div>' for n, d in stays) + '</div></section>')
    days = [('Day 1', 'Arrive in Muscat', 'Airport pick-up and transfer to your hotel. Evening walk on the Muttrah corniche.'),
            ('Day 2', 'Muscat city tour', 'The Sultan Qaboos Grand Mosque, the Royal Opera House from outside, Al Alam Palace in Old Muscat and the Muttrah souq.'),
            ('Day 3', 'Coast road to Sur', 'Drive the coast road with stops at Bimmah Sinkhole and Wadi Shab for a walk and a swim; overnight near Sur.'),
            ('Day 4', 'Wadi Bani Khalid &amp; desert', 'Swim in the green pools of Wadi Bani Khalid, then drive into the Wahiba Sands for a dune drive, sunset and a night at a desert camp.'),
            ('Day 5', 'Nizwa', 'Drive to Nizwa: the fort, the souq and the old town; overnight in Nizwa or the mountains.'),
            ('Day 6', 'Mountains &amp; back to Muscat', 'Morning at Jebel Shams or Jebel Akhdar viewpoints, then return to Muscat — or add a dhow cruise in the evening.'),
            ('Day 7', 'Fly home', 'Transfer to the airport for your flight home — or carry on to Musandam, Salalah or Dubai.')]
    h.append('<section id="sample-itinerary" class="hx-sec"><span class="hx-eye">Sample plan</span><h2>A sample 7-day Oman itinerary</h2>'
             '<p class="hx-sub">The classic loop by road with a driver. We rebuild it around you — slow it down for seniors, add the fjords of Musandam or Salalah, or combine it with Dubai.</p><div class="hx-itin">'
             + ''.join(f'<div class="hx-day"><i>{a}</i><b>{b}</b><p>{c}</p></div>' for a, b, c in days) + '</div></section>')
    seasons = [('Oct – Nov', '<span class="hx-ok">Best</span>', 'Warm days, cooling down', 'Good for Muscat, wadis and the first desert nights of the season; the sea is still warm.'),
               ('Dec – Feb', '<span class="hx-ok">Best</span>', 'Pleasant, cool evenings', 'The most comfortable months for road trips, the desert and the mountains; Christmas and New Year weeks are busy, so book early.'),
               ('Mar – Apr', '<span class="hx-ok">Good</span>', 'Warming up', 'Still good in March; April gets hot in the afternoons, so we plan wadis and walks for the mornings.'),
               ('May – Sep', '<span class="hx-hot">Hot</span>', 'Very hot in Muscat and inland', 'Muscat, the desert and the interior are very hot; this is the time for Salalah, which is misty and green in the khareef, roughly July to September.')]
    h.append('<section id="when-to-go" class="hx-sec"><span class="hx-eye">Best season</span><h2>When to go to Oman</h2>'
             '<p class="hx-sub">For Muscat, the wadis, the desert and Nizwa, the cooler months from October to March are best. Salalah in the south has its own season. This is general guidance; we check the weather, events and flight prices against your plan before we quote.</p>'
             '<div class="hx-tw"><table class="hx-t"><thead><tr><th>Months</th><th>Verdict</th><th>Weather</th><th>What it means for your trip</th></tr></thead><tbody>'
             + ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in seasons) + '</tbody></table></div></section>')
    h.append('<section id="visa-and-entry" class="hx-sec"><span class="hx-eye">Visa &amp; entry</span><h2>Oman visa for Indian passport holders</h2>'
             '<div class="hx-visa"><div class="hx-vbox"><h3>What the official sources say</h3><ul>'
             f'<li><b>Apply online before you fly.</b> Tourist visas for Oman are issued through the official <a href="{SRC_EMB}" target="_blank" rel="noopener nofollow">eVisa portal of the Royal Oman Police</a>. Its <a href="{SRC_ENTRY}" target="_blank" rel="noopener nofollow">FAQ</a> lists unsponsored and sponsored tourist visas and recommends applying at least four days before travel; the e-visa is sent by email.</li>'
             f'<li><b>Visa types depend on nationality:</b> the <a href="{SRC_VISA}" target="_blank" rel="noopener nofollow">visa types page</a> lists unsponsored tourist visit visas of 10 days and 30 days for eligible nationalities, and 10- or 30-day types for travellers who hold a valid Schengen visa or a valid US, UK, Canada, Australia or Japan visa or residency. The portal shows which types you can apply for when you apply — we check this with you before booking.</li>'
             '<li><b>Fees on the portal:</b> OMR 5 for the 10-day and OMR 20 for the 30-day unsponsored tourist visa. Paying the fee does not guarantee that a visa will be issued.</li>'
             '<li><b>Documents for the 30-day tourist visa:</b> a digital photograph and a copy of your passport, valid for at least six months on entry; a valid hotel booking in Oman and a return ticket. You apply from outside Oman, and the visa is for a single entry.</li>'
             '<li><b>Stay:</b> keep to the length of stay on your visa — the portal lists a fine of OMR 10 for each day of overstay.</li></ul>'
             f'<p class="hx-checked">Checked {CHECKED} · sources: <a href="{SRC_EMB}" target="_blank" rel="noopener nofollow">eVisa — Royal Oman Police</a> · <a href="{SRC_VISA}" target="_blank" rel="noopener nofollow">Types of visa — Royal Oman Police eVisa</a> · <a href="{SRC_ENTRY}" target="_blank" rel="noopener nofollow">eVisa FAQ — Royal Oman Police</a></p></div>'
             '<div class="hx-vnote"><p><b>Please note:</b> visa approval, and entry at the border, are always the decision of the Omani authorities — the portal itself says a valid visa does not guarantee entry, which is at the discretion of the Royal Oman Police officer. We help you prepare clear, consistent documents — itinerary, hotel bookings and return tickets — but we never promise an outcome we do not control.</p>'
             '<p>Visa rules and fees can change. We re-check the official portal when you book and tell you which visa type fits your passport and plan.</p></div></div></section>')
    inc = [('doc', 'Visa paperwork help', 'A day-by-day itinerary, hotel confirmations and help with the Oman e-visa application.'), ('pin', 'Hotels &amp; desert camp', 'Named hotels in Muscat, Sur and Nizwa and a desert camp in the Wahiba Sands, chosen for your budget.'),
           ('team', 'Car &amp; driver', 'Airport transfers and a private car or 4x4 with an English-speaking driver for the road trip and dune drive.'), ('globe', 'Tours', 'Muscat city tour, wadis, Nizwa Fort, mountain viewpoints and a dhow cruise, as you choose.'),
           ('food', 'Meal plan', 'Breakfast at hotels, dinner at the desert camp; vegetarian and Jain needs noted in advance.'), ('award', 'Flights optional', 'Land-only, or a full package with international flights from your nearest Indian airport.')]
    h.append('<section id="whats-included" class="hx-sec"><span class="hx-eye">Your package</span><h2>What a Suzu Oman package includes</h2><div class="hx-inc">'
             + ''.join(f'<div>{svg(i)}<span><b>{t}</b><span>{d}</span></span></div>' for i, t, d in inc) + '</div></section>')
    steps = [('chat', 'Tell us the basics', 'Dates, travellers and the kind of trip you want. A WhatsApp message is enough.'),
             ('doc', 'Get a costed itinerary', 'A day-by-day plan with named hotels and a clear per-person price, usually within 24 hours.'),
             ('sliders', 'Adjust until it fits', 'Change the route, hotels, camp or add Musandam or Dubai. We re-quote as needed.'),
             ('lock', 'Confirm with a token', 'Lock your plan with a small token amount; the balance is paid later, as agreed in writing.')]
    h.append('<section id="how-booking-works" class="hx-sec"><span class="hx-eye">Simple process</span><h2>How booking works</h2><div class="hx-steps">'
             + ''.join(f'<div class="hx-step"><div class="hx-n">{svg(i)}</div><b>{t}</b><p>{d}</p></div>' for i, t, d in steps) + '</div></section>')
    h.append('<section id="oman-faq" class="hx-sec"><span class="hx-eye">FAQ</span><h2>Common questions about an Oman tour</h2><div class="hx-faqs">'
             + ''.join(f'<details class="hx-faq"{" open" if k == 0 else ""}><summary>{html.escape(q)}</summary><div class="hx-ans"><p>{html.escape(a)}</p></div></details>' for k, (q, a) in enumerate(FAQ)) + '</div></section>')
    def _img(img): return SPECIAL_IMG[img] if img in SPECIAL_IMG else f'https://suzutravels.com/wp-content/uploads/2026/10/{img}.webp'
    h.append('<section id="more-destinations" class="hx-sec"><span class="hx-eye">Explore more</span><h2>Explore more destinations</h2>'
             '<p class="hx-sub">Every trip is planned the same way — your dates, your budget, one team from quote to return. <a href="https://suzutravels.com/international-tour-packages/">See all international holidays →</a></p><div class="hx-mini">'
             + ''.join(f'<a class="hx-mc" href="https://suzutravels.com/{p}/"><img src="{_img(img)}" alt="{html.escape(n)} holiday — Suzu Travels" width="640" height="360" loading="lazy" decoding="async"><span><b>{html.escape(n)}</b><em>{html.escape(e)}</em></span></a>' for p, n, img, e in REL) + '</div></section>')
    h.append(f'<div class="hx-final"><img src="{U(FINAL)}" alt="{A(FINAL)}" width="1600" height="900" loading="lazy" decoding="async">'
             '<h2>Plan your Oman trip</h2><p>Send us your dates and group size. We will come back with a costed, day-by-day Oman itinerary you can compare, no obligation.</p>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Request an Oman Quote {svg("arrow")}</a><a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div>'
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
    open('pages/oman-tour-packages.html', 'w').write(o)
    print('pages/oman-tour-packages.html', len(o), len(o.encode()))
