"""Skiing explainer: 'Three slopes, one winter'. 1920x1080, 30 fps, 12 s. Facts only from the brief:
Solang ~2,500 m, 13-14 km from Manali; Narkanda (Dhumri slopes) ~2,700 m, 63 km from Shimla; Kufri ~2,600 m,
16-20 km from Shimla. Season Jan-Mar, best Feb, depends on each winter's snow. ABVIMAS courses Jan-Mar:
7-day elementary (10+), 14-day basic to advanced. Map is schematic (not to scale)."""
import sys
from PIL import Image, ImageDraw
from sz import *

W, H, FPS, DUR = 1920, 1080, 30, 12.0
BG = Image.new('RGBA', (W, H), NAVY + (255,))
glow = Image.new('RGBA', (W, H), (0, 0, 0, 0)); gd = ImageDraw.Draw(glow)
for r in range(760, 0, -20):
    gd.ellipse((420 - r, 420 - r, 420 + r, 420 + r), fill=(22, 57, 92, int(3 + 0.9 * (760 - r) / 20)))
BG.alpha_composite(glow)
snow = Snow(W, H, 70, seed=12, rmin=2, rmax=5)
CARD = (22, 57, 92); ICE = (190, 225, 245)

# schematic pins (not to scale): Manali/Solang north, Shimla south with Kufri and Narkanda east of it
PINS = [  # key, x, y, label, alt, note, label side
    ('Solang', 440, 360, 'Solang', 2500, '13–14 km from Manali', 'r'),
    ('Kufri', 600, 800, 'Kufri', 2600, '16–20 km from Shimla', 'l'),
    ('Narkanda', 760, 650, 'Narkanda', 2700, '63 km from Shimla', 'r'),
]
SHIMLA = (470, 860)
RIDGES = [[(140, 560), (240, 470), (300, 520), (380, 420), (470, 500), (560, 400), (650, 470), (760, 380), (860, 460)],
          [(160, 700), (260, 640), (360, 690), (470, 600), (560, 660), (700, 580), (820, 640), (930, 560)]]
MON = ['DEC', 'JAN', 'FEB', 'MAR']

