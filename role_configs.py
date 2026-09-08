"""Role configurations for the 15 July 2026 run."""

# ---- Reusable experience block (eRay GmbH, Project #4 in substance) ----
ERAY_BULLETS_EN = [
    "During a 6 month eRay GmbH and SRH Heidelberg collaboration to forecast lake water quality across 4 target indicators chlorophyll a, turbidity, pH and dissolved oxygen, built an end to end recursive time series pipeline over a 40 feature space with a per target lag suite lag_1h, lag_24h, lag_3d, lag_7d, lag_roll_mean_24h and lag_roll_std_24h.",
    "Benchmarked 6 candidates Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost and Prophet with strict tree constraints max_depth 4 and learning_rate 0.05, landed on CatBoost MultiQuantile at alpha 0.05, 0.5 and 0.85, producing asymmetric 80 percent prediction intervals that hug the 0 floor and chop the top 15 percent of summer ghost spikes.",
    "Made the September evaluation defensible with a 3 pass outlier system pH tightened from 0 to 14 down to 7.0 to 9.0, Oct and Nov caps of 15.0 on chlorophyll a and 50.0 on turbidity, and a rolling z score at z>2.5 over 48 hours, and excluded 5 sparse sensors plus 3 concurrent proxies phycocyanin_abs, phycocyanin_abs_comp and toc, surfacing the honest R squared of 0.86 on dissolved oxygen and 0.81 on pH.",
    "Reconstructed Oct and Nov gaps with IterativeImputer MICE, ran full Memory Buffer recalculation across all 6 lag features, generated a synthetic winter canvas with 4 degree Celsius floor and 0.4 degree diurnal amplitude, then wrapped it all in an orchestrator with gate checks, ecological clips dissolved oxygen 4.0 to 18.0 and pH 6.0 to 9.0 and a 0.003 pH per hour velocity clamp.",
]

ERAY_BULLETS_DE = [
    "In einer 6 monatigen Zusammenarbeit zwischen eRay GmbH und SRH Hochschule Heidelberg zur Prognose der Seewasserqualität über 4 Ziel Indikatoren Chlorophyll a, Trübung, pH und gelösten Sauerstoff wurde eine end to end rekursive Zeitreihen Pipeline über einen 40 Feature Raum mit einem Ziel Lag Set lag_1h, lag_24h, lag_3d, lag_7d, lag_roll_mean_24h und lag_roll_std_24h aufgebaut.",
    "Es wurden 6 Kandidaten direkt verglichen Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost und Prophet mit strikten Tree Einschränkungen max_depth 4 und learning_rate 0.05, die Entscheidung fiel auf CatBoost MultiQuantile bei alpha 0.05, 0.5 und 0.85, was asymmetrische 80 Prozent Vorhersageintervalle lieferte, die den 0 Boden umarmen und die oberen 15 Prozent der Sommer Ghost Spikes abschneiden.",
    "Die September Evaluation wurde belastbar gemacht mit einem 3 Pass Outlier System pH verengt von 0 bis 14 auf 7.0 bis 9.0, Oct und Nov Caps von 15.0 bei Chlorophyll a und 50.0 bei Trübung, ein rollender z score bei z>2.5 über 48 Stunden, und 5 spärliche Sensoren plus 3 zeitgleiche Proxies phycocyanin_abs, phycocyanin_abs_comp und toc wurden ausgeschlossen, was die ehrliche R quadrat Aufteilung von 0.86 bei gelöstem Sauerstoff und 0.81 bei pH offenlegte.",
    "Oct und Nov Lücken wurden mit IterativeImputer MICE rekonstruiert, eine vollständige Memory Buffer Neuberechnung über alle 6 Lag Features durchgeführt, ein synthetisches Winter Canvas mit 4 Grad Celsius Boden und 0.4 Grad diurnaler Amplitude generiert und das Ganze in einen Orchestrator mit Gate Checks, ökologischen Clips gelöster Sauerstoff 4.0 bis 18.0 und pH 6.0 bis 9.0 und einem 0.003 pH pro Stunde Velocity Clamp eingebettet.",
]

# ---- Research and Thesis (Project #9 Diabetes) ----
DIABETES_BULLETS_EN = [
    "For a Bachelor thesis on diabetes prediction with a small clinical dataset of 768 patients, tasked with building a defensible model comparison the examiners could audit, built a full end to end machine learning pipeline comparing six classifiers with 10 fold cross validation and per model confusion matrices, delivering a model comparison that stood up in the thesis defence.",
    "Spotting biologically impossible zero values in the source data that the original authors had overlooked, tasked with restoring data integrity before any model fit, applied IQR based outlier removal and proper imputation, which lifted the dataset from silently broken to a clean training input for every downstream model.",
    "With a 65 to 35 class imbalance that made accuracy a misleading headline metric, tasked with choosing an evaluation that would not hide errors on the minority class, moved the headline metric from accuracy to ROC AUC, which exposed the real error patterns the accuracy score had been masking and gave the thesis an honest performance comparison.",
    "With the results needing to be publishable in substance rather than just submissible, tasked with writing them up formally, produced an IEEE style paper including an honest limitations section and what to do differently in a follow up study, which the supervisor accepted as publishable in substance.",
]

DIABETES_BULLETS_DE = [
    "Für eine Bachelorarbeit zur Diabetesvorhersage auf einem kleinen klinischen Datensatz von 768 Patientinnen und Patienten, mit dem Auftrag einen belastbaren Modellvergleich zu liefern, den die Prüfer nachprüfen können, wurde eine vollständige end to end Machine Learning Pipeline mit sechs Klassifikatoren, 10 facher Kreuzvalidierung und pro Modell erstellten Konfusionsmatrizen aufgebaut, was einen Modellvergleich ergab, der in der Verteidigung standhielt.",
    "Nach dem Erkennen biologisch unmöglicher Nullwerte in den Quelldaten, die die Originalautoren übersehen hatten, mit dem Auftrag die Datenintegrität vor jedem Modelltraining wiederherzustellen, wurde eine IQR basierte Ausreißerbehandlung und saubere Imputation angewandt, was den Datensatz von still fehlerhaft zu einer sauberen Trainingsgrundlage für jedes nachgelagerte Modell brachte.",
    "Bei einer 65 zu 35 Klassenungleichgewicht Verteilung, die Genauigkeit zu einer trügerisch schönen Leitmetrik gemacht hätte, mit dem Auftrag eine Bewertung zu wählen, die Fehler in der Minderheitsklasse nicht verdeckt, wurde die Leitmetrik von Genauigkeit auf ROC AUC umgestellt, was die realen Fehlermuster offenlegte, die die Genauigkeitszahl maskiert hatte und der Arbeit einen ehrlichen Leistungsvergleich gab.",
    "Da die Ergebnisse in der Substanz veröffentlichungsreif und nicht nur abgabefähig sein sollten, mit dem Auftrag sie formal aufzuschreiben, wurde ein IEEE Paper mit einem ehrlichen Abschnitt zu Grenzen und Verbesserungsvorschlägen für eine Folgestudie verfasst, das der Betreuer als in der Substanz veröffentlichungsreif akzeptierte.",
]

# ---- Certificates ----
# ---- SS Engineers and Contractors, full time role, Aug 2023 to Aug 2024 ----
SATENDRA_FT_BULLETS_EN = [
    "With SS Engineers and Contractors running internal Data Dashboards, Analytics platforms, and Employee Portals used across the company, tasked with building and maintaining the front end features that day to day teams depended on, contributed React UI components across all three internal products, which stayed in daily use by internal teams across the company throughout the year in role.",
    "With a client relying on a legacy AngularJS app that had to sit inside an existing module federation setup alongside newer React micro frontends, tasked with porting the client's screens across without breaking the running product, ported around 8 routes from AngularJS to React inside the module federation shell over 4 months of incremental releases, shipped with no production incidents during rollout.",
    "With the same client migration surfacing shared UI patterns and a session boundary between the legacy AngularJS side and the new React side, tasked with keeping the migration code reusable rather than one off, wrote a set of reusable React UI components and an auth compatibility shim that bridged the legacy session shape to the new React app, both of which were later picked up by other developers on a team of 4.",
    "As the internal platforms and the client migration were both moving in parallel and regressions were slipping through manual QA, tasked with adding automated coverage, added Playwright end to end tests across the internal platform work and the client migration work, covering the main user flows so regressions on those flows were caught before release rather than after.",
]

SATENDRA_FT_BULLETS_DE = [
    "Da SS Engineers and Contractors interne Data Dashboards, Analytics Plattformen und Mitarbeiter Portale betreibt, die unternehmensweit genutzt werden, mit dem Auftrag die Frontend Features zu bauen und zu pflegen, auf die die Teams im Alltag angewiesen sind, wurden React UI Komponenten in allen drei internen Produkten beigetragen, die während des gesamten Jahres in der Rolle im täglichen Einsatz der internen Teams blieben.",
    "Bei einem Kunden, dessen Legacy AngularJS Anwendung in einem bestehenden Module Federation Setup neben neueren React Micro Frontends laufen sollte, mit dem Auftrag die Screens des Kunden zu portieren ohne das laufende Produkt zu brechen, wurden rund 8 Routen von AngularJS auf React innerhalb der Module Federation Shell portiert, ausgeliefert über 4 Monate in schrittweisen Releases und ohne Produktionsausfälle während des Rollouts eingespielt.",
    "Da die gleiche Kunden Migration wiederkehrende UI Muster und eine Session Grenze zwischen der Legacy AngularJS Seite und der neuen React Seite aufzeigte, mit dem Auftrag den Migrations Code wiederverwendbar statt einmalig zu halten, wurden gemeinsam genutzte React UI Komponenten sowie ein Auth Kompatibilitäts Shim geschrieben, das die alte Session Form auf die neue React App überträgt, beide wurden später von weiteren Entwicklern in einem 4 köpfigen Team übernommen.",
    "Als die internen Plattformen und die Kunden Migration parallel liefen und Regressionen durch manuelles QA rutschten, mit dem Auftrag automatisierte Abdeckung hinzuzufügen, wurden Playwright End to End Tests über die interne Plattformarbeit und die Kunden Migration hinweg ergänzt, die die Haupt Nutzerflows abdecken, so dass Regressionen auf diesen Flows vor dem Release erkannt wurden statt danach.",
]

