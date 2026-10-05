"""Atal Tunnel & Sissu explainer 'Is Sissu open today?': 1600x900, 30 fps, 12 s. Suzu brand.
Map strip Manali -> Solang Nala barrier -> Atal Tunnel (9.02 km) -> Sissu (~40 km), 3-state road status
(Open / 4x4 + chains / Closed), month strip (Oct-Nov first snow, Dec-Feb deep snow, Mar-Apr melt), end card.
Facts from the brief only; no prices."""
import sys
from PIL import Image, ImageDraw, ImageFilter
from sz import *

W, H, FPS, DUR = 1600, 900, 30, 12.0
GREY = (120, 140, 160); RED = (214, 84, 72); LINE = (36, 66, 96)
bg = Image.new('RGBA', (W, H), NAVY + (255,)); _g = ImageDraw.Draw(bg)
for r in range(900, 0, -30):
    _g.ellipse((1250 - r, 120 - r * .7, 1250 + r, 120 + r * .7), fill=(22, 57, 92, int(2 + (900 - r) / 30)))
bg = bg.filter(ImageFilter.GaussianBlur(50))
SNOW = Snow(W, H, 60, seed=5, rmin=2, rmax=4)

XM, XB, XS, XN, XX, YM = 110, 470, 800, 1080, 1490, 340
def fit(s, w, size, wt='800'):
    while size > 24 and font(wt, size).getlength(s) > w: size -= 2
    return font(wt, size)

STATES = [(4.0, 5.4, 'OPEN', 'Road open to Sissu'),
          (5.4, 6.8, '4x4 ONLY', '4x4 with chains beyond Solang Nala'),
          (6.8, 8.6, 'CLOSED', 'Closed until BRO clears the snow')]
def state(t):
    for i, (s, e, _, _) in enumerate(STATES):
        if s <= t < e: return i
    return 0 if t < 4.0 else 2

def dashed(d, x0, x1, y, col, w=8, n=10):
    for k in range(n):
        a = x0 + (x1 - x0) * k / n; b = x0 + (x1 - x0) * (k + .55) / n
        d.line((a, y, b, y), fill=col, width=w)

