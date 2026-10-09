#!/usr/bin/env python3
"""Homepage enhancement, 9 Oct 2026 (nz layer) — Claude Fable 5.1, interactive session with Sushil.
Usage: python3 enh-2026-10-09.py live.html after.html

1. NEW section #nz-toolkit ("Traveller's toolkit") after #nz-explore, five tools in tabs:
   a. Trip cost estimator  — 15 priced trips from nz-data × travellers × hotel tier × season
                             (identical rules to the trip sheet: Deluxe ×1 / Super Deluxe ×1.18 / Luxury ×1.35, peak ×1.25).
   b. Distance & drive time — 30 North-India road pairs (approx km / hill hours) linked to the /cabs/ route pages.
   c. Packing checklist    — 6 trip kinds, tick-able, progress, copy / WhatsApp share, remembered per browser.
   d. Permits & help       — Rohtang permit, HP entry tax, Inner Line Permit, Char Dham & Amarnath registration,
                             e-Visa, altitude (AMS) awareness, emergency numbers, official links.
   e. Festivals & events   — rolling 12-month calendar (verified dates; "dates vary" where announced yearly).
2. Speed: the hero film's requestAnimationFrame loop now stops while the hero is off-screen,
   the tab is hidden or the film is paused (it ran every frame forever).
3. CLS: the late <style id="suzu-redesign-2026-09"> (szx-* sections, ~556 KB into the body) is moved into <head>.
All additions are plain HTML/CSS/JS inside the page; nothing is removed; no new network calls.
"""
import sys, re, json, html as H

src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
assert 'id="nz-toolkit"' not in s and 'nz-tk-js' not in s, 'already applied'

def once(hay, needle):
    assert hay.count(needle) == 1, (needle[:70], hay.count(needle))
    return hay.index(needle)

# ---------------------------------------------------------------- data
D = json.loads(re.search(r'<script[^>]*id="nz-data"[^>]*>(.*?)</script>', s, re.S).group(1))
PRICED = [t for t in D['trips'] if t.get('price')]
assert len(PRICED) >= 12, len(PRICED)

# Distance pairs: (from, to, km, hours-text, note, cab path or '')
DIST = [
 ("Delhi","Shimla",345,"7–8 h","Via Chandigarh & Kalka; last 90 km is hill road.","/cabs/delhi-to-shimla-taxi/"),
 ("Delhi","Manali",540,"12–13 h","Via Chandigarh, Bilaspur, Mandi & Kullu; night drives common.","/cabs/delhi-to-manali-taxi/"),
 ("Delhi","Chandigarh",250,"4½–5 h","Four-lane highway all the way.","/cabs/delhi-to-chandigarh-taxi/"),
 ("Delhi","Dharamshala",480,"10–11 h","Via Chandigarh & Pathankot road; Kangra valley at the end.","/cabs/dharamshala-taxi-service/"),
 ("Delhi","Dalhousie",560,"12 h","Via Pathankot; last 80 km winds up through pine forest.","/cabs/pathankot-to-dharamshala-taxi/"),
 ("Delhi","Dehradun",250,"5½–6 h","Expressway most of the way.","/cabs/delhi-to-dehradun-taxi/"),
 ("Delhi","Haridwar",220,"5 h","Gateway to Char Dham; expressway till Roorkee.","/cabs/delhi-to-haridwar-taxi/"),
 ("Delhi","Rishikesh",240,"5½ h","Haridwar + 25 km.","/cabs/delhi-to-rishikesh-taxi/"),
 ("Delhi","Mussoorie",290,"7 h","Dehradun + a 35 km climb.","/cabs/delhi-to-mussoorie-taxi/"),
 ("Delhi","Amritsar",450,"8 h","Mostly expressway; Golden Temple by evening.","/cabs/delhi-to-amritsar-taxi/"),
 ("Delhi","Jaipur",280,"5 h","Expressway; good for a Golden Triangle start.",""),
 ("Delhi","Agra",230,"3½–4 h","Yamuna Expressway.",""),
 ("Chandigarh","Shimla",115,"3½ h","Kalka–Shimla climb; the toy train is the slow, pretty option.","/cabs/chandigarh-to-shimla-taxi/"),
 ("Chandigarh","Manali",310,"8 h","Bilaspur, Mandi, Kullu valley; the Beas keeps you company.","/cabs/chandigarh-to-manali-taxi/"),
 ("Chandigarh","Dharamshala",250,"6½ h","Via Una or Hoshiarpur.","/cabs/chandigarh-taxi-service/"),
 ("Chandigarh","Dalhousie",310,"8 h","Via Pathankot.",""),
 ("Chandigarh","Amritsar",230,"4½ h","Highway via Ludhiana & Jalandhar.",""),
 ("Shimla","Manali",250,"7 h","Via Mandi & Kullu; Pandoh dam and Aut tunnel on the way.","/cabs/shimla-to-manali-taxi/"),
 ("Shimla","Kalpa",230,"7½ h","Kinnaur road along the Sutlej; Kinner Kailash view at Kalpa.","/cabs/shimla-taxi-service/"),
 ("Shimla","Kaza",420,"2 days","Via Kinnaur (Reckong Peo, Nako, Tabo); open most of the year.","/cabs/shimla-taxi-service/"),
 ("Manali","Kaza",200,"8 h","Atal Tunnel + Kunzum La (4,551 m); open roughly Jun–Oct only.","/cabs/manali-taxi-service/"),
 ("Manali","Leh",475,"2 days","Rohtang/Atal, Baralacha, Tanglang La; open roughly Jun–Sep.","/cabs/manali-taxi-service/"),
 ("Manali","Dharamshala",235,"6½ h","Via Mandi & Palampur tea gardens.","/cabs/manali-taxi-service/"),
 ("Pathankot","Dharamshala",90,"2½ h","Nearest railhead for Kangra & Dharamshala.","/cabs/pathankot-to-dharamshala-taxi/"),
 ("Pathankot","Dalhousie",80,"2½ h","Nearest railhead for Dalhousie & Khajjiar.","/cabs/pathankot-to-dharamshala-taxi/"),
 ("Jammu","Srinagar",265,"7 h","Via Udhampur, Banihal tunnel; convoy halts possible.","/cabs/jammu-to-srinagar-taxi/"),
 ("Srinagar","Gulmarg",50,"1½ h","Tangmarg climb; chains needed in snow.","/cabs/srinagar-taxi-service/"),
 ("Srinagar","Pahalgam",90,"2½ h","Along the Lidder river via Anantnag.","/cabs/srinagar-taxi-service/"),
 ("Leh","Pangong Lake",225,"6 h","Over Chang La (5,360 m); acclimatise in Leh first.",""),
 ("Haridwar","Kedarnath (Gaurikund)",240,"8–9 h","Rishikesh, Devprayag, Rudraprayag, Guptkashi; then 16 km trek.","/cabs/haridwar-taxi-service/"),
 ("Haridwar","Badrinath",320,"10–11 h","Via Rudraprayag, Karnaprayag & Joshimath.","/cabs/haridwar-taxi-service/"),
 ("Dehradun","Mussoorie",35,"1½ h","Short steep climb; views of the Doon valley.","/cabs/dehradun-taxi-service/"),
]
CITIES = []
for a, b, *_ in DIST:
    for c in (a, b):
        if c not in CITIES: CITIES.append(c)

