#!/usr/bin/env python3
"""Mountain weather feed for the suzutravels.com homepage (added 2026-11-05).

Fetches MET Norway Locationforecast 2.0 (free incl. commercial use, CC BY 4.0,
identifying User-Agent required) for ~30 hill stations in Himachal, Kashmir,
Ladakh and Uttarakhand, builds one compact JSON and uploads it to
public_html/suzu-weather-feed.json with the Hostinger API (same upload as deploy.py).
No site cache clear: the homepage asks for ?h=<UTC hour>, so each hour is a new key.

Run hourly by .github/workflows/weather-feed.yml on the default branch.
Local test without upload:  python3 tools/weather_feed.py --out feed.json
"""
import datetime as dt
import json
import sys
import time
import urllib.request

sys.path.insert(0, __file__.rsplit("/", 1)[0])

UA = "SuzuTravels-weather/1.0 (+https://suzutravels.com; info@suzutravels.com)"
U = "https://suzutravels.com/"
# id, name, hindi, region, lat, lon, altitude m, link
PLACES = [
    ("shimla", "Shimla", "शिमला", "Himachal", 31.1048, 77.1734, 2205, "shimla/"),
    ("kufri", "Kufri", "कुफरी", "Himachal", 31.0979, 77.2678, 2510, "kufri-snowfall/"),
    ("narkanda", "Narkanda", "नारकंडा", "Himachal", 31.2617, 77.4570, 2708, "narkanda/"),
    ("chail", "Chail", "चायल", "Himachal", 30.9667, 77.2000, 2250, "chail/"),
    ("kasauli", "Kasauli", "कसौली", "Himachal", 30.8988, 76.9660, 1800, "kasauli-snowfall/"),
    ("manali", "Manali", "मनाली", "Himachal", 32.2432, 77.1892, 2050, "manali/"),
    ("solang", "Solang Valley", "सोलंग", "Himachal", 32.3166, 77.1569, 2480, "solang-valley-guide/"),
    ("sissu", "Sissu · Lahaul", "सिस्सू", "Himachal", 32.4800, 77.1260, 3120, "adventure/atal-tunnel-sissu-snow-trip/"),
    ("kasol", "Kasol", "कसोल", "Himachal", 32.0099, 77.3150, 1580, "kasol-trip-plan/"),
    ("jibhi", "Jibhi", "जीभी", "Himachal", 31.5900, 77.3650, 1900, "jibhi/"),
    ("kaza", "Kaza · Spiti", "काज़ा", "Himachal", 32.2276, 78.0710, 3800, "destination/spiti-valley-tour-packages/"),
    ("kalpa", "Kalpa", "कल्पा", "Himachal", 31.5370, 78.2553, 2960, "kalpa-himachal/"),
    ("chitkul", "Chitkul", "छितकुल", "Himachal", 31.3513, 78.4370, 3450, "sangla-valley-and-chitkul-kinnaur-trip-guide/"),
    ("dharamshala", "McLeod Ganj", "मैक्लोडगंज", "Himachal", 32.2396, 76.3239, 2080, "mcleod-ganj/"),
    ("dalhousie", "Dalhousie", "डलहौज़ी", "Himachal", 32.5387, 75.9710, 1970, "dalhousie/"),
    ("khajjiar", "Khajjiar", "खज्जियार", "Himachal", 32.5501, 76.0596, 1920, "dalhousie-khajjiar-trip-guide/"),
    ("bir", "Bir Billing", "बीड़", "Himachal", 32.0440, 76.7180, 1525, "adventure/paragliding-in-bir-billing/"),
    ("srinagar", "Srinagar", "श्रीनगर", "Kashmir", 34.0837, 74.7973, 1585, "destination/kashmir-tour-packages/"),
    ("gulmarg", "Gulmarg", "गुलमर्ग", "Kashmir", 34.0484, 74.3805, 2650, "india-tours/gulmarg-ski-holiday/"),
    ("pahalgam", "Pahalgam", "पहलगाम", "Kashmir", 34.0161, 75.3150, 2200, "destination/kashmir-tour-packages/"),
    ("sonamarg", "Sonamarg", "सोनमर्ग", "Kashmir", 34.3036, 75.2930, 2740, "destination/kashmir-tour-packages/"),
    ("doodhpathri", "Doodhpathri", "दूधपथरी", "Kashmir", 33.8800, 74.5700, 2730, "best-kashmir-tour-package/"),
    ("gurez", "Gurez", "गुरेज़", "Kashmir", 34.6340, 74.8480, 2400, "best-kashmir-tour-package/"),
    ("leh", "Leh", "लेह", "Ladakh", 34.1526, 77.5771, 3500, "destination/leh-ladakh-tour-packages/"),
    ("auli", "Auli", "औली", "Uttarakhand", 30.5286, 79.5675, 2800, "auli-in-december/"),
    ("mussoorie", "Mussoorie", "मसूरी", "Uttarakhand", 30.4598, 78.0644, 2005, "mussoorie-in-december/"),
    ("nainital", "Nainital", "नैनीताल", "Uttarakhand", 29.3803, 79.4636, 2084, "nainital-in-december/"),
]
# Extra places for the Hindi/English weather pages (8 Nov 2026). Kept under "more" so the
# homepage marquee (reads only "places") stays the 27 hill stations.
MORE = [
    ("kullu", "Kullu", "कुल्लू", "Himachal", 31.9578, 77.1095, 1220, "kullu-ka-mausam/"),
    ("palampur", "Palampur", "पालमपुर", "Himachal", 32.1109, 76.5363, 1470, "palampur-ka-mausam/"),
    ("kangra", "Kangra", "कांगड़ा", "Himachal", 32.0998, 76.2691, 733, "kangra-ka-mausam/"),
    ("mandi", "Mandi", "मंडी", "Himachal", 31.7088, 76.9320, 760, "mandi-ka-mausam/"),
    ("solan", "Solan", "सोलन", "Himachal", 30.9045, 77.0967, 1500, "solan-ka-mausam/"),
    ("chamba", "Chamba", "चंबा", "Himachal", 32.5534, 76.1258, 996, "chamba-ka-mausam/"),
    ("bilaspur", "Bilaspur", "बिलासपुर", "Himachal", 31.3407, 76.7627, 670, "bilaspur-ka-mausam/"),
    ("hamirpur", "Hamirpur", "हमीरपुर", "Himachal", 31.6862, 76.5213, 785, "hamirpur-ka-mausam/"),
    ("una", "Una", "ऊना", "Himachal", 31.4685, 76.2708, 369, "una-ka-mausam/"),
    ("jammu", "Jammu", "जम्मू", "Jammu", 32.7266, 74.8570, 327, "jammu-ka-mausam/"),
    ("katra", "Katra", "कटरा", "Jammu", 32.9916, 74.9318, 875, "katra-ka-mausam/"),
    ("bhawan", "Vaishno Devi Bhawan", "वैष्णो देवी भवन", "Jammu", 33.0308, 74.9490, 1585, "katra-ka-mausam/"),
    ("patnitop", "Patnitop", "पटनीटॉप", "Jammu", 33.0870, 75.3290, 2024, "patnitop-weather/"),
    ("keylong", "Keylong", "केलांग", "Himachal", 32.5717, 77.0322, 3080, "sissu-weather/"),
    ("tirthan", "Tirthan valley (Gushaini)", "तीर्थन घाटी", "Himachal", 31.6290, 77.4450, 1600, "jibhi-weather/"),
    ("billing", "Billing", "बिलिंग", "Himachal", 32.0790, 76.7230, 2400, "bir-weather/"),
    ("rohtang", "Rohtang Pass", "रोहतांग पास", "Himachal", 32.3716, 77.2466, 3978, "rohtang-weather/"),
    ("kargil", "Kargil", "कारगिल", "Ladakh", 34.5539, 76.1349, 2676, "kargil-weather/"),
    ("drass", "Drass", "द्रास", "Ladakh", 34.4285, 75.7586, 3280, "kargil-weather/"),
    ("anantnag", "Anantnag", "अनंतनाग", "Kashmir", 33.7311, 75.1487, 1601, "anantnag-weather/"),
    ("baramulla", "Baramulla", "बारामूला", "Kashmir", 34.2090, 74.3436, 1590, "baramulla-weather/"),
    ("kokernag", "Kokernag", "कोकरनाग", "Kashmir", 33.5840, 75.3050, 2000, "anantnag-weather/"),
    ("bhaderwah", "Bhaderwah", "भद्रवाह", "Jammu", 32.9800, 75.7130, 1613, "bhaderwah-weather/"),
    ("kupwara", "Kupwara", "कुपवाड़ा", "Kashmir", 34.5260, 74.2546, 1615, "kupwara-weather/"),
    ("pangong", "Pangong Tso (Lukung)", "पैंगोंग", "Ladakh", 34.0300, 78.4600, 4250, "pangong-weather/"),
    ("nubra", "Nubra (Diskit)", "नुब्रा", "Ladakh", 34.5476, 77.5594, 3144, "pangong-weather/"),
    ("kishtwar", "Kishtwar", "किश्तवाड़", "Jammu", 33.3116, 75.7662, 1634, "kishtwar-weather/"),
    ("sinthan", "Sinthan Top", "सिंथन टॉप", "Kashmir", 33.5850, 75.5050, 3748, "kishtwar-weather/"),
    ("rampur", "Rampur Bushahr", "रामपुर बुशहर", "Himachal", 31.4513, 77.6300, 1005, "rampur-weather/"),
    ("sarahan", "Sarahan", "सराहन", "Himachal", 31.5078, 77.7944, 2165, "rampur-weather/"),
    ("manikaran", "Manikaran", "मणिकर्ण", "Himachal", 32.0270, 77.3480, 1760, "parvati-valley-weather/"),
    ("tosh", "Tosh", "तोष", "Himachal", 32.0150, 77.4500, 2400, "parvati-valley-weather/"),
    ("banihal", "Banihal", "बनिहाल", "Jammu", 33.4364, 75.1946, 1624, "banihal-weather/"),
    ("ramban", "Ramban", "रामबन", "Jammu", 33.2425, 75.2386, 747, "banihal-weather/"),
    ("qazigund", "Qazigund", "काज़ीगुंड", "Kashmir", 33.5922, 75.1656, 1670, "banihal-weather/"),
    ("bharmour", "Bharmour", "भरमौर", "Himachal", 32.4415, 76.5340, 2195, "bharmour-weather/"),
    ("kulgam", "Kulgam", "कुलगाम", "Kashmir", 33.6400, 75.0200, 1739, "kulgam-weather/"),
    ("aharbal", "Aharbal", "अहरबल", "Kashmir", 33.6440, 74.7870, 2266, "kulgam-weather/"),
    ("shopian", "Shopian", "शोपियां", "Kashmir", 33.7200, 74.8300, 2057, "shopian-weather/"),
    ("peerkigali", "Peer Ki Gali", "पीर की गली", "Kashmir", 33.6386, 74.5465, 3490, "shopian-weather/"),
    ("budgam", "Budgam", "बडगाम", "Kashmir", 34.0198, 74.7194, 1610, "budgam-weather/"),
    ("yusmarg", "Yusmarg", "यूसमर्ग", "Kashmir", 33.8330, 74.6640, 2396, "budgam-weather/"),
    ("bandipora", "Bandipora", "बांदीपोरा", "Kashmir", 34.4170, 74.6430, 1580, "bandipora-weather/"),
    ("theog", "Theog", "ठियोग", "Himachal", 31.1200, 77.3500, 2100, "theog-weather/"),
    ("rohru", "Rohru", "रोहड़ू", "Himachal", 31.2020, 77.7520, 1525, "rohru-weather/"),
    ("karsog", "Karsog", "करसोग", "Himachal", 31.3800, 77.2000, 1400, "karsog-weather/"),
    ("shikaridevi", "Shikari Devi", "शिकारी देवी", "Himachal", 31.4787, 77.1656, 3300, "karsog-weather/"),
    ("rishikesh", "Rishikesh", "ऋषिकेश", "Uttarakhand", 30.0869, 78.2676, 372, "rishikesh-weather/"),
    ("haridwar", "Haridwar", "हरिद्वार", "Uttarakhand", 29.9457, 78.1642, 314, "rishikesh-weather/"),
    ("dehradun", "Dehradun", "देहरादून", "Uttarakhand", 30.3165, 78.0322, 640, "mussoorie-weather/"),
    ("dhanaulti", "Dhanaulti", "धनौल्टी", "Uttarakhand", 30.4260, 78.2450, 2286, "mussoorie-weather/"),
    ("chakrata", "Chakrata", "चकराता", "Uttarakhand", 30.7020, 77.8690, 2118, "chakrata-weather/"),
    ("lansdowne", "Lansdowne", "लैंसडाउन", "Uttarakhand", 29.8377, 78.6871, 1706, "lansdowne-weather/"),
    ("kedarnath", "Kedarnath", "केदारनाथ", "Uttarakhand", 30.7346, 79.0669, 3583, "kedarnath-weather/"),
    ("gaurikund", "Gaurikund", "गौरीकुंड", "Uttarakhand", 30.6520, 79.0240, 1982, "kedarnath-weather/"),
    ("chopta", "Chopta", "चोपता", "Uttarakhand", 30.4850, 79.2125, 2680, "chopta-weather/"),
    ("tungnath", "Tungnath", "तुंगनाथ", "Uttarakhand", 30.4895, 79.2154, 3680, "chopta-weather/"),
    ("mukteshwar", "Mukteshwar", "मुक्तेश्वर", "Uttarakhand", 29.4722, 79.6479, 2286, "mukteshwar-weather/"),
    ("munsiyari", "Munsiyari", "मुनस्यारी", "Uttarakhand", 30.0676, 80.2386, 2298, "munsiyari-weather/"),
    ("almora", "Almora", "अल्मोड़ा", "Uttarakhand", 29.5971, 79.6591, 1642, "mukteshwar-weather/"),
    ("joshimath", "Joshimath", "जोशीमठ", "Uttarakhand", 30.5550, 79.5643, 1875, "weather/auli/"),
    ("badrinath", "Badrinath", "बद्रीनाथ", "Uttarakhand", 30.7433, 79.4938, 3300, "pilgrimage-tours/badrinath/"),
    ("sankri", "Sankri", "सांकरी", "Uttarakhand", 31.0782, 78.1863, 1950, "kedarkantha-weather/"),
    ("kedarkantha", "Kedarkantha", "केदारकांठा", "Uttarakhand", 31.0230, 78.1710, 3800, "kedarkantha-weather/"),
    ("bhimtal", "Bhimtal", "भीमताल", "Uttarakhand", 29.3480, 79.5510, 1370, "nainital-weather/"),
    ("sangla", "Sangla", "सांगला", "Himachal", 31.4236, 78.2617, 2680, "sangla-weather/"),
    ("tabo", "Tabo", "ताबो", "Himachal", 32.0940, 78.3830, 3280, "spiti-in-winter/"),
    ("nako", "Nako", "नाको", "Himachal", 31.8810, 78.6270, 3660, "spiti-in-winter/"),
    ("hanle", "Hanle", "हानले", "Ladakh", 32.7794, 78.9763, 4500, "weather/leh/"),
    ("padum", "Padum (Zanskar)", "पदुम", "Ladakh", 33.4667, 76.8833, 3657, "weather/leh/"),
    ("gangotri", "Gangotri", "गंगोत्री", "Uttarakhand", 30.9947, 78.9398, 3100, "gangotri-weather/"),
    ("harsil", "Harsil", "हर्षिल", "Uttarakhand", 31.0386, 78.7400, 2620, "gangotri-weather/"),
    ("uttarkashi", "Uttarkashi", "उत्तरकाशी", "Uttarakhand", 30.7268, 78.4354, 1158, "gangotri-weather/"),
    ("yamunotri", "Yamunotri", "यमुनोत्री", "Uttarakhand", 31.0141, 78.4600, 3290, "yamunotri-weather/"),
    ("barkot", "Barkot", "बड़कोट", "Uttarakhand", 30.8094, 78.2056, 1220, "yamunotri-weather/"),
    ("ranikhet", "Ranikhet", "रानीखेत", "Uttarakhand", 29.6434, 79.4322, 1869, "ranikhet-weather/"),
    ("kausani", "Kausani", "कौसानी", "Uttarakhand", 29.8434, 79.6033, 1890, "ranikhet-weather/"),
    ("pithoragarh", "Pithoragarh", "पिथौरागढ़", "Uttarakhand", 29.5829, 80.2182, 1627, "pithoragarh-weather/"),
    ("ramnagar", "Ramnagar (Corbett)", "रामनगर", "Uttarakhand", 29.3949, 79.1265, 345, "jim-corbett-weather/"),
    ("dhikala", "Dhikala (Corbett)", "ढिकाला", "Uttarakhand", 29.5300, 78.8600, 400, "jim-corbett-weather/"),
    ("newtehri", "New Tehri", "नई टिहरी", "Uttarakhand", 30.3780, 78.4320, 1750, "tehri-weather/"),
    ("tehrilake", "Tehri Lake (Koti)", "टिहरी झील", "Uttarakhand", 30.3930, 78.4710, 850, "tehri-weather/"),
    ("champawat", "Champawat", "चंपावत", "Uttarakhand", 29.3364, 80.0910, 1615, "champawat-weather/"),
    ("lohaghat", "Lohaghat", "लोहाघाट", "Uttarakhand", 29.4040, 80.0890, 1706, "champawat-weather/"),
    ("hemkund", "Hemkund Sahib", "हेमकुंड साहिब", "Uttarakhand", 30.7085, 79.6134, 4632, "hemkund-sahib-weather/"),
    ("ghangaria", "Ghangaria", "घांघरिया", "Uttarakhand", 30.6950, 79.5867, 3050, "hemkund-sahib-weather/"),
    ("govindghat", "Govindghat", "गोविंदघाट", "Uttarakhand", 30.6149, 79.5609, 1830, "hemkund-sahib-weather/"),
    ("triund", "Triund", "त्रिउंड", "Himachal", 32.2586, 76.3458, 2850, "triund-weather/"),
    ("mcleodganj", "McLeodganj", "मैक्लोडगंज", "Himachal", 32.2427, 76.3213, 2082, "weather/dharamshala/"),
    ("haldwani", "Haldwani", "हल्द्वानी", "Uttarakhand", 29.2183, 79.5130, 424, "haldwani-weather/"),
    ("kathgodam", "Kathgodam", "काठगोदाम", "Uttarakhand", 29.2660, 79.5440, 554, "haldwani-weather/"),
    ("pauri", "Pauri", "पौड़ी", "Uttarakhand", 30.1520, 78.7790, 1814, "pauri-weather/"),
    ("khirsu", "Khirsu", "खिर्सू", "Uttarakhand", 30.1740, 78.8650, 1700, "pauri-weather/"),
    ("kotdwar", "Kotdwar", "कोटद्वार", "Uttarakhand", 29.7460, 78.5230, 400, "kotdwar-weather/"),
]
IST = dt.timezone(dt.timedelta(hours=5, minutes=30))


