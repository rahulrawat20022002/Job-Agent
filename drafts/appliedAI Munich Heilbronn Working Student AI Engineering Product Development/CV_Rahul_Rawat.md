# Rahul Rawat

## Working Student, AI Engineering and Product Development

Master's student in Data Science and Analytics at SRH Heidelberg based in Mannheim with hands on experience building and testing AI agent functionality in Python and evaluating AI systems against clear, reproducible metrics. I orchestrated a LangGraph multi agent RAG system with an independent LLM as Judge evaluation layer and shipped a Streamlit decision support tool that turns a fairness audit into a plain language output a non technical stakeholder can act on. Comfortable with Python, agent frameworks, REST APIs and building the kind of internal tooling that keeps an AI system accountable.

### Experience

**eRay GmbH**, Data Scientist, Oct 2025 to Mar 2026

* During a 6 month eRay GmbH and SRH Heidelberg collaboration to forecast lake water quality across 4 target indicators chlorophyll a, turbidity, pH and dissolved oxygen, built an end to end recursive time series pipeline over a 40 feature space with a per target lag suite lag_1h, lag_24h, lag_3d, lag_7d, lag_roll_mean_24h and lag_roll_std_24h.
* Benchmarked 6 candidates Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost and Prophet with strict tree constraints max_depth 4 and learning_rate 0.05, landed on CatBoost MultiQuantile at alpha 0.05, 0.5 and 0.85, producing asymmetric 80 percent prediction intervals that hug the 0 floor and chop the top 15 percent of summer ghost spikes.
* Made the September evaluation defensible with a 3 pass outlier system pH tightened from 0 to 14 down to 7.0 to 9.0, Oct and Nov caps of 15.0 on chlorophyll a and 50.0 on turbidity, and a rolling z-score at z>2.5 over 48 hours, and excluded 5 sparse sensors plus 3 concurrent proxies phycocyanin_abs, phycocyanin_abs_comp and toc, surfacing the honest R squared of 0.86 on dissolved oxygen and 0.81 on pH.
* Reconstructed Oct and Nov gaps with IterativeImputer MICE, ran full Memory Buffer recalculation across all 6 lag features, generated a synthetic winter canvas with 4 degree Celsius floor and 0.4 degree diurnal amplitude, then wrapped it all in an orchestrator with gate checks, ecological clips dissolved oxygen 4.0 to 18.0 and pH 6.0 to 9.0 and a 0.003 pH per hour velocity clamp.
