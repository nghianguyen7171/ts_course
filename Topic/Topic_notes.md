

## Topic 1 – Basic Stock Price Time Series (S\&P 500)

**Level:** Easy
**Goal:** Univariate forecasting of daily stock prices (close price) for one S\&P 500 company.

**Dataset:**

- S\&P 500 stock data – Kaggle: https://www.kaggle.com/datasets/camnugent/sandp500[^1]

**Download (manual):**

```markdown
1. Open https://www.kaggle.com/datasets/camnugent/sandp500
2. Log in to Kaggle.
3. Click "Download".
4. Extract ZIP to `data/`.
5. Use `all_stocks_5yr.csv`.
```

**Load (Python, local):**

```python
import pandas as pd

df = pd.read_csv("data/all_stocks_5yr.csv")
aapl = df[df["Name"] == "AAPL"].copy()
aapl["date"] = pd.to_datetime(aapl["date"])
aapl = aapl.set_index("date").sort_index()
```


***

## Topic 2 – Monthly Business Sales Time Series

**Level:** Easy
**Goal:** Analyze and forecast monthly / periodic sales or revenue.

**Dataset:**

- Business Sales Time Series Starter – OpenDataBay:
https://www.opendatabay.com/data/ai-ml/f86d74d9-4656-4313-94d7-0cbd12bb7ffd[^2]

**Download:**

```markdown
1. Open the link.
2. Click "Download CSV" (e.g. `Month_Value_1.csv`).
3. Save as `data/business_sales.csv`.
```

**Load:**

```python
import pandas as pd

df = pd.read_csv("data/business_sales.csv")
df["Month"] = pd.to_datetime(df["Month"])
df = df.set_index("Month").sort_index()
```


***

## Topic 3 – GDP Time Series for Multiple Countries (Kaggle)

**Level:** Easy → Medium
**Goal:** Forecast annual GDP for 1–3 countries, compare trends and growth.

**Dataset:**

- GDP Timeseries Data for various Countries – Kaggle:
https://www.kaggle.com/datasets/iamtushara/gdp-timeseries-data-for-various-countries[^3]

**Download:**

```markdown
1. Open the dataset link.
2. Click "Download".
3. Extract to `data/`.
4. Use the main GDP CSV (e.g. `gdp_timeseries.csv`).
```

**Load:**

```python
import pandas as pd

df = pd.read_csv("data/gdp_timeseries.csv")  # adjust filename
country = df[df["Country"] == "Vietnam"].copy()  # example filter
country["Year"] = pd.to_datetime(country["Year"], format="%Y")
country = country.set_index("Year").sort_index()
```


***

## Topic 4 – US Macroeconomic Indicators (Kaggle)

**Level:** Medium
**Goal:** Model and forecast key US macro indicators (unemployment, inflation, etc.).

**Dataset (example):**

- U.S. Economic Time Series – Kaggle:
https://www.kaggle.com/datasets/utkarshx27/us-economic-time-series[^4]

**Download:**

```markdown
1. Open the dataset link.
2. Click "Download".
3. Extract to `data/`.
4. Use the main CSV, e.g. `USEconomicData.csv`.
```

**Load:**

```python
import pandas as pd

df = pd.read_csv("data/USEconomicData.csv")  # adjust filename
df["DATE"] = pd.to_datetime(df["DATE"])
df = df.set_index("DATE").sort_index()
```


***

## Topic 5 – Single-Stock Case Study: NVIDIA (NVDA)

**Level:** Medium
**Goal:** Univariate forecasting and volatility exploration for a single stock.

**Dataset:**

- NVIDIA (NVDA) Historical Stock Price Data – Kaggle:
https://www.kaggle.com/datasets/elnazalikarami/nvidia-corporation-stock-historical-quotes[^5]

**Download:**

```markdown
1. Open the dataset link.
2. Click "Download".
3. Extract to `data/`.
4. Use the main CSV (e.g. `HistoricalData_....csv`).
```

**Load:**

```python
import pandas as pd

df = pd.read_csv("data/NVDA_HistoricalData.csv")  # adjust filename
df["Date"] = pd.to_datetime(df["Date"])
df = df.set_index("Date").sort_index()
```


***

## Topic 6 – Multivariate Financial Time Series Bundle

