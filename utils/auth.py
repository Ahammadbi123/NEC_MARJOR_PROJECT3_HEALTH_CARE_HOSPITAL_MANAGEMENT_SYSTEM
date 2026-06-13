import streamlit as st
from database.db_manager import create_users_table

create_users_table()

st.set_page_config(
    page_title="AI Healthcare System",
    layout="wide"
)

st.title(
    "🏥 AI-Powered Healthcare Prediction & Resource Management System"
)

st.write(
    "Welcome To Healthcare Platform"
)