

## 1. Course Information

- **Course title:** Time Series Analysis and Forecasting
- **Course code:** EP16.TOKT11122
- **Type of course:** Compulsory
- **Credits:** 3
    - Lecture: 30 hours
    - Lab / Tutorial: 15 hours
    - Self-study: 90 hours
- **Prerequisites:**
    - EP16.TOKT1145
    - EP16.TOKT11108

***

## 2. Department and Instructor

- **Department:** Mathematical Economics
- **Address:** Suite 1105, Building A1, NEU
- **Instructor:** [To be assigned]

***

## 3. Course Description

This course provides a practical introduction to time series analysis and forecasting with applications in finance, economics, and healthcare. Students use Python (NumPy, Pandas, Matplotlib, Statsmodels, Scikit-learn, and optionally deep learning frameworks) to work with real-world time-indexed data.

Core topics include time series concepts and components, exploratory analysis, stationarity, ARIMA and SARIMA models. In the later weeks, students are introduced to machine learning and deep learning methods for time series, such as tree-based models and simple recurrent or convolutional neural networks.

The course is strongly project-based. Students work in groups on real datasets (e.g., stock prices, macroeconomic indicators, vital signs, EEG/ECG signals). All lab weeks are dedicated to **project progress presentations**. A **Midterm Project Baseline Report** (PDF + presentation file) replaces the traditional midterm exam and focuses on establishing strong classical baselines. The final deliverable is a comprehensive group project including both classical and ML/DL methods.

***

## 4. Learning Resources

**Main textbooks**

1. Gebhard Kirchgässner, Jürgen Wolters (2013), *Introduction to Modern Time Series Analysis*, Springer.
2. Wes McKinney (2022), *Python for Data Analysis*, O’Reilly Media.
3. Eryk Lewinson (2022), *Python for Finance Cookbook*, Packt Publishing.

**Other references**

4. Tarek A. Atwan (2022), *Time Series Analysis with Python Cookbook: Practical recipes for exploratory data analysis, data preparation, forecasting, and model evaluation*, Packt Publishing.
5. Changquan Huang and Alla Petukhina (2022), *Applied Time Series Analysis and Forecasting with Python*, Springer.
6. Ben Auffarth (2021), *Machine Learning for Time-Series with Python*, Packt Publishing.
7. Francesca Lazzeri (2020), *Machine Learning for Time Series Forecasting with Python*, Wiley.
8. Online notes: https://online.stat.psu.edu/stat510/

***

## 5. Course Objectives

By the end of the course, students should be able to:

- **G1.** Understand fundamental time series concepts and their applications in stock markets, finance, economics, and healthcare.
- **G2.** Collect, preprocess, and manipulate time series data in Python using appropriate libraries.
- **G3.** Conduct exploratory time series analysis, including visualization, decomposition, and stationarity assessment.
- **G4.** Model and forecast time series data using core statistical methods such as ARIMA and SARIMA.
- **G5.** Apply and compare traditional time series models with basic machine learning and deep learning methods for time series forecasting.
- **G6.** Develop teamwork, self-study, independent work, and shared responsibility within project groups through a project-based learning approach.

***

## 6. Course Learning Outcomes (CLOs)

Students who successfully complete this course will be able to:

- **CLO 1.1 (G1):** Explain key time series concepts (trend, seasonality, cyclicity, noise) and their relevance in real-world applications.
- **CLO 1.2 (G2):** Use Python (Pandas, NumPy, Matplotlib, Statsmodels) to load, preprocess, and visualize time series data.
- **CLO 2.1 (G3):** Perform exploratory analysis of time series using ACF/PACF, decomposition, and smoothing techniques.
- **CLO 3.1 (G3, G4):** Explain the concept of stationarity and apply differencing and basic tests (e.g., ADF) to assess it.
- **CLO 3.2 (G4):** Build and interpret AR, MA, and ARMA models and implement them in Python.
- **CLO 4.1 (G4):** Build, evaluate, and diagnose ARIMA and SARIMA models using the Box–Jenkins methodology.
- **CLO 4.2 (G5):** Transform time series into supervised learning format and implement basic machine learning models (e.g., tree-based models) for forecasting.
- **CLO 4.3 (G5):** Describe the role of deep learning models (RNN/LSTM/CNN) for time series and implement a simple example.
- **CLO 5.1 (G5):** Design and implement a complete forecasting pipeline on a real dataset, combining classical and ML/DL approaches.
- **CLO 5.2 (G5):** Analyze and interpret model results, compare methods, and provide actionable insights.
- **CLO 6.1 (G6):** Demonstrate self-study and independent work through homework and project contributions.
- **CLO 6.2 (G6):** Collaborate effectively in teams and report project progress clearly in written and oral form.

