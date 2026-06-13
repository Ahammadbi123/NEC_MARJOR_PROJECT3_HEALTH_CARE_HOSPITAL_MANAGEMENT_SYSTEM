import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Doctor Dashboard",
    page_icon="👨‍⚕️",
    layout="wide"
)

st.markdown("""
<style>
.main{
background:linear-gradient(to right,#f3f9ff,#ffffff);
}
h1{
color:#1565c0;
}
</style>
""", unsafe_allow_html=True)

st.title("👨‍⚕️ Doctor Dashboard")

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric("Today's Patients","32","+5")

with c2:
    st.metric("Appointments","18","+3")

with c3:
    st.metric("Emergency Cases","4")

with c4:
    st.metric("Success Rate","96%")

st.divider()

left,right = st.columns(2)

with left:

    st.subheader("📅 Today's Schedule")

    schedule = pd.DataFrame({
        "Time":[
            "09:00 AM",
            "10:30 AM",
            "12:00 PM",
            "02:00 PM",
            "04:00 PM"
        ],
        "Patient":[
            "Ramesh",
            "Priya",
            "Kiran",
            "Suresh",
            "Lakshmi"
        ]
    })

    st.dataframe(schedule,use_container_width=True)

with right:

    st.subheader("📈 Weekly Patients")

    chart = pd.DataFrame({
        "Patients":[12,15,20,18,25,30,28]
    })

    st.line_chart(chart)

st.divider()

st.subheader("🩺 Doctor Quick Actions")

a,b,c,d = st.columns(4)

with a:
    st.button("📋 View Patients")

with b:
    st.button("💊 Prescriptions")

with c:
    st.button("🧪 Lab Reports")

with d:
    st.button("📅 Appointments")

st.divider()

st.subheader("🚨 Critical Alerts")

st.error("2 Critical Patients Need Attention")
st.warning("3 Lab Reports Pending Review")
st.success("All Operations Running Normally")