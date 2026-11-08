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
