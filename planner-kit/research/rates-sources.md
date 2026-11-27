# Rate sources (v0.1, 15 Oct 2026)

| Item | Value used | Basis | Checked |
|---|---|---|---|
| Car ₹/km (sedan 12, Ertiga 14, Crysta 19, Tempo 26, Urbania 36), driver ₹400/₹500 per night | same as live /cabs/ engine | `cab-kit/cabs_data.py` (branch `cabs`), benchmarked weekly by the Cab SEO, Fares & QA agent (`research/fare-watch.csv`) | 15 Oct 2026 |
| Min 250 km/day billing (150 on Kashmir/Ladakh union days) | engine | Standard North-India outstation billing; union days use local-taxi pricing instead | 15 Oct 2026 |
| Hotel Manali mid-range | 3,400 MAP/room-night (popular hill class) | championtraveler.com "cost of a trip to Manali": 2–3★ room $33–48/night; 4–5★ $82–129/night (no date on page) → MAP + higher-side buffer | 15 Oct 2026 |
| Luxury tier ×2.6 | ≈ ₹8,800/night in popular hills | same source, 4–5★ range | 15 Oct 2026 |
| Peak ×1.25 and windows | Suzu's own homepage rule (15 Mar–30 Jun, all Oct, 20 Dec–5 Jan) | Homepage agent brief | 15 Oct 2026 |
| Service 10 % + GST 5 % | tour-operator GST 5 % (no ITC) | — | 15 Oct 2026 |

