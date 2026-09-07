"""Ad-hoc role configuration for Rah's direct request on 6 September 2026:
Rohde und Schwarz, Werkstudent Agentic AI Experiments, Teisnach.

Posting fetched via tavily_extract (direct WebFetch to rohde-schwarz.com
was blocked by this sandbox's egress proxy). Posting is entirely in
German, so this ships DE track per the 20 July 2026 language match rule.

Role details from the posting:
  - Title: Werkstudent (m/w/d) Agentic AI Experiments
  - Location: Teisnach (Deutschland), Bavarian Forest manufacturing site
  - Level: Werkstudent*innen, Teilzeit, befristet, Ref. 2086
  - Tasks: experimental/prototype solutions in Agentic AI, automation and
    intelligent workflows; identifying use cases where AI agents/bots/
    automation add value; integrating and linking data from different
    sources; supporting prototypes, dashboards, evaluations and other
    digital support tools; developing workflows with tools like n8n;
    testing/evaluating/iterating new technical approaches in AI and
    automation; documenting experiments, results and learnings;
    collaborating with stakeholders to turn ideas into practical solutions.
  - Requirements: studies in Applied Computer Science, Wirtschafts-
    informatik, engineering or comparable; strong interest in AI,
    automation, agent systems and digital tools; first practical
    experience with scripting, APIs, data processing or software
    development; ideally first touchpoints with n8n, workflow automation,
    low-code/no-code platforms; teamwork and communication skills; very
    good German and English, written and spoken.
  - Apply: https://job.rohde-schwarz.com/default/content/apply/?extJobId=2086-de_DE&locale=de_DE
  - Apply method: company-portal (Rohde und Schwarz's own careers portal,
    job.rohde-schwarz.com, not a LinkedIn/Xing/StepStone/Indeed aggregator
    flow), out of OpenClaw's platform-native automated scope; Rah applies
    manually.

Dedup check: an existing CSV/Notion row for "Rohde und Schwarz GmbH und Co.
KG" already exists (Werkstudent, Data Analytics und Data Science,
Memmingen, Status: Not listed Anymore). This is a different role at a
different site (Teisnach vs Memmingen), so it is a new row, not a
duplicate, under the "different roles at the same company" rule.

Projects selected: Multi Agent RAG with LLM as Judge (agentic AI, LangGraph
multi agent orchestration, iterative evaluation and documentation of
results) and Movie Analytics and ML Pipeline (a fully automated,
0-manual-intervention Cloud Scheduler pipeline plus a Looker Studio
dashboard, the closest existing project to n8n-style workflow automation
and dashboard/reporting work).

19 August 2026 CV content rules apply: no hyphens or dashes in CV text,
no parentheses or brackets in bullets, Languages EN and DE only, German
level locked to "Deutsch: B1, laufend," no page numbers/headers/footers,
2 page hard cap, Ojas style header, Skills grouped into functional
buckets, positioning tag under the name is a pitch not the posting title.
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


CONFIGS_06SEP_RS = [
    # Rohde und Schwarz GmbH und Co. KG, Teisnach
    # Werkstudent (m/w/d) Agentic AI Experiments
    # Company career page (rohde-schwarz.com), Teilzeit befristet, DE track
    # Apply: https://job.rohde-schwarz.com/default/content/apply/?extJobId=2086-de_DE&locale=de_DE
    # Apply method: company-portal (Rohde und Schwarz careers portal)
    {
        "folder": "Rohde Schwarz Teisnach Werkstudent Agentic AI Experiments",
        "company": "Rohde und Schwarz GmbH und Co. KG",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | Agentische KI Experimente und Workflow Automatisierung | Python + LangGraph + Automatisierung",
        "role_strip": "Werkstudent, Agentic AI Experiments",
        "cl_date": "6. September 2026",
        "cl_subject": "Werkstudent Agentic AI Experiments in Teisnach",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Bau experimenteller Agentic AI Loesungen und automatisierter Workflows. Ich habe ein Multi Agent RAG System mit LangGraph orchestriert, dessen Komponenten ich systematisch getestet, evaluiert und iteriert habe, und in einem Cloud Data Projekt eine vollstaendig automatisierte Batch Pipeline mit 0 manuellen Eingriffen sowie ein zugehoeriges Dashboard gebaut. Sicher in Python, APIs, Datenverarbeitung und der Dokumentation technischer Experimente und Ergebnisse.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_MOVIE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit Agentic AI Experiments bei Rohde und Schwarz in Teisnach. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim passt die in der Ausschreibung beschriebene Mitarbeit an experimentellen und prototypischen Loesungen im Bereich Agentic AI, Automatisierung und intelligente Workflows sehr genau zu dem, was ich in den letzten Monaten praktisch aufgebaut habe.",
            "In meinem Multi Agent RAG Projekt habe ich ein LangGraph orchestriertes Agentensystem gebaut und dabei systematisch Anwendungsfaelle identifiziert, an denen ein zusaetzlicher Agent echten Mehrwert schafft, etwa ein LanguageAgent, der die Ausgabesprache fuer jeden nachgelagerten Agenten zentral festlegt, und ein JudgeAgent, der Antworten automatisiert bewertet. Jede Komponente wurde getestet, evaluiert und iteriert, bevor sie in die naechste Version einfloss, und die Ergebnisse wurden durchgehend in JSON und Markdown Reports dokumentiert. Genau diese Arbeitsweise, neue technische Ansaetze im Bereich KI Agenten zu testen und die Learnings festzuhalten, deckt sich mit der in der Ausschreibung beschriebenen Aufgabe.",
            "In meinem Movie Analytics und ML Pipeline Projekt habe ich eine Batch Pipeline gebaut, die vollstaendig automatisiert ueber einen Cloud Scheduler Trigger mit 0 manuellen Eingriffen laeuft und Daten aus einer oeffentlichen API mit mehreren internen Quellen zusammenfuehrt, sowie ein Looker Studio Dashboard, das die Ergebnisse fuer Stakeholder aufbereitet. Diese Erfahrung, wiederkehrende Arbeit in verlaessliche automatisierte Workflows zu ueberfuehren und die Ergebnisse in einem Dashboard sichtbar zu machen, laesst sich direkt auf den Aufbau von Workflows mit Tools wie n8n sowie auf Prototypen und Auswertungen uebertragen, auch wenn ich mit n8n selbst noch keine praktische Erfahrung habe.",
            "Ich arbeite sicher in Python, mit APIs und Datenverarbeitung, und dokumentiere meine Experimente durchgehend. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend, ich hebe es aktiv weiter, und Englisch spreche ich fliessend. Mir ist bewusst, dass die Ausschreibung sehr gute Deutsch und Englischkenntnisse in Wort und Schrift nennt, ein Niveau, das ich im Deutschen noch nicht ganz erreiche, und moechte an dieser Stelle offen damit umgehen. Gerne bespreche ich meinen Beitrag zu Ihrem Team in einem persoenlichen Gespraech.",
        ],
    },
]
