# Data Engineering Challenge

An implementation of core data engineering concepts using Python and SQL, with GitHub Codespaces integration.

## Objective
In this challenge, you are working as a Data Engineer for a retail banking company. Your task is to build an ETL (Extract, Transform, Load) pipeline that processes the bank’s transaction data. The company collects various transaction types, customer ages, and balances, and they need a system to extract this data from raw files, clean and transform it, and load it into a database for analysis.

You will be working with a dataset containing 100 rows of customer IDs, ages, transaction types, and balances, which is provided in the repository as `bank_transactions_dataset.csv`. Your task is to implement the ETL pipeline to process this data.

---

## Getting Started
1. **Fork this project** to create your own copy of the repository.
2. **Use GitHub Codespaces**:
   - Click on the green **Code** button in your forked repository.
   - Select **Codespaces** and choose "Create codespace on main" to open your development environment.

3. The repository includes a pre-configured `python.yml` file, which automatically sets up the Python environment in Codespaces.
   - **Ensure the Python version is correct**: Check that the `python.yml` file has the correct Python version for the project.
     You can update the `python.yml` file if necessary:
     ```yaml
     - name: Set up Python
       uses: actions/setup-python@v2
       with:
         python-version: '3.8'  # Adjust this version based on your project's needs
     ```

4. Once the Codespace is ready and the environment is set up, review the code in the `data_engineering/` folder to understand the structure.
5. Implement the missing functions marked with **TODO** comments.
6. Test your implementation by running the `main.py` file inside GitHub Codespaces.

---

## Files to Work On
- `data_engineering/extract.py`: Implement data extraction from the provided CSV file.
- `data_engineering/transform.py`: Implement data transformation logic (data cleaning, feature engineering).
- `data_engineering/load.py`: Implement loading the cleaned data into a SQLite database.
- `main.py`: Control the ETL pipeline and test your implementation.

---

## Requirements
- **`extract.py`**:
  - Implement the `extract_data` function to read the data from `bank_transactions_dataset.csv`.

- **`transform.py`**:
  - Implement the `transform_data` function to clean and transform the data (handle missing values, format changes, etc.).

- **`load.py`**:
  - Implement the `load_data` function to load the transformed data into a SQLite database.

- **`main.py`**:
  - Implement the pipeline flow (call extract, transform, and load functions).

---

## Steps to Follow
1. **Fork** the repository and set up your environment using **GitHub Codespaces**.
2. **extract.py**: Implement the logic to extract data from the `bank_transactions_dataset.csv`.
3. **transform.py**: Implement the transformation logic (e.g., handle missing values, data normalization).
4. **load.py**: Implement the loading logic to insert the cleaned data into a SQLite database.
5. Run the code inside **GitHub Codespaces** to test your implementation.

---

## Tips
- Make sure to handle different data types properly (e.g., strings, integers, floats).
- Use the SQLite library in Python to interact with the database.
- Ensure data quality checks are in place after the transformation step.

---

## Submission Guidelines
After completing the challenge, submit the link to your **forked GitHub repository** in the **LMS submission link text box**.

---

## Evaluation Criteria
- Correct implementation of the ETL pipeline (extract, transform, load).
- Proper handling of missing or invalid data.
- Accurate data insertion into the SQLite database.
- Clean and readable code with appropriate comments and structure.
- Successful execution of the project within **GitHub Codespaces**.

Good luck, and happy coding!
