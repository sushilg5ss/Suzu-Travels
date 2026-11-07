#!/usr/bin/env python3
"""Compose a circuit page's gallery from photos already on other pages (same WordPress files, same credits).

    python3 tools/borrow_gallery.py <slug> "<h2>" "<lead>" role=src.role.n [role=src.role.n ...]

src = another page slug (its src/pages/<src>.json "gallery") or "self" (this page's own items, e.g. from tools/wp_gallery.py);
role.n = the n-th item (1-based) with that role in src. Example:
    python3 tools/borrow_gallery.py shakti-peeth-himachal "The five shrines" "..." hero=naina-devi.hero.1 fig=jwala-ji.fig.1 g=chintpurni.hero.1
"""
import json, pathlib, sys

KIT = pathlib.Path(__file__).resolve().parent.parent


def items(slug):
    return json.loads((KIT / "src" / "pages" / f"{slug}.json").read_text(encoding="utf-8")).get("gallery", {}).get("items", [])


def main():
    slug, h2, lead = sys.argv[1:4]
    own = items(slug)
    out = []
    for spec in sys.argv[4:]:
        role, src = spec.split("=", 1)
        s, r, n = src.rsplit(".", 2)
        pool = [i for i in (own if s == "self" else items(s)) if i["role"] == r]
        it = dict(pool[int(n) - 1])
        it["role"] = role
        out.append(it)
    p = KIT / "src" / "pages" / f"{slug}.json"
    c = json.loads(p.read_text(encoding="utf-8"))
    c["gallery"] = {"kicker": c.get("gallery", {}).get("kicker", "In pictures"), "h2": h2, "lead": lead, "items": out}
    p.write_text(json.dumps(c, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(slug, [f'{i["role"]}:{i["cap"][:24]}' for i in out])


if __name__ == "__main__":
    main()
