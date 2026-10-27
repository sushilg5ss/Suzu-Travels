# -*- coding: utf-8 -*-
"""Suzu Cab Kit — single source of truth for fleet, fares, places and page content.
Edit fares here (FLEET rates / ROUTE factors) and rebuild; every page and the on-page calculator update together.
Fare rule (Sushil approved research-based fares, 30 Sep 2026; one-way rates and minimums raised to the premium-operator level on 17 Oct 2026 at Sushil's direction):
  one-way  = max(min_fare, dist_km * ow_rate * route_factor) rounded up to the next ...99
  round trip / multi-day = max(2*dist, 250*days) * hire_rate + driver allowance per night
Fares are indicative starting prices (off-season). Tolls, parking and state entry tax/permits are extra at actuals.
"""
import math

PHONE = "917087488961"
PHONE_TXT = "+91 70874 88961"
REG = "HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022"
RATING = "★ 4.7 · 377 Google reviews"   # same phrase the Suzu Live Reviews plugin rewrites site-wide

# Fleet-age tiers (Sushil, 16 Oct 2026): the engine fare is the Standard tier; Prime (newest cars) +15 %, Saver (older cars) -8 %.
# Customer-facing names chosen over A/B/C. mult applies to the final one-way / round-trip amount (rounded up to ...99).
TIERS = [
    dict(id="prime", name="Prime", sub="2023 & newer · under 3 years old", mult=1.15, badge="Latest models"),
    dict(id="standard", name="Standard", sub="3–5 years old · well maintained", mult=1.0, badge="Most booked"),
    dict(id="saver", name="Saver", sub="5–10 years old · budget friendly", mult=0.92, badge="Best price"),
]
TIER_BY_ID = {t["id"]: t for t in TIERS}

# Vehicle types used by the fleet filters (id, label)
VTYPES = [("hatchback", "Hatchback"), ("sedan", "Sedan"), ("muv", "MUV / 6–7 seater"), ("suv", "Premium SUV"),
          ("tempo", "Tempo Traveller"), ("van", "Luxury van"), ("bus", "Bus / coach")]

