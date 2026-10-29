#!/usr/bin/env python3
"""Uzbekistan page — .hx design; same template as gen_australia.py.
Run from outbound-kit/:  python3 pages/gen_uzbekistan.py <PAGE_ID> -> pages/uzbekistan-tour-packages.html (one line)
Facts checked 29 Oct 2026: MFA Uzbekistan "Visa to the Republic of Uzbekistan" (gov.uz/en/mfa, latest update 2025-03-06) — Appendix 1 lists "31. Republic of India" among countries whose citizens can obtain an electronic entry visa (e-visa.gov.uz); tourist visa (category T) issued for up to 1 month; passport valid at least 3 months longer than the visa. Embassy of Uzbekistan in New Delhi consular section — India on the electronic tourist visa list; apply on e-visa.gov.uz at least 3 working days before travel; e-visa sent by email; personal interview may be required; passport valid 90 days more than the stay. Embassy notice (14 Jul 2018, e-visa launch): e-visa valid 90 days from issue for a single stay of up to 30 days. No fees or prices shown on the page.
Keyword Planner IN 29 Oct 2026: "uzbekistan tour package" 1,900/mo (peaks 3,600 Sep), "uzbekistan tour package from india" 320/mo (focus kw), "uzbekistan trip cost from india" 320/mo, "tashkent tour packages" 210/mo.
"""
import json, html, sys, os
sys.path.insert(0, os.getcwd())
import gen_hub as G

