"""Role configurations for the 24 September 2026 scheduled job search run
(normal top 3 cut).

Backlog gate check per 14 July 2026 status source of truth rule: Notion
data source fd974369-40b2-48c5-b660-d15256c88f52 returned 3 rows in status
'drafted' at run start (Atos, Sopra Steria Custom Software Solutions GmbH,
COBACK). 3 drafted falls well under the 8 row floor of the 28 July 2026
yield based reset rule, which allows a normal top 3 to 5 cut.

Data integrity finding during reconciliation, not fixed here: all three of
those Notion drafted rows have no matching CSV row and no draft folder
anywhere in the repo or git history. This is the false drafted flag
invariant #3 warns about. Unlike the 22 September run's Syneco Trading
housekeeping fix (where the missing render was for an already fully
tailored role reused from an earlier verified posting), these three have
no prior tailored content anywhere to reuse, so nothing was rendered for
them this run. They are reported in the digest as an open data integrity
issue for Rah, not silently mirrored into the CSV and not silently
redrafted under a guess at what the original postings were.

Reconciliation this run compared all 219 CSV rows against all 216 valid
Notion rows (one blank placeholder row, "New CVs now", excluded as not a
real job row) and found 5 CSV rows where Notion had moved past 'drafted'
(two Syneco Trading GmbH rows including the still open Thuga duplicate
both to applied, Web Computing GmbH and Modern Drive Technology GmbH to
applied, BLACKFIELD AI to rejected) while the CSV still said 'drafted';
all 5 were corrected in the CSV to match Notion per invariant #1. The
Syneco Trading GmbH Thuga row duplicates the same company and role as the
already applied Xing version; both CSV rows now read applied to match the
single Notion row that tracks this job. One apparent mismatch (Aerzteverband
Deutscher Allergologen with and without the umlaut) is a spelling variant
only, both sides already read applied, no action needed.

Search ran via WebSearch and WebFetch only. Tavily MCP failed to connect
this run (confirmed via the session tool list, a repeat of the pattern
noted in the 22 Sep digest). No browser or Chrome MCP tool was configured
in this session at all, so LinkedIn, Xing, and StepStone individual
listing pages could not be opened directly the way prior runs describe;
WebFetch on every LinkedIn, Xing, StepStone, Indeed, and JobTeaser
individual listing URL attempted this run returned 403, 404, or 410
(examples: de.indeed.com search page 403, jobteaser.com job offer page
403, three separate StepStone stellenangebote pages 410 or 404 within
minutes of surfacing in search results). This is a harder sourcing
failure than prior runs saw and is flagged plainly here and in the digest
rather than worked around by inventing posting content.

Three roles cleared verification through a different, narrower channel
this run: WebFetch succeeded directly against a small aggregator or ATS
page for each (freehire.me and himalayas.app for PRODIGY Consulting,
coac GmbH's own teamtailor.com career page), and for Reply Deutschland SE
two independent WebSearch result summaries agreed on the same title,
hours per week, and technology stack even though the reply.com and
jobteaser.com pages themselves both 404 or 403'd on direct fetch, so that
one is weaker evidence than the other two and is flagged as such below and
in the digest.

Leads found and dropped this run:
  - Retorio GmbH Working Student AI Engineer Agentic Systems (Munich)
    resurfaced again in search; already logged in Notion as Not listed
    Anymore, dropped as a duplicate under the standing company plus role
    case insensitive dedup rule.
  - Mercedes Benz Tech Innovation Working Student AI Agents and Robotics
    Platform resurfaced again in search; already logged in Notion as
    rejected, dropped as a duplicate.
  - CITTI Handelsgesellschaft mbH und Co. KG Werkstudent KI Engineer,
    Kiel: the youngcapital.de mirror explicitly states the position is no
    longer active, dropped as not currently live.
  - Ponturo Consulting AG, SmartTECS Engineers GmbH, and NXP
    Semiconductors Germany GmbH Werkstudent or Working Student AI Engineer
    listings surfaced in search snippets but every individual StepStone
    listing URL fetched returned 404 or 410 within the same search
    session, meaning the listing had already expired or the search index
    was stale; dropped as unverifiable live postings under invariant #4.

Platform mix this run (new finds only):
  - Other (non platform aggregator, Himalayas via freehire.me), 1
    (PRODIGY Consulting GmbH, remote)
  - Company Page (coac GmbH's own teamtailor.com career page), 1
  - JobTeaser, 1 (Reply Deutschland SE, weaker evidence, see above)
  - LinkedIn, Xing, StepStone, Indeed surfaced no individually verifiable,
    non duplicate, in scope postings this run for the reasons above.

Freshness order (all three fall in the single Germany tier, ranked by
verification strength then Best for overlap):
  1. PRODIGY Consulting GmbH, remote Germany, Werkstudent AI Experimenter
     LLM und Dokumentenverarbeitung, DE track, confirmed live via two
     independent direct WebFetch calls (freehire.me mirror and the
     himalayas.app listing itself).
  2. coac GmbH, Berlin und Koeln (remote moeglich), Werkstudent
     Softwareentwicklung und KI, DE track, confirmed live via a direct
     WebFetch of the company's own teamtailor.com career page.
  3. Reply Deutschland SE, Frankfurt am Main and other German cities
     (teilweise remote), Werkstudent AI Business Solutions und Agents, DE
     track, confirmed only via two independent WebSearch result summaries
     that agree on title, hours, and technology stack; direct WebFetch of
     both the reply.com and jobteaser.com pages failed (404 and 403).
     Flagged as weaker evidence in the digest; Rah should sanity check the
     posting is still live before submission.

Language track per 20 July 2026 language match hard rule (posting body
language IS deliverable language): all three postings are written
entirely in German -> DE track for all three.

German level flags (accept German listings per master-projects.md, flag
the bar against Rah's actual B1 in progress level, not a filter):
  - PRODIGY Consulting GmbH requires German language applications but
    states no explicit CEFR bar in the extracted text; flagged as B1
    plausible.
  - coac GmbH explicitly requires "muttersprachlichem Niveau" (native
    level German), well above B1 in progress; flagged prominently, still
    shipped per the standing rule that language level does not filter
    listings.
  - Reply Deutschland SE's snippets mention German and English
    communication skills without a specific CEFR bar; flagged as B1
    plausible pending direct confirmation once the page is reachable.

Dedup check against applied-log.csv and Notion (219 CSV rows, 216 valid
Notion rows at run start, full company plus role comparison run during
this run's reconciliation step): PRODIGY Consulting GmbH and coac GmbH are
entirely new companies, never previously logged. Reply Deutschland SE
already has two Notion and CSV rows for other, differently titled roles
(Generative AI Google Cloud, rejected; AI Data Engineering und Tool
Entwicklung, applied); this AI Business Solutions und Agents role is a
distinct requisition and title, allowed under the standing different
roles at the same company rule.

Apply Method set directly in role_configs where determinable: PRODIGY
Consulting GmbH (Himalayas platform, application requires creating a
Himalayas talent account, out of OpenClaw's platform native scope and
specifically flagged since OpenClaw must never create accounts per its
strict rule 4), coac GmbH (teamtailor.com company career page,
company-portal), Reply Deutschland SE (JobTeaser listing, company-portal,
not one of OpenClaw's four named platform native domains).

19 August 2026 CV content rules apply: no hyphens or dashes in CV text, no
parentheses or brackets in bullets, Languages EN and DE only, German level
locked to "Deutsch: B1, laufend" on the DE track, no page numbers or
headers or footers, 2 page hard cap, Ojas style header, Skills grouped
into functional buckets, positioning tag under the name is a pitch not the
posting title.
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


CONFIGS_24SEP = [
    # 1. PRODIGY Consulting GmbH, remote Germany
    # Werkstudent (m/w/d) AI Experimenter, LLM und Dokumentenverarbeitung
    # Listing surfaced via freehire.me, hosted on the Himalayas platform.
    # DE track. Prompt engineering, variant testing, quality evaluation,
    # document and OCR extraction workflows, prototype to production.
    # Apply: https://himalayas.app/companies/bernert-immobilien-gmbh/jobs/prodigy-consulting-gmbh-werkstudent-m-w-d-ai-experimenter-llm-document-in
    {
        "folder": "PRODIGY Consulting Remote Werkstudent AI Experimenter LLM Document",
        "company": "PRODIGY Consulting GmbH",
        "lang": "de",
        "location": "Deutschlandweit, Remote",
        "apply_link": "https://himalayas.app/companies/bernert-immobilien-gmbh/jobs/prodigy-consulting-gmbh-werkstudent-m-w-d-ai-experimenter-llm-document-in",
        "apply_method": "company-portal",
        "source": "Other",
        "german_level": "B1",
        "tag": "Masterstudent Data Science and Analytics | KI Experimente und LLM Evaluation | Python + Prompt Engineering + Evaluation",
        "role_strip": "Werkstudent, AI Experimenter fuer LLM und Dokumentenverarbeitung",
        "cl_date": "24. September 2026",
        "cl_subject": "Werkstudent AI Experimenter fuer LLM und Dokumentenverarbeitung, Remote",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im systematischen Testen und Bewerten von LLM Workflows sowie im Bau automatisierter Datenverarbeitungspipelines. Ich habe ein Multi Agent RAG System mit einem unabhaengigen LLM as Judge Modell gebaut, das Antworten auf 5 Dimensionen im JSON Modus bei Temperatur 0 bewertet, sowie eine vollautomatisierte Pipeline, die rohe Eingabedaten ueber mehrere Quellen zu einer sauberen, produktionsreifen Ausgabe verarbeitet. Sicher in Python und im Uebersetzen experimenteller Prototypen in dokumentierte, wiederholbare Ergebnisse.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_MOVIE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit AI Experimenter fuer LLM und Dokumentenverarbeitung bei der PRODIGY Consulting GmbH, remote in Deutschland. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim passt die Aufgabe, KI gestuetzte Workflows zu entwerfen, Prompt Engineering und Variantentests durchzufuehren und Prototypen bis zur Produktionsreife zu verfeinern, sehr genau zu dem, was ich in den letzten Monaten praktisch gebaut habe.",
            "In meinem Multi Agent RAG Projekt habe ich einen JudgeAgent implementiert, der Antworten auf 5 Dimensionen Grounding, Relevanz, Vollstaendigkeit, Zitatqualitaet und Sprachqualitaet im JSON Modus bei Temperatur 0 bewertet, und Self Preference Bias eliminiert, indem der Richter bewusst auf einem anderen lokalen Modell laeuft als der Generator, mit einer harten Fehlerbehandlung bei fehlendem Judge Modell. Genau dieses Muster, Prompt Varianten systematisch statt subjektiv zu bewerten und Ergebnisse nachvollziehbar zu dokumentieren, deckt sich direkt mit der in der Ausschreibung genannten Aufgabe der Qualitaetsbewertung von LLM Workflows.",
            "In meinem Movie Analytics und ML Pipeline Projekt habe ich eine end to end Pipeline gebaut, die rohe Daten aus einer oeffentlichen API in einen Data Lake zieht und ueber eine 3 stufige Bronze Silver Gold Architektur in ein sauberes, analysebereites Format verarbeitet, vollstaendig automatisiert ohne manuellen Eingriff. Diese Erfahrung, unstrukturierte Rohdaten zuverlaessig in eine strukturierte, produktionsreife Ausgabe zu ueberfuehren, uebertraegt sich direkt auf die in der Ausschreibung beschriebene Dokumentenverarbeitung inklusive Extraktionslogik.",
            "Ich arbeite sicher in Python und habe praktische Erfahrung mit LLM Prompting, REST APIs und Git Workflows. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend, ich hebe es aktiv weiter, und Englisch spreche ich fliessend. Ich kann die Werkstudentenstelle remote zeitnah beginnen und stelle mich gerne in einem persoenlichen Gespraech vor.",
        ],
    },

    # 2. coac GmbH, Berlin und Koeln
    # Werkstudent Softwareentwicklung und KI (m/w/d)
    # Company's own teamtailor.com career page. DE track, native level
    # German required. Python AI solutions, SQL, Linux, SAP BTP.
    # Apply: https://coacgmbh-1728891424.teamtailor.com/jobs/5119036-werkstudent-softwareentwicklung-und-ki-m-w-d
    {
        "folder": "coac Berlin Koeln Werkstudent Softwareentwicklung KI",
        "company": "coac GmbH",
        "lang": "de",
        "location": "Berlin/Koeln, Remote moeglich",
        "apply_link": "https://coacgmbh-1728891424.teamtailor.com/jobs/5119036-werkstudent-softwareentwicklung-und-ki-m-w-d",
        "apply_method": "company-portal",
        "source": "Company Page",
        "german_level": "C2",
        "tag": "Masterstudent Data Science and Analytics | KI Loesungen in Python | Python + SQL + Cloud",
        "role_strip": "Werkstudent, Softwareentwicklung und KI",
        "cl_date": "24. September 2026",
        "cl_subject": "Werkstudent Softwareentwicklung und KI in Berlin und Koeln",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Bau von KI Loesungen in Python sowie im Umgang mit SQL und Cloud Plattformen fuer produktionsnahe Datenverarbeitung. Ich habe ein Multi Agent RAG System vollstaendig in Python gebaut sowie eine per Airflow orchestrierte Pipeline auf Google Cloud, die Batch und Echtzeit Daten automatisch verarbeitet. Sicher im eigenstaendigen Explorieren neuer Technologien und im Uebersetzen von Ideen in lauffaehige Prototypen.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_FLIGHT_DE, P_RAG_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Position als Werkstudent Softwareentwicklung und KI bei der coac GmbH in Berlin und Koeln. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim passt die Aufgabe, KI Loesungen in Python zu entwickeln, neue Technologien zu explorieren und Daten aus verschiedenen Quellen mit Reporting Tools zu analysieren, sehr genau zu dem, was ich in den letzten Monaten praktisch gebaut habe.",
            "In meinem Real Time Flight Tracking Projekt habe ich Python Collectors und PySpark Cleaning Skripte auf Google Cloud gebaut, die Daten aus vier Quellen zu einer sauberen Tabelle mit ueber 128 tausend Datensaetzen zusammenfuehren, und das Gesamtsystem mit Apache Airflow auf GCS gestuetztem Speicher und Dataproc Compute orchestriert, sodass es automatisch alle 15 Minuten ohne manuellen Eingriff aktualisiert wird. Diese Erfahrung, Datenpipelines in Python eigenstaendig zu entwerfen und produktionsnah zu betreiben, deckt sich direkt mit der in der Ausschreibung genannten Systemadministration und Fehlerbehebung.",
            "In meinem Multi Agent RAG Projekt habe ich ein LangGraph basiertes Agentensystem in Python gebaut, das Nutzerfragen ueber eine hybride Retrieval Pipeline beantwortet, mit einem JudgeAgent, der Antworten systematisch bewertet. Diese Erfahrung, KI Loesungen von Grund auf in Python zu entwickeln und dabei staendig neue Technologien und Bibliotheken zu explorieren, ist genau das, was die Ausschreibung mit der Entwicklung von KI Loesungen beschreibt.",
            "Ich arbeite sicher in Python und SQL und habe praktische Erfahrung mit der Linux Konsole sowie mit maschinellem Lernen. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend, ich moechte offen sein, dass ich das in der Ausschreibung genannte muttersprachliche Niveau noch nicht erreicht habe, arbeite aber aktiv daran, und Englisch spreche ich sehr gut. Ich kann die Werkstudentenstelle in Berlin oder Koeln zeitnah beginnen und stelle mich gerne in einem persoenlichen Gespraech vor.",
        ],
    },

    # 3. Reply Deutschland SE, Frankfurt am Main and other German cities
    # Werkstudent AI Business Solutions und Agents (m/w/d)
    # JobTeaser listing, weaker evidence (WebSearch snippets only, direct
    # fetch of both reply.com and jobteaser.com failed this run). DE track.
    # Microsoft Copilot Studio, Power Platform, Agentic AI, AI Bootcamp
    # onboarding, 15 to 20 hours per week.
    # Apply: https://www.jobteaser.com/de/job-offers/21f36cc5-c6b8-42ba-8edf-04bfe3424dca-reply-deutschland-se-werkstudent-ai-business-solutions-agents-m-w-d
    {
        "folder": "Reply Deutschland Werkstudent AI Business Solutions Agents",
        "company": "Reply Deutschland SE",
        "lang": "de",
        "location": "Frankfurt am Main u.a., teilweise Remote",
        "apply_link": "https://www.jobteaser.com/de/job-offers/21f36cc5-c6b8-42ba-8edf-04bfe3424dca-reply-deutschland-se-werkstudent-ai-business-solutions-agents-m-w-d",
        "apply_method": "company-portal",
        "source": "JobTeaser",
        "german_level": "B1",
        "tag": "Masterstudent Data Science and Analytics | Agentische KI und Business Loesungen | Python + LangGraph + Automatisierung",
        "role_strip": "Werkstudent, AI Business Solutions und Agents",
        "cl_date": "24. September 2026",
        "cl_subject": "Werkstudent AI Business Solutions und Agents",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Entwurf agentischer KI Systeme sowie im Uebersetzen von Geschaeftsprozessen in automatisierte Loesungen. Ich habe ein LangGraph Multi Agenten System mit klar abgegrenzten Verantwortlichkeiten gebaut und in einem regulierten Kredit Scoring System technische Ergebnisse in ein Entscheidungsunterstuetzungs Tool fuer Fachanwender uebersetzt. Sicher im Analysieren von Prozessen und im Ableiten sinnvoller Automatisierungsmoeglichkeiten mit KI Agenten.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_CREDITIQ_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit AI Business Solutions und Agents bei der Reply Deutschland SE. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim passt die Aufgabe, gemeinsam mit erfahrenen Consultants und Architekten moderne KI Loesungen zu entwickeln und Geschaeftsprozesse auf sinnvolle Automatisierungsmoeglichkeiten zu untersuchen, sehr genau zu dem, was ich in den letzten Monaten praktisch gebaut habe.",
            "In meinem Multi Agent RAG Projekt habe ich ein LangGraph basiertes Agentensystem mit einem LanguageAgent und Retrieval Agenten entworfen, jeweils mit klar abgegrenzten Verantwortlichkeiten und definiertem Fallback Verhalten, sowie einen JudgeAgent, der Antworten auf 5 Dimensionen systematisch bewertet. Diese Erfahrung, KI Agenten eigenstaendig zu entwerfen und ihre Zusammenarbeit technisch zu verantworten, ist genau das, was der Bau und die Optimierung von KI Agenten in der Ausschreibung braucht.",
            "In meinem CreditIQ Projekt zu regulierbarem Credit Scoring habe ich technische Ergebnisse aus SHAP Analyse und Schwellenwertkalibrierung in ein Streamlit Entscheidungsunterstuetzungs Tool mit einer klartextlichen Erklaerung fuer Fachanwender uebersetzt. Diese Erfahrung, technische KI Arbeit fuer Geschaeftsanwender verstaendlich und nutzbar zu machen, deckt sich direkt mit der in der Ausschreibung genannten Analyse von Geschaeftsprozessen fuer sinnvolle KI und Automatisierungsanwendungen.",
            "Ich arbeite sicher in Python und LangGraph und habe praktische Erfahrung mit Automatisierung und agentischen Systemen. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend, ich hebe es aktiv weiter, und Englisch spreche ich fliessend. Ich kann die Werkstudentenstelle mit 15 bis 20 Stunden pro Woche zeitnah beginnen und stelle mich gerne in einem persoenlichen Gespraech vor.",
        ],
    },
]
