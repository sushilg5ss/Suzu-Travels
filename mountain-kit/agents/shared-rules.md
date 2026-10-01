## Shared rules for every Suzu Mountain agent (v1 — 1 Oct 2026; read carefully)

**The project.** The **Mountains of India** section of suzutravels.com consists of:
- the hub `/mountains-of-india/` (WordPress page **11831**);
- the master list `/mountains-of-india/highest-peaks-in-india/` (**11841**, a 156-peak dataset);
- child pages `/mountains-of-india/<slug>/` (peaks, height bands, states, guides);
- the enquiry page `/adventure/himalayan-peak-expeditions/` (**11846**, parent 11529).

The goal (Sushil, 1 Oct 2026) is to rank worldwide for India-mountain searches, both informational and commercial, and turn them into WhatsApp enquiries. Suzu arranges climbs with validated, authorised **Himachal** mountaineering companies. Every page carries striking HyperFrames visuals and must stay fast. Built by Claude with Sushil on 1 Oct 2026.

**The owner.**
- Sushil Kumar, Suzu Travels, office at NH 103, Kulahru, Tehsil Ghumarwin, Bilaspur HP.
- Phone / WhatsApp **+91 70874 88961** (all older numbers are dead); info@suzutravels.com.
- Registration: HP Tourism registered travel agent · Reg. No. **DTO-MND-11-243/2022** (link `/certificates/`).
- Never call Suzu a "registered DMC", and never use another number.

**Nobody is watching this run.**
- Never ask a question: take the most reasonable reading, act, and report.
- Your final message IS the report, in simple Hinglish that reads well on a phone.
- Give every page with its full URL.
- Put only real decisions under **"Sushil ke liye"**, or write "kuch nahi".

**The Mountain Kit is the single source of truth.** GitHub `sushilg5ss/Suzu-Travels`, branch **`mountains`**, folder `mountain-kit/`. To get it:
1. `add_repo` (Claude Code Remote connector) with owner `sushilg5ss`, repo `Suzu-Travels`, access `push`.
2. `git clone --depth 1 --single-branch -b mountains https://github.com/sushilg5ss/Suzu-Travels ~/mk`. Use one clone and a generous timeout.
3. `cd ~/mk && git config user.name "Suzu Mountain Agent" && git config user.email info@suzutravels.com`.

Then read:
- `mountain-kit/README.md` **fully first**. It holds the business rules, the facts to avoid, the page schema, the media pipeline, the publishing steps, the WordPress traps and the quality gate.
- `BACKLOG.md`: which page is next.
- `LOG.md`: the progress log. Add ONE line per run at the top, newest first.
- `live.json`: the published pages.

**Git and commits.**
- Before every push, run `git pull --rebase`. Commit as the agent above and push to `mountains` only.
- Never force-push and never touch other branches.
- Commit messages are short: what changed and why.

**Non-negotiables** (README §1–2 in full):
- **No Suzu prices.** Use "Get Quote". Official IMF / state fees in US$ are OK as dated information.
- **Never mention Suzu's partner companies or people**: not their camps, Gorkhas, Everest summiteers or names. Never write "our vendor network", "partner company", "our own guides" or "in-house guides". The approved line is "we pair you with a registered Himachal outfitter and certified guides".
- **Sell only Himachal climbs.** Never sell Stok Kangri (closed since 2020). Kanamo stays on hold until its access status is verified.
- **Facts.** Every fact comes from the page's fact pack with a source; there are no invented numbers, records, reviews or claims. Heights and years come from `data/peaks.json`. Obey the facts-to-avoid list. Official and neutral sources come first. Read competitor operator sites if you need to, but never cite, link or copy them.
- **Photos.** A photo is captioned as a named peak only if `hf/photos/CREDITS.md` says it is that peak.
- **Social.** No Instagram or social posting, of any kind.

**WordPress** (Royal MCP "Suzu Travels WordPress" cloud connector):
- Its tools may be deferred: load them with ToolSearch, e.g. `select:mcp__Suzu_Travels_WordPress__wp_get_page,...wp_create_page,...wp_update_page,...wp_replace_in_page,...wp_update_seo_meta,...wp_get_seo_meta`. If they are absent, log it in LOG.md, push, report and stop.
- Every write returns a 72-hour undo token: put it in LOG.md.
- **Never:**
  - delete content, or change existing URLs or slugs;
  - touch the static homepage, menus, theme, plugins, PHP or settings;
  - edit pages outside this section. The exceptions are ONE contextual internal link into this section (SEO & QA only, on non-Elementor pages; check `_elementor_edit_mode` first) and re-adding the manual Mountaineering tile or card on the Adventure hub 11529 if they vanish.
- **WP Rocket cache.** Verify live twice: `?v=<random>` and plain. A meta-only change does not purge the cache, so re-save the page with the same title to purge.
- **Delay JS.** kit.js runs after the first interaction. Ignore the site-wide console errors `moment`, `setSettings` and `feather`.
- **Hostinger bot protection.**
  - Keep headless Chromium loads to a few per run, and do them before any link check.
  - Space requests to suzutravels.com at least 1 s apart.
  - A 403 page titled "Checking your browser before accessing" is the bot challenge for your container's IP, triggered by request bursts. It is not a broken page and not drift: never re-upload or "fix" anything because of it.
  - `tools/cmp_live.py` and `tools/linkcheck.py` detect it, wait and retry, and exit with code 3. Re-run later in the run; if it persists, log `bot challenge` in LOG.md.

**Lanes.** Each agent edits only what its file says:
- **Research & Data:** `research/`, `data/`, BACKLOG status `researched` and re-ranking.
- **Visual Studio:** `src/media/`, `media/`, `compositions/`, `hf/`, `gen_media.py`, `make_media.sh`, `media.json`, BACKLOG status `media`.
- **Page Builder:** `src/pages/`, `out/`, `live.json`, the WordPress pages of this section, BACKLOG status `live`.
- **SEO & QA:** fixes on live pages, `gen_pages.py` / `kit.css` / `kit.js` / `build.py` / `tools/` improvements (re-sync every page it changes), internal links from the rest of the site.

Other Suzu agents (Adventure squad, Cab squad, Design, CTR, GEO, Content Engine, Housekeeping…) do not edit these pages. You do not edit theirs, apart from the one-link rule above.

**Capacity.** Sushil keeps about 30% of his Claude capacity for himself. Work efficiently and never run the same heavy step twice without a reason. If there is nothing useful to do, write the LOG line and stop early.

**Human-only.** List these under "Sushil ke liye" and never do them yourself:
- naming or onboarding partner companies;
- showing prices;
- ad spend;
- WP Rocket full cache clear;
- menu or header changes;
- File Manager / PHP;
- anything involving money or legal agreements.
