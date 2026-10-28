# itinerary-pdf (TRUST_BACKLOG row 8)
"Take this plan with you" card + a static, printable 2-page A4 PDF of the itinerary. No email gate, no JS, no third-party, nothing stored.

- PDF content is copied ONLY from the live hand-built page (11412 day-by-day, 'What Every Tour Includes' minus the 24/7 card,
  exclusions line, FAQ price wording); price US$449 from data/prices.json ("per person, two sharing a room"); booking line +
  registration line exact; office address + +91 70874 88961 + info@suzutravels.com. build.py asserts prices ∈ prices.json, no 24/7/verified/₹.
- `golden-triangle-6-day-itinerary-suzu-travels.pdf` — rendered by `node render.js` (Chromium print) from `gt-6-day.html` (`python3 build.py`).
- Hosting: WordPress media upload via the MCP accepts images only → PDF is served from jsDelivr pinned to commit
  ccf7eb01e4b8eb964380cc492eabace05375e4e1 (lowercase `sushilg5ss/suzu-travels` — the mixed-case repo path returns 503 on jsDelivr).
  If the PDF changes: commit, then `python3 build.py widget <new pinned URL>` and replace the marked block.
- `widget-11412.html` — live on /golden-triangle-tour/ (11412) since 21 Oct 2026, inserted before
  `<section class="lp-sec" id="taj-mahal-tips-for-foreign-visitors"` (right after the 6-day itinerary + 'Get this tour in USD').
- Child itinerary pages (kit-generated) need a kit hook — Reviewer: gen_pages.py should render a PDF per `itinerary` page and add this card.
- Remove: `wp_replace_in_page` the whole `<!--szt:itinerary-pdf-->…<!--/szt:itinerary-pdf-->` block with ''.
- **11413 (28 Oct 2026):** `build_chardham.py` → `cd-11-day.html` → `node render2.js cd-11-day.html char-dham-yatra-11-day-itinerary-suzu-travels.pdf` (3 pages A4, 105 KB). Text only from live 11413 (itinerary, 'What Our NRI Pilgrims Get' minus the oxygen/first-aid line, 'About our prices', Documents & Rules with README §1 visa + health lines), US$799 from prices.json. Pinned jsDelivr bc61aa787f9c445478f091cd6498207ef49a886b. `widget-11413.html` inserted before `<section class="lp-sec" id="trek-pony-palki-or-helicopter"` (right after the 11-day itinerary).
