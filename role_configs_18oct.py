"""Role configurations for the 18 October 2026 scheduled job search run
(Notion backlog 10 drafted, 8 to 10 zone of the 28 July 2026 gate, so the
cut is capped at top 3).

Reconciliation: the 17 October run branch (unmerged, merged into this
branch) already corrected 7 CSV rows to match Notion. Notion holds 10
drafted rows now, the CSV only 3; 7 Notion drafted rows have no CSV row
and no draft folder on this branch, left for Rah to decide as flagged in
the 17 October digest.

Search ran via Tavily and WebFetch. Xing's own domain refused WebFetch.
LinkedIn returned HTTP 429 on one fetch. Indeed MCP not available.

Three roles cleared verification:
  1. Iits, remote Germany, Working Student AI Engineer LLMs and AI Agents,
     DE track, company portal (Personio), posted yesterday per Remotive.
  2. Infineon Technologies, Munich, Working Student Generative AI and
     Agent Engineering, EN track, LinkedIn listing posted 4 days ago.
     No Easy Apply button visible, so Apply Method is company-portal as
     the safe default.
  3. Handelsblatt Media Group, Duesseldorf, Werkstudent KI Entwicklung,
     DE track, apply through the finest-jobs.com aggregator form. The
     posting asks for very good German (C1), a real gap against B1 in
     progress; disclosed honestly in the cover letter.

19 August 2026 CV content rules apply to every field below.
"""

from role_configs import (
    ERAY_BULLETS_EN,
    ERAY_BULLETS_DE,
    DIABETES_BULLETS_EN,
    DIABETES_BULLETS_DE,
    CERT_NVIDIA,
    CERT_AWS,
    CERT_GOOGLE,
    CERT_NVIDIA_DE,
    CERT_AWS_DE,
    CERT_GOOGLE_DE,
    ACH_USAII_EN,
    ACH_USAII_DE,
    P_RAG_EN,
    P_RAG_DE,
    P_CREDITIQ_EN,
    P_CREDITIQ_DE,
)