**Level:** Medium → Hard
**Goal:** Model several assets jointly (correlations, VAR, multivariate forecasting).

**Dataset:**

- Financial Time Series Datasets – Kaggle:
https://www.kaggle.com/datasets/praxitelisk/financial-time-series-datasets[^6]

**Download:**

```markdown
1. Open the dataset page.
2. Click "Download".
3. Extract to `data/financial/`.
4. Choose some CSVs (indices, FX, commodities).
```

**Load (example):**

```python
import pandas as pd
import os

print(os.listdir("data/financial"))

sp500 = pd.read_csv("data/financial/sp500.csv")  # adjust
oil   = pd.read_csv("data/financial/oil.csv")    # adjust

for df_ in (sp500, oil):
    df_["Date"] = pd.to_datetime(df_["Date"])
    df_.set_index("Date", inplace=True)
    df_.sort_index(inplace=True)

merged = sp500[["Close"]].rename(columns={"Close": "SP500"}).join(
    oil[["Close"]].rename(columns={"Close": "OIL"}), how="inner"
)
```


***

## Topic 7 – Human Vital Signs (Kaggle)

**Level:** Medium
**Goal:** Analyze and forecast physiological signals (HR, BP, SpO2, etc.).

**Dataset:**

- Human Vital Sign Dataset – Kaggle:
https://www.kaggle.com/datasets/nasirayub2/human-vital-sign-dataset[^7]

**Download:**

```markdown
1. Open the dataset link.
2. Click "Download".
3. Extract to `data/vital_signs/`.
4. Use the main CSV, e.g. `HumanVitalSigns.csv`.
```

**Load:**

```python
import pandas as pd

df = pd.read_csv("data/vital_signs/HumanVitalSigns.csv")  # adjust
df["Time"] = pd.to_datetime(df["Time"])  # adapt time column name
df = df.set_index("Time").sort_index()
```


***

## Topic 8 – High-Resolution Vital Signs with VitalDB (Python Library)

**Level:** Medium → Hard
**Goal:** Work with high-frequency ICU/OR vital signs via VitalDB library.

**Dataset \& Library:**

- VitalDB – PhysioNet: https://physionet.org/content/vitaldb/[^8]
- Python library `vitaldb`, docs: https://vitaldb.net/docs/[^9]

**Install and load:**

```bash
pip install vitaldb
```

```python
import vitaldb
import pandas as pd

vf = vitaldb.VitalFile(1)  # example case 1
tracks = ["SNUADC/ECG", "Solar 8000/ART1"]

vals, t = vitaldb.vital_recs(vf, track_names=tracks, return_datetime=True)
df = pd.DataFrame(vals, columns=["ECG", "ART"])
df["Time"] = t
df = df.set_index("Time")
```


***

## Topic 9 – Airline Passenger Time Series (Statsmodels built-in)

**Level:** Easy
**Goal:** Classic monthly airline passenger series (trend + seasonality) using a **library dataset**.

**Dataset \& Library:**

- AirPassengers dataset via `statsmodels.datasets.get_rdataset`[^10][^11][^12][^13]

**Install (if needed):**

```bash
pip install statsmodels
```

**Load directly from Python (no manual download):**

```python
import pandas as pd
from statsmodels.datasets import get_rdataset

data = get_rdataset("AirPassengers", "datasets").data
# Original data typically has a 'time' or 'Month' column and 'value' column
print(data.head())

# If there is only an index and a passenger column:
# Example conversion (adapt depending on structure)
data["Month"] = pd.date_range(start="1949-01-01", periods=len(data), freq="M")
data = data.set_index("Month").sort_index()
data.rename(columns={data.columns[^0]: "Passengers"}, inplace=True)

print(data.head())
```

> This replaces the older epidemiology topic: it is much easier to load and is ideal for ARIMA/SARIMA demos.

***

## Topic 10 – EEG Analysis with MNE Sample Dataset

**Level:** Hard
**Goal:** Use EEG time series (one or a few channels) for analysis and simple modeling.

**Library \& Data:**

- MNE datasets: https://mne.tools/stable/documentation/datasets.html[^14][^15]

**Install:**

```bash
pip install mne
```

**Load:**

