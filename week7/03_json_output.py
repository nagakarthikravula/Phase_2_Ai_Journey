import os
import json
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


rude_config1 = genai.types.GenerateContentConfig(
    system_instruction='''You are a product review analyzer. Always respond in valid 
JSON format with exactly these three keys:
- sentiment: either Positive, Negative, or Neutral
- topics: a list of topics mentioned in the review
- summary: one sentence summary of the review
Never add any text outside the JSON.''',
response_mime_type= "application/json"
)
client = genai.Client(api_key = api_key)

response1 = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = '''Analyze this review: 
'The laptop arrived two days early which was great. 
Battery life is excellent — lasts all day. 
The keyboard feels a bit cheap though, 
and the screen could be brighter.''',
    config= rude_config1
    )
    
print(response1.text)
data = json.loads(response1.text)
print(data["sentiment"])
print(data["topics"])
print(data["summary"])


