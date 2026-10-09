import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Exact values from AILearningLab_SystemsArchitecture.pdf
BASE = "https://api-ailearninglab-prod.uvic.ca/v1/"
KEY = os.environ["AILAB_API_KEY"]

# Initialize client exactly as specified in the PDF
client = OpenAI(base_url=BASE, api_key=KEY)

# Quick test from PDF
try:
    models = client.models.list()
    for model in models.data:
        print(f"Connected to model: {model.id}")
    print("✅ UVic AI Learning Lab API connection successful.")
except Exception as e:
    print(f"❌ Connection failed: {e}")
