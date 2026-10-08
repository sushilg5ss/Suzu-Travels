#!/usr/bin/env python3
"""Suzu Cabs hub hero — 1920x1080, 12 s seamless loop: parallax Himalaya, winding road, Suzu-branded SUV, cycling route names.
Output: cab-hero/index.html"""
import math, random, pathlib, sys
import os, pathlib as _pl
KIT = _pl.Path(__file__).resolve().parent
SCAFFOLD = KIT / "hf-scaffold"
HF_OUT = _pl.Path(os.environ.get("CAB_HF_OUT", str(KIT.parent.parent / "cab-hf")))
sys.path.insert(0, str(KIT))
W, H, DUR = 1920, 1080, 12
rng = random.Random(7)

def ridge(n, ymin, ymax, seed, jag=0.0):
    r = random.Random(seed)
    pts = []
    step = W / n
    ys = [r.uniform(ymin, ymax) for _ in range(n)]
    ys.append(ys[0])  # seamless tile
    for i, y in enumerate(ys):
        pts.append((i * step, y))
    # add jagged mid points
    out = []
    for i in range(len(pts) - 1):
        (x0, y0), (x1, y1) = pts[i], pts[i + 1]
        out.append((x0, y0))
        if jag:
            mx = (x0 + x1) / 2 + r.uniform(-step * .15, step * .15)
            my = (y0 + y1) / 2 + r.uniform(-jag, jag)
            out.append((mx, my))
    out.append(pts[-1])
    return out

def tile_path(pts, base):
    d = "M0 %d " % base + " ".join("L%.1f %.1f" % p for p in pts) + " L%d %d Z" % (W, base)
    return d

def snow(pts, depth):
    polys = []
    for i in range(1, len(pts) - 1):
        x, y = pts[i]
        if y < pts[i - 1][1] and y < pts[i + 1][1]:
            lx = x + (pts[i - 1][0] - x) * .28; ly = y + (pts[i - 1][1] - y) * .28
            rx = x + (pts[i + 1][0] - x) * .28; ry = y + (pts[i + 1][1] - y) * .28
            polys.append(f'<path d="M{lx:.1f} {ly:.1f} L{x:.1f} {y:.1f} L{rx:.1f} {ry:.1f} L{(x+rx)/2:.1f} {ry-depth*.2:.1f} L{x:.1f} {ly+depth*.35:.1f} Z" fill="#f5f2e8" opacity=".92"/>')
    return "".join(polys)

far = ridge(9, 300, 470, 11, jag=40)
mid = ridge(7, 520, 640, 23, jag=25)

def layer(pts, base, fill, extra=""):
    one = f'<path d="{tile_path(pts, base)}" fill="{fill}"/>{extra}'
    return f'<g>{one}</g><g transform="translate({W} 0)">{one}</g><g transform="translate({2*W} 0)">{one}</g><g transform="translate({3*W} 0)">{one}</g>'

def trees(seed, y, h, count, color):
    r = random.Random(seed)
    s = []
    for i in range(count):
        x = i * W / count + r.uniform(-30, 30)
        hh = h * r.uniform(.7, 1.15)
        s.append(f'<path d="M{x:.0f} {y-hh:.0f} L{x+hh*.28:.0f} {y:.0f} L{x-hh*.28:.0f} {y:.0f} Z" fill="{color}"/>')
    one = "".join(s)
    return "".join(f'<g transform="translate({k*W} 0)">{one}</g>' for k in range(4))

# poles / km stones on road side
def posts():
    one = "".join(f'<g transform="translate({x} 0)"><rect x="0" y="846" width="10" height="30" rx="2" fill="#f4f1e6"/><rect x="0" y="846" width="10" height="9" rx="2" fill="#d4af37"/></g>' for x in range(80, W, 480))
    return "".join(f'<g transform="translate({k*W} 0)">{one}</g>' for k in range(4))

