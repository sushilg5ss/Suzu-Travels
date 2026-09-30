#!/usr/bin/env python3
"""Suzu Mountain Kit — HyperFrames composition generator.

    python3 gen_media.py <mountains-hero|height-ladder|expeditions-hero|all>      section-level compositions (already rendered)
    python3 gen_media.py peak-hero <slug>        per-page hero      <- src/media/<slug>.json  "hero"
    python3 gen_media.py route-profile <slug>    per-page explainer <- src/media/<slug>.json  "profile"
    python3 gen_media.py peak-ladder <slug>      per-page explainer <- src/media/<slug>.json  "ladder"
    (src/media/<slug>.json holds the media spec; a "media" key inside src/pages/<slug>.json also works)

Compositions (1920x1080, 30 fps, silent, seamless loops):
  mountains-hero      hub hero: 4 photo scenes + rolling altitude read-out 3,000 -> 8,586 m + altitude gauge + spindrift
  height-ladder       explainer: India's height ladder — named summits placed at their true heights, climber route
  expeditions-hero    /adventure/himalayan-peak-expeditions/ hero: ROPE UP / HIGH CAMP / SUMMIT DAY / HOME SAFE
  peak-hero           media.hero.steps -> photo hero with rolling altitude read-out (start -> summit)
                      media.hero.words -> photo hero with 4 big two-word lines (guides: permits, courses, records …)
  route-profile       media.profile.camps -> animated altitude profile, camp by camp
  peak-ladder         media.ladder.peaks (3-7 ids from data/peaks.json) -> those summits at their true heights

Writes $MK_HF_OUT/<name>/index.html plus assets/ (fonts, photos). Render + encode with make_media.sh.
Rules: photos are free-licence (Pexels, listed in hf/photos/CREDITS.md) and NEVER captioned as a named peak unless
CREDITS.md says the photo shows that peak; text stays in the right 55% of the frame (the page's tagline sits on the left).
"""
import html as _html, json, os, random, shutil, sys, pathlib

KIT = pathlib.Path(__file__).resolve().parent
HF = KIT / "hf"
OUT_ROOT = pathlib.Path(os.environ.get("MK_HF_OUT", str(KIT.parent.parent / "mk-hf")))
W, H = 1920, 1080
GSAP = "https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"

FONTS = """
@font-face{font-family:"SZ";src:url("assets/pjs-800.woff2") format("woff2");font-weight:800}
@font-face{font-family:"SZ";src:url("assets/pjs-700.woff2") format("woff2");font-weight:700}
@font-face{font-family:"SZ";src:url("assets/pjs-500.woff2") format("woff2");font-weight:500}
*{margin:0;padding:0;box-sizing:border-box}
html,body{margin:0;width:1920px;height:1080px;overflow:hidden;background:#06121f}
#root{position:relative;width:100%;height:100%;overflow:hidden;font-family:"SZ",sans-serif}
"""


def prep(name, photos=()):
    d = OUT_ROOT / name
    (d / "assets").mkdir(parents=True, exist_ok=True)
    for f in (HF / "assets").glob("*.woff2"):
        shutil.copy(f, d / "assets" / f.name)
    for p in photos:
        shutil.copy(HF / "photos" / p, d / "assets" / p)
    shutil.copy(HF / "hyperframes.json", d / "hyperframes.json")
    (d / "meta.json").write_text(json.dumps({"id": name, "name": name}))
    return d


def snow_layers(dur, seed=5):
    """Two periodic spindrift layers (SVG patterns). Far layer moves 1 tile, near layer 2 tiles per loop => seamless."""
    r = random.Random(seed)
    def pattern(pid, n, rmin, rmax, omin, omax):
        c = "".join(f'<circle cx="{r.uniform(0, W):.0f}" cy="{r.uniform(0, H):.0f}" r="{r.uniform(rmin, rmax):.1f}" fill="#fff" opacity="{r.uniform(omin, omax):.2f}"/>' for _ in range(n))
        return f'<pattern id="{pid}" width="{W}" height="{H}" patternUnits="userSpaceOnUse">{c}</pattern>'
    far = f'<svg class="snow" id="snowfar" width="{2*W}" height="{2*H}" style="left:0;top:{-H}px"><defs>{pattern("pf", 70, 1.2, 2.6, .25, .6)}</defs><rect width="{2*W}" height="{2*H}" fill="url(#pf)"/></svg>'
    near = f'<svg class="snow" id="snownear" width="{3*W}" height="{3*H}" style="left:0;top:{-2*H}px"><defs>{pattern("pn", 30, 2.8, 5.6, .5, .9)}</defs><rect width="{3*W}" height="{3*H}" fill="url(#pn)"/></svg>'
    js = (f'tl.fromTo("#snowfar",{{x:0,y:0}},{{x:{-W},y:{H},duration:{dur},ease:"none"}},0);'
          f'tl.fromTo("#snownear",{{x:0,y:0}},{{x:{-2*W},y:{2*H},duration:{dur},ease:"none"}},0);')
    return far + near, js


# --------------------------------------------------------------------------------------------
# Photo hero with rolling altitude read-out (hub)
# --------------------------------------------------------------------------------------------
def photo_scene_html(i, sc, dur):
    if sc["kind"] == "tilt":  # portrait photo, 1920 wide, starts bottom-aligned
        h = sc["h"]
        style = f'left:0;top:{H - h}px;width:{W}px;height:{h}px'
    else:  # landscape 2112 wide, centred
        w, h = sc.get("w", 2112), sc["h"]
        style = f'left:{(W - w) // 2}px;top:{(H - h) // 2}px;width:{w}px;height:{h}px'
    if sc.get("mirror"):
        return (f'<div class="clip" style="position:absolute;inset:0;transform:scaleX(-1)" data-start="0" data-duration="{dur}" data-track-index="{i}">'
                f'<img id="p{i}" class="ph" src="assets/{sc["img"]}" style="{style}" /></div>')
    return f'<img id="p{i}" class="ph clip" src="assets/{sc["img"]}" style="{style}" data-start="0" data-duration="{dur}" data-track-index="{i}" />'


