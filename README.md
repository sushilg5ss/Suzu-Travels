# deploy-static — cloud deploys for the static files on suzutravels.com

**Why:** the homepage (`public_html/index.html`), the Trip Planner (`public_html/plan-your-trip/`)
and the Suzu Assistant (`public_html/suzu-assistant.js`) are plain files on Hostinger, not WordPress.
Until 20 Oct 2026 they could only go live through hPanel File Manager in Sushil's Chrome, so every
cloud run at night ended with "Needs Sushil: Chrome closed, release ready".
Now an agent queues the release here and GitHub Actions deploys it through the **Hostinger API**
(laptop off, Chrome closed — doesn't matter).

## One-time setup (Sushil, ~3 minutes)
1. hPanel → profile → **API** (https://hpanel.hostinger.com/profile/api) → *Generate token*
   (name: `suzu-deploy`, expiry: 1 year).
2. GitHub → `sushilg5ss/Suzu-Travels` → **Settings → Secrets and variables → Actions →
   New repository secret** → Name `HOSTINGER_API_TOKEN`, value = the token.
3. Done. Releases already waiting in `queue/` deploy within the hour (hourly retry), or click
   **Actions → "Deploy static files to suzutravels.com" → Run workflow** to do it now.

## How an agent deploys (replaces the old Chrome / File Browser steps)
```bash
git clone --depth 1 --single-branch -b deploy-static https://github.com/sushilg5ss/Suzu-Travels ~/ds
cd ~/ds && git config user.name "<Agent name>" && git config user.email info@suzutravels.com
python3 tools/queue_release.py --id YYYY-MM-DD-<lane> --agent "<Agent name>" --summary "<one line>" \
  --file index.html=/path/after.html --url index.html=https://suzutravels.com/ \
  --base index.html=<SHA-256 of the live file you built on> \
  --backup index.html=index-nz-previous.html \
  --push --wait 900
```
- `--file TARGET=LOCAL` (TARGET is relative to `public_html`), one per file; `--url` = the public URL
  of that file; `--base` = SHA-256 of the live bytes you built on (deploy is refused if live changed);
  `--backup` = the ONE rolling undo copy (homepage `index-nz-previous.html`, assistant
  `suzu-assistant-previous.js`, planner `plan-your-trip/index-previous.html`).
- Exit code: `0` deployed / already live · `2` failed or rolled back (nothing broken: old bytes were
  put back) · `3` still waiting (e.g. token not set yet — it will deploy automatically later, report
  "queued, will go live automatically").
- Result file: `done/<id>.json` on this branch (`status`: deployed | already_live | rolled_back | failed).
- Only paths in `tools/allowlist.txt` can be written. Never PHP, `.htaccess`, `wp-*`.

## What the deployer does (tools/deploy.py)
SHA check of the release → fetch live (cache-busted) and compare with `base_sha256` → upload live
bytes to the backup file → upload release (Hostinger API upload URL, TUS) → clear Hostinger
cache (server + CDN) → re-fetch until the SHA matches, else put the old bytes back.
Temporary problems (token missing, site/API unreachable) keep the release queued and retry hourly,
max 6 tries.

Rollback by hand: queue the `*-previous` file's bytes as a new release for the main target.
