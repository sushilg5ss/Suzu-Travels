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
