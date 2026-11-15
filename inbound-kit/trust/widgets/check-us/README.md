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
