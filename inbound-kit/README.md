# Suzu Inbound Kit v0.1 — "India for international travellers" (16 Oct 2026)

**Goal (Sushil Kumar, 16 Oct 2026):** make suzutravels.com rank for what foreign visitors to India actually search, give them
honest, complete answers, and turn that trust into enquiries (WhatsApp / email / 20% deposit). Foreign guests book 10–14 day
private trips (US$1,500–4,000 pp) — 3–5× an Indian guest's ticket — and their #1 question is *"who can I trust in India?"*.
A local Himachal company with a real office answers that better than any OTA. This kit is how four scheduled agents build the
section without Sushil's daily involvement.

Section: hub **`/india-tours/`** (WordPress page **11411**, live since Sep 2026, USD "from" prices) with the existing children
`/golden-triangle-tour/` (**11412**) and `/char-dham-yatra-for-nri/` (**11413**). New pages are published as **children of 11411**
at `/india-tours/<slug>/` (guides, itineraries, the private-driver product, practical pages).

## 0. The four agents (lanes)
| Agent | Schedule (IST) | Owns | Status it sets |
|---|---|---|---|
| **Inbound Research & Keywords** | Mon/Wed/Fri 09:23 | `research/`, `data/` (not prices.json), BACKLOG order | `researched` |
| **Inbound Page Builder** (developer) | daily 12:23 | `src/pages/`, `out/`, `live.json`, this section's WP pages | `live` |
| **Inbound Visual Studio** | daily 16:23 | `src/media/`, `media/`, `compositions/`, `hf/`, `gen_media.py`, `make_media.sh`, `media.json` | `media` |
| **Inbound Reviewer — SEO, Legal & Compliance QA** | daily 21:23 | fixes on live pages, kit code (`gen_pages.py`, `kit.css`, `kit.js`, `build.py`, `tools/`), internal links from the rest of the site, `research/forum-drafts/` | `FIX NEEDED` lines |

Flow per page: `todo → researched → media → live`, with the Reviewer testing every live page and sending `FIX NEEDED` back.
Each agent reads `agents/shared-rules.md` + its own `agents/<name>.md` first, every run.

## 1. Non-negotiables (every agent)
1. **Truth.** Every fact (visa rule, fee, distance, opening month, safety advice) comes from `research/pages/<slug>.md` with a
   source URL and an as-of date. Official sources first: indianvisaonline.gov.in, MEA, Incredible India, IRCTC, state tourism,
   RBI/NPCI (UPI for tourists), IMD, government advisories (US State Dept, UK FCDO, Smartraveller) for the "is it safe" pages.
   Never invent numbers, reviews, ratings, customer counts, awards or "seats left". Where unsure: "confirm before travel".
2. **Prices.** Only the US$ "from" figures in `data/prices.json` (the live /india-tours/ rates). Everything else = "on request"
   / "ask for a quote". No ₹ on inbound pages. No "cheapest / best price" claims. Adding a price to `prices.json` is Sushil's call.
3. **Booking terms (exact, Sushil 16 Oct 2026):** *20% deposit locks your dates and price; full refund if cancelled within 48 hours
   of paying; balance before the trip; pay by card via Razorpay (international cards accepted) or PayPal.* `gen_pages.py` prints this
   line on every page — never reword it per page.
4. **Drivers & partners.** Never name transporters, hotels we contract, guides or partner companies. **Never claim "verified /
   police-verified / background-checked drivers" on the website.** Approved wording: *"your driver's name, photo and car number
   are shared with you before the trip"*. Driver data is given only after booking (Sushil, 16 Oct 2026).
5. **Legal & compliance (Reviewer enforces, Builder obeys):**
   - Registration shown exactly: *HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022* (link `/certificates/`). Never "registered DMC", never "government approved", never "licensed by Ministry of Tourism".
   - Visa pages: we are not a visa agency — always "apply yourself at the official site indianvisaonline.gov.in; beware look-alike sites that charge extra"; no visa-approval promises; fees dated.
   - Safety pages: balanced, sourced to government advisories, no scare-mongering, no absolute promises.
   - Health: no medical advice beyond "consult your doctor / official travel-health site (CDC, NHS Fit for Travel)".
   - Photos/videos: only (a) kit-rendered compositions, (b) Suzu's own guest photos already on suzutravels.com uploads with permission, or (c) Pexels/Unsplash-licensed photos recorded in `hf/photos/CREDITS.md`. No Google-Images downloads, no competitor assets, no copied text.
   - Privacy: forms only to Suzu's existing endpoints; no third-party trackers added; the site's privacy policy covers EU/UK visitors (GDPR mention: data used only to answer the enquiry).
   - Consumer law (India CPA 2019 / ASCI): no misleading superlatives, every "from" price says what it covers and excludes.
6. **Only Suzu's channels.** Phone/WhatsApp **+91 70874 88961** only; email info@suzutravels.com. No Instagram/social posting.
   Forum answers (Reddit/TripAdvisor) are DRAFTED into `research/forum-drafts/` for Sushil's team to post — agents never create accounts or post.
7. **One voice.** Warm, precise English for a global reader (US/UK/AU/CA/DE/IL). Short sentences. Distances in km and miles, temps in °C and °F, times in IST with UTC offset. "We" = the Suzu Travels team in Himachal.

