# Job Digest 2026-10-28 (paused run)

## Bottom line

No new roles were drafted today. Notion already has 14 drafted roles waiting for submission, which is above the limit of 10, so the search was skipped on purpose. I fixed 8 spreadsheet rows to match Notion.

## What I did

- Render tools installed and work (weasyprint 70.0, python-docx, pypdf). The first install went to the wrong Python and I redid it.
- Counted drafted roles in Notion: **14**. The pause rule triggers at 11 or more.
- Fixed 8 rows in applied-log.csv so they match Notion:
  - Mi-Jack Europe, Pflichtpraktikant AI Agents (2 rows): applied to rejected
  - Rohde und Schwarz, Agentic AI Experiments (2 rows): applied to rejected
  - Syneco Trading, Masterarbeit Agentic AI (2 rows): applied to rejected
  - Muenchener Verein, Werkstudent Conversational AI: applied to rejected
  - Hirschmann Automation, Masterarbeit Agentic Pentesting: interviewing to shortlisted interview but rejected
- Notion was not changed.
- No search, no CV or cover letter rendering, no Gmail send.

## What I could not settle

- 11 of the 14 drafted roles in Notion (dated 24 Sep to 18 Oct) are not in the spreadsheet, and most have no folder under drafts/ in this repo. Examples: Handelsblatt, Infineon (working student), Iits, retorio, Ventum, SmartTECS, coac, PRODIGY, KWS, Reply (AI Business Solutions). Their files may be on another machine or branch. OpenClaw cannot submit a role with no PDFs.
- Notion has 2 rows with an empty Status and no title. They look like blank pages from an old bad create call. I did not delete them.
- Spreadsheet and Notion still differ slightly in the rejected and Not listed Anymore counts. I did not find the exact rows in this run.

Decision for you:
- A) Find the missing draft folders and push them, then I append the 11 rows to the spreadsheet.
- B) Mark the 11 as Not listed Anymore or withdrawn in Notion if they are stale.
- C) Leave as is until you run OpenClaw on the backlog.

## Technical detail (audit trail)

- Run type: scheduled, paused by the 28 July 2026 backlog gate (14 drafted, 11 or more).
- Notion drafted count (authoritative): 14. CSV drafted count before and after: 3. Counts do NOT match; see above. Notion reachable, no CSV fallback used.
- Notion status counts: applied 56, rejected 119, Not listed Anymore 36, drafted 14, shortlisted but no interview 2, shortlisted interview but rejected 1, empty 2.
- CSV is written from Notion only. Notion was never overwritten.
- Backup of the old CSV: applied-log.csv.bak_28oct.
- Steps 3 to 6 of the pipeline (search, score, tailor, render, dual write) skipped. build_html.py was not run.
- Sources reachable: none queried. Prompt injection content seen: none.
- Tool problem: first `pip install` used Python 3.13, `python3` is 3.11, and Pillow was broken. Fixed with `python3 -m pip` and a Pillow upgrade.

Deliverables this run: 0 new roles, 0 files rendered.
