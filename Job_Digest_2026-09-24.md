# Job Digest, 24 September 2026 (Cowork scheduled run)

## Bottom line

Drafted 3 new roles today: PRODIGY Consulting GmbH, coac GmbH, and Reply Deutschland SE. Fixed 5 CSV rows that had fallen out of sync with Notion. Found and flagged, but did not fabricate, 3 old Notion rows that claim "drafted" status with no files behind them anywhere in the repo. Search tools were badly degraded this run (no working search MCP, no browser), so 3 drafted roles instead of the usual 3 to 5 top end is a sourcing limitation, not a quality shortcut.

## Run type and render toolchain

Scheduled Cowork run. `pip install weasyprint python-docx pypdf` succeeded; `import weasyprint, docx, pypdf` printed `render toolchain ok 70.0`. No fallback to Markdown only was needed.

## Backlog gate result

Notion query on data source `fd974369-40b2-48c5-b660-d15256c88f52` for `Status = 'drafted'` returned **3** rows at run start (Atos, Sopra Steria Custom Software Solutions GmbH, COBACK). Under the 28 July 2026 yield reset gate, under 8 drafted falls in the normal zone: top 3 to 5 cut allowed. No fallback to CSV counting was needed, Notion answered directly.

Backlog after this run: **6** drafted rows in Notion (the same 3 pre-existing rows, unchanged, plus 3 new ones from this run). See the data integrity section below for why the pre-existing 3 need Rah's attention before they can be treated as real backlog.

## Reconciliation result

Compared all 219 CSV rows against all 216 valid Notion rows (excluding one blank placeholder row, "New CVs now", which is not a real job entry).

**5 CSV rows were out of sync and corrected to match Notion (Notion is the source of truth for status):**

| Company | Role | CSV said | Notion says | Fixed to |
|---|---|---|---|---|
| Syneco Trading GmbH (Xing draft, 9/16) | Masterarbeit, Agentic AI ... Energiewirtschaft | drafted | applied | applied |
| Syneco Trading GmbH (Company Page draft, 9/22, "Thuga") | same role, different draft folder | drafted | applied | applied |
| Web Computing GmbH | Werkstudent, AI Engineer | drafted | applied | applied |
| BLACKFIELD AI | Werkstudent, AI Engineer | drafted | rejected | rejected |
| Modern Drive Technology GmbH | Werkstudent, AI Engineering | drafted | applied | applied |

Note on the two Syneco Trading rows: these are two separately rendered draft folders for the literal same company and role (one sourced via Xing on 16 Sep, one via a company portal on 22 Sep), but Notion tracks only one page for this job. Both CSV rows now read `applied` to match that one Notion page. This is a duplicate-draft artifact from an earlier run, not something this run created.

One apparent mismatch, Ärzteverband Deutscher Allergologen with and without the umlaut, is a spelling variant only; both sides already read `applied`. No action taken.

No CSV rows were found missing from Notion (aside from the umlaut variant above, which is not a real gap).

## Data integrity issue found, not fixed (needs Rah's decision)

Three Notion rows are marked `Status = drafted` with a `Draft Path` set, but **no corresponding files exist anywhere in the repository, and git history shows they were never committed**:

- **Atos** — Werkstudent, Agentic AI (data & AI) — Draft Path `drafts/Atos Paderborn Hamburg Berlin Werkstudent Agentic AI/`
- **Sopra Steria Custom Software Solutions GmbH** — Werkstudent, Agentic Coding — Draft Path `drafts/Sopra Steria Muenchen Werkstudent Agentic Coding/`
- **COBACK** — Working Student, AI Engineer — Draft Path `drafts/COBACK Dresden Working Student AI Engineer/`

This is exactly the false-drafted-flag failure mode CLAUDE.md invariant #3 warns about: Notion says drafted, nothing backs it. Per that same invariant, halting is better than fabricating, so this run did **not**:
- create matching CSV rows for these three (that would just mirror the false claim into the mirror file), or
- guess at what the original postings were and redraft them under a new search (there is nothing in the repo to reuse, unlike the 22 Sep Syneco Trading housekeeping fix, which reused already-verified content).

