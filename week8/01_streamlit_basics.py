import streamlit as st

st.title("My First Streamlit App")

name = st.text_input("Enter your name: ")
mood = st.selectbox(
    "Choose a mood",
    ["Happy", "Focused", "Tired"]
)

if st.button("Say Something"):
    st.write(f"Hello {name}! You seem {mood} today.")