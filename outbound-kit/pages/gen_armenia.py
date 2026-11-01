#!/usr/bin/env python3
"""Armenia (Yerevan) page — .hx design; same template as gen_kazakhstan.py.
Run from outbound-kit/:  python3 pages/gen_armenia.py <PAGE_ID> -> pages/armenia-tour-packages.html (one line)
Facts: MFA Armenia visa page + its visa-check tool (India, ordinary passport; tool text "Updated 30.06.2026"; read 1 Nov 2026):
visa required. Options: (1) e-visa via evisa.mfa.am with travel (medical) insurance + EITHER a valid residence permit/visa of EU/Schengen,
USA, Australia, NZ, Rep. of Korea, UK, Canada, RF or Japan (or a GCC residence permit) OR air ticket reservation with return + invitation
from a party in Armenia (e.g. local tourist agency) + proof of funds (3-month bank statement etc.); (2) visa at the Armenian border with
such a valid visa/residence permit; (3) at Armenian embassies (application, photo, insurance, invitation, funds, ticket, consular fee).
Passport valid for the entire stay. "It is recommended to apply for E-VISA. Processing time is three working days."
Temporary visa exemption 1 Jul 2026 – 1 Jul 2027 for nationals of 111 countries (India is on the list PDF) holding a US/EU/Schengen/UAE/
Bahrain/Qatar/KSA/Kuwait/Oman residence permit valid >= 6 months from entry: up to 180 days in a year. Armenian visas are issued for
max 120 days (+60 extension). No fees shown on our page.
Keyword Planner IN 1 Nov 2026: "armenia tour package" 590/mo (720 Oct-Dec 2025), "armenia tour package from india" 90/mo (focus kw),
"armenia trip cost from india" 90/mo (170 May-Jun).
Photos: Wikimedia Commons (CC0 / CC BY / CC BY-SA, file pages checked 1 Nov 2026), WP IDs 17219-17233.
"""

import json, html, sys, os
sys.path.insert(0, os.getcwd())
import gen_hub as G

