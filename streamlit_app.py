import streamlit as st

st.title("💧 Water Potability Predictor")

ph = st.number_input("Enter pH value")

if st.button("Predict"):
    if 6.5 < ph < 8.5:
        st.success("✅ Water is Potable")
    else:
        st.error("❌ Water is NOT Potable")