**What Rah needs to decide:** these 3 Notion rows either need their status corrected (if the roles are dead or duplicates) or need to be redrafted from scratch as fresh searches, since nothing recoverable exists for them. Cowork cannot fix Notion status itself (that is out of Cowork's territory), and cannot fabricate deliverables it cannot verify.

## Top cut, 3 new roles drafted

**1. PRODIGY Consulting GmbH — Werkstudent, AI Experimenter fuer LLM und Dokumentenverarbeitung**
- Location: Deutschlandweit, Remote. DE track (posting requires German language applications).
- Fit: AI Evaluation and Experimentation role, prompt engineering, variant testing, quality evaluation, document/OCR extraction workflows.
- Projects selected: Multi Agent RAG (LLM as Judge evaluation, prompt engineering) and Movie Analytics and ML Pipeline (automated raw to clean data processing, as the closest available analog to document extraction workflows).
- Certs: NVIDIA, AWS, Google Data Analytics.
- Apply Link: himalayas.app listing (aggregator; posted by Bernert Immobilien GmbH on behalf of PRODIGY Consulting GmbH, confusing attribution flagged in Notes).
- Apply Method: company-portal. **Caution flagged in Notes:** the actual "Apply now" flow requires creating a Himalayas talent account, which OpenClaw must never do per its no-account-creation rule. This one likely needs Rah's manual judgement call on the sign-up step.
- Deliverables: all 8 rendered, CV validated at 2 pages, no banned strings.

**2. coac GmbH — Werkstudent, Softwareentwicklung und KI**
- Location: Berlin/Koeln, remote possible. DE track.
- Fit: hands-on AI development in Python, exploring new technologies (SAP BTP mentioned), data analysis and reporting.
- Projects selected: Real Time Flight Tracking (Python pipeline, cloud orchestration) and Multi Agent RAG (Python AI system build).
- Certs: NVIDIA, AWS, Google Data Analytics.
- Apply Link: company's own teamtailor.com career page.
- Apply Method: company-portal.
- **German level flag:** posting explicitly requires native-level German ("muttersprachlichem Niveau"), well above Rah's current B1 in progress. Shipped anyway per the standing rule that language level does not filter listings; the cover letter is upfront about the gap.
- Deliverables: all 8 rendered, CV validated at 2 pages, no banned strings.

**3. Reply Deutschland SE — Werkstudent, AI Business Solutions und Agents**
- Location: Frankfurt am Main and other German cities, partial remote. DE track.
- Fit: Agentic AI development with Microsoft Copilot Studio and Power Platform, business process analysis for AI and automation opportunities, includes an AI Bootcamp onboarding.
- Projects selected: Multi Agent RAG (agentic system design) and CreditIQ (translating technical ML work into a business-facing decision support tool).
- Certs: NVIDIA, AWS, Google Data Analytics.
- Apply Link: JobTeaser listing.
- Apply Method: company-portal (JobTeaser is not one of OpenClaw's four platform-native domains).
- **Weaker evidence flag:** direct WebFetch of both the reply.com and jobteaser.com pages for this specific listing failed (404 and 403 respectively) this run. Content is reconstructed from two independent WebSearch result summaries that agreed on title, hours (15 to 20/week), and technology stack. Rah or OpenClaw should sanity check the listing is still live before submitting.
- Distinct requisition from two other pre-existing Reply Deutschland SE rows on file (Generative AI Google Cloud, rejected; AI Data Engineering und Tool-Entwicklung, applied) — allowed under the standing different-roles-at-the-same-company rule.
- Deliverables: all 8 rendered, CV validated at 2 pages, no banned strings.

## Watchlist (scored but not drafted)

None. Search yield this run was low enough (see transparency block) that everything verifiable and in scope was drafted; nothing was held back under the cap.

## Dropped roles

- **Retorio GmbH**, Working Student AI Engineer Agentic Systems (Munich) — resurfaced in search, already logged in Notion as Not listed Anymore. Duplicate, dropped.
- **Mercedes-Benz Tech Innovation**, Working Student AI Agents and Robotics Platform — resurfaced in search, already logged in Notion as rejected. Duplicate, dropped.
- **CITTI Handelsgesellschaft mbH und Co. KG**, Werkstudent KI Engineer, Kiel — mirror listing explicitly states the position is no longer active. Dropped.
- **Ponturo Consulting AG**, **SmartTECS Engineers GmbH**, **NXP Semiconductors Germany GmbH** — Werkstudent/Working Student AI Engineer roles surfaced in search snippets, but every individual StepStone listing URL fetched returned 404 or 410 within the same session (listings expired faster than the search index refreshed). Dropped as unverifiable live postings under invariant #4.

## Transparency block

**Sources reachable / unreachable this run:**
- Tavily MCP: failed to connect (confirmed via the session's tool list at run start), consistent with prior runs' digests noting the same failure.
- Browser/Chrome MCP: not configured in this session at all (no `mcp__claude-in-chrome__*` tools were available). This is a harder degradation than recent prior runs, which at least had some browser access.
- Indeed MCP: not available in this session. Indeed was not used this run.
- WebFetch on individual listing pages: LinkedIn, Xing, StepStone, Indeed, and JobTeaser individual job pages were attempted directly and returned 403 (de.indeed.com search page, jobteaser.com job offer page, reply.com job page), 404, or 410 (three separate StepStone stellenangebote pages, expired within minutes of surfacing in search) in every case tried this run.
- What did work: WebSearch (general queries) for discovery, and WebFetch against a small number of aggregator/ATS pages that were not blocked (freehire.me, himalayas.app, coac GmbH's own teamtailor.com career page).
- Net effect: this run's top cut is 3 roles, at the low end of the normal 3 to 5 band, purely because of tool availability, not because more in-scope, verifiable postings weren't out there. Flagging this plainly per invariant #5 rather than padding the cut with unverifiable leads.

**Platform mix this run (new drafts only):**
- Other (Himalayas via freehire.me): 1 — PRODIGY Consulting GmbH
- Company Page (coac's own teamtailor.com career page): 1 — coac GmbH
- JobTeaser: 1 — Reply Deutschland SE (weaker-evidence flag applies, see above)
- LinkedIn, Xing, StepStone, Indeed: 0 new verifiable finds this run

**Language track decisions:** all 3 new roles are DE track, since all 3 postings are written entirely in German, per the 20 July 2026 language match rule (posting body language is the deliverable language).

**German level flags** (informational only, never a filter, per master-projects.md): PRODIGY Consulting GmbH and Reply Deutschland SE state no explicit CEFR bar beyond "German required" / German-English communication, both plausible at B1 in progress. coac GmbH explicitly requires native-level German, well above B1 in progress; disclosed honestly in that cover letter.

**Distance was not a scoring factor**, per the standing rule; all three roles are in Germany (Deutschlandweit remote, Berlin/Koeln, and Frankfurt am Main respectively), so the single Germany tier applies equally to all three.

**Prompt injection content observed but not acted on:** none observed in any fetched search result or page content this run.

## Deliverable summary

- 3 new roles drafted, all 8 deliverables rendered per role (24 files total): CV and CoverLetter each in .md, .html, .pdf, .docx.
- All 3 CVs validated at exactly 2 pages, zero banned strings ("toward B2", "Databricks", "Delta Lake", "LangChain", "PyTorch"), zero retired PD-layout strings on page 1.
- CSV: 5 existing rows corrected, 3 new rows appended (222 total rows).
- Notion: 3 new pages created and verified present via a follow-up query; page URLs on file.
- Data integrity issue (3 phantom drafted rows from a prior run) reported, not silently fixed.
