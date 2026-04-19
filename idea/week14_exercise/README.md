# Time Series Forecasting: Traditional vs ML vs Deep Learning

## Objective
This lab combines all three forecasting paradigms into a single notebook, applied to the **Beijing PM2.5 Air Quality** dataset (~44K hourly observations, 2010–2014):

| Part | Approach | Models |
|------|----------|--------|
| **A** | Traditional | ARIMA, GARCH volatility analysis |
| **B** | Machine Learning | Linear Regression, Random Forest, XGBoost |
| **C** | Deep Learning | LSTM (basic & regularized), GRU, 1D-CNN |

All models forecast hourly PM2.5 concentration with the same train/test split (pre-2014 / 2014), enabling a fair head-to-head comparison.

## Dataset
**Beijing PM2.5 Air Quality** — hourly PM2.5 readings with weather covariates (temperature, pressure, dewpoint, wind speed).

### Kaggle Setup (Preferred)
1. Create a new Kaggle Notebook.
2. **Add Data** → search for `trongnghia7171/beijing-air-quality`.
3. **Settings → Accelerator → GPU** (recommended for DL sections).

### Local Setup
1. Download from Kaggle: [Beijing Air Quality](https://www.kaggle.com/datasets/trongnghia7171/beijing-air-quality)
2. Place `beijing_air_quality.csv` inside `data/`.
3. Alternatively, run `python generate_dataset.py` if you have the raw PRSA CSV.

---

## Lab Structure

### Part A: Traditional Models
1. **ARIMA** — Univariate baseline on daily-averaged PM2.5.
2. **GARCH** — Volatility analysis on ARIMA residuals.

### Part B: Machine Learning
3. **Feature Engineering** — Lag features, rolling statistics, calendar variables.
4. **Model Training** — Linear Regression, Random Forest, XGBoost.
5. **Feature Importance** — What drives predictions?
6. **Temporal Validation** — TimeSeriesSplit cross-validation.

### Part C: Deep Learning
7. **DL Preprocessing** — Scale, window into 3D tensors (samples × time steps × features).
8. **LSTM** — Basic and regularized (stacked + Dropout).
9. **GRU** — Lighter recurrent alternative.
10. **1D-CNN** — Convolutional approach to temporal patterns.
11. **Multi-step Forecasting** — Predict the next 6 hours simultaneously.

### Grand Comparison
12. **All-models comparison table** — MAE/RMSE across Traditional, ML, DL.
13. **Forecast overlay plot** — Visual comparison on the same test window.
14. **Discussion** — When to use which paradigm.

---

## Deliverables
- A complete notebook with all sections executed.
- Training curves for each DL model.
- Feature importance plots for ML models.
- A grand comparison table and forecast overlay plot.
- A brief written discussion on the trade-offs between paradigms.

## Submission Note
- If you present this lab in slides, add your source code link on the final slide (GitHub repository URL or any accessible versioned code link).
