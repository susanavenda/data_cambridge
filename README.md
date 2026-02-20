# Data Science Portfolio: Statistical Methods & Predictive Modeling

> **Week 2: From Intuition to Evidence-Based Decision Making**

## 🧭 Project Overview

This repository contains a series of technical analyses focused on applying advanced statistical techniques to solve business problems. The goal of this work is to move beyond "gut feeling" and use mathematical rigor to validate assumptions, identify patterns, and predict future outcomes.

## 🛠️ Skills Demonstrated

* **Hypothesis Testing:** -tests, ANOVA, and Chi-Square analysis.
* **Correlation:** Pearson () and Spearman () coefficients for relationship mapping.
* **Regression:** Simple and Multiple Linear Regression using OLS (Ordinary Least Squares).
* **Model Evaluation:** Interpreting , Adjusted , and RSS (Residual Sum of Squares).
* **Risk Assessment:** Evaluating Sensitivity vs. Specificity and Prediction Intervals.

---

## Decision Logic Flow

The following diagram illustrates the decision-making framework used throughout these activities to select the appropriate statistical test based on data types and business goals.

```mermaid
graph TD
    A[Start: Receive Dataset] --> B{Data Type?}
    
    B -- Categorical --> C[Count frequencies / Proportions]
    B -- Continuous --> D[Check Distribution: Histogram]
    
    D --> E{Is it Normal?}
    E -- Yes: Parametric --> F[Mean, SD, Pearson r, t-test]
    E -- No: Non-Parametric --> G[Median, IQR, Spearman rho]
    
    F --> H{Business Goal?}
    G --> H
    C --> H
    
    H -- "Compare Groups" --> I{How many groups?}
    I -- 2 Groups --> J[t-test]
    I -- 3+ Groups --> K[ANOVA]
    I -- Cat vs Cat --> L[Chi-Square]
    
    H -- "Find Relationships" --> M[Correlation Analysis]
    H -- "Predict Outcomes" --> O[Linear Regression]
    
    O --> P[Check Model Fit: R-Squared / RSS]
    P --> Q[Check Assumptions: Residual Plots]
    
    R[p-value] --> U[Business Recommendation]
    S[Strength/Direction] --> U
    T[Coefficients] --> U

```

---

## Portfolio Activities

###  Activity 2.1.3: Hypothesis Testing
```mermaid
graph LR
    Start[Business Scenario] --> Q1{What are we comparing?}
    Q1 -- "Means (Averages)" --> Q2{How many groups?}
    Q1 -- "Category Counts" --> Chi[Chi-Square Test]
    
    Q2 -- "2 Groups" --> T[t-test]
    Q2 -- "3+ Groups" --> ANOVA[One-way ANOVA]
    
    T --> P{p < 0.05?}
    ANOVA --> P
    Chi --> P
    
    P -- Yes --> Res1[Significant: Reject Null]
    P -- No --> Res2[Not Significant: Keep Status Quo]
```
* **Objective:** Validate business assumptions across five scenarios (Price, Productivity, Market Research, QC, and Product Lines).
* **Technical Implementation:** Utilized `scipy.stats` to perform t-tests and ANOVA.
* **Key Insight:** Separated "signal" from "noise" by interpreting -values against a significance level () of **0.05**.

### 🔗 Activity 2.2.3: Interpreting Correlation

<img width="3998" height="2011" alt="image" src="https://github.com/user-attachments/assets/3482bbcc-fe5a-4fe6-abeb-37a3fc208faa" />

```mermaid
graph TD
    Data[BMI, Children, Costs] --> Plot[Scatter Plot Visualization]
    Plot --> Linear{Is the trend a<br/>straight line?}
    
    Linear -- Yes --> Pearson[Pearson r]
    Linear -- No/Outliers --> Spearman[Spearman rho]
    
    Pearson --> Interpret[Check Strength & Direction]
    Spearman --> Interpret
    
    Interpret --> Caution[Identify Confounding Factors]
    Caution --> Logic[Correlation != Causation]
```    
* **Objective:** Analyze lifestyle impacts (BMI, children) on medical insurance costs for an investment firm.
* **Technical Implementation:** Computed Pearson and Spearman coefficients; visualized relationships via Seaborn scatterplots.
* **Key Insight:** Identified confounding variables (like Age) to avoid the "Correlation implies Causation" fallacy.

### 📈 Activity 2.3.5: Building Predictive Models
```mermaid
graph TD
    Features[Quality, Awareness, Satisfaction] --> Model[Multiple Linear Regression]
    Model --> Coeff[Interpret Coefficients: Impact per variable]
    Model --> Fit{Evaluate Fit}
    
    Fit -- "R-Squared" --> Stats[Explain % of Variance]
    Fit -- "RSS" --> Stats[Quantify Unexplained Error]
    
    Stats --> Assumptions{Check Residuals}
    Assumptions -- "Random Scatter" --> Valid[Model Reliable]
    Assumptions -- "Pattern/Fan Shape" --> Invalid[Model Biased: Heteroscedasticity]
    
    Valid --> Recommend[Strategy: Which feature to invest in?]
```
* **Objective:** Predict customer loyalty for a national retailer based on product quality and brand awareness.
* **Technical Implementation:** Built a Multiple Linear Regression model using `statsmodels` and `scikit-learn`.
* **Evaluation:** Optimized the model by minimizing RSS and analyzing Adjusted  to prevent overfitting.
* **Business Impact:** Provided coefficient-based insights (e.g., "A 1-unit increase in perceived quality yields a  increase in loyalty").

---

## Assumption & Diagnostic Checks

To ensure model reliability, I performed the following diagnostic checks:

* **Homoscedasticity:** Verified constant variance in residuals to ensure consistent prediction accuracy.
* **Multicollinearity:** Screened independent variables to ensure they were not redundant.
* **Prediction Intervals:** Provided a range for new observations to account for individual variability.

---

## Technologies Used

* **Language:** Python 3.x
* **Libraries:** `Pandas`, `NumPy`, `Matplotlib`, `Seaborn`, `Scipy.stats`, `Statsmodels`, `Scikit-Learn`
* **Documentation:** Mermaid.js, Markdown