PID = int(sys.argv[1]) if len(sys.argv) > 1 else 0
M = G.M
svg, WA_SVG, wa = G.svg, G.WA_SVG, G.wa
CHECKED = '1 November 2026'
SRC_MFA = 'https://www.mfa.am/en/visa/'
SRC_EVISA = 'https://evisa.mfa.am/'
SRC_TVE = 'https://www.mfa.am/filemanager/consular/visa/2025/2026-06-30-LIST-OF-COUNTRIES-TEMPORARY-VISA-EXEMPTION.pdf'

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
body.page-id-PID .page-header:before{content:"Holidays abroad \00B7  Armenia";display:inline-block;font:800 12px/1 "Plus Jakarta Sans",sans-serif;letter-spacing:.18em;text-transform:uppercase;color:#1a1606;background:#E2C158;padding:8px 13px;border-radius:999px;margin-bottom:16px}
body.page-id-PID .page-header .entry-title{color:#fff!important;font-family:"Sora","Plus Jakarta Sans",sans-serif!important;font-size:clamp(34px,4.2vw,58px)!important;line-height:1.06!important;letter-spacing:-.035em!important;margin:0!important;font-weight:800!important;max-width:15ch;text-shadow:0 2px 24px rgba(0,0,0,.35)}
@media(max-width:1100px){.hx .hx-cards{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-itin{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-visa{grid-template-columns:1fr}.hx .hx-inc,.hx .hx-steps{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:700px){body.page-id-PID .page-header{left:14px;right:14px;padding:26px 18px 0}body.page-id-PID .page-header:before{font-size:10.5px;padding:7px 11px;margin-bottom:12px}body.page-id-PID .page-header .entry-title{font-size:33px!important}.hx .hx-facts{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-pg{grid-template-columns:repeat(2,minmax(0,1fr));grid-auto-rows:150px}.hx .hx-pg figure:first-child{grid-column:span 2;grid-row:span 1}.hx .hx-pg figure:nth-child(4){grid-row:span 1}.hx .hx-pg figure:nth-child(8){display:none}.hx .hx-cards,.hx .hx-itin,.hx .hx-inc,.hx .hx-steps{grid-template-columns:1fr}.hx .hx-mini{grid-template-columns:repeat(2,minmax(0,1fr))}}
.hx .hx-pg p,.hx .hx-cards>p,.hx .hx-itin>p,.hx .hx-inc>p,.hx .hx-facts>p{display:none}
""".replace('PID', str(PID))
CSS = ' '.join(l.strip() for l in (base + EXTRA).strip().splitlines() if l.strip() and not l.strip().startswith('/*'))
CSS = CSS + (' body.page-id-PID .page-header .entry-title{max-width:19ch;font-size:clamp(32px,3.6vw,52px)!important}'
              ' @media(max-width:700px){body.page-id-PID .page-header .entry-title{font-size:28px!important}}').replace('PID', str(PID))
CSS = CSS + ' @media(min-width:1101px){.hx .hx-itin{grid-template-columns:repeat(3,minmax(0,1fr))}}'
# Hostinger WAF (31 Oct 2026) returns 503 for writes containing '@media(' — use the equivalent '@media screen and ('
CSS = CSS.replace('@media(', '@media screen and (')
HERO = ['armenia-1', 'armenia-2', 'armenia-3', 'armenia-4', 'armenia-5', 'armenia-6']
GAL = ['armenia-9', 'armenia-7', 'armenia-11', 'armenia-10', 'armenia-8', 'armenia-12', 'armenia-13', 'armenia-14']
FINAL = 'armenia-15'

FAQ = [
    ("Do Indians need a visa for Armenia?", "Yes. The Ministry of Foreign Affairs of Armenia shows that Indian ordinary passport holders need a visa. Most travellers apply for an e-visa on the official portal (evisa.mfa.am); the Ministry recommends the e-visa and gives a processing time of three working days. With an Indian passport, the e-visa needs travel (medical) insurance plus either a valid visa or residence permit of the EU/Schengen states, the USA, the UK, Canada, Australia, New Zealand, the Republic of Korea, Russia or Japan (or a residence permit of a Gulf country), or a return air ticket reservation, an invitation from a party in Armenia such as a local tourist agency, and proof of funds. We checked this on 1 November 2026. Issuing a visa is always the decision of the Armenian authorities."),
    ("Can I get an Armenian visa on arrival with a US, UK or Schengen visa?", "The Ministry of Foreign Affairs of Armenia says Indian citizens can get a visa at the border if they show a valid visa or residence permit of the EU/Schengen states, the USA, the UK, Canada, Australia, New Zealand, the Republic of Korea, Russia or Japan, or a valid residence permit of the UAE, Saudi Arabia, Kuwait, Qatar, Bahrain or Oman. Separately, from 1 July 2026 to 1 July 2027, Indians who hold a US, EU, Schengen, UAE, Bahrain, Qatar, Saudi, Kuwait or Oman residence permit valid for at least six more months are exempt from the visa. Entry is always the decision of the Armenian border authorities, so we confirm your case before booking."),
    ("How many days are enough for Armenia?", "Five to six nights covers Yerevan, Garni and Geghard, Khor Virap and Noravank, Lake Sevan and Dilijan, and the long drive south to Tatev. With three or four nights, keep to Yerevan and the day trips around it. Add three or four nights to combine Armenia with Georgia."),
    ("Which is the best time to visit Armenia from India?", "May, June, September and October are the most comfortable months, with mild days for sightseeing and road trips. July and August are hot in Yerevan but fine for Lake Sevan and the hills. December to March is snow season — Garni and the mountains turn white, and the ski slopes at Tsaghkadzor open."),
    ("Can we combine Armenia with Georgia?", "Yes. Armenia and Georgia share a border, and a road transfer between Yerevan and Tbilisi via the north (Dilijan or Haghpat side) is a common way to combine them. Georgia has its own entry rules for Indian passport holders (usually an e-visa, unless you hold a qualifying visa or residence permit), so we plan both countries' paperwork together. See our Georgia page for that part of the trip."),
    ("Is vegetarian and Indian food available in Armenia?", "Armenian food has plenty of vegetarian dishes — fresh bread (lavash), salads, cheese, grilled vegetables, dried fruit and herbs — and Yerevan has Indian restaurants too. Outside Yerevan the choice is smaller, so we note vegetarian and Jain needs with hotels and drivers in advance and suggest where to eat."),
    ("Why are there no prices on this page?", "Armenia costs depend on your dates, hotel category, private car or small-group day trips, the Georgia add-on and the airfare from your city. Instead of a teaser price that changes when you ask, we send a costed, day-by-day quote for your dates — usually within 24 hours."),
]

JS = ("(function(){var f=document.getElementById('hxPlan');if(!f){return;}f.addEventListener('submit',function(e){e.preventDefault();"
      "var d=f.querySelector('[name=d]').value,s=f.querySelector('[name=s]').value,m=f.querySelector('[name=m]').value,a=f.querySelector('[name=a]').value,k=f.querySelector('[name=k]').value,c=f.querySelector('[name=c]').value;"
      "var t='Hi Suzu Travels, please send me a costed Armenia itinerary.\\nTrip: '+d+'\\nTrip type: '+s+'\\nTravel month: '+m+'\\nAdults: '+a+'\\nChildren: '+k;"
      "if(c){t=t+'\\nDeparting from: '+c;}"
      "window.open('https:'+String.fromCharCode(47,47)+'wa.me/917087488961?text='+encodeURIComponent(t),'_blank','noopener');});})();")

REL = [('georgia-tour-packages', 'Georgia', 'suzu-abroad-georgia', 'Tbilisi, Kazbegi, Gudauri'), ('azerbaijan-tour-packages', 'Azerbaijan', 'suzu-abroad-azerbaijan', 'Baku, Gabala, Shahdag'),
       ('dubai-tour-packages', 'Dubai', 'suzu-abroad-dubai', 'Burj Khalifa, desert, Abu Dhabi'), ('turkey-tour-packages', 'Turkey', 'suzu-abroad-turkey', 'Istanbul, Cappadocia, Pamukkale'),
       ('kazakhstan-tour-packages', 'Kazakhstan', 'suzu-abroad-kazakhstan', 'Almaty, lakes, Kyrgyzstan'), ('uzbekistan-tour-packages', 'Uzbekistan', 'suzu-abroad-uzbekistan', 'Samarkand, Bukhara, Khiva'),
       ('egypt-tour-packages', 'Egypt', 'suzu-abroad-egypt', 'Cairo, Nile cruise, Luxor'), ('europe-tour-packages', 'Europe', 'suzu-abroad-europe', 'Paris, Swiss Alps, Italy'),
       ('switzerland-tour-packages', 'Switzerland', 'suzu-abroad-switzerland', 'Lucerne, Jungfrau, Zermatt'), ('uk-tour-packages', 'UK', 'suzu-abroad-uk', 'London, Cotswolds, Scotland'),
       ('japan-tour-packages', 'Japan', 'suzu-abroad-japan', 'Tokyo, Fuji, Kyoto, Osaka'), ('australia-tour-packages', 'Australia & NZ', 'suzu-abroad-australia', 'Sydney, Melbourne, Queenstown'),
       ('mauritius-tour-packages', 'Mauritius', 'suzu-abroad-mauritius', 'Lagoons, Le Morne, island tours'), ('maldives-tour-packages', 'Maldives', 'suzu-card-maldives', 'Overwater villas'),
       ('bali-tour-packages', 'Bali', 'suzu-card-bali', 'Ubud, villas, temples'), ('thailand-tour-packages', 'Thailand', 'suzu-card-thailand', 'Bangkok, Phuket, Krabi'),
       ('singapore-tour-packages', 'Singapore', 'suzu-card-singapore', 'City, Sentosa, Universal'), ('malaysia-tour-packages', 'Malaysia', 'suzu-card-malaysia', 'KL, Langkawi, Genting'),
       ('vietnam-tour-packages', 'Vietnam', 'suzu-card-vietnam', 'Hanoi, Ha Long, Hoi An'), ('sri-lanka-tour-packages', 'Sri Lanka', 'suzu-card-sri-lanka', 'Beaches & tea country'),
       ('nepal-tour-packages', 'Nepal', 'suzu-card-nepal', 'No visa for Indians'), ('bhutan-tour-packages', 'Bhutan', 'suzu-card-bhutan', 'Paro, Thimphu, Punakha')]

def build():
    W = "Hi Suzu Travels, I'm planning an Armenia trip. Please share a quote."
    h = [f'<div class="suzu-intl hx hx-country"><style>{CSS}</style>']
    slides = ''.join(f'<div class="hx-slide"><img src="{U(s)}" alt="{A(s)}" width="1600" height="1000" {"fetchpriority=\"high\" loading=\"eager\"" if i == 0 else "loading=\"lazy\""} decoding="async"><span class="hx-cap">{C(s)}</span></div>' for i, s in enumerate(HERO))
    h.append('<section class="hx-hero" aria-label="Armenia tour packages from India"><div class="hx-slides">' + slides + '</div><div class="hx-copy">'
             '<p class="hx-lede">Snowy Mount Ararat above Yerevan, the Greek-style Garni Temple, Geghard Monastery cut into the rock, Noravank under red cliffs, blue Lake Sevan and Tatev on the edge of a gorge — Armenia packs a lot into a short, easy-paced holiday. We plan it to your dates, budget and pace, with good hotels, private drivers and honest e-visa guidance — and can pair it with Georgia.</p>'
             '<div class="hx-badges">'
             f'<span class="hx-badge">{svg("globe")}Yerevan, monasteries, Sevan &amp; Tatev</span><span class="hx-badge">{svg("doc")}E-visa guidance for Indians</span>'
             f'<span class="hx-badge">{svg("team")}Families, couples &amp; groups</span><span class="hx-badge">{svg("food")}Vegetarian meals planned</span></div>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Get an Armenia Quote {svg("arrow")}</a>'
             f'<a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div></div>'
             '<form class="hx-plan" id="hxPlan" aria-label="Get a costed Armenia itinerary on WhatsApp"><h3>Plan my Armenia trip</h3>'
             '<p>Tell us the basics — we reply on WhatsApp with a costed, day-by-day plan, usually within 24 hours.</p><div class="hx-f">'
             '<label class="hx-full">Trip<select name="d"><option selected>Yerevan + Garni, Sevan &amp; Tatev (classic)</option><option>Yerevan + day trips (short trip)</option><option>Armenia + Georgia</option><option>Armenia winter / snow trip</option><option>Armenia honeymoon</option><option>Not sure yet</option></select></label>'
             '<label>Trip type<select name="s"><option>Family</option><option>Honeymoon / couple</option><option>Friends</option><option>Seniors</option><option>Group</option><option>Corporate / MICE</option></select></label>'
             f'<label>Travel month<select name="m">{G.months()}</select></label>'
             '<label>Adults<select name="a"><option>1</option><option selected>2</option><option>3</option><option>4</option><option>5</option><option>6</option><option>7–10</option><option>11–20</option><option>20+</option></select></label>'
             '<label>Children<select name="k"><option>0</option><option>1</option><option>2</option><option>3</option><option>4+</option></select></label>'
             '<label class="hx-full">Departing from<input name="c" type="text" placeholder="e.g. Delhi, Mumbai, Chandigarh" autocomplete="address-level2"></label></div>'
             f'<button class="hx-btn" type="submit">{WA_SVG}Get my Armenia plan on WhatsApp</button><small>Opens WhatsApp with your details filled in. We do not store anything on this page.</small></form></section>')
    h.append('<div class="hx-trust">'
             f'<div>{svg("clock")}<span><b>Quote in ~24 hours</b><span>Costed, day by day</span></span></div>'
             f'<div>{svg("doc")}<span><b>Honest e-visa guidance</b><span>Official Armenian rules, checked</span></span></div>'
             f'<div>{svg("shield")}<span><b>HP Tourism registered</b><span>Reg. DTO-MND-11-243/2022</span></span></div>'
             f'<div>{svg("chat")}<span><b>One team, start to finish</b><span>On WhatsApp while you travel</span></span></div></div>')
    h.append('<nav class="hx-toc" aria-label="On this page"><a href="#why-armenia">Why Armenia</a><a href="#armenia-in-photos">Photos</a><a href="#how-to-choose">Choose your trip</a><a href="#sample-itinerary">Sample itinerary</a><a href="#when-to-go">When to go</a><a href="#visa-and-entry">Visa</a><a href="#whats-included">What\'s included</a><a href="#armenia-faq">FAQ</a></nav>')
    facts = [('Getting there', 'Fly into Yerevan; we compare routes and connections from your city'), ('Time difference', 'Armenia is 1 hour 30 minutes behind India'), ('Currency', 'Armenian dram (AMD)'),
             ('Best season', 'May–June and September–October; December to March for snow'), ('Typical trip', '5 to 6 nights; 8 to 10 with Georgia'), ('Visa', 'Visa needed; e-visa recommended (about 3 working days)')]
    h.append('<section id="why-armenia" class="hx-sec"><span class="hx-eye">Armenia</span><h2>Why Armenia works so well for Indian travellers</h2>'
             '<p class="hx-sub">Armenia is small, so the big sights are close together: from a base in Yerevan you reach Garni and Geghard, Khor Virap below Mount Ararat, and Lake Sevan as day trips, and a two-day loop adds Noravank and Tatev in the south. Distances are short, the pace is relaxed, and it pairs naturally with Georgia next door.</p>'
             '<div class="hx-facts">' + ''.join(f'<div class="hx-fact"><b>{a}</b><span>{b}</span></div>' for a, b in facts) + '</div></section>')
    h.append('<section id="armenia-in-photos" class="hx-sec"><span class="hx-eye">Real places</span><h2>Armenia in photos</h2>'
             '<p class="hx-sub">Garni Temple in winter snow, Republic Square at night, Lake Sevan, Geghard in the Azat valley, the Cascade in Yerevan, old Dilijan, Haghpat Monastery and the Jermuk waterfall. Real photos by Wikimedia Commons photographers, credited below.</p><div class="hx-pg">'
             + ''.join(f'<figure><img src="{U(k)}" alt="{A(k)}" width="800" height="600" loading="lazy" decoding="async"><figcaption>{C(k)}</figcaption></figure>' for k in GAL) + '</div></section>')
    cards = [('Families', 'Armenia with children', 'Short drives from one Yerevan hotel, open spaces at Garni and Lake Sevan, the Cascade steps and fountains, and family rooms in central hotels.'),
             ('Couples', 'Honeymoon in Armenia', 'Ararat views from Khor Virap, a quiet evening by Lake Sevan, leafy Dilijan and the Wings of Tatev cable car above the gorge.'),
             ('Snow lovers', 'Winter in Armenia', 'December to March: Garni and the hills under snow, a day on the slopes at Tsaghkadzor and warm cafes in Yerevan.'),
             ('Two countries', 'Armenia + Georgia', 'Yerevan and the monasteries, then north via Dilijan or Haghpat to Tbilisi and Kazbegi, with the paperwork for both countries planned together.')]
    stays = [('Yerevan centre', 'A central hotel near Republic Square or the Cascade keeps cafes, the Opera and evening walks close, with day trips leaving from the door.'),
             ('Dilijan', 'A forest-town stay in Dilijan breaks the trip north and puts Lake Sevan, Haghpat and the Georgia road within reach.'),
             ('Goris / Tatev area', 'One night in the south makes Noravank, the Wings of Tatev and Tatev Monastery an easy two-day loop.'),
             ('Tsaghkadzor', 'A mountain hotel in Tsaghkadzor suits winter snow trips and cooler summer nights, an hour from Yerevan.')]
    h.append('<section id="how-to-choose" class="hx-sec"><span class="hx-eye">How to choose</span><h2>Choose the Armenia trip that fits you</h2>'
             '<p class="hx-sub">Start from the kind of trip you want — we fine-tune the days, hotels, drivers and guides to your group.</p><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><span class="hx-tag">{t}</span><h3>{n}</h3><p>{d}</p></div>' for t, n, d in cards) + '</div>'
             '<h3 style="margin-top:30px">Where to stay</h3><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><h3>{n}</h3><p>{d}</p></div>' for n, d in stays) + '</div></section>')
    days = [('Day 1', 'Arrive in Yerevan', 'Airport pickup and hotel. An easy evening walk to Republic Square and up the Cascade steps for views over the city — and Ararat on a clear day.'),
            ('Day 2', 'Garni &amp; Geghard', 'Drive into the hills to the Garni Temple above its gorge, then Geghard Monastery, partly carved into the rock of the Azat valley. Back to Yerevan.'),
            ('Day 3', 'Lake Sevan &amp; Dilijan', 'North to Lake Sevan and the Sevanavank churches on the peninsula, then the forest town of Dilijan and its old quarter. Return to Yerevan.'),
            ('Day 4', 'Khor Virap &amp; Noravank', 'Khor Virap with Mount Ararat behind it, then the red cliffs of Noravank, and on south to Goris for the night.'),
            ('Day 5', 'Wings of Tatev', 'Ride the Wings of Tatev cable car across the gorge to Tatev Monastery, then the long scenic drive back to Yerevan.'),
            ('Day 6', 'Fly home', 'Free morning for shopping and a last coffee in Yerevan, then transfer to the airport — or carry on north to Georgia.')]
    h.append('<section id="sample-itinerary" class="hx-sec"><span class="hx-eye">Sample plan</span><h2>A sample 6-day Yerevan, Garni, Sevan &amp; Tatev itinerary</h2>'
             '<p class="hx-sub">The classic first trip to Armenia. We rebuild it around you — a shorter Yerevan-and-day-trips holiday, a winter snow trip, or three or four extra nights in Georgia.</p><div class="hx-itin">'
             + ''.join(f'<div class="hx-day"><i>{a}</i><b>{b}</b><p>{c}</p></div>' for a, b, c in days) + '</div></section>')
    seasons = [('May – Jun', '<span class="hx-ok">Best</span>', 'Mild, green', 'Green hills, wildflowers and comfortable days for Garni, Sevan and the drive to Tatev; Indian summer holidays fall here — book early.'),
               ('Sep – Oct', '<span class="hx-ok">Best</span>', 'Warm to mild', 'Settled weather, autumn colours around Dilijan and Jermuk, and harvest season in the wine villages near Noravank.'),
               ('Jul – Aug', '<span class="hx-mid">Hot</span>', 'Hot in Yerevan', 'Hot days in the city but pleasant at Lake Sevan and in the hills; we start sightseeing early and keep afternoons easy.'),
               ('Dec – Mar', '<span class="hx-ok">Snow</span>', 'Cold, snowy', 'Snow on Garni and the mountains and skiing at Tsaghkadzor; some high roads can close after snowfall, so we plan around the weather.'),
               ('Nov &amp; Apr', '<span class="hx-mid">Shoulder</span>', 'Changeable', 'Fewer visitors and good city days, but mountain weather can change quickly — we keep the plan flexible.')]
    h.append('<section id="when-to-go" class="hx-sec"><span class="hx-eye">Best season</span><h2>When to go to Armenia</h2>'
             '<p class="hx-sub">Armenia has warm, dry summers and cold, snowy winters, so spring and autumn are the easiest months, with winter good for snow lovers. We check the season, road conditions and flight prices against your plan before we quote.</p>'
             '<div class="hx-tw"><table class="hx-t"><thead><tr><th>Months</th><th>Verdict</th><th>Weather</th><th>What it means for your trip</th></tr></thead><tbody>'
             + ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in seasons) + '</tbody></table></div></section>')
    h.append('<section id="visa-and-entry" class="hx-sec"><span class="hx-eye">Visa &amp; entry</span><h2>Armenia visa for Indian passport holders</h2>'
             '<div class="hx-visa"><div class="hx-vbox"><h3>What the official rules say</h3><ul>'
             '<li>Indian ordinary passport holders <b>need a visa</b> for Armenia. The Ministry of Foreign Affairs <b>recommends the e-visa</b>, applied for on the official portal <b>evisa.mfa.am</b>, with a stated <b>processing time of three working days</b>.</li>'
             '<li>For the e-visa you need <b>travel (medical) insurance</b> plus <b>either</b> a valid visa or residence permit of the <b>EU/Schengen states, the USA, the UK, Canada, Australia, New Zealand, the Republic of Korea, Russia or Japan</b> (or a residence permit of the UAE, Saudi Arabia, Kuwait, Qatar, Bahrain or Oman), <b>or</b> a <b>return air ticket reservation</b>, an <b>invitation</b> from a party in Armenia (for example a local tourist agency) and <b>proof of funds</b> such as a 3-month bank statement.</li>'
             '<li>With such a valid visa or residence permit, a visa can also be obtained <b>at the Armenian border</b>; otherwise you can apply at an Armenian embassy.</li>'
             '<li><b>Temporary exemption:</b> from 1 July 2026 to 1 July 2027, Indians holding a <b>US, EU, Schengen, UAE, Bahrain, Qatar, Saudi, Kuwait or Oman residence permit</b> valid for at least six months from entry do not need a visa (up to 180 days in a year).</li>'
             '<li>Your <b>passport must be valid for the entire stay</b> in Armenia.</li></ul>'
             f'<p class="hx-checked">Checked {CHECKED} · sources: <a href="{SRC_MFA}" target="_blank" rel="noopener nofollow">Ministry of Foreign Affairs of Armenia — visa requirements (India, ordinary passport)</a> · <a href="{SRC_EVISA}" target="_blank" rel="noopener nofollow">Armenia e-visa portal</a> · <a href="{SRC_TVE}" target="_blank" rel="noopener nofollow">MFA list of countries for the temporary visa exemption</a></p></div>'
             '<div class="hx-vnote"><p><b>Please note:</b> whether a visa is issued, and admission at the border, is always the decision of the authorities of the Republic of Armenia. We help you prepare a complete, honest application, but we never promise an outcome we do not control.</p>'
             '<p>We share a document checklist that matches your itinerary, give you a day-by-day plan and hotel details, and confirm non-refundable bookings only after your e-visa is approved. If you add Georgia, we check its entry rules for you at the same time.</p></div></div></section>')
    inc = [('doc', 'E-visa guidance', 'A clear checklist for the Armenian e-visa (and Georgia&rsquo;s entry rules if you add it), matched to your trip.'), ('pin', 'Hotels', 'Named hotels in Yerevan, a night in the south for Tatev, and Dilijan or Tsaghkadzor where it suits you.'),
           ('team', 'Private car &amp; driver', 'Airport transfers and a private car with driver for Garni, Sevan, Khor Virap, Noravank and Tatev.'), ('globe', 'Guides &amp; tickets', 'English-speaking guides where useful, plus the Wings of Tatev cable car and entry tickets as chosen.'),
           ('food', 'Meal plan', 'Breakfast at most hotels; vegetarian and Jain needs noted in advance, with restaurant suggestions.'), ('award', 'Flights optional', 'Land-only, or a full package with international flights from your nearest Indian airport.')]
    h.append('<section id="whats-included" class="hx-sec"><span class="hx-eye">Your package</span><h2>What a Suzu Armenia package includes</h2><div class="hx-inc">'
             + ''.join(f'<div>{svg(i)}<span><b>{t}</b><span>{d}</span></span></div>' for i, t, d in inc) + '</div></section>')
    steps = [('chat', 'Tell us the basics', 'Dates, travellers and the kind of trip you want. A WhatsApp message is enough.'),
             ('doc', 'Get a costed itinerary', 'A day-by-day plan with named hotels and a clear per-person price, usually within 24 hours.'),
             ('sliders', 'Adjust until it fits', 'Change the days, hotels, car or the Georgia add-on. We re-quote as needed.'),
             ('lock', 'Confirm with a token', 'Lock your plan with a small token amount; the balance is paid later, as agreed in writing.')]
    h.append('<section id="how-booking-works" class="hx-sec"><span class="hx-eye">Simple process</span><h2>How booking works</h2><div class="hx-steps">'
             + ''.join(f'<div class="hx-step"><div class="hx-n">{svg(i)}</div><b>{t}</b><p>{d}</p></div>' for i, t, d in steps) + '</div></section>')
    h.append('<section id="armenia-faq" class="hx-sec"><span class="hx-eye">FAQ</span><h2>Common questions about an Armenia tour</h2><div class="hx-faqs">'
             + ''.join(f'<details class="hx-faq"{" open" if k == 0 else ""}><summary>{html.escape(q)}</summary><div class="hx-ans"><p>{html.escape(a)}</p></div></details>' for k, (q, a) in enumerate(FAQ)) + '</div></section>')
    h.append('<section id="more-destinations" class="hx-sec"><span class="hx-eye">Explore more</span><h2>Explore more destinations</h2>'
             '<p class="hx-sub">Every trip is planned the same way — your dates, your budget, one team from quote to return. <a href="https://suzutravels.com/international-tour-packages/">See all international holidays →</a></p><div class="hx-mini">'
             + ''.join(f'<a class="hx-mc" href="https://suzutravels.com/{p}/"><img src="https://suzutravels.com/wp-content/uploads/2026/10/{img}.webp" alt="{html.escape(n)} holiday — Suzu Travels" width="640" height="360" loading="lazy" decoding="async"><span><b>{html.escape(n)}</b><em>{html.escape(e)}</em></span></a>' for p, n, img, e in REL) + '</div></section>')
    h.append(f'<div class="hx-final"><img src="{U(FINAL)}" alt="{A(FINAL)}" width="1600" height="900" loading="lazy" decoding="async">'
             '<h2>Plan your Armenia trip</h2><p>Send us your dates and group size. We will come back with a costed, day-by-day Armenia itinerary you can compare, no obligation.</p>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Request an Armenia Quote {svg("arrow")}</a><a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div>'
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
    open('pages/armenia-tour-packages.html', 'w').write(o)
    print('pages/armenia-tour-packages.html', len(o))
