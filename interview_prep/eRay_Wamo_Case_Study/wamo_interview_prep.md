# Wamo / AI4HAB — Interview Prep (revised)

Water-quality forecasting case study for **eRay GmbH** (via SRH). Sensor buoy on a lake
(Babenhäuser See) logs hourly readings. Goal: forecast harmful algal blooms early.

**My task:** forecast 4 targets for December, hour by hour —
`chl-a`, `turbidity`, `dissolved_oxygen`, `ph`.

---

## Core challenge (know this cold)
Recursive multi-step forecasting. Each predicted hour is fed back in as the lag feature
for the next hour. So December is forecast on top of my own forecasts, not real data —
**error compounds**. That's the hard part.

---

## Pipeline (orchestrated, gate-checked)
All steps chained in `9_orchestator.py`. After each step a **gate check** validates output
(NaN gate / flatline gate / bounds gate) and halts on failure instead of cascading bad data.

**1. Cleaning** — drop first 4 sparse rows, resample to clean 1-hour intervals.

**2. Outlier removal — 3 passes:**
- Pass 1: global physical bounds (ALL months) — impossible values → NaN (e.g. pH outside 7–9, chl-a > 200).
- Pass 2: seasonal hard caps (Oct/Nov only) — chl-a > 15, turbidity > 50 → NaN. Catches prolonged sensor fouling.
- Pass 3: 48h rolling z-score (Oct/Nov only, threshold 2.5) — catches short glitches.
- **Summer (Apr–Aug, and Sep) gets Pass 1 ONLY** — real blooms must be preserved, not deleted.

**3. Split interpolation (limit=4h):**
- Exogenous + physical targets (pH, DO): `interpolate(limit=4).bfill().ffill()` → zero NaN.
- Biological targets (chl-a, turbidity): `interpolate(limit=4)` ONLY — long gaps left NaN on purpose for MICE.
- `limit=4` = only bridge gaps up to 4 hours; longer gaps not interpolated (would invent data).

**4. Feature engineering:**
- Cyclical time: hour + month as sin/cos.
- Lags: 1h, 24h, 3d, 7d per target.
- Rolling stats: 24h mean & std.

**5. MICE bridge (Phase C, Oct/Nov):** IterativeImputer reconstructs chl-a/turbidity gaps
by predicting from correlated columns, then recalculates lags for targets only.

**5c. Forecast canvas (Phase D setup — "the future paradox"):** December has no real data,
so synthesize exogenous drivers with physics priors: temp exponential winter decay + diurnal
sine (±0.4°C), DOC decay to ~3.0 floor, conductivity linear drift, micro-noise. The 4 targets
are NOT filled here — they come from recursion.

**6/7. Model shootout + forecast — FORKED EXECUTION:**
- Path 1 (Ridge, RF, LGBM, XGBoost, CatBoost): step-by-step recursive loop.
- Path 2 (Prophet): DIRECT whole-horizon forecast, bypasses the loop, all lag/roll features stripped.
- Tree constraints: max_depth=4, lr=0.05.

**7. Ensemble + CI:**
- Ensemble = mean ± 1.96×std across models (secondary 95% band).
- **Headline interval = CatBoost Multi-Quantile:** alpha=0.05, 0.5, 0.85 → asymmetric 80% band.
  Hugs zero-floor on biologicals, chops top 15% to kill "summer ghosts."
- **Only the median (0.5) is fed back into recursion** — feeding a quantile back would explode exponentially.

---

## Key concepts (quick reference)

**Z-score** = (value − mean) / std → how many std's from average. ~±3 = rare. Used to flag
outliers. "Seasonal rolling" = 48h moving window in Oct/Nov, so each reading is judged against
its ±24h neighbours, not the whole year.

**alpha (quantiles)** = probability level. 0.5 = median, 0.05 = low edge, 0.85 = high edge.
0.05→0.85 = 80% wide band. Asymmetric because top side is tighter (cuts unrealistic winter spikes).

**Carbon Separation Rule:** DOC used as **concurrent feature only** (current hour, no lags, no rolling).
Reason: slow-moving + weak hourly autocorrelation, and lags would demand non-existent future values.
TOC excluded entirely (1:1 proxy → leakage); phycocyanin also excluded.

**RandomizedSearchCV** = hyperparameter tuner; samples random dial combos (cheaper than full grid).
Paired with **TimeSeriesSplit** (train on past, validate on next block, no shuffle) to avoid leakage.

**Honest R² divergence:** physicals (DO, pH ~0.81) score high — driven by exogenous drivers
(temp, sunlight), almost deterministic. Biologicals (chl-a ~0.44) low — stochastic, and I refused
to cheat with 1:1 proxies. Low R² is the honest result, not a failure. **CatBoost was champion.**

---

## Likely questions — ready answers
- Why TimeSeriesSplit not k-fold? No shuffling — can't train on future to predict past (leakage).
- Why trees over LSTM? Tabular, moderate data, strong lag features → boosting wins, cheaper to tune.
- Stop leakage in lags? Causal (past-only); in recursion lags filled with predictions, never future.
- Biggest weakness? chl-a accuracy + error accumulation over a month of recursion.

## Unresolved to fix before interview
Master doc says roster = "Gradient Boosting", but the ensemble code uses **Random Forest**.
Decide which is the real forecast roster. Based on running code: **RF**.
