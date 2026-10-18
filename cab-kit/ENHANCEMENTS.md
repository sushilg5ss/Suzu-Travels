# Cab Experience Enhancer — backlog & ideas board

Owner: the **Suzu Cab Experience Enhancer** agent (15:07 IST daily). Take the FIRST unticked row, build it in the kit, test, publish (hub first), tick it with the date + what shipped. Keep the order by expected enquiries gained. Anyone may add rows at the bottom of a section; the agent re-ranks on measurement days with a one-line reason.

## Shipped (v2, 16 Oct 2026 — Claude + Sushil)
- [x] 2026-10-16 Fleet tiers Prime / Standard / Saver (age-based, +15 % / 0 / −8 %), one global switch that re-paints every price, calculator, viewer and planner
- [x] 2026-10-16 Fleet expanded 7 → 13 classes (Hycross, Fortuner, Tempo 17-seater, 26-seat mini coach, 35- and 45-seat coaches = on quote) with type + seat filters
- [x] 2026-10-16 Real-photo fleet gallery (Wikimedia Commons CC photos, credits block) with 3D tilt + "View car" viewer (specs + per-tier fares + WhatsApp)
- [x] 2026-10-16 Live route planner on the hub: any-to-any geocoding, real road route (OSRM) on a MapLibre/OpenFreeMap map, drive-through animation, distance/time, per-tier fares, WhatsApp lock-in, "Map" button on every route card

- [x] 2026-10-17 Cinematic real-footage hero film on all 30 pages (replaces the drawn HyperFrames car loops), luxury hero styling (gradient, gold rule, glass chips)

## Next up (in order)
| # | Enhancement | Why | Notes |
|---|---|---|---|
| 1 | [x] 2026-10-17 **v2 rollout to all 28 child pages** — done in the live session (REST POST from the wp-admin tab, all 29 pages byte-identical to the kit build @14035b0, Rank Math titles/descriptions pushed via `rankmath/v1/updateMeta`) | | Rollout complete: 29/29 on v2 |
| 2 | [x] 2026-10-17 **Photos for the classes still on SVG** — checked: 12/13 classes already have Commons photos; only **Force Urbania** is on SVG and Wikimedia Commons has NO Urbania photo at all (full-text + intitle search, Force-vans category: only Traveller/Citibus; Pexels/Unsplash: none). Needs Suzu's own Urbania photo from Sushil → then `media/fleet-photos/urbania.webp` + `media.json` (credit "Suzu Travels") | Realistic pictures convert better | Re-check Commons once a quarter. **18 Oct 2026: Sushil OK'd a licensed stock photo (no Urbania in the fleet yet).** Re-checked 18 Oct: Commons (search + Force Motors categories), Openverse/Flickr CC and Pexels have no Urbania photo — a free one does not exist yet; options = Sushil buys one stock licence (Alamy/Shutterstock) or a dealer/operator photo with written permission. Until then keep the SVG; never an AI render or a dealer/aggregator image without permission. |
| 3 | [~] 2026-10-17 **Planner on route pages** — built (`route_planner()` in build.py: `#live` section after Fares, fixed From/To, Car/Trip/Date/People, ⇄ Reverse, auto-plays when scrolled into view, per-tier fares, WhatsApp carries `(page: <slug> planner)`; route pages ≈117 KB). Live on hub (kit.js/css) + 8 route pages: delhi-to-manali, delhi-to-shimla, chandigarh-to-manali, chandigarh-to-shimla (17 Oct) + kalka-to-shimla, delhi-to-chandigarh, delhi-to-dehradun, delhi-to-haridwar (18 Oct). **Rollout left: 8 route pages** (delhi-to-rishikesh, delhi-to-mussoorie, dehradun-to-mussoorie, delhi-to-nainital, shimla-to-manali, delhi-to-amritsar, pathankot-to-dharamshala, jammu-to-srinagar) + 14 city/vehicle pages need only the kit.js/css sync (recipe: `wp_get_page` → save stored content → `python3 diff_ops.py <slug> <dir>` → 8 `wp_replace_in_page` ops with `expected_count` 1; only op 4 (the `#live` section) differs per page, ops 1–3 and 5–8 are identical for every route page; city/vehicle pages = kit.js/css ops only). Tick when all 31 match `out/` | The animation is the most engaging element on the site; route pages get the search traffic | 4 pages per run, newest/most-visited first |
| 4 | [ ] **Multi-stop trips in the planner** ("via Kasol", "+ Shimla") | Himachal circuits are multi-city; round-trip estimate with per-day minimum | OSRM supports multi-waypoint; show total km, days needed (250 km/day rule) |
| 5 | [ ] **Share / save the plan** (copy link with `?from=&to=&car=&tier=` that re-runs the planner on load) | Guests forward routes to family on WhatsApp — becomes a lead loop | Read `location.search` on load; no storage |
| 6 | [ ] **Pickup-point presets** (IGI T3, ISBT Kashmere Gate, Chandigarh IXC, Kalka station …) in the From datalist with coordinates in PLACES | Exact pickups = cleaner quotes | Add to `PLACES` with 3-decimal lat/lon |
| 7 | [ ] **Hill-season banner in the planner** (snow/landslide/permit note by destination and month, from the kit's tips) | Honest expectations, fewer cancellations | Data-only; no live road status claims |
| 8 | [ ] **"Which car do I need?" helper** (people + bags + hill route → recommends class + tier) | Customers ask this on every call | Pure JS, ends in WhatsApp |
| 9 | [ ] **Seat-map / luggage visual per class** in the viewer | Pictures of space beat text | Original SVG seat layouts (no third-party art) |
| 10 | [ ] **Speed pass**: inline-critical CSS trim, `content-visibility:auto` on below-fold sections, photo `srcset` | Keep PSI mobile ≥ 85 | Measure before/after |
| 11 | [ ] **Compare 2–3 cars side by side** (tick cards → sticky compare bar) | Aggregators have it; ours ties into tiers | |
| 12 | [ ] **Map labels outside India** (Islamabad/Lahore show at wide zoom on tall routes like Delhi→Manali): add a light mask polygon west of the border or bias `fitBounds` padding so the view stays over India | Sensitive for a Himachal brand | MapLibre fill layer over a hand-drawn polygon; keep boundaries hidden |
| 13 | [ ] **Hero film v2** — add one clip with a clean modern SUV/Innova on a Himachal highway (Pexels/Suzu footage), light rain/night variant for monsoon months; keep ≤ 8 MB | Sushil wants it to feel luxury | ffmpeg recipe in LOG 17 Oct |
| 14 | [ ] **Guest photo strip** (Suzu's own trip photos once Sushil shares a folder) | Trust | Only Suzu-owned images |

## Ideas parked (need Sushil)
- Online token payment from the planner (Razorpay link) — Sushil decides when the booking engine (Trip Planner kit) is ready.
- Driver live-tracking page — driver details stay private per policy; only after booking, outside the website.
- Paid routing/map tier (MapTiler / OpenRouteService / Stadia) if free fair-use limits are hit.
