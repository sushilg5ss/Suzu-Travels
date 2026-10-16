#!/usr/bin/env python3
"""Suzu Inbound Kit — HyperFrames composition generator for the "India for international travellers" section.

    python3 gen_media.py photo-hero  <slug>   hero      <- src/media/<slug>.json "hero"   licensed photos, slow pans, caption steps
    python3 gen_media.py route-map   <slug>   explainer <- src/media/<slug>.json "route"  stops by lat/lon, English labels, day numbers
    python3 gen_media.py cost-ladder <slug>   explainer <- src/media/<slug>.json "cost"   what a trip includes, in words (US$ only from data/prices.json)

Field reference: src/media/_example-guide.json (a model file; `_` files are never rendered for real).

Rules (carried over from the pilgrim / mountain kits): 1920x1080, 30 fps, silent, seamless loop (last frame == first frame),
deterministic (no Math.random at runtime). Hero text stays in the RIGHT 55% of the frame; the LEFT 45% carries the photo
(on phones the page crops the hero to the left, object-position 15%, and prints its own H1). Explainers (route, cost) are
full-frame 16:9 and sit inside page sections. Writes $IK_HF_OUT/<name>/index.html + assets/. Render + encode with make_media.sh.

Honesty: every photo must be a file in hf/photos/ that has a row in hf/photos/CREDITS.md (checked here); a caption may name a
place only if that row's "allowed captions" says so (the Visual Studio checks this by hand — the generator cannot). Route maps
draw NO outline and NO state or national boundary lines: just a graticule, the stops and the line between them. Cost ladders
print a US$ figure only if it is in data/prices.json "allowed"; anything else is words only.
"""
import html as _html, json, math, os, random, re, shutil, sys, pathlib

KIT = pathlib.Path(__file__).resolve().parent
HF = KIT / "hf"
DATA = KIT / "data"
OUT_ROOT = pathlib.Path(os.environ.get("IK_HF_OUT", str(KIT.parent.parent / "ik-hf")))
W, H = 1920, 1080
GSAP = "https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"

# Himalaya-sky palette (matches kit.css .szi)
NAVY, NAVY2, GOLD, GOLD2, GOLD3, SAFF, IVORY = "#0b1f3a", "#06121f", "#d99a2b", "#f2c14e", "#ffe3a3", "#ff8a2a", "#f4f8fb"

FONTS = """
@font-face{font-family:"SZ";src:url("assets/pjs-800.woff2") format("woff2");font-weight:800}
@font-face{font-family:"SZ";src:url("assets/pjs-700.woff2") format("woff2");font-weight:700}
@font-face{font-family:"SZ";src:url("assets/pjs-500.woff2") format("woff2");font-weight:500}
@font-face{font-family:"CG";src:url("assets/cg-700.woff2") format("woff2");font-weight:700}
@font-face{font-family:"CG";src:url("assets/cg-600.woff2") format("woff2");font-weight:600}
*{margin:0;padding:0;box-sizing:border-box}
html,body{margin:0;width:1920px;height:1080px;overflow:hidden;background:#0b1f3a}
#root{position:relative;width:100%;height:100%;overflow:hidden;font-family:"SZ",sans-serif}
.lay{position:absolute;inset:0}
.kick{font:800 26px "SZ",sans-serif;letter-spacing:.34em;color:#f2c14e;text-transform:uppercase}
.mark{position:absolute;right:150px;bottom:84px;text-align:right}
.mark b{display:block;font:800 22px "SZ",sans-serif;letter-spacing:.32em;color:#ffe3a3}
.mark small{display:block;font:500 16px "SZ",sans-serif;letter-spacing:.12em;color:rgba(244,248,251,.72);margin-top:6px}
"""


def esc(s):
    """Idempotent HTML escape ("A & B" and "A &amp; B" both come out right)."""
    return _html.escape(_html.unescape(str(s)), quote=False)


def spec_for(slug, key):
    f = KIT / "src" / "media" / f"{slug}.json"
    if not f.exists():
        raise SystemExit(f"missing src/media/{slug}.json")
    j = json.loads(f.read_text(encoding="utf-8"))
    if key not in j:
        raise SystemExit(f"src/media/{slug}.json has no \"{key}\" block")
    return j[key]


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


