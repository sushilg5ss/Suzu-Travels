# planner-matches (hub 11411) — live 2026-10-27

Finishes TRUST_BACKLOG row 4 ("Next: show matching live pages + 'from' prices under the chips").
Under the region chips of the hero planner card (`#szpForm`, from `<!--szv:skin-->`) a small sand panel shows, live as chips change:
- **Matching tours on this page** — the hub's own `.lp-card` packages whose title/location line contains the region; title and
  "from US$…" are READ from the card (`h3`, `.lp-price b`), so no number is typed here. Click = smooth scroll + gold outline on the card.
  No match → "No ready-made tour for this mix yet. Send it to us and we plan it from scratch, with a US$ quote."
- **Read before you go** — up to 4 live child-page links (paths + labels from `live.json`, built by `build.py`; ' & ' → ' and').
JS off → nothing shown (planner unchanged). No storage, no fetch, no third-party code. Prefix `.szj` (checked unused on hub).
Placement: `<!--szt:planner-matches-->` right after `<!--/szv:skin-->`. Revert = replace the marked block with ''.
Rebuild: `python3 build.py` → widget.html, then wp_replace_in_page the old block. Update the map when new region pages go live.
Note: on the cached plain URL WP Rocket "Delay JS" runs it after first scroll/tap (same as the planner script).

**21 Nov 2026 (row 39):** map refreshed — each region chip now lists its own dedicated live page first (varanasi-trip-guide, ladakh-trip-guide, amritsar-golden-temple-tour, himachal-10-day-itinerary, kashmir-7-day-itinerary, golden-triangle-itinerary-7-days, south-india-tour …). Publish with `ops-row39-2026-11-21.json` (one replace of the JS map; dry_run, expected_count 1). Revert = the same op reversed. Note: the JS shows max 3 guides per region (loop q<3), max 4 links in total.

**Live 22 Nov 2026:** row 39 map published on 11411 (dry_run 1, replaced 1). Live check 1440 + 390 (?v= + plain): Varanasi/Ladakh/Amritsar/Kerala chips list their own guides; screenshot live-row39-390.png.