def car(kind="crysta"):
    from vehicles_svg import V
    v = V[kind]
    pts = " ".join(f"{x},{y}" for x, y in v["body"])
    wins = "".join(f'<polygon points="{" ".join(f"{x},{y}" for x,y in w)}" fill="url(#glass)"/>' for w in v["win"])
    x0, x1 = v["wheels"][0] + 24, v["wheels"][1] - 24
    wheels = "".join(f'<circle cx="{wx}" cy="106" r="24" fill="#0f1a13"/>' for wx in v["wheels"])
    rims = "".join(
        f'<g transform="translate({wx} 106)"><circle r="19" fill="#161b18"/><g class="rim"><circle r="11" fill="#a9b1ab"/><path d="M0-11V11M-11 0H11M-8-8L8 8M-8 8L8-8" stroke="#5d655f" stroke-width="2.4"/></g><circle r="3.5" fill="#d4af37"/></g>'
        for wx in v["wheels"])
    return (f'<svg viewBox="0 0 320 140" width="720" height="315" xmlns="http://www.w3.org/2000/svg"><defs>'
            f'<linearGradient id="body" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#cfd6d1"/></linearGradient>'
            f'<linearGradient id="glass" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#3b5d66"/><stop offset=".55" stop-color="#15252a"/><stop offset="1" stop-color="#e9c778" stop-opacity=".8"/></linearGradient></defs>'
            f'<polygon points="{pts}" fill="url(#body)" stroke="#122615" stroke-opacity=".3" stroke-width="1.2" stroke-linejoin="round"/>'
            f'<rect x="{min(x for x,_ in v["body"])+2}" y="99" width="{max(x for x,_ in v["body"])-min(x for x,_ in v["body"])-4}" height="7" rx="3" fill="#1b2620" opacity=".9"/>{wheels}{wins}'
            f'<rect x="{x0}" y="80" width="{x1-x0}" height="15" rx="3" fill="#d4af37"/>'
            f'<text x="{(x0+x1)/2}" y="91.5" text-anchor="middle" font-family="SuzuSans" font-size="9.5" font-weight="800" letter-spacing="2" fill="#122615">SUZU TRAVELS</text>'
            f'<rect x="{max(x for x,_ in v["body"])-14}" y="70" width="12" height="6" rx="2" fill="#fff3c4"/><rect x="{min(x for x,_ in v["body"])-1}" y="72" width="7" height="8" rx="2" fill="#c0392b"/>{rims}</svg>')

