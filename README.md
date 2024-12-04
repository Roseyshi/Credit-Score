# **Credit Scorecard Project**

### **Table of Contents**
1. Project Overview
2. Features
3. Technologies Used
4. Installation
5. Usage
6. Data
7. Model
8. Evaluation
9. Future Enhancements
10. Contributing
11. Contact

### **Project Overview**
**BUSINESS PROBLEM:**

A credit company currently faces a high risk of loan defaults, which directly impacts profitability and increases operational costs associated with debt recovery. Many customers who are approved for credit loans may not have the financial stability or creditworthiness to manage debt effectively, leading to missed payments and default. The company needs a robust way to evaluate applicants’ eligibility for credit loans to reduce the likelihood of default and ensure that only financially responsible customers are approved.

**BUSINESS OBJECTIVES:**
1. Minimize Loan Default Rates: Implement a data-driven model to predict and identify high-risk customers likely to default on loans, thereby reducing the overall loan default rate.
2. Improve Loan Eligibility Assessment: Develop a systematic method for assessing creditworthiness by using key financial and behavioral indicators (such as outstanding debt, credit history, income level, and payment behavior) to make more accurate loan approval decisions.

3. Enhance Profitability through Risk Management: By approving loans primarily for customers with strong credit profiles, the company can decrease losses due to defaults and increase profitability.

4. Increase Customer Retention of Low-Risk Borrowers: Retain and attract low-risk customers by offering favorable loan terms to those who demonstrate financial responsibility, thereby improving customer loyalty and satisfaction among reliable borrowers.

5. Support Financial Health of Borderline Customers: Provide resources or alternative loan products for borderline customers who are not immediately eligible for standard loans. This could include smaller loans or financial education programs to help these customers improve their creditworthiness, creating a pipeline of future eligible customers.

**DATA UNDERSTANDING:**
1. Identification Columns: ID, Customer_ID: Unique identifiers for records and customers, likely strings.

2. Demographic Information: Name, Age, SSN, Occupation: Descriptive attributes about customers. Financial and Credit Attributes:

3. Income Inofrmation: Annual_Income, Monthly_Inhand_Salary, Num_Bank_Accounts, Num_Credit_Card: Count of banking products, possibly integers. Interest_Rate, Outstanding_Debt, Credit_Utilization_Ratio: Financial metrics, potentially floats. Num_of_Loan, Type_of_Loan: Loan-related info, with Type_of_Loan listing loan types.

4. Behavioral and Payment Information: Delay_from_due_date, Num_of_Delayed_Payment, Changed_Credit_Limit, Num_Credit_Inquiries: Indicators of payment history and credit management. Payment_Behaviour, Payment_of_Min_Amount: Details on payment patterns, possibly strings or categories. Monthly_Balance, Total_EMI_per_month, Amount_invested_monthly: Monthly financial metrics, possibly floats.

5. The source of the data is Kaggle through their website https://www.kaggle.com/datasets

### **Features**
1. **Predictive Model**: Uses machine learning to predict credit scores.
2. **Data Preprocessing**: Includes handling missing data, outliers, and scaling features.
3. **Model Explainability**: Provides insights into the model's decisions using feature importance.
4. **Performance Metrics**: Accuracy, Precision, Recall, F1-Score, and AUC-ROC.

### **Technologies Used**
1. Programming Language: Python 3.13
2. Libraries:
3. Pandas
4. NumPy
5. Scikit-learn
6. XGBoost
7. Matplotlib & Seaborn for visualization

  
### **Data**
The dataset includes anonymized financial information with features like income, credit history, debt, and other personal details.
![image](https://github.com/user-attachments/assets/45aaa2f7-6bde-4815-9ca2-0835ef53d7da)
Most of the customers have a standard credit mix. However ~20000 individuals have credit mixes whose information may either be ambiguous, 
inconsistent or not enough data to determine their where thy fall. We keep this in mind.

![image](https://github.com/user-attachments/assets/10cf1c30-40b7-4714-b471-d1161696c51b)
The customers have an average of 1300 of outstanding debt regardless of occupation.


### **Model**
The model uses [e.g., Logistic Regression, Decision Trees, XGBoost] to predict credit scores. Hyperparameter tuning and cross-validation ensure optimal performance.

### **Evaluation**
The model is evaluated using various performance metrics to ensure its reliability and accuracy. Confusion matrix, ROC curve, and classification reports are generated.
![image](https://github.com/user-attachments/assets/7014d382-e98d-444c-930e-68c4d8b3c6a9)


### **Results:**
![image](https://github.com/user-attachments/assets/5814f037-1087-4524-9b84-f70d8773a292)


### **Future Enhancements**
Incorporate more diverse datasets for robustness.
Implement deep learning models.
Develop a user-friendly web interface for real-time credit scoring.
Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

### **Contact**
For any inquiries, please contact:
wahomeshiko@gmail.com 
