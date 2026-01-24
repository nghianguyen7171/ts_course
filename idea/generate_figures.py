import numpy as np
import matplotlib.pyplot as plt

# Problem 1.1: Time series x = [2, 4, 6, 8, 10]
x = np.array([2, 4, 6, 8, 10])
time = np.arange(1, len(x) + 1)

plt.figure(figsize=(10, 6))
plt.plot(time, x, marker='o', markersize=10, linewidth=2, color='steelblue', markerfacecolor='crimson', markeredgewidth=2)
plt.title('Time Series: x = [2, 4, 6, 8, 10]', fontsize=14, fontweight='bold')
plt.xlabel('Time Index (t)', fontsize=12)
plt.ylabel('Value (x_t)', fontsize=12)
plt.grid(True, alpha=0.3, linestyle='--')
plt.xticks(time)
plt.yticks(x)
plt.tight_layout()
plt.savefig('idea/figures/problem1_1_timeseries.png', dpi=300, bbox_inches='tight')
plt.close()

print("Figure saved: idea/figures/problem1_1_timeseries.png")

# Problem 1.3: Time series x = [10, 8, 6, 4, 2]
x = np.array([10, 8, 6, 4, 2])
time = np.arange(1, len(x) + 1)

plt.figure(figsize=(10, 6))
plt.plot(time, x, marker='o', markersize=10, linewidth=2, color='steelblue', markerfacecolor='crimson', markeredgewidth=2)
plt.title('Time Series: x = [10, 8, 6, 4, 2]', fontsize=14, fontweight='bold')
plt.xlabel('Time Index (t)', fontsize=12)
plt.ylabel('Value (x_t)', fontsize=12)
plt.grid(True, alpha=0.3, linestyle='--')
plt.xticks(time)
plt.yticks(x)
plt.tight_layout()
plt.savefig('idea/figures/problem1_3_timeseries.png', dpi=300, bbox_inches='tight')
plt.close()

print("Figure saved: idea/figures/problem1_3_timeseries.png")

# Problem 1.4: Time series x = [3, 7, 3, 7, 3]
x = np.array([3, 7, 3, 7, 3])
time = np.arange(1, len(x) + 1)

plt.figure(figsize=(10, 6))
plt.plot(time, x, marker='o', markersize=10, linewidth=2, color='steelblue', markerfacecolor='crimson', markeredgewidth=2)
plt.title('Time Series: x = [3, 7, 3, 7, 3]', fontsize=14, fontweight='bold')
plt.xlabel('Time Index (t)', fontsize=12)
plt.ylabel('Value (x_t)', fontsize=12)
plt.grid(True, alpha=0.3, linestyle='--')
plt.xticks(time)
plt.yticks(x)
plt.tight_layout()
plt.savefig('idea/figures/problem1_4_timeseries.png', dpi=300, bbox_inches='tight')
plt.close()

print("Figure saved: idea/figures/problem1_4_timeseries.png")

# Problem 1.5: Time series x = [12, 15, 18, 12, 15, 18, 12]
x = np.array([12, 15, 18, 12, 15, 18, 12])
time = np.arange(1, len(x) + 1)

plt.figure(figsize=(10, 6))
plt.plot(time, x, marker='o', markersize=10, linewidth=2, color='steelblue', markerfacecolor='crimson', markeredgewidth=2)
plt.title('Time Series: x = [12, 15, 18, 12, 15, 18, 12]', fontsize=14, fontweight='bold')
plt.xlabel('Time Index (t)', fontsize=12)
plt.ylabel('Value (x_t)', fontsize=12)
plt.grid(True, alpha=0.3, linestyle='--')
plt.xticks(time)
plt.yticks(x)
plt.tight_layout()
plt.savefig('idea/figures/problem1_5_timeseries.png', dpi=300, bbox_inches='tight')
plt.close()

print("Figure saved: idea/figures/problem1_5_timeseries.png")

# Problem 2.1: Time series x = [5, 7, 9, 11, 13]
x = np.array([5, 7, 9, 11, 13])
time = np.arange(1, len(x) + 1)

