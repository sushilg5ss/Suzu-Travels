# Suzu About Kit v1.0 (14 Oct 2026)

Cinematic redesign of **https://suzutravels.com/about-suzu-travels/** (WordPress page **9964**).
Built by Claude with Sushil Kumar. Branch `about`, folder `about-kit/`.

## How the page is put together
- Page 9964 uses the **default theme template** (`_wp_page_template` = `default`). Before 14 Oct 2026 it used the plugin template `suzu-team-members/about-page-template.php` with empty post content — **rollback = set the template meta back to that value**.
- The whole design is the page content: one minified line (`out/about.min.html`) with scoped CSS (`.szab`), the content, JSON-LD and one small script.
- The theme prints the H1 (page title "About Suzu Travels"); `about.css` positions it inside the hero (`.page-content:has(.szab) .page-header`). If the page title is changed, check the hero on phone and desktop (the hero reserves 1 line on desktop, 2 on phones).
- WP Rocket delays inline scripts until the first interaction, so everything works without JS (CSS animations, scroll-driven reveals, radio-button filters, `<details>`). JS only adds: live Google rating from `/suzu-reviews.json`, crew-film autoplay on view, count-up numbers, chapter-nav highlight, map row hover.

## Sections
Hero (HyperFrames film loop) · chapter nav · Our story (answer-first "Who is Suzu Travels?" + fact file) · Journey film strip 2019–2026 · The crew (credits film + 13 cards, filters by department and squad) · India network map (official boundary; agent arcs / "Where we travel" toggle) · 8 departments · B2B partners · Google reviews · Feedback · FAQ (9, FAQPage schema) · final CTA.

## Files
| Path | What |
|---|---|
| `src/team.py` | **Single source of truth for the team** (names, roles, squads, languages, emails, bios). Change here, rebuild page (and the crew film if a person joins/leaves). |
| `src/gen_page.py` | Page generator → `out/about.html` + `out/about.min.html`. `python3 gen_page.py preview` uses local media for screenshots. Needs `config.json` (`cdn`, `images`) and `reviews.json` (copy of /suzu-reviews.json). |
| `src/about.css`, `src/about.js` | Design system + script (scoped `.szab`). |
| `src/india-map.json`, `src/make_map.py` | India map paths. Outline: DataMeet `Country/india-composite.geojson` (CC0, India's official boundary). States: DataMeet `States/Admin2.shp` (CC BY 4.0, 36 states/UTs incl. Ladakh). Never replace with a map that cuts J&K/Ladakh. |
| `src/gen_hero.py`, `src/gen_crew.py`, `compositions/` | HyperFrames compositions (hyperframes@0.8.85): hero = 16 s seamless Himalaya dawn loop (no text); crew = 27 s opening-credits film of the team. |
| `media/` | Encoded films + posters, served via jsDelivr pinned to the commit. |
| `team/` | 640×800 portrait crops (also uploaded to the WP media library — the page uses the WP URLs). |
| `fonts/` | Cormorant Garamond 600/700 + Plus Jakarta Sans 500/700/800 (OFL). |

## Rules
- Trust wording: "Registered Travel Agent with HP Tourism — Reg. No. DTO-MND-11-243/2022". Never "registered DMC". No prices. No "4★ and above"/review-filter wording; keep "Reviews and ratings: Google."
- Phone/WhatsApp only +91 70874 88961.
- Team member reviews (e.g. a staff member's own Google review) are excluded from the review strip.
