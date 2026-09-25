"""Role configurations for the 25 September 2026 scheduled job search run
(normal top 3 cut).

Backlog gate check per 14 July 2026 status source of truth rule: Notion
data source fd974369-40b2-48c5-b660-d15256c88f52 returned 6 rows in status
'drafted' at run start (Atos, Sopra Steria Custom Software Solutions GmbH,
COBACK, coac GmbH, PRODIGY Consulting GmbH, Reply Deutschland SE). 6 falls
well under the 8 row floor of the 28 July 2026 yield based reset rule,
which allows a normal top 3 to 5 cut.

Critical reconciliation finding, not a search result: all 6 of those
Notion drafted rows (created 2026-09-23 and 2026-09-24) have no
corresponding folder anywhere under drafts/ in this repo, and no digest
or git commit exists for either date. This is the exact false-drafted
risk invariant #3 warns about: Notion says drafted, but no CV or cover
letter was ever rendered or committed for any of the six. This run does
NOT attempt to silently reconstruct those six from Notion's Notes field
alone (insufficient original posting detail to tailor safely); it flags
them in Job_Digest_2026-09-25.md for Rah's decision and adds mirroring
CSV rows so applied-log.csv and Notion stay in sync on status, while
being explicit in the digest that the underlying files are still missing.

Reconciliation also found 5 CSV rows still reading 'drafted' from the 22
Sep run while Notion had already moved them on: Syneco Trading GmbH
Masterarbeit (both the 16 Sep Xing row and the 22 Sep company-portal row)
to 'applied', Web Computing GmbH to 'applied', Modern Drive Technology
GmbH to 'applied', and BLACKFIELD AI to 'rejected'. All five corrected in
the CSV to match Notion per invariant #1.

Search ran via WebSearch and WebFetch across LinkedIn, StepStone, Xing,
JobTeaser and company career pages (Tavily MCP failed to connect again
this run; no Indeed MCP tool was available in this session). Search
conditions were unusually poor tonight: a large number of promising leads
resolved to dead links (HTTP 410 Gone or "vacancy no longer available")
on verification, including CognitX AI GmbH (Darmstadt, posting dated
November 2025, both known apply links now dead), Ponturo Consulting AG
(Werkstudent AI Engineer, multiple cities, all known apply mirrors dead),
BMW Group Werkstudent Agentic AI (Munich, "vacancy no longer available"),
Dussmann AI Werkstudent (Berlin, StepStone returned 503 on every attempt),
and the Mercedes-Benz AI Agents and Robotics Platform Werkstudent listing
(arbeitsagentur.de mirror returned 410). All five were dropped under
invariant #4 (every write must be auditable) rather than drafted on stale
information. This tightened the top cut from a possible 4 to 5 down to 3
verified, currently live roles.

Three roles cleared verification: a live posting fetched directly, a
confirmed apply path, and a clean dedup check against applied-log.csv and
Notion (226 CSV rows including the 6 mirrored orphan rows, 6 Notion
drafted rows plus historical rows, at run start).

Platform mix this run:
  - StepStone, 2 (retorio GmbH Munich, KontextWork GbR Hannover)
  - Company Page, 1 (KWS SAAT SE and Co KGaA, Einbeck, jobs.kws.com)
  - LinkedIn, Xing, JobTeaser, Indeed surfaced no new in-scope,
    verifiable, non-duplicate postings this run beyond the dead links
    listed above (Indeed also not used, no MCP tool available).

Freshness order (all three fall in the single Germany tier, ranked by
recency then Best for overlap):
  1. KWS SAAT SE and Co KGaA, Einbeck, Working Student Global IT AI and
     LLM Solutions, EN track, posted 19 September 2026 and updated within
     hours of this run per the source listing, the freshest of the three.
  2. retorio GmbH, Munich, Working Student AI Engineer Agentic Systems,
     EN track, confirmed live via direct StepStone fetch.
  3. KontextWork GbR, Hannover, Werkstudent KI Engineer Generative KI and
     LLM, DE track, confirmed live via direct StepStone fetch.

Language track per 20 July 2026 language match hard rule (posting body
language IS deliverable language):
  1. retorio posting body written entirely in English, no German
     requirement stated -> EN track.
  2. KontextWork posting body written entirely in German -> DE track.
  3. KWS SAAT posting body written in English and explicitly accepts
     "very good communication skills in either German or English" ->
     EN track, since the posting content itself is English.

German level flags (accept German listings per master-projects.md, flag
the bar against Rah's actual B1 in progress level, not a filter):
  - retorio states no German requirement at all.
  - KontextWork states no explicit German level bar in the posting text,
    but the German language listing and Hannover client facing context
    imply working German is expected; flagged for Rah's own judgement.
  - KWS SAAT explicitly accepts English or German, either is acceptable,
    the softest bar of the three.

Dedup check against applied-log.csv and Notion (226 CSV rows at run
start after this run's reconciliation additions): retorio GmbH,
KontextWork GbR, and KWS SAAT SE and Co KGaA are all entirely new
companies, never previously logged under any role.

Apply Method set directly in role_configs where determinable from the
posting: retorio GmbH (StepStone Schnelle Bewerbung, platform-native, in
OpenClaw's scope), KontextWork GbR (StepStone Schnelle Bewerbung,
platform-native, in OpenClaw's scope), KWS SAAT SE and Co KGaA
(jobs.kws.com own careers portal, company-portal, out of OpenClaw's
platform-native scope, Rah to submit manually).

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


CONFIGS_25SEP = [
    # 1. retorio GmbH, Munich
    # Working Student: AI Engineer, Agentic Systems (m/f/d), ~20 hrs/week, 5 months
    # StepStone Schnelle Bewerbung, platform-native. EN track. Agentic
    # systems, tool calling, MCP, eval datasets, A/B testing, GCP deploy.
    # Apply: https://www.stepstone.de/stellenangebote--Working-Student-AI-Engineer-Agentic-Systems-m-f-d-Munich-retorio-GmbH--14400893-inline.html
    {
        "folder": "retorio Muenchen Working Student AI Engineer Agentic Systems",
        "company": "retorio GmbH",
        "lang": "en",
        "location": "Munich",
        "apply_link": "https://www.stepstone.de/stellenangebote--Working-Student-AI-Engineer-Agentic-Systems-m-f-d-Munich-retorio-GmbH--14400893-inline.html",
        "apply_method": "platform-native",
        "source": "StepStone",
        "german_level": "none",
        "tag": "Data Science Master's Student | Agentic AI Systems and Evaluation | Python + LangGraph + Eval Tooling",
        "role_strip": "Working Student, AI Engineer, Agentic Systems",
        "cl_date": "25 September 2026",
        "cl_subject": "Working Student, AI Engineer, Agentic Systems in Munich",
        "profile": "Master's student in Data Science and Analytics at SRH Heidelberg, based in Mannheim, with hands on experience designing agentic systems and holding them to a rigorous evaluation bar rather than shipping on intuition. I built a multi agent RAG system in LangGraph with tool calling, retrieval, and an independent LLM as Judge that scores every answer on 5 dimensions in JSON mode at temperature 0, plus a cloud native batch pipeline deployed on GCP Cloud Run with a fully automated Cloud Scheduler trigger. Comfortable across Python, backend APIs, and cloud deployment end to end.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_RAG_EN, P_MOVIE_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_NVIDIA, CERT_AWS, CERT_GOOGLE],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am writing to apply for the Working Student position in AI Engineer, Agentic Systems at retorio in Munich. As a Master's student in Data Science and Analytics at SRH Heidelberg based in Mannheim, the mix of designing agentic systems with tool calling and retrieval and holding them to a rigorous evaluation bar with eval datasets and A/B testing maps very closely to the projects I have shipped in the last several months.",
            "In my Multi Agent RAG project I built a full LangGraph orchestrated agent system with tool calling, retrieval, and structured outputs that answers policy questions end to end. I implemented a JudgeAgent that scores answers on 5 dimensions in JSON mode at temperature 0, and eliminated self preference bias by running the judge on a different local model from the generator, plus an EvalAgent computing 5 retrieval metrics and 4 generation metrics into JSON and Markdown reports. That same discipline, measuring an agentic system honestly rather than trusting it by default, is exactly what a rigorous evaluation loop with eval datasets and observability tooling needs.",
            "In my Movie Analytics and ML Pipeline project I built an end to end batch pipeline on GCP that pulls data into a GCS data lake and processes it through a 3 tier Bronze Silver Gold medallion architecture in BigQuery on Cloud Run, running on a fully automated Cloud Scheduler trigger with 0 manual interventions. That experience with containerized GCP deployment, monitoring, and cost aware scaling maps directly onto the DevOps ownership side of building agentic systems in production.",
            "I work comfortably in Python, backend APIs, and cloud deployment on GCP, and I am currently on Cloud Run, container based deployment, and CI and CD. I hold the NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations, and Google Data Analytics certificates and was recognised as a Finalist of the USAII Global AI Hackathon 2026 at Graduate Level. I am fluent in English and B1 in progress in German. As a working student I can join in Munich for around 20 hours a week immediately and would welcome the chance to discuss how I could contribute to your agentic systems team.",
        ],
    },

    # 2. KontextWork GbR, Hannover
    # Werkstudent:in KI-Engineer, Generative KI und LLM (m/w/d), 16-20 Std/Woche
    # StepStone Schnelle Bewerbung, platform-native. DE track. RAG systems,
    # LLM prompting, Drupal Wiki AI integration for business clients.
    # Apply: https://www.stepstone.de/stellenangebote--Werkstudent-in-KI-Engineer-Generative-KI-LLM-m-w-d-Hanover-KontextWork-GbR-Inh-Sven-Reher-und-Andre-Ulrich--13730672-inline.html
    {
        "folder": "KontextWork Hannover Werkstudent KI Engineer Generative KI LLM",
        "company": "KontextWork GbR",
        "lang": "de",
        "location": "Hannover",
        "apply_link": "https://www.stepstone.de/stellenangebote--Werkstudent-in-KI-Engineer-Generative-KI-LLM-m-w-d-Hanover-KontextWork-GbR-Inh-Sven-Reher-und-Andre-Ulrich--13730672-inline.html",
        "apply_method": "platform-native",
        "source": "StepStone",
        "german_level": "B1",
        "tag": "Masterstudent Data Science and Analytics | RAG Systeme und LLM Integration | Python + LangGraph + Prompting",
        "role_strip": "Werkstudent KI Engineer, Generative KI und LLM",
        "cl_date": "25. September 2026",
        "cl_subject": "Werkstudent KI Engineer, Generative KI und LLM in Hannover",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau von RAG Systemen und der Integration von LLMs in bestehende Geschaeftsprozesse. Ich habe ein Multi Agent RAG System mit hybrider BM25 plus Dense Retrieval Pipeline und einem unabhaengigen LLM as Judge Modell gebaut sowie in CreditIQ ein reguliertes Entscheidungsunterstuetzungssystem mit einer klartextlichen LLM generierten Erklaerung ausgeliefert. Sicher in Python, Prompting Techniken und im Uebersetzen von Geschaeftswissen in KI gestuetzte Loesungen.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_CREDITIQ_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit als KI Engineer im Bereich Generative KI und LLM bei der KontextWork GbR in Hannover. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim passt die Aufgabe, KI Loesungen im Geschaeftsumfeld zu evaluieren, zu konzipieren und zu entwickeln sowie RAG Systeme aufzubauen, sehr genau zu dem, was ich in den letzten Monaten praktisch gebaut habe.",
            "In meinem Multi Agent RAG Projekt habe ich eine hybride BM25 plus Dense Retrieval Pipeline mit einem LangGraph orchestrierten Agentensystem gebaut, das Nutzerfragen end to end beantwortet, und einen JudgeAgent implementiert, der Antworten auf 5 Dimensionen im JSON Modus bei Temperatur 0 bewertet. Diese Erfahrung, RAG Systeme von der Retrieval Schicht bis zur systematischen Qualitaetspruefung selbststaendig zu bauen, deckt sich direkt mit der in der Ausschreibung genannten Aufgabe, RAG Systeme aufzubauen und Kunden bei der Nutzung ihres Geschaeftswissens ueber KI zu unterstuetzen.",
            "In CreditIQ habe ich ein reguliertes Kredit Scoring System entwickelt und als Streamlit Entscheidungsunterstuetzungs Tool mit einer klartextlichen LLM generierten Erklaerung fuer den Endnutzer ausgeliefert, sodass eine fachfremde Person die Modellentscheidung nachvollziehen kann. Diese Erfahrung, komplexe KI Ergebnisse in verstaendliche Sprache fuer Geschaeftsanwender zu uebersetzen, ist genau das, was die Integration von KI in bestehende Wissenssysteme fuer Kunden braucht.",
            "Ich arbeite sicher in Python, JavaScript und habe praktische Erfahrung mit Prompting Techniken und analytischem Denken bei komplexen Ablaeufen. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend, und Englisch spreche ich fliessend. Ich kann die Werkstudentenstelle mit 16 bis 20 Stunden pro Woche zeitnah beginnen und stelle mich gerne in einem persoenlichen Gespraech vor.",
        ],
    },

    # 3. KWS SAAT SE and Co KGaA, Einbeck
    # Working Student Global IT (m/f/d), Focus on AI and LLM Solutions,
    # 20 hrs/week during studies. jobs.kws.com own careers portal,
    # company-portal. EN track. RAG and GraphRAG, response quality
    # evaluation, systematic model evaluations and benchmarks.
    # Apply: https://jobs.kws.com/job/Einbeck-Working-Student-Global-IT-%28mfd%29-Focus-on-AI-&-LLM-Solutions-Lowe/1440976433/
    {
        "folder": "KWS SAAT Einbeck Working Student Global IT AI LLM Solutions",
        "company": "KWS SAAT SE and Co KGaA",
        "lang": "en",
        "location": "Einbeck",
        "apply_link": "https://jobs.kws.com/job/Einbeck-Working-Student-Global-IT-%28mfd%29-Focus-on-AI-&-LLM-Solutions-Lowe/1440976433/",
        "apply_method": "company-portal",
        "source": "Company Page",
        "german_level": "none",
        "tag": "Data Science Master's Student | RAG Evaluation and LLM Benchmarking | Python + LangGraph + Eval Frameworks",
        "role_strip": "Working Student, Global IT, AI and LLM Solutions",
        "cl_date": "25 September 2026",
        "cl_subject": "Working Student, Global IT, AI and LLM Solutions in Einbeck",
        "profile": "Master's student in Data Science and Analytics at SRH Heidelberg, based in Mannheim, with hands on experience building RAG pipelines and holding generative AI outputs to a systematic, auditable evaluation standard rather than a subjective one. I built a multi agent RAG system with an independent LLM as Judge that scores answers on 5 dimensions in JSON mode at temperature 0, and a regulated credit scoring system that raised a fairness metric from a failing 0.79 to a compliant 0.88 through SHAP driven subgroup analysis. Comfortable across Python, RAG architectures, and designing evaluation frameworks for non deterministic AI systems.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_RAG_EN, P_CREDITIQ_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_NVIDIA, CERT_AWS, CERT_GOOGLE],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am writing to apply for the Working Student position in Global IT with a focus on AI and LLM Solutions at KWS SAAT in Einbeck. As a Master's student in Data Science and Analytics at SRH Heidelberg based in Mannheim, the mix of contributing to RAG use cases with response quality evaluation and assisting with systematic model evaluations and benchmarks maps very closely to the projects I have shipped in the last several months.",
            "In my Multi Agent RAG project I built a hybrid BM25 plus dense retrieval pipeline with an independent LLM as Judge that scores every answer on 5 dimensions in JSON mode at temperature 0, and eliminated self preference bias by running the judge on a different local model from the generator. An EvalAgent then computes 5 retrieval metrics and 4 generation metrics into JSON and Markdown reports on a labelled evaluation set. That exact discipline, measuring RAG response quality systematically rather than trusting outputs by default, is what a response quality evaluation workflow for RAG and GraphRAG use cases needs.",
            "In CreditIQ, a regulated credit scoring project, I used SHAP driven subgroup analysis to expose a hidden intersectional bias and raised the Disparate Impact ratio from a failing 0.79 to a compliant 0.88 without gutting predictive quality, then documented the fairness accuracy trade off as a defensible decision. That habit of running systematic model evaluations and benchmarks on quality and fairness before anything reaches a business user maps directly onto assisting with model evaluations and benchmarks focused on quality, security, and performance.",
            "I work comfortably in Python, RAG architectures, and Git, and I hold a genuine interest in agent frameworks, embeddings, and prompt engineering. I hold the NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations, and Google Data Analytics certificates and was recognised as a Finalist of the USAII Global AI Hackathon 2026 at Graduate Level. I am fluent in English and B1 in progress in German. As a working student I can join for around 20 hours a week during the semester and would welcome the chance to discuss how I could contribute to your Global IT team.",
        ],
    },
]
