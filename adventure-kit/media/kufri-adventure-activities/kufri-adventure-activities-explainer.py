"""Kufri explainer: 'Your Kufri half-day'. 1920x1080, 30 fps, 12 s. Facts only from the brief."""
import sys
from PIL import Image, ImageDraw
from sz import *

W, H, FPS, DUR = 1920, 1080, 30, 12.0
BG = Image.new('RGBA', (W, H), NAVY + (255,))
glow = Image.new('RGBA', (W, H), (0, 0, 0, 0)); gd = ImageDraw.Draw(glow)
for r in range(760, 0, -20):
    gd.ellipse((1560 - r, 120 - r, 1560 + r, 120 + r), fill=(22, 57, 92, int(3 + 0.9 * (760 - r) / 20)))
BG.alpha_composite(glow)
snow = Snow(W, H, 90, seed=5, rmin=2, rmax=5)
CARD = (22, 57, 92)

STOPS = [  # title, line2, time label
    ('Adventure park', 'go-karts, zipline, rides', '1–2 h'),
    ('Horse ride', 'up to Mahasu Peak', '30–45 min'),
    ('Nature Park', 'Himalayan wildlife', '1.5–2 h'),
    ('Green Valley', 'photo stop', '15 min'),
]
CX = [120, 560, 1000, 1440]; CW, CT, CH = 360, 520, 300

def render(t):
    im = BG.copy(); L = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    endp = prog(t, 10.2, .45); main = 1 - endp
    winter = ease_out(prog(t, 8.2, .6))
    snow.draw(L, t, alpha=0.45 * winter * main + 0.3 * endp)
    p = ease_out(prog(t, .1, .5))
    text(L, (120, 80), 'KUFRI · SHIMLA', font('800', 36), GOLD, p * main, dy=-16 * (1 - p))
    p2 = ease_out(prog(t, .25, .5))
    text(L, (120, 128), 'Your Kufri half-day', font('800', 92), WHITE, p2 * main, dy=30 * (1 - p2))
    # route strip with altitude counter
    y = 360; xa, xb = 160, 1760
    rp = ease_in_out(prog(t, .7, 2.4)); ra = ease_out(prog(t, .55, .4)) * main
    if ra > 0:
        d.line((xa, y, xb, y), fill=(255, 255, 255, int(70 * ra)), width=4)
        d.line((xa, y, xa + (xb - xa) * rp, y), fill=GOLD + (int(255 * ra),), width=8)
        for x, lab, anc in ((xa, 'Shimla', 'ls'), (xb, 'Kufri', 'rs')):
            d.ellipse((x - 14, y - 14, x + 14, y + 14), fill=WHITE + (int(255 * ra),), outline=GOLD + (int(255 * ra),), width=6)
            text(L, (x, y - 36), lab, font('800', 42), WHITE, ra, anchor=anc)
        cx = xa + (xb - xa) * rp
        d.ellipse((cx - 10, y - 10, cx + 10, y + 10), fill=GOLD_L + (int(255 * ra),))
        alt = 2200 + round(450 * rp / 10) * 10
        text(L, (xb, y + 62), f'~{alt:,} m', font('800', 48), GOLD_L, ra, anchor='rs')
        text(L, (xa, y + 62), '~2,200 m', font('500', 36), WHITE, ra * .8, anchor='ls')
        text(L, ((xa + xb) / 2, y + 62), '16–20 km · 30–45 min on NH-5', font('500', 38), WHITE, ra * ease_out(prog(t, 1.6, .5)), anchor='ms')
    # four stops
    for i, (a, b, tl) in enumerate(STOPS):
        t0 = 3.3 + i * .55
        cp = ease_out(prog(t, t0, .5)); ca = cp * main
        if ca <= 0: continue
        x = CX[i]; yy = CT + 40 * (1 - cp)
        d.rounded_rectangle((x, yy, x + CW, yy + CH), radius=24, fill=CARD + (int(255 * ca),))
        d.rounded_rectangle((x, yy, x + CW, yy + 10), radius=5, fill=GOLD + (int(255 * ca),))
        d.ellipse((x + 28, yy + 38, x + 88, yy + 98), fill=GOLD + (int(255 * ca),))
        text(L, (x + 58, yy + 69), str(i + 1), font('800', 34), NAVY, ca, anchor='mm')
        text(L, (x + 28, yy + 128), a, font('800', 40), WHITE, ca)
        text(L, (x + 28, yy + 180), b, font('500', 30), WHITE, ca * .85)
        # time counter pill
        tp = ease_back(prog(t, t0 + .35, .45))
        if tp > 0:
            pill(L, (x + 28, yy + 228), tl, font('800', 30), GOLD_L, NAVY, ca, pad=(20, 8), scale=clamp(tp, 0, 1.2))
    # snowflake toggle: winter extras
    if winter > 0 and main > 0:
        wa = winter * main
        yb = 880
        d.rounded_rectangle((120, yb, 1800, yb + 110), radius=55, fill=(255, 255, 255, int(235 * wa)))
        # toggle knob
        d.rounded_rectangle((150, yb + 25, 270, yb + 85), radius=30, fill=GOLD + (int(255 * wa),))
        kx = 180 + 60 * winter
        d.ellipse((kx - 24, yb + 31, kx + 24, yb + 79), fill=WHITE + (int(255 * wa),))
        import math as _m
        for k in range(3):
            ang = _m.pi / 3 * k + _m.pi / 2
            dx, dy = 15 * _m.cos(ang), 15 * _m.sin(ang)
            d.line((kx - dx, yb + 55 - dy, kx + dx, yb + 55 + dy), fill=NAVY + (int(255 * wa),), width=4)
        text(L, (300, yb + 55), 'Dec–Feb snow days:', font('800', 40), NAVY, wa, anchor='lm')
        text(L, (740, yb + 55), 'sledging · tubing · beginner skiing', font('500', 40), NAVY, wa, anchor='lm')
    # end card
    if endp > 0:
        e1 = ease_out(prog(t, 10.35, .5)); e2 = ease_out(prog(t, 10.6, .5)); e3 = ease_out(prog(t, 10.85, .5))
        text(L, (W / 2, 390), 'Hotel + cab + Kufri day', font('800', 104), WHITE, e1, dy=30 * (1 - e1), anchor='mm')
        text(L, (W / 2, 500), 'We plan it with your Shimla trip', font('500', 48), WHITE, e2 * .9, dy=20 * (1 - e2), anchor='mm')
        f = font('800', 52); w = f.getlength('Get Quote') + 120
        pill(L, (W / 2 - w / 2, 600), 'Get Quote', f, GOLD, NAVY, e3, pad=(60, 24), scale=0.9 + 0.1 * e3)
        text(L, (W / 2, 800), 'suzutravels.com/adventure', font('500', 36), GOLD_L, e3, anchor='mm')
    im.alpha_composite(L)
    return im.convert('RGB')

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'snap':
        for ts in sys.argv[2:]:
            render(float(ts)).save(f'/home/claude/work/snap-exp-{ts}.jpg', quality=85)
        sys.exit()
    w = Writer('/home/claude/work/out/explainer-master.mp4', W, H, FPS)
    for f in range(int(DUR * FPS)):
        w.add(render(f / FPS))
    w.close()
