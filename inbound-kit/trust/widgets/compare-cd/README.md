# compare-cd (TRUST_BACKLOG row 20 `compare-char-dham-yatras`) — live 2026-11-03 on /char-dham-yatra-for-nri/ (11413)
"Compare at a glance — Which yatra fits your family?": table (desktop) / stacked rows (≤760 px) of the page's own four yatra cards
(Do Dham 7 d, Char Dham by Road 11 d, Comfort Yatra 12 d, Helicopter 6 d): name + style tag, length, route, 'from' price + unit, "Quote this one".
- **Nothing typed:** rows are read in the browser from `.lp-card` elements with `.lp-price` (same logic as compare-gt, row 19). Build asserts no US$ figure in the HTML.
- "Quote this one" selects the matching yatra in the 11413 quote helper (`#szr-tour`); names are compared with '&' read as 'and'
  (card "Do Dham: Kedarnath & Badrinath" ↔ option "Do Dham: Kedarnath and Badrinath (7 days)"), fires `change` (message + WhatsApp/email rebuild), scrolls to `#quote-helper`.
- No fetch, no third-party JS, no cookies, nothing stored. JS: no `&`, no `//`, no backslash. Prefix `.szg` (shared with compare-gt; different page). Section id `compare-yatras`.
- No JS / fewer than 2 cards: section keeps `hidden` → nothing shows.
- Placement: `<!--szt:compare-cd-->…<!--/szt:compare-cd-->` right before `<!--szt:quote-helper-->` on 11413.
- Build: `python3 build.py` (imports CSS from ../compare-gt/build.py) → widget-11413.html. Remove: `wp_replace_in_page` the marked block with ''.
