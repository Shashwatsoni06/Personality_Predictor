import streamlit as st
import pickle
import pandas as pd

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Personality Predictor",
    page_icon="🧠",
    layout="wide"
)

# -----------------------------
# Load saved objects
# -----------------------------
with open("personality_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

with open("model_features.pkl", "rb") as f:
    feature_names = pickle.load(f)

# -----------------------------
# Header Section
# -----------------------------
st.title("🧠 Personality Type Prediction System")
st.markdown("### Discover your personality based on behavioral traits")
st.markdown("---")

# -----------------------------
# Input Section
# -----------------------------
st.subheader("📋 Enter Your Traits")

col1, col2 = st.columns(2)

user_input = {}

for i, feature in enumerate(feature_names):
    if i % 2 == 0:
        with col1:
            user_input[feature] = st.slider(
                feature.replace("_", " ").title(),
                0, 10, 5
            )
    else:
        with col2:
            user_input[feature] = st.slider(
                feature.replace("_", " ").title(),
                0, 10, 5
            )

st.markdown("---")

# -----------------------------
# Prediction Section
# -----------------------------
if st.button("🔍 Predict Personality Type"):

    input_df = pd.DataFrame([user_input])
    input_df = input_df[feature_names]

    input_scaled = scaler.transform(input_df)

    prediction = model.predict(input_scaled)
    probability = model.predict_proba(input_scaled)

    predicted_text = label_encoder.inverse_transform(prediction)[0]
    confidence = max(probability[0]) * 100

    st.markdown("## 🎯 Prediction Result")

    st.success(f"### 🧠 Personality Type: **{predicted_text}**")
    st.info(f"Confidence Level: **{confidence:.2f}%**")

    st.markdown("---")