# Hub 11529 — #treks category photo, sharper on hi-DPI screens (Visual Studio, 14 Nov 2026)

Live edit (wp_replace_in_page, expected_count 1) on the #treks category head image: added
`srcset="…/2026/10/treks-cathead-prashar-lake-768x480-1.webp 768w, …/2026/11/treks-cathead-prashar-lake-1600.webp 1600w" sizes="(max-width: 760px) 100vw, 560px"`.
Same Suzu trip photo (Prashar Lake aerial, WP 13810) re-cropped 16:10 at 1600×1000, WP 22230 (408 KB). 1x desktop keeps the 768 file; retina/phones get the 1600 file. Builder: SRCSET map in pages/adventure.py.
Undo: replace the srcset/sizes attributes with nothing.
