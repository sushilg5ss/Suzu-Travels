"""Hub Air category motion graphic: 'Where and when you can fly'. 1920x1080, 30 fps, 12 s.
Facts only from the live hub page 11529 (#air cards, #safety band) and the shared rules:
Bir Billing take-off about 2,400 m (Kangra), mid-Sep to Jun, best Oct-Nov & Mar-May; Manali registered sites around
Solang, Dobhi, Gadsa, Raisan, Oct-Jun; Indrunag above Dharamshala, Oct-Jun; Bandla hill, Bilaspur, landing near
Gobind Sagar lake, Oct-Jun; monsoon stop 15 Jul-15 Sep (Kullu, Kangra); no passengers under 12 years or 30 kg;
registered pilots, notified sites; every flight depends on the day's weather. Map is schematic (not to scale)."""
import sys
from PIL import Image, ImageDraw
from sz import *

W, H, FPS, DUR = 1920, 1080, 30, 12.0
BG = Image.new('RGBA', (W, H), NAVY + (255,))
glow = Image.new('RGBA', (W, H), (0, 0, 0, 0)); gd = ImageDraw.Draw(glow)
for r in range(760, 0, -20):
    gd.ellipse((520 - r, 420 - r, 520 + r, 420 + r), fill=(22, 57, 92, int(3 + 0.9 * (760 - r) / 20)))
BG.alpha_composite(glow)
CARD = (22, 57, 92); ICE = (190, 225, 245); RED = (214, 69, 65); SKY = (120, 180, 220)
rnd = random.Random(5)
CLOUDS = [(rnd.uniform(0, W), rnd.uniform(260, 900), rnd.uniform(60, 140), rnd.uniform(8, 20)) for _ in range(9)]

PINS = [  # name, x, y, sub (card), side
    ('Bir Billing', 560, 620, 'Kangra · take-off about 2,400 m', 'r'),
    ('Indrunag', 330, 540, 'Above Dharamshala', 'l'),
    ('Manali', 830, 450, 'Solang, Dobhi, Gadsa, Raisan', 'r'),
    ('Bandla', 660, 880, 'Bilaspur · lands near Gobind Sagar', 'r'),
]
MON = 'JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC'.split()
SX, SWD = 330, 1460 / 12
def mx(m): return SX + SWD * m
ROWS = [
    ('Flying', ICE, [(0, 6), (8.5, 12)], 'Mid-Sep – Jun at Bir · Oct – Jun at the others'),
    ('Best', GOLD, [(2, 5), (9, 11)], 'Oct – Nov · Mar – May'),
    ('Closed', RED, [(6.5, 8.5)], 'No flying 15 Jul – 15 Sep (Kullu, Kangra)'),
]
RY0, RH, RG = 330, 60, 24

def glider(d, x, y, a, s=1.0):
    # small paraglider: arc wing + lines + pilot dot
    col = GOLD + (int(255 * a),)
    d.arc((x - 34 * s, y - 26 * s, x + 34 * s, y + 18 * s), 200, 340, fill=col, width=int(8 * s))
    for dx in (-26, 0, 26):
        d.line((x + dx * s, y - 14 * s + abs(dx) * .25 * s, x, y + 22 * s), fill=(255, 255, 255, int(170 * a)), width=2)
    d.ellipse((x - 6 * s, y + 18 * s, x + 6 * s, y + 30 * s), fill=(255, 255, 255, int(255 * a)))

