import streamlit as st

st.title("👨‍⚕️ Doctor Management System")

doctor_id = st.text_input("Doctor ID")

doctor_name = st.text_input("Doctor Name")

specialization = st.selectbox(
    "Specialization",
    [
        "Cardiologist",
        "Neurologist",
        "Orthopedic",
        "Dermatologist",
        "General Physician"
    ]
)

department = st.text_input("Department")

experience = st.number_input(
    "Experience (Years)",
    min_value=0,
    max_value=50
)

qualification = st.text_input("Qualification")

phone = st.text_input("Phone Number")

email = st.text_input("Email")

availability = st.selectbox(
    "Availability",
    [
        "Morning",
        "Afternoon",
        "Evening",
        "Full Day"
    ]
)

if st.button("Register Doctor"):
    st.success("Doctor Registered Successfully")