"""Atal Tunnel & Sissu snow trip hero loop: 1920x1080, 30 fps, 12 s, seamless (frame 0 == frame 360). Suzu brand.
Scenes: SUV on a snowy road -> rock tunnel after snowfall -> snowy valley with a river -> frozen waterfall.
Signature: gold route line Manali ~2,050 m -> tunnel (9.02 km, dashed) -> Sissu ~3,120 m with a rising altitude
counter, plus periodic falling snow. Facts from the brief only. Photos are generic (no place label on a photo)."""
import sys
from PIL import Image, ImageDraw
from sz import *

W, H, FPS, DUR = 1920, 1080, 30, 12.0
PH = '/home/claude/work/ph/'
A = Photo(PH + 'wp_suv-snowy-mountain-road.webp', W, H, focus=(0.42, 0.55), zmax=1.14)
B = Photo(PH + 'px15295177.jpg', W, H, focus=(0.5, 0.62), zmax=1.12)
C = Photo(PH + 'wp_Frozen-river-Spiti-2-scaled.webp', W, H, focus=(0.45, 0.5), zmax=1.12)
D = Photo(PH + 'px12548491.jpg', W, H, focus=(0.4, 0.5), zmax=1.12)
SNOW = Snow(W, H, 120, seed=23, rmin=2, rmax=6)

shade = grad_h(W, H, [(0, 0), (0.30, 0.0), (0.52, 0.66), (1, 0.92)])
shade_v = grad_v(W, H, [(0, .30), (.22, 0), (.66, 0), (1, .70)])
X0, XMAX = 1010, 1850

def fit(s, w, size, wt='800'):
    while size > 40 and font(wt, size).getlength(s) > w: size -= 4
    return font(wt, size)

SCN = [
    (0.0, 3.4, '01 · FROM MANALI', 'Snow, ~40 km away', 'Manali – Atal Tunnel – Sissu'),
    (3.1, 6.4, '02 · THE TUNNEL', '9.02 km under the pass', 'No Rohtang permit needed'),
    (6.1, 9.4, '03 · BEYOND', 'Snow on the far side', 'First snow Oct–Nov · deepest Dec–Feb'),
    (9.1, 11.3, '04 · AFTER SNOWFALL', '4x4 after fresh snow', 'We check road + snow the evening before'),
]

def a_img(t): return A.frame(1.10 + 0.04 * ease_in_out(prog(t, 0, 3.4)), dx=0)
def b_img(t): return B.frame(1.0 + 0.10 * prog(t, 3.1, 3.3))
def c_img(t): return C.frame(1.10 - 0.09 * prog(t, 6.1, 3.3))
def d_img(t): return D.frame(1.0 + 0.09 * prog(t, 9.1, 2.6))

def photo_at(t):
    if t < 3.1: return a_img(t)
    if t < 3.5: return Image.blend(a_img(t), b_img(t), ease_in_out(prog(t, 3.1, .4)))
    if t < 6.1: return b_img(t)
    if t < 6.5: return Image.blend(b_img(t), c_img(t), ease_in_out(prog(t, 6.1, .4)))
    if t < 9.1: return c_img(t)
    if t < 9.5: return Image.blend(c_img(t), d_img(t), ease_in_out(prog(t, 9.1, .4)))
    if t < 11.3: return d_img(t)
    return Image.blend(d_img(t), a_img(0), ease_in_out(prog(t, 11.3, .7)))

# route geometry (right half, bottom band)
PM, PS, PN, PX = (1030, 1000), (1380, 952), (1590, 946), (1830, 918)
ROUTE1 = smooth([PM, (1150, 992), (1270, 970), PS], 14)
ROUTE3 = smooth([PN, (1700, 942), (1770, 925), PX], 14)
T0, T1 = 1.0, 9.6   # route draws over the loop, then fades away for a clean loop

