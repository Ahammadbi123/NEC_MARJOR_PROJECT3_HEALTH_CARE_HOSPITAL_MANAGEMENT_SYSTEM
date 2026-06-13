import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📈 Patient Outcome Prediction")

age = st.number_input(
    "Age",
    min_value=1,
    max_value=120
)

severity = st.selectbox(
    "Disease Severity",
    ["Low", "Medium", "High"]
)

if st.button("Predict Outcome"):

    # Outcome Values
    if severity == "Low":
        recovery = 95
        stay = 2
        icu = 5

        st.success("""
Recovery Probability : 95%

Hospital Stay : 2 Days

ICU Requirement : No
""")

    elif severity == "Medium":
        recovery = 75
        stay = 5
        icu = 25

        st.warning("""
Recovery Probability : 75%

Hospital Stay : 5 Days

ICU Requirement : Possible
""")

    else:
        recovery = 50
        stay = 10
        icu = 60

        st.error("""
Recovery Probability : 50%

Hospital Stay : 10 Days

ICU Requirement : Required
""")

    st.markdown("---")

    # Metrics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Recovery Rate",
            f"{recovery}%"
        )

    with col2:
        st.metric(
            "Hospital Stay",
            f"{stay} Days"
        )

    with col3:
        st.metric(
            "ICU Risk",
            f"{icu}%"
        )

    st.markdown("---")

    # Bar Chart
    st.subheader("📊 Outcome Analytics")

    chart_data = pd.DataFrame({
        "Metric": [
            "Recovery",
            "Hospital Stay",
            "ICU Risk"
        ],
        "Value": [
            recovery,
            stay,
            icu
        ]
    })

    st.bar_chart(
        chart_data.set_index("Metric")
    )

    # Line Chart
    st.subheader("📈 Recovery Progress Trend")

    trend = pd.DataFrame({
        "Day": [1,2,3,4,5,6,7],
        "Recovery %": [
            recovery*0.3,
            recovery*0.45,
            recovery*0.60,
            recovery*0.72,
            recovery*0.85,
            recovery*0.92,
            recovery
        ]
    })

    st.line_chart(
        trend.set_index("Day")
    )

    # Pie Chart
    st.subheader("🥧 Patient Outcome Distribution")

    pie_labels = [
        "Recovered",
        "Under Treatment",
        "Critical"
    ]

    if severity == "Low":
        pie_values = [80, 15, 5]
    elif severity == "Medium":
        pie_values = [60, 25, 15]
    else:
        pie_values = [40, 30, 30]

    fig, ax = plt.subplots(figsize=(6,6))

    ax.pie(
        pie_values,
        labels=pie_labels,
        autopct="%1.1f%%"
    )

    ax.set_title(
        "Patient Outcome Distribution"
    )

    st.pyplot(fig)