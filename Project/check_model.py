from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

for model in client.models.list():
    try:
        print("MODEL:", model.name)

        if hasattr(model, "supported_actions"):
            print("SUPPORTED:", model.supported_actions)

        if hasattr(model, "supported_generation_methods"):
            print("METHODS:", model.supported_generation_methods)

        print("-" * 50)

    except Exception as e:
        print(e)