def render(t):
    im = BG.copy(); L = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    endp = ease_out(prog(t, 10.1, .45))
    mapa = 1 - ease_out(prog(t, 5.6, .45))
    seasa = ease_out(prog(t, 5.9, .5)) * (1 - endp)
    snow.draw(L, t, alpha=.35 * ease_out(prog(t, .6, .6)) * (1 - endp) + .25 * endp)
    p = ease_out(prog(t, .1, .5)); hd = 1 - endp
    text(L, (120, 80), 'SKIING · HIMACHAL', font('800', 36), GOLD, p * hd, dy=-16 * (1 - p))
    p2 = ease_out(prog(t, .25, .5))
    if t < 5.75:
        text(L, (120, 128), 'Three slopes, one winter', font('800', 92), WHITE, p2 * (1 - prog(t, 5.45, .3)), dy=30 * (1 - p2))
    else:
        q = ease_out(prog(t, 5.8, .4))
        text(L, (120, 128), 'When to go', font('800', 92), WHITE, q * hd, dy=30 * (1 - q))
    if mapa > 0:
        for k, rg in enumerate(RIDGES):
            ra = ease_out(prog(t, .5 + k * .2, .8)) * mapa
            seg = polyline_partial(rg, ease_in_out(prog(t, .5 + k * .2, 1.2)))
            if len(seg) > 1: d.line(seg, fill=(255, 255, 255, int(45 * ra)), width=4, joint='curve')
        text(L, (120, 980), 'Schematic map, not to scale', font('500', 24), WHITE, .5 * mapa * ease_out(prog(t, 1, .5)))
        # Shimla reference dot + link Manali side to Shimla side
        sa = ease_out(prog(t, 1.0, .4)) * mapa
        x, y = SHIMLA
        d.ellipse((x - 9, y - 9, x + 9, y + 9), fill=WHITE + (int(200 * sa),))
        text(L, (x - 22, y + 8), 'Shimla', font('500', 30), WHITE, sa * .85, anchor='rm')
        for i, (key, x, y, lab, alt, note, side) in enumerate(PINS):
            t0 = 1.2 + i * .75
            pa = ease_back(prog(t, t0, .45)) ; aa = ease_out(prog(t, t0, .35)) * mapa
            if aa <= 0: continue
            rr = 18 * clamp(pa, 0, 1.2)
            # pin drop: stem + head
            d.line((x, y, x, y - 46 * clamp(pa, 0, 1)), fill=GOLD + (int(255 * aa),), width=5)
            d.ellipse((x - rr, y - 46 - rr, x + rr, y - 46 + rr), fill=GOLD + (int(255 * aa),), outline=GOLD_L + (int(255 * aa),), width=4)
            d.ellipse((x - 6, y - 3, x + 6, y + 3), fill=(0, 0, 0, int(90 * aa)))
            cp = ease_out(prog(t, t0 + .15, 1.2))
            a = round((2000 + (alt - 2000) * cp) / 10) * 10
            if side == 'r':
                text(L, (x + 36, y - 60), lab, font('800', 46), WHITE, aa, anchor='ls')
                text(L, (x + 36, y - 14), f'~{a:,} m', font('800', 38), GOLD_L, aa, anchor='ls')
            else:
                text(L, (x - 36, y - 60), lab, font('800', 46), WHITE, aa, anchor='rs')
                text(L, (x - 36, y - 14), f'~{a:,} m', font('800', 38), GOLD_L, aa, anchor='rs')
        # right column cards
        for i, (key, x, y, lab, alt, note, side) in enumerate(PINS):
            t0 = 1.5 + i * .75; ca = ease_out(prog(t, t0, .45)) * mapa
            if ca <= 0: continue
            cx = 1080; cy = 300 + i * 200 + 30 * (1 - ca)
            d.rounded_rectangle((cx, cy, cx + 720, cy + 170), radius=24, fill=CARD + (int(255 * ca),))
            d.rounded_rectangle((cx, cy, cx + 10, cy + 170), radius=5, fill=GOLD + (int(255 * ca),))
            text(L, (cx + 44, cy + 34), lab, font('800', 54), WHITE, ca)
            text(L, (cx + 44, cy + 108), note, font('500', 34), ICE, ca * .95)
            text(L, (cx + 680, cy + 34), f'~{alt:,} m', font('800', 44), GOLD_L, ca, anchor='ra')
        text(L, (1080, 940), 'Gentle nursery slopes — good for first-timers', font('500', 32), WHITE, ease_out(prog(t, 3.8, .5)) * mapa * .9)
    if seasa > 0:
        SX, SW, SY, SH = 120, 1680 / 4, 360, 110
        for i, m in enumerate(MON):
            a = ease_out(prog(t, 6.0 + i * .06, .4)) * seasa
            text(L, (SX + SW * (i + .5), SY - 26), m, font('800', 38), WHITE, a * .9, anchor='ms')
        d.rounded_rectangle((SX, SY, SX + 4 * SW, SY + SH), radius=24, fill=(255, 255, 255, int(20 * seasa)))
        bp = ease_in_out(prog(t, 6.3, 1.0))
        x0 = SX + SW; x1 = x0 + 3 * SW * bp
        if x1 - x0 > 10:
            d.rounded_rectangle((x0 + 4, SY + 4, x1 - 4, SY + SH - 4), radius=20, fill=ICE + (int(255 * seasa),))
        fa = ease_back(prog(t, 7.2, .5))
        if fa > 0:
            fx0, fx1 = SX + 2 * SW + 4, SX + 3 * SW - 4
            d.rounded_rectangle((fx0, SY + 4, fx1, SY + SH - 4), radius=20, fill=GOLD + (int(255 * seasa * clamp(fa)),))
            text(L, ((fx0 + fx1) / 2, SY + SH / 2), 'BEST', font('800', 44), NAVY, seasa * clamp(fa), anchor='mm')
        text(L, (SX + SW * 1.5, SY + SH / 2), 'SKI', font('800', 40), NAVY, seasa * ease_out(prog(t, 6.9, .3)), anchor='mm')
        text(L, (SX + SW * 3.5, SY + SH / 2), 'SKI', font('800', 40), NAVY, seasa * ease_out(prog(t, 7.1, .3)), anchor='mm')
        text(L, (SX, SY + SH + 56), 'January to March, best in February — depends on each winter\'s snow', font('500', 36), WHITE, seasa * ease_out(prog(t, 7.5, .4)) * .92)
        # ABVIMAS course cards
        CC = [(7, '{:d} days', 'Elementary course · age 10+'), (14, '{:d} days', 'Basic, intermediate, advanced')]
        pa = ease_out(prog(t, 8.0, .45)) * seasa
        pill(L, (SX, 690), 'ABVIMAS courses · Jan – Mar', font('800', 36), GOLD, NAVY, pa, pad=(30, 14))
        for i, (v, fmt, lab) in enumerate(CC):
            t0 = 8.3 + i * .4; ca = ease_out(prog(t, t0, .45)) * seasa
            if ca <= 0: continue
            x = SX + i * 620; y = 790 + 30 * (1 - ca)
            d.rounded_rectangle((x, y, x + 580, y + 170), radius=24, fill=CARD + (int(255 * ca),))
            d.rounded_rectangle((x, y, x + 580, y + 10), radius=5, fill=GOLD + (int(255 * ca),))
            cp = ease_out(prog(t, t0 + .1, 1.0))
            text(L, (x + 36, y + 30), fmt.format(round(v * cp)), font('800', 72), GOLD_L, ca)
            text(L, (x + 36, y + 118), lab, font('500', 32), WHITE, ca * .9)
        ga = ease_out(prog(t, 9.0, .45)) * seasa
        text(L, (1400, 840), 'Government institute,', font('500', 32), WHITE, ga * .85)
        text(L, (1400, 884), 'Manali', font('500', 32), WHITE, ga * .85)
    if endp > 0:
        e1 = ease_out(prog(t, 10.25, .5)); e2 = ease_out(prog(t, 10.5, .5)); e3 = ease_out(prog(t, 10.75, .5))
        text(L, (W / 2, 380), 'Lesson or course?', font('800', 110), WHITE, e1, dy=30 * (1 - e1), anchor='mm')
        text(L, (W / 2, 495), 'We add the hotel, cab and snow gear', font('500', 48), WHITE, e2 * .9, dy=20 * (1 - e2), anchor='mm')
        f = font('800', 52); w = f.getlength('Get Quote') + 120
        pill(L, (W / 2 - w / 2, 590), 'Get Quote', f, GOLD, NAVY, e3, pad=(60, 24), scale=0.9 + 0.1 * e3)
        text(L, (W / 2, 790), 'suzutravels.com/adventure', font('500', 36), GOLD_L, e3, anchor='mm')
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
