# Job Digest 2026-10-26 (paused run)

**Bottom line:** No new roles drafted today. Notion has 14 drafted roles waiting, which is above the limit of 10, so search and drafting were paused. I only fixed the spreadsheet so it matches Notion.

## What I did
- Render tools installed and working (weasyprint, python-docx, pypdf). Not used today.
- Counted drafted roles in Notion: 14 (pause starts at 11). Notion was reachable, no CSV fallback.
- Spreadsheet (applied-log.csv) fixed to match Notion:
  - Hirschmann Automation: "interviewing" changed to "shortlisted interview but rejected".
  - 7 duplicate or stale "applied" lines changed to "rejected" (Mi-Jack x2, Rohde und Schwarz Teisnach x2, Syneco Trading x2, Muenchener Verein Conversational AI x1).
  - 11 drafted roles that were in Notion but missing from the spreadsheet were added (coac, PRODIGY, Reply, retorio, KontextWork, KWS SAAT, Ventum, SmartTECS, Handelsblatt, Infineon, Iits). Spreadsheet now shows 14 drafted, same as Notion.
- Nothing written to Notion. No Notion status changed.

## What I could not decide for you
- 9 of the 14 drafted roles have no folder with CVs in this checkout (coac, PRODIGY, Reply, KWS SAAT, Ventum, SmartTECS, Handelsblatt, Infineon, Iits). Their Notion Draft Path points to folders that are not in git. They may have been rendered somewhere that never got pushed.
  - A) Leave as is, you check your local copy.
  - B) Next run re-renders them from scratch.
  - C) Mark them withdrawn in Notion.
- Handelsblatt, Infineon and Iits were drafted on 18 Oct, 8 days ago. They may be stale; the posting could be gone.

## Backlog gate
Notion drafted count 14, zone: hard pause (11 or more). Backlog after run: 14.

## Technical detail
- Reconciliation direction: Notion to CSV only. Source of truth per 14 July 2026 rule.
- CSV rows changed: lines 116, 188, 191, 196, 199, 206, 212, 217. Duplicate CSV lines for Mi-Jack, Rohde, Syneco still exist (one Notion row each); left in place, only status aligned.
- Notion has 2 blank-title rows ("New CVs now" and an empty row), not touched.
- Sources reachable: Notion only. No search sources were queried (paused). No prompt-injection content seen.
- Folder check: drafts present with 8 files for COBACK, Atos, Sopra Steria, retorio, KontextWork. Missing for the 9 listed above.
