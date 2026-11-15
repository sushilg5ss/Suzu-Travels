#!/usr/bin/env python3
"""Russia page — .hx design; same template as gen_china.py.
Run from outbound-kit/:  python3 pages/gen_russia.py <PAGE_ID> -> pages/russia-tour-packages.html (one line)
Facts (official pages read 15 Nov 2026, MFA of Russia e-visa portal electronic-visa.kdmid.ru):
- country_en.html: India is on the list of States whose nationals may get an e-visa.
- index_en.html: e-visa issued within 4 calendar days; no invitations; apply online, pay, notification shown to carrier + border.
- faq_en.html: processing excludes submission day; returned for correction within 2 days, then 4 days from resubmission;
  since 23 Aug 2025 single e-visa valid 120 days from issue, stay up to 30 days from entry, exit within 120 days;
  fee non-refundable, only cards issued outside Russia; each minor child separate application; purposes: guest, business,
  tourism, events (else paper visa at a mission); migration registration within 7 working days, hotels do it automatically;
  entry/exit only through approved checkpoints.
- checkpoint_en.html: includes Moscow Vnukovo, Domodedovo, Sheremetyevo, Zhukovsky; Saint Petersburg Pulkovo; Kazan.
- Visa-free group travel India-Russia: only media reports of talks (WebSearch 15 Nov 2026) — not stated as a rule.
Keyword Planner IN 15 Nov 2026: "russia tour package" 3,600/mo (focus kw), "russia tour package from india" 720,
"russia trip cost from india" 720, "russia visa for indians" 8,100, "india to russia visa price" 590, "moscow tour package" 260.
Photos: Wikimedia Commons (CC0 / CC BY / CC BY-SA; licence read from each file page's wikitext 15 Nov 2026), WP IDs 22470-22486
(used: 22470-22473, 22475-22479, 22482-22485; not used: 22474 dark Alexander Column, 22480 identifiable people on Zaryadye
bridge, 22481 drawbridge with watermark, 22486 Smolensk church — spare).
Climate/season wording is general guidance (no figures); no prices.
"""

import json, html, sys, os
sys.path.insert(0, os.getcwd())
import gen_hub as G

