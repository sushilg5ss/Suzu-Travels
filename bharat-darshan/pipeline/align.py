#!/usr/bin/env python3
"""Word timings for captions. Never displays Whisper's spelling: script words are mapped onto
Whisper's time spans by cumulative character fraction.

usage: align.py EP_DIR [--asr small]
writes EP_DIR/voice/captions.json {line_id: [{"w": word, "s": sec, "e": sec}, ...]} (line-relative)
"""
import bisect, json, os, re, sys
from faster_whisper import WhisperModel


def main():
    ep_dir = sys.argv[1]
    asr_name = sys.argv[sys.argv.index("--asr") + 1] if "--asr" in sys.argv else "small"
    ep = json.load(open(os.path.join(ep_dir, "episode.json")))
    meta = {m["id"]: m for m in json.load(open(os.path.join(ep_dir, "voice", "voice_meta.json")))}
    asr = WhisperModel(asr_name, device="cpu", compute_type="int8")
    out = {}
    for ln in ep["lines"]:
        wav = os.path.join(ep_dir, "voice", ln["id"] + ".wav")
        dur = meta[ln["id"]]["dur"]
        segs, _ = asr.transcribe(wav, language="hi", word_timestamps=True, beam_size=5)
        ww = [(w.start, w.end, len(w.word.strip()) or 1) for s in segs for w in (s.words or [])]
        if not ww:
            ww = [(0.0, dur, 1)]
        # cumulative char -> time mapping (piecewise linear inside each whisper word)
        xs, ts = [0.0], [ww[0][0]]
        tot = 0
        for s, e, L in ww:
            if tot > 0:  # jump across the gap between words
                xs.append(tot + 1e-6); ts.append(s)
            tot += L
            xs.append(tot); ts.append(e)
        words = [w for w in re.split(r"\s+", ln.get("caption", ln["tts"]).replace("...", "… ").strip()) if w]
        lens = [len(re.sub(r"[^\wऀ-ॿ]", "", w)) or 1 for w in words]
        n = sum(lens)

        def at(frac):
            x = frac * tot
            i = min(max(bisect.bisect_left(xs, x), 1), len(xs) - 1)
            x0, x1, t0, t1 = xs[i - 1], xs[i], ts[i - 1], ts[i]
            return t0 if x1 == x0 else t0 + (t1 - t0) * (x - x0) / (x1 - x0)

        c, res = 0, []
        for w, L in zip(words, lens):
            s, e = at(c / n), at((c + L) / n)
            c += L
            res.append({"w": w, "s": round(max(0, s), 3), "e": round(min(dur, max(e, s + 0.08)), 3)})
        out[ln["id"]] = res
        print(ln["id"], " ".join(f"{r['w']}@{r['s']}" for r in res))
    json.dump(out, open(os.path.join(ep_dir, "voice", "captions.json"), "w"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
