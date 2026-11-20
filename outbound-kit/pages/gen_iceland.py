#!/usr/bin/env python3
"""Iceland page - .hx design; same template as gen_cambodia.py / gen_southkorea.py.
Run from outbound-kit/:  python3 pages/gen_iceland.py <PAGE_ID> -> pages/iceland-tour-packages.html (one line)
Facts (official pages read 20 Nov 2026 with curl):
- government.is, Embassy of Iceland in New Delhi, Consular Services: "Yes, Indian citizens are required to obtain a Schengen
  visa before traveling to Iceland"; the Embassy handles all visa matters; applications in one of the VFS Global visa
  application centres in India; a Schengen visa issued for Iceland gives access to the other Schengen countries.
- island.is/en/get-a-visa (Ministry for Foreign Affairs): uniform Schengen visa valid for the whole area for up to 90 days;
  apply at the embassy of the main destination (longest stay, or first if equal); fee EUR 90 (EUR 45 for 6-12 year olds);
  generally apply in person; processing approx. two weeks when complete; passport valid at least 3 months beyond departure
  and issued within the last 10 years; in some instances the Ministry decides.
- island.is/en/entry-requirements-to-iceland (Directorate of Immigration): same passport rule for non-EEA/EFTA citizens.
Not stated (not read officially): EES/biometric border details, visa validity/multiple-entry rules for Indians.
Keyword Planner IN 20 Nov 2026: "iceland tour package" 2,400/mo (focus kw), "iceland tour package from india" 320,
"iceland trip cost from india" 590, "iceland visa for indians" 1,900.
Photos: Wikimedia Commons (CC BY 4.0, CC BY-SA 4.0, CC BY-SA 2.5 CA; licence + author read from each File: page raw
wikitext 20 Nov 2026), WP IDs 23867-23879; every uploaded WP copy viewed.
Climate/season/daylight wording is general guidance (no figures); no package prices; no flight times.
"""
import json, html, sys, os
sys.path.insert(0, os.getcwd())
import gen_hub as G

