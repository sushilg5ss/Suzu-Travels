import sys
from PIL import Image, ImageDraw, ImageOps
from sz import *

W, H, FPS, DUR = 1920, 1080, 30, 12.0
PH = '/home/claude/work/ph/'
A = Photo(PH + 'px6617820.jpg', W, H, focus=(0.5, 0.76), zmax=1.08)
bm = Image.open(PH + 'px804572.jpg'); ImageOps.mirror(bm).save(PH + 'px804572-m.jpg', quality=95)
B = Photo(PH + 'px804572-m.jpg', W, H, focus=(0.42, 0.55), zmax=1.12)
C = Photo(PH + 'px15324807.jpg', W, H, focus=(0.5, 0.55), zmax=1.10)
from PIL import ImageFilter
_cs = Image.open(PH + 'px15324807.jpg').convert('RGB')
CARD = Photo(PH + 'px15324807.jpg', 600, 900, focus=(0.5, 0.55), zmax=1.08)
class CardScene:
    def frame(self, z):
        bg = C.frame(1.0).resize((W // 8, H // 8)).filter(ImageFilter.GaussianBlur(3)).resize((W, H), Image.BILINEAR)
        card = CARD.frame(z)
        m = Image.new('L', card.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, 600, 900), radius=28, fill=255)
        sh = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ImageDraw.Draw(sh).rounded_rectangle((250, 110, 850, 1010), radius=28, fill=(0, 0, 0, 120))
        bg = bg.convert('RGBA'); bg.alpha_composite(sh.filter(ImageFilter.GaussianBlur(24)))
        bg = bg.convert('RGB'); bg.paste(card, (240, 90), m)
        ImageDraw.Draw(bg).rounded_rectangle((240, 90, 840, 990), radius=28, outline=GOLD, width=6)
        return bg
C2 = CardScene()
D = Photo(PH + 'wp-snow-covered-himalayan-valley.webp', W, H, focus=(0.5, 0.5), zmax=1.08)

shade = grad_h(W, H, [(0, 0), (0.40, 0.0), (0.60, 0.55), (1, 0.84)])
shade_v = grad_v(W, H, [(0, .28), (.22, 0), (.78, 0), (1, .35)])
X0, XMAX = 1030, 1850

def fit(s, w, size):
    while size > 40:
        f = font('800', size)
        if f.getlength(s) <= w: return f
        size -= 4
    return font('800', size)

SCN = [  # (start, end, num, big, sub)
    (0.0, 3.6, '01 · SLIDE', 'Snow tubing', 'Easy fun for kids and grown-ups'),
    (3.2, 6.8, '02 · RIDE', 'Snow scooter', 'Zip across fresh snow'),
    (6.4, 9.2, '03 · LEARN', 'Skiing', 'Beginners ski with an instructor'),
    (8.8, 11.3, '04 · WHERE', 'Snow points', 'We check which one is open'),
]
ROUTE = [(1070, 985), (1300, 950), (1540, 905), (1775, 880)]
RLAB = [('Manali', '2,050 m'), ('Solang', '2,560 m'), ('Atal Tunnel', '3,060 m'), ('Sissu', '')]

def photo_at(t):
    if t < 3.6 or t >= 11.3:
        pass
    def a_img(tt): return A.frame(1.0 + 0.10 * ease_in_out(prog(tt, 0, 3.6)))
    def b_img(tt): return B.frame(1.10 - 0.09 * prog(tt, 3.2, 3.6))
    def c_img(tt): return C2.frame(1.0 + 0.09 * prog(tt, 6.4, 2.8))
    def d_img(tt): return D.frame(1.0 + 0.07 * prog(tt, 8.8, 3.2))
    if t < 3.2: return a_img(t)
    if t < 3.6: return Image.blend(a_img(t), b_img(t), ease_in_out(prog(t, 3.2, .4)))
    if t < 6.4: return b_img(t)
    if t < 6.8: return Image.blend(b_img(t), c_img(t), ease_in_out(prog(t, 6.4, .4)))
    if t < 8.8: return c_img(t)
    if t < 9.2: return Image.blend(c_img(t), d_img(t), ease_in_out(prog(t, 8.8, .4)))
    if t < 11.3: return d_img(t)
    return Image.blend(d_img(t), a_img(0), ease_in_out(prog(t, 11.3, .7)))

def render(t):
    im = photo_at(t).convert('RGBA')
    im.alpha_composite(shade); im.alpha_composite(shade_v)
    L = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    # persistent kicker
    ka = min(prog(t, 0.2, .4), 1 - prog(t, 11.0, .3))
    text(L, (X0, 150), 'SNOW · MANALI', font('800', 38), GOLD_L, ka, dy=-14 * (1 - ease_out(prog(t, .2, .4))), shadow=True)
    text(L, (X0, 204), 'by Suzu Travels', font('500', 30), WHITE, ka * .9, shadow=True)
    for i, (s, e, num, big, sub) in enumerate(SCN):
        if not (s <= t <= e): continue
        tin = s + (0.35 if i else 0.4)
        out = 1 - ease_out(prog(t, e - 0.45, .35)) if i < 3 else 1 - prog(t, 11.0, .3)
        top = 430 if i == 3 else 560
        p1 = ease_out(prog(t, tin, .5)); p2 = ease_out(prog(t, tin + .15, .5)); p3 = ease_out(prog(t, tin + .3, .5))
        text(L, (X0, top), num, font('800', 36), GOLD, p1 * out, dy=24 * (1 - p1), shadow=True)
        bf = fit(big, XMAX - X0, 132)
        text(L, (X0, top + 46), big, bf, WHITE, p2 * out, dy=40 * (1 - p2), shadow=True)
        # gold underline grows
        d = ImageDraw.Draw(L)
        uw = 150 * ease_out(prog(t, tin + .35, .6))
        if uw > 1 and out > 0:
            d.rounded_rectangle((X0, top + 206, X0 + uw, top + 216), radius=5, fill=GOLD + (int(255 * out),))
        text(L, (X0, top + 238), sub, font('500', 46), WHITE, p3 * out, dy=24 * (1 - p3), shadow=True)
    # route line in scene 4
    if 9.3 <= t < 11.3:
        rp = ease_in_out(prog(t, 9.5, 1.3)); ro = 1 - prog(t, 11.0, .3)
        pts = smooth(ROUTE, 16)
        seg = polyline_partial(pts, rp)
        d = ImageDraw.Draw(L)
        if len(seg) > 1:
            d.line(seg, fill=GOLD + (int(255 * ro),), width=7, joint='curve')
        for j, (pt, (nm, sub)) in enumerate(zip(ROUTE, RLAB)):
            dp = ease_back(prog(t, 9.5 + j * 0.4, .35)) if prog(t, 9.5 + j * .4, .35) > 0 else 0
            if dp <= 0: continue
            r = 13 * dp
            d.ellipse((pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r), fill=WHITE + (int(255 * ro),), outline=GOLD + (int(255 * ro),), width=5)
            la = clamp(dp) * ro
            anc = 'ms'
            text(L, (pt[0], pt[1] - 34), nm, font('800', 36), WHITE, la, anchor=anc, shadow=True)
            text(L, (pt[0], pt[1] + 52), sub, font('500', 30), GOLD_L, la, anchor=anc, shadow=True)
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