def render(t):
    im = BG.copy(); L = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    endp = ease_out(prog(t, 10.1, .45))
    mapa = 1 - ease_out(prog(t, 5.6, .45))
    seasa = ease_out(prog(t, 5.9, .5)) * (1 - endp)
    p = ease_out(prog(t, .1, .5)); hd = 1 - endp
    text(L, (120, 80), 'AIR · HIMACHAL', font('800', 36), GOLD, p * hd, dy=-16 * (1 - p))
    p2 = ease_out(prog(t, .25, .5))
    if t < 5.75:
        text(L, (120, 128), 'Where you can fly', font('800', 92), WHITE, p2 * (1 - prog(t, 5.45, .3)), dy=30 * (1 - p2))
    else:
        q = ease_out(prog(t, 5.8, .4))
        text(L, (120, 128), 'When you can fly', font('800', 92), WHITE, q * hd, dy=30 * (1 - q))
    if mapa > 0:
        text(L, (120, 980), 'Schematic map, not to scale', font('500', 24), WHITE, .5 * mapa * ease_out(prog(t, 1, .5)))
        for i, (name, x, y, sub, side) in enumerate(PINS):
            t0 = 1.0 + i * .6
            aa = ease_out(prog(t, t0, .35)) * mapa
            if aa <= 0: continue
            # flight arc: take-off above the pin, glider drifts down to it
            fp = ease_in_out(prog(t, t0, 1.6))
            arc = smooth([(x - 120, y - 150), (x - 40, y - 175), (x + 50, y - 110), (x, y - 20)], 10)
            d.line(arc, fill=(255, 255, 255, int(50 * aa)), width=3, joint='curve')
            seg = polyline_partial(arc, fp)
            if len(seg) > 1: d.line(seg, fill=GOLD + (int(220 * aa),), width=5, joint='curve')
            gx, gy = seg[-1]
            glider(d, gx, gy - 30, aa * (1 - prog(fp, .92, .08)), .8)
            pa = ease_back(prog(t, t0 + 1.3, .4))
            rr = 16 * clamp(pa, 0, 1.2)
            if rr > 0:
                d.ellipse((x - rr, y - rr, x + rr, y + rr), fill=GOLD + (int(255 * aa),), outline=GOLD_L + (int(255 * aa),), width=4)
            la = ease_out(prog(t, t0 + 1.2, .4)) * mapa
            if side == 'r':
                text(L, (x + 30, y + 14), name, font('800', 40), WHITE, la, anchor='ls')
            else:
                text(L, (x - 30, y + 14), name, font('800', 40), WHITE, la, anchor='rs')
        for i, (name, x, y, sub, side) in enumerate(PINS):
            t0 = 1.4 + i * .6; ca = ease_out(prog(t, t0, .45)) * mapa
            if ca <= 0: continue
            cx = 1110; cy = 290 + i * 160 + 30 * (1 - ca)
            d.rounded_rectangle((cx, cy, cx + 700, cy + 136), radius=22, fill=CARD + (int(255 * ca),))
            d.rounded_rectangle((cx, cy, cx + 10, cy + 136), radius=5, fill=GOLD + (int(255 * ca),))
            text(L, (cx + 40, cy + 26), name, font('800', 46), WHITE, ca)
            text(L, (cx + 40, cy + 88), sub, font('500', 30), ICE, ca * .95)
        text(L, (1110, 960), 'Tandem flights with registered pilots', font('500', 32), WHITE, ease_out(prog(t, 4.0, .5)) * mapa * .9)
    if seasa > 0:
        for i, m in enumerate(MON):
            a = ease_out(prog(t, 6.0 + i * .03, .4)) * seasa
            text(L, (mx(i + .5), RY0 - 26), m, font('800', 28), WHITE, a * .85, anchor='ms')
            d.line((mx(i), RY0 - 8, mx(i), RY0 + 3 * (RH + RG) - RG), fill=(255, 255, 255, int(40 * a)), width=2)
        d.line((mx(12), RY0 - 8, mx(12), RY0 + 3 * (RH + RG) - RG), fill=(255, 255, 255, int(40 * seasa)), width=2)
        for r, (lab, col, spans, note) in enumerate(ROWS):
            t0 = 6.3 + r * .45; y = RY0 + r * (RH + RG)
            la = ease_out(prog(t, t0, .4)) * seasa
            text(L, (120, y + RH / 2), lab, font('800', 40), col, la, anchor='lm')
            d.rounded_rectangle((SX, y, mx(12), y + RH), radius=14, fill=(255, 255, 255, int(18 * la)))
            for s, e in spans:
                bp = ease_in_out(prog(t, t0 + .1, .7))
                x1 = mx(s) + (mx(e) - mx(s)) * bp
                if x1 - mx(s) > 8:
                    d.rounded_rectangle((mx(s) + 3, y + 3, x1 - 3, y + RH - 3), radius=12, fill=col + (int(255 * seasa),))
            if r == 2:
                s, e = spans[0]
                text(L, ((mx(s) + mx(e)) / 2, y + RH / 2), 'CLOSED', font('800', 28), WHITE, ease_out(prog(t, t0 + .7, .3)) * seasa, anchor='mm')
        ny = RY0 + 3 * (RH + RG) + 14
        for r, (lab, col, spans, note) in enumerate(ROWS):
            na = ease_out(prog(t, 7.1 + r * .3, .4)) * seasa
            yy = ny + r * 50
            d.rounded_rectangle((SX, yy + 8, SX + 22, yy + 30), radius=6, fill=col + (int(255 * na),))
            text(L, (SX + 36, yy + 19), note, font('500', 32), WHITE, na * .92, anchor='lm')
        RULES = ['12+ years · 30 kg+', 'Registered pilots, notified sites', 'Weather decides every flight']
        x = 120
        for i, rl in enumerate(RULES):
            ra = ease_back(prog(t, 8.2 + i * .35, .45))
            f = font('800', 34)
            w = f.getlength(rl) + 60
            if ra > 0:
                pill(L, (x, 870), rl, f, GOLD if i == 0 else CARD, NAVY if i == 0 else WHITE, clamp(ra) * seasa, pad=(30, 16), scale=clamp(.85 + .15 * ra, 0, 1.05))
            x += w + 28
    if endp > 0:
        e1 = ease_out(prog(t, 10.25, .5)); e2 = ease_out(prog(t, 10.5, .5)); e3 = ease_out(prog(t, 10.75, .5))
        glider(d, W / 2, 230 - 20 * e1, e1, 1.4)
        text(L, (W / 2, 380), 'Flight + hotel + cab', font('800', 110), WHITE, e1, dy=30 * (1 - e1), anchor='mm')
        text(L, (W / 2, 495), 'We check the site and the weather for your date', font('500', 48), WHITE, e2 * .9, dy=20 * (1 - e2), anchor='mm')
        f = font('800', 52); w = f.getlength('Get Quote') + 120
        pill(L, (W / 2 - w / 2, 590), 'Get Quote', f, GOLD, NAVY, e3, pad=(60, 24), scale=0.9 + 0.1 * e3)
        text(L, (W / 2, 790), 'suzutravels.com/adventure', font('500', 36), GOLD_L, e3, anchor='mm')
    im.alpha_composite(L)
    return im.convert('RGB')

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'snap':
        for ts in sys.argv[2:]:
            render(float(ts)).save(f'/home/claude/work/snap-air-{ts}.jpg', quality=85)
        sys.exit()
    w = Writer('/home/claude/work/out/air-explainer-master.mp4', W, H, FPS)
    for f in range(int(DUR * FPS)):
        w.add(render(f / FPS))
    w.close()
