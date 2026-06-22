import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
high_temp = genai.types.GenerateContentConfig(temperature=1.0)
low_temp = genai.types.GenerateContentConfig(temperature=0.0)

rude_config = genai.types.GenerateContentConfig(
    system_instruction='''You are a rude, sarcastic assistant 
    who gives answers in maximum 1 sentence and always 
    complains about the question being too simple.'''
)

client = genai.Client(api_key = api_key)
response1 = client.models.generate_content(
    model = "gemini-3-flash-preview",
    contents = "What is the capital of India?",
    config= rude_config
)

print("Response 1: ", response1.text)