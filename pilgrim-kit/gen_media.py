#!/usr/bin/env python3
"""Suzu Pilgrim Kit — HyperFrames composition generator (original illustrated motion graphics, no photos).

    python3 gen_media.py pilgrim-hero                 hub hero: 4 temple scenes (Himalaya / sea shikhara / ghats / Devi hill)
    python3 gen_media.py light-map                    explainer: the 12 Jyotirlingas light up at their true positions
    python3 gen_media.py temple-hero <slug>           per-page hero  <- src/media/<slug>.json "hero"
    python3 gen_media.py story-strip <slug>           per-page explainer <- src/media/<slug>.json "story" (legend in 4 beats)
    python3 gen_media.py route-map <slug>             per-page explainer <- src/media/<slug>.json "route" (stops by lat/lon)

Why illustrated: every visual is drawn here from SVG shapes, so there is no photo licence to worry about (Sushil, 8 Oct
2026: "copyright claim na ho"). Temple drawings are stylised ARCHETYPES (himalaya, nagara, ghats, gopuram, cave, devi,
pillar, gurudwara, pagoda) — never captioned as an exact architectural likeness.

Rules (same as the mountain kit): 1920x1080, 30 fps, silent, seamless loop (last frame == first frame), deterministic
(no Math.random at runtime — every random number is generated here with a fixed seed). Hero text stays in the RIGHT 55%
of the frame; the LEFT 45% carries the temple art (on phones the page crops the hero to the left, object-position 15%).
Writes $PK_HF_OUT/<name>/index.html + assets/. Render + encode with make_media.sh.
"""
import html as _html, json, math, os, random, shutil, sys, pathlib

KIT = pathlib.Path(__file__).resolve().parent
HF = KIT / "hf"
DATA = KIT / "data"
OUT_ROOT = pathlib.Path(os.environ.get("PK_HF_OUT", str(KIT.parent.parent / "pk-hf")))
W, H = 1920, 1080
GSAP = "https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"

GOLD, GOLD2, SAFF, MAR, INK = "#f2c14e", "#ffd98a", "#ff8a2a", "#5a0f1e", "#140a1c"

FONTS = """
@font-face{font-family:"SZ";src:url("assets/pjs-800.woff2") format("woff2");font-weight:800}
@font-face{font-family:"SZ";src:url("assets/pjs-700.woff2") format("woff2");font-weight:700}
@font-face{font-family:"SZ";src:url("assets/pjs-500.woff2") format("woff2");font-weight:500}
@font-face{font-family:"CG";src:url("assets/cg-700.woff2") format("woff2");font-weight:700}
@font-face{font-family:"CG";src:url("assets/cg-600.woff2") format("woff2");font-weight:600}
@font-face{font-family:"TD";src:url("assets/tiro-deva.woff2") format("woff2");font-weight:400}
*{margin:0;padding:0;box-sizing:border-box}
html,body{margin:0;width:1920px;height:1080px;overflow:hidden;background:#140a1c}
#root{position:relative;width:100%;height:100%;overflow:hidden;font-family:"SZ",sans-serif}
.lay{position:absolute;inset:0}
.kick{font:800 25px "SZ",sans-serif;letter-spacing:.32em;color:#f2c14e;text-transform:uppercase}
.deva{font-family:"TD",serif;line-height:1.15;background:linear-gradient(180deg,#fff3c4 0%,#f2c14e 55%,#e0892a 100%);-webkit-background-clip:text;background-clip:text;color:transparent;filter:drop-shadow(0 6px 26px rgba(255,150,40,.35))}
.en{font-family:"CG",serif;font-weight:700;color:#fff7e6;text-shadow:0 6px 30px rgba(0,0,0,.5)}
"""

SKIES = {  # top, mid, horizon glow
    "dusk": ("#0d0826", "#3b1240", "#ff8a3d"),
    "dawn": ("#14113a", "#5b2a5e", "#ffb46a"),
    "night": ("#05060f", "#151338", "#7a3b8a"),
    "saffron": ("#2a0a1e", "#7a1f2b", "#ffa040"),
    "snow": ("#0b1430", "#2c3f72", "#ffc98a"),
}


def esc(s):
    return _html.escape(str(s), quote=True)


def prep(name):
    d = OUT_ROOT / name
    (d / "assets").mkdir(parents=True, exist_ok=True)
    for f in (HF / "assets").glob("*.woff2"):
        shutil.copy(f, d / "assets" / f.name)
    shutil.copy(HF / "hyperframes.json", d / "hyperframes.json")
    (d / "meta.json").write_text(json.dumps({"id": name, "name": name}))
    return d


# ------------------------------------------------------------------------------------------------ shared layers
def sky_svg(uid, sky="dusk", sun=(470, 610, 150)):
    t, m, g = SKIES[sky]
    cx, cy, r = sun
    return (f'<svg class="lay" viewBox="0 0 {W} {H}" preserveAspectRatio="none"><defs>'
            f'<linearGradient id="sk{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{t}"/><stop offset=".55" stop-color="{m}"/><stop offset="1" stop-color="{g}"/></linearGradient>'
            f'<radialGradient id="sn{uid}"><stop offset="0" stop-color="#fff2c8"/><stop offset=".35" stop-color="#ffcf73" stop-opacity=".95"/><stop offset="1" stop-color="#ff8a3d" stop-opacity="0"/></radialGradient></defs>'
            f'<rect width="{W}" height="{H}" fill="url(#sk{uid})"/><circle cx="{cx}" cy="{cy}" r="{r * 2.6:.0f}" fill="url(#sn{uid})" opacity=".55"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r * .62:.0f}" fill="#ffe7a8" opacity=".9"/></svg>')


def stars(uid, n=90, seed=3, ymax=640):
    r = random.Random(seed)
    c = "".join(f'<circle cx="{r.uniform(0, W):.0f}" cy="{r.uniform(0, ymax):.0f}" r="{r.uniform(.8, 2.2):.1f}" fill="#fff" opacity="{r.uniform(.25, .8):.2f}"/>' for _ in range(n))
    return f'<svg class="lay" viewBox="0 0 {W} {H}">{c}</svg>'


