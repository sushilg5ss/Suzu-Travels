# Suzu Adventure Kit v1.3 (29 Sep 2026)

Design system + build tool for every page under `suzutravels.com/adventure/`.
Owner: Suzu Travels (Sushil Kumar). Used by the scheduled "Suzu Adventure …" agents.

## Files
- `kit.css` — all styles, scoped to `.sza` (plus a small `:has(.sza)` rule that tidies the theme title bar). Never edit per page; improve it here and bump the version.
- `template-activity.html` — the landing-page template for an activity or activity×place page (sample filled for Bir Billing paragliding).
- `build.py` — `python3 build.py page.html > page.min.html` → inlines `kit.css` as `<style>` and minifies to ONE line (WordPress wpautop cannot break it). It REFUSES to build if a placeholder or a ₹/Rs price is left in.
- `media/<slug>/` — HyperFrames videos and stills per page (see Media).

## Business rules baked into the kit (non-negotiable)
1. **No prices anywhere.** Every price slot says "Get Quote". Suzu sends today's rate for the customer's date on request (WhatsApp / quote form).
2. **No operator names and no vendor-network claims.** Vendor onboarding is parked (Sushil, 29 Sep 2026): the pages exist to bring enquiries for Suzu's core packages. Suzu's sales team arranges each activity with a registered local operator on demand. Never write "our vendor network", "authorised/partner/verified vendors" or "2–3 options".
3. Suzu Travels is a **registered Travel Agent with HP Tourism** — see "Business facts" below. Trust-row text: "HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022", linked to `/certificates/`. Never "registered DMC".
4. Every page's CTAs: WhatsApp `https://wa.me/917087488961?text=<url-encoded: Hi Suzu Travels, I want a quote for <activity> in <place>. Travel date: ___ , people: ___>` and `/himachal-tour-packages-quote/`.
5. Facts (seasons, closures, age/weight limits, rules) must be researched and current. Monsoon ban (Kullu, Kangra): 15 Jul – 15 Sep.

## Page anatomy (activity / spot page) — keep this order
1. `.sza-hero` — HyperFrames loop video (`<video autoplay muted loop playsinline preload="metadata" poster>` with WebM + MP4) or a hero image; kicker, big tagline (`p.sza-hero-tag`, NOT a heading — the theme prints the page H1), sub line, 4–6 fact chips, 2 CTAs, trust row.
2. `.sza-nav` — sticky in-page menu (sticks under the 70px site header). One link per section + "Get Quote".
3. `#overview` — `.sza-answer` (answer-first, 40–70 words) + `.sza-facts` (5–6 facts, last one = "Price: Get Quote").
4. `#spots` — `.sza-grid` of `.sza-card` (spots / options / variants), each with its own Get Quote link.
5. `#experience` — `.sza-steps` (what happens) + `.sza-media` (motion graphic / second video / map still).
6. `#season` — `.sza-tbl` month table (inside `.sza-scroll`).
7. `#safety` — `.sza-band` + `.sza-checks` (what we check before we book it).
8. `#booking` — `.sza-steps`: Tell us → We check your date → You get one quote → Confirm and go (hotel + cab included if wanted).
9. `.sza-quote` — big CTA block.
10. `#packages` — contextual links to real `/packages/`, `/tours/` or hub pages (check they return 200).
11. `#faq` — `.sza-faq` `<details>` (6–8 questions). Plain-HTML answers, no JS.
12. `#more` — `.sza-cats` tiles to sibling adventure pages that are LIVE only.

## Hub page anatomy (`/adventure/`) — LIVE, page 11529, built 29 Sep 2026 from `pages/adventure.py`
Each activity card has a unique id `act-<slug>` and a unique WhatsApp link; when a child page goes live the Page Builder switches that card's link to the page ("Explore →") with one targeted replace. Regenerate with `python3 pages/adventure.py && python3 build.py pages/adventure.html > pages/adventure.min.html` only if you also re-apply live card switches.
Hero (montage video) → sticky menu of categories (Air · Water · Snow · Land & Rides · Treks & Camps · Ropeways & Parks · Rentals & Services · By destination) → `.sza-cats` category tiles → one `.sza-sec` per category with a `.sza-grid` of every activity in it (live pages link "Explore →", not-yet-built ones show only "Get Quote →") → "By destination" grid (Manali–Solang, Bir–Kangra, Kullu, Shimla–Kufri–Narkanda, Dharamshala, Bilaspur, Chamba–Dalhousie, Tirthan–Jibhi, Lahaul–Spiti) → safety band → how booking works → quote block → FAQ.

