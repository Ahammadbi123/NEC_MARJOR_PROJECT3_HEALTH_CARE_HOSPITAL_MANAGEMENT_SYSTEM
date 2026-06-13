import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Patient Management",
    page_icon="🧑‍⚕️",
    layout="wide"
)

st.title("🧑‍⚕️ Patient Management System")

# ================= FORM =================

name = st.text_input("Patient Name")

age = st.number_input(
    "Age",
    min_value=1,
    max_value=120,
    value=1
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female", "Other"]
)

blood_group = st.selectbox(
    "Blood Group",
    ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
)

phone = st.text_input("Phone Number")

# ================= SESSION STORAGE =================

if "patients" not in st.session_state:
    st.session_state.patients = []

# ================= SAVE BUTTON =================

if st.button("💾 Save Patient"):

    if name == "" or phone == "":
        st.error("Please fill all fields")
    else:

        patient = {
            "Patient Name": name,
            "Age": age,
            "Gender": gender,
            "Blood Group": blood_group,
            "Phone Number": phone
        }

        st.session_state.patients.append(patient)

        st.success("✅ Patient Added Successfully")

# ================= PATIENT TABLE =================

st.markdown("---")

st.subheader("📋 Registered Patients")

if len(st.session_state.patients) > 0:

    df = pd.DataFrame(
        st.session_state.patients
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    st.download_button(
        "⬇ Download Patient Data",
        data=df.to_csv(index=False),
        file_name="patients.csv",
        mime="text/csv"
    )

else:
    st.info("No Patients Registered Yet")