def mandala(cx, cy, R, uid, petals=12, op=.22):
    """12-fold mandala: a rotation by 360/petals degrees maps it onto itself => seamless rotation loop."""
    parts = []
    for k in range(petals):
        a = 360 / petals * k
        parts.append(f'<g transform="rotate({a} {cx} {cy})"><path d="M{cx} {cy - R} C{cx + R * .16} {cy - R * .72} {cx + R * .16} {cy - R * .5} {cx} {cy - R * .34} C{cx - R * .16} {cy - R * .5} {cx - R * .16} {cy - R * .72} {cx} {cy - R}Z" fill="none" stroke="{GOLD}" stroke-width="2.2"/>'
                     f'<circle cx="{cx}" cy="{cy - R * 1.06:.0f}" r="{R * .028:.1f}" fill="{GOLD}"/></g>')
    rings = "".join(f'<circle cx="{cx}" cy="{cy}" r="{R * f:.0f}" fill="none" stroke="{GOLD}" stroke-width="{w}" stroke-dasharray="{d}"/>' for f, w, d in [(1.14, 1.4, "2 10"), (.86, 1.6, "none"), (.3, 1.6, "4 6")])
    return f'<svg id="{uid}" class="lay" viewBox="0 0 {W} {H}" style="opacity:{op};transform-origin:{cx}px {cy}px">{rings}{"".join(parts)}</svg>'


def embers(seed=11):
    """Rising embers / diya sparks: two periodic layers translated up by 1 and 2 tiles per loop => seamless."""
    r = random.Random(seed)
    def pat(pid, n, rmin, rmax):
        c = "".join(f'<circle cx="{r.uniform(0, W):.0f}" cy="{r.uniform(0, H):.0f}" r="{r.uniform(rmin, rmax):.1f}" fill="url(#eg)" opacity="{r.uniform(.35, .95):.2f}"/>' for _ in range(n))
        return f'<pattern id="{pid}" width="{W}" height="{H}" patternUnits="userSpaceOnUse">{c}</pattern>'
    g = '<radialGradient id="eg"><stop offset="0" stop-color="#fff1b8"/><stop offset=".4" stop-color="#ffb347"/><stop offset="1" stop-color="#ff7a1a" stop-opacity="0"/></radialGradient>'
    far = f'<svg class="emb" id="embfar" width="{W}" height="{2 * H}" style="position:absolute;left:0;top:0"><defs>{g}{pat("ef", 34, 2, 4.5)}</defs><rect width="{W}" height="{2 * H}" fill="url(#ef)"/></svg>'
    near = f'<svg class="emb" id="embnear" width="{W}" height="{3 * H}" style="position:absolute;left:0;top:0"><defs>{pat("en", 14, 4.5, 8)}</defs><rect width="{W}" height="{3 * H}" fill="url(#en)"/></svg>'
    return far + near


def embers_js(dur):
    return (f'tl.fromTo("#embfar",{{y:0}},{{y:{-H},duration:{dur},ease:"none"}},0);'
            f'tl.fromTo("#embnear",{{y:0}},{{y:{-2 * H},duration:{dur},ease:"none"}},0);')


# ------------------------------------------------------------------------------------------------ temple archetypes
# Every archetype draws inside a 900x1080 box (x 0..900) — the left 45% of the frame. Silhouette + gold rim + glowing door.
SIL, RIM = "#1b0c1f", "rgba(242,193,78,.55)"


def flag(x, y, h=90, fid="f"):
    return (f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y - h}" stroke="{GOLD}" stroke-width="3"/>'
            f'<path id="{fid}" d="M{x} {y - h} L{x + 62} {y - h + 16} L{x} {y - h + 34}Z" fill="{SAFF}" style="transform-origin:{x}px {y - h + 17}px"/>')


def kalash(x, y, s=1.0):
    return (f'<ellipse cx="{x}" cy="{y}" rx="{16 * s:.0f}" ry="{12 * s:.0f}" fill="{GOLD}"/><rect x="{x - 5 * s:.0f}" y="{y - 30 * s:.0f}" width="{10 * s:.0f}" height="{22 * s:.0f}" fill="{GOLD}"/>'
            f'<circle cx="{x}" cy="{y - 34 * s:.0f}" r="{7 * s:.0f}" fill="{GOLD2}"/>')


def door(x, y, w, h):
    return (f'<path d="M{x - w / 2} {y} L{x - w / 2} {y - h * .62} Q{x} {y - h * 1.1} {x + w / 2} {y - h * .62} L{x + w / 2} {y}Z" fill="#ffb347"/>'
            f'<path d="M{x - w / 2} {y} L{x - w / 2} {y - h * .62} Q{x} {y - h * 1.1} {x + w / 2} {y - h * .62} L{x + w / 2} {y}Z" fill="url(#dg)" opacity=".9"/>')


DEFS = ('<defs><radialGradient id="dg" cx=".5" cy=".75" r=".8"><stop offset="0" stop-color="#fff6d0"/><stop offset=".5" stop-color="#ffb347"/><stop offset="1" stop-color="#c2410c"/></radialGradient>'
        '<linearGradient id="rv" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ff9a4a" stop-opacity=".55"/><stop offset="1" stop-color="#1b0c1f" stop-opacity=".9"/></linearGradient>'
        '<linearGradient id="pl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".35" stop-color="#fff4c9"/><stop offset=".65" stop-color="#ffd27a"/><stop offset="1" stop-color="#ff9a3d" stop-opacity="0"/></linearGradient>'
        '<linearGradient id="snowg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#c9d6f2"/></linearGradient></defs>')


def nagara_shikhara(cx, base, w, h):
    """Curvilinear north-Indian spire with amalaka + kalash."""
    hw = w / 2
    d = (f"M{cx - hw} {base} C{cx - hw} {base - h * .45} {cx - hw * .62} {base - h * .86} {cx - hw * .2} {base - h}"
         f" L{cx + hw * .2} {base - h} C{cx + hw * .62} {base - h * .86} {cx + hw} {base - h * .45} {cx + hw} {base}Z")
    bands = "".join(f'<path d="M{cx - hw * (1 - .38 * f * f):.0f} {base - h * f:.0f} L{cx + hw * (1 - .38 * f * f):.0f} {base - h * f:.0f}" stroke="{RIM}" stroke-width="2"/>' for f in [.2, .38, .55, .7, .83])
    am = f'<ellipse cx="{cx}" cy="{base - h - 10}" rx="{hw * .32:.0f}" ry="14" fill="{SIL}" stroke="{GOLD}" stroke-width="2.4"/>'
    return f'<path d="{d}" fill="{SIL}" stroke="{RIM}" stroke-width="3"/>{bands}{am}{kalash(cx, base - h - 26, 1.1)}'


