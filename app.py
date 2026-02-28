import streamlit as st
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

st.title("🚦 AI Network Intrusion Detection Dashboard")

# Load Dataset
df = pd.read_csv("data/" \
"KDDTrain+.txt")

st.subheader("Dataset Preview")
st.write(df.head())

# Train simple model (for demo)
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

model = RandomForestClassifier()
model.fit(X, y)

st.success("Model Trained Successfully!")

# Predict sample
if st.button("Run Sample Prediction"):
    prediction = model.predict([X.iloc[0]])
    st.write("Prediction:", prediction[0])