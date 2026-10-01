# Mountain section — progress log (newest first; one line per agent run)

Format (take the time from `TZ=Asia/Kolkata date '+%F %H:%M'`, not from the schedule): `YYYY-MM-DD HH:MM IST · <agent> · what changed · page IDs · undo tokens · checks · FIX NEEDED: <who> — <what>`

- 2026-10-01 17:32 IST · Visual Studio · Media for 2 pages (BACKLOG → `media`):
  - `himachal-pradesh`: words hero (UP TO 6,816 m · 47 PEAKS OPENED · MAY–JUN / SEP–OCT · START IN MANALI) hero.mp4 2.06 MB / -m 0.78 MB; ladder (Reo Purgyil, Leo Pargial, Manirang, Mulkila, Indrasan, Deo Tibba, Friendship) 0.26 MB. Photos px-38930225, px-32109154, px-20809686, px-37358046. Pinned 90ab9c95749a.
  - `hanuman-tibba`: steps hero (2,050 Manali → 3,600 Beas Kund camp → 4,750 Tentu Pass → 5,050 summit camp → 5,982 summit) hero.mp4 1.53 MB / -m 0.59 MB; profile (7 camps, Day 1–9) 0.15 MB. Photos px-10254837 (NEW, Pexels 10254837, CAT logo, no mirror), px-38468349, px-20809686, px-9683997. Pinned 8e95bcfccc5d.
  - Contact sheets checked; jsDelivr 200 on hero / -m / explainer for both. No FIX NEEDED (media) open. Stok Kangri (`researched`) is next.
- 2026-10-01 19:30 IST · Claude (Sushil: gear/tools/utilities ki poori information bhi website pe banao) · **Gear & skills guide cluster added to BACKLOG** as rows 10–16, right after `mountaineering-courses`, so the daily pipeline builds them next week without any new agent:
  - mountaineering-gear-list · crampons-and-mountaineering-boots · ice-axe-guide · what-to-wear-himalayan-climb (layering) · expedition-camping · altitude-sickness · first-6000m-peak.
  - Keyword evidence pulled (Keyword Planner): crampons 165K ww, mountaineering equipment 74K ww, ice axe 27.1K ww, mountaineering gear 27.1K ww, mountaineering boots 14.8K ww; India: mountaineering course 1.6K, winter trek in india 1K, camping in himachal 390. Saved: research/kw/gear_in_2026-10-01.json.
  - Rules carried into the row notes: NO gear brand names, NO prices; rentals mentioned generically; ice-axe/self-arrest concept-level only with a safety note; altitude page cites the CDC with the not-medical-advice line.
  - Later ideas updated: winter-treks-in-india (kedarkantha 49.5K IN — coordinate with Adventure lane) and a mountaineering glossary added; the three promoted bullets removed.
- 2026-10-01 11:35 IST · Claude (Sushil: "Homepage pe bhi laga do") · **Static homepage menu done:**
  - `public_html/index.html` was edited via the Hostinger File Browser API in Sushil's Chrome: the "Mountains" dropdown li (`<!--szmnt-->`) went in after the Adventure li, and `<style id="szmnt-nav">` before `</head>`.
  - Size 353,318 → 355,506 bytes; read-back SHA-256 matches (c05b7e44c69e…).
  - Backup: `public_html/index.html.pre-mountains-menu-2026-10-01` (353,318 bytes, sha 13d736d56ca7…). Rollback = copy it back over index.html.
  - Live (hcdn DYNAMIC, no purge needed). From 1181 to 1920 px: 11 items on one row, right-hand buttons fully on screen (they were cut at 1440–1536 px before). Mobile menu shows Mountains.
- 2026-10-01 10:55 IST · Claude (Sushil asked: "Mountains of India ka header pe link / menu button") · **Header menu, WordPress pages:**
  - **Menu 5 "Primary Menu".** New top-level item **"Mountains"** (11958 → /mountains-of-india/) after Adventure. Its dropdown:
    - Mountains of India (11959)
    - Highest peaks in India (11960)
    - Friendship Peak (5,289 m) (11961)
    - Guided peak climbs (11962)
  - **Adventure dropdown.** New item "Peak climbing & mountaineering" (11963 → /adventure/himalayan-peak-expeditions/).
  - **Order.** Reordered (undo d60a28aab065c2f08692657d5bed95f2).
  - **Additional CSS.** A block appended AFTER the Design Agent's END marker (undo d30b137d283f903bd0cdbfc1067fccc6) tightens the desktop nav so 11 items fit beside the phone and Enquire buttons:
    - 1181–1299 px: link padding 5 px, 12.5 px text;
    - ≥ 1300 px: padding 6 px, 13 px text;
    - header side padding 24 px.

    Checked at 1200/1280/1440: one row, 17–69 px clear of the buttons. The mobile drawer gets a "Mountains" section with the 4 links.
  - **WP Rocket.** Menu edits through the connector do not purge the cache: a nav_menu term re-save (undo c86ba0b42d5dda4416a9ac2f82bc1ceb) did not purge either, so "Clear and Preload Cache" was clicked in wp-admin. All pages now serve the new header.
  - **Static homepage** (public_html/index.html, its own hand-coded nav): NOT changed. The edit through Hostinger File Manager was blocked by the permission check, so it waits for Sushil.
    - Tested snippet: `site/homepage-nav-mountains.html`.
    - It also fixes the homepage's existing cut-off of the right-hand buttons at 1440–1536 px.
  - Menus stay human-only for the agents.
