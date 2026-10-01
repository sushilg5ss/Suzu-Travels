"""Solang explainer: 'Solang by month'. 1920x1080, 30 fps, 12 s. Facts only from the brief:
snow usually late Dec-Feb; flying Mar-mid-Jul & mid-Sep-Nov; paragliding closed 15 Jul-15 Sep (Kullu order);
13-14 km from Manali; ropeway 1.3 km; ~2,500 m -> ~3,200 m at Fatru (+700 m); Manali -> Palchan -> Solang -> Atal Tunnel south portal."""
import sys
from PIL import Image, ImageDraw
from sz import *

W, H, FPS, DUR = 1920, 1080, 30, 12.0
BG = Image.new('RGBA', (W, H), NAVY + (255,))
glow = Image.new('RGBA', (W, H), (0, 0, 0, 0)); gd = ImageDraw.Draw(glow)
for r in range(760, 0, -20):
    gd.ellipse((1560 - r, 120 - r, 1560 + r, 120 + r), fill=(22, 57, 92, int(3 + 0.9 * (760 - r) / 20)))
BG.alpha_composite(glow)
snow = Snow(W, H, 70, seed=9, rmin=2, rmax=5)
CARD = (22, 57, 92); ICE = (190, 225, 245); RED = (214, 69, 65)
MON = 'JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC'.split()
SX, SW = 330, 1460 / 12  # strip x start, month width
def mx(m): return SX + SW * m  # m in months from 1 Jan (float)

ROWS = [  # label, colour, [(start, end) in months], text colour
    ('Snow', ICE, [(0, 2), (11, 12)], NAVY, 'usually late Dec – Feb'),
    ('Flying', GOLD, [(2, 6.5), (8.5, 11)], NAVY, 'Mar – mid-Jul · mid-Sep – Nov'),
    ('Closed', RED, [(6.5, 8.5)], WHITE, 'no paragliding 15 Jul – 15 Sep'),
]
RY0, RH, RG = 330, 64, 26

