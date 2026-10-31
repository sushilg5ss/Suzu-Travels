#!/usr/bin/env python3
"""Kazakhstan (Almaty) + Kyrgyzstan page — .hx design; same template as gen_australia.py.
Run from outbound-kit/:  python3 pages/gen_kazakhstan.py <PAGE_ID> -> pages/kazakhstan-tour-packages.html (one line)
Facts: Kazakhstan — Embassy of Kazakhstan in India news 398872 (11 Jul 2022, re-read 31 Oct 2026): Government Decree 464 of 7 Jul 2022 — Indian citizens visa-free, continuous stay up to 14 days, max 42 days within every 180 days; applies to business, private and tourist purposes. Passport validity / registration NOT stated there — not stated on the page.
Kyrgyzstan — official e-Visa portal evisa.e-gov.kg "Do I need visa?" (India, ordinary passport; read 30 Oct 2026): visa needed; tourist e-visa validity up to 30 calendar days; review 5 working days; passport valid >= 6 months after visa validity with >= 2 free pages; separate e-visa per traveller incl. children; fee non-refundable; avoid buying air tickets before approval; registration at place of stay within 5 working days unless exempt (exempt list not checked). Embassy of India Bishkek advisory (re-read 31 Oct 2026): Cabinet Decree No. 312 of 30 Apr 2026 introduced a new visa procedure; overstays need an exit visa with fees.
Keyword Planner IN 30 Oct 2026: "almaty tour package" 2,400/mo, "kazakhstan trip cost from india" 480/mo, "kazakhstan tour package from india" 390/mo (focus kw), "almaty tour package from india" 210/mo, "kyrgyzstan tour package from india" 140/mo.
Photos: Wikimedia Commons (CC0 / CC BY / CC BY-SA, file pages checked 31 Oct 2026) + existing hub card (Unsplash).
"""
import json, html, sys, os
sys.path.insert(0, os.getcwd())
import gen_hub as G

