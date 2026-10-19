#!/usr/bin/env python3
"""Turkey country page (.hx design system, shares CSS with gen_hub.py via the Dubai template).
Run from outbound-kit/:  python3 pages/gen_turkey.py <PAGE_ID>  -> pages/turkey-tour-packages.html (one line)
Facts: visa/entry checked 19 Oct 2026 against the Republic of Turkiye MFA and the Turkish Embassy New Delhi (official). No prices.
"""
import json, html, sys, os
sys.path.insert(0, os.getcwd())
import gen_hub as G

PID = int(sys.argv[1]) if len(sys.argv) > 1 else 0
M = G.M
svg, WA_SVG, wa = G.svg, G.WA_SVG, G.wa
CHECKED = '19 October 2026'
SRC_MFA = 'https://www.mfa.gov.tr/visa-information-for-foreigners.en.mfa'
SRC_EMB = 'https://newdelhi-emb.mfa.gov.tr/Mission/ShowAnnouncement/361514'

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
body.page-id-PID .page-header:before{content:"Holidays abroad \00B7  Turkey";display:inline-block;font:800 12px/1 "Plus Jakarta Sans",sans-serif;letter-spacing:.18em;text-transform:uppercase;color:#1a1606;background:#E2C158;padding:8px 13px;border-radius:999px;margin-bottom:16px}
body.page-id-PID .page-header .entry-title{color:#fff!important;font-family:"Sora","Plus Jakarta Sans",sans-serif!important;font-size:clamp(34px,4.2vw,58px)!important;line-height:1.06!important;letter-spacing:-.035em!important;margin:0!important;font-weight:800!important;max-width:15ch;text-shadow:0 2px 24px rgba(0,0,0,.35)}
@media(max-width:1100px){.hx .hx-cards{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-itin{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-visa{grid-template-columns:1fr}.hx .hx-inc,.hx .hx-steps{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:700px){body.page-id-PID .page-header{left:14px;right:14px;padding:26px 18px 0}body.page-id-PID .page-header:before{font-size:10.5px;padding:7px 11px;margin-bottom:12px}body.page-id-PID .page-header .entry-title{font-size:33px!important}.hx .hx-facts{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-pg{grid-template-columns:repeat(2,minmax(0,1fr));grid-auto-rows:150px}.hx .hx-pg figure:first-child{grid-column:span 2;grid-row:span 1}.hx .hx-pg figure:nth-child(4){grid-row:span 1}.hx .hx-pg figure:nth-child(8){display:none}.hx .hx-cards,.hx .hx-itin,.hx .hx-inc,.hx .hx-steps{grid-template-columns:1fr}.hx .hx-mini{grid-template-columns:repeat(2,minmax(0,1fr))}}
.hx .hx-pg p,.hx .hx-cards>p,.hx .hx-itin>p,.hx .hx-inc>p,.hx .hx-facts>p{display:none}
""".replace('PID', str(PID))
CSS = ' '.join(l.strip() for l in (base + EXTRA).strip().splitlines() if l.strip() and not l.strip().startswith('/*'))
HERO = ['turkey-1', 'turkey-2', 'turkey-3', 'turkey-4', 'turkey-5', 'turkey-6']
GAL = ['turkey-12', 'turkey-7', 'turkey-9', 'turkey-8', 'turkey-11', 'turkey-10', 'turkey-3', 'turkey-5']
CC = 'Turkey'

FAQ = [
    ("Do Indians need a visa for Turkey?", "Yes. Indian ordinary passport holders need a visa for Turkey (Türkiye). If you hold a valid Schengen, USA, UK or Ireland visa or residence permit, you may be eligible for a single-entry e-Visa valid for one month, applied for only on the official site evisa.gov.tr — you must carry the original supporting visa or permit. Everyone else applies for a visa through the Turkish Embassy or Consulate process in India. Approval is always the decision of the Turkish authorities."),
    ("How many days are enough for Turkey?", "Seven to eight nights covers the classic circuit — Istanbul, Cappadocia, Pamukkale and Ephesus — at a comfortable pace. With five or six nights we suggest Istanbul and Cappadocia only, so you are not spending the holiday in transfers."),
    ("When is the best time to visit Turkey from India?", "April to June and September to November: mild weather for walking in Istanbul and the ruins, and good conditions in Cappadocia. July and August are hot and busy but fine for the coast. Winter is cold inland and Cappadocia can get snow."),
    ("Is the Cappadocia hot-air balloon ride guaranteed?", "No. Balloon flights depend on the weather on the morning and are cancelled when winds or visibility are not safe. We plan two mornings in Cappadocia where we can, so there is a second chance if the first flight is called off."),
    ("Is vegetarian food easy to find in Turkey?", "Yes, with a little planning. Turkish cuisine has many vegetarian dishes — mezes, lentil soup, vegetable dishes, pide and fresh bread — and Istanbul has Indian restaurants. Jain meals need advance notice, which we arrange with hotels where possible."),
    ("Why are there no prices on this page?", "Turkey costs depend on your dates, hotel category, internal flights and the airfare from India. Instead of a teaser price that changes when you ask, we send a costed, day-by-day quote for your dates — usually within 24 hours."),
]

JS = ("(function(){var f=document.getElementById('hxPlan');if(!f){return;}f.addEventListener('submit',function(e){e.preventDefault();"
      "var d=f.querySelector('[name=d]').value,s=f.querySelector('[name=s]').value,m=f.querySelector('[name=m]').value,a=f.querySelector('[name=a]').value,k=f.querySelector('[name=k]').value,c=f.querySelector('[name=c]').value;"
      "var t='Hi Suzu Travels, please send me a costed Turkey itinerary.\\nTrip: '+d+'\\nTrip type: '+s+'\\nTravel month: '+m+'\\nAdults: '+a+'\\nChildren: '+k;"
      "if(c){t=t+'\\nDeparting from: '+c;}"
      "window.open('https:'+String.fromCharCode(47,47)+'wa.me/917087488961?text='+encodeURIComponent(t),'_blank','noopener');});})();")

REL = [('dubai-tour-packages', 'Dubai', 'suzu-abroad-dubai', 'Burj Khalifa, desert, Abu Dhabi'),
       ('nepal-tour-packages', 'Nepal', 'suzu-card-nepal', 'No visa for Indians'), ('bhutan-tour-packages', 'Bhutan', 'suzu-card-bhutan', 'Paro, Thimphu, Punakha'),
       ('sri-lanka-tour-packages', 'Sri Lanka', 'suzu-card-sri-lanka', 'Beaches & tea country'), ('maldives-tour-packages', 'Maldives', 'suzu-card-maldives', 'Overwater villas'),
       ('thailand-tour-packages', 'Thailand', 'suzu-card-thailand', 'Bangkok, Phuket, Krabi'), ('singapore-tour-packages', 'Singapore', 'suzu-card-singapore', 'City, Sentosa, Universal'),
       ('malaysia-tour-packages', 'Malaysia', 'suzu-card-malaysia', 'KL, Langkawi, Genting'), ('vietnam-tour-packages', 'Vietnam', 'suzu-card-vietnam', 'Hanoi, Ha Long, Hoi An'),
       ('bali-tour-packages', 'Bali', 'suzu-card-bali', 'Ubud, villas, temples')]

def build():
    W = "Hi Suzu Travels, I'm planning a Turkey trip. Please share a quote."
    h = [f'<div class="suzu-intl hx hx-country"><style>{CSS}</style>']
    slides = ''.join(f'<div class="hx-slide"><img src="{U(s)}" alt="{A(s)}" width="1600" height="1000" {"fetchpriority=\"high\" loading=\"eager\"" if i == 0 else "loading=\"lazy\""} decoding="async"><span class="hx-cap">{C(s)}</span></div>' for i, s in enumerate(HERO))
    h.append('<section class="hx-hero" aria-label="Turkey tour packages from India"><div class="hx-slides">' + slides + '</div><div class="hx-copy">'
             '<p class="hx-lede">Hot-air balloons at sunrise over Cappadocia, a ferry across the Bosphorus between Europe and Asia, the Hagia Sophia, the white terraces of Pamukkale and the marble streets of Ephesus — Turkey is one of the most rewarding holidays abroad for Indian travellers. We plan it to your dates, your budget and your pace.</p>'
             '<div class="hx-badges">'
             f'<span class="hx-badge">{svg("globe")}Istanbul, Cappadocia &amp; more</span><span class="hx-badge">{svg("food")}Vegetarian meals arranged</span>'
             f'<span class="hx-badge">{svg("team")}Families, couples &amp; groups</span><span class="hx-badge">{svg("doc")}Honest visa guidance</span></div>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Get a Turkey Quote {svg("arrow")}</a>'
             f'<a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div></div>'
             '<form class="hx-plan" id="hxPlan" aria-label="Get a costed Turkey itinerary on WhatsApp"><h3>Plan my Turkey trip</h3>'
             '<p>Tell us the basics — we reply on WhatsApp with a costed, day-by-day plan, usually within 24 hours.</p><div class="hx-f">'
             '<label class="hx-full">Trip<select name="d"><option>Istanbul only</option><option>Istanbul + Cappadocia</option><option selected>Istanbul + Cappadocia + Pamukkale + Ephesus</option><option>Turkey with the coast (Antalya / Bodrum)</option><option>Turkey combined with another country</option></select></label>'
             '<label>Trip type<select name="s"><option>Family</option><option>Honeymoon / couple</option><option>Friends</option><option>Group</option><option>Corporate / MICE</option></select></label>'
             f'<label>Travel month<select name="m">{G.months()}</select></label>'
             '<label>Adults<select name="a"><option>1</option><option selected>2</option><option>3</option><option>4</option><option>5</option><option>6</option><option>7–10</option><option>11–20</option><option>20+</option></select></label>'
             '<label>Children<select name="k"><option>0</option><option>1</option><option>2</option><option>3</option><option>4+</option></select></label>'
             '<label class="hx-full">Departing from<input name="c" type="text" placeholder="e.g. Delhi, Mumbai, Chandigarh" autocomplete="address-level2"></label></div>'
             f'<button class="hx-btn" type="submit">{WA_SVG}Get my Turkey plan on WhatsApp</button><small>Opens WhatsApp with your details filled in. We do not store anything on this page.</small></form></section>')
    h.append('<div class="hx-trust">'
             f'<div>{svg("clock")}<span><b>Quote in ~24 hours</b><span>Costed, day by day</span></span></div>'
             f'<div>{svg("doc")}<span><b>Honest visa guidance</b><span>Official rules, checked</span></span></div>'
             f'<div>{svg("shield")}<span><b>HP Tourism registered</b><span>Reg. DTO-MND-11-243/2022</span></span></div>'
             f'<div>{svg("chat")}<span><b>One team, start to finish</b><span>On WhatsApp while you travel</span></span></div></div>')
    h.append('<nav class="hx-toc" aria-label="On this page"><a href="#why-turkey">Why Turkey</a><a href="#turkey-in-photos">Photos</a><a href="#how-to-choose">Choose your trip</a><a href="#sample-itinerary">Sample itinerary</a><a href="#when-to-go">When to go</a><a href="#visa-and-entry">Visa &amp; entry</a><a href="#whats-included">What\'s included</a><a href="#turkey-faq">FAQ</a></nav>')
    facts = [('Getting there', 'Non-stop flights from Delhi and Mumbai to Istanbul'), ('Time difference', 'Turkey is 2 hrs 30 min behind IST'), ('Currency', 'Turkish Lira (TRY)'),
             ('Best season', 'April to June, September to November'), ('Typical trip', '7 to 9 nights'), ('Language', 'Turkish; English in hotels and tourist areas')]
    h.append('<section id="why-turkey" class="hx-sec"><span class="hx-eye">Turkey (Türkiye)</span><h2>Why Turkey works so well for Indian travellers</h2>'
             '<p class="hx-sub">Few countries pack so much variety into one trip: Istanbul\'s mosques, palaces and bazaars on two continents, the fairy-chimney valleys and cave hotels of Cappadocia, the travertine pools of Pamukkale and the Roman city of Ephesus — with the Mediterranean and Aegean coast if you want beach days. Domestic flights keep the long distances manageable, and Turkish food has plenty of vegetarian choices.</p>'
             '<div class="hx-facts">' + ''.join(f'<div class="hx-fact"><b>{a}</b><span>{b}</span></div>' for a, b in facts) + '</div></section>')
    h.append('<section id="turkey-in-photos" class="hx-sec"><span class="hx-eye">Real places</span><h2>Turkey in photos</h2>'
             '<p class="hx-sub">Istanbul, Cappadocia, Pamukkale and Ephesus — the places on a classic Suzu Turkey itinerary. Photos by Unsplash photographers, credited below.</p><div class="hx-pg">'
             + ''.join(f'<figure><img src="{U(k)}" alt="{A(k)}" width="800" height="600" loading="lazy" decoding="async"><figcaption>{C(k)}</figcaption></figure>' for k in GAL) + '</div></section>')
    cards = [('Couples', 'Honeymoon', 'A Bosphorus-view stay in Istanbul, a cave hotel in Cappadocia and a sunrise balloon flight (weather permitting). Add a few slow days on the coast if you have the time.'),
             ('First trip to Turkey', 'Classic circuit', 'Istanbul, Cappadocia, Pamukkale and Ephesus in 7–9 nights, with internal flights to cut out the longest drives. The trip most first-time visitors from India choose.'),
             ('Families', 'Family holiday', 'Fewer hotel changes, private transfers, rest built into the day and kid-friendly stops. Istanbul and Cappadocia alone make a relaxed 6-night family trip.'),
             ('Groups', 'Groups &amp; corporate', 'Coaches with guides, group check-ins, conference venues and team dinners. Tell us the group size and we quote accordingly, including B2B for travel agents.')]
    stays = [('Sultanahmet, Istanbul', 'Old Istanbul — walk to the Hagia Sophia, the Blue Mosque, Topkapı Palace and the Grand Bazaar. The easiest base for a first visit.'),
             ('Taksim, Galata &amp; Karaköy', 'The livelier, modern side: cafés, the Galata Tower, İstiklal Avenue and Bosphorus views. Good for couples and friends.'),
             ('Göreme &amp; Uçhisar, Cappadocia', 'Cave and stone hotels among the fairy chimneys, close to the valleys and the balloon launch areas. Book early for terrace rooms.'),
             ('Coast — Antalya, Bodrum or Kuşadası', 'Beach and resort stays to end the trip slowly. Kuşadası is close to Ephesus; Antalya and Bodrum suit longer beach breaks.')]
    h.append('<section id="how-to-choose" class="hx-sec"><span class="hx-eye">How to choose</span><h2>Choose the Turkey trip that fits you</h2>'
             '<p class="hx-sub">Start from the kind of trip you want — we fine-tune the days, hotels and pace to your group.</p><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><span class="hx-tag">{t}</span><h3>{n}</h3><p>{d}</p></div>' for t, n, d in cards) + '</div>'
             '<h3 style="margin-top:30px">Where to stay — it shapes your whole trip</h3><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><h3>{n}</h3><p>{d}</p></div>' for n, d in stays) + '</div></section>')
    days = [('Day 1', 'Arrive in Istanbul', 'Airport pickup and hotel check-in. An easy evening walk and dinner near your hotel.'),
            ('Day 2', 'Old Istanbul', 'The Hagia Sophia (a working mosque — modest dress), the Blue Mosque, Topkapı Palace and the Grand Bazaar with a local guide.'),
            ('Day 3', 'Bosphorus &amp; Galata', 'A Bosphorus cruise between Europe and Asia, the Spice Bazaar, the Galata Tower area and an evening on İstiklal Avenue.'),
            ('Day 4', 'Fly to Cappadocia', 'A short domestic flight to Kayseri or Nevşehir, transfer to your cave hotel and a sunset viewpoint over the valleys.'),
            ('Day 5', 'Balloons &amp; valleys', 'Optional sunrise balloon flight (weather permitting), then the open-air museum area, the valleys and an underground city.'),
            ('Day 6', 'To Pamukkale', 'A long travel day — by road or via a flight connection, whichever suits your group — to Pamukkale.'),
            ('Day 7', 'Pamukkale &amp; Ephesus', 'Walk the white travertine terraces and Hierapolis in the morning, then continue to Selçuk or Kuşadası.'),
            ('Day 8', 'Ephesus &amp; fly home', 'The ancient city of Ephesus with a guide, then a flight home from İzmir via Istanbul.')]
    h.append('<section id="sample-itinerary" class="hx-sec"><span class="hx-eye">Sample plan</span><h2>A sample 8-day Istanbul, Cappadocia, Pamukkale &amp; Ephesus itinerary</h2>'
             '<p class="hx-sub">The classic first trip to Turkey. We rebuild it around you — fewer hotel changes for families, more time in Istanbul for shoppers, a coast extension for a honeymoon.</p><div class="hx-itin">'
             + ''.join(f'<div class="hx-day"><i>{a}</i><b>{b}</b><p>{c}</p></div>' for a, b, c in days) + '</div></section>')
    seasons = [('Apr – Jun', '<span class="hx-ok">Best</span>', 'Spring, mild to warm', 'Comfortable for sightseeing across the country; tulips in Istanbul\'s parks in April. Popular — book Cappadocia hotels early.'),
               ('Jul – Aug', '<span class="hx-mid">Good</span>', 'Hot, busiest months', 'Peak season and school holidays. Best for adding the coast; plan ruins and walking for early morning.'),
               ('Sep – Nov', '<span class="hx-ok">Best</span>', 'Warm, then cool', 'Pleasant days and smaller crowds. Late autumn evenings get chilly in Cappadocia — pack a jacket.'),
               ('Dec – Mar', '<span class="hx-mid">Quiet</span>', 'Cold inland', 'Snow is possible in Cappadocia and balloon flights are cancelled more often by weather. Quieter sites and often better hotel value.')]
    h.append('<section id="when-to-go" class="hx-sec"><span class="hx-eye">Best season</span><h2>When to go to Turkey</h2>'
             '<p class="hx-sub">Spring and autumn suit most Indian travellers. Religious holidays and Ramadan dates move every year and can change opening hours, so we check them against your dates.</p>'
             '<div class="hx-tw"><table class="hx-t"><thead><tr><th>Months</th><th>Verdict</th><th>Weather</th><th>What it means for your trip</th></tr></thead><tbody>'
             + ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in seasons) + '</tbody></table></div></section>')
    h.append('<section id="visa-and-entry" class="hx-sec"><span class="hx-eye">Visa &amp; entry</span><h2>Visa and entry for Indian passport holders</h2>'
             '<div class="hx-visa"><div class="hx-vbox"><h3>What the official rules say</h3><ul>'
             '<li>Indian <b>ordinary passport holders need a visa</b> to enter Turkey (Türkiye).</li>'
             '<li><b>e-Visa — only with a supporting document.</b> Indian citizens who hold a valid <b>Schengen, USA, UK or Ireland visa or residence permit</b> may get a single-entry e-Visa valid for one month, if they meet the conditions. The original supporting visa or permit must be with you when you enter. E-visas of other countries are not accepted as supporting documents.</li>'
             '<li>The e-Visa is applied for <b>only on the official website evisa.gov.tr</b>; the Turkish Embassy says no company in India is authorised to issue or facilitate it. It is valid only for tourism or business travel.</li>'
             '<li>Without such a visa or permit, you apply for a visa through the Turkish Embassy or Consulate process in India — we guide you through the documents and the timeline.</li>'
             '<li>Your passport must be valid at least 60 days beyond your permitted stay; the Ministry advises at least 6 months from arrival.</li></ul>'
             f'<p class="hx-checked">Checked {CHECKED} · sources: <a href="{SRC_MFA}" target="_blank" rel="noopener nofollow">Republic of Türkiye Ministry of Foreign Affairs — Visa information for foreigners</a> · <a href="{SRC_EMB}" target="_blank" rel="noopener nofollow">Turkish Embassy in New Delhi — e-Visa announcement</a></p></div>'
             '<div class="hx-vnote"><p><b>Please note:</b> visa approval is always the decision of the Turkish authorities. We guide you through the documentation and timelines honestly, but we never promise an outcome we do not control.</p>'
             '<p>Apply with enough lead time — embassy appointments get busy before the summer and Diwali holidays.</p></div></div></section>')
    inc = [('doc', 'Visa guidance', 'Document checklist and application support — e-Visa or embassy visa, whichever applies to you.'), ('pin', 'Hotels in the right area', 'Named hotels — Sultanahmet or Galata in Istanbul, a cave hotel in Cappadocia.'),
           ('team', 'Private transfers', 'Airport pickup and drop, and private or shared vehicles with guides for sightseeing.'), ('globe', 'Internal flights &amp; tours', 'Domestic flights where they save a day, guided Istanbul, Cappadocia and Ephesus tours.'),
           ('food', 'Meal plan', 'Breakfast as standard; vegetarian and Jain meals arranged on request where hotels can.'), ('award', 'Flights optional', 'Land-only, or a full package with international flights from your nearest Indian airport.')]
    h.append('<section id="whats-included" class="hx-sec"><span class="hx-eye">Your package</span><h2>What a Suzu Turkey package includes</h2><div class="hx-inc">'
             + ''.join(f'<div>{svg(i)}<span><b>{t}</b><span>{d}</span></span></div>' for i, t, d in inc) + '</div></section>')
    steps = [('chat', 'Tell us the basics', 'Dates, travellers and the kind of Turkey trip you want. A WhatsApp message is enough.'),
             ('doc', 'Get a costed itinerary', 'A day-by-day plan with named hotels and a clear per-person price, usually within 24 hours.'),
             ('sliders', 'Adjust until it fits', 'Add the coast, drop a city, upgrade a cave hotel, change the pace. We re-quote as needed.'),
             ('lock', 'Confirm with a token', 'Lock your rate with a small token amount; the balance is paid later, as agreed in writing.')]
    h.append('<section id="how-booking-works" class="hx-sec"><span class="hx-eye">Simple process</span><h2>How booking works</h2><div class="hx-steps">'
             + ''.join(f'<div class="hx-step"><div class="hx-n">{svg(i)}</div><b>{t}</b><p>{d}</p></div>' for i, t, d in steps) + '</div></section>')
    h.append('<section id="turkey-faq" class="hx-sec"><span class="hx-eye">FAQ</span><h2>Common questions about Turkey</h2><div class="hx-faqs">'
             + ''.join(f'<details class="hx-faq"{" open" if k == 0 else ""}><summary>{html.escape(q)}</summary><div class="hx-ans"><p>{html.escape(a)}</p></div></details>' for k, (q, a) in enumerate(FAQ)) + '</div></section>')
    h.append('<section id="more-destinations" class="hx-sec"><span class="hx-eye">Explore more</span><h2>Explore more destinations</h2>'
             '<p class="hx-sub">Every trip is planned the same way — your dates, your budget, one team from quote to return. <a href="https://suzutravels.com/international-tour-packages/">See all international holidays →</a></p><div class="hx-mini">'
             + ''.join(f'<a class="hx-mc" href="https://suzutravels.com/{p}/"><img src="https://suzutravels.com/wp-content/uploads/2026/10/{img}.webp" alt="{html.escape(n)} holiday — Suzu Travels" width="640" height="360" loading="lazy" decoding="async"><span><b>{html.escape(n)}</b><em>{html.escape(e)}</em></span></a>' for p, n, img, e in REL) + '</div></section>')
    h.append(f'<div class="hx-final"><img src="{U("turkey-6")}" alt="{A("turkey-6")}" width="1600" height="900" loading="lazy" decoding="async">'
             '<h2>Plan your Turkey trip</h2><p>Send us your dates and group size. We will come back with a costed, day-by-day Turkey itinerary you can compare — no obligation.</p>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Request a Turkey Quote {svg("arrow")}</a><a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div>'
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
    open('pages/turkey-tour-packages.html', 'w').write(o)
    print('pages/turkey-tour-packages.html', len(o))
