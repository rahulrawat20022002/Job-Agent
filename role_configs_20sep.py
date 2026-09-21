"""Role configurations for the 20 September 2026 scheduled job search run
(8 to 10 drafted backlog zone per the 28 July 2026 yield reset, capped at
top 3).

Backlog gate check per 14 July 2026 status source of truth rule: Notion
data source fd974369-40b2-48c5-b660-d15256c88f52 returned 10 rows in
status 'drafted' at run start (FZI Forschungszentrum Informatik, iLert
GmbH, Syneco Trading GmbH, Temedica GmbH, Charles Real Estate GmbH, SAP
Walldorf LLM SE Solutions, Stiftung Polytechnische Gesellschaft Frankfurt,
Muenchener Verein Versicherungsgruppe, Atruvia AG, disruptive GmbH). 10
drafted falls in the 8 to 10 zone of the 28 July 2026 yield based reset
rule, which caps this run at the top 3 (not the normal top 3 to 5, and not
a hard pause).

Reconciliation this run compared all 212 applied-log.csv rows against 207
Notion rows with a Company plus Role value (208 total rows in the data
source, one of which is the internal "New CVs now" placeholder row with no
Company or Role value and is excluded from the comparison). Found 3 real
Status drift rows where the CSV still read 'applied' but Notion already
carried 'rejected' (Mercedes-Benz AG Werkstudent Data Analytics and
Projektsteuerung MB.OS; Mercedes-Benz Tech Innovation Werkstudent AI
Agents and Robotics Platform; Mercedes-Benz Tech Innovation Werkstudent
Machine Learning Engineering); per invariant 1, Notion is the source of
truth, so all 3 CSV rows were updated to 'rejected' to match Notion. One
apparent 'missing from Notion' row (Aerzteverband Deutscher Allergologen
with the umlaut in the CSV versus Arzteverband without it as SQL text mode
lossily returns it) was confirmed via a direct SQL LIKE lookup to already
exist in Notion with a matching 'applied' status; this is the same known
spelling variant flagged in prior digests, not a real gap, and no new
Notion row was created for it.

Search environment this run: the Tavily MCP server failed to connect
(SdkHttpError, CLIENT_HTTP_NOT_IMPLEMENTED) for the entire run, and no
Indeed MCP tool was available. All search relied on the built in WebSearch
tool. WebFetch worked for LinkedIn job view pages and several company or
ATS domains (predori.com returned 404, a ponturo StudySmarter mirror
returned 410, jobs.sap.com rendered a real "position has been filled"
page), but WebFetch returned 403 or 503 on every direct stepstone.de and
jobteaser.com URL attempted, consistent with the EGRESS_BLOCKED pattern
the 9 through 18 September digests already logged for those two domains.
Because of this, the 3 roles drafted below that live on stepstone.de or
jobteaser.com were verified through WebSearch result snippets only (title,
company, location, responsibilities, requirements as surfaced by the
search tool), not through a direct fetch of the full original posting
text. This is a weaker evidence standard than a direct page fetch and is
flagged here plainly per invariant 5; no outcome is claimed beyond what
the search snippets support, and language track below is inferred from
each posting's own title language and company profile rather than a
confirmed full body read.

Leads found and dropped this run: KLUGSYS Werkstudent Agentic AI Engineer
(Aachen area, LinkedIn) is no longer accepting applications per the
posting's own "Es werden keine Bewerbungen mehr angenommen" notice, so it
was dropped as closed; Modern Drive Technology GmbH Werkstudent AI
Engineering (Neumarkt in der Oberpfalz, LinkedIn) requires verhandlungssicheres
Deutsch for onsite process interviews with users, a hard non negotiable
requirement well above the current B1 in progress level, so it was dropped
on German level mismatch and is noted on the watchlist; AKDB Werkstudent
Workflow Automation and Agentic AI (Koeln) returned HTTP 410 Gone on its
own careers page, so it was dropped as closed; SAP Walldorf Working
Student AI based Quality Evaluation for AI Generated Code Changes (SAP
HANA Cloud) returned "Sorry, this position has been filled" on the
official jobs.sap.com page, so it was dropped as filled (note this is a
different specific requisition than the SAP Walldorf LLM SE Solutions role
already drafted on 16 September); predori Werkstudent NLP or LLM Engineer
returned HTTP 404 on its own careers page and the only surfaced posting
date was October 2025, roughly 11 months stale, so it was dropped as
likely expired; EY Parthenon Werkstudent AI and GenAI, Strategy and
Transactions reads predominantly as a strategy consulting role using AI
tooling for market and capital strategy work rather than AI engineering or
evaluation build work, so it falls outside the 26 August 2026 narrowing
and was dropped; Reply Deutschland Werkstudent AI Business Solutions and
Agents centres on Microsoft Copilot Studio and Power Platform citizen
development rather than model or agent engineering, a weaker fit than the
3 selected roles, and was placed on the watchlist rather than drafted
under this run's top 3 cap; Ponturo Consulting Werkstudent AI Engineer
(multi city) is a plausible fit but its StudySmarter mirror returned HTTP
410 Gone and no first party ponturo.com posting could be independently
reached this run, so it was not drafted under invariant 4 and is left on
the watchlist for re verification on a future run.

Three roles cleared verification to the standard available this run
(WebSearch snippet evidence, dedup checked against the reconciled 212 row
CSV and 207 row Notion set, all 3 confirmed as entirely new companies
never previously logged):

1. Control Expert GmbH, Langenfeld Rheinland, Working Student QA Engineer,
   AI / LLM Systems. Source StepStone (also mirrored on the company's own
   softgarden ATS, which returned 404 on direct fetch this run). Role
   tests and evaluates an Agentic AI team's LLM and agent based systems,
   squarely AI Evaluation flavoured (test design for multi step reasoning,
   tool use and decision flows). Requirements list good communication in
   both German and English rather than a hard fluency bar in either
   direction, and the posting's own title and requirement list are
   entirely in English, so this is drafted EN track; flagged as an
   inferred call given the snippet only evidence standard above, not a
   confirmed full body read.
2. FUNKE Mediengruppe, Hamburg, Werkstudent Workflow Automation n8n,
   Agentic AI. Source StepStone. Role orchestrates LLM agents via n8n and
   supports an internal Agentic AI platform, squarely Agentic AI Engineer
   flavoured. Posting title and company are German, drafted DE track.
3. Vector Informatik GmbH, Stuttgart and Karlsruhe, Werkstudent, AI driven
   CI or CD Automation. Source JobTeaser. Role integrates AI agents into
   CI pipelines for automatic log and artifact evaluation and builds AI
   based classification of build and test failures, an AI Engineer plus
   evaluation blend. Onsite presence required, no pure remote option per
   the posting; still within the standing Germany geography filter.
   Posting title and company are German, drafted DE track.

Platform mix this run: StepStone 2 (Control Expert, FUNKE Mediengruppe),
JobTeaser 1 (Vector Informatik). LinkedIn, Xing, and company career pages
were also searched via WebSearch this run; LinkedIn and Xing surfaced only
already logged, closed, or out of scope leads per the dropped list above.
Indeed was not used, no MCP tool available and no in scope Indeed result
surfaced via WebSearch.

Freshness: none of the 3 postings carried a confirmable exact post date
within the WebSearch snippet evidence available this run; all 3 were
confirmed as currently listed and accepting applications (Control Expert
and FUNKE Mediengruppe via their live StepStone listing pages appearing in
search results, Vector Informatik via its live JobTeaser listing), so
freshness is ranked by geographic tier alone this run, all 3 falling in
the single Germany tier with no further recency signal to rank within it.
Order presented below follows Best for project overlap strength as the
tiebreaker: Control Expert first as the strongest direct match to the RAG
project's LLM as Judge and eval harness work, then FUNKE Mediengruppe and
Vector Informatik as strong but slightly less direct Agentic AI Engineer
matches.

Apply Method left unset in Notion for all 3 roles pending OpenClaw's
platform native versus company portal determination at submission time.
Control Expert and FUNKE Mediengruppe are StepStone listings, which per
CLAUDE.md's Agent B scope are platform native only when the Schnelle
Bewerbung flow stays inside StepStone itself; Vector Informatik is a
JobTeaser listing pointing at a company owned careers domain, so it is
likely company portal shaped, but the final call is OpenClaw's per the
standing scope split.

19 August 2026 CV content rules apply: no hyphens or dashes in CV text, no
parentheses or brackets in bullets, Languages EN and DE only, German level
locked to "German: B1, in progress" or "Deutsch: B1, laufend" on the
respective track, no page numbers or headers or footers, 2 page hard cap,
Ojas style header, Skills grouped into functional buckets, positioning tag
under the name is a pitch not the posting title.
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
    P_FLIGHT_DE,
    P_MOVIE_DE,
)


CONFIGS_20SEP = [
    # 1. Control Expert GmbH, Langenfeld Rheinland
    # Working Student QA Engineer, AI / LLM Systems
    # StepStone. EN track. Tests and evaluates an Agentic AI team's LLM
    # and agent based systems: multi step reasoning, tool use, decision
    # flow test design.
    # Apply: https://www.stepstone.de/stellenangebote--Working-Student-QA-Engineer-gn-AI-LLM-Systems-Langenfeld-Rheinland-Control-Expert-GmbH--14186197-inline.html
    {
        "folder": "Control Expert Langenfeld Working Student QA Engineer AI LLM Systems",
        "company": "Control Expert GmbH",
        "lang": "en",
        "tag": "Data Science Master's Student | AI Evaluation and LLM Agent Testing | Python + LLM as Judge Harnesses",
        "role_strip": "Working Student QA Engineer, AI / LLM Systems",
        "cl_date": "20 September 2026",
        "cl_subject": "Working Student QA Engineer, AI / LLM Systems in Langenfeld",
        "profile": "Data Science and Analytics Master's student at SRH Heidelberg based in Mannheim with hands on experience designing evaluation harnesses for LLM and agent based systems. I built an LLM as Judge evaluation layer scoring answers on 5 quality dimensions with a self preference bias check, plus a 9 metric retrieval and generation evaluation suite reported per language on a paired EN and DE eval set. Comfortable in Python, curious about how agent systems reason and fail, and ready to bring that same rigor to testing production LLM and agent pipelines.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_RAG_EN, P_CREDITIQ_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_NVIDIA, CERT_AWS, CERT_GOOGLE],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am writing to apply for the Working Student QA Engineer, AI / LLM Systems position at Control Expert in Langenfeld. As a Data Science and Analytics Master's student at SRH Heidelberg based in Mannheim, testing and evaluating LLM and agent based systems is exactly the work I have been doing hands on over the past months, not something I would be learning from scratch.",
            "In my Multi Agent RAG project, I built an LLM as Judge evaluation layer that scores answers on 5 quality dimensions, groundedness, relevance, completeness, citation quality and language quality, in JSON mode at temperature 0, and I eliminated self preference bias by running the judge on a different local model than the generator, with a hard failure whenever the judge model is missing so a silent regression cannot slip through unnoticed. That same instinct, that an evaluation system is only trustworthy if its own failure modes are caught rather than assumed away, is what a QA role over an Agentic AI team's own systems needs.",
            "In the same project, I also built a 9 metric evaluation suite, 5 retrieval metrics including hit at k and nDCG at k plus 4 generation metrics, aggregated overall and per language into JSON and Markdown reports on a paired EN and DE labelled evaluation set. Separately, in my CreditIQ project I backed a regulated credit scoring pipeline with unit tests at 100 percent branch coverage and used SHAP driven subgroup analysis to expose a hidden bias pattern a single axis check had missed. Both experiences translate directly into designing test cases for multi step reasoning, tool use, and decision flows in an agent based system, and into the analytical curiosity about how a system reasons and fails that the role calls for.",
            "I work confidently in Python, have practical exposure to LLM APIs, prompt engineering, and evaluation metric design, and hold the NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations, and Google Data Analytics certificates, alongside a Finalist placement at the USAII Global AI Hackathon 2026 Graduate Level. My German is at B1 and in progress, and I am comfortable communicating in both German and English day to day. I am available to start as a working student in Langenfeld and would welcome the opportunity to discuss the role further.",
        ],
    },

    # 2. FUNKE Mediengruppe, Hamburg
    # Werkstudent Workflow Automation n8n, Agentic AI
    # StepStone. DE track. Orchestrates LLM agents via n8n, supports the
    # buildout of an internal Agentic AI platform.
    # Apply: https://www.stepstone.de/stellenangebote--Werkstudent-Workflow-Automation-n8n-Agentic-AI-m-w-d-Hamburg-FUNKE-Mediengruppe--13397936-inline.html
    {
        "folder": "FUNKE Mediengruppe Hamburg Werkstudent Workflow Automation Agentic AI",
        "company": "FUNKE Mediengruppe",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | Agentenbasierte Workflow Automatisierung | Python + LangGraph",
        "role_strip": "Werkstudent Workflow Automation n8n, Agentic AI",
        "cl_date": "20. September 2026",
        "cl_subject": "Werkstudent Workflow Automation n8n, Agentic AI in Hamburg",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Entwurf und Betrieb agentenbasierter Workflow Systeme. Ich habe ein LangGraph basiertes Multi Agenten System mit klar abgegrenzten Verantwortlichkeiten pro Agent gebaut sowie ein Gesamtsystem vollstaendig automatisiert orchestriert, das alle 15 Minuten unbeaufsichtigt aktualisiert. Sicher im Uebersetzen von Geschaeftsprozessen in wiederverwendbare, produktionsreife Automatisierungsbausteine in Python.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_FLIGHT_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich als Werkstudent Workflow Automation n8n, Agentic AI bei der FUNKE Mediengruppe in Hamburg, um LLM Agenten zu orchestrieren und den Aufbau einer internen Agentic AI Plattform zu unterstuetzen. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim passt diese Aufgabe sehr genau zu dem, was ich in den letzten Monaten praktisch gebaut habe.",
            "In meinem Multi Agent RAG Projekt habe ich ein LangGraph basiertes Multi Agenten System entworfen, in dem jeder Agent eine klar begrenzte Verantwortung traegt, darunter ein LanguageAgent, der die Ausgabesprache zentral an jeden nachgelagerten Agenten weiterreicht, und ein JudgeAgent mit einem Hard Failure bei fehlendem Judge Modell, damit ein stiller Fehler nicht unbemerkt bleibt. Diese Erfahrung, agentenbasierte Systeme mit klaren Verantwortungsgrenzen und wiederverwendbaren Bausteinen zu entwerfen, deckt sich direkt mit dem Aufbau wiederverwendbarer Workflow Templates und der Orchestrierung von LLM Agenten ueber n8n.",
            "In meinem Real Time Flight Tracking Projekt habe ich das Gesamtsystem mit Apache Airflow auf GCS gestuetztem Speicher und Dataproc Compute orchestriert, sodass Batch und Echtzeit Schichten automatisch alle 15 Minuten ohne manuellen Eingriff aktualisieren. Diese Erfahrung, ein System zuverlaessig unbeaufsichtigt im produktiven Betrieb zu halten statt es nur einmalig zu bauen, uebertraegt sich direkt auf den Betrieb und die Weiterentwicklung von n8n Workflows fuer reale Geschaeftsprozesse.",
            "Ich arbeite sicher in Python, habe praktische Erfahrung mit REST APIs, LLM Integration und Agentensystemen und halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate. Ich wurde zudem als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend, ich hebe es aktiv weiter, und Englisch spreche ich fliessend. Ich kann als Werkstudent in Hamburg zeitnah beginnen und freue mich auf ein persoenliches Gespraech.",
        ],
    },

    # 3. Vector Informatik GmbH, Stuttgart und Karlsruhe
    # Werkstudent, AI driven CI/CD Automation
    # JobTeaser. DE track. Integriert AI Agenten in CI Pipelines zur
    # automatischen Auswertung von Logs und Artefakten, entwickelt KI
    # basierte Klassifikation von Build und Testfehlern. Onsite Praesenz
    # erforderlich, kein reines Remote.
    # Apply: https://www.jobteaser.com/de/job-offers/47288d2e-e9b1-4b12-804d-834af1a16533-vector-informatik-gmbh-werkstudent-ai-driven-ci-cd-automation-m-w-d
    {
        "folder": "Vector Informatik Stuttgart Karlsruhe Werkstudent AI CI CD Automation",
        "company": "Vector Informatik GmbH",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | KI gestuetzte CI/CD Automatisierung | Python + Agentenbasierte Pipeline Auswertung",
        "role_strip": "Werkstudent, AI driven CI/CD Automation",
        "cl_date": "20. September 2026",
        "cl_subject": "Werkstudent, AI driven CI/CD Automation in Stuttgart oder Karlsruhe",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Bauen automatisierter, agentenbasierter Pipelines mit eingebauten Gate Checks. Ich habe ein LangGraph basiertes Multi Agenten System mit einer eigenstaendigen Evaluationsschicht gebaut sowie eine vollautomatisierte Cloud Pipeline mit 0 manuellen Eingriffen orchestriert. Sicher im Entwerfen von KI gestuetzten Ansaetzen zur automatischen Klassifikation und Auswertung in Python.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_MOVIE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich als Werkstudent fuer AI driven CI/CD Automation bei Vector Informatik in Stuttgart oder Karlsruhe, um KI Agenten in CI Pipelines zur automatischen Auswertung von Logs und Artefakten zu integrieren. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim passt diese Aufgabe sehr genau zu dem, was ich in den letzten Monaten praktisch gebaut habe.",
            "In meinem Multi Agent RAG Projekt habe ich einen EvalAgent implementiert, der 5 Retrieval Metriken und 4 Generation Metriken automatisch berechnet und aggregiert in JSON und Markdown Reports ausgibt, sowie einen JudgeAgent mit einem Hard Failure bei fehlendem Judge Modell, damit ein stiller Fehler in der automatisierten Auswertung nicht unbemerkt bleibt. Diese Erfahrung, automatisierte Auswertungslogik fuer komplexe Systemzustaende zuverlaessig zu bauen, deckt sich direkt mit der KI gestuetzten Analyse und Klassifikation von Build und Testfehlern.",
            "In meinem Movie Analytics und ML Pipeline Projekt habe ich eine end to end Batch Pipeline mit einer 3 stufigen Bronze Silber Gold Medallion Architektur gebaut, die vollstaendig automatisiert per Cloud Scheduler laeuft und 0 manuelle Eingriffe benoetigt, abgesichert mit einem Least Privilege Service Account. Diese Erfahrung, Pipelines zuverlaessig automatisiert und ohne manuellen Eingriff im produktiven Betrieb zu halten, uebertraegt sich direkt auf die Weiterentwicklung skalierbarer CI/CD Systeme mit gezieltem KI Einsatz.",
            "Ich arbeite sicher in Python, habe praktische Erfahrung mit Automatisierung, Agentensystemen und CI/CD nahen Pipeline Orchestrierung und halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate. Ich wurde zudem als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend, ich hebe es aktiv weiter, und Englisch spreche ich fliessend. Ich kann als Werkstudent vor Ort in Stuttgart oder Karlsruhe zeitnah beginnen und freue mich auf ein persoenliches Gespraech.",
        ],
    },
]
