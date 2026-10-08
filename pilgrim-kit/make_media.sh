#!/usr/bin/env bash
# Suzu Pilgrim Kit — render one HyperFrames composition and encode it for the web.
#   bash make_media.sh <composition> <media-slug> <hero|explainer> [poster-second]
#     composition = pilgrim-hero | light-map                         (section-level, fixed; media-slug = pilgrimage-tours)
#                 | temple-hero | story-strip | route-map            (per page: reads src/media/<media-slug>.json)
# e.g. bash make_media.sh pilgrim-hero pilgrimage-tours hero 0
#      bash make_media.sh temple-hero 12-jyotirlinga hero 0
#      bash make_media.sh light-map 12-jyotirlinga explainer 12
# Output: pilgrim-kit/media/<media-slug>/<name>{,-m}.{mp4,webm} + <name>-poster.webp
#   name = composition name for section-level ones; hero / story / route for per-page ones.
# ALWAYS look at the contact sheet printed below before trusting a render (Read the .jpg).
# SNAP_ONLY=1 bash make_media.sh ...  -> composition + contact sheet only.
set -euo pipefail
COMP="$1"; SLUG="$2"; KIND="${3:-hero}"; PT="${4:-0}"
KIT="$(cd "$(dirname "$0")" && pwd)"
export PK_HF_OUT="${PK_HF_OUT:-$KIT/../../pk-hf}"
HF="npx -y hyperframes@0.8.85"
case "$COMP" in
  temple-hero) python3 "$KIT/gen_media.py" temple-hero "$SLUG" >/dev/null; D="$PK_HF_OUT/$SLUG-hero";  NAME="hero" ;;
  story-strip) python3 "$KIT/gen_media.py" story-strip "$SLUG" >/dev/null; D="$PK_HF_OUT/$SLUG-story"; NAME="story" ;;
  route-map)   python3 "$KIT/gen_media.py" route-map "$SLUG" >/dev/null;   D="$PK_HF_OUT/$SLUG-route"; NAME="route" ;;
  *)           python3 "$KIT/gen_media.py" "$COMP" >/dev/null;             D="$PK_HF_OUT/$COMP";       NAME="$COMP" ;;
esac
OUT="$KIT/media/$SLUG"; mkdir -p "$OUT" "$KIT/compositions/$SLUG-$NAME"
if [[ "$KIND" == hero ]]; then AT="1.5,5,8.5,12"; else AT="3,7,11,12.5"; fi
(cd "$D" && rm -rf snapshots && $HF snapshot --at "$AT" >/dev/null 2>&1) || echo "snapshot failed (render anyway)"
echo "LOOK AT THIS before trusting the render: $D/snapshots/contact-sheet.jpg"
if [[ "${SNAP_ONLY:-0}" == 1 ]]; then exit 0; fi
(cd "$D" && $HF render -o out/master.mp4)
M="$D/out/master.mp4"
if [[ "$KIND" == hero ]]; then
  ffmpeg -y -loglevel error -i "$M" -vf "scale=1600:-2" -c:v libx264 -crf 27 -preset slow -pix_fmt yuv420p -movflags +faststart -an "$OUT/$NAME.mp4"
  ffmpeg -y -loglevel error -i "$M" -vf "scale=1600:-2" -c:v libvpx-vp9 -crf 40 -b:v 0 -row-mt 1 -an "$OUT/$NAME.webm"
  ffmpeg -y -loglevel error -i "$M" -vf "scale=960:-2" -c:v libx264 -crf 28 -preset slow -pix_fmt yuv420p -movflags +faststart -an "$OUT/$NAME-m.mp4"
  ffmpeg -y -loglevel error -i "$M" -vf "scale=960:-2" -c:v libvpx-vp9 -crf 41 -b:v 0 -row-mt 1 -an "$OUT/$NAME-m.webm"
  ffmpeg -y -loglevel error -ss "$PT" -i "$M" -vf "scale=1600:-2" -frames:v 1 -q:v 72 "$OUT/$NAME-poster.webp"
else
  ffmpeg -y -loglevel error -i "$M" -vf "scale=1280:-2" -c:v libx264 -crf 26 -preset slow -pix_fmt yuv420p -movflags +faststart -an "$OUT/$NAME.mp4"
  ffmpeg -y -loglevel error -i "$M" -vf "scale=1280:-2" -c:v libvpx-vp9 -crf 37 -b:v 0 -row-mt 1 -an "$OUT/$NAME.webm"
  ffmpeg -y -loglevel error -ss "$PT" -i "$M" -vf "scale=1280:-2" -frames:v 1 -q:v 75 "$OUT/$NAME-poster.webp"
fi
cp "$D/index.html" "$KIT/compositions/$SLUG-$NAME/index.html"
ls -la "$OUT" | grep "$NAME"