PACK = {
 "snow": ["Snow & winter (Dec–Mar)", [
   ("Wear", ["Thermal inner set (top + bottom)","Fleece or wool mid-layer","Waterproof padded jacket","Woollen cap, gloves & neck warmer","2 pairs woollen socks per day","Waterproof boots with grip (or rent snow boots at Solang)"]),
   ("Carry", ["Sunglasses — snow glare is strong","Sunscreen SPF 50 & lip balm","Moisturiser (dry cold air)","Small flask for hot water / tea","Power bank — batteries drain in cold","Zip-lock bags to keep phone dry"]),
   ("Papers", ["Photo ID for everyone (hotel check-in)","Hotel & cab confirmations on phone","Rohtang / Atal Tunnel permit if self-driving"]),
   ("Health", ["Regular medicines + a basic kit","Cold & cough tablets, ORS","Motion-sickness tablets for hill roads"])]],
 "summer": ["Summer hills (Apr–Jun)", [
   ("Wear", ["Light cottons for the day","One warm layer for evenings (Shimla/Manali are 10–15 °C at night)","Comfortable walking shoes","Cap or hat"]),
   ("Carry", ["Sunscreen & sunglasses","Reusable water bottle","Light rain jacket (May–Jun showers)","Day-pack for Mall Road & short walks","Power bank & charger"]),
   ("Papers", ["Photo ID for everyone","Bookings on phone + one printed copy","Rohtang permit if self-driving (closed Tuesdays)"]),
   ("Health", ["Regular medicines","ORS & motion-sickness tablets","Hand sanitiser"])]],
 "monsoon": ["Monsoon hills (Jul–Sep)", [
   ("Wear", ["Quick-dry clothes","Waterproof jacket or poncho","Sandals/boots with grip; avoid canvas shoes","A light warm layer for cloudy days"]),
   ("Carry", ["Sturdy umbrella","Rain covers for bags","Zip-lock bags for electronics & papers","Torch — power cuts happen","Mosquito repellent"]),
   ("Papers", ["Photo ID for everyone","Bookings on phone (network can drop)","Keep a flexible day — landslides can close roads"]),
   ("Health", ["Regular medicines + first-aid","Antiseptic cream & band-aids","Water purification tablets or bottled water"])]],
 "altitude": ["High altitude — Spiti, Ladakh (3,500 m+)", [
   ("Wear", ["Layers: thermal + fleece + windproof shell","Warm cap, gloves, buff","UV sunglasses (category 3+)","Broken-in trekking shoes"]),
   ("Carry", ["Sunscreen SPF 50 — UV is intense","3 L water capacity; drink constantly","Lip balm & moisturiser","Dry snacks (chikki, nuts, chocolate)","Power bank; few charging points","Cash — ATMs are rare, cards rarely work"]),
   ("Papers", ["Photo ID; Inner Line Permit for foreigners (Kinnaur–Spiti)","Ladakh permits for Nubra / Pangong if needed","Travel insurance that covers altitude"]),
   ("Health", ["Doctor's advice on altitude medicine before the trip","Plan an acclimatisation day at Kaza / Leh","Avoid alcohol & smoking on arrival","Pulse oximeter is useful for groups"])]],
 "pilgrim": ["Pilgrimage — Char Dham, Shakti Peeth, Amarnath", [
   ("Wear", ["Modest, comfortable clothes for temple visits","Warm layer — Kedarnath & Badrinath are cold even in May","Shoes easy to remove; thick socks for cold temple floors","Raincoat or poncho (May–Jun & Sep)"]),
   ("Carry", ["Yatra registration / RFID card (Char Dham) or SASB card (Amarnath)","Photo ID & 2 passport photos","Small torch & whistle","Dry fruits & glucose for walks","Walking stick for Kedarnath / Yamunotri treks","Cloth bag for prasad; polythene is banned in many shrines"]),
   ("Papers", ["Medical fitness certificate where required (Amarnath, elderly pilgrims)","Hotel & cab confirmations","Emergency contacts written on paper"]),
   ("Health", ["Regular medicines for the full trip + 3 days","ORS, pain-relief spray, band-aids","Motion-sickness tablets for the mountain roads"])]],
 "beach": ["Beach & backwaters — Goa, Kerala, Andaman", [
   ("Wear", ["Light cottons & linen","Swimwear + cover-up","Flip-flops & one pair of closed shoes","Hat & sunglasses"]),
   ("Carry", ["Reef-safe sunscreen SPF 50","Mosquito repellent (Kerala evenings)","Waterproof phone pouch","Reusable water bottle","Light rain jacket (Jun–Sep)","Dry bag for boat trips"]),
   ("Papers", ["Photo ID; passport for Andaman foreigners (RAP)","Ferry / cruise tickets on phone","Scuba / water-sports medical declaration if planned"]),
   ("Health", ["After-sun lotion & aloe gel","ORS & anti-diarrhoea tablets","Regular medicines"])]],
}

