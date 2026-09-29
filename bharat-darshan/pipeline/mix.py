#!/usr/bin/env python3
"""Mix narration + score + SFX and mux onto the silent HyperFrames render.

usage: mix.py EP_DIR VIDEO_IN OUT_MP4
voice lines placed at timing.json line starts; music ducked ~9 dB under voice (smoothed envelope);
final loudness -14 LUFS / -1 dBTP (Instagram / YouTube / Facebook friendly).
"""
import json, os, subprocess, sys
import numpy as np, soundfile as sf
from scipy.signal import resample_poly

SR = 48000


def load(path):
    x, sr = sf.read(path, always_2d=True)
    x = x.mean(1)
    if sr != SR:
        from math import gcd
        g = gcd(SR, sr); x = resample_poly(x, SR // g, sr // g)
    return x


def main():
    ep_dir, vin, out = sys.argv[1:4]
    tm = json.load(open(os.path.join(ep_dir, "timing.json")))
    n = int((tm["total"] + 0.5) * SR)
    voice = np.zeros(n)
    for lid, t in tm["lines"].items():
        x = load(os.path.join(ep_dir, "voice", lid + ".wav"))
        x = x / (np.abs(x).max() + 1e-9) * 0.8
        i = int(t * SR); j = min(n, i + len(x)); voice[i:j] += x[: j - i]
    music, _ = sf.read(os.path.join(ep_dir, "audio", "music.wav"), always_2d=True)
    sfx, _ = sf.read(os.path.join(ep_dir, "audio", "sfx.wav"), always_2d=True)
    music = np.pad(music, ((0, max(0, n - len(music))), (0, 0)))[:n]
    sfx = np.pad(sfx, ((0, max(0, n - len(sfx))), (0, 0)))[:n]
    # ducking envelope
    win = int(0.05 * SR)
    env = np.sqrt(np.convolve(voice ** 2, np.ones(win) / win, "same"))
    act = (env > 0.02).astype(float)
    k = int(0.25 * SR)
    act = np.convolve(act, np.ones(k) / k, "same").clip(0, 1)
    gain = 10 ** ((-9 * act) / 20)
    mix = np.stack([voice, voice], 1) * 1.0 + music * 0.30 * gain[:, None] + sfx * 0.42
    mix /= max(1.0, np.abs(mix).max() / 0.95)
    tmp = os.path.join(ep_dir, "audio", "mix_raw.wav")
    sf.write(tmp, mix, SR)
    # size budget ~18.5 MB: jsDelivr serves GitHub files only up to 20 MB (as video/mp4, which Instagram and
    # Facebook fetch reliably); chat delivery limit is 30 MiB. Two-pass x264 keeps quality at this size.
    dur = tm["total"]
    vk = int(min(6000, max(1200, (18.5 * 8 * 1000 * 1000 / dur) / 1000 - 200)))
    aac = os.path.join(ep_dir, "audio", "mix.m4a")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", tmp, "-af", "loudnorm=I=-14:TP=-1.5:LRA=11",
                    "-c:a", "aac", "-b:a", "160k", "-ar", "48000", aac], check=True)
    venc = ["-c:v", "libx264", "-preset", "slow", "-b:v", f"{vk}k", "-maxrate", f"{int(vk*1.4)}k",
            "-bufsize", f"{int(vk*2.8)}k", "-profile:v", "high", "-level:v", "4.1", "-pix_fmt", "yuv420p", "-r", "30", "-g", "60"]
    plog = os.path.join(ep_dir, "audio", "x264pass")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", vin] + venc + ["-pass", "1", "-passlogfile", plog, "-an",
                    "-f", "null", "/dev/null"], check=True)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", vin, "-i", aac, "-map", "0:v", "-map", "1:a"] + venc +
                   ["-pass", "2", "-passlogfile", plog, "-c:a", "copy", "-shortest", "-movflags", "+faststart", out],
                   check=True)
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", out, "-af", "ebur128", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    print("mixed", out, [l.strip() for l in r.splitlines() if "I:" in l][-1:])


if __name__ == "__main__":
    main()
