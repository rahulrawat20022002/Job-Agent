# Job Digest — 18 September 2026

**Run type:** Scheduled Cowork Drafting Agent (Agent A) run.
**Render toolchain:** weasyprint 70.0, python-docx 1.2.0, pypdf 6.19.0 installed clean. `import weasyprint, docx, pypdf` printed `render toolchain ok 70.0`. No fallback to Markdown-only needed.

---

## Backlog gate result

Queried Notion data source `fd974369-40b2-48c5-b660-d15256c88f52` for `Status = 'drafted'` at run start: **6 rows** (FZI Forschungszentrum Informatik, iLert GmbH, Temedica GmbH, Charles Real Estate GmbH, SAP Walldorf LLM based SE Solutions, Syneco Trading GmbH). No retry needed, Notion answered on the first query.

6 drafted is under the 8-row floor of the 28 July 2026 yield reset, so the **normal top 3 to 5 cut** applies. Search yielded **4 new roles** this run. Backlog after this run: **10 drafted** in Notion. Flagging forward: 10 crosses into the 8-to-10 tier (cap at top 3) that would apply to the *next* scheduled run if OpenClaw has not submitted any of these in the meantime; this run's own gate was correctly applied against the 6-row count at its own start.

## Reconciliation result

Pulled all 204 rows from the Notion data source (SQL mode, paginated 100/100/4) and matched every one of the 208 rows in `applied-log.csv` by company plus role, case insensitive.

**No real Status drift found.** One apparent mismatch is the same known spelling variant flagged in the 16 and 17 September digests: "Ärzteverband Deutscher Allergologen" (CSV, with umlaut) versus "Arzteverband Deutscher Allergologen" (Notion, umlaut dropped by the SQL text layer) — both sides already read `applied`, no action needed.

**New data-quality finding, flagged but not fixed (out of scope for the two defined reconciliation write directions):** five CSV rows are exact duplicate pairs of an already-logged company plus role — Mi-Jack Europe GmbH (Pflichtpraktikant, Entwicklung von AI Agents), appliedAI Initiative GmbH (Working Student, AI Engineering and Product Development), KontextWork GbR (Werkstudent, KI Engineer Generative KI und LLM), Rohde und Schwarz GmbH und Co. KG (Werkstudent, Agentic AI Experiments), and Estateanfrage Inh. Fabian Kroner (Werkstudent AI Engineer). Each pair has identical status and content; this is CSV noise, not a Status disagreement with Notion, so it does not fall under either of the two reconciliation write directions (fix CSV to match Notion, or create a missing Notion row). Recommend Rah decide whether a future run should be authorized to deduplicate these five CSV rows.

**Resolution of a concern carried over from the 17 September digest:** that digest flagged four Notion rows (Temedica GmbH, Charles Real Estate GmbH, SAP Walldorf, Syneco Trading GmbH) as `drafted` with no backing CSV row, drafts folder, or git history — a possible false "drafted" claim under invariant #3. On this run's checkout (`origin/main` at `30ea737`, this session's branch already even with it), all four now have complete CSV rows and all 8 committed deliverables in `drafts/`. Investigation of the git graph shows this was a branch-timing artifact: the 16 September run's pull request (#35, commit `e56d466`) landed on `main` concurrently with the 17 September run's own session, whose branch had already forked from an earlier point in `main` before PR #35 merged — so its checkout genuinely could not see those files at the time, even though they existed in git. No data was ever actually lost; the concern is resolved as of this run.

