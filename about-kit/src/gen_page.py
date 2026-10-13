# Suzu Travels — About page generator. python3 gen_page.py [preview]
# Produces out/about.html (readable) and out/about.min.html (one line, what goes into WordPress page 9964).
import json, math, re, sys, html, os
from team import TEAM
E = html.escape
PREVIEW = len(sys.argv) > 1 and sys.argv[1] == 'preview'
CFG = json.load(open('config.json'))           # cdn, images (slug -> url)
CDN = '.' if PREVIEW else CFG['cdn']
def IMG(slug): return f'team/suzu-team-{slug}.webp' if PREVIEW else CFG['images'][slug]
def MED(n): return f'media/{n}' if PREVIEW else f"{CFG['cdn']}/media/{n}"
PHONE = '+91 70874 88961'; TEL = 'tel:+917087488961'
def wa(t): return 'https://wa.me/917087488961?text=' + re.sub(r'\s', '%20', t).replace("'", '%27').replace(',', '%2C').replace('?', '%3F').replace(':', '%3A')
WA = wa('Hi Suzu Travels, I read your About page and want to plan a trip. Destination: ___ , dates: ___ , people: ___')
WA_B2B = wa('Hi Suzu Travels, I am a travel agent and want to become a B2B partner. Agency name: ___ , city: ___')
REV = json.load(open('reviews.json'))
RATING, COUNT = REV['rating_text'], REV['count']

# ---------- icons (simple stroke icons, drawn for this kit) ----------
def ic(name):
    P = {
     'wa': '<path d="M3.5 20.5l1.3-4.2A8.5 8.5 0 1 1 8 19.4z"/><path d="M9 8.6c.2 2.6 2.8 5.4 5.6 5.8l1.3-1.3-2-1-1 .8c-1-.4-2-1.4-2.4-2.4l.8-1-1-2z"/>',
     'down': '<path d="M12 5v14M6 13l6 6 6-6"/>',
     'phone': '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
     'mail': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
     'star': '<path d="M12 3.5l2.6 5.4 5.9.8-4.3 4.1 1 5.8L12 16.8l-5.2 2.8 1-5.8L3.5 9.7l5.9-.8z"/>',
     'route': '<circle cx="6" cy="18" r="2.5"/><circle cx="18" cy="6" r="2.5"/><path d="M8.5 18H15a3 3 0 0 0 0-6H9a3 3 0 0 1 0-6h6.5"/>',
     'hotel': '<path d="M3 20V7l9-4 9 4v13"/><path d="M9 20v-5h6v5M8 9h1M15 9h1M8 12h1M15 12h1"/>',
     'car': '<path d="M5 16h14v-4l-2-5H7l-2 5z"/><circle cx="8" cy="16.5" r="1.8"/><circle cx="16" cy="16.5" r="1.8"/><path d="M5 12h14"/>',
     'map': '<path d="M9 4L3 6v14l6-2 6 2 6-2V4l-6 2z"/><path d="M9 4v14M15 6v14"/>',
     'mount': '<path d="M2 20l7-12 4 6 3-4 6 10z"/><path d="M7.5 10.5l1.5 1.5 1.5-1.5"/>',
     'shield': '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
     'users': '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><circle cx="17" cy="9" r="2.5"/><path d="M16 14.2a5 5 0 0 1 5.5 5"/>',
     'clock': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
     'flag': '<path d="M5 21V4M5 4h11l-2 4 2 4H5"/>',
     'plane': '<path d="M2.5 13.5l7-1.5 5-7.5h2l-2.5 7.5 5.5-1 1.5-2h1.5l-1 4 1 4H20l-1.5-2-5.5-1 2.5 7.5h-2l-5-7.5-7-1.5z"/>',
     'temple': '<path d="M12 2v3M8 9l4-4 4 4M6 21V11h12v10M4 21h16M10 21v-5h4v5"/>',
     'handshake': '<path d="M3 11l4-4 4 2 3-2 4 1 3 3"/><path d="M7 7v6l4 4 2-1 2 2 2-1 2-3"/><path d="M11 17l-2 2"/>',
     'chart': '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
     'heart': '<path d="M12 20s-7-4.4-9-9a4.8 4.8 0 0 1 9-3 4.8 4.8 0 0 1 9 3c-2 4.6-9 9-9 9z"/>',
     'megaphone': '<path d="M3 10v4h3l7 4V6L6 10z"/><path d="M17 9a4 4 0 0 1 0 6M6 14l1.5 5h2.5l-1-4.5"/>',
     'rupee': '<path d="M7 5h10M7 9h10M8 5c5 0 5 8 0 8h-1l7 7"/>',
     'compass': '<circle cx="12" cy="12" r="9"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/>',
     'bolt': '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
     'doc': '<path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4M9 12h6M9 16h6"/>',
     'cal': '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
     'chat': '<path d="M4 5h16v11H9l-5 4z"/><path d="M8 9h8M8 12h5"/>',
     'idea': '<path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2.1h5c0-.9.4-1.6 1-2.1A6 6 0 0 0 12 3z"/>',
     'brief': '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5h6v2M3 12h18"/>',
     'swap': '<path d="M4 8h13l-3-3M20 16H7l3 3"/>',
     'cash': '<rect x="2" y="6" width="20" height="12" rx="2"/><circle cx="12" cy="12" r="2.5"/><path d="M6 10v4M18 10v4"/>',
     'eye': '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
     'globe': '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18"/>',
    }
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{P[name]}</svg>'

