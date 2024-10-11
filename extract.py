# data_engineering/extract.py

import pandas as pd

def extract_data(file_path):
    """
    Extracts data from a CSV file.

    Parameters:
    - file_path (str): Path to the CSV file.

    Returns:
    - pd.DataFrame: Extracted data.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Successfully extracted data from {file_path}")
        return df
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return pd.DataFrame()  # Return empty DataFrame on failure
    except pd.errors.ParserError:
        print(f"Error parsing {file_path}.")
        return pd.DataFrame()

