# cd-guides (TRUST_BACKLOG row 30) — built 2026-11-13 18:55 IST, placement pending

**What:** "Plan the rest of your trip — Free guides for your Char Dham yatra" for /char-dham-yatra-for-nri/ (11413):
5 pilgrim-journey link cards in two groups (More of sacred India · Add to your yatra) + the same dark trust line
linking the agency-checking guide and /certificates/ with the exact registration line. Reuses the gt-guides (row 29)
build with a page switch — Char Dham add-ons instead of Golden Triangle ones.
**Why:** curl 12 Nov 2026 — 11413 links only the 7 before-you-fly guides + private-driver, none of these live
pilgrim pages (Varanasi, Kumbh Mela 2027, Rishikesh yoga retreat, Amritsar Golden Temple, Best time to visit Himachal).
**Data:** label + blurb from `live.json` only. No prices, no new facts, no JS, nothing stored.
**Where:** right after `<!--/szt:itinerary-pdf-->` on 11413 (mirrors gt-guides on 11412), wrapped in
`<!--szt:cd-guides-->…<!--/szt:cd-guides-->`. Prefix `.szw` (gt-guides prefix; the two never share a page).
**Verified (local only):** Playwright 1440 + 390 px — no overflow, 1 H1 (page's own), single .szw block, 5 card links +
2 trust links, 0 console errors. Palette gold/sand/ink, no green.
**NOT live:** Suzu Travels WordPress MCP was unreachable this run (CONNECT_TIMEOUT), so wp_replace_in_page could not
run. Placement + live verify (dry_run expected_count 1 after `<!--/szt:itinerary-pdf-->`, then Playwright 1440/390 live
+ curl ×2) is the first step for the next Trust run once the WP connector is back.
**Undo (once placed):** wp_replace_in_page 11413, replace the marked block with ''.
**Rebuild:** `python3 build.py` → widget.html (asserts: no US$, ₹, verified, 24/7, DMC, script; 1 marker; reg line present).
