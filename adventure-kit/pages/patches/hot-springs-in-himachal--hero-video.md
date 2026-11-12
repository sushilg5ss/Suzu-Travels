# hot-springs-in-himachal (WP 18598) — hero video (live 13 Nov 2026 IST, Visual Studio night)

Replaced the static hero image in `.sza-hero` with a 12 s seamless hero loop (media @4a3290fbba9d1323ad19506da85ee72514a646c9, poster WP 21653). Apply the same on any rebuild:

FIND:
<img class="sza-hero-img" src="https://suzutravels.com/wp-content/uploads/2026/10/steam-rising-over-hot-spring-pool.webp" alt="Steam rising over a warm natural pool edged with rocks on a cool morning" loading="eager">

REPLACE:
<video autoplay muted loop playsinline preload="metadata" style="object-position:0% 50%" poster="https://suzutravels.com/wp-content/uploads/2026/11/hot-springs-in-himachal-hero-poster.webp" aria-label="Steam rising over a warm rock-edged pool, a wooden Himachali temple below forested mountains and a wide river valley, with the words Hot springs of Himachal: Vashisht 3 km from Manali, Manikaran about 4 km past Kasol, Tattapani about 52 km from Shimla, best soak season December to February"><source src="https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@4a3290fbba9d1323ad19506da85ee72514a646c9/adventure-kit/media/hot-springs-in-himachal/hero.webm" type="video/webm"><source src="https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@4a3290fbba9d1323ad19506da85ee72514a646c9/adventure-kit/media/hot-springs-in-himachal/hero.mp4" type="video/mp4"></video>

Video: steaming pool → wooden Himachali temple → river valley → pool (existing page photos, no place labels on screen); right half "Hot springs / of Himachal", rising steam lines over a gold water line, counter 0 → 5 springs; facts Vashisht · 3 km from Manali · Manikaran · ~4 km past Kasol · Tattapani · ~52 km from Shimla · Best soak season Dec – Feb (all from the page's own chips). hero.mp4 0.92 MB / hero.webm 0.81 MB / poster 51 KB, seam 0.8/255.
Verified: ?v + plain fetch 200, video present, index robots; Playwright 1366 & 390: readyState 4 (webm), no overflow, one H1, no page errors.
