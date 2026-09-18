"""Role configurations for the 18 September 2026 scheduled job search run
(normal top 3 to 5 cut).

Backlog gate check per 14 July 2026 status source of truth rule: Notion
data source fd974369-40b2-48c5-b660-d15256c88f52 returned 6 rows in status
'drafted' at run start (FZI Forschungszentrum Informatik, iLert GmbH,
Temedica GmbH, Charles Real Estate GmbH, SAP Walldorf LLM SE Solutions,
Syneco Trading GmbH). 6 drafted falls under the 8 row floor of the 28 July
2026 yield based reset rule, which allows a normal top 3 to 5 cut.

Reconciliation this run found no real Status drift between applied-log.csv
(208 rows) and the 204 row Notion data source. One apparent mismatch
(Aerzteverband Deutscher Allergologen with and without the umlaut) is the
same known spelling variant flagged in the 16 and 17 September digests,
both sides already read 'applied'. Five CSV rows are exact duplicate
pairs of an already-logged company plus role (Mi-Jack Europe GmbH,
appliedAI Initiative GmbH, KontextWork GbR, Rohde und Schwarz GmbH und Co.
KG Agentic AI Experiments, Estateanfrage Inh. Fabian Kroner); this is a
CSV data quality note only, not Status drift, and is flagged in the
digest rather than fixed, since deduplicating CSV rows is not one of the
two write directions the standing reconciliation rule defines. Separately,
the four roles the 17 September digest flagged as having a Notion
'drafted' Status with no backing CSV row, drafts folder, or git history
(Temedica GmbH, Charles Real Estate GmbH, SAP Walldorf, Syneco Trading
GmbH) are confirmed on this run's checkout to have all 8 deliverables
committed and matching CSV rows: that gap was a branch-timing artifact
(the 17 September run's session forked from main before the 16 September
run's pull request merged), not a real orphaned claim, and is resolved on
the current main.

Search ran via Tavily search plus Tavily extract. WebFetch hit the same
blanket EGRESS_BLOCKED proxy denial reported in the 9 through 17 September
digests (confirmed against jobteaser.com, a Saarland uni JobTeaser mirror,
and stepstone.de), so all verification this run went through Tavily
search and Tavily extract instead, which were both reachable end to end
for the first time since before 9 September. No Indeed MCP tool was
available in this session, consistent with prior runs.

Several leads were found and dropped: BMW Group Werkstudent Cloud
Engineering and AI Integration (Munich, JobTeaser, own careers content)
reads predominantly as AWS and Kubernetes cloud platform engineering with
LLMs and agentic AI mentioned as one bullet among many, not squarely an
AI Engineer role, so it falls outside the 26 August 2026 narrowing and was
dropped as plain cloud engineering; Villeroy and Boch AG (V&B Fliesen
GmbH) Working Student SAP and AI Technologies (Merzig, JobTeaser) reads
predominantly as SAP ABAP development, Process Mining with Celonis, and
supply chain digitalisation with Generative AI listed as one of ten
workstreams, so it was dropped as plain SAP or Data consulting, not AI
Engineer or AI Evaluation flavoured; AXA Konzern AG AI Infrastructure
Engineer im Data Innovation Lab (Cologne, StepStone) is a full time
permanent role (Feste Anstellung, Vollzeit per the listing itself), out of
scope under the standing work types filter (Werkstudent, mandatory
internship, and Masterarbeit only); jemix GmbH Werkstudent AI Engineer
(via a StudySmarter/Talents aggregator mirror) was investigated but the
aggregator's own task description reads as Cloud and Systemintegration
work on a PSA platform, not AI engineering, and no first party jemix
careers page could be reached to confirm the title independently, so it
was dropped under invariant 4 (every write must be auditable) rather than
trusted off a templated-looking third party mirror; Daimler Truck AG
Werkstudententaetigkeit im Bereich Global AI Enablement und Agentic AI
Campaign (Leinfelden-Echterdingen, StepStone) reads as an internal AI
literacy and adoption campaign role (training, communications, change
management) based on Daimler Truck's own public AI upskilling programme
material, not an AI engineering or evaluation build role, so it was
dropped as out of scope; Ambit IQ Praktikant/Werkstudent AI Engineer
(LinkedIn) is based in the Zurich metropolitan area, Switzerland, which is
outside the standing Germany plus remote-in-EU geography filter, so it
was dropped; appliedAI Initiative GmbH Working Student AI Engineering and
Product Development (Munich/Heilbronn) duplicates a company and role
combination already logged as 'rejected'.

Four roles cleared verification: a live posting fetched directly (three
via each company's own careers site or an official partner university
JobTeaser feed, one via a job aggregator that mirrors the employer's own
listing verbatim with a confirmed still-active apply link), and a clean
dedup check against applied-log.csv and Notion (208 CSV rows, 204 Notion
rows, full company plus role comparison run during this run's
reconciliation step).

Platform mix this run:
  - Company Page, 2 (Stiftung Polytechnische Gesellschaft Frankfurt,
    sptg.de; Atruvia AG, karriere.atruvia.de, also mirrored on jobware.de
    and a Hochschule Worms/Ludwigshafen JobTeaser-style Stellenmarkt feed)
  - StepStone, 1 (disruptive GmbH, also mirrored on join.com and an
    aggregator; original discovery via a StepStone werkstudent-in-ai
    listing page)
  - Company Page, 1 (Muenchener Verein Versicherungsgruppe, own
    stellenangebote-innendienst careers page; also listed on StepStone)
  - Xing, JobTeaser, LinkedIn searched this run via Tavily; JobTeaser and
    LinkedIn surfaced only already-logged, out of scope, or dropped leads
    per the paragraph above; Indeed not used, no MCP tool available and
    Tavily based Indeed search returned nothing new in scope.

Freshness order (all four fall in the single Germany tier, so ranked by
recency then Best for overlap):
  1. Atruvia AG, Aschheim and Karlsruhe, Werkstudent Generative AI /
     Agentic AI (m/w/d), DE track, confirmed live via jobware.de and a
     Hochschule Worms/Ludwigshafen Stellenmarkt mirror both showing an
     "Aktualitaet" of 10.09.2026, so posted 8 days before this run.
  2. disruptive GmbH, Munich, Werkstudent:in AI Engineering (m/w/d), DE
     track, confirmed live via join.com (disruptive's own ATS) and a
     StepStone aggregator listing marked "vor 5 Tagen".
  3. Muenchener Verein Versicherungsgruppe, Munich, Werkstudent (m/w/d)
     Conversational AI, DE track, confirmed live via the company's own
     stellenangebote-innendienst careers page; a StepStone mirror of the
     same posting carries an original post date of 5 August 2026, so this
     is an older but still open posting, ranked last on recency among the
     four.
  4. Stiftung Polytechnische Gesellschaft Frankfurt am Main, Frankfurt,
     Werkstudent/in AI Engineering (w/m/d), DE track, confirmed live via
     the foundation's own sptg.de careers page; no explicit post date was
     shown on the page itself, so freshness could not be pinned to a
     specific day, only confirmed currently live and listed among "Aktuelle
     Stellenangebote".

Language track per 20 July 2026 language match hard rule (posting body
language IS deliverable language): all four postings are written entirely
in German with no English requirement stated -> DE track for all four.

Dedup check against applied-log.csv and Notion (208 CSV rows, 204 Notion
rows, full company plus role comparison run during this run's
reconciliation step): Stiftung Polytechnische Gesellschaft Frankfurt,
disruptive GmbH, and Atruvia AG are all entirely new companies, never
previously logged. Muenchener Verein Versicherungsgruppe has one prior
row logged (Werkstudent, Data Analytics und KI, status 'rejected'), which
is a different role at the same company (Data Analytics und KI versus
Conversational AI), so this is not a duplicate under the standing company
plus role case insensitive match rule.

Apply Method left unset in Notion for all four roles pending OpenClaw's
platform-native versus company-portal determination at submission time;
all four read as company-owned careers domains from the scraped content,
so all four are the expected company-portal shape, but the final call is
OpenClaw's per the standing scope split.

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


CONFIGS_18SEP = [
    # 1. Stiftung Polytechnische Gesellschaft Frankfurt am Main
    # Werkstudent/in AI Engineering (w/m/d)
    # Company career page (sptg.de). DE track. Weiterentwicklung und
    # Betreuung der cloudbasierten KI-Wissensplattform der Stiftung.
    # Apply: https://sptg.de/service/karriere
    {
        "folder": "Stiftung Polytechnische Gesellschaft Frankfurt Werkstudent AI Engineering",
        "company": "Stiftung Polytechnische Gesellschaft Frankfurt am Main",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | KI Wissensplattformen und RAG Evaluation | Python + LangGraph + Cloud",
        "role_strip": "Werkstudent/in AI Engineering",
        "cl_date": "18. September 2026",
        "cl_subject": "Werkstudent/in AI Engineering in Frankfurt am Main",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau und Betrieb cloudbasierter KI Wissensplattformen. Ich habe ein Multi Agent RAG System mit hybrider BM25 und Dense Retrieval sowie einem unabhaengigen LLM as Judge Modell gebaut, das auf einer gemeinsamen mehrsprachigen Vektorbasis Deutsch und Englisch bedient, sowie eine vollautomatisierte Cloud Pipeline, die ohne manuellen Eingriff laeuft. Sicher im Weiterentwickeln und Betreuen produktiver KI Plattformen in Python.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_MOVIE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich als Werkstudent/in AI Engineering bei der Stiftung Polytechnische Gesellschaft Frankfurt am Main zur Weiterentwicklung und Betreuung der cloudbasierten KI Wissensplattform der Stiftung. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim passt diese Aufgabe sehr genau zu dem, was ich in den letzten Monaten praktisch gebaut habe.",
            "In meinem Multi Agent RAG Projekt habe ich eine englischsprachige Wissensplattform ueber einen 14 Dokumente Corpus so erweitert, dass Deutsch und Englisch auf einer gemeinsamen mehrsprachigen Vektorbasis paraphrase multilingual MiniLM L12 v2 bedient werden, sodass eine deutsche Anfrage englische Quellen findet und end to end auf Deutsch beantwortet wird. Diese Erfahrung, eine bestehende Wissensplattform ohne Duplizierung des Corpus mehrsprachig und produktionsreif weiterzuentwickeln, deckt sich direkt mit der Aufgabe, die cloudbasierte KI Wissensplattform der Stiftung weiterzuentwickeln und zu betreuen.",
            "In meinem Movie Analytics und ML Pipeline Projekt habe ich eine end to end Batch Pipeline mit einer 3 stufigen Bronze Silber Gold Medallion Architektur in BigQuery auf Cloud Run gebaut, die vollautomatisch per Cloud Scheduler laeuft und 0 manuelle Eingriffe benoetigt, abgesichert mit einem Least Privilege Service Account und Secret Manager. Diese Erfahrung, eine Cloud Plattform zuverlaessig und sicher im laufenden Betrieb zu halten statt sie nur einmalig zu bauen, uebertraegt sich direkt auf die Betreuung der KI Wissensplattform der Stiftung im Tagesbetrieb.",
            "Ich arbeite sicher in Python und habe praktische Erfahrung mit RAG Systemen, LLM Evaluation und Cloud Betrieb. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend, ich hebe es aktiv weiter, und Englisch spreche ich fliessend. Ich kann als Werkstudent in Frankfurt am Main zeitnah beginnen und freue mich auf ein persoenliches Gespraech.",
        ],
    },

    # 2. disruptive GmbH, Munich
    # Werkstudent:in AI Engineering (m/w/d)
    # StepStone, also disruptive's own join.com ATS page. DE track. Young
    # AI consultancy building smart software solutions for Mittelstand
    # clients across more than 50 projects.
    # Apply: https://join.com/companies/disruptive-muenchen/16665740-werkstudent-in-ai-engineering-m-w-d
    {
        "folder": "disruptive Muenchen Werkstudent AI Engineering",
        "company": "disruptive GmbH",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | KI Loesungen fuer den Mittelstand | Python + LangGraph + Evaluation",
        "role_strip": "Werkstudent:in AI Engineering",
        "cl_date": "18. September 2026",
        "cl_subject": "Werkstudent:in AI Engineering in Muenchen",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Bauen smarter, produktionsreifer KI Softwareloesungen fuer reale Geschaeftsprozesse. Ich habe ein Multi Agent RAG System mit LangGraph und unabhaengiger LLM as Judge Evaluation gebaut sowie eine vollautomatisierte vierstufige Pipeline mit klaren Gate Checks orchestriert, die ohne manuellen Eingriff laeuft. Sicher im Uebersetzen von Kundenanforderungen in pragmatische KI Loesungen in Python.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_FLIGHT_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich als Werkstudent:in AI Engineering bei disruptive in Muenchen, um Mittelstandskunden dabei zu unterstuetzen, die Chancen von KI Technologien in langfristigen Unternehmenserfolg zu ueberfuehren. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim passt die Entwicklung smarter Softwareloesungen sehr genau zu dem, was ich in den letzten Monaten praktisch gebaut habe.",
            "In meinem Multi Agent RAG Projekt habe ich ein LangGraph basiertes Multi Agenten System mit einem LanguageAgent, Retrieval Agenten und einem JudgeAgent entworfen, jeder mit klar begrenzter Verantwortung und definiertem Fallback Verhalten, inklusive eines Hard Failure bei fehlendem Judge Modell, damit eine stille Regression nicht unbemerkt bleibt. Diese Erfahrung, KI Architekturen eigenstaendig zu entwerfen und pragmatisch auf reale Anforderungen zuzuschneiden, ist genau das, was das Uebersetzen von Mittelstandsproblemen in smarte KI Loesungen braucht.",
            "In meinem Real Time Flight Tracking Projekt habe ich das gesamte System mit Apache Airflow auf GCS gestuetztem Speicher und Dataproc Compute orchestriert, sodass Batch und Echtzeit Schichten automatisch alle 15 Minuten ohne manuellen Eingriff aktualisiert werden. Diese Erfahrung, eine KI Loesung zuverlaessig im produktiven Betrieb statt nur im Prototyp laufen zu lassen, uebertraegt sich direkt auf den Anspruch, dass Technologie bei disruptive kein Selbstzweck bleibt, sondern gezielt dort zum Einsatz kommt, wo sie einen echten Hebel darstellt.",
            "Ich arbeite sicher in Python und habe praktische Erfahrung mit generativer KI, Agentensystemen und Prompt Engineering. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend, ich hebe es aktiv weiter, und Englisch spreche ich fliessend. Ich kann als Werkstudent in Muenchen zeitnah beginnen und freue mich auf ein persoenliches Gespraech.",
        ],
    },

    # 3. Atruvia AG, Aschheim and Karlsruhe
    # Werkstudent Generative AI / Agentic AI (m/w/d)
    # Company career page (karriere.atruvia.de), also mirrored on
    # jobware.de and a Hochschule Worms/Ludwigshafen Stellenmarkt feed. DE
    # track. Atruvia is the IT service provider for the German
    # Volksbanken Raiffeisenbanken cooperative banking group; role works
    # on agentenbasierte KI Loesungen (agent based AI solutions) from
    # technical concept through implementation.
    # Apply: https://www.jobware.de/job/werkstudent-generative-ai-agentic-ai-m-w-d-064084499
    {
        "folder": "Atruvia Aschheim Karlsruhe Werkstudent Generative AI Agentic AI",
        "company": "Atruvia AG",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | Agentenbasierte KI im Bankenkontext | Python + LangGraph + Fairness Evaluation",
        "role_strip": "Werkstudent Generative AI / Agentic AI",
        "cl_date": "18. September 2026",
        "cl_subject": "Werkstudent Generative AI / Agentic AI in Aschheim oder Karlsruhe",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Bauen agentenbasierter KI Loesungen sowie im Evaluieren von KI Systemen fuer den regulierten Finanzsektor. Ich habe ein Multi Agent RAG System mit LangGraph und unabhaengiger LLM as Judge Evaluation gebaut sowie ein fairness by design Kreditscoring System, das die Anforderungen des EU AI Act und der DSGVO erfuellt. Sicher im Uebersetzen technischer Konzepte agentenbasierter KI in belastbare, auditierbare Umsetzungen in Python.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_CREDITIQ_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich als Werkstudent Generative AI / Agentic AI bei der Atruvia AG in Aschheim oder Karlsruhe, um an agentenbasierten KI Loesungen von der technischen Konzeption bis zur Umsetzung mitzuwirken. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim passt diese Aufgabe sehr genau zu dem, was ich in den letzten Monaten praktisch gebaut habe.",
            "In meinem Multi Agent RAG Projekt habe ich ein LangGraph basiertes Multi Agenten System mit einem JudgeAgent implementiert, der Antworten in 5 Dimensionen bewertet und Self Preference Bias eliminiert, indem der Richter auf einem anderen lokalen Modell laeuft als der Generator, mit einem self_judged Flag in jedem Report und einem Hard Failure bei fehlendem Judge Modell. Diese Erfahrung, agentenbasierte KI Systeme von der Konzeption bis zur belastbaren Evaluation eigenstaendig umzusetzen, deckt sich direkt mit der Aufgabe im Team Generative AI und Agentic AI.",
            "In meinem CreditIQ Projekt habe ich ein Kreditscoring Modell im regulierten Finanzumfeld mit AIF360 Mitigation und Schwellenwert Kalibrierung wieder in Einklang mit dem EU AI Act und dem AGG gebracht, die Disparate Impact Ratio von 0.79 auf 0.88 angehoben, und ein Streamlit Entscheidungsunterstuetzungstool mit vollstaendiger regulatorischer Dokumentation ausgeliefert, das die Anforderungen aus DSGVO Artikel 22 und EU AI Act Artikel 14 zum Human in the Loop erfuellt. Diese Erfahrung, KI Loesungen im regulierten Bankenumfeld auditierbar und belastbar zu gestalten, uebertraegt sich direkt auf agentenbasierte KI Loesungen im genossenschaftlichen Bankensektor.",
            "Ich arbeite sicher in Python und habe praktische Erfahrung mit Agentensystemen, generativer KI und regulatorisch belastbarer Evaluation. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend, ich hebe es aktiv weiter, und Englisch spreche ich fliessend. Ich kann als Werkstudent in Aschheim oder Karlsruhe zeitnah beginnen und freue mich auf ein persoenliches Gespraech.",
        ],
    },

    # 4. Muenchener Verein Versicherungsgruppe, Munich
    # Werkstudent (m/w/d) Conversational AI
    # Company career page (stellenangebote-innendienst), also listed on
    # StepStone. DE track. Supports conception, design and implementation
    # of Conversational AI solutions (chat and voice bots) for customer
    # and sales communication, including evaluation and integration of
    # LLMs and prompt engineering.
    # Apply: https://www.muenchener-verein.de/unternehmen/karriere-ausbildung/stellenangebote-innendienst
    {
        "folder": "Muenchener Verein Muenchen Werkstudent Conversational AI",
        "company": "Muenchener Verein Versicherungsgruppe",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | Conversational AI und LLM Evaluation | Python + Multilinguale RAG Systeme",
        "role_strip": "Werkstudent, Conversational AI",
        "cl_date": "18. September 2026",
        "cl_subject": "Werkstudent (m/w/d) Conversational AI in Muenchen",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Konzipieren und Evaluieren dialogbasierter KI Systeme in mehrsprachigem Deutsch und Englisch Kontext. Ich habe ein Multi Agent RAG System mit einem LanguageAgent fuer konsistente Sprachausgabe sowie einer LLM as Judge Evaluation ueber 5 Qualitaetsdimensionen gebaut. Sicher im Uebersetzen fachlicher Anforderungen in smarte Dialogloesungen und in der Recherche und Integration aktueller LLM Entwicklungen in Python.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_FLIGHT_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich als Werkstudent (m/w/d) Conversational AI beim Muenchener Verein in Muenchen, um bei der Konzeption, dem Design und der Implementierung von Conversational AI Loesungen fuer die Kunden und Vertriebskommunikation mitzuwirken. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim passt diese Aufgabe sehr genau zu dem, was ich in den letzten Monaten praktisch gebaut habe.",
            "In meinem Multi Agent RAG Projekt habe ich einen LanguageAgent gebaut, der die Sprachauswahl zentral mit einer Konfidenzschwelle steuert und die Ausgabesprache an jeden nachgelagerten Agenten weitergibt, sodass ein System konsistent auf Deutsch oder Englisch antwortet statt sprachlich zu driften. Diese Erfahrung, dialogbasierte Systeme sprachlich konsistent und nachvollziehbar zu steuern, deckt sich direkt mit der Aufgabe, smarte Dialogloesungen fuer die Kunden und Vertriebskommunikation zu entwickeln.",
            "Ausserdem habe ich in demselben Projekt eine LLM as Judge Evaluation implementiert, die Antworten in 5 Dimensionen bewertet, darunter Sprachqualitaet und Relevanz, im JSON Modus bei Temperatur 0 mit einem Hard Failure bei fehlendem Judge Modell. Diese Erfahrung, LLMs systematisch statt subjektiv zu evaluieren und in eine bestehende Systemlandschaft zu integrieren, uebertraegt sich direkt auf die Recherche und Evaluation aktueller Large Language Model Entwicklungen fuer Ihre Conversational AI Loesungen.",
            "Ich arbeite sicher in Python und habe praktische Erfahrung mit Prompt Engineering, LLM Integration und mehrsprachigen KI Anwendungen im Unternehmenskontext. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend, ich hebe es aktiv weiter, und Englisch spreche ich fliessend. Ich kann als Werkstudent in Muenchen zeitnah beginnen und freue mich auf ein persoenliches Gespraech.",
        ],
    },
]
