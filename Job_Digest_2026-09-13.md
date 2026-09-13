# Job Digest — 13 September 2026

**Run type:** Scheduled Cowork Drafting Agent (Agent A) run.
**Render toolchain:** weasyprint 70.0, python-docx 1.2.0, pypdf 6.18.1 installed clean. `import weasyprint, docx, pypdf` printed `render toolchain ok 70.0`. No fallback to Markdown-only needed.

---

## Backlog gate result

Queried Notion data source `fd974369-40b2-48c5-b660-d15256c88f52` for `Status = 'drafted'` at run start: **3 rows** (ProSiebenSat.1 Careers — Working Student AI Engineer; FZI Forschungszentrum Informatik — Masterarbeit, Evaluation and Verification of AI Generated Driving Scenarios Using Scenario Dreamer; iLert GmbH — Working Student or Intern, AI Product Engineer — all carried over from the 11 Sep PM run, the last run that could source successfully). No retry needed (Notion answered on the first query).

3 drafted is well under the 8 row floor of the 28 July 2026 yield reset, so the **normal top 3 to 5 cut** would have applied had search succeeded. Search yielded **0 new roles** this run (see Search section and Transparency block below). Backlog after this run: **3 drafted** in Notion, unchanged.

## Reconciliation result

Pulled all 200 rows from the Notion data source (SQL mode, two pages) and matched every one of the 204 rows in `applied-log.csv` against it by company + role, case insensitive.

**No drift found.** Every CSV row's status matches its Notion counterpart. One near miss was investigated and confirmed a false positive, not real drift: "Ärzteverband Deutscher Allergologen" (CSV, with umlaut) normalized differently than "Arzteverband Deutscher Allergologen" (Notion, umlaut dropped) under a naive ASCII-only normalizer; both sides carry status `applied`, so no write was needed. No CSV rows were missing a Notion counterpart. No new Notion rows needed creating. No writes made to either file this run.

