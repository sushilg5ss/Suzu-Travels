#!/usr/bin/env python3
"""Pull a page's uploaded photos from the WordPress media library into src/pages/<slug>.json -> "gallery".

    python3 tools/wp_gallery.py <slug> "<h2>" "<lead html>" [--titles titles.json]

Photos are uploaded as suzu-<slug>-<role>-<n>.<ext> (role = hero | fig | g | bg), alt text set, caption
"<cap> — Photo: <author>, <licence> (Wikimedia Commons)" and description = JSON {file, by, lic, licurl, role, slug, cap}.
Only CC BY / CC BY-SA / CC0 / public-domain files are allowed (README §6b). The page credits each photo next to it and
in "Photo credits" at the bottom.
"""
import html, json, pathlib, re, sys, urllib.parse, urllib.request

KIT = pathlib.Path(__file__).resolve().parent.parent
OVR = {}
OK_LIC = re.compile(r"^(CC BY(-SA)? [0-9.]+|CC0|Public domain)$", re.I)


def clean_by(by):
    by = re.sub(r"\s+", " ", by).strip()
    if len(by) <= 60:
        return by
    m = re.search(r"(?:taken|photographed|shot|uploaded) by ([A-Z][a-z'-]+(?: [A-Z]\.)*(?: [A-Z][a-z'-]+){0,3})", by)
    if m:
        return m.group(1).strip().rstrip(".")
    m = re.search(r"No machine-readable author provided\. (\S+?)(?:~commonswiki)? assumed", by)
    if m:
        return m.group(1)
    return re.split(r"[;(]|\. ", by)[0][:60].strip()


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "SuzuPilgrimKit/1.0"})
    return json.loads(urllib.request.urlopen(req, timeout=40).read())


def main():
    slug, h2, lead = sys.argv[1], sys.argv[2], sys.argv[3]
    titles = {}
    if "--titles" in sys.argv:
        titles = json.loads(pathlib.Path(sys.argv[sys.argv.index("--titles") + 1]).read_text())
    global OVR
    OVR = {int(a): b for a, b in (x.split("=") for x in sys.argv[sys.argv.index("--role") + 1].split(","))} if "--role" in sys.argv else {}
    q = urllib.parse.urlencode({"search": f"suzu-{slug}-", "per_page": 50, "_fields": "id,source_url,alt_text,caption,media_details,description"})
    media = get(f"https://suzutravels.com/wp-json/wp/v2/media?{q}")
    items = []
    for m in media:
        fn = m["source_url"].rsplit("/", 1)[-1]
        mm = re.match(rf"suzu-{re.escape(slug)}-(hero|fig|g|bg|side)-(\d+)(?:-scaled)?\.", fn)
        if not mm:
            continue
        role, n = mm.group(1), int(mm.group(2))
        role = OVR.get(m["id"], role)
        cap_raw = html.unescape(re.sub(r"<[^>]+>", "", m["caption"]["rendered"])).strip()
        desc = html.unescape(re.sub(r"<[^>]+>", "", m["description"]["rendered"])).strip()
        for a, b in (("\u201c", '"'), ("\u201d", '"'), ("\u2033", '"'), ("\u2032", "'"), ("\u2019", "'"), ("\u2018", "'"), ("\u2013", "-"), ("\u2014", "—")):
            desc = desc.replace(a, b)  # wptexturize curls the JSON quotes in description.rendered
        meta = {}
        try:
            meta = json.loads(desc[desc.find("{"):desc.rfind("}") + 1]) if "{" in desc else {}
        except Exception:
            meta = {}
        cm = re.match(r"(.*?) [—-] Photo: (.*), ([^,]+) \(Wikimedia Commons\)$", cap_raw)
        cap = meta.get("cap") or (cm.group(1) if cm else cap_raw)
        by = meta.get("by") or (cm.group(2) if cm else "")
        lic = meta.get("lic") or (cm.group(3) if cm else "")
        file = meta.get("file") or titles.get(fn.rsplit(".", 1)[0], "")
        if not file:
            sys.exit(f"no Commons file URL for {fn} (pass --titles)")
        if not OK_LIC.match(lic.strip()):
            sys.exit(f"licence not allowed for {fn}: {lic}")
        md = m["media_details"]
        sz = md.get("sizes", {})
        ss = []
        for k in ("medium_large", "large", "1536x1536"):
            if k in sz:
                ss.append(f'{sz[k]["source_url"]} {sz[k]["width"]}w')
        ss.append(f'{m["source_url"]} {md["width"]}w')
        it = {"role": role, "n": n, "src": m["source_url"], "srcset": ", ".join(ss), "w": md["width"], "h": md["height"],
              "alt": m["alt_text"], "cap": cap, "by": clean_by(by), "lic": lic.strip(), "file": file,
              "thumb": sz.get("medium_large", sz.get("large", {"source_url": m["source_url"]}))["source_url"], "wp_id": m["id"]}
        items.append(it)
    items.sort(key=lambda x: x["n"])
    for it in items:
        it.pop("n")
    p = KIT / "src" / "pages" / f"{slug}.json"
    c = json.loads(p.read_text(encoding="utf-8"))
    old = c.get("gallery", {})
    c["gallery"] = {"kicker": old.get("kicker", "In pictures"), "h2": h2, "lead": lead, "items": items}
    p.write_text(json.dumps(c, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(slug, {r: sum(1 for i in items if i["role"] == r) for r in ("hero", "fig", "g", "bg", "side")})


if __name__ == "__main__":
    main()
