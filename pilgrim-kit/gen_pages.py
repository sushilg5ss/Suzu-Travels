#!/usr/bin/env python3
"""Suzu Pilgrim Kit — page generator.

    python3 gen_pages.py <slug|all>        -> out/<slug>.html   (then: python3 build.py <slug> -> out/<slug>.min.html)

Base pages (functions below): pilgrimage-tours (hub) · 12-jyotirlinga (guide + map of light).
Every other page is DATA: src/pages/<slug>.json rendered by content_page() — see README.md "Page file schema".
Facts come from data/*.json (research, each fact with source + as_of) — never type a date or timing by hand that is not in
the data or the page's fact pack. Links between pages come from live.json (published pages only).
Copy is original English with Devanagari names; legends are retold in our own words as tradition ("it is believed…").
"""
import html, json, math, os, pathlib, re, sys, urllib.parse

KIT = pathlib.Path(__file__).resolve().parent
J = json.loads((KIT / "data" / "jyotirlinga.json").read_text(encoding="utf-8"))
S = {x["slug"]: x for x in json.loads((KIT / "data" / "shaktipeeth.json").read_text(encoding="utf-8"))}
Y = {x["slug"]: x for x in json.loads((KIT / "data" / "yatras.json").read_text(encoding="utf-8"))}
MEDIA = json.loads((KIT / "media.json").read_text()) if (KIT / "media.json").exists() else {}
LIVE = json.loads((KIT / "live.json").read_text()) if (KIT / "live.json").exists() else {}
VERIFIED = "8 Oct 2026"
REPO = "sushilg5ss/suzu-travels"
HUB = "/pilgrimage-tours/"
WA = "https://wa.me/917087488961?text="
QUOTE = "/himachal-tour-packages-quote/"
REG = "HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022"
# existing bookable packages on suzutravels.com that OWN the commercial keywords (never compete, always link)
PKG = {
    "jyotirlinga": ("/tours/12-jyotirlinga-tour-package/", "12 Jyotirlinga tour package", "All 12 temples in one planned journey"),
    "shakti5": ("/tours/5-shakti-peeth-tour-package-himachal-5-days-4-nights/", "5 Shakti Peeth Yatra, Himachal", "Naina Devi to Chamunda, 5 days"),
    "chardham": ("/packages/ultimate-char-dham-yatra/", "Char Dham Yatra package", "12 days from Haridwar"),
    "dodham": ("/tours/holiest-himalayan-pilgrimage-tour/", "Kedarnath–Badrinath Do Dham tour", "From Haridwar"),
    "chardham-nri": ("/char-dham-yatra-for-nri/", "Char Dham Yatra for NRIs", "Planned from Delhi, quoted in USD"),
    "chardham-dates": ("/char-dham-closing-dates-2026/", "Char Dham closing dates 2026", "Our live update post"),
    "amarnath": ("/packages/kashmir-amarnath-by-helicopter/", "Amarnath Yatra package", "Baltal route, 4 days"),
    "vaishno": ("/tours/amazing-kashmir-vaishno-devi-package/", "Kashmir with Vaishno Devi", "7 days"),
    "kashi": ("/tours/spiritual-journey-varanasi-ayodhya-prayagraj-tour-package/", "Varanasi–Ayodhya–Prayagraj tour", "6 days"),
    "kainchi": ("/kainchi-dham-registration-2026-new-rules-and-crowd-cap/", "Kainchi Dham registration 2026", "Rules and daily cap"),
    "chardham-archive": ("/destination/chardham-tour-packages/", "All Char Dham trips", "Every Uttarakhand yatra we run"),
}


def e(s):
    # " - " -> " – ": WordPress' wptexturize does this on output anyway, so the build matches live (cmp_live 0 diffs)
    return html.escape(str(s), quote=True).replace(" - ", " – ")


def wa(text):
    return WA + urllib.parse.quote(text)


def ext(url, text):
    return f'<a href="{e(url)}" target="_blank" rel="noopener">{text}</a>'


def live_path(slug):
    return LIVE.get(slug, {}).get("path")


LOCAL_MEDIA = bool(os.environ.get("PK_LOCAL_MEDIA"))


def media_url(slug, fname):
    if LOCAL_MEDIA:
        return (KIT / "media" / slug / fname).as_uri()
    sha = MEDIA.get(slug)
    if not sha:
        raise SystemExit(f"media.json has no commit pinned for '{slug}' — run make_media.sh, push, then pin_media.py")
    return f"https://cdn.jsdelivr.net/gh/{REPO}@{sha}/pilgrim-kit/media/{slug}/{fname}"


def hero_video(slug, comp, alt):
    u = lambda f: media_url(slug, f)
    return (f'<video autoplay muted loop playsinline preload="metadata" poster="{u(comp + "-poster.webp")}" aria-label="{e(alt)}">'
            f'<source media="(max-width: 640px)" src="{u(comp + "-m.webm")}" type="video/webm">'
            f'<source media="(max-width: 640px)" src="{u(comp + "-m.mp4")}" type="video/mp4">'
            f'<source src="{u(comp + ".webm")}" type="video/webm"><source src="{u(comp + ".mp4")}" type="video/mp4"></video>')


def lazy_video(slug, comp, alt):
    u = lambda f: media_url(slug, f)
    return (f'<video data-lazy muted loop playsinline preload="none" poster="{u(comp + "-poster.webp")}" aria-label="{e(alt)}">'
            f'<source data-src="{u(comp + ".webm")}" type="video/webm"><source data-src="{u(comp + ".mp4")}" type="video/mp4"></video>')


def nav(items, cta_href):
    a = "".join(f'<a href="#{i}">{t}</a>' for i, t in items)
    return f'<nav class="szp-nav" aria-label="On this page"><div class="szp-nav-in">{a}<a class="cta" href="{cta_href}" target="_blank" rel="noopener">Plan my yatra</a></div></nav>'


def faq(items):
    return '<div class="szp-faq">' + "".join(f"<details><summary>{e(q)}</summary><p>{a}</p></details>" for q, a in items) + "</div>"


def faq_ld(items):
    strip = lambda s: re.sub(r"<[^>]+>", "", s)
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": html.unescape(strip(a))}} for q, a in items]}


def ld(*objs):
    g = {"@context": "https://schema.org", "@graph": list(objs)}
    return '<script type="application/ld+json">' + json.dumps(g, ensure_ascii=False).replace("</", "<\\/") + "</script>"


def quote_block(title, text, wa_text, second=None):
    s = second or (QUOTE, "Send a quote request")
    return (f'<div class="szp-quote"><div><span class="k">Plan it with Suzu</span><h2>{title}</h2><p>{text}</p></div>'
            f'<div class="szp-btns"><a class="szp-btn gold" href="{wa(wa_text)}" target="_blank" rel="noopener">WhatsApp +91 70874 88961</a>'
            f'<a class="szp-btn ghost" href="{s[0]}">{s[1]}</a></div></div>')


def trust(verified=None):
    return (f'<div class="szp-trust"><span><a href="/certificates/">{REG}</a></span><span>Dates &amp; timings checked {e(verified or VERIFIED)}</span>'
            f'<span>Official sources listed</span><span>Office in Bilaspur, Himachal</span></div>')


def sources(items):
    return '<ol class="szp-src">' + "".join(f"<li>{ext(u, e(t))}</li>" for t, u in items) + "</ol>"


def page(body):
    return f'<div class="szp">{body}</div><script>/*KITJS*/</script>'


def pkg_link(key, cls="szp-link pkg"):
    p, n, c = PKG[key]
    return f'<a class="{cls}" href="{p}"><span class="n">{e(n)}</span><span class="c">{e(c)}</span></a>'


def tile(v):
    return f'<a class="szp-link" href="{v["path"]}"><span class="n">{e(v["label"])}</span><span class="c">{e(v.get("blurb", ""))}</span></a>'


BASE = ("pilgrimage-tours", "12-jyotirlinga")
KIND_LABEL = {"circuit": "Yatras &amp; circuits", "temple": "Temple guides", "guide": "Planning guides", "yatra": "Seasonal yatras"}


def children(kind=None, exclude=()):
    items = [(k, v) for k, v in LIVE.items() if k != "pilgrimage-tours" and k not in exclude and (kind is None or v.get("kind") == kind)]
    return sorted(items, key=lambda kv: (kv[1].get("added", ""), kv[0]), reverse=True)


def guides_block(exclude=()):
    out = []
    for kind in ("circuit", "yatra", "temple", "guide"):
        items = children(kind, exclude)
        if items:
            out.append(f'<h3 class="szp-gh">{KIND_LABEL[kind]}</h3><div class="szp-links">' + "".join(tile(v) for _, v in items) + "</div>")
    return "".join(out)


def jl_page(slug):
    """Live page for a Jyotirlinga (live.json entry with "shrine": slug), else None."""
    for k, v in LIVE.items():
        if v.get("shrine") == slug:
            return v["path"]
    return None


