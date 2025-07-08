# Landsat-7 Data Processing Pipeline for Marine Researchers

## Overview

This repository provides a simple Python pipeline to download and process Landsat-7 data, designed for marine researchers with minimal coding background.

## Setup Instructions

1. Clone the repo:
   ```
   git clone https://github.com/yourusername/landsat-pipeline.git
   cd landsat-pipeline
   ```

2. Setup Python environment and install dependencies:
   ```bash
   ./setup_env.sh
   ```

3. Run download script to get Landsat-7 data:
   ```bash
   python scripts/download.py
   ```

4. Run processing script:
   ```bash
   python scripts/process.py
   ```

5. Run tests:
   ```bash
   pytest
   ```

## Folder Structure

- `data/raw/`: Raw Landsat-7 data (do not commit large files here)
- `data/processed/`: Processed outputs
- `scripts/`: Python scripts for download and processing
- `tests/`: Unit tests

## Code Quality

- Lint with `flake8`:
  ```
  flake8 scripts/
  ```

- Format code with `black`:
  ```
  black scripts/
  ```

---

## Notes

- Update `scripts/download.py` with actual data download code.
- Add processing logic in `scripts/process.py`.
- Extend tests as needed.
