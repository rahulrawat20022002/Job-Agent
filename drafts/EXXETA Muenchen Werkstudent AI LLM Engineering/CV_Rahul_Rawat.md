# Rahul Rawat

## Werkstudent AI und LLM Engineering

Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau generativer KI Loesungen von der ersten Idee bis zur produktionsnahen Anwendung. Ich habe ein Multi Agent RAG System mit LLM as Judge Evaluation gebaut und in CreditIQ ein Kredit Scoring System entwickelt, das eine Fairness Grenze von 0,79 auf 0,88 gehoben hat. Sicher in Python, LangGraph, RAG Architekturen und der Uebersetzung von Geschaeftsanforderungen in lauffaehige KI Loesungen.

### Experience

**eRay GmbH**, Data Scientist, Oct 2025 to Mar 2026

* In einer 6 monatigen Zusammenarbeit zwischen eRay GmbH und SRH Hochschule Heidelberg zur Prognose der Seewasserqualität über 4 Ziel Indikatoren Chlorophyll a, Trübung, pH und gelösten Sauerstoff wurde eine end to end rekursive Zeitreihen Pipeline über einen 40 Feature Raum mit einem Ziel Lag Set lag_1h, lag_24h, lag_3d, lag_7d, lag_roll_mean_24h und lag_roll_std_24h aufgebaut.
* Es wurden 6 Kandidaten direkt verglichen Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost und Prophet mit strikten Tree Einschränkungen max_depth 4 und learning_rate 0.05, die Entscheidung fiel auf CatBoost MultiQuantile bei alpha 0.05, 0.5 und 0.85, was asymmetrische 80 Prozent Vorhersageintervalle lieferte, die den 0 Boden umarmen und die oberen 15 Prozent der Sommer Ghost Spikes abschneiden.
* Die September Evaluation wurde belastbar gemacht mit einem 3 Pass Outlier System pH verengt von 0 bis 14 auf 7.0 bis 9.0, Oct und Nov Caps von 15.0 bei Chlorophyll a und 50.0 bei Trübung, ein rollender z-score bei z>2.5 über 48 Stunden, und 5 spärliche Sensoren plus 3 zeitgleiche Proxies phycocyanin_abs, phycocyanin_abs_comp und toc wurden ausgeschlossen, was die ehrliche R quadrat Aufteilung von 0.86 bei gelöstem Sauerstoff und 0.81 bei pH offenlegte.
* Oct und Nov Lücken wurden mit IterativeImputer MICE rekonstruiert, eine vollständige Memory Buffer Neuberechnung über alle 6 Lag Features durchgeführt, ein synthetisches Winter Canvas mit 4 Grad Celsius Boden und 0.4 Grad diurnaler Amplitude generiert und das Ganze in einen Orchestrator mit Gate Checks, ökologischen Clips gelöster Sauerstoff 4.0 bis 18.0 und pH 6.0 bis 9.0 und einem 0.003 pH pro Stunde Velocity Clamp eingebettet.