CONFIGS_18OCT = [
    # 1. Iits, remote Germany
    {
        "folder": "Iits Remote Werkstudent AI Engineer LLMs und KI Agenten",
        "company": "Iits",
        "lang": "de",
        "location": "Remote, Deutschland",
        "apply_link": "https://iits.jobs.personio.com/job/2396923",
        "apply_method": "company-portal",
        "source": "Company Page",
        "german_level": "B2",
        "tag": "Masterstudent Data Science and Analytics | LLM Agenten und RAG Evaluation | Python + LangGraph + Pinecone",
        "role_strip": "Werkstudent, AI Engineer LLMs und KI Agenten",
        "cl_date": "18. Oktober 2026",
        "cl_subject": "Werkstudent AI Engineer LLMs und KI Agenten, remote",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Bau agentischer LLM Systeme mit LangGraph, RAG und Tool Calling. Ich habe ein Multi Agenten RAG System mit einem unabhaengigen LLM as Judge Modell gebaut, das Antworten auf 5 Dimensionen bewertet, sowie ein regulatorisch abgesichertes Kreditscoring System mit einer LLM generierten Erklaerung. Sicher in Python und darin, Prototypen in getestete, wartbare Software zu ueberfuehren.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_CREDITIQ_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich als Werkstudent AI Engineer fuer LLMs und KI Agenten bei Iits, remote aus Deutschland. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim passt die Aufgabe, spezialisierte LLM Agenten mit Tool Calling und RAG zu entwickeln und ihre Qualitaet zu bewerten, sehr genau zu dem, was ich in den letzten Monaten gebaut habe.",
            "In meinem Multi Agent RAG Projekt habe ich mit LangGraph ein Agentensystem mit einem LanguageAgent, einem JudgeAgent und eigenen Retrieval Agenten entworfen, mit einem gemeinsamen Pinecone Index. Der JudgeAgent bewertet Antworten auf 5 Dimensionen im JSON Modus bei Temperatur 0 und laeuft auf einem anderen lokalen Modell als der Generator, damit keine Selbstbevorzugung entsteht. Genau diese Verbindung aus agentischem Workflow und systematischer Qualitaetsbewertung nennt Ihre Ausschreibung.",
            "In meinem CreditIQ Projekt habe ich ein Scoring System mit AIF360 Fairness Korrektur, getesteten Pipelines mit 100 Prozent Branch Coverage und einem Streamlit Tool mit LLM generierter Erklaerung bis zur Auslieferung gebracht. Diese Erfahrung, einen Prototypen in robuste, getestete und wartbare Software zu ueberfuehren, uebertraegt sich direkt auf Ihre internen KI Automationen und Kundenprojekte.",
            "Ich arbeite sicher in Python, mit LangGraph, RAG und der Integration von Sprachmodellen ueber APIs. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Ehrlicherweise liegt mein Deutsch bei B1 laufend und damit unter dem von Ihnen genannten B2 Niveau. Ich arbeite aktiv daran, und Englisch spreche ich fliessend. Ich stelle mich gerne in einem persoenlichen Gespraech vor.",
        ],
    },

    # 2. Infineon Technologies, Munich
    {
        "folder": "Infineon Munich Working Student Generative AI Agent Engineering",
        "company": "Infineon Technologies",
        "lang": "en",
        "location": "Munich",
        "apply_link": "https://de.linkedin.com/jobs/view/working-student-%E2%80%93-generative-ai-agent-engineering-f-m-div-at-infineon-technologies-4479038477",
        "apply_method": "company-portal",
        "source": "LinkedIn",
        "german_level": "none",
        "tag": "Master's Student Data Science and Analytics | AI Agents and LLM Evaluation | Python + LangGraph + Prompt Engineering",
        "role_strip": "Working Student, Generative AI and Agent Engineering",
        "cl_date": "18 October 2026",
        "cl_subject": "Working Student Generative AI and Agent Engineering in Munich",
        "profile": "Master's student in Data Science and Analytics at SRH Heidelberg, based in Mannheim, with hands on experience building, configuring, and evaluating LLM agents. I built a LangGraph multi agent RAG system with an independent LLM as Judge model scoring answers across 5 dimensions, and a regulated credit scoring system with a plain language LLM explanation. Comfortable in Python, prompt and workflow customisation, and judging which AI use cases deliver measurable value.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_RAG_EN, P_CREDITIQ_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_NVIDIA, CERT_AWS, CERT_GOOGLE],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am writing to apply for the Working Student Generative AI and Agent Engineering position at Infineon Technologies in Munich. As a Master's student in Data Science and Analytics at SRH Heidelberg based in Mannheim, analysing AI agents and frameworks, adapting them to business and engineering use cases, and customising prompts, workflows, and tools to improve agent performance maps closely to what I have built over the last several months.",
            "In my Multi Agent RAG project I designed a LangGraph agent system with a LanguageAgent, a JudgeAgent, and dedicated retrieval agents. The JudgeAgent scores answers on 5 dimensions in JSON mode at temperature 0 and runs on a different local model from the generator to remove self preference bias. That experience judging agent capabilities and limits with measurable scores, rather than by impression, is what evaluating and prioritising use cases with measurable business value requires.",
            "In my CreditIQ project I applied AIF360 mitigation to a credit scoring model, backed the pipeline with unit tests at 100 percent branch coverage, and shipped a Streamlit tool with a plain language LLM explanation and a full regulatory write up. That experience adapting AI to a demanding quality and compliance setting transfers directly to configuring agents for the Quality organization.",
            "I work comfortably in Python, with prompt engineering, LLM workflows, and APIs. I hold the NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations, and Google Data Analytics certificates, and was recognised as a Finalist of the USAII Global AI Hackathon 2026 at Graduate Level. I am fluent in English and B1 in progress in German. I am enrolled in a Master's programme, can commute to Munich, and can provide my enrollment certificate and transcript. I would welcome the chance to discuss how I could contribute.",
        ],
    },

    # 3. Handelsblatt Media Group, Duesseldorf
    {
        "folder": "Handelsblatt Media Group Duesseldorf Werkstudent KI Entwicklung",
        "company": "Handelsblatt Media Group",
        "lang": "de",
        "location": "Duesseldorf",
        "apply_link": "https://www.finest-jobs.com/bewerbung/werkstudentin-ki-entwicklung-gn-schwerpunkt-python-1324674",
        "apply_method": "company-portal",
        "source": "Other",
        "german_level": "C1",
        "tag": "Masterstudent Data Science and Analytics | LLM Anwendungen und RAG | Python + LangGraph + Pinecone",
        "role_strip": "Werkstudent, KI Entwicklung Schwerpunkt Python und AI Applications",
        "cl_date": "18. Oktober 2026",
        "cl_subject": "Werkstudent KI Entwicklung, Schwerpunkt Python und AI Applications",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung in Python Backends fuer LLM Anwendungen, agentischer KI, RAG und Embeddings. Ich habe ein Multi Agenten RAG System mit Pinecone Vektorindex und einem unabhaengigen LLM as Judge Modell gebaut sowie ein getestetes Scoring System mit Streamlit Oberflaeche. Sicher in Python, Git und darin, neue Funktionen sauber zu testen und zu dokumentieren.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_CREDITIQ_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich als Werkstudent KI Entwicklung mit Schwerpunkt Python und AI Applications bei der Handelsblatt Media Group in Duesseldorf. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim passt die Arbeit an LLM basierten Anwendungen, agentischer KI, Retrieval Augmented Generation und Embeddings sehr genau zu dem, was ich in den letzten Monaten gebaut habe.",
            "In meinem Multi Agent RAG Projekt habe ich mit LangGraph ein Agentensystem mit eigenen Retrieval Agenten und einem gemeinsamen Pinecone Vektorindex entworfen. Ein JudgeAgent bewertet die Antworten auf 5 Dimensionen und laeuft auf einem anderen Modell als der Generator. Diese Erfahrung mit Backend Logik, Embeddings und Wissenssystemen entspricht den Aufgaben Ihres KI Teams.",
            "In meinem CreditIQ Projekt habe ich ein Scoring System mit Unit Tests bei 100 Prozent Branch Coverage und einer Streamlit Oberflaeche ausgeliefert und technisch dokumentiert. Das Testen, Absichern und Dokumentieren neuer Funktionen ist fuer mich Standard, ebenso das Arbeiten mit Git.",
            "Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Ehrlicherweise liegt mein Deutsch bei B1 laufend und damit unter dem in Ihrer Ausschreibung genannten C1 Niveau. Ich arbeite aktiv daran, und Englisch spreche ich fliessend. Ich kann ab sofort starten und stelle mich gerne in einem persoenlichen Gespraech vor.",
        ],
    },
]
