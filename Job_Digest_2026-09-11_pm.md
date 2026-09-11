# Job Digest — 11 September 2026 (second run, PM)

**Run type:** Scheduled Cowork Drafting Agent (Agent A) run. This is the
second scheduled invocation for 11 September 2026 — the first run (digest
at `Job_Digest_2026-09-11.md`, logged 13:32) hit a total search source
outage (Tavily unreachable, WebFetch egress blocked everywhere) and drafted
0 roles. This run found Tavily reachable again; WebFetch remained
egress blocked for every domain tested (`linkedin.com`, `stepstone.de`),
same as the last two runs.

**Render toolchain:** weasyprint 70.0, python-docx 1.2.0, pypdf 6.18.1
installed clean. `import weasyprint, docx, pypdf` succeeded. No fallback to
Markdown only needed.

---

## Backlog gate result

Queried Notion data source `fd974369-40b2-48c5-b660-d15256c88f52` for
`Status = 'drafted'` at run start: **0 rows**. (The 1 row carried into the
13:32 run today, Estateanfrage Inh. Fabian Kroner, had moved to `rejected`
in Notion between the two runs today — not a Cowork or OpenClaw write,
presumably Rah reviewing it manually.)

0 drafted is well under the 8 row floor of the 28 July 2026 yield reset, so
the **normal top 3 to 5 cut** applied. Backlog after this run: **3
drafted** in Notion.

## Reconciliation result