# ---- SS Engineers and Contractors, internship, Feb 2023 to July 2023 ----
SATENDRA_INTERN_BULLETS_EN = [
    "During a six month internship at SS Engineers and Contractors, tasked with learning the codebase and then taking on small UI work across the internal Data Dashboards and Employee Portals under senior review, paired closely with senior developers to walk the codebase and then shipped focused UI components including charts, filters, and profile pages, iterating each one on code review feedback until it landed.",
    "With intern code going straight into internal products that other teams used every day, tasked with catching problems earlier in the loop, fixed bugs across the parts of the codebase I worked on, wrote tests to cover the code I contributed, and helped the QA team investigate new issues as they came in, so problems on my areas were caught in review or in automated tests rather than in QA.",
]

SATENDRA_INTERN_BULLETS_DE = [
    "Während eines sechsmonatigen Praktikums bei SS Engineers and Contractors, mit dem Auftrag die Codebasis kennenzulernen und dann unter Senior Review kleinere UI Arbeiten in den internen Data Dashboards und Mitarbeiter Portalen zu übernehmen, wurde eng mit Senior Entwicklern durch die Codebasis gegangen und anschließend wurden fokussierte UI Komponenten wie Charts, Filter und Profilseiten geliefert, jede iterativ auf Basis von Code Review Feedback verbessert bis sie freigegeben war.",
    "Da der Praktikanten Code direkt in interne Produkte ging, die andere Teams täglich nutzten, mit dem Auftrag Probleme früher im Prozess abzufangen, wurden Bugs in den Bereichen der Codebasis behoben an denen ich arbeitete, Tests für den beigetragenen Code geschrieben und dem QA Team bei der Untersuchung neuer Issues geholfen, sodass Probleme in meinen Bereichen bereits im Review oder in den automatisierten Tests gefunden wurden statt erst im QA.",
]


CERT_NVIDIA = "NVIDIA: Building LLM Applications With Prompt Engineering, issued November 2025."
CERT_AWS = "AWS Academy Graduate: AWS Academy Cloud Foundations, issued July 2025."
CERT_SAS = "SAS Certified Specialist: Visual Business Analytics Using SAS Viya, issued May 2025."
CERT_GOOGLE = "Google Data Analytics: Foundations, Data, Data, Everywhere, issued April 2025 on Coursera."

CERT_NVIDIA_DE = "NVIDIA: Building LLM Applications With Prompt Engineering, ausgestellt im November 2025."
CERT_AWS_DE = "AWS Academy Graduate: AWS Academy Cloud Foundations, ausgestellt im Juli 2025."
CERT_SAS_DE = "SAS Certified Specialist: Visual Business Analytics Using SAS Viya, ausgestellt im Mai 2025."
CERT_GOOGLE_DE = "Google Data Analytics: Foundations, Data, Data, Everywhere, ausgestellt im April 2025 auf Coursera."

# ---- Achievement ----
ACH_USAII_EN = "USAII Global AI Hackathon 2026: Finalist at Graduate Level, awarded by the United States Artificial Intelligence Institute for innovation, technical creativity, and applied AI on real world challenges."
ACH_USAII_DE = "USAII Global AI Hackathon 2026: Finalist auf Graduate Level, ausgezeichnet vom United States Artificial Intelligence Institute für Innovation, technische Kreativität und angewandte KI an realen Herausforderungen."


# ---- Project bank ----
P_RAG_EN = {
    "title": "Multi Agent RAG with LLM as Judge and Multilingual EN and DE Support",
    "stack": ["Python", "LangGraph multi agent", "Ollama with Mistral 7B and Qwen2.5 14B", "Pinecone", "paraphrase multilingual MiniLM L12 v2", "spaCy", "BM25"],
    "bullets": [
        "For an English only hybrid BM25 plus dense RAG policy analysis system over a 14 document policy corpus that could not serve German speakers, tasked with adding multilingual support without duplicating the corpus, migrated embeddings and retrieval to a paraphrase multilingual MiniLM L12 v2 shared vector space so a German query retrieves English sources and is answered in German end to end.",
        "With every agent in the graph re running language detection and producing inconsistent output languages, tasked with a single source of truth, built a LanguageAgent that centralises seeded language detection with a confidence floor, propagates the output language directive to every downstream agent, and routes preprocessing to language matched spaCy pipelines with a blank multilingual fallback and per chunk language recording so retrieval and evaluation can slice by language.",
        "To measure answer quality without hand grading, implemented an LLM as Judge JudgeAgent scoring answers 1 to 5 on 5 dimensions, groundedness, relevance, completeness, citation quality and language quality, in JSON mode at temperature 0, and eliminated self preference bias by running the judge on a different local model Qwen2.5 14B from the generator Mistral 7B with a self_judged flag propagated into every report and a hard failure on missing judge model so a silent fallback to self judging cannot regress unnoticed.",
        "Built an EvalAgent computing 5 retrieval metrics, hit@k, precision@k, recall@k, MRR and nDCG@k, alongside 4 generation metrics, answer relevancy, context utilisation, citation density and language match rate, aggregated overall and per language into JSON and Markdown reports on a paired EN and DE labelled eval set, then ported the evaluator from the HuggingFace API to Ollama so retrieval, generation, judging and evaluation all run locally with Pinecone as the only remaining external service.",
    ],
}

P_CREDITIQ_EN = {
    "title": "CreditIQ: Fairness by Design Credit Scoring",
    "stack": ["Python", "scikit learn", "AIF360", "SHAP", "Streamlit"],
    "bullets": [
        "For an SRH Heidelberg project on regulated credit scoring where a baseline model was failing the EU AI Act and AGG 80 percent fairness bar, tasked with getting it back into compliance without gutting predictive quality, applied AIF360 mitigation and threshold calibration on a real credit dataset, which raised the Disparate Impact ratio from a failing 0.79 to a compliant 0.88.",
        "After single axis age bias was fixed but younger women were still being penalised, tasked with finding and correcting the hidden intersectional bias, used SHAP driven subgroup analysis to expose the pattern and designed a four way age by gender threshold matrix, which corrected it without over correcting into reverse discrimination.",
        "With a large false negative rate silently rejecting good applicants, tasked with cutting it while keeping overall accuracy defensible, documented the fairness accuracy trade off as a deliberate and regulator defensible decision, which brought the false negative rate down from 44 percent to 16.7 percent while accuracy held at 75 percent on the held out test split.",
        "Because a compliant model that only lives in a notebook is not decision support, tasked with delivering it to a finance manager, shipped a Streamlit decision support tool that gives a recommendation plus a plain language LLM generated explanation, backed the pipeline with unit tests at 100 percent branch coverage and a full regulatory write up, and cleared GDPR Article 22 and EU AI Act Article 14 human in the loop requirements.",
    ],
}

P_FLIGHT_EN = {
    "title": "Real Time Flight Tracking Data Pipeline",
    "stack": ["Python", "PySpark", "BigQuery", "dbt", "Apache Airflow", "GCP Dataproc and GCS", "Tableau with TabPy"],
    "bullets": [
        "For a Data Engineering module at SRH Heidelberg needing a real time joined view over live aircraft above Germany, tasked with the collection and enrichment layer, built Python collectors that poll the OpenSky Network API every 30 seconds and PySpark cleaning on Google Cloud that joins against airport, aircraft, and weather data across four sources, producing a clean joined table covering more than 128 thousand records.",
        "With raw collector output not being usable for analysis and each aircraft needing a nearest airport label, tasked with the modelling layer, shaped the data into analysis ready tables with dbt and computed each aircraft's nearest airport with PySpark for heavy lift, which produced consistent nearest airport labels across the historical dataset.",
        "Because manual reruns would kill the real time promise, tasked with automating refresh, orchestrated the whole system with Apache Airflow on GCS backed storage and Dataproc compute so that batch and real time layers refresh automatically every 15 minutes without operator intervention.",
        "With the pipeline sitting on data but no insight, tasked with the analytics surface, built a Tableau workbook backed by Python statistics through TabPy on the dbt aggregates as the feed, which surfaced the finding that air traffic drops 4.4 times in heavy rain and clusters around hubs like Frankfurt and Munich.",
    ],
}

P_MOVIE_EN = {
    "title": "Movie Analytics and ML Pipeline on GCP",
    "stack": ["GCP BigQuery", "Cloud Run", "GCS", "Cloud Scheduler", "BigQuery ML", "Python", "SQL", "Looker Studio"],
    "bullets": [
        "For a personal cloud data project on movie analytics that needed to run unattended on GCP, tasked with the ingestion and processing layer, built an end to end batch pipeline that pulls movie data from a public API into a GCS data lake and processes it through a 3 tier Bronze Silver Gold medallion architecture in BigQuery on Cloud Run, running on a fully automated Cloud Scheduler trigger with 0 manual interventions required.",
        "With raw ingested data being unfit for direct analytics, tasked with hardening the Silver layer, applied schema enforcement, safe type casting, deduplication via window functions and genre normalisation into a relational model, which held clean referential integrity across every downstream Gold table.",
        "Because a classifier trained on post release signals would leak the answer, tasked with a leakage free hit prediction, trained a BigQuery ML classifier that predicts whether a film will be a hit before release, deliberately splitting features into 2 tables so only pre release signals feed the model, and confirmed leakage free evaluation on the split.",
        "With business stakeholders needing concrete answers rather than raw tables, tasked with the analytics surface, built Gold layer aggregates and a 5 page Looker Studio dashboard answering questions on genre ROI, foreign language growth and release season timing plus an ML early warning view, and secured the system with a least privilege service account and Secret Manager.",
    ],
}