One more data quality note, not acted on (out of Cowork's write scope, carried forward from prior digests): the Notion data source still contains a stray row with Company `"New CVs now"` and null Role/Status. Still there; flagging again for manual cleanup.

## Search, filter, score, tailor

**Search sources reachable this run:** Tavily search and Tavily extract were both reachable end to end for the first time since before 9 September, breaking the multi-day outage reported in the 9 through 17 September digests. WebFetch, however, hit the same blanket `EGRESS_BLOCKED` proxy denial as those prior runs, confirmed against `jobteaser.com`, a Saarland-university JobTeaser mirror, and `stepstone.de` directly — so all verification this run went through Tavily instead of WebFetch. No Indeed MCP tool was available in this session, consistent with prior runs; Tavily-based Indeed search returned nothing new in scope, so Indeed was not used.

### Top cut (4 new roles drafted)

1. **Atruvia AG** — Werkstudent Generative AI / Agentic AI (m/w/d), Aschheim / Karlsruhe. Source: Company Page (karriere.atruvia.de, mirrored on jobware.de and a Hochschule Worms/Ludwigshafen Stellenmarkt feed), posted 10.09.2026. Atruvia is the IT service provider for the German Volksbanken Raiffeisenbanken cooperative banking group; role builds agent-based AI solutions from technical concept through implementation. Fit rationale: squarely Agentic AI titled and scoped; regulated financial-services backdrop matches CreditIQ's fairness-by-design, EU AI Act / GDPR compliant credit scoring work almost exactly. Projects selected: Multi-Agent RAG, CreditIQ (fairness by design credit scoring). Certs: NVIDIA, AWS, Google Data Analytics (DE). Language track: DE (posting entirely in German). Apply link: jobware.de listing. Apply method: unset, pending OpenClaw's platform-native vs company-portal check (reads as company portal). Deliverables: all 8 rendered, CV 2 pages, banned-string and PD-layout checks clean.

2. **disruptive GmbH** — Werkstudent:in AI Engineering (m/w/d), München. Source: StepStone (original discovery), apply via disruptive's own join.com ATS. Posted "vor 5 Tagen" per StepStone. A young AI consultancy (subsidiary of communications agency In A Nutshell) helping Mittelstand clients adopt AI across 50+ projects. Fit rationale: squarely AI Engineering titled; consultancy context rewards demonstrable, production-shipped AI systems over academic-only work. Projects selected: Multi-Agent RAG, Real-Time Flight Tracking (automated orchestration). Certs: NVIDIA, AWS, Google Data Analytics (DE). Language track: DE. Apply method: unset, pending OpenClaw (reads as company portal via join.com). Deliverables: all 8 rendered, CV 2 pages, checks clean.

3. **Münchener Verein Versicherungsgruppe** — Werkstudent (m/w/d) Conversational AI, München. Source: Company Page (own stellenangebote-innendienst careers page; also mirrored on StepStone with an original post date of 5 August 2026, so an older but still-open posting). Supports conception, design, and implementation of Conversational AI (chat/voice bots) for customer and sales communication, including LLM evaluation, integration, and prompt engineering. Fit rationale: RAG project's LanguageAgent (consistent multilingual dialogue output) and LLM-as-Judge evaluation harness map directly onto the posting's LLM evaluation and integration ask. **Not a duplicate**: company already has one Notion row (Werkstudent, Data Analytics und KI, status `rejected`), but this is a distinct req (Conversational AI, not Data Analytics), so it clears the standing company+role dedup check. Projects selected: Multi-Agent RAG, Real-Time Flight Tracking. Certs: NVIDIA, AWS, Google Data Analytics (DE). Language track: DE. Apply method: unset, pending OpenClaw (reads as company portal). Deliverables: all 8 rendered, CV 2 pages, checks clean.

4. **Stiftung Polytechnische Gesellschaft Frankfurt am Main** — Werkstudent/in AI Engineering (w/m/d), Frankfurt am Main. Source: Company Page (sptg.de, one of the largest private nonprofit foundations in Germany). No explicit post date shown on the page; confirmed currently live under "Aktuelle Stellenangebote." Maintains and develops the foundation's cloud-based AI knowledge platform. Fit rationale: the RAG project **is** a cloud-deployable, multilingual knowledge-retrieval-and-answer platform with an evaluation harness — about as close a one-to-one match as this pipeline finds. Projects selected: Multi-Agent RAG, Movie Analytics & ML Pipeline (automated cloud platform, always-on Cloud Scheduler trigger). Certs: NVIDIA, AWS, Google Data Analytics (DE). Language track: DE. Apply method: unset, pending OpenClaw (reads as company portal, no third-party ATS visible). Deliverables: all 8 rendered, CV 2 pages, checks clean.

All four cleared: a live posting fetched directly, a confirmed still-active apply link, and a clean dedup check against the full 204-row Notion set and 208-row CSV.

### Watchlist

None scored below the cut — all four verified leads were drafted.

### Dropped section

- **BMW Group** — Werkstudent Cloud Engineering & AI-Integration (München, JobTeaser). Reads predominantly as AWS/Kubernetes/Terraform cloud platform engineering; AI/LLM/Agentic AI appears as one bullet among many, not squarely an AI Engineer role. Dropped under the 26 August 2026 narrowing (plain cloud/infra engineering is out of scope).
- **Villeroy & Boch AG (V&B Fliesen GmbH)** — Working Student SAP and AI Technologies (Merzig, JobTeaser). Reads predominantly as SAP ABAP development, Celonis process mining, and supply-chain digitalization; "Artificial Intelligence and Generative AI" is one workstream among ten. Dropped as plain SAP/Data consulting, not AI Engineer/Evaluation flavored.
- **AXA Konzern AG** — AI Infrastructure Engineer im Data Innovation Lab (Köln, StepStone). Explicitly "Feste Anstellung, Vollzeit" (permanent, full-time). Dropped: out of scope under the standing work-types filter (Werkstudent, mandatory internship, Masterarbeit only).
- **jemix GmbH** — Werkstudent AI Engineer (via a StudySmarter/Talents aggregator mirror only). The aggregator's own task description reads as Cloud & Systemintegration work on a PSA platform, not AI engineering, and no first-party jemix careers page could be reached to verify the title independently. Dropped under invariant #4 (every write must be auditable) — a title/content mismatch on a third-party mirror is not sufficient evidence.
- **Daimler Truck AG** — Werkstudententätigkeit im Bereich Global AI Enablement & Agentic AI Campaign (Leinfelden-Echterdingen, StepStone). Cross-checked against Daimler Truck's own public AI-upskilling programme material (LibreChat rollout, AI literacy campaign, 20,000+ participants trained); this role reads as internal AI adoption/training/communications, not an AI engineering or evaluation build role. Dropped as out of scope.
- **Ambit IQ** — Praktikant/Werkstudent AI Engineer (LinkedIn). Based in the Zürich metropolitan area, Switzerland — outside the standing Germany-plus-remote-in-EU geography filter. Dropped.
- **appliedAI Initiative GmbH** — Working Student AI Engineering and Product Development (München/Heilbronn). Duplicates a company+role combination already logged as `rejected`. Skipped as a duplicate, not scored fresh.

## Transparency block

- **Sources reachable this run:** Tavily search and Tavily extract, both fully reachable — the first run since before 9 September where verification did not depend on WebSearch snippets alone.
- **Sources unreachable this run:** WebFetch, blocked by the network egress proxy with `EGRESS_BLOCKED` against three independently tested domains (jobteaser.com, a Saarland-university JobTeaser mirror, stepstone.de directly). No Indeed MCP tool available.
- **No prompt-injection content observed** in any fetched posting or search result this run.
- **Platform mix:** Company Page 3 (Atruvia AG, Münchener Verein, Stiftung Polytechnische Gesellschaft), StepStone 1 (disruptive GmbH, original discovery channel; apply link itself is the company's own join.com ATS). Xing, JobTeaser, and LinkedIn were searched via Tavily but surfaced only already-logged, out-of-scope, or dropped leads (see Dropped section). Indeed not used.
- **Distance was not a scoring factor.** All four new roles are in Germany (Aschheim/Karlsruhe, München ×2, Frankfurt am Main), so the geographic tier was tied; ranked by recency then Best-for overlap as usual.
- **Language track decisions:** all four postings are written entirely in German with no English requirement stated → DE track for all four, per the 20 July 2026 hard rule.

## Deliverable summary

- **4** new roles drafted, **32** files rendered (8 deliverables × 4 roles), all validated: 2-page CVs, banned strings (`toward B2`, `Databricks`, `Delta Lake`, `LangChain`, `PyTorch`) absent, retired PD-layout strings absent, only hyphen present is the allowed portfolio-URL identifier in the contact block, no parentheses.
- **4** CSV rows appended (`applied-log.csv`, now 212 data rows incl. the pre-existing duplicate pairs noted above).
- **1** CSV row's Status is unaffected by reconciliation (no real drift found); the ProSiebenSat.1 correction reported in the 17 September digest was already applied by that run and remains in place.
- **4** Notion rows created (verified via a follow-up SQL query: `Status = 'drafted'` count went from 6 to 10, matching CSV's 10 drafted rows exactly).
- Backlog now **10 drafted** in Notion, up from 6 at run start.
