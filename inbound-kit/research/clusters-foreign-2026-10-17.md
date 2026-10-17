# Foreign-traveller keyword clusters for suzutravels.com/india-tours/ — 17 Oct 2026

Source: Google Ads Keyword Planner (GenerateKeywordIdeas) via Pipeboard, customer 1172710099, language English (1000), network GOOGLE_SEARCH. Volumes are average monthly searches over Oct 2025–Sep 2026. Bids are top-of-page bids in INR (account currency).

- **Group A** = US + GB + CA + AU combined. **Group B** = DE + FR + NL + IT + ES combined (English-language searches only). **Group C** = SG + AE + NZ + IE, checked for 40 focus keywords only.
- Raw universe: 9 seed sets x 2 markets (6 briefed groups + 3 supplementary seed sets for head terms, retreats/safaris/festivals and Himalayan treks), up to 300 ideas each. After de-duplication and filtering, **1562 keywords** (3020 keyword x market rows) are in `keywords-foreign-2026-10-17.csv`.
- Dropped: hotel/accommodation 323, outbound/other-country 128, domestic 116, irrelevant 77, zero-volume 74, brand 41, old-year 22, flights/transport-ticket 8. "Hotel/accommodation" covers named hotels and "hotels near X". "Outbound" covers other countries, Everest and Nepal-only searches, and searches like "insurance from India to USA". "Domestic" covers searches like "from Mumbai", Hindi/Hinglish, IRCTC, self-drive and rupee prices.
- `intent` column: **commercial** (tour/package/trip/safari/retreat/driver…), **informational** (best time, things to do, visa, guides), **domestic-likely** (kept but not scored. It covers "from Delhi" for hill stations, "trip package", "for couple", "cheap", "kullu manali" and bike trips. "from Delhi" stays foreign intent for Taj, Agra, Golden Triangle and Jaipur).

## How the score works

`score = Σ over the cluster's keywords of (vol A + 0.5 × vol B) × intent weight × fit weight`
- Intent weight: commercial 1.0, informational 0.6, domestic-likely 0.
- Fit weight: 1.0 for North India, Himalaya, Golden Triangle, Rajasthan, Kashmir, Ladakh, Rishikesh/Uttarakhand, Varanasi, Amritsar, tiger safari (Ranthambore/Corbett) and India-wide practical guides. 0.7 for Kerala, Goa, Andaman, South India, Northeast, Darjeeling/Sikkim, Mumbai, luxury trains and Hornbill (arranged through partners).
- **Close-variant de-dupe:** Keyword Planner gives grouped variants the same numbers. For example, "india tour packages" and "india holiday packages" are both 2,900 with an identical 12-month curve. Keywords with the same 12-month vector and bids are counted once.
- **Bare place names are not scored**, for example "kashmir" (110k), "jaipur" (74k), "varanasi" (60k), "darjeeling" and "shimla". They are mostly news, weather and general curiosity. They are listed under each cluster as *head terms* to show the size of the topic. The cluster score uses only modifier keywords such as tour, trip, things to do or best time.
- **Spike guard:** if one or two months are more than 5x a keyword's median month, the keyword is scored on its non-spike baseline. These keywords are marked `*` and show the raw figure. For example, "agra tour" averages 12,100 only because of 74k/60k in Mar–Apr 2026. Its baseline is about 200. The CSV keeps raw averages and adds a `spike_baseline` column.
- **Head-term grouping guard:** some keywords have exactly the same numbers as a bare place name, because Keyword Planner grouped them together. These are not scored: "chadar trek" = "chadar" (1,600). For example, "chadar trek" = "chadar", and "chadar" is also the Hindi word for bedsheet, so its true trek demand is far lower.
- Peak months are the top 3 months of the cluster's combined A+B monthly volume. **Nov–Mar** = peak month in Nov–Mar or ≥2 of the top 3 months in Nov–Mar.

## Top clusters, ranked

| # | Cluster | Slug | Type | Focus keyword | Focus vol A | Focus vol B | Focus vol C | Cluster vol A | Cluster vol B | Peak months | Nov–Mar | Score |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | India e-Visa guide for tourists | `/india-tours/india-e-visa-guide/` | practical | e tourist visa india | 49500 | 18100 | - | 129,770 | 35,410 | Dec, Nov, Oct | **yes** | 88,549 |
| 2 | India tour packages — hub (EXISTING /india-tours/) | `/india-tours/` | product | india tours | 4400 | 880 | 480 | 15,520 | 1,890 | Oct, Jan, Mar | **yes** | 16,465 |
| 3 | Holi festival tour (Mathura–Vrindavan–Jaipur) | `/india-tours/holi-festival-tour/` | product | holi festival india | 18100 | 2900 | 1000 | 22,510 | 4,810 | Mar, Sep, Feb | **yes** | 14,955 |
| 4 | Taj Mahal day trip / sunrise tour from Delhi | `/india-tours/taj-mahal-tour-from-delhi/` | product | taj mahal tours | 9900 | 30 | - | 16,180 | 1,020 | Nov, Dec, Oct | **yes** | 14,872 |
| 5 | Best places to visit in India | `/india-tours/best-places-to-visit-in-india/` | guide | places to visit in india | 9900 | 590 | 880 | 19,190 | 1,200 | Jan, Nov, Mar | **yes** | 12,004 |
| 6 | Rishikesh yoga, meditation & Ganga | `/india-tours/rishikesh-yoga-retreat/` | product | yoga retreat india | 1600 | 390 | 140 | 11,200 | 3,990 | Jan, Oct, Feb | **yes** | 11,388 |
| 7 | Kerala tour (backwaters, Munnar, houseboat) | `/india-tours/kerala-tour/` | itinerary | kerala tour packages | 1900 | 170 | 880 | 20,770 | 3,600 | Jan, Oct, Nov | **yes** | 11,178 |
| 8 | Golden Triangle tour (EXISTING /golden-triangle-tour/) | `/golden-triangle-tour/` | itinerary | golden triangle india | 5400 | 590 | - | 11,660 | 1,120 | Jan, Oct, Nov | **yes** | 9,538 |
| 9 | Goa beach holiday | `/india-tours/goa-holiday/` | product | goa holiday | 6600 | 170 | 90 | 15,190 | 1,610 | Jan, Oct, Feb | **yes** | 8,996 |
| 10 | Char Dham Yatra (EXISTING /char-dham-yatra-for-nri/) | `/char-dham-yatra-for-nri/` | product | char dham yatra package | 1600 | 50 | 260 | 11,270 | 1,080 | May, Apr, Jun |  | 8,212 |
| 11 | Tiger safari India (Ranthambore, Corbett, Bandhavgarh) | `/india-tours/tiger-safari-india/` | product | tiger safari india | 1600 | 110 | 90 | 7,180 | 1,140 | Jan, Dec, Oct | **yes** | 7,690 |
| 12 | India train travel & luxury trains | `/india-tours/luxury-trains-india/` | guide | maharaja express india | 5400 | 1300 | - | 9,800 | 1,850 | Jan, Oct, Nov | **yes** | 7,374 |
| 13 | Rajasthan tour (Jaipur–Jodhpur–Udaipur) | `/india-tours/rajasthan-tour/` | itinerary | rajasthan tour packages | 720 | 70 | - | 6,380 | 1,510 | Nov, Jan, Dec | **yes** | 5,782 |
| 14 | India travel insurance (guide) | `/india-tours/india-travel-insurance/` | practical | trip insurance india | 2900 | 260 | - | 4,760 | 810 | Oct, Mar, Dec | **yes** | 4,292 |
| 15 | Kumbh Mela 2027 (Haridwar / Nashik) | `/india-tours/kumbh-mela-tour/` | product | kumbh mela | 5400 | 2900 | 880 | 5,510 | 2,990 | Jan, Apr, Feb | **yes** | 4,203 |
| 16 | Best time to visit India (month-by-month) | `/india-tours/best-time-to-visit-india/` | guide | best time to go to india | 5400 | 260 | - | 6,280 | 280 | Jan, Oct, Nov | **yes** | 3,852 |
| 17 | Gulmarg ski holiday | `/india-tours/gulmarg-ski-holiday/` | product | gulmarg skiing | 2900 | 720 | 260 | 2,940 | 760 | Feb, Jan, Dec | **yes** | 3,290 |
| 18 | Diwali in India tour | `/india-tours/diwali-in-india-tour/` | product | diwali in india | 4690 | 1060 | - | 4,690 | 1,060 | Oct, Sep, Dec |  | 3,132 |
| 19 | Himachal tour (Shimla–Manali) | `/india-tours/himachal-tour/` | itinerary | manali tour package | 320 | 50 | - | 4,530 | 1,250 | Jan, Dec, Nov | **yes** | 2,996 |
| 20 | India travel tips & first-time guide | `/india-tours/india-travel-tips-first-time/` | guide | india travel | 1900 | 210 | - | 4,530 | 570 | Jan, Mar, Oct | **yes** | 2,927 |
| 21 | Delhi tour (Old & New Delhi) | `/india-tours/delhi-tour/` | product | delhi tour | 320 | 30 | - | 3,120 | 520 | Jan, Oct, Nov | **yes** | 2,686 |
| 22 | Dharamshala & McLeod Ganj (Tibetan culture, Triund) | `/india-tours/dharamshala-mcleodganj/` | itinerary | triund trek | 1300 | 260 | 320 | 2,060 | 500 | May, Oct, Nov |  | 2,241 |
| 23 | Ayurveda retreat Kerala | `/india-tours/ayurveda-retreat-kerala/` | product | ayurveda retreat kerala | 720 | 210 | 140 | 2,790 | 1,040 | Jan, Nov, Oct | **yes** | 2,223 |
| 24 | Andaman Islands | `/india-tours/andaman-islands/` | product | andaman tour packages | 720 | 140 | 390 | 4,260 | 890 | Jan, Nov, Oct | **yes** | 2,187 |
| 25 | Ladakh tour (Leh–Nubra–Pangong) | `/india-tours/ladakh-tour/` | itinerary | ladakh trip | 390 | 40 | - | 2,270 | 500 | May, Apr, Aug |  | 2,145 |
| 26 | Himachal treks (Hampta Pass, Kheerganga, Kasol/Parvati) | `/india-tours/himachal-treks/` | itinerary | hampta pass trek | 720 | 140 | 260 | 1,890 | 560 | May, Jun, Aug |  | 2,108 |
| 27 | Kashmir tour (Srinagar houseboat–Gulmarg–Pahalgam) | `/india-tours/kashmir-tour/` | itinerary | kashmir tour package | 260 | 40 | 260 | 2,350 | 730 | Jan, May, Apr | **yes** | 1,916 |
| 28 | South India tour (Tamil Nadu temples, Hampi, Mysore) | `/india-tours/south-india-tour/` | itinerary | south india tour | 720 | 40 | 70 | 2,380 | 300 | Jan, Mar, Oct | **yes** | 1,669 |
| 29 | Mumbai tour | `/india-tours/mumbai-tour/` | product | mumbai tour | 390 | 210 | - | 2,190 | 590 | Jan, Nov, Oct | **yes** | 1,658 |
| 30 | Is India safe for tourists (incl. solo female) | `/india-tours/is-india-safe-for-tourists/` | guide | is india safe for tourists | 2400 | 90 | 170 | 2,400 | 90 | Mar, Jan, Sep | **yes** | 1,467 |
| 31 | Varanasi tour (Ganga aarti, Sarnath) | `/india-tours/varanasi-tour/` | itinerary | varanasi trip | 260 | 20 | - | 1,760 | 220 | Nov, Jan, Dec | **yes** | 1,446 |
| 32 | Luxury India tours | `/india-tours/luxury-india-tour/` | product | luxury india tour | 1000 | 50 | 40 | 1,210 | 60 | Sep, Jun, Jul |  | 1,240 |
| 33 | Himalayan motorcycle tour (Ladakh/Spiti on Royal Enfield) | `/india-tours/himalayan-motorcycle-tour/` | product | himalayan motorcycle tour | 880 | 50 | 50 | 1,700 | 290 | Mar, May, Apr | **yes** | 1,225 |
| 34 | North India tour | `/india-tours/north-india-tour/` | itinerary | himalayas tour | 390 | 210 | - | 970 | 240 | Dec, Mar, Jan | **yes** | 1,090 |
| 35 | Jaisalmer desert safari & camp | `/india-tours/jaisalmer-desert-safari/` | product | jaisalmer desert camp | 320 | 70 | - | 970 | 220 | Nov, Dec, Oct | **yes** | 1,080 |
| 36 | Uttarakhand treks (Valley of Flowers, Roopkund, Kedarkantha) | `/india-tours/uttarakhand-himalaya-treks/` | itinerary | valley of flowers trek | 480 | 70 | - | 970 | 220 | Aug, May, Jul |  | 1,010 |
| 37 | Ladakh treks (Markha, Stok Kangri) | `/india-tours/ladakh-trekking/` | itinerary | markha valley trek | 590 | 320 | - | 630 | 340 | May, Aug, Jun |  | 800 |
| 38 | Darjeeling & Sikkim | `/india-tours/darjeeling-sikkim-tour/` | itinerary | darjeeling tour | 140 | 480 | 30 | 860 | 730 | Jan, Dec, Jun | **yes** | 798 |
| 39 | Pushkar Camel Fair tour | `/india-tours/pushkar-camel-fair/` | product | pushkar camel fair | 1000 | 320 | 140 | 1,000 | 320 | Oct, Nov, Jan | **yes** | 696 |
| 40 | Spiti Valley tour | `/india-tours/spiti-valley-tour/` | itinerary | spiti valley tour | 110 | 20 | 40 | 680 | 290 | May, Jun, Jan |  | 684 |
| 41 | India itineraries (10 days / 2 weeks / 3 weeks) | `/india-tours/india-itinerary-2-weeks/` | itinerary | india itinerary | 390 | 50 | - | 930 | 130 | Jan, Oct, Dec | **yes** | 597 |
| 42 | What to wear in India | `/india-tours/what-to-wear-in-india/` | practical | what to wear in india | 590 | 30 | 30 | 800 | 40 | Jan, Feb, Nov | **yes** | 492 |
| 43 | Hornbill Festival Nagaland | `/india-tours/hornbill-festival-tour/` | product | hornbill festival | 880 | 320 | - | 880 | 320 | Dec, Nov, Oct | **yes** | 437 |
| 44 | India SIM / eSIM for tourists | `/india-tours/india-sim-card-for-tourists/` | practical | india sim card tourist | 260 | 50 | - | 540 | 130 | Jan, Nov, Oct | **yes** | 363 |
| 45 | Meghalaya & Northeast India | `/india-tours/northeast-india-tour/` | itinerary | north east india tour packages | 170 | 20 | - | 400 | 50 | Apr, May, Jan |  | 298 |
| 46 | Private car & driver in India (EXISTING) | `/india-tours/private-driver-india/` | product | private driver india | 110 | 50 | 10 | 210 | 90 | Jan, Oct, Feb | **yes** | 255 |
| 47 | Delhi airport transfer | `/india-tours/delhi-airport-transfer/` | product | delhi airport transfer | 110 | 20 | - | 240 | 60 | Jan, Dec, Nov | **yes** | 246 |
| 48 | India tour cost & prices (USD) | `/india-tours/india-tour-cost/` | guide | cheap holidays to india | 170 | 10 | - | 390 | 40 | Oct, Jan, Feb | **yes** | 235 |
| 49 | Buddhist circuit (Bodh Gaya–Sarnath–Kushinagar) | `/india-tours/buddhist-circuit-tour/` | itinerary | bodhgaya temple | 260 | 70 | - | 270 | 80 | Nov, Jan, Dec | **yes** | 186 |
| 50 | India family tour | `/india-tours/india-family-tour/` | product | india family tour packages | 70 | 10 | - | 150 | 40 | Oct, Dec, Jan | **yes** | 170 |
| 51 | India & Nepal combined tour | `/india-tours/india-nepal-tour/` | itinerary | india and nepal tour | 110 | 10 | - | 110 | 10 | Jan, Oct, Nov | **yes** | 115 |
| 52 | Chadar frozen-river trek (Zanskar) | `/india-tours/chadar-trek/` | itinerary | chadar lake trek | 10 | 10 | - | 60 | 40 | Sep, Oct, May |  | 76 |
| 53 | Amritsar & Golden Temple | `/india-tours/amritsar-golden-temple-tour/` | itinerary | golden temple amritsar tour | 40 | 10 | 10 | 40 | 10 | Apr, May, Mar |  | 45 |

