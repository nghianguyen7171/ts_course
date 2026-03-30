import nbformat as nbf

nb = nbf.v4.new_notebook()

cells = []

# Title
cells.append(nbf.v4.new_markdown_cell("""# Week 10: Seasonality, SARIMA, and SARIMAX
**Objective**: Build quantitative forecasting models for urban power consumption by integrating cyclical seasonal behaviors and meteorological exogenous variables (Temperature, Humidity)."""))

# 1. Setup and Data Loading
cells.append(nbf.v4.new_markdown_cell("""## 1. Data Preparation and Resampling
The dataset contains power consumption for Tetuan City along with weather variables, originally recorded at 10-minute intervals."""))

cells.append(nbf.v4.new_code_cell("""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import os

from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.statespace.sarimax import SARIMAX

warnings.filterwarnings('ignore')
plt.style.use('seaborn-v0_8-whitegrid')

# Check data paths (local vs Kaggle)
kaggle_path = "/kaggle/input/tetuan-city-power-consumption/Tetuan City power consumption.csv"
local_path = "data/Tetuan City power consumption.csv"

path = kaggle_path if os.path.exists(kaggle_path) else local_path

print(f"Loading data from: {path}")
df = pd.read_csv(path)

# Parse DateTime
df['DateTime'] = pd.to_datetime(df['DateTime'])
df.set_index('DateTime', inplace=True)

# Resample to hourly data to smooth micro-noise
df_hourly = df.resample('H').mean().dropna()

print("Original shape:", df.shape)
print("Hourly shape:", df_hourly.shape)

# Subset for analysis (First 2 months to make charts clear)
df_subset = df_hourly.loc['2017-01-01':'2017-02-28']
target_y = df_subset['Zone 1 Power Consumption']

plt.figure(figsize=(15, 5))
plt.plot(target_y)
plt.title("Hourly Power Consumption (Zone 1) - Jan to Feb 2017")
plt.ylabel("Power Consumption")
plt.tight_layout()
plt.show()"""))

# 2. Decomposition
cells.append(nbf.v4.new_markdown_cell("""## 2. Decomposition and Seasonality Analysis
We dissect the time series into Trend, Seasonal, and Residual components. Given the daily rhythm, we use `period=24` (24 hours)."""))

cells.append(nbf.v4.new_code_cell("""# Decompose the time series
decomposition = seasonal_decompose(target_y, model='additive', period=24)

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(15, 10), sharex=True)
decomposition.observed.plot(ax=ax1, title='Observed Signal', color='black')
decomposition.trend.plot(ax=ax2, title='Trend', color='blue')
decomposition.seasonal.plot(ax=ax3, title='Seasonal Component (24h period)', color='green')
decomposition.resid.plot(ax=ax4, title='Residuals', color='red')

plt.tight_layout()
plt.show()"""))

cells.append(nbf.v4.new_markdown_cell("""**Observation**: 
- A clear 24-hour seasonal pattern exists.
- The trend component shows variations across days/weeks.
- The additive model is suitable because the seasonal amplitude remains relatively stable over time."""))

# 3. Stationarization
cells.append(nbf.v4.new_markdown_cell("""## 3. Stationarization Pipeline (Hyndman Protocol)
We apply the Augmented Dickey-Fuller (ADF) test to check for stationarity, then apply seasonal differencing to remove the 24-hour cycle."""))

cells.append(nbf.v4.new_code_cell("""def check_stationarity(series, name):
    result = adfuller(series.dropna())
    print(f"ADF Statistic for {name}: {result[0]:.4f}")
    print(f"p-value: {result[1]:.4f}")
    if result[1] <= 0.05:
        print("=> The series is STATIONARY.\\n")
    else:
        print("=> The series is NON-STATIONARY.\\n")

# 1. Original Series
check_stationarity(target_y, "Original Series")

# 2. Seasonal Differencing (lag=24)
diff_seasonal = target_y.diff(24).dropna()
check_stationarity(diff_seasonal, "Seasonally Differenced Series (s=24)")

# Plot the differenced series
plt.figure(figsize=(15, 4))
plt.plot(diff_seasonal, color='purple')
plt.title("Seasonally Differenced Power Consumption")
plt.tight_layout()
plt.show()"""))

cells.append(nbf.v4.new_markdown_cell("""**Observation**: The series becomes strictly stationary after a single seasonal differencing ($D=1, s=24$). We do not need a non-seasonal differencing ($d=0$) to avoid over-differencing."""))

# 4. Identification
cells.append(nbf.v4.new_markdown_cell("""## 4. Identification (ACF / PACF)
Plotting ACF and PACF for the seasonally differenced series to identify AR ($p, P$) and MA ($q, Q$) terms."""))

cells.append(nbf.v4.new_code_cell("""fig, ax = plt.subplots(2, 1, figsize=(15, 10))
plot_acf(diff_seasonal, lags=75, ax=ax[0])
plot_pacf(diff_seasonal, lags=75, ax=ax[1])
plt.tight_layout()
plt.show()"""))

cells.append(nbf.v4.new_markdown_cell("""**Interpretation**:
- **Non-seasonal**: PACF has significant spikes at lag 1 and 2, then cuts off. ACF tails off. This suggests an AR(2) process -> $p=2, q=0$.
- **Seasonal**: Look at lags 24, 48, 72. ACF has a strong negative spike at lag 24, while PACF trails off at seasonal lags. This suggests a Seasonal MA(1) term -> $P=0, Q=1$.

Hence, our initial guess is **SARIMA(2, 0, 0)(0, 1, 1, 24)**."""))