***

## 7. Course Assessment

| Type of Assessment | Content | Week | CLOs covered | Tools / Criteria | Weight |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Homework | Theory \& programming (individual) | Selected weeks | 1.2, 2.1, 3.1, 3.2, 4.1, 4.2, 4.3, 6.1 | LMS / online submission; correctness, problem-solving, application to time series, time management | 20% |
| Midterm Project Baseline | Group baseline report (PDF) + baseline presentation file (slides) | Week 10 | 1.2–4.1, 5.1, 5.2, 6.1, 6.2 | Written baseline report + slide deck; EDA, ARIMA/SARIMA baseline, forecasts \& plots, clarity, structure | 30% |
| Final Project | Full group project report (PDF) \& final presentation (slides + oral) | Week 15 | 1.1–5.2, 6.1, 6.2 | Report, code, slides; integration of classical + ML/DL models, depth of analysis, comparison, clarity, teamwork | 50% |

**Notes:**

- All **lab weeks** are used for **group progress presentations**; these count toward the overall project evaluation (midterm and final), not as separate lab assignments.
- The **Midterm Project Baseline** replaces a traditional written exam and focuses on producing a strong classical (ARIMA/SARIMA) baseline.

***

## 8. Teaching Plan (15 Weeks, Lecture–Lab Alternation)

### Week 1 – Course Introduction \& Environment Setup (Lecture)

- **Content:**
    - Course overview: objectives, assessment, project-based structure, topics
    - Group project requirements: team size, roles, deliverables, timeline
    - Introduction to time series: definition, examples, applications in finance, economics, healthcare
    - Python ecosystem overview: NumPy, Pandas, Matplotlib, Statsmodels, Scikit-learn
    - Environment setup:
        - Anaconda/Conda installation and environment creation
        - Installing core libraries
        - Kaggle: account creation, finding datasets, Kaggle Notebook vs local Jupyter
- **CLOs:** 1.1, 1.2, 6.1, 6.2
- **Activities:** Lecture, live demo, Q\&A
- **Assessment:** None

***

### Week 2 – Python \& Time Series Fundamentals (Lecture)

- **Content:**
    - NumPy review for time series (arrays, vectorization, indexing)
    - Pandas for time series:
        - Reading CSV, parsing dates, datetime index
        - Resampling and frequency conversion
        - Rolling windows and basic statistics
    - Simple financial indicators as time series practice:
        - SMA, EMA, RSI, MACD implementation using Pandas
- **CLOs:** 1.2, 2.1, 6.1
- **Activities:** Lecture + code walkthrough
- **Assessment:** Homework 1 (data loading, basic indicators, plotting)

***

### Week 3 – Lab 1: Project Kick-off \& Progress Reporting

- **Content:**
    - Confirm group formation and topic selection
    - Each group (approximately 2–3 minutes):
        - Introduces dataset and problem statement
        - Shows successful data loading and a simple time series plot
    - Instructor feedback on feasibility and scope
- **CLOs:** 1.2, 5.1, 6.1, 6.2
- **Activities:** Short group presentations, open lab time for technical issues
- **Assessment:** Project progress (contributes to midterm/final project evaluation)

***

### Week 4 – Exploratory Time Series Analysis (Lecture)

- **Content:**
    - Time series components: trend, seasonality, cyclicity, noise
    - White noise vs structured time series
    - Autocorrelation Function (ACF) and Partial Autocorrelation Function (PACF):
        - Interpretation, relationship to model identification
    - Time series decomposition:
        - Additive vs multiplicative decomposition using Statsmodels
    - Simple smoothing:
        - Moving average and exponential smoothing (conceptual and practical)
- **CLOs:** 2.1, 3.1, 6.1
- **Activities:** Lecture + code examples
- **Assessment:** Homework 2 (EDA with ACF/PACF and decomposition on a given dataset)

