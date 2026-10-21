# Outbound kit — Holidays Abroad section of suzutravels.com

Owner: Sushil Kumar (Suzu Travels). Created 17 Oct 2026 after the section had seen no development since the 28 Sep redesign.
Audience: **Indian travellers going abroad**. Goal: enquiries (WhatsApp +91 70874 88961, /contact/, info@suzutravels.com). No prices on outbound pages — every trip is a costed quote within ~24 h.

## Pages (WordPress, classic content, ONE-line HTML)
| page | id | design |
|---|---|---|
| /international-tour-packages/ (hub, menu "Holidays Abroad") | 11347 | `.hx` v1 — real-photo hero slideshow + WhatsApp trip planner, trust strip, photo destination cards, trip-style tabs, guest photos, steps, why, FAQ (+FAQPage JSON-LD), photo CTA, photo credits |
| /nepal-tour-packages/ | 11355 | `.sx` (28 Sep) + real-photo hero slideshow (17 Oct) |
| /bhutan-tour-packages/ | 11362 | same |
| /sri-lanka-tour-packages/ | 11364 | same |
| /maldives-tour-packages/ | 11366 | same |
| /thailand-tour-packages/ | 11368 | same |
| /singapore-tour-packages/ | 11370 | same |
| /malaysia-tour-packages/ | 11372 | same |
| /vietnam-tour-packages/ | 11374 | same |
| /bali-tour-packages/ | 11376 | same |
| /dubai-tour-packages/ | 14234 | `.hx` country page (18 Oct 2026) — `pages/gen_dubai.py` (template for future country pages) |
| /georgia-tour-packages/ | 14841 | `.hx` country page (20 Oct 2026) — `pages/gen_georgia.py` (6-day itinerary grid = 3 columns on desktop) |
| /azerbaijan-tour-packages/ | 15017 | `.hx` country page (21 Oct 2026) — `pages/gen_azerbaijan.py` (6-day itinerary grid = 3 columns) |
| /turkey-tour-packages/ | 14629 | `.hx` country page (19 Oct 2026) — `pages/gen_turkey.py` (same template; 8-day itinerary grid = 4 columns) |

## Files
- `gen_hub.py` — builds the hub (`hub.html`, one line) from `photos/wp_map.json`. Edit copy here, rebuild, upload with `wp_update_page` (content), verify.
- `slides.py` — the CSS-only photo slideshow that sits inside a country page's `.sx-media` hero box (replaced the old green route-map videos).
- `photos/wp_map.json` — slug → WordPress media URL, alt, credit, licence, source page. `photos/credits.json` — full licence log.
- `pages/` — per-page sources/builds. `backups/` — rendered HTML before each change.

## Design rules
- One H1 = the theme title (`.page-header .entry-title`), restyled by page-scoped CSS (`body.page-id-N …`). On the hub it is absolutely positioned over the photo hero; the hero reserves `padding-top:236px` (desktop) / `206px` (≤700px) for it.
- `gen_dubai.py`/`gen_turkey.py` prune hub CSS with `_DROP`; a hub rule that shares a selector with a dropped class (e.g. `.hx-steps,.hx-why`) is lost — re-add it in `EXTRA` (fixed 19 Oct for `.hx-steps` mobile columns).
- Content must stay a single line (wpautop inserts `<p>`/`<br>` on new lines). Inline JS: no `&`, no `//`.
- Real photos only (Unsplash free licence, Pexels, Wikimedia CC0/BY/BY-SA, Suzu guest photos). Drawn/animated map graphics were rejected by Sushil (17 Oct 2026) as cheap-looking.
- Old green route-map media (`/wp-content/uploads/suzu-intl/*.mp4|webm|poster.webp`) are no longer referenced by the outbound pages; keep the files (other pages/links may use them).

## Verification
Playwright 1440 + 390 (no overflow, 0 broken images, one H1), links/media 200, live `?v=` and plain fetch. Hostinger bot-protection may show reCAPTCHA to headless Chromium after many requests — use curl or space the checks.