Read all 201 rows in `applied-log.csv` (before this run's new additions)
and matched each against Notion by company plus role, case insensitive,
with diacritic folding.

**Drift found and fixed: 3 CSV rows.** Notion (source of truth) showed
`rejected`; the CSV still said `applied` or `drafted`:

| Company | Role | CSV was | Notion is (now applied to CSV) |
|---|---|---|---|
| Rosenberger Hochfrequenztechnik GmbH und Co. KG | Werkstudent, fuer KI Projekte | applied | rejected |
| EXXETA | Werkstudent, AI und LLM Engineering | applied | rejected |
| Estateanfrage Inh. Fabian Kroner | Werkstudent AI Engineer (m/w/d) | drafted (2nd CSV copy; 1st copy already read rejected) | rejected |

No CSV rows were missing a Notion counterpart. No new Notion rows needed
creating during reconciliation. Only the CSV was written this run.

## Top cut

Three roles drafted, all cleared full verification (live posting fetched
directly via Tavily extract, confirmed apply link, clean dedup check).

### 1. FZI Forschungszentrum Informatik — Karlsruhe
**Masterarbeit, Evaluation and Verification of AI Generated Driving
Scenarios Using Scenario Dreamer**
- **Fit rationale:** FZI's Eingebettete Systeme und Mikrosysteme (ESM)
  department develops, evaluates and tests AI models with a strong focus
  on the automotive sector, and generative AI for images and video. This
  is squarely AI Evaluation flavored under the 26 August 2026 scope
  narrowing — a rigorous evaluation and verification thesis for
  generative outputs.
- **Projects selected:** Multi Agent RAG with LLM as Judge (JudgeAgent /
  EvalAgent evaluation harness), CreditIQ fairness by design credit
  scoring (quantitative, regulator grade evaluation methodology). Auto
  trim ladder reduced to 1 project to hold the 2 page cap.
- **Certs:** NVIDIA, AWS, Google Data Analytics (NVIDIA led per the LLM
  and RAG role routing note).
- **Apply link:** https://www.xing.com/jobs/karlsruhe-student-abschlussarbeit-master-thema-evaluation-and-verification-of-ai-generated-driving-scenarios-using-scenario-dreamer-152602249
- **Apply method:** unset in Notion, pending OpenClaw's platform-native vs
  company-portal determination — Xing job pages sometimes redirect to an
  external ATS and this was not independently confirmed from the scraped
  content.
- **Language track:** DE (posting body in German). The posting's own
  German level requirement was not visible in the scraped content (the
  "Das bringst Du mit" requirements bullet list did not render in the
  extract, likely JS rendered) — flagging as unconfirmed rather than
  assuming it matches Rah's B1 in progress level.
- **Deliverables:** all 8 rendered, CV 2 pages, all validation checks
  passed.

### 2. ProSiebenSat.1 Careers — Muenchen
**Working Student, AI Engineer** (AI Tech — Personalization team)
- **Fit rationale:** Works on recommendation systems for movie, series and
  live TV experiences; the role explicitly explores and evaluates new
  machine learning methods including LLM applications for recommender
  systems. Strong AI Engineer match, and the Movie Analytics project gives
  a genuine domain overlap (movie and entertainment data pipeline).
- **Projects selected:** Multi Agent RAG with LLM as Judge, Movie
  Analytics and ML Pipeline (leakage free hit prediction classifier,
  BigQuery, Looker Studio). Auto trim reduced to 1 project.
- **Certs:** NVIDIA, AWS, Google Data Analytics.
- **Apply link:** https://www.stepstone.de/stellenangebote--working-student-ai-engineer-m-f-d-muenchen-prosiebensat-1-careers--13800397-inline.html
- **Apply method:** unset in Notion, pending OpenClaw's determination.
- **Language track:** EN (posting body entirely in English, no German
  requirement stated).
- **Deliverables:** all 8 rendered, CV 2 pages, all validation checks
  passed.

### 3. iLert GmbH — Cologne
**Working Student or Intern, AI Product Engineer**
- **Fit rationale:** Builds Autonomous AI SRE agents that investigate,
  analyse and mitigate production issues; role covers designing agent
  reasoning loops, prompt templates, and building guardrails and
  validation layers so agents act safely and deterministically. Strong
  overlap with the LanguageAgent confidence floor and JudgeAgent hard
  failure design in the RAG project, and with CreditIQ's safety and
  regulatory compliance framing.
- **Projects selected:** Multi Agent RAG with LLM as Judge, CreditIQ
  fairness by design credit scoring. Auto trim reduced to 1 project.
- **Certs:** NVIDIA, AWS, Google Data Analytics.
- **Apply link:** https://www.stepstone.de/stellenangebote--Working-Student-Intern-AI-Product-Engineer-f-m-x-Cologne-iLert-GmbH--13513211-inline.html
- **Apply method:** unset in Notion, pending OpenClaw's determination.
- **Language track:** EN (posting body entirely in English, no German
  requirement stated).
- **Deliverables:** all 8 rendered, CV 2 pages, all validation checks
  passed.

## Watchlist

None held back under the cap this run (only 3 candidates cleared full
verification; nothing was scored but excluded for capacity reasons).

## Dropped section

Candidates found via search but not drafted, with reasons:

- **CognitX AI GmbH**, AI / LLM Engineering Werkstudent, Darmstadt (Xing) —
  strong scope match on the search snippet, but the live Xing page
  returned "This job ad isn't available" on direct extract. Same posting
  flagged unverified in the 13:32 run's watchlist; now confirmed expired
  or removed. Dropped, not drafted from a stale snippet.
- **bundesweit.digital GmbH**, Werkstudent KI Prompting / Prompt Engineer,
  Hanover (StepStone) — the direct StepStone URL 404'd ("Error - Page not
  found") on extract. Dropped.
- **Prelytics**, Praktikant LLM/RAG and Machine Learning Engineer,
  remote/Germany (LinkedIn) — confirmed live, but the posting states the
  internship is unpaid ("dieses Praktikum ist unverguetet") at a young
  startup with no Pflichtpraktikum framing tied to a study programme.
  Dropped under the standing voluntary internship (freiwilliges Praktikum)
  exclusion in the Candidate targeting parameters.
- **Cinemo GmbH**, Working Student GenAI/LLM Evaluation Agentic AI/NLP,
  Karlsruhe (StepStone) — resurfaced in search, but duplicates a company
  plus role pair already logged in Notion and the CSV as `applied`. Not
  redrafted.
- **Mercedes-Benz Tech Innovation** ("Software Development, AI Entwicklung,
  LLM's", Karlsruhe), **Reply Deutschland SE** ("Werkstudent Artificial
  Intelligence", Frankfurt), **Transdev GmbH** ("Werkstudentin Kuenstliche
  Intelligenz/AI Engineering", Berlin), and **Atruvia AG** ("Werkstudent
  Generative AI / Agentic AI", Karlsruhe) all surfaced only as aggregator
  "similar jobs" sidebar entries or generic listing snippets, with no
  independently fetchable posting URL confirming the exact role, apply
  link, or whether it duplicates an existing tracked row at the same
  company. None drafted, per invariant 4 (every write must be auditable) —
  fabricating an apply link or role detail from a sidebar snippet would
  violate that invariant even if the company plus title looks plausible.
- **NXP Semiconductors**, Working Student AI Automation Engineer — Quality
  Automation, Hamburg (StepStone) — confirmed live, but on the full
  description the AI component is a minor part (roughly 20 to 30 percent)
  of a quality gate and release readiness automation role; read as a QA
  automation role with light AI assistance rather than an AI Engineer or
  AI Evaluation role under the 26 August 2026 scope narrowing. Dropped.

## Transparency block

- **Sources reachable:** Tavily search and Tavily extract, both working
  cleanly this run (a clear improvement over the 9 and 11 Sep 13:32 runs,
  where Tavily itself was down).
- **Sources unreachable:** WebFetch returned `EGRESS_BLOCKED` for every
  domain tested this run (`www.linkedin.com`, `www.stepstone.de`), the
  same blanket network policy block seen in the two prior runs. Per the
  proxy README, this is an organization policy denial, not retried or
  routed around. LinkedIn and StepStone content was instead reached via
  Tavily extract, which worked where WebFetch did not.
- **No Indeed MCP tool** was available in this session's tool list,
  consistent with prior runs; Indeed searched via Tavily only, yielded
  nothing new in scope.
- **No prompt injection content observed** in any fetched posting this
  run.
- **Platform mix:** Xing 1, StepStone 2, of 3 drafted. LinkedIn and
  JobTeaser searched but yielded only already tracked roles or
  unverifiable sidebar snippets; not used this run.
- **Distance was not a scoring factor.** All three drafted roles fall in
  the single Germany geographic tier; ranked by recency then Best for
  overlap within that tier.
- **Language track decisions:** 1 DE (FZI), 2 EN (ProSiebenSat.1, iLert),
  each matching the posting body's own language per the 20 July 2026 rule.
- **Recommended fix for Rah:** none needed this run on the search side —
  Tavily recovered on its own. The WebFetch egress block for job boards
  remains unresolved across three consecutive runs (9 Sep, 11 Sep AM,
  11 Sep PM); Tavily extract is working around it adequately for now, but
  if Tavily ever goes down again at the same time WebFetch is blocked,
  search will halt entirely as it did in the 13:32 run today.

## Deliverable summary

- **3** new roles drafted, **24** deliverables rendered (8 per role), all
  validated (2 pages, no banned strings, correct Ojas style header).
- **3** CSV rows appended for new roles.
- **3** Notion rows created for new roles, verified present via follow up
  query.
- **3** CSV rows corrected during reconciliation to match Notion's
  authoritative status.
- Backlog now **3** drafted in Notion (up from 0 at this run's start).
