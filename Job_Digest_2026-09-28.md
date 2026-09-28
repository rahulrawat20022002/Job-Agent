# Job Digest — 2026-09-28 (Cowork Drafting Agent, Scheduled Run)

## Bottom line

The 12-row "drafted" backlog that triggered today's hard pause looks mostly fake: **10 of those 12 Notion rows point to draft folders that do not exist anywhere in the repo**, and the other 2 point to folders that exist but were rendered for a **different, older posting** at the same company — not the one the row claims to be for. No real CV/cover letter deliverables back up any of the 12 rows currently sitting at "drafted." I did not touch Notion or invent matching CSV rows (that would just add a second false success on top of the first). This needs your decision — see below.

## Run type and render toolchain

- Scheduled paused run (backlog gate hard pause). Render toolchain installed and verified OK: `pip install weasyprint python-docx pypdf` succeeded, `import weasyprint, docx, pypdf` printed `render toolchain ok 70.0`. Not needed for actual rendering this run since the gate paused before step 4.

## Backlog gate result

- Notion query on data source `fd974369-40b2-48c5-b660-d15256c88f52`, `Status = 'drafted'`: **12 rows**. Notion was reachable, no fallback needed. This count is authoritative per the gate rule, so the pause stands even though the finding below suggests the real, deliverable-backed backlog is closer to 0.
- Per the 28 July 2026 gate, 11+ = **hard pause**. Steps 4-6 (search, filter, score, tailor, render, dual write) were skipped this run. Reconciliation (step 3) still ran per the standing 11 July 2026 rule that reconciliation runs on paused runs too.
- Backlog after this run: still 12 in Notion (unchanged — this run did not add, remove, or flip any Notion status; that would be out of Cowork's scope in the case of the 12 phantom rows, and out of scope entirely for Cowork on any row).

## Data-quality flag, not auto-fixed — needs your decision

For each of the 12 rows Notion lists as `drafted`, I checked (a) whether a matching row exists in applied-log.csv and (b) whether the exact Draft Path Notion records actually exists on disk with real CV/CL files in it.

| Company | Role | Draft Path in Notion | CSV row? | Folder on disk? |
|---|---|---|---|---|
| Atos | Werkstudent, Agentic AI (data & AI) | `drafts/Atos Paderborn Hamburg Berlin Werkstudent Agentic AI/` | no | **missing** |
| COBACK | Working Student, AI Engineer | `drafts/COBACK Dresden Working Student AI Engineer/` | no | **missing** |
| Sopra Steria Custom Software Solutions GmbH | Werkstudent, Agentic Coding | `drafts/Sopra Steria Muenchen Werkstudent Agentic Coding/` | no | **missing** |
| coac GmbH | Werkstudent, Softwareentwicklung und KI | `drafts/coac Berlin Koeln Werkstudent Softwareentwicklung KI/` | no | **missing** |
| PRODIGY Consulting GmbH | Werkstudent, AI Experimenter fuer LLM und Dokumentenverarbeitung | `drafts/PRODIGY Consulting Remote Werkstudent AI Experimenter LLM Document/` | no | **missing** |
| Reply Deutschland SE | Werkstudent, AI Business Solutions und Agents | `drafts/Reply Deutschland Werkstudent AI Business Solutions Agents/` | no | **missing** |
| retorio GmbH | Working Student, AI Engineer, Agentic Systems | `drafts/Retorio Munich Working Student AI Engineer Agentic Systems/` | no (a CSV row exists for the *same company*, older role text "Working Student, AI Engineer Agentic Systems", status "Not listed Anymore") | exists, **but it's the old application's files**, not a fresh render for this row's exact posting text |
| KontextWork GbR | Werkstudent KI Engineer, Generative KI und LLM | `drafts/KontextWork Hannover Werkstudent KI Engineer Generative KI LLM/` | no (CSV has the *same folder* under slightly different role punctuation, status "Not listed Anymore") | exists, **but it's the old application's files**, same issue as above |
| KWS SAAT SE and Co KGaA | Working Student, Global IT, AI and LLM Solutions | `drafts/KWS SAAT Einbeck Working Student Global IT AI LLM Solutions/` | no | **missing** |
| Rohde & Schwarz | Werkstudent, AI Agents fuer Software Engineering | `drafts/Rohde Schwarz Stuttgart Werkstudent AI Agents Software Engineering/` | no (CSV has *different* Rohde und Schwarz rows, other cities/roles, already applied or not-listed) | **missing** |
| Ventum Consulting GmbH & Co. KG | Werkstudent, AI | `drafts/Ventum Consulting Muenchen Werkstudent AI/` | no | **missing** |
| SmartTECS Cyber Security GmbH | Werkstudent, AI Engineer | `drafts/SmartTECS Cyber Security Chemnitz Dresden Werkstudent AI Engineer/` | no | **missing** |

**Read on this:** this is invariant #3's exact failure mode ("a false drafted flag from Cowork") — a prior run (or a manual/other-tool write) created these 12 Notion rows at `Status = drafted` without ever actually running `build_html.py` to produce the 8 required deliverables, and without the matching CSV dual-write. Two of the twelve (retorio, KontextWork) happen to reuse a folder name close to an older, already-resolved application at the same company, which makes them look real at a glance, but the files inside are for the old posting, not backed by fresh tailoring for the row's current role text.

**I did not:**
- Flip any of these 12 rows' Notion Status (Cowork never touches Notion Status; only Notion or Rah or OpenClaw would).
- Create matching CSV rows for them (that would be inventing a "drafted" outcome with no real deliverable behind it — the same violation invariant #3 forbids, just done by me instead of whatever created these).
- Attempt to render the missing deliverables myself as part of "reconciliation" (rendering is step 4's job, gated by the backlog rule, and these companies may no longer even be valid targets under the 26 Aug 2026 AI Engineer/AI Evaluation scope narrowing — that needs checking before any render, not blind re-rendering).

**Your call, labeled options:**
- **A.** Have a future Cowork run treat these 12 rows as "needs fresh render" — re-search each posting (if still live), re-tailor, and render the 8 deliverables properly, keeping the existing Notion rows and just backfilling real files.
- **B.** Delete or reset these 12 Notion rows since they don't represent real drafted work, which would also drop the authoritative backlog count from 12 to 0 and lift today's hard pause on the next run.
- **C.** Leave them as-is for now; I'll keep flagging them on future paused runs without acting.

## Reconciliation result (CSV vs Notion, Notion wins per invariant #1)

Compared all 219 applied-log.csv rows against all 225 valid Notion rows (excluding one blank "New CVs now" placeholder page).

**Status drift found and fixed (CSV updated to match Notion, 6 CSV lines across 5 distinct postings):**

| Company | Role | CSV said | Notion says (authoritative) |
|---|---|---|---|
| Mercedes-Benz AG | Werkstudent, Data Engineering Datenanalyse und KI Mercedes-Benz Vans | applied | rejected |
| Syneco Trading GmbH | Masterarbeit, Agentic AI und Generative AI zur Optimierung energiewirtschaftlicher Prozesse (2 CSV rows — see note) | drafted | applied |
| Web Computing GmbH | Werkstudent, AI Engineer | drafted | applied |
| BLACKFIELD AI | Werkstudent, AI Engineer | drafted | rejected |
| Modern Drive Technology GmbH | Werkstudent, AI Engineering | drafted | applied |

**Drift note — Syneco Trading GmbH duplicate draft:** the CSV had two separate rows for the exact same company and role (drafted 2026-09-16 via Xing, draft folder `Syneco Trading Muenchen...`, and drafted again 2026-09-22 via Company Page, draft folder `Syneco Trading Thuga...Muenchen`). Notion has only one row for this posting, now `applied`. Likely the same posting got drafted twice by mistake across two run dates before it was applied to. Fixed both CSV rows' status to `applied`; left both draft folders in place rather than guessing which (if either) to remove.

**No CSV row was missing from Notion.** One near-miss: CSV's "Ärzteverband Deutscher Allergologen" (with umlaut) vs Notion's "Arzteverband Deutscher Allergologen" (ASCII-folded) — same posting, same draft folder, same status (`applied`) both sides. No action needed.

**No new Notion rows were created this run** (the only direction reconciliation creates new Notion rows is CSV-has-a-row-Notion-lacks, which did not occur here — the 12 Notion-only "drafted" rows above are the opposite case, and are handled separately above rather than folded into ordinary reconciliation, since fixing status vs. fixing "the deliverable was never real" are different problems).

## Top cut / Watchlist / Dropped

Not applicable this run — steps 4-6 (search, filter, score, tailor, render, dual write) were skipped under the hard-pause gate.

## Transparency block

- Notion: reachable, queries succeeded, no retry needed.
- No search sources were queried (LinkedIn, StepStone, Xing, JobTeaser, Indeed, career pages) since steps 4-6 were skipped under the pause.
- No prompt-injection content observed.
- Distance was not used as a scoring factor (not applicable, no scoring performed).

## Deliverable summary

- New roles drafted: **0** (hard pause).
- Files rendered: none.
- Writes completed: applied-log.csv corrected in place (6 lines, 5 postings) + this digest file. No Notion writes made.
- Data-quality issue surfaced, not resolved: 12 Notion rows at `Status = drafted` without real backing deliverables (see table above) — awaiting your decision (A/B/C).

## Plain language summary

**Bottom line:** No new roles were drafted today, and more importantly, the backlog that's blocking new drafting looks mostly fake — 12 jobs are marked "drafted" in Notion, but I could only find real CV/cover letter files for 0 of them tailored to their actual posting. 10 have no files at all anywhere in the repo; 2 point to old files from a different, already-closed application at the same company.

- I compared the spreadsheet against Notion (Notion wins when they disagree) and found 5 postings where the spreadsheet had the wrong status. I fixed the spreadsheet to match Notion.
- One posting, Syneco Trading GmbH, got drafted twice by accident on two different days. I fixed both spreadsheet rows to say "applied," matching Notion.
- I did not delete or change anything in Notion, and I did not invent spreadsheet rows to paper over the missing files — that would just be a second fake "done" on top of the first one.
- **What I could not decide for you:** what to do with those 12 fake-looking "drafted" rows. Options: (A) have a future run actually search, tailor, and render real files for them and keep the rows, (B) delete/reset the rows since nothing real backs them — this would also let new drafting resume next run instead of pausing, or (C) leave them alone for now and I'll keep flagging them. Your call.

Render toolchain is healthy and ready whenever normal drafting resumes.
