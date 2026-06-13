import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Resource Allocation",
    page_icon="🏥",
    layout="wide"
)

# ================= HEADER =================

st.markdown("""
<h1 style='text-align:center;color:#00B4FF;'>
🏥  Hospital Resource Allocation Dashboard
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<h4 style='text-align:center;color:gray;'>
AI-Powered Resource Monitoring & Optimization System
</h4>
""", unsafe_allow_html=True)

# ================= IMAGE =================

st.image(
    "https://images.pexels.com/photos/6129688/pexels-photo-6129688.jpeg",
    use_container_width=True
)
st.image(
    "https://images.pexels.com/photos/4386466/pexels-photo-4386466.jpeg",
    use_container_width=True
)
st.markdown("---")

# ================= INPUTS =================

st.subheader("📦 Hospital Resource Management")

col1, col2, col3 = st.columns(3)

with col1:
    ventilators = st.number_input(
        "Available Ventilators",
        min_value=0,
        value=25
    )

with col2:
    oxygen_units = st.number_input(
        "Available Oxygen Units",
        min_value=0,
        value=100
    )

with col3:
    equipment = st.number_input(
        "Medical Equipment Count",
        min_value=0,
        value=50
    )

# ================= BUTTON =================

if st.button("🚀 Allocate Resources"):

    st.success("✅ Resources Allocated Successfully")

    st.markdown("---")

    # ================= METRICS =================

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "🫁 Ventilators",
            ventilators
        )

    with c2:
        st.metric(
            "🧪 Oxygen Units",
            oxygen_units
        )

    with c3:
        st.metric(
            "🏥 Equipment",
            equipment
        )

    st.markdown("---")

    # ================= BAR CHART =================

    st.subheader("📊 Resource Availability")

    chart_data = pd.DataFrame({
        "Resource":[
            "Ventilators",
            "Oxygen Units",
            "Equipment"
        ],
        "Count":[
            ventilators,
            oxygen_units,
            equipment
        ]
    })

    st.bar_chart(
        chart_data.set_index("Resource")
    )

    st.markdown("---")

    # ================= PIE CHART =================

    st.subheader("🥧 Resource Distribution")

    fig, ax = plt.subplots(figsize=(6,6))

    ax.pie(
        [
            ventilators,
            oxygen_units,
            equipment
        ],
        labels=[
            "Ventilators",
            "Oxygen",
            "Equipment"
        ],
        autopct="%1.1f%%"
    )

    ax.set_title(
        "Hospital Resource Distribution"
    )

    st.pyplot(fig)

    st.markdown("---")

    # ================= LINE GRAPH =================

    st.subheader("📈 Weekly Resource Usage Trend")

    trend_data = pd.DataFrame({
        "Day":[
            "Mon",
            "Tue",
            "Wed",
            "Thu",
            "Fri",
            "Sat",
            "Sun"
        ],
        "Usage":[
            65,
            70,
            75,
            80,
            78,
            85,
            82
        ]
    })

    st.line_chart(
        trend_data.set_index("Day")
    )

    st.markdown("---")

    # ================= TABLE =================

    st.subheader("🏥 Department Resource Allocation")

    resource_table = pd.DataFrame({
        "Department":[
            "ICU",
            "Emergency",
            "General Ward",
            "Operation Theatre",
            "Pediatrics"
        ],
        "Resources Allocated":[
            40,
            30,
            20,
            25,
            15
        ]
    })

    st.dataframe(
        resource_table,
        use_container_width=True
    )

    st.markdown("---")

    # ================= AI INSIGHTS =================

    st.subheader("🤖 AI Resource Insights")

    if ventilators < 20:
        st.warning(
            "⚠ Ventilator availability is getting low."
        )
    else:
        st.success(
            "✅ Ventilator stock is sufficient."
        )

    if oxygen_units < 80:
        st.warning(
            "⚠ Oxygen stock needs replenishment."
        )
    else:
        st.success(
            "✅ Oxygen supply is stable."
        )

    st.info(
        "🤖 AI Forecast: Expected resource utilization tomorrow is 82%."
    )

    st.info(
        "🏥 Emergency Preparedness Level: HIGH"
    )

    st.success(
        "🏥 Hospital Resources Optimized Successfully"
    )

