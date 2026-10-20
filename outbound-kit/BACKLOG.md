# Outbound backlog (Holidays Abroad) — status: todo / doing / live / FIX NEEDED

| # | item | type | status | notes |
|---|---|---|---|---|
| 1 | Dubai & UAE tour packages from India — /dubai-tour-packages/ | new country page | live | 2026-10-18 · page 14234 · `pages/gen_dubai.py` · hub tile + 9 "Explore more" grids link to it · visa checked 18 Oct 2026 (GDRFA Dubai) — re-check every ~3 months |
| 2 | Turkey tour packages from India — /turkey-tour-packages/ | new country page | live | 2026-10-19 · page 14629 · `pages/gen_turkey.py` · hub tile + 9 country "Explore more" grids + Dubai page link to it · visa checked 19 Oct 2026 (MFA Türkiye + Turkish Embassy New Delhi) — re-check every ~3 months |
| 3 | Georgia tour packages from India — /georgia-tour-packages/ | new country page | FIX NEEDED | 2026-10-20 · page 14841 built as DRAFT (`pages/gen_georgia.py`, content byte-exact 55874, Rank Math title/desc/focus kw + slug `georgia-tour-packages`, featured 14831, 10 Unsplash photos 14831–14840). Local render test green (1440/390, 1 H1, 0 overflow, 0 broken, 48 links 200). **Publish step was blocked by the agent permission guard** → next run (or Sushil): set 14841 to publish (parent 0), run live checks, then hub tile (`gen_hub.py` LIVE_PAGES georgia) + Georgia card in "Explore more" on 11 country pages, live.json. Visa checked 20 Oct 2026 (evisa.gov.ge, MFA Ordinance 256, georgia.travel) |
| 4 | Azerbaijan (Baku) tour packages from India — /azerbaijan-tour-packages/ | new country page | todo | |
| 5 | Japan tour packages from India — /japan-tour-packages/ | new country page | todo | long visa lead time — say so |
| 6 | Europe multi-country tour packages — /europe-tour-packages/ | new country page | todo | Schengen appointment lead time |
| 7 | Country pages: add 6-photo real gallery (Unsplash/Pexels) under "Why <country>" on the 8 pages without guest photos | upgrade | todo | Nepal already has Suzu guest photos |
| 8 | Hub: "Where to go in <month>" seasonal block driven by the best-season facts of the 9 pages | hub feature | todo | |
| 9 | Hub: comparison table (flight time, entry type, typical trip, best season) for the 9 countries — facts copied from each page's fact box, with "checked <date>" | hub feature | todo | |
| 10 | Switzerland, UK, Mauritius, Egypt, Australia/NZ, Uzbekistan, Kazakhstan/Kyrgyzstan, Armenia pages | new country pages | todo | one per run, demand order via Semrush (db `in`) |
| 11 | Ask Technical SEO squad (hand-off) to confirm all outbound pages are in page-sitemap.xml | check | todo | known Rank Math sitemap under-report bug |
| 12 | Dubai page: add a Suzu guest photo block once Sushil shares real Dubai trip photos | upgrade | todo | no guest photos for UAE yet |
| 13 | Existing 9 country pages: add Dubai to the hub planner/related blocks consistently; consider moving `.sx` pages to the `.hx` look (Dubai page = template via `gen_dubai.py`) | upgrade | todo | |
| 14 | Turkey page: add a Suzu guest photo block once Sushil shares real Turkey trip photos | upgrade | todo | no guest photos for Turkey yet |
