# Topic 7 – Human Vital Signs (Kaggle)

**Level:** Medium  
**Goal:** Analyze and forecast physiological signals (HR, BP, SpO2, etc.).

## Dataset

- **Source:** Human Vital Sign Dataset – Kaggle
- **Link:** https://www.kaggle.com/datasets/nasirayub2/human-vital-sign-dataset

## Download Instructions

1. Open the dataset link above.
2. Click "Download".
3. Extract to `data/vital_signs/`.
4. Use the main CSV, e.g. `HumanVitalSigns.csv`.

## Data Loading

```python
import pandas as pd

df = pd.read_csv("data/vital_signs/HumanVitalSigns.csv")  # adjust
df["Time"] = pd.to_datetime(df["Time"])  # adapt time column name
df = df.set_index("Time").sort_index()
```

## Implementation Steps

### 1. Data Exploration
- Load vital signs dataset
- Identify available signals (Heart Rate, Blood Pressure, SpO2, etc.)
- Inspect data frequency and time range
- Check for missing values and data quality
- Understand measurement units and normal ranges

### 2. Exploratory Data Analysis (EDA)
- Plot each vital sign over time
- Identify patterns (resting vs active periods, circadian rhythms)
- Calculate basic statistics (mean, std, min, max)
- Analyze relationships between different vital signs
- Perform time series decomposition

### 3. Signal Preprocessing
- Handle missing values (interpolation, forward fill)
- Detect and handle outliers (physiological limits)
- Smooth noisy signals if needed (moving average, median filter)
- Resample to consistent frequency if needed

### 4. Stationarity Analysis
- Test each signal for stationarity
- Vital signs may have trends (e.g., HR during exercise)
- Apply differencing or detrending if needed
- Consider segmenting by activity state

### 5. Model Building
- **Univariate Models:**
  - ARIMA/SARIMA for each vital sign
  - Consider seasonality (circadian rhythms)
- **Multivariate Models (optional):**
  - VAR models to capture relationships between vital signs
  - Analyze how one sign affects another

### 6. Model Evaluation
- Split data temporally
- Generate forecasts for each vital sign
- Calculate accuracy metrics
- Visualize forecasts with actual values
- Analyze forecast errors

### 7. Clinical Interpretation
- Interpret results in clinical context
- Identify normal vs abnormal patterns
- Discuss implications for monitoring
- Compare with clinical knowledge

## Expected Deliverables

1. **EDA Report:**
   - Time series plots for each vital sign
   - Statistical summaries
   - Relationship analysis between signs
   - Decomposition plots

2. **Model Results:**
   - Model parameters for each signal
   - Forecast accuracy metrics
   - Forecast plots
   - Clinical interpretation

3. **Code:**
   - Complete Python notebook
   - Preprocessing functions
   - Visualization utilities

## Tips

- Vital signs have physiological limits - use domain knowledge for validation
- Consider activity states (rest, exercise, sleep) in analysis
- Circadian rhythms may create daily seasonality
- Handle outliers carefully - they may be real events (e.g., spikes during activity)
- Use appropriate sampling frequency (too high may be noisy, too low loses information)
- Multivariate models can capture physiological relationships (e.g., HR and BP)
- Consider patient-specific models vs population models
- Document any preprocessing decisions and their rationale