def get(lat, lon, alt):
    url = (f"https://api.met.no/weatherapi/locationforecast/2.0/compact?"
           f"lat={lat:.4f}&lon={lon:.4f}&altitude={alt}")
    for i in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read())
        except Exception as e:  # noqa: BLE001
            print("  retry", url, e, flush=True)
            time.sleep(3 * (i + 1))
    return None


def build_place(p, raw):
    pid, name, hi, region, lat, lon, alt, link = p
    ts = raw["properties"]["timeseries"]
    first = ts[0]
    det = first["data"]["instant"]["details"]
    nxt = first["data"].get("next_1_hours") or first["data"].get("next_6_hours") or {}
    now = {
        "t": round(det.get("air_temperature", 0), 1),
        "rh": round(det.get("relative_humidity", 0)),
        "ws": round(det.get("wind_speed", 0) * 3.6, 1),  # m/s -> km/h
        "sym": nxt.get("summary", {}).get("symbol_code", "cloudy"),
        "pr": nxt.get("details", {}).get("precipitation_amount", 0),
    }
    days = {}
    for t in ts:
        when = dt.datetime.fromisoformat(t["time"].replace("Z", "+00:00")).astimezone(IST)
        d = when.date().isoformat()
        x = days.setdefault(d, {"d": d, "lo": 99, "hi": -99, "pr": 0.0, "sym": None, "symh": 99, "snow": False})
        temp = t["data"]["instant"]["details"].get("air_temperature")
        if temp is not None:
            x["lo"] = min(x["lo"], temp)
            x["hi"] = max(x["hi"], temp)
        n1 = t["data"].get("next_1_hours")
        n6 = t["data"].get("next_6_hours")
        blk = n1 or n6
        if blk:
            sym = blk.get("summary", {}).get("symbol_code", "")
            amt = blk.get("details", {}).get("precipitation_amount", 0) or 0
            # avoid double counting: hourly blocks when present, else 6-hourly
            if n1:
                x["pr"] += amt
            elif n6 and when.hour in (0, 6, 12, 18):
                x["pr"] += amt
            if "snow" in sym or ("sleet" in sym):
                x["snow"] = True
            elif amt > 0.2 and temp is not None and temp <= 0.5:
                x["snow"] = True
            # representative symbol: closest to 13:00 IST
            dist = abs(when.hour - 13)
            if dist < x["symh"]:
                x["sym"], x["symh"] = sym, dist
    out = []
    for d in sorted(days)[:6]:
        x = days[d]
        if x["lo"] == 99:
            continue
        out.append({"d": d, "lo": round(x["lo"]), "hi": round(x["hi"]), "pr": round(x["pr"], 1),
                    "sym": x["sym"] or "cloudy", "snow": x["snow"]})
    return {"id": pid, "name": name, "hi": hi, "region": region, "alt": alt,
            "url": U + link, "now": now, "days": out[:5]}


