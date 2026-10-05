"""Atal Tunnel & Sissu snow trip reel: 1080x1920, 30 fps, 15 s. Road tunnel after snowfall -> snowy valley with river -> frozen waterfall -> Get Quote end card. Facts from the brief only; generic photos, no place label on a photo; no prices."""
import sys
from PIL import Image, ImageDraw
from sz import *

W, H, FPS, DUR = 1080, 1920, 30, 15.0
PH = '/home/claude/work/ph/'
P = [Photo(PH + 'px15295177.jpg', W, 1180, focus=(0.5, 0.55), zmax=1.10),
     Photo(PH + 'wp_Frozen-river-Spiti-2-scaled.webp', W, 1180, focus=(0.42, 0.5), zmax=1.10),
     Photo(PH + 'px12548491.jpg', W, 1180, focus=(0.35, 0.5), zmax=1.10)]
MASK1 = Image.new('L', (W, 1180), 255)
_md = ImageDraw.Draw(MASK1)
for _y in range(880, 1180): _md.line((0, _y, W, _y), fill=int(255 * (1180 - _y) / 300))
SC = [(0.0, 3.8), (3.6, 7.4), (7.2, 10.8)]
CAP = [('01 · THE TUNNEL', '9.02 KM', 'Under the pass, Manali to Lahaul', 'No Rohtang permit'),
       ('02 · SNOW', 'SNOW DAY', 'About 40 km from Manali', 'First snow Oct–Nov'),
       ('03 · AFTER SNOWFALL', '4x4 ONLY', 'Chains beyond Solang Nala', 'Checked the evening before')]
shade = grad_v(W, H, [(0, .78), (.22, .10), (.40, 0), (.55, .55), (.78, .92), (1, .96)])
snow = Snow(W, H, 70, seed=3, rmin=3, rmax=7)
RIDGE = [(0, 118), (120, 96), (190, 108), (300, 52), (372, 84), (470, 20), (560, 76), (640, 58), (740, 104), (830, 42), (920, 80), (1000, 64), (1080, 92)]
RIDGE = [(x, y + 930) for x, y in RIDGE]
end_bg = Image.new('RGBA', (W, H), NAVY + (255,)); gd = ImageDraw.Draw(end_bg)
for r in range(1100, 0, -25):
    gd.ellipse((864 - r, 190 - r * .6, 864 + r, 190 + r * .6), fill=(22, 57, 92, int(2 + 1.2 * (1100 - r) / 25)))
from PIL import ImageFilter
end_bg = end_bg.filter(ImageFilter.GaussianBlur(60))

def fit(s, w, size, wt='800'):
    while size > 30 and font(wt, size).getlength(s) > w: size -= 4
    return font(wt, size)

def photo(t):
    def f(i, tt):
        s, e = SC[i]; p = prog(tt, s, e - s)
        if True:
            bg = Image.new('RGB', (W, H), NAVY); bg.paste(P[i].frame(1.1 - 0.09 * p if i == 1 else 1.0 + 0.09 * p), (0, 0), MASK1); return bg
        return P[i].frame(1.0 + 0.1 * p)
    if t < 3.6: return f(0, t)
    if t < 4.1: return Image.blend(f(0, t), f(1, t), ease_in_out(prog(t, 3.6, .5)))
    if t < 7.2: return f(1, t)
    if t < 7.7: return Image.blend(f(1, t), f(2, t), ease_in_out(prog(t, 7.2, .5)))
    return f(2, t)

