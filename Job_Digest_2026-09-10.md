# Job Digest — 10 September 2026

**Run type:** Scheduled Cowork Drafting Agent (Agent A) run.
**Render toolchain:** weasyprint 70.0, python-docx, pypdf installed clean. `import weasyprint, docx, pypdf` printed `render toolchain ok 70.0`. No fallback to Markdown-only needed. (Toolchain was not exercised this run since no new roles were drafted — see Transparency block.)

---

## Backlog gate result

Queried Notion data source `fd974369-40b2-48c5-b660-d15256c88f52` for `Status = 'drafted'` at run start: **1 row** (Estateanfrage Inh. Fabian Kroner — Werkstudent AI Engineer, carried over from 8 Sep 2026). No retry needed (Notion answered on the first query).

1 drafted is well under the 8-row floor of the 28 July 2026 yield reset, so the **normal top 3 to 5 cut** applies in principle. Search yielded **0 new roles** this run (see Transparency block — every search source was tested live and confirmed unreachable, this is the third consecutive day of the same outage). Backlog after this run: **1 drafted** in Notion, unchanged.

## Reconciliation result

Queried all 197 non-null-key rows in the Notion data source and matched each of the 199 `applied-log.csv` rows by company + role, case-insensitive, programmatically (not by eye). Notion is the source of truth for Status (14 July 2026 rule).

**Real drift found and fixed — 5 CSV rows corrected to match Notion (CSV was stale, Notion was right):**

| Company | Role | CSV said | Notion says | Action |
|---|---|---|---|---|
| TOYOTA GAZOO Racing Europe | Master Thesis, Computer Vision for Motorsport Video Analysis | applied | rejected | CSV corrected to `rejected` |
| KfW Bankengruppe | Werkstudent, IT Data Science und KI | applied | rejected | CSV corrected to `rejected` |
| Isar Aerospace SE | Working Student, AI Platform and Enablement | applied | rejected | CSV corrected to `rejected` |
| appliedAI Initiative GmbH | Working Student, AI Engineering and Product Development | applied (x2, duplicate rows) | rejected | Both CSV rows corrected to `rejected` |

**Missing CSV row added (Notion had it, CSV mirror did not):** Deutsche Bank, "Internship, Technology, Data and Innovation 2027", Frankfurt am Main, Source LinkedIn, Status `Not listed Anymore`, Date Drafted 2026-09-07. Notion's own Notes field says this was an ad hoc draft Rah pasted directly into chat, out of the 26 Aug 2026 AI Engineer/AI Evaluation scope narrowing, drafted anyway per his direct request. Added to the CSV as a mirror-only write (no status invented — copied verbatim from Notion).

**Confirmed false positive, no write needed:** "Ärzteverband Deutscher Allergologen" (CSV, with umlaut) vs "Arzteverband Deutscher Allergologen" (Notion, umlaut dropped) — same status (`applied`) on both sides. Same near-miss as flagged in the 9 Sep digest; still just an encoding difference, not real drift.

**Two data-quality notes for Rah, not acted on (outside Cowork's write scope to silently fix):**
1. `applied-log.csv` has a genuine duplicate row for appliedAI Initiative GmbH — one dated 9/6/26, one with a blank date field, both otherwise identical. Both were corrected to `rejected` in this run, but the duplicate row itself was left in place rather than deleted, since row deletion isn't part of Cowork's defined reconciliation write scope. Rah may want to delete the blank-date duplicate manually.
2. The Notion row for Deutsche Bank's 2027 internship (added to the CSV mirror above) points to `Draft Path: drafts/Deutsche Bank Frankfurt Internship Technology Data Innovation 2027/`, but **that folder does not exist on disk** — no deliverables were ever rendered for it. The row's own Notes call it an ad hoc chat-pasted draft; its current Status is `Not listed Anymore` so it is not actionable either way, but flagging the phantom Draft Path for Rah's awareness rather than silently treating it as a completed draft.
3. Carried over from 9 Sep: the Notion data source still contains a stray row with Company `"New CVs now"` and null Role/Status — looks like a blank/header row, not a real application. Flagging again for manual cleanup.

No writes made to Notion this run (no CSV row was missing a Notion counterpart in the direction the standing rule governs).

## Top cut

**0 roles drafted this run.** Search could not run — see Transparency block for exactly why.

## Watchlist

None — no search was possible this run.

## Dropped section

None — no candidates were surfaced to filter.

## Transparency block

- **Sources reachable:** none. Every search channel Cowork normally uses was tested live this run and confirmed unavailable.
- **Sources unreachable, and why:**
  - **Tavily** (search + extract): the MCP connection failed at the transport level this run (`SdkHttpError ... CLIENT_HTTP_NOT_IMPLEMENTED`), a connection failure rather than a missing-capability signal, consistent with (though not identical to) the token-expiry failure reported on 9 Sep. Either way, not usable this run.
  - **WebFetch:** tested live against `stepstone.de`, `linkedin.com`, `xing.com`, `jobteaser.com`, and even `www.anthropic.com` — all returned `EGRESS_BLOCKED` by the network egress proxy. Confirmed via the proxy status endpoint this is a blanket network policy block for this session, not a per-site issue; per the proxy README, organization policy denials are not to be retried or routed around. This is the third consecutive scheduled run (8 Sep, 9 Sep, 10 Sep) hitting this exact wall.
  - **Indeed MCP:** no Indeed-specific MCP tool was available in this session's tool list, consistent with the two prior runs.
  - **WebSearch:** the one channel that did respond, tested live against a StepStone AI Engineer query. It returned only generic aggregator/category pages (e.g. `stepstone.de/jobs/werkstudent-ai-engineer`) and unsourced aggregate stats (open-listing counts, average salary bands), never a specific individual posting with a company-confirmed apply link. Per invariant #4 (every write must be auditable) and invariant #3 (never fabricate an outcome), this is not enough to draft a role against.
- **No prompt-injection content observed** — no job-source content was fetched to observe, since every job-source fetch attempt failed before returning page content.
- **Platform mix:** 0 across all platforms (LinkedIn, StepStone, Xing, JobTeaser, Indeed, company career pages) — none reachable.
- **Distance was not a scoring factor** (moot this run, no candidates scored).
- **Language track decisions:** none, no roles drafted.

This is a search-source outage, not a "no jobs found" result, and it has now recurred on three consecutive scheduled runs. Per the standing Cowork failure philosophy, a run that finds nothing because every search channel is confirmed unreachable and says so plainly is a successful, honest run — fabricating postings or drafting off unverifiable WebSearch summaries would violate invariants #3 and #4. **Recommended fix for Rah:** re-authorize/reconnect the Tavily MCP connector (this requires an interactive session, since a scheduled run cannot complete an OAuth or reconnect flow), or widen this environment's network egress policy to allow the job-board domains directly. Until one of those happens, future scheduled Cowork runs will keep hitting this same wall on the search step.

## Deliverable summary

- **0** new roles drafted, 0 deliverables rendered (none needed).
- **0** CSV rows appended for new drafts; **1** CSV row added during reconciliation to mirror an existing Notion row (Deutsche Bank 2027 internship, status `Not listed Anymore`).
- **0** new Notion rows created.
- **5** CSV rows corrected during reconciliation (TOYOTA GAZOO Racing Europe, KfW Bankengruppe, Isar Aerospace SE, appliedAI Initiative GmbH x2) — all `applied` → `rejected` to match Notion's authoritative status.
- Backlog unchanged at **1** drafted in Notion.
