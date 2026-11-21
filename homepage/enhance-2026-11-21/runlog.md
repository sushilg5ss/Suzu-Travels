# Homepage Enhancement Agent — 21 Nov 2026 night run

## Summary
- **Live base:** `a4efbfbf…f496` (1,046,536 B) = last night's fc84e5d1 + the Google-review counter update (409→411 reviews, "400+"→"410+"; 10 bytes, same size, done outside deploy-static by the live-reviews automation). Built on it, kept it.
- **Deploy: LIVE** — deploy-static `2026-11-21n-homepage`, status `deployed` 18:04:06 UTC (23:34 IST), attempt 1, exit 0. Plain + `?nc` fetch SHA = after. Server backup `index-nz-previous.html` = a4efbfbf (verified).
- **New tonight:**
  1. **"Weather on this route" in every trip sheet** (roadmap 3 informative + 5 links): under "When to go", up to 5 chips for the places on the trip's route, each with the **live temperature now** and a **"❄ snow" flag** when the 5-day forecast has snow, linking to that place's weather page, plus a **हिंदी** link where a `*-ka-mausam` page exists. Header shows "Now · updated HH:MM IST · MET Norway".
     - Data: the same `/suzu-weather-feed.json` the weather widget uses (121 places). Fetched **only when a sheet opens**, never on page load; skipped on Save-Data; temps hidden if the feed is > 30 h old (the links still show). Respects the widget's °C/°F choice (`nzw-unit`).
     - 55 route names mapped → 36 places / 67 URLs, all checked 200. Example: Shimla–Manali → Shimla 10°C · Kufri 9°C · Manali 11°C · Solang 8°C ❄; Shakti Peeth → Bilaspur/Una/Kangra; Manali–Leh → Leh 3°C, Nubra ❄, Pangong 0°C. 55 of 63 trips get a row (Goa, Kerala, Rajasthan, Varanasi… have no weather pages → no row).
  2. **Fix (own work, 20 Nov):** the 74 links in "Weather today in 74 more places" had no trailing slash → every one was a 301 hop. Now point straight at the 200 URL. This is why exact parity flags "74 links removed" (see Parity).
  3. **10 links to pages published 20 Nov** (all 200, index, self-canonical): Routes fold +6 (Shimla Airport, Kangra Airport, Kangra Valley toy train, Norbulingka, Tushita, Library of Tibetan Works & Archives) → 35; Overseas fold +4 (Himachal trip from Malaysia, 3 German guides with `lang="de"`) → 115.
- **Data freshness (5 trips): 0 drift** — shimla-manali-chandigarh ₹12,499 6D/5N ✓ · kashmir-7 7D/6N, goa-7 7D/6N, glimpses-ladakh 5D/4N, nainital 4D/3N: pages still publish no package price → "Price on request" stays correct.

## Speed (Lighthouse 12.6.1 mobile, live)
- Before: 59 · LCP 3.6 s · TBT 1,710 ms · CLS 0.001 · 1,330 KiB · DOM 7,678
- After: 60 · LCP 4.4 s · TBT 940 ms · CLS 0.001 · 1,332 KiB · DOM 7,698
- Same range — run-to-run noise is bigger than tonight's change (+8.4 KB HTML, no load-time JS; feed fetched only on sheet open).

## SHAs
- before/live `a4efbfbf59cce0b7585a2dcda373eb06ec1f9dabed5185daaa2f4fcad176f496`
- after/LIVE `725e962e8b1b3e0a0af9a57587c0c901988684fc25015e74fe3270f464d23ab9` (1,054,894 B)
- Present 1×: #tp-engine, #himachal-weather, nzw-css, nzw-js, #sbx, sbx-css, sbx-js, #nz-data; nzw-chip 15 → 15; 1 H1.

## Parity
Exact (before → after):
```
PARITY FAIL
  x links removed: 74 e.g. ['https://suzutravels.com/kishtwar-weather', ...]
  - links 1123 -> 1135, headings 172 -> 172, json-ld 4 -> 4
```
The 74 "removed" are exactly our own no-slash `*-weather` links from 20 Nov; each is present in after with the trailing slash (checked programmatically). Normalised (before + only the slash fix) → after:
```
PARITY PASS
  - size 1046610 -> 1054894 bytes
  - links 1123 -> 1135, headings 172 -> 172, json-ld 4 -> 4
```
(+10 real links; +2 are the JS template strings in wxRow.)

## Tests (Playwright, live URL routed to after.html, SW blocked, sendBeacon + admin-ajax stubbed → nothing real posted)
| Check | 1440 | Pixel 7 |
|---|---|---|
| Page errors / H1 / overflow | 0 / 1 / 0 | 0 / 1 / 0 |
| #tp-engine above fold; Plan my trip → /plan-your-trip/?embed=1… | ✅ top 463 | ✅ top 292 |
| Book Now → hero-search active | ✅ | ✅ |
| Uttarakhand filter | 12 → 10 | 6 → 6 (phones show 6) |
| View trip (real click) → sheet, WhatsApp 1 | ✅ | ✅ |
| Weather row: Shimla–Manali / Winter Spiti 4x4 / Kinnaur / Mussoorie / Luxury Kashmir / Shakti Peeth / Manali–Leh | ✅ temps + Hindi | ✅ |
| Goa week → no row | ✅ | ✅ |
| Chip min height | 44 px | 44 px (49 css × zoom .9) |
| #nz-wxa links with slash | 74/74 | 74/74 |
Screenshots reviewed (sheet desktop + mobile): chips sit under the month strip, glacier-blue pills, Hindi half in white; clean, on brand, no overflow.

**verify_live.js after deploy:** desktop + mobile 0 page errors, #tp-engine top 463/292, Book Now → hero-search, sheet WhatsApp ✓, weather row ✓ (Shimla 10°C · Kufri 9°C · Manali 11°C · Solang 8°C ❄). Only console error: Tawk embed CORS on desktop (third-party, legacy, not ours). No 4xx on suzutravels.com.

## Rollback
Fetch `https://suzutravels.com/index-nz-previous.html?nc=<rand>` (= a4efbfbf), queue it as index.html with `--base 725e962e8b1b3e0a0af9a57587c0c901988684fc25015e74fe3270f464d23ab9 --backup index.html=index-nz-previous.html`.

## Notes
- Weather feed was last updated 11:49 UTC (≈6 h before this run); the sheet shows the update time honestly. If the hourly feed workflow has stalled, that's the Ranking/feed owner's lane.
- Release files: `claude/himachal-landing/releases/2026-11-21/` (enh-2026-11-21.py + wxmap.py). Script asserts "already applied".

## Next ideas
1. Same weather chips on the "Pick your kind of trip" / region slides (region → hub weather page) — cheap now that the map exists.
2. Hindi weather pages exist for 38 places; 17 mapped places have only English — link Hindi when Content publishes them.
3. When tour pages show a visible "From" price for the 9 meta-only trips, fill them in.