# ---------- map ----------
MAP = json.load(open('india-map.json'))
K = 36.0; C = math.cos(math.radians(23)); LON0 = 68.0; LAT0 = 37.3
def P(lon, lat): return ((lon - LON0) * C * K, (LAT0 - lat) * K)
STATE_COL = {
 'Jammu & Kashmir':'#7fc8c3','Ladakh':'#a9c6e8','Himachal Pradesh':'#f2b84b','Punjab':'#f6d58a','Haryana':'#9bd3a8','Delhi':'#e8738c','Chandigarh':'#e8738c','Uttarakhand':'#7cc6a0',
 'Rajasthan':'#f4a87c','Gujarat':'#ef8fa6','Dadra and Nagar Haveli and Daman and Diu':'#c99ae0','Maharashtra':'#a99be6','Goa':'#f0c35c',
 'Uttar Pradesh':'#f3c98a','Madhya Pradesh':'#9fd0e6','Chhattisgarh':'#b5dc8c','Bihar':'#e3a3c9','Jharkhand':'#f2b394','West Bengal':'#8fc2ee','Odisha':'#f5d17c',
 'Sikkim':'#ee8aa0','Assam':'#9ad7b4','Arunachal Pradesh':'#c3b2ee','Nagaland':'#f2a98a','Manipur':'#86cbd7','Mizoram':'#f3cf73','Tripura':'#ef9fbb','Meghalaya':'#f2c08c',
 'Telangana':'#f39a8f','Andhra Pradesh':'#8fd1c1','Karnataka':'#f7cc6b','Tamil Nadu':'#b7a3e8','Kerala':'#7fcf9a','Puducherry':'#e8738c','Lakshadweep':'#e07a5f','Andaman & Nicobar':'#e07a5f',
}
DEST_STATES = {'Himachal Pradesh','Jammu & Kashmir','Ladakh','Uttarakhand','Rajasthan','Goa','Kerala','Andaman & Nicobar','Uttar Pradesh','Delhi'}
PARTNERS = [('Delhi',40),('Chandigarh',30),('Mumbai',25),('Jaipur',20),('Bengaluru',20),('Kolkata',18),('Hyderabad',15),('Pune',15),('Lucknow',14),('Chennai',12),('Ahmedabad',12),('Amritsar',10)]
LABEL_DX = {'Chandigarh':(14,22),'Delhi':(14,6),'Amritsar':(-14,-10,'end'),'Mumbai':(-14,6,'end'),'Pune':(14,16),'Ahmedabad':(-14,6,'end'),'Jaipur':(-14,6,'end'),'Chennai':(14,6),'Bengaluru':(-14,6,'end'),'Kolkata':(14,6),'Hyderabad':(14,6),'Lucknow':(14,6)}
HQ = P(76.715886, 31.423784)
DESTS = [  # name, lon, lat, url, label dx, dy, anchor
 ('Srinagar',74.80,34.08,'/destination/kashmir-tour-packages/',-14,-6,'end'),
 ('Leh–Ladakh',77.58,34.15,'/destination/leh-ladakh-tour-packages/',14,-6,'start'),
 ('Spiti',78.07,32.23,'/destination/spiti-valley-tour-packages/',14,0,'start'),
 ('Manali',77.19,32.24,'/manali/',-6,-16,'end'),
 ('Dharamshala',76.32,32.22,'/destination/dharamshala-tour-packages/',-14,4,'end'),
 ('Shimla',77.17,31.10,'/shimla/',14,14,'start'),
 ('Char Dham',79.07,30.73,'/destination/chardham-tour-packages/',14,0,'start'),
 ('Nainital',79.46,29.38,'/uttarakhand/',14,8,'start'),
 ('Varanasi',83.01,25.32,'/pilgrimage-tours/',14,6,'start'),
 ('Rajasthan',73.71,24.58,'/rajasthan-tour-packages/',-14,6,'end'),
 ('Goa',73.83,15.49,'/goa-tour-packages/',-14,6,'end'),
 ('Kerala',77.06,10.09,'/kerala-tour-packages/',-14,6,'end'),
 ('Andaman',92.73,11.62,'/andaman/',-14,6,'end'),
]
def build_map():
    w, h = MAP['w'], MAP['h']
    s = [f'<svg viewBox="-10 -10 {w+20} {h+20}" role="img" aria-labelledby="abMapT abMapD"><title id="abMapT">Map of India showing Suzu Travels\' head office in Ghumarwin, Himachal Pradesh, and travel-agent partner cities</title><desc id="abMapD">Arcs run from the Ghumarwin head office to partner agents in Delhi, Chandigarh, Mumbai, Jaipur, Bengaluru, Kolkata, Hyderabad, Pune, Lucknow, Chennai, Ahmedabad and Amritsar.</desc>']
    s.append('<defs><linearGradient id="abArc" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#b8832e"/><stop offset="1" stop-color="#e2542f"/></linearGradient></defs>')
    s.append(f'<path class="ol" d="{MAP["outline"]}"/>')
    for n, v in MAP['states'].items():
        cls = 'st' + (' hp' if n == 'Himachal Pradesh' else '') + (' dz' if n in DEST_STATES else '')
        s.append(f'<path class="{cls}" fill="{STATE_COL.get(n,"#ddd")}" d="{v["d"]}"><title>{E(n)}</title></path>')
    # arcs
    hx, hy = HQ
    s.append('<g class="arcs">')
    for i, (c, n) in enumerate(PARTNERS):
        x, y = MAP['cities'][c]
        dx, dy = x - hx, y - hy; L = math.hypot(dx, dy)
        bend = 0.22 if L > 120 else 0.5
        cx, cy = (hx + x) / 2 - dy * bend, (hy + y) / 2 + dx * bend
        s.append(f'<path class="arc" d="M{hx:.0f} {hy:.0f}Q{cx:.0f} {cy:.0f} {x} {y}" stroke-width="{1.6 + n/14:.1f}" style="animation-delay:0s,{.15*i:.2f}s"/>')
    s.append('</g><g class="cts">')
    for i, (c, n) in enumerate(PARTNERS):
        x, y = MAP['cities'][c]; r = 5 + n / 8
        d = LABEL_DX.get(c, (14, 6)); anchor = d[2] if len(d) > 2 else 'start'
        s.append(f'<g class="ct" data-c="{c}"><circle class="p" cx="{x}" cy="{y}" r="{r:.1f}" style="animation-delay:{.2*i:.1f}s"/><circle class="c" cx="{x}" cy="{y}" r="{r:.1f}"/><text x="{x+d[0]}" y="{y+d[1]}" text-anchor="{anchor}">{c} <tspan>{n}+</tspan></text></g>')
    s.append('</g><g class="dss">')
    for name, lon, lat, url, dx, dy, an in DESTS:
        x, y = P(lon, lat)
        s.append(f'<g class="ds"><a href="https://suzutravels.com{url}"><circle cx="{x:.0f}" cy="{y:.0f}" r="8"/><text x="{x+dx:.0f}" y="{y+dy:.0f}" text-anchor="{an}">{E(name)}</text></a></g>')
    s.append('</g>')
    s.append(f'<g class="hq"><circle class="p" cx="{hx:.0f}" cy="{hy:.0f}" r="13"/><circle class="h" cx="{hx:.0f}" cy="{hy:.0f}" r="11"/><rect x="{hx+20:.0f}" y="{hy-62:.0f}" rx="10" width="208" height="38"/><text x="{hx+34:.0f}" y="{hy-37:.0f}">★ Suzu HQ · Ghumarwin</text><path d="M{hx+30:.0f} {hy-24:.0f}L{hx+8:.0f} {hy-8:.0f}" stroke="#0b1f33" stroke-width="2.5"/></g>')
    s.append('</svg>')
    return ''.join(s)

