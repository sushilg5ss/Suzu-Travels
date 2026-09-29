import sys
from PIL import Image, ImageDraw
from sz import *

W, H, FPS, DUR = 1920, 1080, 30, 12.0
BG = Image.new('RGBA', (W, H), NAVY + (255,))
g = grad_v(W, H, [(0, 0), (1, 0)])
# soft radial-ish glow top right
glow = Image.new('RGBA', (W, H), (0, 0, 0, 0)); gd = ImageDraw.Draw(glow)
for r in range(700, 0, -20):
    gd.ellipse((1500 - r, 150 - r, 1500 + r, 150 + r), fill=(22, 57, 92, int(3 + 0.9 * (700 - r) / 20)))
BG.alpha_composite(glow)
snow = Snow(W, H, 90, seed=11, rmin=2, rmax=5)

BASE = 900; SCALE = 560 / 4000
BARS = [  # name, alt, sub, x, snow-step (1 = Oct–Nov, 2 = late Dec–Feb, 0 = none claimed)
    ('Manali', 2050, '', 260, 0),
    ('Solang', 2560, '14 km from Manali', 540, 2),
    ('Atal Tunnel', 3060, 'Sissu 5 km past', 820, 1),
    ('Rohtang', 3978, 'online permit', 1100, 1),
]
BW = 170
STEPS = [
    (3.6, 6.2, 'OCT – NOV', ['First snow up high:', 'Sissu side & Rohtang']),
    (6.2, 8.8, 'LATE DEC – FEB', ['Best snow time at', 'Solang Valley']),
    (8.8, 10.4, 'GOOD TO KNOW', ['Atal Tunnel needs', 'no Rohtang permit']),
]

def render(t):
    im = BG.copy(); L = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    endp = prog(t, 10.3, .4)
    snow.draw(L, t, alpha=0.35)
    main = 1 - endp
    # title
    p = ease_out(prog(t, .1, .5))
    text(L, (120, 90), 'SNOW · MANALI', font('800', 36), GOLD, p * main, dy=-16 * (1 - p))
    p2 = ease_out(prog(t, .25, .5))
    text(L, (120, 138), "Where's the snow?", font('800', 96), WHITE, p2 * main, dy=30 * (1 - p2))
    # baseline
    bl = ease_out(prog(t, .5, .6))
    d.line((180, BASE, 180 + 1060 * bl, BASE), fill=(255, 255, 255, int(90 * main)), width=3)
    step = 0
    for s0, s1, *_ in STEPS:
        if t >= s0: step += 1
    for i, (nm, alt, sub, x, sstep) in enumerate(BARS):
        gp = ease_out(prog(t, 0.9 + i * .25, 1.1))
        h = alt * SCALE * gp
        a = int(255 * main)
        if h > 1:
            d.rounded_rectangle((x - BW / 2, BASE - h, x + BW / 2, BASE), radius=14, fill=(22, 57, 92, a))
            # snow cap when its season step is active
            lit = sstep and step >= sstep
            cp = ease_back(prog(t, STEPS[sstep - 1][0] + .2 + .15 * (i % 2), .5)) if sstep else 0
            if lit and cp > 0:
                ch = 46 * clamp(cp, 0, 1.2)
                d.rounded_rectangle((x - BW / 2, BASE - h, x + BW / 2, BASE - h + ch), radius=14, fill=(255, 255, 255, a))
                d.rectangle((x - BW / 2, BASE - h + ch - 14, x + BW / 2, BASE - h + ch), fill=(255, 255, 255, a))
            else:
                d.rounded_rectangle((x - BW / 2, BASE - h, x + BW / 2, BASE - h + 10), radius=5, fill=GOLD + (a,))
            val = alt if gp >= 1 else int(round(alt * gp / 10) * 10)
            text(L, (x, BASE - h - 24), f'{val:,} m', font('800', 40), GOLD_L if not (sstep and step >= sstep) else WHITE, main * clamp(gp * 3), anchor='ms')
        lp = ease_out(prog(t, 1.0 + i * .25, .5))
        text(L, (x, BASE + 52), nm, font('800', 38), WHITE, lp * main, anchor='ms')
        if sub:
            text(L, (x, BASE + 94), sub, font('500', 28), (200, 212, 225), lp * main, anchor='ms')
    # right panel with the season steps
    for s0, s1, head, lines in STEPS:
        if not (s0 <= t <= s1 + .01): continue
        pin = ease_out(prog(t, s0, .45)); pout = 1 - prog(t, s1 - .3, .3) if s1 < 10.4 else 1 - endp
        a = pin * pout
        x0 = 1330 + 40 * (1 - pin)
        d.rounded_rectangle((x0, 330, x0 + 540, 640), radius=28, fill=(255, 255, 255, int(18 * a)), outline=GOLD + (int(255 * a),), width=3)
        pill(L, (x0 + 40, 370), head, font('800', 34), GOLD, NAVY, a)
        for j, ln in enumerate(lines):
            text(L, (x0 + 40, 470 + j * 62), ln, font('800' if j else '500', 42), WHITE, a)
    # end card
    if endp > 0:
        e1 = ease_out(prog(t, 10.4, .5)); e2 = ease_out(prog(t, 10.6, .5)); e3 = ease_back(prog(t, 10.8, .5))
        text(L, (W / 2, 400), 'WE CHECK THE ROAD & SNOW', font('800', 40), GOLD, e1, anchor='ms', dy=20 * (1 - e1))
        text(L, (W / 2, 520), 'the evening before your snow day', font('800', 78), WHITE, e2, anchor='ms', dy=30 * (1 - e2))
        if e3 > 0:
            f = font('800', 56); w = f.getlength('Get Quote') + 120
            pill(L, (W / 2 - w / 2, 610), 'Get Quote', f, GOLD, NAVY, clamp(e3), pad=(60, 26), scale=clamp(e3, 0, 1.2))
        text(L, (W / 2, 850), 'HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022', font('500', 32), (220, 228, 236), e2, anchor='ms')
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
