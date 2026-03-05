# Week 8B – Forecasting, Pipeline, Python, and Homework 4 (Practice)

**Part of:** Week 8 – ARIMA and Box–Jenkins Methodology  
**Format:** Lecture (practice and implementation)  
**CLOs:** 3.1, 4.1, 5.1, 6.1  
**See also:** [week8A_teaching_content.md](week8A_teaching_content.md) (ARIMA and Box–Jenkins theory)

---

## 1. Learning objectives (Week 8B)

By the end of this part, you should be able to:

- **Explain** the difference between **multi-step** and **rolling one-step-ahead** forecasts and when each is appropriate.
- **Describe** long-horizon forecast behaviour (mean reversion) and how **forecast intervals** widen with horizon.
- **Execute** the full ARIMA pipeline from data load to forecast evaluation using the checklist in this document.
- **Use** Python and Statsmodels: `adfuller`, `ARIMA`, `fit.forecast`, `get_forecast`, `acorr_ljungbox`, `plot_acf`, `plot_pacf` with correct arguments and interpretation of outputs.
- **Complete** Homework 4: end-to-end ARIMA on a given dataset with the suggested deliverables.

---

## 2. Forecasting – complete treatment

### 2.1 Point forecasts and forecast origin

- **Forecast origin:** The last time point \(n\) at which we have observed data. We forecast \(X_{n+1}, X_{n+2}, \ldots\).
- **Point forecast** for horizon \(h\): \(\hat{X}_{n+h \mid n} = E[X_{n+h} \mid X_1, \ldots, X_n]\), the conditional expectation under the fitted model. This is the “best” prediction in the mean-squared-error sense under the model.

### 2.2 Multi-step forecast (single fit)

**Procedure:**

1. Fit the ARIMA model **once** on the training sample (e.g. all data up to time \(n\), or data up to the start of the test set).
2. Call `fit.forecast(steps=h)` to obtain \(\hat{X}_{n+1}, \ldots, \hat{X}_{n+h}\) in one go.

**Long-horizon behaviour (stationary ARMA):**

- For a **stationary** ARMA process (i.e. the differenced series \(W_t\) is stationary), the **unconditional mean** \(\mu_W = E[W_t]\) and **unconditional variance** \(\sigma_W^2 = \mathrm{Var}(W_t)\) exist.
- As the forecast horizon \(h\) increases, the **forecast mean** of \(W_{n+h}\) tends to \(\mu_W\) (mean reversion), and the **forecast variance** of \(W_{n+h}\) tends to \(\sigma_W^2\).
- When we **reconstruct** the level \(X_{n+h}\) from the differenced forecasts (by summing back), the long-horizon forecast of \(X_{n+h}\) can look like a **flat line** (the series “reverts” to a constant level). So a **single** multi-step forecast from time \(n\) often does **not** track short-term fluctuations in the actual series; it reflects the long-run average behaviour.

**When to use:** When you need forecasts for **several steps ahead** from a **fixed** origin (e.g. “forecast the next 12 months from today”) and are interested in the medium/long-run level rather than tracking every short-term move.

### 2.3 One-step-ahead forecast

- **One-step-ahead:** At time \(t\), we forecast **only** \(X_{t+1}\) (i.e. \(h=1\)).
- **Accuracy:** One-step-ahead forecasts are typically **more accurate** than multi-step forecasts for the same horizon, because we use the most recent information and do not compound errors over many steps.

### 2.4 Rolling one-step-ahead forecasts (with optional re-estimation)

**Procedure:**

1. Split the data into **train** (e.g. up to time \(n_0\)) and **test** (e.g. \(n_0+1\) to \(n\)).
2. For **each** time point \(t\) in the test set (e.g. \(t = n_0+1, n_0+2, \ldots, n\)):
   - Use **all observed data up to time \(t-1\)** (optionally **re-estimate** the ARIMA model on \(X_1, \ldots, X_{t-1}\)).
   - Produce the **one-step-ahead** forecast \(\hat{X}_{t \mid t-1}\) for \(X_t\).