## Build first: clusters that peak Nov–Mar

These clusters score at least 300 and peak in Nov–Mar, listed by score. Pages should go live 4–8 weeks before the peak. Foreign travellers research 2–6 months ahead, so the Oct–Jan research window is now.

1. India e-Visa guide for tourists: `/india-tours/india-e-visa-guide/` (score 88,549, peaks Dec, Nov, Oct)
2. India tour packages — hub (EXISTING /india-tours/): `/india-tours/` (score 16,465, peaks Oct, Jan, Mar)
3. Holi festival tour (Mathura–Vrindavan–Jaipur): `/india-tours/holi-festival-tour/` (score 14,955, peaks Mar, Sep, Feb)
4. Taj Mahal day trip / sunrise tour from Delhi: `/india-tours/taj-mahal-tour-from-delhi/` (score 14,872, peaks Nov, Dec, Oct)
5. Best places to visit in India: `/india-tours/best-places-to-visit-in-india/` (score 12,004, peaks Jan, Nov, Mar)
6. Rishikesh yoga, meditation & Ganga: `/india-tours/rishikesh-yoga-retreat/` (score 11,388, peaks Jan, Oct, Feb)
7. Kerala tour (backwaters, Munnar, houseboat): `/india-tours/kerala-tour/` (score 11,178, peaks Jan, Oct, Nov)
8. Golden Triangle tour (EXISTING /golden-triangle-tour/): `/golden-triangle-tour/` (score 9,538, peaks Jan, Oct, Nov)
9. Goa beach holiday: `/india-tours/goa-holiday/` (score 8,996, peaks Jan, Oct, Feb)
10. Tiger safari India (Ranthambore, Corbett, Bandhavgarh): `/india-tours/tiger-safari-india/` (score 7,690, peaks Jan, Dec, Oct)
11. India train travel & luxury trains: `/india-tours/luxury-trains-india/` (score 7,374, peaks Jan, Oct, Nov)
12. Rajasthan tour (Jaipur–Jodhpur–Udaipur): `/india-tours/rajasthan-tour/` (score 5,782, peaks Nov, Jan, Dec)
13. India travel insurance (guide): `/india-tours/india-travel-insurance/` (score 4,292, peaks Oct, Mar, Dec)
14. Kumbh Mela 2027 (Haridwar / Nashik): `/india-tours/kumbh-mela-tour/` (score 4,203, peaks Jan, Apr, Feb)
15. Best time to visit India (month-by-month): `/india-tours/best-time-to-visit-india/` (score 3,852, peaks Jan, Oct, Nov)
16. Gulmarg ski holiday: `/india-tours/gulmarg-ski-holiday/` (score 3,290, peaks Feb, Jan, Dec)
17. Himachal tour (Shimla–Manali): `/india-tours/himachal-tour/` (score 2,996, peaks Jan, Dec, Nov)
18. India travel tips & first-time guide: `/india-tours/india-travel-tips-first-time/` (score 2,927, peaks Jan, Mar, Oct)
19. Delhi tour (Old & New Delhi): `/india-tours/delhi-tour/` (score 2,686, peaks Jan, Oct, Nov)
20. Ayurveda retreat Kerala: `/india-tours/ayurveda-retreat-kerala/` (score 2,223, peaks Jan, Nov, Oct)
21. Andaman Islands: `/india-tours/andaman-islands/` (score 2,187, peaks Jan, Nov, Oct)
22. Kashmir tour (Srinagar houseboat–Gulmarg–Pahalgam): `/india-tours/kashmir-tour/` (score 1,916, peaks Jan, May, Apr)
23. South India tour (Tamil Nadu temples, Hampi, Mysore): `/india-tours/south-india-tour/` (score 1,669, peaks Jan, Mar, Oct)
24. Mumbai tour: `/india-tours/mumbai-tour/` (score 1,658, peaks Jan, Nov, Oct)
25. Is India safe for tourists (incl. solo female): `/india-tours/is-india-safe-for-tourists/` (score 1,467, peaks Mar, Jan, Sep)
26. Varanasi tour (Ganga aarti, Sarnath): `/india-tours/varanasi-tour/` (score 1,446, peaks Nov, Jan, Dec)
27. Himalayan motorcycle tour (Ladakh/Spiti on Royal Enfield): `/india-tours/himalayan-motorcycle-tour/` (score 1,225, peaks Mar, May, Apr)
28. North India tour: `/india-tours/north-india-tour/` (score 1,090, peaks Dec, Mar, Jan)
29. Jaisalmer desert safari & camp: `/india-tours/jaisalmer-desert-safari/` (score 1,080, peaks Nov, Dec, Oct)
30. Darjeeling & Sikkim: `/india-tours/darjeeling-sikkim-tour/` (score 798, peaks Jan, Dec, Jun)
31. Pushkar Camel Fair tour: `/india-tours/pushkar-camel-fair/` (score 696, peaks Oct, Nov, Jan)
32. India itineraries (10 days / 2 weeks / 3 weeks): `/india-tours/india-itinerary-2-weeks/` (score 597, peaks Jan, Oct, Dec)
33. What to wear in India: `/india-tours/what-to-wear-in-india/` (score 492, peaks Jan, Feb, Nov)
34. Hornbill Festival Nagaland: `/india-tours/hornbill-festival-tour/` (score 437, peaks Dec, Nov, Oct)
35. India SIM / eSIM for tourists: `/india-tours/india-sim-card-for-tourists/` (score 363, peaks Jan, Nov, Oct)

## Notes for the page-building agents

