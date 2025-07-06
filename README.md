# 🏦 Loan Approval Prediction - End-to-End Machine Learning Project

This project is a complete **End-to-End Machine Learning pipeline** that predicts whether a loan application will be approved based on customer data. It covers everything from **data ingestion** to **deployment with Streamlit**.

---

## 🚀 Project Overview

This project demonstrates a full ML workflow:
1. **Data Ingestion** → Load and split the dataset.
2. **Data Preprocessing & Transformation** → Handle missing values, encode categorical data, and scale features.
3. **Model Training** → Train and evaluate multiple models.
4. **Model Evaluation** → Select the best model based on performance metrics.
5. **Model Deployment** → Build a Streamlit web app for predictions.

>📝 Initial Exploratory Data Analysis (EDA) and basic preprocessing were done using Jupyter Notebook for better visualization and understanding of the dataset.



---

## 📂 Project Structure
```
├── src/
│   ├── components/
│   │   ├── ingestion.py           # Data Ingestion Module
│   │   ├── transformation.py      # Data Transformation Module 
│   │   ├── trainer.py             # Model Trainer Module
│   │   ├── evaluate.py            # Model Evaluation Module
│   │   └── utils.py               # Utility Functions (save/load objects)
│   ├── exception.py               # Custom Exception Handling
│   ├── logger.py                  # Logging Configuration
│
├── artifacts/                     # Saved Models & Preprocessors
│   └── (model.pkl, processor.pkl, etc.)
│
├── logs/                          # Log Files
│   └── (log files)
│
├── app.py                         # Main Execution Script (Training Pipeline)
│
├── streamlit_app.py               # Streamlit App for Prediction
│
├── README.md                      # Project Documentation
│
└── requirements.txt               # Project Dependencies 


```

## 📊 Dataset Info
- The dataset contains loan applications with features like:
  - Applicant Income
  - Coapplicant Income
  - Loan Amount
  - Loan Term
  - Credit History
  - Gender, Marital Status, etc.

- **Target Variable:** `Loan_Status`
  - `Y` → Loan Approved
  - `N` → Loan Not Approved

---

## ✅ Models Used
- Logistic Regression  
- Decision Tree  
- Random Forest  
- K-Nearest Neighbors  
- AdaBoost  
- Gradient Boosting  
- XGBoost  
- CatBoost  

> The best model is selected based on **Accuracy** and **F1 Score**.

---
## ⚙️ How to Run

### 1. Install Requirements

```bash
pip install -r requirements.txt
---
```

📬 Contact
Author: Mohamed Nasser Abohamda

LinkedIn: www.linkedin.com/in/mohamed-hagag-a117682a7

GitHub: [MohamedNHagag](https://github.com/MohamedNHagag)

Email: hagag9868@gmail.com

