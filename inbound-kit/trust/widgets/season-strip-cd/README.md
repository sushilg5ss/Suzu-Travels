# season-strip-cd (TRUST_BACKLOG row 25) — "When to go: the Char Dham year at a glance"
Live since 8 Nov 2026 on /char-dham-yatra-for-nri/ (11413), `<!--szt:season-strip-cd-->…<!--/szt:season-strip-cd-->`, inserted right
before `<section class="lp-sec" id="trek-pony-palki-or-helicopter"` (i.e. after the 11-day itinerary + itinerary-PDF card).

- 12 month tiles: Jan–Mar + Dec temples closed · Apr / Nov opening / closing month · May–Jun + Sep–Oct best window · Jul–Aug monsoon.
- NO NEW FACTS: every line is 11413's own hand-built text — FAQ "When is the best time for NRIs to do the Char Dham Yatra?"
  (open late April or May, close October or November, best May–June + Sep–Oct, Jul–Aug monsoon landslides, dates announced early each
  year), packing line ("nights are cold even in June"), registration FAQ (registrationandtouristcare.uk.gov.in). No year-specific dates
  → "please confirm before travel". No prices.
- Tap a month (default = visitor's month) → summary + WhatsApp (+91 70874 88961) prefilled with the month. Nothing stored, no fetch,
  no third-party JS, no cookies. JS: no `&`, no `//`, no HTML in strings. JS off: tiles + legend + notes visible, buttons disabled.
- Prefix `.szt-sc`, id `szt-sc` (free, checked 8 Nov 2026). WP Rocket delay-JS: first tap may only wake the scripts.
- Build: `python3 build.py`. Remove: `wp_replace_in_page` the marked block with ''.
- If 11413's own season FAQ changes, update CODE/SUM in build.py and replace the block (expected_count 1).