def main():
    out_path = None
    if "--out" in sys.argv:
        out_path = sys.argv[sys.argv.index("--out") + 1]
    places = []
    for p in PLACES:
        raw = get(p[4], p[5], p[6])
        if not raw:
            print("  skip", p[0], flush=True)
            continue
        try:
            places.append(build_place(p, raw))
        except Exception as e:  # noqa: BLE001
            print("  bad", p[0], e, flush=True)
        time.sleep(0.4)
    more = []
    for p in MORE:
        raw = get(p[4], p[5], p[6])
        if not raw:
            print("  skip", p[0], flush=True)
            continue
        try:
            more.append(build_place(p, raw))
        except Exception as e:  # noqa: BLE001
            print("  bad", p[0], e, flush=True)
        time.sleep(0.4)
    if len(places) < len(PLACES) * 0.7:
        print(f"only {len(places)} of {len(PLACES)} places — not uploading", flush=True)
        sys.exit(1)
    feed = {"updated": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),
            "source": "MET Norway", "license": "CC BY 4.0", "places": places, "more": more}
    data = json.dumps(feed, ensure_ascii=False, separators=(",", ":")).encode()
    print(f"feed {len(places)}+{len(more)} places, {len(data)} B", flush=True)
    if out_path:
        open(out_path, "wb").write(data)
        return
    import deploy  # tools/deploy.py — Hostinger API helpers
    if not deploy.TOKEN:
        print("HOSTINGER_API_TOKEN missing", flush=True)
        sys.exit(1)
    deploy.upload("suzu-weather-feed.json", data)


if __name__ == "__main__":
    main()