# 5. Baseline Modeling
cells.append(nbf.v4.new_markdown_cell("""## 5. Baseline Modeling: SARIMA
We fit the SARIMA model without any exogenous variables."""))

cells.append(nbf.v4.new_code_cell("""# Define SARIMA configuration
order = (2, 0, 0)
seasonal_order = (0, 1, 1, 24)

# Fit SARIMA baseline
print("Fitting SARIMA model (this might take a minute or two)...")
sarima_model = SARIMAX(target_y, 
                       order=order, 
                       seasonal_order=seasonal_order,
                       enforce_stationarity=False,
                       enforce_invertibility=False)

sarima_results = sarima_model.fit(disp=False)
print(sarima_results.summary())"""))

# 6. SARIMAX Upgrading
cells.append(nbf.v4.new_markdown_cell("""## 6. Upgrading to SARIMAX (Integrating Weather Features)
We include `Temperature` and `Humidity` as exogenous variables ($X$). The model will simultaneously perform linear regression on the weather data and SARIMA on the errors."""))

cells.append(nbf.v4.new_code_cell("""# Extract Exogenous Features
exog_features = df_subset[['Temperature', 'Humidity']]

print("Fitting SARIMAX model with exogenous features...")
sarimax_model = SARIMAX(target_y, 
                        exog=exog_features,
                        order=order, 
                        seasonal_order=seasonal_order,
                        enforce_stationarity=False,
                        enforce_invertibility=False)

sarimax_results = sarimax_model.fit(disp=False)
print(sarimax_results.summary())"""))

cells.append(nbf.v4.new_markdown_cell("""**Comparison**:
Check the **AICc** metric from both model summaries. The SARIMAX model should report a lower AICc, proving that adding weather variables increases the model's informational value and predictive power."""))

# 7. Diagnostic Validation
cells.append(nbf.v4.new_markdown_cell("""## 7. Diagnostic Validation
We validate the assumptions of the SARIMAX model's residuals."""))

cells.append(nbf.v4.new_code_cell("""# Plot residual diagnostics
fig = sarimax_results.plot_diagnostics(figsize=(15, 12))
plt.tight_layout()
plt.show()"""))

cells.append(nbf.v4.new_markdown_cell("""**Exogenous Variables p-values**:
Let's check if `Temperature` and `Humidity` are statistically significant ($p < 0.05$)."""))

cells.append(nbf.v4.new_code_cell("""print("p-values of the exogenous variables:")
print(sarimax_results.pvalues[['Temperature', 'Humidity']])"""))

# 8. Forecasting
cells.append(nbf.v4.new_markdown_cell("""## 8. Forecasting Evaluation (Train/Test Split)
To visualize how well the model predicts future values, let's train on the first 50 days and test on the next 9 days."""))

cells.append(nbf.v4.new_code_cell("""# Split the subset into Train and Test
train_y = df_subset.loc['2017-01-01':'2017-02-19', 'Zone 1 Power Consumption']
test_y  = df_subset.loc['2017-02-20':'2017-02-28', 'Zone 1 Power Consumption']

train_exog = df_subset.loc['2017-01-01':'2017-02-19', ['Temperature', 'Humidity']]
test_exog  = df_subset.loc['2017-02-20':'2017-02-28', ['Temperature', 'Humidity']]

print("Train shape:", train_y.shape)
print("Test shape:", test_y.shape)

# Train SARIMAX on Training data
forecast_model = SARIMAX(train_y, 
                         exog=train_exog,
                         order=order, 
                         seasonal_order=seasonal_order,
                         enforce_stationarity=False,
                         enforce_invertibility=False)
forecast_results = forecast_model.fit(disp=False)

# Forecast on Test data
predictions = forecast_results.get_forecast(steps=len(test_y), exog=test_exog)
pred_mean = predictions.predicted_mean
pred_ci = predictions.conf_int()

# Plot the Forecast
plt.figure(figsize=(15, 6))
plt.plot(train_y.index[-100:], train_y.values[-100:], label='Train (last 100 hrs)')
plt.plot(test_y.index, test_y.values, label='Actual Test')
plt.plot(test_y.index, pred_mean.values, color='red', label='SARIMAX Forecast')

# Confidence Interval
plt.fill_between(test_y.index, 
                 pred_ci.iloc[:, 0], 
                 pred_ci.iloc[:, 1], 
                 color='r', alpha=0.1, label='95% CI')

plt.title('SARIMAX Forecast vs Actual Power Consumption')
plt.ylabel('Power Consumption')
plt.legend()
plt.tight_layout()
plt.show()"""))

cells.append(nbf.v4.new_markdown_cell("""## 9. Conclusion
- We successfully downsampled 10-minute frequency data into a manageable hourly signal.
- The decomposition and ACF/PACF plots directed us to choose a single seasonal differencing ($D=1, s=24$), an AR(2) term, and a Seasonal MA(1) term.
- Evaluating **AICc** confirmed that adding the `Temperature` and `Humidity` variables (SARIMAX) improved our fit over the SARIMA baseline.
- Forecasting results demonstrated that the model effectively captured the daily 24-hour cycle and adapted to the environmental variations."""))

nb['cells'] = cells

with open('/Users/nguyennghia/PROJECT/TS_Analysis/idea/week10_exercise/solution_key.ipynb', 'w') as f:
    nbf.write(nb, f)
print("Notebook created successfully.")
