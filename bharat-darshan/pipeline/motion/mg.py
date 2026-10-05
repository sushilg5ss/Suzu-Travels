#!/usr/bin/env python3
"""Suzu Travels — English motion-graphics reel builder (HyperFrames, 1080x1920).

usage: mg.py SPEC.json OUT_DIR
Scene types: photo (Ken Burns + kinetic headline + optional stat), map (India outline, pins, route),
list (numbered points), end (brand card).  All timing absolute (seconds) via "start"/"dur".
"""
import json, math, os, shutil, sys, html
from PIL import Image, ImageEnhance, ImageFilter

W, H = 1080, 1920
HERE = os.path.dirname(os.path.abspath(__file__))
GOLD, GOLD2, EM, EM2 = "#F2C84B", "#D4AF37", "#122615", "#2E7D32"
esc = lambda s: html.escape(str(s))

CITIES = {  # lon, lat
    "Delhi": (77.21, 28.61), "Agra": (78.01, 27.18), "Jaipur": (75.79, 26.91), "Varanasi": (83.01, 25.32),
    "Kochi": (76.27, 9.93), "Leh": (77.58, 34.16), "Manali": (77.19, 32.24), "Goa": (73.83, 15.49),
    "Mumbai": (72.88, 19.08), "Jaisalmer": (70.91, 26.92), "Darjeeling": (88.26, 27.04), "Hampi": (76.46, 15.34),
    "Amritsar": (74.87, 31.63), "Shimla": (77.17, 31.10), "Udaipur": (73.71, 24.58), "Rishikesh": (78.27, 30.09),
    "Kolkata": (88.36, 22.57), "Chennai": (80.27, 13.08), "Bengaluru": (77.59, 12.97), "Khajuraho": (79.92, 24.85),
    "Munnar": (77.06, 10.09), "Thekkady": (77.16, 9.60), "Alleppey": (76.34, 9.49),
}


def prep(src_dir, out_dir, name, grade="warm"):
    im = Image.open(os.path.join(src_dir, name)).convert("RGB")
    im.thumbnail((2400, 2400))
    if grade == "dark":
        im = ImageEnhance.Brightness(ImageEnhance.Contrast(im).enhance(1.08)).enhance(0.7)
    elif grade == "mono":
        im = ImageEnhance.Contrast(im.convert("L").convert("RGB")).enhance(1.2)
    else:
        im = ImageEnhance.Contrast(ImageEnhance.Color(im).enhance(1.1)).enhance(1.05)
    fn = os.path.splitext(name)[0] + f"-{grade}.jpg"
    im.save(os.path.join(out_dir, fn), quality=88)
    return fn, im.size


def words_html(lines, cls, idp, tag="div"):
    out = [f'<{tag} class="{cls}" id="{idp}">']
    for li, line in enumerate(lines):
        out.append('<span class="ln">')
        for wi, w in enumerate(line.split(" ")):
            cw = "w gold" if w.startswith("*") else "w"
            out.append(f'<span class="{cw}"><span class="wi" id="{idp}-w{li}-{wi}">{esc(w.lstrip("*"))}</span></span> ')
        out.append("</span>")
    out.append(f"</{tag}>")
    return "".join(out)


def words_js(idp, lines, t0, step=0.07, dur=0.6):
    js, k = [], 0
    for li, line in enumerate(lines):
        for wi, _ in enumerate(line.split(" ")):
            js.append(f'tl.fromTo("#{idp}-w{li}-{wi}",{{yPercent:110,rotate:4,opacity:0}},{{yPercent:0,rotate:0,opacity:1,duration:{dur},ease:"power4.out"}},{t0+k*step:.3f});')
            k += 1
    return js


