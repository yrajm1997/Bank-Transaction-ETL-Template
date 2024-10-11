# data_engineering/transform.py

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def transform_data(df):
    """
    Transforms the extracted data by cleaning and preparing it for loading.

    Parameters:
    - df (pd.DataFrame): Extracted data.

    Returns:
    - pd.DataFrame: Transformed data.
    """
    if df.empty:
        print("Empty DataFrame received for transformation.")
        return df

    # Step 1: Handle Missing Values
    df = handle_missing_values(df)

    # Step 2: Normalize Numerical Columns
    df = normalize_data(df, numerical_cols=['Age', 'Balance'])

    # Optional Step: Encode Categorical Columns (Uncomment if needed)
    # df = encode_categorical(df, categorical_cols=['transaction_type'])

    print("Data transformation completed.")
    return df

def handle_missing_values(df):
    """
    Handles missing values in the DataFrame by dropping rows with any missing data.

    Parameters:
    - df (pd.DataFrame): Data to clean.

    Returns:
    - pd.DataFrame: Cleaned data.
    """
    initial_count = len(df)
    df = df.dropna()
    final_count = len(df)
    dropped_rows = initial_count - final_count
    print(f"Dropped {dropped_rows} rows due to missing values.")
    return df

def normalize_data(df, numerical_cols):
    """
    Normalizes specified numerical columns using Min-Max scaling.

    Parameters:
    - df (pd.DataFrame): Data to normalize.
    - numerical_cols (list): List of numerical column names to normalize.

    Returns:
    - pd.DataFrame: Data with normalized columns.
    """
    scaler = MinMaxScaler()
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])
    print(f"Normalized columns: {', '.join(numerical_cols)}")
    return df

# Optional: Encode Categorical Columns
def encode_categorical(df, categorical_cols):
    """
    Encodes categorical variables using one-hot encoding.

    Parameters:
    - df (pd.DataFrame): Data to encode.
    - categorical_cols (list): List of categorical column names.

    Returns:
    - pd.DataFrame: Data with encoded categorical variables.
    """
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    print(f"Encoded categorical columns: {', '.join(categorical_cols)}")
    return df
