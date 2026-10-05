"""Hub water explainer: 'Where and when you can get on the water'. 1920x1080 (web 1600x900), 30 fps, 12 s.
Facts only from the live hub #water section (page 11529): Beas rafting Kullu (Pirdi/Babeli/Raisan to Jhiri, Grade II-III,
Mar-Jun + mid-Sep-Nov, closed 15 Jul-15 Sep); Sutlej rafting at Tattapani (Oct-May); lakes: Gobind Sagar (Luhnu, Bilaspur:
jet ski, speed boat, kayak), Kol Dam (boat rides), Pong Dam (kayak, canoe, sail), Oct-Jun, Pong closed 15 Jul-15 Sep;
trout angling Tirthan, Barot, Rohru, Sangla, 1 Mar-31 Oct, Fisheries licence. Map is schematic (not to scale). No prices."""
import sys
from PIL import Image, ImageDraw
from sz import *

W, H, FPS, DUR = 1920, 1080, 30, 12.0
BG = Image.new('RGBA', (W, H), NAVY + (255,))
glow = Image.new('RGBA', (W, H), (0, 0, 0, 0)); gd = ImageDraw.Draw(glow)
for r in range(760, 0, -20):
    gd.ellipse((700 - r, 560 - r, 700 + r, 560 + r), fill=(22, 57, 92, int(3 + 0.9 * (760 - r) / 20)))
BG.alpha_composite(glow)
CARD = (22, 57, 92); ICE = (190, 225, 245); WATER = (120, 196, 230); RED = (226, 110, 96)

BEAS = smooth([(1180, 360), (1080, 440), (980, 530), (840, 580), (660, 565), (430, 550)], 16)
SUT = smooth([(1230, 760), (1060, 800), (880, 770), (690, 830), (450, 930)], 16)
PINS = [  # x, y, label, side, appear
    (1060, 455, 'Kullu · Beas', 'r', 1.4, 'raft'),
    (450, 550, 'Pong Dam', 'l', 2.4, 'lake'),
    (1060, 800, 'Tattapani · Sutlej', 'r', 3.0, 'raft'),
    (880, 770, 'Kol Dam', 'b', 3.6, 'lake'),
    (690, 830, 'Gobind Sagar', 'b', 4.0, 'lake'),
    (1180, 630, 'Tirthan', 'r', 4.6, 'fish'),
    (820, 440, 'Barot', 'l', 4.8, 'fish'),
]
CARDS = [(1.4, 'RAFTING · BEAS', 'Kullu: Pirdi to Jhiri', 'Grade II–III rapids'),
         (3.0, 'RAFTING · SUTLEJ', 'Tattapani, near Shimla', 'Pairs with the hot springs'),
         (3.6, 'LAKES', 'Gobind Sagar · Kol Dam · Pong', 'Jet ski, kayak, boat rides'),
         (4.6, 'TROUT ANGLING', 'Tirthan · Barot · Rohru · Sangla', 'Fisheries licence needed')]
MON = ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D']
ROWS = [('Rafting, Beas', [(2, 6), (8.5, 11)]), ('Rafting, Tattapani', [(9, 12), (0, 5)]),
        ('Lakes', [(9, 12), (0, 6)]), ('Trout angling', [(2, 10)])]
MX0, MX1 = 560, 1800

def mx(m): return MX0 + (MX1 - MX0) * m / 12

