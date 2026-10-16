#!/usr/bin/env python3
"""Split out/<slug>.min.html into upload chunks for the WordPress connector (a tool call carries ~30 KB safely).

    python3 tools/chunks.py <slug> [--max 30000] [--dir /tmp/pk-chunks]

Writes <dir>/<slug>.<n>.txt (split only between two tags, never inside one) and prints the upload recipe:
  1. first chunk:  wp_update_page(id, content = chunk0 + "@@MKCONT@@")      (new page: wp_create_page(... content = same))
  2. each middle chunk:  wp_replace_in_page(id, find="@@MKCONT@@", replace = chunkN + "@@MKCONT@@", expected_count=1)
  3. last chunk:   wp_replace_in_page(id, find="@@MKCONT@@", replace = chunkLast, expected_count=1)
  4. wp_get_page(id): stored content length must equal the byte size printed below; then tools/cmp_live.py <slug>.
Read each chunk file with the Read tool and paste it EXACTLY (no edits, no trailing newline) into the call.
"""
import pathlib, sys

KIT = pathlib.Path(__file__).resolve().parents[1]
MARK = "@@MKCONT@@"


def split(s, mx):
    parts, i = [], 0
    while len(s) - i > mx:
        j = s.rfind("><", i, i + mx)
        if j <= i:
            raise SystemExit("no tag boundary found — page has a text run longer than the chunk size")
        parts.append(s[i:j + 1])
        i = j + 1
    parts.append(s[i:])
    return parts


def main():
    slug = sys.argv[1]
    mx = int(sys.argv[sys.argv.index("--max") + 1]) if "--max" in sys.argv else 30000
    d = pathlib.Path(sys.argv[sys.argv.index("--dir") + 1]) if "--dir" in sys.argv else pathlib.Path("/tmp/pk-chunks")
    d.mkdir(parents=True, exist_ok=True)
    s = (KIT / "out" / f"{slug}.min.html").read_text(encoding="utf-8")
    if MARK in s:
        raise SystemExit("marker found inside the page")
    parts = split(s, mx)
    assert "".join(parts) == s
    for old in d.glob(f"{slug}.*.txt"):
        old.unlink()
    for n, p in enumerate(parts):
        (d / f"{slug}.{n}.txt").write_text(p, encoding="utf-8")
    print(f"{slug}: {len(s):,} chars, {len(s.encode('utf-8')):,} bytes -> {len(parts)} chunk(s)")
    for n, p in enumerate(parts):
        role = "FIRST (create/update + marker)" if n == 0 else ("LAST (replace marker, no new marker)" if n == len(parts) - 1 else "MIDDLE (replace marker, append marker)")
        if len(parts) == 1:
            role = "ONLY (create/update, no marker)"
        print(f"  {d}/{slug}.{n}.txt  {len(p):,} chars  {role}")
    print(f"expected stored length: {len(s.encode('utf-8')):,} bytes ({len(s):,} characters)")


if __name__ == "__main__":
    main()
