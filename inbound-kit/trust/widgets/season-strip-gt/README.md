# season-strip-gt (TRUST_BACKLOG row 22)
"Month by month: the Golden Triangle and its add-ons" on /golden-triangle-tour/ (11412). The page's hand-built table only says
"October – March"; its own add-on cards (Rishikesh, Himalayas = Shimla/Manali, Kashmir) run on different seasons.

- Rows: Delhi · Agra · Jaipur / Haridwar · Rishikesh / Shimla · Manali — month codes, notes and source line **imported** from
  `../season-heatmap/build.py` (hub chart, live 20 Oct 2026). No new facts, no prices. Kashmir: no colours, only the hub's dated
  FCDO + US State Dept advisory line.
- Month buttons (default = visitor's month) → summary per tour + WhatsApp (+91 70874 88961) prefilled with the month and the tours
  marked best. Link to the full hub chart `/india-tours/#szt-season`.
- Nothing stored, no fetch, no third-party JS, no cookies. JS: no `&`, no `//`, no HTML in strings. JS off = full strip + notes.
- Prefix `.szt-sg`, id `szt-sg`. Placed (5 Nov 2026) right after the 'Best Time for a Golden Triangle Tour' section, i.e. inserted
  before `<section class="lp-sec" id="what-every-tour-includes"`.
- Build: `python3 build.py`. Remove: `wp_replace_in_page` the `<!--szt:season-strip-gt-->…<!--/szt:season-strip-gt-->` block with ''.
- If the hub chart rows change, re-run build.py and replace the block (expected_count 1).
