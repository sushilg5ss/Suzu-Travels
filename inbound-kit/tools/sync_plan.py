#!/usr/bin/env python3
"""After a NEW page goes live, work out the small edits every other live page needs (links, tiles, table rows).

    python3 tools/sync_plan.py <new-slug>            (live.json must already contain <new-slug>)
    python3 tools/sync_plan.py <new-slug> --page <slug>   (only one page)
    python3 tools/sync_plan.py --rebuild <slug>      (after editing src/pages/<slug>.json or the kit: ops from the committed
                                                      out/<slug>.min.html — what is live — to a fresh build; run it BEFORE
                                                      build.py overwrites out/, then apply, verify, and build)

For every live page P (from live.json, the three base pages and <new-slug> itself included) it renders P twice with gen_pages.py — once with
live.json WITHOUT <new-slug> (= what is on the site now) and once WITH it — and diffs the two one-line builds.
Output (stdout, JSON): {"ops": [ {"page", "id", "find", "replace", "expected_count": 1}, ... ], "full": [slugs to re-upload in full]}
Apply each op IN THE ORDER GIVEN with the WordPress connector:
    wp_replace_in_page(id=<id>, find=<find>, replace=<replace>, expected_count=1)
If an op reports 0 matches (the live page was built from an older template), do not force it: put the page in LOG.md as
"FIX NEEDED: full re-upload <slug>" — the SEO & QA agent re-uploads it with tools/chunks.py.
Then check each touched page with tools/cmp_live.py <slug> (0 text/attr diffs expected).
"""
import copy, difflib, json, pathlib, re, sys

KIT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(KIT))
import build  # noqa: E402
import gen_pages as G  # noqa: E402

MAX_OPS, MAX_CHARS = 16, 40000


def tokens(s):
    """Tags stay whole; long text runs (CSS, JSON-LD, paragraphs) are split into words so edits stay small."""
    out = []
    for t in re.findall(r"<[^>]*>|[^<]+", s):
        out.extend(re.findall(r"\S+\s*|\s+", t) if (len(t) > 200 and not t.startswith("<")) else [t])
    return out


def render(slug, live):
    G.LIVE.clear()
    G.LIVE.update(live)
    if slug not in G.PAGES and not (G.KIT / "src" / "pages" / f"{slug}.json").exists():
        raise SystemExit(f"no generator for '{slug}' (base page function or src/pages/{slug}.json)")
    return build.assemble(G.render(slug), slug)


def plan(a, b):
    """Return [(find, replace), ...] that turns a into b when applied in order; each find is unique when it is applied."""
    ta, tb = tokens(a), tokens(b)
    sm = difflib.SequenceMatcher(None, ta, tb, autojunk=False)
    regions = [(i1, i2, j1, j2) for op, i1, i2, j1, j2 in sm.get_opcodes() if op != "equal"]
    merged = []
    for r in regions:  # merge changes that sit close together
        if merged and r[0] - merged[-1][1] < 8:
            m = merged[-1]
            merged[-1] = (m[0], r[1], m[2], r[3])
        else:
            merged.append(r)
    pa, pb = [0], [0]
    for t in ta:
        pa.append(pa[-1] + len(t))
    for t in tb:
        pb.append(pb[-1] + len(t))
    cur, ops = a, []
    nxt = len(ta)  # token index where the (already applied) region to the right starts
    for i1, i2, j1, j2 in reversed(merged):  # right to left: text left of i1 is still identical to a
        for k in range(1, 80):
            l_, r_ = max(0, i1 - k), min(nxt, i2 + k)
            find = cur[pa[l_]:pa[r_]]
            if find and cur.count(find) == 1:
                repl = cur[pa[l_]:pa[i1]] + b[pb[j1]:pb[j2]] + cur[pa[i2]:pa[r_]]
                cur = cur[:pa[l_]] + repl + cur[pa[r_]:]
                ops.append((find, repl))
                break
        else:
            return None
        nxt = i1
    return ops if cur == b else None


def rebuild(slug):
    """Kit or page-file change on ONE live page: ops from the committed out/<slug>.min.html (what is live) to a fresh build."""
    live = json.loads((KIT / "live.json").read_text())
    a = (KIT / "out" / f"{slug}.min.html").read_text(encoding="utf-8")
    b = render(slug, live)
    out = {"ops": [], "full": [], "unchanged": [], "expected_bytes": len(b.encode("utf-8"))}
    if a == b:
        out["unchanged"].append(slug)
    else:
        ops = plan(a, b)
        if ops is None or len(ops) > MAX_OPS or sum(len(f) + len(r) for f, r in ops) > MAX_CHARS:
            out["full"].append(slug)
        else:
            out["ops"] = [{"page": slug, "id": live[slug]["id"], "find": f, "replace": r, "expected_count": 1} for f, r in ops]
    json.dump(out, sys.stdout, ensure_ascii=False, indent=1)
    print()


def main():
    if sys.argv[1] == "--rebuild":
        return rebuild(sys.argv[2])
    new = sys.argv[1]
    only = sys.argv[sys.argv.index("--page") + 1] if "--page" in sys.argv else None
    live = json.loads((KIT / "live.json").read_text())
    if new not in live:
        raise SystemExit(f"add '{new}' to live.json first (after it is published)")
    before = copy.deepcopy(live)
    before.pop(new)
    out = {"ops": [], "full": [], "unchanged": []}
    for slug, v in live.items():
        if only and slug != only:
            continue  # the new page itself is included too: it was built before live.json listed it, so its own
                      # self-links (e.g. its row in a peak table) need ops as well (fix 4 Oct 2026)
        a, b = render(slug, before), render(slug, live)
        if a == b:
            out["unchanged"].append(slug)
            continue
        ops = plan(a, b)
        if ops is None or len(ops) > MAX_OPS or sum(len(f) + len(r) for f, r in ops) > MAX_CHARS:
            out["full"].append(slug)
            continue
        for f, r in ops:
            out["ops"].append({"page": slug, "id": v["id"], "find": f, "replace": r, "expected_count": 1})
    G.LIVE.clear()
    G.LIVE.update(live)
    json.dump(out, sys.stdout, ensure_ascii=False, indent=1)
    print()


if __name__ == "__main__":
    main()
