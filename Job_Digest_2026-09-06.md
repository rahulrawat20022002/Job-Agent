# Job Digest, 6 September 2026

Run type: Scheduled Cowork Drafting Agent (Agent A), normal top 3 cut.
Render toolchain: weasyprint 69.0, python-docx, pypdf installed clean on
this run's fresh checkout. `import weasyprint, docx, pypdf` printed
"render toolchain ok 69.0". No fallback to Markdown-only output needed.

## Backlog gate

Notion data source `fd974369-40b2-48c5-b660-d15256c88f52` queried directly
(no retry needed): **0 rows in Status = 'drafted'** at run start. Under the
28 July 2026 yield reset, 0 drafted falls in the under-8 zone: normal top
3 to 5 cut. This run drafted 3.

Backlog after this run: **3 drafted** in Notion (verified by a follow-up
query after the writes; see Deliverable summary below).

## Reconciliation

Read all 186 pre-run rows of `applied-log.csv` and matched each against
Notion by company plus role, case insensitive, per the 14 July 2026 status
source of truth rule.

- **Drift found and fixed (3 rows):** Mercedes-Benz Tech Innovation
  (Werkstudent, AI Agents and Robotics Platform), Beilmann Marketing GmbH
  (Werkstudent, KI Automatisierung und interne Tools), and ETG-Elektronik
  GmbH (Praktikant or Werkstudent, AI Systems and Generative AI) were all
  logged as `drafted` in the CSV but Notion already showed `applied` for
  all three (OpenClaw evidently ran a submission pass since the 5
  September run). The CSV was corrected to `applied` for all three,
  matching Notion. No reverse writes were made.
- **False-positive checked and cleared:** one row
  (Ärzteverband/Arzteverband Deutscher Allergologen) initially looked like
  a CSV/Notion mismatch but was only an umlaut encoding difference between
  the two systems referring to the same row; no write needed.
- **No missing rows either direction:** every other CSV row has a matching
  Notion row with the same status, and no Notion row lacked a CSV
  counterpart.

Reconciliation ran before the backlog gate check per the standing
instruction that it runs even on paused runs.

## Top cut (3 new drafted roles)

### 1. Mi-Jack Europe GmbH — Pflichtpraktikant, Entwicklung von AI Agents
- **Location:** Karlsruhe (homeoffice possible)
- **Source:** StepStone, posted 1 week ago, "Verifiziert"
- **Work type:** Pflichtpraktikum (mandatory internship), full time, minimum 6 months
- **Language track:** DE (posting fully in German)
- **Fit rationale:** Tasks are almost entirely AI agent evaluation —
  designing test cases and evaluation metrics for AI agents, judging
  factual accuracy/consistency/reliability, hallucination analysis, safety
  and guardrail testing, automated test scripts and bug reports. This maps
  closely onto the JudgeAgent (5-dimension scoring, hard failure on
  missing judge model to prevent silent self-judging) and EvalAgent work
  in the Multi Agent RAG project, plus the systematic SHAP-driven bias
  audit in CreditIQ.
- **Projects selected:** Multi Agent RAG with LLM as Judge, CreditIQ
- **Certs:** NVIDIA, AWS Academy, Google Data Analytics (DE track order)
- **Apply link:** stepstone.de listing 13907202
- **Apply method:** platform-native (StepStone Schnelle Bewerbung, in OpenClaw's automated scope)
- **Deliverables:** all 8 rendered, CV 2 pages, CL 1 page, validation gate passed
- **Transparency:** posting asks for "sichere Kommunikation in Deutsch und Englisch," above current B1 in progress; flagged openly in the cover letter's closing paragraph.

### 2. appliedAI Initiative GmbH — Working Student, AI Engineering and Product Development
- **Location:** Munich (House of Communication) or Heilbronn (IPAI), hybrid
- **Source:** Company career page (appliedai.de), no posting-age indicator shown
- **Work type:** Working Student (Werkstudent-equivalent)
- **Language track:** EN — the posting's section labels ("Ueber uns,"
  "Deine Aufgaben," "Dein Profil") are German, but every substantive
  sentence describing tasks, requirements, and benefits is written in
  English, so per the 20 July 2026 language match rule the body language
  (English) is the deliverable language.