# quote=True vehicles have no per-km rate on the site (price varies too much) — they appear in the fleet gallery with "Get quote" only.
FLEET = [
    dict(id="hatch", name="Hatchback", model="Swift / Celerio / WagonR class", type="hatchback", seats=4, bags="2 small bags", fuel="Petrol / CNG",
         ow=13, hire=11, min=2199, night=400, best="Couples & short transfers", page=None,
         photo_alt="Maruti Suzuki Celerio hatchback, the class of car used for Suzu hatchback cabs"),
    dict(id="sedan", name="Sedan", model="Dzire / Etios / Aura", type="sedan", seats=4, bags="3 bags", fuel="Petrol / CNG",
         ow=15, hire=12, min=2499, night=400, best="Couples & small families, highway runs", page=None,
         photo_alt="Maruti Suzuki Dzire sedan taxi, 4 seats with boot space for 3 bags"),
    dict(id="ertiga", name="Maruti Ertiga", model="6-seater MUV", type="muv", seats=6, bags="3 bags + carrier", fuel="Petrol / CNG",
         ow=19, hire=14, min=3299, night=400, best="Families of 5–6 on a budget", page=None,
         photo_alt="Maruti Suzuki Ertiga 6-seater MUV used for family cab trips"),
    dict(id="carens", name="Kia Carens", model="6-seater premium MPV", type="muv", seats=6, bags="4 bags", fuel="Diesel / Petrol",
         ow=22, hire=16, min=3799, night=400, best="Families who want extra comfort", page=None,
         photo_alt="Kia Carens 6-seater MPV with captain seats"),
    dict(id="crysta", name="Toyota Innova Crysta", model="6+1 / 7-seater SUV", type="muv", seats=7, bags="5 bags", fuel="Diesel",
         ow=26, hire=19, min=4499, night=400, best="Hill circuits, senior citizens, groups of 6–7", page="innova-crysta-on-rent",
         photo_alt="Toyota Innova Crysta, the most booked 7-seater for Himachal hill roads"),
    dict(id="hycross", name="Toyota Innova Hycross", model="7-seater premium MPV", type="muv", seats=7, bags="5 bags", fuel="Petrol hybrid",
         ow=30, hire=22, min=4999, night=400, best="Premium family trips, quieter and roomier than the Crysta", page=None,
         photo_alt="Toyota Innova Hycross premium 7-seater MPV"),
    dict(id="fortuner", name="Toyota Fortuner", model="7-seater premium SUV", type="suv", seats=6, bags="4 bags", fuel="Diesel",
         ow=42, hire=32, min=7499, night=500, best="VIP transfers, weddings, Leh & Spiti roads", page=None,
         photo_alt="Toyota Fortuner premium SUV for VIP transfers and high-altitude roads"),
    dict(id="tempo", name="Tempo Traveller", model="Force Traveller 12–14 seater", type="tempo", seats=12, bags="10 bags", fuel="Diesel",
         ow=51, hire=26, min=7499, night=500, best="Groups, pilgrimages, office trips", page="tempo-traveller-hire-delhi",
         photo_alt="Force Traveller 12-seater Tempo Traveller for group trips"),
    dict(id="tempo17", name="Tempo Traveller 17-seater", model="Force Traveller 17 seater", type="tempo", seats=17, bags="14 bags", fuel="Diesel",
         ow=52, hire=30, min=8499, night=500, best="Bigger groups, Char Dham, school & office tours", page="tempo-traveller-hire-delhi",
         photo_alt="17-seater Force Traveller Tempo Traveller for large groups"),
    dict(id="urbania", name="Force Urbania", model="Luxury van, up to 17 seats", type="van", seats=17, bags="12+ bags", fuel="Diesel",
         ow=53, hire=36, min=10999, night=500, best="Premium group transfers & weddings", page=None,
         photo_alt="Force Urbania luxury van, up to 17 reclining seats"),
    dict(id="minibus", name="Mini coach 26-seater", model="AC mini bus, 2+2 seats", type="bus", seats=26, bags="Luggage hold", fuel="Diesel",
         ow=None, hire=None, min=None, night=600, best="Wedding parties, corporate outings, school trips", page=None, quote=True,
         photo_alt="26-seater AC mini coach for group tours"),
    dict(id="bus35", name="AC coach 35-seater", model="2+2 push-back seats", type="bus", seats=35, bags="Luggage hold", fuel="Diesel",
         ow=None, hire=None, min=None, night=600, best="Large groups, yatras and corporate tours", page=None, quote=True,
         photo_alt="35-seater AC coach with push-back seats"),
    dict(id="bus45", name="Luxury coach 45-seater", model="Volvo / Scania class", type="bus", seats=45, bags="Luggage hold", fuel="Diesel",
         ow=None, hire=None, min=None, night=600, best="Big groups between Delhi, Chandigarh and the hills", page=None, quote=True,
         photo_alt="45-seater luxury Volvo-class coach"),
]
PRICED = [v for v in FLEET if not v.get("quote")]
FLEET_BY_ID = {v["id"]: v for v in FLEET}


def r99(x):
    return int(math.ceil(x / 100.0) * 100 - 1)


def oneway(vid, dist, factor, tier="standard"):
    v = FLEET_BY_ID[vid]
    if v.get("quote"):
        return None
    base = max(v["min"], r99(dist * v["ow"] * factor))
    m = TIER_BY_ID[tier]["mult"]
    return base if m == 1 else r99(base * m)


def inr(n):
    s = str(int(n))
    if len(s) <= 3:
        return "₹" + s
    last3, rest = s[-3:], s[:-3]
    parts = []
    while len(rest) > 2:
        parts.insert(0, rest[-2:])
        rest = rest[:-2]
    if rest:
        parts.insert(0, rest)
    return "₹" + ",".join(parts) + "," + last3


