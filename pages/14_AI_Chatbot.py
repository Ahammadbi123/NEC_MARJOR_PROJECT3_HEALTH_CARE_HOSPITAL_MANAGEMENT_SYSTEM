import streamlit as st

st.title("🤖 Healthcare AI Chatbot")

question = st.text_input(
    "Ask Health Question"
)

if st.button("Ask"):

    q = question.lower()

    if "fever" in q:

        st.success(
            "Drink fluids and consult a doctor if symptoms continue."
        )

    elif "diabetes" in q:

        st.success(
            "Monitor blood sugar regularly and follow a healthy diet."
        )

    elif "heart" in q:

        st.success(
            "Regular exercise and cardiac consultation are recommended."
        )

    else:

        st.info(
            "Please consult a healthcare professional."
        )