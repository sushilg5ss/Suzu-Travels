#!/usr/bin/env python3
"""Dubai & UAE country page (.hx design system, shares CSS with gen_hub.py).
Run from outbound-kit/:  python3 pages/gen_dubai.py <PAGE_ID>  -> pages/dubai-tour-packages.html (one line)
Facts: visa/entry checked 18 Oct 2026 against GDRFA Dubai (official). No prices — costed quote within ~24 h.
"""
import json, html, sys, os
sys.path.insert(0, os.getcwd())
import gen_hub as G

PID = int(sys.argv[1]) if len(sys.argv) > 1 else 0
M = G.M
svg, WA_SVG, wa = G.svg, G.WA_SVG, G.wa
CHECKED = '18 October 2026'
SRC_VOA = 'https://gdrfad.gov.ae/en/services/727c91b1-52eb-11ea-0320-0050569629e8'

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
body.page-id-PID .page-header:before{content:"Holidays abroad \00B7  Dubai \0026  UAE";display:inline-block;font:800 12px/1 "Plus Jakarta Sans",sans-serif;letter-spacing:.18em;text-transform:uppercase;color:#1a1606;background:#E2C158;padding:8px 13px;border-radius:999px;margin-bottom:16px}
body.page-id-PID .page-header .entry-title{color:#fff!important;font-family:"Sora","Plus Jakarta Sans",sans-serif!important;font-size:clamp(34px,4.2vw,58px)!important;line-height:1.06!important;letter-spacing:-.035em!important;margin:0!important;font-weight:800!important;max-width:15ch;text-shadow:0 2px 24px rgba(0,0,0,.35)}
@media(max-width:1100px){.hx .hx-cards{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-itin{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-visa{grid-template-columns:1fr}.hx .hx-inc,.hx .hx-steps{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:700px){body.page-id-PID .page-header{left:14px;right:14px;padding:26px 18px 0}body.page-id-PID .page-header:before{font-size:10.5px;padding:7px 11px;margin-bottom:12px}body.page-id-PID .page-header .entry-title{font-size:33px!important}.hx .hx-facts{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-pg{grid-template-columns:repeat(2,minmax(0,1fr));grid-auto-rows:150px}.hx .hx-pg figure:first-child{grid-column:span 2;grid-row:span 1}.hx .hx-pg figure:nth-child(4){grid-row:span 1}.hx .hx-pg figure:nth-child(8){display:none}.hx .hx-cards,.hx .hx-itin,.hx .hx-inc,.hx .hx-steps{grid-template-columns:1fr}.hx .hx-mini{grid-template-columns:repeat(2,minmax(0,1fr))}}
.hx .hx-pg p,.hx .hx-cards>p,.hx .hx-itin>p,.hx .hx-inc>p,.hx .hx-facts>p{display:none}
""".replace('PID', str(PID))
CSS = ' '.join(l.strip() for l in (base + EXTRA).strip().splitlines() if l.strip() and not l.strip().startswith('/*'))

HERO = ['dubai-1', 'dubai-2', 'dubai-3', 'dubai-4', 'dubai-5', 'dubai-7']
GAL = ['dubai-6', 'dubai-9', 'dubai-10', 'dubai-8', 'dubai-5', 'dubai-7', 'dubai-4', 'dubai-2']

FAQ = [
    ("Do Indians need a visa for Dubai?", "Most Indian passport holders need a UAE visit visa issued before they fly, and we guide you through the documents and the application. Indian citizens who hold certain US, UK or EU visas or residence permits may qualify for a visa on arrival instead — we check your exact case against the official UAE rules before you book. Approval is always the decision of the UAE authorities."),
    ("How many days are enough for Dubai?", "Four nights covers Dubai's highlights at a comfortable pace. Five nights lets you add a full day in Abu Dhabi for the Sheikh Zayed Grand Mosque and Yas Island, which we recommend for a first visit."),
    ("What is the best time to visit Dubai from India?", "November to March, when days are warm rather than hot and evenings are pleasant outdoors. June to September is very hot, so plans shift to indoor attractions, mornings and evenings — hotel rates are usually lower then."),
    ("Is Dubai good for families with kids and senior citizens?", "Yes. Distances are short, roads and hotels are excellent, and Indian vegetarian food is easy to find. We pace the days with rest in the afternoon heat and use private transfers so nobody waits around."),
    ("Is vegetarian and Jain food easy in Dubai?", "Very. Dubai has a large Indian community and many pure-vegetarian restaurants, especially around Bur Dubai and Karama. Jain meals need advance notice, which we arrange with hotels and the desert camp."),
    ("Why are there no prices on this page?", "Dubai costs move a lot with dates, school holidays, events and airfare. Instead of a teaser price that changes when you ask, we send a costed, day-by-day quote for your dates — usually within 24 hours."),
]

JS = ("(function(){var f=document.getElementById('hxPlan');if(!f){return;}f.addEventListener('submit',function(e){e.preventDefault();"
      "var d=f.querySelector('[name=d]').value,s=f.querySelector('[name=s]').value,m=f.querySelector('[name=m]').value,a=f.querySelector('[name=a]').value,k=f.querySelector('[name=k]').value,c=f.querySelector('[name=c]').value;"
      "var t='Hi Suzu Travels, please send me a costed Dubai itinerary.\\nTrip: '+d+'\\nTrip type: '+s+'\\nTravel month: '+m+'\\nAdults: '+a+'\\nChildren: '+k;"
      "if(c){t=t+'\\nDeparting from: '+c;}"
      "window.open('https:'+String.fromCharCode(47,47)+'wa.me/917087488961?text='+encodeURIComponent(t),'_blank','noopener');});})();")

REL = [('turkey-tour-packages', 'Turkey', 'suzu-abroad-turkey', 'Istanbul, Cappadocia, Pamukkale'), ('nepal-tour-packages', 'Nepal', 'suzu-card-nepal', 'No visa for Indians'), ('bhutan-tour-packages', 'Bhutan', 'suzu-card-bhutan', 'Paro, Thimphu, Punakha'),
       ('sri-lanka-tour-packages', 'Sri Lanka', 'suzu-card-sri-lanka', 'Beaches & tea country'), ('maldives-tour-packages', 'Maldives', 'suzu-card-maldives', 'Overwater villas'),
       ('thailand-tour-packages', 'Thailand', 'suzu-card-thailand', 'Bangkok, Phuket, Krabi'), ('singapore-tour-packages', 'Singapore', 'suzu-card-singapore', 'City, Sentosa, Universal'),
       ('malaysia-tour-packages', 'Malaysia', 'suzu-card-malaysia', 'KL, Langkawi, Genting'), ('vietnam-tour-packages', 'Vietnam', 'suzu-card-vietnam', 'Hanoi, Ha Long, Hoi An'),
       ('bali-tour-packages', 'Bali', 'suzu-card-bali', 'Ubud, villas, temples')]

def build():
    W = "Hi Suzu Travels, I'm planning a Dubai trip. Please share a quote."
    h = [f'<div class="suzu-intl hx hx-country"><style>{CSS}</style>']
    slides = ''.join(f'<div class="hx-slide"><img src="{U(s)}" alt="{A(s)}" width="1600" height="1000" {"fetchpriority=\"high\" loading=\"eager\"" if i == 0 else "loading=\"lazy\""} decoding="async"><span class="hx-cap">{C(s)}</span></div>' for i, s in enumerate(HERO))
    h.append('<section class="hx-hero" aria-label="Dubai tour packages from India"><div class="hx-slides">' + slides + '</div><div class="hx-copy">'
             '<p class="hx-lede">The Burj Khalifa at sunset, a dune drive and dinner at a desert camp, a dhow cruise along the Marina and a day at Abu Dhabi\'s Sheikh Zayed Grand Mosque — Dubai is the easiest big international holiday from India, a short non-stop flight from most metros. We plan it to your dates, your budget and your pace.</p>'
             '<div class="hx-badges">'
             f'<span class="hx-badge">{svg("clock")}Short non-stop flights</span><span class="hx-badge">{svg("food")}Veg &amp; Jain meals arranged</span>'
             f'<span class="hx-badge">{svg("team")}Families, couples &amp; groups</span><span class="hx-badge">{svg("doc")}Visa guidance</span></div>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Get a Dubai Quote {svg("arrow")}</a>'
             f'<a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div></div>'
             '<form class="hx-plan" id="hxPlan" aria-label="Get a costed Dubai itinerary on WhatsApp"><h3>Plan my Dubai trip</h3>'
             '<p>Tell us the basics — we reply on WhatsApp with a costed, day-by-day plan, usually within 24 hours.</p><div class="hx-f">'
             '<label class="hx-full">Trip<select name="d"><option>Dubai only</option><option selected>Dubai + Abu Dhabi</option><option>Dubai + Abu Dhabi + more UAE</option><option>Dubai combined with another country</option></select></label>'
             '<label>Trip type<select name="s"><option>Family</option><option>Honeymoon / couple</option><option>Friends</option><option>Group</option><option>Corporate / MICE</option></select></label>'
             f'<label>Travel month<select name="m">{G.months()}</select></label>'
             '<label>Adults<select name="a"><option>1</option><option selected>2</option><option>3</option><option>4</option><option>5</option><option>6</option><option>7–10</option><option>11–20</option><option>20+</option></select></label>'
             '<label>Children<select name="k"><option>0</option><option>1</option><option>2</option><option>3</option><option>4+</option></select></label>'
             '<label class="hx-full">Departing from<input name="c" type="text" placeholder="e.g. Delhi, Mumbai, Chandigarh" autocomplete="address-level2"></label></div>'
             f'<button class="hx-btn" type="submit">{WA_SVG}Get my Dubai plan on WhatsApp</button><small>Opens WhatsApp with your details filled in. We do not store anything on this page.</small></form></section>')
    h.append('<div class="hx-trust">'
             f'<div>{svg("clock")}<span><b>Quote in ~24 hours</b><span>Costed, day by day</span></span></div>'
             f'<div>{svg("doc")}<span><b>Honest visa guidance</b><span>Official rules, checked</span></span></div>'
             f'<div>{svg("shield")}<span><b>HP Tourism registered</b><span>Reg. DTO-MND-11-243/2022</span></span></div>'
             f'<div>{svg("chat")}<span><b>One team, start to finish</b><span>On WhatsApp while you travel</span></span></div></div>')
    h.append('<nav class="hx-toc" aria-label="On this page"><a href="#why-dubai">Why Dubai</a><a href="#dubai-in-photos">Photos</a><a href="#how-to-choose">Choose your trip</a><a href="#sample-itinerary">Sample itinerary</a><a href="#when-to-go">When to go</a><a href="#visa-and-entry">Visa &amp; entry</a><a href="#whats-included">What\'s included</a><a href="#dubai-faq">FAQ</a></nav>')
    facts = [('Flight time', 'About 3–4 hrs non-stop from most Indian metros'), ('Time difference', 'UAE is 1 hr 30 min behind IST'), ('Currency', 'UAE Dirham (AED)'),
             ('Best season', 'November to March'), ('Typical trip', '4 to 6 nights'), ('Language', 'Arabic; English everywhere in tourism')]
    h.append('<section id="why-dubai" class="hx-sec"><span class="hx-eye">Dubai &amp; UAE</span><h2>Why Dubai works so well for Indian travellers</h2>'
             '<p class="hx-sub">Dubai packs a lot into a short trip: record-breaking skyscrapers and malls, real desert a short drive from the city, beaches, theme parks and Abu Dhabi\'s landmarks within easy reach. For Indian families it is also one of the most comfortable places to travel abroad — Hindi and English are widely understood, Indian vegetarian food is everywhere, and the flight is shorter than many domestic connections.</p>'
             '<div class="hx-facts">' + ''.join(f'<div class="hx-fact"><b>{a}</b><span>{b}</span></div>' for a, b in facts) + '</div></section>')
    h.append('<section id="dubai-in-photos" class="hx-sec"><span class="hx-eye">Real places</span><h2>Dubai and Abu Dhabi in photos</h2>'
             '<p class="hx-sub">The desert, the Marina and the landmarks you will actually see on a Suzu itinerary. Photos by Unsplash photographers, credited below.</p><div class="hx-pg">'
             + ''.join(f'<figure><img src="{U(k)}" alt="{A(k)}" width="800" height="600" loading="lazy" decoding="async"><figcaption>{C(k)}</figcaption></figure>' for k in GAL) + '</div></section>')
    cards = [('First trip abroad', 'Family holiday', '4–5 nights in a central hotel, the city tour, Burj Khalifa, a desert safari and an Abu Dhabi day. Unhurried mornings and rest in the afternoon heat — works for children and grandparents alike.'),
             ('Couples', 'Honeymoon', 'A Marina or Palm Jumeirah stay, a dhow dinner cruise, sunset at the top of the Burj Khalifa and an evening at a desert camp. We ask hotels for honeymoon touches where they offer them.'),
             ('Winter', 'Shopping &amp; festivals', 'Time it with the Dubai Shopping Festival and Global Village season in the cooler months. Event dates are announced each year, so we confirm them for your travel dates.'),
             ('Groups', 'Groups &amp; corporate', 'Coaches with guides, group check-ins, conference venues, team dinners and desert-camp events. Tell us the group size and we quote accordingly, including B2B for travel agents.')]
    stays = [('Downtown &amp; Business Bay', 'Next to the Burj Khalifa and Dubai Mall. Central for sightseeing and the fountain show; the most convenient base for a first visit.'),
             ('Dubai Marina &amp; JBR', 'Waterfront towers, the beach walk and dhow cruises at the door. Livelier in the evenings and good for couples and friends.'),
             ('Bur Dubai &amp; Deira', 'Old Dubai by the Creek — souks, abra boats and many Indian vegetarian restaurants. Better value, a little further from the new landmarks.'),
             ('Palm Jumeirah', 'Resort hotels with private beaches and pools. Best for a relaxed honeymoon or a family who wants a resort day or two.')]
    h.append('<section id="how-to-choose" class="hx-sec"><span class="hx-eye">How to choose</span><h2>Choose the Dubai trip that fits you</h2>'
             '<p class="hx-sub">Start from the kind of trip you want — we fine-tune the days, hotels and pace to your group.</p><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><span class="hx-tag">{t}</span><h3>{n}</h3><p>{d}</p></div>' for t, n, d in cards) + '</div>'
             '<h3 style="margin-top:30px">Where to stay — it shapes your whole trip</h3><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><h3>{n}</h3><p>{d}</p></div>' for n, d in stays) + '</div></section>')
    days = [('Day 1', 'Arrive in Dubai', 'Airport pickup and hotel check-in. Evening dhow dinner cruise on the Marina or the Creek.'),
            ('Day 2', 'City tour &amp; Burj Khalifa', 'Old Dubai by the Creek, an abra ride and the souks, the Dubai Frame, then At the Top of the Burj Khalifa and the Dubai Mall fountain.'),
            ('Day 3', 'Desert safari', 'A free morning, then the afternoon desert safari: dune drive, camels, sunset and dinner at a desert camp with vegetarian options.'),
            ('Day 4', 'Abu Dhabi day trip', 'Sheikh Zayed Grand Mosque (modest dress), then Yas Island — Ferrari World or Warner Bros. World if you want a theme park — and back to Dubai.'),
            ('Day 5', 'Shopping &amp; departure', 'Time for the malls or the gold and spice souks, then your airport transfer.')]
    h.append('<section id="sample-itinerary" class="hx-sec"><span class="hx-eye">Sample plan</span><h2>A sample 5-day Dubai &amp; Abu Dhabi itinerary</h2>'
             '<p class="hx-sub">The plan most first-time visitors from India enjoy. We rebuild it around your interests — more theme parks for children, more relaxed days for seniors, a resort stay for a honeymoon.</p><div class="hx-itin">'
             + ''.join(f'<div class="hx-day"><i>{a}</i><b>{b}</b><p>{c}</p></div>' for a, b, c in days) + '</div></section>')
    seasons = [('Nov – Mar', '<span class="hx-ok">Best</span>', 'Warm days, pleasant evenings', 'Peak season — desert camps, outdoor dining, Global Village and winter festivals. Book early for Christmas, New Year and Diwali holidays.'),
               ('Apr – May', '<span class="hx-mid">Good</span>', 'Getting hot', 'Still workable with early starts; rates begin to ease.'),
               ('Jun – Sep', '<span class="hx-hot">Very hot</span>', 'Hottest months', 'Indoor attractions, malls and water parks; sightseeing early or late. Often the best hotel value.'),
               ('Oct', '<span class="hx-mid">Good</span>', 'Cooling down', 'Shoulder season — outdoor plans become comfortable again towards the end of the month.')]
    h.append('<section id="when-to-go" class="hx-sec"><span class="hx-eye">Best season</span><h2>When to go to Dubai</h2>'
             '<p class="hx-sub">Weather is the biggest factor. Ramadan dates move every year and can change opening hours, so we check them against your dates.</p>'
             '<div class="hx-tw"><table class="hx-t"><thead><tr><th>Months</th><th>Verdict</th><th>Weather</th><th>What it means for your trip</th></tr></thead><tbody>'
             + ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in seasons) + '</tbody></table></div></section>')
    h.append('<section id="visa-and-entry" class="hx-sec"><span class="hx-eye">Visa &amp; entry</span><h2>Visa and entry for Indian passport holders</h2>'
             '<div class="hx-visa"><div class="hx-vbox"><h3>What applies to most Indian travellers</h3><ul>'
             '<li>Most Indian passport holders need a <b>UAE visit visa issued before they fly</b>. We tell you the documents needed and guide the application through an authorised channel.</li>'
             f'<li><b>Visa on arrival — only for some Indian citizens.</b> GDRFA Dubai lists a 14-day visa on arrival for Indian citizens with an ordinary passport who hold a US permanent resident card (green card) or a UK or EU residence visa, valid for at least 6 months. It can be extended once for a similar period.</li>'
             '<li>Your passport should be valid for at least 6 months.</li>'
             '<li>The UAE has widened visa-on-arrival eligibility in recent years, so we check your exact case against the current official rules before you book.</li></ul>'
             f'<p class="hx-checked">Checked {CHECKED} · source: <a href="{SRC_VOA}" target="_blank" rel="noopener nofollow">GDRFA Dubai — Visa on arrival for citizens of the Republic of India</a></p></div>'
             '<div class="hx-vnote"><p><b>Please note:</b> visa approval is always the decision of the UAE authorities. We guide you through the documentation and timelines honestly, but we never promise an outcome we do not control.</p>'
             '<p>Apply with enough lead time — allow extra time around school holidays and festivals.</p></div></div></section>')
    inc = [('doc', 'Visa guidance', 'Document checklist and application support for your UAE visit visa.'), ('pin', 'Hotels in the right area', 'Named hotels matched to your trip — central, Marina, Old Dubai or resort.'),
           ('team', 'Private transfers', 'Airport pickup and drop, and private or shared vehicles for sightseeing.'), ('globe', 'Sightseeing &amp; tickets', 'City tour, Burj Khalifa, desert safari and Abu Dhabi day — booked in advance.'),
           ('food', 'Meal plan', 'Breakfast as standard; Indian vegetarian and Jain meals arranged on request.'), ('award', 'Flights optional', 'Land-only, or a full package with flights from your nearest Indian airport.')]
    h.append('<section id="whats-included" class="hx-sec"><span class="hx-eye">Your package</span><h2>What a Suzu Dubai package includes</h2><div class="hx-inc">'
             + ''.join(f'<div>{svg(i)}<span><b>{t}</b><span>{d}</span></span></div>' for i, t, d in inc) + '</div></section>')
    steps = [('chat', 'Tell us the basics', 'Dates, travellers and the kind of Dubai trip you want. A WhatsApp message is enough.'),
             ('doc', 'Get a costed itinerary', 'A day-by-day plan with named hotels and a clear per-person price, usually within 24 hours.'),
             ('sliders', 'Adjust until it fits', 'Swap hotels, add Abu Dhabi or a theme park, change the pace. We re-quote as needed.'),
             ('lock', 'Confirm with a token', 'Lock your rate with a small token amount; the balance is paid later, as agreed in writing.')]
    h.append('<section id="how-booking-works" class="hx-sec"><span class="hx-eye">Simple process</span><h2>How booking works</h2><div class="hx-steps">'
             + ''.join(f'<div class="hx-step"><div class="hx-n">{svg(i)}</div><b>{t}</b><p>{d}</p></div>' for i, t, d in steps) + '</div></section>')
    h.append('<section id="dubai-faq" class="hx-sec"><span class="hx-eye">FAQ</span><h2>Common questions about Dubai</h2><div class="hx-faqs">'
             + ''.join(f'<details class="hx-faq"{" open" if k == 0 else ""}><summary>{html.escape(q)}</summary><div class="hx-ans"><p>{html.escape(a)}</p></div></details>' for k, (q, a) in enumerate(FAQ)) + '</div></section>')
    h.append('<section id="more-destinations" class="hx-sec"><span class="hx-eye">Explore more</span><h2>Explore more destinations</h2>'
             '<p class="hx-sub">Every trip is planned the same way — your dates, your budget, one team from quote to return. <a href="https://suzutravels.com/international-tour-packages/">See all international holidays →</a></p><div class="hx-mini">'
             + ''.join(f'<a class="hx-mc" href="https://suzutravels.com/{p}/"><img src="https://suzutravels.com/wp-content/uploads/2026/10/{img}.webp" alt="{n} holiday — Suzu Travels" width="640" height="360" loading="lazy" decoding="async"><span><b>{n}</b><em>{e}</em></span></a>' for p, n, img, e in REL) + '</div></section>')
    h.append(f'<div class="hx-final"><img src="{U("dubai-5")}" alt="{A("dubai-5")}" width="1600" height="900" loading="lazy" decoding="async">'
             '<h2>Plan your Dubai trip</h2><p>Send us your dates and group size. We will come back with a costed, day-by-day Dubai itinerary you can compare — no obligation.</p>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Request a Dubai Quote {svg("arrow")}</a><a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div>'
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
    open('pages/dubai-tour-packages.html', 'w').write(o)
    print('pages/dubai-tour-packages.html', len(o))
