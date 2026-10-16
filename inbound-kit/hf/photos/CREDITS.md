# Photo library for the Inbound Kit videos (`photo-hero`)

All photos here are from **Pexels** under the [Pexels License](https://www.pexels.com/license/) (free to use, including commercially, no attribution required — we credit anyway). Never add a photo from Google Images, a competitor site or any unlicensed source. Suzu's own guest photos may be used only when they already sit on suzutravels.com uploads with permission (`intl/` precedent).

Each file is re-sized for HyperFrames scenes:
- `land` = landscape, **2112 wide** (centred in the 1920×1080 frame, slow scale/x/y pan)
- `tilt` = portrait, **1920 wide**, at least 2160 tall (bottom-aligned, slow vertical pan)

**Honesty rule.** A photo may be captioned as a place only when the "shows" column says it is that place. Nothing else may carry a place name in a video caption or alt text. Faces: no private person as the main subject. Mirroring (`"mirror": true`) is allowed only where this table says there is no writing, signage or logo in the frame.

| file | kind / size | shows | photographer | licence | source URL | allowed captions | mirror? | added |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| px-33777272.jpg | tilt 1920×2400 | Taj Mahal, Agra, front view with its reflection in the long pool, overcast morning sky, cypress rows both sides, a few distant visitors | Ryan Thomas | Pexels | https://www.pexels.com/photo/majestic-taj-mahal-reflection-at-sunrise-in-agra-33777272/ | "Taj Mahal", "Agra", "Taj at dawn" | no (symmetry; keep as shot) | 2026-10-16 |
| px-29295304.jpg | tilt 1920×2560 | Hawa Mahal, Jaipur — the pink-red latticed facade shot from below against a moody grey sky, no people | Gowri Manoj | Pexels | https://www.pexels.com/photo/spectacular-view-of-hawa-mahal-in-jaipur-india-29295304/ | "Hawa Mahal", "Jaipur", "Pink City" | yes (no writing) | 2026-10-16 |
| px-3672388.jpg | land 2112×1408 | Humayun's Tomb, New Delhi — red sandstone tomb with white dome, palms left, lawn in front, blue sky | shalender kumar | Pexels | https://www.pexels.com/photo/humayun-s-tomb-under-blue-sky-3672388/ | "Humayun's Tomb", "Delhi" | yes (no writing) | 2026-10-16 |
| px-28206557.jpg | tilt 1920×2400 | Manali valley, Himachal — green valley with village houses, snow peaks behind, a string of coloured prayer flags across the top | Prajwal Malve | Pexels | https://www.pexels.com/photo/snow-28206557/ | "Manali", "Himachal hills", "Kullu valley" | no (prayer-flag script) | 2026-10-16 |

**Adding a photo** (Visual Studio, at most 4 per run).
1. Find candidates with WebSearch/WebFetch on pexels.com (or unsplash.com) for the exact place. The photo page gives the photographer; the image itself downloads from the CDN: `https://images.pexels.com/photos/<id>/pexels-photo-<id>.jpeg?auto=compress&cs=tinysrgb&w=2400` (checked 16 Oct 2026; pexels.com pages 403 to curl).
2. **Look at the image** (Read) before using it: no private faces as the subject, no mirrored signage, nothing that contradicts the caption.
3. Resize with PIL to `land` (2112 wide) or `tilt` (1920 wide), JPEG ≤ ~900 KB, saved as `hf/photos/px-<id>.jpg` (Unsplash: `us-<id>.jpg`).
4. Add a row above with what the photo really shows, the photographer, licence, source URL, allowed captions, mirror rule and date.
