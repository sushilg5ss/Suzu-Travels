# camping-near-shimla-kasauli (WP 19389) — hero video (live 12 Nov 2026, Visual Studio night)

Replaced the static hero image in `.sza-hero` with a 12 s seamless hero loop (media @8a306d8e4379fede5fad782175e334758bc416d9, poster WP 21436). Apply the same on any rebuild:

FIND:
<img class="sza-hero-img" src="https://suzutravels.com/wp-content/uploads/2026/10/lit-canvas-tent-pine-forest-night.webp" alt="A glowing canvas tent among tall pine trees under a starry night sky" loading="eager">

REPLACE:
<video autoplay muted loop playsinline preload="metadata" style="object-position:0% 50%" poster="https://suzutravels.com/wp-content/uploads/2026/11/camping-near-shimla-kasauli-hero-poster.webp" aria-label="A glowing canvas tent among pines at night, lit dome tents at dusk, a bonfire and tents on a hilltop meadow at sunrise, with a gold road line from Chandigarh via Kasauli (58 km) to the Shimla camps"><source src="https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@8a306d8e4379fede5fad782175e334758bc416d9/adventure-kit/media/camping-near-shimla-kasauli/hero.webm" type="video/webm"><source src="https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@8a306d8e4379fede5fad782175e334758bc416d9/adventure-kit/media/camping-near-shimla-kasauli/hero.mp4" type="video/mp4"></video>

`object-position:0% 50%` keeps the video's own title (right half) out of the mobile crop so it never overlaps the page tagline at 390 px.
Video: tent at night → dome tents at dusk → bonfire → hilltop tents at sunrise (all existing page photos); right half "Camping near Shimla / one night under the pines", road line Chandigarh → Kasauli 58 km → Shimla camps, counter ~115 km; facts Swiss and alpine tents · Bonfire where the camp allows · Narkanda camps for snow · We add your cab, both ways. hero.mp4 1.07 MB / hero.webm 0.93 MB / poster 54 KB, seam 1.1/255.
Verified 12 Nov 2026: ?v + plain fetch 200, video present, index robots; Playwright 1366 & 390: readyState 4 (webm), no overflow, one H1.
