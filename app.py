!pip install streamlit
!pip install joblib

import streamlit as st
import joblib

# Load model
model = joblib.load('credit_model.pkl')

# App title
st.title("Credit Score Prediction App")

# Input fields
feature1 = st.number_input("Outstanding_Debt")
feature2 = st.number_input("Credit_Mix")
feature3 = st.number_input("Credit_History_Age_in_months")
feature4 = st.number_input("Monthly_Balance")
feature5 = st.number_input("Paymnet_Behaviour")
feature6 = st.number_input("Annual_Income")
feature7 = st.number_input("Number_of_Delayed_Payment")



if st.button("Predict"):
    prediction = model.predict([[feature1, feature2, feature3, feature4, feature5, feature6, feature7]])
    st.write(f"Predicted Class: {data.target_names[prediction[0]]}")
