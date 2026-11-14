#!/usr/bin/env python3
"""China page — .hx design; same template as gen_hongkong.py.
Run from outbound-kit/:  python3 pages/gen_china.py <PAGE_ID> -> pages/china-tour-packages.html (one line)
Facts (official pages read 14 Nov 2026):
- Embassy of China in India, "Notice on Chinese Visa Application (2026.10.22)": submit by consular district (Maharashtra +
  Karnataka -> CG Mumbai; Bihar, Jharkhand, Odisha, Chhattisgarh, West Bengal temporarily -> Embassy; rest -> Embassy);
  online form + document upload at consular.mfa.gov.cn/VISA/ for online review (no fee); after approval email, submit
  passport/documents in person within 30 days; fee paid on collection. Passport > 6 months, >= 2 blank pages, previous
  passports of past 5 years; 2 photos 48x33 mm white background; tourist (L): 6 months savings statements with average
  monthly balance >= INR 1 lakh or deposit certificate (>= 3 months old). Fingerprints exempt until 31 Dec 2026 for
  short-term visas <= 180 days. Processing 7 working days regular / 4 express (from day after submission).
  HK/Macao: separate rules.
- Embassy notice 22 Oct 2026: from 26 Oct 2026 Embassy + CG Mumbai accept applications directly; Kolkata district temporarily Embassy.
Keyword Planner IN 14 Nov 2026: "china tour package" 5,400/mo (focus kw), "china trip cost from india" 1,300,
"china tour package from india" 1,300, "china visa for indians" 22,200, "shanghai tour package" 260.
Photos: Wikimedia Commons (CC0 / CC BY / CC BY-SA / GFDL; licence read from each file page's wikitext 14 Nov 2026), WP IDs 22258-22270.
Climate/season wording is general guidance (no figures); no prices.
"""

import json, html, sys, os
sys.path.insert(0, os.getcwd())
import gen_hub as G

