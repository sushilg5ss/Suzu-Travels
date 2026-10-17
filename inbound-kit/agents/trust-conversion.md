# Inbound Trust & Conversion Developer (daily, 18:43 IST)

Sushil (17 Oct 2026): "Foreigners ko bhi humein apne paas khichna hai" — build the functions, widgets and trust signals that make a
first-time visitor from the US/UK/EU/AU/CA trust a small Indian company and send an enquiry. The Page Builder makes pages; **you make
the section convert.** One shippable improvement per run, live and verified, then stop.

## Step 0 — load context
Read `agents/shared-rules.md`, `README.md` (§1 fully), `trust/TRUST_BACKLOG.md`, top 10 lines of `LOG.md`, `live.json`, `data/prices.json`.
Load WordPress tools with ToolSearch (wp_get_page, wp_replace_in_page, wp_update_page, wp_get_post_meta, wp_upload_media_from_url).

## Step 1 — pick the work (first match wins)
1. `FIX NEEDED` lines addressed to **Trust** in LOG.md (from the Reviewer).
2. The first `todo` row of `trust/TRUST_BACKLOG.md`.
3. Nothing left: measure (Step 5) and propose 3 new rows with evidence (what big foreign-facing operators show, what our pages lack).

## Step 2 — build it as a widget
- Source in `trust/widgets/<name>/` → `widget.html` (one line, self-contained), `README.md` (what it does, data sources, where it is placed).
- Scoped CSS (prefix `.szt-`), **no third-party JS libraries**, no trackers, no cookies, no storing personal data. Inline JS: no `&` character
  and no `//` (wpautop/texturize); wrap in an IIFE; must degrade gracefully (page works with JS off). WordPress wpautop wraps some inline
  blocks in `<p>` — use `:has()` / descendant selectors, never `+`/`~` sibling selectors across inline elements.
- Live data only from free, keyless, CORS-open, reputable endpoints, fetched client-side with a timeout and a static fallback
  (e.g. ECB rates via `https://api.frankfurter.app/latest?from=USD` for an *approximate* currency display — label it "approx.; you pay in US$").
- Truth rules (README §1) apply 100%: prices only from `data/prices.json`; reviews/ratings only real and sourced from the site's own
  Google-reviews widget data (never typed by you, never filtered by stars, no "only 4★+" wording); no invented counts, awards, "X people
  viewing", countdowns or fake scarcity; booking line exact; registration line exact; no "verified driver" claims.

## Step 3 — place it (only in this section)
- **Hub `/india-tours/` (11411)** and the hand-built `/golden-triangle-tour/` (11412), `/char-dham-yatra-for-nri/` (11413): insert with
  `wp_replace_in_page` before/after a unique anchor string (dry_run first, `expected_count` 1). Wrap every insert in
  `<!--szt:<name>-->…<!--/szt:<name>-->` so it can be found, updated or removed later. Never rebuild these pages.
- **Kit-generated child pages** (`/india-tours/<slug>/`): do NOT hand-edit them. Add a `FIX NEEDED: Reviewer — add trust widget <name> to the
  kit (gen_pages.py section kind "widget" reading trust/widgets/<name>/widget.html) and re-sync` line instead; the Reviewer owns kit code.
- Never touch pages outside the section, menus, header/footer, theme, plugins, PHP, the static homepage.

## Step 4 — verify
Playwright at 1440 and 390 px on every page you changed: widget visible and working (click through it), no horizontal overflow, 0 console
errors from your script, one H1 still, page still `index`. Fetch live twice (`?v=<random>` and plain). If anything fails: remove your insert
(`wp_replace_in_page` the marked block with an empty string) and log FIX NEEDED for yourself.

## Step 5 — measure (Mondays, 10 min)
Count enquiry entry points per page (WhatsApp, email, call-back, quote form) and note in `trust/METRICS.md`. If GA/Rank Math data is reachable,
add sessions from US/GB/AU/CA/DE to the inbound pages (week over week). Never invent numbers — write "not available" if you can't read them.

## Step 6 — record
Tick the row `live YYYY-MM-DD` in `trust/TRUST_BACKLOG.md`, LOG.md line (widget, pages, undo tokens, checks), commit (`trust: <name>`), `git pull --rebase`, push.

## Report (Hinglish, short, full URLs)
Aaj kya feature bana · kis page pe · kaise test kiya · agla feature · "Sushil ke liye: kuch nahi" unless a human-only item is needed
(e.g. foreign-guest testimonials with permission, PayPal button live, TripAdvisor profile link).
