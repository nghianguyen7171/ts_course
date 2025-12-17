# Topic 15 – Healthcare Call Data Analysis During Emergency Times (Kaggle)

**Level:** Easy  
**Goal:** Analyze and forecast healthcare call center data during emergency periods using time series analysis. Suitable for both traditional ARIMA/SARIMA methods and ML/DL approaches.

## Dataset

- **Source:** Healthcare Call Data Analysis During Emergency Times – Kaggle
- **Link:** https://www.kaggle.com/datasets/shuvokumarbasak2030/healthcare-call-data-analysis-duringemergencytimes/data

## Download Instructions

1. Open the dataset link above.
2. Log in to Kaggle.
3. Click "Download".
4. Extract to `data/healthcare_calls/`.
5. Use the file `daily_and_month_call_report.csv`.

## Data Loading

```python
import pandas as pd

df = pd.read_csv("data/healthcare_calls/daily_and_month_call_report.csv")

# Create datetime index from Year and Month columns
df['Date'] = pd.to_datetime(df['Year'].astype(str) + '-' + df['Month'] + '-01')
df = df.set_index('Date').sort_index()

# Select a time series to analyze (e.g., Total Number of Calls)
ts = df['Total Number of Calls']
```

## Implementation Steps

### 1. Data Exploration
- Load the dataset and inspect structure
- Understand the multiple time series available (calls, consultations, health info, ambulance info, complaints, service inquiries)
- Select one or more time series for analysis (e.g., Total Number of Calls)
- Visualize the time series over time
- Check for missing values and handle them appropriately
- Examine basic statistics (mean, std, min, max)
- Identify patterns, especially during emergency periods (e.g., 2021-2022)

### 2. Exploratory Data Analysis (EDA)
- Plot time series with trend lines
- Identify emergency periods and their impact on call volumes
- Perform time series decomposition (trend, seasonality, residual)
- Calculate and visualize ACF/PACF plots
- Identify monthly and yearly seasonality patterns
- Analyze outliers or unusual patterns (especially during emergency times)
- Compare call volumes across different emergency periods

### 3. Stationarity Analysis
- Test for stationarity using ADF test
- Apply differencing if needed (1st or 2nd order)
- Consider seasonal differencing if strong monthly/yearly patterns exist
- Apply log transformation if variance is non-constant
- Consider segmenting data by emergency vs normal periods

### 4. Model Building

#### Traditional Methods:
- **ARIMA Models:**
  - Use ACF/PACF to identify initial (p, d, q) parameters
  - Try multiple ARIMA configurations
  - Use AIC/BIC for model selection
- **SARIMA Models:**
  - Identify seasonal patterns (monthly: 12 months, yearly patterns)
  - Fit SARIMA models with seasonal components (e.g., SARIMA(p, d, q)(P, D, Q)12)
  - Compare different seasonal configurations
  - Consider models that account for emergency period effects

#### Machine Learning Methods:
- **Feature Engineering:**
  - Create lag features (previous month, year)
  - Add time-based features (month, year, quarter, is_emergency_period)
  - Rolling statistics (3-month, 12-month averages)
  - Create dummy variables for emergency periods
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
- Evaluate model performance during emergency vs normal periods

### 6. Forecasting
- Generate future forecasts (e.g., next 6-12 months)
- Include prediction intervals/confidence bands
- Visualize forecasts with historical data
- Interpret results in healthcare emergency context
- Consider scenario analysis for future emergency periods

## Expected Deliverables

1. **EDA Report:**
   - Time series plots showing patterns and emergency period impacts
   - Decomposition plots (trend, seasonal, residual)
   - ACF/PACF plots
   - Stationarity test results
   - Monthly/yearly pattern analysis
   - Comparison of emergency vs normal periods

2. **Model Results:**
   - Best traditional model (ARIMA/SARIMA) with parameters
   - Best ML model with feature importance
   - Best DL model (if implemented) with architecture
   - Performance comparison table
   - Forecast plots with confidence intervals
   - Analysis of model performance during different periods

3. **Code:**
   - Complete Python notebook
   - Functions for data preprocessing, feature engineering, modeling
   - Visualization utilities
   - Model comparison scripts

## Tips

- The dataset contains monthly data, not daily - adjust your analysis accordingly
- Pay special attention to emergency periods (e.g., 2021-2022) which show significant spikes
- Consider creating separate models for emergency vs normal periods
- Monthly seasonality (12-month patterns) is likely important
- Feature engineering should include emergency period indicators
- Use appropriate train/validation/test splits (temporal, not random)
- Start with simple models (ARIMA) before moving to complex ML/DL
- Compare multiple approaches and justify your choice
- Document any data preprocessing steps clearly
- Consider the healthcare emergency context when interpreting results
