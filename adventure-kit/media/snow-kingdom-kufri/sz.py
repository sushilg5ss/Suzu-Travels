"""Tiny deterministic motion-graphics renderer (PIL frames -> ffmpeg). Suzu brand."""
import math, subprocess, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

NAVY = (11, 31, 51); GOLD = (212, 162, 76); GOLD_L = (243, 217, 143); WHITE = (255, 255, 255)
FDIR = '/home/claude/work/fonts/package/files/'
_fc = {}
def font(w, size):
    k = (w, size)
    if k not in _fc:
        _fc[k] = ImageFont.truetype(FDIR + 'plus-jakarta-sans-latin-%s-normal.woff' % w, size)
    return _fc[k]

def clamp(x, a=0.0, b=1.0): return max(a, min(b, x))
def prog(t, t0, d): return clamp((t - t0) / d) if d > 0 else (1.0 if t >= t0 else 0.0)
def ease_out(p): return 1 - (1 - p) ** 3
def ease_in_out(p): return 4 * p ** 3 if p < .5 else 1 - (-2 * p + 2) ** 3 / 2
def ease_back(p, s=1.6):
    c3 = s + 1; return 1 + c3 * (p - 1) ** 3 + s * (p - 1) ** 2

class Photo:
    """Pre-scaled cover image; frame(t) returns W x H crop with Ken Burns zoom/pan."""
    def __init__(self, path, W, H, focus=(0.5, 0.5), zmax=1.14):
        im = Image.open(path).convert('RGB')
        s = max(W / im.width, H / im.height) * zmax
        self.im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
        self.W, self.H, self.focus, self.zmax = W, H, focus, zmax
    def frame(self, z, dx=0.0):
        # z in [1, zmax]: 1 = widest crop
        cw, ch = self.W * self.zmax / z, self.H * self.zmax / z
        fx, fy = self.focus
        cx = clamp(fx * self.im.width + dx * self.im.width, cw / 2, self.im.width - cw / 2)
        cy = clamp(fy * self.im.height, ch / 2, self.im.height - ch / 2)
        cw, ch = min(cw, self.im.width), min(ch, self.im.height)
        x0 = clamp(cx - cw / 2, 0, self.im.width - cw); y0 = clamp(cy - ch / 2, 0, self.im.height - ch)
        box = (x0, y0, x0 + cw, y0 + ch)
        return self.im.resize((self.W, self.H), Image.BILINEAR, box=box)

def grad_h(W, H, stops):
    """Horizontal RGBA gradient; stops = [(x_frac, alpha)] navy."""
    row = Image.new('RGBA', (W, 1))
    px = row.load()
    for x in range(W):
        f = x / (W - 1)
        for (a0, v0), (a1, v1) in zip(stops, stops[1:]):
            if a0 <= f <= a1:
                v = v0 + (v1 - v0) * ((f - a0) / (a1 - a0) if a1 > a0 else 0); break
        else:
            v = stops[-1][1]
        px[x, 0] = NAVY + (int(255 * v),)
    return row.resize((W, H))

def grad_v(W, H, stops):
    col = Image.new('RGBA', (1, H)); px = col.load()
    for y in range(H):
        f = y / (H - 1)
        for (a0, v0), (a1, v1) in zip(stops, stops[1:]):
            if a0 <= f <= a1:
                v = v0 + (v1 - v0) * ((f - a0) / (a1 - a0) if a1 > a0 else 0); break
        else:
            v = stops[-1][1]
        px[0, y] = NAVY + (int(255 * v),)
    return col.resize((W, H))

def text(layer, xy, s, fnt, fill, alpha=1.0, dy=0, anchor='la', shadow=False):
    if alpha <= 0: return
    a = int(255 * clamp(alpha))
    d = ImageDraw.Draw(layer)
    x, y = xy
    if shadow:
        sh = Image.new('RGBA', layer.size, (0, 0, 0, 0))
        ImageDraw.Draw(sh).text((x, y + dy + 3), s, font=fnt, fill=(0, 0, 0, int(a * .55)), anchor=anchor)
        sh = sh.filter(ImageFilter.GaussianBlur(8))
        layer.alpha_composite(sh)
    d.text((x, y + dy), s, font=fnt, fill=fill + (a,), anchor=anchor)

