# Job Digest 2026-10-22 (paused run, Cowork Agent A)

**Bottom line:** Nothing new was drafted today. Notion shows 14 drafted roles waiting, which is above the limit of 10, so search and drafting were skipped. I only fixed 8 spreadsheet rows to match Notion.

## What I did
- Render tools installed fine (weasyprint 70.0, python-docx, pypdf). Needed a Pillow upgrade first.
- Counted drafted roles in Notion: 14 (limit for any new drafting is 10).
- Fixed 8 spreadsheet (applied-log.csv) rows so they match Notion:
  - Mi-Jack Europe, Pflichtpraktikant AI Agents (2 rows): applied -> rejected
  - Rohde und Schwarz, Agentic AI Experiments (2 rows): applied -> rejected
  - Syneco Trading, Masterarbeit Agentic AI (2 rows): applied -> rejected
  - Muenchener Verein, Conversational AI: applied -> rejected
  - Hirschmann Automation (Belden): interviewing -> shortlisted interview but rejected
- Backup of the old spreadsheet: applied-log.csv.bak_22oct.

## What I could not decide for you
- 11 of the 14 drafted roles in Notion (dated 24 Sep, 25 Sep, 26 Sep, 18 Oct) are not in the spreadsheet and their draft folders are not on main. They sit on unmerged claude/ branches. I did not copy them in, to avoid conflicts with those branches.
  - A) Merge those branches into main, then I sync the spreadsheet next run.
  - B) Leave as is.
- Rohde und Schwarz, "AI Agents fuer Software Engineering" is rejected in Notion but has no spreadsheet row. Left alone.

## Technical detail
- Run type: paused (28 Jul 2026 gate, 11 or more drafted). Steps 4 to 6 skipped.
- Notion drafted list: Atos, COBACK, Sopra Steria Custom Software, coac, PRODIGY, Reply Deutschland (AI Business Solutions), retorio, KontextWork, KWS SAAT, Ventum, SmartTECS, Handelsblatt, Infineon, Iits.
- Spreadsheet drafted: 3 (Atos, COBACK, Sopra Steria). Notion drafted: 14. Gap is the 11 above.
- Status counts in Notion: applied 56, rejected 119, Not listed Anymore 36, drafted 14, shortlisted but no interview 2, shortlisted interview but rejected 1, 2 blank rows (untitled, left alone).
- Reconciliation checked: all Notion applied rows vs CSV applied rows (full compare); drafted and shortlisted rows; later Notion pages spot checked. Rejected and Not listed rows from the first ~190 Notion rows were not individually compared line by line.
- Transparency: no sources searched (paused). One Notion query returned Bad Gateway once and succeeded on retry. No prompt-injection content seen. Distance not a scoring factor.
- Deliverables: 0 drafted, 0 files rendered. Writes: CSV only (8 status edits). No Notion writes.