# ------------------------------------------------------------------------------------------------ small art for cards
def art(kind):
    g = '<defs><linearGradient id="ag" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f2c14e"/><stop offset="1" stop-color="#e8731f"/></linearGradient></defs>'
    sil, rim = "#140a1c", "rgba(242,193,78,.7)"
    shapes = {
        "shikhara": f'<circle cx="120" cy="70" r="46" fill="url(#ag)" opacity=".35"/><path d="M80 150 C80 110 95 70 112 52 L128 52 C145 70 160 110 160 150Z" fill="{sil}" stroke="{rim}" stroke-width="2"/><ellipse cx="120" cy="48" rx="14" ry="5" fill="{sil}" stroke="#f2c14e" stroke-width="2"/><circle cx="120" cy="36" r="5" fill="#f2c14e"/><rect x="50" y="150" width="140" height="10" fill="{sil}"/>',
        "devi": f'<circle cx="125" cy="62" r="40" fill="url(#ag)" opacity=".35"/><path d="M0 160 Q70 80 120 72 Q170 80 200 120 L200 160Z" fill="{sil}"/><path d="M108 74 C108 58 114 46 120 40 C126 46 132 58 132 74Z" fill="{sil}" stroke="{rim}" stroke-width="2"/><path d="M134 40 l20 6 l-20 7Z" fill="#ff8a2a"/><line x1="134" y1="40" x2="134" y2="62" stroke="#f2c14e" stroke-width="2"/>',
        "himalaya": f'<circle cx="120" cy="60" r="40" fill="url(#ag)" opacity=".3"/><path d="M0 160 L60 70 L95 110 L135 40 L200 130 L200 160Z" fill="#26325c"/><path d="M135 40 L150 66 L135 60 L122 64Z" fill="#fff"/><path d="M90 160 L90 128 L120 110 L150 128 L150 160Z" fill="{sil}" stroke="{rim}" stroke-width="2"/>',
        "cave": f'<path d="M0 160 L40 80 L90 110 L140 30 L200 100 L200 160Z" fill="#26325c"/><path d="M140 30 L152 52 L140 47 L128 51Z" fill="#fff"/><path d="M110 160 Q135 105 160 160Z" fill="#0c0610"/><path d="M131 158 Q130 132 135 122 Q140 132 139 158Z" fill="#eaf4ff"/>',
        "ghats": f'<circle cx="150" cy="60" r="34" fill="#ffe7a8" opacity=".8"/>' + "".join(f'<rect x="{0}" y="{110 + i * 8}" width="200" height="8" fill="{["#2a1630", "#231129"][i % 2]}"/>' for i in range(6)) + f'<path d="M60 110 C60 86 68 66 76 58 L84 58 C92 66 100 86 100 110Z" fill="{sil}" stroke="{rim}" stroke-width="2"/><path d="M118 110 C118 92 124 78 130 72 L136 72 C142 78 148 92 148 110Z" fill="{sil}" stroke="{rim}" stroke-width="2"/>',
        "lake": f'<path d="M0 120 L50 50 L80 80 L120 20 L170 70 L200 50 L200 120Z" fill="#26325c"/><path d="M120 20 L132 40 L120 36 L108 40Z" fill="#fff"/><ellipse cx="100" cy="135" rx="90" ry="18" fill="#7fb3d5" opacity=".6"/>',
        "gopuram": "".join(f'<rect x="{100 - (60 - i * 9)}" y="{140 - i * 18}" width="{2 * (60 - i * 9)}" height="18" fill="{sil}" stroke="{rim}" stroke-width="1.5"/>' for i in range(6)) + '<path d="M70 32 Q100 6 130 32Z" fill="#140a1c" stroke="#f2c14e" stroke-width="2"/>',
        "calendar": f'<circle cx="110" cy="85" r="62" fill="none" stroke="#f2c14e" stroke-width="3" stroke-dasharray="6 7"/><circle cx="110" cy="85" r="40" fill="url(#ag)" opacity=".3"/><path d="M110 85 L110 40 M110 85 L140 100" stroke="#f2c14e" stroke-width="4" stroke-linecap="round"/>',
    }
    return f'<svg class="art" viewBox="0 0 200 160" aria-hidden="true">{g}{shapes[kind]}</svg>'


def circuit(href, deva, title, text, meta, kind):
    return f'<a class="szp-circ" href="{href}"><span class="dv">{e(deva)}</span><span class="t">{e(title)}</span><span class="c">{text}</span><span class="m">{meta} →</span>{art(kind)}</a>'


# ------------------------------------------------------------------------------------------------ map of light (SVG, lat/lon, no borders)
LON0, LON1, LAT0, LAT1 = 67.5, 97.5, 6.5, 36.5


def mapsvg(points, w=600, h=640, label="Map of the 12 Jyotirlingas"):
    pad = 30

    def p(lat, lon):
        return pad + (lon - LON0) / (LON1 - LON0) * (w - 2 * pad), pad + (LAT1 - lat) / (LAT1 - LAT0) * (h - 2 * pad)
    grat = ""
    for lon in range(70, 98, 5):
        x, _ = p(LAT0, lon)
        grat += f'<line x1="{x:.0f}" y1="{pad}" x2="{x:.0f}" y2="{h - pad}" stroke="#f2c14e" stroke-opacity=".1"/>'
    for lat in range(10, 37, 5):
        _, y = p(lat, LON0)
        grat += f'<line x1="{pad}" y1="{y:.0f}" x2="{w - pad}" y2="{y:.0f}" stroke="#f2c14e" stroke-opacity=".1"/><text x="{pad + 4}" y="{y - 4:.0f}" font-size="11" fill="#f2c14e" fill-opacity=".45">{lat}°N</text>'
    pts = ""
    for i, pt in enumerate(points):
        x, y = p(pt["lat"], pt["lon"])
        dx = 12 if x < w - 60 else -26
        pts += (f'<g class="pt" data-i="{i}" aria-label="{e(pt["label"])}"><circle cx="{x:.1f}" cy="{y:.1f}" r="22" fill="url(#szpg)"/>'
                f'<rect x="{x - 2.5:.1f}" y="{y - 46:.1f}" width="5" height="46" fill="url(#szpp)"/><circle class="c" cx="{x:.1f}" cy="{y:.1f}" r="7"/>'
                f'<text x="{x + dx:.1f}" y="{y + 5:.1f}">{pt.get("n", i + 1)}</text></g>')
    defs = ('<defs><radialGradient id="szpg"><stop offset="0" stop-color="#ffe9a8" stop-opacity=".85"/><stop offset="1" stop-color="#ff8a2a" stop-opacity="0"/></radialGradient>'
            '<linearGradient id="szpp" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#ffd27a"/></linearGradient></defs>')
    return f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="{e(label)}">{defs}{grat}{pts}</svg>'


def map_block(points, first_card, label):
    data = [{k: pt[k] for k in ("k", "dv", "n", "m", "p", "u", "ul")} for pt in points]
    return (f'<div class="szp-map">{mapsvg([{"lat": pt["lat"], "lon": pt["lon"], "label": pt["n"], "n": pt.get("num", i + 1)} for i, pt in enumerate(points)], label=label)}'
            f'<div class="szp-mapcard" aria-live="polite">{first_card}</div>'
            f'<script type="application/json" class="szp-mapdata">{json.dumps(data, ensure_ascii=False).replace("</", "<\\/")}</script></div>')


def short_name(j):
    return j["name_en"].replace(" Jyotirlinga", "").split(" (")[0]


def deva_short(j):
    return j["name_hi"].replace(" ज्योतिर्लिंग", "").split(" (")[0].strip()


def first_sentences(t, n=2):
    parts = re.split(r"(?<=[.!?])\s+", t.strip())
    return " ".join(parts[:n])


def jl_points():
    pts = []
    for i, j in enumerate(J):
        own = jl_page(j["slug"])
        pts.append({"lat": j["lat"], "lon": j["lon"], "k": f"Jyotirlinga {i + 1} of 12", "dv": deva_short(j), "n": short_name(j),
                    "m": e(f'{j["town"]}, {j["state"]}'), "p": e(first_sentences(j["legend_summary"], 2)),
                    "u": own or "/pilgrimage-tours/12-jyotirlinga/#jl-" + j["slug"], "ul": "Read the guide" if own else "Timings &amp; how to reach"})
    return pts


def jl_first_card(pts):
    x = pts[0]
    return f'<span class="k">{x["k"]}</span><div class="dv">{x["dv"]}</div><h3>{x["n"]}</h3><div class="meta">{x["m"]}</div><p>{x["p"]}</p><p class="szp-note" style="color:rgba(247,234,214,.6)">Tap any light on the map to read its story.</p>'


# ------------------------------------------------------------------------------------------------ HUB
CAL = [  # (month, [(text, kind)]) — kind "x" = closing / ends ; verified in data/yatras.json & research notes (as of 8 Oct 2026)
    ("Jan", [("Haridwar Ardh Kumbh begins 14 Jan 2027", ""), ("Makar Sankranti snan", "")]),
    ("Feb", [("Mauni Amavasya 6 Feb, Basant Panchami 11 Feb 2027", "")]),
    ("Mar", [("Mahashivratri 6 Mar 2027 — Jyotirlinga peak day", ""), ("Kumbh Amrit Snan 6 &amp; 8 Mar", "")]),
    ("Apr", [("Chaitra Navratri from 7 Apr 2027", ""), ("Char Dham portals usually open late Apr", ""), ("Amarnath registration usually opens", "")]),
    ("May", [("Char Dham in full swing", ""), ("Hemkund Sahib usually opens", "")]),
    ("Jun", [("Kainchi Dham fair, 15 Jun", ""), ("Best Himachal Devi season (Mar–Jun)", "")]),
    ("Jul", [("Amarnath Yatra (2026: 3 Jul–28 Aug)", ""), ("Shravan — Shiva temples busiest", "")]),
    ("Aug", [("Manimahesh (2026: 25 Aug–19 Sep)", ""), ("Shravan Ashtami melas, Naina Devi &amp; Chintpurni", "")]),
    ("Sep", [("Post-monsoon Char Dham window opens", ""), ("Manimahesh ends on Radha Ashtami", "x")]),
    ("Oct", [("Sharad Navratri from 11 Oct 2026", ""), ("Badrinath closing date fixed on Dussehra, 20 Oct", "x")]),
    ("Nov", [("Kedarnath &amp; Yamunotri close around Bhai Dooj", "x"), ("Gangotri closes on Annakut", "x")]),
    ("Dec", [("Winter Char Dham: Ukhimath, Joshimath seats", ""), ("12 Jyotirlinga circuits run all winter", "")]),
]


