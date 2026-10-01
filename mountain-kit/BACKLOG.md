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
| 2 | researched | `himachal-pradesh` | state | state himachal-pradesh | peaks in himachal pradesh (1,900) | Highest Peaks in Himachal Pradesh: List & Climbing Guide | yes | Table where state=himachal-pradesh; ladder of 5–7 HP peaks; links every HP peak page. |
| 3 | researched | `hanuman-tibba` | peak | peak_id hanuman-tibba | hanuman tibba (2,900) | Hanuman Tibba (5,982 m): Route, Grade & Expedition Guide | yes | Height quoted 5,860–5,982 m: state the range once. |
| 4 | researched | `stok-kangri` | peak | peak_id stok-kangri | stok kangri (2,900; intl 480) | Stok Kangri 2026: Is It Open? Status & Best Alternatives | no | CLOSED since 2020 — never sell it. Funnel to Yunam, Friendship Peak, Kang Yatse. |
| 5 | todo | `deo-tibba` | peak | peak_id deo-tibba | deo tibba (1,300) | Deo Tibba (6,001 m): Expedition Route, Itinerary & Season | yes | Jagatsukh–Chika–Seri–Duhangan Col route; profile video. |
| 6 | todo | `yunam-peak` | peak | peak_id mount-yunam | yunam peak (1,600) | Yunam Peak (6,111 m): Route, Itinerary & Best Season | yes | Easiest 6,000er angle; Bharatpur / Baralacha La base. |
| 7 | todo | `imf-permit-fees` | guide | - | imf permit / peak fees india | IMF Climbing Permit & Peak Fees in India (USD Guide) | yes | Words hero. Fees in USD are information (allowed). No Suzu prices. |
| 8 | todo | `trekking-peaks` | guide | table ids (beginner peaks) | trekking peaks india | Trekking Peaks in India: Best First 5,000–6,000 m Climbs | yes | Compare Friendship, Shitidhar, Ladakhi, Yunam, Kanamo*, Mentok Kangri; ladder. |
| 9 | todo | `mountaineering-courses` | guide | - | mountaineering course india (1,600) | Mountaineering Courses in India: Basic & Advanced (2026) | no | ABVIMAS, NIM, HMI, JIM&WS, NIMAS — link each official site; no fees unless official and dated. |
| 10 | todo | `7000m-peaks` | band | band 7000 | 7000m peaks india | 7000m Peaks in India: Complete List & Climbing Status | no | Table band=7000; ladder of 7 seven-thousanders. |
| 11 | todo | `mountaineering-in-india` | guide | - | mountaineering in india (14,800 shared) | Mountaineering in India: Guide for Foreign Climbers | yes | Owns 'how to climb / foreigners'; must not target 'mountains in india' (hub). |
| 12 | todo | `reo-purgyil` | peak | peak_id reo-purgyil | reo purgyil (1,900) | Reo Purgyil (6,816 m): Highest Peak of Himachal Pradesh | yes | Border belt: protected-area permit for foreigners. |
| 13 | todo | `nanda-devi` | peak | peak_id nanda-devi | nanda devi (49,500) | Nanda Devi (7,816 m): Facts, History & Climbing Status | no | CLOSED since 1983; only Nanda Devi East is on the 2026 list. |
| 14 | todo | `kangchenjunga` | peak | peak_id kangchenjunga | kangchenjunga (40,500) | Kangchenjunga from India: Facts, Views & Climbing Status | no | Banned from Sikkim (70/HOME/2001). px-30701907 is a verified photo. |
| 15 | todo | `6000m-peaks` | band | band 6000 | 6000m peaks india | 6000m Peaks in India: List by State, Grade & Season | no | Table band=6000; ladder. |
| 16 | todo | `kanamo-peak` | peak | peak_id kanamo | kanamo peak (1,300) | Kanamo Peak (5,964 m), Spiti: Status, Route & Season | hold | Access status conflicting (banned vs reopened): verify with 2026 local/official sources first; if unclear say so and sell alternatives. |
| 17 | todo | `chau-chau-kang-nilda` | peak | peak_id chau-chau-kang-nilda | chau chau kang nilda (170) | Chau Chau Kang Nilda (6,303 m), Spiti: Expedition Guide | yes | Spiti, Kaza base. |
| 18 | todo | `unclimbed-peaks` | guide | table status=unclimbed (+ closed/restricted) | unclimbed peaks india | Unclimbed Peaks in India: Virgin & Closed Summits List | no | Data + editorial; Kangto first ascent late 2025. |
| 19 | todo | `records` | guide | - | mountaineering records india | Indian Himalaya Climbing Records & First Ascents Timeline | no | Trisul 1907 was the first 7,000 m summit (not Kamet). |
| 20 | todo | `satopanth` | peak | peak_id satopanth | satopanth (1,900) | Satopanth (7,075 m): Expedition Guide & Climbing History | no | Uttarakhand; on the 2026 opened list? verify. |
| 21 | todo | `shivling-peak` | peak | peak_id shivling | shivling peak (2,400) | Shivling Peak (6,543 m): Routes, Grade & Climbing History | no | Gangotri; 'Matterhorn of the Himalaya'. |
| 22 | todo | `mulkila` | peak | peak_id mulkila | mulkila | Mulkila (6,517 m), Lahaul: Route & Expedition Guide | yes | Highest in Lahaul; Milang valley. |
| 23 | todo | `indrasan` | peak | peak_id indrasan | indrasan | Indrasan (6,220 m): Route, Grade & Climbing History | yes | Experts only — hardest in the Pir Panjal. |
| 24 | todo | `kang-yatse` | peak | peak_id kang-yatse-i (+ add Kang Yatse II via additions.json) | kang yatse (1,300) | Kang Yatse I & II, Ladakh: Climbing Guide & Season | no | Ladakh — informational; CTA suggests Himachal alternatives. |
| 25 | todo | `kamet` | peak | peak_id kamet | kamet mountain (27,100 incl. whisky) | Kamet (7,756 m): History, Route & Climbing Guide | no | 1931 first ascent: first summit above 25,000 ft — NOT the first 7,000 m summit. |
| 26 | todo | `changabang` | peak | peak_id changabang | changabang (1,000) | Changabang (6,864 m): The Granite Fang of Garhwal | no | 1974 first ascent; 1976 West Wall. |
| 27 | todo | `uttarakhand` | state | state uttarakhand | highest peak in uttarakhand | Highest Peaks in Uttarakhand: List & Climbing Guide | no | Table state=uttarakhand; 83 peaks opened Feb 2026 (UKMPS). |
| 28 | todo | `ladakh` | state | state ladakh | highest peak in ladakh | Highest Peaks in Ladakh: List & Climbing Guide | no | Siachen peaks restricted; Stok Kangri closed. |
| 29 | todo | `trisul` | peak | peak_id trisul-i | trishul peak / trisul | Trisul (7,120 m): The First 7,000 m Summit Ever Climbed | no | 1907, Longstaff; 'trishul' volume is mostly the symbol — target 'trishul peak/parvat'. |
| 30 | todo | `highest-peak-in-every-state` | guide | - | highest peak in each state of india | Highest Peak in Every Indian State & UT (Full List) | no | Needs a verified table of every state/UT high point (incl. Anamudi, Doddabetta…) in extra_sections. |
| 31 | todo | `sikkim` | state | state sikkim | highest peak in sikkim | Highest Peaks in Sikkim: List, Status & Viewpoints | no | Sacred peaks; viewpoints (Goecha La, Sandakphu). |
| 32 | todo | `jammu-kashmir` | state | state jammu-kashmir | highest peak in jammu and kashmir | Highest Peaks in Jammu & Kashmir: List & Climbing Guide | no | Nun is counted under J&K. |
| 33 | todo | `arunachal-pradesh` | state | state arunachal-pradesh | highest peak in arunachal pradesh | Highest Peaks in Arunachal Pradesh: Kangto & More | no | Kangto first recorded ascent late 2025. |
| 34 | todo | `menthosa` | peak | peak_id menthosa | menthosa | Menthosa (6,443 m), Lahaul: Expedition Guide | yes | Miyar valley. |
| 35 | todo | `manirang` | peak | peak_id manirang | manirang | Manirang (6,593 m), Spiti: Route & Expedition Guide | yes | PAP for foreigners. |
| 36 | todo | `hardest-peaks-in-india` | guide | - | hardest mountains to climb in india | Hardest Peaks to Climb in India: Changabang to Meru | no | Piolet d'Or lines; from the hub's 'hardest' section, expanded. |
| 37 | todo | `best-time-for-mountaineering-in-india` | guide | - | best time for mountaineering in india | Best Time for Mountaineering in India: Season by Region | yes | Region-by-region months; monsoon; rain-shadow. |
| 38 | todo | `3000m-4000m-summits` | band | bands 3000+4000 (table min_m 3000 max_m 4999) | easy himalayan summits | Easy Himalayan Summits in India (3,000–4,999 m) | no | Churdhar, Kedarkantha, Chandrashila, Sandakphu, Pangarchulla… |

## Later ideas (add rows when the list above is nearly done)
- Other high peaks with search demand:
  - Bhagirathi group, Thalay Sagar, Meru, Chaukhamba, Nun Kun, Saser Kangri, Mentok Kangri, Shilla.
  - Papsura and CB-13 (add to the dataset first).
- "How to climb your first 6,000 m peak" (a guide that funnels to Yunam and Friendship Peak).
- "Altitude sickness on Indian peaks" (cite the CDC, and add the "not medical advice" line).
- "Mountaineering gear checklist" (no brand promotion).
- "Women mountaineers of India" (records), and "Indian Everest summiteers from Himachal". These are verified facts only: see the facts-to-avoid list.
- Comparison pages:
  - "Friendship Peak vs Yunam"
  - "Stok Kangri alternatives"
  - "Deo Tibba vs Hanuman Tibba"
