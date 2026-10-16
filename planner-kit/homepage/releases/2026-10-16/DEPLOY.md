# Homepage hero-engine release — 16 Oct 2026 (Trip Planner agent lane, NOT deployed)

File: `index.html` → `public_html/index.html` (943,534 B, sha256 6dc089e3879af9aed091c370b29afc628745733423131f85c9e1fb96fcebfabe)
Built on LIVE homepage 63c1b336900766e5 (943,238 B). Only `<style id="tp-engine-css">` and `<script id="tp-engine-js">` changed:
hero photo zoom + snow animation pause (`#nz-hero.tpx-off`) when the hero is scrolled off-screen or the tab is hidden; resume when back.
PARITY PASS (346 links, 203 headings, JSON-LD 4). test_home.js desktop + Pixel 7: 0 errors, overlay 6 days, Esc/back/close, cab, popup, assistant, 6 slides. Pause verified (scroll 4000 px → paused, back → running).

Deploy ONLY if live is still 63c1b336… (another agent may have deployed since): write live bytes to `public_html/index-nz-previous.html`, then upload this file. Otherwise re-apply the 2 small edits on the new live bytes.
Rollback: copy `index-nz-previous.html` back to `index.html`.
