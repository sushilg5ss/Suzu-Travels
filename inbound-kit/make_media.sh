#!/usr/bin/env bash
# Suzu Inbound Kit — render one HyperFrames composition and encode it for the web.
#   bash make_media.sh <composition> <media-slug> <hero|explainer> [poster-second]
#     composition = photo-hero   (hero,      reads src/media/<media-slug>.json "hero"  -> media/<slug>/hero{,-m}.mp4/.webm + hero-poster.webp)
#                 | route-map    (explainer, reads "route" -> route.mp4/.webm + route-poster.webp)
#                 | cost-ladder  (explainer, reads "cost"  -> cost.mp4/.webm  + cost-poster.webp)
# e.g. bash make_media.sh photo-hero india-2-week-itinerary hero 0        (poster = first frame, so the loop starts on it)
#      bash make_media.sh route-map  india-2-week-itinerary explainer 11
#      bash make_media.sh cost-ladder private-driver-india explainer 13
# Budgets: hero.mp4 <= 2.5 MB, hero-m.mp4 <= 1 MB, hero-poster.webp <= 45 KB (LCP), explainers <= 2 MB. Photo heroes compress worse than vector art, so the
# defaults are CRF 29 (hero) / 30 (hero-m) / 26 (explainers). If a file is over budget: CRF_ADD=2 ENCODE_ONLY=1 bash make_media.sh ...
# re-encodes the existing master (no 8-minute re-render) with the CRF raised by 2. POSTER_ONLY=1 rebuilds just the poster from media/<slug>/hero.mp4.
# Then: git add + commit + push, python3 pin_media.py <media-slug> $(git rev-parse HEAD), commit + push media.json.
# ALWAYS look at the contact sheet printed below before trusting a render (Read the .jpg).
# SNAP_ONLY=1 bash make_media.sh ...  -> composition + contact sheet only (fast check, no render).
set -euo pipefail
COMP="$1"; SLUG="$2"; KIND="${3:-hero}"; PT="${4:-0}"
KIT="$(cd "$(dirname "$0")" && pwd)"
export IK_HF_OUT="${IK_HF_OUT:-$KIT/../../ik-hf}"
HF="npx -y hyperframes@0.8.85"
case "$COMP" in
  photo-hero)  NAME="hero" ;;
  route-map)   NAME="route" ;;
  cost-ladder) NAME="cost" ;;
  *) echo "unknown composition $COMP (photo-hero | route-map | cost-ladder)"; exit 2 ;;
esac
OUT="$KIT/media/$SLUG"
if [[ "${POSTER_ONLY:-0}" == 1 ]]; then  # poster only, from the already-encoded hero.mp4 (no composition, no render)
  M="$OUT/$NAME.mp4"; [[ -s "$M" ]] || { echo "POSTER_ONLY: no $M"; exit 2; }
  for Q in 42 38 34 30; do
    ffmpeg -y -loglevel error -ss "$PT" -i "$M" -vf "scale=1280:-2" -frames:v 1 -c:v libwebp -compression_level 6 -q:v $Q "$OUT/$NAME-poster.webp"
    [[ $(stat -c %s "$OUT/$NAME-poster.webp") -le 46080 ]] && break
  done
  ls -la "$OUT/$NAME-poster.webp"; exit 0
fi
python3 "$KIT/gen_media.py" "$COMP" "$SLUG" >/dev/null
D="$IK_HF_OUT/$SLUG-$NAME"
mkdir -p "$OUT" "$KIT/compositions/$SLUG-$NAME"
if [[ "$KIND" == hero ]]; then AT="1.5,5,8.5,12"; else AT="3,7,11,12.5"; fi
(cd "$D" && rm -rf snapshots && $HF snapshot --at "$AT" >/dev/null 2>&1) || echo "snapshot failed (render anyway)"
echo "LOOK AT THIS before trusting the render: $D/snapshots/contact-sheet.jpg"
if [[ "${SNAP_ONLY:-0}" == 1 ]]; then exit 0; fi
M="$D/out/master.mp4"
if [[ "${ENCODE_ONLY:-0}" == 1 && -s "$M" ]]; then echo "ENCODE_ONLY: reusing $M"; else (cd "$D" && $HF render -o out/master.mp4); fi
A="${CRF_ADD:-0}"
if [[ "$KIND" == hero ]]; then
  ffmpeg -y -loglevel error -i "$M" -vf "scale=1600:-2" -c:v libx264 -crf $((29 + A)) -preset slow -pix_fmt yuv420p -movflags +faststart -an "$OUT/$NAME.mp4"
  ffmpeg -y -loglevel error -i "$M" -vf "scale=1600:-2" -c:v libvpx-vp9 -crf $((41 + A)) -b:v 0 -row-mt 1 -an "$OUT/$NAME.webm"
  ffmpeg -y -loglevel error -i "$M" -vf "scale=960:-2" -c:v libx264 -crf $((30 + A)) -preset slow -pix_fmt yuv420p -movflags +faststart -an "$OUT/$NAME-m.mp4"
  ffmpeg -y -loglevel error -i "$M" -vf "scale=960:-2" -c:v libvpx-vp9 -crf $((43 + A)) -b:v 0 -row-mt 1 -an "$OUT/$NAME-m.webm"
  # Poster = the page's LCP element (Reviewer, 17 Oct 2026): 1280 px, <= 45 KB. Start at q 42 and step down until it fits.
  for Q in 42 38 34 30; do
    ffmpeg -y -loglevel error -ss "$PT" -i "$M" -vf "scale=1280:-2" -frames:v 1 -c:v libwebp -compression_level 6 -q:v $Q "$OUT/$NAME-poster.webp"
    [[ $(stat -c %s "$OUT/$NAME-poster.webp") -le 46080 ]] && break
  done
else
  ffmpeg -y -loglevel error -i "$M" -vf "scale=1280:-2" -c:v libx264 -crf $((26 + A)) -preset slow -pix_fmt yuv420p -movflags +faststart -an "$OUT/$NAME.mp4"
  ffmpeg -y -loglevel error -i "$M" -vf "scale=1280:-2" -c:v libvpx-vp9 -crf $((37 + A)) -b:v 0 -row-mt 1 -an "$OUT/$NAME.webm"
  ffmpeg -y -loglevel error -ss "$PT" -i "$M" -vf "scale=1280:-2" -frames:v 1 -q:v 75 "$OUT/$NAME-poster.webp"
fi
cp "$D/index.html" "$KIT/compositions/$SLUG-$NAME/index.html"
ls -la "$OUT" | grep "$NAME"
python3 - "$OUT" "$NAME" "$KIND" <<'PY'
import os, sys
out, name, kind = sys.argv[1:4]
lim = {"hero": {f"{name}.mp4": 2.5e6, f"{name}-m.mp4": 1e6, f"{name}-poster.webp": 46080}, "explainer": {f"{name}.mp4": 2e6}}[kind]
over = [f"{f} {os.path.getsize(os.path.join(out, f)) / 1e6:.2f} MB" for f, l in lim.items() if os.path.getsize(os.path.join(out, f)) > l]
print("OVER BUDGET -> CRF_ADD=2 ENCODE_ONLY=1 bash make_media.sh ... :", ", ".join(over)) if over else print("sizes within budget")
PY
