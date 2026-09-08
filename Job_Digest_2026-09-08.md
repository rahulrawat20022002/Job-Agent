# Job Digest — 8 September 2026

**Run type:** Scheduled Cowork Drafting Agent (Agent A) run.
**Render toolchain:** weasyprint 69.0, python-docx, pypdf installed clean. `import weasyprint, docx, pypdf` printed `render toolchain ok 69.0`. No fallback to Markdown-only needed.

---

## Backlog gate result

Queried Notion data source `fd974369-40b2-48c5-b660-d15256c88f52` for `Status = 'drafted'` at run start: **0 rows**. No retry needed (Notion answered on the first query).

0 drafted is well under the 8-row floor of the 28 July 2026 yield reset, so the **normal top 3 to 5 cut** applied. Search yielded exactly **1** role that survived verification (see Transparency block for why the yield was this thin). Backlog after this run: **1 drafted** in Notion.

## Reconciliation result

Read all 198 rows in `applied-log.csv` and matched each against Notion by company + role, case-insensitive. Notion is the source of truth for Status (14 July 2026 rule).

**Drift found and fixed (10 rows, CSV updated to match Notion, no reverse writes):**

| Company | Role | CSV said | Notion says (now applied to CSV) |
|---|---|---|---|
| Fraunhofer-Institut fuer Optronik... IOSB | Abschlussarbeit, Training Data Anonymization... | applied | rejected |
| Kaufland | Praktikant, Data Science | applied | rejected |
| Mercedes-Benz Tech Innovation | Werkstudent, Machine Learning Engineering | drafted | applied |
| Generali Deutschland AG | Werkstudent, Machine Learning Engineering | drafted | applied |
| EXXETA | Werkstudent, AI und LLM Engineering | drafted | applied |
| Merantix Momentum | Working Student, AI Full Stack Engineer | drafted | applied |
| Mi-Jack Europe GmbH | Pflichtpraktikant, Entwicklung von AI Agents | drafted | applied |
| appliedAI Initiative GmbH | Working Student, AI Engineering and Product Development | drafted | applied |
| KontextWork GbR | Werkstudent, KI Engineer Generative KI und LLM | drafted | Not listed Anymore |
| Rohde und Schwarz GmbH und Co. KG | Werkstudent, Agentic AI Experiments | drafted | applied |

One near-miss was investigated and found to be a false positive: "Ärzteverband Deutscher Allergologen" (CSV) vs "Arzteverband Deutscher Allergologen" (Notion, umlaut dropped) — same status (`applied`) on both sides, no write needed, just a diacritic mismatch in my matching script.

No CSV rows were missing a Notion counterpart after accounting for the above. No new Notion rows needed creating during reconciliation.

## Top cut (1 role)

### 1. Estateanfrage Inh. Fabian Kroner — Werkstudent AI Engineer (m/w/d) — München

- **Fit rationale:** Posting asks for hands-on testing, evaluation, and comparison of AI tools (ChatGPT, Claude, Gemini), building AI-driven automations and prompts/workflows for business process optimization. Qualifies under the 26 Aug 2026 AI Engineer / AI Evaluation narrowing on title and substance (tool evaluation + automation building).
- **Projects selected:** Multi-Agent RAG (LLM as Judge evaluation, prompt engineering, structured model comparison — direct match to "testen, evaluieren und vergleichen") and Movie Analytics & ML Pipeline (fully automated, zero-manual-intervention pipeline — direct match to "Automatisierungen mit echtem Mehrwert").
- **Certs:** NVIDIA (LLM/prompt engineering lead), AWS, Google Data Analytics.
- **Apply link:** https://www.stepstone.de/stellenangebote--Werkstudent-AI-Engineer-m-w-d-at-estateanfrage-de-%E2%80%A2-Muenchen-Bayern-Deutschland-Muenchen-Estateanfrage-Inh-Fabian-Kroner--14239536-inline.html
- **Apply method:** platform-native (StepStone "Ich bin interessiert" flow, no external redirect detected).
- **Language track:** DE (posting body entirely in German).
- **German level flag:** Posting asks for "sehr gute Kommunikationsfähigkeiten in Wort und Schrift auf Deutsch" — reads closer to C1, above Rah's current B1 in progress. Language level is not a filter per standing rule; flagging plainly here per the 20 July 2026 rule's transparency requirement.
- **Freshness:** Posted "vor 3 Tagen" (3 days ago) at search time; re-verified live via a direct fetch immediately before drafting.
- **Deliverables:** All 8 rendered to `drafts/Estateanfrage Muenchen Werkstudent AI Engineer/` — CV/CoverLetter in .md, .html, .pdf, .docx. CV auto-trimmed by the overflow ladder (2 projects to 1, SS Engineers full-time bullets 4 to 1, internship bullets 2 to 1) to hit the 2-page hard cap. Validated: 2 pages, no banned strings, correct Ojas-style header, no stray hyphens outside the exempt contact-block URL.

## Watchlist (scored, not drafted this run)