# ---------- content blocks ----------
def hero():
    stats = [('7','+','Years in travel · since 2019'),('5,000','+','Happy travellers'),('200','+','Travel-agent partners'),('50','+','Destinations across India'),(RATING,'★',f'Google rating · {COUNT} reviews')]
    st = ''.join(f'<div class="ab-st" style="--i:{i}"><b><span{" data-ab-rating" if t=="★" else ""}>{n}</span><i>{t}</i></b><span{" data-ab-count" if t=="★" else ""}>{E(l)}</span></div>' for i,(n,t,l) in enumerate(stats))
    return (f'<section class="ab-hero ab-bars" id="top" aria-label="Suzu Travels — about us">'
     f'<video class="ab-hv" autoplay muted loop playsinline preload="metadata" poster="{MED("about-hero-poster.webp")}" aria-hidden="true"><source src="{MED("about-hero-m.mp4")}" type="video/mp4" media="(max-width: 700px)"><source src="{MED("about-hero.mp4")}" type="video/mp4"></video>'
     '<div class="ab-shade"></div>'
     '<p class="kick ab-hk">Since 2019 · Ghumarwin<span class="xl">, Himachal Pradesh</span></p>'
     '<div class="ab-hb"><p class="ab-tag">Born in the Himalaya. Trusted across India.</p>'
     '<p class="ab-sub">We are a Himachal-based travel agency and destination management company (DMC). Our own team plans, books and runs trips from Kashmir to Kanyakumari — for families, couples, pilgrims, adventure seekers and more than 200 travel-agent partners.</p>'
     f'<div class="ab-cta"><a class="btn btn-gold" href="{WA}" target="_blank" rel="noopener">{ic("wa")}Plan my trip with Suzu</a><a class="btn btn-ghost" href="#crew">Meet the crew {ic("down")}</a></div></div>'
     f'<div class="ab-stats">{st}</div><div class="ab-scroll" aria-hidden="true">Scroll</div></section>')

def nav():
    items = [('story','Our story'),('journey','Journey'),('crew','The crew'),('network','India network'),('departments','Departments'),('partners','B2B partners'),('reviews','Reviews'),('faq','FAQ')]
    a = ''.join(f'<a href="#{i}"><span>{n:02d}</span>{t}</a>' for n,(i,t) in enumerate(items,1))
    return f'<nav class="ab-nav" aria-label="About page sections"><div class="wrap">{a}<a class="go" href="{WA}" target="_blank" rel="noopener">Plan a trip →</a></div></nav>'

def story():
    pills = [('route','No middlemen'),('hotel','Direct hotel inventory'),('car','Own taxi fleet'),('compass','Local guides'),('clock','24/7 on-trip support')]
    p = ''.join(f'<li>{ic(i)}{t}</li>' for i,t in pills)
    facts = [
     ('Who we are','Suzu Travels — travel agency &amp; DMC (destination management company). Tagline: <em>DMC of India</em>.'),
     ('Founded','2019 in Ghumarwin, Himachal Pradesh · GST-registered since January 2021 (GSTIN 02BLPPK1401E1ZR)'),
     ('Licence','Registered Travel Agent with HP Tourism — Reg. No. DTO-MND-11-243/2022, valid to December 2028 · <a href="https://suzutravels.com/certificates/">see the certificates</a>'),
     ('Head office','NH-103 Roadside, Kulahru, Ghumarwin, District Bilaspur, Himachal Pradesh 174021'),
     ('We serve','Families, couples, groups and pilgrims (B2C) and travel agents across India (B2B)'),
     ('Open','Every day, 9 am – 8 pm · on-trip support around the clock'),
     ('Talk to us',f'<a href="{TEL}">{PHONE}</a> · <a href="mailto:info@suzutravels.com">info@suzutravels.com</a>'),
    ]
    dl = ''.join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k,v in facts)
    return ('<section class="sec ab-story" id="story"><div class="wrap ab-answer"><div class="rv">'
     '<p class="kick">Our story</p><h2 class="h2">Born in the mountains of <em>Himachal</em></h2>'
     '<p class="ab-q">Who is Suzu Travels?</p>'
     '<p class="ab-a">Suzu Travels is a Himachal-based travel agency and destination management company (DMC), founded in 2019 in Ghumarwin, District Bilaspur, and registered with HP Tourism (Reg. No. DTO-MND-11-243/2022). It plans and runs complete tours — hotels, cabs, sightseeing and meals — across Himachal and the rest of India, for travellers and for travel-agent partners.</p>'
     '<div class="ab-prose"><p>We are not an aggregator sitting in a city office. We live in Himachal. We know the roads, the hotels, the passes and the seasons — when Rohtang opens, which Spiti road is shut by snow, which hotel in Manali has the view you were promised. That local knowledge is what makes a Suzu itinerary work on the ground, not just on paper.</p>'
     '<p>From one desk in Ghumarwin we have grown into a full-service team with departments for sales, reservations, operations, marketing, accounts and customer experience. Himachal is still our home ground; today our planners also run trips to Kashmir, Ladakh, Uttarakhand, Rajasthan, Goa, Kerala, the Andamans and India\'s great pilgrimages.</p></div>'
     '<blockquote class="ab-quote">Every traveller should get a genuine, safe and unforgettable experience of the Himalayas and of India.<cite>— Our mission since day one</cite></blockquote>'
     f'</div><aside class="ab-file rv-s" aria-label="Suzu Travels fact file"><h3>Fact file</h3><dl>{dl}</dl></aside></div>'
     f'<div class="wrap"><ul class="ab-pills rv">{p}</ul></div></section>')

