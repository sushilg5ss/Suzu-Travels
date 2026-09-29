#!/usr/bin/env bash
# Suzu Cab Kit — render the HyperFrames media for one page and encode it for the web.
#   bash make_media.sh <slug> [hero|route|both]      (default: both)
# Needs: node/npx, ffmpeg. Output: cab-kit/media/<slug>/{hero,route}.{mp4,webm} + *-poster.webp,
# and the composition sources in cab-kit/compositions/<slug>/. Then commit, push, and pin the SHA in media.json
# (python3 pin_media.py <slug> <sha>).
set -euo pipefail
SLUG="$1"; WHAT="${2:-both}"
KIT="$(cd "$(dirname "$0")" && pwd)"
export CAB_HF_OUT="${CAB_HF_OUT:-$KIT/../../cab-hf}"
HF="npx -y hyperframes@0.8.85"
OUT="$KIT/media/$SLUG"; mkdir -p "$OUT" "$KIT/compositions/$SLUG"

if [[ "$WHAT" == hero || "$WHAT" == both ]]; then
  python3 "$KIT/gen_hero.py" "$SLUG" >/dev/null
  D="$CAB_HF_OUT/heroes/$SLUG"
  (cd "$D" && $HF snapshot --at 1,4.5 --describe false >/dev/null 2>&1 || true)
  (cd "$D" && $HF render -o out/master.mp4)
  ffmpeg -y -loglevel error -i "$D/out/master.mp4" -vf "scale=1600:-2" -c:v libx264 -crf 28 -preset slow -pix_fmt yuv420p -movflags +faststart -an "$OUT/hero.mp4"
  ffmpeg -y -loglevel error -i "$D/out/master.mp4" -vf "scale=1600:-2" -c:v libvpx-vp9 -crf 40 -b:v 0 -row-mt 1 -an "$OUT/hero.webm"
  ffmpeg -y -loglevel error -i "$D/out/master.mp4" -vf "select=eq(n\,0),scale=1600:-2" -frames:v 1 "$OUT/hero-poster.webp"
  cp "$D/index.html" "$KIT/compositions/$SLUG/hero.html"
  echo "hero done: $(du -h "$OUT/hero.mp4" | cut -f1) mp4, $(du -h "$OUT/hero.webm" | cut -f1) webm"
fi

if [[ "$WHAT" == route || "$WHAT" == both ]]; then
  python3 "$KIT/gen_route.py" "$SLUG" >/dev/null
  D="$CAB_HF_OUT/routes/$SLUG"
  (cd "$D" && $HF snapshot --at 6.5 --no-end --describe false >/dev/null 2>&1 || $HF snapshot --at 6.5 --describe false >/dev/null 2>&1 || true)
  echo "LOOK at the snapshot before trusting the render (label overlaps!): $(ls -1 "$D"/snapshots/* 2>/dev/null | head -3 | tr '\n' ' ')"
  (cd "$D" && $HF render -o out/master.mp4)
  ffmpeg -y -loglevel error -i "$D/out/master.mp4" -vf "scale=1280:-2" -c:v libx264 -crf 27 -preset slow -pix_fmt yuv420p -movflags +faststart -an "$OUT/route.mp4"
  ffmpeg -y -loglevel error -i "$D/out/master.mp4" -vf "scale=1280:-2" -c:v libvpx-vp9 -crf 38 -b:v 0 -row-mt 1 -an "$OUT/route.webm"
  ffmpeg -y -loglevel error -ss 6.5 -i "$D/out/master.mp4" -vf "scale=1280:-2" -frames:v 1 "$OUT/route-poster.webp"
  cp "$D/index.html" "$KIT/compositions/$SLUG/route.html"
  echo "route done: $(du -h "$OUT/route.mp4" | cut -f1) mp4, $(du -h "$OUT/route.webm" | cut -f1) webm"
fi
