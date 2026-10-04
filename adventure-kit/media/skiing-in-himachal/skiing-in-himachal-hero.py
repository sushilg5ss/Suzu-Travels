"""Skiing in Himachal hero loop: 1920x1080, 30 fps, 12 s, seamless (frame 0 == frame 360). Suzu brand.
Scenes: gentle slope with pines -> child skier -> skier on a gentle slope by snowy trees -> ski gear.
Signature: periodic falling snow + a gold ski-track line linking the three slopes
Solang ~2,500 m -> Kufri ~2,600 m -> Narkanda ~2,700 m with a rising altitude counter. Facts from the brief only."""
import sys
from PIL import Image, ImageDraw, ImageOps
from sz import *

W, H, FPS, DUR = 1920, 1080, 30, 12.0
PH = '/home/claude/work/ph/'
_m = ImageOps.mirror(Image.open(PH + 'px19967160.jpg').convert('RGB')); _m.save(PH + 'px19967160-m.jpg', quality=95)
A = Photo(PH + 'px21822635.jpg', W, H, focus=(0.64, 0.55), zmax=1.22)   # gentle slope, pines, blue sky
B = Photo(PH + 'px19822708.jpg', W, H, focus=(0.5, 0.42), zmax=1.10)    # child skier with helmet
C = Photo(PH + 'px19967160-m.jpg', W, H, focus=(0.5, 0.40), zmax=1.10)  # skier on gentle slope, snowy trees (mirrored)
D = Photo(PH + 'lib11626.jpg', W, H, focus=(0.42, 0.5), zmax=1.15)      # skis, boots, poles
SNOW = Snow(W, H, 120, seed=31, rmin=2, rmax=6)

shade = grad_h(W, H, [(0, 0), (0.30, 0.0), (0.56, 0.62), (1, 0.9)])
shade_v = grad_v(W, H, [(0, .32), (.22, 0), (.70, 0), (1, .6)])
X0, XMAX = 1030, 1850

def fit(s, w, size):
    while size > 40:
        f = font('800', size)
        if f.getlength(s) <= w: return f
        size -= 4
    return font('800', size)

SCN = [
    (0.0, 3.6, '01 · LEARN', 'First ski turns', 'Gentle slopes for beginners'),
    (3.2, 6.8, '02 · KIDS', 'Kids learn too', 'Govt. ABVIMAS course from age 10'),
    (6.4, 9.2, '03 · SEASON', 'January – March', 'Best in February'),
    (8.8, 11.3, '04 · GEAR', 'Skis, boots, poles', 'On hire at the slope'),
]

def a_img(t): return A.frame(1.12 + 0.10 * ease_in_out(prog(t, 0, 3.6)), dx=-0.03 * prog(t, 0, 3.6))
def b_img(t): return B.frame(1.09 - 0.08 * prog(t, 3.2, 3.6))
def c_img(t): return C.frame(1.0 + 0.08 * prog(t, 6.4, 2.8))
def d_img(t): return D.frame(1.04 + 0.09 * prog(t, 8.8, 3.2))

def photo_at(t):
    if t < 3.2: return a_img(t)
    if t < 3.6: return Image.blend(a_img(t), b_img(t), ease_in_out(prog(t, 3.2, .4)))
    if t < 6.4: return b_img(t)
    if t < 6.8: return Image.blend(b_img(t), c_img(t), ease_in_out(prog(t, 6.4, .4)))
    if t < 8.8: return c_img(t)
    if t < 9.2: return Image.blend(c_img(t), d_img(t), ease_in_out(prog(t, 8.8, .4)))
    if t < 11.3: return d_img(t)
    return Image.blend(d_img(t), a_img(0), ease_in_out(prog(t, 11.3, .7)))

RX = [X0, (X0 + XMAX - 20) / 2, XMAX - 20]; RALT = [2500, 2600, 2700]; RY = 930
RLAB = ['Solang', 'Kufri', 'Narkanda']

def track_pts():
    # a ski track: S-curves (snowplough turns) between the three slopes
    xa, xb = RX[0], RX[2]; pts = []
    for k in range(121):
        f = k / 120
        pts.append((xa + (xb - xa) * f, RY - 30 * f + 16 * math.sin(f * math.pi * 6)))
    return pts