def photo_scene_js(scenes, dur, xf=0.6):
    js = []
    n = len(scenes)
    for i, sc in enumerate(scenes):
        a, b = sc["t"]
        f, t = sc["from"], sc["to"]
        if i == 0:
            js.append(f'tl.set("#p0",{{opacity:1,scale:{f.get("scale",1)},x:{f.get("x",0)},y:{f.get("y",0)}}},0);')
            js.append(f'tl.to("#p0",{{scale:{t.get("scale",1)},x:{t.get("x",0)},y:{t.get("y",0)},duration:{b - a},ease:"none"}},0);')
            # hide after next scene fully in, then return for the loop at the end (static, same as frame 0)
            nxt = scenes[1]["t"][0] + xf
            js.append(f'tl.set("#p0",{{opacity:0}},{nxt + .05});')
            js.append(f'tl.set("#p0",{{scale:{f.get("scale",1)},x:{f.get("x",0)},y:{f.get("y",0)}}},{nxt + .1});')
            js.append(f'tl.set("#p0",{{opacity:1}},{dur - xf - .3});')
        else:
            js.append(f'tl.set("#p{i}",{{opacity:0,scale:{f.get("scale",1)},x:{f.get("x",0)},y:{f.get("y",0)}}},0);')
            js.append(f'tl.to("#p{i}",{{opacity:1,duration:{xf},ease:"none"}},{a});')
            js.append(f'tl.to("#p{i}",{{scale:{t.get("scale",1)},x:{t.get("x",0)},y:{t.get("y",0)},duration:{b - a},ease:"none"}},{a});')
            if i < n - 1:
                nxt = scenes[i + 1]["t"][0] + xf
                js.append(f'tl.set("#p{i}",{{opacity:0}},{nxt + .05});')
            else:  # last scene fades out on top of scene 0 => seamless loop
                js.append(f'tl.to("#p{i}",{{opacity:0,duration:{xf + .2},ease:"none"}},{dur - xf - .2});')
    return "".join(js)


