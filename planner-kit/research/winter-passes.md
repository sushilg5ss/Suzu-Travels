# Winter passes (v1.9, 3 Nov 2026)

Used by `WP` + `leg()` in `src/planner.js`. Rule of thumb, always phrased "about / usually" in the UI.

| Pass / road | Planner rule | Sources (checked 3 Nov 2026) |
|---|---|---|
| Kunzum Pass (Gramphu – Kaza, Manali/Lahaul ↔ Spiti) | closed outside Jun–Oct → Spiti legs that would cross Kunzum are re-routed via Kinnaur (Nako); warning | https://en.wikipedia.org/wiki/Kunzum_Pass · https://tribuneindia.com/news/gramphu-kaza-highway-officially-closed-for-traffic-via-kunzum-pass · https://discoverkullumanali.in/manali-spiti-road-opens-after-eight-months/ · https://www.outlooktraveller.com/travelnews/kunzum-pass-reopened-after-months-of-closure |
| Manali – Leh highway (Baralacha La, Tanglang La; detected = road passes Sarchu) | closed outside Jun–Oct → warning "fly into Leh or via Srinagar–Zojila" | https://www.tribuneindia.com/news/himachal/manali-leh-highway-via-atal-tunnel-closes-beyond-solang-after-fresh-snowfall-in-himachal-449545 |
| Zojila Pass (Srinagar – Kargil – Leh) | closed Jan–Mar (reopened 28 Feb–mid Apr in recent years) → fly-in warning; Dec & Apr → "can close a few days" | https://www.tribuneindia.com/news/j-k/srinagar-leh-road-reopens-after-73-days-378993 · https://www.tribuneindia.com/news/j-k/srinagar-leh-road-reopens-after-2-months-218791 · https://www.drishtiias.com/daily-updates/daily-news-analysis/zojila-pass-and-razdan-pass-reopen-after-short-winter-closure/print_manually |

Detection uses the OSRM km matrix: a Spiti leg (Kaza/Tabo ↔ X) "enters through Kinnaur" when km(X,Nako)+km(Nako,Spiti) ≤ km(X,Spiti)+15; otherwise it crosses Kunzum (25 pairs: Manali, Sissu, Jispa, Sarchu, Ladakh, Sonamarg/Baltal). Chandratal is skipped (already "closed" by its own months).