plt.figure(figsize=(10, 6))
plt.plot(time, x, marker='o', markersize=10, linewidth=2, color='steelblue', markerfacecolor='crimson', markeredgewidth=2)
plt.title('Time Series: x = [5, 7, 9, 11, 13]', fontsize=14, fontweight='bold')
plt.xlabel('Time Index (t)', fontsize=12)
plt.ylabel('Value (x_t)', fontsize=12)
plt.grid(True, alpha=0.3, linestyle='--')
plt.xticks(time)
plt.yticks(x)
plt.tight_layout()
plt.savefig('idea/figures/problem2_1_timeseries.png', dpi=300, bbox_inches='tight')
plt.close()

print("Figure saved: idea/figures/problem2_1_timeseries.png")

# Problem 2.3: Time series x = [20, 20, 20, 25, 25, 25]
x = np.array([20, 20, 20, 25, 25, 25])
time = np.arange(1, len(x) + 1)

plt.figure(figsize=(10, 6))
plt.plot(time, x, marker='o', markersize=10, linewidth=2, color='steelblue', markerfacecolor='crimson', markeredgewidth=2)
plt.title('Time Series: x = [20, 20, 20, 25, 25, 25]', fontsize=14, fontweight='bold')
plt.xlabel('Time Index (t)', fontsize=12)
plt.ylabel('Value (x_t)', fontsize=12)
plt.grid(True, alpha=0.3, linestyle='--')
plt.xticks(time)
plt.yticks(x)
plt.tight_layout()
plt.savefig('idea/figures/problem2_3_timeseries.png', dpi=300, bbox_inches='tight')
plt.close()

print("Figure saved: idea/figures/problem2_3_timeseries.png")

# Problem 2.5: Time series x = [10, 12, 14, 10, 12, 14, 10]
x = np.array([10, 12, 14, 10, 12, 14, 10])
time = np.arange(1, len(x) + 1)

plt.figure(figsize=(10, 6))
plt.plot(time, x, marker='o', markersize=10, linewidth=2, color='steelblue', markerfacecolor='crimson', markeredgewidth=2)
plt.title('Time Series: x = [10, 12, 14, 10, 12, 14, 10]', fontsize=14, fontweight='bold')
plt.xlabel('Time Index (t)', fontsize=12)
plt.ylabel('Value (x_t)', fontsize=12)
plt.grid(True, alpha=0.3, linestyle='--')
plt.xticks(time)
plt.yticks(x)
plt.tight_layout()
plt.savefig('idea/figures/problem2_5_timeseries.png', dpi=300, bbox_inches='tight')
plt.close()

print("Figure saved: idea/figures/problem2_5_timeseries.png")

# Problem 3.1: White noise time series
np.random.seed(42)
n = 200
white_noise = np.random.normal(loc=0, scale=1, size=n)
time = np.arange(n)

plt.figure(figsize=(12, 6))
plt.plot(time, white_noise, linewidth=0.8, color='steelblue')
plt.title('White Noise Time Series', fontsize=14, fontweight='bold')
plt.xlabel('Time', fontsize=12)
plt.ylabel('Value', fontsize=12)
plt.grid(True, alpha=0.3, linestyle='--')
plt.axhline(y=0, color='gray', linestyle='-', alpha=0.5, linewidth=1)
plt.tight_layout()
plt.savefig('idea/figures/problem3_1_timeseries.png', dpi=300, bbox_inches='tight')
plt.close()

print("Figure saved: idea/figures/problem3_1_timeseries.png")

# Problem 3.2: Random walk (non-stationary with slow ACF decay)
np.random.seed(42)
n = 200
time = np.arange(n)
random_walk = np.cumsum(np.random.normal(0, 1, n))

plt.figure(figsize=(12, 6))
plt.plot(time, random_walk, linewidth=1, color='crimson')
plt.title('Random Walk Time Series (Non-Stationary)', fontsize=14, fontweight='bold')
plt.xlabel('Time', fontsize=12)
plt.ylabel('Value', fontsize=12)
plt.grid(True, alpha=0.3, linestyle='--')
plt.tight_layout()
plt.savefig('idea/figures/problem3_2_timeseries.png', dpi=300, bbox_inches='tight')
plt.close()

print("Figure saved: idea/figures/problem3_2_timeseries.png")