P_TABLEAU_EN = {
    "title": "Fast Food Nutritional Analyzer and Meal Simulator",
    "showcase": "public.tableau.com/shared/YC6Y4ZBM5",
    "stack": ["Tableau with Set Actions", "parameters and calculated fields", "data storytelling and UI or UX"],
    "bullets": [
        "For a Tableau dashboard project where users needed to explore fast food nutrition and simulate a meal rather than just filter charts, tasked with the interaction layer, built a dynamic shopping cart using Tableau Set Actions so end users can select scatter plot points and instantly total the 3 key macros calories, fat and protein for a simulated meal.",
        "With 1 static Y axis being unable to serve both a muscle gain and a weight loss goal, tasked with letting the viewer switch objective without reloading, implemented parameter driven analytics with a dynamic Y axis tied to a user controlled goal parameter using a CASE statement, which produced consistent axis switching across 2 objectives without dashboard reloads.",
        "Because deceptive high fat and high calorie items were reading as safe on the raw data, tasked with surfacing them, authored complex order of operation IF and THEN calculated fields for logical grouping and custom flags such as an Is It A Trap flag, which flagged the trap items correctly on manual spot checks against the source nutrition data.",
        "For a non technical stakeholder who needed both the big picture and the deep dive, tasked with the layout, designed a 2 tier view combining an executive macro view and a granular food finder in a colour blind safe dark mode palette, which met the target of reduced time to insight in stakeholder feedback.",
    ],
}

P_CLIMATE_EN = {
    "title": "Economic Impact Analysis of Global Climate Events",
    "stack": ["Python with Pandas and scikit learn", "Random Forest", "statistical modelling", "Matplotlib and Seaborn"],
    "bullets": [
        "For a data science project needing to turn raw global climate event data into decision support for resource allocation and risk assessment, tasked with the full analytics pipeline, executed an end to end project from ingestion to stakeholder report, delivered as a single reproducible pipeline from raw CSV to a management ready output.",
        "With the raw data carrying outliers, missing values, and inconsistent scales that would poison any downstream model, tasked with building a clean foundation, performed advanced data preparation and cleansing over outliers, imputation, and normalisation, which held stable model performance before and after feature scaling.",
        "Because the business question was where economic risk actually concentrates, tasked with the modelling layer, developed Random Forest models to analyse correlations between event duration and financial impact, and read the results through feature importance rankings and residual analysis, which produced clear business relevant insights on the risk concentration.",
        "With the audience being non technical stakeholders rather than data scientists, tasked with the communication layer, produced comprehensive visual reports and calibrated confidence statements, which survived a management review without further translation.",
    ],
}

P_HADOOP_EN = {
    "title": "Hadoop Based Data Crawling and Processing Platform",
    "stack": ["Python with Selenium and BeautifulSoup and Pandas", "Docker Swarm", "Hadoop HDFS", "SQL Server"],
    "bullets": [
        "For a distributed data engineering project on e commerce data at scale, tasked with the cluster layer, orchestrated a distributed Hadoop cluster with one Name Node and three Data Nodes on Docker Swarm, which delivered automated container management and self healing on node failure.",
        "Because dynamic paginated e commerce pages were fragile to scrape and each network hiccup risked lost data, tasked with the collection layer, built a decoupled web scraping pipeline with Python and Selenium that navigates dynamic paginated results and saves raw HTML locally for data safety, which allowed clean re runs against the saved raw pages.",
        "With sponsored click tracking URLs and missing fields corrupting the extracted product list, tasked with the parsing layer, engineered a robust BeautifulSoup parser that handles missing data and decodes sponsored click tracking URLs into clean product links, which held up against a manual verification set for parser correctness.",
        "Because the platform was only worth the effort if the storage was durable and query ready, tasked with the storage and handoff layer, ingested structured CSVs into HDFS and ran redundancy tests that confirmed consistent block replication counts across the three Data Nodes, then extracted processed data into SQL Server for downstream analysis.",
    ],
}

# ---- German variants for tracks that need them ----
P_MOVIE_DE = {
    "title": "Movie Analytics und ML Pipeline auf GCP",
    "stack": ["GCP BigQuery", "Cloud Run", "GCS", "Cloud Scheduler", "BigQuery ML", "Python", "SQL", "Looker Studio"],
    "bullets": [
        "Für ein persönliches Cloud Data Projekt zu Movie Analytics, das unbeaufsichtigt auf GCP laufen sollte, mit dem Auftrag die Ingestion und Verarbeitungsschicht zu bauen, wurde eine end to end Batch Pipeline aufgesetzt, die Filmdaten aus einer öffentlichen API in einen GCS Data Lake zieht und über eine 3 Tier Bronze Silver Gold Medallion Architektur in BigQuery auf Cloud Run verarbeitet, laufend über einen vollständig automatisierten Cloud Scheduler Trigger mit 0 manuellen Eingriffen.",
        "Da die roh eingelesenen Daten für direkte Analytik ungeeignet waren, mit dem Auftrag die Silver Schicht zu härten, wurden Schema Enforcement, sicheres Type Casting, Deduplikation per Window Functions und Genre Normalisierung in ein relationales Modell angewandt, was in allen nachgelagerten Gold Tabellen saubere referenzielle Integrität lieferte.",
        "Da ein Klassifikator auf Post Release Signalen die Antwort geleakt hätte, mit dem Auftrag eine leakage freie Hit Vorhersage zu liefern, wurde ein BigQuery ML Klassifikator trainiert, der vor Kinostart vorhersagt ob ein Film ein Hit wird, indem Merkmale bewusst in 2 Tabellen aufgeteilt wurden so dass nur Pre Release Signale ins Modell fließen, und die Split Evaluation als leakage frei bestätigt wurde.",
        "Da Business Stakeholder konkrete Antworten statt Rohtabellen brauchten, mit dem Auftrag die Analytics Oberfläche zu bauen, wurden Gold Aggregate und ein 5 seitiges Looker Studio Dashboard erstellt, das Fragen zu Genre ROI, Wachstum fremdsprachiger Filme und Release Saison Timing sowie eine ML Early Warning Sicht beantwortet, und das System mit einem Least Privilege Service Account und Secret Manager abgesichert.",
    ],
}

P_CREDITIQ_DE = {
    "title": "CreditIQ: Fairness by Design Credit Scoring",
    "stack": ["Python", "scikit learn", "AIF360", "SHAP", "Streamlit"],
    "bullets": [
        "Für ein SRH Heidelberg Projekt zu reguliertem Credit Scoring, bei dem ein Baseline Modell die 80 Prozent Fairness Schwelle nach EU AI Act und AGG nicht erfüllte, mit dem Auftrag die Compliance ohne massiven Genauigkeitsverlust wiederherzustellen, wurden AIF360 Mitigation und Schwellenwertkalibrierung auf einen realen Kreditdatensatz angewandt, was den Disparate Impact Wert von einem durchgefallenen 0,79 auf einen konformen 0,88 hob.",
        "Nach Korrektur der einachsigen Altersverzerrung wurden jüngere Frauen weiterhin benachteiligt, mit dem Auftrag die versteckte intersektionale Verzerrung zu finden und zu beheben, wurde eine SHAP getriebene Subgruppenanalyse durchgeführt und eine vierfeldrige Alter und Geschlecht Schwellenwertmatrix entworfen, was die Verzerrung korrigierte ohne in umgekehrte Diskriminierung zu kippen.",
        "Bei einer großen False Negative Rate, die stumm gute Bewerber ablehnte, mit dem Auftrag diese zu senken bei belastbarer Gesamtgenauigkeit, wurde der Fairness Accuracy Trade off als bewusste und regulatorisch belastbare Entscheidung dokumentiert, was die False Negative Rate von 44 Prozent auf 16,7 Prozent senkte, während die Genauigkeit am Held Out Test Split bei 75 Prozent blieb.",
        "Da ein konformes Modell im Notebook noch keine Entscheidungsunterstützung ist, mit dem Auftrag es an eine Finanzverantwortliche zu liefern, wurde ein Streamlit Entscheidungsunterstützungs Tool ausgeliefert, das eine Empfehlung plus eine in einfacher Sprache generierte LLM Erklärung gibt, die Pipeline durch Unit Tests mit 100 Prozent Branch Coverage und eine vollständige regulatorische Dokumentation abgestützt, und die Human in the Loop Anforderungen aus GDPR Artikel 22 und EU AI Act Artikel 14 erfüllt.",
    ],
}

P_FLIGHT_DE = {
    "title": "Echtzeit Flugverfolgungs Pipeline",
    "stack": ["Python", "PySpark", "BigQuery", "dbt", "Apache Airflow", "GCP Dataproc und GCS", "Tableau mit TabPy"],
    "bullets": [
        "Für ein Data Engineering Modul an der SRH Heidelberg, das eine Echtzeitsicht auf Live Flugzeuge über Deutschland benötigte, mit dem Auftrag die Sammel und Anreicherungsschicht zu bauen, wurden Python Collectors aufgesetzt, die die OpenSky Network API alle 30 Sekunden abfragen, sowie PySpark Cleaning auf Google Cloud, das gegen Flughafen, Flugzeug und Wetterdaten aus vier Quellen joint, was eine saubere Join Tabelle mit über 128 tausend Datensätzen ergab.",
        "Da Rohdaten der Collectors nicht direkt analysierbar waren und jedes Flugzeug ein nächstgelegenes Flughafen Label brauchte, mit dem Auftrag die Modellierungsschicht zu bauen, wurden die Daten mit dbt in analysebereite Tabellen geformt und der nächstgelegene Flughafen mit PySpark berechnet, was konsistente Labels über den gesamten historischen Zeitraum lieferte.",
        "Da manuelle Reruns das Echtzeit Versprechen brechen würden, mit dem Auftrag die Aktualisierung zu automatisieren, wurde das Gesamtsystem mit Apache Airflow auf GCS Speicher und Dataproc Compute so orchestriert, dass sich Batch und Echtzeit Schichten alle 15 Minuten unbeaufsichtigt aktualisieren.",
        "Da die Pipeline auf Daten saß aber noch keine Erkenntnis lieferte, mit dem Auftrag die Analytics Oberfläche zu bauen, wurde ein Tableau Workbook mit Python Statistik über TabPy auf den dbt Aggregaten als Feed gebaut, was die Erkenntnis brachte, dass der Luftverkehr bei starkem Regen um Faktor 4,4 einbricht und sich um Drehkreuze wie Frankfurt und München bündelt.",
    ],
}

