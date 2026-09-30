# भारत दर्शन — R&D log

## 2026-09-29 — studio built (pilot: Konark)
- Voice: **Chatterbox Multilingual (MIT)** chosen over Kokoro hm_omega — far more natural Hindi prosody, zero-shot clone from a 10 s reference. ~6–7× slower than real time on 2 CPUs (≈15 min per episode incl. Whisper QA). OOM if Chatterbox + Whisper-medium are loaded together → voice.py alternates them.
- Checked and not used: IndicF5 and Indic Parler-TTS (gated on HuggingFace — need Sushil's HF account), XTTS-v2 (non-commercial licence), MusicGen weights (CC-BY-NC — not for a business page), Piper hi voices (non-commercial).
- Music: Kevin MacLeod / incompetech library (CC BY 4.0, credit line in caption) + synthesised SFX. FreePD has shut down. Pixabay/Pexels blocked from the workspace.
- Photos: Wikimedia Commons API with a licence filter; use curl + descriptive UA (urllib gets HTTP 429). Standard thumb widths only (1920/3840).
- Render: 72 s at 1080×1920/30 fps ≈ 8 min (screenshot capture, software GL); encode to ~55 MB with CRF 22 / 6 Mbps cap.
- Layout lessons: global vignette above scenes dimmed gold numbers → vignette now lives inside each scene under the text; `filter: drop-shadow` must sit on the parent of `background-clip:text` elements; no letterSpacing tweens (lint error); captions off during hook/title/end cards (on-screen text already says it).
- Open: talking avatar of Sushil — real lip-sync models (SadTalker, LivePortrait, Wav2Lip) are GPU-class; on 2 CPUs only a short stylised presenter card is practical. HeyGen avatars via `hyperframes auth login` are the quality path (paid).

## 2026-09-30 — ep 2 (Rani ki Vav)
- **Pipeline changes (tested in today's render):** `build.py` — the currency-note prop is now generic: `prop_value` ("₹100"), `prop_words` ("सौ रुपये"), `prop_bg` (CSS gradient; lavender for the ₹100 note), settable per scene or at episode level; defaults stay ₹10 for Konark. `commons.py` — credits.json is now written after every download (a timeout used to lose all credits), a failed/429 search skips that query instead of crashing the run, backoff 12 s steps.
- **Wikimedia rate-limits hard** (HTTP 429 on upload.wikimedia.org originals, ~1 file/min at times). Only 7 of ~20 candidate photos downloaded in 15 min. Next: request `iiurlwidth=1920` for landscape shots that don't need 3840, and start the photo download *first* (right after picking the topic) so it overlaps setup.
- **Custom signature animation idea that worked:** SVG cross-section (7 stepped levels + well shaft, gold stroke-draw) with a patterned "silt" rect rising inside a clipPath — pillar stubs + well mouth stay above the ground line. Reusable for any "buried / flooded / rediscovered" story.
- **TTS research:** VoxCPM2 (openbmb, Apache-2.0, 30 languages incl. Hindi, voice clone) — best-rated open local Hindi voice in Sanyam35/hindi-voice-bench (naturalness 4.0/5), but 2B params, CUDA-first, ~8× slower than real time even on a 16 GB Mac → not practical on 2 vCPU / 7.8 GB. Lead to test on Sunday: `onnx-community/chatterbox-multilingual-ONNX` (same MIT Chatterbox model as ONNX — may cut voice time on CPU). Sarvam Bulbul v3 is API-only (paid), strong on numbers/dates.
- Voice today: 14 lines, 1 regeneration (l05 CER 0.27 → 0.22), total 67.95 s narration; whole voice step ≈ 17 min.
