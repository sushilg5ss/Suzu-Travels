#!/usr/bin/env python3
"""Procedural cinematic Indian score + SFX (fully owned audio, no licence risk).

usage: score.py EP_DIR [--sa 138.59]
reads EP_DIR/timing.json (total, scenes, sfx cues); writes EP_DIR/audio/music.wav and sfx.wav (48k stereo)
Layers: tanpura drone (Karplus-Strong + jawari buzz), string pad (detuned saws, low-passed swell),
taiko/dhol-like hits on a 90 bpm grid that grow in intensity, risers, whooshes, stamp hits, clock ticks.
"""
import json, os, sys
import numpy as np
from scipy.signal import butter, sosfilt, fftconvolve

SR = 48000
rng = np.random.default_rng(5)


def lp(x, f, o=4):
    return sosfilt(butter(o, f, "low", fs=SR, output="sos"), x)


def hp(x, f, o=2):
    return sosfilt(butter(o, f, "high", fs=SR, output="sos"), x)


def bp(x, lo, hi, o=2):
    return sosfilt(butter(o, [lo, hi], "band", fs=SR, output="sos"), x)


def ks_pluck(freq, dur, bright=0.5):
    n = int(dur * SR); N = int(SR / freq)
    buf = rng.uniform(-1, 1, N) * bright + rng.uniform(-1, 1, N) * (1 - bright) * 0.3
    out = np.zeros(n)
    for i in range(n):
        out[i] = buf[i % N]
        buf[i % N] = 0.4985 * (buf[i % N] + buf[(i + 1) % N])
    out = np.tanh(out * 2.2)  # jawari-ish buzz
    return out * np.exp(-np.linspace(0, dur, n) * 0.9)


def ks_fast(freq, dur):
    # vectorised Karplus-Strong via repeated averaging per period (fast enough for drones)
    N = int(SR / freq); n = int(dur * SR)
    reps = n // N + 2
    buf = rng.uniform(-1, 1, N)
    rows = []
    for _ in range(reps):
        rows.append(buf)
        buf = 0.497 * (buf + np.roll(buf, -1))
    out = np.concatenate(rows)[:n]
    out = np.tanh(out * 2.5) * np.exp(-np.linspace(0, dur, n) * 0.7)
    return out


def saw(freq, t):
    return 2 * ((t * freq) % 1.0) - 1


def reverb(x, secs=2.8, mix=0.35):
    n = int(secs * SR)
    ir = rng.normal(0, 1, n) * np.exp(-np.linspace(0, 7, n))
    ir = lp(ir, 6000)
    ir /= np.sqrt((ir ** 2).sum())
    wet = fftconvolve(x, ir)[: len(x)]
    return (1 - mix) * x + mix * wet * 0.6


def taiko(dur=1.2, f0=95, f1=42, amp=1.0):
    n = int(dur * SR); t = np.arange(n) / SR
    f = f1 + (f0 - f1) * np.exp(-t * 18)
    ph = 2 * np.pi * np.cumsum(f) / SR
    body = np.sin(ph) * np.exp(-t * 4.5)
    click = lp(rng.normal(0, 1, n), 2500) * np.exp(-t * 60) * 0.5
    return amp * np.tanh(1.6 * (body + click))


def dha(dur=0.5, amp=0.6):
    # tabla-ish "dha": pitched membrane + slap
    n = int(dur * SR); t = np.arange(n) / SR
    tone = np.sin(2 * np.pi * 220 * t + 3 * np.exp(-t * 30)) * np.exp(-t * 9)
    bass = np.sin(2 * np.pi * (90 + 60 * np.exp(-t * 25)) * t) * np.exp(-t * 6)
    slap = bp(rng.normal(0, 1, n), 800, 5000) * np.exp(-t * 80)
    return amp * (0.5 * tone + 0.7 * bass + 0.4 * slap)


def whoosh(dur=0.7, amp=0.5):
    n = int(dur * SR); t = np.linspace(0, 1, n)
    noise = rng.normal(0, 1, n)
    env = np.sin(np.pi * t) ** 2
    out = np.zeros(n); seg = 2048
    for i in range(0, n, seg):
        c = 300 + 5000 * np.sin(np.pi * (i / n))
        out[i:i + seg] = bp(noise[i:i + seg], c * 0.6, min(c * 1.6, 20000))
    return amp * out * env


def riser(dur=2.0, amp=0.45):
    n = int(dur * SR); t = np.arange(n) / SR
    f = 200 * (2 ** (t / dur * 3))
    tone = np.sin(2 * np.pi * np.cumsum(f) / SR) * 0.3
    noise = hp(rng.normal(0, 1, n), 1500) * 0.4
    env = (t / dur) ** 2
    return amp * (tone + noise) * env


def tick(amp=0.25):
    n = int(0.05 * SR); t = np.arange(n) / SR
    return amp * bp(rng.normal(0, 1, n), 2500, 7000) * np.exp(-t * 180)


def place(buf, x, t, gain=1.0):
    i = int(t * SR)
    if i >= len(buf):
        return
    j = min(len(buf), i + len(x))
    buf[i:j] += x[: j - i] * gain


