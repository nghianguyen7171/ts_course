# EEG & EMG Practice Exercise: Stationarity, Unit Root, Differencing, AR/MA/ARMA

**Objective:** Use synthetic EEG and EMG time series to practice the full pipeline (unit root testing, differencing, ACF/PACF model selection, AR/MA/ARMA fitting, evaluation) with **EEG- and EMG-specific** interpretations (alpha rhythm, burst dynamics, physiological non-stationarity).

## Dataset

- **File:** `data/eeg_emg_ts.csv`
- **Description:** Two univariate series over the same time index (1-minute epochs, 800 epochs).
  - **eeg_alpha_power:** Simulated EEG alpha-band power (e.g. 8–12 Hz band power, microvolts² scale). Includes trend, weak periodic modulation, and AR-like dynamics.
  - **emg_rms:** Simulated EMG RMS amplitude (arbitrary units). Includes trend and MA-like dynamics (burst-like behavior).
- **Length:** 800 rows (~13.3 hours of 1-min epochs).
- **Columns:** `date`, `eeg_alpha_power`, `emg_rms`.

## Tasks (no solutions in this README)

1. **Load and explore**
   - Load the CSV, parse `date`, set datetime index. Plot both series (EEG and EMG) and compute basic statistics.
   - Comment on trend, variability, and **physiological interpretation** (e.g. alpha power changes over a recording session; EMG baseline drift and burst structure).

2. **Unit root tests**
   - Run the **ADF** test on the **raw** EEG series and on the **raw** EMG series. Report test statistic, p-value, and critical values for each.
   - Conclude for each series whether it is stationary or has a unit root. Optionally run **KPSS** and compare.

3. **Differencing**
   - Compute the **first difference** of each series. Plot both differenced series.
   - Run ADF (and optionally KPSS) on each **differenced** series. Conclude stationarity and appropriate **d** (e.g. d = 1 for both).

4. **ACF and PACF for model selection**
   - Plot **ACF** and **PACF** of the **differenced EEG** series. Use the usual guidelines to suggest (p, q) for the differenced series, hence **ARIMA(p, 1, q)** for the raw EEG. Note any **periodic peaks** (e.g. alpha-rhythm modulation).
   - Plot **ACF** and **PACF** of the **differenced EMG** series. Suggest **ARIMA(p, 1, q)** for the raw EMG. Comment on **EMG-specific** behavior (e.g. short memory, MA-like cutoff).

5. **AR/MA/ARMA fit**
   - Fit 2–3 candidate **ARIMA(p, 1, q)** models for the **EEG** series. Report coefficients, AIC, BIC. Choose a preferred model.
   - Fit 2–3 candidate **ARIMA(p, 1, q)** models for the **EMG** series. Report coefficients, AIC, BIC. Choose a preferred model.
   - Compare the **EEG** and **EMG** preferred orders and interpret (e.g. AR vs MA dominance).

6. **Evaluation**
   - **Residual diagnostics:** For both preferred models, plot ACF of residuals and run a **Ljung–Box** test. Comment on white-noise behavior.
   - **Forecast evaluation:** For both series, use a temporal train/test split (e.g. last 10–15%). Compute **RMSE** and **MAE** and plot forecasts vs actual. Briefly compare EEG vs EMG forecastability.

## Deliverables

- A Jupyter notebook that performs all steps above with **EEG- and EMG-specific** interpretations.
- For the solution key, see `solution_key.ipynb` (instructor use).
