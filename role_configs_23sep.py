"""Role configurations for the 23 September 2026 scheduled job search run
(normal top 3 to 5 cut).

Backlog gate check per 14 July 2026 status source of truth rule: Notion
data source fd974369-40b2-48c5-b660-d15256c88f52 returned 0 rows in status
'drafted' at run start. 0 drafted falls well under the 8 row floor of the
28 July 2026 yield based reset rule, which allows a normal top 3 to 5 cut.

Reconciliation this run compared all 219 CSV rows against all 214 valid
Notion rows (one blank placeholder row, "New CVs now", excluded as not a
real job row) and found 5 drift rows where Notion had moved past
'drafted' (two to 'applied' for the same duplicate Syneco Trading GmbH
Masterarbeit row that exists twice in the CSV under different dates and
sources, plus Web Computing GmbH and Modern Drive Technology GmbH to
'applied', and BLACKFIELD AI to 'rejected') while the CSV still said
'drafted'; all 5 were corrected in the CSV to match Notion per invariant
#1. One apparent mismatch (Arzteverband Deutscher Allergologen with and
without the umlaut) is a spelling/transcription variant only, both sides
already read 'applied', no action needed. After the fix, 0 CSV rows carry
status 'drafted', matching the 0 count in Notion.

Search ran via WebSearch and WebFetch across LinkedIn, StepStone, JobTeaser
and company career pages (Tavily MCP again failed to connect this run,
consistent with every prior run's digest note; no Indeed MCP tool was
available in this session either, so Indeed was not used). Xing's own
domain (www.xing.com) actively refused the WebFetch tool this run
("Claude Code is unable to fetch from www.xing.com"), a harder failure
than the usual "resolves back to StepStone mirrors" pattern noted in
recent digests, so Xing is flagged fully unreachable this run.

This was an unusually difficult search session: a large majority of leads
that surfaced via WebSearch turned out to be dead links when checked
directly, returning HTTP 410 Gone, 404 Not Found, or an explicit "Sorry,
this position has been filled" page. Every lead below was verified with a
direct fetch before being drafted; every lead that failed verification is
listed in the dropped section with the specific failure.

Leads found and dropped as unverifiable, filled, or duplicate:
  - Ponturo Consulting AG Werkstudent AI Engineer (multiple cities): the
    only detailed source (a studysmarter.de mirror) returned 410 Gone: the
    listing has expired.
  - Jemix GmbH Werkstudent AI Engineer, Berlin: a StepStone listing
    surfaced but returned HTTP 503 on direct fetch; the company's own
    Personio job board (jemix-gmbh.jobs.personio.de) lists only an
    apprenticeship, a sales manager role, and IT support, no AI Engineer
    or AI agent role among current openings. Dropped as unverifiable.
  - CognitX AI GmbH AI/LLM Engineering Werkstudent, Darmstadt: both
    sources found (join.com and arbeitnow.com) returned HTTP 410 Gone.
  - SAP Working Student (f/m/d) for AI Agent Research, and the paired
    Working Student for AI Agent Research and Vibe Coding, both Karlsruhe:
    both job IDs on jobs.sap.com show "Sorry, this position has been
    filled."
  - SAP Working Student (f/m/d) AI Engineering & Data Science, Walldorf:
    jobs.sap.com shows "Sorry, this position has been filled."
  - appliedAI Initiative GmbH Working Student, Agentic AI & Automation
    (Heilbronn/Munich): the company's own careers page returned 404, its
    Personio listing returned 404, and the arbeitnow.com mirror returned
    410 Gone across three separate checks. Dropped as unverifiable; note
    this is a different role from the appliedAI Working Student, AI
    Engineering and Product Development role already logged in Notion as
    'rejected'.
  - CHECK24 Werkstudent KI & Chatbot Produktmanagement, and the related
    CHECK24 Digitales Produktmanagement Chatbot & KI InsurTech postings:
    both are Produktmanagement (product management) roles rather than AI
    Engineer or AI Evaluation flavoured engineering work, dropped as out
    of the 26 August 2026 scope narrowing.
  - CHECK24 Werkstudent AI-Produkte, Kreditvergleich (KAI Team): same
    role already logged in Notion as CHECK24 Vergleichsportal Finanzen
    GmbH, status 'rejected'. Dropped as duplicate.
  - KontextWork GbR Werkstudent Generative AI & LLM, Hanover: same company
    already logged in Notion as 'Not listed Anymore'. Dropped as
    duplicate under the standing company plus role dedup rule.
  - Mercedes-Benz Tech Innovation Werkstudent AI Agents & Robotics
    Platform, Karlsruhe: same company plus role already logged in Notion
    as 'rejected'. Dropped as duplicate.
  - Sopra Steria AI Platform Engineer and Testmanager roles surfaced in
    the same search but are full time consultant roles outside the
    Werkstudent scope of the one role drafted below. Not drafted.

Three roles cleared verification: a live posting fetched directly (or, for
Sopra Steria, a live confirmed match on the company's own job search
listing after the specific deep link 404'd), a confirmed or best available
apply path, and a clean dedup check against applied-log.csv and Notion
(219 CSV rows, 214 Notion rows at run start).

Platform mix this run:
  - Company Page, 2 (COBACK, Dresden, external company portal at
    hire.co-back.com; Sopra Steria Custom Software Solutions GmbH,
    Muenchen/Hamburg/Karlsruhe, company careers portal)
  - Other/aggregator with confirmed employer identity, 1 (Atos,
    Paderborn/Hamburg/Berlin, surfaced and verified via the Workopia
    aggregator platform, which requires sign in to reach the employer's
    own application link; Apply Method set to company-portal as the safe
    default per the 22 September 2026 ambiguous-listing convention)
  - LinkedIn, StepStone: surfaced no new in-scope, verifiable,
    non-duplicate postings this run beyond the leads listed as dropped
    above; the fresh LinkedIn AI Engineer / Agentic AI leads found this
    run (SAP Agentic AI and Robot Learning Research, BCG Generative AI and
    Workflow Automation, Siemens Software Development AI & Data
    Integration) were either confirmed filled or could not be verified
    live within this run's time budget and were left for a future run
    rather than drafted unverified.
  - JobTeaser surfaced Reply Deutschland SE Werkstudent Artificial
    Intelligence (Huacaya AI platform, LLM finetuning), which returned
    HTTP 403 Forbidden on direct fetch; Reply Deutschland SE already has
    two roles logged in Notion (REPLY, rejected; Reply Deutschland SE,
    applied) so this was not pursued further as a priority given the
    verification difficulty.
  - Indeed not used (no MCP tool available this session, consistent with
    prior runs).

Freshness order (all three fall in the single Germany tier, ranked by
recency then Best for overlap):
  1. COBACK, Dresden, Working Student AI Engineer, EN track, confirmed
     live via a direct fetch of the dresden-exists.de mirror of the
     posting (the company's own hire.co-back.com portal returned 503 on
     a direct check, consistent with anti-bot blocking rather than the
     listing being gone, since the mirror content was current).
  2. Atos, Paderborn/Hamburg/Berlin, Werkstudent Agentic AI (data & AI),
     EN track, confirmed live via a direct fetch of the Workopia listing.
  3. Sopra Steria Custom Software Solutions GmbH, Muenchen/Hamburg/
     Karlsruhe, Werkstudent fuer Agentic Coding, DE track (posting title
     and company blog content are in German), confirmed live via a direct
     fetch of the company's own jobs search results page filtered to
     "Agentic", which returned exactly this one live posting.

Language track per 20 July 2026 language match hard rule (posting body
language IS deliverable language): COBACK and Atos postings are written in
English -> EN track. Sopra Steria's posting title and surrounding company
content are in German -> DE track.

German level flags (accept German listings per master-projects.md, flag
the bar against Rah's actual B1 in progress level, not a filter):
  - COBACK states "fluent English; German considered advantageous", well
    within reach at B1 in progress.
  - Atos states German AND English proficiency both required, which is a
    real risk against B1 in progress; flagged here for Rah's judgement,
    not used to drop the role since German level is not a scoring filter
    per master-projects.md.
  - Sopra Steria's listing did not state an explicit German level bar in
    the content retrieved; flagged as unknown.

Dedup check against applied-log.csv and Notion (219 CSV rows, 214 Notion
rows at run start, full company plus role comparison run during this
run's reconciliation step): COBACK, Atos, and Sopra Steria Custom Software
Solutions GmbH are all entirely new companies for this specific role, never
previously logged.

Apply Method set directly in role_configs where determinable from the
posting: COBACK (external company portal, company-portal, out of
OpenClaw's platform-native scope), Sopra Steria (company careers portal,
company-portal). Atos is set to company-portal as the safe default since
the only verified access path (Workopia) is an aggregator requiring sign
in to reach the employer's actual application destination, and OpenClaw's
scope rules default an ambiguous listing to company-portal.

19 August 2026 CV content rules apply: no hyphens or dashes in CV text,
no parentheses or brackets in bullets, Languages EN and DE only, German
level locked to "German: B1, in progress" or "Deutsch: B1, laufend" on
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


CONFIGS_23SEP = [
    # 1. COBACK, Dresden
    # Working Student AI Engineer (m/f/d), SHK/Teilzeit, start from March
    # External company portal (hire.co-back.com). EN track. AI powered
    # compliance platform for sustainability and ESG reporting; support
    # development and evaluation of AI features, LLMs, embeddings, vector
    # databases, RAG pipelines, prompt engineering and evaluation.
    # Apply: https://hire.co-back.com/
    {
        "folder": "COBACK Dresden Working Student AI Engineer",
        "company": "COBACK",
        "lang": "en",
        "location": "Dresden",
        "apply_link": "https://hire.co-back.com/",
        "apply_method": "company-portal",
        "source": "Company Page",
        "german_level": "B1",
        "tag": "Master's Student Data Science and Analytics | LLM Evaluation and RAG Pipelines | Python + LangGraph + AIF360",
        "role_strip": "Working Student, AI Engineer",
        "cl_date": "23 September 2026",
        "cl_subject": "Working Student AI Engineer in Dresden",
        "profile": "Master's student in Data Science and Analytics at SRH Heidelberg, based in Mannheim, with hands on experience building and systematically evaluating LLM based applications, embeddings, and RAG pipelines for a regulated, compliance sensitive domain. I built a Multi Agent RAG system with an independent LLM as Judge model scoring answers across 5 dimensions, and a fairness by design credit scoring system that cleared EU AI Act and GDPR Article 22 human in the loop requirements. Comfortable in Python, prompt engineering, and moving AI features from prototype to production with defensible evaluation.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_RAG_EN, P_CREDITIQ_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_NVIDIA, CERT_AWS, CERT_GOOGLE],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am writing to apply for the Working Student AI Engineer position at COBACK in Dresden. As a Master's student in Data Science and Analytics at SRH Heidelberg based in Mannheim, the mix of building LLM based applications, working with embeddings and vector databases, and supporting evaluation of AI features for a compliance and ESG reporting platform maps closely to the work I have shipped over the last several months.",
            "In my Multi Agent RAG project I implemented a JudgeAgent that scores answers on 5 dimensions, groundedness, relevance, completeness, citation quality and language quality, in JSON mode at temperature 0, and eliminated self preference bias by running the judge on a different local model from the generator, with a hard failure on a missing judge model so a silent fallback to self judging cannot regress unnoticed. That experience evaluating LLM outputs systematically rather than subjectively is exactly the kind of rigor a compliance platform's AI features need.",
            "In my CreditIQ project on regulated credit scoring, I applied AIF360 mitigation and threshold calibration to bring a model back into EU AI Act and AGG fairness compliance, then shipped a Streamlit decision support tool with a plain language LLM generated explanation and a full regulatory write up covering GDPR Article 22 and EU AI Act Article 14 human in the loop requirements. That experience building AI features for a regulated, audit sensitive domain transfers directly to evaluating AI features for sustainability and ESG reporting.",
            "I work comfortably in Python and have hands on experience with prompt engineering, LLMs, and RAG pipelines. I hold the NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations, and Google Data Analytics certificates, and was recognised as a Finalist of the USAII Global AI Hackathon 2026 at Graduate Level. I am fluent in English and B1 in progress in German. I can join as a working student in Dresden and would welcome the chance to discuss how I could contribute to your AI engineering work.",
        ],
    },

    # 2. Atos, Paderborn / Hamburg / Berlin
    # Werkstudent Agentic AI (data & AI) (m/w/d)
    # Surfaced and verified via Workopia aggregator (employer application
    # link requires sign in). EN track (listing content retrieved in
    # English). Support development of Agentic AI solutions, LLM
    # orchestration frameworks, agent technologies, vector databases, AI
    # governance and regulatory frameworks.
    # Apply: https://workopia.io/jobs/6451f50cdce4cae9028bce9921173f4c
    {
        "folder": "Atos Paderborn Hamburg Berlin Werkstudent Agentic AI",
        "company": "Atos",
        "lang": "en",
        "location": "Paderborn, Hamburg, or Berlin",
        "apply_link": "https://workopia.io/jobs/6451f50cdce4cae9028bce9921173f4c",
        "apply_method": "company-portal",
        "source": "Other",
        "german_level": "B1",
        "tag": "Master's Student Data Science and Analytics | Agentic AI and LLM Orchestration | Python + LangGraph + Vector Databases",
        "role_strip": "Werkstudent, Agentic AI",
        "cl_date": "23 September 2026",
        "cl_subject": "Werkstudent Agentic AI (data & AI) in Paderborn, Hamburg, or Berlin",
        "profile": "Master's student in Data Science and Analytics at SRH Heidelberg, based in Mannheim, with hands on experience designing multi agent systems, working with vector databases, and documenting AI governance relevant tradeoffs for regulated use cases. I built a LangGraph based multi agent RAG system with an independent LLM as Judge model and a Pinecone backed retrieval layer, and a fairness by design credit scoring system with a full EU AI Act and GDPR regulatory write up. Comfortable in Python, agent orchestration frameworks, and translating research literature into working prototypes.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_RAG_EN, P_CREDITIQ_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_NVIDIA, CERT_AWS, CERT_GOOGLE],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am writing to apply for the Werkstudent Agentic AI (data & AI) position at Atos. As a Master's student in Data Science and Analytics at SRH Heidelberg based in Mannheim, the mix of developing Agentic AI solutions, working with LLM orchestration frameworks and vector databases, and engaging with AI governance and regulatory frameworks maps closely to the work I have shipped over the last several months.",
            "In my Multi Agent RAG project I designed a LangGraph based agent system with a LanguageAgent, a JudgeAgent, and dedicated retrieval agents, each with clearly scoped responsibilities, a shared Pinecone vector index, and a hard failure on a missing judge model rather than a silent fallback. That experience designing multi agent systems end to end and making deliberate tradeoffs about how individual agents cooperate is exactly what building Agentic AI solutions from research literature to working prototypes requires.",
            "In my CreditIQ project I documented the fairness accuracy tradeoff as a deliberate, regulator defensible decision, backed the pipeline with unit tests at 100 percent branch coverage, and produced a full regulatory write up spanning the EU AI Act, GDPR, and a model card. That experience treating AI governance and regulatory frameworks as first class engineering constraints rather than an afterthought transfers directly to Atos's interest in AI governance alongside agent technologies.",
            "I work comfortably in Python and have hands on experience with LLM orchestration frameworks, agent technologies, and vector databases, and I am comfortable reading and reproducing findings from technical literature. I hold the NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations, and Google Data Analytics certificates, and was recognised as a Finalist of the USAII Global AI Hackathon 2026 at Graduate Level. I am fluent in English and B1 in progress in German. I can join as a working student and would welcome the chance to discuss how I could contribute to your Agentic AI work.",
        ],
    },

    # 3. Sopra Steria Custom Software Solutions GmbH, Muenchen / Hamburg /
    #    Karlsruhe
    # Werkstudent fuer Agentic Coding (m/w/d)
    # Company careers portal (careers.soprasteria.de), deep link 404'd but
    # confirmed live via the company's own job search filtered to
    # "Agentic". DE track. IT Architecture department, agentic and vibe
    # coding methodologies for digital transformation projects.
    # Apply: https://careers.soprasteria.de/jobs?search=Agentic
    {
        "folder": "Sopra Steria Muenchen Werkstudent Agentic Coding",
        "company": "Sopra Steria Custom Software Solutions GmbH",
        "lang": "de",
        "location": "Muenchen, Hamburg, oder Karlsruhe",
        "apply_link": "https://careers.soprasteria.de/jobs?search=Agentic",
        "apply_method": "company-portal",
        "source": "Company Page",
        "german_level": "B1",
        "tag": "Masterstudent Data Science and Analytics | Agentische KI und Softwarearchitektur | Python + LangGraph + REST Integrationen",
        "role_strip": "Werkstudent, Agentic Coding",
        "cl_date": "23. September 2026",
        "cl_subject": "Werkstudent fuer Agentic Coding in Muenchen",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Entwurf agentischer Systeme und in der Automatisierung wiederkehrender Entwicklungsaufgaben ueber LLM gestuetzte Workflows. Ich habe ein LangGraph Multi Agenten System mit klar abgegrenzten Verantwortlichkeiten gebaut sowie eine vollautomatisierte Airflow Orchestrierung mit Gate Checks, die manuelle Wiederholungen ersetzt. Sicher im Uebersetzen neuer KI gestuetzter Entwicklungsmethoden wie Agentic Coding in produktionsreife Loesungen in Python.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_CREDITIQ_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Position als Werkstudent fuer Agentic Coding bei der Sopra Steria Custom Software Solutions GmbH in Muenchen. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim passt die Aufgabe, digitale Zukunftsthemen aktiv mitzugestalten und an innovativen Loesungen fuer die digitale Transformation mit agentischen und KI gestuetzten Entwicklungsmethoden zu arbeiten, sehr genau zu dem, was ich in den letzten Monaten praktisch gebaut habe.",
            "In meinem Multi Agent RAG Projekt habe ich ein LangGraph basiertes Agentensystem mit einem LanguageAgent und einem JudgeAgent entworfen, jeweils mit klar abgegrenzten Verantwortlichkeiten und definiertem Fallback Verhalten, sowie eine harte Fehlerbehandlung bei fehlendem Judge Modell statt eines stillen Rueckfalls. Diese Erfahrung, Agentensysteme eigenstaendig zu entwerfen und technische Entscheidungen ueber die Zusammenarbeit einzelner Agenten zu treffen, ist genau das, was Agentic Coding in der Softwarearchitektur Praxis braucht.",
            "In meinem CreditIQ Projekt habe ich ein reguliertes Machine Learning System von der Bereinigung ueber SHAP Analyse bis zu einem ausgelieferten Streamlit Tool mit vollstaendiger regulatorischer Dokumentation getragen. Diese Erfahrung, ein Projekt durchgaengig von der Analyse bis zur produktionsreifen Integration zu verantworten statt nur einzelne Bausteine zu liefern, uebertraegt sich direkt auf die Arbeit an vollstaendigen digitalen Transformationsloesungen.",
            "Ich arbeite sicher in Python und habe praktische Erfahrung mit LangGraph, Prompt Engineering und REST Integrationen. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend, ich hebe es aktiv weiter, und Englisch spreche ich fliessend. Ich kann die Werkstudentenstelle zeitnah beginnen und stelle mich gerne in einem persoenlichen Gespraech vor.",
        ],
    },
]
