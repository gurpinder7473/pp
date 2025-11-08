
import streamlit as st
import requests

st.set_page_config(page_title="Bike Price Prediction", layout="centered")

st.title("🚴 Bike Price Prediction App")
st.write("Enter bike details below and get predicted price.")

# Backend URL (update after deployment)
BACKEND_URL = st.secrets.get("backend_url", "http://localhost:8000/predict")

brand = st.text_input("Brand")
age = st.number_input("Age (Years)", min_value=0.0)
mileage = st.number_input("Mileage (km)", min_value=0.0)
power = st.number_input("Power (HP)", min_value=0.0)
engine_size = st.number_input("Engine Size (CC)", min_value=0.0)

if st.button("Predict Price"):
    data = {
        "brand": brand,
        "age": age,
        "mileage": mileage,
        "power": power,
        "engine_size": engine_size,
    }

    try:
        res = requests.post(BACKEND_URL, json=data, timeout=10)
        if res.status_code == 200:
            st.success(f"💰 Predicted Price: ₹{res.json()['predicted_price']:,}")
        else:
            st.error("Prediction failed: " + res.text)
    except Exception as e:
        st.error(f"Connection error: {e}")