def journey():
    F = [
     ('2019','flag','Founded in Ghumarwin','Suzu Travels opens in Ghumarwin, District Bilaspur — Himachal trips planned by people who live in Himachal.'),
     ('2021','mount','Kashmir &amp; Ladakh, officially','GST registration in January 2021, and the first Kashmir and Ladakh packages join our Himachal tours.'),
     ('2022','shield','Registered with HP Tourism','Registered Travel Agent with the Department of Tourism, Government of Himachal Pradesh — Reg. No. DTO-MND-11-243/2022.'),
     ('2023','car','Our own taxi fleet','Innova, Tempo Traveller and SUVs on our own roster, so ground transport is in our hands, not a stranger\'s.'),
     ('2024','handshake','200+ agent partners','Travel agents from Delhi to Chennai start sending us their Himachal, Kashmir and Ladakh guests.'),
     ('2025','users','5,000+ travellers','We cross 5,000 happy travellers, and our HP Tourism registration is renewed until 2028.'),
     ('2026','globe','Pan-India and beyond','Kerala, Goa, Rajasthan and the Andamans, new pilgrimage, mountaineering and adventure guides — and holidays abroad.'),
    ]
    fr = ''.join(f'<li class="ab-fr{" now" if y=="2026" else ""}"><span class="ab-ic">{ic(i)}</span><p class="ab-yr">{y}</p>{"<span class=ab-tagnow>Now</span>" if y=="2026" else ""}<h3>{t}</h3><p>{d}</p></li>' for y,i,t,d in F)
    return ('<section class="sec dark ab-journey" id="journey"><div class="wrap rv"><p class="kick">Our journey</p><h2 class="h2">Seven years, <em>one road</em></h2>'
     '<p class="lead">From a single office on the Shimla–Dharamshala highway to a team that plans trips across India. Swipe through the reel.</p></div>'
     f'<div class="ab-strip"><ol class="ab-track" aria-label="Suzu Travels timeline, 2019 to 2026">{fr}</ol><div class="ab-rail"><i></i></div></div>'
     f'<div class="wrap"><p class="ab-hint">{ic("swap")} Drag or swipe the film strip</p></div></section>')

def card(m, big=False):
    g = m['grp'] + (' ' + m['squad'].lower() if m.get('squad') else '')
    tags = ''.join(f'<li class="x">{E(l)}</li>' for l in m['langs'])
    for k in ('exp','edu','since'):
        if m.get(k): tags += f'<li>{E(("Since " if k=="since" else "")+m[k])}</li>'
    mail = f'<a href="mailto:{m["email"]}">{E(m["email"])}</a>' + (f'<a href="tel:{m["phone"].replace(" ","")}">{E(m["phone"])}</a>' if m.get('phone') else '')
    name = (m.get('hon','') + ' ' + m['name']).strip()
    sq = f'<span class="ab-sq {m["squad"].lower()}">Team {m["squad"]}</span>' if m.get('squad') else ''
    alt = f'{name}, {m["role"]} at Suzu Travels'
    if big:
        return (f'<article class="ab-card big rv" data-g="{g}" itemscope itemtype="https://schema.org/Person"><div class="ab-ph"><img src="{IMG(m["slug"])}" alt="{E(alt)}" width="640" height="800" loading="lazy" decoding="async" itemprop="image"></div>'
         f'<div class="ab-cb"><p class="rk">Leadership</p><h3 itemprop="name">{E(name)}</h3><p class="rl" itemprop="jobTitle">{E(m["role"])}</p><p class="ab-focus">{E(m["focus"])}</p><p class="bio" itemprop="description">{E(m["bio"])}</p><ul class="ab-tags">{tags}</ul><p class="ab-mail">{mail}</p></div></article>')
    return (f'<article class="ab-card rv" data-g="{g}" itemscope itemtype="https://schema.org/Person"><div class="ab-ph">{sq}<img src="{IMG(m["slug"])}" alt="{E(alt)}" width="640" height="800" loading="lazy" decoding="async" itemprop="image"><div class="nm"><h3 itemprop="name">{E(name)}</h3><p itemprop="jobTitle">{E(m["role"])}</p></div></div>'
     f'<div class="ab-cb"><p class="ab-focus">{E(m["focus"])}</p><ul class="ab-tags">{tags}</ul><details><summary>Read bio</summary><p itemprop="description">{E(m["bio"])}</p></details><p class="ab-mail">{mail}</p></div></article>')

