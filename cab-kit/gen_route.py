#!/usr/bin/env python3
"""Suzu route-map motion graphic (HyperFrames). 1600x900, 9 s seamless loop.
  python3 gen_route.py <slug>   -> routes/<slug>/index.html (+ assets)
Modes: 'path' (A->B through waypoints) or 'hub' (spokes from one town). Data comes from the Cab Kit page content.
No borders are drawn (one borderless landmass look); only towns, a Himalaya zone and the route.
"""
import sys, math, json, shutil, pathlib
import os, pathlib as _pl
sys.path.insert(0, str(_pl.Path(__file__).resolve().parent))
from cabs_data import PLACES, ROUTE_BY_SLUG
from pages_content import PAGES

W, H, DUR = 1600, 900, 9
KIT = pathlib.Path(__file__).resolve().parent
HF = pathlib.Path(os.environ.get("CAB_HF_OUT", str(KIT.parent.parent / "cab-hf")))  # render workspace (outside the repo)
SCAFFOLD = KIT / "hf-scaffold"
FONTS = SCAFFOLD / "assets"

FRONT = [(33.6, 70.0), (33.3, 73.6), (32.75, 75.0), (32.35, 75.75), (32.05, 76.2), (31.75, 76.6), (31.35, 76.85), (31.0, 76.95), (30.85, 77.0),
         (30.55, 77.6), (30.35, 77.95), (30.1, 78.3), (29.7, 78.9), (29.35, 79.4), (29.2, 80.5), (28.6, 84.0), (27.5, 95.0)]

