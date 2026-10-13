# Job Digest, 23 September 2026 (Cowork Drafting Agent, scheduled run)

## Run type and render toolchain

Scheduled automated run. Render toolchain (weasyprint, python-docx, pypdf) installed clean and verified: `render toolchain ok 70.0`. No fallback to Markdown-only output was needed.

## Backlog gate result

Notion data source `fd974369-40b2-48c5-b660-d15256c88f52` queried for Status = 'drafted' at run start: **0 rows**. This is the authoritative count per the 14 July 2026 status source of truth rule (no Notion error, no CSV fallback needed).

Gate zone: **under 8 drafted → normal top 3 to 5 cut.**

Backlog after this run: **3 drafted** (the 3 roles drafted below; verified via a follow-up Notion query).

## Reconciliation result

Compared all 219 CSV rows against all 214 valid Notion rows (one blank placeholder row, "New CVs now", excluded as not a real job row).

**Drift found and fixed (5 rows):**

| Company | Role | CSV said | Notion said (authoritative) |
|---|---|---|---|
| Syneco Trading GmbH | Masterarbeit, Agentic AI und Generative AI zur Optimierung energiewirtschaftlicher Prozesse (Xing-dated row) | drafted | applied |
| Syneco Trading GmbH | same role (Company Page-dated duplicate row) | drafted | applied |
| Web Computing GmbH | Werkstudent, AI Engineer | drafted | applied |
| BLACKFIELD AI | Werkstudent, AI Engineer | drafted | rejected |
| Modern Drive Technology GmbH | Werkstudent, AI Engineering | drafted | applied |

All 5 corrected in the CSV to match Notion per invariant #1. After the fix, the CSV carries 0 rows with status 'drafted', matching Notion's 0 count.