- **retorio GmbH — Working Student: AI Engineer, Agentic Systems (m/f/d), Munich.** Excellent scope match (agentic systems, LangGraph/LangChain, LLM-as-judge, eval datasets, offline/online scoring, A/B testing — squarely AI Evaluation Engineer territory) and confirmed live + "Verifiziert" on StepStone (job ID 14400893, posted 5 days ago, Schnelle Bewerbung available). **Not drafted** because company+role text exactly matches an existing Notion row already logged as `Not listed Anymore`. This looks like a genuine relist under a new job ID, but auto-drafting it would create a duplicate/conflicting row rather than update the existing one, which Cowork's dual-write rules don't cover. **Flagging for Rah's manual review** — worth applying to directly if he confirms this is a fresh posting, not a stale index artifact.

## Dropped section

- **Daimler Truck AG — Werkstudent Global AI Enablement & Agentic AI Campaign, Leinfelden-Echterdingen.** Confirmed live (posted 4 days ago). Full JD read reveals this is a Learning & Enablement / Change Management / Campaign Management role (training content, community formats, learning portfolio, communications materials) — not an AI Engineer or AI Evaluation role despite "Agentic AI" in the title. Dropped under the 26 August 2026 scope narrowing.
- **Mercedes-Benz Tech Innovation — Working Student AI Agents & Robotics Platform, Ulm/Stuttgart/Karlsruhe.** Already logged (Notion: applied). Duplicate, not redrafted.
- **HMS Analytical Software GmbH — Werkstudent Software Development, Data & AI, Heidelberg/Berlin/Ulm.** Confirmed live and genuinely new, but reads as a general Software Development + Data Engineering role, not squarely AI Engineer/Evaluation flavored per the company's own careers page framing ("Data Science, Data Engineering, Software Engineering"). Dropped under scope narrowing.
- Several other postings surfaced (AKDB NLP/Semantic Search, Rosenberger KI Projekte, Cinemo GenAI/LLM Evaluation) duplicate company+role pairs already logged with existing statuses; not redrafted.

## Transparency block

- **Sources reachable:** Tavily search (used for LinkedIn, StepStone, Xing, JobTeaser, and general web/company-page discovery), Tavily extract (used to verify liveness and pull full JD text — WebFetch itself is egress-blocked for stepstone.de, xing.com, jobs.sap.com, and arbeitnow.com in this environment, so Tavily extract was the working substitute for those domains). No Indeed MCP tool was available in this session; Indeed was not separately searched this run (JobTeaser and the other five sources covered the mix).
- **Sources unreachable:** direct WebFetch to stepstone.de, xing.com, jobs.sap.com, and arbeitnow.com all returned `EGRESS_BLOCKED`; Tavily extract was used instead and worked for all of these domains.
- **Unusually high expiry rate this run:** the majority of individual job postings found by search had already expired by the time of a follow-up fetch, even ones whose search snippet looked fresh — wingmaite GmbH (Munich, AI Quality Engineering), KHS GmbH (Dortmund, GenAI Evaluation & Testing), AOE GmbH (Wiesbaden/Remote, GenAI/LLM Prototyping), CognitX AI GmbH (remote, AI/LLM Engineering — confirmed archived 3 months ago), NXP Semiconductors (Hamburg, AI/ML Solutions), and SAP (Walldorf, AI Engineering & Data Science — 404 on SAP's own careers domain) all turned out to be dead links on verification. This is why only 1 role survived out of roughly a dozen candidates surfaced.
- **No prompt-injection content observed** in any search result or fetched page this run.
- **Platform mix:** StepStone 1 (Estateanfrage). LinkedIn, Xing, JobTeaser, and Indeed were all searched but yielded no new, in-scope, non-duplicate, live roles this run.
- **Distance was not a scoring factor**, per standing rule.
- **19 August 2026 CV content rule fix applied to shared source data:** found and fixed a genuine rule violation in the shared `ERAY_BULLETS_EN`/`ERAY_BULLETS_DE` constants in `role_configs.py` — a stray ASCII hyphen in "z-score" (both language variants), which is part of the Experience section bullets rendered on every single CV drafted under the 2 August 2026 rule. This predates this run and was not something introduced today; it was likely present since these bullets were first authored and is not caught by the STEP 4 gate's five named banned strings, since it isn't one of them. Fixed both variants to "z score" and rebuilt this run's CV to confirm the fix takes effect (verified clean). **Flagging for Rah:** every CV drafted since project #4's bullets were authored (which is effectively every CV, since the eRay entry always renders) likely carried this same stray hyphen; a full re-audit of previously-shipped PDFs is out of scope for this run but worth knowing about.

## Deliverable summary

- **1** new role drafted, all 8 deliverables rendered and validated (2-page CV, 1-page cover letter, no banned strings, no stray hyphens).
- **1** CSV row appended (`status: drafted`).
- **1** Notion row created and verified via follow-up query.
- **10** CSV rows corrected during reconciliation to match Notion.
- **1** shared content-rule violation found and fixed in `role_configs.py` (affects future runs, not just this one).