PID = int(sys.argv[1]) if len(sys.argv) > 1 else 0
M = G.M
svg, WA_SVG, wa = G.svg, G.WA_SVG, G.wa
CHECKED = '31 October 2026'
SRC_KZ = 'https://www.gov.kz/memleket/entities/mfa-delhi/press/news/details/398872?lang=en'
SRC_KG = 'https://evisa.e-gov.kg/'
SRC_KGIN = 'https://indembbishkek.gov.in/docs/1781168326ADV-VISA%20REGLTN.pdf'

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
body.page-id-PID .page-header:before{content:"Holidays abroad \00B7  Kazakhstan";display:inline-block;font:800 12px/1 "Plus Jakarta Sans",sans-serif;letter-spacing:.18em;text-transform:uppercase;color:#1a1606;background:#E2C158;padding:8px 13px;border-radius:999px;margin-bottom:16px}
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
HERO = ['kazakhstan-1', 'kazakhstan-2', 'kazakhstan-10', 'kazakhstan-4', 'kazakhstan-5', 'kazakhstan-6']
GAL = ['kazakhstan-7', 'kazakhstan-8', 'kazakhstan-9', 'kazakhstan-12', 'kazakhstan-11', 'kazakhstan-13', 'kazakhstan-14', 'kazakhstan']
FINAL = 'kazakhstan-15'

FAQ = [
    ("Do Indians need a visa for Kazakhstan?", "No visa is needed for a short holiday. The Embassy of Kazakhstan in India says that under Government Decree No. 464 of 7 July 2022, Indian citizens can stay in Kazakhstan without a visa for up to 14 days at a time, and for a maximum of 42 days within every 180 days, for business, private and tourist trips. Entry is always the decision of the Kazakh border authorities. We checked this on 31 October 2026 and re-check it before every booking."),
    ("Do Indians need a visa for Kyrgyzstan?", "Yes. The official Kyrgyz e-Visa portal (evisa.e-gov.kg) shows that Indian ordinary passport holders need a visa. A tourist e-visa is valid for up to 30 days, review takes about 5 working days, each traveller (children included) needs a separate e-visa, and the portal advises not buying air tickets before the approval notice. Your passport should be valid for at least 6 months after the visa ends, with at least 2 blank pages. Kyrgyzstan changed its visa procedure in 2026 (Cabinet Decree No. 312 of 30 April 2026), so we re-check the rules for your dates. Issuing a visa is always the decision of the Kyrgyz authorities."),
    ("How many days are enough for Almaty and Kazakhstan?", "Five to six nights covers Almaty city, Medeu and Shymbulak, Big Almaty Lake, and a two-day trip to Charyn Canyon, Kolsay and Kaindy lakes. With three or four nights, keep to Almaty and the mountains just above the city. Add three or four nights for Bishkek, Ala-Archa and Lake Issyk-Kul in Kyrgyzstan."),
    ("Which is the best time to visit Almaty from India?", "May to September is best for the lakes, canyons and mountain walks, when the roads to Kolsay and Kaindy are open and the hills are green. December to March is snow season, when Shymbulak is a ski resort and Medeu is used for skating. April and October are shoulder months with changeable mountain weather."),
    ("Can we combine Kazakhstan with Kyrgyzstan?", "Yes. Almaty and Bishkek are close, and a road transfer between them is a common way to combine the two. In Kyrgyzstan we usually add Ala-Archa National Park, the Burana Tower and a stay on Lake Issyk-Kul. Remember that Kyrgyzstan needs a separate e-visa for Indian passport holders, so we plan the order of the trip around it."),
    ("Is vegetarian and Indian food available in Almaty?", "Kazakh food is meat-heavy, but Almaty is a large city with Indian restaurants, cafes, salads, bread, fruit and vegetable dishes. On mountain and lake days, choices are smaller, so we note vegetarian and Jain needs with hotels and drivers in advance and suggest where to eat."),
    ("Why are there no prices on this page?", "Kazakhstan costs depend on your dates, hotel category, private car or small-group day trips, the Kyrgyzstan add-on and the airfare from your city. Instead of a teaser price that changes when you ask, we send a costed, day-by-day quote for your dates — usually within 24 hours."),
]

JS = ("(function(){var f=document.getElementById('hxPlan');if(!f){return;}f.addEventListener('submit',function(e){e.preventDefault();"
      "var d=f.querySelector('[name=d]').value,s=f.querySelector('[name=s]').value,m=f.querySelector('[name=m]').value,a=f.querySelector('[name=a]').value,k=f.querySelector('[name=k]').value,c=f.querySelector('[name=c]').value;"
      "var t='Hi Suzu Travels, please send me a costed Kazakhstan itinerary.\\nTrip: '+d+'\\nTrip type: '+s+'\\nTravel month: '+m+'\\nAdults: '+a+'\\nChildren: '+k;"
      "if(c){t=t+'\\nDeparting from: '+c;}"
      "window.open('https:'+String.fromCharCode(47,47)+'wa.me/917087488961?text='+encodeURIComponent(t),'_blank','noopener');});})();")

REL = [('dubai-tour-packages', 'Dubai', 'suzu-abroad-dubai', 'Burj Khalifa, desert, Abu Dhabi'), ('turkey-tour-packages', 'Turkey', 'suzu-abroad-turkey', 'Istanbul, Cappadocia, Pamukkale'),
       ('georgia-tour-packages', 'Georgia', 'suzu-abroad-georgia', 'Tbilisi, Kazbegi, Gudauri'), ('azerbaijan-tour-packages', 'Azerbaijan', 'suzu-abroad-azerbaijan', 'Baku, Gabala, Shahdag'),
       ('uzbekistan-tour-packages', 'Uzbekistan', 'suzu-abroad-uzbekistan', 'Samarkand, Bukhara, Khiva'),
       ('egypt-tour-packages', 'Egypt', 'suzu-abroad-egypt', 'Cairo, Nile cruise, Luxor'), ('europe-tour-packages', 'Europe', 'suzu-abroad-europe', 'Paris, Swiss Alps, Italy'),
       ('switzerland-tour-packages', 'Switzerland', 'suzu-abroad-switzerland', 'Lucerne, Jungfrau, Zermatt'), ('uk-tour-packages', 'UK', 'suzu-abroad-uk', 'London, Cotswolds, Scotland'),
       ('japan-tour-packages', 'Japan', 'suzu-abroad-japan', 'Tokyo, Fuji, Kyoto, Osaka'), ('australia-tour-packages', 'Australia & NZ', 'suzu-abroad-australia', 'Sydney, Melbourne, Queenstown'),
       ('mauritius-tour-packages', 'Mauritius', 'suzu-abroad-mauritius', 'Lagoons, Le Morne, island tours'), ('maldives-tour-packages', 'Maldives', 'suzu-card-maldives', 'Overwater villas'),
       ('bali-tour-packages', 'Bali', 'suzu-card-bali', 'Ubud, villas, temples'), ('thailand-tour-packages', 'Thailand', 'suzu-card-thailand', 'Bangkok, Phuket, Krabi'),
       ('singapore-tour-packages', 'Singapore', 'suzu-card-singapore', 'City, Sentosa, Universal'), ('malaysia-tour-packages', 'Malaysia', 'suzu-card-malaysia', 'KL, Langkawi, Genting'),
       ('vietnam-tour-packages', 'Vietnam', 'suzu-card-vietnam', 'Hanoi, Ha Long, Hoi An'), ('sri-lanka-tour-packages', 'Sri Lanka', 'suzu-card-sri-lanka', 'Beaches & tea country'),
       ('nepal-tour-packages', 'Nepal', 'suzu-card-nepal', 'No visa for Indians'), ('bhutan-tour-packages', 'Bhutan', 'suzu-card-bhutan', 'Paro, Thimphu, Punakha')]

def build():
    W = "Hi Suzu Travels, I'm planning a Kazakhstan (Almaty) trip. Please share a quote."
    h = [f'<div class="suzu-intl hx hx-country"><style>{CSS}</style>']
    slides = ''.join(f'<div class="hx-slide"><img src="{U(s)}" alt="{A(s)}" width="1600" height="1000" {"fetchpriority=\"high\" loading=\"eager\"" if i == 0 else "loading=\"lazy\""} decoding="async"><span class="hx-cap">{C(s)}</span></div>' for i, s in enumerate(HERO))
    h.append('<section class="hx-hero" aria-label="Kazakhstan and Almaty tour packages from India"><div class="hx-slides">' + slides + '</div><div class="hx-copy">'
             '<p class="hx-lede">Turquoise Big Almaty Lake, the red walls of Charyn Canyon, the sunken forest of Lake Kaindy, ski slopes at Shymbulak and a green, mountain-backed city — Almaty is one of the easiest mountain holidays abroad for Indian travellers, with no visa needed for a short trip. Add Kyrgyzstan for Ala-Archa and Lake Issyk-Kul. We plan it to your dates, budget and pace, with good hotels, private drivers and honest entry guidance.</p>'
             '<div class="hx-badges">'
             f'<span class="hx-badge">{svg("globe")}Almaty, lakes, canyons &amp; Kyrgyzstan</span><span class="hx-badge">{svg("doc")}Visa-free for Indians (up to 14 days)</span>'
             f'<span class="hx-badge">{svg("team")}Families, couples &amp; groups</span><span class="hx-badge">{svg("food")}Vegetarian meals planned</span></div>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Get a Kazakhstan Quote {svg("arrow")}</a>'
             f'<a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div></div>'
             '<form class="hx-plan" id="hxPlan" aria-label="Get a costed Kazakhstan itinerary on WhatsApp"><h3>Plan my Kazakhstan trip</h3>'
             '<p>Tell us the basics — we reply on WhatsApp with a costed, day-by-day plan, usually within 24 hours.</p><div class="hx-f">'
             '<label class="hx-full">Trip<select name="d"><option selected>Almaty + lakes + Charyn Canyon</option><option>Almaty city + mountains (short trip)</option><option>Kazakhstan + Kyrgyzstan</option><option>Almaty snow / ski holiday (winter)</option><option>Kazakhstan + Uzbekistan</option><option>Almaty honeymoon</option><option>Not sure yet</option></select></label>'
             '<label>Trip type<select name="s"><option>Family</option><option>Honeymoon / couple</option><option>Friends</option><option>Seniors</option><option>Group</option><option>Corporate / MICE</option></select></label>'
             f'<label>Travel month<select name="m">{G.months()}</select></label>'
             '<label>Adults<select name="a"><option>1</option><option selected>2</option><option>3</option><option>4</option><option>5</option><option>6</option><option>7–10</option><option>11–20</option><option>20+</option></select></label>'
             '<label>Children<select name="k"><option>0</option><option>1</option><option>2</option><option>3</option><option>4+</option></select></label>'
             '<label class="hx-full">Departing from<input name="c" type="text" placeholder="e.g. Delhi, Mumbai, Chandigarh" autocomplete="address-level2"></label></div>'
             f'<button class="hx-btn" type="submit">{WA_SVG}Get my Kazakhstan plan on WhatsApp</button><small>Opens WhatsApp with your details filled in. We do not store anything on this page.</small></form></section>')
    h.append('<div class="hx-trust">'
             f'<div>{svg("clock")}<span><b>Quote in ~24 hours</b><span>Costed, day by day</span></span></div>'
             f'<div>{svg("doc")}<span><b>Honest entry guidance</b><span>Official Kazakh &amp; Kyrgyz rules, checked</span></span></div>'
             f'<div>{svg("shield")}<span><b>HP Tourism registered</b><span>Reg. DTO-MND-11-243/2022</span></span></div>'
             f'<div>{svg("chat")}<span><b>One team, start to finish</b><span>On WhatsApp while you travel</span></span></div></div>')
    h.append('<nav class="hx-toc" aria-label="On this page"><a href="#why-kazakhstan">Why Kazakhstan</a><a href="#kazakhstan-in-photos">Photos</a><a href="#how-to-choose">Choose your trip</a><a href="#sample-itinerary">Sample itinerary</a><a href="#when-to-go">When to go</a><a href="#visa-and-entry">Visa</a><a href="#whats-included">What\'s included</a><a href="#kazakhstan-faq">FAQ</a></nav>')
    facts = [('Getting there', 'Fly into Almaty; we compare routes and connections from your city'), ('Time difference', 'Kazakhstan is 30 minutes behind India'), ('Currency', 'Kazakhstani tenge (KZT); Kyrgyz som in Kyrgyzstan'),
             ('Best season', 'May to September; December to March for snow'), ('Typical trip', '5 to 6 nights for Almaty; 8 to 10 with Kyrgyzstan'), ('Visa', 'Kazakhstan: visa-free up to 14 days. Kyrgyzstan: e-visa needed')]
    h.append('<section id="why-kazakhstan" class="hx-sec"><span class="hx-eye">Kazakhstan</span><h2>Why Almaty and Kazakhstan work so well for Indian travellers</h2>'
             '<p class="hx-sub">Almaty sits right below the snowy Tian Shan mountains: in under an hour you are at the Medeu skating rink, the Shymbulak ski resort or Big Almaty Lake, and day trips reach Charyn Canyon and the Kolsay and Kaindy lakes. There is no visa for short trips on an Indian passport, the city is modern and easy to get around, and Kyrgyzstan&rsquo;s lakes and valleys are a short drive away.</p>'
             '<div class="hx-facts">' + ''.join(f'<div class="hx-fact"><b>{a}</b><span>{b}</span></div>' for a, b in facts) + '</div></section>')
    h.append('<section id="kazakhstan-in-photos" class="hx-sec"><span class="hx-eye">Real places</span><h2>Kazakhstan &amp; Kyrgyzstan in photos</h2>'
             '<p class="hx-sub">Kolsay Lake, the painted domes of Zenkov Cathedral, Almaty from Kok Tobe, the Ala-Archa valley and the Medeu rink, the Burana Tower, a beach on Lake Issyk-Kul and Big Almaty Lake. Real photos by Wikimedia Commons and Unsplash photographers, credited below.</p><div class="hx-pg">'
             + ''.join(f'<figure><img src="{U(k)}" alt="{A(k)}" width="800" height="600" loading="lazy" decoding="async"><figcaption>{C(k)}</figcaption></figure>' for k in GAL) + '</div></section>')
    cards = [('Families', 'Almaty with children', 'Short drives, cable cars up to Kok Tobe and Shymbulak, lake picnics and family rooms in central hotels — no long days on the road.'),
             ('Couples', 'Honeymoon in the mountains', 'Sunset over the city from Kok Tobe, a quiet morning at Big Almaty Lake, a night near the Kolsay lakes and a cosy mountain hotel at Shymbulak.'),
             ('Snow lovers', 'Winter &amp; ski trip', 'December to March: skiing or snow play at Shymbulak, skating at Medeu and snowy city sights, with warm gear and transfers arranged.'),
             ('Two countries', 'Kazakhstan + Kyrgyzstan', 'Almaty with Bishkek, Ala-Archa National Park, the Burana Tower and Lake Issyk-Kul, linked by road, with the Kyrgyz e-visa planned in advance.')]
    stays = [('Almaty city centre', 'A central hotel near Panfilov Park or the Arbat keeps the city sights, cafes and the Kok Tobe cable car close.'),
             ('Shymbulak / Medeu', 'A mountain hotel near Medeu or at Shymbulak suits ski trips and couples who want the snow at the door.'),
             ('Saty village', 'A simple guesthouse in Saty breaks the long drive and puts Kolsay and Kaindy lakes within easy reach.'),
             ('Issyk-Kul (Kyrgyzstan)', 'A lakeside resort near Cholpon-Ata or Bosteri for two or three slow days on Lake Issyk-Kul.')]
    h.append('<section id="how-to-choose" class="hx-sec"><span class="hx-eye">How to choose</span><h2>Choose the Kazakhstan trip that fits you</h2>'
             '<p class="hx-sub">Start from the kind of trip you want — we fine-tune the days, hotels, drivers and guides to your group.</p><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><span class="hx-tag">{t}</span><h3>{n}</h3><p>{d}</p></div>' for t, n, d in cards) + '</div>'
             '<h3 style="margin-top:30px">Where to stay</h3><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><h3>{n}</h3><p>{d}</p></div>' for n, d in stays) + '</div></section>')
    days = [('Day 1', 'Arrive in Almaty', 'Airport pickup and hotel. An easy walk in Panfilov Park past Zenkov Cathedral, then the Green Bazaar, and sunset from Kok Tobe by cable car.'),
            ('Day 2', 'Medeu &amp; Shymbulak', 'Drive up to the Medeu rink, then cable cars at Shymbulak for mountain views (or skiing in winter). Evening on the Arbat.'),
            ('Day 3', 'Big Almaty Lake', 'A morning trip to the turquoise Big Almaty Lake in Ile-Alatau National Park. Free afternoon in the city.'),
            ('Day 4', 'Charyn Canyon', 'A long scenic drive to Charyn Canyon and its Valley of Castles, then on to Saty village for the night.'),
            ('Day 5', 'Kaindy &amp; Kolsay lakes', 'Lake Kaindy and its sunken forest, then the first Kolsay lake, before driving back to Almaty.'),
            ('Day 6', 'Fly home', 'Free morning for shopping, then transfer to Almaty airport — or carry on to Bishkek and Lake Issyk-Kul in Kyrgyzstan.')]
    h.append('<section id="sample-itinerary" class="hx-sec"><span class="hx-eye">Sample plan</span><h2>A sample 6-day Almaty, lakes &amp; Charyn Canyon itinerary</h2>'
             '<p class="hx-sub">The classic first trip to Kazakhstan. We rebuild it around you — a shorter city-and-mountains trip, a winter snow holiday, or three or four extra nights for Bishkek, Ala-Archa and Lake Issyk-Kul in Kyrgyzstan.</p><div class="hx-itin">'
             + ''.join(f'<div class="hx-day"><i>{a}</i><b>{b}</b><p>{c}</p></div>' for a, b, c in days) + '</div></section>')
    seasons = [('May – Sep', '<span class="hx-ok">Best</span>', 'Late spring &amp; summer', 'Green mountains, open roads to Kolsay and Kaindy, and the best months for Big Almaty Lake, Charyn Canyon and Issyk-Kul. Summer school holidays from India fall here — book early.'),
               ('Dec – Mar', '<span class="hx-ok">Snow</span>', 'Winter, cold', 'Snow season: skiing and snow play at Shymbulak and skating at Medeu. Some mountain lakes and roads are harder to reach, so we plan around the snow.'),
               ('Apr &amp; Oct', '<span class="hx-mid">Shoulder</span>', 'Changeable', 'Fewer visitors and pleasant city days, but mountain weather can change quickly — we keep the plan flexible.'),
               ('Nov', '<span class="hx-mid">Quiet</span>', 'Cold, early snow', 'Between seasons: good for a city break, while the ski season and the lake season are both not yet at their best.')]
    h.append('<section id="when-to-go" class="hx-sec"><span class="hx-eye">Best season</span><h2>When to go to Almaty and Kazakhstan</h2>'
             '<p class="hx-sub">Almaty has warm summers and snowy winters, so there are two good seasons: summer for lakes and canyons, winter for snow. We check the season, road conditions and flight prices against your plan before we quote.</p>'
             '<div class="hx-tw"><table class="hx-t"><thead><tr><th>Months</th><th>Verdict</th><th>Weather</th><th>What it means for your trip</th></tr></thead><tbody>'
             + ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in seasons) + '</tbody></table></div></section>')
    h.append('<section id="visa-and-entry" class="hx-sec"><span class="hx-eye">Visa &amp; entry</span><h2>Kazakhstan and Kyrgyzstan visa for Indian passport holders</h2>'
             '<div class="hx-visa"><div class="hx-vbox"><h3>Kazakhstan — what the official rules say</h3><ul>'
             '<li>Under <b>Government Decree No. 464 of 7 July 2022</b>, Indian citizens can enter Kazakhstan <b>without a visa</b>.</li>'
             '<li>You can stay <b>up to 14 days continuously</b>, and <b>no more than 42 days within every 180 days</b>.</li>'
             '<li>The visa-free regime applies to <b>business, private and tourist</b> trips.</li></ul>'
             f'<p class="hx-checked">Checked {CHECKED} · source: <a href="{SRC_KZ}" target="_blank" rel="noopener nofollow">Embassy of the Republic of Kazakhstan in India</a></p>'
             '<h3 style="margin-top:20px">Kyrgyzstan add-on — what the official rules say</h3><ul>'
             '<li>Indian ordinary passport holders <b>need a visa</b> for Kyrgyzstan; it is applied for online on the <b>official e-Visa portal</b>.</li>'
             '<li>A <b>tourist e-visa is valid for up to 30 days</b>, and the application review takes about <b>5 working days</b>. Each traveller, <b>children included</b>, needs a separate e-visa; the fee is non-refundable.</li>'
             '<li>Your passport should be valid for <b>at least 6 months after the visa ends</b>, with <b>at least 2 blank pages</b>. The portal advises <b>not buying air tickets before the approval notice</b>.</li>'
             '<li>Kyrgyzstan adopted a <b>new visa procedure</b> (Cabinet Decree No. 312 of 30 April 2026), and overstays need a paid exit visa — we re-check the rules, including registration of stay, for your dates.</li></ul>'
             f'<p class="hx-checked">Checked 30–31 October 2026 · sources: <a href="{SRC_KG}" target="_blank" rel="noopener nofollow">Kyrgyz Republic e-Visa portal</a> · <a href="{SRC_KGIN}" target="_blank" rel="noopener nofollow">Embassy of India, Bishkek — advisory on new visa regulations</a></p></div>'
             '<div class="hx-vnote"><p><b>Please note:</b> admission at the border is always the decision of the Kazakh authorities, and whether a visa is issued is always the decision of the authorities of the Kyrgyz Republic. We help you prepare a complete, honest application, but we never promise an outcome we do not control.</p>'
             '<p>We share a document checklist that matches your itinerary, give you a day-by-day plan and hotel details, and for Kyrgyzstan confirm non-refundable bookings only after your e-visa is approved.</p></div></div></section>')
    inc = [('doc', 'Entry guidance', 'A clear checklist for visa-free entry to Kazakhstan and, if you add it, the Kyrgyz e-visa.'), ('pin', 'Hotels', 'Named hotels in Almaty, a mountain or lake stay where it suits you, and lakeside resorts on Issyk-Kul.'),
           ('team', 'Private car &amp; driver', 'Airport transfers and a private car with driver for the mountains, lakes and Charyn Canyon.'), ('globe', 'Guides &amp; tickets', 'English-speaking guides where useful, plus cable car and park tickets as chosen.'),
           ('food', 'Meal plan', 'Breakfast at most hotels; vegetarian and Jain needs noted in advance, with restaurant suggestions.'), ('award', 'Flights optional', 'Land-only, or a full package with international flights from your nearest Indian airport.')]
    h.append('<section id="whats-included" class="hx-sec"><span class="hx-eye">Your package</span><h2>What a Suzu Kazakhstan package includes</h2><div class="hx-inc">'
             + ''.join(f'<div>{svg(i)}<span><b>{t}</b><span>{d}</span></span></div>' for i, t, d in inc) + '</div></section>')
    steps = [('chat', 'Tell us the basics', 'Dates, travellers and the kind of trip you want. A WhatsApp message is enough.'),
             ('doc', 'Get a costed itinerary', 'A day-by-day plan with named hotels and a clear per-person price, usually within 24 hours.'),
             ('sliders', 'Adjust until it fits', 'Change the days, hotels, car or the Kyrgyzstan add-on. We re-quote as needed.'),
             ('lock', 'Confirm with a token', 'Lock your plan with a small token amount; the balance is paid later, as agreed in writing.')]
    h.append('<section id="how-booking-works" class="hx-sec"><span class="hx-eye">Simple process</span><h2>How booking works</h2><div class="hx-steps">'
             + ''.join(f'<div class="hx-step"><div class="hx-n">{svg(i)}</div><b>{t}</b><p>{d}</p></div>' for i, t, d in steps) + '</div></section>')
    h.append('<section id="kazakhstan-faq" class="hx-sec"><span class="hx-eye">FAQ</span><h2>Common questions about a Kazakhstan tour</h2><div class="hx-faqs">'
             + ''.join(f'<details class="hx-faq"{" open" if k == 0 else ""}><summary>{html.escape(q)}</summary><div class="hx-ans"><p>{html.escape(a)}</p></div></details>' for k, (q, a) in enumerate(FAQ)) + '</div></section>')
    h.append('<section id="more-destinations" class="hx-sec"><span class="hx-eye">Explore more</span><h2>Explore more destinations</h2>'
             '<p class="hx-sub">Every trip is planned the same way — your dates, your budget, one team from quote to return. <a href="https://suzutravels.com/international-tour-packages/">See all international holidays →</a></p><div class="hx-mini">'
             + ''.join(f'<a class="hx-mc" href="https://suzutravels.com/{p}/"><img src="https://suzutravels.com/wp-content/uploads/2026/10/{img}.webp" alt="{html.escape(n)} holiday — Suzu Travels" width="640" height="360" loading="lazy" decoding="async"><span><b>{html.escape(n)}</b><em>{html.escape(e)}</em></span></a>' for p, n, img, e in REL) + '</div></section>')
    h.append(f'<div class="hx-final"><img src="{U(FINAL)}" alt="{A(FINAL)}" width="1600" height="900" loading="lazy" decoding="async">'
             '<h2>Plan your Kazakhstan trip</h2><p>Send us your dates and group size. We will come back with a costed, day-by-day Almaty itinerary you can compare, no obligation.</p>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Request a Kazakhstan Quote {svg("arrow")}</a><a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div>'
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
    open('pages/kazakhstan-tour-packages.html', 'w').write(o)
    print('pages/kazakhstan-tour-packages.html', len(o))
