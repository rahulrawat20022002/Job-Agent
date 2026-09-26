"""Role configurations for the 26 September 2026 scheduled job search run
(8 to 10 drafted tier, capped at top 3 under the 28 July 2026 yield reset).

Backlog gate check per 14 July 2026 status source of truth rule: Notion
data source fd974369-40b2-48c5-b660-d15256c88f52 returned 9 rows in status
'drafted' at run start. 9 falls in the 8 to 10 tier, which caps this run at
the top 3 newly scored roles.

Reconciliation this run compared all 219 CSV rows against all 221 valid
Notion rows (one blank placeholder row, "New CVs now", excluded as not a
real job row) and found 6 drift rows where Notion had moved past
'drafted' (Mercedes-Benz AG Vans to rejected, Syneco Trading GmbH x2 rows
to applied, Web Computing GmbH and Modern Drive Technology GmbH to
applied, BLACKFIELD AI to rejected) while the CSV still said 'drafted' or
an older status; all 6 were corrected in the CSV to match Notion per
invariant #1. One apparent mismatch (Aerzteverband Deutscher Allergologen
with and without the umlaut) is a spelling variant only, both sides
already read 'applied', no action needed. Two duplicate CSV rows for
KontextWork GbR (both 'Not listed Anymore') are a harmless CSV-internal
duplicate, no fix needed.

CRITICAL FINDING this run, reported in full in Job_Digest_2026-09-26.md and
flagged prominently to Rah: 7 of the 9 Notion rows carrying Status =
'drafted' at run start (Atos, COBACK, Sopra Steria Custom Software
Solutions GmbH / Agentic Coding, coac GmbH, PRODIGY Consulting GmbH, Reply
Deutschland SE / AI Business Solutions und Agents, KWS SAAT SE and Co
KGaA) have NO corresponding draft folder anywhere on disk and NO CSV row
at all. This is the exact false-drafted-flag risk invariant #3 warns
about: a prior run's Notion write for these 7 rows was never backed by an
actual render. This run does NOT fabricate a fix for those 7 (would
require inventing tailored content without having done the search/scoring
work for them), does NOT touch their Notion Status (Cowork does not flip
Notion Status per the agent boundary, and inventing a retroactive
'drafted' justification would itself be a fabrication), and instead flags
all 7 in the digest for Rah's decision. Separately, the 8th and 9th rows
(retorio GmbH, KontextWork GbR) DO have real rendered folders on disk, but
retorio GmbH's Notion Draft Path field pointed at a folder name
("retorio Muenchen Working Student AI Engineer Agentic Systems") that does
not exist; the actual folder is "Retorio Munich Working Student AI
Engineer Agentic Systems". This is a safe text-field correction (not a
status flip), so this run corrected the Draft Path in Notion directly.
Note: in making that correction the previous Notes field content was
inadvertently overwritten rather than appended; also flagged in the
digest as a process error to avoid repeating.

Search ran via WebSearch and WebFetch across LinkedIn, StepStone, Xing,
JobTeaser and company career pages (Tavily MCP failed to connect again
this run; no Indeed MCP tool was available in this session, so Indeed was
not used). Many promising leads surfaced through aggregator search results
(join.com, arbeitnow.com, startup.jobs, studysmarter.de, workopia.io) but
resolved to expired/removed postings (410 Gone or removed from the
company's own careers page) when checked directly, and were dropped under
invariant #4 (every write must be auditable, only a currently-live posting
counts as evidence):
  - CognitX AI GmbH, AI/LLM Engineering (Werkstudent), Darmstadt: both
    join.com listing IDs returned 410 Gone; company's own join.com career
    page states "no open positions at the moment". Dropped.
  - Jemix GmbH, Werkstudent AI Engineer, Berlin: StepStone/search listing
    exists but the company's own join.com jobs page lists only an
    apprenticeship, a sales role, and an IT support role in Spain; no AI
    Engineer Werkstudent among current openings. Dropped as no longer
    live (same conclusion as the 22 Sep run's assessment of this company).
  - Allianz Kunde und Markt GmbH, Werkstudent Robotik-Prozessautomatisierung
    & Agentic AI, Unterfoehring: the specific posting URL returned 410
    Gone and does not appear on Allianz's own student careers page.
    Dropped as no longer live.
  - ponturo consulting AG, Werkstudent AI Engineer (multiple cities): the
    third-party mirror (studysmarter) is 410 Gone and the company's own
    join.com careers page lists only a "Spontaneous Application" option,
    no AI Engineer role. Dropped, consistent with the 22 Sep run's finding
    for this same company.
  - HDI AG, Agentic AI Platform Engineer, Hannover: StepStone listing
    traces back to a posting dated March 2026, 6+ months stale. Dropped
    on freshness grounds.
  - Jobgether, "AI Engineer", Germany (remote/onsite conflict in the
    listing itself): Jobgether is a staffing/aggregator brand, not the
    actual hiring company; the posting requires sign-in to view further
    details, gives no work type, and gives no traceable hiring entity.
    Dropped under invariant #4, not auditable.
  - appliedAI Initiative GmbH, Working Student Agentic AI & Automation,
    Munich: search-indexed listing no longer appears on the company's own
    current careers page, which lists only the pre-existing "Working
    Student AI Engineering & Product Development" role (already logged as
    rejected in Notion/CSV from an earlier run). Dropped as no longer live
    and would in any case duplicate an existing row.

Three roles cleared verification: a live posting fetched directly (or, for
SmartTECS, the official Bundesagentur fuer Arbeit job listing), a
confirmed apply path, and a clean dedup check against applied-log.csv and
Notion (219 CSV rows, 221 valid Notion rows at run start).

Platform mix this run:
  - Company Page, 2 (Rohde & Schwarz, own careers portal job.rohde-schwarz.com;
    Ventum Consulting GmbH & Co. KG, own careers page via Onlyfy application
    form)
  - Other, 1 (SmartTECS Cyber Security GmbH, listed and applied via the
    official Bundesagentur fuer Arbeit reference-number system, not one of
    the four platform-native aggregators)
  - LinkedIn, Xing, StepStone, JobTeaser, Indeed: surfaced no new in-scope,
    verifiable, non-duplicate postings this run beyond the leads listed as
    dropped above (Indeed not used, no MCP tool available this session).

Freshness order (all three fall in the single Germany tier, ranked by
recency then Best for overlap):
  1. Rohde & Schwarz, Stuttgart, Werkstudent AI Agents fuer Software
     Engineering, DE track, posted 19 September 2026 (confirmed on the
     company's own job portal), Referenz 2351.
  2. Ventum Consulting GmbH & Co. KG, Muenchen, Werkstudent AI, DE track,
     confirmed live via a direct fetch of ventum-consulting.com; no exact
     posting date shown on the page.
  3. SmartTECS Cyber Security GmbH, Chemnitz/Dresden, Werkstudent AI
     Engineer, DE track, confirmed live via the official Bundesagentur
     fuer Arbeit listing, shown as posted "vor 30+ Tagen" (over 30 days
     ago) but still listed as open on the official government job board.

Language track per 20 July 2026 language match hard rule (posting body
language IS deliverable language): all three postings are written
entirely in German -> DE track for all three.

German level flags (accept German listings per master-projects.md, flag
the bar against Rah's actual B1 in progress level, not a filter):
  - SmartTECS Cyber Security GmbH states "Deutsch und Englisch sehr gut"
    (very good German and English), above B1 in progress.
  - Ventum Consulting GmbH & Co. KG states "sehr gute Deutschkenntnisse"
    (excellent German) plus good English, above B1 in progress.
  - Rohde & Schwarz: posting entirely in German implies working German is
    needed day to day; no explicit CEFR level was stated in the fetched
    extract.
  Flagged here as information for Rah's own judgement per
  master-projects.md; German level is not a scoring filter.

Dedup check against applied-log.csv and Notion (219 CSV rows, 221 valid
Notion rows at run start, full company plus role comparison run during
this run's reconciliation step): all three companies and roles are
entirely new, never previously logged. Rohde & Schwarz has two prior
entries under this exact CSV/Notion history (Memmingen Data Analytics and
Data Science, 'Not listed Anymore'; Teisnach Werkstudent Agentic AI
Experiments, 'applied') but this Stuttgart AI Agents for Software
Engineering role is a distinct location and distinct role focus (developer
productivity and knowledge management tooling for AI assistants, not
generic "Agentic AI Experiments"), allowed under the standing 'different
roles at the same company' rule.

Apply Method set directly in role_configs where determinable from the
posting: Rohde & Schwarz (own ATS portal, company-portal, out of
OpenClaw's platform-native scope), Ventum Consulting (Onlyfy application
form on the company's own domain, company-portal), SmartTECS Cyber
Security GmbH (Bundesagentur fuer Arbeit reference-number application,
company-portal, out of OpenClaw's platform-native scope).

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
    P_MOVIE_DE,
)


CONFIGS_26SEP = [
    # 1. Rohde & Schwarz, Stuttgart
    # Werkstudent AI Agents fuer Software Engineering (m/w/d)
    # Company career portal (job.rohde-schwarz.com), posted 19 Sep 2026,
    # Referenz 2351. DE track. Up to 20 hours/week, mobile work options,
    # central workplace Stuttgart. Aufbereitung, Strukturierung und
    # Validierung technischer Informationen fuer KI-Assistenten und AI
    # Agents; developer productivity and knowledge management focus.
    # Apply: https://job.rohde-schwarz.com/job/Stuttgart-Werkstudent-AI-Agents-für-Software-Engineering-(mwd)-70499/1435136733/
    {
        "folder": "Rohde Schwarz Stuttgart Werkstudent AI Agents Software Engineering",
        "company": "Rohde & Schwarz",
        "lang": "de",
        "location": "Stuttgart",
        "apply_link": "https://job.rohde-schwarz.com/job/Stuttgart-Werkstudent-AI-Agents-für-Software-Engineering-(mwd)-70499/1435136733/",
        "apply_method": "company-portal",
        "source": "Company Page",
        "german_level": "B1",
        "tag": "Masterstudent Data Science and Analytics | KI Agenten und Evaluation | Python + LangGraph + Automatisierung",
        "role_strip": "Werkstudent, AI Agents fuer Software Engineering",
        "cl_date": "26. September 2026",
        "cl_subject": "Werkstudent AI Agents fuer Software Engineering in Stuttgart, Referenz 2351",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau und in der Evaluation von KI Agenten, die technische Informationen strukturieren und aufbereiten. Ich habe ein LangGraph Multi Agenten System mit einem unabhaengigen LLM as Judge Modell gebaut, das Antworten auf 5 Dimensionen bewertet, sowie eine vollautomatisierte Airflow Orchestrierung mit klaren Uebergabepunkten und Gate Checks. Sicher in Python und im Uebersetzen unstrukturierter technischer Information in eine Form, die KI Assistenten zuverlaessig nutzen koennen.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_FLIGHT_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit AI Agents fuer Software Engineering bei Rohde & Schwarz in Stuttgart, Referenz 2351. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim passt die Aufgabe, technische Informationen fuer die Nutzung durch KI Assistenten und AI Agents aufzubereiten, zu strukturieren und zu validieren, sehr genau zu dem, was ich in den letzten Monaten praktisch gebaut habe.",
            "In meinem Multi Agent RAG Projekt habe ich einen LanguageAgent und einen JudgeAgent in einem LangGraph Multi Agenten System implementiert, wobei der JudgeAgent Antworten auf 5 Dimensionen Grounding, Relevanz, Vollstaendigkeit, Zitatqualitaet und Sprachqualitaet im JSON Modus bei Temperatur 0 bewertet und Self Preference Bias eliminiert, indem er auf einem anderen lokalen Modell laeuft als der Generator. Diese Erfahrung, die Qualitaet und Verlaesslichkeit von KI Agenten systematisch statt subjektiv zu pruefen, deckt sich direkt mit der in der Ausschreibung genannten Aufgabe rund um Developer Productivity und Knowledge Management fuer AI Agents.",
            "In meinem Real Time Flight Tracking Projekt habe ich das Gesamtsystem mit Apache Airflow auf GCS gestuetztem Speicher und Dataproc Compute orchestriert, sodass Batch und Echtzeit Schichten automatisch alle 15 Minuten ohne manuellen Eingriff aktualisiert werden, und dabei technische Informationen aus vier Datenquellen sauber zusammengefuehrt und validiert. Diese Erfahrung, rohe technische Information in eine strukturierte, validierte und automatisiert aktualisierte Form zu ueberfuehren, uebertraegt sich direkt auf die Aufbereitung technischer Informationen fuer KI Assistenten.",
            "Ich arbeite sicher in Python und habe praktische Erfahrung mit Linux, Docker und CI/CD Workflows aus meiner Zeit bei SS Engineers and Contractors, wo ich Playwright End to End Tests in ein bestehendes Code Review Verfahren integriert habe. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend, ich hebe es aktiv weiter, und Englisch spreche ich fliessend. Ich kann bis zu 20 Stunden pro Woche waehrend der Vorlesungszeit in Stuttgart einsteigen und bespreche meinen Beitrag gerne in einem persoenlichen Gespraech.",
        ],
    },

    # 2. Ventum Consulting GmbH & Co. KG, Muenchen
    # Werkstudent AI (m/w/d)
    # Company career page (ventum-consulting.com), Onlyfy application form.
    # DE track. Internal "AI Factory" role: entwickeln und testen von
    # KI-basierten Loesungen zur Optimierung interner Prozesse und
    # Arbeitsablaeufe.
    # Apply: https://ventum-consulting.onlyfy.jobs/apply/0zb1tx6doqa7jw1bxgpddwd7pi3enab
    {
        "folder": "Ventum Consulting Muenchen Werkstudent AI",
        "company": "Ventum Consulting GmbH & Co. KG",
        "lang": "de",
        "location": "Muenchen",
        "apply_link": "https://ventum-consulting.onlyfy.jobs/apply/0zb1tx6doqa7jw1bxgpddwd7pi3enab",
        "apply_method": "company-portal",
        "source": "Company Page",
        "german_level": "B1",
        "tag": "Masterstudent Data Science and Analytics | Generative KI und Prozessautomatisierung | Python + LangGraph + Cloud",
        "role_strip": "Werkstudent, AI",
        "cl_date": "26. September 2026",
        "cl_subject": "Werkstudent AI in Muenchen",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Entwickeln und Testen KI basierter Loesungen zur Optimierung interner Prozesse und Arbeitsablaeufe. Ich habe ein Multi Agent RAG System mit generativer KI und Large Language Models end to end gebaut sowie eine vollautomatisierte Cloud Pipeline, die ohne manuellen Eingriff laeuft. Sicher in Python, generativer KI und im Uebersetzen von Prozessverstaendnis in getestete, dokumentierte Automatisierungsloesungen.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_MOVIE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit AI bei der Ventum Consulting GmbH & Co. KG in Muenchen. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim passt die Aufgabe, KI basierte Loesungen zur Optimierung interner Prozesse und Arbeitsablaeufe zu entwickeln und zu testen, sehr genau zu dem, was ich in den letzten Monaten praktisch gebaut habe.",
            "In meinem Multi Agent RAG Projekt habe ich ein LangGraph orchestriertes Agentensystem mit generativer KI und Large Language Models gebaut, das Nutzerfragen in Englisch oder Deutsch end to end beantwortet, inklusive eines JudgeAgent, der Antworten auf 5 Dimensionen im JSON Modus bei Temperatur 0 bewertet. Diese Erfahrung, generative KI Systeme sauber zu strukturieren, zu testen und zu dokumentieren statt nur zu prototypisieren, deckt sich direkt mit der in der Ausschreibung genannten Aufgabe rund um interne KI basierte Prozessloesungen.",
            "In meinem Movie Analytics und ML Pipeline Projekt habe ich eine 3 stufige Bronze Silver Gold Medaillon Architektur auf BigQuery und Cloud Run mit vollautomatisiertem Cloud Scheduler Trigger gebaut, die ohne manuellen Eingriff laeuft, und den Silver Layer mit Schema Enforcement und Datenvalidierung gehaertet. Diese Erfahrung, bestehende manuelle Arbeitsablaeufe in eine automatisierte, gut dokumentierte Pipeline zu ueberfuehren, uebertraegt sich direkt auf die interne Prozessoptimierung, die die Ausschreibung beschreibt.",
            "Ich arbeite sicher in Python und habe erste Erfahrung mit JavaScript und TypeScript aus meiner Zeit bei SS Engineers and Contractors, wo ich React Komponenten fuer interne Dashboards und Portale gebaut habe. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend, ich hebe es aktiv weiter, und Englisch spreche ich fliessend. Ich kann als Werkstudent in Muenchen zeitnah einsteigen und stelle mich gerne in einem persoenlichen Gespraech vor.",
        ],
    },

    # 3. SmartTECS Cyber Security GmbH, Chemnitz / Dresden
    # Werkstudent AI Engineer (m/w/d)
    # Listed on the official Bundesagentur fuer Arbeit job board, apply via
    # Referenz-Nr. 10001-1003090842-S. DE track. Local AI solutions, data
    # engineering for AI applications, RAG systems, embeddings and vector
    # databases, ML model fine tuning, GenAI security risk analysis based
    # on OWASP Top 10.
    # Apply: https://www.arbeitsagentur.de/jobsuche/jobdetail/10001-1003090842-S
    {
        "folder": "SmartTECS Cyber Security Chemnitz Dresden Werkstudent AI Engineer",
        "company": "SmartTECS Cyber Security GmbH",
        "lang": "de",
        "location": "Chemnitz, Dresden",
        "apply_link": "https://www.arbeitsagentur.de/jobsuche/jobdetail/10001-1003090842-S",
        "apply_method": "company-portal",
        "source": "Other",
        "german_level": "B1",
        "tag": "Masterstudent Data Science and Analytics | RAG Systeme und Vector Datenbanken | Python + LangGraph + Evaluation",
        "role_strip": "Werkstudent, AI Engineer",
        "cl_date": "26. September 2026",
        "cl_subject": "Werkstudent AI Engineer, Referenz 10001-1003090842-S",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau von RAG Systemen, Vector Datenbanken und der systematischen Evaluation generativer KI Systeme. Ich habe ein Multi Agent RAG System mit hybrider BM25 plus Dense Retrieval Pipeline ueber Pinecone gebaut sowie in CreditIQ ein reguliertes Machine Learning System mit vollstaendiger Fairness und Sicherheitsdokumentation ausgeliefert. Sicher in Python, RAG Architekturen, Embeddings und im Modell Fine Tuning.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_CREDITIQ_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit AI Engineer bei der SmartTECS Cyber Security GmbH am Standort Chemnitz oder Dresden, Referenz 10001-1003090842-S. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim passt die Aufgabe, lokale KI Loesungen zu konzipieren, RAG basierte Systeme mit Embeddings und Vector Datenbanken zu entwickeln und Modelle fein abzustimmen, sehr genau zu dem, was ich in den letzten Monaten praktisch gebaut habe.",
            "In meinem Multi Agent RAG Projekt habe ich Embeddings ueber paraphrase multilingual MiniLM in einen gemeinsamen Pinecone Vector Space migriert und eine hybride BM25 plus Dense Retrieval Pipeline gebaut, sodass eine deutsche Anfrage englische Quellen findet und Ende zu Ende auf Deutsch beantwortet wird. Diese Erfahrung, RAG Systeme mit Vector Datenbanken von Grund auf zu konzipieren und zu integrieren, deckt sich direkt mit der in der Ausschreibung genannten Aufgabe rund um Datenmanagement und RAG basierte Loesungen.",
            "In CreditIQ habe ich ein reguliertes Kredit Scoring System entwickelt und dabei Sicherheits und Fairness Risiken systematisch dokumentiert, unter anderem ueber einen vollstaendigen regulatorischen Bericht zu EU AI Act, GDPR und Angriffsvektoren. Diese Erfahrung, generative und Machine Learning Systeme auf Sicherheitsrisiken hin zu bewerten statt sie ungeprueft auszuliefern, uebertraegt sich direkt auf die in der Ausschreibung genannte Analyse von Sicherheitsrisiken generativer KI Systeme nach OWASP Top 10.",
            "Ich arbeite sicher in Python mit ML Frameworks und habe praktische Erfahrung im Modell Fine Tuning ueber CatBoost MultiQuantile bei eRay GmbH. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend, ich hebe es aktiv weiter, und Englisch spreche ich fliessend, auch wenn die Ausschreibung sehr gute Kenntnisse in beiden Sprachen nennt, moechte ich hier offen sein und bringe gleichzeitig sehr belastbare fachliche Faehigkeiten mit. Ich kann als Werkstudent in Chemnitz oder Dresden zeitnah einsteigen und stelle mich gerne in einem persoenlichen Gespraech vor.",
        ],
    },
]
