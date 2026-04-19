# Week 14: Deep Learning for Time Series

## Part 1: Deep Learning Architectures for Time Series

While traditional machine learning (like Random Forests) transforms time series into tabular data using feature engineering, deep learning architectures are inherently designed to process raw sequence data directly.

### Recurrent Neural Networks (RNNs)
- **Concept:** RNNs maintain a "hidden state" (memory) that is updated as each new step in the sequence is processed. This allows them to capture temporal dependencies.
- **Limitation:** Standard RNNs struggle with long sequences due to the **vanishing gradient problem**. As gradients are backpropagated through time, they shrink exponentially, causing the network to "forget" earlier inputs.

### LSTM (Long Short-Term Memory) & GRU (Gated Recurrent Unit)
- **Concept:** To solve the vanishing gradient issue, LSTMs introduce a "cell state" and three gates (Forget, Input, Output). These gates regulate the flow of information, allowing the network to explicitly decide what to remember over long periods and what to discard.
- **GRU:** A streamlined, computationally faster variant of the LSTM that merges some of the gates (Reset and Update gates) while maintaining similar performance on many tasks.

### 1D-Convolutional Neural Networks (1D-CNN)
- **Concept:** While CNNs are famous for 2D image processing, 1D-CNNs slide a one-dimensional filter across the time axis.
- **Advantage:** They are excellent at extracting local temporal patterns (like short-term shapes, spikes, or motifs) and are often much faster to train than LSTMs because they don't have to process sequences sequentially.

---

## Part 2: Typical DL Workflows for Time Series

Deep learning models require specific data preparation steps that differ from classical models.

### Sliding Window Input (3D Tensor)
Unlike tabular ML which requires a 2D shape `(samples, features)`, RNNs/LSTMs require a 3D tensor shape:
`[batch_size, time_steps, features]`
- **batch_size:** The number of samples processed at once.
- **time_steps:** The length of the historical window (lookback period) used to make a prediction.
- **features:** The number of variables measured at each time step (e.g., 1 for univariate, $N$ for multivariate).

### Prediction Setups
- **Sequence-to-One:** The network takes in $T$ past steps and outputs a single future step ($T+1$).
- **Sequence-to-Sequence:** The network takes in $T$ past steps and simultaneously outputs the next $H$ future steps.

### Normalization
Deep learning models are highly sensitive to the scale of the input data. Large values can cause exploding gradients or slow convergence.
- **Critical Step:** Always apply `MinMaxScaler` or `StandardScaler` to the training set, and then transform the validation/test sets using the fitted scaler.

### Temporal Train/Validation Splits
As with ML models, never use random $k$-fold cross-validation. Use chronological splits or walk-forward validation to prevent data leakage.

---

## Part 3: Simple LSTM Example (Keras/TensorFlow)

Here is a conceptual overview of building a univariate forecasting model using an LSTM.

### 1. Data Preparation
```python
from sklearn.preprocessing import MinMaxScaler
import numpy as np

# Scale the data
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(raw_data)

# Create sequences
def create_sequences(data, time_steps):
    X, y = [], []
    for i in range(len(data) - time_steps):
        X.append(data[i:(i + time_steps)])
        y.append(data[i + time_steps])
    return np.array(X), np.array(y)

time_steps = 24 # Use past 24 hours
X_train, y_train = create_sequences(scaled_data_train, time_steps)
# X_train shape is now (samples, 24, 1)
```

### 2. Model Definition
```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

model = Sequential([
    LSTM(50, activation='relu', input_shape=(time_steps, 1)),
    Dense(1) # Predict a single future value
])

model.compile(optimizer='adam', loss='mse')
```

### 3. Training & Evaluation
```python
# Train the model
history = model.fit(X_train, y_train, epochs=20, batch_size=32, validation_split=0.1, shuffle=False)

# Evaluate (Remember to inverse_transform predictions to compute true MAE/RMSE)
predictions = model.predict(X_test)
predictions_real = scaler.inverse_transform(predictions)
```

---

## Part 4: Discussion - When to use Deep Learning?

Deep Learning is powerful, but it is not a silver bullet for time series forecasting.

### When DL is Highly Useful:
- **Massive Datasets:** You have hundreds of thousands or millions of data points.
- **High-Frequency/Raw Sensor Data:** Processing raw audio, EEG, or vibration telemetry where manual feature engineering is incredibly difficult.
- **Complex Multivariate Relationships:** You have dozens of interacting exogenous variables with deep non-linear effects over time.

### When Classical/ML Models are Sufficient (or Superior):
- **Small to Medium Datasets:** ARIMA or XGBoost will almost always outperform LSTMs on short or medium-length datasets (e.g., monthly macro-economic data, 144 airline passenger rows). Deep learning easily overfits small data.
- **Interpretability Needed:** If business stakeholders need to know *why* a forecast was made, ARIMA (coefficients) or Random Forests (feature importance) are much easier to explain than a black-box neural network.
- **Setup & Compute Constraints:** Classical models take seconds to run on a CPU. DL models require careful architectural tuning, hyperparameter search, scaling, and ideally GPU acceleration.