P_TABLEAU_DE = {
    "title": "Fast Food Nährwert Analyzer und Meal Simulator",
    "showcase": "public.tableau.com/shared/YC6Y4ZBM5",
    "stack": ["Tableau mit Set Actions", "Parameter und Calculated Fields", "Data Storytelling und UI oder UX"],
    "bullets": [
        "Für ein Tableau Dashboard Projekt, in dem Nutzer Fast Food Nährwerte erkunden und ein Menü simulieren sollten statt nur Charts zu filtern, mit dem Auftrag die Interaktionsschicht zu bauen, wurde ein dynamischer Warenkorb mit Tableau Set Actions umgesetzt, so dass Endnutzer Punkte im Scatter Plot auswählen und sofort die 3 zentralen Makros Kalorien, Fett und Eiweiß eines simulierten Menüs summiert bekommen.",
        "Da 1 statische Y Achse weder Muskelaufbau noch Gewichtsverlust gleichzeitig unterstützen konnte, mit dem Auftrag dem Betrachter das Umschalten ohne Reload zu ermöglichen, wurde parameter gesteuerte Analytik mit einer dynamischen Y Achse an einen Zielparameter gekoppelt und per CASE Statement umgesetzt, was konsistenten Achsenwechsel über 2 Ziele ohne Dashboard Reload ergab.",
        "Da trügerisch fett und kalorienreiche Produkte in den Rohdaten harmlos wirkten, mit dem Auftrag sie sichtbar zu machen, wurden komplexe IF THEN Calculated Fields für logische Gruppierung und eigene Flags wie ein Is It A Trap Flag formuliert, die die kritischen Produkte in manuellen Stichproben gegen die Nährwertquelle korrekt markierten.",
        "Für eine nicht technische Stakeholderin, die sowohl das große Bild als auch den Deep Dive brauchte, mit dem Auftrag das Layout zu entwerfen, wurde eine 2 stufige Sicht aus Executive Makro Sicht und granularer Food Finder Sicht in einer farbenblind sicheren Dark Mode Palette gestaltet, die im Stakeholder Feedback das Ziel geringerer Time to Insight erfüllte.",
    ],
}

P_CLIMATE_DE = {
    "title": "Wirtschaftliche Analyse globaler Klimaereignisse",
    "stack": ["Python mit Pandas und scikit learn", "Random Forest", "statistische Modellierung", "Matplotlib und Seaborn"],
    "bullets": [
        "Für ein Data Science Projekt, das rohe globale Klimaereignis Daten in Entscheidungsunterstützung für Ressourcenallokation und Risikobewertung überführen sollte, mit dem Auftrag die gesamte Analyse Pipeline zu bauen, wurde ein end to end Projekt von der Ingestion bis zum Stakeholder Report umgesetzt, geliefert als reproduzierbare Pipeline von der Roh CSV bis zur management fähigen Ausgabe.",
        "Da die Rohdaten Ausreißer, fehlende Werte und inkonsistente Skalen enthielten, die jedes nachgelagerte Modell vergiften würden, mit dem Auftrag eine saubere Datenbasis zu schaffen, wurde fortgeschrittene Datenaufbereitung über Ausreißer, Imputation und Normalisierung durchgeführt, was stabile Modellleistung vor und nach dem Feature Scaling ergab.",
        "Da die Geschäftsfrage lautete, wo sich wirtschaftliches Risiko tatsächlich konzentriert, mit dem Auftrag die Modellierungsschicht zu bauen, wurden Random Forest Modelle zur Analyse des Zusammenhangs zwischen Ereignisdauer und finanzieller Wirkung entwickelt und über Feature Importance Rankings und Residuenanalyse gelesen, was klare, für das Geschäft relevante Aussagen zur Risikokonzentration lieferte.",
        "Da die Zielgruppe nicht technische Stakeholder statt Data Scientists waren, mit dem Auftrag die Kommunikationsebene zu liefern, wurden vollständige visuelle Reports und kalibrierte Konfidenzaussagen erstellt, die einer Management Review ohne weitere Übersetzung standhielten.",
    ],
}

P_RAG_DE = {
    "title": "Multi Agent RAG mit LLM as Judge und mehrsprachiger EN und DE Unterstützung",
    "stack": ["Python", "LangGraph Multi Agent", "Ollama mit Mistral 7B und Qwen2.5 14B", "Pinecone", "paraphrase multilingual MiniLM L12 v2", "spaCy", "BM25"],
    "bullets": [
        "Für ein rein englisches Hybrid RAG Policy Analysesystem mit BM25 und dichter Vektorsuche über einen 14 Dokumente Policy Korpus, das deutschsprachige Nutzer nicht bedienen konnte, mit dem Auftrag mehrsprachige Unterstützung ohne Korpus Duplizierung hinzuzufügen, wurden Embeddings und Retrieval auf einen paraphrase multilingual MiniLM L12 v2 gemeinsamen Vektorraum migriert, sodass eine deutsche Anfrage englische Quellen abruft und end to end auf Deutsch beantwortet wird.",
        "Da jeder Agent im Graph erneut Spracherkennung ausführte und inkonsistente Ausgabesprachen produzierte, mit dem Auftrag eine zentrale Wahrheitsquelle zu schaffen, wurde ein LanguageAgent gebaut, der geseedete Spracherkennung mit einem Confidence Floor zentralisiert, die Ausgabesprache Direktive an jeden nachgelagerten Agent weiterreicht und Preprocessing an sprachpassende spaCy Pipelines mit einem leeren Multilingual Fallback routet und die Sprache pro Chunk protokolliert, sodass Retrieval und Evaluation nach Sprache geschnitten werden können.",
        "Um Antwortqualität ohne manuelle Bewertung zu messen, wurde ein LLM as Judge JudgeAgent implementiert, der Antworten mit 1 bis 5 auf 5 Dimensionen bewertet, Groundedness, Relevance, Completeness, Citation Quality und Language Quality, im JSON Modus bei Temperatur 0, und Self Preference Bias wurde eliminiert, indem der Judge auf einem anderen lokalen Modell Qwen2.5 14B lief als der Generator Mistral 7B, mit einem self_judged Flag in jedem Report und einer harten Fehlerbehandlung bei fehlendem Judge Modell, damit ein stiller Rückfall auf Self Judging nicht unbemerkt regressieren kann.",
        "Es wurde ein EvalAgent gebaut, der 5 Retrieval Metriken, hit@k, precision@k, recall@k, MRR und nDCG@k, neben 4 Generation Metriken, Answer Relevancy, Context Utilisation, Citation Density und Language Match Rate, berechnet, aggregiert insgesamt und pro Sprache in JSON und Markdown Reports auf einem gepaarten EN und DE Evaluations Set, dann wurde die Evaluation von der HuggingFace API auf Ollama portiert, sodass Retrieval, Generation, Judging und Evaluation vollständig lokal laufen mit Pinecone als einzigem verbleibenden externen Service.",
    ],
}


