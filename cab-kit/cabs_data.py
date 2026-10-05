# -*- coding: utf-8 -*-
"""Suzu Cab Kit — single source of truth for fleet, fares, places and page content.
Edit fares here (FLEET rates / ROUTE factors) and rebuild; every page and the on-page calculator update together.
Fare rule (Sushil approved research-based fares, 30 Sep 2026):
  one-way  = max(min_fare, dist_km * ow_rate * route_factor) rounded up to the next ...99
  round trip / multi-day = max(2*dist, 250*days) * hire_rate + driver allowance per night
Fares are indicative starting prices (off-season). Tolls, parking and state entry tax/permits are extra at actuals.
"""
import math

PHONE = "917087488961"
PHONE_TXT = "+91 70874 88961"
REG = "HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022"
RATING = "★ 4.7 · 377 Google reviews"   # same phrase the Suzu Live Reviews plugin rewrites site-wide

FLEET = [
    dict(id="hatch", name="Hatchback", model="Swift / WagonR class", seats=4, bags="2 small bags", fuel="Petrol / CNG",
         ow=12, hire=11, min=1999, night=400, best="Couples & short transfers", page=None),
    dict(id="sedan", name="Sedan", model="Dzire / Etios / Aura", seats=4, bags="3 bags", fuel="Petrol / CNG",
         ow=14, hire=12, min=2299, night=400, best="Couples & small families, highway runs", page=None),
    dict(id="ertiga", name="Maruti Ertiga", model="6-seater MUV", seats=6, bags="3 bags + carrier", fuel="Petrol / CNG",
         ow=17, hire=14, min=2999, night=400, best="Families of 5–6 on a budget", page=None),
    dict(id="carens", name="Kia Carens", model="6-seater premium MPV", seats=6, bags="4 bags", fuel="Diesel / Petrol",
         ow=19, hire=16, min=3499, night=400, best="Families who want extra comfort", page=None),
    dict(id="crysta", name="Toyota Innova Crysta", model="6+1 / 7-seater SUV", seats=7, bags="5 bags", fuel="Diesel",
         ow=24, hire=19, min=3999, night=400, best="Hill circuits, senior citizens, groups of 6–7", page="innova-crysta-on-rent"),
    dict(id="tempo", name="Tempo Traveller", model="Force Traveller 12–14 seater", seats=12, bags="10 bags", fuel="Diesel",
         ow=32, hire=26, min=6999, night=500, best="Groups, pilgrimages, office trips", page="tempo-traveller-hire-delhi"),
    dict(id="urbania", name="Force Urbania", model="Luxury van, up to 17 seats", seats=17, bags="12+ bags", fuel="Diesel",
         ow=42, hire=36, min=9999, night=500, best="Premium group transfers & weddings", page=None),
]
FLEET_BY_ID = {v["id"]: v for v in FLEET}


def r99(x):
    return int(math.ceil(x / 100.0) * 100 - 1)


def oneway(vid, dist, factor):
    v = FLEET_BY_ID[vid]
    return max(v["min"], r99(dist * v["ow"] * factor))


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
    "Shivpuri": (30.14, 78.39), "Jolly Grant": (30.19, 78.18), "Doiwala": (30.18, 78.12),
    "Paonta Sahib": (30.44, 77.62), "Nahan": (30.56, 77.30), "Dhanaulti": (30.43, 78.24), "Kempty": (30.49, 77.99),
    "Chakrata": (30.70, 77.87),
    "Rajpura": (30.48, 76.59), "Khanna": (30.70, 76.22), "Ludhiana": (30.90, 75.85), "Phagwara": (31.22, 75.77),
    "Jalandhar": (31.33, 75.58), "Beas": (31.52, 75.29), "Attari": (31.60, 74.60),
    "Palampur": (32.11, 76.54), "Bir": (32.05, 76.73), "Baijnath": (32.05, 76.65), "Bhagsu": (32.25, 76.33),
}

# every route card shown anywhere (hub grid, "more routes"); page = slug when a page exists
ROUTES = [
    # slug, from, to, km, time, factor
    dict(slug="delhi-to-shimla-taxi", a="Delhi", b="Shimla", km=345, t="7–8 hrs", f=1.0),
    dict(slug="delhi-to-manali-taxi", a="Delhi", b="Manali", km=540, t="11–13 hrs", f=1.0),
    dict(slug="chandigarh-to-manali-taxi", a="Chandigarh", b="Manali", km=290, t="7–8 hrs", f=1.1),
    dict(slug="chandigarh-to-shimla-taxi", a="Chandigarh", b="Shimla", km=115, t="3–3.5 hrs", f=1.1),
    dict(slug="delhi-to-chandigarh-taxi", a="Delhi", b="Chandigarh", km=250, t="4–5 hrs", f=0.85),
    dict(slug="delhi-to-dehradun-taxi", a="Delhi", b="Dehradun", km=240, t="4–5 hrs", f=0.85),
    dict(slug="pathankot-to-dharamshala-taxi", a="Pathankot", b="Dharamshala", km=90, t="2.5–3 hrs", f=1.1),
    dict(slug="jammu-to-srinagar-taxi", a="Jammu", b="Srinagar", km=250, t="6–8 hrs", f=1.7),
    dict(slug=None, a="Shimla", b="Manali", km=245, t="7–8 hrs", f=1.1),
    dict(slug=None, a="Kalka", b="Shimla", km=85, t="2.5–3 hrs", f=1.1),
    dict(slug=None, a="Delhi", b="Dharamshala", km=475, t="9–10 hrs", f=1.0),
    dict(slug=None, a="Delhi", b="Kasol", km=520, t="11–12 hrs", f=1.0),
    dict(slug=None, a="Manali", b="Leh", km=430, t="2 days (Jun–Oct)", f=1.6),
    dict(slug=None, a="Chandigarh", b="Dharamshala", km=240, t="5.5–6.5 hrs", f=1.1),
    dict(slug=None, a="Pathankot", b="Dalhousie", km=80, t="2.5–3 hrs", f=1.1),
    dict(slug="delhi-to-haridwar-taxi", a="Delhi", b="Haridwar", km=220, t="4.5–5.5 hrs", f=0.85),
    dict(slug="delhi-to-rishikesh-taxi", a="Delhi", b="Rishikesh", km=240, t="5–6 hrs", f=0.85),
    dict(slug=None, a="Delhi", b="Mussoorie", km=280, t="5–6 hrs", f=0.95),
    dict(slug="delhi-to-amritsar-taxi", a="Delhi", b="Amritsar", km=460, t="7–8 hrs", f=0.85),
    dict(slug=None, a="Delhi", b="Katra", km=640, t="11–12 hrs", f=0.85),
    dict(slug=None, a="Delhi", b="Nainital", km=310, t="7–8 hrs", f=0.95),
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
