"""Role configurations for the 22 September 2026 scheduled job search run
(normal top 3 to 5 cut).

Backlog gate check per 14 July 2026 status source of truth rule: Notion
data source fd974369-40b2-48c5-b660-d15256c88f52 returned 2 rows in status
'drafted' at run start (both Syneco Trading GmbH, same Masterarbeit role,
one via Xing already fully rendered, one a company-portal duplicate row
Rah created directly on 21 Sep while already on the application upload
page, that never got its 8 deliverables rendered or a CSV row). 2 drafted
falls well under the 8 row floor of the 28 July 2026 yield based reset
rule, which allows a normal top 3 to 5 cut.

Reconciliation this run compared all 215 CSV rows against all 211 valid
Notion rows (one blank placeholder row, "New CVs now", excluded as not a
real job row) and found 14 drift rows where Notion had moved past
'drafted' (mostly to 'Not listed Anymore', two to 'applied', two to
'rejected') while the CSV still said 'drafted' or an older status; all 14
were corrected in the CSV to match Notion per invariant #1. One apparent
mismatch (Aerzteverband Deutscher Allergologen with and without the
umlaut) is a spelling variant only, both sides already read 'applied', no
action needed.

Housekeeping fix, not a search find: the Syneco Trading GmbH company-portal
row (Notion page created 2026-09-21 22:16, Draft Path "drafts/Syneco
Trading Thuga Masterarbeit Agentic AI Generative AI Energiewirtschaft
Muenchen/") had no CSV counterpart and no files anywhere in the repo. This
is the exact false-drafted risk invariant #3 warns about: Notion says
drafted, but nothing backs it. Since it is the identical company and role
already fully tailored for the Xing version (see role_configs_16sep.py
entry 1), this run renders its real 8 deliverables into that exact folder
and adds the matching CSV row rather than leaving the gap or fabricating a
status. Cover letter content is reused near verbatim from the Xing version
since it never named the Xing platform in the first place.

Search ran via WebSearch and WebFetch across StepStone, Xing, LinkedIn,
JobTeaser and company career pages (Tavily MCP failed to connect again
this run, consistent with prior runs; no Indeed MCP tool was available in
this session either, so Indeed was not used). Xing's own domain did not
surface distinct results through WebSearch (queries kept resolving back to
StepStone mirrors), a repeat of the pattern noted in the 16 Sep digest, so
Xing is flagged unreachable in its own right this run even though
StepStone coverage is strong. Company career pages were fetched directly
wherever a lead named a specific employer.

Several leads were found and dropped:
  - Ponturo Consulting AG Werkstudent AI Engineer (multiple cities): the
    listing surfaced via a third party mirror (studysmarter, now 410
    Gone) but the company's own careers page (ponturo.com/de/karriere/
    studenten) shows zero open student positions, so this could not be
    verified as currently live and was dropped under invariant #4 (every
    write must be auditable).
  - Jemix GmbH Werkstudent AI Engineer, Berlin: same pattern, a StepStone
    listing exists but the company's own careers page (jemix.de/de/
    karriere/) does not list any AI Engineer or AI agent role among its
    current openings, only Werkstudent IT and Digital Recruiting. Dropped
    as unverifiable.
  - Klugsys Werkstudent Agentic AI Engineer, Aachen: a LinkedIn listing
    surfaced but the company's own careers page (klugsys.com/en/career)
    lists only full time roles (Senior ML Engineer, AI Voice Agent
    Engineer, Full Stack Engineer, Automotive AI Specialist) and states no
    intern or working student roles are currently open. Dropped as
    unverifiable and out of scope on work type.
  - itdesign Werkstudent AI Engineer: the karriere.itdesign.de listing
    URL returned 404, dropped as no longer live.
  - Helmholtz Munich Agentic AI Research Engineer, Munich: real and live
    on jobteaser.com, but the role requires a PhD or MSc with substantial
    professional experience for a full time research position, outside
    the Werkstudent / Pflichtpraktikum / Masterarbeit work type scope in
    master-projects.md. Dropped as out of scope.
  - Retorio GmbH Working Student AI Engineer Agentic Systems (Munich) and
    Mercedes-Benz Tech Innovation Werkstudent AI Agents and Robotics
    Platform (Ulm/Stuttgart/Karlsruhe) both resurfaced in this run's
    search but duplicate rows already logged in Notion ('Not listed
    Anymore' and 'rejected' respectively), so both were dropped as
    duplicates under the standing company plus role case insensitive
    dedup rule.

Three roles cleared verification: a live posting fetched directly (or,
for BLACKFIELD AI, a direct fetch of the company's own job page), a
confirmed apply path, and a clean dedup check against applied-log.csv and
Notion (215 CSV rows, 211 Notion rows at run start).

Platform mix this run (new finds only, Syneco Thuga fix excluded since it
duplicates an already counted Xing find from 16 Sep):
  - Company Page, 2 (BLACKFIELD AI Bremen, email application; Web
    Computing GmbH Muenster, online form application)
  - LinkedIn, 1 (Modern Drive Technology GmbH, Neumarkt in der Oberpfalz,
    LinkedIn Easy Apply, platform-native)
  - StepStone and Xing surfaced no new in-scope, verifiable, non-duplicate
    postings this run beyond the leads listed as dropped above.
  - JobTeaser surfaced only the out-of-scope Helmholtz Munich lead dropped
    above.
  - Indeed not used (no MCP tool available this session, consistent with
    prior runs).

Freshness order (all four fall in the single Germany tier, ranked by
recency then Best for overlap):
  1. Syneco Trading GmbH company-portal fix, Muenchen, DE track: housekeeping
     render of an already-verified live role from 16 Sep, not a new find,
     listed first only because its underlying posting is the oldest of the
     four.
  2. Web Computing GmbH, Muenster, Werkstudent AI-Engineer, DE track,
     confirmed live via a direct fetch of web-computing.de, application
     open now.
  3. BLACKFIELD AI, Bremen, Werkstudent AI Engineer, DE track, confirmed
     live via a direct fetch of blackfield.ai, application open now.
  4. Modern Drive Technology GmbH, Neumarkt in der Oberpfalz, Werkstudent
     AI Engineering, DE track, confirmed live via LinkedIn with an "89
     applications" counter showing recent activity, posted approximately
     2 weeks ago per the listing.

Language track per 20 July 2026 language match hard rule (posting body
language IS deliverable language): all four postings are written entirely
in German -> DE track for all four.

German level flags (accept German listings per master-projects.md, flag
the bar against Rah's actual B1 in progress level, not a filter):
  - BLACKFIELD AI states C1/C2 German required, well above B1 in progress.
  - Modern Drive Technology GmbH states "verhandlungssicheres Deutsch"
    (negotiation fluent), also above B1 in progress.
  - Web Computing GmbH states "gute Deutsch- und Englischkenntnisse"
    (good German and English), a softer bar, plausibly reachable at B1
    in progress.
  - Syneco Trading GmbH states no explicit German level bar in the
    posting itself (unchanged from the 16 Sep assessment).
  Flagged here as information for Rah's own judgement per master-projects.md;
  German level is not a scoring filter.

Dedup check against applied-log.csv and Notion (215 CSV rows, 211 Notion
rows at run start, full company plus role comparison run during this
run's reconciliation step): BLACKFIELD AI, Web Computing GmbH, and Modern
Drive Technology GmbH are all entirely new companies, never previously
logged. Syneco Trading GmbH already has one CSV/Notion row (the Xing
version); this run's addition is the pre-existing second Notion row's
company-portal counterpart, not a new duplicate write.

Apply Method set directly in role_configs where determinable from the
posting: BLACKFIELD AI (email application, company-portal, out of
OpenClaw's platform-native scope), Web Computing GmbH (online form on the
company's own domain, company-portal), Modern Drive Technology GmbH
(LinkedIn Easy Apply login required, platform-native, in OpenClaw's
scope). Syneco Trading GmbH company-portal fix keeps its existing
Notion-set Apply Method of company-portal (softgarden career site).

19 August 2026 CV content rules apply: no hyphens or dashes in CV text,
no parentheses or brackets in bullets, Languages EN and DE only, German
level locked to "Deutsch: B1, laufend" or "German: B1, in progress" on
the respective track, no page numbers or headers or footers, 2 page hard
cap, Ojas style header, Skills grouped into functional buckets,
positioning tag under the name is a pitch not the posting title.
"""

