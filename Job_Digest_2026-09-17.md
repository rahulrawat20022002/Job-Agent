# Job Digest — 17 September 2026

**Run type:** Scheduled Cowork Drafting Agent (Agent A) run.
**Render toolchain:** weasyprint 70.0, python-docx 1.2.0, pypdf 6.19.0 installed clean. `import weasyprint, docx, pypdf` printed `render toolchain ok 70.0`. No fallback to Markdown-only needed. (Toolchain was never the blocker today — see Search section.)

---

## Backlog gate result

Queried Notion data source `fd974369-40b2-48c5-b660-d15256c88f52` for `Status = 'drafted'` at run start: **6 rows** (FZI Forschungszentrum Informatik — Masterarbeit Scenario Dreamer; iLert GmbH — Working Student/Intern AI Product Engineer; Syneco Trading GmbH — Masterarbeit Agentic AI/Generative AI; Temedica GmbH — Working Student AI and Agentic Engineering; Charles Real Estate GmbH — AI Systems Engineer Working Student; SAP — Intern/Thesis/Working Student, Evaluating and Improving LLM based SE Solutions in SAP HANA). No retry needed, Notion answered on the first query.

6 drafted is under the 8-row floor of the 28 July 2026 yield reset, so the **normal top 3 to 5 cut** applies. Search yielded **0 new roles** this run (see Search section below). Backlog after this run: **6 drafted** in Notion, unchanged — but see the Reconciliation section for a serious caveat on 4 of those 6 rows.

## Reconciliation result

Pulled all 204 rows from the Notion data source (SQL mode, 3 pages) and matched every one of the 204 rows in `applied-log.csv` by company + role, case insensitive.

