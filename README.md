# Data Science Portfolio: Statistical Methods and Predictive Modeling

## Project Overview

This repository contains a series of technical analyses focused on applying advanced statistical techniques to solve business problems. The goal of this work is to move beyond "gut feeling" and use mathematical rigor to validate assumptions, identify patterns, and predict future outcomes. This portfolio follows the transition from strategic business framing to predictive execution.

## Skills Demonstrated

* **Strategic Planning:** CRISP-DM lifecycle, 5 Whys Root Cause Analysis, and DIKW Pyramid.
* **Hypothesis Testing:** t-tests, ANOVA, and Chi-Square analysis.
* **Correlation:** Pearson (r) and Spearman (rho) coefficients for relationship mapping.
* **Regression:** Simple and Multiple Linear Regression using OLS (Ordinary Least Squares).
* **Model Evaluation:** Interpreting R-Squared, Adjusted R-Squared, and RSS (Residual Sum of Squares).
* **Risk Assessment:** Evaluating Sensitivity vs. Specificity and Prediction Intervals.

---

## Week 1: Strategic Foundations

### 1. The CRISP-DM Framework

Before performing analysis, I utilize the **CRISP-DM** (Cross-Industry Process for Data Mining) lifecycle to ensure technical work aligns with business ROI.

```mermaid
graph LR
    subgraph Iterative Cycle
    BU[Business Understanding] <--> DU[Data Understanding]
    DU <--> DP[Data Preparation]
    DP <--> M[Modeling]
    M <--> E[Evaluation]
    E --> BU
    end
    E --> D[Deployment]
    style BU fill:#f9f,stroke:#333,stroke-width:2px
    style D fill:#6f6,stroke:#333,stroke-width:2px

```

* **Business Understanding (DIKW Pyramid):** Moving from raw data to actionable wisdom.

```mermaid
graph TD
    W[Wisdom: Strategic Action] --- K[Knowledge: Why it happened]
    K --- I[Information: Context/Trends]
    I --- D[Data: Raw Numbers]
    style W fill:#ffd700,stroke:#333,stroke-width:4px

```

* **Data Understanding (The 5 Vs):** Assessing **Volume, Velocity, Variety, Veracity, and Value** to determine data maturity.

```mermaid
mindmap
  root((5 Vs of Big Data))
    Volume
    Velocity
    Variety
    Veracity
    Value

```

* **Feature Engineering:** Applying human ingenuity to create new variables (e.g., **Debt-to-Income ratio**) that provide context to "Black Box" models.

```mermaid
graph TD
    Raw[Raw Data Sources] --> Domain[Domain Knowledge Application]
    Domain --> Creation{New Feature Creation}
    Creation -- Example --> DTI[Debt-to-Income Ratio]
    Creation -- Example --> PPSF[Price Per Sq Ft]
    DTI --> Selection[Feature Selection]
    PPSF --> Selection
    Selection --> Model[Machine Learning Model]
    linkStyle default stroke:#2ecc71,stroke-width:2px;

```

### 2. Data Classification and Maturity

Understanding data types determines the mathematical toolkit required for the project.

* **Categorical (Nominal/Ordinal):** For grouping and ranking.
* **Numerical (Discrete/Continuous):** For counting and measuring.

```mermaid
graph TD
    Data[Data Types] --> Cat[Categorical / Qualitative]
    Data --> Num[Numerical / Quantitative]
    Cat --> Nom[Nominal]
    Nom -- Example --> Eye[Eye Color, Gender]
    Cat --> Ord[Ordinal]
    Ord -- Example --> Rank[Survey Ratings, Seniority]
    Num --> Disc[Discrete]
    Disc -- Example --> Count[Number of Employees]
    Num --> Cont[Continuous]
    Cont -- Example --> Meas[Revenue, Weight, Time]
    style Cat fill:#e1f5fe,stroke:#01579b
    style Num fill:#fff3e0,stroke:#e65100

```

---

## Master Decision Logic Flow

The following diagram illustrates the end-to-end framework used to select the appropriate statistical test based on data types and business goals.

```mermaid
graph TD
    A[Start: Receive Dataset] --> B[CRISP-DM: Business Understanding]
    B --> C{Data Type?}
    C -- Categorical --> D[Count frequencies / Proportions]
    C -- Continuous --> E[Check Distribution: Histogram]
    E --> F{Is it Normal?}
    F -- Yes: Parametric --> G[Mean, SD, Pearson r, t-test]
    F -- No: Non-Parametric --> H[Median, IQR, Spearman rho]
    G --> I{Business Goal?}
    H --> I
    D --> I
    I -- "Compare Groups" --> J{How many groups?}
    J -- 2 Groups --> K[t-test]
    J -- 3+ Groups --> L[ANOVA]
    J -- Cat vs Cat --> M[Chi-Square]
    I -- "Find Relationships" --> N[Correlation Analysis]
    I -- "Predict Outcomes" --> O[Linear Regression]
    O --> P[Check Model Fit: R-Squared / RSS]
    P --> Q[Check Assumptions: Residual Plots]

```

---

## Portfolio Activities