- 2026-10-01 10:40 IST · Claude (setup with Sushil) · Dataset re-sync and a public-dataset rule fix:
  - **Dataset re-sync.** The research run's dataset changes went live on list page 11841 (129,340 → 129,476) with 6 targeted ops from `sync_plan.py --rebuild`: Hanuman Tibba first ascent 1912 (row, data-fa, note), and the CSV re-pinned to b5c19c0 in all 3 places (hero button, method link, Dataset JSON-LD). `cmp_live` 0/0 (cache-buster + plain). Stok Kangri's new status note is not shown on the list page, so nothing changed there.
  - **Rule fix.** The research run had put an operator site (trekthehimalayas) in Stok Kangri's dataset sources, which flow into the public CSV. It was removed. `data/build_data.py` now drops operator domains (the `build.py` COMPETITORS list) from dataset sources and prints a warning.
  - **Kit.** The TouristTrip schema name on non-peak pages now defaults to "Guided Himalayan peak climbs from Himachal" (override with `trip_name`). Live pages are unchanged.
- 2026-10-01 10:15 IST · Claude (setup with Sushil) · Final QA + two fixes:
  - **Final QA:** `cmp_live` 0/0 on all 4 pages (cache-buster + plain); `linkcheck`: 93/94 URLs 200, CDC blocks bots but the page is fine (checked with WebFetch); 390 px: heroes play, no overflow.
  - **Kit v1.2, mobile hero crop:** `.szm-hero video,.szm-hero .bgimg{object-position:15% 50%}` at ≤ 640 px. On phones the video's right-side captions were showing half-cut ("FRIENDSH…") behind the page text. Applied live with one targeted `wp_replace_in_page` each on 11831 (69,456 → 69,513), 11841 (129,283 → 129,340), 11846 (55,088 → 55,145) and 11920 (39,975 → 40,032, equal to the build). Verified by the rule served live, `cmp_live` 0/0 and 390 px screenshots.
  - **Hostinger bot challenge:** a burst of about 60 curl requests made the site answer this container's IP with 403 "Checking your browser" to any request sending `Accept-Encoding`. Real browsers (headless Chromium) still load fine.
    - New `tools/linkcheck.py`; `cmp_live.py` waits and retries, then exits 3.
    - README §8/§9, shared rules and SEO & QA steps updated; all 4 scheduled task prompts updated to match `agents/*.md`.
