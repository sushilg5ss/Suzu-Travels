# currency-view (TRUST_BACKLOG row 3 — 11412 + 11413)
Toggle US$ / £ GBP / € EUR / A$ AUD / C$ CAD above the package cards. Shows "≈ £224 (approx.)" under each `.lp-price b`
US$ "from" price already on the page (prices only from data/prices.json, never typed here). Rates: ECB reference rates via
`api.frankfurter.dev/v1/latest?base=USD` (free, keyless, CORS *), fetched on the first non-US$ click, 7 s timeout →
"Live rates unavailable… all quotes and payments are in US$" and back to US$. Note shows the rate date. No storage/cookies/3rd-party JS;
inline JS has no ampersand and no double slash. JS off / before WP Rocket runs scripts: buttons do nothing, US$ prices stay (graceful).
Clicks while rates are loading are ignored (busy guard). Gold/ink/sand v2 palette, classes `.szt-cur`, `.szt-cx`, id `sztCur`.
The hub 11411 has its own older copy (`<!--szv:currency-->`, hub-v2/build.py).

- `widget.html` — same block on both pages. Build: `python3 build.py`.
- 11412 /golden-triangle-tour/: inserted after `All tours are private and can be changed.</p>` (Tour packages section). Live 2026-10-26.
- 11413 /char-dham-yatra-for-nri/: inserted after `All are private, and all can be changed.</p>` (Yatra packages section). Live 2026-10-26.
- Remove: `wp_replace_in_page` the whole `<!--szt:currency-view-->…<!--/szt:currency-view-->` block with an empty string.
