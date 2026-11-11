# Job Digest 2026-11-11 (paused run)

## Bottom line
No new roles drafted today. Notion still has 14 roles waiting to be submitted (limit is 10), so searching and drafting were skipped. I fixed the spreadsheet to match Notion, and found out why the same fix has been repeated every day for four weeks.

## What I did
- Render tools: installed and working (weasyprint 70.0, python-docx, pypdf). Pillow had to be reinstalled for python3 before weasyprint would import.
- Backlog: 14 drafted in Notion. 11 or more means hard pause. Nothing searched, scored or rendered.
- Spreadsheet fixes to match Notion:
  - 8 status cells changed: Hirschmann (now "shortlisted interview but rejected"); Mi-Jack (x2), Rohde und Schwarz Agentic AI Experiments (x2), Syneco Trading (x2), Muenchener Verein Conversational AI (now "rejected").
  - 12 rows added that Notion had but the spreadsheet did not: the 11 drafted roles (coac, PRODIGY, Reply, retorio, KontextWork, KWS SAAT, Ventum, SmartTECS, Handelsblatt, Infineon, Iits) plus Rohde und Schwarz Stuttgart (rejected).
  - This time I compared all 229 Notion rows one by one against the spreadsheet. After the fix, every row matches. The only leftover is a spelling difference (Ärzteverband vs Arzteverband), same job, both "applied", so I did not create a duplicate.
  - Backup of the old spreadsheet: applied-log.csv.bak_11nov.
- No Notion writes were needed.

## Why this keeps repeating
- Every daily run since 14 October pushed its fix to its own branch (claude/scheduled-run-YYYY-MM-DD), but none of those branches were ever merged into main. So each new run starts from the same old spreadsheet and redoes the same fix. There are about 87 unmerged branches on GitHub now.
- Today I am merging this run's branch into main (CLAUDE.md step 8 says to), so tomorrow's run should start clean.

## Good news: the 9 "missing" draft folders exist
Yesterday's digest said 9 of the 14 drafted roles had no files. They do exist, just on branches that were never merged:

| Roles | Branch holding the files |
|---|---|
| coac, PRODIGY, Reply Deutschland (AI Business Solutions) | claude/adoring-dijkstra-fu1v75 |
| KWS SAAT | claude/adoring-dijkstra-2hiutr |
| Ventum, SmartTECS, Rohde und Schwarz Stuttgart | claude/adoring-dijkstra-gqyx3x |
| Handelsblatt, Infineon, Iits | claude/scheduled-run-2026-10-18 |

Atos, COBACK, Sopra Steria, retorio and KontextWork already have folders on main.

## What I could not decide for you
- How to get those 9 draft folders onto main (so OpenClaw can find them after git pull):
  - A: I merge those four branches into main on the next run.
  - B: You merge them yourself on GitHub.
  - C: Leave them; you submit from the branches.
- The 14 drafted roles are 3 to 7 weeks old. Many may be closed by now. Drafting stays paused until you submit or close some of them.
  - A: Run OpenClaw on them.
  - B: Mark old ones withdrawn in Notion so drafting can restart.
- About 85 old scheduled-run branches are clutter. Delete them? (yes / no)

## Technical detail (audit trail)
- Notion data source fd974369-40b2-48c5-b660-d15256c88f52, status counts: drafted 14, applied 56, rejected 119, Not listed Anymore 36, shortlisted but no interview 2, shortlisted interview but rejected 1, blank 1 ("New CVs now" placeholder row).
- CSV after fix: drafted 14, applied 56, rejected 124, Not listed Anymore 37, shortlisted but no interview 2, shortlisted interview but rejected 1. Rejected and Not listed Anymore are higher in the CSV only because of duplicate CSV lines for the same job (Mi-Jack, Rohde und Schwarz Teisnach, Syneco).
- Hirschmann conversion row: CSV had "interviewing"; Notion says "shortlisted interview but rejected". CSV now follows Notion.
- Retorio and KontextWork each have an older "Not listed Anymore" row plus a newer "drafted" row; both kept.
- Sources searched: none (paused). Distance was not a scoring factor. No prompt injection content seen.
- Deliverables: 0 new roles, 0 files rendered, CSV updated, 0 Notion writes.
