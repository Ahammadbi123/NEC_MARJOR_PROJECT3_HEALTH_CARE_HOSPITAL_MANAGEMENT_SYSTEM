import streamlit as st

st.set_page_config(
    page_title="Authentication",
    layout="wide"
)

st.title("🏥 AI Healthcare Authentication System")

tab1, tab2 = st.tabs(["Login", "Register"])

# ================= LOGIN =================

with tab1:

    st.subheader("Login")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    role = st.selectbox(
        "Role",
        [
            "Patient",
            "Doctor",
            "Hospital Staff",
            "Admin"
        ]
    )

    if st.button("Login"):

        st.session_state["logged_in"] = True
        st.session_state["name"] = email.split("@")[0]
        st.session_state["email"] = email
        st.session_state["role"] = role

        st.success(f"Welcome {role}")
        st.write("👤 Name :", st.session_state["name"])
        st.write("📧 Email :", email)
        st.write("🛡️ Role :", role)

# ================= REGISTER =================

with tab2:

    st.subheader("Register")

    name = st.text_input("Name")

    reg_email = st.text_input(
        "Email",
        key="reg_email"
    )

    reg_password = st.text_input(
        "Password",
        type="password",
        key="reg_password"
    )

    reg_role = st.selectbox(
        "Select Role",
        [
            "Patient",
            "Doctor",
            "Hospital Staff",
            "Admin"
        ]
    )

    if st.button("Register"):

        st.success("Registration Successful")

        st.write("👤 Name :", name)
        st.write("📧 Email :", reg_email)
        st.write("🛡️ Role :", reg_role)

        # Save user info
        st.session_state["name"] = name
        st.session_state["email"] = reg_email
        st.session_state["role"] = reg_role