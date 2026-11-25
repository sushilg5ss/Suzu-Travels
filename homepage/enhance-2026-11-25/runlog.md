# Homepage Enhancement Agent — 25 Nov 2026 night run

## Summary
- **Live base:** `ae7940bc…426e` (1,071,727 B) = last night's 24n release, unchanged since (no other agent touched index.html today). Built on the live file.
- **Deploy: LIVE** — deploy-static `2026-11-25n-homepage`, status `deployed` 17:56:29 UTC (23:26 IST), attempt 1, exit 0. Plain + `?nc` fetch SHA = after. Server backup `index-nz-previous.html` = ae7940bc (verified).
- **New tonight:**
  1. **One shared weather-feed request instead of five separate ones** (last night's idea 2, roadmap 1 speed). Five blocks read `/suzu-weather-feed.json`: the nzw marquee (on load, `?h=<UTC hour>`), Snow tile line (nz-xp-live), Himachal-vs-Kashmir weather (nz-hk-wx), region weather (nz-rwx) and the trip sheet's "Weather on this route" (nature JS). Each fetched on its own (the lazy ones with a plain URL, so no HTTP-cache sharing with nzw).
     - New `<script id="nz-wxf-js">` (placed just before nz-hk-wx-js) defines `window.nzWxFeed()`: one memoised fetch of the same URL nzw used (`?h=` hour key, `cache:'default'`), 20-min memo (nzw's 30-min refresh still re-fetches), memo cleared on error so callers can retry.
     - The four nz callers now call `window.nzWxFeed()`; nzw-js calls it too with its own old fetch kept as fallback (`window.nzWxFeed ? … : fetch(…)`), and its `/suzu-weather.php` fallback + 6 h stale check are unchanged. No other logic touched.
     - Measured (Playwright, full scroll + Book Now + open sheet): weather-feed requests per page view **3 → 1** on both 1440 and Pixel 7 (before: `?h=…` + 2× plain; opening a trip sheet would add a 4th, a region pick a 5th). All five blocks still fill from the single response.
  2. **+11 Explore links** to pages published 24–25 Nov (all 200, `index`, self-canonical; checked from the sitemaps' lastmod):
     - Activities 80→82: adventure/treks-near-shimla, adventure/shali-tibba-trek
     - Peaks 45→46: mountains-of-india/nilkantha (Neelkanth Peak)
     - Kashmir/Ladakh 24→25: trekking-vs-road-trips-in-ladakh-… (re-saved 24 Nov, was not linked)
     - Temples 64→65: pilgrimage-tours/jagannath-puri
     - Overseas 124→125: india-tours/jaisalmer
     - Kerala & Rajasthan 43→46: mehrangarh-fort, jaigarh-fort, christmas-in-kerala
     - Cabs 59→60: cabs/dalhousie-taxi-service
     - Countries 27→28: kenya-tour-packages
- **Data freshness (5 trips): 0 drift** — dharamshala-dalhousie-chandigarh ₹19,499 ✓ · magical-kashmir ₹16,999 6D/5N ✓ · luxury-kashmir ₹21,999 ✓ · kinnaur-sangla-chitkul ₹24,999 ✓ · dodham-badrinath ₹22,999 6D/5N ✓ (in meta description "From ₹22,999 pp" + product price; Sushil-approved 2 Nov — the visible page body shows no rupee figure, info only).

## Speed (Lighthouse 12, live, 1 run each; proxy noise is large)
- Mobile before 56 · LCP 3.8 s · TBT 1,550 ms · CLS 0.003 · 1,336 KiB → after 75 · LCP 4.4 s · TBT 70 ms · CLS 0.001 · 1,085 KiB
- Desktop before 90 · LCP 1.6 s · TBT 40 ms · CLS 0.008 · 2,000 KiB → after 89 · LCP 1.6 s · TBT 90 ms · CLS 0.007 · 2,000 KiB
- Honest read: the mobile jump is run-to-run noise (third-party Tawk/GTM timing; the after run loaded ~250 KiB less third-party). Tonight's change doesn't touch the load path — its real gain is 2–4 fewer requests later in the visit. +1.4 KB HTML.

## SHAs
- before/live `ae7940bcf46043be56e42e39b481dfee9571f8891c8b84f4fefe189e2842426e`
- after/LIVE `cf8e022040c612fa47db5f34b1896418c56063e66c84f626e679aa88c24258b7` (1,073,119 B)
- Present 1×: #tp-engine, #himachal-weather, nzw-css, nzw-js, #sbx, sbx-css, sbx-js, #nz-data; nzw-chip 15 → 15; 1 H1. `fetch('/suzu-weather-feed.json')` left in page: 0.

## Parity
```
PARITY PASS
  - size 1071727 -> 1073119 bytes
  - links 1170 -> 1181, headings 172 -> 172, json-ld 4 -> 4
```

## Tests (Playwright, SW blocked, sendBeacon + admin-ajax stubbed → nothing reached the server)
Local (after.html routed) and again on LIVE — identical:
| Check | 1440 | Pixel 7 |
|---|---|---|
| Page errors / H1 / overflow | 0 / 1 / 0 | 0 / 1 / 0 |
| #tp-engine above fold; Plan my trip → iframe /plan-your-trip/?embed=1… | ✅ top 463 | ✅ top 292 |
| Book Now → #hero-search in view, popup active | ✅ | ✅ |
| Weather-feed requests per visit (before → after) | 3 → 1 | 3 → 1 |
| Snow tile line / H-vs-K weather / nzw marquee filled | ✅ | ✅ |
| Region Kashmir → View trip → sheet "Stunning Kashmir", WhatsApp 1, route weather Srinagar 7°C · Sonamarg −7°C | ✅ | ✅ |
| New Explore links present | ✅ | ✅ |
verify_live: mobile 0 console errors; desktop only the known Tawk embed CORS/ERR_FAILED from the sandbox proxy (third-party). (Its "popup" selector is outdated — popup confirmed by the test above. Its "₹550" sheet price = the Rohtang permit fee line, not a trip price.)
Screenshots reviewed (hero, sheet): unchanged layout, route-weather pills fill.

## Rollback
Fetch `https://suzutravels.com/index-nz-previous.html?nc=<rand>` (= ae7940bc), queue as index.html with `--base cf8e022040c612fa47db5f34b1896418c56063e66c84f626e679aa88c24258b7 --backup index.html=index-nz-previous.html`.

## Notes
- Hand-off board is at its cap (49,074/49,152 B): only the "24n LIVE" line was swapped for "25n LIVE". Supervisor/Interactive: please prune ticked items older than 7 days.
- `add_repo` isn't in this session's tools any more, but the repo is already scoped to this session — clone + push to deploy-static worked without it.

## Next ideas
1. Explorer: "snow first" sort when the Snow theme chip is on (carried over).
2. nz-snow-js (`API` = snow spots) and nz-gr reviews could also use one idle loader; check their request timing next.
3. Update verify_live.js: popup selector (#szp-* / hero-search) and the tp-engine check instead of the film.
4. Keep adding Explore links as other agents publish.
