import streamlit as st
import pickle

# Load the model
with open('credit_model.pkl', 'rb') as f:
    rf = pickle.load(f)

# Use 'rf' for predictions in your Streamlit app
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
    prediction = rf.predict([[feature1, feature2, feature3, feature4, feature5, feature6, feature7]])
    st.write(f"Predicted Class: {data.target_names[prediction[0]]}")
