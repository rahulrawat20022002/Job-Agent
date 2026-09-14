"""English translation of the Hirschmann Automation and Control GmbH
Masterarbeit Agentic Pentesting CV, for Rah's interview prep only (interview
15 Sep 2026). NOT a new application: the original submission was DE track
per the 20 July 2026 language match rule (posting title and body were German
on StepStone). This EN version renders the same facts, same project
selection (Multi Agent RAG + CreditIQ, per the 2 Sep 2026 conversion note),
same eRay experience entry, same certifications, translated to English so
Rah has an English copy to review before the interview.

Patterned on role_configs_08aug.py's Hirschmann DE entry (entry 2), translated
by hand from the same facts, not filed as part of any scheduled drafting run,
no Notion or CSV write associated with this file.
"""

from role_configs import (
    ERAY_BULLETS_EN,
    DIABETES_BULLETS_EN,
    CERT_NVIDIA,
    CERT_AWS,
    CERT_GOOGLE,
    ACH_USAII_EN,
    P_RAG_EN,
    P_CREDITIQ_EN,
)

CONFIGS_HIRSCHMANN_EN = [
    {
        "folder": "Hirschmann Automation Masterarbeit Agentic Pentesting KI Agent Neckartenzlingen EN",
        "company": "Hirschmann Automation and Control GmbH",
        "lang": "en",
        "role_strip": "Master Thesis Agentic Pentesting and AI Agents for Pentest Workflows",
        "cl_date": "8 August 2026",
        "cl_subject": "Master Thesis Agentic Pentesting: Development and Evaluation of an AI Agent to Automate Pentest Workflows in Neckartenzlingen",
        "profile": "Data Science and Analytics Master student at SRH Heidelberg based in Mannheim with hands on practice in AI agents, Retrieval Augmented Generation and LLM orchestration. I built a Hybrid RAG Orchestrator with agentic routing on top of Llama 3.1 8b via Groq and LangChain, delivered a Fairness by Design credit scoring system with honest evaluation aligned to the EU AI Act, and shipped an end to end time series pipeline at eRay GmbH with gate checks and governance rules. Comfortable in Python, LangChain, Git and API based LLM services, with a clear eye for evaluation, guardrails and traceable agent behaviour.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_RAG_EN, P_CREDITIQ_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_NVIDIA, CERT_AWS, CERT_GOOGLE],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am writing to apply for the Master Thesis Agentic Pentesting position at Hirschmann Automation and Control in Neckartenzlingen. The posting, developing and evaluating an AI agent to automate pentest workflows, aligns closely with the systems I have been building over the past months.",
            "In my Hybrid RAG Orchestrator I built a custom decision making router on top of Llama 3.1 8b via Groq and LangChain that classifies user intent into three execution paths, local knowledge retrieval, external web search, or direct conversational logic. A stateful MemoryAgent keeps multi turn context intact over ChromaDB and HuggingFace embeddings, and the whole system ships as a deployed Streamlit prototype end to end. That is the same shape of work I would bring to developing your pentest agent, agent definition, routing, guardrails and traceable behaviour.",
            "In CreditIQ I delivered a Fairness by Design pipeline that raised the Disparate Impact ratio from a failing 0.79 to a compliant 0.88, brought the false negative rate down from 44 percent to 16.7 percent while accuracy held at 75 percent, and backed the pipeline with unit tests at 100 percent branch coverage. At eRay GmbH I benchmarked six models head to head, enforced strict anti leakage rules and wrapped the pipeline in a governance orchestrator with gate checks so a failed imputation halts the run rather than corrupting downstream predictions. My Bachelor thesis compares six classifiers with 10 fold cross validation and was written up as an IEEE style paper with an honest limitations section.",
            "I work confidently in Python, Git and API based LLM services such as OpenAI and Groq, document methods and results for team hand off, and can move complex problems into structured proofs of concept. My German level is B1 in progress and English is my working language. I hold the NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations and Google Data Analytics Foundations certificates, and was recognised as a Finalist at Graduate Level in the USAII Global AI Hackathon 2026. I would welcome the chance to discuss my contribution with your team in Neckartenzlingen.",
        ],
    },
]
