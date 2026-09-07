# Job Digest, 7 September 2026

Run type: Scheduled Cowork run (Agent A). Render toolchain: weasyprint 69.0, python-docx, pypdf installed clean, `import weasyprint, docx, pypdf` printed `render toolchain ok`. No Markdown-only fallback needed.

## Backlog gate

Notion data source `fd974369-40b2-48c5-b660-d15256c88f52` queried for `Status = 'drafted'` at run start: **0 rows**. No retry fallback to CSV needed (Notion reachable on first query).

0 drafted falls under the 8 row floor of the 28 July 2026 yield reset rule: **normal top 3 to 5 gate applied.** 4 roles drafted this run. Backlog after this run: **4 drafted in Notion.**

## Reconciliation (14 July 2026 status source of truth, 11 July 2026 reconciliation rule)

Notion is the source of truth; CSV was checked row by row against Notion by company plus role, case insensitive.

- **Drift found and fixed (3 rows):** CSV had these three still at `drafted`, Notion already showed `applied` (OpenClaw submitted them since the last Cowork run):
  - Mercedes-Benz Tech Innovation, Werkstudent AI Agents and Robotics Platform, drafted to applied
  - Beilmann Marketing GmbH, Werkstudent KI Automatisierung und interne Tools, drafted to applied
  - ETG-Elektronik GmbH, Praktikant or Werkstudent AI Systems and Generative AI, drafted to applied
- **CSV rows backfilled from Notion (4 rows):** Notion had 4 rows with no CSV counterpart at all: Mi-Jack Europe GmbH (applied), appliedAI Initiative GmbH (applied), KontextWork GbR (Not listed Anymore), Rohde und Schwarz GmbH und Co. KG, Werkstudent Agentic AI Experiments, Teisnach (applied). Backfilled into the CSV mirror with Notion's status, location, source, and draft path. Their original Date Drafted could not be verified from any source available in this checkout (no matching `drafts/` folders or git history for those rows), so the date column was left blank for these 4 rather than fabricating a date, per invariant 3 (never fabricate).
- No reverse writes made from CSV to Notion.

## Top cut, 4 roles drafted

All four are Werkstudent roles, Germany geographic tier, AI Engineer scope per the 26 August 2026 narrowing. Full deliverable set (CV and CoverLetter each as .md, .html, .pdf, .docx) rendered via `build_html.py` for every role; no hand written CV or cover letter text.

