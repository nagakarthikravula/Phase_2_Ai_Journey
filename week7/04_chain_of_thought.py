import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


# rude_config1 = genai.types.GenerateContentConfig(
#     system_instruction='''You are a sentiment classifier. 
# Reply with exactly one word: Positive, Negative, or Neutral.'''
# )
client = genai.Client(api_key = api_key)

response1 = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = '''A store is having a 20% off sale. An item originally 
costs 850 rupees. You also have a coupon for 10% off the sale 
price. What is the final price you pay? Give me just the 
final number in rupees.'''
        # config= rude_config1
    )
print(response1.text)

response2 = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = '''A store is having a 20% off sale. An item originally 
costs 850 rupees. You also have a coupon for 10% off the sale 
price. What is the final price you pay? Think through this 
step by step, showing each calculation, then give the final answer.'''
        # config= rude_config1
    )
print(response1.text)
print(response2.text)