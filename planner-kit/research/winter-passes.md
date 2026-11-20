# Winter passes (v1.9, 3 Nov 2026)

Used by `WP` + `leg()` in `src/planner.js`. Rule of thumb, always phrased "about / usually" in the UI.

| Pass / road | Planner rule | Sources (checked 3 Nov 2026) |
|---|---|---|
| Kunzum Pass (Gramphu – Kaza, Manali/Lahaul ↔ Spiti) | closed outside Jun–Oct → Spiti legs that would cross Kunzum are re-routed via Kinnaur (Nako); warning | https://en.wikipedia.org/wiki/Kunzum_Pass · https://tribuneindia.com/news/gramphu-kaza-highway-officially-closed-for-traffic-via-kunzum-pass · https://discoverkullumanali.in/manali-spiti-road-opens-after-eight-months/ · https://www.outlooktraveller.com/travelnews/kunzum-pass-reopened-after-months-of-closure |
| Manali – Leh highway (Baralacha La, Tanglang La; detected = road passes Sarchu) | closed outside Jun–Oct → warning "fly into Leh or via Srinagar–Zojila" | https://www.tribuneindia.com/news/himachal/manali-leh-highway-via-atal-tunnel-closes-beyond-solang-after-fresh-snowfall-in-himachal-449545 |
| Zojila Pass (Srinagar – Kargil – Leh) | closed Jan–Mar (reopened 28 Feb–mid Apr in recent years) → fly-in warning; Dec & Apr → "can close a few days" | https://www.tribuneindia.com/news/j-k/srinagar-leh-road-reopens-after-73-days-378993 · https://www.tribuneindia.com/news/j-k/srinagar-leh-road-reopens-after-2-months-218791 · https://www.drishtiias.com/daily-updates/daily-news-analysis/zojila-pass-and-razdan-pass-reopen-after-short-winter-closure/print_manually |

Detection uses the OSRM km matrix: a Spiti leg (Kaza/Tabo ↔ X) "enters through Kinnaur" when km(X,Nako)+km(Nako,Spiti) ≤ km(X,Spiti)+15; otherwise it crosses Kunzum (25 pairs: Manali, Sissu, Jispa, Sarchu, Ladakh, Sonamarg/Baltal). Chandratal is skipped (already "closed" by its own months).

## Atal Tunnel / Lahaul in winter (v2.4, 19 Nov 2026)
| Rule | Planner behaviour | Sources |
|---|---|---|
| Dec–Mar: after fresh snow the Manali – Atal Tunnel – Lahaul road is closed beyond Solang Nala to tourist vehicles, sometimes for weeks (only locals / 4x4 let through) | One note per plan: Sissu stay (r:1, Manali back-up night) or the "Atal Tunnel & Sissu" sight day (r:0, Solang Valley fallback). Prices unchanged. | https://www.tribuneindia.com/news/himachal/atal-tunnel-opened-to-tourists-after-24-days-205596 · https://www.tribuneindia.com/news/himachal/manali-leh-highway-restored-only-locals-allowed-via-atal-tunnel-469903 · https://www.tribuneindia.com/news/himachal/manali-leh-nh-restored-for-locals-tourist-throng-solang-470736 · https://www.tribuneindia.com/news/himachal/250-tourist-vehicles-sent-back-from-atal-tunnel-after-snow-192950 · https://discoverkullumanali.in/manali-atal-tunnel-highway-status/ |

## Char Dham winter seats (v2.5, checked 20 Nov 2026)
- Kedarnath & Yamunotri portals closed for winter on 11 Nov 2026 (All India Radio: https://newsonair.gov.in/kedarnath-and-yamunotri-dhams-to-close-for-winter-today/ ; NewKerala: https://www.newkerala.com/news/a/portals-shri-kedarnath-dham-close-winter-utsav-doli-570.htm). Gangotri closes around Diwali / Annakut, Badrinath in the second half of November (closing dates announced yearly: https://www.newsonair.gov.in/uttarakhand-announces-winter-closing-dates-for-kedarnath-badrinath-gangotri-and-yamunotri-temples).
- Winter seats (deities' doli moves here, darshan continues Nov–Apr): Yamuna → Kharsali (Khushimath); Ganga → Mukhba; Kedarnath → Omkareshwar Temple, Ukhimath; Badrinath → Yogdhyan Badri, Pandukeshwar + Narsingh Temple, Jyotirmath; Tungnath → Markandeya Temple, Makkumath. Uttarakhand promotes a "winter Char Dham yatra" to these seats (Hindustan Times: https://magzter.com/stories/newspaper/Hindustan-Times-Uttarakhand/CHAR-DHAM-SHRINES-SHIFTED-TO-WINTER-ABODE-OPEN-FOR-YATRA ; Devdiscourse: https://www.devdiscourse.com/article/law-order/3788833-over-34000-pilgrims-visit-char-dham-winter-seats-in-uttarakhand-since-shrine-closure).
- Planner rule: any plan day Nov–Apr touching Barkot / Uttarkashi / Guptkashi / Badrinath / Chopta → one note naming the closed temple(s) and their winter seats. Shrines reopen around Akshaya Tritiya (late Apr – May).
