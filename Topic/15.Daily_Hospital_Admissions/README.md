# Topic 15 – Daily Hospital Admissions Time Series (Kaggle)

**Level:** Easy  
**Goal:** Forecast daily hospital admissions using univariate time series analysis. Suitable for both traditional ARIMA/SARIMA methods and ML/DL approaches.

## Dataset

- **Source:** Daily hospital admissions time series dataset from Kaggle
- **Link:** Search Kaggle for a suitable dataset (e.g., search for "hospital admissions", "emergency department visits", or "daily patient admissions"). Choose a dataset that provides a date column and an admissions/count column.

## Download Instructions

1. Search Kaggle for a suitable daily hospital admissions dataset.
2. Log in to Kaggle.
3. Click "Download" for your chosen dataset.
4. Extract to `data/hospital/`.
5. Use the main CSV file (e.g., `hospital_admissions.csv` or `daily_admissions.csv`).

## Data Loading

```python
import pandas as pd

df = pd.read_csv("data/hospital/hospital_admissions.csv")  # adjust filename
df["Date"] = pd.to_datetime(df["Date"])  # adapt column name if different
df = df.set_index("Date").sort_index()
```

## Implementation Steps

### 1. Data Exploration
- Load the dataset and inspect structure
- Visualize the time series (daily admissions over time)
- Check for missing values and handle them appropriately
- Examine basic statistics (mean, std, min, max)
- Identify any obvious patterns (trends, seasonality)

### 2. Exploratory Data Analysis (EDA)
- Plot time series with trend lines
- Perform time series decomposition (trend, seasonality, residual)
- Calculate and visualize ACF/PACF plots
- Identify weekly patterns (weekday vs weekend effects)
- Check for monthly or yearly seasonality
- Analyze outliers or unusual patterns

### 3. Stationarity Analysis
- Test for stationarity using ADF test
- Apply differencing if needed (1st or 2nd order)
- Consider seasonal differencing if strong weekly patterns exist
- Apply log transformation if variance is non-constant

### 4. Model Building

#### Traditional Methods:
- **ARIMA Models:**
  - Use ACF/PACF to identify initial (p, d, q) parameters
  - Try multiple ARIMA configurations
  - Use AIC/BIC for model selection
- **SARIMA Models:**
  - Identify seasonal patterns (weekly: 7 days, monthly: 30 days)
  - Fit SARIMA models with seasonal components
  - Compare different seasonal configurations

#### Machine Learning Methods:
- **Feature Engineering:**
  - Create lag features (previous day, week)
  - Add time-based features (day of week, month, is_weekend)
  - Rolling statistics (7-day, 30-day averages)
- **Models:**
  - Random Forest or XGBoost for regression
  - Linear regression with features
  - Compare with ARIMA/SARIMA baseline

#### Deep Learning Methods (Optional):
- **LSTM/GRU:**
  - Prepare sequences for RNN models
  - Train LSTM or GRU networks
  - Tune hyperparameters
- **Simple CNN:**
  - Use 1D convolutions for time series
  - Compare with RNN approaches

### 5. Model Evaluation
- Split data temporally (e.g., last 20-30% as test set)
- Use walk-forward validation for time series
- Calculate metrics: MAE, RMSE, MAPE
- Compare traditional vs ML/DL approaches
- Visualize actual vs predicted values
- Analyze forecast errors and residuals

### 6. Forecasting
- Generate future forecasts (e.g., next 30 days)
- Include prediction intervals/confidence bands
- Visualize forecasts with historical data
- Interpret results in healthcare context

## Expected Deliverables

1. **EDA Report:**
   - Time series plots showing patterns
   - Decomposition plots (trend, seasonal, residual)
   - ACF/PACF plots
   - Stationarity test results
   - Weekly/monthly pattern analysis

2. **Model Results:**
   - Best traditional model (ARIMA/SARIMA) with parameters
   - Best ML model with feature importance
   - Best DL model (if implemented) with architecture
   - Performance comparison table
   - Forecast plots with confidence intervals

3. **Code:**
   - Complete Python notebook
   - Functions for data preprocessing, feature engineering, modeling
   - Visualization utilities
   - Model comparison scripts

## Tips

- Hospital admissions often show weekly patterns (lower on weekends)
- Consider external factors (holidays, events) that might affect admissions
- Use appropriate train/validation/test splits (temporal, not random)
- Start with simple models (ARIMA) before moving to complex ML/DL
- Feature engineering is crucial for ML models - create meaningful time-based features
- Compare multiple approaches and justify your choice
- Document any data preprocessing steps clearly
- Consider the healthcare context when interpreting results