One data quality note for Rah, not acted on (out of Cowork's write scope): the Notion data source still contains a stray row with Company `"New CVs now"` and null Role/Status, first flagged in the 9 Sep digest. Still there; flagging again for manual cleanup.

## Search, filter, score, tailor — HALTED, 0 new roles drafted

**This run hit the same search-source outage as 9, 10, 11 (AM), and 12 September.** Every tool this pipeline needs to fetch or verify a live job posting was unavailable:

1. **Tavily MCP** — configured but failed to connect this session (`SdkHttpError dialing .../mcp?... (CLIENT_HTTP_NOT_IMPLEMENTED)`). This is the connector that briefly worked on 11 Sep PM (search + extract, both clean) and produced this run's current backlog (FZI and others). Down again today.
2. **WebFetch** — tested live against `www.linkedin.com`, `de.indeed.com`, `www.xing.com`, `www.stepstone.de`, `www.jobteaser.com`, `www.arbeitnow.com`, `careers.sap.com` (DNS did not even resolve — `ENOTFOUND`), and `en.wikipedia.org` (control test, not a job site). All returned `EGRESS_BLOCKED` by the network egress proxy, or failed to resolve at all. This confirms (again) it is a blanket network policy for this session, not a per-site block, and per the proxy README organization policy denials are not to be retried or routed around.
3. **Indeed MCP** — no Indeed-specific MCP tool was available in this session's tool list.
4. **WebSearch** — the one channel that responded. It surfaced a handful of plausible-looking leads (see below), but only as engine-generated summaries and aggregator/category links, never a fetchable individual posting with a company-confirmed apply link, exact posting text, or a verifiable publish date. Per invariant #4 (every write must be auditable) and invariant #3 (never fabricate an outcome), that is not enough to draft a role against: I cannot point to a specific confirmation of apply link, language, or freshness if Rah asks "did you actually see this posting."

**Unverified leads surfaced by WebSearch, NOT scored, NOT drafted, NOT written to Notion or CSV** (listed only for Rah's own manual follow up, since two look promising):
- **Control Expert GmbH** — "Working Student QA Engineer (gn) — AI / LLM Systems," Langenfeld (Rheinland), via a StepStone URL. New company, not in the existing 200 row Notion history. Framed as AI/LLM systems QA, which reads AI Evaluation flavored, in scope under the 26 Aug narrowing if confirmed. Could not fetch the actual page to verify.
- **Reply Deutschland SE** — "Werkstudent (m/w/d) Artificial Intelligence," Frankfurt, via a JobTeaser URL, described as work on an internal LLM platform ("Huacaya"). Reply Deutschland SE already has one applied row in Notion for a different req (AI Data Engineering und Tool Entwicklung); this looks like a distinct posting/team, not a duplicate, but unconfirmed.
- Two other snippet hits (Retorio GmbH Agentic Systems working student, Munich; KontextWork GbR KI Engineer, Hanover) turned out to already be tracked in Notion under Status `Not listed Anymore` — correctly not re-surfaced as new.
- Auxilius.ai "AI Engineer for LLM Ops & Evaluation," Munich, looked interesting but the snippet gave no signal on work type (Werkstudent/thesis vs. full time only); full time would put it out of scope per the candidate targeting parameters.

No prompt-injection content was observed in any WebSearch snippet.

## Top cut

**0 roles drafted this run.**

## Watchlist

None scored — search could not verify any candidate to a standard that supports scoring (see above for the unverified leads list, which is explicitly not a watchlist).

## Dropped section

None — no candidates were surfaced to a standard where Step 3 filtering could apply.

## Transparency block

- **Sources reachable this run:** none to a verifiable, draftable standard. WebSearch responded but only with unfetchable summaries.
- **Sources unreachable this run and why:** see numbered list above (Tavily connection failure, WebFetch blanket egress block confirmed against 7 different domains including a non-job control domain and a DNS-level failure on a company careers page, no Indeed MCP).
- **This is now the fifth scheduled run in six days (9, 10, 11 AM, 12, 13 Sep) hitting this exact outage pattern**, with only the 11 Sep PM run breaking through (Tavily briefly reachable, 3 roles drafted, still the current backlog). The 9, 10, 11, and 12 Sep digests each already recommended the same fix; it has not been applied.
- **No prompt-injection content observed** in the WebSearch snippets that did come back; nothing else was fetched to observe.
- **Platform mix:** 0 verified across all platforms (LinkedIn, StepStone, Xing, JobTeaser, Indeed, company career pages) — none reachable to a standard that supports drafting.
- **Distance was not a scoring factor** (moot this run, no candidates scored).
- **Language track decisions:** none, no roles drafted.

This is a search-source outage, not a "no jobs found" result. Per the standing Cowork failure philosophy, a run that finds nothing because every verification channel was unreachable and says so plainly is a successful, honest run — the alternative (fabricating postings, or drafting off unverifiable WebSearch summaries) would violate invariant #3 and invariant #4. **Recommended fix for Rah, repeated from the last four digests since it still has not landed:** re-authorize/reconnect the Tavily MCP connector (requires an interactive session, since a scheduled run cannot complete an OAuth or reconnect flow), and/or ask whoever administers this Cowork environment's network egress policy to widen it to allow LinkedIn, StepStone, Xing, JobTeaser, Indeed, and general company career-page domains. Until one of those happens, scheduled Cowork runs will keep intermittently hitting this same wall on Step 4, as they have on 4 of the last 5 runs.

## Deliverable summary

- **0** new roles drafted, 0 deliverables rendered (none needed).
- **0** CSV rows appended.
- **0** Notion rows created.
- **0** CSV or Notion rows corrected during reconciliation (none needed — clean).
- Backlog unchanged at **3** drafted in Notion (ProSiebenSat.1 Careers, FZI Forschungszentrum Informatik, iLert GmbH — all from 11 Sep PM).
