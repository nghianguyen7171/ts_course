# Time Series Problem Set: Autocorrelation Function (ACF)

## Exercise Type 1: Numerical ACF Calculation

### Problem 1.1

Given the time series: $x = [2, 4, 6, 8, 10]$

![Time Series Plot](figures/problem1_1_timeseries.png)

Compute:
1. The sample mean $\bar{x}$
2. The sample variance $s^2$
3. The autocovariance $\gamma(k)$ for lags $k = 0, 1, 2$
4. The autocorrelation $\rho(k)$ for lags $k = 0, 1, 2$

**Solution 1.1**

1. **Sample Mean:**
   $$
   \bar{x} = \frac{1}{n}\sum_{t=1}^{n} x_t = \frac{2 + 4 + 6 + 8 + 10}{5} = \frac{30}{5} = 6
   $$

2. **Sample Variance:**
   $$
   s^2 = \frac{1}{n-1}\sum_{t=1}^{n}(x_t - \bar{x})^2
   $$
   
   Deviations from mean:
   - $x_1 - \bar{x} = 2 - 6 = -4$
   - $x_2 - \bar{x} = 4 - 6 = -2$
   - $x_3 - \bar{x} = 6 - 6 = 0$
   - $x_4 - \bar{x} = 8 - 6 = 2$
   - $x_5 - \bar{x} = 10 - 6 = 4$
   
   $$
   s^2 = \frac{(-4)^2 + (-2)^2 + 0^2 + 2^2 + 4^2}{4} = \frac{16 + 4 + 0 + 4 + 16}{4} = \frac{40}{4} = 10
   $$

3. **Autocovariance:**
   
   For lag $k = 0$:
   $$
   \gamma(0) = \frac{1}{n}\sum_{t=1}^{n}(x_t - \bar{x})^2 = \frac{40}{5} = 8
   $$
   
   For lag $k = 1$:
   $$
   \gamma(1) = \frac{1}{n}\sum_{t=1}^{n-1}(x_t - \bar{x})(x_{t+1} - \bar{x})
   $$
   $$
   = \frac{1}{5}[(-4)(-2) + (-2)(0) + (0)(2) + (2)(4)]
   $$
   $$
   = \frac{1}{5}[8 + 0 + 0 + 8] = \frac{16}{5} = 3.2
   $$
   
   For lag $k = 2$:
   $$
   \gamma(2) = \frac{1}{n}\sum_{t=1}^{n-2}(x_t - \bar{x})(x_{t+2} - \bar{x})
   $$
   $$
   = \frac{1}{5}[(-4)(0) + (-2)(2) + (0)(4)]
   $$
   $$
   = \frac{1}{5}[0 - 4 + 0] = -\frac{4}{5} = -0.8
   $$

4. **Autocorrelation:**
   $$
   \rho(k) = \frac{\gamma(k)}{\gamma(0)}
   $$
   
   - $\rho(0) = \frac{8}{8} = 1.0$
   - $\rho(1) = \frac{3.2}{8} = 0.4$
   - $\rho(2) = \frac{-0.8}{8} = -0.1$

---

### Problem 1.2

Given the time series: $x = [5, 5, 5, 5, 5]$

Compute the autocovariance and autocorrelation. What happens when all values are identical?

**Solution 1.2**

1. **Sample Mean:**
   $$
   \bar{x} = \frac{5 + 5 + 5 + 5 + 5}{5} = 5
   $$

2. **Sample Variance:**
   $$
   s^2 = \frac{1}{4}\sum_{t=1}^{5}(5 - 5)^2 = \frac{1}{4}(0 + 0 + 0 + 0 + 0) = 0
   $$

3. **Autocovariance:**
   
   For lag $k = 0$:
   $$
   \gamma(0) = \frac{1}{5}\sum_{t=1}^{5}(5 - 5)^2 = 0
   $$
   
   For any lag $k > 0$:
   $$
   \gamma(k) = \frac{1}{n}\sum_{t=1}^{n-k}(5 - 5)(5 - 5) = 0
   $$

4. **Autocorrelation:**
   
   When $\gamma(0) = 0$ (zero variance), the autocorrelation $\rho(k) = \frac{\gamma(k)}{\gamma(0)}$ is **undefined** because we cannot divide by zero.
   
   **Interpretation:** A constant time series has no variability. The ACF cannot be computed because there is no variation to measure correlation against. In practice, such series are considered degenerate and ACF analysis is not meaningful.

---

### Problem 1.3

Given the time series: $x = [10, 8, 6, 4, 2]$

![Time Series Plot](figures/problem1_3_timeseries.png)

Compute the autocovariance $\gamma(k)$ and autocorrelation $\rho(k)$ for lags $k = 0, 1, 2$.

**Solution 1.3**

1. **Sample Mean:**
   $$
   \bar{x} = \frac{10 + 8 + 6 + 4 + 2}{5} = \frac{30}{5} = 6
   $$

2. **Sample Variance:**
   
   Deviations: $[4, 2, 0, -2, -4]$
   
   $$
   s^2 = \frac{4^2 + 2^2 + 0^2 + (-2)^2 + (-4)^2}{4} = \frac{16 + 4 + 0 + 4 + 16}{4} = 10
   $$

3. **Autocovariance:**
   
   For lag $k = 0$:
   $$
   \gamma(0) = \frac{1}{5}(16 + 4 + 0 + 4 + 16) = \frac{40}{5} = 8
   $$
   
   For lag $k = 1$:
   $$
   \gamma(1) = \frac{1}{5}[(4)(2) + (2)(0) + (0)(-2) + (-2)(-4)]
   $$
   $$
   = \frac{1}{5}[8 + 0 + 0 + 8] = \frac{16}{5} = 3.2
   $$
   
   For lag $k = 2$:
   $$
   \gamma(2) = \frac{1}{5}[(4)(0) + (2)(-2) + (0)(-4)]
   $$
   $$
   = \frac{1}{5}[0 - 4 + 0] = -\frac{4}{5} = -0.8
   $$

4. **Autocorrelation:**
   - $\rho(0) = 1.0$
   - $\rho(1) = \frac{3.2}{8} = 0.4$
   - $\rho(2) = \frac{-0.8}{8} = -0.1$

**Note:** This series has the same ACF as Problem 1.1 because both are linear trends with the same variance structure.

---

### Problem 1.4

Given the time series: $x = [3, 7, 3, 7, 3]$

![Time Series Plot](figures/problem1_4_timeseries.png)

Compute the autocovariance and autocorrelation for lags $k = 0, 1, 2, 3$.

**Solution 1.4**

1. **Sample Mean:**
   $$
   \bar{x} = \frac{3 + 7 + 3 + 7 + 3}{5} = \frac{23}{5} = 4.6
   $$

2. **Sample Variance:**
   
   Deviations: $[-1.6, 2.4, -1.6, 2.4, -1.6]$
   
   $$
   s^2 = \frac{(-1.6)^2 + 2.4^2 + (-1.6)^2 + 2.4^2 + (-1.6)^2}{4}
   $$
   $$
   = \frac{2.56 + 5.76 + 2.56 + 5.76 + 2.56}{4} = \frac{19.2}{4} = 4.8
   $$