TODO (BACKLOG #2): replace the single generic source with 3-date public listing samples per class (MakeMyTrip / Agoda / Booking.com) for Shimla, Manali, Dharamshala, Dalhousie, Kasol, Kaza, Sangla, Katra, Haridwar, Srinagar, Gulmarg, Leh.

---
# Rate audit #1 — 16 Oct 2026 (BACKLOG #2, partial)

Source: live hotel metasearch (SlickTrip / Google Hotels data, via MCP), 2 adults, 1 room, 1 night, filter ≥3★, sorted cheapest first, prices "cheapest room" USD, converted at ₹88/$. Off-peak dates: 18 Nov 2026 and 10 Feb 2027 (Leh: 10 Jun 2027, peak).
Method: "public deluxe MAP" = median of the first ~6 priced 3★/4★ listings with guest rating ≥ 4.0, × 1.12 (room GST, prices may be pre-tax) + ₹900/room dinner for 2 (MAP). Target base rate = 0.87 × public (so base + 10 % service + 5 % GST ≈ public retail → estimate never below what a guest sees online). Max +15 % per class per run unless a place is reclassified.

| Place | Date | Priced listings (USD/night, ≥4.0) | Median | Public deluxe MAP ₹ | Planner deluxe before → after |
|---|---|---|---|---|---|
| Manali | 18 Nov 26 | 26, 28, 29, 35, 45, 48 | 32 | 4,050 | 3,400 → 3,800 (hill_premium) |
| Manali | 10 Feb 27 | 21, 26, 34, 35, 40, 42 | 34.5 | 4,300 | ″ |
| Shimla | 18 Nov 26 | 37, 39, 41, 45, 46 (3.9★ 26 excluded) | 41 | 4,940 | ″ |
| Shimla | 10 Feb 27 | 45, 49, 65 | 49 | 5,730 | ″ |
| Dharamshala | 18 Nov 26 | 18, 27, 31, 37, 46, 49 | 34 | 4,250 | ″ |
| Kasol | 18 Nov 26 | 22, 33, 33, 45 | 33 | 4,150 | 2,800 → 3,200 (hill, +14 % cap; one sample only) |
| Katra | 18 Nov 26 | 19, 31, 33, 35, 37, 41 | 34 | 4,250 | 2,400 → 4,000 (new class pilgrim_city) |
| Katra | 10 Feb 27 | 14, 29, 42, 47, 47, 48 | 44.5 | 5,290 | ″ |
| Haridwar | 18 Nov 26 | 26, 29, 33, 46, 47, 58 | 39.5 | 4,790 | ″ |
| Srinagar | 18 Nov 26 | 46, 65, 86 (no 3★ listed) | 65 | 7,330 (4★) | 3,800 → 4,400 (kashmir; super-deluxe 4★ now 6,380) |
| Srinagar | 10 Feb 27 | 73, 108, 137 (4★) | 108 | 11,540 (4★) | ″ |
| Leh | 10 Jun 27 (peak) | 20, 30, 31, 83 | 30.5 | 3,910 | 3,900 ×1.25 peak = 4,875 → unchanged (above market) |
| Manali luxury | 18 Nov 26 | 5★ 48, 116, 142 | 116 | 12,330 | 9,880 (×2.6) ≈ 0.8× → unchanged, re-check next audit |

Not sampled yet (unchanged): metro, remote, small pilgrim towns (Naina Devi, Chintpurni, Jwala Ji, Kangra, Chamunda, Char Dham towns), Gulmarg/Pahalgam, Nubra/Pangong. Next audit: these + MakeMyTrip package listings for the 3 top templates.
Search URLs (re-open to re-check): https://slicktrip.com/hotels?key=Manali,-Himachal-Pradesh,-India%3B2026-11-18%3B2026-11-19%3B2%3B0&hotel_class=3,4,5 (swap place/dates).

---
# Rate audit #2 — 18 Oct 2026 (BACKLOG #2, classes not sampled in #1)

Same source and method as audit #1 (live hotel metasearch via MCP, 2 adults · 1 room · 1 night, ≥3★, cheapest first, USD × ₹88; public deluxe MAP = median of first ~6 priced listings with rating ≥ 4.0 × 1.12 + ₹900; target base ≈ 0.87 × public; max +15 % per class per run unless a place is reclassified). Off-peak date 18 Nov 2026; remote/Ladakh on 10 Jun 2027 (peak ×1.25 compared).

| Place (class) | Date | Priced listings (USD) | Median | Public deluxe MAP ₹ | Planner deluxe before → after |
|---|---|---|---|---|---|
| Gulmarg (kashmir) | 18 Nov 26 | 49, 66, 80, 112, 201 (3.8★ 118 excl.) | 80 | 8,790 | 4,400 → **6,800 new class `kashmir_resort`** (Gulmarg, Pahalgam, Sonamarg) |
| Pahalgam (kashmir) | 18 Nov 26 | 33, 58, 75, 80, 92, 116 | 77.5 | 8,540 | ″ |
| Srinagar (kashmir) | audit #1 | — | — | 7,330 (4★) | 4,400 → 5,000 (+14 %, cap; still below — re-check) |
| Jaipur (rajasthan) | 18 Nov 26 | 28, 31, 61, 89, 110 (3–4★) | 61 | 6,910 | 3,600 → 4,100 (+14 %, cap) |
| Udaipur (rajasthan) | 18 Nov 26 | 28, 30, 33, 37, 45, 55 | 35 | 4,350 | ″ |
| New Delhi (metro) | 18 Nov 26 | 34, 106, 124, 133, 139, 170 (bimodal; cheapest 4★ 4.4 = 34) | — | 4,250 (cheapest good 4★) | 3,200 → 3,500 (+9 %) |
| Amritsar (metro) | 18 Nov 26 | 11, 18, 22, 28, 31, 33 | 25 | 3,360 | ″ (now above market, OK) |
| Kangra / Dharamshala side (pilgrim) | 18 Nov 26 | 32, 38, 52, 53, 71, 76 | 52.5 | 6,080 (3–5★ mix) | 2,400 → 2,750 (+15 %, cap; small temple towns have fewer listed 3★) |
| Kaza (remote) | 10 Jun 27 | 26, 29, 32, 40, 50, 59 | 36 | 4,450 | 3,600 × 1.25 peak = 4,500 → unchanged (above) |
| Nubra (ladakh) | 10 Jun 27 | 44, 49, 55, 56 (+ 5★ 206, 253) | 55.5 | 6,370 | 3,900 → 4,300 (+10 %; Leh was above market in #1) |

Note: Rajasthan's real high season is Oct–Mar (our peak windows are hill-based); flagged for a Rajasthan-specific peak window in a later run.
Next audit: Srinagar + Jaipur again (both still below target after the cap), small Mata towns (Chintpurni, Jwala Ji, Naina Devi), Char Dham towns, Manali luxury.

# Rajasthan high-season window — 23 Nov 2026 (v2.8)
Rajasthan city/heritage hotels peak in the cool months Oct–Mar (Diwali, Pushkar fair, Christmas–New Year, wedding season) and are off-season Apr–Sep (heat, monsoon). Audit #2 already showed Jaipur's public deluxe MAP at ₹6,910 on 18 Nov vs our ₹4,100 base. Change: `rates.json` hotel.peak.by_class.rajasthan = 1 Oct – 31 Mar (×1.25), replacing the hill windows for that class only (Mount Abu = hill class, Pushkar = pilgrim class keep the default windows). Effect: Rajasthan Royal 2 adults deluxe 10 Dec ₹46,000/adult (8 peak nights); 10 May ₹41,700/adult.
Sources (season, neutral/industry): https://www.thomascook.in/india-tourism/best-time-to-visit-rajasthan · https://www.sotc.in/tourism/rajasthan-tourism/best-time-to-visit-rajasthan · https://www.skyscanner.co.in/news/best-time-to-visit-rajasthan

# Gulmarg snow & ski season — 24 Nov 2026 (v2.9)
Gulmarg (class kashmir_resort, deluxe ₹6,800 off-peak) had no winter peak: our default windows give it only 20 Dec–5 Jan, but Dec–early Mar is Gulmarg's costliest season (gondola/ski). Public data: zoutons Gulmarg guide (27 Aug 2026) — "Winter (Dec–early Mar): Peak of peaks", "January-February weekends are the most expensive nights of the Gulmarg year", mid-range near gondola ₹4,000–10,000/night; travelcoffee (28 Oct 2026) — sampled rates for 15 Dec 2026, 2 adults: median ₹6,207 (1–2.5 km from Gondola), ₹11,231 (within 1 km), ₹2,741 (Tangmarg). Room-only figures; our MAP deluxe ₹6,800 → ₹8,500 with peak keeps us at/above the mid band.
Change: `rates.json` hotel.peak.add_by_place.gulmarg = 15 Dec – 14 Mar (×1.25) added on top of the default windows (15 Mar–30 Jun, Oct, Christmas–New Year already peak). Pahalgam / Sonamarg winter stays off-peak (no evidence of a winter high season).
Sources: https://zoutons.com/news/gulmarg-trip-guide-2026 · https://travelcoffee.in/blog/gulmarg-vs-tangmarg-stay-in-winter

# Rate audit #3 — 25 Nov 2026 (v3.0) — small Mata towns + Char Dham towns
Same method as audits #1/#2 (live hotel metasearch via MCP, 2 adults · 1 room · 1 night, cheapest first, USD × ₹88; public deluxe MAP = median priced listing × 1.12 + ₹900; target base ≈ 0.87 × public; max +15 % per class per run).

| Place (class) | Date | Priced listings (USD) | Median | Public deluxe MAP ₹ | Planner deluxe before → after |
|---|---|---|---|---|---|
| Chintpurni (pilgrim) | 15 Jan 27 | 17, 21, 24, 44 (4★), 46, 116 (4★) | 34 | 4,250 | 2,750 → **3,160** (+15 %, cap) |
| Uttarkashi (pilgrim) | 15 Sep 27 | 14, 15, 27, 31, 31, 115 (6 of 12 unpriced) | 29 | 3,760 | ″ |
| Badrinath (pilgrim) | 15 Sep 27 | 3★ Hotel Dwarikesh 74 only (7 of 8 ≥3★ unpriced — 2027 yatra rates not out) | — | ~8,190 (1 listing) | ″ — thin; re-check Apr 2027 when yatra rates publish |
| Guptkashi (pilgrim) | 15 Sep 27 | 0 of 12 priced | — | — | re-check Apr 2027 |

Kangra (audit #2) was 6,080 public. The pilgrim class is still below target after the cap → re-check next audit (with Jwala Ji, Naina Devi). Char Dham towns: flag for a yatra-season (May–Jun, Sep–Oct) by_class window once 2027 rates are published.
Source: https://slicktrip.com/hotels (searches above, run 25 Nov 2026).

# Rate audit #4 — 26 Nov 2026 (v3.1) — Srinagar, Jaipur, Jwala Ji, Naina Devi
Same method (live hotel metasearch via MCP, 2 adults · 1 room · 1 night, cheapest first, USD × ₹88; public deluxe MAP = median priced listing × 1.12 + ₹900; target base ≈ 0.87 × public; max +15 % per class per run). Srinagar/Jaipur: ≥3★ filter, deluxe-comparable median = 3–4★ listings (5★ excluded) except Jaipur July (cheap 5★ included, few 3–4★ priced).

| Place (class) | Date | Priced listings (USD) | Median | Public deluxe MAP ₹ | Planner deluxe before → after |
|---|---|---|---|---|---|
| Srinagar (kashmir) | 15 Jan 27 (off-peak) | 3–4★: 62, 65, 97, 104, 110, 172 (5★ 127–311) | 100 | 10,800 | 5,000 → **5,750** (+15 %, cap; still far below → next audit) |
| Jaipur (rajasthan) | 15 Jan 27 (peak) | 3–4★: 50, 68, 71, 86, 100 | 71 | 7,900 (vs our peak 4,100 × 1.25 = 5,125) | 4,100 → **4,700** (+15 %, cap) |
| Jaipur (rajasthan) | 15 Jul 27 (off-peak) | 50 (5★ deal), 57, 62, 75, 120 | 62 | 7,010 | ″ — target ≈ 6,100, still below → next audit |
| Jawalamukhi / Jwala Ji (pilgrim) | 15 Jan 27 | 23, 27, 50, 55, 56, 116, 124 (5 unpriced) | 55 | 6,320 | 3,160 → **3,480** (= target 0.87 × median of Chintpurni 4,250 / Uttarkashi 3,760 / Naina Devi 3,660 / Jwala Ji 6,320 ≈ 4,000) |
| Naina Devi (pilgrim) | 15 Jan 27 | 15, 25, 25, 31, 45, 55 (6 unpriced; some Anandpur Sahib) | 28 | 3,660 | ″ |

Pilgrim class now at target. Kashmir (Srinagar) and Rajasthan still below → continue +15 %/run in later audits. Char Dham yatra-season window: re-check Apr 2027.
Source: https://slicktrip.com/hotels (searches above, run 26 Nov 2026).

# Rate audit #5 — 27 Nov 2026 (v3.2) — Srinagar/Jaipur step + Udaipur, Jodhpur spot-check
Same method (live hotel metasearch via MCP, 2 adults · 1 room · 1 night, ≥3★, cheapest first, USD × ₹88; public deluxe MAP = median 3–4★ priced listing × 1.12 + ₹900; target base ≈ 0.87 × public; max +15 % per class per run).

| Place (class) | Date | Priced 3–4★ listings (USD) | Median | Public deluxe MAP ₹ | Planner deluxe before → after |
|---|---|---|---|---|---|
| Udaipur (rajasthan) | 15 Jan 27 (peak) | 12, 31, 37, 42, 43, 44, 65, 128 (5★ 190–672) | 42.5 | 5,090 | ″ |
| Jodhpur (rajasthan) | 15 Jan 27 (peak) | 50, 79, 106, 110, 113 (5★ 116–1,249) | 106 | 11,350 | ″ |
| Rajasthan class (Jaipur 7,900 / 7,010 · Udaipur 5,090 · Jodhpur 11,350) | — | — | — | median ≈ 7,450 → target ≈ 6,500 | 4,700 → **5,400** (+15 %, cap; still below → next audit) |
| Srinagar (kashmir) | audit #4 (15 Jan 27) | — | 100 | 10,800 → target ≈ 9,400 | 5,750 → **6,600** (+15 %, cap; still below → next audit) |

Effect (2 adults deluxe): Rajasthan Royal 10 Dec ₹49,900 → ₹54,000/adult, 10 May ₹45,000 → ₹48,200; Kashmir (gmpeak) 15 Jan ₹29,000 → ₹29,900; Shimla–Manali unchanged (₹23,300 rjpeak.sm).
Source: https://slicktrip.com/hotels (searches above, run 27 Nov 2026).
