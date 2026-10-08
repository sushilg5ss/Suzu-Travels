# Pilgrimage section: keyword plan

**Site:** suzutravels.com · **Prepared:** 8 Oct 2026 · **Status:** research only. Nothing was changed on the site or in any ad account.

Companion files in this folder:
- `keywords.csv` has every keyword idea pulled: 4,726 rows (3,726 India-EN · 500 India-Hindi · 500 Worldwide-EN), deduplicated per location, with the seed batch(es), bids and the 12-month trend.
- `site-inventory.md` lists existing URLs, who owns which keyword, and site issues found.
- `tools/build_plan_tables.py` + `tools/keyword_ideas_agg.json` regenerate the page tables below.

---

## 1. How the data was collected

| Item | Detail |
|---|---|
| Source | Google Ads Keyword Planner (`GenerateKeywordIdeas`) via the Pipeboard connector. **The Ads tool worked, so no autocomplete fallback was needed.** |
| Account | Customer `1172710099` (suzutravels@gmail.com, INR). It is the only enabled account on the login. Four other linked IDs returned `CUSTOMER_NOT_ENABLED`. |
| Window | Sep 2025 – Aug 2026 (12-month averages; trends are kept in the CSV) |
| Pulls | 9 English/India batches (generic, jyotirlinga temples, jyotirlinga timings, jyotirlinga how-to-reach, shakti/devi, char dham, amarnath + others, famous temples, Himachal temples), plus a year/gap-fill batch, **1 Hindi-language/India pull** (`languageConstants/1023`) and **1 worldwide English pull** (no geo) for the main seeds |
| Caveats | Each pull returned up to 500 ideas ranked by relevance. Very broad batches had more ideas available (e.g. jyotirlinga temples 3,558, char dham 2,460, worldwide 4,528), so the long tail is sampled, not complete. A few low-volume seeds returned no row at all (e.g. "kashi ayodhya prayagraj tour", "kedarnath kapat closing date"); the nearest variants are used instead. Keyword Planner merges close variants, so several variants show the same number (for example "kashi vishwanath temple" and "kashi temple" both show 673,000). Treat big temple numbers as **cluster** volume. Bids are top-of-page INR. Year-specific terms ("char dham yatra 2026") only appear when seeded directly, and their 12-month average under-states the April–May peak. |

---

## 2. Hub URL slug: recommend **`/pilgrimage-tours/`**

