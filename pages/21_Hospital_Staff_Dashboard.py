import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Hospital Staff Dashboard",
    page_icon="👨‍⚕️",
    layout="wide"
)

st.markdown("""
<style>
.main{
background:linear-gradient(to right,#fff3e0,#ffffff);
}
</style>
""", unsafe_allow_html=True)

st.title("🏥 Hospital Staff Dashboard")

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric("Patients Assisted","145")

with c2:
    st.metric("Beds Managed","85")

with c3:
    st.metric("Resources Available","92%")

with c4:
    st.metric("Staff On Duty","35")

st.divider()

left,right = st.columns(2)

with left:

    st.subheader("🛏 Bed Status")

    bed_data = pd.DataFrame({
        "Beds":[100,85,15]
    },index=["Total","Occupied","Available"])

    st.bar_chart(bed_data)

with right:

    st.subheader("📦 Resource Usage")

    resource = pd.DataFrame({
        "Usage":[80,65,45,90]
    },index=[
        "Ventilators",
        "Oxygen",
        "Medicines",
        "Equipment"
    ])

    st.bar_chart(resource)

st.divider()

st.subheader("📋 Staff Tasks")

st.success("✔ ICU Monitoring")
st.success("✔ Patient Admission")
st.success("✔ Resource Allocation")
st.success("✔ Emergency Support")

st.divider()

st.subheader("⚡ Quick Actions")

a,b,c,d = st.columns(4)

with a:
    st.button("🛏 Bed Management")

with b:
    st.button("📦 Resources")

with c:
    st.button("🚨 Emergency")

with d:
    st.button("📢 Notifications")

st.divider()

st.subheader("🚨 Alerts")

st.warning("Low Oxygen Stock")
st.info("2 Ambulances Available")
st.success("All Critical Equipment Operational")