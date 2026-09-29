# भारत दर्शन — R&D log

## 2026-09-29 — studio built (pilot: Konark)
- Voice: **Chatterbox Multilingual (MIT)** chosen over Kokoro hm_omega — far more natural Hindi prosody, zero-shot clone from a 10 s reference. ~6–7× slower than real time on 2 CPUs (≈15 min per episode incl. Whisper QA). OOM if Chatterbox + Whisper-medium are loaded together → voice.py alternates them.
- Checked and not used: IndicF5 and Indic Parler-TTS (gated on HuggingFace — need Sushil's HF account), XTTS-v2 (non-commercial licence), MusicGen weights (CC-BY-NC — not for a business page), Piper hi voices (non-commercial).
- Music: Kevin MacLeod / incompetech library (CC BY 4.0, credit line in caption) + synthesised SFX. FreePD has shut down. Pixabay/Pexels blocked from the workspace.
- Photos: Wikimedia Commons API with a licence filter; use curl + descriptive UA (urllib gets HTTP 429). Standard thumb widths only (1920/3840).
- Render: 72 s at 1080×1920/30 fps ≈ 8 min (screenshot capture, software GL); encode to ~55 MB with CRF 22 / 6 Mbps cap.
- Layout lessons: global vignette above scenes dimmed gold numbers → vignette now lives inside each scene under the text; `filter: drop-shadow` must sit on the parent of `background-clip:text` elements; no letterSpacing tweens (lint error); captions off during hook/title/end cards (on-screen text already says it).
- Open: talking avatar of Sushil — real lip-sync models (SadTalker, LivePortrait, Wav2Lip) are GPU-class; on 2 CPUs only a short stylised presenter card is practical. HeyGen avatars via `hyperframes auth login` are the quality path (paid).
