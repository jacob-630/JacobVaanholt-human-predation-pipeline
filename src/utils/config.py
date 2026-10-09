import os
from dotenv import load_dotenv

# Load the environment variables (your API key)
load_dotenv()

# CONFIGURATION OBJECT
class AIConfig:
    UVIC_API_BASE = "https://api-ailearninglab-prod.uvic.ca/v1/"
    UVIC_API_KEY = os.getenv("AILAB_API_KEY")
    MODEL_NAME = "qwen3-6-35b-a3b-vllm" # The specific UVic model
    
    # Check if key is present
    if not UVIC_API_KEY:
        raise ValueError("API Key not found in .env file. Please add your UVic API key.")
