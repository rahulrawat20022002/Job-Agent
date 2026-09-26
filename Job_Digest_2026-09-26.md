# Job Digest, 26 September 2026

Run type: scheduled Cowork Drafting Agent (Agent A). Render toolchain (weasyprint, python-docx, pypdf) installed and verified successfully at run start.

## Bottom line

Notion said 9 roles were already waiting to be applied to; that count put this run in the "cap at top 3" tier, so 3 new roles got drafted today. While checking the backlog, I found 7 of those 9 pre-existing "waiting" roles are hollow: Notion says they are ready, but no CV or cover letter was ever actually built for them. I have not touched those 7 — see the critical finding below, which needs your call.

## Backlog gate result

- Notion drafted count at run start: **9** (authoritative, no fallback needed).
- Gate zone: 8 to 10 drafted → capped at top 3 new roles this run.
- Backlog after this run: **12** drafted in Notion (9 + 3 new).
- CSV drafted count after this run: **3** (only today's three; see critical finding below for why this does not match Notion's 12).

## CRITICAL FINDING: 7 "drafted" backlog rows have no CV/CL ever built

While reconciling, I checked every Notion row marked `drafted` against the actual `drafts/` folder on disk. Two thirds of the existing backlog turned out to be empty:

- **Atos** — Werkstudent, Agentic AI (data & AI) — no draft folder, no CSV row.
- **COBACK** — Working Student, AI Engineer — no draft folder, no CSV row.
- **Sopra Steria Custom Software Solutions GmbH** — Werkstudent, Agentic Coding — no draft folder, no CSV row.
- **coac GmbH** — Werkstudent, Softwareentwicklung und KI — no draft folder, no CSV row.
- **PRODIGY Consulting GmbH** — Werkstudent, AI Experimenter fuer LLM und Dokumentenverarbeitung — no draft folder, no CSV row.
- **Reply Deutschland SE** — Werkstudent, AI Business Solutions und Agents — no draft folder, no CSV row.
- **KWS SAAT SE and Co KGaA** — Working Student, Global IT, AI and LLM Solutions — no draft folder, no CSV row.

For each of these, Notion has a page with Status = drafted and a Draft Path, but the folder that path names does not exist anywhere in the repository, and there is no corresponding row in applied-log.csv. This is exactly the false-success pattern the standing rules warn against: at some point Notion was written to as if a CV and cover letter had been built, but they never were.