def route(L, t):
    fade = 1 - prog(t, 10.6, .6)
    if fade <= 0 or t < T0: return
    d = ImageDraw.Draw(L)
    p = ease_in_out(prog(t, T0, T1 - T0))
    a = int(255 * fade)
    # three legs by share of progress: road 0-.45, tunnel .45-.70, road .70-1
    p1 = clamp(p / .45); p2 = clamp((p - .45) / .25); p3 = clamp((p - .70) / .30)
    pts = polyline_partial(ROUTE1, p1)
    if len(pts) > 1: d.line(pts, fill=GOLD + (a,), width=8, joint='curve')
    if p2 > 0:  # dashed underground segment
        n = 9
        for k in range(n):
            f0, f1 = k / n, (k + .55) / n
            if f0 > p2: break
            f1 = min(f1, p2)
            x0 = PS[0] + (PN[0] - PS[0]) * f0; y0 = PS[1] + (PN[1] - PS[1]) * f0
            x1 = PS[0] + (PN[0] - PS[0]) * f1; y1 = PS[1] + (PN[1] - PS[1]) * f1
            d.line((x0, y0, x1, y1), fill=GOLD_L + (a,), width=6)
    pts = polyline_partial(ROUTE3, p3)
    if len(pts) > 1: d.line(pts, fill=GOLD + (a,), width=8, joint='curve')
    # nodes + labels
    nodes = [(PM, 'Manali', 0.0), (PS, 'Tunnel 9.02 km', .45), (PX, 'Sissu', 1.0)]
    for (x, y), lab, at in nodes:
        q = clamp((p - at * .94) / .06) if at > 0 else clamp((t - T0) / .3)
        if q <= 0: continue
        r = 11 * ease_back(q, 1.4)
        d.ellipse((x - r, y - r, x + r, y + r), fill=WHITE + (int(a * q),), outline=GOLD + (int(a * q),), width=4)
        anc = 'ls' if at == 0 else ('ms' if at < 1 else 'rs')
        text(L, (x, y - 24), lab, font('800', 28), WHITE, q * fade, anchor=anc, shadow=True)
    # altitude counter: ~2,050 m (Manali) to ~3,120 m (Sissu)
    alt = 2050 + 950 * ease_in_out(p1) + 60 * p2 + 60 * p3
    alt = round(alt / 10) * 10
    text(L, (XMAX, 760), f'~{alt:,} m', font('800', 64), GOLD_L, fade * clamp((t - T0) / .4), anchor='rs', shadow=True)
    text(L, (XMAX, 800), 'ALTITUDE', font('800', 22), WHITE, .85 * fade * clamp((t - T0) / .4), anchor='rs', shadow=True)

def render(t):
    im = photo_at(t).convert('RGBA')
    im.alpha_composite(shade); im.alpha_composite(shade_v)
    L = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    SNOW.draw(L, t, alpha=.8, period=DUR)
    text(L, (X0, 120), 'SNOW · MANALI TO LAHAUL', font('800', 40), GOLD_L, 1.0, shadow=True)
    text(L, (X0, 176), 'Atal Tunnel & Sissu snow day', font('500', 32), WHITE, .92, shadow=True)
    for i, (s, e, num, big, sub) in enumerate(SCN):
        if i == 0:
            p = 1.0 if t < 2.9 else (1 - ease_out(prog(t, 2.9, .35)))
            if t >= 11.3: p = ease_out(prog(t, 11.35, .55))
            p1 = p2 = p3 = p; out = 1; tin = 0
        else:
            if not (s <= t <= e): continue
            tin = s + 0.35
            out = 1 - ease_out(prog(t, e - 0.45, .35))
            p1 = ease_out(prog(t, tin, .5)); p2 = ease_out(prog(t, tin + .15, .5)); p3 = ease_out(prog(t, tin + .3, .5))
        top = 290
        text(L, (X0, top), num, font('800', 36), GOLD, p1 * out, dy=24 * (1 - p1), shadow=True)
        text(L, (X0, top + 46), big, fit(big, XMAX - X0, 104), WHITE, p2 * out, dy=40 * (1 - p2), shadow=True)
        d = ImageDraw.Draw(L)
        uw = 150 * (p3 if i == 0 else ease_out(prog(t, tin + .35, .6)))
        if uw > 1 and out * p3 > 0:
            d.rounded_rectangle((X0, top + 194, X0 + uw, top + 204), radius=5, fill=GOLD + (int(255 * out * p3),))
        text(L, (X0, top + 224), sub, fit(sub, XMAX - X0, 40, '500'), WHITE, p3 * out, dy=24 * (1 - p3), shadow=True)
    route(L, t)
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
