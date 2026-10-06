#!/usr/bin/env python3
"""Generate the /adventure/ hub (page 11529) source HTML -> adventure.html, then build with ../build.py.
Built by Claude on 29 Sep 2026. Facts: claude/adventure-research-baseline.md (HP rules, seasons, spots).
NO prices, NO operator names. Every activity card has a unique id (act-<slug>) and a unique WhatsApp link,
so the Page Builder can switch one card to "Explore →" with a single targeted replace when its page goes live."""
import html, os, re
from urllib.parse import quote

U = 'https://suzutravels.com'
WA = 'https://wa.me/917087488961?text='
MEDIA = U + '/wp-content/uploads/2026/09/'
CDN = 'https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@f78b1e54ab94954a543918c767a24419733b56ba/adventure-kit/media/adventure-hub/'
REG = 'DTO-MND-11-243/2022'


def slug(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


def wa(activity, place=''):
    where = f' in {place}' if place else ''
    return WA + quote(f'Hi Suzu Travels, I want a quote for {activity}{where}. Travel date: ___ , people: ___ (page: adventure)')


def e(s):
    return html.escape(s, quote=False)


# icon paths (24px, stroke)
IC = {
    'air': '<path d="M3 10c3-5 15-5 18 0"/><path d="M3 10l9 7 9-7"/><path d="M12 17v4"/>',
    'water': '<path d="M2 15c2.5 0 2.5-2 5-2s2.5 2 5 2 2.5-2 5-2 2.5 2 5 2"/><path d="M2 19c2.5 0 2.5-2 5-2s2.5 2 5 2 2.5-2 5-2 2.5 2 5 2"/><path d="M8 10l4-6 4 6"/>',
    'snow': '<path d="M12 2v20M4.9 6.5l14.2 11M19.1 6.5L4.9 17.5"/><path d="M9 4l3 3 3-3M9 20l3-3 3 3"/>',
    'land': '<circle cx="6" cy="17" r="3"/><circle cx="18" cy="17" r="3"/><path d="M6 17l4-7h5l3 7M10 10l-1-3h3"/>',
    'treks': '<path d="M3 20l7-12 4 6 2-3 5 9z"/><path d="M10 8V4l3 1-3 1"/>',
    'ropeways': '<path d="M2 5l20-2"/><path d="M12 4v4"/><rect x="7" y="8" width="10" height="9" rx="2"/><path d="M7 12h10"/>',
    'services': '<rect x="5" y="7" width="14" height="14" rx="3"/><path d="M9 7V5a3 3 0 0 1 6 0v2M9 13h6"/>',
    'dest': '<path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>',
}


def icon(k, cls='ic'):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{IC[k]}</svg>')


# (id, nav label, kicker, h2, lead, image file, image alt, [ (name, where, season, line, badge|None, wa_place) ])
CATS = [
    ('air', 'Air', 'Fly', 'Air: paragliding, bungee and zipline',
     'Himachal has some of the best flying in Asia. Tandem pilots take first-timers up at registered sites, and every flight depends on the day’s weather.',
     'paragliding-over-mountains-768x549.webp', 'Tandem paraglider with an orange wing over a mountain valley', [
         ('Paragliding in Bir Billing', 'Billing take-off (about 2,400 m) to Bir landing, Kangra', 'Mid-Sep to Jun · best Oct–Nov, Mar–May',
          'India’s best-known paragliding site, with tandem joyrides for first-timers.', 'Flagship site', 'Bir Billing'),
         ('Paragliding in Manali', 'Registered sites around Solang, Dobhi, Gadsa and Raisan', 'Oct to Jun, weather permitting',
          'Short tandem flights with valley and snow-peak views, easy to fit into a Manali trip.', None, 'Manali'),
         ('Paragliding at Indrunag', 'Indrunag, above Dharamshala', 'Oct to Jun',
          'Fly over Dharamshala with the Dhauladhar range behind you.', None, 'Dharamshala'),
         ('Paragliding at Bandla', 'Bandla hill, Bilaspur, landing near the Gobind Sagar lake', 'Oct to Jun',
          'A quieter site in our home district, with lake views as you come in to land.', 'Near our office', 'Bilaspur'),
         ('Bungee jumping', 'Bir, Kangra', 'Outside the monsoon, operator-dependent',
          'HP adventure rules allow bungee for ages 12 to 55 and weights of 40 to 110 kg.', None, 'Bir'),
         ('Zipline and flying fox', 'Solang and Nehru Kund (Manali), Bir, parks near Kasauli', 'Year-round, weather permitting',
          'We book registered zipline operators only.', None, ''),
         ('Sky cycling and giant swing', 'Solang Valley and Bir', 'Year-round, weather permitting',
          'Short adrenaline rides you can add to a sightseeing day.', None, ''),
         ('Hot-air balloon ride', 'Solang Valley (tethered rides)', 'Weather-dependent',
          'A gentle lift above the valley floor for families and couples.', None, 'Solang Valley'),
     ]),
    ('water', 'Water', 'Splash', 'Water: rafting, lakes and angling',
     'The Beas and the Sutlej give Himachal its rafting. The big lakes in Bilaspur and Kangra add jet skis, kayaks and boat rides, and the trout streams need a fishing licence.',
     'river-rafting-white-water-768x513.webp', 'Group in helmets and life jackets rafting through white-water rapids', [
         ('River rafting in Kullu', 'Beas river stretches from Pirdi, Babeli and Raisan to Jhiri', 'Mar–Jun and mid-Sep–Nov · closed 15 Jul–15 Sep',
          'Grade II–III rapids, from short runs to longer stretches.', 'Most popular', 'Kullu'),
         ('Rafting at Tattapani', 'Sutlej river, Tattapani (Shimla–Mandi border)', 'Oct to May',
          'Often paired with the hot springs, and an easy add-on from Shimla.', None, 'Tattapani'),
         ('Water sports at Gobind Sagar', 'Luhnu, Bilaspur', 'Oct to Jun',
          'Jet ski, speed boat and kayak rides on the lake, close to our office.', 'Near our office', 'Bilaspur'),
         ('Boating at Kol Dam', 'Kol Dam lake on the Sutlej (Bilaspur–Mandi)', 'Oct to Jun',
          'Boat rides on a quiet mountain reservoir.', None, 'Kol Dam'),
         ('Water sports at Pong Dam', 'Maharana Pratap Sagar, Kangra', 'Oct to Jun · closed 15 Jul–15 Sep',
          'Kayaking, canoeing and sailing at the regional water sports centre.', None, 'Pong Dam'),
         ('Trout angling', 'Tirthan (Gushaini), Barot, Rohru and Sangla', '1 Mar to 31 Oct',
          'Trout fishing on licensed stretches; every angler needs a Fisheries Department licence.', None, ''),
     ]),
    ('snow', 'Snow', 'Play', 'Snow: snow points, skiing and igloos',
     'Snow season usually runs from December to March and depends on snowfall. Solang and Kufri are the easy snow days; Narkanda and Solang are where people learn to ski.',
     'snow-covered-himalayan-valley-768x432.webp', 'Snow-covered Himalayan valley under a blue sky', [
         ('Snow activities in Solang Valley', 'Solang Valley, Manali', 'Dec to Mar, snow-dependent',
          'Snow play, ski lessons, snow scooters and the ropeway in one place.', 'Winter favourite', 'Solang Valley'),
         ('Atal Tunnel and Sissu snow point', 'Sissu, north of the Atal Tunnel, Lahaul', 'Dec to Mar, on days the road is open',
          'Snow scooters and sledging; the tunnel does not need the Rohtang permit.', None, 'Sissu'),
         ('Kufri snow and fun park', 'Kufri, Shimla', 'Snow Dec–Mar · rides year-round',
          'Snow, sledging, horse and yak rides close to Shimla.', None, 'Kufri'),
         ('Skiing in Narkanda', 'Hatu and Dhumri slopes, Narkanda', 'Jan to Mar',
          'Day lessons and short beginner courses on Shimla’s ski slopes.', None, 'Narkanda'),
         ('Skiing in Solang', 'Solang Valley, Manali', 'Jan to Mar',
          'Gear and an instructor for first-timers.', None, 'Solang'),
         ('Snow scooter rides', 'Solang, Sissu and Kufri', 'Dec to Mar',
          'Short guided rides across the snow fields.', None, ''),
         ('Igloo stays', 'Sethan, on the Hampta road above Manali', 'Jan to Mar, snow-dependent',
          'A night in a snow igloo with a local team.', None, 'Sethan'),
         ('Sledging and snow tubing', 'Kufri, Solang, Sissu and Narkanda', 'Dec to Mar',
          'Easy snow fun for children and first-timers.', None, ''),
         ('Gulaba snow point', 'Gulaba, on the Rohtang road above Manali', 'Winter and spring; permit rules change by season',
          'Snow close to Manali; we check the permit rules for your date.', None, 'Gulaba'),
     ]),
    ('land', 'Land & Rides', 'Ride', 'Land and rides: ATVs, horses, bikes and jeeps',
     'From short rides at the snow points to week-long bike trips through Spiti, these are the land adventures we fit into a Himachal trip.',
     'motorbike-mountain-road-768x512.webp', 'Motorcyclist riding a dirt road along a dry Himalayan mountainside', [
         ('ATV quad bike rides', 'Solang Valley and Kufri', 'Year-round', 'Short off-road loops at the snow points.', None, ''),
         ('Horse and yak rides', 'Kufri, Solang, Khajjiar and Gulaba', 'Year-round',
          'Gentle rides for families to the viewpoints.', None, ''),
         ('Zorbing', 'Solang Valley', 'Summer on grass, winter on snow', 'Roll down the slope inside a giant ball.', None, 'Solang'),
         ('Spiti bike trips', 'Manali or Shimla to Kaza', 'May to Oct; winter Spiti only via Kinnaur',
          'Guided or self-ride motorbike trips over the high passes.', 'Bucket list', 'Spiti'),
         ('Jeep safari in Spiti', 'Kaza, Langza, Hikkim and Komic', 'May to Oct; winter 4x4 tours',
          'The highest villages of Spiti by 4x4 with a local driver.', None, 'Spiti'),
         ('Rock climbing and rappelling', 'Vashisht and Solang (Manali), Dharamshala, Bir', 'Mar–Jun and Sep–Nov',
          'Beginner sessions with instructors; minimum age 10 under HP rules.', None, ''),
         ('Mountain biking', 'Manali–Spiti roads and around Bir', 'May to Oct', 'Supported rides on mountain roads and trails.', None, ''),
     ]),
    ('treks', 'Treks & Camps', 'Walk', 'Treks and camps: day hikes to high passes',
     'Low treks run most of the year outside the monsoon; high passes open from mid-June to mid-October. Trekking in Himachal comes under the state’s adventure rules, with registered guides and insurance.',
     'camping-tents-mountain-valley-768x512.webp', 'Orange camping tent pitched in a high mountain valley under storm clouds', [
         ('Triund trek', 'McLeodganj, Dharamshala', 'Mar–Jun and Sep–Dec',
          'A short ridge trek with big Dhauladhar views; overnight camps on top.', 'Beginner friendly', 'Triund'),
         ('Kareri Lake trek', 'Kareri village, Dharamshala', 'May–Jun and Sep–Nov', 'A glacial lake below the Dhauladhars.', None, 'Kareri'),
         ('Hampta Pass trek', 'Jobra (Manali) to Chatru (Lahaul)', 'Mid-Jun to mid-Oct',
          'A classic four-to-five-day crossing from green Kullu to barren Lahaul.', None, 'Manali'),
         ('Beas Kund and Bhrigu Lake treks', 'Solang and Gulaba, Manali', 'Jun to Oct', 'Alpine lakes above Manali in two to three days.', None, 'Manali'),
         ('Kheerganga trek', 'Barshaini, Parvati Valley (Kasol)', 'Apr–Jun and Sep–Nov', 'Forest trail to meadows and hot springs.', None, 'Kasol'),
         ('Prashar Lake trek', 'Near Mandi', 'Most of the year; snow in winter', 'A lake and temple on a high meadow.', None, 'Mandi'),
         ('Great Himalayan National Park treks', 'Tirthan and Sainj valleys', 'Mar–Jun and Sep–Nov',
          'UNESCO-listed park; core-zone treks need a registered guide.', None, 'Tirthan Valley'),
         ('Camping in Himachal', 'Sethan, Kasol, Jibhi, Bir, Tirthan and Solang', 'Most of the year; high camps May–Oct',
          'Riverside and forest camps with meals and bonfires.', None, ''),
         ('Chandratal camping', 'Camps near Chandratal lake, Lahaul–Spiti', 'Jun to Oct',
          'Camping on the lake bank is banned, so camps sit a short walk away.', None, 'Chandratal'),
         ('Snow leopard safari', 'Kibber and Chicham, Spiti', 'Jan to Mar',
          'Multi-day winter trips with local spotters, for fit travellers.', None, 'Spiti'),
     ]),
    ('ropeways', 'Ropeways & Parks', 'Glide', 'Ropeways and adventure parks',
     'Ropeways are the easiest way to reach the views, and they suit every age. Timings depend on weather and maintenance days.',
     'ropeway-cable-car-snow-768x512.webp', 'Red ropeway cable car cabins over a snowy mountain slope', [
         ('Solang ropeway', 'Solang Valley, Manali', 'Year-round, weather permitting', 'Up to the snow slopes above Solang.', None, 'Solang Valley'),
         ('Dharamshala Skyway', 'Dharamshala to McLeodganj', 'Year-round', 'About 1.8 km in around five minutes.', None, 'Dharamshala'),
         ('Jakhu ropeway', 'Shimla, up to the Jakhu temple', 'Year-round', 'Skip the steep climb to Shimla’s highest point.', None, 'Shimla'),
         ('Timber Trail ropeway', 'Parwanoo, at the start of Himachal', 'Year-round', 'A first stop on the Shimla road.', None, 'Parwanoo'),
         ('Naina Devi ropeway', 'Shri Naina Devi, Bilaspur', 'Year-round', 'The easy way up to the hilltop temple.', None, 'Naina Devi'),
         ('Kufri Fun World and adventure park', 'Kufri, Shimla', 'Year-round', 'Rides and activities for families near Shimla.', None, 'Kufri'),
         ('Adventure parks near Kasauli', 'Kasauli area', 'Year-round', 'Ziplines, sky cycles and swings in pine forest.', None, 'Kasauli'),
     ]),
    ('services', 'Rentals & Services', 'Arrange', 'Rentals and services we arrange',
     'The small things decide a good snow day or a smooth Spiti trip. Tell us what you need and we arrange it with your hotel and cab.',
     'adventure-motorbike-rental-768x576.webp', 'Adventure motorbike parked on snow with bare Himalayan mountains behind', [
         ('Snow suit and boot rental', 'Palchan, Kothi and Solang (Manali); Kufri and Narkanda', 'Dec to Mar',
          'We tell your driver where to stop and what to rent.', 'Winter must-have', ''),
         ('Rohtang Pass permit', 'Online permit, booked with your cab', 'When the pass is open; closed on Tuesdays',
          'We book it for your date with the vehicle details.', None, ''),
         ('Lahaul–Spiti entry registration', 'Online e-Aagman registration', 'Year-round', 'Free, and we fill it in with you.', None, ''),
         ('Motorbike rental', 'Manali and Kaza', 'May to Oct', 'Bikes for Spiti and Lahaul, with riding gear on request.', None, ''),
         ('Photos and GoPro videos', 'At the paragliding and rafting sites', 'With your activity', 'Keep the memory of your flight or rapid.', None, ''),
         ('Camping gear, guides and porters', 'Manali, Kasol, Bir and Kaza', 'Trek season', 'Tents, sleeping bags and local guides.', None, ''),
         ('Local taxi for the snow points', 'Solang, Atal Tunnel and Rohtang from Manali', 'Winter and summer seasons',
          'Snow-point trips from Manali often need a local taxi; we pre-arrange it.', None, ''),
     ]),
]

DESTS = [
    ('Manali and Solang', 'Paragliding, snow activities, skiing, ATV rides, the ropeway and Hampta treks.', 'Oct–Jun · snow Dec–Mar',
     [('Manali packages', U + '/manali/')]),
    ('Bir and Kangra', 'Bir Billing paragliding, bungee, camps and monasteries.', 'Oct–Nov and Mar–May',
     [('Dharamshala packages', U + '/destination/dharamshala-tour-packages/')]),
    ('Kullu and Kasol', 'River rafting on the Beas, the Kheerganga trek and riverside camps.', 'Mar–Jun and Sep–Nov',
     [('Himachal packages', U + '/himachal-tour-packages/')]),
    ('Shimla, Kufri and Narkanda', 'Snow and skiing, horse and yak rides, Kufri Fun World and Tattapani rafting.', 'Snow Dec–Mar · rides year-round',
     [('Shimla packages', U + '/shimla/')]),
    ('Dharamshala and McLeodganj', 'Triund and Kareri treks, Indrunag paragliding and the Skyway.', 'Mar–Jun and Sep–Dec',
     [('Dharamshala packages', U + '/destination/dharamshala-tour-packages/')]),
    ('Bilaspur, our home district', 'Bandla paragliding, Gobind Sagar water sports, Kol Dam and the Naina Devi ropeway.', 'Oct–Jun',
     []),
    ('Chamba, Dalhousie and Khajjiar', 'Khajjiar horse rides and paragliding, forest walks and treks.', 'Mar–Jun and Sep–Nov',
     [('Dalhousie packages', U + '/dalhousie/')]),
    ('Tirthan and Jibhi', 'Trout angling, Great Himalayan National Park treks and riverside camps.', 'Mar–Jun and Sep–Nov',
     [('Himachal packages', U + '/himachal-tour-packages/')]),
    ('Lahaul and Spiti', 'Chandratal camps, Spiti bike and jeep trips, snow leopard winters.', 'May–Oct · winter trips Jan–Mar',
     [('Spiti packages', U + '/destination/spiti-valley-tour-packages/')]),
]

FAQ = [
    ('Which adventure activities can I do in Himachal Pradesh?',
     'Paragliding at Bir Billing, Manali, Dharamshala and Bilaspur; river rafting on the Beas near Kullu and on the Sutlej at Tattapani; '
     'snow activities and skiing at Solang, Kufri, Narkanda and Sissu; bungee at Bir; ziplines, ropeways and adventure parks; '
     'treks and camps; and bike and jeep trips in Spiti.'),
    ('Where is the best paragliding in Himachal?',
     'Bir Billing in Kangra is the best-known site: tandem flights take off at Billing, at about 2,400 m, and land at Bir. '
     'Solang and Dobhi near Manali, Indrunag above Dharamshala and Bandla in Bilaspur also run tandem flights. '
     'The best months are October–November and March–May.'),
    ('When are adventure activities closed in Himachal?',
     'Every year the district administrations stop paragliding, river rafting and water sports in Kullu and Kangra for the monsoon, '
     'from 15 July to 15 September. Snow activities depend on snowfall, usually December to March, and weather can stop flying on any day.'),
    ('Is there an age or weight limit for paragliding?',
     'Yes. Under the Himachal Pradesh Aero Sports Rules, passengers must be at least 12 years old and weigh at least 30 kg. '
     'People with heart conditions, epilepsy, lung problems or asthma, and pregnant women, cannot fly.'),
    ('Why don’t you show prices?',
     'Rates change with the season, the day, the group size and extras such as video or pickup. So we send today’s rate for your date on '
     'WhatsApp, as one clear quote, on its own or with your hotel and cab.'),
    ('Can you add activities to my Himachal tour package?',
     'Yes. Most guests do exactly that. Tell us the activity, your date and group size, and we fit it into your itinerary with the hotel, '
     'cab and sightseeing.'),
    ('Do I need a permit for Rohtang Pass or the Atal Tunnel?',
     'Rohtang Pass needs an online permit and is closed to tourists on Tuesdays. The Atal Tunnel and Sissu do not need the Rohtang permit. '
     'We arrange the permit with your cab when your plan includes Rohtang.'),
    ('Is Suzu Travels registered?',
     f'Yes. Suzu Travels is registered as a travel agent with the Department of Tourism &amp; Civil Aviation, Government of Himachal Pradesh '
     f'(Reg. No. {REG}), and is GST-registered. You can see both certificates on our <a href="{U}/certificates/">certificates page</a>.'),
]

HUB_CSS = '''
.sza .sza-cats .sza-cat svg.ic{width:30px;height:30px;color:var(--gold2)}
.sza .sza-cat .n{margin-top:6px}
.sza .sza-cat.dest{background:linear-gradient(145deg,#122615,#1f3d24)}
.sza .sza-cathead{display:grid;grid-template-columns:1fr 1.15fr;gap:28px;align-items:center}
.sza .sza-cathead img{width:100%;aspect-ratio:16/10;object-fit:cover;border-radius:var(--r);display:block;background:var(--navy2)}
.sza .sza-cathead .sza-lead{margin-bottom:0}
.sza .sza-count{display:inline-flex;align-items:center;gap:8px;margin-top:14px;font-size:14px;font-weight:700;color:var(--navy2);background:#fff;border:1px solid var(--line);border-radius:999px;padding:6px 12px}
.sza .sza-count svg{width:18px;height:18px;color:var(--gold)}
.sza .sza-acts{grid-template-columns:repeat(auto-fill,minmax(250px,1fr))}
.sza .sza-act .body{padding:18px}
.sza .sza-act h3{font-size:18px;margin:0}
.sza .sza-act .row{display:flex;gap:8px;font-size:14px;color:var(--mid);line-height:1.45}
.sza .sza-act .row b{flex:0 0 auto;color:var(--navy);font-weight:700;min-width:56px}
.sza .sza-act p{font-size:15px;margin:4px 0 0;color:var(--ink)}
.sza .sza-act .tag{align-self:flex-start;font-size:11.5px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:var(--navy);background:#fdf3de;border:1px solid #f0d9a8;border-radius:999px;padding:3px 9px}
.sza .sza-dests .sza-card .body{padding:20px}
.sza .sza-dests h3{display:flex;align-items:center;gap:8px}
.sza .sza-dests h3 svg{width:20px;height:20px;color:var(--gold);flex:0 0 auto}
.sza .sza-trust a{color:#fff!important;text-decoration:underline;text-decoration-color:rgba(243,217,143,.6);text-underline-offset:3px}
.sza .sza-regline{font-size:14px;color:var(--mid);margin-top:10px}
.sza #categories .sza-cats{grid-template-columns:repeat(4,minmax(0,1fr))}
.sza .sza-dests{grid-template-columns:repeat(3,minmax(0,1fr))}
.sza #safety .sza-checks{grid-template-columns:repeat(3,minmax(0,1fr))}
@media(max-width:1000px){.sza .sza-dests,.sza #safety .sza-checks{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:640px){.sza #categories .sza-cats{grid-template-columns:repeat(2,minmax(0,1fr))}.sza .sza-dests,.sza #safety .sza-checks{grid-template-columns:1fr}}
.sza .sza-regline a{color:var(--navy)!important;font-weight:700}
@media(max-width:820px){.sza .sza-cathead{grid-template-columns:1fr;gap:18px}}
'''


def act_card(cat, name, where, season, line, badge, place):
    aid = 'act-' + slug(name)
    tag = f'<span class="tag">{e(badge)}</span>' if badge else ''
    return (f'<article class="sza-card sza-act" id="{aid}"><div class="body">{tag}<h3>{e(name)}</h3>'
            f'<div class="row"><b>Where</b><span>{e(where)}</span></div>'
            f'<div class="row"><b>When</b><span>{e(season)}</span></div>'
            f'<p>{e(line)}</p>'
            f'<div class="go"><a class="q" href="{wa(name, place)}" target="_blank" rel="noopener">Get Quote →</a></div></div></article>')


def build():
    n_acts = sum(len(c[7]) for c in CATS)
    wa_hub = wa('adventure activities', 'Himachal')
    nav = ''.join(f'<a href="#{c[0]}">{e(c[1])}</a>' for c in CATS)
    nav += '<a href="#destinations">By destination</a><a href="#safety">Safety</a><a href="#faq">FAQ</a>'
    nav += f'<a class="cta" href="{wa_hub}" target="_blank" rel="noopener">Get Quote</a>'
    tiles = ''.join(f'<a class="sza-cat" href="#{c[0]}">{icon(c[0])}<span class="n">{e(c[1])}</span>'
                    f'<span class="c">{len(c[7])} {"services" if c[0] == "services" else "activities"}</span></a>' for c in CATS)
    tiles += f'<a class="sza-cat dest" href="#destinations">{icon("dest")}<span class="n">By destination</span><span class="c">{len(DESTS)} regions</span></a>'

    TREKS_EXPLAINER = '<figure id="treks-explainer" style="margin:0 auto 32px;max-width:880px"><video poster="https://suzutravels.com/wp-content/uploads/2026/10/which-trek-which-month-himachal-treks-explainer.webp" autoplay muted loop playsinline preload="none" width="1600" height="900" style="display:block;width:100%;height:auto;aspect-ratio:16/9;border-radius:18px;background:#0b1f33;box-shadow:0 12px 32px rgba(11,31,51,.2)" aria-label="12-second motion graphic: which trek in which month. Triund March to June and September to December; Kareri Lake May to June and September to November; Kheerganga April to June and September to November; Great Himalayan National Park March to June and September to November; Beas Kund and Bhrigu Lake June to October; Hampta Pass mid-June to mid-October; Chandratal camping June to October"><source src="https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@54b9fe2af8b93005dc800e0977cf058a5f76646a/adventure-kit/media/adventure-hub/treks-explainer.webm" type="video/webm"><source src="https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@54b9fe2af8b93005dc800e0977cf058a5f76646a/adventure-kit/media/adventure-hub/treks-explainer.mp4" type="video/mp4"></video><figcaption style="margin-top:10px;font-size:15px;line-height:1.5;color:#5b6975;text-align:center">Which trek, which month. Low treks have a spring and an autumn window; high passes and Chandratal open from June to October.</figcaption></figure>'
    SNOW_EXPLAINER = '<figure id="snow-explainer" style="margin:0 auto 32px;max-width:880px"><video poster="https://suzutravels.com/wp-content/uploads/2026/09/wheres-the-snow-manali-altitude-explainer.webp" autoplay muted loop playsinline preload="none" width="1600" height="900" style="display:block;width:100%;height:auto;aspect-ratio:16/9;border-radius:18px;background:#0b1f33;box-shadow:0 12px 32px rgba(11,31,51,.2)" aria-label="12-second motion graphic: where is the snow near Manali. Altitudes Manali 2,050 m, Solang 2,560 m, Atal Tunnel 3,060 m, Rohtang 3,978 m; first snow up high in October to November, best snow at Solang late December to February; Atal Tunnel needs no Rohtang permit"><source src="https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@94beec6a920a51a03b5fd553534a8b2951d6b7db/adventure-kit/media/snow-activities-manali/explainer.webm" type="video/webm"><source src="https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@94beec6a920a51a03b5fd553534a8b2951d6b7db/adventure-kit/media/snow-activities-manali/explainer.mp4" type="video/mp4"></video><figcaption style="margin-top:10px;font-size:15px;line-height:1.5;color:#5b6975;text-align:center">Where\'s the snow near Manali? Higher points get it first. We check the road and snow status the evening before your snow day.</figcaption></figure>'
    AIR_EXPLAINER = '<figure id="air-explainer" style="margin:0 auto 32px;max-width:880px"><video poster="https://suzutravels.com/wp-content/uploads/2026/10/where-you-can-fly-himachal-air-explainer.webp" autoplay muted loop playsinline preload="none" width="1600" height="900" style="display:block;width:100%;height:auto;aspect-ratio:16/9;border-radius:18px;background:#0b1f33;box-shadow:0 12px 32px rgba(11,31,51,.2)" aria-label="12-second motion graphic: where and when you can fly in Himachal. Paragliding at Bir Billing (Kangra, take-off about 2,400 m), Indrunag above Dharamshala, Manali sites around Solang, Dobhi, Gadsa and Raisan, and Bandla in Bilaspur. Flying mid-September to June at Bir and October to June at the others, best October to November and March to May, no flying 15 July to 15 September in Kullu and Kangra. Passengers 12 years and 30 kg or more, registered pilots, notified sites, weather decides every flight"><source src="https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@f72f24f2f04db5137d5bef8006c8e04e36a50d19/adventure-kit/media/adventure-hub/air-explainer.webm" type="video/webm"><source src="https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@f72f24f2f04db5137d5bef8006c8e04e36a50d19/adventure-kit/media/adventure-hub/air-explainer.mp4" type="video/mp4"></video><figcaption style="margin-top:10px;font-size:15px;line-height:1.5;color:#5b6975;text-align:center">Where and when you can fly. We check the site and the day&#8217;s weather for your date before we book the flight.</figcaption></figure>'
    WATER_EXPLAINER = '<figure id="water-explainer" style="margin:0 auto 32px;max-width:880px"><video poster="https://suzutravels.com/wp-content/uploads/2026/10/where-you-can-get-on-the-water-himachal-explainer.webp" autoplay muted loop playsinline preload="none" width="1600" height="900" style="display:block;width:100%;height:auto;aspect-ratio:16/9;border-radius:18px;background:#0b1f33;box-shadow:0 12px 32px rgba(11,31,51,.2)" aria-label="12-second motion graphic: where and when you can get on the water in Himachal. Rafting on the Beas in Kullu from Pirdi to Jhiri, Grade II to III rapids, March to June and mid-September to November; rafting on the Sutlej at Tattapani, October to May; jet ski, kayak and boat rides on Gobind Sagar, Kol Dam and Pong Dam, October to June; trout angling at Tirthan, Barot, Rohru and Sangla, 1 March to 31 October with a Fisheries licence. Rafting and water sports are closed 15 July to 15 September in Kullu and Kangra"><source src="https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@68b3a65c854d1125d4db62ba32a2fa41716fcdb5/adventure-kit/media/adventure-hub/water-explainer.webm" type="video/webm"><source src="https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@68b3a65c854d1125d4db62ba32a2fa41716fcdb5/adventure-kit/media/adventure-hub/water-explainer.mp4" type="video/mp4"></video><figcaption style="margin-top:10px;font-size:15px;line-height:1.5;color:#5b6975;text-align:center">Where and when you can get on the water. We check the river level and the day&#8217;s weather for your date before we book.</figcaption></figure>'
    secs = []
    for i, (cid, label, kicker, h2, lead, img, alt, acts) in enumerate(CATS):
        alt_cls = ' alt' if i % 2 == 0 else ''
        cards = ''.join(act_card(cid, *a) for a in acts)
        word = 'services' if cid == 'services' else 'activities'
        # Visual Studio 29 Sep 2026: snow explainer motion graphic between the snow head and its cards
        extra = SNOW_EXPLAINER if cid == 'snow' else ''
        # Visual Studio 4 Oct 2026: Air motion graphic (where + when you can fly) between the air head and its cards
        if cid == 'air': extra = AIR_EXPLAINER
        # Visual Studio 5 Oct 2026: Water motion graphic (where + when: rafting, lakes, trout) between the water head and its cards
        if cid == 'water': extra = WATER_EXPLAINER
        # Visual Studio 6 Oct 2026: Treks motion graphic (which trek, which month) between the treks head and its cards
        if cid == 'treks': extra = TREKS_EXPLAINER
        secs.append(
            f'<section class="sza-sec{alt_cls}" id="{cid}"><div class="sza-cathead">'
            f'<img src="{MEDIA}{img}" alt="{e(alt)}" loading="lazy" decoding="async" width="768" height="480">'
            f'<div><span class="sza-kicker">{e(kicker)}</span><h2>{e(h2)}</h2><p class="sza-lead">{e(lead)}</p>'
            f'<span class="sza-count">{icon(cid, "")}{len(acts)} {word} · price on request</span></div></div>'
            f'{extra}<div class="sza-grid sza-acts">{cards}</div></section>')

    dcards = ''
    for name, what, when, links in DESTS:
        more = ''.join(f'<a class="x" href="{h}">{e(t)} →</a>' for t, h in links)
        dcards += (f'<article class="sza-card" id="dest-{slug(name)}"><div class="body"><h3>{icon("dest", "")}{e(name)}</h3>'
                   f'<p class="meta">{e(what)}</p><p class="meta"><b>Best time:</b> {e(when)}</p>'
                   f'<div class="go"><a class="q" href="{wa("adventure activities", name)}" target="_blank" rel="noopener">Get Quote →</a>{more}</div></div></article>')

    faq = ''.join(f'<details><summary>{e(q)}</summary><p>{a if "<a " in a else e(a)}</p></details>' for q, a in FAQ)

    out = f'''<style>{HUB_CSS}</style>
<div class="sza">
<section class="sza-hero">
<video autoplay muted loop playsinline preload="metadata" poster="{MEDIA}himachal-adventure-activities-hero.webp"><source src="{CDN}hero.webm" type="video/webm"><source src="{CDN}hero.mp4" type="video/mp4"></video>
<div class="sza-hero-in">
<span class="sza-kicker">Himachal Pradesh · Adventure</span>
<p class="sza-hero-tag">Fly, raft, ski and trek across Himachal, planned by one local team</p>
<p class="sza-hero-sub">{n_acts} adventures in {len(DESTS)} regions: paragliding at Bir Billing, rafting on the Beas, snow days in Solang and Kufri, treks, camps and ropeways, added to your hotel-and-cab trip with one message.</p>
<ul class="sza-chips"><li><b>{n_acts}</b> activities &amp; services</li><li><b>{len(DESTS)}</b> regions</li><li><b>Flying</b> Oct – Jun</li><li><b>Snow</b> Dec – Mar</li><li><b>Price</b> Get Quote</li></ul>
<div class="sza-btns"><a class="sza-btn gold" href="{wa_hub}" target="_blank" rel="noopener">Get a quote on WhatsApp</a><a class="sza-btn ghost" href="#categories">Explore activities</a></div>
<div class="sza-trust"><span><a href="{U}/certificates/">HP Tourism registered travel agent · Reg. No. {REG}</a></span><span>Local team in Himachal</span><span>Hotel, cab and activity in one plan</span></div>
</div>
</section>
<nav class="sza-nav" aria-label="Adventure categories"><div class="sza-nav-in">{nav}</div></nav>
<section class="sza-sec" id="categories">
<span class="sza-kicker">Choose your adventure</span>
<h2>Air, water, snow and more: pick your adventure</h2>
<p class="sza-answer">Himachal Pradesh offers paragliding at Bir Billing, Manali and Dharamshala, river rafting on the Beas near Kullu, snow activities and skiing at Solang, Kufri and Narkanda, plus treks, camps, ropeways and bike trips in Spiti. Most activities run from October to June; paragliding, rafting and water sports stop in Kullu and Kangra from 15 July to 15 September. Suzu Travels arranges them with registered local operators and adds hotel and cab.</p>
<div class="sza-cats">{tiles}</div>
<p class="sza-regline">Suzu Travels is an <a href="{U}/certificates/">HP Tourism registered travel agent (Reg. No. {REG})</a> based in Ghumarwin, Bilaspur.</p>
</section>
{''.join(secs)}
<section class="sza-sec" id="destinations">
<span class="sza-kicker">Where to go</span>
<h2>Adventure by destination</h2>
<p class="sza-lead">Already know where you are staying? Here is what each region is best for, and when to go.</p>
<div class="sza-grid sza-dests">{dcards}</div>
</section>
<section class="sza-band" id="safety"><div class="sza-band-in">
<span class="sza-kicker">Safety first</span>
<h2>What we check before we book it</h2>
<p class="sza-lead">Adventure in Himachal is regulated by the state. We follow the rules below and only book registered local operators.</p>
<ul class="sza-checks">
<li><b>Registered operators only</b>Operators and guides must be registered under the HP Tourism Development and Registration Act, 2002 and the state adventure rules.</li>
<li><b>Paragliding rules</b>Registered pilots, notified sites only, no passengers under 12 years or under 30 kg (HP Aero Sports Rules).</li>
<li><b>Monsoon closure</b>Paragliding, rafting and water sports stop in Kullu and Kangra from 15 July to 15 September.</li>
<li><b>Bungee and zipline limits</b>Bungee is allowed for ages 12–55 and 40–110 kg; ziplines only with registered operators.</li>
<li><b>Weather calls</b>Flights, rafting and snow rides stop when the weather turns. We plan a buffer day for flying where we can.</li>
<li><b>Permits handled</b>Rohtang, Lahaul–Spiti and national-park permits are arranged with your cab and itinerary.</li>
</ul>
<figure id="safety-explainer" style="margin:28px auto 0;max-width:880px"><video poster="https://suzutravels.com/wp-content/uploads/2026/10/adventure-safety-checks-explainer.webp" autoplay muted loop playsinline preload="none" width="1600" height="900" style="display:block;width:100%;height:auto;aspect-ratio:16/9;border-radius:18px;background:#0b1f33;box-shadow:0 12px 32px rgba(0,0,0,.3)" aria-label="10-second motion graphic: what we check before we book. Paragliding only for passengers 12 years and over and 30 kg and over, with registered pilots at notified sites; no paragliding, rafting or water sports in Kullu and Kangra from 15 July to 15 September; bungee for ages 12 to 55 and 40 to 110 kg; weather first; registered local operators only and permits arranged with your cab"><source src="https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@2ca73775ed4811aab226daf655b26074d4abc5ba/adventure-kit/media/adventure-hub/safety-explainer.webm" type="video/webm"><source src="https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@2ca73775ed4811aab226daf655b26074d4abc5ba/adventure-kit/media/adventure-hub/safety-explainer.mp4" type="video/mp4"></video><figcaption style="margin-top:10px;font-size:15px;line-height:1.5;color:#d7e0e9;text-align:center">The four rules we check for every booking, in 10 seconds. Ask us on WhatsApp if your group has kids or elders.</figcaption></figure>
</div></section>
<section class="sza-sec" id="booking">
<span class="sza-kicker">How it works</span>
<h2>How booking works</h2>
<ol class="sza-steps">
<li><h3>Tell us</h3><p>The activity, place, date and group size, on WhatsApp or the quote form.</p></li>
<li><h3>We check your date</h3><p>Season, weather rules and a slot with a registered local operator.</p></li>
<li><h3>You get one quote</h3><p>The activity alone, or with hotel, cab and sightseeing.</p></li>
<li><h3>Confirm and go</h3><p>A small advance confirms it, and our team looks after the day.</p></li>
</ol>
<figure id="booking-explainer" style="margin:28px auto 0;max-width:880px"><video poster="https://suzutravels.com/wp-content/uploads/2026/09/how-booking-works-adventure-explainer.webp" autoplay muted loop playsinline preload="none" width="1600" height="900" style="display:block;width:100%;height:auto;aspect-ratio:16/9;border-radius:18px;background:#0b1f33;box-shadow:0 12px 32px rgba(11,31,51,.2)" aria-label="10-second motion graphic: how booking works in 4 steps. Tell us the activity, place, date and group size; we check your date, season, weather rules and a registered local operator; you get one quote, activity alone or with hotel, cab and sightseeing; confirm with a small advance and our team looks after the day"><source src="https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@1d39d275782e44fb56b01370aa2524e4786607f3/adventure-kit/media/adventure-hub/booking-explainer.webm" type="video/webm"><source src="https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@1d39d275782e44fb56b01370aa2524e4786607f3/adventure-kit/media/adventure-hub/booking-explainer.mp4" type="video/mp4"></video><figcaption style="margin-top:10px;font-size:15px;line-height:1.5;color:#5b6975;text-align:center">Four steps from your WhatsApp message to your adventure day. Send your plan and get today&#8217;s rate within minutes.</figcaption></figure>
</section>
<section class="sza-sec" id="reel"><div style="display:flex;flex-wrap:wrap;align-items:center;gap:32px"><div style="flex:0 0 auto;width:min(300px,100%);margin:0 auto"><video poster="https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@241427f0ff3f1bb319810e060a1d53b4f3c6359a/adventure-kit/media/adventure-hub/reel-web-poster.webp" autoplay muted loop playsinline preload="metadata" width="300" height="533" style="display:block;width:100%;height:auto;aspect-ratio:9/16;border-radius:18px;background:#0b1f33;box-shadow:0 12px 32px rgba(11,31,51,.25)" aria-label="15-second reel: air, water and snow adventures in Himachal with Suzu Travels"><source src="https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@777751efe8e8e7afe4b27edba6234489fe066569/adventure-kit/media/adventure-hub/reel-web.webm" type="video/webm"><source src="https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@241427f0ff3f1bb319810e060a1d53b4f3c6359a/adventure-kit/media/adventure-hub/reel-web.mp4" type="video/mp4"></video></div><div style="flex:1 1 320px;min-width:0"><span class="sza-kicker">Watch in 15 seconds</span><h2>Air, water and snow in one Himachal trip</h2><p>Paragliding, rafting, snow days, treks and ropeways: tell us which ones you want and we add them to your hotel and cab plan.</p><div class="sza-btns"><a class="sza-btn gold" href="https://wa.me/917087488961?text=Hi%20Suzu%20Travels%2C%20I%20want%20a%20quote%20for%20adventure%20activities%20in%20Himachal.%20Travel%20date%3A%20___%20%2C%20people%3A%20___%20%28page%3A%20adventure%20reel%29" target="_blank" rel="noopener">Get Quote on WhatsApp</a><a class="sza-btn" href="#categories" style="background:#fff;color:#0b1f33;border:2px solid #0b1f33">See all activities</a></div></div></div></section>
<section class="sza-quote"><div><span class="sza-kicker">Plan it with us</span><h2>Add an adventure to your Himachal trip</h2><p>Send your dates and group size. We reply with today’s rate for the activity, and a full plan with hotel and cab if you want one.</p></div>
<div class="sza-btns"><a class="sza-btn gold" href="{wa_hub}" target="_blank" rel="noopener">WhatsApp for a quote</a><a class="sza-btn ghost" href="{U}/himachal-tour-packages-quote/">Quote form</a><a class="sza-btn ghost" href="tel:+917087488961">Call +91 70874 88961</a></div></section>
<section class="sza-sec" id="faq">
<span class="sza-kicker">Good to know</span>
<h2>Himachal adventure FAQs</h2>
<div class="sza-faq">{faq}</div>
<p class="sza-note">Rules and seasons checked on 29 September 2026. Weather and district orders can change them at short notice; we confirm for your date.</p>
</section>
</div>'''
    return out, n_acts


if __name__ == '__main__':
    here = os.path.dirname(os.path.abspath(__file__))
    out, n = build()
    open(os.path.join(here, 'adventure.html'), 'w').write(out)
    print('activities:', n, 'bytes:', len(out))
