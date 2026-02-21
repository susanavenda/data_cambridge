# Data Science Portfolio: Statistical Methods & Predictive Modeling

> **Week 2: From Intuition to Evidence-Based Decision Making**

## Project Overview

This repository documents a complete data science workflow. It transitions from the strategic planning of Week 1 (CRISP-DM, Data Maturity, and Feature Engineering) to the mathematical execution of Week 2 (Hypothesis Testing, Correlation, and Regression). The goal is to move beyond "gut feeling" and use mathematical rigor to validate assumptions and predict outcomes.

## 🛠️ Skills Demonstrated
* **Strategic Planning:** CRISP-DM lifecycle, 5 Whys Root Cause Analysis, and DIKW Pyramid.
* **Hypothesis Testing:** -tests, ANOVA, and Chi-Square analysis.
* **Correlation:** Pearson () and Spearman () coefficients for relationship mapping.
* **Regression:** Simple and Multiple Linear Regression using OLS (Ordinary Least Squares).
* **Model Evaluation:** Interpreting , Adjusted , and RSS (Residual Sum of Squares).
* **Risk Assessment:** Evaluating Sensitivity vs. Specificity and Prediction Intervals.

---

Week 1: Strategic Foundations
1. The CRISP-DM Framework
Before touching code, I utilize the CRISP-DM lifecycle to ensure technical work solves a real business problem.
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

Business Understanding: Defining the "Wisdom" required for action.
```mermaid
graph TD
    W[Wisdom: Strategic Action] --- K[Knowledge: Why it happened]
    K --- I[Information: Context/Trends]
    I --- D[Data: Raw Numbers]
    
    style W fill:#ffd700,stroke:#333,stroke-width:4px
```
Data Understanding: Assessing the 5 Vs of Big Data (Volume, Velocity, Variety, Veracity, and Value).
```mermaid
mindmap
  root((5 Vs of Big Data))
    Volume
      Massive Scale
      Storage Needs
    Velocity
      Streaming Data
      Real-time Processing
    Variety
      Unstructured
      Semi-structured
      Structured
    Veracity
      Data Quality
      Trustworthiness
      Cleanliness
    Value
      ROI
      Business Insights
      Actionability

```
Feature Engineering: Applying human ingenuity to create new variables (e.g., "Debt-to-Income ratio") that help models see patterns they would otherwise miss.

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
    
2. Data Classification
Understanding data types is the first step in selecting the correct statistical tool:

Categorical (Nominal/Ordinal): Used for identification and ranking.

Numerical (Discrete/Continuous): Used for counting and precise measuring.

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

Objective: Validate assumptions across five scenarios (Price, Productivity, Market Research, QC, and Product Lines).
Implementation: Used scipy.stats to separate "signal" from "noise" by interpreting $p$-values against a significance level ($\alpha$) of 0.05.

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
---
### Activity 2.2.3: Interpreting Correlation

Objective: Analyze lifestyle impacts (BMI, children) on medical insurance costs.

Implementation: Evaluated Pearson vs. Spearman to account for outliers and non-linear trends.

Insight: Identified confounding variables (like Age) to avoid the "Correlation implies Causation" fallacy.


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
---
### 📈 Activity 2.3.5: Building Predictive Models
Objective: Predict customer loyalty for a national retailer.
Implementation: Built a Multiple Linear Regression model using statsmodels and scikit-learn.
Evaluation: Optimized the model by minimizing RSS and analyzing Adjusted $R^2$ to prevent overfitting.

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

Homoscedasticity: Verified constant variance in residuals to ensure consistent prediction accuracy.
Central Limit Theorem: Leveraged the CLT to ensure that sample means follow a normal distribution, allowing for valid inference.
Risk Assessment: Evaluated Sensitivity vs. Specificity trade-offs to balance between missing positives and raising false alarms.

* **Homoscedasticity:** Verified constant variance in residuals to ensure consistent prediction accuracy.
* **Multicollinearity:** Screened independent variables to ensure they were not redundant.
* **Prediction Intervals:** Provided a range for new observations to account for individual variability.

---

## Technologies Used

* **Language:** Python 3.x
* **Libraries:** `Pandas`, `NumPy`, `Matplotlib`, `Seaborn`, `Scipy.stats`, `Statsmodels`, `Scikit-Learn`
* **Documentation:** Mermaid.js, Markdown