def arch_himalaya():
    peaks = ('<path d="M-40 760 L160 420 L260 520 L420 250 L560 470 L660 380 L900 700 L1200 560 L1500 690 L1960 520 L1960 1080 L-40 1080Z" fill="#26325c"/>'
             '<path d="M160 420 L205 478 L180 470 L150 500 L130 470Z M420 250 L480 345 L445 330 L420 360 L395 330 L370 345Z M660 380 L720 450 L690 445 L665 470 L640 445Z" fill="url(#snowg)"/>'
             '<path d="M-40 860 L260 640 L520 760 L760 610 L900 700 L1300 640 L1700 760 L1960 680 L1960 1080 L-40 1080Z" fill="#1d2448"/>')
    # Kedar-style stone temple: wide base, mandapa, pyramidal stepped roof, short shikhara
    t = ('<rect x="250" y="770" width="400" height="170" fill="#1b0c1f" stroke="rgba(242,193,78,.55)" stroke-width="3"/>'
         '<path d="M230 770 L450 650 L670 770Z" fill="#1b0c1f" stroke="rgba(242,193,78,.55)" stroke-width="3"/>'
         '<path d="M300 700 L450 560 L600 700Z" fill="#1b0c1f" stroke="rgba(242,193,78,.55)" stroke-width="3"/>'
         + nagara_shikhara(450, 600, 150, 150)
         + door(450, 940, 70, 120) + '<rect x="220" y="940" width="460" height="22" fill="#2a1630"/><rect x="190" y="962" width="520" height="22" fill="#21112a"/>'
         + flag(560, 470, 80, "fg"))
    return peaks + t + '<rect x="-40" y="984" width="2000" height="120" fill="#120714"/>'


def arch_nagara_sea():
    t = ('<rect x="170" y="760" width="560" height="150" fill="#1b0c1f" stroke="rgba(242,193,78,.55)" stroke-width="3"/>'
         + "".join(f'<rect x="{x}" y="790" width="18" height="120" fill="#2b1532"/>' for x in range(200, 720, 64))
         + '<path d="M190 760 Q260 690 330 760Z M560 760 Q630 690 700 760Z" fill="#1b0c1f" stroke="rgba(242,193,78,.55)" stroke-width="3"/>'
         + nagara_shikhara(450, 760, 260, 400) + door(450, 910, 76, 130) + flag(450, 334, 70, "fg"))
    sea = "".join(f'<path id="wv{i}" d="M-200 {930 + i * 40} q60 -18 120 0 t120 0 t120 0 t120 0 t120 0 t120 0 t120 0 t120 0 t120 0 t120 0 t120 0 t120 0 t120 0 t120 0 t120 0 t120 0 t120 0 t120 0 t120 0 t120 0 t120 0" stroke="{GOLD}" stroke-opacity="{.5 - i * .12:.2f}" stroke-width="3" fill="none"/>' for i in range(4))
    return t + '<rect x="-40" y="910" width="2000" height="200" fill="url(#rv)"/>' + sea


def arch_ghats():
    steps = "".join(f'<rect x="{-40 + i * 10}" y="{700 + i * 26}" width="{2000}" height="26" fill="{["#2a1630", "#231129"][i % 2]}"/>' for i in range(8))
    tem = ""
    for x, h, w in [(150, 230, 110), (330, 300, 140), (560, 250, 120), (760, 200, 100)]:
        tem += f'<rect x="{x - w * .55:.0f}" y="{700 - 60}" width="{w * 1.1:.0f}" height="60" fill="{SIL}" stroke="{RIM}" stroke-width="2"/>' + nagara_shikhara(x, 640, w, h)
    ch = "".join(f'<path d="M{x - 40} 700 Q{x} 640 {x + 40} 700Z" fill="{SIL}" stroke="{RIM}" stroke-width="2"/><rect x="{x - 3}" y="700" width="6" height="40" fill="{GOLD}"/>' for x in (240, 450, 660))
    river = '<rect x="-40" y="908" width="2000" height="200" fill="url(#rv)"/>'
    diyas = "".join(f'<g id="dy{i}"><ellipse cx="{x}" cy="{y}" rx="14" ry="5" fill="#c2410c"/><path d="M{x} {y - 22} Q{x + 7} {y - 9} {x} {y - 4} Q{x - 7} {y - 9} {x} {y - 22}Z" fill="#ffd27a"/><circle cx="{x}" cy="{y - 12}" r="16" fill="url(#eg2)"/></g>'
                    for i, (x, y) in enumerate([(120, 960), (300, 1000), (520, 975), (700, 1020), (840, 970)]))
    return ('<defs><radialGradient id="eg2"><stop offset="0" stop-color="#fff1b8" stop-opacity=".9"/><stop offset="1" stop-color="#ff7a1a" stop-opacity="0"/></radialGradient></defs>'
            + tem + ch + steps + river + diyas)


def arch_devi():
    hill = ('<path d="M-40 880 Q180 560 420 470 Q620 520 900 760 Q1300 900 1960 820 L1960 1080 L-40 1080Z" fill="#241332"/>'
            '<path d="M-40 980 Q300 820 560 860 Q760 880 900 840 Q1400 900 1960 880 L1960 1080 L-40 1080Z" fill="#1a0d24"/>'
            '<path d="M-40 1000 L120 860 L240 960 L360 840 L520 980 L680 860 L900 1000 L1200 900 L1500 990 L1960 920 L1960 1080 L-40 1080Z" fill="#140a1c"/>')
    tem = ('<rect x="360" y="430" width="140" height="60" fill="#1b0c1f" stroke="rgba(242,193,78,.55)" stroke-width="2"/>'
           + nagara_shikhara(430, 430, 110, 150) + door(430, 490, 34, 50) + flag(500, 300, 70, "fg"))
    # strings of prayer/bunting flags down the hill
    bunt = ""
    for j, (x0, y0, x1, y1) in enumerate([(430, 470, 120, 760), (430, 470, 760, 700)]):
        for k in range(1, 10):
            f = k / 10
            x = x0 + (x1 - x0) * f
            y = y0 + (y1 - y0) * f + math.sin(f * math.pi) * 40
            col = [SAFF, "#e11d48", GOLD][k % 3]
            bunt += f'<path d="M{x:.0f} {y:.0f} l12 0 l-6 16Z" fill="{col}"/>'
        bunt += f'<path d="M{x0} {y0} Q{(x0 + x1) / 2:.0f} {(y0 + y1) / 2 + 40:.0f} {x1} {y1}" stroke="{GOLD}" stroke-opacity=".6" fill="none" stroke-width="1.6"/>'
    return hill + tem + bunt