def wrap(dur, body, css, js):
    return f'''<!doctype html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width={W}, height={H}">
<script src="{GSAP}"></script>
<style>{FONTS}{css}</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{dur}" data-width="{W}" data-height="{H}">
{body}
</div>
<script>
const tl = gsap.timeline({{ paused: true }});
{js}
window.__timelines = window.__timelines || {{}};
window.__timelines["main"] = tl;
tl.seek(0);
</script></body></html>'''


def wordmark(dur, track):
    return (f'<div class="mark clip" data-start="0" data-duration="{dur}" data-track-index="{track}">'
            f'<b>SUZU TRAVELS</b><small>Himachal · India · since 2019</small></div>')


def stars(n=140, seed=17, ymax=H):
    r = random.Random(seed)
    return "".join(f'<circle cx="{r.uniform(0, W):.0f}" cy="{r.uniform(0, ymax):.0f}" r="{r.uniform(.6, 1.8):.1f}" fill="#fff" opacity="{r.uniform(.12, .5):.2f}"/>' for _ in range(n))


# ------------------------------------------------------------------------------------------------ photos
def credited_photos():
    """Filenames that have a row in hf/photos/CREDITS.md (the licence register)."""
    f = HF / "photos" / "CREDITS.md"
    if not f.exists():
        return set()
    return set(re.findall(r"^\|\s*((?:px|us)-[\w.-]+\.jpe?g)\s*\|", f.read_text(encoding="utf-8"), re.M))


def photo_size(fname):
    try:
        from PIL import Image
        with Image.open(HF / "photos" / fname) as im:
            return im.size
    except Exception:
        return None


def photo_scene_html(i, sc, dur):
    w, h = sc["w"], sc["h"]
    if sc["kind"] == "tilt":   # portrait, 1920 wide, bottom-aligned; positive y pans down the image (reveals the top)
        style = f"left:{(W - w) // 2}px;top:{H - h}px;width:{w}px;height:{h}px"
    else:                      # landscape, 2112 wide, centred
        style = f"left:{(W - w) // 2}px;top:{(H - h) // 2}px;width:{w}px;height:{h}px"
    img = f'<img id="p{i}" class="ph" src="assets/{sc["img"]}" style="{style}" alt="">'
    if sc.get("mirror"):
        return (f'<div class="clip" style="position:absolute;inset:0;transform:scaleX(-1)" data-start="0" data-duration="{dur}" data-track-index="{i}">{img}</div>')
    return f'<div class="clip" style="position:absolute;inset:0" data-start="0" data-duration="{dur}" data-track-index="{i}">{img}</div>'


def photo_scene_js(scenes, dur, xf=0.6):
    """Scene i fades in over xf s at t[0], moves from->to until t[1]; the last scene fades out over scene 0 => seamless loop."""
    js, n = [], len(scenes)
    for i, sc in enumerate(scenes):
        a, b = sc["t"]
        f, t = sc["from"], sc["to"]
        fs = f'scale:{f.get("scale", 1)},x:{f.get("x", 0)},y:{f.get("y", 0)}'
        ts = f'scale:{t.get("scale", 1)},x:{t.get("x", 0)},y:{t.get("y", 0)}'
        if i == 0:
            js.append(f'tl.set("#p0",{{opacity:1,{fs}}},0);tl.to("#p0",{{{ts},duration:{b - a:.2f},ease:"none"}},0);')
            nxt = scenes[1]["t"][0] + xf
            js.append(f'tl.set("#p0",{{opacity:0}},{nxt + .05:.2f});tl.set("#p0",{{{fs}}},{nxt + .1:.2f});tl.set("#p0",{{opacity:1}},{dur - xf - .3:.2f});')
        else:
            js.append(f'tl.set("#p{i}",{{opacity:0,{fs}}},0);tl.to("#p{i}",{{opacity:1,duration:{xf},ease:"none"}},{a:.2f});'
                      f'tl.to("#p{i}",{{{ts},duration:{b - a:.2f},ease:"none"}},{a:.2f});')
            if i < n - 1:
                js.append(f'tl.set("#p{i}",{{opacity:0}},{scenes[i + 1]["t"][0] + xf + .05:.2f});')
            else:
                js.append(f'tl.to("#p{i}",{{opacity:0,duration:{xf + .2:.2f},ease:"none"}},{dur - xf - .2:.2f});')
    return "".join(js)


