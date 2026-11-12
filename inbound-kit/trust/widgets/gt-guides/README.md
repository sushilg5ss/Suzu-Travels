# gt-guides (TRUST_BACKLOG row 29) — live 2026-11-12

**What:** "Plan the rest of your trip — Free guides for your Golden Triangle tour" on /golden-triangle-tour/ (11412):
8 link cards in two groups (Delhi/Agra/Jaipur in detail · add-on trips) + a dark trust line linking the agency-checking
guide and /certificates/ with the exact registration line.
**Why:** curl 12 Nov 2026 — 11412 linked none of the live GT-related child pages (7-day itinerary, Delhi tour, Taj from
Delhi, Agra→Jaipur, Rajasthan, Amritsar, Himachal 10 days, India in 2 weeks, choosing a travel agency).
**Data:** label + blurb from `live.json` only. No prices, no new facts, no JS, nothing stored.
**Where:** right after `<!--/szt:itinerary-pdf-->`, wrapped in `<!--szt:gt-guides-->…<!--/szt:gt-guides-->`. Prefix `.szw`.
**Undo:** wp_replace_in_page 11412, replace the marked block with ''.
**Rebuild:** `python3 build.py` → widget.html (asserts: no US$, ₹, verified, 24/7, script).