# ---- CONFIGS: one per role in the top cut for the 16 July 2026 run ----
CONFIGS_16JUL = [
    # 1. Porsche — Werkstudent Data Science & Process Mining Zuffenhausen (German track)
    {
        "folder": "Porsche Werkstudent DS Process Mining",
        "company": "Porsche",
        "lang": "de",
        "role_strip": "Data Science und Process Mining Werkstudent",
        "cl_date": "16. Juli 2026",
        "cl_subject": "Werkstudent Data Science und Process Mining in Zuffenhausen",
        "profile": "Master Student der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung in Data Analytics, Machine Learning und Process Mining nahen Pipelines. Ich habe eine automatisierte BigQuery Medallion Pipeline mit BigQuery ML Klassifikator und Looker Studio Reporting geliefert, eine PySpark und dbt gestützte Echtzeit Pipeline für über 128 tausend Flugpositionen auf Google Cloud betrieben und ein Fairness by Design Credit Scoring System nach EU AI Act umgesetzt. Sicher in Python, SQL, PyTorch und scikit learn, bin ich die richtige Verstärkung für Data Science und Process Analytics Aufgaben in Produktions und Logistikprozessen.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_MOVIE_DE, P_FLIGHT_DE, P_CREDITIQ_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_SAS_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich als Werkstudent Data Science und Process Mining am Standort Zuffenhausen. Ihre Ausschreibung, die Mitwirkung an Artificial Intelligence und Data und Process Analytics, die Anwendung fortgeschrittener Data Science Methoden auf Realdaten aus Produktions und Logistikprozessen sowie die Mithilfe bei der Implementierung neuronaler Netze und Machine Learning Verfahren, deckt sich sehr genau mit dem, was ich in den letzten Monaten in der Praxis geliefert habe.",
            "In meiner Movie Analytics und ML Pipeline auf GCP habe ich eine vollständig automatisierte Bronze Silver Gold Medallion Architektur in BigQuery gebaut, mit schemakonformer Datenaufbereitung, Deduplikation per Window Functions und einem BigQuery ML Klassifikator, der bewusst leakage frei nur Pre Release Signale nutzt. Ergänzt wird das durch ein fünfseitiges Looker Studio Dashboard für konkrete Business Fragen. Diese Architektur überträgt sich direkt auf Analytics Anwendungen im Produktions und Supply Chain Umfeld.",
            "In meiner Echtzeit Flugverfolgungs Pipeline habe ich mit PySpark auf Google Cloud rohe Daten sauber verarbeitet, mit dbt in analysebereite Tabellen überführt und mit Apache Airflow so orchestriert, dass sich Batch und Echtzeit Schichten alle 15 Minuten automatisch aktualisieren. Bei eRay GmbH habe ich eine rekursive Zeitreihen Pipeline für vier Wasserqualitätsindikatoren mit sechs Modellen im Vergleich und CatBoost Multi Quantil Regression umgesetzt, mit strengen anti leakage Regeln, das schult den Blick für belastbare Data Science auf Realdaten.",
            "Zur Sprachanforderung: mein aktuelles Deutschniveau ist B1 in Bearbeitung, ich lerne aktiv weiter. Ich arbeite sicher in Python, R nah durch scikit learn und PyTorch, SQL und Cloud Umgebungen und bringe das NVIDIA Building LLM Applications With Prompt Engineering sowie das AWS Academy Cloud Foundations Zertifikat mit. Sehr gerne bespreche ich meine Passung in einem persönlichen Gespräch.",
        ],
    },

    # 2. Dico Drinks — Werkstudent IT Datenvisualisierung Hückelhoven (English track, posting in German but no German level stated)
    {
        "folder": "Dico Drinks Werkstudent IT Datenvisualisierung",
        "company": "DICO Drinks GmbH",
        "lang": "en",
        "role_strip": "IT Datenvisualisierung Werkstudent",
        "cl_date": "16 July 2026",
        "cl_subject": "Working Student, IT Datenvisualisierung and Produktionsdaten",
        "profile": "Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, with hands on dashboarding, data visualisation, and production data work. I have shipped an interactive Tableau dashboard with dynamic Set Actions and parameter driven analytics, a fully automated BigQuery medallion pipeline feeding a five page Looker Studio dashboard, and a real time flight tracking pipeline processing over 128 thousand records on Google Cloud. Comfortable in Python, SQL, dashboarding tools, and structured data preparation, I am the right fit for building and maintaining production and machine data dashboards on your central data platform.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_TABLEAU_EN, P_MOVIE_EN, P_FLIGHT_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_SAS, CERT_GOOGLE, CERT_AWS],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am applying for the Werkstudent IT Datenvisualisierung and Produktionsdaten role at DICO in Hückelhoven. The brief on building and maintaining dashboards for production and machine data, translating business defined KPIs into charts, tables, and views for various departments, and iterating with IT, Production, and Maintenance on display and usability is exactly the kind of work I have been shipping over the past year.",
            "In my Fast Food Nutritional Analyzer and Meal Simulator I built a two tier Tableau dashboard combining an executive macro view with a granular food finder, using Set Actions, parameter driven Y axes, and complex calculated fields to let non technical users interact directly with the data, and I used a colour blind safe dark mode palette to reduce time to insight. That is directly the kind of clear, structured visualisation work you describe.",
            "In my Movie Analytics and ML Pipeline on GCP I engineered an end to end Bronze to Silver to Gold BigQuery medallion architecture with schema enforcement, deduplication via window functions, and a leakage free BigQuery ML classifier, and delivered a five page Looker Studio dashboard answering concrete business questions. In my Real Time Flight Tracking Data Pipeline I ran a PySpark and dbt pipeline on Google Cloud with Apache Airflow refreshing every 15 minutes, that is a strong parallel to your central data platform aggregating productivity and machine data.",
            "I am comfortable in Python and SQL, hold the SAS Certified Specialist Visual Business Analytics Using SAS Viya certificate and the Google Data Analytics Foundations certificate, and my current German level is B1 in progress. I would be glad to support your IT and Digitalisation team on dashboarding and documentation from the first week.",
        ],
    },

    # 3. Animore — Working Student / Intern Post-Training for Robot Learning München (English)
    {
        "folder": "Animore Working Student Robot Learning",
        "company": "Animore",
        "lang": "en",
        "role_strip": "Machine Learning Working Student",
        "cl_date": "16 July 2026",
        "cl_subject": "Working Student and Intern, Post Training for Robot Learning",
        "profile": "Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, with hands on machine learning work spanning LLM based systems, rigorous model evaluation, and real time data pipelines. I have shipped a modular Retrieval Augmented Generation system with a custom decision making router on Llama 3.1 8b via Groq and LangChain, a fairness by design classification system validated to EU AI Act thresholds, and a recursive time series pipeline at eRay GmbH built on CatBoost multi quantile regression with strict anti leakage guarantees. Comfortable in Python, numpy, pandas, PyTorch style workflows, and Linux, I am the right fit for post training and evaluating robot foundation models.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_RAG_EN, P_CREDITIQ_EN, P_FLIGHT_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_NVIDIA, CERT_AWS, CERT_GOOGLE],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am applying for the Working Student and Intern role in Post Training for Robot Learning at Animore in Munich. The brief on helping fine tune large foundation models, reading recent papers and implementing them in code, running post training experiments, and contributing to evaluation and benchmarking harnesses is exactly the shape of work I want to be doing.",
            "My Hybrid RAG Orchestrator is a working generative AI system with a custom decision making router over Llama 3.1 8b via Groq, LangChain orchestration, a ChromaDB vector store with local persistence, and a stateful MemoryAgent inside the inference pipeline. Building it taught me the practical side of foundation model integration, prompt engineering, embeddings, and iterative debugging of an LLM system. In CreditIQ I built rigorous evaluation and benchmarking harnesses, computing per subgroup metrics, cutting the false negative rate from 44 to 16.7 percent while holding accuracy at 75 percent, and backing everything with unit tests at 100 percent branch coverage. That is the same benchmarking mindset you want on post training runs.",
            "At eRay GmbH I built a recursive time series pipeline forecasting four water quality indicators for a German lake, benchmarking six models head to head and enforcing strict anti leakage rules across the pipeline. In my Real Time Flight Tracking Data Pipeline I processed over 128 thousand records with PySpark on Google Cloud, enriching flight positions against four data sources every 30 seconds. Together they show I am comfortable digging into messy data, automating recurring runs, and iterating on tooling that makes training jobs easier to start, configure, and debug.",
            "I am proficient in Python and comfortable in Linux, familiar with PyTorch style workflows, and hold the NVIDIA Building LLM Applications With Prompt Engineering certificate. I would be glad to start with the three month internship phase and continue as a working student, staying at least a year in total as the role calls for.",
        ],
    },

    # 4. Fraunhofer SIT — Werkstudierende NLP Darmstadt (English track, German posting but no German level stated)
    {
        "folder": "Fraunhofer SIT Werkstudent NLP",
        "company": "Fraunhofer SIT",
        "lang": "en",
        "role_strip": "NLP and Machine Learning Werkstudent",
        "cl_date": "16 July 2026",
        "cl_subject": "Werkstudierende in the NLP research area at Fraunhofer SIT",
        "profile": "Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, with hands on Natural Language Processing and machine learning work built around LLMs, embeddings, and rigorous evaluation. I have shipped a modular Retrieval Augmented Generation system with a custom decision making router on Llama 3.1 8b via Groq and LangChain with HuggingFace MiniLM L6 v2 embeddings, a fairness by design classification pipeline validated to EU AI Act thresholds, and a recursive time series pipeline at eRay GmbH with strict anti leakage rules. Comfortable in Python, PyTorch style workflows, Transformer architectures, and web interface development with Streamlit, I am the right fit for supporting your NLP research on authorship, style change detection, and AI generated text.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_RAG_EN, P_CREDITIQ_EN, P_MOVIE_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_NVIDIA, CERT_AWS, CERT_GOOGLE],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am applying for the Werkstudierende role in the NLP research area at Fraunhofer SIT in Darmstadt, reference 81228. The brief on implementing NLP approaches around feature extraction, style change detection, AI generated text detection, and authorship attribution, plus applying machine learning methods spanning zero and few shot learning, fine tuning of foundation models, Transformer architectures, CNNs, and classical baselines, is exactly the shape of NLP work I have been building this year.",
            "My Hybrid RAG Orchestrator is a working NLP system with a custom decision making router over Llama 3.1 8b via Groq and LangChain, a ChromaDB vector store with local persistence, and HuggingFace MiniLM L6 v2 embeddings for semantic retrieval. Building it exercised the LLM based feature extraction, embedding, and prompt engineering side of the role and taught me the practical side of Transformer inference in a production style pipeline. The Streamlit interface on top gave me hands on experience shipping user facing NLP tools, in line with your interest in Streamlit, Gradio, and similar web UIs.",
            "In CreditIQ I ran rigorous machine learning evaluation across classifiers, using SHAP for driven subgroup analysis and computing standard metrics including ROC AUC and confusion matrices. In my Diabetes Prediction Bachelor Thesis I compared six classifiers on a clinical dataset with 10 fold cross validation and chose ROC AUC as the honest headline metric for an imbalanced target. That evaluation discipline transfers directly to the authorship attribution and verification benchmarks in your work.",
            "I am proficient in Python, comfortable with Transformer style architectures, CNNs, and classical baselines, and hold the NVIDIA Building LLM Applications With Prompt Engineering certificate. I would be glad to work 40 to 80 hours per month around my studies and to discuss how the role could extend into a Master Thesis at Fraunhofer SIT.",
        ],
    },

    # 5. REHAU New Ventures — Working Student AI & Innovation Hamburg / Remote (English)
    {
        "folder": "REHAU New Ventures Working Student AI Innovation",
        "company": "REHAU New Ventures",
        "lang": "en",
        "role_strip": "AI and Innovation Working Student",
        "cl_date": "16 July 2026",
        "cl_subject": "Working Student, AI and Innovation at REHAU New Ventures",
        "profile": "Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, with hands on AI enablement and applied machine learning work across LLM applications, business analytics, and full stack data pipelines. I have shipped a modular Retrieval Augmented Generation system with a custom decision making router on Llama 3.1 8b via Groq, a fairness by design credit scoring system covering EU AI Act and GDPR with a business facing decision support UI, and a Random Forest driven study translating raw global event data into structured business insight. Comfortable in Python, SQL, LLM tooling, and clear business communication, I am the right fit for supporting startup scouting, AI enablement, and use case identification at REHAU New Ventures.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_RAG_EN, P_CREDITIQ_EN, P_CLIMATE_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_NVIDIA, CERT_GOOGLE, CERT_AWS],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am applying for the Working Student AI and Innovation role at REHAU New Ventures. The brief on venture clienting, AI enablement across business units, evaluating current AI technologies and choosing between existing tools, custom prompting, and external solutions, and translating requirements into use cases matches the way I already think and work with AI.",
            "My Hybrid RAG Orchestrator is a working AI system with a custom decision making router that dispatches user intent across local knowledge retrieval, external web search, or direct conversational logic. Building it end to end taught me exactly the trade off you describe, when to reach for an existing tool, when custom prompting is enough, and when a bespoke component is worth it. In CreditIQ I designed a business facing decision support tool with a plain language LLM generated explanation next to every recommendation, mapping directly to your interest in cross functional business cases and translating AI capability into actionable use cases.",
            "In my Economic Impact Analysis of Global Climate Events I ran Random Forest models on raw event data to translate duration and severity into clear business relevant risk signals for resource allocation, and communicated the results in reports that non technical stakeholders could act on. At eRay GmbH I delivered a recursive time series pipeline with anti leakage rules and honest reporting of what the data does and does not support, that mindset transfers directly to scouting, use case screening, and honest business case development.",
            "I have been actively using ChatGPT and similar LLM tools for more than two years, I am fluent in English, my current German level is B1 in progress, and I hold the NVIDIA Building LLM Applications With Prompt Engineering certificate. I would be glad to start soon on a 12 month contract, remote from Mannheim with regular Hamburg on site days as fits your team.",
        ],
    },
]


