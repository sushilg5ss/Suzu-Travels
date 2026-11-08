# Morning plan — 9 Nov 2026 (after the 00:10–02:45 IST quiet window)

Prepared by Claude at the end of the 8 Nov night shift. Nothing below has been written to the site yet.

## 1. Ready-to-publish pages (specs written, photos picked, uploads NOT done)

| Page | Spec | Photos | Category | Keyword (India, avg / peak month) |
|---|---|---|---|---|
| /theog-weather/ | spec_theog_weather_en.py | 5 new (queue: morning-upload-queue-theog-rohru.json) + 4 reused from narkanda-ka-mausam / shimla-snowfall | 77 | theog weather 60.5K (Dec 40.5K) |
| /rohru-weather/ | spec_rohru_weather_en.py | 9 new (same queue file) | 77 | rohru weather 90.5K (Dec 49.5K), chanshal pass 6.6K |
| /karsog-weather/ | spec_karsog_weather_en.py | 9 new (queue: morning-upload-queue-karsog.json) | 77 | karsog weather 49.5K (Dec 27.1K) |

Steps for each:
1. Weather feed (tools/weather_feed.py, MORE list) — add and deploy BEFORE publishing:
   - theog — 31.1200, 77.3500, 2100 m, link theog-weather/
   - rohru — 31.2020, 77.7520, 1525 m, link rohru-weather/
   - karsog — 31.3800, 77.2000, 1400 m, link karsog-weather/
   - shikaridevi — 31.4787, 77.1656 (Wikipedia infobox), 3300 m, link karsog-weather/
2. Upload the queue with runQ (one writer, ≥40 s gaps, health check < 4 s). Uploads count as writes — only after 02:45.
3. `python3 build_post.py spec_<x>`; link check; preview hero + gallery (look for dark heroes, children close-ups, wrong captions).
4. Commit + push to ranking branch, `rkCreate(sha, slug, [77])`, then Rank Math title / description / focus from the spec.
5. Low priority: night-page meta descriptions run 200–250 characters; trim to ~155 when convenient.
6. Internal links: /weather/narkanda (18262) → Theog, Rohru; /weather/shimla (18242) → Theog; mandi-weather → Karsog; rampur-weather (19883) → Rohru.

## 1b. Small updates to live pages (rebuilt HTML already committed on the ranking branch)
- rkPush(sha, 'budgam-weather', 19935) — adds links to the existing /doodhpathri-yusmarg/ guide.
- rkPush(sha, 'bandipora-weather', 19947) — adds links to the existing /gurez-valley/ guide.
- rkPush(sha, 'jibhi-weather', 19748) → /jalori-pass/; rkPush(sha, 'pangong-weather', 19785) → /leh-to-pangong-lake/; rkPush(sha, 'parvati-valley-weather', 19856) → /manikaran-sahib/, /tosh-village/.
- NOTE: patnitop-weather (19539), anantnag-weather (19773), chamba-weather (19573), kinnaur-weather (19663) and bhaderwah-weather (19831) had night link edits made directly in WP; their specs on the ranking branch already include them, so a future rkPush keeps the links.
- Reverse links (wp_replace_in_post, one at a time): /gurez-valley/ → bandipora-weather; /doodhpathri-yusmarg/ → budgam-weather; /adventure/kheerganga-trek/ → parvati-valley-weather; /adventure/chanshal-pass/ → rohru-weather (after Rohru is live).

## 2. Indexing (Google quota resets ~13:30 IST)
Google Indexing API (Rank Math Instant Indexing → Publish/update) or GSC "Request indexing" for the 24 night pages:
sissu-weather, jibhi-weather, chail-weather, rohtang-weather, anantnag-weather, baramulla-weather, pangong-weather, kargil-weather, chillai-kalan, bir-weather, solang-valley-weather, bhaderwah-weather, bilaspur-weather, hamirpur-weather, kupwara-weather, parvati-valley-weather, kishtwar-weather, rampur-weather, banihal-weather, bharmour-weather, kulgam-weather, shopian-weather, budgam-weather, bandipora-weather
plus the evening Hindi pages still waiting: pahalgam-ka-mausam, gulmarg-ka-mausam, sonamarg-ka-mausam, narkanda-ka-mausam.
(IndexNow for Bing/Yandex was already sent for all of these on 8 Nov.)

## 3. Next research queue (Keyword Planner, India)
- Jammu side, large but mostly local: udhampur weather 246K, doda 201K, poonch 165K, kathua 165K, rajouri 135K — only if paired with travel angles (Patnitop, Mughal Road, Noori Chamb).
- Hindi twins of the strongest English night pages (banihal, kishtwar, anantnag) — Hindi volumes are much smaller; low priority.
- Snowfall pages already exist for Shimla, Manali, Kashmir, Kufri, Dalhousie, Dharamshala, Gulmarg, Pahalgam, Sonmarg, Auli, Mussoorie, Kasauli — keep them fresh in December instead of new ones.

## 4. Still waiting on Sushil
- Permanent delete of media 19720 (children close-up, unused — urgent), 19617, 19715 and the earlier temporary contact-sheet media.
- "OK weather workflow" for the hourly feed refresh (the feed is static until then; pages say "refreshed about once a day").
- Theme text: header "24/7" and footer "most trusted" (banned claims) — needs a theme edit.
- "since 2019", Kashmir hub, homepage release (from earlier shifts).