**What I did about it:** nothing that changes their status. I did not flip these to any other status (that would be inventing a new outcome without evidence, and status flips out of drafted are OpenClaw's territory, not mine to reach for even to fix a data problem). I did not fabricate CVs for them under today's cap, since I have not done fresh search/scoring work for these specific roles. I am flagging them here so you can decide.

**Decision needed from you (pick one):**
- **A.** Treat all 7 as real candidates: tell me to search, score, and render their 8 deliverables properly on a future run (this would use up backlog-gate headroom on old roles instead of fresh ones).
- **B.** Treat all 7 as stale/abandoned: tell me to delete the Notion rows (or flip them to a status like "Not listed Anymore") so the backlog count reflects reality.
- **C.** Leave them as-is for now and I'll keep flagging them each run until you decide.

Two other existing "drafted" rows checked out fine — **retorio GmbH** and **KontextWork GbR** both have complete, real 8-file draft folders on disk. Retorio's Notion Draft Path field, however, pointed at a folder name that does not exist ("retorio Muenchen Working Student AI Engineer Agentic Systems"); the real folder is named "Retorio Munich Working Student AI Engineer Agentic Systems". I corrected the Draft Path field in Notion to point at the real folder (a text-field fix, not a status change). **Process error on my part:** in making that correction I overwrote the row's existing Notes field instead of appending to it, so whatever context was in that field before is gone. Noting it here so I don't repeat the mistake, and so you know if anything there seemed to disappear.

## Reconciliation result

Compared all 219 CSV rows against all 221 valid Notion rows (one blank placeholder row, "New CVs now", excluded). Found 6 real drift rows where Notion had moved past `drafted` while the CSV was stale; fixed all 6 in the CSV per the standing rule that Notion wins:

| Company | Role | CSV said | Notion says (now applied) |
|---|---|---|---|
| Mercedes-Benz AG | Werkstudent, Data Engineering Datenanalyse und KI Mercedes-Benz Vans | applied | rejected |
| Syneco Trading GmbH (Xing entry) | Masterarbeit, Agentic AI... | drafted | applied |
| Syneco Trading GmbH (Company Page entry) | Masterarbeit, Agentic AI... | drafted | applied |
| Web Computing GmbH | Werkstudent, AI Engineer | drafted | applied |
| BLACKFIELD AI | Werkstudent, AI Engineer | drafted | rejected |
| Modern Drive Technology GmbH | Werkstudent, AI Engineering | drafted | applied |

The last four are almost certainly OpenClaw submission results from a run after 22 September that Cowork never had a chance to reconcile back into the CSV until today. One duplicate KontextWork GbR pair in the CSV (both already "Not listed Anymore" on both sides) needed no fix. One apparent Ärzteverband/Arzteverband mismatch was just a missing-umlaut spelling variant, both sides already say "applied," no action needed.

## Top cut, 3 new roles drafted

All three passed live-verification (fetched directly, not from a stale aggregator mirror), all three are DE-track (postings entirely in German), all three are brand-new companies never logged before.

### 1. Rohde & Schwarz — Werkstudent, AI Agents fuer Software Engineering — Stuttgart
- **Fit:** structuring and validating technical information for AI assistants and AI agents; developer productivity and knowledge management. Strong match to the Multi-Agent RAG project's LangGraph/JudgeAgent work and the Flight Tracking pipeline's automation story.
- **Projects on CV:** Multi-Agent RAG, Real-Time Flight Tracking.
- **Certs:** NVIDIA, AWS, Google Data Analytics.
- **Apply link:** job.rohde-schwarz.com (company's own ATS), Referenz 2351.
- **Apply method:** company-portal (out of OpenClaw's platform-native scope).
- **Language track:** DE. German level: posting entirely in German, no explicit CEFR bar stated.
- **Freshness:** posted 19 September 2026 (one week old, freshest of the three).
- **Deliverables:** all 8 rendered, 2-page CV, gate passed.

### 2. Ventum Consulting GmbH & Co. KG — Werkstudent, AI — Muenchen
- **Fit:** internal "AI Factory" role building and testing GenAI/LLM solutions to streamline internal processes. Matches the Multi-Agent RAG project's GenAI work and the Movie Analytics pipeline's automation story.
- **Projects on CV:** Multi-Agent RAG, Movie Analytics & ML Pipeline.
- **Certs:** NVIDIA, AWS, Google Data Analytics.
- **Apply link:** ventum-consulting.onlyfy.jobs (Onlyfy form on company's own domain).
- **Apply method:** company-portal.
- **Language track:** DE. German level: posting states "sehr gute Deutschkenntnisse" (excellent German) — above B1 in progress, flagged for your judgement, not used as a filter.
- **Deliverables:** all 8 rendered, 2-page CV, gate passed.

### 3. SmartTECS Cyber Security GmbH — Werkstudent, AI Engineer — Chemnitz / Dresden
- **Fit:** RAG systems, embeddings, vector databases, model fine-tuning, and GenAI security risk analysis against OWASP Top 10. Excellent match to the Multi-Agent RAG project's Pinecone/hybrid-retrieval work and CreditIQ's regulatory/security documentation.
- **Projects on CV:** Multi-Agent RAG, CreditIQ.
- **Certs:** NVIDIA, AWS, Google Data Analytics.
- **Apply link:** official Bundesagentur fuer Arbeit listing, Referenz-Nr. 10001-1003090842-S (no direct company online form found).
- **Apply method:** company-portal.
- **Language track:** DE. German level: posting states "Deutsch und Englisch sehr gut" (very good German and English) — above B1 in progress, flagged for your judgement, not used as a filter.
- **Freshness:** posted 30+ days ago per the listing, but still shown as open on the official government job board.
- **Deliverables:** all 8 rendered, 2-page CV, gate passed.

## Watchlist (found but not drafted, cap reached)

None — only 3 verifiable live leads were found this run after dropping the stale ones below, exactly matching the cap. No roles were bumped by the cap itself.

## Dropped section

All dropped for freshness/verifiability, not fit — every one of these looked like a strong match on paper but turned out to be a dead listing when checked directly:

- **CognitX AI GmbH** (AI/LLM Engineering, Werkstudent, Darmstadt): both aggregator links 410 Gone; company's own careers page says no open positions.
- **Jemix GmbH** (Werkstudent AI Engineer, Berlin): StepStone listing exists but company's own careers page no longer lists it (consistent with the 22 Sep run's finding for the same company).
- **Allianz Kunde und Markt GmbH** (Werkstudent Robotik-Prozessautomatisierung & Agentic AI, Unterfoehring): posting URL 410 Gone, not on current student careers listing.
- **ponturo consulting AG** (Werkstudent AI Engineer, multiple cities): third-party mirror 410 Gone, company's own careers page shows no open student AI role (consistent with 22 Sep finding).
- **HDI AG** (Agentic AI Platform Engineer, Hannover): traces back to a March 2026 posting, 6+ months stale.
- **Jobgether "AI Engineer"** (Germany): not a real employer name, sign-in wall, no work type given, not auditable.
- **appliedAI Initiative GmbH** (Working Student Agentic AI & Automation, Munich): no longer on the company's live careers page, which only shows the already-logged (rejected) AI Engineering & Product Development role.

## Transparency block

- **Sources reachable this run:** WebSearch (general), WebFetch (company career pages, Bundesagentur fuer Arbeit, Rohde & Schwarz's own ATS, Ventum's own careers page).
- **Sources unreachable/degraded this run:** Tavily MCP failed to connect (consistent with prior runs). No Indeed MCP tool was available in this session, so Indeed was not used. StepStone.de and most third-party aggregator mirrors (join.com specific listing IDs, arbeitnow.com, startup.jobs, studysmarter.de) returned 503/410 errors on direct fetch; where a lead only existed on a dead mirror it was dropped rather than drafted on unverifiable information.
- **Freshness dating:** noted per-role above; freshest is Rohde & Schwarz (19 Sep 2026), oldest still-open listing is SmartTECS (30+ days, verified still live on the official government board).
- **Prompt-injection content observed:** none.
- **Platform mix this run:** Company Page x2 (Rohde & Schwarz, Ventum Consulting), Other x1 (SmartTECS, via Bundesagentur fuer Arbeit).
- **Distance was not a scoring factor**, per standing rule; all three roles are within Germany (Stuttgart, Muenchen, Chemnitz/Dresden), all top geographic tier.
- **Apply method per role:** all three company-portal (none of the three cleared as LinkedIn/Xing/StepStone/Indeed platform-native Easy Apply, so all three fall outside OpenClaw's scope and are for Rah to submit manually — OpenClaw's Notes handling will apply when it next runs).

## Deliverable summary

- 3 new roles drafted, all 8 deliverables each (CV .md/.html/.pdf/.docx, CoverLetter .md/.html/.pdf/.docx) = 24 files, all present and verified.
- CSV: 3 new drafted rows appended, plus 6 drift corrections from reconciliation.
- Notion: 3 new drafted pages created and verified via follow-up query; 1 existing row's Draft Path corrected (retorio).
- **CSV/Notion drafted-count mismatch after this run (3 vs 12) is expected and explained above** — it is not a bug in today's run; it is the pre-existing 7 hollow rows plus 2 real-but-never-CSV-logged rows (retorio, KontextWork) that predate today.