from role_configs_22jul import CONFIGS_22JUL
CONFIGS = CONFIGS_22JUL


# ---- Previous run archive: 15 July 2026 top 10 (kept for auditability) ----
CONFIGS_15JUL = [
    # 1. Volkswagen — Master Thesis Deep Learning autonomous driving
    {
        "folder": "Volkswagen Master Thesis Autonomous Driving",
        "company": "Volkswagen",
        "lang": "en",
        "role_strip": "Master Thesis Student",
        "cl_date": "15 July 2026",
        "cl_subject": "Master Thesis, Deep Learning for Autonomous Driving",
        "profile": "Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, with hands on deep learning and generative AI work on real production data. I have shipped a Retrieval Augmented Generation system with agentic routing on Llama 3.1 8b via Groq, a fairness by design credit scoring system covering EU AI Act and GDPR, and a recursive time series forecasting pipeline at eRay GmbH built on CatBoost multi quantile regression with anti leakage guarantees. Comfortable in Python, PyTorch style workflows, and scientific evaluation, I am the right fit for a Master Thesis on generating anomalous traffic scenarios and evaluating generated data for autonomous driving.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_RAG_EN, P_CREDITIQ_EN, P_MOVIE_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_NVIDIA, CERT_AWS, CERT_GOOGLE],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am applying for the Master Thesis on Deep Learning for autonomous driving with Volkswagen Group Innovation in Wolfsburg. The brief on generating traffic scenarios with anomalies or adverse conditions, evaluating data driven deep learning methods for scenario generation, and assessing the quality of generated data against defined criteria maps directly to the work I have been shipping over the past year.",
            "At eRay GmbH I built an end to end recursive time series pipeline forecasting four water quality indicators for a German lake over a six month collaboration with SRH University. I benchmarked six models head to head, used CatBoost multi quantile regression for asymmetric 80 percent prediction intervals, and enforced strict anti leakage rules across the pipeline. The same discipline of scientific evaluation, anti leakage design, and honest reporting of model limits transfers directly to evaluating generated deep learning scenarios for autonomous driving.",
            "My Hybrid RAG Orchestrator is a working generative AI system with a custom decision making router over Llama 3.1 8b via Groq and LangChain, plus a stateful MemoryAgent that keeps multi turn context intact. Alongside CreditIQ, where I lifted the Disparate Impact ratio from 0.79 to 0.88 and cut the false negative rate from 44 to 16.7 percent with a documented EU AI Act write up, this shows I can design, train, and rigorously evaluate deep learning systems under real world constraints.",
            "I am proficient in Python, familiar with PyTorch and generative AI workflows, and hold the NVIDIA Building LLM Applications With Prompt Engineering certificate. I would be glad to shape the thesis with my professor at SRH Heidelberg and start on the schedule that fits your team.",
        ],
    },

    # 2. Bausch + Lomb — Werkstudent BI Berlin (German track)
    {
        "folder": "Bausch Lomb BI Werkstudent",
        "company": "Bausch + Lomb",
        "lang": "de",
        "role_strip": "Business Intelligence Werkstudent",
        "cl_date": "15. Juli 2026",
        "cl_subject": "Werkstudent Business Intelligence in Berlin",
        "profile": "Master Student der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung in Business Intelligence, Dashboarding und Data Storytelling für Fachbereiche. Ich habe ein interaktives Tableau Dashboard mit dynamischer Set Action Steuerung gebaut, eine Random Forest Analyse zur wirtschaftlichen Wirkung globaler Klimaereignisse durchgeführt und eine BigQuery Medallion Pipeline mit fünfseitigem Looker Studio Dashboard geliefert. Sicher in Excel, SQL, Python und Power BI nahen Werkzeugen, bin ich die richtige Verstärkung, um das CRM und Business Intelligence Team im Vertrieb bei Reports, Adhoc Analysen und Dashboards zu unterstützen.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_TABLEAU_DE, P_MOVIE_DE, P_CLIMATE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_SAS_DE, CERT_GOOGLE_DE, CERT_NVIDIA_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich als Werkstudent Business Intelligence in Ihrem Berliner Standort. Die Ausschreibung beschreibt genau die Art Aufgaben, die ich bereits geliefert habe, nämlich Auswertungen kunden und vertriebsbezogener Daten, Weiterentwicklung mobiler CRM Lösungen, Reports und Dashboards für Geschäftsführung, Marketing und Vertrieb sowie Adhoc Analysen für Management und Vertrieb.",
            "In meinem Fast Food Nutritional Analyzer und Meal Simulator habe ich ein zweistufiges Tableau Dashboard aus einer Executive Makro Sicht und einer granularen Detailsicht entwickelt, mit dynamischen Set Actions, calculated fields und einer farbenblind sicheren Dark Mode Palette. In meiner Movie Analytics und ML Pipeline auf GCP habe ich eine vollständige Bronze Silver Gold Medallion Pipeline auf BigQuery gebaut und in einem fünfseitigen Looker Studio Dashboard Fragen zu Genre ROI, Wachstum fremdsprachiger Filme und Release Saison Timing beantwortet, das entspricht der Reporting Kompetenz, die Sie suchen.",
            "In meiner wirtschaftlichen Analyse globaler Klimaereignisse habe ich Random Forest Modelle und statistische Modellierung genutzt, um Ergebnisse verständlich für nicht technische Stakeholder aufzubereiten. Bei eRay GmbH habe ich eine rekursive Zeitreihen Pipeline mit CatBoost Multi Quantil Regression und anti leakage Regeln geliefert, das schult den Blick für saubere Datenaufbereitung, Territory Management und Interpretation im BI Umfeld.",
            "Ich arbeite sicher in Python, SQL und Excel, habe erste Berührungspunkte mit Power BI und KI Tools und bringe das SAS Certified Specialist Visual Business Analytics Zertifikat sowie das Google Data Analytics Foundations Zertifikat mit. Sehr gerne bespreche ich in einem persönlichen Gespräch, wie ich Sie im Team unterstützen kann.",
        ],
    },

    # 3. WERTGARANTIE Group — Werkstudent Data Science Hannover (German track, C1 required)
    {
        "folder": "WERTGARANTIE Werkstudent Data Science",
        "company": "WERTGARANTIE Group",
        "lang": "de",
        "role_strip": "Werkstudent Data Science",
        "cl_date": "15. Juli 2026",
        "cl_subject": "Werkstudent Data Science in Hannover",
        "profile": "Master Student der Data Science and Analytics an der SRH Heidelberg mit praktischer Erfahrung in Machine Learning, Generative AI und Reporting. Ich habe ein Hybrid RAG System auf Llama 3.1 8b, ein faires Credit Scoring nach EU AI Act sowie eine BigQuery ML Pipeline mit Looker Studio Reporting geliefert. Sicher in Python, SQL und cloud getriebenen KI Workflows.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_CREDITIQ_DE, {
            "title": P_MOVIE_DE["title"],
            "stack": P_MOVIE_DE["stack"],
            "bullets": P_MOVIE_DE["bullets"][:3],
        }],
        "research_bullets": DIABETES_BULLETS_DE[:3],
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich als Werkstudent Data Science in der WERTGARANTIE Group in Hannover. Die Ausschreibung, die Entwicklung und Umsetzung von Use Cases im Bereich Machine Learning und Generative AI, die Integration moderner AI Services in bestehende Prozesse sowie der Aufbau von Reporting Lösungen aus Standard Reporting, Adhoc Analysen und deskriptiven Dashboards deckt sich sehr genau mit dem, was ich in den letzten Monaten geliefert habe.",
            "Bei eRay GmbH habe ich eine rekursive Zeitreihen Pipeline für vier Wasserqualitätsindikatoren eines deutschen Sees über sechs Monate hinweg gebaut, mit CatBoost Multi Quantil Regression für asymmetrische 80 Prozent Vorhersageintervalle und strengen anti leakage Regeln. Bei meinem Hybrid RAG Orchestrator habe ich ein modulares Generative AI System mit LangChain und Llama 3.1 8b via Groq umgesetzt, mit einem eigenen Decision Making Router und einem zustandsbehafteten MemoryAgent. Beides zeigt die praktische Erfahrung, die die Rolle voraussetzt.",
            "Meine Movie Analytics und ML Pipeline auf GCP zeigt die Reporting Seite: eine Bronze Silver Gold Medallion Architektur in BigQuery, ein BigQuery ML Klassifikator mit leakage freier Evaluation und ein fünfseitiges Looker Studio Dashboard für konkrete Business Fragen. Die Übertragbarkeit dieser Architektur auf ein Microsoft Azure Umfeld mit Azure AI Foundry und Azure Machine Learning ist gering und lässt sich schnell einarbeiten.",
            "Zur Sprachanforderung: mein aktuelles Deutschniveau ist B1 in Bearbeitung, ich lerne aktiv weiter und würde die Rolle unter dieser Voraussetzung sehr gerne besprechen. Ich arbeite sicher in Python und SQL, kenne AWS Cloud Grundlagen und bringe das NVIDIA Building LLM Applications With Prompt Engineering Zertifikat mit. Sehr gerne stelle ich mich in einem persönlichen Gespräch vor.",
        ],
    },

    # 4. Sopra Steria — Werkstudent Data Engineer / Analyst Hamburg (German track, B2 required)
    {
        "folder": "Sopra Steria Werkstudent Data Engineer Analyst",
        "company": "Sopra Steria",
        "lang": "de",
        "role_strip": "Data Engineer und Analyst Werkstudent",
        "cl_date": "15. Juli 2026",
        "cl_subject": "Werkstudent Data Engineer und Analyst in Hamburg",
        "profile": "Master Student der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau produktionsreifer Datenpipelines. Ich habe eine PySpark und dbt gestützte Echtzeit Pipeline für über 128 tausend Flugpositionen auf Google Cloud betrieben, eine Bronze Silver Gold Medallion Architektur auf BigQuery mit BigQuery ML Klassifikator ausgeliefert und ein modulares Retrieval Augmented Generation System mit LangChain und Llama 3.1 8b via Groq umgesetzt. Sicher in Python und PySpark sowie mit einem Grundverständnis von Databricks nahen Plattformen und Large Language Models, bin ich die richtige Verstärkung für Data Engineering und Data Analysis auf der Palantir Foundry Plattform.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_FLIGHT_DE, P_MOVIE_DE, P_RAG_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_AWS_DE, CERT_NVIDIA_DE, CERT_SAS_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich als Werkstudent Data Engineer und Analyst bei Sopra Steria in Hamburg. Ihre Ausschreibung, die Entwicklung von Data Engineering und Data Analysis Lösungen auf Palantir Foundry, der Bau von Datenpipelines mit PySpark oder Pandas, Dashboarding für Stakeholder und die Entwicklung von Prototypen mit Machine oder Deep Learning und LLMs, deckt sich genau mit dem, was ich in den letzten Monaten in der Praxis geliefert habe.",
            "In meiner Echtzeit Flugverfolgungs Pipeline habe ich alle 30 Sekunden Positionen von der OpenSky Network API gesammelt und mit vier Quellen über Flughafen, Flugzeug und Wetterdaten mit PySpark auf Google Cloud angereichert, dbt für die Modellierungsschicht genutzt und Apache Airflow als Orchestrator geschaltet, so dass sich Batch und Echtzeit Schichten alle 15 Minuten automatisch aktualisieren. Das entspricht der Palantir Foundry Denke, PySpark Bausteine plus geplante Aggregate für die Analyse.",
            "In meiner Movie Analytics und ML Pipeline auf GCP habe ich eine Bronze Silver Gold Medallion Architektur in BigQuery gebaut, mit sauberer Schema Enforcement, Deduplikation und einem BigQuery ML Klassifikator, der bewusst nur Pre Release Signale verwendet. Für Dashboarding habe ich ein fünfseitiges Looker Studio Dashboard geliefert. Für den LLM Teil zeigt mein Hybrid RAG Orchestrator ein arbeitsfähiges LLM Prototyp System mit einem Decision Making Router und persistenter Vector Speicherung.",
            "Zur Sprachanforderung: mein aktuelles Deutschniveau ist B1 in Bearbeitung. Ich arbeite sicher in Python und PySpark, kenne Git und Cloud Umgebungen und bringe die AWS Academy Cloud Foundations sowie das NVIDIA Building LLM Applications With Prompt Engineering Zertifikat mit. Sehr gerne bespreche ich meine Passung in einem persönlichen Gespräch.",
        ],
    },

    # 5. Picnic — Werkstudent Business Analyst Logistic Analytics Düsseldorf
    {
        "folder": "Picnic Werkstudent Business Analyst Logistics",
        "company": "Picnic",
        "lang": "en",
        "role_strip": "Business Analyst Werkstudent",
        "cl_date": "15 July 2026",
        "cl_subject": "Working Student, Business Analyst Logistic Analytics",
        "profile": "Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, with hands on business analytics work on real, messy data. I have delivered an interactive Tableau dashboard with parameter driven and Set Action interactions, a Random Forest driven study on the economic impact of global climate events, and an automated GCP pipeline with a five page Looker Studio dashboard that answers concrete business questions. Comfortable in SQL, Python, and business storytelling, I am the right fit for a data driven Logistics Analyst role in a fast paced fulfilment environment.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_TABLEAU_EN, P_CLIMATE_EN, P_MOVIE_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_GOOGLE, CERT_SAS, CERT_AWS],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am applying for the Business Analyst Working Student role with the Logistic Analytics team at Picnic in Düsseldorf. The brief, analysing real time data from the fulfilment centres, uncovering problems, and building strategic solutions on top of a data driven and analytical approach, matches what I have been shipping over the last year.",
            "In my Fast Food Nutritional Analyzer and Meal Simulator I built a dynamic shopping cart in Tableau backed by Set Actions and calculated fields, letting non technical users instantly total nutrition metrics for simulated meals. In my Economic Impact Analysis of Global Climate Events I ran Random Forest models on raw event data to translate duration and severity into clear business relevant signals for resource allocation and risk assessment, and communicated the results in reports that non technical stakeholders could act on. Both are the shape of work your Logistics Analyst role calls for.",
            "For the pipeline side, my Movie Analytics and ML Pipeline on GCP is a fully automated Bronze to Silver to Gold BigQuery medallion architecture with a leakage free BigQuery ML classifier and a five page Looker Studio dashboard answering concrete business questions. At eRay GmbH I delivered a recursive time series pipeline for four water quality indicators, benchmarked six models head to head, and wrapped the pipeline in an orchestrator with gate checks. That mindset transfers directly to real time logistics signals and warehouse operations.",
            "I am fluent in English, comfortable in SQL and Python, and my current German level is B1 in progress. I would be glad to discuss how I can support the Logistics Analytics team over at least 16 hours per week and how the role could grow from there.",
        ],
    },

    # 6. Infineon — Master Thesis AI Condition Monitoring for Drive Systems (NRW)
    {
        "folder": "Infineon Master Thesis AI Condition Monitoring",
        "company": "Infineon Technologies",
        "lang": "en",
        "role_strip": "Master Thesis Student",
        "cl_date": "15 July 2026",
        "cl_subject": "Master Thesis, AI Based Condition Monitoring for Drive Systems",
        "profile": "Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, with hands on machine learning work spanning time series forecasting, signal quality validation, and real world sensor data. I have shipped a recursive time series pipeline at eRay GmbH forecasting four water quality indicators with anti leakage guarantees, a fairness by design classification system with rigorous evaluation, and a real time Google Cloud pipeline enriching flight positions against airport, aircraft, and weather data. Comfortable in Python, scikit learn, and MATLAB style modelling, I am the right fit for a Master Thesis on AI based condition monitoring for industrial drive systems.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_CREDITIQ_EN, P_FLIGHT_EN, P_CLIMATE_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_NVIDIA, CERT_AWS, CERT_GOOGLE],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am applying for the Master Thesis on AI based condition monitoring for drive systems at Infineon Technologies. The brief covering synthetic data generation, machine learning model development and training, and validation under realistic operating conditions, with a specific use case around DC Link capacitor degradation, aligns closely with the work I have been shipping.",
            "At eRay GmbH I built a recursive time series pipeline forecasting chlorophyll a, turbidity, pH, and dissolved oxygen for a German lake, benchmarking six models head to head and using CatBoost multi quantile regression for asymmetric 80 percent prediction intervals. I enforced strict anti leakage rules, reconstructed missing winter readings with MICE imputation, and wrapped the pipeline in an orchestrator with gate checks. That is exactly the discipline required for reliable condition monitoring signals off drive systems.",
            "In CreditIQ I designed and validated a machine learning pipeline against strict evaluation criteria, cutting the false negative rate from 44 percent to 16.7 percent while holding accuracy at 75 percent and backing everything with unit tests at 100 percent branch coverage. In my Real Time Flight Tracking Data Pipeline I processed more than 128 thousand records with PySpark on Google Cloud and orchestrated the whole system with Apache Airflow, refreshing every 15 minutes. That is a solid foundation for the data preprocessing, feature extraction, and labelling side of the thesis.",
            "I am proficient in Python and scikit learn, comfortable in MATLAB and Simulink at the level required, and hold the NVIDIA Building LLM Applications With Prompt Engineering certificate. I would be glad to shape the thesis with my professor at SRH Heidelberg and align on the drive system context with the Application and AI teams.",
        ],
    },

    # 7. Airbus AI FDIR — Working Student Spacecraft München
    {
        "folder": "Airbus AI Spacecraft FDIR",
        "company": "Airbus Defence and Space",
        "lang": "en",
        "role_strip": "AI Engineer Werkstudent",
        "cl_date": "15 July 2026",
        "cl_subject": "Working Student, Development of AI Models for Spacecraft FDIR",
        "profile": "Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, with hands on AI model development spanning classical machine learning, deep neural network evaluation, and real time signal pipelines. I have shipped a Retrieval Augmented Generation system with agentic routing on Llama 3.1 8b via Groq, a rigorously validated classification pipeline covering EU AI Act and GDPR, and a real time flight tracking data pipeline processing over 128 thousand records on Google Cloud. Comfortable in Python, TensorFlow and PyTorch style workflows, and signal processing thinking, I am the right fit for developing AI models for autonomous FDIR on Airbus spacecraft.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_RAG_EN, P_CREDITIQ_EN, P_FLIGHT_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_NVIDIA, CERT_AWS, CERT_GOOGLE],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am applying for the Working Student position developing AI models for Spacecraft FDIR with the Digital Payload Processors Design Team at Airbus Defence and Space in Taufkirchen. The brief on exploring AI architectures for input driven results, running trade off analysis on key performance indices, and validating AI models to ensure reliability and performance is exactly the shape of work I have been shipping.",
            "At eRay GmbH I built an end to end recursive time series pipeline forecasting four water quality indicators for a German lake, benchmarking six models head to head, running quantile regression for asymmetric 80 percent prediction intervals, and enforcing strict anti leakage rules across the pipeline. In CreditIQ I lifted the Disparate Impact ratio from 0.79 to 0.88 and cut the false negative rate from 44 to 16.7 percent while holding accuracy, backed by unit tests at 100 percent branch coverage. That is directly the trade off analysis and validation discipline autonomous FDIR needs.",
            "My Hybrid RAG Orchestrator is a working AI system with a custom decision making router over Llama 3.1 8b via Groq and LangChain, showing I can design and integrate AI components into a larger inference pipeline. In my Real Time Flight Tracking Data Pipeline I processed over 128 thousand records with PySpark on Google Cloud, enriching flight positions against airport, aircraft, and weather data every 30 seconds, which gives me a working feel for aerospace grade signal fusion.",
            "I am fluent in English, comfortable in Python and neural network modelling frameworks, and hold the NVIDIA Building LLM Applications With Prompt Engineering certificate. I would be glad to start on 1 October 2026 for a minimum of six months at 18 hours per week from the Taufkirchen site.",
        ],
    },

    # 8. Wieland Group — Werkstudent Data Platform & AI Engineering Ulm (English track)
    {
        "folder": "Wieland Werkstudent Data Platform AI Engineering",
        "company": "Wieland Group",
        "lang": "en",
        "role_strip": "Data Platform and AI Engineering Werkstudent",
        "cl_date": "15 July 2026",
        "cl_subject": "Working Student, Data Platform and AI Engineering",
        "profile": "Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, with hands on data platform and AI engineering work across cloud pipelines and LLM applications. I have built a PySpark and dbt driven real time flight tracking pipeline on Google Cloud, an automated BigQuery medallion architecture with a BigQuery ML classifier, and a Retrieval Augmented Generation system with agentic routing on Llama 3.1 8b via Groq. Comfortable in Python, SQL, PySpark, Git, and LLM tooling, and with a working Databricks style mindset, I am the right fit for driving data platform improvements and AI proofs of concept in parallel.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_FLIGHT_EN, P_MOVIE_EN, P_RAG_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_AWS, CERT_NVIDIA, CERT_SAS],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am applying for the Werkstudent Data Platform and AI Engineering role with Wieland Group in Ulm. The brief on exploring new ideas around your Databricks based platform, prototyping improvements pragmatically, and driving AI projects with LLMs from first idea through data preparation to working proofs of concept, matches the way I already work.",
            "In my Real Time Flight Tracking Data Pipeline I set up live collection every 30 seconds, enriched positions against airport, aircraft, and weather sources with PySpark on Google Cloud, shaped the data with dbt, and orchestrated the whole system on Apache Airflow so batch and real time layers refresh every 15 minutes. In my Movie Analytics and ML Pipeline on GCP I built an end to end Bronze to Silver to Gold BigQuery medallion architecture with schema enforcement, deduplication via window functions, and a leakage free BigQuery ML classifier that only sees pre release signals. That is the exact shape of pragmatic platform prototyping you describe.",
            "My Hybrid RAG Orchestrator is a working LLM proof of concept with a custom decision making router over Llama 3.1 8b via Groq and LangChain, plus a stateful MemoryAgent inside the inference pipeline. At eRay GmbH I delivered a recursive time series pipeline with anti leakage rules and quantile regression prediction intervals. Together they show I can go from first idea to shipped LLM or ML prototype quickly and honestly, without fabricating uplift.",
            "I am proficient in Python and SQL, comfortable with PySpark and Git, and hold the AWS Academy Cloud Foundations and NVIDIA Building LLM Applications With Prompt Engineering certificates. I would be glad to start soon and bring my own initiative to your platform.",
        ],
    },

    # 9. mitteldeutsche IT — Werkstudent KI-Entwicklung Leipzig
    {
        "folder": "mitteldeutsche IT Werkstudent KI Entwicklung",
        "company": "mitteldeutsche IT GmbH",
        "lang": "en",
        "role_strip": "KI Engineering Werkstudent",
        "cl_date": "15 July 2026",
        "cl_subject": "Werkstudent KI Entwicklung in Leipzig",
        "profile": "Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, with hands on AI development on LLMs, RAG systems, and workflow automation. I have shipped a modular Retrieval Augmented Generation system with a custom decision making router on Llama 3.1 8b via Groq, a fairness by design credit scoring system covering EU AI Act and GDPR, and a fully automated Bronze to Silver to Gold BigQuery pipeline with a BigQuery ML classifier. Comfortable in Python and structured software engineering, I am the right fit for supporting AI projects, intelligent ticketing systems, and workflow automation at mitteldeutsche IT.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_RAG_EN, P_CREDITIQ_EN, P_MOVIE_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_NVIDIA, CERT_AWS, CERT_GOOGLE],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am applying for the Werkstudent KI Entwicklung role with mitteldeutsche IT in Leipzig. The brief on supporting your teams in AI projects, contributing to intelligent ticketing systems and workflow automations, Python software development, and structured documentation of technical and organisational topics matches what I have been building this year.",
            "My Hybrid RAG Orchestrator is a working LLM system with a custom decision making router that classifies user intent into three execution paths, local knowledge retrieval, external web search, or direct conversational logic, all on Llama 3.1 8b via Groq with LangChain. That is the same shape of engineering that intelligent ticketing systems and RAG driven workflow automations need. In CreditIQ I built a full ML system backed by unit tests at 100 percent branch coverage and a full regulatory write up, showing the reliability and documentation habits mitteldeutsche IT looks for.",
            "In my Movie Analytics and ML Pipeline on GCP I built an end to end Bronze to Silver to Gold BigQuery medallion architecture, fully automated on Cloud Scheduler, secured with a least privilege service account and Secret Manager, with a BigQuery ML classifier and a five page Looker Studio dashboard. That mindset around structured Python software development and secure infrastructure carries directly into your platform.",
            "I am proficient in Python, comfortable working in a team, have my German level at B1 in progress, and hold the NVIDIA Building LLM Applications With Prompt Engineering and AWS Academy Cloud Foundations certificates. I would be glad to start soon and support your KI Entwicklung team.",
        ],
    },

    # 10. MTU Aero Engines — Werkstudent Business Analyst Workflow-Automatisierungen Hannover
    {
        "folder": "MTU Aero Engines Werkstudent Business Analyst",
        "company": "MTU Aero Engines",
        "lang": "en",
        "role_strip": "Business Analyst Werkstudent",
        "cl_date": "15 July 2026",
        "cl_subject": "Working Student, Business Analyst for Workflow Automation",
        "profile": "Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, with hands on business analysis and process automation work across LLM driven agents, cloud pipelines, and BI dashboards. I have shipped a Retrieval Augmented Generation system with agentic routing over Llama 3.1 8b via Groq, a Random Forest driven study translating raw event data into business relevant risk insights, and a fully automated BigQuery medallion pipeline with a five page Looker Studio dashboard. Comfortable in Python, SQL, and workflow thinking, I am the right fit for analysing business processes, identifying automation potential, and supporting the technical rollout of workflow automations.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_RAG_EN, P_CLIMATE_EN, P_MOVIE_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_GOOGLE, CERT_SAS, CERT_NVIDIA],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am applying for the Werkstudent Business Analyst role for workflow automation and digital transformation at MTU Aero Engines in Hannover. The brief on analysing existing business processes, identifying automation potential, defining target processes together with the business, and supporting the technical rollout of process automations aligns directly with the work I have been shipping.",
            "My Hybrid RAG Orchestrator is a working workflow automation system in miniature: a custom decision making router that classifies user intent into three execution paths and dispatches accordingly, backed by a stateful MemoryAgent and a ChromaDB vector store. It is exactly the kind of intelligent routing that sits behind modern process automation platforms. In my Movie Analytics and ML Pipeline on GCP I automated a full Bronze to Silver to Gold pipeline on Cloud Scheduler with no manual steps, secured by a least privilege service account and Secret Manager, and delivered a five page Looker Studio dashboard for decision makers.",
            "In my Economic Impact Analysis of Global Climate Events I translated raw global event datasets into structured insights for resource allocation and risk assessment, running Random Forest models to isolate the drivers of financial impact and communicating the results in reports non technical stakeholders could act on. At eRay GmbH I delivered a recursive time series pipeline with strict anti leakage rules and an orchestrator with gate checks, that mindset carries into designing target processes that are resilient rather than fragile.",
            "I am fluent in English, comfortable in Python and SQL, and hold the Google Data Analytics Foundations and NVIDIA Building LLM Applications With Prompt Engineering certificates. I would be glad to start at the beginning of a month and support the Workflow Automation team on RPA rollouts with Power Automate or UiPath as needed.",
        ],
    },
]
