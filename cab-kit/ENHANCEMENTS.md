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
| 2 | [ ] **Photos for the classes still on SVG** | Realistic pictures convert better; customers don't know what an Urbania or Hycross looks like | Commons: Force Urbania, Maruti Swift/WagonR, Dzire, Ertiga, Fortuner; if none under a free licence, ask Sushil for Suzu's own car photos (report) |
| 3 | [ ] **Planner on route pages** (compact: map + fares for that route only, auto-plays on scroll) | The animation is the most engaging element on the site; route pages get the search traffic | Reuse `planner()` with fixed From/To, no form; keep page ≤ 130 KB |
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
