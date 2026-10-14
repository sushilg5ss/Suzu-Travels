# -*- coding: utf-8 -*-
"""Suzu Trip Planner — master place list (v0.1, 15 Oct 2026).

Each place: id, name, hi (Hindi name), lat, lon, region, kind, cls (hotel class), stay (can overnight),
months (open months, None = all year), sights [(name, extra_km_round_trip, note)], tip.

kind:  hub   = arrival / departure city (airport / railhead)
       stay  = overnight destination
       temple= shrine town (pilgrim circuits)
cls (hotel class, see rates.json):  metro, hill_premium, hill, remote, pilgrim, kashmir, ladakh
"""

P = []
def add(id, name, hi, lat, lon, region, kind, cls, sights=(), months=None, tip="", stay=True, local_km=60):
    P.append(dict(id=id, name=name, hi=hi, lat=lat, lon=lon, region=region, kind=kind, cls=cls,
                  stay=stay, months=months, local_km=local_km,
                  sights=[dict(n=s[0], km=s[1], note=(s[2] if len(s) > 2 else "")) for s in sights], tip=tip))

SUMMER = [6, 7, 8, 9, 10]           # high passes (Kunzum, Baralacha, Chandratal, Manali-Leh road)
DHAM = [5, 6, 7, 8, 9, 10]          # Char Dham portals (opening late Apr/May, closing Oct/Nov)

# ---------- arrival hubs ----------
add("delhi", "Delhi", "दिल्ली", 28.6139, 77.2090, "hub", "hub", "metro",
    [("India Gate & Kartavya Path", 20), ("Akshardham", 25), ("Qutub Minar", 30)], tip="IGI Airport / NDLS railway station pickup")
add("chandigarh", "Chandigarh", "चंडीगढ़", 30.7333, 76.7794, "hub", "hub", "metro",
    [("Rock Garden", 10), ("Sukhna Lake", 10), ("Mansa Devi Temple, Panchkula", 25)], tip="Airport / railway station / ISBT pickup")
add("amritsar", "Amritsar", "अमृतसर", 31.6200, 74.8765, "punjab", "hub", "metro",
    [("Golden Temple", 10), ("Wagah Border ceremony", 60), ("Jallianwala Bagh", 5)])
add("pathankot", "Pathankot", "पठानकोट", 32.2733, 75.6522, "hub", "hub", "metro", tip="Railway station pickup")
add("jammu", "Jammu", "जम्मू", 32.7266, 74.8570, "kashmir", "hub", "metro", [("Raghunath Temple", 10)])
add("dehradun", "Dehradun", "देहरादून", 30.3165, 78.0322, "uttarakhand", "hub", "metro",
    [("Robber's Cave", 20), ("Sahastradhara", 30)], tip="Jolly Grant airport pickup")

# ---------- Himachal ----------
add("kasauli", "Kasauli", "कसौली", 30.9010, 76.9650, "himachal", "stay", "hill_premium",
    [("Monkey Point", 10), ("Mall Road & Christ Church", 5), ("Sunset Point", 5)])
add("chail", "Chail", "चायल", 30.9640, 77.1990, "himachal", "stay", "hill",
    [("Chail Palace", 5), ("World's highest cricket ground", 5), ("Kali Ka Tibba", 10)])
add("shimla", "Shimla", "शिमला", 31.1048, 77.1734, "himachal", "stay", "hill_premium",
    [("Kufri & Fagu snow point", 45), ("Mall Road, Ridge & Christ Church", 5), ("Jakhu Temple", 10),
     ("Viceregal Lodge", 10), ("Mashobra & Naldehra", 50)], local_km=70)
add("narkanda", "Narkanda", "नारकंडा", 31.2600, 77.4600, "himachal", "stay", "hill",
    [("Hatu Peak & temple", 16), ("Apple orchards of Thanedhar", 20)], months=None)
add("sarahan", "Sarahan", "सराहन", 31.5110, 77.7950, "himachal", "stay", "hill",
    [("Bhimakali Temple", 3)])
add("sangla", "Sangla", "सांगला", 31.4260, 78.2640, "himachal", "stay", "hill",
    [("Chitkul — last village", 50), ("Kamru Fort", 5), ("Baspa river walk", 5)])
