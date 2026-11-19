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

## Product pages (row 34) — live 2026-11-18 on /golden-triangle-tour/ (11412) + /char-dham-yatra-for-nri/ (11413)
- `python3 build_product.py` → `widget-11412.html` / `widget-11413.html` (imports build.py; hub widget.html stays byte-identical).
- 7 Qs each; questions the page's own FAQ already answers are dropped (11412: car-or-train, monsoon; 11413: first-trip, car-or-train).
- Changes vs hub text: FCDO answer complete (J&K except Jammu city air/within; 10 km border except Wagah–Attari; Manipur all but essential;
  updated 7 Oct 2026, checked 18 Nov 2026 via gov.uk content API), US line adds J&K Level 4 (checked 14 Nov 2026, fact pack
  manali-vs-kashmir), dated Visitor Visa note (PIB 2335182), OCI/Indian-passport line on 11413, links to live UPI / SIM / insurance /
  choose-an-agency / solo-female guides, page-specific WhatsApp prefill. e-Visa facts re-checked on tvoa page 18 Nov 2026.
- Prefix `.szu` (`.szk` is used on these pages by check-us). No JS, no schema, nothing stored.
- Placement: inserted directly before `<section class="lp-sec" id="more-tours">`. Remove: replace the marked block with ''.
- Verified live 18 Nov 2026: `?v=` + plain, 1440 + 390, 7 details, toggle works, scrollWidth = viewport, 1 H1, index, 0 console errors.

## Hub refresh (row 35) — live 2026-11-19 on /india-tours/ (11411)
- `python3 build_hub.py` → `widget-11411.html` (= current live hub block) + `ops-11411.json` (8 literal replace ops from the old `widget.html`;
  the script asserts the ops reproduce widget-11411.html exactly). `widget.html` stays = the 23 Oct original (the ops' 'find' base).
- Changes: visa checked 18 Nov + dated Visitor Visa note; e-Arrival re-checked 18 Nov; FCDO line complete (Jammu city air/within, 10 km border
  except Wagah–Attari, Manipur all but essential — gov.uk content API, updated 7 Oct 2026, text re-checked 19 Nov 2026); links to solo-female
  safety, choose-an-agency, UPI, SIM, insurance guides; sources line updated. US line unchanged (checked 23 Oct 2026; curl 403).
- Verified 19 Nov 2026: hub content +988 bytes (= file delta), `?v=` + plain curl 200 with new text, 1 H1, index; Playwright 1440 + 390 + iPhone 13:
  9 details, toggles open, 0 overflowing elements, scrollWidth = viewport, 0 console errors. All 5 new links 200.
