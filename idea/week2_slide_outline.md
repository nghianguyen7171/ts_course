# Week 2 Slide Outline: Python & Time Series Fundamentals

## Overview
**Week:** 2  
**Format:** Lecture  
**Duration:** ~2 hours  
**CLOs:** 1.2, 2.1, 6.1  
**Assessment:** Homework 1 (data loading, basic indicators, plotting)

---

## Slide Structure

### Part 1: Introduction (5 minutes)

#### Slide 1: Title Slide
- **Title:** Python & Time Series Fundamentals
- **Instructor:** Trong-Nghia Nguyen
- **Faculty:** Faculty of DS & AI
- **Semester:** Spring 2026
- **Course:** Time-series

#### Slide 2: Content
- **Outline:**
  - NumPy Review for Time Series
  - NumPy Operations for Time Series
    - General representation of time series data
    - Time-series decomposition
    - Forecasting formulation
    - Multivariate time series

---

### Part 2: NumPy Review for Time Series (20-25 minutes)

#### Slide 3: NumPy Review for Time Series - Exercises
- **Exercise 1:** Create a NumPy array with 50 evenly spaced values from 0 to 10 (inclusive). What is the shape and dtype?
- **Exercise 2:** Given the array `arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])`:
  - Extract the first 5 elements
  - Extract elements from index 3 to 7 (inclusive)
  - Extract every other element starting from index 0
- **Exercise 3:** Create two arrays: `a = np.array([1, 2, 3])` and `b = np.array([10, 20, 30])`.
  - Add them element-wise
  - Multiply them element-wise
  - What happens if you try `a + 5`? (Broadcasting)
- **Exercise 4:** Create a time series array with 100 daily values starting from January 1, 2020. Use `np.arange()` to create day numbers (0 to 99), then create values as `100 + 2*day + np.random.normal(0, 5, 100)`. What is the mean and standard deviation?

#### Slide 3a: NumPy Arrays Basics (Concept Slide)
- **Content:**
  - Creating arrays: `np.array()`, `np.arange()`, `np.linspace()`
  - Array attributes: shape, dtype, size
  - Indexing and slicing
  - Broadcasting
- **Code Example:**
```python
import numpy as np
# Create time-based array
time_points = np.arange(0, 100, 0.1)  # 0 to 100, step 0.1
values = np.sin(time_points) + np.random.normal(0, 0.1, len(time_points))
```

#### Slide 3b: Answer Key - NumPy Arrays Basics
- **Answer 1:**
```python
arr = np.linspace(0, 10, 50)
print(arr.shape)  # (50,)
print(arr.dtype)  # float64
```
- **Answer 2:**
```python
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
first_five = arr[:5]  # [10, 20, 30, 40, 50]
middle = arr[3:8]  # [40, 50, 60, 70, 80]
every_other = arr[::2]  # [10, 30, 50, 70, 90]
```
- **Answer 3:**
```python
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
sum_result = a + b  # [11, 22, 33]
multiply_result = a * b  # [10, 40, 90]
broadcast_result = a + 5  # [6, 7, 8] - broadcasting adds 5 to each element
```
- **Answer 4:**
```python
days = np.arange(100)
values = 100 + 2*days + np.random.normal(0, 5, 100)
print(f"Mean: {values.mean():.2f}")
print(f"Std: {values.std():.2f}")
# Mean should be around 199 (100 + 2*49.5)
# Std should be around 5
```

---

### Part 3: NumPy Operations for Time Series - Mathematical Foundations (15-20 minutes)

#### Slide 4: NumPy Operations for Time Series
**General representation of time series data:**

$$
\{x_t\}_{t=1}^T = \{x_1, x_2, \ldots, x_T\}
$$

**Where:**
- $x_t$ is the value at time $t$
- $T$ is the total number of observations
- Time index $t$ can be discrete (daily, monthly) or continuous

**Explanation:**
- A time series is an ordered sequence of observations
- Each observation $x_t$ is recorded at a specific time point $t$
- The entire series spans from $t=1$ to $t=T$

---

#### Slide 5: NumPy Operations for Time Series
**Time-series decomposition:**

$$
x_t = T_t + S_t + R_t
$$

**Where:**
- $T_t$ = Trend component (long-term direction)
- $S_t$ = Seasonal component (repeating patterns)
- $R_t$ = Residual/Random component (irregular fluctuations)

