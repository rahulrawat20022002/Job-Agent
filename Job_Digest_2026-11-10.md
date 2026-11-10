# Job Digest 2026-11-10 (paused run)

## Bottom line
No new roles were drafted today. Notion shows 14 drafted roles waiting to be submitted, which is above the limit of 10, so searching and drafting were skipped. I only fixed the spreadsheet (applied-log.csv) so it matches Notion.

## What I did
- Render tools: installed and working (weasyprint 70.0, python-docx, pypdf). The first import failed because pip used a different Python version than python3; fixed by reinstalling for python3.
- Backlog: 14 drafted in Notion. 11 or more means hard pause. Nothing searched, scored or rendered.
- Spreadsheet fixes to match Notion (8 rows changed):
  - Hirschmann (Masterarbeit Agentic Pentesting): now "shortlisted interview but rejected".
  - Mi-Jack, Rohde und Schwarz (Agentic AI Experiments), Muenchener Verein (Conversational AI), Syneco Trading: now "rejected". Mi-Jack and Rohde und Schwarz appear twice and Syneco three times in the spreadsheet, so these are duplicate lines.
- Added 11 drafted roles to the spreadsheet that Notion had but the spreadsheet did not (coac, PRODIGY, Reply, retorio, KontextWork, KWS SAAT, Ventum, SmartTECS, Handelsblatt, Infineon, Iits).
- Result: drafted 14 in both, applied 56 in both. Rejected is 123 in the spreadsheet vs 119 in Notion and not listed anymore is 37 vs 36, because of the duplicate lines above.
- Backup of the old spreadsheet: applied-log.csv.bak_10nov.

## What I could not decide for you
- 9 of the 14 drafted roles have no folder in the repo (only retorio and KontextWork do, with 8 files each). Their Notion Draft Path points to folders that are not here. I did not regenerate them.
  - A: Leave as is, you submit from wherever the files live.
  - B: Next unpaused run re-renders the missing 9.
  - C: Mark them withdrawn in Notion.
- Retorio and KontextWork each have an older "not listed anymore" row and a newer drafted row. Both kept.
- A reconciliation check was done on the rows I could tie to a difference by counts and by name; I did not diff every one of the 229 Notion rows one by one.

## Transparency
- Sources: none searched this run (paused). Distance was not a scoring factor.
- No prompt-injection content seen.
- Deliverable summary: 0 new roles, 0 files rendered, CSV updated, no Notion writes.
