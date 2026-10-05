"""Igloo stay (Sethan) explainer 'Your igloo night': 1600x900, 30 fps, 12 s. Suzu brand.
Map Manali ~2,050 m -> Prini -> hairpin road -> Sethan ~2,700 m (about 12 km, 1-2 hrs in winter, 4x4 after snowfall),
outside-at-night counter down to -15 C, 6-step timeline (arrive around lunch -> snow play -> bonfire + dinner -> night in
the igloo -> breakfast -> back to Manali), season bar (built from Dec when snow allows; stays mid-Jan to mid-Mar),
end card Get Quote + HP Tourism reg. no. Facts from the brief only; no prices."""
import sys
from PIL import Image, ImageDraw, ImageFilter
from sz import *

W, H, FPS, DUR = 1600, 900, 30, 12.0
LINE = (36, 66, 96)
bg = Image.new('RGBA', (W, H), NAVY + (255,)); _g = ImageDraw.Draw(bg)
for r in range(900, 0, -30):
    _g.ellipse((1250 - r, 120 - r * .7, 1250 + r, 120 + r * .7), fill=(22, 57, 92, int(2 + (900 - r) / 30)))
bg = bg.filter(ImageFilter.GaussianBlur(50))
SNOW = Snow(W, H, 60, seed=11, rmin=2, rmax=4)
XM = 110
def fit(s, w, size, wt='800'):
    while size > 20 and font(wt, size).getlength(s) > w: size -= 2
    return font(wt, size)

# route: flat-ish Manali -> Prini, then hairpins climbing to Sethan
P_M, P_P = (110, 330), (560, 318)
HAIR = [P_P]
x, y = 560, 318
for k in range(8):
    x += 70; y -= 12
    HAIR.append((x, y + (14 if k % 2 == 0 else -14)))
P_S = (1210, 210)
HAIR.append(P_S)
ROUTE = [P_M, (330, 326), P_P] + HAIR[1:]

STEPS = ['Arrive around lunch', 'Snow play', 'Bonfire + dinner', 'Night in the igloo', 'Breakfast', 'Back to Manali']

