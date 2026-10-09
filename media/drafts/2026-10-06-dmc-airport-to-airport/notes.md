# Motion Reels — 2026-10-07 (interactive catch-up session)

**Reel:** "What a local DMC does" — hook *Land in India. We do the rest.* (pillar D, topic #7, CTA DM "PLAN")
**DRAFT ONLY — not posted anywhere.**

## QA
- 1080x1920, 30 fps, **40.0 s**, **18.98 MB**, **-14.3 LUFS**, AAC 48 kHz stereo
- Music: "Vadodora" — Kevin MacLeod, CC BY 4.0 (credit in caption.txt)
- 10-frame check of the final MP4: text readable, safe zones respected, no overlaps

## Scenes
1. Taj Mahal at sunrise — "Land in India. We do the rest" (0–5 s)
2. **New timeline scene** — "One team, whole trip": Before you fly / Arrival day / Every day / Last day (5–15 s)
3. Highway + car — "Your own driver, all trip" (15–21 s)
4. Heritage haveli courtyard — "Hotels we know first-hand" (21–27 s)
5. Train in winter haze — "We fix it on the ground" + fog buffer-day tip (27–34 s)
6. End card — "India, handled by locals" + DM "PLAN" + WhatsApp/website (34–40 s)

## Animation upgrade
- `timeline` scene merged into mg.py: gold rail draws down, white dot travels it, each node pops as the dot
  arrives, the previous step dims. Lint 0 errors; looked clearly better than the `_fallback_list` panel.

## Still pending for Sushil
- **GitHub push failed** — this session is not authorised to push to sushilg5ss/Suzu-Travels. The commit
  (93d2e32) is in `suzu-motion-reels-93d2e32.bundle`. To push from a clone of branch `bharat-darshan`:
  `git pull <path>\suzu-motion-reels-93d2e32.bundle bharat-darshan` then `git push origin bharat-darshan`.
- Scheduled task still needs "Automatically approve" (or it keeps stopping at setup-motion.sh).

## Update 2026-10-09
- Synced to GitHub branch `bharat-darshan` in the 2026-10-09 interactive catch-up (laptop copies of the MP4, cover, caption, credits and these notes; spec from the Project copy). The `timeline` scene was already on GitHub via commit 3097056. The git bundle itself was not committed (it only duplicated these files).
