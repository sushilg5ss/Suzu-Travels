#!/usr/bin/env bash
# Bharat Darshan episode runner.  usage: bd.sh <step> EP_DIR [args]
#   voice    EP_DIR [REF_WAV]   Chatterbox narration per line + ASR quality gate   (~12–18 min on 2 CPUs)
#   captions EP_DIR             word timings for captions
#   build    EP_DIR             HyperFrames project in EP_DIR/hf + lint (must be 0 errors)
#   snap     EP_DIR             snapshots at every scene midpoint -> EP_DIR/hf/snapshots/contact-sheet*.jpg
#   render   EP_DIR             silent 1080x1920 30fps render -> EP_DIR/hf/renders/video.mp4 (~15–20 min)
#   score    EP_DIR TRACK.mp3   music bed (licensed track) + SFX from timing cues
#   mix      EP_DIR             final mp4 -> EP_DIR/final/<slug>.mp4 (+ cover.jpg), -14 LUFS
#   qa       EP_DIR             duration / loudness / black-frame / ASR spot check of the final file
#   all      EP_DIR TRACK.mp3   everything after voice (captions→mix→qa), for re-runs after edits
set -euo pipefail
P="$(cd "$(dirname "$0")" && pwd)"
VENV="${VENV:-$HOME/bd-venv}"; source "$VENV/bin/activate"
step="$1"; EP="$(cd "$2" && pwd)"; shift 2
slug=$(python3 -c "import json;print(json.load(open('$EP/episode.json'))['slug'])")
case "$step" in
  voice)    python -u "$P/voice.py" "$EP" "${1:-$P/assets/narrator_ref.wav}" --asr medium ;;
  captions) python "$P/align.py" "$EP" --asr small ;;
  build)    python "$P/build.py" "$EP" && (cd "$EP/hf" && hyperframes lint 2>&1 | tail -3 | tee /dev/stderr | grep -q " 0 error") ;;
  snap)     ats=$(python3 -c "import json;t=json.load(open('$EP/timing.json'));print(','.join(f'{min(b-0.3,a+max(1.2,(b-a)*0.6)):.1f}' for a,b in t['scenes']))")
            (cd "$EP/hf" && rm -rf snapshots && hyperframes snapshot --at "$ats" --no-end --describe false | tail -2) ;;
  render)   (cd "$EP/hf" && hyperframes render -o renders/video.mp4 -f 30 -q looks -w 2 --quiet) ;;
  score)    python "$P/score.py" "$EP" --track "$1" ;;
  mix)      mkdir -p "$EP/final"
            python "$P/mix.py" "$EP" "$EP/hf/renders/video.mp4" "$EP/final/$slug.mp4"
            # cover: the title-card frame
            t=$(python3 -c "import json;t=json.load(open('$EP/timing.json'));a,b=t['scenes'][1];print(round(a+min(2.2,(b-a)*0.8),2))")
            ffmpeg -v error -y -ss "$t" -i "$EP/final/$slug.mp4" -frames:v 1 -q:v 2 "$EP/final/$slug-cover.jpg" ;;
  qa)       f="$EP/final/$slug.mp4"
            ffprobe -v error -show_entries format=duration,size:stream=codec_name,width,height,r_frame_rate -of compact "$f"
            ffmpeg -hide_banner -i "$f" -af ebur128 -f null - 2>&1 | grep -E "^\s+I:" | tail -1
            echo "black segments:"; ffmpeg -hide_banner -i "$f" -vf blackdetect=d=0.4:pix_th=0.06 -an -f null - 2>&1 | grep -c black_start || true
            python "$P/asr_check.py" small "$f" 2>/dev/null | cut -c1-400 ;;
  all)      "$0" captions "$EP"; "$0" build "$EP"; "$0" render "$EP"; "$0" score "$EP" "$1"; "$0" mix "$EP"; "$0" qa "$EP" ;;
  *) echo "unknown step $step"; exit 1 ;;
esac