HELP = [
 ("Rohtang Pass permit", "rohtang", "var(--nz-glacier)",
  "Private vehicles need a permit for Rohtang (mid-May to late Oct). Tourism permit ₹550 incl. congestion charge, 1,200 vehicles/day, closed to tourists every Tuesday. Atal Tunnel to Lahaul (Sissu) needs no Rohtang permit.",
  [("https://rohtangpermits.hp.gov.in/","Official permit portal",1),("/rohtang-pass-permit-himachal-road-status/","Our permit & road-status guide",0)]),
 ("Himachal entry tax", "tax", "var(--nz-emerald)",
  "Vehicles registered outside Himachal pay a green / entry tax at the border barriers (Parwanoo, Swarghat, Kandwal). Commercial cabs are covered by our transporters.",
  [("/himachal-entry-tax-permits-2026/","Entry tax & permits guide 2026",0)]),
 ("Inner Line Permit (foreigners)", "ilp", "var(--nz-indigo)",
  "Foreign nationals need an Inner Line Permit for Kinnaur beyond Jangi (Nako, Tabo, Kaza route). Issued at the SDM office in Reckong Peo or Kaza, or the DC office Shimla. Indian citizens need no permit for Spiti.",
  [("/winter-spiti-valley-guide-2026-27/","Winter Spiti guide",0),("/private-india-tours-for-foreigners/","Tours for international guests",0)]),
 ("Char Dham registration", "chardham", "var(--nz-saffron)",
  "Yatra registration is mandatory for Yamunotri, Gangotri, Kedarnath and Badrinath. Register online with ID and travel dates; carry the registration on your phone.",
  [("https://registrationandtouristcare.uk.gov.in/","Uttarakhand Yatra registration",1),("/destination/chardham-tour-packages/","Char Dham packages",0)]),
 ("Amarnath Yatra", "amarnath", "var(--nz-rose)",
  "Registration opens each spring through the Shri Amarnathji Shrine Board with a compulsory health certificate from an authorised doctor. Yatra usually runs July–August.",
  [("https://jksasb.nic.in/","Shrine Board (SASB)",1),("/pilgrimage-tours/","Pilgrimage tours",0)]),
 ("e-Visa for international guests", "evisa", "var(--nz-lagoon)",
  "Most nationalities can apply for an Indian e-Tourist Visa online (30-day, 1-year and 5-year). Apply only on the Government of India portal.",
  [("https://indianvisaonline.gov.in/evisa/","Government e-Visa portal",1),("/private-india-tours-for-foreigners/","Private India tours (USD)",0)]),
 ("Altitude awareness (AMS)", "ams", "var(--nz-ember)",
  "Above 3,000 m — Spiti, Ladakh, Kedarnath — headache, nausea and breathlessness are early signs of altitude sickness. Climb gradually, keep a rest day, drink water, avoid alcohol, and descend if symptoms worsen. Talk to your doctor before the trip.",
  [("/how-to-prepare-for-high-altitude-trekking-in-ladakh-a-complete-preparation-guide/","High-altitude preparation guide",0),("/complete-ladakh-packing-list-essential-gear-for-a-safe-high-altitude-trip/","Ladakh packing list",0)]),
]
EMERG = [("112","All-India emergency (police, fire, ambulance)"),("108","Ambulance"),("1363","Tourist helpline (Ministry of Tourism, 24×7, multilingual)"),("1073","Highway / road accident helpline"),("+91 70874 88961","Suzu Travels tour manager, 24×7")]
LINKS = [
 ("https://himachaltourism.gov.in/","Himachal Tourism (official)"),("https://hptdc.in/","HPTDC hotels & tours"),
 ("https://online.hrtchp.com/","HRTC bus booking"),("https://www.irctc.co.in/","IRCTC train tickets"),
 ("https://mausam.imd.gov.in/","IMD weather"),("https://uttarakhandtourism.gov.in/","Uttarakhand Tourism"),
 ("https://www.jktourism.jk.gov.in/","J&K Tourism"),("https://www.incredibleindia.gov.in/","Incredible India"),
]
# Festivals: (iso-date-or-month 'YYYY-MM', 'YYYY-MM-DD'), title, where, note, link(path), fixed(True) or 'varies'
FEST = [
 ("2026-10-20","2026-10-26","Kullu Dussehra","Kullu, Himachal","Week-long rath yatra of Raghunath ji — 200+ village deities gather at Dhalpur.","/himachal-tour-packages/",True),
 ("2026-11-08","","Diwali","All India","Peak week for family trips; book hotels early.","/tours/",True),
 ("2026-12-24","2027-01-01","Christmas & New Year in the hills","Shimla · Manali · Dalhousie","Snow-week rush; Shimla's winter carnival runs around these dates.","/himachal-snowfall-winter-2026-27/",False),
 ("2027-01-13","","Lohri","Punjab · Himachal","Bonfire night; Amritsar and Kangra are lively.","/cabs/delhi-to-amritsar-taxi/",True),
 ("2027-02","","Losar (Tibetan New Year)","Spiti · Ladakh · Dharamshala","Monastery dances and butter-lamp prayers; dates follow the Tibetan calendar.","/winter-spiti-valley-guide-2026-27/",False),
 ("2027-03-06","","Maha Shivaratri","Baijnath · Jyotirlingas","Night-long worship; Baijnath (Kangra) is Himachal's classic Shivaratri.","/pilgrimage-tours/12-jyotirlinga/",True),
 ("2027-03-22","","Holi","All India","Colour festival; Barsana & Vrindavan for the famous one.","/golden-triangle-tour/",True),
 ("2027-05","","Char Dham opening","Uttarakhand","Portals open around Akshaya Tritiya; exact dates announced on Basant Panchami.","/destination/chardham-tour-packages/",False),
 ("2027-06","2027-07","Hemis Festival","Hemis, Ladakh","Masked Cham dances at Ladakh's biggest monastery; 2026 edition was 24–25 June.","/destination/leh-ladakh-tour-packages/",False),
 ("2027-07","2027-08","Amarnath Yatra","Kashmir","Pilgrimage to the ice lingam; registration via the Shrine Board.","/pilgrimage-tours/",False),
 ("2027-07","2027-08","Minjar Mela","Chamba, Himachal","Week-long fair ending with the Minjar offering to the Ravi river.","/himachal-tour-packages/",False),
 ("2027-08-17","","Raksha Bandhan","All India","Long weekend around it is popular for short hill breaks.","/himachal-tour-package-5-nights-6-days/",True),
 ("2027-09-04","","Ganesh Chaturthi","Maharashtra · Goa","Goa's Chaturthi is quieter and more traditional than Mumbai's.","/goa-tour-packages/",True),
 ("2027-10-09","","Dussehra / Kullu Dussehra begins","Kullu, Himachal","Kullu's week starts on Vijayadashami.","/himachal-tour-packages/",True),
 ("2027-10-29","","Diwali","All India","Peak week for family trips.","/tours/",True),
]

U = 'https://suzutravels.com'
def a(path):  return path if path.startswith('http') else U + path
def esc(x):   return H.escape(x, quote=True)

