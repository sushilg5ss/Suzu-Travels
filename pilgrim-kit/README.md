# Suzu Pilgrim Kit v1.0 (8 Oct 2026)

Design system, dataset, video pipeline and publishing toolkit for the **Pilgrimage Tours (Tirth Yatra)** section of suzutravels.com:
- hub `/pilgrimage-tours/` (the "Devotional" button on the homepage and in the header menu points here)
- guides `/pilgrimage-tours/<slug>/` (circuits, yatras, Himachal temples)
- Jyotirlinga temple pages `/pilgrimage-tours/12-jyotirlinga/<temple>/` (WordPress parent = the 12 Jyotirlinga page)

Owner: Suzu Travels (Sushil Kumar). Built by Claude with Sushil on 8 Oct 2026; run daily by the scheduled **Suzu Pilgrim** agents. Repo `sushilg5ss/Suzu-Travels`, branch **`pilgrimage`**, folder `pilgrim-kit/`.

**Goal (Sushil, 8 Oct 2026).** A world-class devotional section: every famous temple and yatra in India researched, with its story told beautifully (motion graphics, HyperFrames visuals), darshan timings, dates, how to reach, itineraries and FAQs — built for SEO so pages keep getting indexed and new pages keep coming, with **no copyright risk** and **no dependency on Sushil**. Traffic turns into WhatsApp enquiries that Suzu plans as packages.

---

## 1. Business rules (non-negotiable)
1. **No Suzu prices on these pages.** Every price slot says "Get Quote". `build.py` refuses ₹ / Rs / INR amounts. Bookable packages already exist on the site (with their own prices) — link to them (`PKG` in `gen_pages.py`), never compete with them (see §9 keyword owners).
2. **Facts.** Every date, timing, distance and rule comes from `data/*.json` or the page's fact pack `research/pages/<slug>.md`, each with its source URL and `as_of` date. Official sources first (temple trusts, shrine boards, state government, PIB), then major news, then Wikipedia. If a timing is not published officially, say "confirm locally" — **never guess**. Dates that are not yet announced are written as "not announced yet" (with the usual pattern), never invented.
3. **Legends** are retold in our own words as tradition ("according to the Shiva Purana…", "it is believed…"), never as history. Where traditions disagree (Vaidyanath, Nageshwar, Bhimashankar, Shakti Peeth lists, body parts) say so neutrally.
4. **Copyright.** No copied text (paraphrase everything), no song lyrics, no modern copyrighted bhajans/aartis (classical Sanskrit stotras are public domain), no photos without a licence that allows commercial use. **Visuals are original illustrated motion graphics** made by `gen_media.py` (temple archetypes drawn in SVG), so there is nothing to license. Never caption an archetype as an exact likeness of a temple.
5. **Trust row** (the kit prints it): "HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022" → `/certificates/`. Never write "registered DMC". Phone / WhatsApp **+91 70874 88961** only. Office: Bilaspur district, Himachal (Naina Devi is in our home district — a genuine local angle).
6. **Safety and respect.** Always point to the official registration / helicopter site (only `heliyatra.irctc.co.in` for Kedarnath; `online.maavaishnodevi.org`; SASB for Amarnath; `registrationandtouristcare.uk.gov.in` for Char Dham). Warn about fake booking sites. Mention age/health rules where they exist. No fear-mongering, no caste or communal content, no claims that a temple "grants" anything.
7. **No social posting.** Website only.