### Activity 2.1.3: Hypothesis Testing

* **Objective:** Validate business assumptions across five scenarios (**Price, Productivity, Market Research, QC, and Product Lines**).
* **Technical Implementation:** Utilized `scipy.stats` to perform t-tests and ANOVA to separate "signal" from "noise."
* **Key Insight:** Interpreted p-values against a significance level (alpha) of **0.05** to determine if results were statistically significant or due to chance.

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

### Activity 2.2.3: Interpreting Correlation

* **Objective:** Analyze lifestyle impacts (**BMI, children**) on medical insurance costs for an investment firm.
* **Technical Implementation:** Computed **Pearson (r)** for linear trends and **Spearman (rho)** for non-linear relationships or outliers.
* **Key Insight:** Identified confounding variables (like **Age**) to avoid the "Correlation implies Causation" fallacy.

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

### Activity 2.3.5: Building Predictive Models

* **Objective:** Predict customer loyalty for a national retailer based on **product quality, brand awareness, and satisfaction**.
* **Technical Implementation:** Built a Multiple Linear Regression model using **OLS (Ordinary Least Squares)**.
* **Evaluation:** Interpreted **Adjusted R-Squared** to ensure model complexity did not lead to overfitting and minimized **RSS**.
* **Business Impact:** Provided coefficient-based insights (e.g., "A 1-unit increase in perceived quality yields a measurable increase in loyalty score").

```mermaid
graph TD
    Features[Quality, Awareness, Satisfaction] --> Model[Multiple Linear Regression]
    Model --> Coeff[Interpret Coefficients: Impact per variable]
    Model --> Fit{Evaluate Fit}
    Fit -- "R-Squared" --> Stats[Explain % of Variance]
    Fit -- "RSS" --> Stats[Quantify Unexplained Error]
    Stats --> Assumptions{Check Residuals}
    Assumptions -- "Random Scatter" --> Valid[Model Reliable]

```

---

## Assumption and Diagnostic Checks

### 1. Central Limit Theorem (CLT)

The CLT is the "Safety Net" of statistics. It explains why we can use Normal Distribution math even if the raw data looks "messy" or non-normal.

[Image illustrating the Central Limit Theorem showing how different population distributions result in normal sampling distributions]

```mermaid
graph LR
    Pop[Messy/Non-Normal Population] --> Samples[Take 1000s of Samples]
    Samples --> Means[Calculate Mean of each Sample]
    Means --> Dist[Normal Distribution of Means]
    style Dist fill:#f9f,stroke:#333,stroke-width:2px

```

### 2. Prediction vs. Confidence Intervals

This diagnostic check accounts for the difference between group averages and individual variability.

[Image comparing Confidence Intervals and Prediction Intervals on a regression plot, showing the PI as a wider band]

```mermaid
graph TD
    A[Prediction] --> B{What are you predicting?}
    B -- "The Group Average" --> C[Confidence Interval: Narrower Band]
    B -- "A Specific Individual" --> D[Prediction Interval: Wider Band]
    C --> E[Use for Strategy/ROI]
    D --> F[Use for Risk Assessment]
    style D fill:#fff3e0,stroke:#e65100

```

### 3. Model Reliability Audits

* **Homoscedasticity:** Verified constant variance in residuals to ensure consistent prediction accuracy.
* **Multicollinearity:** Screened independent variables using **VIF Analysis** to ensure they were not redundant.
* **Risk Assessment (Sensitivity vs. Specificity):** Evaluated trade-offs to balance between missing positives and raising false alarms.

```mermaid
graph LR
    subgraph "Sensitivity (Catching the Truth)"
    TP[True Positives]
    FN[False Negatives]
    end
    subgraph "Specificity (Avoiding False Alarms)"
    TN[True Negatives]
    FP[False Positives]
    end
    TP -.-> Tradeoff{The Balance}
    FP -.-> Tradeoff

```

---

## Glossary of Mathematical Terms for Study

| Term | Definition |
| --- | --- |
| **p-value** | The probability that the observed results happened by chance. If , we reject the Null Hypothesis. |
| **OLS (Ordinary Least Squares)** | A method for estimating the parameters in a linear regression model by minimizing the sum of the squares of the vertical deviations between each data point and the fitted line. |
| **RSS (Residual Sum of Squares)** | A measure of the discrepancy between the data and an estimation model. A small RSS indicates a tight fit of the model to the data. |
| **R-Squared ()** | The proportion of the variance for a dependent variable that is explained by an independent variable or variables in a regression model. |
| **Adjusted R-Squared** | A modified version of R-squared that has been adjusted for the number of predictors in the model; it only increases if the new term improves the model more than would be expected by chance. |
| **VIF (Variance Inflation Factor)** | A measure of the amount of multicollinearity in a set of multiple regression variables. High VIF (usually > 5 or 10) indicates high correlation between predictors. |
| **Homoscedasticity** | A condition in which the variance of the residual (error) is constant across all levels of the independent variables. |

---

## Technologies Used

* **Language:** Python 3.x
* **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scipy.stats, Statsmodels, Scikit-Learn
* **Documentation:** Mermaid.js, Markdown
