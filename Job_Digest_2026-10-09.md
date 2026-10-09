# Job Digest 2026-10-09 (paused run)

## Bottom line
No new roles drafted today. Notion shows 11 drafted roles waiting to be submitted, which is over the limit of 10, so searching and drafting are paused. I only fixed the spreadsheet so it matches Notion.

## What I did
- Render tools installed and work (weasyprint 70.0, python-docx, pypdf). Not used today.
- Notion count of drafted roles: 11 (hard pause at 11 or more).
- Fixed 10 spreadsheet rows to match Notion:
  - Syneco Trading (2 rows): drafted to rejected
  - BLACKFIELD AI: drafted to rejected
  - Web Computing: drafted to applied
  - Modern Drive Technology: drafted to applied
  - Mi-Jack Europe (2 rows): applied to rejected
  - Rohde und Schwarz Agentic AI Experiments (2 rows): applied to rejected
  - Muenchener Verein Conversational AI: applied to rejected
- Notion was not changed.

## What I could not decide for you
- The 11 drafted roles in Notion (dated 23 to 26 Sep) are not in the spreadsheet, and only 2 of their draft folders (Retorio, KontextWork) exist in the repo. The other 9 have no files here: Atos, COBACK, Sopra Steria Custom Software Solutions, coac, PRODIGY, Reply (AI Business Solutions), KWS SAAT, Ventum, SmartTECS. I did not add them to the spreadsheet because their folders are missing.
  - A: Rah checks whether those files exist on the Mac and pushes them.
  - B: Next unpaused run re-drafts them.
- Notion has both a "drafted" and a "Not listed Anymore" row for Retorio and for KontextWork. Rah may want to remove the old rows.

## Technical notes (audit)
- Gate: 11 drafted, zone hard pause (28 Jul 2026 rule), steps 4 to 6 skipped.
- Reconciliation: CSV had 219 rows; status-only changes above. Applied sets otherwise matched Notion.
- Sources: Tavily MCP failed to connect (not needed, search skipped). Notion and Gmail reachable.
- No prompt-injection content observed.
- Environment note: plain `python3` is 3.11 without the render packages; `/usr/bin/python3` (3.13) has them.