def photo_hero(name, scenes, vals, caps, alts, times, kicker="MOUNTAINS OF INDIA", DUR=14, gauge=(3000, 8586)):
    """Photo scenes + rolling altitude read-out + gauge. vals/caps/alts/times: one entry per step (times[0] is None)."""
    NH, CH = 212, 50
    GY0, GY1 = 850, 250   # gauge y for gauge[0] and gauge[1]
    LO, HI = gauge

    def gy(a):
        return GY0 - (a - LO) / (HI - LO) * (GY0 - GY1)

    ticks = "".join(
        f'<div class="tk" style="top:{gy(a) - 1:.0f}px"></div><div class="tl" style="top:{gy(a) - 13:.0f}px">{a // 1000}k</div>'
        for a in range((LO // 1000 + (1 if LO % 1000 else 0)) * 1000, HI, 1000) if HI - a > 250)
    ticks += f'<div class="tk top" style="top:{gy(HI) - 1:.0f}px"></div><div class="tl gold" style="top:{gy(HI) - 13:.0f}px">{HI}</div>'
    snow_html, snow_js = snow_layers(DUR)
    d = prep(name, [s["img"] for s in scenes])
    num_strip = "".join(f"<div>{v}</div>" for v in vals)
    cap_strip = "".join(f"<div>{c}</div>" for c in caps)

    js = [photo_scene_js(scenes, DUR), snow_js]
    for k in range(1, len(vals)):
        t = times[k]
        roll = .7 if k == len(vals) - 1 else .5
        js.append(f'tl.to("#ns",{{y:{-k * NH},duration:{roll},ease:"power3.inOut"}},{t});')
        js.append(f'tl.to("#cs",{{y:{-k * CH},duration:{roll},ease:"power3.inOut"}},{t + .06});')
        js.append(f'tl.to("#mk",{{y:{gy(alts[k]) - gy(alts[0]):.1f},duration:{roll + .15},ease:"power2.inOut"}},{t});')
    # gold flash at the crown
    js.append(f'tl.fromTo("#crown",{{opacity:0,scaleX:0}},{{opacity:1,scaleX:1,duration:.5,ease:"power2.out"}},{times[-2] + .2});')
    js.append(f'tl.to("#crown",{{opacity:0,duration:.4}},{times[-1] - .15});')
    js.append(f'tl.fromTo("#bar",{{scaleX:0}},{{scaleX:1,duration:{times[-1] - .6:.2f},ease:"none"}},.2);tl.to("#bar",{{opacity:0,duration:.3}},{times[-1] - .2:.2f});tl.set("#bar",{{scaleX:0,opacity:1}},{times[-1] + .2:.2f});')

    html = f'''<!doctype html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width={W}, height={H}">
<script src="{GSAP}"></script>
<style>{FONTS}
.ph{{position:absolute;object-fit:cover;opacity:0;transform-origin:50% 50%}}
.shade{{position:absolute;inset:0;background:linear-gradient(90deg,rgba(6,18,31,.30) 0%,rgba(6,18,31,.10) 40%,rgba(6,18,31,.55) 64%,rgba(6,18,31,.88) 100%)}}
.vig{{position:absolute;inset:0;background:radial-gradient(ellipse at 40% 45%,rgba(0,0,0,0) 55%,rgba(0,0,0,.35) 100%)}}
.snow{{position:absolute}}
.hud{{position:absolute;right:190px;top:236px;width:760px;text-align:right;color:#fff}}
.kick{{font-size:27px;font-weight:800;letter-spacing:.34em;color:#f3d98f;margin-bottom:18px}}
.nwin{{height:{NH}px;overflow:hidden;position:relative}}
.nstrip div{{height:{NH}px;line-height:{NH}px;font-size:168px;font-weight:800;letter-spacing:-.02em;font-variant-numeric:tabular-nums;text-shadow:0 8px 40px rgba(0,0,0,.45)}}
.unit{{position:absolute;right:-78px;top:118px;font-size:60px;font-weight:800;color:#d4a24c}}
.cwin{{height:{CH}px;overflow:hidden;margin-top:6px}}
.cstrip div{{height:{CH}px;line-height:{CH}px;font-size:34px;font-weight:700;letter-spacing:.14em;color:rgba(255,255,255,.9)}}
.bar{{height:6px;width:420px;margin:18px 0 0 auto;background:#d4a24c;border-radius:3px;transform-origin:100% 50%}}
.crown{{position:absolute;right:190px;top:{236 + 45 + NH - 8}px;width:560px;height:4px;background:linear-gradient(90deg,rgba(243,217,143,0),#f3d98f);transform-origin:100% 50%;opacity:0}}
.gauge{{position:absolute;left:1808px;top:0;width:90px;height:{H}px}}
.gline{{position:absolute;left:44px;top:{GY1}px;width:2px;height:{GY0 - GY1}px;background:linear-gradient(180deg,#f3d98f,rgba(255,255,255,.55))}}
.tk{{position:absolute;left:36px;width:18px;height:2px;background:rgba(255,255,255,.7)}}
.tk.top{{background:#f3d98f;width:22px;left:34px}}
.tl{{position:absolute;left:-10px;width:40px;text-align:right;font-size:18px;font-weight:700;color:rgba(255,255,255,.75)}}
.tl.gold{{color:#f3d98f;left:-26px;width:56px}}
.mk{{position:absolute;left:26px;top:{gy(alts[0]) - 12:.0f}px;width:0;height:0;border-top:12px solid transparent;border-bottom:12px solid transparent;border-left:18px solid #d4a24c;filter:drop-shadow(0 0 10px rgba(212,162,76,.8))}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="{W}" data-height="{H}">
{"".join(photo_scene_html(i, s, DUR) for i, s in enumerate(scenes))}
<div class="vig clip" data-start="0" data-duration="{DUR}" data-track-index="10"></div>
<div class="clip" data-start="0" data-duration="{DUR}" data-track-index="11" style="position:absolute;inset:0;overflow:hidden">{snow_html}</div>
<div class="shade clip" data-start="0" data-duration="{DUR}" data-track-index="12"></div>
<div class="hud clip" data-start="0" data-duration="{DUR}" data-track-index="13">
  <div class="kick">{kicker}</div>
  <div style="position:relative;display:inline-block;width:640px"><div class="nwin"><div class="nstrip" id="ns">{num_strip}</div></div><div class="unit">m</div></div>
  <div class="cwin"><div class="cstrip" id="cs">{cap_strip}</div></div>
  <div class="bar" id="bar"></div>
</div>
<div id="crown" class="crown clip" data-start="0" data-duration="{DUR}" data-track-index="14"></div>
<div class="gauge clip" data-start="0" data-duration="{DUR}" data-track-index="15"><div class="gline"></div>{ticks}<div class="mk" id="mk"></div></div>
</div>
<script>
const tl = gsap.timeline({{ paused: true }});
{"".join(js)}
window.__timelines = window.__timelines || {{}};
window.__timelines["main"] = tl;
tl.seek(0);
</script></body></html>'''
    (d / "index.html").write_text(html, encoding="utf-8")
    return d


def mountains_hero():
    scenes = [
        {"img": "px-38930225.jpg", "kind": "land", "h": 1188, "t": (0, 4.0), "from": {"scale": 1.0}, "to": {"scale": 1.09, "x": -30}},
        {"img": "px-37358046.jpg", "kind": "tilt", "h": 2880, "t": (3.4, 7.6), "from": {"y": 250}, "to": {"y": 1320}},
        {"img": "px-38468349.jpg", "kind": "land", "h": 1406, "mirror": True, "t": (7.0, 10.8), "from": {"scale": 1.04, "x": 30, "y": -20}, "to": {"scale": 1.13, "x": -30, "y": 30}},
        {"img": "px-30701907.jpg", "kind": "land", "h": 1408, "t": (10.2, 14.0), "from": {"scale": 1.08, "x": -150}, "to": {"scale": 1.15, "x": -215}},
    ]
    vals = ["3,000", "4,000", "5,000", "6,000", "7,000", "8,000", "8,586", "3,000"]
    caps = ["HILL SUMMITS", "HIGH PASSES &amp; SUMMITS", "TREKKING PEAKS", "EXPEDITION PEAKS", "THE SEVEN-THOUSANDERS", "ABOVE 8,000 m", "INDIA&#8217;S HIGHEST SUMMIT", "HILL SUMMITS"]
    alts = [3000, 4000, 5000, 6000, 7000, 8000, 8586, 3000]
    times = [None, 1.7, 3.7, 5.5, 7.3, 10.4, 11.7, 13.25]
    return photo_hero("mountains-hero", scenes, vals, caps, alts, times)


# --------------------------------------------------------------------------------------------
# Expeditions hero (commercial page)
# --------------------------------------------------------------------------------------------
def expeditions_hero():
    scenes = [
        {"img": "px-32109154.jpg", "kind": "tilt", "h": 2560, "t": (0, 3.6), "from": {"y": 0}, "to": {"y": 520}},
        {"img": "px-20809686.jpg", "kind": "tilt", "h": 2560, "t": (3.0, 6.8), "from": {"y": 820, "scale": 1.0}, "to": {"y": 940, "scale": 1.06}},
        {"img": "px-9683997.jpg", "kind": "land", "h": 1408, "t": (6.2, 10.0), "from": {"scale": 1.02, "x": 60, "y": 30}, "to": {"scale": 1.12, "x": -20, "y": 70}},
        {"img": "px-38468355.jpg", "kind": "land", "h": 1406, "t": (9.4, 13.0), "from": {"scale": 1.1, "x": -150}, "to": {"scale": 1.16, "x": -230}},
    ]
    words = [("ROPE", "UP."), ("HIGH", "CAMP."), ("SUMMIT", "DAY."), ("HOME", "SAFE.")]
    return words_hero("expeditions-hero", scenes, words, "GUIDED PEAK CLIMBS")


def words_hero(name, scenes, words, kicker, DUR=13, seed=11):
    """Photo scenes + four big two-word lines (white word + gold word), one per scene. Keep each word <= 9 letters."""
    n = len(words)
    wt = [0.25 + i * (DUR - 0.25) / n for i in range(n)]
    snow_html, snow_js = snow_layers(DUR, seed=seed)
    d = prep(name, [s["img"] for s in scenes])
    wh = "".join(f'<div class="w clip" id="w{i}" data-start="0" data-duration="{DUR}" data-track-index="{20 + i}"><span>{a}</span> <b>{b}</b></div>' for i, (a, b) in enumerate(words))
    js = [photo_scene_js(scenes, DUR), snow_js]
    for i, t in enumerate(wt):
        js.append(f'tl.fromTo("#w{i}",{{opacity:0,y:50}},{{opacity:1,y:0,duration:.6,ease:"power3.out"}},{t:.2f});')
        js.append(f'tl.to("#w{i}",{{opacity:0,y:-36,duration:.45,ease:"power2.in"}},{t + 2.6:.2f});')
    js.append(f'tl.fromTo("#kick",{{opacity:0}},{{opacity:1,duration:.6}},.1);tl.to("#kick",{{opacity:0,duration:.4}},{DUR - .6:.2f});')
    js.append(f'tl.fromTo("#bar",{{scaleX:0}},{{scaleX:1,duration:{DUR - .9:.2f},ease:"none"}},.2);tl.to("#bar",{{opacity:0,duration:.3}},{DUR - .6:.2f});')
    html = f'''<!doctype html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width={W}, height={H}">
<script src="{GSAP}"></script>
<style>{FONTS}
.ph{{position:absolute;object-fit:cover;opacity:0;transform-origin:50% 50%}}
.shade{{position:absolute;inset:0;background:linear-gradient(90deg,rgba(6,18,31,.28) 0%,rgba(6,18,31,.08) 38%,rgba(6,18,31,.55) 62%,rgba(6,18,31,.86) 100%)}}
.snow{{position:absolute}}
.kick{{position:absolute;right:150px;top:170px;font-size:27px;font-weight:800;letter-spacing:.32em;color:#f3d98f;opacity:0}}
.w{{position:absolute;right:146px;top:220px;font-size:150px;font-weight:800;letter-spacing:-.02em;color:#fff;opacity:0;text-align:right;line-height:1.02;text-shadow:0 8px 40px rgba(0,0,0,.5)}}
.w span{{display:block}} .w b{{display:block;color:#f3d98f}}
.bar{{position:absolute;right:150px;top:572px;height:6px;width:420px;background:#d4a24c;border-radius:3px;transform-origin:100% 50%}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="{W}" data-height="{H}">
{"".join(photo_scene_html(i, s, DUR) for i, s in enumerate(scenes))}
<div class="clip" data-start="0" data-duration="{DUR}" data-track-index="11" style="position:absolute;inset:0;overflow:hidden">{snow_html}</div>
<div class="shade clip" data-start="0" data-duration="{DUR}" data-track-index="12"></div>
<div id="kick" class="kick clip" data-start="0" data-duration="{DUR}" data-track-index="13">{kicker}</div>
{wh}
<div id="bar" class="bar clip" data-start="0" data-duration="{DUR}" data-track-index="30"></div>
</div>
<script>
const tl = gsap.timeline({{ paused: true }});
{"".join(js)}
window.__timelines = window.__timelines || {{}};
window.__timelines["main"] = tl;
tl.seek(0);
</script></body></html>'''
    (d / "index.html").write_text(html, encoding="utf-8")
    return d


# --------------------------------------------------------------------------------------------
# Height ladder explainer (vector, no photos)
# --------------------------------------------------------------------------------------------
LADDER = [  # name, height, sub-label   (hub composition; heights match data/peaks.json)
    ("Churdhar", 3647, "Himachal"),
    ("Friendship Peak", 5289, "Himachal"),
    ("Deo Tibba", 6001, "Himachal"),
    ("Reo Purgyil", 6816, "Himachal&#8217;s highest"),
    ("Kamet", 7756, "Uttarakhand"),
    ("Nanda Devi", 7816, "Highest wholly in India"),
    ("Kangchenjunga", 8586, "India&#8217;s highest"),
]


def height_ladder():
    n_peaks = len(json.loads((KIT / "data" / "peaks.json").read_text(encoding="utf-8")))
    return ladder_comp("height-ladder", LADDER, "INDIA&#8217;S HEIGHT LADDER", "From hill summits to the 8,586 m crown",
                       f"{n_peaks} peaks · heights · first ascents · climbing status", "suzutravels.com/mountains-of-india", lo=2500, hi=8800)


def ladder_comp(name, items, kicker, title, end_a, end_b, DUR=16, lo=None, hi=None):
    """items: [(name, height_m, sub_label)], 3-7 of them; drawn left->right in ascending height at their true altitudes.
    The scale is fitted to the heights (lowest ~24% up, highest ~93% up, at least 2,000 m of scale) unless lo/hi are given."""
    items = sorted(items, key=lambda t: t[1])
    n = len(items)
    ms = [m for _, m, _ in items]
    if lo is None or hi is None:
        span = max((max(ms) - min(ms)) / 0.69, 2000)
        lo = int((min(ms) - 0.24 * span) // 100 * 100)
        hi = int(lo + span + 99) // 100 * 100
    span = hi - lo
    Y0, Y1 = 960, 190

    def y(a):
        return Y0 - (a - lo) / (hi - lo) * (Y0 - Y1)
    xs = [330 + (1710 - 330) * i / (n - 1) for i in range(n)] if n > 1 else [1020]
    # ridge profile: start low left, summits at named heights, saddles between them
    pts = [(-20, y(lo + .016 * span)), (150, y(lo + .08 * span))]
    prev = None
    for (nm, a, st), x in zip(items, xs):
        if prev:
            px, pa = prev
            sad = min(pa, a) - (.06 if (a - lo) / span < .55 else .1) * span
            pts.append(((px + x) / 2, y(max(lo + .03 * span, sad))))
        pts.append((x, y(a)))
        prev = (x, a)
    pts += [(xs[-1] + 50, y(ms[-1] - .39 * span)), (1940, y(ms[-1] - .53 * span)), (1940, 1100), (-20, 1100)]
    d_ridge = "M" + " L".join(f"{px:.0f} {py:.0f}" for px, py in pts) + " Z"
    # snow caps on the upper summits
    caps = []
    for (nm, a, st), x in zip(items, xs):
        fr = (a - lo) / span
        if fr > .38:
            sy = y(a)
            k = 26 + (fr - .38) * 150
            caps.append(f'<path d="M{x - k:.0f} {sy + k * .9:.0f} L{x:.0f} {sy:.0f} L{x + k:.0f} {sy + k * .9:.0f} L{x + k * .45:.0f} {sy + k * .72:.0f} L{x + k * .1:.0f} {sy + k * .95:.0f} L{x - k * .35:.0f} {sy + k * .7:.0f} Z" fill="#eef4f8"/>')
    gstep = 1000 if span > 3500 else 500
    grid = ""
    for a in range((lo // gstep + 1) * gstep, hi, gstep):
        grid += f'<div class="gl" style="top:{y(a):.0f}px"></div><div class="gt" style="top:{y(a) - 30:.0f}px">{a:,} m</div>'
    markers, js = "", []
    route = [(150, y(lo + .08 * span))] + [(x, y(a)) for (_, a, _), x in zip(items, xs)]
    t0 = 4.2
    step = min(1.3, 6.3 / max(1, n - 1))
    for i, ((nm, a, st), x) in enumerate(zip(items, xs)):
        my = y(a)
        top_ = i == n - 1
        lw = 226
        lab = f'left:{x - lw // 2:.0f}px;top:{my + 24:.0f}px;width:{lw}px'
        big = " big" if top_ else ""
        markers += (f'<div class="dot{big}" id="d{i}" style="left:{x - 11:.0f}px;top:{my - 11:.0f}px"></div>'
                    f'<div class="lab{big}" id="l{i}" style="{lab}"><div class="h">{a:,} m</div><div class="n">{nm}</div><div class="s">{st}</div></div>')
        t = t0 + i * step
        js.append(f'tl.fromTo("#d{i}",{{scale:0,opacity:0}},{{scale:1,opacity:1,duration:.35,ease:"back.out(2.2)"}},{t:.2f});')
        js.append(f'tl.fromTo("#l{i}",{{opacity:0,y:14}},{{opacity:1,y:0,duration:.4,ease:"power2.out"}},{t + .08:.2f});')
    # climber moving along the route (piecewise)
    js.append(f'tl.set("#cl",{{x:{route[0][0] - 9:.0f},y:{route[0][1] - 9:.0f},opacity:0}},0);tl.to("#cl",{{opacity:1,duration:.3}},{t0 - .7:.2f});')
    for i in range(1, len(route)):
        x, yy = route[i]
        js.append(f'tl.to("#cl",{{x:{x - 9:.0f},y:{yy - 9:.0f},duration:{step - .05 if i > 1 else .6:.2f},ease:"power1.inOut"}},{t0 - .65 + (i - 1) * step if i > 1 else t0 - .65:.2f});')
    poly = " ".join(f"{px:.0f},{py:.0f}" for px, py in route)
    total = sum(((route[i][0] - route[i - 1][0]) ** 2 + (route[i][1] - route[i - 1][1]) ** 2) ** .5 for i in range(1, len(route)))
    js.append(f'tl.fromTo("#rline",{{strokeDashoffset:{total:.0f}}},{{strokeDashoffset:0,duration:{step * (len(route) - 1):.2f},ease:"none"}},{t0 - .65:.2f});')
    tend = t0 + (n - 1) * step + .6
    js.insert(0, 'tl.fromTo("#ttl",{opacity:0,y:20},{opacity:1,y:0,duration:.6,ease:"power2.out"},.2);')
    js.insert(1, 'tl.fromTo(".gl",{scaleX:0},{scaleX:1,duration:1.1,stagger:.08,ease:"power2.out"},.5);tl.fromTo(".gt",{opacity:0},{opacity:1,duration:.5,stagger:.08},.7);')
    js.insert(2, 'tl.fromTo("#massif",{y:500},{y:0,duration:1.8,ease:"power3.out"},1.3);tl.fromTo("#massif2",{y:520},{y:0,duration:2.0,ease:"power3.out"},1.2);')
    js.append(f'tl.fromTo("#halo",{{opacity:0,scale:.4}},{{opacity:1,scale:1,duration:.7,ease:"power2.out"}},{tend:.2f});')
    js.append(f'tl.fromTo("#end",{{opacity:0,y:16}},{{opacity:1,y:0,duration:.6}},{tend + .4:.2f});')
    js.append(f'tl.to("#all",{{opacity:0,duration:.6,ease:"none"}},{DUR - .6:.2f});')
    hx, hy = xs[-1], y(ms[-1])
    html = f'''<!doctype html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width={W}, height={H}">
<script src="{GSAP}"></script>
<style>{FONTS}
html,body{{background:#06121f}}
.bg{{position:absolute;inset:0;background:radial-gradient(ellipse at 78% 12%,#16395c 0%,#0b1f33 42%,#06121f 100%)}}
.topo{{position:absolute;inset:0;opacity:.10}}
#all{{position:absolute;inset:0}}
.gl{{position:absolute;left:60px;width:1800px;height:1px;background:rgba(207,230,245,.22);transform-origin:0 50%}}
.gt{{position:absolute;left:64px;font-size:22px;font-weight:700;color:rgba(207,230,245,.6);letter-spacing:.04em}}
.dot{{position:absolute;width:22px;height:22px;border-radius:50%;background:#fff;border:5px solid #d4a24c;box-shadow:0 0 0 6px rgba(212,162,76,.25)}}
.dot.big{{background:#d4a24c;border-color:#fff}}
.lab{{position:absolute;color:#fff;text-align:center;background:rgba(6,18,31,.62);border:1px solid rgba(207,230,245,.18);border-radius:14px;padding:8px 10px 10px}}
.lab .h{{font-size:36px;font-weight:800;letter-spacing:-.01em;font-variant-numeric:tabular-nums}}
.lab .n{{font-size:24px;font-weight:700;color:#f3d98f;margin-top:2px}}
.lab .s{{font-size:18px;font-weight:500;color:rgba(207,230,245,.75);margin-top:2px}}
.lab.big .h{{font-size:46px;color:#f3d98f}} .lab.big{{border-color:rgba(243,217,143,.6)}} .lab.big .n{{color:#fff}}
#ttl{{position:absolute;left:64px;top:60px}}
#ttl .k{{font-size:24px;font-weight:800;letter-spacing:.32em;color:#d4a24c}}
#ttl .t{{font-size:56px;font-weight:800;color:#fff;margin-top:6px;letter-spacing:-.01em}}
#cl{{position:absolute;left:0;top:0;width:18px;height:18px;border-radius:50%;background:#ff5a36;box-shadow:0 0 0 7px rgba(255,90,54,.28),0 0 26px rgba(255,90,54,.8)}}
#halo{{position:absolute;left:{hx - 90:.0f}px;top:{hy - 90:.0f}px;width:180px;height:180px;border-radius:50%;background:radial-gradient(circle,rgba(243,217,143,.55),rgba(243,217,143,0) 70%)}}
#end{{position:absolute;left:64px;bottom:40px;text-align:left;color:#fff}}
#end .a{{font-size:30px;font-weight:800}} #end .b{{font-size:22px;font-weight:600;color:rgba(207,230,245,.8);margin-top:4px}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="{W}" data-height="{H}">
<div class="bg clip" data-start="0" data-duration="{DUR}" data-track-index="0"></div>
<svg class="topo clip" data-start="0" data-duration="{DUR}" data-track-index="1" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{topo_lines()}</svg>
<div id="all" class="clip" data-start="0" data-duration="{DUR}" data-track-index="2">
 {grid}
 <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="position:absolute;left:0;top:0">
  <defs><linearGradient id="rg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2d5b82"/><stop offset=".55" stop-color="#143452"/><stop offset="1" stop-color="#0a1d30"/></linearGradient>
  <linearGradient id="rg2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1b3f63" stop-opacity=".45"/><stop offset="1" stop-color="#0b1f33" stop-opacity=".2"/></linearGradient></defs>
  <g id="massif2"><path d="{back_ridge()}" fill="url(#rg2)"/></g>
  <g id="massif"><path d="{d_ridge}" fill="url(#rg)" stroke="rgba(207,230,245,.35)" stroke-width="2"/>{"".join(caps)}</g>
  <polyline id="rline" points="{poly}" fill="none" stroke="#ff7a50" stroke-width="4" stroke-dasharray="{total:.0f}" stroke-dashoffset="{total:.0f}" stroke-linecap="round" stroke-linejoin="round" opacity=".9"/>
 </svg>
 <div id="halo"></div>
 {markers}
 <div id="cl"></div>
 <div id="ttl"><div class="k">{kicker}</div><div class="t">{title}</div></div>
 <div id="end"><div class="a">{end_a}</div><div class="b">{end_b}</div></div>
</div>
</div>
<script>
const tl = gsap.timeline({{ paused: true }});
{"".join(js)}
window.__timelines = window.__timelines || {{}};
window.__timelines["main"] = tl;
tl.seek(0);
</script></body></html>'''
    d = prep(name)
    (d / "index.html").write_text(html, encoding="utf-8")
    return d


def back_ridge():
    r = random.Random(3)
    pts = [(-20, 760)]
    x = -20
    while x < 1960:
        x += r.uniform(70, 150)
        pts.append((x, r.uniform(600, 780)))
    pts += [(1960, 1100), (-20, 1100)]
    return "M" + " L".join(f"{a:.0f} {b:.0f}" for a, b in pts) + " Z"


def topo_lines():
    r = random.Random(9)
    out = []
    for k in range(14):
        cy = 120 + k * 70
        pts = []
        for i in range(0, 21):
            x = i * 100 - 40
            pts.append(f"{x},{cy + 26 * __import__('math').sin(i * .55 + k * .8) + r.uniform(-8, 8):.0f}")
        out.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="#cfe6f5" stroke-width="1.5"/>')
    return "".join(out)



# --------------------------------------------------------------------------------------------
# Per-page compositions for the Mountain agents (read src/media/<slug>.json, else src/pages/<slug>.json -> "media")
# --------------------------------------------------------------------------------------------
def page_spec(slug):
    """{"media": {...}} for a page: src/media/<slug>.json (written by the Visual Studio) or the "media" key of src/pages/<slug>.json."""
    m = KIT / "src" / "media" / f"{slug}.json"
    if m.exists():
        return {"media": json.loads(m.read_text(encoding="utf-8"))}
    f = KIT / "src" / "pages" / f"{slug}.json"
    if not f.exists():
        raise SystemExit(f"missing src/media/{slug}.json (and src/pages/{slug}.json)")
    return json.loads(f.read_text(encoding="utf-8"))


def esc(s):
    """Idempotent HTML escape for text that agents write into page JSON ("A & B" or "A &amp; B" both come out right)."""
    return _html.escape(_html.unescape(str(s)), quote=False)


def peak_hero(slug):
    """Photo hero for a peak or guide page. spec["media"]["hero"] = {
         "scenes": [ {img, kind: land|tilt, h, mirror?, t:[a,b], from:{}, to:{}} x 3-4 ]   photos from hf/photos/ (see CREDITS.md:
                     sizes, what each shows, which may be mirrored). NEVER caption a photo of another mountain as this peak.
         "kicker": "FRIENDSHIP PEAK · HIMACHAL",
         and EITHER "steps": [[altitude_m, "CAPTION"], ...]  3-7 steps, first = start (road-head / base camp), last = summit
                                                           -> rolling altitude read-out start -> summit -> start (peak pages)
         OR     "words": [["APPLY", "EARLY."], ["PAY THE", "PEAK FEE."], ...]  exactly 4 pairs, each word <= 9 letters
                                                           -> four big two-line statements (guide pages) }
    Scene times must tile the loop: first scene starts at 0, each next one starts ~0.6 s before the previous ends,
    the last ends at DUR (14 s for steps, 13 s for words)."""
    spec = page_spec(slug)["media"]["hero"]
    scenes = [{**sc, "t": tuple(sc["t"])} for sc in spec["scenes"]]
    kicker = esc(spec.get("kicker", "MOUNTAINS OF INDIA"))
    if spec.get("words"):
        words = [(esc(a), esc(b)) for a, b in spec["words"]]
        return words_hero(f"{slug}-hero", scenes, words, kicker, DUR=round(max(sc["t"][1] for sc in scenes)))
    if not 3 <= len(spec["steps"]) <= 7:
        raise SystemExit("media.hero.steps needs 3-7 [altitude, caption] pairs")
    steps = spec["steps"] + [spec["steps"][0]]
    vals = [f"{a:,}" for a, _ in steps]
    caps = [esc(c) for _, c in steps]
    alts = [a for a, _ in steps]
    n = len(steps) - 1
    times = [None] + [round(1.5 + (11.2 / (n - 1)) * i, 2) for i in range(n - 1)] + [13.25]
    lo = (min(alts) // 1000) * 1000
    hi = max(alts)
    return photo_hero(f"{slug}-hero", scenes, vals, caps, alts, times, kicker=kicker, gauge=(lo, hi))


def peak_ladder(slug):
    """Summits at their true heights. spec["media"]["ladder"] = {
         "kicker": "INDIA'S 7,000 m PEAKS", "title": "The seven-thousanders, side by side",
         "peaks": ["kamet", "nanda-devi", ...]   3-7 ids from data/peaks.json (heights + names are read from the dataset),
         "subs": {"nanda-devi": "Closed since 1983"}   optional sub-labels (default: the peak's state),
         "end": "48 peaks above 7,000 m in our list"   optional end-card line }"""
    spec = page_spec(slug)["media"]["ladder"]
    data = {p["id"]: p for p in json.loads((KIT / "data" / "peaks.json").read_text(encoding="utf-8"))}
    ids = spec["peaks"]
    if not 3 <= len(ids) <= 7:
        raise SystemExit("media.ladder.peaks needs 3-7 peak ids")
    missing = [i for i in ids if i not in data]
    if missing:
        raise SystemExit(f"unknown peak ids: {missing}")
    subs = spec.get("subs", {})
    items = [(esc(data[i]["name"]), data[i]["m"], esc(subs.get(i, data[i]["state_label"]))) for i in ids]
    return ladder_comp(f"{slug}-ladder", items, esc(spec.get("kicker", "MOUNTAINS OF INDIA")), esc(spec.get("title", "")),
                       esc(spec.get("end", f"{len(data)} peaks · heights · first ascents · climbing status")), "suzutravels.com/mountains-of-india")


def route_profile(slug):
    """Altitude-profile explainer. spec["media"]["profile"] = {
         "title": "Friendship Peak route", "sub": "Manali to the 5,289 m summit",
         "camps": [ {"name": "Manali", "m": 2050, "day": "Day 1"}, ..., {"name": "Summit", "m": 5289, "day": "Day 6"} ] }
       Every altitude must come from the page's fact pack (research), never guessed."""
    spec = page_spec(slug)["media"]["profile"]
    camps = spec["camps"]
    DUR = 12
    lo = (min(c["m"] for c in camps) // 1000) * 1000
    hi = ((max(c["m"] for c in camps) + 300) // 1000 + 1) * 1000   # >= 300 m headroom above the summit label
    X0, X1, Y0, Y1 = 270, 1760, 900, 250

    def y(a):
        return Y0 - (a - lo) / (hi - lo) * (Y0 - Y1)
    xs = [X0 + (X1 - X0) * i / (len(camps) - 1) for i in range(len(camps))]
    pts = [(x, y(c["m"])) for x, c in zip(xs, camps)]
    grid = "".join(f'<div class="gl" style="top:{y(a):.0f}px"></div><div class="gt" style="top:{y(a) - 28:.0f}px">{a:,} m</div>' for a in range(lo, hi + 1, 1000))
    poly = " ".join(f"{a:.0f},{b:.0f}" for a, b in pts)
    area = f"M{X0} {Y0} " + " ".join(f"L{a:.0f} {b:.0f}" for a, b in pts) + f" L{X1} {Y0} Z"
    total = sum(((pts[i][0] - pts[i - 1][0]) ** 2 + (pts[i][1] - pts[i - 1][1]) ** 2) ** .5 for i in range(1, len(pts)))
    step = 7.0 / (len(camps) - 1)
    labs, js = "", []
    for i, ((x, yy), c) in enumerate(zip(pts, camps)):
        above = (i % 2 == 0) or i == len(camps) - 1
        top = yy - 136 if above else yy + 26
        top = max(150, min(top, Y0 - 100))
        last = " big" if i == len(camps) - 1 else ""
        labs += (f'<div class="dot{last}" id="d{i}" style="left:{x - 11:.0f}px;top:{yy - 11:.0f}px"></div>'
                 f'<div class="lab{last}" id="l{i}" style="left:{x - 110:.0f}px;top:{top:.0f}px"><div class="h">{c["m"]:,} m</div><div class="n">{esc(c["name"])}</div><div class="s">{esc(c.get("day", ""))}</div></div>')
        t = 1.6 + i * step
        js.append(f'tl.fromTo("#d{i}",{{scale:0,opacity:0}},{{scale:1,opacity:1,duration:.3,ease:"back.out(2)"}},{t:.2f});')
        js.append(f'tl.fromTo("#l{i}",{{opacity:0,y:12}},{{opacity:1,y:0,duration:.35}},{t + .05:.2f});')
    js.append(f'tl.fromTo("#rl",{{strokeDashoffset:{total:.0f}}},{{strokeDashoffset:0,duration:{7.0:.2f},ease:"none"}},1.6);')
    js.append('tl.fromTo("#area",{opacity:0},{opacity:1,duration:1.2},1.2);')
    js.append('tl.fromTo("#ttl",{opacity:0,y:16},{opacity:1,y:0,duration:.6},.2);tl.fromTo(".gl",{scaleX:0},{scaleX:1,duration:1,stagger:.06},.4);tl.fromTo(".gt",{opacity:0},{opacity:1,duration:.4,stagger:.06},.6);')
    js.append(f'tl.to("#all",{{opacity:0,duration:.6}},{DUR - .6});')
    html = f'''<!doctype html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width={W}, height={H}">
<script src="{GSAP}"></script>
<style>{FONTS}
.bg{{position:absolute;inset:0;background:radial-gradient(ellipse at 80% 10%,#16395c 0%,#0b1f33 45%,#06121f 100%)}}
#all{{position:absolute;inset:0}}
.gl{{position:absolute;left:{X0 - 40}px;width:{X1 - X0 + 80}px;height:1px;background:rgba(207,230,245,.2);transform-origin:0 50%}}
.gt{{position:absolute;left:40px;font-size:22px;font-weight:700;color:rgba(207,230,245,.6)}}
.dot{{position:absolute;width:22px;height:22px;border-radius:50%;background:#fff;border:5px solid #d4a24c}}
.dot.big{{background:#d4a24c;border-color:#fff;box-shadow:0 0 0 10px rgba(212,162,76,.25)}}
.lab{{position:absolute;width:220px;text-align:center;color:#fff;background:rgba(6,18,31,.66);border:1px solid rgba(207,230,245,.18);border-radius:14px;padding:8px 8px 10px}}
.lab .h{{font-size:32px;font-weight:800;font-variant-numeric:tabular-nums}} .lab .n{{font-size:21px;font-weight:700;color:#f3d98f}} .lab .s{{font-size:17px;color:rgba(207,230,245,.75)}}
.lab.big{{border-color:rgba(243,217,143,.6)}} .lab.big .h{{color:#f3d98f;font-size:40px}}
#ttl{{position:absolute;left:60px;top:54px}} #ttl .k{{font-size:24px;font-weight:800;letter-spacing:.3em;color:#d4a24c}} #ttl .t{{font-size:52px;font-weight:800;color:#fff;margin-top:4px}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="{W}" data-height="{H}">
<div class="bg clip" data-start="0" data-duration="{DUR}" data-track-index="0"></div>
<div id="all" class="clip" data-start="0" data-duration="{DUR}" data-track-index="1">{grid}
<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="position:absolute;left:0;top:0"><defs><linearGradient id="ag" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2f78b7" stop-opacity=".55"/><stop offset="1" stop-color="#0b1f33" stop-opacity=".1"/></linearGradient></defs>
<path id="area" d="{area}" fill="url(#ag)"/><polyline id="rl" points="{poly}" fill="none" stroke="#f3d98f" stroke-width="5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="{total:.0f}" stroke-dashoffset="{total:.0f}"/></svg>
{labs}
<div id="ttl"><div class="k">ALTITUDE PROFILE</div><div class="t">{esc(spec.get("title", ""))}</div></div>
</div></div>
<script>
const tl = gsap.timeline({{ paused: true }});
{"".join(js)}
window.__timelines = window.__timelines || {{}};
window.__timelines["main"] = tl;
tl.seek(0);
</script></body></html>'''
    d = prep(f"{slug}-profile")
    (d / "index.html").write_text(html, encoding="utf-8")
    return d

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which == "peak-hero":
        print(peak_hero(sys.argv[2]))
    elif which == "route-profile":
        print(route_profile(sys.argv[2]))
    elif which == "peak-ladder":
        print(peak_ladder(sys.argv[2]))
    else:
        fns = {"mountains-hero": mountains_hero, "height-ladder": height_ladder, "expeditions-hero": expeditions_hero}
        for k, f in fns.items():
            if which in (k, "all"):
                print(f())