- **e-Visa is the biggest foreign-intent cluster by far** (A ~130k/mo). It is informational, and it competes with the official indianvisaonline.gov.in portal and visa agencies. Build an independent, trust-first guide: steps, fees in USD, 30-day/1-year/5-year options, port-of-entry list and a "plan your trip with us" CTA. Never imply Suzu is the government or a visa agent.
- **Holi (Mar) and Diwali (Oct/Nov)** are mostly searches for festival dates and meaning. Real "tour" volume is tiny (holi festival india tour = 10). Build the pages as guide + bookable festival tour. Holi 2027 is around 22 Mar 2027 (Mathura/Vrindavan/Barsana Lathmar Holi), so the page is needed by Dec–Jan. Diwali 2026 falls on 8 Nov 2026, which is too late for this year, so build for Diwali 2027.
- **Kumbh:** volume is steady at 5.4k/mo in group A. Haridwar Ardh Kumbh is due in 2027 (Uttarakhand, so fit = 1.0). Nashik Simhastha starts mid-2027. "kumbh mela 2027" is still small (110/mo) but will grow.
- **Taj Mahal:** "agra tour" (12,100 avg) is a Mar–Apr 2026 spike, and its baseline is about 200. "taj mahal tours" A 9,900 vs B 30 suggests Keyword Planner grouped it with ticket/close variants, so treat it as an upper bound. The dependable foreign day-trip keywords are "taj mahal tour from delhi" (480) and "delhi to agra" (1,900). Link this page both ways with /golden-triangle-tour/.
- **Golden Triangle (existing page):** the umbrella phrase "golden triangle india" (5.4k, steady) beats "golden triangle tour" (1.6k raw, Dec spike). Make sure the existing page targets both, plus "golden triangle tours from delhi" (1k).
- **Rishikesh cluster** covers generic "yoga retreat india" (1.6k) and "rishikesh yoga teacher training" (590). Goa and Kerala yoga searches are routed to their own clusters. Group B (EU) is relatively strong here: "rishikesh yoga" has B 720 > A 590.
- **Kashmir, Ladakh and Himachal:** huge bare-name demand ("kashmir" 110k, "ladakh" 33k, "shimla" 27k, "manali" 18k) but small foreign "tour" volume. Much of the remaining package volume is domestic-likely (diaspora or Indian VPN), for example "kullu manali tour package" and "kashmir trip package". Pages should still be built because Suzu operates there (fit 1.0), but expect long-tail traffic. Ladakh, Spiti, Himachal treks and Dharamshala/Triund peak Apr–Aug, so they can wait until Feb–Mar.
- **Gulmarg skiing** (2.9k A / 720 B / 260 C, peaks Dec–Feb, low competition) is the strongest Himalaya-winter product cluster. Build it now.
- **Chadar trek:** the 1,600/mo figure is the same as the bare word "chadar" (Hindi for bedsheet), so it is not real demand. True trek searches are tiny. Low priority despite the Jan–Feb season.
- **Amritsar:** 27k bare-name and 8k "golden temple amritsar" head demand, but almost every modifier search is a hotel or room. Best handled as a section or add-on in the Golden Triangle / North India pages, not a standalone page.
- **Luxury trains** ("maharaja express india" 5.4k): Suzu can only resell these through partners, hence fit 0.7. Good for a guide page with a "train + private tour" CTA.
- **Existing pages:** /india-tours/ (hub, rank 2), /golden-triangle-tour/ (rank 8), /char-dham-yatra-for-nri/ (rank 10, peaks Apr–Jun, so refresh in Jan–Feb) and /india-tours/private-driver-india/ (small: "private driver india" 110). Keep their URLs and refresh the on-page keywords from the supporting lists below.
- Group C (SG/AE/NZ/IE) volumes are in the table for the 40 focus keywords checked. UAE/Singapore volume is largely Indian expats ("kerala tour packages" C 880, "india e visa" C 4.4k, "char dham yatra package" C 260).

## Cluster detail

### 1. India e-Visa guide for tourists
- **URL:** `/india-tours/india-e-visa-guide/`  |  **Page type:** practical  |  **Fit weight:** 1.0  |  **Score:** 88,549
- **Focus keyword:** `e tourist visa india`: A 49,500 / B 18,100 · competition Low (0) · top-of-page bid ₹142–530 · intent informational
- **Cluster totals (deduped, scored keywords):** A 129,770 / B 35,410 · 29 keywords in CSV · median competition index (A) 0
- **Seasonality:** peaks Dec, Nov, Oct (peak month = 1.65x the monthly average) · **Nov–Mar build-first**
- **Supporting keywords (vol A / vol B, intent):**
  - indian visa online: 33,100 / 8,100, informational
  - india e visa: 27,100 / 2,900, informational _(same data as: electronic travel authorization india)_
  - indian e visa online: 5,400 / 880, informational
  - indian visa online visa: 1,600 / 2,900, informational
  - india e visa application: 2,400 / 140, informational
  - apply for evisa india: 1,900 / 90, informational
  - indian visa online application: 1,600 / 110, informational
  - apply indian visa online: 1,600 / 70, informational
  - indian visa online gov in: 880 / 480, informational
  - apply for indian evisa: 880 / 20, informational
  - indian visa online gov: 480 / 590, informational
  - e visa india official website: 590 / 210, informational
  - government of india e visa: 480 / 320, informational
  - e business visa india: 480 / 140, informational
  - apply india e visa: 390 / 10, informational

### 2. India tour packages — hub (EXISTING /india-tours/)
- **URL:** `/india-tours/`  |  **Page type:** product  |  **Fit weight:** 1.0  |  **Score:** 16,465
- **Focus keyword:** `india tours`: A 4,400 / B 880 / C 480 · competition Medium (65) · top-of-page bid ₹134–607 · intent commercial
- **Cluster totals (deduped, scored keywords):** A 15,520 / B 1,890 · 42 keywords in CSV · median competition index (A) 58
- **Seasonality:** peaks Oct, Jan, Mar (peak month = 1.25x the monthly average) · **Nov–Mar build-first**
- **Supporting keywords (vol A / vol B, intent):**
  - india tour packages: 2,900 / 210, commercial _(same data as: india travel packages, india holiday packages)_
  - trip to india: 1,300 / 70, commercial
  - india travel agency: 720 / 70, commercial
  - india vacation: 720 / 50, commercial
  - india group tours: 480 / 30, commercial
  - india tour operator: 390 / 210, commercial
  - guided tours india: 390 / 10, commercial _(same data as: india guided tours)_
  - india tours and travels: 320 / 40, commercial
  - my trip to india: 320 / 30, commercial
  - private tour of india: 320 / 20, commercial
  - best india tours: 320 / 10, commercial
  - best tour operators in india: 320 / 10, commercial _(same data as: best tour companies for india)_
  - best travel agency in india: 260 / 20, commercial
  - india travel tours: 260 / 20, commercial
  - escorted tours india: 260 / 10, commercial

### 3. Holi festival tour (Mathura–Vrindavan–Jaipur)
- **URL:** `/india-tours/holi-festival-tour/`  |  **Page type:** product  |  **Fit weight:** 1.0  |  **Score:** 14,955
- **Focus keyword:** `holi festival india`: A 18,100 / B 2,900 / C 1,000 · competition Low (1) · top-of-page bid ₹169–784 · intent informational
- **Cluster totals (deduped, scored keywords):** A 22,510 / B 4,810 · 5 keywords in CSV · median competition index (A) 4
- **Seasonality:** peaks Mar, Sep, Feb (peak month = 3.22x the monthly average) · **Nov–Mar build-first**
- **Supporting keywords (vol A / vol B, intent):**
  - holi indian: 4,400 / 1,900, informational
  - holi festival india tour: 10 / 10, commercial

### 4. Taj Mahal day trip / sunrise tour from Delhi
- **URL:** `/india-tours/taj-mahal-tour-from-delhi/`  |  **Page type:** product  |  **Fit weight:** 1.0  |  **Score:** 14,872
- **Focus keyword:** `taj mahal tours`: A 9,900 / B 30 · competition Low (12) · top-of-page bid ₹117–430 · intent commercial
- **Cluster totals (deduped, scored keywords):** A 16,180 / B 1,020 · 46 keywords in CSV · median competition index (A) 66
- **Seasonality:** peaks Nov, Dec, Oct (peak month = 1.73x the monthly average) · **Nov–Mar build-first**
- **Supporting keywords (vol A / vol B, intent):**
  - delhi to agra: 1,900 / 260, informational
  - delhi to taj mahal: 880 / 210, informational
  - agra to jaipur: 720 / 70, informational
  - taj mahal tour from delhi: 480 / 50, commercial _(same data as: taj mahal trip from delhi, taj mahal from delhi day trip)_
  - visit taj mahal: 440* (raw 880) / 70, informational
  - delhi to agra by car: 260 / 10, informational
  - taj mahal tour packages: 260 / 10, commercial
  - agra tour: 180* (raw 12,100) / 20, commercial
  - delhi agra tour: 170 / 20, commercial _(same data as: agra tour from delhi, agra trip from delhi)_
  - taj mahal day tour from delhi: 170 / 20, commercial _(same data as: taj mahal one day tour from delhi, taj mahal day trip from delhi, new delhi to taj mahal day trip)_
  - delhi to agra day trip: 140 / 10, commercial _(same data as: agra day trip from delhi)_
  - taj mahal sunrise tour: 140 / 10, commercial
  - day trip to taj mahal from delhi: 90 / 20, commercial _(same data as: one day trip to taj mahal from delhi)_
  - day trip from delhi to taj mahal: 70 / 10, commercial
  - delhi agra and jaipur tour package: 50 / 10, commercial

### 5. Best places to visit in India
- **URL:** `/india-tours/best-places-to-visit-in-india/`  |  **Page type:** guide  |  **Fit weight:** 1.0  |  **Score:** 12,004
- **Focus keyword:** `places to visit in india`: A 9,900 / B 590 / C 880 · competition Medium (33) · top-of-page bid ₹22–137 · intent informational
- **Cluster totals (deduped, scored keywords):** A 19,190 / B 1,200 · 5 keywords in CSV · median competition index (A) 50
- **Seasonality:** peaks Jan, Nov, Mar (peak month = 1.29x the monthly average) · **Nov–Mar build-first**
- **Supporting keywords (vol A / vol B, intent):**
  - tourist places in india: 4,400 / 320, informational
  - best places to visit in india: 4,400 / 260, informational
  - india holiday destinations: 320 / 10, commercial
  - best tourist places in india: 170 / 20, informational

### 6. Rishikesh yoga, meditation & Ganga
- **URL:** `/india-tours/rishikesh-yoga-retreat/`  |  **Page type:** product  |  **Fit weight:** 1.0  |  **Score:** 11,388
- **Focus keyword:** `yoga retreat india`: A 1,600 / B 390 / C 140 · competition Medium (52) · top-of-page bid ₹74–182 · intent commercial
- **Cluster totals (deduped, scored keywords):** A 11,200 / B 3,990 · 174 keywords in CSV · median competition index (A) 53
- **Seasonality:** peaks Jan, Oct, Feb (peak month = 1.33x the monthly average) · **Nov–Mar build-first**
- **Supporting keywords (vol A / vol B, intent):**
  - rishikesh yoga: 590 / 720, informational _(same data as: yoga india rishikesh)_
  - rafting in rishikesh: 720 / 110, commercial
  - rishikesh yoga teacher training: 590 / 170, commercial _(same data as: yoga teacher training india rishikesh)_
  - meditation retreat india: 590 / 70, commercial _(same data as: retreat india meditation, spiritual retreats in india)_
  - retreats in india: 480 / 110, commercial
  - rishikesh yoga retreat: 480 / 90, commercial
  - sivananda ashram in rishikesh: 320 / 170, informational
  - vipassana india: 320 / 140, informational
  - yoga ashram in rishikesh: 320 / 10, informational
  - tapovan rishikesh: 260 / 110, informational
  - yoga ashram india: 260 / 90, informational
  - river rafting in rishikesh: 210 / 30, commercial
  - yoga training rishikesh: 170 / 110, commercial _(same data as: yoga courses in rishikesh)_
  - rishikesh retreat: 170 / 40, commercial
  - veda5 rishikesh: 170 / 40, informational
- **Head terms (not scored):** rishikesh 22,200/12,100