def hub():
    jl_live = live_path("12-jyotirlinga")
    jl_href = jl_live or "#jyotirlinga"
    cd = Y["char-dham-yatra-uttarakhand"]
    am = Y["amarnath-yatra"]
    faqs = [
        ("What is a tirth yatra?",
         "A tirth yatra (तीर्थ यात्रा) is a pilgrimage to a sacred place — a tirtha, literally a \"crossing place\" between the everyday and the divine. In India it can be one temple, like Kedarnath, or a circuit such as the 12 Jyotirlingas, the Char Dham of Uttarakhand or the Devi shrines of Himachal."),
        ("Which are the 12 Jyotirlingas?",
         "Somnath (Gujarat), Mallikarjuna (Andhra Pradesh), Mahakaleshwar and Omkareshwar (Madhya Pradesh), Kedarnath (Uttarakhand), Bhimashankar (Maharashtra), Kashi Vishwanath (Uttar Pradesh), Trimbakeshwar (Maharashtra), Vaidyanath (Deoghar, Jharkhand), Nageshwar (Gujarat), Rameshwaram (Tamil Nadu) and Grishneshwar (Maharashtra). Some traditions place Vaidyanath at Parli and Nageshwar at Aundha, both in Maharashtra."),
        ("How many Shakti Peeths are in Himachal Pradesh?",
         "Five shrines are commonly called the Shakti Peeths of Himachal: Naina Devi (Bilaspur), Jwala Ji, Brajeshwari (Kangra Devi) and Chamunda (all in Kangra), and Chintpurni (Una). Jwala Ji, Brajeshwari and Naina Devi appear in the classical 51-peetha lists; Chintpurni's body-part tradition is disputed, and Chamunda is revered as a great Devi temple rather than a classical peetha."),
        ("Which nine temples make up the Nau Devi Yatra?",
         "The traditional nine are Vaishno Devi, Mansa Devi (Panchkula), Kali Mata (Kalka), Shakumbhari Devi (Saharanpur), Naina Devi, Chintpurni, Jwala Ji, Brajeshwari and Chamunda. Many packages swap Kalka and Shakumbhari for Baglamukhi (Kangra). Allow about 9 days from Delhi, or 7 days from Chandigarh."),
        ("When does the Char Dham Yatra 2026 close?",
         "The 2026 closing dates are fixed by tradition and announced by the temple committees: Badrinath's date is announced on Vijayadashami, 20 October 2026; Kedarnath and Yamunotri close on Bhai Dooj and Gangotri on Annakut (around 10–11 November 2026). We update our <a href=\"/char-dham-closing-dates-2026/\">closing-dates post</a> as soon as they are announced."),
        ("When is the Amarnath Yatra 2027?",
         "The 2027 dates have not been announced yet. The Shri Amarnathji Shrine Board usually announces them in spring and opens registration around mid-April. In 2026 the yatra ran from 3 July to 28 August (57 days). Pilgrims must be 13–70 years old, carry a compulsory health certificate and collect an RFID card."),
        ("Is registration needed for Char Dham and Vaishno Devi?",
         "Yes. Char Dham pilgrims must register on the Uttarakhand government's portal (registrationandtouristcare.uk.gov.in) or app, and Kedarnath helicopter tickets are sold only on heliyatra.irctc.co.in. Every Vaishno Devi pilgrim needs a free RFID yatra card from the Shrine Board (online.maavaishnodevi.org or the Katra counters) and must cross Banganga within 6 hours of getting it."),
        ("Can senior citizens do these yatras?",
         "Most can. The 12 Jyotirlingas, Kashi–Ayodhya–Prayagraj and the Himachal Devi temples are road-and-ropeway journeys. Kedarnath (about 16 km on foot from Gaurikund) and Vaishno Devi (about 12 km) have pony, palki, battery-car or helicopter options. Amarnath has an age limit of 70. We plan the pace, hotels near the temples and the slower days around each pilgrim."),
    ]
    jl_cards = ""
    for i, j in enumerate(J):
        own = jl_page(j["slug"])
        jl_cards += (f'<li class="szp-shrine"><span class="no">{i + 1:02d} · {e(j["state"]).upper()}</span><span class="dv">{e(deva_short(j))}</span><h3>{e(short_name(j))}</h3>'
                     f'<div class="meta">{e(j["town"])}</div><ol class="szp-beats">{"".join(f"<li>{e(b)}</li>" for b in j["story_beats"])}</ol>'
                     f'<div class="go"><a href="{own or (jl_live + "#jl-" + j["slug"] if jl_live else "#jyotirlinga")}">{"Temple guide" if own else "Timings, route &amp; story"} →</a></div></li>')
    pts = jl_points()
    devi5 = ["naina-devi-bilaspur", "jwalamukhi-jwala-ji-kangra", "chintpurni-una", "brajeshwari-kangra-devi", "chamunda-nandikeshwar-dham-kangra"]
    devi_cards = ""
    for s in devi5:
        x = S[s]
        nm = {"naina-devi-bilaspur": "Naina Devi", "jwalamukhi-jwala-ji-kangra": "Jwala Ji (Jwalamukhi)", "chintpurni-una": "Chintpurni",
              "brajeshwari-kangra-devi": "Brajeshwari (Kangra Devi)", "chamunda-nandikeshwar-dham-kangra": "Chamunda Devi"}[s]
        bp = {"naina-devi-bilaspur": "Sati's eyes, by tradition", "jwalamukhi-jwala-ji-kangra": "Sati's tongue — the eternal flames",
              "chintpurni-una": "Chhinnamasta, the Devi who ends worry", "brajeshwari-kangra-devi": "Sati's left breast, by tradition",
              "chamunda-nandikeshwar-dham-kangra": "Where the Devi slew Chanda and Munda"}[s]
        devi_cards += (f'<li class="szp-shrine"><span class="no">{e(x["district"]).upper()} · HIMACHAL</span><span class="dv">{e(x["name_hi"].split(",")[0].replace("श्री ", ""))}</span><h3>{nm}</h3>'
                       f'<div class="meta">{bp}</div><ol class="szp-beats">{"".join(f"<li>{e(b)}</li>" for b in x["story_beats"])}</ol></li>')
    nau = [("Shakumbhari Devi", "शाकुम्भरी देवी", "Behat, Saharanpur (UP)", "Day 1 · 210 km from Delhi", "Start the circuit with the Devi of greens and grain, after a stop at Bhura Dev."),
           ("Mansa Devi &amp; Kali Mata", "मनसा देवी · काली माता", "Panchkula &amp; Kalka (Haryana)", "Day 2 · 156 + 25 km", "Both temples are run by the Mansa Devi Shrine Board; summer darshan 4 am–10 pm."),
           ("Naina Devi", "नैना देवी", "Bilaspur, Himachal — our home district", "Day 3 · 110 km", "A cable car lifts you to the hilltop shrine above the Gobind Sagar lake."),
           ("Chintpurni", "चिंतपूर्णी", "Una, Himachal", "Day 4 · 112 km", "Take a darshan slip at the gate; the online Sugam Darshan saves hours in peak season."),
           ("Jwala Ji &amp; Brajeshwari", "ज्वाला जी · ब्रजेश्वरी", "Kangra, Himachal", "Day 5–6 · 31 + 36 km", "Natural flames instead of an idol at Jwala Ji; the butter-clad Devi of Kangra each Makar Sankranti."),
           ("Chamunda Devi", "चामुंडा देवी", "Kangra, Himachal", "Day 6 · 22 km", "On the Baner river below the Dhauladhar; pair it with Dharamshala and McLeod Ganj."),
           ("Vaishno Devi", "वैष्णो देवी", "Katra, J&amp;K", "Day 7–8 · 241 km + 12 km trek", "Get your free RFID card, climb to the cave and finish the yatra at Bhairon temple.")]
    nau_html = "".join(f'<li><div class="d">{d}</div><div class="t">{t}<span class="dv">{dv}</span></div><p><b>{w}.</b> {p}</p></li>' for t, dv, w, d, p in nau)
    cal_html = "".join(f'<div class="mo"><b>{m}</b>' + "".join(f'<span class="{k}">{t}</span>' for t, k in items) + "</div>" for m, items in CAL)
    watxt = "Namaste Suzu Travels, I want to plan a yatra. Which temples: ___ , from city: ___ , dates: ___ , people: ___"
    more = guides_block()
    body = f'''
<section class="szp-hero">{hero_video("pilgrimage-tours", "pilgrim-hero", "Illustrated temples of India at dusk — Kedarnath in the snows, Somnath by the sea, the ghats of Kashi and a Devi shrine on a Himachal hill")}
<div class="szp-hero-in"><span class="k">Tirth Yatra · Pilgrimage tours of India</span>
<p class="szp-tag"><span class="dv">तीर्थ यात्रा</span>Every temple has a story. Walk it with us.</p>
<p class="szp-sub">The 12 Jyotirlingas, the Shakti Peeths and Nau Devi temples of Himachal, the Char Dham, Amarnath and Kashi — with the legends behind them, this season's dates, darshan timings and an honest route plan from a Himachal travel agency.</p>
<ul class="szp-chips"><li><b>12</b> Jyotirlingas</li><li><b>5</b> Shakti Peeths in Himachal</li><li><b>9</b> Devi temples · Nau Devi</li><li><b>4</b> Dhams of Uttarakhand</li><li><b>2027</b> Kumbh &amp; yatra calendar</li></ul>
<div class="szp-btns"><a class="szp-btn gold" href="#circuits">Choose your yatra</a><a class="szp-btn ghost" href="{wa(watxt)}" target="_blank" rel="noopener">Plan on WhatsApp</a></div>
{trust()}</div></section>
{nav([("circuits", '<span class="dv">ॐ</span>All yatras'), ("jyotirlinga", "12 Jyotirlinga"), ("shakti", "Shakti Peeth"), ("naudevi", "Nau Devi"), ("chardham", "Char Dham"), ("amarnath", "Amarnath"), ("vaishno", "Vaishno Devi"), ("kashi", "Kashi–Ayodhya"), ("himachal", "Himachal yatras"), ("calendar", "Calendar"), ("faq", "FAQ")], wa(watxt))}
<section class="szp-sec" id="overview"><span class="szp-verified">Dates and timings verified {VERIFIED}</span>
<h2>Pilgrimage tours in India, planned from the Himalaya</h2>
<div class="szp-answer"><p>A <b>tirth yatra</b> is a journey to sacred places — a single temple or a whole circuit. The best known are the <b>12 Jyotirlingas</b> of Shiva, the <b>Shakti Peeths</b> of the Goddess (five of them in Himachal), the <b>Char Dham</b> of Uttarakhand, the <b>Amarnath</b> cave and <b>Vaishno Devi</b> in Jammu &amp; Kashmir, and the <b>Kashi–Ayodhya–Prayagraj</b> trail. Suzu Travels plans these yatras end to end — registration, hotels near the temples, cars, ponies or helicopters, and the slower days elders need.</p></div>
<div class="szp-stats"><div class="szp-stat"><b>12</b><span>Jyotirlingas in 7 states — Shiva as a pillar of light</span></div><div class="szp-stat"><b>51</b><span>Shakti Peeths in the most-quoted list (traditions count 18 to 108)</span></div><div class="szp-stat"><b>3,583 m</b><span>Kedarnath — the highest of the Jyotirlingas</span></div><div class="szp-stat"><b>9</b><span>Devi temples on the Nau Devi circuit, 5 in Himachal</span></div></div>
</section>
<section class="szp-sec alt" id="circuits"><span class="k">Choose your yatra</span><h2>Eight journeys of faith</h2>
<p class="lead">Each card opens the guide below — the story, the season, the route and how we plan it. Prices depend on dates, hotels and group size, so every yatra is quoted for you.</p>
<div class="szp-circuits">
{circuit(jl_href, "द्वादश ज्योतिर्लिंग", "12 Jyotirlingas", "Somnath to Rameshwaram — Shiva's twelve pillars of light.", "7 states · all year", "shikhara")}
{circuit("#shakti", "शक्तिपीठ", "Shakti Peeths of Himachal", "Naina Devi, Jwala Ji, Chintpurni, Kangra and Chamunda.", "5 shrines · 5 days", "devi")}
{circuit("#naudevi", "नौ देवी दर्शन", "Nau Devi Yatra", "Nine Devi temples from Saharanpur to Vaishno Devi.", "9 days from Delhi", "devi")}
{circuit("#chardham", "चार धाम", "Char Dham Yatra", "Yamunotri, Gangotri, Kedarnath and Badrinath.", "Apr–Nov · 10–12 days", "himalaya")}
{circuit("#amarnath", "अमरनाथ", "Amarnath Yatra", "The ice lingam in a Himalayan cave at 3,888 m.", "Jul–Aug · registration", "cave")}
{circuit("#vaishno", "वैष्णो देवी", "Vaishno Devi", "The Trikuta cave shrine above Katra.", "All year · 12 km trek", "cave")}
{circuit("#kashi", "काशी · अयोध्या", "Kashi, Ayodhya & Prayagraj", "Ganga aarti, Ram Mandir and the Sangam.", "All year · 6 days", "ghats")}
{circuit("#himachal", "देवभूमि", "Himachal yatras", "Manimahesh, Kinner Kailash, Baijnath and more.", "Seasonal · Dev Bhoomi", "lake")}
</div></section>
<section class="szp-sec dark" id="jyotirlinga"><span class="k">द्वादश ज्योतिर्लिंग · 12 Jyotirlingas</span><h2>Twelve pillars of light across India</h2>
<p class="lead">The Shiva Purana tells how Brahma and Vishnu argued over who was greater — until an endless column of light split the worlds. Neither could find its top or its base, and Shiva emerged from it. The twelve Jyotirlingas mark where that light is worshipped. Tap a light on the map to read its story.</p>
{map_block(pts, jl_first_card(pts), "Map of the 12 Jyotirlingas of India")}
<div class="szp-media">{lazy_video("12-jyotirlinga", "light-map", "Animated map: the 12 Jyotirlingas light up one by one at their true positions, with names in Hindi and English")}
<div><h3>Plan the full circuit in 18–22 days</h3><p style="color:rgba(247,234,214,.85)">The twelve temples sit in seven states. Most pilgrims group them — Gujarat (Somnath, Nageshwar), Madhya Pradesh (Mahakaleshwar, Omkareshwar), Maharashtra (Trimbakeshwar, Bhimashankar, Grishneshwar), the south (Mallikarjuna, Rameshwaram), the north (Kedarnath, Kashi Vishwanath) and the east (Vaidyanath) — and fly between the groups.</p>
<div class="szp-btns"><a class="szp-btn gold" href="{jl_href}">Open the 12 Jyotirlinga guide</a><a class="szp-btn ghost" href="{PKG["jyotirlinga"][0]}">See our 12 Jyotirlinga tour</a></div></div></div>
<ul class="szp-shrines" style="color:var(--ink)">{jl_cards}</ul></section>
<section class="szp-sec" id="shakti"><span class="k">शक्तिपीठ · Shakti Peeths</span><h2>Where Sati fell: the Shakti Peeths of Himachal</h2>
<p class="lead">When Sati gave up her body at her father Daksha's yagna, Shiva carried her through the worlds in grief. Vishnu's Sudarshan Chakra freed him — and wherever a part of her fell, a seat of the Goddess arose. Five of the most visited are a day's drive from our office in Bilaspur.</p>
<ol class="szp-story" style="background:var(--night);border-radius:22px;padding:18px">
<li><b>Daksha's yagna</b><span>Daksha invites every god but Shiva. Sati goes anyway — and is humiliated.</span></li>
<li><b>Sati's sacrifice</b><span>Unable to bear the insult to her husband, she gives up her body.</span></li>
<li><b>Shiva's tandava</b><span>Grief-struck, Shiva wanders the worlds with her body; creation trembles.</span></li>
<li><b>The Sudarshan Chakra</b><span>Vishnu's discus parts the body — each fallen part becomes a peetha.</span></li></ol>
<ul class="szp-shrines">{devi_cards}</ul>
<div class="szp-call"><p><b>Lists differ, and that's normal.</b> The most quoted list has 51 peethas; Adi Shankara's hymn names 18 great ones, and other texts count 52, 64 or 108. Vaishno Devi, for example, is not in the classical 51 but is among the most visited Devi shrines in India.</p></div>
<div class="szp-links">{pkg_link("shakti5")}</div></section>
<section class="szp-sec alt" id="naudevi"><span class="k">नौ देवी दर्शन · Nau Devi Yatra</span><h2>Nau Devi Yatra: nine Devis in nine days</h2>
<p class="lead">The folk tradition of the "seven sisters" — Vaishno Devi, Jwala Ji, Naina Devi, Chintpurni, Kangra, Chamunda and Mansa Devi — grew to nine to match the nine nights of Navratri, adding Shakumbhari and Kalka. From Chandigarh you can do seven of them in about 7 days.</p>
<ol class="szp-route">{nau_html}</ol>
<p class="szp-note">Road distances are approximate (OpenStreetMap routing) — hill roads take longer than the map says. Sharad Navratri 2026 begins on 11 October and Chaitra Navratri 2027 on 7 April: expect the biggest crowds then.</p></section>
<section class="szp-sec" id="chardham"><span class="k">चार धाम · Char Dham Yatra</span><h2>Char Dham Yatra: 2026 season and 2027 planning</h2>
<div class="szp-answer"><p>The 2026 yatra opened with <b>Yamunotri and Gangotri on 19 April</b>, <b>Kedarnath on 22 April</b> and <b>Badrinath on 23 April</b>. Closing dates follow tradition: Badrinath's is announced on <b>Vijayadashami, 20 October 2026</b>; Kedarnath and Yamunotri close on <b>Bhai Dooj</b> and Gangotri on <b>Annakut</b> (around 10–11 November). Registration on the Uttarakhand government portal is compulsory.</p></div>
<ol class="szp-steps"><li><b>Register first</b>On registrationandtouristcare.uk.gov.in or the Tourist Care Uttarakhand app — for every pilgrim, before you travel.</li>
<li><b>Go west to east</b>Yamunotri → Gangotri → Kedarnath → Badrinath; allow 10–12 days from Haridwar or Rishikesh.</li>
<li><b>Know the walks</b>About 6 km from Janki Chatti to Yamunotri and about 16 km from Gaurikund to Kedarnath; ponies, palkis and helicopters are available.</li>
<li><b>Book helicopters safely</b>Kedarnath helicopter tickets are sold only on heliyatra.irctc.co.in — avoid look-alike sites.</li></ol>
<div class="szp-links">{pkg_link("chardham")}{pkg_link("dodham")}{pkg_link("chardham-nri")}{pkg_link("chardham-dates")}</div></section>
<section class="szp-sec alt" id="amarnath"><span class="k">अमरनाथ · Amarnath Yatra</span><h2>Amarnath Yatra: what to know for 2027</h2>
<div class="szp-answer"><p>The 2026 yatra ran from <b>3 July to 28 August</b> (57 days). The <b>2027 dates are not announced yet</b> — the Shri Amarnathji Shrine Board usually announces them in spring and opens registration around mid-April. Pilgrims must be <b>13 to 70 years old</b>, carry a <b>compulsory health certificate</b> and collect an <b>RFID card</b> in Jammu or Kashmir.</p></div>
<p>According to tradition, Shiva chose this cave to tell Parvati the secret of immortality, the Amar Katha, leaving even his companions behind on the way. A pair of pigeons is said to have overheard it — and devotees still look for them at the cave. Two routes lead there: the longer, gentler <b>Pahalgam</b> route via Chandanwari, Sheshnag and Panchtarni (about 32–36 km) and the short, steep <b>Baltal</b> route (about 14 km).</p>
<div class="szp-call warn"><p><b>Helicopters:</b> in 2026 no helicopter service ran on the yatra routes because the area was a no-fly zone. Check the Shrine Board's notice for 2027 before you plan around one.</p></div>
<div class="szp-links">{pkg_link("amarnath")}</div></section>
<section class="szp-sec" id="vaishno"><span class="k">वैष्णो देवी · Vaishno Devi</span><h2>Vaishno Devi: the climb to the Trikuta cave</h2>
<p class="lead">From Katra a paved track of about 12–13 km climbs to the cave shrine at 1,585 m, where the Devi is worshipped as three natural pindis. Tradition says she meditated for nine months in the Ardhkuwari cave on the way; the yatra is completed at the Bhairon temple above.</p>
<ol class="szp-steps"><li><b>Get the free RFID card</b>Online at online.maavaishnodevi.org or at the Katra counters — cross Banganga within 6 hours of collecting it.</li>
<li><b>Choose your way up</b>Walk, pony or palki; helicopter Katra–Sanjichhat; battery car on the Tarakote side; ropeway Bhawan–Bhairon (9 am–5 pm).</li>
<li><b>Mind the aarti</b>Darshan pauses for about two hours at each aarti, before sunrise and after sunset.</li>
<li><b>Avoid peak rain</b>Spring and autumn are best; in heavy monsoon the Shrine Board can pause the track.</li></ol>
<div class="szp-links">{pkg_link("vaishno")}</div></section>
<section class="szp-sec dark" id="kashi"><span class="k">काशी · अयोध्या · प्रयागराज</span><h2>Kashi, Ayodhya and Prayagraj</h2>
<p class="lead">Three of the oldest sacred cities on one trail: Kashi Vishwanath and the Ganga aarti in Varanasi, the Ram Mandir in Ayodhya (consecrated on 22 January 2024), and the Triveni Sangam at Prayagraj.</p>
<div class="szp-cards" style="color:var(--ink)">
<div class="szp-card"><span class="dv">काशी विश्वनाथ</span><h3>Kashi Vishwanath, Varanasi</h3><p>The temple opens at 2:30 am, with the Mangala aarti from 3 am, and closes at 11 pm after the Shayan aarti. The Kashi Vishwanath Dham corridor links the temple to the Ganga.</p></div>
<div class="szp-card"><span class="dv">राम मंदिर</span><h3>Ram Mandir, Ayodhya</h3><p>Free darshan runs from about 7 am to 9 pm with a midday break; free passes are issued on the Shri Ram Janmabhoomi Teerth Kshetra website.</p></div>
<div class="szp-card"><span class="dv">त्रिवेणी संगम</span><h3>Sangam, Prayagraj</h3><p>The meeting of the Ganga, Yamuna and the unseen Saraswati. In 2027 the Magh Mela bathing days fall from January to March; Haridwar holds its Ardh Kumbh from 14 January to 20 April 2027.</p></div></div>
<div class="szp-links" style="margin-top:18px">{pkg_link("kashi")}</div></section>
<section class="szp-sec" id="himachal"><span class="k">देवभूमि · Himachal yatras</span><h2>Yatras of Dev Bhoomi Himachal</h2>
<p class="lead">Himachal is called the land of the gods. Beyond its Devi temples, it holds some of India's toughest and most beautiful Shiva pilgrimages.</p>
<div class="szp-cards">
<div class="szp-card"><span class="dv">मणिमहेश</span><h3>Manimahesh Kailash, Chamba</h3><p>A steep 13–14 km climb to a lake at 4,080 m below the sacred peak, between Janmashtami and Radha Ashtami. In 2026 it ran from 25 August to 19 September with a new online e-pass and a cap of about 5,000 pilgrims a day.</p></div>
<div class="szp-card"><span class="dv">किन्नर कैलाश</span><h3>Kinner Kailash, Kinnaur</h3><p>A hard trek from Tangling to a rock pillar said to change colour through the day. The 2026 season ran from 30 July to 10 August with a daily cap and a compulsory fitness check.</p></div>
<div class="szp-card"><span class="dv">श्रीखंड महादेव</span><h3>Shrikhand Mahadev, Kullu</h3><p>One of India's hardest pilgrimages, to a rock lingam at about 5,200 m. The 2026 yatra was suspended by the Kullu administration on safety grounds — wait for the 2027 notice.</p></div>
<div class="szp-card"><span class="dv">बैजनाथ · बिजली महादेव</span><h3>Baijnath &amp; Bijli Mahadev</h3><p>Easy, year-round Shiva temples: the 13th-century stone temple of Baijnath in Kangra, and the hilltop Bijli Mahadev above Kullu, whose lingam is said to be struck by lightning.</p></div></div></section>
<section class="szp-sec alt" id="calendar"><span class="k">Yatra calendar 2026–27</span><h2>When to go: the pilgrim's year</h2>
<p class="lead">Dates marked with a year are confirmed by official or major news sources as of {VERIFIED}. Others are the usual pattern — we confirm each one before we book.</p>
<div class="szp-cal">{cal_html}</div></section>
<section class="szp-sec" id="plan"><ol class="szp-steps"><li><b>Tell us the temples</b>One shrine or a whole circuit, your city, dates and who is travelling — elders, children, NRIs.</li>
<li><b>We plan the yatra</b>Registrations, darshan passes where they exist, hotels close to the temples, cars, ponies or helicopters.</li>
<li><b>One quote, no surprises</b>Every yatra is priced for your dates and group, with what's included written down.</li>
<li><b>On the road with you</b>A WhatsApp line to our Himachal office for the whole journey.</li></ol>
{quote_block("Plan your tirth yatra with Suzu", "Suzu Travels is an HP Tourism-registered travel agent based in Bilaspur, Himachal Pradesh — the home district of Naina Devi. Tell us which temples you want to visit and we'll plan the route, the stays and the pace around you.", watxt)}</section>
<section class="szp-sec alt" id="faq"><span class="k">FAQ</span><h2>Questions pilgrims ask us</h2>{faq(faqs)}</section>
<section class="szp-sec" id="more"><h2>Keep exploring</h2>{more}<h3 class="szp-gh">Bookable yatras on Suzu Travels</h3><div class="szp-links">{"".join(pkg_link(k) for k in ("jyotirlinga", "shakti5", "chardham", "dodham", "amarnath", "vaishno", "kashi", "chardham-archive"))}</div>
<h3 class="szp-gh">Sources</h3>{sources(SRC_HUB)}
<p class="szp-note">Legends are retold in our own words as traditions, not historical claims. Illustrations and animations are original artwork by Suzu Travels and show stylised temples, not exact likenesses.</p></section>'''
    schema = ld(
        {"@type": "CollectionPage", "@id": "https://suzutravels.com" + HUB + "#page", "name": "Pilgrimage Tours in India: Tirth Yatra Guide & Packages", "url": "https://suzutravels.com" + HUB,
         "dateModified": "2026-10-08", "inLanguage": "en-IN",
         "about": [{"@type": "HinduTemple", "name": short_name(j) + " Jyotirlinga", "address": {"@type": "PostalAddress", "addressLocality": j["town"], "addressRegion": j["state"], "addressCountry": "IN"}} for j in J],
         "publisher": {"@type": "TravelAgency", "name": "Suzu Travels", "url": "https://suzutravels.com/", "telephone": "+91-7087488961"}},
        {"@type": "ItemList", "name": "The 12 Jyotirlingas of India", "numberOfItems": 12,
         "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": f"{short_name(j)} ({j['state']})"} for i, j in enumerate(J)]},
        faq_ld(faqs))
    return page(body + schema)


