#!/usr/bin/env python3
"""Norway page - .hx design; same template as gen_iceland.py.
PREPARED 21 Nov 2026 but NOT PUBLISHED: the Suzu Travels WordPress connector needed a reconnect, so no photo could be
uploaded and no page created. Next run: upload the 14 photos in photos/upload_plan_norway.json (view every WP copy,
fix alt/cap if needed), add them to photos/wp_map.json as norway-1..14 + 'norway', then build with the page id.
Run from outbound-kit/:  python3 pages/gen_norway.py <PAGE_ID> -> pages/norway-tour-packages.html (one line)
Until wp_map has norway-* keys the build uses the Commons 1280px thumbs (PREVIEW only, never publish that build).
Facts (official UDI pages read 21 Nov 2026 with curl, personalised for citizens of India, ?c=ind):
- udi.no visitors-visa-to-norway: "If you plan to visit Norway for up to 90 days, you can apply for a visitor visa. This visa
  is valid for entry to all Schengen countries." Requirements: application fee; all documents on the embassy's checklist;
  passport valid at least three months after the end of the visit and issued within the last ten years; valid travel
  insurance; enough money for the stay and return journey; register fingerprints. UDI considers how probable it is that
  the applicant returns home.
- udi.no how-to-apply (tourism, India): applications processed by embassies; hand in at the visa application centre, an
  embassy or a consulate no earlier than six months before travel; several Schengen countries -> embassy/consulate of
  the main destination; no work (incl. remote work) on a visitor visa.
- udi.no/en/word-definitions/fees/: visitor visa adults and children over 12 EUR 90; children 6-12 EUR 45.
Not stated (not read officially): the name of the visa centre operator in India (norway.no India pages are behind a
Cloudflare JS challenge from the sandbox), processing times.
Keyword Planner IN 20 Nov 2026 (BACKLOG #85): "norway tour package" 2,400/mo (focus kw), "norway trip cost from india" 720.
Photos: Wikimedia Commons (CC BY-SA 3.0/4.0, CC BY 2.0/4.0, CC BY-SA 2.0 DE; licence + author from raw wikitext 21 Nov 2026).
Climate/season/daylight wording is general guidance; no package prices; no flight times.
"""
import json, html, sys, os
sys.path.insert(0, os.getcwd())
import gen_hub as G

PID = int(sys.argv[1]) if len(sys.argv) > 1 else 0
M = dict(G.M)
PLAN = json.load(open('photos/upload_plan_norway.json'))
PREVIEW = not all(p['slug'] in M for p in PLAN)
if PREVIEW:
    for p in PLAN:
        M[p['slug']] = dict(url=p['thumb1280'], med=p['thumb1280'], alt=p['alt'], cap=p['cap'], credit=p['credit'], license=p['license'], src=p['src'])