add("chitkul", "Chitkul", "छितकुल", 31.3510, 78.4370, "himachal", "stay", "remote",
    [("Baspa riverside & Mathi temple", 5)], months=[3, 4, 5, 6, 7, 8, 9, 10, 11])
add("kalpa", "Kalpa", "कल्पा", 31.5376, 78.2550, "himachal", "stay", "hill",
    [("Kinner Kailash sunrise view", 5), ("Roghi village & Suicide Point", 15), ("Reckong Peo market", 15)])
add("nako", "Nako", "नाको", 31.8790, 78.6270, "himachal", "stay", "remote",
    [("Nako Lake & monastery", 3)])
add("tabo", "Tabo", "ताबो", 32.0940, 78.3830, "himachal", "stay", "remote",
    [("Tabo Monastery (996 AD)", 3), ("Dhankar Monastery & lake", 70)])
add("kaza", "Kaza", "काज़ा", 32.2260, 78.0720, "himachal", "stay", "remote",
    [("Key Monastery & Kibber", 40), ("Langza, Hikkim & Komic", 50), ("Pin Valley & Mud", 100), ("Dhankar Monastery", 70)],
    tip="SUV recommended. Altitude 3,800 m — take it slow on day 1", local_km=80)
add("chandratal", "Chandratal (camps)", "चंद्रताल", 32.4780, 77.6150, "himachal", "stay", "remote",
    [("Chandratal Lake walk", 10)], months=SUMMER, tip="Camps only, open about mid-June to mid-October")
add("manali", "Manali", "मनाली", 32.2432, 77.1892, "himachal", "stay", "hill_premium",
    [("Solang Valley", 30), ("Atal Tunnel & Sissu", 70), ("Hadimba Temple & Old Manali", 10),
     ("Vashisht hot springs", 8), ("Rohtang Pass (permit, May–Nov)", 110), ("Naggar Castle", 45)], local_km=80)
add("sissu", "Sissu (Lahaul)", "सिस्सू", 32.4820, 77.1250, "himachal", "stay", "hill",
    [("Sissu waterfall & lake", 5), ("Keylong & Kardang Monastery", 60)])
add("jispa", "Jispa", "जिस्पा", 32.6410, 77.1890, "himachal", "stay", "remote",
    [("Bhaga riverside", 5)], months=SUMMER)
add("kullu", "Kullu", "कुल्लू", 31.9578, 77.1095, "himachal", "stay", "hill",
    [("River rafting at Babeli/Pirdi", 20), ("Bijli Mahadev", 40), ("Kullu shawl factories", 10)])
add("kasol", "Kasol", "कसोल", 32.0099, 77.3150, "himachal", "stay", "hill",
    [("Manikaran Sahib & hot springs", 10), ("Tosh & Kalga villages", 40), ("Chalal walk", 5)])
add("jibhi", "Jibhi", "जीभी", 31.5900, 77.3700, "himachal", "stay", "hill",
    [("Jibhi waterfall", 3), ("Jalori Pass & Serolsar Lake", 25), ("Chehni Kothi", 15)])
add("tirthan", "Tirthan Valley", "तीर्थन घाटी", 31.6400, 77.4400, "himachal", "stay", "hill",
    [("Great Himalayan National Park gate", 10), ("Trout farms & river walk", 5)])
add("mandi", "Mandi", "मंडी", 31.7080, 76.9318, "himachal", "stay", "hill",
    [("Bhootnath & Panchvaktra temples", 5), ("Rewalsar Lake", 50), ("Prashar Lake", 100)])
add("bir", "Bir Billing", "बीर बिलिंग", 32.0440, 76.7230, "himachal", "stay", "hill",
    [("Paragliding from Billing (Get Quote)", 30), ("Tibetan colony & monasteries", 5)])
add("palampur", "Palampur", "पालमपुर", 32.1100, 76.5363, "himachal", "stay", "hill",
    [("Tea gardens", 10), ("Baijnath Temple", 30), ("Andretta artists' village", 25)])
