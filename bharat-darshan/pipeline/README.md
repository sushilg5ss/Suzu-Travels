# भारत दर्शन Studio — daily reel pipeline (Suzu Travels)

Open-source, CPU-only pipeline that turns one researched story into a 60–80 s, 9:16, Hindi-narrated,
cinematic reel and publishes it. Built 29 Sep 2026; pilot = Konark Sun Temple.

## Stack (all free / open)
| Layer | Tool | Licence / note |
|---|---|---|
| Motion graphics + render | HyperFrames 0.8.91 (HTML + GSAP → MP4), headless Chrome | Apache-2.0 |
| Narration | Chatterbox Multilingual (Resemble AI), Hindi, zero-shot voice clone from `assets/narrator_ref.wav` | MIT (adds an inaudible Perth watermark) |
| Voice QA + captions | faster-whisper medium/small — every line is transcribed back; CER > 0.22 → regenerated (3 tries) | MIT |
| Fallback voice | Kokoro `hm_omega` via `hyperframes tts` | Apache-2.0 |
| Photos | Wikimedia Commons API (`commons.py`) — only CC0 / PD / CC BY / CC BY-SA kept, credits.json written | credit in caption |
| Music | Kevin MacLeod library in `assets/music/` (`catalog.json` has feel + credit line) | CC BY 4.0 — credit line MUST go in every caption/description |
| SFX + fallback score | `score.py` — synthesised taiko/dha hits, whooshes, riser, stamp, clock ticks, tanpura drone | own |
| Fonts | Tiro Devanagari Hindi (titles), Baloo 2 (captions), Cinzel (numbers/English), Sora | OFL |

Machine: 2 vCPU / 7.8 GB RAM, no GPU. Voice ≈ 15 min, render ≈ 18 min for 72 s. **Never load Chatterbox
and Whisper-medium at the same time** (OOM at ~6 GB) — `voice.py` already alternates them.

## Files
```
setup.sh      bootstrap a fresh container (npm hyperframes, browser, skills, venv, model cache)
bd.sh         step runner: voice | captions | build | snap | render | score | mix | qa | all
commons.py    photo search/download with licence filter  (python3 commons.py EP/raw "query" ... --n 5)
voice.py      narration + ASR gate      align.py  caption word timings (script words, Whisper timing)
build.py      episode.json → HyperFrames project (scene templates, captions, grain, light leaks, dust)
score.py      music bed + SFX from timing cues      mix.py  ducking + -14 LUFS + mux
topics.md     backlog + series format rules      examples/konark-episode.json  full worked example
```

## episode.json (what the agent writes each day)
- `slug`, `place`, `place_en`, `region`, `state_badge` (Hindi state name shown in the top badge), `coords`
- `lines[]`: `{id, tts, caption?, exag}` — `tts` = what is spoken (numbers in words: "बारह सौ पचास"),
  `caption` = what is shown (digits: "1250"), `exag` 0.5–0.75 (higher = more dramatic delivery).
  Short clauses with commas and "..." read best. Avoid ड़/aspirated-heavy rare words where a common word works.
- `scenes[]` → types: `hook` (big 2-line hook, optional `prop`), `title` (place name + district + coords),
  `photo` (Ken Burns, optional `stat` count-up, `label_en`), `beat` (dark push-in + one-line headline),
  `dial` (circle/spoke overlay + ticking clock — adapt for any "measurement" story), `stamp` (UNESCO-style
  stamp slam), `end` (Suzu badge, series sign-off, CTA). Shots: `img, focus[fx,fy], zoom[z0,z1], pan[dx,dy],
  at, grade(warm|dark|mono), fit(contain + width)`. Scenes accept `custom_html` + `custom_js`
  (`tl`, `S` = scene start, `D` = duration) for a one-off signature animation each day.
- `music_track` (file in assets/music), `hashtags` (max 5), `sources[]` (URLs used to verify every fact).

## Quality bar (check before publishing)
1. Every fact traceable to `sources`; legends phrased as "मान्यता है".
2. `bd.sh build` → 0 lint errors. `bd.sh snap` → look at every contact sheet frame: no text over the top
   250 px / bottom 420 px / right 180 px, no overlapping text, no captions colliding with headlines.
3. `bd.sh qa` → duration 55–90 s, integrated loudness −15…−13 LUFS, 0 black segments, ASR of the final mix
   still reads the story (music not masking voice).
4. Hook lands in the first 2 s (on-screen text + voice both start by 0.8 s).

## Publishing
- Host: push `final/<slug>.mp4` + cover to branch `bharat-darshan` of `sushilg5ss/suzu-travels` under
  `media/`, then use `https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@bharat-darshan/media/<file>`
  (served as `video/mp4`) — fall back to `https://raw.githubusercontent.com/...` if jsDelivr lags.
- Instagram @suzutravels `17841452423207372`: Pipeboard `publish_instagram_media` REELS, `cover_url`,
  `share_to_feed: true`. Facebook page Suzu Travels `102371355018489`: `publish_facebook_page_post` VIDEO.
- YouTube Shorts: through Postiz (`postiz` skill) once Sushil connects it; until then note "YouTube pending"
  in the run report and keep the file in the device folder for manual upload.
- Caption: hook line + 2–3 story lines + "📍 district, state" + soft CTA ("कोणार्क–पुरी टूर प्लान के लिए
  कमेंट करें / DM करें · +91 70874 88961") + "जुड़े रहिए भारत दर्शन के साथ 🙏" + music credit + max 5 hashtags.