PID = int(sys.argv[1]) if len(sys.argv) > 1 else 0
M = G.M
svg, WA_SVG, wa = G.svg, G.WA_SVG, G.wa
CHECKED = '29 October 2026'
SRC_MFA = 'https://gov.uz/en/mfa/activity_page/o-zbekiston-respublikasi-vizasi'
SRC_EMB = 'https://www.uzbekembassy.in/consular-section/'
SRC_EV = 'https://e-visa.gov.uz/'
SRC_EMB18 = 'https://www.uzbekembassy.in/?p=21742'

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
body.page-id-PID .page-header:before{content:"Holidays abroad \00B7  Uzbekistan";display:inline-block;font:800 12px/1 "Plus Jakarta Sans",sans-serif;letter-spacing:.18em;text-transform:uppercase;color:#1a1606;background:#E2C158;padding:8px 13px;border-radius:999px;margin-bottom:16px}
body.page-id-PID .page-header .entry-title{color:#fff!important;font-family:"Sora","Plus Jakarta Sans",sans-serif!important;font-size:clamp(34px,4.2vw,58px)!important;line-height:1.06!important;letter-spacing:-.035em!important;margin:0!important;font-weight:800!important;max-width:15ch;text-shadow:0 2px 24px rgba(0,0,0,.35)}
@media(max-width:1100px){.hx .hx-cards{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-itin{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-visa{grid-template-columns:1fr}.hx .hx-inc,.hx .hx-steps{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:700px){body.page-id-PID .page-header{left:14px;right:14px;padding:26px 18px 0}body.page-id-PID .page-header:before{font-size:10.5px;padding:7px 11px;margin-bottom:12px}body.page-id-PID .page-header .entry-title{font-size:33px!important}.hx .hx-facts{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-pg{grid-template-columns:repeat(2,minmax(0,1fr));grid-auto-rows:150px}.hx .hx-pg figure:first-child{grid-column:span 2;grid-row:span 1}.hx .hx-pg figure:nth-child(4){grid-row:span 1}.hx .hx-pg figure:nth-child(8){display:none}.hx .hx-cards,.hx .hx-itin,.hx .hx-inc,.hx .hx-steps{grid-template-columns:1fr}.hx .hx-mini{grid-template-columns:repeat(2,minmax(0,1fr))}}
.hx .hx-pg p,.hx .hx-cards>p,.hx .hx-itin>p,.hx .hx-inc>p,.hx .hx-facts>p{display:none}
""".replace('PID', str(PID))
CSS = ' '.join(l.strip() for l in (base + EXTRA).strip().splitlines() if l.strip() and not l.strip().startswith('/*'))
CSS = CSS + (' body.page-id-PID .page-header .entry-title{max-width:19ch;font-size:clamp(32px,3.6vw,52px)!important}'
              ' @media(max-width:700px){body.page-id-PID .page-header .entry-title{font-size:28px!important}}').replace('PID', str(PID))
HERO = ['uzbekistan-1', 'uzbekistan-2', 'uzbekistan-3', 'uzbekistan-4', 'uzbekistan-5', 'uzbekistan-6']
GAL = ['uzbekistan-7', 'uzbekistan-8', 'uzbekistan-9', 'uzbekistan-10', 'uzbekistan-11', 'uzbekistan-12', 'uzbekistan-13', 'uzbekistan-14']
FINAL = 'uzbekistan-15'

FAQ = [
    ("Do Indians need a visa for Uzbekistan?", "Yes, Indian passport holders need a visa, and India is on the official list of countries whose citizens can get an electronic entry visa through e-visa.gov.uz. The Embassy of Uzbekistan in New Delhi advises applying at least 3 working days before you travel; the e-visa is sent by email, and a personal interview may be asked for. Your passport should be valid for at least 3 months beyond your visa. Whether a visa is issued is always the decision of the Uzbek authorities. We checked these rules on 29 October 2026 and re-check them before every booking."),
    ("How long can we stay in Uzbekistan on an e-visa?", "Uzbekistan's Ministry of Foreign Affairs says the tourist visa is issued for up to one month, and the Embassy in New Delhi describes the e-visa as valid for 90 days from issue for a single stay of up to 30 days. A classic Tashkent, Samarkand, Bukhara and Khiva trip takes 7 to 9 nights, well inside that."),
    ("How many days are enough for Uzbekistan?", "Seven to nine nights covers the classic Silk Road circuit: Tashkent, Samarkand, Bukhara and Khiva. With five or six nights, keep to Tashkent, Samarkand and Bukhara. Add a night or two for a mountain day near Tashkent, or for a slower pace in the old towns."),
    ("Which is the best time to visit Uzbekistan from India?", "April to early June and September to October are the most comfortable months, with pleasant days for walking around the old towns. July and August are very hot, especially in Bukhara and Khiva, so sightseeing is best in the early morning and evening. Winter is cold but quiet, with fewer visitors."),
    ("How do we travel between Tashkent, Samarkand, Bukhara and Khiva?", "Fast trains link Tashkent, Samarkand and Bukhara, which is the easiest way to travel between them. For Khiva we use a train, a road transfer or a domestic flight via Urgench, depending on your dates and pace. We book seats in advance and arrange station and airport transfers."),
    ("Is vegetarian and Indian food available in Uzbekistan?", "Uzbek food is meat-heavy — plov, kebabs and samsa — but fresh bread, salads, fruit, nuts and vegetable dishes are easy to find, and Tashkent has Indian restaurants. We note vegetarian and Jain needs with your hotels and guides in advance and suggest suitable restaurants on touring days."),
    ("Why are there no prices on this page?", "Uzbekistan costs depend on your dates, hotel category, train seats or domestic flights, guides and the airfare from your city. Instead of a teaser price that changes when you ask, we send a costed, day-by-day quote for your dates — usually within 24 hours."),
]

JS = ("(function(){var f=document.getElementById('hxPlan');if(!f){return;}f.addEventListener('submit',function(e){e.preventDefault();"
      "var d=f.querySelector('[name=d]').value,s=f.querySelector('[name=s]').value,m=f.querySelector('[name=m]').value,a=f.querySelector('[name=a]').value,k=f.querySelector('[name=k]').value,c=f.querySelector('[name=c]').value;"
      "var t='Hi Suzu Travels, please send me a costed Uzbekistan itinerary.\\nTrip: '+d+'\\nTrip type: '+s+'\\nTravel month: '+m+'\\nAdults: '+a+'\\nChildren: '+k;"
      "if(c){t=t+'\\nDeparting from: '+c;}"
      "window.open('https:'+String.fromCharCode(47,47)+'wa.me/917087488961?text='+encodeURIComponent(t),'_blank','noopener');});})();")

REL = [('dubai-tour-packages', 'Dubai', 'suzu-abroad-dubai', 'Burj Khalifa, desert, Abu Dhabi'), ('turkey-tour-packages', 'Turkey', 'suzu-abroad-turkey', 'Istanbul, Cappadocia, Pamukkale'),
       ('georgia-tour-packages', 'Georgia', 'suzu-abroad-georgia', 'Tbilisi, Kazbegi, Gudauri'), ('azerbaijan-tour-packages', 'Azerbaijan', 'suzu-abroad-azerbaijan', 'Baku, Gabala, Shahdag'),
       ('egypt-tour-packages', 'Egypt', 'suzu-abroad-egypt', 'Cairo, Nile cruise, Luxor'), ('europe-tour-packages', 'Europe', 'suzu-abroad-europe', 'Paris, Swiss Alps, Italy'),
       ('switzerland-tour-packages', 'Switzerland', 'suzu-abroad-switzerland', 'Lucerne, Jungfrau, Zermatt'), ('uk-tour-packages', 'UK', 'suzu-abroad-uk', 'London, Cotswolds, Scotland'),
       ('japan-tour-packages', 'Japan', 'suzu-abroad-japan', 'Tokyo, Fuji, Kyoto, Osaka'), ('australia-tour-packages', 'Australia & NZ', 'suzu-abroad-australia', 'Sydney, Melbourne, Queenstown'),
       ('mauritius-tour-packages', 'Mauritius', 'suzu-abroad-mauritius', 'Lagoons, Le Morne, island tours'), ('maldives-tour-packages', 'Maldives', 'suzu-card-maldives', 'Overwater villas'),
       ('bali-tour-packages', 'Bali', 'suzu-card-bali', 'Ubud, villas, temples'), ('thailand-tour-packages', 'Thailand', 'suzu-card-thailand', 'Bangkok, Phuket, Krabi'),
       ('singapore-tour-packages', 'Singapore', 'suzu-card-singapore', 'City, Sentosa, Universal'), ('malaysia-tour-packages', 'Malaysia', 'suzu-card-malaysia', 'KL, Langkawi, Genting'),
       ('vietnam-tour-packages', 'Vietnam', 'suzu-card-vietnam', 'Hanoi, Ha Long, Hoi An'), ('sri-lanka-tour-packages', 'Sri Lanka', 'suzu-card-sri-lanka', 'Beaches & tea country'),
       ('nepal-tour-packages', 'Nepal', 'suzu-card-nepal', 'No visa for Indians'), ('bhutan-tour-packages', 'Bhutan', 'suzu-card-bhutan', 'Paro, Thimphu, Punakha')]

def build():
    W = "Hi Suzu Travels, I'm planning an Uzbekistan trip. Please share a quote."
    h = [f'<div class="suzu-intl hx hx-country"><style>{CSS}</style>']
    slides = ''.join(f'<div class="hx-slide"><img src="{U(s)}" alt="{A(s)}" width="1600" height="1000" {"fetchpriority=\"high\" loading=\"eager\"" if i == 0 else "loading=\"lazy\""} decoding="async"><span class="hx-cap">{C(s)}</span></div>' for i, s in enumerate(HERO))
    h.append('<section class="hx-hero" aria-label="Uzbekistan tour packages from India"><div class="hx-slides">' + slides + '</div><div class="hx-copy">'
             '<p class="hx-lede">The blue domes of Registan in Samarkand, the minarets and trading domes of Bukhara, the walled old town of Khiva and the wide avenues of Tashkent — Uzbekistan is the heart of the old Silk Road, and one of the most rewarding short-haul holidays from India. We plan it to your dates, budget and pace, with good hotels, fast trains between the cities and honest visa guidance from the start.</p>'
             '<div class="hx-badges">'
             f'<span class="hx-badge">{svg("globe")}Tashkent, Samarkand, Bukhara &amp; Khiva</span><span class="hx-badge">{svg("food")}Vegetarian meals planned</span>'
             f'<span class="hx-badge">{svg("team")}Families, couples &amp; groups</span><span class="hx-badge">{svg("doc")}Official e-visa rules, checked</span></div>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Get an Uzbekistan Quote {svg("arrow")}</a>'
             f'<a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div></div>'
             '<form class="hx-plan" id="hxPlan" aria-label="Get a costed Uzbekistan itinerary on WhatsApp"><h3>Plan my Uzbekistan trip</h3>'
             '<p>Tell us the basics — we reply on WhatsApp with a costed, day-by-day plan, usually within 24 hours.</p><div class="hx-f">'
             '<label class="hx-full">Trip<select name="d"><option selected>Tashkent + Samarkand + Bukhara + Khiva</option><option>Tashkent + Samarkand + Bukhara</option><option>Tashkent + Samarkand (short trip)</option><option>Uzbekistan + Kazakhstan / Kyrgyzstan</option><option>Uzbekistan honeymoon</option><option>Uzbekistan family holiday</option><option>Not sure yet</option></select></label>'
             '<label>Trip type<select name="s"><option>Family</option><option>Honeymoon / couple</option><option>Friends</option><option>Seniors</option><option>Group</option><option>Corporate / MICE</option></select></label>'
             f'<label>Travel month<select name="m">{G.months()}</select></label>'
             '<label>Adults<select name="a"><option>1</option><option selected>2</option><option>3</option><option>4</option><option>5</option><option>6</option><option>7–10</option><option>11–20</option><option>20+</option></select></label>'
             '<label>Children<select name="k"><option>0</option><option>1</option><option>2</option><option>3</option><option>4+</option></select></label>'
             '<label class="hx-full">Departing from<input name="c" type="text" placeholder="e.g. Delhi, Mumbai, Chandigarh" autocomplete="address-level2"></label></div>'
             f'<button class="hx-btn" type="submit">{WA_SVG}Get my Uzbekistan plan on WhatsApp</button><small>Opens WhatsApp with your details filled in. We do not store anything on this page.</small></form></section>')
    h.append('<div class="hx-trust">'
             f'<div>{svg("clock")}<span><b>Quote in ~24 hours</b><span>Costed, day by day</span></span></div>'
             f'<div>{svg("doc")}<span><b>Honest visa guidance</b><span>Official Uzbek e-visa rules, checked</span></span></div>'
             f'<div>{svg("shield")}<span><b>HP Tourism registered</b><span>Reg. DTO-MND-11-243/2022</span></span></div>'
             f'<div>{svg("chat")}<span><b>One team, start to finish</b><span>On WhatsApp while you travel</span></span></div></div>')
    h.append('<nav class="hx-toc" aria-label="On this page"><a href="#why-uzbekistan">Why Uzbekistan</a><a href="#uzbekistan-in-photos">Photos</a><a href="#how-to-choose">Choose your trip</a><a href="#sample-itinerary">Sample itinerary</a><a href="#when-to-go">When to go</a><a href="#visa-and-entry">Visa</a><a href="#whats-included">What\'s included</a><a href="#uzbekistan-faq">FAQ</a></nav>')
    facts = [('Getting there', 'Fly into Tashkent; we compare routes and connections from your city'), ('Time difference', 'Uzbekistan is 30 minutes behind India'), ('Currency', 'Uzbekistani som (UZS)'),
             ('Best season', 'April to early June and September to October'), ('Typical trip', '7 to 9 nights for Tashkent, Samarkand, Bukhara &amp; Khiva'), ('Visa', 'Visa needed; Indian passports can apply for an e-visa online')]
    h.append('<section id="why-uzbekistan" class="hx-sec"><span class="hx-eye">Uzbekistan</span><h2>Why Uzbekistan works so well for Indian travellers</h2>'
             '<p class="hx-sub">Uzbekistan packs some of the finest Islamic architecture in the world into one compact trip: the madrasas of Registan and the tiled lanes of Samarkand, the Kalyan Minaret and old trading domes of Bukhara, and Khiva&rsquo;s walled inner town, all linked by trains and short transfers. The e-visa is applied for online, the cities are walkable, and the old Silk Road history feels close to home for Indian travellers.</p>'
             '<div class="hx-facts">' + ''.join(f'<div class="hx-fact"><b>{a}</b><span>{b}</span></div>' for a, b in facts) + '</div></section>')
    h.append('<section id="uzbekistan-in-photos" class="hx-sec"><span class="hx-eye">Real places</span><h2>Uzbekistan in photos</h2>'
             '<p class="hx-sub">The Tilya-Kori Madrasah and blue tilework in Samarkand, the old city of Bukhara, Khiva at dusk and its old town bazaar, a madrasa in Tashkent, and Registan Square by day and at dusk. Photos by Unsplash photographers, credited below.</p><div class="hx-pg">'
             + ''.join(f'<figure><img src="{U(k)}" alt="{A(k)}" width="800" height="600" loading="lazy" decoding="async"><figcaption>{C(k)}</figcaption></figure>' for k in GAL) + '</div></section>')
    cards = [('Families', 'Uzbekistan with children', 'Fast trains instead of long drives, walkable old towns, a visit to a local craft workshop, and family rooms in well-located hotels.'),
             ('Couples', 'Honeymoon &amp; romance', 'Registan lit up at night, boutique hotels inside the old towns of Bukhara and Khiva, and slow evenings by the Lyabi-Hauz pool.'),
             ('Seniors', 'Easy Silk Road holiday', 'A relaxed pace with a private guide and car, hotels close to the sights, business-class train seats where available and vegetarian meals arranged.'),
             ('History &amp; culture', 'Silk Road in depth', 'Samarkand&rsquo;s Shah-i-Zinda and Gur-e-Amir, Bukhara&rsquo;s madrasas and caravanserais, Khiva&rsquo;s Itchan Kala, and crafts such as silk carpets and suzani embroidery.')]
    stays = [('Tashkent', 'A central hotel near Amir Timur Square or the metro keeps the city sights and the railway station easy to reach.'),
             ('Samarkand', 'A hotel within walking distance of Registan lets you see the square at sunset and again when it is lit up at night.'),
             ('Bukhara', 'A boutique hotel in the old town, near Lyabi-Hauz, puts the trading domes and the Kalyan Minaret a short walk away.'),
             ('Khiva', 'A hotel just inside or outside the Itchan Kala walls makes early-morning and sunset walks easy.')]
    h.append('<section id="how-to-choose" class="hx-sec"><span class="hx-eye">How to choose</span><h2>Choose the Uzbekistan trip that fits you</h2>'
             '<p class="hx-sub">Start from the kind of trip you want — we fine-tune the cities, hotels, trains and guides to your group.</p><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><span class="hx-tag">{t}</span><h3>{n}</h3><p>{d}</p></div>' for t, n, d in cards) + '</div>'
             '<h3 style="margin-top:30px">Where to stay</h3><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><h3>{n}</h3><p>{d}</p></div>' for n, d in stays) + '</div></section>')
    days = [('Day 1', 'Arrive in Tashkent', 'Airport pickup and transfer to your hotel. An easy evening around Amir Timur Square.'),
            ('Day 2', 'Tashkent city', 'The Hazrati Imam complex, Chorsu Bazaar and a ride on the Tashkent metro to see its decorated stations.'),
            ('Day 3', 'Fast train to Samarkand', 'Train to Samarkand, then the Gur-e-Amir mausoleum and Registan Square at sunset.'),
            ('Day 4', 'Samarkand', 'Registan&rsquo;s three madrasas by day, the Shah-i-Zinda necropolis, Bibi-Khanym Mosque and Siyob Bazaar.'),
            ('Day 5', 'Train to Bukhara', 'Train to Bukhara and an evening walk to Lyabi-Hauz in the old town.'),
            ('Day 6', 'Bukhara', 'The Ark fortress, the Kalyan Minaret and Po-i-Kalyan, the old trading domes and a madrasa visit.'),
            ('Day 7', 'On to Khiva', 'Train or road transfer to Khiva, then sunset over the Itchan Kala walls.'),
            ('Day 8', 'Khiva — fly home', 'A morning in Itchan Kala, then a flight from nearby Urgench to Tashkent for your flight home — or one more night to slow down.')]
    h.append('<section id="sample-itinerary" class="hx-sec"><span class="hx-eye">Sample plan</span><h2>A sample 8-day Tashkent, Samarkand, Bukhara &amp; Khiva itinerary</h2>'
             '<p class="hx-sub">The classic Silk Road circuit. We rebuild it around you — skip Khiva for a shorter trip, add a mountain day near Tashkent, or slow down with extra nights in Samarkand and Bukhara.</p><div class="hx-itin">'
             + ''.join(f'<div class="hx-day"><i>{a}</i><b>{b}</b><p>{c}</p></div>' for a, b, c in days) + '</div></section>')
    seasons = [('Apr – early Jun', '<span class="hx-ok">Best</span>', 'Spring, warm days', 'Pleasant for walking around Samarkand, Bukhara and Khiva, with green gardens and long days. A popular window — book hotels early.'),
               ('Jun – Aug', '<span class="hx-hot">Hot</span>', 'Summer, very hot', 'Very hot in the day, especially in Bukhara and Khiva. Sightseeing works best early in the morning and in the evening; summer school holidays from India also fall here.'),
               ('Sep – Oct', '<span class="hx-ok">Best</span>', 'Autumn, warm to mild', 'Comfortable days, harvest season and markets full of fruit — a favourite window for Indian travellers around Dussehra and Diwali.'),
               ('Nov – Mar', '<span class="hx-mid">Quiet</span>', 'Winter, cold', 'Cold, with fewer visitors and quieter monuments. Good for travellers who do not mind the cold and want the sights to themselves.')]
    h.append('<section id="when-to-go" class="hx-sec"><span class="hx-eye">Best season</span><h2>When to go to Uzbekistan</h2>'
             '<p class="hx-sub">Uzbekistan has hot summers and cold winters, so spring and autumn are the sweet spots. We check the season, festival dates and flight prices against your plan before we quote.</p>'
             '<div class="hx-tw"><table class="hx-t"><thead><tr><th>Months</th><th>Verdict</th><th>Weather</th><th>What it means for your trip</th></tr></thead><tbody>'
             + ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in seasons) + '</tbody></table></div></section>')
    h.append('<section id="visa-and-entry" class="hx-sec"><span class="hx-eye">Visa &amp; entry</span><h2>Uzbekistan visa for Indian passport holders</h2>'
             '<div class="hx-visa"><div class="hx-vbox"><h3>What the official rules say</h3><ul>'
             '<li>Indian passport holders <b>need a visa</b> for Uzbekistan. India is on the Ministry of Foreign Affairs&rsquo; <b>list of countries whose citizens can obtain an electronic entry visa</b> through <b>e-visa.gov.uz</b>.</li>'
             '<li>The Ministry says the <b>tourist visa is issued for up to one month</b>. The Embassy of Uzbekistan in New Delhi describes the e-visa as <b>valid for 90 days from issue, for a single stay of up to 30 days</b>.</li>'
             '<li>The Embassy advises applying <b>at least 3 working days before your planned travel</b>. You fill in the online form and upload a photo and your passport page; the e-visa is <b>sent to you by email</b>, and a <b>personal interview may be requested</b>.</li>'
             '<li>Your <b>passport should be valid for at least 3 months (90 days) beyond your visa and your stay</b>, with a blank page.</li></ul>'
             f'<p class="hx-checked">Checked {CHECKED} · sources: <a href="{SRC_MFA}" target="_blank" rel="noopener nofollow">Ministry of Foreign Affairs of Uzbekistan — Visa to the Republic of Uzbekistan</a> · <a href="{SRC_EMB}" target="_blank" rel="noopener nofollow">Embassy of Uzbekistan in India — Consular section</a> · <a href="{SRC_EMB18}" target="_blank" rel="noopener nofollow">Embassy notice on the e-visa system</a> · <a href="{SRC_EV}" target="_blank" rel="noopener nofollow">e-visa.gov.uz</a></p></div>'
             '<div class="hx-vnote"><p><b>Please note:</b> whether a visa is issued, and whether you are admitted at the border, is always the decision of the authorities of the Republic of Uzbekistan. We help you prepare a complete, honest application, but we never promise an outcome we do not control.</p>'
             '<p>We share a document checklist that matches your itinerary, give you a day-by-day plan and hotel details for the application, and confirm non-refundable bookings only after your e-visa is issued.</p></div></div></section>')
    inc = [('doc', 'Visa guidance', 'A clear checklist for the Uzbekistan e-visa, with an itinerary and hotel details that match your application.'), ('pin', 'Hotels', 'Named hotels in Tashkent, Samarkand, Bukhara and Khiva — boutique old-town stays where they suit you.'),
           ('team', 'Trains &amp; transfers', 'Airport and station transfers, fast-train seats between the cities, and a road transfer or domestic flight for Khiva.'), ('globe', 'Guides &amp; tickets', 'English-speaking local guides in each city and monument entry tickets as chosen.'),
           ('food', 'Meal plan', 'Breakfast at most hotels; vegetarian and Jain needs noted in advance, with restaurant suggestions on touring days.'), ('award', 'Flights optional', 'Land-only, or a full package with international flights from your nearest Indian airport.')]
    h.append('<section id="whats-included" class="hx-sec"><span class="hx-eye">Your package</span><h2>What a Suzu Uzbekistan package includes</h2><div class="hx-inc">'
             + ''.join(f'<div>{svg(i)}<span><b>{t}</b><span>{d}</span></span></div>' for i, t, d in inc) + '</div></section>')
    steps = [('chat', 'Tell us the basics', 'Dates, travellers and the kind of trip you want. A WhatsApp message is enough.'),
             ('doc', 'Get a costed itinerary', 'A day-by-day plan with named hotels and a clear per-person price, usually within 24 hours.'),
             ('sliders', 'Adjust until it fits', 'Change the cities, hotels, trains or guides. We re-quote as needed.'),
             ('lock', 'Confirm with a token', 'Lock your plan with a small token amount; the balance is paid later, as agreed in writing.')]
    h.append('<section id="how-booking-works" class="hx-sec"><span class="hx-eye">Simple process</span><h2>How booking works</h2><div class="hx-steps">'
             + ''.join(f'<div class="hx-step"><div class="hx-n">{svg(i)}</div><b>{t}</b><p>{d}</p></div>' for i, t, d in steps) + '</div></section>')
    h.append('<section id="uzbekistan-faq" class="hx-sec"><span class="hx-eye">FAQ</span><h2>Common questions about an Uzbekistan tour</h2><div class="hx-faqs">'
             + ''.join(f'<details class="hx-faq"{" open" if k == 0 else ""}><summary>{html.escape(q)}</summary><div class="hx-ans"><p>{html.escape(a)}</p></div></details>' for k, (q, a) in enumerate(FAQ)) + '</div></section>')
    h.append('<section id="more-destinations" class="hx-sec"><span class="hx-eye">Explore more</span><h2>Explore more destinations</h2>'
             '<p class="hx-sub">Every trip is planned the same way — your dates, your budget, one team from quote to return. <a href="https://suzutravels.com/international-tour-packages/">See all international holidays →</a></p><div class="hx-mini">'
             + ''.join(f'<a class="hx-mc" href="https://suzutravels.com/{p}/"><img src="https://suzutravels.com/wp-content/uploads/2026/10/{img}.webp" alt="{html.escape(n)} holiday — Suzu Travels" width="640" height="360" loading="lazy" decoding="async"><span><b>{html.escape(n)}</b><em>{html.escape(e)}</em></span></a>' for p, n, img, e in REL) + '</div></section>')
    h.append(f'<div class="hx-final"><img src="{U(FINAL)}" alt="{A(FINAL)}" width="1600" height="900" loading="lazy" decoding="async">'
             '<h2>Plan your Uzbekistan trip</h2><p>Send us your dates and group size. We will come back with a costed, day-by-day Silk Road itinerary you can compare, no obligation.</p>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Request an Uzbekistan Quote {svg("arrow")}</a><a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div>'
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
    open('pages/uzbekistan-tour-packages.html', 'w').write(o)
    print('pages/uzbekistan-tour-packages.html', len(o))