SRC_HUB = [
    ("Shri Somnath Trust — FAQ and darshan", "https://somnath.org/faq/"),
    ("Uttarakhand Tourism — Char Dham registration portal", "https://registrationandtouristcare.uk.gov.in/"),
    ("IRCTC HeliYatra — the only official Kedarnath helicopter booking", "https://heliyatra.irctc.co.in/"),
    ("Shri Badrinath–Shri Kedarnath Temple Committee", "https://badrinath-kedarnath.gov.in/"),
    ("Shri Amarnathji Shrine Board", "https://jksasb.nic.in/"),
    ("Shri Mata Vaishno Devi Shrine Board — online services", "https://online.maavaishnodevi.org/"),
    ("Shri Mata Mansa Devi Shrine Board", "https://mansadevi.org.in/"),
    ("HP Kangra district — Kangra pilgrimage", "https://hpkangra.nic.in/kangra-pilgrimage/"),
    ("Incredible India — Shree Naina Devi Temple", "https://www.incredibleindia.gov.in/en/himachal-pradesh/bilaspur/shree-naina-devi-temple"),
    ("Manimahesh Yatra — HP government registration", "https://manimaheshyatra.hp.gov.in/"),
    ("Shri Ram Janmabhoomi Teerth Kshetra", "https://srjbtkshetra.org/"),
    ("Shri Kashi Vishwanath Temple Trust", "https://shrikashivishwanath.org/"),
    ("Wikipedia — Jyotirlinga", "https://en.wikipedia.org/wiki/Jyotirlinga"),
    ("Wikipedia — Shakta pithas", "https://en.wikipedia.org/wiki/Shakta_pithas"),
    ("Wikipedia — Saat Behna (seven sister goddesses)", "https://en.wikipedia.org/wiki/Saat_Behna_(seven_sister_goddesses)"),
]


