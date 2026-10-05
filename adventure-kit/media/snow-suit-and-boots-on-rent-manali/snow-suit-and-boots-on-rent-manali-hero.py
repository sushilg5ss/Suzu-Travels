"""Snow suit & boots on rent (Manali) hero loop: 1920x1080, 30 fps, 10 s, seamless (frame 0 == frame 300). Suzu brand.
Scenes: snow boots in fresh snow -> mittens + snowball -> group in matching snow suits -> family playing in snow.
Signature: gold 'layers' stack on the right (Thermals -> Fleece -> Snow suit -> Boots + gloves), BRING vs RENT tags,
plus periodic falling snow. Facts from the brief only (thermals/fleece are not rented; suit, boots, gloves are)."""
import sys
from PIL import Image, ImageDraw
from sz import *

W, H, FPS, DUR = 1920, 1080, 30, 10.0
PH = '/home/claude/work/ph/'
A = Photo(PH + 'px6432003-m.jpg', W, H, focus=(0.45, 0.55), zmax=1.16)  # boots in snow (mirrored: boots left)
B = Photo(PH + 'px6012813.jpg', W, H, focus=(0.55, 0.55), zmax=1.14)    # mittens + snowball
C = Photo(PH + 'px671906.jpg', W, H, focus=(0.5, 0.40), zmax=1.10)      # group in matching snow suits
D = Photo(PH + 'px6617714.jpg', W, H, focus=(0.5, 0.5), zmax=1.12)      # family playing in snow
SNOW = Snow(W, H, 110, seed=17, rmin=2, rmax=6)

shade = grad_h(W, H, [(0, 0), (0.30, 0.0), (0.54, 0.66), (1, 0.92)])
shade_v = grad_v(W, H, [(0, .30), (.22, 0), (.70, 0), (1, .55)])
X0, XMAX = 1030, 1850

def fit(s, w, size, wt='800'):
    while size > 40 and font(wt, size).getlength(s) > w: size -= 4
    return font(wt, size)

SCN = [
    (0.0, 2.9, '01 · BOOTS', 'Dry feet first', 'Snow boots, both the same size'),
    (2.6, 5.4, '02 · GLOVES', 'Warm, dry hands', 'Waterproof gloves for snow play'),
    (5.1, 7.9, '03 · SUIT', 'One suit on top', 'Waterproof, one- or two-piece'),
    (7.6, 9.4, '04 · ON THE WAY', 'Picked up en route', 'Solang · Gulaba · Sissu'),
]

def a_img(t): return A.frame(1.10 + 0.06 * ease_in_out(prog(t, 0, 2.9)))
def b_img(t): return B.frame(1.0 + 0.08 * prog(t, 2.6, 2.8))
def c_img(t): return C.frame(1.09 - 0.08 * prog(t, 5.1, 2.8))
def d_img(t): return D.frame(1.0 + 0.08 * prog(t, 7.6, 2.4))

def photo_at(t):
    if t < 2.6: return a_img(t)
    if t < 3.0: return Image.blend(a_img(t), b_img(t), ease_in_out(prog(t, 2.6, .4)))
    if t < 5.1: return b_img(t)
    if t < 5.5: return Image.blend(b_img(t), c_img(t), ease_in_out(prog(t, 5.1, .4)))
    if t < 7.6: return c_img(t)
    if t < 8.0: return Image.blend(c_img(t), d_img(t), ease_in_out(prog(t, 7.6, .4)))
    if t < 9.4: return d_img(t)
    return Image.blend(d_img(t), a_img(0), ease_in_out(prog(t, 9.4, .6)))

LAYERS = [('Thermals', 'BRING'), ('Fleece / sweater', 'BRING'), ('Snow suit', 'RENT'), ('Boots + gloves', 'RENT')]
LT = [0.9, 2.9, 5.4, 7.9]   # each layer drops in as its scene starts
LX0, LX1, LH, LGAP, LBOT = X0, XMAX, 52, 10, 1000

def render(t):
    im = photo_at(t).convert('RGBA')
    im.alpha_composite(shade); im.alpha_composite(shade_v)
    L = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    SNOW.draw(L, t, alpha=.8, period=DUR)
    text(L, (X0, 120), 'SNOW GEAR · MANALI', font('800', 40), GOLD_L, 1.0, shadow=True)
    text(L, (X0, 176), 'Suit + boots + gloves, sized for every guest', font('500', 30), WHITE, .92, shadow=True)
    for i, (s, e, num, big, sub) in enumerate(SCN):
        if i == 0:
            p = 1.0 if t < 2.4 else (1 - ease_out(prog(t, 2.4, .35)))
            if t >= 9.4: p = ease_out(prog(t, 9.45, .45))
            p1 = p2 = p3 = p; out = 1; tin = 0
        else:
            if not (s <= t <= e): continue
            tin = s + 0.35
            out = 1 - ease_out(prog(t, e - 0.45, .35))
            p1 = ease_out(prog(t, tin, .5)); p2 = ease_out(prog(t, tin + .15, .5)); p3 = ease_out(prog(t, tin + .3, .5))
        top = 300
        text(L, (X0, top), num, font('800', 36), GOLD, p1 * out, dy=24 * (1 - p1), shadow=True)
        text(L, (X0, top + 46), big, fit(big, XMAX - X0, 118), WHITE, p2 * out, dy=40 * (1 - p2), shadow=True)
        d = ImageDraw.Draw(L)
        uw = 150 * (p3 if i == 0 else ease_out(prog(t, tin + .35, .6)))
        if uw > 1 and out * p3 > 0:
            d.rounded_rectangle((X0, top + 192, X0 + uw, top + 202), radius=5, fill=GOLD + (int(255 * out * p3),))
        text(L, (X0, top + 222), sub, fit(sub, XMAX - X0, 42, '500'), WHITE, p3 * out, dy=24 * (1 - p3), shadow=True)
    # signature: layers stack (empty at loop start/end so frame 0 == last frame)
    fade = 1 - prog(t, 9.2, .4)
    d = ImageDraw.Draw(L)
    for k, ((lab, tag), lt) in enumerate(zip(LAYERS, LT)):
        p = ease_back(prog(t, lt, .55), 1.2)
        a = clamp(prog(t, lt, .25)) * fade
        if a <= 0: continue
        y1 = LBOT - k * (LH + LGAP); y0 = y1 - LH
        dy = -70 * (1 - clamp(p, 0, 1.2))
        rent = tag == 'RENT'
        fill = (GOLD if rent else WHITE) + (int((235 if rent else 60) * a),)
        d.rounded_rectangle((LX0, y0 + dy, LX1, y1 + dy), radius=14, fill=fill,
                            outline=(GOLD if rent else (255, 255, 255)) + (int(255 * a),), width=3)
        text(L, (LX0 + 26, (y0 + y1) / 2 + dy), lab, font('800', 30), NAVY if rent else WHITE, a, anchor='lm')
        text(L, (LX1 - 26, (y0 + y1) / 2 + dy), tag, font('800', 24), NAVY if rent else GOLD_L, a, anchor='rm')
    ka = clamp(prog(t, 0.9, .3)) * fade
    if ka > 0:
        text(L, (LX0, LBOT - 4 * (LH + LGAP) - 14), 'HOW TO LAYER FOR SNOW', font('800', 26), GOLD_L, ka, anchor='ls', shadow=True)
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