def build(spec_path, out_dir):
    spec = json.load(open(spec_path))
    src_dir = spec.get("img_dir", os.path.join(os.path.dirname(os.path.abspath(spec_path)), "img"))
    os.makedirs(os.path.join(out_dir, "img"), exist_ok=True)
    os.makedirs(os.path.join(out_dir, "assets", "fonts"), exist_ok=True)
    for f in os.listdir(os.path.join(HERE, "fonts")):
        shutil.copy(os.path.join(HERE, "fonts", f), os.path.join(out_dir, "assets", "fonts", f))
    for f in ("gsap.min.js", "suzu-logo.png", "grain.png"):
        shutil.copy(os.path.join(HERE, "assets", f), os.path.join(out_dir, "assets", f))
    india = json.load(open(os.path.join(HERE, "data", "india.json")))
    total = spec["duration"]
    body, js, css_extra = [], [], []

    for si, sc in enumerate(spec["scenes"]):
        S, D = sc["start"], sc["dur"]
        p = f"s{si}"
        typ = sc["type"]
        inner = []
        # ---------- background ----------
        if sc.get("img"):
            fn, (iw, ih) = prep(src_dir, os.path.join(out_dir, "img"), sc["img"], sc.get("grade", "warm"))
            fx, fy = sc.get("focus", [0.5, 0.5])
            s0 = max(W / iw, H / ih)
            dw, dh = iw * s0, ih * s0
            left, top = min(0, max(W - dw, W / 2 - fx * dw)), min(0, max(H - dh, H / 2 - fy * dh))
            z0, z1 = sc.get("zoom", [1.12, 1.0])
            px, py = sc.get("pan", [0, 0])
            inner.append(f'<div class="mover" id="{p}-m" style="left:{left:.1f}px;top:{top:.1f}px;width:{dw:.1f}px;height:{dh:.1f}px;transform-origin:{fx*100:.1f}% {fy*100:.1f}%"><img class="ph" src="img/{fn}" alt=""></div>')
            js.append(f'tl.fromTo("#{p}-m",{{scale:{z0},x:0,y:0}},{{scale:{z1},x:{px},y:{py},duration:{D+0.6:.2f},ease:"sine.inOut"}},{S:.3f});')
            inner.append('<div class="shade"></div>')
        else:
            inner.append('<div class="embg"></div>')
        # ---------- scene content ----------
        if typ == "photo":
            if sc.get("kicker"):
                inner.append(f'<div class="kicker" id="{p}-k">{esc(sc["kicker"])}</div>')
                js.append(f'tl.fromTo("#{p}-k",{{opacity:0,x:-30}},{{opacity:1,x:0,duration:0.6,ease:"power3.out"}},{S+0.25:.3f});')
            if sc.get("days"):  # itinerary day strip: {"total":7,"on":[2,3]}
                dy = sc["days"]; tot = dy.get("total", 7); on = set(dy.get("on", []))
                cells = "".join(f'<div class="dcell{" on" if d in on else ""}" id="{p}-d{d}">{d}</div>' for d in range(1, tot + 1))
                inner.append(f'<div class="days" id="{p}-days"><span class="dlab">DAY</span>{cells}</div>')
                t0 = S + dy.get("at", 0.15)
                js.append(f'tl.fromTo("#{p}-days .dcell",{{opacity:0,y:18}},{{opacity:1,y:0,duration:0.35,stagger:0.05,ease:"power3.out"}},{t0:.3f});')
                js.append(f'tl.fromTo("#{p}-days .dlab",{{opacity:0}},{{opacity:1,duration:0.4}},{t0:.3f});')
                for j, d in enumerate(sorted(on)):
                    js.append(f'tl.fromTo("#{p}-d{d}",{{scale:1}},{{scale:1.22,duration:0.22,yoyo:true,repeat:1,ease:"power2.out"}},{t0+0.45+tot*0.05+j*0.12:.3f});')
            if sc.get("headline"):
                pos = sc.get("pos", "low")
                inner.append(words_html(sc["headline"], f"hl hl-{pos}", f"{p}-h").replace('id="%s-h"' % p, 'id="%s-h" style="font-size:%dpx"' % (p, sc.get("hl_size", 150)), 1))
                js += words_js(f"{p}-h", sc["headline"], S + sc.get("t_head", 0.35))
            if sc.get("sub"):
                inner.append(f'<div class="sub" id="{p}-sub">{esc(sc["sub"])}</div>')
                js.append(f'tl.fromTo("#{p}-sub",{{opacity:0,y:24}},{{opacity:1,y:0,duration:0.7,ease:"power3.out"}},{S+sc.get("t_sub",1.2):.3f});')
            if sc.get("stat"):
                st = sc["stat"]
                inner.append(f'<div class="stat" id="{p}-st"><div class="stat-n" id="{p}-stn">{esc(st.get("prefix",""))}0{esc(st.get("suffix",""))}</div><div class="stat-l">{esc(st["label"])}</div></div>')
                t = S + st.get("at", 0.4)
                js.append(f'tl.fromTo("#{p}-st",{{opacity:0,y:40}},{{opacity:1,y:0,duration:0.5,ease:"power3.out"}},{t:.3f});')
                js.append(f'(function(){{var o={{v:{st.get("from",0)}}};tl.to(o,{{v:{st["num"]},duration:{st.get("cdur",1.2)},ease:"power2.out",onUpdate:function(){{document.getElementById("{p}-stn").textContent="{st.get("prefix","")}"+o.v.toLocaleString("en-US",{{minimumFractionDigits:{st.get("decimals",0)},maximumFractionDigits:{st.get("decimals",0)}}})+"{st.get("suffix","")}";}}}},{t:.3f});}})();')
            if sc.get("tag"):
                inner.append(f'<div class="tag" id="{p}-tag">{esc(sc["tag"])}</div>')
                js.append(f'tl.fromTo("#{p}-tag",{{opacity:0,scale:0.8}},{{opacity:1,scale:1,duration:0.5,ease:"back.out(2)"}},{S+sc.get("t_tag",1.0):.3f});')
        if typ == "map":
            mw = sc.get("map_w", 820)
            k = mw / india["W"]
            mh = india["H"] * k
            mx, my = (W - mw) / 2 + sc.get("map_dx", 0), sc.get("map_y", 560)
            def P(lon, lat):
                return ((lon - india["minx"]) * india["k"] * india["s"] * k + mx, (india["maxy"] - lat) * india["s"] * k + my)
            svg = [f'<svg class="map" viewBox="0 0 {W} {H}" width="{W}" height="{H}">']
            svg.append(f'<defs><filter id="{p}-glow"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>')
            zm = sc.get("zoom_map")  # {"scale":2.4,"at":2.0,"dur":1.4}
            zs = zm["scale"] if zm else 1.0
            svg.append(f'<g id="{p}-cam">')
            svg.append(f'<g transform="translate({mx:.1f},{my:.1f}) scale({k:.5f})"><path d="{india["d"]}" fill="rgba(46,125,50,.28)" stroke="none" id="{p}-fill" opacity="0"/><path d="{india["d"]}" fill="none" stroke="{GOLD}" stroke-width="{2.6/k:.2f}" stroke-linejoin="round" id="{p}-outline" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/></g>')
            js.append(f'tl.to("#{p}-outline",{{strokeDashoffset:0,duration:{sc.get("draw",2.2)},ease:"power2.inOut"}},{S+0.2:.3f});')
            js.append(f'tl.to("#{p}-fill",{{opacity:1,duration:0.8}},{S+1.6:.3f});')
            pts = {}
            for i, pin in enumerate(sc.get("pins", [])):
                lon, lat = CITIES[pin["city"]] if "city" in pin else (pin["lon"], pin["lat"])
                x, y = P(lon, lat); pts[pin.get("city", i)] = (x, y)
                t = S + pin.get("at", 1.0 + i * 0.35)
                side = pin.get("side", "r")
                lx = x + 26 if side == "r" else x - 26
                anchor = "start" if side == "r" else "end"
                lx = x + 26/zs if side == "r" else x - 26/zs
                svg.append(f'<g id="{p}-pin{i}" style="transform-origin:{x:.1f}px {y:.1f}px"><circle cx="{x:.1f}" cy="{y:.1f}" r="{22/zs:.1f}" fill="{GOLD}" opacity=".25"/><circle cx="{x:.1f}" cy="{y:.1f}" r="{10/zs:.1f}" fill="{GOLD}" filter="url(#{p}-glow)"/>'
                           f'<text x="{lx:.1f}" y="{y+12/zs:.1f}" text-anchor="{anchor}" class="pinlab" style="font-size:{34/zs:.1f}px;stroke-width:{8/zs:.1f}px">{esc(pin.get("label", pin.get("city","")))}</text></g>')
                js.append(f'tl.fromTo("#{p}-pin{i}",{{scale:0,opacity:0}},{{scale:1,opacity:1,duration:0.45,ease:"back.out(2.5)"}},{t:.3f});')
            if sc.get("route"):
                r = sc["route"]; seq = r["cities"]
                d = "M" + " L".join(f"{pts[c][0]:.1f},{pts[c][1]:.1f}" for c in seq)
                if r.get("close"): d += " Z"
                svg.append(f'<path d="{d}" fill="none" stroke="#fff" stroke-width="{5/zs:.2f}" stroke-linecap="round" stroke-dasharray="1" stroke-dashoffset="1" pathLength="1" id="{p}-route" filter="url(#{p}-glow)"/>')
                js.append(f'tl.to("#{p}-route",{{strokeDashoffset:0,duration:{r.get("draw",2.0)},ease:"power2.inOut"}},{S+r.get("at",2.4):.3f});')
                for j, lab in enumerate(r.get("labels", [])):
                    a, b = pts[seq[j]], pts[seq[(j + 1) % len(seq)]]
                    cx, cy = (a[0] + b[0]) / 2 + lab.get("dx", 0), (a[1] + b[1]) / 2 + lab.get("dy", 0)
                    cx, cy = (a[0] + b[0]) / 2 + lab.get("dx", 0)/zs, (a[1] + b[1]) / 2 + lab.get("dy", 0)/zs
                    svg.append(f'<g id="{p}-rl{j}"><rect x="{cx-92/zs:.1f}" y="{cy-26/zs:.1f}" width="{184/zs:.1f}" height="{52/zs:.1f}" rx="{26/zs:.1f}" fill="{EM}" stroke="{GOLD}" stroke-width="{2/zs:.2f}"/><text x="{cx:.1f}" y="{cy+11/zs:.1f}" text-anchor="middle" class="rlab" style="font-size:{28/zs:.1f}px">{esc(lab["text"])}</text></g>')
                    js.append(f'tl.fromTo("#{p}-rl{j}",{{opacity:0,y:14}},{{opacity:1,y:0,duration:0.4}},{S+r.get("at",2.4)+r.get("draw",2.0)*(j+0.7)/max(1,len(r["labels"])):.3f});')
            svg.append("</g></svg>")
            if zm:
                cs = [pts[c] for c in zm.get("around", list(pts.keys()))]
                ox, oy = sum(c[0] for c in cs) / len(cs), sum(c[1] for c in cs) / len(cs)
                tx, ty = zm.get("to", [W / 2, 1000])
                js.append(f'tl.to("#{p}-outline",{{attr:{{"stroke-width":{2.6/k/zs*zm.get("stroke_keep",1.6):.2f}}},duration:{zm.get("dur",1.4)},ease:"power2.inOut"}},{S+zm.get("at",2.0):.3f});')
                js.append(f'tl.fromTo("#{p}-cam",{{scale:1,x:0,y:0,svgOrigin:"{ox:.1f} {oy:.1f}"}},{{scale:{zs},x:{tx-ox:.1f},y:{ty-oy:.1f},duration:{zm.get("dur",1.4)},ease:"power2.inOut"}},{S+zm.get("at",2.0):.3f});')
            inner.append("".join(svg))
            if sc.get("kicker"):
                inner.append(f'<div class="kicker top" id="{p}-k">{esc(sc["kicker"])}</div>')
                js.append(f'tl.fromTo("#{p}-k",{{opacity:0,x:-30}},{{opacity:1,x:0,duration:0.6,ease:"power3.out"}},{S+0.2:.3f});')
            if sc.get("headline"):
                inner.append(words_html(sc["headline"], "hl hl-top", f"{p}-h"))
                js += words_js(f"{p}-h", sc["headline"], S + 0.3)
            if sc.get("stat"):
                st = sc["stat"]
                inner.append(f'<div class="stat stat-bottom" id="{p}-st"><div class="stat-n" id="{p}-stn">0</div><div class="stat-l">{esc(st["label"])}</div></div>')
                t = S + st.get("at", 1.0)
                js.append(f'tl.fromTo("#{p}-st",{{opacity:0,y:40}},{{opacity:1,y:0,duration:0.5,ease:"power3.out"}},{t:.3f});')
                js.append(f'(function(){{var o={{v:0}};tl.to(o,{{v:{st["num"]},duration:{st.get("cdur",1.6)},ease:"power2.out",onUpdate:function(){{document.getElementById("{p}-stn").textContent="{st.get("prefix","")}"+o.v.toLocaleString("en-US",{{minimumFractionDigits:{st.get("decimals",0)},maximumFractionDigits:{st.get("decimals",0)}}})+"{st.get("suffix","")}";}}}},{t:.3f});}})();')
            if sc.get("sub"):
                inner.append(f'<div class="sub sub-bottom" id="{p}-sub">{esc(sc["sub"])}</div>')
                js.append(f'tl.fromTo("#{p}-sub",{{opacity:0,y:24}},{{opacity:1,y:0,duration:0.7,ease:"power3.out"}},{S+sc.get("t_sub",2.6):.3f});')
        if typ == "list":
            if sc.get("kicker"):
                inner.append(f'<div class="kicker top" id="{p}-k">{esc(sc["kicker"])}</div>')
                js.append(f'tl.fromTo("#{p}-k",{{opacity:0,x:-30}},{{opacity:1,x:0,duration:0.6,ease:"power3.out"}},{S+0.2:.3f});')
            if sc.get("headline"):
                inner.append(words_html(sc["headline"], "hl hl-top", f"{p}-h"))
                js += words_js(f"{p}-h", sc["headline"], S + 0.3)
            items = ['<div class="list" id="%s-list">' % p]
            for i, it in enumerate(sc["items"]):
                items.append(f'<div class="item" id="{p}-it{i}"><div class="num">{i+sc.get("first",1):02d}</div><div class="it-t"><div class="it-a">{esc(it["a"])}</div><div class="it-b">{esc(it.get("b",""))}</div></div></div>')
                t = S + sc.get("t_items", 1.0) + i * sc.get("step", 0.9)
                js.append(f'tl.fromTo("#{p}-it{i}",{{opacity:0,x:60}},{{opacity:1,x:0,duration:0.55,ease:"power3.out"}},{t:.3f});')
            items.append("</div>")
            inner.append("".join(items))
            js.append(f'tl.fromTo("#{p}-list",{{opacity:0,y:30}},{{opacity:1,y:0,duration:0.5,ease:"power3.out"}},{S+sc.get("t_items",1.0)-0.2:.3f});')
        if typ == "end":
            inner.append(f'''<div class="end">
<div class="halo" id="{p}-halo"></div><img class="logo" id="{p}-logo" src="assets/suzu-logo.png" alt="">
<div class="end-big" id="{p}-big">{esc(sc.get("big","Plan India with locals"))}</div>
<div class="end-sm" id="{p}-sm">{esc(sc.get("small","Suzu Travels · DMC of India"))}</div>
<div class="cta" id="{p}-cta">{esc(sc.get("cta","DM us or visit suzutravels.com"))}</div>
<div class="contact" id="{p}-c">WhatsApp +91 70874 88961 · suzutravels.com</div></div>''')
            js.append(f'tl.fromTo("#{p}-halo",{{opacity:0,scale:0.5}},{{opacity:1,scale:1,duration:1.2,ease:"power2.out"}},{S+0.1:.3f});')
            js.append(f'tl.fromTo("#{p}-logo",{{scale:0.5,opacity:0,rotate:-12}},{{scale:1,opacity:1,rotate:0,duration:0.9,ease:"back.out(1.6)"}},{S+0.2:.3f});')
            js.append(f'tl.fromTo("#{p}-big",{{opacity:0,y:30}},{{opacity:1,y:0,duration:0.7,ease:"power3.out"}},{S+0.7:.3f});')
            js.append(f'tl.fromTo("#{p}-sm",{{opacity:0}},{{opacity:1,duration:0.6}},{S+1.1:.3f});')
            js.append(f'tl.fromTo("#{p}-cta",{{opacity:0,y:30}},{{opacity:1,y:0,duration:0.6,ease:"back.out(2)"}},{S+1.6:.3f});')
            js.append(f'tl.fromTo("#{p}-c",{{opacity:0}},{{opacity:1,duration:0.6}},{S+2.0:.3f});')
        if sc.get("custom_html"):
            inner.append(sc["custom_html"])
        if sc.get("custom_js"):
            js.append(f'(function(S,D){{{sc["custom_js"]}}})({S},{D});')
        # transition: gold wipe line + fade in
        body.append(f'<section class="clip scene" id="{p}" data-start="{S}" data-duration="{D}" data-track-index="1">{"".join(inner)}<div class="wipe" id="{p}-wipe"></div></section>')
        if si > 0:
            js.append(f'tl.fromTo("#{p}",{{opacity:0}},{{opacity:1,duration:0.3}},{S:.3f});')
            js.append(f'tl.fromTo("#{p}-wipe",{{xPercent:-110}},{{xPercent:110,duration:0.55,ease:"power2.inOut"}},{S-0.1 if S>0.1 else 0:.3f});')

    fonts = """
@font-face{font-family:"Bebas";src:url(assets/fonts/bebas-neue-latin-400-normal.woff2) format("woff2")}
@font-face{font-family:"Inter";font-weight:500;src:url(assets/fonts/inter-latin-500-normal.woff2) format("woff2")}
@font-face{font-family:"Inter";font-weight:700;src:url(assets/fonts/inter-latin-700-normal.woff2) format("woff2")}
@font-face{font-family:"Inter";font-weight:800;src:url(assets/fonts/inter-latin-800-normal.woff2) format("woff2")}
@font-face{font-family:"Playfair";font-style:italic;font-weight:500;src:url(assets/fonts/playfair-display-latin-500-italic.woff2) format("woff2")}
"""
    css = fonts + f"""
body{{margin:0;background:{EM}}}
#root{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:{EM};color:#fff;font-family:"Inter",sans-serif}}
.scene{{position:absolute;inset:0;overflow:hidden}}
.mover{{position:absolute}} .mover .ph{{position:absolute;inset:0;width:100%;height:100%;display:block}}
.embg{{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 30%,#1d3b23 0%,{EM} 60%,#0a160d 100%)}}
.shade{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(7,15,9,.7) 0%,rgba(7,15,9,.15) 28%,rgba(7,15,9,0) 50%,rgba(7,15,9,.35) 68%,rgba(7,15,9,.9) 100%)}}
.kicker{{position:absolute;left:80px;top:1040px;font-family:"Inter";font-weight:700;font-size:34px;letter-spacing:.22em;text-transform:uppercase;color:{GOLD};text-shadow:0 3px 14px rgba(0,0,0,.8)}}
.kicker.top{{top:300px}}
.hl{{position:absolute;left:80px;right:190px;font-family:"Bebas";font-size:150px;line-height:.94;color:#fff;text-shadow:0 6px 30px rgba(0,0,0,.75)}}
.hl .ln{{display:block}} .hl .w{{display:inline-block;overflow:hidden;vertical-align:top;padding:.04em 0}} .hl .wi{{display:inline-block}}
.hl .gold .wi{{color:{GOLD}}}
.hl-low{{top:1100px}} .hl-mid{{top:760px}} .hl-top{{top:360px}}
.sub{{position:absolute;left:80px;right:190px;top:1410px;font-family:"Playfair";font-style:italic;font-size:40px;line-height:1.3;color:rgba(255,255,255,.92);text-shadow:0 3px 14px rgba(0,0,0,.8)}}
.sub-bottom{{top:1380px}}
.stat{{position:absolute;left:80px;top:330px;text-shadow:0 6px 24px rgba(0,0,0,.85)}}
.stat-bottom{{top:auto;bottom:430px;left:80px}}
.stat-n{{font-family:"Bebas";font-size:300px;line-height:.9;color:{GOLD}}}
.stat-l{{font-family:"Inter";font-weight:700;font-size:44px;letter-spacing:.08em;text-transform:uppercase;margin-top:10px;max-width:820px}}
.tag{{position:absolute;right:210px;top:300px;background:{GOLD};color:{EM};font-family:"Inter";font-weight:800;font-size:30px;letter-spacing:.12em;text-transform:uppercase;padding:14px 26px;border-radius:999px}}
.days{{position:absolute;left:80px;top:950px;display:flex;align-items:center;gap:12px}}
.dlab{{font-family:"Inter";font-weight:800;font-size:22px;letter-spacing:.2em;color:rgba(255,255,255,.75);margin-right:6px;text-shadow:0 2px 10px rgba(0,0,0,.8)}}
.dcell{{width:56px;height:56px;border-radius:50%;border:2px solid rgba(255,255,255,.6);background:rgba(7,15,9,.35);display:flex;align-items:center;justify-content:center;font-family:"Inter";font-weight:800;font-size:24px;color:rgba(255,255,255,.8)}}
.dcell.on{{background:{GOLD};border-color:{GOLD};color:{EM};box-shadow:0 0 24px rgba(242,200,75,.55)}}
.map{{position:absolute;inset:0}}
.pinlab{{font-family:"Inter";font-weight:700;font-size:34px;fill:#fff;paint-order:stroke;stroke:{EM};stroke-width:8px;stroke-linejoin:round}}
.rlab{{font-family:"Inter";font-weight:700;font-size:28px;fill:{GOLD}}}
.list{{position:absolute;left:60px;right:170px;top:700px;background:rgba(7,15,9,.5);padding:44px 40px 10px;border-radius:32px;backdrop-filter:blur(6px)}}
.item{{display:flex;gap:30px;align-items:flex-start;margin-bottom:54px}}
.num{{font-family:"Bebas";font-size:96px;line-height:.9;color:{GOLD};min-width:110px}}
.it-a{{font-family:"Inter";font-weight:800;font-size:56px;line-height:1.1}}
.it-b{{font-family:"Inter";font-weight:500;font-size:38px;line-height:1.3;color:rgba(255,255,255,.78);margin-top:8px}}
.end{{position:absolute;inset:0;text-align:center}}
.halo{{position:absolute;left:190px;top:330px;width:700px;height:700px;border-radius:50%;background:radial-gradient(circle,rgba(242,200,75,.35),rgba(242,200,75,0) 70%)}}
.logo{{position:absolute;left:340px;top:430px;width:400px}}
.end-big{{position:absolute;left:80px;right:80px;top:900px;font-family:"Bebas";font-size:150px;line-height:.95}}
.end-sm{{position:absolute;left:80px;right:80px;top:1230px;font-family:"Playfair";font-style:italic;font-size:48px;color:{GOLD}}}
.cta{{position:absolute;left:190px;right:190px;top:1400px;background:{GOLD};color:{EM};font-family:"Inter";font-weight:800;font-size:38px;padding:26px 30px;border-radius:999px;letter-spacing:.04em}}
.contact{{position:absolute;left:80px;right:80px;top:1530px;font-family:"Inter";font-weight:700;font-size:34px;letter-spacing:.06em;color:rgba(255,255,255,.9)}}
.wipe{{position:absolute;top:0;bottom:0;left:0;width:100%;background:linear-gradient(90deg,transparent,{GOLD} 50%,transparent);opacity:.9;mix-blend-mode:screen;pointer-events:none}}
#brand{{position:absolute;left:80px;top:150px;display:flex;align-items:center;gap:16px;font-family:"Inter";font-weight:800;font-size:28px;letter-spacing:.2em;color:{GOLD};text-shadow:0 2px 10px rgba(0,0,0,.7)}}
#brand img{{width:64px;height:64px;object-fit:contain}}
#grain{{position:absolute;inset:0;background:url(assets/grain.png);opacity:.08;mix-blend-mode:overlay;pointer-events:none}}
#prog{{position:absolute;left:0;bottom:0;height:8px;width:100%;background:{GOLD};transform-origin:0 50%}}
""" + "".join(css_extra)
    out = f'''<!doctype html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width={W}, height={H}">
<title>{esc(spec.get("title","Suzu Travels reel"))}</title>
<script src="assets/gsap.min.js"></script>
<style>{css}</style></head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-width="{W}" data-height="{H}" data-duration="{total}">
{"".join(body)}
<div id="brand"><img src="assets/suzu-logo.png" alt="">SUZU TRAVELS</div>
<div id="grain"></div><div id="prog"></div>
</div>
<script>
const tl = gsap.timeline({{ paused: true }});
{chr(10).join(js)}
tl.set(".wipe",{{xPercent:-110}},0);
tl.fromTo("#prog",{{scaleX:0}},{{scaleX:1,duration:{total},ease:"none"}},0);
tl.fromTo("#brand",{{opacity:0,y:-16}},{{opacity:1,y:0,duration:0.6}},0.3);
window.__timelines = window.__timelines || {{}};
window.__timelines["main"] = tl;
</script>
</body></html>'''
    open(os.path.join(out_dir, "index.html"), "w").write(out)
    for f in ("hyperframes.json", "package.json"):
        shutil.copy(os.path.join(HERE, "assets", "hf-template", f), os.path.join(out_dir, f))
    print("built", out_dir, total, "s")


if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2])
