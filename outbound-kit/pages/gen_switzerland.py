#!/usr/bin/env python3
"""Switzerland page — .hx design system; same template as gen_europe.py / gen_japan.py.
Run from outbound-kit/:  python3 pages/gen_switzerland.py <PAGE_ID>  -> pages/switzerland-tour-packages.html (one line)
Facts: Embassy of Switzerland in India visa page checked 24 Oct 2026 (VFS Global, processed in New Delhi, not earlier than
6 months, normally 10-15 working days, 6-month residence in India); Schengen-wide rules as checked 23 Oct 2026 (European
Commission Migration and Home Affairs). No prices. 8-day itinerary grid = 4 columns on desktop.
"""
import json, html, sys, os
sys.path.insert(0, os.getcwd())
import gen_hub as G

PID = int(sys.argv[1]) if len(sys.argv) > 1 else 0
M = G.M
svg, WA_SVG, wa = G.svg, G.WA_SVG, G.wa
CHECKED = '24 October 2026'
SRC_CHE = 'https://www.schweiz-indien.eda.admin.ch/en/visa-entry-to-and-residence-in-switzerland'
SRC_CHE2 = 'https://www.schweiz-indien.eda.admin.ch/en/schengen-visa'
SRC_EC = 'https://home-affairs.ec.europa.eu/policies/schengen/visa-policy/applying-schengen-visa_en'

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
body.page-id-PID .page-header:before{content:"Holidays abroad \00B7  Switzerland";display:inline-block;font:800 12px/1 "Plus Jakarta Sans",sans-serif;letter-spacing:.18em;text-transform:uppercase;color:#1a1606;background:#E2C158;padding:8px 13px;border-radius:999px;margin-bottom:16px}
body.page-id-PID .page-header .entry-title{color:#fff!important;font-family:"Sora","Plus Jakarta Sans",sans-serif!important;font-size:clamp(34px,4.2vw,58px)!important;line-height:1.06!important;letter-spacing:-.035em!important;margin:0!important;font-weight:800!important;max-width:15ch;text-shadow:0 2px 24px rgba(0,0,0,.35)}
@media(max-width:1100px){.hx .hx-cards{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-itin{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-visa{grid-template-columns:1fr}.hx .hx-inc,.hx .hx-steps{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:700px){body.page-id-PID .page-header{left:14px;right:14px;padding:26px 18px 0}body.page-id-PID .page-header:before{font-size:10.5px;padding:7px 11px;margin-bottom:12px}body.page-id-PID .page-header .entry-title{font-size:33px!important}.hx .hx-facts{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-pg{grid-template-columns:repeat(2,minmax(0,1fr));grid-auto-rows:150px}.hx .hx-pg figure:first-child{grid-column:span 2;grid-row:span 1}.hx .hx-pg figure:nth-child(4){grid-row:span 1}.hx .hx-pg figure:nth-child(8){display:none}.hx .hx-cards,.hx .hx-itin,.hx .hx-inc,.hx .hx-steps{grid-template-columns:1fr}.hx .hx-mini{grid-template-columns:repeat(2,minmax(0,1fr))}}
.hx .hx-pg p,.hx .hx-cards>p,.hx .hx-itin>p,.hx .hx-inc>p,.hx .hx-facts>p{display:none}
""".replace('PID', str(PID))
CSS = ' '.join(l.strip() for l in (base + EXTRA).strip().splitlines() if l.strip() and not l.strip().startswith('/*'))
HERO = ['switzerland-1', 'europe-2', 'switzerland-4', 'switzerland-6', 'switzerland-5', 'switzerland']
GAL = ['switzerland-2', 'europe-2', 'switzerland-4', 'switzerland-1', 'europe-4', 'switzerland-5', 'switzerland-7', 'switzerland-6']
CC = 'Switzerland'

FAQ = [
    ("Do Indians need a visa for Switzerland?", "Yes. Switzerland is part of the Schengen area, so Indian passport holders need a Schengen short-stay visa for a holiday. If Switzerland is your main destination, you apply to Switzerland: in India, applications are submitted at VFS Global centres and processed by the Embassy of Switzerland in New Delhi, normally in 10 to 15 working days after they reach the Embassy. You can apply no earlier than six months before your trip. Approval is always the decision of the Swiss authorities."),
    ("How many days are enough for Switzerland?", "Seven to eight nights covers the classic first trip: Lucerne and Mount Titlis, Interlaken and the Jungfraujoch, then Zermatt and the Matterhorn. Five nights works for Lucerne and Interlaken alone. With ten nights or more you can add the Glacier Express or Bernina Express, Lake Geneva and Montreux, or a few days in Paris or Italy on the same Schengen visa."),
    ("Which is the best time to visit Switzerland from India?", "June to September is the classic season — green valleys, long days and every mountain railway and cable car running. December to March is for snow, skiing and winter villages. April–May and October are quieter shoulder months with lower demand, but some mountain lifts close for maintenance between seasons, so we check each excursion against your dates."),
    ("What is the Swiss Travel Pass and do I need it?", "It is a rail pass for visitors that covers most trains, buses and lake boats in Switzerland for a set number of days and gives discounts on many mountain railways and cable cars. Whether it saves money depends on your route, so we compare the pass with point-to-point tickets for your exact itinerary before we book."),
    ("Is Switzerland good for a honeymoon?", "It is one of the most popular honeymoon destinations for Indian couples: lake-view hotels in Lucerne or Interlaken, the car-free mountain village of Zermatt under the Matterhorn, panoramic train journeys and snow at the Jungfraujoch even in summer. We keep hotel changes few and add special touches when you tell us the occasion."),
    ("Is vegetarian food easy to find in Switzerland?", "Yes. Lucerne, Interlaken, Zurich, Geneva and even Zermatt have Indian restaurants, and Swiss cheese fondue, rösti and Italian dishes have vegetarian options. We note vegetarian and Jain needs with hotels and suggest restaurants for every stop."),
    ("Why are there no prices on this page?", "Switzerland costs depend heavily on your dates, hotel category and location, the rail pass or tickets, mountain excursions such as the Jungfraujoch and Mount Titlis, and the airfare from India. Instead of a teaser price that changes when you ask, we send a costed, day-by-day quote for your dates — usually within 24 hours."),
]

JS = ("(function(){var f=document.getElementById('hxPlan');if(!f){return;}f.addEventListener('submit',function(e){e.preventDefault();"
      "var d=f.querySelector('[name=d]').value,s=f.querySelector('[name=s]').value,m=f.querySelector('[name=m]').value,a=f.querySelector('[name=a]').value,k=f.querySelector('[name=k]').value,c=f.querySelector('[name=c]').value;"
      "var t='Hi Suzu Travels, please send me a costed Switzerland itinerary.\\nTrip: '+d+'\\nTrip type: '+s+'\\nTravel month: '+m+'\\nAdults: '+a+'\\nChildren: '+k;"
      "if(c){t=t+'\\nDeparting from: '+c;}"
      "window.open('https:'+String.fromCharCode(47,47)+'wa.me/917087488961?text='+encodeURIComponent(t),'_blank','noopener');});})();")

REL = [('europe-tour-packages', 'Europe', 'suzu-abroad-europe', 'Paris, Swiss Alps, Italy'), ('dubai-tour-packages', 'Dubai', 'suzu-abroad-dubai', 'Burj Khalifa, desert, Abu Dhabi'), ('turkey-tour-packages', 'Turkey', 'suzu-abroad-turkey', 'Istanbul, Cappadocia, Pamukkale'),
       ('georgia-tour-packages', 'Georgia', 'suzu-abroad-georgia', 'Tbilisi, Kazbegi, Gudauri'), ('azerbaijan-tour-packages', 'Azerbaijan', 'suzu-abroad-azerbaijan', 'Baku, Gabala, Shahdag'),
       ('japan-tour-packages', 'Japan', 'suzu-abroad-japan', 'Tokyo, Fuji, Kyoto, Osaka'),
       ('nepal-tour-packages', 'Nepal', 'suzu-card-nepal', 'No visa for Indians'), ('bhutan-tour-packages', 'Bhutan', 'suzu-card-bhutan', 'Paro, Thimphu, Punakha'),
       ('sri-lanka-tour-packages', 'Sri Lanka', 'suzu-card-sri-lanka', 'Beaches & tea country'), ('maldives-tour-packages', 'Maldives', 'suzu-card-maldives', 'Overwater villas'),
       ('thailand-tour-packages', 'Thailand', 'suzu-card-thailand', 'Bangkok, Phuket, Krabi'), ('singapore-tour-packages', 'Singapore', 'suzu-card-singapore', 'City, Sentosa, Universal'),
       ('malaysia-tour-packages', 'Malaysia', 'suzu-card-malaysia', 'KL, Langkawi, Genting'), ('vietnam-tour-packages', 'Vietnam', 'suzu-card-vietnam', 'Hanoi, Ha Long, Hoi An'),
       ('bali-tour-packages', 'Bali', 'suzu-card-bali', 'Ubud, villas, temples')]

def build():
    W = "Hi Suzu Travels, I'm planning a Switzerland trip. Please share a quote."
    h = [f'<div class="suzu-intl hx hx-country"><style>{CSS}</style>']
    slides = ''.join(f'<div class="hx-slide"><img src="{U(s)}" alt="{A(s)}" width="1600" height="1000" {"fetchpriority=\"high\" loading=\"eager\"" if i == 0 else "loading=\"lazy\""} decoding="async"><span class="hx-cap">{C(s)}</span></div>' for i, s in enumerate(HERO))
    h.append('<section class="hx-hero" aria-label="Switzerland tour packages from India"><div class="hx-slides">' + slides + '</div><div class="hx-copy">'
             '<p class="hx-lede">The Matterhorn above car-free Zermatt, Lucerne\'s Chapel Bridge, snow at the Jungfraujoch and red trains winding past glaciers — Switzerland is the dream holiday for Indian couples and families. We plan it to your dates, budget and pace, with the right rail pass and honest Schengen visa guidance from the start.</p>'
             '<div class="hx-badges">'
             f'<span class="hx-badge">{svg("globe")}Lucerne, Interlaken &amp; Zermatt</span><span class="hx-badge">{svg("food")}Vegetarian meals planned</span>'
             f'<span class="hx-badge">{svg("team")}Honeymoon, family &amp; groups</span><span class="hx-badge">{svg("doc")}Honest Schengen visa guidance</span></div>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Get a Switzerland Quote {svg("arrow")}</a>'
             f'<a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div></div>'
             '<form class="hx-plan" id="hxPlan" aria-label="Get a costed Switzerland itinerary on WhatsApp"><h3>Plan my Switzerland trip</h3>'
             '<p>Tell us the basics — we reply on WhatsApp with a costed, day-by-day plan, usually within 24 hours.</p><div class="hx-f">'
             '<label class="hx-full">Trip<select name="d"><option selected>Lucerne + Interlaken + Zermatt</option><option>Lucerne + Interlaken</option><option>Switzerland honeymoon</option><option>Switzerland with Glacier Express</option><option>Switzerland + Lake Geneva &amp; Montreux</option><option>Switzerland in winter (snow)</option><option>Switzerland + Paris or Italy</option></select></label>'
             '<label>Trip type<select name="s"><option>Honeymoon / couple</option><option>Family</option><option>Friends</option><option>Seniors</option><option>Group</option><option>Corporate / MICE</option></select></label>'
             f'<label>Travel month<select name="m">{G.months()}</select></label>'
             '<label>Adults<select name="a"><option>1</option><option selected>2</option><option>3</option><option>4</option><option>5</option><option>6</option><option>7–10</option><option>11–20</option><option>20+</option></select></label>'
             '<label>Children<select name="k"><option>0</option><option>1</option><option>2</option><option>3</option><option>4+</option></select></label>'
             '<label class="hx-full">Departing from<input name="c" type="text" placeholder="e.g. Delhi, Mumbai, Chandigarh" autocomplete="address-level2"></label></div>'
             f'<button class="hx-btn" type="submit">{WA_SVG}Get my Switzerland plan on WhatsApp</button><small>Opens WhatsApp with your details filled in. We do not store anything on this page.</small></form></section>')
    h.append('<div class="hx-trust">'
             f'<div>{svg("clock")}<span><b>Quote in ~24 hours</b><span>Costed, day by day</span></span></div>'
             f'<div>{svg("doc")}<span><b>Honest visa guidance</b><span>Official rules, checked</span></span></div>'
             f'<div>{svg("shield")}<span><b>HP Tourism registered</b><span>Reg. DTO-MND-11-243/2022</span></span></div>'
             f'<div>{svg("chat")}<span><b>One team, start to finish</b><span>On WhatsApp while you travel</span></span></div></div>')
    h.append('<nav class="hx-toc" aria-label="On this page"><a href="#why-switzerland">Why Switzerland</a><a href="#switzerland-in-photos">Photos</a><a href="#how-to-choose">Choose your trip</a><a href="#sample-itinerary">Sample itinerary</a><a href="#when-to-go">When to go</a><a href="#visa-and-entry">Visa &amp; entry</a><a href="#whats-included">What\'s included</a><a href="#switzerland-faq">FAQ</a></nav>')
    facts = [('Getting there', 'Fly into Zurich or Geneva — we compare routes from your city'), ('Time difference', 'India is 4 hr 30 min ahead in winter, 3 hr 30 min in summer'), ('Currency', 'Swiss franc (CHF)'),
             ('Best season', 'June to September for green Alps; December to March for snow'), ('Typical trip', '6 to 10 nights, three bases'), ('Visa', 'Schengen short-stay visa — Switzerland is in Schengen')]
    h.append('<section id="why-switzerland" class="hx-sec"><span class="hx-eye">Switzerland</span><h2>Why Switzerland is worth a trip of its own</h2>'
             '<p class="hx-sub">On a multi-country Europe tour Switzerland gets two or three days. On its own, you have time for the places that make it special: Lucerne and its lake with Mount Titlis above Engelberg; Interlaken, Grindelwald, the Lauterbrunnen valley and the railway to the Jungfraujoch; car-free Zermatt under the Matterhorn with the Gornergrat railway; and panoramic trains such as the Glacier Express and the Bernina Express. Trains, buses and lake boats link it all, so there are no long drives — and one Schengen visa also lets you add Paris or Italy.</p>'
             '<div class="hx-facts">' + ''.join(f'<div class="hx-fact"><b>{a}</b><span>{b}</span></div>' for a, b in facts) + '</div></section>')
    h.append('<section id="switzerland-in-photos" class="hx-sec"><span class="hx-eye">Real places</span><h2>Switzerland in photos</h2>'
             '<p class="hx-sub">The Matterhorn at sunrise, Lucerne\'s Chapel Bridge, the Bernina line near Morteratsch, the Matterhorn above Zermatt, a mountain train at Kleine Scheidegg, Chillon Castle on Lake Geneva, the Rhine Falls and Grindelwald — the places on a Suzu Switzerland itinerary. Photos by Unsplash photographers, credited below.</p><div class="hx-pg">'
             + ''.join(f'<figure><img src="{U(k)}" alt="{A(k)}" width="800" height="600" loading="lazy" decoding="async"><figcaption>{C(k)}</figcaption></figure>' for k in GAL) + '</div></section>')
    cards = [('Couples', 'Honeymoon', 'Lake-view rooms in Lucerne or Interlaken, a night or two in Zermatt under the Matterhorn, a panoramic train journey and snow at the Jungfraujoch. Fewer hotel changes, more time together.'),
             ('First trip', 'Classic Switzerland', 'Lucerne and Mount Titlis, Interlaken and the Jungfraujoch, then Zermatt and the Gornergrat in 7–8 nights, all by train.'),
             ('Families &amp; seniors', 'Easy-pace family holiday', 'Two or three bases instead of daily moves, cable cars and mountain railways instead of hikes, private transfers with luggage where it helps.'),
             ('Scenic trains', 'Glacier &amp; Bernina Express', 'Build the trip around a panoramic train — the Glacier Express between Zermatt and St. Moritz, or the Bernina Express over the Alps — with seats reserved in advance.')]
    stays = [('Lucerne', 'The easiest first base: lake, old town and Chapel Bridge, with day trips to Mount Titlis, Mount Pilatus or Rigi.'),
             ('Interlaken or Grindelwald', 'Interlaken for convenience and lake views; Grindelwald or Wengen for a real mountain-village feel close to the Jungfraujoch.'),
             ('Zermatt', 'Car-free village under the Matterhorn — electric taxis from the station, the Gornergrat railway on your doorstep. Book early for summer and winter.'),
             ('Montreux or Geneva', 'For Lake Geneva, Chillon Castle and an easy last night before flying home from Geneva.')]
    h.append('<section id="how-to-choose" class="hx-sec"><span class="hx-eye">How to choose</span><h2>Choose the Switzerland trip that fits you</h2>'
             '<p class="hx-sub">Start from the kind of trip you want — we fine-tune the bases, trains and pace to your group.</p><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><span class="hx-tag">{t}</span><h3>{n}</h3><p>{d}</p></div>' for t, n, d in cards) + '</div>'
             '<h3 style="margin-top:30px">Where to stay — it shapes your whole trip</h3><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><h3>{n}</h3><p>{d}</p></div>' for n, d in stays) + '</div></section>')
    days = [('Day 1', 'Arrive in Zurich, on to Lucerne', 'Airport pickup or a direct train to Lucerne. Evening walk across the Chapel Bridge and along the lakefront.'),
            ('Day 2', 'Mount Titlis', 'A day trip to Engelberg and the cable cars up Mount Titlis for snow, the glacier and wide views of the Alps.'),
            ('Day 3', 'Lucerne to Interlaken', 'The scenic Luzern–Interlaken Express train past lakes and mountain passes. Free evening in Interlaken.'),
            ('Day 4', 'Jungfraujoch', 'Mountain railways via Grindelwald or Lauterbrunnen and Kleine Scheidegg up to the Jungfraujoch, Europe\'s highest railway station.'),
            ('Day 5', 'Lauterbrunnen &amp; Grindelwald', 'The waterfall valley of Lauterbrunnen and the village of Grindelwald at your own pace, or a lake cruise on Lake Brienz or Thun.'),
            ('Day 6', 'Train to Zermatt', 'A train south to car-free Zermatt. Evening walk through the village with the Matterhorn above.'),
            ('Day 7', 'Gornergrat &amp; the Matterhorn', 'The Gornergrat railway for close-up Matterhorn and glacier views, or the Glacier Express as a day-long journey if it fits your route.'),
            ('Day 8', 'Lake Geneva &amp; fly home', 'A train along Lake Geneva, with a stop at Chillon Castle near Montreux if time allows, then your flight home from Geneva.')]
    h.append('<section id="sample-itinerary" class="hx-sec"><span class="hx-eye">Sample plan</span><h2>A sample 8-day Lucerne, Interlaken &amp; Zermatt itinerary</h2>'
             '<p class="hx-sub">The classic first trip to Switzerland. We rebuild it around you — add the Glacier or Bernina Express, the Rhine Falls near Zurich, a few days in Paris or Italy, or swap Zermatt for more nights in the Jungfrau region.</p><div class="hx-itin">'
             + ''.join(f'<div class="hx-day"><i>{a}</i><b>{b}</b><p>{c}</p></div>' for a, b, c in days) + '</div></section>')
    seasons = [('Jun – Sep', '<span class="hx-ok">Best</span>', 'Summer, long days', 'Green valleys, flowers and every mountain railway and cable car running. The busiest and most popular season with Indian travellers — book hotels and visa appointments early.'),
               ('Oct – Nov', '<span class="hx-mid">Quieter</span>', 'Cool autumn, first snow up high', 'Autumn colours in October and fewer visitors. Some lifts and high-mountain services close for maintenance between seasons, so we check each excursion against your dates.'),
               ('Dec – Mar', '<span class="hx-ok">Best for snow</span>', 'Cold, snow in the mountains', 'Snow-covered villages, skiing in Zermatt, Grindelwald and Engelberg, and Christmas markets in December. Short days; mountain views depend on the weather.'),
               ('Apr – May', '<span class="hx-mid">Shoulder</span>', 'Spring, snow melting', 'Spring in the lakes and valleys with snow still on the peaks. Calmer than summer; as in autumn, some mountain services pause for maintenance.')]
    h.append('<section id="when-to-go" class="hx-sec"><span class="hx-eye">Best season</span><h2>When to go to Switzerland</h2>'
             '<p class="hx-sub">Summer is the classic season, winter is for snow, and the months in between are quieter. We check weather, holiday dates, mountain-lift schedules and visa appointment availability against your plan.</p>'
             '<div class="hx-tw"><table class="hx-t"><thead><tr><th>Months</th><th>Verdict</th><th>Weather</th><th>What it means for your trip</th></tr></thead><tbody>'
             + ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in seasons) + '</tbody></table></div></section>')
    h.append('<section id="visa-and-entry" class="hx-sec"><span class="hx-eye">Visa &amp; entry</span><h2>Swiss (Schengen) visa for Indian passport holders</h2>'
             '<div class="hx-visa"><div class="hx-vbox"><h3>What the official rules say</h3><ul>'
             '<li>Switzerland is part of the <b>Schengen area</b>. Indian passport holders <b>need a Schengen short-stay visa</b> for a holiday, which allows <b>up to 90 days in any 180-day period</b> across the Schengen countries.</li>'
             '<li>If Switzerland is your <b>main destination</b> (where you spend the longest time), you apply to Switzerland. In India, Swiss Schengen visa applications are submitted at <b>VFS Global</b> centres (including Delhi, Mumbai, Bengaluru, Chennai, Kolkata and Pune) and <b>processed by the Embassy of Switzerland in New Delhi</b>.</li>'
             '<li>The Embassy says to apply <b>not earlier than 6 months</b> before entering the Schengen area, and that processing normally takes <b>10 to 15 working days</b> after the application reaches the Embassy. Applicants should be <b>legally residing in India for at least the last six months</b> to apply with the Swiss representation in India.</li>'
             '<li>Under the common Schengen rules you apply <b>at least 15 days</b> before travel, give <b>fingerprints</b>, and carry <b>travel medical insurance</b> covering emergency medical care, hospitalisation and repatriation, with a <b>passport valid for at least 3 months after you leave</b> the Schengen area.</li>'
             '<li>Appointments drive the timeline, so we suggest starting <b>two to three months before travel</b> — earlier for May–June school-holiday dates.</li></ul>'
             f'<p class="hx-checked">Checked {CHECKED} · sources: <a href="{SRC_CHE}" target="_blank" rel="noopener nofollow">Embassy of Switzerland in India — Visa, entry and residence</a> · <a href="{SRC_CHE2}" target="_blank" rel="noopener nofollow">Embassy of Switzerland in India — Schengen visa</a> · Schengen-wide rules checked 23 October 2026: <a href="{SRC_EC}" target="_blank" rel="noopener nofollow">European Commission — Applying for a Schengen visa</a></p></div>'
             '<div class="hx-vnote"><p><b>Please note:</b> visa approval and entry at the border are always the decision of the Swiss authorities and the border officers of the country you enter. We guide you through the documents and timelines honestly, but we never promise an outcome we do not control.</p>'
             '<p>Apply only through the official channel, keep your hotel bookings, insurance and return ticket consistent with your application, and carry copies for the immigration desk.</p></div></div></section>')
    inc = [('doc', 'Visa guidance', 'A clear Schengen document checklist, a day-by-day itinerary and hotel confirmations that match your application, and help booking the VFS appointment.'), ('pin', 'Hotels in the right area', 'Named hotels close to the station or lake in Lucerne, Interlaken or Grindelwald, Zermatt and Geneva.'),
           ('team', 'Transfers &amp; rail', 'Airport transfers, train tickets or a Swiss Travel Pass where it saves money, and seat reservations for panoramic trains.'), ('globe', 'Mountains &amp; sightseeing', 'Mount Titlis, the Jungfraujoch, the Gornergrat and lake cruises, plus the Rhine Falls or Chillon Castle if you want them.'),
           ('food', 'Meal plan', 'Breakfast as standard; vegetarian and Jain needs noted with hotels, plus Indian restaurant suggestions at every stop.'), ('award', 'Flights optional', 'Land-only, or a full package with international flights from your nearest Indian airport.')]
    h.append('<section id="whats-included" class="hx-sec"><span class="hx-eye">Your package</span><h2>What a Suzu Switzerland package includes</h2><div class="hx-inc">'
             + ''.join(f'<div>{svg(i)}<span><b>{t}</b><span>{d}</span></span></div>' for i, t, d in inc) + '</div></section>')
    steps = [('chat', 'Tell us the basics', 'Dates, travellers and the places you want to see. A WhatsApp message is enough.'),
             ('doc', 'Get a costed itinerary', 'A day-by-day plan with named hotels and a clear per-person price, usually within 24 hours.'),
             ('sliders', 'Adjust until it fits', 'Add a panoramic train, swap a base, upgrade a hotel, change the pace. We re-quote as needed.'),
             ('lock', 'Confirm with a token', 'Lock your rate with a small token amount; the balance is paid later, as agreed in writing.')]
    h.append('<section id="how-booking-works" class="hx-sec"><span class="hx-eye">Simple process</span><h2>How booking works</h2><div class="hx-steps">'
             + ''.join(f'<div class="hx-step"><div class="hx-n">{svg(i)}</div><b>{t}</b><p>{d}</p></div>' for i, t, d in steps) + '</div></section>')
    h.append('<section id="switzerland-faq" class="hx-sec"><span class="hx-eye">FAQ</span><h2>Common questions about a Switzerland tour</h2><div class="hx-faqs">'
             + ''.join(f'<details class="hx-faq"{" open" if k == 0 else ""}><summary>{html.escape(q)}</summary><div class="hx-ans"><p>{html.escape(a)}</p></div></details>' for k, (q, a) in enumerate(FAQ)) + '</div></section>')
    h.append('<section id="more-destinations" class="hx-sec"><span class="hx-eye">Explore more</span><h2>Explore more destinations</h2>'
             '<p class="hx-sub">Every trip is planned the same way — your dates, your budget, one team from quote to return. <a href="https://suzutravels.com/international-tour-packages/">See all international holidays →</a></p><div class="hx-mini">'
             + ''.join(f'<a class="hx-mc" href="https://suzutravels.com/{p}/"><img src="https://suzutravels.com/wp-content/uploads/2026/10/{img}.webp" alt="{html.escape(n)} holiday — Suzu Travels" width="640" height="360" loading="lazy" decoding="async"><span><b>{html.escape(n)}</b><em>{html.escape(e)}</em></span></a>' for p, n, img, e in REL) + '</div></section>')
    h.append(f'<div class="hx-final"><img src="{U("switzerland-2")}" alt="{A("switzerland-2")}" width="1600" height="900" loading="lazy" decoding="async">'
             '<h2>Plan your Switzerland trip</h2><p>Send us your dates and group size. We will come back with a costed, day-by-day Switzerland itinerary you can compare — no obligation.</p>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Request a Switzerland Quote {svg("arrow")}</a><a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div>'
             '<p class="hx-contact">Or call <strong>+91 70874 88961</strong> · <a href="mailto:info@suzutravels.com">info@suzutravels.com</a></p></div>')
    seen = []
    for k in HERO + GAL + ['switzerland-2']:
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
    open('pages/switzerland-tour-packages.html', 'w').write(o)
    print('pages/switzerland-tour-packages.html', len(o))