### 1. Mercedes-Benz Tech Innovation, Werkstudent Machine Learning Engineering, Karlsruhe
- **Fit rationale:** Role develops LLMs into multimodal audio/vision models, builds data/training/evaluation pipelines in the cloud, fine tunes base models, and works with RAG, tool calling, and agentic behaviour. Near one to one match to the Multi Agent RAG project's LLM as Judge evaluation harness and training/eval pipeline work.
- **Projects selected:** Multi Agent RAG (DE), Movie Analytics and ML Pipeline (DE)
- **Certs:** NVIDIA, AWS Academy, Google Data Analytics (DE)
- **Apply link:** stepstone.de listing 14400316 (routes to Mercedes-Benz's own Workday careers flow)
- **Apply method:** company-portal
- **Language track:** DE. Posting asks "gute Deutsch- und Englischkenntnisse", a step above current B1 in progress; cover letter is upfront about this.
- **Deliverables:** all 8 rendered, PDF validated at 2 pages, no banned strings.

### 2. Generali Deutschland AG, Werkstudent Machine Learning Engineering, Saarbruecken
- **Fit rationale:** Machine Learning Engineering team building generative AI based chatbots and agents in the Analytics and AI department. Matches the RAG project's agent orchestration and CreditIQ's experience shipping a regulated, fairness audited decision support tool at an insurer style institution.
- **Projects selected:** Multi Agent RAG (DE), CreditIQ (DE)
- **Certs:** NVIDIA, AWS Academy, Google Data Analytics (DE)
- **Apply link:** xing.com/jobs/saarbruecken-werkstudent-machine-learning-engineering-155911815
- **Apply method:** platform-native (Xing Easy Apply)
- **Language track:** DE, no explicit CEFR bar stated.
- **Deliverables:** all 8 rendered, PDF validated at 2 pages, no banned strings.

### 3. EXXETA, Werkstudent AI und LLM Engineering, Muenchen
- **Fit rationale:** Consulting firm building generative AI, LLM, and ML solutions at the intersection of technology, strategy, and business. Matches the RAG project's end to end delivery and CreditIQ's business translation angle (fairness requirement to shipped decision tool).
- **Projects selected:** Multi Agent RAG (DE), CreditIQ (DE)
- **Certs:** NVIDIA, AWS Academy, Google Data Analytics (DE)
- **Apply link:** xing.com/jobs/muenchen-werkstudent-ai-llm-engineering-all-genders-156675659 (also listed on Indeed by the same employer; Xing kept as canonical Apply Link)
- **Apply method:** platform-native (Xing Easy Apply)
- **Language track:** DE, no explicit CEFR bar stated.
- **Deliverables:** all 8 rendered, PDF validated at 2 pages, no banned strings.

### 4. Merantix Momentum, Working Student AI Full Stack Engineer, Berlin
- **Fit rationale:** Berlin AI startup, Full Stack team shipping real production code for AI powered applications. Matches the RAG project's production discipline plus two years of full time React experience (SS Engineers and Contractors), giving genuine full stack range beyond a notebook demo.
- **Projects selected:** Multi Agent RAG (EN), Movie Analytics and ML Pipeline (EN)
- **Certs:** NVIDIA, AWS Academy, Google Data Analytics (EN)
- **Apply link:** careers.merantix-aicampus.com, Working Student AI Full Stack Engineer listing
- **Apply method:** company-portal (Merantix AI Campus careers site, not an aggregator flow)
- **Language track:** EN, posting body entirely in English, no German requirement stated.
- **Deliverables:** all 8 rendered, PDF validated at 2 pages, no banned strings.

## Watchlist (scored but not drafted, at the 4 of 5 cap)

None held back this run; all 4 strong candidates found were drafted (under the top 3 to 5 cap, no need to hold any back for a future run).

## Dropped

- **Kenbun IT AG, Werkstudent Data Science und Deep Learning, Karlsruhe (StepStone):** Reviewed and dropped. Core task is quality review of French audio and text data, requiring near native French at C2 level; machine learning evaluation is listed only as an optional stretch topic if the candidate is interested. Does not read as an AI Engineer or AI Evaluation role under the 26 August 2026 scope narrowing, and Rah does not hold C2 French.
- **BMW Group, Intern AI Platform and Agentic Architecture Engineer, Muenchen (JobTeaser/LinkedIn):** Considered but not drafted this run. Listed as "Intern" rather than BMW's usual Werkstudent/Praktikant framing; could not confirm from the posting whether it satisfies the mandatory Pflichtpraktikum work type requirement or is a voluntary international internship track, which is out of scope. Flagged here for Rah's judgment rather than drafted on an unverified assumption.
- Reply Deutschland SE, Werkstudent Artificial Intelligence, Frankfurt (JobTeaser): appears to be the same underlying opening as the already logged and applied Reply Deutschland SE, Werkstudent fuer AI Data Engineering und Tool Entwicklung row (same employer, overlapping AI/Data Engineering scope, multiple near identical Reply postings across cities); not redrafted to avoid a likely duplicate application.
- General duplicates skipped without further note: any posting matching a company plus role combination already present in applied-log.csv or Notion (checked for all 4 candidates before drafting).

## Transparency block

- **Sources reachable this run:** Tavily search (used for StepStone, Xing, LinkedIn, and JobTeaser listings, since direct WebFetch to stepstone.de and xing.com is blocked by this session's network egress proxy; `tavily_extract` was used instead to pull full job description text from the 4 shortlisted postings), company career pages (Merantix AI Campus, Mercedes Benz Workday).
- **Sources unreachable or not used this run:** Direct WebFetch to stepstone.de (EGRESS_BLOCKED) and xing.com (fetch unavailable); worked around via Tavily search and tavily_extract instead, so no source was actually skipped. No dedicated Indeed MCP tool was available in this session; Indeed coverage this run came from Tavily search results only, and no in scope, non duplicate Indeed candidate surfaced. LinkedIn and JobTeaser were both searched via Tavily; JobTeaser in particular surfaced no new in scope, non duplicate AI Engineer or AI Evaluation candidate this run (results were either duplicates of already logged Reply postings or out of scope full time and non Germany roles).
- **Freshness dating:** all 4 drafted postings showed "posted" or "vor X Tagen" timestamps within roughly the last 1 to 2 weeks at search time (7 September 2026); exact original post dates were not independently re-verified beyond the platform's own listing metadata.
- **Prompt injection or unusual content:** none observed in any fetched job posting or search result this run.
- **Platform mix this run:** StepStone 1, Xing 2, Company Page 1 (Merantix AI Campus). LinkedIn, JobTeaser, Indeed searched but yielded 0 usable new candidates this run for the reasons above.
- **Language track decisions:** 3 of 4 roles DE track (posting body in German), 1 of 4 EN track (Merantix Momentum, posting body entirely in English), per the 20 July 2026 language match rule.
- **Apply method per role:** 2 platform-native (Generali via Xing, EXXETA via Xing, in OpenClaw's automated scope), 2 company-portal (Mercedes-Benz Tech Innovation via Workday, Merantix Momentum via the Merantix AI Campus careers site).
- **Distance was not a scoring factor**, per the standing rule; all 4 roles are in the Germany geographic tier (Karlsruhe, Saarbruecken, Muenchen, Berlin).
- **19 August 2026 CV content rules:** all 4 CVs validated for the 2 page hard cap, absence of the 5 banned strings (toward B2, Databricks, Delta Lake, LangChain, PyTorch), and absence of the 6 retired PERSONAL DETAILS block strings on page 1. All pass.
- **SHOW_SS_ENGINEERS_EXPERIENCE:** left at its default `True` (not touched this run). **SHOW_BACHELOR_THESIS:** left at its default `False` (not touched this run).

## Deliverable summary

- 4 new roles drafted, 32 files rendered (8 deliverables x 4 roles), all verified present on disk.
- CSV: 3 status corrections (drafted to applied), 4 backfilled mirror rows, 4 new drafted rows appended. Total CSV rows: 194.
- Notion: 4 new pages created under data source `fd974369-40b2-48c5-b660-d15256c88f52`, verified present via a follow up query for `Status = 'drafted'`.
- CSV and Notion drafted counts confirmed matching after the run: 4 and 4.
