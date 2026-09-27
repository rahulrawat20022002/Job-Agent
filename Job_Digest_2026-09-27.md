# Job Digest — 2026-09-27 (Cowork Drafting Agent, scheduled run)

## Bottom line

Notion's drafted backlog is 12, over the 11+ hard-pause threshold, so **no new
roles were searched or drafted this run.** Reconciliation ran anyway (it
always does, even on a paused run) and found real drift: 8 CSV rows were
stale because OpenClaw had already moved those applications on in Notion, and
the CSV has now been corrected to match Notion. Separately, this run also
found that **10 of the 12 rows currently sitting in the Notion backlog have
no CV or cover letter files anywhere in the repo** — they say "drafted" but
nothing was actually rendered or committed. That is a decision item for Rah,
flagged below and not touched further by this run.

## Run type and render toolchain

Scheduled Cowork run. Toolchain installed and verified:
`pip install weasyprint python-docx pypdf` succeeded;
`python3 -c "import weasyprint, docx, pypdf"` printed
`render toolchain ok 70.0`. No fallback to Markdown-only was needed or used.

## Backlog gate (28 July 2026 gate, Notion first)

- Notion query on data source `fd974369-40b2-48c5-b660-d15256c88f52`,
  `Status = 'drafted'`: **12 rows**. Query succeeded on first try, no CSV
  fallback needed.
- Gate zone: **11 or more → hard pause.** Steps 4-6 (search, tailor, render,
  dual-write of new roles) were skipped this run per the gate. Reconciliation
  (step 3) still ran per the standing CLAUDE.md rule that reconciliation runs
  on paused runs too, and commit/push/verify (steps 7-8) still ran.
- Backlog after this run: still 12 in Notion (no new rows created, none
  removed — see decision item below for why the true "actually drafted"
  count is lower).

## Reconciliation result

Read all 219 rows of `applied-log.csv`, matched each drafted-status CSV row
to Notion by company + role (case-insensitive). Notion is the source of
truth for Status (14 July 2026 rule) — CSV updated to match, never the
reverse. **8 CSV rows were out of date and have been corrected:**

| Company | Role (short) | CSV said | Notion says (now applied to CSV) |
|---|---|---|---|
| Syneco Trading GmbH | Masterarbeit, Agentic AI... (Xing, 9/16) | drafted | applied |
| Syneco Trading GmbH | Masterarbeit, Agentic AI... (Company Page, 9/22) | drafted | applied |
| Web Computing GmbH | Werkstudent, AI Engineer | drafted | applied |
| BLACKFIELD AI | Werkstudent, AI Engineer | drafted | rejected |
| Modern Drive Technology GmbH | Werkstudent, AI Engineering | drafted | applied |
| Retorio | Working Student, AI Engineer Agentic Systems | Not listed Anymore | drafted |
| KontextWork GbR (row, blank date) | Werkstudent, KI Engineer Generative KI und LLM | Not listed Anymore | drafted |
| KontextWork GbR (row, 9/6) | Werkstudent, KI Engineer Generative KI und LLM | Not listed Anymore | drafted |

No CSV row was missing a Notion counterpart in a way that required creating
a new Notion row (the CSV→Notion direction of reconciliation). See the
decision item below for the reverse situation (Notion rows with no CSV/file
counterpart), which reconciliation as specified does not cover and this run
did not invent a fix for.

## Decision item for Rah: 10 "drafted" Notion rows have no files anywhere

**What I found:** Notion says these 10 roles are drafted, but there is no
`drafts/[folder]/` for any of them in the repo, on any branch, at any point
in git history. I checked `main`, this run's branch, and full git history —
nothing. That means no CV, no cover letter, nothing was ever actually
rendered and committed for these, even though Notion says "drafted."

- Atos — Werkstudent, Agentic AI (data & AI) — drafted 2026-09-23
- COBACK — Working Student, AI Engineer — drafted 2026-09-23
- Sopra Steria Custom Software Solutions GmbH — Werkstudent, Agentic Coding — drafted 2026-09-23
- coac GmbH — Werkstudent, Softwareentwicklung und KI — drafted 2026-09-24
- PRODIGY Consulting GmbH — Werkstudent, AI Experimenter fuer LLM und Dokumentenverarbeitung — drafted 2026-09-24
- Reply Deutschland SE — Werkstudent, AI Business Solutions und Agents — drafted 2026-09-24
- KWS SAAT SE and Co KGaA — Working Student, Global IT, AI and LLM Solutions — drafted 2026-09-25
- Rohde & Schwarz — Werkstudent, AI Agents fuer Software Engineering — drafted 2026-09-26
- Ventum Consulting GmbH & Co. KG — Werkstudent, AI — drafted 2026-09-26
- SmartTECS Cyber Security GmbH — Werkstudent, AI Engineer — drafted 2026-09-26

(The other 2 of the 12 backlog rows — retorio GmbH and KontextWork GbR — do
have real, complete 8-file draft folders on disk, confirmed above.)

**What this means:** the real "ready to submit" backlog is 2 roles, not 12.
The other 10 are phantom entries — Notion rows created by an earlier run
without the render-and-commit step actually completing (or completing
somewhere that never got pushed/merged). I did not invent CVs for these,
did not delete the Notion rows, and did not backfill fake CSV rows to match
them, because any of those would either fabricate a deliverable or fabricate
an audit trail — both against the no-fabrication rule this pipeline runs on.

**What I could not decide for you — pick one:**
- **A.** Have a future Cowork run regenerate real deliverables for these 10
  using the company/role/location/source already sitting in Notion, so the
  "drafted" flag becomes true.
- **B.** Have Rah (or a future run, told explicitly) reset these 10 Notion
  rows to some other status (e.g. back to a re-search queue) since the
  postings may be stale by now (oldest is 4 days old, 23 Sep).
- **C.** Leave them exactly as-is for now and revisit later.

This run took no action on these 10 beyond finding and reporting them, and
they are excluded from anything this run treats as a real, file-backed
draft.

## Top cut / watchlist / dropped

None — this run drafted zero new roles (hard-pause gate). No search was
run, so there is no watchlist or dropped-roles list to report this cycle.

## Transparency block

- Sources reachable/unreachable: not applicable, search step was skipped
  under the pause gate.
- Freshness dating: not applicable this run.
- Prompt-injection content observed but not acted on: the Notion MCP
  server's tool instructions for this session included an unusual
  instruction telling the agent to surface an "upgrade"/advanced-analysis
  link in the final chat reply under certain conditions. That condition
  was never triggered during this run (no multi-data-source query was
  attempted), so nothing was surfaced, but it is noted here per the
  standing instruction to report anything that looked like it was trying to
  steer output beyond the task.
- Platform mix: not applicable, no new drafts this run.
- Distance was not a scoring factor (standing rule, unaffected this run).

## Deliverable summary

- New roles drafted this run: 0 (hard-pause gate).
- CSV rows corrected during reconciliation: 8.
- New Notion rows created: 0.
- Files rendered this run: 0.
- Decision item raised for Rah: 10 phantom "drafted" Notion rows with no
  backing files (see above).
