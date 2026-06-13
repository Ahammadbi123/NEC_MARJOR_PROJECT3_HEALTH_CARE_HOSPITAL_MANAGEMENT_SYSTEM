import streamlit as st

st.title("👤 Patient Management")

name = st.text_input("Patient Name")

age = st.number_input(
    "Age",
    min_value=1,
    max_value=120
)

gender = st.selectbox(
    "Gender",
    ["Male","Female","Other"]
)

blood = st.selectbox(
    "Blood Group",
    ["A+","A-","B+","B-","O+","O-","AB+","AB-"]
)

phone = st.text_input("Phone Number")

if st.button("Save Patient"):

    st.success("Patient Added Successfully")