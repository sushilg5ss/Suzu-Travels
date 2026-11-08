import blogkit as K

PTS = [
    ("manali", "Manali", 2050, "Himachal", "/snowfall-in-manali/"),
    ("shimla", "Shimla", 2205, "Himachal", "/shimla-snowfall/"),
    ("solang", "Solang Valley", 2480, "Himachal", "/adventure/snow-activities-manali/"),
    ("kufri", "Kufri", 2620, "Himachal", "/kufri-snowfall/"),
    ("gulmarg", "Gulmarg", 2650, "Kashmir", "/gulmarg-snowfall/"),
    ("narkanda", "Narkanda", 2708, "Himachal", "/adventure/snow-and-skiing-in-narkanda/"),
    ("auli", "Auli", 2800, "Uttarakhand", "/auli-in-december/"),
    ("sissu", "Sissu · Atal Tunnel", 3130, "Himachal", "/adventure/atal-tunnel-sissu-snow-trip/"),
]

GUIDES = [("Shimla snowfall", "/shimla-snowfall/"), ("Kufri snowfall", "/kufri-snowfall/"), ("Snowfall in Manali", "/snowfall-in-manali/"),
          ("Dharamshala snowfall", "/dharamshala-snowfall/"), ("Dalhousie snowfall", "/dalhousie-snowfall/"), ("Kasauli snowfall", "/kasauli-snowfall/"),
          ("Narkanda snow & skiing", "/adventure/snow-and-skiing-in-narkanda/"), ("Sissu & Atal Tunnel", "/adventure/atal-tunnel-sissu-snow-trip/"),
          ("Himachal snowfall 2026-27", "/himachal-snowfall-winter-2026-27/"), ("Gulmarg snowfall", "/gulmarg-snowfall/"), ("Sonmarg snowfall", "/sonmarg-snowfall/"),
          ("Pahalgam snowfall", "/pahalgam-snowfall/"), ("Kashmir snowfall", "/kashmir-snowfall/"), ("Auli snowfall", "/auli-snowfall/"),
          ("Mussoorie snowfall", "/mussoorie-snowfall/"), ("Winter Spiti", "/winter-spiti-valley-guide-2026-27/"),
          ("बर्फबारी (हिंदी)", "/barfbari/"), ("हिमाचल का मौसम", "/himachal-ka-mausam/"), ("शिमला का मौसम", "/shimla-ka-mausam/"), ("मनाली का मौसम", "/manali-ka-mausam/"), ("कुफरी का मौसम", "/kufri-ka-mausam/"), ("धर्मशाला का मौसम", "/dharamshala-ka-mausam/"), ("कश्मीर का मौसम", "/kashmir-ka-mausam/")]
GUIDE_HTML = '<div class="szb-chiplinks">' + "".join(f'<a href="{h}">❄ {t}</a>' for t, h in GUIDES) + '</div>'