TRACK = track_pts()

def render(t):
    im = photo_at(t).convert('RGBA')
    im.alpha_composite(shade); im.alpha_composite(shade_v)
    L = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    SNOW.draw(L, t, alpha=.85, period=DUR)
    text(L, (X0, 150), 'SKIING · HIMACHAL', font('800', 40), GOLD_L, 1.0, shadow=True)
    text(L, (X0, 206), 'Solang · Narkanda · Kufri', font('500', 30), WHITE, .92, shadow=True)
    for i, (s, e, num, big, sub) in enumerate(SCN):
        if i == 0:
            p = 1.0 if t < 3.0 else (1 - ease_out(prog(t, 3.0, .35)))
            if t >= 11.3: p = ease_out(prog(t, 11.4, .5))
            p1 = p2 = p3 = p; out = 1
        else:
            if not (s <= t <= e): continue
            tin = s + 0.35
            out = 1 - ease_out(prog(t, e - 0.45, .35))
            p1 = ease_out(prog(t, tin, .5)); p2 = ease_out(prog(t, tin + .15, .5)); p3 = ease_out(prog(t, tin + .3, .5))
        top = 430
        text(L, (X0, top), num, font('800', 36), GOLD, p1 * out, dy=24 * (1 - p1), shadow=True)
        text(L, (X0, top + 46), big, fit(big, XMAX - X0, 124), WHITE, p2 * out, dy=40 * (1 - p2), shadow=True)
        d = ImageDraw.Draw(L)
        uw = 150 * (p3 if i == 0 else ease_out(prog(t, tin + .35, .6)))
        if uw > 1 and out * p3 > 0:
            d.rounded_rectangle((X0, top + 200, X0 + uw, top + 210), radius=5, fill=GOLD + (int(255 * out * p3),))
        text(L, (X0, top + 232), sub, font('500', 42), WHITE, p3 * out, dy=24 * (1 - p3), shadow=True)
    # signature: gold ski track linking the three slopes (hidden at loop start/end)
    ra = min(prog(t, 0.8, .5), 1 - prog(t, 10.9, .4))
    if ra > 0:
        d = ImageDraw.Draw(L)
        rp = ease_in_out(prog(t, 1.0, 9.0))
        d.line(TRACK, fill=WHITE + (int(80 * ra),), width=4, joint='curve')
        seg = polyline_partial(TRACK, rp)
        if len(seg) > 1: d.line(seg, fill=GOLD + (int(255 * ra),), width=7, joint='curve')
        xa, xb = RX[0], RX[2]
        for j, x in enumerate(RX):
            k = (x - xa) / (xb - xa); y = RY - 30 * k + 16 * math.sin(k * math.pi * 6)
            on = rp >= k - 1e-6
            d.ellipse((x - 11, y - 11, x + 11, y + 11), fill=(GOLD_L if on else WHITE) + (int(255 * ra),), outline=GOLD + (int(255 * ra),), width=5)
            anc = 'ls' if j == 0 else ('ms' if j == 1 else 'rs')
            text(L, (x, y - 36), RLAB[j], font('800', 30), WHITE, ra, anchor=anc, shadow=True)
        cx, cy = seg[-1]
        d.ellipse((cx - 8, cy - 8, cx + 8, cy + 8), fill=WHITE + (int(255 * ra),))
        alt = 2500 + 100 * prog(rp, 0, .5) + 100 * prog(rp, .5, .5)
        alt = round(alt / 10) * 10
        text(L, (xb, RY + 78), f'~{alt:,} m', font('800', 40), GOLD_L, ra, anchor='rs', shadow=True)
        text(L, (xa, RY + 78), 'Three slopes, one winter', font('500', 32), WHITE, ra, anchor='ls', shadow=True)
    im.alpha_composite(L)
    return im.convert('RGB')

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'snap':
        for ts in sys.argv[2:]:
            render(float(ts)).save(f'/home/claude/work/snap-hero-{ts}.jpg', quality=85)
        sys.exit()
    w = Writer('/home/claude/work/out/hero-master.mp4', W, H, FPS)
    for f in range(int(DUR * FPS)):
        w.add(render(f / FPS))
    w.close()