def photo_hero(slug):
    """Premium photo-film hero. src/media/<slug>.json "hero" = {
         "kicker": "NORTH INDIA · 12 DAYS",
         "scenes": [ {"img": "px-33777272.jpg", "kind": "tilt"|"land", "mirror": false,
                      "t": [start, end]  (optional — scenes tile the 14 s loop automatically, 0.6 s cross-fades),
                      "from": {"y": 0}, "to": {"y": 560}  (optional — gentle default pans; tilt = y, land = scale + x)} x 3–5 ],
         "steps": ["DELHI → AGRA", "TAJ AT SUNRISE", "SHIMLA HILLS"]   3–5 captions, CAPITALS, ≤ 18 characters each.
       Every img must be in hf/photos/ AND in CREDITS.md. Caption a photo as a place only if CREDITS.md allows it."""
    spec = spec_for(slug, "hero")
    scenes, steps = [dict(s) for s in spec["scenes"]], [str(s) for s in spec["steps"]]
    DUR, XF = 14.0, 0.6
    if not 3 <= len(scenes) <= 5:
        raise SystemExit("hero.scenes needs 3-5 photos")
    if not 3 <= len(steps) <= 5:
        raise SystemExit("hero.steps needs 3-5 captions")
    for s in steps:
        if len(s) > 18:
            raise SystemExit(f"caption longer than 18 characters: {s!r}")
        if s != s.upper():
            raise SystemExit(f"captions are CAPITALS: {s!r}")
    ok = credited_photos()
    n = len(scenes)
    seg = (DUR + (n - 1) * XF) / n
    for i, sc in enumerate(scenes):
        if sc["img"] not in ok or not (HF / "photos" / sc["img"]).exists():
            raise SystemExit(f"{sc['img']} is not in hf/photos/ + CREDITS.md — licensed photos only")
        size = photo_size(sc["img"])
        if size:
            sc["w"], sc["h"] = size
        else:
            sc.setdefault("w", 1920 if sc["kind"] == "tilt" else 2112)
            if "h" not in sc:
                raise SystemExit(f"{sc['img']}: give \"h\" (PIL not available to read it)")
        if sc["kind"] not in ("tilt", "land"):
            raise SystemExit("scene kind must be tilt or land")
        if sc["kind"] == "tilt" and sc["h"] < H + 200:
            raise SystemExit(f"{sc['img']}: tilt photos need ≥ {H + 200}px height")
        sc["t"] = tuple(sc.get("t") or (round(i * (seg - XF), 2), round(i * (seg - XF) + seg, 2)))
        if "from" not in sc or "to" not in sc:
            if sc["kind"] == "tilt":
                room = min(sc["h"] - H, 620)
                sc["from"], sc["to"] = ({"y": 0}, {"y": room}) if i % 2 == 0 else ({"y": room}, {"y": 0})
            else:
                sc["from"], sc["to"] = ({"scale": 1.02, "x": 40}, {"scale": 1.12, "x": -40}) if i % 2 == 0 else ({"scale": 1.12, "x": -40}, {"scale": 1.02, "x": 40})
    if scenes[0]["t"][0] != 0 or abs(scenes[-1]["t"][1] - DUR) > .01:
        raise SystemExit(f"scene times must start at 0 and end at {DUR}")
    d = prep(f"{slug}-hero", [s["img"] for s in scenes])
    kicker = esc(spec.get("kicker", "INDIA · PRIVATE TRIPS"))
    # caption font size: CG capitals ~0.72 em per character with the tracking below; keep every caption inside 900 px
    caps = []
    for i, s in enumerate(steps):
        fs = min(96, int(900 / (0.72 * max(len(s), 8))))
        caps.append(f'<div class="cp" id="c{i}" style="font-size:{fs}px"><span class="no">{i + 1:02d} / {len(steps):02d}</span>{esc(s)}</div>')
    body = ["".join(photo_scene_html(i, s, DUR) for i, s in enumerate(scenes)),
            f'<div class="vig clip" data-start="0" data-duration="{DUR}" data-track-index="10"></div>',
            f'<div class="shade clip" data-start="0" data-duration="{DUR}" data-track-index="11"></div>',
            f'<div class="hud clip" data-start="0" data-duration="{DUR}" data-track-index="12"><div class="kick">{kicker}</div><div class="bar" id="bar"></div>'
            f'<div style="position:relative;height:260px">{"".join(caps)}</div></div>',
            wordmark(DUR, 13)]
    js = [photo_scene_js(scenes, DUR, XF)]
    m = len(steps)
    cs = DUR / m
    for i in range(m):
        a = i * cs
        if i == 0:
            js.append(f'tl.set("#c0",{{opacity:1,y:0}},0);tl.to("#c0",{{opacity:0,y:-22,duration:.45}},{cs - .1:.2f});'
                      f'tl.set("#c0",{{y:22}},{cs + .4:.2f});tl.to("#c0",{{opacity:1,y:0,duration:.5}},{DUR - .5:.2f});')
        else:
            out_at = (i + 1) * cs - .1 if i < m - 1 else DUR - 1.0
            js.append(f'tl.set("#c{i}",{{opacity:0,y:22}},0);tl.to("#c{i}",{{opacity:1,y:0,duration:.55,ease:"power2.out"}},{a + .3:.2f});'
                      f'tl.to("#c{i}",{{opacity:0,y:-22,duration:.45}},{out_at:.2f});')
    js.append(f'tl.fromTo("#bar",{{scaleX:0}},{{scaleX:1,duration:{DUR - .4:.2f},ease:"none"}},.1);tl.to("#bar",{{opacity:0,duration:.25}},{DUR - .3:.2f});')
    css = ('.ph{position:absolute;object-fit:cover;opacity:0;transform-origin:50% 50%}'
           '.shade{position:absolute;inset:0;background:linear-gradient(90deg,rgba(11,31,58,.22) 0%,rgba(11,31,58,.04) 38%,rgba(11,31,58,.58) 62%,rgba(11,31,58,.9) 100%)}'
           '.vig{position:absolute;inset:0;background:radial-gradient(ellipse at 38% 48%,rgba(0,0,0,0) 52%,rgba(0,0,0,.38) 100%)}'
           '.hud{position:absolute;right:150px;top:300px;width:900px;text-align:right}'
           '.bar{height:5px;width:380px;margin:18px 0 34px auto;background:linear-gradient(90deg,#ff8a2a,#f2c14e);border-radius:3px;transform-origin:100% 50%}'
           '.cp{position:absolute;right:0;top:0;width:900px;opacity:0;font-family:"CG",serif;font-weight:700;line-height:1.08;letter-spacing:.06em;color:#fff7e6;text-shadow:0 6px 30px rgba(0,0,0,.6);white-space:nowrap}'
           '.cp .no{display:block;font:800 22px "SZ",sans-serif;letter-spacing:.3em;color:#ffe3a3;margin-bottom:16px}')
    (d / "index.html").write_text(wrap(DUR, "\n".join(body), css, "".join(js)), encoding="utf-8")
    return d


