# Job Digest 2026-11-01 (paused run, 0 new drafts)

## Bottom line
No new jobs were drafted today. Notion shows 14 drafted jobs waiting, well over the pause limit of 11, so searching and drafting were skipped on purpose.

## What I did
- Render tools: installed fine (weasyprint 70.0, python-docx, pypdf). Note: plain `python3` here is 3.11 and cannot see them; `python3.13` can. Not needed today, but a future drafting run must use `python3.13`.
- Counted drafted rows in Notion: 14 (authoritative). Pause zone applies.
- Fixed one spreadsheet line: Hirschmann Automation (Agentic Pentesting) said "interviewing" in applied-log.csv, Notion says "shortlisted interview but rejected". Spreadsheet now matches Notion.
- Tavily search tool failed to connect this run (not needed, paused).

## Things that need your attention
- 11 of the 14 drafted jobs (dated 24 Sep to 18 Oct) are in Notion but NOT in applied-log.csv on main, and 9 of them have no drafts folder on main at all (Ventum, SmartTECS, KWS SAAT, coac, PRODIGY, Reply AI Business Solutions, Handelsblatt, Infineon, Iits). Retorio and KontextWork folders exist from older runs.
- Cause: earlier scheduled runs pushed to their own `claude/scheduled-run-*` branches and those were never merged into main (last merge to main was 13 Oct). The files probably still exist on those branches (e.g. origin/claude/scheduled-run-2026-10-18).
- I did not copy rows or files across branches, because I cannot verify them from main.
- Notion has 2 blank-status rows ("New CVs now" and an untitled row) that look like stray entries. I left them alone.
- Count gaps remain unexplained: Notion applied 56 vs CSV 63, rejected 119 vs 116, Not listed Anymore 36 vs 37. Only the shortlisted/interview/drafted rows were compared line by line; the bulk rows were not.

## Decision for you
- A) Merge the pending scheduled-run branches into main so the drafted files and CSV rows land (I can do this next run if you say so).
- B) Leave the branches as archive and only work on the 14 rows in Notion by hand.
- C) Tell me which of the 14 to mark withdrawn so drafting can restart (needs backlog under 11).

## Backlog gate
Notion drafted = 14, gate zone = hard pause (11 or more). Backlog after run: 14.

## Reconciliation
1 fix (Hirschmann status). Rows missing from CSV listed above, not copied.

## Top cut / Watchlist / Dropped
None, search skipped by the pause.

## Transparency
- Sources: none queried (paused). Tavily MCP failed to connect.
- Distance was not a scoring factor.
- No prompt-injection content seen.

## Deliverable summary
0 roles drafted, 0 files rendered, 0 Notion writes, 1 CSV edit (backup applied-log.csv.bak_01nov).
