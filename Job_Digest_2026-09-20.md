# Job Digest — 20 September 2026 (Cowork Scheduled Run)

## Run type and render toolchain

Scheduled Cowork drafting run (Agent A). Render toolchain installed clean:
`pip install weasyprint python-docx pypdf` succeeded, `import weasyprint,
docx, pypdf` printed `render toolchain ok 70.0`. No fallback to
Markdown-only output was needed.

## Backlog gate result

Notion data source `fd974369-40b2-48c5-b660-d15256c88f52` returned **10**
rows in Status `drafted` at run start (authoritative count, no fallback to
CSV needed). Per the 28 July 2026 yield reset gate, 10 drafted falls in the
**8 to 10 zone**, which caps this run at the **top 3** (not the normal top
3 to 5, and not a hard pause). After this run's 3 new drafts, backlog is
**13 drafted** in Notion (verified via a follow-up count query).

## Reconciliation result

Compared all 212 applied-log.csv rows against 207 Notion rows carrying a
Company plus Role value (the data source's 208th row, "New CVs now", is an
internal placeholder with no Company/Role and was excluded).

- **3 real Status drift rows found and fixed** (CSV updated to match
  Notion per invariant 1, Notion is the source of truth):
  - Mercedes-Benz AG, Werkstudent Data Analytics and Projektsteuerung
    MB.OS — CSV said `applied`, Notion said `rejected` → CSV corrected to
    `rejected`.
  - Mercedes-Benz Tech Innovation, Werkstudent AI Agents and Robotics
    Platform — CSV said `applied`, Notion said `rejected` → CSV corrected
    to `rejected`.
  - Mercedes-Benz Tech Innovation, Werkstudent Machine Learning
    Engineering — CSV said `applied`, Notion said `rejected` → CSV
    corrected to `rejected`.
- **1 apparent "missing from Notion" row, confirmed a false positive:**
  Ärzteverband Deutscher Allergologen (Werkstudent, Data Science) appeared
  missing only because Notion's SQL text mode strips the umlaut
  (`Arzteverband`). A direct `LIKE '%Allerg%'` lookup confirmed the row
  exists in Notion with a matching `applied` status. No new row created;
  this is the same known spelling variant flagged in prior digests.
- No reverse-direction writes were made (CSV never overwrote Notion).

## Top cut (3 new drafts, capped by the 8–10 backlog gate)

### 1. Control Expert GmbH — Working Student QA Engineer, AI / LLM Systems
- **Location:** Langenfeld (Rheinland), NRW
- **Source:** StepStone
- **Language track:** EN (posting title and requirements entirely in
  English; requires good communication in German and English, not a hard
  fluency bar)
- **German level required:** not a hard bar; compatible with current B1
- **Fit rationale:** Squarely AI Evaluation — tests and evaluates an
  Agentic AI team's LLM and agent-based systems (multi-step reasoning,
  tool use, decision-flow test design).
- **Projects selected:** Multi-Agent RAG (LLM-as-Judge evaluation harness,
  9-metric retrieval/generation suite), CreditIQ (100% branch coverage,
  SHAP-driven bias detection)
- **Certs:** NVIDIA (led), AWS, Google Data Analytics
- **Apply Link:** stepstone.de listing (id 14186197)
- **Apply Method:** unset, pending OpenClaw's platform-native vs
  company-portal check
- **Deliverables:** all 8 rendered, CV 2 pages, all validation gates
  passed

### 2. FUNKE Mediengruppe — Werkstudent Workflow Automation n8n, Agentic AI
- **Location:** Hamburg
- **Source:** StepStone
- **Language track:** DE (German posting title, German media company)
- **Fit rationale:** Agentic AI Engineer — orchestrates LLM agents via
  n8n, supports buildout of an internal Agentic AI platform.
- **Projects selected:** Multi-Agent RAG (LangGraph multi-agent design,
  bounded per-agent responsibility), Real-Time Flight Tracking (Airflow
  orchestration, 15-minute unattended refresh)
- **Certs:** NVIDIA, AWS, Google Data Analytics
- **Apply Link:** stepstone.de listing (id 13397936)
- **Apply Method:** unset, pending OpenClaw's check
- **Deliverables:** all 8 rendered, CV 2 pages, all validation gates
  passed

### 3. Vector Informatik GmbH — Werkstudent, AI driven CI/CD Automation
- **Location:** Stuttgart / Karlsruhe
- **Source:** JobTeaser
- **Language track:** DE (German posting title, German engineering
  company)
- **Fit rationale:** AI Engineer plus evaluation blend — integrates AI
  agents into CI pipelines for automatic log/artifact evaluation, builds
  AI-based classification of build/test failures. Onsite presence
  required, no pure remote option (still within the standing Germany
  geography filter).
- **Projects selected:** Multi-Agent RAG (EvalAgent automated metric
  computation), Movie Analytics and ML Pipeline (fully automated Cloud
  Scheduler pipeline, 0 manual interventions)
- **Certs:** NVIDIA, AWS, Google Data Analytics
- **Apply Link:** jobteaser.com listing
- **Apply Method:** unset, pending OpenClaw's check (JobTeaser listing
  points at a company-owned careers domain, likely company-portal shaped)
