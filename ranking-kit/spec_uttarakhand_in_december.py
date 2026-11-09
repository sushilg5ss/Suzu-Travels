A = "auli-snowfall"
M = "mussoorie-snowfall"
N = "nainital-weather"
R = "rishikesh-weather"
J = "jim-corbett-weather"
K = "kedarkantha-weather"
SPEC = dict(
    lang="en",
    slug="uttarakhand-in-december",
    title="Uttarakhand in December 2026: Weather, Snow and the Best Places to Visit",
    seo_title="Uttarakhand in December 2026: Weather, Snow & Best Places",
    seo_desc="Places to visit in Uttarakhand in December: weather for each hill station (IMD), where the first snow falls, Auli, Mussoorie, Nainital, Rishikesh, Corbett and the Kedarkantha trek, crowds and road tips.",
    focus="places to visit in uttarakhand in december, uttarakhand in december",
    photo_pick=dict(slugs=[A, M, N, R, J, K], ids=[
        (A + ":hero-1", "hero", "Auli under snow", "Auli's slopes under winter snow"),
        (N + ":fig-1", "fig", "The Himalaya from Nainital", "The snow peaks of the Himalaya seen from Nainital on a clear winter day"),
        (M + ":g-3", "g", "Mussoorie rooftops in snow", "Snow on the rooftops of Mussoorie"),
        (N + ":hero-1", "g", "Nainital around its lake", "Nainital town around Naini lake"),
        (R + ":hero-1", "g", "Rishikesh across the Ganga", "Rishikesh on both banks of the Ganga"),
        (J + ":hero-1", "g", "Morning mist at Dhikala", "Winter morning mist over the grassland at Dhikala in Corbett"),
        (K + ":g-2", "g", "The snow trail to Kedarkantha", "Trekkers on the snow trail to the Kedarkantha summit"),
        (A + ":g-4", "g", "Himalayan peaks from Auli", "Snow peaks seen from Auli"),
        (R + ":g-4", "g", "Evening aarti at Parmarth Niketan", "The evening Ganga aarti at Parmarth Niketan, Rishikesh"),
    ]),
    kicker="Uttarakhand · Auli · Mussoorie · Nainital · December 2026",
    tag="Uttarakhand in December: cold, clear and the start of the snow season",
    sub="What the weather is like in each hill station, where the first snow is likely, the best places to go, and how to plan around the Christmas–New Year rush.",
    chips=[("~13° / 3 °C", "Mussoorie & Nainital (IMD)"), ("~22° / 8 °C", "Rishikesh & Dehradun"), ("Late Dec", "snow more likely"), ("Closed", "Char Dham shrines")],
    flakes=True,
    updated="November 2026",
    wa="Hello Suzu Travels, I am planning Uttarakhand in December. Dates: ___ , people: ___ , starting from: ___",
    cta2=("/uttarakhand-weather/", "Today's weather"),
    answer="<b>December in Uttarakhand is cold, mostly dry and clear.</b> Mussoorie and Nainital average about <b>13 °C by day and 3–4 °C at night</b>, Rishikesh and Dehradun about <b>22 °C and 8 °C</b> (IMD normals). Snow is likely at <b>Auli, Chopta and on the Kedarkantha trek</b>, and possible in Mussoorie, Dhanaulti, Mukteshwar and Nainital, mostly in the second half of the month. The best places to visit are <b>Auli</b> for snow, <b>Mussoorie and Nainital</b> for hill-station winters, <b>Rishikesh</b> for the river, yoga and mild days, <b>Jim Corbett</b> for safaris, and <b>Kedarkantha</b> for a snow trek. The Char Dham shrines are closed. From about Christmas to New Year the hill stations fill up and traffic builds, so book early.",
    quick=[
        ("Weather", "Mussoorie ~12.7° / 4.5 °C, Nainital ~12.8° / 2.9 °C, Rishikesh ~21.7° / 7.6 °C (IMD)."),
        ("Snow", "Likely at Auli, Chopta, Kedarkantha; possible in the hill stations late in the month."),
        ("Best places", "Auli, Mussoorie, Nainital, Rishikesh, Jim Corbett, Kedarkantha trek."),
        ("Crowds", "Quiet till mid-December; busy from about Christmas to New Year."),
        ("Closed", "Kedarnath, Badrinath, Gangotri and Yamunotri."),
    ],
    wx=dict(src="/suzu-weather-feed.json", daily=True, kicker="Live forecast", h2="Uttarakhand weather today: Auli, Mussoorie, Nainital and Rishikesh",
            lead="Current temperature and the next days' high, low, rain and snow at four places you are likely to visit in December.",
            places=[dict(id="auli", name="Auli", alt="2800"), dict(id="mussoorie", name="Mussoorie", alt="2005"), dict(id="nainital", name="Nainital", alt="2084"), dict(id="rishikesh", name="Rishikesh", alt="372")]),
    sections=[
        dict(id="weather", kicker="December weather", h2="What is the weather like in Uttarakhand in December?", ps=[
            "December is one of the driest months of the year in Uttarakhand, with clear skies, cold mornings and, in the hill stations, nights near freezing. Western disturbances bring a few cloudy days, with rain in the valleys and snow on the heights — usually more often in the second half of the month.",
        ], table=(["Place", "Height", "December day / night", "Snow in December?"], [
            ["<a href=\"/rishikesh-weather/\">Rishikesh</a>", "~340 m", "21.7° / 7.6 °C (Dehradun IMD ref.)", "No; cool, foggy mornings"],
            ["<a href=\"/dehradun-weather/\">Dehradun</a>", "~640 m", "21.7° / 7.6 °C (IMD)", "No"],
            ["<a href=\"/jim-corbett-weather/\">Jim Corbett</a>", "~350 m", "22.1° / 7.7 °C (Roorkee IMD ref.)", "No; misty mornings, cold open-jeep safaris"],
            ["<a href=\"/tehri-weather/\">New Tehri</a>", "~1,750 m", "17.1° / 4.5 °C (IMD)", "Rare"],
            ["<a href=\"/joshimath-weather/\">Joshimath</a>", "~1,875 m", "13.4° / 3.9 °C (IMD)", "Occasional, late in the month"],
            ["<a href=\"/mussoorie-weather/\">Mussoorie</a>", "~2,005 m", "12.7° / 4.5 °C (IMD)", "Possible, mostly late in the month"],
            ["<a href=\"/nainital-weather/\">Nainital</a>", "~2,084 m", "12.8° / 2.9 °C (IMD)", "Uncommon"],
            ["<a href=\"/mukteshwar-weather/\">Mukteshwar</a>", "2,171 m", "14.4° / 3.6 °C (IMD)", "Possible"],
            ["<a href=\"/weather/auli/\">Auli</a>", "~2,500–3,050 m", "Below freezing at night", "Likely, deepening late in the month"],
            ["<a href=\"/chopta-weather/\">Chopta</a>", "~2,680 m", "~8° / −1 °C (estimate)", "Likely; first heavy snow"],
        ]), after=[
            "IMD = India Meteorological Department normals; \"ref.\" = a nearby station shown as a reference. Every place: <a href=\"/uttarakhand-weather/\">Uttarakhand weather</a> · snow outlook: <a href=\"/uttarakhand-snowfall/\">Uttarakhand snowfall 2026-27</a>.",
        ]),
        dict(id="snow", kicker="Snow", h2="Will there be snow in Uttarakhand in December?", fig=True, ps=[
            "<b>On the heights, very likely.</b> Kedarnath and Badrinath already had heavy snow in late October and early November 2026, and Auli, Chopta–Tungnath, Harsil and the Kedarkantha trail usually have snow on the ground by mid to late December.",
            "<b>In the hill stations, possible but not certain.</b> Mussoorie, Dhanaulti, Chakrata, Mukteshwar and Nainital get snow in some Decembers, mostly late in the month; in other years the first snow waits until January — last season it came on 23 January 2026. If snow is the main reason for your trip, plan Auli or Chopta, or keep Dhanaulti as a day trip from Mussoorie.",
        ]),
    ],
    gallery=dict(h2="Uttarakhand in winter", lead="Auli, Mussoorie, Nainital, Rishikesh, Corbett and the Kedarkantha trail — real photographs, each credited to its photographer."),
    spots=dict(kicker="Where to go", h2="Best places to visit in Uttarakhand in December", lead="From snow slopes to a mild river town.", items=[
        ("Auli", "Snow and skiing · ~2,500–3,050 m", "The surest snow in Uttarakhand, with the ropeway from Joshimath. <a href=\"/auli-in-december/\">Auli in December →</a>"),
        ("Mussoorie and Landour", "Hill station · ~2,000 m", "Cold, sunny days and Winterline sunsets; snow possible late in the month. <a href=\"/mussoorie-in-december/\">Mussoorie in December →</a>"),
        ("Nainital", "Lake town · ~2,084 m", "Crisp days, clear Himalayan views from Snow View and Tiffin Top. <a href=\"/nainital-in-december/\">Nainital in December →</a>"),
        ("Rishikesh", "River town · ~340 m", "The mildest choice: Ganga aarti, yoga and day-time walks by the river. <a href=\"/rishikesh-in-december/\">Rishikesh in December →</a>"),
        ("Jim Corbett", "Safari · ~350 m", "Winter safaris with the Dhikala zone open; cold, misty mornings. <a href=\"/jim-corbett-weather/\">Jim Corbett weather →</a>"),
        ("Kedarkantha trek", "Snow trek · ~3,800 m summit", "Uttarakhand's classic winter trek from Sankri. <a href=\"/kedarkantha-weather/\">Kedarkantha weather →</a>"),
        ("Chopta–Tungnath", "Meadows · ~2,680 m", "Snow and silence; roads can close after heavy falls. <a href=\"/chopta-in-winter/\">Chopta in winter →</a>"),
        ("Mukteshwar and Kausani", "Kumaon · ~1,900–2,200 m", "Wide Himalayan views in the clearest month. <a href=\"/mukteshwar-weather/\">Mukteshwar weather →</a>"),
    ]),
    sections2=[
        dict(id="plan", kicker="Plan your trip", h2="Uttarakhand in December: crowds, roads and packing", ps=[
            "<b>Crowds:</b> the first half of December is quiet. From about Christmas to New Year, Mussoorie, Nainital, Dhanaulti and Auli fill up, hotels sell out and traffic queues build on the hill roads — book early and travel up on weekdays where you can.",
            "<b>Roads:</b> after a snow spell, roads to Auli, Chopta, Dhanaulti and Munsiyari can close for hours. Travel in daylight with a driver used to hill roads and keep a spare day. On the plains, morning fog can delay trains to Dehradun, Haridwar and Kathgodam late in the month.",
            "<b>Packing:</b> a padded jacket, thermals, gloves and a cap for the hill stations; proper winter boots for Auli, Chopta and Kedarkantha; a warm layer even for Rishikesh evenings.",
            "<b>Shrines:</b> the Char Dham temples are closed for winter — see <a href=\"/char-dham-closing-dates-2026/\">Char Dham closing dates 2026</a>. For Himachal or Kashmir instead: <a href=\"/himachal-in-december/\">Himachal in December</a> · <a href=\"/kashmir-in-december/\">Kashmir in December</a>.",
        ]),
    ],
    ctas=dict(h2="Our Uttarakhand trips", lead="Hotels, meals and a private car in one quote.", items=[
        ("/uttarakhand-winter-packages-travel-agents/", "Uttarakhand in winter", "Snow trips for 2026–27.", "Winter"),
        ("/tours/queen-of-hills-mussoorie/", "Mussoorie tour from Dehradun", "Mussoorie, Kempty and Landour.", "Mussoorie"),
        ("/tours/the-exotic-uttarakhand/", "Nainital, Corbett and Mussoorie", "Two hill stations and a jungle in one trip.", "Uttarakhand"),
        ("/uttarakhand/", "Uttarakhand tour packages", "All our Uttarakhand trips.", "Packages"),
    ]),
    quote_h2="Planning Uttarakhand in December?",
    quote_text="Tell us your dates, where you are starting from and how many of you are travelling. We watch the forecast, suggest where snow is likeliest for your dates and send one written quote with hotels, meals and a private car. Suzu Travels is a travel agent registered with HP Tourism, based in Bilaspur, Himachal Pradesh, and plans trips across north India.",
    faq_h2="Uttarakhand in December: frequently asked questions",
    faqs=[
        ("Is December a good time to visit Uttarakhand?", "Yes — it is dry and clear, with cold hill stations, mild days in Rishikesh, winter safaris in Corbett and snow on the heights. Book early for Christmas–New Year."),
        ("Which places in Uttarakhand get snow in December?", "Auli, Chopta–Tungnath, Harsil and the Kedarkantha trail usually do; Mussoorie, Dhanaulti, Mukteshwar and Nainital sometimes, mostly late in the month."),
        ("How cold is Mussoorie in December?", "About 12.7 °C by day and 4.5 °C at night on average (IMD normals)."),
        ("How cold is Nainital in December?", "About 12.8 °C by day and 2.9 °C at night on average (IMD normals)."),
        ("Is Kedarnath open in December?", "No. Kedarnath closed on 11 November 2026 and Badrinath on 16 November; they reopen in late April or May."),
        ("Is Jim Corbett open in December?", "Yes — December is in the main winter safari season, and the Dhikala zone is open from 15 November."),
    ],
    sources=[
        ("India Meteorological Department — climatological normals", "https://mausam.imd.gov.in/"),
        ("DD News: Fresh snowfall blankets Badrinath — 2 Nov 2026", "https://ddindia.co.in/2026/11/fresh-snowfall-blankets-badrinath-temperatures-drop-sharply-in-uttarakhand/"),
        ("MET Norway Locationforecast (CC BY 4.0) — live forecast data", "https://api.met.no/"),
    ],
)
