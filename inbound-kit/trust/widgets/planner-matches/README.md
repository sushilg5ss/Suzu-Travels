# planner-matches (hub 11411) — live 2026-10-27

Finishes TRUST_BACKLOG row 4 ("Next: show matching live pages + 'from' prices under the chips").
Under the region chips of the hero planner card (`#szpForm`, from `<!--szv:skin-->`) a small sand panel shows, live as chips change:
- **Matching tours on this page** — the hub's own `.lp-card` packages whose title/location line contains the region; title and
  "from US$…" are READ from the card (`h3`, `.lp-price b`), so no number is typed here. Click = smooth scroll + gold outline on the card.
  No match → "No ready-made tour for this mix yet. Send it to us and we plan it from scratch, with a US$ quote."
- **Read before you go** — up to 4 live child-page links (paths + labels from `live.json`, built by `build.py`; ' & ' → ' and').
JS off → nothing shown (planner unchanged). No storage, no fetch, no third-party code. Prefix `.szj` (checked unused on hub).
Placement: `<!--szt:planner-matches-->` right after `<!--/szv:skin-->`. Revert = replace the marked block with ''.
Rebuild: `python3 build.py` → widget.html, then wp_replace_in_page the old block. Update the map when new region pages go live.
Note: on the cached plain URL WP Rocket "Delay JS" runs it after first scroll/tap (same as the planner script).
