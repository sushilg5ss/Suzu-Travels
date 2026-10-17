# trust-bar (TRUST_BACKLOG rows 1 + 2)
Trust strip (HP Tourism registration + certificate link, Google review count mirrored from the site's Trustindex widget `.ti-sub strong`
— never typed, hidden if the widget is absent, card/PayPal, local company since 2019) + "talk to a real person" bar (IST vs visitor-local
clock, "We usually reply within 2 hours", WhatsApp with visitor city from the browser time zone, email) + the exact booking line.
No third-party JS, no cookies, nothing stored. JS has no `&` / `//`. WP Rocket delays the inline script until first interaction —
before that the clocks show "—" and the review tile reads "Read what our guests say" (graceful).

- `widget.html` — original (green) palette; live on hub 11411 (the hub skin recolours it).
- `widget-11412.html` — gold/ink v2 palette + mobile width fix `body.page-id-11412{max-width:none}` (site-wide `html{zoom:.9}` strip);
  live on /golden-triangle-tour/ (11412) since 17 Oct 2026, inserted before `<nav aria-label="On this page" class="sx-toc">`.
- Build: `python3 build.py` (writes both). `variant(<page id>)` makes the gold version for another page (11413 next).
- Remove: `wp_replace_in_page` the whole `<!--szt:trust-bar-->…<!--/szt:trust-bar-->` block with an empty string.