3. **Autocovariance:**
   
   For lag $k = 0$:
   $$
   \gamma(0) = \frac{1}{5}(2.56 + 5.76 + 2.56 + 5.76 + 2.56) = \frac{19.2}{5} = 3.84
   $$
   
   For lag $k = 1$:
   $$
   \gamma(1) = \frac{1}{5}[(-1.6)(2.4) + (2.4)(-1.6) + (-1.6)(2.4) + (2.4)(-1.6)]
   $$
   $$
   = \frac{1}{5}[-3.84 - 3.84 - 3.84 - 3.84] = \frac{-15.36}{5} = -3.072
   $$
   
   For lag $k = 2$:
   $$
   \gamma(2) = \frac{1}{5}[(-1.6)(-1.6) + (2.4)(2.4) + (-1.6)(-1.6)]
   $$
   $$
   = \frac{1}{5}[2.56 + 5.76 + 2.56] = \frac{10.88}{5} = 2.176
   $$
   
   For lag $k = 3$:
   $$
   \gamma(3) = \frac{1}{5}[(-1.6)(2.4) + (2.4)(-1.6)]
   $$
   $$
   = \frac{1}{5}[-3.84 - 3.84] = \frac{-7.68}{5} = -1.536
   $$

4. **Autocorrelation:**
   - $\rho(0) = 1.0$
   - $\rho(1) = \frac{-3.072}{3.84} = -0.8$
   - $\rho(2) = \frac{2.176}{3.84} = 0.5667$
   - $\rho(3) = \frac{-1.536}{3.84} = -0.4$

**Interpretation:** The alternating pattern creates negative autocorrelation at odd lags and positive at even lags.

---

### Problem 1.5

Given the time series: $x = [12, 15, 18, 12, 15, 18, 12]$

![Time Series Plot](figures/problem1_5_timeseries.png)

Compute the autocovariance and autocorrelation for lags $k = 0, 1, 2, 3$.

**Solution 1.5**

1. **Sample Mean:**
   $$
   \bar{x} = \frac{12 + 15 + 18 + 12 + 15 + 18 + 12}{7} = \frac{102}{7} \approx 14.571
   $$

2. **Sample Variance:**
   
   Deviations: $[-2.571, 0.429, 3.429, -2.571, 0.429, 3.429, -2.571]$
   
   $$
   s^2 = \frac{(-2.571)^2 + 0.429^2 + 3.429^2 + (-2.571)^2 + 0.429^2 + 3.429^2 + (-2.571)^2}{6}
   $$
   $$
   = \frac{6.613 + 0.184 + 11.755 + 6.613 + 0.184 + 11.755 + 6.613}{6} = \frac{43.717}{6} \approx 7.286
   $$

3. **Autocovariance:**
   
   For lag $k = 0$:
   $$
   \gamma(0) = \frac{43.717}{7} \approx 6.245
   $$
   
   For lag $k = 1$:
   $$
   \gamma(1) = \frac{1}{7}[(-2.571)(0.429) + (0.429)(3.429) + (3.429)(-2.571) + (-2.571)(0.429) + (0.429)(3.429) + (3.429)(-2.571)]
   $$
   $$
   = \frac{1}{7}[-1.103 + 1.471 - 8.808 - 1.103 + 1.471 - 8.808] = \frac{-17.88}{7} \approx -2.554
   $$
   
   For lag $k = 2$:
   $$
   \gamma(2) = \frac{1}{7}[(-2.571)(3.429) + (0.429)(-2.571) + (3.429)(0.429) + (-2.571)(3.429) + (0.429)(-2.571) + (3.429)(0.429)]
   $$
   $$
   = \frac{1}{7}[-8.808 - 1.103 + 1.471 - 8.808 - 1.103 + 1.471] = \frac{-17.88}{7} \approx -2.554
   $$
   
   For lag $k = 3$:
   $$
   \gamma(3) = \frac{1}{7}[(-2.571)(-2.571) + (0.429)(0.429) + (3.429)(3.429) + (-2.571)(-2.571) + (0.429)(0.429) + (3.429)(3.429)]
   $$
   $$
   = \frac{1}{7}[6.613 + 0.184 + 11.755 + 6.613 + 0.184 + 11.755] = \frac{37.084}{7} \approx 5.298
   $$

4. **Autocorrelation:**
   - $\rho(0) = 1.0$
   - $\rho(1) = \frac{-2.554}{6.245} \approx -0.409$
   - $\rho(2) = \frac{-2.554}{6.245} \approx -0.409$
   - $\rho(3) = \frac{5.298}{6.245} \approx 0.848$

**Interpretation:** The period-3 pattern shows strong positive autocorrelation at lag 3 (the period length).

---

## Exercise Type 2: Effect of Mean Removal

### Problem 2.1

Given the time series: $x = [5, 7, 9, 11, 13]$

![Time Series Plot](figures/problem2_1_timeseries.png)

1. Compute the autocovariance **without** removing the mean.
2. Compute the autocovariance **with** mean removal.
3. Compare the results and explain why mean removal is necessary.

**Solution 2.1**

**Part 1: Without Mean Removal**

Using the formula: $\gamma(k) = \frac{1}{n}\sum_{t=1}^{n-k} x_t x_{t+k}$

Mean: $\bar{x} = 9$

For lag $k = 0$:
$$
\gamma(0) = \frac{1}{5}(5^2 + 7^2 + 9^2 + 11^2 + 13^2) = \frac{25 + 49 + 81 + 121 + 169}{5} = \frac{445}{5} = 89
$$

For lag $k = 1$:
$$
\gamma(1) = \frac{1}{5}(5 \times 7 + 7 \times 9 + 9 \times 11 + 11 \times 13)
$$
$$
= \frac{1}{5}(35 + 63 + 99 + 143) = \frac{340}{5} = 68
$$

**Part 2: With Mean Removal**

Deviations: $[-4, -2, 0, 2, 4]$

For lag $k = 0$:
$$
\gamma(0) = \frac{1}{5}[(-4)^2 + (-2)^2 + 0^2 + 2^2 + 4^2] = \frac{40}{5} = 8
$$

For lag $k = 1$:
$$
\gamma(1) = \frac{1}{5}[(-4)(-2) + (-2)(0) + (0)(2) + (2)(4)]
$$
$$
= \frac{1}{5}[8 + 0 + 0 + 8] = \frac{16}{5} = 3.2
$$

**Part 3: Comparison and Explanation**

- **Without mean removal:** $\gamma(0) = 89$, $\gamma(1) = 68$, $\rho(1) = 68/89 = 0.764$
- **With mean removal:** $\gamma(0) = 8$, $\gamma(1) = 3.2$, $\rho(1) = 3.2/8 = 0.4$

**Why mean removal is necessary:**

When we don't remove the mean, the autocovariance captures both:
1. The true correlation structure of the deviations
2. The spurious correlation introduced by the non-zero mean

The large mean (9) dominates the calculation, making the series appear more correlated than it actually is. Mean removal isolates the true correlation structure by focusing only on deviations from the mean, which is what autocorrelation should measure.

---

### Problem 2.2

