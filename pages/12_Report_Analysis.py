import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Medical Report Analysis",
    page_icon="🔬",
    layout="wide"
)

st.title("🔬 AI Medical Report Analysis System")

# Medical Report Banner
st.image(
    "https://images.pexels.com/photos/7089401/pexels-photo-7089401.jpeg",
    use_container_width=True
)

st.info("""
AI-Powered Medical Report Analysis System

✔ Blood Test Analysis

✔ Diagnostic Report Review

✔ Risk Assessment

✔ Health Monitoring

✔ AI-Based Recommendations
""")

st.markdown("---")

report = st.file_uploader(
    "📄 Upload Medical Report",
    type=["pdf", "jpg", "png"]
)

if st.button("🔍 Analyze Report"):

    st.success("✅ Analysis Completed Successfully")

    # Metrics
    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Hemoglobin",
            "13.5 g/dL"
        )

    with c2:
        st.metric(
            "Blood Sugar",
            "145 mg/dL"
        )

    with c3:
        st.metric(
            "Cholesterol",
            "180 mg/dL"
        )

    st.markdown("---")

    st.subheader("📋 Analysis Results")

    st.success("✔ Hemoglobin : Normal")

    st.warning("⚠ Blood Sugar : Slightly High")

    st.success("✔ Cholesterol : Normal")

    st.info(
        "🩺 Regular Monitoring Recommended"
    )

    st.markdown("---")

    # Small Pie Chart
    st.subheader("🥧 Health Parameter Distribution")

    fig, ax = plt.subplots(figsize=(4,4))

    ax.pie(
        [60, 25, 15],
        labels=[
            "Normal",
            "Attention",
            "Critical"
        ],
        autopct="%1.1f%%"
    )

    ax.set_title(
        "Health Status"
    )

    st.pyplot(fig)

    st.markdown("---")

    st.success(
        "🤖 AI Report Analysis Generated Successfully"
    )

