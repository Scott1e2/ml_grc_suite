
# data_loader.py - Unified Data Loading Utility for ML-GRC Suite

import pandas as pd
import json

def load_csv(file_path):
    """Load data from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        print(f"CSV data loaded successfully from {file_path}.")
        return data
    except Exception as e:
        raise Exception(f"Error loading CSV file: {e}")

def load_json(file_path):
    """Load data from a JSON file."""
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
        print(f"JSON data loaded successfully from {file_path}.")
        return data
    except Exception as e:
        raise Exception(f"Error loading JSON file: {e}")

def load_text(file_path):
    """Load data from a plain text file."""
    try:
        with open(file_path, "r") as file:
            data = file.read()
        print(f"Text data loaded successfully from {file_path}.")
        return data
    except Exception as e:
        raise Exception(f"Error loading text file: {e}")