def pill(layer, xy, s, fnt, bg, fg, alpha=1.0, pad=(30, 16), scale=1.0):
    if alpha <= 0: return
    a = int(255 * clamp(alpha)); d = ImageDraw.Draw(layer)
    x, y = xy
    l, t, r, b = d.textbbox((0, 0), s, font=fnt)
    w, h = (r - l) + 2 * pad[0], (b - t) + 2 * pad[1]
    cx, cy = x + w / 2, y + h / 2
    w2, h2 = w * scale, h * scale
    d.rounded_rectangle((cx - w2 / 2, cy - h2 / 2, cx + w2 / 2, cy + h2 / 2), radius=h2 / 2, fill=bg + (a,))
    d.text((cx, cy), s, font=fnt, fill=fg + (a,), anchor='mm')
    return w, h

def polyline_partial(pts, p):
    """Return points of polyline drawn up to fraction p of its length."""
    segs = [math.dist(a, b) for a, b in zip(pts, pts[1:])]
    L = sum(segs) * clamp(p); out = [pts[0]]
    for (a, b), s in zip(zip(pts, pts[1:]), segs):
        if L >= s: out.append(b); L -= s
        else:
            if L > 0: out.append((a[0] + (b[0] - a[0]) * L / s, a[1] + (b[1] - a[1]) * L / s))
            break
    return out

def smooth(pts, n=12):
    """Catmull-Rom smoothing."""
    P = [pts[0]] + pts + [pts[-1]]; out = []
    for i in range(1, len(P) - 2):
        p0, p1, p2, p3 = P[i - 1], P[i], P[i + 1], P[i + 2]
        for k in range(n):
            t = k / n; t2, t3 = t * t, t * t * t
            out.append(tuple(0.5 * ((2 * p1[j]) + (-p0[j] + p2[j]) * t + (2 * p0[j] - 5 * p1[j] + 4 * p2[j] - p3[j]) * t2 + (-p0[j] + 3 * p1[j] - 3 * p2[j] + p3[j]) * t3) for j in (0, 1)))
    out.append(pts[-1]); return out

class Snow:
    def __init__(self, W, H, n, seed=7, rmin=2, rmax=6):
        r = random.Random(seed)
        self.W, self.H = W, H
        self.f = [(r.random() * W, r.random() * H, r.uniform(rmin, rmax), r.uniform(40, 110), r.uniform(0, 6.28), r.uniform(.35, .9)) for _ in range(n)]
    def draw(self, layer, t, alpha=1.0, period=None):
        d = ImageDraw.Draw(layer)
        for x0, y0, rad, sp, ph, op in self.f:
            y = (y0 + sp * t) % (self.H + 20) - 10
            if period:  # perfectly periodic: speed snapped so flake returns after `period` seconds
                k = max(1, round(sp * period / (self.H + 20))); v = k * (self.H + 20) / period
                y = (y0 + v * t) % (self.H + 20) - 10
                x = x0 + 14 * math.sin(2 * math.pi * t / period * max(1, round(period / 4)) + ph)
            else:
                x = x0 + 14 * math.sin(t * 1.3 + ph)
            a = int(255 * op * alpha)
            d.ellipse((x - rad, y - rad, x + rad, y + rad), fill=(255, 255, 255, a))

class Writer:
    def __init__(self, path, W, H, fps=30):
        self.p = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(fps), '-i', '-',
                                   '-c:v', 'libx264', '-preset', 'medium', '-crf', '16', '-pix_fmt', 'yuv420p', path], stdin=subprocess.PIPE)
    def add(self, im): self.p.stdin.write(im.convert('RGB').tobytes())
    def close(self): self.p.stdin.close(); self.p.wait()