# lat, lon — used by the route-map videos
PLACES = {
    "Delhi": (28.61, 77.21), "Murthal": (29.03, 77.07), "Panipat": (29.39, 76.97), "Karnal": (29.69, 76.99),
    "Kurukshetra": (29.97, 76.88), "Ambala": (30.38, 76.78), "Zirakpur": (30.64, 76.82), "Chandigarh": (30.73, 76.78),
    "Kalka": (30.84, 76.94), "Parwanoo": (30.84, 76.96), "Dharampur": (30.90, 77.02), "Solan": (30.90, 77.10),
    "Kandaghat": (30.97, 77.11), "Shimla": (31.10, 77.17), "Kufri": (31.10, 77.26), "Kharar": (30.75, 76.65),
    "Ropar": (30.97, 76.53), "Kiratpur Sahib": (31.18, 76.57), "Kiratpur": (31.18, 76.57), "Bilaspur": (31.34, 76.76), "Sundernagar": (31.53, 76.89),
    "Mandi": (31.71, 76.93), "Pandoh": (31.67, 77.06), "Aut": (31.76, 77.14), "Bhuntar": (31.88, 77.15),
    "Kullu": (31.96, 77.11), "Manali": (32.24, 77.19), "Kasol": (32.01, 77.31), "Solang": (32.32, 77.16),
    "Sissu": (32.48, 77.13), "Rohtang": (32.37, 77.25), "Naggar": (32.12, 77.17), "Pathankot": (32.27, 75.65),
    "Nurpur": (32.30, 75.89), "Shahpur": (32.21, 76.18), "Gaggal": (32.16, 76.26), "Kangra": (32.10, 76.27),
    "Dharamshala": (32.22, 76.32), "McLeodganj": (32.24, 76.32), "Dalhousie": (32.54, 75.97),
    "Jammu": (32.73, 74.86), "Nagrota": (32.78, 74.91), "Udhampur": (32.92, 75.14), "Ramban": (33.24, 75.24),
    "Banihal": (33.43, 75.20), "Qazigund": (33.59, 75.16), "Anantnag": (33.73, 75.15), "Pampore": (34.02, 74.93),
    "Srinagar": (34.08, 74.80), "Katra": (32.99, 74.93), "Baghpat": (28.94, 77.22), "Shamli": (29.45, 77.31),
    "Saharanpur": (29.96, 77.55), "Dehradun": (30.32, 78.03), "Mussoorie": (30.46, 78.07), "Haridwar": (29.95, 78.16),
    "Rishikesh": (30.09, 78.27), "Amritsar": (31.63, 74.87), "Leh": (34.15, 77.58), "Keylong": (32.57, 77.03),
    "Kasauli": (30.90, 76.96), "Chail": (30.97, 77.20), "Narkanda": (31.26, 77.46), "Naldehra": (31.20, 77.19),
    "Mashobra": (31.13, 77.23), "Nainital": (29.38, 79.46), "Agra": (27.18, 78.01), "Jaipur": (26.91, 75.79),
    "Meerut": (28.98, 77.71), "Khatauli": (29.28, 77.73), "Muzaffarnagar": (29.47, 77.70), "Narsan": (29.71, 77.87),
    "Roorkee": (29.87, 77.89), "Bahadarabad": (29.92, 78.04),
    "Ghanahatti": (31.13, 77.08), "Shalaghat": (31.17, 77.01), "Darlaghat": (31.23, 76.96), "Ner Chowk": (31.59, 76.92),
    "Jalori Pass": (31.53, 77.38), "Banjar": (31.64, 77.34),
    "Shivpuri": (30.14, 78.39), "Jolly Grant": (30.19, 78.18), "Doiwala": (30.18, 78.12),
    "Paonta Sahib": (30.44, 77.62), "Nahan": (30.56, 77.30), "Dhanaulti": (30.43, 78.24), "Kempty": (30.49, 77.99),
    "Chakrata": (30.70, 77.87), "Kuthal Gate": (30.39, 78.07), "Kolhukhet": (30.42, 78.06), "Kincraig": (30.45, 78.06), "Loni": (28.75, 77.29), "Ganeshpur": (30.16, 77.84),
    "Rajpura": (30.48, 76.59), "Khanna": (30.70, 76.22), "Ludhiana": (30.90, 75.85), "Phagwara": (31.22, 75.77),
    "Jalandhar": (31.33, 75.58), "Beas": (31.52, 75.29), "Attari": (31.60, 74.60),
    "Palampur": (32.11, 76.54), "Bir": (32.05, 76.73), "Baijnath": (32.05, 76.65), "Bhagsu": (32.25, 76.33),
    "Gulmarg": (34.05, 74.38), "Tangmarg": (34.06, 74.43), "Sonamarg": (34.30, 75.29), "Pahalgam": (34.02, 75.32),
    "Doodhpathri": (33.87, 74.56), "Yusmarg": (33.83, 74.66), "Baramulla": (34.20, 74.34), "Kargil": (34.56, 76.13),
    "Batala": (31.82, 75.20), "Gurdaspur": (32.04, 75.40),
    "Ghaziabad": (28.67, 77.44), "Hapur": (28.73, 77.78), "Garhmukteshwar": (28.79, 78.10), "Gajraula": (28.85, 78.24),
    "Moradabad": (28.84, 78.77), "Rampur": (28.81, 79.03), "Rudrapur": (28.98, 79.40), "Haldwani": (29.22, 79.51),
    "Kathgodam": (29.27, 79.54), "Bhimtal": (29.35, 79.56), "Bhowali": (29.38, 79.51), "Ramnagar": (29.39, 79.13),
    "Almora": (29.60, 79.66), "Mukteshwar": (29.47, 79.65),
    "Pantnagar": (29.03, 79.47), "Lalkuan": (29.07, 79.52), "Ranikhet": (29.64, 79.43), "Kausani": (29.84, 79.60), "Kainchi Dham": (29.42, 79.52),
    "Chandigarh Airport": (30.67, 76.79),
    "Patnitop": (33.09, 75.33), "Sanasar": (33.13, 75.26), "Kud": (33.08, 75.29), "Reasi": (33.08, 74.84), "Shiv Khori": (33.17, 74.62), "Jammu Airport": (32.69, 74.84),
    "Dasuya": (31.82, 75.65), "Mukerian": (31.95, 75.62), "Lakhanpur": (32.40, 75.60), "Kathua": (32.37, 75.52), "Samba": (32.56, 75.12),
    "Jari": (31.99, 77.24), "Manikaran": (32.03, 77.35),
    "Atal Tunnel": (32.40, 77.15), "Tandi": (32.56, 76.97), "Jispa": (32.64, 77.18), "Darcha": (32.67, 77.22), "Baralacha La": (32.76, 77.42),
    "Sarchu": (32.82, 77.53), "Gata Loops": (33.03, 77.60), "Pang": (33.13, 77.79), "Tanglang La": (33.51, 77.77), "Rumtse": (33.63, 77.76),
    "Upshi": (33.83, 77.81), "Karu": (33.93, 77.73),
    "Noida": (28.57, 77.32), "Greater Noida": (28.47, 77.50), "Jewar": (28.13, 77.56), "Tappal": (28.04, 77.59),
    "Mathura": (27.49, 77.67), "Vrindavan": (27.58, 77.70), "Fatehpur Sikri": (27.09, 77.66),
    "Kurali": (30.83, 76.58), "Anandpur Sahib": (31.23, 76.50), "Nangal": (31.38, 76.38), "Una": (31.48, 76.28), "Amb": (31.70, 76.12), "Mubarikpur": (31.71, 76.09),
    "Chintpurni": (31.81, 76.11), "Dehra": (31.88, 76.23), "Jawalamukhi": (31.84, 76.31), "Ranital": (32.00, 76.23),
    "Neelkanth": (30.08, 78.34), "Chopta": (30.47, 79.21), "Devprayag": (30.15, 78.60), "Rudraprayag": (30.28, 78.98), "Sonprayag": (30.63, 78.99), "Badrinath": (30.74, 79.49),
    # 26 Oct 2026 · Char Dham circuit (Photon/OSM coords, checked)
    "Barkot": (30.81, 78.21), "Janki Chatti": (30.98, 78.44), "Yamunotri": (31.01, 78.46), "Uttarkashi": (30.73, 78.45), "Gangotri": (30.99, 78.94),
    "Ghansali": (30.43, 78.66), "Tilwara": (30.35, 78.98), "Guptkashi": (30.52, 79.08), "Gaurikund": (30.65, 79.02), "Kedarnath": (30.73, 79.07),
    "Ukhimath": (30.52, 79.10), "Chamoli": (30.40, 79.32), "Joshimath": (30.56, 79.56), "Karnaprayag": (30.26, 79.22),
}

