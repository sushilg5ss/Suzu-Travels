#!/usr/bin/env python3
"""Hong Kong & Macau page — .hx design; same template as gen_armenia.py.
Run from outbound-kit/:  python3 pages/gen_hongkong.py <PAGE_ID> -> pages/hong-kong-tour-packages.html (one line)
Facts (official pages read 13 Nov 2026):
- Hong Kong Immigration Department, "Pre-arrival Registration for Indian Nationals": Indian nationals must apply for and
  successfully complete pre-arrival registration (PAR) online before visiting/transiting visa-free (not needed for direct
  air transit without leaving the transit area). Free; passport valid >= 6 months; stay up to 14 days. Result instant;
  notification slip printed on blank A4 white paper and signed; carried with the same passport before boarding and on
  arrival. Valid 6 months, multiple visits of up to 14 days each. Slip is not a guarantee of entry. If unsuccessful or
  stay > 14 days: visit visa from the Immigration Department (normally four weeks).
- Macao SAR Government Portal PS-1474b "Immigration Clearance of Non-residents of Macao": India is on the list of
  nationals exempted (written instruction of the Chief Executive); limit of stay for holders of a valid passport: max 30 days.
Keyword Planner IN 13 Nov 2026: "hong kong tour package" 2,900/mo (focus kw), "hong kong package" 880/mo,
"hong kong macau tour package" 880/mo, "hong kong trip cost from india" 390/mo, "hong kong tour package from india" 260/mo,
"hong kong disneyland package from india" 170/mo, "macau tour package from india" 70/mo.
Photos: Wikimedia Commons (CC0 / CC BY / CC BY-SA / public domain; file pages checked 13 Nov 2026), WP IDs 21710-21726.
Climate/season wording is general guidance (no figures); no prices.
"""

import json, html, sys, os
sys.path.insert(0, os.getcwd())
import gen_hub as G

