"""Hub 'How booking works' explainer: 4 steps from the hub's own #booking list. 1920x1080, 30 fps, 10 s."""
import sys, math
from PIL import Image, ImageDraw
from sz import *

W, H, FPS, DUR = 1920, 1080, 30, 10.0
BG = Image.new('RGBA', (W, H), NAVY + (255,))
glow = Image.new('RGBA', (W, H), (0, 0, 0, 0)); gd = ImageDraw.Draw(glow)
for r in range(800, 0, -20):
    gd.ellipse((360 - r, 980 - r, 360 + r, 980 + r), fill=(22, 57, 92, int(3 + 0.9 * (800 - r) / 20)))
BG.alpha_composite(glow)
CARD = (22, 57, 92)
STEPS = [
    ('Tell us', ['Activity, place, date', 'and group size']),
    ('We check your date', ['Season, weather rules,', 'a registered local operator']),
    ('You get one quote', ['Activity alone, or with', 'hotel, cab and sightseeing']),
    ('Confirm and go', ['A small advance, and', 'our team looks after the day']),
]
XS = [300, 740, 1180, 1620]; LY = 430

def icon(d, i, cx, cy, a):
    c = NAVY + (a,)
    if i == 0:   # chat bubble
        d.rounded_rectangle((cx - 30, cy - 24, cx + 30, cy + 16), radius=12, outline=c, width=6)
        d.polygon([(cx - 14, cy + 14), (cx - 22, cy + 30), (cx - 2, cy + 14)], fill=c)
    elif i == 1:  # calendar
        d.rounded_rectangle((cx - 28, cy - 22, cx + 28, cy + 28), radius=8, outline=c, width=6)
        d.line((cx - 28, cy - 6, cx + 28, cy - 6), fill=c, width=6)
        for x in (cx - 14, cx + 14): d.line((x, cy - 32, x, cy - 16), fill=c, width=6)
        d.rectangle((cx + 4, cy + 6, cx + 16, cy + 18), fill=c)
    elif i == 2:  # quote sheet
        d.rounded_rectangle((cx - 24, cy - 30, cx + 24, cy + 30), radius=6, outline=c, width=6)
        for k in range(3): d.line((cx - 12, cy - 12 + k * 13, cx + 12, cy - 12 + k * 13), fill=c, width=5)
    else:         # check
        d.line([(cx - 24, cy + 2), (cx - 6, cy + 20), (cx + 26, cy - 18)], fill=c, width=9, joint='curve')

def render(t):
    im = BG.copy(); L = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    endp = prog(t, 8.2, .45); main = 1 - endp
    p = ease_out(prog(t, .1, .5))
    text(L, (120, 90), 'HOW IT WORKS', font('800', 36), GOLD, p * main, dy=-16 * (1 - p))
    p2 = ease_out(prog(t, .25, .5))
    text(L, (120, 138), 'How booking works', font('800', 96), WHITE, p2 * main, dy=30 * (1 - p2))
    # track
    ta = ease_out(prog(t, .6, .4)) * main
    d.line((XS[0], LY, XS[-1], LY), fill=(255, 255, 255, int(60 * ta)), width=6)
    lp = ease_in_out(prog(t, .9, 5.6))
    d.line((XS[0], LY, XS[0] + (XS[-1] - XS[0]) * lp, LY), fill=GOLD + (int(255 * ta),), width=8)
    for i, (h, ls) in enumerate(STEPS):
        t0 = .9 + i * (5.6 / 3) - (.25 if i else 0)
        np_ = ease_back(prog(t, t0, .5)); a = int(255 * clamp(np_) * main)
        if np_ <= 0: continue
        r = 62 * clamp(np_, 0, 1.15)
        x = XS[i]
        d.ellipse((x - r - 8, LY - r - 8, x + r + 8, LY + r + 8), fill=NAVY + (a,))
        d.ellipse((x - r, LY - r, x + r, LY + r), fill=GOLD + (a,))
        if np_ > .6: icon(d, i, x, LY, a)
        text(L, (x, LY - 100), f'STEP {i + 1}', font('800', 30), GOLD_L, clamp(np_) * main, anchor='ms')
        cp = ease_out(prog(t, t0 + .25, .5)); ca = cp * main
        if ca > 0:
            y0 = 560 + 30 * (1 - cp)
            d.rounded_rectangle((x - 212, y0, x + 212, y0 + 240), radius=22, fill=CARD + (int(255 * ca),))
            text(L, (x, y0 + 64), h, font('800', 36), WHITE, ca, anchor='ms')
            for k, ln in enumerate(ls):
                text(L, (x, y0 + 130 + k * 44), ln, font('500', 28), WHITE, ca * .85, anchor='ms')
    fa = ease_out(prog(t, 6.9, .5)) * main
    if fa > 0:
        text(L, (W / 2, 930), 'Send your plan on WhatsApp: today\'s rate within minutes', font('500', 38), GOLD_L, fa, anchor='ms')
    if endp > 0:
        e1 = ease_out(prog(t, 8.3, .5)); e2 = ease_out(prog(t, 8.55, .5)); e3 = ease_out(prog(t, 8.8, .5))
        text(L, (W / 2, 400), 'One quote.', font('800', 120), WHITE, e1, dy=30 * (1 - e1), anchor='mm')
        text(L, (W / 2, 510), 'Hotel + cab + adventure', font('500', 56), GOLD_L, e2, dy=20 * (1 - e2), anchor='mm')
        f = font('800', 52); w = f.getlength('Get Quote') + 120
        pill(L, (W / 2 - w / 2, 610), 'Get Quote', f, GOLD, NAVY, e3, pad=(60, 24), scale=0.9 + 0.1 * e3)
        text(L, (W / 2, 820), 'HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022', font('500', 32), (215, 224, 233), e3, anchor='mm')
    im.alpha_composite(L)
    return im.convert('RGB')

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'snap':
        for ts in sys.argv[2:]:
            render(float(ts)).save(f'/home/claude/work/snap-bk-{ts}.jpg', quality=85)
        sys.exit()
    w = Writer('/home/claude/work/out/booking-master.mp4', W, H, FPS)
    for f in range(int(DUR * FPS)):
        w.add(render(f / FPS))
    w.close()
