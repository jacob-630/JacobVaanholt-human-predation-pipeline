# Human Predation Pipeline

**Project Type:** Systematic Review Data Pipeline & Database  
**Supervisor:** Prof. Chris Darimont (UVic)  
**Student:** Jacob Vaanholt  
**Date:** October 9, 2026

## 1. Scientific Context
This project constructs a reproducible, code-based pipeline for a systematic review of human predation success on wild vertebrates. 
The goal is to quantify capture efficiency across the entire predation sequence (detection -> harvest) and compare it with natural predation systems.

**Core Research Question:** How does the probability of successful human predation change across hunting stages and how does it vary with species, method, geography, and environment?

## 2. Methodology
The pipeline follows a strict PRISMA-based protocol (V2) but utilizes **Active Learning (ASReview)** and **LLM-based extraction** to maximize efficiency.

### Search Strategy
- **Concept:** Broad search using Process and Action terms; specific species terms are excluded to prevent discovery bias.
- **Scope:** North America (Canada + US), 1980–2026.
- **Taxa:** All wild vertebrates (Ungulates, Fish, Birds, Reptiles, Amphibians).

### Data Structure
The project uses a hierarchical database schema:
`Study` -> `Publication` -> `Observation` -> `Measurement`.
Raw numerators and denominators are preserved in all data tiers.

## 3. Repository Structure
- `docs/`: Protocol, Search Strings, and Metadata.
- `data/`: Raw PDFs, ASReview exports, and SQLite Database files.
- `src/`: Python scripts for Agents, Scrapers, and Extraction.
- `notebooks/`: Jupyter notebooks for data exploration and visualization.

## 4. Technical Stack
- **Language:** Python 3.10
- **Database:** SQLite (via SQLAlchemy)
- **AI Agents:** LangChain (for extraction and screening logic)
- **Environment:** Conda
- **Version Control:** Git/GitHub Actions

## 5. Installation
To replicate this environment, install Conda and run:
```bash
conda create -n predation-ai python=3.10
conda activate predation-ai
pip install -r requirements.txt

## Citation
if you use this data or code, please cite the subsequent manuscript