PID = int(sys.argv[1]) if len(sys.argv) > 1 else 0
M = G.M
svg, WA_SVG, wa = G.svg, G.WA_SVG, G.wa
CHECKED = '20 November 2026'
SRC_EMB = 'https://www.government.is/ministries/diplomatic-missions/new-delhi-india/consular-services/'
SRC_VISA = 'https://island.is/en/get-a-visa'
SRC_ENTRY = 'https://island.is/en/entry-requirements-to-iceland'

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
body.page-id-PID .page-header:before{content:"Holidays abroad \00B7  Iceland";display:inline-block;font:800 12px/1 "Plus Jakarta Sans",sans-serif;letter-spacing:.18em;text-transform:uppercase;color:#1a1606;background:#E2C158;padding:8px 13px;border-radius:999px;margin-bottom:16px}
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
HERO = ['iceland-1', 'iceland-2', 'iceland-3', 'iceland-4', 'iceland-5', 'iceland-6']
GAL = ['iceland-7', 'iceland-8', 'iceland-9', 'iceland-10', 'iceland-11', 'iceland-12', 'iceland-13']
FINAL = 'iceland-5'  # wide Reynisfjara + Reynisdrangar (also hero slide 5)

FAQ = [
    ("Do Indians need a visa for Iceland?", "Yes. The Embassy of Iceland in New Delhi states that Indian citizens are required to obtain a Schengen visa before travelling to Iceland (checked 20 November 2026). Iceland is part of the Schengen area, so a Schengen visa issued for your Iceland trip also covers the other Schengen countries. Whether a visa is issued is always the decision of the Icelandic authorities."),
    ("Where do I apply for an Iceland visa in India?", "The Embassy of Iceland in New Delhi handles visa matters and receives applications through the VFS Global visa application centres in India. If Iceland is your main destination — the Schengen country where you spend the most nights, or the first one if the nights are equal — you apply for Iceland. If you spend longer in another Schengen country, you apply to that country instead."),
    ("What is the Schengen visa fee and processing time for Iceland?", "Iceland's official visa page (Ministry for Foreign Affairs, on island.is) listed a visa application fee of EUR 90, or EUR 45 for children aged six to twelve, when we checked on 20 November 2026. It says applications are generally lodged in person and take approximately two weeks when all documents are in order. Fees and timings can change, so we re-check when you book and suggest applying well ahead of your travel dates."),
    ("How long must my passport be valid for Iceland?", "Iceland's official guidance for visitors who are not EEA/EFTA citizens says the passport must be valid for at least three months beyond your intended departure date from Iceland and must have been issued within the last ten years."),
    ("When can I see the northern lights in Iceland?", "The northern lights need dark, clear skies, so the season runs through the darker months, roughly from September to April. Sightings depend on solar activity and cloud cover and are never guaranteed — we plan stays away from town lights and keep a flexible evening for a guided aurora outing."),
    ("How many days are enough for an Iceland trip?", "Six to eight nights covers Reykjavík, the Golden Circle and the south coast as far as the Jökulsárlón glacier lagoon. With ten to twelve nights you can drive the full Ring Road around the island, or add the Snæfellsnes peninsula and the north around Lake Mývatn."),
    ("Is it safe to drive in Iceland in winter?", "Winter roads can be icy and weather changes quickly, and some roads close in storms. For most Indian travellers we recommend a private driver-guide or guided day tours from November to March, with spare time built into the plan. Self-drive suits summer better, when daylight is long."),
    ("Why are there no prices on this page?", "An Iceland trip cost depends on your dates, season, hotel category, self-drive or driver-guide, tours such as glacier walks or ice caves, and the airfare from your city. Instead of a teaser price that changes when you ask, we send a costed, day-by-day quote for your dates — usually within 24 hours."),
]

JS = ("(function(){var f=document.getElementById('hxPlan');if(!f){return;}f.addEventListener('submit',function(e){e.preventDefault();"
      "var d=f.querySelector('[name=d]').value,s=f.querySelector('[name=s]').value,m=f.querySelector('[name=m]').value,a=f.querySelector('[name=a]').value,k=f.querySelector('[name=k]').value,c=f.querySelector('[name=c]').value;"
      "var t='Hi Suzu Travels, please send me a costed Iceland itinerary.\\nTrip: '+d+'\\nTrip type: '+s+'\\nTravel month: '+m+'\\nAdults: '+a+'\\nChildren: '+k;"
      "if(c){t=t+'\\nDeparting from: '+c;}"
      "window.open('https:'+String.fromCharCode(47,47)+'wa.me/917087488961?text='+encodeURIComponent(t),'_blank','noopener');});})();")

REL = [('europe-tour-packages', 'Europe', 'suzu-abroad-europe', 'Paris, Swiss Alps, Italy'), ('switzerland-tour-packages', 'Switzerland', 'suzu-abroad-switzerland', 'Lucerne, Jungfrau, Zermatt'),
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
SPECIAL_IMG = {'HK': 'https://suzutravels.com/wp-content/uploads/2026/11/hong-kong-victoria-harbour-night-from-the-peak-768x363.webp',
               'CN': 'https://suzutravels.com/wp-content/uploads/2026/11/china-great-wall-mutianyu-768x575.webp',
               'RU': 'https://suzutravels.com/wp-content/uploads/2026/11/russia-moscow-saint-basils-cathedral-red-square-768x512.webp',
               'NZ': 'https://suzutravels.com/wp-content/uploads/2026/11/new-zealand-milford-sound-mitre-peak-768x481.webp',
               'PH': 'https://suzutravels.com/wp-content/uploads/2026/11/philippines-el-nido-big-lagoon-palawan-768x512.webp',
               'KR': 'https://suzutravels.com/wp-content/uploads/2026/11/south-korea-seoul-gyeongbokgung-geunjeongjeon-768x432.webp',
               'KH': 'https://suzutravels.com/wp-content/uploads/2026/11/cambodia-angkor-wat-reflection-pond-768x499.webp'}

def build():
    W = "Hi Suzu Travels, I'm planning an Iceland trip. Please share a quote."
    h = [f'<div class="suzu-intl hx hx-country"><style>{CSS}</style>']
    slides = ''.join(f'<div class="hx-slide"><img src="{U(s)}" alt="{A(s)}" width="1600" height="1000" {"fetchpriority=\"high\" loading=\"eager\"" if i == 0 else "loading=\"lazy\""} decoding="async"><span class="hx-cap">{C(s)}</span></div>' for i, s in enumerate(HERO))
    h.append('<section class="hx-hero" aria-label="Iceland tour packages from India"><div class="hx-slides">' + slides + '</div><div class="hx-copy">'
             '<p class="hx-lede">Stand behind the curtain of Seljalandsfoss, watch Strokkur geyser erupt, walk the black sand of Reynisfjara and see icebergs drift across the Jökulsárlón glacier lagoon — then wait under a dark sky for the northern lights. We plan Iceland to your dates, budget and season, with a private driver-guide or a well-paced self-drive, warm stays, vegetarian meals noted in advance and honest guidance on the Schengen visa.</p>'
             '<div class="hx-badges">'
             f'<span class="hx-badge">{svg("globe")}Golden Circle &amp; south coast</span><span class="hx-badge">{svg("doc")}Schengen visa steps explained</span>'
             f'<span class="hx-badge">{svg("team")}Couples, families &amp; groups</span><span class="hx-badge">{svg("food")}Vegetarian meals planned</span></div>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Get an Iceland Quote {svg("arrow")}</a>'
             f'<a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div></div>'
             '<form class="hx-plan" id="hxPlan" aria-label="Get a costed Iceland itinerary on WhatsApp"><h3>Plan my Iceland trip</h3>'
             '<p>Tell us the basics — we reply on WhatsApp with a costed, day-by-day plan, usually within 24 hours.</p><div class="hx-f">'
             '<label class="hx-full">Trip<select name="d"><option selected>Golden Circle + south coast (classic)</option><option>Northern lights winter trip</option><option>Full Ring Road</option><option>Iceland + Europe</option><option>Reykjavík short break</option><option>Not sure yet</option></select></label>'
             '<label>Trip type<select name="s"><option>Honeymoon / couple</option><option>Family</option><option>Friends</option><option>Seniors</option><option>Group</option><option>Corporate / MICE</option></select></label>'
             f'<label>Travel month<select name="m">{G.months()}</select></label>'
             '<label>Adults<select name="a"><option>1</option><option selected>2</option><option>3</option><option>4</option><option>5</option><option>6</option><option>7–10</option><option>11–20</option><option>20+</option></select></label>'
             '<label>Children<select name="k"><option>0</option><option>1</option><option>2</option><option>3</option><option>4+</option></select></label>'
             '<label class="hx-full">Departing from<input name="c" type="text" placeholder="e.g. Delhi, Mumbai, Chandigarh" autocomplete="address-level2"></label></div>'
             f'<button class="hx-btn" type="submit">{WA_SVG}Get my Iceland plan on WhatsApp</button><small>Opens WhatsApp with your details filled in. We do not store anything on this page.</small></form></section>')
    h.append('<div class="hx-trust">'
             f'<div>{svg("clock")}<span><b>Quote in ~24 hours</b><span>Costed, day by day</span></span></div>'
             f'<div>{svg("doc")}<span><b>Honest visa guidance</b><span>Official Icelandic sources, checked</span></span></div>'
             f'<div>{svg("shield")}<span><b>HP Tourism registered</b><span>Reg. DTO-MND-11-243/2022</span></span></div>'
             f'<div>{svg("chat")}<span><b>One team, start to finish</b><span>Reachable while you travel</span></span></div></div>')
    h.append('<nav class="hx-toc" aria-label="On this page"><a href="#why-iceland">Why Iceland</a><a href="#iceland-in-photos">Photos</a><a href="#how-to-choose">Choose your trip</a><a href="#sample-itinerary">Sample itinerary</a><a href="#when-to-go">When to go</a><a href="#visa-and-entry">Visa</a><a href="#whats-included">What\'s included</a><a href="#iceland-faq">FAQ</a></nav>')
    facts = [('Getting there', 'Fly into Keflavík International Airport near Reykjavík; we compare connections from your city'), ('Time difference', 'India is 5 hours 30 minutes ahead of Iceland'), ('Currency', 'Icelandic króna (ISK); card payments are widely used'),
             ('Best season', 'June to August for long days; September to March for the northern lights'), ('Typical trip', '6 to 8 nights; 10 to 12 for the full Ring Road'), ('Entry', 'Schengen visa needed for Indians — apply through VFS Global in India')]
    h.append('<section id="why-iceland" class="hx-sec"><span class="hx-eye">Iceland</span><h2>Why Iceland is worth it for Indian travellers</h2>'
             '<p class="hx-sub">Few places pack so much nature into one short trip: waterfalls you can walk behind, an erupting geyser, black sand beaches, glacier lagoons full of icebergs and the rift valley of Þingvellir, all on good roads from Reykjavík. Summer brings very long days for road trips; winter brings snow, ice caves and the chance of the northern lights. One Schengen visa covers Iceland and the rest of the Schengen area, so it also pairs well with Europe.</p>'
             '<div class="hx-facts">' + ''.join(f'<div class="hx-fact"><b>{a}</b><span>{b}</span></div>' for a, b in facts) + '</div></section>')
    h.append('<section id="iceland-in-photos" class="hx-sec"><span class="hx-eye">Real places</span><h2>Iceland in photos</h2>'
             '<p class="hx-sub">Svartifoss among its basalt columns, Gullfoss in early spring, Strokkur geyser, the lava rifts of Þingvellir, Seljalandsfoss, an ice block on Diamond Beach and the canyon of Fjaðrárgljúfur. Real photos by Wikimedia Commons photographers, credited below.</p><div class="hx-pg">'
             + ''.join(f'<figure><img src="{U(k) if j == 0 else M[k]["med"]}" alt="{A(k)}" width="800" height="600" loading="lazy" decoding="async"><figcaption>{C(k)}</figcaption></figure>' for j, k in enumerate(GAL)) + '</div></section>')
    cards = [('First-timers', 'Golden Circle &amp; south coast', 'Þingvellir, Geysir and Gullfoss, then the south coast waterfalls, Reynisfjara beach and the Jökulsárlón glacier lagoon — the classic first trip.'),
             ('Winter', 'Northern lights trip', 'November to March: stays away from town lights, a guided aurora evening, ice-cave and glacier tours when conditions allow, and a driver-guide for winter roads.'),
             ('Couples', 'Lagoons &amp; glaciers', 'Geothermal lagoons, a glacier walk, boutique hotels and countryside lodges — a slower, scenic honeymoon with time for the views.'),
             ('Combine', 'Iceland &amp; Europe', 'Add Iceland to a Europe or Switzerland holiday — one Schengen visa covers both, and we plan the order of countries around your visa application.')]
    stays = [('Reykjavík — city centre', 'Walkable streets around Hallgrímskirkja and the old harbour, with restaurants, the Harpa concert hall and easy pick-ups for day tours.'),
             ('South coast — Hella to Vík', 'Country hotels and farm stays close to Seljalandsfoss, Skógafoss and Reynisfjara, with darker skies for the northern lights.'),
             ('South-east — near Jökulsárlón', 'Hotels and guesthouses between Skaftafell and Höfn, for an early start at the glacier lagoon and Diamond Beach.'),
             ('Countryside lodges', 'Quiet lodges and cabins away from town lights — good for couples and for watching the night sky in winter.')]
    h.append('<section id="how-to-choose" class="hx-sec"><span class="hx-eye">How to choose</span><h2>Choose the Iceland trip that fits you</h2>'
             '<p class="hx-sub">Start from the kind of trip you want — we fine-tune the route, hotels, tours, vehicle and driver to your group and season.</p><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><span class="hx-tag">{t}</span><h3>{n}</h3><p>{d}</p></div>' for t, n, d in cards) + '</div>'
             '<h3 style="margin-top:30px">Where to stay</h3><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><h3>{n}</h3><p>{d}</p></div>' for n, d in stays) + '</div></section>')
    days = [('Day 1', 'Arrive in Reykjavík', 'Transfer from Keflavík airport to Reykjavík. Easy evening around Hallgrímskirkja and the old harbour.'),
            ('Day 2', 'Golden Circle', 'The rift valley of Þingvellir, Strokkur geyser at Geysir and the Gullfoss waterfall; overnight in the south.'),
            ('Day 3', 'South coast waterfalls', 'Walk behind Seljalandsfoss, climb beside Skógafoss and see the sea stacks from Reynisfjara black sand beach near Vík.'),
            ('Day 4', 'Canyon &amp; Skaftafell', 'Fjaðrárgljúfur canyon, then Skaftafell for the walk to Svartifoss and its basalt columns.'),
            ('Day 5', 'Jökulsárlón &amp; Diamond Beach', 'Icebergs in the glacier lagoon and ice on the black sand; a glacier walk, or an ice-cave tour in winter when conditions allow.'),
            ('Day 6', 'Back west', 'A scenic drive back along the south coast with stops you missed; in winter, an evening out for the northern lights.'),
            ('Day 7', 'Snæfellsnes or Reykjavík', 'A day trip to Kirkjufell on the Snæfellsnes peninsula, or a slow day in Reykjavík with a geothermal lagoon.'),
            ('Day 8', 'Fly home', 'Transfer to Keflavík airport and fly home — or continue to Europe on the same Schengen visa.')]
    h.append('<section id="sample-itinerary" class="hx-sec"><span class="hx-eye">Sample plan</span><h2>A sample 8-day Iceland itinerary</h2>'
             '<p class="hx-sub">The classic first trip. We rebuild it around you — add the north and Lake Mývatn for the full Ring Road, keep it to four nights around Reykjavík, or slow it down for winter driving.</p><div class="hx-itin">'
             + ''.join(f'<div class="hx-day"><i>{a}</i><b>{b}</b><p>{c}</p></div>' for a, b, c in days) + '</div></section>')
    seasons = [('Jun – Aug', '<span class="hx-ok">Best</span>', 'Mildest, very long days', 'The easiest time for road trips and hikes, with daylight late into the night; also the busiest season, so book early. No northern lights in the bright nights.'),
               ('Sep – Oct', '<span class="hx-ok">Good</span>', 'Cool, darker nights return', 'Autumn colours, fewer visitors and the first chances of the northern lights; weather becomes more changeable.'),
               ('Nov – Mar', '<span class="hx-mid">Aurora</span>', 'Cold, short days, snow and ice', 'The main northern lights and ice-cave season. Daylight is short and some roads can close in storms — we use a driver-guide and keep spare time.'),
               ('Apr – May', '<span class="hx-mid">Quiet</span>', 'Cool, days lengthening', 'Fewer visitors and longer days; snow can linger on higher ground. A good value window for the Golden Circle and south coast.')]
    h.append('<section id="when-to-go" class="hx-sec"><span class="hx-eye">Best season</span><h2>When to go to Iceland</h2>'
             '<p class="hx-sub">There is no single best month — summer is for long days on the road, winter is for snow and the northern lights. We check the season, daylight, holidays and flight prices against your plan before we quote.</p>'
             '<div class="hx-tw"><table class="hx-t"><thead><tr><th>Months</th><th>Verdict</th><th>Weather</th><th>What it means for your trip</th></tr></thead><tbody>'
             + ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in seasons) + '</tbody></table></div></section>')
    h.append('<section id="visa-and-entry" class="hx-sec"><span class="hx-eye">Visa &amp; entry</span><h2>Iceland visa for Indian passport holders</h2>'
             '<div class="hx-visa"><div class="hx-vbox"><h3>What the official sources say</h3><ul>'
             f'<li><b>A Schengen visa is needed.</b> The <a href="{SRC_EMB}" target="_blank" rel="noopener nofollow">Embassy of Iceland in New Delhi</a> states that Indian citizens are required to obtain a Schengen visa before travelling to Iceland.</li>'
             '<li><b>Where to apply:</b> the Embassy handles visa matters and receives applications through the VFS Global visa application centres in India.</li>'
             f'<li><b>Main destination rule:</b> according to <a href="{SRC_VISA}" target="_blank" rel="noopener nofollow">Iceland&rsquo;s official visa page</a>, you apply to the Schengen country where you will spend the longest time — or the one you visit first if the time is equal. A uniform Schengen visa is valid for travel in the whole Schengen area for up to 90 days.</li>'
             '<li><b>Fee and timing:</b> the same page lists a visa application fee of EUR 90 (EUR 45 for children aged six to twelve), says applications are generally lodged in person, and gives a processing time of approximately two weeks when all documents are in order.</li>'
             f'<li><b>Passport:</b> for visitors who are not EEA/EFTA citizens, Iceland&rsquo;s <a href="{SRC_ENTRY}" target="_blank" rel="noopener nofollow">entry requirements</a> say the passport must be valid at least three months beyond the intended departure date and issued within the last ten years.</li></ul>'
             f'<p class="hx-checked">Checked {CHECKED} · sources: <a href="{SRC_EMB}" target="_blank" rel="noopener nofollow">Embassy of Iceland in New Delhi — consular services</a> · <a href="{SRC_VISA}" target="_blank" rel="noopener nofollow">Apply for a visa to Iceland — Ministry for Foreign Affairs (island.is)</a> · <a href="{SRC_ENTRY}" target="_blank" rel="noopener nofollow">Entry requirements to Iceland — Directorate of Immigration (island.is)</a></p></div>'
             '<div class="hx-vnote"><p><b>Please note:</b> whether a visa is issued is always the decision of the Icelandic authorities, and admission is decided at the border. We help you prepare a clear, consistent application — itinerary, hotel bookings and travel insurance — but we never promise an outcome we do not control.</p>'
             '<p>Fees, documents and processing times can change. We re-check the official sources when you book, and we suggest applying well before your travel dates, especially for summer and the Christmas–New Year period.</p></div></div></section>')
    inc = [('doc', 'Visa paperwork help', 'A day-by-day itinerary, hotel confirmations and a document checklist for your Schengen application through VFS Global.'), ('pin', 'Hotels', 'Named hotels and lodges in Reykjavík and along your route, chosen for your budget and season.'),
           ('team', 'Driver-guide or self-drive', 'A private driver-guide in a comfortable vehicle, or a self-drive car with a route planned around daylight and weather.'), ('globe', 'Tours', 'Golden Circle, south coast, glacier walk, ice cave in winter, whale watching, northern lights evening and lagoons, as you choose.'),
           ('food', 'Meal plan', 'Breakfast at most hotels; vegetarian and Jain needs noted in advance, with restaurant and supermarket stops planned on long drives.'), ('award', 'Flights optional', 'Land-only, or a full package with international flights from your nearest Indian airport.')]
    h.append('<section id="whats-included" class="hx-sec"><span class="hx-eye">Your package</span><h2>What a Suzu Iceland package includes</h2><div class="hx-inc">'
             + ''.join(f'<div>{svg(i)}<span><b>{t}</b><span>{d}</span></span></div>' for i, t, d in inc) + '</div></section>')
    steps = [('chat', 'Tell us the basics', 'Dates, travellers and the kind of trip you want. A WhatsApp message is enough.'),
             ('doc', 'Get a costed itinerary', 'A day-by-day plan with named hotels and a clear per-person price, usually within 24 hours.'),
             ('sliders', 'Adjust until it fits', 'Change the route, hotels, tours or add Europe. We re-quote as needed.'),
             ('lock', 'Confirm with a token', 'Lock your plan with a small token amount; the balance is paid later, as agreed in writing.')]
    h.append('<section id="how-booking-works" class="hx-sec"><span class="hx-eye">Simple process</span><h2>How booking works</h2><div class="hx-steps">'
             + ''.join(f'<div class="hx-step"><div class="hx-n">{svg(i)}</div><b>{t}</b><p>{d}</p></div>' for i, t, d in steps) + '</div></section>')
    h.append('<section id="iceland-faq" class="hx-sec"><span class="hx-eye">FAQ</span><h2>Common questions about an Iceland tour</h2><div class="hx-faqs">'
             + ''.join(f'<details class="hx-faq"{" open" if k == 0 else ""}><summary>{html.escape(q)}</summary><div class="hx-ans"><p>{html.escape(a)}</p></div></details>' for k, (q, a) in enumerate(FAQ)) + '</div></section>')
    def _img(img): return SPECIAL_IMG[img] if img in SPECIAL_IMG else f'https://suzutravels.com/wp-content/uploads/2026/10/{img}.webp'
    h.append('<section id="more-destinations" class="hx-sec"><span class="hx-eye">Explore more</span><h2>Explore more destinations</h2>'
             '<p class="hx-sub">Every trip is planned the same way — your dates, your budget, one team from quote to return. <a href="https://suzutravels.com/international-tour-packages/">See all international holidays →</a></p><div class="hx-mini">'
             + ''.join(f'<a class="hx-mc" href="https://suzutravels.com/{p}/"><img src="{_img(img)}" alt="{html.escape(n)} holiday — Suzu Travels" width="640" height="360" loading="lazy" decoding="async"><span><b>{html.escape(n)}</b><em>{html.escape(e)}</em></span></a>' for p, n, img, e in REL) + '</div></section>')
    h.append(f'<div class="hx-final"><img src="{U(FINAL)}" alt="{A(FINAL)}" width="1600" height="900" loading="lazy" decoding="async">'
             '<h2>Plan your Iceland trip</h2><p>Send us your dates and group size. We will come back with a costed, day-by-day Iceland itinerary you can compare, no obligation.</p>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Request an Iceland Quote {svg("arrow")}</a><a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div>'
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
    open('pages/iceland-tour-packages.html', 'w').write(o)
    print('pages/iceland-tour-packages.html', len(o), len(o.encode()))
