pip install streamlit

import streamlit as st
import pandas as pd
import joblib

st.title("AI Network Intrusion Detection System")

uploaded_file = st.file_uploader(
    "Upload Network Traffic CSV", type="csv"
)

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    predictions = best_rf.predict(data)
    
    attack_percentage = (predictions.sum() / len(predictions)) * 100
    
    st.write("Attack Percentage:", attack_percentage)