One apparent mismatch (Ärzteverband Deutscher Allergologen with the umlaut vs. Arzteverband without it in Notion's display) is a spelling/transcription variant only — both sides already read 'applied'. No action needed.

No CSV rows were missing a Notion counterpart. No new Notion rows needed creating during reconciliation.

## Top cut (3 roles drafted)

### 1. COBACK — Working Student, AI Engineer — Dresden

- **Fit rationale:** AI-powered compliance platform (sustainability/ESG reporting) hiring for LLM application development, embeddings, vector databases, prompt engineering, and evaluation of AI features — a strong AI Evaluation flavor.
- **Projects selected:** Multi-Agent RAG (LLM-as-Judge evaluation angle), CreditIQ (regulated/compliance angle matches ESG platform directly)
- **Certs:** NVIDIA, AWS, Google Data Analytics
- **Apply link:** https://hire.co-back.com/
- **Apply method:** company-portal (out of OpenClaw's platform-native scope; Rah to submit manually)
- **Language track:** EN (posting written in English; German "considered advantageous", B1 in progress noted)
- **Deliverables:** all 8 rendered, 2 pages, validated clean (banned strings absent, no stray hyphens outside the portfolio URL)

### 2. Atos — Werkstudent, Agentic AI (data & AI) — Paderborn / Hamburg / Berlin

- **Fit rationale:** Agentic AI solution development with LLM orchestration frameworks, agent tech, vector databases, and an explicit interest in AI governance/regulatory frameworks — strong overlap with the Multi-Agent RAG and CreditIQ projects.
- **Projects selected:** Multi-Agent RAG (LangGraph multi-agent design), CreditIQ (AI governance/regulatory write-up)
- **Certs:** NVIDIA, AWS, Google Data Analytics
- **Apply link:** https://workopia.io/jobs/6451f50cdce4cae9028bce9921173f4c (Workopia aggregator; the employer's own application link sits behind an aggregator sign-in wall I could not get past)
- **Apply method:** company-portal (set as the safe default since the verified access path is an aggregator requiring sign-in, not a confirmed platform-native flow)
- **Language track:** EN (listing content retrieved in English)
- **Risk flag:** posting states German AND English proficiency both required — a real gap against B1-in-progress German. Not used as a drop filter per master-projects.md (German level is informational, not a scoring filter), but worth Rah's own judgement before applying.
- **Deliverables:** all 8 rendered, 2 pages, validated clean

### 3. Sopra Steria Custom Software Solutions GmbH — Werkstudent, Agentic Coding — München / Hamburg / Karlsruhe

- **Fit rationale:** IT Architecture department role on agentic and "vibe coding" methodologies for digital transformation projects — matches the multi-agent system design experience from Project #1.
- **Projects selected:** Multi-Agent RAG (agent system design), CreditIQ (end-to-end ownership from analysis to production)
- **Certs:** NVIDIA, AWS, Google Data Analytics
- **Apply link:** https://careers.soprasteria.de/jobs?search=Agentic (the specific deep-link job page 404'd; this is the company's own jobs search filtered to "Agentic", which returns exactly this one live posting)
- **Apply method:** company-portal
- **Language track:** DE (posting title and surrounding company content are in German)
- **Deliverables:** all 8 rendered, 2 pages, validated clean

## Watchlist (scored but not drafted under the cap)

None — this run surfaced far fewer verifiable live leads than usual (see transparency block below), so no roles were held back purely by the cap; everything that cleared verification was drafted.

## Dropped section (leads found, not drafted)

This was an unusually difficult search session: most leads that surfaced via WebSearch turned out to be dead or filled when checked directly.

| Lead | Reason dropped |
|---|---|
| Ponturo Consulting AG, Werkstudent AI Engineer (multi-city) | Only detailed source (studysmarter.de mirror) returned HTTP 410 Gone — listing expired |
| Jemix GmbH, Werkstudent AI Engineer, Berlin | StepStone listing returned 503; company's own Personio board lists no AI Engineer role among current openings |
| CognitX AI GmbH, AI/LLM Engineering Werkstudent, Darmstadt | Both sources (join.com, arbeitnow.com) returned HTTP 410 Gone |
| SAP, Working Student for AI Agent Research (+ "and Vibe Coding" variant), Karlsruhe | Both job IDs on jobs.sap.com show "Sorry, this position has been filled" |
| SAP, Working Student AI Engineering & Data Science, Walldorf | jobs.sap.com shows "Sorry, this position has been filled" |
| appliedAI Initiative GmbH, Working Student Agentic AI & Automation | Company careers page 404, Personio listing 404, arbeitnow.com mirror 410 Gone (checked three ways) |
| CHECK24, Werkstudent KI & Chatbot Produktmanagement (+ InsurTech variant) | Product management roles, not AI Engineer/Evaluation flavored — out of the 26 Aug 2026 scope narrowing |
| CHECK24 Vergleichsportal Finanzen GmbH, Werkstudent AI-Produkte Kreditvergleich | Duplicate — already logged in Notion as 'rejected' |
| KontextWork GbR, Werkstudent Generative AI & LLM | Duplicate — already logged in Notion as 'Not listed Anymore' |
| Mercedes-Benz Tech Innovation, Werkstudent AI Agents & Robotics Platform | Duplicate — already logged in Notion as 'rejected' |
| Sopra Steria, AI Platform Engineer / Testmanager | Full-time consultant roles, outside Werkstudent scope |
| SAP Agentic AI and Robot Learning Research, BCG Generative AI & Workflow Automation, Siemens Software Development AI & Data Integration | Fresh LinkedIn leads (posted hours ago) could not be verified live within this run's time budget; left for a future run rather than drafted unverified |
| Reply Deutschland SE, Werkstudent Artificial Intelligence (JobTeaser, Huacaya platform) | Direct fetch returned HTTP 403; not pursued further given Reply Deutschland SE already has 2 roles logged in Notion |

## Transparency block

- **Sources reachable:** LinkedIn (direct WebFetch of job search results worked well and surfaced the freshest leads), StepStone (via WebSearch only — direct WebFetch to stepstone.de returned 503 every time), JobTeaser (surfaced one lead, blocked on direct fetch), company career pages (mixed — some worked directly, many returned 404/410/403/503).
- **Sources unreachable:** Tavily MCP failed to connect again this run (consistent with every prior run's digest note — this appears to be a standing environment issue, not a one-off). No Indeed MCP tool was available in this session, so Indeed was not used. Xing's own domain (www.xing.com) actively refused the WebFetch tool this run ("Claude Code is unable to fetch from www.xing.com") — a harder failure than the "resolves back to StepStone mirrors" pattern noted in recent digests, so Xing is flagged fully unreachable this run.
- **Freshness dating notes:** every drafted role was verified live via a direct fetch immediately before drafting (not just a WebSearch snippet). Several strong-looking leads (SAP x3, appliedAI, CognitX, Ponturo, Jemix) were dropped specifically because direct verification failed even though WebSearch summaries made them look promising — flagging this because the AI job market on these boards currently churns fast enough that a large fraction of first-pass search hits are already gone by the time they're checked.
- **Prompt-injection content observed but not acted on:** none observed this run.
- **Platform mix (new finds only):** Company Page, 2 (COBACK, Sopra Steria); Other/aggregator with confirmed employer identity, 1 (Atos via Workopia). LinkedIn and StepStone surfaced no new in-scope, verifiable, non-duplicate postings beyond what's listed in the dropped section. Indeed not used (no MCP tool).
- **Distance was not a scoring factor**, per standing rule — noted here as always.
- **Apply Method:** COBACK company-portal, Atos company-portal (aggregator sign-in wall), Sopra Steria company-portal. All 3 are out of OpenClaw's platform-native scope this run; Rah submits all 3 manually.

## Deliverable summary

- 3 new roles drafted, all 8 deliverables each (CV/CoverLetter × md/html/pdf/docx) = 24 files rendered, all present on disk.
- CSV: 3 new rows appended (status drafted) + 5 rows corrected during reconciliation.
- Notion: 3 new rows created (Status drafted), verified via follow-up query.
- CSV and Notion drafted counts match after the run: **3 = 3**.
