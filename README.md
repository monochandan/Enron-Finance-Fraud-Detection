# Financial Fraud Detection Using the Enron Email Dataset

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python\&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikit-learn\&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

## 📌 Overview

This project explores the use of **machine learning for detecting potentially fraudulent activities in financial data** using the **Enron Email Dataset**.

The project is motivated by the Enron scandal, one of the major corporate scandals in history, which involved fraudulent financial activities including hiding debts and inflating reported earnings. The scandal ultimately resulted in the company's bankruptcy and criminal charges against several executives.

The objective is to analyze the available financial and email-related information, engineer useful features, build classification models, and evaluate their ability to identify fraudulent activity.

---

## 🎯 Objectives

The main objectives of this project are:

* Perform exploratory data analysis (EDA)
* Clean and preprocess the dataset
* Engineer relevant features
* Select informative features for classification
* Build machine learning models for fraud detection
* Compare model performance
* Tune model hyperparameters
* Evaluate models using appropriate classification metrics
* Explore possible approaches for future real-time fraud detection

These objectives follow the project framework provided in the original project specification.

---

## 📊 Dataset

The project uses the **Enron Email Dataset**, which contains information related to email exchanges and financial information associated with Enron employees.

The financial data includes information such as:

* Company earnings
* Stock values
* Executive compensation
* Total payments
* Email-related information

The dataset was made publicly available following the Enron scandal and is also referenced as being available through Kaggle.

> **Note:** The project documentation states that the dataset used for the implementation contains **146 records**.

---

## 🔬 Methodology

The project follows a standard machine learning workflow.

### 1. Data Loading and Preprocessing

The dataset is loaded into a Pandas DataFrame and prepared for analysis.

Preprocessing includes:

* Handling missing values
* Removing irrelevant data
* Removing unnecessary columns
* Scaling data where appropriate
* Preparing the data for machine learning

### 2. Feature Engineering

Relevant features are extracted and new features are created from existing information.

Examples include:

* Number of emails sent
* Number of emails received
* Total payments
* Total stock value
* Other potentially relevant financial and email-related characteristics

The purpose is to capture information that may help distinguish fraudulent from non-fraudulent activity.

### 3. Exploratory Data Analysis

EDA is performed to understand the structure and characteristics of the dataset.

The analysis includes:

* Feature distributions
* Correlations
* Patterns and anomalies
* Statistical analysis
* Visualization of relevant variables

### 4. Model Selection

Several classification algorithms are considered, including:

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier

The dataset is divided into training and testing sets, and the models are evaluated using classification metrics.

### 5. Hyperparameter Tuning

Model hyperparameters can be optimized using cross-validation to identify configurations that provide better performance.

Possible approaches include:

* Grid Search
* Randomized Search
* Bayesian Optimization

### 6. Model Evaluation

The models are evaluated using metrics including:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix
* ROC Curve
* ROC-AUC

## For imbalanced classification problems, additional metrics such as PR-AUC can also be considered.

## 🛠️ Technologies Used

| Technology   | Purpose                         |
| ------------ | ------------------------------- |
| Python       | Programming language            |
| Pandas       | Data loading and manipulation   |
| NumPy        | Numerical computation           |
| Matplotlib   | Data visualization              |
| Seaborn      | Statistical visualization       |
| Scikit-learn | Machine learning and evaluation |

The project documentation specifically identifies Pandas, NumPy, Matplotlib, Seaborn, and Scikit-learn as the primary libraries used.

---

## 📁 Project Workflow

```text
Enron Dataset
      │
      ▼
Data Loading
      │
      ▼
Data Cleaning & Preprocessing
      │
      ▼
Feature Engineering
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Feature Selection
      │
      ▼
Model Training
      │
      ├── Logistic Regression
      ├── Decision Tree
      └── Random Forest
      │
      ▼
Hyperparameter Tuning
      │
      ▼
Model Evaluation
      │
      ▼
Fraud Detection
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the project

Run the main Python script or notebook included in the repository.

```bash
python code.py
```

---

## 📈 Evaluation

The project evaluates classification models using metrics such as:

* **Accuracy** — overall proportion of correct predictions
* **Precision** — proportion of predicted fraudulent cases that are actually fraudulent
* **Recall** — proportion of fraudulent cases correctly identified
* **F1-score** — balance between precision and recall
* **ROC-AUC** — ability of the classifier to distinguish between classes

For imbalanced datasets, precision, recall, F1-score, ROC-AUC, and PR-AUC are particularly useful evaluation measures.

---

## 🔮 Future Work

Several improvements could be explored in future versions of the project.

### Advanced Feature Engineering

Additional features could be extracted from:

* Email content
* Email frequency
* Email recipients
* Financial relationships
* Domain-specific information

These features may provide additional signals for fraud detection.

### Improved Data Preprocessing

Future work could investigate:

* Outlier detection
* Outlier removal
* Data normalization
* Data transformation
* Improved feature scaling

### Additional Machine Learning Models

Other algorithms could be investigated, including:

* Support Vector Machines
* Naïve Bayes
* Gradient Boosting
* Neural Networks

Their performance could be compared with the existing models.

### Real-Time Fraud Detection

A future version could implement a real-time fraud detection system by deploying the model through a cloud platform and integrating it with an email system.

A REST API could also be used to make predictions available to web or mobile applications.

### Larger Dataset

The current dataset is relatively small. Testing the system on a larger dataset could improve the assessment of model generalizability and robustness.

---

## 📚 Project Deliverables

The original project specification identifies the following deliverables:

* Data analysis and feature engineering report
* Machine learning model for fraud detection
* Presentation of findings
* Recommendations for further development

---

## 📄 License

This project is licensed under the **MIT License**.

See the [`LICENSE`](LICENSE) file for details.

---

## 👤 Author

**monochandan**

GitHub: [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)

---

## ⚠️ Disclaimer

This project is intended for **educational and research purposes**. The model should not be considered a production-ready financial fraud detection system without additional validation, testing on larger datasets, and appropriate domain-specific evaluation.