def crew():
    cnt = lambda f: sum(1 for m in TEAM if f(m))
    F = [('all','Everyone',len(TEAM)),('lead','Leadership',cnt(lambda m:m['grp']=='lead')),('mgmt','Management',cnt(lambda m:m['grp']=='mgmt')),('sales','Travel experts',cnt(lambda m:m['grp']=='sales')),('ops','Reservations',cnt(lambda m:m['grp']=='ops')),('digital','Digital',cnt(lambda m:m['grp']=='digital')),
         ('pathfinder','Team Pathfinder',cnt(lambda m:m.get('squad')=='Pathfinder')),('autopilot','Team AutoPilot',cnt(lambda m:m.get('squad')=='AutoPilot')),('phoenix','Team Phoenix',cnt(lambda m:m.get('squad')=='Phoenix'))]
    fl = ''.join(f'<input type="radio" name="abf" id="abf-{k}"{" checked" if k=="all" else ""}><label for="abf-{k}">{t}<b>{n}</b></label>' for k,t,n in F)
    lead = ''.join(card(m, True) for m in TEAM if m['grp']=='lead')
    rest = ''.join(card(m) for m in TEAM if m['grp']!='lead')
    sq = [('Pathfinder','First contact and reservations — they find the right trip and set up B2B bookings.'),('AutoPilot','Destination planners who build and run itineraries end to end, from Kashmir to Kanyakumari.'),('Phoenix','Senior sales strategy — personalised trips for travellers who want every detail just right.')]
    sqh = ''.join(f'<div class="ab-squad rv"><b>Team {n}</b><p>{t}</p></div>' for n,t in sq)
    return ('<section class="sec ab-crew" id="crew"><div class="wrap"><div class="rv"><p class="kick">The crew</p><h2 class="h2">Meet the people who <em>plan your trip</em></h2>'
     f'<p class="lead">{len(TEAM)} people across sales, reservations, operations, marketing and finance — most of them from Himachal, many with a master\'s degree in tourism. When you call Suzu, one of them answers.</p></div>'
     f'<figure class="ab-film rv-s"><video id="abCrewFilm" muted playsinline loop controls preload="none" poster="{MED("about-crew-poster.webp")}" aria-label="Opening credits film introducing the Suzu Travels team"><source src="{MED("about-crew-m.mp4")}" type="video/mp4" media="(max-width: 700px)"><source src="{MED("about-crew.mp4")}" type="video/mp4"></video><figcaption>▶ The Crew · 27 s</figcaption></figure>'
     f'<div class="ab-filters" role="group" aria-label="Filter the team">{fl}</div>'
     f'<div class="ab-lead">{lead}</div><div class="ab-grid">{rest}<div class="ab-join rv"><b>Your planner is one message away</b><p>Tell us where and when — the right person from this team replies within 30 minutes.</p><a class="btn btn-gold" href="{WA}" target="_blank" rel="noopener">{ic("wa")}WhatsApp the team</a></div></div><div class="ab-squads">{sqh}</div></div></section>')

def network():
    mx = max(n for _,n in PARTNERS)
    bars = ''.join(f'<li data-c="{c}"><span>{c}</span><span class="bar"><i style="--w:{n/mx*100:.0f}%"></i></span><b>{n}+</b></li>' for c,n in PARTNERS)
    dests = ''.join(f'<a href="https://suzutravels.com{u}">{E(n)}</a>' for n,_,_,u,*_ in DESTS)
    return ('<section class="sec ab-net" id="network"><div class="wrap"><div class="rv"><p class="kick">India network</p><h2 class="h2">From a Himachal HQ to <em>every corner of India</em></h2>'
     '<p class="lead">Our head office is in Ghumarwin. Our partners are travel agents in 12+ cities who trust us with their guests — and our travellers go from Ladakh to the Andamans.</p>'
     '<div class="ab-modes" role="group" aria-label="Map view"><input type="radio" name="abm" id="abm-agents" checked><label for="abm-agents">Agent network</label><input type="radio" name="abm" id="abm-trips"><label for="abm-trips">Where we travel</label></div></div>'
     f'<div class="ab-mapwrap"><div class="ab-map rv-s">{build_map()}</div>'
     '<div class="ab-panel"><div class="ab-panel-agents"><h3>200+ authorised travel agents</h3><p>Active B2B partners by city. Arcs show where bookings come from — every one of them is handled from our Himachal office.</p>'
     f'<ul class="ab-bars2">{bars}</ul><div class="ab-kpis"><div><b>200+</b><span>agent partners</span></div><div><b>12+</b><span>partner cities</span></div><div><b>~2 h</b><span>to confirm hotels &amp; cabs</span></div></div></div>'
     '<div class="ab-panel-trips"><h3>Where we take travellers</h3><p>Himachal is our home ground. These are the regions our planners run every season — tap one to see the trips.</p>'
     f'<div class="ab-dests">{dests}</div><div class="ab-kpis"><div><b>50+</b><span>destinations</span></div><div><b>5,000+</b><span>travellers hosted</span></div><div><b>24/7</b><span>on-trip support</span></div></div></div>'
     '<p class="ab-mapnote">Map shows the official boundary of India. Boundary data: <a href="https://github.com/datameet/maps" rel="nofollow noopener" target="_blank">DataMeet India community</a> (CC BY 4.0 / CC0). Partner counts are approximate.</p></div></div></div></section>')

