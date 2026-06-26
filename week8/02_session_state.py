import streamlit as st

st.title("My First Streamlit App")

name = st.text_input("Enter your name: ")
mood = st.selectbox(
    "Choose a mood",
    ["Happy", "Focused", "Tired"]
)

if "message" not in st.session_state:
    st.session_state.message = ""

if st.button("Say Something"):
    message = f"Hello {name}! You seem {mood} today."
    st.session_state.message = message

st.write(st.session_state.message)