### 7. Kerala tour (backwaters, Munnar, houseboat)
- **URL:** `/india-tours/kerala-tour/`  |  **Page type:** itinerary  |  **Fit weight:** 0.7  |  **Score:** 11,178
- **Focus keyword:** `kerala tour packages`: A 1,900 / B 170 / C 880 · competition High (67) · top-of-page bid ₹67–296 · intent commercial
- **Cluster totals (deduped, scored keywords):** A 20,770 / B 3,600 · 81 keywords in CSV · median competition index (A) 57
- **Seasonality:** peaks Jan, Oct, Nov (peak month = 1.27x the monthly average) · **Nov–Mar build-first**
- **Supporting keywords (vol A / vol B, intent):**
  - kerala backwaters: 3,600 / 1,000, informational
  - house boat in kerala: 2,400 / 390, informational
  - kerala tourism: 2,400 / 390, informational
  - best time to visit kerala: 1,600 / 140, informational
  - kerala holidays: 1,600 / 70, commercial _(same data as: holidays to kerala, holidays to kerala india)_
  - kerala backwaters houseboat: 1,000 / 320, commercial
  - munnar tourist places: 880 / 110, informational
  - kerala tour: 720 / 110, commercial
  - kerala itinerary: 320 / 40, informational
  - kerala trip: 320 / 40, domestic-likely
  - kerala package: 320 / 20, domestic-likely
  - holidays in kerala: 260 / 20, commercial
  - kerala backwaters tour: 210 / 50, commercial
  - tall trees munnar: 210 / 40, informational
  - munnar tour package: 210 / 20, commercial _(same data as: munnar package, munnar trip package)_
- **Head terms (not scored):** munnar 18,100/6,600

### 8. Golden Triangle tour (EXISTING /golden-triangle-tour/)
- **URL:** `/golden-triangle-tour/`  |  **Page type:** itinerary  |  **Fit weight:** 1.0  |  **Score:** 9,538
- **Focus keyword:** `golden triangle india`: A 5,400 / B 590 · competition Medium (45) · top-of-page bid ₹101–302 · intent informational
- **Cluster totals (deduped, scored keywords):** A 11,660 / B 1,120 · 38 keywords in CSV · median competition index (A) 64
- **Seasonality:** peaks Jan, Oct, Nov (peak month = 1.3x the monthly average) · **Nov–Mar build-first**
- **Supporting keywords (vol A / vol B, intent):**
  - delhi triangle tour: 1,000 / 70, commercial _(same data as: golden triangle tour india, golden triangle tours from delhi)_
  - india golden triangle tour: 880 / 40, commercial _(same data as: golden triangle trip)_
  - golden triangle tour: 870* (raw 1,600) / 50, commercial
  - golden triangle india tour packages: 590 / 30, commercial
  - best time to visit india golden triangle: 590 / 10, informational
  - golden triangle tour packages: 390 / 20, commercial
  - golden triangle holidays: 390 / 10, commercial _(same data as: india golden triangle holidays)_
  - delhi agra jaipur tour: 210 / 40, commercial _(same data as: new delhi agra jaipur tour, delhi agra jaipur tour package)_
  - best golden triangle tour packages: 210 / 10, commercial
  - golden triangle itinerary: 170 / 10, informational
  - india triangle tour: 170 / 10, commercial
  - delhi agra jaipur: 140 / 50, informational
  - package holidays to india golden triangle: 140 / 10, commercial
  - luxury golden triangle tour: 110 / 10, commercial
  - delhi golden triangle: 70 / 10, informational

### 9. Goa beach holiday
- **URL:** `/india-tours/goa-holiday/`  |  **Page type:** product  |  **Fit weight:** 0.7  |  **Score:** 8,996
- **Focus keyword:** `goa holiday`: A 6,600 / B 170 / C 90 · competition High (73) · top-of-page bid ₹50–156 · intent commercial
- **Cluster totals (deduped, scored keywords):** A 15,190 / B 1,610 · 56 keywords in CSV · median competition index (A) 60
- **Seasonality:** peaks Jan, Oct, Feb (peak month = 1.74x the monthly average) · **Nov–Mar build-first**
- **Supporting keywords (vol A / vol B, intent):**
  - things to do in goa: 2,400 / 110, informational
  - goa tour package: 1,300 / 90, commercial _(same data as: goa travel packages, goa holiday packages, goa package tour)_
  - goa trip: 880 / 90, domestic-likely _(same data as: trip to goa)_
  - yoga retreat goa: 590 / 210, commercial
  - goa holidays all inclusive: 590 / 30, commercial
  - cheap holidays to goa: 390 / 30, domestic-likely
  - south goa holidays: 320 / 10, commercial
  - goa tour: 170 / 140, commercial
  - yoga in goa india: 170 / 140, informational
  - goa packages: 210 / 20, domestic-likely
  - goa trip package: 170 / 20, domestic-likely
  - goa beach holiday: 170 / 10, commercial
  - yoga goa: 70 / 210, informational
  - goa retreat: 140 / 50, commercial
  - holidays to goa from manchester: 140 / 10, commercial

### 10. Char Dham Yatra (EXISTING /char-dham-yatra-for-nri/)
- **URL:** `/char-dham-yatra-for-nri/`  |  **Page type:** product  |  **Fit weight:** 1.0  |  **Score:** 8,212
- **Focus keyword:** `char dham yatra package`: A 1,600 / B 50 / C 260 · competition Medium (33) · top-of-page bid ₹15–113 · intent commercial
- **Cluster totals (deduped, scored keywords):** A 11,270 / B 1,080 · 47 keywords in CSV · median competition index (A) 21
- **Seasonality:** peaks May, Apr, Jun (peak month = 1.46x the monthly average)
- **Supporting keywords (vol A / vol B, intent):**
  - char dham yatra: 3,600 / 260, informational
  - char dham: 2,900 / 260, informational
  - 4 dham: 720 / 70, informational
  - 4 dham yatra: 720 / 50, informational
  - kedarnath trek: 480 / 70, commercial _(same data as: kedarnath trekking)_
  - chardham yatra by helicopter: 390 / 20, informational
  - chardham yatra tour package: 320 / 10, commercial
  - 4 dham yatra package: 140 / 10, commercial
  - kedarnath trip package: 40 / 10, domestic-likely
  - char dham package: 30 / 10, commercial
  - chardham tour package: 30* (raw 70) / 10, commercial
  - 2 dham yatra by helicopter: 10 / 10, informational
  - 2 dham yatra package: 10 / 10, commercial
  - 2 dham yatra package by helicopter: 10 / 10, commercial
  - 4 dham tour package: 10 / 10, commercial _(same data as: best tour operator for char dham yatra, 4 dham package, char dham yatra package cost)_

### 11. Tiger safari India (Ranthambore, Corbett, Bandhavgarh)
- **URL:** `/india-tours/tiger-safari-india/`  |  **Page type:** product  |  **Fit weight:** 1.0  |  **Score:** 7,690
- **Focus keyword:** `tiger safari india`: A 1,600 / B 110 / C 90 · competition Medium (36) · top-of-page bid ₹117–395 · intent commercial
- **Cluster totals (deduped, scored keywords):** A 7,180 / B 1,140 · 36 keywords in CSV · median competition index (A) 48
- **Seasonality:** peaks Jan, Dec, Oct (peak month = 1.29x the monthly average) · **Nov–Mar build-first**
- **Supporting keywords (vol A / vol B, intent):**
  - india safari: 1,300 / 320, commercial
  - ranthambore tiger safari: 880 / 90, commercial _(same data as: tiger safari india ranthambore)_
  - ranthambore safari: 720 / 320, commercial
  - jim corbett safari: 590 / 50, commercial
  - india wildlife tours: 260 / 10, commercial
  - bandhavgarh national park safari: 210 / 10, commercial
  - kanha tiger safari: 210 / 10, commercial _(same data as: kanha national park safari)_
  - bandhavgarh tiger safari: 170 / 10, commercial
  - best safaris in india: 170 / 10, commercial
  - best tiger safari in india: 170 / 10, commercial
  - india safari tours: 170 / 10, commercial
  - best tiger reserve in india: 110 / 10, informational
  - tiger tours india: 110 / 10, commercial
  - india wildlife safari: 90 / 10, commercial
  - safari booking bandhavgarh: 70 / 10, commercial _(same data as: bandhavgarh national park safari booking)_

### 12. India train travel & luxury trains
- **URL:** `/india-tours/luxury-trains-india/`  |  **Page type:** guide  |  **Fit weight:** 0.7  |  **Score:** 7,374
- **Focus keyword:** `maharaja express india`: A 5,400 / B 1,300 · competition Medium (48) · top-of-page bid ₹70–181 · intent commercial
- **Cluster totals (deduped, scored keywords):** A 9,800 / B 1,850 · 18 keywords in CSV · median competition index (A) 52
- **Seasonality:** peaks Jan, Oct, Nov (peak month = 1.3x the monthly average) · **Nov–Mar build-first**
- **Supporting keywords (vol A / vol B, intent):**
  - luxury train india: 1,900 / 320, commercial
  - maharaja train india: 590 / 70, commercial
  - train journeys in india: 390 / 20, commercial
  - luxury train journeys india: 260 / 10, commercial _(same data as: luxury train travel in india)_
  - india train travel: 210 / 20, commercial
  - luxury train travel india: 170 / 10, commercial
  - train tours india: 170 / 10, commercial
  - best trains in india: 140 / 10, commercial
  - india train holidays: 140 / 10, commercial
  - luxury train tours in india: 110* (raw 210) / 10, commercial
  - delhi to manali train: 90 / 20, domestic-likely
  - cheapest luxury train in india: 70 / 10, domestic-likely
  - india train tours packages: 70 / 10, commercial
  - train through india: 70 / 10, commercial
  - kashmir tour packages for family with train: 10 / 10, domestic-likely

### 13. Rajasthan tour (Jaipur–Jodhpur–Udaipur)
- **URL:** `/india-tours/rajasthan-tour/`  |  **Page type:** itinerary  |  **Fit weight:** 1.0  |  **Score:** 5,782
- **Focus keyword:** `rajasthan tour packages`: A 720 / B 70 · competition High (72) · top-of-page bid ₹83–300 · intent commercial
- **Cluster totals (deduped, scored keywords):** A 6,380 / B 1,510 · 72 keywords in CSV · median competition index (A) 59
- **Seasonality:** peaks Nov, Jan, Dec (peak month = 1.47x the monthly average) · **Nov–Mar build-first**
- **Supporting keywords (vol A / vol B, intent):**
  - places to visit in udaipur: 880 / 70, informational
  - rajasthan tour: 590 / 260, commercial
  - jaipur tour package: 260 / 20, commercial _(same data as: jaipur city tour package, jaipur trip package, jaipur travel package)_
  - sarovar premiere jaipur: 210 / 90, informational
  - jaipur sightseeing: 210 / 40, informational
  - jaipur tour: 210 / 30, commercial
  - royal retreat udaipur: 210 / 20, commercial
  - rajasthan holidays: 210 / 10, commercial
  - park plaza jodhpur: 170 / 70, informational
  - udaipur tour package: 170 / 10, commercial
  - ram pratap palace udaipur: 140 / 30, informational
  - jaipur tourism: 140 / 20, informational
  - rajasthan tours and travels: 140 / 20, commercial
  - jaipur trip: 140 / 10, commercial
  - royal orchid jaipur: 110 / 70, informational
- **Head terms (not scored):** jaipur 74,000/49,500; jodhpur 60,500/18,100; udaipur 33,100/14,800; jaipur palace 5,400/1,900; city palace udaipur 1,900/390; udaipur palace 1,600/320

