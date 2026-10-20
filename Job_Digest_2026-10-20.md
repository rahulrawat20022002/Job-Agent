# Job Digest 2026-10-20 (paused run)

## Bottom line
Nothing new was drafted today. Notion shows 14 drafted jobs waiting to be submitted, and the limit for pausing is 11. I only fixed the spreadsheet so it matches Notion.

## What I did
- Render tools installed and working (needed one extra fix for a broken image library). No CVs were rendered, since the run was paused.
- Notion says 14 jobs are still "drafted". The spreadsheet only listed 3 of them. I added the 11 missing rows to applied-log.csv. Both now show 14.
- Notion was not changed.
- Search sources: not used this run (paused). Tavily search tool also failed to connect.

## What I could not decide for you
- Backlog of 14 is over the pause limit. It will stay paused until OpenClaw or you submit or drop at least 4 of them (to get under 11) and it drops to 10 or fewer for a capped run.
  - A) Run OpenClaw on the 2 platform-native rows (retorio, KontextWork), then submit company-portal ones by hand.
  - B) Mark stale rows as withdrawn or Not listed Anymore.
  - C) Raise the pause limit.

## Details (audit trail)
- Run type: scheduled, paused under the 28 July 2026 gate (14 drafted, 11 or more = hard pause).
- Render toolchain: ok (weasyprint 70.0, python-docx, pypdf) after reinstalling pillow.
- Reconciliation: 11 CSV rows missing vs Notion, all Notion status drafted, added with Notion's dates, sources and draft paths: coac, PRODIGY Consulting, Reply Deutschland (AI Business Solutions und Agents), retorio GmbH, KontextWork GbR (reposted role, older CSV rows for the same role stay Not listed Anymore), KWS SAAT, Ventum Consulting, SmartTECS, Handelsblatt Media Group, Infineon (Working Student GenAI Agent Engineering), Iits.
- The full Notion list is paged at 100 rows; I checked every drafted row and the retorio, KontextWork and Reply rows directly. I did not diff every old rejected/applied row one by one this run.
- Drafted backlog: 14. Apply methods: 2 platform-native (retorio, KontextWork), 12 company-portal.
- Several drafted roles flag German level above B1 (coac native, Handelsblatt C1, Iits B2, Ventum, SmartTECS), for your judgement.
- Transparency: no web search done; Tavily MCP failed to connect (404). Distance not a factor.
- Deliverable summary: 0 new roles, 0 files rendered, 11 CSV rows added, 0 Notion writes.