Given the time series: $x = [100, 102, 104, 106, 108]$

1. Compute autocorrelation at lag 1 **without** mean removal.
2. Compute autocorrelation at lag 1 **with** mean removal.
3. Explain the difference.

**Solution 2.2**

**Part 1: Without Mean Removal**

Mean: $\bar{x} = 104$

Using raw values:
$$
\gamma(0) = \frac{1}{5}(100^2 + 102^2 + 104^2 + 106^2 + 108^2)
$$
$$
= \frac{1}{5}(10000 + 10404 + 10816 + 11236 + 11664) = \frac{54120}{5} = 10824
$$

$$
\gamma(1) = \frac{1}{5}(100 \times 102 + 102 \times 104 + 104 \times 106 + 106 \times 108)
$$
$$
= \frac{1}{5}(10200 + 10608 + 11024 + 11448) = \frac{43280}{5} = 8656
$$

$$
\rho(1) = \frac{8656}{10824} \approx 0.799
$$

**Part 2: With Mean Removal**

Deviations: $[-4, -2, 0, 2, 4]$

$$
\gamma(0) = \frac{1}{5}[(-4)^2 + (-2)^2 + 0^2 + 2^2 + 4^2] = \frac{40}{5} = 8
$$

$$
\gamma(1) = \frac{1}{5}[(-4)(-2) + (-2)(0) + (0)(2) + (2)(4)]
$$
$$
= \frac{1}{5}[8 + 0 + 0 + 8] = \frac{16}{5} = 3.2
$$

$$
\rho(1) = \frac{3.2}{8} = 0.4
$$

**Part 3: Explanation**

The autocorrelation without mean removal (0.799) is much higher than with mean removal (0.4). This is because:

1. **Spurious correlation:** The large mean value (104) creates artificial correlation. When both $x_t$ and $x_{t+1}$ are large positive numbers, their product is large, even if their deviations from the mean are only weakly correlated.

2. **True correlation:** After mean removal, we see the actual correlation between deviations is only 0.4, which reflects the linear trend in the data.

3. **Mathematical reason:** Without mean removal, $\gamma(1) = E[x_t x_{t+1}]$ includes the mean squared term, which inflates the correlation. With mean removal, $\gamma(1) = E[(x_t - \mu)(x_{t+1} - \mu)]$ measures only the correlation of deviations.

---

### Problem 2.3

Given the time series: $x = [20, 20, 20, 25, 25, 25]$

![Time Series Plot](figures/problem2_3_timeseries.png)

Compare the autocorrelation at lag 1 computed with and without mean removal. What does this tell you about the series?

**Solution 2.3**

**Part 1: Without Mean Removal**

Mean: $\bar{x} = \frac{20 + 20 + 20 + 25 + 25 + 25}{6} = \frac{135}{6} = 22.5$

$$
\gamma(0) = \frac{1}{6}(20^2 + 20^2 + 20^2 + 25^2 + 25^2 + 25^2)
$$
$$
= \frac{1}{6}(400 + 400 + 400 + 625 + 625 + 625) = \frac{3075}{6} = 512.5
$$

$$
\gamma(1) = \frac{1}{6}(20 \times 20 + 20 \times 20 + 20 \times 25 + 25 \times 25 + 25 \times 25)
$$
$$
= \frac{1}{6}(400 + 400 + 500 + 625 + 625) = \frac{2550}{6} = 425
$$

$$
\rho(1) = \frac{425}{512.5} \approx 0.829
$$

**Part 2: With Mean Removal**

Deviations: $[-2.5, -2.5, -2.5, 2.5, 2.5, 2.5]$

$$
\gamma(0) = \frac{1}{6}[(-2.5)^2 + (-2.5)^2 + (-2.5)^2 + 2.5^2 + 2.5^2 + 2.5^2]
$$
$$
= \frac{1}{6}(6.25 + 6.25 + 6.25 + 6.25 + 6.25 + 6.25) = \frac{37.5}{6} = 6.25
$$

$$
\gamma(1) = \frac{1}{6}[(-2.5)(-2.5) + (-2.5)(-2.5) + (-2.5)(2.5) + (2.5)(2.5) + (2.5)(2.5)]
$$
$$
= \frac{1}{6}[6.25 + 6.25 - 6.25 + 6.25 + 6.25] = \frac{18.75}{6} = 3.125
$$

$$
\rho(1) = \frac{3.125}{6.25} = 0.5
$$

**Interpretation:**

- **Without mean removal:** $\rho(1) = 0.829$ (highly correlated)
- **With mean removal:** $\rho(1) = 0.5$ (moderately correlated)

The series has a step change at position 4. Without mean removal, the autocorrelation is inflated because values in the first half (20) are consistently different from values in the second half (25). After mean removal, we see that the correlation is actually 0.5, which reflects the step structure: values within each block are perfectly correlated, but the transition creates lower correlation.

---

### Problem 2.4

Given the time series: $x = [1, 3, 5, 1, 3, 5]$

Compute autocorrelation at lag 2 with and without mean removal. Explain why the results differ.

**Solution 2.4**

**Part 1: Without Mean Removal**

Mean: $\bar{x} = \frac{1 + 3 + 5 + 1 + 3 + 5}{6} = \frac{18}{6} = 3$

$$
\gamma(0) = \frac{1}{6}(1^2 + 3^2 + 5^2 + 1^2 + 3^2 + 5^2)
$$
$$
= \frac{1}{6}(1 + 9 + 25 + 1 + 9 + 25) = \frac{70}{6} \approx 11.667
$$

$$
\gamma(2) = \frac{1}{6}(1 \times 5 + 3 \times 1 + 5 \times 3 + 1 \times 5)
$$
$$
= \frac{1}{6}(5 + 3 + 15 + 5) = \frac{28}{6} \approx 4.667
$$

$$
\rho(2) = \frac{4.667}{11.667} \approx 0.4
$$

**Part 2: With Mean Removal**

Deviations: $[-2, 0, 2, -2, 0, 2]$

$$
\gamma(0) = \frac{1}{6}[(-2)^2 + 0^2 + 2^2 + (-2)^2 + 0^2 + 2^2]
$$
$$
= \frac{1}{6}(4 + 0 + 4 + 4 + 0 + 4) = \frac{16}{6} \approx 2.667
$$

$$
\gamma(2) = \frac{1}{6}[(-2)(2) + (0)(-2) + (2)(0) + (-2)(2)]
$$
$$
= \frac{1}{6}[-4 + 0 + 0 - 4] = \frac{-8}{6} \approx -1.333
$$

$$
\rho(2) = \frac{-1.333}{2.667} = -0.5
$$

**Explanation:**

The results differ significantly:
- **Without mean removal:** $\rho(2) = 0.4$ (positive)
- **With mean removal:** $\rho(2) = -0.5$ (negative)

**Why they differ:**

1. **Without mean removal:** The calculation $E[x_t x_{t+2}]$ includes the mean effect. Since the mean is 3, and most products involve values around 3, we get a positive correlation.

2. **With mean removal:** The true pattern emerges. The series has period 3, so at lag 2, we're comparing positions that are out of phase (e.g., position 1 with position 3: -2 vs 2). This creates negative correlation.

