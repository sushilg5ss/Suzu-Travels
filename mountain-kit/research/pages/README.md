# Fact packs: `research/pages/<slug>.md`

The Mountain Research agent writes one fact pack per backlog page before any copy or video is made. The Visual Studio and Page Builder then use only what the pack says. If a fact is not in the pack with a source, it does not go on the page.

## Template

```markdown
# <Page H1> — fact pack
slug: <slug> · kind: peak|band|state|guide · path: /mountains-of-india/<slug>/ · peak_id: <id from data/peaks.json or -> additions>
researched: <YYYY-MM-DD> · status: researched

## Target
- Focus keyword: "<kw>" — <WW>/mo worldwide, <IN> India, <INTL> US+GB+AU+IL+DE+FR (Keyword Planner, customer 1172710099, <date>)
- Secondary keywords (5–12) with volumes
- Search intent in one line, and who ranks now (top 5 domains, and what they cover or miss)
- Cannibalisation check: which live Suzu page must NOT target this keyword (see README "Keyword owners")

## Verified facts   (one row per fact; the value exactly as the page will state it)
| Fact | Value | Source (URL) | Checked |
|---|---|---|---|

## Route and camps   (peaks only: every point the profile video and route table will show)
| Point | Altitude (m) | Typical day | Note | Source |
|---|---|---|---|---|

## Season, access status and permits   (dated: "closed since 2020 — source, checked <date>")

## History and notable ascents   (years, names and routes, each sourced)

## Questions people ask   (6–10 real questions from Google "People also ask" or related searches, each with a short verified answer)

## Media notes for the Visual Studio
- Hero: "steps" (altitude read-out: start -> summit, 3–7 points from the route table) or "words" (4 two-line statements for guides)
- Ladder: 3–7 peak ids (band and state pages)
- Photos: which hf/photos files fit (see hf/photos/CREDITS.md), or "needs new photos of X"; a named-peak photo only if verified

## Do not say   (claims found in sources that are uncertain, contradicted or out of date)

## Sources   (numbered; prefer official: IMF, state govts, PIB, district administrations; then Wikipedia, Himalayan Journal, AAJ, news.
   Operator sites may be read for research, but never cited or linked on the page)
```

## Rules

- Heights come from `data/peaks.json`. If a source disagrees, write both values under "Verified facts" and use the dataset value on the page. If the dataset is wrong, fix it in `data/overrides.json` (with the source in the LOG).
- A peak missing from the dataset goes in `data/additions.json` (same fields as `data/peaks.research.json`). Then run `python3 data/build_data.py`.
- Dates matter. Closures, fees and rules are stated as "as of <month year>" and must have a source from 2025–26.
- Keep the pack factual and short. Copy writing happens in the Page Builder.