## 2. Facts to avoid (build.py catches some)
- Kedarnath opened **22 Apr 2026** (not on Akshaya Tritiya, 19 Apr). Yamunotri & Gangotri 19 Apr; Badrinath **23 Apr** (not 24).
- 2026 Char Dham closing dates: Badrinath's is announced on **Vijayadashami, 20 Oct 2026**; Kedarnath & Yamunotri close on Bhai Dooj, Gangotri on Annakut (~10–11 Nov) — only state exact dates once officially announced (post 12021 owns that topic).
- Amarnath 2026 ran **3 Jul – 28 Aug** (57 days); **no helicopter service in 2026** (no-fly zone); 2027 dates not announced. Age 13–70, CHC, RFID.
- **Vaishno Devi is not in the classical 51** Shakti Peeth lists; Chamunda is not a classical peetha either; Chintpurni's body part is disputed.
- Jwala Ji's flames are natural gas (ONGC drilled exploratory wells from 1957) — give tradition and geology side by side.
- Sharad Navratri 2026 starts **11 Oct** (not 22 Sep); Chaitra Navratri 2027 starts 7 Apr; **Mahashivratri 2027 = 6 Mar**.
- Mahakal Bhasma Aarti: online booking; since June 2026 one booking per mobile number every 90 days; the ash is no longer from funeral pyres.
- Bhimashankar was closed 9 Jan – 14 Jun 2026 for works.
- Shrikhand Mahadev 2026 yatra was **suspended** (29 Jun 2026). Manimahesh 2026: 25 Aug – 19 Sep, e-pass, ~5,000/day.
- Haridwar Ardh Kumbh 2027: 14 Jan – 20 Apr 2027 (Amrit Snan 6 Mar, 8 Mar, 14 Apr).
- Full lists: `research/*-notes.md` → "FACT TRAPS".

## 3. Folder map
| Path | What |
|---|---|
| `data/jyotirlinga.json`, `data/shaktipeeth.json`, `data/yatras.json` | Research datasets (12 + 28 + 23 records) with sources and `as_of`. **Source of truth for facts.** |
| `data/jl_display.json` | Clean display values (hours, aarti, best months, airport, rail, tip) for the 12 Jyotirlinga page |
| `research/` | Research notes (`*-notes.md`), `keyword-plan.md` (hub + 40 child pages, focus keywords + volumes), `site-inventory.md` (existing URLs that own keywords), `keywords.csv`, and `pages/<slug>.md` fact packs |
| `BACKLOG.md` | Which page is next and its status (`todo → researched → media → live`) |
| `LOG.md` | One line per agent run, newest first |
| `live.json` | Every published page — drives internal links |
| `media.json` | Pinned commit per media folder (and `fonts`) for jsDelivr URLs |
| `src/meta.json` | SEO meta of the two base pages |
| `src/pages/<slug>.json` | One file per content page (copy + structure) — see §5. `_example-temple.json` is the model |
| `src/media/<slug>.json` | The page's video spec (`hero` / `story` / `route`) |
| `gen_pages.py` | Hub + 12 Jyotirlinga page (functions) + `content_page()` for everything in `src/pages/` |
| `gen_media.py`, `make_media.sh`, `hf/` | HyperFrames compositions (illustrated temple archetypes), render + encode script, fonts (OFL) |
| `media/<slug>/` | Encoded videos + posters (served from jsDelivr) · `compositions/` = source of every render |
| `kit.css`, `kit.js` | Design system (scoped `.szp`, "diya & dusk" palette) and page script (lazy video, story reveal, map of light, table filters, menu highlight) |
| `build.py` | One-line minified build + quality gate |
| `tools/` | `sync_plan.py`, `chunks.py`, `cmp_live.py`, `linkcheck.py`, `preview.py`, `shots.js`, `live_check.js` (same as the mountain kit) |
| `agents/` | The four agents' standing instructions (the scheduled prompts are copies of these) |

## 4. Pipeline (one new page per day)
1. **Research & Data** (daily 14:17 IST) — fact packs for the next 2 `todo` rows (`research/pages/<slug>.md`), keyword check, date re-checks (Char Dham closing, Amarnath 2027, Navratri, Kumbh) → rows `researched`.
2. **Visual Studio** (daily 18:07) — `src/media/<slug>.json` + render (`temple-hero`, optionally `story-strip` / `route-map`), push, pin → row `media`.
3. **Page Builder** (daily 20:47) — `src/pages/<slug>.json`, build, preview, publish, Rank Math meta, live.json, sync links into the hub and siblings, verify → row `live`.
4. **SEO & QA** (Mon, Wed, Fri 22:37) — quality gate on every page, fixes and re-syncs, date refreshes, one contextual internal link per run from an existing non-Elementor post into this section.

