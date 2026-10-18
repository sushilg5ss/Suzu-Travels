# Trip Planner backlog (top = next). Tick with `done YYYY-MM-DD` + one LOG line.

## Phase 0 — deploy pending
000. [x] done 2026-10-16 18:40 (live acb9460c, includes engine sync 2026-10-16b) **Deploy homepage release** `homepage/releases/2026-10-16/` (hero motion pause).
00. [x] done 2026-10-16 18:05 (live dfbcaaa77cf38e3b + roads-geo 0eabc86d) **Deploy v0.5** (supersedes v0.4; TWO files: index.html + roads-geo.json) (rate audit; release in Project `claude/trip-planner/releases/2026-10-16/`) — Chrome tools absent on 16 Oct run.
0. [x] done 2026-10-16 (live = 4c765ffa, uploaded during the 16 Oct ops sweep / by Sushil) **Deploy v0.3** (dist 4c765ffa28e2b0a9, release in Project `claude/trip-planner/releases/2026-10-15/`) — Chrome tools were absent on 15 Oct 11:53 run. Rebuild from branch if newer.

0000. [ ] **Deploy v0.7** (supersedes v0.6) — upload `dist/plan-your-trip/index.html` only (c44eee3f24b2a743; roads-geo.json unchanged); backup index-previous.html = dfbcaaa7 first. Homepage card needs no re-sync (no hotel-class data in tpe-data).

## Phase 1 — go live at /plan-your-trip/ (week 1)
1. [x] done 2026-10-15 (live SHA 873f29f3c6f26826; real test lead skipped — send one only if leads look missing) **Deploy v0.1** to `public_html/plan-your-trip/index.html` (new folder). Verify 200, test live (stubbed lead), then ONE real test lead named "TEST Claude Trip Planner (ignore)" and confirm it reached the lead inbox / info@ email. Add Rank Math-independent sitemap note in LOG (static page: ask GSC URL inspection is human-only → "Sushil ke liye").
2. [~] 2026-10-18: audit #2 done (Gulmarg, Pahalgam, Jaipur, Udaipur, Delhi, Amritsar, Kangra, Kaza, Nubra) → new kashmir_resort 6,800, kashmir 5,000, rajasthan 4,100, metro 3,500, pilgrim 2,750, ladakh 4,300 = v0.7. Next: Srinagar/Jaipur re-check, small Mata towns, Char Dham towns, Rajasthan Oct–Mar peak. 2026-10-16: audit #1 done (Manali, Shimla, Dharamshala, Kasol, Katra, Haridwar, Srinagar, Leh; 2 dates) → hill_premium 3,800, hill 3,200, new pilgrim_city 4,000, kashmir 4,400 = v0.4. Next: metro, remote, small temple towns, Gulmarg/Pahalgam, Nubra. **Rate audit** — research 2026 hotel rates (MakeMyTrip/Agoda/Booking public listings, 3 dates) for the 7 classes and the 12 most-used places; cab rates already = /cabs/ engine. Write `research/rates-sources.md` (dated rows + URLs); move `rates.json` only if the estimate is BELOW market (it must stay on the higher side).
3. [~] 2026-10-15: /himachal-tour-packages/ link done (page 1087); next /cabs/, /destinations/, pilgrimage hub, menu via Design agent. **Entry points (outside the homepage)**: ask the Design agent via hand-off board for a "Plan your trip" link in menus; on WordPress hub pages (`/himachal-tour-packages/`, `/cabs/`, `/destinations/`, pilgrimage hub) add ONE contextual link each (Royal MCP, non-Elementor pages only, check `_elementor_edit_mode`).
4. [ ] **Hindi UI toggle** (EN / हिं) for labels, day-plan sentences and PDF.
5. [x] done 2026-10-16 (v0.5: roads-geo.json lazy; index 701→239 KB, gzip 206→81 KB; Lighthouse pending after deploy) **Split data**: lazy-load road geometry (`/plan-your-trip/roads.json`) after first paint; target < 150 KB first load, LCP < 2.0 s mobile. Lighthouse before/after in LOG.

## Phase 2 — homepage booking engine (LIVE 15 Oct 2026) — now: improve it
- [ ] Measure homepage Lighthouse mobile/desktop after the swap (before: mobile 84 / desktop 90) and fix any regression (LCP image size, CLS of the card).
- [~] 2026-10-16: data synced to v0.5 + dropdown overlap fixed (`homepage/sync_engine.py` — re-run after every places/templates change). Open: recent searches chip, auto-suggest by season, 'Plan with Suzu assistant' link, Hindi labels.
- [x] done 2026-10-16 (v0.5: iOS in embed opens ?pdf=1#t=… in a new tab; verify on a real iPhone after deploy) iOS Safari PDF inside the overlay iframe.
6. [x] done 2026-10-15 (live 065caa4b, see LOG) Build `#tp-engine` hero (MakeMyTrip-style search card: Holiday planner · Yatra & Mata darshan · Cabs · Hotels) for the static homepage, deep-linking to `/plan-your-trip/#t=…`. Rules in `agents/developer.md` §Homepage. Ship only after /plan-your-trip/ has been live and green for 2 runs.
7. [~] 2026-10-15: light photo crossfade shipped instead of video (Sushil: no video in hero). Optional later: a tiny CSS/SVG motion layer only if Lighthouse stays green. Lightweight HyperFrames loop (≤ 1.5 MB phone / 2.5 MB desktop, poster first) as the engine's background — snow, roads, temples — instead of the 11-scene film; or a pure CSS/SVG animated mountain scene if speed suffers.

## Phase 3 — make it the best planner in India
8. [~] 2026-10-16: Rajasthan (11), Agra/Mathura, Kumaon/Garhwal (11), Himachal extras (5), Patnitop, Lamayuru, Tso Moriri, Kainchi Dham, Anandpur Sahib done (v0.5, 87 places). Open: Kerala, Goa, Sikkim/North-East (fly-in circuits; hotel-only + local car), Amarnath, Adi Kailash, Varanasi. Re-run `tools/fetch_roads.py`.
9. [~] 2026-10-17: Navratri crowd note for Mata temples (v0.6, dates to Oct 2027 — add 2028 next year). 2026-10-15: Rohtang winter skip + Kedarnath 2-night warning built (v0.3). Rest open: Smarter day plans: opening hours/closed days of sights, Navratri crowd notes, sunrise/sunset slots, snow-season "Atal Tunnel only" logic for Rohtang, Kedarnath 2-night rule enforced.
10. [ ] Hotel-name suggestions per class (no prices, "or similar"), photos from Suzu's own media only.
11. [ ] "Compare 2 plans" and "Budget slider → auto-pick tier/car".
12. [ ] HyperFrames: render a shareable 15-s "trip film" of a plan (route + day titles) server-side later; for now an in-page animated preview.
13. [ ] Agent portal polish: agency logo upload (kept in the browser only, never uploaded), GST invoice note, B2B rate card request button.
14. [ ] Suzu Assistant hand-off: when a chat mentions a route, offer "Open in Trip Planner" (coordinate via hand-off board — the assistant file is not ours).
15. [x] done 2026-10-15 (v0.3 build; live after deploy) Structured data: FAQPage for the FAQ block; WebApplication already present.