def build(p):
    m = p["map"]
    mode = "hub" if "hub" in m else "path"
    if mode == "path":
        seq = m["path"]; labels = m["labels"]
    else:
        seq = [m["hub"]] + m["spokes"]; labels = seq
    ctx = [c for c in m.get("ctx", []) if c in PLACES]
    names = list(dict.fromkeys(seq + labels + ctx + (["Chandigarh"] if "Chandigarh" in labels else [])))
    lats = [PLACES[n][0] for n in names]; lons = [PLACES[n][1] for n in names]
    latc = math.radians(sum(lats) / len(lats))
    # map area: left part of frame, panel on the right
    ax0, ay0, ax1, ay1 = 70, 80, 1010, 830
    xs = [lo * math.cos(latc) for lo in lons]; ys = [-la for la in lats]
    minx, maxx, miny, maxy = min(xs), max(xs), min(ys), max(ys)
    spanx, spany = max(maxx - minx, .3), max(maxy - miny, .3)
    k = min((ax1 - ax0) / spanx, (ay1 - ay0) / spany) * 0.86
    cx, cy = (minx + maxx) / 2, (miny + maxy) / 2
    def P(name=None, lat=None, lon=None):
        if name: lat, lon = PLACES[name]
        return ((ax0 + ax1) / 2 + (lon * math.cos(latc) - cx) * k, (ay0 + ay1) / 2 + (-lat - cy) * k)
    # grid every 0.5 deg
    grid = []
    for lat2 in [x / 2 for x in range(50, 72)]:
        y = P(lat=lat2, lon=77)[1]
        if -10 < y < H + 10: grid.append(f'<line x1="0" y1="{y:.0f}" x2="{W}" y2="{y:.0f}"/>')
    for lon2 in [x / 2 for x in range(140, 164)]:
        x = P(lat=31, lon=lon2)[0]
        if -10 < x < W + 10: grid.append(f'<line x1="{x:.0f}" y1="0" x2="{x:.0f}" y2="{H}"/>')
    # himalaya zone
    fp = [P(lat=a, lon=b) for a, b in FRONT]
    zone = "M" + " L".join(f"{x:.0f} {y:.0f}" for x, y in fp) + f" L{fp[-1][0]:.0f} -2000 L{fp[0][0]:.0f} -2000 Z"
    # mountain glyphs inside zone (deterministic lattice)
    glyphs = []
    def inside(x, y):
        # zone = north (smaller y) of the front polyline
        for i in range(len(fp) - 1):
            (x0, y0), (x1, y1) = fp[i], fp[i + 1]
            if min(x0, x1) <= x <= max(x0, x1) and x1 != x0:
                yl = y0 + (y1 - y0) * (x - x0) / (x1 - x0)
                return y < yl - 18
        return False
    for gy in range(40, H, 58):
        for gx in range(20 + (gy // 58 % 2) * 34, W, 68):
            if inside(gx, gy):
                glyphs.append(f'<path d="M{gx-13} {gy+8} L{gx} {gy-9} L{gx+13} {gy+8}" />')
    # route geometry
    def catmull(pts, n=14):
        out = []
        pts = [pts[0]] + pts + [pts[-1]]
        for i in range(1, len(pts) - 2):
            p0, p1, p2, p3 = pts[i - 1], pts[i], pts[i + 1], pts[i + 2]
            for t in [j / n for j in range(n)]:
                t2, t3 = t * t, t * t * t
                out.append(tuple(0.5 * ((2 * p1[c]) + (-p0[c] + p2[c]) * t + (2 * p0[c] - 5 * p1[c] + 4 * p2[c] - p3[c]) * t2 + (-p0[c] + 3 * p1[c] - 3 * p2[c] + p3[c]) * t3) for c in (0, 1)))
        out.append(pts[-2])
        return out
    paths = []
    if mode == "path":
        pts = catmull([P(n) for n in seq])
        paths.append("M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts))
    else:
        hx, hy = P(m["hub"])
        for s in m["spokes"]:
            sx, sy = P(s)
            mx, my = (hx + sx) / 2, (hy + sy) / 2
            dx, dy = sx - hx, sy - hy
            qx, qy = mx - dy * .18, my + dx * .18
            paths.append(f"M{hx:.1f} {hy:.1f} Q{qx:.1f} {qy:.1f} {sx:.1f} {sy:.1f}")
    # towns
    towns = []
    lab_set = labels
    kept = []
    isend = lambda i: (mode == "path" and (i == 0 or i == len(lab_set) - 1)) or (mode == "hub" and i == 0)
    order = [i for i in range(len(lab_set)) if isend(i)] + [i for i in range(len(lab_set)) if not isend(i)]
    for i in order:
        n = lab_set[i]
        x, y = P(n)
        end = isend(i)
        if mode == "path" and not end and any(abs(x - kx) < 150 and abs(y - ky) < 34 for kx, ky in kept):
            towns.append(f'<g class="town" id="t{i}" data-x="{x:.1f}" data-y="{y:.1f}"><circle class="halo" cx="{x:.1f}" cy="{y:.1f}" r="14"/><circle class="dot" cx="{x:.1f}" cy="{y:.1f}" r="6"/></g>')
            continue
        kept.append((x, y))
        cls = "town end" if end else "town"
        anchor, dx = ("end", -16) if x > 900 else ("start", 30 if end else 16)
        dy = 7
        if mode == "hub" and not end:
            hx0 = P(m["hub"])[0]
            anchor, dx = ("end", -16) if x < hx0 - 5 else ("start", 16)
        if mode == "path" and end and x > 900:
            anchor, dx, dy = ("end", 0, -30)
        towns.append(f'<g class="{cls}" id="t{i}" data-x="{x:.1f}" data-y="{y:.1f}"><circle class="halo" cx="{x:.1f}" cy="{y:.1f}" r="{22 if end else 14}"/><circle class="dot" cx="{x:.1f}" cy="{y:.1f}" r="{9 if end else 6}"/>'
                     f'<text x="{x+dx:.1f}" y="{y+dy:.1f}" text-anchor="{anchor}">{n}</text></g>')
    for n in dict.fromkeys(ctx):
        if n in lab_set: continue
        x, y = P(n)
        if 0 < x < 1040 and 0 < y < H and not any(abs(x - kx) < 170 and abs(y - ky) < 40 for kx, ky in kept):
            towns.insert(0, f'<g class="ctx"><circle cx="{x:.1f}" cy="{y:.1f}" r="5"/><text x="{x+11:.1f}" y="{y+5:.1f}">{n}</text></g>')
            kept.append((x, y))
    # panel
    if mode == "path":
        r = ROUTE_BY_SLUG[p["route"]]
        via = [n for n in labels[1:-1]][:3]
        panel = (f'<div class="kick">ROUTE PLAN</div><div class="big">{r["a"]}</div><div class="arrow"><i></i></div><div class="big">{r["b"]}</div>'
                 f'<div class="stats"><div><b>{r["km"]} km</b><span>distance</span></div><div><b>{r["t"]}</b><span>by road</span></div></div>'
                 f'<div class="via">via {" · ".join(via)}</div>')
    else:
        panel = (f'<div class="kick">POPULAR TRIPS FROM</div><div class="big">{m["hub"]}</div>'
                 f'<ul class="list">' + "".join(f'<li id="li{i}"><i></i>{s}</li>' for i, s in enumerate(m["spokes"])) + '</ul>')
    panel += '<div class="brand">SUZU TRAVELS · CABS</div>'
    cfg = json.dumps(dict(mode=mode, n=len(paths), labels=len(lab_set)))
    html = f'''<!doctype html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width={W}, height={H}">
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
<style>
@font-face{{font-family:"SuzuSans";src:url("assets/plus-jakarta-sans-latin-800-normal.woff2") format("woff2");font-weight:800}}
@font-face{{font-family:"SuzuSans";src:url("assets/plus-jakarta-sans-latin-700-normal.woff2") format("woff2");font-weight:700}}
@font-face{{font-family:"SuzuSans";src:url("assets/plus-jakarta-sans-latin-500-normal.woff2") format("woff2");font-weight:500}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{margin:0;width:{W}px;height:{H}px;overflow:hidden;background:#0d1f12}}
#root{{position:relative;width:100%;height:100%;overflow:hidden;font-family:"SuzuSans",sans-serif}}
.scene{{position:absolute;inset:0;width:100%;height:100%;background:radial-gradient(1200px 800px at 35% 55%,#1d3f27 0%,#122615 55%,#0b1a0e 100%)}}
svg.map{{position:absolute;inset:0;width:100%;height:100%}}
.grid line{{stroke:#ffffff;stroke-opacity:.05;stroke-width:1}}
.zone{{fill:#26452e;fill-opacity:.55}}
.glyph path{{fill:none;stroke:#8fb59a;stroke-opacity:.17;stroke-width:2;stroke-linejoin:round}}
.zlabel{{font-size:22px;font-weight:800;letter-spacing:.5em;fill:#cfe3d4;fill-opacity:.35}}
.ctx circle{{fill:#9fb7a6;fill-opacity:.55}} .ctx text{{font-size:20px;font-weight:500;fill:#cfe0d4;fill-opacity:.55}}
.town .dot{{fill:#ffffff}} .town .halo{{fill:#d4af37;fill-opacity:.0}}
.town text{{font-size:26px;font-weight:700;fill:#ffffff;paint-order:stroke;stroke:#0b1a0e;stroke-width:6px;stroke-linejoin:round}}
.town.end .dot{{fill:#d4af37;stroke:#fff;stroke-width:3}} .town.end text{{font-size:32px;font-weight:800;fill:#f1d98a}}
.road{{fill:none;stroke:#d4af37;stroke-width:7;stroke-linecap:round;stroke-linejoin:round}}
.roadglow{{fill:none;stroke:#f1d98a;stroke-opacity:.25;stroke-width:22;stroke-linecap:round;stroke-linejoin:round}}
.base{{fill:none;stroke:#ffffff;stroke-opacity:.12;stroke-width:4;stroke-dasharray:2 12;stroke-linecap:round}}
.cab{{filter:drop-shadow(0 4px 10px rgba(0,0,0,.5))}}
.panel{{position:absolute;left:1070px;top:70px;width:470px;height:760px;padding:44px 40px;border-radius:30px;background:rgba(9,22,12,.72);border:1px solid rgba(241,217,138,.28);display:flex;flex-direction:column;gap:10px;color:#fff}}
.kick{{font-size:20px;font-weight:800;letter-spacing:.3em;color:#d4af37}}
.big{{font-size:62px;font-weight:800;line-height:1.02;letter-spacing:-.01em}}
.arrow{{display:block;width:140px;height:8px;margin:6px 0}} .arrow i{{display:block;width:100%;height:8px;border-radius:4px;background:#d4af37}}
.stats{{display:flex;gap:18px;margin-top:22px}}
.stats div{{flex:1;background:rgba(255,255,255,.07);border-radius:18px;padding:18px 18px}}
.stats b{{display:block;white-space:nowrap;font-size:30px;font-weight:800;color:#f1d98a;line-height:1.1}} .stats span{{font-size:18px;color:#cfe0d4;font-weight:500}}
.via{{font-size:22px;color:#e8efe9;margin-top:16px;line-height:1.4;font-weight:500}}
.list{{list-style:none;margin-top:14px;display:flex;flex-direction:column;gap:14px}}
.list li{{font-size:30px;font-weight:700;display:flex;align-items:center;gap:16px;color:#e8efe9;opacity:.45}}
.list li i{{display:block;width:16px;height:16px;border-radius:50%;background:#d4af37;flex:0 0 16px}}
.brand{{margin-top:auto;font-size:18px;font-weight:800;letter-spacing:.3em;color:#f1d98a;opacity:.85}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="{W}" data-height="{H}">
<div class="scene clip" id="scene" data-start="0" data-duration="{DUR}" data-track-index="0">
<svg class="map" viewBox="0 0 {W} {H}" data-layout-allow-overflow>
 <g class="grid">{"".join(grid)}</g>
 <path class="zone" d="{zone}"/>
 <g class="glyph">{"".join(glyphs)}</g>
 {"".join(f'<path class="base" d="{d}"/>' for d in paths)}
 {"".join(f'<path class="roadglow" id="g{i}" d="{d}"/><path class="road" id="r{i}" d="{d}"/>' for i, d in enumerate(paths))}
 {"".join(towns)}
 <g class="cab" id="cab"><circle r="20" fill="#d4af37"/><circle r="20" fill="none" stroke="#fff" stroke-width="4"/>
   <path d="M-11 3 L-9 -4 L-4 -8 L6 -8 L10 -3 L12 3 L12 6 L-12 6 Z" fill="#122615"/><circle cx="-6" cy="7" r="3.2" fill="#fff"/><circle cx="7" cy="7" r="3.2" fill="#fff"/></g>
</svg>
<div class="panel" data-layout-allow-overflow>{panel}</div>
</div></div>
<script>
const C={cfg};
const tl=gsap.timeline({{paused:true}});
const roads=[...Array(C.n).keys()].map(i=>document.getElementById("r"+i));
const glows=[...Array(C.n).keys()].map(i=>document.getElementById("g"+i));
const lens=roads.map(r=>r.getTotalLength());
roads.forEach((r,i)=>{{gsap.set([r,glows[i]],{{strokeDasharray:lens[i],strokeDashoffset:lens[i]}});}});
const cab=document.getElementById("cab");
function place(i,t){{const p=roads[i].getPointAtLength(lens[i]*t);cab.setAttribute("transform","translate("+p.x+" "+p.y+")");}}
place(0,0);
gsap.set(cab,{{opacity:0}});
const towns=[...Array(C.labels).keys()].map(i=>document.getElementById("t"+i));
towns.forEach((t,i)=>{{gsap.set(t,{{opacity:(i===0?1:.5)}});}});
if(C.mode==="path"){{
  const drawStart=0.6, drawDur=5.0;
  tl.fromTo(cab,{{opacity:0}},{{opacity:1,duration:0.3}},drawStart-0.3);
  tl.fromTo([roads[0],glows[0]],{{strokeDashoffset:lens[0]}},{{strokeDashoffset:0,duration:drawDur,ease:"power1.inOut"}},drawStart);
  const prox={{t:0}};
  tl.fromTo(prox,{{t:0}},{{t:1,duration:drawDur,ease:"power1.inOut",onUpdate:()=>place(0,prox.t)}},drawStart);
  // light up towns in order of distance along the road
  const samples=200;const pts=[...Array(samples+1).keys()].map(j=>roads[0].getPointAtLength(lens[0]*j/samples));
  towns.forEach((t,i)=>{{
    if(i===0) return;
    const x=+t.dataset.x,y=+t.dataset.y;let best=0,bd=1e9;
    pts.forEach((p,j)=>{{const d=(p.x-x)**2+(p.y-y)**2;if(d<bd){{bd=d;best=j;}}}});
    const f=best/samples;
    tl.fromTo(t,{{opacity:.5}},{{opacity:1,duration:0.3}},drawStart+drawDur*f-0.1);
  }});
  const last=towns[towns.length-1].querySelector(".halo");
  tl.fromTo(last,{{fillOpacity:0,scale:.6,transformOrigin:"50% 50%"}},{{fillOpacity:.45,scale:1.6,duration:0.9,ease:"power2.out",yoyo:true,repeat:1}},drawStart+drawDur);
  tl.to([roads[0],glows[0]],{{opacity:0,duration:0.7}},8.0);
  tl.to(cab,{{opacity:0,duration:0.5}},8.0);
  tl.to(towns.slice(1),{{opacity:.5,duration:0.6}},8.1);
  tl.set([roads[0],glows[0]],{{strokeDashoffset:lens[0]}},8.85);
  tl.set([roads[0],glows[0]],{{opacity:1}},8.9);
}} else {{
  const per=7.2/C.n;
  const hubHalo=towns[0].querySelector(".halo");
  tl.fromTo(hubHalo,{{fillOpacity:0,scale:.6,transformOrigin:"50% 50%"}},{{fillOpacity:.4,scale:1.5,duration:0.6,yoyo:true,repeat:1}},0.1);
  roads.forEach((r,i)=>{{
    const t0=0.4+i*per, d=per*0.8; const prox={{t:0}};
    tl.fromTo([r,glows[i]],{{strokeDashoffset:lens[i]}},{{strokeDashoffset:0,duration:d,ease:"power1.inOut"}},t0);
    tl.fromTo(prox,{{t:0}},{{t:1,duration:d,ease:"power1.inOut",onUpdate:()=>place(i,prox.t)}},t0);
    tl.fromTo(towns[i+1],{{opacity:.5}},{{opacity:1,duration:0.3}},t0+d-0.2);
    const li=document.getElementById("li"+i); if(li) tl.fromTo(li,{{opacity:.45}},{{opacity:1,duration:0.3}},t0+d-0.2);
  }});
  tl.fromTo(cab,{{opacity:0}},{{opacity:1,duration:0.3}},0.2);
  tl.to(cab,{{opacity:0,duration:0.4}},8.0);
  tl.to([...roads,...glows],{{opacity:0,duration:0.6}},8.1);
  tl.to(towns.slice(1),{{opacity:.5,duration:0.6}},8.1);
  tl.to([...document.querySelectorAll(".list li")],{{opacity:.45,duration:0.6}},8.1);
  tl.set([...roads,...glows],{{strokeDashoffset:(i,el)=>el.getTotalLength()}},8.85);
  tl.set([...roads,...glows],{{opacity:1}},8.9);
}}
window.__timelines["main"]=tl;
</script></body></html>'''
    d = HF / "routes" / p["slug"]
    (d / "assets").mkdir(parents=True, exist_ok=True)
    for f in FONTS.glob("*.woff2"):
        shutil.copy(f, d / "assets" / f.name)
    for f in ["package.json", "hyperframes.json", "meta.json"]:
        shutil.copy(SCAFFOLD / f, d / f)
    (d / "index.html").write_text(html)
    return d

if __name__ == "__main__":
    want = sys.argv[1:]
    for p in PAGES:
        if not want or p["slug"] in want:
            print(build(p))
