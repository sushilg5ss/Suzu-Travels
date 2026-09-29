# भारत दर्शन — publishing config (the daily agent reads this every run)

Change a line here to change what the agent does; no need to touch the scheduled task.

## Channels
| Channel | Account | Status | How |
|---|---|---|---|
| Instagram Reels | @suzutravels · IG id `17841452423207372` (ad account `act_206984245998270`) | WAITING — needs a public video URL route | Pipeboard `publish_instagram_media` (media_type REELS, share_to_feed true, cover_url) |
| Facebook Page | Suzu Travels · page id `102371355018489` | WAITING — same public URL route | Pipeboard `publish_facebook_page_post` (post_type VIDEO, video_title) |
| YouTube Shorts | Suzu Travels channel | WAITING — no YouTube connection yet | Postiz (`postiz` skill) once connected |

## Public video URL route
`none` — Instagram and Facebook fetch the video from a public HTTPS URL, and this workspace has no approved
place to put one yet. Options Sushil can pick (write the chosen one here):
- `github` — push each final MP4 to branch `bharat-darshan` of `sushilg5ss/suzu-travels` (media/…) and use
  `https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@bharat-darshan/media/<file>.mp4`. Needs Sushil's
  explicit OK for the agent to push to that repo.
- `postiz` — Postiz uploads the file itself and posts to Instagram + Facebook + YouTube in one go
  (needs a Postiz account + API key stored as POSTIZ_API_KEY).

## Until a route is set (current behaviour)
Make the reel, send it in the run with `SendUserFile` (video + cover + ready-to-paste caption), and log it
as `made, not posted` in `claude/bharat-darshan/episode-log.md`. Never post anywhere else.

## Posting time
Target: publish between 17:00 and 18:30 IST (Sushil's suggested 4–6 pm window).