def make(out, routes, kicker="SUZU TRAVELS · CABS", vehicle="crysta"):
  ROUTES = routes
  single = len(ROUTES) == 1
  def one(i, r):
    if len(r) == 2 and r[1]:
      return f'<div class="rt" id="rt{i}"><span class="a">{r[0]}</span><span class="arrow"><i></i></span><span class="b">{r[1]}</span></div>'
    return f'<div class="rt" id="rt{i}"><span class="a">{r[0]}</span></div>'
  route_html = "".join(one(i, r) for i, r in enumerate(ROUTES))

  html = f'''<!doctype html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width={W}, height={H}">
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
<style>
@font-face{{font-family:"SuzuSans";src:url("assets/plus-jakarta-sans-latin-800-normal.woff2") format("woff2");font-weight:800}}
@font-face{{font-family:"SuzuSans";src:url("assets/plus-jakarta-sans-latin-700-normal.woff2") format("woff2");font-weight:700}}
@font-face{{font-family:"SuzuSans";src:url("assets/plus-jakarta-sans-latin-500-normal.woff2") format("woff2");font-weight:500}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{margin:0;width:{W}px;height:{H}px;overflow:hidden;background:#10281a}}
#root{{position:relative;width:100%;height:100%;overflow:hidden;font-family:"SuzuSans",sans-serif}}
.scene{{position:absolute;inset:0;width:100%;height:100%}}
.sky{{position:absolute;inset:0;background:linear-gradient(180deg,#0d2216 0%,#1f4a30 38%,#9aa56a 66%,#f0cf7e 82%,#f6dd97 100%)}}
.sun{{position:absolute;left:1420px;top:250px;width:260px;height:260px;border-radius:50%;background:radial-gradient(circle,#fff6d2 0%,#f7d77c 40%,rgba(247,215,124,0) 70%)}}
.lyr{{position:absolute;left:0;top:0;width:{4*W}px;height:{H}px}}
.road{{position:absolute;left:0;top:870px;width:100%;height:210px;background:linear-gradient(180deg,#2a302c 0%,#1a1e1b 100%)}}
.edge{{position:absolute;left:0;top:862px;width:100%;height:10px;background:#d4af37}}
.dash{{position:absolute;left:0;top:966px;width:{W}px;height:10px;background:repeating-linear-gradient(90deg,#f5f1e3 0 90px,transparent 90px 160px)}}
.car{{position:absolute;left:980px;top:652px;width:720px;height:315px}}
.shadow{{position:absolute;left:1000px;top:945px;width:680px;height:30px;border-radius:50%;background:rgba(0,0,0,.45);filter:blur(10px)}}
.streak{{position:absolute;height:4px;border-radius:4px;background:linear-gradient(90deg,rgba(255,255,255,0),rgba(255,255,255,.55))}}
.brand{{position:absolute;left:1050px;top:120px;width:760px;display:flex;flex-direction:column;align-items:flex-end;gap:14px}}
.kick{{font-size:30px;font-weight:800;letter-spacing:.32em;color:#f1d98a}}
.rtbox{{position:relative;width:760px;height:120px}}
.rt{{position:absolute;right:0;top:0;height:120px;display:flex;align-items:center;gap:26px;color:#fff;font-size:76px;font-weight:800;letter-spacing:-.01em;opacity:0;text-shadow:0 6px 30px rgba(0,0,0,.35)}}
.rt .arrow{{display:block;width:120px;height:8px;position:relative}}
.rt .arrow i{{display:block;width:100%;height:8px;border-radius:4px;background:#d4af37}}
.bar{{width:220px;height:6px;border-radius:3px;background:#d4af37}}
</style></head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="{W}" data-height="{H}">
 <div class="scene clip" data-start="0" data-duration="{DUR}" data-track-index="0">
  <div class="sky"></div><div class="sun" id="sun"></div>
  <svg class="lyr" id="far" viewBox="0 0 {4*W} {H}">{layer(far, 760, "#6f8a8a", snow(far, 70))}</svg>
  <svg class="lyr" id="mid" viewBox="0 0 {4*W} {H}">{layer(mid, 880, "#2f5a3d")}{trees(5, 700, 70, 26, "#244a31")}</svg>
  <svg class="lyr" id="near" viewBox="0 0 {4*W} {H}"><rect x="0" y="780" width="{4*W}" height="90" fill="#17361f"/>{trees(9, 800, 150, 12, "#0f2616")}{posts()}</svg>
  <div class="road"></div><div class="edge"></div><div class="dash" id="dash"></div>
  <div class="streak" id="s1" style="left:760px;top:760px;width:180px"></div>
  <div class="streak" id="s2" style="left:820px;top:840px;width:240px"></div>
  <div class="streak" id="s3" style="left:700px;top:900px;width:150px"></div>
  <div class="shadow"></div>
  <div class="car" id="car">{car(vehicle)}</div>
  <div class="brand"><div class="kick">{kicker}</div><div class="rtbox" data-layout-allow-overlap>{route_html}</div><div class="bar"></div></div>
 </div>
</div>
<script>
const tl = gsap.timeline({{paused:true}});
tl.fromTo("#far",{{x:0}},{{x:-{W},duration:{DUR},ease:"none"}},0);
tl.fromTo("#mid",{{x:0}},{{x:-{2*W},duration:{DUR},ease:"none"}},0);
tl.fromTo("#near",{{x:0}},{{x:-{3*W},duration:{DUR},ease:"none"}},0);
tl.fromTo("#dash",{{backgroundPositionX:"0px"}},{{backgroundPositionX:"-{160*60}px",duration:{DUR},ease:"none"}},0);
tl.fromTo(".rim",{{rotation:0}},{{rotation:360*36,duration:{DUR},ease:"none",transformOrigin:"50% 50%"}},0);
tl.fromTo("#car",{{y:0}},{{y:-5,duration:0.5,ease:"sine.inOut",yoyo:true,repeat:{int(DUR/0.5)-1}}},0);
["#s1","#s2","#s3"].forEach((s,i)=>{{tl.fromTo(s,{{x:0,opacity:0}},{{x:-520,opacity:1,duration:0.75,ease:"none",repeat:{int(DUR/1.5)-1},repeatDelay:0.75}},0.25*i);}});
tl.fromTo("#sun",{{scale:1}},{{scale:1.06,duration:3,ease:"sine.inOut",yoyo:true,repeat:3}},0);
{"gsap.set('#rt0',{opacity:1});" if single else ""}
{"" if single else "for(let i=0;i<"+str(len(ROUTES))+";i++){const t0=i*3;tl.fromTo('#rt'+i,{opacity:0,x:60},{opacity:1,x:0,duration:0.5,ease:'power3.out'},t0+0.05);tl.to('#rt'+i,{opacity:0,x:-60,duration:0.45,ease:'power2.in'},t0+2.5);}"}
window.__timelines["main"] = tl;
</script>
</body></html>'''
  d = pathlib.Path(out); (d/"assets").mkdir(parents=True, exist_ok=True)
  import shutil
  for f in (SCAFFOLD / "assets").glob("*.woff2"):
      if not (d/"assets"/f.name).exists(): shutil.copy(f, d/"assets"/f.name)
  for f in ["package.json","hyperframes.json","meta.json"]:
      if not (d/f).exists(): shutil.copy(SCAFFOLD / f, d/f)
  (d/"index.html").write_text(html)
  return d