def render(t):
    if t < 10.8 or t < 11.2:
        im = photo(min(t, 10.8)).convert('RGBA'); im.alpha_composite(shade)
    L = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    if t < 11.2:
        snow.draw(L, t, alpha=.8)
        bp = ease_out(prog(t, .1, .5)) * (1 - prog(t, 10.4, .3))
        text(L, (72, 236), 'ATAL TUNNEL · SISSU', font('800', 38), GOLD_L, bp, dy=-20 * (1 - bp), shadow=True)
        text(L, (72, 290), 'by Suzu Travels', font('500', 32), WHITE, bp * .9, shadow=True)
        # ridge draws each scene
        for s, e in SC:
            if s + .1 <= t < e:
                rp = ease_in_out(prog(t, s + .1, 1.4)); ro = 1 - prog(t, e - .35, .3)
                seg = polyline_partial(RIDGE, rp)
                if len(seg) > 1: d.line(seg, fill=GOLD + (int(255 * ro),), width=7, joint='curve')
        for i, ((s, e), (num, big, sub, chip)) in enumerate(zip(SC, CAP)):
            ts = s + (.2 if i == 0 else .4)
            if not (s <= t < e): continue
            out = 1 - prog(t, e - .45, .35)
            p1 = ease_out(prog(t, ts, .5)); p2 = ease_out(prog(t, ts + .1, .55)); p3 = ease_out(prog(t, ts + .3, .5)); p4 = ease_back(prog(t, ts + .45, .5))
            text(L, (72, 1080), num, font('800', 38), GOLD, p1 * out, dy=30 * (1 - p1), shadow=True)
            text(L, (72, 1120), big, fit(big, 936, 220), WHITE, p2 * out, dy=60 * (1 - p2), shadow=True)
            text(L, (72, 1380), sub, fit(sub, 936, 58, '500'), WHITE, p3 * out, dy=30 * (1 - p3), shadow=True)
            if p4 > 0:
                pill(L, (72, 1480), chip, font('800', 44), GOLD, NAVY, clamp(p4) * out, pad=(34, 18), scale=clamp(.85 + .15 * p4, 0, 1.1))
        im.alpha_composite(L)
    if t >= 10.8:
        a = ease_out(prog(t, 10.8, .4))
        E = end_bg.copy(); EL = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ed = ImageDraw.Draw(EL)
        snow.draw(EL, t, alpha=.35)
        def ea(k): return ease_out(prog(t, 10.95 + k * .1, .45))
        text(EL, (72, 400), 'SISSU SNOW DAY, SORTED', font('800', 38), GOLD, ea(0), dy=30 * (1 - ea(0)))
        for j, ln in enumerate(['Hotel + cab +', 'snow day,', 'one quote.']):
            text(EL, (72, 470 + j * 124), ln, font('800', 118), GOLD_L if j == 1 else WHITE, ea(1 + j * .5), dy=30 * (1 - ea(1 + j * .5)))
        for j, ln in enumerate(['Road + snow checked', 'the evening before.']):
            text(EL, (72, 880 + j * 64), ln, font('500', 50), (240, 244, 248), ea(3), dy=30 * (1 - ea(3)))
        bp = ease_back(prog(t, 11.5, .5))
        pulse = 1 + .05 * math.sin(max(0, t - 12.6) * 2 * math.pi / 1.2) if t > 12.6 else 1
        if bp > 0:
            pill(EL, (72, 1060), 'Get Quote', font('800', 64), GOLD, NAVY, clamp(bp), pad=(62, 30), scale=clamp(bp, 0, 1.1) * pulse)
        text(EL, (72, 1260), 'suzutravels.com', font('800', 50), WHITE, ea(5))
        text(EL, (72, 1322), '/adventure/atal-tunnel-sissu-snow-trip', fit('/adventure/atal-tunnel-sissu-snow-trip', 936, 42, '500'), WHITE, ea(5))
        text(EL, (72, 1450), 'HP Tourism registered travel agent', font('500', 34), (215, 224, 233), ea(6))
        text(EL, (72, 1496), 'Reg. No. DTO-MND-11-243/2022', font('500', 34), (215, 224, 233), ea(6))
        E.alpha_composite(EL)
        im = Image.blend(im.convert('RGB'), E.convert('RGB'), a) if t < 11.2 else E
    return im.convert('RGB')

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'snap':
        for ts in sys.argv[2:]:
            render(float(ts)).save(f'/home/claude/work/snap-reel-{ts}.jpg', quality=85)
        sys.exit()
    w = Writer('/home/claude/work/out/reel-master.mp4', W, H, FPS)
    for f in range(int(DUR * FPS)):
        w.add(render(f / FPS))
    w.close()
