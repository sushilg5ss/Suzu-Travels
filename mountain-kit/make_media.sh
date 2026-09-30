#!/usr/bin/env bash
# Suzu Mountain Kit — render one HyperFrames composition and encode it for the web.
#   bash make_media.sh <composition> <media-slug> <hero|explainer> [poster-second]
#     composition = mountains-hero | height-ladder | expeditions-hero        (section-level, fixed)
#                 | peak-hero | route-profile | peak-ladder                (per page: reads src/media/<media-slug>.json)
# e.g. bash make_media.sh peak-hero friendship-peak hero 0          (poster = first frame, so the loop starts on it)
#      bash make_media.sh route-profile friendship-peak explainer 11
#      bash make_media.sh peak-ladder 7000m-peaks explainer 13
# Output: mountain-kit/media/<media-slug>/<name>{,-m}.{mp4,webm} + <name>-poster.webp
#         name = the composition for section-level ones; hero / profile / ladder for per-page ones.
#         hero -> 1600 w + 960 w (mobile) mp4/webm; explainer -> 1280 w mp4/webm. Keep each hero file under ~2.5 MB.
# Then: git add + commit + push, python3 pin_media.py <media-slug> $(git rev-parse HEAD), commit + push media.json.
# ALWAYS look at the contact sheet the script prints before trusting a render (Read the .jpg).
# SNAP_ONLY=1 bash make_media.sh ...   -> builds the composition + contact sheet only (fast check, no render).
set -euo pipefail
COMP="$1"; SLUG="$2"; KIND="${3:-hero}"; PT="${4:-0}"
KIT="$(cd "$(dirname "$0")" && pwd)"
export MK_HF_OUT="${MK_HF_OUT:-$KIT/../../mk-hf}"
HF="npx -y hyperframes@0.8.85"
case "$COMP" in
  peak-hero)     python3 "$KIT/gen_media.py" peak-hero "$SLUG" >/dev/null;     D="$MK_HF_OUT/$SLUG-hero";    NAME="hero" ;;
  route-profile) python3 "$KIT/gen_media.py" route-profile "$SLUG" >/dev/null; D="$MK_HF_OUT/$SLUG-profile"; NAME="profile" ;;
  peak-ladder)   python3 "$KIT/gen_media.py" peak-ladder "$SLUG" >/dev/null;   D="$MK_HF_OUT/$SLUG-ladder";  NAME="ladder" ;;
  *)             python3 "$KIT/gen_media.py" "$COMP" >/dev/null;              D="$MK_HF_OUT/$COMP";         NAME="$COMP" ;;
esac
OUT="$KIT/media/$SLUG"; mkdir -p "$OUT" "$KIT/compositions/$SLUG-$NAME"
if [[ "$KIND" == hero ]]; then AT="1.5,5,8.5,12"; else AT="4,8,11"; fi
(cd "$D" && rm -rf snapshots && $HF snapshot --at "$AT" >/dev/null 2>&1) || echo "snapshot failed (render anyway)"
echo "LOOK AT THIS before trusting the render: $D/snapshots/contact-sheet.jpg"
if [[ "${SNAP_ONLY:-0}" == 1 ]]; then exit 0; fi
(cd "$D" && $HF render -o out/master.mp4)
M="$D/out/master.mp4"
if [[ "$KIND" == hero ]]; then
  ffmpeg -y -loglevel error -i "$M" -vf "scale=1600:-2" -c:v libx264 -crf 28 -preset slow -pix_fmt yuv420p -movflags +faststart -an "$OUT/$NAME.mp4"
  ffmpeg -y -loglevel error -i "$M" -vf "scale=1600:-2" -c:v libvpx-vp9 -crf 41 -b:v 0 -row-mt 1 -an "$OUT/$NAME.webm"
  ffmpeg -y -loglevel error -i "$M" -vf "scale=960:-2" -c:v libx264 -crf 29 -preset slow -pix_fmt yuv420p -movflags +faststart -an "$OUT/$NAME-m.mp4"
  ffmpeg -y -loglevel error -i "$M" -vf "scale=960:-2" -c:v libvpx-vp9 -crf 42 -b:v 0 -row-mt 1 -an "$OUT/$NAME-m.webm"
  ffmpeg -y -loglevel error -ss "$PT" -i "$M" -vf "scale=1600:-2" -frames:v 1 -q:v 70 "$OUT/$NAME-poster.webp"
else
  ffmpeg -y -loglevel error -i "$M" -vf "scale=1280:-2" -c:v libx264 -crf 27 -preset slow -pix_fmt yuv420p -movflags +faststart -an "$OUT/$NAME.mp4"
  ffmpeg -y -loglevel error -i "$M" -vf "scale=1280:-2" -c:v libvpx-vp9 -crf 38 -b:v 0 -row-mt 1 -an "$OUT/$NAME.webm"
  ffmpeg -y -loglevel error -ss "$PT" -i "$M" -vf "scale=1280:-2" -frames:v 1 -q:v 75 "$OUT/$NAME-poster.webp"
fi
cp "$D/index.html" "$KIT/compositions/$SLUG-$NAME/index.html"
ls -la "$OUT" | grep "$NAME"
