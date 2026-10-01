"""Solang Valley hero loop: 1920x1080, 30 fps, 12 s, seamless (frame 0 == frame 360). Suzu brand.
Scenes: ropeway -> paragliding -> snow field -> snow tubing. Signature: gold altitude route
Manali ~2,050 m -> Solang ~2,500 m -> Fatru ~3,200 m with a gondola cabin riding the line."""
import sys
from PIL import Image, ImageDraw
from sz import *

W, H, FPS, DUR = 1920, 1080, 30, 12.0
PH = '/home/claude/work/ph/'
A = Photo(PH + 'px29952995-m.jpg', W, H, focus=(0.66, 0.45), zmax=1.30)  # gondola over snow (mirrored: cabin left)
B = Photo(PH + 'px6149892.jpg', W, H, focus=(0.40, 0.45), zmax=1.10)    # paraglider, red wing
C = Photo(PH + 'px34978635.jpg', W, H, focus=(0.5, 0.40), zmax=1.10)    # snow field below peaks
D = Photo(PH + 'lib11622.jpg', W, H, focus=(0.68, 0.78), zmax=1.30)      # family snow tubing
SNOW = Snow(W, H, 110, seed=21, rmin=2, rmax=6)

shade = grad_h(W, H, [(0, 0), (0.28, 0.0), (0.56, 0.6), (1, 0.88)])
shade_v = grad_v(W, H, [(0, .30), (.22, 0), (.72, 0), (1, .55)])
X0, XMAX = 1030, 1850

def fit(s, w, size):
    while size > 40:
        f = font('800', size)
        if f.getlength(s) <= w: return f
        size -= 4
    return font('800', size)

SCN = [
    (0.0, 3.6, '01 · RIDE', 'Ropeway', '1.3 km up to Fatru, ~3,200 m'),
    (3.2, 6.8, '02 · FLY', 'Paragliding', 'Mar–Jun · Oct–Nov, 12+ yrs'),
    (6.4, 9.2, '03 · SNOW', 'Snow days', 'Usually late Dec – Feb'),
    (8.8, 11.3, '04 · PLAY', 'Snow tubing', 'Gentle runs for kids'),
]

def a_img(t): return A.frame(1.20 + 0.09 * ease_in_out(prog(t, 0, 3.6)))
def b_img(t): return B.frame(1.09 - 0.08 * prog(t, 3.2, 3.6))
def c_img(t): return C.frame(1.0 + 0.08 * prog(t, 6.4, 2.8))
def d_img(t): return D.frame(1.18 + 0.08 * prog(t, 8.8, 3.2))

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
    # falling snow over the two winter scenes only; zero at t=0 and t=12
    return min(prog(t, 6.4, .5), 1 - prog(t, 11.1, .7))

# route: 3 nodes, altitude climbs 2,050 -> 2,500 -> 3,200
RX = [X0, (X0 + XMAX - 20) / 2, XMAX - 20]; RALT = [2050, 2500, 3200]; RY = 935
RLAB = ['Manali', 'Solang', 'Fatru']

def render(t):
    im = photo_at(t).convert('RGBA')
    im.alpha_composite(shade); im.alpha_composite(shade_v)
    L = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    sa = snow_alpha(t)
    if sa > 0: SNOW.draw(L, t, alpha=sa * .9, period=DUR)
    text(L, (X0, 150), 'SOLANG VALLEY · MANALI', font('800', 40), GOLD_L, 1.0, shadow=True)
    text(L, (X0, 206), 'by Suzu Travels', font('500', 30), WHITE, .9, shadow=True)
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
        top = 440
        text(L, (X0, top), num, font('800', 36), GOLD, p1 * out, dy=24 * (1 - p1), shadow=True)
        text(L, (X0, top + 46), big, fit(big, XMAX - X0, 132), WHITE, p2 * out, dy=40 * (1 - p2), shadow=True)
        d = ImageDraw.Draw(L)
        uw = 150 * (p3 if i == 0 else ease_out(prog(t, tin + .35, .6)))
        if uw > 1 and out * p3 > 0:
            d.rounded_rectangle((X0, top + 206, X0 + uw, top + 216), radius=5, fill=GOLD + (int(255 * out * p3),))
        text(L, (X0, top + 238), sub, font('500', 44), WHITE, p3 * out, dy=24 * (1 - p3), shadow=True)
    # signature: gold altitude route with a gondola cabin riding it (hidden at loop start/end)
    ra = min(prog(t, 0.8, .5), 1 - prog(t, 10.9, .4))
    if ra > 0:
        d = ImageDraw.Draw(L)
        rp = ease_in_out(prog(t, 1.0, 9.0))
        xa, xb = RX[0], RX[2]
        # cable dips slightly (catenary look)
        pts = [(xa + (xb - xa) * k / 40, RY - 70 * (k / 40) + 22 * math.sin(math.pi * k / 40)) for k in range(41)]
        d.line(pts, fill=WHITE + (int(90 * ra),), width=4)
        seg = polyline_partial(pts, rp)
        if len(seg) > 1: d.line(seg, fill=GOLD + (int(255 * ra),), width=7)
        for j, x in enumerate(RX):
            k = (x - xa) / (xb - xa); y = RY - 70 * k + 22 * math.sin(math.pi * k)
            on = rp >= k - 1e-6
            d.ellipse((x - 11, y - 11, x + 11, y + 11), fill=(GOLD_L if on else WHITE) + (int(255 * ra),), outline=GOLD + (int(255 * ra),), width=5)
            anc = 'ls' if j == 0 else ('ms' if j == 1 else 'rs')
            text(L, (x, y - 34), RLAB[j], font('800', 30), WHITE, ra, anchor=anc, shadow=True)
        # gondola cabin hanging from the moving point
        cx, cy = seg[-1]
        d.line((cx, cy, cx, cy + 22), fill=GOLD_L + (int(255 * ra),), width=4)
        d.rounded_rectangle((cx - 20, cy + 22, cx + 20, cy + 54), radius=8, fill=GOLD + (int(255 * ra),))
        d.rectangle((cx - 13, cy + 28, cx + 13, cy + 38), fill=NAVY + (int(255 * ra),))
        # altitude counter (piecewise through Solang)
        alt = 2050 + (450 * prog(rp, 0, .5) + 700 * prog(rp, .5, .5))
        alt = round(alt / 10) * 10
        text(L, (xb, RY + 22 + 56), f'~{alt:,} m', font('800', 40), GOLD_L, ra, anchor='rs', shadow=True)
        text(L, (xa, RY + 22 + 56), '13–14 km from Manali', font('500', 32), WHITE, ra, anchor='ls', shadow=True)
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
