## **Credit Score Card Project**
**Overview**
This project focuses on developing a machine learning model to predict a borrower's credit score based on historical financial and demographic data. The model aims to assist financial institutions in assessing the creditworthiness of applicants, reduce loan default risks, and streamline the credit approval process.

**Table of Contents**
1. Introduction
2. Features
3. Technologies Used
4. Setup and Installation
5. Usage
6. Model Performance
7. Results
   

**Introduction**

The objective of this project is to build a credit score prediction system using machine learning. Credit scores are vital for lenders to evaluate a borrower's ability to repay loans. The model uses various features such as income, loan history, credit mix, and debt-to-income ratio to classify applicants into creditworthiness categories.


**Problem Statement**

Financial institutions often struggle to accurately predict loan default risks due to data inconsistency and inadequate scoring systems. This project addresses these challenges by leveraging machine learning techniques to build a robust and scalable credit scoring model.


**Features**
The project uses the following features (columns from the dataset):

1. Age: Age of the applicant.
2. Income: Monthly income.
3. Credit Mix: Types of credit accounts held (e.g., secured, unsecured).
4. Loan History: Duration of previous loans.
5. Outstanding Debt: Total unpaid debt.
6. Credit History: Whether the applicant defaulted on loans in the past.
7. Number of loans
8. Occupation
9. Monthly balance
10. Amount invested monthly.
11. Annual income
12. Payment behaviour
13. Delay from due date
14. Interest rate
15. Type of loan: Different customers are currently repaying different loans.
16. Credit score: This is the target column that determines credibility of a customer.

**Methods Used**

1. Inferential Statistics.
2. Machine learning.
3. Data visualization.
4. Predictive modelling.


**Technologies Used**
1. Programming Language: Python
2. Libraries:Pandas and NumPy for data manipulation and analysis, Matplotlib and Seaborn for data visualization, Scikit-learn for machine learning model building.
3. XGBoost for advanced boosting techniques

**Usage**
1. Prepare the Dataset.

2. Place the dataset in the data/ directory.
Ensure the file is named credit_data.csv (or update the script to match your filename).
Run the Notebook:

3. Open the credit_score_card.ipynb file.
Follow the instructions in the notebook to preprocess the data, train models, and evaluate performance.
Visualize Results:

4. Use the EDA section to explore data insights.
View the heatmap and feature importance graphs.

**Model Performance**
The following metrics were used to evaluate the model:
Accuracy: 85%
Precision: 83%
Recall: 81%
F1-Score: 82%
AUC-ROC: 0.90
Performance metrics are visualized through a confusion matrix, classification report, and ROC curve.

**Results**
The model successfully classifies applicants into creditworthiness categories (e.g., "Good," "Average," "Bad").
Key Insights:
Income and credit mix are the strongest predictors of credit score.
Applicants with a higher debt-to-income ratio have a higher likelihood of default.
