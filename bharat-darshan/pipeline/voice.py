#!/usr/bin/env python3
"""Generate per-line Hindi narration with Chatterbox Multilingual (MIT) + quality gate.

usage: voice.py EP_DIR REF_WAV [--asr medium]
Reads EP_DIR/episode.json lines[{id,tts,exag}], writes EP_DIR/voice/<id>.wav (trimmed, 24k mono)
and EP_DIR/voice/voice_meta.json [{id, dur, cer, asr}].
Each line is transcribed back with faster-whisper; if the character error rate is high,
the line is regenerated (up to 3 tries) and the best take is kept.
"""
import json, os, re, subprocess, sys, unicodedata

import torch, torchaudio as ta
from chatterbox.mtl_tts import ChatterboxMultilingualTTS
from faster_whisper import WhisperModel


def norm(s):
    s = unicodedata.normalize("NFC", s)
    s = re.sub(r"[़]", "", s)          # nukta: ज़ vs ज
    s = re.sub(r"[^ऀ-ॿ0-9a-zA-Z]", "", s).lower()  # Devanagari + digits/latin
    return s


def cer(a, b):
    a, b = norm(a), norm(b)
    if not a:
        return 1.0
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1] / len(a)


def trim(src, dst):
    # trim leading/trailing silence, light compression, 24k mono
    af = ("silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.05,"
          "areverse,silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.08,areverse,"
          "acompressor=threshold=-20dB:ratio=3:attack=5:release=80,aresample=24000")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-af", af, "-ac", "1", dst], check=True)
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", dst],
                         capture_output=True, text=True).stdout
    return float(out.strip())


def main():
    ep_dir, ref = sys.argv[1], sys.argv[2]
    asr_name = sys.argv[sys.argv.index("--asr") + 1] if "--asr" in sys.argv else "medium"
    only = sys.argv[sys.argv.index("--only") + 1].split(",") if "--only" in sys.argv else None
    ep = json.load(open(os.path.join(ep_dir, "episode.json")))
    vdir = os.path.join(ep_dir, "voice"); os.makedirs(vdir, exist_ok=True)
    meta_path = os.path.join(vdir, "voice_meta.json")
    meta = {m["id"]: m for m in json.load(open(meta_path))} if os.path.exists(meta_path) else {}
    import gc
    torch.manual_seed(7)
    todo = [ln for ln in ep["lines"] if (only and ln["id"] in only) or
            (not only and not (ln["id"] in meta and os.path.exists(os.path.join(vdir, ln["id"] + ".wav"))))]
    takes = {ln["id"]: [] for ln in todo}   # id -> [(cer, raw, text)]
    for rnd in range(3):
        if not todo:
            break
        # phase A: synthesize (TTS model only in RAM)
        tts = ChatterboxMultilingualTTS.from_pretrained(device="cpu")
        for ln in todo:
            w = tts.generate(ln["tts"], language_id="hi", audio_prompt_path=ref,
                             exaggeration=ln.get("exag", 0.6), cfg_weight=0.5, temperature=0.8)
            raw = os.path.join(vdir, f"{ln['id']}_raw{rnd}.wav")
            ta.save(raw, w, tts.sr)
            print(f"gen {ln['id']} round{rnd} {w.shape[-1]/tts.sr:.1f}s", flush=True)
        del tts; gc.collect()
        # phase B: transcribe back (ASR model only in RAM)
        asr = WhisperModel(asr_name, device="cpu", compute_type="int8")
        nxt = []
        for ln in todo:
            raw = os.path.join(vdir, f"{ln['id']}_raw{rnd}.wav")
            segs, _ = asr.transcribe(raw, language="hi", beam_size=5)
            text = " ".join(x.text.strip() for x in segs)
            c = min(cer(ln["tts"], text), cer(ln.get("caption", ln["tts"]), text))
            takes[ln["id"]].append((c, raw, text))
            print(f"{ln['id']} round{rnd} cer={c:.2f} | {text}", flush=True)
            if c > 0.22:
                nxt.append(ln)
        del asr; gc.collect()
        todo = nxt
    for lid, tk in takes.items():
        c, raw, text = min(tk)
        dur = trim(raw, os.path.join(vdir, lid + ".wav"))
        meta[lid] = {"id": lid, "dur": round(dur, 3), "cer": round(c, 3), "asr": text}
    order = [ln["id"] for ln in ep["lines"]]
    json.dump(sorted(meta.values(), key=lambda m: order.index(m["id"])), open(meta_path, "w"), ensure_ascii=False, indent=1)
    for f in os.listdir(vdir):
        if "_raw" in f:
            os.remove(os.path.join(vdir, f))
    print("DONE", sum(m["dur"] for m in meta.values()))


if __name__ == "__main__":
    main()
