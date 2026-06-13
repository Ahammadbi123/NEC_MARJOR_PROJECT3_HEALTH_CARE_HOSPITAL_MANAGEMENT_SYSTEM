import streamlit as st

st.title("🔔 Notification Center")
st.image(
    "https://images.pexels.com/photos/3183150/pexels-photo-3183150.jpeg",
    use_container_width=True
)

notification = st.selectbox(
    "Notification Type",
    [
        "Appointment Reminder",
        "Medicine Reminder",
        "Emergency Alert",
        "Lab Report Ready"
    ]
)

if st.button("Send Notification"):

    st.success(
        f"{notification} Sent Successfully"
    )