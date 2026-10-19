#!/usr/bin/env python3
"""Suzu static-file deployer (runs inside GitHub Actions — no laptop, no Chrome).

Reads every release in queue/<id>/manifest.json, and for each one:
  1. checks the release bytes match the SHA-256 written in the manifest,
  2. fetches the LIVE file over HTTPS (cache-busted) and checks it still equals
     base_sha256 (if another agent changed it meanwhile, nothing is touched),
  3. uploads the live bytes to the one rolling backup file (if the manifest names one),
  4. uploads the release bytes over the target (Hostinger API -> File Browser TUS upload),
  5. clears the Hostinger website cache (also purges the CDN),
  6. re-fetches live until the SHA matches; if it never does, puts the old bytes back.
Result goes to done/<id>.json (status: deployed | already_live | failed | rolled_back).
Temporary problems (no token yet, site fetch blocked, API down) leave the release in
queue/ and it is retried on the next run (hourly schedule) — up to MAX_ATTEMPTS.

Only stdlib. Secrets: HOSTINGER_API_TOKEN (repo secret). Never prints the token.
"""
import datetime as dt
import hashlib
import json
import os
import pathlib
import random
import shutil
import sys
import time
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
QUEUE = ROOT / "queue"
DONE = ROOT / "done"
ALLOW = ROOT / "tools" / "allowlist.txt"
API = os.environ.get("HOSTINGER_API_BASE", "https://developers.hostinger.com")
USERNAME = os.environ.get("HOSTINGER_USERNAME", "u263844788")
DOMAIN = os.environ.get("HOSTINGER_DOMAIN", "suzutravels.com")
TOKEN = os.environ.get("HOSTINGER_API_TOKEN", "").strip()
MAX_ATTEMPTS = 6
MAX_PER_RUN = 4
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/129.0 Safari/537.36 SuzuDeployBot/1.0")


class Temporary(Exception):
    """Retry later; nothing was changed on the server."""


class Fatal(Exception):
    """Give up on this release; nothing (or only the backup copy) was changed."""


def now():
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha(b):
    return hashlib.sha256(b).hexdigest()


def log(*a):
    print(*a, flush=True)


def allowed(target):
    pats = [l.strip() for l in ALLOW.read_text().splitlines()
            if l.strip() and not l.startswith("#")]
    if ".." in target or target.startswith("/"):
        return False
    for p in pats:
        if p.endswith("/**") and target.startswith(p[:-2]):
            return True
        if target == p:
            return True
    return False


def http(method, url, data=None, headers=None, timeout=60):
    req = urllib.request.Request(url, data=data, method=method, headers=headers or {})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, dict(r.headers), r.read()
    except urllib.error.HTTPError as e:
        return e.code, dict(e.headers or {}), e.read()
    except Exception as e:  # network
        return 0, {}, str(e).encode()


def api(method, path, body=None):
    h = {"Authorization": f"Bearer {TOKEN}", "Accept": "application/json"}
    data = None
    if body is not None:
        data = json.dumps(body).encode()
        h["Content-Type"] = "application/json"
    st, _, raw = http(method, API + path, data, h)
    if st == 401:
        raise Temporary("Hostinger API token rejected (401) — check the HOSTINGER_API_TOKEN secret")
    if st == 0 or st >= 500 or st == 409 or st == 429:
        raise Temporary(f"Hostinger API {method} {path} -> {st}")
    if st >= 400:
        raise Fatal(f"Hostinger API {method} {path} -> {st}: {raw[:300]!r}")
    return json.loads(raw or b"{}")


def fetch_live(url):
    sep = "&" if "?" in url else "?"
    u = f"{url}{sep}nc={int(time.time())}{random.randint(1000, 9999)}"
    last = None
    for i in range(3):
        st, _, body = http("GET", u, headers={"User-Agent": UA, "Cache-Control": "no-cache",
                                              "Accept": "*/*"}, timeout=60)
        if st == 200:
            return body
        last = st
        time.sleep(5 * (i + 1))
    raise Temporary(f"could not fetch live {url} (HTTP {last})")


def upload(rel, data):
    """Upload bytes to public_html/<rel> via Hostinger API upload URL + TUS."""
    info = api("POST", "/api/hosting/v1/files/upload-urls",
               {"username": USERNAME, "domain": DOMAIN})
    base = info["url"].rstrip("/")
    h = {"X-Auth": info["auth_key"], "X-Auth-Rest": info["rest_auth_key"],
         "Tus-Resumable": "1.0.0"}
    target = f"{base}/{rel}?override=true"
    st, _, raw = http("POST", target, b"", {**h, "Upload-Length": str(len(data)),
                                            "Upload-Offset": "0"})
    if st not in (200, 201, 204):
        raise Temporary(f"upload create {rel} -> {st}: {raw[:200]!r}")
    st, hd, raw = http("PATCH", target, data, {**h, "Upload-Offset": "0",
                       "Content-Type": "application/offset+octet-stream"}, timeout=300)
    off = {k.lower(): v for k, v in hd.items()}.get("upload-offset")
    if st not in (200, 204) or (off is not None and int(off) != len(data)):
        raise Fatal(f"upload data {rel} -> {st}, offset {off} of {len(data)}")
    log(f"  uploaded public_html/{rel} ({len(data)} B)")