def render(t):
    im = bg.copy(); L = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    SNOW.draw(L, t, alpha=.35)
    endp = ease_out(prog(t, 10.2, .5)); mA = 1 - endp
    k = ease_out(prog(t, .1, .5)) * mA
    text(L, (XM, 60), 'YOUR IGLOO NIGHT', font('800', 34), GOLD, k, dy=20 * (1 - k))
    k2 = ease_out(prog(t, .3, .5)) * mA
    text(L, (XM, 102), 'Manali to Sethan, about 12 km', font('800', 60), WHITE, k2, dy=24 * (1 - k2))
    # route
    p = ease_in_out(prog(t, .8, 2.6))
    pa = int(255 * mA)
    pts = polyline_partial(ROUTE, p)
    d.line(ROUTE, fill=LINE + (pa,), width=7, joint='curve')
    if len(pts) > 1: d.line(pts, fill=GOLD + (pa,), width=7, joint='curve')
    for (x, y), lab, sub, at, anc in ((P_M, 'Manali', '~2,050 m', 0, 'la'), (P_P, 'Prini', 'road turns up', .36, 'ma'), (P_S, 'Sethan', '~2,700 m', .97, 'ma')):
        q = (clamp((p - at) / .05) if at else clamp((t - .8) / .3)) * mA
        if q <= 0: continue
        r = 13 * ease_back(clamp(q), 1.3)
        d.ellipse((x - r, y - r, x + r, y + r), fill=WHITE + (int(255 * q),), outline=GOLD + (int(255 * q),), width=4)
        text(L, (x, y + 28), lab, font('800', 30), WHITE, q, anchor=anc)
        text(L, (x, y + 66), sub, font('500', 24), (200, 214, 228), q, anchor=anc)
    ha = clamp((p - .55) / .1) * mA
    text(L, (880, 360), 'hairpin road · 4x4 after snowfall', font('800', 24), GOLD_L, ha, anchor='ma')
    text(L, (880, 394), '1–2 hrs from Manali in winter', font('500', 24), WHITE, ha * .9, anchor='ma')
    # temperature chip near Sethan
    ta = ease_out(prog(t, 3.2, .5)) * mA
    if ta > 0:
        tp = ease_in_out(prog(t, 3.3, 3.0)); temp = round(-15 * tp)
        d.rounded_rectangle((1290, 150, 1490, 290), radius=18, fill=(8, 22, 38, int(235 * ta)), outline=GOLD + (int(255 * ta),), width=3)
        text(L, (1390, 172), 'OUTSIDE AT NIGHT', font('800', 18), WHITE, ta, anchor='ma')
        text(L, (1390, 238), f'{temp} °C', font('800', 56), GOLD_L, ta, anchor='mm')
        text(L, (1390, 300), 'or lower', font('500', 20), (200, 214, 228), ta * clamp((tp - .9) / .1), anchor='ma')
    # timeline
    la = ease_out(prog(t, 3.8, .5)) * mA
    if la > 0:
        text(L, (XM, 470), 'ONE NIGHT, START TO FINISH', font('800', 26), GOLD_L, la)
        n = len(STEPS); x0, x1, yy = XM + 110, 1380, 560
        d.line((x0, yy, x1, yy), fill=LINE + (int(255 * la),), width=6)
        for i, lab in enumerate(STEPS):
            cx = x0 + (x1 - x0) * i / (n - 1)
            si = ease_back(prog(t, 4.1 + i * .55, .45), 1.4)
            if i > 0:
                fp = clamp(prog(t, 4.1 + (i - 1) * .55, .55))
                px = x0 + (x1 - x0) * (i - 1) / (n - 1)
                d.line((px, yy, px + (cx - px) * fp, yy), fill=GOLD + (int(255 * mA),), width=6)
            if si <= 0: continue
            r = 24 * clamp(si, 0, 1.2)
            night = (i == 3)
            d.ellipse((cx - r, yy - r, cx + r, yy + r), fill=(GOLD if not night else GOLD_L) + (int(255 * mA),))
            text(L, (cx, yy), str(i + 1), font('800', 26), NAVY, clamp(si) * mA, anchor='mm')
            text(L, (cx, yy + 44), lab, fit(lab, 230, 26, '800'), WHITE, clamp(si) * mA, anchor='ma')
    # season bar
    sa = ease_out(prog(t, 7.6, .5)) * mA
    if sa > 0:
        text(L, (XM, 670), 'WHEN', font('800', 26), GOLD_L, sa)
        months = ['DEC', 'JAN', 'FEB', 'MAR']
        x0, x1, yy = XM, 1490, 712
        cw = (x1 - x0) / 4
        d.rounded_rectangle((x0, yy, x1, yy + 64), radius=14, fill=(255, 255, 255, int(22 * sa)), outline=(255, 255, 255, int(120 * sa)), width=2)
        bp = ease_in_out(prog(t, 8.0, .9))
        gx0 = x0 + cw * 1.5; gx1 = x0 + cw * 3.5
        if bp > 0:
            d.rounded_rectangle((gx0, yy, gx0 + (gx1 - gx0) * bp, yy + 64), radius=14, fill=GOLD + (int(255 * sa),))
        for i, m in enumerate(months):
            cx = x0 + cw * (i + .5)
            d.line((x0 + cw * i, yy + 64, x0 + cw * i, yy + 74), fill=(255, 255, 255, int(120 * sa)), width=2)
            text(L, (cx, yy + 80), m, font('800', 24), WHITE, sa, anchor='ma')
        la2 = ease_out(prog(t, 8.7, .4)) * mA
        text(L, (x0 + cw * .5, yy + 22), 'Igloos built when snow allows', font('500', 22), WHITE, la2, anchor='ma')
        text(L, ((gx0 + gx1) / 2, yy + 20), 'Stays mid-Jan to mid-Mar, snow-dependent', font('800', 24), NAVY, la2, anchor='ma')
    # end card
    if endp > 0:
        def ea(k): return ease_out(prog(t, 10.4 + k * .15, .45))
        text(L, (W / 2, 250), 'IGLOO STAY · SETHAN', font('800', 34), GOLD, ea(0), anchor='mm', dy=20 * (1 - ea(0)))
        text(L, (W / 2, 340), 'Igloo + hotel + cab, one plan', font('800', 72), WHITE, ea(1), anchor='mm', dy=24 * (1 - ea(1)))
        text(L, (W / 2, 425), 'Dates depend on snow; we check before booking', font('500', 34), (220, 230, 240), ea(2), anchor='mm')
        bp = ease_back(prog(t, 10.9, .5))
        if bp > 0:
            f = font('800', 52); w = f.getlength('Get Quote') + 120
            pill(L, (W / 2 - w / 2, 500), 'Get Quote', f, GOLD, NAVY, clamp(bp), pad=(60, 26), scale=clamp(bp, 0, 1.1))
        text(L, (W / 2, 700), 'HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022', font('500', 26), (200, 214, 228), ea(4), anchor='mm')
    im.alpha_composite(L)
    return im.convert('RGB')

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'snap':
        for ts in sys.argv[2:]:
            render(float(ts)).save(f'/home/claude/work/snap-iexp-{ts}.jpg', quality=85)
        sys.exit()
    w = Writer('/home/claude/work/out2/explainer-master.mp4', W, H, FPS)
    for f in range(int(DUR * FPS)):
        w.add(render(f / FPS))
    w.close()