def arch_gopuram():
    tiers = ""
    for i in range(7):
        w = 420 - i * 46
        y = 900 - 80 - i * 64
        tiers += f'<rect x="{450 - w / 2:.0f}" y="{y}" width="{w}" height="64" fill="{SIL}" stroke="{RIM}" stroke-width="2.4"/>'
        tiers += "".join(f'<rect x="{450 - w / 2 + 14 + k * 36:.0f}" y="{y + 18}" width="14" height="30" fill="#2e1736"/>' for k in range(int((w - 20) // 36)))
    top_y = 900 - 80 - 7 * 64
    vault = f'<path d="M{450 - 120} {top_y + 4} Q450 {top_y - 90} {450 + 120} {top_y + 4}Z" fill="{SIL}" stroke="{GOLD}" stroke-width="2.4"/>'
    kal = "".join(kalash(x, top_y - 30 if x == 450 else top_y - 18, .8) for x in (370, 410, 450, 490, 530))
    base = '<rect x="200" y="820" width="500" height="120" fill="#1b0c1f" stroke="rgba(242,193,78,.55)" stroke-width="3"/>' + door(450, 940, 90, 150)
    return tiers + vault + kal + base + '<rect x="-40" y="940" width="2000" height="160" fill="#120714"/>'


def arch_cave():
    mtn = ('<path d="M-40 1080 L-40 620 L180 300 L320 420 L470 180 L640 400 L900 520 L1250 380 L1600 560 L1960 450 L1960 1080Z" fill="#26325c"/>'
           '<path d="M470 180 L540 285 L500 270 L470 300 L440 268 L405 285Z M180 300 L230 370 L200 362 L175 385 L150 360Z" fill="url(#snowg)"/>'
           '<path d="M-40 1080 L-40 820 L260 640 L520 720 L900 640 L1400 760 L1960 660 L1960 1080Z" fill="#1d2448"/>')
    cave = ('<path d="M330 760 Q450 560 570 760 L570 800 L330 800Z" fill="#0c0610"/>'
            '<ellipse cx="450" cy="770" rx="70" ry="22" fill="url(#eg2)"/>'
            '<path d="M432 790 Q428 700 450 660 Q472 700 468 790Z" fill="#eaf4ff" opacity=".95"/>')
    path = '<path d="M60 1080 Q200 960 120 900 Q60 860 220 840 Q380 820 330 800" stroke="#f2c14e" stroke-width="5" stroke-dasharray="10 14" fill="none" opacity=".75"/>'
    return ('<defs><radialGradient id="eg2"><stop offset="0" stop-color="#fff1b8" stop-opacity=".9"/><stop offset="1" stop-color="#ff7a1a" stop-opacity="0"/></radialGradient></defs>'
            + mtn + cave + path)


def arch_pillar():
    ground = ('<path d="M-40 760 Q450 700 900 760 Q1400 800 1960 740 L1960 1080 L-40 1080Z" fill="#1a0d24"/>'
              '<path d="M-40 840 Q450 790 900 840 Q1400 870 1960 830 L1960 1080 L-40 1080Z" fill="#140a1c"/>')
    pill = ('<rect id="pil" x="390" y="-40" width="120" height="1160" fill="url(#pl)" style="transform-origin:450px 540px"/>'
            '<rect x="430" y="-40" width="40" height="1160" fill="#fffbe8" opacity=".85"/>'
            '<ellipse cx="450" cy="760" rx="230" ry="36" fill="url(#eg2)" opacity=".9"/>')
    orbs = ('<circle id="ob1" cx="560" cy="700" r="14" fill="#fff4c9"/><circle id="ob2" cx="340" cy="780" r="14" fill="#ffd27a"/>')
    return ('<defs><radialGradient id="eg2"><stop offset="0" stop-color="#fff1b8" stop-opacity=".95"/><stop offset="1" stop-color="#ff7a1a" stop-opacity="0"/></radialGradient></defs>'
            + ground + pill + orbs)


def arch_gurudwara():
    pool = '<rect x="-40" y="900" width="2000" height="200" fill="url(#rv)"/>'
    b = ('<rect x="220" y="700" width="460" height="180" fill="#1b0c1f" stroke="rgba(242,193,78,.8)" stroke-width="3"/>'
         '<path d="M330 700 Q450 520 570 700Z" fill="#3a2410" stroke="#f2c14e" stroke-width="3"/>'
         + "".join(f'<path d="M{x - 30} 700 Q{x} 640 {x + 30} 700Z" fill="#3a2410" stroke="#f2c14e" stroke-width="2"/>' for x in (250, 650))
         + "".join(f'<rect x="{x}" y="740" width="26" height="60" rx="13" fill="#ffcf73"/>' for x in range(250, 660, 60)) + kalash(450, 575, 1))
    causeway = '<rect x="0" y="872" width="1960" height="16" fill="#2a1630"/>'
    return b + causeway + pool


def arch_pagoda():
    """Himachal hill temple (Kath-Kuni / pagoda style, e.g. the Hidimba or Bhimakali type): stone-and-timber base,
    stacked hipped wooden roofs, brass finial, deodar forest and snow ridges. Stylised archetype, not a likeness."""
    ridge = ('<path d="M-40 720 L140 470 L260 560 L430 330 L600 520 L720 430 L900 640 L1250 520 L1600 640 L1960 500 L1960 1080 L-40 1080Z" fill="#26325c"/>'
             '<path d="M430 330 L492 418 L458 404 L430 432 L402 404 L368 418Z M140 470 L185 530 L160 522 L135 548 L112 524Z M720 430 L772 494 L745 488 L720 512 L698 488Z" fill="url(#snowg)"/>'
             '<path d="M-40 880 L240 700 L520 800 L780 690 L900 740 L1400 700 L1960 780 L1960 1080 L-40 1080Z" fill="#1d2448"/>')
    def deodar(x, base, h, op=1):
        t = "".join(f'<path d="M{x} {base - h + i * h * .2:.0f} L{x + h * (.16 + i * .06):.0f} {base - h * (.62 - i * .2) + h * .2:.0f} L{x - h * (.16 + i * .06):.0f} {base - h * (.62 - i * .2) + h * .2:.0f}Z" fill="#101a2e" opacity="{op}"/>' for i in range(4))
        return t + f'<rect x="{x - 4}" y="{base - h * .1:.0f}" width="8" height="{h * .12:.0f}" fill="#101a2e" opacity="{op}"/>'
    trees = "".join(deodar(x, b, h, o) for x, b, h, o in [(60, 900, 300, .9), (150, 930, 380, 1), (760, 920, 360, 1), (850, 890, 280, .9), (690, 950, 240, 1)])
    t = ('<rect x="320" y="800" width="260" height="140" fill="#1b0c1f" stroke="rgba(242,193,78,.55)" stroke-width="3"/>'
         + "".join(f'<rect x="320" y="{y}" width="260" height="8" fill="#3a2410"/>' for y in (830, 870, 910))
         + door(450, 940, 60, 100))
    roofs = ""
    for i, (w, y, h) in enumerate([(400, 800, 60), (330, 700, 70), (260, 610, 64), (190, 530, 56)]):
        roofs += (f'<path d="M{450 - w / 2 - 20:.0f} {y} L{450 - w / 2 + 30:.0f} {y - h} L{450 + w / 2 - 30:.0f} {y - h} L{450 + w / 2 + 20:.0f} {y}Z" fill="{SIL}" stroke="{GOLD}" stroke-width="2.4"/>'
                  + "".join(f'<line x1="{450 - w / 2 + 20 + k * 24:.0f}" y1="{y - 4}" x2="{450 - w / 2 + 34 + k * 24:.0f}" y2="{y - h + 6}" stroke="{RIM}" stroke-width="1.4"/>' for k in range(int((w - 40) // 24)))
                  + (f'<rect x="{450 - w * .36:.0f}" y="{y - h - (100 - h) + 4:.0f}" width="{w * .72:.0f}" height="{100 - h - 4}" fill="#1b0c1f" stroke="{RIM}" stroke-width="2"/>' if i < 3 else ""))
    cone = (f'<path d="M370 474 Q450 330 530 474Z" fill="{SIL}" stroke="{GOLD}" stroke-width="2.4"/>' + kalash(450, 380, 1.0)
            + "".join(f'<circle cx="{x}" cy="{y}" r="5" fill="{GOLD2}"/>' for x, y in [(230, 800), (670, 800), (285, 700), (615, 700), (320, 610), (580, 610)]))
    return ridge + trees + roofs + cone + t + flag(600, 940, 160, "fg") + '<rect x="-40" y="940" width="2000" height="160" fill="#120714"/>'


ARCH = {"himalaya": arch_himalaya, "nagara": arch_nagara_sea, "ghats": arch_ghats, "devi": arch_devi,
        "gopuram": arch_gopuram, "cave": arch_cave, "pillar": arch_pillar, "gurudwara": arch_gurudwara,
        "pagoda": arch_pagoda}
SKY_FOR = {"himalaya": "snow", "nagara": "dusk", "ghats": "saffron", "devi": "dawn", "gopuram": "dusk", "cave": "night", "pillar": "night", "gurudwara": "dawn", "pagoda": "snow"}


def scene_svg(arch, uid, sky=None):
    sky = sky or SKY_FOR[arch]
    sun = {"himalaya": (470, 420, 110), "pagoda": (700, 250, 60), "pillar": (450, 420, 60), "cave": (700, 220, 50)}.get(arch, (470, 560, 140))
    return (sky_svg(uid, sky, sun) + (stars(uid, 80, 7) if sky in ("night", "snow", "dusk") else "")
            + mandala(sun[0], sun[1], 300, f"md{uid}", op=.18)
            + f'<svg class="lay" viewBox="0 0 {W} {H}">{DEFS}<g>{ARCH[arch]()}</g></svg>')


def arch_js(arch, uid_prefix, dur, start=0.0):
    """Small seamless secondary motion for an archetype (flag sway, waves, diya bob, pillar pulse)."""
    js = []
    if arch in ("himalaya", "nagara", "devi", "pagoda"):
        js.append(f'tl.fromTo("{uid_prefix} #fg",{{rotation:-6}},{{rotation:6,duration:{dur / 8:.3f},ease:"sine.inOut",yoyo:true,repeat:7}},{start});')
    if arch == "nagara":
        for i in range(4):
            js.append(f'tl.fromTo("{uid_prefix} #wv{i}",{{x:0}},{{x:-240,duration:{dur:.3f},ease:"none"}},{start});')
    if arch == "ghats":
        for i in range(5):
            js.append(f'tl.fromTo("{uid_prefix} #dy{i}",{{y:0}},{{y:-8,duration:{dur / 6:.3f},ease:"sine.inOut",yoyo:true,repeat:5}},{start + i * .2:.2f});')
    if arch == "pillar":
        js.append(f'tl.fromTo("{uid_prefix} #pil",{{scaleX:.85,opacity:.85}},{{scaleX:1.12,opacity:1,duration:{dur / 4:.3f},ease:"sine.inOut",yoyo:true,repeat:3}},{start});')
        js.append(f'tl.fromTo("{uid_prefix} #ob1",{{y:0}},{{y:-640,duration:{dur / 2:.3f},ease:"sine.inOut",yoyo:true,repeat:1}},{start});')
        js.append(f'tl.fromTo("{uid_prefix} #ob2",{{y:0}},{{y:300,duration:{dur / 2:.3f},ease:"sine.inOut",yoyo:true,repeat:1}},{start});')
    return "".join(js)


def wrap(name, dur, body, css, js):
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


SHADE = ('.shade{position:absolute;inset:0;background:linear-gradient(90deg,rgba(20,10,28,0) 0%,rgba(20,10,28,.05) 40%,rgba(20,10,28,.62) 62%,rgba(20,10,28,.9) 100%)}'
         '.vig{position:absolute;inset:0;background:radial-gradient(ellipse at 30% 50%,rgba(0,0,0,0) 50%,rgba(0,0,0,.42) 100%)}')


# ------------------------------------------------------------------------------------------------ multi-scene hero (hub)
def scenes_hero(name, scenes, kicker, dur=14.0, xf=.7):
    """scenes: [{arch, deva, en, sky?}] — each scene = illustrated background + Devanagari word + English line (right side)."""
    n = len(scenes)
    seg = dur / n
    d = prep(name)
    body, js = [], [embers_js(dur)]
    for i, s in enumerate(scenes):
        uid = f"s{i}"
        body.append(f'<div id="{uid}" class="lay clip" data-start="0" data-duration="{dur}" data-track-index="{i}">{scene_svg(s["arch"], uid, s.get("sky"))}</div>')
        js.append(arch_js(s["arch"], f"#{uid}", dur))
        js.append(f'tl.fromTo("#md{uid}",{{rotation:0}},{{rotation:30,duration:{dur},ease:"none"}},0);')
        a = i * seg
        if i == 0:
            js.append(f'tl.set("#{uid}",{{opacity:1}},0);tl.set("#{uid}",{{opacity:0}},{seg + xf + .05:.2f});tl.set("#{uid}",{{opacity:1}},{dur - xf - .3:.2f});')
            js.append(f'tl.fromTo("#{uid}",{{scale:1}},{{scale:1.05,duration:{seg + xf:.2f},ease:"none"}},0);tl.set("#{uid}",{{scale:1}},{seg + xf + .1:.2f});')
        else:
            js.append(f'tl.set("#{uid}",{{opacity:0}},0);tl.to("#{uid}",{{opacity:1,duration:{xf},ease:"none"}},{a:.2f});')
            js.append(f'tl.fromTo("#{uid}",{{scale:1}},{{scale:1.05,duration:{seg + xf:.2f},ease:"none"}},{a:.2f});')
            if i < n - 1:
                js.append(f'tl.set("#{uid}",{{opacity:0}},{(i + 1) * seg + xf + .05:.2f});')
            else:
                js.append(f'tl.to("#{uid}",{{opacity:0,duration:{xf + .2:.2f},ease:"none"}},{dur - xf - .2:.2f});')
    body.append(f'<div class="vig clip" data-start="0" data-duration="{dur}" data-track-index="20"></div>')
    body.append(f'<div class="clip" data-start="0" data-duration="{dur}" data-track-index="21" style="position:absolute;inset:0;overflow:hidden">{embers()}</div>')
    body.append(f'<div class="shade clip" data-start="0" data-duration="{dur}" data-track-index="22"></div>')
    texts = "".join(f'<div class="tx" id="t{i}"><div class="deva" style="font-size:{s.get("deva_size", 150)}px">{esc(s["deva"])}</div><div class="en" style="font-size:60px">{esc(s["en"])}</div></div>' for i, s in enumerate(scenes))
    body.append(f'<div class="hud clip" data-start="0" data-duration="{dur}" data-track-index="23"><div class="kick">{esc(kicker)}</div><div class="bar" id="bar"></div><div style="position:relative;height:420px">{texts}</div></div>')
    for i in range(n):
        a = i * seg
        if i == 0:
            js.append(f'tl.set("#t0",{{opacity:1,y:0}},0);tl.to("#t0",{{opacity:0,y:-24,duration:.45}},{seg - .1:.2f});tl.set("#t0",{{y:24}},{seg + .4:.2f});tl.to("#t0",{{opacity:1,y:0,duration:.5}},{dur - .5:.2f});')
        else:
            js.append(f'tl.set("#t{i}",{{opacity:0,y:24}},0);tl.to("#t{i}",{{opacity:1,y:0,duration:.55,ease:"power2.out"}},{a + .3:.2f});tl.to("#t{i}",{{opacity:0,y:-24,duration:.45}},{(i + 1) * seg - .1 if i < n - 1 else dur - 1.0:.2f});')
    js.append(f'tl.fromTo("#bar",{{scaleX:0}},{{scaleX:1,duration:{dur - .4:.2f},ease:"none"}},.1);tl.to("#bar",{{opacity:0,duration:.25}},{dur - .3:.2f});')
    css = SHADE + ('.hud{position:absolute;right:150px;top:250px;width:860px;text-align:right}'
                   '.tx{position:absolute;right:0;top:0;width:860px;opacity:0}.tx .en{margin-top:8px;line-height:1.08}'
                   '.bar{height:5px;width:380px;margin:18px 0 34px auto;background:linear-gradient(90deg,#ff8a2a,#f2c14e);border-radius:3px;transform-origin:100% 50%}')
    (d / "index.html").write_text(wrap(name, dur, "\n".join(body), css, "".join(js)), encoding="utf-8")
    return d


def pilgrim_hero():
    return scenes_hero("pilgrim-hero", [
        {"arch": "himalaya", "deva": "केदारनाथ", "en": "Shiva’s shrine in the snows"},
        {"arch": "nagara", "deva": "सोमनाथ", "en": "The first Jyotirlinga, by the sea"},
        {"arch": "ghats", "deva": "काशी", "en": "Lamps on the Ganga every evening"},
        {"arch": "devi", "deva": "शक्ति", "en": "The Devi’s hills of Himachal"},
    ], "Tirth Yatra · Pilgrimage tours of India")


# ------------------------------------------------------------------------------------------------ single-scene temple hero (per page)
def temple_hero(slug):
    spec = json.loads((KIT / "src" / "media" / f"{slug}.json").read_text(encoding="utf-8"))["hero"]
    arch, deva, kick, beats = spec["arch"], spec["deva"], spec["kicker"], spec["beats"]
    assert arch in ARCH, f"unknown archetype {arch}"
    assert 3 <= len(beats) <= 4 and all(len(b.split()) <= 8 for b in beats), "3-4 beats, max 8 words each"
    dur = 14.0
    name = f"{slug}-hero"
    d = prep(name)
    body = [f'<div id="s0" class="lay clip" data-start="0" data-duration="{dur}" data-track-index="0">{scene_svg(arch, "s0", spec.get("sky"))}</div>',
            f'<div class="vig clip" data-start="0" data-duration="{dur}" data-track-index="1"></div>',
            f'<div class="clip" data-start="0" data-duration="{dur}" data-track-index="2" style="position:absolute;inset:0;overflow:hidden">{embers(len(slug))}</div>',
            f'<div class="shade clip" data-start="0" data-duration="{dur}" data-track-index="3"></div>']
    bt = "".join(f'<div class="bt" id="b{i}"><span class="no">{i + 1:02d}</span>{esc(b)}</div>' for i, b in enumerate(beats))
    ds = spec.get("deva_size", 150 if len(deva) <= 9 else 118)
    body.append(f'<div class="hud clip" data-start="0" data-duration="{dur}" data-track-index="4"><div class="kick">{esc(kick)}</div>'
                f'<div class="deva" style="font-size:{ds}px;margin-top:10px">{esc(deva)}</div><div class="bar" id="bar"></div><div style="position:relative;height:200px">{bt}</div></div>')
    js = [embers_js(dur), arch_js(arch, "#s0", dur), f'tl.fromTo("#mds0",{{rotation:0}},{{rotation:30,duration:{dur},ease:"none"}},0);',
          f'tl.fromTo("#s0",{{scale:1}},{{scale:1.05,duration:{dur / 2},ease:"sine.inOut",yoyo:true,repeat:1}},0);']
    n = len(beats)
    seg = dur / n
    for i in range(n):
        a = i * seg
        if i == 0:
            js.append(f'tl.set("#b0",{{opacity:1,y:0}},0);tl.to("#b0",{{opacity:0,y:-20,duration:.4}},{seg - .1:.2f});tl.set("#b0",{{y:20}},{seg + .3:.2f});tl.to("#b0",{{opacity:1,y:0,duration:.45}},{dur - .48:.2f});')
        else:
            js.append(f'tl.set("#b{i}",{{opacity:0,y:20}},0);tl.to("#b{i}",{{opacity:1,y:0,duration:.5,ease:"power2.out"}},{a + .25:.2f});tl.to("#b{i}",{{opacity:0,y:-20,duration:.4}},{(i + 1) * seg - .1 if i < n - 1 else dur - 1.0:.2f});')
    js.append(f'tl.fromTo("#bar",{{scaleX:0}},{{scaleX:1,duration:{dur - .4:.2f},ease:"none"}},.1);tl.to("#bar",{{opacity:0,duration:.25}},{dur - .3:.2f});')
    css = SHADE + ('.hud{position:absolute;right:150px;top:230px;width:900px;text-align:right}'
                   '.bar{height:5px;width:380px;margin:14px 0 30px auto;background:linear-gradient(90deg,#ff8a2a,#f2c14e);border-radius:3px;transform-origin:100% 50%}'
                   '.bt{position:absolute;right:0;top:0;width:900px;opacity:0;font:700 52px/1.16 "CG",serif;color:#fff7e6;text-shadow:0 6px 30px rgba(0,0,0,.55)}'
                   '.bt .no{display:inline-block;font:800 24px "SZ",sans-serif;color:#f2c14e;letter-spacing:.2em;margin-right:18px;vertical-align:middle}')
    (d / "index.html").write_text(wrap(name, dur, "\n".join(body), css, "".join(js)), encoding="utf-8")
    return d


# ------------------------------------------------------------------------------------------------ map of light (stops by lat/lon, no borders)
LON0, LON1, LAT0, LAT1 = 67.5, 97.5, 6.5, 36.5


BOUNDS = None  # optional (lon0, lon1, lat0, lat1) zoom for regional route maps (route spec "bounds"; added 8 Oct 2026)


def proj(lat, lon, box):
    x0, y0, x1, y1 = box
    l0, l1, a0, a1 = BOUNDS or (LON0, LON1, LAT0, LAT1)
    return x0 + (lon - l0) / (l1 - l0) * (x1 - x0), y0 + (a1 - lat) / (a1 - a0) * (y1 - y0)


def light_map_comp(name, stops, title, sub, dur=13.0, box=(200, 40, 1240, 1050), route=False):
    """stops: [{name, deva, state, lat, lon}] ignite one by one with a pillar of light; graticule + stars, no borders."""
    d = prep(name)
    r = random.Random(17)
    star = "".join(f'<circle cx="{r.uniform(0, W):.0f}" cy="{r.uniform(0, H):.0f}" r="{r.uniform(.6, 1.8):.1f}" fill="#fff" opacity="{r.uniform(.15, .55):.2f}"/>' for _ in range(160))
    grat = ""
    if BOUNDS:
        l0, l1, a0, a1 = BOUNDS
        lons = [l0 + (l1 - l0) * k / 6 for k in range(1, 6)]
        lats = [a0 + (a1 - a0) * k / 6 for k in range(1, 6)]
        lbl = lambda v: f"{v:.1f}°N"
    else:
        lons, lats, lbl = range(70, 98, 5), range(10, 37, 5), (lambda v: f"{v}°N")
    for lon in lons:
        x, _ = proj(0 if BOUNDS else LAT0, lon, box)
        grat += f'<line x1="{x:.0f}" y1="{box[1]}" x2="{x:.0f}" y2="{box[3]}" stroke="#f2c14e" stroke-opacity=".08"/>'
    for lat in lats:
        _, y = proj(lat, 0, box)
        grat += f'<line x1="{box[0]}" y1="{y:.0f}" x2="{box[2]}" y2="{y:.0f}" stroke="#f2c14e" stroke-opacity=".08"/>'
        grat += f'<text x="{box[0] - 12}" y="{y + 6:.0f}" text-anchor="end" font-family="SZ" font-size="15" fill="#f2c14e" fill-opacity=".35">{lbl(lat)}</text>'
    pts = [proj(s["lat"], s["lon"], box) for s in stops]
    path = "M" + " L".join(f"{x:.0f} {y:.0f}" for x, y in pts)
    plen = sum(math.dist(pts[i], pts[i + 1]) for i in range(len(pts) - 1)) + 10
    dots, labels, js = [], [], []
    t0, step = .7, (dur - 3.2) / len(stops)
    for i, ((x, y), s) in enumerate(zip(pts, stops)):
        dots.append(f'<g id="p{i}" style="opacity:.25"><rect x="{x - 9:.0f}" y="{y - 260:.0f}" width="18" height="260" fill="url(#pl2)" id="pb{i}" style="transform-origin:{x:.0f}px {y:.0f}px"/>'
                    f'<circle cx="{x:.0f}" cy="{y:.0f}" r="30" fill="url(#gl)"/><circle cx="{x:.0f}" cy="{y:.0f}" r="7" fill="#fff4c9"/>'
                    f'<text x="{x + 16:.0f}" y="{y + 6:.0f}" font-family="SZ" font-weight="700" font-size="19" fill="#ffe7a8">{i + 1}</text></g>')
        labels.append(f'<div class="lb" id="l{i}"><b>{i + 1:02d}</b><span class="dv">{esc(s["deva"])}</span><span class="nm">{esc(s["name"])}<small>{esc(s["state"])}</small></span></div>')
        t = t0 + i * step
        js.append(f'tl.set("#p{i}",{{opacity:.25}},0);tl.to("#p{i}",{{opacity:1,duration:.35}},{t:.2f});tl.fromTo("#pb{i}",{{scaleY:0}},{{scaleY:1,duration:.55,ease:"power2.out"}},{t:.2f});'
                  f'tl.to("#pb{i}",{{opacity:.35,duration:.6}},{t + .8:.2f});')
        js.append(f'tl.set("#l{i}",{{opacity:.28}},0);tl.to("#l{i}",{{opacity:1,x:-10,duration:.3}},{t:.2f});tl.to("#l{i}",{{x:0,duration:.3}},{t + .4:.2f});')
    tend = t0 + len(stops) * step
    if route:
        js.append(f'tl.fromTo("#route",{{strokeDashoffset:{plen:.0f}}},{{strokeDashoffset:0,duration:{tend - t0:.2f},ease:"none"}},{t0});')
    # loop: fade everything back to the dim start state
    fo = dur - 1.1
    if route:
        js.append(f'tl.to("#route",{{opacity:0,duration:.8}},{fo:.2f});tl.set("#route",{{strokeDashoffset:{plen:.0f},opacity:.75}},{dur - .05:.2f});')
    for i in range(len(stops)):
        js.append(f'tl.to("#p{i}",{{opacity:.25,duration:.8}},{fo:.2f});tl.to("#l{i}",{{opacity:.28,duration:.8}},{fo:.2f});tl.set("#pb{i}",{{opacity:1,scaleY:0}},{dur - .05:.2f});')
    js.append(f'tl.fromTo("#mdm",{{rotation:0}},{{rotation:30,duration:{dur},ease:"none"}},0);')
    svg = (f'<svg class="lay" viewBox="0 0 {W} {H}"><defs><radialGradient id="gl"><stop offset="0" stop-color="#ffe9a8" stop-opacity=".9"/><stop offset="1" stop-color="#ff8a2a" stop-opacity="0"/></radialGradient>'
           f'<linearGradient id="pl2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".7" stop-color="#ffe2a0" stop-opacity=".9"/><stop offset="1" stop-color="#ffb347"/></linearGradient>'
           f'<radialGradient id="bgg" cx=".35" cy=".5" r=".75"><stop offset="0" stop-color="#2a1340"/><stop offset="1" stop-color="#0a0614"/></radialGradient></defs>'
           f'<rect width="{W}" height="{H}" fill="url(#bgg)"/>{star}{grat}'
           + (f'<path id="route" d="{path}" fill="none" stroke="#f2c14e" stroke-opacity=".75" stroke-width="2.5" stroke-dasharray="{plen:.0f}" stroke-dashoffset="{plen:.0f}"/>' if route else '')
           + f'{"".join(dots)}</svg>')
    body = [mandala(730, 540, 420, "mdm", op=.07).replace('class="lay"', 'class="lay clip" data-start="0" data-duration="%s" data-track-index="0"' % dur),
            f'<div class="lay clip" data-start="0" data-duration="{dur}" data-track-index="1">{svg}</div>',
            f'<div class="side clip" data-start="0" data-duration="{dur}" data-track-index="2"><div class="kick">{esc(title)}</div><div class="sub">{esc(sub)}</div>{"".join(labels)}</div>']
    css = ('.side{position:absolute;right:70px;top:70px;width:560px}.sub{font:600 30px "CG",serif;color:#fff7e6;margin:8px 0 18px}'
           '.lb{display:flex;align-items:center;gap:14px;height:70px;border-bottom:1px solid rgba(242,193,78,.16);opacity:.28}'
           '.lb b{font:800 18px "SZ",sans-serif;color:#f2c14e;width:30px}.lb .dv{font:34px "TD",serif;color:#ffd98a;min-width:200px}'
           '.lb .nm{font:700 24px "SZ",sans-serif;color:#fff}.lb small{display:block;font:500 16px "SZ",sans-serif;color:rgba(255,255,255,.6);margin-top:2px}')
    (d / "index.html").write_text(wrap(name, dur, "\n".join(body), css, "".join(js)), encoding="utf-8")
    return d


def light_map():
    J = json.loads((DATA / "jyotirlinga.json").read_text(encoding="utf-8"))
    short = {"Somnath": "Somnath", "Mallikarjuna": "Mallikarjuna", "Mahakaleshwar": "Mahakaleshwar", "Omkareshwar": "Omkareshwar", "Kedarnath": "Kedarnath",
             "Bhimashankar": "Bhimashankar", "Kashi Vishwanath": "Kashi Vishwanath", "Trimbakeshwar": "Trimbakeshwar", "Vaidyanath": "Vaidyanath",
             "Nageshwar": "Nageshwar", "Rameshwaram": "Rameshwaram", "Grishneshwar": "Grishneshwar"}
    stops = []
    for j in J:
        nm = j["name_en"].replace(" Jyotirlinga", "").split(" (")[0]
        stops.append({"name": short.get(nm, nm), "deva": j["name_hi"].replace(" ज्योतिर्लिंग", "").split(" (")[0].strip(), "state": j["state"], "lat": j["lat"], "lon": j["lon"]})
    return light_map_comp("light-map", stops, "12 Jyotirlingas", "Twelve pillars of light across India")


def route_map(slug):
    global BOUNDS
    spec = json.loads((KIT / "src" / "media" / f"{slug}.json").read_text(encoding="utf-8"))["route"]
    BOUNDS = tuple(spec["bounds"]) if spec.get("bounds") else None
    return light_map_comp(f"{slug}-route", spec["stops"], spec["title"], spec["sub"], dur=float(spec.get("dur", 13)), route=True)


# ------------------------------------------------------------------------------------------------ story strip (legend in 4 beats, full-frame)
def story_strip(slug):
    spec = json.loads((KIT / "src" / "media" / f"{slug}.json").read_text(encoding="utf-8"))["story"]
    beats = spec["beats"]  # [{arch, line}] 4 items
    dur = 16.0
    name = f"{slug}-story"
    d = prep(name)
    n = len(beats)
    seg = dur / n
    body, js = [], [embers_js(dur)]
    for i, b in enumerate(beats):
        uid = f"q{i}"
        body.append(f'<div id="{uid}" class="lay clip" data-start="0" data-duration="{dur}" data-track-index="{i}">{scene_svg(b["arch"], uid, b.get("sky"))}</div>')
        js.append(arch_js(b["arch"], f"#{uid}", dur))
        a = i * seg
        if i == 0:
            js.append(f'tl.set("#{uid}",{{opacity:1}},0);tl.set("#{uid}",{{opacity:0}},{seg + .75:.2f});tl.set("#{uid}",{{opacity:1}},{dur - 1:.2f});')
        else:
            js.append(f'tl.set("#{uid}",{{opacity:0}},0);tl.to("#{uid}",{{opacity:1,duration:.7}},{a:.2f});')
            js.append(f'tl.set("#{uid}",{{opacity:0}},{(i + 1) * seg + .75:.2f});' if i < n - 1 else f'tl.to("#{uid}",{{opacity:0,duration:.9}},{dur - .9:.2f});')
    body.append(f'<div class="clip" data-start="0" data-duration="{dur}" data-track-index="9" style="position:absolute;inset:0;overflow:hidden">{embers(5)}</div>')
    body.append(f'<div class="shade clip" data-start="0" data-duration="{dur}" data-track-index="10"></div>')
    caps = "".join(f'<div class="cp" id="c{i}"><span>{i + 1} / {n}</span>{esc(b["line"])}</div>' for i, b in enumerate(beats))
    body.append(f'<div class="cap clip" data-start="0" data-duration="{dur}" data-track-index="11"><div class="kick">{esc(spec["title"])}</div><div style="position:relative;height:300px;margin-top:16px">{caps}</div></div>')
    for i in range(n):
        a = i * seg
        if i == 0:
            js.append(f'tl.set("#c0",{{opacity:1}},0);tl.to("#c0",{{opacity:0,duration:.4}},{seg - .1:.2f});tl.to("#c0",{{opacity:1,duration:.5}},{dur - .55:.2f});')
        else:
            js.append(f'tl.set("#c{i}",{{opacity:0}},0);tl.to("#c{i}",{{opacity:1,duration:.5}},{a + .35:.2f});tl.to("#c{i}",{{opacity:0,duration:.4}},{(i + 1) * seg - .1 if i < n - 1 else dur - .6:.2f});')
    css = SHADE + ('.cap{position:absolute;right:120px;top:300px;width:820px;text-align:right}'
                   '.cp{position:absolute;right:0;top:0;width:820px;opacity:0;font:700 62px/1.15 "CG",serif;color:#fff7e6;text-shadow:0 6px 30px rgba(0,0,0,.6)}'
                   '.cp span{display:block;font:800 22px "SZ",sans-serif;letter-spacing:.24em;color:#f2c14e;margin-bottom:14px}')
    (d / "index.html").write_text(wrap(name, dur, "\n".join(body), css, "".join(js)), encoding="utf-8")
    return d


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        raise SystemExit(__doc__)
    fn = {"pilgrim-hero": pilgrim_hero, "light-map": light_map}.get(a[0])
    if fn:
        print(fn())
    elif a[0] in ("temple-hero", "story-strip", "route-map"):
        print({"temple-hero": temple_hero, "story-strip": story_strip, "route-map": route_map}[a[0]](a[1]))
    else:
        raise SystemExit(f"unknown composition {a[0]}")
