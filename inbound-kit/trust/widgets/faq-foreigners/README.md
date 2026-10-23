# faq-foreigners (TRUST_BACKLOG row 10 `faq-for-foreigners-hub`) — live 2026-10-23 on hub /india-tours/ (11411)
"Questions International Travellers Ask" — 9 extra Q&As for first-time foreign visitors (first trip checklist, e-Visa without
being overcharged + visa legal line, e-Arrival card, US/UK government advice (dated), scams/touts (FCDO quotes + registration +
booking line), car+driver vs trains (FTQ 365 days, FCDO night/fog, driver line), card/UPI (neutral NPCI line + booking line),
vaccinations (yellow-fever line + doctor/CDC/NHS), monsoon (IMD normals)) + WhatsApp/email CTA + dated sources.
Links to live pages: first-time guide 15453, e-Visa 14187, private driver 14015, best time 15204, /certificates/.

- Pure HTML `<details>` — no JS, no cookies, works everywhere. Class prefix `.szk` (new). Palette ink/gold/sand.
- **No schema on purpose:** the hand-built FAQPage JSON-LD stays the page's only FAQPage (no second FAQPage). If wanted later, the
  Reviewer may append these 9 Q&As to that hand-built JSON-LD.
- Not answered (fact packs' 'Do not say'): tipping, dress code, SIM/eSIM, UPI limits, visa fees, vaccine lists, 'India is safe'.
  Add those Qs only after Research writes fact packs (rows sim-card / upi-and-money / insurance).
- Placement: `<!--szt:faq-foreigners-->…<!--/szt:faq-foreigners-->` inserted directly before `<section class="lp-sec" id="more-tours">`
  (= right after the hand-built FAQ). Build: `python3 build.py` (asserts booking + registration lines, banned words, prices).
- Lesson: no backslash escapes in CSS sent through the MCP — the open-state icon uses a literal '−'.
- Remove: `wp_replace_in_page` the whole marked block with ''.