**Alternative: Multiplicative model:**
$$
x_t = T_t \times S_t \times R_t
$$

**Explanation:**
- **Additive model:** Components are added together (suitable when seasonal variation is constant)
- **Multiplicative model:** Components are multiplied (suitable when seasonal variation increases with trend)
- Decomposition helps identify underlying patterns and separate signal from noise

---

#### Slide 6: NumPy Operations for Time Series
**Forecasting formulation:**

$$
\hat{x}_{t+h} = f(x_t, x_{t-1}, \ldots, x_{t-p})
$$

**Where:**
- $\hat{x}_{t+h}$ is the forecast for $h$ steps ahead
- $f(\cdot)$ is the forecasting function/model
- $p$ is the number of past observations used (lag order)
- Goal: Predict future values based on historical patterns

**Explanation:**
- Forecasting uses historical data to predict future values
- The function $f$ can be:
  - Linear models (ARIMA, AR, MA)
  - Machine learning models (Random Forest, XGBoost)
  - Deep learning models (LSTM, GRU, CNN)
- The forecast horizon $h$ determines how far ahead we predict

---

#### Slide 7: NumPy Operations for Time Series
**Multivariate time series:**

$$
\mathbf{X}_t = \begin{bmatrix} x_{1,t} \\ x_{2,t} \\ \vdots \\ x_{m,t} \end{bmatrix}
$$

**Where:**
- $\mathbf{X}_t$ is a vector of $m$ variables at time $t$
- Each $x_{i,t}$ represents a different time series variable
- Used for modeling relationships between multiple series

**Explanation:**
- Multiple time series observed simultaneously
- Variables may be correlated or have causal relationships
- Examples:
  - Stock prices of multiple companies
  - Economic indicators (GDP, inflation, unemployment)
  - Vital signs (heart rate, blood pressure, temperature)
- Models: VAR (Vector Autoregression), multivariate ARIMA

---

#### Slide 8: NumPy Operations for Time Series - Practical Applications
- **Mathematical Model (Simple Moving Average over a window of size $k$):**
  $$
    \bar{x}_t = \frac{1}{k} \sum_{i=0}^{k-1} x_{t-i}
  $$
  This averages the most recent $k$ points $x_{t}, x_{t-1}, \dots, x_{t-k+1}$ to smooth short-term fluctuations.

- **Scrolling (Sliding) Window Idea:**
  - Choose a window size $k$ (e.g., $k = 10$)
  - Slide the window one step at a time along the series
  - At each position $t$, compute $\bar{x}_t$ using the formula above
  - This produces a new, shorter series of smoothed values

- **Content:**
  - Element-wise operations
  - Aggregations: `mean()`, `std()`, `min()`, `max()`, `sum()`
  - Statistical functions: `np.corrcoef()`, `np.percentile()`
  - Array concatenation and stacking

- **Code Example:**
```python
# Rolling window calculation (manual)
window_size = 10
rolling_mean = np.convolve(values, np.ones(window_size)/window_size, mode='valid')
```

- **Visualization of the Rolling Window Process:**

**Step 1: Create the kernel (averaging window)**
```
np.ones(window_size) = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # 10 ones
np.ones(window_size) / window_size = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
# This creates a uniform weight kernel where each element = 1/10 = 0.1
```

**Step 2: Example with sample data**
```
values = [100, 102, 98, 105, 103, 107, 110, 108, 112, 115, 118, 120, 122, 125, 128]
#         v0   v1   v2   v3   v4   v5   v6   v7   v8   v9   v10  v11  v12  v13  v14

kernel = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
```

