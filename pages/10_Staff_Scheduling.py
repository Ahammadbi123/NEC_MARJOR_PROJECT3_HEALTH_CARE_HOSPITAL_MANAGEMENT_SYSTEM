import streamlit as st

st.title("👨‍⚕️ Staff Scheduling System")
st.image(
    "https://images.pexels.com/photos/3845810/pexels-photo-3845810.jpeg",
    use_container_width=True
)
doctor_count = st.number_input(
    "Available Doctors",
    min_value=1,
    value=10
)

nurse_count = st.number_input(
    "Available Nurses",
    min_value=1,
    value=20
)

shift = st.selectbox(
    "Select Shift",
    [
        "Morning",
        "Afternoon",
        "Night"
    ]
)

if st.button("Generate Schedule"):

    st.success("Schedule Generated Successfully")

    st.write(f"Doctors Assigned : {doctor_count}")
    st.write(f"Nurses Assigned : {nurse_count}")
    st.write(f"Shift : {shift}")