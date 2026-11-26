#!/usr/bin/env python3
"""Tanzania page - .hx design; same template as gen_kenya.py.
Built + published 26 Nov 2026 (photos WP 25747-25760; 13 used, 25760 dhow off Nungwi spare - portrait, people in the water).
Run from outbound-kit/:  python3 pages/gen_tanzania.py <PAGE_ID> -> pages/tanzania-tour-packages.html (one line)
Facts (Tanzania Immigration Services Department, Ministry of Home Affairs; read 26 Nov 2026 with headless Chromium + curl):
- immigration.go.tz/tourist-info: tourists from countries that need a visa apply for an Ordinary Visa (USD 50, non-refundable);
  two methods - online visa or visa on arrival, online "highly recommended"; online applications "may be processed within
  ten days"; one visa covers Tanzania mainland and Zanzibar; yellow fever requirements per Ministry of Health guidelines;
  visitors to Zanzibar must also obtain a mandatory health insurance.
- immigration.go.tz/service-fee (Visa tab): Ordinary Visa 50 USD; Multiple entry 100 USD; Transit 30 USD.
- Tanzania Visa Guidelines PDF (Quick Menu "Visa"): Commonwealth nationals visa-free EXCEPT UK, Canada, India, Pakistan,
  Australia, NZ -> Indians need a visa; India is on the list of nationals eligible for both online and on-arrival visa;
  passport valid >= 6 months with at least one unused visa page; return ticket shown on arrival; every passport holder incl.
  minors needs a separate application; apply only via the official website; Ordinary Visa validity up to 90 days;
  requirements: passport bio page copy, return ticket, online form, fee; Visa Grant Notice "is not a final authority to enter".
Keyword Planner IN 26 Nov 2026: "tanzania tour package" 590/mo (focus kw; Feb peak 720), "zanzibar tour package" 480 (Feb 1,600,
Mar 1,000), "tanzania visa for indians" 2,400 (Jul-Oct 2,900), "tanzania tour package from india" 170, "serengeti safari
package" 170 (Jul-Aug 320). South Africa lower: 390 / 260 / 260.
Photos: Wikimedia Commons CC BY-SA 4.0 (Giles Laurent, Diego Delso, Charles J Sharp, ObonyoML) + CC0 (Paul W, spare).
Ikiwaner Serengeti elephant / Ngorongoro rhino skipped (GFDL-only). Season wording is general guidance; no prices; no flight times.
"""
import json, html, sys, os
sys.path.insert(0, os.getcwd())
import gen_hub as G

