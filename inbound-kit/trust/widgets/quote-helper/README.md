# quote-helper (TRUST_BACKLOG row 14 `quote-request-helper`) — live 2026-10-29 on 11412 + 11413
"What to send us for an exact US$ quote": 6 fields (tour/yatra from the page's own package cards, flying in from, dates or month,
travellers adults + children, hotel class [11412] / ages of the elders [11413], arrival airport DEL/JAI or DEL/DED) → live message
preview → "Send on WhatsApp" (+91 70874 88961) / "Send by email" (info@suzutravels.com). Blank = "Not sure yet".
- Nothing stored or sent by the page; no fetch, no cookies, no third-party JS. Placeholder of "Flying in from" = browser time-zone city
  (e.g. "e.g. Chicago"), never prefilled. JS: no `&` (fromCharCode(38)), no `//` (URL bases in data-b), no backslashes (newline = fromCharCode(10)).
- JS off / before WP Rocket runs the script: buttons carry a static message listing the fields (graceful); the click listener rebuilds the link at click time.
- No prices printed (build asserts any US$ ∈ prices.json, no 24/7 / verified / ₹ / DMC).
- Placement: own `<section class="szr">` right after the package cards — 11412 before `<section class="lp-sec" id="what-you-see-in-delhi-agra-and-jaipur"`,
  11413 before `<section class="lp-sec" id="what-our-nri-pilgrims-get"`. Class prefix `.szr` (new).
- Build: `python3 build.py` → widget-11412.html / widget-11413.html. Remove: `wp_replace_in_page` the marked `<!--szt:quote-helper-->…<!--/szt:quote-helper-->` block with ''.
