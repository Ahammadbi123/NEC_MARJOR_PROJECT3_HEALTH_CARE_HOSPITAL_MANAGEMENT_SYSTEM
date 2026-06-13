import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Admin Dashboard",
    page_icon="🏥",
    layout="wide"
)

st.markdown("""
<style>
.main {
    background: linear-gradient(to right,#e3f2fd,#ffffff);
}
.big-title{
    font-size:45px;
    font-weight:bold;
    color:#1565c0;
}
.card{
    background-color:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 2px 10px rgba(0,0,0,0.1);
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    "<div class='big-title'>🏥 Hospital Administration Dashboard</div>",
    unsafe_allow_html=True
)

st.write("---")

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric("👥 Total Patients", "1250", "+35")

with c2:
    st.metric("👨‍⚕️ Doctors", "85", "+5")

with c3:
    st.metric("🏥 Staff", "220", "+12")

with c4:
    st.metric("🛏 Available Beds", "35", "-2")

st.write("---")

col1,col2 = st.columns(2)

with col1:

    st.subheader("📈 Monthly Patient Growth")

    df = pd.DataFrame({
        "Patients":[
            120,150,180,
            220,270,320,
            400
        ]
    })

    st.line_chart(df)

with col2:

    st.subheader("💰 Revenue Overview")

    revenue = pd.DataFrame({
        "Revenue":[
            10000,15000,17000,
            22000,26000,30000,
            45000
        ]
    })

    st.bar_chart(revenue)

st.write("---")

st.subheader("🏥 Hospital Overview")

a,b,c = st.columns(3)

with a:
    st.success("Emergency Department Active")

with b:
    st.info("12 Ambulances Available")

with c:
    st.warning("3 ICU Beds Remaining")

st.write("---")

st.subheader("⚡ Quick Access")

q1,q2,q3,q4 = st.columns(4)

with q1:
    st.button("👥 Patient Management")

with q2:
    st.button("👨‍⚕️ Doctor Management")

with q3:
    st.button("📅 Appointments")

with q4:
    st.button("📊 Analytics")

st.write("---")

st.subheader("🚨 Emergency Alerts")

st.error("Critical Patient in ICU - Immediate Attention Required")

st.warning("Low Blood Stock Alert")

st.success("All Ventilators Operational")