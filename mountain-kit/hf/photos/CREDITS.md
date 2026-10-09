# Photo library for the Mountain Kit videos

All photos are from Pexels under the **Pexels License** (free to use, including commercially, with no attribution required).
Each one is re-sized for HyperFrames scenes:
- `land` = landscape, 2112 wide
- `tilt` = portrait, 1920 wide, used for slow vertical pans

**Honesty rule.** A photo may be captioned with a peak's name only when the "Shows" column below says it is that peak and a source confirms it. Everything else is a generic climbing or snow shot. Never write a peak's name over a generic photo in a video, and never describe one that way in alt text.

| File | Kind / size | Shows | Mirror? | Notes |
|---|---|---|---|---|
| px-10254837.jpg | land 2112×1408 | Back view of a roped line of climbers with ice axes on a snow slope, rocks on the left | **no** | CAT logo on the yellow pack. Climbers fill the left half (good for the phone crop). Added 1 Oct 2026, pexels.com/photo/10254837 |
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
| px-17613105.jpg | tilt 1920×2880 | Hiker (pink beanie, dark pack) on brown scree with snow patches, a glaciated generic peak behind | **no** | Nike swoosh on the pack. Not a named peak. Use as Lahaul / high-desert approach. Added 4 Oct 2026, pexels.com/photo/17613105 |
| px-28409954.jpg | land 2112×1399 | Three roped climbers (helmets, ice axes) crossing a flat glacier under seracs and rock bands | ok | No logos seen. Climbers sit bottom-left (move the scene up ~y −190 to show them). "Glacier plateau" shot. Added 4 Oct 2026, pexels.com/photo/28409954 |
| px-35905430.jpg | tilt 1920×2880 | Two hikers with big packs picking through a giant-boulder moraine with old snow | **no** | Painted red-white trail mark on a boulder; no brand logos seen (kept no-mirror to be safe). Hikers in the lower third: keep y 0–500. "Moraine to base camp". Added 4 Oct 2026, pexels.com/photo/35905430 |
| px-37016841.jpg | tilt 1920×2880 | Close-up of two mountaineering boots with strap-on crampons biting into snow | **no** | Small wordmark on a boot (unreadable at hero size; keep no-mirror). Boots fill the left/centre (good for the phone crop); y 600–900 shows the crampon points. "Boots + crampons" gear shot. Added 6 Oct 2026, pexels.com/photo/37016841 |
| px-92081.jpg | land 2112×1408 | Hiker from behind in a hooded green shell jacket with a grey pack, on a snowfield; generic snow peaks behind (not a named peak) | **no** | Small red patch on the sleeve and a pack wordmark (unreadable at hero size; keep no-mirror). Heavy teal grade. Figure sits centre-right: use x ≈ −120…−180 at scale 1.06–1.12 to move it left of the text. "Shell / layers" shot. Added 8 Oct 2026, pexels.com/photo/92081 |
| px-14100743.jpg | tilt 1920×2560 | Grassy high meadow camp: a grey ridge tent in front, pink/red ridge tents behind, a green hill and a cloud-wrapped snow range (not a named peak) | **no** | No logos seen. Litter/rubbish on the ground below y ≈ 2300 — keep y ≤ 1100 so it never shows. Tents sit centre-left (good for the phone crop). "Base camp" shot. Added 9 Oct 2026, pexels.com/photo/14100743 |
| px-10555794.jpg | land 2112×1408 | Two lit dome tents (red and green) on deep snow at night, pine slope and snowy ridge behind (not a named peak) | **no** | No logos seen (kept no-mirror). Tents bottom-centre-left; text side stays clear at x ≈ −60…−140, scale 1.02–1.1. Lower, forested winter camp — use as "camp on snow", not as a summit camp. Added 9 Oct 2026, pexels.com/photo/10555794 |

**Adding a photo.**
1. Find candidate photo IDs with WebSearch or WebFetch, e.g. "pexels mountaineer snow ridge". pexels.com pages return 403 to curl, but the image CDN works: download the large JPEG with curl from `https://images.pexels.com/photos/<id>/pexels-photo-<id>.jpeg?auto=compress&cs=tinysrgb&w=2400` (checked 1 Oct 2026). Look at the image (Read) before using it.
2. Resize and crop it to `land` (2112 wide) or `tilt` (1920 wide, at least 2560 tall) with Python PIL, as `hf/photos/px-<id>.jpg`.
3. Keep it under about 900 KB.
4. Add a row to the table above with the photo's real content, and note any logos.
5. If the photo claims to show a named peak, cite the Pexels page and a second source that confirms it.
