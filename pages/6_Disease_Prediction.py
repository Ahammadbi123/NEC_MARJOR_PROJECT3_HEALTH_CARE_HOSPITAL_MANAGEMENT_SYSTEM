import streamlit as st

st.title("🧠 AI Disease Prediction")

age = st.number_input("Age",1,120)
sugar = st.number_input("Sugar Level")

if st.button("Predict"):

    if sugar > 140:
        st.error("High Diabetes Risk")
    else:
        st.success("Low Diabetes Risk")