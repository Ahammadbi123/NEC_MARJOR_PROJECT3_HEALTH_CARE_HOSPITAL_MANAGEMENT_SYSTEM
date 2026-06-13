import streamlit as st
import pandas as pd

st.title("📄 Hospital Reports")

report_type = st.selectbox(
    "Select Report",
    [
        "Patient Report",
        "Doctor Report",
        "Bed Report",
        "Disease Report"
    ]
)

if st.button("Generate Report"):

    data = pd.DataFrame({
        "ID":[1,2,3],
        "Name":["Patient A","Patient B","Patient C"],
        "Status":["Recovered","Under Treatment","Recovered"]
    })

    st.success(f"{report_type} Generated Successfully")

    st.dataframe(data)