# tests/test_load.py

import pytest
import pandas as pd
import sqlite3
import os
from load import load_data

def test_load_data_success(tmp_path):
    # Sample data
    data = {
        "Customer_id": [1, 2],
        "Age": [0.0, 1.0],
        "Balance": [0.0, 1.0]
    }
    df = pd.DataFrame(data)

    # Define database path
    db_path = tmp_path / "test_bank_transactions.db"
    table_name = "transactions"

    # Call the load_data function
    load_data(df, db_name=str(db_path), table_name=table_name)

    # Connect to the database and verify data
    conn = sqlite3.connect(str(db_path))
    loaded_df = pd.read_sql_query(f"SELECT * FROM {table_name};", conn)
    conn.close()

    # Assertions
    assert not loaded_df.empty, "Loaded DataFrame should not be empty"
    assert len(loaded_df) == len(df), "Number of records loaded should match the input DataFrame"
    assert list(loaded_df.columns) == list(df.columns), "Table columns should match DataFrame columns"

def test_load_data_empty_dataframe(tmp_path):
    # Empty DataFrame
    df = pd.DataFrame()

    # Define database path
    db_path = tmp_path / "test_bank_transactions.db"
    table_name = "transactions"

    # Call the load_data function
    load_data(df, db_name=str(db_path), table_name=table_name)

    # Connect to the database and verify data
    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';")
    table_exists = cursor.fetchone()
    conn.close()

    # Assertions
    assert table_exists is None, "No table should be created when loading an empty DataFrame"