### 14. India travel insurance (guide)
- **URL:** `/india-tours/india-travel-insurance/`  |  **Page type:** practical  |  **Fit weight:** 1.0  |  **Score:** 4,292
- **Focus keyword:** `trip insurance india`: A 2,900 / B 260 · competition Medium (59) · top-of-page bid ₹199–832 · intent commercial
- **Cluster totals (deduped, scored keywords):** A 4,760 / B 810 · 82 keywords in CSV · median competition index (A) 49
- **Seasonality:** peaks Oct, Mar, Dec (peak month = 1.25x the monthly average) · **Nov–Mar build-first**
- **Supporting keywords (vol A / vol B, intent):**
  - best travel insurance india: 260 / 10, informational _(same data as: best travel insurance to india)_
  - cheap travel insurance india: 170 / 10, domestic-likely
  - travel medical insurance india: 140 / 20, informational _(same data as: travel and health insurance india)_
  - foreign travel insurance india: 140 / 10, informational _(same data as: international travel insurance india)_
  - international health insurance india: 90 / 10, informational _(same data as: international medical insurance india)_
  - travel health insurance india: 70 / 20, informational
  - buy travel insurance india: 70 / 10, informational
  - health insurance for visitors to india: 70 / 10, informational
  - compare travel insurance india: 50 / 10, informational
  - overseas health insurance india: 40 / 10, informational _(same data as: overseas medical insurance india)_
  - tata aig travel insurance india: 40 / 10, informational
  - allianz india travel insurance: 30 / 10, informational _(same data as: allianz travel insurance india)_
  - bajaj allianz travel insurance india: 30 / 10, informational
  - best overseas travel insurance in india: 30 / 10, informational _(same data as: best international travel insurance india)_
  - domestic travel insurance india: 30 / 10, informational

### 15. Kumbh Mela 2027 (Haridwar / Nashik)
- **URL:** `/india-tours/kumbh-mela-tour/`  |  **Page type:** product  |  **Fit weight:** 1.0  |  **Score:** 4,203
- **Focus keyword:** `kumbh mela`: A 5,400 / B 2,900 / C 880 · competition Low (1) · top-of-page bid ₹164–190 · intent informational
- **Cluster totals (deduped, scored keywords):** A 5,510 / B 2,990 · 2 keywords in CSV · median competition index (A) 0
- **Seasonality:** peaks Jan, Apr, Feb (peak month = 1.27x the monthly average) · **Nov–Mar build-first**
- **Supporting keywords (vol A / vol B, intent):**
  - kumbh mela 2027: 110 / 90, informational

### 16. Best time to visit India (month-by-month)
- **URL:** `/india-tours/best-time-to-visit-india/`  |  **Page type:** guide  |  **Fit weight:** 1.0  |  **Score:** 3,852
- **Focus keyword:** `best time to go to india`: A 5,400 / B 260 · competition Low (25) · top-of-page bid ₹33–415 · intent informational
- **Cluster totals (deduped, scored keywords):** A 6,280 / B 280 · 4 keywords in CSV · median competition index (A) 26
- **Seasonality:** peaks Jan, Oct, Nov (peak month = 1.47x the monthly average) · **Nov–Mar build-first**
- **Supporting keywords (vol A / vol B, intent):**
  - best time of year to visit india: 880 / 20, informational

### 17. Gulmarg ski holiday
- **URL:** `/india-tours/gulmarg-ski-holiday/`  |  **Page type:** product  |  **Fit weight:** 1.0  |  **Score:** 3,290
- **Focus keyword:** `gulmarg skiing`: A 2,900 / B 720 / C 260 · competition Low (5) · top-of-page bid ₹41–145 · intent commercial
- **Cluster totals (deduped, scored keywords):** A 2,940 / B 760 · 6 keywords in CSV · median competition index (A) 19
- **Seasonality:** peaks Feb, Jan, Dec (peak month = 2.07x the monthly average) · **Nov–Mar build-first**
- **Supporting keywords (vol A / vol B, intent):**
  - gulmarg package for couple: 10 / 10, domestic-likely
  - gulmarg tour packages: 10 / 10, commercial
  - gulmarg trip: 10 / 10, commercial
  - gulmarg package from delhi: 10 / 0, domestic-likely
  - gulmarg tour packages for couple: 0 / 10, domestic-likely

### 18. Diwali in India tour
- **URL:** `/india-tours/diwali-in-india-tour/`  |  **Page type:** product  |  **Fit weight:** 1.0  |  **Score:** 3,132
- **Focus keyword:** `diwali in india`: A 4,690* (raw 9,900) / B 1,060* (raw 2,400) · competition Low (1) · top-of-page bid ₹15–819 · intent informational
- **Cluster totals (deduped, scored keywords):** A 4,690 / B 1,060 · 2 keywords in CSV · median competition index (A) 1
- **Seasonality:** peaks Oct, Sep, Dec (peak month = 2.45x the monthly average)

### 19. Himachal tour (Shimla–Manali)
- **URL:** `/india-tours/himachal-tour/`  |  **Page type:** itinerary  |  **Fit weight:** 1.0  |  **Score:** 2,996
- **Focus keyword:** `manali tour package`: A 320 / B 50 · competition Medium (50) · top-of-page bid ₹45–149 · intent commercial
- **Cluster totals (deduped, scored keywords):** A 4,530 / B 1,250 · 211 keywords in CSV · median competition index (A) 34
- **Seasonality:** peaks Jan, Dec, Nov (peak month = 1.4x the monthly average) · **Nov–Mar build-first**
- **Supporting keywords (vol A / vol B, intent):**
  - delhi to shimla: 480 / 50, domestic-likely
  - shimla tourist places: 480 / 30, informational _(same data as: places to visit in shimla)_
  - shimla to manali: 260 / 40, informational _(same data as: shimla manali)_
  - himachal tourism: 260 / 30, informational _(same data as: himachal pradesh tourism)_
  - manali tourist places: 260 / 20, informational
  - trekking in himachal pradesh: 140 / 40, commercial
  - package of himachal tour: 110 / 10, commercial _(same data as: himachal pradesh tour package, himachal pradesh tour packages, himachal holiday packages)_
  - shimla tour: 110 / 10, commercial _(same data as: tour to shimla, shimla trip)_
  - shimla tour package: 110 / 10, commercial
  - shimla manali tour package: 90 / 10, domestic-likely _(same data as: shimla manali tour packages)_
  - cottages in manali: 70 / 10, informational
  - manali tour: 70 / 10, commercial _(same data as: trip to manali, kullu manali tour)_
  - manali package: 70 / 10, domestic-likely
  - manali trip: 70 / 10, commercial
  - places to visit in manali: 70 / 10, informational
- **Head terms (not scored):** shimla 27,100/6,600; manali 18,100/5,400; kullu manali 1,600/260; barog himachal pradesh 590/110

### 20. India travel tips & first-time guide
- **URL:** `/india-tours/india-travel-tips-first-time/`  |  **Page type:** guide  |  **Fit weight:** 1.0  |  **Score:** 2,927
- **Focus keyword:** `india travel`: A 1,900 / B 210 · competition Low (31) · top-of-page bid ₹126–433 · intent informational
- **Cluster totals (deduped, scored keywords):** A 4,530 / B 570 · 8 keywords in CSV · median competition index (A) 44
- **Seasonality:** peaks Jan, Mar, Oct (peak month = 1.41x the monthly average) · **Nov–Mar build-first**
- **Supporting keywords (vol A / vol B, intent):**
  - visit india: 1,000 / 170, informational
  - travel india: 720 / 110, informational
  - india travel guide: 480 / 40, informational _(same data as: travel guide india)_
  - india travel tips: 320 / 20* (raw 40), informational
  - luxury travel india: 90 / 10, commercial
  - first time in india: 20 / 10, informational

### 21. Delhi tour (Old & New Delhi)
- **URL:** `/india-tours/delhi-tour/`  |  **Page type:** product  |  **Fit weight:** 1.0  |  **Score:** 2,686
- **Focus keyword:** `delhi tour`: A 320 / B 30 · competition High (91) · top-of-page bid ₹80–301 · intent commercial
- **Cluster totals (deduped, scored keywords):** A 3,120 / B 520 · 30 keywords in CSV · median competition index (A) 73
- **Seasonality:** peaks Jan, Oct, Nov (peak month = 1.35x the monthly average) · **Nov–Mar build-first**
- **Supporting keywords (vol A / vol B, intent):**
  - things to do in new delhi: 1,000 / 70, informational
  - delhi tour package: 320 / 30, commercial
  - delhi trip: 320 / 20, commercial
  - delhi sightseeing: 260 / 110, informational
  - day trips from delhi: 260 / 20, commercial
  - new delhi tours: 170 / 40, commercial
  - delhi day tour: 90 / 10, commercial
  - tours from delhi: 50 / 10, domestic-likely
  - delhi darshan: 40 / 10, informational
  - tours in delhi: 40 / 10, commercial
  - tour delhi: 30 / 20, commercial
  - delhi city tour: 30 / 10, commercial
  - tour and travels delhi: 30 / 10, commercial
  - delhi one day tour: 20 / 10, commercial
  - delhi sightseeing tour: 20 / 10, commercial

### 22. Dharamshala & McLeod Ganj (Tibetan culture, Triund)
- **URL:** `/india-tours/dharamshala-mcleodganj/`  |  **Page type:** itinerary  |  **Fit weight:** 1.0  |  **Score:** 2,241
- **Focus keyword:** `triund trek`: A 1,300 / B 260 / C 320 · competition Low (1) · top-of-page bid ₹74–246 · intent commercial
- **Cluster totals (deduped, scored keywords):** A 2,060 / B 500 · 21 keywords in CSV · median competition index (A) 2
- **Seasonality:** peaks May, Oct, Nov (peak month = 1.33x the monthly average)
- **Supporting keywords (vol A / vol B, intent):**
  - bir billing paragliding: 480 / 110, commercial
  - dharamshala mcleodganj: 110 / 20, informational
  - bir billing paragliding cost: 20 / 10, commercial _(same data as: bir billing paragliding price)_
  - dalhousie tour package: 20 / 10, commercial
  - best paragliding in bir billing: 10 / 10, commercial
  - dalhousie tour package for couple: 10 / 10, domestic-likely
  - dharamshala meditation retreat: 10 / 10, commercial
  - paragliding price in bir billing: 10 / 10, commercial
  - triund camping: 10 / 10, informational
  - triund trek booking: 10 / 10, commercial
  - triund trek camping: 10* (raw 30) / 10, commercial
  - triund trek package: 10 / 10, commercial
  - triund trek starting point: 10 / 10, commercial
  - age limit for paragliding in bir billing: 10 / 0, commercial
  - bir billing paragliding booking: 10 / 0, commercial
- **Head terms (not scored):** mcleod ganj 4,400/1,000; triund 880/210

### 23. Ayurveda retreat Kerala
- **URL:** `/india-tours/ayurveda-retreat-kerala/`  |  **Page type:** product  |  **Fit weight:** 0.7  |  **Score:** 2,223
- **Focus keyword:** `ayurveda retreat kerala`: A 720 / B 210 / C 140 · competition High (69) · top-of-page bid ₹57–246 · intent commercial
- **Cluster totals (deduped, scored keywords):** A 2,790 / B 1,040 · 34 keywords in CSV · median competition index (A) 56
- **Seasonality:** peaks Jan, Nov, Oct (peak month = 1.47x the monthly average) · **Nov–Mar build-first**
- **Supporting keywords (vol A / vol B, intent):**
  - ayurveda retreat india: 590 / 170, commercial
  - yoga retreat kerala: 390 / 140, commercial _(same data as: yoga retreat kerala india)_
  - kerala retreat: 210 / 50, commercial _(same data as: retreats in kerala, retreat in kerala india)_
  - kerala yoga: 140 / 140, informational
  - kerala wellness retreat: 140 / 20, commercial
  - best ayurvedic retreat in kerala: 90 / 20, commercial
  - rishikesh ayurveda retreat: 70 / 20, commercial
  - goa ayurveda retreat: 50 / 50, commercial _(same data as: ayurveda retreat goa india)_
  - ayurveda rishikesh: 40 / 40, informational
  - kerala retreat with ayurveda & yoga: 50 / 10, commercial
  - ayurvedic retreat bangalore: 40 / 10, commercial
  - affordable ayurveda retreat india: 30 / 10, commercial
  - ayurvedic treatment in rishikesh: 30 / 10, informational
  - best ayurvedic retreat in india: 30 / 10, commercial
  - panchakarma retreat india: 30 / 10, commercial

