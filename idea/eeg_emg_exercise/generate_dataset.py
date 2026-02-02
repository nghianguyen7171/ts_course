"""
Generate synthetic EEG and EMG time series for practice exercise.
- EEG: simulated alpha-band power over 1-min epochs (trend + weak oscillation + AR structure).
- EMG: simulated RMS amplitude over 1-min epochs (trend + MA structure).
Slightly higher complexity: two signals, different dynamics, optional periodicity in EEG.
Reproducible via fixed seed; run once and commit data/eeg_emg_ts.csv.
"""
import numpy as np
import pandas as pd
from pathlib import Path

np.random.seed(43)

# Length: 800 1-minute epochs (~13.3 hours of recording)
n = 800
dates = pd.date_range(start="2022-01-01 00:00:00", periods=n, freq="1min")

# ---- EEG (alpha power, microvolts^2 scale) ----
# Non-stationary: linear trend (e.g. drowsiness) + cumsum of AR(1) + weak alpha-rhythm oscillation
drift_eeg = 0.015
phi_eeg = 0.55
sigma_eeg = 1.8
period_alpha = 60  # ~1 Hz modulation (cycle every 60 epochs)

z_eeg = np.zeros(n)
z_eeg[0] = drift_eeg + sigma_eeg * np.random.randn()
for t in range(1, n):
    z_eeg[t] = drift_eeg + phi_eeg * (z_eeg[t - 1] - drift_eeg) + sigma_eeg * np.random.randn()

trend_eeg = 0.02 * np.arange(n)
oscillation = 4.0 * np.sin(2 * np.pi * np.arange(n) / period_alpha)
eeg_level = np.cumsum(z_eeg) + trend_eeg + oscillation
eeg_alpha_power = 20 + eeg_level  # scale to plausible alpha power range

# ---- EMG (RMS amplitude, arbitrary units) ----
# Non-stationary: linear trend + cumsum of MA(1) innovations (burst-like dynamics)
theta_emg = 0.6
sigma_emg = 2.0
w = sigma_emg * np.random.randn(n)
# MA(1): z_t = w_t + theta * w_{t-1}
z_emg = np.zeros(n)
z_emg[0] = w[0]
for t in range(1, n):
    z_emg[t] = w[t] + theta_emg * w[t - 1]

drift_emg = 0.03
trend_emg = 0.015 * np.arange(n)
emg_level = np.cumsum(drift_emg + z_emg) + trend_emg
emg_rms = 50 + emg_level  # scale to plausible RMS range

df = pd.DataFrame({
    "date": dates,
    "eeg_alpha_power": np.round(eeg_alpha_power, 4),
    "emg_rms": np.round(emg_rms, 4),
})
out_dir = Path(__file__).resolve().parent / "data"
out_dir.mkdir(parents=True, exist_ok=True)
out_path = out_dir / "eeg_emg_ts.csv"
df.to_csv(out_path, index=False)
print(f"Saved {len(df)} rows to {out_path}")
