#!/usr/bin/env python3
"""Egypt page — .hx design system; same template as gen_uk.py / gen_mauritius.py.
Run from outbound-kit/:  python3 pages/gen_egypt.py <PAGE_ID>  -> pages/egypt-tour-packages.html (one line)
Facts: Egypt e-Visa Portal (visa2egypt.gov.eg/eVisa/FAQ, Government of Egypt) checked 27 Oct 2026 — India is in the table of
nationalities that "may be issued with an e-Visa upon application"; tourism e-Visa single or multiple entry; passport valid
at least 6 months from arrival date; on arrival: e-Visa printout, travel itinerary, hotel bookings; "Egyptian port
authorities have the right to refuse entry to Egypt for an e-visa holder without any explanation". The portal FAQ gives no
validity/stay/processing time, so the page states none. No prices (visa fee deliberately not shown). 8-day itinerary = 4 cols.
Keyword Planner IN 27 Oct 2026: "egypt tour package from india" 880/mo (focus kw), "egypt trip cost from india" 480/mo,
"cost of egypt tour from india" 480/mo, "egypt packages from india" 390/mo.
"""
import json, html, sys, os
sys.path.insert(0, os.getcwd())
import gen_hub as G

PID = int(sys.argv[1]) if len(sys.argv) > 1 else 0
M = G.M
svg, WA_SVG, wa = G.svg, G.WA_SVG, G.wa
CHECKED = '27 October 2026'
SRC_EV = 'https://visa2egypt.gov.eg/eVisa/FAQ'

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
body.page-id-PID .page-header:before{content:"Holidays abroad \00B7  Egypt";display:inline-block;font:800 12px/1 "Plus Jakarta Sans",sans-serif;letter-spacing:.18em;text-transform:uppercase;color:#1a1606;background:#E2C158;padding:8px 13px;border-radius:999px;margin-bottom:16px}
body.page-id-PID .page-header .entry-title{color:#fff!important;font-family:"Sora","Plus Jakarta Sans",sans-serif!important;font-size:clamp(34px,4.2vw,58px)!important;line-height:1.06!important;letter-spacing:-.035em!important;margin:0!important;font-weight:800!important;max-width:15ch;text-shadow:0 2px 24px rgba(0,0,0,.35)}
@media(max-width:1100px){.hx .hx-cards{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-itin{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-visa{grid-template-columns:1fr}.hx .hx-inc,.hx .hx-steps{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:700px){body.page-id-PID .page-header{left:14px;right:14px;padding:26px 18px 0}body.page-id-PID .page-header:before{font-size:10.5px;padding:7px 11px;margin-bottom:12px}body.page-id-PID .page-header .entry-title{font-size:33px!important}.hx .hx-facts{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-pg{grid-template-columns:repeat(2,minmax(0,1fr));grid-auto-rows:150px}.hx .hx-pg figure:first-child{grid-column:span 2;grid-row:span 1}.hx .hx-pg figure:nth-child(4){grid-row:span 1}.hx .hx-pg figure:nth-child(8){display:none}.hx .hx-cards,.hx .hx-itin,.hx .hx-inc,.hx .hx-steps{grid-template-columns:1fr}.hx .hx-mini{grid-template-columns:repeat(2,minmax(0,1fr))}}
.hx .hx-pg p,.hx .hx-cards>p,.hx .hx-itin>p,.hx .hx-inc>p,.hx .hx-facts>p{display:none}
""".replace('PID', str(PID))
CSS = ' '.join(l.strip() for l in (base + EXTRA).strip().splitlines() if l.strip() and not l.strip().startswith('/*'))
HERO = ['egypt-1', 'egypt-9', 'egypt-6', 'egypt-11', 'egypt-3', 'egypt-2']
GAL = ['egypt-5', 'egypt-7', 'egypt-12', 'egypt-8', 'egypt-4', 'egypt-10', 'egypt-13', 'egypt-2']
FINAL = 'egypt'
CC = 'Egypt'

FAQ = [
    ("Do Indians need a visa for Egypt?", "Yes. Indian nationals need a visa for Egypt. India is on the list of nationalities that can apply for a tourist e-Visa on the Government of Egypt's official e-Visa Portal (visa2egypt.gov.eg), for single or multiple entry. Your passport must be valid for at least 6 months from your arrival date. The decision is always made by the Egyptian authorities, and the portal says port authorities can refuse entry even to an e-Visa holder — we help you prepare a complete, honest application but cannot promise an outcome. We checked these rules on 27 October 2026 and re-check them before every booking."),
    ("What documents do we carry on arrival in Egypt?", "The official e-Visa Portal lists a printout of your e-Visa, your travel itinerary and your hotel bookings (or details of the places you will visit), together with a passport valid for at least 6 months from arrival. We give you a printed day-by-day itinerary with all hotel and cruise details for exactly this reason."),
    ("How many days are enough for Egypt?", "Seven to eight nights covers the classic trip: Cairo and the Pyramids of Giza, a flight to Aswan, Abu Simbel, a three- or four-night Nile cruise to Luxor and the Valley of the Kings. With ten to twelve nights you can add three or four relaxed beach days at Hurghada on the Red Sea. A short Cairo-and-Giza break of four nights also works if you are combining Egypt with another country."),
    ("Which is the best time to visit Egypt from India?", "October to April is the most comfortable time, and December to February is the coolest and busiest season, including Christmas and New Year. From May to September it is very hot in Luxor and Aswan, so sightseeing is planned for early mornings and evenings — the Red Sea coast is still good for a beach holiday. We also check Ramadan and Eid dates, which move every year, against your plan."),
    ("Is a Nile cruise better than staying in hotels?", "For most first-time visitors, yes. A cruise between Aswan and Luxor is your hotel, restaurant and transport in one, and it stops at the temples of Kom Ombo and Edfu on the way. If you prefer more space or fewer fixed timings, we can plan hotels in Aswan and Luxor with a private car instead. We compare both for your dates."),
    ("Is vegetarian and Indian food easy to find in Egypt?", "Yes, with a little planning. Many Egyptian staples are vegetarian — koshari, ful medames, ta'meya (Egyptian falafel), lentil soup and fresh breads and salads — and Indian restaurants can be found in Cairo and the main resort towns. We note vegetarian and Jain needs with your hotels and Nile cruise in advance."),
    ("Why are there no prices on this page?", "Egypt costs depend on your dates, the hotel and cruise category, internal flights to Aswan or Abu Simbel, entry tickets, guides and the airfare from your city. Instead of a teaser price that changes when you ask, we send a costed, day-by-day quote for your dates — usually within 24 hours."),
]

JS = ("(function(){var f=document.getElementById('hxPlan');if(!f){return;}f.addEventListener('submit',function(e){e.preventDefault();"
      "var d=f.querySelector('[name=d]').value,s=f.querySelector('[name=s]').value,m=f.querySelector('[name=m]').value,a=f.querySelector('[name=a]').value,k=f.querySelector('[name=k]').value,c=f.querySelector('[name=c]').value;"
      "var t='Hi Suzu Travels, please send me a costed Egypt itinerary.\\nTrip: '+d+'\\nTrip type: '+s+'\\nTravel month: '+m+'\\nAdults: '+a+'\\nChildren: '+k;"
      "if(c){t=t+'\\nDeparting from: '+c;}"
      "window.open('https:'+String.fromCharCode(47,47)+'wa.me/917087488961?text='+encodeURIComponent(t),'_blank','noopener');});})();")

REL = [('dubai-tour-packages', 'Dubai', 'suzu-abroad-dubai', 'Burj Khalifa, desert, Abu Dhabi'), ('turkey-tour-packages', 'Turkey', 'suzu-abroad-turkey', 'Istanbul, Cappadocia, Pamukkale'),
       ('europe-tour-packages', 'Europe', 'suzu-abroad-europe', 'Paris, Swiss Alps, Italy'), ('switzerland-tour-packages', 'Switzerland', 'suzu-abroad-switzerland', 'Lucerne, Jungfrau, Zermatt'),
       ('uk-tour-packages', 'UK', 'suzu-abroad-uk', 'London, Cotswolds, Scotland'), ('japan-tour-packages', 'Japan', 'suzu-abroad-japan', 'Tokyo, Fuji, Kyoto, Osaka'),
       ('mauritius-tour-packages', 'Mauritius', 'suzu-abroad-mauritius', 'Lagoons, Le Morne, island tours'), ('australia-tour-packages', 'Australia & NZ', 'suzu-abroad-australia', 'Sydney, Melbourne, Queenstown'), ('georgia-tour-packages', 'Georgia', 'suzu-abroad-georgia', 'Tbilisi, Kazbegi, Gudauri'),
       ('azerbaijan-tour-packages', 'Azerbaijan', 'suzu-abroad-azerbaijan', 'Baku, Gabala, Shahdag'),
       ('maldives-tour-packages', 'Maldives', 'suzu-card-maldives', 'Overwater villas'), ('bali-tour-packages', 'Bali', 'suzu-card-bali', 'Ubud, villas, temples'),
       ('thailand-tour-packages', 'Thailand', 'suzu-card-thailand', 'Bangkok, Phuket, Krabi'), ('sri-lanka-tour-packages', 'Sri Lanka', 'suzu-card-sri-lanka', 'Beaches & tea country'),
       ('nepal-tour-packages', 'Nepal', 'suzu-card-nepal', 'No visa for Indians'), ('bhutan-tour-packages', 'Bhutan', 'suzu-card-bhutan', 'Paro, Thimphu, Punakha'),
       ('singapore-tour-packages', 'Singapore', 'suzu-card-singapore', 'City, Sentosa, Universal'), ('malaysia-tour-packages', 'Malaysia', 'suzu-card-malaysia', 'KL, Langkawi, Genting'),
       ('vietnam-tour-packages', 'Vietnam', 'suzu-card-vietnam', 'Hanoi, Ha Long, Hoi An')]

def build():
    W = "Hi Suzu Travels, I'm planning an Egypt trip. Please share a quote."
    h = [f'<div class="suzu-intl hx hx-country"><style>{CSS}</style>']
    slides = ''.join(f'<div class="hx-slide"><img src="{U(s)}" alt="{A(s)}" width="1600" height="1000" {"fetchpriority=\"high\" loading=\"eager\"" if i == 0 else "loading=\"lazy\""} decoding="async"><span class="hx-cap">{C(s)}</span></div>' for i, s in enumerate(HERO))
    h.append('<section class="hx-hero" aria-label="Egypt tour packages from India"><div class="hx-slides">' + slides + '</div><div class="hx-copy">'
             '<p class="hx-lede">The Pyramids of Giza and the Sphinx, the mosques and bazaars of old Cairo, the great temples of Luxor and Abu Simbel, and slow days on a Nile cruise between them — Egypt is one of the world&rsquo;s great history trips, with the Red Sea coast for a beach finish. We plan it to your dates, budget and pace, with good hotels, a licensed guide at every site and honest e-Visa guidance from the start.</p>'
             '<div class="hx-badges">'
             f'<span class="hx-badge">{svg("globe")}Cairo, Nile cruise &amp; Luxor</span><span class="hx-badge">{svg("food")}Vegetarian meals planned</span>'
             f'<span class="hx-badge">{svg("team")}Families, couples &amp; groups</span><span class="hx-badge">{svg("doc")}Official e-Visa rules, checked</span></div>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Get an Egypt Quote {svg("arrow")}</a>'
             f'<a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div></div>'
             '<form class="hx-plan" id="hxPlan" aria-label="Get a costed Egypt itinerary on WhatsApp"><h3>Plan my Egypt trip</h3>'
             '<p>Tell us the basics — we reply on WhatsApp with a costed, day-by-day plan, usually within 24 hours.</p><div class="hx-f">'
             '<label class="hx-full">Trip<select name="d"><option selected>Cairo + Nile cruise + Luxor</option><option>Cairo &amp; Pyramids short break</option><option>Egypt + Red Sea beach (Hurghada)</option><option>Egypt honeymoon</option><option>Egypt family holiday</option><option>Not sure yet</option></select></label>'
             '<label>Trip type<select name="s"><option>Family</option><option>Honeymoon / couple</option><option>Friends</option><option>Seniors</option><option>Group</option><option>Corporate / MICE</option></select></label>'
             f'<label>Travel month<select name="m">{G.months()}</select></label>'
             '<label>Adults<select name="a"><option>1</option><option selected>2</option><option>3</option><option>4</option><option>5</option><option>6</option><option>7–10</option><option>11–20</option><option>20+</option></select></label>'
             '<label>Children<select name="k"><option>0</option><option>1</option><option>2</option><option>3</option><option>4+</option></select></label>'
             '<label class="hx-full">Departing from<input name="c" type="text" placeholder="e.g. Delhi, Mumbai, Chandigarh" autocomplete="address-level2"></label></div>'
             f'<button class="hx-btn" type="submit">{WA_SVG}Get my Egypt plan on WhatsApp</button><small>Opens WhatsApp with your details filled in. We do not store anything on this page.</small></form></section>')
    h.append('<div class="hx-trust">'
             f'<div>{svg("clock")}<span><b>Quote in ~24 hours</b><span>Costed, day by day</span></span></div>'
             f'<div>{svg("doc")}<span><b>Honest visa guidance</b><span>Official e-Visa Portal rules, checked</span></span></div>'
             f'<div>{svg("shield")}<span><b>HP Tourism registered</b><span>Reg. DTO-MND-11-243/2022</span></span></div>'
             f'<div>{svg("chat")}<span><b>One team, start to finish</b><span>On WhatsApp while you travel</span></span></div></div>')
    h.append('<nav class="hx-toc" aria-label="On this page"><a href="#why-egypt">Why Egypt</a><a href="#egypt-in-photos">Photos</a><a href="#how-to-choose">Choose your trip</a><a href="#sample-itinerary">Sample itinerary</a><a href="#when-to-go">When to go</a><a href="#visa-and-entry">Visa</a><a href="#whats-included">What\'s included</a><a href="#egypt-faq">FAQ</a></nav>')
    facts = [('Getting there', 'Fly into Cairo; we compare routes and connections from your city'), ('Time difference', 'India is 3 hr 30 min ahead of Egypt, and 2 hr 30 min ahead when Egypt is on summer time'), ('Currency', 'Egyptian pound (EGP)'),
             ('Best season', 'October to April; December to February is the coolest and busiest'), ('Typical trip', '7 to 10 nights — Cairo, a Nile cruise, Luxor, optional Red Sea'), ('Visa', 'Visa needed; India is on Egypt&rsquo;s official tourist e-Visa list — apply before you travel')]
    h.append('<section id="why-egypt" class="hx-sec"><span class="hx-eye">Egypt</span><h2>Why Egypt works so well for Indian travellers</h2>'
             '<p class="hx-sub">Few places pack so much history into one trip: the Pyramids and Sphinx at Giza, Islamic Cairo and the Khan el-Khalili bazaar, the Grand Egyptian Museum near the pyramids, then the Nile valley — Philae and Abu Simbel near Aswan, Kom Ombo and Edfu on a cruise, and the temples of Karnak and Luxor, the Valley of the Kings and the Temple of Hatshepsut at Luxor. Distances are covered by short internal flights and the cruise itself, licensed Egyptologist guides explain every site, and many trips end with a few easy days on the Red Sea.</p>'
             '<div class="hx-facts">' + ''.join(f'<div class="hx-fact"><b>{a}</b><span>{b}</span></div>' for a, b in facts) + '</div></section>')
    h.append('<section id="egypt-in-photos" class="hx-sec"><span class="hx-eye">Real places</span><h2>Egypt in photos</h2>'
             '<p class="hx-sub">Temple columns at Luxor, the Temple of Hatshepsut, Philae near Aswan, a painted tomb in the Valley of the Kings, the Mosque of Muhammad Ali in Cairo, a felucca on the Nile at Aswan, the Red Sea at Hurghada and the Great Sphinx. Photos by Unsplash photographers, credited below.</p><div class="hx-pg">'
             + ''.join(f'<figure><img src="{U(k)}" alt="{A(k)}" width="800" height="600" loading="lazy" decoding="async"><figcaption>{C(k)}</figcaption></figure>' for k in GAL) + '</div></section>')
    cards = [('Families', 'Egypt with children', 'Pyramids and a camel ride at Giza, mummies and treasures in Cairo&rsquo;s museums, a Nile cruise with a pool on deck, and a beach finish — with fewer early starts and family cabins or rooms.'),
             ('Couples', 'Honeymoon &amp; romance', 'A Nile-view hotel in Cairo, a sunset felucca sail in Aswan, a sunrise balloon flight over Luxor and a few quiet days at a Red Sea resort.'),
             ('Seniors', 'Easy Egypt holiday', 'Short flights instead of long drives, a comfortable cruise as your moving hotel, private transfers, a guide at every site and vegetarian meals arranged.'),
             ('History', 'The full Nile story', 'Giza, Saqqara and Cairo, then Abu Simbel, Philae, Kom Ombo, Edfu, Karnak and the Valley of the Kings — with an Egyptologist guide throughout.')]
    stays = [('Cairo &amp; Giza', 'A hotel near the Nile in Cairo is central for the museums and old city; a stay in Giza puts the pyramids outside your window.'),
             ('Nile cruise', 'Three or four nights between Aswan and Luxor, stopping at Kom Ombo and Edfu — the easiest way to see the temples of the south.'),
             ('Luxor &amp; Aswan hotels', 'Prefer more space? Riverside hotels in Aswan and Luxor with a private car between them replace the cruise.'),
             ('Red Sea coast', 'Hurghada and other Red Sea resorts are for beach days, snorkelling and diving — a relaxed end to a busy sightseeing trip.')]
    h.append('<section id="how-to-choose" class="hx-sec"><span class="hx-eye">How to choose</span><h2>Choose the Egypt trip that fits you</h2>'
             '<p class="hx-sub">Start from the kind of trip you want — we fine-tune the cities, hotels, cruise and guides to your group.</p><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><span class="hx-tag">{t}</span><h3>{n}</h3><p>{d}</p></div>' for t, n, d in cards) + '</div>'
             '<h3 style="margin-top:30px">Where to stay — cruise or hotels</h3><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><h3>{n}</h3><p>{d}</p></div>' for n, d in stays) + '</div></section>')
    days = [('Day 1', 'Arrive in Cairo', 'Airport pickup and transfer to your hotel. An easy evening, or a walk by the Nile.'),
            ('Day 2', 'Pyramids &amp; Sphinx', 'The Pyramids of Giza and the Great Sphinx with your guide, then the Grand Egyptian Museum nearby.'),
            ('Day 3', 'Old Cairo', 'The Citadel and the Mosque of Muhammad Ali, the Sultan Hassan and Al-Rifai mosques, and an evening in the Khan el-Khalili bazaar.'),
            ('Day 4', 'Fly to Aswan', 'A short flight to Aswan. Philae Temple by boat and a sunset felucca sail on the Nile, then board your cruise.'),
            ('Day 5', 'Abu Simbel', 'An early start to the great temples of Ramesses II and Nefertari at Abu Simbel, back to Aswan by afternoon.'),
            ('Day 6', 'Kom Ombo &amp; Edfu', 'Cruise north on the Nile, visiting the riverside temple of Kom Ombo and the Temple of Horus at Edfu.'),
            ('Day 7', 'Luxor West &amp; East Bank', 'Optional sunrise balloon flight, the Valley of the Kings and the Temple of Hatshepsut, then Karnak and Luxor Temple.'),
            ('Day 8', 'Fly home', 'Disembark after breakfast and fly from Luxor via Cairo for your flight home — or continue to the Red Sea.')]
    h.append('<section id="sample-itinerary" class="hx-sec"><span class="hx-eye">Sample plan</span><h2>A sample 8-day Cairo, Nile cruise &amp; Luxor itinerary</h2>'
             '<p class="hx-sub">The classic first trip: Cairo and Giza, then the temples of the south on a Nile cruise. We rebuild it around you — an extra Cairo day, hotels instead of a cruise, or three or four beach days at Hurghada at the end.</p><div class="hx-itin">'
             + ''.join(f'<div class="hx-day"><i>{a}</i><b>{b}</b><p>{c}</p></div>' for a, b, c in days) + '</div></section>')
    seasons = [('Oct – Nov', '<span class="hx-ok">Good</span>', 'Warm days, cooler evenings', 'Comfortable for sightseeing in Cairo, Luxor and Aswan, and the Red Sea is still warm for swimming. Popular with Indian travellers around Diwali — book early.'),
               ('Dec – Feb', '<span class="hx-ok">Best</span>', 'Winter, mild days, cool nights', 'The coolest and most comfortable months for the temples of the south, and the busiest — Christmas and New Year are peak dates. Carry a warm layer for early mornings and evenings.'),
               ('Mar – Apr', '<span class="hx-ok">Good</span>', 'Spring, warming up', 'Pleasant at first and getting hot in the south by April. Spring can bring dusty desert winds on some days, so we keep the plan flexible.'),
               ('May – Sep', '<span class="hx-hot">Very hot</span>', 'Summer', 'Very hot in Luxor and Aswan, so sightseeing is planned for early mornings and evenings. Cairo plus a Red Sea beach stay works well; it is also the quietest season at the big sites.')]
    h.append('<section id="when-to-go" class="hx-sec"><span class="hx-eye">Best season</span><h2>When to go to Egypt</h2>'
             '<p class="hx-sub">Egypt can be visited all year, but the heat in the south decides the plan. We check the season, Ramadan and Eid dates, school holidays and cruise schedules against your plan before we quote.</p>'
             '<div class="hx-tw"><table class="hx-t"><thead><tr><th>Months</th><th>Verdict</th><th>Weather</th><th>What it means for your trip</th></tr></thead><tbody>'
             + ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in seasons) + '</tbody></table></div></section>')
    h.append('<section id="visa-and-entry" class="hx-sec"><span class="hx-eye">Visa &amp; entry</span><h2>Egypt visa for Indian passport holders</h2>'
             '<div class="hx-visa"><div class="hx-vbox"><h3>What the official rules say</h3><ul>'
             '<li>The Government of Egypt&rsquo;s official <b>e-Visa Portal</b> says citizens of a foreign country generally need a visa before entering Egypt, and <b>India is on its list of nationalities that may be issued an e-Visa</b> on application.</li>'
             '<li>The <b>tourist e-Visa</b> is issued for <b>single or multiple entry</b>. You apply and pay online, and once approved a <b>link to download your e-Visa</b> is sent to you.</li>'
             '<li>Your <b>passport must be valid for at least 6 months from your arrival date</b>.</li>'
             '<li>On arrival the portal lists: a <b>printout of your e-Visa</b>, your <b>travel itinerary</b>, and <b>hotel bookings</b> or details of the places you will visit.</li>'
             '<li>The portal also states that <b>Egyptian port authorities have the right to refuse entry to an e-Visa holder</b> without explanation — an e-Visa is permission to travel, not a guarantee of entry.</li>'
             '<li>Apply only on the official portal. Each traveller, including children, needs their own visa. We check the latest rules again for your exact dates before you apply.</li></ul>'
             f'<p class="hx-checked">Checked {CHECKED} · source: <a href="{SRC_EV}" target="_blank" rel="noopener nofollow">Egypt e-Visa Portal (Government of Egypt) — FAQ and eligible nationalities</a></p></div>'
             '<div class="hx-vnote"><p><b>Please note:</b> whether a visa is granted, and whether you are admitted at the border, is always the decision of the Egyptian authorities. We help you prepare a complete, honest application, but we never promise an outcome we do not control.</p>'
             '<p>We share a document checklist that matches your itinerary, give you printed hotel and cruise details for arrival, and confirm non-refundable bookings only after your e-Visa is issued.</p></div></div></section>')
    inc = [('doc', 'Visa guidance', 'A clear e-Visa checklist, a day-by-day itinerary and hotel and cruise details that match your application and arrival documents.'), ('pin', 'Hotels &amp; Nile cruise', 'Named hotels in Cairo, a Nile cruise between Aswan and Luxor (or riverside hotels), and an optional Red Sea resort.'),
           ('team', 'Flights &amp; transfers', 'Airport transfers, internal flights such as Cairo–Aswan and Luxor–Cairo, and a private car for sightseeing.'), ('globe', 'Guides &amp; entry tickets', 'A licensed Egyptologist guide at the sites, and entry tickets for the Pyramids, museums and temples on your plan.'),
           ('food', 'Meal plan', 'Breakfast at hotels and meals on the cruise as per the cruise plan; vegetarian and Jain needs noted in advance.'), ('award', 'Flights optional', 'Land-only, or a full package with international flights from your nearest Indian airport.')]
    h.append('<section id="whats-included" class="hx-sec"><span class="hx-eye">Your package</span><h2>What a Suzu Egypt package includes</h2><div class="hx-inc">'
             + ''.join(f'<div>{svg(i)}<span><b>{t}</b><span>{d}</span></span></div>' for i, t, d in inc) + '</div></section>')
    steps = [('chat', 'Tell us the basics', 'Dates, travellers and the kind of trip you want. A WhatsApp message is enough.'),
             ('doc', 'Get a costed itinerary', 'A day-by-day plan with named hotels and a clear per-person price, usually within 24 hours.'),
             ('sliders', 'Adjust until it fits', 'Change the hotels, the cruise, the flights or the sites. We re-quote as needed.'),
             ('lock', 'Confirm with a token', 'Lock your plan with a small token amount; the balance is paid later, as agreed in writing.')]
    h.append('<section id="how-booking-works" class="hx-sec"><span class="hx-eye">Simple process</span><h2>How booking works</h2><div class="hx-steps">'
             + ''.join(f'<div class="hx-step"><div class="hx-n">{svg(i)}</div><b>{t}</b><p>{d}</p></div>' for i, t, d in steps) + '</div></section>')
    h.append('<section id="egypt-faq" class="hx-sec"><span class="hx-eye">FAQ</span><h2>Common questions about an Egypt tour</h2><div class="hx-faqs">'
             + ''.join(f'<details class="hx-faq"{" open" if k == 0 else ""}><summary>{html.escape(q)}</summary><div class="hx-ans"><p>{html.escape(a)}</p></div></details>' for k, (q, a) in enumerate(FAQ)) + '</div></section>')
    h.append('<section id="more-destinations" class="hx-sec"><span class="hx-eye">Explore more</span><h2>Explore more destinations</h2>'
             '<p class="hx-sub">Every trip is planned the same way — your dates, your budget, one team from quote to return. <a href="https://suzutravels.com/international-tour-packages/">See all international holidays →</a></p><div class="hx-mini">'
             + ''.join(f'<a class="hx-mc" href="https://suzutravels.com/{p}/"><img src="https://suzutravels.com/wp-content/uploads/2026/10/{img}.webp" alt="{html.escape(n)} holiday — Suzu Travels" width="640" height="360" loading="lazy" decoding="async"><span><b>{html.escape(n)}</b><em>{html.escape(e)}</em></span></a>' for p, n, img, e in REL) + '</div></section>')
    h.append(f'<div class="hx-final"><img src="{U(FINAL)}" alt="{A(FINAL)}" width="1600" height="900" loading="lazy" decoding="async">'
             '<h2>Plan your Egypt trip</h2><p>Send us your dates and group size. We will come back with a costed, day-by-day Cairo, Nile and Luxor itinerary you can compare — no obligation.</p>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Request an Egypt Quote {svg("arrow")}</a><a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div>'
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
    open('pages/egypt-tour-packages.html', 'w').write(o)
    print('pages/egypt-tour-packages.html', len(o))
