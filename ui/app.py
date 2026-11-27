import streamlit as st
import requests

st.title("Iris Full-Stack Classifier")

sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, format="%.2f")
sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, format="%.2f")
petal_length = st.number_input("Petal Length (cm)", min_value=0.0, format="%.2f")
petal_width = st.number_input("Petal Width (cm)", min_value=0.0, format="%.2f")

if st.button("Predict"):
    payload = {
        "feature_array": [sepal_length, sepal_width, petal_length, petal_width]
    }
    try:
        response = requests.post("http://api:8000/predict", json=payload)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted Species: {result}")
        else:
            st.error(f"API Error {response.status_code}: {response.text}")
    except Exception as e:
        st.error(f"Connection Error: {str(e)}")