# ------------------------------------------------------------------------------------------------ 12 JYOTIRLINGA guide
def dash(v):
    return "—" if v in (None, "", [], {}) else v


JD = json.loads((KIT / "data" / "jl_display.json").read_text(encoding="utf-8"))


def hours(j):
    return JD[j["slug"]]["hours"]


def airport(j):
    return JD[j["slug"]]["air"]


def rail(j):
    return JD[j["slug"]]["rail"]


def months(j):
    return JD[j["slug"]]["best"]


def jyotirlinga_page():
    pts = jl_points()
    rows = ""
    for i, j in enumerate(J):
        rows += (f'<tr id="row-{j["slug"]}" data-state="{e(j["state"])}"><td class="n">{i + 1}</td><td><b>{e(short_name(j))}</b><span class="dv">{e(deva_short(j))}</span></td>'
                 f'<td>{e(j["town"])}<br><small>{e(j["state"])}</small></td><td>{e(dash(hours(j)))}</td><td>{e(dash(airport(j)))}</td><td>{e(dash(rail(j)))}</td><td>{e(dash(months(j)))}</td></tr>')
    states = sorted({j["state"] for j in J})
    filt = '<div class="szp-filt" role="group" aria-label="State"><button type="button" data-k="state" data-v="" aria-pressed="true">All states</button>' + "".join(
        f'<button type="button" data-k="state" data-v="{e(s)}" aria-pressed="false">{e(s)}</button>' for s in states) + "</div>"
    names_rows = "".join(f"<tr><td class='n'>{i + 1}</td><td><span class='dv' style='display:inline'>{e(j['name_hi'])}</span></td><td>{e(short_name(j))} Jyotirlinga</td><td>{e(j['state'])}</td></tr>" for i, j in enumerate(J))
    details = ""
    for i, j in enumerate(J):
        dd_ = JD[j["slug"]]
        aart, os_ = dd_.get("aarti"), dd_.get("season")
        disp = ""
        if isinstance(j.get("disputes"), dict) and j["disputes"].get("note"):
            disp = f'<p class="szp-note"><b>Other traditions:</b> {e(first_sentences(j["disputes"]["note"], 2))}</p>'
        details += (f'<article class="szp-sec{" alt" if i % 2 else ""}" id="jl-{j["slug"]}"><span class="k">Jyotirlinga {i + 1} of 12 · {e(j["state"])}</span>'
                    f'<h2>{e(short_name(j))} <span class="dv" style="color:var(--saff);font-size:.8em">{e(deva_short(j))}</span></h2>'
                    f'<p class="lead">{e(j["temple_name"])} · {e(j["town"])}, {e(j["district"])} district</p>'
                    f'<p>{e(j["legend_summary"])}</p>'
                    f'<div class="szp-scroll"><table class="szp-tbl" style="min-width:520px"><tbody>'
                    f'<tr><td><b>Temple hours</b></td><td>{e(dash(hours(j)))}</td></tr>'
                    + (f'<tr><td><b>Aarti</b></td><td>{e(aart)}</td></tr>' if aart else "")
                    + (f'<tr><td><b>Season</b></td><td>{e(os_)}</td></tr>' if os_ else "")
                    + f'<tr><td><b>Best months</b></td><td>{e(dash(months(j)))}</td></tr><tr><td><b>Good to know</b></td><td>{e(dd_["tip"])}</td></tr>'
                    f'<tr><td><b>Nearest airport</b></td><td>{e(dash(airport(j)))}</td></tr><tr><td><b>Nearest railway</b></td><td>{e(dash(rail(j)))}</td></tr>'
                    + (f'<tr><td><b>Official site</b></td><td>{ext(j["official_site"], e(urllib.parse.urlparse(j["official_site"]).netloc))}</td></tr>' if j.get("official_site") else "")
                    + f'</tbody></table></div>{disp}<p class="szp-note">Timings as published by the temple or state tourism (checked {VERIFIED}); they change on festivals — confirm before you go.</p></article>')
    faqs = [
        ("What are the names of the 12 Jyotirlingas?", "Somnath, Mallikarjuna, Mahakaleshwar, Omkareshwar, Kedarnath, Bhimashankar, Kashi Vishwanath, Trimbakeshwar, Vaidyanath, Nageshwar, Rameshwaram and Grishneshwar — the order of the Shiva Purana."),
        ("Which is the first Jyotirlinga?", "Somnath, at Prabhas Patan on the Gujarat coast, is traditionally counted first. Its legend tells of the Moon (Soma), cursed to fade, who regained his light by worshipping Shiva here."),
        ("Which Jyotirlinga is the highest?", "Kedarnath, at about 3,583 m in Uttarakhand's Rudraprayag district. It is open only from late April or May to around Bhai Dooj in November, and is reached by a walk of about 16 km from Gaurikund, by pony or palki, or by helicopter."),
        ("Which Jyotirlingas are in Maharashtra?", "Three by the most common list — Trimbakeshwar (Nashik), Bhimashankar (Pune district) and Grishneshwar (near Ellora). Other traditions add Parli Vaidyanath and Aundha Nagnath, which makes five."),
        ("Which Jyotirlinga is in South India?", "Mallikarjuna at Srisailam (Andhra Pradesh) and Rameshwaram (Ramanathaswamy) in Tamil Nadu. Mallikarjuna is also a Shakti Peeth, as Bhramaramba Devi."),
        ("Can I visit all 12 Jyotirlingas in 15 days?", "Only at a rush with several flights. A comfortable circuit takes 18–22 days because the temples are spread over seven states; we group them by region so you fly between groups and drive within them."),
        ("When is Mahashivratri 2027?", "Saturday, 6 March 2027 — the busiest day at every Jyotirlinga, so book hotels and darshan passes early."),
        ("Is the Bhasma Aarti at Mahakaleshwar open to everyone?", "Yes, with an advance booking through the temple. Since June 2026 one booking per mobile number is allowed every 90 days, and the aarti begins around 4 am."),
    ]
    watxt = "Namaste Suzu Travels, I want to plan a 12 Jyotirlinga yatra. From city: ___ , dates: ___ , people: ___"
    stotra = ("सौराष्ट्रे सोमनाथं च श्रीशैले मल्लिकार्जुनम् ।<br>उज्जयिन्यां महाकालम् ओंकारम् अमलेश्वरम् ॥<br>"
              "परल्यां वैद्यनाथं च डाकिन्यां भीमशंकरम् ।<br>सेतुबन्धे तु रामेशं नागेशं दारुकावने ॥<br>"
              "वाराणस्यां तु विश्वेशं त्र्यम्बकं गौतमीतटे ।<br>हिमालये तु केदारं घुश्मेशं च शिवालये ॥")
    body = f'''
<section class="szp-hero">{hero_video("12-jyotirlinga", "hero", "Animation: a pillar of light splits earth and sky — the Shiva Purana story of the first Jyotirlinga")}
<div class="szp-hero-in"><span class="k">Pilgrimage tours · 12 Jyotirlinga</span>
<p class="szp-tag"><span class="dv">द्वादश ज्योतिर्लिंग</span>Twelve pillars of light, one yatra.</p>
<p class="szp-sub">The names and places of all 12 Jyotirlingas, an interactive map, the legend behind each temple, darshan timings, how to reach — and a realistic route for the full circuit.</p>
<ul class="szp-chips"><li><b>12</b> temples</li><li><b>7</b> states</li><li><b>3,583 m</b> Kedarnath, the highest</li><li><b>18–22</b> days for all twelve</li></ul>
<div class="szp-btns"><a class="szp-btn gold" href="#map">Open the map</a><a class="szp-btn ghost" href="{PKG["jyotirlinga"][0]}">See our 12 Jyotirlinga tour</a></div>
{trust()}</div></section>
{nav([("list", "Names &amp; places"), ("map", "Map"), ("story", "The legend"), ("route", "Route plan"), ("temples", "Temple by temple"), ("stotram", "Stotram"), ("faq", "FAQ")], wa(watxt))}
<section class="szp-sec" id="list"><span class="szp-verified">Timings checked {VERIFIED}</span>
<h2>The 12 Jyotirlingas: names, places and states</h2>
<div class="szp-answer"><p>The 12 Jyotirlingas are <b>Somnath</b> (Gujarat), <b>Mallikarjuna</b> (Andhra Pradesh), <b>Mahakaleshwar</b> and <b>Omkareshwar</b> (Madhya Pradesh), <b>Kedarnath</b> (Uttarakhand), <b>Bhimashankar</b> (Maharashtra), <b>Kashi Vishwanath</b> (Uttar Pradesh), <b>Trimbakeshwar</b> (Maharashtra), <b>Vaidyanath</b> (Jharkhand), <b>Nageshwar</b> (Gujarat), <b>Rameshwaram</b> (Tamil Nadu) and <b>Grishneshwar</b> (Maharashtra). Each marks a place where Shiva is worshipped as a pillar of light.</p></div>
<div class="szp-tools"><input class="szp-q" type="search" placeholder="Search a temple, town or state…" aria-label="Search Jyotirlingas"></div>
<div class="szp-tools">{filt}</div>
<p class="szp-note szp-count" aria-live="polite">Showing 12 of 12</p>
<div class="szp-scroll"><table class="szp-tbl szp-data"><thead><tr><th>#</th><th>Jyotirlinga</th><th>Town &amp; state</th><th>Temple hours</th><th>Nearest airport</th><th>Nearest railway</th><th>Best months</th></tr></thead><tbody>{rows}</tbody></table></div>
<h3 style="margin-top:26px">12 Jyotirling ke naam — names in Hindi</h3>
<div class="szp-scroll"><table class="szp-tbl" style="min-width:520px"><thead><tr><th>#</th><th>हिन्दी नाम</th><th>English</th><th>State</th></tr></thead><tbody>{names_rows}</tbody></table></div></section>
<section class="szp-sec dark" id="map"><span class="k">Interactive map</span><h2>Where are the 12 Jyotirlingas?</h2>
<p class="lead">Each light sits at the temple's true latitude and longitude. Tap one to read its story; the animation lights them in the Shiva Purana's order.</p>
{map_block(pts, jl_first_card(pts), "Map of the 12 Jyotirlingas of India")}
<div class="szp-media">{lazy_video("12-jyotirlinga", "light-map", "Animated map: the 12 Jyotirlingas light up one by one, with names in Hindi and English")}<div><p style="color:rgba(247,234,214,.85)">Four of the twelve are in Maharashtra and Madhya Pradesh's Malwa plateau, two on the Gujarat coast, two in the deep south, two in the north and one in the east — which is why the full yatra is planned region by region.</p></div></div></section>
<section class="szp-sec" id="story"><span class="k">The legend</span><h2>Why "pillar of light"? The story of the first Jyotirlinga</h2>
<p class="lead">The Shiva Purana tells of a quarrel at the beginning of time, between Brahma the creator and Vishnu the preserver.</p>
<ol class="szp-story" style="background:var(--night);border-radius:22px;padding:18px">
<li><b>Who is greater?</b><span>Brahma and Vishnu argue over which of them is supreme.</span></li>
<li><b>A pillar of light</b><span>An endless column of fire appears between them, splitting earth and sky.</span></li>
<li><b>No top, no end</b><span>Vishnu dives as a boar to find its base; Brahma flies up as a swan. Neither finds an end.</span></li>
<li><b>Shiva emerges</b><span>Shiva appears from the pillar — the light worshipped at the twelve Jyotirlingas.</span></li></ol>
<p>The scene is carved in temples across India as the <b>Lingodbhava</b>. Each Jyotirlinga then has its own story — the Moon's curse at Somnath, the demon Dushana at Ujjain, the Vindhya mountain at Omkareshwar, the Pandavas at Kedarnath. You'll find them temple by temple below.</p></section>
<section class="szp-sec alt" id="route"><span class="k">Route plan</span><h2>How to plan the 12 Jyotirlinga yatra</h2>
<p class="lead">The temples are spread over seven states, so pilgrims group them and fly between the groups. A comfortable pace is 18–22 days; many families split the circuit over two or three trips.</p>
<ol class="szp-route">
<li><div class="d">North · 5–7 days</div><div class="t">Kedarnath &amp; Kashi Vishwanath<span class="dv">केदारनाथ · काशी</span></div><p>Kedarnath only between late April and November (registration compulsory); Kashi all year — combine with Ayodhya and Prayagraj.</p></li>
<li><div class="d">Madhya Pradesh · 2–3 days</div><div class="t">Mahakaleshwar &amp; Omkareshwar<span class="dv">महाकाल · ओंकारेश्वर</span></div><p>Fly to Indore; Ujjain and Omkareshwar are a drive apart. Book the Bhasma Aarti well in advance.</p></li>
<li><div class="d">Maharashtra · 4–5 days</div><div class="t">Trimbakeshwar, Grishneshwar &amp; Bhimashankar<span class="dv">त्र्यंबकेश्वर · घृष्णेश्वर · भीमाशंकर</span></div><p>Nashik, Ellora and the Sahyadri forests. Add Parli Vaidyanath and Aundha Nagnath if you follow those traditions.</p></li>
<li><div class="d">Gujarat · 2–3 days</div><div class="t">Somnath &amp; Nageshwar<span class="dv">सोमनाथ · नागेश्वर</span></div><p>The Saurashtra coast, with Dwarkadhish temple next to Nageshwar.</p></li>
<li><div class="d">South · 3–4 days</div><div class="t">Mallikarjuna &amp; Rameshwaram<span class="dv">मल्लिकार्जुन · रामेश्वरम्</span></div><p>Srisailam in the Nallamala hills; Rameshwaram on Pamban island — add Madurai and Kanyakumari.</p></li>
<li><div class="d">East · 1–2 days</div><div class="t">Vaidyanath, Deoghar<span class="dv">बैद्यनाथ धाम</span></div><p>Busiest in Shravan, when kanwariyas carry Ganga water from Sultanganj.</p></li></ol>
<div class="szp-links">{pkg_link("jyotirlinga")}</div></section>
<div id="temples">{details}</div>
<section class="szp-sec dark" id="stotram"><span class="k">Dwadasha Jyotirlinga Stotram</span><h2>The verse that names all twelve</h2>
<p class="dv" style="font-size:clamp(20px,2.4vw,28px);line-height:1.7;color:var(--gold3);margin:18px 0">{stotra}</p>
<p style="color:rgba(247,234,214,.8)">Recited daily by devotees, the stotram lists the twelve in its own order: Somnath in Saurashtra, Mallikarjuna on Shrishaila, Mahakal in Ujjain, Omkareshwar (with Amaleshwar), Vaidyanath "at Parli", Bhimashankar "in Dakini", Rameshwaram at the Setu, Nageshwar in the Daruka forest, Vishwanath in Varanasi, Trimbakeshwar on the Gautami's bank, Kedar in the Himalaya and Ghushmeshwar at Shivalaya. Chanting it, tradition says, washes away the sins of seven lifetimes.</p></section>
<section class="szp-sec" id="plan">{quote_block("Plan your 12 Jyotirlinga yatra with Suzu", "We plan the circuit around you — the order, flights between regions, hotels near each temple, Bhasma Aarti and darshan bookings where they exist, and rest days for elders.", watxt, (PKG["jyotirlinga"][0], "See the 12 Jyotirlinga tour"))}</section>
<section class="szp-sec alt" id="faq"><span class="k">FAQ</span><h2>12 Jyotirlinga: questions people ask</h2>{faq(faqs)}</section>
<section class="szp-sec" id="more"><h2>More pilgrimage guides</h2>{guides_block(exclude=("12-jyotirlinga",))}<div class="szp-links"><a class="szp-link" href="{HUB}"><span class="n">All pilgrimage tours</span><span class="c">Shakti Peeths, Char Dham, Amarnath &amp; more</span></a>{pkg_link("jyotirlinga")}{pkg_link("kashi")}{pkg_link("chardham")}</div>
<h3 class="szp-gh">Sources</h3>{sources(SRC_JL)}
<p class="szp-note">Legends are retold in our own words from the Shiva Purana and temple traditions. The animations are original artwork by Suzu Travels.</p></section>'''
    faq_schema = faq_ld(faqs)
    schema = ld(
        {"@type": "Article", "@id": "https://suzutravels.com/pilgrimage-tours/12-jyotirlinga/#article", "headline": "12 Jyotirlinga: Names, Places, Map & Yatra Route",
         "inLanguage": "en-IN", "dateModified": "2026-10-08", "author": {"@type": "Organization", "name": "Suzu Travels"}, "publisher": {"@type": "TravelAgency", "name": "Suzu Travels", "url": "https://suzutravels.com/"}},
        {"@type": "ItemList", "name": "The 12 Jyotirlingas", "numberOfItems": 12, "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "item": {"@type": "HinduTemple", "name": j["temple_name"], "alternateName": j["name_hi"],
                                                               "address": {"@type": "PostalAddress", "addressLocality": j["town"], "addressRegion": j["state"], "addressCountry": "IN"},
                                                               "geo": {"@type": "GeoCoordinates", "latitude": j["lat"], "longitude": j["lon"]}}} for i, j in enumerate(J)]},
        faq_schema)
    return page(body + schema)


