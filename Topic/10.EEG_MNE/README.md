# Topic 10 – EEG Analysis with MNE Sample Dataset

**Level:** Hard  
**Goal:** Use EEG time series (one or a few channels) for analysis and simple modeling.

## Library & Data

- **MNE Python:** https://mne.tools/stable/
- **MNE Datasets:** https://mne.tools/stable/documentation/datasets.html

## Installation

```bash
pip install mne
```

## Data Loading

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

## Implementation Steps

### 1. Library Setup and Data Loading
- Install MNE library
- Download sample dataset (automatic on first use)
- Load EEG data
- Understand MNE data structure

### 2. Data Exploration
- Inspect available EEG channels
- Select 1-3 channels for analysis
- Examine sampling rate (typically 100-1000 Hz)
- Plot raw EEG signals
- Understand signal characteristics

### 3. Data Preprocessing
- **Filtering:**
  - Apply band-pass filter (e.g., 1-40 Hz for EEG)
  - Remove line noise (50/60 Hz) if present
- **Artifact Removal:**
  - Identify and remove artifacts (eye blinks, muscle activity)
  - Use MNE's artifact detection methods
- **Downsampling (optional):**
  - May need to downsample for time series analysis
  - Preserve frequency content of interest

### 4. Feature Extraction
- **Frequency Domain:**
  - Calculate power spectral density (PSD)
  - Analyze frequency bands (delta, theta, alpha, beta, gamma)
  - Extract band power over time
- **Time Domain:**
  - Extract amplitude features
  - Calculate statistical features (mean, std, etc.)
- **Create Lower-Frequency Series:**
  - Extract features per time window (e.g., alpha power per second)
  - Create time series of extracted features

### 5. Exploratory Data Analysis (EDA)
- Plot raw and filtered signals
- Visualize frequency content (spectrogram, PSD)
- Analyze temporal patterns
- Examine stationarity of extracted features

### 6. Model Building
- **Feature Time Series:**
  - Apply ARIMA/SARIMA to extracted features (e.g., alpha power)
  - Model lower-frequency derived series
- **Raw Signal (advanced):**
  - May need specialized methods for high-frequency signals
  - Consider state-space models or specialized EEG analysis

### 7. Model Evaluation
- Split data temporally
- Generate forecasts for features
- Calculate accuracy metrics
- Visualize results
- Compare with neurophysiological expectations

### 8. Neurophysiological Interpretation
- Interpret results in neuroscience context
- Relate to known EEG patterns (alpha, beta waves)
- Discuss implications for signal analysis
- Compare with EEG literature

## Expected Deliverables

1. **EDA Report:**
   - Raw and filtered EEG plots
   - Frequency analysis (PSD, spectrograms)
   - Feature extraction results
   - Temporal pattern analysis

2. **Model Results:**
   - Selected models for feature time series
   - Forecast accuracy
   - Visualization of results
   - Neurophysiological interpretation

3. **Code:**
   - Complete Python notebook
   - MNE data loading and preprocessing functions
   - Feature extraction utilities
   - Visualization tools

## Tips

- EEG data is high-frequency and requires specialized preprocessing
- Filtering is essential (remove artifacts, focus on frequency bands of interest)
- Consider extracting features rather than modeling raw signals directly
- Frequency domain analysis is often more informative than time domain
- Use MNE's built-in functions for preprocessing and analysis
- Understand neurophysiological context (different frequency bands have different meanings)
- Downsampling may be necessary for standard time series methods
- Document all preprocessing steps (filtering, artifact removal)
- Consider event-related analysis in addition to continuous forecasting
- Consult neuroscience literature for appropriate analysis methods

