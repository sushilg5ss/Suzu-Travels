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
