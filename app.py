import streamlit as st

st.set_page_config(
    page_title="AI Healthcare System",
    layout="wide"
)

st.title("🏥 AI-Powered Healthcare Prediction & Resource Management System")

st.image(
    "https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d",
    use_container_width=True
)

st.write("### Hospital Overview")

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric("👥 Patients",1250)

with c2:
    st.metric("👨‍⚕️ Doctors",85)

with c3:
    st.metric("📅 Appointments",420)

with c4:
    st.metric("🛏 Beds",35)

st.write("---")

st.subheader("🏥 Hospital Information")

st.write("""
• Multi Speciality Hospital

• 24/7 Emergency Services

• AI Disease Prediction

• Smart Resource Management

• Online Appointment Booking
""")