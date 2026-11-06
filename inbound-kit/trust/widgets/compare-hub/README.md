# compare-hub (TRUST_BACKLOG row 23 `compare-hub-tours`) — live 2026-11-06 on /india-tours/ (11411)
"Compare at a glance — Which India tour fits your trip?": table (desktop) / stacked rows (≤760 px) of the hub's own six package cards
(Classic GT 6 d, GT + Rishikesh 8 d, GT + Kashmir 10 d, GT + Himalayas 12 d, Golden Temple & Himalayas 10 d, Char Dham 11 d): name + style tag, length, places, 'from' price + unit.
- **Nothing typed:** rows are read in the browser from `.lp-card` elements with `.lp-price` (same logic as compare-gt/compare-cd). Build asserts no US$ figure in the HTML.
- The hub has no quote helper → "Quote this one" is a link whose href is copied from the card's own "Get Free Quote" WhatsApp link (`.foot a.q`, tour name prefilled); "See tour" scrolls to the card and outlines it in gold for 2.6 s.
- Works with the hub currency toggle (reads `.lp-price b` and the first `span` only). No fetch, no third-party JS, no cookies, nothing stored. JS: no `&`, no `//`, no backslash. Prefix `.szg` (also used on 11412/11413; checked unused on the hub — only the `<!--szgal-->` comment). Section id `compare-hub-tours`.
- No JS / fewer than 2 cards: section keeps `hidden` → nothing shows.
- Placement: `<!--szt:compare-hub-->…<!--/szt:compare-hub-->` right after the package section, before `<!--szv:dest-->` on 11411.
- Build: `python3 build.py` (imports CSS from ../compare-gt/build.py) → widget-11411.html. Remove: `wp_replace_in_page` the marked block with ''.
