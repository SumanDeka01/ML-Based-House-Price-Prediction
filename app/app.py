import streamlit as st

st.set_page_config(page_title="House Price Prediction", layout="centered")

st.title("🏠 House Price Prediction System")
st.write("Enter house details to estimate price")

# Inputs
area = st.number_input("Area (in sq ft)", min_value=300, max_value=10000)
bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10)
bathrooms = st.number_input("Number of Bathrooms", min_value=1, max_value=10)

# Button
if st.button("Predict Price"):
    st.success("Predicted Price: ₹ XX,XX,XXX")
    st.info("Model integration coming soon 🚀")
