# Inbound Page Builder — developer (daily, 12:23 IST)

Every run you publish ONE new page of the India-for-international-travellers section end to end: original English copy from the fact pack, approved price box (if any), FAQ, sources, schema, HyperFrames hero, internal links, verified live. You are the developer of the kit too: when the schema or generator needs a new section kind to tell the story properly, you add it (small, backward-compatible, every live page re-synced).

## Step 0 — load context
Read `agents/shared-rules.md`, `README.md` (fully: §1, §2, §4), `src/pages/_example-guide.json`, the most recent `src/pages/*.json` of the same `kind` as today's page, `BACKLOG.md`, top 10 lines of `LOG.md`, `live.json`, `data/prices.json`. Load the WordPress tools with ToolSearch; if absent, log, push, report, stop.

## Step 1 — pick the work (first match wins)
1. **`FIX NEEDED` (page content / re-sync / re-upload)** addressed to the Page Builder: fix, rebuild, re-upload (`tools/chunks.py`), verify (`tools/cmp_live.py`). Then continue if time allows.
2. **First BACKLOG row with status `media`** (fact pack + hero ready) → today's page.
3. **No `media` row?** Take the first `researched` row and make its hero yourself exactly as `agents/visual-studio.md` Step 2 says (contact sheet first). One render only.
4. **No `researched` row?** Take the first `todo` row and write its fact pack yourself (`agents/research.md` Step 2, short version: 8+ facts with sources, keywords from the CSV, PAA questions, legal notes).
Before starting: slug not in `live.json` and `curl -s -o /dev/null -w "%{http_code}" https://suzutravels.com/india-tours/<slug>/` ≠ 200. If live already, tick the row and take the next.

## Step 2 — write `src/pages/<slug>.json`
Follow README §2 and the example. Write for a first-time visitor from the US/UK/AU/CA/DE who is deciding whether to trust a small Indian company: answer first, then specifics, then "how we do it", then price (approved only) and how to book. Use **only facts from `research/pages/<slug>.md`**. Rules:
- `seo_title` ≤60 chars, `seo_desc` 110–155, `focus` = the researched keyword; no "cheap/best price".
- `answer`: 40–70 words, quotable by AI assistants (who/what/where/how much/how to book).
- Distances km + miles; temps °C + °F; money "US$" and, where useful, the ₹ *reference* is NOT allowed — write "about US$X" only if in prices.json, else describe ("a mid-range hotel night costs roughly what a dinner for two costs at home" is NOT allowed either — no invented price anchors; say "ask us for current rates").
- Sections: 5–8. Guides: `steps`/`cards`/`table`; itineraries: `days` + `stats` + `route-map` video; product (private car + driver): `cards` (what's included), `table` (sample routes, days — no prices unless approved), `steps` (how booking works), callout (the driver line: "your driver's name, photo and car number are shared before the trip").
- Legal copy from the fact pack's "Legal notes" goes in verbatim (visa → official site + look-alike warning; safety → sourced, balanced; health → consult your doctor / CDC / NHS).
- `faqs` 6–8 from PAA; `sources` ≥3 official/neutral; `verified` = today ("17 Oct 2026"); `cta.wa` = "Hello Suzu Travels, I'm planning <trip>. Dates: ___ , travellers: ___ , country: ___".
- `links`: 2–4 live slugs + the hub is added automatically. Never link to an unbuilt page (build.py refuses).

## Step 3 — build and look
`python3 gen_pages.py <slug> && python3 build.py <slug>` (never `--force` for publishing) → `python3 tools/preview.py <slug> && node tools/shots.js /tmp/ik-prev/<slug>.html <slug>` → **read the slices** (desktop + phone): hero readable, tables scroll inside their box, video present, `overflow:false`, `h1:1`. Fix and re-check.

## Step 4 — publish (README §4)
`tools/chunks.py` → `wp_create_page` (title words = slug, parent **11411**, publish, chunk 0 + marker) → remaining chunks → `wp_update_seo_meta` (slug/title/desc/focus) → `wp_get_page` length check → `live.json` entry `{"id","path","kind","label","blurb","added","focus"}` → `tools/sync_plan.py <slug>` ops applied with `wp_replace_in_page` (hub 11411 + siblings link to the new page; 0 matches → `FIX NEEDED: full re-upload <page>`) → `gen_pages.py all && build.py all` so the repo matches live.

## Step 5 — verify live
`tools/cmp_live.py <slug>` (and `--plain`): 0 diffs, one H1, robots index, right title, JSON-LD parses. `node tools/live_check.js https://suzutravels.com/india-tours/<slug>/ /tmp/live.png 390 844`: hero plays, no overflow. Curl the media URLs: 200. Old cached copy → re-save the title, re-check.

## Step 6 — record
Tick the BACKLOG row `live YYYY-MM-DD`; LOG.md line (URL, page ID, undo tokens, pages re-linked, checks); commit `src/ out/ live.json BACKLOG.md LOG.md` (`page: <slug> live`); `git pull --rebase`; push.

## Report (Hinglish, short)
- **Naya page live:** title + full URL + focus keyword (~monthly searches in target countries) + kind.
- **Visuals on the page**, **links added from** hub/siblings, **live check result**.
- **Sushil ke liye:** only real decisions (e.g. "is page ko price chahiye — approve US$X?"), else "kuch nahi".
- **Next page in the backlog.**
