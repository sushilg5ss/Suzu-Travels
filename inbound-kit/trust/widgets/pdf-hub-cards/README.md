# pdf-hub-cards (TRUST_BACKLOG row 16)
'Itinerary PDF' download pill on the hub 11411 package cards that have a printable plan:
- Classic Golden Triangle (6 Days) → golden-triangle-6-day PDF (jsDelivr pinned ccf7eb0, 2 pages, 219 KB)
- Char Dham Yatra (11 Days) → char-dham-yatra-11-day PDF (jsDelivr pinned bc61aa7, 3 pages, 105 KB)
PDFs are the ones made by `trust/widgets/itinerary-pdf/` (text from live 11412/11413). No JS, no third party, nothing stored, no prices printed.
Prefix `.szy` (inline styles only). `python3 build.py` → widget-gt.html / widget-cd.html (one line each).
Placed 30 Oct 2026 directly before each card's `<div class="foot"><a class="q" href="https://wa.me/...%22Classic%20Golden%20Triangle%22`
/ `...%22Char%20Dham%20Yatra%22%20%2811` (inside the card, under the from-price).
Remove: `wp_replace_in_page` the `<!--szt:pdf-hub-gt-->…<!--/szt:pdf-hub-gt-->` and `<!--szt:pdf-hub-cd-->…<!--/szt:pdf-hub-cd-->` blocks with ''.
If a PDF changes: re-pin, edit CARDS in build.py, rebuild, replace the marked block.