***

### Week 5 – Lab 2: EDA on Project Data \& Progress Reporting

- **Content:**
    - Each group reports:
        - Data cleaning steps and handling missing values
        - Main EDA plots (time plots, ACF/PACF, decomposition)
        - Observed trend, seasonality, and possible issues
    - Instructor feedback on modeling directions
- **CLOs:** 2.1, 3.1, 5.1, 5.2, 6.1, 6.2
- **Activities:** Group presentations + discussion
- **Assessment:** Project progress

***

### Week 6 – Stationarity \& Basic Time Series Models (Lecture)

- **Content:**
    - Stationarity:
        - Definition and importance for modeling
        - Visual diagnostics (plots, rolling statistics)
        - Unit root tests (ADF) at a practical level
    - Differencing and backshift operator (conceptual explanation + code)
    - AR(p), MA(q), ARMA(p,q) models:
        - Model structure and intuition
        - Using ACF/PACF for identifying AR/MA patterns
    - Implementation with Statsmodels:
        - Fitting AR/MA/ARMA and basic residual diagnostics
- **CLOs:** 3.1, 3.2, 4.1, 6.1
- **Activities:** Lecture, derivation sketches, code examples
- **Assessment:** Homework 3 (stationarity checks + simple AR/MA/ARMA on a sample time series)

***

### Week 7 – Lab 3: Stationarity \& AR/MA/ARMA on Project Data

- **Content:**
    - Each group reports:
        - Stationarity assessment (plots, ADF results, differencing if needed)
        - First AR/MA/ARMA models fitted to key series
        - Preliminary evaluation: residual behavior, limitations
    - Instructor feedback guiding next steps toward ARIMA
- **CLOs:** 3.1, 3.2, 4.1, 5.1, 6.1, 6.2
- **Activities:** Group presentations, Q\&A, open lab work
- **Assessment:** Project progress

***

### Week 8 – ARIMA and Box–Jenkins Methodology (Lecture)

- **Content:**
    - ARIMA(p,d,q) models:
        - Role of differencing (d)
        - Interpretation of p, d, q
    - Box–Jenkins process:
        - Identification → Estimation → Diagnostic checking → Forecasting
    - Model selection:
        - AIC/BIC, residual diagnostics, forecast error metrics (MAE, RMSE)
    - Full ARIMA pipeline in Python with Statsmodels:
        - From differencing to model selection and forecasting
- **CLOs:** 3.1, 4.1, 5.1, 6.1
- **Activities:** Lecture + code-along example
- **Assessment:** Homework 4 (end-to-end ARIMA on a given dataset)

***

### Week 9 – Lab 4: ARIMA on Project Data \& Midterm Preparation

- **Content:**
    - Each group reports:
        - ARIMA models for key series (chosen p,d,q, justification)
        - Model selection (AIC/BIC) and residual diagnostics
        - Short-term forecast plots and forecast accuracy metrics
    - Instructor details **Midterm Project Baseline** requirements:

**Midterm Project Baseline (due Week 10):**
        - **Deliverables:**
            - PDF baseline report
            - Presentation file (slides, e.g., PowerPoint/PDF)
        - **Report structure (suggested):**

1. Problem statement and objectives
2. Dataset description (source, variables, time range)
3. EDA summary (key plots, stationarity analysis)
4. ARIMA/SARIMA baseline models (specification and rationale)
5. Forecasting results:
                - Visualizations (actual vs forecast)
                - Quantitative evaluation (e.g., MAE, RMSE)
6. Discussion: strengths, limitations, and next steps (ML/DL plans)
- **CLOs:** 3.1, 4.1, 5.1, 5.2, 6.1, 6.2
- **Activities:** Group presentations, instructor guidance for midterm report
- **Assessment:** Project progress

***

### Week 10 – Midterm Project Baseline (Lecture / Presentations)

- **Content:**
    - **Submission (before or at class):**
        - Midterm Project Baseline Report (PDF)
        - Midterm Baseline Presentation file (slides)
    - **In-class presentations** (about 5–7 minutes per group):
        - Problem statement \& dataset overview
        - EDA highlights and stationarity findings
        - ARIMA/SARIMA baseline models and reasons for selection
        - Forecast plots and performance metrics
        - Short discussion of insights and limitations
    - Instructor and peers provide feedback to guide second-phase (ML/DL) work
