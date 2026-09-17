"""Role configurations for the 16 September 2026 scheduled job search run
(normal top 3 to 5 cut).

Backlog gate check per 14 July 2026 status source of truth rule: Notion
data source fd974369-40b2-48c5-b660-d15256c88f52 returned 2 rows in status
'drafted' at run start (FZI Forschungszentrum Informatik and iLert GmbH,
both carried over from the 11 September run, still awaiting OpenClaw's
platform-native versus company-portal submission pass). 2 drafted falls
well under the 8 row floor of the 28 July 2026 yield based reset rule,
which allows a normal top 3 to 5 cut.

Reconciliation this run found one drift: ProSiebenSat.1 Careers, Working
Student AI Engineer, Muenchen was still 'drafted' in applied-log.csv but
Notion carried it as 'Not listed Anymore'. Per invariant 1 (Notion is the
source of truth for row status), the CSV row was corrected to match
Notion. No other drift found across 204 CSV rows against 200 Notion rows;
one apparent mismatch (Aerzteverband Deutscher Allergologen with and
without the umlaut) is a spelling variant only, both sides already read
'applied'.

Search ran via Tavily search plus Tavily extract across StepStone, Xing,
JobTeaser and LinkedIn (via Tavily, no direct browser session) plus one
company career page (jobs.sap.com), all reachable this run. No Indeed MCP
tool was available in this session, consistent with prior runs; Tavily
based Indeed search also returned nothing new in scope, so Indeed was not
used this run. Several leads were found and dropped: Retorio GmbH Working
Student AI Engineer Agentic Systems (Munich, Xing) duplicates a company
and near identical role already logged as 'Not listed Anymore'; EXXETA
Werkstudent AI and LLM Engineering (Munich, Xing) duplicates a role
already logged as 'rejected'; appliedAI Initiative GmbH Working Student
AI Engineering and Product Development (Munich) duplicates a company and
near identical role already logged as 'rejected'; Estateanfrage AI
Engineer Trainee (Munich) duplicates a role already logged as 'rejected';
Motius / eigenblue "Join our Tech Community as a Working Student" (Munich,
Xing) is a generic talent pool funnel page with no defined role scope or
task list, not a specific open position, so it was dropped under
invariant 4 (every write must be auditable); Deutsche Boerse Group
Working Student Data and AI Engineering (Frankfurt, JobTeaser and company
career page) reads predominantly as Data Mesh implementation and data
governance support with AI use cases mentioned only in passing, which
falls outside the 26 August 2026 AI Engineer / AI Evaluation narrowing,
so it was dropped as plain Data Engineering; diconium GmbH Working
Student AI Testing Platform (Ingolstadt, Xing) was considered but set
aside in favour of the stronger Temedica match below, since diconium's
scope reads closer to general software test tooling than AI engineering
or evaluation.

Four roles cleared verification: a live posting fetched directly, a
confirmed apply link, and a clean dedup check against applied-log.csv and
Notion (204 CSV rows, 200 Notion rows, full company plus role comparison
run during this run's reconciliation step).

Platform mix this run:
  - Xing, 1 (Syneco Trading GmbH)
  - StepStone, 1 (Charles Real Estate GmbH)
  - Company Page, 2 (SAP jobs.sap.com; Temedica personio-hosted careers
    page, also listed on LinkedIn)
  - LinkedIn, JobTeaser searched this run; JobTeaser yielded only the
    dropped Deutsche Boerse lead above (out of scope) and otherwise
    already logged or off scope postings; LinkedIn (via Tavily search,
    no direct browser session) surfaced the Temedica and SAP leads among
    heavy aggregator noise; neither used as the counted platform mix
    entry once resolved to the company's own posting.

Freshness order (all four fall in the single Germany tier, so ranked by
recency then Best for overlap):
  1. Syneco Trading GmbH, Muenchen, Masterarbeit Agentic AI und Generative
     AI zur Optimierung energiewirtschaftlicher Prozesse, DE track,
     confirmed live via Xing extract, posted within the last 5 days per
     the listing's own "Vor 5 Tagen" marker.
  2. Charles Real Estate GmbH, Berlin, AI Systems Engineer Working
     Student, EN track, confirmed live via a direct StepStone fetch this
     run.
  3. Temedica GmbH, Muenchen, Working Student AI and Agentic Engineering,
     EN track, confirmed live via the company's own Personio-hosted
     careers page, also surfaced on LinkedIn.
  4. SAP, Walldorf, Intern/Thesis/Working Student, Evaluating and
     Improving LLM based SE Solutions in SAP HANA, EN track, confirmed
     live via a direct jobs.sap.com fetch; the listing's own metadata on
     a third party mirror showed an original post date of 19 August 2026,
     so this is treated as an older but still open posting rather than a
     same day find, and is ranked last on recency among the four.

Language track per 20 July 2026 language match hard rule (posting body
language IS deliverable language):
  1. Syneco Trading GmbH posting body written entirely in German -> DE
     track. No explicit German level bar was stated in the posting; Rah's
     B1 in progress level is noted as unconfirmed against the posting's
     actual bar in the digest, same caveat pattern as prior Masterarbeit
     roles at German-language-only employers.
  2. Charles Real Estate GmbH posting body written entirely in English,
     no German requirement stated -> EN track.
  3. Temedica GmbH posting body written entirely in English, no German
     requirement stated -> EN track.
  4. SAP posting body written entirely in English, no German requirement
     stated -> EN track.

Dedup check against applied-log.csv and Notion (204 CSV rows, 200 Notion
rows, full company plus role comparison run during this run's
reconciliation step): Syneco Trading GmbH, Charles Real Estate GmbH, and
Temedica GmbH are all entirely new companies, never previously logged.
SAP has many prior rows logged under other Working Student and Internship
titles, none matching this Evaluating and Improving LLM based SE
Solutions in SAP HANA role, so this is not a duplicate under the standing
company plus role case insensitive match rule.

Apply Method left unset in Notion for all four roles pending OpenClaw's
platform-native versus company-portal determination at submission time;
jobs.sap.com and the Temedica Personio careers page both read as company
owned careers domains from the scraped content alone but the final call
is OpenClaw's per the standing scope split.

19 August 2026 CV content rules apply: no hyphens or dashes in CV text,
no parentheses or brackets in bullets, Languages EN and DE only, German
level locked to "Deutsch: B1, laufend" or "German: B1, in progress" on
the respective track, no page numbers or headers or footers, 2 page hard
cap, Ojas style header, Skills grouped into functional buckets,
positioning tag under the name is a pitch not the posting title.
"""

