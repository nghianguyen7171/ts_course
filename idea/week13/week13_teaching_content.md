# Week 13: Advanced Traditional Models & Machine Learning for Time Series

## Part 1: Brief Introduction to Advanced Traditional Models (ARCH/GARCH)

In many financial and economic time series, the variance of the series is not constant over time. This phenomenon is known as **heteroskedasticity**.

### Volatility Clustering
Volatility clustering refers to the observation that large changes in a time series tend to be followed by large changes (of either sign), and small changes tend to be followed by small changes. This is common in stock returns, exchange rates, and other financial data.

### Autoregressive Conditional Heteroskedasticity (ARCH)
Traditional models like ARIMA assume that the variance of the residuals (errors) is constant (homoskedastic). 
The **ARCH** model, introduced by Robert Engle (1982), addresses this by modeling the variance of the current error term as a function of the actual sizes of the previous time periods' error terms.

- **Use case:** When the residuals of an ARIMA model exhibit volatility clustering.

### Generalized ARCH (GARCH)
The **GARCH** model, developed by Tim Bollerslev (1986), generalizes the ARCH model. It models the conditional variance as a function of both past squared errors (the ARCH component) and past variances (the GARCH component).
- **GARCH(p, q):** `p` refers to the number of lag variances, and `q` refers to the number of lag squared errors.
- **Relationship with ARIMA:** A common pipeline in finance is an ARMA-GARCH model. ARMA models the *mean* (expected value), while GARCH models the *variance* (volatility or risk) of the series simultaneously.

---

## Part 2: Time Series as Supervised Learning

To use standard machine learning models (like Random Forests or Gradient Boosting) for time series forecasting, we must transform our sequence data into a tabular format, treating it as a **supervised learning problem** where input features ($X$) map to a target variable ($y$).

### Feature Engineering
The core of this transformation relies heavily on feature engineering. Common features include:

1. **Lag Features:** 
   Using past values of the target variable as predictors. For example, to predict $y_t$, we might use $y_{t-1}, y_{t-2}, y_{t-3}$ as features.
2. **Rolling-Window Statistics:** 
   Applying summary statistics over a trailing window of time. 
   - *Rolling Mean:* Captures the local trend or smoothed value over the past $N$ periods.
   - *Rolling Standard Deviation:* Captures local volatility.
3. **Calendar / Time Variables:** 
   Extracting categorical or numerical features from the timestamp itself, such as:
   - Hour of day, day of week, month, quarter.
   - Boolean markers for weekends, holidays, or business days.

### Multi-step Forecasting Strategies
If we need to forecast multiple steps into the future, we generally use one of two strategies with ML models:
1. **Direct Strategy:** Train a separate model for each forecast horizon (e.g., Model 1 predicts $t+1$, Model 2 predicts $t+2$).
2. **Recursive Strategy:** Train a single one-step-ahead model. Use its prediction for $t+1$ as a feature to predict $t+2$, and so on. This can suffer from accumulated error over long horizons.

---

## Part 3: ML Models for Forecasting

Once the data is tabular, we can apply various regression algorithms.

### Linear Regression as a Baseline
Before jumping into complex models, a simple Linear Regression model using lagged and calendar features serves as a robust baseline. It is easy to interpret and fast to train.

### Tree-based Models (Random Forests & Gradient Boosting)
Tree-based models have become highly popular for tabular data.
- **Random Forest:** An ensemble of decision trees built on bootstrapped samples, which reduces overfitting.
- **Gradient Boosting (e.g., XGBoost, LightGBM):** Sequentially builds trees to correct the errors of previous trees, often achieving state-of-the-art performance on structured data.

### Strengths and Limitations
- **Strengths:** Tree-based models are excellent at capturing non-linear relationships, interacting features (e.g., specific combinations of lagged values and day-of-week), and handling outliers.
- **Limitations:** Unlike ARIMA, tree-based models cannot extrapolate trends outside the bounds of the training data. If there is a strong upward trend, a tree-based model will flatline its predictions for future values that are higher than anything seen in the training set. Therefore, data must often be explicitly detrended or differenced before applying tree-based models.

---

## Part 4: Temporal Validation Strategies

When evaluating machine learning models on time series, we cannot use standard random $k$-fold cross-validation. Randomly splitting the data leads to **data leakage** because the model would use future data to predict the past.

### Rolling-Origin Validation (Time Series Split)
In this approach, we create multiple training and validation splits respecting the chronological order:
- Split 1: Train on data up to time $T$, validate on $T+1$ to $T+H$.
- Split 2: Train on data up to time $T+H$, validate on $T+H+1$ to $T+2H$.
This ensures the model never sees future data during training.

### Walk-Forward Validation
Similar to rolling-origin, walk-forward validation repeatedly refits the model as new data becomes available. This closely mimics a production environment where the model is retrained periodically (e.g., daily or weekly) to capture the latest dynamics.

---

## Part 5: Practical Examples & Comparisons

To wrap up, it is instructive to compare the traditional and machine learning approaches.

### Pipeline Comparison
- **Statistical Pipeline (e.g., Box-Jenkins / ARIMA):**
  1. Test for stationarity (ADF test).
  2. Apply differencing if needed.
  3. Analyze ACF/PACF to identify AR and MA terms.
  4. Fit the model and evaluate information criteria (AIC/BIC).
  5. Perform residual diagnostics (Ljung-Box test, Q-Q plots).
- **Machine Learning Pipeline (Supervised):**
  1. Perform feature engineering (lags, rolling stats, date features).
  2. Detrend the data if using tree-based models.
  3. Split data chronologically (Time Series Split).
  4. Train the model (e.g., XGBoost) and tune hyperparameters using validation sets.
  5. Evaluate using standard regression metrics (MAE, RMSE, MAPE).

### Pros and Cons: ARIMA/SARIMA vs. Random Forest/XGBoost

| Feature | ARIMA / SARIMA | Tree-based ML (RF, XGBoost) |
| :--- | :--- | :--- |
| **Data Requirements** | Works well with small datasets. | Often requires larger datasets to capture complex patterns. |
| **Exogenous Variables** | Handled via SARIMAX, but strictly linear relationships. | Easily integrates multiple, non-linear, and categorical exogenous features. |
| **Trend Handling** | Handled natively via differencing ($d$ term). | Cannot extrapolate; requires explicit detrending. |
| **Interpretability** | High (coefficients are directly tied to past lags/errors). | Moderate to Low (requires feature importance or SHAP values). |
| **Setup Complexity** | High domain knowledge needed (ACF/PACF interpretation). | Heavy focus on feature engineering; training is straightforward. |
