import streamlit as st
import pickle
import pandas as pd


# Load trained model
model = pickle.load(open("finalized_model.sav", "rb"))

# App title
st.title("Salary Prediction Using (Simple Linear Regression)")

st.write("Enter the Year's of Experience to predict Salary.")

# User Inputs
Exp = st.number_input("Year's of Experience", min_value=0.1, max_value=80.0, value=1.0)


# Prediction button
if st.button("Predict Insurance Cost"):

    input_data = pd.DataFrame([[Exp]],columns=['YearsExperience'])


    prediction = model.predict(input_data)
    

    st.success(f"Predicted Startup Profit: Rs./ {prediction[0][0]:,.2f}")