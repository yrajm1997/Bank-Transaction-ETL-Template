from extract import extract_data
from transform import transform_data
from load import load_data

def main():
    # File paths
    # csv_file = 'data/bank_transactions_dataset.csv'
    # db_name = 'etl_database.db'
    # table_name = 'cleaned_data'
    
    # # Step 1: Extract data
    # data = extract_data(csv_file)
    
    # if data is not None:
    #     # Step 2: Transform data
    #     cleaned_data = transform_data(data)
    #     print(cleaned_data.head())
    #     if cleaned_data is not None:
    #         # Step 3: Load data into the database
    #         load_data(cleaned_data, db_name, table_name)
    #         print("ETL process completed successfully!")
    #     else:
    #         print("Data transformation failed.")
    # else:
    #     print("Data extraction failed.")
    return

if __name__ == "__main__":
    main()