- 2026-10-01 10:05 IST · Research & Data · Kick-start re-fire: rows 2–4 (himachal-pradesh, hanuman-tibba, stok-kangri) were already researched at 10:04 in the same session, so nothing was repeated (capacity rule). Rows 5–7 (deo-tibba, yunam-peak, imf-permit-fees) are left for the Fri 2 Oct run.
- 2026-10-01 10:04 IST · Research & Data · Fact packs: `himachal-pradesh`, `hanuman-tibba`, `stok-kangri` → researched (keywords: research/kw/pages_2026-10-01.json, 3 geos; ~22 sources checked). No `FIX NEEDED` (data) open; not Monday, no status sweep.
  - Dataset (overrides.json → build_data.py): Hanuman Tibba first ascent 1912 (Bruce's guide Führer and party, HJ 25 1964) + notable/sources; Stok Kangri status_note now cites the 21 Dec 2023 Ladakh administration order (The Statesman) on top of the 2020 ALTOA halt.
  - Found: Hanuman Tibba height still disputed (Survey of India point 19,450 ft ≈ 5,928 m; itineraries 5,932 m; dataset/Wikipedia 5,982 m) — kept 5,982 m, range stated once.
  - ~~FIX NEEDED: SEO & QA — re-upload highest-peaks-in-india (dataset changed) and re-pin the CSV.~~ Done at 10:40 IST by Claude (see the entry above).
- 2026-10-01 09:45 IST · Claude (setup with Sushil) · **Four Suzu Mountain agents scheduled** (cloud, automatic approval; prompts = `agents/*.md` + shared rules):
  - Research & Data, Mon/Wed/Fri 11:47 · `trig_011guuR4Cj49yiQcxSZbRFtg`
  - Visual Studio, daily 17:17 · `trig_01GJzzhGutGknu8iP33PfX7v`
  - Page Builder, daily 19:37 · `trig_011o83qJ3nDkWCi4kqVDEGXN` (push + email on finish)
  - SEO & QA, Sun/Tue/Thu/Sat 22:37 · `trig_019E5tsYSkuQUL6hiP4NrMrV`

  Kick-start: Research fired once today (Thu) for BACKLOG rows 2–4 (himachal-pradesh, hanuman-tibba, stok-kangri), so today's Visual Studio and Page Builder runs have researched pages. README §12 now lists the task IDs.
- 2026-10-01 05:05 IST · Claude (first pipeline run, end to end) · **Friendship Peak LIVE:** https://suzutravels.com/mountains-of-india/friendship-peak/ (page **11920**, parent 11831).
  - Fact pack, and media (hero 1.83 MB + mobile 0.65 MB, route profile 0.14 MB) pinned at 8e1bcb9.
  - Content 39,975 bytes, 2 chunks, stored length verified.
  - Rank Math: slug, title, description and focus set (undo b13b290ff62a264093edeaecc40ed618).
  - Sync ops applied: hub 11831 (Peak guides group + band link), list 11841 (row name link), expeditions 11846 (tile + "Route guide").
  - Also IMF fee wording fixed: US$200 IMF-listed trekking peaks / US$500 up to 6,500 m (hub ×2, expeditions ×3). `.szm-gh` / `.szm-crumbs` CSS inserted on hub and list.
  - `cmp_live`: 0/0 on all 4 pages (cache-buster and plain). 390 px: hero plays, no overflow.
  - Kit: content pages now inline only the CSS rules they use (about 11.6 KB instead of 21 KB); sync_plan splits long text into words (small ops).
- 2026-10-01 04:25 IST · Claude · Dataset CSV re-pinned to d12f4fc (includes the public-wording overrides). Page 11841: the CSV URL updated in all 3 places (hero button, method link, Dataset JSON-LD) via `wp_replace_in_page`; length stays 128,910. `cmp_live`: 0/0 with cache-buster and plain.
- 2026-10-01 04:10 IST · Claude (setup with Sushil) · Kit v1.1 for the agents:
  - generic page template `content_page()` for `src/pages/*.json` + media specs in `src/media/`;
  - new HyperFrames compositions: words hero, peak ladder (any 3–7 dataset peaks), route profile fixes;
  - automatic internal links from `live.json` (hub groups, list-row name links, band/state guide links, expeditions tiles, sibling tiles);
  - `tools/` (sync_plan, chunks, cmp_live, preview, shots, live_check);
  - build gate: fact traps, competitor links, video required, SEO lengths.

  The 3 base pages were regenerated byte-identical to what is live (`cmp_live`: 0/0 diffs).
- 2026-10-01 03:10 IST · Claude · Mobile hero fix on 11831 / 11841 / 11846: chips 4+ hidden under 640 px, so the CTA is above the fold (targeted `wp_replace_in_page`).
- 2026-10-01 02:55 IST · Claude · Adventure hub 11529 (owned by the Adventure squad), two manual edits:
  - "Mountaineering" category tile → `/mountains-of-india/`, after "Treks & Camps";
  - card `#act-peak-climbing` "Peak climbing (5,000–6,500 m)" → `/adventure/himalayan-peak-expeditions/` + WhatsApp Get Quote, before `#act-triund-trek`.

  Content went 77,922 → 79,144 bytes. Re-add these if a hub regeneration drops them.
- 2026-10-01 02:40 IST · Claude · PUBLISHED three pages. Verified live: 0 text / 0 attr diffs, 1 H1, index, canonical OK, videos play (desktop and 390 px), table filters work after interaction.

  | Page | ID | Parent | Undo tokens | Rank Math focus |
  |---|---|---|---|---|
  | `/mountains-of-india/` | 11831 | — | 993588b9d9ff550890a919416250484b, b1c02e7102e0bd0ba8f0bef95b1501ff | "mountains in india" |
  | `/mountains-of-india/highest-peaks-in-india/` | 11841 | 11831 | 837bb84045d16f6fb457fed6bb25fd5a | "highest peaks in india" |
  | `/adventure/himalayan-peak-expeditions/` | 11846 | 11529 | 5650d8c9a1e703e7f1249cf5ff8ba300 | "peak climbing himachal" |
- 2026-09-30 → 10-01 · Claude:
  - research: `rules-records.md`, `seo-plan.md`, Keyword Planner pulls, 156-peak dataset (`data/`);
  - HyperFrames renders: hub hero, height ladder, expeditions hero (commit 959eded).