3. Collect the sequence of one-step-ahead forecasts for the test period and compare to actuals; compute MAE, RMSE.

**Why it tracks the series better:**

- Each forecast uses **only** the next step, so error does not accumulate over many steps.
- If we **re-estimate** at each origin, we use the **latest** parameter estimates and the most recent history. The forecasts therefore **follow** the local behaviour of the series more closely than a single multi-step forecast from the start of the test set.

**When to use:** When you want to **evaluate** how well the model would have predicted **one step at a time** on a test period, or when you want forecasts that **track** the actual series more closely (e.g. for comparison plots). See [../week6_7_exercise/solution_key.ipynb](../week6_7_exercise/solution_key.ipynb) Section 6.3 for the implementation and the comparison plot (multi-step vs rolling one-step).

### 2.5 Forecast intervals (confidence/prediction intervals)

- In addition to **point** forecasts, we often want **interval** forecasts: e.g. a 95% interval \([L_{n+h}, U_{n+h}]\) such that \(P(L_{n+h} \leq X_{n+h} \leq U_{n+h}) \approx 0.95\) under the model.
- **Sources of uncertainty:** (1) **Innovation** uncertainty (future \(\varepsilon_{n+1}, \ldots, \varepsilon_{n+h}\)); (2) **Parameter** uncertainty (we use estimates \(\hat{\phi}, \hat{\theta}\), not the true values). The forecast interval accounts for both; it **widens** as \(h\) increases because uncertainty accumulates.
- **In Statsmodels:** Use `get_forecast(steps=h)` instead of `forecast(steps=h)`. The returned object has:
  - `.predicted_mean`: point forecasts;
  - `.conf_int(alpha=0.05)`: confidence interval for the forecast (e.g. 95%).
- **Interpretation:** We expect the actual value to lie inside the interval with the stated probability (e.g. 95%) under the model assumptions. Wider intervals for larger \(h\) reflect increased uncertainty.

---

## 3. Full ARIMA pipeline – ordered checklist

Use this as a step-by-step guide for an end-to-end ARIMA analysis. The implemented example is in [../week6_7_exercise/solution_key.ipynb](../week6_7_exercise/solution_key.ipynb) (Sections 1–6, including 6.2 and 6.3).

### Step 1: Load data and set index

- Read the dataset (e.g. CSV); parse date columns and set a **datetime index** so that the series is properly ordered in time.
- Extract the univariate series (e.g. `y = df["value"]`).

### Step 2: Exploratory data analysis (EDA)

- **Plot** the series (time on x-axis, value on y-axis). Comment on:
  - **Trend:** upward, downward, or none.
  - **Seasonality:** periodic patterns (e.g. yearly, monthly).
  - **Variability:** constant variance or changing (e.g. increasing with level).
- **Summary statistics:** mean, standard deviation, min, max (e.g. `y.describe()`). Note the sample size and date range.

### Step 3: Test stationarity (raw series)

- Run the **ADF test** on the **raw** series: `adfuller(y, autolag="AIC")`.
- Report: test statistic, p-value, critical values.
- **Conclusion:** If p-value &gt; 0.05 (or similar threshold), do **not** reject unit root → treat as **non-stationary** → proceed to differencing. If p-value &lt; 0.05, the series may be stationary → consider d=0 and still check ACF/PACF.

### Step 4: Differencing and choice of d

- Compute the **first difference:** e.g. `dy = y.diff().dropna()`.
- **Plot** the differenced series. Run **ADF** on the differenced series.
- If the differenced series is **stationary** (ADF rejects unit root), set **d = 1**. If not, try second difference and set **d = 2** if needed.
- **Document** your choice of d with justification (ADF results, possibly ACF of raw series).

### Step 5: Identify (p, q) from ACF/PACF

