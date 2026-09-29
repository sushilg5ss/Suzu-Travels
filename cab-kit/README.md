# Suzu Cab Kit v1.0 (30 Sep 2026)

Design system + content + build tool for every page under **suzutravels.com/cabs/** (hub = page **10080**, children have `post_parent` 10080).
Owner: Suzu Travels (Sushil Kumar). Used by the scheduled "Suzu Cab …" agents. Branch `cabs` of `sushilg5ss/suzu-travels`, folder `cab-kit/`.

## Files
| File | What it is |
|---|---|
| `cabs_data.py` | **Single source of truth**: fleet (rates), fare engine, `PLACES` (lat/lon for maps), `ROUTES` (every route card; `slug` set when a page exists), booking steps, inclusions. |
| `pages_content.py` | Copy for every child page (one dict per page: SEO fields, hero, answer, facts, stops, map, tips, FAQ, related links, WhatsApp text). |
| `hub.py` | The `/cabs/` hub page. |
| `build.py` | `python3 build.py [slug ...]` → `out/<slug>.html` + `out/<slug>.min.html` (ONE line, CSS inlined — this is what goes into WordPress). Refuses to build on a fare mismatch between `seo_title` and the engine, placeholders, or `&&` in JS. |
| `kit.css` | Styles, scoped to `.szc` (emerald #122615 / green #2E7D32 / gold #D4AF37, Plus Jakarta Sans). |
| `kit.js` | Fare calculator, quote form → WhatsApp, hub route finder. **Never use `&`/`&&` in it** (WordPress `convert_chars` turns `&` into `&#038;` and breaks JS) and no `//` comments. |
| `vehicles_svg.py` | Original flat vehicle illustrations (no third-party car photos). Published as `media/fleet/<id>.svg`. |
| `media.json` | jsDelivr URLs (pinned commit) for hero videos, route maps and fleet SVGs. |
| `live.json` | Slugs that are LIVE. Only live pages get "Route & fares" links; others show WhatsApp quote. |
| `gen_hero.py` | HyperFrames hero loop generator (parallax Himalaya, Suzu-branded car, page title). `VARIANTS` dict = one per page. |
| `gen_route.py` | HyperFrames route-map loop generator (path mode A→B via waypoints, or hub mode = spokes). Borderless map (no state/national borders drawn). |
| `research/kw_all.csv` | Google Ads Keyword Planner export (India, 30 Sep 2026) — 700+ cab/taxi keywords with monthly volume. |

## Fare rules (approved by Sushil on 30 Sep 2026 — prices ARE shown on cab pages)
- One-way = `max(min_fare, km × one-way rate × route factor)`, rounded up to …99. Rates/km: hatch 12, sedan 14, Ertiga 17, Carens 19, Crysta 24, Tempo 32, Urbania 42. Route factor: plains 0.85, mixed 1.0, hills 1.1, Leh/J&K 1.6–1.7.
- Round trip / tours: km × hire rate (hatch 11, sedan 12, Ertiga 14, Carens 16, Crysta 19, Tempo 26, Urbania 36), minimum 250 km/day, driver allowance ₹400/night (₹500 Tempo/Urbania).
- Included: AC car, fuel, driver, driver allowance. Extra at actuals: tolls, parking, state entry tax/permits. Peak dates cost more.
- Always write fares as "from ₹X" / "starts around" — indicative, confirmed on the WhatsApp quote. Change a rate only in `cabs_data.py`, rebuild, and republish every live page (the calculator, tables and copy must agree).
- Benchmarks used (Sep 2026): Delhi–Shimla sedan ₹4,500–5,500 one-way, Crysta ₹7,000–8,500 (trivenicabs 2026 guide); Chandigarh–Manali sedan ₹4,000–6,500, Crysta ₹9,500–11,000 (rajputanacabs, taxiyatri 2026); outstation per-km sedan ₹10–17, Innova ₹18–22, Tempo ₹26–32 (cabbazar Jul 2026); Manali union 2026: Solang 1,999/2,499/2,999, Atal+Sissu 2,999/3,499/4,999, Rohtang 3,999/4,999/6,999 (himalayan-routes).

## Business facts to use (never invent others)
- HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022 (link `/certificates/`), GST registered. Office NH 103, Kulahru, Tehsil Ghumarwin, Bilaspur HP. WhatsApp/phone +91 70874 88961.
- Rating phrase must be exactly `★ 4.7 · 377 Google reviews` (the Suzu Live Reviews plugin rewrites it site-wide).
- Manali (Solang/Atal/Rohtang) and Kashmir local sightseeing = locally registered union taxis; Suzu books them. Rohtang: online permit, closed Tuesdays. Himachal entry fee for non-HP vehicles (₹100/day up to 12 seats, 2026–27).
- Never claim fleet size, "verified/insured drivers", customer counts, awards or reviews that are not proven.

## Page anatomy (route page) — keep this order
Hero (per-page HyperFrames loop, title in video on the right) → sticky menu → `#overview` (answer-first 40–70 words + facts) → `#fares` (table for 7 vehicles + inclusions + calculator) → `#route` (route-map loop + stop-by-stop list) → `#cars` → `#tips` → `#booking` → `#quote` form (WhatsApp) + "Request a call back" (`#enquiry` opens the site-wide lead popup) → `#more` (route cards + related links) → `#faq` (+ FAQPage JSON-LD) + TaxiService JSON-LD (no prices/offers in schema).
City pages add a local-rates table and outstation table; vehicle pages add per-km rate tables.

## Media (HyperFrames)
- Hero: `python3 gen_hero.py <slug>` (add a `VARIANTS` entry) → `cd heroes/<slug> && npx -y hyperframes@0.8.85 render -o out/master.mp4` → ffmpeg to 1600 px `hero.mp4` (crf 28) + `hero.webm` (VP9 crf 40) + `poster.webp` (frame 0).
- Route map: add the page to `pages_content.py` with `map` (path + labels + ctx, or hub + spokes; every name must exist in `PLACES`) → `python3 gen_route.py <slug>` → snapshot (`npx hyperframes snapshot --at 6.5 --describe false`) and LOOK for label overlaps → render → 1280 px `route.mp4/.webm` + `route-poster.webp` (frame 6.5 s).
- Commit to `cab-kit/media/<slug>/` on branch `cabs`, pin the new commit SHA in `media.json`. Sources of each composition go to `cab-kit/compositions/<slug>/`.

## Publishing
- Build: `python3 build.py <slug> cabs`.
- New child page: WordPress REST or Royal MCP `wp_create_page` (parent 10080, content = `out/<slug>.min.html`), slug = the page slug, template default. Rank Math title/description/focus keyword via `wp_update_seo_meta`. Add the slug to `live.json`, rebuild the hub and update page 10080's content.
- Verify live twice (cache-busted and plain): 200, one H1, index robots, video plays, no horizontal overflow at 390 px, all links 200.
- Rollback for the hub: set `_wp_page_template` of 10080 back to `page-cabs.php` and empty the content (the old PHP template is untouched in the theme).

## LIVE STATE (30 Sep 2026, ~03:45 IST)
- Hub + 12 child pages are LIVE. WordPress IDs in `wp_ids.json`. Published from commit `c8b53a7` (content fetched from jsDelivr in the logged-in wp-admin tab, POST `/wp-json/wp/v2/pages`, saved raw content verified byte-identical).
- **HUB TEMPLATE GOTCHA:** the theme has `page-cabs.php`, and WordPress picks `page-{slug}.php` automatically when a page's template is "default" — so `/cabs/` kept rendering the OLD template with the new content appended at the bottom. Fix applied: `_wp_page_template` of 10080 set to `page.php` (via Royal MCP `wp_update_post_meta`), which forces the theme's normal page wrapper (H1 = page title). Do NOT set the hub template back to "default" through the editor/REST. Rollback = set it to `page-cabs.php`.
- After changing only post meta, WP Rocket does not purge — re-save the page (REST POST with the same title) to purge the cache.
- WP Rocket "Delay JS" is on: kit.js (calculator, route finder, quote form) runs after the first user interaction — expected. `moment is not defined` / `setSettings` / `feather is not defined` console errors are PRE-EXISTING site-wide (seen on /contact/ too), not from the kit.
- Rank Math titles/descriptions/focus keywords set on all 13 (see `out/meta.json`). Old hub SEO: title "Himachal Cab Booking | Delhi & Chandigarh Taxi | Suzu Travels", focus "cab booking himachal"; old hub title "Cab Booking".
- Old rendered hub saved in `backup/cabs-old-rendered-2026-09-30.html`.
