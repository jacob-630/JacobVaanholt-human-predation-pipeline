"""
Phase 2: Screening with ASReview LAB.

Usage (from project root, with the conda env active):
    python src/phases/02_screening.py              # prepare -> lab -> finalize
    python src/phases/02_screening.py prepare      # only build the import file
    python src/phases/02_screening.py lab          # only launch ASReview LAB
    python src/phases/02_screening.py finalize     # only build included_papers.csv
"""
import argparse
import subprocess
import sys
import threading
import time
import webbrowser
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
INTERIM = ROOT / "data" / "interim"

INPUT_CSV = INTERIM / "screening_input.csv"       # from Phase 1
IMPORT_CSV = INTERIM / "asreview_import.csv"      # you import THIS into ASReview
EXPORT_CSV = INTERIM / "asreview_export.csv"      # you export TO this path from ASReview
OUTPUT_CSV = INTERIM / "included_papers.csv"      # the "Gold List"

PORT = 5000


def prepare() -> None:
    if not INPUT_CSV.exists():
        sys.exit(f"Missing input file: {INPUT_CSV}")

    df = pd.read_csv(INPUT_CSV)
    for col in ("title", "abstract"):
        if col not in df.columns:
            sys.exit(f"Input CSV is missing required column: '{col}'")

    n_start = len(df)

    # Drop records with no usable text at all
    df = df.dropna(subset=["title", "abstract"], how="all")

    # De-duplicate (ASReview works best without duplicates): DOI first, then title
    if "doi" in df.columns:
        has_doi = df["doi"].notna()
        df = pd.concat([
            df[has_doi].drop_duplicates(subset="doi"),
            df[~has_doi],
        ]).sort_index()
    df = df.drop_duplicates(subset="title")

    missing_abs = df["abstract"].isna().sum()
    if missing_abs:
        print(f"Warning: {missing_abs} record(s) have no abstract "
              "(they are harder for the model to rank).")

    # NOTE: no label column is written. Unlabeled records are what ASReview
    # expects for a fresh screening; your decisions are recorded in the UI.
    df.to_csv(IMPORT_CSV, index=False)
    print(f"Prepared {len(df)} records (from {n_start}) -> {IMPORT_CSV}")


def lab() -> None:
    url = f"http://localhost:{PORT}"
    print(f"\nStarting ASReview LAB at {url}")
    print("Browser steps:")
    print(f"  1. Create a project and import: {IMPORT_CSV}")
    print("  2. Screen records (Include / Exclude)")
    print(f"  3. Export as CSV and save to: {EXPORT_CSV}")
    print("  4. Come back here and press Ctrl+C to shut the server down\n")

    # Open the browser ourselves, since LAB didn't do it for you
    threading.Thread(
        target=lambda: (time.sleep(4), webbrowser.open(url)), daemon=True
    ).start()

    # sys.executable guarantees the same conda env (predation-ai) is used
    proc = subprocess.Popen(
        [sys.executable, "-m", "asreview", "lab", "--port", str(PORT)]
    )
    try:
        proc.wait()
    except KeyboardInterrupt:
        proc.terminate()
        proc.wait()
    print("ASReview LAB stopped.")


def finalize() -> None:
    if not EXPORT_CSV.exists():
        sys.exit(
            f"Export not found: {EXPORT_CSV}\n"
            "In ASReview LAB click Export, choose CSV, and save it to that exact path."
        )

    df = pd.read_csv(EXPORT_CSV)

    # Different ASReview versions name the decision column differently
    label_col = next((c for c in ("included", "label") if c in df.columns), None)
    if label_col is None:
        sys.exit(f"No label column found. Columns in export: {list(df.columns)}")

    labels = pd.to_numeric(df[label_col], errors="coerce")
    df["review_status"] = "unknown"
    df.loc[labels == 1, "review_status"] = "include"
    df.loc[labels == 0, "review_status"] = "exclude"

    included = df[df["review_status"] == "include"]
    print(f"Included: {len(included)} | "
          f"Excluded: {(df['review_status'] == 'exclude').sum()} | "
          f"Unscreened: {(df['review_status'] == 'unknown').sum()}")

    included.to_csv(OUTPUT_CSV, index=False)
    print(f"Gold list written -> {OUTPUT_CSV}")


def main() -> None:
    p = argparse.ArgumentParser(description="Phase 2: ASReview screening")
    p.add_argument("step", nargs="?", default="all",
                   choices=["all", "prepare", "lab", "finalize"])
    step = p.parse_args().step

    if step in ("all", "prepare"):
        prepare()
    if step in ("all", "lab"):
        lab()
    if step in ("all", "finalize"):
        if EXPORT_CSV.exists():
            finalize()
        else:
            print(f"\nNo export at {EXPORT_CSV} yet. After exporting, run:\n"
                  "  python src/phases/02_screening.py finalize")


if __name__ == "__main__":
    main()
