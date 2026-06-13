import streamlit as st

st.title("📅 Appointment Scheduling System")
st.image(
    "https://images.pexels.com/photos/40568/medical-appointment-doctor-healthcare-40568.jpeg",
    use_container_width=True
)

patient_name = st.text_input("Patient Name")

doctor_name = st.selectbox(
    "Select Doctor",
    [
        "Dr. Ram",
        "Dr. Suresh",
        "Dr. Priya",
        "Dr. Kiran"
    ]
)

appointment_date = st.date_input(
    "Appointment Date"
)

appointment_time = st.time_input(
    "Appointment Time"
)

problem = st.text_area(
    "Describe Problem"
)

if st.button("Book Appointment"):

    st.success(
        "Appointment Booked Successfully"
    )

    st.write("Patient :", patient_name)
    st.write("Doctor :", doctor_name)
    st.write("Date :", appointment_date)
    st.write("Time :", appointment_time)