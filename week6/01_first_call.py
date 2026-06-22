import os 
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key = api_key)
response = client.models.generate_content(
    model = "gemini-3-flash-preview",
    contents = "Explain what a token is in LLMs in 3 sentences"
)

print(response.text)