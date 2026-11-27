# adventure-activities-in-shimla (page 15439) — #booking explainer (Visual Studio, 27 Nov 2026)

Live change via wp_replace_in_page (1 occurrence). In section #booking, the .sza-media image (duplicate of the Treks & camps card photo, hiker-on-grassy-ridge-trail-pine-valley-768x512.webp) was replaced by a 10 s motion graphic of the page's own 4 booking steps.

Find:
`<div class="sza-media"><img src="https://suzutravels.com/wp-content/uploads/2026/10/hiker-on-grassy-ridge-trail-pine-valley-768x512.webp" alt="Hiker with a backpack walking a narrow grassy ridge trail past a pine tree, with forested mountains and snow patches across the valley" loading="lazy" width="768" height="512">`

Replace (one line):
`<div class="sza-media" id="booking-explainer"><video poster="https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@4488a29459946471559f0d585a79247b21de9dff/adventure-kit/media/adventure-activities-in-shimla/booking-explainer-poster.webp" autoplay muted loop playsinline preload="metadata" width="1600" height="900" style="display:block;width:100%;height:auto;aspect-ratio:16/9;border-radius:14px;background:#0b1f33" aria-label="10-second motion graphic, how booking works: 1 tell us your dates, activities and group; 2 we check weather, snow, river level and a registered operator; 3 you get one quote for activities, hotel and cab; 4 confirm and go"><source src="https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@4488a29459946471559f0d585a79247b21de9dff/adventure-kit/media/adventure-activities-in-shimla/booking-explainer.webm" type="video/webm"><source src="https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@4488a29459946471559f0d585a79247b21de9dff/adventure-kit/media/adventure-activities-in-shimla/booking-explainer.mp4" type="video/mp4"></video>`

Poster also in WP: 25995. Source: media/adventure-activities-in-shimla/adventure-activities-in-shimla-booking-explainer.html. Undo: swap back to the Find string.