## 5. Page file schema: `src/pages/<slug>.json`
**Required:** `path` (`/pilgrimage-tours/<slug>/` or `/pilgrimage-tours/12-jyotirlinga/<temple>/`), `parent` (WP page id of the hub or 12-JL page — see §11), `kind` (temple | yatra | circuit | guide), `title` (H1, 45–70 chars), `seo_title` (≤ 60), `seo_desc` (110–155), `focus`, `label` + `blurb` (tile text), `kicker`, `deva` (Devanagari name), `tag` (hero line, not a heading), `sub`, `q` (overview H2 as a question), `answer` (40–70 words, answer-first, may contain links), `faqs` (≥ 5 `[q, a]`), `sources` (≥ 3 `[title, url]`), `verified` ("9 Oct 2026").

**Optional, rendered in this order when present:** `chips` [[bold, text]×3–5] · `facts` [[big, small]×4] (stat tiles) · `intro` [paragraphs] · `story` {h2, lead, beats [[title, text]×4], more [paragraphs]} (dark section; the `story` video is used if `src/media/<slug>.json` has one) · `darshan` {h2, rows [[label, html]], note} · `dates` {h2, rows [[what, date, status/source]], note} · `route` {h2, lead, stops [[distance/day, title, deva, text]], note} · `reach` {h2, cards [[title, text]]} · `itinerary` {h2, days [[n, title, text]]} · `tips` {h2, items [[title, text]]} · `extra_sections` [{id, label, kicker, h2, html, cls}] (kit classes only) · `packages` [keys of `PKG`] · `quote_h2` / `quote_text` / `wa` · `links` [live slugs] · `place` {name, alt, town, state, lat, lon, type: HinduTemple|PlaceOfWorship, sameAs[]} · `trip_name` (TouristTrip, no offers) · `media_slug`.

**Schema output:** Article + HinduTemple/PlaceOfWorship (if `place`) + TouristTrip (if `trip_name`) + FAQPage.