| Candidate slug | Keyword family volume, India-EN (sum of all ideas containing the word) | Best head term (India-EN) | Worldwide-EN | What ranks / intent |
|---|---|---|---|---|
| **/pilgrimage-tours/** | **37,040** (216 ideas) | pilgrimage places in india 1,300 · pilgrimage sites in india 1,300 · pilgrimage to india 1,300 · badrinath pilgrimage 1,600 · pilgrimage tours india 110 | **2,760** (pilgrimage to india 2,400) | Commercial SERP: Veena World `/pilgrimage`, IRCTC pilgrimage packages. Understood by NRI and foreign buyers (the site already sells Char Dham to NRIs). |
| /tirth-yatra/ | 8,220 (44 ideas); Hindi pull 3,750 | tirth yatra 3,600 (+ teerth yatra 880, teertha yatra 880) | 0 | Spelling is split three ways. Roughly 1,300/mo is operator brand names (om shiv shankar / shree tripur / mahesh sharma tirth yatra). The test SERP is religious literature, not packages. Means nothing to NRI/foreign buyers. |
| /spiritual-tours/ | 1,470 | spiritual tours india 210 | 1,630 | Leans toward yoga, retreats and Varanasi experiences, not darshan yatras |
| /devotional-tours/ | 230 | devotional tour packages 70 | 70 | IRCTC owns the term (three IRCTC URLs fill the SERP) |

(The family sums include some off-topic ideas such as hajj, Buddhist and Christian pilgrimage. Even after removing those, "pilgrimage" is the largest English family by a wide margin.)

**Recommendation**
- Slug `/pilgrimage-tours/`. Rank Math focus keyword **`pilgrimage tours india`**. Put **"Tirth Yatra"** in the title and H1 to capture the 3,600 + 880 + 880 Hinglish demand without making it the slug. Example title: *"Pilgrimage Tours in India 2027: Tirth Yatra Packages | Suzu Travels"*.
- Secondaries for the hub: tirth yatra (3,600), pilgrimage places in india (1,300), teerth yatra (880), spiritual tour packages in india (110), religious tour packages (90), devotional tour packages (70), senior citizen tirth yatra (90).
- Nest children under the hub (`/pilgrimage-tours/<circuit>/` and `/pilgrimage-tours/<circuit>/<temple>/`) for a clean topical cluster. All four candidate slugs return 404 today, so the slug is free.

---

## 3. Demand at a glance (India, English, avg monthly searches)

Highest-volume keywords that the new pages will target:

| Keyword | Vol | Page |
|---|---|---|
| kashi vishwanath temple (cluster) | 673,000 | Kashi Vishwanath |
| omkareshwar jyotirlinga (cluster) | 673,000 | Omkareshwar |
| 12 jyotirlinga | 450,000 | 12 Jyotirlinga guide |
| somnath temple | 450,000 | Somnath |
| rameshwaram temple | 246,000 | Rameshwaram |
| kainchi dham | 201,000 | Kainchi Dham |
| hidimba devi temple | 165,000 | Hidimba Devi |
| kedarnath temple | 135,000 | Kedarnath |
| bhimashankar jyotirlinga | 135,000 | Bhimashankar |
| naina devi | 110,000 | Naina Devi |
| char dham yatra | 90,500 (WW 110,000) | Char Dham guide |
| badrinath temple | 90,500 | Badrinath |
| chintpurni | 90,500 | Chintpurni |
| amarnath yatra | 74,000 | Amarnath guide |
| char dham yatra registration | 60,500 | Char Dham guide |
| kedarnath helicopter booking | 49,500 | Kedarnath |
| shakti peeth | 40,500 | 51 Shakti Peeth |
| panch kedar | 40,500 | Panch Kedar |

**Commercial ("package") demand, where bookings come from:** char dham yatra package 33,100 (owned by an existing page) · chardham yatra tour package 8,100 (existing) · kedarnath tour package 5,400 · varanasi tour package 4,400 · 4 dham yatra package 4,400 · 12 jyotirlinga tour package 3,600 (existing) · kailash mansarovar yatra package 3,600 · ayodhya tour package 2,900 · vaishno devi tour package 2,400 · amarnath yatra package 1,600 · badrinath kedarnath tour package 1,600 · adi kailash yatra packages 1,000 · do dham yatra 1,000 · kainchi dham tour package 320 · nau devi / 9 devi yatra package ≤ 20.

**Seasonality (Sep 2025 – Aug 2026 trend):**
- **Amarnath:** "amarnath yatra 2026" ran 590 in Sep → 450,000 in Apr (registration opened 15 Apr) → 27,100 in Aug. "amarnath yatra registration" peaked at 201,000 in Apr. **The 2027 page must be live by Jan 2027.**
- **Char Dham:** "char dham yatra registration" and "kedarnath helicopter booking" both peaked at 201,000 in Apr. "char dham yatra package" sits on a 60,500 plateau from Mar to Jun. **The 2027 guide should be live by Feb 2027.**
- **Manimahesh:** "manimahesh yatra 2026" climbed to 27,100 in Aug. The page should be live by Jun.
- **Kailash Mansarovar:** peaks in Jun (49,500).
- **12 Jyotirlinga / Shakti Peeth:** steady all year. 12 jyotirlinga moves between 301,000 and 550,000, with 550,000 peaks in Jan, Jun and Aug. Shakti peeth holds 40,500–49,500.
- **Himachal Devi temples:** peak in summer holidays and Shravan (Naina Devi 201,000 in Jun, Chintpurni 165,000 in Aug, Jwalamukhi 27,100 in Jun).

**Hindi-language pull:** Devanagari queries are small next to romanised Hindi. 12 ज्योतिर्लिंग 18,100 · 12 ज्योतिर्लिंग के नाम 18,100 · अमरनाथ यात्रा 5,400 · शक्तिपीठ 2,400 · चार धाम यात्रा 1,900 · केदारनाथ यात्रा 1,000 · तीर्थ यात्रा 720 · नौ देवी यात्रा 10. Romanised Hindi is large: "12 jyotirling ke naam" 40,500, "12 jyotirling kaha kaha hai" 12,100. **Recommendation:** use English pages and add the Devanagari name in the H1/alt text plus a "names in Hindi" table and FAQ. Separate Hindi pages are not justified yet.

**Worldwide pull:** almost all volume is India. The worldwide uplift is small but useful for the NRI angle: pilgrimage to india 2,400 vs 1,300 · spiritual tours india 390 vs 210 · kailash mansarovar yatra 27,100 vs 18,100 · char dham yatra 110,000 vs 90,500.

---

## 4. Page plan: hub + 40 child pages

Volumes are India/English averages. `[HI]` means found only in the Hindi pull and `[WW]` only in the worldwide pull. Competition is Google Ads competition (L/M/H), not SEO difficulty. **Rule: a new page never uses another URL's focus keyword** (see `site-inventory.md` §3).

### Hub

| # | Proposed URL | Page | Focus keyword (vol) | Secondary keywords (vol) | Intent | Cannibalisation note |
|---|---|---|---|---|---|---|
| 1 | `/pilgrimage-tours/` | Pilgrimage Tours hub (Tirth Yatra) | **pilgrimage tours india (110)** | tirth yatra (3,600); pilgrimage places in india (1,300); teerth yatra (880); spiritual tour packages in india (110); religious tour packages (90); devotional tour packages (70) | Commercial + navigational hub | New. Links down to every circuit/temple page and across to existing package URLs. |

### Circuits & yatras

| # | Proposed URL | Page | Focus keyword (vol) | Secondary keywords (vol) | Intent | Cannibalisation note |
|---|---|---|---|---|---|---|
| 2 | `/pilgrimage-tours/12-jyotirlinga/` | 12 Jyotirlinga: names, places, map & yatra route | **12 jyotirlinga (450,000)** | 12 jyotirlinga name and place (40,500); 12 jyotirlinga list (33,100); 12 jyotirlinga map (33,100); jyotirlingas (165,000); jyotirlinga yatra (1,600) | Informational | Must NOT target "12 jyotirlinga tour package" (owned by product 10876). Link to it as the booking CTA. |
| 3 | `/pilgrimage-tours/char-dham-yatra/` | Char Dham Yatra 2027 guide | **char dham yatra (90,500)** | char dham yatra registration (60,500); chardham yatra by helicopter (6,600); char dham yatra 2027 (70); char dham yatra itinerary (480); char dham yatra for senior citizens (110) | Mixed (info, high volume) | Head term is unowned today, BUT /char-dham-yatra/ currently 301s to the NRI page; fix that redirect first. Must NOT target "char dham yatra package" (owned by 9905). |
| 4 | `/pilgrimage-tours/kedarnath/` | Kedarnath Yatra & temple guide | **kedarnath yatra (8,100)** | kedarnath temple (135,000); kedarnath helicopter booking (49,500); how to reach kedarnath (3,600); kedarnath opening date 2027 (1,000); haridwar to kedarnath (8,100) | Mixed | Unowned. Leave "kedarnath closing date" (1,600) to post 12021 (closing-dates post) and link to it. Link to do-dham products 9467/9483 and 9905. |
| 5 | `/pilgrimage-tours/badrinath/` | Badrinath Temple guide | **badrinath temple (90,500)** | badrinath mandir (90,500); badrinath opening (590); badrinath pilgrimage (1,600); badrinath by road (1,300); badrinath kedarnath tour package (1,600) | Informational | Unowned. "badrinath kedarnath tour package" should point to product 9467 (retarget it). |
| 6 | `/pilgrimage-tours/amarnath-yatra/` | Amarnath Yatra 2027 guide | **amarnath yatra (74,000)** | amarnath yatra registration (33,100); amarnath yatra 2027 (210); amarnath yatra package (1,600); amarnath yatra by helicopter booking (4,400); amarnath yatra package from delhi (260) | Mixed (seasonal Apr-Aug) | Unowned head. Must NOT target "amarnath yatra by helicopter" (owned by suzu_package 9763). |
| 7 | `/pilgrimage-tours/vaishno-devi-yatra/` | Vaishno Devi Yatra guide | **vaishno devi yatra (9,900)** | vaishno devi tour package (2,400); vaishno devi helicopter booking (33,100); vaishno devi darshan (1,600); vaishno devi yatra package (480); vaishno devi package (720) | Mixed | Unowned. Existing 9367/9215 target "kashmir (with) vaishno devi" only; keep them as combo packages and link to them. |
| 8 | `/pilgrimage-tours/shakti-peeth-himachal/` | Shakti Peeth in Himachal / Nau Devi Yatra | **shakti peeth in himachal pradesh (2,400)** | shakti peeth in himachal (1,600); himachal devi darshan (260); 5 devi darshan in himachal (210); 9 devi yatra (140); nau devi yatra (90) | Mixed | Must NOT target "5 shakti peeth tour package himachal" (owned by product 10861). Treat the product as the booking CTA. |
| 9 | `/pilgrimage-tours/51-shakti-peeth/` | 51 Shakti Peeth list & map | **51 shakti peeth (27,100)** | shakti peeth (40,500); 51 shakti peeth list (27,100); shakti peeth list (12,100); 52 shakti peeth (6,600); 18 shakti peethas list (8,100) | Informational | Unowned. |
| 10 | `/pilgrimage-tours/panch-kedar/` | Panch Kedar Yatra | **panch kedar (40,500)** | tungnath (165,000); tungnath temple (90,500); rudranath trek (14,800); kalpeshwar temple (4,400); madhmaheshwar trek (720) | Informational | Unowned. Tungnath/Rudranath trek intent overlaps adventure section; cross-link. |
| 11 | `/pilgrimage-tours/manimahesh-yatra/` | Manimahesh Kailash Yatra (Chamba) | **manimahesh yatra (2,900)** | manimahesh yatra 2026 (4,400) | Mixed (seasonal Aug-Sep) | Unowned; only a passing mention on /mountains-of-india/ pages. Strong Himachal fit. |
| 12 | `/pilgrimage-tours/shrikhand-mahadev-yatra/` | Shrikhand Mahadev Yatra | **shrikhand mahadev yatra (880)** | (none with data) | Mixed (seasonal July) | Unowned. Low volume (880) but Himachal-local and low competition. |
| 13 | `/pilgrimage-tours/adi-kailash-yatra/` | Adi Kailash & Om Parvat Yatra | **adi kailash yatra (2,900)** | adi kailash (60,500); adi kailash yatra packages (1,000); adi kailash om parvat (1,000); adi kailash permit (480) | Mixed | Unowned. |
| 14 | `/pilgrimage-tours/kailash-mansarovar-yatra/` | Kailash Mansarovar Yatra | **kailash mansarovar yatra (18,100)** | kailash mansarovar (49,500); kailash mansarovar yatra cost (3,600); kailash mansarovar yatra package (3,600); mount kailash mansarovar (1,600) | Mixed | Unowned. /nepal-tour-packages/ mentions it; link from there. |
| 15 | `/pilgrimage-tours/kainchi-dham/` | Kainchi Dham (Neem Karoli Baba) | **kainchi dham (201,000)** | baba neem karoli dham (1,600); best time to visit kainchi dham (590); kainchi dham tour package (320); kainchi dham stay (390) | Informational/navigational | Post 12444 owns "kainchi dham registration" (keep). NOTE /kainchi-dham/ currently 301-guesses to that post; a page at that slug would take it over. |
| 16 | `/pilgrimage-tours/himachal-temples/` | Temples in Himachal Pradesh | **temples in himachal pradesh (5,400)** | himachal temple tour package (30); himachal devi darshan (260); baijnath temple (22,200); jakhu temple (22,200) | Informational | Unowned. Parent of the Himachal temple pages below. |

### 12 Jyotirlinga temple pages (Kedarnath is covered above)

| # | Proposed URL | Page | Focus keyword (vol) | Secondary keywords (vol) | Intent | Cannibalisation note |
|---|---|---|---|---|---|---|
| 17 | `/pilgrimage-tours/12-jyotirlinga/somnath/` | Somnath Temple | **somnath temple (450,000)** | somnath darshan timing (1,900); somnath temple gujarat darshan timings (2,400); how to reach somnath (1,000); somnath temple room booking (1,900) | Informational | Unowned. |
| 18 | `/pilgrimage-tours/12-jyotirlinga/mallikarjuna/` | Mallikarjuna (Srisailam) | **mallikarjuna jyotirlinga (74,000)** | mallikarjuna temple (27,100); how to reach mallikarjuna (170); mallikarjuna darshan timing (50) | Informational | Unowned. |
| 19 | `/pilgrimage-tours/12-jyotirlinga/mahakaleshwar/` | Mahakaleshwar (Ujjain) | **mahakaleshwar temple (90,500)** | mahakaleshwar jyotirlinga (49,500); mahakal aarti time (9,900); mahakaleshwar timing (6,600); mahakaleshwar jyotirlinga tickets (5,400); ujjain mahakal tour package (390) | Informational | Unowned. |
| 20 | `/pilgrimage-tours/12-jyotirlinga/omkareshwar/` | Omkareshwar | **omkareshwar jyotirlinga (673,000)** | omkareshwar temple (201,000); omkareshwar darshan timing (2,900); how to reach omkareshwar (210); mahakaleshwar omkareshwar tour packages (90) | Informational | Unowned. |
| 21 | `/pilgrimage-tours/12-jyotirlinga/bhimashankar/` | Bhimashankar | **bhimashankar jyotirlinga (135,000)** | bhimashankar temple (74,000); how to reach bhimashankar jyotirlinga (480); bhimashankar darshan timing (390) | Informational | Unowned. |
| 22 | `/pilgrimage-tours/12-jyotirlinga/kashi-vishwanath/` | Kashi Vishwanath (Varanasi) | **kashi vishwanath temple (673,000)** | kashi vishwanath darshan timing (2,400); kashi vishwanath temple tour package (210); varanasi tour package (4,400); kashi tour package (3,600) | Informational (+ commercial secondaries) | Post 8623 owns "varanasi spiritual and cultural guide"; product 10584 owns the Varanasi-Ayodhya-Prayagraj combo. This page takes the temple + single-city Varanasi package terms. |
| 23 | `/pilgrimage-tours/12-jyotirlinga/trimbakeshwar/` | Trimbakeshwar (Nashik) | **trimbakeshwar temple (90,500)** | trimbakeshwar temple timings (9,900); trimbakeshwar kaal sarp puja (3,600); how to reach trimbakeshwar (480) | Informational | Unowned. |
| 24 | `/pilgrimage-tours/12-jyotirlinga/baidyanath/` | Baidyanath Dham (Deoghar) | **baidyanath temple (90,500)** | how to reach baidyanath jyotirlinga (1,900); hotels near baidyanath dham (590); baidyanath shakti peeth (320) | Informational | Unowned. Do not confuse with Baijnath (Himachal), which has its own page. |
| 25 | `/pilgrimage-tours/12-jyotirlinga/nageshwar/` | Nageshwar (Dwarka) | **nageshwar jyotirlinga (60,500)** | nageshwar temple (33,100); how to reach nageshwar jyotirlinga (140); dwarkadhish temple (368,000); how to reach nageshwar jyotirlinga from somnath (40) | Informational | Unowned. Can also carry Dwarkadhish secondaries (no Dwarka page planned). |
| 26 | `/pilgrimage-tours/12-jyotirlinga/rameshwaram/` | Rameshwaram (Ramanathaswamy) | **rameshwaram temple (246,000)** | how to reach rameshwaram (1,300); rameshwaram darshan timing (1,000); thila homam rameshwaram (1,300) | Informational | South India temple posts 9786/9780 mention it; link from them. |
| 27 | `/pilgrimage-tours/12-jyotirlinga/grishneshwar/` | Grishneshwar (Ellora) | **grishneshwar temple (49,500)** | how to reach grishneshwar jyotirlinga (260); hotel near grishneshwar jyotirlinga (2,400); 12 jyotirlinga grishneshwar (140) | Informational | Unowned. |

### Himachal Devi (Shakti Peeth / Nau Devi) temple pages

| # | Proposed URL | Page | Focus keyword (vol) | Secondary keywords (vol) | Intent | Cannibalisation note |
|---|---|---|---|---|---|---|
| 28 | `/pilgrimage-tours/himachal-temples/naina-devi/` | Naina Devi (Bilaspur) | **naina devi (110,000)** | naina devi temple bilaspur (260); naina devi hotels (720); naina devi himachal hotels (110) | Informational/navigational | Unowned. |
| 29 | `/pilgrimage-tours/himachal-temples/jwala-ji/` | Jwala Ji / Jwalamukhi Temple | **jwalamukhi temple (18,100)** | jwala ji (9,900); jwala ji temple (2,400); hotel in jawala ji (1,300); jwala devi temple dharamshala (70) | Informational | Unowned. |
| 30 | `/pilgrimage-tours/himachal-temples/chintpurni/` | Chintpurni Mata | **chintpurni temple (8,100)** | chintpurni (90,500); chintpurni mata (33,100); maa chintpurni (5,400); mata chintpurni darshan (70) | Informational/navigational | Unowned. Bare "chintpurni" (90.5k) is mostly navigational/local. |
| 31 | `/pilgrimage-tours/himachal-temples/chamunda-devi/` | Chamunda Devi (Kangra) | **chamunda devi temple (14,800)** | chamunda devi (22,200); chamunda devi himachal (1,900); chamunda devi mandir (5,400); mata chamunda (12,100) | Informational | Unowned. Dharamshala page 1078 is noindex, so no conflict. |
| 32 | `/pilgrimage-tours/himachal-temples/kangra-devi/` | Brajeshwari / Kangra Devi | **kangra devi temple (6,600)** | kangra devi (6,600); kangra temple himachal pradesh (2,400); brajeshwari devi temple kangra (210); hotels near kangra devi temple (210) | Informational | Unowned. |
| 33 | `/pilgrimage-tours/himachal-temples/baglamukhi/` | Baglamukhi Temple (Bankhandi, Kangra) | **baglamukhi mandir himachal (6,600)** | baglamukhi mandir kangra (4,400); baglamukhi mata mandir himachal (3,600); baglamukhi shakti peeth (1,300); baglamukhi himachal pradesh (1,300) | Informational | Unowned. |
| 34 | `/pilgrimage-tours/himachal-temples/mansa-devi/` | Mansa Devi (Panchkula) | **mansa devi temple (22,200)** | mansa devi (90,500); mansa devi mandir (18,100); mansa devi shakti peeth (480); mata mansa devi (1,600) | Informational | Unowned. Note Haridwar Mansa Devi (ropeway queries) is a different temple; disambiguate on page. |

### Other Himachal temple pages

| # | Proposed URL | Page | Focus keyword (vol) | Secondary keywords (vol) | Intent | Cannibalisation note |
|---|---|---|---|---|---|---|
| 35 | `/pilgrimage-tours/himachal-temples/baijnath/` | Baijnath Temple | **baijnath temple (22,200)** | baijnath himachal pradesh (60,500); baijnath dham (18,100); baba baijnath dham (3,600); baijnath jyotirlinga (3,600) | Informational | Unowned. |
| 36 | `/pilgrimage-tours/himachal-temples/hidimba-devi/` | Hidimba Devi Temple (Manali) | **hidimba devi temple (165,000)** | hidimba devi (165,000); hidimba devi mandir manali (165,000); hidimba devi temple history (590) | Informational | Manali pages/posts mention it in itineraries only (no page targets it). |
| 37 | `/pilgrimage-tours/himachal-temples/bhimakali/` | Bhimakali Temple (Sarahan) | **bhimakali temple sarahan (5,400)** | (none with data) | Informational | Kinnaur package pages mention it; link from them. |
| 38 | `/pilgrimage-tours/himachal-temples/baba-balak-nath/` | Baba Balak Nath (Deotsidh) | **baba balak nath temple (12,100)** | baba balak nath (33,100); baba balak nath ji (6,600) | Informational | Unowned. |
| 39 | `/pilgrimage-tours/himachal-temples/jakhu/` | Jakhu Temple (Shimla) | **jakhu temple shimla (22,200)** | jakhu temple (22,200); jakhu mandir shimla (3,600); jakhu temple timings (590); jakhu hill (1,600) | Informational | Shimla pages mention it only in itineraries. |

### Other famous temples

| # | Proposed URL | Page | Focus keyword (vol) | Secondary keywords (vol) | Intent | Cannibalisation note |
|---|---|---|---|---|---|---|
| 40 | `/pilgrimage-tours/ayodhya-ram-mandir/` | Ayodhya Ram Mandir darshan + Ayodhya tour | **ayodhya tour package (2,900)** | ayodhya ram mandir darshan timing (1,300); ayodhya tour (1,000); ayodhya package (590); ayodhya trip plan (390); ayodhya ram mandir tour package (170) | Commercial | Product 10584 owns "varanasi ayodhya prayagraj tour package" (combo). This page owns single-city Ayodhya terms and links to the combo. |
| 41 | `/pilgrimage-tours/golden-temple-amritsar/` | Golden Temple, Amritsar | **golden temple amritsar (74,000)** | amritsar golden temple tour (2,400); hotels in amritsar near golden temple (33,100); amritsar golden temple tour package (30) | Informational | Unowned. Destination "Amritsar" archive (2 products) exists; link to it. |

---

## 5. SERP shape for 6 head terms (Part C, light)

> Method note: these checks used the built-in WebSearch tool, which is **not Google India**. It shows which *kinds* of pages rank, not exact google.co.in positions. Section notes come from opening the top pages. No text was copied.

| Head term | What ranks (types) | What the top pages contain | Implication for our page |
|---|---|---|---|
| **12 jyotirlinga** (450,000) | Wikipedia #1; devotional publishers (themandirstore, bhaktibharat, sanskritimagazine); GK/edu (unacademy); news (punjabkesari); one tour-operator collection (ttrikon) | Name, place and state list/table; map; legend per temple; Hindi names; Dwadasha Jyotirlinga stotram; FAQs | Purely informational. Win with a better **table** (name, form, town, state, nearest airport/railhead, darshan hours, best months), an **interactive map**, a **suggested route order** with day count, Hindi names, and FAQ. Booking CTA goes to the existing 23-day product. |
| **char dham yatra 2026** (2,400; head 90,500) | News (The Statesman, Bhaskar English, explurger), blogs (discoverwithdheeraj), ashram site (Sivananda), pilgrimage OTA (triptotemples). Uttarakhand's official registration portal usually appears for the head term. | **Opening/closing dates table**; registration rules; routes; new-rule explainers; package carousels and videos. The top OTA page has no map, no FAQ and no itinerary. | Date- and rule-driven, so freshness wins. Build a **2027** page with a dates table (refresh when the dates are announced), registration step-by-step, a route map, helicopter options, a live-status box linking our status posts, and FAQ. |
| **nau devi yatra** (90; 9 devi yatra 140) | Wikipedia (Naina Devi); cab operators (trivenicabs `/religious-tours/nau-devi-tour`); package aggregator (tourtravelworld); travel blog (ghumakkar); several spam notes | Trivenicabs: temple cards, day-wise itinerary (cards + table), inclusions, "why us", 8 FAQs, how to reach, "from ₹18,000" price. **No map, no darshan timings**, and the temple list is incomplete. | Very low competition. Add an accurate list of all 9 Devis with a map, timings, km/drive-time table, and a 5D/7D/9D itinerary. Link the 5 Shakti Peeth product. |
| **amarnath yatra** (74,000; 2027 = 210 and rising) | Government news (newsonair.gov.in); national news (Free Press Journal, ETV Bharat); blogs (hindutone); B2B trade (TBO Academy). The official SASB site ranks for registration. | Dates, registration (bank branches, online), compulsory health certificate (CHC), Baltal vs Pahalgam routes, helicopter, quotas. Blog category pages are thin. | Build a **2027** guide: expected dates, registration and documents checklist, a route-comparison table, helicopter section (link product 9763), packing, and FAQ. Have it live by January. |
| **shakti peeth in himachal** (2,400) | Reference/spiritual sites (greenmesg), Wikipedia (Chintpurni), current-affairs edu (iasgyan), pilgrimage directory (daanyam: "What is", map, list by state, 51 with filters, suggested yatras, FAQ), spam | Lists and maps of peethas; legends; little practical travel info | Few commercial competitors. Combine legend + accurate map + route + timings + package link. Strong Himachal-DMC E-E-A-T angle. |
| **devotional tour packages** (70) | IRCTC Tourism dominates (devotional, dharmik and pilgrimage-special pages); SOTC news | Packages grouped by circuit (Bharat Darshan train), shrine (Vaishno Devi, Rameshwaram); FAQ; no prices on the hub | "Devotional" is IRCTC's vocabulary, so it is a poor slug. On our hub, group cards by **circuit → shrine**, with prices and durations, which IRCTC's hub lacks. |

Extra check: "pilgrimage tours india packages" returns Veena World `/pilgrimage` and IRCTC (commercial). "tirth yatra" returns religious-literature and operator pages (non-commercial). This supports §2.

---

## 6. Build order (by demand × fit × timing)

1. **Hub** `/pilgrimage-tours/` + **12 Jyotirlinga guide** + **Shakti Peeth Himachal / Nau Devi** (evergreen; Himachal DMC fit; low competition)
2. **Char Dham Yatra 2027** + **Kedarnath** + **Badrinath** (live by Feb 2027; resolve the `/char-dham-yatra/` redirect first, see site-inventory)
3. **Amarnath Yatra 2027** + **Vaishno Devi** (live by Jan 2027)
4. Himachal temple pages (Naina Devi, Jwala Ji, Chintpurni, Chamunda, Kangra, Baglamukhi, Baijnath, Hidimba, Jakhu, Bhimakali, Baba Balak Nath) and **Manimahesh** (live by Jun 2027)
5. Remaining 11 Jyotirlinga temple pages, Panch Kedar, Adi Kailash, Kailash Mansarovar, Kainchi Dham, Ayodhya, Golden Temple

Each temple page should carry: darshan/aarti timings table, how to reach (air/rail/road with km), best time/season, dress code and rules, nearby temples, map, FAQ (FAQPage schema), and a "Book this as part of" card linking the circuit package. Keep volume-heavy *informational* temple pages honest: they win on practical travel detail, not on legends.