def render(t):
    im = bg.copy(); L = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    SNOW.draw(L, t, alpha=.35)
    endp = ease_out(prog(t, 10.2, .5))
    mainA = 1 - endp
    k = ease_out(prog(t, .1, .5)) * mainA
    text(L, (XM, 70), 'IS SISSU OPEN TODAY?', font('800', 34), GOLD, k, dy=20 * (1 - k))
    k2 = ease_out(prog(t, .3, .5)) * mainA
    text(L, (XM, 112), 'Manali to Sissu, about 40 km', font('800', 64), WHITE, k2, dy=24 * (1 - k2))
    # map strip
    p = ease_in_out(prog(t, .8, 2.6))
    pa = int(255 * mainA)
    d.line((XM, YM, XX, YM), fill=LINE + (pa,), width=8)
    st = state(t) if t >= 4.0 else -1
    xe = XM + (XX - XM) * p
    beyond_col = GOLD if st in (-1, 0) else (GOLD_L if st == 1 else GREY)
    # leg 1: Manali -> barrier (always open)
    d.line((XM, YM, min(xe, XB), YM), fill=GOLD + (pa,), width=8)
    if xe > XB:
        if st == 1:
            dashed(d, XB, min(xe, XS), YM, GOLD_L + (pa,), n=6)
        else:
            d.line((XB, YM, min(xe, XS), YM), fill=beyond_col + (pa,), width=8)
    if xe > XS:  # tunnel: dashed underground
        dashed(d, XS, min(xe, XN), YM, (beyond_col if st != -1 else GOLD_L) + (pa,), w=6, n=8)
        if p > .55:
            ta = clamp((p - .55) / .1) * mainA
            text(L, ((XS + XN) / 2, YM - 30), 'Atal Tunnel · 9.02 km', font('800', 28), GOLD_L, ta, anchor='ms')
    if xe > XN:
        if st == 1: dashed(d, XN, min(xe, XX), YM, GOLD_L + (pa,), n=8)
        else: d.line((XN, YM, min(xe, XX), YM), fill=beyond_col + (pa,), width=8)
    nodes = [(XM, 'Manali', '~2,050 m', 0), (XB, 'Solang Nala', 'checkpoint', (XB - XM) / (XX - XM)),
             (XS, '', '', (XS - XM) / (XX - XM)), (XN, '', '', (XN - XM) / (XX - XM)), (XX, 'Sissu', '~3,120 m', .97)]
    for x, lab, sub, at in nodes:
        q = clamp((p - at) / .05) if at > 0 else clamp((t - .8) / .3)
        q *= mainA
        if q <= 0: continue
        r = 13 * ease_back(clamp(q), 1.3) if lab else 9
        d.ellipse((x - r, YM - r, x + r, YM + r), fill=WHITE + (int(255 * q),), outline=GOLD + (int(255 * q),), width=4)
        if lab:
            anc = 'la' if x == XM else ('ra' if x == XX else 'ma')
            text(L, (x, YM + 30), lab, font('800', 32), WHITE, q, anchor=anc)
            text(L, (x, YM + 72), sub, font('500', 26), (200, 214, 228), q, anchor=anc)
    # barrier at Solang Nala in CLOSED / 4x4 states
    if st in (1, 2):
        ba = ease_out(prog(t, STATES[st][0], .3)) * mainA
        col = RED if st == 2 else GOLD_L
        d.rounded_rectangle((XB + 14, YM - 62, XB + 24, YM - 10), radius=4, fill=col + (int(255 * ba),))
        for j in range(3):
            d.rectangle((XB + 24 + j * 30, YM - 60, XB + 38 + j * 30, YM - 48), fill=col + (int(255 * ba),))
            d.rectangle((XB + 38 + j * 30, YM - 60, XB + 54 + j * 30, YM - 48), fill=WHITE + (int(255 * ba),))
    # status toggle
    sa = ease_out(prog(t, 3.6, .5)) * mainA
    if sa > 0:
        text(L, (XM, 500), 'ROAD STATUS AFTER SNOWFALL', font('800', 26), GOLD_L, sa)
        x = XM
        for i, (s, e, lab, desc) in enumerate(STATES):
            on = (st == i)
            f = font('800', 34); w = f.getlength(lab) + 64
            fill = (RED if i == 2 else GOLD) if on else (255, 255, 255)
            d.rounded_rectangle((x, 540, x + w, 600), radius=30, fill=fill + (int((255 if on else 30) * sa),),
                                outline=((RED if i == 2 else GOLD) if on else (255, 255, 255)) + (int(255 * sa),), width=3)
            text(L, (x + w / 2, 570), lab, f, NAVY if (on and i != 2) else WHITE, sa, anchor='mm')
            x += w + 20
        if st >= 0:
            s0 = STATES[st][0]; da = ease_out(prog(t, s0 + .05, .35)) * mainA
            text(L, (x + 20, 570), STATES[st][3], fit(STATES[st][3], XX - x - 20, 34, '500'), WHITE, da, anchor='lm', dy=0)
    # month strip
    ma = ease_out(prog(t, 7.0, .5)) * mainA
    if ma > 0:
        text(L, (XM, 670), 'WHEN IS THE SNOW?', font('800', 26), GOLD_L, ma)
        months = ['OCT', 'NOV', 'DEC', 'JAN', 'FEB', 'MAR', 'APR']
        cw = (XX - XM - 6 * 10) / 7
        groups = [(0, 2, 'FIRST SNOW', (255, 255, 255), 70), (2, 5, 'DEEP SNOW', GOLD, 255), (5, 7, 'MELTING SNOW', (255, 255, 255), 30)]
        for gi, (a, b, lab, col, al) in enumerate(groups):
            gp = ease_back(prog(t, 7.3 + gi * .35, .5), 1.2)
            if gp <= 0: continue
            x0 = XM + a * (cw + 10); x1 = XM + b * (cw + 10) - 10
            yy = 712 + 20 * (1 - clamp(gp))
            d.rounded_rectangle((x0, yy, x1, yy + 70), radius=14, fill=col + (int(al * clamp(gp) * mainA),),
                                outline=col + (int(255 * clamp(gp) * mainA),), width=3)
            for m in range(a, b):
                cx = XM + m * (cw + 10) + cw / 2
                text(L, (cx, yy + 35), months[m], font('800', 28), NAVY if gi == 1 else WHITE, clamp(gp) * mainA, anchor='mm')
            text(L, ((x0 + x1) / 2, yy + 104), lab, font('800', 26), GOLD_L if gi == 1 else WHITE, clamp(gp) * mainA, anchor='mm')
    # end card
    if endp > 0:
        def ea(k): return ease_out(prog(t, 10.4 + k * .15, .45))
        text(L, (W / 2, 290), 'ATAL TUNNEL · SISSU', font('800', 34), GOLD, ea(0), anchor='mm', dy=20 * (1 - ea(0)))
        text(L, (W / 2, 380), 'No Rohtang permit needed', font('800', 76), WHITE, ea(1), anchor='mm', dy=24 * (1 - ea(1)))
        text(L, (W / 2, 470), 'We check the road and snow the evening before', font('500', 36), (220, 230, 240), ea(2), anchor='mm')
        bp = ease_back(prog(t, 10.9, .5))
        if bp > 0:
            f = font('800', 52); w = f.getlength('Get Quote') + 120
            pill(L, (W / 2 - w / 2, 560), 'Get Quote', f, GOLD, NAVY, clamp(bp), pad=(60, 26), scale=clamp(bp, 0, 1.1))
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
