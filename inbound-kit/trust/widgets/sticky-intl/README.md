# sticky-intl (TRUST_BACKLOG row 11 `sticky-enquiry-bar-intl`) — live 2026-10-25 on 11411, 11412, 11413
The site already shows a mobile sticky bar `#szcta` (Get Free Quote → szmq enquiry popup · Book a Call · WhatsApp · Call) on every
page, so no second bar was added (it would clash). Problem found: on the inbound pages its WhatsApp button pre-filled
"Hi Suzu Travels, I would like a Himachal quote. [Ref: DR-<slug>]" — wrong for a foreign visitor on the India / Golden Triangle /
Char Dham pages.

This block only RE-LABELS that one link on its own page (the bar itself, the popup and the Ref tag are untouched):
- 11411: "Hello Suzu Travels, I am planning a trip to India (I am in <city>). Please send me ideas and a US$ quote. [Ref: DR-india-tours]"
- 11412: "... I am interested in a private Golden Triangle tour (Delhi, Agra, Jaipur) (I am in <city>) ... [Ref: DR-golden-triangle-tour]"
- 11413: "... I am interested in the Char Dham Yatra (Yamunotri, Gangotri, Kedarnath, Badrinath) (I am in <city>) ... [Ref: DR-char-dham-yatra-for-nri]"
- `<city>` = last part of the browser time zone (e.g. America/New_York → New York); omitted for India time zones. Nothing stored or sent.
- Runs at once, on DOMContentLoaded/load, at 1.5 s and 4 s, and in a capturing click listener on `#szcta a.w` (so it is right even if
  WP Rocket delays the inline script until the first tap). No CSS, no `&`, no `//`. JS off → old link (graceful).
- Placement: `<!--szt:sticky-intl-->…<!--/szt:sticky-intl-->` directly after `<!--/szt:trust-bar-->` on each page.
- Build: `python3 build.py` → widget-<id>.html. Remove: `wp_replace_in_page` the marked block with ''.
- Site-wide fix (not ours): the base `#szcta` WhatsApp text says "Himachal quote" on every page of the site — owner of that bar may
  want a per-section message.
