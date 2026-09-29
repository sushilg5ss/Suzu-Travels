#!/usr/bin/env python3
"""Bharat Darshan episode -> HyperFrames project (9:16, 1080x1920, 30fps).

usage: build.py EP_DIR
needs EP_DIR/episode.json (lines + scenes), EP_DIR/voice/voice_meta.json, EP_DIR/voice/captions.json,
images in EP_DIR/img/. Writes EP_DIR/hf/ (index.html + assets) and EP_DIR/timing.json
(absolute line starts, scene starts, SFX cues) for mix.py.

Scene types: hook | title | photo | beat | dial | stamp | end
Shot keys: img, focus[fx,fy], zoom[z0,z1], pan[dx,dy], at (0..1 of scene), grade (warm|dark|mono),
           fit ("cover"|"contain"), width (display width in frame-widths, contain only),
           anchor[ax,ay] px, stat{num,prefix,suffix,label}, dial{cx,cy,r} (fractions of image width/height)
Scene keys: headline[..], headline2[..], kicker, coords, stat, label_en, stamp[3], prop ("note10" + prop_img, prop_caption), cta,
            pack_kicker / pack_title (end card, e.g. "कोणार्क · पुरी · भुवनेश्वर" / "पूरा टूर प्लान"),
            no_captions, custom_html (raw HTML placed in scene), custom_js (JS using tl, S=scene start, D=duration)
"""
import html, json, os, random, re, shutil, sys
from PIL import Image, ImageFilter, ImageEnhance

W, H, FPS = 1080, 1920, 30
HERE = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(HERE, "assets")
GAP_LINE, GAP_SCENE, LEAD = 0.28, 0.42, 0.3
GOLD = "#F2C84B"

esc = lambda s: html.escape(str(s))


def timings(ep, meta):
    dur = {m["id"]: m["dur"] for m in meta}
    t, line_start, scene_t = 0.75, {}, []
    for si, sc in enumerate(ep["scenes"]):
        first = t
        for lid in sc["lines"]:
            line_start[lid] = round(t, 3)
            t += dur[lid] + GAP_LINE
        t += GAP_SCENE - GAP_LINE + sc.get("extra_pause", 0)
        scene_t.append([0.0 if si == 0 else round(first - LEAD, 3), None])
    for i in range(len(scene_t) - 1):
        scene_t[i][1] = scene_t[i + 1][0]
    total = round(t + 2.4, 2)
    scene_t[-1][1] = total
    return line_start, [(a, b) for a, b in scene_t], total, dur


def prep_image(ep_dir, out_dir, name, grade, blur_bg=False):
    src = os.path.join(ep_dir, "img", name)
    im = Image.open(src).convert("RGB")
    base = os.path.splitext(name)[0]
    fn = f"{base}-{grade or 'n'}.jpg"
    if not os.path.exists(os.path.join(out_dir, fn)):
        g = im
        if grade == "mono":
            g = ImageEnhance.Contrast(im.convert("L").convert("RGB")).enhance(1.25)
            g = ImageEnhance.Brightness(g).enhance(0.75)
        elif grade == "dark":
            g = ImageEnhance.Brightness(ImageEnhance.Contrast(im).enhance(1.1)).enhance(0.62)
        else:  # warm cinematic: slight contrast + warmth
            g = ImageEnhance.Contrast(ImageEnhance.Color(im).enhance(1.12)).enhance(1.06)
        g.save(os.path.join(out_dir, fn), quality=90)
    bgfn = None
    if blur_bg:
        bgfn = f"{base}-blur.jpg"
        b = im.copy(); b.thumbnail((720, 720))
        b = ImageEnhance.Brightness(b.filter(ImageFilter.GaussianBlur(28))).enhance(0.45)
        b.save(os.path.join(out_dir, bgfn), quality=85)
    return fn, bgfn, im.size


def headline_html(lines, cls, idp):
    out = []
    for li, line in enumerate(lines):
        words = "".join(f'<span class="w"><span class="wi" id="{idp}-w{li}-{k}">{esc(w)}</span></span> '
                        for k, w in enumerate(line.split()))
        out.append(f'<div class="hl-line">{words}</div>')
    return f'<div class="{cls}" id="{idp}">{"".join(out)}</div>'


def reveal_js(idp, lines, t0, step=0.09):
    js, k = [], 0
    for li, line in enumerate(lines):
        for wi, _ in enumerate(line.split()):
            js.append(f'tl.fromTo("#{idp}-w{li}-{wi}",{{yPercent:115,opacity:0}},{{yPercent:0,opacity:1,duration:0.55,ease:"power4.out"}},{t0 + k*step:.3f});')
            k += 1
    return "\n".join(js)


NOTE10 = '''<div class="note-wrap" id="{p}-note"><div class="note" id="{p}-notecard">
<svg class="note-guil" viewBox="0 0 760 360" preserveAspectRatio="none">{guil}</svg>
<div class="note-10">₹10</div><div class="note-txt">दस रुपये</div>
<div class="note-win"><img src="{img}" alt=""></div>
<div class="note-cap">{cap}</div><div class="note-shine" id="{p}-shine"></div>
</div></div>'''


