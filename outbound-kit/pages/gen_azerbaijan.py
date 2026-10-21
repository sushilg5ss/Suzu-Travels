#!/usr/bin/env python3
"""Azerbaijan country page (.hx design system; same template as gen_georgia.py / gen_turkey.py / gen_dubai.py).
Run from outbound-kit/:  python3 pages/gen_azerbaijan.py <PAGE_ID>  -> pages/azerbaijan-tour-packages.html (one line)
Facts: visa/entry checked 21 Oct 2026 against official Azerbaijani sources (ASAN e-Visa portal evisa.gov.az conditions,
MFA Azerbaijan embassy pages on ASAN Visa and on visa upon arrival). No prices.
"""
import json, html, sys, os
sys.path.insert(0, os.getcwd())
import gen_hub as G

PID = int(sys.argv[1]) if len(sys.argv) > 1 else 0
M = G.M
svg, WA_SVG, wa = G.svg, G.WA_SVG, G.wa
CHECKED = '21 October 2026'
SRC_COND = 'https://evisa.gov.az/en/conditions'
SRC_ASAN = 'https://canberra.mfa.gov.az/en/category/asan-viza-e-visa'
SRC_VOA = 'https://bern.mfa.gov.az/en/content/61/visa-upon-arrival-to-azerbaijan'

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
body.page-id-PID .page-header:before{content:"Holidays abroad \00B7  Azerbaijan";display:inline-block;font:800 12px/1 "Plus Jakarta Sans",sans-serif;letter-spacing:.18em;text-transform:uppercase;color:#1a1606;background:#E2C158;padding:8px 13px;border-radius:999px;margin-bottom:16px}
body.page-id-PID .page-header .entry-title{color:#fff!important;font-family:"Sora","Plus Jakarta Sans",sans-serif!important;font-size:clamp(34px,4.2vw,58px)!important;line-height:1.06!important;letter-spacing:-.035em!important;margin:0!important;font-weight:800!important;max-width:15ch;text-shadow:0 2px 24px rgba(0,0,0,.35)}
@media(max-width:1100px){.hx .hx-cards{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-itin{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-visa{grid-template-columns:1fr}.hx .hx-inc,.hx .hx-steps{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:700px){body.page-id-PID .page-header{left:14px;right:14px;padding:26px 18px 0}body.page-id-PID .page-header:before{font-size:10.5px;padding:7px 11px;margin-bottom:12px}body.page-id-PID .page-header .entry-title{font-size:33px!important}.hx .hx-facts{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-pg{grid-template-columns:repeat(2,minmax(0,1fr));grid-auto-rows:150px}.hx .hx-pg figure:first-child{grid-column:span 2;grid-row:span 1}.hx .hx-pg figure:nth-child(4){grid-row:span 1}.hx .hx-pg figure:nth-child(8){display:none}.hx .hx-cards,.hx .hx-itin,.hx .hx-inc,.hx .hx-steps{grid-template-columns:1fr}.hx .hx-mini{grid-template-columns:repeat(2,minmax(0,1fr))}}
.hx .hx-pg p,.hx .hx-cards>p,.hx .hx-itin>p,.hx .hx-inc>p,.hx .hx-facts>p{display:none}
""".replace('PID', str(PID))
EXTRA += "@media(min-width:1101px){.hx .hx-itin{grid-template-columns:repeat(3,minmax(0,1fr))}}"
CSS = ' '.join(l.strip() for l in (base + EXTRA).strip().splitlines() if l.strip() and not l.strip().startswith('/*'))
HERO = ['azerbaijan-1', 'azerbaijan-6', 'azerbaijan-2', 'azerbaijan-3', 'azerbaijan-8', 'azerbaijan-9']
GAL = ['azerbaijan-5', 'azerbaijan-7', 'azerbaijan-2', 'azerbaijan-8', 'azerbaijan-3', 'azerbaijan-6', 'azerbaijan-4', 'azerbaijan-9']
CC = 'Azerbaijan'

FAQ = [
    ("Do Indians need a visa for Azerbaijan?", "Yes. Indian citizens need a visa, and India is on the list of countries whose citizens can apply for Azerbaijan's electronic visa (ASAN Visa) on the official portal evisa.gov.az. The e-visa is single entry, valid for 90 days, and allows a stay of up to 30 days. The standard e-visa is issued within 3 working days and an urgent one within 3 hours. India is not on the official visa-upon-arrival list, so apply online before you fly. Approval is always the decision of the Azerbaijani authorities."),
    ("How many days are enough for Azerbaijan?", "Four to five nights covers Baku — the Old City, the Flame Towers, the seafront Boulevard and a day trip on the Absheron peninsula — plus one or two nights in the mountains at Gabala or Shahdag. With six to eight nights you can add Sheki or combine Azerbaijan with Georgia."),
    ("When is the best time to visit Azerbaijan from India?", "April to June and September to October suit most Indian travellers: comfortable weather in Baku and green mountain valleys. July and August are hot in Baku but pleasant in Gabala and Qusar. December to March is the snow season in the mountains, when Shahdag and Tufandag operate as ski resorts."),
    ("Can we see snow in Azerbaijan?", "Yes. In winter the Greater Caucasus around Gabala and Qusar is usually snow-covered, and the Shahdag Mountain Resort (Qusar) and the Tufandag resort (Gabala) have ski slopes and cable cars. Snow depends on the year, so we check conditions against your dates before we confirm a snow day."),
    ("Is vegetarian food easy to find in Azerbaijan?", "Azerbaijani food leans towards meat, but vegetarian options are easy to arrange: herb- and pumpkin-filled qutab flatbreads, vegetable dolma, rice dishes, fresh salads, bread, cheese and fruit. Baku also has Indian restaurants. Jain meals need advance notice, which we arrange with hotels where possible."),
    ("Can we combine Azerbaijan with Georgia?", "Yes. Baku and Tbilisi are well connected, and Azerbaijan plus Georgia is a popular 8 to 10-night trip. Each country has its own visa rules for Indian passport holders, so we check both and plan the documents in the right order."),
    ("Why are there no prices on this page?", "Azerbaijan costs depend on your dates, hotel category, the vehicle you need and the airfare from India. Instead of a teaser price that changes when you ask, we send a costed, day-by-day quote for your dates — usually within 24 hours."),
]

JS = ("(function(){var f=document.getElementById('hxPlan');if(!f){return;}f.addEventListener('submit',function(e){e.preventDefault();"
      "var d=f.querySelector('[name=d]').value,s=f.querySelector('[name=s]').value,m=f.querySelector('[name=m]').value,a=f.querySelector('[name=a]').value,k=f.querySelector('[name=k]').value,c=f.querySelector('[name=c]').value;"
      "var t='Hi Suzu Travels, please send me a costed Azerbaijan itinerary.\\nTrip: '+d+'\\nTrip type: '+s+'\\nTravel month: '+m+'\\nAdults: '+a+'\\nChildren: '+k;"
      "if(c){t=t+'\\nDeparting from: '+c;}"
      "window.open('https:'+String.fromCharCode(47,47)+'wa.me/917087488961?text='+encodeURIComponent(t),'_blank','noopener');});})();")

REL = [('dubai-tour-packages', 'Dubai', 'suzu-abroad-dubai', 'Burj Khalifa, desert, Abu Dhabi'), ('turkey-tour-packages', 'Turkey', 'suzu-abroad-turkey', 'Istanbul, Cappadocia, Pamukkale'),
       ('georgia-tour-packages', 'Georgia', 'suzu-abroad-georgia', 'Tbilisi, Kazbegi, Gudauri'),
       ('nepal-tour-packages', 'Nepal', 'suzu-card-nepal', 'No visa for Indians'), ('bhutan-tour-packages', 'Bhutan', 'suzu-card-bhutan', 'Paro, Thimphu, Punakha'),
       ('sri-lanka-tour-packages', 'Sri Lanka', 'suzu-card-sri-lanka', 'Beaches & tea country'), ('maldives-tour-packages', 'Maldives', 'suzu-card-maldives', 'Overwater villas'),
       ('thailand-tour-packages', 'Thailand', 'suzu-card-thailand', 'Bangkok, Phuket, Krabi'), ('singapore-tour-packages', 'Singapore', 'suzu-card-singapore', 'City, Sentosa, Universal'),
       ('malaysia-tour-packages', 'Malaysia', 'suzu-card-malaysia', 'KL, Langkawi, Genting'), ('vietnam-tour-packages', 'Vietnam', 'suzu-card-vietnam', 'Hanoi, Ha Long, Hoi An'),
       ('bali-tour-packages', 'Bali', 'suzu-card-bali', 'Ubud, villas, temples')]

def build():
    W = "Hi Suzu Travels, I'm planning an Azerbaijan trip. Please share a quote."
    h = [f'<div class="suzu-intl hx hx-country"><style>{CSS}</style>']
    slides = ''.join(f'<div class="hx-slide"><img src="{U(s)}" alt="{A(s)}" width="1600" height="1000" {"fetchpriority=\"high\" loading=\"eager\"" if i == 0 else "loading=\"lazy\""} decoding="async"><span class="hx-cap">{C(s)}</span></div>' for i, s in enumerate(HERO))
    h.append('<section class="hx-hero" aria-label="Azerbaijan tour packages from India"><div class="hx-slides">' + slides + '</div><div class="hx-copy">'
             '<p class="hx-lede">The Flame Towers above the Caspian Sea, the stone lanes and Maiden Tower of Baku\'s Old City, the curves of the Heydar Aliyev Center and the green and snowy Caucasus valleys of Gabala and Qusar — Azerbaijan is a short, easy holiday abroad for Indian travellers. We plan it to your dates, your budget and your pace.</p>'
             '<div class="hx-badges">'
             f'<span class="hx-badge">{svg("globe")}Baku, Gabala &amp; Shahdag</span><span class="hx-badge">{svg("food")}Vegetarian meals arranged</span>'
             f'<span class="hx-badge">{svg("team")}Families, couples &amp; groups</span><span class="hx-badge">{svg("doc")}Honest e-visa guidance</span></div>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Get an Azerbaijan Quote {svg("arrow")}</a>'
             f'<a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div></div>'
             '<form class="hx-plan" id="hxPlan" aria-label="Get a costed Azerbaijan itinerary on WhatsApp"><h3>Plan my Azerbaijan trip</h3>'
             '<p>Tell us the basics — we reply on WhatsApp with a costed, day-by-day plan, usually within 24 hours.</p><div class="hx-f">'
             '<label class="hx-full">Trip<select name="d"><option>Baku only</option><option selected>Baku + Gabala</option><option>Baku + Shahdag / Qusar</option><option>Baku + Gabala + Sheki</option><option>Snow trip — Shahdag or Tufandag in winter</option><option>Azerbaijan + Georgia</option></select></label>'
             '<label>Trip type<select name="s"><option>Family</option><option>Honeymoon / couple</option><option>Friends</option><option>Group</option><option>Corporate / MICE</option></select></label>'
             f'<label>Travel month<select name="m">{G.months()}</select></label>'
             '<label>Adults<select name="a"><option>1</option><option selected>2</option><option>3</option><option>4</option><option>5</option><option>6</option><option>7–10</option><option>11–20</option><option>20+</option></select></label>'
             '<label>Children<select name="k"><option>0</option><option>1</option><option>2</option><option>3</option><option>4+</option></select></label>'
             '<label class="hx-full">Departing from<input name="c" type="text" placeholder="e.g. Delhi, Mumbai, Chandigarh" autocomplete="address-level2"></label></div>'
             f'<button class="hx-btn" type="submit">{WA_SVG}Get my Azerbaijan plan on WhatsApp</button><small>Opens WhatsApp with your details filled in. We do not store anything on this page.</small></form></section>')
    h.append('<div class="hx-trust">'
             f'<div>{svg("clock")}<span><b>Quote in ~24 hours</b><span>Costed, day by day</span></span></div>'
             f'<div>{svg("doc")}<span><b>Honest visa guidance</b><span>Official rules, checked</span></span></div>'
             f'<div>{svg("shield")}<span><b>HP Tourism registered</b><span>Reg. DTO-MND-11-243/2022</span></span></div>'
             f'<div>{svg("chat")}<span><b>One team, start to finish</b><span>On WhatsApp while you travel</span></span></div></div>')
    h.append('<nav class="hx-toc" aria-label="On this page"><a href="#why-azerbaijan">Why Azerbaijan</a><a href="#azerbaijan-in-photos">Photos</a><a href="#how-to-choose">Choose your trip</a><a href="#sample-itinerary">Sample itinerary</a><a href="#when-to-go">When to go</a><a href="#visa-and-entry">Visa &amp; entry</a><a href="#whats-included">What\'s included</a><a href="#azerbaijan-faq">FAQ</a></nav>')
    facts = [('Getting there', 'Flights to Baku — we compare options from your city'), ('Time difference', 'Azerbaijan is 1 hr 30 min behind IST'), ('Currency', 'Azerbaijani Manat (AZN)'),
             ('Best season', 'April to June, September to October; Dec to Mar for snow'), ('Typical trip', '4 to 6 nights'), ('Language', 'Azerbaijani; Russian widely spoken; English in hotels')]
    h.append('<section id="why-azerbaijan" class="hx-sec"><span class="hx-eye">Azerbaijan · Land of Fire</span><h2>Why Azerbaijan works so well for Indian travellers</h2>'
             '<p class="hx-sub">Azerbaijan packs a modern capital and old mountain country into a short trip. Baku has a walled Old City with the Maiden Tower and the Palace of the Shirvanshahs, a long seafront Boulevard on the Caspian Sea, the Flame Towers and the Heydar Aliyev Center. A day on the Absheron peninsula takes in the Gobustan rock art and the Ateshgah fire temple, whose old inscriptions include Sanskrit and Punjabi. A few hours\' drive away, Gabala and Qusar offer green Caucasus valleys in summer and snow and cable cars in winter.</p>'
             '<div class="hx-facts">' + ''.join(f'<div class="hx-fact"><b>{a}</b><span>{b}</span></div>' for a, b in facts) + '</div></section>')
    h.append('<section id="azerbaijan-in-photos" class="hx-sec"><span class="hx-eye">Real places</span><h2>Azerbaijan in photos</h2>'
             '<p class="hx-sub">Baku\'s Old City, the Flame Towers, the Boulevard, the Heydar Aliyev Center and the mountains of Qusar and Gabala — the places on a classic Suzu Azerbaijan itinerary. Photos by Unsplash photographers, credited below.</p><div class="hx-pg">'
             + ''.join(f'<figure><img src="{U(k)}" alt="{A(k)}" width="800" height="600" loading="lazy" decoding="async"><figcaption>{C(k)}</figcaption></figure>' for k in GAL) + '</div></section>')
    cards = [('Couples', 'Honeymoon', 'A sea-view room in Baku, evenings on the Boulevard and in the Old City, then a quiet mountain resort in Gabala. Add Sheki or Georgia if you have more time.'),
             ('First trip to Azerbaijan', 'Classic circuit', 'Baku, the Absheron peninsula and Gabala in 4–6 nights — the trip most first-time visitors from India choose.'),
             ('Families', 'Family holiday', 'Two hotel bases, a private vehicle with driver and short sightseeing days. In winter, a snow day at Shahdag or Tufandag is a favourite with children.'),
             ('Groups', 'Groups &amp; corporate', 'Coaches with guides, group check-ins, conference venues and team dinners in Baku. Tell us the group size and we quote accordingly, including B2B for travel agents.')]
    stays = [('Old City &amp; Fountain Square, Baku', 'Stay inside or next to the walled Old City — the Maiden Tower, cafés and the Boulevard are all on foot. The easiest base for a first visit.'),
             ('Seafront &amp; Boulevard, Baku', 'Larger city hotels along the Caspian, with sea views and easy taxis. Good for families who want space and a pool.'),
             ('Gabala', 'Mountain resorts below the Greater Caucasus, with the Tufandag cable car and Nohur lake nearby. Green in summer, snowy in winter.'),
             ('Shahdag (Qusar) or Sheki', 'Shahdag is a mountain resort with ski slopes in winter; Sheki is an old silk-road town known for the Khan\'s Palace, for a longer trip.')]
    h.append('<section id="how-to-choose" class="hx-sec"><span class="hx-eye">How to choose</span><h2>Choose the Azerbaijan trip that fits you</h2>'
             '<p class="hx-sub">Start from the kind of trip you want — we fine-tune the days, hotels and pace to your group.</p><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><span class="hx-tag">{t}</span><h3>{n}</h3><p>{d}</p></div>' for t, n, d in cards) + '</div>'
             '<h3 style="margin-top:30px">Where to stay — it shapes your whole trip</h3><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><h3>{n}</h3><p>{d}</p></div>' for n, d in stays) + '</div></section>')
    days = [('Day 1', 'Arrive in Baku', 'Airport pickup and hotel check-in. An easy evening walk on the seafront Boulevard and dinner near your hotel.'),
            ('Day 2', 'Old City &amp; Flame Towers', 'The Maiden Tower and the Palace of the Shirvanshahs in the walled Old City with a local guide, the Heydar Aliyev Center, and the city view from Highland (Upland) Park.'),
            ('Day 3', 'Absheron peninsula', 'Gobustan rock art and the mud volcanoes, then the Ateshgah fire temple and Yanar Dag, the hillside where a natural gas fire burns.'),
            ('Day 4', 'Baku to Gabala', 'A scenic drive into the Caucasus foothills via Shamakhi, then the Tufandag cable car or Nohur lake in Gabala. Night in a mountain resort.'),
            ('Day 5', 'Gabala to Baku', 'A slow morning in the mountains, then back to Baku for shopping on Nizami Street and a last evening on the Boulevard.'),
            ('Day 6', 'Fly home', 'Breakfast, then the transfer to Baku airport for your flight home.')]
    h.append('<section id="sample-itinerary" class="hx-sec"><span class="hx-eye">Sample plan</span><h2>A sample 6-day Baku, Absheron &amp; Gabala itinerary</h2>'
             '<p class="hx-sub">The classic first trip to Azerbaijan. We rebuild it around you — Shahdag instead of Gabala, a snow day in winter, Sheki for a longer trip, or a few days in Georgia.</p><div class="hx-itin">'
             + ''.join(f'<div class="hx-day"><i>{a}</i><b>{b}</b><p>{c}</p></div>' for a, b, c in days) + '</div></section>')
    seasons = [('Apr – Jun', '<span class="hx-ok">Best</span>', 'Spring, mild to warm', 'Comfortable city walks in Baku and green valleys in Gabala and Qusar. The best all-round time for a first visit.'),
               ('Jul – Aug', '<span class="hx-mid">Good</span>', 'Hot in Baku, pleasant in the mountains', 'Plan Baku sightseeing for mornings and evenings and spend more nights in Gabala or Shahdag.'),
               ('Sep – Oct', '<span class="hx-ok">Best</span>', 'Warm days, cooler evenings', 'Pleasant weather across the country. Baku can be windy, so carry a light jacket.'),
               ('Nov – Mar', '<span class="hx-mid">Snow season</span>', 'Cold, snow in the mountains', 'Ski slopes and snow at Shahdag and Tufandag; Baku is cool and windy. Snow varies by year, so we check conditions before confirming a snow day.')]
    h.append('<section id="when-to-go" class="hx-sec"><span class="hx-eye">Best season</span><h2>When to go to Azerbaijan</h2>'
             '<p class="hx-sub">Spring and early autumn suit most Indian travellers; winter is for those who want snow. We check weather and resort conditions against your dates.</p>'
             '<div class="hx-tw"><table class="hx-t"><thead><tr><th>Months</th><th>Verdict</th><th>Weather</th><th>What it means for your trip</th></tr></thead><tbody>'
             + ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in seasons) + '</tbody></table></div></section>')
    h.append('<section id="visa-and-entry" class="hx-sec"><span class="hx-eye">Visa &amp; entry</span><h2>Visa and entry for Indian passport holders</h2>'
             '<div class="hx-visa"><div class="hx-vbox"><h3>What the official rules say</h3><ul>'
             '<li>Indian passport holders <b>need a visa</b> for Azerbaijan. India is on the list of countries whose citizens can apply for the <b>electronic visa (ASAN Visa)</b> on the official portal <b>evisa.gov.az</b>.</li>'
             '<li>The e-visa is <b>single entry</b> and <b>valid for 90 days</b>, with permission to <b>stay up to 30 days</b>.</li>'
             '<li>The <b>standard e-visa is issued within 3 working days</b> and the <b>urgent e-visa within 3 hours</b>, so apply at least that long before you arrive — we suggest well before your flight.</li>'
             '<li>Your <b>passport must be valid for at least 3 months beyond the e-visa\'s expiry date</b>. The e-visa is not stamped in the passport — print it and carry it with your passport.</li>'
             '<li>India is <b>not</b> on the official visa-upon-arrival list, so do not plan to get a visa at the airport. Payments are not refunded if an e-visa is refused.</li></ul>'
             f'<p class="hx-checked">Checked {CHECKED} · sources: <a href="{SRC_COND}" target="_blank" rel="noopener nofollow">ASAN Visa portal (evisa.gov.az) — conditions for issuing electronic visas</a> · <a href="{SRC_ASAN}" target="_blank" rel="noopener nofollow">Ministry of Foreign Affairs of Azerbaijan, Embassy page — ASAN Visa (e-Visa) and eligible countries</a> · <a href="{SRC_VOA}" target="_blank" rel="noopener nofollow">Ministry of Foreign Affairs of Azerbaijan, Embassy page — visa upon arrival</a></p></div>'
             '<div class="hx-vnote"><p><b>Please note:</b> visa approval and entry at the border are always the decision of the Azerbaijani authorities. We guide you through the documents and timelines honestly, but we never promise an outcome we do not control.</p>'
             '<p>Apply only on the official portal evisa.gov.az — not on look-alike sites — and keep printed copies of your e-visa, hotel bookings and return ticket with you.</p></div></div></section>')
    inc = [('doc', 'Visa guidance', 'A clear checklist and help with your ASAN e-visa application on the official portal.'), ('pin', 'Hotels in the right area', 'Named hotels — near the Old City or on the seafront in Baku, and a mountain resort in Gabala or Shahdag.'),
           ('team', 'Private vehicle &amp; driver', 'Airport pickup and drop, and a private car, van or coach with driver for the Absheron and mountain days.'), ('globe', 'Guided sightseeing', 'Local guides for the Old City and the Absheron peninsula; cable car tickets where you want them.'),
           ('food', 'Meal plan', 'Breakfast as standard; vegetarian and Jain meals arranged on request where hotels can.'), ('award', 'Flights optional', 'Land-only, or a full package with international flights from your nearest Indian airport.')]
    h.append('<section id="whats-included" class="hx-sec"><span class="hx-eye">Your package</span><h2>What a Suzu Azerbaijan package includes</h2><div class="hx-inc">'
             + ''.join(f'<div>{svg(i)}<span><b>{t}</b><span>{d}</span></span></div>' for i, t, d in inc) + '</div></section>')
    steps = [('chat', 'Tell us the basics', 'Dates, travellers and the kind of Azerbaijan trip you want. A WhatsApp message is enough.'),
             ('doc', 'Get a costed itinerary', 'A day-by-day plan with named hotels and a clear per-person price, usually within 24 hours.'),
             ('sliders', 'Adjust until it fits', 'Add Sheki, a snow day or a few days in Georgia, upgrade a hotel, change the pace. We re-quote as needed.'),
             ('lock', 'Confirm with a token', 'Lock your rate with a small token amount; the balance is paid later, as agreed in writing.')]
    h.append('<section id="how-booking-works" class="hx-sec"><span class="hx-eye">Simple process</span><h2>How booking works</h2><div class="hx-steps">'
             + ''.join(f'<div class="hx-step"><div class="hx-n">{svg(i)}</div><b>{t}</b><p>{d}</p></div>' for i, t, d in steps) + '</div></section>')
    h.append('<section id="azerbaijan-faq" class="hx-sec"><span class="hx-eye">FAQ</span><h2>Common questions about Azerbaijan</h2><div class="hx-faqs">'
             + ''.join(f'<details class="hx-faq"{" open" if k == 0 else ""}><summary>{html.escape(q)}</summary><div class="hx-ans"><p>{html.escape(a)}</p></div></details>' for k, (q, a) in enumerate(FAQ)) + '</div></section>')
    h.append('<section id="more-destinations" class="hx-sec"><span class="hx-eye">Explore more</span><h2>Explore more destinations</h2>'
             '<p class="hx-sub">Every trip is planned the same way — your dates, your budget, one team from quote to return. <a href="https://suzutravels.com/international-tour-packages/">See all international holidays →</a></p><div class="hx-mini">'
             + ''.join(f'<a class="hx-mc" href="https://suzutravels.com/{p}/"><img src="https://suzutravels.com/wp-content/uploads/2026/10/{img}.webp" alt="{html.escape(n)} holiday — Suzu Travels" width="640" height="360" loading="lazy" decoding="async"><span><b>{html.escape(n)}</b><em>{html.escape(e)}</em></span></a>' for p, n, img, e in REL) + '</div></section>')
    h.append(f'<div class="hx-final"><img src="{U("azerbaijan-1")}" alt="{A("azerbaijan-1")}" width="1600" height="900" loading="lazy" decoding="async">'
             '<h2>Plan your Azerbaijan trip</h2><p>Send us your dates and group size. We will come back with a costed, day-by-day Azerbaijan itinerary you can compare — no obligation.</p>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Request an Azerbaijan Quote {svg("arrow")}</a><a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div>'
             '<p class="hx-contact">Or call <strong>+91 70874 88961</strong> · <a href="mailto:info@suzutravels.com">info@suzutravels.com</a></p></div>')
    seen = []
    for k in HERO + GAL:
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
    open('pages/azerbaijan-tour-packages.html', 'w').write(o)
    print('pages/azerbaijan-tour-packages.html', len(o))