## 6. Media (every page has a HyperFrames hero; build.py refuses a page without a video)
| Composition | Spec | What it shows |
|---|---|---|
| `pilgrim-hero` | fixed | Hub hero: Kedarnath in snow → Somnath by the sea → Kashi ghats → Devi hill shrine, Devanagari words |
| `light-map` | fixed (data) | The 12 Jyotirlingas light up at their true lat/lon (no borders drawn — never draw India's outline) |
| `temple-hero` | `hero` {arch, deva, kicker, beats[3–4, ≤8 words], sky?} | One illustrated temple + its story in 4 beats |
| `story-strip` | `story` {title, beats[{arch, line}]×4} | Legend told across 4 illustrated scenes (16 s) |
| `route-map` | `route` {title, sub, stops[{name, deva, state, lat, lon}]} | A yatra's stops lighting up (Nau Devi, Char Dham, Panch Kedar…) |

Archetypes (`arch`): `himalaya` (Kedarnath-style stone temple in snow), `nagara` (curved shikhara by the sea), `ghats` (river ghats with diyas), `devi` (hill shrine with flags), `gopuram` (south-Indian tower), `cave` (mountain cave with ice lingam), `pillar` (pillar of light), `gurudwara`, `pagoda` (Himachal hill temple — stacked wooden roofs, brass finial, deodars, snow ridges; for Hidimba / Bhimakali-type temples; caption it as a Himachal-style temple, not a likeness; added 8 Oct 2026). Skies: dusk, dawn, night, saffron, snow.

Commands: `SNAP_ONLY=1 bash make_media.sh temple-hero <slug> hero` (contact sheet only — **Read it**), then `bash make_media.sh temple-hero <slug> hero 0`; `bash make_media.sh story-strip <slug> explainer 2`; `bash make_media.sh route-map <slug> explainer 11`. A 14 s render takes ~8 min on 2 CPUs. Then `git add pilgrim-kit/media/<slug> pilgrim-kit/compositions pilgrim-kit/src/media/<slug>.json` → commit → push → `python3 pin_media.py <slug> $(git rev-parse HEAD)` → commit + push `media.json`.
Budgets: hero < 2.5 MB desktop / < 1 MB mobile; explainers < 2 MB. Text stays in the right 55% of the frame; phones crop the hero to the left (temple art).

## 7. Build, preview and publish
1. `python3 gen_pages.py <slug> && python3 build.py <slug>` (never publish a `--force` build).
2. Preview: `python3 tools/preview.py <slug> && node tools/shots.js /tmp/pk-prev/<slug>.html <slug>` — **Read the slices** (desktop + phone): `overflow:false`, `h1:1`, videos present.
3. Create: `wp_create_page` title = `title`, **parent** per §11, status publish, content = the exact one-line `.min.html` (chunks of ≤ 30,000 chars with `tools/chunks.py` and the `@@MKCONT@@` marker). Then `wp_update_seo_meta` (slug, title, description, focus keyword). The URL must end up exactly `path`.
4. Verify stored length = file bytes (`wp_get_page`).
5. Add to `live.json`: `{id, path, kind, label, blurb, added, shrine?}` (`shrine` = the data slug, e.g. `somnath-jyotirlinga`, so the 12-JL page and hub link to it).
6. `python3 tools/sync_plan.py <slug>` → apply each op with `wp_replace_in_page(id, find, replace, expected_count=1)`; pages under `"full"` get a full chunked re-upload.
7. Verify live: `python3 tools/cmp_live.py <slug>` (+ `--plain`), `node tools/live_check.js https://suzutravels.com<path> /tmp/x.png 390 844`.
8. Commit `src/`, `out/`, `live.json`, `BACKLOG.md`, `LOG.md`; push. `out/*.min.html` = what is live.

## 8. WordPress traps (same server as the mountain section)
**wpautop inside scripts:** WordPress inserts line breaks and `</p>` before block-level tags (`<div>`, `<h3>`, `<p>`…) even inside `<script>` — never write block-level HTML inside JS strings (kit.js builds DOM with `createElement`). `build.py`'s JS check: `node --check` the inline script of every new build.
**wptexturize:** " - " becomes " – " on output; `gen_pages.e()` already does this so cmp_live shows 0 diffs.
One-line content only (wpautop). WP Rocket: meta-only changes don't purge — re-save the title. Every Royal MCP write returns a 72-h undo token → LOG.md. Hostinger bot protection: space requests ≥ 1 s, a 403 "Checking your browser" is not a broken page. **Never**: delete content, change existing URLs/slugs, touch the static homepage, menus, theme, plugins, PHP, .htaccess, or bookable package/product pages (only link to them).

## 9. Keyword owners (avoid cannibalisation — research/site-inventory.md)
| Existing URL (owner) | Owns | Our pages link to it as the booking CTA |
|---|---|---|
| `/tours/12-jyotirlinga-tour-package/` (10876) | 12 jyotirlinga tour package | 12-JL page, every Jyotirlinga temple page |
| `/tours/5-shakti-peeth-tour-package-himachal-5-days-4-nights/` (10861) | 5 shakti peeth tour package himachal | Shakti Peeth / Himachal Devi pages |
| `/packages/ultimate-char-dham-yatra/` (9905) | char dham yatra package | Char Dham, Kedarnath, Badrinath |
| `/char-dham-closing-dates-2026/` (post 12021) | char dham / kedarnath closing date | link, never target |
| `/packages/kashmir-amarnath-by-helicopter/` (9763) | amarnath yatra by helicopter | Amarnath page |
| `/tours/amazing-kashmir-vaishno-devi-package/` (9367) | kashmir with vaishno devi | Vaishno Devi page |
| `/tours/spiritual-journey-varanasi-ayodhya-prayagraj-tour-package/` (10584) | varanasi ayodhya prayagraj tour package | Kashi / Ayodhya pages |
| `/kainchi-dham-registration-…/` (post 12444) | kainchi dham registration | Kainchi Dham page |
| `/char-dham-yatra-for-nri/` (11413) | char dham yatra for nri | Char Dham page |
Our pages own the **informational** heads ("12 jyotirlinga", "naina devi", "char dham yatra", "amarnath yatra", "somnath temple"…). Focus keywords per page: `research/keyword-plan.md` §4.

**Redirects & archives set on 8 Oct 2026 (see LOG):**
- `/char-dham-yatra/` → Rank Math Redirections rule, **302** to `/pilgrimage-tours/#chardham`. It used to be a WordPress 404 *guess* that sent the 90,500/mo head term to the NRI page. When BACKLOG row 13 (`/pilgrimage-tours/char-dham-yatra/`) is live, the Page Builder edits this rule in wp-admin › Rank Math › Redirections to **301 → the new guide** (the one allowed redirect edit; no other redirect changes).
- `/destination/jyotirlinga-tour-packages/` (suzu_destination term 212) is **noindex, follow** (term meta `rank_math_robots`) because it held 1 package and competed with 10876. Re-index it (`["index","follow"]`) only when it lists 3+ packages. Do not link to it from our pages meanwhile.
- WordPress trap: a URL that doesn't exist is 301-guessed to any slug that starts with it (`x-redirect-by: WordPress`). Before claiming a short slug, `curl -sI` it; an explicit Rank Math rule or a real page overrides the guess.

## 10. Quality gate (SEO & QA checks every live page)
200 with and without cache-buster · one H1 · robots index · canonical = URL · Rank Math title ≤ 60, description 110–155 · `cmp_live.py` 0/0 · JSON-LD parses · no ₹, no competitor links, no fact traps · every internal link, video and poster 200 (`tools/linkcheck.py`) · hero plays at 390 px · no overflow at 390 / 1440 · dates on the page still current (anything "not announced yet" re-checked weekly).

## 11. Live pages
| Page | ID | URL |
|---|---|---|
| Hub | 12541 | https://suzutravels.com/pilgrimage-tours/ |
| 12 Jyotirlinga | 12542 (parent 12541) | https://suzutravels.com/pilgrimage-tours/12-jyotirlinga/ |

**Menus (8 Oct 2026, with Sushil):** Primary Menu 5 has a top-level **"Devotional"** item (12549) after Mountains with 7 links (12550–12556); an Additional CSS block ("Header menu: Devotional item…") tightens the 12-item desktop nav. The static homepage got the same saffron "Devotional" dropdown (`<!--szpil-->`, `#szpil-nav`), two links in Destinations › Pilgrimages, the Pilgrimage experience tile → hub, and a "Devotional tours" chip (`site/enh-devotional.py`; backup `index-nz-previous.html`). Menus stay human-only for agents.
Parents: Jyotirlinga temple pages → parent = 12-jyotirlinga page id; everything else → parent = hub id.

## 12. The agents
| Agent | When (IST) | Job |
|---|---|---|
| Suzu Pilgrim Research & Data | daily 14:17 | 2 fact packs/day, keyword checks, date re-checks |
| Suzu Pilgrim Visual Studio | daily 18:07 | HyperFrames media for the next researched page |
| Suzu Pilgrim Page Builder | daily 20:47 | One new page per day, end to end |
| Suzu Pilgrim SEO & QA | Mon, Wed, Fri 22:37 | QA, fixes, date refresh, internal links from the rest of the site |

Scheduled tasks (cloud, automatic approval, created 8 Oct 2026): Research `trig_015L21nL3YQFMu6Rv8SUNroA` · Visual Studio `trig_01B8Qm59M8AjmTbu6bQc1EDM` · Page Builder `trig_018mUq2WTP2zBhkr8iwZTa2c` · SEO & QA `trig_015gFnnAauowkS3L87aQnh72`. Their prompts only bootstrap the repo and point to `agents/<agent>.md` + `agents/shared-rules.md`, so editing those files changes the agents — no trigger update needed.
They commit as `Suzu Pilgrim Agent <info@suzutravels.com>` and push to `pilgrimage` only (`git pull --rebase` first; never force-push). Reports go to Sushil in simple Hinglish with full URLs.