3. **Key insight:** Mean removal reveals the true correlation structure. Without it, the mean dominates and masks the underlying pattern.

---

### Problem 2.5

Given the time series: $x = [10, 12, 14, 10, 12, 14, 10]$

![Time Series Plot](figures/problem2_5_timeseries.png)

1. Compute autocorrelation at lag 3 with and without mean removal.
2. Explain which method gives the correct interpretation of the series' periodic structure.

**Solution 2.5**

**Part 1: Without Mean Removal**

Mean: $\bar{x} = \frac{10 + 12 + 14 + 10 + 12 + 14 + 10}{7} = \frac{82}{7} \approx 11.714$

$$
\gamma(0) = \frac{1}{7}(10^2 + 12^2 + 14^2 + 10^2 + 12^2 + 14^2 + 10^2)
$$
$$
= \frac{1}{7}(100 + 144 + 196 + 100 + 144 + 196 + 100) = \frac{980}{7} = 140
$$

$$
\gamma(3) = \frac{1}{7}(10 \times 10 + 12 \times 12 + 14 \times 14 + 10 \times 10)
$$
$$
= \frac{1}{7}(100 + 144 + 196 + 100) = \frac{540}{7} \approx 77.143
$$

$$
\rho(3) = \frac{77.143}{140} \approx 0.551
$$

**Part 2: With Mean Removal**

Deviations: $[-1.714, 0.286, 2.286, -1.714, 0.286, 2.286, -1.714]$

$$
\gamma(0) = \frac{1}{7}[(-1.714)^2 + 0.286^2 + 2.286^2 + (-1.714)^2 + 0.286^2 + 2.286^2 + (-1.714)^2]
$$
$$
= \frac{1}{7}(2.938 + 0.082 + 5.226 + 2.938 + 0.082 + 5.226 + 2.938) = \frac{19.45}{7} \approx 2.779
$$

$$
\gamma(3) = \frac{1}{7}[(-1.714)(-1.714) + (0.286)(0.286) + (2.286)(2.286) + (-1.714)(-1.714)]
$$
$$
= \frac{1}{7}(2.938 + 0.082 + 5.226 + 2.938) = \frac{14.184}{7} \approx 2.026
$$

$$
\rho(3) = \frac{2.026}{2.779} \approx 0.729
$$

**Part 3: Interpretation**

- **Without mean removal:** $\rho(3) = 0.551$
- **With mean removal:** $\rho(3) = 0.729$

**Which is correct?**

The method **with mean removal** gives the correct interpretation because:

1. **Periodic structure:** The series has period 3. At lag 3, we should see strong positive correlation since we're comparing values at the same phase of the cycle (e.g., position 1 with position 4, both are 10).

2. **Mean removal reveals true correlation:** The autocorrelation of 0.729 correctly identifies the strong periodic pattern. Without mean removal, the correlation is diluted by the mean effect.

3. **Statistical principle:** Autocorrelation should measure the correlation of deviations from the mean, not the correlation of raw values. This is the standard definition in time series analysis.

---

## Exercise Type 3: Interpreting ACF Patterns

### Problem 3.1

A time series has an ACF plot where $\rho(0) = 1$ and $\rho(k) \approx 0$ for all $k > 0$, with values randomly scattered around zero within the confidence bands.

![Time Series Plot](figures/problem3_1_timeseries.png)

1. What type of process does this indicate?
2. What are the characteristics of such a process?
3. Generate a synthetic time series with this ACF pattern and plot both the series and its ACF.

**Solution 3.1**

1. **Process Type:** This indicates a **white noise** process.

2. **Characteristics:**
   - No serial correlation (uncorrelated observations)
   - Constant mean and variance (stationary)
   - No predictable pattern
   - Each observation is independent of previous observations
   - Used as a baseline for model diagnostics (residuals should be white noise)

3. **Python Code:**

```python
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import acf
from statsmodels.graphics.tsaplots import plot_acf

# Set random seed for reproducibility
np.random.seed(42)

# Generate white noise time series
n = 200
white_noise = np.random.normal(loc=0, scale=1, size=n)

# Create time index
time = np.arange(n)

# Plot the time series
plt.figure(figsize=(14, 5))

plt.subplot(1, 2, 1)
plt.plot(time, white_noise, linewidth=0.8, color='steelblue')
plt.title('White Noise Time Series', fontsize=14, fontweight='bold')
plt.xlabel('Time', fontsize=12)
plt.ylabel('Value', fontsize=12)
plt.grid(True, alpha=0.3)

# Compute and plot ACF
plt.subplot(1, 2, 2)
plot_acf(white_noise, lags=40, alpha=0.05, ax=plt.gca())
plt.title('ACF Plot: White Noise', fontsize=14, fontweight='bold')
plt.xlabel('Lag', fontsize=12)
plt.ylabel('Autocorrelation', fontsize=12)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Print ACF values for first few lags
acf_values = acf(white_noise, nlags=10, fft=False)
print("ACF values for lags 0-10:")
for k in range(11):
    print(f"  ρ({k}) = {acf_values[k]:.4f}")
```

**Expected Output:**
- Time series: Random fluctuations around zero
- ACF: All lags (except 0) near zero, within confidence bands
- ACF values: $\rho(0) = 1.0$, $\rho(k) \approx 0$ for $k > 0$

---

### Problem 3.2

A time series has an ACF plot showing $\rho(k)$ that decays very slowly, remaining positive and significant even at large lags (e.g., $\rho(20) > 0.5$).

![Time Series Plot](figures/problem3_2_timeseries.png)

1. What does this pattern indicate?
2. What type of non-stationarity is likely present?
3. Generate a synthetic time series with this ACF pattern and plot both the series and its ACF.

**Solution 3.2**

1. **Pattern Indication:** This indicates a **trend** or **non-stationary** process. The slow decay suggests that the series has a long memory, typically due to a deterministic or stochastic trend.

2. **Non-stationarity Type:**
   - **Deterministic trend:** Linear or polynomial trend in the mean
   - **Random walk:** Stochastic trend where the mean changes over time
   - **Unit root process:** The series is integrated of order 1 (I(1))

3. **Python Code:**