svg, WA_SVG, wa = G.svg, G.WA_SVG, G.wa
CHECKED = '21 November 2026'
SRC_EMB = 'https://www.udi.no/en/want-to-apply/visit-and-holiday/visitors-visa-to-norway/?c=ind'
SRC_VISA = 'https://www.udi.no/en/want-to-apply/visit-and-holiday/visitors-visa-to-norway/tourism-or-visit-norway-for-other-reasons1/how-to-apply-for-a-visitors-visa/?c=ind'
SRC_ENTRY = 'https://www.udi.no/en/word-definitions/fees/'

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
body.page-id-PID .page-header:before{content:"Holidays abroad \00B7  Norway";display:inline-block;font:800 12px/1 "Plus Jakarta Sans",sans-serif;letter-spacing:.18em;text-transform:uppercase;color:#1a1606;background:#E2C158;padding:8px 13px;border-radius:999px;margin-bottom:16px}
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
HERO = ['norway-1', 'norway-2', 'norway-3', 'norway-6', 'norway-5', 'norway-8']
GAL = ['norway-4', 'norway-7', 'norway-9', 'norway-10', 'norway-11', 'norway-12', 'norway-13']
FINAL = 'norway-3'  # Reine, Lofoten (also hero slide 3)

FAQ = [
    ("Do Indians need a visa for Norway?", "Yes. Norway's Directorate of Immigration (UDI) says that citizens of India who plan to visit Norway for up to 90 days can apply for a visitor visa, and that this visa is valid for entry to all Schengen countries (checked 21 November 2026). Whether a visa is issued is always the decision of the Norwegian authorities."),
    ("Where do I apply for a Norway visa in India?", "UDI says visitor visa applications are processed by embassies and are handed in at the visa application centre, an embassy or a consulate, no earlier than six months before you travel. If Norway is your main destination in the Schengen area, you apply for Norway; if you spend longer in another Schengen country, you apply to that country instead. We confirm the current application centre and checklist for your city when you book."),
    ("What is the Norway visa fee?", "UDI's fee list showed EUR 90 for a visitor visa for adults and children over 12, and EUR 45 for children aged six to twelve, when we checked on 21 November 2026. Fees can change, so we re-check when you book. Any service charge of the visa application centre is separate."),
    ("What documents do I need for a Norway visitor visa?", "UDI lists these requirements: the application fee, all documents on the embassy's checklist, a passport valid for at least three months after the end of your visit and issued within the last ten years, valid travel insurance, enough money for your stay and return journey, and registration of your fingerprints. We help you prepare a clear itinerary and hotel confirmations for the file."),
    ("When can I see the northern lights in Norway?", "The northern lights need dark, clear skies, so the season in northern Norway — around Tromsø and the Lofoten islands — runs through the darker months, roughly from late September to March. Sightings depend on solar activity and cloud cover and are never guaranteed; we plan nights away from town lights and keep a flexible evening for a guided aurora outing."),
    ("How many days are enough for a Norway trip?", "Seven to nine nights covers Oslo, the Flåm Railway, a Nærøyfjord cruise, Bergen and Geirangerfjord with Ålesund. For the north, add three to four nights in Tromsø or the Lofoten islands. Shorter trips of five nights work well around Oslo, Flåm and Bergen."),
    ("Is Norway good for a honeymoon or a family trip?", "Yes. Couples like fjord-side hotels, scenic train and boat journeys and winter cabins under the northern lights. Families do well with the Flåm Railway, fjord cruises and easy viewpoints such as Stegastein and Aksla. We pace the days for your group and plan vegetarian meals in advance."),
    ("Why are there no prices on this page?", "A Norway trip cost depends on your dates, season, hotel category, trains, fjord cruises and northern-lights tours, and the airfare from your city. Instead of a teaser price that changes when you ask, we send a costed, day-by-day quote for your dates — usually within 24 hours."),
]

JS = ("(function(){var f=document.getElementById('hxPlan');if(!f){return;}f.addEventListener('submit',function(e){e.preventDefault();"
      "var d=f.querySelector('[name=d]').value,s=f.querySelector('[name=s]').value,m=f.querySelector('[name=m]').value,a=f.querySelector('[name=a]').value,k=f.querySelector('[name=k]').value,c=f.querySelector('[name=c]').value;"
      "var t='Hi Suzu Travels, please send me a costed Norway itinerary.\\nTrip: '+d+'\\nTrip type: '+s+'\\nTravel month: '+m+'\\nAdults: '+a+'\\nChildren: '+k;"
      "if(c){t=t+'\\nDeparting from: '+c;}"
      "window.open('https:'+String.fromCharCode(47,47)+'wa.me/917087488961?text='+encodeURIComponent(t),'_blank','noopener');});})();")

REL = [('iceland-tour-packages', 'Iceland', 'IS', 'Golden Circle, glaciers, northern lights'), ('europe-tour-packages', 'Europe', 'suzu-abroad-europe', 'Paris, Swiss Alps, Italy'), ('switzerland-tour-packages', 'Switzerland', 'suzu-abroad-switzerland', 'Lucerne, Jungfrau, Zermatt'),
       ('uk-tour-packages', 'UK', 'suzu-abroad-uk', 'London, Cotswolds, Scotland'), ('russia-tour-packages', 'Russia', 'RU', 'Moscow, Saint Petersburg'),
       ('new-zealand-tour-packages', 'New Zealand', 'NZ', 'Queenstown, Milford, Mount Cook'), ('australia-tour-packages', 'Australia & NZ', 'suzu-abroad-australia', 'Sydney, Melbourne, Queenstown'),
       ('japan-tour-packages', 'Japan', 'suzu-abroad-japan', 'Tokyo, Fuji, Kyoto, Osaka'), ('south-korea-tour-packages', 'South Korea', 'KR', 'Seoul, Busan, Jeju'),
       ('china-tour-packages', 'China', 'CN', 'Great Wall, Xi’an, Shanghai'), ('hong-kong-tour-packages', 'Hong Kong & Macau', 'HK', 'Harbour, Peak, Disneyland, Macau'),
       ('turkey-tour-packages', 'Turkey', 'suzu-abroad-turkey', 'Istanbul, Cappadocia, Pamukkale'), ('egypt-tour-packages', 'Egypt', 'suzu-abroad-egypt', 'Cairo, Nile cruise, Luxor'),
       ('dubai-tour-packages', 'Dubai', 'suzu-abroad-dubai', 'Burj Khalifa, desert, Abu Dhabi'), ('georgia-tour-packages', 'Georgia', 'suzu-abroad-georgia', 'Tbilisi, Kazbegi, Gudauri'),
       ('azerbaijan-tour-packages', 'Azerbaijan', 'suzu-abroad-azerbaijan', 'Baku, Gabala, Shahdag'), ('armenia-tour-packages', 'Armenia', 'suzu-abroad-armenia', 'Yerevan, Garni, Sevan'),
       ('uzbekistan-tour-packages', 'Uzbekistan', 'suzu-abroad-uzbekistan', 'Samarkand, Bukhara, Khiva'), ('kazakhstan-tour-packages', 'Kazakhstan', 'suzu-abroad-kazakhstan', 'Almaty, lakes, Kyrgyzstan'),
       ('mauritius-tour-packages', 'Mauritius', 'suzu-abroad-mauritius', 'Lagoons, Le Morne, island tours'), ('maldives-tour-packages', 'Maldives', 'suzu-card-maldives', 'Overwater villas'),
       ('sri-lanka-tour-packages', 'Sri Lanka', 'suzu-card-sri-lanka', 'Beaches & tea country'), ('thailand-tour-packages', 'Thailand', 'suzu-card-thailand', 'Bangkok, Phuket, Krabi'),
       ('vietnam-tour-packages', 'Vietnam', 'suzu-card-vietnam', 'Hanoi, Ha Long, Hoi An'), ('cambodia-tour-packages', 'Cambodia', 'KH', 'Angkor Wat, Siem Reap, Phnom Penh'),
       ('philippines-tour-packages', 'Philippines', 'PH', 'Palawan, Boracay, Bohol'), ('malaysia-tour-packages', 'Malaysia', 'suzu-card-malaysia', 'KL, Langkawi, Genting'),
       ('singapore-tour-packages', 'Singapore', 'suzu-card-singapore', 'City, Sentosa, Universal'), ('bali-tour-packages', 'Bali', 'suzu-card-bali', 'Ubud, villas, temples'),
       ('nepal-tour-packages', 'Nepal', 'suzu-card-nepal', 'No visa for Indians'), ('bhutan-tour-packages', 'Bhutan', 'suzu-card-bhutan', 'Paro, Thimphu, Punakha')]
SPECIAL_IMG = {'IS': 'https://suzutravels.com/wp-content/uploads/2026/11/iceland-jokulsarlon-glacier-lagoon-768x509.webp',
               'HK': 'https://suzutravels.com/wp-content/uploads/2026/11/hong-kong-victoria-harbour-night-from-the-peak-768x363.webp',
               'CN': 'https://suzutravels.com/wp-content/uploads/2026/11/china-great-wall-mutianyu-768x575.webp',
               'RU': 'https://suzutravels.com/wp-content/uploads/2026/11/russia-moscow-saint-basils-cathedral-red-square-768x512.webp',
               'NZ': 'https://suzutravels.com/wp-content/uploads/2026/11/new-zealand-milford-sound-mitre-peak-768x481.webp',
               'PH': 'https://suzutravels.com/wp-content/uploads/2026/11/philippines-el-nido-big-lagoon-palawan-768x512.webp',
               'KR': 'https://suzutravels.com/wp-content/uploads/2026/11/south-korea-seoul-gyeongbokgung-geunjeongjeon-768x432.webp',
               'KH': 'https://suzutravels.com/wp-content/uploads/2026/11/cambodia-angkor-wat-reflection-pond-768x499.webp'}

def build():
    W = "Hi Suzu Travels, I'm planning a Norway trip. Please share a quote."
    h = [f'<div class="suzu-intl hx hx-country"><style>{CSS}</style>']
    slides = ''.join(f'<div class="hx-slide"><img src="{U(s)}" alt="{A(s)}" width="1600" height="1000" {"fetchpriority=\"high\" loading=\"eager\"" if i == 0 else "loading=\"lazy\""} decoding="async"><span class="hx-cap">{C(s)}</span></div>' for i, s in enumerate(HERO))
    h.append('<section class="hx-hero" aria-label="Norway tour packages from India"><div class="hx-slides">' + slides + '</div><div class="hx-copy">'
             '<p class="hx-lede">Ride the Flåm Railway down to the fjord, cruise the narrow Nærøyfjord, walk the wooden wharf of Bryggen in Bergen and look down on Geirangerfjord — then head north to Tromsø or the Lofoten islands for the northern lights. We plan Norway to your dates, budget and season, with trains, fjord cruises and hotels lined up, vegetarian meals noted in advance and honest guidance on the Schengen visa.</p>'
             '<div class="hx-badges">'
             f'<span class="hx-badge">{svg("globe")}Fjords, trains &amp; cruises</span><span class="hx-badge">{svg("doc")}Schengen visa steps explained</span>'
             f'<span class="hx-badge">{svg("team")}Couples, families &amp; groups</span><span class="hx-badge">{svg("food")}Vegetarian meals planned</span></div>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Get a Norway Quote {svg("arrow")}</a>'
             f'<a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div></div>'
             '<form class="hx-plan" id="hxPlan" aria-label="Get a costed Norway itinerary on WhatsApp"><h3>Plan my Norway trip</h3>'
             '<p>Tell us the basics — we reply on WhatsApp with a costed, day-by-day plan, usually within 24 hours.</p><div class="hx-f">'
             '<label class="hx-full">Trip<select name="d"><option selected>Fjords: Oslo, Flåm, Bergen, Geiranger</option><option>Northern lights: Tromsø / Lofoten</option><option>Fjords + northern lights</option><option>Norway + Europe</option><option>Scandinavia (Norway, Sweden, Denmark)</option><option>Not sure yet</option></select></label>'
             '<label>Trip type<select name="s"><option>Honeymoon / couple</option><option>Family</option><option>Friends</option><option>Seniors</option><option>Group</option><option>Corporate / MICE</option></select></label>'
             f'<label>Travel month<select name="m">{G.months()}</select></label>'
             '<label>Adults<select name="a"><option>1</option><option selected>2</option><option>3</option><option>4</option><option>5</option><option>6</option><option>7–10</option><option>11–20</option><option>20+</option></select></label>'
             '<label>Children<select name="k"><option>0</option><option>1</option><option>2</option><option>3</option><option>4+</option></select></label>'
             '<label class="hx-full">Departing from<input name="c" type="text" placeholder="e.g. Delhi, Mumbai, Chandigarh" autocomplete="address-level2"></label></div>'
             f'<button class="hx-btn" type="submit">{WA_SVG}Get my Norway plan on WhatsApp</button><small>Opens WhatsApp with your details filled in. We do not store anything on this page.</small></form></section>')
    h.append('<div class="hx-trust">'
             f'<div>{svg("clock")}<span><b>Quote in ~24 hours</b><span>Costed, day by day</span></span></div>'
             f'<div>{svg("doc")}<span><b>Honest visa guidance</b><span>Official Norwegian sources, checked</span></span></div>'
             f'<div>{svg("shield")}<span><b>HP Tourism registered</b><span>Reg. DTO-MND-11-243/2022</span></span></div>'
             f'<div>{svg("chat")}<span><b>One team, start to finish</b><span>Reachable while you travel</span></span></div></div>')
    h.append('<nav class="hx-toc" aria-label="On this page"><a href="#why-norway">Why Norway</a><a href="#norway-in-photos">Photos</a><a href="#how-to-choose">Choose your trip</a><a href="#sample-itinerary">Sample itinerary</a><a href="#when-to-go">When to go</a><a href="#visa-and-entry">Visa</a><a href="#whats-included">What\'s included</a><a href="#norway-faq">FAQ</a></nav>')
    facts = [('Getting there', 'Fly into Oslo Gardermoen; Bergen and Tromsø via connections — we compare routes from your city'), ('Time difference', 'India is 4 hours 30 minutes ahead of Norway (3 hours 30 minutes in Norwegian summer time)'), ('Currency', 'Norwegian krone (NOK); card payments are widely used'),
             ('Best season', 'May to September for the fjords; late September to March for the northern lights'), ('Typical trip', '7 to 9 nights; add 3 to 4 for Tromsø or Lofoten'), ('Entry', 'Schengen visitor visa needed for Indians — apply before you travel')]
    h.append('<section id="why-norway" class="hx-sec"><span class="hx-eye">Norway</span><h2>Why Norway is worth it for Indian travellers</h2>'
             '<p class="hx-sub">Norway is the fjord country: deep blue water between steep green mountains, waterfalls on every side, and some of the most scenic train and boat journeys in Europe. In the south-west you link Oslo, the Flåm Railway, the Nærøyfjord, Bergen and Geiranger; in the Arctic north, Tromsø and the Lofoten islands bring winter snow and the chance of the northern lights. One Schengen visa covers Norway and the rest of the Schengen area, so it pairs well with Europe or Iceland.</p>'
             '<div class="hx-facts">' + ''.join(f'<div class="hx-fact"><b>{a}</b><span>{b}</span></div>' for a, b in facts) + '</div></section>')
    h.append('<section id="norway-in-photos" class="hx-sec"><span class="hx-eye">Real places</span><h2>Norway in photos</h2>'
             '<p class="hx-sub">The view from Preikestolen over Lysefjorden, the Flåm valley beside the railway line, the Oslo Opera House roof, Ålesund from Aksla, the fishing harbour of Hamnøy in Lofoten, the Atlantic Ocean Road and Geiranger from Flydalsjuvet. Real photos by Wikimedia Commons photographers, credited below.</p><div class="hx-pg">'
             + ''.join(f'<figure><img src="{U(k) if j == 0 else M[k]["med"]}" alt="{A(k)}" width="800" height="600" loading="lazy" decoding="async"><figcaption>{C(k)}</figcaption></figure>' for j, k in enumerate(GAL)) + '</div></section>')
    cards = [('First-timers', 'Fjords &amp; scenic trains', 'Oslo, the Bergen Line and the Flåm Railway, a Nærøyfjord cruise, Bergen and Geirangerfjord — the classic first trip.'),
             ('Winter', 'Northern lights in the Arctic', 'Late September to March: Tromsø or the Lofoten islands, a guided aurora evening, and snow activities when conditions allow.'),
             ('Couples', 'Fjord-side honeymoon', 'Fjord-view hotels, a slow cruise, the Stegastein viewpoint and a night or two in a quiet village — a scenic, unhurried honeymoon.'),
             ('Combine', 'Norway &amp; Europe', 'Add Norway to a Europe, Switzerland or Iceland holiday — one Schengen visa covers them, and we plan the order of countries around your application.')]
    stays = [('Oslo — city centre', 'Walkable streets near the harbour, the Opera House and the station, with easy trains to the fjords.'),
             ('Flåm &amp; Aurland', 'Small hotels by the Aurlandsfjord at the foot of the Flåm Railway, close to Stegastein and the Nærøyfjord cruise.'),
             ('Bergen — Bryggen area', 'Hotels near the old wharf and fish market, with the Fløibanen funicular a short walk away.'),
             ('Tromsø &amp; Lofoten', 'City hotels in Tromsø or fishermen&rsquo;s cabins in Lofoten — darker skies away from town lights in winter.')]
    h.append('<section id="how-to-choose" class="hx-sec"><span class="hx-eye">How to choose</span><h2>Choose the Norway trip that fits you</h2>'
             '<p class="hx-sub">Start from the kind of trip you want — we fine-tune the route, hotels, trains, cruises and tours to your group and season.</p><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><span class="hx-tag">{t}</span><h3>{n}</h3><p>{d}</p></div>' for t, n, d in cards) + '</div>'
             '<h3 style="margin-top:30px">Where to stay</h3><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><h3>{n}</h3><p>{d}</p></div>' for n, d in stays) + '</div></section>')
    days = [('Day 1', 'Arrive in Oslo', 'Transfer from Oslo airport to your hotel. Easy evening walk on the Opera House roof and along the harbour.'),
            ('Day 2', 'Oslo sightseeing', 'Vigeland sculpture park, the museums of the Bygdøy peninsula and the waterfront at Aker Brygge.'),
            ('Day 3', 'Bergen Line &amp; Flåm Railway', 'Scenic train across the mountains to Myrdal, then the Flåm Railway down the valley to Flåm by the fjord.'),
            ('Day 4', 'Nærøyfjord &amp; Stegastein', 'Morning at the Stegastein viewpoint, then a cruise on the narrow Nærøyfjord and onward to Bergen.'),
            ('Day 5', 'Bergen', 'The wooden wharf of Bryggen, the fish market and the Fløibanen funicular for a view over the city.'),
            ('Day 6', 'To the Geiranger area', 'A scenic drive north through fjord country with ferry crossings; overnight near Geiranger.'),
            ('Day 7', 'Geirangerfjord &amp; Ålesund', 'Viewpoints above Geiranger and a fjord cruise past waterfalls, then on to Ålesund and the Aksla viewpoint.'),
            ('Day 8', 'Fly home', 'Fly home via Oslo — or continue north to Tromsø or Lofoten for the northern lights in season.')]
    h.append('<section id="sample-itinerary" class="hx-sec"><span class="hx-eye">Sample plan</span><h2>A sample 8-day Norway itinerary</h2>'
             '<p class="hx-sub">The classic fjords trip. We rebuild it around you — add Tromsø or Lofoten for the north, keep it to five nights around Oslo, Flåm and Bergen, or slow it down for families and seniors.</p><div class="hx-itin">'
             + ''.join(f'<div class="hx-day"><i>{a}</i><b>{b}</b><p>{c}</p></div>' for a, b, c in days) + '</div></section>')
    seasons = [('May – Sep', '<span class="hx-ok">Best</span>', 'Mild, very long days', 'The main season for the fjords, the Flåm Railway, cruises and mountain roads; the busiest time, so book early. Midnight sun in the far north in early summer, so no northern lights.'),
               ('Late Sep – Oct', '<span class="hx-ok">Good</span>', 'Cool, autumn colours', 'Fewer visitors in the fjords and the first dark nights for the northern lights in the north; some mountain roads begin to close.'),
               ('Nov – Mar', '<span class="hx-mid">Aurora</span>', 'Cold, short days, snow in the north', 'The main northern lights season around Tromsø and Lofoten. Daylight is short in the Arctic, and some mountain roads around Geiranger are closed in winter.'),
               ('Apr', '<span class="hx-mid">Quiet</span>', 'Cool, days lengthening', 'A shoulder month with lengthening days; snow lingers in the mountains and some seasonal routes are not yet open.')]
    h.append('<section id="when-to-go" class="hx-sec"><span class="hx-eye">Best season</span><h2>When to go to Norway</h2>'
             '<p class="hx-sub">Summer is for the fjords, scenic trains and long days; winter is for snow and the northern lights in the Arctic north. We check the season, daylight, road openings and flight prices against your plan before we quote.</p>'
             '<div class="hx-tw"><table class="hx-t"><thead><tr><th>Months</th><th>Verdict</th><th>Weather</th><th>What it means for your trip</th></tr></thead><tbody>'
             + ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in seasons) + '</tbody></table></div></section>')
    h.append('<section id="visa-and-entry" class="hx-sec"><span class="hx-eye">Visa &amp; entry</span><h2>Norway visa for Indian passport holders</h2>'
             '<div class="hx-visa"><div class="hx-vbox"><h3>What the official sources say</h3><ul>'
             f'<li><b>A visitor visa is needed.</b> Norway&rsquo;s <a href="{SRC_EMB}" target="_blank" rel="noopener nofollow">Directorate of Immigration (UDI)</a> says citizens of India who plan to visit Norway for up to 90 days can apply for a visitor visa, and that it is valid for entry to all Schengen countries.</li>'
             f'<li><b>Where to apply:</b> according to <a href="{SRC_VISA}" target="_blank" rel="noopener nofollow">UDI&rsquo;s how-to-apply page</a>, visitor visa applications are processed by embassies and are handed in at the visa application centre, an embassy or a consulate — no earlier than six months before you travel.</li>'
             '<li><b>Main destination rule:</b> if you visit several Schengen countries, you apply to the embassy or consulate of the country that is your main destination.</li>'
             f'<li><b>Fee:</b> UDI&rsquo;s <a href="{SRC_ENTRY}" target="_blank" rel="noopener nofollow">fee list</a> shows EUR 90 for adults and children over 12, and EUR 45 for children aged six to twelve.</li>'
             '<li><b>Requirements:</b> all documents on the embassy&rsquo;s checklist, a passport valid at least three months after the end of your visit and issued within the last ten years, valid travel insurance, enough money for the stay and the return journey, and registration of your fingerprints. A visitor visa does not allow work, including remote work.</li></ul>'
             f'<p class="hx-checked">Checked {CHECKED} · sources: <a href="{SRC_EMB}" target="_blank" rel="noopener nofollow">Visitor visas for Norway — UDI (citizens of India)</a> · <a href="{SRC_VISA}" target="_blank" rel="noopener nofollow">How to apply for a visitor visa — UDI</a> · <a href="{SRC_ENTRY}" target="_blank" rel="noopener nofollow">Fees — UDI</a></p></div>'
             '<div class="hx-vnote"><p><b>Please note:</b> whether a visa is issued is always the decision of the Norwegian authorities, and admission is decided at the border. UDI says it considers how likely it is that you will return home after the visit. We help you prepare a clear, consistent application — itinerary, hotel bookings and travel insurance — but we never promise an outcome we do not control.</p>'
             '<p>Fees, documents and processing times can change. We re-check the official sources when you book, and we suggest applying well before your travel dates, especially for the summer season.</p></div></div></section>')
    inc = [('doc', 'Visa paperwork help', 'A day-by-day itinerary, hotel confirmations and a document checklist for your Schengen visitor visa application.'), ('pin', 'Hotels', 'Named hotels in Oslo, by the fjords, in Bergen and in the north, chosen for your budget and season.'),
           ('team', 'Trains, cruises &amp; transfers', 'The Bergen Line and Flåm Railway, fjord cruises, ferries and private transfers or a driver where it helps.'), ('globe', 'Tours', 'Fjord cruises, Stegastein, Bryggen, Geiranger viewpoints, Atlantic Ocean Road, and northern lights or snow activities in winter, as you choose.'),
           ('food', 'Meal plan', 'Breakfast at most hotels; vegetarian and Jain needs noted in advance, with restaurant stops planned on travel days.'), ('award', 'Flights optional', 'Land-only, or a full package with international flights from your nearest Indian airport.')]
    h.append('<section id="whats-included" class="hx-sec"><span class="hx-eye">Your package</span><h2>What a Suzu Norway package includes</h2><div class="hx-inc">'
             + ''.join(f'<div>{svg(i)}<span><b>{t}</b><span>{d}</span></span></div>' for i, t, d in inc) + '</div></section>')
    steps = [('chat', 'Tell us the basics', 'Dates, travellers and the kind of trip you want. A WhatsApp message is enough.'),
             ('doc', 'Get a costed itinerary', 'A day-by-day plan with named hotels and a clear per-person price, usually within 24 hours.'),
             ('sliders', 'Adjust until it fits', 'Change the route, hotels, tours or add Europe. We re-quote as needed.'),
             ('lock', 'Confirm with a token', 'Lock your plan with a small token amount; the balance is paid later, as agreed in writing.')]
    h.append('<section id="how-booking-works" class="hx-sec"><span class="hx-eye">Simple process</span><h2>How booking works</h2><div class="hx-steps">'
             + ''.join(f'<div class="hx-step"><div class="hx-n">{svg(i)}</div><b>{t}</b><p>{d}</p></div>' for i, t, d in steps) + '</div></section>')
    h.append('<section id="norway-faq" class="hx-sec"><span class="hx-eye">FAQ</span><h2>Common questions about a Norway tour</h2><div class="hx-faqs">'
             + ''.join(f'<details class="hx-faq"{" open" if k == 0 else ""}><summary>{html.escape(q)}</summary><div class="hx-ans"><p>{html.escape(a)}</p></div></details>' for k, (q, a) in enumerate(FAQ)) + '</div></section>')
    def _img(img): return SPECIAL_IMG[img] if img in SPECIAL_IMG else f'https://suzutravels.com/wp-content/uploads/2026/10/{img}.webp'
    h.append('<section id="more-destinations" class="hx-sec"><span class="hx-eye">Explore more</span><h2>Explore more destinations</h2>'
             '<p class="hx-sub">Every trip is planned the same way — your dates, your budget, one team from quote to return. <a href="https://suzutravels.com/international-tour-packages/">See all international holidays →</a></p><div class="hx-mini">'
             + ''.join(f'<a class="hx-mc" href="https://suzutravels.com/{p}/"><img src="{_img(img)}" alt="{html.escape(n)} holiday — Suzu Travels" width="640" height="360" loading="lazy" decoding="async"><span><b>{html.escape(n)}</b><em>{html.escape(e)}</em></span></a>' for p, n, img, e in REL) + '</div></section>')
    h.append(f'<div class="hx-final"><img src="{U(FINAL)}" alt="{A(FINAL)}" width="1600" height="900" loading="lazy" decoding="async">'
             '<h2>Plan your Norway trip</h2><p>Send us your dates and group size. We will come back with a costed, day-by-day Norway itinerary you can compare, no obligation.</p>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Request a Norway Quote {svg("arrow")}</a><a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div>'
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
    if PREVIEW: print('PREVIEW build (Commons thumbs) — do not publish')
    open('pages/norway-tour-packages.html' if not PREVIEW else 'pages/norway-tour-packages.preview.html', 'w').write(o)
    print('pages/norway-tour-packages.html', len(o), len(o.encode()))
