"""Kufri hero loop: 1920x1080, 30 fps, 12 s, seamless (frame 0 == frame 360). Suzu brand."""
import sys
from PIL import Image, ImageDraw
from sz import *

W, H, FPS, DUR = 1920, 1080, 30, 12.0
PH = '/home/claude/work/ph/'
A = Photo(PH + 'px12932967.jpg', W, H, focus=(0.42, 0.62), zmax=1.10)   # sledging
B = Photo(PH + 'px10549768.jpg', W, H, focus=(0.35, 0.55), zmax=1.10)   # horse trail
C = Photo(PH + 'px2041759-m.jpg', W, H, focus=(0.55, 0.55), zmax=1.10)  # zipline (mirrored: rider left)
from PIL import ImageFilter
_D = Photo(PH + 'px236974.jpg', W, H, focus=(0.5, 0.6), zmax=1.10)
DCARD = Photo(PH + 'px236974.jpg', 860, 640, focus=(0.62, 0.62), zmax=1.08)
_Dbg = _D.frame(1.0).resize((W // 8, H // 8)).filter(ImageFilter.GaussianBlur(3)).resize((W, H), Image.BILINEAR).convert('RGBA')
_sh = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ImageDraw.Draw(_sh).rounded_rectangle((110, 250, 970, 890), radius=28, fill=(0, 0, 0, 130))
_Dbg.alpha_composite(_sh.filter(ImageFilter.GaussianBlur(26))); _Dbg = _Dbg.convert('RGB')
_m = Image.new('L', (860, 640), 0); ImageDraw.Draw(_m).rounded_rectangle((0, 0, 860, 640), radius=28, fill=255)
class _Card:
    def frame(self, z):
        bg = _Dbg.copy(); bg.paste(DCARD.frame(z), (100, 230), _m)
        ImageDraw.Draw(bg).rounded_rectangle((100, 230, 960, 870), radius=28, outline=GOLD, width=6)
        return bg
D = _Card()
SNOW = Snow(W, H, 110, seed=11, rmin=2, rmax=6)

shade = grad_h(W, H, [(0, 0), (0.40, 0.0), (0.60, 0.55), (1, 0.86)])
shade_v = grad_v(W, H, [(0, .30), (.22, 0), (.74, 0), (1, .45)])
X0, XMAX = 1030, 1850

def fit(s, w, size):
    while size > 40:
        f = font('800', size)
        if f.getlength(s) <= w: return f
        size -= 4
    return font('800', size)

SCN = [
    (0.0, 3.6, '01 · SNOW', 'Sledging', 'Snow play for kids, Dec–Feb'),
    (3.2, 6.8, '02 · RIDE', 'Horse rides', '30–45 min up through the pines'),
    (6.4, 9.2, '03 · FLY', 'Zipline', 'A quick thrill above the trees'),
    (8.8, 11.3, '04 · RACE', 'Go-karts', 'Family fun at the adventure park'),
]

def a_img(t): return A.frame(1.0 + 0.09 * ease_in_out(prog(t, 0, 3.6)))
def b_img(t): return B.frame(1.09 - 0.08 * prog(t, 3.2, 3.6))
def c_img(t): return C.frame(1.0 + 0.08 * prog(t, 6.4, 2.8))
def d_img(t): return D.frame(1.0 + 0.07 * prog(t, 8.8, 3.2))

def photo_at(t):
    if t < 3.2: return a_img(t)
    if t < 3.6: return Image.blend(a_img(t), b_img(t), ease_in_out(prog(t, 3.2, .4)))
    if t < 6.4: return b_img(t)
    if t < 6.8: return Image.blend(b_img(t), c_img(t), ease_in_out(prog(t, 6.4, .4)))
    if t < 8.8: return c_img(t)
    if t < 9.2: return Image.blend(c_img(t), d_img(t), ease_in_out(prog(t, 8.8, .4)))
    if t < 11.3: return d_img(t)
    return Image.blend(d_img(t), a_img(0), ease_in_out(prog(t, 11.3, .7)))

def snow_alpha(t):
    # snow over the winter scene only; identical (full) at t=0 and t=12
    if t < 3.6: return 1 - prog(t, 3.2, .4)
    if t >= 11.3: return prog(t, 11.3, .7)
    return 0

def render(t):
    im = photo_at(t).convert('RGBA')
    im.alpha_composite(shade); im.alpha_composite(shade_v)
    L = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    sa = snow_alpha(t)
    if sa > 0: SNOW.draw(L, t, alpha=sa * .9, period=DUR)
    ka = 1.0  # kicker is constant (present in first and last frame)
    text(L, (X0, 150), 'KUFRI · SHIMLA', font('800', 40), GOLD_L, ka, shadow=True)
    text(L, (X0, 206), 'by Suzu Travels', font('500', 30), WHITE, .9, shadow=True)
    for i, (s, e, num, big, sub) in enumerate(SCN):
        if i == 0:
            # scene 1 text is fully visible at t=0 and fades back in at the loop end
            p = 1.0 if t < 3.0 else (1 - ease_out(prog(t, 3.0, .35)))
            if t >= 11.3: p = ease_out(prog(t, 11.4, .5))
            p1 = p2 = p3 = p; out = 1
        else:
            if not (s <= t <= e): continue
            tin = s + 0.35
            out = 1 - ease_out(prog(t, e - 0.45, .35))
            p1 = ease_out(prog(t, tin, .5)); p2 = ease_out(prog(t, tin + .15, .5)); p3 = ease_out(prog(t, tin + .3, .5))
        top = 470
        text(L, (X0, top), num, font('800', 36), GOLD, p1 * out, dy=24 * (1 - p1), shadow=True)
        text(L, (X0, top + 46), big, fit(big, XMAX - X0, 132), WHITE, p2 * out, dy=40 * (1 - p2), shadow=True)
        d = ImageDraw.Draw(L)
        uw = 150 * (p3 if i == 0 else ease_out(prog(t, tin + .35, .6)))
        if uw > 1 and out * p3 > 0:
            d.rounded_rectangle((X0, top + 206, X0 + uw, top + 216), radius=5, fill=GOLD + (int(255 * out * p3),))
        text(L, (X0, top + 238), sub, font('500', 46), WHITE, p3 * out, dy=24 * (1 - p3), shadow=True)
    # signature: gold route Shimla -> Kufri with rising altitude counter (hidden at loop start/end)
    ra = min(prog(t, 0.8, .5), 1 - prog(t, 10.9, .4))
    if ra > 0:
        y = 930; xa, xb = X0, XMAX - 20
        rp = ease_in_out(prog(t, 1.0, 9.0))
        d = ImageDraw.Draw(L)
        d.line((xa, y, xb, y), fill=WHITE + (int(90 * ra),), width=4)
        d.line((xa, y, xa + (xb - xa) * rp, y), fill=GOLD + (int(255 * ra),), width=7)
        for x in (xa, xb):
            d.ellipse((x - 11, y - 11, x + 11, y + 11), fill=WHITE + (int(255 * ra),), outline=GOLD + (int(255 * ra),), width=5)
        cx = xa + (xb - xa) * rp
        d.ellipse((cx - 8, y - 8, cx + 8, y + 8), fill=GOLD_L + (int(255 * ra),))
        text(L, (xa, y - 30), 'Shimla', font('800', 32), WHITE, ra, anchor='ls', shadow=True)
        text(L, (xb, y - 30), 'Kufri', font('800', 32), WHITE, ra, anchor='rs', shadow=True)
        alt = 2200 + round((2650 - 2200) * rp / 10) * 10
        text(L, (xb, y + 58), f'~{alt:,} m', font('800', 40), GOLD_L, ra, anchor='rs', shadow=True)
        text(L, (xa, y + 58), '16–20 km', font('500', 34), WHITE, ra, anchor='ls', shadow=True)
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
