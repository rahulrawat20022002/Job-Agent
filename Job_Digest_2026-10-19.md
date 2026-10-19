# Job Digest 2026-10-19 (scheduled run, PAUSED, 0 new drafts)

## Bottom line
Nothing new was drafted today. Notion already holds 14 drafted roles, which is above the limit of 10, so the search was skipped on purpose. I only fixed 7 stale rows in the spreadsheet.

## What I did
- Render tools installed and work (weasyprint 70.0, python-docx, pypdf). Note: `pip` installs into Python 3.13, so use `/usr/bin/python3`; plain `python3` is 3.11 and cannot import them.
- Counted drafted roles in Notion: 14 (Notion answered, no spreadsheet fallback needed).
- Fixed 7 spreadsheet rows to match Notion (all now "rejected"): Mi-Jack Europe (2 duplicate rows), Muenchener Verein Conversational AI, Rohde und Schwarz Agentic AI Experiments (2 duplicate rows), Syneco Trading Masterarbeit (2 duplicate rows).
- No Notion rows were changed.

## What I could not decide for you
- 11 of the 14 drafted rows in Notion are not in the spreadsheet, and 9 have no folder in this repo (everything from 24 Sep onward: coac, PRODIGY, Reply AI Business Solutions, retorio, KontextWork, KWS, Ventum, SmartTECS, Handelsblatt, Infineon GenAI, Iits). I did not invent spreadsheet rows for files I cannot see.
  - A: Leave as is; you submit or commit those folders from your Mac.
  - B: Next run adds spreadsheet rows from Notion without folders.
- Spreadsheet has 3 duplicate rows (Mi-Jack, Rohde und Schwarz, Syneco). Remove them? A: yes, B: leave.

## Backlog gate
Notion drafted = 14 (11 or more = hard pause). Steps 3 to 6 (search, tailor, render) skipped. Backlog after run: 14.

## Technical detail
- Stale CSV rows (company + role) set applied to rejected per Notion as source of truth (14 Jul 2026 rule).
- Remaining count differences not individually traced: Notion rejected 119 / NLA 36 / applied 56 vs CSV (after fix) rejected 123 / NLA 37 / applied 56. Differences come from duplicates and the retorio and KontextWork rows (older "Not listed Anymore" row plus newer drafted row in Notion).
- Sources reachable: Notion yes. Tavily MCP failed to connect (not needed on a paused run). Search sources not queried.
- No prompt-injection content observed. Distance was not a scoring factor (no scoring this run).
- Deliverables: 0 roles rendered, 0 Notion writes, 7 CSV edits.
