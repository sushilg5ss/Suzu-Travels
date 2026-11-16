# check-us (TRUST_BACKLOG row 31) — "Check us before you pay"
Hub /india-tours/ (11411), right after `<!--/szt:booking-protected-->` (before call-time). Live 15 Nov 2026.

Four checks from the live guide /india-tours/how-to-choose-a-travel-agency-in-india/ (its own checklist headings — build.py asserts
they still match `src/pages/how-to-choose-a-travel-agency-in-india.json`), each answered with Suzu's own proof, text copied from the
guide's "How we do it" cards + the exact registration and booking lines (README §1):
1. Registration → /certificates/ + WhatsApp "send me a copy of your registration certificate"
2. Office on a map → Google Maps search of the office address
3. Written day-by-day plan → the two pinned sample itinerary PDFs (GT 6 d, Char Dham 11 d — same URLs as pdf-hub-cards)
4. Deposit + refund rule → exact booking line + jump to #booking-protected
Footer button → the full guide (8-point checklist + red flags).

No JS, no prices, no reviews/counts, nothing stored. Prefix `.szq` (unused on 11411). Gold/ink/sand palette.
Build: `python3 build.py` → widget.html. Remove: `wp_replace_in_page` 11411 the whole `<!--szt:check-us-->…<!--/szt:check-us-->` with ''.

## Product pages (TRUST_BACKLOG row 32) — live 16 Nov 2026
`python3 build_product.py` → `widget-11412.html` (/golden-triangle-tour/) + `widget-11413.html` (/char-dham-yatra-for-nri/), each placed right after
`<!--/szt:before-you-fly-->`. Same 4 checks/answers as the hub (imports build.py). Prefix **.szk** (.szq is already used on 11412/11413 by
itinerary-pdf). Check 3 links only that page's own PDF; check 4 links `#booking-protected` on 11412 and the hub's panel on 11413 (11413 has no panel).
Remove: `wp_replace_in_page` the whole `<!--szt:check-us-->…<!--/szt:check-us-->` block with ''.
