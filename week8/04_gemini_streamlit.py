import streamlit as st
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

st.title("Ai Writing Assistant")

col1, col2 = st.columns(2)

with col1:
    topic = st.text_input("Enter a Topic:")
with col2:
    tone = st.selectbox("Choose a Tone",["Formal","Casual","Funny"]) 

with st.sidebar:
    st.title("Settings")
    temperature = st.slider("Temperature",0.0,1.0,0.7)
    st.write(f"Current Temperature: {temperature}")

if "response" not in st.session_state:
    st.session_state.response = ""

if st.button("Generate"):
    if not topic:
        st.warning("Please enter a topic first.")
    else:
        try:
            with st.spinner("Generating..."):
                config1 = genai.types.GenerateContentConfig(
                    system_instruction=f"You are a professional writer. Write exactly one paragraph about the given topic in a {tone} tone. Be concise, clear, and well-structured. Do not add headings or extra commentary — just the paragraph.",
                    temperature=temperature
                )
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=f"Write a paragraph about {topic}",
                    config=config1
                )
                st.session_state.response = response.text
        except Exception as e:
            st.error(f"Something went wrong: {e}")

if st.session_state.response:
    st.write(st.session_state.response)