def render(t):
    im = BG.copy(); L = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    endp = ease_out(prog(t, 10.2, .45))
    stripa = 1 - ease_out(prog(t, 6.3, .45))          # month strip + counters
    mapa = ease_out(prog(t, 6.6, .5)) * (1 - endp)     # mini map
    snow.draw(L, t, alpha=.35 * ease_out(prog(t, .9, .6)) * stripa + .25 * endp)
    p = ease_out(prog(t, .1, .5)); hd = 1 - endp
    text(L, (120, 80), 'SOLANG VALLEY · MANALI', font('800', 36), GOLD, p * hd, dy=-16 * (1 - p))
    p2 = ease_out(prog(t, .25, .5))
    title = 'Solang by month' if t < 6.45 else 'Getting there'
    ta = p2 * hd * (1 - prog(t, 6.15, .3) + prog(t, 6.5, .35)) if t < 7 else hd
    text(L, (120, 128), title, font('800', 92), WHITE, clamp(ta), dy=30 * (1 - p2))
    if stripa > 0:
        # month labels
        for i, m in enumerate(MON):
            a = ease_out(prog(t, .5 + i * .04, .4)) * stripa
            text(L, (mx(i + .5), RY0 - 30), m, font('800', 30), WHITE, a * .85, anchor='ms')
            d.line((mx(i), RY0 - 10, mx(i), RY0 + 3 * (RH + RG) - RG), fill=(255, 255, 255, int(40 * a)), width=2)
        d.line((mx(12), RY0 - 10, mx(12), RY0 + 3 * (RH + RG) - RG), fill=(255, 255, 255, int(40 * stripa)), width=2)
        for r, (lab, col, spans, tc, note) in enumerate(ROWS):
            t0 = 1.0 + r * .7; y = RY0 + r * (RH + RG)
            la = ease_out(prog(t, t0, .4)) * stripa
            text(L, (120, y + RH / 2), lab, font('800', 42), col if r != 0 else ICE, la, anchor='lm')
            d.rounded_rectangle((SX, y, mx(12), y + RH), radius=14, fill=(255, 255, 255, int(18 * la)))
            for s, e in spans:
                bp = ease_in_out(prog(t, t0 + .1, .8))
                x1 = mx(s) + (mx(e) - mx(s)) * bp
                if x1 - mx(s) > 8:
                    d.rounded_rectangle((mx(s) + 3, y + 3, x1 - 3, y + RH - 3), radius=12, fill=col + (int(255 * stripa),))
            na = ease_out(prog(t, t0 + .7, .4)) * stripa
            # note under the widest span
            s, e = max(spans, key=lambda se: se[1] - se[0])
            if r == 2:
                text(L, ((mx(s) + mx(e)) / 2, y + RH / 2), 'CLOSED', font('800', 30), WHITE, na, anchor='mm')
        # legend notes
        ny = RY0 + 3 * (RH + RG) + 10
        for r, (lab, col, spans, tc, note) in enumerate(ROWS):
            na = ease_out(prog(t, 1.8 + r * .7, .4)) * stripa
            x = 330 + r * 500
            d.rounded_rectangle((x, ny + 8, x + 22, ny + 30), radius=6, fill=col + (int(255 * na),))
            text(L, (x + 36, ny + 19), note, font('500', 30), WHITE, na * .9, anchor='lm')
        # counters
        CN = [(13, '{:d} km', 'from Manali (13–14 km)'), (1.3, '{:.1f} km', 'ropeway to Fatru'), (700, '+{:d} m', 'climb, ~2,500 to ~3,200 m')]
        for i, (v, fmt, lab) in enumerate(CN):
            t0 = 3.4 + i * .45; ca = ease_out(prog(t, t0, .45)) * stripa
            if ca <= 0: continue
            x = 120 + i * 570; y = 790 + 30 * (1 - ca)
            d.rounded_rectangle((x, y, x + 530, y + 190), radius=24, fill=CARD + (int(255 * ca),))
            d.rounded_rectangle((x, y, x + 530, y + 10), radius=5, fill=GOLD + (int(255 * ca),))
            cp = ease_out(prog(t, t0 + .1, 1.3))
            val = v * cp
            sval = fmt.format(round(val) if isinstance(v, int) else round(val, 1))
            text(L, (x + 36, y + 40), sval, font('800', 80), GOLD_L, ca)
            text(L, (x + 36, y + 136), lab, font('500', 32), WHITE, ca * .9)
    if mapa > 0:
        # schematic mini-map, Manali (bottom) -> Palchan -> Solang -> Atal Tunnel south portal (top)
        pts = [(330, 900), (620, 760), (900, 560), (1180, 440), (1400, 300)]
        line = smooth(pts, 14)
        rp = ease_in_out(prog(t, 6.8, 2.4))
        d.line(line, fill=(255, 255, 255, int(70 * mapa)), width=6, joint='curve')
        seg = polyline_partial(line, rp)
        if len(seg) > 1: d.line(seg, fill=GOLD + (int(255 * mapa),), width=10, joint='curve')
        NODES = [(0, 'Manali', '~2,050 m', 'r'), (1, 'Palchan', '', 'r'), (2, 'Solang Valley', '~2,500 m · ropeway to Fatru', 'r'), (4, 'Atal Tunnel', 'south portal · a short drive on', 'r')]
        for k, (idx, lab, sub, side) in enumerate(NODES):
            x, y = pts[idx]
            frac = [0, .26, .55, 1.0][k]
            na = ease_out(prog(rp, frac - .07, .07)) * mapa if frac > 0 else mapa
            big = idx == 2
            rr = 22 if big else 14
            d.ellipse((x - rr, y - rr, x + rr, y + rr), fill=(GOLD if big else WHITE) + (int(255 * na),), outline=GOLD + (int(255 * na),), width=6)
            if side == 'r':
                oy = 0 if idx == 4 else 50
                text(L, (x + 40, y - 8 + oy), lab, font('800', 54 if big else 42), WHITE, na, anchor='ls')
                if sub: text(L, (x + 40, y + 40 + oy), sub, font('500', 32), GOLD_L if big else WHITE, na * .95, anchor='ls')
            else:
                text(L, (x - 40, y - 8), lab, font('800', 42), WHITE, na, anchor='rs')
                text(L, (x - 40, y + 38), sub, font('500', 30), WHITE, na * .9, anchor='rs')
        la = ease_out(prog(t, 7.6, .5)) * mapa
        text(L, (120, 300), 'Manali to Solang: 13–14 km · 30–40 min by cab', font('500', 34), GOLD_L, la, anchor='ls')
        pill(L, (1180, 800), 'No permit needed', font('800', 34), GOLD, NAVY, ease_out(prog(t, 8.6, .4)) * mapa, pad=(28, 14))
        text(L, (1180, 900), 'Only Rohtang Pass needs a permit', font('500', 28), WHITE, ease_out(prog(t, 8.9, .4)) * mapa * .85)
    if endp > 0:
        e1 = ease_out(prog(t, 10.35, .5)); e2 = ease_out(prog(t, 10.6, .5)); e3 = ease_out(prog(t, 10.85, .5))
        text(L, (W / 2, 390), 'Hotel + cab + Solang day', font('800', 104), WHITE, e1, dy=30 * (1 - e1), anchor='mm')
        text(L, (W / 2, 500), 'We check the season and road before you go', font('500', 48), WHITE, e2 * .9, dy=20 * (1 - e2), anchor='mm')
        f = font('800', 52); w = f.getlength('Get Quote') + 120
        pill(L, (W / 2 - w / 2, 600), 'Get Quote', f, GOLD, NAVY, e3, pad=(60, 24), scale=0.9 + 0.1 * e3)
        text(L, (W / 2, 800), 'suzutravels.com/adventure', font('500', 36), GOLD_L, e3, anchor='mm')
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
