#!/usr/bin/env bash
# Suzu International Motion Reels — bootstrap a fresh cloud container (≈3–5 min). No TTS, no torch.
# Result: ~/mr = builder (mg.py, mix.sh, fonts, data/india.json, assets/), ~/bd/pipeline/assets/music = CC BY music.
set -euo pipefail
ST="${ST:-$HOME/st}"                      # clone of sushilg5ss/Suzu-Travels @ bharat-darshan
M="$ST/bharat-darshan/pipeline/motion"; P="$ST/bharat-darshan/pipeline"
HF_VER="${HF_VER:-0.8.91}"
npm i -g "hyperframes@$HF_VER" >/dev/null 2>&1 || npm i -g hyperframes >/dev/null
hyperframes browser ensure >/dev/null 2>&1 || npx -y "hyperframes@$HF_VER" browser ensure
python3 -c "import PIL" 2>/dev/null || pip install -q --break-system-packages pillow
mkdir -p ~/bd ~/mr/assets ~/mr/raw ~/mr/reels
[ -d ~/bd/pipeline ] || cp -r "$P" ~/bd/pipeline
cp "$M/mg.py" "$M/mix.sh" ~/mr/ && chmod +x ~/mr/mix.sh
cp -r "$M/fonts" "$M/data" ~/mr/
cp -r "$P/assets/gsap.min.js" "$P/assets/suzu-logo.png" "$P/assets/grain.png" "$P/assets/hf-template" ~/mr/assets/
sed 's/"iiurlwidth": 3840/"iiurlwidth": 1920/' "$P/commons.py" > ~/mr/commons1920.py
A=~/bd/pipeline/assets/music; mkdir -p "$A"
for f in Dhaka Jalandhar Vadodora Naraina Tabuk "Eastern Thought" "Our Story Begins" "Long Road Ahead" "Impact Lento" Magistar "Tempting Secrets" "Noble Race"; do
  [ -s "$A/$f.mp3" ] || curl -s -m 120 -o "$A/$f.mp3" "https://incompetech.com/music/royalty-free/mp3-royaltyfree/${f// /%20}.mp3"
done
hyperframes doctor 2>&1 | grep -E "Chrome|FFmpeg" || true
echo "MOTION SETUP OK"