### 24. Andaman Islands
- **URL:** `/india-tours/andaman-islands/`  |  **Page type:** product  |  **Fit weight:** 0.7  |  **Score:** 2,187
- **Focus keyword:** `andaman tour packages`: A 720 / B 140 / C 390 · competition Medium (34) · top-of-page bid ₹33–148 · intent commercial
- **Cluster totals (deduped, scored keywords):** A 4,260 / B 890 · 49 keywords in CSV · median competition index (A) 34
- **Seasonality:** peaks Jan, Nov, Oct (peak month = 1.38x the monthly average) · **Nov–Mar build-first**
- **Supporting keywords (vol A / vol B, intent):**
  - scuba diving in andaman: 590 / 170, informational
  - andaman tourism: 480 / 70, informational _(same data as: andaman and nicobar islands tourism)_
  - andaman trip: 480 / 40, domestic-likely
  - andaman nicobar package: 390 / 40, commercial _(same data as: andaman and nicobar package)_
  - seashell havelock: 260 / 70, informational
  - seashell port blair: 260 / 30, informational _(same data as: sea shell port blair)_
  - andaman nicobar trip: 210 / 40, commercial
  - places to visit in andaman: 140 / 20, informational
  - andaman and nicobar islands package: 140 / 10, commercial
  - scuba diving in havelock: 110* (raw 390) / 30, informational
  - sea shell havelock: 90 / 20, informational
  - port blair to havelock: 70 / 30, informational
  - andaman packages: 50 / 10, domestic-likely
  - symphony samudra port blair: 50 / 10, informational
  - mumbai to andaman cruise: 30 / 10, commercial
- **Head terms (not scored):** andaman islands 22,200/3,600; andaman 14,800/5,400; andaman and nicobar 12,100/1,600; andaman and nicobar islands 12,100/1,600; andaman nicobar 3,600/720; havelock island 2,900/1,300

### 25. Ladakh tour (Leh–Nubra–Pangong)
- **URL:** `/india-tours/ladakh-tour/`  |  **Page type:** itinerary  |  **Fit weight:** 1.0  |  **Score:** 2,145
- **Focus keyword:** `ladakh trip`: A 390 / B 40 · competition Low (23) · top-of-page bid ₹45–215 · intent commercial
- **Cluster totals (deduped, scored keywords):** A 2,270 / B 500 · 58 keywords in CSV · median competition index (A) 38
- **Seasonality:** peaks May, Apr, Aug (peak month = 1.35x the monthly average)
- **Supporting keywords (vol A / vol B, intent):**
  - leh ladakh trip: 320 / 30, commercial
  - leh ladakh tour packages: 260 / 30, commercial _(same data as: leh ladakh package, ladakh trip package, leh ladakh trip package)_
  - ladakh tourism: 210 / 20, informational
  - ladakh tour: 170 / 50, commercial
  - ladakh tour package: 170 / 10, commercial _(same data as: ladakh tour packages)_
  - leh ladakh tour: 90 / 10, commercial
  - ladakh road trip: 70 / 20, commercial
  - leh trip: 50 / 10, commercial
  - ladakh itinerary: 40 / 10, informational
  - leh ladakh itinerary: 40 / 10, informational
  - leh tour package: 40 / 10, commercial _(same data as: leh packages)_
  - ladakh package: 30 / 10, commercial
  - accommodation in pangong: 20 / 10, informational _(same data as: pangong lake accommodation)_
  - ladakh tour package from delhi: 20 / 10, domestic-likely _(same data as: ladakh package from delhi)_
  - ladakh trip cost: 20 / 10, commercial
- **Head terms (not scored):** ladakh 33,100/18,100; leh ladakh 9,900/2,900; pangong lake 3,600/1,900; zanskar 3,600/2,400; nubra valley 1,600/880

### 26. Himachal treks (Hampta Pass, Kheerganga, Kasol/Parvati)
- **URL:** `/india-tours/himachal-treks/`  |  **Page type:** itinerary  |  **Fit weight:** 1.0  |  **Score:** 2,108
- **Focus keyword:** `hampta pass trek`: A 720 / B 140 / C 260 · competition Low (2) · top-of-page bid ₹107–640 · intent commercial
- **Cluster totals (deduped, scored keywords):** A 1,890 / B 560 · 26 keywords in CSV · median competition index (A) 19
- **Seasonality:** peaks May, Jun, Aug (peak month = 1.23x the monthly average)
- **Supporting keywords (vol A / vol B, intent):**
  - himalaya trek india: 480 / 210, commercial
  - kheerganga trek: 390 / 70, commercial
  - himalayan trekking india: 110 / 30, commercial
  - kasol trip: 30 / 10, commercial
  - hampta pass trek package: 20 / 10, commercial
  - chalo kasol: 10 / 10, informational
  - gostops kasol: 10 / 10, informational
  - hampta pass itinerary: 10 / 10, informational
  - hampta pass package: 10 / 10, commercial
  - hampta pass trek route: 10 / 10, commercial _(same data as: hampta pass trek itinerary)_
  - hampta trek: 10 / 10, commercial
  - manali kasol tour package from delhi: 10 / 10, domestic-likely
  - moksha kasol: 10 / 10, informational
  - shimla manali kasol tour package: 10 / 10, domestic-likely
  - about tirthan valley: 10 / 0, informational
- **Head terms (not scored):** kasol 4,400/1,000; hampta pass 880/170; tirthan valley 880/170; great himalayan national park 390/210

### 27. Kashmir tour (Srinagar houseboat–Gulmarg–Pahalgam)
- **URL:** `/india-tours/kashmir-tour/`  |  **Page type:** itinerary  |  **Fit weight:** 1.0  |  **Score:** 1,916
- **Focus keyword:** `kashmir tour package`: A 260 / B 40 / C 260 · competition Medium (45) · top-of-page bid ₹41–161 · intent commercial
- **Cluster totals (deduped, scored keywords):** A 2,350 / B 730 · 101 keywords in CSV · median competition index (A) 36
- **Seasonality:** peaks Jan, May, Apr (peak month = 1.21x the monthly average) · **Nov–Mar build-first**
- **Supporting keywords (vol A / vol B, intent):**
  - best time to visit kashmir: 390 / 30, informational
  - dal lake houseboat: 260 / 40, commercial _(same data as: srinagar houseboat dal lake)_
  - srinagar houseboat: 210 / 70, commercial _(same data as: srinagar boathouse, house boat srinagar)_
  - kashmir trip: 140 / 20, domestic-likely _(same data as: jammu and kashmir trip)_
  - kashmir holiday packages: 140 / 10, commercial
  - kashmir tour: 110 / 20, commercial
  - jammu kashmir tour package: 70 / 10, commercial _(same data as: kashmir travel packages, jammu kashmir trip package)_
  - kashmir package: 50 / 10, domestic-likely _(same data as: jammu kashmir package)_
  - srinagar tour packages: 40 / 10, commercial _(same data as: kashmir tour package from srinagar, srinagar package)_
  - kashmir tour itinerary: 30 / 10, informational _(same data as: kashmir itinerary, kashmir trip itinerary)_
  - best houseboat in srinagar: 20 / 10, commercial
  - jammu kashmir tour: 20 / 10, commercial _(same data as: jammu kashmir trip)_
  - kashmir tour package from delhi: 20 / 10, domestic-likely _(same data as: kashmir package from delhi, kashmir packages from delhi)_
  - srinagar trip package: 20 / 10, domestic-likely _(same data as: kashmir package from srinagar)_
  - kashmir tours and travels: 20 / 10, commercial
- **Head terms (not scored):** kashmir 110,000/40,500

### 28. South India tour (Tamil Nadu temples, Hampi, Mysore)
- **URL:** `/india-tours/south-india-tour/`  |  **Page type:** itinerary  |  **Fit weight:** 0.7  |  **Score:** 1,669
- **Focus keyword:** `south india tour`: A 720 / B 40 / C 70 · competition High (70) · top-of-page bid ₹103–476 · intent commercial
- **Cluster totals (deduped, scored keywords):** A 2,380 / B 300 · 33 keywords in CSV · median competition index (A) 48
- **Seasonality:** peaks Jan, Mar, Oct (peak month = 1.27x the monthly average) · **Nov–Mar build-first**
- **Supporting keywords (vol A / vol B, intent):**
  - south india tour packages: 590 / 20, commercial _(same data as: south india travel packages, south india holiday packages)_
  - southern india holidays: 210 / 10, commercial
  - ooty tour package: 170 / 20, commercial
  - hyderabad tour packages: 170 / 10, commercial
  - tours of southern india: 90 / 10, commercial
  - hampi international: 70 / 10, informational
  - coorg tour packages: 50 / 10, commercial
  - 7 days south india tour packages: 40 / 10, commercial
  - luxury south india tour packages: 40 / 10, commercial
  - ooty package: 40 / 10, commercial
  - hampi tourism: 30 / 10, informational
  - tamil nadu temple tour: 30 / 10, commercial
  - south india tour packages for 10 days: 20 / 10, commercial
  - coorg packages for couple: 10 / 10, commercial
  - hyderabad tour package for family: 10 / 10, domestic-likely
- **Head terms (not scored):** mysore 27,100/8,100; hampi 14,800/6,600; mysore palace 6,600/1,600

### 29. Mumbai tour
- **URL:** `/india-tours/mumbai-tour/`  |  **Page type:** product  |  **Fit weight:** 0.7  |  **Score:** 1,658
- **Focus keyword:** `mumbai tour`: A 390 / B 210 · competition High (81) · top-of-page bid ₹63–254 · intent commercial
- **Cluster totals (deduped, scored keywords):** A 2,190 / B 590 · 15 keywords in CSV · median competition index (A) 80
- **Seasonality:** peaks Jan, Nov, Oct (peak month = 1.4x the monthly average) · **Nov–Mar build-first**
- **Supporting keywords (vol A / vol B, intent):**
  - holidays to mumbai: 480 / 30, commercial
  - bollywood tour mumbai: 260 / 90, commercial
  - dharavi slum tour: 260 / 40, commercial
  - mumbai sightseeing: 210 / 110, informational
  - mumbai tour package: 170 / 10, commercial _(same data as: mumbai holiday package)_
  - mumbai slum tour: 140 / 40, commercial
  - mumbai day tour: 140 / 20, commercial
  - tours and travels mumbai: 70 / 10, commercial
  - mumbai city tour: 40 / 10, commercial
  - mumbai darshan package: 10 / 10, commercial
  - one day trip near mumbai: 10 / 10, commercial
  - mumbai tour package for family: 10 / 0, domestic-likely

### 30. Is India safe for tourists (incl. solo female)
- **URL:** `/india-tours/is-india-safe-for-tourists/`  |  **Page type:** guide  |  **Fit weight:** 1.0  |  **Score:** 1,467
- **Focus keyword:** `is india safe for tourists`: A 2,400 / B 90 / C 170 · competition Low (1) · top-of-page bid ₹1–37 · intent informational
- **Cluster totals (deduped, scored keywords):** A 2,400 / B 90 · 1 keywords in CSV · median competition index (A) 1
- **Seasonality:** peaks Mar, Jan, Sep (peak month = 1.82x the monthly average) · **Nov–Mar build-first**

