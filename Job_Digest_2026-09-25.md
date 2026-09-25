# Job Digest, 25 September 2026

## Run type and render toolchain

Scheduled Cowork run. Render toolchain installed cleanly at run start:
`pip install weasyprint python-docx pypdf` succeeded, `import weasyprint,
docx, pypdf` printed `render toolchain ok 70.0`. No fallback to
Markdown only at any point.

## The bottom line

Three new roles drafted and ready to submit: retorio (Munich), KontextWork
(Hannover), and KWS SAAT (Einbeck). Along the way, reconciliation found a
real problem from earlier runs: six job applications that Notion says are
"ready to apply" actually have no CV or cover letter file anywhere. Nothing
was deleted or hidden about that, it is flagged below with a decision for
you. Separately, one of tonight's three (KontextWork) turned out to be a
repost of a role drafted twice before; I caught it late, kept it since the
posting is genuinely live again, and flagged exactly what happened below.

## Backlog gate

Notion query for Status = drafted at run start returned **6** rows (Atos,
Sopra Steria Custom Software Solutions GmbH, COBACK, coac GmbH, PRODIGY
Consulting GmbH, Reply Deutschland SE). 6 is under the 8 row floor, so the
28 July 2026 yield reset gate applies its normal top 3 to 5 cut. No
fallback to CSV counting was needed, Notion answered on the first query.

Backlog after this run: **9** drafted rows in Notion (6 carried over plus
3 new). CSV drafted count also reads 9 after this run's writes, the two
stay in sync.

## Reconciliation

**What I found, in plain terms:**

- Your spreadsheet had 5 rows still marked "drafted" from the 22 September
  run, but Notion already showed the real outcome for all 5: the Syneco
  Trading Masterarbeit (both the Xing row from 16 Sep and the
  company-portal row from 22 Sep) is now applied, Web Computing is
  applied, Modern Drive Technology is applied, and BLACKFIELD AI is
  rejected. I updated the spreadsheet to match Notion on all 5, since
  Notion is always the correct answer for status.
- **The one you need to look at:** six rows Notion shows as "drafted",
  created on 23 and 24 September (Atos, Sopra Steria Agentic Coding,
  COBACK, coac GmbH, PRODIGY Consulting, Reply Deutschland AI Business
  Solutions), have **no CV or cover letter file anywhere in the repo**,
  and there is no digest or git commit from either of those two dates
  either. In other words, whatever ran on 23 and 24 September wrote
  "ready to submit" into Notion but the actual documents were never
  created or saved. If OpenClaw tries to submit any of these six today,
  it will not find a PDF to upload and will correctly stop rather than
  submit nothing, but you should know now rather than find out then.
  - I did not try to guess and recreate those six CVs from the short
    notes Notion has on file, that felt too close to fabricating a
    result. I also cannot change Notion's status field myself, that is
    OpenClaw's job, not mine.
  - **Decision needed from you, pick one:**
    **A)** Tell me to research and draft the real 8 files for all six on
    a future run, treating them as a priority backlog item.
    **B)** Tell me to leave them as is and you will handle those six
    manually.
    **C)** Tell OpenClaw (or me) to flip those six rows back to some
    other status since they were never truly drafted.
  - I mirrored all six into applied-log.csv exactly as Notion has them
    (still marked drafted) so the two systems count the same number of
    rows, but the underlying files are still missing for all six.

## Top cut, 3 new roles

### 1. retorio GmbH, Munich
- **Role:** Working Student, AI Engineer, Agentic Systems (~20 hrs/week, 5 months)
- **Fit rationale:** Posting asks for agentic systems design (tool calling,
  MCP, retrieval, structured outputs) and rigorous evaluation via eval
  datasets, A/B testing, and observability tooling, plus GCP deployment.
  Near one to one match with the Multi Agent RAG project's LLM as Judge
  evaluation harness and the Movie Analytics pipeline's GCP Cloud Run and
  Cloud Scheduler deployment.
- **Projects selected:** Multi Agent RAG, Movie Analytics and ML Pipeline
- **Certs:** NVIDIA, AWS Academy, Google Data Analytics
- **Apply link:** stepstone.de listing 14400893
- **Apply method:** platform-native (StepStone Schnelle Bewerbung), in OpenClaw's scope
- **Language track:** EN (posting entirely in English, no German requirement)
- **Deliverables:** all 8 rendered, CV 2 pages, PDF validation clean

### 2. KontextWork GbR, Hannover
- **Role:** Werkstudent KI Engineer, Generative KI und LLM (16 to 20 hrs/week)
- **Fit rationale:** Role covers evaluating and building RAG systems and
  integrating LLMs into a business knowledge tool. Strong overlap with the
  Multi Agent RAG project's retrieval pipeline and CreditIQ's plain
  language LLM generated explanation for end users.
- **Projects selected:** Multi Agent RAG, CreditIQ
- **Certs:** NVIDIA, AWS Academy, Google Data Analytics
- **Apply link:** stepstone.de listing 13730672
- **Apply method:** platform-native (StepStone Schnelle Bewerbung), in OpenClaw's scope
- **Language track:** DE (posting entirely in German)
- **German level flag:** no explicit bar stated in the posting text, but a
  German language listing for a client facing Hannover role likely
  expects working German; noted for your own judgement, not used as a
  filter
