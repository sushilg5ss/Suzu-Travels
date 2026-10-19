#!/usr/bin/env python3
"""Queue a static-file release for the cloud deployer, then (optionally) wait for the result.

Usage (from a clone of branch deploy-static):
  python3 tools/queue_release.py --id 2026-10-20-homepage --agent "Homepage Enhancement" \
      --summary "Rohtang note + pulse dots" \
      --file index.html=/path/after.html --url index.html=https://suzutravels.com/ \
      --base index.html=<sha256 of the live file you built on> \
      --backup index.html=index-nz-previous.html \
      --push --wait 900

--file/--url/--base/--backup take TARGET=VALUE (TARGET is the path inside public_html).
--base is strongly recommended: the deploy is refused if live changed since you built.
--wait N  : after pushing, poll the result for up to N seconds and print it (exit 0 only
            when status is deployed or already_live).
"""
import argparse
import hashlib
import json
import pathlib
import shutil
import subprocess
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parent.parent


def kv(items):
    out = {}
    for s in items or []:
        k, _, v = s.partition("=")
        out[k.strip()] = v.strip()
    return out


def git(*a, check=True):
    return subprocess.run(["git", "-C", str(ROOT), *a], check=check, capture_output=True, text=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--id", required=True)
    ap.add_argument("--agent", required=True)
    ap.add_argument("--summary", default="")
    ap.add_argument("--file", action="append", required=True)
    ap.add_argument("--url", action="append", required=True)
    ap.add_argument("--base", action="append")
    ap.add_argument("--backup", action="append")
    ap.add_argument("--push", action="store_true")
    ap.add_argument("--wait", type=int, default=0)
    a = ap.parse_args()

    files, urls, bases, backs = kv(a.file), kv(a.url), kv(a.base), kv(a.backup)
    allow = [l.strip() for l in (ROOT / "tools/allowlist.txt").read_text().splitlines()
             if l.strip() and not l.startswith("#")]
    q = ROOT / "queue" / a.id
    if q.exists() or (ROOT / "done" / f"{a.id}.json").exists():
        sys.exit(f"id {a.id} already used — pick a new id")
    q.mkdir(parents=True)
    man = {"id": a.id, "agent": a.agent, "summary": a.summary, "files": []}
    for t, src in files.items():
        ok = t in allow or any(p.endswith("/**") and t.startswith(p[:-2]) for p in allow)
        if not ok:
            shutil.rmtree(q)
            sys.exit(f"{t} is not in tools/allowlist.txt")
        if t not in urls:
            shutil.rmtree(q)
            sys.exit(f"--url missing for {t}")
        name = t.replace("/", "__")
        shutil.copy(src, q / name)
        b = (q / name).read_bytes()
        man["files"].append({"target": t, "source": name, "sha256": hashlib.sha256(b).hexdigest(),
                             "base_sha256": bases.get(t) or None, "backup": backs.get(t) or None,
                             "url": urls[t], "bytes": len(b)})
    (q / "manifest.json").write_text(json.dumps(man, indent=1))
    print(json.dumps(man, indent=1))
    if not a.push:
        return
    git("add", "-A", "queue")
    git("commit", "-m", f"queue {a.id} ({a.agent})")
    for i in range(3):
        git("pull", "--rebase", "origin", "deploy-static", check=False)
        if git("push", "origin", "HEAD:deploy-static", check=False).returncode == 0:
            break
        time.sleep(10)
    else:
        sys.exit("push failed")
    print("queued + pushed")
    if not a.wait:
        return
    t0 = time.time()
    while time.time() - t0 < a.wait:
        time.sleep(30)
        git("fetch", "origin", "deploy-static", check=False)
        r = git("show", f"origin/deploy-static:done/{a.id}.json", check=False)
        if r.returncode == 0:
            res = json.loads(r.stdout)
            print("RESULT", json.dumps(res, indent=1))
            sys.exit(0 if res.get("status") in ("deployed", "already_live") else 2)
        p = git("show", f"origin/deploy-static:done/{a.id}.pending.json", check=False)
        if p.returncode == 0:
            print("still waiting:", json.loads(p.stdout).get("last_error"))
    print("RESULT not yet available (deployer may be waiting for its next hourly run)")
    sys.exit(3)


if __name__ == "__main__":
    main()