PID = int(sys.argv[1]) if len(sys.argv) > 1 else 0
M = G.M
svg, WA_SVG, wa = G.svg, G.WA_SVG, G.wa
CHECKED = '13 November 2026'
SRC_HK = 'https://www.immd.gov.hk/eng/services/visas/pre-arrival_registration_for_indian_nationals.html'
SRC_MO = 'https://www.gov.mo/en/services/ps-1474/ps-1474b/'

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
body.page-id-PID .page-header:before{content:"Holidays abroad \00B7  Hong Kong \0026  Macau";display:inline-block;font:800 12px/1 "Plus Jakarta Sans",sans-serif;letter-spacing:.18em;text-transform:uppercase;color:#1a1606;background:#E2C158;padding:8px 13px;border-radius:999px;margin-bottom:16px}
body.page-id-PID .page-header .entry-title{color:#fff!important;font-family:"Sora","Plus Jakarta Sans",sans-serif!important;font-size:clamp(34px,4.2vw,58px)!important;line-height:1.06!important;letter-spacing:-.035em!important;margin:0!important;font-weight:800!important;max-width:15ch;text-shadow:0 2px 24px rgba(0,0,0,.35)}
@media(max-width:1100px){.hx .hx-cards{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-itin{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-visa{grid-template-columns:1fr}.hx .hx-inc,.hx .hx-steps{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:700px){body.page-id-PID .page-header{left:14px;right:14px;padding:26px 18px 0}body.page-id-PID .page-header:before{font-size:10.5px;padding:7px 11px;margin-bottom:12px}body.page-id-PID .page-header .entry-title{font-size:33px!important}.hx .hx-facts{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-pg{grid-template-columns:repeat(2,minmax(0,1fr));grid-auto-rows:150px}.hx .hx-pg figure:first-child{grid-column:span 2;grid-row:span 1}.hx .hx-pg figure:nth-child(4){grid-row:span 1}.hx .hx-pg figure:nth-child(8){display:none}.hx .hx-cards,.hx .hx-itin,.hx .hx-inc,.hx .hx-steps{grid-template-columns:1fr}.hx .hx-mini{grid-template-columns:repeat(2,minmax(0,1fr))}}
.hx .hx-pg p,.hx .hx-cards>p,.hx .hx-itin>p,.hx .hx-inc>p,.hx .hx-facts>p{display:none}
""".replace('PID', str(PID))
CSS = ' '.join(l.strip() for l in (base + EXTRA).strip().splitlines() if l.strip() and not l.strip().startswith('/*'))
CSS = CSS + (' body.page-id-PID .page-header .entry-title{max-width:19ch;font-size:clamp(32px,3.6vw,52px)!important}'
              ' @media(max-width:700px){body.page-id-PID .page-header .entry-title{font-size:28px!important}}').replace('PID', str(PID))
CSS = CSS + ' @media(min-width:1101px){.hx .hx-itin{grid-template-columns:repeat(3,minmax(0,1fr))}}'
# 13 Nov 2026: 3-line title on phones overlapped the lede — extra hero top padding on this page
CSS = CSS + (' @media(max-width:700px){body.page-id-PID .hx .hx-hero{padding-top:262px}}').replace('PID', str(PID))
# Hostinger WAF (31 Oct 2026) returns 503 for writes containing '@media(' — use the equivalent '@media screen and ('
CSS = CSS.replace('@media(', '@media screen and (')
HERO = ['hongkong-1', 'hongkong-2', 'hongkong-3', 'hongkong-4', 'hongkong-5', 'hongkong-6']
GAL = ['hongkong-7', 'hongkong-8', 'hongkong-9', 'hongkong-10', 'hongkong-11', 'hongkong-12', 'hongkong-13', 'hongkong-14']
FINAL = 'hongkong-15'

FAQ = [
    ("Do Indians need a visa for Hong Kong?", "Indian passport holders can visit Hong Kong visa-free for up to 14 days, but only after they successfully complete the free online Pre-arrival Registration (PAR) of the Hong Kong Immigration Department. Your passport must be valid for at least six months. The result is shown instantly; you print the notification slip on blank A4 white paper, sign it and carry it with the same passport, because airlines check it before boarding and immigration checks it on arrival. A registration is valid for six months and covers multiple visits of up to 14 days each. If the registration is unsuccessful, or you want to stay longer than 14 days, you need a visit visa from the Immigration Department, which normally takes about four weeks. The slip is not a guarantee of entry — admission is always the decision of Hong Kong Immigration."),
    ("Do Indians need a visa for Macau?", "The Macao SAR Government Portal lists India among the nationalities that do not need a visa for Macau, with a stay of up to 30 days for holders of a valid passport. Admission is decided by the Macau immigration authorities at the border. If you go from Hong Kong to Macau and back to Hong Kong, your Hong Kong Pre-arrival Registration covers multiple visits within its six-month validity, so you re-enter Hong Kong on the same slip."),
    ("How many days are enough for Hong Kong and Macau?", "Five nights is a comfortable first trip: three or four nights in Hong Kong for the harbour, Victoria Peak, Lantau and the Big Buddha and one theme-park day, then one night (or a long day trip) in Macau. With three or four nights, keep to Hong Kong and do Macau as a day trip."),
    ("Which is the best time to visit Hong Kong?", "October to December is usually the most comfortable — cooler, drier days that suit walking and the Peak views. March and April are also pleasant. June to September is hot, humid and rainy, and it is the typhoon season, so we keep plans flexible in those months. Chinese New Year (January or February) is festive but busier and more expensive."),
    ("Is Hong Kong good for a family trip with children?", "Yes. Hong Kong Disneyland and Ocean Park are the two big theme-park days, the Ngong Ping 360 cable car and the Star Ferry are fun for children too, and the city is compact with good public transport. We plan one park day (or both) around your children's ages and keep the rest of the days easy-paced."),
    ("Is vegetarian and Indian food available in Hong Kong?", "Yes. Hong Kong has many Indian restaurants, especially around Tsim Sha Tsui in Kowloon, and vegetarian Chinese food is easy to find. Macau has fewer options, so we note vegetarian and Jain needs with hotels in advance and suggest where to eat."),
    ("Why are there no prices on this page?", "Hong Kong costs depend on your dates, hotel area and category, theme-park tickets, the Macau add-on and the airfare from your city. Instead of a teaser price that changes when you ask, we send a costed, day-by-day quote for your dates — usually within 24 hours."),
]

JS = ("(function(){var f=document.getElementById('hxPlan');if(!f){return;}f.addEventListener('submit',function(e){e.preventDefault();"
      "var d=f.querySelector('[name=d]').value,s=f.querySelector('[name=s]').value,m=f.querySelector('[name=m]').value,a=f.querySelector('[name=a]').value,k=f.querySelector('[name=k]').value,c=f.querySelector('[name=c]').value;"
      "var t='Hi Suzu Travels, please send me a costed Hong Kong itinerary.\\nTrip: '+d+'\\nTrip type: '+s+'\\nTravel month: '+m+'\\nAdults: '+a+'\\nChildren: '+k;"
      "if(c){t=t+'\\nDeparting from: '+c;}"
      "window.open('https:'+String.fromCharCode(47,47)+'wa.me/917087488961?text='+encodeURIComponent(t),'_blank','noopener');});})();")

REL = [('singapore-tour-packages', 'Singapore', 'suzu-card-singapore', 'City, Sentosa, Universal'), ('japan-tour-packages', 'Japan', 'suzu-abroad-japan', 'Tokyo, Fuji, Kyoto, Osaka'),
       ('thailand-tour-packages', 'Thailand', 'suzu-card-thailand', 'Bangkok, Phuket, Krabi'), ('malaysia-tour-packages', 'Malaysia', 'suzu-card-malaysia', 'KL, Langkawi, Genting'),
       ('vietnam-tour-packages', 'Vietnam', 'suzu-card-vietnam', 'Hanoi, Ha Long, Hoi An'), ('bali-tour-packages', 'Bali', 'suzu-card-bali', 'Ubud, villas, temples'),
       ('dubai-tour-packages', 'Dubai', 'suzu-abroad-dubai', 'Burj Khalifa, desert, Abu Dhabi'), ('australia-tour-packages', 'Australia & NZ', 'suzu-abroad-australia', 'Sydney, Melbourne, Queenstown'),
       ('maldives-tour-packages', 'Maldives', 'suzu-card-maldives', 'Overwater villas'), ('mauritius-tour-packages', 'Mauritius', 'suzu-abroad-mauritius', 'Lagoons, Le Morne, island tours'),
       ('europe-tour-packages', 'Europe', 'suzu-abroad-europe', 'Paris, Swiss Alps, Italy'), ('switzerland-tour-packages', 'Switzerland', 'suzu-abroad-switzerland', 'Lucerne, Jungfrau, Zermatt'),
       ('uk-tour-packages', 'UK', 'suzu-abroad-uk', 'London, Cotswolds, Scotland'), ('turkey-tour-packages', 'Turkey', 'suzu-abroad-turkey', 'Istanbul, Cappadocia, Pamukkale'),
       ('egypt-tour-packages', 'Egypt', 'suzu-abroad-egypt', 'Cairo, Nile cruise, Luxor'), ('georgia-tour-packages', 'Georgia', 'suzu-abroad-georgia', 'Tbilisi, Kazbegi, Gudauri'),
       ('azerbaijan-tour-packages', 'Azerbaijan', 'suzu-abroad-azerbaijan', 'Baku, Gabala, Shahdag'), ('armenia-tour-packages', 'Armenia', 'suzu-abroad-armenia', 'Yerevan, Garni, Sevan'),
       ('uzbekistan-tour-packages', 'Uzbekistan', 'suzu-abroad-uzbekistan', 'Samarkand, Bukhara, Khiva'), ('kazakhstan-tour-packages', 'Kazakhstan', 'suzu-abroad-kazakhstan', 'Almaty, lakes, Kyrgyzstan'),
       ('sri-lanka-tour-packages', 'Sri Lanka', 'suzu-card-sri-lanka', 'Beaches & tea country'), ('nepal-tour-packages', 'Nepal', 'suzu-card-nepal', 'No visa for Indians'),
       ('bhutan-tour-packages', 'Bhutan', 'suzu-card-bhutan', 'Paro, Thimphu, Punakha')]

def build():
    W = "Hi Suzu Travels, I'm planning a Hong Kong trip. Please share a quote."
    h = [f'<div class="suzu-intl hx hx-country"><style>{CSS}</style>']
    slides = ''.join(f'<div class="hx-slide"><img src="{U(s)}" alt="{A(s)}" width="1600" height="1000" {"fetchpriority=\"high\" loading=\"eager\"" if i == 0 else "loading=\"lazy\""} decoding="async"><span class="hx-cap">{C(s)}</span></div>' for i, s in enumerate(HERO))
    h.append('<section class="hx-hero" aria-label="Hong Kong and Macau tour packages from India"><div class="hx-slides">' + slides + '</div><div class="hx-copy">'
             '<p class="hx-lede">The Victoria Harbour skyline from the Peak, the Star Ferry, the Big Buddha on Lantau, a Disneyland or Ocean Park day for the children, night markets in Kowloon — and old Portuguese Macau just across the water. We plan Hong Kong and Macau to your dates, budget and pace, with well-located hotels, transfers and clear guidance on the free online pre-arrival registration for Indians.</p>'
             '<div class="hx-badges">'
             f'<span class="hx-badge">{svg("globe")}Hong Kong, Lantau &amp; Macau</span><span class="hx-badge">{svg("doc")}Pre-arrival registration guidance</span>'
             f'<span class="hx-badge">{svg("team")}Families, couples &amp; groups</span><span class="hx-badge">{svg("food")}Vegetarian meals planned</span></div>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Get a Hong Kong Quote {svg("arrow")}</a>'
             f'<a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div></div>'
             '<form class="hx-plan" id="hxPlan" aria-label="Get a costed Hong Kong itinerary on WhatsApp"><h3>Plan my Hong Kong trip</h3>'
             '<p>Tell us the basics — we reply on WhatsApp with a costed, day-by-day plan, usually within 24 hours.</p><div class="hx-f">'
             '<label class="hx-full">Trip<select name="d"><option selected>Hong Kong + Macau (classic)</option><option>Hong Kong only</option><option>Hong Kong with Disneyland / Ocean Park</option><option>Hong Kong + Macau honeymoon</option><option>Hong Kong + another country</option><option>Not sure yet</option></select></label>'
             '<label>Trip type<select name="s"><option>Family</option><option>Honeymoon / couple</option><option>Friends</option><option>Seniors</option><option>Group</option><option>Corporate / MICE</option></select></label>'
             f'<label>Travel month<select name="m">{G.months()}</select></label>'
             '<label>Adults<select name="a"><option>1</option><option selected>2</option><option>3</option><option>4</option><option>5</option><option>6</option><option>7–10</option><option>11–20</option><option>20+</option></select></label>'
             '<label>Children<select name="k"><option>0</option><option>1</option><option>2</option><option>3</option><option>4+</option></select></label>'
             '<label class="hx-full">Departing from<input name="c" type="text" placeholder="e.g. Delhi, Mumbai, Chandigarh" autocomplete="address-level2"></label></div>'
             f'<button class="hx-btn" type="submit">{WA_SVG}Get my Hong Kong plan on WhatsApp</button><small>Opens WhatsApp with your details filled in. We do not store anything on this page.</small></form></section>')
    h.append('<div class="hx-trust">'
             f'<div>{svg("clock")}<span><b>Quote in ~24 hours</b><span>Costed, day by day</span></span></div>'
             f'<div>{svg("doc")}<span><b>Honest entry guidance</b><span>Official Hong Kong &amp; Macau rules, checked</span></span></div>'
             f'<div>{svg("shield")}<span><b>HP Tourism registered</b><span>Reg. DTO-MND-11-243/2022</span></span></div>'
             f'<div>{svg("chat")}<span><b>One team, start to finish</b><span>On WhatsApp while you travel</span></span></div></div>')
    h.append('<nav class="hx-toc" aria-label="On this page"><a href="#why-hong-kong">Why Hong Kong</a><a href="#hong-kong-in-photos">Photos</a><a href="#how-to-choose">Choose your trip</a><a href="#sample-itinerary">Sample itinerary</a><a href="#when-to-go">When to go</a><a href="#visa-and-entry">Entry rules</a><a href="#whats-included">What\'s included</a><a href="#hong-kong-faq">FAQ</a></nav>')
    facts = [('Getting there', 'Fly into Hong Kong; we compare direct and connecting flights from your city'), ('Time difference', 'Hong Kong and Macau are 2 hours 30 minutes ahead of India'), ('Currency', 'Hong Kong dollar (HKD); Macau uses the pataca (MOP)'),
             ('Best season', 'October to December; March and April are also pleasant'), ('Typical trip', '4 to 6 nights, including Macau'), ('Entry', 'Hong Kong: free online pre-arrival registration, up to 14 days; Macau: no visa, up to 30 days')]
    h.append('<section id="why-hong-kong" class="hx-sec"><span class="hx-eye">Hong Kong &amp; Macau</span><h2>Why Hong Kong and Macau work so well for Indian travellers</h2>'
             '<p class="hx-sub">Hong Kong packs a lot into a short holiday: a skyline harbour you cross by ferry, a tram up to Victoria Peak, beaches and hiking trails, the Big Buddha on Lantau, two theme parks and street markets that run late into the night. Macau, a short ferry or bridge-bus ride away, adds Portuguese-era squares, temples and the big resorts of Cotai. Entry for Indian passport holders is simple — a free online registration for Hong Kong and no visa for Macau.</p>'
             '<div class="hx-facts">' + ''.join(f'<div class="hx-fact"><b>{a}</b><span>{b}</span></div>' for a, b in facts) + '</div></section>')
    h.append('<section id="hong-kong-in-photos" class="hx-sec"><span class="hx-eye">Real places</span><h2>Hong Kong and Macau in photos</h2>'
             '<p class="hx-sub">Temple Street at night, incense coils in Man Mo Temple, A-Ma Temple and the Ruins of St. Paul\'s in Macau, the Avenue of Stars, the Ocean Park cable car, red Hong Kong taxis on the Kowloon waterfront and Senado Square. Real photos by Wikimedia Commons photographers, credited below.</p><div class="hx-pg">'
             + ''.join(f'<figure><img src="{U(k)}" alt="{A(k)}" width="800" height="600" loading="lazy" decoding="async"><figcaption>{C(k)}</figcaption></figure>' for k in GAL) + '</div></section>')
    cards = [('Families', 'Hong Kong with children', 'A Hong Kong Disneyland or Ocean Park day, the Ngong Ping 360 cable car, the Star Ferry and the Peak — with family rooms close to the metro.'),
             ('Couples', 'Honeymoon in Hong Kong &amp; Macau', 'Harbour views from your room, the Peak at sunset, the evening skyline from Tsim Sha Tsui and a night in Macau.'),
             ('First-timers', 'Hong Kong + Macau classic', 'Hong Kong Island, Kowloon, Lantau and a theme-park day, then Macau&rsquo;s old town and Cotai — a well-paced first visit.'),
             ('Two countries', 'Hong Kong + another country', 'Hong Kong pairs well with Singapore, Thailand or Japan on one ticket; we plan the entry rules for each country together.')]
    stays = [('Tsim Sha Tsui (Kowloon)', 'Harbour views, the Avenue of Stars, shopping and many Indian restaurants, with the Star Ferry and the metro at the door.'),
             ('Central &amp; Admiralty', 'Hong Kong Island&rsquo;s business heart — close to the Peak Tram, the Star Ferry and the Mid-Levels escalator.'),
             ('Lantau / Disneyland area', 'Convenient for a Disneyland day and the airport; quieter, and good for families with small children.'),
             ('Macau (Cotai or the peninsula)', 'Big resort hotels in Cotai, or a smaller hotel near the historic centre for Senado Square and St. Paul&rsquo;s.')]
    h.append('<section id="how-to-choose" class="hx-sec"><span class="hx-eye">How to choose</span><h2>Choose the Hong Kong trip that fits you</h2>'
             '<p class="hx-sub">Start from the kind of trip you want — we fine-tune the days, hotels, transfers and tickets to your group.</p><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><span class="hx-tag">{t}</span><h3>{n}</h3><p>{d}</p></div>' for t, n, d in cards) + '</div>'
             '<h3 style="margin-top:30px">Where to stay</h3><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><h3>{n}</h3><p>{d}</p></div>' for n, d in stays) + '</div></section>')
    days = [('Day 1', 'Arrive in Hong Kong', 'Airport transfer to your hotel. In the evening, walk the Tsim Sha Tsui waterfront and the Avenue of Stars for the lit-up Hong Kong Island skyline across the harbour.'),
            ('Day 2', 'Hong Kong Island', 'Up to Victoria Peak for the view over the harbour, then Central, Man Mo Temple on Hollywood Road and the Star Ferry back to Kowloon.'),
            ('Day 3', 'Lantau &amp; the Big Buddha', 'Ride the Ngong Ping 360 cable car to the Tian Tan Buddha and Po Lin Monastery. Evening at the Temple Street night market.'),
            ('Day 4', 'Disneyland or Ocean Park', 'A full theme-park day — Hong Kong Disneyland or Ocean Park — or a free day for shopping and the city if you prefer.'),
            ('Day 5', 'Macau', 'By ferry or bridge bus to Macau: the Ruins of St. Paul&rsquo;s, Senado Square, A-Ma Temple, the Macau Tower and the resorts of Cotai. Stay overnight or return to Hong Kong.'),
            ('Day 6', 'Fly home', 'Free morning, then transfer to Hong Kong airport for your flight home.')]
    h.append('<section id="sample-itinerary" class="hx-sec"><span class="hx-eye">Sample plan</span><h2>A sample 6-day Hong Kong &amp; Macau itinerary</h2>'
             '<p class="hx-sub">The classic first trip. We rebuild it around you — a shorter Hong Kong-only break, two theme-park days for the children, or an extra night in Macau.</p><div class="hx-itin">'
             + ''.join(f'<div class="hx-day"><i>{a}</i><b>{b}</b><p>{c}</p></div>' for a, b, c in days) + '</div></section>')
    seasons = [('Oct – Dec', '<span class="hx-ok">Best</span>', 'Mild, mostly dry', 'Comfortable days for walking, the Peak and Lantau, with clearer harbour views; Diwali and year-end holidays are popular — book early.'),
               ('Mar – Apr', '<span class="hx-ok">Good</span>', 'Warm, can be misty', 'Pleasant temperatures for sightseeing and theme parks; some days are humid or hazy.'),
               ('Jan – Feb', '<span class="hx-mid">Cool</span>', 'Cool, dry', 'Good sightseeing weather; around Chinese New Year the city is festive but busier and hotels cost more.'),
               ('May', '<span class="hx-mid">Warm</span>', 'Hot, humid', 'Getting hot and humid, with more showers; we keep afternoons indoors or at the parks.'),
               ('Jun – Sep', '<span class="hx-hot">Hot &amp; wet</span>', 'Hot, rainy, typhoons', 'Indian summer holidays fall here: it works, but it is the hot, rainy typhoon season — we keep the plan flexible and choose indoor options for bad-weather days.')]
    h.append('<section id="when-to-go" class="hx-sec"><span class="hx-eye">Best season</span><h2>When to go to Hong Kong</h2>'
             '<p class="hx-sub">Hong Kong and Macau have a subtropical climate — warm to hot for most of the year, with the most comfortable weather in autumn and early winter. We check the season, holidays and flight prices against your plan before we quote.</p>'
             '<div class="hx-tw"><table class="hx-t"><thead><tr><th>Months</th><th>Verdict</th><th>Weather</th><th>What it means for your trip</th></tr></thead><tbody>'
             + ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in seasons) + '</tbody></table></div></section>')
    h.append('<section id="visa-and-entry" class="hx-sec"><span class="hx-eye">Visa &amp; entry</span><h2>Hong Kong and Macau entry rules for Indian passport holders</h2>'
             '<div class="hx-visa"><div class="hx-vbox"><h3>What the official rules say</h3><ul>'
             '<li><b>Hong Kong:</b> Indian nationals must apply for and <b>successfully complete Pre-arrival Registration (PAR) online</b> before they can visit visa-free. It is <b>free of charge</b>, needs an Indian passport <b>valid for at least six months</b>, and covers a stay of <b>up to 14 days</b> per visit.</li>'
             '<li>The result is shown instantly. You must <b>print the notification slip on blank A4 white paper, sign it</b> and carry it with the <b>same passport</b> — airlines check it before boarding and Hong Kong Immigration checks it on arrival.</li>'
             '<li>A registration is <b>valid for six months</b> and can be used for <b>multiple visits</b> of up to 14 days each — useful for a Hong Kong → Macau → Hong Kong trip.</li>'
             '<li>If the registration is unsuccessful, or you want to stay longer than 14 days, you need a <b>visit visa from the Hong Kong Immigration Department</b> (normally about four weeks).</li>'
             '<li><b>Macau:</b> the Macao SAR Government Portal lists <b>India among the nationalities that do not need a visa</b>, with a stay of <b>up to 30 days</b> for holders of a valid passport.</li></ul>'
             f'<p class="hx-checked">Checked {CHECKED} · sources: <a href="{SRC_HK}" target="_blank" rel="noopener nofollow">Hong Kong Immigration Department — Pre-arrival Registration for Indian Nationals</a> · <a href="{SRC_MO}" target="_blank" rel="noopener nofollow">Macao SAR Government Portal — immigration clearance of non-residents</a></p></div>'
             '<div class="hx-vnote"><p><b>Please note:</b> admission at the border, and any visa, is always the decision of the immigration authorities of Hong Kong and of Macau. The registration slip is not a guarantee of entry. We help you prepare correctly, but we never promise an outcome we do not control.</p>'
             '<p>We send you the official registration link and a checklist, give you a day-by-day plan with hotel details, and confirm non-refundable bookings only after your registration is successful. If you add another country, we check its entry rules at the same time.</p></div></div></section>')
    inc = [('doc', 'Entry guidance', 'Step-by-step help with Hong Kong&rsquo;s pre-arrival registration and a checklist for Macau, matched to your trip.'), ('pin', 'Hotels', 'Named hotels in Tsim Sha Tsui, Central or near Disneyland, plus Macau if you stay overnight.'),
           ('team', 'Transfers', 'Airport transfers and the ferry or bridge-bus connection to Macau and back.'), ('globe', 'Tickets &amp; tours', 'Peak, Ngong Ping 360, Disneyland or Ocean Park tickets and guided tours, as you choose.'),
           ('food', 'Meal plan', 'Breakfast at most hotels; vegetarian and Jain needs noted in advance, with Indian restaurant suggestions.'), ('award', 'Flights optional', 'Land-only, or a full package with international flights from your nearest Indian airport.')]
    h.append('<section id="whats-included" class="hx-sec"><span class="hx-eye">Your package</span><h2>What a Suzu Hong Kong package includes</h2><div class="hx-inc">'
             + ''.join(f'<div>{svg(i)}<span><b>{t}</b><span>{d}</span></span></div>' for i, t, d in inc) + '</div></section>')
    steps = [('chat', 'Tell us the basics', 'Dates, travellers and the kind of trip you want. A WhatsApp message is enough.'),
             ('doc', 'Get a costed itinerary', 'A day-by-day plan with named hotels and a clear per-person price, usually within 24 hours.'),
             ('sliders', 'Adjust until it fits', 'Change the days, hotels, theme parks or the Macau night. We re-quote as needed.'),
             ('lock', 'Confirm with a token', 'Lock your plan with a small token amount; the balance is paid later, as agreed in writing.')]
    h.append('<section id="how-booking-works" class="hx-sec"><span class="hx-eye">Simple process</span><h2>How booking works</h2><div class="hx-steps">'
             + ''.join(f'<div class="hx-step"><div class="hx-n">{svg(i)}</div><b>{t}</b><p>{d}</p></div>' for i, t, d in steps) + '</div></section>')
    h.append('<section id="hong-kong-faq" class="hx-sec"><span class="hx-eye">FAQ</span><h2>Common questions about a Hong Kong tour</h2><div class="hx-faqs">'
             + ''.join(f'<details class="hx-faq"{" open" if k == 0 else ""}><summary>{html.escape(q)}</summary><div class="hx-ans"><p>{html.escape(a)}</p></div></details>' for k, (q, a) in enumerate(FAQ)) + '</div></section>')
    h.append('<section id="more-destinations" class="hx-sec"><span class="hx-eye">Explore more</span><h2>Explore more destinations</h2>'
             '<p class="hx-sub">Every trip is planned the same way — your dates, your budget, one team from quote to return. <a href="https://suzutravels.com/international-tour-packages/">See all international holidays →</a></p><div class="hx-mini">'
             + ''.join(f'<a class="hx-mc" href="https://suzutravels.com/{p}/"><img src="https://suzutravels.com/wp-content/uploads/2026/10/{img}.webp" alt="{html.escape(n)} holiday — Suzu Travels" width="640" height="360" loading="lazy" decoding="async"><span><b>{html.escape(n)}</b><em>{html.escape(e)}</em></span></a>' for p, n, img, e in REL) + '</div></section>')
    h.append(f'<div class="hx-final"><img src="{U(FINAL)}" alt="{A(FINAL)}" width="1600" height="900" loading="lazy" decoding="async">'
             '<h2>Plan your Hong Kong trip</h2><p>Send us your dates and group size. We will come back with a costed, day-by-day Hong Kong and Macau itinerary you can compare, no obligation.</p>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Request a Hong Kong Quote {svg("arrow")}</a><a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div>'
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
    open('pages/hong-kong-tour-packages.html', 'w').write(o)
    print('pages/hong-kong-tour-packages.html', len(o))
