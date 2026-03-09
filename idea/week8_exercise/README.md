# Week 8 Lab Exercise: ARIMA, Box–Jenkins, Model Selection, Forecasting

**Objective:** Apply the Box–Jenkins methodology to a real dataset: identify ARIMA orders, compare models with AIC/BIC, perform residual diagnostics, and evaluate multi-step and rolling one-step-ahead forecasts (aligned with Week 8 slides and teaching content).

## Dataset

- **File:** `data/air_passengers.csv`
- **Description:** Monthly totals of international airline passengers (1949–1960), 144 observations.
- **Source:** Classic Box & Jenkins (1970) dataset, fetched via `statsmodels.datasets.get_rdataset("AirPassengers", "datasets")`.
- **Columns:** `date`, `Passengers`.

## Tasks (no solutions in this README)

1. **Load and quick EDA**
   - Load the CSV, parse dates, set a datetime index.
   - Plot the series and compute basic statistics (mean, std, min, max). Comment on trend, seasonality, and variability.

2. **Stationarity check and differencing (recap)**
   - Run the ADF test on the raw series. Conclude whether the series has a unit root.
   - Compute the first difference. Plot the differenced series and run ADF again. Conclude whether differencing is sufficient; set d.
   - *(This recaps Weeks 6–7; keep it brief.)*

3. **Box–Jenkins Identification**
   - Plot the ACF and PACF of the differenced series (e.g. 20–30 lags).
   - Using the standard guidelines (PACF cutoff → AR order, ACF cutoff → MA order), propose 3–4 candidate ARIMA(p,d,q) orders (e.g. (1,1,0), (0,1,1), (1,1,1), (2,1,1)).
   - Briefly explain why each candidate is plausible from the ACF/PACF.

4. **Estimation and model comparison (AIC/BIC)**
   - Fit each candidate ARIMA model.
   - For each, report: estimated coefficients, AIC, and BIC.
   - Build a comparison table (DataFrame) and choose the preferred model. Justify your choice (e.g. lowest BIC, parsimony).

5. **Residual diagnostics**
   - Plot the ACF of the residuals of the chosen model (should be within confidence bands).
   - Run the Ljung–Box test on the residuals (e.g. lags 1–20). Report p-values.
   - Plot a histogram (or QQ-plot) of residuals and residuals over time.
   - Conclude whether the residuals behave like white noise. If not, discuss what to try next.

6. **Forecasting: multi-step vs rolling one-step**
   - Split the data temporally (e.g. last 24 months as test).
   - **Multi-step:** Fit on train, forecast the full test horizon. Compute RMSE and MAE.
   - **Rolling one-step-ahead:** At each test point, re-estimate the model using all data up to that point and forecast one step. Compute RMSE and MAE.
   - Compare the two approaches in a table and plot both forecasts vs actuals.

7. **Forecast intervals**
   - Using `get_forecast`, produce 95% forecast intervals for the test period.
   - Plot historical data, point forecast, and shaded 95% interval.
   - Comment on how the interval width changes with horizon and what this means for practical use.

## Deliverables

- A Jupyter notebook (or script) that performs all steps above with brief interpretations.
- For the solution key, see `solution_key.ipynb` (instructor use).

## Notes

- This dataset has **seasonality** (yearly pattern). A non-seasonal ARIMA will not capture it perfectly; this is expected. Note the limitation and mention that SARIMA (Week 11) is the proper extension.
- Focus on the **methodology** (Box–Jenkins steps, diagnostics, forecast comparison) rather than achieving the best possible fit.
