#!/usr/bin/env python3
"""Kenya page - .hx design; same template as gen_oman.py.
Built + published 25 Nov 2026 (photos WP 25339-25352; 13 used, 25344 Diani beach bar spare - business sign + people, do not use).
Run from outbound-kit/:  python3 pages/gen_kenya.py <PAGE_ID> -> pages/kenya-tour-packages.html (one line)
Facts (official Kenya eTA portal etakenya.go.ke, Directorate of Immigration Services; read 25 Nov 2026 with curl):
- /how-to-apply: "All visitors including infants and children who intend to travel to the Republic of Kenya must have an
  approved Electronic Travel Authorisation (eTA) before the start of their journey." Exemption list (Kenya Citizenship and
  Immigration (Amendment) Rules, 2025): EAC partner states, listed countries 90/60 days; for India only "Holders of
  Diplomatic, Official or Service Passports from the Republic of India" (90 days) -> ordinary Indian passports need an eTA.
  Documents: passport min 6 months validity + one blank page, selfie/passport photo, email + phone, itinerary (arrival and
  departure), accommodation booking confirmation, payment card. Processing typically 3 working days.
- /general-information: eTA "is not the final authority to enter ... Admissibility will be determined at the point of
  entry"; usually processed in 3 days, urgent service exists, recommended to apply at least 2 weeks before travel.
- /faqs: apply only on etakenya.go.ke or the official "Kenya Travel Authorisation" app; one eTA per traveller (group option);
  normal processing up to 72 hours "starting at $30", expedited (immediate) "an addition $100"; approval/refusal by email.
- /eligibility: Standard eTA "Allows entry into Kenya once" $30; Transit $20; One Year Multi-Entry $300.
NOT stated officially (not on the page): length of stay allowed on a standard eTA -> not claimed.
Keyword Planner IN 25 Nov 2026: "kenya tour package" 1,600/mo (focus kw), "masai mara tour package" 2,900,
"kenya masai mara safari packages" 2,900 (May-Jun peak 12,100-18,100), "kenya safari package" 880, "kenya visa for indians"
3,600, "kenya tour package from india" 260, "kenya holiday packages" 210, "kenya trip cost from india" 140.
Photos: Wikimedia Commons (CC BY-SA 3.0 Amoghavarsha JS; CC BY-SA 4.0 Volodymyr Burdiak, Kidoleeee, Diego Delso, Alexmbogo,
Lebu Ayiga; CC0 Hobbyfotowiki). Season wording is general guidance; no package prices; no flight or drive times.
"""
import json, html, sys, os
sys.path.insert(0, os.getcwd())
import gen_hub as G

