# Suzu Mountain Kit v1.1 (1 Oct 2026)

This kit is the design system, dataset, video pipeline and publishing toolkit for the **Mountains of India** section of suzutravels.com. It covers:
- `/mountains-of-india/` and its child pages
- the enquiry page `/adventure/himalayan-peak-expeditions/`

Owner: Suzu Travels (Sushil Kumar). The kit is built and run by the scheduled Suzu Mountain agents. Repo: `sushilg5ss/Suzu-Travels`, branch **`mountains`**, folder `mountain-kit/`.

**Goal (Sushil, 1 Oct 2026).** Rank worldwide for India-mountain searches, both informational ("highest peaks in India", "Friendship Peak", "IMF permit") and commercial ("peak climbing Himachal"). Turn that traffic into WhatsApp enquiries. Suzu arranges each climb with validated, authorised **Himachal** mountaineering companies. The pages stay **informational and neutral**: no partner is ever named. Every page gets striking **HyperFrames** visuals and must still load fast.

---

## 1. Business rules (non-negotiable)
1. **No prices of Suzu's.** Every price slot says "Get Quote". `build.py` refuses ₹, Rs and INR amounts.
   - Official **government / IMF fees in US$** may be stated as information, with the source and "as of" date.
2. **No partner names, and no network or team claims.**
   - Never name, hint at or describe the companies or people Suzu works with (camps, Gorkhas, "Everest summiteers").
   - Never write "our vendor network", "partner company", "our own guides" or "in-house guides".
   - The approved wording is: "we pair you with a registered Himachal outfitter and certified guides".
3. **Only Himachal climbs are sold** (`commercial: true`). Other states' peaks are information, and their CTA suggests Himachal climbs.
   - **Never sell Stok Kangri** (closed since 2020).
   - **Never sell Kanamo** until its access status is verified.
4. **Trust row** (the kit prints it): "HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022", linked to `/certificates/`.
   - Never write "registered DMC".
   - Phone / WhatsApp is **+91 70874 88961** only.
5. **Original copy, true facts.**
   - Every fact traces to the page's fact pack (`research/pages/<slug>.md`), where each fact has its source URL. The page lists the official and neutral sources; operator sites may back route logistics inside the fact pack only.
   - No copied competitor text.
   - No links to or mentions of competitor operators (`build.py` refuses the known ones).
6. **Photo honesty.** A photo may be labelled as a named peak only when `hf/photos/CREDITS.md` says it shows that peak.
7. **No Instagram / social posting.** The visual work goes on the website only.

## 2. Facts to avoid (they cost trust, and `build.py` catches some of them)
- **"Kamet was the first 7,000 m summit": wrong.**
  - Trisul (1907) was the first 7,000 m summit.
  - Kamet (1931) was the first summit above 25,000 ft.
- **Nanda Devi.** It has been closed since 1983. Only **Nanda Devi East** is on Uttarakhand's 2026 open list.
- **Kangchenjunga cannot be climbed from India.**
  - Sikkim Notification 70/HOME/2001 bans it.
  - The 2025 Indo-Nepal Army ascent went via Nepal.
- **Stok Kangri** is closed (2020 → no official reopening). **Kanamo:** access status conflicting, so verify it before any sales wording.
- **IMF fees.**
  - Base fees for a team of two are fine: US$200 (IMF-listed trekking peaks), US$500 (up to 6,500 m), US$700 (6,501–7,000 m), US$1,000 (above 7,000 m), plus US$500 LO equipment hire (IMF peak-fee page, checked 1 Oct 2026). Do not claim a particular peak is on the trekking-peak list unless the IMF says so.
  - Per-member figures differ between IMF pages, so write "per-member charges apply".
  - There is no national garbage deposit. There is no new national IMF portal or fee waiver: the 2026 change is Uttarakhand's UKMPS portal and state-fee waiver for Indians.
