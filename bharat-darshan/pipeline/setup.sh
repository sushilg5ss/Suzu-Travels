#!/usr/bin/env bash
# Bharat Darshan studio — one-shot bootstrap for a fresh cloud container (≈6–10 min).
# Installs: HyperFrames CLI + render browser + skills, Python venv with Chatterbox Multilingual TTS (MIT),
# faster-whisper (captions / QA), Kokoro (fallback voice), scipy/soundfile/Pillow.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
VENV="${VENV:-$HOME/bd-venv}"
HF_VER="${HF_VER:-0.8.91}"

echo "== HyperFrames CLI $HF_VER"
npm i -g "hyperframes@$HF_VER" >/dev/null 2>&1 || npm i -g hyperframes >/dev/null
hyperframes browser ensure >/dev/null 2>&1 || npx -y "hyperframes@$HF_VER" browser ensure

echo "== HyperFrames skills (for reference while authoring custom scenes)"
if [ ! -d "$HOME/.claude/skills/hyperframes-core" ]; then
  tmp=$(mktemp -d); git clone -q --depth 1 https://github.com/heygen-com/hyperframes.git "$tmp/hf" \
    && mkdir -p "$HOME/.claude/skills" && cp -r "$tmp/hf/skills/"* "$HOME/.claude/skills/" || echo "skills clone skipped"
fi

echo "== Python venv at $VENV"
python3 -m venv "$VENV"
# shellcheck disable=SC1091
source "$VENV/bin/activate"
pip install -q --upgrade pip
pip install -q torch==2.6.0 torchaudio==2.6.0 --index-url https://download.pytorch.org/whl/cpu
pip install -q chatterbox-tts faster-whisper soundfile scipy numpy pillow kokoro-onnx "misaki[hi]"
python - <<'EOF'
# warm the model caches so the first episode doesn't pay for downloads mid-run
from faster_whisper import WhisperModel
WhisperModel("small", device="cpu", compute_type="int8"); WhisperModel("medium", device="cpu", compute_type="int8")
from chatterbox.mtl_tts import ChatterboxMultilingualTTS
ChatterboxMultilingualTTS.from_pretrained(device="cpu")
print("models cached")
EOF
echo "== binary assets (fonts, gsap, grain, logo, music, narrator reference)"
A="$HERE/assets"; mkdir -p "$A/fonts" "$A/music" "$A/hf-template"
if [ ! -f "$A/gsap.min.js" ] || [ ! -f "$A/fonts/tiro-devanagari-hindi-devanagari-400-normal.woff2" ]; then
  tmp=$(mktemp -d); (cd "$tmp" && npm init -y >/dev/null && npm i -s @fontsource/baloo-2 @fontsource/tiro-devanagari-hindi @fontsource/cinzel @fontsource/sora gsap@3.14.2 >/dev/null 2>&1)
  F="$tmp/node_modules/@fontsource"; cp "$tmp/node_modules/gsap/dist/gsap.min.js" "$A/"
  cp $F/tiro-devanagari-hindi/files/tiro-devanagari-hindi-{devanagari,latin}-400-normal.woff2 \
     $F/baloo-2/files/baloo-2-{devanagari,latin}-{600,800}-normal.woff2 \
     $F/cinzel/files/cinzel-latin-{700,900}-normal.woff2 $F/sora/files/sora-latin-{600,700}-normal.woff2 "$A/fonts/"
fi
[ -f "$A/suzu-logo.png" ] || python - <<PY
import urllib.request, io
from PIL import Image
d = urllib.request.urlopen(urllib.request.Request("https://suzutravels.com/wp-content/uploads/2026/05/suzutravels-logo.webp", headers={"User-Agent":"Mozilla/5.0"})).read()
Image.open(io.BytesIO(d)).save("$A/suzu-logo.png")
PY
[ -f "$A/grain.png" ] || python -c "import numpy as np;from PIL import Image;Image.fromarray(np.random.default_rng(3).normal(128,48,(256,256)).clip(0,255).astype('uint8'),'L').save('$A/grain.png')"
[ -f "$A/hf-template/hyperframes.json" ] || { tmp=$(mktemp -d); (cd "$tmp" && HYPERFRAMES_SKIP_SKILLS=1 hyperframes init t --example blank --non-interactive >/dev/null 2>&1); cp "$tmp/t/hyperframes.json" "$tmp/t/package.json" "$A/hf-template/"; }
for f in Dhaka Jalandhar Vadodora Naraina Tabuk "Eastern Thought" "Our Story Begins" "Long Road Ahead" "Impact Lento" Magistar "Tempting Secrets" "Noble Race"; do
  [ -s "$A/music/$f.mp3" ] || curl -s -m 120 -o "$A/music/$f.mp3" "https://incompetech.com/music/royalty-free/mp3-royaltyfree/${f// /%20}.mp3"
done
# narrator reference: Sushil's own voice sample if present (assets/narrator_ref.wav), else a Kokoro hm_omega seed voice
[ -f "$A/narrator_ref.wav" ] || hyperframes tts "कोणार्क सूर्य मंदिर, ओडिशा। करीब बारह सौ पचास ईस्वी में, राजा नरसिंहदेव प्रथम ने, सूर्य देव के लिए, पत्थर का एक विशाल रथ बनवाया।" -v hm_omega -l hi -s 1.0 -o "$A/narrator_ref.wav" < /dev/null
hyperframes doctor 2>&1 | grep -E "Version|Chrome|FFmpeg" || true
echo "SETUP OK  (activate with: source $VENV/bin/activate)"
