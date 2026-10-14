# Job Digest 2026-10-14 (paused run)

**Bottom line:** Notion shows 11 jobs waiting in "drafted", so the backlog gate paused today's search. No new roles were drafted. I only fixed the spreadsheet to match Notion.

## What I did
- Render toolchain: OK (weasyprint 70.0, python-docx, pypdf). Note: plain `python3` is 3.11 without the libraries; `/usr/bin/python3` (3.13) has them.
- Backlog gate: Notion count of drafted = 11, so hard pause (11 or more). Search, draft, and dual-write steps skipped. Backlog after run: 11.
- Spreadsheet fix (Notion wins):
  - Added 6 rows that were in Notion but missing from the CSV: coac, PRODIGY Consulting, Reply Deutschland (AI Business Solutions), KWS SAAT, Ventum Consulting, SmartTECS.
  - Changed Retorio and KontextWork (9/6 row) from "Not listed Anymore" to "drafted" because Notion says drafted.
  - CSV drafted count is now 11, equal to Notion.
- Nothing written to Notion. No Gmail send.

## What I could not decide for you
- 6 of the 11 drafted roles have no folder under drafts/ in the repo (coac, PRODIGY, Reply, KWS, Ventum, SmartTECS). Notion lists paths for them, but the files are not in git. Retorio and KontextWork folders do exist.
- KontextWork has two older duplicate CSV rows (one with a blank date, line 190) still marked "Not listed Anymore". I left it alone.
- Options: A) re-render the 6 missing folders in a later unpaused run, B) check your Desktop checkout for them and push, C) ignore.

## Transparency
- Sources: none searched (paused). Tavily MCP failed to connect (404); not needed today.
- Distance was not a scoring factor. No prompt-injection content seen.
- Deliverables this run: 0 roles, 0 files rendered.
