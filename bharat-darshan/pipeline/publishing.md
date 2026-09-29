# भारत दर्शन — publishing config (the daily agent reads this every run)

Change a line here to change what the agent does; no need to touch the scheduled task.

## Public video URL route: `github` (approved by Sushil, 29 Sep 2026)
1. Attach the repo with push access: Claude_Code_Remote `add_repo` owner `sushilg5ss`, repo `Suzu-Travels`, access `push`.
2. `git clone --depth 1 --single-branch -b bharat-darshan https://github.com/sushilg5ss/Suzu-Travels ~/st`
   (the pipeline code + assets also live here under `bharat-darshan/pipeline/`).
3. Copy the final files to `media/<YYYY-MM-DD>-<slug>/` as `bharat-darshan-<slug>.mp4`, `cover.jpg`, `caption.txt`;
   also `bharat-darshan/episodes/<date>-<slug>.json`. Commit as "Suzu Bharat Darshan Agent" <info@suzutravels.com>
   and `git push` to branch `bharat-darshan` (never to any other branch).
4. Public URL = `https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@<COMMIT_SHA>/media/<folder>/<file>` —
   always the commit SHA, never the branch name (jsDelivr caches branch URLs for hours).
   Check it returns `200 video/mp4` before posting. jsDelivr refuses files over 20 MB → mix.py targets ~18.5 MB.

## Channels
| Channel | Account | Status | How |
|---|---|---|---|
| Instagram Reels | @suzutravels · IG id `17841452423207372` | ENABLED | Pipeboard `publish_instagram_media`: media_type `REELS`, `video_url` = jsDelivr SHA URL, `share_to_feed: true`, `thumb_offset` = ms of the title-card frame (≈ scene-1 start + 2 s). **Do NOT pass `cover_url`** — it made Meta fail the container (error 2207077) on 29 Sep. |
| Facebook Page | Suzu Travels · page id `102371355018489` | BLOCKED — Pipeboard gets "(#100) No permission to publish the video" | Try once per run with `publish_facebook_page_post` (VIDEO); if it still fails, skip and note it. Fix = Sushil turns on Reels auto-share to Facebook in Instagram, or reconnects Pipeboard with video-publish permission. |
| YouTube Shorts | Suzu Travels channel | WAITING — no YouTube connection | Postiz (`postiz` skill) once Sushil connects it. Until then, include the MP4 in the run delivery for manual upload. |

## Posting time
Publish between 17:00 and 18:30 IST. One reel per day. Never delete or edit earlier posts.
