# Topic 2 – Monthly Business Sales Time Series

**Level:** Easy  
**Goal:** Analyze and forecast monthly / periodic sales or revenue.

## Dataset

- **Source:** Business Sales Time Series Starter – OpenDataBay
- **Link:** https://www.opendatabay.com/data/ai-ml/f86d74d9-4656-4313-94d7-0cbd12bb7ffd

## Download Instructions

1. Open the link above.
2. Click "Download CSV" (e.g. `Month_Value_1.csv`).
3. Save as `data/business_sales.csv`.

## Data Loading

```python
import pandas as pd

df = pd.read_csv("data/business_sales.csv")
df["Month"] = pd.to_datetime(df["Month"])
df = df.set_index("Month").sort_index()
```

## Implementation Steps

### 1. Data Exploration
- Load and inspect the dataset structure
- Identify the target variable (sales/revenue column)
- Check data range and frequency (monthly)
- Examine basic statistics and data quality

### 2. Exploratory Data Analysis (EDA)
- Plot monthly sales over time
- Identify trends (increasing, decreasing, stable)
- Detect seasonality patterns (monthly, quarterly, yearly)
- Perform time series decomposition (additive or multiplicative)
- Calculate ACF/PACF to understand autocorrelation

### 3. Stationarity Analysis
- Visual inspection (rolling mean and variance)
- Perform Augmented Dickey-Fuller (ADF) test
- Apply differencing if non-stationary
- Consider seasonal differencing if strong seasonality exists

### 4. Model Building
- **Classical Methods:**
  - ARIMA models (identify p, d, q from ACF/PACF)
  - SARIMA models (for seasonal patterns)
  - Exponential Smoothing (Holt-Winters)
- **Model Selection:**
  - Use AIC/BIC for comparison
  - Cross-validation on validation set

### 5. Model Evaluation
- Split data: training (70%), validation (15%), test (15%)
- Generate forecasts and compare with actual values
- Calculate error metrics: MAE, RMSE, MAPE
- Visualize forecasts vs actuals
- Check residual diagnostics

### 6. Forecasting
- Generate future monthly forecasts
- Include prediction intervals
- Visualize with historical data

## Expected Deliverables

1. **EDA Report:**
   - Time series plots with trend/seasonality
   - Decomposition plots
   - ACF/PACF analysis
   - Stationarity test results

2. **Model Results:**
   - Selected model with parameters
   - Model diagnostics (residual plots, ACF of residuals)
   - Performance metrics table
   - Forecast plots

3. **Code:**
   - Complete Python notebook with all steps
   - Reusable functions for preprocessing and modeling

## Tips

- Monthly data often shows strong seasonality (yearly patterns)
- Consider multiplicative models if variance increases with level
- Use SARIMA for seasonal patterns (e.g., SARIMA(1,1,1)(1,1,1)12)
- Compare multiple models (ARIMA, SARIMA, Exponential Smoothing)
- Business sales may have external factors (holidays, promotions) - note these in analysis

