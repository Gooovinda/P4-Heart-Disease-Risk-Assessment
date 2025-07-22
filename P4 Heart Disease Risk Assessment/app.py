import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Loading the trained model
model = joblib.load("heart_disease_model.pkl")  

st.title("Heart Disease Risk Assessment")
st.write("Enter Your Health Metrics Below :")

# Creating input fields
chest_pain = st.selectbox("Chest Pain", [0, 1])
short_breath = st.selectbox("Shortness of Breath", [0, 1])
fatigue = st.selectbox("Fatigue", [0, 1])
palpitations = st.selectbox("Palpitations", [0, 1])
dizziness = st.selectbox("Dizziness", [0, 1])
swelling = st.selectbox("Swelling", [0, 1])
pain_arms = st.selectbox("Pain in Arms/Jaw/Back", [0, 1])
cold_sweats = st.selectbox("Cold Sweats/Nausea", [0, 1])
high_bp = st.selectbox("High Blood Pressure", [0, 1])
high_chol = st.selectbox("High Cholesterol", [0, 1])
diabetes = st.selectbox("Diabetes", [0, 1])
smoking = st.selectbox("Smoking", [0, 1])
obesity = st.selectbox("Obesity", [0, 1])
sedentary = st.selectbox("Sedentary Lifestyle", [0, 1])
family_hist = st.selectbox("Family History", [0, 1])
stress = st.selectbox("Chronic Stress", [0, 1])
gender = st.selectbox("Gender (0 = Female, 1 = Male)", [0, 1])
age = st.slider("Age", 20, 100)

if st.button("Predict Risk"):
    input_data = np.array([[chest_pain, short_breath, fatigue, palpitations, dizziness, swelling,
                            pain_arms, cold_sweats, high_bp, high_chol, diabetes, smoking,
                            obesity, sedentary, family_hist, stress, gender, age]])
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.error("High Risk of Heart Disease 🚨")
    else:
        st.success("Low Risk of Heart Disease ✅")
