import streamlit as st

st.title("🚨 Emergency Alert System")

st.image(
    "https://images.pexels.com/photos/263402/pexels-photo-263402.jpeg",
    use_container_width=True
)

oxygen = st.number_input(
    "Patient Oxygen Level (%)",
    min_value=0,
    max_value=100,
    value=98
)

heart_rate = st.number_input(
    "Heart Rate",
    min_value=0,
    value=75
)

if st.button("Check Emergency Status"):

    if oxygen < 90:

        st.error("""
🚨 CRITICAL ALERT

Doctor Notified

Nurse Notified

Emergency Team Activated
""")

    else:

        st.success(
            "Patient Condition Stable"
        )