# Problem 3.3: Seasonal time series (period = 12)
np.random.seed(42)
n = 200
time = np.arange(n)
seasonal_period = 12
seasonal_component = 5 * np.sin(2 * np.pi * time / seasonal_period)
trend = 0.02 * time
noise = np.random.normal(0, 0.5, n)
seasonal_series = trend + seasonal_component + noise

plt.figure(figsize=(12, 6))
plt.plot(time, seasonal_series, linewidth=1, color='steelblue')
plt.title('Time Series with Seasonality (Period = 12)', fontsize=14, fontweight='bold')
plt.xlabel('Time', fontsize=12)
plt.ylabel('Value', fontsize=12)
plt.grid(True, alpha=0.3, linestyle='--')
plt.tight_layout()
plt.savefig('idea/figures/problem3_3_timeseries.png', dpi=300, bbox_inches='tight')
plt.close()

print("Figure saved: idea/figures/problem3_3_timeseries.png")

# Problem 3.4: MA(2) process - manually generate
np.random.seed(42)
n = 200
epsilon = np.random.normal(0, 1, n + 2)  # Extra for lag
ma2_series = np.zeros(n)
theta1, theta2 = 0.5, 0.3
for t in range(n):
    ma2_series[t] = epsilon[t+2] + theta1 * epsilon[t+1] + theta2 * epsilon[t]

plt.figure(figsize=(12, 6))
time = np.arange(n)
plt.plot(time, ma2_series, linewidth=1, color='steelblue')
plt.title('MA(2) Time Series', fontsize=14, fontweight='bold')
plt.xlabel('Time', fontsize=12)
plt.ylabel('Value', fontsize=12)
plt.grid(True, alpha=0.3, linestyle='--')
plt.axhline(y=0, color='gray', linestyle='-', alpha=0.5, linewidth=1)
plt.tight_layout()
plt.savefig('idea/figures/problem3_4_timeseries.png', dpi=300, bbox_inches='tight')
plt.close()

print("Figure saved: idea/figures/problem3_4_timeseries.png")

# Problem 3.5: AR(1) process - manually generate
np.random.seed(42)
n = 200
ar1_series = np.zeros(n)
phi = 0.7
epsilon = np.random.normal(0, 1, n)
ar1_series[0] = epsilon[0]
for t in range(1, n):
    ar1_series[t] = phi * ar1_series[t-1] + epsilon[t]

plt.figure(figsize=(12, 6))
time = np.arange(n)
plt.plot(time, ar1_series, linewidth=1, color='steelblue')
plt.title('AR(1) Time Series (φ = 0.7)', fontsize=14, fontweight='bold')
plt.xlabel('Time', fontsize=12)
plt.ylabel('Value', fontsize=12)
plt.grid(True, alpha=0.3, linestyle='--')
plt.axhline(y=0, color='gray', linestyle='-', alpha=0.5, linewidth=1)
plt.tight_layout()
plt.savefig('idea/figures/problem3_5_timeseries.png', dpi=300, bbox_inches='tight')
plt.close()

print("Figure saved: idea/figures/problem3_5_timeseries.png")

# Problem 4.1: Heart rate (AR(1) with φ = 0.8)
np.random.seed(42)
n = 300
heart_rate_base = np.zeros(n)
phi = 0.8
epsilon = np.random.normal(0, 1, n)
heart_rate_base[0] = epsilon[0]
for t in range(1, n):
    heart_rate_base[t] = phi * heart_rate_base[t-1] + epsilon[t]
heart_rate_mean = 75
heart_rate_std = 8
heart_rate = heart_rate_mean + heart_rate_std * heart_rate_base

plt.figure(figsize=(12, 6))
time = np.arange(len(heart_rate))
plt.plot(time, heart_rate, linewidth=1, color='crimson')
plt.title('Synthetic Heart Rate Time Series', fontsize=14, fontweight='bold')
plt.xlabel('Time (seconds)', fontsize=12)
plt.ylabel('Heart Rate (bpm)', fontsize=12)
plt.grid(True, alpha=0.3, linestyle='--')
plt.axhline(y=heart_rate_mean, color='gray', linestyle='--', alpha=0.5, linewidth=1)
plt.tight_layout()
plt.savefig('idea/figures/problem4_1_timeseries.png', dpi=300, bbox_inches='tight')
plt.close()

print("Figure saved: idea/figures/problem4_1_timeseries.png")

