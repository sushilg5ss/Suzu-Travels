P = "chillai-kalan"
G = "gulmarg-snowfall"
H = "pahalgam-snowfall"
S = "sonmarg-snowfall"
R = "srinagar-ka-mausam"
SPEC = dict(
    lang="en",
    slug="chillai-kalan",
    title="Chillai Kalan 2026–27: Dates, Weather and Travelling in Kashmir's 40 Coldest Days",
    seo_title="Chillai Kalan 2026–27: Dates, Weather & Kashmir Travel Guide",
    seo_desc="Chillai Kalan 2026–27 runs from 21 December 2026 to 29 January 2027, followed by Chillai Khurd and Chillai Bachha. Live Srinagar, Gulmarg and Pahalgam forecast, how cold it gets, frozen pipes and Dal Lake, pheran and kangri, and how to travel safely.",
    focus="chillai kalan, chillai kalan 2026",
    photo_pick=dict(slugs=[P, G, H, S, R], ids=[
        (P + ":hero-1", "hero", "Jamia Masjid, Srinagar, in winter", "Jamia Masjid, Srinagar, under winter snow"),
        (P + ":fig-1", "fig", "A Kashmiri kangri", "A Kashmiri kangri — an earthen fire-pot in a wicker basket"),
        (G + ":g-4", "g", "The Gulmarg meadow under snow", "The Gulmarg meadow under snow"),
        (P + ":g-1", "g", "Jamia Masjid in winter", "Jamia Masjid courtyard in winter"),
        (H + ":g-6", "g", "Betaab Valley in winter", "Betaab Valley under snow"),
        (S + ":hero-1", "g", "Thajiwas, Sonamarg, under snow", "Thajiwas, Sonamarg, under snow"),
        (P + ":g-2", "g", "A giant kangri", "A giant kangri on display in Srinagar"),
        (R + ":hero-1", "g", "Houseboats on Dal Lake", "Houseboats on Dal Lake, Srinagar"),
        (G + ":g-6", "g", "Gulmarg in December", "Snow-covered road and pines at Gulmarg in December"),
    ]),
    kicker="Kashmir winter · 21 Dec – 29 Jan · live weather",
    tag="Chillai Kalan: Kashmir's 40 harshest days",
    sub="When Chillai Kalan starts and ends, how cold Srinagar, Gulmarg and Pahalgam get, what freezes, how Kashmiris keep warm, and how to plan a trip in the coldest weeks of the year.",
    chips=[("21 Dec", "starts"), ("29 Jan", "ends"), ("40 days", "Chillai Kalan"), ("Live", "3 places")],
    flakes=True,
    updated="November 2026",
    wa="Hello Suzu Travels, I am planning Kashmir in December/January (Chillai Kalan). Dates: ___ , people: ___ , starting from: ___",
    cta2=("#weather", "See today's weather"),
    answer="<b>Chillai Kalan is the 40-day core of the Kashmir winter, from 21 December to 29 January</b> — so for this season, <b>21 December 2026 to 29 January 2027</b>. It is followed by <b>Chillai Khurd</b> (\"the small cold\", 30 January–18 February) and <b>Chillai Bachha</b> (\"the baby cold\", 19–28 February). Nights stay below freezing, parts of Dal Lake can freeze, water pipes freeze, and snow that falls in these weeks lasts and feeds the glaciers. Srinagar averages about 7 °C by day and −2 °C at night in January (IMD 1991–2020); Gulmarg about 1 °C and −8 °C. It is also the best time for snow at Gulmarg, Sonamarg and Pahalgam — if you plan for the cold and for road and flight delays.",
    quick=[
        ("Chillai Kalan", "21 December – 29 January (40 days)."),
        ("Chillai Khurd", "30 January – 18 February (20 days)."),
        ("Chillai Bachha", "19 – 28 February (10 days)."),
        ("Srinagar, January", "About 7 °C by day, −2 °C at night."),
        ("Gulmarg, January", "About 1 °C by day, −8 °C at night."),
    ],
    wx=dict(src="/suzu-weather-feed.json", daily=True, kicker="Live forecast", h2="Srinagar, Gulmarg and Pahalgam weather today",
            lead="Srinagar (1,585 m), Gulmarg (2,650 m) and Pahalgam (2,200 m) — current temperature and the next days' high, low, rain and snow.",
            places=[dict(id="srinagar", name="Srinagar", alt="1585"), dict(id="gulmarg", name="Gulmarg", alt="2650"), dict(id="pahalgam", name="Pahalgam", alt="2200")]),
    sections=[
        dict(id="cold", kicker="How cold", h2="How cold does it get in Chillai Kalan?", ps=[
            "These are India Meteorological Department averages for 1991–2020 for the two Chillai Kalan months. Single cold snaps go well below them — on 21 December 2024, the first night of Chillai Kalan, Pahalgam fell to −8.6 °C and Gulmarg to −6.2 °C (Kashmir Reader / PTI).",
        ], table=(["Place", "December avg high / low", "January avg high / low", "What to expect"], [
            ["Srinagar (1,585 m)", "9.9° / −1.6 °C", "7.1° / −1.9 °C", "Freezing nights, foggy mornings; snow some days"],
            ["Pahalgam (2,200 m)", "7.9° / −4.2 °C", "4.9° / −6.1 °C", "Snowbound valley; side roads close after snow"],
            ["Gulmarg (2,650 m)", "4.6° / −4.8 °C", "0.7° / −7.7 °C", "Deep snow; skiing; chains/4×4 rule"],
        ]), after=[
            "Full monthly figures: <a href=\"/weather/srinagar/\">Srinagar weather</a>, <a href=\"/weather/gulmarg/\">Gulmarg weather</a>, <a href=\"/weather/pahalgam/\">Pahalgam weather</a>.",
        ]),
        dict(id="life", kicker="Life in the cold", h2="What happens in Kashmir during Chillai Kalan", fig=True, ps=[
            "<b>Freezing:</b> water pipes in homes and hotels often freeze overnight, and parts of Dal Lake and other water bodies can freeze in the coldest spells. Electricity demand for heating rises sharply, and power cuts are common.",
            "<b>Keeping warm:</b> Kashmiris wear the <b>pheran</b>, a long woollen cloak (21 December is observed as Pheran Day), and carry a <b>kangri</b> — an earthen pot of embers in a wicker basket — under it. Hearty foods such as <b>harissa</b>, a slow-cooked meat dish sold from early-morning shops in Srinagar, are a winter staple.",
            "<b>Travel:</b> snow, ice and poor visibility can close the Jammu–Srinagar highway (NH-44) and delay or cancel flights at Srinagar airport. Keep a buffer day at the end of your trip, and book hotels with proper heating.",
        ]),
        dict(id="travel", kicker="Planning a trip", h2="Should you visit Kashmir in Chillai Kalan?", ps=[
            "<b>Yes, if you want snow.</b> These weeks bring the most reliable snow at <a href=\"/gulmarg-ka-mausam/\">Gulmarg</a>, <a href=\"/sonamarg-ka-mausam/\">Sonamarg</a> and <a href=\"/pahalgam-ka-mausam/\">Pahalgam</a>, and Srinagar's houseboats and Mughal gardens look very different under snow.",
            "<b>Plan for the cold:</b> thermals, a down jacket, waterproof boots and gloves; confirm room heating (electric blankets or central heating) when you book. Put Gulmarg on the clearest forecast day; after snow, only 4×4s or cars with chains are allowed on the Tangmarg–Gulmarg road.",
            "<b>Be flexible:</b> the highway and flights can be disrupted for a day or two after heavy snow — avoid tight connections on your last day. More: <a href=\"/kashmir-in-december/\">Kashmir in December</a> and <a href=\"/kashmir-in-january/\">Kashmir in January</a>.",
        ]),
    ],
    gallery=dict(h2="Kashmir in Chillai Kalan", lead="Snow at Gulmarg, Sonamarg and Pahalgam, Srinagar in winter, and the kangri — real photographs, each credited to its photographer."),
    spots=dict(kicker="Where to go", h2="Best places to visit during Chillai Kalan", lead="If you are travelling between 21 December and 29 January.", items=[
        ("Gulmarg", "Skiing and the gondola", "Deepest snow; keep a spare half-day for the gondola."),
        ("Sonamarg", "Snow day trip", "Reachable all winter through the Z-Morh tunnel."),
        ("Pahalgam", "Snowbound valley", "Town and Betaab valley; side roads close after snow."),
        ("Srinagar", "Houseboats and gardens", "Freezing nights; harissa breakfasts."),
        ("Doodhpathri", "Quiet snowfields", "Road can close after heavy snow."),
        ("Patnitop", "On the way from Jammu", "Snow on the highway hills."),
    ]),
    sections2=[
        dict(id="tips", kicker="Before you go", h2="Chillai Kalan travel checklist", ps=[
            "Thermals, down jacket, waterproof boots, gloves, cap and sunglasses; a buffer day before your flight home; hotels with confirmed heating; and a driver who carries chains. Check the J&K Traffic Police advisory each morning.",
        ]),
    ],
    ctas=dict(h2="Our Kashmir winter trips", lead="Hotels with heating, meals, and a private car with a winter-road driver.", items=[
        ("/best-kashmir-tour-package/", "Kashmir tour package", "From ₹16,999 per person. Srinagar, Gulmarg, Pahalgam and Sonamarg.", "Kashmir"),
        ("/gulmarg-tour-package/", "Gulmarg tour package", "From ₹16,999 per person; gondola help.", "Gulmarg"),
        ("/kashmir-in-january/", "Kashmir in January", "What is open and what to wear.", "Guide"),
        ("/cabs/srinagar-taxi-service/", "Srinagar taxi", "Private car with a driver used to winter roads.", "Cab"),
    ]),
    quote_h2="Planning Kashmir in the snow?",
    quote_text="Tell us your dates and how many of you are travelling. We put Gulmarg on the clearest day, book heated rooms, keep a buffer day for the weather, and send a written quote with hotels, meals and a private car. Suzu Travels is a travel agent registered with HP Tourism, based in Bilaspur, Himachal Pradesh, and plans trips across north India.",
    faq_h2="Chillai Kalan: frequently asked questions",
    faqs=[
        ("When is Chillai Kalan 2026–27?", "From 21 December 2026 to 29 January 2027 — 40 days."),
        ("What comes after Chillai Kalan?", "Chillai Khurd (30 January–18 February) and then Chillai Bachha (19–28 February)."),
        ("How cold is Srinagar in Chillai Kalan?", "IMD averages for January are about 7 °C by day and −2 °C at night; cold snaps go lower."),
        ("Does Dal Lake freeze?", "Parts of Dal Lake can freeze during the coldest spells of Chillai Kalan, though not every year."),
        ("Is it a good time to visit Kashmir?", "Yes for snow at Gulmarg, Sonamarg and Pahalgam — if you pack for the cold, book heated rooms and keep a buffer day for road and flight delays."),
        ("What are pheran and kangri?", "The pheran is a long woollen cloak; the kangri is an earthen pot of embers in a wicker basket carried under it for warmth."),
    ],
    sources=[
        ("MET Norway Locationforecast (CC BY 4.0) — live forecast data", "https://api.met.no/"),
        ("Wikipedia: Chillai Kalan — dates and winter life", "https://en.wikipedia.org/wiki/Chillai_Kalan"),
        ("India Meteorological Department — Srinagar, Gulmarg and Pahalgam normals 1991–2020", "https://mausam.imd.gov.in/"),
    ],
)