### 31. Varanasi tour (Ganga aarti, Sarnath)
- **URL:** `/india-tours/varanasi-tour/`  |  **Page type:** itinerary  |  **Fit weight:** 1.0  |  **Score:** 1,446
- **Focus keyword:** `varanasi trip`: A 260 / B 20 · competition Low (21) · top-of-page bid ₹37–214 · intent commercial
- **Cluster totals (deduped, scored keywords):** A 1,760 / B 220 · 15 keywords in CSV · median competition index (A) 33
- **Seasonality:** peaks Nov, Jan, Dec (peak month = 1.53x the monthly average) · **Nov–Mar build-first**
- **Supporting keywords (vol A / vol B, intent):**
  - things to do in varanasi: 720 / 50, informational
  - varanasi ganga aarti: 260 / 30, informational
  - varanasi tour: 170 / 40, commercial
  - varanasi tour package: 170 / 10, commercial
  - kasi tour package: 110 / 10, commercial _(same data as: kashi tour package)_
  - tent city varanasi: 20 / 10* (raw 20), informational
  - travel agency in varanasi: 20* (raw 70) / 10, commercial
  - kashi yatra package: 10 / 10, commercial
  - tour and travels in varanasi: 10 / 10, commercial
  - varanasi tent city: 10 / 10, informational
  - varanasi 2 days tour package: 0 / 10, commercial
- **Head terms (not scored):** varanasi 60,500/33,100; kashi vishwanath temple 9,900/2,400

### 32. Luxury India tours
- **URL:** `/india-tours/luxury-india-tour/`  |  **Page type:** product  |  **Fit weight:** 1.0  |  **Score:** 1,240
- **Focus keyword:** `luxury india tour`: A 1,000 / B 50 / C 40 · competition Low (30) · top-of-page bid ₹222–1066 · intent commercial
- **Cluster totals (deduped, scored keywords):** A 1,210 / B 60 · 2 keywords in CSV · median competition index (A) 40
- **Seasonality:** peaks Sep, Jun, Jul (peak month = 1.48x the monthly average)
- **Supporting keywords (vol A / vol B, intent):**
  - luxury india tour packages: 210 / 10, commercial

### 33. Himalayan motorcycle tour (Ladakh/Spiti on Royal Enfield)
- **URL:** `/india-tours/himalayan-motorcycle-tour/`  |  **Page type:** product  |  **Fit weight:** 1.0  |  **Score:** 1,225
- **Focus keyword:** `himalayan motorcycle tour`: A 880 / B 50 / C 50 · competition Low (25) · top-of-page bid ₹57–148 · intent commercial
- **Cluster totals (deduped, scored keywords):** A 1,700 / B 290 · 26 keywords in CSV · median competition index (A) 19
- **Seasonality:** peaks Mar, May, Apr (peak month = 1.67x the monthly average) · **Nov–Mar build-first**
- **Supporting keywords (vol A / vol B, intent):**
  - ladakh bike trip: 390 / 110, domestic-likely _(same data as: leh ladakh bike trip)_
  - leh ladakh motorcycle tour: 140 / 10, commercial
  - ladakh bike tour packages: 70 / 10, commercial _(same data as: leh ladakh bike tour packages, ladakh bike trip package, leh ladakh bike trip packages)_
  - best himalayan motorcycle tours: 40 / 10, commercial
  - leh bike trip: 40 / 10, domestic-likely _(same data as: bike trip to ladakh)_
  - manali to leh bike trip: 30 / 10, domestic-likely
  - spiti bike trip: 20 / 10, domestic-likely _(same data as: spiti valley bike trip)_
  - spiti valley bike tour packages: 10 / 10, commercial _(same data as: ladakh bike trip cost, bike trip to spiti valley, manali to ladakh bike trip)_
  - delhi to ladakh bike trip: 10 / 10, domestic-likely
  - leh bike tour packages: 10 / 10, commercial
  - leh ladakh bike trip for couples: 10 / 10, domestic-likely
  - manali to spiti valley bike trip: 10 / 10, domestic-likely
  - road trip royal enfield himalayan: 10 / 10, commercial
  - spiti valley bike trip itinerary: 10 / 10, domestic-likely
  - spiti bike tour packages: 10 / 0, commercial

### 34. North India tour
- **URL:** `/india-tours/north-india-tour/`  |  **Page type:** itinerary  |  **Fit weight:** 1.0  |  **Score:** 1,090
- **Focus keyword:** `himalayas tour`: A 390 / B 210 · competition Medium (43) · top-of-page bid ₹63–229 · intent commercial
- **Cluster totals (deduped, scored keywords):** A 970 / B 240 · 3 keywords in CSV · median competition index (A) 51
- **Seasonality:** peaks Dec, Mar, Jan (peak month = 1.4x the monthly average) · **Nov–Mar build-first**
- **Supporting keywords (vol A / vol B, intent):**
  - north india tour packages: 320 / 20, commercial
  - north india tour: 260 / 10, commercial

### 35. Jaisalmer desert safari & camp
- **URL:** `/india-tours/jaisalmer-desert-safari/`  |  **Page type:** product  |  **Fit weight:** 1.0  |  **Score:** 1,080
- **Focus keyword:** `jaisalmer desert camp`: A 320 / B 70 · competition Medium (43) · top-of-page bid ₹17–138 · intent commercial
- **Cluster totals (deduped, scored keywords):** A 970 / B 220 · 17 keywords in CSV · median competition index (A) 57
- **Seasonality:** peaks Nov, Dec, Oct (peak month = 1.98x the monthly average) · **Nov–Mar build-first**
- **Supporting keywords (vol A / vol B, intent):**
  - desert safari jaisalmer: 260 / 30, commercial _(same data as: jaisalmer desert safari)_
  - jaisalmer tour package: 110 / 10, commercial _(same data as: jaisalmer package)_
  - jaisalmer trip: 70 / 10, commercial
  - desert safari in jodhpur: 50 / 10, commercial
  - desert safari camp jaisalmer: 40 / 10, commercial
  - jaisalmer tour: 40 / 10, commercial
  - jaisalmer camp package: 10 / 10, commercial
  - jaisalmer desert camp package: 10 / 10, commercial
  - jaisalmer desert camp package price: 10 / 10, commercial
  - jaisalmer desert safari camp package: 10 / 10, commercial
  - jaisalmer desert safari price: 10 / 10, commercial
  - sam desert camp jaisalmer: 10 / 10, commercial
  - top 10 desert camp in jaisalmer: 10 / 10, commercial
  - family package for jaisalmer: 10 / 0, commercial

### 36. Uttarakhand treks (Valley of Flowers, Roopkund, Kedarkantha)
- **URL:** `/india-tours/uttarakhand-himalaya-treks/`  |  **Page type:** itinerary  |  **Fit weight:** 1.0  |  **Score:** 1,010
- **Focus keyword:** `valley of flowers trek`: A 480 / B 70 · competition Low (3) · top-of-page bid ₹15–272 · intent commercial
- **Cluster totals (deduped, scored keywords):** A 970 / B 220 · 16 keywords in CSV · median competition index (A) 33
- **Seasonality:** peaks Aug, May, Jul (peak month = 1.27x the monthly average)
- **Supporting keywords (vol A / vol B, intent):**
  - roopkund trek: 170 / 40, commercial
  - uttarakhand tour package: 90 / 10, commercial _(same data as: uttarakhand tour packages)_
  - uttarakhand tour: 70 / 10, commercial _(same data as: uttarakhand trip)_
  - nainital tour package: 50 / 10, commercial
  - nainital package: 30 / 10, commercial
  - mussoorie tour package: 10 / 10, commercial
  - nainital couple package: 10 / 10, domestic-likely
  - nainital tour package from delhi: 10 / 10, domestic-likely
  - nainital tour packages for couple: 10 / 10, domestic-likely
  - uttarakhand packages: 10 / 10, commercial
  - uttarakhand tour packages from delhi: 10 / 10, domestic-likely
  - uttarakhand trip plan: 10 / 10, commercial
  - nainital tour packages for family: 10 / 0, domestic-likely

### 37. Ladakh treks (Markha, Stok Kangri)
- **URL:** `/india-tours/ladakh-trekking/`  |  **Page type:** itinerary  |  **Fit weight:** 1.0  |  **Score:** 800
- **Focus keyword:** `markha valley trek`: A 590 / B 320 · competition Low (13) · top-of-page bid ₹52–283 · intent commercial
- **Cluster totals (deduped, scored keywords):** A 630 / B 340 · 3 keywords in CSV · median competition index (A) 14
- **Seasonality:** peaks May, Aug, Jun (peak month = 1.4x the monthly average)
- **Supporting keywords (vol A / vol B, intent):**
  - stok kangri trek: 40 / 20, commercial
- **Head terms (not scored):** stok kangri 390/260

### 38. Darjeeling & Sikkim
- **URL:** `/india-tours/darjeeling-sikkim-tour/`  |  **Page type:** itinerary  |  **Fit weight:** 0.7  |  **Score:** 798
- **Focus keyword:** `darjeeling tour`: A 140 / B 480 / C 30 · competition High (68) · top-of-page bid ₹66–259 · intent commercial
- **Cluster totals (deduped, scored keywords):** A 860 / B 730 · 31 keywords in CSV · median competition index (A) 37
- **Seasonality:** peaks Jan, Dec, Jun (peak month = 1.23x the monthly average) · **Nov–Mar build-first**
- **Supporting keywords (vol A / vol B, intent):**
  - sikkim tour package: 170 / 20, commercial _(same data as: sikkim travel packages, sikkim holiday packages, sikkim trip package)_
  - darjeeling tourism: 140 / 20, informational
  - sikkim tour: 110 / 10, commercial _(same data as: sikkim trip)_
  - sikkim gangtok tour: 40 / 10, commercial
  - gangtok tour package: 30 / 10, commercial
  - gangtok trip: 20 / 10, commercial
  - north sikkim tour: 20 / 10, commercial
  - sikkim packages: 20 / 10, commercial
  - darjeeling and gangtok tour package: 10 / 10, commercial
  - darjeeling package for couple: 10 / 10, domestic-likely
  - darjeeling tourism package: 10 / 10, commercial
  - gangtok darjeeling sikkim family package: 10 / 10, commercial
  - gangtok darjeeling tour package: 10 / 10, commercial
  - gangtok package: 10 / 10, commercial
  - gangtok travel agency: 10 / 10, commercial
- **Head terms (not scored):** darjeeling 40,500/135,000

### 39. Pushkar Camel Fair tour
- **URL:** `/india-tours/pushkar-camel-fair/`  |  **Page type:** product  |  **Fit weight:** 1.0  |  **Score:** 696
- **Focus keyword:** `pushkar camel fair`: A 1,000 / B 320 / C 140 · competition Low (2) · top-of-page bid ₹57–366 · intent informational
- **Cluster totals (deduped, scored keywords):** A 1,000 / B 320 · 1 keywords in CSV · median competition index (A) 2
- **Seasonality:** peaks Oct, Nov, Jan (peak month = 1.78x the monthly average) · **Nov–Mar build-first**