- **Deliverables:** all 8 rendered, CV 2 pages, all validation gates
  passed

## Watchlist (scored but not drafted under the top-3 cap)

- **Modern Drive Technology GmbH**, Werkstudent AI Engineering (Neumarkt
  in der Oberpfalz, LinkedIn) — genuinely AI-focused (LLM agents,
  automation workflows) but requires **verhandlungssicheres Deutsch**
  (business-fluent) for onsite process interviews with users, a hard
  requirement well above the current B1-in-progress level. Dropped on
  German-level mismatch, not scope.
- **Reply Deutschland SE**, Werkstudent AI Business Solutions and Agents
  — centres on Microsoft Copilot Studio / Power Platform citizen
  development rather than model or agent engineering; weaker fit than the
  3 drafted roles.
- **Ponturo Consulting AG**, Werkstudent AI Engineer (multi-city) —
  plausible fit, but the only mirror found (StudySmarter) returned HTTP
  410 Gone and no first-party ponturo.com posting could be reached this
  run. Left for re-verification on a future run rather than drafted
  without independent evidence (invariant 4).

## Dropped (closed, filled, or out of scope)

- **KLUGSYS**, Werkstudent Agentic AI Engineer (Aachen area) — posting's
  own notice: "Es werden keine Bewerbungen mehr angenommen" (closed).
- **AKDB**, Werkstudent Workflow Automation and Agentic AI (Köln) — own
  careers page returned HTTP 410 Gone (closed).
- **SAP Walldorf**, Working Student AI-based Quality Evaluation for
  AI-Generated Code Changes (SAP HANA Cloud) — jobs.sap.com shows "Sorry,
  this position has been filled." (Different requisition than the SAP
  Walldorf LLM SE Solutions role already drafted 16 September.)
- **predori**, Werkstudent NLP/LLM Engineer — own careers page returned
  HTTP 404; only dateable evidence found was an October 2025 posting date,
  roughly 11 months stale. Dropped as likely expired.
- **EY-Parthenon**, Werkstudent AI and GenAI (Strategy and Transactions)
  — reads as strategy consulting using AI tooling, not AI engineering or
  evaluation build work. Out of scope under the 26 August 2026 narrowing.

## Transparency block

- **Search tool availability:** the Tavily MCP server failed to connect
  the entire run (`SdkHttpError`, `CLIENT_HTTP_NOT_IMPLEMENTED`). No
  Indeed MCP tool was available. All search relied on the built-in
  WebSearch tool.
- **WebFetch reachability:** worked for LinkedIn job-view pages and
  several first-party company/ATS domains (jobs.sap.com rendered real
  content; a ponturo StudySmarter mirror returned a real 410; predori.com
  returned a real 404). **WebFetch returned 403 or 503 on every direct
  stepstone.de and jobteaser.com URL attempted this run**, consistent with
  the EGRESS_BLOCKED pattern the 9–18 September digests already logged
  for those two domains.
- **Evidence standard for the 3 drafted roles:** because all 3 live on
  blocked domains (2 StepStone, 1 JobTeaser), verification relied on
  WebSearch result snippets only, not a direct fetch of the full original
  posting text. This is a weaker evidence standard than prior runs that
  had Tavily search+extract available, and is flagged here per invariant
  5. Language track for all 3 was inferred from posting title language and
  company profile rather than confirmed via a full body read.
- **Platform mix:** StepStone 2, JobTeaser 1. LinkedIn, Xing, and company
  career pages were also searched via WebSearch; they surfaced only
  already-logged, closed, or out-of-scope leads (see Dropped section).
  Indeed was not used (no MCP tool, no in-scope WebSearch result).
- **Freshness:** none of the 3 postings carried a confirmable exact post
  date within the WebSearch snippet evidence available; all 3 were
  confirmed currently listed and accepting applications. All 3 fall in the
  single Germany geographic tier; ordered by Best-for project overlap as
  tiebreaker since no further recency signal was available.
- **Distance was not a scoring factor**, per standing rule.
- **No prompt-injection content observed** in any search result or
  fetched page this run.

## Deliverable summary

- 3 new roles drafted, all 8 deliverables each (CV .md/.html/.pdf/.docx,
  CoverLetter .md/.html/.pdf/.docx) = 24 files rendered, all present on
  disk.
- All 3 CV PDFs: 2 pages, no banned strings (`toward B2`, `Databricks`,
  `Delta Lake`, `LangChain`, `PyTorch`), no retired PD-layout strings
  (`PERSONAL DETAILS`, `Portfolio:`, `Date of birth`, `Nationality:`,
  `Availability:`, `Hindi:`) on page 1. Ojas-style header confirmed on all
  3.
- applied-log.csv: 3 new rows appended (drafted), 3 rows corrected via
  reconciliation. Total CSV rows now 215.
- Notion: 3 new rows created under Status `drafted`, verified via
  follow-up count query (10 → 13 drafted).
- Git: pending commit and push to
  `claude/scheduled-run-2026-09-20` (see commit step).