- **CLOs:** 1.2–4.1, 5.1, 5.2, 6.1, 6.2
- **Activities:** Group presentations, Q\&A, feedback
- **Assessment:** Midterm Project Baseline – 30%

***

### Week 11 – Seasonal Models and SARIMA (Lecture)

- **Content:**
    - Seasonal patterns and seasonal nonstationarity
    - Seasonal differencing and seasonal lags
    - SARIMA models:
        - Structure (p,d,q) × (P,D,Q)\_s and intuition
    - Implementation with Statsmodels (SARIMAX)
    - Comparison: ARIMA vs SARIMA for seasonal data
- **CLOs:** 3.1, 4.1, 5.1, 6.1
- **Activities:** Lecture + demonstrations
- **Assessment:** Homework 5 (SARIMA on a seasonal dataset)

***

### Week 12 – Lab 5: Seasonal Refinement \& ML Planning

- **Content:**
    - Each group reports:
        - Any seasonal modeling (SARIMA) applied and its impact on baseline results
        - Final choice of classical models to keep in the project
        - Plan for ML/DL extensions:
            - Feature engineering (lags, rolling stats, calendar features)
            - Candidate ML/DL models (tree-based, LSTM, etc.)
    - Instructor feedback on design and feasibility of ML/DL phase
- **CLOs:** 3.1, 4.1, 5.1, 5.2, 6.1, 6.2
- **Activities:** Group presentations, planning discussion
- **Assessment:** Project progress

***

### Week 13 – Machine Learning for Time Series (Lecture)

- **Content:**
    - Time series as supervised learning:
        - Creating lag features, rolling-window features, calendar variables
    - ML models for forecasting:
        - Linear regression baselines
        - Tree-based models: Random Forest, Gradient Boosting (e.g., XGBoost/LightGBM)
    - Train/validation/test splits in time:
        - Rolling-origin, walk-forward validation basics
    - Example: ARIMA vs Random Forest on a simple time series forecasting task
- **CLOs:** 4.2, 5.1, 5.2, 6.1
- **Activities:** Lecture + code examples
- **Assessment:** Homework 6 (build and evaluate a tree-based ML model on a time series forecasting task)

***

### Week 14 – Deep Learning for Time Series (Lecture)

- **Content:**
    - Deep learning architectures for time series:
        - RNN, LSTM, GRU (high-level understanding)
        - 1D-CNN for time series
    - Typical DL workflows:
        - Sliding window input, sequence-to-one and sequence-to-sequence setups
        - Normalization and temporal train/validation splits
    - Simple LSTM example (univariate forecasting) using Keras/PyTorch:
        - Model definition
        - Training and evaluation
    - Discussion: when DL is useful vs when classical/ML models are sufficient
- **CLOs:** 4.3, 5.1, 5.2, 6.1
- **Activities:** Lecture + code walkthrough (focus on concepts, not heavy implementation details)
- **Assessment:** Optional DL mini-extension linked to Homework 6 (depending on time)

***

### Week 15 – Final Project Presentations (Lab)

- **Content:**
    - Each group presents (10–15 minutes):
        - Problem and dataset
        - EDA and classical models (final ARIMA/SARIMA baselines)
        - ML/DL models implemented (at least one ML; DL encouraged but optional)
        - Model comparison with metrics and plots
        - Key insights, limitations, and potential future work
    - Submission:
        - Final project report (PDF) – extended and improved from midterm baseline
        - All notebooks/code
        - Final presentation slides
- **CLOs:** 1.1–5.2, 6.1, 6.2
- **Activities:** Group presentations, peer questions, instructor feedback
- **Assessment:** Final Project – 50%

***

## 9. Class Regulations

- Students must attend at least **80%** of classes to pass the course.
- Active participation in lectures and labs is expected.
- Participation in the **group project** is **mandatory**.
- In class:
    - Avoid using mobile phones or eating
    - Use laptops/tablets only for course-related activities (coding, notes, calculations)
- Academic integrity is strictly enforced. Plagiarism and cheating in homework, reports, or exams will be handled according to university regulations.

