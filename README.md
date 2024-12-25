## AI-Powered-Personal-Finance-Planner

---

![Python](https://img.shields.io/badge/Python-3.9-blue.svg)  
![Build]([![Build](https://img.shields.io/github/actions/workflow/status/benefoon/AI-Powered-Personal-Finance-Planner/ci-cd.yml?branch=main)](https://github.com/benefoon/AI-Powered-Personal-Finance-Planner/actions)
)

---

## **AI Finance Planner**

An intelligent system designed to help individuals and organizations analyze, predict, and optimize financial transactions and patterns using state-of-the-art machine learning models and visualization techniques.

---

## **Project Objectives**

🔹 Provide intelligent recommendations for financial decisions.  
🔹 Detect spending anomalies for budgeting and security purposes.  
🔹 Visualize and analyze spending habits interactively.  
🔹 Offer modular and extensible features for data processing and analysis.  

---

## **Key Features**

| Feature                     | Description                                                                                     |
|-----------------------------|-------------------------------------------------------------------------------------------------|
| 📊 **Data Cleaning**         | Processes raw transaction data, handling missing values and anomalies.                         |
| ✨ **Feature Engineering**   | Extracts insights such as spending patterns, transaction categories, and seasonal trends.       |
| 🤖 **Machine Learning**      | Builds predictive models for categorization, fraud detection, and forecasting.                 |
| 📈 **Interactive Dashboard** | Visualizes financial trends and allows users to explore data interactively.                   |
| 🔍 **Anomaly Detection**     | Identifies unusual spending behaviors using advanced machine learning techniques.              |

---

## **Repository Structure**

```plaintext
AI-Finance-Planner/
├── data/                      # Data storage and processing
│   ├── raw/                   # Raw transaction data files
│   ├── processed/             # Processed and cleaned data files
│   ├── cleaning.py            # Script for data cleaning
│   ├── structures.py          # Functions to define and manipulate data structures
├── notebooks/                 # Jupyter Notebooks for exploratory data analysis and model development
│   ├── 01_data_cleaning.ipynb # Cleaning and preprocessing data
│   ├── 02_feature_engineering.ipynb # Feature extraction and transformation
│   ├── 03_modeling.ipynb      # Building ML models
│   ├── 04_dashboard.ipynb     # Designing dashboard
├── src/                       # Source code for the project
│   ├── data_cleaning.py       # Data cleaning scripts
│   ├── feature_engineering.py # Feature engineering scripts
│   ├── ml_model.py            # ML models
│   ├── anomaly_detection.py   # Anomaly detection logic
│   ├── dashboard.py           # Dashboard backend
│   ├── utils.py               # Utility functions
├── tests/                     # Automated tests
│   ├── test_data_cleaning.py  # Tests for data cleaning
│   ├── test_feature_engineering.py # Tests for feature engineering
│   ├── test_ml_model.py       # Tests for ML models
├── dashboards/                # Dashboard design files
│   ├── templates/             # HTML templates for the dashboard
│   ├── static/                # Static CSS/JS files
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Docker configuration
├── .github/                   
│   ├── workflows/             # CI/CD workflows
│       ├── main.yml
├── README.md                  # Project documentation
└── setup.py                   # Project setup script
```

---

## **Data and Structures**

### **Data Cleaning**
The `data/cleaning.py` script provides robust functionality for cleaning raw financial data. It includes:  
- Handling missing values using forward fill.  
- Removing outliers based on quantile thresholds.

### **Structures**
The `data/structures.py` script introduces reusable and modular structures for managing transaction data:  
- **TransactionRecord**: A class or dictionary-based structure for individual transactions.  
- **DataPipeline**: Functions for integrating data cleaning and feature engineering.  

---

## **Installation**

1. Clone the repository:  
   ```bash
   git clone https://github.com/username/AI-Finance-Planner.git
   cd AI-Finance-Planner
   ```

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

3. Run data preprocessing:  
   ```bash
   python data/cleaning.py
   ```

4. Execute feature engineering:  
   ```bash
   python src/feature_engineering.py
   ```

5. Train machine learning models:  
   ```bash
   python src/ml_model.py
   ```

6. Launch the dashboard:  
   ```bash
   python src/dashboard.py
   ```

---

## **Usage Workflow**

### 1️⃣ Data Cleaning  
Execute the `01_data_cleaning.ipynb` notebook or use `data/cleaning.py` to preprocess raw financial data.  

### 2️⃣ Feature Engineering  
Run `02_feature_engineering.ipynb` or `src/feature_engineering.py` to extract insights and prepare data for analysis.  

### 3️⃣ Structures Integration  
Use the `data/structures.py` to define and manage reusable data structures.  

### 4️⃣ Model Development  
Utilize `03_modeling.ipynb` or `src/ml_model.py` to train predictive models for categorizing transactions and forecasting trends.  

### 5️⃣ Anomaly Detection  
Use `src/anomaly_detection.py` to identify unusual spending patterns.

### 6️⃣ Interactive Dashboard  
Launch the `dashboard.py` to visualize financial insights interactively.

---

## **Technologies Used**

| Category          | Technologies                                                                                         |
|-------------------|-----------------------------------------------------------------------------------------------------|
| **Programming**   | Python (Pandas, NumPy, Scikit-learn, Flask)                                                         |
| **Visualization** | Matplotlib, Seaborn, Plotly                                                                         |
| **Infrastructure**| Docker, GitHub Actions for CI/CD                                                                    |
| **Machine Learning** | Isolation Forest, Random Forest Classifier                                                       |

---

## **Screenshots**

| Dashboard View                  | Model Training Workflow               |
|---------------------------------|---------------------------------------|
| ![Dashboard Overview](https://github.com/benefoon/AI-Powered-Personal-Finance-Planner/blob/main/screenshots/dashboard_mock.png) | ![Data Flow Architecture]([https://github.com/benefoon/AI-Powered-Personal-Finance-Planner/blob/main/screenshots/architecture_mock.png]) |

---

## **References**

1. [Scikit-learn Documentation](https://scikit-learn.org/stable/)  
2. [Pandas Documentation](https://pandas.pydata.org/docs/)  
3. [Matplotlib Documentation](https://matplotlib.org/stable/index.html)  
