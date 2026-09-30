# Photo library for the Mountain Kit videos

All photos are from Pexels under the **Pexels License** (free to use, including commercially, with no attribution required).
Each one is re-sized for HyperFrames scenes:
- `land` = landscape, 2112 wide
- `tilt` = portrait, 1920 wide, used for slow vertical pans

**Honesty rule.** A photo may be captioned with a peak's name only when the "Shows" column below says it is that peak and a source confirms it. Everything else is a generic climbing or snow shot. Never write a peak's name over a generic photo in a video, and never describe one that way in alt text.

| File | Kind / size | Shows | Mirror? | Notes |
|---|---|---|---|---|
| px-15148510.jpg | land 2112×1408 | Aerial view of a vast snowfield with a line of roped climbers | ok | Great "scale" shot for any page |
| px-20809686.jpg | tilt 1920×2560 | Orange tent glowing at night on snow, under a starry sky | ok | "High camp" scene |
| px-30701907.jpg | land 2112×1408 | **Kangchenjunga** at sunrise, verified 30 Sep 2026 | **no** | The only named-peak photo. Use it for Kangchenjunga or India's highest, never as any other peak |
| px-32109154.jpg | tilt 1920×2560 | Roped team in red jackets climbing a snow slope | ok | Classic "summit push" |
| px-35319376.jpg | tilt 1920×2560 | Climber with a red pack on a snow trail; others ahead | **no** | Helly Hansen logo on trousers |
| px-37358046.jpg | tilt 1920×2880 | Climber on a steep snow and ice ridge, blue sky | **no** | SCARPA logo on the boot would read backwards |
| px-38468349.jpg | land 2112×1406 | Night ascent: a line of headlamps on a snow slope | ok | Mirrored in the hub hero |
| px-38468355.jpg | land 2112×1406 | Portrait of a climber (red jacket, helmet, ice axe) | **no** | Mont-bell logo on the jacket |
| px-38930225.jpg | land 2112×1188 | Snowy mountain range under cloud (not a named peak) | ok | Wide establishing shot |
| px-9683997.jpg | land 2112×1408 | Two climbers on a corniced snow ridge | ok | "Ridge" or "summit day" |

**Adding a photo.**
1. Find candidate photo IDs with WebSearch or WebFetch, e.g. "pexels mountaineer snow ridge". pexels.com pages return 403 to curl, but the image CDN works: download the large JPEG with curl from `https://images.pexels.com/photos/<id>/pexels-photo-<id>.jpeg?auto=compress&cs=tinysrgb&w=2400` (checked 1 Oct 2026). Look at the image (Read) before using it.
2. Resize and crop it to `land` (2112 wide) or `tilt` (1920 wide, at least 2560 tall) with Python PIL, as `hf/photos/px-<id>.jpg`.
3. Keep it under about 900 KB.
4. Add a row to the table above with the photo's real content, and note any logos.
5. If the photo claims to show a named peak, cite the Pexels page and a second source that confirms it.
