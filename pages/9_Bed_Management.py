import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🛏️ Bed Management System")

# Hospital Bed Image
st.image(
    "https://images.pexels.com/photos/236380/pexels-photo-236380.jpeg",
    use_container_width=True
)


# Inputs
total_beds = st.number_input(
    "Total Beds",
    min_value=1,
    value=100
)

occupied_beds = st.number_input(
    "Occupied Beds",
    min_value=0,
    value=65
)

available_beds = total_beds - occupied_beds

# Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "🛏 Total Beds",
        total_beds
    )

with col2:
    st.metric(
        "🏥 Occupied Beds",
        occupied_beds
    )

with col3:
    st.metric(
        "✅ Available Beds",
        available_beds
    )

# Status
if available_beds < 10:
    st.error("⚠️ Critical Bed Shortage")
else:
    st.success("✅ Beds Available")

st.divider()

# Bed Analytics
st.subheader("📊 Bed Occupancy Analytics")

chart_data = pd.DataFrame({
    "Beds":[
        total_beds,
        occupied_beds,
        available_beds
    ]
},
index=[
    "Total",
    "Occupied",
    "Available"
])

st.bar_chart(chart_data)

st.divider()

# Pie Chart
st.subheader("🥧 Bed Distribution")

fig, ax = plt.subplots(figsize=(6,6))

ax.pie(
    [occupied_beds, available_beds],
    labels=["Occupied", "Available"],
    autopct="%1.1f%%"
)

ax.set_title("Hospital Bed Status")

st.pyplot(fig)

st.divider()

# Patient Allocation Table
st.subheader("👥 Current Bed Allocation")

patients = pd.DataFrame({
    "Patient ID":[
        "P101",
        "P102",
        "P103",
        "P104",
        "P105"
    ],
    "Patient Name":[
        "Ravi",
        "Priya",
        "Kumar",
        "Sneha",
        "Ramesh"
    ],
    "Ward":[
        "ICU",
        "General",
        "General",
        "ICU",
        "Emergency"
    ],
    "Bed No":[
        "B01",
        "B12",
        "B15",
        "B03",
        "B20"
    ]
})

st.dataframe(
    patients,
    use_container_width=True
)

st.divider()

# Monthly Trend
st.subheader("📈 Monthly Bed Usage Trend")

trend = pd.DataFrame({
    "Beds Used":[
        45,
        52,
        60,
        68,
        75,
        82,
        65
    ]
},
index=[
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul"
])

st.line_chart(trend)

st.divider()

st.info("""
🏥 Hospital Capacity Management Summary

• Total Hospital Capacity Monitored

• Real-Time Bed Availability Tracking

• ICU & Emergency Ward Monitoring

• Patient Bed Allocation Management

• Occupancy Analytics Dashboard
""")