- **Visas.** A tourist visa covers open areas. The X (mountaineering) visa is for restricted areas. Always "confirm with the Indian mission".
- **Heights that vary by source.**
  - Hanuman Tibba 5,860–5,982 m.
  - Ladakhi 5,257–5,345 m.
  - Shitidhar 5,250–5,294 m.
  - Use the dataset value and mention the range once.
- **People.**
  - The first Indians on Everest were Avtar Singh Cheema and Nawang Gombu (20 May 1965).
  - Baljeet Kaur: use only the verified 2021–22 records and "seven 8,000 m peaks". There are no confirmed 2024–25 records.
  - "Youngest Indian on Everest": only "Arjun Vajpai was the youngest Indian at the time (2010)".
- **Kangra trekker registration** (8 Jul–15 Oct 2026) applies to ten Dhauladhar routes only. It is not a statewide rule.
- Full list with sources: `research/rules-records.md` §8.

## 3. Folder map
| Path | What |
|---|---|
| `data/peaks.json` | Canonical dataset (156 peaks). **Every height, count and year on a page comes from here.** Built by `data/build_data.py` from `peaks.research.json` + `additions.json` (new peaks) + `overrides.json` (fixes) |
| `data/india-peaks.csv` | Public download (CC BY 4.0), linked from the list page (pinned to a commit in `media.json` → `data`) |
| `research/` | Background research: `rules-records.md` (permits, rules, records, costs, safety, facts to avoid), `seo-plan.md` (keywords, URL plan, linking, schema), `kw/*.json` (Keyword Planner pulls), `pages/<slug>.md` (fact packs) |
| `BACKLOG.md` | Which page is next and its status (`todo → researched → media → live`) |
| `LOG.md` | One line per agent run, newest first: what changed, IDs, undo tokens, `FIX NEEDED` items |
| `live.json` | Every published page: `{slug: {id, path, kind, label, blurb, added, peak_id?, peak_ids?, state?, band?, commercial?}}` — drives all internal links |
| `media.json` | Pinned commit per media folder (and `data`) for jsDelivr URLs |
| `src/pages/<slug>.json` | One file per page (copy + structure). `_example-peak.json` = schema example (files starting `_` are never built) |
| `src/media/<slug>.json` | The page's video spec (hero / profile / ladder). Examples: `_example-peak.json`, `_example-guide.json` |
| `gen_pages.py` | Page generator: base pages (hub, list, expeditions) + `content_page()` for everything in `src/pages/` |
| `gen_media.py`, `make_media.sh`, `hf/` | HyperFrames compositions, render + encode script, fonts, photos (`hf/photos/CREDITS.md`) |
| `media/<slug>/` | Encoded videos + posters (served from jsDelivr) · `compositions/` = source of every render |
| `kit.css`, `kit.js` | Design system (scoped `.szm`) and the small page script (lazy videos, table filters/sort/search, hash links) |
| `build.py` | One-line minified build + quality gate |
| `tools/` | `sync_plan.py` (link updates on live pages), `chunks.py` (upload in chunks), `cmp_live.py` (live vs build), `preview.py` + `shots.js` (theme preview screenshots), `live_check.js` (live video/overflow/filter test) |
| `agents/` | The four agents' standing instructions (the scheduled prompts are copies of these) |

## 4. Pipeline (one page per day)
1. **Research** (Mon, Wed and Fri, 11:47 IST). For the next 3 `todo` rows:
   - write `research/pages/<slug>.md` (see `research/pages/README.md`);
   - run keyword research;
   - add data fixes or new peaks;
   - set the rows to `researched`.
2. **Visual Studio** (daily, 17:17). For the first `researched` row:
   - write `src/media/<slug>.json` and check the contact sheet;
   - render it (`make_media.sh`), push, then `pin_media.py <slug> <sha>`;
   - set the row to `media`.