# ------------------------------------------------------------------------------------------------ route map (stops by lat/lon, no borders, no outline)
LON0, LON1, LAT0, LAT1 = 67.5, 97.5, 6.5, 36.5
BOUNDS = None  # optional (lon0, lon1, lat0, lat1) zoom for regional routes (spec "bounds")


def proj(lat, lon, box):
    x0, y0, x1, y1 = box
    l0, l1, a0, a1 = BOUNDS or (LON0, LON1, LAT0, LAT1)
    return x0 + (lon - l0) / (l1 - l0) * (x1 - x0), y0 + (a1 - lat) / (a1 - a0) * (y1 - y0)


def route_map(slug):
    """Animated itinerary map. src/media/<slug>.json "route" = {
         "title": "INDIA · 14 DAYS", "sub": "Delhi to the Himalaya and back",
         "bounds": "auto" | [lon0, lon1, lat0, lat1]   zoom to the stops / fixed window (omit for all-India),
         "dur": 13,
         "stops": [ {"name": "Delhi", "sub": "arrive", "day": "Day 1–2", "lat": 28.61, "lon": 77.21}, ... ] 3–9 stops,
                   lat/lon from the fact pack only. }
       Draws a graticule, the stops and the line between them — NO outline, NO state or national boundary lines."""
    global BOUNDS
    spec = spec_for(slug, "route")
    stops = spec["stops"]
    if not 3 <= len(stops) <= 9:
        raise SystemExit("route.stops needs 3-9 stops")
    box = (200, 60, 1240, 1040)
    b = spec.get("bounds")
    if b == "auto":   # fit the stops with a margin, keeping the box's aspect (1° lon ≈ 0.87° lat at these latitudes)
        la = [s["lat"] for s in stops]; lo_ = [s["lon"] for s in stops]
        clat, clon = (max(la) + min(la)) / 2, (max(lo_) + min(lo_)) / 2
        dlat = max(max(la) - min(la), 1.0) * 1.35 + .4
        dlon = max(max(lo_) - min(lo_), 1.0) * 1.35 + .4
        k = 0.87 * (box[2] - box[0]) / (box[3] - box[1])   # lon-degrees per lat-degree for a square-looking box
        if dlon / dlat < k:
            dlon = dlat * k
        else:
            dlat = dlon / k
        b = [round(clon - dlon / 2, 2), round(clon + dlon / 2, 2), round(clat - dlat / 2, 2), round(clat + dlat / 2, 2)]
    BOUNDS = tuple(b) if b else None
    dur = float(spec.get("dur", 13))
    d = prep(f"{slug}-route")
    grat = ""
    if BOUNDS:
        l0, l1, a0, a1 = BOUNDS
        lons = [l0 + (l1 - l0) * k / 6 for k in range(1, 6)]
        lats = [a0 + (a1 - a0) * k / 6 for k in range(1, 6)]
        lbl = lambda v: f"{v:.1f}°N"
    else:
        lons, lats, lbl = range(70, 98, 5), range(10, 37, 5), (lambda v: f"{v}°N")
    for lon in lons:
        x, _ = proj(0, lon, box)
        grat += f'<line x1="{x:.0f}" y1="{box[1]}" x2="{x:.0f}" y2="{box[3]}" stroke="{GOLD2}" stroke-opacity=".09"/>'
    for lat in lats:
        _, y = proj(lat, 0, box)
        grat += (f'<line x1="{box[0]}" y1="{y:.0f}" x2="{box[2]}" y2="{y:.0f}" stroke="{GOLD2}" stroke-opacity=".09"/>'
                 f'<text x="{box[0] - 12}" y="{y + 6:.0f}" text-anchor="end" font-family="SZ" font-size="15" fill="{GOLD2}" fill-opacity=".35">{lbl(lat)}</text>')
    pts = [proj(s["lat"], s["lon"], box) for s in stops]
    for (x, y) in pts:
        if not (box[0] <= x <= box[2] and box[1] <= y <= box[3]):
            raise SystemExit(f"a stop falls outside the map box ({x:.0f},{y:.0f}) — widen \"bounds\"")
    path = "M" + " L".join(f"{x:.0f} {y:.0f}" for x, y in pts)
    plen = sum(math.dist(pts[i], pts[i + 1]) for i in range(len(pts) - 1)) + 10
    dots, labels, js = [], [], []
    t0, step = .7, (dur - 3.2) / len(stops)
    for i, ((x, y), s) in enumerate(zip(pts, stops)):
        dup = any(math.dist((x, y), q) < 8 for q in pts[:i])   # a repeated stop (e.g. back to Delhi): number on the left
        numtxt = (f'<text x="{x - 16:.0f}" y="{y + 6:.0f}" text-anchor="end" font-family="SZ" font-weight="700" font-size="19" fill="{GOLD3}">{i + 1}</text>' if dup
                  else f'<text x="{x + 16:.0f}" y="{y + 6:.0f}" font-family="SZ" font-weight="700" font-size="19" fill="{GOLD3}">{i + 1}</text>')
        ph = min(240, int(y) - 12)   # light pillar never runs off the top of the frame
        dots.append(f'<g id="p{i}" style="opacity:.25"><rect x="{x - 9:.0f}" y="{y - ph:.0f}" width="18" height="{ph}" fill="url(#pl2)" id="pb{i}" style="transform-origin:{x:.0f}px {y:.0f}px"/>'
                    f'<circle cx="{x:.0f}" cy="{y:.0f}" r="30" fill="url(#gl)"/><circle cx="{x:.0f}" cy="{y:.0f}" r="7" fill="#fff4c9"/>{numtxt}</g>')
        labels.append(f'<div class="lb" id="l{i}"><b>{i + 1:02d}</b><span class="dy">{esc(s.get("day", ""))}</span>'
                      f'<span class="nm">{esc(s["name"])}<small>{esc(s.get("sub", s.get("state", "")))}</small></span></div>')
        t = t0 + i * step
        js.append(f'tl.set("#p{i}",{{opacity:.25}},0);tl.to("#p{i}",{{opacity:1,duration:.35}},{t:.2f});tl.fromTo("#pb{i}",{{scaleY:0}},{{scaleY:1,duration:.55,ease:"power2.out"}},{t:.2f});'
                  f'tl.to("#pb{i}",{{opacity:.35,duration:.6}},{t + .8:.2f});')
        js.append(f'tl.set("#l{i}",{{opacity:.28}},0);tl.to("#l{i}",{{opacity:1,x:-10,duration:.3}},{t:.2f});tl.to("#l{i}",{{x:0,duration:.3}},{t + .4:.2f});')
    tend = t0 + len(stops) * step
    js.append(f'tl.fromTo("#route",{{strokeDashoffset:{plen:.0f}}},{{strokeDashoffset:0,duration:{tend - t0:.2f},ease:"none"}},{t0});')
    fo = dur - 1.1   # loop: fade back to the dim start state
    js.append(f'tl.to("#route",{{opacity:0,duration:.8}},{fo:.2f});tl.set("#route",{{strokeDashoffset:{plen:.0f},opacity:.8}},{dur - .05:.2f});')
    for i in range(len(stops)):
        js.append(f'tl.to("#p{i}",{{opacity:.25,duration:.8}},{fo:.2f});tl.to("#l{i}",{{opacity:.28,duration:.8}},{fo:.2f});tl.set("#pb{i}",{{opacity:1,scaleY:0}},{dur - .05:.2f});')
    svg = (f'<svg class="lay" viewBox="0 0 {W} {H}"><defs><radialGradient id="gl"><stop offset="0" stop-color="#ffe9a8" stop-opacity=".9"/><stop offset="1" stop-color="{SAFF}" stop-opacity="0"/></radialGradient>'
           f'<linearGradient id="pl2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".7" stop-color="#ffe2a0" stop-opacity=".9"/><stop offset="1" stop-color="#ffb347"/></linearGradient>'
           f'<radialGradient id="bgg" cx=".35" cy=".5" r=".75"><stop offset="0" stop-color="#143a5e"/><stop offset="1" stop-color="{NAVY2}"/></radialGradient></defs>'
           f'<rect width="{W}" height="{H}" fill="url(#bgg)"/>{stars()}{grat}'
           f'<path id="route" d="{path}" fill="none" stroke="{GOLD2}" stroke-opacity=".8" stroke-width="2.5" stroke-dasharray="{plen:.0f}" stroke-dashoffset="{plen:.0f}"/>'
           f'{"".join(dots)}</svg>')
    body = [f'<div class="lay clip" data-start="0" data-duration="{dur}" data-track-index="0">{svg}</div>',
            f'<div class="side clip" data-start="0" data-duration="{dur}" data-track-index="1"><div class="kick">{esc(spec["title"])}</div><div class="sub">{esc(spec.get("sub", ""))}</div>{"".join(labels)}</div>',
            wordmark(dur, 2)]
    rowh = 70 if len(stops) <= 7 else 58
    css = ('.side{position:absolute;right:70px;top:70px;width:600px}.sub{font:600 30px "CG",serif;color:#fff7e6;margin:8px 0 18px}'
           f'.lb{{display:flex;align-items:center;gap:14px;height:{rowh}px;border-bottom:1px solid rgba(242,193,78,.16);opacity:.28}}'
           '.lb b{font:800 18px "SZ",sans-serif;color:#f2c14e;width:30px}.lb .dy{font:700 20px "SZ",sans-serif;letter-spacing:.08em;color:#ffe3a3;min-width:150px}'
           '.lb .nm{font:700 24px "SZ",sans-serif;color:#fff}.lb small{display:block;font:500 16px "SZ",sans-serif;color:rgba(255,255,255,.6);margin-top:2px}'
           '.mark{bottom:60px;right:70px}')
    (d / "index.html").write_text(wrap(dur, "\n".join(body), css, "".join(js)), encoding="utf-8")
    return d


