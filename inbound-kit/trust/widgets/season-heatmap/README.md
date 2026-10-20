# season-heatmap (TRUST_BACKLOG row 6)
"India Season Chart: Where to Go Each Month" — month × region grid (Delhi·Agra·Jaipur, Varanasi, Amritsar, Rishikesh·Haridwar,
Shimla·Dharamshala, Manali, Ladakh/Leh, Kerala, Goa) with 4 states: ★ Best · ❄ Snow season · ☔ Monsoon · "Possible — ask us"
(never "avoid" without a source). Kashmir has no colours, only the dated FCDO + State Dept line. Month buttons (default = visitor's
current month) highlight the column and show a summary + WhatsApp link prefilled with the month and the 'best' regions. Nothing stored,
no third-party, no cookies. JS off (or WP Rocket delayed JS before first interaction): full grid + notes visible, buttons hidden.

Data only from fact packs: best-places-to-visit-in-india.md season table + facts 1/3/7/8/14/15, kerala-tour.md facts 11/12,
goa-holiday.md facts 1/4/5/7, rishikesh-yoga-retreat-guide.md fact 10. Amritsar = Suzu planning (labelled). Ladakh = "summer,
no official month source — confirm".

- `widget.html` — hub /india-tours/ (11411), live 20 Oct 2026, inserted before `<section class="lp-sec" id="travelling-with-us"`
  (right after the hand-built 'Best Time to Visit North India' table).
- Build: `python3 build.py` (asserts: one line, no `&`/`//` in JS, no HTML tags inside JS strings, banned words absent, 12 months per row).
- **Lesson (20 Oct):** wpautop rewrote `"<div>"` inside a JS string (→ syntax error), and `<` escapes sent through the MCP were
  stored with a doubled backslash. Build DOM nodes with `createElement` — never HTML strings in inline JS.
- Remove: `wp_replace_in_page` the whole `<!--szt:season-heatmap-->…<!--/szt:season-heatmap-->` block with ''.
