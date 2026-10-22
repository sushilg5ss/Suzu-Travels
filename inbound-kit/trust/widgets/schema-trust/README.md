# schema-trust (TRUST_BACKLOG row 9) — live 2026-10-22 on hub /india-tours/ (11411)
Invisible JSON-LD block that extends Rank Math's existing graph — **no second Organization**:
- one untyped node with the SAME `@id` as Rank Math's TravelAgency (`https://suzutravels.com/#organization`) adding
  `hasCredential` (HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022, url /certificates/), `foundingDate` 2019,
  `areaServed` India, `knowsLanguage` en, `hasOfferCatalog` → `#tours`. Rank Math's sameAs/address/phone/priceRange untouched.
- `OfferCatalog` `https://suzutravels.com/india-tours/#tours`: the 6 hub tour cards as Offer + TouristTrip (name, days/nights,
  City itinerary, card image), US$ 'from' prices asserted against `data/prices.json` (449, 649, 899, 1099, 949, 799), price note =
  the hub's 'About our prices' text, exact booking line in the catalog description. No ratings/reviews in schema.
- Placement: `<!--szt:schema-trust-->…<!--/szt:schema-trust-->` inserted directly before the hand-built FAQPage
  `<script type="application/ld+json">` in 11411 content (unique anchor).
- Build: `python3 build.py` → `widget.html` (one line, no `&`, no `<`, no newline). Update = replace the marked block.
- Remove: `wp_replace_in_page` the whole marked block with an empty string.
- If the hub cards/prices change, edit TOURS in build.py and re-replace the block.