```python
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import acf
from statsmodels.graphics.tsaplots import plot_acf

# Set random seed for reproducibility
np.random.seed(42)

# Generate time series with trend
n = 200
time = np.arange(n)

# Option 1: Deterministic linear trend + noise
trend = 0.05 * time
noise = np.random.normal(0, 1, n)
trend_series = trend + noise

# Option 2: Random walk (stochastic trend)
random_walk = np.cumsum(np.random.normal(0, 1, n))

# Plot both series
plt.figure(figsize=(16, 10))

# Deterministic trend
plt.subplot(2, 2, 1)
plt.plot(time, trend_series, linewidth=1, color='steelblue')
plt.title('Time Series with Deterministic Trend', fontsize=14, fontweight='bold')
plt.xlabel('Time', fontsize=12)
plt.ylabel('Value', fontsize=12)
plt.grid(True, alpha=0.3)

plt.subplot(2, 2, 2)
plot_acf(trend_series, lags=40, alpha=0.05, ax=plt.gca())
plt.title('ACF: Deterministic Trend', fontsize=14, fontweight='bold')
plt.xlabel('Lag', fontsize=12)
plt.ylabel('Autocorrelation', fontsize=12)
plt.grid(True, alpha=0.3)

# Random walk
plt.subplot(2, 2, 3)
plt.plot(time, random_walk, linewidth=1, color='crimson')
plt.title('Random Walk (Stochastic Trend)', fontsize=14, fontweight='bold')
plt.xlabel('Time', fontsize=12)
plt.ylabel('Value', fontsize=12)
plt.grid(True, alpha=0.3)

plt.subplot(2, 2, 4)
plot_acf(random_walk, lags=40, alpha=0.05, ax=plt.gca())
plt.title('ACF: Random Walk', fontsize=14, fontweight='bold')
plt.xlabel('Lag', fontsize=12)
plt.ylabel('Autocorrelation', fontsize=12)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Print ACF values for random walk
acf_values = acf(random_walk, nlags=20, fft=False)
print("ACF values for Random Walk (lags 0-20):")
for k in range(0, 21, 5):
    print(f"  ρ({k}) = {acf_values[k]:.4f}")
```

**Expected Output:**
- Time series: Clear upward (or downward) trend
- ACF: Slow decay, remains positive and significant at large lags
- Interpretation: Non-stationary process requiring differencing

---

### Problem 3.3

A time series has an ACF plot showing oscillatory (sinusoidal) behavior, with autocorrelations alternating between positive and negative values in a periodic pattern.

![Time Series Plot](figures/problem3_3_timeseries.png)

1. What does this pattern indicate?
2. What type of seasonality or cyclical behavior is present?
3. Generate a synthetic time series with this ACF pattern and plot both the series and its ACF.

**Solution 3.3**

1. **Pattern Indication:** This indicates **seasonality** or **cyclical behavior**. The oscillatory ACF suggests a periodic component in the time series.

2. **Seasonality Type:**
   - **Deterministic seasonality:** Fixed periodic pattern (e.g., monthly, quarterly)
   - **Cyclical component:** Longer-term business or economic cycles
   - **Sinusoidal pattern:** Regular oscillations with a specific frequency

3. **Python Code:**

```python
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import acf
from statsmodels.graphics.tsaplots import plot_acf

# Set random seed for reproducibility
np.random.seed(42)

# Generate time series with seasonality
n = 200
time = np.arange(n)

# Create seasonal component (period = 12, like monthly data)
seasonal_period = 12
seasonal_component = 5 * np.sin(2 * np.pi * time / seasonal_period)

# Add trend and noise
trend = 0.02 * time
noise = np.random.normal(0, 0.5, n)
seasonal_series = trend + seasonal_component + noise

# Plot the time series and ACF
plt.figure(figsize=(16, 5))

plt.subplot(1, 2, 1)
plt.plot(time, seasonal_series, linewidth=1, color='steelblue')
plt.title('Time Series with Seasonality (Period = 12)', fontsize=14, fontweight='bold')
plt.xlabel('Time', fontsize=12)
plt.ylabel('Value', fontsize=12)
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
plot_acf(seasonal_series, lags=50, alpha=0.05, ax=plt.gca())
plt.title('ACF Plot: Seasonal Pattern', fontsize=14, fontweight='bold')
plt.xlabel('Lag', fontsize=12)
plt.ylabel('Autocorrelation', fontsize=12)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Print ACF values at seasonal lags
acf_values = acf(seasonal_series, nlags=50, fft=False)
print("ACF values at seasonal lags:")
for k in [0, 12, 24, 36, 48]:
    if k < len(acf_values):
        print(f"  ρ({k}) = {acf_values[k]:.4f}")
```

**Expected Output:**
- Time series: Clear periodic pattern repeating every 12 time points
- ACF: Oscillatory pattern with peaks at lags 12, 24, 36, etc.
- Interpretation: Strong seasonal component with period 12

---

### Problem 3.4

A time series has an ACF plot where $\rho(k)$ shows a sharp cutoff after lag $q = 2$, with $\rho(1)$ and $\rho(2)$ being significant, but $\rho(k) \approx 0$ for all $k > 2$.

![Time Series Plot](figures/problem3_4_timeseries.png)

1. What type of process does this suggest?
2. What is the likely model order?
3. Generate a synthetic time series with this ACF pattern and plot both the series and its ACF.

**Solution 3.4**

1. **Process Type:** This suggests a **Moving Average (MA) process of order q**, specifically **MA(2)**. The sharp cutoff is characteristic of MA processes.

2. **Model Order:** The model is likely **MA(2)**, meaning:
   $$
   x_t = \mu + \epsilon_t + \theta_1 \epsilon_{t-1} + \theta_2 \epsilon_{t-2}
   $$
   where $\epsilon_t$ is white noise.

3. **Python Code:**

```python
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import acf
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.arima_process import ArmaProcess

# Set random seed for reproducibility
np.random.seed(42)

# Generate MA(2) process
# MA(2): x_t = ε_t + 0.5*ε_{t-1} + 0.3*ε_{t-2}
# This corresponds to AR polynomial = 1, MA polynomial = [1, 0.5, 0.3]
ma_coeffs = np.array([1, 0.5, 0.3])  # [1, θ1, θ2]
ar_coeffs = np.array([1])  # AR part is just 1 (no AR terms)

# Create ARMA process (AR=0, MA=2)
arma_process = ArmaProcess(ar_coeffs, ma_coeffs)
ma2_series = arma_process.generate_sample(nsample=200)

# Plot the time series and ACF
plt.figure(figsize=(16, 5))

plt.subplot(1, 2, 1)
plt.plot(ma2_series, linewidth=1, color='steelblue')
plt.title('MA(2) Time Series', fontsize=14, fontweight='bold')
plt.xlabel('Time', fontsize=12)
plt.ylabel('Value', fontsize=12)
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
plot_acf(ma2_series, lags=20, alpha=0.05, ax=plt.gca())
plt.title('ACF Plot: MA(2) Process', fontsize=14, fontweight='bold')
plt.xlabel('Lag', fontsize=12)
plt.ylabel('Autocorrelation', fontsize=12)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Print ACF values
acf_values = acf(ma2_series, nlags=10, fft=False)
print("ACF values for MA(2) process (lags 0-10):")
for k in range(11):
    print(f"  ρ({k}) = {acf_values[k]:.4f}")
print("\nNote: ACF should show significant values only at lags 0, 1, 2")
```

**Expected Output:**
- Time series: Stationary series with short memory
- ACF: Sharp cutoff after lag 2, with $\rho(1)$ and $\rho(2)$ significant, $\rho(k) \approx 0$ for $k > 2$
- Interpretation: MA(2) process - memory extends only 2 periods back

---

### Problem 3.5

A time series has an ACF plot showing exponential decay: $\rho(k)$ starts high and decays gradually, remaining positive but decreasing, with no sharp cutoff.

![Time Series Plot](figures/problem3_5_timeseries.png)

1. What type of process does this indicate?
2. How does this differ from the MA process pattern?
3. Generate a synthetic time series with this ACF pattern and plot both the series and its ACF.