## Changelog
- v1.3 (29 Sep 2026, QA): `.sza-band` gets `scroll-margin-top:140px` — the #safety menu anchor landed under the sticky menu on both live pages. Already patched live on pages 11529 and 11632 (targeted CSS replace); new pages get it from kit.css.
- v1.2 (29 Sep 2026, Page Builder): mobile sticky menu `top:70px` (was 60px, hid under the 70 px header); paragraph text links underlined. Live on 11632; hub 11529 got the 70px fix by QA replace (the underline rule is not on the hub yet — Builder re-inlines when it next touches the hub).
- Note: `pages/adventure.min.html` in this repo is the hub BEFORE the 29 Sep live edits (Explore card switches, #snow-explainer, QA CSS/Rohtang fixes). The live page 11529 is the source of truth — pull it with wp_get_page before regenerating.
- Image rule (QA): never put a full-size upload in a card. Use the WP `-768x…` / `-1024x…` sizes (cards render ~300–660 px wide) so HTML + images stay under 1.5 MB.

## Live child pages (card switches already applied to the live hub)
- `/adventure/snow-activities-manali/` — page 11632 (29 Sep 2026). Its source files were not pushed (Builder's push was blocked); full source + kit v1.2 diff: Project doc `claude/adventure-pages/snow-activities-manali.patch`. Hub cards switched to "Explore →": act-snow-activities-in-solang-valley, act-gulaba-snow-point, act-sledging-and-snow-tubing. If you regenerate the hub from adventure.py, re-apply these.

## Business facts (verified from the certificates, 29 Sep 2026)
- **HP Tourism:** Certificate of Registration of Travel Agent, Dept. of Tourism & Civil Aviation, Govt. of Himachal Pradesh — Permanent Reg. No. **DTO-MND-11-243/2022**, certificate no. 060925/58761 dated 04-12-2025, **renewal due 03-12-2028**. Name and style: Suzu Travels, NH 103, Road Side, Kulahru, Tehsil Ghumarwin, District Bilaspur, HP.
- **GST:** GSTIN **02BLPPK1401E1ZR**, regular, valid from 13-01-2021; proprietorship of Sushil Kumar.
- **Proof page:** https://suzutravels.com/certificates/ (page 11527). Phone/WhatsApp +91 70874 88961 · info@suzutravels.com.

## Media (HyperFrames)
- Per page: hero loop 1920×1080, 8–15 s, silent, seamless; export `hero.mp4` (H.264, ≤ 4 MB), `hero.webm` (≤ 3 MB), `poster.webp` (first frame, ≤ 200 KB); optional `explainer.mp4` (motion graphic: flight path, map, altitude, how-it-works) and `reel-9x16.mp4` for Instagram.
- Text inside videos: large, few words, brand colours (navy #0b1f33, gold #d4a24c). Keep text clear of the left 45% of the hero frame on desktop (the page's own tagline sits there) and inside the centre 36% for mobile crops.
- Stills and photos: Suzu media library first; else free-licence photos (Pexels / Unsplash) downloaded and re-hosted in the WordPress media library via `wp_upload_media_from_url`. Never present a photo of another place as the named Himachal location — use neutral alt text for generic activity photos.
- Hosting: images → WordPress media library. Videos → this repo's `adventure` branch under `adventure-kit/media/<slug>/`, served through jsDelivr pinned to the commit: `https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@<commit>/adventure-kit/media/<slug>/hero.mp4` (WordPress media upload only accepts images).

## Quality gate (QA agent checks every page)
Live 200 with and without cache-buster · one H1 (theme title) · no ₹/prices · no vendor names · every link 200 · images load · video plays (desktop + 390 px phone screenshot) · sticky menu anchors work · Rank Math title < 60, description < 155 · page weight excl. video < 1.5 MB · no layout overflow at 390 px.
