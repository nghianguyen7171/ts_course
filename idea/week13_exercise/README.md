# Week 13: Machine Learning for Time Series Forecasting

## Objective
In this lab you will apply the full ML-for-time-series pipeline to real air-quality data. You will:
1. Briefly explore ARCH/GARCH volatility modeling on ARIMA residuals.
2. Transform a time series into a supervised-learning dataset via feature engineering.
3. Train and compare Linear Regression, Random Forest, and XGBoost models.
4. Evaluate models using proper temporal validation strategies.

## Dataset
**Beijing PM2.5 Air Quality** — hourly PM2.5 concentration (2010–2014) with weather features (temperature, pressure, dew point, wind speed/direction, rain, snow).

### Local Setup
1. Download from Kaggle: [Beijing PM2.5 Data](https://www.kaggle.com/datasets/djhaveri/beijing-pm2-5-data-data-set)
2. Place the CSV inside `data/` as `data/PRSA_data_2010.1.1-2014.12.31.csv`.
3. Run the preparation script:
   ```bash
   python generate_dataset.py
   ```
   This produces `data/beijing_air_quality.csv`.

### Kaggle Setup
1. Click **"Add Data"** and search for `djhaveri/beijing-pm2-5-data-data-set`.
2. Load the data directly or run the preparation script.

---

## Lab Tasks

### 1. Exploratory Data Analysis
- Load the cleaned dataset and plot the PM2.5 time series.
- Show average PM2.5 by hour of day and by month. Comment on daily and seasonal patterns.

### 2. ARCH/GARCH Volatility Analysis
- Fit a simple ARIMA model on a subset of PM2.5 data (e.g., one year).
- Inspect the residuals for volatility clustering (plot squared residuals).
- Fit a GARCH(1,1) model on the ARIMA residuals using the `arch` library.
- Plot the estimated conditional variance. Interpret what it means for air-quality forecasting.

### 3. Supervised Learning Transformation
- Create **lag features**: PM2.5 values at lags 1, 2, 3, 6, 12, 24 hours.
- Create **rolling-window statistics**: rolling mean and rolling standard deviation over 6-hour and 24-hour windows.
- Create **calendar features**: hour of day, day of week, month, is_weekend.
- Drop rows with NaN created by lagging/rolling. Define the target column.

### 4. Train ML Models
- Split data chronologically: use the last year (2014) as the test set.
- Train three models:
  1. **Linear Regression** (baseline).
  2. **Random Forest**.
  3. **XGBoost (Gradient Boosting)**.
- For each model, compute MAE and RMSE on the test set.
- Plot feature importance for Random Forest and XGBoost.

### 5. Temporal Validation
- Implement **TimeSeriesSplit** (e.g., 5 folds) on the training data.
- Run cross-validation for each model and report mean MAE across folds.
- Plot fold-by-fold scores. Discuss whether performance is stable across time.

### 6. Final Comparison
- Build a summary table comparing all models (ARIMA baseline, Linear Regression, Random Forest, XGBoost) on MAE and RMSE.
- Plot actual vs. predicted PM2.5 on a representative test window (e.g., one week).

### 7. Interpretation
- Which model performed best and why?
- Connect results to practical air-quality monitoring: how would accurate PM2.5 forecasts support public health alerts, traffic management, or industrial regulation?

---

## Deliverables
- A complete, well-commented Jupyter Notebook following the steps above.
- Clear markdown cells explaining each transformation and model choice.
- A comparison table and forecast plots.
- A concise interpretation connecting model output to practical decision-making.

## Submission Note
- If you present this lab in slides, add your source code link on the final slide (GitHub repository URL or any accessible versioned code link).
