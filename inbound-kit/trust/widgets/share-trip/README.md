# share-trip (TRUST_BACKLOG row 18 share-this-trip) — "Send this to your travel partner"
Live since 1 Nov 2026 on, `<!--szt:share-trip-->…<!--/szt:share-trip-->`:
- hub /india-tours/ (11411) — right after `<!--/szt:call-time-->` (widget-11411.html, page link only)
- /golden-triangle-tour/ (11412) — right after `<!--/szt:quote-helper-->` (widget-11412.html, + 6-day GT PDF, jsDelivr ccf7eb0)
- /char-dham-yatra-for-nri/ (11413) — right after `<!--/szt:quote-helper-->` (widget-11413.html, + 11-day Char Dham PDF, jsDelivr bc61aa7)

What it does: foreign trips are decided by couples/families → one tap sends the page (and the itinerary PDF) to the visitor's partner:
Share on WhatsApp (`api.whatsapp.com/send?text=` with no recipient — deliberately NOT `wa.me`, because the site's #szwap lead popup
intercepts every wa.me click and would ask for name/phone before a share to a friend), Email it (`mailto:` with no recipient),
Copy link (Clipboard API, textarea fallback), "More ways to share" (navigator.share, shown only where supported — phones), PDF link.
Static canonical URLs (no tracking params). No fetch, no third-party JS, no cookies, nothing stored, no prices, nothing sent to Suzu.
JS has no `&` / `//`. Prefix `.szh` (free on the site, checked 1 Nov 2026). Without JS: Copy/More buttons hidden, WhatsApp/Email/PDF
links and the plain link text still work.
- Build: `python3 build.py` → widget-11411/11412/11413.html (asserts: no & or // in JS, banned words, no US$, no wa.me).
- Remove: `wp_replace_in_page` the whole marked block with an empty string.
- Next: kit hook for child pages (Reviewer) if wanted.
