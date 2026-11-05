# Job Digest 2026-11-05 (paused run)

## Bottom line
Search was paused. Notion shows 14 drafted roles waiting to be submitted, and the limit for pausing is 11. No new roles were drafted.

## What happened
- Render tools: installed and working (weasyprint 70.0, python-docx, pypdf). Note: `python3` here is 3.11 and only `/usr/bin/python3` can import them.
- Backlog check (Notion, authoritative): 14 rows with Status drafted (a row listing returned 13; a count query returned 14). Zone applied: 11 or more, hard pause. Steps for search, tailoring, drafting and Notion row creation were skipped.
- Tavily search server failed to connect this run (not needed because of the pause).
- Oldest waiting drafts are from 23 Sep 2026, newest from 18 Oct 2026. Several are likely stale by now.
- 10 of the 14 drafted rows have a company-portal apply method, so Rah has to submit them by hand.

## What I could not fix on my own
- Notion and applied-log.csv disagree on counts, and the CSV stops at 23 Sep 2026.
  - Notion: applied 56, rejected 119, Not listed Anymore 36, drafted 14, shortlisted but no interview 2, shortlisted interview but rejected 1, 2 rows with no status.
  - CSV: applied 63, rejected 116, Not listed Anymore 37, drafted 3, shortlisted but no interview 2, interviewing 1.
- I did not edit the CSV, because a safe row by row comparison needs the full Notion list and I only got part of it. Left untouched on purpose.

## Decision for Rah
- A) Submit or drop the 14 drafted roles so the backlog falls below 8, then search resumes automatically.
- B) Tell me to run a full CSV vs Notion sync in a separate run.
- C) Raise the pause limit (needs your explicit instruction).

## Transparency
Sources reached: Notion. Failed: Tavily. No LinkedIn, Xing, StepStone, JobTeaser, Indeed fetches (paused). No prompt injection seen. Distance was not a scoring factor. Roles drafted: 0.
