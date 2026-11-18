# ropeways-in-himachal (WP 15192) — #jakhu-ways explainer figure (Visual Studio, 18 Nov 2026)

Inserted at the end of `#spots` (just before `</section><section class="sza-sec" id="experience">`), one line:

```html
<figure id="jakhu-ways" style="margin:32px auto 0;max-width:880px"><video poster="https://suzutravels.com/wp-content/uploads/2026/11/jakhu-ropeway-shimla-three-ways-explainer-poster.webp" autoplay muted loop playsinline preload="none" width="1600" height="900" style="display:block;width:100%;height:auto;aspect-ratio:16/9;border-radius:18px;background:#0b1f33;box-shadow:0 12px 32px rgba(11,31,51,.2)" aria-label="11-second motion graphic: three ways up from the Ridge at about 2,200 m to Jakhu temple at about 2,455 m. Ropeway about 5 to 8 minutes over about 450 m of cable in cabins for about 6; walk 2 to 2.5 km, steep, 40 to 60 minutes through deodars; or taxi up the hill road and the escalator. December to February the ropeway stops in heavy snow or wind. Ropeway, cab and hotel: Get Quote"><source src="https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@253bc50cfbfffe10359d874e45838f78658741c2/adventure-kit/media/jakhu-ropeway-shimla/explainer.webm" type="video/webm"><source src="https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@253bc50cfbfffe10359d874e45838f78658741c2/adventure-kit/media/jakhu-ropeway-shimla/explainer.mp4" type="video/mp4"></video><figcaption style="margin-top:10px;font-size:15px;line-height:1.5;color:#3b4a5a;text-align:center">Jakhu in Shimla: ride about 5–8 minutes from near the Ridge, walk 2–2.5 km uphill, or take a taxi to near the top. In heavy snow or wind the ropeway stops, so we keep a taxi backup for the same slot. <a href="/pilgrimage-tours/jakhu-temple/" style="color:#0b1f33;font-weight:700">Jakhu temple darshan guide →</a></figcaption></figure>
```

Live: https://suzutravels.com/adventure/ropeways-in-himachal/#jakhu-ways
Undo: wp_replace_in_page 15192 — remove the `<figure id="jakhu-ways" …></figure>` before `</section><section class="sza-sec" id="experience">`.
When /adventure/jakhu-ropeway-shimla/ goes live, the Jakhu card "Explore →" should point there (Page Builder) and the caption can gain one link to it.