PID = int(sys.argv[1]) if len(sys.argv) > 1 else 0
M = dict(G.M)
PREVIEW = False
svg, WA_SVG, wa = G.svg, G.WA_SVG, G.wa
CHECKED = '26 November 2026'
SRC_EMB = 'https://www.immigration.go.tz/tourist-info'
SRC_VISA = 'https://www.immigration.go.tz/service-fee'
SRC_ENTRY = 'https://www.immigration.go.tz/websiteportal/uploads/information_links/info_link_20260910_084204_a50ed70947.pdf'
SRC_GEN = 'https://www.immigration.go.tz/'

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
body.page-id-PID .page-header:before{content:"Holidays abroad \00B7  Tanzania";display:inline-block;font:800 12px/1 "Plus Jakarta Sans",sans-serif;letter-spacing:.18em;text-transform:uppercase;color:#1a1606;background:#E2C158;padding:8px 13px;border-radius:999px;margin-bottom:16px}
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
HERO = ['tanzania-1', 'tanzania-2', 'tanzania-3', 'tanzania-4', 'tanzania-5', 'tanzania-6']
GAL = ['tanzania-7', 'tanzania-8', 'tanzania-9', 'tanzania-10', 'tanzania-12', 'tanzania-13', 'tanzania-11']
FINAL = 'tanzania-11'  # Serengeti sunrise (also last in the gallery)

FAQ = [
    ("Do Indians need a visa for Tanzania?", "Yes. Tanzania's official visa guidelines list India among the Commonwealth countries whose nationals need a visa, and India is on the list of countries eligible for both the online visa and the visa on arrival. For a holiday you apply for an Ordinary Visa. The Immigration Services Department strongly recommends applying online before you travel for quicker clearance at the airport (checked 26 November 2026). The Visa Grant Notice is not a final authority to enter — the immigration officer at the point of entry decides."),
    ("How much is the Tanzania tourist visa fee?", "The official Immigration Services Department lists the Ordinary Visa at USD 50, non-refundable, with a validity of up to 90 days (checked 26 November 2026). Every passport holder, including children, needs their own application. Fees can change, and the portal shows the amount when you apply."),
    ("What documents do I need for the Tanzania e-visa?", "The official guidelines ask for a passport valid for at least six months with at least one unused visa page, a copy of the passport's photo page, a recent colour photo, a return ticket, the online application form and the visa fee. You must show your return ticket on arrival. We give you a day-by-day itinerary and lodge confirmations so your paperwork is clear and consistent."),
    ("How long does the Tanzania visa take?", "The official tourist information page says online applications may be processed within ten days. Apply only on the official Tanzania Immigration Services website, not through other links, and wait for the approval notice by email before you start your journey."),
    ("Is one visa enough for Zanzibar too?", "Yes. The Immigration Services Department says one Tanzania visa is enough to visit both the mainland and Zanzibar — you enter your first point of entry on the form. Visitors to Zanzibar must also have a mandatory health insurance, which we include in your planning checklist."),
    ("When is the best time for a Serengeti safari?", "The long dry season, roughly late June to October, is the classic time for game drives, and in the northern Serengeti the wildebeest herds often cross the Mara River from about July to September. From about December to March the herds are usually on the southern plains, where the calving season is in January and February. The herds follow the rain, so the timing changes every year. April and May bring the long rains."),
    ("How many days are enough for Tanzania?", "Six to eight nights covers the northern safari circuit from Arusha — Tarangire, the Ngorongoro Crater and two or three nights in the Serengeti. Add three or four nights on Zanzibar for Stone Town and the beaches, or combine Tanzania with a Kenya safari."),
    ("Why are there no prices on this page?", "A Tanzania safari cost depends on your dates, the season, the lodges or tented camps, park and crater fees, the vehicle, whether you drive or fly between the parks, Zanzibar nights and the airfare from your city. Instead of a teaser price that changes when you ask, we send a costed, day-by-day quote for your dates — usually within 24 hours."),
]

JS = ("(function(){var f=document.getElementById('hxPlan');if(!f){return;}f.addEventListener('submit',function(e){e.preventDefault();"
      "var d=f.querySelector('[name=d]').value,s=f.querySelector('[name=s]').value,m=f.querySelector('[name=m]').value,a=f.querySelector('[name=a]').value,k=f.querySelector('[name=k]').value,c=f.querySelector('[name=c]').value;"
      "var t='Hi Suzu Travels, please send me a costed Tanzania itinerary.\\nTrip: '+d+'\\nTrip type: '+s+'\\nTravel month: '+m+'\\nAdults: '+a+'\\nChildren: '+k;"
      "if(c){t=t+'\\nDeparting from: '+c;}"
      "window.open('https:'+String.fromCharCode(47,47)+'wa.me/917087488961?text='+encodeURIComponent(t),'_blank','noopener');});})();")

REL = [('kenya-tour-packages', 'Kenya', 'KE', 'Masai Mara, Amboseli, lakes'), ('seychelles-tour-packages', 'Seychelles', 'SC', 'Mahé, Praslin, La Digue'), ('mauritius-tour-packages', 'Mauritius', 'suzu-abroad-mauritius', 'Lagoons, Le Morne, island tours'),
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
               'SC': M['seychelles-1']['med'], 'OM': M['oman']['med'],
               'KE': 'https://suzutravels.com/wp-content/uploads/2026/11/kenya-masai-mara-giraffes-768x511.webp'}


def build():
    W = "Hi Suzu Travels, I'm planning a Tanzania safari. Please share a quote."
    h = [f'<div class="suzu-intl hx hx-country"><style>{CSS}</style>']
    slides = ''.join(f'<div class="hx-slide"><img src="{U(s)}" alt="{A(s)}" width="1600" height="1000" {"fetchpriority=\"high\" loading=\"eager\"" if i == 0 else "loading=\"lazy\""} decoding="async"><span class="hx-cap">{C(s)}</span></div>' for i, s in enumerate(HERO))
    h.append('<section class="hx-hero" aria-label="Tanzania tour packages from India"><div class="hx-slides">' + slides + '</div><div class="hx-copy">'
             '<p class="hx-lede">Follow lions, cheetahs and the great wildebeest herds across the Serengeti, drive down into the Ngorongoro Crater, see elephants under the baobabs of Tarangire, catch Mount Kilimanjaro above the clouds and finish on the white sand of Zanzibar. We plan your Tanzania safari to your dates, budget and pace, with lodges or tented camps, a safari vehicle and driver-guide, vegetarian meals noted in advance and honest guidance on the visa.</p>'
             '<div class="hx-badges">'
             f'<span class="hx-badge">{svg("globe")}Serengeti, Ngorongoro &amp; Tarangire</span><span class="hx-badge">{svg("doc")}Visa steps explained</span>'
             f'<span class="hx-badge">{svg("team")}Families, couples &amp; groups</span><span class="hx-badge">{svg("food")}Vegetarian meals planned</span></div>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Get a Tanzania Quote {svg("arrow")}</a>'
             f'<a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div></div>'
             '<form class="hx-plan" id="hxPlan" aria-label="Get a costed Tanzania itinerary on WhatsApp"><h3>Plan my Tanzania safari</h3>'
             '<p>Tell us the basics — we reply on WhatsApp with a costed, day-by-day plan, usually within 24 hours.</p><div class="hx-f">'
             '<label class="hx-full">Trip<select name="d"><option selected>Serengeti, Ngorongoro &amp; Tarangire</option><option>Safari + Zanzibar beach</option><option>Zanzibar only</option><option>Migration season safari</option><option>Tanzania + Kenya</option><option>Not sure yet</option></select></label>'
             '<label>Trip type<select name="s"><option>Family</option><option>Honeymoon / couple</option><option>Friends</option><option>Seniors</option><option>Group</option><option>Corporate / MICE</option></select></label>'
             f'<label>Travel month<select name="m">{G.months()}</select></label>'
             '<label>Adults<select name="a"><option>1</option><option selected>2</option><option>3</option><option>4</option><option>5</option><option>6</option><option>7–10</option><option>11–20</option><option>20+</option></select></label>'
             '<label>Children<select name="k"><option>0</option><option>1</option><option>2</option><option>3</option><option>4+</option></select></label>'
             '<label class="hx-full">Departing from<input name="c" type="text" placeholder="e.g. Delhi, Mumbai, Chandigarh" autocomplete="address-level2"></label></div>'
             f'<button class="hx-btn" type="submit">{WA_SVG}Get my Tanzania plan on WhatsApp</button><small>Opens WhatsApp with your details filled in. We do not store anything on this page.</small></form></section>')
    h.append('<div class="hx-trust">'
             f'<div>{svg("clock")}<span><b>Quote in ~24 hours</b><span>Costed, day by day</span></span></div>'
             f'<div>{svg("doc")}<span><b>Honest visa guidance</b><span>Official Tanzania Immigration pages, checked</span></span></div>'
             f'<div>{svg("shield")}<span><b>HP Tourism registered</b><span>Reg. DTO-MND-11-243/2022</span></span></div>'
             f'<div>{svg("chat")}<span><b>One team, start to finish</b><span>Reachable while you travel</span></span></div></div>')
    h.append('<nav class="hx-toc" aria-label="On this page"><a href="#why-tanzania">Why Tanzania</a><a href="#tanzania-in-photos">Photos</a><a href="#how-to-choose">Choose your trip</a><a href="#sample-itinerary">Sample itinerary</a><a href="#when-to-go">When to go</a><a href="#visa-and-entry">Visa</a><a href="#whats-included">What\'s included</a><a href="#tanzania-faq">FAQ</a></nav>')
    facts = [('Getting there', 'Fly into Kilimanjaro (for Arusha and the parks), Dar es Salaam or Zanzibar — we compare routes from your city'), ('Time difference', 'India is 2 hours 30 minutes ahead of Tanzania'), ('Currency', 'Tanzanian shilling (TZS)'),
             ('Best season', 'Late June to October for game drives; December to March for the southern Serengeti calving season'), ('Typical trip', '6 to 8 nights on safari; add 3 to 4 nights on Zanzibar'), ('Entry', 'Visa for Indian passports — online e-visa recommended; one visa covers Zanzibar')]
    h.append('<section id="why-tanzania" class="hx-sec"><span class="hx-eye">Tanzania</span><h2>Why Tanzania is worth it for Indian travellers</h2>'
             '<p class="hx-sub">Tanzania, on the east coast of Africa across the Indian Ocean from India, has some of the most famous safari country on earth. The Serengeti is home to big cats and the great migration of wildebeest and zebra, the Ngorongoro Crater holds a whole world of wildlife inside an old volcano, and Tarangire is known for its elephants and giant baobab trees. Mount Kilimanjaro, Africa\'s highest mountain, rises above the north, and the island of Zanzibar adds the old lanes of Stone Town and white beaches for slow days after the safari.</p>'
             '<div class="hx-facts">' + ''.join(f'<div class="hx-fact"><b>{a}</b><span>{b}</span></div>' for a, b in facts) + '</div></section>')
    h.append('<section id="tanzania-in-photos" class="hx-sec"><span class="hx-eye">Real places</span><h2>Tanzania in photos</h2>'
             '<p class="hx-sub">Wildebeest crossing the Mara River in the Serengeti, a cheetah, an elephant in Tarangire, the green Ngorongoro highlands, Forodhani Park on the Stone Town seafront, the sea at Nungwi on Zanzibar and sunrise over the Serengeti plains. Real photos by Wikimedia Commons photographers, credited below.</p><div class="hx-pg">'
             + ''.join(f'<figure><img src="{U(k) if j == 0 else M[k]["med"]}" alt="{A(k)}" width="800" height="600" loading="lazy" decoding="async"><figcaption>{C(k)}</figcaption></figure>' for j, k in enumerate(GAL)) + '</div></section>')
    cards = [('First-timers', 'The northern circuit', 'Elephants and baobabs in Tarangire, a day inside the Ngorongoro Crater and two or three nights of game drives in the Serengeti.'),
             ('Families', 'Easy-paced safari', 'Lodges with pools, shorter game drives with breaks, and the option of short flights between the parks instead of long drives.'),
             ('Couples', 'Safari &amp; Zanzibar', 'A tented camp in the Serengeti, an optional sunrise balloon flight, then Stone Town and a beach resort on Zanzibar.'),
             ('Migration', 'Calving or river crossings', 'December to March for the calving on the southern plains, or about July to September for the Mara River crossings in the north. Camps fill early.')]
    stays = [('Arusha', 'Hotels and coffee-farm lodges for the first and last night — the gateway to the northern parks and close to Kilimanjaro airport.'),
             ('Tarangire &amp; Karatu', 'Lodges near Tarangire, and in the green highlands of Karatu on the way to the Ngorongoro Crater.'),
             ('Serengeti', 'Lodges and tented camps in the central, northern or southern Serengeti, chosen for where the herds are in your month.'),
             ('Zanzibar', 'Boutique stays in Stone Town, and beach resorts on the north or east coast, such as Nungwi.')]
    h.append('<section id="how-to-choose" class="hx-sec"><span class="hx-eye">How to choose</span><h2>Choose the Tanzania trip that fits you</h2>'
             '<p class="hx-sub">Start from the kind of trip you want — we fine-tune the route, lodges, vehicle and pace to your group and season.</p><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><span class="hx-tag">{t}</span><h3>{n}</h3><p>{d}</p></div>' for t, n, d in cards) + '</div>'
             '<h3 style="margin-top:30px">Where to stay</h3><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><h3>{n}</h3><p>{d}</p></div>' for n, d in stays) + '</div></section>')
    days = [('Day 1', 'Arrive in Arusha', 'Airport pick-up at Kilimanjaro and transfer to your hotel in Arusha. On a clear day you may see Mount Kilimanjaro or Mount Meru.'),
            ('Day 2', 'Tarangire', 'Game drive in Tarangire National Park among the baobabs, known for its big elephant herds, then on to Karatu.'),
            ('Day 3', 'Into the Serengeti', 'Drive through the Ngorongoro highlands into the Serengeti, with a game drive on the way to your lodge or tented camp.'),
            ('Day 4', 'Serengeti full day', 'Morning and afternoon game drives for lions, cheetahs, leopards and the herds. Optional sunrise balloon flight.'),
            ('Day 5', 'Serengeti', 'Another day following the wildlife — your guide goes where the animals are in that season.'),
            ('Day 6', 'Ngorongoro Crater', 'Drive down onto the crater floor for a game drive among buffalo, zebras, wildebeest and lions, then overnight in Karatu.'),
            ('Day 7', 'Fly to Zanzibar', 'Short flight to Zanzibar and a walk through the lanes of Stone Town and Forodhani Gardens at sunset.'),
            ('Day 8', 'Beach or fly home', 'Fly home — or move to a beach resort such as Nungwi for three or four more nights on Zanzibar.')]
    h.append('<section id="sample-itinerary" class="hx-sec"><span class="hx-eye">Sample plan</span><h2>A sample 8-day Tanzania safari &amp; Zanzibar itinerary</h2>'
             '<p class="hx-sub">The classic northern safari with a driver-guide, finishing on Zanzibar. We rebuild it around you — fly between the parks to save time, add more Serengeti nights in the migration season, or combine it with Kenya.</p><div class="hx-itin">'
             + ''.join(f'<div class="hx-day"><i>{a}</i><b>{b}</b><p>{c}</p></div>' for a, b, c in days) + '</div></section>')
    seasons = [('Jan – Feb', '<span class="hx-ok">Good</span>', 'Warm, shorter dry spell', 'The calving season on the southern Serengeti plains; good game viewing and a fine time for Zanzibar.'),
               ('Mar – May', '<span class="hx-mid">Rainy</span>', 'The long rains', 'Green, quieter parks; April and May are the wettest months, some camps close and Zanzibar is often rainy — we choose routes with care.'),
               ('Jun – Oct', '<span class="hx-ok">Best</span>', 'Dry season, cool mornings', 'The classic safari season; the herds are usually in the north from about July, with Mara River crossings. Busiest — book well ahead.'),
               ('Nov – Dec', '<span class="hx-mid">Short rains</span>', 'Short showers', 'Short rains, often in the afternoons; the herds move south again. Good value before the busy holiday weeks in late December.')]
    h.append('<section id="when-to-go" class="hx-sec"><span class="hx-eye">Best season</span><h2>When to go to Tanzania</h2>'
             '<p class="hx-sub">Tanzania has wildlife to see all year. The dry months are easiest for game drives, and the great migration follows the rains around the Serengeti, so its timing changes a little each year. This is general guidance; we check the season, camp availability and flight prices against your plan before we quote.</p>'
             '<div class="hx-tw"><table class="hx-t"><thead><tr><th>Months</th><th>Verdict</th><th>Weather</th><th>What it means for your trip</th></tr></thead><tbody>'
             + ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in seasons) + '</tbody></table></div></section>')
    h.append('<section id="visa-and-entry" class="hx-sec"><span class="hx-eye">Visa &amp; entry</span><h2>Tanzania visa for Indian passport holders</h2>'
             '<div class="hx-visa"><div class="hx-vbox"><h3>What the official sources say</h3><ul>'
             f'<li><b>A visa is needed.</b> The official <a href="{SRC_ENTRY}" target="_blank" rel="noopener nofollow">Tanzania Visa Guidelines</a> of the Immigration Services Department list India among the Commonwealth countries whose nationals need a visa. For a holiday you apply for an <b>Ordinary Visa</b>.</li>'
             f'<li><b>Online or on arrival:</b> India is on the list of countries eligible for both the online visa and the visa on arrival. The <a href="{SRC_EMB}" target="_blank" rel="noopener nofollow">official tourist information page</a> highly recommends applying online for quicker clearance at the airport — apply only through the official Tanzania Immigration website.</li>'
             f'<li><b>Fee:</b> the <a href="{SRC_VISA}" target="_blank" rel="noopener nofollow">official fee table</a> lists the Ordinary Visa at USD 50, non-refundable; the guidelines give it a validity of up to 90 days. Every passport holder, including children, needs a separate application.</li>'
             '<li><b>Documents:</b> a passport valid for at least six months with at least one unused visa page, a copy of the passport photo page, a colour photo, a return ticket, the online form and the fee. You must show your return ticket on arrival.</li>'
             '<li><b>Timing and Zanzibar:</b> online applications may be processed within ten days. One visa covers both the mainland and Zanzibar; visitors to Zanzibar must also have a mandatory health insurance.</li></ul>'
             f'<p class="hx-checked">Checked {CHECKED} · sources: <a href="{SRC_EMB}" target="_blank" rel="noopener nofollow">Tourist info — Tanzania Immigration</a> · <a href="{SRC_VISA}" target="_blank" rel="noopener nofollow">Service fees — Tanzania Immigration</a> · <a href="{SRC_ENTRY}" target="_blank" rel="noopener nofollow">Tanzania Visa Guidelines (PDF)</a></p></div>'
             '<div class="hx-vnote"><p><b>Please note:</b> visa approval, and entry at the border, are always the decision of the Tanzanian authorities — the official guidelines say a Visa Grant Notice is not a final authority to enter, and the immigration officer at the point of entry may refuse entry. We help you prepare clear, consistent documents — itinerary, lodge bookings and return tickets — but we never promise an outcome we do not control.</p>'
             '<p>Rules and fees can change. We re-check the official pages when you book. The Immigration Department also asks visitors to follow the Ministry of Health yellow fever guidelines — please ask your doctor about vaccinations and malaria precautions, and check the current health rules for your return to India, before you travel.</p></div></div></section>')
    inc = [('doc', 'Visa paperwork help', 'A day-by-day itinerary, lodge confirmations and help with the Tanzania e-visa and the Zanzibar insurance for each traveller.'), ('pin', 'Lodges &amp; camps', 'Named hotels, safari lodges and tented camps in Arusha, Tarangire, Karatu, the Serengeti and on Zanzibar, chosen for your budget.'),
           ('team', 'Safari vehicle &amp; guide', 'Airport transfers and a safari vehicle with a pop-up roof and an English-speaking driver-guide — or light-aircraft flights between parks.'), ('globe', 'Game drives &amp; park fees', 'Game drives, national park and Ngorongoro Crater fees, itemised in your quote; balloon flight as an option.'),
           ('food', 'Meal plan', 'Usually all meals at safari lodges and camps; vegetarian and Jain needs noted in advance at every stay.'), ('award', 'Flights optional', 'Land-only, or a full package with international flights from your nearest Indian airport.')]
    h.append('<section id="whats-included" class="hx-sec"><span class="hx-eye">Your package</span><h2>What a Suzu Tanzania package includes</h2><div class="hx-inc">'
             + ''.join(f'<div>{svg(i)}<span><b>{t}</b><span>{d}</span></span></div>' for i, t, d in inc) + '</div></section>')
    steps = [('chat', 'Tell us the basics', 'Dates, travellers and the kind of safari you want. A WhatsApp message is enough.'),
             ('doc', 'Get a costed itinerary', 'A day-by-day plan with named lodges and a clear per-person price, usually within 24 hours.'),
             ('sliders', 'Adjust until it fits', 'Change the parks, lodges or vehicle, fly between parks or add Zanzibar. We re-quote as needed.'),
             ('lock', 'Confirm with a token', 'Lock your plan with a small token amount; the balance is paid later, as agreed in writing.')]
    h.append('<section id="how-booking-works" class="hx-sec"><span class="hx-eye">Simple process</span><h2>How booking works</h2><div class="hx-steps">'
             + ''.join(f'<div class="hx-step"><div class="hx-n">{svg(i)}</div><b>{t}</b><p>{d}</p></div>' for i, t, d in steps) + '</div></section>')
    h.append('<section id="tanzania-faq" class="hx-sec"><span class="hx-eye">FAQ</span><h2>Common questions about a Tanzania holiday</h2><div class="hx-faqs">'
             + ''.join(f'<details class="hx-faq"{" open" if k == 0 else ""}><summary>{html.escape(q)}</summary><div class="hx-ans"><p>{html.escape(a)}</p></div></details>' for k, (q, a) in enumerate(FAQ)) + '</div></section>')
    def _img(img): return SPECIAL_IMG[img] if img in SPECIAL_IMG else f'https://suzutravels.com/wp-content/uploads/2026/10/{img}.webp'
    h.append('<section id="more-destinations" class="hx-sec"><span class="hx-eye">Explore more</span><h2>Explore more destinations</h2>'
             '<p class="hx-sub">Every trip is planned the same way — your dates, your budget, one team from quote to return. <a href="https://suzutravels.com/international-tour-packages/">See all international holidays →</a></p><div class="hx-mini">'
             + ''.join(f'<a class="hx-mc" href="https://suzutravels.com/{p}/"><img src="{_img(img)}" alt="{html.escape(n)} holiday — Suzu Travels" width="640" height="360" loading="lazy" decoding="async"><span><b>{html.escape(n)}</b><em>{html.escape(e)}</em></span></a>' for p, n, img, e in REL) + '</div></section>')
    h.append(f'<div class="hx-final"><img src="{U(FINAL)}" alt="{A(FINAL)}" width="1600" height="900" loading="lazy" decoding="async">'
             '<h2>Plan your Tanzania safari</h2><p>Send us your dates and group size. We will come back with a costed, day-by-day Tanzania itinerary you can compare, no obligation.</p>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Request a Tanzania Quote {svg("arrow")}</a><a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div>'
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
    open('pages/tanzania-tour-packages.html', 'w').write(o)
    print('pages/tanzania-tour-packages.html', len(o), len(o.encode()))
