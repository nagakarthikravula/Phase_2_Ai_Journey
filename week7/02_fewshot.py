import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


rude_config1 = genai.types.GenerateContentConfig(
    system_instruction='''You are a sentiment classifier. 
Reply with exactly one word: Positive, Negative, or Neutral.'''
)
client = genai.Client(api_key = api_key)

for i in range(5):
    response1 = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = '''Example 1:
Feedback: "Great product, very happy with my purchase."
Classification: Positive

Example 2:
Feedback: "Terrible quality, broke after one day."
Classification: Negative

Example 3:
Feedback: "It works but nothing special."
Classification: Neutral

Example 4:
Feedback: "I liked the product but the delivery was slow."
Classification: Neutral

Now classify this:
Feedback: "Fast delivery but the color was different from 
the photo, though I still like it overall."
Classification:''',
        config= rude_config1
    )
    print(repr(response1.text))
