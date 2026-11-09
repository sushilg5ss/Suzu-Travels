A = "auli-snowfall"
M = "mussoorie-snowfall"
K = "kedarkantha-weather"
D = "dhanaulti-weather"
C = "chopta-weather"
SPEC = dict(
    lang="en",
    slug="uttarakhand-snowfall",
    title="Uttarakhand Snowfall 2026-27: When It Snows and the Best Snow Places",
    seo_title="Uttarakhand Snowfall 2026-27: When & Where It Snows",
    seo_desc="Snowfall in Uttarakhand: this season's first snow, the usual months, a live snow forecast for Auli, Chopta, Dhanaulti and Munsiyari, and the best snowfall places from Mussoorie to Kedarkantha.",
    focus="uttarakhand snowfall, snowfall in uttarakhand, snowfall places in uttarakhand",
    photo_pick=dict(slugs=[A, M, K, D, C], ids=[
        (A + ":hero-1", "hero", "Auli under snow", "Auli's slopes under deep winter snow"),
        (K + ":fig-1", "fig", "Juda ka Talab in winter", "The frozen Juda ka Talab lake on the Kedarkantha trail"),
        (M + ":g-3", "g", "Mussoorie rooftops in snow", "Snow on the rooftops of Mussoorie"),
        (C + ":g-1", "g", "Tungnath in winter", "Snow on the way to Tungnath on a winter morning"),
        (K + ":g-3", "g", "Kedarkantha meadows in snow", "Snow-covered meadows on the Kedarkantha trek"),
        (D + ":g-7", "g", "Snow above Dhanaulti", "Snow on the hills above Dhanaulti"),
        (A + ":g-3", "g", "Snow on the Auli slopes", "Skiers' slopes at Auli covered in snow"),
        (M + ":fig-2", "g", "A Mussoorie church after snowfall", "A church in Mussoorie after a snowfall"),
        (K + ":g-1", "g", "Snow at the base camp", "Tents and snow at the Kedarkantha base camp"),
    ]),
    kicker="Uttarakhand · Auli · Chopta · Mussoorie · Winter 2026-27",
    tag="Snow in Uttarakhand: when it comes, and where to find it",
    sub="The high shrines already have snow. Here is when the hill stations usually turn white, a live 7-day snow forecast for six snow places, and where to go for a sure snow trip.",
    chips=[("Late Dec–Feb", "usual snow window"), ("23 Jan 2026", "last season's first snow in the hill stations"), ("Live", "6 snow places"), ("~2,000–3,800 m", "Mussoorie to Kedarkantha")],
    flakes=True,
    updated="November 2026",
    wa="Hello Suzu Travels, I want to see snow in Uttarakhand. Dates: ___ , people: ___ , starting from: ___",
    cta2=("#weather", "See the snow forecast"),
    answer="<b>In Uttarakhand, snow usually reaches the hill stations between late December and February, with January the most likely month.</b> The high places — Kedarnath, Badrinath, Auli, Chopta–Tungnath, Harsil and Kedarkantha — get snow earlier and more reliably; this season the shrines had their first heavy snow in late October and early November 2026. Mussoorie, Dhanaulti, Chakrata, Mukteshwar and Munsiyari (about 2,000–2,300 m) get snow on some days most winters, but not every year: last season the first snow came only on <b>23 January 2026</b>. For a sure snow trip, go to <b>Auli, Chopta or the Kedarkantha trek</b> between late December and March; for a short trip from Delhi, try <b>Dhanaulti or Mussoorie's Lal Tibba</b> in January.",
    quick=[
        ("Most likely month", "January, then February; late December in a cold year."),
        ("Surest snow", "Auli, Chopta–Tungnath, Kedarkantha, Harsil."),
        ("Nearest to Delhi", "Dhanaulti, Mussoorie's Landour and Lal Tibba, Chakrata."),
        ("Kumaon", "Mukteshwar and Munsiyari; Nainital only on a few days."),
        ("This season", "Kedarnath and Badrinath had heavy snow by early November 2026."),
    ],
    wx=dict(src="/suzu-weather-feed.json", daily=True, kicker="Live snow forecast", h2="Snow forecast for Auli, Chopta, Harsil, Dhanaulti, Munsiyari and Mussoorie",
            lead="Current temperature and the next days' high, low, rain and snow at six of Uttarakhand's snow places, from Auli (about 2,800 m) down to Mussoorie (about 2,005 m). Snow days are marked ❄️.",
            places=[dict(id="auli", name="Auli", alt="2800"), dict(id="chopta", name="Chopta", alt="2680"), dict(id="harsil", name="Harsil", alt="2620"),
                    dict(id="munsiyari", name="Munsiyari", alt="2298"), dict(id="dhanaulti", name="Dhanaulti", alt="2286"), dict(id="mussoorie", name="Mussoorie", alt="2005")]),
    sections=[
        dict(id="when", kicker="When it snows", h2="When does it snow in Uttarakhand?", fig=True, ps=[
            "Winter snow in Uttarakhand comes with <b>western disturbances</b> — weather systems from the west that bring a few days of cloud, rain in the valleys and snow on the heights. Height decides almost everything: above about 2,600 m (Auli, Chopta, Harsil, the Char Dham shrines) snow is regular from December to March; at 2,000–2,300 m (Mussoorie, Dhanaulti, Chakrata, Mukteshwar, Munsiyari) it comes on some days in a normal winter; below about 1,800 m it is rare.",
            "<b>This season</b> started early on the heights: Kedarnath had its first heavy snow at the end of October 2026 and Badrinath had fresh snow on the night of 1–2 November. <b>Last season</b> shows how uncertain the hill stations are: after a long dry spell, the first snow reached Mussoorie, Dhanaulti, Chakrata, Auli and Munsiyari together on <b>23 January 2026</b>.",
            "So plan for a window, not a date — late December to February for the hill stations, December to March for the high places — and check the forecast above a week before you go.",
        ]),
        dict(id="months", kicker="Month by month", h2="Uttarakhand snowfall by month", ps=[
            "A simple guide from the usual pattern and recent winters. Check the forecast for your dates.",
        ], table=(["Month", "High places (Auli, Chopta, Harsil, Kedarkantha)", "Hill stations (Mussoorie, Dhanaulti, Mukteshwar, Munsiyari)", "What to expect"], [
            ["November", "First snow spells; Char Dham closes", "Rare", "Clear, cold days; quiet"],
            ["December", "Snow likely, deepening late in the month", "Possible, mostly late in the month", "Christmas–New Year crowds; book early"],
            ["January", "Deep snow; skiing at Auli", "Most likely month", "Coldest; roads can close after heavy spells"],
            ["February", "Deep snow", "Possible; likely in a cold year", "Fewer crowds; Auli ski season"],
            ["March", "Snow on the ground; melting late", "Uncommon", "Spring begins lower down"],
        ]), after=[
            "Live temperatures for every Uttarakhand hill station: <a href=\"/uttarakhand-weather/\">Uttarakhand weather</a>. Across Himachal, Kashmir and Uttarakhand: <a href=\"/snow-tracker/\">live snow tracker</a>. Month guides: <a href=\"/uttarakhand-in-december/\">Uttarakhand in December</a> · <a href=\"/auli-in-january/\">Auli in January</a> · <a href=\"/mussoorie-in-january/\">Mussoorie in January</a> · <a href=\"/nainital-in-january/\">Nainital in January</a>.",
        ]),
    ],
    gallery=dict(h2="Uttarakhand in the snow", lead="Auli, Mussoorie, Dhanaulti, Tungnath and the Kedarkantha trail — real photographs, each credited to its photographer."),
    spots=dict(kicker="Where to see snow", h2="Best snowfall places in Uttarakhand", lead="From the surest snow to the easiest trip from Delhi.", items=[
        ("Auli", "Chamoli · ~2,500–3,050 m", "Uttarakhand's ski slopes, 16 km by road above Joshimath (the cable car has been closed since January 2023); the surest snow from late December to March. <a href=\"/auli-snowfall/\">Auli snowfall →</a>"),
        ("Chopta–Tungnath", "Rudraprayag · ~2,680 m", "Snowbound meadows and the walk towards Tungnath; the road can close beyond Chopta after heavy snow. <a href=\"/chopta-in-winter/\">Chopta in winter →</a>"),
        ("Kedarkantha trek", "Uttarkashi · ~3,800 m summit", "India's best-known winter snow trek, from Sankri; snow on the trail from December to March. <a href=\"/kedarkantha-weather/\">Kedarkantha weather →</a>"),
        ("Harsil", "Uttarkashi · ~2,620 m", "A quiet apple valley on the Bhagirathi that turns white in January. <a href=\"/harsil-weather/\">Harsil weather →</a>"),
        ("Dhanaulti and Surkanda Devi", "Tehri · ~2,280–2,750 m", "The nearest snow to Delhi with Mussoorie; best in January–February. <a href=\"/dhanaulti-weather/\">Dhanaulti weather →</a>"),
        ("Mussoorie and Landour", "Dehradun · ~2,000–2,270 m", "Snow on some days most winters; Lal Tibba whitens first. <a href=\"/mussoorie-snowfall/\">Mussoorie snowfall →</a>"),
        ("Chakrata", "Dehradun · ~2,118 m", "Deodar ridges above the Yamuna, with snow on the higher points in January. <a href=\"/chakrata-weather/\">Chakrata weather →</a>"),
        ("Mukteshwar and Munsiyari", "Kumaon · ~2,200–2,300 m", "Kumaon's best snow chances, with wide Himalayan views. <a href=\"/mukteshwar-weather/\">Mukteshwar weather →</a>"),
    ]),
    sections2=[
        dict(id="travel", kicker="Plan safely", h2="Travelling in Uttarakhand in snow season", ps=[
            "<b>Roads:</b> after a heavy spell, roads to Auli, Chopta, Harsil, Dhanaulti and Munsiyari can close for hours or days. Travel in daylight with a driver used to hill roads, keep a spare day, and expect chains or a smaller vehicle on the last stretch.",
            "<b>Crowds:</b> the first snow brings big weekend crowds to Mussoorie and Dhanaulti, with long traffic queues from Dehradun. Midweek is calmer.",
            "<b>Clothes:</b> a padded jacket, thermals, gloves, a cap and shoes with grip; for Auli, Chopta and Kedarkantha, proper winter boots and layers for well below freezing.",
            "<b>Shrines:</b> Kedarnath, Badrinath, Gangotri and Yamunotri are closed in winter — see <a href=\"/char-dham-closing-dates-2026/\">Char Dham closing dates 2026</a>.",
        ]),
    ],
    ctas=dict(h2="Our Uttarakhand snow trips", lead="Hotels, meals and a private car in one quote.", items=[
        ("/uttarakhand-winter-packages-travel-agents/", "Uttarakhand in winter", "Snow trips for 2026–27.", "Winter"),
        ("/auli-in-december/", "Auli in December", "Ski slopes, snow odds and what to expect.", "Auli"),
        ("/uttarakhand/", "Uttarakhand tour packages", "Nainital, Corbett, Rishikesh and Mussoorie.", "Uttarakhand"),
        ("/snow-tracker/", "Live snow tracker", "Where snow is in the forecast this week.", "Live"),
    ]),
    quote_h2="Want to see snow in Uttarakhand?",
    quote_text="Tell us your dates, where you are starting from and how many of you are travelling. We watch the forecast, suggest where the snow is likeliest for your dates and send one written quote with hotels, meals and a private car. Suzu Travels is a travel agent registered with HP Tourism, based in Bilaspur, Himachal Pradesh, and plans trips across north India.",
    faq_h2="Uttarakhand snowfall: frequently asked questions",
    faqs=[
        ("When does it snow in Uttarakhand?", "In the hill stations, usually between late December and February, with January the most likely month. The high places — Auli, Chopta, Harsil, Kedarkantha — get snow from December to March."),
        ("Has it snowed in Uttarakhand this season?", "Yes, on the heights: Kedarnath had its first heavy snow at the end of October 2026 and Badrinath had fresh snow on 1–2 November. The hill stations usually get their first snow later, in December or January."),
        ("Which is the best place to see snow in Uttarakhand?", "Auli is the surest, with its ski slopes 16 km by road above Joshimath; Chopta–Tungnath and the Kedarkantha trek are also reliable from late December to March."),
        ("Where can I see snow near Delhi in Uttarakhand?", "Dhanaulti and Mussoorie's Landour and Lal Tibba, about 7–8 hours' drive from Delhi, give the best chance in January–February."),
        ("Does it snow in Nainital?", "Only on a few days in some winters, usually in January; Mukteshwar, about 50 km away, gets snow more often."),
        ("When did it last snow in Mussoorie?", "Last season the first snow reached Mussoorie, Dhanaulti, Chakrata, Auli and Munsiyari on 23 January 2026."),
    ],
    sources=[
        ("DD News: Fresh snowfall blankets Badrinath — 2 Nov 2026", "https://ddindia.co.in/2026/11/fresh-snowfall-blankets-badrinath-temperatures-drop-sharply-in-uttarakhand/"),
        ("The Week (PTI): Uttarakhand sees first snowfall of 2026 — 24 Jan 2026", "https://www.theweek.in/wire-updates/national/2026/01/24/uttarakhand-sees-first-snowfall-of-2026-thick-blanket-of-snow-covers-high-altitude-areas.html"),
        ("MET Norway Locationforecast (CC BY 4.0) — live forecast data", "https://api.met.no/"),
    ],
)