# ------------------------------------------------------------------------------------------------ cost ladder (what's included, in words)
def allowed_prices():
    f = DATA / "prices.json"
    return set(json.loads(f.read_text(encoding="utf-8")).get("allowed", [])) if f.exists() else set()


def cost_ladder(slug):
    """What a trip includes / costs, as a vertical ladder. src/media/<slug>.json "cost" = {
         "kicker": "WHAT'S INCLUDED", "title": "One price, few surprises",
         "items": [ {"label": "Car + driver", "sub": "fuel, tolls, parking, driver's stay", "price": 449}, ... ] 3–7 rungs, bottom to top;
                   "price" (optional) prints "from US$449" and MUST be in data/prices.json "allowed" — otherwise leave it out,
         "end": "Flights, visa and tips are extra · exact quote on request" }
       No numbers other than approved US$ figures: distances, days and hotel stars belong in the page text, not here."""
    spec = spec_for(slug, "cost")
    items = spec["items"]
    if not 3 <= len(items) <= 7:
        raise SystemExit("cost.items needs 3-7 rungs")
    ok = allowed_prices()
    for it in items:
        if "price" in it and it["price"] not in ok:
            raise SystemExit(f"price {it['price']} is not in data/prices.json allowed — remove it (words only)")
        if len(str(it["label"])) > 26 or len(str(it.get("sub", ""))) > 60:
            raise SystemExit(f"label ≤ 26 chars, sub ≤ 60 chars: {it}")
    DUR = 14.0
    n = len(items)
    d = prep(f"{slug}-cost")
    RX, Y0, Y1 = 330, 880, 290          # rail x, bottom rung y, top rung y
    ys = [Y0 - (Y0 - Y1) * i / (n - 1) for i in range(n)]
    rungs, js = [], []
    t0, step = 1.6, min(1.5, 8.4 / n)
    for i, (it, y) in enumerate(zip(items, ys)):
        price = f'<div class="pr">from <b>US${it["price"]:,}</b></div>' if "price" in it else '<div class="pr dim">included</div>'
        rungs.append(f'<div class="rg" id="r{i}" style="top:{y:.0f}px"><div class="dot"></div><div class="lab"><div class="l">{esc(it["label"])}</div><div class="s">{esc(it.get("sub", ""))}</div></div>{price}</div>')
        t = t0 + i * step
        js.append(f'tl.fromTo("#r{i}",{{opacity:0,x:-26}},{{opacity:1,x:0,duration:.5,ease:"power2.out"}},{t:.2f});')
        js.append(f'tl.fromTo("#r{i} .dot",{{scale:0}},{{scale:1,duration:.4,ease:"back.out(2.2)"}},{t:.2f});')
    tend = t0 + (n - 1) * step
    js.insert(0, f'tl.fromTo("#ttl",{{opacity:0,y:18}},{{opacity:1,y:0,duration:.6,ease:"power2.out"}},.2);')
    js.insert(1, f'tl.fromTo("#rail",{{scaleY:0}},{{scaleY:1,duration:{tend - t0 + .5:.2f},ease:"none"}},{t0 - .2:.2f});')
    js.append(f'tl.set("#cl",{{y:0,opacity:0}},0);tl.to("#cl",{{opacity:1,duration:.3}},{t0 - .3:.2f});')
    for i in range(1, n):
        js.append(f'tl.to("#cl",{{y:{ys[i] - ys[0]:.0f},duration:{step - .05:.2f},ease:"power1.inOut"}},{t0 + (i - 1) * step + .15:.2f});')
    js.append(f'tl.fromTo("#halo",{{opacity:0,scale:.4}},{{opacity:1,scale:1,duration:.7,ease:"power2.out"}},{tend + .3:.2f});')
    js.append(f'tl.fromTo("#end",{{opacity:0,y:16}},{{opacity:1,y:0,duration:.6}},{tend + .6:.2f});')
    js.append(f'tl.to("#all",{{opacity:0,duration:.7,ease:"none"}},{DUR - .7:.2f});')
    grid = "".join(f'<div class="gl" style="top:{y:.0f}px"></div>' for y in ys)
    body = [f'<div class="bg clip" data-start="0" data-duration="{DUR}" data-track-index="0"></div>',
            f'<svg class="lay clip" data-start="0" data-duration="{DUR}" data-track-index="1" viewBox="0 0 {W} {H}">{stars(110, 23)}</svg>',
            f'<div id="all" class="clip" data-start="0" data-duration="{DUR}" data-track-index="2">{grid}'
            f'<div id="rail" style="top:{Y1 - 40:.0f}px;height:{Y0 - Y1 + 80:.0f}px"></div>'
            f'<div id="halo" style="top:{Y1 - 90:.0f}px"></div>{"".join(rungs)}<div id="cl" style="top:{ys[0] - 10:.0f}px"></div>'
            f'<div id="ttl"><div class="kick">{esc(spec.get("kicker", "WHAT&#8217;S INCLUDED"))}</div><div class="t">{esc(spec.get("title", ""))}</div></div>'
            f'<div id="end">{esc(spec.get("end", "Exact quote on request"))}</div></div>',
            wordmark(DUR, 3)]
    css = (f'.bg{{position:absolute;inset:0;background:radial-gradient(ellipse at 78% 12%,#16395c 0%,{NAVY} 42%,{NAVY2} 100%)}}'
           '#all{position:absolute;inset:0}'
           f'.gl{{position:absolute;left:{RX}px;width:1480px;height:1px;background:rgba(207,230,245,.10)}}'
           f'#rail{{position:absolute;left:{RX - 2}px;width:4px;border-radius:2px;background:linear-gradient(0deg,{SAFF},{GOLD2});transform-origin:50% 100%}}'
           f'#halo{{position:absolute;left:{RX - 90}px;width:180px;height:180px;border-radius:50%;background:radial-gradient(circle,rgba(243,217,143,.5),rgba(243,217,143,0) 70%)}}'
           f'#cl{{position:absolute;left:{RX - 10}px;width:20px;height:20px;border-radius:50%;background:#ff5a36;box-shadow:0 0 0 7px rgba(255,90,54,.28),0 0 26px rgba(255,90,54,.8)}}'
           f'.rg{{position:absolute;left:{RX - 15}px;width:{1860 - RX}px;height:0;display:flex;align-items:center;gap:26px;opacity:0}}'
           f'.dot{{width:30px;height:30px;border-radius:50%;background:#fff;border:6px solid {GOLD};box-shadow:0 0 0 7px rgba(217,154,43,.22);flex:none}}'
           '.lab{flex:1;min-width:0}.lab .l{font:800 44px/1.1 "SZ",sans-serif;color:#fff;letter-spacing:-.01em}'
           '.lab .s{font:500 24px/1.2 "SZ",sans-serif;color:rgba(207,230,245,.78);margin-top:6px}'
           f'.pr{{flex:none;font:700 26px "SZ",sans-serif;color:{GOLD3};background:rgba(242,193,78,.12);border:1px solid rgba(242,193,78,.45);border-radius:999px;padding:12px 26px}}'
           '.pr b{font-weight:800;font-size:34px;color:#fff}.pr.dim{color:rgba(207,230,245,.7);border-color:rgba(207,230,245,.25);background:rgba(207,230,245,.06)}'
           '#ttl{position:absolute;left:70px;top:70px}#ttl .t{font:800 54px "SZ",sans-serif;color:#fff;margin-top:8px;letter-spacing:-.01em}'
           '#end{position:absolute;left:70px;bottom:70px;font:600 28px "CG",serif;color:rgba(255,247,230,.9)}'
           '.mark{bottom:60px;right:70px}')
    (d / "index.html").write_text(wrap(DUR, "\n".join(body), css, "".join(js)), encoding="utf-8")
    return d


if __name__ == "__main__":
    a = sys.argv[1:]
    fns = {"photo-hero": photo_hero, "route-map": route_map, "cost-ladder": cost_ladder}
    if len(a) != 2 or a[0] not in fns:
        raise SystemExit(__doc__)
    print(fns[a[0]](a[1]))