PID = int(sys.argv[1]) if len(sys.argv) > 1 else 0
M = dict(G.M)
PREVIEW = False
svg, WA_SVG, wa = G.svg, G.WA_SVG, G.wa
CHECKED = '25 November 2026'
SRC_EMB = 'https://etakenya.go.ke/how-to-apply'
SRC_VISA = 'https://etakenya.go.ke/eligibility'
SRC_ENTRY = 'https://etakenya.go.ke/faqs'
SRC_GEN = 'https://etakenya.go.ke/general-information'

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
body.page-id-PID .page-header:before{content:"Holidays abroad \00B7  Kenya";display:inline-block;font:800 12px/1 "Plus Jakarta Sans",sans-serif;letter-spacing:.18em;text-transform:uppercase;color:#1a1606;background:#E2C158;padding:8px 13px;border-radius:999px;margin-bottom:16px}
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
HERO = ['kenya-1', 'kenya-2', 'kenya-3', 'kenya-4', 'kenya-5', 'kenya-6']
GAL = ['kenya-7', 'kenya-8', 'kenya-9', 'kenya-10', 'kenya-11', 'kenya-12', 'kenya-13']
FINAL = 'kenya-2'  # giraffes in the Masai Mara (also in the hero)

FAQ = [
    ("Do Indians need a visa for Kenya?", "Kenya has replaced the visa with an Electronic Travel Authorisation (eTA) for most visitors. The official eTA portal says every visitor, including infants and children, must have an approved eTA before starting the journey. For India, only diplomatic, official and service passport holders are on the exemption list, so travellers on an ordinary Indian passport need an eTA (checked 25 November 2026). The eTA is not the final authority to enter — admission is decided at the point of entry by the Kenyan authorities."),
    ("How much does the Kenya eTA cost?", "On the official portal etakenya.go.ke, the standard eTA, which allows one entry into Kenya, is listed at USD 30, and the expedited service costs an additional USD 100 (checked 25 November 2026). Fees can change, and the portal shows the amount for your eTA type when you apply. Each traveller needs their own eTA, even in a group."),
    ("What documents do I need for the Kenya eTA?", "The official portal asks for a passport valid for at least six months with at least one blank page, a selfie or passport-type photo, your email and phone number, a travel itinerary with arrival and departure, an accommodation booking confirmation and a card to pay. We give you a clear day-by-day itinerary and lodge confirmations to upload."),
    ("How early should I apply for the Kenya eTA?", "The official portal says applications are usually processed in about three working days, but can take longer, and recommends applying at least two weeks before travel. Apply only on etakenya.go.ke or the official Kenya Travel Authorisation app. The approved eTA arrives by email; carry it with you for departure and arrival."),
    ("When is the best time for a Masai Mara safari?", "The drier months from late June to October are the classic safari season in the Masai Mara, and the great wildebeest migration is usually in the Mara from about July to October — the herds follow the rains, so the timing changes a little each year. January and February are also dry and good for game drives. The long rains, roughly March to May, and the short rains around November make some roads muddy, but the parks are greener and quieter."),
    ("How many days are enough for a Kenya safari?", "Six to eight nights covers Nairobi, two or three nights in the Masai Mara, a night at Lake Naivasha or Lake Nakuru and two nights in Amboseli with views of Mount Kilimanjaro. Add three or four nights on the Indian Ocean coast at Diani for a safari-and-beach holiday."),
    ("Is Kenya good for families and vegetarian travellers?", "Yes. Safari lodges and tented camps welcome families, many have pools, and game drives can be kept shorter for young children and seniors. Nairobi has many Indian restaurants, and lodges and camps can prepare vegetarian and Jain meals when we tell them in advance — we note your needs at every stay."),
    ("Why are there no prices on this page?", "A Kenya safari cost depends on your dates, the season, the lodges or camps you choose, park fees, the vehicle, whether you drive or fly into the Masai Mara, and the airfare from your city. Instead of a teaser price that changes when you ask, we send a costed, day-by-day quote for your dates — usually within 24 hours."),
]

JS = ("(function(){var f=document.getElementById('hxPlan');if(!f){return;}f.addEventListener('submit',function(e){e.preventDefault();"
      "var d=f.querySelector('[name=d]').value,s=f.querySelector('[name=s]').value,m=f.querySelector('[name=m]').value,a=f.querySelector('[name=a]').value,k=f.querySelector('[name=k]').value,c=f.querySelector('[name=c]').value;"
      "var t='Hi Suzu Travels, please send me a costed Kenya itinerary.\\nTrip: '+d+'\\nTrip type: '+s+'\\nTravel month: '+m+'\\nAdults: '+a+'\\nChildren: '+k;"
      "if(c){t=t+'\\nDeparting from: '+c;}"
      "window.open('https:'+String.fromCharCode(47,47)+'wa.me/917087488961?text='+encodeURIComponent(t),'_blank','noopener');});})();")

REL = [('seychelles-tour-packages', 'Seychelles', 'SC', 'Mahé, Praslin, La Digue'), ('mauritius-tour-packages', 'Mauritius', 'suzu-abroad-mauritius', 'Lagoons, Le Morne, island tours'),
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
               'SC': M['seychelles-1']['med'], 'OM': M['oman']['med']}


def build():
    W = "Hi Suzu Travels, I'm planning a Kenya safari. Please share a quote."
    h = [f'<div class="suzu-intl hx hx-country"><style>{CSS}</style>']
    slides = ''.join(f'<div class="hx-slide"><img src="{U(s)}" alt="{A(s)}" width="1600" height="1000" {"fetchpriority=\"high\" loading=\"eager\"" if i == 0 else "loading=\"lazy\""} decoding="async"><span class="hx-cap">{C(s)}</span></div>' for i, s in enumerate(HERO))
    h.append('<section class="hx-hero" aria-label="Kenya tour packages from India"><div class="hx-slides">' + slides + '</div><div class="hx-copy">'
             '<p class="hx-lede">Watch lions, cheetahs and the great herds on game drives in the Masai Mara, see elephants walk beneath Mount Kilimanjaro in Amboseli, take a boat out on Lake Naivasha and finish on the white sand of Diani. We plan your Kenya safari to your dates, budget and pace, with lodges or tented camps, a safari vehicle and driver-guide, vegetarian meals noted in advance and honest guidance on the eTA.</p>'
             '<div class="hx-badges">'
             f'<span class="hx-badge">{svg("globe")}Masai Mara, Amboseli &amp; lakes</span><span class="hx-badge">{svg("doc")}eTA steps explained</span>'
             f'<span class="hx-badge">{svg("team")}Families, couples &amp; groups</span><span class="hx-badge">{svg("food")}Vegetarian meals planned</span></div>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Get a Kenya Quote {svg("arrow")}</a>'
             f'<a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div></div>'
             '<form class="hx-plan" id="hxPlan" aria-label="Get a costed Kenya itinerary on WhatsApp"><h3>Plan my Kenya safari</h3>'
             '<p>Tell us the basics — we reply on WhatsApp with a costed, day-by-day plan, usually within 24 hours.</p><div class="hx-f">'
             '<label class="hx-full">Trip<select name="d"><option selected>Masai Mara, lakes &amp; Amboseli</option><option>Masai Mara short safari</option><option>Safari + Diani beach</option><option>Migration season safari (Jul–Oct)</option><option>Kenya + Dubai</option><option>Not sure yet</option></select></label>'
             '<label>Trip type<select name="s"><option>Family</option><option>Honeymoon / couple</option><option>Friends</option><option>Seniors</option><option>Group</option><option>Corporate / MICE</option></select></label>'
             f'<label>Travel month<select name="m">{G.months()}</select></label>'
             '<label>Adults<select name="a"><option>1</option><option selected>2</option><option>3</option><option>4</option><option>5</option><option>6</option><option>7–10</option><option>11–20</option><option>20+</option></select></label>'
             '<label>Children<select name="k"><option>0</option><option>1</option><option>2</option><option>3</option><option>4+</option></select></label>'
             '<label class="hx-full">Departing from<input name="c" type="text" placeholder="e.g. Delhi, Mumbai, Chandigarh" autocomplete="address-level2"></label></div>'
             f'<button class="hx-btn" type="submit">{WA_SVG}Get my Kenya plan on WhatsApp</button><small>Opens WhatsApp with your details filled in. We do not store anything on this page.</small></form></section>')
    h.append('<div class="hx-trust">'
             f'<div>{svg("clock")}<span><b>Quote in ~24 hours</b><span>Costed, day by day</span></span></div>'
             f'<div>{svg("doc")}<span><b>Honest eTA guidance</b><span>Official Kenya eTA portal, checked</span></span></div>'
             f'<div>{svg("shield")}<span><b>HP Tourism registered</b><span>Reg. DTO-MND-11-243/2022</span></span></div>'
             f'<div>{svg("chat")}<span><b>One team, start to finish</b><span>Reachable while you travel</span></span></div></div>')
    h.append('<nav class="hx-toc" aria-label="On this page"><a href="#why-kenya">Why Kenya</a><a href="#kenya-in-photos">Photos</a><a href="#how-to-choose">Choose your trip</a><a href="#sample-itinerary">Sample itinerary</a><a href="#when-to-go">When to go</a><a href="#visa-and-entry">eTA</a><a href="#whats-included">What\'s included</a><a href="#kenya-faq">FAQ</a></nav>')
    facts = [('Getting there', 'Fly into Jomo Kenyatta International Airport, Nairobi — we compare routes and connections from your city'), ('Time difference', 'India is 2 hours 30 minutes ahead of Kenya'), ('Currency', 'Kenyan shilling (KES)'),
             ('Best season', 'Late June to October (migration usually July to October); January and February are also dry'), ('Typical trip', '6 to 8 nights: Masai Mara, a Rift Valley lake and Amboseli'), ('Entry', 'Electronic Travel Authorisation (eTA) online before you fly, for every traveller')]
    h.append('<section id="why-kenya" class="hx-sec"><span class="hx-eye">Kenya</span><h2>Why Kenya is worth it for Indian travellers</h2>'
             '<p class="hx-sub">Kenya, on the east coast of Africa across the Indian Ocean from India, is one of the easiest places in the world to go on safari. The Masai Mara has big cats and huge herds of wildebeest and zebra, Amboseli has elephants with Mount Kilimanjaro behind them, and the Rift Valley lakes of Naivasha and Nakuru add boat rides, birds and rhinos. Nairobi has its own national park on the edge of the city, and the coast at Diani has white beaches for a few slow days after the safari.</p>'
             '<div class="hx-facts">' + ''.join(f'<div class="hx-fact"><b>{a}</b><span>{b}</span></div>' for a, b in facts) + '</div></section>')
    h.append('<section id="kenya-in-photos" class="hx-sec"><span class="hx-eye">Real places</span><h2>Kenya in photos</h2>'
             '<p class="hx-sub">Grassland and acacia woodland at Lake Nakuru, a giraffe in front of the Nairobi skyline in Nairobi National Park, elephants in the Masai Mara and Amboseli, a lion at Lake Nakuru, a wooden ngalawa canoe on Diani Beach and the lake at dusk. Real photos by Wikimedia Commons photographers, credited below.</p><div class="hx-pg">'
             + ''.join(f'<figure><img src="{U(k) if j == 0 else M[k]["med"]}" alt="{A(k)}" width="800" height="600" loading="lazy" decoding="async"><figcaption>{C(k)}</figcaption></figure>' for j, k in enumerate(GAL)) + '</div></section>')
    cards = [('First-timers', 'Mara, lakes &amp; Amboseli', 'The classic circuit: game drives in the Masai Mara, a boat on Lake Naivasha, rhinos at Lake Nakuru and elephants under Kilimanjaro in Amboseli.'),
             ('Families', 'Easy-paced safari', 'Lodges with pools, shorter game drives with breaks, the Giraffe Centre in Nairobi — and the option to fly into the Masai Mara instead of the long drive.'),
             ('Couples', 'Tented camp &amp; beach', 'A tented camp in the Masai Mara, an optional sunrise balloon flight, then slow days on the Indian Ocean at Diani.'),
             ('Migration', 'July to October', 'Time your Masai Mara nights for the wildebeest migration season. Camps fill early, so we suggest booking months ahead.')]
    stays = [('Nairobi', 'City hotels for the first and last night — close to the airport, Nairobi National Park and the Giraffe Centre.'),
             ('Masai Mara', 'Lodges and tented camps inside or just outside the reserve, from comfortable to luxury, usually with all meals.'),
             ('Naivasha &amp; Nakuru', 'Lakeside lodges at Naivasha, or stays near Lake Nakuru National Park for an early game drive.'),
             ('Amboseli &amp; Diani', 'Lodges and camps with Kilimanjaro views in Amboseli; beach resorts at Diani for the coast.')]
    h.append('<section id="how-to-choose" class="hx-sec"><span class="hx-eye">How to choose</span><h2>Choose the Kenya safari that fits you</h2>'
             '<p class="hx-sub">Start from the kind of trip you want — we fine-tune the route, lodges, vehicle and pace to your group and season.</p><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><span class="hx-tag">{t}</span><h3>{n}</h3><p>{d}</p></div>' for t, n, d in cards) + '</div>'
             '<h3 style="margin-top:30px">Where to stay</h3><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><h3>{n}</h3><p>{d}</p></div>' for n, d in stays) + '</div></section>')
    days = [('Day 1', 'Arrive in Nairobi', 'Airport pick-up and transfer to your hotel. If time allows, visit the Giraffe Centre or Nairobi National Park.'),
            ('Day 2', 'Into the Masai Mara', 'Drive to the Masai Mara (or take a short flight), check in at your lodge or tented camp and head out on an afternoon game drive.'),
            ('Day 3', 'Masai Mara full day', 'Morning and afternoon game drives for lions, cheetahs, elephants and the herds. Optional sunrise balloon flight or a Maasai village visit.'),
            ('Day 4', 'Lake Naivasha', 'A last morning drive in the Mara, then on to Lake Naivasha for a boat ride to see hippos and birds.'),
            ('Day 5', 'Lake Nakuru', 'Game drive in Lake Nakuru National Park, known for its rhinos and birdlife, then overnight at Nakuru or Naivasha.'),
            ('Day 6', 'To Amboseli', 'A long drive south to Amboseli, with an evening game drive across the plains below Mount Kilimanjaro.'),
            ('Day 7', 'Amboseli', 'Early game drive, when the mountain is often clearest, to see elephant herds, then free time at the lodge and another drive.'),
            ('Day 8', 'Fly home', 'Drive back to Nairobi for your flight home — or carry on to the beach at Diani for three or four more nights.')]
    h.append('<section id="sample-itinerary" class="hx-sec"><span class="hx-eye">Sample plan</span><h2>A sample 8-day Kenya safari itinerary</h2>'
             '<p class="hx-sub">The classic road safari with a driver-guide. We rebuild it around you — fly into the Mara to save time, add more nights in the migration season, or finish on the beach at Diani.</p><div class="hx-itin">'
             + ''.join(f'<div class="hx-day"><i>{a}</i><b>{b}</b><p>{c}</p></div>' for a, b, c in days) + '</div></section>')
    seasons = [('Jan – Feb', '<span class="hx-ok">Good</span>', 'Warm and mostly dry', 'Good game viewing in all the parks; a popular time for the Christmas and New Year holidays, so book early.'),
               ('Mar – May', '<span class="hx-mid">Rainy</span>', 'The long rains', 'Green, quieter parks; some roads get muddy and a few camps close, so we choose lodges and routes with care.'),
               ('Jun – Oct', '<span class="hx-ok">Best</span>', 'Dry season, cool mornings', 'The classic safari season; the wildebeest migration is usually in the Masai Mara from about July to October. Busiest and most in demand — book well ahead.'),
               ('Nov – Dec', '<span class="hx-mid">Short rains</span>', 'Short showers', 'Short rains around November, often in the afternoons; good value before the busy holiday weeks in late December.')]
    h.append('<section id="when-to-go" class="hx-sec"><span class="hx-eye">Best season</span><h2>When to go to Kenya</h2>'
             '<p class="hx-sub">Kenya has wildlife to see all year. The dry months are easiest for game drives, and the herds of the great migration follow the rains, so their timing changes a little each year. This is general guidance; we check the season, camp availability and flight prices against your plan before we quote.</p>'
             '<div class="hx-tw"><table class="hx-t"><thead><tr><th>Months</th><th>Verdict</th><th>Weather</th><th>What it means for your trip</th></tr></thead><tbody>'
             + ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in seasons) + '</tbody></table></div></section>')
    h.append('<section id="visa-and-entry" class="hx-sec"><span class="hx-eye">Visa &amp; entry</span><h2>Kenya eTA for Indian passport holders</h2>'
             '<div class="hx-visa"><div class="hx-vbox"><h3>What the official sources say</h3><ul>'
             f'<li><b>eTA before you travel.</b> The official <a href="{SRC_EMB}" target="_blank" rel="noopener nofollow">Kenya eTA portal</a> of the Directorate of Immigration Services says all visitors, including infants and children, must have an approved Electronic Travel Authorisation (eTA) before the start of their journey.</li>'
             '<li><b>Indian passports:</b> on the exemption list, India appears only for diplomatic, official and service passport holders. Travellers on an ordinary Indian passport apply for an eTA.</li>'
             f'<li><b>Fees on the portal:</b> the <a href="{SRC_VISA}" target="_blank" rel="noopener nofollow">standard eTA</a>, for one entry, is listed at USD 30; the expedited service costs an additional USD 100. Each traveller needs their own eTA, even in a group.</li>'
             '<li><b>Documents:</b> a passport valid for at least six months with at least one blank page, a selfie or passport-type photo, email and phone number, a travel itinerary with arrival and departure, an accommodation booking confirmation and a card to pay.</li>'
             f'<li><b>Timing:</b> usually about three working days, but it can take longer; the portal recommends applying at least two weeks before travel. Apply only on etakenya.go.ke or the official Kenya Travel Authorisation app (<a href="{SRC_ENTRY}" target="_blank" rel="noopener nofollow">eTA FAQ</a>).</li></ul>'
             f'<p class="hx-checked">Checked {CHECKED} · sources: <a href="{SRC_EMB}" target="_blank" rel="noopener nofollow">How to apply — Kenya eTA</a> · <a href="{SRC_GEN}" target="_blank" rel="noopener nofollow">General information — Kenya eTA</a> · <a href="{SRC_VISA}" target="_blank" rel="noopener nofollow">eTA types and fees — Kenya eTA</a> · <a href="{SRC_ENTRY}" target="_blank" rel="noopener nofollow">FAQs — Kenya eTA</a></p></div>'
             '<div class="hx-vnote"><p><b>Please note:</b> eTA approval, and entry at the border, are always the decision of the Kenyan authorities — the portal itself says an eTA is not the final authority to enter and admissibility is decided at the point of entry. We help you prepare clear, consistent documents — itinerary, lodge bookings and return tickets — but we never promise an outcome we do not control.</p>'
             '<p>Rules and fees can change. We re-check the official portal when you book. Please also ask your doctor about vaccinations and malaria precautions, and check the current health rules for your return to India, before you travel.</p></div></div></section>')
    inc = [('doc', 'eTA paperwork help', 'A day-by-day itinerary, lodge confirmations and help with the Kenya eTA application for each traveller.'), ('pin', 'Lodges &amp; camps', 'Named hotels, safari lodges and tented camps in Nairobi, the Masai Mara, the lakes and Amboseli, chosen for your budget.'),
           ('team', 'Safari vehicle &amp; guide', 'Airport transfers and a safari vehicle with a pop-up roof and an English-speaking driver-guide — or flights into the Mara.'), ('globe', 'Game drives &amp; park fees', 'Game drives, park entry fees and a boat ride on Lake Naivasha, itemised in your quote; balloon flight as an option.'),
           ('food', 'Meal plan', 'Usually all meals at safari lodges and camps; vegetarian and Jain needs noted in advance at every stay.'), ('award', 'Flights optional', 'Land-only, or a full package with international flights from your nearest Indian airport.')]
    h.append('<section id="whats-included" class="hx-sec"><span class="hx-eye">Your package</span><h2>What a Suzu Kenya package includes</h2><div class="hx-inc">'
             + ''.join(f'<div>{svg(i)}<span><b>{t}</b><span>{d}</span></span></div>' for i, t, d in inc) + '</div></section>')
    steps = [('chat', 'Tell us the basics', 'Dates, travellers and the kind of safari you want. A WhatsApp message is enough.'),
             ('doc', 'Get a costed itinerary', 'A day-by-day plan with named lodges and a clear per-person price, usually within 24 hours.'),
             ('sliders', 'Adjust until it fits', 'Change the parks, lodges or vehicle, fly into the Mara or add Diani. We re-quote as needed.'),
             ('lock', 'Confirm with a token', 'Lock your plan with a small token amount; the balance is paid later, as agreed in writing.')]
    h.append('<section id="how-booking-works" class="hx-sec"><span class="hx-eye">Simple process</span><h2>How booking works</h2><div class="hx-steps">'
             + ''.join(f'<div class="hx-step"><div class="hx-n">{svg(i)}</div><b>{t}</b><p>{d}</p></div>' for i, t, d in steps) + '</div></section>')
    h.append('<section id="kenya-faq" class="hx-sec"><span class="hx-eye">FAQ</span><h2>Common questions about a Kenya safari</h2><div class="hx-faqs">'
             + ''.join(f'<details class="hx-faq"{" open" if k == 0 else ""}><summary>{html.escape(q)}</summary><div class="hx-ans"><p>{html.escape(a)}</p></div></details>' for k, (q, a) in enumerate(FAQ)) + '</div></section>')
    def _img(img): return SPECIAL_IMG[img] if img in SPECIAL_IMG else f'https://suzutravels.com/wp-content/uploads/2026/10/{img}.webp'
    h.append('<section id="more-destinations" class="hx-sec"><span class="hx-eye">Explore more</span><h2>Explore more destinations</h2>'
             '<p class="hx-sub">Every trip is planned the same way — your dates, your budget, one team from quote to return. <a href="https://suzutravels.com/international-tour-packages/">See all international holidays →</a></p><div class="hx-mini">'
             + ''.join(f'<a class="hx-mc" href="https://suzutravels.com/{p}/"><img src="{_img(img)}" alt="{html.escape(n)} holiday — Suzu Travels" width="640" height="360" loading="lazy" decoding="async"><span><b>{html.escape(n)}</b><em>{html.escape(e)}</em></span></a>' for p, n, img, e in REL) + '</div></section>')
    h.append(f'<div class="hx-final"><img src="{U(FINAL)}" alt="{A(FINAL)}" width="1600" height="900" loading="lazy" decoding="async">'
             '<h2>Plan your Kenya safari</h2><p>Send us your dates and group size. We will come back with a costed, day-by-day Kenya itinerary you can compare, no obligation.</p>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Request a Kenya Quote {svg("arrow")}</a><a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div>'
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
    open('pages/kenya-tour-packages.html', 'w').write(o)
    print('pages/kenya-tour-packages.html', len(o), len(o.encode()))