**Step 3: Convolution process (sliding window)**
```
Position 0: Multiply and sum
  values:  [100, 102, 98, 105, 103, 107, 110, 108, 112, 115, ...]
  kernel:  [0.1, 0.1,  0.1, 0.1,  0.1, 0.1,  0.1, 0.1,  0.1, 0.1]
  ─────────────────────────────────────────────────────────────
  result:  100×0.1 + 102×0.1 + 98×0.1 + ... + 115×0.1 = 105.8
           = (100+102+98+105+103+107+110+108+112+115) / 10

Position 1: Shift window by 1
  values:  [100, 102, 98, 105, 103, 107, 110, 108, 112, 115, 118, ...]
  kernel:       [0.1, 0.1,  0.1, 0.1,  0.1, 0.1,  0.1, 0.1,  0.1, 0.1]
  ─────────────────────────────────────────────────────────────
  result:  102×0.1 + 98×0.1 + 105×0.1 + ... + 118×0.1 = 106.8
           = (102+98+105+103+107+110+108+112+115+118) / 10

Position 2: Continue shifting...
  values:  [100, 102, 98, 105, 103, 107, 110, 108, 112, 115, 118, 120, ...]
  kernel:            [0.1, 0.1,  0.1, 0.1,  0.1, 0.1,  0.1, 0.1,  0.1, 0.1]
  ─────────────────────────────────────────────────────────────
  result:  (98+105+103+107+110+108+112+115+118+120) / 10 = 107.6
```

**Step 4: Result with `mode='valid'`**
```
Original length: 15 values
Window size: 10
Output length: 15 - 10 + 1 = 6 values

rolling_mean = [105.8, 106.8, 107.6, 109.2, 111.0, 112.8]
              ↑      ↑      ↑      ↑      ↑      ↑
            pos 0  pos 1  pos 2  pos 3  pos 4  pos 5
```

**Key Points:**
- **`np.convolve()`**: Performs convolution (sliding multiplication and sum)
- **`mode='valid'`**: Only computes where the full window fits (no padding)
- **Result**: Each element is the average of the previous 10 values
- **Length reduction**: Output is shorter by `(window_size - 1)` elements

**Visual Timeline:**
```
Time:     0    1    2    3    4    5    6    7    8    9   10   11   12   13   14
values: [100, 102, 98, 105, 103, 107, 110, 108, 112, 115, 118, 120, 122, 125, 128]
         └─────────────────┘
         Window 0: avg = 105.8
            └─────────────────┘
            Window 1: avg = 106.8
               └─────────────────┘
               Window 2: avg = 107.6
                  └─────────────────┘
                  Window 3: avg = 109.2
                     └─────────────────┘
                     Window 4: avg = 111.0
                        └─────────────────┘
                        Window 5: avg = 112.8
```


---
### Part 4: Pandas for Time Series (30-40 minutes)

#### Slide 11: Introducing the AirPassengers Dataset
- **Dataset Description:**
  - Monthly airline passenger numbers (1949–1960)
  - Univariate time series
  - Clear trend and seasonality
  - Widely used benchmark dataset in time-series analysis
- **Why This Dataset?**
  - Classic example with well-defined patterns
  - Suitable for demonstrating time series concepts
  - Available in statsmodels library

#### Slide 12: Loading AirPassengers into Pandas
- **Steps:**
  - Load dataset from statsmodels
  - Convert to Pandas Series
  - Create DatetimeIndex
  - Inspect data (head, tail, info)
- **Code Example:**
```python
from statsmodels.datasets import get_rdataset
import pandas as pd

# Load AirPassengers dataset
data = get_rdataset('AirPassengers', 'datasets')
df = data.data

# Convert to Pandas Series with datetime index
ts = pd.Series(df['value'].values, 
               index=pd.date_range('1949-01', periods=len(df), freq='M'))
print(ts.head())
print(ts.info())
```

#### Slide 13: Time Indexing and Slicing
- **Content:**
  - Date-based indexing
  - Subsetting by year or date range
  - Shifting the time series
  - Differencing for trend removal
- **Code Example:**
```python
# Date-based indexing
ts_1950 = ts['1950']  # All data from 1950
ts_1950_1955 = ts['1950':'1955']  # Date range

# Shifting
ts_lag1 = ts.shift(1)  # Shift by 1 period

# Differencing (removes trend)
ts_diff = ts.diff()  # First difference
```

---

### Part 5: Resampling and Rolling Statistics (20-25 minutes)

#### Slide 14: Resampling Concepts
- **Why Resampling is Needed:**
  - Change frequency of observations
  - Aggregate data for analysis
  - Align multiple time series
- **Types:**
  - **Downsampling:** Reduce frequency (e.g., daily → monthly)
  - **Upsampling:** Increase frequency (e.g., monthly → daily)
- **Common Frequencies:**
  - 'D' (daily), 'W' (weekly), 'M' (monthly), 'Q' (quarterly), 'Y' (yearly)