**Solution 3.5**

1. **Process Type:** This indicates an **Autoregressive (AR) process**. The exponential decay is characteristic of AR processes, where the autocorrelation decays gradually rather than cutting off sharply.

2. **Difference from MA:**
   - **AR process:** ACF decays exponentially (gradual decline)
   - **MA process:** ACF cuts off sharply after lag q
   - **AR:** Long memory (past values influence future values indirectly)
   - **MA:** Short memory (only recent shocks matter)

3. **Python Code:**

```python
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import acf
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.arima_process import ArmaProcess

# Set random seed for reproducibility
np.random.seed(42)

# Generate AR(1) process
# AR(1): x_t = 0.7*x_{t-1} + ε_t
# This corresponds to AR polynomial = [1, -0.7], MA polynomial = [1]
ar_coeffs = np.array([1, -0.7])  # [1, -φ1] for AR(1)
ma_coeffs = np.array([1])  # MA part is just 1 (no MA terms)

# Create ARMA process (AR=1, MA=0)
arma_process = ArmaProcess(ar_coeffs, ma_coeffs)
ar1_series = arma_process.generate_sample(nsample=200)

# Plot the time series and ACF
plt.figure(figsize=(16, 5))

plt.subplot(1, 2, 1)
plt.plot(ar1_series, linewidth=1, color='steelblue')
plt.title('AR(1) Time Series (φ = 0.7)', fontsize=14, fontweight='bold')
plt.xlabel('Time', fontsize=12)
plt.ylabel('Value', fontsize=12)
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
plot_acf(ar1_series, lags=20, alpha=0.05, ax=plt.gca())
plt.title('ACF Plot: AR(1) Process (Exponential Decay)', fontsize=14, fontweight='bold')
plt.xlabel('Lag', fontsize=12)
plt.ylabel('Autocorrelation', fontsize=12)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Print ACF values
acf_values = acf(ar1_series, nlags=10, fft=False)
print("ACF values for AR(1) process (lags 0-10):")
for k in range(11):
    print(f"  ρ({k}) = {acf_values[k]:.4f}")
print("\nNote: ACF decays exponentially: ρ(k) ≈ φ^k = 0.7^k")
print("Theoretical values:")
for k in range(11):
    theoretical = 0.7**k
    print(f"  Theoretical ρ({k}) = {theoretical:.4f}")
```

**Expected Output:**
- Time series: Stationary series with smooth variations
- ACF: Exponential decay, $\rho(k) \approx \phi^k$ where $\phi$ is the AR coefficient
- Interpretation: AR(1) process - each value depends on the previous value, creating gradual memory decay

---

## Exercise Type 4: Physiological Time-Series Interpretation

### Problem 4.1

Consider a heart rate time series where the ACF shows:
- Strong positive autocorrelation at lag 1 ($\rho(1) \approx 0.8$)
- Rapid decay to near zero by lag 5
- No significant periodic patterns

![Time Series Plot](figures/problem4_1_timeseries.png)

1. What does this tell you about the memory length of the process?
2. What AR/MA/ARIMA model order would be appropriate?
3. Would deep learning be necessary for forecasting?
4. Generate a synthetic heart rate time series with these characteristics and plot the series and ACF.

**Solution 4.1**

1. **Memory Length:** The process has **short memory** (approximately 5 time steps). The rapid decay indicates that heart rate values are only correlated with recent past values, not distant ones.

2. **Model Order:**
   - **AR(1) or AR(2):** The exponential decay suggests an autoregressive process
   - **ARIMA(1,0,0) or ARIMA(2,0,0):** Since the series appears stationary (no differencing needed)
   - The high $\rho(1)$ suggests AR(1) might be sufficient

3. **Deep Learning Necessity:** **No, deep learning is not necessary.** Traditional AR/ARIMA models would be sufficient because:
   - The process has short memory
   - The ACF pattern is simple (exponential decay)
   - No complex nonlinear patterns are evident
   - AR models are interpretable and computationally efficient

4. **Python Code:**

```python
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import acf
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.arima_process import ArmaProcess

# Set random seed for reproducibility
np.random.seed(42)

# Generate AR(1) process to simulate heart rate
# AR(1): x_t = μ + φ*(x_{t-1} - μ) + ε_t
# Use φ = 0.8 to match the ACF requirement
ar_coeffs = np.array([1, -0.8])  # AR(1) with φ = 0.8
ma_coeffs = np.array([1])

arma_process = ArmaProcess(ar_coeffs, ma_coeffs)
heart_rate_base = arma_process.generate_sample(nsample=300)

# Scale to realistic heart rate values (60-100 bpm)
heart_rate_mean = 75
heart_rate_std = 8
heart_rate = heart_rate_mean + heart_rate_std * heart_rate_base

# Plot the time series and ACF
plt.figure(figsize=(16, 5))

plt.subplot(1, 2, 1)
time = np.arange(len(heart_rate))
plt.plot(time, heart_rate, linewidth=1, color='crimson')
plt.title('Synthetic Heart Rate Time Series', fontsize=14, fontweight='bold')
plt.xlabel('Time (seconds)', fontsize=12)
plt.ylabel('Heart Rate (bpm)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.axhline(y=heart_rate_mean, color='gray', linestyle='--', alpha=0.5, label=f'Mean = {heart_rate_mean} bpm')
plt.legend()

plt.subplot(1, 2, 2)
plot_acf(heart_rate, lags=20, alpha=0.05, ax=plt.gca())
plt.title('ACF Plot: Heart Rate', fontsize=14, fontweight='bold')
plt.xlabel('Lag', fontsize=12)
plt.ylabel('Autocorrelation', fontsize=12)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Print ACF values
acf_values = acf(heart_rate, nlags=10, fft=False)
print("ACF values for heart rate (lags 0-10):")
for k in range(11):
    print(f"  ρ({k}) = {acf_values[k]:.4f}")
print(f"\nMemory length: ~5 time steps (where ACF decays to near zero)")
```

**Expected Output:**
- Time series: Smooth variations around mean heart rate
- ACF: Strong $\rho(1) \approx 0.8$, rapid decay to near zero by lag 5
- Model recommendation: AR(1) or ARIMA(1,0,0)

---

### Problem 4.2

Consider a blood pressure time series where the ACF shows:
- Very slow decay, remaining above 0.5 even at lag 20
- No clear periodic pattern
- Gradual decrease rather than sharp cutoff

![Time Series Plot](figures/problem4_2_timeseries.png)

1. What does this indicate about the process?
2. What preprocessing step might be necessary?
3. What model would be appropriate after preprocessing?
4. Generate a synthetic blood pressure time series and plot the series and ACF.

**Solution 4.2**

1. **Process Indication:** This indicates a **non-stationary process**, likely a **random walk** or **unit root process**. The slow decay suggests the mean is changing over time.

2. **Preprocessing:** **First-order differencing** is necessary:
   - Compute $\Delta x_t = x_t - x_{t-1}$
   - This removes the trend and makes the series stationary
   - The differenced series should show faster ACF decay

3. **Model After Preprocessing:**
   - After differencing, the series becomes stationary
   - The differenced series might follow AR(1) or ARIMA(1,0,0)
   - Original series: **ARIMA(1,1,0)** (AR(1) with first-order differencing)

