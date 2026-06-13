import streamlit as st

st.title("📋 Electronic Health Records")

st.image(
    "https://images.pexels.com/photos/7089629/pexels-photo-7089629.jpeg",
    use_container_width=True
)

patient_id = st.text_input("Patient ID")
patient_name = st.text_input("Patient Name")
diagnosis = st.text_area("Diagnosis")
prescription = st.text_area("Prescription")
allergies = st.text_area("Allergies")
medical_history = st.text_area("Medical History")

uploaded_file = st.file_uploader(
    "Upload Medical Report",
    type=["pdf", "jpg", "png"]
)

if st.button("Save Record"):

    st.success("Medical Record Saved Successfully")

    st.write("Patient ID:", patient_id)
    st.write("Patient Name:", patient_name)
    st.write("Diagnosis:", diagnosis)