def departments():
    D = [
     ('chat','Sales &amp; Enquiry','We answer enquiries from travellers and agents within 30 minutes on WhatsApp, phone and email — every day.',['Enquiry handling','Custom itineraries','Package pricing &amp; quotes','Group bookings'],'sales@suzutravels.com'),
     ('hotel','Reservations','Hotels, vehicles, activities and vouchers. Every booking is double-confirmed before you travel.',['Hotel reservations across India','Cab allocation','Activity bookings','Vouchers &amp; changes'],'reservation@suzutravels.com'),
     ('route','Tour Operations','The ground team that makes the plan happen — drivers, guides, check-ins and emergencies.',['Driver &amp; guide coordination','24/7 on-trip support','Emergency handling','Quality checks at every stop'],'operations@suzutravels.com'),
     ('megaphone','Marketing &amp; Digital','Instagram, YouTube, Google and this website — the content that inspires your next trip.',['Social media','Google Ads &amp; SEO','Content creation','Email campaigns'],'marketing@suzutravels.com'),
     ('handshake','B2B &amp; Travel Agents','Net rates, quick confirmations and a dedicated desk for our agent partners.',['Agent onboarding','Net-rate quotations','White-label itineraries','Priority booking support'],'b2b@suzutravels.com'),
     ('rupee','Accounts &amp; Finance','Payments, GST invoices, refunds and commissions — fully transparent.',['Invoices &amp; GST billing','Payment collection','Refund processing','Agent payouts'],'accounts@suzutravels.com'),
     ('heart','Customer Experience','After the trip we follow up, listen and fix — and look after repeat travellers.',['Post-trip feedback','Complaint resolution','Review management','Repeat-traveller benefits'],'feedback@suzutravels.com'),
     ('compass','Management','Strategy, partnerships and quality — the standards every department works to.',['Strategic planning','Hotel &amp; partner negotiations','Quality assurance','Policy &amp; compliance'],'info@suzutravels.com'),
    ]
    c = ''.join(f'<article class="ab-dep rv" style="animation-delay:{.05*i:.2f}s"><span class="ix">{i+1:02d}</span><span class="ic">{ic(icn)}</span><h3>{t}</h3><p>{d}</p><ul>{"".join(f"<li>{x}</li>" for x in L)}</ul><a class="em" href="mailto:{em}">{em}</a></article>' for i,(icn,t,d,L,em) in enumerate(D))
    return ('<section class="sec dark" id="departments"><div class="wrap"><div class="rv"><p class="kick">How we are organised</p><h2 class="h2">Eight departments, <em>one trip</em></h2>'
     '<p class="lead">Every stage of your trip has an owner — so the person answering your question is the person who can fix it.</p></div>'
     f'<div class="ab-deps">{c}</div></div></section>')

def partners():
    B = [('rupee','Competitive net rates','Net B2B rates in Himachal — add your margin and sell with confidence.'),('bolt','Fast confirmations','Hotel and vehicle confirmations within about 2 hours of a booking request.'),
         ('doc','White-label itineraries','Itineraries in your agency\'s branding, ready to send to your client.'),('users','A dedicated B2B manager','One point of contact for bookings, changes and support.'),
         ('cash','Flexible payment terms','Credit facility for established agent partners.'),('eye','Real-time availability','Check hotel and cab availability on WhatsApp or email.')]
    b = ''.join(f'<div class="ab-ben rv">{ic(i)}<h3>{t}</h3><p>{d}</p></div>' for i,t,d in B)
    return ('<section class="sec" id="partners" style="background:var(--paper)"><div class="wrap ab-part"><div class="rv"><p class="kick">B2B partner network</p><h2 class="h2">Travel agents: <em>we are your team on the ground</em></h2>'
     '<p class="lead">More than 200 agents across India hand us their Himachal, Kashmir, Ladakh and Uttarakhand guests. You keep the client; we run the trip as if it were our own.</p>'
     f'<div class="ab-cta" style="animation:none"><a class="btn btn-gold" href="{WA_B2B}" target="_blank" rel="noopener">{ic("handshake")}Become a B2B partner</a><a class="btn btn-line" href="mailto:b2b@suzutravels.com">{ic("mail")}b2b@suzutravels.com</a></div>'
     '<div class="ab-dmc"><a href="https://suzutravels.com/best-dmc-for-himachal-pradesh/">Himachal DMC</a><a href="https://suzutravels.com/kashmir-dmc/">Kashmir DMC</a><a href="https://suzutravels.com/uttarakhand-dmc/">Uttarakhand DMC</a></div></div>'
     f'<div class="ab-bens">{b}</div></div></section>')

def reviews():
    team_names = {m['name'].lower() for m in TEAM}
    rs = [r for r in REV['reviews'] if r.get('text') and r['author'].lower() not in team_names][:8]
    def rc(r):
        t = r['text'].strip(); t = (t[:300].rsplit(' ',1)[0] + '…') if len(t) > 300 else t
        ini = ''.join(w[0] for w in r['author'].split()[:2]).upper()
        return f'<article class="ab-rc"><div class="who"><span class="av" aria-hidden="true">{E(ini)}</span><div><b>{E(r["author"].title())}</b><div class="s" aria-label="{r["rating"]} out of 5 stars">{"★"*int(r["rating"])}</div></div></div><p>{E(t)}</p></article>'
    cards = ''.join(rc(r) for r in rs)
    return ('<section class="sec ab-rev" id="reviews"><div class="wrap"><div class="ab-rhead rv"><div><p class="kick">In travellers\' words</p><h2 class="h2">Trusted by <em>thousands of travellers</em></h2></div>'
     f'<div class="ab-score"><b data-ab-rating>{RATING}</b><div><div class="stars" aria-hidden="true">★★★★★</div><span>Google rating · <span data-ab-count2>{COUNT}</span> reviews</span></div></div></div></div>'
     f'<div class="ab-rv" aria-label="Recent Google reviews"><div class="ab-rvt">{cards}<div style="display:contents" aria-hidden="true">{cards}</div></div></div>'
     f'<div class="wrap ab-rlinks"><a class="btn btn-line" href="{REV["maps_url"]}" target="_blank" rel="noopener">{ic("star")}Read all reviews on Google</a><a class="btn btn-gold" href="{REV["write_url"]}" target="_blank" rel="noopener">{ic("heart")}Write a review</a><span class="ab-src">Reviews and ratings: Google.</span></div></section>')

