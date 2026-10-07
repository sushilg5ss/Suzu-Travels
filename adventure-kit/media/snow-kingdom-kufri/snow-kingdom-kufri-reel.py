"""Snow Kingdom Kufri page reel: 1080x1920, 30 fps, 15 s. Photos: Pexels 20008914, 10936117, 6617714 (mirrored)."""
import sys
from PIL import Image, ImageDraw
from sz import *

W, H, FPS, DUR = 1080, 1920, 30, 15.0
PH = '/home/claude/work/ph/'
A = Photo(PH + 'px20008914.jpg', W, H, focus=(0.5, 0.45), zmax=1.10)
B = Photo(PH + 'px10936117.jpg', W, H, focus=(0.5, 0.55), zmax=1.10)
C = Photo(PH + 'px6617714-m.jpg', W, H, focus=(0.40, 0.6), zmax=1.08)
SNOW = Snow(W, H, 90, seed=9, rmin=2, rmax=6)
shade = grad_v(W, H, [(0, .55), (.25, 0), (.55, 0), (.78, .7), (1, .9)])

def fit(s, w, size, wt='800'):
    while size > 30 and font(wt, size).getlength(s) > w: size -= 2
    return font(wt, size)

SC = [  # start, end, image fn, kicker, line1, line2
    (0.0, 4.0, lambda t: A.frame(1.0 + .09 * prog(t, 0, 4.3)), 'SNOW KINGDOM · KUFRI', 'Real snow', 'in any month'),
    (3.7, 7.7, lambda t: B.frame(1.09 - .08 * prog(t, 3.7, 4.3)), 'WHAT YOU CAN DO', 'Sledges, tubes', '& snowballs'),
    (7.4, 11.4, lambda t: C.frame(1.0 + .07 * prog(t, 7.4, 4.3)), 'ABOUT 1 HOUR', 'Jacket, boots', '& gloves given'),
]

def endcard(t):
    im = Image.new('RGBA', (W, H), NAVY + (255,))
    L = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    SNOW.draw(L, t, alpha=.4)
    p = ease_out(prog(t, 11.6, .5)); p2 = ease_out(prog(t, 11.9, .5)); p3 = ease_back(prog(t, 12.3, .5))
    text(L, (W / 2, 560), 'SHIMLA + KUFRI', font('800', 46), GOLD, p, anchor='mm', dy=20 * (1 - p))
    text(L, (W / 2, 680), 'Snow day, hotel', font('800', 92), WHITE, p2, anchor='mm', dy=30 * (1 - p2))
    text(L, (W / 2, 790), '& cab in one plan', font('800', 92), WHITE, p2, anchor='mm', dy=30 * (1 - p2))
    d = ImageDraw.Draw(L)
    uw = 260 * ease_out(prog(t, 12.1, .6))
    if uw > 1: d.rounded_rectangle((W / 2 - uw, 870, W / 2 + uw, 882), radius=6, fill=GOLD + (255,))
    if p3 > 0:
        f = font('800', 64); w = f.getlength('Get Quote') + 80
        pill(L, (W / 2 - w / 2, 960), 'Get Quote', f, GOLD, NAVY, 1, pad=(40, 24), scale=p3)
    p4 = ease_out(prog(t, 12.6, .5))
    s = 'suzutravels.com/adventure/snow-kingdom-kufri'
    text(L, (W / 2, 1180), s, fit(s, W - 120, 44), WHITE, p4, anchor='mm')
    text(L, (W / 2, 1400), 'HP Tourism registered travel agent', font('500', 38), (210, 222, 235), p4, anchor='mm')
    text(L, (W / 2, 1456), 'Reg. No. DTO-MND-11-243/2022', font('500', 38), (210, 222, 235), p4, anchor='mm')
    im.alpha_composite(L)
    return im

def render(t):
    if t >= 11.4:
        im = endcard(t)
        if t < 11.8:  # crossfade from last photo scene
            prev = render_scene(2, t)
            im = Image.blend(prev, im, ease_in_out(prog(t, 11.4, .4)))
        return im.convert('RGB')
    for i in (2, 1, 0):
        s, e = SC[i][0], SC[i][1]
        if t >= s:
            im = render_scene(i, t)
            if i > 0 and t < s + .3:
                im = Image.blend(render_scene(i - 1, t), im, ease_in_out(prog(t, s, .3)))
            return im.convert('RGB')

def render_scene(i, t):
    s, e, fn, kick, l1, l2 = SC[i]
    im = fn(t).convert('RGBA'); im.alpha_composite(shade)
    L = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    SNOW.draw(L, t, alpha=.85)
    tin = s + (.15 if i else 0)
    p1 = 1 if i == 0 and t < .01 else ease_out(prog(t, tin, .45))
    p2 = ease_out(prog(t, tin + .15, .45)); p3 = ease_out(prog(t, tin + .3, .45))
    if i == 0: p1 = p2 = p3 = 1.0  # first frame is a readable poster
    out = 1 - prog(t, e - .35, .3)
    text(L, (90, 1380), kick, font('800', 44), GOLD_L, p1 * out, dy=20 * (1 - p1), shadow=True)
    text(L, (90, 1440), l1, fit(l1, W - 180, 120), WHITE, p2 * out, dy=30 * (1 - p2), shadow=True)
    text(L, (90, 1580), l2, fit(l2, W - 180, 120), WHITE, p3 * out, dy=30 * (1 - p3), shadow=True)
    d = ImageDraw.Draw(L)
    uw = 220 * (1 if i == 0 else ease_out(prog(t, tin + .4, .6)))
    d.rounded_rectangle((90, 1740, 90 + uw, 1754), radius=7, fill=GOLD + (int(255 * out),))
    text(L, (W / 2, 120), 'suzutravels.com', font('500', 34), WHITE, .85, anchor='mm', shadow=True)
    im.alpha_composite(L)
    return im

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'snap':
        for ts in sys.argv[2:]:
            render(float(ts)).save(f'/home/claude/work/out/snap-reel-{ts}.jpg', quality=85)
        sys.exit()
    w = Writer('/home/claude/work/out/reel-master.mp4', W, H, FPS)
    for f in range(int(DUR * FPS)):
        w.add(render(f / FPS))
    w.close()