# Problem 4.2: Blood pressure (random walk)
np.random.seed(42)
n = 300
shocks = np.random.normal(0, 2, n)
blood_pressure = np.cumsum(shocks) + 120

plt.figure(figsize=(12, 6))
time = np.arange(n)
plt.plot(time, blood_pressure, linewidth=1, color='crimson')
plt.title('Blood Pressure Time Series (Non-Stationary)', fontsize=14, fontweight='bold')
plt.xlabel('Time (minutes)', fontsize=12)
plt.ylabel('Blood Pressure (mmHg)', fontsize=12)
plt.grid(True, alpha=0.3, linestyle='--')
plt.tight_layout()
plt.savefig('idea/figures/problem4_2_timeseries.png', dpi=300, bbox_inches='tight')
plt.close()

print("Figure saved: idea/figures/problem4_2_timeseries.png")

# Problem 4.3: EEG signal (oscillatory with period 10)
np.random.seed(42)
n = 400
time = np.arange(n)
period = 10
oscillatory = 3 * np.sin(2 * np.pi * time / period)
trend = 0.01 * time
noise = np.random.normal(0, 0.5, n)
eeg_signal = trend + oscillatory + noise

plt.figure(figsize=(12, 6))
plt.plot(time, eeg_signal, linewidth=0.8, color='steelblue')
plt.title('Synthetic EEG-like Signal (Oscillatory Pattern)', fontsize=14, fontweight='bold')
plt.xlabel('Time (samples)', fontsize=12)
plt.ylabel('Amplitude (μV)', fontsize=12)
plt.grid(True, alpha=0.3, linestyle='--')
plt.tight_layout()
plt.savefig('idea/figures/problem4_3_timeseries.png', dpi=300, bbox_inches='tight')
plt.close()

print("Figure saved: idea/figures/problem4_3_timeseries.png")

# Problem 4.4: Respiratory rate (MA(2))
np.random.seed(42)
n = 300
epsilon = np.random.normal(0, 1, n + 2)
respiratory_base = np.zeros(n)
theta1, theta2 = 0.5, 0.3
for t in range(n):
    respiratory_base[t] = epsilon[t+2] + theta1 * epsilon[t+1] + theta2 * epsilon[t]
respiratory_mean = 16
respiratory_std = 2
respiratory_rate = respiratory_mean + respiratory_std * respiratory_base

plt.figure(figsize=(12, 6))
time = np.arange(len(respiratory_rate))
plt.plot(time, respiratory_rate, linewidth=1, color='steelblue')
plt.title('Synthetic Respiratory Rate Time Series', fontsize=14, fontweight='bold')
plt.xlabel('Time (minutes)', fontsize=12)
plt.ylabel('Respiratory Rate (breaths/min)', fontsize=12)
plt.grid(True, alpha=0.3, linestyle='--')
plt.axhline(y=respiratory_mean, color='gray', linestyle='--', alpha=0.5, linewidth=1)
plt.tight_layout()
plt.savefig('idea/figures/problem4_4_timeseries.png', dpi=300, bbox_inches='tight')
plt.close()

print("Figure saved: idea/figures/problem4_4_timeseries.png")

# Problem 4.5: Body temperature (AR(1) with φ = 0.9)
np.random.seed(42)
n = 300
temp_base = np.zeros(n)
phi = 0.9
epsilon = np.random.normal(0, 1, n)
temp_base[0] = epsilon[0]
for t in range(1, n):
    temp_base[t] = phi * temp_base[t-1] + epsilon[t]
temp_mean = 37.0
temp_std = 0.3
body_temp = temp_mean + temp_std * temp_base

plt.figure(figsize=(12, 6))
time = np.arange(len(body_temp))
plt.plot(time, body_temp, linewidth=1, color='crimson')
plt.title('Synthetic Body Temperature Time Series', fontsize=14, fontweight='bold')
plt.xlabel('Time (hours)', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)
plt.grid(True, alpha=0.3, linestyle='--')
plt.axhline(y=temp_mean, color='gray', linestyle='--', alpha=0.5, linewidth=1)
plt.tight_layout()
plt.savefig('idea/figures/problem4_5_timeseries.png', dpi=300, bbox_inches='tight')
plt.close()

print("Figure saved: idea/figures/problem4_5_timeseries.png")
