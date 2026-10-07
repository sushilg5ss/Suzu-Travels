"""Snow Kingdom Kufri hero loop: 1920x1080, 30 fps, 12 s, seamless (frame 0 == frame 360). Suzu brand.
Deterministic PIL + ffmpeg renderer (sz.py). Photos: Pexels 6617714 (mirrored), 1620651, 10589592 (mirrored), 6618008."""
import sys, os
from PIL import Image, ImageDraw, ImageOps
from sz import *

W, H, FPS, DUR = 1920, 1080, 30, 12.0
PH = '/home/claude/work/ph/'
def mir(src, dst):
    if not os.path.exists(dst): ImageOps.mirror(Image.open(src)).save(dst, quality=95)
    return dst
A = Photo(mir(PH + 'px6617714.jpg', PH + 'px6617714-m.jpg'), W, H, focus=(0.45, 0.55), zmax=1.10)
B = Photo(PH + 'px1620651.jpg', W, H, focus=(0.35, 0.5), zmax=1.10)
C = Photo(mir(PH + 'px10589592.jpg', PH + 'px10589592-m.jpg'), W, H, focus=(0.42, 0.55), zmax=1.12)
D = Photo(PH + 'px6618008.jpg', W, H, focus=(0.5, 0.45), zmax=1.10)
SNOW = Snow(W, H, 120, seed=21, rmin=2, rmax=6)

shade = grad_h(W, H, [(0, 0), (0.40, 0.0), (0.58, 0.58), (1, 0.88)])
shade_v = grad_v(W, H, [(0, .30), (.22, 0), (.74, 0), (1, .5)])
X0, XMAX = 1030, 1850

FACTS = [
    ('Real snow, any month', 'An indoor snow park that never melts'),
    ('About a 1-hour session', '15 min gear-up + 45 min in the snow'),
    ('Gear included', 'Snow jacket, boots and gloves given'),
    ('Sledges, tubes & slides', 'Plus snowballs and a snowman zone'),
]
SLOT = [(0.0, 3.0), (3.0, 6.0), (6.0, 9.0), (9.0, 12.0)]

def a_img(t): return A.frame(1.0 + 0.09 * ease_in_out(prog(t, 0, 3.6)))
def b_img(t): return B.frame(1.10 - 0.09 * prog(t, 2.7, 3.6))
def c_img(t): return C.frame(1.0 + 0.10 * prog(t, 5.6, 3.6))
def d_img(t): return D.frame(1.10 - 0.09 * prog(t, 8.5, 3.4))

def photo_at(t):
    if t < 2.7: return a_img(t)
    if t < 3.3: return Image.blend(a_img(t), b_img(t), ease_in_out(prog(t, 2.7, .6)))
    if t < 5.6: return b_img(t)
    if t < 6.2: return Image.blend(b_img(t), c_img(t), ease_in_out(prog(t, 5.6, .6)))
    if t < 8.5: return c_img(t)
    if t < 9.1: return Image.blend(c_img(t), d_img(t), ease_in_out(prog(t, 8.5, .6)))
    if t < 11.2: return d_img(t)
    return Image.blend(d_img(t), a_img(0), ease_in_out(prog(t, 11.2, .8)))

def fit(s, w, size, wt='800'):
    while size > 30:
        f = font(wt, size)
        if f.getlength(s) <= w: return f
        size -= 2
    return font(wt, size)

MONTHS = 'JFMAMJJASOND'

def render(t):
    im = photo_at(t).convert('RGBA')
    im.alpha_composite(shade); im.alpha_composite(shade_v)
    L = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    SNOW.draw(L, t, alpha=.85, period=DUR)
    text(L, (X0, 170), 'KUFRI · NEAR SHIMLA', font('800', 40), GOLD_L, 1, shadow=True)
    text(L, (X0, 226), 'Snow Kingdom', fit('Snow Kingdom', XMAX - X0, 112), WHITE, 1, shadow=True)
    # chip pulse
    sc = 1 + .05 * math.sin(math.pi * prog(t, .8, .6))
    pill(L, (X0, 372), 'Real snow · all year', font('800', 40), GOLD, NAVY, 1, scale=sc)
    # rotating facts; fact 0 fully visible at t=0 and t=12
    for i, (big, sub) in enumerate(FACTS):
        s, e = SLOT[i]
        if i == 0:
            p = 1.0 if t < 2.55 else 1 - ease_out(prog(t, 2.55, .35))
            if t >= 11.0: p = ease_out(prog(t, 11.1, .5))
            pin, out = p, 1
        else:
            if not (s - .1 <= t <= e): continue
            pin = ease_out(prog(t, s + .1, .5)); out = 1 - ease_out(prog(t, e - .45, .35))
        a = pin * out
        if a <= 0: continue
        text(L, (X0, 520), big, fit(big, XMAX - X0, 72), WHITE, a, dy=30 * (1 - pin), shadow=True)
        text(L, (X0, 612), sub, fit(sub, XMAX - X0, 42, '500'), WHITE, a * .95, dy=24 * (1 - pin), shadow=True)
    # signature: 12-month strip; the indoor bar lights every month (hidden at loop start/end)
    ra = min(prog(t, 0.9, .5), 1 - prog(t, 10.7, .4))
    if ra > 0:
        d = ImageDraw.Draw(L)
        y = 800; cw = (XMAX - X0) / 12
        text(L, (X0, y - 22), 'Indoor snow, month by month', font('500', 32), WHITE, ra * .95, anchor='ls', shadow=True)
        lit = ease_in_out(prog(t, 1.4, 8.0)) * 12
        for k, m in enumerate(MONTHS):
            x = X0 + k * cw
            on = clamp(lit - k)
            d.rounded_rectangle((x + 4, y, x + cw - 4, y + 64), radius=12,
                                fill=(GOLD if on > .5 else (255, 255, 255)) + (int((255 if on > .5 else 46) * ra),))
            text(L, (x + cw / 2, y + 33), m, font('800', 32), NAVY if on > .5 else WHITE, ra, anchor='mm')
        n = int(min(12, lit + .5))
        text(L, (XMAX, y + 120), f'{n}/12 months', font('800', 44), GOLD_L, ra, anchor='rs', shadow=True)
        text(L, (X0, y + 120), 'Shimla to Kufri · 16–20 km', font('500', 34), WHITE, ra, anchor='ls', shadow=True)
    text(L, (XMAX, 1040), 'suzutravels.com', font('500', 28), WHITE, .85, anchor='rs', shadow=True)
    im.alpha_composite(L)
    return im.convert('RGB')

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'snap':
        for ts in sys.argv[2:]:
            render(float(ts)).save(f'/home/claude/work/out/snap-hero-{ts}.jpg', quality=85)
        sys.exit()
    w = Writer('/home/claude/work/out/hero-master.mp4', W, H, FPS)
    for f in range(int(DUR * FPS)):
        w.add(render(f / FPS))
    w.close()
