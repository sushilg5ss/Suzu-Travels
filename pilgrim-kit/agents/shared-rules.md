## Shared rules for every Suzu Pilgrim agent (v1 — 8 Oct 2026; read carefully)

**The project.** The **Pilgrimage Tours (Tirth Yatra)** section of suzutravels.com: hub `/pilgrimage-tours/`, the 12 Jyotirlinga guide `/pilgrimage-tours/12-jyotirlinga/`, and child pages `/pilgrimage-tours/<slug>/` and `/pilgrimage-tours/12-jyotirlinga/<temple>/`. Goal (Sushil, 8 Oct 2026): a world-class devotional section — every famous Indian temple and yatra researched and told beautifully with stories, motion graphics (HyperFrames), darshan timings, dates, how to reach, itineraries and FAQs; built for SEO so new pages keep coming and get indexed; zero copyright risk; no dependency on Sushil. Traffic → WhatsApp enquiries → Suzu packages.

**The owner.** Sushil Kumar, Suzu Travels, office at NH 103, Kulahru, Tehsil Ghumarwin, Bilaspur HP. Phone / WhatsApp **+91 70874 88961** (all older numbers are dead); info@suzutravels.com. HP Tourism registered travel agent · Reg. No. **DTO-MND-11-243/2022** (link `/certificates/`). Never "registered DMC", never another number.

**Nobody is watching this run.** Never ask a question: take the most reasonable reading, act, and report. Your final message IS the report, in simple Hinglish that reads well on a phone, with every page's full URL. Put only real decisions under **"Sushil ke liye"**, or write "kuch nahi".

**The Pilgrim Kit is the single source of truth.** GitHub `sushilg5ss/Suzu-Travels`, branch **`pilgrimage`**, folder `pilgrim-kit/`.
1. `add_repo` (Claude Code Remote connector) with owner `sushilg5ss`, repo `Suzu-Travels`, access `push`.
2. `git clone --depth 1 --single-branch -b pilgrimage https://github.com/sushilg5ss/Suzu-Travels ~/pk` (one clone, generous timeout).
3. `cd ~/pk && git config user.name "Suzu Pilgrim Agent" && git config user.email info@suzutravels.com`.
Then read `pilgrim-kit/README.md` **fully first** (rules, facts to avoid, schema, media, publishing, traps, quality gate, keyword owners), `BACKLOG.md`, the top of `LOG.md` and `live.json`. Take the real time from `TZ=Asia/Kolkata date` for logs.

**Git.** `git pull --rebase` before every push; push to `pilgrimage` only; never force-push; short commit messages.

**Non-negotiables** (README §1–2):
- No Suzu prices ("Get Quote"); link to the existing package pages, never compete with their keywords.
- Facts only from `data/*.json` or `research/pages/<slug>.md`, each with source + as_of. Official sources first. Unpublished timings → "confirm locally". Unannounced dates → "not announced yet". Never guess.
- Legends in our own words, as tradition; disputes stated neutrally. No copied text, no lyrics, no modern copyrighted bhajans; classical Sanskrit stotras are fine.
- Visuals: only the kit's original illustrated compositions (or photos with a verified commercial-use licence recorded in `hf/photos/CREDITS.md`). Never caption an archetype as an exact likeness.
- Point pilgrims only to official registration/booking sites; warn about fake ones. No communal or caste content. No social posting.

**WordPress** (Royal MCP "Suzu Travels WordPress" cloud connector). Load tools with ToolSearch, e.g. `select:mcp__Suzu_Travels_WordPress__wp_get_page,mcp__Suzu_Travels_WordPress__wp_create_page,mcp__Suzu_Travels_WordPress__wp_update_page,mcp__Suzu_Travels_WordPress__wp_replace_in_page,mcp__Suzu_Travels_WordPress__wp_update_seo_meta,mcp__Suzu_Travels_WordPress__wp_get_seo_meta`. If absent: log in LOG.md, push, report, stop. Every write returns a 72-hour undo token → LOG.md.
**Never:** delete content; change existing URLs or slugs; touch the static homepage, menus, theme, plugins, PHP, settings or .htaccess; edit package/product pages or pages outside this section — except ONE contextual internal link per run into this section (SEO & QA only, non-Elementor posts; check `_elementor_edit_mode` first).
**WP Rocket:** verify live twice (`?v=<random>` and plain); meta-only changes don't purge — re-save the title. **Hostinger bot protection:** few headless loads per run, ≥ 1 s between requests; a 403 "Checking your browser" is not a broken page — wait and retry (tools exit 3), never "fix" a page because of it.

**Lanes.** Research & Data: `research/`, `data/`, BACKLOG `researched` + re-ranking. Visual Studio: `src/media/`, `media/`, `compositions/`, `hf/`, `gen_media.py`, `make_media.sh`, `media.json`, BACKLOG `media`. Page Builder: `src/pages/`, `out/`, `live.json`, this section's WordPress pages, BACKLOG `live`. SEO & QA: fixes on live pages, `gen_pages.py` / `kit.css` / `kit.js` / `build.py` / `tools/` improvements (re-sync every page it changes), internal links from the rest of the site. Other Suzu agents (Mountain, Adventure, Cab, Design, CTR, GEO, Content Engine, Housekeeping…) don't edit these pages; you don't edit theirs (apart from the one-link rule).

**Capacity.** Sushil keeps ~30% of his Claude capacity for himself. Work efficiently, don't repeat heavy steps (a HyperFrames render is ~8 min), and stop early with a LOG line if there is nothing useful to do.

**Human-only** (list under "Sushil ke liye", never do): showing prices, ad spend, partner/vendor names, menu/header changes, File Manager/PHP, WP Rocket full cache clear, anything involving money or legal agreements.