def _src_jl():
    seen, out = set(), []
    for j in J:
        for s in j.get("sources", [])[:2]:
            u, t = (s.get("url"), s.get("title")) if isinstance(s, dict) else (None, None)
            if u and u not in seen:
                seen.add(u)
                out.append((t or u, u))
    return out[:24]


SRC_JL = _src_jl()


# ------------------------------------------------------------------------------------------------ content pages (agents)
def content_page(slug):
    """src/pages/<slug>.json -> page. See README "Page file schema"."""
    c = json.loads((KIT / "src" / "pages" / f"{slug}.json").read_text(encoding="utf-8"))
    m = c.get("media_slug", slug)
    watxt = c.get("wa", f"Namaste Suzu Travels, I want to plan a yatra to {c['label']}. From city: ___ , dates: ___ , people: ___")
    secs, navi = [], []

    def add(id_, label, html_, cls=""):
        navi.append((id_, label))
        secs.append(f'<section class="szp-sec{(" " + cls) if cls else ""}" id="{id_}">{html_}</section>')
    ov = f'<span class="szp-verified">Checked {e(c.get("verified", VERIFIED))}</span><h2>{e(c["q"])}</h2><div class="szp-answer"><p>{c["answer"]}</p></div>'
    if c.get("facts"):
        ov += '<div class="szp-stats">' + "".join(f'<div class="szp-stat"><b>{e(a)}</b><span>{e(b)}</span></div>' for a, b in c["facts"][:4]) + "</div>"
    if c.get("intro"):
        ov += "".join(f"<p>{p}</p>" for p in c["intro"])
    add("overview", "Overview", ov)
    if c.get("story"):
        s = c["story"]
        st = f'<span class="k">The legend</span><h2>{e(s["h2"])}</h2><p class="lead">{s["lead"]}</p><ol class="szp-story">' + "".join(f"<li><b>{e(t)}</b><span>{x}</span></li>" for t, x in s["beats"]) + "</ol>"
        if (KIT / "src" / "media" / f"{m}.json").exists() and "story" in json.loads((KIT / "src" / "media" / f"{m}.json").read_text(encoding="utf-8")) and MEDIA.get(m):
            st += f'<div class="szp-media">{lazy_video(m, "story", s["h2"])}<div>' + "".join(f'<p style="color:rgba(247,234,214,.85)">{p}</p>' for p in s.get("more", [])) + "</div></div>"
        else:
            st += "".join(f'<p style="color:rgba(247,234,214,.85)">{p}</p>' for p in s.get("more", []))
        add("story", "The legend", st, "dark")
    if c.get("darshan"):
        d = c["darshan"]
        rows = "".join(f"<tr><td><b>{e(a)}</b></td><td>{b}</td></tr>" for a, b in d["rows"])
        add("darshan", "Timings", f'<span class="k">Darshan &amp; aarti</span><h2>{e(d["h2"])}</h2><div class="szp-scroll"><table class="szp-tbl" style="min-width:520px"><tbody>{rows}</tbody></table></div><p class="szp-note">{d.get("note", "Timings change on festivals — confirm with the temple before you go.")}</p>', "alt")
    if c.get("dates"):
        d = c["dates"]
        rows = "".join(f"<tr><td><b>{e(a)}</b></td><td>{b}</td><td class='szp-note'>{x}</td></tr>" for a, b, x in d["rows"])
        add("dates", "Dates", f'<span class="k">Season &amp; dates</span><h2>{e(d["h2"])}</h2><div class="szp-scroll"><table class="szp-tbl"><thead><tr><th>What</th><th>Date</th><th>Status / source</th></tr></thead><tbody>{rows}</tbody></table></div>' + (f'<div class="szp-call"><p>{d["note"]}</p></div>' if d.get("note") else ""))
    if c.get("route"):
        r = c["route"]
        lis = "".join(f'<li><div class="d">{e(dd)}</div><div class="t">{e(t)}' + (f'<span class="dv">{e(dv)}</span>' if dv else "") + f'</div><p>{p}</p></li>' for dd, t, dv, p in r["stops"])
        add("route", "Route", f'<span class="k">Route</span><h2>{e(r["h2"])}</h2>' + (f'<p class="lead">{r["lead"]}</p>' if r.get("lead") else "") + f'<ol class="szp-route">{lis}</ol>' + (f'<p class="szp-note">{r["note"]}</p>' if r.get("note") else ""), "alt" if not c.get("dates") else "")
    if c.get("reach"):
        r = c["reach"]
        cards = "".join(f'<div class="szp-card"><h3>{e(a)}</h3><p>{b}</p></div>' for a, b in r["cards"])
        add("reach", "How to reach", f'<span class="k">How to reach</span><h2>{e(r["h2"])}</h2><div class="szp-cards">{cards}</div>')
    if c.get("itinerary"):
        it = c["itinerary"]
        lis = "".join(f'<li><div class="d">Day {e(dd)}</div><div class="t">{e(t)}</div><p>{p}</p></li>' for dd, t, p in it["days"])
        add("itinerary", "Itinerary", f'<span class="k">Sample itinerary</span><h2>{e(it["h2"])}</h2><ol class="szp-route">{lis}</ol><p class="szp-note">Every yatra is planned for your dates, group and pace — Price: Get Quote.</p>', "alt")
    if c.get("tips"):
        t = c["tips"]
        add("tips", "Rules &amp; tips", f'<span class="k">Before you go</span><h2>{e(t["h2"])}</h2><ol class="szp-steps">' + "".join(f"<li><b>{e(a)}</b>{b}</li>" for a, b in t["items"]) + "</ol>")
    for x in c.get("extra_sections", []):
        add(x["id"], x["label"], f'<span class="k">{e(x.get("kicker", ""))}</span><h2>{e(x["h2"])}</h2>{x["html"]}', x.get("cls", ""))
    pk = "".join(pkg_link(k) for k in c.get("packages", []) if k in PKG)
    secs.append(f'<section class="szp-sec" id="plan">{quote_block(c.get("quote_h2", "Plan this yatra with Suzu"), c.get("quote_text", "Suzu Travels is an HP Tourism-registered travel agent based in Bilaspur, Himachal Pradesh. Tell us your dates and group and we will plan the route, the stays and the pace around you."), watxt)}'
                + (f'<div class="szp-links" style="margin-top:18px">{pk}</div>' if pk else "") + "</section>")
    add("faq", "FAQ", f'<span class="k">FAQ</span><h2>{e(c.get("faq_h2", "Questions pilgrims ask"))}</h2>{faq(c["faqs"])}', "alt")
    links = "".join(tile(LIVE[s]) for s in c.get("links", []) if s in LIVE) + f'<a class="szp-link" href="{HUB}"><span class="n">All pilgrimage tours</span><span class="c">Jyotirlingas, Shakti Peeths, Char Dham &amp; more</span></a>'
    secs.append(f'<section class="szp-sec" id="more"><h2>Keep exploring</h2><div class="szp-links">{links}</div>{guides_block(exclude=(slug,))}<h3 class="szp-gh">Sources</h3>{sources([(a, b) for a, b in c["sources"]])}'
                f'<p class="szp-note">Legends are retold in our own words as traditions. Animations are original artwork by Suzu Travels.</p></section>')
    hero = (f'<section class="szp-hero">{hero_video(m, "hero", c.get("hero_alt", c["title"]))}<div class="szp-hero-in"><span class="k">{e(c["kicker"])}</span>'
            f'<p class="szp-tag"><span class="dv">{e(c["deva"])}</span>{e(c["tag"])}</p><p class="szp-sub">{c["sub"]}</p>'
            + ('<ul class="szp-chips">' + "".join(f"<li><b>{e(a)}</b> {e(b)}</li>" for a, b in c.get("chips", [])) + "</ul>" if c.get("chips") else "")
            + f'<div class="szp-btns"><a class="szp-btn gold" href="#{navi[1][0] if len(navi) > 1 else "overview"}">{e(c.get("cta1", "Read the guide"))}</a><a class="szp-btn ghost" href="{wa(watxt)}" target="_blank" rel="noopener">Plan on WhatsApp</a></div>{trust(c.get("verified"))}</div></section>')
    body = hero + nav(navi, wa(watxt)) + "".join(secs)
    graph = [{"@type": "Article", "headline": c["title"], "inLanguage": "en-IN", "dateModified": c.get("modified", "2026-10-08"),
              "author": {"@type": "Organization", "name": "Suzu Travels"}, "publisher": {"@type": "TravelAgency", "name": "Suzu Travels", "url": "https://suzutravels.com/"}}]
    if c.get("place"):
        p = c["place"]
        graph.append({"@type": p.get("type", "HinduTemple"), "name": p["name"], "alternateName": p.get("alt"),
                      "address": {"@type": "PostalAddress", "addressLocality": p["town"], "addressRegion": p["state"], "addressCountry": "IN"},
                      **({"geo": {"@type": "GeoCoordinates", "latitude": p["lat"], "longitude": p["lon"]}} if p.get("lat") else {}),
                      **({"sameAs": p["sameAs"]} if p.get("sameAs") else {})})
    if c.get("trip_name"):
        graph.append({"@type": "TouristTrip", "name": c["trip_name"], "provider": {"@type": "TravelAgency", "name": "Suzu Travels", "telephone": "+91-7087488961"}})
    graph.append(faq_ld(c["faqs"]))
    return page(body + ld(*graph))


PAGES = {"pilgrimage-tours": hub, "12-jyotirlinga": jyotirlinga_page}


def render(slug):
    fn = PAGES.get(slug)
    return fn() if fn else content_page(slug)


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    slugs = (list(PAGES) + [p.stem for p in (KIT / "src" / "pages").glob("*.json") if not p.stem.startswith("_")]) if which == "all" else [which]
    (KIT / "out").mkdir(exist_ok=True)
    for s in slugs:
        (KIT / "out" / f"{s}.html").write_text(render(s), encoding="utf-8")
        print(f"out/{s}.html")
