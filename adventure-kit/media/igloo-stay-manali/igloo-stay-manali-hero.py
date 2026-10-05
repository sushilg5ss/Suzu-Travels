"""Igloo stay (Sethan, Manali) hero loop: 1920x1080, 30 fps, 12 s, seamless (frame 0 == frame 360). Suzu brand.
Scenes: lit snow igloo at night -> SUV on a snowy road -> friends at a bonfire in the snow -> bonfire sparks.
Signature: gold sparks rising + an outside-temperature gauge falling 0 -> about -15 C (brief: nights can fall to -15 C
or lower outside), plus falling snow. Facts from the brief only; generic photos, no place label on a photo; no prices."""
import sys, random
from PIL import Image, ImageDraw
from sz import *

W, H, FPS, DUR = 1920, 1080, 30, 12.0
PH = '/home/claude/work/ph/'
A = Photo(PH + 'px35907592-m.jpg', W, H, focus=(0.45, 0.5), zmax=1.14)  # mirrored: lit igloo left
B = Photo(PH + 'wp_suv-snowy-mountain-road.webp', W, H, focus=(0.42, 0.55), zmax=1.12)
C = Photo(PH + 'px6623929.jpg', W, H, focus=(0.35, 0.55), zmax=1.12)
D = Photo(PH + 'px16053277-m.jpg', W, H, focus=(0.55, 0.55), zmax=1.12)  # mirrored: fire left
SNOW = Snow(W, H, 90, seed=31, rmin=2, rmax=5)
_r = random.Random(9)
SPARKS = [(_r.uniform(1050, 1880), _r.uniform(0, H), _r.uniform(2, 4.5), _r.choice([1, 2, 3]), _r.uniform(0, 6.28)) for _ in range(46)]

shade = grad_h(W, H, [(0, 0), (0.30, 0.0), (0.52, 0.66), (1, 0.92)])
shade_v = grad_v(W, H, [(0, .30), (.22, 0), (.66, 0), (1, .70)])
X0, XMAX = 1010, 1850

def fit(s, w, size, wt='800'):
    while size > 40 and font(wt, size).getlength(s) > w: size -= 4
    return font(wt, size)

SCN = [
    (0.0, 3.4, '01 · THE NIGHT', 'Sleep in a snow igloo', 'Hand-built igloos, about 12 km above Manali'),
    (3.1, 6.4, '02 · THE ROAD', 'Up by 4x4', '1–2 hrs from Manali in winter'),
    (6.1, 9.4, '03 · THE EVENING', 'Bonfire + snow play', 'Meals and bonfire usually included'),
    (9.1, 11.3, '04 · THE SEASON', 'Mid-Jan to mid-Mar', 'Snow-dependent · check-in around lunch'),
]

def a_img(t): return A.frame(1.10 + 0.04 * ease_in_out(prog(t, 0, 3.4)))
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

def sparks(L, t):
    d = ImageDraw.Draw(L)
    for x0, y0, r, k, ph in SPARKS:  # periodic: k loops per DUR
        y = (y0 - k * (H + 40) * t / DUR) % (H + 40) - 20
        x = x0 + 18 * math.sin(2 * math.pi * t / DUR * 3 + ph)
        a = int(200 * (0.35 + 0.65 * (0.5 + 0.5 * math.sin(2 * math.pi * t / DUR * 6 + ph))) * clamp(y / 500))
        d.ellipse((x - r, y - r, x + r, y + r), fill=GOLD_L + (a,))

GX0, GX1, GY = 1010, 1850, 905
def gauge(L, t):
    fade = 1 - prog(t, 10.7, .5)
    ga = clamp((t - 0.8) / .4) * fade
    if ga <= 0: return
    p = ease_in_out(prog(t, 1.0, 8.6))
    temp = round(-15 * p)
    d = ImageDraw.Draw(L)
    text(L, (GX0, GY - 58), 'OUTSIDE AT NIGHT', font('800', 24), WHITE, .85 * ga, shadow=True)
    text(L, (GX1, GY - 30), f'{temp} °C' if temp else '0 °C', font('800', 64), GOLD_L, ga, anchor='rs', shadow=True)
    d.rounded_rectangle((GX0, GY, GX1, GY + 16), radius=8, fill=(255, 255, 255, int(60 * ga)))
    xe = GX1 - (GX1 - GX0) * p
    d.rounded_rectangle((xe, GY, GX1, GY + 16), radius=8, fill=GOLD + (int(255 * ga),))
    for k, lab in ((0, '0'), (5, '-5'), (10, '-10'), (15, '-15')):
        x = GX1 - (GX1 - GX0) * k / 15
        text(L, (x, GY + 30), lab, font('500', 22), WHITE, .8 * ga, anchor='ma')
    ia = clamp((p - .6) / .2) * ga
    text(L, (GX0, GY + 66), 'Inside: warm bedding', font('800', 26), GOLD_L, ia, anchor='la', shadow=True)

def render(t):
    im = photo_at(t).convert('RGBA')
    im.alpha_composite(shade); im.alpha_composite(shade_v)
    L = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    SNOW.draw(L, t, alpha=.7, period=DUR)
    sparks(L, t)
    text(L, (X0, 120), 'SNOW · SETHAN, HAMPTA VALLEY', font('800', 40), GOLD_L, 1.0, shadow=True)
    text(L, (X0, 176), 'Igloo stay near Manali, ~2,700 m', font('500', 32), WHITE, .92, shadow=True)
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
    gauge(L, t)
    im.alpha_composite(L)
    return im.convert('RGB')

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'snap':
        for ts in sys.argv[2:]:
            render(float(ts)).save(f'/home/claude/work/snap-ihero-{ts}.jpg', quality=85)
        sys.exit()
    w = Writer('/home/claude/work/out2/hero-master.mp4', W, H, FPS)
    for f in range(int(DUR * FPS)):
        w.add(render(f / FPS))
    w.close()
