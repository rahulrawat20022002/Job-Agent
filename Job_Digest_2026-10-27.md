# Job Digest 2026-10-27 (paused run)

**Bottom line:** No new roles were drafted today. Notion shows 14 drafted roles waiting to be submitted, which is above the limit of 10, so the search was paused on purpose.

## What I did
- Render tools installed and work (weasyprint 70.0, python-docx, pypdf). They only import under `/usr/bin/python3`; the default `python3` is a different version and cannot see them. No render was needed today.
- Counted drafted roles in Notion: **14** (limit for a normal run is under 8; 11 or more means pause).
- Skipped search, drafting, new Notion rows and rendering.
- Fixed one spreadsheet row to match Notion: Hirschmann Automation (Belden), Masterarbeit Agentic Pentesting. Spreadsheet said "interviewing"; Notion says "shortlisted interview but rejected". Spreadsheet now matches Notion.

## What I found but did not change
- 11 of the 14 drafted roles in Notion have no row in the spreadsheet. They were drafted 24 Sep to 18 Oct: coac, PRODIGY, Reply (AI Business Solutions), retorio, KontextWork, KWS, Ventum, SmartTECS, Handelsblatt, Infineon (GenAI), Iits. Only Atos, COBACK and Sopra Steria are in both.
- Two possible duplicates in Notion: KontextWork (one drafted row, one "Not listed Anymore" row) and Retorio/retorio GmbH (same split).
- I compared the spreadsheet's drafted, shortlisted and interviewing rows against Notion. I did not check all 223 spreadsheet rows one by one.

## Decisions for Rah
- **A:** I add the 11 missing rows to the spreadsheet from Notion data.
- **B:** Leave the spreadsheet as is; Notion is the record.
- **C:** Mark the possible duplicates (KontextWork, Retorio) as "Not listed Anymore" or remove them, your call per row.

The backlog drops under 11 once some of the 14 are submitted or marked not listed anymore. Until then the daily run stays paused.

## Technical detail
- Backlog gate: Notion `Status = 'drafted'` count 14, zone: hard pause (11 or more). Notion reachable, no CSV fallback.
- Sources: Tavily MCP failed to connect this run (not needed because search was skipped). LinkedIn, Xing, StepStone, Indeed, JobTeaser not queried.
- Platform mix: none. Distance was not a scoring factor. No prompt-injection content observed.
- Deliverable summary: 0 new rows, 0 files rendered, 1 CSV status correction (line 116).
