import streamlit as st
import pandas as pd

st.title("📊 Hospital Analytics Dashboard")

# Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Patients", 1250)

with col2:
    st.metric("Doctors", 85)

with col3:
    st.metric("Appointments", 420)

with col4:
    st.metric("Available Beds", 35)

st.divider()

# Patient Statistics
st.subheader("📈 Monthly Patient Statistics")

data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Patients": [120, 150, 180, 210, 250, 300]
})

st.line_chart(data.set_index("Month"))

st.divider()

# Disease Cases
st.subheader("🦠 Disease Cases")

disease_data = pd.DataFrame({
    "Disease": [
        "Diabetes",
        "Heart Disease",
        "Kidney Disease",
        "Cancer"
    ],
    "Cases": [120, 80, 60, 40]
})

st.bar_chart(
    disease_data.set_index("Disease")
)

st.divider()

# Hospital Summary
st.subheader("🏥 Hospital Summary")

st.success("""
✔ Healthcare System Running Successfully

✔ Patient Records Managed

✔ AI Disease Prediction Active

✔ Resource Allocation Active

✔ Bed Management Active
""")