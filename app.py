import streamlit as st
import pickle

# Load model using pickle
with open('credit_model.pkl', 'rb') as f:
    model = pickle.load(f)

# App title
st.title("Credit Score Prediction App")

# Input fields
feature1 = st.number_input("Outstanding Debt")
feature2 = st.number_input("Credit Mix")
feature3 = st.number_input("Credit History Age (in months)")
feature4 = st.number_input("Monthly Balance")
feature5 = st.number_input("Payment Behaviour")
feature6 = st.number_input("Annual Income")
feature7 = st.number_input("Number of Delayed Payments")

if st.button("Predict"):
    prediction = model.predict([[feature1, feature2, feature3, feature4, feature5, feature6, feature7]])
    st.write(f"Predicted Class: {prediction[0]}")