def feedback():
    F = [('chat','File a complaint','Had an issue during your trip? Tell us exactly what happened — we resolve complaints within 24 hours.','mailto:feedback@suzutravels.com','feedback@suzutravels.com'),
         ('idea','Share a suggestion','Have an idea to make our service better? We genuinely welcome feedback from travellers and partners.','mailto:feedback@suzutravels.com','feedback@suzutravels.com'),
         ('star','Leave a review','Had a great trip? Your Google review helps other travellers choose us — and makes our team\'s day.',REV['write_url'],'Write a Google review →'),
         ('brief','Business enquiry','List your hotel, partner with us or become an authorised travel agent.','mailto:b2b@suzutravels.com','b2b@suzutravels.com')]
    c = ''.join(f'<div class="ab-fbc rv"><span class="ic">{ic(i)}</span><h3>{t}</h3><p>{d}</p><a href="{u}"{" target=_blank rel=noopener" if u.startswith("http") else ""}>{l}</a></div>' for i,t,d,u,l in F)
    return ('<section class="sec" id="feedback" style="background:var(--paper)"><div class="wrap"><div class="rv"><p class="kick">We listen</p><h2 class="h2">Complaints, suggestions <em>&amp; feedback</em></h2>'
     '<p class="lead">Your experience matters more than anything. If something went wrong, or you have an idea, we want to hear it — and we will act on it.</p></div>'
     f'<div class="ab-fb">{c}</div></div></section>')

FAQ = [
 ('Who owns Suzu Travels?','Suzu Travels is owned and run by Sushil Kumar, its Managing Director, who leads sales, marketing and business growth. Sujata Rai is Director of Finance &amp; Operations. The business is registered for GST (GSTIN 02BLPPK1401E1ZR) as a proprietorship of Sushil Kumar.'),
 ('Is Suzu Travels a registered and genuine travel agency?','Yes. Suzu Travels is a registered Travel Agent with the Department of Tourism &amp; Civil Aviation, Government of Himachal Pradesh — Reg. No. DTO-MND-11-243/2022, valid to December 2028 — and has been GST-registered since January 2021. You can see both on our <a href="https://suzutravels.com/certificates/">certificates page</a>. Travellers rate us ' + RATING + '★ on Google from ' + str(COUNT) + ' reviews.'),
 ('Where is the Suzu Travels office?','Our head office is on NH-103 Roadside, Kulahru, Ghumarwin, District Bilaspur, Himachal Pradesh 174021 — on the Shimla–Dharamshala highway. It is open every day from 9 am to 8 pm, and on-trip support runs around the clock on ' + PHONE + '.'),
 ('What is a DMC, and what does Suzu Travels do?','A DMC (destination management company) is a local company that plans and runs everything on the ground — hotels, cabs, sightseeing, guides, permits and activities. Suzu Travels does this for travellers who book with us directly and for travel agents who send us their guests.'),
 ('Which destinations does Suzu Travels cover?','Himachal Pradesh is our home ground — Shimla, Manali, Spiti, Dharamshala, Dalhousie and beyond. We also run trips to Kashmir, Ladakh, Uttarakhand and the Char Dham, Rajasthan, Goa, Kerala, the Andamans and India\'s major pilgrimages, plus <a href="https://suzutravels.com/international-tour-packages/">holidays abroad</a>.'),
 ('How do I book a trip, and how do payments work?','Tell us your dates and plans on WhatsApp, phone or email and a planner sends you an itinerary with hotels named. A small token advance confirms the booking and locks today\'s rate; the balance is paid before the trip starts. You can pay online (Razorpay), by bank transfer or by UPI. The advance is non-refundable, but you can move your travel date once, to any date within six months.'),
 ('Can travel agents work with Suzu Travels?','Yes. More than 200 travel agents across India work with us for net rates, confirmations within about two hours, white-label itineraries, a dedicated B2B manager and credit terms for established partners. Write to b2b@suzutravels.com or WhatsApp ' + PHONE + '.'),
 ('Which languages does the Suzu team speak?','Our planners speak Hindi and English, and Sujata Rai and Shashi Rai also speak Nepali. Shashi Rai is the single point of contact for travellers from Nepal planning an India tour.'),
 ('How quickly will Suzu Travels reply to me?','Our sales team replies to enquiries within 30 minutes on WhatsApp, phone and email, every day. Complaints are resolved within 24 hours.'),
]
def faq():
    q = ''.join(f'<details{" open" if i==0 else ""}><summary>{E(a)}</summary><p>{b}</p></details>' for i,(a,b) in enumerate(FAQ))
    return ('<section class="sec" id="faq" style="background:var(--cream)"><div class="wrap ab-faq"><div class="rv"><p class="kick">Good to know</p><h2 class="h2">Questions people ask <em>about us</em></h2>'
     f'<p class="lead">Straight answers about who we are, how we work and how to reach us. Anything else? <a href="{WA}" target="_blank" rel="noopener" style="color:#a8711c;border-bottom:1px dotted">Ask on WhatsApp</a>.</p></div>'
     f'<div>{q}</div></div></section>')

def ending():
    return (f'<section class="sec ab-end" id="plan"><img class="bg" src="{MED("about-hero-poster.webp")}" alt="" loading="lazy" decoding="async"><div class="wrap rv"><p class="kick">Your story next</p><h2 class="h2">Ready to write your own <em>Suzu chapter?</em></h2>'
     '<p class="lead">A free consultation and a personalised itinerary with hotels named — from the team you just met.</p>'
     f'<div class="ab-cta"><a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener">{ic("wa")}WhatsApp us</a><a class="btn btn-gold" href="{TEL}">{ic("phone")}Call {PHONE}</a><a class="btn btn-ghost" href="https://suzutravels.com/contact/">{ic("mail")}Contact page</a></div>'
     '<p class="ab-trust"><a href="https://suzutravels.com/certificates/">HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022</a><span>GST registered</span><span>' + RATING + '★ Google</span><a href="https://suzutravels.com/packages/">Browse tour packages</a><a href="https://suzutravels.com/cabs/">Book a cab</a></p></div></section>')

