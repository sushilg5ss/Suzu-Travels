"""Snow Kingdom Kufri explainer 'Real snow, any month': 1920x1080, 30 fps, 11 s. Facts from the 7 Oct 2026 brief only."""
import sys
from PIL import Image, ImageDraw
from sz import *

W, H, FPS, DUR = 1920, 1080, 30, 11.0
BG = grad_v(W, H, [(0, 0.0), (1, 0.0)])
SNOW = Snow(W, H, 70, seed=5, rmin=1.5, rmax=4)
MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
OUT_ON = {0, 1, 11}
X0, X1 = 500, 1800
CW = (X1 - X0) / 12

def base():
    im = Image.new('RGBA', (W, H), NAVY + (255,))
    d = ImageDraw.Draw(im)
    return im

def fit(s, w, size, wt='800'):
    while size > 24 and font(wt, size).getlength(s) > w: size -= 2
    return font(wt, size)

def calendar(L, t, a):
    d = ImageDraw.Draw(L)
    text(L, (120, 110), 'REAL SNOW, ANY MONTH', font('800', 40), GOLD, a)
    text(L, (120, 160), 'When can you play in snow near Shimla?', font('800', 64), WHITE, a)
    for k, m in enumerate(MON):
        text(L, (X0 + k * CW + CW / 2, 400), m, font('800', 34), WHITE, a * .85, anchor='mm')
    rows = [(530, 'Outdoor Kufri', 'natural snow', OUT_ON, 1.2, (170, 200, 230)),
            (720, 'Indoor snow park', 'Snow Kingdom', set(range(12)), 3.0, GOLD)]
    for y, lab, sub, on, t0, col in rows:
        text(L, (120, y - 26), lab, fit(lab, X0 - 140, 40), WHITE, a)
        text(L, (120, y + 26), sub, font('500', 32), (210, 222, 235), a)
        for k in range(12):
            x = X0 + k * CW
            d.rounded_rectangle((x + 6, y - 40, x + CW - 6, y + 40), radius=16, fill=(255, 255, 255, int(28 * a)))
            if k in on:
                order = k if on is not OUT_ON else {11: 0, 0: 1, 1: 2}[k]
                p = ease_back(prog(t, t0 + order * .12, .35))
                if p > 0:
                    cx, cy = x + CW / 2, y
                    hw, hh = (CW / 2 - 6) * p, 40 * p
                    d.rounded_rectangle((cx - hw, cy - hh, cx + hw, cy + hh), radius=16, fill=col + (int(255 * a),))
    # verdict line
    pv = ease_out(prog(t, 4.6, .5))
    text(L, (120, 880), 'Dec–Feb: do both.  Mar–Nov: indoor is the sure snow.', font('800', 50), GOLD_L, a * pv, dy=20 * (1 - pv))

def ring(L, t, a):
    d = ImageDraw.Draw(L)
    cx, cy, R = 560, 560, 270
    text(L, (120, 110), 'ONE SESSION', font('800', 40), GOLD, a)
    text(L, (120, 160), 'About an hour, gear included', font('800', 64), WHITE, a)
    p = ease_in_out(prog(t, 6.1, 1.8))
    d.ellipse((cx - R, cy - R + 60, cx + R, cy + R + 60), outline=(255, 255, 255, int(40 * a)), width=44)
    ang = 360 * p
    g = min(ang, 90)
    if g > 0: d.arc((cx - R, cy - R + 60, cx + R, cy + R + 60), -90, -90 + g, fill=(170, 200, 230, int(255 * a)), width=44)
    if ang > 90: d.arc((cx - R, cy - R + 60, cx + R, cy + R + 60), 0, -90 + ang, fill=GOLD + (int(255 * a),), width=44)
    mins = round(60 * p)
    text(L, (cx, cy + 40), f'{mins}', font('800', 150), WHITE, a, anchor='mm')
    text(L, (cx, cy + 140), 'minutes', font('500', 40), WHITE, a * .9, anchor='mm')
    p1 = ease_out(prog(t, 6.4, .5)); p2 = ease_out(prog(t, 7.4, .5))
    d.rounded_rectangle((980, 420, 1012, 452), radius=8, fill=(170, 200, 230, int(255 * a * p1)))
    text(L, (1040, 412), '~15 min · gear up', font('800', 56), WHITE, a * p1, dy=20 * (1 - p1))
    text(L, (1040, 484), 'Snow jacket, boots and gloves given', font('500', 38), (210, 222, 235), a * p1, dy=20 * (1 - p1))
    d.rounded_rectangle((980, 620, 1012, 652), radius=8, fill=GOLD + (int(255 * a * p2),))
    text(L, (1040, 612), '~45 min · in the snow', font('800', 56), WHITE, a * p2, dy=20 * (1 - p2))
    text(L, (1040, 684), 'Sledging, tube rides, slides, snowballs', font('500', 38), (210, 222, 235), a * p2, dy=20 * (1 - p2))

def endcard(L, t, a):
    d = ImageDraw.Draw(L)
    p = ease_in_out(prog(t, 9.0, 1.0))
    xa, xb, y = 360, 1560, 520
    d.line((xa, y, xb, y), fill=(255, 255, 255, int(70 * a)), width=6)
    d.line((xa, y, xa + (xb - xa) * p, y), fill=GOLD + (int(255 * a),), width=10)
    for x in (xa, xb):
        d.ellipse((x - 18, y - 18, x + 18, y + 18), fill=WHITE + (int(255 * a),), outline=GOLD + (int(255 * a),), width=7)
    text(L, (xa, y - 50), 'Shimla', font('800', 60), WHITE, a, anchor='ms')
    text(L, (xb, y - 50), 'Kufri', font('800', 60), WHITE, a, anchor='ms')
    text(L, ((xa + xb) / 2, y + 80), '16–20 km · 30–45 min by cab', font('500', 44), WHITE, a * .95, anchor='mt')
    pq = ease_back(prog(t, 9.6, .5))
    if pq > 0:
        _f = font('800', 44); _w = _f.getlength('Hotel + cab + snow day · Get Quote') + 60
        pill(L, (W / 2 - _w / 2, 760), 'Hotel + cab + snow day · Get Quote', font('800', 44), GOLD, NAVY, a, scale=pq)

def render(t):
    im = base()
    L = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    SNOW.draw(L, t, alpha=.35)
    a1 = prog(t, 0, .4) * (1 - prog(t, 5.5, .4))
    a2 = prog(t, 5.8, .4) * (1 - prog(t, 8.5, .4))
    a3 = prog(t, 8.8, .4)
    if a1 > 0: calendar(L, t, a1)
    if a2 > 0: ring(L, t, a2)
    if a3 > 0: endcard(L, t, a3)
    text(L, (W - 80, H - 50), 'suzutravels.com', font('500', 30), WHITE, .8, anchor='rs')
    im.alpha_composite(L)
    return im.convert('RGB')

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'snap':
        for ts in sys.argv[2:]:
            render(float(ts)).save(f'/home/claude/work/out/snap-ex-{ts}.jpg', quality=85)
        sys.exit()
    w = Writer('/home/claude/work/out/explainer-master.mp4', W, H, FPS)
    for f in range(int(DUR * FPS)):
        w.add(render(f / FPS))
    w.close()
