#!/usr/bin/env python3
"""Japan country page (.hx design system; same template as gen_azerbaijan.py / gen_georgia.py / gen_turkey.py / gen_dubai.py).
Run from outbound-kit/:  python3 pages/gen_japan.py <PAGE_ID>  -> pages/japan-tour-packages.html (one line)
Facts: visa/entry checked 22 Oct 2026 against official Japanese sources (MOFA Japan visa page, JAPAN eVISA FAQ,
Consulate-General of Japan in Bengaluru eVISA notice). No prices.
"""
import json, html, sys, os
sys.path.insert(0, os.getcwd())
import gen_hub as G

PID = int(sys.argv[1]) if len(sys.argv) > 1 else 0
M = G.M
svg, WA_SVG, wa = G.svg, G.WA_SVG, G.wa
CHECKED = '22 October 2026'
SRC_MOFA = 'https://www.mofa.go.jp/j_info/visit/visa/visaonline.html'
SRC_FAQ = 'https://www.evisa.mofa.go.jp/personal/faq'
SRC_BLR = 'https://www.bengaluru.in.emb-japan.go.jp/itpr_ja/20240325_00002.html'

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
body.page-id-PID .page-header:before{content:"Holidays abroad \00B7  Japan";display:inline-block;font:800 12px/1 "Plus Jakarta Sans",sans-serif;letter-spacing:.18em;text-transform:uppercase;color:#1a1606;background:#E2C158;padding:8px 13px;border-radius:999px;margin-bottom:16px}
body.page-id-PID .page-header .entry-title{color:#fff!important;font-family:"Sora","Plus Jakarta Sans",sans-serif!important;font-size:clamp(34px,4.2vw,58px)!important;line-height:1.06!important;letter-spacing:-.035em!important;margin:0!important;font-weight:800!important;max-width:15ch;text-shadow:0 2px 24px rgba(0,0,0,.35)}
@media(max-width:1100px){.hx .hx-cards{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-itin{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-visa{grid-template-columns:1fr}.hx .hx-inc,.hx .hx-steps{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:700px){body.page-id-PID .page-header{left:14px;right:14px;padding:26px 18px 0}body.page-id-PID .page-header:before{font-size:10.5px;padding:7px 11px;margin-bottom:12px}body.page-id-PID .page-header .entry-title{font-size:33px!important}.hx .hx-facts{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-pg{grid-template-columns:repeat(2,minmax(0,1fr));grid-auto-rows:150px}.hx .hx-pg figure:first-child{grid-column:span 2;grid-row:span 1}.hx .hx-pg figure:nth-child(4){grid-row:span 1}.hx .hx-pg figure:nth-child(8){display:none}.hx .hx-cards,.hx .hx-itin,.hx .hx-inc,.hx .hx-steps{grid-template-columns:1fr}.hx .hx-mini{grid-template-columns:repeat(2,minmax(0,1fr))}}
.hx .hx-pg p,.hx .hx-cards>p,.hx .hx-itin>p,.hx .hx-inc>p,.hx .hx-facts>p{display:none}
""".replace('PID', str(PID))
CSS = ' '.join(l.strip() for l in (base + EXTRA).strip().splitlines() if l.strip() and not l.strip().startswith('/*'))
HERO = ['japan', 'japan-2', 'japan-1', 'japan-9', 'japan-5', 'japan-4']
GAL = ['japan-9', 'japan-2', 'japan-1', 'japan-3', 'japan-6', 'japan-10', 'japan-7', 'japan-8']
CC = 'Japan'

FAQ = [
    ("Do Indians need a visa for Japan?", "Yes. Indian passport holders need a visa for a short holiday in Japan. Since 1 April 2024, Indian nationals and foreign nationals living in India can get a single-entry short-term tourist visa as an eVISA, applied for through the Japan Visa Application Centres (VFS Global). Japan's eVISA FAQ says examination normally takes 5 working days but can take more than a month in busy periods, and the eVISA must be used within 3 months of issue. At the airport you show the visa issuance notice on your phone with internet access — screenshots and printouts are not accepted. Approval is always the decision of the Japanese authorities."),
    ("How many days are enough for Japan?", "Seven to eight nights covers the classic first trip: Tokyo, a night near Mount Fuji, Kyoto with a day in Nara, and Osaka. With ten to twelve nights you can add Hiroshima and Miyajima, the Japanese Alps, or more relaxed days in Kyoto. Hokkaido in winter needs its own four to five nights."),
    ("When is the best time to visit Japan from India?", "Late March to early April for cherry blossom and October to November for autumn leaves are the favourite seasons; both are busy, so plan early. May and early October are pleasant and calmer. June to mid-July is the rainy season on the main island, July and August are hot and humid, and typhoons are most likely from August to September. December to February is cold, with snow in Hokkaido and the mountains."),
    ("When is cherry blossom season in Japan?", "In Tokyo and Kyoto the cherry blossoms usually open in late March and early April, but the dates move every year with the weather and the trees stay at their best for only about a week. Japan publishes blossom forecasts from early in the year; we follow them and build your dates with a little flexibility."),
    ("Is vegetarian food easy to find in Japan?", "It needs planning. Many Japanese dishes use dashi, a fish stock, even when they look vegetarian. Tokyo, Kyoto and Osaka have Indian and vegetarian restaurants, and Kyoto's Buddhist temple cuisine (shojin ryori) is fully vegetarian. We note vegetarian and Jain needs with hotels and suggest restaurants for every day of your trip."),
    ("Is Japan good for a family trip with children?", "Very. Japan is clean, safe and runs on time. Tokyo Disneyland and DisneySea, Universal Studios Japan in Osaka, the deer park in Nara and a ride on the Shinkansen bullet train are favourites with children. We keep travel days short and book hotel rooms that fit your family, since many city rooms in Japan are small."),
    ("Why are there no prices on this page?", "Japan costs depend heavily on your dates (cherry blossom and autumn weeks cost more), hotel category, rail passes and the airfare from India. Instead of a teaser price that changes when you ask, we send a costed, day-by-day quote for your dates — usually within 24 hours."),
]

JS = ("(function(){var f=document.getElementById('hxPlan');if(!f){return;}f.addEventListener('submit',function(e){e.preventDefault();"
      "var d=f.querySelector('[name=d]').value,s=f.querySelector('[name=s]').value,m=f.querySelector('[name=m]').value,a=f.querySelector('[name=a]').value,k=f.querySelector('[name=k]').value,c=f.querySelector('[name=c]').value;"
      "var t='Hi Suzu Travels, please send me a costed Japan itinerary.\\nTrip: '+d+'\\nTrip type: '+s+'\\nTravel month: '+m+'\\nAdults: '+a+'\\nChildren: '+k;"
      "if(c){t=t+'\\nDeparting from: '+c;}"
      "window.open('https:'+String.fromCharCode(47,47)+'wa.me/917087488961?text='+encodeURIComponent(t),'_blank','noopener');});})();")

REL = [('dubai-tour-packages', 'Dubai', 'suzu-abroad-dubai', 'Burj Khalifa, desert, Abu Dhabi'), ('turkey-tour-packages', 'Turkey', 'suzu-abroad-turkey', 'Istanbul, Cappadocia, Pamukkale'),
       ('georgia-tour-packages', 'Georgia', 'suzu-abroad-georgia', 'Tbilisi, Kazbegi, Gudauri'), ('azerbaijan-tour-packages', 'Azerbaijan', 'suzu-abroad-azerbaijan', 'Baku, Gabala, Shahdag'),
       ('nepal-tour-packages', 'Nepal', 'suzu-card-nepal', 'No visa for Indians'), ('bhutan-tour-packages', 'Bhutan', 'suzu-card-bhutan', 'Paro, Thimphu, Punakha'),
       ('sri-lanka-tour-packages', 'Sri Lanka', 'suzu-card-sri-lanka', 'Beaches & tea country'), ('maldives-tour-packages', 'Maldives', 'suzu-card-maldives', 'Overwater villas'),
       ('thailand-tour-packages', 'Thailand', 'suzu-card-thailand', 'Bangkok, Phuket, Krabi'), ('singapore-tour-packages', 'Singapore', 'suzu-card-singapore', 'City, Sentosa, Universal'),
       ('malaysia-tour-packages', 'Malaysia', 'suzu-card-malaysia', 'KL, Langkawi, Genting'), ('vietnam-tour-packages', 'Vietnam', 'suzu-card-vietnam', 'Hanoi, Ha Long, Hoi An'),
       ('bali-tour-packages', 'Bali', 'suzu-card-bali', 'Ubud, villas, temples')]

def build():
    W = "Hi Suzu Travels, I'm planning a Japan trip. Please share a quote."
    h = [f'<div class="suzu-intl hx hx-country"><style>{CSS}</style>']
    slides = ''.join(f'<div class="hx-slide"><img src="{U(s)}" alt="{A(s)}" width="1600" height="1000" {"fetchpriority=\"high\" loading=\"eager\"" if i == 0 else "loading=\"lazy\""} decoding="async"><span class="hx-cap">{C(s)}</span></div>' for i, s in enumerate(HERO))
    h.append('<section class="hx-hero" aria-label="Japan tour packages from India"><div class="hx-slides">' + slides + '</div><div class="hx-copy">'
             '<p class="hx-lede">The Shibuya crossing and Tokyo Tower at night, Mount Fuji over Lake Kawaguchi, the orange torii tunnels of Fushimi Inari, Kyoto\'s temples and Osaka\'s street food — Japan is a once-in-a-lifetime holiday for Indian travellers. We plan it to your dates, your budget and your pace, with honest visa guidance from the start.</p>'
             '<div class="hx-badges">'
             f'<span class="hx-badge">{svg("globe")}Tokyo, Fuji, Kyoto &amp; Osaka</span><span class="hx-badge">{svg("food")}Vegetarian meals planned</span>'
             f'<span class="hx-badge">{svg("team")}Families, couples &amp; groups</span><span class="hx-badge">{svg("doc")}Honest eVISA guidance</span></div>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Get a Japan Quote {svg("arrow")}</a>'
             f'<a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div></div>'
             '<form class="hx-plan" id="hxPlan" aria-label="Get a costed Japan itinerary on WhatsApp"><h3>Plan my Japan trip</h3>'
             '<p>Tell us the basics — we reply on WhatsApp with a costed, day-by-day plan, usually within 24 hours.</p><div class="hx-f">'
             '<label class="hx-full">Trip<select name="d"><option>Tokyo only</option><option selected>Tokyo + Mount Fuji + Kyoto + Osaka</option><option>Tokyo + Kyoto</option><option>Cherry blossom trip (late Mar – Apr)</option><option>Autumn leaves trip (Oct – Nov)</option><option>Family trip with Disney / Universal</option><option>Hokkaido snow trip (winter)</option></select></label>'
             '<label>Trip type<select name="s"><option>Family</option><option>Honeymoon / couple</option><option>Friends</option><option>Group</option><option>Corporate / MICE</option></select></label>'
             f'<label>Travel month<select name="m">{G.months()}</select></label>'
             '<label>Adults<select name="a"><option>1</option><option selected>2</option><option>3</option><option>4</option><option>5</option><option>6</option><option>7–10</option><option>11–20</option><option>20+</option></select></label>'
             '<label>Children<select name="k"><option>0</option><option>1</option><option>2</option><option>3</option><option>4+</option></select></label>'
             '<label class="hx-full">Departing from<input name="c" type="text" placeholder="e.g. Delhi, Mumbai, Chandigarh" autocomplete="address-level2"></label></div>'
             f'<button class="hx-btn" type="submit">{WA_SVG}Get my Japan plan on WhatsApp</button><small>Opens WhatsApp with your details filled in. We do not store anything on this page.</small></form></section>')
    h.append('<div class="hx-trust">'
             f'<div>{svg("clock")}<span><b>Quote in ~24 hours</b><span>Costed, day by day</span></span></div>'
             f'<div>{svg("doc")}<span><b>Honest visa guidance</b><span>Official rules, checked</span></span></div>'
             f'<div>{svg("shield")}<span><b>HP Tourism registered</b><span>Reg. DTO-MND-11-243/2022</span></span></div>'
             f'<div>{svg("chat")}<span><b>One team, start to finish</b><span>On WhatsApp while you travel</span></span></div></div>')
    h.append('<nav class="hx-toc" aria-label="On this page"><a href="#why-japan">Why Japan</a><a href="#japan-in-photos">Photos</a><a href="#how-to-choose">Choose your trip</a><a href="#sample-itinerary">Sample itinerary</a><a href="#when-to-go">When to go</a><a href="#visa-and-entry">Visa &amp; entry</a><a href="#whats-included">What\'s included</a><a href="#japan-faq">FAQ</a></nav>')
    facts = [('Getting there', 'Flights to Tokyo or Osaka — we compare options from your city'), ('Time difference', 'Japan is 3 hr 30 min ahead of IST'), ('Currency', 'Japanese Yen (JPY)'),
             ('Best season', 'Late Mar to May; October to November'), ('Typical trip', '7 to 10 nights'), ('Language', 'Japanese; English signs on trains and in big cities')]
    h.append('<section id="why-japan" class="hx-sec"><span class="hx-eye">Japan · Land of the Rising Sun</span><h2>Why Japan is worth the planning for Indian travellers</h2>'
             '<p class="hx-sub">Japan puts a giant modern city, old temple towns and mountain scenery within a few hours of each other, joined by the Shinkansen bullet train. Tokyo has the Shibuya crossing, Asakusa\'s Senso-ji temple and Tokyo Tower; Mount Fuji rises over the lakes of Kawaguchiko and the hills of Hakone; Kyoto keeps the Golden Pavilion, Kiyomizu-dera, the bamboo grove of Arashiyama and the torii gates of Fushimi Inari; Nara\'s deer wander around Todai-ji; and Osaka is Japan\'s street-food city. It is clean, safe and punctual — the visa just needs to be started early.</p>'
             '<div class="hx-facts">' + ''.join(f'<div class="hx-fact"><b>{a}</b><span>{b}</span></div>' for a, b in facts) + '</div></section>')
    h.append('<section id="japan-in-photos" class="hx-sec"><span class="hx-eye">Real places</span><h2>Japan in photos</h2>'
             '<p class="hx-sub">Kyoto\'s temples and torii gates, the Shibuya crossing, the Arashiyama bamboo grove, the Shinkansen, the deer of Nara and Tokyo Tower — the places on a classic Suzu Japan itinerary. Photos by Unsplash photographers, credited below.</p><div class="hx-pg">'
             + ''.join(f'<figure><img src="{U(k)}" alt="{A(k)}" width="800" height="600" loading="lazy" decoding="async"><figcaption>{C(k)}</figcaption></figure>' for k in GAL) + '</div></section>')
    cards = [('Couples', 'Honeymoon', 'A Tokyo hotel with a city view, a ryokan night with a private bath near Mount Fuji or in Hakone, and slow evenings in Kyoto\'s Gion. Cherry blossom or autumn dates make it special.'),
             ('First trip to Japan', 'Classic Golden Route', 'Tokyo, Mount Fuji, Kyoto, Nara and Osaka in 7–8 nights, with the bullet train in between — the trip most first-time visitors from India choose.'),
             ('Families', 'Family holiday', 'Tokyo Disney Resort, Universal Studios Japan, the Nara deer park and short travel days, with rooms that fit a family and luggage sent ahead between cities.'),
             ('Groups', 'Groups &amp; corporate', 'Coaches with English-speaking guides, group rail reservations, factory and study visits, and team dinners. Tell us the group size and we quote accordingly, including B2B for travel agents.')]
    stays = [('Shinjuku or Ginza, Tokyo', 'Big stations, shopping and food on the doorstep. Shinjuku is the easiest base for day trips to Mount Fuji; Ginza and Tokyo Station suit the bullet train.'),
             ('Lake Kawaguchi or Hakone', 'One night near Mount Fuji — lake-side hotels or a ryokan with hot-spring baths. Fuji is often hidden by cloud, so a night here gives you a second chance to see it.'),
             ('Central Kyoto', 'Stay near Kyoto Station or Shijo and Gion for easy buses and trains to the temples. Kyoto fills up fast in cherry blossom and autumn weeks.'),
             ('Namba, Osaka', 'Next to Dotonbori\'s food streets and well connected to Kansai airport, Universal Studios Japan and Nara.')]
    h.append('<section id="how-to-choose" class="hx-sec"><span class="hx-eye">How to choose</span><h2>Choose the Japan trip that fits you</h2>'
             '<p class="hx-sub">Start from the kind of trip you want — we fine-tune the days, hotels and pace to your group.</p><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><span class="hx-tag">{t}</span><h3>{n}</h3><p>{d}</p></div>' for t, n, d in cards) + '</div>'
             '<h3 style="margin-top:30px">Where to stay — it shapes your whole trip</h3><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><h3>{n}</h3><p>{d}</p></div>' for n, d in stays) + '</div></section>')
    days = [('Day 1', 'Arrive in Tokyo', 'Airport pickup and hotel check-in. An easy first evening around Shinjuku or Shibuya, and the Shibuya crossing after dark.'),
            ('Day 2', 'Tokyo old and new', 'Senso-ji temple and Nakamise street in Asakusa, the Meiji Jingu shrine and Harajuku, then Tokyo Tower or a city observation deck at sunset.'),
            ('Day 3', 'Tokyo your way', 'A day at Tokyo Disneyland or DisneySea, or Ginza, Akihabara and teamLab — your choice, planned around your group.'),
            ('Day 4', 'Mount Fuji &amp; Lake Kawaguchi', 'A drive to the Fuji Five Lakes for views of Mount Fuji across Lake Kawaguchi, the Chureito Pagoda and a lakeside or hot-spring stay.'),
            ('Day 5', 'Bullet train to Kyoto', 'The Shinkansen to Kyoto, then the thousands of torii gates at Fushimi Inari in the afternoon and an evening walk in Gion.'),
            ('Day 6', 'Kyoto temples', 'The Golden Pavilion of Kinkaku-ji, the Arashiyama bamboo grove and the wooden stage of Kiyomizu-dera with a local guide.'),
            ('Day 7', 'Nara &amp; Osaka', 'Todai-ji temple and the deer of Nara Park, then on to Osaka for dinner on the neon-lit Dotonbori food street.'),
            ('Day 8', 'Fly home', 'Breakfast, then the transfer to Kansai airport for your flight home.')]
    h.append('<section id="sample-itinerary" class="hx-sec"><span class="hx-eye">Sample plan</span><h2>A sample 8-day Tokyo, Mount Fuji, Kyoto &amp; Osaka itinerary</h2>'
             '<p class="hx-sub">The classic first trip to Japan. We rebuild it around you — Hakone instead of Kawaguchiko, Universal Studios in Osaka, Hiroshima and Miyajima for a longer trip, or Hokkaido in winter.</p><div class="hx-itin">'
             + ''.join(f'<div class="hx-day"><i>{a}</i><b>{b}</b><p>{c}</p></div>' for a, b, c in days) + '</div></section>')
    seasons = [('Mar – May', '<span class="hx-ok">Best</span>', 'Spring, mild', 'Cherry blossom usually opens in late March and early April in Tokyo and Kyoto — the busiest weeks, so book early. May is green and pleasant; avoid the Golden Week holidays in late April and early May if you can.'),
               ('Jun – Aug', '<span class="hx-mid">Good with care</span>', 'Rainy, then hot and humid', 'The rainy season runs from about June to mid-July on the main island, followed by hot, humid weeks. Good for festivals and Hokkaido; plan indoor options for the cities.'),
               ('Sep – Nov', '<span class="hx-ok">Best</span>', 'Cooler, clear days', 'Typhoons are still possible in September. October and November bring comfortable weather and autumn colours, with Kyoto\'s maples usually at their best in November.'),
               ('Dec – Feb', '<span class="hx-mid">Winter</span>', 'Cold, dry in the cities', 'Clear views of Mount Fuji and quieter temples. Snow in Hokkaido and the mountains, with the Sapporo Snow Festival in February.')]
    h.append('<section id="when-to-go" class="hx-sec"><span class="hx-eye">Best season</span><h2>When to go to Japan</h2>'
             '<p class="hx-sub">Spring and autumn suit most Indian travellers; winter is for snow and clear Fuji views. We check weather, blossom forecasts and Japanese holiday dates against your plan.</p>'
             '<div class="hx-tw"><table class="hx-t"><thead><tr><th>Months</th><th>Verdict</th><th>Weather</th><th>What it means for your trip</th></tr></thead><tbody>'
             + ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in seasons) + '</tbody></table></div></section>')
    h.append('<section id="visa-and-entry" class="hx-sec"><span class="hx-eye">Visa &amp; entry</span><h2>Visa and entry for Indian passport holders</h2>'
             '<div class="hx-visa"><div class="hx-vbox"><h3>What the official rules say</h3><ul>'
             '<li>Indian passport holders <b>need a visa</b> for a holiday in Japan. Since <b>1 April 2024</b>, Indian nationals and foreign nationals living in India can get a <b>single-entry short-term visa for tourism as an eVISA</b>.</li>'
             '<li>Applications from India are made through the <b>Japan Visa Application Centres (VFS Global)</b>, which are accredited by the Embassy and Consulates of Japan. The eVISA is issued electronically — there is no sticker in the passport.</li>'
             '<li>Japan\'s eVISA FAQ says examination <b>normally takes 5 working days</b>, but it <b>can take more than a month</b> at busy times or if more documents are needed. The eVISA is <b>valid for 3 months after issue</b> and for <b>one entry</b>; the permitted stay is up to <b>90 days</b>, as decided by the issuing office.</li>'
             '<li>At the airport you show the <b>visa issuance notice on your phone with internet access</b>. PDFs, screenshots and printouts are <b>not accepted</b>.</li>'
             '<li>Visa appointments drive the timeline, so we suggest starting <b>at least four to six weeks before travel</b> — earlier for cherry blossom and autumn dates.</li></ul>'
             f'<p class="hx-checked">Checked {CHECKED} · sources: <a href="{SRC_MOFA}" target="_blank" rel="noopener nofollow">Ministry of Foreign Affairs of Japan — JAPAN eVISA</a> · <a href="{SRC_FAQ}" target="_blank" rel="noopener nofollow">JAPAN eVISA — frequently asked questions</a> · <a href="{SRC_BLR}" target="_blank" rel="noopener nofollow">Consulate-General of Japan in Bengaluru — the JAPAN eVISA system in India</a></p></div>'
             '<div class="hx-vnote"><p><b>Please note:</b> visa approval and entry at the border are always the decision of the Japanese authorities. We guide you through the documents and timelines honestly, but we never promise an outcome we do not control.</p>'
             '<p>Apply only through the official channel — the Japan Visa Application Centre for your region — and keep your hotel bookings and return ticket handy for the immigration desk.</p></div></div></section>')
    inc = [('doc', 'Visa guidance', 'A clear document checklist and help preparing your eVISA application for the Japan Visa Application Centre.'), ('pin', 'Hotels in the right area', 'Named hotels near the right stations in Tokyo, Kyoto and Osaka, and a lake-side hotel or ryokan near Mount Fuji.'),
           ('team', 'Transfers &amp; rail', 'Airport transfers, Shinkansen tickets or a rail pass where it saves money, and luggage forwarding between cities.'), ('globe', 'Guided sightseeing', 'English-speaking guides for Tokyo and Kyoto, Mount Fuji day plans, and theme-park tickets if you want them.'),
           ('food', 'Meal plan', 'Breakfast as standard; vegetarian and Jain needs noted with hotels, plus restaurant suggestions for each day.'), ('award', 'Flights optional', 'Land-only, or a full package with international flights from your nearest Indian airport.')]
    h.append('<section id="whats-included" class="hx-sec"><span class="hx-eye">Your package</span><h2>What a Suzu Japan package includes</h2><div class="hx-inc">'
             + ''.join(f'<div>{svg(i)}<span><b>{t}</b><span>{d}</span></span></div>' for i, t, d in inc) + '</div></section>')
    steps = [('chat', 'Tell us the basics', 'Dates, travellers and the kind of Japan trip you want. A WhatsApp message is enough.'),
             ('doc', 'Get a costed itinerary', 'A day-by-day plan with named hotels and a clear per-person price, usually within 24 hours.'),
             ('sliders', 'Adjust until it fits', 'Add Hiroshima, a ryokan night or a theme park, upgrade a hotel, change the pace. We re-quote as needed.'),
             ('lock', 'Confirm with a token', 'Lock your rate with a small token amount; the balance is paid later, as agreed in writing.')]
    h.append('<section id="how-booking-works" class="hx-sec"><span class="hx-eye">Simple process</span><h2>How booking works</h2><div class="hx-steps">'
             + ''.join(f'<div class="hx-step"><div class="hx-n">{svg(i)}</div><b>{t}</b><p>{d}</p></div>' for i, t, d in steps) + '</div></section>')
    h.append('<section id="japan-faq" class="hx-sec"><span class="hx-eye">FAQ</span><h2>Common questions about Japan</h2><div class="hx-faqs">'
             + ''.join(f'<details class="hx-faq"{" open" if k == 0 else ""}><summary>{html.escape(q)}</summary><div class="hx-ans"><p>{html.escape(a)}</p></div></details>' for k, (q, a) in enumerate(FAQ)) + '</div></section>')
    h.append('<section id="more-destinations" class="hx-sec"><span class="hx-eye">Explore more</span><h2>Explore more destinations</h2>'
             '<p class="hx-sub">Every trip is planned the same way — your dates, your budget, one team from quote to return. <a href="https://suzutravels.com/international-tour-packages/">See all international holidays →</a></p><div class="hx-mini">'
             + ''.join(f'<a class="hx-mc" href="https://suzutravels.com/{p}/"><img src="https://suzutravels.com/wp-content/uploads/2026/10/{img}.webp" alt="{html.escape(n)} holiday — Suzu Travels" width="640" height="360" loading="lazy" decoding="async"><span><b>{html.escape(n)}</b><em>{html.escape(e)}</em></span></a>' for p, n, img, e in REL) + '</div></section>')
    h.append(f'<div class="hx-final"><img src="{U("japan-5")}" alt="{A("japan-5")}" width="1600" height="900" loading="lazy" decoding="async">'
             '<h2>Plan your Japan trip</h2><p>Send us your dates and group size. We will come back with a costed, day-by-day Japan itinerary you can compare — no obligation.</p>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Request a Japan Quote {svg("arrow")}</a><a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div>'
             '<p class="hx-contact">Or call <strong>+91 70874 88961</strong> · <a href="mailto:info@suzutravels.com">info@suzutravels.com</a></p></div>')
    seen = []
    for k in HERO + GAL + ['japan-5']:
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
    open('pages/japan-tour-packages.html', 'w').write(o)
    print('pages/japan-tour-packages.html', len(o))