3. **Page Builder** (daily, 19:37). For the first `media` row (or `researched`, rendering the media itself):
   - write `src/pages/<slug>.json`, build it, preview it, publish it;
   - set the Rank Math meta and add the page to `live.json`;
   - apply the link updates to the other live pages (`tools/sync_plan.py`) and verify;
   - set the row to `live`.
4. **SEO & QA** (Sun, Tue, Thu and Sat, 22:37):
   - check every live page and fix defects;
   - re-sync pages that drifted;
   - add internal links from the rest of the site;
   - clear `FIX NEEDED` entries.

## 5. Page file schema: `src/pages/<slug>.json`
**Required:**
- `path`: `/mountains-of-india/<slug>/`
- `title`: the WordPress title and H1, 45–70 characters with the height for peaks, e.g. "Friendship Peak (5,289 m), Manali: Climbing Guide"
- `kicker`, `tag` (the big hero line, which is **not** a heading), `sub` (one paragraph)
- `answer`: 40–70 words, answer-first, may contain internal `<a>` links

**Also expected:**
- `kind`: peak | band | state | guide. Add `peak_id` for a peak, which must exist in `data/peaks.json`.
- `seo_title`: 60 characters or fewer, no price words. `seo_desc`: 110–155 characters. `focus`.
- `commercial` (true only for sellable Himachal climbs).
- `label` + `blurb`: the tile text other pages show when linking here.
- `chips` [[bold, text] × 3–5], `q` (the overview H2 as a question)
- `faqs` (at least 5 real questions), `sources` (at least 3, official or neutral first)

**Optional sections** (appear in this order, each only if present):
1. `facts`: auto-filled from the dataset for peaks when left out
2. `intro`
3. `route` (+ `route_text`, `route_h2`): a camp table; the profile video sits beside it
4. `itinerary` [[day, title, text]]
5. `difficulty` + `skills`
6. `months` {Jan..Dec: good|maybe|no} + `season_text`
7. `table` {where{band/state/status}, min_m, max_m, ids[], h2, text[], label}: a filtered peak table; the ladder video sits beside the text
8. `permits`
9. `includes` + `cost_text`: "Price: Get Quote"
10. `gear`
11. `history`
12. `extra_sections` [{id, label, kicker, h2, html}]: original HTML using kit classes only
13. Nearby peaks (automatic for peaks)
14. Quote block (`quote_h2` / `quote_text` / `wa` override the defaults)
15. `faqs`
16. `links` (tile list; default hub / list / expeditions) + automatic related live pages
17. `sources`

