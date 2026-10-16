# -*- coding: utf-8 -*-
"""Suzu Trip Planner — master place list (v0.1, 15 Oct 2026).

Each place: id, name, hi (Hindi name), lat, lon, region, kind, cls (hotel class), stay (can overnight),
months (open months, None = all year), sights [(name, extra_km_round_trip, note[, open_months])], tip.

kind:  hub   = arrival / departure city (airport / railhead)
       stay  = overnight destination
       temple= shrine town (pilgrim circuits)
cls (hotel class, see rates.json):  metro, hill_premium, hill, remote, pilgrim, pilgrim_city, kashmir, ladakh
"""

P = []
def add(id, name, hi, lat, lon, region, kind, cls, sights=(), months=None, tip="", stay=True, local_km=60):
    P.append(dict(id=id, name=name, hi=hi, lat=lat, lon=lon, region=region, kind=kind, cls=cls,
                  stay=stay, months=months, local_km=local_km,
                  sights=[dict(n=s[0], km=s[1], note=(s[2] if len(s) > 2 else ""), **({"m": s[3]} if len(s) > 3 else {})) for s in sights], tip=tip))

SUMMER = [6, 7, 8, 9, 10]           # high passes (Kunzum, Baralacha, Chandratal, Manali-Leh road)
ROHTANG = [5, 6, 7, 8, 9, 10, 11]   # Rohtang Pass usually open mid-May to mid-Nov (snow closes it in winter)
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
     ("Vashisht hot springs", 8), ("Rohtang Pass (permit, May–Nov)", 110, "Online permit needed; closed in winter", ROHTANG), ("Naggar Castle", 45)], local_km=80)
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
add("katra", "Katra (Vaishno Devi)", "कटरा (वैष्णो देवी)", 32.9916, 74.9318, "kashmir", "temple", "pilgrim_city",
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
add("haridwar", "Haridwar", "हरिद्वार", 29.9457, 78.1642, "uttarakhand", "temple", "pilgrim_city",
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

# ---------- v0.5 (16 Oct 2026): Agra & Mathura, Rajasthan, Kumaon & Garhwal extras, Himachal extras, J&K / Ladakh extras ----------
# ---- Uttar Pradesh: Agra & Braj ----
add("agra", "Agra", "आगरा", 27.1767, 78.0081, "up", "stay", "metro",
    [("Taj Mahal at sunrise (closed Fridays)", 10, "Buy tickets online; closed on Fridays"), ("Agra Fort", 8), ("Mehtab Bagh sunset view", 15),
     ("Fatehpur Sikri", 80), ("Itimad-ud-Daulah (Baby Taj)", 10)], tip="Agra Cantt railway / Yamuna Expressway from Delhi (~3.5 h)")
add("mathura", "Mathura – Vrindavan", "मथुरा – वृंदावन", 27.4924, 77.6737, "up", "temple", "pilgrim_city",
    [("Shri Krishna Janmabhoomi darshan", 5), ("Banke Bihari & Prem Mandir, Vrindavan", 25), ("ISKCON Vrindavan", 25),
     ("Govardhan parikrama (21 km, optional)", 50), ("Barsana & Nandgaon", 110)], tip="Keep phones/leather items out at Janmabhoomi; evening Prem Mandir lights")
# ---- Rajasthan ----
add("jaipur", "Jaipur", "जयपुर", 26.9124, 75.7873, "rajasthan", "hub", "rajasthan",
    [("Amber Fort & Jal Mahal", 30), ("Hawa Mahal, City Palace & Jantar Mantar", 10), ("Nahargarh sunset", 20),
     ("Chokhi Dhani evening", 40), ("Birla Mandir & Albert Hall", 10)], tip="Jaipur airport / railway station pickup", local_km=70)
add("pushkar", "Pushkar – Ajmer", "पुष्कर – अजमेर", 26.4897, 74.5511, "rajasthan", "temple", "pilgrim",
    [("Brahma Temple & Pushkar Lake ghats", 3), ("Ajmer Sharif Dargah", 30), ("Savitri Mata ropeway", 5)],
    tip="Camel fair in Kartik (Oct/Nov) — hotels fill up")
add("ranthambore", "Ranthambore (Sawai Madhopur)", "रणथंभौर", 26.0173, 76.5026, "rajasthan", "stay", "rajasthan",
    [("Jungle safari — morning / afternoon (book online, Get Quote)", 40), ("Ranthambore Fort & Trinetra Ganesh", 20)],
    months=[10, 11, 12, 1, 2, 3, 4, 5, 6], tip="Park closed July–September for monsoon; safaris book out 30+ days ahead")
add("bikaner", "Bikaner", "बीकानेर", 28.0229, 73.3119, "rajasthan", "stay", "rajasthan",
    [("Junagarh Fort", 5), ("Karni Mata Temple, Deshnok", 65), ("Camel Research Centre", 20)])
add("jaisalmer", "Jaisalmer", "जैसलमेर", 26.9157, 70.9083, "rajasthan", "stay", "rajasthan",
    [("Golden Fort & Patwon ki Haveli", 5), ("Sam sand dunes — camel ride & desert camp", 90), ("Gadisar Lake sunrise", 5),
     ("Kuldhara & Longewala war memorial", 250)], tip="Desert camp night at Sam is the highlight; very hot Apr–Jun", local_km=70)
add("jodhpur", "Jodhpur", "जोधपुर", 26.2389, 73.0243, "rajasthan", "stay", "rajasthan",
    [("Mehrangarh Fort & Jaswant Thada", 10), ("Blue City walk & Clock Tower market", 5), ("Umaid Bhawan Palace museum", 10),
     ("Osian temples", 130)])
add("kumbhalgarh", "Kumbhalgarh – Ranakpur", "कुंभलगढ़ – रणकपुर", 25.1528, 73.5872, "rajasthan", "stay", "remote",
    [("Kumbhalgarh Fort — 36 km wall", 5), ("Ranakpur Jain Temple", 70)])
add("udaipur", "Udaipur", "उदयपुर", 24.5854, 73.7125, "rajasthan", "stay", "rajasthan",
    [("City Palace & Lake Pichola boat ride", 8), ("Jagdish Temple & Bagore ki Haveli dance show", 5), ("Sajjangarh (Monsoon Palace) sunset", 20),
     ("Eklingji & Nathdwara (Shrinathji)", 100), ("Chittorgarh Fort", 240)], local_km=70)
add("mountabu", "Mount Abu", "माउंट आबू", 24.5926, 72.7156, "rajasthan", "stay", "hill",
    [("Dilwara Jain Temples", 5), ("Nakki Lake & Sunset Point", 5), ("Guru Shikhar", 30), ("Achalgarh", 20)])
# ---- Uttarakhand: Kumaon & Garhwal extras ----
add("kathgodam", "Kathgodam / Haldwani", "काठगोदाम", 29.2650, 79.5470, "uttarakhand", "hub", "metro", tip="Railhead for Nainital & Kumaon (Shatabdi / Ranikhet Express)")
add("kainchi", "Kainchi Dham", "कैंची धाम", 29.4150, 79.5136, "uttarakhand", "temple", "pilgrim",
    [("Neem Karoli Baba ashram darshan", 2, "No photography inside; big crowd on 15 June bhandara")], tip="Usually a stop on the way to Nainital / Almora; stays are limited")
add("bhimtal", "Bhimtal – Sattal", "भीमताल – सातताल", 29.3445, 79.5631, "uttarakhand", "stay", "hill",
    [("Bhimtal Lake & island aquarium", 3), ("Sattal birding & boating", 15), ("Naukuchiatal", 10)])
add("mukteshwar", "Mukteshwar", "मुक्तेश्वर", 29.4722, 79.6479, "uttarakhand", "stay", "hill",
    [("Mukteshwar Mahadev & Chauli ki Jali", 3), ("Himalayan sunrise view", 2), ("Fruit orchards & Bhalu Gaad waterfall", 15)])
add("almora", "Almora", "अल्मोड़ा", 29.5971, 79.6591, "uttarakhand", "stay", "hill",
    [("Kasar Devi Temple", 10), ("Jageshwar Dham (124 temples)", 70), ("Binsar Wildlife Sanctuary & Zero Point", 60), ("Chitai Golu Devta", 15)])
add("kausani", "Kausani", "कौसानी", 29.8425, 79.6027, "uttarakhand", "stay", "hill",
    [("300 km Himalayan panorama — Trishul, Nanda Devi", 2), ("Anasakti (Gandhi) Ashram", 2), ("Baijnath Temple, Garur", 40), ("Tea estate", 5)])
add("ranikhet", "Ranikhet", "रानीखेत", 29.6434, 79.4322, "uttarakhand", "stay", "hill",
    [("Jhula Devi Temple & Chaubatia Gardens", 15), ("Majkhali view point", 25), ("Golf course & KRC Museum", 5)])
add("lansdowne", "Lansdowne", "लैंसडाउन", 29.8377, 78.6871, "uttarakhand", "stay", "hill",
    [("Tip-n-Top & Bhulla Tal", 5), ("Tarkeshwar Mahadev", 70), ("St Mary's Church & War Memorial", 3)])
add("dhanaulti", "Dhanaulti – Kanatal", "धनोल्टी – कानाताल", 30.4267, 78.2413, "uttarakhand", "stay", "hill",
    [("Eco Park & Surkanda Devi (ropeway)", 15), ("Tehri Lake water sports (Get Quote)", 50), ("Camp evening", 0)])
add("chopta", "Chopta – Tungnath", "चोपता – तुंगनाथ", 30.4895, 79.1927, "uttarakhand", "stay", "remote",
    [("Tungnath Temple & Chandrashila trek (4 km, 3,680 m)", 5, "Trek starts at dawn; temple open ~May–Nov"), ("Deoria Tal", 25), ("Ukhimath Omkareshwar", 30)],
    months=[3, 4, 5, 6, 9, 10, 11, 12], tip="Camps and small lodges; heavy snow Jan–Feb, road often shut")
add("auli", "Auli", "औली", 30.5293, 79.5658, "uttarakhand", "stay", "remote",
    [("Auli ropeway & Gorson Bugyal", 5), ("Skiing / snow play Jan–Mar (Get Quote)", 0), ("Joshimath Narsingh Temple", 15), ("Badrinath day trip (May–Oct)", 90, "", DHAM)],
    tip="Via Joshimath; SUV advised. Snow Dec–Mar, meadows Apr–Jun")
# ---- Himachal extras ----
add("khajjiar", "Khajjiar", "खज्जियार", 32.5490, 76.0620, "himachal", "stay", "hill",
    [("Khajjiar meadow & lake — Mini Switzerland", 2), ("Kalatop Wildlife Sanctuary", 15), ("Zorbing & horse ride (Get Quote)", 0)],
    tip="Road from Dalhousie can close after heavy snow (Jan–Feb)")
add("barot", "Barot", "बरोट", 32.0330, 76.8450, "himachal", "stay", "remote",
    [("Uhl river & trout fishing", 3), ("Nargu Wildlife Sanctuary walk", 10), ("Lohardi & Rajgundha", 40)])
add("rewalsar", "Rewalsar", "रिवालसर", 31.6340, 76.8330, "himachal", "temple", "pilgrim",
    [("Rewalsar Lake — Padmasambhava statue, gurudwara & temples", 2), ("Naina Devi (Rewalsar) & seven lakes", 15)], stay=True)
add("baijnath", "Baijnath", "बैजनाथ", 32.0523, 76.6487, "himachal", "temple", "pilgrim",
    [("Baijnath Shiva Temple (1204 AD)", 2), ("Bir Tibetan colony", 15)], tip="Usually a 1-hour stop between Palampur and Bir/Mandi")
add("shoja", "Shoja", "शोजा", 31.5560, 77.3650, "himachal", "stay", "hill",
    [("Jalori Pass & Serolsar Lake (5 km walk)", 15), ("Raghupur Fort meadow", 15), ("Waterfall point", 5)],
    months=[3, 4, 5, 6, 7, 8, 9, 10, 11, 12], tip="Jalori Pass closes in heavy snow (Jan–Feb)")
# ---- Punjab ----
add("anandpur", "Anandpur Sahib", "आनंदपुर साहिब", 31.2390, 76.5020, "punjab", "temple", "pilgrim",
    [("Takht Sri Kesgarh Sahib", 2), ("Virasat-e-Khalsa museum (closed Mondays)", 3), ("Naina Devi (ropeway)", 20)])
# ---- Jammu & Kashmir / Ladakh extras ----
add("patnitop", "Patnitop", "पटनीटॉप", 33.0880, 75.3270, "kashmir", "stay", "hill",
    [("Nathatop & Sanasar meadow (paragliding, Get Quote)", 30), ("Patnitop skyview gondola", 10), ("Naag Mandir & pine walks", 3)],
    tip="2 h from Katra — a cool break after the Vaishno Devi trek")
add("lamayuru", "Lamayuru", "लामायुरू", 34.2830, 76.7730, "ladakh", "stay", "ladakh",
    [("Lamayuru Monastery & moonland", 3), ("Alchi Monastery", 60), ("Fotu La view", 15)])
add("tsomoriri", "Tso Moriri (Korzok)", "त्सो मोरीरी", 32.9630, 78.2640, "ladakh", "stay", "remote",
    [("Tso Moriri lakeside & Korzok Monastery", 3), ("Puga hot springs & Tso Kar", 60)],
    months=[5, 6, 7, 8, 9, 10], tip="4,500 m — only after 2+ nights in Leh; Inner Line Permit")

PLACES = P