# ---------------------------------------------------------------- CSS
CSS = r"""
/* ---------- 2026-10-09: traveller's toolkit ---------- */
.nz-tk{background:linear-gradient(180deg,var(--nz-snow) 0%,var(--nz-sky) 100%);padding:clamp(48px,7vw,84px) 0;content-visibility:auto;contain-intrinsic-size:1px 1100px;position:relative;overflow:hidden}
.nz-tk::before{content:"";position:absolute;inset:auto -10% -40px -10%;height:220px;background:radial-gradient(60% 100% at 50% 100%,rgba(31,122,69,.10),transparent 70%);pointer-events:none}
.nz-tk-tabs{display:flex;gap:8px;overflow-x:auto;scrollbar-width:none;padding:4px 2px 14px;margin:0 -2px}
.nz-tk-tabs::-webkit-scrollbar{display:none}
.nz-tk-tab{flex:none;display:inline-flex;align-items:center;gap:9px;border:1.5px solid var(--nz-line);background:#fff;color:var(--nz-ink);border-radius:999px;padding:10px 16px 10px 12px;font:700 .9rem var(--nz-body);cursor:pointer;min-height:44px;transition:border-color .2s,box-shadow .2s,transform .2s}
.nz-tk-tab svg{width:20px;height:20px;color:var(--c,var(--nz-emerald))}
.nz-tk-tab:hover{border-color:var(--c,var(--nz-emerald));transform:translateY(-1px)}
.nz-tk-tab[aria-selected="true"]{background:var(--nz-forest);border-color:var(--nz-forest);color:#fff;box-shadow:0 10px 24px -12px rgba(20,83,45,.7)}
.nz-tk-tab[aria-selected="true"] svg{color:var(--nz-gold)}
.nz-tk-panel{background:#fff;border:1.5px solid var(--nz-line);border-radius:var(--nz-r);box-shadow:var(--nz-shadow);padding:clamp(18px,3vw,30px);animation:nzTkIn .35s ease}
@keyframes nzTkIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
.nz-tk-panel h3{font-size:1.25rem;margin-bottom:4px}
.nz-tk-panel .sub{color:var(--nz-muted);font-size:.9rem;line-height:1.5;margin-bottom:18px}
.nz-tk-grid{display:grid;grid-template-columns:1.15fr .85fr;gap:24px}
@media (max-width:860px){.nz-tk-grid{grid-template-columns:1fr}}
.nz-tk-f{display:grid;gap:14px}
.nz-tk-f label,.nz-tk-f .lb{font-size:.78rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--nz-muted);display:block;margin-bottom:6px}
.nz-tk-f select,.nz-tk-f input[type="number"]{width:100%;border:1.5px solid var(--nz-line);border-radius:12px;padding:12px 14px;font:600 .95rem var(--nz-body);color:var(--nz-ink);background:#fff;min-height:46px}
.nz-tk-f select:focus,.nz-tk-f input:focus{border-color:var(--nz-emerald);outline:0;box-shadow:0 0 0 3px rgba(31,122,69,.15)}
.nz-tk-row{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.nz-tk-seg{display:flex;gap:6px;flex-wrap:wrap}
.nz-tk-seg button{flex:1 1 auto;border:1.5px solid var(--nz-line);background:#fff;border-radius:12px;padding:9px 10px;font:600 .84rem var(--nz-body);color:var(--nz-ink);cursor:pointer;min-height:44px;display:grid;gap:2px;text-align:center}
.nz-tk-seg button small{font-weight:500;color:var(--nz-muted);font-size:.72rem}
.nz-tk-seg button[aria-pressed="true"]{border-color:var(--nz-emerald);background:var(--nz-mint);box-shadow:inset 0 0 0 1px var(--nz-emerald)}
.nz-tk-step{display:flex;align-items:center;gap:0;border:1.5px solid var(--nz-line);border-radius:12px;overflow:hidden;width:fit-content}
.nz-tk-step button{width:46px;height:46px;border:0;background:var(--nz-mint);font:800 1.2rem var(--nz-body);color:var(--nz-ink);cursor:pointer}
.nz-tk-step output{min-width:64px;text-align:center;font:800 1.05rem var(--nz-display);color:var(--nz-ink)}
.nz-tk-out{background:linear-gradient(145deg,var(--nz-forest),#1F7A45 70%,#2B8A3E);color:#fff;border-radius:18px;padding:22px;display:grid;gap:14px;position:relative;overflow:hidden;align-self:start}
.nz-tk-out::after{content:"";position:absolute;right:-40px;top:-40px;width:180px;height:180px;border-radius:50%;background:radial-gradient(circle,rgba(212,160,23,.35),transparent 70%)}
.nz-tk-out .k{font-size:.74rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;opacity:.8}
.nz-tk-out .big{font:800 clamp(2rem,4vw,2.7rem)/1 var(--nz-display);color:#FFE08A;letter-spacing:-.02em}
.nz-tk-out .big small{font-size:.5em;color:#fff;opacity:.85;font-weight:600}
.nz-tk-out .ln{display:flex;justify-content:space-between;gap:12px;font-size:.92rem;border-top:1px solid rgba(255,255,255,.18);padding-top:10px}
.nz-tk-out .ln b{font-weight:800}
.nz-tk-out .tags{display:flex;flex-wrap:wrap;gap:6px}
.nz-tk-out .tag{font-size:.72rem;font-weight:700;background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.3);border-radius:999px;padding:4px 10px}
.nz-tk-out .nz-btn{justify-content:center}
.nz-tk-out .note{font-size:.76rem;opacity:.8;line-height:1.45}
.nz-tk-cta{display:flex;flex-wrap:wrap;gap:10px;position:relative;z-index:1}
.nz-tk-cta .nz-btn{flex:1 1 180px}
/* distance */
.nz-tk-map{position:relative;background:var(--nz-sky);border-radius:16px;padding:18px;min-height:150px;overflow:hidden}
.nz-tk-map svg{width:100%;height:auto;display:block}
.nz-tk-map .dash{stroke-dasharray:10 8;animation:nzDash 1.6s linear infinite}
@keyframes nzDash{to{stroke-dashoffset:-36}}
.nz-tk-map .car{animation:nzCar 3.2s ease-in-out infinite alternate}
@keyframes nzCar{from{offset-distance:0%}to{offset-distance:100%}}
.nz-tk-km{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:14px}
.nz-tk-km div{background:var(--nz-mint);border-radius:12px;padding:12px;text-align:center}
.nz-tk-km b{display:block;font:800 1.45rem/1.1 var(--nz-display);color:var(--nz-ink)}
.nz-tk-km span{font-size:.74rem;color:var(--nz-muted);font-weight:600}
.nz-tk-quick{display:flex;flex-wrap:wrap;gap:6px;margin-top:12px}
.nz-tk-note{font-size:.84rem;color:var(--nz-text);line-height:1.5;margin-top:12px}
/* packing */
.nz-tk-pk{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:14px;margin-top:16px}
.nz-tk-pk .g{background:var(--nz-snow);border:1.5px solid var(--nz-line);border-radius:14px;padding:12px 14px}
.nz-tk-pk h4{margin:0 0 8px;font:800 .8rem var(--nz-body);letter-spacing:.08em;text-transform:uppercase;color:var(--nz-emerald)}
.nz-tk-pk label{display:flex;gap:10px;align-items:flex-start;padding:7px 0;font-size:.9rem;line-height:1.35;cursor:pointer;border-top:1px dashed var(--nz-line)}
.nz-tk-pk label:first-of-type{border-top:0}
.nz-tk-pk input{width:20px;height:20px;accent-color:var(--nz-emerald);flex:none;margin-top:1px}
.nz-tk-pk input:checked+span{opacity:.55;color:var(--nz-muted)}
.nz-tk-prog{display:flex;align-items:center;gap:12px;margin-top:14px;font-size:.88rem;font-weight:700;color:var(--nz-ink)}
.nz-tk-prog .bar{flex:1;height:10px;border-radius:999px;background:var(--nz-mint);overflow:hidden}
.nz-tk-prog .bar i{display:block;height:100%;width:0;background:linear-gradient(90deg,var(--nz-emerald),var(--nz-gold));transition:width .3s ease}
/* help */
.nz-tk-hg{display:grid;grid-template-columns:repeat(auto-fit,minmax(270px,1fr));gap:14px}
.nz-tk-hc{--c:var(--nz-emerald);border:1.5px solid var(--nz-line);border-left:5px solid var(--c);border-radius:14px;padding:14px 16px;background:#fff;display:grid;gap:8px;align-content:start}
.nz-tk-hc h4{margin:0;font:800 1rem var(--nz-display);color:var(--nz-ink)}
.nz-tk-hc p{font-size:.86rem;line-height:1.5;color:var(--nz-text)}
.nz-tk-hc .ls{display:flex;flex-wrap:wrap;gap:6px 14px;font-size:.84rem;font-weight:700}
.nz-tk-hc .ls a{color:var(--c);text-decoration:none;border-bottom:1.5px solid color-mix(in srgb,var(--c) 40%,transparent)}
.nz-tk-hc .ls a[target]::after{content:" ↗";font-size:.8em}
.nz-tk-em{display:flex;flex-wrap:wrap;gap:10px;margin:18px 0 6px}
.nz-tk-em a{display:inline-flex;flex-direction:column;gap:2px;background:var(--nz-ink);color:#fff;border-radius:14px;padding:10px 14px;text-decoration:none;min-width:150px}
.nz-tk-em b{font:800 1.15rem var(--nz-display);color:#FFE08A}
.nz-tk-em span{font-size:.72rem;opacity:.85}
.nz-tk-links{display:flex;flex-wrap:wrap;gap:8px;margin-top:10px}
.nz-tk-links a{font-size:.82rem;font-weight:700;color:var(--nz-ink);background:var(--nz-mint);border-radius:999px;padding:7px 12px;text-decoration:none;min-height:36px;display:inline-flex;align-items:center}
.nz-tk-links a:hover{background:var(--nz-gold-soft)}
/* festivals */
.nz-tk-fl{display:grid;gap:10px}
.nz-tk-fe{display:grid;grid-template-columns:78px 1fr auto;gap:14px;align-items:center;border:1.5px solid var(--nz-line);border-radius:14px;padding:10px 14px 10px 10px;background:#fff;text-decoration:none;color:inherit;transition:border-color .2s,transform .2s}
.nz-tk-fe:hover{border-color:var(--nz-gold);transform:translateX(3px)}
.nz-tk-fe .d{background:var(--nz-gold-soft);border-radius:12px;text-align:center;padding:8px 4px;display:grid;line-height:1.05}
.nz-tk-fe .d b{font:800 1.35rem var(--nz-display);color:var(--nz-ink)}
.nz-tk-fe .d span{font-size:.7rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--nz-gold-deep)}
.nz-tk-fe h4{margin:0;font:800 1rem var(--nz-display);color:var(--nz-ink)}
.nz-tk-fe p{font-size:.82rem;color:var(--nz-muted);line-height:1.4}
.nz-tk-fe .in{font-size:.76rem;font-weight:800;color:var(--nz-emerald);white-space:nowrap;background:var(--nz-mint);border-radius:999px;padding:5px 10px}
.nz-tk-fe .in.soon{background:var(--nz-gold-soft);color:var(--nz-gold-deep)}
.nz-tk-fe .in.var{background:var(--nz-sky);color:var(--nz-glacier)}
@media (max-width:560px){.nz-tk-fe{grid-template-columns:64px 1fr}.nz-tk-fe .in{grid-column:2;justify-self:start}}
.nz-tk-foot{font-size:.78rem;color:var(--nz-muted);line-height:1.5;margin-top:14px}
"""

