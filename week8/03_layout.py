import streamlit as st

st.title("Layout Practice")
col1, col2 = st.columns(2)

with col1:
    topic = st.text_input("Topic")

with col2:
    tone = st.selectbox("Choose a Tone",["Formal","Casual","Funny"])

with st.sidebar:
    st.title("Settings")
    temperature = st.slider("Temperature",0.0,1.0,0.7)
    st.write(f"Current temperature: {temperature}")

if "message" not in st.session_state:
    st.session_state.message = ""

if st.button("Generate"):
    res = f"Topic: {topic} | Tone: {tone} | Temp: {temperature}"
    st.session_state.message = res

st.write(st.session_state.message)

