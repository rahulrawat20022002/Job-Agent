"""Role configurations for the 11 September 2026 scheduled job search run
(second run of the day; the 13:32 run found 0 drafts due to a search
source outage that had cleared by this run).

Backlog gate check per 14 July 2026 status source of truth rule: Notion
data source fd974369-40b2-48c5-b660-d15256c88f52 returned 0 rows in status
'drafted' at run start (the 1 carried over Estateanfrage row moved to
'rejected' between the two runs today, presumably by Rah). 0 drafted
falls well under the 8 row floor of the 28 July 2026 yield based reset
rule, which allows a normal top 3 to 5 cut.

This run's search (Tavily search plus Tavily extract; WebFetch remained
EGRESS_BLOCKED for every domain tested, same as the two prior runs) found
Tavily itself reachable again after being down on 9 and 11 Sep's earlier
run. Search still ran into heavy attrition: several promising leads
(CognitX AI GmbH AI/LLM Engineering Werkstudent on Xing, bundesweit.digital
GmbH KI Prompting/Prompt Engineer Werkstudent on StepStone) returned "job
ad isn't available" or a 404 on direct extract and were dropped rather
than drafted from a stale search snippet. Prelytics GmbH's Praktikant LLM
RAG and Machine Learning Engineer posting was confirmed live but reads as
an unpaid, non mandatory Praktikum at a startup with no Pflichtpraktikum
framing, so it was dropped under the standing voluntary internship
exclusion. Cinemo GmbH's Working Student GenAI/LLM Evaluation posting
resurfaced but duplicates a row already logged as 'applied'. Several
Mercedes-Benz Tech Innovation, Reply Deutschland, Transdev, and Atruvia
leads surfaced only as aggregator snippets or "similar jobs" sidebar
entries with no independently confirmed live posting URL, so none were
drafted per invariant 4, every write must be auditable.

Three roles cleared verification: a live posting fetched directly, a
confirmed apply link, and a clean dedup check against applied-log.csv and
Notion.

Platform mix this run:
  - Xing, 1 (FZI Forschungszentrum Informatik)
  - StepStone, 2 (ProSiebenSat.1, iLert GmbH)
  - LinkedIn, JobTeaser searched via Tavily this run but yielded only
    already logged roles, expired listings, or off scope postings; none
    used this run. Indeed not used this run (no Indeed MCP tool available
    in this session, consistent with prior runs; Tavily based Indeed
    search also returned nothing new in scope).

Freshness order (all three fall in the single Germany tier, so ranked by
recency then Best for overlap):
  1. FZI Forschungszentrum Informatik, Karlsruhe, Masterarbeit Evaluation
     and Verification of AI Generated Driving Scenarios, DE track,
     confirmed live via Xing extract immediately before drafting.
  2. ProSiebenSat.1 Careers, Muenchen, Working Student AI Engineer, EN
     track, surfaced in a same day Tavily search window.
  3. iLert GmbH, Cologne, Working Student or Intern AI Product Engineer,
     EN track, surfaced in the same same day search window.

Language track per 20 July 2026 language match hard rule (posting body
language IS deliverable language):
  1. FZI posting body written in German (Aufgaben under "Das erwartet
     Dich bei uns" section) -> DE track. No explicit German level bar
     was visible in the scraped content (the requirements bullet list did
     not render in the extract); Rah's B1 in progress level is noted as
     unconfirmed against the posting's actual bar in the digest.
  2. ProSiebenSat.1 posting body written entirely in English, no German
     requirement stated -> EN track.
  3. iLert posting body written entirely in English, no German
     requirement stated -> EN track.

Dedup check against applied-log.csv and Notion (197 rows, full company
plus role comparison run during this run's reconciliation step): FZI
Forschungszentrum Informatik, ProSiebenSat.1, and iLert GmbH are all
entirely new companies, never previously logged.

Apply Method left unset in Notion for all three roles pending OpenClaw's
platform-native versus company-portal determination at submission time,
per the standing 'Apply Method if known' rule; none was independently
confirmed as staying inside the aggregator's own apply flow from the
scraped content alone.

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
)


CONFIGS_11SEP = [
    # 1. FZI Forschungszentrum Informatik, Karlsruhe
    # Student in (Abschlussarbeit Master) zum Thema Evaluation and
    # Verification of AI Generated Driving Scenarios Using Scenario Dreamer
    # Xing, DE track, hourly based, fixed term, department ESM (Eingebettete
    # Systeme und Mikrosysteme), evaluates and tests AI models with a focus
    # on the automotive sector and generative AI for images and video.
    # Apply: https://www.xing.com/jobs/karlsruhe-student-abschlussarbeit-master-thema-evaluation-and-verification-of-ai-generated-driving-scenarios-using-scenario-dreamer-152602249
    {
        "folder": "FZI Karlsruhe Masterarbeit Evaluation Verification AI Generated Driving Scenarios",
        "company": "FZI Forschungszentrum Informatik",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | KI Evaluation und Agentische Systeme | Python + LangGraph + Evaluation Frameworks",
        "role_strip": "Abschlussarbeit Master, Evaluation and Verification of AI Generated Driving Scenarios Using Scenario Dreamer",
        "cl_date": "11. September 2026",
        "cl_subject": "Abschlussarbeit Master, Evaluation and Verification of AI Generated Driving Scenarios in Karlsruhe",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau und in der systematischen Evaluation generativer KI Systeme. Ich habe ein Multi Agent RAG System mit einem unabhaengigen LLM as Judge Modell gebaut, das Antworten auf 5 Dimensionen bewertet, sowie einen EvalAgent, der 5 Retrieval Metriken und 4 Generierungsmetriken pro Sprache aggregiert. Sicher im Aufbau nachvollziehbarer, auditierbarer Evaluationspipelines fuer nicht deterministische KI Systeme in Python.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_CREDITIQ_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Abschlussarbeit Master zum Thema Evaluation and Verification of AI Generated Driving Scenarios Using Scenario Dreamer am FZI Forschungszentrum Informatik in Karlsruhe. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim passt die Aufgabe Ihrer Abteilung Eingebettete Systeme und Mikrosysteme, KI Modelle mit starkem Fokus auf der Automobilbranche zu entwickeln, zu evaluieren und zu testen, sehr genau zu dem, was ich in den letzten Monaten praktisch gebaut habe.",
            "In meinem Multi Agent RAG Projekt habe ich einen JudgeAgent implementiert, der Antworten in 5 Dimensionen Grounding, Relevanz, Vollstaendigkeit, Zitatqualitaet und Sprachqualitaet im JSON Modus bei Temperatur 0 bewertet, und Self Preference Bias eliminiert, indem der Richter Qwen2.5 14B auf einem anderen lokalen Modell laeuft als der Generator Mistral 7B. Zusaetzlich habe ich einen EvalAgent gebaut, der 5 Retrieval Metriken und 4 Generierungsmetriken pro Sprache in JSON und Markdown Berichten aggregiert. Diese Erfahrung, nicht deterministische KI Ausgaben systematisch statt subjektiv zu bewerten, deckt sich direkt mit der Aufgabe, KI generierte Fahrszenarien zu evaluieren und zu verifizieren.",
            "In meinem CreditIQ Projekt zur fairen Kreditvergabe habe ich AIF360 Mitigation und Schwellenwertkalibrierung auf einem realen Kreditdatensatz angewendet, eine versteckte intersektionale Verzerrung ueber SHAP basierte Subgruppenanalyse aufgedeckt und korrigiert, und einen vollstaendigen regulatorischen Bericht ueber EU AI Act Anhang III, DSGVO, Modellkarte und Angriffsvektoren erstellt. Diese Erfahrung, quantitative Bewertungskriterien so zu waehlen, dass sie echte Fehlermuster offenlegen statt sie zu verdecken, und die Ergebnisse fuer ein regulatorisches Audit nachvollziehbar zu dokumentieren, uebertraegt sich direkt auf die Verifikation KI generierter Inhalte in einem sicherheitskritischen automobilen Kontext.",
            "Ich arbeite sicher in Python, LangGraph und scikit learn und habe praktische Erfahrung mit generativer KI und Prompt Engineering. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend, ich hebe es aktiv weiter, und Englisch spreche ich fliessend. Ich kann die Abschlussarbeit in Karlsruhe ab sofort beginnen. Gerne bespreche ich das Thema in einem persoenlichen Gespraech mit Herrn Schenkel.",
        ],
    },

    # 2. ProSiebenSat.1 Careers, Muenchen
    # Working Student AI Engineer (m/f/d), AI Tech Personalization team
    # StepStone, EN track. Works on recommendation systems for movie,
    # series and live TV experiences, explores and evaluates new machine
    # learning methods including LLM applications for recommender systems.
    # Apply: https://www.stepstone.de/stellenangebote--working-student-ai-engineer-m-f-d-muenchen-prosiebensat-1-careers--13800397-inline.html
    {
        "folder": "ProSiebenSat1 Muenchen Working Student AI Engineer",
        "company": "ProSiebenSat.1 Careers",
        "lang": "en",
        "tag": "Data Science Master's Student | LLM Evaluation and Recommendation Systems | Python + LangGraph + BigQuery",
        "role_strip": "Working Student, AI Engineer",
        "cl_date": "11 September 2026",
        "cl_subject": "Working Student, AI Engineer in Munich",
        "profile": "Master's student in Data Science and Analytics at SRH Heidelberg, based in Mannheim, with hands on experience building and evaluating LLM powered systems end to end. I built a multi agent RAG system with an LLM as Judge evaluation that scores answers on 5 dimensions in JSON mode at temperature 0, and a fully automated cloud pipeline that turned raw movie data into a leakage free hit prediction classifier plus a 5 page analytics dashboard. Comfortable exploring and evaluating new machine learning methods, including LLM applications, end to end in Python.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_RAG_EN, P_MOVIE_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_NVIDIA, CERT_AWS, CERT_GOOGLE],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am writing to apply for the Working Student AI Engineer position on the AI Tech Personalization team at ProSiebenSat.1 in Munich. As a Master's student in Data Science and Analytics at SRH Heidelberg based in Mannheim, the task of exploring and evaluating new machine learning methods, including LLM applications for recommender systems, maps closely to the projects I have shipped in the last several months.",
            "In my Multi Agent RAG project I built a JudgeAgent that scores answers on 5 dimensions, groundedness, relevance, completeness, citation quality and language quality, in JSON mode at temperature 0, and eliminated self preference bias by running the judge Qwen2.5 14B on a different local model from the generator Mistral 7B. I also built an EvalAgent computing 5 retrieval metrics and 4 generation metrics aggregated into JSON and Markdown reports. This same discipline, choosing evaluation metrics that expose real quality gaps rather than hide them, is exactly what evaluating a new LLM based recommendation method needs before it ships to millions of users.",
            "In my Movie Analytics and ML Pipeline project I built an end to end batch pipeline that pulls movie data from a public API into a GCS data lake and processes it through a 3 tier Bronze Silver Gold medallion architecture in BigQuery on Cloud Run, running on a fully automated Cloud Scheduler trigger with 0 manual interventions. I trained a leakage free hit prediction classifier by deliberately splitting features into pre release and post release tables, then closed with a 5 page Looker Studio dashboard answering questions on genre ROI and release season timing. Working directly with movie and entertainment data on a fully automated cloud pipeline is close to the recommendation systems work your Personalization team runs for movie, series and live TV experiences.",
            "I work comfortably in Python, LangGraph and BigQuery, and hold the NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations and Google Data Analytics certificates. I was recognised as a Finalist of the USAII Global AI Hackathon 2026 at Graduate Level. I am fluent in English and B1 in progress in German. I can join in Munich as a working student immediately and would welcome the chance to discuss how I could contribute to your Personalization team.",
        ],
    },

    # 3. iLert GmbH, Cologne
    # Working Student / Intern: AI Product Engineer (f/m/x)
    # StepStone, EN track. Builds agentic AI SRE agents that investigate,
    # analyse and mitigate production issues, designs agent reasoning loops
    # and prompt templates, and builds guardrails and validation layers so
    # the agents act safely and deterministically.
    # Apply: https://www.stepstone.de/stellenangebote--Working-Student-Intern-AI-Product-Engineer-f-m-x-Cologne-iLert-GmbH--13513211-inline.html
    {
        "folder": "iLert Cologne Working Student Intern AI Product Engineer",
        "company": "iLert GmbH",
        "lang": "en",
        "tag": "Data Science Master's Student | Agentic AI and Guardrails Engineering | Python + LangGraph + Prompt Engineering",
        "role_strip": "Working Student or Intern, AI Product Engineer",
        "cl_date": "11 September 2026",
        "cl_subject": "Working Student or Intern, AI Product Engineer in Cologne",
        "profile": "Master's student in Data Science and Analytics at SRH Heidelberg, based in Mannheim, with hands on experience designing agent reasoning loops and safety guardrails for LLM powered systems. I built a LanguageAgent that centralises seeded language detection with a confidence floor, and a JudgeAgent with a hard failure on a missing judge model so a silent fallback cannot regress unnoticed, plus a fairness by design credit scoring system backed by a full regulatory write up covering attack vectors and human in the loop requirements. Comfortable building agentic systems end to end in Python and LangGraph with real safety constraints, not just prompts.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_RAG_EN, P_CREDITIQ_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_NVIDIA, CERT_AWS, CERT_GOOGLE],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am writing to apply for the Working Student or Intern AI Product Engineer position at iLert in Cologne. As a Master's student in Data Science and Analytics at SRH Heidelberg based in Mannheim, the task of designing agent reasoning loops and building guardrails and validation layers so autonomous AI agents act safely and deterministically maps closely to the projects I have shipped in the last several months.",
            "In my Multi Agent RAG project I built a LanguageAgent that centralises seeded language detection with a confidence floor and propagates a single output language directive to every downstream agent, and a JudgeAgent that scores every answer on 5 dimensions with a self judged flag and a hard failure on a missing judge model, so a silent fallback to self judging cannot regress unnoticed. Building a multi agent system where every agent's behaviour is bounded, monitored and falls back safely rather than silently is exactly the discipline your reliability and safety guardrails need for AI SRE agents acting on real infrastructure.",
            "In my CreditIQ project I applied AIF360 mitigation and threshold calibration to bring a regulated credit scoring model back into compliance, used SHAP driven subgroup analysis to expose and correct a hidden intersectional bias, and delivered a Streamlit decision support tool backed by a full regulatory write up spanning the EU AI Act, GDPR, a model card and attack vectors, clearing GDPR Article 22 and EU AI Act Article 14 human in the loop requirements. This experience, treating safety and compliance as a deliberate design constraint rather than an afterthought, transfers directly to building validation layers that keep agentic AI systems acting safely on production infrastructure like Kubernetes, GitHub and AWS.",
            "I work comfortably in Python and LangGraph, and have experimented with LLM based agents including RAG, prompting and agentic workflows. I hold the NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations and Google Data Analytics certificates and was recognised as a Finalist of the USAII Global AI Hackathon 2026 at Graduate Level. I am fluent in English and B1 in progress in German. I can join in Cologne as a working student or intern immediately and would welcome the chance to discuss how I could contribute to your AI SRE agent work.",
        ],
    },
]