- Work with the **differenced** series \(W_t\) (e.g. `dy` when d=1).
- Plot **ACF** and **PACF** of \(W_t\) (e.g. 20–40 lags): `plot_acf(dy, lags=40)`, `plot_pacf(dy, lags=40, method="ywm")`.
- Apply the **identification guidelines** (Week 8A): PACF cutoff → AR order p; ACF cutoff → MA order q; both tail off → try ARIMA(p,d,q).
- List **2–3 candidate** orders (e.g. (1,1,0), (0,1,1), (1,1,1)).

### Step 6: Estimate candidate models

- For each candidate `(p, d, q)`, fit: `model = ARIMA(y, order=(p,d,q))`, `fit = model.fit()`.
- For each fit, report: **estimated coefficients** (e.g. `fit.params`), **AIC** (`fit.aic`), **BIC** (`fit.bic`).
- **Choose** a preferred model (e.g. **lowest BIC** or by parsimony). State the chosen order clearly.

### Step 7: Residual diagnostics

- Extract residuals: `resid = fit.resid` (or the residuals of the chosen model).
- **ACF of residuals:** `plot_acf(resid, lags=...)`. Check that spikes lie within the confidence band (e.g. \(\pm 1.96/\sqrt{n}\)).
- **Ljung–Box test:** `acorr_ljungbox(resid, lags=range(1, 21), return_df=True)` (or similar). Check that p-values are **large** (e.g. &gt; 0.05).
- **Conclusion:** If diagnostics are **satisfactory**, proceed to forecasting. If **not** (e.g. significant residual ACF or small Ljung–Box p-value), return to **Step 5** and try a different (p,d,q), then re-estimate and re-check.

### Step 8: Forecast and evaluate

- **Split:** e.g. last 10–15% of the data as **test** set; rest as **train**.
- **Multi-step:** Fit the chosen model on **train**, then `fit.forecast(steps=len(test))`; compute **RMSE** and **MAE** on the test set; plot forecasts vs actuals.
- **Rolling one-step (optional):** For each test point, (optionally re-estimate and) forecast one step ahead; collect forecasts; compute RMSE and MAE; plot vs actuals (see solution_key Section 6.3).
- **Report:** Test RMSE, test MAE; brief comment on whether the model is adequate for the intended use.

### Step 9: Optional – forecast intervals and future forecasts

- Use `get_forecast(steps=h)` to obtain point forecasts and confidence intervals for the next \(h\) periods.
- Plot historical data, point forecast, and interval (e.g. 95%) for interpretation.

---

## 4. Python and Statsmodels – function reference

All functions below appear in [../week6_7_exercise/solution_key.ipynb](../week6_7_exercise/solution_key.ipynb). Use the same imports and patterns for consistency.