# ---------------------------------------------------------------- HTML
ICON = {
 'cost':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 4h12M6 8h12M9 20l9-12M6 12h6a3 3 0 0 1 0 6H9"/></svg>',
 'dist':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="5" cy="19" r="2"/><circle cx="19" cy="5" r="2"/><path d="M7 17c4-1 6-4 6-7 0-2 1-3 4-3"/></svg>',
 'pack':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M3 12h18"/></svg>',
 'help':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6l-8-3Z"/><path d="M9 12l2 2 4-4"/></svg>',
 'fest':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4M8 15h3"/></svg>',
}
TABS = [('cost','Trip cost','कितना लगेगा?','var(--nz-gold-deep)'),('dist','Distance & time','दूरी','var(--nz-glacier)'),('pack','Packing list','सामान','var(--nz-leaf)'),('help','Permits & help','परमिट','var(--nz-saffron)'),('fest','Festivals','त्योहार','var(--nz-rose)')]

def opt_trips():
    out = []
    for t in sorted(PRICED, key=lambda t: t['price']):
        out.append('<option value="%s">%s — %dD/%dN from %s · ₹%s</option>' % (esc(t['slug']), esc(t['title']), t['days'], t['nights'], esc(t['start']), format(t['price'], ',')))
    return ''.join(out)