# every route card shown anywhere (hub grid, "more routes"); page = slug when a page exists
ROUTES = [
    # slug, from, to, km, time, factor
    dict(slug="delhi-to-shimla-taxi", a="Delhi", b="Shimla", km=345, t="7–8 hrs", f=1.0),
    dict(slug="delhi-to-manali-taxi", a="Delhi", b="Manali", km=540, t="11–13 hrs", f=0.85),
    dict(slug="chandigarh-to-manali-taxi", a="Chandigarh", b="Manali", km=290, t="7–8 hrs", f=0.95),
    dict(slug="chandigarh-to-shimla-taxi", a="Chandigarh", b="Shimla", km=115, t="3–3.5 hrs", f=1.1),
    dict(slug="delhi-to-chandigarh-taxi", a="Delhi", b="Chandigarh", km=250, t="4–5 hrs", f=0.85),
    dict(slug="delhi-to-dehradun-taxi", a="Delhi", b="Dehradun", km=240, t="4–5 hrs", f=0.85),
    dict(slug="pathankot-to-dharamshala-taxi", a="Pathankot", b="Dharamshala", km=90, t="2.5–3 hrs", f=1.1),
    dict(slug="jammu-to-srinagar-taxi", a="Jammu", b="Srinagar", km=250, t="6–8 hrs", f=1.7),
    dict(slug="shimla-to-manali-taxi", a="Shimla", b="Manali", km=250, t="7–8 hrs", f=1.3),
    dict(slug="kalka-to-shimla-taxi", a="Kalka", b="Shimla", km=85, t="2.5–3 hrs", f=1.1),
    dict(slug="delhi-to-dharamshala-taxi", a="Delhi", b="Dharamshala", km=475, t="9–10 hrs", f=1.0),   # 24 Oct 2026: page live; route via Kiratpur Sahib–Una–Amb–Dehra–Kangra (NH503)
    dict(slug="delhi-to-kasol-taxi", a="Delhi", b="Kasol", km=520, t="11–12 hrs", f=1.0),
    dict(slug="manali-to-leh-taxi", a="Manali", b="Leh", km=430, t="2 days (Jun–Oct)", f=1.6),
    dict(slug="chandigarh-to-dharamshala-taxi", a="Chandigarh", b="Dharamshala", km=240, t="5.5–6.5 hrs", f=1.1),   # 27 Oct 2026: page live; via Kharar–Ropar–Kiratpur–Anandpur Sahib–Una–Amb–Dehra–Kangra (NH503); Triveni/HurryUp/EMT 238–244 km
    dict(slug=None, a="Pathankot", b="Dalhousie", km=80, t="2.5–3 hrs", f=1.1),
    dict(slug="delhi-to-haridwar-taxi", a="Delhi", b="Haridwar", km=220, t="4.5–5.5 hrs", f=0.85),
    dict(slug="delhi-to-rishikesh-taxi", a="Delhi", b="Rishikesh", km=240, t="5–6 hrs", f=0.85),
    dict(slug="delhi-to-mussoorie-taxi", a="Delhi", b="Mussoorie", km=280, t="5–6 hrs", f=0.95),
    dict(slug="dehradun-to-mussoorie-taxi", a="Dehradun", b="Mussoorie", km=35, t="1–1.5 hrs", f=1.1),
    dict(slug="delhi-to-amritsar-taxi", a="Delhi", b="Amritsar", km=460, t="7–8 hrs", f=0.85),
    dict(slug=None, a="Delhi", b="Katra", km=640, t="11–12 hrs", f=0.85),
    dict(slug="delhi-to-nainital-taxi", a="Delhi", b="Nainital", km=310, t="7–8 hrs", f=0.9),
    dict(slug="delhi-to-haldwani-taxi", a="Delhi", b="Haldwani", km=285, t="6–7 hrs", f=0.85),   # 25 Oct 2026: all-plains NH-9 + NH-109 (MMT 284 km, HurryUp 302, CabBazar 300)
    dict(slug="delhi-to-jammu-taxi", a="Delhi", b="Jammu", km=590, t="10–11 hrs", f=0.85),
    dict(slug="delhi-to-agra-taxi", a="Delhi", b="Agra", km=230, t="3.5–4.5 hrs", f=0.9),   # 23 Oct 2026: f 0.9 keeps sedan at the market median (Uber ₹2,537 · Triveni ₹3,300 · HurryUp ₹3,798)
]
ROUTE_BY_SLUG = {r["slug"]: r for r in ROUTES if r["slug"]}

WA_BASE = "https://wa.me/" + PHONE + "?text="

COMMON_INCLUDES = [
    "<b>Included in one-way fares:</b> AC car, fuel, driver and driver allowance.",
    "<b>Extra at actuals:</b> tolls, parking, and state entry tax / permit where the car crosses a state border (Himachal charges non-HP vehicles an entry fee).",
    "<b>Round trips & multi-day tours:</b> per-km rate × kilometres driven (minimum 250 km a day) + ₹400 a night driver allowance (₹500 for Tempo Traveller & Urbania).",
    "<b>Peak dates cost more:</b> May–June, Diwali, Christmas–New Year and long weekends. Your WhatsApp quote shows the all-in total before you pay anything.",
]

BOOKING_STEPS = [
    ("Tell us the trip", "Pickup point, drop, date, number of people and luggage — WhatsApp, call or the form below."),
    ("Get one clear quote", "Car, driver, total fare and what it includes, usually within 15–30 minutes."),
    ("Confirm with a small advance", "Pay the advance on our secure payment page (UPI / card). The balance is paid as written in your quote."),
    ("Driver details a day before", "Driver name, phone and car number on WhatsApp. Our team tracks the trip until you're dropped."),
]