- **Deliverables:** all 8 rendered, CV 2 pages, PDF validation clean
- **Correction, caught late:** this exact company and role was drafted
  twice before in this repo's history (one undated row, one dated 6 Sep
  2026), both ending in Not listed Anymore, using this same drafts folder
  name. My dedup check during search missed it because the role text had
  a comma in a different place ("KI Engineer Generative KI und LLM" vs
  "KI Engineer, Generative KI und LLM"). I only caught this at the git
  staging step, when the folder showed as modified instead of new. The
  posting is confirmed freshly live again via tonight's direct fetch,
  consistent with the company reposting a role that expired unfilled
  before, so I kept it as a legitimate re-application rather than
  withdrawing it, but flagging the process miss here and in Notion's
  Notes for the audit trail. Rah, let me know if you would rather I treat
  a repost like this as out of scope going forward.

### 3. KWS SAAT SE and Co KGaA, Einbeck
- **Role:** Working Student, Global IT, AI and LLM Solutions (20 hrs/week during studies)
- **Fit rationale:** Posting explicitly asks for RAG and GraphRAG
  contributions with response quality evaluation, plus systematic model
  evaluations and benchmarks on quality, security, and performance. This
  is the closest one to one match to the "AI Evaluation" scope of any
  role found this run, echoing the Multi Agent RAG evaluation harness and
  CreditIQ's systematic fairness benchmarking.
- **Projects selected:** Multi Agent RAG, CreditIQ
- **Certs:** NVIDIA, AWS Academy, Google Data Analytics
- **Apply link:** jobs.kws.com/job/... (job id 1440976433)
- **Apply method:** company-portal, out of OpenClaw's scope, you submit manually
- **Language track:** EN (posting content in English; explicitly accepts German or English)
- **Freshness:** posted 19 Sep 2026, updated within hours of this run per the source listing, the freshest lead found tonight
- **Deliverables:** all 8 rendered, CV 2 pages, PDF validation clean

## Watchlist (scored but not drafted)

None. Only 3 roles cleared verification tonight; nothing was held back
under the cap since the cap allowed up to 5.

## Dropped roles (found, then excluded)

Search conditions were unusually poor tonight, an unusual number of
promising leads turned out to be dead on verification:

- **CognitX AI GmbH**, AI/LLM Engineering Werkstudent, Darmstadt: posting
  dated November 2025, both known apply links (arbeitnow mirror, join.com)
  now return HTTP 410 Gone. Dropped, stale.
- **Ponturo Consulting AG**, Werkstudent AI Engineer, multiple cities: the
  only mirror with full details (studysmarter.de) now returns 410 Gone,
  and StepStone itself returned 503 (anti-bot) on every direct attempt to
  find a fresh listing. Dropped, unverifiable.
- **BMW Group**, Werkstudent Agentic AI, Munich: bmwgroup.jobs itself
  says "this vacancy is unfortunately no longer available." Dropped, closed.
- **Dussmann**, AI Werkstudent, Berlin: dussmann.jobs returned 503 on
  every attempt. Dropped, unverifiable.
- **Mercedes-Benz Tech Innovation**, AI Agents and Robotics Platform
  Werkstudent, Karlsruhe: arbeitsagentur.de mirror returned 410 Gone.
  Dropped, stale. (A different Mercedes-Benz Tech Innovation role is
  already logged and rejected from an earlier run.)

All five were dropped rather than drafted on stale information, per the
standing rule that every write must point to specific, checkable
evidence.

## Transparency block

- **Sources reachable this run:** StepStone (direct fetch worked for the
  2 roles ultimately selected from it), company career pages (direct
  fetch worked for KWS SAAT's jobs.kws.com), WebSearch generally.
- **Sources unreachable or degraded this run:** Tavily MCP failed to
  connect (consistent with recent runs). No Indeed MCP tool was available
  in this session, so Indeed was not used. StepStone's own site returned
  503 (anti-bot) on some direct listing-page fetches, though individual
  job detail pages fetched fine. Several third party job aggregator
  mirrors (studysmarter, arbeitnow, join.com, arbeitsagentur.de,
  dussmann.jobs) returned 410 Gone or 503 for postings this run, more
  than a typical run.
- **Freshness dating notes:** KWS SAAT's own listing states "Posted Sep
  19, 2026; Updated 6 hr. ago" at fetch time, the freshest of the three.
  retorio and KontextWork listings did not carry an explicit post date in
  the fetched content but were confirmed live via direct fetch.
- **Prompt injection content observed:** none this run.
- **Platform mix:** StepStone 2, Company Page 1. LinkedIn, Xing,
  JobTeaser, Indeed surfaced no new in-scope, verifiable, non-duplicate
  postings this run.
- **Distance was not a scoring factor**, per the standing rule. All 3
  roles are in Germany (Munich, Hannover, Einbeck), a single geographic
  tier.
- **Work type scope:** all 3 roles are Werkstudent / working student
  positions, in scope per the 22 September 2026 narrowing (mandatory
  internship and Master Thesis are out of scope; these three are neither).

## Deliverable summary

- 3 roles drafted, 24 files rendered (8 per role), all present on disk
- CV_Rahul_Rawat.pdf validated for all 3: 2 pages each, no banned strings
  (toward B2, Databricks, Delta Lake, LangChain, PyTorch), no retired PD
  block strings on page 1
- applied-log.csv: 5 status corrections (Syneco Trading x2, Web Computing,
  Modern Drive Technology, BLACKFIELD AI), 6 mirror rows added for the
  Notion-only orphan rows, 3 new drafted rows appended for tonight's roles
- Notion: 3 new pages created via create_pages with the correct
  data_source_id parent shape, verified with a follow-up query showing 9
  drafted rows, matching the CSV's 9 drafted count
