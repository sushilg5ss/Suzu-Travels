#!/usr/bin/env python3
"""Normalise the research dataset into the kit's canonical peaks.json + a public CSV.

    python3 data/build_data.py

Input : data/peaks.research.json (research agent output, 1 Oct 2026) + data/overrides.json (manual fixes, optional)
Output: data/peaks.json  (canonical, used by every page)  and  data/india-peaks.csv (public download, CC BY 4.0)
Never type a height or first-ascent year into a page by hand — add/fix it here and rebuild.
"""
import csv, json, pathlib, re, unicodedata

D = pathlib.Path(__file__).resolve().parent
STATES = [  # key, label, match words
    ("sikkim", "Sikkim", ["Sikkim"]),
    ("uttarakhand", "Uttarakhand", ["Uttarakhand"]),
    ("himachal-pradesh", "Himachal Pradesh", ["Himachal"]),
    ("jammu-kashmir", "Jammu & Kashmir", ["Jammu"]),
    ("ladakh", "Ladakh", ["Ladakh"]),
    ("arunachal-pradesh", "Arunachal Pradesh", ["Arunachal"]),
    ("west-bengal", "West Bengal", ["West Bengal"]),
]
BANDS = {"8000": "8,000 m+", "7000": "7,000–7,999 m", "6000": "6,000–6,999 m", "5000": "5,000–5,999 m", "4000": "4,000–4,999 m", "3000": "3,000–3,999 m"}
STATUS = {"climbed": "Climbed", "unclimbed": "Unclimbed", "closed": "Closed", "restricted": "Restricted"}
GRADE = {"trekking peak": "Trekking peak", "moderate": "Moderate", "technical": "Technical", "extreme": "Extreme"}


def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"\(.*?\)", "", s).lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def state_of(p):
    txt = p["state"]
    if p["name"] == "Nun":
        return "jammu-kashmir"
    if p["name"].startswith("Chiling"):
        return "ladakh"
    hits = [(txt.find(w), k) for k, _, words in STATES for w in words if w in txt]
    if not hits:
        raise SystemExit("no state for " + p["name"])
    return min(hits)[1]  # the state named first wins ("West Bengal (WB–Sikkim–Nepal border)" -> West Bengal)


def main():
    raw = json.loads((D / "peaks.research.json").read_text())
    ov = json.loads((D / "overrides.json").read_text()) if (D / "overrides.json").exists() else {}
    out = []
    for p in raw:
        p = {**p, **ov.get(p["name"], {})}
        st = state_of(p)
        out.append({
            "id": slug(p["name"]),
            "name": p["name"],
            "alt": p.get("alt_names") or [],
            "m": int(p["height_m"]),
            "ft": round(p["height_m"] * 3.28084),
            "m_alt": p.get("height_alternates_m") or [],
            "band": p["band"],
            "state": st,
            "state_label": dict((k, l) for k, l, _ in STATES)[st],
            "where": p["state"],
            "range": p["range"],
            "area": p.get("district_or_area") or "",
            "fa": p.get("first_ascent_year"),
            "fa_by": p.get("first_ascent_by") or "",
            "status": p["status"],
            "status_note": p.get("status_note") or "",
            "grade": p["difficulty"],
            "grade_note": p.get("difficulty_note") or "",
            "season": p.get("best_season") or "",
            "base": p.get("base") or "",
            "foreigners": p.get("open_to_foreigners") or "unknown",
            "rank": p.get("india_rank"),
            "notable": p.get("notable") or "",
            "sources": p.get("sources") or [],
        })
    out.sort(key=lambda r: (-r["m"], r["name"]))
    ids = [r["id"] for r in out]
    assert len(ids) == len(set(ids)), "duplicate ids"
    (D / "peaks.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    with open(D / "india-peaks.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["name", "height_m", "height_ft", "state", "location", "range", "first_ascent_year", "first_ascent_by", "status", "status_note", "grade", "best_season", "base", "notable", "sources"])
        for r in out:
            w.writerow([r["name"], r["m"], r["ft"], r["state_label"], r["where"], r["range"], r["fa"] or "", r["fa_by"], STATUS[r["status"]], r["status_note"], GRADE[r["grade"]], r["season"], r["base"], r["notable"], " ".join(r["sources"])])
    print(f"{len(out)} peaks -> peaks.json + india-peaks.csv")


if __name__ == "__main__":
    main()
