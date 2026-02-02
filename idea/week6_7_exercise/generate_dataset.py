"""
Generate synthetic healthcare time series for Week 6-7 exercise.
Series: daily hospital admissions (simulated) with trend and AR(1) structure after differencing.
Reproducible via fixed seed; run once and commit data/healthcare_ts.csv.
"""
import numpy as np
import pandas as pd
from pathlib import Path

np.random.seed(42)

# Length: ~2 years daily
n = 730
dates = pd.date_range(start="2022-01-01", periods=n, freq="D")

# Design: Y_t = Y_{t-1} + Z_t, so diff(Y)_t = Z_t.
# Z_t = drift + phi * Z_{t-1} + eps_t (AR(1)), so first difference is stationary AR(1).
# Raw Y will have unit root (ADF fails); diff(Y) is AR(1) (ADF passes, ACF/PACF suggest ARIMA(1,1,0)).
drift = 0.8
phi = 0.6
sigma = 12.0

z = np.zeros(n)
z[0] = drift + sigma * np.random.randn()
for t in range(1, n):
    z[t] = drift + phi * (z[t - 1] - drift) + sigma * np.random.randn()

# Level: Y_t = cumsum(Z_t), so diff(Y) = Z
y = np.cumsum(z)

# Scale to plausible "daily admissions" range and add a small linear trend for extra clarity
trend = 0.05 * np.arange(n)
value = 80 + y + trend

df = pd.DataFrame({"date": dates, "value": value})
out_dir = Path(__file__).resolve().parent / "data"
out_dir.mkdir(parents=True, exist_ok=True)
out_path = out_dir / "healthcare_ts.csv"
df.to_csv(out_path, index=False)
print(f"Saved {len(df)} rows to {out_path}")
