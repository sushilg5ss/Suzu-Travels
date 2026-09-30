#!/bin/bash
# usage: mix.sh REEL_DIR  -> REEL_DIR/final/<slug>.mp4 + cover.jpg  (music bed, fades, -14 LUFS, ~18 MB)
set -e
R=$(cd "$1" && pwd); slug=$(basename "$R")
M=$(python3 -c "import json;print(json.load(open('$R/spec.json'))['music'])")
D=$(python3 -c "import json;print(json.load(open('$R/spec.json'))['duration'])")
mkdir -p "$R/final"; cd "$R/final"
ffmpeg -v error -y -i "$HOME/bd/pipeline/assets/music/$M" -t $D -af "afade=t=in:d=0.4,afade=t=out:st=$(python3 -c "print($D-2.5)"):d=2.5,loudnorm=I=-14:TP=-1.5:LRA=11" -ar 48000 music.wav
kbps=$(python3 -c "print(int(18.2*8192/$D-160))")
ffmpeg -v error -y -i ../hf/renders/video.mp4 -c:v libx264 -preset slow -b:v ${kbps}k -pass 1 -passlogfile p -an -f mp4 /dev/null
ffmpeg -v error -y -i ../hf/renders/video.mp4 -i music.wav -c:v libx264 -preset slow -b:v ${kbps}k -pass 2 -passlogfile p -pix_fmt yuv420p -c:a aac -b:a 160k -shortest -movflags +faststart "$slug.mp4"
ffmpeg -v error -y -ss 1.8 -i "$slug.mp4" -frames:v 1 -q:v 2 cover.jpg
rm -f p-0.log* music.wav
ffprobe -v error -show_entries format=duration,size -of compact "$slug.mp4"
ffmpeg -hide_banner -i "$slug.mp4" -af ebur128 -f null - 2>&1 | grep -E "^\s+I:" | tail -1