- **Fit rationale:** Building and testing AI agent functionality in
  Python with LangChain/Azure AI Foundry, plus maintaining an internal
  "maturity assessment tool," maps directly onto the LangGraph multi-agent
  orchestration and JudgeAgent scoring work in the RAG project, and the
  CreditIQ Streamlit tool that turns a technical audit into something a
  non-technical stakeholder can use.
- **Projects selected:** Multi Agent RAG with LLM as Judge, CreditIQ
- **Certs:** NVIDIA, AWS Academy, Google Data Analytics (EN track order)
- **Apply link:** appliedai.jobs.personio.de/job/2690896
- **Apply method:** company-portal (Personio-hosted form), out of OpenClaw's platform-native scope; Rah applies manually
- **Deliverables:** all 8 rendered, CV 2 pages, CL 1 page, validation gate passed
- **Transparency:** posting asks for "proficiency in German and English," above current B1 in progress; flagged openly in the cover letter's closing paragraph.

### 3. KontextWork GbR — Werkstudent, KI Engineer Generative KI und LLM
- **Location:** Hannover
- **Source:** StepStone, posted about 1 month ago (older listing, still live and accepting applications at run time)
- **Work type:** Werkstudent, 16 to 20 hours per week
- **Language track:** DE (posting fully in German)
- **Fit rationale:** Building RAG systems, integrating LLMs into an
  existing knowledge system (Drupal Wiki), and automating workflows maps
  onto the multilingual RAG retrieval pipeline and the fully automated
  0-manual-intervention batch pipeline in the Movie Analytics project.
  Automation-tool experience (Make/Zapier/n8n) is not something Rah has
  hands-on, and the cover letter says so plainly rather than implying it.
