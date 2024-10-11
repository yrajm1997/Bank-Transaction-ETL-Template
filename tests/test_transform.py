# tests/test_transform.py

import pytest
import pandas as pd
from transform import transform_data

def test_transform_data_normalization():
    # Sample data
    data = {
        "Customer_id": [1, 2, 3],
        "Age": [25, 35, 45],
        "Balance": [1000.0, 2000.0, 3000.0]
    }
    df = pd.DataFrame(data)

    # Call the transform_data function
    transformed_df = transform_data(df)

    # Assertions
    assert "Age" in transformed_df.columns, "age column should exist after transformation"
    assert "Balance" in transformed_df.columns, "balance column should exist after transformation"

    # Check normalization: age and balance should be between 0 and 1
    assert transformed_df["Age"].min() == 0.0, "age column not normalized correctly"
    assert transformed_df["Age"].max() == 1.0, "age column not normalized correctly"
    assert transformed_df["Balance"].min() == 0.0, "balance column not normalized correctly"
    assert transformed_df["Balance"].max() == 1.0, "balance column not normalized correctly"

def test_transform_data_handle_missing_values():
    # Sample data with missing values
    data = {
        "Customer_id": [1, 2, 3],
        "Age": [25, None, 45],
        "Balance": [1000.0, 2000.0, None]
    }
    df = pd.DataFrame(data)

    # Call the transform_data function
    transformed_df = transform_data(df)

    # Assertions
    assert len(transformed_df) == 1, "Rows with missing values should be dropped"
    assert not transformed_df.isnull().values.any(), "There should be no missing values after transformation"