def main():
    ep_dir = sys.argv[1]
    sa = float(sys.argv[sys.argv.index("--sa") + 1]) if "--sa" in sys.argv else 138.59  # C#3
    tm = json.load(open(os.path.join(ep_dir, "timing.json")))
    T = tm["total"] + 0.5
    n = int(T * SR); t = np.arange(n) / SR
    music = np.zeros(n)
    track = sys.argv[sys.argv.index("--track") + 1] if "--track" in sys.argv else None
    if track:
        # licensed bed (e.g. Kevin MacLeod CC BY 4.0): start where the piece is established, loop if short
        import subprocess, tempfile
        tmpw = tempfile.mktemp(suffix=".wav")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", track, "-ac", "1", "-ar", str(SR), tmpw], check=True)
        import soundfile as _sf
        y, _ = _sf.read(tmpw)
        off = float(sys.argv[sys.argv.index("--offset") + 1]) if "--offset" in sys.argv else None
        if off is None:  # first moment the 4s RMS reaches 70% of the track's median loudness
            w = SR * 4
            r = np.array([np.sqrt((y[i:i + w] ** 2).mean()) for i in range(0, max(1, len(y) - w), SR)])
            med = np.median(r)
            off = float(np.argmax(r > 0.7 * med)) if len(r) else 0.0
        y = y[int(off * SR):]
        while len(y) < n:
            y = np.concatenate([y, y])
        bed = y[:n] / (np.abs(y[:n]).max() + 1e-9)
        bed *= np.clip(t / 1.2, 0, 1)
        music += 0.85 * bed
    # --- string pad: Sa + Pa + octave, detuned saws, slow swell; brighter in 2nd half
    pad = np.zeros(n)
    for f, a in ((sa / 2, 0.5), (sa * 1.5 / 2, 0.35), (sa, 0.3), (sa * 1.5, 0.12)):
        for d in (-0.35, 0.0, 0.4):
            pad += a * saw(f * (1 + d / 100), t)
    cut = 400 + 1400 * np.clip(t / T, 0, 1)
    pad_f = np.zeros(n); seg = SR // 2
    for i in range(0, n, seg):
        pad_f[i:i + seg] = lp(pad[i:i + seg], float(cut[i]))
    pad_env = np.clip(t / 4.0, 0, 1) * (0.8 + 0.2 * np.sin(2 * np.pi * t / 9))
    music += (0.03 if track else 0.10) * pad_f * pad_env
    # --- tanpura cycle: Pa Sa' Sa' Sa (each ~0.62s), continuous
    notes = [sa * 1.5 / 2, sa, sa, sa / 2]
    k, tt = 0, 0.2
    while tt < T and not track:
        place(music, ks_fast(notes[k % 4], 3.0), tt, 0.16)
        k += 1; tt += 0.62
    # --- percussion grid (90 bpm) from scene 2 onward, intensity grows
    beat = 60 / 90
    scenes = tm["scenes"]
    start_perc = scenes[1][0] if len(scenes) > 1 else 3
    end_card = scenes[-1][0]
    b = 0
    tt = start_perc
    while tt < end_card - 0.2:
        prog = (tt - start_perc) / max(1, end_card - start_perc)
        if track:
            break
        if b % 4 == 0:
            place(music, taiko(amp=0.55 + 0.35 * prog), tt)
        if b % 2 == 1 and prog > 0.15:
            place(music, dha(amp=0.35 + 0.3 * prog), tt)
        if prog > 0.45 and b % 4 == 3:
            place(music, dha(amp=0.3), tt + beat / 2)
        b += 1; tt += beat
    # end card: big hit + sustained chord
    place(music, taiko(dur=2.5, amp=1.0), end_card)
    music = reverb(music, 2.6, 0.12 if track else 0.3)
    fade = np.clip((T - t) / 2.0, 0, 1)
    music *= fade
    # --- SFX track
    sfx = np.zeros(n)
    place(sfx, taiko(dur=3.0, f0=70, f1=30, amp=1.0), 0.0)          # opening boom
    for c in tm["sfx"]:
        k = c["kind"]
        if k == "whoosh":
            place(sfx, whoosh(), max(0, c["t"] - 0.35))
        elif k == "hit":
            place(sfx, taiko(dur=1.0, amp=0.55), c["t"])
        elif k == "riser":
            place(sfx, riser(1.6), max(0, c["t"] - 1.2))
        elif k == "stamp":
            place(sfx, taiko(dur=1.4, f0=120, f1=50, amp=1.0), c["t"])
            place(sfx, lp(rng.normal(0, 1, int(0.2 * SR)), 3000) * np.exp(-np.arange(int(0.2 * SR)) / SR * 30) * 0.6, c["t"])
        elif k == "ticks":
            x = c["t"]
            while x < c["t"] + c.get("dur", 3):
                place(sfx, tick(), x); x += 0.5
    sfx = reverb(sfx, 1.8, 0.25)
    os.makedirs(os.path.join(ep_dir, "audio"), exist_ok=True)
    import soundfile as sf
    for name, x in (("music", music), ("sfx", sfx)):
        x = x / (np.abs(x).max() + 1e-9) * 0.9
        st = np.stack([x, np.roll(x, int(0.011 * SR)) * 0.97], 1) if name == "music" else np.stack([x, x], 1)
        sf.write(os.path.join(ep_dir, "audio", name + ".wav"), st, SR)
    print("score ok", T)


if __name__ == "__main__":
    main()