add("dharamshala", "Dharamshala / McLeodganj", "धर्मशाला / मैक्लोडगंज", 32.2190, 76.3234, "himachal", "stay", "hill_premium",
    [("Dalai Lama Temple, McLeodganj", 10), ("Bhagsu Nag & waterfall", 12), ("HPCA Stadium", 10),
     ("Naddi & Dal Lake", 15), ("Kangra Fort", 40), ("Triund trek (Get Quote)", 10)])
add("dalhousie", "Dalhousie", "डलहौज़ी", 32.5387, 75.9710, "himachal", "stay", "hill_premium",
    [("Khajjiar — Mini Switzerland", 50), ("Panchpula", 10), ("Dainkund Peak", 25), ("St John's Church", 5)])
add("chamba", "Chamba", "चंबा", 32.5534, 76.1258, "himachal", "stay", "hill",
    [("Chamunda & Lakshmi Narayan temples", 5), ("Bhuri Singh Museum", 3)])

# ---------- Mata / Shakti Peeth circuit (Himachal "Nau Devi") ----------
add("nainadevi", "Naina Devi", "नैना देवी", 31.3058, 76.5353, "pilgrim", "temple", "pilgrim",
    [("Shri Naina Devi Ji darshan (ropeway)", 5), ("Anandpur Sahib Gurudwara", 40), ("Gobind Sagar Lake view", 20)],
    tip="Ropeway or 1.5 km climb to the shrine")
add("chintpurni", "Chintpurni", "चिंतपूर्णी", 31.8200, 76.0000, "pilgrim", "temple", "pilgrim",
    [("Maa Chintpurni darshan", 3)], tip="Navratri brings 2–4 hour queues")
add("jwalaji", "Jwala Ji", "ज्वाला जी", 31.8760, 76.3250, "pilgrim", "temple", "pilgrim",
    [("Jwalamukhi Devi darshan (eternal flames)", 3), ("Gorakh Dibbi", 2)])
add("kangra", "Kangra (Brajeshwari Devi)", "कांगड़ा (बज्रेश्वरी देवी)", 32.1000, 76.2690, "pilgrim", "temple", "pilgrim",
    [("Maa Brajeshwari Devi darshan", 3), ("Kangra Fort", 6), ("Masroor rock-cut temples", 70)])
add("chamunda", "Chamunda Devi", "चामुंडा देवी", 32.1446, 76.4011, "pilgrim", "temple", "pilgrim",
    [("Chamunda Nandikeshwar Dham darshan", 3)])
add("katra", "Katra (Vaishno Devi)", "कटरा (वैष्णो देवी)", 32.9916, 74.9318, "kashmir", "temple", "pilgrim",
    [("Mata Vaishno Devi Bhawan (13 km trek / helicopter)", 0, "Yatra registration (RFID card) required"), ("Shiv Khori", 160)],
    tip="Keep a full day for the Bhawan trek")

# ---------- Kashmir ----------
add("srinagar", "Srinagar", "श्रीनगर", 34.0837, 74.7973, "kashmir", "stay", "kashmir",
    [("Dal Lake shikara ride", 10), ("Mughal Gardens — Nishat, Shalimar, Chashme Shahi", 30), ("Shankaracharya Temple", 15),
     ("Doodhpathri", 90), ("Yusmarg", 100)], tip="One night on a houseboat is a classic")
add("gulmarg", "Gulmarg", "गुलमर्ग", 34.0484, 74.3805, "kashmir", "stay", "kashmir",
    [("Gulmarg Gondola (book online)", 5), ("Khilanmarg walk", 6), ("Strawberry valley", 10)])
add("pahalgam", "Pahalgam", "पहलगाम", 34.0161, 75.3150, "kashmir", "stay", "kashmir",
    [("Aru, Betaab & Chandanwari valleys (local union taxi)", 50), ("Baisaran meadow (pony)", 10)])
add("sonamarg", "Sonamarg", "सोनमर्ग", 34.3030, 75.2930, "kashmir", "stay", "kashmir",
    [("Thajiwas Glacier (pony)", 10), ("Zero Point, Zojila (local taxi)", 60)])

# ---------- Ladakh ----------
add("kargil", "Kargil", "कारगिल", 34.5539, 76.1349, "ladakh", "stay", "ladakh",
    [("Kargil War Memorial, Drass", 120)])
