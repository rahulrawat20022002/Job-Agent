# Job Digest — 2026-09-22 (Cowork Drafting Agent, Scheduled Run)

## Bottom line

Drafted 4 roles this run: 3 brand new finds (Web Computing GmbH, BLACKFIELD AI, Modern Drive Technology GmbH, all Werkstudent AI Engineer roles) plus one housekeeping fix — a Syneco Trading GmbH company-portal row that Rah created directly in Notion on 21 Sep but that never actually got its CV/CL files rendered. That row now has real deliverables behind it. Reconciliation also found and fixed 14 CSV rows that were out of sync with Notion.

## Run type and render toolchain

Normal scheduled run. Render toolchain installed and verified OK (weasyprint 70.0, python-docx, pypdf).

## Backlog gate result

- Notion query on data source `fd974369-40b2-48c5-b660-d15256c88f52`, `Status = 'drafted'` at run start: **2 rows** (both Syneco Trading GmbH, same role, one Xing already fully rendered, one company-portal with no files).
- Per the 28 July 2026 gate, under 8 = **normal top 3 to 5 cut**.
- Backlog after this run: **5 rows** in Notion (2 at start, +3 new Notion pages created; the Syneco company-portal row was not a new Notion page, just newly backed by real files and a CSV row).
- CSV drafted count after this run: **5**, matching Notion.

## Reconciliation result

Compared all 215 CSV rows against all 211 valid Notion rows (one blank placeholder row, "New CVs now", excluded as not a real job row).