def guilloche():
    s = []
    for i in range(18):
        s.append(f'<ellipse cx="380" cy="180" rx="{60+i*20}" ry="{30+i*9}" fill="none" stroke="rgba(255,235,200,.10)" stroke-width="1.2"/>')
    for i in range(24):
        s.append(f'<line x1="0" y1="{i*16}" x2="760" y2="{i*16-120}" stroke="rgba(255,235,200,.05)" stroke-width="1"/>')
    return "".join(s)


def build(ep_dir):
    ep = json.load(open(os.path.join(ep_dir, "episode.json")))
    meta = json.load(open(os.path.join(ep_dir, "voice", "voice_meta.json")))
    caps = json.load(open(os.path.join(ep_dir, "voice", "captions.json")))
    line_start, scene_t, total, ldur = timings(ep, meta)
    hf = os.path.join(ep_dir, "hf")
    os.makedirs(os.path.join(hf, "assets", "fonts"), exist_ok=True)
    os.makedirs(os.path.join(hf, "img"), exist_ok=True)
    for f in os.listdir(os.path.join(A, "fonts")):
        shutil.copy(os.path.join(A, "fonts", f), os.path.join(hf, "assets", "fonts", f))
    for f in ("gsap.min.js", "grain.png", "suzu-logo.png"):
        shutil.copy(os.path.join(A, f), os.path.join(hf, "assets", f))

    rnd = random.Random(ep.get("episode", 1))
    scenes_html, js = [], []
    sfx = [{"t": 0.0, "kind": "boom"}]
    for si, sc in enumerate(ep["scenes"]):
        S, E = scene_t[si]
        D = round(E - S, 3)
        p = f"s{si}"
        typ = sc["type"]
        body = []
        # ---------- shots ----------
        shots = sc.get("shots", [])
        for k, sh in enumerate(shots):
            fit = sh.get("fit", "cover")
            fn, bgfn, (iw, ih) = prep_image(ep_dir, os.path.join(hf, "img"), sh["img"], sh.get("grade", "warm"), fit == "contain")
            fx, fy = sh.get("focus", [0.5, 0.5])
            ax, ay = sh.get("anchor", [W / 2, H / 2 - 40])
            if fit == "contain":
                dw = W * sh.get("width", 1.5); s0 = dw / iw
            else:
                s0 = max(W / iw, H / ih) * sh.get("base", 1.0)
            dw, dh = iw * s0, ih * s0
            left, top = ax - fx * dw, ay - fy * dh
            if fit == "cover":
                left = min(0, max(W - dw, left)); top = min(0, max(H - dh, top))
            sid = f"{p}-sh{k}"
            t_in = sh.get("at", 0) * D
            t_out = shots[k + 1].get("at", 1) * D if k + 1 < len(shots) else D
            bg = f'<img class="blurbg" src="img/{bgfn}" alt="">' if bgfn else ""
            overlay = ""
            if "dial" in sh:
                d = sh["dial"]; cx, cy, r = d["cx"] * iw, d["cy"] * ih, d["r"] * iw
                spokes = "".join(
                    f'<line id="{sid}-sp{i}" x1="{cx}" y1="{cy}" x2="{cx + r*0.93*__import__("math").cos(i*0.785398-1.5708):.0f}" y2="{cy + r*0.93*__import__("math").sin(i*0.785398-1.5708):.0f}" stroke="{GOLD}" stroke-width="{iw*0.006:.0f}" stroke-linecap="round" opacity="0"/>'
                    for i in range(8))
                overlay = f'''<svg class="dial" viewBox="0 0 {iw} {ih}" preserveAspectRatio="none">
<defs><linearGradient id="{sid}-shg" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#000" stop-opacity=".0"/><stop offset=".5" stop-color="#F2C84B" stop-opacity=".8"/><stop offset="1" stop-color="#000" stop-opacity="0"/></linearGradient></defs>
<circle id="{sid}-ring" cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{GOLD}" stroke-width="{iw*0.007:.0f}" stroke-dasharray="{6.2832*r:.0f}" stroke-dashoffset="{6.2832*r:.0f}"/>
{spokes}
<g id="{sid}-shadow" style="transform-origin:{cx}px {cy}px"><rect x="{cx - iw*0.004}" y="{cy - r*0.98}" width="{iw*0.008}" height="{r*0.98}" fill="#fff3c4" opacity=".95"/><rect x="{cx - iw*0.02}" y="{cy - r*0.98}" width="{iw*0.04}" height="{r*0.98}" fill="url(#{sid}-shg)" opacity=".55"/></g>
<circle cx="{cx}" cy="{cy}" r="{iw*0.018}" fill="{GOLD}"/></svg>'''
                js.append(f'tl.to("#{sid}-ring",{{strokeDashoffset:0,duration:1.6,ease:"power2.inOut"}},{S+0.4:.3f});')
                for i in range(8):
                    js.append(f'tl.to("#{sid}-sp{i}",{{opacity:1,duration:0.25}},{S+1.2+i*0.18:.3f});')
                    js.append(f'tl.to("#{sid}-sp{i}",{{opacity:0.25,duration:0.6}},{S+1.5+i*0.18:.3f});')
                l2 = sc["lines"][-1]
                js.append(f'tl.fromTo("#{sid}-shadow",{{rotation:-90}},{{rotation:54,duration:{max(2.5, line_start[l2]+ldur[l2]-S-2.8):.2f},ease:"none"}},{S+2.8:.3f});')
            body.append(f'''<div class="shot" id="{sid}">{bg}<div class="mover" id="{sid}-m" style="left:{left:.1f}px;top:{top:.1f}px;width:{dw:.1f}px;height:{dh:.1f}px;transform-origin:{fx*100:.1f}% {fy*100:.1f}%">
<img class="ph{' card' if fit=='contain' else ''}" src="img/{fn}" alt="">{overlay}</div></div>''')
            z0, z1 = sh.get("zoom", [1.12, 1.0])
            px, py = sh.get("pan", [0, 0])
            span = t_out - t_in + (0.6 if k + 1 < len(shots) else 0)
            js.append(f'tl.fromTo("#{sid}-m",{{scale:{z0},x:0,y:0}},{{scale:{z1},x:{px},y:{py},duration:{span:.3f},ease:"sine.inOut"}},{S+t_in:.3f});')
            if k > 0:
                js.append(f'tl.fromTo("#{sid}",{{opacity:0}},{{opacity:1,duration:0.35,ease:"power1.out"}},{S+t_in:.3f});')
                sfx.append({"t": round(S + t_in, 3), "kind": "whoosh"})
            else:
                js.append(f'tl.set("#{sid}",{{opacity:1}},{S:.3f});')
            if "stat" in sh:
                st = sh["stat"]; stid = f"{sid}-stat"
                body.append(f'<div class="stat" id="{stid}" style="opacity:0"><div class="stat-num" id="{stid}-n">{esc(st.get("prefix",""))}0{esc(st.get("suffix",""))}</div><div class="stat-lab">{esc(st["label"])}</div></div>')
                t = S + t_in + 0.25
                js.append(f'tl.fromTo("#{stid}",{{opacity:0,y:40}},{{opacity:1,y:0,duration:0.5,ease:"power3.out"}},{t:.3f});')
                js.append(f'(function(){{var o={{v:0}};tl.to(o,{{v:{st["num"]},duration:0.9,ease:"power2.out",onUpdate:function(){{document.getElementById("{stid}-n").textContent="{st.get("prefix","")}"+Math.round(o.v)+"{st.get("suffix","")}";}}}},{t:.3f});}})();')
                if k + 1 < len(shots):
                    js.append(f'tl.to("#{stid}",{{opacity:0,duration:0.3}},{S+t_out-0.2:.3f});')
                sfx.append({"t": round(t, 3), "kind": "hit"})
        # grade overlays
        body.append('<div class="shade"></div>')
        # ---------- scene furniture ----------
        if typ in ("hook", "beat"):
            if sc.get("prop") == "note10":
                wimg = prep_image(ep_dir, os.path.join(hf, "img"), sc.get("prop_img", "konark-sun-temple-wheel-3.jpg"), "warm")[0]
                body.append(NOTE10.format(p=p, guil=guilloche(), img="img/" + wimg, cap=esc(sc.get("prop_caption", ep.get("place", "")))))
                js.append(f'tl.fromTo("#{p}-notecard",{{y:900,rotation:-28,rotationX:55,opacity:0}},{{y:0,rotation:-6,rotationX:0,opacity:1,duration:1.1,ease:"expo.out"}},{S+0.35:.3f});')
                js.append(f'tl.to("#{p}-notecard",{{rotation:-3,y:-18,duration:{D-1.5:.2f},ease:"sine.inOut"}},{S+1.45:.3f});')
                js.append(f'tl.fromTo("#{p}-shine",{{xPercent:-160}},{{xPercent:260,duration:1.0,ease:"power2.inOut"}},{S+1.6:.3f});')
                sfx.append({"t": round(S + 0.35, 3), "kind": "whoosh"})
            if sc.get("headline"):
                cls = "hl hl-top" if sc.get("prop") else "hl hl-mid"
                body.append(headline_html(sc["headline"], cls, f"{p}-hl"))
                t0 = S + 0.5 if typ == "hook" and si == 0 else line_start[sc["lines"][0]] + 0.1
                if sc.get("prop") and si != 0:
                    t0 = line_start[sc["lines"][-1]] + ldur[sc["lines"][-1]] * 0.55
                js.append(reveal_js(f"{p}-hl", sc["headline"], t0))
            if sc.get("headline2"):
                body.append(headline_html(sc["headline2"], "hl hl-low", f"{p}-hl2"))
                l2 = sc["lines"][1] if len(sc["lines"]) > 1 else sc["lines"][0]
                js.append(reveal_js(f"{p}-hl2", sc["headline2"], line_start[l2] + ldur[l2] * 0.4))
            if typ == "beat":
                sfx.append({"t": round(S, 3), "kind": "riser"})
        if typ == "title":
            body.append(f'<div class="title-block" id="{p}-tb"><div class="kicker" id="{p}-k"><span class="pin">◉</span>{esc(sc.get("kicker",""))}</div>'
                        + headline_html(sc["headline"], "hl hl-title", f"{p}-hl")
                        + f'<div class="coords" id="{p}-c">{esc(sc.get("coords",""))}</div></div>')
            js.append(f'tl.fromTo("#{p}-k",{{opacity:0,x:-40}},{{opacity:1,x:0,duration:0.6,ease:"power3.out"}},{S+0.35:.3f});')
            js.append(reveal_js(f"{p}-hl", sc["headline"], S + 0.45, 0.14))
            js.append(f'tl.fromTo("#{p}-c",{{opacity:0,scaleX:1.35}},{{opacity:1,scaleX:1,duration:1.2,ease:"power2.out"}},{S+1.0:.3f});')
            sfx.append({"t": round(S + 0.4, 3), "kind": "hit"})
        if "stat" in sc:
            st = sc["stat"]; stid = f"{p}-stat"
            body.append(f'<div class="stat" id="{stid}" style="opacity:0"><div class="stat-num" id="{stid}-n">{esc(st.get("prefix",""))}0{esc(st.get("suffix",""))}</div><div class="stat-lab">{esc(st["label"])}</div></div>')
            t = S + 0.5
            js.append(f'tl.fromTo("#{stid}",{{opacity:0,y:40}},{{opacity:1,y:0,duration:0.6,ease:"power3.out"}},{t:.3f});')
            js.append(f'(function(){{var o={{v:{int(st["num"]*0.8)}}};tl.to(o,{{v:{st["num"]},duration:1.4,ease:"power2.out",onUpdate:function(){{document.getElementById("{stid}-n").textContent="{st.get("prefix","")}"+Math.round(o.v)+"{st.get("suffix","")}";}}}},{t:.3f});}})();')
            sfx.append({"t": round(t, 3), "kind": "hit"})
        if "label_en" in sc:
            body.append(f'<div class="label-en" id="{p}-le">{esc(sc["label_en"])}</div>')
            js.append(f'tl.fromTo("#{p}-le",{{opacity:0,scaleX:1.6,scaleY:1.05}},{{opacity:1,scaleX:1,scaleY:1,duration:1.6,ease:"power3.out"}},{line_start[sc["lines"][0]]+ldur[sc["lines"][0]]*0.55:.3f});')
            sfx.append({"t": round(line_start[sc["lines"][0]] + ldur[sc["lines"][0]] * 0.55, 3), "kind": "hit"})
        if typ == "dial":
            c0, c1 = sc.get("clock", ["06:00", "09:36"])
            m0 = int(c0[:2]) * 60 + int(c0[3:]); m1 = int(c1[:2]) * 60 + int(c1[3:])
            body.append(f'<div class="dial-head" id="{p}-dh"><div class="kicker">{esc(sc.get("kicker",""))}</div><div class="clock" id="{p}-clk">{c0}</div></div>')
            js.append(f'tl.fromTo("#{p}-dh",{{opacity:0,y:-30}},{{opacity:1,y:0,duration:0.7,ease:"power3.out"}},{S+0.3:.3f});')
            l2 = sc["lines"][-1]
            dd = max(2.5, line_start[l2] + ldur[l2] - S - 2.8)
            js.append(f'(function(){{var o={{v:{m0}}};tl.to(o,{{v:{m1},duration:{dd:.2f},ease:"none",onUpdate:function(){{var v=Math.round(o.v),h=Math.floor(v/60),m=v%60;document.getElementById("{p}-clk").textContent=(h<10?"0":"")+h+":"+(m<10?"0":"")+m;}}}},{S+2.8:.3f});}})();')
            sfx.append({"t": round(S + 2.8, 3), "kind": "ticks", "dur": round(dd, 2)})
        if typ == "stamp":
            a, b, c = sc["stamp"]
            body.append(f'<div class="stamp" id="{p}-st"><div class="stamp-in"><div class="st-a">{esc(a)}</div><div class="st-b">{esc(b)}</div><div class="st-c">{esc(c)}</div></div></div>')
            t = line_start[sc["lines"][0]] + ldur[sc["lines"][0]] * 0.45
            js.append(f'tl.fromTo("#{p}-st",{{scale:2.6,rotation:-24,opacity:0}},{{scale:1,rotation:-10,opacity:1,duration:0.32,ease:"expo.in"}},{t:.3f});')
            js.append(f'tl.fromTo("#{p}",{{x:0}},{{keyframes:[{{x:-14,duration:0.04}},{{x:12,duration:0.04}},{{x:-8,duration:0.04}},{{x:5,duration:0.04}},{{x:0,duration:0.05}}]}},{t+0.32:.3f});')
            sfx.append({"t": round(t + 0.3, 3), "kind": "stamp"})
        if typ == "end":
            l1, l2 = sc["lines"][0], sc["lines"][-1]
            body.append(f'''<div class="end" id="{p}-end">
<div class="end-halo" id="{p}-halo"></div><img class="end-logo" id="{p}-logo" src="assets/suzu-logo.png" alt="">
<div class="end-pack" id="{p}-pack"><div class="kicker">{esc(sc.get("pack_kicker", ep.get("place","")))}</div><div class="end-pack-t">{esc(sc.get("pack_title","पूरा टूर प्लान"))}</div></div>
<div class="end-series" id="{p}-series"><div class="end-sm">जुड़े रहिए</div><div class="end-big">भारत दर्शन</div><div class="end-sm">के साथ</div></div>
<div class="cta" id="{p}-cta">{esc(sc.get("cta","कमेंट करें: अगला एपिसोड कहाँ?"))}</div>
<div class="brand" id="{p}-brand"><div class="brand-n">SUZU TRAVELS</div><div class="brand-s">DMC OF INDIA · +91 70874 88961 · suzutravels.com</div></div></div>''')
            js.append(f'tl.fromTo("#{p}-halo",{{opacity:0,scale:0.6}},{{opacity:1,scale:1,duration:1.2,ease:"power2.out"}},{S+0.2:.3f});')
            js.append(f'tl.fromTo("#{p}-logo",{{scale:0.4,opacity:0,rotation:-20}},{{scale:1,opacity:1,rotation:0,duration:0.9,ease:"back.out(1.6)"}},{S+0.3:.3f});')
            js.append(f'tl.fromTo("#{p}-pack",{{opacity:0,y:30}},{{opacity:1,y:0,duration:0.6}},{S+0.6:.3f});')
            js.append(f'tl.to("#{p}-pack",{{opacity:0,y:-20,duration:0.4}},{line_start[l2]-0.3:.3f});')
            js.append(f'tl.fromTo("#{p}-series",{{opacity:0,scale:0.9}},{{opacity:1,scale:1,duration:0.8,ease:"power3.out"}},{line_start[l2]-0.1:.3f});')
            js.append(f'tl.fromTo("#{p}-cta",{{opacity:0,y:30}},{{opacity:1,y:0,duration:0.6,ease:"back.out(2)"}},{line_start[l2]+ldur[l2]:.3f});')
            js.append(f'tl.fromTo("#{p}-brand",{{opacity:0}},{{opacity:1,duration:0.8}},{S+0.9:.3f});')
            sfx.append({"t": round(S + 0.3, 3), "kind": "hit"})
        if sc.get("custom_html"):
            body.append(sc["custom_html"])
        if sc.get("custom_js"):
            js.append(f"(function(S,D){{{sc['custom_js']}}})({S},{D});")
        scenes_html.append(f'<section class="clip scene" id="{p}" data-start="{S}" data-duration="{D}" data-track-index="1">{"".join(body)}</section>')
        if si > 0:
            js.append(f'tl.fromTo("#leak",{{x:-1500,opacity:0}},{{immediateRender:false,keyframes:[{{x:-300,opacity:0.95,duration:0.3}},{{x:1500,opacity:0,duration:0.5}}],ease:"none"}},{S-0.3:.3f});')
            sfx.append({"t": round(S - 0.2, 3), "kind": "whoosh"})

    # ---------- captions ----------
    cap_html, no_cap = [], {l for sc in ep["scenes"] if sc.get("no_captions", sc["type"] in ("end", "title")) for l in sc["lines"]}
    allchunks = []
    ci = 0
    for ln in ep["lines"]:
        if ln["id"] in no_cap:
            continue
        words = caps[ln["id"]]
        chunks, cur = [], []
        for w in words:
            cur.append(w)
            if len(cur) >= 3 or re.search(r"[,।.…?!]$", w["w"]):
                chunks.append(cur); cur = []
        if cur:
            chunks.append(cur)
        base = line_start[ln["id"]]
        for ch in chunks:
            allchunks.append((base, ch))
    for idx, (base, ch) in enumerate(allchunks):
            cid = f"c{ci}"; ci += 1
            spans = "".join(f'<span class="cw" id="{cid}-{k}">{esc(w["w"])}</span> ' for k, w in enumerate(ch))
            cap_html.append(f'<div class="cap" id="{cid}" style="opacity:0">{spans}</div>')
            t0, t1 = base + ch[0]["s"] - 0.05, base + ch[-1]["e"] + 0.12
            if idx + 1 < len(allchunks):
                nb, nch = allchunks[idx + 1]
                t1 = min(t1, nb + nch[0]["s"] - 0.07)
            t1 = max(t1, t0 + 0.2)
            js.append(f'tl.fromTo("#{cid}",{{opacity:0,y:18,scale:0.96}},{{opacity:1,y:0,scale:1,duration:0.12,ease:"power2.out",immediateRender:false}},{t0:.3f});')
            js.append(f'tl.to("#{cid}",{{opacity:0,duration:0.06}},{t1:.3f});')
            for k, w in enumerate(ch):
                js.append(f'tl.to("#{cid}-{k}",{{color:"{GOLD}",scale:1.1,duration:0.08}},{base+w["s"]:.3f});')
                js.append(f'tl.to("#{cid}-{k}",{{color:"#ffffff",scale:1,duration:0.1}},{base+w["e"]:.3f});')

    # ---------- global: grain, dust ----------
    g = random.Random(11)
    n = int(total * 12)
    for i in range(n):
        js.append(f'tl.set("#grain",{{backgroundPosition:"{g.randint(0,255)}px {g.randint(0,255)}px"}},{i/12:.3f});')
    dust = []
    for i in range(34):
        x, y, s = rnd.uniform(0, W), rnd.uniform(200, H), rnd.uniform(3, 8)
        dust.append(f'<div class="dust" id="d{i}" style="left:{x:.0f}px;top:{y:.0f}px;width:{s:.1f}px;height:{s:.1f}px"></div>')
        js.append(f'tl.fromTo("#d{i}",{{y:0,x:0,opacity:0}},{{y:{-rnd.uniform(250,700):.0f},x:{rnd.uniform(-80,80):.0f},opacity:{rnd.uniform(0.35,0.8):.2f},duration:{total:.2f},ease:"none"}},0);')
    js.insert(0, 'tl.set("#leak",{x:-1500,opacity:0},0);')
    js.append(f'tl.fromTo("#prog",{{scaleX:0}},{{scaleX:1,duration:{total:.2f},ease:"none"}},0);')
    js.append('tl.fromTo("#badge",{opacity:0,y:-20},{opacity:1,y:0,duration:0.6,ease:"power3.out"},0.2);')
    js.append(f'tl.to("#badge",{{opacity:0,duration:0.4}},{scene_t[-1][0]:.3f});')
    js.append(f'tl.fromTo("#flash",{{opacity:0.9}},{{opacity:0,duration:0.5,ease:"power2.out"}},0);')

    ep_no = ep.get("episode", "")
    doc = f'''<!doctype html>
<html lang="hi"><head><meta charset="UTF-8"><meta name="viewport" content="width={W}, height={H}">
<title>Bharat Darshan — {esc(ep.get("place_en",""))}</title>
<script src="assets/gsap.min.js"></script>
<style>
@font-face{{font-family:"Tiro";src:url(assets/fonts/tiro-devanagari-hindi-devanagari-400-normal.woff2) format("woff2");unicode-range:U+0900-097F,U+1CD0-1CF9,U+200C-200D,U+20A8,U+20B9,U+25CC,U+A830-A839,U+A8E0-A8FF;}}
@font-face{{font-family:"Tiro";src:url(assets/fonts/tiro-devanagari-hindi-latin-400-normal.woff2) format("woff2");unicode-range:U+0000-00FF,U+2000-206F,U+20AC,U+2122;}}
@font-face{{font-family:"Baloo";font-weight:600;src:url(assets/fonts/baloo-2-devanagari-600-normal.woff2) format("woff2");unicode-range:U+0900-097F,U+200C-200D,U+20B9,U+25CC,U+A8E0-A8FF;}}
@font-face{{font-family:"Baloo";font-weight:800;src:url(assets/fonts/baloo-2-devanagari-800-normal.woff2) format("woff2");unicode-range:U+0900-097F,U+200C-200D,U+20B9,U+25CC,U+A8E0-A8FF;}}
@font-face{{font-family:"Baloo";font-weight:600;src:url(assets/fonts/baloo-2-latin-600-normal.woff2) format("woff2");unicode-range:U+0000-00FF,U+2000-206F;}}
@font-face{{font-family:"Baloo";font-weight:800;src:url(assets/fonts/baloo-2-latin-800-normal.woff2) format("woff2");unicode-range:U+0000-00FF,U+2000-206F;}}
@font-face{{font-family:"Cinzel";font-weight:700;src:url(assets/fonts/cinzel-latin-700-normal.woff2) format("woff2");}}
@font-face{{font-family:"Cinzel";font-weight:900;src:url(assets/fonts/cinzel-latin-900-normal.woff2) format("woff2");}}
@font-face{{font-family:"Sora";font-weight:700;src:url(assets/fonts/sora-latin-700-normal.woff2) format("woff2");}}
body{{margin:0;background:#07090c;}}
#root{{position:relative;width:100%;height:100%;overflow:hidden;background:#07090c;font-family:"Baloo",sans-serif;color:#fff}}
.scene{{position:absolute;inset:0;overflow:hidden}}
.shot{{position:absolute;inset:0;overflow:hidden;opacity:0}}
.blurbg{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}
.mover{{position:absolute}}
.mover .ph{{position:absolute;inset:0;width:100%;height:100%;display:block}}
.mover .ph.card{{border-radius:28px;box-shadow:0 40px 90px rgba(0,0,0,.65),0 0 0 3px rgba(242,200,75,.35)}}
.dial{{position:absolute;inset:0;width:100%;height:100%}}
.shade{{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 45%,transparent 50%,rgba(0,0,0,.45) 100%),linear-gradient(180deg,rgba(0,0,0,.62) 0%,rgba(0,0,0,.08) 26%,rgba(0,0,0,0) 50%,rgba(0,0,0,.25) 64%,rgba(0,0,0,.78) 100%)}}
.hl{{position:absolute;left:70px;right:190px;font-family:"Tiro",serif;line-height:1.34;filter:drop-shadow(0 4px 10px rgba(0,0,0,.9)) drop-shadow(0 0 30px rgba(0,0,0,.6))}}
.hl-line{{display:block;overflow:hidden;padding:.18em 0 .08em}}
.w{{display:inline-block}} .wi{{display:inline-block;background:linear-gradient(180deg,#fffdf2 0%,#ffe9a8 45%,#F2C84B 80%,#e0a53a 100%);-webkit-background-clip:text;background-clip:text;color:transparent}}
.hl-top{{top:350px;font-size:104px}}
.hl-mid{{top:700px;font-size:120px;text-align:center;left:60px;right:60px}}
.hl-low{{top:1310px;font-size:84px}}
.hl-title{{position:relative;left:0;right:0;font-size:150px;line-height:1.28}}
.title-block{{position:absolute;left:70px;right:180px;top:1020px}}
.kicker{{font-family:"Baloo";font-weight:600;font-size:42px;letter-spacing:.06em;color:#F2C84B;text-shadow:0 3px 14px rgba(0,0,0,.8)}}
.pin{{margin-right:14px;font-size:34px}}
.coords{{transform-origin:0 50%;font-family:"Sora";font-weight:700;font-size:30px;letter-spacing:.18em;color:rgba(255,255,255,.85);margin-top:6px}}
.stat{{position:absolute;left:70px;top:360px;filter:drop-shadow(0 4px 8px rgba(0,0,0,.95)) drop-shadow(0 0 26px rgba(0,0,0,.65))}}
.stat-num{{font-family:"Cinzel";font-weight:900;font-size:210px;line-height:1;background:linear-gradient(180deg,#fffdf2,#ffe39a 50%,#F2C84B);-webkit-background-clip:text;background-clip:text;color:transparent}}

.stat-lab{{font-family:"Baloo";font-weight:800;font-size:66px;margin-top:4px}}
.label-en{{position:absolute;left:0;right:0;top:420px;text-align:center;letter-spacing:.14em;font-family:"Cinzel";font-weight:900;font-size:58px;color:#fff;text-shadow:0 0 40px rgba(0,0,0,.9)}}
.dial-head{{position:absolute;left:0;right:0;top:250px;text-align:center}}
.clock{{font-family:"Cinzel";font-weight:900;font-size:104px;line-height:1.05;color:#fff;text-shadow:0 0 30px rgba(242,200,75,.6)}}
.stamp{{position:absolute;left:250px;top:560px;width:580px;height:580px;border-radius:50%;border:12px double #F2C84B;background:radial-gradient(circle,rgba(20,14,4,.72),rgba(20,14,4,.55));display:flex;align-items:center;justify-content:center;box-shadow:0 0 60px rgba(242,200,75,.45)}}
.stamp-in{{text-align:center}}
.st-a{{font-family:"Cinzel";font-weight:900;font-size:78px;letter-spacing:.12em;color:#F2C84B}}
.st-b{{font-family:"Tiro";font-size:72px;line-height:1.35}}
.st-c{{font-family:"Cinzel";font-weight:900;font-size:108px;color:#F2C84B;line-height:1}}
.note-wrap{{position:absolute;left:0;right:0;top:760px;height:420px;display:flex;justify-content:center;perspective:1400px}}
.note{{position:relative;width:760px;height:360px;border-radius:22px;overflow:hidden;background:linear-gradient(135deg,#5a3424,#8c5a3c 45%,#6d412b);box-shadow:0 50px 90px rgba(0,0,0,.7),inset 0 0 0 6px rgba(255,220,170,.18)}}
.note-guil{{position:absolute;inset:0;width:100%;height:100%}}
.note-10{{position:absolute;left:34px;top:30px;font-family:"Cinzel";font-weight:900;font-size:120px;color:#ffe7c2;line-height:1}}
.note-txt{{position:absolute;left:40px;top:170px;font-family:"Tiro";font-size:44px;color:#ffe7c2}}
.note-win{{position:absolute;right:40px;top:30px;width:300px;height:300px;border-radius:50%;overflow:hidden;box-shadow:0 0 0 8px rgba(242,200,75,.75),0 0 40px rgba(242,200,75,.5)}}
.note-win img{{width:100%;height:100%;object-fit:cover;object-position:50% 42%}}
.note-cap{{position:absolute;left:40px;bottom:36px;font-family:"Baloo";font-weight:600;font-size:32px;color:rgba(255,231,194,.85)}}
.note-shine{{position:absolute;top:-40%;left:0;width:34%;height:180%;background:linear-gradient(90deg,transparent,rgba(255,255,255,.45),transparent);transform:rotate(18deg)}}
.cap{{position:absolute;left:60px;width:840px;bottom:440px;text-align:center;font-family:"Baloo";font-weight:800;font-size:66px;line-height:1.32;color:#fff;-webkit-text-stroke:10px rgba(0,0,0,.85);paint-order:stroke fill;text-shadow:0 6px 18px rgba(0,0,0,.6)}}
.cw{{display:inline-block;margin:0 6px}}
.end{{position:absolute;inset:0}}
.end-logo{{position:absolute;left:330px;top:270px;width:420px;height:420px;filter:drop-shadow(0 16px 30px rgba(0,0,0,.75))}}
.end-halo{{position:absolute;left:190px;top:130px;width:700px;height:700px;border-radius:50%;background:radial-gradient(circle,rgba(255,236,190,.34),rgba(255,236,190,0) 62%)}}
.end-pack{{position:absolute;left:0;right:0;top:740px;text-align:center}}
.end-pack-t{{font-family:"Tiro";font-size:96px;line-height:1.35;color:#fff}}
.end-series{{position:absolute;left:0;right:0;top:720px;text-align:center}}
.end-sm{{font-family:"Baloo";font-weight:600;font-size:52px;color:#fff}}
.end-big{{font-family:"Tiro";font-size:150px;line-height:1.3;background:linear-gradient(180deg,#fff6d8,#F2C84B 55%,#b67f22);-webkit-background-clip:text;background-clip:text;color:transparent}}
.cta{{position:absolute;left:120px;right:120px;top:1150px;text-align:center;padding:18px 20px;border-radius:60px;background:#F2C84B;color:#1b1406;font-family:"Baloo";font-weight:800;font-size:46px;box-shadow:0 10px 30px rgba(0,0,0,.5)}}
.brand{{position:absolute;left:0;right:0;top:1300px;text-align:center}}
.brand-n{{font-family:"Cinzel";font-weight:900;font-size:58px;letter-spacing:.14em;color:#F2C84B}}
.brand-s{{font-family:"Sora";font-weight:700;font-size:26px;letter-spacing:.06em;color:rgba(255,255,255,.9);margin-top:6px}}
#badge{{position:absolute;left:60px;top:250px;display:flex;align-items:center;gap:14px;padding:10px 22px 8px;border-radius:40px;background:rgba(10,8,4,.55);border:2px solid rgba(242,200,75,.7);font-family:"Baloo";font-weight:800;font-size:34px;color:#F2C84B}}
#badge .ep{{font-family:"Baloo";font-weight:600;font-size:30px;color:#fff}}
#prog{{position:absolute;left:0;top:0;width:100%;height:8px;background:#F2C84B;transform-origin:0 50%}}
#grain{{position:absolute;inset:0;background:url(assets/grain.png);opacity:.075;mix-blend-mode:overlay;pointer-events:none}}
#vig{{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 50%,transparent 68%,rgba(0,0,0,.32) 100%);pointer-events:none}}
#leak{{position:absolute;top:160px;left:-200px;width:1500px;height:1500px;border-radius:50%;background:radial-gradient(circle,rgba(255,214,140,.95) 0%,rgba(255,150,50,.55) 30%,rgba(255,110,20,0) 68%);mix-blend-mode:screen;opacity:0;pointer-events:none}}
#flash{{position:absolute;inset:0;background:#fff;opacity:0;pointer-events:none}}
.dust{{position:absolute;border-radius:50%;background:#ffe6a8;box-shadow:0 0 12px 3px rgba(255,210,120,.6);opacity:0}}
</style></head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-width="{W}" data-height="{H}" data-duration="{total}">
{"".join(scenes_html)}
<div id="vig"></div>
{"".join(dust)}
<div id="leak"></div>
<div id="grain"></div>
{"".join(cap_html)}
<div id="badge">भारत दर्शन <span class="ep">· {esc(ep.get("state_badge",""))}</span></div>
<div id="prog"></div>
<div id="flash"></div>
</div>
<script>
const tl = gsap.timeline({{ paused: true }});
{chr(10).join(js)}
window.__timelines["main"] = tl;
</script>
</body></html>'''
    open(os.path.join(hf, "index.html"), "w").write(doc)
    for f in ("hyperframes.json", "package.json"):
        shutil.copy(os.path.join(A, "hf-template", f), os.path.join(hf, f))
    json.dump({"id": ep.get("slug", "episode"), "name": ep.get("slug", "episode")}, open(os.path.join(hf, "meta.json"), "w"))
    json.dump({"total": total, "lines": line_start, "scenes": scene_t, "sfx": sorted(sfx, key=lambda x: x["t"])},
              open(os.path.join(ep_dir, "timing.json"), "w"), indent=1)
    print("built", os.path.join(hf, "index.html"), "duration", total, "s")


if __name__ == "__main__":
    build(sys.argv[1])