### 40. Spiti Valley tour
- **URL:** `/india-tours/spiti-valley-tour/`  |  **Page type:** itinerary  |  **Fit weight:** 1.0  |  **Score:** 684
- **Focus keyword:** `spiti valley tour`: A 110 / B 20 / C 40 · competition Medium (46) · top-of-page bid ₹43–177 · intent commercial
- **Cluster totals (deduped, scored keywords):** A 680 / B 290 · 51 keywords in CSV · median competition index (A) 16
- **Seasonality:** peaks May, Jun, Jan (peak month = 1.33x the monthly average)
- **Supporting keywords (vol A / vol B, intent):**
  - spiti trip: 110 / 10, commercial _(same data as: spiti valley trip)_
  - spiti valley from delhi: 30 / 10, domestic-likely
  - spiti valley road trip: 30 / 10, commercial
  - spiti tour package: 20 / 10, commercial _(same data as: spiti valley tour packages)_
  - spiti valley packages: 20 / 10, commercial
  - best spiti valley tour packages: 10 / 10, commercial
  - hampta pass chandratal trek: 10 / 10, commercial _(same data as: hampta pass and chandratal trek)_
  - spiti itinerary: 10 / 10, informational _(same data as: spiti valley itinerary, itinerary for spiti valley)_
  - kaza tour package: 10 / 10, commercial
  - lahaul spiti tour: 10 / 10, commercial
  - spiti circuit trip: 10 / 10, commercial
  - spiti group tours: 10 / 10, commercial
  - spiti tour: 10 / 10, commercial
  - spiti tour itinerary: 10 / 10, informational
  - spiti travel package: 10 / 10, commercial
- **Head terms (not scored):** spiti valley 9,900/1,600

### 41. India itineraries (10 days / 2 weeks / 3 weeks)
- **URL:** `/india-tours/india-itinerary-2-weeks/`  |  **Page type:** itinerary  |  **Fit weight:** 1.0  |  **Score:** 597
- **Focus keyword:** `india itinerary`: A 390 / B 50 · competition High (77) · top-of-page bid ₹75–263 · intent informational
- **Cluster totals (deduped, scored keywords):** A 930 / B 130 · 5 keywords in CSV · median competition index (A) 48
- **Seasonality:** peaks Jan, Oct, Dec (peak month = 1.37x the monthly average) · **Nov–Mar build-first**
- **Supporting keywords (vol A / vol B, intent):**
  - 2 weeks in india itinerary: 320 / 40, informational
  - india itinerary 3 weeks: 110 / 30, informational
  - india itinerary 10 days: 110 / 10, informational

### 42. What to wear in India
- **URL:** `/india-tours/what-to-wear-in-india/`  |  **Page type:** practical  |  **Fit weight:** 1.0  |  **Score:** 492
- **Focus keyword:** `what to wear in india`: A 590 / B 30 / C 30 · competition High (100) · top-of-page bid ₹12–130 · intent informational
- **Cluster totals (deduped, scored keywords):** A 800 / B 40 · 2 keywords in CSV · median competition index (A) 100
- **Seasonality:** peaks Jan, Feb, Nov (peak month = 1.7x the monthly average) · **Nov–Mar build-first**
- **Supporting keywords (vol A / vol B, intent):**
  - what to wear in india female: 210 / 10, informational

### 43. Hornbill Festival Nagaland
- **URL:** `/india-tours/hornbill-festival-tour/`  |  **Page type:** product  |  **Fit weight:** 0.7  |  **Score:** 437
- **Focus keyword:** `hornbill festival`: A 880 / B 320 · competition Low (1) · top-of-page bid ₹11–114 · intent informational
- **Cluster totals (deduped, scored keywords):** A 880 / B 320 · 1 keywords in CSV · median competition index (A) 1
- **Seasonality:** peaks Dec, Nov, Oct (peak month = 2.72x the monthly average) · **Nov–Mar build-first**

### 44. India SIM / eSIM for tourists
- **URL:** `/india-tours/india-sim-card-for-tourists/`  |  **Page type:** practical  |  **Fit weight:** 1.0  |  **Score:** 363
- **Focus keyword:** `india sim card tourist`: A 260 / B 50 · competition High (98) · top-of-page bid ₹43–150 · intent informational
- **Cluster totals (deduped, scored keywords):** A 540 / B 130 · 4 keywords in CSV · median competition index (A) 98
- **Seasonality:** peaks Jan, Nov, Oct (peak month = 1.78x the monthly average) · **Nov–Mar build-first**
- **Supporting keywords (vol A / vol B, intent):**
  - esim india tourist: 170 / 70, informational
  - india esim tourist: 110 / 10, informational

### 45. Meghalaya & Northeast India
- **URL:** `/india-tours/northeast-india-tour/`  |  **Page type:** itinerary  |  **Fit weight:** 0.7  |  **Score:** 298
- **Focus keyword:** `north east india tour packages`: A 170 / B 20 · competition Medium (67) · top-of-page bid ₹50–224 · intent commercial
- **Cluster totals (deduped, scored keywords):** A 400 / B 50 · 5 keywords in CSV · median competition index (A) 48
- **Seasonality:** peaks Apr, May, Jan (peak month = 1.31x the monthly average)
- **Supporting keywords (vol A / vol B, intent):**
  - northeast india tour: 110 / 10, commercial
  - meghalaya trip: 90 / 10, commercial
  - north east tour packages: 30 / 10, commercial
- **Head terms (not scored):** meghalaya 22,200/8,100

### 46. Private car & driver in India (EXISTING)
- **URL:** `/india-tours/private-driver-india/`  |  **Page type:** product  |  **Fit weight:** 1.0  |  **Score:** 255
- **Focus keyword:** `private driver india`: A 110 / B 50 / C 10 · competition Medium (45) · top-of-page bid ₹152–783 · intent commercial
- **Cluster totals (deduped, scored keywords):** A 210 / B 90 · 5 keywords in CSV · median competition index (A) 45
- **Seasonality:** peaks Jan, Oct, Feb (peak month = 1.73x the monthly average) · **Nov–Mar build-first**
- **Supporting keywords (vol A / vol B, intent):**
  - driver in delhi: 40 / 10, commercial
  - car with driver india: 30 / 10, commercial
  - hire driver in delhi: 20 / 10, commercial
  - india tour with driver: 10 / 10, commercial

### 47. Delhi airport transfer
- **URL:** `/india-tours/delhi-airport-transfer/`  |  **Page type:** product  |  **Fit weight:** 1.0  |  **Score:** 246
- **Focus keyword:** `delhi airport transfer`: A 110 / B 20 · competition Medium (51) · top-of-page bid ₹44–144 · intent commercial
- **Cluster totals (deduped, scored keywords):** A 240 / B 60 · 6 keywords in CSV · median competition index (A) 65
- **Seasonality:** peaks Jan, Dec, Nov (peak month = 1.61x the monthly average) · **Nov–Mar build-first**
- **Supporting keywords (vol A / vol B, intent):**
  - delhi airport taxi booking: 50 / 10, commercial
  - delhi airport pickup: 40 / 10, informational _(same data as: delhi airport pickup service)_
  - airport transfer delhi: 30 / 10, commercial
  - airport pickup delhi: 10 / 10, informational

### 48. India tour cost & prices (USD)
- **URL:** `/india-tours/india-tour-cost/`  |  **Page type:** guide  |  **Fit weight:** 1.0  |  **Score:** 235
- **Focus keyword:** `cheap holidays to india`: A 170 / B 10 · competition Medium (61) · top-of-page bid ₹45–208 · intent domestic-likely
- **Cluster totals (deduped, scored keywords):** A 390 / B 40 · 5 keywords in CSV · median competition index (A) 52
- **Seasonality:** peaks Oct, Jan, Feb (peak month = 1.66x the monthly average) · **Nov–Mar build-first**
- **Supporting keywords (vol A / vol B, intent):**
  - trip to india cost: 110 / 10, commercial
  - all india tour packages prices: 50 / 10, commercial
  - india tours packages prices: 50 / 10, commercial
  - india tour cost: 10 / 0, commercial

### 49. Buddhist circuit (Bodh Gaya–Sarnath–Kushinagar)
- **URL:** `/india-tours/buddhist-circuit-tour/`  |  **Page type:** itinerary  |  **Fit weight:** 1.0  |  **Score:** 186
- **Focus keyword:** `bodhgaya temple`: A 260 / B 70 · competition Medium (63) · top-of-page bid - · intent informational
- **Cluster totals (deduped, scored keywords):** A 270 / B 80 · 3 keywords in CSV · median competition index (A) 43
- **Seasonality:** peaks Nov, Jan, Dec (peak month = 1.71x the monthly average) · **Nov–Mar build-first**
- **Supporting keywords (vol A / vol B, intent):**
  - buddhist circuit india: 10 / 10, informational
- **Head terms (not scored):** bodh gaya 5,400/1,300

### 50. India family tour
- **URL:** `/india-tours/india-family-tour/`  |  **Page type:** product  |  **Fit weight:** 1.0  |  **Score:** 170
- **Focus keyword:** `india family tour packages`: A 70 / B 10 · competition Medium (54) · top-of-page bid ₹52–262 · intent commercial
- **Cluster totals (deduped, scored keywords):** A 150 / B 40 · 6 keywords in CSV · median competition index (A) 40
- **Seasonality:** peaks Oct, Dec, Jan (peak month = 1.29x the monthly average) · **Nov–Mar build-first**
- **Supporting keywords (vol A / vol B, intent):**
  - family trip in india: 50 / 10, commercial
  - india family tour: 10 / 10, commercial
  - lakshadweep family tour packages: 10 / 10, commercial
  - odisha family tour packages: 10 / 0, commercial

### 51. India & Nepal combined tour
- **URL:** `/india-tours/india-nepal-tour/`  |  **Page type:** itinerary  |  **Fit weight:** 1.0  |  **Score:** 115
- **Focus keyword:** `india and nepal tour`: A 110 / B 10 · competition High (68) · top-of-page bid ₹116–536 · intent commercial
- **Cluster totals (deduped, scored keywords):** A 110 / B 10 · 1 keywords in CSV · median competition index (A) 68
- **Seasonality:** peaks Jan, Oct, Nov (peak month = 1.62x the monthly average) · **Nov–Mar build-first**

### 52. Chadar frozen-river trek (Zanskar)
- **URL:** `/india-tours/chadar-trek/`  |  **Page type:** itinerary  |  **Fit weight:** 1.0  |  **Score:** 76
- **Focus keyword:** `chadar lake trek`: A 10 / B 10 · competition Low (0) · top-of-page bid - · intent commercial
- **Cluster totals (deduped, scored keywords):** A 60 / B 40 · 10 keywords in CSV · median competition index (A) 0
- **Seasonality:** peaks Sep, Oct, May (peak month = 1.96x the monthly average)
- **Supporting keywords (vol A / vol B, intent):**
  - chadar trek booking: 10 / 10, commercial
  - chadar trek in december: 10 / 10, commercial
  - chadar trek package: 10 / 10, commercial
  - best chadar: 10 / 0, informational
  - best chadar trek organizers: 10 / 0, commercial
- **Head terms (not scored):** chadar 1,600/480

### 53. Amritsar & Golden Temple
- **URL:** `/india-tours/amritsar-golden-temple-tour/`  |  **Page type:** itinerary  |  **Fit weight:** 1.0  |  **Score:** 45
- **Focus keyword:** `golden temple amritsar tour`: A 40 / B 10 / C 10 · competition Medium (50) · top-of-page bid ₹55–293 · intent commercial
- **Cluster totals (deduped, scored keywords):** A 40 / B 10 · 3 keywords in CSV · median competition index (A) 50
- **Seasonality:** peaks Apr, May, Mar (peak month = 2.22x the monthly average)
- **Head terms (not scored):** amritsar 27,100/8,100; golden temple amritsar 8,100/1,000