**Status drift found and fixed (14 rows, CSV updated to match Notion per invariant #1):**

| Company | Role | CSV said | Notion says (now authoritative) |
|---|---|---|---|
| Fraunhofer-Institut fuer Sichere Informationstechnologie SIT | Masterarbeit, Modellierungsansaetze und Loss Design... | applied | rejected |
| Generali Deutschland AG | Werkstudent, Machine Learning Engineering | applied | rejected |
| FZI Forschungszentrum Informatik | Masterarbeit, Evaluation and Verification of AI Generated Driving Scenarios... | drafted | applied |
| iLert GmbH | Working Student or Intern, AI Product Engineer | drafted | Not listed Anymore |
| Charles Real Estate GmbH | AI Systems Engineer, Working Student | drafted | Not listed Anymore |
| Temedica GmbH | Working Student, AI and Agentic Engineering | drafted | applied |
| SAP | Intern, Thesis or Working Student, Evaluating and Improving LLM based SE Solutions in SAP HANA | drafted | Not listed Anymore |
| Atruvia AG | Werkstudent Generative AI / Agentic AI | drafted | Not listed Anymore |
| disruptive GmbH | Werkstudent:in AI Engineering | drafted | Not listed Anymore |
| Muenchener Verein Versicherungsgruppe | Werkstudent, Conversational AI | drafted | applied |
| Stiftung Polytechnische Gesellschaft Frankfurt am Main | Werkstudent/in AI Engineering | drafted | applied |
| Control Expert GmbH | Working Student QA Engineer, AI / LLM Systems | drafted | Not listed Anymore |
| FUNKE Mediengruppe | Werkstudent Workflow Automation n8n, Agentic AI | drafted | Not listed Anymore |
| Vector Informatik GmbH | Werkstudent, AI driven CI/CD Automation | drafted | Not listed Anymore |

The last three (Control Expert, FUNKE Mediengruppe, Vector Informatik) were flagged as false-drafted-with-no-files in yesterday's (21 Sep) digest; they have since been correctly moved to "Not listed Anymore" in Notion, resolving that flag.

**Data quality gap found and fixed (not a status drift, a missing-deliverables gap):** the Syneco Trading GmbH company-portal Notion row (created 2026-09-21 22:16 by Rah directly) was `Status = drafted` with a Draft Path set, but had no CSV counterpart and no files anywhere in the repo — the exact false-drafted risk invariant #3 warns about. This run rendered its real 8 deliverables (reusing the already-verified 16 Sep Xing version's content for the same company and role) and added the matching CSV row, rather than leaving the gap silent.

**Minor, no action needed:** one CSV/Notion match looked like a miss ("Ärzteverband Deutscher Allergologen" in CSV vs "Arzteverband..." in Notion, umlaut-only spelling difference) — both sides already say `applied`.

## Top cut (4 roles drafted, all deliverables verified)

### 1. Syneco Trading GmbH — Masterarbeit, Agentic AI und Generative AI zur Optimierung energiewirtschaftlicher Prozesse (housekeeping fix, not a new find)
- **Location:** Muenchen | **Source:** Company Page (softgarden, branded Thuga Aktiengesellschaft) | **Apply Method:** company-portal (out of OpenClaw's scope, Rah submits manually) | **Language track:** DE
- **Apply link:** https://syneco.softgarden.io/job/67345185/Masterarbeit-m-w-d-Agentic-AI-und-Generative-AI-zur-Optimierung-energiewirtschaftlicher-Prozesse
- **Projects:** Multi-Agent RAG (trimmed to 1 by the overflow ladder), Flight Tracking referenced in cover letter
- **Fit:** Same role Rah is also applying to via Xing; this is the company-portal channel for the identical posting.
- **German level flag:** posting reads near-native German required (C1-ish), above Rah's B1 in progress — Rah's own call before submitting.
- **Deliverables:** all 8 present, 2 pages, banned strings absent.

### 2. Web Computing GmbH — Werkstudent, AI Engineer
- **Location:** Muenster | **Source:** Company Page | **Apply Method:** company-portal (online form) | **Language track:** DE
- **Apply link:** https://www.web-computing.de/werkstudent-ai-engineer/
- **Projects:** Multi-Agent RAG and CreditIQ (trimmed to 1 by the overflow ladder)
- **Fit:** Full ML lifecycle role (CRISP-DM: analysis, design, preprocessing, modeling, training, evaluation, integration) across Computer Vision, NLP and Predictive Analytics — matches CreditIQ's end-to-end delivery and RAG's evaluation work closely.
- **German level:** posting states "gute Deutsch- und Englischkenntnisse" (good, not native) — most reachable of this run's German bars against Rah's B1 in progress.
- **Deliverables:** all 8 present, 2 pages, banned strings absent.

### 3. BLACKFIELD AI — Werkstudent, AI Engineer
- **Location:** Bremen | **Source:** Company Page | **Apply Method:** company-portal (email to info@blackfield.ai) | **Language track:** DE
- **Apply link:** https://blackfield.ai/karriere/werkstudent-ai-engineer-mwd
- **Projects:** Multi-Agent RAG and Flight Tracking (trimmed to 1 by the overflow ladder)
- **Fit:** LLM/ML prototyping, data preparation and evaluations, scripts/tests/data pipelines, MLOps — strong match to RAG's JudgeAgent evaluation work and Flight Tracking's Airflow orchestration and testing.
- **German level flag:** posting states C1/C2 required, above Rah's B1 in progress — Rah's own call before submitting.
- **Deliverables:** all 8 present, 2 pages, banned strings absent.

### 4. Modern Drive Technology GmbH — Werkstudent, AI Engineering
- **Location:** Neumarkt in der Oberpfalz | **Source:** LinkedIn (Easy Apply) | **Apply Method:** platform-native (in OpenClaw's scope) | **Language track:** DE
- **Apply link:** https://de.linkedin.com/jobs/view/werkstudent-ai-engineering-m-w-d-at-modern-drive-technology-gmbh-4462220941
- **Projects:** Multi-Agent RAG and Flight Tracking (trimmed to 1 by the overflow ladder)
- **Fit:** Process automation via AI agents, LLM API integrations, REST integrations, LangChain/LangGraph preferred — matches RAG's LangGraph agent architecture and Flight Tracking's Airflow-driven replacement of manual reruns.
- **German level flag:** posting states "verhandlungssicheres Deutsch" (negotiation fluent), above Rah's B1 in progress — Rah's own call before submitting. Requires at least 1 day/week on-site in Neumarkt.
- **Posted:** approximately 2 weeks ago per LinkedIn, 89 applications showing at fetch time (still open).
- **Deliverables:** all 8 present, 2 pages, banned strings absent.

## Watchlist

None scored but not drafted this run — search yield matched the top cut exactly (4 verified, in-scope, non-duplicate finds).

## Dropped

- **Ponturo Consulting AG**, Werkstudent AI Engineer (multiple cities): listing only found via a now-dead third-party mirror (410 Gone); the company's own careers page shows zero open student positions. Dropped as unverifiable (invariant #4).
- **Jemix GmbH**, Werkstudent AI Engineer, Berlin: StepStone listing exists but the company's own careers page does not list this role among current openings. Dropped as unverifiable.
- **Klugsys**, Werkstudent Agentic AI Engineer, Aachen: LinkedIn listing surfaced but the company's own careers page lists only full-time roles and explicitly states no intern/working student roles are open. Dropped as unverifiable and out of scope.
- **itdesign**, Werkstudent AI Engineer: listing URL returned 404. Dropped as no longer live.
- **Helmholtz Munich**, Agentic AI Research Engineer, Munich: real and live on JobTeaser, but requires a PhD or MSc with substantial professional experience for a full-time research position — outside the Werkstudent/Pflichtpraktikum/Masterarbeit work-type scope. Dropped as out of scope.
- **Retorio GmbH** (Working Student AI Engineer Agentic Systems, Munich) and **Mercedes-Benz Tech Innovation** (Werkstudent AI Agents and Robotics Platform): both resurfaced in search but duplicate rows already logged in Notion ("Not listed Anymore" and "rejected" respectively). Dropped as duplicates.

## Transparency block

- **Notion:** reachable, all queries succeeded, no retry needed.
- **Tavily MCP:** failed to connect again this run (proxy-level connection error). Used WebSearch and WebFetch instead across StepStone, Xing, LinkedIn, JobTeaser and direct company career page fetches.
- **Indeed:** no MCP tool available this session, consistent with prior runs; Indeed not used (within the 28 July yield cap anyway).
- **Xing:** WebSearch queries scoped to xing.com/jobs kept resolving to StepStone mirrors rather than Xing's own domain, so Xing is flagged unreachable in its own right this run, same pattern noted in the 16 Sep digest.
- **Platform mix (new finds):** Company Page 2 (Web Computing GmbH, BLACKFIELD AI), LinkedIn 1 (Modern Drive Technology GmbH). The Syneco Trading company-portal fix is not counted as a new platform-mix entry since it duplicates an already-counted 16 Sep Xing find.
- **Prompt-injection content:** none observed in any fetched posting or Notion data this run.
- **Distance was not used as a scoring factor**, per standing rule; all four roles fall in the single Germany tier.
- **German level bars flagged as information only, never a filter**, per master-projects.md: three of the four roles this run (Syneco, BLACKFIELD, Modern Drive) state a German bar above Rah's actual B1 in progress; Web Computing's bar is the softest of the four.

## Deliverable summary

- New roles drafted: **4** (1 housekeeping fix + 3 new finds)
- Files rendered: **32** (4 roles × 8 deliverables each), all verified present, all 2 pages, all banned strings absent
- CSV writes: 14 status corrections (reconciliation) + 4 new drafted rows appended
- Notion writes: 3 new pages created (Web Computing GmbH, BLACKFIELD AI, Modern Drive Technology GmbH) + 1 existing page's Notes updated (Syneco Trading GmbH company-portal row)
- Backlog after run: **5 drafted** in Notion, CSV drafted count matches at **5**