from role_configs import (
    ERAY_BULLETS_EN,
    ERAY_BULLETS_DE,
    DIABETES_BULLETS_EN,
    DIABETES_BULLETS_DE,
    CERT_NVIDIA,
    CERT_NVIDIA_DE,
    CERT_AWS,
    CERT_AWS_DE,
    CERT_GOOGLE,
    CERT_GOOGLE_DE,
    ACH_USAII_EN,
    ACH_USAII_DE,
    P_RAG_EN,
    P_RAG_DE,
    P_CREDITIQ_EN,
    P_CREDITIQ_DE,
    P_MOVIE_EN,
    P_FLIGHT_DE,
)


CONFIGS_16SEP = [
    # 1. Syneco Trading GmbH, Muenchen
    # Masterarbeit (m/w/d) Agentic AI und Generative AI zur Optimierung
    # energiewirtschaftlicher Prozesse
    # Xing, DE track. Investigates which recurring, manual processes in
    # Bilanzkreis and Fahrplanmanagement can be usefully supported or
    # automated by generative and agentic AI systems, with a research
    # question centred on evaluating those systems for efficiency,
    # quality, robustness and implementation effort.
    # Apply: https://www.xing.com/jobs/muenchen-masterarbeit-agentic-ai-generative-ai-optimierung-energiewirtschaftlicher-prozesse-157808741
    {
        "folder": "Syneco Trading Muenchen Masterarbeit Agentic AI Generative AI Energiewirtschaft",
        "company": "Syneco Trading GmbH",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | Agentische KI und Evaluation | Python + LangGraph + Evaluation Frameworks",
        "role_strip": "Masterarbeit, Agentic AI und Generative AI zur Optimierung energiewirtschaftlicher Prozesse",
        "cl_date": "16. September 2026",
        "cl_subject": "Masterarbeit, Agentic AI und Generative AI zur Optimierung energiewirtschaftlicher Prozesse in Muenchen",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau und in der systematischen Evaluation agentischer und generativer KI Systeme in realen Geschaeftsprozessen. Ich habe ein Multi Agent RAG System mit einem unabhaengigen LLM as Judge Modell gebaut, das Antworten auf 5 Dimensionen bewertet, sowie eine vollautomatisierte Airflow Orchestrierung mit Gate Checks, die wiederkehrende manuelle Prozesse ersetzt. Sicher im Aufbau nachvollziehbarer, auditierbarer Evaluationspipelines fuer nicht deterministische KI Systeme in Python.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_FLIGHT_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Masterarbeit zum Thema Agentic AI und Generative AI zur Optimierung energiewirtschaftlicher Prozesse bei der Syneco Trading GmbH in Muenchen. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim passt die Aufgabe, zu untersuchen, welche Prozesse im Bilanzkreis und Fahrplanmanagement sinnvoll durch generative und agentische KI Systeme unterstuetzt oder automatisiert werden koennen, sehr genau zu dem, was ich in den letzten Monaten praktisch gebaut habe.",
            "In meinem Multi Agent RAG Projekt habe ich einen LanguageAgent und einen JudgeAgent in einem LangGraph Multi Agenten System implementiert, der Antworten in 5 Dimensionen Grounding, Relevanz, Vollstaendigkeit, Zitatqualitaet und Sprachqualitaet im JSON Modus bei Temperatur 0 bewertet, und Self Preference Bias eliminiert, indem der Richter auf einem anderen lokalen Modell laeuft als der Generator. Diese Erfahrung, agentische Systeme systematisch statt subjektiv auf Effizienz, Qualitaet und Robustheit zu evaluieren, deckt sich direkt mit der in der Ausschreibung genannten Forschungsfrage, wie sich generative und agentische KI Systeme hinsichtlich Effizienz, Qualitaet, Robustheit und Implementierungsaufwand evaluieren lassen.",
            "In meinem Real Time Flight Tracking Projekt habe ich das gesamte System mit Apache Airflow auf GCS gestuetztem Speicher und Dataproc Compute orchestriert, sodass Batch und Echtzeit Schichten automatisch alle 15 Minuten ohne manuellen Eingriff aktualisiert werden, und eine dbt Modellierungsschicht gebaut, die jedem Flugzeug konsistent den naechstgelegenen Flughafen zuordnet. Diese Erfahrung, wiederkehrende manuelle Prozesse in eine zuverlaessige automatisierte Pipeline mit klaren Gate Checks zu ueberfuehren, uebertraegt sich direkt auf die Automatisierung wiederkehrender Taetigkeiten im Bilanzkreis und Fahrplanmanagement.",
            "Ich arbeite sicher in Python, LangGraph und scikit learn und habe praktische Erfahrung mit generativer KI und Prompt Engineering. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend, ich hebe es aktiv weiter, und Englisch spreche ich fliessend. Ich kann die Masterarbeit in Muenchen zeitnah beginnen und bespreche das Thema gerne in einem persoenlichen Gespraech.",
        ],
    },

    # 2. Charles Real Estate GmbH, Berlin
    # AI Systems Engineer (Working Student, m/f/d)
    # StepStone, EN track. Builds AI powered applications, agents and
    # automations for a real estate investment and development company,
    # turning business requirements into practical software, designing
    # architectures independently, and deploying production ready
    # applications.
    # Apply: https://www.stepstone.de/stellenangebote--AI-Systems-Engineer-Working-Student-m-f-d-Berlin-Charles-Real-Estate-GmbH--14112550-inline.html
    {
        "folder": "Charles Real Estate Berlin AI Systems Engineer Working Student",
        "company": "Charles Real Estate GmbH",
        "lang": "en",
        "tag": "Data Science Master's Student | Agentic AI and LLM Powered Automation | Python + LangGraph + Cloud Deployment",
        "role_strip": "AI Systems Engineer, Working Student",
        "cl_date": "16 September 2026",
        "cl_subject": "AI Systems Engineer, Working Student in Berlin",
        "profile": "Master's student in Data Science and Analytics at SRH Heidelberg, based in Mannheim, with hands on experience designing, deploying and maintaining production ready AI powered applications and agents. I built a multi agent LangGraph system with independent agents for language detection, retrieval, generation and evaluation, and a fully automated cloud pipeline that runs unattended end to end with 0 manual interventions required. Comfortable turning business requirements into working AI powered software, end to end in Python.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_RAG_EN, P_MOVIE_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_NVIDIA, CERT_AWS, CERT_GOOGLE],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am writing to apply for the AI Systems Engineer Working Student position at Charles Real Estate in Berlin. As a Master's student in Data Science and Analytics at SRH Heidelberg based in Mannheim, the task of turning business requirements into practical AI powered applications, agents and automations that transform workflows, data collection and decision making maps closely to the projects I have shipped in the last several months.",
            "In my Multi Agent RAG project I designed a LangGraph based agent architecture with a LanguageAgent, retrieval agents and a JudgeAgent, each with bounded responsibilities and clear fallback behaviour, including a hard failure on a missing judge model so a silent regression cannot slip through. This experience, designing software architectures and agent systems independently and making technical decisions about how agents hand off work to each other, is exactly what building AI powered applications and automations from the ground up needs.",
            "In my Movie Analytics and ML Pipeline project I built an end to end batch pipeline that pulls data from a public API into a GCS data lake and processes it through a 3 tier Bronze Silver Gold medallion architecture in BigQuery on Cloud Run, running on a fully automated Cloud Scheduler trigger with 0 manual interventions required, and secured it with a least privilege service account and Secret Manager. This experience, deploying and maintaining production ready applications that run unattended rather than living only in a notebook, transfers directly to building and maintaining AI powered internal systems that automate workflows across your business.",
            "I work comfortably in Python, APIs, databases and modern AI development tools, and have hands on experience building AI agents and automations end to end. I hold the NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations and Google Data Analytics certificates and was recognised as a Finalist of the USAII Global AI Hackathon 2026 at Graduate Level. I am fluent in English and B1 in progress in German. I can join in Berlin as a working student immediately and would welcome the chance to discuss how I could contribute to your AI first operating system.",
        ],
    },

    # 3. Temedica GmbH, Muenchen
    # Working Student, AI and Agentic Engineering (f/d/x)
    # Company career page (Personio), also listed on LinkedIn. EN track.
    # Designs, prototypes and develops LLM based applications, AI agents
    # and intelligent automation in digital health, then evaluates and
    # improves those solutions for output quality, reliability, usability
    # and safety in a regulated healthcare environment.
    # Apply: https://temedica.jobs.personio.de/job/2599740?language=en
    {
        "folder": "Temedica Muenchen Working Student AI Agentic Engineering",
        "company": "Temedica GmbH",
        "lang": "en",
        "tag": "Data Science Master's Student | Agentic AI Engineering and Evaluation | Python + LangGraph + Healthcare Compliance",
        "role_strip": "Working Student, AI and Agentic Engineering",
        "cl_date": "16 September 2026",
        "cl_subject": "Working Student, AI and Agentic Engineering in Munich",
        "profile": "Master's student in Data Science and Analytics at SRH Heidelberg, based in Mannheim, with hands on experience designing, prototyping and evaluating LLM based agents in regulated, safety critical settings. I built a multi agent RAG system with an LLM as Judge evaluation that scores output quality and reliability on 5 dimensions, and a fairness by design credit scoring system that cleared GDPR Article 22 and EU AI Act Article 14 human in the loop requirements. Comfortable balancing AI powered product development with output quality, reliability and safety in a regulated environment, in Python.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_RAG_EN, P_CREDITIQ_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_NVIDIA, CERT_AWS, CERT_GOOGLE],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am writing to apply for the Working Student AI and Agentic Engineering position at Temedica in Munich. As a Master's student in Data Science and Analytics at SRH Heidelberg based in Mannheim, the task of designing, prototyping and developing LLM based applications and AI agents while evaluating and improving them for output quality, reliability, usability and safety in a regulated healthcare environment maps closely to the projects I have shipped in the last several months.",
            "In my Multi Agent RAG project I built a JudgeAgent that scores answers on 5 dimensions, groundedness, relevance, completeness, citation quality and language quality, in JSON mode at temperature 0, with a self_judged flag propagated into every report and a hard failure on a missing judge model so a silent fallback cannot regress unnoticed. This discipline, treating output quality and reliability as something to measure and enforce rather than assume, is exactly what evaluating AI agents for real world use in a healthcare context needs.",
            "In my CreditIQ project I applied AIF360 mitigation and threshold calibration to bring a regulated credit scoring model back into compliance, used SHAP driven subgroup analysis to find and correct a hidden intersectional bias, and shipped a Streamlit decision support tool backed by a full regulatory write up spanning the EU AI Act, GDPR, a model card and attack vectors, clearing GDPR Article 22 and EU AI Act Article 14 human in the loop requirements. This experience, designing AI powered decision support for a regulated, safety critical domain rather than a low stakes demo, transfers directly to building intelligent automation solutions that create real value for patients and clinicians in digital health.",
            "I work comfortably in Python and have hands on experience developing AI agentic applications using LangGraph and similar frameworks. I hold the NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations and Google Data Analytics certificates and was recognised as a Finalist of the USAII Global AI Hackathon 2026 at Graduate Level. I am fluent in English and B1 in progress in German. I can join in Munich as a working student immediately and would welcome the chance to discuss how I could contribute to your AI powered health insights work.",
        ],
    },

    # 4. SAP, Walldorf
    # Intern/Thesis/Working Student (f/m/d), Evaluating and Improving
    # LLM based SE Solutions in SAP HANA
    # Company career page (jobs.sap.com). EN track. Supports an internal
    # PhD driven research project evaluating the usefulness of LLMs in
    # the context of a 10 million line codebase not in any public LLM's
    # training data, across tasks like test generation, fault
    # localisation, LLM as a judge, code review automation and
    # benchmarking.
    # Apply: https://jobs.sap.com/job/Walldorf-InternThesisWorking-Student-%28fmd%29-Evaluating-and-Improving-LLM-based-SE-Solutions-in-SAP-HANA-69190/1427816733
    {
        "folder": "SAP Walldorf Evaluating Improving LLM SE Solutions SAP HANA",
        "company": "SAP",
        "lang": "en",
        "tag": "Data Science Master's Student | LLM Evaluation and Software Engineering | Python + Evaluation Frameworks + LangGraph",
        "role_strip": "Intern, Thesis or Working Student, Evaluating and Improving LLM based SE Solutions in SAP HANA",
        "cl_date": "16 September 2026",
        "cl_subject": "Intern, Thesis or Working Student, Evaluating and Improving LLM based SE Solutions in SAP HANA in Walldorf",
        "profile": "Master's student in Data Science and Analytics at SRH Heidelberg, based in Mannheim, with hands on experience building and evaluating LLM powered systems end to end. I built an LLM as Judge evaluation harness that scores answers on 5 dimensions in JSON mode at temperature 0 with a hard failure on a missing judge model, and a fairness by design credit scoring system backed by unit tests at 100 percent branch coverage and a full regulatory write up. Comfortable designing evaluation metrics and benchmarks that expose real quality gaps in non deterministic AI systems, in Python.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_RAG_EN, P_CREDITIQ_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_NVIDIA, CERT_AWS, CERT_GOOGLE],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am writing to apply for the Intern, Thesis or Working Student position on Evaluating and Improving LLM based SE Solutions in SAP HANA at SAP in Walldorf. As a Master's student in Data Science and Analytics at SRH Heidelberg based in Mannheim, the task of determining concrete recommendations for how to apply LLM in software engineering tasks such as test generation, fault localisation, LLM as a judge and benchmarking maps closely to the projects I have shipped in the last several months.",
            "In my Multi Agent RAG project I built a JudgeAgent that scores answers on 5 dimensions, groundedness, relevance, completeness, citation quality and language quality, in JSON mode at temperature 0, and eliminated self preference bias by running the judge Qwen2.5 14B on a different local model from the generator Mistral 7B, with a self_judged flag propagated into every report and a hard failure on a missing judge model so a silent fallback cannot regress unnoticed. This same discipline, designing an LLM as a judge evaluation that exposes real quality gaps rather than hiding them, is exactly what determining concrete recommendations for LLM usage on a 10 million line codebase like SAP HANA needs.",
            "In my CreditIQ project I applied AIF360 mitigation and threshold calibration to bring a regulated credit scoring model back into compliance, backed the pipeline with unit tests at 100 percent branch coverage, and documented a fairness accuracy trade off as a deliberate, regulator defensible decision rather than an accident. This experience, holding a non deterministic system to a rigorous, benchmarked evaluation standard before trusting its output, transfers directly to software reliability engineering tasks such as code review automation, bug fix analysis and test flakiness improvements for LLM based tooling.",
            "I work comfortably in Python and have hands on experience with LLM as a judge evaluation, prompt engineering and benchmarking non deterministic systems. I hold the NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations and Google Data Analytics certificates and was recognised as a Finalist of the USAII Global AI Hackathon 2026 at Graduate Level. I am fluent in English and B1 in progress in German. I can join in Walldorf as an intern, thesis student or working student and would welcome the chance to discuss the research direction with the team.",
        ],
    },
]
