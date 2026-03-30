# Week 10: Seasonality, SARIMA, and SARIMAX

## Objective
In this lab, you will build quantitative forecasting models for urban power consumption, integrating both cyclical seasonal behaviors and extreme meteorological exogenous variables. You will learn to identify seasonality, perform seasonal differencing, establish a SARIMA baseline, and elevate it to a SARIMAX architecture using weather features.

## Dataset
We will use the **Tetuan City Power Consumption** dataset. It provides power consumption measurements (originally 10-minute intervals, which we will resample to hourly) alongside weather-related features like Temperature, Humidity, Wind Speed, and General Diffuse Flows.

### Local Setup
1. Download the dataset from Kaggle: [Tetuan City Power Consumption](https://www.kaggle.com/datasets/gmkeshav/tetuan-city-power-consumption)
2. Create a folder named `data/` in your current directory.
3. Place the downloaded `Tetuan City power consumption.csv` inside the `data/` folder.
4. Run the data preparation script to resample the dataset from 10-minute intervals to hourly intervals:
   ```bash
   python generate_dataset.py
   ```
   This will generate `data/hourly_tetuan_power.csv`.

### Kaggle Setup
If you are running this notebook on Kaggle:
1. Click **"Add Data"** in the right sidebar.
2. Search for `gmkeshav/tetuan-city-power-consumption` and add it to your environment.
3. Run the data preparation script or load the data directly in your notebook and perform the hourly resampling (`df.resample('H').mean()`).

---

## Lab Tasks

### 1. Data Preparation and Resampling
- Load the raw dataset and parse the `DateTime` column.
- Resample the high-frequency 10-minute data to an hourly frequency (`'H'`) using `.mean()` to reduce micro-noise and create a stable temporal structure.
- Select a subset of the data (e.g., the first 2 months: Jan-Feb 2017) to make computation and visualization more manageable. 
- Define your target variable (e.g., `Zone 1 Power Consumption`).

### 2. Decomposition and Seasonality Analysis
- Use `seasonal_decompose` (with `period=24`) to dissect the target series into its constituent parts: Observed, Trend, Seasonal, and Residual.
- Visualize the decomposition. Observe the daily rhythm (24 hours) of power consumption.

### 3. Stationarization Pipeline (Hyndman Protocol)
- Perform the Augmented Dickey-Fuller (ADF) test on the original series to check for stationarity.
- Apply **seasonal differencing** (lag=24) to strip away the daily seasonality.
- Perform the ADF test again on the seasonally differenced series to confirm it has reached a stationary state. **Do not over-difference** if the series is already stationary after the seasonal step.

### 4. Identification (ACF / PACF)
- Plot the Autocorrelation Function (ACF) and Partial Autocorrelation Function (PACF) of the seasonally differenced series (up to 75 lags).
- Identify the **Non-seasonal** AR/MA terms by looking at the early lags (1, 2, 3...).
- Identify the **Seasonal** AR/MA terms by looking at the seasonal lags (24, 48, 72...).

### 5. Baseline Modeling: SARIMA
- Construct a closed-system SARIMA model based on the identified $(p, d, q) \times (P, D, Q)_s$ orders.
- Fit the model to the target variable using Maximum Likelihood Estimation.
- Print the model summary and note the **AICc** metric. 

### 6. Upgrading to SARIMAX (Exogenous Variables)
- Extract weather features such as `Temperature` and `Humidity` to act as exogenous forces ($X$).
- Construct a SARIMAX model using the same parameters as the baseline SARIMA, but this time include the exogenous variables using the `exog` parameter.
- Fit the model and print the summary.
- Compare the **AICc** of the SARIMAX model with the SARIMA baseline. Does the inclusion of meteorological data improve the model?

### 7. Diagnostic Validation
- Plot the model diagnostics for your SARIMAX model (`plot_diagnostics()`).
- Verify the standard assumptions of the residuals:
  - Do they resemble White Noise?
  - Does the Q-Q plot show a normal distribution?
  - What does the Ljung-Box test imply?
- Check the p-values of the exogenous variables in the model summary to confirm their statistical significance ($p < 0.05$).

### 8. Forecasting
- Generate forecasts for a hold-out test period.
- Plot the actual values vs. the predicted values.

---

## Deliverables
- A complete, well-commented Jupyter Notebook following the steps above.
- Clear markdown cells interpreting the ACF/PACF plots and justifying your chosen SARIMA orders.
- A comparison of your SARIMA vs. SARIMAX models, analyzing whether the external weather variables improved the forecasting power.
- A concise interpretation that connects model output to practical energy operations (staffing, dispatch, demand planning), not only theory.

## Submission Note
- If you present this lab in slides, add your source code link on the final slide (GitHub repository URL or any accessible versioned code link).
