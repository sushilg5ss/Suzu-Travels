#!/usr/bin/env python3
"""Australia & New Zealand page — .hx design; same template as gen_egypt.py.
Run from outbound-kit/:  python3 pages/gen_australia.py 16306 -> pages/australia-tour-packages.html (one line)
Facts checked 28 Oct 2026: Home Affairs Visitor visa (600) Tourist stream (apply outside Australia) page — outside Australia to apply and at decision; ImmiAccount; separate application per family member; enough money, genuine visitor, health + character; generally 3 months stay, up to 12; single or multiple entry; digital, no label; "Do not arrange to travel to Australia until we let you know, in writing"; processing-time guide only; India not on ETA (601) or eVisitor (651) eligible passport lists. Immigration NZ Visitor Visa page (passports from some countries must apply; high volumes over summer, apply early) + INZ 11223 Checklist for India (online or NZ VACs in India). No prices, no visa fees.
Keyword Planner IN 27 Oct 2026: "australia tour package from india" 720/mo (focus kw), "australia and new zealand tour packages from india" 260/mo.
"""
import json, html, sys, os
sys.path.insert(0, os.getcwd())
import gen_hub as G

PID = int(sys.argv[1]) if len(sys.argv) > 1 else 0
M = G.M
svg, WA_SVG, wa = G.svg, G.WA_SVG, G.wa
CHECKED = '28 October 2026'
SRC_AU = 'https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/visitor-600/tourist-stream-overseas'
SRC_ETA = 'https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/electronic-travel-authority-601'
SRC_NZ = 'https://www.immigration.govt.nz/visas/visitor-visa/'
SRC_NZIN = 'https://www.immigration.govt.nz/assets/inz/documents/checklists/india/inz-11223.pdf'

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
body.page-id-PID .page-header:before{content:"Holidays abroad \00B7  Australia \00B7  NZ";display:inline-block;font:800 12px/1 "Plus Jakarta Sans",sans-serif;letter-spacing:.18em;text-transform:uppercase;color:#1a1606;background:#E2C158;padding:8px 13px;border-radius:999px;margin-bottom:16px}
body.page-id-PID .page-header .entry-title{color:#fff!important;font-family:"Sora","Plus Jakarta Sans",sans-serif!important;font-size:clamp(34px,4.2vw,58px)!important;line-height:1.06!important;letter-spacing:-.035em!important;margin:0!important;font-weight:800!important;max-width:15ch;text-shadow:0 2px 24px rgba(0,0,0,.35)}
@media(max-width:1100px){.hx .hx-cards{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-itin{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-visa{grid-template-columns:1fr}.hx .hx-inc,.hx .hx-steps{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:700px){body.page-id-PID .page-header{left:14px;right:14px;padding:26px 18px 0}body.page-id-PID .page-header:before{font-size:10.5px;padding:7px 11px;margin-bottom:12px}body.page-id-PID .page-header .entry-title{font-size:33px!important}.hx .hx-facts{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-pg{grid-template-columns:repeat(2,minmax(0,1fr));grid-auto-rows:150px}.hx .hx-pg figure:first-child{grid-column:span 2;grid-row:span 1}.hx .hx-pg figure:nth-child(4){grid-row:span 1}.hx .hx-pg figure:nth-child(8){display:none}.hx .hx-cards,.hx .hx-itin,.hx .hx-inc,.hx .hx-steps{grid-template-columns:1fr}.hx .hx-mini{grid-template-columns:repeat(2,minmax(0,1fr))}}
.hx .hx-pg p,.hx .hx-cards>p,.hx .hx-itin>p,.hx .hx-inc>p,.hx .hx-facts>p{display:none}
""".replace('PID', str(PID))
CSS = ' '.join(l.strip() for l in (base + EXTRA).strip().splitlines() if l.strip() and not l.strip().startswith('/*'))
CSS = CSS + (' body.page-id-PID .page-header .entry-title{max-width:19ch;font-size:clamp(32px,3.6vw,52px)!important}'
              ' @media(max-width:700px){body.page-id-PID .page-header .entry-title{font-size:28px!important}}').replace('PID', str(PID))
HERO = ['australia-1', 'australia-2', 'australia-3', 'australia-4', 'australia-5', 'australia-6']
GAL = ['australia-7', 'australia-8', 'australia-9', 'australia-10', 'australia-11', 'australia-12', 'australia-13', 'australia-14']
FINAL = 'australia-15'
CC = 'Australia'

FAQ = [
    ("Do Indians need a visa for Australia?", "Yes. Indian passports are not on the eligible lists for Australia's ETA (subclass 601) or eVisitor (subclass 651), so the usual holiday visa is the Visitor visa (subclass 600) Tourist stream, applied for online in ImmiAccount while you are outside Australia. You show you are a genuine visitor with enough money for the trip, and you meet health and character requirements. The Department of Home Affairs decides each application and the stay it grants — generally 3 months. We help you prepare a complete, honest application but cannot promise an outcome. We checked these rules on 28 October 2026 and re-check them before every booking."),
    ("Do we need a separate visa for New Zealand?", "Yes. Australia and New Zealand are separate countries with separate visas. For New Zealand, Indian travellers apply for a New Zealand Visitor Visa — Immigration New Zealand publishes a visitor visa checklist specifically for India, and you can apply online or through the New Zealand Visa Application Centres in India. The decision is made by Immigration New Zealand. We plan the order of both applications so your dates stay safe."),
    ("How many days are enough for Australia?", "Eight to ten nights covers the classic first trip: Sydney and the Blue Mountains, the Gold Coast, and Melbourne with the Great Ocean Road. Add three or four nights for Cairns and the Great Barrier Reef, two nights for Uluru, or four to six nights for New Zealand's Queenstown and Milford Sound. Australia is large, so we use short domestic flights between cities."),
    ("Which is the best time to visit Australia from India?", "Australia is in the southern hemisphere, so its seasons are the opposite of India's. Spring (September to November) and autumn (March to May) are the most comfortable for Sydney, Melbourne and the Blue Mountains. December to February is summer and beach season, with Christmas and New Year as peak dates. June to August is winter — cool in Sydney, cold in Melbourne, and a good time for the tropical north and the outback."),
    ("Can we combine Australia and New Zealand in one trip?", "Yes, and many Indian families do. A common plan is eight to ten nights in Australia followed by four to six nights in New Zealand — Queenstown, Milford Sound and sometimes Auckland or Rotorua — with a flight across the Tasman Sea. We sequence the two visa applications and the flights so the trip works as one holiday."),
    ("Is vegetarian and Indian food easy to find in Australia and New Zealand?", "Yes. Sydney, Melbourne, the Gold Coast, Auckland and Queenstown all have Indian restaurants, and vegetarian options are common in cafes and restaurants. We note vegetarian and Jain needs with your hotels and tours in advance, and suggest a good Indian dinner stop on long touring days."),
    ("Why are there no prices on this page?", "Australia and New Zealand costs depend on your dates, school holidays, hotel category, domestic flights, tours such as the reef or Milford Sound, and the airfare from your city. Instead of a teaser price that changes when you ask, we send a costed, day-by-day quote for your dates — usually within 24 hours."),
]

JS = ("(function(){var f=document.getElementById('hxPlan');if(!f){return;}f.addEventListener('submit',function(e){e.preventDefault();"
      "var d=f.querySelector('[name=d]').value,s=f.querySelector('[name=s]').value,m=f.querySelector('[name=m]').value,a=f.querySelector('[name=a]').value,k=f.querySelector('[name=k]').value,c=f.querySelector('[name=c]').value;"
      "var t='Hi Suzu Travels, please send me a costed Australia / New Zealand itinerary.\\nTrip: '+d+'\\nTrip type: '+s+'\\nTravel month: '+m+'\\nAdults: '+a+'\\nChildren: '+k;"
      "if(c){t=t+'\\nDeparting from: '+c;}"
      "window.open('https:'+String.fromCharCode(47,47)+'wa.me/917087488961?text='+encodeURIComponent(t),'_blank','noopener');});})();")

REL = [('dubai-tour-packages', 'Dubai', 'suzu-abroad-dubai', 'Burj Khalifa, desert, Abu Dhabi'), ('europe-tour-packages', 'Europe', 'suzu-abroad-europe', 'Paris, Swiss Alps, Italy'),
       ('switzerland-tour-packages', 'Switzerland', 'suzu-abroad-switzerland', 'Lucerne, Jungfrau, Zermatt'), ('uk-tour-packages', 'UK', 'suzu-abroad-uk', 'London, Cotswolds, Scotland'),
       ('japan-tour-packages', 'Japan', 'suzu-abroad-japan', 'Tokyo, Fuji, Kyoto, Osaka'), ('mauritius-tour-packages', 'Mauritius', 'suzu-abroad-mauritius', 'Lagoons, Le Morne, island tours'),
       ('egypt-tour-packages', 'Egypt', 'suzu-abroad-egypt', 'Cairo, Nile cruise, Luxor'), ('uzbekistan-tour-packages', 'Uzbekistan', 'suzu-abroad-uzbekistan', 'Samarkand, Bukhara, Khiva'), ('turkey-tour-packages', 'Turkey', 'suzu-abroad-turkey', 'Istanbul, Cappadocia, Pamukkale'),
       ('georgia-tour-packages', 'Georgia', 'suzu-abroad-georgia', 'Tbilisi, Kazbegi, Gudauri'), ('azerbaijan-tour-packages', 'Azerbaijan', 'suzu-abroad-azerbaijan', 'Baku, Gabala, Shahdag'),
       ('maldives-tour-packages', 'Maldives', 'suzu-card-maldives', 'Overwater villas'), ('bali-tour-packages', 'Bali', 'suzu-card-bali', 'Ubud, villas, temples'),
       ('thailand-tour-packages', 'Thailand', 'suzu-card-thailand', 'Bangkok, Phuket, Krabi'), ('singapore-tour-packages', 'Singapore', 'suzu-card-singapore', 'City, Sentosa, Universal'),
       ('malaysia-tour-packages', 'Malaysia', 'suzu-card-malaysia', 'KL, Langkawi, Genting'), ('vietnam-tour-packages', 'Vietnam', 'suzu-card-vietnam', 'Hanoi, Ha Long, Hoi An'),
       ('sri-lanka-tour-packages', 'Sri Lanka', 'suzu-card-sri-lanka', 'Beaches & tea country'), ('nepal-tour-packages', 'Nepal', 'suzu-card-nepal', 'No visa for Indians'),
       ('bhutan-tour-packages', 'Bhutan', 'suzu-card-bhutan', 'Paro, Thimphu, Punakha')]

def build():
    W = "Hi Suzu Travels, I'm planning an Australia / New Zealand trip. Please share a quote."
    h = [f'<div class="suzu-intl hx hx-country"><style>{CSS}</style>']
    slides = ''.join(f'<div class="hx-slide"><img src="{U(s)}" alt="{A(s)}" width="1600" height="1000" {"fetchpriority=\"high\" loading=\"eager\"" if i == 0 else "loading=\"lazy\""} decoding="async"><span class="hx-cap">{C(s)}</span></div>' for i, s in enumerate(HERO))
    h.append('<section class="hx-hero" aria-label="Australia and New Zealand tour packages from India"><div class="hx-slides">' + slides + '</div><div class="hx-copy">'
             '<p class="hx-lede">The Opera House and Harbour Bridge in Sydney, the Blue Mountains, the beaches of the Gold Coast, Melbourne&rsquo;s laneways and the Twelve Apostles on the Great Ocean Road — then, if you like, the Great Barrier Reef, Uluru, or the lakes and fiords of New Zealand. We plan Australia and New Zealand to your dates, budget and pace, with good hotels, short domestic flights and honest visa guidance from the start.</p>'
             '<div class="hx-badges">'
             f'<span class="hx-badge">{svg("globe")}Sydney, Gold Coast &amp; Melbourne</span><span class="hx-badge">{svg("food")}Vegetarian meals planned</span>'
             f'<span class="hx-badge">{svg("team")}Families, couples &amp; groups</span><span class="hx-badge">{svg("doc")}Official visa rules, checked</span></div>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Get an Australia Quote {svg("arrow")}</a>'
             f'<a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div></div>'
             '<form class="hx-plan" id="hxPlan" aria-label="Get a costed Australia or New Zealand itinerary on WhatsApp"><h3>Plan my Australia trip</h3>'
             '<p>Tell us the basics — we reply on WhatsApp with a costed, day-by-day plan, usually within 24 hours.</p><div class="hx-f">'
             '<label class="hx-full">Trip<select name="d"><option selected>Sydney + Gold Coast + Melbourne</option><option>Australia + New Zealand</option><option>New Zealand only</option><option>Australia + Great Barrier Reef (Cairns)</option><option>Australia honeymoon</option><option>Australia family holiday</option><option>Not sure yet</option></select></label>'
             '<label>Trip type<select name="s"><option>Family</option><option>Honeymoon / couple</option><option>Friends</option><option>Seniors</option><option>Group</option><option>Corporate / MICE</option></select></label>'
             f'<label>Travel month<select name="m">{G.months()}</select></label>'
             '<label>Adults<select name="a"><option>1</option><option selected>2</option><option>3</option><option>4</option><option>5</option><option>6</option><option>7–10</option><option>11–20</option><option>20+</option></select></label>'
             '<label>Children<select name="k"><option>0</option><option>1</option><option>2</option><option>3</option><option>4+</option></select></label>'
             '<label class="hx-full">Departing from<input name="c" type="text" placeholder="e.g. Delhi, Mumbai, Chandigarh" autocomplete="address-level2"></label></div>'
             f'<button class="hx-btn" type="submit">{WA_SVG}Get my Australia plan on WhatsApp</button><small>Opens WhatsApp with your details filled in. We do not store anything on this page.</small></form></section>')
    h.append('<div class="hx-trust">'
             f'<div>{svg("clock")}<span><b>Quote in ~24 hours</b><span>Costed, day by day</span></span></div>'
             f'<div>{svg("doc")}<span><b>Honest visa guidance</b><span>Home Affairs &amp; Immigration NZ rules, checked</span></span></div>'
             f'<div>{svg("shield")}<span><b>HP Tourism registered</b><span>Reg. DTO-MND-11-243/2022</span></span></div>'
             f'<div>{svg("chat")}<span><b>One team, start to finish</b><span>On WhatsApp while you travel</span></span></div></div>')
    h.append('<nav class="hx-toc" aria-label="On this page"><a href="#why-australia">Why Australia</a><a href="#australia-in-photos">Photos</a><a href="#how-to-choose">Choose your trip</a><a href="#sample-itinerary">Sample itinerary</a><a href="#when-to-go">When to go</a><a href="#visa-and-entry">Visa</a><a href="#whats-included">What\'s included</a><a href="#australia-faq">FAQ</a></nav>')
    facts = [('Getting there', 'Fly into Sydney or Melbourne; we compare routes and connections from your city'), ('Time difference', 'Sydney &amp; Melbourne are 4 hr 30 min ahead of India (5 hr 30 min in their summer); New Zealand 6 hr 30 min (7 hr 30 min in summer)'), ('Currency', 'Australian dollar (AUD); New Zealand dollar (NZD)'),
             ('Best season', 'September to November and March to May — seasons are the reverse of India&rsquo;s'), ('Typical trip', '8 to 10 nights in Australia; 12 to 16 with New Zealand'), ('Visa', 'Visa needed for both; Australia Visitor visa (subclass 600) and NZ Visitor Visa, applied separately')]
    h.append('<section id="why-australia" class="hx-sec"><span class="hx-eye">Australia &amp; New Zealand</span><h2>Why Australia works so well for Indian travellers</h2>'
             '<p class="hx-sub">Australia gives you world-famous cities and big nature in one trip: Sydney&rsquo;s harbour, Bondi and the Blue Mountains, the theme parks and beaches of the Gold Coast, Melbourne&rsquo;s food and the Great Ocean Road, and — with a few more days — the Great Barrier Reef from Cairns or the red centre at Uluru. English is spoken everywhere, roads and tours are well organised, Indian food is easy to find, and New Zealand&rsquo;s Queenstown and Milford Sound are a short flight away.</p>'
             '<div class="hx-facts">' + ''.join(f'<div class="hx-fact"><b>{a}</b><span>{b}</span></div>' for a, b in facts) + '</div></section>')
    h.append('<section id="australia-in-photos" class="hx-sec"><span class="hx-eye">Real places</span><h2>Australia &amp; New Zealand in photos</h2>'
             '<p class="hx-sub">Sydney Harbour from the air, Flinders Street Station in Melbourne, the Three Sisters in the Blue Mountains, the Twelve Apostles on the Great Ocean Road, the Great Barrier Reef, the ocean pool at Bondi, Milford Sound in New Zealand and a kangaroo. Photos by Unsplash photographers, credited below.</p><div class="hx-pg">'
             + ''.join(f'<figure><img src="{U(k)}" alt="{A(k)}" width="800" height="600" loading="lazy" decoding="async"><figcaption>{C(k)}</figcaption></figure>' for k in GAL) + '</div></section>')
    cards = [('Families', 'Australia with children', 'Gold Coast theme parks and beaches, wildlife parks with kangaroos and koalas, the Sydney ferries and an easy pace with family rooms and short flights.'),
             ('Couples', 'Honeymoon &amp; romance', 'A harbour-view hotel in Sydney, sunset on the Great Ocean Road, a day on the reef or at Whitehaven Beach, and a few days in Queenstown.'),
             ('Seniors', 'Easy Australia holiday', 'Short domestic flights instead of long drives, guided day tours, private transfers, step-free hotels where possible and vegetarian meals arranged.'),
             ('Nature', 'Reef, outback &amp; fiords', 'Cairns and the Great Barrier Reef, Uluru in the red centre, the Whitsunday Islands, or New Zealand&rsquo;s lakes, mountains and Milford Sound.')]
    stays = [('Sydney', 'A hotel near Circular Quay or Darling Harbour keeps the Opera House, ferries and harbour cruises a short walk away.'),
             ('Gold Coast', 'Surfers Paradise or Broadbeach for the beach, with the theme parks a short drive inland.'),
             ('Melbourne', 'The city centre (CBD) or Southbank for trams, laneways and the start of the Great Ocean Road day trip.'),
             ('New Zealand', 'Queenstown on Lake Wakatipu for Milford Sound and the mountains; Auckland or Rotorua for the North Island.')]
    h.append('<section id="how-to-choose" class="hx-sec"><span class="hx-eye">How to choose</span><h2>Choose the Australia trip that fits you</h2>'
             '<p class="hx-sub">Start from the kind of trip you want — we fine-tune the cities, hotels, flights and tours to your group.</p><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><span class="hx-tag">{t}</span><h3>{n}</h3><p>{d}</p></div>' for t, n, d in cards) + '</div>'
             '<h3 style="margin-top:30px">Where to stay</h3><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><h3>{n}</h3><p>{d}</p></div>' for n, d in stays) + '</div></section>')
    days = [('Day 1', 'Arrive in Sydney', 'Airport pickup and transfer to your hotel. An easy evening walk around Circular Quay and the Opera House.'),
            ('Day 2', 'Sydney city &amp; harbour', 'The Opera House, the Harbour Bridge, The Rocks and a harbour cruise, then Bondi Beach in the afternoon.'),
            ('Day 3', 'Blue Mountains', 'A day trip to the Three Sisters at Echo Point and the Blue Mountains lookouts, with a wildlife park stop on the way.'),
            ('Day 4', 'Fly to the Gold Coast', 'A short flight north. Check in near the beach and spend the evening at Surfers Paradise.'),
            ('Day 5', 'Gold Coast', 'A theme park day or a beach and wildlife day — we match it to your group and your children&rsquo;s ages.'),
            ('Day 6', 'Fly to Melbourne', 'Melbourne&rsquo;s laneways, Federation Square and Flinders Street Station, by tram and on foot.'),
            ('Day 7', 'Great Ocean Road', 'A full-day drive along the coast to the Twelve Apostles and back, stopping at beaches and lookouts.'),
            ('Day 8', 'Fly home — or on to New Zealand', 'Fly home from Melbourne, or cross to Queenstown for four to six nights with a Milford Sound day.')]
    h.append('<section id="sample-itinerary" class="hx-sec"><span class="hx-eye">Sample plan</span><h2>A sample 8-day Sydney, Gold Coast &amp; Melbourne itinerary</h2>'
             '<p class="hx-sub">The classic first trip to Australia. We rebuild it around you — Cairns and the reef, two nights at Uluru, an extra city day, or New Zealand at the end.</p><div class="hx-itin">'
             + ''.join(f'<div class="hx-day"><i>{a}</i><b>{b}</b><p>{c}</p></div>' for a, b, c in days) + '</div></section>')
    seasons = [('Sep – Nov', '<span class="hx-ok">Best</span>', 'Spring, mild and fresh', 'Comfortable for Sydney, the Blue Mountains, Melbourne and the Great Ocean Road. A favourite window for Indian travellers around Dussehra and Diwali — book early.'),
               ('Dec – Feb', '<span class="hx-mid">Peak</span>', 'Summer, warm to hot', 'Beach season on the Gold Coast and at Bondi, long daylight, and Christmas and New Year as peak dates. The tropical north around Cairns is in its wet season.'),
               ('Mar – May', '<span class="hx-ok">Best</span>', 'Autumn, mild', 'Pleasant across Sydney and Melbourne and good for touring; New Zealand has autumn colours around Queenstown.'),
               ('Jun – Aug', '<span class="hx-ok">Good</span>', 'Winter, cool to cold', 'Cool in Sydney and cold in Melbourne, but a good time for Cairns, the reef and the outback. Queenstown is in its snow and ski season.')]
    h.append('<section id="when-to-go" class="hx-sec"><span class="hx-eye">Best season</span><h2>When to go to Australia &amp; New Zealand</h2>'
             '<p class="hx-sub">Australia and New Zealand are in the southern hemisphere, so their seasons are the opposite of India&rsquo;s. We check the season, school holidays, event dates and flight prices against your plan before we quote.</p>'
             '<div class="hx-tw"><table class="hx-t"><thead><tr><th>Months</th><th>Verdict</th><th>Weather</th><th>What it means for your trip</th></tr></thead><tbody>'
             + ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in seasons) + '</tbody></table></div></section>')
    h.append('<section id="visa-and-entry" class="hx-sec"><span class="hx-eye">Visa &amp; entry</span><h2>Australia &amp; New Zealand visa for Indian passport holders</h2>'
             '<div class="hx-visa"><div class="hx-vbox"><h3>Australia — what the official rules say</h3><ul>'
             '<li>Indian passports are <b>not on the eligible lists for Australia&rsquo;s ETA (subclass 601) or eVisitor (subclass 651)</b>, so the usual holiday visa is the <b>Visitor visa (subclass 600) Tourist stream</b>.</li>'
             '<li>You apply <b>online in ImmiAccount</b> and must be <b>outside Australia when you apply and when the visa is decided</b>. Each family member submits a separate application.</li>'
             '<li>You must have <b>enough money for your stay</b>, be a <b>genuine visitor</b> and meet <b>health and character requirements</b>. Home Affairs suggests evidence such as 3 months of bank statements, pay slips and proof of reasons to return home. You may be asked for biometrics or health checks.</li>'
             '<li>Home Affairs decides the length of stay case by case — <b>generally 3 months</b>, up to 12 months in certain circumstances — and grants single or multiple entry. The visa is linked to your passport digitally; there is no label.</li>'
             '<li>Home Affairs says: <b>do not arrange to travel to Australia until you are told in writing that the visa is granted</b>. It publishes a processing-time guide only, so no fixed time is promised here.</li></ul>'
             '<h3 style="margin-top:18px">New Zealand — separate visa</h3><ul>'
             '<li>New Zealand needs its own <b>Visitor Visa</b>. Immigration New Zealand publishes a <b>visitor visa checklist for India</b>; you apply online, or at the New Zealand Visa Application Centres in India.</li>'
             '<li>You show funds for your stay, onward or return travel and that you are a genuine visitor. Immigration New Zealand advises applying early, as it receives high volumes of visitor visa applications over summer, especially for Christmas.</li></ul>'
             f'<p class="hx-checked">Checked {CHECKED} · sources: <a href="{SRC_AU}" target="_blank" rel="noopener nofollow">Department of Home Affairs — Visitor visa (subclass 600) Tourist stream</a> · <a href="{SRC_ETA}" target="_blank" rel="noopener nofollow">Home Affairs — ETA eligible passports</a> · <a href="{SRC_NZ}" target="_blank" rel="noopener nofollow">Immigration New Zealand — Visitor Visa</a> · <a href="{SRC_NZIN}" target="_blank" rel="noopener nofollow">INZ checklist for India</a></p></div>'
             '<div class="hx-vnote"><p><b>Please note:</b> whether a visa is granted, for how long, and whether you are admitted at the border, is always the decision of the Australian Department of Home Affairs and Immigration New Zealand. We help you prepare a complete, honest application, but we never promise an outcome we do not control.</p>'
             '<p>We share a document checklist that matches your itinerary, give you a day-by-day plan and hotel details for the application, and confirm non-refundable bookings only after your visa is granted.</p></div></div></section>')
    inc = [('doc', 'Visa guidance', 'A clear checklist for the Australian and New Zealand visitor visas, with an itinerary and hotel details that match your application.'), ('pin', 'Hotels', 'Named hotels in Sydney, the Gold Coast and Melbourne — and Queenstown or Auckland if you add New Zealand.'),
           ('team', 'Flights &amp; transfers', 'Airport transfers and domestic flights such as Sydney–Gold Coast and Gold Coast–Melbourne, booked to fit your plan.'), ('globe', 'Tours &amp; tickets', 'Harbour cruise, Blue Mountains and Great Ocean Road day tours, theme park or wildlife park tickets, and reef or Milford Sound trips as chosen.'),
           ('food', 'Meal plan', 'Breakfast at most hotels; vegetarian and Jain needs noted in advance, with Indian dinner suggestions on touring days.'), ('award', 'Flights optional', 'Land-only, or a full package with international flights from your nearest Indian airport.')]
    h.append('<section id="whats-included" class="hx-sec"><span class="hx-eye">Your package</span><h2>What a Suzu Australia package includes</h2><div class="hx-inc">'
             + ''.join(f'<div>{svg(i)}<span><b>{t}</b><span>{d}</span></span></div>' for i, t, d in inc) + '</div></section>')
    steps = [('chat', 'Tell us the basics', 'Dates, travellers and the kind of trip you want. A WhatsApp message is enough.'),
             ('doc', 'Get a costed itinerary', 'A day-by-day plan with named hotels and a clear per-person price, usually within 24 hours.'),
             ('sliders', 'Adjust until it fits', 'Change the cities, hotels, tours or flights. We re-quote as needed.'),
             ('lock', 'Confirm with a token', 'Lock your plan with a small token amount; the balance is paid later, as agreed in writing.')]
    h.append('<section id="how-booking-works" class="hx-sec"><span class="hx-eye">Simple process</span><h2>How booking works</h2><div class="hx-steps">'
             + ''.join(f'<div class="hx-step"><div class="hx-n">{svg(i)}</div><b>{t}</b><p>{d}</p></div>' for i, t, d in steps) + '</div></section>')
    h.append('<section id="australia-faq" class="hx-sec"><span class="hx-eye">FAQ</span><h2>Common questions about an Australia tour</h2><div class="hx-faqs">'
             + ''.join(f'<details class="hx-faq"{" open" if k == 0 else ""}><summary>{html.escape(q)}</summary><div class="hx-ans"><p>{html.escape(a)}</p></div></details>' for k, (q, a) in enumerate(FAQ)) + '</div></section>')
    h.append('<section id="more-destinations" class="hx-sec"><span class="hx-eye">Explore more</span><h2>Explore more destinations</h2>'
             '<p class="hx-sub">Every trip is planned the same way — your dates, your budget, one team from quote to return. <a href="https://suzutravels.com/international-tour-packages/">See all international holidays →</a></p><div class="hx-mini">'
             + ''.join(f'<a class="hx-mc" href="https://suzutravels.com/{p}/"><img src="https://suzutravels.com/wp-content/uploads/2026/10/{img}.webp" alt="{html.escape(n)} holiday — Suzu Travels" width="640" height="360" loading="lazy" decoding="async"><span><b>{html.escape(n)}</b><em>{html.escape(e)}</em></span></a>' for p, n, img, e in REL) + '</div></section>')
    h.append(f'<div class="hx-final"><img src="{U(FINAL)}" alt="{A(FINAL)}" width="1600" height="900" loading="lazy" decoding="async">'
             '<h2>Plan your Australia trip</h2><p>Send us your dates and group size. We will come back with a costed, day-by-day Australia — or Australia and New Zealand — itinerary you can compare, no obligation.</p>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Request an Australia Quote {svg("arrow")}</a><a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div>'
             '<p class="hx-contact">Or call <strong>+91 70874 88961</strong> · <a href="mailto:info@suzutravels.com">info@suzutravels.com</a></p></div>')
    seen = []
    for k in HERO + GAL + [FINAL]:
        v = M[k]
        if (v['credit'], v['src']) not in seen:
            seen.append((v['credit'], v['src']))
    h.append('<details class="hx-credits"><summary>Photo credits</summary><p>' + ' · '.join(f'<a href="{html.escape(s, quote=True)}" rel="nofollow noopener" target="_blank">{html.escape(c)}</a> (Unsplash License)' for c, s in seen) + '</p></details>')
    ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}
    h.append('<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + '</script><script>' + JS + '</script></div>')
    out = ''.join(h)
    assert '\n' not in out.replace('\\n', '')
    js = out[out.rfind('<script>'):]
    assert '&' not in js and '//' not in js
    return out

if __name__ == '__main__':
    o = build()
    open('pages/australia-tour-packages.html', 'w').write(o)
    print('pages/australia-tour-packages.html', len(o))