### 4.1 Imports

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.stats.diagnostic import acorr_ljungbox
```

### 4.2 Augmented Dickey–Fuller test

**Function:** `adfuller(y, autolag="AIC", maxlag=None, ...)`

- **Purpose:** Test the null hypothesis that the series has a **unit root** (non-stationary).
- **Arguments:**
  - `y`: 1-d array or pandas Series (the time series).
  - `autolag`: Method for choosing the number of lags in the ADF regression; `"AIC"` or `"BIC"` are common.
  - `maxlag`: Maximum number of lags to consider (optional; if None, a default rule is used).
- **Returns:** A tuple; commonly unpacked as:
  - `adf_stat`: ADF test statistic (more negative → more evidence against unit root).
  - `pvalue`: p-value. **Small** (e.g. &lt; 0.05) → reject unit root → **stationary**.
  - `usedlag`: Number of lags used.
  - `nobs`: Number of observations used.
  - `critical_values`: Dict of critical values at 1%, 5%, 10%.
  - `icbest`: Value of the information criterion for the chosen lag (if autolag used).

**Example:** `adf_raw = adfuller(y, autolag="AIC"); print("ADF stat:", adf_raw[0], "p-value:", adf_raw[1])`

### 4.3 ARIMA model

**Class:** `ARIMA(endog, order=(p, d, q), ...)`

- **Purpose:** Specify an ARIMA(p,d,q) model.
- **Arguments:**
  - `endog`: The observed time series (1-d array or Series). Use the **level** \(X_t\), not the differenced series; the model applies differencing internally when d &gt; 0.
  - `order`: Tuple `(p, d, q)`.
- **Methods:**
  - `.fit()`: Estimate the model by maximum likelihood. Returns a **Results** object (e.g. `fit`).

**Results object (fit):**

- `fit.params`: Estimated parameters (AR and MA coefficients, constant, variance).
- `fit.aic`: Akaike Information Criterion.
- `fit.bic`: Bayesian Information Criterion.
- `fit.resid`: Residuals (same length as endog, with NaNs where not defined).
- `fit.summary()`: Text summary of the model (coefficients, standard errors, AIC, BIC, etc.).
- `fit.forecast(steps=h)`: Point forecasts for the next `h` steps. Returns a array-like (e.g. pandas Series with a datetime index if the model was fit with a Series).
- `fit.get_forecast(steps=h)`: Returns a **Forecast** object with `.predicted_mean` and `.conf_int(alpha=0.05)` for forecast intervals.

**Example:** `model = ARIMA(y, order=(1, 1, 0)); fit = model.fit(); print(fit.summary())`

### 4.4 Forecasts

- **Point forecasts only:** `fc = fit.forecast(steps=12)` → `fc` is the forecast for the next 12 periods.
- **With intervals:** `fcast = fit.get_forecast(steps=12); mean = fcast.predicted_mean; ci = fcast.conf_int(alpha=0.05)`.

### 4.5 Ljung–Box test (residuals)

**Function:** `acorr_ljungbox(resid, lags=None, model_df=0, return_df=True, ...)`

- **Purpose:** Test whether the **residuals** are uncorrelated (white noise) up to a given lag.
- **Arguments:**
  - `resid`: 1-d array or Series of **residuals**.
  - `lags`: Int or array-like. If int, tests at lags 1, 2, …, lags. If array-like, tests at those specific lags.
  - `model_df`: Number of parameters estimated (degrees-of-freedom adjustment). For ARIMA(p,d,q) without constant, often `p+q`; with constant, `p+q+1`. Default 0; can leave default or set for a more accurate null distribution.
  - `return_df`: If True, returns a pandas DataFrame with columns such as `lb_stat` (Ljung–Box statistic) and `lb_pvalue` (p-value).
- **Returns:** If `return_df=True`, a DataFrame with one row per lag group and columns including the test statistic and **p-value**.
- **Interpretation:** **Large p-value** (e.g. &gt; 0.05) → do not reject “residuals are white noise” → model adequate. **Small p-value** → reject → residual autocorrelation → model may be inadequate.

**Example:** `lb = acorr_ljungbox(fit.resid, lags=20, return_df=True); print(lb[["lb_stat", "lb_pvalue"]])`

### 4.6 ACF and PACF plots

**Functions:** `plot_acf(x, lags=None, ax=None, alpha=0.05, ...)` and `plot_pacf(x, lags=None, ax=None, alpha=0.05, method="ywm", ...)`

- **Purpose:** Plot the **sample ACF** or **sample PACF** of a series (or residuals) with confidence bands.
- **Arguments:**
  - `x`: 1-d array or Series.
  - `lags`: Number of lags to display (e.g. 40). If None, a default is used.
  - `ax`: Matplotlib axis; if None, current axis or new figure.
  - `alpha`: Significance level for the confidence band (e.g. 0.05 for 95% band). The band is typically \(\pm z_{\alpha/2}/\sqrt{n}\).
  - `method` (PACF only): Method for computing PACF; `"ywm"` (Yule–Walker with bias correction) is common.
- **Usage:** For the **differenced** series: `plot_acf(dy, lags=40)`, `plot_pacf(dy, lags=40, method="ywm")`. For **residuals**: `plot_acf(fit.resid, lags=40)`.

---

## 5. Homework 4

**From the syllabus:** End-to-end ARIMA on a given dataset.

### 5.1 Suggested deliverables

1. **Data and EDA**
   - Load the given dataset; set a datetime index.
   - Plot the series; comment on trend, seasonality, variability.
   - Report basic statistics (mean, std, min, max, sample size).

2. **Stationarity and differencing**
   - Run the ADF test on the raw series; report test statistic and p-value; conclude stationary or non-stationary.
   - If non-stationary, compute the first (and if needed second) difference; run ADF on the differenced series; **justify the choice of d**.

3. **Identification**
   - Plot ACF and PACF of the **differenced** series.
   - State 2–3 **candidate** orders (p,d,q) with brief justification from the ACF/PACF.

4. **Estimation and model choice**
   - Fit each candidate ARIMA model; report estimated coefficients, AIC, and BIC.
   - **Choose** a preferred model (e.g. by BIC); state the final order and why you chose it.

5. **Residual diagnostics**
   - Plot the ACF of the residuals of the chosen model.
   - Run the Ljung–Box test on the residuals.
   - **Comment** on whether the residuals are consistent with white noise; if not, note what you would try next.

6. **Forecasting and evaluation**
   - Split the data (e.g. last 10–15% as test).
   - Generate multi-step (and optionally rolling one-step) forecasts for the test period.
   - Report **MAE** and **RMSE** (and optionally MAPE); plot forecasts vs actuals.

7. **Short report**
   - Problem statement; method (how you chose d, p, q; diagnostics); results (chosen model, order, AIC/BIC, MAE/RMSE, key plots); brief conclusions and limitations.

### 5.2 What to avoid

- Do not skip the justification for d and (p,q).
- Do not ignore residual diagnostics; if they fail, discuss and (if possible) try an alternative model.
- Do not forget to report units when stating MAE/RMSE (same as the series).

---

## 6. References

### Course textbooks

- **Kirchgässner, G., & Wolters, J. (2013).** *Introduction to Modern Time Series Analysis.* Springer. — ARIMA and Box–Jenkins.
- **Atwan, T. A. (2022).** *Time Series Analysis with Python Cookbook.* Packt. — Python recipes.
- **Huang, C., & Petukhina, A. (2022).** *Applied Time Series Analysis and Forecasting with Python.* Springer. — Applied TS with Python.

### Online

- **Penn State STAT 510:** https://online.stat.psu.edu/stat510/ — ARIMA and Box–Jenkins.

### Internal project materials

- **Slides:** 4.1 and 4.2; supplement `Time_Series_ARMA_Modeling.pdf`.
- **Exercises:** [../week6_7_exercise/README.md](../week6_7_exercise/README.md), [../week6_7_exercise/solution_key.ipynb](../week6_7_exercise/solution_key.ipynb); [../eeg_emg_exercise/eeg_emg_practice_exercises.html](../eeg_emg_exercise/eeg_emg_practice_exercises.html).
- **ACF/PACF:** [../acf_problem_set.md](../acf_problem_set.md).
- **Topic example:** [../../Topic/9.Airline_Passengers/README.md](../../Topic/9.Airline_Passengers/README.md) (Box–Jenkins, AIC/BIC, MAE/RMSE/MAPE).

---

## 7. Link to Week 9

**Week 9 (Lab 4)** applies the Week 8 methodology to **project data**: each group reports ARIMA models for key series (chosen p,d,q with justification), model selection (AIC/BIC), residual diagnostics, short-term forecast plots, and forecast accuracy metrics. The instructor also outlines the **Midterm Project Baseline** (report + slides). This document and **Week 8A** are the methodological references for that lab and for the classical (ARIMA/SARIMA) part of the midterm baseline.
