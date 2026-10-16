# Homepage release 2026-10-16b — DEPLOYED 16 Oct 2026 ~18:40 IST (Claude with Sushil)
Base: live 63c1b336900766e5 → + homepage agent's hero-motion-pause release (6dc089e3) → + engine sync (sync_engine.py) = **acb9460c6805afe9** (947,837 B). PARITY PASS. Rolling backup public_html/index-nz-previous.html = 63c1b336.
Changes in our #tp-engine blocks only:
- tpe-data refreshed from planner v0.5: 87 places, 31 ready ideas, from-cities incl. Jaipur, Kathgodam, Agra, Udaipur, Jodhpur, Nainital (19 options).
- Regions Rajasthan / Agra & Mathura in search + cab/hotel selects; 11 popular chips (Golden Triangle, Kainchi+Nainital, Royal Rajasthan added).
- "Going to" dropdown no longer overlaps the section below / fixed CTA bar: hero + engine get .dd-open (z 99999) while open, and the list height is capped to the space left inside the hero (scrolls inside).
Also included: hero photo zoom + snow pause when #nz-hero is off-screen / tab hidden (homepage agent's 15 Oct ask).
