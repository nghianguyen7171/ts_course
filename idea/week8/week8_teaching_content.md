# Week 8 – ARIMA and Box–Jenkins Methodology

**Week:** 8  
**Format:** Lecture  
**CLOs:** 3.1, 4.1, 5.1, 6.1  
**Assessment:** Homework 4 (end-to-end ARIMA on a given dataset)

---

## Document structure (8A and 8B)

The Week 8 content is split into two sub-documents for clarity and length:

| Document | Content | Use when |
|----------|---------|----------|
| **[week8A_teaching_content.md](week8A_teaching_content.md)** | **Theory:** ARIMA(p,d,q) definitions, backshift notation, role of d/p/q; Box–Jenkins (Identification, Estimation, Diagnostic checking, Forecasting); model selection (AIC/BIC, residual diagnostics, MAE/RMSE/MAPE formulas). | Learning concepts and methodology. |
| **[week8B_teaching_content.md](week8B_teaching_content.md)** | **Practice:** Forecasting (multi-step, rolling one-step, intervals); full ARIMA pipeline checklist; Python/Statsmodels function reference; Homework 4 deliverables; references; link to Week 9. | Implementing the pipeline and doing Homework 4. |

**Recommendation:** Work through **8A** first for definitions and the Box–Jenkins steps, then **8B** for the pipeline, code, and homework.

---

## 1. Learning objectives (overview)

By the end of Week 8, students should be able to:

- **Define and interpret** ARIMA(p,d,q): role of differencing (d), interpretation of p and q; link to ARMA on the differenced series.
- **Apply** the Box–Jenkins methodology: Identification → Estimation → Diagnostic checking → Forecasting, and iterate when diagnostics fail.
- **Use** AIC/BIC and residual diagnostics (ACF of residuals, Ljung–Box) to select and validate models.
- **Implement** the full ARIMA pipeline in Python with Statsmodels: load data, test stationarity, difference, identify (p,q), estimate, diagnose, forecast.
- **Compute and interpret** forecast error metrics (MAE, RMSE, optionally MAPE) and understand multi-step vs rolling one-step forecasts.

---

## 2. Prerequisites (brief)

- **Weeks 6–7:** Stationarity, ADF test, differencing; AR/MA/ARMA; ACF/PACF for order choice.
- **Materials:** Slides 4.1 and 4.2; [../week6_7_exercise/README.md](../week6_7_exercise/README.md); [../acf_problem_set.md](../acf_problem_set.md).

---

## 3. ARIMA and Box–Jenkins (condensed)

- **ARIMA(p,d,q):** Model the **d-th difference** \(W_t = \nabla^d X_t\) as **ARMA(p,q)**. Choose **d** by unit root tests (ADF); choose **(p,q)** by ACF/PACF of \(W_t\).
- **Box–Jenkins:** (1) **Identify** d and (p,q). (2) **Estimate** by ML. (3) **Diagnose** residuals (ACF, Ljung–Box); if not white noise, re-identify. (4) **Forecast** and evaluate (MAE, RMSE).
- **Model choice:** Prefer lower **AIC** or **BIC**; BIC favours parsimony. Confirm adequacy with residual diagnostics.

Full definitions, formulas, and examples: **[week8A_teaching_content.md](week8A_teaching_content.md)**.

---

## 4. Pipeline and implementation (condensed)

- **Pipeline order:** Load → EDA → ADF (raw) → differencing → ADF (differenced) → ACF/PACF → fit candidates → choose by AIC/BIC → residual diagnostics → forecast and evaluate.
- **Forecasting:** **Multi-step** from a single fit reverts to the long-run mean; **rolling one-step** (optionally re-estimating) tracks the series better. Use `get_forecast` for intervals.
- **Python:** `adfuller`, `ARIMA(y, order=(p,d,q)).fit()`, `fit.forecast(steps=h)`, `get_forecast`, `acorr_ljungbox`, `plot_acf`, `plot_pacf`.

Full checklist, function reference, and Homework 4: **[week8B_teaching_content.md](week8B_teaching_content.md)**. Implemented example: [../week6_7_exercise/solution_key.ipynb](../week6_7_exercise/solution_key.ipynb).

---

## 5. Homework 4 (brief)

End-to-end ARIMA on a given dataset: load data, EDA, stationarity/differencing (justify d), identification (ACF/PACF), estimation (2–3 candidates, AIC/BIC), residual diagnostics, forecast evaluation (MAE, RMSE, plots), and a short report. Full deliverables: **[week8B_teaching_content.md](week8B_teaching_content.md)** §5.

---

## 6. References (brief)

- **Textbooks:** Kirchgässner & Wolters (2013); Atwan (2022); Huang & Petukhina (2022).
- **Online:** PSU STAT 510 (https://online.stat.psu.edu/stat510/).
- **Internal:** Week 6–7 slides and [../week6_7_exercise/](../week6_7_exercise/); [../acf_problem_set.md](../acf_problem_set.md); [../../Topic/9.Airline_Passengers/README.md](../../Topic/9.Airline_Passengers/README.md).

---

## 7. Link to Week 9

Week 9 (Lab 4) applies ARIMA on **project data** (model choice, diagnostics, forecasts, metrics) and introduces the **Midterm Project Baseline**. Week 8 (8A and 8B) is the methodological reference for that lab.
