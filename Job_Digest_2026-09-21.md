# Job Digest — 2026-09-21 (Cowork Drafting Agent, Scheduled Run)

## Bottom line

Notion's drafted backlog is at 13, which trips the 11+ hard pause, so this run drafted zero new roles. I did run reconciliation (required even on paused runs) and found two things worth your attention: three status corrections, and three "drafted" rows in Notion that have no actual CV/CL files behind them anywhere in the repo — likely a false-success from a prior run.

## Run type and render toolchain

- Scheduled paused run (backlog gate hard pause). Render toolchain installed and verified OK (weasyprint 70.0, python-docx, pypdf) even though it was not needed for any new drafts this run.

## Backlog gate result

- Notion query on data source `fd974369-40b2-48c5-b660-d15256c88f52`, `Status = 'drafted'`: **13 rows**. Notion was reachable, no fallback needed.
- Per the 28 July 2026 gate, 11+ = **hard pause**. Steps 4-6 (search, tailor, render, dual-write) were skipped this run. Reconciliation (step 3) still ran per the CLAUDE.md rule that reconciliation runs on paused runs too.
- Backlog after this run: still 13 in Notion (no rows were added or removed from Notion this run).

## Reconciliation result

Compared all 212 CSV rows against all 210 valid Notion rows (one blank placeholder row in Notion, "New CVs now", was excluded as not a real job row).

**Status drift found and fixed (3 rows, CSV updated to match Notion per invariant #1):**

| Company | Role | CSV said | Notion says (now authoritative) |
|---|---|---|---|
| Mercedes-Benz AG | Werkstudent, Data Analytics and Projektsteuerung MB.OS | applied | rejected |
| Mercedes-Benz Tech Innovation | Werkstudent, AI Agents and Robotics Platform | applied | rejected |
| Mercedes-Benz Tech Innovation | Werkstudent, Machine Learning Engineering | applied | rejected |

These three CSV rows were flipped from `applied` to `rejected` to match Notion. No Notion writes were made (CSV is the mirror; Notion is not overwritten).

**Data-quality flag, not auto-fixed — needs your decision:**

Three Notion rows are `Status = drafted` (created 2026-09-20, presumably by yesterday's run) but **have no matching draft folder anywhere in the repo** — meaning no CV/CL files were ever actually rendered for them. This looks like a false "drafted" flag from a prior run (the exact failure mode invariant #3 warns about), so I did not add matching CSV rows or touch the Notion status — writing either would risk mirroring a record that isn't backed by real deliverables.

| Company | Role | Notion Status | Draft Path in Notion | Files on disk |
|---|---|---|---|---|
| Control Expert GmbH | Working Student QA Engineer, AI / LLM Systems | drafted | `drafts/Control Expert Langenfeld Working Student QA Engineer AI LLM Systems/` | **missing** |
| FUNKE Mediengruppe | Werkstudent Workflow Automation n8n, Agentic AI | drafted | `drafts/FUNKE Mediengruppe Hamburg Werkstudent Workflow Automation Agentic AI/` | **missing** |
| Vector Informatik GmbH | Werkstudent, AI driven CI/CD Automation | drafted | `drafts/Vector Informatik Stuttgart Karlsruhe Werkstudent AI CI CD Automation/` | **missing** |

These 3 rows count toward the "13 drafted" backlog number above (Notion's count is authoritative per the gate rule, so I did not subtract them), but they are not real, actionable drafts right now. Your call: (A) have a future Cowork run re-render these three properly, or (B) delete/correct the 3 Notion rows if they should not exist. I'm flagging rather than deciding.

**Minor, no action needed:** one CSV/Notion match looked like a miss ("Ärzteverband Deutscher Allergologen" in CSV vs "Arzteverband..." in Notion, umlaut-only spelling difference) — both sides already say `applied`, so there was nothing to reconcile.

**CSV housekeeping note (not fixed, low priority):** 5 pairs of exact duplicate rows exist in applied-log.csv (same company+role appearing twice, same status both times) — e.g. Mi-Jack Europe GmbH, appliedAI Initiative GmbH, KontextWork GbR, Rohde und Schwarz, Estateanfrage. Harmless (no status conflict) but noted for a future cleanup pass.

## Top cut / Watchlist / Dropped

Not applicable this run — search, filter, score, and tailor (steps 4-6) were skipped under the hard pause.

## Transparency block

- **Notion:** reachable, single query, no retry needed.
- **Tavily MCP:** failed to connect this run (proxy-level connection error, not an access denial). This would have limited company-career-page search via Tavily had this been a normal (non-paused) run; noting it here so it's on record for the next active run.
- **No search sources were queried** (LinkedIn, StepStone, Xing, JobTeaser, Indeed, career pages) since steps 4-6 were skipped under the pause. Nothing to report on freshness dating, platform mix, or prompt-injection content this run.
- Distance was not used as a scoring factor (not applicable — no scoring performed this run).

## Deliverable summary

- New roles drafted: **0** (hard pause)
- Files rendered: none
- Writes completed: 1 (applied-log.csv status corrections, 3 rows) + this digest file
- Notion writes: none (no new pages created, no existing rows modified)