4. **Python Code:**

```python
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import acf
from statsmodels.graphics.tsaplots import plot_acf

# Set random seed for reproducibility
np.random.seed(42)

# Generate random walk to simulate non-stationary blood pressure
n = 300
# Random walk: x_t = x_{t-1} + ε_t
shocks = np.random.normal(0, 2, n)
blood_pressure = np.cumsum(shocks) + 120  # Start at 120 mmHg

# Compute first difference
blood_pressure_diff = np.diff(blood_pressure)

# Plot original series, differenced series, and ACFs
plt.figure(figsize=(16, 10))

# Original series
plt.subplot(2, 2, 1)
time = np.arange(n)
plt.plot(time, blood_pressure, linewidth=1, color='crimson')
plt.title('Blood Pressure Time Series (Non-Stationary)', fontsize=14, fontweight='bold')
plt.xlabel('Time (minutes)', fontsize=12)
plt.ylabel('Blood Pressure (mmHg)', fontsize=12)
plt.grid(True, alpha=0.3)

plt.subplot(2, 2, 2)
plot_acf(blood_pressure, lags=30, alpha=0.05, ax=plt.gca())
plt.title('ACF: Original Series (Slow Decay)', fontsize=14, fontweight='bold')
plt.xlabel('Lag', fontsize=12)
plt.ylabel('Autocorrelation', fontsize=12)
plt.grid(True, alpha=0.3)

# Differenced series
plt.subplot(2, 2, 3)
time_diff = np.arange(len(blood_pressure_diff))
plt.plot(time_diff, blood_pressure_diff, linewidth=1, color='steelblue')
plt.title('First-Differenced Blood Pressure (Stationary)', fontsize=14, fontweight='bold')
plt.xlabel('Time (minutes)', fontsize=12)
plt.ylabel('Δ Blood Pressure', fontsize=12)
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='gray', linestyle='--', alpha=0.5)

plt.subplot(2, 2, 4)
plot_acf(blood_pressure_diff, lags=20, alpha=0.05, ax=plt.gca())
plt.title('ACF: Differenced Series (Fast Decay)', fontsize=14, fontweight='bold')
plt.xlabel('Lag', fontsize=12)
plt.ylabel('Autocorrelation', fontsize=12)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Print ACF values
print("ACF values for original series (lags 0, 5, 10, 15, 20):")
acf_original = acf(blood_pressure, nlags=20, fft=False)
for k in [0, 5, 10, 15, 20]:
    print(f"  ρ({k}) = {acf_original[k]:.4f}")

print("\nACF values for differenced series (lags 0-10):")
acf_diff = acf(blood_pressure_diff, nlags=10, fft=False)
for k in range(11):
    print(f"  ρ({k}) = {acf_diff[k]:.4f}")
print("\nNote: Differencing removes the trend and makes ACF decay rapidly")
```

**Expected Output:**
- Original series: Non-stationary with trend
- Original ACF: Slow decay, remains high at large lags
- Differenced series: Stationary, mean-reverting
- Differenced ACF: Fast decay, suitable for AR modeling
- Model: ARIMA(1,1,0) for original series

---

### Problem 4.3

Consider an EEG-like signal where the ACF shows:
- Oscillatory pattern with period approximately 10 time steps
- Significant autocorrelation at lags 10, 20, 30
- Decay in amplitude of oscillations over time

![Time Series Plot](figures/problem4_3_timeseries.png)

1. What does this indicate about the signal?
2. What type of seasonality is present?
3. Would a seasonal ARIMA model be appropriate?
4. Generate a synthetic EEG-like signal and plot the series and ACF.

**Solution 4.3**

1. **Signal Indication:** The signal has a **strong periodic/seasonal component** with period 10. This suggests rhythmic brain activity, possibly alpha waves (8-13 Hz) or another oscillatory neural pattern.

2. **Seasonality Type:** **Deterministic seasonality** with period 10. The repeating pattern at regular intervals indicates a consistent oscillatory component.

3. **Seasonal ARIMA:** Yes, a **SARIMA model** would be appropriate:
   - **SARIMA(p,d,q)(P,D,Q)s** where $s = 10$ (seasonal period)
   - Example: SARIMA(1,0,1)(1,0,1)₁₀
   - This captures both the short-term AR/MA structure and the seasonal pattern

4. **Python Code:**

```python
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import acf
from statsmodels.graphics.tsaplots import plot_acf

# Set random seed for reproducibility
np.random.seed(42)

# Generate EEG-like signal with oscillatory component
n = 400
time = np.arange(n)

# Create oscillatory component (period = 10, like alpha waves)
period = 10
oscillatory = 3 * np.sin(2 * np.pi * time / period)

# Add slower trend and noise
trend = 0.01 * time
noise = np.random.normal(0, 0.5, n)
eeg_signal = trend + oscillatory + noise

# Plot the time series and ACF
plt.figure(figsize=(16, 5))

plt.subplot(1, 2, 1)
plt.plot(time, eeg_signal, linewidth=0.8, color='steelblue')
plt.title('Synthetic EEG-like Signal (Oscillatory Pattern)', fontsize=14, fontweight='bold')
plt.xlabel('Time (samples)', fontsize=12)
plt.ylabel('Amplitude (μV)', fontsize=12)
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
plot_acf(eeg_signal, lags=50, alpha=0.05, ax=plt.gca())
plt.title('ACF Plot: EEG Signal (Periodic Pattern)', fontsize=14, fontweight='bold')
plt.xlabel('Lag', fontsize=12)
plt.ylabel('Autocorrelation', fontsize=12)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Print ACF values at seasonal lags
acf_values = acf(eeg_signal, nlags=50, fft=False)
print("ACF values at seasonal lags (period = 10):")
for k in [0, 10, 20, 30, 40, 50]:
    if k < len(acf_values):
        print(f"  ρ({k}) = {acf_values[k]:.4f}")
print("\nNote: Significant autocorrelation at multiples of period 10")
```

**Expected Output:**
- Time series: Clear oscillatory pattern with period 10
- ACF: Peaks at lags 10, 20, 30, with oscillatory decay
- Model recommendation: SARIMA(1,0,1)(1,0,1)₁₀

---

### Problem 4.4

Consider a respiratory rate time series where the ACF shows:
- Sharp cutoff after lag 2
- $\rho(1) \approx 0.6$, $\rho(2) \approx 0.3$
- $\rho(k) \approx 0$ for $k > 2$

![Time Series Plot](figures/problem4_4_timeseries.png)

1. What type of process does this indicate?
2. What is the memory length?
3. What model order would be appropriate?
4. Generate a synthetic respiratory rate time series and plot the series and ACF.

**Solution 4.4**

1. **Process Type:** This indicates a **Moving Average (MA) process of order 2**, specifically **MA(2)**. The sharp cutoff is the hallmark of MA processes.

2. **Memory Length:** The memory extends only **2 time steps**. Beyond lag 2, there is no significant autocorrelation.