PID = int(sys.argv[1]) if len(sys.argv) > 1 else 0
M = G.M
svg, WA_SVG, wa = G.svg, G.WA_SVG, G.wa
CHECKED = '14 November 2026'
SRC_CN = 'https://in.china-embassy.gov.cn/eng/sggg/202408/t20240820_11476941.htm'
SRC_CN2 = 'https://in.china-embassy.gov.cn/eng/gdxw/202610/t20261022_12044936.htm'
SRC_ON = 'https://consular.mfa.gov.cn/VISA/'

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
body.page-id-PID .page-header:before{content:"Holidays abroad \00B7  China";display:inline-block;font:800 12px/1 "Plus Jakarta Sans",sans-serif;letter-spacing:.18em;text-transform:uppercase;color:#1a1606;background:#E2C158;padding:8px 13px;border-radius:999px;margin-bottom:16px}
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
HERO = ['china-1', 'china-2', 'china-3', 'china-4', 'china-5', 'china-6']
GAL = ['china-8', 'china-9', 'china-10', 'china-7', 'china-12', 'china-11', 'china-13']
FINAL = 'china-1'  # reuses hero slide 1 (Mutianyu) — Badaling snow moved into the 7-photo gallery

FAQ = [
    ("Do Indians need a visa for China?", "Yes. Indian passport holders need a Chinese visa for a holiday in mainland China — for tourism this is the L (tourist) visa, issued by the Chinese Embassy in New Delhi or the Chinese Consulate General in Mumbai. You first fill in and submit the visa application form online for review on the official Chinese consular website; once the online review is approved you receive an email and, within 30 days, take your passport and documents to the Embassy or Consulate in person. The Embassy lists regular processing as 7 working days and express as 4 working days, counted from the day after you hand in your passport. Approval is always the decision of the Chinese authorities — we help you prepare, but we never promise an outcome."),
    ("Which documents does a tourist (L) visa need?", "The Embassy's notice lists the online application form, a passport valid for more than six months with at least two blank visa pages (plus any previous passport issued in the past five years), two recent colour photos (48 mm × 33 mm, white background) and, for tourist visas, personal savings bank statements for the last six months with a consistent average monthly balance of at least INR 1 lakh, or a bank deposit certificate of a similar amount made at least three months before you apply. Children under 18 need extra documents. Requirements can change, so we always send you the current official checklist."),
    ("Where do I submit my China visa application?", "Applicants living in Maharashtra and Karnataka submit at the Chinese Consulate General in Mumbai. Applicants from Bihar, Jharkhand, Odisha, Chhattisgarh and West Bengal currently submit at the Chinese Embassy in New Delhi, as do applicants from all other states. Since 26 October 2026 the Embassy and the Mumbai Consulate accept applications directly. Until 31 December 2026, fingerprints are not collected for short-term visas of up to 180 days."),
    ("How many days are enough for a China trip?", "Eight days is a comfortable first trip for Beijing, Xi'an and Shanghai, travelling between the cities by high-speed train or short flight. Add three or four days for Zhangjiajie's sandstone pillars, or for Guilin and the Li River to Yangshuo."),
    ("Which is the best time to visit China?", "April to May and September to October usually bring the most comfortable weather for Beijing, Xi'an and Shanghai. Summer is hot and humid with more rain, and northern winters are cold and dry (the Great Wall can be beautiful in snow). China's national holidays in early May and the first week of October are very crowded, so we plan around them."),
    ("Is vegetarian and Indian food available in China?", "In Beijing and Shanghai there are Indian restaurants and vegetarian Buddhist restaurants; in smaller places it takes more planning. We note vegetarian and Jain needs with hotels in advance and give you a written food card in Chinese to show at restaurants."),
    ("Will my phone, WhatsApp and Google work in China?", "Many apps Indian travellers use every day, including Google services and WhatsApp, do not work normally on mainland China networks. We share your full plan in advance (offline), keep phone contact with you and suggest how to stay connected and pay — mobile payment apps are widely used in China."),
    ("Why are there no prices on this page?", "China costs depend on your dates, cities, hotel category, train or flight connections between cities, entry tickets and the airfare from your city. Instead of a teaser price that changes when you ask, we send a costed, day-by-day quote for your dates — usually within 24 hours."),
]

JS = ("(function(){var f=document.getElementById('hxPlan');if(!f){return;}f.addEventListener('submit',function(e){e.preventDefault();"
      "var d=f.querySelector('[name=d]').value,s=f.querySelector('[name=s]').value,m=f.querySelector('[name=m]').value,a=f.querySelector('[name=a]').value,k=f.querySelector('[name=k]').value,c=f.querySelector('[name=c]').value;"
      "var t='Hi Suzu Travels, please send me a costed China itinerary.\\nTrip: '+d+'\\nTrip type: '+s+'\\nTravel month: '+m+'\\nAdults: '+a+'\\nChildren: '+k;"
      "if(c){t=t+'\\nDeparting from: '+c;}"
      "window.open('https:'+String.fromCharCode(47,47)+'wa.me/917087488961?text='+encodeURIComponent(t),'_blank','noopener');});})();")

REL = [('hong-kong-tour-packages', 'Hong Kong & Macau', None, 'Harbour, Peak, Disneyland, Macau'), ('japan-tour-packages', 'Japan', 'suzu-abroad-japan', 'Tokyo, Fuji, Kyoto, Osaka'),
       ('singapore-tour-packages', 'Singapore', 'suzu-card-singapore', 'City, Sentosa, Universal'),
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
HK_IMG = 'https://suzutravels.com/wp-content/uploads/2026/11/hong-kong-victoria-harbour-night-from-the-peak-768x363.webp'

def build():
    W = "Hi Suzu Travels, I'm planning a China trip. Please share a quote."
    h = [f'<div class="suzu-intl hx hx-country"><style>{CSS}</style>']
    slides = ''.join(f'<div class="hx-slide"><img src="{U(s)}" alt="{A(s)}" width="1600" height="1000" {"fetchpriority=\"high\" loading=\"eager\"" if i == 0 else "loading=\"lazy\""} decoding="async"><span class="hx-cap">{C(s)}</span></div>' for i, s in enumerate(HERO))
    h.append('<section class="hx-hero" aria-label="China tour packages from India"><div class="hx-slides">' + slides + '</div><div class="hx-copy">'
             '<p class="hx-lede">Walk the Great Wall, step into the Forbidden City, stand before the Terracotta Army in Xi&rsquo;an and watch the Shanghai skyline light up from the Bund — then add the sandstone pillars of Zhangjiajie or the Li River at Guilin. We plan China to your dates, budget and pace, with well-located hotels, high-speed trains between cities, vegetarian meals noted in advance and an honest, step-by-step guide to the Chinese tourist visa.</p>'
             '<div class="hx-badges">'
             f'<span class="hx-badge">{svg("globe")}Beijing, Xi&rsquo;an &amp; Shanghai</span><span class="hx-badge">{svg("doc")}Tourist visa checklist</span>'
             f'<span class="hx-badge">{svg("team")}Families, couples &amp; groups</span><span class="hx-badge">{svg("food")}Vegetarian meals planned</span></div>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Get a China Quote {svg("arrow")}</a>'
             f'<a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div></div>'
             '<form class="hx-plan" id="hxPlan" aria-label="Get a costed China itinerary on WhatsApp"><h3>Plan my China trip</h3>'
             '<p>Tell us the basics — we reply on WhatsApp with a costed, day-by-day plan, usually within 24 hours.</p><div class="hx-f">'
             '<label class="hx-full">Trip<select name="d"><option selected>Beijing + Xi&#39;an + Shanghai (classic)</option><option>Beijing + Shanghai</option><option>Classic + Zhangjiajie</option><option>Classic + Guilin &amp; Yangshuo</option><option>China + Hong Kong</option><option>Not sure yet</option></select></label>'
             '<label>Trip type<select name="s"><option>Family</option><option>Honeymoon / couple</option><option>Friends</option><option>Seniors</option><option>Group</option><option>Corporate / MICE</option></select></label>'
             f'<label>Travel month<select name="m">{G.months()}</select></label>'
             '<label>Adults<select name="a"><option>1</option><option selected>2</option><option>3</option><option>4</option><option>5</option><option>6</option><option>7–10</option><option>11–20</option><option>20+</option></select></label>'
             '<label>Children<select name="k"><option>0</option><option>1</option><option>2</option><option>3</option><option>4+</option></select></label>'
             '<label class="hx-full">Departing from<input name="c" type="text" placeholder="e.g. Delhi, Mumbai, Chandigarh" autocomplete="address-level2"></label></div>'
             f'<button class="hx-btn" type="submit">{WA_SVG}Get my China plan on WhatsApp</button><small>Opens WhatsApp with your details filled in. We do not store anything on this page.</small></form></section>')
    h.append('<div class="hx-trust">'
             f'<div>{svg("clock")}<span><b>Quote in ~24 hours</b><span>Costed, day by day</span></span></div>'
             f'<div>{svg("doc")}<span><b>Honest visa guidance</b><span>Official Chinese Embassy rules, checked</span></span></div>'
             f'<div>{svg("shield")}<span><b>HP Tourism registered</b><span>Reg. DTO-MND-11-243/2022</span></span></div>'
             f'<div>{svg("chat")}<span><b>One team, start to finish</b><span>Reachable while you travel</span></span></div></div>')
    h.append('<nav class="hx-toc" aria-label="On this page"><a href="#why-china">Why China</a><a href="#china-in-photos">Photos</a><a href="#how-to-choose">Choose your trip</a><a href="#sample-itinerary">Sample itinerary</a><a href="#when-to-go">When to go</a><a href="#visa-and-entry">Visa</a><a href="#whats-included">What\'s included</a><a href="#china-faq">FAQ</a></nav>')
    facts = [('Getting there', 'Fly into Beijing or Shanghai; we compare direct and connecting flights from your city'), ('Time difference', 'China is 2 hours 30 minutes ahead of India'), ('Currency', 'Chinese yuan (renminbi, CNY); mobile payments are widely used'),
             ('Best season', 'April to May and September to October'), ('Typical trip', '7 to 10 nights; 10 to 13 with Zhangjiajie or Guilin'), ('Entry', 'Tourist (L) visa from the Chinese Embassy or Consulate in India — online form first')]
    h.append('<section id="why-china" class="hx-sec"><span class="hx-eye">China</span><h2>Why China is worth the journey for Indian travellers</h2>'
             '<p class="hx-sub">Few countries put so many world-famous sights into one trip: the Great Wall and the Forbidden City in Beijing, the Terracotta Army in Xi&rsquo;an, the Bund and the Pudong skyline in Shanghai, and landscapes such as Zhangjiajie&rsquo;s sandstone pillars and the karst peaks along the Li River. Fast trains and good domestic flights link the big cities. The tourist visa needs some paperwork — we walk you through it with the official checklist.</p>'
             '<div class="hx-facts">' + ''.join(f'<div class="hx-fact"><b>{a}</b><span>{b}</span></div>' for a, b in facts) + '</div></section>')
    h.append('<section id="china-in-photos" class="hx-sec"><span class="hx-eye">Real places</span><h2>China in photos</h2>'
             '<p class="hx-sub">The Bund seen from Pudong, Yu Garden in old Shanghai, the Marble Boat and the imperial boathouses at Beijing&rsquo;s Summer Palace, the Badaling section of the Great Wall in snow, a bronze water vat in the Forbidden City and the museum at the Terracotta Army site in Xi&rsquo;an. Real photos by Wikimedia Commons photographers, credited below.</p><div class="hx-pg">'
             + ''.join(f'<figure><img src="{U(k)}" alt="{A(k)}" width="800" height="600" loading="lazy" decoding="async"><figcaption>{C(k)}</figcaption></figure>' for k in GAL) + '</div></section>')
    cards = [('First-timers', 'Beijing, Xi&rsquo;an &amp; Shanghai', 'The classic first trip: the Great Wall, Forbidden City, Terracotta Army and the Shanghai skyline, linked by high-speed train.'),
             ('Nature', 'Zhangjiajie or Guilin add-on', 'Add three or four days for Zhangjiajie&rsquo;s sandstone pillars, or for the Li River and the karst countryside of Yangshuo.'),
             ('Families', 'China with children', 'Easy-paced days, the Great Wall by cable car, Shanghai&rsquo;s riverfront and parks, and family rooms close to the metro.'),
             ('Two places', 'China + Hong Kong', 'Combine mainland China with Hong Kong and Macau; we plan the separate entry rules for each together.')]
    stays = [('Beijing — Wangfujing / Dongcheng', 'Central for the Forbidden City, Tiananmen Square and Jingshan Park, with shopping streets and the metro close by.'),
             ('Xi&rsquo;an — inside the City Wall', 'Walk to the Bell Tower, the Muslim Quarter and the wall itself; the Terracotta Army is a day trip.'),
             ('Shanghai — the Bund / Nanjing Road', 'River views, the Bund promenade and Yu Garden nearby; Pudong across the river for skyline hotels.'),
             ('Zhangjiajie or Yangshuo', 'Wulingyuan for the national park, or a riverside stay in Yangshuo for the Li River countryside.')]
    h.append('<section id="how-to-choose" class="hx-sec"><span class="hx-eye">How to choose</span><h2>Choose the China trip that fits you</h2>'
             '<p class="hx-sub">Start from the kind of trip you want — we fine-tune the cities, hotels, trains, flights and tickets to your group.</p><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><span class="hx-tag">{t}</span><h3>{n}</h3><p>{d}</p></div>' for t, n, d in cards) + '</div>'
             '<h3 style="margin-top:30px">Where to stay</h3><div class="hx-cards">'
             + ''.join(f'<div class="hx-card"><h3>{n}</h3><p>{d}</p></div>' for n, d in stays) + '</div></section>')
    days = [('Day 1', 'Arrive in Beijing', 'Airport transfer to your hotel. An easy evening walk on Wangfujing street to settle in.'),
            ('Day 2', 'Forbidden City', 'Tiananmen Square and the Forbidden City, then up Jingshan Park for the view over its golden roofs.'),
            ('Day 3', 'The Great Wall', 'A day at the Mutianyu section of the Great Wall, with a cable car up for an easier walk. Evening free.'),
            ('Day 4', 'Summer Palace → Xi&rsquo;an', 'Morning at the Summer Palace and Kunming Lake, then the high-speed train to Xi&rsquo;an.'),
            ('Day 5', 'Terracotta Army', 'The Terracotta Army museum and pits outside Xi&rsquo;an; evening on the Xi&rsquo;an City Wall or in the Muslim Quarter.'),
            ('Day 6', 'Xi&rsquo;an → Shanghai', 'Train or short flight to Shanghai. Evening on the Bund, looking across the river at the Pudong skyline.'),
            ('Day 7', 'Shanghai', 'Yu Garden and the old town, Nanjing Road, then Pudong for the view from one of the tall towers.'),
            ('Day 8', 'Fly home', 'Free morning, then transfer to Shanghai airport for your flight home.')]
    h.append('<section id="sample-itinerary" class="hx-sec"><span class="hx-eye">Sample plan</span><h2>A sample 8-day China itinerary</h2>'
             '<p class="hx-sub">The classic first trip. We rebuild it around you — a shorter Beijing and Shanghai break, an extra day in Xi&rsquo;an, or add-ons to Zhangjiajie, Guilin and Yangshuo or Hong Kong.</p><div class="hx-itin">'
             + ''.join(f'<div class="hx-day"><i>{a}</i><b>{b}</b><p>{c}</p></div>' for a, b, c in days) + '</div></section>')
    seasons = [('Apr – May', '<span class="hx-ok">Best</span>', 'Mild, spring', 'Comfortable days for the Great Wall and city walking; avoid the national holiday in early May if you can.'),
               ('Sep – Oct', '<span class="hx-ok">Best</span>', 'Mild, mostly dry', 'Clear autumn weather in Beijing and Xi&rsquo;an; the first week of October is a national holiday and very crowded.'),
               ('Nov &amp; Mar', '<span class="hx-mid">Good</span>', 'Cool', 'Cooler and quieter; good value for city trips — pack warm layers for the north.'),
               ('Dec – Feb', '<span class="hx-mid">Cold</span>', 'Cold, dry in the north', 'Beijing is cold, and the Great Wall can be beautiful in snow; around Chinese New Year travel is busy.'),
               ('Jun – Aug', '<span class="hx-hot">Hot &amp; wet</span>', 'Hot, humid, rainy', 'Indian summer holidays fall here: it works, but it is hot and wet in most regions — we plan early starts and indoor options.')]
    h.append('<section id="when-to-go" class="hx-sec"><span class="hx-eye">Best season</span><h2>When to go to China</h2>'
             '<p class="hx-sub">China is large and its climate varies by region, but spring and autumn are the most comfortable seasons for the classic Beijing, Xi&rsquo;an and Shanghai route. We check the season, Chinese holidays and flight prices against your plan before we quote.</p>'
             '<div class="hx-tw"><table class="hx-t"><thead><tr><th>Months</th><th>Verdict</th><th>Weather</th><th>What it means for your trip</th></tr></thead><tbody>'
             + ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in seasons) + '</tbody></table></div></section>')
    h.append('<section id="visa-and-entry" class="hx-sec"><span class="hx-eye">Visa &amp; entry</span><h2>China tourist visa for Indian passport holders</h2>'
             '<div class="hx-visa"><div class="hx-vbox"><h3>What the official rules say</h3><ul>'
             '<li><b>A visa is needed.</b> For a holiday in mainland China, Indian passport holders apply for a <b>tourist (L) visa</b> at the <b>Chinese Embassy in New Delhi</b> or the <b>Chinese Consulate General in Mumbai</b> (for residents of Maharashtra and Karnataka). Applicants from Bihar, Jharkhand, Odisha, Chhattisgarh and West Bengal currently apply in New Delhi.</li>'
             f'<li><b>Online first:</b> fill in the visa application form and upload the documents on the <a href="{SRC_ON}" target="_blank" rel="noopener nofollow">official Chinese consular website</a> for online review (no fee at this step). After approval you get an email and must <b>submit your passport and documents in person within 30 days</b>; the fee is paid when you collect the visa.</li>'
             '<li><b>Documents</b> include a passport <b>valid for more than six months</b> with at least two blank visa pages (and any previous passport from the last five years), two recent 48 mm × 33 mm colour photos on a white background and, for a tourist visa, <b>six months of personal savings bank statements with an average monthly balance of at least INR 1 lakh</b>, or a bank deposit certificate of a similar amount made at least three months before applying.</li>'
             '<li><b>Processing time:</b> 7 working days regular, 4 working days express, counted from the day after the passport is submitted. Until 31 December 2026, fingerprints are not collected for short-term visas of up to 180 days.</li>'
             '<li><b>Hong Kong and Macau</b> have their own entry rules, separate from the mainland China visa — see our <a href="https://suzutravels.com/hong-kong-tour-packages/#visa-and-entry">Hong Kong &amp; Macau page</a>.</li></ul>'
             f'<p class="hx-checked">Checked {CHECKED} · sources: <a href="{SRC_CN}" target="_blank" rel="noopener nofollow">Embassy of China in India — Notice on Chinese Visa Application</a> · <a href="{SRC_CN2}" target="_blank" rel="noopener nofollow">Embassy notice on direct acceptance of visa applications (from 26 Oct 2026)</a></p></div>'
             '<div class="hx-vnote"><p><b>Please note:</b> whether a visa is issued, and admission at the border, is always the decision of the Chinese authorities. We help you prepare a complete application, but we never promise an outcome we do not control.</p>'
             '<p>We send you the current official checklist, a day-by-day itinerary with hotel bookings for your application, and confirm non-refundable bookings only once your visa is issued. Apply well ahead of your travel dates — we suggest at least a month.</p></div></div></section>')
    inc = [('doc', 'Visa paperwork help', 'The current official checklist, a day-by-day itinerary and hotel details for your tourist (L) visa application.'), ('pin', 'Hotels', 'Named, central hotels in Beijing, Xi&rsquo;an and Shanghai, plus Zhangjiajie or Yangshuo if you add them.'),
           ('team', 'Transfers &amp; trains', 'Airport transfers, high-speed train or domestic flight tickets between cities, and station transfers.'), ('globe', 'Tickets &amp; guides', 'Great Wall cable car, Forbidden City and Terracotta Army tickets and English-speaking guides, as you choose.'),
           ('food', 'Meal plan', 'Breakfast at most hotels; vegetarian and Jain needs noted in advance, with a food card in Chinese and Indian restaurant suggestions.'), ('award', 'Flights optional', 'Land-only, or a full package with international flights from your nearest Indian airport.')]
    h.append('<section id="whats-included" class="hx-sec"><span class="hx-eye">Your package</span><h2>What a Suzu China package includes</h2><div class="hx-inc">'
             + ''.join(f'<div>{svg(i)}<span><b>{t}</b><span>{d}</span></span></div>' for i, t, d in inc) + '</div></section>')
    steps = [('chat', 'Tell us the basics', 'Dates, travellers and the kind of trip you want. A WhatsApp message is enough.'),
             ('doc', 'Get a costed itinerary', 'A day-by-day plan with named hotels and a clear per-person price, usually within 24 hours.'),
             ('sliders', 'Adjust until it fits', 'Change the cities, hotels, trains or add-ons. We re-quote as needed.'),
             ('lock', 'Confirm with a token', 'Lock your plan with a small token amount; the balance is paid later, as agreed in writing.')]
    h.append('<section id="how-booking-works" class="hx-sec"><span class="hx-eye">Simple process</span><h2>How booking works</h2><div class="hx-steps">'
             + ''.join(f'<div class="hx-step"><div class="hx-n">{svg(i)}</div><b>{t}</b><p>{d}</p></div>' for i, t, d in steps) + '</div></section>')
    h.append('<section id="china-faq" class="hx-sec"><span class="hx-eye">FAQ</span><h2>Common questions about a China tour</h2><div class="hx-faqs">'
             + ''.join(f'<details class="hx-faq"{" open" if k == 0 else ""}><summary>{html.escape(q)}</summary><div class="hx-ans"><p>{html.escape(a)}</p></div></details>' for k, (q, a) in enumerate(FAQ)) + '</div></section>')
    def _img(img): return HK_IMG if img is None else f'https://suzutravels.com/wp-content/uploads/2026/10/{img}.webp'
    h.append('<section id="more-destinations" class="hx-sec"><span class="hx-eye">Explore more</span><h2>Explore more destinations</h2>'
             '<p class="hx-sub">Every trip is planned the same way — your dates, your budget, one team from quote to return. <a href="https://suzutravels.com/international-tour-packages/">See all international holidays →</a></p><div class="hx-mini">'
             + ''.join(f'<a class="hx-mc" href="https://suzutravels.com/{p}/"><img src="{_img(img)}" alt="{html.escape(n)} holiday — Suzu Travels" width="640" height="360" loading="lazy" decoding="async"><span><b>{html.escape(n)}</b><em>{html.escape(e)}</em></span></a>' for p, n, img, e in REL) + '</div></section>')
    h.append(f'<div class="hx-final"><img src="{U(FINAL)}" alt="{A(FINAL)}" width="1600" height="900" loading="lazy" decoding="async">'
             '<h2>Plan your China trip</h2><p>Send us your dates and group size. We will come back with a costed, day-by-day China itinerary you can compare, no obligation.</p>'
             f'<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Request a China Quote {svg("arrow")}</a><a class="hx-ghost" href="{wa(W)}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div>'
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
    open('pages/china-tour-packages.html', 'w').write(o)
    print('pages/china-tour-packages.html', len(o))
