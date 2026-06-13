import streamlit as st
st.title("💊 Treatment Recommendation")
st.markdown("""
<div style="
background:linear-gradient(135deg,#00E5FF,#7B2FF7);
padding:25px;
border-radius:20px;
text-align:center;
box-shadow:0px 0px 30px #00E5FF;
margin-bottom:25px;
">
<h1 style="color:white;font-size:55px;">
💊 Treatment Recommendation
</h1>

<h3 style="color:white;">
AI-Based Personalized Healthcare Treatment Engine
</h3>
</div>
""", unsafe_allow_html=True)

st.image(
    "https://images.pexels.com/photos/40568/medical-appointment-doctor-healthcare-40568.jpeg",
    use_container_width=True
)
disease = st.selectbox(
    "Select Disease",
    [
        "Diabetes",
        "Heart Disease",
        "Kidney Disease"
    ]
)

if st.button("Recommend Treatment"):

    if disease == "Diabetes":

        st.success("""
Recommended:

• Low Sugar Diet

• Daily Exercise

• Regular Blood Sugar Monitoring

• Doctor Consultation
""")

    elif disease == "Heart Disease":

        st.success("""
Recommended:

• Low Fat Diet

• Cardiology Consultation

• Regular ECG Monitoring

• Daily Walking
""")

    else:

        st.success("""
Recommended:

• Kidney Function Tests

• Hydration Monitoring

• Nephrologist Consultation
""")