3. **Model Order:** **MA(2) or ARIMA(0,0,2)** would be appropriate:
   $$
   x_t = \mu + \epsilon_t + \theta_1 \epsilon_{t-1} + \theta_2 \epsilon_{t-2}
   $$

4. **Python Code:**

```python
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import acf
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.arima_process import ArmaProcess

# Set random seed for reproducibility
np.random.seed(42)

# Generate MA(2) process to simulate respiratory rate
# MA(2): x_t = ε_t + θ1*ε_{t-1} + θ2*ε_{t-2}
# Choose coefficients to match ACF: ρ(1) ≈ 0.6, ρ(2) ≈ 0.3
# For MA(2), we need to solve for θ1 and θ2
# Using approximate values: θ1 = 0.5, θ2 = 0.3
ma_coeffs = np.array([1, 0.5, 0.3])  # [1, θ1, θ2]
ar_coeffs = np.array([1])  # No AR terms

arma_process = ArmaProcess(ar_coeffs, ma_coeffs)
respiratory_base = arma_process.generate_sample(nsample=300)

# Scale to realistic respiratory rate values (12-20 breaths/min)
respiratory_mean = 16
respiratory_std = 2
respiratory_rate = respiratory_mean + respiratory_std * respiratory_base

# Plot the time series and ACF
plt.figure(figsize=(16, 5))

plt.subplot(1, 2, 1)
time = np.arange(len(respiratory_rate))
plt.plot(time, respiratory_rate, linewidth=1, color='steelblue')
plt.title('Synthetic Respiratory Rate Time Series', fontsize=14, fontweight='bold')
plt.xlabel('Time (minutes)', fontsize=12)
plt.ylabel('Respiratory Rate (breaths/min)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.axhline(y=respiratory_mean, color='gray', linestyle='--', alpha=0.5, label=f'Mean = {respiratory_mean} breaths/min')
plt.legend()

plt.subplot(1, 2, 2)
plot_acf(respiratory_rate, lags=15, alpha=0.05, ax=plt.gca())
plt.title('ACF Plot: Respiratory Rate (MA(2) Pattern)', fontsize=14, fontweight='bold')
plt.xlabel('Lag', fontsize=12)
plt.ylabel('Autocorrelation', fontsize=12)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Print ACF values
acf_values = acf(respiratory_rate, nlags=10, fft=False)
print("ACF values for respiratory rate (lags 0-10):")
for k in range(11):
    print(f"  ρ({k}) = {acf_values[k]:.4f}")
print("\nNote: Sharp cutoff after lag 2 indicates MA(2) process")
print("Memory length: 2 time steps")
```

**Expected Output:**
- Time series: Stationary with short memory
- ACF: Sharp cutoff after lag 2, $\rho(1)$ and $\rho(2)$ significant
- Model: MA(2) or ARIMA(0,0,2)

---

### Problem 4.5

Consider a body temperature time series where the ACF shows:
- Exponential decay starting at $\rho(1) \approx 0.9$
- Gradual decrease: $\rho(5) \approx 0.5$, $\rho(10) \approx 0.2$
- All values positive, no oscillations

![Time Series Plot](figures/problem4_5_timeseries.png)

1. What type of process does this indicate?
2. What is the approximate memory length?
3. Would deep learning provide significant advantages over traditional methods?
4. Generate a synthetic body temperature time series and plot the series and ACF.

**Solution 4.5**

1. **Process Type:** This indicates an **Autoregressive (AR) process**, likely **AR(1)** with a high coefficient ($\phi \approx 0.9$). The exponential decay is characteristic of AR processes.

2. **Memory Length:** The memory is **longer** than MA processes. While the ACF decays, it remains significant for many lags. The "effective memory" might be around 10-15 time steps (where ACF drops below 0.2).

3. **Deep Learning Necessity:** **Probably not necessary**, but depends on context:
   - **Traditional AR/ARIMA sufficient if:** The process is linear and stationary
   - **Deep learning might help if:** There are nonlinear relationships, external factors, or complex patterns not captured by ACF
   - **For simple AR(1):** Traditional methods are more interpretable and efficient

4. **Python Code:**

```python
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import acf
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.arima_process import ArmaProcess

# Set random seed for reproducibility
np.random.seed(42)

# Generate AR(1) process to simulate body temperature
# AR(1): x_t = μ + φ*(x_{t-1} - μ) + ε_t
# Use φ = 0.9 to match the ACF requirement
ar_coeffs = np.array([1, -0.9])  # AR(1) with φ = 0.9
ma_coeffs = np.array([1])

arma_process = ArmaProcess(ar_coeffs, ma_coeffs)
temp_base = arma_process.generate_sample(nsample=300)

# Scale to realistic body temperature values (36.5-37.5°C)
temp_mean = 37.0
temp_std = 0.3
body_temp = temp_mean + temp_std * temp_base

# Plot the time series and ACF
plt.figure(figsize=(16, 5))

plt.subplot(1, 2, 1)
time = np.arange(len(body_temp))
plt.plot(time, body_temp, linewidth=1, color='crimson')
plt.title('Synthetic Body Temperature Time Series', fontsize=14, fontweight='bold')
plt.xlabel('Time (hours)', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.axhline(y=temp_mean, color='gray', linestyle='--', alpha=0.5, label=f'Mean = {temp_mean}°C')
plt.legend()

plt.subplot(1, 2, 2)
plot_acf(body_temp, lags=20, alpha=0.05, ax=plt.gca())
plt.title('ACF Plot: Body Temperature (AR(1) Exponential Decay)', fontsize=14, fontweight='bold')
plt.xlabel('Lag', fontsize=12)
plt.ylabel('Autocorrelation', fontsize=12)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Print ACF values
acf_values = acf(body_temp, nlags=15, fft=False)
print("ACF values for body temperature (lags 0-15):")
for k in range(0, 16, 2):
    print(f"  ρ({k}) = {acf_values[k]:.4f}")

# Compare with theoretical AR(1) decay
print("\nTheoretical AR(1) decay (φ = 0.9):")
for k in range(0, 16, 2):
    theoretical = 0.9**k
    print(f"  Theoretical ρ({k}) = {theoretical:.4f}")

print("\nMemory length: ~10-15 time steps (where ACF drops below 0.2)")
print("Model recommendation: AR(1) or ARIMA(1,0,0)")
```

**Expected Output:**
- Time series: Smooth, persistent variations
- ACF: Exponential decay, $\rho(k) \approx 0.9^k$
- Memory: Long (10-15 time steps)
- Model: AR(1) or ARIMA(1,0,0)

---

## Summary

This problem set covers:

1. **Numerical ACF Calculation:** Manual computation of autocovariance and autocorrelation, including edge cases (constant series, zero variance).

2. **Mean Removal Effect:** Understanding why mean removal is essential for correct autocorrelation computation and avoiding spurious correlations.

3. **ACF Pattern Interpretation:** Identifying process types (white noise, trend, seasonality, AR, MA) from ACF plots with Python visualizations.

4. **Physiological Time-Series:** Applying ACF analysis to real-world biomedical signals, determining appropriate models, and assessing when advanced methods are needed.

All problems include complete solutions with mathematical derivations, Python code for illustrations, and pedagogical explanations suitable for undergraduate students.