MONTHS = D['months']
import datetime
today = datetime.date.today()
def opt_months():
    out = []
    for i in range(12):
        m = (today.month - 1 + i) % 12; y = today.year + ((today.month - 1 + i) // 12)
        out.append('<option value="%d-%02d">%s %d</option>' % (y, m + 1, MONTHS[m], y))
    return ''.join(out)

def opt_cities(sel):
    return ''.join('<option value="%s"%s>%s</option>' % (esc(c), ' selected' if c == sel else '', esc(c)) for c in CITIES)

def pack_html():
    seg = ''.join('<button type="button" data-k="%s" aria-pressed="%s">%s</button>' % (k, 'true' if k == 'snow' else 'false', esc(v[0])) for k, v in PACK.items())
    return seg

def help_html():
    cards = []
    for title, key, col, body, links in HELP:
        ls = ''.join('<a href="%s"%s>%s</a>' % (esc(a(u)), ' target="_blank" rel="noopener"' if ext else '', esc(lab)) for u, lab, ext in links)
        cards.append('<div class="nz-tk-hc" style="--c:%s"><h4>%s</h4><p>%s</p><div class="ls">%s</div></div>' % (col, esc(title), esc(body), ls))
    em = ''.join('<a href="tel:%s"><b>%s</b><span>%s</span></a>' % (re.sub(r'[^\d+]', '', n), esc(n), esc(l)) for n, l in EMERG)
    lk = ''.join('<a href="%s" target="_blank" rel="noopener">%s ↗</a>' % (esc(u), esc(l)) for u, l in LINKS)
    return '<div class="nz-tk-hg">%s</div><p class="lb" style="margin-top:20px">Emergency numbers — save these</p><div class="nz-tk-em">%s</div><p class="lb" style="margin-top:14px">Official links</p><div class="nz-tk-links">%s</div><p class="nz-tk-foot">Permit rules, fees and dates change each season — the official portals above are the final word; we re-check this card before every departure.</p>' % (''.join(cards), em, lk)

FEST_JSON = json.dumps([{'s': f[0], 'e': f[1], 't': f[2], 'w': f[3], 'n': f[4], 'u': a(f[5]), 'x': f[6]} for f in FEST], ensure_ascii=False)
DIST_JSON = json.dumps([{'a': d[0], 'b': d[1], 'km': d[2], 'h': d[3], 'n': d[4], 'u': a(d[5]) if d[5] else ''} for d in DIST], ensure_ascii=False)
PACK_JSON = json.dumps(PACK, ensure_ascii=False)

def fest_static():
    """Crawlable list rendered server-side (JS re-sorts it for 'today')."""
    out = []
    for s0, e0, t, w, n, u, fixed in FEST:
        d = s0.split('-')
        dd = d[2] if len(d) == 3 else '—'
        mm = MONTHS[int(d[1]) - 1][:3]
        out.append('<a class="nz-tk-fe" href="%s" data-s="%s"><div class="d"><b>%s</b><span>%s %s</span></div><div><h4>%s</h4><p>%s · %s</p></div><span class="in%s">%s</span></a>' % (
            esc(u), s0, dd, mm, d[0][2:], esc(t), esc(w), esc(n), '' if fixed else ' var', 'Fixed date' if fixed else 'Dates vary'))
    return ''.join(out)

SECTION = ('<section class="nz nz-tk" id="nz-toolkit" aria-labelledby="nz-tk-h"><div class="nz-wrap">'
 '<div class="nz-head"><div class="st"><span class="nz-eyebrow">Traveller’s toolkit · यात्रा किट</span><h2 id="nz-tk-h">Plan smarter, <span>before you book</span></h2></div>'
 '<p>Five quick tools from our ground team: a cost estimate on the same rules as our trip sheet, road distances with honest hill timings, a packing list you can tick off, the permits and numbers that matter, and the festivals worth planning around.</p></div>'
 '<div class="nz-tk-tabs" role="tablist" aria-label="Toolkit">' +
 ''.join('<button class="nz-tk-tab" role="tab" id="nz-tk-t-%s" aria-controls="nz-tk-p-%s" aria-selected="%s" style="--c:%s">%s<span>%s</span> <span lang="hi" style="opacity:.75;font-weight:500">%s</span></button>' % (k, k, 'true' if i == 0 else 'false', col, ICON[k], lab, hi) for i, (k, lab, hi, col) in enumerate(TABS)) +
 '</div>'
 # ---- cost
 '<div class="nz-tk-panel" role="tabpanel" id="nz-tk-p-cost" aria-labelledby="nz-tk-t-cost"><h3>How much will my trip cost?</h3><p class="sub">Pick a priced trip, your group, hotel level and month. The estimate uses the page’s starting rate and the same hotel and season rules as our trip sheet — the final quote is to your exact dates and rooms.</p>'
 '<div class="nz-tk-grid"><form class="nz-tk-f" id="nz-tk-cf" onsubmit="return false">'
 '<div><label for="nz-tk-trip">Trip</label><select id="nz-tk-trip">' + opt_trips() + '</select></div>'
 '<div class="nz-tk-row"><div><span class="lb">Travellers</span><div class="nz-tk-step"><button type="button" data-d="-1" aria-label="Fewer travellers">−</button><output id="nz-tk-n">2</output><button type="button" data-d="1" aria-label="More travellers">+</button></div></div>'
 '<div><label for="nz-tk-m">Travel month</label><select id="nz-tk-m">' + opt_months() + '</select></div></div>'
 '<div><span class="lb">Hotel level</span><div class="nz-tk-seg" id="nz-tk-tier"><button type="button" data-t="0" aria-pressed="true">Deluxe<small>good 3★</small></button><button type="button" data-t="1" aria-pressed="false">Super Deluxe<small>4★ · ×1.18</small></button><button type="button" data-t="2" aria-pressed="false">Luxury<small>5★ · ×1.35</small></button></div></div>'
 '</form><div class="nz-tk-out" id="nz-tk-co" aria-live="polite"></div></div></div>'
 # ---- distance
 '<div class="nz-tk-panel" role="tabpanel" id="nz-tk-p-dist" aria-labelledby="nz-tk-t-dist" hidden><h3>How far is it, really?</h3><p class="sub">Road distance and realistic driving time on hill roads — not the map’s optimistic number. Every pair links to the cab page where we run it.</p>'
 '<div class="nz-tk-grid"><div class="nz-tk-f"><div class="nz-tk-row"><div><label for="nz-tk-from">From</label><select id="nz-tk-from">' + opt_cities('Delhi') + '</select></div><div><label for="nz-tk-to">To</label><select id="nz-tk-to">' + opt_cities('Manali') + '</select></div></div>'
 '<div class="nz-tk-map" id="nz-tk-map" aria-hidden="true"></div><div class="nz-tk-km" id="nz-tk-km"></div><p class="nz-tk-note" id="nz-tk-dn"></p>'
 '<div class="nz-tk-quick" id="nz-tk-dq"></div></div><div class="nz-tk-out" id="nz-tk-do"></div></div></div>'
 # ---- packing
 '<div class="nz-tk-panel" role="tabpanel" id="nz-tk-p-pack" aria-labelledby="nz-tk-t-pack" hidden><h3>What should I pack?</h3><p class="sub">Choose the kind of trip; tick things off as you pack. Your ticks are remembered on this device. Snow suits and boots can be rented in Manali — no need to buy.</p>'
 '<div class="nz-tk-seg" id="nz-tk-pkk">' + pack_html() + '</div><div class="nz-tk-prog"><span id="nz-tk-pc">0 of 0 packed</span><div class="bar"><i id="nz-tk-pb"></i></div></div><div class="nz-tk-pk" id="nz-tk-pkl"></div>'
 '<div class="nz-tk-cta" style="margin-top:16px"><button class="nz-btn nz-btn-line" type="button" id="nz-tk-pcopy">Copy list</button><a class="nz-btn nz-btn-wa" id="nz-tk-pwa" href="https://wa.me/917087488961" target="_blank" rel="noopener">Send list to WhatsApp</a><button class="nz-btn nz-btn-line" type="button" id="nz-tk-preset">Reset ticks</button></div>'
 '<p class="nz-tk-foot">Related: <a href="' + a('/adventure/snow-suit-and-boots-on-rent-manali/') + '">snow suit & boots on rent in Manali</a> · <a href="' + a('/complete-ladakh-packing-list-essential-gear-for-a-safe-high-altitude-trip/') + '">Ladakh packing list</a> · <a href="' + a('/himachal-snowfall-winter-2026-27/') + '">snowfall calendar 2026–27</a></p></div>'
 # ---- help
 '<div class="nz-tk-panel" role="tabpanel" id="nz-tk-p-help" aria-labelledby="nz-tk-t-help" hidden><h3>Permits, registrations and who to call</h3><p class="sub">The paperwork that trips up first-time hill travellers, with the official portals — and the numbers to keep on your phone.</p>' + help_html() + '</div>'
 # ---- festivals
 '<div class="nz-tk-panel" role="tabpanel" id="nz-tk-p-fest" aria-labelledby="nz-tk-t-fest" hidden><h3>Festivals &amp; events — next 12 months</h3><p class="sub">Dates worth planning a trip around (or avoiding, if you want quiet roads). Fixed dates are confirmed; “dates vary” events are announced each year by the organisers.</p>'
 '<div class="nz-tk-fl" id="nz-tk-fl">' + fest_static() + '</div><p class="nz-tk-foot">Hotel prices rise 20–40% in festival weeks around Diwali, Christmas–New Year and long weekends — lock your rate early with a token amount.</p></div>'
 '</div></section>')

# ---------------------------------------------------------------- JS
JS = r"""<script id="nz-tk-js">
(function(){'use strict';
var S=document.getElementById('nz-toolkit');if(!S)return;
function $(q,c){return (c||S).querySelector(q)}function $$(q,c){return Array.prototype.slice.call((c||S).querySelectorAll(q))}
var D=JSON.parse(document.getElementById('nz-data').textContent),BY={};D.trips.forEach(function(t){BY[t.slug]=t});
var DIST=__DIST__,FEST=__FEST__,PACK=__PACK__;
var WA='https://wa.me/917087488961?text=',reduce=window.matchMedia('(prefers-reduced-motion:reduce)').matches;
var TIERS=[["Deluxe",1,"good 3★ hotels"],["Super Deluxe",1.18,"4★ hotels"],["Luxury",1.35,"5★ hotels & resorts"]],PEAK=1.25;
function isPeakM(ym){var m=+ym.split('-')[1];return m===4||m===5||m===6||m===10}
function edgeM(ym){var m=+ym.split('-')[1];return m===3?'Peak rates apply from 15 March.':m===12?'Peak rates apply from 20 December.':m===1?'Peak rates until 5 January.':''}
function inr(n){return '₹'+Math.round(n).toLocaleString('en-IN')}
function toast(m){var t=document.getElementById('nz-toast');if(!t)return;t.textContent=m;t.classList.add('on');clearTimeout(t._x);t._x=setTimeout(function(){t.classList.remove('on')},2200)}
function track(ev){try{if(window.gtag)gtag('event',ev,{event_category:'toolkit'})}catch(e){}}
/* tabs */
var tabs=$$('.nz-tk-tab'),panels=$$('.nz-tk-panel');
function show(k){tabs.forEach(function(t){var on=t.id==='nz-tk-t-'+k;t.setAttribute('aria-selected',on?'true':'false');t.tabIndex=on?0:-1});panels.forEach(function(p){p.hidden=p.id!=='nz-tk-p-'+k});try{localStorage.setItem('nz-tk-tab',k)}catch(e){}track('toolkit_'+k)}
tabs.forEach(function(t,i){t.addEventListener('click',function(){show(t.id.replace('nz-tk-t-',''))});t.addEventListener('keydown',function(e){if(e.key==='ArrowRight'||e.key==='ArrowLeft'){e.preventDefault();var j=(i+(e.key==='ArrowRight'?1:tabs.length-1))%tabs.length;tabs[j].focus();tabs[j].click()}})});
function fromHash(){var m=(location.hash||'').match(/^#toolkit-(cost|dist|pack|help|fest)$/);if(m){show(m[1]);S.scrollIntoView({block:'start'})}return m}
var m0=fromHash();window.addEventListener('hashchange',fromHash);
/* ---- cost ---- */
(function(){var sel=$('#nz-tk-trip'),mon=$('#nz-tk-m'),out=$('#nz-tk-co'),nO=$('#nz-tk-n'),n=2,tier=0;
  function anim(el,from,to){if(reduce||!el){if(el)el.textContent=inr(to);return}var t0=performance.now(),d=500;(function f(t){var p=Math.min(1,(t-t0)/d),k=1-Math.pow(1-p,3);el.textContent=inr(from+(to-from)*k);if(p<1)requestAnimationFrame(f)})(t0)}
  var last=0;
  function paint(){var t=BY[sel.value];if(!t)return;var pk=isPeakM(mon.value),tm=t.tiers?TIERS[tier][1]:1,pp=Math.round(t.price*tm*(pk?PEAK:1)),tot=pp*n,perday=Math.round(pp/t.days);
    var ym=mon.value.split('-'),mname=D.months[+ym[1]-1]+' '+ym[0];
    var msg='Hi Suzu Travels, I used the cost tool on your website. Trip: '+t.title+' ('+t.days+'D/'+t.nights+'N from '+t.start+'), '+n+' traveller'+(n>1?'s':'')+', '+TIERS[tier][0]+' hotels, '+mname+'. Estimate shown: '+inr(tot)+' total. Please send me the exact quote.';
    out.innerHTML='<div><div class="k">Estimated total · '+n+' traveller'+(n>1?'s':'')+'</div><div class="big" id="nz-tk-big">'+inr(last||tot)+'</div></div>'+
      '<div class="ln"><span>Per person</span><b>'+inr(pp)+'</b></div><div class="ln"><span>Per person per day</span><b>'+inr(perday)+' × '+t.days+' days</b></div><div class="ln"><span>Hotels · season</span><b>'+TIERS[tier][0]+(t.tiers?'':' (fixed)')+' · '+(pk?'peak +25%':'regular')+'</b></div>'+
      '<div class="tags"><span class="tag">'+t.days+'D / '+t.nights+'N</span><span class="tag">From '+t.start+'</span><span class="tag">'+(t.top?t.top[0]+' · '+t.top[1].toLocaleString('en-IN')+' m':'')+'</span><span class="tag">Cab · hotels · breakfast · tour manager</span></div>'+
      '<div class="nz-tk-cta"><a class="nz-btn nz-btn-gold" href="'+WA+encodeURIComponent(msg)+'" target="_blank" rel="noopener">Get exact quote on WhatsApp</a><a class="nz-btn nz-btn-ghost" href="#trip-'+t.slug+'">View itinerary</a></div>'+
      '<p class="note">'+(edgeM(mon.value)?edgeM(mon.value)+' ':'')+(t.tiers?'':'This trip is priced for one hotel standard; ')+'Book with a small token to lock today’s rate; balance later. Flights and personal expenses not included.</p>';
    anim($('#nz-tk-big'),last||tot*0.9,tot);last=tot}
  sel.addEventListener('change',paint);mon.addEventListener('change',paint);
  $$('#nz-tk-cf .nz-tk-step button').forEach(function(b){b.addEventListener('click',function(){n=Math.max(1,Math.min(20,n+ +b.dataset.d));nO.textContent=n;paint()})});
  $$('#nz-tk-tier button').forEach(function(b){b.addEventListener('click',function(){tier=+b.dataset.t;$$('#nz-tk-tier button').forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false')});paint()})});
  out.addEventListener('click',function(e){var l=e.target.closest('a[href^="#trip-"]');if(l){e.preventDefault();location.hash=l.getAttribute('href')}});
  paint()})();
/* ---- distance ---- */
(function(){var F=$('#nz-tk-from'),T=$('#nz-tk-to'),map=$('#nz-tk-map'),km=$('#nz-tk-km'),note=$('#nz-tk-dn'),out=$('#nz-tk-do'),q=$('#nz-tk-dq');
  function find(a,b){for(var i=0;i<DIST.length;i++){var d=DIST[i];if((d.a===a&&d.b===b)||(d.a===b&&d.b===a))return d}return null}
  function svg(a,b){return '<svg viewBox="0 0 400 130" role="img"><defs><linearGradient id="nzTkSky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#E3F1FB"/><stop offset="1" stop-color="#F7FAF6"/></linearGradient></defs><rect width="400" height="130" fill="url(#nzTkSky)" rx="12"/>'+
    '<path d="M0 100 L60 55 L95 80 L140 35 L185 75 L225 50 L265 85 L310 40 L350 70 L400 45 V130 H0Z" fill="#CFE3D4"/><path d="M0 110 L50 85 L110 100 L170 70 L230 95 L300 75 L360 98 L400 80 V130 H0Z" fill="#B7D3BF"/>'+
    '<path id="nzTkRoute" d="M40 100 C 120 100, 150 40, 200 60 S 300 110, 360 42" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round"/><path class="dash" d="M40 100 C 120 100, 150 40, 200 60 S 300 110, 360 42" fill="none" stroke="#1F7A45" stroke-width="3" stroke-linecap="round"/>'+
    '<circle cx="40" cy="100" r="7" fill="#D4A017" stroke="#fff" stroke-width="3"/><circle cx="360" cy="42" r="7" fill="#E8590C" stroke="#fff" stroke-width="3"/>'+
    '<g class="car" style="offset-path:path(\'M40 100 C 120 100, 150 40, 200 60 S 300 110, 360 42\')"><rect x="-9" y="-6" width="18" height="12" rx="3" fill="#14532D"/><circle cx="-5" cy="7" r="2.5" fill="#10261A"/><circle cx="5" cy="7" r="2.5" fill="#10261A"/></g>'+
    '<text x="40" y="122" font-size="11" font-weight="700" fill="#10261A" text-anchor="start" font-family="system-ui">'+a+'</text><text x="360" y="28" font-size="11" font-weight="700" fill="#10261A" text-anchor="end" font-family="system-ui">'+b+'</text></svg>'}
  function paint(){var a=F.value,b=T.value,d=find(a,b);map.innerHTML=svg(a,b);
    if(!d||a===b){km.innerHTML='';note.textContent=a===b?'Pick two different places.':'We have not measured this pair yet — ask us and we will quote it with timings.';out.innerHTML='<div><div class="k">Cab for this route</div><div class="big">On request</div></div><div class="nz-tk-cta"><a class="nz-btn nz-btn-gold" href="'+WA+encodeURIComponent('Hi Suzu Travels, I need a cab from '+a+' to '+b+'. Please share distance, time and fare.')+'" target="_blank" rel="noopener">Ask on WhatsApp</a><a class="nz-btn nz-btn-ghost" href="https://suzutravels.com/cabs/">All cab routes</a></div>';return}
    km.innerHTML='<div><b>'+d.km.toLocaleString('en-IN')+'</b><span>km by road</span></div><div><b>'+d.h+'</b><span>driving time</span></div><div><b>'+(d.km>300?'2':'1')+'</b><span>'+(d.km>300?'meal halts':'tea halt')+'</span></div>';
    note.textContent=d.n+' Times are for a private cab in normal conditions; add 1–2 h in snow, rain or holiday traffic.';
    out.innerHTML='<div><div class="k">'+a+' → '+b+'</div><div class="big">'+d.km.toLocaleString('en-IN')+' <small>km · '+d.h+'</small></div></div><div class="ln"><span>Best for</span><b>'+(d.km>400?'Night drive or overnight halt':d.km>200?'Day drive, start early':'Easy half-day')+'</b></div><div class="ln"><span>Our fleet</span><b>Sedan · Innova Crysta · Tempo Traveller</b></div>'+
      '<div class="nz-tk-cta">'+(d.u?'<a class="nz-btn nz-btn-gold" href="'+d.u+'">Fares & book this route</a>':'<a class="nz-btn nz-btn-gold" href="https://suzutravels.com/cabs/">See cab fares</a>')+'<a class="nz-btn nz-btn-ghost" href="'+WA+encodeURIComponent('Hi Suzu Travels, I need a cab from '+a+' to '+b+' ('+d.km+' km). Please share the fare.')+'" target="_blank" rel="noopener">Quote on WhatsApp</a></div><p class="note">Transparent fares: tolls, parking and driver allowance are listed on the route page; no hidden night charges on our routes.</p>'}
  F.addEventListener('change',paint);T.addEventListener('change',paint);
  var Q=[['Delhi','Manali'],['Delhi','Shimla'],['Chandigarh','Manali'],['Shimla','Manali'],['Manali','Kaza'],['Jammu','Srinagar'],['Haridwar','Kedarnath (Gaurikund)'],['Delhi','Dharamshala']];
  q.innerHTML=Q.map(function(p){return '<button class="nz-chip" type="button" data-a="'+p[0]+'" data-b="'+p[1]+'">'+p[0]+' → '+p[1]+'</button>'}).join('');
  $$('button',q).forEach(function(b){b.addEventListener('click',function(){F.value=b.dataset.a;T.value=b.dataset.b;paint()})});
  paint()})();
/* ---- packing ---- */
(function(){var kind='snow',list=$('#nz-tk-pkl'),pc=$('#nz-tk-pc'),pb=$('#nz-tk-pb'),K={};
  try{K=JSON.parse(localStorage.getItem('nz-tk-pack')||'{}')||{}}catch(e){K={}}
  function save(){try{localStorage.setItem('nz-tk-pack',JSON.stringify(K))}catch(e){}}
  function paint(){var P=PACK[kind];list.innerHTML=P[1].map(function(g,gi){return '<div class="g"><h4>'+g[0]+'</h4>'+g[1].map(function(it,i){var id=kind+'-'+gi+'-'+i;return '<label><input type="checkbox" data-id="'+id+'"'+(K[id]?' checked':'')+'><span>'+it+'</span></label>'}).join('')+'</div>'}).join('');prog()}
  function prog(){var all=$$('input',list),on=all.filter(function(i){return i.checked}).length;pc.textContent=on+' of '+all.length+' packed';pb.style.width=(all.length?on/all.length*100:0)+'%'}
  list.addEventListener('change',function(e){var i=e.target;if(i.dataset.id){if(i.checked)K[i.dataset.id]=1;else delete K[i.dataset.id];save();prog()}});
  $$('#nz-tk-pkk button').forEach(function(b){b.addEventListener('click',function(){kind=b.dataset.k;$$('#nz-tk-pkk button').forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false')});paint()})});
  function text(){var P=PACK[kind],s='Packing list — '+P[0]+' (Suzu Travels)\n';P[1].forEach(function(g,gi){s+='\n'+g[0].toUpperCase()+'\n';g[1].forEach(function(it,i){s+=(K[kind+'-'+gi+'-'+i]?'☑ ':'☐ ')+it+'\n'})});return s+'\nhttps://suzutravels.com/#toolkit-pack'}
  $('#nz-tk-pcopy').addEventListener('click',function(){var t=text();if(navigator.clipboard&&navigator.clipboard.writeText)navigator.clipboard.writeText(t).then(function(){toast('List copied')},function(){toast('Could not copy')});else toast('Copy not supported here')});
  $('#nz-tk-pwa').addEventListener('click',function(){this.href='https://wa.me/?text='+encodeURIComponent(text())});
  $('#nz-tk-preset').addEventListener('click',function(){Object.keys(K).forEach(function(k){if(k.indexOf(kind+'-')===0)delete K[k]});save();paint()});
  paint()})();
/* ---- festivals: sort for today, hide past, show countdown ---- */
(function(){var L=$('#nz-tk-fl'),now=new Date();now.setHours(0,0,0,0);var MN=D.months;
  function dt(s,end){var p=s.split('-');return p.length===3?new Date(+p[0],+p[1]-1,+p[2]):new Date(+p[0],+p[1]-1,end?28:1)}
  var items=FEST.map(function(f){var s=dt(f.s),e=f.e?dt(f.e,true):(f.s.length===7?dt(f.s,true):s);return {f:f,s:s,e:e}}).filter(function(x){return x.e>=now}).sort(function(a,b){return a.s-b.s}).slice(0,12);
  if(!items.length)return;
  L.innerHTML=items.map(function(x){var f=x.f,p=f.s.split('-'),days=Math.round((x.s-now)/864e5),live=x.s<=now&&x.e>=now;
    var when=live?'Now on':days<=45?'In '+days+' days':f.x?'Fixed date':'Dates vary',cls=live||days<=45?' soon':f.x?'':' var';
    return '<a class="nz-tk-fe" href="'+f.u+'"><div class="d"><b>'+(p.length===3?+p[2]:'—')+'</b><span>'+MN[+p[1]-1].slice(0,3)+' '+p[0].slice(2)+'</span></div><div><h4>'+f.t+'</h4><p>'+f.w+' · '+f.n+'</p></div><span class="in'+cls+'">'+when+'</span></a>'}).join('')})();
try{var k=localStorage.getItem('nz-tk-tab');if(k&&!m0&&document.getElementById('nz-tk-t-'+k))show(k)}catch(e){}
})();
</script>
"""
JS = JS.replace('__DIST__', DIST_JSON).replace('__FEST__', FEST_JSON).replace('__PACK__', PACK_JSON)

# ---------------------------------------------------------------- apply
# 1. CSS -> end of the nature style block (after the 2026-10-08 additions)
i = once(s, '/* ---------- 2026-10-08: compare trips + explore-more links ---------- */')
j = s.index('</style>', i)
s = s[:j] + CSS + s[j:]
# 2. section before #when-to-go (i.e. right after #nz-explore)
i = once(s, '<section class="szx-mo" id="when-to-go"')
s = s[:i] + SECTION + '\n' + s[i:]
# 3. JS before the weather widget script
i = once(s, '<script id="nzw-js">')
s = s[:i] + JS + s[i:]
# 4. hero rAF gating
old = "requestAnimationFrame(tick);\n  }\n  title(0);cur=0;requestAnimationFrame(tick);"
new = ("if(rafOn)requestAnimationFrame(tick);\n  }\n  var rafOn=true,heroIn=true;function rafGo(){if(!rafOn&&heroIn&&!document.hidden){rafOn=true;requestAnimationFrame(tick)}}\n"
       "  V.addEventListener('timeupdate',rafGo);V.addEventListener('play',rafGo);\n"
       "  if('IntersectionObserver' in window)new IntersectionObserver(function(es){heroIn=es[0].isIntersecting;if(!heroIn)rafOn=false;else rafGo()}).observe(H);\n"
       "  document.addEventListener('visibilitychange',function(){if(document.hidden)rafOn=false;else rafGo()});\n"
       "  title(0);cur=0;requestAnimationFrame(tick);")
once(s, old); s = s.replace(old, new)
# in tick: stop when paused (lite mode keeps its own seek loop; 'timeupdate' restarts us)
old2 = "function tick(){\n    var t=V.currentTime||0, i=sceneAt(t);"
new2 = "function tick(){\n    if(V.paused&&!lite){rafOn=false;return}\n    var t=V.currentTime||0, i=sceneAt(t);"
once(s, old2); s = s.replace(old2, new2)
# 5. szx <style> -> head
i = once(s, '<style id="suzu-redesign-2026-09">'); j = s.index('</style>', i) + len('</style>')
blk = s[i:j]; s = s[:i] + s[j:]
k = once(s, '</head>'); s = s[:k] + blk + '\n' + s[k:]

open(dst, 'w', encoding='utf-8').write(s)
print('ok', len(s), 'priced', len(PRICED), 'dist', len(DIST), 'fest', len(FEST))