## 2. Page schema — `src/pages/<slug>.json` (see `_example-guide.json`)
Required: `path` (`/india-tours/<slug>/`), `parent` (11411), `kind` (guide | itinerary | product | practical), `title`, `seo_title` (≤60),
`seo_desc` (110–155), `focus`, `label`, `blurb`, `kicker`, `tag`, `sub`, `chips` (3–4 `[big, small]`), `q` + `answer` (40–70 words, answer-first),
`facts` (3–4 stats), `sections[]` (each: `id`, `h2`, `kind` = prose | steps | cards | table | days | stats | callout, optional `nav`, `lead`,
`video` (explainer name in `media/<slug>/`), `note`, `style` = `alt`|`dark`), `faqs` (≥5), `sources` (≥3 `[title, url]`), `verified`, `cta` (`h2`, `text`, `wa`),
optional `prices` (`h2`, `rows[[option, "from US$449", covers]]`), `trip` (TouristTrip schema), `service` (Service schema), `links` (live slugs), `media` (defaults to slug).
Build: `python3 gen_pages.py <slug> && python3 build.py <slug>` → `out/<slug>.min.html` (one line, kit CSS/JS inlined). build.py refuses
placeholders, ₹, banned claims, fact traps, links to unbuilt pages and pages without a hero video.

## 3. Media (Visual Studio)
Hero = 16:9 + 9:16 loops (`hero.mp4`, `hero-m.mp4`, `hero-poster.webp`), ≤2.5 MB / ≤1 MB, built with HyperFrames (`npx -y hyperframes@0.8.85`),
Chromium at `/opt/pw-browsers/chromium`. Compositions live in `compositions/<slug>-hero/`; `gen_media.py` is the pilgrim-kit generator carried
over as a base — **Sprint 0 for the Visual Studio is to add three inbound compositions**: `photo-hero` (licensed photos + 3–5 caption steps,
like mountain-kit `peak_hero`), `route-map` (stops by lat/lon, reuse pilgrim `route-map`), `cost-ladder` (what a day costs: car, hotel tiers, meals —
labels only, US$ only from prices.json). Render with `make_media.sh`, push, `pin_media.py <slug> <sha>` → `media.json`. Always look at the contact sheet first.

## 4. Publishing (Page Builder) — WordPress via the Royal MCP "Suzu Travels WordPress" connector
1. `python3 tools/chunks.py <slug>` → `wp_create_page` (title words = slug, **parent 11411**, status publish, content = chunk 0 + marker) → remaining chunks with `wp_replace_in_page` (`expected_count` 1).
2. `wp_update_seo_meta`: slug, title (≤60), description (110–155), focus keyword. Confirm slug.
3. `wp_get_page`: stored length == printed byte size.
4. Add to `live.json`, run `tools/sync_plan.py <slug>` and apply the link ops (hub 11411 + siblings start linking to the new page).
5. Verify live twice (`?v=<random>` and plain): 200, one H1, robots index, right title, JSON-LD parses; `node tools/live_check.js <url> /tmp/x.png 390 844` → hero plays, no overflow.
6. hreflang: pages are `en`; Rank Math handles canonical. Do not add language alternates until German/French pages exist.
WordPress traps: WP Rocket cache (re-save title to purge), Delay-JS (kit.js runs after first interaction), Hostinger bot challenge (space requests ≥1 s, few headless loads), 72-h undo tokens → LOG.md.

## 5. Quality gate (Reviewer) — every live page, every run
Content: `cmp_live.py` 0 diffs · facts spot-check 3 claims against their sources · price figures ∈ prices.json · booking line exact · registration line exact · no banned claims.
Legal: visa/safety/health wording rules above · photo credits present · no competitor text (search 2 random sentences in quotes).
SEO: title ≤60 / desc 110–155 / focus set / index · H1 once · FAQ + Article/TouristTrip JSON-LD valid · internal links ≥3 in, ≥3 out · sitemap has the URL within 24 h · Lighthouse mobile ≥85 on one rotating page.
Growth: ONE contextual internal link per run from an existing relevant suzutravels.com page/post into the section (non-Elementor; check `_elementor_edit_mode`), and 2 forum-answer drafts per run into `research/forum-drafts/YYYY-MM-DD.md` (question URL, our honest answer, where to link).

## 6. Files
`BACKLOG.md` (what's next; Research re-ranks by keyword value × fit), `LOG.md` (one line per run, newest first), `live.json` (published pages),
`media.json` (pinned media SHAs), `data/prices.json` (allowed US$), `research/kw_en5_2026-10-16.csv` (Keyword Planner, US+GB+AU+CA+DE, 400 rows),
`research/pages/<slug>.md` (fact packs — template in `research/pages/README.md`), `research/forum-drafts/`, `research/serp-log.csv`.

## 7. Distribution beyond SEO (Sushil decided 16 Oct 2026)
- Marketplace listings (Viator / GetYourGuide / TripAdvisor Experiences) use **Himachal packages** (Suzu's USP). Listing copy drafts go in `research/marketplace/` — Sushil's team creates the accounts and lists (human-only: accounts, money).
- Forum presence: drafts only (see §5). Google Ads USD test: Sushil decides budget.

## 8. Human-only ("Sushil ke liye")
Adding prices to `prices.json` · marketplace/forum accounts · ad spend · menu/header changes · File Manager/PHP · WP Rocket full clear · naming partners · anything with money or legal agreements.