- **Projects selected:** Multi Agent RAG with LLM as Judge, Movie Analytics and ML Pipeline
- **Certs:** NVIDIA, AWS Academy, Google Data Analytics (DE track order)
- **Apply link:** stepstone.de listing 13730672
- **Apply method:** platform-native (StepStone Schnelle Bewerbung, in OpenClaw's automated scope)
- **Deliverables:** all 8 rendered, CV 2 pages, CL 1 page, validation gate passed
- **Transparency:** listing is roughly a month old; drafted anyway since it remained live and accepting applications, flagged here for visibility in case it has quietly filled.

## Watchlist (scored but not drafted)

- **Mercedes-Benz Group — Intern Enterprise Data & AI Architecture
  (Mandatory Internship), Stuttgart** (Xing). Mandatory internship, in
  scope as a work type, but the role itself reads as data-and-AI
  architecture and governance (stakeholder presentations, architecture
  artefacts, metadata governance) rather than hands-on AI Engineering or
  AI Evaluation work per the 26 August 2026 scope narrowing. One
  deep-dive project option mentions LLM-based knowledge base automation,
  keeping it borderline; left for Rah's judgment rather than drafted.
- **Fraunhofer Heinrich Hertz Institute HHI — Werkstudent*in Erklaerbare
  KI, Berlin** (LinkedIn, surfaced via Tavily search, posted about 3 days
  ago). Explainable AI is squarely in the AI Evaluation space and would
  likely have scored well, but the LinkedIn posting could not be fetched
  by any tool available this run (de.linkedin.com is blocked by the
  sandbox's egress proxy, and Tavily's extractor did not return content
  for this specific URL). Per invariant #3, not drafted without a verified
  posting; flagged here for Rah to check directly if interested.
- **"Werkstudent Agentic AI (Data & AI)"** surfaced via a wearedevelopers.com
  search result; the listing returned "Job Not Found" on fetch (already
  removed). Dropped rather than drafted.
- **EVEX Deutschland GmbH — Werkstudent AI Engineering & Developer
  Productivity, Stuttgart.** Found via Bundesagentur fuer Arbeit mirror
  sites; the original listing (fox8.com mirror) explicitly shows "This job
  has expired," originally posted 27 August. Dropped as stale.
- **bundesweit.digital GmbH — Werkstudent*in KI Prompting/Prompt-Engineer,
  Hanover.** The StepStone URL returned a 404 "Seite nicht gefunden."
  Dropped as stale/removed.

## Dropped (filtered before scoring)

- **Rosenberger Hochfrequenztechnik GmbH & Co. KG — Werkstudent fuer
  KI-Projekte, Fridolfing.** Already logged in Notion/CSV with Status
  `applied`; the same posting resurfaced in this run's search. Dropped as
  a duplicate, not re-drafted.
- General Data Engineer / Data Analyst / Business Analyst / plain Data
  Scientist postings surfaced incidentally in broader searches (e.g. NXP
  Semiconductors AI Automation Engineer — Quality Automation, several
  Werkstudent Data & AI Analytics listings) were not scored against the
  narrowed 26 August 2026 AI Engineer / AI Evaluation target and were
  excluded at the filter stage.

## Transparency block

- **Sources reachable this run:** Tavily web search (general), Tavily
  `tavily_extract` (successfully retrieved full StepStone, company career
  page, and Bundesagentur-mirror content). Company career pages reachable
  via Tavily.
- **Sources partially blocked:** direct `WebFetch` to `www.stepstone.de`
  and `de.linkedin.com` both failed with `EGRESS_BLOCKED` from this
  sandbox's network proxy. StepStone content was still retrieved
  successfully via `tavily_extract` as a workaround. LinkedIn direct-page
  content could not be retrieved by any available tool this run; one
  LinkedIn lead (Fraunhofer HHI) is on the watchlist as a result rather
  than fabricated or guessed at.
- **Sources not available at all:** no Indeed MCP tool is present in this
  environment; Indeed coverage this run was limited to Tavily's
  `site:indeed.com` / `de.indeed.com` web search, which surfaced no new
  in-scope postings. 0 Indeed rows this run (well under the 1-per-run cap).
- **JobTeaser:** searched, no new in-scope AI Engineer / AI Evaluation
  postings surfaced this run (only unrelated project-management and PhD
  listings came back).
- **Xing:** searched directly and via general web search; the one
  AI-Engineer-scoped in-scope lead found (Mercedes-Benz Group Enterprise
  Data & AI Architecture internship) is on the watchlist rather than
  drafted, per the fit rationale above.
- **No prompt injection content observed** in any fetched posting or
  search result this run.
- **Platform mix:** StepStone 2, Company Page 1, Indeed 0, Xing 0 (search
  attempted, no draft), LinkedIn 0 (search attempted, blocked on fetch),
  JobTeaser 0 (search attempted, no in-scope match).
- **Language track decisions:** 2 DE (Mi-Jack Europe, KontextWork), 1 EN
  (appliedAI, based on substantive body language despite German section
  headers).
- **Distance was not a scoring factor**, per standing rule; all three
  roles are within Germany (Karlsruhe, Munich/Heilbronn, Hannover).
- **SS Engineers and Contractors experience section:** `SHOW_SS_ENGINEERS_EXPERIENCE`
  left at its default `True` this run, per standing instruction that
  Cowork never changes this switch on its own judgement.
- **Bachelor Thesis / Research and Thesis section:** `SHOW_BACHELOR_THESIS`
  left at its default `False` this run, per standing instruction.

## Deliverable summary

- 3 new roles drafted, 24 files rendered (8 deliverables x 3 roles), all
  verified present on disk.
- CSV drafted-count and Notion drafted-count both confirmed at 3 after
  this run's writes.
- All 3 CV PDFs passed the 19 August 2026 validation gate: exactly 2
  pages each, no banned strings ("toward B2", "Databricks", "Delta Lake",
  "PyTorch") anywhere in the document, and no retired PD-layout strings
  ("PERSONAL DETAILS", "Portfolio:", "Date of birth", "Nationality:",
  "Availability:", "Hindi:") on page 1.
- All 3 cover letter PDFs rendered at 1 page.
