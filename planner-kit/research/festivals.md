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
