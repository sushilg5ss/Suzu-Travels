#!/usr/bin/env python3
"""Europe multi-country page (Paris, Switzerland, Italy) — .hx design system; same template as gen_japan.py.
Run from outbound-kit/:  python3 pages/gen_europe.py <PAGE_ID>  -> pages/europe-tour-packages.html (one line)
Facts: Schengen visa rules checked 23 Oct 2026 against official sources (European Commission Migration and Home Affairs
"Applying for a Schengen visa" + "Visa policy", Embassy of the Czech Republic in New Delhi, Swiss FDFA). No prices.
10-day itinerary grid = 5 columns on desktop.
"""
import json, html, sys, os
sys.path.insert(0, os.getcwd())
import gen_hub as G

PID = int(sys.argv[1]) if len(sys.argv) > 1 else 0
M = G.M
svg, WA_SVG, wa = G.svg, G.WA_SVG, G.wa
CHECKED = '23 October 2026'
SRC_EC = 'https://home-affairs.ec.europa.eu/policies/schengen/visa-policy/applying-schengen-visa_en'
SRC_EC2 = 'https://home-affairs.ec.europa.eu/policies/schengen/visa-policy_en'
SRC_CZ = 'https://mzv.gov.cz/newdelhi/en/ko/visa_information/schengen_visa_up_to_90_days/how_to_apply_for_a_visa_up_to_90_days.html'
SRC_CH = 'https://www.eda.admin.ch/countries/croatia/en/home/visa/entry-ch/up-90-days/documents-schengen.html'

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
body.page-id-PID .page-header:before{content:"Holidays abroad \00B7  Europe";display:inline-block;font:800 12px/1 "Plus Jakarta Sans",sans-serif;letter-spacing:.18em;text-transform:uppercase;color:#1a1606;background:#E2C158;padding:8px 13px;border-radius:999px;margin-bottom:16px}
body.page-id-PID .page-header .entry-title{color:#fff!important;font-family:"Sora","Plus Jakarta Sans",sans-serif!important;font-size:clamp(34px,4.2vw,58px)!important;line-height:1.06!important;letter-spacing:-.035em!important;margin:0!important;font-weight:800!important;max-width:15ch;text-shadow:0 2px 24px rgba(0,0,0,.35)}
@media(max-width:1100px){.hx .hx-cards{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-itin{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-visa{grid-template-columns:1fr}.hx .hx-inc,.hx .hx-steps{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:700px){body.page-id-PID .page-header{left:14px;right:14px;padding:26px 18px 0}body.page-id-PID .page-header:before{font-size:10.5px;padding:7px 11px;margin-bottom:12px}body.page-id-PID .page-header .entry-title{font-size:33px!important}.hx .hx-facts{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-pg{grid-template-columns:repeat(2,minmax(0,1fr));grid-auto-rows:150px}.hx .hx-pg figure:first-child{grid-column:span 2;grid-row:span 1}.hx .hx-pg figure:nth-child(4){grid-row:span 1}.hx .hx-pg figure:nth-child(8){display:none}.hx .hx-cards,.hx .hx-itin,.hx .hx-inc,.hx .hx-steps{grid-template-columns:1fr}.hx .hx-mini{grid-template-columns:repeat(2,minmax(0,1fr))}}
.hx .hx-pg p,.hx .hx-cards>p,.hx .hx-itin>p,.hx .hx-inc>p,.hx .hx-facts>p{display:none}
""".replace('PID', str(PID))
CSS = ' '.join(l.strip() for l in (base + EXTRA).strip().splitlines() if l.strip() and not l.strip().startswith('/*'))
HERO = ['europe', 'europe-2', 'europe-3', 'europe-5', 'europe-7', 'europe-1']
GAL = ['europe-1', 'europe-2', 'europe-4', 'europe-6', 'switzerland', 'europe-5', 'europe-7', 'europe-3']
CC = 'Europe'

FAQ = [
    ("Do Indians need a visa for a Europe tour?", "Yes. Indian passport holders need a Schengen short-stay visa for a holiday in France, Switzerland, Italy and the other Schengen countries. One Schengen visa covers the whole Schengen area for stays of up to 90 days in any 180-day period. You apply to the consulate of the country where you will spend the longest time (or, if the stays are equal, the country you enter first), between six months and 15 days before travel. The decision normally takes 15 days and can be extended to 45 days. Approval is always the decision of the issuing country."),
    ("Is one visa enough for Paris, Switzerland and Italy?", "Yes. France, Switzerland and Italy are all in the Schengen area, so one Schengen visa covers a Paris, Swiss Alps and Italy trip. The UK and Ireland are not part of Schengen and need their own separate visas, so adding London means a second visa application, which we plan for you."),
    ("How many days are enough for a Europe trip?", "Nine to eleven nights covers the classic first trip: Paris, Lucerne and the Jungfrau region in Switzerland, then Venice, Florence and Rome. Seven nights works well for Paris and Switzerland alone. With two weeks you can add Amsterdam, Austria or the Italian lakes at a calmer pace."),
    ("When is the best time to visit Europe from India?", "April to June and September to early October suit most Indian travellers — pleasant weather and long days. May and June are also the Indian school-holiday rush, so visa appointments and hotels fill early. July and August are hot in Italy and very busy everywhere. November to March is cold with snow in the Alps, short days and Christmas markets in December."),
    ("Is vegetarian food easy to find in Europe?", "Yes, with a little planning. Paris, Lucerne, Interlaken and Rome all have Indian restaurants, and Italian pizza, pasta and risotto have many vegetarian options. We note vegetarian and Jain needs with hotels and suggest restaurants for every day of your trip."),
    ("Is a Europe tour good for families and seniors?", "Very. Trains between Paris, Switzerland and Italy are comfortable, the Swiss mountain railways and cable cars make the Alps easy without hiking, and Disneyland Paris is a favourite with children. For seniors we keep hotel changes few, use private transfers with luggage, and avoid rushed early starts."),
    ("Why are there no prices on this page?", "Europe costs depend heavily on your dates (school holidays and summer cost more), hotel category, rail tickets, Swiss mountain excursions and the airfare from India. Instead of a teaser price that changes when you ask, we send a costed, day-by-day quote for your dates — usually within 24 hours."),
]

JS = ("(function(){var f=document.getElementById('hxPlan');if(!f){return;}f.addEventListener('submit',function(e){e.preventDefault();"
      "var d=f.querySelector('[name=d]').value,s=f.querySelector('[name=s]').value,m=f.querySelector('[name=m]').value,a=f.querySelector('[name=a]').value,k=f.querySelector('[name=k]').value,c=f.querySelector('[name=c]').value;"
      "var t='Hi Suzu Travels, please send me a costed Europe itinerary.\\nTrip: '+d+'\\nTrip type: '+s+'\\nTravel month: '+m+'\\nAdults: '+a+'\\nChildren: '+k;"
      "if(c){t=t+'\\nDeparting from: '+c;}"
      "window.open('https:'+String.fromCharCode(47,47)+'wa.me/917087488961?text='+encodeURIComponent(t),'_blank','noopener');});})();")

REL = [('dubai-tour-packages', 'Dubai', 'suzu-abroad-dubai', 'Burj Khalifa, desert, Abu Dhabi'), ('turkey-tour-packages', 'Turkey', 'suzu-abroad-turkey', 'Istanbul, Cappadocia, Pamukkale'),
       ('georgia-tour-packages', 'Georgia', 'suzu-abroad-georgia', 'Tbilisi, Kazbegi, Gudauri'), ('azerbaijan-tour-packages', 'Azerbaijan', 'suzu-abroad-azerbaijan', 'Baku, Gabala, Shahdag'),
       ('japan-tour-packages', 'Japan', 'suzu-abroad-japan', 'Tokyo, Fuji, Kyoto, Osaka'),
       ('nepal-tour-packages', 'Nepal', 'suzu-card-nepal', 'No visa for Indians'), ('bhutan-tour-packages', 'Bhutan', 'suzu-card-bhutan', 'Paro, Thimphu, Punakha'),
       ('sri-lanka-tour-packages', 'Sri Lanka', 'suzu-card-sri-lanka', 'Beaches & tea country'), ('maldives-tour-packages', 'Maldives', 'suzu-card-maldives', 'Overwater villas'),
       ('thailand-tour-packages', 'Thailand', 'suzu-card-thailand', 'Bangkok, Phuket, Krabi'), ('singapore-tour-packages', 'Singapore', 'suzu-card-singapore', 'City, Sentosa, Universal'),
       ('malaysia-tour-packages', 'Malaysia', 'suzu-card-malaysia', 'KL, Langkawi, Genting'), ('vietnam-tour-packages', 'Vietnam', 'suzu-card-vietnam', 'Hanoi, Ha Long, Hoi An'),
       ('bali-tour-packages', 'Bali', 'suzu-card-bali', 'Ubud, villas, temples')]

def build():
    W = "Hi Suzu Travels, I'm planning a Europe trip. Please share a quote."
    h = [f'<div class="suzu-intl hx hx-country"><style>{CSS}</style>']
    slides = ''.join(f'<div class="hx-slide"><img src="{U(s)}" alt="{A(s)}" width="1600" height="1000" {"fetchpriority=\"high\" loading=\"eager\"" if i == 0 else "loading=\"lazy\""} decoding="async"><span class="hx-cap">{C(s)}</span></div>' for i, s in enumerate(HERO))
    h.append('<section class="hx-hero" aria-label="Europe tour packages from India"><div class="hx-slides">' + slides + '</div><div class="hx-copy">'
             '<p class="hx-lede">The Eiffel Tower and the Louvre, Lucerne\'s Chapel Bridge, the snow of the Jungfrau region, the canals of Venice and the Colosseum in Rome — a first Europe trip is a dream holiday for Indian families and couples. We plan it to your dates, your budget and your pace, with honest Schengen visa guidance from the start.</p>'
             '<div class="hx-badges">'
             f'<span class="hx-badge">{svg("globe")}Paris, Swiss Alps &amp; Italy</span><span class="hx-badge">{svg("food")}Vegetarian meals planned</span>'
             f'<span class="hx-badge">{svg("team")}Families, couples &amp; groups</span><span class="hx-badge">{svg("doc")}Honest Schengen visa guidance</span></div>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Get a Europe Quote {svg("arrow")}</a>'
             f'<a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div></div>'
             '<form class="hx-plan" id="hxPlan" aria-label="Get a costed Europe itinerary on WhatsApp"><h3>Plan my Europe trip</h3>'
             '<p>Tell us the basics — we reply on WhatsApp with a costed, day-by-day plan, usually within 24 hours.</p><div class="hx-f">'
             '<label class="hx-full">Trip<select name="d"><option selected>Paris + Switzerland + Italy</option><option>Paris + Switzerland</option><option>Switzerland only</option><option>Italy only (Venice, Florence, Rome)</option><option>Paris + Amsterdam + Switzerland</option><option>Europe honeymoon</option><option>Europe with London (two visas)</option></select></label>'
             '<label>Trip type<select name="s"><option>Family</option><option>Honeymoon / couple</option><option>Friends</option><option>Seniors</option><option>Group</option><option>Corporate / MICE</option></select></label>'
             f'<label>Travel month<select name="m">{G.months()}</select></label>'
             '<label>Adults<select name="a"><option>1</option><option selected>2</option><option>3</option><option>4</option><option>5</option><option>6</option><option>7–10</option><option>11–20</option><option>20+</option></select></label>'
             '<label>Children<select name="k"><option>0</option><option>1</option><option>2</option><option>3</option><option>4+</option></select></label>'
             '<label class="hx-full">Departing from<input name="c" type="text" placeholder="e.g. Delhi, Mumbai, Chandigarh" autocomplete="address-level2"></label></div>'
             f'<button class="hx-btn" type="submit">{WA_SVG}Get my Europe plan on WhatsApp</button><small>Opens WhatsApp with your details filled in. We do not store anything on this page.</small></form></section>')
    h.append('<div class="hx-trust">'
             f'<div>{svg("clock")}<span><b>Quote in ~24 hours</b><span>Costed, day by day</span></span></div>'
             f'<div>{svg("doc")}<span><b>Honest visa guidance</b><span>Official rules, checked</span></span></div>'
             f'<div>{svg("shield")}<span><b>HP Tourism registered</b><span>Reg. DTO-MND-11-243/2022</span></span></div>'
             f'<div>{svg("chat")}<span><b>One team, start to finish</b><span>On WhatsApp while you travel</span></span></div></div>')
    h.append('<nav class="hx-toc" aria-label="On this page"><a href="#why-europe">Why Europe</a><a href="#europe-in-photos">Photos</a><a href="#how-to-choose">Choose your trip</a><a href="#sample-itinerary">Sample itinerary</a><a href="#when-to-go">When to go</a><a href="#visa-and-entry">Visa &amp; entry</a><a href="#whats-included">What\'s included</a><a href="#europe-faq">FAQ</a></nav>')
    facts = [('Getting there', 'Fly into Paris and home from Rome — we compare routes from your city'), ('Time difference', 'India is 4 hr 30 min ahead in winter, 3 hr 30 min in summer'), ('Currency', 'Euro (France, Italy); Swiss franc (Switzerland)'),
             ('Best season', 'April to June; September to early October'), ('Typical trip', '9 to 14 nights, three or four countries'), ('One visa', 'A Schengen visa covers France, Switzerland and Italy')]
    h.append('<section id="why-europe" class="hx-sec"><span class="hx-eye">Europe · Multi-country</span><h2>Why a multi-country Europe tour works so well from India</h2>'
             '<p class="hx-sub">Europe packs big cities, mountain scenery and old towns close together, joined by fast trains — so one trip can cover Paris, the Swiss Alps and Italy without long drives. Paris has the Eiffel Tower, the Louvre and a Seine cruise; in Switzerland, Lucerne\'s Chapel Bridge, Mount Titlis and the mountain railways of the Jungfrau region bring the snow close even in summer; Italy adds the canals of Venice, the cathedral of Florence and Rome\'s Colosseum. One Schengen visa covers all three countries — it just needs to be started early.</p>'
             '<div class="hx-facts">' + ''.join(f'<div class="hx-fact"><b>{a}</b><span>{b}</span></div>' for a, b in facts) + '</div></section>')
    h.append('<section id="europe-in-photos" class="hx-sec"><span class="hx-eye">Real places</span><h2>Europe in photos</h2>'
             '<p class="hx-sub">The Louvre in Paris, Lucerne\'s Chapel Bridge, the Jungfrau mountain railway, Florence Cathedral, the Lauterbrunnen valley, Venice\'s Grand Canal, the Colosseum and the Swiss Alps — the places on a classic Suzu Europe itinerary. Photos by Unsplash photographers, credited below.</p><div class="hx-pg">'
             + ''.join(f'<figure><img src="{U(k)}" alt="{A(k)}" width="800" height="600" loading="lazy" decoding="async"><figcaption>{C(k)}</figcaption></figure>' for k in GAL) + '</div></section>')
    cards = [('Couples', 'Honeymoon', 'Paris evenings by the Seine, a lake-view hotel in Lucerne or Interlaken, a gondola in Venice and slow dinners in Florence or Rome. Fewer hotel changes, more time together.'),
             ('First trip to Europe', 'Paris, Swiss Alps &amp; Italy', 'The classic first Europe tour in 9–11 nights — Paris, Lucerne, the Jungfrau region, Venice, Florence and Rome, linked by trains.'),
             ('Families &amp; seniors', 'Family holiday', 'Disneyland Paris, snow on Mount Titlis and the Jungfrau, private transfers with luggage, and an easy daily pace with rooms that fit a family.'),
             ('Groups', 'Groups &amp; corporate', 'Coaches with tour managers, group rail and mountain-excursion bookings, Indian meals and team dinners. Tell us the group size and we quote accordingly, including B2B for travel agents.')]
    stays = [('Central Paris', 'Near the Eiffel Tower, the Opera or the Latin Quarter, close to a metro station — the city is best seen on foot and by metro.'),
             ('Lucerne or Interlaken', 'Lucerne for the lake and Mount Titlis; Interlaken for the Jungfraujoch, Lauterbrunnen and Grindelwald. On longer trips we use both.'),
             ('Venice island or Mestre', 'One night on the island lets you see Venice after the day visitors leave; mainland Mestre is simpler with luggage.'),
             ('Central Florence &amp; Rome', 'Walkable centres near the main stations, so the Duomo, the Colosseum and the Trevi Fountain are a short walk away.')]
    h.append('<section id="how-to-choose" class="hx-sec"><span class="hx-eye">How to choose</span><h2>Choose the Europe trip that fits you</h2>'
             '<p class="hx-sub">Start from the kind of trip you want — we fine-tune the countries, hotels and pace to your group.</p><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><span class="hx-tag">{t}</span><h3>{n}</h3><p>{d}</p></div>' for t, n, d in cards) + '</div>'
             '<h3 style="margin-top:30px">Where to stay — it shapes your whole trip</h3><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><h3>{n}</h3><p>{d}</p></div>' for n, d in stays) + '</div></section>')
    days = [('Day 1', 'Arrive in Paris', 'Airport pickup and hotel check-in. An easy evening walk and your first look at the Eiffel Tower lit up after dark.'),
            ('Day 2', 'Paris highlights', 'The Eiffel Tower, the Louvre and its glass pyramid, the Champs-Élysées and the Arc de Triomphe, then a cruise on the Seine.'),
            ('Day 3', 'Paris your way', 'A day at Disneyland Paris, or the Palace of Versailles and Montmartre — planned around your group.'),
            ('Day 4', 'Train to Lucerne', 'A train to Switzerland and Lucerne. Evening walk across the Chapel Bridge and along the lake.'),
            ('Day 5', 'Mount Titlis', 'A day trip to Engelberg and the cable cars of Mount Titlis for snow, the glacier and views of the Alps.'),
            ('Day 6', 'Interlaken &amp; Jungfraujoch', 'On to Interlaken and the mountain railway to the Jungfraujoch, past Kleine Scheidegg, with the Lauterbrunnen valley on the way.'),
            ('Day 7', 'Into Italy — Venice', 'A scenic train ride south into Italy and on to Venice. Evening water-bus ride along the Grand Canal.'),
            ('Day 8', 'Venice to Florence', 'St Mark\'s Square and an optional gondola ride in the morning, then the train to Florence.'),
            ('Day 9', 'Florence to Rome', 'The Duomo and Giotto\'s bell tower in Florence, then the train to Rome and an evening at the Trevi Fountain.'),
            ('Day 10', 'Rome &amp; fly home', 'The Colosseum and the Roman Forum with a guide, then the transfer to Rome airport for your flight home.')]
    h.append('<section id="sample-itinerary" class="hx-sec"><span class="hx-eye">Sample plan</span><h2>A sample 10-day Paris, Switzerland &amp; Italy itinerary</h2>'
             '<p class="hx-sub">The classic first trip to Europe. We rebuild it around you — Amsterdam or Brussels after Paris, more nights in the Swiss Alps, Pisa or the Vatican in Italy, or London with a separate UK visa.</p><div class="hx-itin">'
             + ''.join(f'<div class="hx-day"><i>{a}</i><b>{b}</b><p>{c}</p></div>' for a, b, c in days) + '</div></section>')
    seasons = [('Apr – Jun', '<span class="hx-ok">Best</span>', 'Spring into early summer, long days', 'Green Alps, blossom and pleasant city weather. May and June are also the Indian school-holiday rush — visa appointments and hotels fill early, so start planning in winter.'),
               ('Jul – Aug', '<span class="hx-mid">Good with care</span>', 'Warm to hot', 'Peak season across Europe. Hot afternoons in Italy and the busiest weeks at the big sights; the Swiss mountains are at their most comfortable.'),
               ('Sep – Oct', '<span class="hx-ok">Best</span>', 'Mild, settling into autumn', 'Warm September days, thinner crowds after the summer holidays and autumn colours in the Alps. One of the best times for a first trip.'),
               ('Nov – Mar', '<span class="hx-mid">Winter</span>', 'Cold, snow in the Alps', 'Short days and cold weather, with snow in Switzerland and Christmas markets in December. Good value outside the holidays; some mountain excursions depend on the weather.')]
    h.append('<section id="when-to-go" class="hx-sec"><span class="hx-eye">Best season</span><h2>When to go to Europe</h2>'
             '<p class="hx-sub">Spring and early autumn suit most Indian travellers; summer is busiest; winter is for snow and Christmas markets. We check weather, holiday dates and visa appointment availability against your plan.</p>'
             '<div class="hx-tw"><table class="hx-t"><thead><tr><th>Months</th><th>Verdict</th><th>Weather</th><th>What it means for your trip</th></tr></thead><tbody>'
             + ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in seasons) + '</tbody></table></div></section>')
    h.append('<section id="visa-and-entry" class="hx-sec"><span class="hx-eye">Visa &amp; entry</span><h2>Schengen visa and entry for Indian passport holders</h2>'
             '<div class="hx-visa"><div class="hx-vbox"><h3>What the official rules say</h3><ul>'
             '<li>Indian passport holders <b>need a Schengen short-stay visa</b> for a holiday in France, Switzerland, Italy and the other Schengen countries. All Schengen countries apply the <b>same visa rules</b>, and a short-stay visa allows <b>up to 90 days in any 180-day period</b>.</li>'
             '<li>You apply to the <b>consulate of the country where you will spend the longest time</b>. If your stays are equal, you apply to the <b>country you will visit first</b>. In India, applications are made through the consulate\'s appointed visa application centre (for example, VFS Global for the Czech Republic).</li>'
             '<li>Apply <b>no earlier than 6 months</b> and <b>at least 15 days</b> before your trip. A decision normally takes <b>15 days</b> and <b>can be extended to up to 45 days</b> if more checks or documents are needed. <b>Fingerprints</b> are collected when you apply.</li>'
             '<li>You need <b>travel medical insurance</b> covering emergency medical care, hospitalisation and repatriation, and a <b>passport valid for at least 3 months after you leave</b> the Schengen area.</li>'
             '<li>Appointments drive the timeline, so we suggest starting <b>two to three months before travel</b> — earlier for May–June school-holiday dates. The UK and Ireland are not in Schengen and need separate visas.</li></ul>'
             f'<p class="hx-checked">Checked {CHECKED} · sources: <a href="{SRC_EC}" target="_blank" rel="noopener nofollow">European Commission — Applying for a Schengen visa</a> · <a href="{SRC_EC2}" target="_blank" rel="noopener nofollow">European Commission — Visa policy</a> · <a href="{SRC_CZ}" target="_blank" rel="noopener nofollow">Embassy of the Czech Republic in New Delhi — Schengen visa up to 90 days</a> · <a href="{SRC_CH}" target="_blank" rel="noopener nofollow">Swiss FDFA — Application for Schengen visa and procedure</a></p></div>'
             '<div class="hx-vnote"><p><b>Please note:</b> visa approval and entry at the border are always the decision of the authorities of the issuing country and the country you enter. We guide you through the documents and timelines honestly, but we never promise an outcome we do not control.</p>'
             '<p>Apply only through the official channel for your main destination\'s consulate, keep your hotel bookings, insurance and return ticket consistent with your application, and carry copies for the immigration desk.</p></div></div></section>')
    inc = [('doc', 'Visa guidance', 'A clear Schengen document checklist, a day-by-day itinerary and hotel confirmations that match your application, and help booking the appointment.'), ('pin', 'Hotels in the right area', 'Named hotels near the right stations in Paris, Lucerne or Interlaken, Venice, Florence and Rome.'),
           ('team', 'Transfers &amp; rail', 'Airport transfers, train tickets between countries and a Swiss travel pass where it saves money.'), ('globe', 'Sightseeing &amp; mountains', 'Eiffel Tower, Seine cruise, Mount Titlis, Jungfraujoch and guided Rome and Florence visits, plus Disneyland Paris if you want it.'),
           ('food', 'Meal plan', 'Breakfast as standard; vegetarian and Jain needs noted with hotels, plus Indian restaurant suggestions in each city.'), ('award', 'Flights optional', 'Land-only, or a full package with international flights from your nearest Indian airport.')]
    h.append('<section id="whats-included" class="hx-sec"><span class="hx-eye">Your package</span><h2>What a Suzu Europe package includes</h2><div class="hx-inc">'
             + ''.join(f'<div>{svg(i)}<span><b>{t}</b><span>{d}</span></span></div>' for i, t, d in inc) + '</div></section>')
    steps = [('chat', 'Tell us the basics', 'Dates, travellers and the countries you want to see. A WhatsApp message is enough.'),
             ('doc', 'Get a costed itinerary', 'A day-by-day plan with named hotels and a clear per-person price, usually within 24 hours.'),
             ('sliders', 'Adjust until it fits', 'Add Amsterdam or London, swap a city, upgrade a hotel, change the pace. We re-quote as needed.'),
             ('lock', 'Confirm with a token', 'Lock your rate with a small token amount; the balance is paid later, as agreed in writing.')]
    h.append('<section id="how-booking-works" class="hx-sec"><span class="hx-eye">Simple process</span><h2>How booking works</h2><div class="hx-steps">'
             + ''.join(f'<div class="hx-step"><div class="hx-n">{svg(i)}</div><b>{t}</b><p>{d}</p></div>' for i, t, d in steps) + '</div></section>')
    h.append('<section id="europe-faq" class="hx-sec"><span class="hx-eye">FAQ</span><h2>Common questions about a Europe tour</h2><div class="hx-faqs">'
             + ''.join(f'<details class="hx-faq"{" open" if k == 0 else ""}><summary>{html.escape(q)}</summary><div class="hx-ans"><p>{html.escape(a)}</p></div></details>' for k, (q, a) in enumerate(FAQ)) + '</div></section>')
    h.append('<section id="more-destinations" class="hx-sec"><span class="hx-eye">Explore more</span><h2>Explore more destinations</h2>'
             '<p class="hx-sub">Every trip is planned the same way — your dates, your budget, one team from quote to return. <a href="https://suzutravels.com/international-tour-packages/">See all international holidays →</a></p><div class="hx-mini">'
             + ''.join(f'<a class="hx-mc" href="https://suzutravels.com/{p}/"><img src="https://suzutravels.com/wp-content/uploads/2026/10/{img}.webp" alt="{html.escape(n)} holiday — Suzu Travels" width="640" height="360" loading="lazy" decoding="async"><span><b>{html.escape(n)}</b><em>{html.escape(e)}</em></span></a>' for p, n, img, e in REL) + '</div></section>')
    h.append(f'<div class="hx-final"><img src="{U("europe-2")}" alt="{A("europe-2")}" width="1600" height="900" loading="lazy" decoding="async">'
             '<h2>Plan your Europe trip</h2><p>Send us your dates and group size. We will come back with a costed, day-by-day Europe itinerary you can compare — no obligation.</p>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Request a Europe Quote {svg("arrow")}</a><a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div>'
             '<p class="hx-contact">Or call <strong>+91 70874 88961</strong> · <a href="mailto:info@suzutravels.com">info@suzutravels.com</a></p></div>')
    seen = []
    for k in HERO + GAL + ['europe-2']:
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
    open('pages/europe-tour-packages.html', 'w').write(o)
    print('pages/europe-tour-packages.html', len(o))
