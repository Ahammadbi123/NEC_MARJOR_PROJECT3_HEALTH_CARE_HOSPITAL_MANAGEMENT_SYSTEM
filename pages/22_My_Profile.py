import streamlit as st

st.set_page_config(
    page_title="My Profile",
    page_icon="👤",
    layout="wide"
)

st.title("👤 My Profile Dashboard")

# Default Values
if "name" not in st.session_state:
    st.session_state["name"] = "User"

if "email" not in st.session_state:
    st.session_state["email"] = "user@gmail.com"

if "role" not in st.session_state:
    st.session_state["role"] = "Patient"

# Profile Image
st.image(
    "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
    width=180
)

st.markdown("---")

# Profile Details
st.subheader("📋 Profile Information")

st.write("👤 Name :", st.session_state["name"])
st.write("📧 Email :", st.session_state["email"])
st.write("🛡️ Role :", st.session_state["role"])

st.markdown("---")

# EDIT PROFILE
st.subheader("✏️ Edit Profile")

new_name = st.text_input(
    "Name",
    value=st.session_state["name"]
)

new_email = st.text_input(
    "Email",
    value=st.session_state["email"]
)

new_role = st.selectbox(
    "Role",
    [
        "Patient",
        "Doctor",
        "Hospital Staff",
        "Admin"
    ],
    index=[
        "Patient",
        "Doctor",
        "Hospital Staff",
        "Admin"
    ].index(st.session_state["role"])
)

if st.button("💾 Update Profile"):

    st.session_state["name"] = new_name
    st.session_state["email"] = new_email
    st.session_state["role"] = new_role

    st.success("✅ Profile Updated Successfully")

st.markdown("---")

# DELETE ACCOUNT
if st.button("🗑️ Delete Account"):

    st.session_state.clear()

    st.warning(
        "Account Deleted Successfully"
    )

st.markdown("---")

# LOGOUT
if st.button("🚪 Logout"):

    st.session_state.clear()

    st.success(
        "Logged Out Successfully"
    )

    st.rerun()

