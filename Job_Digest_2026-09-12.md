# Job Digest — 2026-09-12 (Cowork scheduled run)

## Run type and render toolchain result

Scheduled Cowork Drafting Agent run. Render toolchain installed and verified
successfully:

```
pip install weasyprint python-docx pypdf --break-system-packages
python3 -c "import weasyprint, docx, pypdf; print('render toolchain ok', weasyprint.__version__)"
render toolchain ok 70.0
```

No render work was needed this run (zero new roles — see Search section
below), so the toolchain was verified but not exercised end to end.

## Backlog gate result

Queried Notion data source `fd974369-40b2-48c5-b660-d15256c88f52` for
`Status = 'drafted'`. **3 rows drafted** (all from yesterday's 2026-09-11
run: ProSiebenSat.1 Careers, FZI Forschungszentrum Informatik, iLert GmbH).
3 is under 8, so this is the **normal zone** (top 3 to 5 cut applies). No
pause triggered.

## Reconciliation result

Read all 204 data rows in `applied-log.csv` and compared each to Notion by
company + role (case insensitive). Pulled all 200 Notion rows via SQL query
for the comparison.

- **Drift found and fixed: none.** Every CSV row's status matched its
  Notion counterpart exactly.
- **CSV rows missing from Notion: none real.** One near-miss surfaced by
  the automated matcher — "Ärzteverband Deutscher Allergologen" (CSV, with
  umlaut) vs "Arzteverband Deutscher Allergologen" (Notion, umlaut
  stripped) — but manual verification confirmed this is the same row
  (both status `applied`), just a diacritic transcription difference. No
  duplicate was created.
- Reconciliation is clean; no writes were needed in either direction.

## Search, filter, score, tailor — HALTED, 0 new roles drafted

**This is the significant finding of this run.** Step 4 (search) could not
be executed safely, so per CLAUDE.md's failure philosophy ("halting a row
is always better than a false success," invariant #3, never fabricate an
outcome) I halted rather than draft roles from unverifiable data.

**What happened, in order:**

1. **Tavily MCP** — configured but failed to connect this session
   (`SdkHttpError ... CLIENT_HTTP_NOT_IMPLEMENTED`). This is the source
   the scheduled prompt designates for company career pages.
2. **Indeed connector** — checked via `ListConnectors`: authenticated and
   connected at the org level, but **toggled off for this chat**
   (`enabledInChat: false`). Its tools were not present in this session's
   tool list, so the Indeed MCP the prompt asks me to prefer for Indeed
   listings was unavailable.
3. **Firecrawl connector** — same situation: connected at org level,
   toggled off for this chat. Could have served as a scraping fallback
   for LinkedIn/Xing/StepStone/JobTeaser but was not available.
4. **WebFetch** — tested against multiple targets (stepstone.de,
   jobteaser.com, welcometothejungle.com, jobs.fraunhofer.de, indeed.com,
   and as a control, en.wikipedia.org and example.com). **Every single
   one returned `EGRESS_BLOCKED`** — this session's network egress policy
   blocks WebFetch to external domains outright, not just job boards.
   This is a session/environment configuration matter, not a
   job-board-specific block.
5. **WebSearch** — the only reachable tool. It returned real, current
   search-result snippets (titles, companies, sometimes locations, short
   description fragments) for AI Engineer / AI Evaluation postings on
   StepStone, LinkedIn, JobTeaser, and via Glassdoor/other aggregators
   (e.g., a Fraunhofer Munich Master Thesis on "Agentic LLM for Tool
   Evaluation," a Lilt Berlin "AI Research & Data Evaluation Work
   Student," an ABB AG JobTeaser generative-AI internship). These are
   plausible, on-target leads. **But** a WebSearch snippet is not the
   full posting body: it cannot confirm the posting's actual language
   (English vs German, which the 20 July 2026 rule requires to determine
   the CV/CL language track end to end), the exact German-level bar, the
   live apply link's current validity, or the requirements text needed to
   tailor bullets without inventing detail. Drafting a full 8-deliverable
   CV/cover letter package on snippet text alone would risk exactly the
   fabrication invariant #3 forbids.

**Decision:** halt Step 4 entirely this run. Zero roles drafted. Zero
Notion rows created. Zero CSV rows appended. Backlog stays at 3 drafted in
Notion, unchanged from before this run.

**Leads surfaced by WebSearch, not drafted, for a future run once sourcing
is restored** (unverified — listed as pointers only, not vetted fits):

- Fraunhofer (institute unspecified in snippet), Munich — "Master Thesis
  on Agentic LLM for Tool Evaluation" — strong AI Evaluation keyword match
  on title alone.
- Lilt, Berlin — "AI Research & Data Evaluation Work Student" (part-time)
  — strong AI Evaluation match on title.
- ABB AG, via JobTeaser — "Internship or Student Worker, Generative AI for
  Network Observability" — plausible AI Engineer fit.
- Daimler Truck AG, via JobTeaser — "Working Student, AI Applications,
  Software Development & Social Intranet," from March 2026 — broader fit,
  needs closer read against 26 Aug 2026 AI Engineer/AI Evaluation
  narrowing before treating as in-scope.

None of these were added to any watchlist file or Notion; they are quoted
here only from WebSearch snippet text, not verified against the full
posting.

## Watchlist

None scored this run (search halted before scoring).

## Dropped section

None dropped this run (search halted before filtering).

## Transparency block

- **Sources reachable this run:** WebSearch only (snippet-level).
- **Sources unreachable this run:** Tavily (MCP connection failure), Indeed
  connector (toggled off for chat), Firecrawl connector (toggled off for
  chat), WebFetch to every external domain tested including StepStone,
  Xing was not even reachable to test, JobTeaser, LinkedIn Jobs, Fraunhofer
  careers, Indeed, and neutral controls (Wikipedia, example.com) — this
  appears to be a session-wide network egress policy, not a per-site block.
- **Action needed from Rah:** enable the Indeed and/or Firecrawl connectors
  for this chat/session (Settings → Connectors, or the equivalent for the
  scheduled Cowork task), and/or check why Tavily's MCP is failing to
  dial, and/or confirm whether this session's network policy is intended
  to block general web access. Any one of these fixed would likely restore
  Step 4 for the next scheduled run.
- **Freshness dating notes:** n/a, no postings drafted.
- **Prompt-injection content observed but not acted on:** none observed.
- **Platform mix:** n/a, zero drafted this run.
- **Distance was not a scoring factor:** consistent with standing rule (n/a
  this run since nothing was scored).

## Deliverable summary

- Rows drafted this run: 0
- Files rendered: 0
- CSV rows appended: 0
- Notion rows created: 0
- Reconciliation writes: 0 (none needed, already clean)
- Backlog after run: 3 drafted in Notion (unchanged)
