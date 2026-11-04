# call-time (TRUST_BACKLOG row 17) — "Pick a call time in your own time zone"
Live on hub /india-tours/ (11411) since 31 Oct 2026, `<!--szt:call-time-->…<!--/szt:call-time-->`, inserted right before
`<section class="lp-sec" id="do-you-need-a-visa-for-india"` (i.e. after the booking-protection panel).

- Shows up to 3 days (grouped by the visitor's local date) of hourly call slots inside the team's hours **9 am–9 pm IST (UTC+5:30)** —
  same wording as the kit's `talk` strip (gen_pages.py) — converted to the visitor's clock (browser time zone), each with its IST time.
  Slots start ≥ 2 hours from now (published "usually within 2 hours" reply time). IST has no DST; visitor DST handled by the browser.
- Picking a slot writes a call request (local time + zone + IST) → Send on WhatsApp (+91 70874 88961) / Send by email. It is a
  request, not a booked slot — the team confirms. The site's own WhatsApp popup (#szwap) may intercept the wa.me click, as on every link.
- No fetch, no third-party JS, no cookies, nothing stored. JS has no `&` / `//`. Prefix `.szo` (free on the site, checked 31 Oct 2026).
  Without JS (or before WP Rocket's delayed JS runs) the day/slot grid is hidden and a static message + both buttons still work.
- Build: `python3 build.py` → `widget.html` (asserts: no & or // in JS, banned words, no US$).
- Remove: `wp_replace_in_page` the whole marked block with an empty string.
- **Row 21 (4 Nov 2026):** also live on /golden-triangle-tour/ (11412, widget-11412.html) and /char-dham-yatra-for-nri/ (11413, widget-11413.html),
  inserted right after `<!--/szt:share-trip-->`. build.py now has a PAGES dict (hello line, page path, 'bring your questions' list, page-id rule);
  widget.html for the hub is byte-identical to before.
- Next: a kit hook for child pages (Reviewer) if wanted.
