import os
import sys
import re
import json
import requests
import PyPDF2
from openai import OpenAI
from dotenv import load_dotenv

# Ensure project root is in path
sys.path.insert(0, os.getcwd())

from src.utils.config import AIConfig
from src.utils.log_manager import get_logger

# Setup APIs
load_dotenv()
ai_client = OpenAI(api_key=AIConfig.UVIC_API_KEY, base_url=AIConfig.UVIC_API_BASE)
logger = get_logger()

# CONFIGURE YOUR EMAIL HERE
# Crossref requires this for their free API
USER_AGENT_EMAIL = "jacobvaanholt@uvic.ca" 

def extract_metadata_smart(pdf_path):
    """
    The Tiered Hybrid Approach.
    1. Try Regex to find DOI -> Use Crossref API (Gold Standard/Free).
    2. If DOI fails -> Use AI (Fallback).
    """
    
    # STEP 1: Extract raw text to search for DOI
    try:
        with open(pdf_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            # Search first 3 pages
            text = "".join([reader.pages[0].extract_text() for i in range(3)])
            
        # Look for DOI pattern
        doi_match = re.search(r'(?:doi:)?(10\.\d{4,9}/[-._;()/:A-Z0-9]+)', text, re.IGNORECASE)
        doi = doi_match.group(1).strip() if doi_match else None
        
        if doi:
            logger.info(f"Found DOI: {doi}. Fetching from Crossref API...")
            result = fetch_from_crossref(doi)
            result['source_method'] = "Crossref_API" # Tag it!
            return result
        else:
            logger.info("No DOI found. Falling back to AI extraction...")

    except Exception as e:
        logger.error(f"Regex extraction failed: {e}")

    # STEP 2: Fallback to AI
    try:
        with open(pdf_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            text = "".join([reader.pages[i].extract_text() for i in range(3)])
            
        prompt = f"""
        Extract metadata from this text:
        1. Title
        2. Authors
        3. Year
        4. DOI (null if missing)

        Return JSON: {{"title": "...", "authors": "...", "year": "...", "doi": "..."}}
        TEXT: {text[:3000]}
        """
        
        response = ai_client.chat.completions.create(
            model=AIConfig.MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        result = json.loads(response.choices[0].message.content)
        result['source_method'] = "AI_Qwen" # Tag it!
        return result

    except Exception as e:
        return {"error": str(e)}

def fetch_from_crossref(doi):
    """
    Uses the official Crossref API.
    """
    try:
        url = f"https://api.crossref.org/works/{doi}"
        # This is the "Key" - the email address identifying the user
        headers = {'User-Agent': USER_AGENT_EMAIL} 
        response = requests.get(url, headers=headers)
        data = response.json()
        
        if data['status'] == 'ok':
            msg = data['message']
            return {
                "title": msg.get('title', ['Untitled'])[0],
                "authors": ", ".join([a.get('family', 'Unknown') for a in msg.get('author', [])]),
                "year": str(msg.get('published-print', msg.get('published-online', {})).get('date-parts', [[0]])[0][0]),
                "doi": doi
            }
        else:
            return {"error": f"Crossref failed for DOI: {doi}"}
            
    except Exception as e:
        return {"error": f"API Request Failed: {e}"}

if __name__ == "__main__":
    # Test with your file
    pdf_file = "data/raw/Darimont el al 2023 Communications Biology.pdf"
    if os.path.exists(pdf_file):
        result = extract_metadata_smart(pdf_file)
        print("✅ RESULT:")
        print(json.dumps(result, indent=4))
        
        # Save to CSV to see the source column
        import pandas as pd
        pd.DataFrame([result]).to_csv("data/interim/universal_metadata.csv", index=False)
        print("💾 Saved to CSV with 'source_method' column.")
