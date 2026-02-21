
# Data Science Portfolio: Statistical Methods & Predictive Modeling

> **Weeks 1 & 2: From Business Alignment to Evidence-Based Decision Making**

## Project Overview

This repository documents a complete data science workflow. It transitions from the strategic planning of **Week 1** (CRISP-DM, Data Maturity, and Feature Engineering) to the mathematical execution of **Week 2** (Hypothesis Testing, Correlation, and Regression). The goal is to move beyond "gut feeling" and use mathematical rigor to validate assumptions, identify patterns, and predict future outcomes.

## 🛠️ Skills Demonstrated

* **Strategic Planning:** CRISP-DM lifecycle, 5 Whys Root Cause Analysis, and DIKW Pyramid.
* **Hypothesis Testing:** -tests, ANOVA, and Chi-Square analysis.
* **Correlation:** Pearson () and Spearman () coefficients for relationship mapping.
* **Regression:** Simple and Multiple Linear Regression using OLS (Ordinary Least Squares).
* **Model Evaluation:** Interpreting , Adjusted , and RSS (Residual Sum of Squares).
* **Risk Assessment:** Evaluating Sensitivity vs. Specificity and Prediction Intervals.

---

## Week 1: Strategic Foundations

### 1. The CRISP-DM Framework

Before touching code, I utilize the **CRISP-DM** lifecycle to ensure technical work solves a real business problem.

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

### 2. Business Logic & Data Understanding

* **DIKW Pyramid:** Defining the "Wisdom" required for action.

```mermaid
graph TD
    W[Wisdom: Strategic Action] --- K[Knowledge: Why it happened]
    K --- I[Information: Context/Trends]
    I --- D[Data: Raw Numbers]
    style W fill:#ffd700,stroke:#333,stroke-width:4px

```

* **The 5 Vs:** Assessing Volume, Velocity, Variety, Veracity, and Value.

```mermaid
mindmap
  root((5 Vs of Big Data))
    Volume
      Massive Scale
    Velocity
      Real-time Processing
    Variety
      Unstructured/Structured
    Veracity
      Data Quality
    Value
      ROI/Insights

```

* **Feature Engineering:** Applying human ingenuity to create variables that help models see hidden patterns.

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

### 3. Data Classification

Understanding data types is the first step in selecting the correct statistical tool.

```mermaid
graph TD
    Data[Data Types] --> Cat[Categorical / Qualitative]
    Data --> Num[Numerical / Quantitative]
    Cat --> Nom[Nominal]
    Nom -- Example --> Eye[Eye Color, Gender]
    Cat --> Ord[Ordinal]
    Ord -- Example --> Rank[Survey Ratings]
    Num --> Disc[Discrete]
    Disc -- Example --> Count[Employee Count]
    Num --> Cont[Continuous]
    Cont -- Example --> Meas[Revenue, Time]
    style Cat fill:#e1f5fe,stroke:#01579b
    style Num fill:#fff3e0,stroke:#e65100

```

---

## Master Decision Logic Flow

This framework is used throughout the activities to select the appropriate statistical test.

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

* **Objective:** Validate assumptions across scenarios (Price, Productivity, Market Research, QC, and Product Lines).
* **Technical Implementation:** Utilized `scipy.stats` to perform t-tests and ANOVA.
* **Key Insight:** Separated "signal" from "noise" by interpreting -values against .

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

* **Objective:** Analyze lifestyle impacts (BMI, children) on medical insurance costs.
* **Technical Implementation:** Computed Pearson and Spearman coefficients; visualized relationships via Seaborn.

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

* **Objective:** Predict customer loyalty based on product quality and brand awareness.
* **Technical Implementation:** Built a Multiple Linear Regression model using `statsmodels`.
* **Business Impact:** Provided coefficient-based insights (e.g., "A 1-unit increase in quality yields a specific increase in loyalty").

```mermaid
graph TD
    Features[Quality, Awareness, Satisfaction] --> Model[Multiple Linear Regression]
    Model --> Coeff[Interpret Coefficients]
    Model --> Fit{Evaluate Fit}
    Fit -- "R-Squared" --> Stats[Explain % of Variance]
    Fit -- "RSS" --> Stats[Quantify Unexplained Error]
    Stats --> Assumptions{Check Residuals}
    Assumptions -- "Random Scatter" --> Valid[Model Reliable]

```