def clear_cache():
    try:
        api("DELETE", f"/api/hosting/v1/accounts/{USERNAME}/websites/{DOMAIN}/cache/clear")
        log("  cache cleared (server + CDN)")
        return True
    except Exception as e:
        log(f"  cache clear failed: {e}")
        return False


def wait_live(url, want, tries=6):
    for i in range(tries):
        time.sleep(15 if i else 5)
        try:
            if sha(fetch_live(url)) == want:
                return True
        except Temporary:
            pass
    return False


def deploy(mid, mdir, man):
    files = man.get("files") or []
    if not files:
        raise Fatal("manifest has no files")
    plan = []
    # ---- checks (no server change) ----
    for f in files:
        t = f["target"]
        if not allowed(t):
            raise Fatal(f"target {t} is not in tools/allowlist.txt")
        if f.get("backup") and not allowed(f["backup"]):
            raise Fatal(f"backup {f['backup']} is not in tools/allowlist.txt")
        src = (mdir / f["source"]).read_bytes()
        if sha(src) != f["sha256"]:
            raise Fatal(f"{f['source']} SHA {sha(src)[:12]} != manifest {f['sha256'][:12]}")
        live = fetch_live(f["url"])
        lsha = sha(live)
        if lsha == f["sha256"]:
            log(f"  {t}: already live")
            plan.append((f, src, live, "same"))
            continue
        base = f.get("base_sha256")
        if base and lsha != base:
            raise Fatal(f"{t}: live SHA {lsha[:12]} != base {base[:12]} — someone changed it; "
                        "rebuild on the new live file and queue again")
        plan.append((f, src, live, "go"))
    if all(p[3] == "same" for p in plan):
        return "already_live", {}
    if not TOKEN:
        raise Temporary("HOSTINGER_API_TOKEN secret is not set yet")
    # ---- changes ----
    done = []
    try:
        for f, src, live, mode in plan:
            if mode == "same":
                continue
            if f.get("backup"):
                upload(f["backup"], live)
            upload(f["target"], src)
            done.append((f, live))
        clear_cache()
        bad = [f["target"] for f, _ in done if not wait_live(f["url"], f["sha256"])]
        if bad:
            raise Fatal(f"live SHA did not match after upload: {bad}")
        return "deployed", {}
    except Exception as e:
        if done:
            log(f"  ROLLBACK because: {e}")
            for f, live in done:
                try:
                    upload(f["target"], live)
                except Exception as e2:
                    log(f"  rollback upload failed for {f['target']}: {e2}")
            clear_cache()
            return "rolled_back", {"error": str(e)}
        raise


def main():
    DONE.mkdir(exist_ok=True)
    items = sorted(p for p in QUEUE.iterdir() if (p / "manifest.json").exists()) if QUEUE.exists() else []
    if not items:
        log("queue empty")
        return 0
    rc = 0
    for mdir in items[:MAX_PER_RUN]:
        mid = mdir.name
        man = json.loads((mdir / "manifest.json").read_text())
        state_f = mdir / "attempts.json"
        st = json.loads(state_f.read_text()) if state_f.exists() else {"attempts": 0, "errors": []}
        st["attempts"] += 1
        log(f"== {mid} (attempt {st['attempts']}) by {man.get('agent', '?')}")
        result = {"id": mid, "agent": man.get("agent"), "summary": man.get("summary"),
                  "files": [{k: f.get(k) for k in ("target", "sha256", "base_sha256", "url")}
                            for f in man.get("files", [])],
                  "attempts": st["attempts"], "finished_at": now()}
        try:
            status, extra = deploy(mid, mdir, man)
            result.update(status=status, **extra)
        except Temporary as e:
            st["errors"].append(f"{now()} {e}")
            log(f"  temporary: {e}")
            if st["attempts"] < MAX_ATTEMPTS:
                state_f.write_text(json.dumps(st, indent=1))
                (DONE / f"{mid}.pending.json").write_text(json.dumps(
                    {**result, "status": "waiting", "last_error": str(e)}, indent=1))
                continue
            result.update(status="failed", error=f"gave up after {st['attempts']} tries: {e}")
        except Fatal as e:
            result.update(status="failed", error=str(e))
        except Exception as e:  # unexpected bug: nothing deployed unless upload ran (handled)
            result.update(status="failed", error=f"unexpected: {e!r}")
        log(f"  -> {result['status']} {result.get('error', '')}")
        (DONE / f"{mid}.json").write_text(json.dumps(result, indent=1))
        pend = DONE / f"{mid}.pending.json"
        if pend.exists():
            pend.unlink()
        # keep only the manifest (small) as a record; drop the big release bytes
        arch = DONE / "manifests" / mid
        arch.mkdir(parents=True, exist_ok=True)
        shutil.copy(mdir / "manifest.json", arch / "manifest.json")
        shutil.rmtree(mdir)
        if result["status"] in ("failed", "rolled_back"):
            rc = 1
    return rc


if __name__ == "__main__":
    sys.exit(main())