from role_configs import (
    ERAY_BULLETS_DE,
    DIABETES_BULLETS_DE,
    CERT_NVIDIA_DE,
    CERT_AWS_DE,
    CERT_GOOGLE_DE,
    ACH_USAII_DE,
    P_RAG_DE,
    P_CREDITIQ_DE,
    P_FLIGHT_DE,
)


CONFIGS_22SEP = [
    # 1. Syneco Trading GmbH, Muenchen -- company-portal housekeeping fix
    # Masterarbeit (m/w/d) Agentic AI und Generative AI zur Optimierung
    # energiewirtschaftlicher Prozesse
    # Company career portal (softgarden, branded Thuga Aktiengesellschaft,
    # hiring entity Syneco Trading GmbH). DE track. Content reused from the
    # already-verified 16 Sep Xing version of this exact role, which never
    # named the Xing platform in its own text.
    # Apply: https://syneco.softgarden.io/job/67345185/Masterarbeit-m-w-d-Agentic-AI-und-Generative-AI-zur-Optimierung-energiewirtschaftlicher-Prozesse?jobDbPVId=284431545&l=de
    {
        "folder": "Syneco Trading Thuga Masterarbeit Agentic AI Generative AI Energiewirtschaft Muenchen",
        "company": "Syneco Trading GmbH",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | Agentische KI und Evaluation | Python + LangGraph + Evaluation Frameworks",
        "role_strip": "Masterarbeit, Agentic AI und Generative AI zur Optimierung energiewirtschaftlicher Prozesse",
        "cl_date": "22. September 2026",
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

    # 2. Web Computing GmbH, Muenster
    # Werkstudent AI-Engineer (m/w/d), 15-20 Std/Woche
    # Company career page (web-computing.de). DE track. Full ML lifecycle
    # work following CRISP-DM: analysis, design, preprocessing, modeling,
    # training, evaluation and integration into existing software systems,
    # across Computer Vision, NLP and Predictive Analytics topics.
    # Apply: https://www.web-computing.de/werkstudent-ai-engineer/
    {
        "folder": "Web Computing Muenster Werkstudent AI Engineer",
        "company": "Web Computing GmbH",
        "lang": "de",
        "location": "Muenster",
        "apply_link": "https://www.web-computing.de/werkstudent-ai-engineer/",
        "apply_method": "company-portal",
        "source": "Company Page",
        "german_level": "B1",
        "tag": "Masterstudent Data Science and Analytics | ML Lifecycle und Evaluation | Python + scikit learn + LangGraph",
        "role_strip": "Werkstudent, AI Engineer",
        "cl_date": "22. September 2026",
        "cl_subject": "Werkstudent AI Engineer in Muenster",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im gesamten ML Lifecycle von der Datenaufbereitung ueber Modellierung bis zur Integration in bestehende Softwaresysteme. Ich habe ein reguliertes Credit Scoring System von der Bereinigung uebe SHAP Analyse bis zu einem ausgelieferten Streamlit Tool gebaut sowie ein Multi Agent RAG System mit systematischer Evaluation auf 5 Dimensionen. Sicher in Python, scikit learn und im Uebergang von Analyse zu produktionsreifer Integration.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_CREDITIQ_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Position als Werkstudent AI Engineer bei der Web Computing GmbH in Muenster. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim passt die Aufgabe, den gesamten ML Lifecycle von Analyse und Design ueber Preprocessing und Modellierung bis zu Training, Evaluation und Integration in bestehende Softwaresysteme mitzugestalten, sehr genau zu dem, was ich in den letzten Monaten praktisch gebaut habe.",
            "In meinem CreditIQ Projekt zu regulierbarem Credit Scoring habe ich AIF360 Mitigation und Schwellenwertkalibrierung angewandt, eine SHAP getriebene Subgruppenanalyse zur Aufdeckung versteckter Verzerrungen durchgefuehrt und das fertige Modell als Streamlit Entscheidungsunterstuetzungs Tool mit vollstaendiger regulatorischer Dokumentation ausgeliefert. Diese Erfahrung, ein Projekt durchgaengig von der Datenanalyse bis zur produktionsreifen Integration zu tragen, deckt sich direkt mit der CRISP-DM gepraegten Arbeitsweise, die die Ausschreibung beschreibt.",
            "In meinem Multi Agent RAG Projekt habe ich einen JudgeAgent implementiert, der Antworten auf 5 Dimensionen im JSON Modus bei Temperatur 0 bewertet, sowie spaCy Pipelines fuer sprachspezifisches Preprocessing eingebunden. Diese Erfahrung, Natural Language Processing Komponenten systematisch zu evaluieren statt nur zu prototypisieren, uebertraegt sich direkt auf die in der Ausschreibung genannten Themenfelder Computer Vision, NLP und Predictive Analytics.",
            "Ich arbeite sicher in Python mit TensorFlow und scikit learn und habe praktische Erfahrung mit agiler Softwareentwicklung. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend, ich hebe es aktiv weiter, und Englisch spreche ich fliessend. Ich kann die Werkstudentenstelle zeitnah beginnen und stelle mich gerne in einem persoenlichen Gespraech vor.",
        ],
    },

    # 3. BLACKFIELD AI, Bremen
    # Werkstudent AI Engineer (m/w/d), 15-20 Std/Woche
    # Company career page (blackfield.ai), email application. DE track.
    # LLM/ML use case prototyping, data preparation and evaluations,
    # scripts/tests/data pipelines, MLOps research.
    # Apply: info@blackfield.ai (via https://blackfield.ai/karriere/werkstudent-ai-engineer-mwd)
    {
        "folder": "BLACKFIELD AI Bremen Werkstudent AI Engineer",
        "company": "BLACKFIELD AI",
        "lang": "de",
        "location": "Bremen",
        "apply_link": "https://blackfield.ai/karriere/werkstudent-ai-engineer-mwd",
        "apply_method": "company-portal",
        "source": "Company Page",
        "german_level": "B1",
        "tag": "Masterstudent Data Science and Analytics | LLM Evaluation und Data Pipelines | Python + LangGraph + MLOps",
        "role_strip": "Werkstudent, AI Engineer",
        "cl_date": "22. September 2026",
        "cl_subject": "Werkstudent AI Engineer in Bremen",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Prototyping von LLM und ML Use Cases inklusive Datenaufbereitung, systematischer Evaluation und automatisierter Datenpipelines. Ich habe ein Multi Agent RAG System mit einem unabhaengigen LLM as Judge Modell gebaut, das Antworten auf 5 Dimensionen bewertet, sowie eine per Apache Airflow orchestrierte Pipeline mit Gate Checks und automatisierten Tests. Sicher in Python mit pandas und scikit learn und im Aufbau reproduzierbarer, testbarer Skripte fuer nicht deterministische KI Systeme.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_FLIGHT_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Position als Werkstudent AI Engineer bei BLACKFIELD AI in Bremen. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim passt die Aufgabe, LLM und ML Use Cases inklusive Datenaufbereitung und Evaluation zu prototypisieren sowie Skripte, Tests und Datenpipelines zu pflegen, sehr genau zu dem, was ich in den letzten Monaten praktisch gebaut habe.",
            "In meinem Multi Agent RAG Projekt habe ich einen JudgeAgent implementiert, der Antworten auf 5 Dimensionen Grounding, Relevanz, Vollstaendigkeit, Zitatqualitaet und Sprachqualitaet im JSON Modus bei Temperatur 0 bewertet, und Self Preference Bias eliminiert, indem der Richter auf einem anderen lokalen Modell laeuft als der Generator, mit einer harten Fehlerbehandlung bei fehlendem Judge Modell. Diese Erfahrung, LLM Use Cases systematisch statt subjektiv zu evaluieren, deckt sich direkt mit der in der Ausschreibung genannten Aufgabe, Evaluationen fuer LLM und ML Use Cases zu unterstuetzen.",
            "In meinem Real Time Flight Tracking Projekt habe ich Python Collectors und PySpark Cleaning Skripte gebaut sowie das Gesamtsystem mit Apache Airflow orchestriert, sodass Batch und Echtzeit Schichten automatisch aktualisiert werden, und dbt Modelle mit klaren Tests gepflegt. Diese Erfahrung, Skripte, Tests und Datenpipelines produktionsnah zu pflegen statt nur einmalig zu prototypisieren, uebertraegt sich direkt auf die MLOps orientierten Aufgaben der Ausschreibung.",
            "Ich arbeite sicher in Python mit pandas und scikit learn und habe praktische Erfahrung mit LLM Prompting und sauberem Code inklusive Git Workflows. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend, ich hebe es aktiv weiter, und Englisch spreche ich fliessend. Ich kann die Werkstudentenstelle zeitnah beginnen und stelle mich gerne in einem persoenlichen Gespraech vor.",
        ],
    },

    # 4. Modern Drive Technology GmbH, Neumarkt in der Oberpfalz
    # Werkstudent AI Engineering (m/w/d), 15-20 Std/Woche waehrend des
    # Semesters
    # LinkedIn Easy Apply, platform-native. DE track. Process automation
    # via AI agents, LLM API integrations, automation workflows and REST
    # integrations; LangChain/LangGraph and RAG preferred.
    # Apply: LinkedIn job posting (id 4462220941)
    {
        "folder": "Modern Drive Technology Neumarkt Werkstudent AI Engineering",
        "company": "Modern Drive Technology GmbH",
        "lang": "de",
        "location": "Neumarkt in der Oberpfalz",
        "apply_link": "https://de.linkedin.com/jobs/view/werkstudent-ai-engineering-m-w-d-at-modern-drive-technology-gmbh-4462220941",
        "apply_method": "platform-native",
        "source": "LinkedIn",
        "german_level": "B1",
        "tag": "Masterstudent Data Science and Analytics | KI Agenten und Prozessautomatisierung | Python + LangGraph + REST Integrationen",
        "role_strip": "Werkstudent, AI Engineering",
        "cl_date": "22. September 2026",
        "cl_subject": "Werkstudent AI Engineering in Neumarkt in der Oberpfalz",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Bau von KI Agenten und der Automatisierung wiederkehrender Prozesse ueber LLM APIs und REST Integrationen. Ich habe ein LangGraph Multi Agenten System mit klar abgegrenzten Verantwortlichkeiten gebaut sowie eine vollautomatisierte Airflow Orchestrierung mit Gate Checks, die manuelle Wiederholungen ersetzt. Sicher im Uebersetzen von Prozessverstaendnis in automatisierte, produktionsreife Loesungen in Python.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_FLIGHT_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Position als Werkstudent AI Engineering bei der Modern Drive Technology GmbH in Neumarkt in der Oberpfalz. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim passt die Aufgabe, mit Prozessverantwortlichen zu sprechen, Engpaesse zu identifizieren und Automatisierungsloesungen mit KI Agenten, LLM Integrationen und Systemanbindungen zu bauen, sehr genau zu dem, was ich in den letzten Monaten praktisch gebaut habe.",
            "In meinem Multi Agent RAG Projekt habe ich ein LangGraph basiertes Agentensystem mit einem LanguageAgent und Retrieval Agenten entworfen, jeweils mit klar abgegrenzten Verantwortlichkeiten und definiertem Fallback Verhalten. Diese Erfahrung, Agentensysteme eigenstaendig zu entwerfen und technische Entscheidungen ueber die Zusammenarbeit einzelner Agenten zu treffen, ist genau das, was der Bau von KI Agenten und Automatisierungsloesungen von Grund auf braucht.",
            "In meinem Real Time Flight Tracking Projekt habe ich bestehende manuelle Prozesse durch eine mit Apache Airflow orchestrierte Pipeline ersetzt, die Batch und Echtzeit Schichten automatisch alle 15 Minuten ohne manuellen Eingriff aktualisiert, und dabei Klarheit ueber Uebergabepunkte und Gate Checks dokumentiert. Diese Erfahrung, bestehende Ablaeufe zu dokumentieren und durch pragmatische Automatisierung zu ersetzen statt sie zu ueberkomplizieren, uebertraegt sich direkt auf die in der Ausschreibung beschriebene Arbeit mit Prozessverantwortlichen.",
            "Ich arbeite sicher in Python und habe praktische Erfahrung mit LangGraph, Prompt Engineering und REST Integrationen. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend, ich hebe es aktiv weiter, und Englisch spreche ich fliessend. Ich kann mindestens einen Tag pro Woche vor Ort in Neumarkt sein und bespreche die Aufgabe gerne in einem persoenlichen Gespraech.",
        ],
    },
]
