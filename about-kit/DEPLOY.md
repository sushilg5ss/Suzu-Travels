# About Suzu Travels — cinematic redesign (LIVE 14 Oct 2026, ~00:20 IST)

**URL:** https://suzutravels.com/about-suzu-travels/ (WordPress page **9964**; /about-us/ still 301s here)
**Source:** repo `sushilg5ss/suzu-travels`, branch `about`, folder `about-kit/` (commit 37436ba). Media + fonts served from jsDelivr pinned to commit 0b77c5e.

## What changed on WordPress
1. Page 9964 content = `out/about.min.html` (150,338 bytes, one line, SHA-256 05274fee…). Written through the REST API from the logged-in browser; the stored raw content was read back and matched byte-for-byte.
2. `_wp_page_template`: `suzu-team-members/about-page-template.php` → default (`""`).
3. Deleted post meta `_elementor_edit_mode` (= "builder"). With it set, the theme hid the page H1 and the content wrapper. The page never had real Elementor content.
4. Rank Math: title "About Suzu Travels | Himachal Travel Agency & DMC Since 2019" (60), description (143), focus keyword "suzu travels", new OG title/description. Undo token (72 h): 5603cc9ae5878e2536fde43b73cc4e1d.
5. 13 new portrait crops uploaded to the media library (IDs 13233–13248, `/wp-content/uploads/2026/10/suzu-team-*.webp`).

## Rollback (2 minutes)
- Set `_wp_page_template` back to `suzu-team-members/about-page-template.php` (Royal MCP `wp_update_post_meta`, or Page Attributes → Template). The plugin template ignores post content, so the old page returns as it was.
- Optional: re-add `_elementor_edit_mode` = `builder` and empty the content.

## Page sections
Hero film (HyperFrames, 16 s seamless Himalaya dawn loop; 1.15 MB desktop / 0.42 MB phone) · chapter nav · Our story (answer-first "Who is Suzu Travels?" + fact file) · Journey film strip 2019–2026 · The crew (27 s credits film + 13 cards; filters: department + Team Pathfinder / AutoPilot / Phoenix) · India network map (official boundary, 36 states coloured; HQ → 12 partner-city arcs; "Where we travel" toggle with 13 linked destinations) · 8 departments · B2B partners · Google reviews strip (live rating from /suzu-reviews.json) · feedback · 9 FAQs · final CTA.

## SEO / AEO / GEO
- One H1 (theme title, styled into the hero). H2 per section, answer-first paragraph for "Who is Suzu Travels?".
- JSON-LD: AboutPage + TravelAgency (founding date, founder, address, geo, HP Tourism credential, GSTIN, languages, sameAs) + 13 Person (jobTitle, image, languages) + FAQPage (9 Q&A) + VideoObject. All parse on the live page, alongside Rank Math's own graph.
- 21 internal links (destinations, DMC pages, certificates, packages, cabs, pilgrimage, international) — all 200.

## Checks done (live)
200 with and without cache-buster · 1 H1 · no horizontal overflow at 1440 and 390 px · `<script nowprocket>` survives WP Rocket (not delayed) · JSON-LD valid · all media 200 · no prices, no "registered DMC", no review-filter wording.

## Open items for Sushil
- Purvi Thakur's card shows **Pooja.thakur@suzutravels.com** — copied from the old page; probably wrong. Send the right address and it is a one-line fix in `team.py`.
- Partner counts by city (Delhi 40+, Chandigarh 30+…) and the timeline milestones are taken from the old page — confirm or update.
- If someone joins or leaves: edit `src/team.py`, re-crop the photo, rebuild the page (and re-render the crew film with `gen_crew.py`).
