"""Hub safety band motion graphic: 'What we check before we book it'. 1600x900, 30 fps, 10 s, seamless-ish.
Text = the hub's own #safety checks (registered operators, paragliding 12+ yrs / 30 kg+, notified sites,
monsoon stop 15 Jul-15 Sep in Kullu & Kangra, bungee 12-55 yrs / 40-110 kg, weather calls)."""
import sys, math
from PIL import Image, ImageDraw
from sz import *

W, H, FPS, DUR = 1600, 900, 30, 10.0
BG = Image.new('RGBA', (W, H), NAVY + (255,))
glow = Image.new('RGBA', (W, H), (0, 0, 0, 0)); gd = ImageDraw.Draw(glow)
for r in range(700, 0, -20):
    gd.ellipse((1300 - r, 120 - r, 1300 + r, 120 + r), fill=(22, 57, 92, int(3 + 0.9 * (700 - r) / 20)))
BG.alpha_composite(glow)
CARD = (22, 57, 92); RED = (214, 69, 65)

def shield(d, cx, cy, s, a, p):
    """Gold shield outline with a tick drawn by p."""
    pts = [(cx, cy - s), (cx + s * .85, cy - s * .62), (cx + s * .78, cy + s * .2), (cx, cy + s), (cx - s * .78, cy + s * .2), (cx - s * .85, cy - s * .62), (cx, cy - s)]
    d.line(pts, fill=GOLD + (int(255 * a),), width=9, joint='curve')
    tick = [(cx - s * .38, cy + s * .02), (cx - s * .08, cy + s * .32), (cx + s * .42, cy - s * .3)]
    seg = polyline_partial(tick, p)
    if len(seg) > 1: d.line(seg, fill=GOLD_L + (int(255 * a),), width=12, joint='curve')

CARDS = [  # big, small, icon kind
    ('12+ yrs · 30 kg+', 'Paragliding: registered pilots, notified sites only', 'para'),
    ('15 Jul – 15 Sep', 'No paragliding, rafting or water sports in Kullu & Kangra', 'stop'),
    ('12–55 yrs · 40–110 kg', 'Bungee limits; ziplines with registered operators', 'bungee'),
    ('Weather first', 'Flights, rafting and snow rides stop when it turns', 'cloud'),
]
POS = [(80, 262), (820, 262), (80, 522), (820, 522)]; CW, CH = 700, 230

def icon(d, kind, x, y, a):
    c = GOLD + (int(255 * a),)
    if kind == 'para':
        d.arc((x - 40, y - 34, x + 40, y + 26), 200, 340, fill=c, width=8)
        for dx in (-30, 0, 30): d.line((x + dx, y - 22 + abs(dx) * .3, x, y + 30), fill=c, width=3)
        d.ellipse((x - 7, y + 26, x + 7, y + 40), fill=c)
    elif kind == 'stop':
        d.ellipse((x - 36, y - 36, x + 36, y + 36), outline=RED + (int(255 * a),), width=8)
        d.line((x - 24, y + 24, x + 24, y - 24), fill=RED + (int(255 * a),), width=8)
    elif kind == 'bungee':
        d.line((x - 36, y - 34, x + 36, y - 34), fill=c, width=8)
        pts = [(x, y - 34)] + [(x + (12 if k % 2 else -12), y - 26 + k * 9) for k in range(6)] + [(x, y + 30)]
        d.line(pts, fill=c, width=5); d.ellipse((x - 9, y + 26, x + 9, y + 44), fill=c)
    else:
        d.ellipse((x - 36, y - 10, x - 2, y + 22), fill=c); d.ellipse((x - 16, y - 30, x + 26, y + 12), fill=c)
        d.ellipse((x + 6, y - 8, x + 40, y + 22), fill=c); d.rectangle((x - 18, y + 4, x + 22, y + 22), fill=c)

def render(t):
    im = BG.copy(); L = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    out = 1 - ease_in_out(prog(t, 9.3, .6))  # fade to bare navy so the loop restarts cleanly
    p = ease_out(prog(t, .1, .5)) * out
    shield(d, 140, 145, 62, p, ease_out(prog(t, .5, .6)))
    text(L, (240, 90), 'SAFETY FIRST', font('800', 34), GOLD, p, dy=-14 * (1 - p))
    p2 = ease_out(prog(t, .25, .5)) * out
    text(L, (240, 132), 'What we check before we book', font('800', 66), WHITE, p2, dy=24 * (1 - p2))
    for i, ((big, small, kind), (x, y)) in enumerate(zip(CARDS, POS)):
        t0 = 1.1 + i * .9
        cp = ease_out(prog(t, t0, .5)); ca = cp * out
        if ca <= 0: continue
        yy = y + 30 * (1 - cp)
        d.rounded_rectangle((x, yy, x + CW, yy + CH), radius=24, fill=CARD + (int(255 * ca),))
        d.rounded_rectangle((x, yy, x + 10, yy + CH), radius=5, fill=(RED if kind == 'stop' else GOLD) + (int(255 * ca),))
        icon(d, kind, x + 80, yy + 92, ca)
        bp = ease_back(prog(t, t0 + .2, .5))
        fb = font('800', 54)
        while fb.getlength(big) > CW - 175: fb = font('800', fb.size - 2)
        text(L, (x + 150, yy + 52), big, fb, GOLD_L if kind != 'stop' else (255, 214, 210), ca, dy=16 * (1 - clamp(bp)))
        # wrap small text in two lines max
        f = font('500', 30); words = small.split(); lines = ['']
        for w_ in words:
            trial = (lines[-1] + ' ' + w_).strip()
            if f.getlength(trial) <= CW - 180: lines[-1] = trial
            else: lines.append(w_)
        sa = ease_out(prog(t, t0 + .35, .45)) * out
        for k, ln in enumerate(lines[:2]):
            text(L, (x + 150, yy + 140 + k * 40), ln, f, WHITE, sa * .92)
    # registered-operators ribbon
    ra = ease_out(prog(t, 5.0, .5)) * out
    if ra > 0:
        f = font('800', 32); s = 'Registered local operators only  ·  permits arranged with your cab'
        w = f.getlength(s) + 80
        d.rounded_rectangle(((W - w) / 2, 800 - 6, (W + w) / 2, 800 + 46), radius=26, fill=GOLD + (int(255 * ra),))
        text(L, (W / 2, 800 + 20), s, f, NAVY, ra, anchor='mm')
    im.alpha_composite(L)
    return im.convert('RGB')

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'snap':
        for ts in sys.argv[2:]:
            render(float(ts)).save(f'/home/claude/work/snap-safe-{ts}.jpg', quality=85)
        sys.exit()
    w = Writer('/home/claude/work/out/safety-master.mp4', W, H, FPS)
    for f in range(int(DUR * FPS)):
        w.add(render(f / FPS))
    w.close()