- **Aggregation Functions:**
  - `mean()`, `sum()`, `last()`, `first()`, `max()`, `min()`

#### Slide 15: Resampling AirPassengers
- **Content:**
  - Monthly to yearly aggregation
  - Effect of resampling on trend and variance
  - Visual comparison of different frequencies
- **Code Example:**
```python
# Monthly to yearly aggregation
yearly = ts.resample('Y').mean()  # Yearly mean
yearly_sum = ts.resample('Y').sum()  # Yearly sum

# Visual comparison
import matplotlib.pyplot as plt
fig, axes = plt.subplots(2, 1, figsize=(12, 8))
axes[0].plot(ts.index, ts.values, label='Monthly')
axes[0].set_title('Monthly AirPassengers')
axes[1].plot(yearly.index, yearly.values, label='Yearly Mean')
axes[1].set_title('Yearly Aggregated AirPassengers')
plt.tight_layout()
plt.show()
```

#### Slide 16: Rolling Statistics with Pandas
- **Content:**
  - Rolling mean
  - Rolling standard deviation
  - Effect of window size (3, 6, 12)
  - Connection to NumPy sliding window
- **Code Example:**
```python
# Rolling statistics
ts_rolling_mean_12 = ts.rolling(window=12).mean()  # 12-month rolling mean
ts_rolling_std_12 = ts.rolling(window=12).std()  # 12-month rolling std

# Different window sizes
ts_rolling_3 = ts.rolling(window=3).mean()
ts_rolling_6 = ts.rolling(window=6).mean()
ts_rolling_12 = ts.rolling(window=12).mean()

# Visualization
plt.figure(figsize=(12, 6))
plt.plot(ts.index, ts.values, label='Original', alpha=0.5)
plt.plot(ts_rolling_3.index, ts_rolling_3.values, label='3-month MA')
plt.plot(ts_rolling_6.index, ts_rolling_6.values, label='6-month MA')
plt.plot(ts_rolling_12.index, ts_rolling_12.values, label='12-month MA')
plt.legend()
plt.title('Rolling Mean with Different Window Sizes')
plt.show()
```

---

### Part 6: Technical Indicators and EDA (25-30 minutes)

#### Slide 17: From SMA to EMA
- **Simple Moving Average (SMA):**
  - Equal weights for all observations in window
  - Formula: SMA(n) = (P₁ + P₂ + ... + Pₙ) / n
- **Exponential Moving Average (EMA):**
  - More weight to recent observations
  - Formula: EMA(t) = α × Price(t) + (1-α) × EMA(t-1)
  - Where α = 2 / (n + 1)
- **Comparison:**
  - EMA is more responsive to recent changes
  - SMA is smoother but less reactive
- **Use Cases Beyond Finance:**
  - Smoothing any time series data
  - Trend detection in various domains
- **Code Example:**
```python
# SMA
sma_12 = ts.rolling(window=12).mean()

# EMA
ema_12 = ts.ewm(span=12, adjust=False).mean()

# Comparison plot
plt.figure(figsize=(12, 6))
plt.plot(ts.index, ts.values, label='Original', alpha=0.3)
plt.plot(sma_12.index, sma_12.values, label='SMA(12)')
plt.plot(ema_12.index, ema_12.values, label='EMA(12)')
plt.legend()
plt.title('SMA vs EMA Comparison')
plt.show()
```

#### Slide 18: MACD Indicator
- **Components:**
  - Fast EMA (typically 12 periods)
  - Slow EMA (typically 26 periods)
  - MACD line = Fast EMA - Slow EMA
  - Signal line = EMA(9) of MACD line
- **Interpretation:**
  - Momentum indicator
  - MACD > Signal: Bullish momentum
  - MACD < Signal: Bearish momentum
- **Demonstration on AirPassengers:**
```python
# Calculate MACD
ema_fast = ts.ewm(span=12, adjust=False).mean()
ema_slow = ts.ewm(span=26, adjust=False).mean()
macd_line = ema_fast - ema_slow
signal_line = macd_line.ewm(span=9, adjust=False).mean()
histogram = macd_line - signal_line

# Visualization
fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
axes[0].plot(ts.index, ts.values, label='AirPassengers')
axes[0].set_title('AirPassengers with EMAs')
axes[0].legend()

axes[1].plot(macd_line.index, macd_line.values, label='MACD')
axes[1].plot(signal_line.index, signal_line.values, label='Signal')
axes[1].bar(histogram.index, histogram.values, alpha=0.3, label='Histogram')
axes[1].axhline(y=0, color='black', linestyle='--')
axes[1].set_title('MACD Indicator')
axes[1].legend()
plt.tight_layout()
plt.show()
```

