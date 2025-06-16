import os
from dotenv import load_dotenv

load_dotenv()

news_key = os.getenv("NEWS_API_KEY")
gemini_key = os.getenv("GOOGLE_GEMINI_API_KEY")

print(f"News Key: {news_key}")
print(f"Gemini Key: {gemini_key}")

if news_key:
    print("Successfully loaded News API Key!")
else:
    print("FAILED to load News API Key.")

if gemini_key:
    print("Successfully loaded Gemini API Key!")
else:
    print("FAILED to load Gemini API Key.")

#  file_name.env  >>>>>>> wrong
#  .env >>>>>>>>> right