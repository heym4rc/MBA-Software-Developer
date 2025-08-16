import os
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv('API_KEY')

client = genai.Client()

pergunta = input("Digite sua pergunta: ")

response = client.models.generate_content(
    model="gemini-2.5-pro",
    contents=pergunta,
)

print(response.text)