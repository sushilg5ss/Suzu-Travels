# Trip Planner backlog (top = next). Tick with `done YYYY-MM-DD` + one LOG line.

## Phase 1 — go live at /plan-your-trip/ (week 1)
1. [x] done 2026-10-15 (live SHA 873f29f3c6f26826; real test lead skipped — send one only if leads look missing) **Deploy v0.1** to `public_html/plan-your-trip/index.html` (new folder). Verify 200, test live (stubbed lead), then ONE real test lead named "TEST Claude Trip Planner (ignore)" and confirm it reached the lead inbox / info@ email. Add Rank Math-independent sitemap note in LOG (static page: ask GSC URL inspection is human-only → "Sushil ke liye").
2. [ ] **Rate audit** — research 2026 hotel rates (MakeMyTrip/Agoda/Booking public listings, 3 dates) for the 7 classes and the 12 most-used places; cab rates already = /cabs/ engine. Write `research/rates-sources.md` (dated rows + URLs); move `rates.json` only if the estimate is BELOW market (it must stay on the higher side).
3. [ ] **Entry points (outside the homepage)**: ask the Design agent via hand-off board for a "Plan your trip" link in menus; on WordPress hub pages (`/himachal-tour-packages/`, `/cabs/`, `/destinations/`, pilgrimage hub) add ONE contextual link each (Royal MCP, non-Elementor pages only, check `_elementor_edit_mode`).
4. [ ] **Hindi UI toggle** (EN / हिं) for labels, day-plan sentences and PDF.
5. [ ] **Split data**: lazy-load road geometry (`/plan-your-trip/roads.json`) after first paint; target < 150 KB first load, LCP < 2.0 s mobile. Lighthouse before/after in LOG.

## Phase 2 — homepage booking engine (LIVE 15 Oct 2026) — now: improve it
- [ ] Measure homepage Lighthouse mobile/desktop after the swap (before: mobile 84 / desktop 90) and fix any regression (LCP image size, CLS of the card).
- [ ] Card UX: recent searches chip, auto-suggest by season, 'Plan with Suzu assistant' link, Hindi labels.
- [ ] iOS Safari: check PDF/print inside the overlay iframe; if it fails, open /plan-your-trip/#t=… in a new tab for PDF.
6. [x] done 2026-10-15 (live 065caa4b, see LOG) Build `#tp-engine` hero (MakeMyTrip-style search card: Holiday planner · Yatra & Mata darshan · Cabs · Hotels) for the static homepage, deep-linking to `/plan-your-trip/#t=…`. Rules in `agents/developer.md` §Homepage. Ship only after /plan-your-trip/ has been live and green for 2 runs.
7. [~] 2026-10-15: light photo crossfade shipped instead of video (Sushil: no video in hero). Optional later: a tiny CSS/SVG motion layer only if Lighthouse stays green. Lightweight HyperFrames loop (≤ 1.5 MB phone / 2.5 MB desktop, poster first) as the engine's background — snow, roads, temples — instead of the 11-scene film; or a pure CSS/SVG animated mountain scene if speed suffers.

## Phase 3 — make it the best planner in India
8. [ ] More places: Kerala, Goa, Rajasthan, Sikkim/North-East (fly-in circuits; hotel-only + local car), Amarnath, Kainchi Dham, Adi Kailash. Re-run `tools/fetch_roads.py`.
9. [ ] Smarter day plans: opening hours/closed days of sights, Navratri crowd notes, sunrise/sunset slots, snow-season "Atal Tunnel only" logic for Rohtang, Kedarnath 2-night rule enforced.
10. [ ] Hotel-name suggestions per class (no prices, "or similar"), photos from Suzu's own media only.
11. [ ] "Compare 2 plans" and "Budget slider → auto-pick tier/car".
12. [ ] HyperFrames: render a shareable 15-s "trip film" of a plan (route + day titles) server-side later; for now an in-page animated preview.
13. [ ] Agent portal polish: agency logo upload (kept in the browser only, never uploaded), GST invoice note, B2B rate card request button.
14. [ ] Suzu Assistant hand-off: when a chat mentions a route, offer "Open in Trip Planner" (coordinate via hand-off board — the assistant file is not ours).
15. [ ] Structured data: FAQPage for the FAQ block; WebApplication already present.
