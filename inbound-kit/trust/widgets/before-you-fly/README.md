# before-you-fly (TRUST_BACKLOG row 24) — "Your before-you-fly checklist"
Live since 7 Nov 2026, `<!--szt:before-you-fly-->…<!--/szt:before-you-fly-->`, right after `<!--/szt:call-time-->` on:
- /golden-triangle-tour/ (11412) — widget-11412.html (kicker "Before you fly to Delhi")
- /char-dham-yatra-for-nri/ (11413) — widget-11413.html (kicker "Before you fly for the yatra")
- hub /india-tours/ (11411) — widget-11411.html (kicker "Before you fly to India"), since 10 Nov 2026 (row 27), right after `<!--/szt:share-trip-->`.
  **Hub copy uses prefix `.szb`** (ids szb, szb-n, szb-r, szb-1..6): the hub already carries `.szy`/`.szy-a` (pdf-hub-cards links), and `.szy{padding…}` would have restyled them. build.py re-prefixes via PAGES['11411']['prefix'].

Row 28 (11 Nov 2026): 7th card **India trip cost** (/india-tours/india-trip-cost/, 20694, label+blurb from live.json) added on all three pages + 'Seven things'. india-festivals-calendar deliberately not added (trip planning, not a pre-flight task).

What it does: 6 (now 7) tick-box cards linking the live practical guides (e-Visa, travel insurance, SIM/eSIM, UPI & money, trains vs flights,
first time in India). Text = each guide's own label + blurb from live.json (no new facts) + "Apply yourself on the official site; we are
not a visa agency." Counter "x of 6 done", Clear ticks, WhatsApp question link (+91 70874 88961), "information only" line.
Ticks are plain checkboxes — nothing stored, no fetch, no 3rd-party JS, no cookies. JS has no & / //. Prefix `.szy` (free, checked 7 Nov).
Without JS: ticks still work natively, counter/Clear hidden.
Note: WP Rocket delay-JS swallows the very first tap before scripts load (same for every widget); after first interaction it works.
- Build: `python3 build.py` (reads ../../../live.json; asserts banned words, no US$, visa line).
- Remove: `wp_replace_in_page` the whole marked block with ''.