VARIANTS = {
  "hub": dict(routes=[("Delhi","Shimla"),("Chandigarh","Manali"),("Pathankot","Dharamshala"),("Jammu","Srinagar")]),
  "delhi-to-shimla-taxi": dict(routes=[("Delhi","Shimla")], kicker="ONE-WAY · ROUND TRIP"),
  "delhi-to-manali-taxi": dict(routes=[("Delhi","Manali")], kicker="ONE-WAY · ROUND TRIP"),
  "chandigarh-to-manali-taxi": dict(routes=[("Chandigarh","Manali")], kicker="ONE-WAY · ROUND TRIP"),
  "chandigarh-to-shimla-taxi": dict(routes=[("Chandigarh","Shimla")], kicker="ONE-WAY · ROUND TRIP"),
  "delhi-to-chandigarh-taxi": dict(routes=[("Delhi","Chandigarh")], kicker="ONE-WAY · BOTH WAYS"),
  "delhi-to-dehradun-taxi": dict(routes=[("Delhi","Dehradun")], kicker="VIA THE NEW EXPRESSWAY"),
  "pathankot-to-dharamshala-taxi": dict(routes=[("Pathankot","Dharamshala")], kicker="STATION · AIRPORT PICKUP"),
  "jammu-to-srinagar-taxi": dict(routes=[("Jammu","Srinagar")], kicker="THROUGH THE BANIHAL TUNNELS"),
  "delhi-to-haridwar-taxi": dict(routes=[("Delhi","Haridwar")], kicker="HAR KI PAURI · GANGA AARTI"),
  "delhi-to-rishikesh-taxi": dict(routes=[("Delhi","Rishikesh")], kicker="TAPOVAN · SHIVPURI CAMPS"),
  "delhi-to-amritsar-taxi": dict(routes=[("Delhi","Amritsar")], kicker="GOLDEN TEMPLE · WAGAH"),
  "manali-taxi-service": dict(routes=[("Manali taxis",None)], kicker="SOLANG · ATAL TUNNEL · ROHTANG"),
  "shimla-taxi-service": dict(routes=[("Shimla taxis",None)], kicker="KUFRI · CHAIL · NARKANDA"),
  "chandigarh-taxi-service": dict(routes=[("Chandigarh taxis",None)], kicker="AIRPORT · TRICITY · HILLS"),
  "delhi-to-mussoorie-taxi": dict(routes=[("Delhi","Mussoorie")], kicker="KEMPTY FALLS · LANDOUR"),
  "shimla-to-manali-taxi": dict(routes=[("Shimla","Manali")], kicker="MANDI · KULLU VALLEY · BEAS"),
  "dehradun-taxi-service": dict(routes=[("Dehradun taxis",None)], kicker="JOLLY GRANT · MUSSOORIE"),
  "dharamshala-taxi-service": dict(routes=[("Dharamshala taxis",None)], kicker="MCLEODGANJ · BIR · GAGGAL"),
  "srinagar-taxi-service": dict(routes=[("Srinagar taxis",None)], kicker="GULMARG · PAHALGAM · DAL"),
  "tempo-traveller-hire-delhi": dict(routes=[("Tempo Traveller",None)], kicker="12–17 SEATS · DELHI NCR", vehicle="tempo"),
  "innova-crysta-on-rent": dict(routes=[("Innova Crysta",None)], kicker="ON RENT WITH DRIVER"),
}
if __name__ == "__main__":
  want = sys.argv[1:] or list(VARIANTS)
  for k in want:
      print(make(str(HF_OUT / "heroes" / k), **VARIANTS[k]))
