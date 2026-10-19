# booking-protected (TRUST_BACKLOG row 5 — how-booking-is-protected)
"How Your Booking Is Protected": exact booking line, 6 money-safety cards (everything in writing · only 20% up front · official
payment channels only / never a personal account · HP Tourism registration + certificate link, GST, office address · driver's
name/photo/car number before the trip (approved wording) · reachable on +91 70874 88961 before and during the trip) and 5 honest
"what if" answers in native `<details>` (flight delayed · road/monument closed — Terms §08 'extra costs paid by the guest' ·
cancel — 48 h full refund, then the terms in the confirmation · we cancel — full refund or another date (Refund policy §04) ·
how to know you pay the real Suzu — /payment/ page). **No JavaScript**, no third-party anything, nothing stored. Gold/ink v2 palette.

Sources: README §1 (booking line, registration line, driver wording), /terms-and-conditions/ §01/§08 and
/cancellation-and-refund-policy/ §01/§04 (both last updated 28 Sep 2026, repo `policies/`). No 24/7, no insurance, no 'verified'.

- `widget-11411.html` — hub /india-tours/ (no steps: the hub already has 'Book Your India Tour in 4 Easy Steps'); live 19 Oct 2026,
  inserted before `<section class="lp-sec" id="do-you-need-a-visa-for-india"` (i.e. right after the 4-steps section).
- `widget-11412.html` — /golden-triangle-tour/ with the 4 steps; live 19 Oct 2026, inserted before
  `<section class="lp-sec" id="golden-triangle-tour-frequently-asked-qu"` (after the guests section, before the FAQ).
- Build: `python3 build.py` (asserts: one line, no script, booking line once, registration exact, banned words absent).
- Remove: `wp_replace_in_page` the whole `<!--szt:booking-protected-->…<!--/szt:booking-protected-->` block with ''.
- Note: on the plain (WP Rocket) copy the very first click on the page loads the delayed site JS; summaries then toggle normally.
