# Festival windows used by the planner (crowd notes, not pricing)

Checked 17 Oct 2026. Pricing is NOT changed by these windows — Sharad Navratri falls in the October peak and Chaitra Navratri in the 15 Mar–30 Jun peak (rates.json `peak`), so estimates already carry ×1.25.

| Festival | Dates | Source |
|---|---|---|
| Sharad Navratri 2026 | 11–20 Oct 2026 (Ghatasthapana → Vijayadashami) | rampuri.com "Navratri 2026 Dates: Ghatasthapana to Dussehra (Oct 11-20)" https://rampuri.com/navratri-durga-puja-2016-dates/ |
| Chaitra Navratri 2027 | 7–15 Apr 2027 (Pratipada → Ram Navami) | Drik Panchang https://www.drikpanchang.com/navratri/chaitra-vasant-navratri-dates.html?year=2027 |
| Sharad Navratri 2027 | 30 Sep 2027 start (Pratipada) → ~9 Oct 2027 Vijayadashami (end assumed +9 days) | ishvaram.com https://ishvaram.com/navratri-2027/ |

Mata temples flagged: Naina Devi, Chintpurni, Jwala Ji, Kangra (Brajeshwari), Chamunda, Katra (Vaishno Devi; RFID yatra registration note).
TODO next year: add Chaitra 2028 / Sharad 2028 from Drik Panchang; Shravan Ashtami melas (Naina Devi, Chintpurni) once verified.

## Weekly closed days of sights (v1.5, checked 26 Oct 2026)
The day planner never schedules these on their closed day (data: `CLOSED_DAYS` in `data/places.py`); if the stay has no other day, it warns.
| Sight | Closed | Source |
|---|---|---|
| Akshardham, Delhi | Monday | https://akshardham.com/?p=9 (visitor information: closed every Monday) |
| Viceregal Lodge (IIAS), Shimla | Monday + national holidays | https://iias.ac.in/for-tourists/ |
| Bhuri Singh Museum, Chamba | Monday + gazetted holidays | https://www.bhurisinghmuseumchamba.in/visit/ |
| Virasat-e-Khalsa, Anandpur Sahib | Monday | already in data name (closed Mondays) |
Taj Mahal Friday keeps its own warning (unchanged).

## Amarnath Yatra (added 27 Oct 2026, v1.6)
- 2026 Yatra ran 3 Jul – 28 Aug 2026 (57 days) under the Shri Amarnathji Shrine Board (SASB): https://www.freepressjournal.in/lifestyle/amarnath-yatra-2026-when-will-the-holy-pilgrimage-begin-how-to-do-advance-registration-routes-dates-timings-everything-you-need-to-know
- Registration (2026): from 15 Apr at 550+ bank branches, first-come per-route daily quota, Aadhaar biometric, permit names route + date; age 13–70; no pregnancy beyond 6 weeks; valid health certificate from an authorised institution — All India Radio News: https://www.newsonair.gov.in/advance-registration-for-amarnath-yatra-to-begin-from-april-15
- Suzu's own guide https://suzutravels.com/pilgrimage-tours/amarnath-yatra/ (checked 25 Oct 2026): 2027 dates not announced, Baltal ~14 km short & steep, Pahalgam ~32 km 3–4 days, no helicopter in 2026 (no-fly zone) → planner never promises a helicopter.
- Planner: place `baltal` (months Jul–Aug, class remote/camps), template `amarnath-baltal` (Jammu → Srinagar 1N → Baltal 2N → Srinagar 1N → Jammu). Update the 'July–August window / 2027 dates not announced' text in planner.js + i18n.js RX once SASB announces 2027 dates.

## Amarnath Yatra — Pahalgam (traditional) route (added 2026-10-28, v1.7)
- Shri Amarnathji Shrine Board, Traditional Route: https://www.jksasb.nic.in/traditional_route.html (read 28 Oct 2026) — Jammu–Pahalgam 315 km by road; Pahalgam → Chandanwari 16 km (mini buses); trek Chandanwari → Pissu Top → Sheshnag (night 2) → Mahagunas Pass 4,276 m (4.6 km climb) → Panchtarni 3,657 m (night 3) → Holy Cave; after early darshan return the same day. Planner: Pahalgam 1N, Chandanwari stop = 2 trail nights (Sheshnag, Panchtarni camps), cave darshan + walk down to Baltal (~14 km, Baltal route length) while the car goes round via Srinagar (OSRM Chandanwari–Baltal 203 km).

## Kashi – Prayagraj – Ayodhya (added 2026-10-29, v1.8)
- Places `varanasi` (hub, pilgrim_city), `prayagraj` (temple, metro class), `ayodhya` (temple, pilgrim_city); OSRM legs via `tools/patch_roads.py` (Varanasi–Prayagraj 123 km, Prayagraj–Ayodhya 167 km, Ayodhya–Varanasi 209 km).
- Drive time: OSRM gives ~84 km/h on these highways — far too fast; planner uses ×1.6 for legs touching these three (→ ~2.5 h / ~3 h / ~4 h, in line with Google Maps typical times checked 29 Oct 2026).
- Ram Mandir, Ayodhya: phones/bags/electronics not allowed inside, lockers at entry — https://www.outlooktraveller.com/News/planning-a-visit-to-the-ram-mandir-in-ayodhya-read-this-first
- Anand Bhawan, Prayagraj: open Tue–Sun (closed Mondays) — https://www.incredibleindia.gov.in/en/uttar-pradesh/prayagraj/anand-bhawan (added to CLOSED_DAYS)
- Kashi Vishwanath: phones/bags not allowed inside, lockers near gates (temple trust rule, shrikashivishwanath.org). Magh Mela at Sangam Jan–Feb (crowds, diversions).
