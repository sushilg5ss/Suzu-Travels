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
| /japan-tour-packages/ | 15226 | `.hx` country page (22 Oct 2026) — `pages/gen_japan.py` (8-day itinerary grid = 4 columns) |
| /europe-tour-packages/ | 15476 | `.hx` multi-country page (23 Oct 2026) — `pages/gen_europe.py` (10-day itinerary grid = 5 columns) |
| /switzerland-tour-packages/ | 15679 | `.hx` country page (24 Oct 2026) — `pages/gen_switzerland.py` (8-day itinerary grid = 4 columns) |
| /mauritius-tour-packages/ | 15809 | `.hx` country page (25 Oct 2026) — `pages/gen_mauritius.py` (6-day itinerary grid = 3 columns) |
| /uk-tour-packages/ | 15961 | `.hx` country page (26 Oct 2026) — `pages/gen_uk.py` (London + Scotland; 8-day itinerary grid = 4 columns) |
| /egypt-tour-packages/ | 16112 | `.hx` country page (27 Oct 2026) — `pages/gen_egypt.py` (Cairo + Nile cruise + Luxor; 8-day itinerary grid = 4 columns) |
| /australia-tour-packages/ | 16306 | `.hx` country page (28 Oct 2026) — `pages/gen_australia.py` (Australia + New Zealand add-on; 8-day itinerary grid = 4 columns) |
| /uzbekistan-tour-packages/ | 16490 | `.hx` country page (29 Oct 2026) — `pages/gen_uzbekistan.py` (Tashkent–Samarkand–Bukhara–Khiva; 8-day itinerary grid = 4 columns) |
| /kazakhstan-tour-packages/ | 16997 | `.hx` country page (31 Oct 2026) — `pages/gen_kazakhstan.py` (Almaty + Kyrgyzstan add-on; 6-day itinerary grid = 3 columns; first page with Wikimedia Commons photos — per-photo licence in credits) |
| /armenia-tour-packages/ | 17234 | `.hx` country page (1 Nov 2026) — `pages/gen_armenia.py` (Yerevan–Garni/Geghard–Sevan/Dilijan–Khor Virap/Noravank–Tatev; 6-day itinerary grid = 3 columns; Wikimedia Commons photos) |
| /hong-kong-tour-packages/ | 21727 | `.hx` country page (13 Nov 2026) — `pages/gen_hongkong.py` (Hong Kong + Macau; 6-day itinerary grid = 3 columns; Wikimedia Commons photos; extra phone hero padding for the 3-line title) |
| /china-tour-packages/ | 22271 | `.hx` country page (14 Nov 2026) — `pages/gen_china.py` (Beijing–Xi'an–Shanghai + Zhangjiajie/Guilin add-ons; 8-day itinerary grid = 4 columns; 7-photo gallery = first photo spans 2 columns, 1 row; Wikimedia Commons photos) |
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

## Notes (31 Oct 2026)
- Hostinger returned 503 on ~40–60% of requests (GET and MCP writes) during the 31 Oct run; writes that 503 were NOT applied (checked with dry_run) — retry sequentially with pauses, never in parallel, and check `kazakhstan-tour-packages` counts before re-inserting cards.
- Commons photos: search via `commons.wikimedia.org/w/index.php?search=…&ns6=1` HTML (the API is rate-limited), licence/author from the File: page, upload the `upload.wikimedia.org/…/thumb/…/1920px-…` URL (or the original if <1920 px).

## Notes (1 Nov 2026)
- Commons thumbnails from the sandbox: the robot policy returns 429 for fast/odd-size thumb requests — use standard widths (330/500/1920), ~10 s apart, descriptive UA; WordPress itself fetched the 1920px thumbs fine.
- MFA Armenia visa-check tool: POST https://www.mfa.am/en/check-visa-needing with _token (from /en/visa/ page + cookie), country=IN, docutype=1 returns the official India text.

## Verification
Playwright 1440 + 390 (no overflow, 0 broken images, one H1), links/media 200, live `?v=` and plain fetch. Hostinger bot-protection may show reCAPTCHA to headless Chromium after many requests — use curl or space the checks.

## Notes (2 Nov 2026)
- Hub has a comparison table (`#compare-destinations`, `COMPARE` in `gen_hub.py`). When a new country page goes live, add a row to COMPARE (entry line + its official check date, typical trip, best season from the fact box) as well as to WHEN.

## Notes (4 Nov 2026)
- `.sx` galleries: `pages/gen_sx_gallery.py <country>` builds a one-line `<section id="<country>-in-photos" class="sx-sec sxg">` (own scoped CSS; credit `p` rule uses `.sx .sxg p.sxg-cr` to beat `.sx .sx-sec>p`). Insert it before the 2nd `<section` of the page and add a TOC link "Photos". Thumbs use WP sizes (`-1024x683` etc.) — check each size URL returns 200 before building.
- Commons from the sandbox: File: pages escape `_` as `&#95;` in the licence markup; thumb requests often 429 — 960/1280 px worked when 330/500 did not.

## Notes (13 Nov 2026)
- Commons thumbnails from the sandbox returned 429 for every request this run; WordPress `wp_upload_media_from_url` fetched the 1920px thumbs fine, so photos were uploaded first and then viewed from the WP copy (dropped ones stay unused in the library: 21712 B&W crowded Ruins of St. Paul's, 21720 tram with an ad showing people).
- `wp_create_preview_link` URL redirected headless Chromium to the homepage — use a local render (theme-less wrapper) before publishing, then test live.
- Long page titles (3 lines on phones) need extra `.hx-hero` top padding on that page (see gen_hongkong.py).

## Notes (14 Nov 2026)
- Commons API (commons.wikimedia.org/w/api.php) and api.wikimedia.org returned 429 after 1–3 requests; spacing 20–45 s worked slowly. `api.wikimedia.org/core/v1/commons/search/page?q=…` (search) and `/core/v1/commons/page/<File:…>` (wikitext → licence template + author) were the usable routes. WebFetch was blocked (permission prompt unanswered).
- Big page bodies: create the page as a draft, then send content in ~13–18 KB chunks — `wp_update_page` with a marker at the end, then `wp_replace_in_page` marker → next chunk + next marker (expected_count 1). `content_length` returned by the tool is UTF-8 bytes — compare with `len(s.encode())` of the local build.
- Hub: local `hub.html` is 22 bytes longer than the live hub content (pre-existing drift before this run; all 8 China edits applied cleanly with expected_count 1).
