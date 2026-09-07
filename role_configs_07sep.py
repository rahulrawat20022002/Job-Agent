"""Role configurations for the 7 September 2026 scheduled job search run.

Backlog gate check per 14 July 2026 status source of truth rule: Notion
data source fd974369-40b2-48c5-b660-d15256c88f52 returned 0 rows in status
'drafted' at run start. 0 drafted falls well under the 8 row floor of the
28 July 2026 yield based reset rule, which allows a normal top 3 to 5 cut.

Reconciliation this run found 3 CSV rows still marked 'drafted' (Mercedes-
Benz Tech Innovation Werkstudent AI Agents and Robotics Platform, Beilmann
Marketing GmbH Werkstudent KI Automatisierung und interne Tools, ETG-
Elektronik GmbH Praktikant or Werkstudent AI Systems and Generative AI)
that Notion already showed as 'applied'; the CSV was corrected to match
Notion for all three, no reverse writes. Reconciliation also found 4
Notion rows with no CSV counterpart at all (Mi-Jack Europe GmbH, appliedAI
Initiative GmbH, KontextWork GbR, Rohde und Schwarz GmbH und Co. KG
Teisnach Agentic AI Experiments); these were backfilled into the CSV
mirror with Notion's status and Draft Path, original draft date left
blank since it could not be verified from any source in this checkout.

Platform mix this run:
  - StepStone (Mercedes-Benz Tech Innovation), 1
  - Xing (Generali Deutschland AG, EXXETA), 2
  - Company career page (Merantix Momentum, via the Merantix AI Campus
    job board), 1
  - LinkedIn, JobTeaser, and Indeed were all searched this run (LinkedIn
    and JobTeaser via Tavily search, Indeed via Tavily search since no
    Indeed MCP tool was available in this session) but yielded only
    postings already logged, out of scope for the 26 August 2026 AI
    Engineer and AI Evaluation narrowing, or full time and international
    roles outside the Werkstudent and Pflichtpraktikum work types; none
    used this run.

Freshness order per 12 July 2026 priority rule within the single Germany
tier, all Werkstudent, all posted within the last 1 to 2 weeks per
StepStone and Xing timestamps at search time:
  1. Mercedes-Benz Tech Innovation, Werkstudent Machine Learning
     Engineering, Karlsruhe, DE track.
  2. Generali Deutschland AG, Werkstudent Machine Learning Engineering,
     Saarbruecken, DE track.
  3. EXXETA, Werkstudent AI and LLM Engineering, Muenchen, DE track.
  4. Merantix Momentum, Working Student AI Full Stack Engineer, Berlin,
     EN track (posting body is written in English).

Language track per 20 July 2026 language match hard rule (posting body
language IS deliverable language): the first three postings are written
in German, so all three ship DE track. The Merantix Momentum posting is
written in English end to end, so it ships EN track.

Language level transparency: none of the four postings state an explicit
minimum German level (CEFR grade). Mercedes-Benz Tech Innovation asks for
"gute Deutsch- und Englischkenntnisse in Wort und Schrift" (good German
AND English), a step above Rah's current B1 in progress; shipped per the
standing rule that language level does not filter listings, cover letter
stays upfront about the current level. Generali and EXXETA postings do
not state a language bar beyond the German posting body itself. Merantix
Momentum's posting is entirely in English and does not mention German at
all.

Apply method transparency: Mercedes-Benz Tech Innovation's StepStone
listing routes through the company's own careers flow on
mercedesbenztechinnovation.wd3.myworkdayjobs.com (Workday), consistent
with prior MBTI listings, recorded as company-portal with the StepStone
URL kept as the confirmed working Apply Link. Generali Deutschland AG and
EXXETA are both Xing Easy Apply / Schnelle Bewerbung listings,
platform-native, in OpenClaw's automated scope. Merantix Momentum's Apply
Link routes to the Merantix AI Campus job board (a company-affiliated
careers site, not a platform-native aggregator flow), recorded as
company-portal.

Dedup check against applied-log.csv and Notion: Mercedes-Benz Tech
Innovation already has four prior entries logged (Werkstudent Data
Engineering and Data Science, rejected; Werkstudent Agentic AI und
Multi-Agent-Systeme, Not listed Anymore; Werkstudent AI Security Research
und Evaluation, Not listed Anymore; Werkstudent AI Agents and Robotics
Platform, applied) but not this Machine Learning Engineering role,
allowed under the different roles at the same company rule. Generali
Deutschland AG, EXXETA, and Merantix Momentum are all entirely new
companies, never previously logged. A Kenbun IT AG Werkstudent Data
Science and Deep Learning posting found on StepStone this run was
reviewed and dropped rather than drafted: its core task is quality review
of French audio and text data requiring near native French at C2 level,
with machine learning evaluation work listed only as an optional stretch
topic, so it does not read as an AI Engineer or AI Evaluation role under
the 26 August 2026 scope narrowing and Rah does not hold C2 French.

19 August 2026 CV content rules apply: no hyphens or dashes in CV text,
no parentheses or brackets in bullets, Languages EN and DE only, German
level locked to "Deutsch: B1, laufend" or "German: B1, in progress" on
the respective track, no page numbers or headers or footers, 2 page hard
cap, Ojas style header, Skills grouped into functional buckets,
positioning tag under the name is a pitch not the posting title, and
banned strings on the validation gate are met by the new header.
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
    P_MOVIE_DE,
)


CONFIGS_07SEP = [
    # 1. Mercedes-Benz Tech Innovation, Karlsruhe
    # Werkstudent Machine Learning Engineering (d/m/w/x)
    # StepStone, DE track
    # Tasks: further developing large language models into multimodal
    # models for audio and vision, researching and preparing multimodal
    # training datasets, building and managing data, training and
    # evaluation pipelines in the cloud, fine tuning base models such as
    # Qwen, working with RAG, tool calling and agentic behaviour.
    # Requirements: studies in computer science, data science, AI,
    # machine learning or related; experience with Python and training
    # deep learning and machine learning models; understanding of how
    # LLMs work and are trained; good German and English.
    # Apply: https://www.stepstone.de/stellenangebote--Werkstudent-Machine-Learning-Engineering-d-m-w-x-Karlsruhe-Mercedes-Benz-Tech-Innovation--14400316-inline.html
    # Apply method: company-portal (routes to Mercedes-Benz's own Workday careers flow)
    {
        "folder": "MBTI Karlsruhe Werkstudent Machine Learning Engineering",
        "company": "Mercedes-Benz Tech Innovation",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | Machine Learning Engineering fuer multimodale LLMs | Python + RAG + Evaluationspipelines",
        "role_strip": "Werkstudent Machine Learning Engineering",
        "cl_date": "7. September 2026",
        "cl_subject": "Werkstudent Machine Learning Engineering in Karlsruhe",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Training, Fine Tuning und der systematischen Evaluation von Large Language Models. Ich habe ein Multi Agent RAG System vollstaendig lokal ueber Ollama betrieben, mit Mistral 7B als Generator und Qwen2.5 14B als unabhaengigem LLM as Judge, und dabei eigene Trainings und Evaluationspipelines fuer ein gepaartes mehrsprachiges Datenset aufgebaut. Sicher in Python, Deep Learning Frameworks, Cloud Pipelines und der praktischen Arbeit mit RAG, Tool Calling und agentischem Verhalten.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_MOVIE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit Machine Learning Engineering bei Mercedes-Benz Tech Innovation am Standort Karlsruhe. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim passt die in der Ausschreibung beschriebene Arbeit an multimodalen LLMs, Trainings und Evaluationspipelines in der Cloud sowie RAG und agentischem Verhalten sehr genau zu dem, was ich in den letzten Monaten praktisch gebaut habe.",
            "In meinem Multi Agent RAG Projekt habe ich ein LangGraph orchestriertes Agentensystem mit vollstaendig lokaler Inferenz ueber Ollama aufgebaut, Mistral 7B als Generator und Qwen2.5 14B als unabhaengigen LLM as Judge auf einem separaten Modell eingesetzt, um Self Preference Bias auszuschliessen, und einen EvalAgent geschrieben, der 5 Retrieval Metriken und 4 Generation Metriken pro Sprache in JSON und Markdown Reports auf einem gepaarten EN und DE Datenset aggregiert. Genau diese Kombination aus Datenaufbereitung, Fine Tuning nahen Modellarbeiten und systematischer Evaluation deckt sich mit der in der Ausschreibung beschriebenen Aufgabe im Bereich Trainings und Evaluationspipelines.",
            "In meinem Movie Analytics und ML Pipeline Projekt habe ich eine vollautomatisierte Batch Pipeline mit einem BigQuery ML Klassifikator gebaut, der bewusst nur Pre Release Signale sieht, damit keine Leckage im Trainingssatz auftaucht, orchestriert ueber einen Cloud Scheduler Trigger ohne manuelle Eingriffe. Diese Erfahrung, Trainingsdaten sauber zu trennen, Modelle in der Cloud zu orchestrieren und Ergebnisse nachvollziehbar zu dokumentieren, uebertraegt sich direkt auf die Erstellung und das Management von Daten, Trainings und Evaluationspipelines in der Cloud.",
            "Ich arbeite sicher in Python und mit Deep Learning und Machine Learning Frameworks und beschaeftige mich aktiv mit aktuellen Ansaetzen rund um RAG, Tool Calling und agentisches Verhalten. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend, ich hebe es aktiv weiter, und Englisch spreche ich fliessend. Ich kann als Werkstudent in Karlsruhe flexibel einsteigen. Gerne bespreche ich meinen Beitrag zu Ihrem Machine Learning Engineering Team in einem persoenlichen Gespraech.",
        ],
    },

    # 2. Generali Deutschland AG, Saarbruecken
    # Werkstudent (m/w/d) Machine Learning Engineering
    # Xing, DE track
    # Tasks: supporting the Machine Learning Engineering team building
    # intelligent assistants, for example generative AI based chatbots or
    # agents, developing, testing and bringing AI supported solutions into
    # practice, department Analytics and AI.
    # Apply: https://www.xing.com/jobs/saarbruecken-werkstudent-machine-learning-engineering-155911815
    # Apply method: platform-native (Xing Easy Apply / Schnelle Bewerbung)
    {
        "folder": "Generali Saarbruecken Werkstudent Machine Learning Engineering",
        "company": "Generali Deutschland AG",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | Generative KI Chatbots und Agenten | Python + LangGraph + LLM Evaluation",
        "role_strip": "Werkstudent Machine Learning Engineering",
        "cl_date": "7. September 2026",
        "cl_subject": "Werkstudent Machine Learning Engineering in Saarbruecken",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau intelligenter Assistenten auf Basis generativer KI in regulierten Branchen. Ich habe ein Multi Agent RAG System mit LLM as Judge Evaluation gebaut und in CreditIQ ein Kredit Scoring System entwickelt, das den Disparate Impact von 0,79 auf 0,88 gehoben hat, mit vollstaendiger Dokumentation fuer EU AI Act und GDPR Anforderungen. Sicher in Python, LangGraph, scikit learn und der Ueberfuehrung von KI Modellen in produktionsnahe Tools.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_CREDITIQ_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit Machine Learning Engineering in der Abteilung Analytics und AI bei der Generali Deutschland AG am Standort Saarbruecken. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim reizt mich die in der Ausschreibung beschriebene Aufgabe, intelligente Assistenten wie generative KI basierte Chatbots oder Agents zu entwickeln, zu testen und in die Praxis zu ueberfuehren, weil ich in den letzten Monaten genau solche Systeme von der Idee bis zum lauffaehigen Werkzeug gebaut habe.",
            "In meinem Multi Agent RAG Projekt habe ich ein LangGraph orchestriertes Agentensystem gebaut, das Nutzerfragen ueber eine hybride BM25 plus Dense Retrieval Pipeline beantwortet, mit einem JudgeAgent, der Antworten automatisiert im JSON Modus auf 5 Dimensionen bewertet, statt Qualitaet manuell zu pruefen. Diese Erfahrung, einen intelligenten Assistenten end to end zu bauen und seine Antwortqualitaet systematisch zu testen, laesst sich direkt auf generative KI basierte Chatbots und Agents im Versicherungskontext uebertragen.",
            "In CreditIQ habe ich unter EU AI Act und AGG Anforderungen ein Kredit Scoring System entwickelt, den Disparate Impact von 0,79 auf 0,88 gehoben und das Modell als Streamlit Decision Support Tool mit einer plain language LLM generierten Erklaerung fuer den Endbenutzer ausgeliefert, begleitet von einem vollstaendigen regulatorischen Dossier zu EU AI Act, GDPR und Modellkarte. Diese Erfahrung, ein KI gestuetztes Tool in einer regulierten Branche verantwortungsvoll und nachvollziehbar auszuliefern, passt gut zum Aufbau intelligenter Assistenten in einem Versicherungsunternehmen.",
            "Ich arbeite sicher in Python, LangGraph und scikit learn und habe Freude daran, KI Modelle in nutzbare, getestete Tools zu ueberfuehren. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend, ich hebe es aktiv weiter, und Englisch spreche ich fliessend. Ich kann als Werkstudent in Saarbruecken flexibel einsteigen. Gerne bespreche ich meinen Beitrag zu Ihrem Machine Learning Engineering Team in einem persoenlichen Gespraech.",
        ],
    },

    # 3. EXXETA, Muenchen
    # Werkstudent AI & LLM Engineering (all genders)
    # Xing (also listed on Indeed), DE track
    # Tasks: developing innovative AI solutions at the intersection of
    # technology, strategy and business, generative AI, large language
    # models and machine learning, from first idea to application.
    # Apply: https://www.xing.com/jobs/muenchen-werkstudent-ai-llm-engineering-all-genders-156675659
    # Apply method: platform-native (Xing Easy Apply / Schnelle Bewerbung)
    {
        "folder": "EXXETA Muenchen Werkstudent AI LLM Engineering",
        "company": "EXXETA",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | Generative AI und LLM Loesungen | Python + LangGraph + RAG",
        "role_strip": "Werkstudent AI und LLM Engineering",
        "cl_date": "7. September 2026",
        "cl_subject": "Werkstudent AI und LLM Engineering in Muenchen",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau generativer KI Loesungen von der ersten Idee bis zur produktionsnahen Anwendung. Ich habe ein Multi Agent RAG System mit LLM as Judge Evaluation gebaut und in CreditIQ ein Kredit Scoring System entwickelt, das eine Fairness Grenze von 0,79 auf 0,88 gehoben hat. Sicher in Python, LangGraph, RAG Architekturen und der Uebersetzung von Geschaeftsanforderungen in lauffaehige KI Loesungen.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_CREDITIQ_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit AI und LLM Engineering bei EXXETA am Standort Muenchen. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim passt die in der Ausschreibung beschriebene Arbeit an der Schnittstelle von Technologie, Strategie und Geschaeft, generative AI, Large Language Models und Machine Learning, sehr genau zu dem, was ich in den letzten Monaten praktisch gebaut habe.",
            "In meinem Multi Agent RAG Projekt habe ich ein LangGraph orchestriertes Agentensystem von der Architektur bis zur systematischen Evaluation selbststaendig entwickelt, mit einem JudgeAgent, der Antworten automatisiert im JSON Modus auf 5 Dimensionen bewertet, und einem EvalAgent, der Retrieval und Generation Metriken pro Sprache aggregiert. Diese Erfahrung, eine generative KI Loesung von der ersten Idee bis zur belastbaren Evaluation zu tragen, deckt sich mit der in der Ausschreibung beschriebenen Aufgabe im Bereich AI und LLM Engineering.",
            "In CreditIQ habe ich eine geschaeftskritische Fragestellung, faire und regelkonforme Kreditentscheidungen, in ein lauffaehiges Machine Learning System uebersetzt, den Disparate Impact von 0,79 auf 0,88 gehoben und das Ergebnis als Streamlit Decision Support Tool fuer einen Fachbereich ausgeliefert. Diese Faehigkeit, zwischen technischer Umsetzung und Geschaeftsanforderung zu vermitteln, passt gut zur in der Ausschreibung beschriebenen Arbeit an der Schnittstelle von Technologie, Strategie und Geschaeft.",
            "Ich arbeite sicher in Python, LangGraph und RAG Architekturen und habe Freude daran, KI Loesungen von der ersten Idee bis zur produktiven Anwendung zu begleiten. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend, ich hebe es aktiv weiter, und Englisch spreche ich fliessend. Ich kann als Werkstudent in Muenchen flexibel einsteigen. Gerne bespreche ich meinen Beitrag zu Ihrem AI und LLM Engineering Team in einem persoenlichen Gespraech.",
        ],
    },

    # 4. Merantix Momentum, Berlin
    # Working Student AI Full Stack Engineer (m/f/d)
    # Merantix AI Campus job board (company career page), EN track
    # Tasks: contributing to the development of AI powered applications
    # in a Full Stack team, real production code, building interfaces and
    # backend systems that bring machine learning to life.
    # Apply: https://careers.merantix-aicampus.com/companies/merantix-momentum-2/jobs/81860735-working-student-ai-full-stack-engineer-m-f-d
    # Apply method: company-portal (Merantix AI Campus careers site, not a platform-native aggregator flow)
    {
        "folder": "Merantix Momentum Berlin Working Student AI Full Stack Engineer",
        "company": "Merantix Momentum",
        "lang": "en",
        "tag": "Master's Student Data Science and Analytics | AI Powered Applications and Full Stack Engineering | Python + React + LangGraph",
        "role_strip": "Working Student, AI Full Stack Engineer",
        "cl_date": "7 September 2026",
        "cl_subject": "Working Student, AI Full Stack Engineer in Berlin",
        "profile": "Master's student in Data Science and Analytics at SRH Heidelberg, based in Mannheim, with hands on experience building AI powered applications end to end, from the model and evaluation layer through to a working interface. I built a multi agent RAG system with an LLM as Judge evaluation harness running locally on Ollama, and a fully automated cloud native pipeline that closes with a Looker Studio dashboard. Two years of full time production React experience inside a module federation setup gives me the front end and backend fluency to ship real, user facing features rather than notebook demos.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_RAG_EN, P_MOVIE_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_NVIDIA, CERT_AWS, CERT_GOOGLE],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am writing to apply for the Working Student AI Full Stack Engineer position at Merantix Momentum in Berlin. As a Master's student in Data Science and Analytics at SRH Heidelberg based in Mannheim, the description of contributing real production code to AI powered applications, working alongside senior engineers on the interfaces and backend systems that bring machine learning to life, maps closely to the projects I have shipped and the production React background I bring from two years of full time front end work.",
            "In my Multi Agent RAG project I built a LangGraph orchestrated agent system end to end, from a hybrid BM25 plus dense retrieval layer through to a JudgeAgent that scores answers on 5 dimensions in JSON mode, with a hard failure if the independent judge model is missing so a silent fallback can never regress unnoticed. This is the same discipline the role asks for, building AI features that are trustworthy in production, not just a working demo, and evaluating them systematically rather than by eye.",
            "In my Movie Analytics and ML Pipeline project I built a fully automated cloud native pipeline running on a Cloud Scheduler trigger with 0 manual interventions, closing with a Looker Studio dashboard that answers concrete business questions. Alongside that, two years as a full time front end engineer at SS Engineers and Contractors, including porting around 8 routes from a legacy AngularJS app to React inside a live module federation shell with 0 production incidents, gives me real experience shipping user facing interfaces on top of a working data or ML backend, exactly the kind of full stack delivery the role describes.",
            "I work comfortably across Python, LangGraph, React, and the cloud platforms AWS and GCP. I hold the NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations and Google Data Analytics certificates and was recognised as a Finalist of the USAII Global AI Hackathon 2026 at Graduate Level. I am fluent in English and my German is at B1, in progress. I can join as a working student in Berlin. I would welcome the chance to discuss how I could contribute to your Full Stack team.",
        ],
    },
]
