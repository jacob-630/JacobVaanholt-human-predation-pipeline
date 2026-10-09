import os
import sys
import json
import pandas as pd
import PyPDF2
from openai import OpenAI
from dotenv import load_dotenv

# FIX PATHING: This ensures Python looks in the main folder to find 'src'
sys.path.insert(0, os.getcwd())

from src.utils.config import AIConfig
from src.utils.log_manager import get_logger

# 1. Setup the AI Brain
load_dotenv()
client = OpenAI(
    api_key=AIConfig.UVIC_API_KEY,
    base_url=AIConfig.UVIC_API_BASE
)

def extract_metadata_from_pdf(pdf_path):
    """
    The "First Step" of any systematic review. 
    Uses AI to pull Title, Authors, Year, and DOI to create a master index.
    """
    try:
        # FIX: Use standard library usage
        with open(pdf_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            text = ""
            # Extract text from the first 3 pages (where titles/abstracts usually are)
            for i, page in enumerate(reader.pages):
                if i > 2: break
                text += page.extract_text() + "\n"

        prompt = f"""
        You are a bibliographic data assistant. 
        Extract the following metadata from the text:
        1. 'title' (The full paper title)
        2. 'authors' (List of all authors)
        3. 'year' (Year of publication)
        4. 'doi' (Digital Object Identifier if present)

        RULES:
        - Return ONLY valid JSON.
        - If a field is missing, use null.
        
        TEXT: {text[:4000]}
        """

        # Run AI
        response = client.chat.completions.create(
            model=AIConfig.MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        
        # Clean JSON output (handle markdown backticks if present)
        raw_json = response.choices[0].message.content
        if raw_json.startswith("```"):
            raw_json = raw_json[7:-3] 
            
        return json.loads(raw_json)

    except Exception as e:
        # Return error to CSV if extraction fails
        return {"error": str(e), "file": pdf_path}

if __name__ == "__main__":
    logger = get_logger()
    logger.info("🚀 Starting Metadata Ingestion Protocol...")

    raw_folder = "data/raw"
    output_file = "data/interim/universal_metadata.csv"
    
    all_records = []

    if os.path.exists(raw_folder):
        for filename in os.listdir(raw_folder):
            if filename.endswith(".pdf"):
                path = os.path.join(raw_folder, filename)
                logger.info(f"📄 Processing {filename}...")
                data = extract_metadata_from_pdf(path)
                data['source_file'] = filename
                all_records.append(data)
    else:
        logger.error(f"Folder {raw_folder} not found.")

    if all_records:
        df = pd.DataFrame(all_records)
        df.to_csv(output_file, index=False)
        logger.info(f"✅ Ingestion Complete. {len(df)} records saved to {output_file}")
    else:
        logger.info("No records to save.")