# ---------- schema ----------
def schema():
    url = 'https://suzutravels.com/about-suzu-travels/'
    org = 'https://suzutravels.com/#organization'
    people = []
    for m in TEAM:
        p = {'@type':'Person','@id':f'{url}#{m["slug"]}','name':m['name'],'jobTitle':m['role'],'image':(CFG['images'].get(m['slug']) if not PREVIEW else None),'worksFor':{'@id':org},'knowsLanguage':m['langs']}
        if not p['image']: del p['image']
        people.append(p)
    g = {'@context':'https://schema.org','@graph':[
      {'@type':'AboutPage','@id':url+'#aboutpage','url':url,'name':'About Suzu Travels','inLanguage':'en-IN','isPartOf':{'@id':'https://suzutravels.com/#website'},'about':{'@id':org},'mainEntity':{'@id':org},
       'primaryImageOfPage':CFG['cdn']+'/media/about-hero-poster.webp','dateModified':'2026-10-14'},
      {'@type':['TravelAgency','Organization'],'@id':org,'name':'Suzu Travels','alternateName':'Suzu Travels – DMC of India','slogan':'DMC of India','url':'https://suzutravels.com','telephone':'+917087488961','email':'info@suzutravels.com',
       'foundingDate':'2019','foundingLocation':{'@type':'Place','name':'Ghumarwin, Himachal Pradesh, India'},
       'founder':{'@id':url+'#sushil-kumar'},'numberOfEmployees':{'@type':'QuantitativeValue','value':len(TEAM)},
       'address':{'@type':'PostalAddress','streetAddress':'NH-103 Roadside, Kulahru','addressLocality':'Ghumarwin','addressRegion':'Himachal Pradesh','postalCode':'174021','addressCountry':'IN'},
       'geo':{'@type':'GeoCoordinates','latitude':31.423784,'longitude':76.715886},
       'areaServed':[{'@type':'Country','name':'India'}],'knowsLanguage':['Hindi','English','Nepali'],'taxID':'02BLPPK1401E1ZR',
       'hasCredential':{'@type':'EducationalOccupationalCredential','credentialCategory':'Travel Agent registration','name':'Registration of Travel Agent, Department of Tourism & Civil Aviation, Government of Himachal Pradesh — Reg. No. DTO-MND-11-243/2022','recognizedBy':{'@type':'GovernmentOrganization','name':'Department of Tourism & Civil Aviation, Government of Himachal Pradesh'}},
       'employee':[{'@id':p['@id']} for p in people],
       'sameAs':['https://www.facebook.com/suzutravels','https://www.instagram.com/suzutravels/','https://www.youtube.com/channel/UCXJG81FqAOrT3tm18ka3yaA']},
      *people,
      {'@type':'FAQPage','@id':url+'#faq','mainEntity':[{'@type':'Question','name':a,'acceptedAnswer':{'@type':'Answer','text':re.sub(r'<[^>]+>','',b).replace('&amp;','&')}} for a,b in FAQ]},
      {'@type':'VideoObject','name':'Suzu Travels — The Crew','description':'Opening-credits film introducing the 13 people of the Suzu Travels team, from the Managing Director to reservations and digital.','thumbnailUrl':CFG['cdn']+'/media/about-crew-poster.webp','contentUrl':CFG['cdn']+'/media/about-crew.mp4','uploadDate':'2026-10-14T00:00:00+05:30','duration':'PT27S'},
    ]}
    return '<script type="application/ld+json">' + json.dumps(g, ensure_ascii=False, separators=(',',':')) + '</script>'

JS = open('about.js').read()
css = open('about.css').read().replace('{CDN}', CDN)
body = ''.join([hero(), nav(), story(), journey(), crew(), network(), departments(), partners(), reviews(), feedback(), faq(), ending()])
page = f'<div class="szab" id="szab"><style id="szab-css">{css}</style>{body}{schema()}<script id="szab-js" nowprocket>{JS}</script></div>'
os.makedirs('out', exist_ok=True)
open('out/about.html', 'w').write(page)

def minify(h):
    # css: strip comments/whitespace; html: collapse whitespace between tags; one line
    def mcss(m):
        c = m.group(2)
        c = re.sub(r'/\*.*?\*/', '', c, flags=re.S)
        c = re.sub(r'\s+', ' ', c)
        c = re.sub(r'\s*([{};,>])\s*', r'\1', c)
        c = c.replace(';}', '}')
        return m.group(1) + c + '</style>'
    h = re.sub(r'(<style[^>]*>)(.*?)</style>', mcss, h, flags=re.S)
    def mjs(m):
        j = m.group(2)
        j = re.sub(r'^\s*//.*$', '', j, flags=re.M)
        j = re.sub(r'\s*\n\s*', '\n', j).strip().replace('\n', ' ')
        return m.group(1) + j + '</script>'
    h = re.sub(r'(<script id="szab-js"[^>]*>)(.*?)</script>', mjs, h, flags=re.S)
    h = re.sub(r'>\s+<', '><', h)
    h = h.replace('\n', ' ')
    return h
mn = minify(page)
open('out/about.min.html', 'w').write(mn)
# quality gate
assert '\n' not in mn
assert not re.search(r'[₹]\s?\d|Rs\.?\s?\d', mn), 'price found'
assert 'registered DMC' not in mn
assert '4★ and above' not in mn and 'only 4' not in mn
assert mn.count('<h1') == 0, 'content must not contain an H1 (theme prints it)'
print('ok', len(mn), 'bytes')
