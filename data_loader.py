import os
import pandas as pd

DATA_DIR = "data"

def get_csv_files():
    """Returns a list of CSV files in the data directory."""
    return [f for f in os.listdir(DATA_DIR) if f.endswith('.csv')]

def load_csv(file_name):
    """Loads a selected CSV file into a DataFrame."""
    file_path = os.path.join(DATA_DIR, file_name)
    return pd.read_csv(file_path) if os.path.exists(file_path) else None
