# Replacement "Deploy path" for the 3 Chrome-dependent agents

Apply AFTER the `deploy-static` branch is pushed and the `HOSTINGER_API_TOKEN` secret is set.

| Agent | Scheduled task | Where the Chrome steps live |
|---|---|---|
| Suzu Homepage Enhancement Agent (daily 23:13) | trig_01QEMWKM3jetbo3oxwF3UzEq | task prompt → section "## Deploy path" |
| Suzu Assistant Improvement Agent (Tue/Fri 15:43) | trig_01XwaWT9hrgdw3dVcMSmP1AJ | task prompt → "Build → test → deploy", step 3 |
| Suzu Trip Planner Developer (daily 11:53) | trig_01KGTVNedrM8SeDm8uYEGWpP | `planner-kit/agents/developer.md` on branch `planner` |

Replace the Claude-in-Chrome / hPanel / File Browser / `X-Auth` jwt block with:

```
## Deploy path (cloud — no laptop, no Chrome)
Deploy through the deploy-static branch of sushilg5ss/Suzu-Travels (GitHub Actions + Hostinger API):
1. git clone --depth 1 --single-branch -b deploy-static https://github.com/sushilg5ss/Suzu-Travels ~/ds
   && cd ~/ds && git config user.name "<agent name>" && git config user.email info@suzutravels.com
2. python3 tools/queue_release.py --id YYYY-MM-DD-<lane> --agent "<agent name>" --summary "<1 line>"
     --file <target>=<your built file> --url <target>=<public URL>
     --base <target>=<SHA-256 of the live bytes you built on>
     --backup <target>=<rolling undo copy> --push --wait 900
   targets/backups: homepage index.html → index-nz-previous.html ·
   assistant suzu-assistant.js → suzu-assistant-previous.js (plus index.html for the ?v= bump, backup
   index-nz-previous.html) · planner plan-your-trip/index.html → plan-your-trip/index-previous.html
3. Exit 0 = live (re-fetch live, run your live tests; if they fail, queue the previous bytes as a
   rollback release). Exit 2 = deployer refused or rolled back — read done/<id>.json, log FIX NEEDED.
   Exit 3 = queued, not live yet (e.g. token pending) — report "queued, goes live automatically";
   the next run must check done/<id>.json first and build on the LIVE file.
4. Backlog: if an earlier release in the Project (claude/<lane>/releases/<date>/DEPLOY.md) says
   "NOT deployed / Chrome" and live still equals its base SHA, queue that release first.
Never use Claude-in-Chrome or hPanel for deploys any more. Never type passwords.
```
