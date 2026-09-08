"""Role configurations for the 8 September 2026 scheduled job search run.

Backlog gate check per 14 July 2026 status source of truth rule: Notion
data source fd974369-40b2-48c5-b660-d15256c88f52 returned 0 rows in status
'drafted' at run start. 0 drafted falls well under the 8 row floor of the
28 July 2026 yield based reset rule, which allows a normal top 3 to 5 cut.

Reconciliation this run found 10 CSV rows still marked with a stale status
relative to Notion (Fraunhofer IOSB Karlsruhe Abschlussarbeit Training
Data Anonymization and Kaufland Praktikant Data Science had drifted to
'rejected' in Notion while the CSV still read 'applied'; Mercedes-Benz
Tech Innovation Werkstudent Machine Learning Engineering, Generali
Deutschland AG, EXXETA, Merantix Momentum, Mi-Jack Europe GmbH, appliedAI
Initiative GmbH, and Rohde und Schwarz GmbH und Co. KG Teisnach had
drifted to 'applied' in Notion while the CSV still read 'drafted';
KontextWork GbR had moved to 'Not listed Anymore' in Notion while the CSV
still read 'drafted'); the CSV was corrected to match Notion in all 10
cases, no reverse writes.

This run's search proved unusually difficult: the large majority of
individual job postings surfaced by Tavily search for AI Engineer and AI
Evaluation flavoured roles had already expired (StepStone and Xing both
returned "page not found" or "this job ad isn't available" on direct
fetch, even for postings whose search snippet looked fresh), including
wingmaite GmbH Werkstudent AI Quality Engineering Munich, KHS GmbH
Working Student GenAI Evaluation and Testing Dortmund, AOE GmbH Working
Student GenAI/LLM Prototyping Wiesbaden/Remote, CognitX AI GmbH AI/LLM
Engineering Werkstudent (confirmed archived 3 months ago), NXP
Semiconductors Working Student AI/ML Solutions Hamburg, and SAP Working
Student AI Engineering & Data Science Walldorf (404 on the SAP careers
domain). Several other candidates were confirmed live but excluded for
other reasons documented in the digest: retorio GmbH's Working Student AI
Engineer, Agentic Systems posting in Munich is a strong scope match and
verified live and Verifiziert on StepStone, but it duplicates a company
plus role pair already tracked in Notion under status 'Not listed
Anymore', so it was flagged as a probable relist for Rah's manual review
rather than auto redrafted, to avoid a conflicting duplicate row. Daimler
Truck AG's Werkstudent Global AI Enablement & Agentic AI Campaign posting
in Leinfelden-Echterdingen is confirmed live but reads, on the full job
description, as an AI learning, communications, and change management
role (campaign management, community formats, learning portfolio
development) rather than an AI Engineer or AI Evaluation role, so it was
dropped under the 26 August 2026 scope narrowing despite the Agentic AI
wording in the title. Mercedes-Benz Tech Innovation's Working Student AI
Agents & Robotics Platform posting in Ulm/Stuttgart/Karlsruhe, HMS
Analytical Software GmbH's Werkstudent Software Development, Data & AI in
Heidelberg/Berlin/Ulm, and several AKDB/Rosenberger/Cinemo postings
surfaced again this run but all duplicate company plus role pairs already
logged in the CSV and Notion, so none were redrafted.

Platform mix this run:
  - StepStone (Estateanfrage Inh. Fabian Kroner), 1
  - Xing, LinkedIn, JobTeaser, and Indeed were all searched this run
    (LinkedIn and JobTeaser via Tavily search, Indeed via Tavily search
    since no Indeed MCP tool was available in this session) but yielded
    only postings already logged, expired listings, off scope roles, or
    a confirmed duplicate relist; none used this run.

Freshness: Estateanfrage's StepStone listing showed "Erschienen: vor 3
Tagen" (posted 3 days ago) at search time and was independently confirmed
live via a follow up fetch immediately before drafting.

Language track per 20 July 2026 language match hard rule (posting body
language IS deliverable language): the Estateanfrage posting body
(Aufgaben, Ihr Profil, Benefits) is written entirely in German, so this
role ships DE track.

Language level transparency: the Estateanfrage posting asks for "Sehr
gute Kommunikationsfaehigkeiten in Wort und Schrift auf Deutsch" (very
good spoken and written German), noticeably above Rah's current B1 in
progress level. Per the standing rule, language level does not filter
listings; this gap is flagged plainly in the digest for Rah's awareness
rather than silently dropped or silently upgraded on the CV.

Apply method transparency: Estateanfrage's Apply Link is a stepstone.de
hosted listing with an "Ich bin interessiert" button, StepStone's own
apply flow for this posting (no external company career site detected),
recorded as platform-native and in OpenClaw's automated scope.

Dedup check against applied-log.csv and Notion: Estateanfrage Inh. Fabian
Kroner is an entirely new company, never previously logged.

19 August 2026 CV content rules apply: no hyphens or dashes in CV text,
no parentheses or brackets in bullets, Languages EN and DE only, German
level locked to "Deutsch: B1, laufend" or "German: B1, in progress" on
the respective track, no page numbers or headers or footers, 2 page hard
cap, Ojas style header, Skills grouped into functional buckets,
positioning tag under the name is a pitch not the posting title, and
banned strings on the validation gate are met by the new header.
"""

