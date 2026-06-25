import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


rude_config1 = genai.types.GenerateContentConfig(
    system_instruction="You are a sentiment classifier."
)
client = genai.Client(api_key = api_key)

for i in range(5):
    response1 = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = 'Classify this feedback as Positive, Negative, or Neutral: "Fast delivery but the color was different from the photo, though I still like it overall."',
        config= rude_config1
    )
    print(repr(response1.text))