Also: `sameAs` (Wikipedia/Wikidata URLs for the Mountain schema), `verified` (date shown in the badge; default 1 Oct 2026, so set today's date).

**Schema output:**
- a Mountain (peak pages)
- a TouristTrip (commercial pages, without offers or prices)
- a FAQPage

## 6. Media: HyperFrames (every page has at least one video, and `build.py` refuses a page without one)
**Compositions** (1920×1080, silent, seamless loops):

| Composition | Spec key | Content | Best for |
|---|---|---|---|
| `peak-hero` | `hero.steps` | Photo scenes with a rolling altitude read-out, road-head → summit | Peak pages |
| `peak-hero` | `hero.words` | Photo scenes with 4 big two-line statements | Guide pages |
| `route-profile` | `profile.camps` | Animated altitude profile, camp by camp (explainer) | Peak pages |
| `peak-ladder` | `ladder.peaks` | 3–7 dataset peaks drawn at their true heights (explainer) | Band, state and comparison pages |

**Commands:**
- `SNAP_ONLY=1 bash make_media.sh <comp> <slug> <hero|explainer>`: composition plus contact sheet only. **Read the printed `contact-sheet.jpg` before rendering.**
- `bash make_media.sh <comp> <slug> <hero|explainer> [poster-second]`: render and encode. Poster second: hero 0, profile 11, ladder 13.
- Then: `git add mountain-kit/media/<slug> mountain-kit/compositions mountain-kit/src/media/<slug>.json` → commit → push → `python3 pin_media.py <slug> $(git rev-parse HEAD)` → commit + push `media.json`.
- **Preview before pushing:** `MK_LOCAL_MEDIA=1 python3 gen_pages.py <slug>` points the videos at local files. `build.py` refuses such a build for publishing.

**Budgets and layout:**
- Hero: under 2.5 MB desktop and 1 MB mobile.
- Explainer: under 2 MB.
- Text stays in the right 55% of the frame, because the page's own tagline sits on the left.
- Scenes must tile the loop: the first starts at 0, each next one starts about 0.6 s before the previous ends, and the last ends at 14 s (steps) or 13 s (words).
- **Hosting:** videos are served from jsDelivr pinned to a commit, e.g. `https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@<sha>/mountain-kit/media/<slug>/hero.mp4`. The WordPress media library is for images only. Hero videos autoplay (preload=metadata, mobile gets the 960 w file); every other video lazy-loads.

## 7. Build, preview and publish
1. **Generate and build:**
   - `python3 gen_pages.py <slug>` → `out/<slug>.html`.
   - `python3 build.py <slug>` → `out/<slug>.min.html`. It is **one line**, which WordPress wpautop cannot break, with the CSS and JS inlined.
   - If the build refuses, fix the cause. Never publish a `--force` build.
2. **Preview:**
   - `python3 tools/preview.py <slug>` puts the page in the real theme.
   - `node tools/shots.js /tmp/mk-prev/<slug>.html <slug>` prints JSON and makes the slices. **Look at them** (Read the JPEGs) at desktop and phone width.
   - Required: `overflow: false`, `h1: 1`, videos present.
3. **Create the page** with `wp_create_page`: title = `title`, **parent 11831**, status publish.
   - Content: **up to 30,000 characters** is one call with the exact file contents. Bigger pages: create with the first chunk from `python3 tools/chunks.py <slug>`, then follow its recipe (`@@MKCONT@@` marker + `wp_replace_in_page`).
   - Then `wp_update_seo_meta`: `slug` = `<slug>`, title = `seo_title`, description = `seo_desc`, focus keyword = `focus`.
   - The URL must end up exactly `/mountains-of-india/<slug>/`.
4. **Verify the content:** `wp_get_page` → the stored content length must equal the file's byte size (`chunks.py` prints both). If not, write the content again.
5. **Record it** in `live.json`: `{id, path, kind, label, blurb, added: today, peak_id / peak_ids / state / band, commercial}`.
6. **Update the links on other pages:**
   - `python3 tools/sync_plan.py <slug>` gives a JSON list of small find/replace ops.
   - Apply each one in the order given: `wp_replace_in_page(id, find, replace, expected_count=1)`.
   - An op that finds 0 matches means that page is on an older template. Log `FIX NEEDED: full re-upload <slug>` and move on.
   - Pages listed under `"full"` get a full re-upload with `chunks.py`.
7. **Verify live:**
   - `python3 tools/cmp_live.py <slug>` for the new page and every touched page: 0 text / 0 attr diffs.
   - Also check with `--plain` (cached copy), plus one H1, robots `index` and the right title.
   - `node tools/live_check.js <url> /tmp/x.png 390 844`: the hero video plays (readyState ≥ 2) and there is no overflow.
8. **Commit** `src/`, `out/`, `live.json`, `BACKLOG.md` and `LOG.md`, then push.

## 8. WordPress traps (Royal MCP "Suzu Travels WordPress" connector)
- **One-line content.** Content must be exactly the one-line `.min.html`. Multi-line HTML gets `<p>`/`<br>` injected by wpautop.
- **WP Rocket:**
  - A content update purges the page cache; a meta-only change does not. To purge after meta changes, re-save the page with the same title.
  - Always check live twice, with `?v=<random>` and plain.
  - "Delay JS" means kit.js runs only after the first user interaction. Test filters and lazy videos after a mouse move or scroll. The site-wide console errors `moment is not defined`, `setSettings` and `feather is not defined` are pre-existing: ignore them.
- **Undo tokens.** Every Royal MCP write returns a 72-hour undo token; put it in LOG.md.
- **Hostinger bot protection** may show a reCAPTCHA to headless Chromium after many loads. Keep headless loads to a few per run and use curl for the rest.
- **Never:**
  - delete content, or change existing URLs or slugs;
  - touch the static homepage, menus, theme, plugins, PHP or .htaccess;
  - touch `/adventure/` pages other than 11846.
- **The Adventure hub (page 11529)** belongs to the Suzu Adventure squad. Its "Mountaineering" tile and `#act-peak-climbing` card were added by hand on 1 Oct 2026. If they disappear, re-add them with a targeted `wp_replace_in_page` and log it.
- **Mountain pages in the site sitemap.** Rank Math includes new pages automatically. The site-wide Indexing & Housekeeping agent handles indexing requests.

## 9. Quality gate (the SEO & QA agent checks every live page)
- **Status:**
  - HTTP 200 with and without the cache-buster.
  - One H1, the theme title.
  - `robots` includes `index`.
  - The canonical is the page URL.
  - The Rank Math title is 60 characters or fewer; the description is 110–155.
- **Content:**
  - `cmp_live.py` shows 0 text and 0 attr diffs against the current build.
  - The JSON-LD parses.
  - No ₹, no vendor names, no fact traps.
- **Links and media:**
  - Every internal link returns 200.
  - Every video and poster URL returns 200.
  - The hero video plays at 390 px.
  - No horizontal overflow at 390 and 1440 px.
  - The sticky menu anchors work.
- **Weight:** under 200 KB of HTML, and under 1.5 MB before video on first load.

## 10. Keyword owners (avoid cannibalisation)
| Page | Owns | Doesn't target |
|---|---|---|
| Hub `/mountains-of-india/` | "mountains in india" | "highest peaks" |
| List `/highest-peaks-in-india/` | "highest peaks / mountain in india" | – |
| `himachal-pradesh` | "peaks in himachal pradesh" | – |
| `reo-purgyil` | "highest peak in himachal" | – |
| `trekking-peaks` | "beginner / first 6000m / trekking peaks" | – |
| `6000m-peaks` / `7000m-peaks` | the band lists | – |
| `mountaineering-in-india` | "how to climb / foreigners" | – |
| `/adventure/himalayan-peak-expeditions/` | "peak climbing / expedition himachal" | – |

**Anchors:** use the exact focus keyword on at most about 30% of the links to a page, and never point two pages at the same exact anchor.

## 11. Live pages (1 Oct 2026)
| Page | ID | URL |
|---|---|---|
| Hub | 11831 | https://suzutravels.com/mountains-of-india/ |
| Highest peaks list (dataset) | 11841 | https://suzutravels.com/mountains-of-india/highest-peaks-in-india/ |
| Guided expeditions (enquiry) | 11846 (parent 11529) | https://suzutravels.com/adventure/himalayan-peak-expeditions/ |

Child pages are listed in `live.json`, and their history is in LOG.md.

## 12. The agents
| Agent | When (IST) | Job |
|---|---|---|
| Suzu Mountain Research & Data | Mon, Wed, Fri 11:47 | Fact packs for the next 3 pages, keywords, dataset upkeep, weekly status sweep |
| Suzu Mountain Visual Studio | Daily 17:17 | HyperFrames media for the next researched page; visual upgrades |
| Suzu Mountain Page Builder | Daily 19:37 | One new page per day, end to end |
| Suzu Mountain SEO & QA | Sun, Tue, Thu, Sat 22:37 | QA of every page, fixes, re-syncs, internal links from the rest of the site |

Their full instructions are in `agents/`. They commit as `Suzu Mountain Agent <info@suzutravels.com>` and push to `mountains` only (`git pull --rebase` first; never force-push). Reports go to Sushil in simple Hinglish, with full page URLs.
