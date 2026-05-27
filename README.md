\# 💳 Financial Fraud Detection Using Machine Learning



\## 📌 Project Overview

This project focuses on detecting fraudulent financial transactions using Machine Learning techniques. The system analyzes transaction-related features and predicts whether a transaction is fraudulent or normal.



The project also includes data visualization and an interactive dashboard built using Streamlit.



\---



\## 🎯 Objectives

\- Detect fraudulent transactions automatically

\- Handle imbalanced datasets using SMOTE

\- Compare multiple machine learning models

\- Visualize fraud patterns using graphs and dashboard



\---



\## 📂 Dataset Information

The dataset contains around 50,000 transaction records with features such as:



\- Transaction Amount

\- Transaction Type

\- Account Balance

\- Device Type

\- Location

\- Merchant Category

\- Card Type

\- Daily Transaction Count

\- Fraud Label



\### Target Variable

\- `0` → Normal Transaction

\- `1` → Fraudulent Transaction



\---



\## ⚙️ Technologies Used



\### Programming Language

\- Python



\### Libraries

\- Pandas

\- NumPy

\- Matplotlib

\- Scikit-learn

\- Imbalanced-learn (SMOTE)

\- XGBoost

\- Streamlit



\---



\## 🧹 Data Preprocessing

The following preprocessing steps were performed:



\- Data cleaning

\- Encoding categorical features

\- Feature engineering

\- Handling missing values

\- SMOTE for class balancing



Additional features created:

\- Hour

\- Day

\- Month



\---



\## 🤖 Machine Learning Models Used



\### 1. Logistic Regression

Used as the baseline classification model.



\### 2. Random Forest

Used to improve performance and reduce overfitting.



\### 3. XGBoost

Used for advanced boosting and better fraud detection accuracy.



\---



\## 📊 Evaluation Metrics

Models were evaluated using:



\- Accuracy

\- Precision

\- Recall

\- F1-score

\- Confusion Matrix

\- Learning Curve



\---



\## 📈 Visualizations

The project includes:

\- Fraud vs Normal Pie Chart

\- Fraud by Location Bar Chart

\- Learning Curves

\- Confusion Matrix Graphs

\- Dashboard Visualizations



\---



\## 🖥️ Streamlit Dashboard

An interactive dashboard was created using Streamlit to visualize fraud patterns and model insights.



\### Run Dashboard

```bash

streamlit run dashboard.py

```



\---



\## 🚀 Project Structure



```text

financial-fraud-detection/

│

├── fraud\_detection.ipynb

├── dashboard.py

├── cleaned\_fraud\_data.csv

├── requirements.txt

├── README.md

├── learning\_curve.png

├── confusion\_matrix.png

```



\---



\## 🔥 Key Features

\- Fraud detection using ML

\- SMOTE for imbalance handling

\- Multiple model comparison

\- Interactive dashboard

\- Data visualization



\---



\## 📌 Future Improvements

\- Real-time fraud detection

\- Deep learning implementation

\- API deployment

\- Better feature engineering



\---



\## ✅ Conclusion

This project demonstrates how Machine Learning can be used for financial fraud detection. Random Forest and XGBoost showed better performance compared to Logistic Regression. Proper preprocessing and SMOTE significantly improved fraud detection capability.



\---



\## 👨‍💻 Author

Piu De