SPEC = dict(
    slug="snow-tracker",
    title="Snow Tracker 2026-27: Where Is It Snowing in India This Week?",
    seo_title="Where Is It Snowing in India? Live Snow Tracker 2026-27",
    seo_desc="Live 7-day snow forecast for 8 snow points in India — Manali, Solang, Sissu, Shimla, Kufri, Narkanda, Gulmarg and Auli — with snow months and trip tips.",
    focus="snowfall places in india",
    photo_pick=dict(slugs=["gulmarg-snowfall", "shimla-snowfall"], ids=[
        (19097, "hero"), (19093, "g"), (19087, "g"), (19096, "g"), (19091, "g"), (19103, "g"), (19092, "g")]),
    kicker="Live · 8 snow points · Himachal · Kashmir · Uttarakhand",
    tag="Where is it snowing in India this week?",
    sub="One live board for the snow points travellers ask us about most — from Manali and Shimla to Gulmarg and Auli. It reads the latest forecast through the day, so you can see where snow is likely before you book.",
    chips=[("8", "snow points"), ("7 days", "forecast"), ("Updated", "through the day"), ("Free", "no sign-up")],
    flakes=True,
    alt_lang=("/barfbari/", "हिंदी में: बर्फबारी ट्रैकर"),
    updated="November 2026",
    wa="Hi Suzu Travels, I want to see snow. Dates: ___ , people: ___ , from city: ___ . Which snow point is best for us?",
    cta2=("#forecast", "See the live board"),
    answer="<b>In a normal Indian winter, snow is most likely from late December to February</b> at the hill stations people can reach by road — Manali, Shimla, Kufri, Narkanda, Gulmarg and Auli. Higher points get it earlier and keep it longer: <b>Sissu and the Atal Tunnel (about 3,130 m)</b> and the upper slopes of Gulmarg often see snow from October, while <b>Manali (about 2,050 m)</b> and <b>Shimla (about 2,205 m)</b> town may wait until late December or January. The live board below shows which of these eight places have snow in the 7-day forecast right now.",
    quick=[
        ("Surest snow", "Gulmarg and Sissu — high, and snowy for most of the winter."),
        ("Closest to Delhi & Chandigarh", "Kufri and Narkanda, above Shimla."),
        ("Earliest snow", "Sissu, Atal Tunnel and Gulmarg's Apharwat, often from October."),
        ("Best for skiing", "Gulmarg first; Auli and Narkanda in a good winter."),
        ("Peak months", "January and February at almost every point."),
    ],
    snow=dict(first=True, sort=True, summary=True, ids=[p[0] for p in PTS], h2="Where is it snowing this week?", h3="Live snow board · next 7 days",
              links={p[0]: p[4] for p in PTS},
              lead="All eight snow points, sorted with the snowiest week first. Bars show forecast snow per day; a gold outline means snow is in this week's forecast. Tap a place for its full snow guide."),
    sections=[
        dict(id="altitude", kicker="Why height matters", h2="Eight snow points, from lowest to highest", html=K.ladder(PTS), ps=[
            "Snow in the Indian Himalaya depends mostly on height. When a winter weather system arrives, the snow line can sit at 2,500 m one week and 2,000 m the next — so the higher points on this list get snow first, more often, and keep it longest.",
        ], after=[
            "A gold glow on a bar means snow is in that place's forecast this week. If the lower towns are bare, the higher points nearby usually are not: Solang and Sissu above Manali, Kufri and Narkanda above Shimla, Kongdoori and Apharwat above Gulmarg.",
        ]),
        dict(id="compare", kicker="Compare", h2="India's snow points compared", ps=[
            "Usual snow months are a pattern from recent winters, not a promise — use the live board for your dates.",
        ], table=(["Place", "Height", "Getting there", "Usual snow", "Guide"], [
            ["Manali, Himachal", "~2,050 m", "Chandigarh ~300 km by road; Bhuntar airport ~50 km", "Late Dec–Feb in town", "<a href=\"/snowfall-in-manali/\">Snowfall in Manali</a>"],
            ["Shimla, Himachal", "~2,205 m", "Chandigarh ~115 km, 3–3.5 h", "Late Dec–Feb; January most likely", "<a href=\"/shimla-snowfall/\">Shimla snowfall</a>"],
            ["Solang Valley, Himachal", "~2,480 m", "~14 km from Manali", "Dec–Feb; often snowy when Manali is not", "<a href=\"/adventure/snow-activities-manali/\">Snow activities</a>"],
            ["Kufri, Himachal", "~2,620 m", "~16 km from Shimla", "Late Dec–Feb", "<a href=\"/kufri-snowfall/\">Kufri snowfall</a>"],
            ["Gulmarg, Kashmir", "~2,650 m", "Srinagar ~50 km, 1.5–2 h", "Dec–Mar; Apharwat from Oct", "<a href=\"/gulmarg-snowfall/\">Gulmarg snowfall</a>"],
            ["Narkanda, Himachal", "~2,708 m", "~60–65 km from Shimla", "Dec–Feb; skiing in a good winter", "<a href=\"/adventure/snow-and-skiing-in-narkanda/\">Narkanda snow</a>"],
            ["Auli, Uttarakhand", "~2,800 m", "Above Joshimath; Dehradun airport is the nearest", "Dec–Feb", "<a href=\"/auli-in-december/\">Auli in December</a>"],
            ["Sissu · Atal Tunnel, Himachal", "~3,130 m", "~40 km from Manali via the Atal Tunnel", "Oct–Mar; road may shut after heavy snow", "<a href=\"/adventure/atal-tunnel-sissu-snow-trip/\">Sissu snow trip</a>"],
        ])),
    ],
    gallery=dict(h2="India's snow points in pictures", lead="Gulmarg's Gondola and meadow, Shimla's Mall Road, Kufri and Narkanda — real photographs, each credited to its photographer."),
    spots=dict(kicker="Choose your snow", h2="Which snow point fits your trip?", lead="Six quick answers to the question we hear most every winter.", items=[
        ("Nearest to Delhi & Chandigarh", "Kufri · Narkanda", "A Shimla base with a day in Kufri or Narkanda is the shortest road trip to snow from the plains. See <a href=\"/shimla-snowfall/\">Shimla snowfall</a>."),
        ("Most reliable snow", "Gulmarg", "High, cold and snowy for most of the winter, with a Gondola to the upper slopes. See <a href=\"/gulmarg-snowfall/\">Gulmarg snowfall</a>."),
        ("Snow from October", "Sissu · Atal Tunnel", "Through the tunnel from Manali, Lahaul often has snow weeks before Manali does — when the road is open."),
        ("Families & first snow", "Solang Valley", "Snow play, snow scooters and short rides close to Manali hotels. See <a href=\"/adventure/solang-valley-activities/\">Solang activities</a>."),
        ("Skiing", "Gulmarg · Auli · Narkanda", "Gulmarg for the longest season and runs; Auli and Narkanda for beginners in a good winter."),
        ("No snow on your dates?", "Snow Kingdom, Kufri", "An indoor snow park with real snow all year — see <a href=\"/adventure/snow-kingdom-kufri/\">Snow Kingdom Kufri</a>."),
    ]),
    sections2=[
        dict(id="guides", kicker="Snow guides", h2="Snowfall guides for every snow point", ps=[
            "Month-by-month snow patterns, last winter's dates, the best snow spots and road tips for each place.",
        ], html=GUIDE_HTML),
        dict(id="how", kicker="How it works", h2="How this snow tracker works", ps=[
            "<b>Data:</b> the board reads the 7-day Locationforecast from MET Norway (the Norwegian Meteorological Institute, shared under CC BY 4.0) for each place's exact coordinates and height, refreshed through the day.",
            "<b>Snow amounts:</b> when the forecast says precipitation will fall as snow, we show it as centimetres using the simple rule 1 mm of water ≈ 1 cm of snow. Real snow depth varies with temperature and wind, so read it as a guide.",
            "<b>How far ahead:</b> snow forecasts are useful about a week out and get better each day. We check the board, the roads and local reports again the evening before every snow day we plan.",
        ]),
        dict(id="abroad", kicker="Coming from abroad?", h2="Seeing snow in India as an overseas traveller", ps=[
            "India's snow season runs mainly from late December to February. Most international flights land in Delhi; from there, Srinagar is a short flight for Gulmarg, Chandigarh and Kullu-Bhuntar serve Shimla and Manali, and Dehradun is the nearest airport for Auli.",
            "A typical first snow trip is 5–7 days: a city night in Delhi or Chandigarh, then three or four nights in the hills with one buffer day for weather. See <a href=\"/kashmir-tour-packages-for-international-travellers/\">Kashmir for overseas travellers</a> or ask us for a Himachal plan.",
        ]),
    ],
    ctas=dict(h2="Snow trips we plan", lead="Every trip is quoted for your dates — hotels, breakfast and dinner, and a private cab with a hill driver.", items=[
        ("/packages/himachal-tour-package-shimla-manali/", "Shimla Manali Tour from Chandigarh, 5N/6D", "From ₹12,499 per person off-season (twin sharing). Shimla, Kufri, Manali and Solang.", "Himachal"),
        ("/gulmarg-tour-package/", "Gulmarg tour packages", "From ₹16,999 per person. Srinagar houseboat, Gulmarg with Gondola help, and snow days.", "Kashmir"),
        ("/christmas-new-year-manali-packages/", "Christmas & New Year in the hills", "Snow-season trips for the holiday weeks — book early, hotels fill by mid-December.", "Holiday weeks"),
        ("/himachal-tour-packages/", "All Himachal tour packages", "Compare every Himachal trip we run, side by side.", "All trips"),
    ]),
    quote_h2="Not sure where to go for snow?",
    quote_text="Send us your dates and where you are starting from. We look at the forecast for that week, suggest the snow point most likely to deliver, and send one written quote with hotel, meals and a private cab. Suzu Travels is an HP Tourism registered travel agent based in Bilaspur, Himachal.",
    faqs=[
        ("Where can I see snow in India right now?", "Check the live board at the top of this page — it shows which of eight popular snow points (Manali, Solang, Sissu, Shimla, Kufri, Narkanda, Gulmarg and Auli) have snow in the 7-day forecast. In most winters, Gulmarg and Sissu have snow on the ground for the longest stretch."),
        ("Which place gets snow first in India?", "Among places tourists can reach by road, the high points usually get it first — Sissu and the Atal Tunnel in Lahaul, and Apharwat above Gulmarg, often in October. Apharwat got fresh snow on 14 October 2026 this season."),
        ("Where does it snow in December in India?", "Gulmarg, Sissu and Solang usually have snow in December; Kufri and Narkanda often do; Shimla and Manali town are possible in the second half of the month but not certain."),
        ("Which is better for snow, Manali or Gulmarg?", "Gulmarg is higher and more reliably snowy, and has the Gondola and the best skiing. Manali is easier to reach by road from Delhi and Chandigarh, has more hotels, and puts Solang and Sissu within a short drive. Many travellers choose by starting city and dates."),
        ("What is the nearest snowfall place to Delhi?", "Kufri and Narkanda near Shimla are the nearest regular snow points by road — Shimla is about 350 km from Delhi, Kufri 16 km beyond it. Manali, Solang and Sissu are farther but snowier."),
        ("How accurate is this snow forecast?", "It is a good guide for the next few days and less certain towards day seven. Snow amounts are estimated from forecast precipitation; actual depth depends on temperature and wind."),
        ("Can you tell me where to go for snow on my dates?", "Yes — WhatsApp us on +91 70874 88961 with your dates and starting city, and we will suggest the snow point that looks best that week."),
    ],
    sources=[
        ("MET Norway Locationforecast (CC BY 4.0) — live forecast data", "https://api.met.no/"),
        ("ANI: Fresh snowfall at Gulmarg's Apharwat Peak — 14 Oct 2026", "https://www.aninews.in/news/national/general-news/j-k-fresh-snowfall-brings-early-winter-at-gulmarg8217s-apharwat-peak-tourists-thrilled20261014191707/"),
        ("Deccan Chronicle: Shimla gets first snowfall of season — 23 Jan 2026", "https://www.deccanchronicle.com/amp/nation/shimla-gets-first-snowfall-of-season-dry-spell-ends-1932163"),
        ("Outlook India: Kashmir sees snowfall as Chillai-Kalan begins — 21 Dec 2025", "https://www.outlookindia.com/national/kashmir-sees-snowfall-and-rain-as-chillai-kalan-winter-period-begins"),
    ],
)
