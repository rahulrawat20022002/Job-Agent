"""Role configurations for the 6 September 2026 scheduled job search run.

Backlog gate check per 14 July 2026 status source of truth rule: Notion
data source fd974369-40b2-48c5-b660-d15256c88f52 returned 0 rows in status
'drafted' at run start. 0 drafted falls under the 8 row floor of the 28
July 2026 yield based reset rule, which allows a normal top 3 to 5 cut.
This run ships 3.

Reconciliation this run found the CSV 3 rows behind Notion's Status
column for three roles OpenClaw had submitted overnight (Mercedes-Benz
Tech Innovation AI Agents and Robotics Platform, Beilmann Marketing GmbH,
ETG-Elektronik GmbH), all flipped from 'drafted' to 'applied' in Notion.
The CSV was corrected to match Notion (the source of truth for status)
for all three, with no reverse writes. One additional near-miss (Arzteverband
Deutscher Allergologen vs Ärzteverband Deutscher Allergologen) was an
umlaut encoding difference between the two systems referring to the same
row, not an actual drift; no write was needed for it.

Platform mix this run:
  - StepStone (Mi-Jack Europe GmbH, Karlsruhe), 1
  - StepStone (KontextWork GbR, Hannover), 1
  - Company Page (appliedAI Initiative GmbH, Munich/Heilbronn), 1

Sources reachable this run: Tavily web search plus tavily_extract for
StepStone, Xing, LinkedIn (extract only, WebFetch is proxy blocked for
linkedin.com and stepstone.de domains directly in this sandbox), JobTeaser,
and company career pages. Indeed was searched via Tavily site search only
(no Indeed MCP tool available in this environment); one Indeed-domain lead
search returned no in-scope new postings this run, so 0 Indeed rows this
run, consistent with the 1-per-run Indeed cap never being exceeded.
LinkedIn direct fetch (de.linkedin.com) and StepStone direct fetch
(www.stepstone.de) were both blocked by the egress proxy; StepStone content
was retrieved successfully via tavily_extract instead, which is not
proxy-restricted. Two promising LinkedIn leads (Fraunhofer HHI
"Werkstudent*in Erklaerbare KI" and a "Werkstudent Agentic AI" listing on
wearedevelopers.com) could not be verified: the Fraunhofer HHI LinkedIn
page could not be fetched by any available tool, and the wearedevelopers.com
mirror returned "Job Not Found" (listing removed). Both are dropped per
invariant #3 (never fabricate an outcome) rather than drafted on an
unverified posting, and flagged in the digest watchlist.

Freshness order within the single Germany tier:
  1. Mi-Jack Europe GmbH, Pflichtpraktikant AI Agents, Karlsruhe, posted
     1 week ago on StepStone, verified listing, mandatory internship
     (Pflichtpraktikum), DE track.
  2. appliedAI Initiative GmbH, Working Student AI Engineering and Product
     Development, Munich (House of Communication) or Heilbronn (IPAI),
     hybrid, found on the company's own careers page, no posting age shown
     on the page, EN track.
  3. KontextWork GbR, Werkstudent KI-Engineer Generative KI und LLM,
     Hannover, StepStone, posted about 1 month ago (older listing, still
     live and accepting applications as of this run), DE track.

Language track per 20 July 2026 language match hard rule (posting body
language IS deliverable language): Mi-Jack Europe and KontextWork postings
are both entirely in German, so both ship DE track. The appliedAI posting
uses German-language section labels (Ueber uns / Deine Aufgaben / Dein
Profil / Deine Vorteile) but every substantive sentence -- tasks,
requirements, benefits -- is written in English, so per the rule the body
language is English and this role ships EN track. The appliedAI posting
itself asks for "Proficiency in German and English (written and spoken)",
noted in the cover letter for full transparency.

Language level transparency: Mi-Jack Europe asks for "sichere Kommunikation
in Deutsch und Englisch" (confident communication in German and English),
a bar above Rah's current B1 in progress, flagged in the cover letter.
KontextWork's posting states no explicit language requirement. appliedAI
asks for "Proficiency in German and English," also above B1 in progress
and flagged in the cover letter.

Apply method transparency: Mi-Jack Europe's StepStone listing shows
"Schnelle Bewerbung" (Verifiziert), platform-native, in OpenClaw's
automated scope. KontextWork's StepStone listing also shows "Schnelle
Bewerbung," platform-native. appliedAI's "Jetzt bewerben" link routes to
appliedai.jobs.personio.de, a Personio-hosted company application form,
recorded as company-portal and outside OpenClaw's automated scope; Rah
applies manually.

Dedup check against applied-log.csv and Notion: Mi-Jack Europe GmbH,
KontextWork GbR, and appliedAI Initiative GmbH are all entirely new
companies, not previously logged in either system. A Rosenberger
Hochfrequenztechnik "Werkstudent fuer KI-Projekte" listing and a
Mercedes-Benz Group "Intern Enterprise Data & AI Architecture (Mandatory
Internship)" listing also surfaced this run; Rosenberger is already logged
in Notion/CSV as 'applied' (dropped as a duplicate) and the Mercedes-Benz
Group internship reads as a data-and-AI-architecture role (governance,
stakeholder architecture artefacts) rather than hands-on AI Engineering or
AI Evaluation work, so it was scored below the narrowed 26 August 2026
target and left on the watchlist rather than drafted, alongside the two
unverifiable LinkedIn leads noted above.

19 August 2026 CV content rules apply: no hyphens or dashes in CV text,
no parentheses or brackets in bullets, Languages EN and DE only, German
level locked to "Deutsch: B1, laufend" / "German: B1, in progress" per
track, no page numbers or headers or footers, 2 page hard cap, Ojas style
header, Skills grouped into functional buckets, positioning tag under the
name is a pitch not the posting title, and banned strings on the
validation gate are met by the new header.
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
    P_MOVIE_DE,
)


CONFIGS_06SEP = [
    # 1. Mi-Jack Europe GmbH, Karlsruhe
    # Pflichtpraktikant in der Entwicklung von AI Agents (m/w/d)
    # StepStone, posted 1 week ago, verified listing, mandatory internship
    # (Pflichtpraktikum), full time, homeoffice possible, DE track
    # Tasks: design, implement and document test cases, test scenarios and
    # evaluation metrics for AI agents; evaluate agent responses for
    # factual accuracy, consistency, reliability and usability; analyse
    # hallucinations and test safety and guardrail functions; build
    # automated test scripts and reports; document bugs and performance
    # issues with reproduction steps.
    # Requirements: studies with a focus on software development or AI;
    # ideally first hands-on experience with Google ADK or LangChain;
    # knowledge of prompt engineering and vector databases such as Chroma
    # or Milvus; Git and Visual Studio experience a plus; confident
    # communication in German and English.
    # Apply: https://www.stepstone.de/stellenangebote--Pflichtpraktikant-in-der-Entwicklung-von-AI-Agents-m-w-d-Karlsruhe-Mi-Jack-Europe-GmbH--13907202-inline.html
    # Apply method: platform-native (StepStone Schnelle Bewerbung, Verifiziert)
    {
        "folder": "Mi-Jack Europe Karlsruhe Pflichtpraktikant AI Agents",
        "company": "Mi-Jack Europe GmbH",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | KI Agenten Evaluation und Testautomatisierung | Python + LangGraph + Vektordatenbanken",
        "role_strip": "Pflichtpraktikant, Entwicklung von AI Agents",
        "cl_date": "6. September 2026",
        "cl_subject": "Pflichtpraktikum in der Entwicklung von AI Agents in Karlsruhe",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung in der systematischen Evaluation von KI Agenten auf Faktentreue, Konsistenz und Zuverlaessigkeit. Ich habe einen JudgeAgent gebaut, der Antworten automatisiert auf 5 Dimensionen bewertet und dabei bewusst auf einem anderen Modell laeuft als der Generator, um verzerrte Selbstbewertung auszuschliessen, und in einem produktiven Kredit Scoring System per SHAP gestuetzter Analyse eine verborgene Schwachstelle aufgedeckt, die einfache Metriken uebersehen haetten. Sicher in Python, LangGraph, Prompt Engineering und dem Aufbau reproduzierbarer Testfaelle fuer nicht deterministische KI Systeme.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_CREDITIQ_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer das Pflichtpraktikum in der Entwicklung von AI Agents bei Mi-Jack Europe GmbH in Karlsruhe. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim passt die in der Ausschreibung beschriebene Aufgabe, Testfaelle und Evaluationsmetriken fuer AI Agenten zu entwerfen und deren Antworten auf Faktentreue, Konsistenz und Zuverlaessigkeit zu bewerten, sehr genau zu dem, was ich in den letzten Monaten praktisch aufgebaut habe. Das Praktikum ist Pflichtbestandteil meines Studiums.",
            "In meinem Multi Agent RAG Projekt habe ich einen JudgeAgent implementiert, der Antworten im JSON Modus bei Temperatur 0 auf 5 Dimensionen bewertet: Grounding an den Quellen, Relevanz, Vollstaendigkeit, Zitierqualitaet und Sprachqualitaet, und dabei bewusst ein anderes lokales Modell Qwen2.5 14B als Richter eingesetzt als der Generator Mistral 7B, um Self Preference Bias auszuschliessen, mit einem harten Fehlschlag bei fehlendem Judge Modell, damit ein stiller Fallback auf Selbstbewertung nicht unbemerkt durchrutscht. Genau diese Disziplin, Antworten eines Agenten systematisch auf Faktentreue statt nur oberflaechlich zu pruefen, deckt sich mit der in der Ausschreibung beschriebenen Bewertung von Halluzinationen und Zuverlaessigkeit.",
            "In CreditIQ habe ich mit SHAP gestuetzter Subgruppenanalyse eine verborgene intersektionelle Schwachstelle in einem produktiven Machine Learning System aufgedeckt, die einfache Gesamtmetriken verdeckt hatten, und die Pipeline anschliessend mit Unit Tests bei 100 Prozent Branch Coverage sowie einer vollstaendigen Dokumentation der Sicherheits und Fairness Aspekte abgesichert. Diese Erfahrung, ein KI System systematisch zu testen, Schwachstellen zu dokumentieren und die Ergebnisse nachvollziehbar zu belegen, uebertraegt sich direkt auf den Aufbau automatisierter Testskripte und Reports fuer AI Agenten.",
            "Ich arbeite sicher in Python und habe erste Erfahrung mit LangGraph als Agentenframework sowie mit Vektor Datenbanken im Rahmen meiner mehrsprachigen RAG Pipeline. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend, ich hebe es aktiv weiter, und Englisch spreche ich fliessend. Mir ist bewusst, dass die Ausschreibung sichere Kommunikation in Deutsch und Englisch nennt, ein Niveau, das ich im Deutschen noch nicht ganz erreiche, und moechte an dieser Stelle offen damit umgehen. Gerne bespreche ich meinen Beitrag zu Ihrem Team in einem persoenlichen Gespraech.",
        ],
    },

    # 2. appliedAI Initiative GmbH, Munich or Heilbronn
    # Working Student (m/f/x) AI Engineering & Product Development
    # Company career page (appliedai.de), hybrid, no explicit posting age
    # shown, EN track (body content is English despite German section
    # labels)
    # Tasks: support the AI engineering team building and testing AI agent
    # functionality in Python using LangChain or Azure AI Foundry; support
    # design and automation of workflows on modern automation platforms;
    # contribute to demos, workshops and internal documentation; support
    # technical maintenance of an internal maturity assessment tool (MAT).
    # Requirements: enrolled in a Master's programme in Computer Science,
    # AI, Software Engineering or related; hands-on Python and genuine
    # interest in AI/ML frameworks; comfortable with APIs; proficiency in
    # German and English.
    # Apply: https://appliedai.jobs.personio.de/job/2690896?apply
    # Apply method: company-portal (Personio-hosted application form)
    {
        "folder": "appliedAI Munich Heilbronn Working Student AI Engineering Product Development",
        "company": "appliedAI Initiative GmbH",
        "lang": "en",
        "tag": "Data Science Master's Student | AI Agent Engineering and Evaluation Tooling | Python + LangGraph + LangChain",
        "role_strip": "Working Student, AI Engineering and Product Development",
        "cl_date": "6 September 2026",
        "cl_subject": "Working Student, AI Engineering and Product Development in Munich or Heilbronn",
        "profile": "Master's student in Data Science and Analytics at SRH Heidelberg based in Mannheim with hands on experience building and testing AI agent functionality in Python and evaluating AI systems against clear, reproducible metrics. I orchestrated a LangGraph multi agent RAG system with an independent LLM as Judge evaluation layer and shipped a Streamlit decision support tool that turns a fairness audit into a plain language output a non technical stakeholder can act on. Comfortable with Python, agent frameworks, REST APIs and building the kind of internal tooling that keeps an AI system accountable.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_RAG_EN, P_CREDITIQ_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_NVIDIA, CERT_AWS, CERT_GOOGLE],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am writing to apply for the Working Student position in AI Engineering and Product Development at appliedAI Initiative GmbH in Munich or Heilbronn. As a Master's student in Data Science and Analytics at SRH Heidelberg based in Mannheim, the mix of building and testing AI agent functionality in Python, automating workflows, and maintaining an internal maturity assessment tool maps closely to the agent evaluation and internal tooling work I have shipped over the last several months.",
            "In my Multi Agent RAG project I orchestrated a LangGraph based agent system in which a JudgeAgent scores generated answers on 5 dimensions in JSON mode at temperature 0, deliberately running the judge on a different local model from the generator to rule out self preference bias, with a hard failure on a missing judge model so a silent fallback to self judging cannot regress unnoticed. That same discipline of building agents, testing their behaviour systematically, and documenting where they fall short applies directly to developing and testing AI agent functionality with frameworks such as LangChain.",
            "In CreditIQ I used SHAP driven subgroup analysis to expose a hidden intersectional bias in a production credit scoring model that overall metrics alone would have missed, then shipped a Streamlit tool that turns the audit into a recommendation plus a plain language explanation for a non technical stakeholder, backed by unit tests at 100 percent branch coverage. That experience of turning a technical evaluation into a tool other people can actually use and trust is exactly the kind of internal tooling work described for the maturity assessment tool.",
            "I work comfortably in Python, am building hands on experience with LangGraph as an agent framework, and I am comfortable reading API documentation, running tests, and troubleshooting integrations. I hold the NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations, and Google Data Analytics certificates, and was named a Finalist at Graduate Level in the USAII Global AI Hackathon 2026. My German currently stands at B1, in progress, and I am fluent in English; I am aware the posting asks for proficiency in both German and English and want to be upfront that my German is not yet at full proficiency while I continue actively improving it. I would welcome the chance to discuss my contribution to your AI engineering team in person.",
        ],
    },

    # 3. KontextWork GbR, Hannover
    # Werkstudent:in KI-Engineer - Generative KI & LLM (m/w/d)
    # StepStone, posted about 1 month ago (older but still live), 16-20
    # hours per week, DE track
    # Tasks: evaluation, conception and development of AI solutions in a
    # business context; integration of a Drupal Wiki into existing AI
    # frameworks; building RAG systems; supporting customers in using
    # their company knowledge via AI.
    # Requirements: enjoys working with people, knowledge and IT systems;
    # experience with LLMs, RAG systems and prompting techniques, and with
    # automation tools such as Make, Zapier or n8n; programming knowledge
    # in Python, JavaScript or Java; analytical thinking.
    # Apply: https://www.stepstone.de/stellenangebote--Werkstudent-in-KI-Engineer-Generative-KI-LLM-m-w-d-Hanover-KontextWork-GbR-Inh-Sven-Reher-und-Andre-Ulrich--13730672-inline.html
    # Apply method: platform-native (StepStone Schnelle Bewerbung)
    {
        "folder": "KontextWork Hannover Werkstudent KI Engineer Generative KI LLM",
        "company": "KontextWork GbR",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | Generative KI und RAG Systeme | Python + LangGraph + Automatisierung",
        "role_strip": "Werkstudent, KI Engineer Generative KI und LLM",
        "cl_date": "6. September 2026",
        "cl_subject": "Werkstudent KI Engineer Generative KI und LLM in Hannover",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau von RAG Systemen, der Integration von LLMs in bestehende Wissenssysteme und der Automatisierung wiederkehrender Workflows. Ich habe ein Multi Agent RAG System ueber eine mehrsprachige Vektor Datenbank gebaut, das Unternehmenswissen durchsuchbar macht und mit LLM as Judge Evaluation absichert, und in einem Cloud Data Projekt eine Batch Pipeline mit 0 manuellen Eingriffen automatisiert. Sicher in Python, Prompting Techniken und der praktischen Integration von KI Modellen in bestehende Systeme.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_MOVIE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit als KI Engineer im Bereich Generative KI und LLM bei KontextWork GbR in Hannover. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim interessiert mich die in der Ausschreibung beschriebene Aufgabe, KI Loesungen im betrieblichen Umfeld zu evaluieren, zu konzipieren und zu entwickeln sowie RAG Systeme aufzubauen, weil ich in den letzten Monaten genau an dieser Schnittstelle gearbeitet habe.",
            "In meinem Multi Agent RAG Projekt habe ich eine hybride BM25 plus Dense Retrieval Pipeline ueber eine gemeinsame mehrsprachige Vektor Datenbank gebaut, sodass eine deutsche Anfrage gegen englische Quellen gestellt und vollstaendig auf Deutsch beantwortet werden kann, ohne den Dokumentenbestand zu duplizieren. Genau diese Kombination aus RAG Architektur und Wissensintegration deckt sich mit der in der Ausschreibung beschriebenen Aufgabe, Kunden bei der Nutzung ihres Unternehmenswissens mittels KI zu unterstuetzen, etwa ueber die Integration eines Drupal Wiki in bestehende KI Frameworks.",
            "In meinem Movie Analytics und ML Pipeline Projekt habe ich eine Batch Pipeline gebaut, die vollstaendig automatisiert ueber einen Cloud Scheduler Trigger mit 0 manuellen Eingriffen laeuft, von der Rohdatenerfassung bis zum fertigen Dashboard. Diese Erfahrung, wiederkehrende Arbeit systematisch in verlaessliche automatisierte Ablaeufe zu ueberfuehren, laesst sich direkt auf die in der Ausschreibung genannte Automatisierung von Workflows mit Tools wie Make, Zapier oder n8n uebertragen, auch wenn ich mit diesen konkreten Tools noch keine praktische Erfahrung habe.",
            "Ich arbeite sicher in Python und beschaeftige mich aktiv mit Prompting Techniken und dem Aufbau von RAG Systemen. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend, ich hebe es aktiv weiter, und Englisch spreche ich fliessend. Ich kann als Werkstudent in Hannover mit 16 bis 20 Stunden pro Woche flexibel einsteigen. Gerne bespreche ich meinen Beitrag zu Ihrem Team in einem persoenlichen Gespraech.",
        ],
    },
]