def render(t):
    im = BG.copy(); L = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    endp = ease_out(prog(t, 10.6, .45))
    mapa = 1 - ease_out(prog(t, 6.3, .45))
    seasa = ease_out(prog(t, 6.6, .5)) * (1 - endp)
    hd = 1 - endp
    p = ease_out(prog(t, .1, .5))
    text(L, (120, 80), 'WATER · HIMACHAL', font('800', 36), GOLD, p * hd, dy=-16 * (1 - p))
    p2 = ease_out(prog(t, .25, .5))
    if t < 6.45:
        text(L, (120, 128), 'Where you can get on the water', font('800', 80), WHITE, p2 * (1 - prog(t, 6.15, .3)), dy=30 * (1 - p2))
    else:
        q = ease_out(prog(t, 6.55, .45))
        text(L, (120, 128), 'When the water is open', font('800', 80), WHITE, q * hd, dy=30 * (1 - q))
    if mapa > 0:
        # rivers (signature gold river line flowing in)
        for pts, t0, lab, lxy in [(BEAS, .5, 'Beas', (1200, 360)), (SUT, 1.0, 'Sutlej', (1250, 735))]:
            d.line(pts, fill=WATER + (int(70 * mapa),), width=14, joint='curve')
            seg = polyline_partial(pts, ease_in_out(prog(t, t0, 1.8)))
            if len(seg) > 1: d.line(seg, fill=GOLD + (int(255 * mapa),), width=7, joint='curve')
            text(L, lxy, lab, font('500', 28), ICE, mapa * ease_out(prog(t, t0 + .4, .4)), anchor='lm')
        # lakes as soft blobs
        for x, y, lab, side, ta, kind in PINS:
            a = ease_back(prog(t, ta, .45)); al = clamp(a) * mapa
            if al <= 0: continue
            s = clamp(a, 0, 1.15)
            if kind == 'lake':
                d.ellipse((x - 46 * s, y - 22 * s, x + 46 * s, y + 22 * s), fill=WATER + (int(150 * al),))
            r = (13 if kind != 'fish' else 10) * s
            d.ellipse((x - r, y - r, x + r, y + r), fill=(GOLD_L if kind == 'raft' else WHITE) + (int(255 * al),), outline=GOLD + (int(255 * al),), width=4)
            f = font('800', 30) if kind != 'fish' else font('500', 26)
            off = 58 if kind == 'lake' else 26
            if side == 'r': text(L, (x + off, y), lab, f, WHITE, al, anchor='lm')
            elif side == 'l': text(L, (x - off, y), lab, f, WHITE, al, anchor='rm')
            else: text(L, (x, y + 38), lab, f, WHITE, al, anchor='mt')
        text(L, (120, 1010), 'Schematic, not to scale', font('500', 24), (150, 170, 190), mapa * ease_out(prog(t, 1, .5)), anchor='ls')
        # cards on the right
        for i, (tc, k, a1, a2) in enumerate(CARDS):
            a = ease_out(prog(t, tc, .45)) * mapa
            if a <= 0: continue
            y = 290 + i * 172; dx = 40 * (1 - a)
            d.rounded_rectangle((1390 + dx, y, 1820 + dx, y + 150), radius=20, fill=CARD + (int(235 * a),))
            d.rounded_rectangle((1390 + dx, y, 1398 + dx, y + 150), radius=4, fill=GOLD + (int(255 * a),))
            text(L, (1420 + dx, y + 22), k, font('800', 26), GOLD, a)
            text(L, (1420 + dx, y + 60), a1, fit_f(a1, 380, 32, '800'), WHITE, a)
            text(L, (1420 + dx, y + 104), a2, fit_f(a2, 380, 28, '500'), ICE, a)
    if seasa > 0:
        a = seasa
        # month header
        for m, lab in enumerate(MON):
            text(L, ((mx(m) + mx(m + 1)) / 2, 300), lab, font('800', 30), ICE, a, anchor='mm')
        # monsoon closure band 15 Jul - 15 Sep
        bp = ease_out(prog(t, 8.6, .6))
        if bp > 0:
            x0, x1 = mx(6.5), mx(6.5 + 2 * bp)
            d.rounded_rectangle((x0, 330, max(x0 + 2, x1), 790), radius=12, fill=RED + (int(70 * a),), outline=RED + (int(220 * a),), width=3)
        for i, (lab, spans) in enumerate(ROWS):
            y = 360 + i * 105
            ra = ease_out(prog(t, 6.8 + i * .3, .45)) * a
            text(L, (120, y + 30), lab, font('800', 38), WHITE, ra, anchor='lm')
            d.rounded_rectangle((MX0, y + 14, MX1, y + 46), radius=16, fill=(255, 255, 255, int(28 * ra)))
            gp = ease_in_out(prog(t, 7.0 + i * .3, .9))
            for s0, s1 in spans:
                xe = mx(s0) + (mx(s1) - mx(s0)) * gp
                if xe - mx(s0) > 4:
                    d.rounded_rectangle((mx(s0), y + 14, xe, y + 46), radius=16, fill=GOLD + (int(255 * ra),))
        ta = ease_out(prog(t, 9.0, .5)) * a
        text(L, ((mx(6.5) + mx(8.5)) / 2, 830), 'Closed 15 Jul – 15 Sep', font('800', 32), RED, ta, anchor='mt')
        text(L, ((mx(6.5) + mx(8.5)) / 2, 872), 'rafting + water sports, Kullu & Kangra', font('500', 26), ICE, ta, anchor='mt')
        text(L, (120, 960), 'Trout: 1 Mar – 31 Oct · Rafting depends on river level and weather', font('500', 30), ICE, ease_out(prog(t, 9.4, .5)) * a)
    if endp > 0:
        def ea(k): return ease_out(prog(t, 10.7 + k * .12, .45))
        text(L, (W / 2, 360), 'RAFTING · LAKES · TROUT', font('800', 40), GOLD, ea(0), anchor='mm', dy=24 * (1 - ea(0)))
        text(L, (W / 2, 470), 'We check the water for your date', font('800', 92), WHITE, ea(1), anchor='mm', dy=30 * (1 - ea(1)))
        text(L, (W / 2, 572), 'One quote with your hotel and cab', font('500', 44), ICE, ea(2), anchor='mm')
        bp = ease_back(prog(t, 11.1, .45))
        if bp > 0:
            f = font('800', 60); w = f.getlength('Get Quote') + 120
            pill(L, (W / 2 - w / 2, 660), 'Get Quote', f, GOLD, NAVY, clamp(bp), pad=(60, 28), scale=clamp(bp, 0, 1.1))
    im.alpha_composite(L)
    return im.convert('RGB')

def fit_f(s, w, size, wt):
    while size > 18 and font(wt, size).getlength(s) > w: size -= 2
    return font(wt, size)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'snap':
        for ts in sys.argv[2:]:
            render(float(ts)).save(f'/home/claude/work/snap-water-{ts}.jpg', quality=85)
        sys.exit()
    w = Writer('/home/claude/work/out/water-master.mp4', W, H, FPS)
    for f in range(int(DUR * FPS)):
        w.add(render(f / FPS))
    w.close()