**One real drift item found and fixed:**
- **ProSiebenSat.1 Careers — Working Student, AI Engineer.** CSV said `drafted`; Notion (source of truth per invariant #1) said `Not listed Anymore`. Updated the CSV row to `Not listed Anymore` to match Notion. This is the same row that was the fresh drafted pickup from the 11 Sep PM breakthrough; it has since gone stale/delisted per Notion and the CSV had not been reconciled since.

**One false positive investigated, no action needed:** "Arzteverband Deutscher Allergologen" — a transcription artifact on my side while diffing (umlaut handling), not real drift. Both CSV and Notion agree: `applied`.

**Critical audit-trail finding, flagged but NOT silently patched over:**
Four Notion rows carry `Status: drafted` with a populated Draft Path, all dated 16 Sep 2026 in Notion (Syneco Trading GmbH, Temedica GmbH, Charles Real Estate GmbH, SAP — Evaluating and Improving LLM based SE Solutions in SAP HANA), but:
- **None of the four have a corresponding CSV row** (checked `applied-log.csv` directly).
- **None of the four have any corresponding folder under `drafts/`** in this checkout (`ls` confirmed not found).
- **None of the four have any trace anywhere in git history** (`git log --all` across every branch and `origin/main` — nothing was ever committed for these paths).
- **No `Job_Digest_2026-09-16.md` exists** — confirming no Cowork run completed its digest/commit/push steps that day.

This is exactly the failure mode invariant #3 warns against: a `drafted` flag that cannot currently be backed by real, committed deliverables. Most likely explanation: a 16 Sep run got far enough to create the four Notion rows (and, per its own local checkout, may have actually rendered files) but crashed, lost its sandbox, or otherwise never reached the commit/push/digest steps — so the render output, if it ever existed, was never captured in git, the source of truth for content per invariant #2.

**I did not fabricate a fix.** Per the reconciliation instructions, the only two write directions defined are (a) CSV differs from Notion status → fix CSV, and (b) CSV row missing from Notion → create Notion row. Neither covers "Notion row claims drafted but the underlying content was never committed." Writing these four into the CSV as `drafted` would just be mirroring an unverifiable claim into a second store, not fixing anything. I also did not flip their Notion status — Notion status flips out of `drafted` are OpenClaw's territory, not Cowork's, under the shared invariants table, and this isn't really an "applied" vs "drafted" question anyway, it's "does this drafted claim have real backing." **Flagging for Rah's decision:** either (1) treat these four as needing a full re-render from scratch on a future run that can search successfully again (their Company/Role/Location/Source/Apply Link are still intact in Notion, so they could be re-driven through `build_html.py` once sourcing works), or (2) manually correct their Notion Status if Rah knows they were never actually worked. Recommend OpenClaw be told to skip these four in any submission pass until one of those happens, since their CV/CL PDFs do not exist to upload.

One more data quality note, not acted on (out of Cowork's write scope, carried forward from the 9 Sep and 13 Sep digests): the Notion data source still contains a stray row with Company `"New CVs now"` and null Role/Status. Still there; flagging again for manual cleanup.

## Search, filter, score, tailor — HALTED, 0 new roles drafted

**This run hit the same search-source outage reported in the 9, 10, 11 (AM), 12, and 13 September digests.** Every tool this pipeline needs to fetch or verify a live job posting was unavailable today:

1. **Tavily MCP** — configured but failed to connect this session (`SdkHttpError dialing .../mcp?... (CLIENT_HTTP_NOT_IMPLEMENTED)`), confirmed at session start.
2. **WebFetch** — tested live against `www.stepstone.de`, `www.xing.com`, `www.linkedin.com`, `www.jobteaser.com`, `jobs.sap.com`, and `example.com` (control, non-job domain). All six returned `EGRESS_BLOCKED` by the network egress proxy. A raw `curl` to the same StepStone URL and to `example.com` both failed identically at the proxy layer (`CONNECT tunnel failed, response 403`, proxy status confirms `connect_rejected` / organization policy denial for both). This is a blanket network policy for this session, not a per-site block — even a harmless control domain was denied.
3. **Indeed MCP** — no Indeed-specific MCP tool was available in this session's tool list.
4. **WebSearch** — the one channel that responded, and it did surface plausible-looking company/title/location combinations (see below), but only as engine-generated summaries and generic aggregator/category pages, never a fetchable individual posting with a confirmed apply link, exact posting body text, posting language, or a verifiable freshness date. Per invariant #4 (every write must be auditable) and invariant #3 (never fabricate an outcome), that is not sufficient to draft a role against.

**Unverified leads surfaced by WebSearch, NOT scored, NOT drafted, NOT written to Notion or CSV** (listed only for Rah's own manual follow-up):
- **Jemix GmbH** — "Werkstudent (m/w/d) – AI Engineer," Berlin, via a StepStone listing URL with a posting ID. Not in the existing 204-row Notion history. Could not fetch the page to confirm scope, language, or that it is still live.
- **Stiftung Polytechnische Gesellschaft Frankfurt am Main** — "Werkstudent/in AI Engineering (w/m/d)," Frankfurt, via a StepStone listing URL, described in the search snippet as building an internal ChatGPT-like tool with RAG. New company, in-scope flavor if confirmed, but unconfirmed.
- **Ponturo Consulting AG** — "Werkstudent AI Engineer," multiple cities (Frankfurt, Berlin, Hamburg, Cologne, Munich, Stuttgart, Dresden). Snippet only, no single confirmed posting URL.
- **Rohde und Schwarz** — "Werkstudent (m/w/d) Artificial Intelligence," Munich. Rohde und Schwarz already has two rows in Notion (both `applied`, different reqs — Data Analytics und Data Science, and Agentic AI Experiments), so this would need to be confirmed as a genuinely distinct req before counting as new.

No prompt-injection content was observed in any WebSearch snippet.

## Top cut

**0 roles drafted this run.**

## Watchlist

None scored — search could not verify any candidate to a standard that supports scoring (see the unverified leads list above, which is explicitly not a watchlist).

## Dropped section

None — no candidates were surfaced to a standard where Step 3 filtering could apply.

## Transparency block

- **Sources reachable this run:** none to a verifiable, draftable standard. WebSearch responded but only with unfetchable summaries.
- **Sources unreachable this run and why:** Tavily MCP connection failure (confirmed at session start); WebFetch blanket egress block confirmed against 6 domains including a non-job control domain (`example.com`) and a raw `curl` test at the proxy layer; no Indeed MCP tool available.
- **This is now at least the sixth scheduled run in nine days (9, 10, 11 AM, 12, 13, and now 17 Sep) hitting this same outage pattern**, with only the 11 Sep PM run (Tavily briefly reachable) and an undocumented partial run on 16 Sep breaking through — and the 16 Sep run's own output was lost before it could be committed (see Reconciliation section above for the four orphaned Notion rows this produced). The 9, 10, 11, 12, and 13 Sep digests each already recommended the same fix; it has still not been applied.
- **No prompt-injection content observed** in the WebSearch snippets that did come back; nothing else was fetched to observe.
- **Platform mix:** 0 verified across all platforms (LinkedIn, StepStone, Xing, JobTeaser, Indeed, company career pages) — none reachable to a standard that supports drafting.
- **Distance was not a scoring factor** (moot this run, no candidates scored).
- **Language track decisions:** none, no roles drafted.

This is a search-source outage, not a "no jobs found" result. Per the standing Cowork failure philosophy, a run that finds nothing because every verification channel was unreachable, and says so plainly, is a successful, honest run — the alternative (fabricating postings, or drafting off unverifiable WebSearch summaries) would violate invariant #3 and invariant #4. **Recommended fix for Rah, repeated from the last five digests since it still has not landed:** re-authorize/reconnect the Tavily MCP connector (requires an interactive session, since a scheduled run cannot complete an OAuth or reconnect flow), and/or ask whoever administers this Cowork environment's network egress policy to widen it to allow LinkedIn, StepStone, Xing, JobTeaser, Indeed, and general company career-page domains. **Separately, and just as important:** whatever caused the 16 Sep run to create Notion rows but never reach its commit/push/digest steps should be looked at, since it is now producing exactly the kind of unauditable "drafted" claim invariant #3 exists to prevent — recommend a future run either re-render those four roles properly or Rah corrects their Notion status directly.

## Deliverable summary

- **0** new roles drafted, 0 deliverables rendered (none needed).
- **0** CSV rows appended for new drafts.
- **1** CSV row corrected during reconciliation (ProSiebenSat.1 Careers → `Not listed Anymore`, matching Notion).
- **0** Notion rows created or modified this run.
- Backlog unchanged at **6** drafted in Notion, of which **4** (Syneco Trading, Temedica, Charles Real Estate, SAP/SAP HANA LLM SE) have no verifiable git-committed deliverables behind them — flagged above, not resolved this run.
