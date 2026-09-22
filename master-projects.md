# Master Projects Database — Rah

> Source file for automated job-search tailoring.
> For each role, the agent should select the 2–4 projects whose **Best for** tags
> and stack overlap most with the job description, then rewrite the bullets to
> mirror that posting's keywords. Always keep the metrics — they are real.
>
> **Format rule, 18 July 2026:** CV bullets use XYZ (accomplished X, as measured by Y, by doing Z), impact first. Interview answers translate the same project into STAR (Situation, Task, Action, Result), context first. Same substance, different shape per medium. Never speak a CV bullet verbatim in an interview, always retell it as STAR.

---

## Contact

- **Name:** Rahul Rawat
- **Email:** rahulrawat2r@gmail.com
- **Phone:** 015563603340
- **LinkedIn:** linkedin.com/in/rahulrawat2r/
- **GitHub:** github.com/rahulrawat20022002
- **Location:** Mannheim, Germany

## Education

- **M.Sc. Data Science & Analytics** — SRH University of Applied Sciences Heidelberg · 04.2025 – Present · GPA 1.9
- **Bachelor's in Computer Science** — GL Bajaj Institute of Technology and Management · 2019 – 2023 · CGPA 7.3 of 10
> **Routing note:** The Bachelor Thesis (Project #9 — Diabetes Prediction Using Machine Learning) does **NOT** render under Education. It renders as its own top-level **"Research & Thesis"** section, placed after Personal Projects (before Languages), using Project #9's full bullets below verbatim — not a shortened one-line summary.

---

## Languages

- **English:** fluent, professional working proficiency
- **German:** B1, currently in progress
> **Routing note:** Render this on the CV exactly as "German: B1, in progress" (plain prose, no parentheses). Update this line whenever the user's German level changes — do not leave it at a stale level.

---

## Certifications

- **NVIDIA, Building LLM Applications With Prompt Engineering.** Issued 12 November 2025. Certification ID 72WWI4mDQBCJoldHntPx0A. Verify at learn.nvidia.com.
- **AWS Academy Graduate, AWS Academy Cloud Foundations.** Issued 15 July 2025. 20 course hours. Credly badge at credly.com/go/aH6PwQeR.
- **SAS Certified Specialist, Visual Business Analytics Using SAS Viya.** Issued 7 May 2025, valid through 7 May 2030. Verification 7ef119722f564e1883359a1c29099a4a at cp.certmetrics.com/SAS.
- **Google Data Analytics, Foundations: Data, Data, Everywhere.** Issued 7 April 2025, Coursera. Verify at coursera.org/verify/343HREP8HIFE.

> **Routing note:** All four certificates are real and verifiable. Render them under a "Certifications" section on the CV. Pick the two or three most relevant to the posting; do not render all four when a role is not a strong fit. For LLM, RAG, Gen AI, or AI Engineer roles lead with NVIDIA. For cloud, data pipeline, or Data Engineer roles lead with AWS. For BI, Data Analyst, or Business Analyst roles lead with SAS Viya and Google Data Analytics. Never invent certificate titles, dates, or IDs.

---

## Achievements

- **USAII Global AI Hackathon 2026, Finalist at Graduate Level.** Event 14 June to 21 June 2026. Certificate issued 27 June 2026. Hackathon ID 830382652. Awarded by the United States Artificial Intelligence Institute for advancing to the Final Round through innovation, technical creativity, and applied AI on real world challenges.

> **Routing note:** Render this under an "Achievements" section on the CV, placed after Certifications and before Languages, and use it on every CV going forward. Never soften "Finalist" to something weaker; never inflate it to "Winner". Preserve the Hackathon ID as a verifiable reference in the bullet.

---

## Candidate targeting parameters

- **Target roles, 26 August 2026 narrowing:** AI Engineer, AI Evaluation only.
  This replaces the previous broader list (Data Engineer, Data Analyst,
  Business Analyst, Data Scientist, AI/ML Engineer, Researcher, Master
  Thesis) per Rah's live instruction on 26 August 2026. In scope: postings
  titled or scoped around AI Engineer, AI/ML Engineer, Machine Learning
  Engineer, LLM Engineer, Agentic AI Engineer, AI Evaluation Engineer,
  Applied AI or Model Evaluation, LLM-as-Judge or eval-harness work, and
  Responsible AI Evaluation. Plain Data Engineer, Data Analyst, Business
  Analyst, Data Scientist, and general Researcher postings are OUT of
  scope unless the posting itself reads squarely as an AI Engineer or AI
  Evaluation role. Master Thesis is no longer searched as a work type at
  all per the 22 September 2026 work types narrowing below.
- **Location:** anywhere in Germany; remote anywhere in EU
- **Work types, 22 September 2026 narrowing:** Werkstudent / part-time and
  Full-time / Junior full roles are IN scope. Per Rah's live instruction on
  22 September 2026, mandatory internship (Pflichtpraktikum required by the
  study programme) and Master Thesis (Masterarbeit / Abschlussarbeit) are
  now OUT of scope — Rah's enrollment window for those has closed and he
  cannot enroll for them anymore. Voluntary internship (freiwilliges
  Praktikum) is now IN scope, reversing the prior drop rule below, since
  Rah can still take one of those. This is a scope narrowing/reopening, not
  a data deletion: historical applied-log.csv and Notion rows already
  logged under Pflichtpraktikum or Masterarbeit remain untouched and keep
  their existing Status. Cowork must not widen scope back to mandatory
  internship or Master Thesis on its own judgement; only an explicit
  instruction from Rah reopens them.
- **Pay:** not a filter. Include unpaid and low-paid roles, including unpaid voluntary internships. Do not rank or drop by compensation.
- **German level:** B1, currently in progress — accept German-language listings, but flag the required German level (none / A2 / B1 / B2 / C1) per posting and compare it against this current B1 level
- **Base:** Mannheim — distance/commute is NOT a scoring factor. Rank by geographic tier first (all of Germany, remote or on-site, ahead of the rest of Europe), then by recency and "Best for" overlap. Note location and any relocation/on-site expectation in the digest as plain information only.
- **Search sources:** do not rely on Indeed alone. Also try StepStone, Xing, Glassdoor, LinkedIn Jobs, JobTeaser (jobteaser.com), and company career pages (via Claude in Chrome when connected). State in the digest which sources were reachable each run.
- **Drop from results:** dual-study / Duales Studium / apprenticeship programmes; recruiter "Quereinsteiger / career-changer" ads; mandatory internship (Pflichtpraktikum) and Master Thesis (Masterarbeit / Abschlussarbeit) postings per the 22 September 2026 work types narrowing above.

---

## 1. Multi-Agent RAG with LLM-as-Judge and Multilingual EN/DE Support
**One-liner:** Multi-agent Retrieval-Augmented Generation policy analysis system with LLM-as-Judge evaluation, AI eval harness, and full EN/DE multilingual support running locally.
**Stack:** Python, LangGraph multi agent, Ollama (Mistral 7B generator + Qwen2.5 14B judge), Pinecone, paraphrase-multilingual-MiniLM-L12-v2, spaCy, BM25 + dense hybrid retrieval
**Best for:** AI/ML Engineer, Data Scientist, LLM/RAG Engineer

- For an English-only hybrid BM25 plus dense RAG policy analysis system over a 14 document policy corpus that could not serve German speakers, tasked with adding multilingual support without duplicating the corpus, migrated embeddings and retrieval to a paraphrase multilingual MiniLM L12 v2 shared vector space so a German query retrieves English sources and is answered in German end to end.
- With every agent in the graph re running language detection and producing inconsistent output languages, tasked with a single source of truth, built a LanguageAgent that centralises seeded language detection with a confidence floor, propagates the output language directive to every downstream agent, and routes preprocessing to language matched spaCy pipelines with a blank multilingual fallback and per chunk language recording so retrieval and evaluation can slice by language.
- To measure answer quality without hand grading, implemented an LLM as Judge JudgeAgent scoring answers 1 to 5 on 5 dimensions (groundedness, relevance, completeness, citation quality, language quality) in JSON mode at temperature 0, and eliminated self preference bias by running the judge on a different local model Qwen2.5 14B from the generator Mistral 7B with a self_judged flag propagated into every report and a hard failure on missing judge model so a silent fallback to self judging cannot regress unnoticed.
- Built an EvalAgent computing 5 retrieval metrics (hit@k, precision@k, recall@k, MRR, nDCG@k) alongside 4 generation metrics (answer relevancy, context utilisation, citation density, language match rate) aggregated overall and per language into JSON and Markdown reports on a paired EN and DE labelled eval set, then ported the evaluator from the HuggingFace API to Ollama so retrieval, generation, judging and evaluation all run locally with Pinecone as the only remaining external service.
- Refactored for testability and performance by extracting all model, language, index and eval settings into a config.yaml behind a loader, added a build_pipeline factory so importing the orchestrator no longer requires Pinecone credentials, cached the retriever's encoder across searches instead of reloading per query, and switched document resolution to id lookup instead of id string parsing.

---

## 2. CreditIQ — Fairness-by-Design Credit Scoring System
**One-liner:** End-to-end credit-scoring system that flags and corrects bias before it reaches applicants; deployed decision-support tool.
**Stack:** Python, scikit-learn, AIF360, SHAP, Streamlit · Academic project, SRH Heidelberg
**Best for:** Data Scientist, AI/ML Engineer, Business Analyst (regulatory/risk angle)

- For an SRH Heidelberg project on regulated credit scoring where a baseline model was failing the EU AI Act and AGG 80 percent fairness bar, tasked with getting it back into compliance without gutting predictive quality, applied AIF360 mitigation and threshold calibration on a real credit dataset, which raised the Disparate Impact ratio from a failing 0.79 to a compliant 0.88.
- After single axis age bias was fixed but younger women were still being penalised, tasked with finding and correcting the hidden intersectional bias, used SHAP driven subgroup analysis to expose the pattern and designed a four way age by gender threshold matrix, which corrected it without over correcting into reverse discrimination.
- With a large false negative rate silently rejecting good applicants, tasked with cutting it while keeping overall accuracy defensible, documented the fairness accuracy trade off as a deliberate and regulator defensible decision, which brought the false negative rate down from 44 percent to 16.7 percent while accuracy held at 75 percent on the held out test split.
- Because a compliant model that only lives in a notebook is not decision support, tasked with delivering it to a finance manager, shipped a Streamlit decision support tool that gives a recommendation plus a plain language LLM generated explanation, backed the pipeline with unit tests at 100 percent branch coverage and a full regulatory write up spanning EU AI Act Annex III, GDPR, model card, and attack vectors, and cleared GDPR Article 22 and EU AI Act Article 14 human in the loop requirements.

---

## 3. Real-Time Flight Tracking Data Pipeline
**One-liner:** Cloud pipeline tracking live aircraft over Germany, joining each position to nearest airport, aircraft details, and weather; 128K+ records.
**Stack:** Python, PySpark, BigQuery, dbt, Apache Airflow, GCP (Dataproc, GCE, GCS), Tableau, TabPy, OAuth2 · MSc Data Engineering, SRH Heidelberg
**Best for:** Data Engineer, AI/ML Engineer (pipelines), Data Analyst

- For a Data Engineering module at SRH Heidelberg needing a real time joined view over live aircraft above Germany, tasked with the collection and enrichment layer, built Python collectors that poll the OpenSky Network API every 30 seconds and PySpark cleaning on Google Cloud that joins against airport, aircraft, and weather data across four sources, producing a clean joined table covering more than 128 thousand records.
- With raw collector output not being usable for analysis and each aircraft needing a nearest airport label, tasked with the modelling layer, shaped the data into analysis ready tables with dbt and computed each aircraft's nearest airport with PySpark for heavy lift, which produced consistent nearest airport labels across the historical dataset.
- Because manual reruns would kill the real time promise, tasked with automating refresh, orchestrated the whole system with Apache Airflow on GCS backed storage and Dataproc compute so that batch and real time layers refresh automatically every 15 minutes without operator intervention.
- With the pipeline sitting on data but no insight, tasked with the analytics surface, built a Tableau workbook backed by Python statistics through TabPy on the dbt aggregates as the feed, which surfaced the finding that air traffic drops 4.4 times in heavy rain and clusters around hubs like Frankfurt and Munich.

---

## 4. Lake Water Quality Forecasting (eRay GmbH Experience entry)
**CV heading:** eRay GmbH
**CV position title:** Data Scientist
**CV dates:** Oct 2025 to Mar 2026
> **Routing note:** On the CV this renders ONLY as "eRay GmbH" (bold heading) with "Data Scientist" as the italic position subtitle and the dates above. Do not use a case-study or project name as the heading, and do not co-list SRH University in the Experience heading.
**One-liner:** Recursive forecasting pipeline covering four water quality indicators for a German lake; a 6 month academic and industry collaboration.
**Stack:** Python, CatBoost, Prophet, scikit learn, MICE. Collaboration with eRay GmbH and SRH University. Oct 2025 to Mar 2026
**Best for:** Data Scientist, AI/ML Engineer, Data Engineer (orchestration)

- During a 6 month eRay GmbH and SRH Heidelberg collaboration to forecast lake water quality across 4 target indicators chlorophyll a, turbidity, pH and dissolved oxygen, built an end to end recursive time series pipeline over a 40 feature space with a per target lag suite lag_1h, lag_24h, lag_3d, lag_7d, lag_roll_mean_24h and lag_roll_std_24h.
- Benchmarked 6 candidates Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost and Prophet with strict tree constraints max_depth 4 and learning_rate 0.05, landed on CatBoost MultiQuantile at alpha 0.05, 0.5 and 0.85, producing asymmetric 80 percent prediction intervals that hug the 0 floor and chop the top 15 percent of summer ghost spikes.
- Made the September evaluation defensible with a 3 pass outlier system pH tightened from 0 to 14 down to 7.0 to 9.0, Oct and Nov caps of 15.0 on chlorophyll a and 50.0 on turbidity, and a rolling z-score at z>2.5 over 48 hours, and excluded 5 sparse sensors plus 3 concurrent proxies phycocyanin_abs, phycocyanin_abs_comp and toc, surfacing the honest R squared of 0.86 on dissolved oxygen and 0.81 on pH.
- Reconstructed Oct and Nov gaps with IterativeImputer MICE, ran full Memory Buffer recalculation across all 6 lag features, generated a synthetic winter canvas with 4 degree Celsius floor and 0.4 degree diurnal amplitude, then wrapped it all in an orchestrator with gate checks, ecological clips dissolved oxygen 4.0 to 18.0 and pH 6.0 to 9.0 and a 0.003 pH per hour velocity clamp.

---

## 5. Movie Analytics & ML Pipeline — Cloud-Native Data Platform
**One-liner:** End-to-end batch pipeline with medallion architecture and a pre-release "hit or miss" ML classifier; fully automated.
**Stack:** GCP (BigQuery, Cloud Run, GCS, Cloud Scheduler, BigQuery ML), Python, SQL, Looker Studio
**Best for:** Data Engineer, Data Analyst, AI/ML Engineer

- For a personal cloud data project on movie analytics that needed to run unattended on GCP, tasked with the ingestion and processing layer, built an end to end batch pipeline that pulls movie data from a public API into a GCS data lake and processes it through a 3 tier Bronze Silver Gold medallion architecture in BigQuery on Cloud Run, running on a fully automated Cloud Scheduler trigger with 0 manual interventions required.
- With raw ingested data being unfit for direct analytics, tasked with hardening the Silver layer, applied schema enforcement, safe type casting, deduplication via window functions and genre normalisation into a relational model, which held clean referential integrity across every downstream Gold table.
- Because a classifier trained on post release signals would leak the answer, tasked with a leakage free hit prediction, trained a BigQuery ML classifier that predicts whether a film will be a hit before release, deliberately splitting features into 2 tables so only pre release signals feed the model, and confirmed leakage free evaluation on the split.
- With business stakeholders needing concrete answers rather than raw tables, tasked with the analytics surface, built Gold layer aggregates and a 5 page Looker Studio dashboard answering questions on genre ROI, foreign language growth and release season timing plus an ML early warning view, and secured the system with a least privilege service account, Secret Manager, and a version controlled GitHub repo covering all code, SQL and schemas.

---

## 6. Hadoop-based Data Crawling and Processing Platform
**One-liner:** Distributed data-engineering pipeline using Docker Swarm and Hadoop.
**Stack:** Python (Selenium, BeautifulSoup, Pandas), Docker Swarm, Hadoop (HDFS), SQL Server
**Best for:** Data Engineer

- For a distributed data engineering project on e commerce data at scale, tasked with the cluster layer, orchestrated a distributed Hadoop cluster with one Name Node and three Data Nodes on Docker Swarm, which delivered automated container management and self healing on node failure.
- Because dynamic paginated e commerce pages were fragile to scrape and each network hiccup risked lost data, tasked with the collection layer, built a decoupled web scraping pipeline with Python and Selenium that navigates dynamic paginated results and saves raw HTML locally for data safety, which allowed clean re runs against the saved raw pages.
- With sponsored click tracking URLs and missing fields corrupting the extracted product list, tasked with the parsing layer, engineered a robust BeautifulSoup parser that handles missing data and decodes sponsored click tracking URLs into clean product links, which held up against a manual verification set for parser correctness.
- Because the platform was only worth the effort if the storage was durable and query ready, tasked with the storage and handoff layer, ingested structured CSVs into HDFS and ran redundancy tests that confirmed consistent block replication counts across the three Data Nodes, then extracted processed data into SQL Server for downstream analysis.

---

## 7. Fast Food Nutritional Analyzer & Meal Simulator
**One-liner:** Interactive 2-page Tableau dashboard with a dynamic "Meal Cart" simulator optimising macros to fitness goals.
**Stack:** Tableau (Set Actions, Dashboard Actions, parameters, calculated fields), data storytelling, UI/UX
**Best for:** Data Analyst, Business Analyst
**Showcase:** https://public.tableau.com/shared/YC6Y4ZBM5

- For a Tableau dashboard project where users needed to explore fast food nutrition and simulate a meal rather than just filter charts, tasked with the interaction layer, built a dynamic shopping cart using Tableau Set Actions so end users can select scatter plot points and instantly total the 3 key macros calories, fat and protein for a simulated meal.
- With 1 static Y axis being unable to serve both a muscle gain and a weight loss goal, tasked with letting the viewer switch objective without reloading, implemented parameter driven analytics with a dynamic Y axis tied to a user controlled goal parameter using a CASE statement, which produced consistent axis switching across 2 objectives without dashboard reloads.
- Because deceptive high fat and high calorie items were reading as safe on the raw data, tasked with surfacing them, authored complex order of operation IF and THEN calculated fields for logical grouping and custom flags such as an Is It A Trap flag, which flagged the trap items correctly on manual spot checks against the source nutrition data.
- For a non technical stakeholder who needed both the big picture and the deep dive, tasked with the layout, designed a 2 tier view combining an executive macro view and a granular food finder in a colour blind safe dark mode palette, which met the target of reduced time to insight in stakeholder feedback.

---

## 8. Economic Impact Analysis of Global Climate Events
**One-liner:** End-to-end predictive-analytics & BI study turning raw global-event data into business-relevant insight.
**Stack:** Python (Pandas, Scikit-Learn), Matplotlib/Seaborn, Random Forest, statistical modelling
**Best for:** Data Analyst, Business Analyst, Data Scientist

- For a data science project needing to turn raw global climate event data into decision support for resource allocation and risk assessment, tasked with the full analytics pipeline, executed an end to end project from ingestion to stakeholder report, delivered as a single reproducible pipeline from raw CSV to a management ready output.
- With the raw data carrying outliers, missing values, and inconsistent scales that would poison any downstream model, tasked with building a clean foundation, performed advanced data preparation and cleansing over outliers, imputation, and normalisation, which held stable model performance before and after feature scaling.
- Because the business question was where economic risk actually concentrates, tasked with the modelling layer, developed Random Forest models to analyse correlations between event duration and financial impact, and read the results through feature importance rankings and residual analysis, which produced clear business relevant insights on the risk concentration.
- With the audience being non technical stakeholders rather than data scientists, tasked with the communication layer, produced comprehensive visual reports and calibrated confidence statements, which survived a management review without further translation.

---

## 10. Family Business Front End Development (SS Engineers and Contractors, two Experience entries)
**CV heading:** SS Engineers and Contractors
**CV location:** India
> **Routing note:** Per the 2 August 2026 rule in CLAUDE.md, this project renders as TWO separate Experience entries under the same company, in reverse chronological order below eRay GmbH. Entry 2 is the full time role, Entry 3 is the internship. Never merge them into a single compound entry. Rah holds a signed experience letter for both roles, available for background checks and reference calls.
**One-liner:** Multi year role at the family owned engineering and contracting firm, contributing React UI components on internal Data Dashboards, Analytics platforms, and Employee Portals used across the company, plus a client migration from a legacy AngularJS app to React inside an existing module federation setup. Started as a six month front end intern, then hired full time as Junior Associate Software Developer.
**Stack:** React, module federation, Playwright end to end testing, AngularJS familiarity for the legacy side of a client migration, HTML5, CSS3, Git, npm, cross browser testing, code review workflow with pull requests
**Best for:** Front End Developer, React Developer, Web Developer, and supporting entry for Data Analyst, Data Engineer, and Business Analyst roles that value experience building internal dashboards and analytics platforms

**Entry 2, full time role**
**CV position title:** Junior Associate Software Developer
**CV dates:** Aug 2023 to Aug 2024
**Full time bullets:**
- With SS Engineers and Contractors running internal Data Dashboards, Analytics platforms, and Employee Portals used across the company, tasked with building and maintaining the front end features that day to day teams depended on, contributed React UI components across all three internal products, which stayed in daily use by internal teams across the company throughout the year in role.
- With a client relying on a legacy AngularJS app that had to sit inside an existing module federation setup alongside newer React micro frontends, tasked with porting the client's screens across without breaking the running product, ported around 8 routes from AngularJS to React inside the module federation shell over 4 months of incremental releases, shipped with no production incidents during rollout.
- With the same client migration surfacing shared UI patterns and a session boundary between the legacy AngularJS side and the new React side, tasked with keeping the migration code reusable rather than one off, wrote a set of reusable React UI components and an auth compatibility shim that bridged the legacy session shape to the new React app, both of which were later picked up by other developers on a team of 4.
- As the internal platforms and the client migration were both moving in parallel and regressions were slipping through manual QA, tasked with adding automated coverage, added Playwright end to end tests across the internal platform work and the client migration work, covering the main user flows so regressions on those flows were caught before release rather than after.

**Entry 3, internship**
**CV position title:** Front End Developer Intern
**CV dates:** Feb 2023 to July 2023
**Internship bullets:**
- During a six month internship at SS Engineers and Contractors, tasked with learning the codebase and then taking on small UI work across the internal Data Dashboards and Employee Portals under senior review, paired closely with senior developers to walk the codebase and then shipped focused UI components including charts, filters, and profile pages, iterating each one on code review feedback until it landed.
- With intern code going straight into internal products that other teams used every day, tasked with catching problems earlier in the loop, fixed bugs across the parts of the codebase I worked on, wrote tests to cover the code I contributed, and helped the QA team investigate new issues as they came in, so problems on my areas were caught in review or in automated tests rather than in QA.

---

## 9. Bachelor Thesis — Diabetes Prediction Using Machine Learning
**One-liner:** Published-grade ML study comparing 6 classifiers on a real clinical dataset; honest, leakage-aware evaluation.
**Stack:** Python, Scikit-Learn, Pandas, Seaborn, Google Colab · IEEE-style paper
**Best for:** Data Scientist, AI/ML Engineer
> **26 August 2026 note:** Rendering of this project as the standalone
> "Research and Thesis" section is now gated by the `SHOW_BACHELOR_THESIS`
> switch in build_html.py, **default `False`** (hidden) per Rah's 26
> August 2026 instruction. See CLAUDE.md's dated rule for how to flip it
> back on. The routing note below (no render under Education, own
> top-level section, full bullets verbatim) still describes how it renders
> whenever the switch is `True`.

- For a Bachelor thesis on diabetes prediction with a small clinical dataset of 768 patients, tasked with building a defensible model comparison the examiners could audit, built a full end to end machine learning pipeline comparing six classifiers with 10 fold cross validation and per model confusion matrices, delivering a model comparison that stood up in the thesis defence.
- Spotting biologically impossible zero values in the source data that the original authors had overlooked, tasked with restoring data integrity before any model fit, applied IQR based outlier removal and proper imputation, which lifted the dataset from silently broken to a clean training input for every downstream model.
- With a 65 to 35 class imbalance that made accuracy a misleading headline metric, tasked with choosing an evaluation that would not hide errors on the minority class, moved the headline metric from accuracy to ROC AUC, which exposed the real error patterns the accuracy score had been masking and gave the thesis an honest performance comparison.
- With the results needing to be publishable in substance rather than just submissible, tasked with writing them up formally, produced an IEEE style paper including an honest limitations section and what to do differently in a follow up study, which the supervisor accepted as publishable in substance.

---

> **26 August 2026 scope note:** Active search targeting is AI Engineer and
> AI Evaluation only (see Candidate targeting parameters above). The
> role-to-project map below is retained as reference for tailoring within
> AI Engineer / AI Evaluation postings and in case scope widens again;
> the Data Engineer, Data Analyst, Business Analyst, and plain Data
> Scientist rows are not currently used for search targeting.

## Quick role → project map (for fast scoring)

- **Data Engineer:** #3 Flight Tracking, #5 Movie Analytics, #6 Hadoop, #4 Lake (orchestration)
- **Data Analyst:** #7 Fast Food Tableau, #8 Climate Economics, #5 Movie Analytics, #3 Flight Tracking
- **Business Analyst:** #8 Climate Economics, #7 Fast Food Tableau, #2 CreditIQ (risk/regulatory)
- **Data Scientist:** #2 CreditIQ, #4 Lake Forecasting, #9 Diabetes Thesis, #1 RAG
- **AI/ML Engineer:** #1 RAG Orchestrator, #2 CreditIQ, #9 Diabetes Thesis, #4 Lake, #3 Flight Tracking
- **Experience section, both entries always rendered in reverse chronological order per the 2 August 2026 rule in CLAUDE.md:** #4 eRay GmbH Data Scientist (Oct 2025 to Mar 2026), then #10 SS Engineers and Contractors Junior Associate Software Developer (Aug 2023 to Aug 2024) with the preceding six month Front End Developer Internship from Feb 2023 to July 2023. #10 is an Experience entry, never selected under Personal Projects.