from role_configs import (
    ERAY_BULLETS_DE,
    DIABETES_BULLETS_DE,
    CERT_NVIDIA_DE,
    CERT_AWS_DE,
    CERT_GOOGLE_DE,
    ACH_USAII_DE,
    P_RAG_DE,
    P_MOVIE_DE,
)


CONFIGS_08SEP = [
    # 1. Estateanfrage Inh. Fabian Kroner, Muenchen
    # Werkstudent AI Engineer (m/w/d)
    # StepStone, DE track
    # Tasks: analysing existing business processes and finding
    # automation potential, supporting the implementation and
    # optimisation of AI supported workflows, building simple
    # automations with modern AI and no code tools, testing, evaluating
    # and comparing new AI tools and technologies, documenting and
    # continuously improving existing processes, developing prompts and
    # workflows for efficient use of AI systems.
    # Requirements: enrolled student in computer science, business
    # informatics, data science, AI, business administration or
    # comparable; interest in AI, automation and digital technologies;
    # first experience with AI tools such as ChatGPT, Claude or Gemini;
    # very good written and spoken German.
    # Apply: https://www.stepstone.de/stellenangebote--Werkstudent-AI-Engineer-m-w-d-at-estateanfrage-de-%E2%80%A2-Muenchen-Bayern-Deutschland-Muenchen-Estateanfrage-Inh-Fabian-Kroner--14239536-inline.html
    # Apply method: platform-native (StepStone "Ich bin interessiert" apply flow)
    {
        "folder": "Estateanfrage Muenchen Werkstudent AI Engineer",
        "company": "Estateanfrage Inh. Fabian Kroner",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | KI Automatisierung und Tool Evaluation | Python + LangGraph + Prompt Engineering",
        "role_strip": "Werkstudent AI Engineer",
        "cl_date": "8. September 2026",
        "cl_subject": "Werkstudent AI Engineer in Muenchen",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Testen, Vergleichen und produktiven Einsatz moderner KI Tools. Ich habe ein Multi Agent RAG System gebaut, in dem ein unabhaengiges LLM as Judge Modell die Ausgaben eines anderen Modells systematisch bewertet, und eine vollautomatisierte Cloud Pipeline ohne manuelle Eingriffe betrieben. Sicher im Prompt Engineering, im strukturierten Vergleich verschiedener KI Modelle und im Aufbau einfacher Automatisierungen mit echtem Mehrwert.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_MOVIE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit AI Engineer bei Estateanfrage am Standort Muenchen. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim passt die in der Ausschreibung beschriebene Aufgabe, bestehende Geschaeftsprozesse zu analysieren, KI gestuetzte Workflows zu optimieren und neue AI Tools zu testen und zu vergleichen, sehr genau zu dem, was ich in den letzten Monaten praktisch gebaut habe.",
            "In meinem Multi Agent RAG Projekt habe ich verschiedene lokale Modelle gezielt gegeneinander eingesetzt, Mistral 7B als Generator und Qwen2.5 14B als unabhaengigen LLM as Judge, um Antworten strukturiert auf 5 Dimensionen zu bewerten statt sie von Hand zu pruefen, und dabei intensiv mit Prompt Engineering fuer konsistente, auswertbare Ausgaben gearbeitet. Diese Erfahrung, KI Tools systematisch zu testen, zu vergleichen und ueber Prompts auf ein Ziel hin zu steuern, deckt sich direkt mit der in der Ausschreibung beschriebenen Aufgabe.",
            "In meinem Movie Analytics und ML Pipeline Projekt habe ich eine vollautomatisierte Batch Pipeline gebaut, die ueber einen Cloud Scheduler Trigger ohne jede manuelle Eingriffe laeuft. Diese Erfahrung, wiederkehrende Arbeit sauber zu automatisieren und die entstehenden Automatisierungen nachvollziehbar zu dokumentieren, uebertraegt sich direkt auf den Aufbau einfacher Automatisierungen mit modernen AI und No Code Tools.",
            "Ich arbeite aktiv mit KI Tools wie ChatGPT, Claude und Gemini, habe eine loesungsorientierte und analytische Denkweise und dokumentiere meine Arbeit gerne nachvollziehbar. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend, ich hebe es aktiv weiter, und Englisch spreche ich fliessend. Ich kann als Werkstudent in Muenchen flexibel einsteigen. Gerne bespreche ich meinen Beitrag zu Ihrem Team in einem persoenlichen Gespraech.",
        ],
    },
]