#### Slide 19: RSI Indicator (Conceptual)
- **Relative Strength Index (RSI):**
  - Momentum oscillator measuring speed and magnitude of changes
  - Formula: RSI = 100 - (100 / (1 + RS))
  - Where RS = Average Gain / Average Loss (over n periods)
- **Calculation:**
  - Gains and losses over a window (typically 14 periods)
  - Separates positive and negative price changes
- **Interpretation:**
  - RSI > 70: Overbought (potential reversal)
  - RSI < 30: Oversold (potential reversal)
  - RSI = 50: Neutral
- **Non-Financial Illustration Purpose:**
  - Demonstrates momentum concepts applicable to any time series
  - Useful for identifying extreme values in any domain
- **Code Example:**
```python
def calculate_rsi(data, window=14):
    delta = data.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

rsi = calculate_rsi(ts, window=14)

# Visualization
plt.figure(figsize=(12, 6))
plt.plot(rsi.index, rsi.values, label='RSI')
plt.axhline(y=70, color='r', linestyle='--', label='Overbought (70)')
plt.axhline(y=30, color='g', linestyle='--', label='Oversold (30)')
plt.fill_between(rsi.index, 70, 100, alpha=0.2, color='red')
plt.fill_between(rsi.index, 0, 30, alpha=0.2, color='green')
plt.ylim(0, 100)
plt.title('RSI Indicator')
plt.legend()
plt.show()
```

#### Slide 20: Exploratory Data Analysis for Time Series
- **Content:**
  - Line plot of the series
  - Seasonal patterns identification
  - Rolling mean and variance analysis
  - Trend–seasonality decomposition
- **Code Example:**
```python
from statsmodels.tsa.seasonal import seasonal_decompose

# Line plot
plt.figure(figsize=(12, 6))
plt.plot(ts.index, ts.values)
plt.title('AirPassengers Time Series')
plt.xlabel('Date')
plt.ylabel('Number of Passengers')
plt.grid(True)
plt.show()

# Rolling statistics
rolling_mean = ts.rolling(window=12).mean()
rolling_std = ts.rolling(window=12).std()

# Decomposition
decomposition = seasonal_decompose(ts, model='additive')
fig = decomposition.plot()
fig.set_size_inches(12, 8)
plt.tight_layout()
plt.show()
```

#### Slide 21: Summary and Transition
- **Key Takeaways:**
  - From NumPy arrays to Pandas time series
  - From raw data to smoothed representations
  - Role of indicators in understanding dynamics
- **Preparation for:**
  - Stationarity analysis (Week 6)
  - ARIMA models (Week 7-9)
  - Machine learning and deep learning approaches (Week 11-14)
- **Next Steps:**
  - Practice with your project dataset
  - Apply these techniques to your chosen topic
  - Prepare for Week 3 lab presentations


## Notes for Instructor

### Timing Guidelines
- **Part 1 (Introduction):** 5 min
- **Part 2 (NumPy Review):** 20-25 min
- **Part 3 (Mathematical Foundations):** 15-20 min
- **Part 4 (Pandas for Time Series):** 30-40 min
- **Part 5 (Resampling and Rolling Statistics):** 20-25 min
- **Part 6 (Technical Indicators and EDA):** 25-30 min
- **Total:** ~2 hours

### Interactive Elements
- Live coding demonstrations for exercises
- Student participation: "Try Exercise 1 on your own"
- Quick polls: "Who has used NumPy before?"
- Discussion: "Why do we need these mathematical formulations?"

### Visual Aids
- Code examples with syntax highlighting
- Mathematical formulas clearly displayed
- Step-by-step visualization of rolling window process
- Before/after examples showing transformations

### Assessment Alignment
- Exercises prepare students for NumPy operations in time series
- Mathematical foundations support understanding of later topics
- Foundation for Week 2 continuation (Pandas, Financial Indicators)

---

## Revision History
- **Created:** [Date]
- **Last Updated:** [Date]
- **Version:** 2.0 (Aligned with PDF structure)