```python
import mne
import pandas as pd
import numpy as np

data_path = mne.datasets.sample.data_path()
raw_fname = data_path + "/MEG/sample/sample_audvis_raw.fif"

raw = mne.io.read_raw_fif(raw_fname, preload=True)
raw.pick_types(meg=False, eeg=True)

data, times = raw[:1, :]  # first EEG channel
sr = raw.info["sfreq"]
index = pd.to_datetime(times, unit="s")
eeg_series = pd.Series(np.ravel(data), index=index)
```


***

## Topic 11 – ECG Analysis with MIT-BIH (WFDB)

**Level:** Hard
**Goal:** Work with ECG waveforms (e.g. MIT-BIH Arrhythmia).

**Library \& Data:**

- WFDB Python: https://wfdb.io/software/python.html[^16][^17]

**Install and load:**

```bash
pip install wfdb
```

```python
import wfdb
import pandas as pd
import numpy as np

record = wfdb.rdrecord("100", pn_dir="mitdb")
signal = record.p_signal[:, 0]  # first channel
fs = record.fs

times = pd.to_timedelta(np.arange(len(signal)) / fs, unit="s")
ecg_series = pd.Series(signal, index=times)
```


***

## Topic 12 – Open Multidomain Time Series (Custom Advanced Topic)

**Level:** Hard
**Goal:** Choose a series from a curated collection and design a custom forecasting/classification problem.

**Collection:**

- Open Time Series Datasets – GitHub:
https://github.com/liaoyuhua/open-time-series-datasets[^18]

**Download \& load (example):**

```markdown
1. Open the GitHub link.
2. Find a dataset (e.g. airline passengers, air pollution, traffic).
3. Click file → "Download" or "Raw" and save as CSV to `data/open_ts/`.
```

```python
import pandas as pd

df = pd.read_csv("data/open_ts/example.csv")  # adjust
df["Date"] = pd.to_datetime(df["Date"])       # adapt column name
df = df.set_index("Date").sort_index()
```


***

## Topic 13 – Retail Store Sales Time Series (Kaggle Competition Data)

**Level:** Medium → Hard
**Goal:** Daily sales forecasting for multiple stores/items (panel + time series).

**Dataset:**

- Store Sales – Time Series Forecasting (Favorita) – Kaggle:
https://www.kaggle.com/competitions/store-sales-time-series-forecasting/data[^19]

**Download:**

```markdown
1. Open the competition link.
2. Go to "Data" tab.
3. Accept competition rules (if needed).
4. Download `train.csv` and save to `data/store_sales/`.
```

**Load:**

```python
import pandas as pd

df = pd.read_csv("data/store_sales/train.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.set_index("date").sort_index()

print(df.head())
# Columns usually include: date, store_nbr, family, sales, onpromotion, oil_price, etc.
```


***

## Topic 14 – Electricity Load Diagrams (Energy Consumption, Library Dataset)

**Level:** Hard
**Goal:** Model and forecast electricity demand (multiple time series, rich seasonality).

**Dataset (example source):**

- Electricity load diagrams dataset (via libraries like GluonTS/HuggingFace, etc.) – e.g.
https://huggingface.co/datasets/tulipa762/electricity_load_diagrams[^20]

**Download (simple manual approach):**

```markdown
1. Open the link above.
2. Download the CSV file containing the load data (if provided).
3. Save to `data/electricity/`.
```

**Load (if CSV is available):**

```python
import pandas as pd

df = pd.read_csv("data/electricity/electricity.csv")  # adjust filename
print(df.head())

# Example: parse datetime column like "timestamp"
df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df.set_index("timestamp").sort_index()
```

> For advanced groups, using a time-series library (GluonTS, darts, etc.) is encouraged.

***

### Updated Difficulty Layers

- **Easy:**
    - Topic 1 – S\&P 500 single stock
    - Topic 2 – Business sales
    - Topic 3 – GDP series
    - Topic 9 – AirPassengers (statsmodels)
- **Medium:**
    - Topic 4 – US macro indicators
    - Topic 5 – NVDA stock
    - Topic 7 – Human vital signs (Kaggle)
    - Topic 13 – Store sales (Favorita)
- **Hard:**
    - Topic 6 – Multivariate financial bundle
    - Topic 8 – VitalDB high-resolution signals
    - Topic 10 – EEG (MNE)
    - Topic 11 – ECG (WFDB)
    - Topic 12 – Open time series collection
    - Topic 14 – Electricity load diagrams
