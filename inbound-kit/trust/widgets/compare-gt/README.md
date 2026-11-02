# compare-gt (TRUST_BACKLOG row 19 `compare-gt-packages`) — live 2026-11-02 on /golden-triangle-tour/ (11412)
"Compare at a glance — Which Golden Triangle tour fits your trip?": one table (desktop) / stacked rows (≤760 px) of the page's
own six package cards: tour name + style tag, length (days/nights), route line, 'from' price + unit, and a "Quote this one" button.
- **Nothing typed:** the rows are built in the browser from `.lp-card` elements that contain `.lp-price` (tag `.lp-tag` split on " · ",
  `h3`, the `h3 + p` route line, `.lp-price b` + `span`). If a card's price or name changes, the table follows. Build asserts no US$ figure in the HTML.
- "Quote this one" selects the matching tour in the quote helper (`#szr-tour`, option text starts with the card name), fires `change`
  (the helper's message + WhatsApp/email links rebuild) and scrolls to `#quote-helper`. If the helper is missing it only scrolls.
- No fetch, no third-party JS, no cookies, nothing stored. JS: no `&`, no `//`, no backslashes. Prefix `.szg` (free, checked 2 Nov 2026).
- No JS / fewer than 2 cards found: the section keeps its `hidden` attribute → nothing shows, the cards above still work.
- Placement: `<!--szt:compare-gt-->…<!--/szt:compare-gt-->` right before `<!--szt:quote-helper-->` (after the package cards + 'About our prices').
- Build: `python3 build.py` → widget-11412.html. Remove: `wp_replace_in_page` the marked block with ''.
- Note: on plain (WP Rocket delayed-JS) loads the very first tap can be swallowed while the delayed scripts start — same for every widget; second tap works.
