import streamlit as st
import joblib
import pandas as pd


model=joblib.load(r'D:\data science\7)machine learning\projects\classfication logistic & SVM\3)loan\loanokl.pkl')

st.title('Loan Status 🏦')
st.sidebar.info("input Values to check Loan status")
st.header('This model prediction loan status')

Gender=st.sidebar.text_input('Gender')
Married=st.sidebar.text_input('Married')
Dependents=st.sidebar.text_input('Dependents')
Education=st.sidebar.text_input('Education')
Self_Employed=st.sidebar.text_input('Self_Employed')
ApplicantIncome=st.sidebar.text_input('ApplicantIncome')
CoapplicantIncome=st.sidebar.text_input('CoapplicantIncome')
LoanAmount=st.sidebar.text_input('LoanAmount')
Loan_Amount_Term=st.sidebar.text_input('Loan_Amount_Term')
Credit_History=st.sidebar.text_input('Credit_History')
Property_Area=st.sidebar.text_input('Property_Area')

df = pd.DataFrame({
    'Gender': [Gender],
    'Married': [Married],
    'Dependents': [Dependents],
    'Education': [Education],
    'Self_Employed': [Self_Employed],
    'ApplicantIncome': [float(ApplicantIncome)],
    'CoapplicantIncome': [float(CoapplicantIncome)],
    'LoanAmount': [float(LoanAmount)],
    'Loan_Amount_Term': [float(Loan_Amount_Term)],
    'Credit_History': [float(Credit_History)],
    'Property_Area': [Property_Area]
},index=[0])

button_confirm=st.sidebar.button('confirm')
if button_confirm:
    prediction = model.predict(df)
    if prediction[0] == 0:
        st.error("❌ We regret to inform you that your loan application has not been accepted at this time.")
    else:
        st.success("🎉 Congratulations! Your loan application has been successfully accepted.")