add("leh", "Leh", "लेह", 34.1526, 77.5771, "ladakh", "stay", "ladakh",
    [("Shanti Stupa & Leh Palace", 10), ("Hall of Fame & Magnetic Hill", 70), ("Thiksey, Shey & Hemis monasteries", 90),
     ("Sangam — Indus & Zanskar", 70)], tip="Rest day on arrival (3,500 m) is a must", local_km=70)
add("nubra", "Nubra Valley (Hunder)", "नुब्रा घाटी", 34.5800, 77.4700, "ladakh", "stay", "ladakh",
    [("Hunder sand dunes & Bactrian camels", 5), ("Diskit Monastery", 15), ("Turtuk village", 160)])
add("pangong", "Pangong Lake", "पैंगोंग झील", 33.9450, 78.4200, "ladakh", "stay", "ladakh",
    [("Pangong lakeside sunrise", 5)], tip="Camps/cottages, very cold nights")
add("sarchu", "Sarchu (camps)", "सरचू", 32.9100, 77.5800, "ladakh", "stay", "remote",
    [("Camp stay on the Manali–Leh highway", 0)], months=SUMMER)

# ---------- Uttarakhand ----------
add("haridwar", "Haridwar", "हरिद्वार", 29.9457, 78.1642, "uttarakhand", "temple", "pilgrim",
    [("Har Ki Pauri Ganga Aarti", 5), ("Mansa Devi & Chandi Devi (ropeway)", 10)])
add("rishikesh", "Rishikesh", "ऋषिकेश", 30.0869, 78.2676, "uttarakhand", "stay", "hill",
    [("Triveni Ghat aarti", 5), ("Ram Jhula, Laxman Jhula & Beatles Ashram", 10), ("River rafting at Shivpuri (Get Quote)", 40),
     ("Neelkanth Mahadev", 60)])
add("mussoorie", "Mussoorie", "मसूरी", 30.4598, 78.0644, "uttarakhand", "stay", "hill_premium",
    [("Kempty Falls", 30), ("Mall Road & Gun Hill", 5), ("Landour & Char Dukan", 10), ("Dhanaulti", 60)])
add("barkot", "Barkot", "बड़कोट", 30.8090, 78.2070, "uttarakhand", "temple", "pilgrim",
    [("Yamunotri Dham (6 km trek from Janki Chatti)", 90, "Char Dham registration required")], months=DHAM)
add("uttarkashi", "Uttarkashi", "उत्तरकाशी", 30.7268, 78.4354, "uttarakhand", "temple", "pilgrim",
    [("Gangotri Dham", 200, "Char Dham registration required"), ("Kashi Vishwanath, Uttarkashi", 5)], months=DHAM)
add("guptkashi", "Guptkashi / Sitapur", "गुप्तकाशी", 30.5240, 79.0800, "uttarakhand", "temple", "pilgrim",
    [("Kedarnath Dham (16 km trek from Gaurikund / helicopter)", 60, "Char Dham registration required")], months=DHAM,
    tip="Kedarnath needs 2 nights here: trek up, darshan, trek down")
add("joshimath", "Joshimath / Pipalkoti", "जोशीमठ", 30.5550, 79.5640, "uttarakhand", "stay", "pilgrim",
    [("Auli (ropeway / road)", 30)])
add("badrinath", "Badrinath", "बद्रीनाथ", 30.7433, 79.4938, "uttarakhand", "temple", "pilgrim",
    [("Badrinath Dham darshan & Tapt Kund", 3, "Char Dham registration required"), ("Mana — first Indian village", 6)], months=DHAM)
add("nainital", "Nainital", "नैनीताल", 29.3803, 79.4636, "uttarakhand", "stay", "hill_premium",
    [("Naini Lake boating & Mall Road", 5), ("Bhimtal, Sattal & Naukuchiatal", 50), ("Kainchi Dham (Neem Karoli Baba)", 40)])
add("corbett", "Jim Corbett (Ramnagar)", "जिम कॉर्बेट", 29.3940, 79.1260, "uttarakhand", "stay", "hill",
    [("Jungle safari — Bijrani / Jhirna / Dhikala (book online)", 40), ("Garjiya Devi Temple", 15)])

PLACES = P
