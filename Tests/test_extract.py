# tests/test_extract.py

import pytest
import pandas as pd
from extract import extract_data

def test_extract_data_success(tmp_path):
    # Create a temporary CSV file
    test_csv = tmp_path / "test_bank_transactions_dataset.csv"
    data = {
        "Customer_id": [1, 2],
        "Age": [30, 45],
        "Transaction_type": ["deposit", "withdrawal"],
        "Balance": [1000.0, 2500.5]
    }
    df = pd.DataFrame(data)
    df.to_csv(test_csv, index=False)

    # Call the extract_data function
    extracted_df = extract_data(str(test_csv))

    # Assertions
    assert isinstance(extracted_df, pd.DataFrame), "extract_data should return a DataFrame"
    assert not extracted_df.empty, "DataFrame should not be empty"
    assert list(extracted_df.columns) == ["Customer_id", "Age", "Transaction_type", "Balance"], "DataFrame columns mismatch"

def test_extract_data_file_not_found():
    # Call the extract_data function with a non-existent file
    extracted_df = extract_data("non_existent_file.csv")

    # Assertions
    assert isinstance(extracted_df, pd.DataFrame), "extract_data should return a DataFrame even if file not found"
    assert extracted_df.empty, "DataFrame should be empty when file is not found"