---

## 🔍 Assumption & Diagnostic Checks

### 1. Model Diagnostic Flow

```mermaid
graph TD
    Model[Trained Regression Model] --> Check1{Homoscedasticity}
    Check1 -- "Residual Plot" --> Check2{Multicollinearity}
    Check2 -- "VIF Analysis" --> Check3{Normality}
    Check3 -- "Q-Q Plot / CLT" --> Check4{Risk Assessment}
    Check4 --> Sens[Sensitivity vs Specificity]
    Check4 --> PI[Prediction Intervals]
    Sens --> Final[Reliable Business Insight]

```

### 2. Normality & CLT

* **Central Limit Theorem:** Leveraged the CLT to ensure sample means follow a normal distribution, allowing for valid inference.
<img width="458" height="361" alt="image" src="https://github.com/user-attachments/assets/f1f4efa1-9626-45e3-8f11-9aaceb70fd3d" />


```mermaid
graph LR
    Pop[Messy Population] --> Samples[Take 1000s of Samples]
    Samples --> Means[Calculate Mean of each]
    Means --> Dist[Normal Distribution of Means]
    style Dist fill:#f9f,stroke:#333,stroke-width:2px

```

### 3. Multicollinearity & Risk

* **VIF Screening:** Screened independent variables to ensure they were not redundant.

```mermaid
graph TD
    X1[Feature A] --- Correlated((High Correlation))
    X2[Feature B] --- Correlated
    Correlated --> Issue[Unstable Coefficients]
    Issue --> Fix[Drop one Feature]

```

* **Homoscedasticity:** Verified constant variance in residuals.
* **Sensitivity vs. Specificity:** Balanced catching "truth" vs. avoiding "false alarms."

```mermaid
graph LR
    subgraph "Sensitivity"
    TP[True Positives]
    FN[False Negatives]
    end
    subgraph "Specificity"
    TN[True Negatives]
    FP[False Positives]
    end
    TP -.-> Tradeoff{The Balance}
    FP -.-> Tradeoff

```

### 4. Prediction Intervals

Provided a range for individual variability, distinct from population averages.

Prediction vs. Confidence Intervals Logic
This diagram explains why one is wider than the other and when to use each for business decisions.

```mermaid
graph TD
    A[Regression Model Prediction] --> B{What are you<br/>predicting?}
    
    B -- "The Average Group Outcome" --> C[Confidence Interval - CI]
    B -- "A Specific Single Case" --> D[Prediction Interval - PI]
    
    subgraph "Uncertainty Components"
    C --- C1[Model Estimation Error]
    D --- D1[Model Estimation Error]
    D --- D2[Individual Data Noise / Variance]
    end
    
    subgraph "Visual Characteristics"
    C2[Narrower Band]
    D3[Significantly Wider Band]
    end
    
    C1 --> C2
    D1 --> D3
    D2 --> D3
    
    subgraph "Business Use Case"
    C3["Strategic Planning:<br/>'What is the average ROI?'"]
    D4["Risk Assessment:<br/>'What will THIS customer spend?'"]
    end
    
    C2 --> C3
    D3 --> D4

    style C fill:#e1f5fe,stroke:#01579b
    style D fill:#fff3e0,stroke:#e65100
    style D3 stroke-width:4px
```

Visual Representation Guide
When you look at a regression plot:

Confidence Interval (CI): Think of this as the "wiggle room" of the best-fit line itself. If you ran the experiment again, the line might move slightly; the CI shows where the mean line likely stays.

Prediction Interval (PI): Think of this as the "Scatter Zone." It covers nearly all your data points. It is wider because even if you have the perfect line, individual people/events are unpredictable and "noisy."
---

## Technologies Used

* **Language:** Python 3.x
* **Libraries:** `Pandas`, `NumPy`, `Matplotlib`, `Seaborn`, `Scipy.stats`, `Statsmodels`, `Scikit-Learn`
* **Documentation:** Mermaid.js, Markdown
