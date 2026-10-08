# Mountain section backlog

**Owner:** the Suzu Mountain agents. **Order:** top to bottom, one page per day (Page Builder).

The rank weighs four things: search demand (Keyword Planner, 1 Oct 2026), Himachal / lead value, how hard it is to rank, and cluster support. The Research agent may re-rank rows **below the first 3 non-live rows**, but only with keyword evidence, noted in LOG.md.

**Status flow:**
1. `todo`
2. `researched`: Research wrote `research/pages/<slug>.md`.
3. `media`: Visual Studio pinned the renders; `src/media/<slug>.json` exists.
4. `live YYYY-MM-DD`: Page Builder published it and added it to live.json.

**Rules:**
- A status is changed only by the agent that did the step, with `git pull --rebase` first.
- **Sell? = yes:** Himachal peaks Suzu can arrange with registered Himachal outfitters (`commercial: true`).
- **Sell? = no:** information only; the CTA suggests Himachal climbs.
- **Sell? = hold:** status must be verified first.
- **Paths:** every page lives at `/mountains-of-india/<slug>/`, WordPress parent 11831.
- **Titles:** the SEO title never promises a price ("Get Quote" pages), so no "Cost" in titles.

| # | Status | Slug (URL) | Kind | Data key | Focus keyword (monthly searches) | SEO title (≤ 60) | Sell? | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | live 2026-10-01 | `friendship-peak` | peak | peak_id friendship-peak | friendship peak (6,600 + trek 1,900) | Friendship Peak Manali (5,289 m): Route, Itinerary & Season | yes | Top commercial page. Solang–Bakarthach–Lady Leg route; profile video. |
| 2 | live 2026-10-01 | `himachal-pradesh` | state | state himachal-pradesh | peaks in himachal pradesh (1,900) | Highest Peaks in Himachal Pradesh: List & Climbing Guide | yes | Table where state=himachal-pradesh; ladder of 5–7 HP peaks; links every HP peak page. |
| 3 | live 2026-10-03 | `hanuman-tibba` | peak | peak_id hanuman-tibba | hanuman tibba (2,900) | Hanuman Tibba (5,982 m): Route, Grade & Expedition Guide | yes | Height quoted 5,860–5,982 m: state the range once. |
| 4 | live 2026-10-04 | `stok-kangri` | peak | peak_id stok-kangri | stok kangri (2,900; intl 480) | Stok Kangri 2026: Is It Open? Status & Best Alternatives | no | CLOSED since 2020 — never sell it. Funnel to Yunam, Friendship Peak, Kang Yatse. |
| 5 | live 2026-10-05 | `deo-tibba` | peak | peak_id deo-tibba | deo tibba (1,300) | Deo Tibba (6,001 m): Expedition Route, Itinerary & Season | yes | Jagatsukh–Chika–Seri–Duhangan Col route; profile video. |
| 6 | live 2026-10-05 | `yunam-peak` | peak | peak_id mount-yunam | yunam peak (1,600) | Yunam Peak (6,111 m): Route, Itinerary & Best Season | yes | Easiest 6,000er angle; Bharatpur / Baralacha La base. |
| 7 | live 2026-10-06 | `imf-permit-fees` | guide | - | indian mountaineering foundation fees (170 ww / 90 intl; 'imf permit' variants = no volume, 3 Oct) | IMF Climbing Permit & Peak Fees in India (USD Guide) | yes | Words hero. Fees in USD are information (allowed). No Suzu prices. |
| 8 | live 2026-10-07 | `trekking-peaks` | guide | table ids (beginner peaks) | trekking peaks (590 ww / 480 IN / 70 intl; 'trekking peaks india' = no volume, 5 Oct) | Trekking Peaks in India: Best First 5,000–6,000 m Climbs | yes | Compare Friendship, Shitidhar, Ladakhi, Yunam, Kanamo*, Mentok Kangri; ladder. |
| 9 | live 2026-10-08 | `mountaineering-courses` | guide | - | mountaineering course india (1,600 ww / 1,600 IN; + basic mountaineering course 2,900, 5 Oct) | Mountaineering Courses in India: Basic & Advanced (2026) | no | ABVIMAS, NIM, HMI, JIM&WS, NIMAS — link each official site; no fees unless official and dated. |
| 10 | media | `mountaineering-gear-list` | guide | - | mountaineering gear list (260 ww / 30 IN / 140 intl; heads 'mountaineering gear' 27.1K / 'equipment' 74K are shopping SERPs — secondary only, 5 Oct) | Mountaineering Gear List for Indian Peaks: What to Pack | yes | Full kit explained: what the outfitter provides (rope, tents, group gear) vs what you bring; rental options in Manali/Solang mentioned generically. NO brand names, NO prices (kit rule). Words hero; use the gear/boots photos in hf/photos (px-37016841 boots + crampons added 6 Oct). |
| 11 | media | `crampons-and-mountaineering-boots` | guide | - | what are crampons (1,900 ww / 90 IN / 1,600 intl, LOW comp; heads 'crampons' 165K & 'mountaineering boots' 14.8K are shopping SERPs — secondary, 7 Oct) | Crampons & Mountaineering Boots: A Beginner's Guide | yes | What crampons are, how they grip, B1/B2/B3 boot–crampon matching, snow boots vs trekking shoes, fit and care; where climbers rent them for Himachal climbs. szm-tbl for the B1–B3 matrix. |
| 12 | media | `ice-axe-guide` | guide | - | ice axe (27,100 ww / 1,900 IN / 14,800 intl; + self arrest 880, 7 Oct) | Ice Axe Guide: Parts, Types & How Climbers Use It | yes | Parts, walking vs technical axes, sizing, how it is carried/used on Indian snow peaks; self-arrest described at concept level with a safety note (guides teach it at base camp — funnel to guided climbs). |
| 13 | media | `what-to-wear-himalayan-climb` | guide | - | layering system (720 ww / 320 intl, LOW comp; + layering for hiking 1,000; 'what to wear in manali in winter' only 10 IN, 7 Oct) | What to Wear on a Himalayan Climb: The Layering System | yes | Base / mid / shell 3-layer system, summit-day wear, hands-head-feet, what winter Manali visitors need vs climbers; rentals mentioned generically. Words hero (LAYER / SMART etc.). |
| 14 | todo | `expedition-camping` | guide | - | camping in himachal (390 IN) + expedition camp life | Expedition Camping: Base Camp to Summit Camp Explained | yes | How camps work on a climb: tents, sleeping-bag ratings, mats, kitchen/mess, water, toilets, leave-no-trace; links Friendship Peak & Deo Tibba camp tables. |
| 15 | todo | `altitude-sickness` | guide | - | altitude sickness himalayas / AMS | Altitude Sickness on Indian Peaks: Signs, Prevention & Rules | no | Promoted from Later ideas. CDC Yellow Book as source; include the 'informational, not medical advice' line; acclimatisation schedules from live itineraries. |
| 16 | todo | `first-6000m-peak` | guide | - | easiest 6000m peak / first 6000er (long-tail + AEO) | How to Climb Your First 6,000 m Peak in India | yes | Promoted from Later ideas. Fitness prep, course-or-no-course, gear link, peak ladder Yunam/Friendship/Shitidhar; the strongest commercial funnel of the guide set. |
| 17 | todo | `7000m-peaks` | band | band 7000 | 7000m peaks india | 7000m Peaks in India: Complete List & Climbing Status | no | Table band=7000; ladder of 7 seven-thousanders. |
| 18 | todo | `mountaineering-in-india` | guide | - | mountaineering in india (14,800 shared) | Mountaineering in India: Guide for Foreign Climbers | yes | Owns 'how to climb / foreigners'; must not target 'mountains in india' (hub). |
| 19 | todo | `reo-purgyil` | peak | peak_id reo-purgyil | reo purgyil (1,900) | Reo Purgyil (6,816 m): Highest Peak of Himachal Pradesh | yes | Border belt: protected-area permit for foreigners. |
| 20 | todo | `nanda-devi` | peak | peak_id nanda-devi | nanda devi (49,500) | Nanda Devi (7,816 m): Facts, History & Climbing Status | no | CLOSED since 1983; only Nanda Devi East is on the 2026 list. |
| 21 | todo | `kangchenjunga` | peak | peak_id kangchenjunga | kangchenjunga (40,500) | Kangchenjunga from India: Facts, Views & Climbing Status | no | Banned from Sikkim (70/HOME/2001). px-30701907 is a verified photo. |
| 22 | todo | `6000m-peaks` | band | band 6000 | 6000m peaks india | 6000m Peaks in India: List by State, Grade & Season | no | Table band=6000; ladder. |
| 23 | todo | `kanamo-peak` | peak | peak_id kanamo | kanamo peak (1,300) | Kanamo Peak (5,964 m), Spiti: Status, Route & Season | hold | Access status conflicting (banned vs reopened): verify with 2026 local/official sources first; if unclear say so and sell alternatives. |
| 24 | todo | `chau-chau-kang-nilda` | peak | peak_id chau-chau-kang-nilda | chau chau kang nilda (170) | Chau Chau Kang Nilda (6,303 m), Spiti: Expedition Guide | yes | Spiti, Kaza base. |
| 25 | todo | `unclimbed-peaks` | guide | table status=unclimbed (+ closed/restricted) | unclimbed peaks india | Unclimbed Peaks in India: Virgin & Closed Summits List | no | Data + editorial; Kangto first ascent late 2025. |
| 26 | todo | `records` | guide | - | mountaineering records india | Indian Himalaya Climbing Records & First Ascents Timeline | no | Trisul 1907 was the first 7,000 m summit (not Kamet). |
| 27 | todo | `satopanth` | peak | peak_id satopanth | satopanth (1,900) | Satopanth (7,075 m): Expedition Guide & Climbing History | no | Uttarakhand; on the 2026 opened list? verify. |
| 28 | todo | `shivling-peak` | peak | peak_id shivling | shivling peak (2,400) | Shivling Peak (6,543 m): Routes, Grade & Climbing History | no | Gangotri; 'Matterhorn of the Himalaya'. |
| 29 | todo | `mulkila` | peak | peak_id mulkila | mulkila | Mulkila (6,517 m), Lahaul: Route & Expedition Guide | yes | Highest in Lahaul; Milang valley. |
| 30 | todo | `indrasan` | peak | peak_id indrasan | indrasan | Indrasan (6,220 m): Route, Grade & Climbing History | yes | Experts only — hardest in the Pir Panjal. |
| 31 | todo | `kang-yatse` | peak | peak_id kang-yatse-i (+ add Kang Yatse II via additions.json) | kang yatse (1,300) | Kang Yatse I & II, Ladakh: Climbing Guide & Season | no | Ladakh — informational; CTA suggests Himachal alternatives. |
| 32 | todo | `kamet` | peak | peak_id kamet | kamet mountain (27,100 incl. whisky) | Kamet (7,756 m): History, Route & Climbing Guide | no | 1931 first ascent: first summit above 25,000 ft — NOT the first 7,000 m summit. |
| 33 | todo | `changabang` | peak | peak_id changabang | changabang (1,000) | Changabang (6,864 m): The Granite Fang of Garhwal | no | 1974 first ascent; 1976 West Wall. |
| 34 | todo | `uttarakhand` | state | state uttarakhand | highest peak in uttarakhand | Highest Peaks in Uttarakhand: List & Climbing Guide | no | Table state=uttarakhand; 83 peaks opened Feb 2026 (UKMPS). |
| 35 | todo | `ladakh` | state | state ladakh | highest peak in ladakh | Highest Peaks in Ladakh: List & Climbing Guide | no | Siachen peaks restricted; Stok Kangri closed. |
| 36 | todo | `trisul` | peak | peak_id trisul-i | trishul peak / trisul | Trisul (7,120 m): The First 7,000 m Summit Ever Climbed | no | 1907, Longstaff; 'trishul' volume is mostly the symbol — target 'trishul peak/parvat'. |
| 37 | todo | `highest-peak-in-every-state` | guide | - | highest peak in each state of india | Highest Peak in Every Indian State & UT (Full List) | no | Needs a verified table of every state/UT high point (incl. Anamudi, Doddabetta…) in extra_sections. |
| 38 | todo | `sikkim` | state | state sikkim | highest peak in sikkim | Highest Peaks in Sikkim: List, Status & Viewpoints | no | Sacred peaks; viewpoints (Goecha La, Sandakphu). |
| 39 | todo | `jammu-kashmir` | state | state jammu-kashmir | highest peak in jammu and kashmir | Highest Peaks in Jammu & Kashmir: List & Climbing Guide | no | Nun is counted under J&K. |
| 40 | todo | `arunachal-pradesh` | state | state arunachal-pradesh | highest peak in arunachal pradesh | Highest Peaks in Arunachal Pradesh: Kangto & More | no | Kangto first recorded ascent late 2025. |
| 41 | todo | `menthosa` | peak | peak_id menthosa | menthosa | Menthosa (6,443 m), Lahaul: Expedition Guide | yes | Miyar valley. |
| 42 | todo | `manirang` | peak | peak_id manirang | manirang | Manirang (6,593 m), Spiti: Route & Expedition Guide | yes | PAP for foreigners. |
| 43 | todo | `hardest-peaks-in-india` | guide | - | hardest mountains to climb in india | Hardest Peaks to Climb in India: Changabang to Meru | no | Piolet d'Or lines; from the hub's 'hardest' section, expanded. |
| 44 | todo | `best-time-for-mountaineering-in-india` | guide | - | best time for mountaineering in india | Best Time for Mountaineering in India: Season by Region | yes | Region-by-region months; monsoon; rain-shadow. |
| 45 | todo | `3000m-4000m-summits` | band | bands 3000+4000 (table min_m 3000 max_m 4999) | easy himalayan summits | Easy Himalayan Summits in India (3,000–4,999 m) | no | Churdhar, Kedarkantha, Chandrashila, Sandakphu, Pangarchulla… |

## Later ideas (add rows when the list above is nearly done)
- Winter treks in India guide (winter trek in india 1,000 IN; "kedarkantha trek" alone 49.5K IN — informational, would funnel to Himachal winter climbs & Adventure pages; coordinate with the Adventure squad lane before writing).
- Mountaineering glossary A–Z (col, serac, bergschrund, moraine…) — AEO/definition queries, internal-link hub.
- Other high peaks with search demand:
  - Bhagirathi group, Thalay Sagar, Meru, Chaukhamba, Nun Kun, Saser Kangri, Mentok Kangri, Shilla.
  - Papsura and CB-13 (add to the dataset first).
- "Women mountaineers of India" (records), and "Indian Everest summiteers from Himachal". These are verified facts only: see the facts-to-avoid list.
- Comparison pages:
  - "Friendship Peak vs Yunam"
  - "Stok Kangri alternatives"
  - "Deo Tibba vs Hanuman Tibba"
