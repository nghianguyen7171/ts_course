# Week 6–7 Practice Exercise: Stationarity, Unit Root, Differencing, AR/MA/ARMA

**Objective:** Use a healthcare time series to practice the full pipeline from unit root testing through model selection, AR/MA/ARMA fitting, and evaluation (aligned with slides 4.1 and 4.2).

## Dataset

- **File:** `data/healthcare_ts.csv`
- **Description:** Daily hospital admissions (simulated), one univariate series with columns `date` and `value`.
- **Length:** 730 daily observations (~2 years).

## Tasks (no solutions in this README)

1. **Load and explore**
   - Load the CSV, parse dates, set a datetime index.
   - Plot the series and compute basic statistics (mean, std, min, max). Comment on trend and variability.

2. **Unit root tests**
   - Run the Augmented Dickey–Fuller (ADF) test on the raw series.
   - Report the test statistic, p-value, and critical values. Conclude whether the series is stationary or has a unit root.
   - Optionally run the KPSS test and compare conclusions (trend stationary vs difference stationary).

3. **Differencing**
   - Compute the first difference of the series. Plot the differenced series.
   - Run the ADF test (and optionally KPSS) on the differenced series. Conclude whether the differenced series is stationary.

4. **ACF and PACF for model selection**
   - Plot the ACF and PACF of the **differenced** series (use a reasonable number of lags, e.g. 20–40).
   - Optionally plot ACF/PACF of the raw series for comparison.
   - Using the usual guidelines (PACF cutoff for AR order, ACF cutoff for MA order), suggest candidate orders (p, q) for the differenced series, and hence (p, d, q) with d = 1 for the original series (e.g. ARIMA(1,1,0), ARIMA(0,1,1), or ARIMA(1,1,1)).

5. **AR/MA/ARMA fit**
   - Fit 2–3 candidate ARIMA(p, 1, q) models (e.g. (1,1,0), (0,1,1), (1,1,1)).
   - Report estimated coefficients, AIC, and BIC for each model.
   - Choose a preferred model (e.g. by BIC or parsimony) and state the final order.

6. **Evaluation**
   - **Residual diagnostics:** Plot the ACF of the residuals of the chosen model. Run a Ljung–Box test (e.g. on the first several lags). Comment on whether the residuals behave like white noise.
   - **Forecast evaluation:** Split the data temporally (e.g. last 10–15% as test). Generate one-step or short-horizon forecasts for the test period. Compute RMSE and MAE. Plot forecasts vs actual values.

## Deliverables

- A Jupyter notebook (or script) that performs all steps above with brief interpretations.
- For the solution key, see `solution_key.ipynb` (instructor use).