PID = int(sys.argv[1]) if len(sys.argv) > 1 else 0
M = G.M
svg, WA_SVG, wa = G.svg, G.WA_SVG, G.wa
CHECKED = '15 November 2026'
SRC_EV = 'https://evisa.kdmid.ru/'
SRC_KD = 'https://electronic-visa.kdmid.ru/index_en.html'
SRC_FAQ = 'https://electronic-visa.kdmid.ru/faq_en.html'
SRC_CTRY = 'https://electronic-visa.kdmid.ru/country_en.html'
SRC_CP = 'https://electronic-visa.kdmid.ru/checkpoint_en.html'

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
body.page-id-PID .page-header:before{content:"Holidays abroad \00B7  Russia";display:inline-block;font:800 12px/1 "Plus Jakarta Sans",sans-serif;letter-spacing:.18em;text-transform:uppercase;color:#1a1606;background:#E2C158;padding:8px 13px;border-radius:999px;margin-bottom:16px}
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
HERO = ['russia-1', 'russia-2', 'russia-3', 'russia-4', 'russia-5', 'russia-6']
GAL = ['russia-7', 'russia-8', 'russia-9', 'russia-10', 'russia-11', 'russia-12', 'russia-13']
FINAL = 'russia-2'  # reuses hero slide 2 (Kremlin from the Moskva River)

FAQ = [
    ("Do Indians need a visa for Russia?", "Yes. When we checked the official e-visa portal of the Russian Ministry of Foreign Affairs on 15 November 2026, India was on the list of countries whose nationals can apply for the Russian e-visa, and a visa was still needed for a holiday. The e-visa is applied for online, with no invitation needed, and the Ministry says it is issued within 4 calendar days (not counting the day you submit). Reports about a possible visa-free arrangement for Indian tour groups are not a rule until Russia officially brings one into force — we will update this page if that happens. Whether a visa is issued and whether you are admitted is always the decision of the Russian authorities."),
    ("How long can I stay in Russia on an e-visa?", "According to the official e-visa portal, since 23 August 2025 a single-entry e-visa is valid for 120 days from the date it is issued, and you can stay in Russia for up to 30 days from the date of entry. You must also leave Russia within the 120 days. For longer stays or purposes the e-visa does not cover, you apply for a regular (paper) visa at a Russian embassy or consulate."),
    ("Can I fly into any Russian airport on an e-visa?", "No — the e-visa is valid only for entry and exit through the border crossing points approved by the Russian Government, and you cannot leave through a checkpoint that is not on that list. The official list includes the Moscow airports (Sheremetyevo, Domodedovo, Vnukovo and Zhukovsky), Saint Petersburg (Pulkovo) and Kazan. We check your flights against the current list before you book."),
    ("How many days are enough for Moscow and Saint Petersburg?", "Seven or eight days is a comfortable first trip: three or four days in Moscow, a morning on the high-speed train, and three days in Saint Petersburg including Peterhof and Pushkin. Add two days for Kazan, or a day trip from Moscow to Sergiev Posad."),
    ("Which is the best time to visit Russia?", "Late May to early September is the most comfortable season for Moscow and Saint Petersburg, with long days — around midsummer Saint Petersburg has its famous White Nights. Winter, from December to February, is cold and snowy but beautiful, with New Year lights in Moscow; you need proper winter clothing. Spring and autumn are cooler and quieter."),
    ("Can I use my Indian debit or credit card in Russia?", "Do not count on it. The official e-visa portal itself says the visa fee can only be paid with cards issued outside Russia, and inside Russia many international cards do not work. We tell you the current, practical options for money before you travel, and keep your hotels, transfers and tours prepaid where possible."),
    ("Is vegetarian and Indian food available in Russia?", "Yes, in Moscow and Saint Petersburg there are Indian restaurants and places with vegetarian dishes; in smaller towns it takes more planning. We note vegetarian and Jain needs with hotels in advance and suggest restaurants on your route."),
    ("Why are there no prices on this page?", "Russia costs depend on your dates, hotel category, the train or flight between cities, palace and museum tickets, guides and the airfare from your city. Instead of a teaser price that changes when you ask, we send a costed, day-by-day quote for your dates — usually within 24 hours."),
]

JS = ("(function(){var f=document.getElementById('hxPlan');if(!f){return;}f.addEventListener('submit',function(e){e.preventDefault();"
      "var d=f.querySelector('[name=d]').value,s=f.querySelector('[name=s]').value,m=f.querySelector('[name=m]').value,a=f.querySelector('[name=a]').value,k=f.querySelector('[name=k]').value,c=f.querySelector('[name=c]').value;"
      "var t='Hi Suzu Travels, please send me a costed Russia itinerary.\\nTrip: '+d+'\\nTrip type: '+s+'\\nTravel month: '+m+'\\nAdults: '+a+'\\nChildren: '+k;"
      "if(c){t=t+'\\nDeparting from: '+c;}"
      "window.open('https:'+String.fromCharCode(47,47)+'wa.me/917087488961?text='+encodeURIComponent(t),'_blank','noopener');});})();")

REL = [('europe-tour-packages', 'Europe', 'suzu-abroad-europe', 'Paris, Swiss Alps, Italy'), ('switzerland-tour-packages', 'Switzerland', 'suzu-abroad-switzerland', 'Lucerne, Jungfrau, Zermatt'),
       ('uk-tour-packages', 'UK', 'suzu-abroad-uk', 'London, Cotswolds, Scotland'), ('turkey-tour-packages', 'Turkey', 'suzu-abroad-turkey', 'Istanbul, Cappadocia, Pamukkale'),
       ('georgia-tour-packages', 'Georgia', 'suzu-abroad-georgia', 'Tbilisi, Kazbegi, Gudauri'), ('azerbaijan-tour-packages', 'Azerbaijan', 'suzu-abroad-azerbaijan', 'Baku, Gabala, Shahdag'),
       ('armenia-tour-packages', 'Armenia', 'suzu-abroad-armenia', 'Yerevan, Garni, Sevan'), ('uzbekistan-tour-packages', 'Uzbekistan', 'suzu-abroad-uzbekistan', 'Samarkand, Bukhara, Khiva'),
       ('kazakhstan-tour-packages', 'Kazakhstan', 'suzu-abroad-kazakhstan', 'Almaty, lakes, Kyrgyzstan'), ('china-tour-packages', 'China', 'CN', 'Great Wall, Xi’an, Shanghai'),
       ('hong-kong-tour-packages', 'Hong Kong & Macau', 'HK', 'Harbour, Peak, Disneyland, Macau'), ('japan-tour-packages', 'Japan', 'suzu-abroad-japan', 'Tokyo, Fuji, Kyoto, Osaka'),
       ('dubai-tour-packages', 'Dubai', 'suzu-abroad-dubai', 'Burj Khalifa, desert, Abu Dhabi'), ('egypt-tour-packages', 'Egypt', 'suzu-abroad-egypt', 'Cairo, Nile cruise, Luxor'),
       ('singapore-tour-packages', 'Singapore', 'suzu-card-singapore', 'City, Sentosa, Universal'), ('thailand-tour-packages', 'Thailand', 'suzu-card-thailand', 'Bangkok, Phuket, Krabi'),
       ('malaysia-tour-packages', 'Malaysia', 'suzu-card-malaysia', 'KL, Langkawi, Genting'), ('vietnam-tour-packages', 'Vietnam', 'suzu-card-vietnam', 'Hanoi, Ha Long, Hoi An'),
       ('bali-tour-packages', 'Bali', 'suzu-card-bali', 'Ubud, villas, temples'), ('australia-tour-packages', 'Australia & NZ', 'suzu-abroad-australia', 'Sydney, Melbourne, Queenstown'),
       ('maldives-tour-packages', 'Maldives', 'suzu-card-maldives', 'Overwater villas'), ('mauritius-tour-packages', 'Mauritius', 'suzu-abroad-mauritius', 'Lagoons, Le Morne, island tours'),
       ('sri-lanka-tour-packages', 'Sri Lanka', 'suzu-card-sri-lanka', 'Beaches & tea country'), ('nepal-tour-packages', 'Nepal', 'suzu-card-nepal', 'No visa for Indians'),
       ('bhutan-tour-packages', 'Bhutan', 'suzu-card-bhutan', 'Paro, Thimphu, Punakha')]
SPECIAL_IMG = {'HK': 'https://suzutravels.com/wp-content/uploads/2026/11/hong-kong-victoria-harbour-night-from-the-peak-768x363.webp',
               'CN': 'https://suzutravels.com/wp-content/uploads/2026/11/china-great-wall-mutianyu-768x575.webp'}

def build():
    W = "Hi Suzu Travels, I'm planning a Russia trip. Please share a quote."
    h = [f'<div class="suzu-intl hx hx-country"><style>{CSS}</style>']
    slides = ''.join(f'<div class="hx-slide"><img src="{U(s)}" alt="{A(s)}" width="1600" height="1000" {"fetchpriority=\"high\" loading=\"eager\"" if i == 0 else "loading=\"lazy\""} decoding="async"><span class="hx-cap">{C(s)}</span></div>' for i, s in enumerate(HERO))
    h.append('<section class="hx-hero" aria-label="Russia tour packages from India"><div class="hx-slides">' + slides + '</div><div class="hx-copy">'
             '<p class="hx-lede">Stand on Red Square before the domes of Saint Basil&rsquo;s, walk inside the Kremlin, ride the palace-like Moscow Metro, then take the fast train to Saint Petersburg for the Hermitage, the canals and the fountains of Peterhof. We plan Russia to your dates, budget and pace — summer White Nights or snowy New Year — with central hotels, vegetarian meals noted in advance and an honest, step-by-step guide to the Russian e-visa.</p>'
             '<div class="hx-badges">'
             f'<span class="hx-badge">{svg("globe")}Moscow &amp; Saint Petersburg</span><span class="hx-badge">{svg("doc")}Online e-visa guidance</span>'
             f'<span class="hx-badge">{svg("team")}Families, couples &amp; groups</span><span class="hx-badge">{svg("food")}Vegetarian meals planned</span></div>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Get a Russia Quote {svg("arrow")}</a>'
             f'<a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div></div>'
             '<form class="hx-plan" id="hxPlan" aria-label="Get a costed Russia itinerary on WhatsApp"><h3>Plan my Russia trip</h3>'
             '<p>Tell us the basics — we reply on WhatsApp with a costed, day-by-day plan, usually within 24 hours.</p><div class="hx-f">'
             '<label class="hx-full">Trip<select name="d"><option selected>Moscow + Saint Petersburg (classic)</option><option>Moscow only</option><option>Saint Petersburg only</option><option>Classic + Kazan</option><option>Winter / New Year in Russia</option><option>Not sure yet</option></select></label>'
             '<label>Trip type<select name="s"><option>Family</option><option>Honeymoon / couple</option><option>Friends</option><option>Seniors</option><option>Group</option><option>Corporate / MICE</option></select></label>'
             f'<label>Travel month<select name="m">{G.months()}</select></label>'
             '<label>Adults<select name="a"><option>1</option><option selected>2</option><option>3</option><option>4</option><option>5</option><option>6</option><option>7–10</option><option>11–20</option><option>20+</option></select></label>'
             '<label>Children<select name="k"><option>0</option><option>1</option><option>2</option><option>3</option><option>4+</option></select></label>'
             '<label class="hx-full">Departing from<input name="c" type="text" placeholder="e.g. Delhi, Mumbai, Chandigarh" autocomplete="address-level2"></label></div>'
             f'<button class="hx-btn" type="submit">{WA_SVG}Get my Russia plan on WhatsApp</button><small>Opens WhatsApp with your details filled in. We do not store anything on this page.</small></form></section>')
    h.append('<div class="hx-trust">'
             f'<div>{svg("clock")}<span><b>Quote in ~24 hours</b><span>Costed, day by day</span></span></div>'
             f'<div>{svg("doc")}<span><b>Honest visa guidance</b><span>Official Russian e-visa rules, checked</span></span></div>'
             f'<div>{svg("shield")}<span><b>HP Tourism registered</b><span>Reg. DTO-MND-11-243/2022</span></span></div>'
             f'<div>{svg("chat")}<span><b>One team, start to finish</b><span>Reachable while you travel</span></span></div></div>')
    h.append('<nav class="hx-toc" aria-label="On this page"><a href="#why-russia">Why Russia</a><a href="#russia-in-photos">Photos</a><a href="#how-to-choose">Choose your trip</a><a href="#sample-itinerary">Sample itinerary</a><a href="#when-to-go">When to go</a><a href="#visa-and-entry">Visa</a><a href="#whats-included">What\'s included</a><a href="#russia-faq">FAQ</a></nav>')
    facts = [('Getting there', 'Fly into Moscow; we compare direct and connecting flights from your city'), ('Time difference', 'Moscow is 2 hours 30 minutes behind India'), ('Currency', 'Russian rouble (RUB); plan money in advance — many international cards do not work'),
             ('Best season', 'Late May to early September; December to February for snow'), ('Typical trip', '6 to 8 nights; 9 to 10 with Kazan'), ('Entry', 'Russian e-visa online before travel — up to 30 days&rsquo; stay')]
    h.append('<section id="why-russia" class="hx-sec"><span class="hx-eye">Russia</span><h2>Why Russia is worth the journey for Indian travellers</h2>'
             '<p class="hx-sub">Two great cities make one easy trip: Moscow with Red Square, the Kremlin, the Bolshoi Theatre and its famous metro stations, and Saint Petersburg with the Winter Palace and the Hermitage, canals, cathedrals and the imperial palaces of Peterhof and Pushkin. A high-speed train links the two in around four hours. The visa is an online e-visa — we walk you through the official steps.</p>'
             '<div class="hx-facts">' + ''.join(f'<div class="hx-fact"><b>{a}</b><span>{b}</span></div>' for a, b in facts) + '</div></section>')
    h.append('<section id="russia-in-photos" class="hx-sec"><span class="hx-eye">Real places</span><h2>Russia in photos</h2>'
             '<p class="hx-sub">Komsomolskaya metro station and the Bolshoi Theatre in Moscow, Catherine Palace at Pushkin, the Moyka River in Saint Petersburg, the Trinity Lavra at Sergiev Posad, the Kul Sharif Mosque in the Kazan Kremlin and the Winter Palace from the air. Real photos by Wikimedia Commons photographers, credited below.</p><div class="hx-pg">'
             + ''.join(f'<figure><img src="{U(k)}" alt="{A(k)}" width="800" height="600" loading="lazy" decoding="async"><figcaption>{C(k)}</figcaption></figure>' for k in GAL) + '</div></section>')
    cards = [('First-timers', 'Moscow &amp; Saint Petersburg', 'The classic first trip: Red Square and the Kremlin, the metro and the Bolshoi, then the Hermitage, canals and Peterhof.'),
             ('Winter', 'Snow &amp; New Year', 'December to February brings snow, New Year lights in Moscow and cosy museum days; we plan warm clothing and shorter outdoor stretches.'),
             ('Families', 'Russia with children', 'Easy-paced days, river cruises, the Peterhof fountains in summer, parks and family rooms close to the metro.'),
             ('Add-on', 'Kazan or Sergiev Posad', 'Add two days for Kazan and its Kremlin, or a day trip from Moscow to the monastery town of Sergiev Posad.')]
    stays = [('Moscow — around Red Square', 'Kitay-gorod and Tverskaya put Red Square, the Kremlin and the Bolshoi within walking distance, with metro stations close by.'),
             ('Moscow — Arbat', 'A walking street with cafés and museums, a little quieter, and still close to the centre by metro.'),
             ('Saint Petersburg — Nevsky Prospekt', 'The main avenue: walk to the Winter Palace, the Church of the Savior on Blood and the canal boats.'),
             ('Kazan — near the Kremlin', 'Stay near the Kazan Kremlin and Bauman Street for an easy, walkable add-on.')]
    h.append('<section id="how-to-choose" class="hx-sec"><span class="hx-eye">How to choose</span><h2>Choose the Russia trip that fits you</h2>'
             '<p class="hx-sub">Start from the kind of trip you want — we fine-tune the cities, hotels, trains, tickets and guides to your group.</p><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><span class="hx-tag">{t}</span><h3>{n}</h3><p>{d}</p></div>' for t, n, d in cards) + '</div>'
             '<h3 style="margin-top:30px">Where to stay</h3><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><h3>{n}</h3><p>{d}</p></div>' for n, d in stays) + '</div></section>')
    days = [('Day 1', 'Arrive in Moscow', 'Airport transfer to your hotel. An easy evening walk to Red Square and the lights of Saint Basil&rsquo;s.'),
            ('Day 2', 'Red Square &amp; Kremlin', 'Saint Basil&rsquo;s Cathedral and Red Square, then inside the Kremlin walls for its cathedrals and Armoury.'),
            ('Day 3', 'Metro &amp; river', 'A guided ride through the most beautiful metro stations, Zaryadye Park and a boat trip on the Moskva River.'),
            ('Day 4', 'Sergiev Posad or Bolshoi', 'A day trip to the Trinity Lavra at Sergiev Posad, or a free day in Moscow with an evening at the Bolshoi.'),
            ('Day 5', 'Train to Saint Petersburg', 'High-speed train to Saint Petersburg. Evening walk on Nevsky Prospekt and a canal boat ride.'),
            ('Day 6', 'Hermitage', 'The Winter Palace and the Hermitage collections, Palace Square, Saint Isaac&rsquo;s and the Church of the Savior on Blood.'),
            ('Day 7', 'Peterhof &amp; Pushkin', 'The Grand Cascade and park at Peterhof, then Catherine Palace at Pushkin (Tsarskoye Selo).'),
            ('Day 8', 'Fly home', 'Free morning, then transfer to Pulkovo airport for your flight home.')]
    h.append('<section id="sample-itinerary" class="hx-sec"><span class="hx-eye">Sample plan</span><h2>A sample 8-day Russia itinerary</h2>'
             '<p class="hx-sub">The classic first trip. We rebuild it around you — a shorter Moscow break, more time in Saint Petersburg, a Kazan add-on, or a winter version with New Year in Moscow.</p><div class="hx-itin">'
             + ''.join(f'<div class="hx-day"><i>{a}</i><b>{b}</b><p>{c}</p></div>' for a, b, c in days) + '</div></section>')
    seasons = [('Jun – Aug', '<span class="hx-ok">Best</span>', 'Warm, long days', 'The main season, with the White Nights in Saint Petersburg around midsummer and the Peterhof fountains running; book early.'),
               ('Late May &amp; Sep', '<span class="hx-ok">Best</span>', 'Mild', 'Pleasant for walking both cities, with fewer crowds than midsummer; autumn colours in September.'),
               ('Dec – Feb', '<span class="hx-mid">Snow</span>', 'Cold, snowy', 'Snowy squares and New Year lights in Moscow; very cold, short days — you need proper winter clothing.'),
               ('Oct – Nov', '<span class="hx-mid">Quiet</span>', 'Cool to cold', 'Quieter museums and good value; grey, chilly days and early darkness.'),
               ('Mar – Apr', '<span class="hx-mid">Thaw</span>', 'Cool, slushy', 'Snow melts and days get longer; fine for museums and theatre, less so for parks and palaces outdoors.')]
    h.append('<section id="when-to-go" class="hx-sec"><span class="hx-eye">Best season</span><h2>When to go to Russia</h2>'
             '<p class="hx-sub">Russia is a summer and a winter destination: long, mild days from late May to early September, or snow and festive lights in winter. We check the season, holidays and flight prices against your plan before we quote.</p>'
             '<div class="hx-tw"><table class="hx-t"><thead><tr><th>Months</th><th>Verdict</th><th>Weather</th><th>What it means for your trip</th></tr></thead><tbody>'
             + ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in seasons) + '</tbody></table></div></section>')
    h.append('<section id="visa-and-entry" class="hx-sec"><span class="hx-eye">Visa &amp; entry</span><h2>Russia e-visa for Indian passport holders</h2>'
             '<div class="hx-visa"><div class="hx-vbox"><h3>What the official rules say</h3><ul>'
             '<li><b>A visa is needed.</b> India is on the official list of countries whose nationals can apply for the <b>Russian e-visa</b> — for tourism, guest and business visits and events. No invitation is needed; you fill in the application form online and pay the fee.</li>'
             f'<li><b>Apply only on the official site</b> of the Russian Ministry of Foreign Affairs: <a href="{SRC_EV}" target="_blank" rel="noopener nofollow">evisa.kdmid.ru</a>. The Ministry says the e-visa is issued within <b>4 calendar days</b>, not counting the day you submit; if the application is returned for corrections, the time starts again from resubmission. The fee is <b>not refundable</b> and is paid by a bank card issued outside Russia.</li>'
             '<li><b>Validity and stay:</b> a single-entry e-visa is valid for <b>120 days from issue</b>, with a stay of <b>up to 30 days from entry</b>; you must also leave within the 120 days. Each child needs a separate e-visa application.</li>'
             '<li><b>Approved checkpoints only:</b> enter and leave through the border points on the official list — it includes the Moscow airports (Sheremetyevo, Domodedovo, Vnukovo, Zhukovsky), Saint Petersburg Pulkovo and Kazan. Show the e-visa notification to the airline and at the border.</li>'
             '<li><b>Registration:</b> foreign visitors must be registered at their place of stay within 7 working days; when you stay in a hotel, the hotel does this for you.</li></ul>'
             f'<p class="hx-checked">Checked {CHECKED} · sources: <a href="{SRC_KD}" target="_blank" rel="noopener nofollow">MFA of Russia — e-visa portal</a> · <a href="{SRC_FAQ}" target="_blank" rel="noopener nofollow">e-visa FAQ</a> · <a href="{SRC_CTRY}" target="_blank" rel="noopener nofollow">list of eligible countries</a> · <a href="{SRC_CP}" target="_blank" rel="noopener nofollow">list of approved checkpoints</a></p></div>'
             '<div class="hx-vnote"><p><b>Please note:</b> whether a visa is issued, and admission at the border, is always the decision of the Russian authorities. We help you prepare a correct application, but we never promise an outcome we do not control.</p>'
             '<p>We help you fill in the form with the hotel details from your itinerary, check your flights against the approved checkpoints, and confirm non-refundable bookings only once your e-visa is issued. If you need a stay or purpose the e-visa does not cover, we guide you to a regular visa through a Russian embassy or consulate.</p></div></div></section>')
    inc = [('doc', 'E-visa help', 'Step-by-step help with the official e-visa form, using the hotel details from your day-by-day itinerary.'), ('pin', 'Hotels', 'Named, central hotels in Moscow and Saint Petersburg, plus Kazan if you add it.'),
           ('team', 'Transfers &amp; trains', 'Airport transfers, the high-speed train between Moscow and Saint Petersburg, and station transfers.'), ('globe', 'Tickets &amp; guides', 'Kremlin, Hermitage, Peterhof and Catherine Palace tickets, metro tour and English-speaking guides, as you choose.'),
           ('food', 'Meal plan', 'Breakfast at most hotels; vegetarian and Jain needs noted in advance, with Indian restaurant suggestions.'), ('award', 'Flights optional', 'Land-only, or a full package with international flights from your nearest Indian airport.')]
    h.append('<section id="whats-included" class="hx-sec"><span class="hx-eye">Your package</span><h2>What a Suzu Russia package includes</h2><div class="hx-inc">'
             + ''.join(f'<div>{svg(i)}<span><b>{t}</b><span>{d}</span></span></div>' for i, t, d in inc) + '</div></section>')
    steps = [('chat', 'Tell us the basics', 'Dates, travellers and the kind of trip you want. A WhatsApp message is enough.'),
             ('doc', 'Get a costed itinerary', 'A day-by-day plan with named hotels and a clear per-person price, usually within 24 hours.'),
             ('sliders', 'Adjust until it fits', 'Change the cities, hotels, trains or add-ons. We re-quote as needed.'),
             ('lock', 'Confirm with a token', 'Lock your plan with a small token amount; the balance is paid later, as agreed in writing.')]
    h.append('<section id="how-booking-works" class="hx-sec"><span class="hx-eye">Simple process</span><h2>How booking works</h2><div class="hx-steps">'
             + ''.join(f'<div class="hx-step"><div class="hx-n">{svg(i)}</div><b>{t}</b><p>{d}</p></div>' for i, t, d in steps) + '</div></section>')
    h.append('<section id="russia-faq" class="hx-sec"><span class="hx-eye">FAQ</span><h2>Common questions about a Russia tour</h2><div class="hx-faqs">'
             + ''.join(f'<details class="hx-faq"{" open" if k == 0 else ""}><summary>{html.escape(q)}</summary><div class="hx-ans"><p>{html.escape(a)}</p></div></details>' for k, (q, a) in enumerate(FAQ)) + '</div></section>')
    def _img(img): return SPECIAL_IMG[img] if img in SPECIAL_IMG else f'https://suzutravels.com/wp-content/uploads/2026/10/{img}.webp'
    h.append('<section id="more-destinations" class="hx-sec"><span class="hx-eye">Explore more</span><h2>Explore more destinations</h2>'
             '<p class="hx-sub">Every trip is planned the same way — your dates, your budget, one team from quote to return. <a href="https://suzutravels.com/international-tour-packages/">See all international holidays →</a></p><div class="hx-mini">'
             + ''.join(f'<a class="hx-mc" href="https://suzutravels.com/{p}/"><img src="{_img(img)}" alt="{html.escape(n)} holiday — Suzu Travels" width="640" height="360" loading="lazy" decoding="async"><span><b>{html.escape(n)}</b><em>{html.escape(e)}</em></span></a>' for p, n, img, e in REL) + '</div></section>')
    h.append(f'<div class="hx-final"><img src="{U(FINAL)}" alt="{A(FINAL)}" width="1600" height="900" loading="lazy" decoding="async">'
             '<h2>Plan your Russia trip</h2><p>Send us your dates and group size. We will come back with a costed, day-by-day Russia itinerary you can compare, no obligation.</p>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Request a Russia Quote {svg("arrow")}</a><a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div>'
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
    open('pages/russia-tour-packages.html', 'w').write(o)
    print('pages/russia-tour-packages.html', len(o), len(o.encode()))
