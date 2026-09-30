#!/usr/bin/env bash
# Suzu Mountain Kit — render one HyperFrames composition and encode it for the web.
#   bash make_media.sh <composition> <media-slug> <hero|explainer> [poster-second]
# e.g. bash make_media.sh mountains-hero mountains-of-india hero
#      bash make_media.sh height-ladder mountains-of-india explainer 14.4
# Needs: node/npx, ffmpeg. Output: mountain-kit/media/<media-slug>/<composition>{,-m}.{mp4,webm} + <composition>-poster.webp
# Commit + push, then pin the commit SHA in media.json (python3 pin_media.py <media-slug> <sha>).
set -euo pipefail
COMP="$1"; SLUG="$2"; KIND="${3:-hero}"; PT="${4:-0}"
KIT="$(cd "$(dirname "$0")" && pwd)"
export MK_HF_OUT="${MK_HF_OUT:-$KIT/../../mk-hf}"
HF="npx -y hyperframes@0.8.85"
python3 "$KIT/gen_media.py" "$COMP" >/dev/null
D="$MK_HF_OUT/$COMP"
OUT="$KIT/media/$SLUG"; mkdir -p "$OUT" "$KIT/compositions/$COMP"
(cd "$D" && $HF render -o out/master.mp4)
M="$D/out/master.mp4"
if [[ "$KIND" == hero ]]; then
  ffmpeg -y -loglevel error -i "$M" -vf "scale=1600:-2" -c:v libx264 -crf 28 -preset slow -pix_fmt yuv420p -movflags +faststart -an "$OUT/$COMP.mp4"
  ffmpeg -y -loglevel error -i "$M" -vf "scale=1600:-2" -c:v libvpx-vp9 -crf 41 -b:v 0 -row-mt 1 -an "$OUT/$COMP.webm"
  ffmpeg -y -loglevel error -i "$M" -vf "scale=960:-2" -c:v libx264 -crf 29 -preset slow -pix_fmt yuv420p -movflags +faststart -an "$OUT/$COMP-m.mp4"
  ffmpeg -y -loglevel error -i "$M" -vf "scale=960:-2" -c:v libvpx-vp9 -crf 42 -b:v 0 -row-mt 1 -an "$OUT/$COMP-m.webm"
  ffmpeg -y -loglevel error -ss "$PT" -i "$M" -vf "scale=1600:-2" -frames:v 1 -q:v 70 "$OUT/$COMP-poster.webp"
else
  ffmpeg -y -loglevel error -i "$M" -vf "scale=1280:-2" -c:v libx264 -crf 27 -preset slow -pix_fmt yuv420p -movflags +faststart -an "$OUT/$COMP.mp4"
  ffmpeg -y -loglevel error -i "$M" -vf "scale=1280:-2" -c:v libvpx-vp9 -crf 38 -b:v 0 -row-mt 1 -an "$OUT/$COMP.webm"
  ffmpeg -y -loglevel error -ss "$PT" -i "$M" -vf "scale=1280:-2" -frames:v 1 -q:v 75 "$OUT/$COMP-poster.webp"
fi
cp "$D/index.html" "$KIT/compositions/$COMP/index.html"
ls -la "$OUT" | grep "$COMP"
