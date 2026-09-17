# Job Digest, 16 September 2026

Run type: Scheduled Cowork run (Agent A, Cowork Drafting Agent).
Render toolchain: weasyprint 70.0, python-docx, pypdf installed cleanly this run. `import weasyprint, docx, pypdf` printed `render toolchain ok 70.0`. No fallback to Markdown-only needed.

## Backlog gate

Notion data source `fd974369-40b2-48c5-b660-d15256c88f52` returned **2 drafted rows** at run start (FZI Forschungszentrum Informatik and iLert GmbH, both carried over from the 11 September run, still awaiting OpenClaw's platform-native vs company-portal submission pass). No Notion errors, no CSV fallback needed.

2 drafted is under the 8 row floor of the 28 July 2026 yield reset rule → **normal top 3 to 5 cut** applied. 4 roles drafted this run.

Backlog after run: **6 drafted** in Notion (verified via follow-up query), matching 6 `drafted` rows in applied-log.csv.

## Reconciliation

Compared all 204 applied-log.csv rows against all 200 Notion rows (company + role, case insensitive).

- **1 drift found and fixed**: ProSiebenSat.1 Careers, "Working Student, AI Engineer" (Muenchen) was still `drafted` in the CSV but Notion carried it as `Not listed Anymore`. Per invariant 1 (Notion is the source of truth for row status), the CSV row was corrected to match Notion.
- No CSV rows missing from Notion, no Notion rows missing from the CSV (one apparent mismatch — "Ärzteverband" vs "Arzteverband Deutscher Allergologen" — is a spelling/umlaut variant only; both sides already read `applied`, no write needed).
- Reconciliation ran before the search/draft steps per the standing rule.

## Top cut (4 roles drafted)

### 1. Syneco Trading GmbH — Masterarbeit, Agentic AI und Generative AI zur Optimierung energiewirtschaftlicher Prozesse
- **Location:** Muenchen (Germany tier 1)
- **Source:** Xing · **Apply Method:** unset (pending OpenClaw) · **Language track:** DE
- **Apply link:** https://www.xing.com/jobs/muenchen-masterarbeit-agentic-ai-generative-ai-optimierung-energiewirtschaftlicher-prozesse-157808741
- **Fit rationale:** Masterarbeit investigating which recurring, manual processes in Bilanzkreis/Fahrplanmanagement can be supported or automated by generative and agentic AI systems, with a research question explicitly about *evaluating* those systems for efficiency, quality, robustness and implementation effort — squarely AI Engineer/AI Evaluation flavored under the 26 August narrowing.
- **Projects selected:** Multi Agent RAG (agentic, LLM as Judge evaluation) + Real Time Flight Tracking (Airflow orchestration/process automation)
- **Certs:** NVIDIA, AWS Academy, Google Data Analytics (DE)
- **Note:** posting did not state an explicit German level bar; Rah's B1 in progress is flagged as unconfirmed against the actual requirement.
- **Deliverables:** all 8 rendered, CV 2 pages, validation passed.

### 2. Charles Real Estate GmbH — AI Systems Engineer, Working Student
- **Location:** Berlin (Germany tier 1)
- **Source:** StepStone · **Apply Method:** unset (pending OpenClaw) · **Language track:** EN
- **Apply link:** https://www.stepstone.de/stellenangebote--AI-Systems-Engineer-Working-Student-m-f-d-Berlin-Charles-Real-Estate-GmbH--14112550-inline.html
- **Fit rationale:** Building AI powered applications, agents and automations; independent software architecture decisions; deploying production ready applications. Real estate investment company building an internal "AI-first operating system."
- **Projects selected:** Multi Agent RAG (agentic architecture, independent design decisions) + Movie Analytics and ML Pipeline (fully automated deployed cloud pipeline)
- **Certs:** NVIDIA, AWS Academy, Google Data Analytics (EN)
- **Deliverables:** all 8 rendered, CV 2 pages, validation passed.

### 3. Temedica GmbH — Working Student, AI and Agentic Engineering
- **Location:** Muenchen (Germany tier 1)
- **Source:** Company Page (Personio-hosted careers page; also listed on LinkedIn) · **Apply Method:** unset (pending OpenClaw) · **Language track:** EN
- **Apply link:** https://temedica.jobs.personio.de/job/2599740?language=en
- **Fit rationale:** Design/prototype/develop LLM based applications and AI agents in digital health, then evaluate and improve them for output quality, reliability, usability and safety in a **regulated healthcare environment** — strong overlap with CreditIQ's regulatory rigor.
- **Projects selected:** Multi Agent RAG (LLM as Judge evaluation) + CreditIQ (regulated, safety critical decision support, EU AI Act/GDPR compliance)
- **Certs:** NVIDIA, AWS Academy, Google Data Analytics (EN)
- **Deliverables:** all 8 rendered, CV 2 pages, validation passed.

### 4. SAP — Intern, Thesis or Working Student, Evaluating and Improving LLM based SE Solutions in SAP HANA
- **Location:** Walldorf (Germany tier 1)
- **Source:** Company Page (jobs.sap.com) · **Apply Method:** unset (pending OpenClaw) · **Language track:** EN
- **Apply link:** https://jobs.sap.com/job/Walldorf-InternThesisWorking-Student-%28fmd%29-Evaluating-and-Improving-LLM-based-SE-Solutions-in-SAP-HANA-69190/1427816733
- **Fit rationale:** Internal PhD-driven research project evaluating LLM usefulness on a 10M-line codebase (test generation, fault localization, LLM-as-a-judge, benchmarking). About as direct an "AI Evaluation" match as exists in this search.
- **Projects selected:** Multi Agent RAG (LLM as Judge, evaluation harness) + CreditIQ (rigorous testing, 100% branch coverage, benchmarked evaluation standard)
- **Certs:** NVIDIA, AWS Academy, Google Data Analytics (EN)
- **Note:** a third-party mirror showed an original post date of 19 August 2026 — this is an older but still-open posting, not a same-day find; ranked last on recency accordingly. SAP already has many prior applied-log/Notion rows under other titles; this specific role is not a duplicate under the company+role match rule.
- **Deliverables:** all 8 rendered, CV 2 pages, validation passed.

## Watchlist (scored but not drafted, capacity used at 4 of top 3–5)

None — 4 was the full set of roles that cleared verification this run under the normal cut; no additional in-scope, verified-live, non-duplicate roles were held back solely for capacity.

## Dropped

- **Retorio GmbH**, Working Student AI Engineer Agentic Systems (Munich, Xing) — same company and a near identical role already logged as `Not listed Anymore`; treated as a resurfaced repost, not a new opportunity.
- **EXXETA**, Werkstudent AI & LLM Engineering (Munich, Xing) — duplicates a role already logged as `rejected` (Werkstudent, AI und LLM Engineering).
- **appliedAI Initiative GmbH**, Working Student (m/f/x) Agentic AI & Automation (Munich) — same company and a near identical role already logged as `rejected` (Working Student, AI Engineering and Product Development).
- **Estateanfrage**, AI Engineer Trainee (Munich) — duplicates a role already logged as `rejected`.
- **Motius / eigenblue**, "Join our Tech Community as a Working Student — Backend Development & Agentic AI" (Munich, Xing) — on extraction this resolved to a generic talent pool funnel page with no defined task list or role scope, not a specific open position; dropped under invariant 4 (every write must be auditable).
- **Deutsche Börse Group**, Working Student — Data & AI Engineering (Frankfurt, JobTeaser / company career page) — content reads predominantly as Data Mesh implementation and data governance/quality support, with AI use cases mentioned only in passing; falls outside the 26 August 2026 AI Engineer / AI Evaluation narrowing (plain Data Engineering).
- **diconium GmbH**, Working Student AI Testing Platform (Ingolstadt, Xing) — considered but set aside in favour of the stronger Temedica match; scope reads closer to general software test tooling than AI engineering or evaluation.

## Transparency block

- **Sources reachable this run:** Tavily search + Tavily extract (used for StepStone, Xing, JobTeaser, LinkedIn, and direct company career pages). All reachable, no outages observed.
- **Sources not used:** No Indeed MCP tool was available in this session (consistent with prior runs); Tavily-based Indeed search also returned nothing new in scope, so Indeed contributed 0 roles this run (well under its 1-per-run cap, nothing to report there).
- **Freshness dating:** Syneco Trading posting carried its own "vor 5 Tagen" (~5 days old) marker on Xing. Charles Real Estate and Temedica postings had no explicit age marker but were confirmed live via direct fetch this run. SAP's posting showed an original post date of 19 August 2026 on a third-party mirror (jobware.de) — flagged above as an older but still-open listing.
- **Prompt injection:** none observed in any scraped posting content this run.
- **Platform mix:** Xing 1 (Syneco), StepStone 1 (Charles Real Estate), Company Page 2 (Temedica, SAP). LinkedIn and JobTeaser were searched but yielded only already-logged, off-scope, or non-actionable (talent-pool) leads once resolved to their actual posting.
- **Distance was not a scoring factor** — all 4 roles fall in the single "all of Germany" geographic tier per the standing rule; ranked by recency then Best-for overlap within that tier.
- **Target role scope:** all 4 roles confirmed in scope under the 26 August 2026 AI Engineer / AI Evaluation narrowing (2 explicit AI Evaluation flavored — Syneco Masterarbeit, SAP LLM evaluation research; 2 AI/Agentic Engineer flavored — Charles Real Estate, Temedica).

## Deliverable summary

- 4 new roles drafted, all 8 deliverables each (CV .md/.html/.pdf/.docx + CoverLetter .md/.html/.pdf/.docx) — verified present on disk.
- All 4 CVs passed the STEP 4 validation gate: 2 pages each, no banned strings (`toward B2`, `Databricks`, `Delta Lake`, `LangChain`, `PyTorch`), no retired PD-layout strings on page 1, Ojas-style header confirmed by absence of those strings.
- CSV drafted count: 6. Notion drafted count: 6 (verified via follow-up query). Match confirmed.
- 1 reconciliation drift found and fixed (ProSiebenSat.1 Careers CSV status corrected to match Notion).
