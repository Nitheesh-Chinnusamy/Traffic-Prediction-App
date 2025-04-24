import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("traffic_model.pkl")

# Title
st.title("🚦 Traffic Prediction Web App")

# Description
st.markdown("Predict traffic level based on day, zone, and temperature using a machine learning model.")

# Input fields
day = st.selectbox("📅 Day of the Week", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
zone = st.number_input("📍 Zone (e.g., 1 to 10)", min_value=1, max_value=20)
temperature = st.number_input("🌡️ Temperature (°C)", min_value=-10.0, max_value=50.0)

# Map day to code
day_map = {
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6,
    "Sunday": 7
}

# Predict button
if st.button("🚗 Predict Traffic Level"):
    input_data = pd.DataFrame([[day_map[day], zone, temperature]], columns=["Coded Day", "Zone", "Temperature"])
    prediction = model.predict(input_data)
    prediction = round(prediction[0])

    # Display result
    st.success(f"🔮 Predicted Traffic Level: {int(prediction)} (Scale: 1-Low ➜ 5-High)")
