import os
from google import genai
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
high_temp = genai.types.GenerateContentConfig(temperature=1.0)
low_temp = genai.types.GenerateContentConfig(temperature=0.0)

client = genai.Client(api_key = api_key)
response1 = client.models.generate_content(
    model = "gemini-3-flash-preview",
    contents = "Give me a creative name for a tea shop",
    config= low_temp
)

response2 = client.models.generate_content(
    model = "gemini-3-flash-preview",
    contents = "Give me a creative name for a tea shop",
    config= high_temp
)

print("\n--- Token Usage ---")
print("Response 1 tokens:", response1.usage_metadata)
print("Response 2 tokens:", response2.usage_metadata)
