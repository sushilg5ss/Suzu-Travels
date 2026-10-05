"""Snow gear explainer: 'Your snow kit check'. 1920x1080, 30 fps, 10 s. Facts only from the brief:
try-on checks (both boots same size, gloves waterproof, zips work, thermals underneath); the driver stops at a rental
shop on the way (Manali -> Palchan -> Solang / Kothi-Gulaba / Atal Tunnel -> Sissu); gear returned on the way back;
added to one quote with hotel + cab. Map is schematic (not to scale). No prices."""
import sys
from PIL import Image, ImageDraw
from sz import *

W, H, FPS, DUR = 1920, 1080, 30, 10.0
BG = Image.new('RGBA', (W, H), NAVY + (255,))
glow = Image.new('RGBA', (W, H), (0, 0, 0, 0)); gd = ImageDraw.Draw(glow)
for r in range(760, 0, -20):
    gd.ellipse((1400 - r, 520 - r, 1400 + r, 520 + r), fill=(22, 57, 92, int(3 + 0.9 * (760 - r) / 20)))
BG.alpha_composite(glow)
snow = Snow(W, H, 70, seed=21, rmin=2, rmax=5)
CARD = (22, 57, 92); ICE = (190, 225, 245)

CHECKS = [('Boots', 'both the same size'), ('Gloves', 'waterproof'), ('Zips', 'all working'), ('Thermals', 'worn underneath')]

# schematic map (right side), not to scale
MAN = (1180, 930); PAL = (1240, 700); SOL = (1010, 520); KOT = (1420, 470); GUL = (1470, 330)
TUN = (1080, 330); SIS = (1220, 170)
ROADS = [([MAN, (1215, 820), PAL], 0.0), ([PAL, (1120, 610), SOL], 0.35), ([PAL, (1340, 600), KOT, GUL], 0.35),
         ([SOL, (1030, 420), TUN, SIS], 0.75)]

def draw_road(d, pts, p, a):
    sp = smooth(pts, 14)
    d.line(sp, fill=(255, 255, 255, int(55 * a)), width=6, joint='curve')
    seg = polyline_partial(sp, p)
    if len(seg) > 1: d.line(seg, fill=GOLD + (int(255 * a),), width=8, joint='curve')

def dot(d, xy, r, a, fill=WHITE):
    x, y = xy; d.ellipse((x - r, y - r, x + r, y + r), fill=fill + (int(255 * a),), outline=GOLD + (int(255 * a),), width=4)

def render(t):
    im = BG.copy(); L = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    endp = ease_out(prog(t, 8.5, .45))
    snow.draw(L, t, alpha=.30 + .1 * endp)
    hd = 1 - endp
    p = ease_out(prog(t, .1, .5))
    text(L, (120, 90), 'SNOW GEAR · MANALI', font('800', 36), GOLD, p * hd, dy=-16 * (1 - p))
    p2 = ease_out(prog(t, .25, .5))
    text(L, (120, 140), 'Your snow kit check', font('800', 92), WHITE, p2 * hd, dy=30 * (1 - p2))
    text(L, (120, 262), 'Four things to check at the rental shop', font('500', 38), ICE, ease_out(prog(t, .5, .5)) * hd)
    # check list (left)
    for i, (k, v) in enumerate(CHECKS):
        t0 = 0.9 + i * 0.9
        a = ease_out(prog(t, t0, .45)) * hd
        if a <= 0: continue
        y = 360 + i * 140; dx = -40 * (1 - a)
        d.rounded_rectangle((120 + dx, y, 860 + dx, y + 112), radius=22, fill=CARD + (int(235 * a),))
        cp = ease_back(prog(t, t0 + .35, .4))
        cx, cy = 186 + dx, y + 56
        if cp > 0:
            r = 34 * clamp(cp, 0, 1.15)
            d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=GOLD + (int(255 * a),))
            tp = ease_out(prog(t, t0 + .5, .35))
            tick = polyline_partial([(cx - 15, cy + 1), (cx - 4, cy + 13), (cx + 17, cy - 12)], tp)
            if len(tick) > 1: d.line(tick, fill=NAVY + (int(255 * a),), width=8, joint='curve')
        text(L, (250 + dx, y + 56), k, font('800', 48), WHITE, a, anchor='lm')
        kw = font('800', 48).getlength(k)
        text(L, (250 + dx + kw + 20, y + 60), v, font('500', 36), ICE, a, anchor='lm')
    # map (right)
    ma = ease_out(prog(t, 1.2, .6)) * hd
    if ma > 0:
        for pts, off in ROADS:
            draw_road(d, pts, ease_in_out(prog(t, 1.5 + off * 4, 1.6)), ma)
        for xy, lab, side, tt in [(MAN, 'Manali', 'r', 1.4), (SOL, 'Solang', 'l', 3.6), (KOT, 'Kothi', 'r', 3.6),
                                  (GUL, 'Gulaba', 'r', 4.2), (TUN, 'Atal Tunnel', 'l', 5.6), (SIS, 'Sissu', 'r', 6.0)]:
            a = ease_out(prog(t, tt, .4)) * ma
            if a <= 0: continue
            dot(d, xy, 12, a)
            x, y = xy
            if side == 'r': text(L, (x + 26, y), lab, font('800', 34), WHITE, a, anchor='lm')
            else: text(L, (x - 26, y), lab, font('800', 34), WHITE, a, anchor='rm')
        # gear stop pin at Palchan
        pa = ease_back(prog(t, 2.6, .5))
        if pa > 0:
            a = clamp(pa) * ma; x, y = PAL; s = clamp(pa, 0, 1.15)
            d.ellipse((x - 16, y - 16, x + 16, y + 16), fill=GOLD + (int(255 * a),))
            d.polygon([(x, y - 18), (x - 30 * s, y - 64 * s), (x + 30 * s, y - 64 * s)], fill=GOLD + (int(255 * a),))
            d.ellipse((x - 34 * s, y - 112 * s, x + 34 * s, y - 44 * s), fill=GOLD + (int(255 * a),))
            d.ellipse((x - 13 * s, y - 91 * s, x + 13 * s, y - 65 * s), fill=NAVY + (int(255 * a),))
            pill(L, (x + 52, y - 40), 'GEAR STOP · on the way', font('800', 30), GOLD, NAVY, a, pad=(22, 12))
            text(L, (x + 52, y + 34), 'Pick up on the way, return on the way back', font('500', 28), ICE, ease_out(prog(t, 3.1, .5)) * ma)
        text(L, (1800, 1010), 'Schematic, not to scale', font('500', 24), (150, 170, 190), ma, anchor='rs')
    # end card
    if endp > 0:
        def ea(k): return ease_out(prog(t, 8.6 + k * .12, .45))
        text(L, (W / 2, 330), 'SNOW DAY, SORTED', font('800', 40), GOLD, ea(0), anchor='mm', dy=24 * (1 - ea(0)))
        text(L, (W / 2, 440), 'Gear added to your quote', font('800', 104), WHITE, ea(1), anchor='mm', dy=30 * (1 - ea(1)))
        text(L, (W / 2, 548), 'Hotel + cab + snow suit, boots and gloves', font('500', 44), ICE, ea(2), anchor='mm')
        bp = ease_back(prog(t, 9.0, .45))
        if bp > 0:
            f = font('800', 60); w = f.getlength('Get Quote') + 120
            pill(L, (W / 2 - w / 2, 640), 'Get Quote', f, GOLD, NAVY, clamp(bp), pad=(60, 28), scale=clamp(bp, 0, 1.1))
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
