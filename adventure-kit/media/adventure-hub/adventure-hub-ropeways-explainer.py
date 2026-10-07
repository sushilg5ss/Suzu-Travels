"""Adventure hub 'Ropeways & Parks' head motion graphic: 1920x1080, 30 fps, 11 s.
Facts only from the live hub #ropeways cards (no new claims)."""
import sys
from PIL import Image, ImageDraw
from sz import *

W, H, FPS, DUR = 1920, 1080, 30, 11.0
RW = [  # name, where, line
    ('Timber Trail', 'Parwanoo', 'First stop on the Shimla road'),
    ('Jakhu ropeway', 'Shimla', "Up to Shimla's highest point"),
    ('Naina Devi ropeway', 'Bilaspur', 'The easy way to the hilltop temple'),
    ('Dharamshala Skyway', 'to McLeodganj', 'About 1.8 km in ~5 minutes'),
    ('Solang ropeway', 'Manali', 'Up to the snow slopes'),
]
LBLUE = (170, 200, 230)

def gondola(d, x, y, a, s=1.0):
    A = int(255 * a)
    d.line((x, y, x, y + 34 * s), fill=WHITE + (A,), width=4)
    d.rounded_rectangle((x - 30 * s, y + 34 * s, x + 30 * s, y + 92 * s), radius=12 * s, fill=GOLD + (A,))
    d.rounded_rectangle((x - 20 * s, y + 44 * s, x + 20 * s, y + 66 * s), radius=6 * s, fill=NAVY + (A,))

def render(t):
    im = Image.new('RGBA', (W, H), NAVY + (255,))
    L = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    # hills silhouette (static)
    d.polygon([(0, 420), (260, 300), (520, 380), (820, 240), (1100, 360), (1400, 220), (1700, 330), (1920, 270), (1920, 470), (0, 470)], fill=(20, 48, 76, 255))
    d.polygon([(1340, 252), (1400, 220), (1460, 250), (1430, 262), (1400, 246), (1370, 266)], fill=(235, 242, 248, 255))
    d.polygon([(760, 270), (820, 240), (880, 268), (850, 280), (820, 262), (790, 284)], fill=(235, 242, 248, 255))
    # signature: gold cable drawn on, gondola glides along it all clip long
    pc = ease_in_out(prog(t, 0.2, 1.2))
    p0, p1 = (60, 410), (1860, 150)
    if pc > 0:
        d.line((p0[0], p0[1], p0[0] + (p1[0] - p0[0]) * pc, p0[1] + (p1[1] - p0[1]) * pc), fill=GOLD + (255,), width=5)
    for x, y in (p0, p1):
        d.rectangle((x - 8, y - 10, x + 8, y + 70), fill=WHITE + (int(255 * prog(t, .1, .3)),))
    g = ease_in_out(prog(t, 1.0, 9.0))
    gx = p0[0] + 80 + (p1[0] - p0[0] - 160) * g; gy = p0[1] + (p1[1] - p0[1]) * ((gx - p0[0]) / (p1[0] - p0[0]))
    gondola(d, gx, gy, prog(t, 1.0, .3))
    # title
    pt = ease_out(prog(t, .3, .5))
    text(L, (100, 495), 'ROPEWAYS & PARKS', font('800', 40), GOLD, pt, dy=20 * (1 - pt))
    text(L, (100, 545), 'Five ropeways that suit every age', font('800', 66), WHITE, pt, dy=24 * (1 - pt))
    # cards
    cw, chh, gap = 330, 290, 22
    x0 = (W - (5 * cw + 4 * gap)) / 2
    for i, (n, wh, ln) in enumerate(RW):
        p = ease_back(prog(t, 1.6 + i * .55, .5), 1.2)
        if p <= 0: continue
        a = clamp(p)
        x = x0 + i * (cw + gap); y = 655 + 40 * (1 - a)
        d.rounded_rectangle((x, y, x + cw, y + chh), radius=20, fill=(255, 255, 255, int(20 * a)), outline=GOLD + (int(200 * a),), width=3)
        d.ellipse((x + 26, y + 30, x + 64, y + 68), fill=GOLD + (int(255 * a),))
        text(L, (x + 45, y + 49), str(i + 1), font('800', 26), NAVY, a, anchor='mm')
        f = font('800', 34)
        sz = 34
        while f.getlength(n) > cw - 50 and sz > 24: sz -= 2; f = font('800', sz)
        text(L, (x + 26, y + 92), n, f, WHITE, a)
        text(L, (x + 26, y + 138), wh, font('500', 28), LBLUE, a)
        # wrap line into two rows
        words = ln.split(); rows = ['']
        for w_ in words:
            tryr = (rows[-1] + ' ' + w_).strip()
            if font('500', 27).getlength(tryr) <= cw - 50: rows[-1] = tryr
            else: rows.append(w_)
        for k, r in enumerate(rows[:2]):
            text(L, (x + 26, y + 180 + k * 34), r, font('500', 27), WHITE, a * .92)
    pe = ease_out(prog(t, 5.0, .6))
    text(L, (W / 2, 1010), 'Year-round, weather permitting · timings change on maintenance days · Get Quote', font('500', 32), GOLD_L, pe, anchor='mm', dy=14 * (1 - pe))
    im.alpha_composite(L)
    return im.convert('RGB')

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'snap':
        for ts in sys.argv[2:]:
            render(float(ts)).save(f'/home/claude/work/out/snap-rw-{ts}.jpg', quality=85)
        sys.exit()
    w = Writer('/home/claude/work/out/ropeways-master.mp4', W, H, FPS)
    for f in range(int(DUR * FPS)):
        w.add(render(f / FPS))
    w.close()
