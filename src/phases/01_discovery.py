import os
import sys
# CRITICAL FIX: Tell Python where the main project folder is
sys.path.insert(0, os.getcwd()) 

import pandas as pd
from pathlib import Path
from src.utils.log_manager import get_logger

def discover_and_standardize(raw_export_path, output_path="data/interim/screening_input.csv"):
    """
    PHASE 1: Paper Discovery & Metadata Standardization
    """
    logger = get_logger()
    logger.info("🔍 Starting Phase 1: Paper Discovery & Standardization")

    # 1. Load raw export
    suffix = Path(raw_export_path).suffix.lower()
    if suffix == '.csv':
        df = pd.read_csv(raw_export_path)
    elif suffix in ['.xlsx', '.xls']:
        df = pd.read_excel(raw_export_path)
    else:
        raise ValueError("❌ Unsupported format.")

    logger.info(f"📥 Loaded {len(df)} records from {os.path.basename(raw_export_path)}")

    # 2. Standardize column names (handle database variations)
    col_map = {}
    for col in df.columns:
        cl = col.lower().strip()
        if 'title' in cl: col_map[col] = 'title'
        if 'abstract' in cl: col_map[col] = 'abstract'
        if 'author' in cl and 'abstract' not in cl: col_map[col] = 'authors'
        if 'year' in cl or 'publication_year' in cl: col_map[col] = 'year'
        if 'doi' in cl: col_map[col] = 'doi'
    df = df.rename(columns=col_map)

    # 3. Add tracking columns
    df['source_database'] = os.path.basename(raw_export_path).split('.')[0]
    df['review_status'] = 'unknown'  # Required for ASReview

    # 4. Clean data
    df['title'] = df['title'].astype(str).replace('nan', '').replace('\\N', '')
    df['abstract'] = df['abstract'].astype(str).replace('nan', '').replace('\\N', '')
    df['year'] = pd.to_numeric(df['year'], errors='coerce').astype('Int64')
    df['authors'] = df['authors'].astype(str).replace('nan', '').replace('\\N', '')
    df['doi'] = df['doi'].astype(str).replace('nan', '').replace('\\N', '')

    # 5. Deduplicate
    logger.info("🗑️ Running deduplication protocol...")
    has_doi = df['doi'].str.len() > 0
    no_doi = ~has_doi

    df_deduped_doi = df[has_doi].drop_duplicates(subset=['doi'], keep='first')
    df_deduped_no_doi = df[no_doi].drop_duplicates(subset=['title', 'year'], keep='first')
    
    df_final = pd.concat([df_deduped_doi, df_deduped_no_doi], ignore_index=True)
    removed = len(df) - len(df_final)

    logger.info(f"✅ Deduplication complete: {len(df)} → {len(df_final)} records ({removed} removed)")

    # 6. Save
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df_final.to_csv(output_path, index=False)
    logger.info(f"💾 Saved standardized screening data to: {output_path}")
    return df_final

# --- TEST RUN SECTION (Creates a Mock Dataset) ---
if __name__ == "__main__":
    logger = get_logger()
    logger.info("🧪 Creating Mock Database Export for testing...")
    
    # This creates a fake export so you can test without real data yet
    mock_data = {
        'title': ['Human predation success in deer', 'Angler efficiency in trout fisheries', 'Wolf predation rates on elk'],
        'abstract': ['This study examines human predation...', 'Catch per unit effort...', 'Wolf predation rates...'],
        'authors': ['Darimont et al.', 'Smith & Jones', 'Wilmers et al.'],
        'year': [2023, 2021, 2018],
        'doi': ['10.1038/s41586-023-001', '', '10.1111/mec.2018.002']
    }
    pd.DataFrame(mock_data).to_csv("data/raw/mock_scopus_export.csv", index=False)
    
    # Run the pipeline on the fake data
    discover_and_standardize("data/raw/mock_scopus_export.csv")
