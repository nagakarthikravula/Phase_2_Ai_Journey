import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

rude_config = genai.types.GenerateContentConfig(
    system_instruction='''You are a comedy writer. 
   When given a topic, respond with exactly one 
   short joke. No explanation, just the joke.''',
    temperature= 1.0
)

client = genai.Client(api_key = api_key)
response1 = client.models.generate_content(
    model = "gemini-3-flash-preview",
    contents = "Write an unusual, original joke about Python programming that I have never heard before",
    config= rude_config
)

response2 = client.models.generate_content(
    model = "gemini-3-flash-preview",
    contents = "Write an unusual, original joke about Python programming that I have never heard before",
    config= rude_config
)
response3 = client.models.generate_content(
    model = "gemini-3-flash-preview",
    contents = "Write an unusual, original joke about Python programming that I have never heard before",
    config= rude_config
)
print("Joke 1: ", response1.text)
print("Joke 2: ", response2.text)
print("Joke 3: ", response3.text)
